from best_practices_git.dropin import ClaimRecord, RunRecord
from best_practices_git.reviewer import ReviewerScorer, ReviewerStatus


def test_reviewer_report_review_ready():
    run = RunRecord(name="validation")
    run.log_metric("auc", 0.84)
    run.log_artifact("artifacts/results/result-bundle.md")
    run.register_claim(
        ClaimRecord(
            text="The model improved over baseline performance.",
            level="comparative",
            evidence_path="artifacts/results/result-bundle.md",
            evidence_description="Baseline comparison",
            boundary_note="External validation is required before generalization.",
        )
    )

    report = ReviewerScorer().score(run)

    assert report.status == ReviewerStatus.REVIEW_READY
    assert not report.failed_findings()


def test_reviewer_report_flags_missing_claims():
    run = RunRecord(name="validation")
    run.log_metric("auc", 0.84)
    run.log_artifact("artifacts/results/result-bundle.md")

    report = ReviewerScorer().score(run)

    assert report.status == ReviewerStatus.MAJOR_REVISION
    assert report.failed_findings()
    assert "No manuscript claims" in report.to_markdown()


def test_reviewer_report_not_review_ready_when_empty():
    run = RunRecord(name="validation")

    report = ReviewerScorer().score(run)

    assert report.status == ReviewerStatus.NOT_REVIEW_READY
    assert len(report.failed_findings()) == 4
