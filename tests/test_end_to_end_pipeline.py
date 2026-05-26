import json

from best_practices_git import ClaimRecord, ReviewerScorer, ReviewerStatus, RunRecord


def test_end_to_end_ml_pipeline_reviewer_ready(tmp_path):
    run = RunRecord(name="validation")

    run.log_metric("baseline_auc", 0.71)
    run.log_metric("candidate_auc", 0.84)
    run.log_artifact("artifacts/results/result-bundle.md")
    run.log_artifact("artifacts/validation/validation-plan.md")
    run.register_claim(
        ClaimRecord(
            text="The candidate model improved over the baseline during internal validation.",
            level="comparative",
            evidence_path="artifacts/results/result-bundle.md",
            evidence_description="Baseline and candidate model comparison",
            boundary_note="External validation is required before generalization.",
        )
    )

    output_path = run.write_json(tmp_path / "artifacts/drop-in/validation.json")
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    reviewer_report = ReviewerScorer().score(run)

    assert run.is_ready()
    assert payload["status"] == "PASS"
    assert payload["metrics"]["baseline_auc"] == 0.71
    assert payload["metrics"]["candidate_auc"] == 0.84
    assert len(payload["artifacts"]) == 2
    assert payload["claims"][0]["level"] == "comparative"
    assert reviewer_report.status == ReviewerStatus.REVIEW_READY
    assert not reviewer_report.failed_findings()
    assert "REVIEW_READY" in reviewer_report.to_markdown()


def test_end_to_end_ml_pipeline_flags_unbounded_claim():
    run = RunRecord(name="validation")

    run.log_metric("candidate_auc", 0.84)
    run.log_artifact("artifacts/results/result-bundle.md")
    run.register_claim(
        ClaimRecord(
            text="The candidate model is ready for broad use.",
            level="actionable",
            evidence_path="artifacts/results/result-bundle.md",
            evidence_description="Internal validation metric",
            boundary_note="",
        )
    )

    reviewer_report = ReviewerScorer().score(run)

    assert not run.is_ready()
    assert reviewer_report.status == ReviewerStatus.MINOR_REVISION
    assert reviewer_report.failed_findings()
    assert "claim_boundaries" in reviewer_report.to_markdown()
