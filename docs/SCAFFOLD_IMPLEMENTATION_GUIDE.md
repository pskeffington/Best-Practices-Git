# Biomedical Research Scaffold Implementation Guide

Use this guide with the [engineering framework](../README.md), [research README template](../templates/biomedical-research/README.template.md) and [release-gate checklist](../checklists/research-release-gates.md).

## Initialize a new research project

Create a README that states the research question, analytic target, project status and reproducible quick start. Write a protocol identifying the population, sample selection, measurements and interpretation boundaries. Create a data dictionary with identifiers, units, codes, ranges, missingness and transformations. Maintain a source register listing the authoritative source, version, retrieval date, licensing and access process.

Establish a documented environment and synthetic test fixtures before connecting restricted inputs. Add tests for parsing, validation, null handling, stable joins, and expected analytical outputs. Use a project-specific pull-request template to capture the scientific rationale, changed assumptions and test evidence.

## Promotion sequence

**Scaffold → reproducible code → validated data → method review → reviewed artifacts → controlled release.**

Record PASS, BLOCKED or NOT_APPLICABLE for every gate, together with a reviewer and evidence path. A failed gate should produce a specific corrective action rather than a vague release status.

## Scientific output contract

For every public figure or result, record the generating script, code revision, input identifier, parameter settings, software environment and scientific interpretation. Review numerical changes alongside manuscript and figure text.

## Repository responsibilities

Keep this repository focused on reusable practices. Store project-specific cohorts, methods and results in the appropriate project repository. Apply platform-native secret scanning, repository branch protection and independently reviewed release permissions where required.
