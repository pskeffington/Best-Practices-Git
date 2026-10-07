#!/usr/bin/env python3
"""Deterministic linting for generated grant proposal packets."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def find_profile(text: str, profiles: dict, explicit: str | None) -> tuple[str, dict]:
    if explicit:
        return explicit, profiles[explicit]

    match = re.search(r"\*\*Sponsor profile:\*\*\s*\`?([a-z0-9_\-]+)\`?", text, re.I)
    if match and match.group(1) in profiles:
        key = match.group(1)
        return key, profiles[key]

    sponsor = ""
    match = re.search(r"\*\*Sponsor:\*\*\s*(.+)", text)
    if match:
        sponsor = match.group(1).lower()

    mechanism = ""
    match = re.search(r"\*\*Mechanism:\*\*\s*(.+)", text)
    if match:
        mechanism = match.group(1).lower()

    combined = f"{sponsor} {mechanism}"
    if any(token in combined for token in ("sbir", "sttr", "r41", "r42", "r43", "r44")):
        return "nih_small_business", profiles["nih_small_business"]
    if any(token in combined for token in ("nih", "nimh", "nida", "ninds", "nci", "niaid", "ahrq")):
        return "nih_rpg_srf", profiles["nih_rpg_srf"]
    if "nsf" in combined or "national science foundation" in combined:
        return "nsf_research", profiles["nsf_research"]
    if "samhsa" in combined:
        return "samhsa_discretionary", profiles["samhsa_discretionary"]
    return "generic_research", profiles["generic_research"]


def heading_present(text: str, name: str) -> bool:
    pattern = rf"^#{{1,6}}\s+.*{re.escape(name)}.*$"
    return re.search(pattern, text, flags=re.I | re.M) is not None


def section_text(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^#{{1,6}}\s+.*{re.escape(heading)}.*$\n(.*?)(?=^#{{1,6}}\s+|\Z)",
        flags=re.I | re.M | re.S,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def issue(level: str, code: str, message: str, section: str | None = None) -> dict:
    result = {"level": level, "code": code, "message": message}
    if section:
        result["section"] = section
    return result


def lint_text(path: Path, text: str, profiles: dict, explicit_profile: str | None) -> dict:
    profile_key, profile = find_profile(text, profiles, explicit_profile)
    issues: list[dict] = []

    if "Authoritative source:" not in text:
        issues.append(issue("error", "source.missing", "Authoritative opportunity source is not recorded."))

    if "Source verified:" not in text:
        issues.append(issue("error", "source.review_date_missing", "Source verification date is not recorded."))

    for section in profile.get("sections", []):
        required = section.get("required")
        name = section["name"]
        if required is True and not heading_present(text, name):
            issues.append(issue("error", "section.required_missing", f"Required sponsor section is missing: {name}", name))
        elif required == "conditional" and not heading_present(text, name):
            issues.append(issue("info", "section.conditional_missing", f"Conditional section not present: {name}", name))

    if not heading_present(text, "Reviewer crosswalk"):
        issues.append(issue("warning", "review.crosswalk_missing", "No reviewer-criteria crosswalk was found."))

    if not heading_present(text, "Claims-Aims-Evidence-Risk Matrix"):
        issues.append(issue("warning", "architecture.matrix_missing", "No claims/aims/evidence/risk matrix was found."))

    combined = text.lower()
    if "risk" not in combined:
        issues.append(issue("warning", "approach.risk_missing", "No explicit risk language was detected."))
    if not any(term in combined for term in ("alternative strategy", "alternative strategies", "contingency", "fallback")):
        issues.append(issue("warning", "approach.alternative_missing", "No alternative-strategy or contingency language was detected."))
    if not any(term in combined for term in ("milestone", "timeline", "go/no-go")):
        issues.append(issue("warning", "approach.milestone_missing", "No milestone, timeline, or go/no-go language was detected."))

    if profile_key.startswith("nih_"):
        aims = section_text(text, "Specific Aims")
        if not aims:
            issues.append(issue("error", "nih.aims_missing", "NIH profile requires a Specific Aims section.", "Specific Aims"))
        else:
            aim_count = len(re.findall(r"\bAim\s+\d+\b", aims, flags=re.I))
            if aim_count < 2:
                issues.append(issue("warning", "nih.aim_count_low", f"Only {aim_count} numbered aims detected; verify scope.", "Specific Aims"))
            if aim_count > 4:
                issues.append(issue("warning", "nih.aim_count_high", f"{aim_count} numbered aims detected; review for over-ambition.", "Specific Aims"))

            for signal in ("gap", "objective", "outcome", "impact"):
                if signal not in aims.lower():
                    issues.append(issue("warning", f"nih.aims_{signal}_missing", f"Specific Aims does not explicitly signal {signal}.", "Specific Aims"))

            if not any(term in aims.lower() for term in ("hypothesis", "premise")):
                issues.append(issue("warning", "nih.aims_premise_missing", "Specific Aims does not state a central hypothesis or premise.", "Specific Aims"))

    if profile_key == "nsf_research":
        summary = section_text(text, "Project Summary")
        for signal in ("overview", "intellectual merit", "broader impacts"):
            if signal not in summary.lower():
                issues.append(issue("warning", f"nsf.summary_{signal.replace(' ', '_')}_missing", f"Project Summary does not explicitly include {signal}.", "Project Summary"))

        project_description = section_text(text, "Project Description")
        if "broader impacts" not in project_description.lower():
            issues.append(issue("warning", "nsf.description_broader_impacts_missing", "Project Description should include an explicit Broader Impacts discussion.", "Project Description"))

    placeholder_patterns = [
        r"\[TODO[^\]]*\]",
        r"\bTBD\b",
        r"\bUNKNOWN\b",
        r"\[AMOUNT\]",
        r"\[NAME\]",
    ]
    placeholder_count = sum(len(re.findall(p, text, flags=re.I)) for p in placeholder_patterns)
    if placeholder_count:
        issues.append(issue("warning", "draft.placeholders", f"{placeholder_count} unresolved placeholder(s) detected."))

    if "## Budget" not in text and "Budget" not in text:
        issues.append(issue("warning", "budget.missing", "No budget or budget-alignment section detected."))

    if not any(term in combined for term in ("citation", "references", "evidence manifest", "literature")):
        issues.append(issue("warning", "evidence.traceability_missing", "No citation/evidence traceability language detected."))

    errors = sum(1 for item in issues if item["level"] == "error")
    warnings = sum(1 for item in issues if item["level"] == "warning")

    return {
        "path": str(path),
        "profile": profile_key,
        "profileLabel": profile.get("label"),
        "errors": errors,
        "warnings": warnings,
        "issues": issues,
        "pass": errors == 0,
    }


def gather_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(
        path for path in target.rglob("*.md")
        if path.name.lower() not in {"readme.md"} and "literature_review" not in path.name.lower()
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Grant Markdown file or directory")
    parser.add_argument("--profiles", default="grants/sponsor-profiles.json")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--json-out", default=None)
    parser.add_argument("--fail-on-warning", action="store_true")
    args = parser.parse_args()

    profile_data = load_json(args.profiles)
    profiles = profile_data["profiles"]
    files = gather_files(Path(args.target))

    reports = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        reports.append(lint_text(path, text, profiles, args.profile))

    summary = {
        "schemaVersion": "grant-lint-report.v1",
        "files": len(reports),
        "errors": sum(item["errors"] for item in reports),
        "warnings": sum(item["warnings"] for item in reports),
        "pass": all(item["pass"] for item in reports),
        "reports": reports,
    }

    rendered = json.dumps(summary, indent=2) + "\n"
    print(rendered)
    if args.json_out:
        output = Path(args.json_out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")

    if summary["errors"]:
        return 1
    if args.fail_on_warning and summary["warnings"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
