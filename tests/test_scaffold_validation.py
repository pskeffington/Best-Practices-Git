from best_practices_git.scaffold_validation import validate_scaffold


def test_valid_project(tmp_path):
    for name in ("README.md", "docs/protocol.md", "docs/data_dictionary.md", "docs/source_register.md"):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("synthetic example", encoding="utf-8")
    assert validate_scaffold(tmp_path) == {"ok": True, "missing": [], "blocked_paths": []}


def test_missing_docs_and_sensitive_filename_are_reported(tmp_path):
    (tmp_path / ".env").write_text("placeholder", encoding="utf-8")
    result = validate_scaffold(tmp_path)
    assert result["ok"] is False
    assert "docs/protocol.md" in result["missing"]
    assert result["blocked_paths"] == [".env"]


def test_symlink_fails_closed(tmp_path):
    target = tmp_path / "target.txt"
    target.write_text("synthetic", encoding="utf-8")
    (tmp_path / "shortcut.txt").symlink_to(target)
    assert "shortcut.txt" in validate_scaffold(tmp_path)["blocked_paths"]


def test_sensitive_filename_patterns(tmp_path):
    for filename in (".env.production", "export.pem", "identity.p12", "patient_records_2026.csv"):
        (tmp_path / filename).write_text("synthetic", encoding="utf-8")
    result = validate_scaffold(tmp_path)
    assert sorted(result["blocked_paths"]) == sorted((
        ".env.production", "export.pem", "identity.p12", "patient_records_2026.csv"
    ))


def test_excluded_virtual_environment(tmp_path):
    folder = tmp_path / ".venv"
    folder.mkdir()
    (folder / ".env.local").write_text("synthetic", encoding="utf-8")
    assert validate_scaffold(tmp_path)["blocked_paths"] == []


def test_template_has_required_research_sections():
    from pathlib import Path
    template = (Path(__file__).resolve().parents[1] / "templates/biomedical-research/README.template.md").read_text(encoding="utf-8")
    for heading in ("## Status and scope", "## Quick start", "## Methods and provenance", "## Results and interpretation", "## Review and release"):
        assert heading in template
