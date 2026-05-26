# STEM Manuscript Pre-Check Design

## Purpose

This project should generalize beyond machine-learning manuscripts while remaining focused on STEM and scientific publishing. The core product is a science-focused manuscript pre-check layer for publishers, editors, authors, and reviewers.

Machine learning becomes one specialized scientific profile inside a broader STEM manuscript validation framework.

## Core positioning

The framework should not attempt to validate every kind of writing. It should focus on scientific manuscripts where claims are expected to be supported by methods, data, experiments, models, observations, figures, tables, equations, code, or reproducible analysis artifacts.

Best product framing:

> A STEM manuscript pre-check system for claim-to-evidence validation before peer review.

## Core scientific principle

Every scientific manuscript makes claims. Each major claim should be traceable to appropriate scientific support:

```text
Claim -> Evidence -> Method -> Validation or justification -> Boundary -> Reviewer finding
```

## STEM pre-check workflow

```text
Manuscript package
  -> structure parse
  -> scientific claim detection
  -> evidence artifact mapping
  -> methods transparency check
  -> validation or robustness check
  -> reproducibility/source availability check
  -> limitation and boundary review
  -> reviewer-readable report
  -> publisher pre-check status
```

## Discipline-neutral STEM checks

A STEM pre-check should assess:

1. title and abstract presence,
2. research question, objective, or hypothesis,
3. methods or experimental design transparency,
4. data, specimen, simulation, or source provenance,
5. figure and table availability,
6. equation, model, or protocol clarity where relevant,
7. claim-to-evidence traceability,
8. statistical, experimental, computational, or theoretical support,
9. limitations and scope boundaries,
10. ethics, funding, competing interests, and data availability statements,
11. code, protocol, or material availability where relevant,
12. supplemental material completeness,
13. reviewer-readable pre-check summary.

## STEM profiles

| Profile | Main evidence type | Special checks |
|---|---|---|
| `general_stem` | methods, figures, tables, citations | objective, methods, evidence artifacts, limitations |
| `machine_learning` | data, code, models, validation metrics | baseline, validation, metrics, reproducibility, claim boundaries |
| `quantitative_empirical` | datasets, statistical models, tables | data provenance, model specification, effect estimates, robustness |
| `experimental_lab` | protocols, measurements, figures, reagents | experimental design, controls, replication, materials, uncertainty |
| `computational_modeling` | equations, simulation code, parameters, outputs | model assumptions, parameter provenance, sensitivity analysis |
| `clinical_biomedical` | patient data, trial design, outcomes | ethics approval, registration, CONSORT-style reporting, adverse events |
| `environmental_science` | field data, geospatial data, instruments | sampling frame, instrument calibration, spatial/temporal coverage |
| `engineering_systems` | prototypes, benchmarks, tests | system design, test conditions, performance metrics, failure modes |
| `systematic_review_meta_analysis` | search strategy, screened studies, synthesis | search reproducibility, inclusion criteria, risk of bias, synthesis method |

## Claim levels for STEM manuscripts

| Claim level | Meaning |
|---|---|
| `descriptive` | Describes observations, samples, measurements, datasets, or patterns. |
| `comparative` | Compares groups, models, treatments, systems, conditions, or cases. |
| `mechanistic` | Proposes a mechanism, pathway, process, or explanatory relation. |
| `causal` | Claims a cause-effect relationship. |
| `predictive` | Claims forecast, classification, or prediction performance. |
| `generalizable` | Extends findings beyond the observed sample, setting, or system. |
| `actionable` | Recommends implementation, intervention, deployment, policy, or practice change. |
| `theoretical` | Derives or supports a formal, mathematical, or conceptual result. |

## Publisher pre-check statuses

Publisher-facing statuses should remain simple:

- `PRECHECK_PASS`
- `PRECHECK_MINOR`
- `PRECHECK_MAJOR`
- `PRECHECK_FAIL`

Reviewer-facing statuses should remain:

- `REVIEW_READY`
- `MINOR_REVISION`
- `MAJOR_REVISION`
- `NOT_REVIEW_READY`

## What remains ML-specific

The ML adapter should remain the first specialized implementation because it has clear needs:

- baseline comparison,
- validation design,
- metrics,
- leakage review,
- model documentation,
- data documentation,
- claim-boundary control,
- reproducibility package.

## What becomes STEM-core

The following should move into the core framework:

- manuscript structure parsing,
- claim records,
- evidence artifacts,
- reviewer findings,
- publisher pre-check statuses,
- audit reports,
- reproducibility/source availability checks,
- limitation and boundary language checks,
- package completeness checks.

## Implementation direction

The codebase should evolve into two layers:

```text
STEM manuscript pre-check core
  + profile-specific adapters
```

The first adapter remains:

```text
machine_learning
```

Future adapters can include:

```text
quantitative_empirical
experimental_lab
computational_modeling
clinical_biomedical
environmental_science
engineering_systems
systematic_review_meta_analysis
```

## Revised contribution claim

The broader scientific contribution is:

> This framework provides a STEM manuscript pre-check layer that helps publishers and reviewers evaluate whether major scientific claims are traceable to appropriate evidence, methods, validation, limitations, and reproducibility materials before peer review.
