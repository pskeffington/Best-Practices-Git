#!/usr/bin/env python3
"""Validate the private author profile object used by submission builds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "schema_version",
    "object_type",
    "profile_id",
    "display_name",
    "affiliation",
    "latex",
]

REQUIRED_LATEX = [
    "author_block",
    "authors_contributions",
    "authors_information",
]


def validate_profile(profile: dict[str, object]) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in profile:
            errors.append(f"Missing top-level field: {key}")
    if profile.get("object_type") != "author_profile":
        errors.append("object_type must be author_profile")
    latex = profile.get("latex")
    if not isinstance(latex, dict):
        errors.append("latex must be an object")
        return errors
    for key in REQUIRED_LATEX:
        value = latex.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"Missing or empty latex field: {key}")
    author_block = latex.get("author_block", "")
    if "\\author{" not in author_block:
        errors.append("latex.author_block must contain a LaTeX author command")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate author profile JSON for manuscript builds.")
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()

    profile_path = Path(args.profile)
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    errors = validate_profile(profile)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"Author profile valid: {profile_path}")


if __name__ == "__main__":
    main()
