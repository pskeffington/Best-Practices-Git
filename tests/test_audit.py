import json

from best_practices_git.audit import build_audit_report
from best_practices_git.verification import VerificationResult


def test_audit_report_renders_markdown():
    report = build_audit_report(
        (
            VerificationResult(
                name="standards_mapping",
                passed=True,
                messages=("All mappings complete.",),
            ),
        ),
        git_ref="abc123",
    )

    markdown = report.to_markdown()

    assert "# Query-to-Publication Audit Report" in markdown
    assert "standards_mapping" in markdown
    assert "Git ref: abc123" in markdown
    assert "PASS" in markdown


def test_audit_report_renders_json():
    report = build_audit_report(
        (
            VerificationResult(
                name="standards_mapping",
                passed=True,
                messages=("All mappings complete.",),
            ),
        ),
        git_ref="abc123",
    )

    payload = json.loads(report.to_json())

    assert payload["git_ref"] == "abc123"
    assert payload["status"] == "PASS"
    assert payload["results"][0]["name"] == "standards_mapping"


def test_audit_report_fails_when_any_result_fails():
    report = build_audit_report(
        (
            VerificationResult(name="pipeline", passed=True),
            VerificationResult(name="claims", passed=False, messages=("No claims registered.",)),
        )
    )

    assert not report.passed
    assert "NEEDS WORK" in report.to_markdown()


def test_audit_report_writes_latest_and_history_outputs(tmp_path):
    report = build_audit_report(
        (
            VerificationResult(name="pipeline", passed=True),
        ),
        git_ref="abc123",
    )

    latest_md, latest_json, history_md, history_json = report.write_outputs(tmp_path)

    assert latest_md.exists()
    assert latest_json.exists()
    assert history_md.exists()
    assert history_json.exists()
    assert latest_md.name == "latest-audit.md"
    assert latest_json.name == "latest-audit.json"
    assert history_md.name.startswith("audit-")
    assert history_json.name.startswith("audit-")
