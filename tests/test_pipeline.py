from pathlib import Path

from best_practices_git.pipeline import PipelineField, PipelineStage, default_pipeline


def test_pipeline_field_completion():
    empty_field = PipelineField(name="Outcome", prompt="Define the outcome")
    complete_field = PipelineField(name="Outcome", prompt="Define the outcome", value="Mortality")

    assert not empty_field.is_complete
    assert complete_field.is_complete


def test_pipeline_stage_reports_missing_fields():
    stage = PipelineStage(
        name="Research Query",
        artifact_path="artifacts/query/research-query.md",
        fields=(
            PipelineField("Problem", "State the problem", "A clear problem"),
            PipelineField("Outcome", "Define the outcome"),
        ),
    )

    assert stage.completion_ratio == 0.5
    assert stage.missing_fields() == ("Outcome",)


def test_default_pipeline_writes_artifact_templates(tmp_path: Path):
    pipeline = default_pipeline()
    pipeline.write_artifact_templates(tmp_path)

    expected = tmp_path / "artifacts/query/research-query.md"
    assert expected.exists()
    assert "# Research Query" in expected.read_text(encoding="utf-8")
