from best_practices_git.claims import ClaimLevel, EvidenceSource, ManuscriptClaim


def test_evidence_source_requires_path_and_description():
    valid = EvidenceSource(
        artifact_path="artifacts/results/result-bundle.md",
        description="Model comparison table",
    )
    invalid = EvidenceSource(artifact_path="", description="Missing path")

    assert valid.is_valid()
    assert not invalid.is_valid()


def test_claim_requires_valid_evidence():
    claim = ManuscriptClaim(
        text="The model improved over baseline performance.",
        level=ClaimLevel.COMPARATIVE,
        evidence_sources=(
            EvidenceSource(
                artifact_path="artifacts/results/result-bundle.md",
                description="Baseline and candidate model comparison",
            ),
        ),
        boundary_note="Internal validation only; external validation is required before generalization.",
    )

    assert claim.has_evidence()
    assert claim.is_publication_ready()


def test_claim_without_boundary_is_not_publication_ready():
    claim = ManuscriptClaim(
        text="The model predicted the outcome.",
        level=ClaimLevel.PREDICTIVE,
        evidence_sources=(
            EvidenceSource(
                artifact_path="artifacts/validation/validation-plan.md",
                description="Held-out validation design",
            ),
        ),
    )

    assert claim.has_evidence()
    assert not claim.is_publication_ready()
