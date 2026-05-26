#!/usr/bin/env python3
"""Inject a local/private author profile into a LaTeX manuscript.

This script is intended for local submission builds. The generated personalized
TeX output is ignored by Git and should not be committed to the public repo.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def load_author_block(profile_path: Path) -> str:
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    author_block = profile.get("latex", {}).get("author_block")
    if not author_block:
        raise ValueError("Profile is missing latex.author_block")
    return str(author_block)


def inject_author_block(tex: str, author_block: str) -> str:
    pattern = r"\\author\{.*?\}"
    if not re.search(pattern, tex, flags=re.S):
        raise ValueError("No LaTeX author block found")
    return re.sub(pattern, author_block, tex, count=1, flags=re.S)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inject private author metadata into local LaTeX build source.")
    parser.add_argument("--profile", required=True, help="Path to private author profile JSON")
    parser.add_argument("--input", required=True, help="Path to public/template LaTeX manuscript")
    parser.add_argument("--output", required=True, help="Path to local personalized LaTeX output")
    args = parser.parse_args()

    profile_path = Path(args.profile)
    input_path = Path(args.input)
    output_path = Path(args.output)

    author_block = load_author_block(profile_path)
    tex = input_path.read_text(encoding="utf-8")
    output_tex = inject_author_block(tex, author_block)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_tex, encoding="utf-8")
    print(f"Wrote personalized local manuscript: {output_path}")


if __name__ == "__main__":
    main()
