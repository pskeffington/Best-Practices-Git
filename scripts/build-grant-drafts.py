#!/usr/bin/env python3
"""Build provenance-preserving, sponsor-aware grant draft packets."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime, timezone
from pathlib import Path


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9._-]+", "-", value.lower()).strip("-")


def days_old(value: str | None, today: date) -> int | None:
    parsed = parse_date(value)
    return None if parsed is None else (today - parsed).days


def infer_profile_key(grant: dict) -> str:
    combined = " ".join(
        str(grant.get(key, "")) for key in ("sponsor", "mechanism", "title")
    ).lower()

    if any(token in combined for token in ("sbir", "sttr", "r41", "r42", "r43", "r44")):
        return "nih_small_business"
    if "nsf" in combined or "national science foundation" in combined:
        return "nsf_research"
    if "samhsa" in combined:
        return "samhsa_discretionary"
    if any(token in combined for token in ("nih", "nimh", "nida", "ninds", "nci", "niaid", "ahrq")):
        return "nih_rpg_srf"
    return "generic_research"


def eligible(grant: dict, registry: dict, cfg: dict, today: date) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    review = grant.get("lastVerified") or registry.get("updated")
    age = days_old(review, today)

    if age is None:
        reasons.append("missing/invalid source review date")
    elif age > int(cfg["freshnessDays"]):
        reasons.append(f"source review is {age} days old")

    due = parse_date(grant.get("nextDue"))
    if due and due < today:
        reasons.append("deadline has passed")

    if grant.get("draftHold") is True:
        reasons.append("explicit draft hold")

    if grant.get("status") not in set(cfg["allowedStatuses"]):
        reasons.append(f"status {grant.get('status')} is not draft-enabled")

    if int(grant.get("fitScore", -1)) < int(cfg["draftThreshold"]):
        reasons.append(f"fit score below {cfg['draftThreshold']}")

    if not grant.get("source"):
        reasons.append("missing authoritative source")

    if not grant.get("applicantRoute") or not grant.get("directEligibility"):
        reasons.append("applicant route unresolved")

    return (not reasons, reasons)


def review_crosswalk(profile: dict) -> str:
    rows = [
        "| Review factor | Scoring | Primary proposal location | Reviewer question |",
        "|---|---|---|---|",
    ]
    for item in profile.get("reviewFramework", []):
        maps = ", ".join(item.get("mapsTo", []))
        rows.append(
            f"| {item.get('factor', '')} | {item.get('score', '')} | {maps} | {item.get('reviewQuestion', '')} |"
        )
    return "\n".join(rows)


def section_requirements(profile: dict) -> str:
    rows = [
        "| Section | Required | Page rule | Required signals |",
        "|---|---|---|---|",
    ]
    for section in profile.get("sections", []):
        required = section.get("required")
        required_label = "yes" if required is True else str(required)
        signals = "; ".join(section.get("requiredSignals", []))
        rows.append(
            f"| {section['name']} | {required_label} | {section.get('pageRule', '')} | {signals} |"
        )
    return "\n".join(rows)


def proposal_sections(profile_key: str, profile: dict) -> str:
    blocks: list[str] = []

    for section in profile.get("sections", []):
        name = section["name"]

        if profile_key.startswith("nih_") and name == "Specific Aims":
            continue
        if profile_key == "nsf_research" and name in {"Project Summary", "Broader Impacts"}:
            continue

        signals = "; ".join(section.get("requiredSignals", []))
        block = [f"## {name}"]
        if section.get("pageRule"):
            block.append(f"**Page rule:** {section['pageRule']}")
        if signals:
            block.append(f"**Required signals:** {signals}.")
        block.append(
            "[TODO: draft from verified evidence and the live opportunity instructions. "
            "Replace this instruction with proposal prose before submission.]"
        )

        if profile_key == "nsf_research" and name == "Project Description":
            block.append(
                "### Broader Impacts\n\n"
                "[TODO: define concrete broader-impact activities, target participants or beneficiaries, "
                "responsible roles, milestones, and evaluation. Keep this discussion inside the Project Description.]"
            )

        blocks.append("\n\n".join(block))

    return "\n\n".join(blocks)

def aims_architecture(profile_key: str) -> str:
    if profile_key not in {"nih_rpg_srf", "nih_small_business"}:
        return ""

    return """## Specific Aims

**Problem:** [TODO: state the important problem or unmet need in one direct sentence.]

**Gap:** [TODO: state the precise knowledge, implementation, or technical gap that prevents progress.]

**Overall objective:** [TODO: state what this project will accomplish within the award period.]

**Central hypothesis or premise:** [TODO: state the testable hypothesis or defensible premise. If the mechanism is not hypothesis-driven, state the governing premise explicitly.]

### Aim 1 — [TODO: bounded objective]

State the objective, rationale, core method, measurable endpoint, and expected outcome. The aim should remain scientifically useful even if the result is null or the preferred implementation path fails.

### Aim 2 — [TODO: bounded objective]

State the objective, rationale, core method, measurable endpoint, and expected outcome. Do not make this aim depend completely on success of Aim 1.

### Aim 3 — [TODO: bounded objective or omit if unnecessary]

Use only if the scope, budget, and award period support a third aim. Avoid adding an aim merely to make the application look complete.

**Expected outcomes:** [TODO: summarize the concrete scientific, technical, implementation, or access outcomes.]

**Overall impact:** [TODO: explain how completing these aims changes the field, service system, technical capability, or public-health problem.]
"""


def project_summary_architecture(profile_key: str) -> str:
    if profile_key != "nsf_research":
        return ""
    return """## Project Summary

### Overview

[TODO: concise overview of the problem, objectives, and work.]

### Intellectual Merit

[TODO: explain the potential to advance knowledge and the core scientific/technical contribution.]

### Broader Impacts

[TODO: define specific societal/educational/public-benefit activities, target participants or beneficiaries, implementation ownership, and how success will be evaluated.]
"""


def claims_matrix(profile_key: str) -> str:
    unit = "Aim" if profile_key.startswith("nih_") else "Objective"
    return f"""## Claims-Aims-Evidence-Risk Matrix

| {unit} | Claim or premise | Existing evidence | Proposed test/work | Risk | Alternative strategy | Deliverable | Budget owner |
|---|---|---|---|---|---|---|---|
| {unit} 1 | [TODO] | [TODO: citation/pilot/source] | [TODO] | [LOW/MED/HIGH] | [TODO] | [TODO] | [TODO] |
| {unit} 2 | [TODO] | [TODO: citation/pilot/source] | [TODO] | [LOW/MED/HIGH] | [TODO] | [TODO] | [TODO] |
| {unit} 3 | [TODO or omit] | [TODO] | [TODO] | [LOW/MED/HIGH] | [TODO] | [TODO] | [TODO] |

A high-risk row requires either an alternative strategy, a go/no-go milestone, or an explicit justification for accepting the risk.
"""


def render(project: str, grant: dict, registry: dict, today: date, profile_key: str, profile: dict) -> str:
    gates = "\n".join(f"- [ ] {item}" for item in grant.get("gates", []))
    policy = "\n".join(f"- {item}" for item in grant.get("policyNotes", [])) or "- None recorded."
    blockers = "\n".join(f"- [ ] {item}" for item in grant.get("currentBlockers", [])) or "- [ ] Reconcile mechanism-specific blockers with the current source."
    due = grant.get("nextDue") or "Rolling / not currently specified"
    verified = grant.get("lastVerified") or registry.get("updated") or "unknown"
    writing_rules = "\n".join(f"- {item}" for item in profile.get("writingRules", []))
    draft_order = " -> ".join(profile.get("draftOrder", []))
    authoritative = "\n".join(f"- {item}" for item in profile.get("sources", [])) or "- Live opportunity instructions only."
    sponsor_sections = section_requirements(profile)
    aims = aims_architecture(profile_key)
    nsf_summary = project_summary_architecture(profile_key)
    matrix = claims_matrix(profile_key)
    crosswalk = review_crosswalk(profile)

    return f"""<!-- AUTOGENERATED GRANT DRAFT. Rebuild from source registry; do not hand-edit this file. -->

# {grant["title"]}

**Project:** {project}  
**Sponsor:** {grant["sponsor"]}  
**Mechanism:** {grant["mechanism"]}  
**Sponsor profile:** `{profile_key}`  
**Strategic fit:** {grant["fitScore"]}/100  
**Application route:** {grant["applicantRoute"]}  
**Deadline:** {due}  
**Source verified:** {verified}  
**Draft generated:** {today.isoformat()}  
**Authoritative source:** {grant["source"]}

## Drafting status

This is a pre-submission drafting packet generated only after the opportunity passed portfolio freshness, timing, fit, and applicant-route gates. It is not evidence that the project is eligible, that the sponsor will accept the application, or that unresolved partner and institutional requirements have been satisfied.

The live funding opportunity and current sponsor application instructions override this generated profile.

## Working project summary

{registry.get("thesis", project)}

For this mechanism, the working case is:

{grant["rationale"]}

## Eligibility and applicant structure

{grant["directEligibility"]}

Before narrative language is promoted into a submission, confirm the legal applicant, principal investigator or project lead, institutional registrations, partner roles, and any mechanism-specific restrictions against the current sponsor instructions.

## Sponsor-specific proposal architecture

**Profile:** {profile.get("label", profile_key)}  
**Recommended drafting order:** {draft_order}

### Writing rules

{writing_rules}

### Profile source controls

{authoritative}

{aims}
{nsf_summary}
{matrix}
## Reviewer crosswalk

{crosswalk}

Use this crosswalk as a coverage check, not as a substitute for the live NOFO review criteria.

## Sponsor section requirements

{sponsor_sections}

## Approach integration rules

For every aim, objective, or work package:

- define the rationale and responsible role;
- identify the evidence supporting feasibility;
- specify the method or activity;
- define measurable endpoints or acceptance criteria;
- state the expected outcome;
- identify the major risk;
- provide an alternative strategy or go/no-go decision rule;
- map the work to timeline and budget.

## Required gates

{gates}

## Current blockers

{blockers}

## Budget Alignment

**Current registry value:** {grant["budget"]}  
**Duration:** {grant["duration"]}

Build the budget from the work plan rather than fitting the work plan to an arbitrary total. Each major activity should map to personnel effort, partner/subaward effort, infrastructure, evaluation, dissemination, or another allowable category. Flag work packages with no budget owner and budget lines with no narrative purpose.

## Human Subjects and Other Required Plans

**Registry clinical-trial classification:** {grant["clinicalTrial"]}

Do not infer exemption, institutional-review requirements, clinical-trial status, data-sharing obligations, or other regulatory classifications from this generated packet. Reconcile the current protocol, institutional guidance, and sponsor definitions before submission.

## Policy and mechanism notes

{policy}

## Evidence and citation controls

Before narrative promotion:

- map quantitative claims to verified citations or project data;
- map preliminary-data claims to a source artifact;
- separate literature-supported need from intervention-effectiveness claims;
- verify that cited evidence is current enough for the claim;
- do not generate or retain a citation that cannot be resolved to a real source;
- preserve a source/retrieval date for sponsor rules and funding-opportunity facts.

## Evidence-to-manuscript handoff

The proposal should reuse the same evidence controls as a publishable manuscript:

- source registry with retrieval/review dates;
- citation verification log;
- explicit analysis protocol;
- data provenance;
- prespecified outcomes;
- limitations and claim boundaries;
- reproducible tables/figures;
- change/audit trail connecting proposal claims to eventual results.

If funded, create a project-specific manuscript branch at award activation rather than reconstructing methods retrospectively.

## Final pre-submission controls

- [ ] Re-open the authoritative opportunity page.
- [ ] Confirm the opportunity remains active.
- [ ] Confirm deadline, time zone, and submission portal.
- [ ] Confirm applicant eligibility and registrations.
- [ ] Confirm current forms, page limits, review criteria, and attachments.
- [ ] Confirm sponsor-profile assumptions against the live opportunity.
- [ ] Reconcile aims/objectives, milestones, budget, evaluation endpoints, and partner letters.
- [ ] Resolve every placeholder and blocker.
- [ ] Run `scripts/grant_lint.py`.
- [ ] Run citation, privacy, statistical, budget, and claim-boundary review.
- [ ] Run a final reviewer-style critique using the actual scored review criteria.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="grants/pipeline-config.json")
    parser.add_argument("--profiles", default="grants/sponsor-profiles.json")
    parser.add_argument("--registry", action="append", default=[], help="project=path")
    parser.add_argument("--output", default="grants/generated")
    args = parser.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    profile_data = json.loads(Path(args.profiles).read_text(encoding="utf-8"))
    profiles = profile_data["profiles"]
    today = datetime.now(timezone.utc).date()
    out_root = Path(args.output)
    out_root.mkdir(parents=True, exist_ok=True)

    index = {
        "schemaVersion": "grant-draft-index.v2",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "draftThreshold": cfg["draftThreshold"],
        "freshnessDays": cfg["freshnessDays"],
        "profileVersion": profile_data.get("schemaVersion"),
        "drafts": [],
        "held": [],
    }

    for item in args.registry:
        project, path = item.split("=", 1)
        registry = json.loads(Path(path).read_text(encoding="utf-8"))
        reg_age = days_old(registry.get("updated"), today)
        if reg_age is None or reg_age > int(cfg["freshnessDays"]):
            raise SystemExit(f"{project}: registry is missing a current review date")

        project_dir = out_root / slug(project)
        project_dir.mkdir(parents=True, exist_ok=True)

        for grant in registry.get("opportunities", []):
            ok, reasons = eligible(grant, registry, cfg, today)
            profile_key = grant.get("sponsorProfile") or infer_profile_key(grant)
            if profile_key not in profiles:
                reasons.append(f"unknown sponsor profile: {profile_key}")
                ok = False

            record = {
                "project": project,
                "id": grant.get("id"),
                "title": grant.get("title"),
                "fitScore": grant.get("fitScore"),
                "status": grant.get("status"),
                "source": grant.get("source"),
                "nextDue": grant.get("nextDue"),
                "sponsorProfile": profile_key,
            }

            if not ok:
                record["reasons"] = reasons
                index["held"].append(record)
                continue

            target = project_dir / f"{slug(grant['id'])}.md"
            target.write_text(
                render(project, grant, registry, today, profile_key, profiles[profile_key]),
                encoding="utf-8",
            )
            record["path"] = str(target)
            index["drafts"].append(record)

    (out_root / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(index, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
