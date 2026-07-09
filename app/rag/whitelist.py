from __future__ import annotations

from pathlib import Path


ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt", ".md", ".markdown"}
BLOCKED_EXTENSIONS = {
    ".pem",
    ".key",
    ".pfx",
    ".p12",
    ".pyc",
    ".pyd",
    ".dll",
    ".exe",
    ".rar",
    ".zip",
    ".7z",
    ".db",
    ".sqlite",
}
BLOCKED_DIR_NAMES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "site-packages",
    "node_modules",
    ".gradle",
    ".idea",
}


def is_allowed_file(path: Path, whitelist_roots: list[Path] | tuple[Path, ...]) -> bool:
    resolved = path.resolve()
    if resolved.suffix.lower() in BLOCKED_EXTENSIONS:
        return False
    if resolved.suffix.lower() not in ALLOWED_EXTENSIONS:
        return False
    if any(part in BLOCKED_DIR_NAMES for part in resolved.parts):
        return False
    for root in whitelist_roots:
        try:
            resolved.relative_to(root.resolve())
            return True
        except ValueError:
            continue
    return False


def iter_allowed_files(whitelist_roots: list[Path] | tuple[Path, ...]) -> list[Path]:
    files: list[Path] = []
    for root in whitelist_roots:
        if not root.exists() or not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_file() and is_allowed_file(path, whitelist_roots):
                files.append(path)
    return sorted(files)

