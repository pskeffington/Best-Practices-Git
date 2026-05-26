"""Drop-in helpers for ML manuscript projects."""

from dataclasses import dataclass


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


def hello_dropin() -> str:
    """Return a smoke-test string for the drop-in module."""
    return "drop-in-ready"
