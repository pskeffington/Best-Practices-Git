# Biomedical Research Repository Release Gates

Use these gates in sequence, documenting PASS, BLOCKED or NOT_APPLICABLE with a justification and evidence location.

| Gate | Required evidence | Failure response |
| --- | --- | --- |
| G0: scaffold | README, source register, data dictionary, reproducible environment | Block publication |
| G1: code | syntax, lint, unit tests and negative tests | Repair and retest |
| G2: data | permitted sources, schema, units, missingness, join cardinality | Quarantine invalid inputs |
| G3: methods | design, model baselines, split isolation and numerical checks | Return to methods review |
| G4: scientific output | labels, cohorts, citations, figures, claim traceability | Withhold affected artifacts |
| G5: deployment | reviewed source SHA, scoped credentials, smoke tests, rollback | Keep production release closed |

## PR evidence block

- Scientific change / rationale:
- Inputs, units, cohorts and license changes:
- Tests and negative controls:
- Changed outputs / manuscript statements:
- Source commit and artifact checksums:
- Approver and review date:
- Release disposition (PASS / BLOCKED / NOT_APPLICABLE):
