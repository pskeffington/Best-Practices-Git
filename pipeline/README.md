# Query-to-Publication Pipeline

This pipeline turns a machine-learning manuscript from an initial research question into a publication package.

## Pipeline stages

| Stage | Folder | Purpose | Primary output |
|---|---|---|---|
| 01 | `01_query/` | Define the research query and contribution | Query brief |
| 02 | `02_literature/` | Map reporting standards and prior evidence | Evidence matrix |
| 03 | `03_protocol/` | Specify design before analysis | Analysis protocol |
| 04 | `04_data/` | Document data provenance and preprocessing | Data dictionary and provenance note |
| 05 | `05_modeling/` | Train baseline and candidate models | Model comparison record |
| 06 | `06_validation/` | Evaluate performance, calibration, robustness, and error modes | Validation report |
| 07 | `07_ethics/` | Assess privacy, fairness, deployment limits, and intended use | Ethics and governance note |
| 08 | `08_manuscript/` | Convert evidence into manuscript text | Manuscript draft |
| 09 | `09_submission/` | Prepare journal package and reproducibility materials | Submission packet |

## Gate rule

Each stage should produce a written artifact before the next stage begins. The goal is to prevent model-first drift and keep the manuscript defensible from query to publication.

## Branch convention

```bash
git checkout -b pipeline/01-query
git checkout -b pipeline/02-literature
git checkout -b pipeline/03-protocol
git checkout -b pipeline/04-data
git checkout -b pipeline/05-modeling
git checkout -b pipeline/06-validation
git checkout -b pipeline/07-ethics
git checkout -b pipeline/08-manuscript
git checkout -b pipeline/09-submission
```
