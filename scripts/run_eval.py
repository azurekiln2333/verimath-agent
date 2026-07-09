from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from app.agents import TutorRouter
from app.rag.store import KeywordRetriever
from app.settings import settings
from app.test_records import TestRecordStore


def load_items(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            items.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no} is not valid JSONL") from exc
    return items


def evaluate(items: list[dict[str, Any]], limit: int | None = None) -> dict[str, Any]:
    router = TutorRouter()
    retriever = KeywordRetriever(settings.sqlite_path)
    route_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    category_source_hits: Counter[str] = Counter()
    no_source_examples: dict[str, list[str]] = defaultdict(list)
    guard_examples: list[str] = []
    clarification_count = 0
    source_hit_count = 0

    selected = items[:limit] if limit else items
    for item in selected:
        query = str(item.get("query", ""))
        category = str(item.get("category", "uncategorized"))
        retrieved = [chunk.as_dict() for chunk in retriever.search(query, limit=settings.retrieval_limit)]
        answer = router.answer(query, retrieved)
        route_counts[answer.route] += 1
        category_counts[category] += 1
        if answer.requires_clarification:
            clarification_count += 1
        if answer.sources:
            source_hit_count += 1
            category_source_hits[category] += 1
        elif len(no_source_examples[category]) < 3:
            no_source_examples[category].append(str(item.get("id", query[:30])))
        if answer.route == "guard" and len(guard_examples) < 5:
            guard_examples.append(str(item.get("id", query[:30])))

    return {
        "total": len(selected),
        "route_counts": dict(route_counts),
        "category_counts": dict(category_counts),
        "clarification_count": clarification_count,
        "source_hit_count": source_hit_count,
        "source_hit_rate": round(source_hit_count / len(selected), 4) if selected else 0,
        "category_source_hits": dict(category_source_hits),
        "no_source_examples": dict(no_source_examples),
        "guard_examples": guard_examples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline eval runner for seed questions.")
    parser.add_argument("--input", type=Path, default=Path("eval/eval_seed.jsonl"))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--no-save", action="store_true", help="Print the report without saving it.")
    args = parser.parse_args()
    items = load_items(args.input)
    report = evaluate(items, args.limit)
    if not args.no_save:
        TestRecordStore(settings.data_dir).append_eval_run(
            report,
            input_path=str(args.input),
            limit=args.limit,
        )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
