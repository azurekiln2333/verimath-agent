"""Initialize an empty persistent corpus, then replace this process with the app."""
from __future__ import annotations

import os
import subprocess
import sys


def initialize_corpus() -> None:
    if os.getenv("CORPUS_AUTO_INDEX", "true").lower() not in {"1", "true", "yes", "on"}:
        return

    from app.rag.store import KeywordRetriever
    from app.rag.whitelist import iter_allowed_files
    from app.settings import settings

    retriever = KeywordRetriever(settings.sqlite_path)
    if retriever.stats()["chunks"]:
        print("Corpus already populated; preserving the existing index.", flush=True)
        return
    if not iter_allowed_files(settings.corpus_paths):
        print("No corpus files found; starting without a knowledge index.", flush=True)
        return
    print("Initializing the knowledge index in the persistent data directory.", flush=True)
    subprocess.run([sys.executable, "-m", "scripts.build_corpus"], check=True)


def main() -> None:
    command = sys.argv[1:]
    if not command:
        raise SystemExit("A container command is required.")
    initialize_corpus()
    os.execvp(command[0], command)


if __name__ == "__main__":
    main()
