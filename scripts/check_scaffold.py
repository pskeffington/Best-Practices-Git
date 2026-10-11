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
    args = parser.parse_args()
    result = validate_scaffold(args.root)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
