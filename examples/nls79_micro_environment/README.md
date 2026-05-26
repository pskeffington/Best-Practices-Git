# NLSY79 STEM Pre-Check Micro-Environment

This micro-environment demonstrates the updated STEM manuscript pre-check workflow on the NLSY79 LaTeX manuscript package.

## Inputs

- `NLS-79(1).tex`
- `references.bib`
- `Funding-Statement.tex`

## Command

```bash
python stem_precheck_micro.py \
  --tex NLS-79\(1\).tex \
  --references references.bib \
  --funding Funding-Statement.tex \
  --outdir outputs
```

## Outputs

- `outputs/claim-audit-report.md`
- `outputs/claim-audit-trail.json`
- `outputs/publisher-precheck.json`
- `outputs/run-record.json`

## Result

The NLSY79 package passes the updated STEM manuscript pre-check as `PRECHECK_PASS` because the micro-environment includes manuscript source, references, funding statement, evidence tables, bounded claims, and a claim-level audit trail.

The editor note still recommends analysis code, data dictionary, and variable-construction scripts for full computational reproducibility.
