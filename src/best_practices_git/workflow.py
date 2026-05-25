"""Object-oriented helpers for manuscript workflow tracking."""

from dataclasses import dataclass, field
from enum import Enum


class ManuscriptStage(str, Enum):
    """Major stages in a query-to-publication workflow."""

    QUERY = "query"
    PROTOCOL = "protocol"
    ANALYSIS = "analysis"
    INTERPRETATION = "interpretation"
    MANUSCRIPT = "manuscript"
    SUBMISSION = "submission"


@dataclass(frozen=True)
class ManuscriptWorkflow:
    """A minimal workflow model for tracking manuscript readiness."""

    title: str
    stage: ManuscriptStage = ManuscriptStage.QUERY
    completed_gates: tuple[str, ...] = field(default_factory=tuple)

    def advance_to(self, next_stage: ManuscriptStage) -> "ManuscriptWorkflow":
        """Return a new workflow object advanced to the requested stage."""
        return ManuscriptWorkflow(
            title=self.title,
            stage=next_stage,
            completed_gates=self.completed_gates,
        )

    def complete_gate(self, gate_name: str) -> "ManuscriptWorkflow":
        """Return a new workflow object with one additional completed gate."""
        normalized_gate = gate_name.strip()
        if not normalized_gate:
            raise ValueError("gate_name cannot be empty")
        if normalized_gate in self.completed_gates:
            return self
        return ManuscriptWorkflow(
            title=self.title,
            stage=self.stage,
            completed_gates=(*self.completed_gates, normalized_gate),
        )
