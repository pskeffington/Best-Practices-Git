#!/usr/bin/env python3
"""Validate and consolidate structured grant-review results."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


SEVERITY_RANK = {
    "critical": 5,
    "high": 4,
    "medium": 3,
    "low": 2,
    "info": 1,
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def basic_validate(result: dict) -> list[str]:
    errors: list[str] = []
    required = [
        "schemaVersion",
        "reviewerId",
        "reviewerLabel",
        "draftPath",
        "sponsorProfile",
        "decision",
        "confidence",
        "summary",
        "findings",
    ]
    for key in required:
        if key not in result:
            errors.append(f"missing {key}")

    if result.get("schemaVersion") != "grant-review-result.v1":
        errors.append("unsupported schemaVersion")

    if result.get("decision") not in {"PASS", "REVISE", "HOLD"}:
        errors.append("invalid decision")

    if result.get("confidence") not in {"high", "medium", "low"}:
        errors.append("invalid confidence")

    findings = result.get("findings")
    if not isinstance(findings, list):
        errors.append("findings must be an array")
        return errors

    ids: set[str] = set()
    for idx, finding in enumerate(findings):
        prefix = f"finding[{idx}]"
        for key in (
            "id",
            "severity",
            "category",
            "evidenceAnchor",
            "problem",
            "reviewerImpact",
            "recommendedRevision",
            "verificationMethod",
            "status",
        ):
            if key not in finding:
                errors.append(f"{prefix}: missing {key}")

        finding_id = finding.get("id")
        if finding_id in ids:
            errors.append(f"{prefix}: duplicate id {finding_id}")
        if finding_id:
            ids.add(finding_id)

        if finding.get("severity") not in SEVERITY_RANK:
            errors.append(f"{prefix}: invalid severity")

        if finding.get("status") not in {"open", "resolved", "accepted-risk"}:
            errors.append(f"{prefix}: invalid status")

        anchor = finding.get("evidenceAnchor")
        if not isinstance(anchor, dict) or not anchor.get("section"):
            errors.append(f"{prefix}: evidenceAnchor.section required")

    return errors


def derive_decision(results: list[dict], blocking_ids: set[str]) -> str:
    open_findings = [
        (result, finding)
        for result in results
        for finding in result.get("findings", [])
        if finding.get("status") == "open"
    ]

    if any(f.get("severity") == "critical" for _, f in open_findings):
        return "HOLD"

    if any(
        result.get("reviewerId") in blocking_ids and result.get("decision") == "HOLD"
        for result in results
    ):
        return "HOLD"

    if any(
        f.get("severity") in {"high", "medium"}
        for _, f in open_findings
    ):
        return "REVISE"

    if any(result.get("decision") == "REVISE" for result in results):
        return "REVISE"

    return "PASS"


def render_markdown(summary: dict) -> str:
    lines = [
        "# Grant Review Synthesis",
        "",
        f"**Decision:** {summary['decision']}  ",
        f"**Reviews:** {summary['reviewCount']}  ",
        f"**Open findings:** {summary['openFindingCount']}  ",
        f"**Critical:** {summary['severityCounts']['critical']}  ",
        f"**High:** {summary['severityCounts']['high']}  ",
        f"**Medium:** {summary['severityCounts']['medium']}",
        "",
        "## Reviewer decisions",
        "",
        "| Reviewer | Decision | Confidence | Coverage |",
        "|---|---|---|---:|",
    ]

    for result in summary["reviews"]:
        coverage = result.get("criterionCoverage")
        lines.append(
            f"| {result['reviewerId']} | {result['decision']} | {result['confidence']} | "
            f"{'' if coverage is None else coverage} |"
        )

    lines.extend(["", "## Open findings", ""])

    if not summary["openFindings"]:
        lines.append("- None.")
    else:
        for finding in summary["openFindings"]:
            lines.extend(
                [
                    f"### {finding['severity'].upper()} — {finding['id']}",
                    "",
                    f"**Reviewer:** {finding['reviewerId']}  ",
                    f"**Category:** {finding['category']}  ",
                    f"**Section:** {finding['evidenceAnchor'].get('section', '')}",
                    "",
                    f"**Problem:** {finding['problem']}",
                    "",
                    f"**Reviewer impact:** {finding['reviewerImpact']}",
                    "",
                    f"**Recommended revision:** {finding['recommendedRevision']}",
                    "",
                    f"**Verification:** {finding['verificationMethod']}",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", help="Directory containing reviewer JSON results")
    parser.add_argument("--reviewers", default="grants/reviewer-profiles.json")
    parser.add_argument("--json-out", default="grants/generated/review-synthesis.json")
    parser.add_argument("--md-out", default="grants/generated/review-synthesis.md")
    args = parser.parse_args()

    reviewer_data = load(Path(args.reviewers))
    blocking_ids = {
        item["id"] for item in reviewer_data["reviewers"] if item.get("blocking")
    }

    result_paths = sorted(Path(args.results).rglob("*.json"))
    results: list[dict] = []
    validation_errors: list[dict] = []

    for path in result_paths:
        result = load(path)
        errors = basic_validate(result)
        if errors:
            validation_errors.append({"path": str(path), "errors": errors})
        else:
            result["_path"] = str(path)
            results.append(result)

    if validation_errors:
        print(json.dumps({"valid": False, "validationErrors": validation_errors}, indent=2))
        return 1

    if not results:
        print(json.dumps({"valid": False, "error": "no valid review results found"}, indent=2))
        return 1

    open_findings = []
    severity_counts = {key: 0 for key in SEVERITY_RANK}

    for result in results:
        for finding in result.get("findings", []):
            if finding.get("status") != "open":
                continue
            severity_counts[finding["severity"]] += 1
            enriched = dict(finding)
            enriched["reviewerId"] = result["reviewerId"]
            open_findings.append(enriched)

    open_findings.sort(
        key=lambda item: (-SEVERITY_RANK[item["severity"]], item["reviewerId"], item["id"])
    )

    decision = derive_decision(results, blocking_ids)

    summary = {
        "schemaVersion": "grant-review-synthesis.v1",
        "decision": decision,
        "reviewCount": len(results),
        "openFindingCount": len(open_findings),
        "severityCounts": severity_counts,
        "blockingReviewerIds": sorted(blocking_ids),
        "reviews": [
            {
                "reviewerId": r["reviewerId"],
                "reviewerLabel": r["reviewerLabel"],
                "decision": r["decision"],
                "confidence": r["confidence"],
                "criterionCoverage": r.get("criterionCoverage"),
                "summary": r["summary"],
                "sourcePath": r["_path"],
            }
            for r in results
        ],
        "openFindings": open_findings,
    }

    json_path = Path(args.json_out)
    md_path = Path(args.md_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(summary), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
