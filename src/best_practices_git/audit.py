"""Repeatable audit reporting for query-to-publication verification."""

from dataclasses import dataclass
from datetime import datetime, timezone

from .verification import VerificationResult


@dataclass(frozen=True)
class AuditReport:
    """A user-repeatable audit report for workflow verification results."""

    generated_at: str
    results: tuple[VerificationResult, ...]

    @property
    def passed(self) -> bool:
        """Return True when every verification result passed."""
        return all(result.passed for result in self.results)

    def to_markdown(self) -> str:
        """Render the audit report as markdown."""
        status = "PASS" if self.passed else "NEEDS WORK"
        lines = [
            "# Query-to-Publication Audit Report",
            "",
            f"Generated at: {self.generated_at}",
            f"Overall status: {status}",
            "",
            "## Verification results",
            "",
        ]
        for result in self.results:
            result_status = "PASS" if result.passed else "FAIL"
            lines.extend(
                [
                    f"### {result.name}",
                    "",
                    f"Status: {result_status}",
                    "",
                ]
            )
            for message in result.messages:
                lines.append(f"- {message}")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"


def build_audit_report(results: tuple[VerificationResult, ...]) -> AuditReport:
    """Build a timestamped audit report from verification results."""
    generated_at = datetime.now(timezone.utc).isoformat()
    return AuditReport(generated_at=generated_at, results=results)
