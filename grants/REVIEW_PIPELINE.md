# Specialist Grant Review Pipeline

_Last updated: 2026-10-08_

This directory-level review system implements the structured critique stage between deterministic lint and controlled revision.

## Review model

The review system deliberately separates specialist perspectives.

Current reviewers:

1. `R1_COMPLIANCE` — eligibility and compliance;
2. `R2_AIMS` — aims/objectives architecture;
3. `R3_SIGNIFICANCE` — significance and literature positioning;
4. `R4_INNOVATION` — innovation;
5. `R5_METHODS` — methods, rigor, feasibility, and risk;
6. `R6_EVIDENCE` — citations and evidence provenance;
7. `R7_OPERATIONS` — budget, timeline, team, and partner coherence;
8. `R8_READABILITY` — readability and reviewer navigation;
9. `R9_PANEL` — final panel synthesis.

The panel reviewer is downstream of the focused reviewers. It should not erase disagreement among specialist passes.

## Structured finding contract

`reviewer-finding.schema.json` defines the expected result shape.

A finding contains:

- stable ID;
- severity;
- category;
- sponsor review criterion when applicable;
- section/locator evidence anchor;
- problem;
- expected reviewer impact;
- recommended revision;
- verification method;
- optional funding-constraint note;
- resolution status.

Top-level decisions are:

- **PASS** — no critical/high findings remain within reviewer scope;
- **REVISE** — material but repairable weaknesses remain;
- **HOLD** — critical, eligibility/compliance, unverifiable-evidence, or material scientific/regulatory issue blocks promotion.

## Packet generation

Run:

`python scripts/build-grant-review-packets.py <draft-or-directory>`

The command creates one immutable review packet per specialist and records the draft SHA-256. Every specialist therefore reviews the same proposal version.

The scheduled grant workflow now builds these packets after deterministic lint and uploads them as the `grant-review-packets` workflow artifact.

## Review result ingestion

Reviewer outputs should be saved as JSON conforming to the schema.

Then run:

`python scripts/aggregate-grant-reviews.py <review-results-directory>`

The aggregator checks:

- reviewer IDs are known;
- reviewer IDs are unique;
- all results refer to the same draft path;
- all available hashes refer to the same draft version;
- sponsor profile is consistent;
- result fields and finding fields are complete;
- missing panel members are explicit.

The synthesis produces:

- `review-synthesis.json`;
- `review-synthesis.md`;
- severity counts;
- missing-reviewer list;
- complete-panel flag;
- consolidated open findings;
- overall PASS / REVISE / HOLD.

## Promotion rule

A proposal cannot advance to controlled automated revision merely because one reviewer passes it.

Promotion requires:

- deterministic lint passes;
- all required specialist reviews are present;
- no unresolved critical finding;
- no blocking reviewer returns HOLD;
- draft hashes agree;
- panel synthesis is available.

## Current boundary

The repository now creates deterministic review packets and can validate/aggregate structured reviewer results.

The actual model/provider invocation layer is still gated. It must be added explicitly rather than embedding an untracked LLM call in CI. When that layer is added, it must preserve:

- model/provider/version;
- reviewer profile version;
- prompt packet hash;
- response hash;
- token/cost metadata when available;
- retry/error status;
- no silent draft mutation.
