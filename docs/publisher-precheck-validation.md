# Publisher Pre-Check Validation Guide

## Purpose

This framework can be used as an early validation tool for publishers handling machine-learning manuscripts. It is not a replacement for peer review. It is a pre-review quality-control layer that helps editors determine whether a submission is complete enough to send to reviewers.

## Core publisher value

A publisher should be able to answer three questions before full peer review:

1. Is the manuscript package complete enough for technical review?
2. Are major claims linked to evidence artifacts and validation context?
3. Are there obvious workflow gaps that should be fixed before reviewers spend time on the submission?

## Recommended use point

The pre-check should run during editorial intake, before external peer review.

Recommended sequence:

```text
Submission received
  -> package completeness check
  -> ML evidence pre-check
  -> reviewer-readable report generated
  -> editor triage decision
  -> peer review or return-to-author
```

## Publisher-facing statuses

| Status | Meaning | Recommended editorial action |
|---|---|---|
| `PRECHECK_PASS` | Package is complete enough for technical review. | Send to peer review. |
| `PRECHECK_MINOR` | Limited missing or weak elements, but review can proceed. | Send to review or request small clarification. |
| `PRECHECK_MAJOR` | Substantial evidence-chain gaps. | Return to authors before full review. |
| `PRECHECK_FAIL` | Package lacks core evidence or reproducibility materials. | Do not send to full review until corrected. |

## Minimum publisher pre-check dimensions

1. Manuscript source present
2. References present
3. Research query identifiable
4. Data provenance described
5. Methods and model family described
6. Baseline or comparator described
7. Validation design described
8. Metrics reported
9. Evidence artifacts present
10. Major claims linked to evidence
11. Boundary language present
12. Reproducibility package present
13. Ethics or use-limit statement present when relevant

## Publisher red flags

The pre-check should flag:

- no data provenance statement,
- no baseline or comparator,
- no validation design,
- performance claims without metrics,
- generalization claims without external validation,
- causal claims without causal design,
- deployment claims without deployment evidence,
- missing reproducibility materials,
- claims not linked to evidence,
- artifacts referenced but not included.

## Intake package recommendation

Publishers can request that authors upload:

```text
manuscript source or PDF
references file
reviewer report JSON
reviewer report Markdown
audit report JSON
audit report Markdown
result bundle
validation plan
reproducibility package
claim register
```

## Safe policy wording

Publishers may use language such as:

> Machine-learning submissions may be screened using an automated or semi-automated evidence pre-check. This process does not replace peer review. It evaluates whether the submission includes sufficient documentation, evidence artifacts, validation context, and reproducibility materials for reviewers to assess the manuscript efficiently.

## Why this is useful

The tool reduces reviewer burden by detecting preventable evidence-chain failures before review. It also creates consistent editorial language for return-to-author decisions when a manuscript lacks the materials needed for technical evaluation.

## Journal-use boundary

The pre-check should not determine scientific truth, novelty, clinical utility, policy value, or final acceptability. It should only assess whether the submitted evidence package is adequate for review.
