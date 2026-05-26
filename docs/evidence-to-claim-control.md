# Evidence-to-Claim Control Framework

## Purpose

Machine-learning manuscripts often fail when claims become stronger than the evidence produced by the workflow. This framework creates a traceable link between pipeline artifacts, evidence strength, manuscript claims, and publication language.

## Core principle

```text
No manuscript claim should be stronger than the artifact chain that supports it.
```

The artifact chain should show:

```text
Research decision -> Evidence artifact -> Validation check -> Claim boundary -> Manuscript language
```

## Claim levels

| Claim level | Evidence required | Acceptable language | Risk if unsupported |
|---|---|---|---|
| Descriptive | Documented data audit or summary table | The sample shows, the dataset contains, observed patterns indicate | Overgeneralization |
| Predictive | Held-out validation or resampling design | The model predicted, classification performance was, calibration suggested | Inflated performance claim |
| Comparative | Baseline and candidate model comparison | Compared with baseline, the model improved, performance was similar | Weak novelty claim |
| Interpretive | Error analysis, sensitivity checks, domain rationale | Results suggest, one interpretation is, feature patterns are consistent with | Causal overreach |
| Generalizable | External validation or strong replication design | Findings generalized to, performance remained stable in | Unsupported external validity |
| Actionable | Deployment context, ethics review, risk assessment | May inform, could support, should be evaluated before use in | Premature deployment claim |

## Claim-control gates

### Gate 1: Query alignment

The claim must answer the original research query or explicitly explain why the query changed.

Required artifact:

- `artifacts/query/research-query.md`

### Gate 2: Design alignment

The claim must be compatible with the study protocol and validation plan.

Required artifacts:

- `artifacts/protocol/study-protocol.md`
- `artifacts/validation/validation-plan.md`

### Gate 3: Data support

The claim must respect data provenance, sample construction, missingness, measurement limits, and leakage review.

Required artifacts:

- `artifacts/data/data-audit.md`
- `artifacts/features/feature-plan.md`

### Gate 4: Model support

The claim must distinguish baseline performance, candidate model performance, and tuning results.

Required artifacts:

- `artifacts/models/modeling-plan.md`
- `artifacts/results/result-bundle.md`

### Gate 5: Ethics and use boundary

The claim must not imply deployment readiness without ethics, governance, and use-case review.

Required artifact:

- `artifacts/ethics/ethics-review.md`

### Gate 6: Reproducibility support

The claim should be linked to reproducible code, environment, and output manifest whenever possible.

Required artifact:

- `artifacts/reproducibility/reproducibility-package.md`

## Manuscript-language control

| Evidence status | Recommended language |
|---|---|
| Strong internal validation only | The model demonstrated internal predictive performance |
| No external validation | The findings require external validation before generalization |
| No causal design | The results should not be interpreted causally |
| Small or biased sample | The findings should be interpreted as exploratory |
| Incomplete subgroup analysis | Equity and subgroup performance require further evaluation |
| No deployment study | The model should not be treated as deployment-ready |

## Contribution to the paper

This framework strengthens the manuscript by showing that the scaffold does more than organize files. It actively regulates the relationship between scientific evidence and publication claims.

## Implementation plan

1. Add claim-control objects to the Python package.
2. Add a claim-register template.
3. Add tests that verify every claim has an evidence source and claim level.
4. Add a manuscript section on evidence-to-claim traceability.
