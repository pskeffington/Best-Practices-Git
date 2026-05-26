# Journal Use Guide

## Purpose

This guide explains how journals, editors, reviewers, and authors can use the query-to-publication scaffold as a reviewer-readable evidence package for machine-learning manuscripts.

## Core journal-use claim

Machine-learning manuscripts should not ask reviewers to reconstruct the evidence chain from prose, code, and scattered supplementary materials. Authors should provide a compact package that links each major claim to evidence artifacts, validation context, limitations, and reproducibility materials.

## Recommended submission package

A journal-ready submission should include:

```text
manuscript.pdf
manuscript.tex or manuscript source
references.bib
artifacts/results/result-bundle.md
artifacts/validation/validation-plan.md
artifacts/reproducibility/reproducibility-package.md
artifacts/reviewer/reviewer-report.md
artifacts/reviewer/reviewer-report.json
artifacts/audits/latest-audit.md
artifacts/audits/latest-audit.json
```

## Author responsibilities

Authors should provide:

- a clear research query,
- data provenance statement,
- model and baseline description,
- validation design,
- metric rationale,
- evidence-to-claim register,
- claim-boundary notes,
- reproducibility package,
- reviewer report.

## Reviewer responsibilities

Reviewers can use the reviewer report to ask:

- Are the claims traceable to evidence artifacts?
- Are validation results aligned with claim strength?
- Are generalization claims supported by external validation?
- Are causal claims avoided unless the design supports them?
- Are data provenance and feature construction described?
- Are reproducibility materials adequate for review?
- Does the manuscript need minor revision, major revision, or rejection on workflow grounds?

## Editor responsibilities

Editors can use the audit package for triage before sending a manuscript to specialist reviewers.

Suggested triage interpretation:

| Status | Editorial meaning |
|---|---|
| `REVIEW_READY` | The package is complete enough for substantive peer review. |
| `MINOR_REVISION` | The manuscript can proceed, but authors should address limited workflow gaps. |
| `MAJOR_REVISION` | The manuscript has significant workflow or evidence-chain gaps. |
| `NOT_REVIEW_READY` | The manuscript should not proceed to full review until core evidence artifacts are supplied. |

## Minimum reviewer-readable checks

A journal-facing audit should check:

1. research query clarity,
2. data provenance,
3. feature transparency,
4. baseline comparison,
5. validation adequacy,
6. metric alignment,
7. claim support,
8. claim-boundary language,
9. reproducibility artifacts,
10. ethics and use limitations.

## Recommended journal policy language

For machine-learning manuscripts, authors are encouraged to submit a reviewer-readable evidence package that links each major claim to supporting artifacts, validation results, and limitation language. The package should include a machine-readable reviewer report, an audit report, and sufficient reproducibility materials to evaluate the evidence chain.

## Why this matters

The framework reduces reviewer burden by making the scientific workflow inspectable. It does not replace peer review. It gives peer review a structured map from manuscript claims to evidence.
