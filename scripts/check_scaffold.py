#!/usr/bin/env python3
"""CLI for checking a biomedical research project scaffold."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from best_practices_git.scaffold_validation import validate_scaffold

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Path to a research project")
    parser.add_argument("--output", type=Path, help="Optional JSON evidence report destination")
    args = parser.parse_args()
    result = validate_scaffold(args.root)
    report = json.dumps({"schema": "bpg-scaffold-check-v1", **result}, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    print(report, end="")
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
