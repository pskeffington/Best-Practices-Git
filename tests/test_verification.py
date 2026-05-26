from best_practices_git.claims import ClaimLevel, EvidenceSource, ManuscriptClaim
from best_practices_git.pipeline import PipelineField, PipelineStage, ResearchPipeline
from best_practices_git.standards import default_mappings
from best_practices_git.verification import PipelineVerifier


def test_verifier_detects_incomplete_pipeline():
    pipeline = ResearchPipeline(
        stages=(
            PipelineStage(
                name="Research Query",
                artifact_path="artifacts/query/research-query.md",
                fields=(PipelineField("Outcome", "Define the outcome"),),
            ),
        )
    )
    verifier = PipelineVerifier(pipeline=pipeline, mappings=default_mappings())

    result = verifier.verify_pipeline_completeness()

    assert not result.passed
    assert "Research Query" in result.messages[0]


def test_verifier_accepts_ready_claim():
    pipeline = ResearchPipeline(stages=())
    claim = ManuscriptClaim(
        text="The model improved over the baseline in internal validation.",
        level=ClaimLevel.COMPARATIVE,
        evidence_sources=(
            EvidenceSource(
                artifact_path="artifacts/results/result-bundle.md",
                description="Baseline comparison table",
            ),
        ),
        boundary_note="External validation is required before generalization.",
    )
    verifier = PipelineVerifier(
        pipeline=pipeline,
        mappings=default_mappings(),
        claims=(claim,),
    )

    result = verifier.verify_claim_readiness()

    assert result.passed


def test_verifier_run_all_returns_three_results():
    pipeline = ResearchPipeline(stages=())
    verifier = PipelineVerifier(pipeline=pipeline, mappings=default_mappings())

    results = verifier.run_all()

    assert len(results) == 3
