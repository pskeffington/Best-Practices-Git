# User-Repeatable Audit

## Purpose

The audit command gives users a repeatable way to verify manuscript workflow readiness during drafting, revision, and pre-submission review.

## Command

Run from the repository root:

```bash
bpg-workflow audit --root .
```

The command writes:

```text
artifacts/audits/latest-audit.md
```

## Recommended audit cycle

Run the audit at these points:

1. after initializing artifacts,
2. after completing the study protocol,
3. after data audit and feature planning,
4. after model validation,
5. before manuscript drafting,
6. before submission,
7. after reviewer revisions.

## What the audit checks

The current audit verifies:

- pipeline completeness,
- standards mapping readiness,
- manuscript claim readiness.

## How to interpret results

### PASS

The checked component is ready under the current scaffold rules.

### FAIL

The checked component needs additional artifact work, claim support, or boundary language.

### NEEDS WORK

The overall audit contains at least one failed verification result.

## Repeatability principle

The audit is designed to be run repeatedly. Each run checks the same verification categories, producing a consistent report that can be compared across manuscript versions.

## User-facing value

The audit helps users answer:

- What is missing from the research workflow?
- Which claims are not yet publication-ready?
- Are reporting standards connected to workflow stages?
- Is the manuscript ready for internal review or external submission?

## Future extension

Future versions can add:

- timestamped audit history files,
- JSON audit output,
- artifact existence checks,
- manuscript claim extraction,
- Git commit hash recording,
- CI enforcement of audit status.
