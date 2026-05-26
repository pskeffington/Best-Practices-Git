"""Evidence-to-claim controls for ML manuscript development."""

from dataclasses import dataclass
from enum import Enum


class ClaimLevel(str, Enum):
    """Strength level of a manuscript claim."""

    DESCRIPTIVE = "descriptive"
    PREDICTIVE = "predictive"
    COMPARATIVE = "comparative"
    INTERPRETIVE = "interpretive"
    GENERALIZABLE = "generalizable"
    ACTIONABLE = "actionable"


@dataclass(frozen=True)
class EvidenceSource:
    """A workflow artifact or result that supports a claim."""

    artifact_path: str
    description: str

    def is_valid(self) -> bool:
        """Return True when the source has a path and description."""
        return bool(self.artifact_path.strip() and self.description.strip())


@dataclass(frozen=True)
class ManuscriptClaim:
    """A manuscript claim linked to evidence and a permitted claim level."""

    text: str
    level: ClaimLevel
    evidence_sources: tuple[EvidenceSource, ...]
    boundary_note: str = ""

    def has_evidence(self) -> bool:
        """Return True when at least one valid evidence source supports the claim."""
        return any(source.is_valid() for source in self.evidence_sources)

    def is_publication_ready(self) -> bool:
        """Return True when the claim has text, evidence, and a boundary note."""
        return bool(self.text.strip() and self.has_evidence() and self.boundary_note.strip())

    def to_markdown(self) -> str:
        """Render the claim as a markdown register entry."""
        sources = "\n".join(
            f"- `{source.artifact_path}`: {source.description}"
            for source in self.evidence_sources
        )
        return (
            f"## Claim\n\n{self.text}\n\n"
            f"**Level:** {self.level.value}\n\n"
            f"**Evidence sources:**\n\n{sources}\n\n"
            f"**Boundary note:** {self.boundary_note}\n"
        )
