# Standards Gap Map

## Purpose

This document maps the repository scaffold against existing machine-learning and scientific-reporting guidance. The goal is to identify the contribution gap: not another checklist, but an operational workflow that produces the evidence, documentation, and manuscript language that reporting standards require.

## Core distinction

```text
Reporting standards ask: What should the final manuscript disclose?
Workflow scaffolds ask: How are those disclosures produced, reviewed, versioned, and linked to evidence?
```

The contribution of this repository is the second layer.

## Standards and adjacent practices

| Standard or practice | Primary purpose | What it usually provides | Gap this repo addresses |
|---|---|---|---|
| TRIPOD / TRIPOD-AI | Prediction model reporting | Items for transparent reporting of prediction model studies | Converts reporting items into staged research artifacts before manuscript drafting |
| CONSORT-AI | Clinical trial reporting for AI interventions | Trial reporting extension for AI systems | Provides a pre-submission workflow for generating AI intervention documentation |
| SPIRIT-AI | Clinical trial protocol reporting for AI interventions | Protocol extension for AI trials | Extends protocol logic into a general ML manuscript pipeline |
| CLAIM | Medical imaging AI reporting | Checklist for AI in medical imaging studies | Generalizes checklist logic into reusable pipeline stages |
| Model cards | Model-level transparency | Intended use, performance, limitations, ethical concerns | Places model cards inside the larger scientific manuscript workflow |
| Data cards / dataset documentation | Dataset-level transparency | Dataset provenance, purpose, composition, collection, limitations | Places dataset documentation before feature engineering and modeling |
| Open science / reproducibility practice | Research transparency | Code, data, environment, and artifact availability | Makes reproducibility artifacts first-class project outputs |
| REFORMS-style ML science guidance | Reliability and reproducibility in ML-based science | Broad recommendations for ML validity and reporting | Operationalizes scientific reliability as repository structure, gates, and CLI-generated files |

## Scaffold contribution by stage

| Scaffold stage | Scientific-process role | Reporting contribution |
|---|---|---|
| Research Query | Prevents model-first science | Produces the introduction's question, population, target, and contribution language |
| Literature Context | Places the work in a field | Supports rationale, gap, and novelty claims |
| Study Protocol | Locks design before modeling | Supports methods transparency and reduces post hoc design drift |
| Data Audit | Checks whether data can support the claim | Supports data source, missingness, measurement, and limitation reporting |
| Feature Plan | Documents transformations and leakage controls | Supports preprocessing and feature engineering reporting |
| Modeling Plan | Defines baseline and candidate models | Supports model comparison and tuning transparency |
| Validation Plan | Aligns evaluation with claim strength | Supports metrics, split strategy, calibration, sensitivity, and uncertainty reporting |
| Result Bundle | Packages evidence | Supports tables, figures, and results prose |
| Ethics Review | Documents risk and non-use | Supports ethics, fairness, privacy, and governance statements |
| Reproducibility Package | Preserves rerun context | Supports data/code availability and replication materials |
| Manuscript Section Drafts | Translates artifacts into prose | Keeps writing tied to evidence |
| Submission Package | Prepares peer-review materials | Supports venue-specific compliance |

## Unique gap statement

Existing guidance often describes the reporting endpoint. This repository contributes a workflow that begins at the research query and creates the documentation trail needed to support that endpoint.

The scaffold is therefore useful as:

1. a manuscript development system,
2. a reproducibility architecture,
3. a peer-review preparation tool,
4. a leakage and claim-control mechanism,
5. a teaching framework for ML-based scientific research.

## Manuscript implication

The manuscript should argue that ML research needs an intermediate layer between abstract reporting standards and project-specific code. That layer should be modular, executable, versioned, and manuscript-aware.

Recommended contribution phrasing:

> We propose a query-to-publication scaffold that operationalizes machine-learning reporting and reproducibility standards as staged, version-controlled artifacts. The scaffold links scientific question formation, protocol design, data auditing, feature planning, model validation, ethics review, and manuscript drafting into a single auditable workflow.

## Next implementation tasks

- Add a `standards.py` module to represent standards, checklist items, and scaffold mappings.
- Add a standards mapping template in `templates/`.
- Add tests that ensure every pipeline stage maps to at least one reporting function.
- Add a manuscript section explaining the contribution gap.
