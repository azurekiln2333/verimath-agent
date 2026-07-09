from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from app.rag.loaders import chunk_document, load_document
from app.rag.store import KeywordRetriever
from app.rag.whitelist import iter_allowed_files
from app.settings import settings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--license-status",
        default="self_owned_or_authorized",
        help="Metadata label written to each chunk.",
    )
    parser.add_argument(
        "--include-policies",
        default="main,public",
        help="Comma-separated ingest policies to index. Default: main,public",
    )
    parser.add_argument(
        "--db-path",
        default="",
        help="Optional SQLite path override. Use this to build exam_corpus separately.",
    )
    args = parser.parse_args()
    include_policies = {part.strip() for part in args.include_policies.split(",") if part.strip()}
    files = iter_allowed_files(settings.corpus_paths)
    print(f"allowed files: {len(files)}")
    chunks = []
    skipped = 0
    skipped_by_policy = 0
    policy_counts: Counter[str] = Counter()
    doc_type_counts: Counter[str] = Counter()
    for path in files:
        try:
            document = load_document(path, license_status=args.license_status)
            ingest_policy = document.metadata.get("ingest_policy", "main")
            if include_policies and ingest_policy not in include_policies:
                skipped_by_policy += 1
                continue
            policy_counts[ingest_policy] += 1
            doc_type_counts[document.metadata.get("doc_type", "unknown")] += 1
            chunks.extend(chunk_document(document))
        except Exception as exc:
            skipped += 1
            print(f"skip: {path} ({exc})", file=sys.stderr)
    db_path = Path(args.db_path) if args.db_path else settings.sqlite_path
    count = KeywordRetriever(db_path).replace_chunks(chunks)
    print(
        f"indexed chunks: {count}; skipped files: {skipped}; "
        f"skipped by policy: {skipped_by_policy}; db: {db_path}"
    )
    if policy_counts:
        print("indexed policies:", ", ".join(f"{k}={v}" for k, v in sorted(policy_counts.items())))
    if doc_type_counts:
        print("indexed doc types:", ", ".join(f"{k}={v}" for k, v in sorted(doc_type_counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
