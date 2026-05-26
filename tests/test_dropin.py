import json

from best_practices_git.dropin import ClaimRecord, RunRecord, hello_dropin


def test_dropin_smoke():
    assert hello_dropin() == "drop-in-ready"


def test_claim_record_readiness():
    claim = ClaimRecord(
        text="The model improved over baseline performance.",
        level="comparative",
        evidence_path="artifacts/results/result-bundle.md",
        evidence_description="Baseline comparison",
        boundary_note="External validation is required before generalization.",
    )

    assert claim.is_ready()


def test_run_record_readiness_and_json(tmp_path):
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

    output_path = run.write_json(tmp_path / "validation.json")
    payload = json.loads(output_path.read_text(encoding="utf-8"))

    assert run.is_ready()
    assert payload["status"] == "PASS"
    assert payload["metrics"]["auc"] == 0.84
    assert payload["claims"][0]["level"] == "comparative"


def test_run_record_needs_work_without_claims():
    run = RunRecord(name="validation")
    run.log_artifact("artifacts/results/result-bundle.md")

    assert not run.is_ready()
    assert json.loads(run.to_json())["status"] == "NEEDS_WORK"
