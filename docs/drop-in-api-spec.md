# Drop-In API Specification

## Goal

Provide the smallest possible API for ML users who want manuscript evidence tracking without changing their existing ML code.

## User promise

Add the framework beside an existing ML project, log a few evidence records, then generate audit-ready files.

## Minimal API

### `RunRecord`

A single model run, validation run, notebook run, or analysis run.

Required capabilities:

- store a run name,
- log metrics,
- log artifacts,
- log notes,
- register claims,
- export markdown,
- export JSON.

### `ClaimRecord`

A manuscript claim linked to evidence.

Required fields:

- claim text,
- claim level,
- evidence path,
- evidence description,
- boundary note.

### `AuditRecord`

A summary of whether the run is manuscript-ready.

Required checks:

- at least one artifact exists,
- each claim has evidence,
- each claim has a boundary note,
- metrics are captured when applicable.

## Required output files

A drop-in run should be able to write:

```text
artifacts/drop-in/latest-run.md
artifacts/drop-in/latest-run.json
```

Future versions may also write timestamped history files.

## No lock-in rules

The API must not require:

- scikit-learn,
- PyTorch,
- TensorFlow,
- MLflow,
- DVC,
- notebook-specific dependencies,
- cloud services.

## Integration style

Users should be able to use the API as a companion object in existing scripts. The ML code remains unchanged except for evidence logging calls.

## Manuscript contribution

The drop-in API makes the workflow scaffold usable by ordinary ML researchers. It turns the paper's framework into a practical layer that can be inserted into existing scientific workflows.
