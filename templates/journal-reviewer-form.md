# Journal Reviewer Form for ML Manuscripts

Use this form to evaluate whether a machine-learning manuscript has a reviewer-readable evidence package.

## Manuscript identification

- Manuscript title:
- Reviewer:
- Date:
- Version or commit hash:

## Reviewer status

Choose one:

- [ ] `REVIEW_READY`
- [ ] `MINOR_REVISION`
- [ ] `MAJOR_REVISION`
- [ ] `NOT_REVIEW_READY`

## Evidence-chain review

| Dimension | Pass | Flag | Notes |
|---|---:|---:|---|
| Research query is clear | [ ] | [ ] | |
| Data provenance is documented | [ ] | [ ] | |
| Feature construction is documented | [ ] | [ ] | |
| Baseline comparison is present | [ ] | [ ] | |
| Validation design is adequate | [ ] | [ ] | |
| Metrics match the research question | [ ] | [ ] | |
| Claims are linked to evidence artifacts | [ ] | [ ] | |
| Claim boundaries are stated | [ ] | [ ] | |
| Reproducibility artifacts are supplied | [ ] | [ ] | |
| Ethics and use limitations are discussed | [ ] | [ ] | |

## Claim-level review

For each major claim, record the evidence chain.

### Claim 1

- Claim text:
- Claim level:
- Evidence artifact:
- Validation support:
- Boundary note:
- Reviewer concern:

### Claim 2

- Claim text:
- Claim level:
- Evidence artifact:
- Validation support:
- Boundary note:
- Reviewer concern:

### Claim 3

- Claim text:
- Claim level:
- Evidence artifact:
- Validation support:
- Boundary note:
- Reviewer concern:

## Red flags

Check all that apply.

- [ ] Performance claim without reported metrics
- [ ] Generalization claim without external validation
- [ ] Causal language without causal design
- [ ] Deployment claim without deployment evidence
- [ ] Missing baseline comparison
- [ ] Missing data provenance
- [ ] Missing feature construction details
- [ ] Missing reproducibility package
- [ ] Artifacts referenced but not supplied
- [ ] Claims not linked to evidence

## Recommendation

- [ ] Accept or proceed to substantive review
- [ ] Minor revision
- [ ] Major revision
- [ ] Reject or return before review

## Summary for editor

Write a short summary of whether the manuscript's claims are supported by its evidence package.
