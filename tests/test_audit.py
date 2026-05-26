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
        )
    )

    markdown = report.to_markdown()

    assert "# Query-to-Publication Audit Report" in markdown
    assert "standards_mapping" in markdown
    assert "PASS" in markdown


def test_audit_report_fails_when_any_result_fails():
    report = build_audit_report(
        (
            VerificationResult(name="pipeline", passed=True),
            VerificationResult(name="claims", passed=False, messages=("No claims registered.",)),
        )
    )

    assert not report.passed
    assert "NEEDS WORK" in report.to_markdown()
