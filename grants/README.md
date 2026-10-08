# Grant-to-Manuscript Pipeline

_Last updated: 2026-10-07_

This directory is the portfolio-level compiler for grant opportunities that are mature enough to enter proposal drafting.

## Architecture

Source repositories remain authoritative for project-specific opportunity research:

- `mh.institute/data/grants/opportunities.json`
- `gaming.institute/data/grants/opportunities.json`

Best-Practices-Git does not replace those registries. It consumes reviewed records, binds each opportunity to a sponsor profile, generates a structured proposal packet, runs deterministic lint checks, and keeps the eventual funded protocol connected to the manuscript pipeline.

Core controls:

- `LITERATURE_REVIEW.md` — review of grant-compilation patterns, open-source tooling, published grantsmanship literature, and official sponsor guidance.
- `WRITING_STANDARD.md` — proposal-writing rules used across projects.
- `ROADMAP.md` — gated milestone progression from opportunity intake through submission and award handoff.
- `REVIEW_PIPELINE.md` — specialist reviewer contract, packet generation, validation, and synthesis.
- `roadmap.json` — machine-readable gate state for automation/HUD use.
- `sponsor-profiles.json` — machine-readable NIH, NIH SBIR/STTR, NSF, SAMHSA, and generic proposal architecture/review rules.
- `pipeline-config.json` — portfolio ingestion and drafting thresholds.
- `../scripts/build-grant-drafts.py` — deterministic sponsor-aware scaffold compiler.
- `../scripts/grant_lint.py` — pre-review proposal linter.

## Current roadmap status

**Overall:** `G8 IN PROGRESS / G8.3 NEXT`

The compiler foundation, admission/freshness controls, sponsor binding, deterministic draft generation, and lint gates are active. G8 now has structured reviewer schemas, nine specialist profiles, immutable review packets, result validation, and panel aggregation. The next execution gate is G8.3: the explicit model/provider invocation adapter. See `ROADMAP.md` for G0-G14 progression.

## Draft admission gates

An opportunity is auto-drafted only when all of the following are true:

1. the source registry review date is no more than 14 days old;
2. the opportunity has a current authoritative source URL;
3. the deadline has not passed;
4. the status is `target-now`, `next-cycle`, or `partner-led`;
5. strategic fit is at least 85/100;
6. an applicant route and eligibility description exist;
7. no explicit `draftHold` is present;
8. a valid sponsor profile can be resolved.

A high fit score never overrides eligibility, geography, partner, clinical-trial, registration, or sponsor-specific gates.

## Sponsor-aware drafting

The compiler infers or accepts an explicit sponsor profile.

Current profiles:

- `nih_rpg_srf` — NIH research project grants using the Simplified Review Framework where applicable;
- `nih_small_business` — NIH SBIR/STTR;
- `nsf_research` — NSF research proposals;
- `samhsa_discretionary` — SAMHSA discretionary opportunities;
- `generic_research` — foundations/state/local/research opportunities until a more specific profile exists.

The live opportunity and current sponsor instructions always override these profiles.

## Generated packet

Each draft includes:

- sponsor/mechanism provenance;
- sponsor profile;
- fit, deadline, and review date;
- applicant structure;
- sponsor-specific drafting order;
- aims/objectives architecture where applicable;
- claims-aims-evidence-risk matrix;
- reviewer-criteria crosswalk;
- section-level required signals;
- risk/alternative-strategy expectations;
- required gates and current blockers;
- budget-to-work alignment rules;
- human-subjects/clinical-trial boundary;
- citation/evidence controls;
- evidence-to-manuscript handoff;
- final pre-submission checklist.

The generator preserves unknowns as unresolved controls rather than fabricating application facts.

## Deterministic lint

Run:

`python scripts/grant_lint.py grants/generated --profiles grants/sponsor-profiles.json`

The linter checks:

- authoritative source and review date;
- required sponsor sections;
- Specific Aims architecture for NIH profiles;
- NSF Project Summary signals;
- reviewer crosswalk;
- claims/evidence/risk matrix;
- risk and alternative strategies;
- milestones/timeline language;
- unresolved placeholders;
- budget and evidence-traceability surfaces.

Errors fail the automated drafting workflow. Warnings remain visible for human review.

## Automation

`.github/workflows/grant-draft-pipeline.yml` runs daily and can also be dispatched manually.

It:

1. reads current grant registries from the source repositories;
2. runs the sponsor-aware deterministic draft compiler;
3. runs the proposal linter;
4. stores `grants/generated/lint-report.json`;
5. opens a pull request when the generated queue changes.

### Required repository secret

For private sibling repositories, configure:

`PORTFOLIO_GRANT_READ_TOKEN`

The token needs read access to the source repositories. The workflow's normal `GITHUB_TOKEN` remains responsible for writing the generated branch and pull request in Best-Practices-Git.

## Review rule

Generated files are inputs to proposal development, not submission-ready documents.

Promotion to an application requires:

1. live opportunity re-verification;
2. sponsor-profile reconciliation;
3. aims/objectives structural review;
4. literature and citation review;
5. methods/feasibility review;
6. budget/timeline/team consistency review;
7. reviewer-criteria review;
8. institutional and human approval.

## Manuscript handoff

If an award activates, immediately connect the funded protocol to the existing query-to-publication pipeline:

`proposal -> protocol -> data provenance -> modeling/evaluation -> validation -> ethics -> manuscript -> submission`

This keeps grant claims, study methods, eventual results, and publication claims on one traceable audit path.
