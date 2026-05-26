"""Repeatable audit reporting for query-to-publication verification."""

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .verification import VerificationResult


@dataclass(frozen=True)
class AuditReport:
    """A user-repeatable audit report for workflow verification results."""

    generated_at: str
    results: tuple[VerificationResult, ...]
    git_ref: str = "unknown"

    @property
    def passed(self) -> bool:
        """Return True when every verification result passed."""
        return all(result.passed for result in self.results)

    @property
    def status(self) -> str:
        """Return the report-level status label."""
        return "PASS" if self.passed else "NEEDS WORK"

    def to_dict(self) -> dict[str, object]:
        """Render the audit report as a JSON-serializable dictionary."""
        return {
            "generated_at": self.generated_at,
            "git_ref": self.git_ref,
            "status": self.status,
            "passed": self.passed,
            "results": [
                {
                    "name": result.name,
                    "passed": result.passed,
                    "messages": list(result.messages),
                }
                for result in self.results
            ],
        }

    def to_json(self) -> str:
        """Render the audit report as formatted JSON."""
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def to_markdown(self) -> str:
        """Render the audit report as markdown."""
        lines = [
            "# Query-to-Publication Audit Report",
            "",
            f"Generated at: {self.generated_at}",
            f"Git ref: {self.git_ref}",
            f"Overall status: {self.status}",
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

    def write_outputs(self, audit_dir: Path) -> tuple[Path, Path, Path, Path]:
        """Write latest and timestamped markdown and JSON audit files."""
        audit_dir.mkdir(parents=True, exist_ok=True)
        safe_stamp = self.generated_at.replace(":", "-").replace("+", "-")
        latest_md = audit_dir / "latest-audit.md"
        latest_json = audit_dir / "latest-audit.json"
        history_md = audit_dir / f"audit-{safe_stamp}.md"
        history_json = audit_dir / f"audit-{safe_stamp}.json"
        markdown = self.to_markdown()
        json_text = self.to_json()
        latest_md.write_text(markdown, encoding="utf-8")
        latest_json.write_text(json_text, encoding="utf-8")
        history_md.write_text(markdown, encoding="utf-8")
        history_json.write_text(json_text, encoding="utf-8")
        return latest_md, latest_json, history_md, history_json


def build_audit_report(
    results: tuple[VerificationResult, ...],
    git_ref: str = "unknown",
) -> AuditReport:
    """Build a timestamped audit report from verification results."""
    generated_at = datetime.now(timezone.utc).isoformat()
    return AuditReport(generated_at=generated_at, results=results, git_ref=git_ref)
