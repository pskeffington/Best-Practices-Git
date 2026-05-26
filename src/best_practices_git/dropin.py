"""Drop-in helpers for ML manuscript projects."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ClaimRecord:
    """A manuscript claim linked to evidence."""

    text: str
    level: str
    evidence_path: str
    evidence_description: str
    boundary_note: str

    def is_ready(self) -> bool:
        """Return True when the claim has all required fields."""
        return all(
            value.strip()
            for value in [
                self.text,
                self.level,
                self.evidence_path,
                self.evidence_description,
                self.boundary_note,
            ]
        )


@dataclass
class RunRecord:
    """A tiny drop-in record for an ML run."""

    name: str
    metrics: dict[str, float | int | str] = field(default_factory=dict)
    artifacts: list[str] = field(default_factory=list)
    claims: list[ClaimRecord] = field(default_factory=list)

    def log_metric(self, name: str, value: float | int | str) -> None:
        """Log one metric."""
        self.metrics[name] = value

    def log_artifact(self, path: str) -> None:
        """Log one artifact path."""
        self.artifacts.append(path)

    def register_claim(self, claim: ClaimRecord) -> None:
        """Register one manuscript claim."""
        self.claims.append(claim)

    def is_ready(self) -> bool:
        """Return True when the run has artifacts and ready claims."""
        return bool(self.artifacts) and bool(self.claims) and all(
            claim.is_ready() for claim in self.claims
        )


def hello_dropin() -> str:
    """Return a smoke-test string for the drop-in module."""
    return "drop-in-ready"
