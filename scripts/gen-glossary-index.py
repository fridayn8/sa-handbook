#!/usr/bin/env python3
"""Regenerate the A–Z index in architecture/glossary.md.

Reads every `### Term — Full name` heading under a `## N. Category` heading and writes an
alphabetical table between the `<!-- INDEX:START -->` and `<!-- INDEX:END -->` markers.

Usage:
    python3 scripts/gen-glossary-index.py
"""
import re
import sys
from pathlib import Path

GLOSSARY = Path(__file__).resolve().parent.parent / "architecture" / "glossary.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"


def github_slug(heading: str, seen: dict) -> str:
    """Approximate GitHub's heading anchor algorithm."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)  # drop punctuation (keeps letters, digits, _, -, space)
    slug = slug.replace(" ", "-")
    count = seen.get(slug, 0)
    seen[slug] = count + 1
    return slug if count == 0 else f"{slug}-{count}"


def main() -> int:
    text = GLOSSARY.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("Index markers not found", file=sys.stderr)
        return 1

    seen: dict = {}
    category = ""
    rows = []
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6}) (.+)$", line)
        if not m:
            continue
        level, title = len(m.group(1)), m.group(2).strip()
        slug = github_slug(title, seen)
        if level == 2:
            category = re.sub(r"^\d+\.\s*", "", title)
        elif level == 3 and category:
            term, _, full = title.partition(" — ")
            rows.append((term.strip(), full.strip() or "—", category, slug))

    rows.sort(key=lambda r: r[0].lower())
    table = [
        f"## Index (A–Z) — {len(rows)} entries",
        "",
        "| Term | Full name | Category |",
        "|------|-----------|----------|",
    ]
    table += [f"| [{t}](#{s}) | {f} | {c} |" for t, f, c, s in rows]

    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    GLOSSARY.write_text(before + START + "\n\n" + "\n".join(table) + "\n\n" + END + after, encoding="utf-8")
    print(f"Index written: {len(rows)} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
