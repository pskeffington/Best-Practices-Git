"""Workflow helpers for publishable machine-learning manuscripts."""

from .claims import ClaimLevel, EvidenceSource, ManuscriptClaim
from .dropin import ClaimRecord, RunRecord, hello_dropin
from .pipeline import PipelineField, PipelineStage, ResearchPipeline, default_pipeline
from .standards import ReportingStandard, ScaffoldMapping, default_mappings, default_standards
from .verification import PipelineVerifier, VerificationResult
from .workflow import ManuscriptStage, ManuscriptWorkflow

__all__ = [
    "ClaimLevel",
    "ClaimRecord",
    "EvidenceSource",
    "ManuscriptClaim",
    "ManuscriptStage",
    "ManuscriptWorkflow",
    "PipelineField",
    "PipelineStage",
    "PipelineVerifier",
    "ReportingStandard",
    "ResearchPipeline",
    "RunRecord",
    "ScaffoldMapping",
    "VerificationResult",
    "default_mappings",
    "default_pipeline",
    "default_standards",
    "hello_dropin",
]
