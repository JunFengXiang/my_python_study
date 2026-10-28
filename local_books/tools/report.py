#!/usr/bin/env python3
"""Report page markers and local links in the private conversion drafts.

An AI-reviewed marker is a progress record, not proof of human review or of
executable code. This script does not alter the converted books.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = re.compile(r"^## PDF 第\s*(\d+)\s*页\s*$", re.MULTILINE)
REVIEWED = "<!-- page-status: reviewed -->"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def ranges(numbers):
    result = []
    for n in sorted(set(numbers)):
        if result and n == result[-1][-1] + 1:
            result[-1].append(n)
        else:
            result.append([n])
    return "、".join(str(g[0]) if len(g) == 1 else f"{g[0]}–{g[-1]}" for g in result) or "无"


def scan_book(name, directory, expected):
    seen = {}
    reviewed = []
    missing = []
    contradictions = []
    for path in sorted(directory.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        for link in LINK.findall(content):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = link.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                missing.append(f"{path.relative_to(ROOT)}: {link}")
        matches = list(PAGE.finditer(content))
        for index, match in enumerate(matches):
            page = int(match.group(1))
            end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
            chunk = content[match.end():end]
            seen.setdefault(page, []).append(str(path.relative_to(ROOT)))
            if REVIEWED in chunk:
                reviewed.append(page)
                if re.search(r"展开(?:机器|自动)提取文字.*未校对", chunk):
                    contradictions.append(page)
    duplicates = {k: v for k, v in seen.items() if len(v) > 1}
    absent = expected - set(seen)
    unexpected = set(seen) - expected
    print(f"{name}: pages={len(seen)}, ai_reviewed={len(set(reviewed))}, pending={len(seen)-len(set(reviewed))}")
    print(f"  reviewed PDF pages: {ranges(reviewed)}")
    print(f"  missing links={len(missing)}, duplicate pages={len(duplicates)}, missing pages={len(absent)}, unexpected pages={len(unexpected)}")
    if contradictions:
        print(f"  reviewed pages containing unreviewed extraction blocks: {ranges(contradictions)}")
    if absent:
        print(f"  missing PDF pages: {ranges(absent)}")
    if unexpected:
        print(f"  unexpected PDF pages: {ranges(unexpected)}")
    for item in missing[:10]:
        print(f"  missing: {item}")
    for page, files in list(duplicates.items())[:10]:
        print(f"  duplicate page {page}: {files}")
    return bool(missing or duplicates or absent or unexpected or contradictions)


if __name__ == "__main__":
    failures = [
        scan_book("Python编程", ROOT / "python-crash-course", (set(range(43, 336)) | set(range(339, 448)) | set(range(449, 547)) | set(range(548, 727))) - {247}),
        scan_book("Python数据分析", ROOT / "python-data-analysis", set(range(17, 509))),
    ]
    raise SystemExit(1 if any(failures) else 0)
