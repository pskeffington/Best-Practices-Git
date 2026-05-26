"""Automated verification for query-to-publication workflow readiness."""

from dataclasses import dataclass, field

from .claims import ManuscriptClaim
from .pipeline import ResearchPipeline
from .standards import ScaffoldMapping


@dataclass(frozen=True)
class VerificationResult:
    """Result from a workflow verification check."""

    name: str
    passed: bool
    messages: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class PipelineVerifier:
    """Verify pipeline, standards, and claim readiness for manuscript work."""

    pipeline: ResearchPipeline
    mappings: tuple[ScaffoldMapping, ...]
    claims: tuple[ManuscriptClaim, ...] = field(default_factory=tuple)

    def verify_pipeline_completeness(self) -> VerificationResult:
        """Check whether all pipeline stages are complete."""
        incomplete = self.pipeline.incomplete_stages()
        if not incomplete:
            return VerificationResult(
                name="pipeline_completeness",
                passed=True,
                messages=("All pipeline stages are complete.",),
            )
        messages = tuple(
            f"{stage.name} missing: {', '.join(stage.missing_fields())}"
            for stage in incomplete
        )
        return VerificationResult(
            name="pipeline_completeness",
            passed=False,
            messages=messages,
        )

    def verify_standards_mapping(self) -> VerificationResult:
        """Check whether every mapping has standards and reporting functions."""
        failed = tuple(
            mapping.stage_name
            for mapping in self.mappings
            if not mapping.has_reporting_function() or not mapping.standard_names()
        )
        if not failed:
            return VerificationResult(
                name="standards_mapping",
                passed=True,
                messages=("All scaffold mappings have standards and reporting functions.",),
            )
        return VerificationResult(
            name="standards_mapping",
            passed=False,
            messages=tuple(f"Mapping incomplete for stage: {stage}" for stage in failed),
        )

    def verify_claim_readiness(self) -> VerificationResult:
        """Check whether manuscript claims are publication-ready."""
        if not self.claims:
            return VerificationResult(
                name="claim_readiness",
                passed=False,
                messages=("No manuscript claims registered.",),
            )
        failed = tuple(claim.text for claim in self.claims if not claim.is_publication_ready())
        if not failed:
            return VerificationResult(
                name="claim_readiness",
                passed=True,
                messages=("All registered manuscript claims are publication-ready.",),
            )
        return VerificationResult(
            name="claim_readiness",
            passed=False,
            messages=tuple(f"Claim not ready: {claim}" for claim in failed),
        )

    def run_all(self) -> tuple[VerificationResult, ...]:
        """Run all verification checks."""
        return (
            self.verify_pipeline_completeness(),
            self.verify_standards_mapping(),
            self.verify_claim_readiness(),
        )
