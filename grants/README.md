# Grant-to-Manuscript Pipeline

_Last updated: 2026-10-07_

This directory is the portfolio-level compiler for grant opportunities that are mature enough to enter proposal drafting.

## Architecture

Source repositories remain authoritative for project-specific opportunity research:

- `mh.institute/data/grants/opportunities.json`
- `gaming.institute/data/grants/opportunities.json`

Best-Practices-Git does not replace those registries. It consumes reviewed records and generates standardized proposal packets under `grants/generated/`.

## Draft admission gates

An opportunity is auto-drafted only when all of the following are true:

1. the source registry review date is no more than 14 days old;
2. the opportunity has a current authoritative source URL;
3. the deadline has not passed;
4. the status is `target-now`, `next-cycle`, or `partner-led`;
5. strategic fit is at least 85/100;
6. an applicant route and eligibility description exist;
7. no explicit `draftHold` is present.

A high fit score never overrides eligibility, geography, partner, clinical-trial, or institutional-registration gates.

## Generated packet

Each draft includes:

- sponsor/mechanism provenance;
- fit, deadline, and review date;
- applicant structure;
- aims/objectives scaffold;
- significance, innovation, approach, and evaluation scaffolds;
- required gates and current blockers;
- budget frame;
- human-subjects/clinical-trial boundary;
- policy notes;
- evidence-to-manuscript handoff controls;
- final pre-submission checklist.

The generator deliberately preserves unknowns as unresolved controls rather than fabricating application facts.

## Automation

`.github/workflows/grant-draft-pipeline.yml` runs daily and can also be dispatched manually.

It:

1. reads current grant registries from the source repositories;
2. runs the deterministic draft compiler;
3. updates `grants/generated/`;
4. opens a pull request when the generated queue changes.

### Required repository secret

For private sibling repositories, configure:

`PORTFOLIO_GRANT_READ_TOKEN`

The token needs read access to the source repositories. The workflow's normal `GITHUB_TOKEN` remains responsible for writing the generated branch and pull request in Best-Practices-Git.

## Review rule

Generated files are inputs to proposal development, not submission-ready documents. Promotion to a real application requires a human-controlled branch and review against the live sponsor instructions, institutional requirements, source evidence, budget, partners, and current forms.

## Manuscript handoff

If an award activates, the project should immediately connect the funded protocol to the existing query-to-publication pipeline:

`protocol -> data provenance -> modeling/evaluation -> validation -> ethics -> manuscript -> submission`

This keeps grant claims, study methods, eventual results, and publication claims on one traceable audit path.
