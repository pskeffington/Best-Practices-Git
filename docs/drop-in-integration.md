# Drop-In Integration

## Purpose

The framework should be simple enough for an ML user to copy into an existing project and start using immediately.

The target is a dump-and-drop workflow:

1. copy the package or a single helper file into an ML project,
2. run one initialization command,
3. add a few logging calls around existing training or validation code,
4. generate audit artifacts,
5. use the outputs in the manuscript.

## Design rule

The scaffold should not require users to change their ML framework, notebook structure, model code, or data pipeline.

It should sit beside the project and record evidence.

## Minimum user workflow

```bash
pip install -e .
bpg-workflow init-artifacts --root .
bpg-workflow audit --root .
```

## Drop-in project layout

```text
existing-ml-project/
  train.py
  evaluate.py
  notebooks/
  artifacts/
    query/
    protocol/
    data/
    models/
    validation/
    results/
    audits/
  manuscript/
```

## Runtime integration pattern

A user should only need three concepts:

- start a run,
- log evidence,
- audit readiness.

Example pattern:

```text
start run -> log metrics -> log artifacts -> register claims -> write report -> run audit
```

## Zero lock-in principle

The framework should work with:

- scikit-learn,
- PyTorch,
- TensorFlow,
- XGBoost,
- R-generated outputs,
- Jupyter notebooks,
- command-line scripts,
- existing research pipelines.

## What gets produced

The drop-in layer should produce:

- run report,
- metric summary,
- artifact list,
- claim register,
- audit report,
- manuscript-ready evidence notes.

## Paper contribution

The dump-and-drop design matters because reproducibility tools often fail when they require researchers to abandon existing workflows. This framework instead provides a low-friction workflow layer that can be added to existing ML projects.
