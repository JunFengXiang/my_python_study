"""从 Markdown 生成 PDF；显示公式以 SVG 路径嵌入，正文可选取。"""
from html import escape
from io import BytesIO
import json
import re
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from svglib.svglib import svg2rlg
import ziamath

# PDF converters do not consistently implement SVG 2 symbol/use geometry.
# Emit explicit paths so fractions, scripts and inline glyphs keep their positions.
ziamath.config.svg2 = False

ROOT = Path(__file__).resolve().parent


def main():
    markdown = "\n\n".join((ROOT / name).read_text(encoding="utf-8") for name in ["homework.md", "optional.md"])
    ast = json.loads(subprocess.run(["pandoc", "-f", "markdown", "-t", "json"], input=markdown, text=True, capture_output=True, check=True).stdout)
    font = "STSong-Light"
    pdfmetrics.registerFont(UnicodeCIDFont(font))
    pdfmetrics.registerFontFamily(font, normal=font, bold=font, italic=font, boldItalic=font)
    styles = {
        "body": ParagraphStyle("body", fontName=font, fontSize=10.5, leading=18, autoLeading="max", wordWrap=None, spaceAfter=5),
        "h1": ParagraphStyle("h1", fontName=font, fontSize=20, leading=28, spaceAfter=14, keepWithNext=True),
        "h2": ParagraphStyle("h2", fontName=font, fontSize=13, leading=21, spaceBefore=12, spaceAfter=7, keepWithNext=True),
        "cell": ParagraphStyle("cell", fontName=font, fontSize=10, leading=17, autoLeading="max", wordWrap=None, alignment=TA_CENTER),
    }
    story = []
    page_width = A4[0] - 112
    with tempfile.TemporaryDirectory() as temp:
        counter = 0

        def math_asset(tex, inline=False):
            nonlocal counter
            tex = re.sub(r"\\\\\[[0-9.]+pt\]", r"\\\\", tex)
            math = ziamath.Latex(tex, size=10.8 if inline else 12, inline=inline)
            root = math.svgxml()
            width, height = float(root.attrib["width"]), float(root.attrib["height"])
            root.set("width", f"{width}pt")
            root.set("height", f"{height}pt")
            svg = ET.tostring(root)
            if not inline:
                drawing = svg2rlg(BytesIO(svg))
                if drawing.width > page_width:
                    scale = page_width / drawing.width
                    drawing.scale(scale, scale)
                    drawing.width *= scale
                    drawing.height *= scale
                drawing.hAlign = "CENTER"
                return drawing
            counter += 1
            path = Path(temp) / f"math-{counter}.png"
            source = fitz.open(stream=svg, filetype="svg")
            rendered = fitz.open("pdf", source.convert_to_pdf())
            rendered[0].get_pixmap(matrix=fitz.Matrix(4, 4), alpha=True).save(path)
            return f'<img src="{path}" width="{width:.3f}" height="{height:.3f}" valign="{math.getyofst()-1:.3f}"/>'

        def inlines(nodes):
            parts = []
            for node in nodes:
                kind, value = node["t"], node.get("c")
                if kind == "Str":
                    parts.append(escape(value))
                elif kind in ["Space", "SoftBreak"]:
                    parts.append(" ")
                elif kind == "LineBreak":
                    parts.append("<br/>")
                elif kind == "Math":
                    parts.append(math_asset(value[1], inline=True))
                elif kind in ["Strong", "Emph"]:
                    tag = "b" if kind == "Strong" else "i"
                    parts.append(f"<{tag}>" + inlines(value) + f"</{tag}>")
                elif kind == "Code":
                    parts.append(escape(value[1]))
                elif kind == "Quoted":
                    parts.append("“" + inlines(value[1]) + "”")
                else:
                    raise ValueError(f"Unhandled inline node: {kind}")
            return "".join(parts)

        def table_cell(cell):
            return Paragraph(" ".join(inlines(block["c"]) for block in cell[4]), styles["cell"])

        first_heading = True
        for block in ast["blocks"]:
            kind, content = block["t"], block.get("c")
            if kind == "Header":
                level, _, text = content
                if level == 1 and not first_heading:
                    story.append(PageBreak())
                story.append(Paragraph(inlines(text), styles["h1" if level == 1 else "h2"]))
                first_heading = False
            elif kind in ["Para", "Plain"]:
                if len(content) == 1 and content[0]["t"] == "Math" and content[0]["c"][0]["t"] == "DisplayMath":
                    story.extend([Spacer(1, 4), math_asset(content[0]["c"][1]), Spacer(1, 7)])
                else:
                    story.append(Paragraph(inlines(content), styles["body"]))
            elif kind == "Table":
                rows = content[3][1][:]
                for body in content[4]:
                    rows.extend(body[2])
                    rows.extend(body[3])
                rows.extend(content[5][1])
                data = [[table_cell(cell) for cell in row[1]] for row in rows]
                table = Table(data, colWidths=[page_width / len(data[0])] * len(data[0]), repeatRows=1)
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f2f5")),
                    ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#c6cdd6")),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ]))
                story.extend([Spacer(1, 7), table, Spacer(1, 9)])
            else:
                raise ValueError(f"Unhandled block: {kind}")
        output = ROOT / "数值分析第3章作业解答.pdf"
        doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=56, rightMargin=56, topMargin=48, bottomMargin=48, title="数值分析第3章作业解答")

        def page_number(canvas, document):
            canvas.setFont("Helvetica", 9)
            canvas.setFillColor(colors.HexColor("#666666"))
            canvas.drawCentredString(A4[0] / 2, 25, str(document.page))

        # Keep each short exercise together; longer ones may still break naturally.
        grouped, section = [], []
        for flowable in story:
            boundary = isinstance(flowable, PageBreak) or (
                isinstance(flowable, Paragraph) and flowable.style.name in {"h1", "h2"}
            )
            if boundary and section:
                grouped.append(KeepTogether(section))
                section = []
            if isinstance(flowable, Paragraph) and flowable.style.name == "h2":
                section.append(flowable)
            elif section:
                section.append(flowable)
            else:
                grouped.append(flowable)
        if section:
            grouped.append(KeepTogether(section))
        doc.build(grouped, onFirstPage=page_number, onLaterPages=page_number)
    print(output)


if __name__ == "__main__":
    main()
