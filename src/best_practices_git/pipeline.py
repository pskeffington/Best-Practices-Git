"""Pipeline scaffolding for query-to-publication ML manuscript research."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol


class RenderableStage(Protocol):
    """Protocol for pipeline stages that can render themselves as markdown."""

    artifact_path: str

    def to_markdown(self) -> str:
        """Render the stage as markdown."""
        ...


@dataclass(frozen=True)
class PipelineField:
    """A small required field in a research pipeline stage."""

    name: str
    prompt: str
    value: str = ""

    @property
    def is_complete(self) -> bool:
        """Return True when the field has a non-empty value."""
        return bool(self.value.strip())

    def to_markdown(self) -> str:
        """Render the field as markdown."""
        body = self.value.strip() or f"TODO: {self.prompt}"
        return f"## {self.name}\n\n{body}\n"


@dataclass(frozen=True)
class PipelineStage:
    """A manuscript pipeline stage composed of required fields."""

    name: str
    artifact_path: str
    fields: tuple[PipelineField, ...] = field(default_factory=tuple)

    @property
    def completion_ratio(self) -> float:
        """Return the fraction of completed fields."""
        if not self.fields:
            return 1.0
        completed = sum(field.is_complete for field in self.fields)
        return completed / len(self.fields)

    def missing_fields(self) -> tuple[str, ...]:
        """Return the names of incomplete fields."""
        return tuple(field.name for field in self.fields if not field.is_complete)

    def to_markdown(self) -> str:
        """Render the stage as markdown."""
        rendered_fields = "\n".join(field.to_markdown() for field in self.fields)
        return f"# {self.name}\n\n{rendered_fields}"


@dataclass(frozen=True)
class ResearchPipeline:
    """An ordered set of pipeline stages for a manuscript project."""

    stages: tuple[PipelineStage, ...]

    def stage_names(self) -> tuple[str, ...]:
        """Return stage names in order."""
        return tuple(stage.name for stage in self.stages)

    def incomplete_stages(self) -> tuple[PipelineStage, ...]:
        """Return stages that still have missing required fields."""
        return tuple(stage for stage in self.stages if stage.completion_ratio < 1.0)

    def write_artifact_templates(self, root: Path) -> None:
        """Write markdown artifact templates for each stage."""
        for stage in self.stages:
            output_path = root / stage.artifact_path
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(stage.to_markdown(), encoding="utf-8")


def default_pipeline() -> ResearchPipeline:
    """Create the default query-to-publication pipeline."""
    return ResearchPipeline(
        stages=(
            PipelineStage(
                name="Research Query",
                artifact_path="artifacts/query/research-query.md",
                fields=(
                    PipelineField("Problem statement", "State the research problem."),
                    PipelineField("Target population", "Define the population."),
                    PipelineField("Outcome", "Define the outcome or target."),
                    PipelineField("Machine-learning justification", "Explain why ML is appropriate."),
                    PipelineField("Baseline comparison", "Identify the baseline model or method."),
                ),
            ),
            PipelineStage(
                name="Study Protocol",
                artifact_path="artifacts/protocol/study-protocol.md",
                fields=(
                    PipelineField("Data source", "Describe the data source."),
                    PipelineField("Inclusion criteria", "Define inclusion rules."),
                    PipelineField("Exclusion criteria", "Define exclusion rules."),
                    PipelineField("Validation strategy", "Define validation design."),
                    PipelineField("Primary metrics", "Define primary evaluation metrics."),
                ),
            ),
            PipelineStage(
                name="Data Audit",
                artifact_path="artifacts/data/data-audit.md",
                fields=(
                    PipelineField("Provenance", "Document data provenance."),
                    PipelineField("Missingness", "Summarize missingness."),
                    PipelineField("Leakage risks", "Identify leakage risks."),
                    PipelineField("Measurement limits", "Describe measurement limitations."),
                ),
            ),
            PipelineStage(
                name="Modeling Plan",
                artifact_path="artifacts/models/modeling-plan.md",
                fields=(
                    PipelineField("Baseline model", "Define the baseline model."),
                    PipelineField("Candidate models", "List candidate models."),
                    PipelineField("Tuning strategy", "Define tuning strategy."),
                    PipelineField("Software environment", "Record software versions."),
                ),
            ),
            PipelineStage(
                name="Validation Plan",
                artifact_path="artifacts/validation/validation-plan.md",
                fields=(
                    PipelineField("Split design", "Define split or resampling design."),
                    PipelineField("Calibration checks", "Define calibration checks."),
                    PipelineField("Error analysis", "Define error analysis."),
                    PipelineField("Sensitivity checks", "Define sensitivity checks."),
                ),
            ),
            PipelineStage(
                name="Manuscript Package",
                artifact_path="artifacts/submission/submission-package.md",
                fields=(
                    PipelineField("Target venue", "Name the target venue."),
                    PipelineField("Reporting checklist", "Identify reporting checklist."),
                    PipelineField("Data availability", "Draft data availability statement."),
                    PipelineField("Code availability", "Draft code availability statement."),
                ),
            ),
        )
    )
