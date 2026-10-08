#!/usr/bin/env python3
"""Build reviewer-specific packets for grant proposal critique."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9._-]+", "-", value.lower()).strip("-")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sponsor_profile(text: str) -> str:
    match = re.search(r"\*\*Sponsor profile:\*\*\s*\`?([a-z0-9_-]+)\`?", text, re.I)
    return match.group(1) if match else "unknown"


def proposal_title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback


def render_packet(draft_path: Path, draft_text: str, reviewer: dict, sponsor: str, title: str) -> str:
    focus = "\n".join(f"- {item}" for item in reviewer.get("focus", []))
    categories = ", ".join(reviewer.get("categories", []))
    runs_after = ", ".join(reviewer.get("runsAfter", [])) or "none"

    return f"""# Grant Review Packet — {reviewer["label"]}

**Reviewer ID:** {reviewer["id"]}  
**Proposal:** {title}  
**Draft path:** {draft_path}  
**Draft SHA-256:** {sha256_text(draft_text)}  
**Sponsor profile:** {sponsor}  
**Allowed finding categories:** {categories}  
**Blocking reviewer:** {"yes" if reviewer.get("blocking") else "no"}  
**Runs after:** {runs_after}

## Reviewer role

Act as an independent grant reviewer. Review the proposal itself; do not rewrite it wholesale.

Your job is to identify material weaknesses that could affect eligibility, reviewer confidence, score, feasibility, compliance, or submission readiness.

## Focus

{focus}

## Review rules

1. Anchor every finding to a proposal section and, where possible, a short locator or phrase.
2. Do not invent sponsor rules, citations, preliminary data, partner commitments, regulatory classifications, or budget facts.
3. If a fact cannot be verified from the draft or source material, identify it as unresolved rather than assuming it is true.
4. Distinguish a writing weakness from a scientific/design weakness.
5. Use the actual sponsor review logic represented in the proposal's reviewer crosswalk.
6. Give a concrete verification method for every proposed revision.
7. Use **critical** severity only for issues that should stop promotion.
8. Use **HOLD** if there is an unresolved critical issue, eligibility/compliance failure, unverifiable evidence, or material scientific/regulatory uncertainty.
9. Use **REVISE** for substantive but repairable weaknesses.
10. Use **PASS** only when no critical/high findings remain and the proposal is credible within this reviewer's scope.

## Required output contract

Return one JSON object conforming to:

`grants/reviewer-finding.schema.json`

Required top-level fields:

- `schemaVersion`: `grant-review-result.v1`
- `reviewerId`: `{reviewer["id"]}`
- `reviewerLabel`: `{reviewer["label"]}`
- `draftPath`: `{draft_path}`
- `draftSha256`: `{sha256_text(draft_text)}`
- `sponsorProfile`: `{sponsor}`
- `decision`: `PASS`, `REVISE`, or `HOLD`
- `confidence`: `high`, `medium`, or `low`
- `criterionCoverage`: 0-100 when this reviewer can judge it
- `summary`
- `findings`

Each finding must include:

- stable finding `id`;
- `severity`;
- `category`;
- optional `reviewCriterion`;
- `evidenceAnchor.section`;
- optional `evidenceAnchor.quoteOrLocator`;
- `problem`;
- `reviewerImpact`;
- `recommendedRevision`;
- `verificationMethod`;
- optional `fundingConstraintNote`;
- `status` = `open` for a new review.

## Proposal under review

---

{draft_text}
"""


def gather_drafts(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(
        p for p in target.rglob("*.md")
        if "review-packets" not in p.parts and p.name.lower() not in {"readme.md", "review-synthesis.md"}
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Draft Markdown file or directory")
    parser.add_argument("--reviewers", default="grants/reviewer-profiles.json")
    parser.add_argument("--output", default="grants/generated/review-packets")
    args = parser.parse_args()

    reviewer_data = json.loads(Path(args.reviewers).read_text(encoding="utf-8"))
    reviewers = reviewer_data["reviewers"]
    out_root = Path(args.output)
    out_root.mkdir(parents=True, exist_ok=True)

    manifest = {
        "schemaVersion": "grant-review-packet-manifest.v1",
        "reviewerProfileVersion": reviewer_data.get("schemaVersion"),
        "packets": [],
    }

    for draft in gather_drafts(Path(args.target)):
        text = draft.read_text(encoding="utf-8")
        sponsor = sponsor_profile(text)
        title = proposal_title(text, draft.stem)
        draft_key = slug(str(draft.with_suffix("")))
        draft_dir = out_root / draft_key
        draft_dir.mkdir(parents=True, exist_ok=True)

        for reviewer in reviewers:
            packet_path = draft_dir / f"{reviewer['id'].lower()}.md"
            packet = render_packet(draft, text, reviewer, sponsor, title)
            packet_path.write_text(packet, encoding="utf-8")
            manifest["packets"].append(
                {
                    "draftPath": str(draft),
                    "draftSha256": sha256_text(text),
                    "sponsorProfile": sponsor,
                    "reviewerId": reviewer["id"],
                    "packetPath": str(packet_path),
                    "blocking": bool(reviewer.get("blocking")),
                    "runsAfter": reviewer.get("runsAfter", []),
                }
            )

    (out_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
