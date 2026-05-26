"""Reviewer-facing readiness scoring for ML manuscript evidence."""

from dataclasses import dataclass, field
from enum import Enum

from .dropin import RunRecord


class ReviewerStatus(str, Enum):
    """Reviewer-facing manuscript readiness status."""

    REVIEW_READY = "REVIEW_READY"
    MINOR_REVISION = "MINOR_REVISION"
    MAJOR_REVISION = "MAJOR_REVISION"
    NOT_REVIEW_READY = "NOT_REVIEW_READY"


@dataclass(frozen=True)
class ReviewerFinding:
    """One reviewer-facing finding."""

    dimension: str
    passed: bool
    message: str


@dataclass(frozen=True)
class ReviewerReport:
    """Compact reviewer report for an ML run record."""

    run_name: str
    status: ReviewerStatus
    findings: tuple[ReviewerFinding, ...] = field(default_factory=tuple)

    def failed_findings(self) -> tuple[ReviewerFinding, ...]:
        """Return failed findings."""
        return tuple(finding for finding in self.findings if not finding.passed)

    def to_markdown(self) -> str:
        """Render the reviewer report as markdown."""
        lines = [
            f"# Reviewer Report: {self.run_name}",
            "",
            f"Reviewer status: {self.status.value}",
            "",
            "## Findings",
            "",
        ]
        for finding in self.findings:
            status = "PASS" if finding.passed else "FLAG"
            lines.append(f"- {status} | {finding.dimension}: {finding.message}")
        return "\n".join(lines).rstrip() + "\n"


class ReviewerScorer:
    """Score drop-in run records for reviewer readiness."""

    def score(self, run: RunRecord) -> ReviewerReport:
        """Create a reviewer report from a run record."""
        findings = (
            self._check_metrics(run),
            self._check_artifacts(run),
            self._check_claims(run),
            self._check_claim_boundaries(run),
        )
        failed_count = sum(not finding.passed for finding in findings)
        if failed_count == 0:
            status = ReviewerStatus.REVIEW_READY
        elif failed_count == 1:
            status = ReviewerStatus.MINOR_REVISION
        elif failed_count <= 3:
            status = ReviewerStatus.MAJOR_REVISION
        else:
            status = ReviewerStatus.NOT_REVIEW_READY
        return ReviewerReport(run_name=run.name, status=status, findings=findings)

    def _check_metrics(self, run: RunRecord) -> ReviewerFinding:
        if run.metrics:
            return ReviewerFinding("metrics", True, "Metrics are present.")
        return ReviewerFinding("metrics", False, "No model metrics were logged.")

    def _check_artifacts(self, run: RunRecord) -> ReviewerFinding:
        if run.artifacts:
            return ReviewerFinding("artifacts", True, "Evidence artifacts are present.")
        return ReviewerFinding("artifacts", False, "No evidence artifacts were logged.")

    def _check_claims(self, run: RunRecord) -> ReviewerFinding:
        if run.claims:
            return ReviewerFinding("claims", True, "Manuscript claims are registered.")
        return ReviewerFinding("claims", False, "No manuscript claims were registered.")

    def _check_claim_boundaries(self, run: RunRecord) -> ReviewerFinding:
        if run.claims and all(claim.boundary_note.strip() for claim in run.claims):
            return ReviewerFinding("claim_boundaries", True, "Each claim has boundary language.")
        return ReviewerFinding(
            "claim_boundaries",
            False,
            "One or more claims lack boundary language.",
        )
