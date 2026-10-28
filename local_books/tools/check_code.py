#!/usr/bin/env python3
"""Find Python code blocks that need a syntax review, without changing files.

Examples may intentionally be incomplete or invalid; compilation alone does
not prove transcription fidelity or establish runtime behavior.
"""
import ast
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = re.compile(r"^## PDF 第\s*(\d+)\s*页\s*$", re.MULTILINE)
BLOCK = re.compile(r"^(?P<fence>`{3,}|~{3,})(?:python|py)[ \t]*\n(?P<code>.*?)^(?P=fence)[ \t]*$", re.MULTILINE | re.DOTALL)

total = 0
failures = []
for book in (ROOT / "python-crash-course", ROOT / "python-data-analysis"):
    for path in sorted(book.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        pages = list(PAGE.finditer(text))
        for i, page in enumerate(pages):
            end = pages[i + 1].start() if i + 1 < len(pages) else len(text)
            content = text[page.end():end]
            if "<!-- page-status: reviewed -->" not in content:
                continue
            for block in BLOCK.finditer(content):
                total += 1
                try:
                    ast.parse(block.group("code"))
                except SyntaxError as exc:
                    failures.append((path.relative_to(ROOT), page.group(1), exc.msg, exc.lineno))
print(f"Checked {total} Python blocks on AI-reviewed pages; {len(failures)} require context inspection.")
for file, page, message, line in failures:
    print(f"{file} | PDF {page} | line {line}: {message}")
