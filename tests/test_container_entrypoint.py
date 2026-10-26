"""Container boots index an empty volume once and preserve subsequent user data."""
from __future__ import annotations

import os
from pathlib import Path
import sqlite3
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def boot(data: Path, corpus: Path, *, auto_index: bool = True):
    env = {**os.environ, "DATA_DIR": str(data), "CORPUS_WHITELIST": str(corpus),
           "CORPUS_AUTO_INDEX": str(auto_index).lower(), "MODEL_ENABLED": "false"}
    return subprocess.run(
        [sys.executable, "-m", "scripts.container_entrypoint", sys.executable,
         "-c", "print('application-started')"], cwd=ROOT, env=env,
        capture_output=True, text=True, encoding="utf-8", timeout=30,
    )


def test_first_boot_indexes_and_second_boot_preserves_existing_data(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "note.md").write_text("# Normal distribution\nA normal distribution has a mean and variance.", encoding="utf-8")
    data = tmp_path / "data"
    first = boot(data, corpus)
    assert first.returncode == 0, first.stderr
    assert "application-started" in first.stdout
    with sqlite3.connect(data / "a2a.sqlite") as db:
        count = db.execute("SELECT COUNT(*) FROM corpus_chunks").fetchone()[0]
        assert count > 0
        db.execute("CREATE TABLE deployment_user_data (value TEXT)")
        db.execute("INSERT INTO deployment_user_data VALUES ('keep-me')")
    # A new default corpus must not replace the user's already populated index.
    (corpus / "new.md").write_text("# New material\nNew release material.", encoding="utf-8")
    second = boot(data, corpus)
    assert second.returncode == 0, second.stderr
    with sqlite3.connect(data / "a2a.sqlite") as db:
        assert db.execute("SELECT COUNT(*) FROM corpus_chunks").fetchone()[0] == count
        assert db.execute("SELECT value FROM deployment_user_data").fetchone()[0] == "keep-me"


def test_auto_index_can_be_disabled(tmp_path):
    data = tmp_path / "data"
    result = boot(data, tmp_path / "corpus", auto_index=False)
    assert result.returncode == 0, result.stderr
    assert "application-started" in result.stdout
    assert not (data / "a2a.sqlite").exists()


def test_missing_optional_corpus_still_starts_the_application(tmp_path):
    result = boot(tmp_path / "data", tmp_path / "absent")
    assert result.returncode == 0, result.stderr
    assert "No corpus files found" in result.stdout
    assert "application-started" in result.stdout
