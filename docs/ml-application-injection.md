# ML Application Injection Design

## Purpose

The scaffold should be easy for ML users to inject into existing applications, notebooks, training scripts, and research pipelines.

Users should not need to rewrite their full project around this repository. They should be able to import lightweight objects that record workflow evidence, claims, validation metadata, and audit events while their existing ML code runs.

## Design principle

Do not force users to adopt the scaffold first. Let users inject the scaffold into the ML workflow they already have.

## Injection modes

### Decorator injection

Users can wrap training, evaluation, and reporting functions with a stage tracker.

### Context-manager injection

Users can open a workflow run around notebook or script blocks, then log metrics, artifacts, and claims.

### Event logging injection

Users can record important workflow events from custom orchestration code.

### Claim registration injection

Users can register manuscript claims directly from analysis code, including evidence paths and boundary notes.

### Audit injection

Users can trigger an audit at the end of a script, notebook, or CI job.

## User-facing value

Injection makes the framework usable for scikit-learn scripts, PyTorch loops, TensorFlow projects, Jupyter notebooks, MLflow-like pipelines, research software engineering projects, and lightweight graduate research projects.

## Minimal viable API

The injectable layer should provide:

- `WorkflowRun`
- `track_stage`
- `log_event`
- `log_metric`
- `log_artifact`
- `register_claim`
- `audit`

## Contribution to the paper

This strengthens the framework's publishable contribution because the scaffold becomes not only a repository template but an injectable workflow layer for ML applications.

The manuscript can argue that reproducible ML science should be embedded into the scientific workflow at runtime, where modeling, validation, and claim generation actually occur.
