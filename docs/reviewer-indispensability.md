# Reviewer Indispensability Strategy

## Goal

Make the framework useful enough that journal reviewers, editors, and methods reviewers want authors to provide it with machine-learning manuscripts.

The drop-in should answer the reviewer's core question:

> Can I trace this manuscript's claims back to evidence, validation, artifacts, and limitations without reconstructing the entire project myself?

## Reviewer-facing value proposition

A reviewer should be able to inspect one report and quickly determine:

- what the model was intended to do,
- which claims are being made,
- what evidence supports each claim,
- whether the validation design supports the claim strength,
- whether artifacts are present,
- whether boundary language prevents overclaiming,
- whether reproducibility materials are sufficient for review,
- whether the manuscript should be accepted, revised, or rejected on workflow grounds.

## The reviewer report

The key output should be a reviewer-facing report, separate from the author-facing run record.

Recommended files:

```text
artifacts/reviewer/reviewer-report.md
artifacts/reviewer/reviewer-report.json
```

## Reviewer score dimensions

A useful reviewer report should score or flag the following dimensions:

1. Query clarity
2. Data provenance
3. Feature transparency
4. Baseline comparison
5. Validation adequacy
6. Metric alignment
7. Claim support
8. Claim boundary language
9. Reproducibility artifacts
10. Ethics and use limitations

## Decision categories

The report should not replace peer review, but it should support triage.

Recommended status labels:

- `REVIEW_READY`
- `MINOR_REVISION`
- `MAJOR_REVISION`
- `NOT_REVIEW_READY`

## Reviewer red flags

The system should explicitly flag:

- no baseline comparison,
- no validation artifact,
- performance claims without metrics,
- generalization claims without external validation,
- deployment claims without ethics or use-boundary review,
- causal language without causal design,
- missing data provenance,
- claims without evidence paths,
- artifacts referenced but not present,
- missing reproducibility instructions.

## Why reviewers would cite it

The contribution is not merely that authors can track their own work. The key contribution is that reviewers can evaluate the scientific evidence chain quickly and consistently.

A reviewer-facing workflow layer creates a common language for manuscript readiness:

```text
Claim -> Evidence -> Validation -> Boundary -> Artifact -> Reviewer finding
```

## Manuscript claim

The paper should argue that ML manuscripts need reviewer-readable evidence packages, not only author-controlled code repositories. The reviewer package should expose claim support, validation adequacy, and reproducibility readiness in a compact, auditable form.
