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
