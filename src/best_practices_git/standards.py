"""Standards mapping objects for ML manuscript workflow scaffolding."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ReportingStandard:
    """A reporting standard or adjacent documentation practice."""

    name: str
    purpose: str
    scope: str


@dataclass(frozen=True)
class ScaffoldMapping:
    """A mapping between a workflow stage and reporting standards."""

    stage_name: str
    reporting_functions: tuple[str, ...] = field(default_factory=tuple)
    standards: tuple[ReportingStandard, ...] = field(default_factory=tuple)

    def has_reporting_function(self) -> bool:
        """Return True when the stage has at least one reporting function."""
        return bool(self.reporting_functions)

    def standard_names(self) -> tuple[str, ...]:
        """Return mapped standard names."""
        return tuple(standard.name for standard in self.standards)


def default_standards() -> tuple[ReportingStandard, ...]:
    """Return common standards and practices relevant to ML manuscripts."""
    return (
        ReportingStandard(
            name="TRIPOD-AI",
            purpose="Transparent reporting of prediction model studies using AI or ML.",
            scope="Prediction modeling",
        ),
        ReportingStandard(
            name="CONSORT-AI",
            purpose="Reporting randomized trials that evaluate AI interventions.",
            scope="Clinical trials",
        ),
        ReportingStandard(
            name="SPIRIT-AI",
            purpose="Protocol reporting for clinical trials involving AI interventions.",
            scope="Clinical trial protocols",
        ),
        ReportingStandard(
            name="CLAIM",
            purpose="Checklist for AI in medical imaging studies.",
            scope="Medical imaging AI",
        ),
        ReportingStandard(
            name="Model Cards",
            purpose="Structured model documentation for intended use, performance, and limits.",
            scope="Model transparency",
        ),
        ReportingStandard(
            name="Data Cards",
            purpose="Structured dataset documentation for provenance, composition, and limits.",
            scope="Dataset transparency",
        ),
        ReportingStandard(
            name="Open Science Reproducibility",
            purpose="Availability of code, data, environments, and research artifacts.",
            scope="Reproducibility",
        ),
    )


def default_mappings() -> tuple[ScaffoldMapping, ...]:
    """Return default workflow-stage mappings to reporting functions."""
    standards = {standard.name: standard for standard in default_standards()}
    return (
        ScaffoldMapping(
            stage_name="Research Query",
            reporting_functions=("Question", "Population", "Target", "Contribution"),
            standards=(standards["TRIPOD-AI"],),
        ),
        ScaffoldMapping(
            stage_name="Study Protocol",
            reporting_functions=("Design", "Eligibility", "Outcome definition", "Metrics"),
            standards=(standards["SPIRIT-AI"], standards["TRIPOD-AI"]),
        ),
        ScaffoldMapping(
            stage_name="Data Audit",
            reporting_functions=("Data source", "Missingness", "Measurement limits"),
            standards=(standards["Data Cards"], standards["Open Science Reproducibility"]),
        ),
        ScaffoldMapping(
            stage_name="Modeling Plan",
            reporting_functions=("Baseline", "Candidate models", "Tuning", "Software"),
            standards=(standards["TRIPOD-AI"], standards["Model Cards"]),
        ),
        ScaffoldMapping(
            stage_name="Validation Plan",
            reporting_functions=("Validation design", "Calibration", "Error analysis"),
            standards=(standards["TRIPOD-AI"], standards["Model Cards"]),
        ),
        ScaffoldMapping(
            stage_name="Manuscript Package",
            reporting_functions=("Availability statements", "Checklist compliance", "Submission readiness"),
            standards=(standards["Open Science Reproducibility"],),
        ),
    )
