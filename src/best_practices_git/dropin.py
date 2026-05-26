"""Drop-in helpers for ML manuscript projects."""

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path


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

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-ready run dictionary."""
        return {
            "name": self.name,
            "status": "PASS" if self.is_ready() else "NEEDS_WORK",
            "metrics": self.metrics,
            "artifacts": self.artifacts,
            "claims": [asdict(claim) for claim in self.claims],
        }

    def to_json(self) -> str:
        """Return a formatted JSON run record."""
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def write_json(self, path: str | Path) -> Path:
        """Write the run record to a JSON file."""
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(self.to_json(), encoding="utf-8")
        return output_path


def hello_dropin() -> str:
    """Return a smoke-test string for the drop-in module."""
    return "drop-in-ready"
