# Research Pipeline Scaffold

This pipeline converts a machine-learning idea into a publishable manuscript package.

## Pipeline overview

```text
01_query
02_literature
03_protocol
04_data
05_features
06_models
07_validation
08_interpretation
09_manuscript
10_submission
```

Each stage produces a small artifact that can be reviewed, revised, and cited inside the manuscript.

## Stage outputs

| Stage | Output | Review gate |
|---|---|---|
| Query | Research question memo | Is the question publishable? |
| Literature | Evidence matrix | Is the gap real? |
| Protocol | Analysis plan | Is the design defensible? |
| Data | Data provenance note | Can the sample be audited? |
| Features | Feature dictionary | Is leakage controlled? |
| Models | Model registry | Are baselines and candidates justified? |
| Validation | Evaluation report | Are claims supported? |
| Interpretation | Error and limitation memo | Are results responsibly interpreted? |
| Manuscript | LaTeX draft | Is the paper coherent? |
| Submission | Journal package | Does it meet venue rules? |

## Branching model

Use one branch per pipeline stage:

```bash
git checkout -b pipeline/01-query
git checkout -b pipeline/02-literature
git checkout -b pipeline/03-protocol
git checkout -b pipeline/04-data
git checkout -b pipeline/05-features
git checkout -b pipeline/06-models
git checkout -b pipeline/07-validation
git checkout -b pipeline/08-interpretation
git checkout -b pipeline/09-manuscript
git checkout -b pipeline/10-submission
```

## Research object model

The pipeline should be treated as a set of small objects:

- `ResearchQuery`: the question, target population, outcome, and contribution.
- `EvidenceSource`: one article, guideline, dataset note, or reporting standard.
- `Protocol`: the planned design before analysis.
- `DatasetProfile`: provenance, inclusion rules, missingness, and access limits.
- `FeatureSpec`: feature definition, source field, timing, and leakage risk.
- `ModelSpec`: baseline, candidate model, hyperparameters, and justification.
- `ValidationPlan`: split strategy, metric set, calibration, and robustness checks.
- `ManuscriptSection`: section purpose, required claims, tables, and citations.

## Research cadence

Every stage should end with three files or notes:

1. A human-readable memo.
2. A structured machine-readable record.
3. A checklist entry showing what is complete and what remains unresolved.
