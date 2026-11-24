"""Deterministic, offline checks for a biomedical research repository scaffold."""
from __future__ import annotations

from pathlib import Path
import fnmatch

REQUIRED = ("README.md", "docs/protocol.md", "docs/data_dictionary.md", "docs/source_register.md")
BLOCKED_NAMES = {".env", "id_rsa", "credentials.json", "patient_records.csv"}
BLOCKED_PATTERNS = (".env.*", "*.pem", "*.p12", "*.pfx", "*_private_key", "patient_records*.csv")
EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__"}

def validate_scaffold(root: Path) -> dict:
    """Return a compact report; never open or emit sensitive file contents."""
    root = Path(root)
    if not root.is_dir() or root.is_symlink():
        return {"ok": False, "missing": list(REQUIRED), "blocked_paths": ["invalid-root"]}
    missing = [name for name in REQUIRED if not (root / name).is_file() or (root / name).is_symlink()]
    blocked = []
    for candidate in root.rglob("*"):
        rel = candidate.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if candidate.is_symlink() or (candidate.is_file() and (candidate.name.lower() in BLOCKED_NAMES or any(fnmatch.fnmatchcase(candidate.name.lower(), pattern) for pattern in BLOCKED_PATTERNS))):
            blocked.append(str(rel))
    return {"ok": not missing and not blocked, "missing": missing, "blocked_paths": sorted(blocked)}
