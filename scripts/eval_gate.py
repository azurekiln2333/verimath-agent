from __future__ import annotations

"""质量回归 gate：跑黄金集 → 对比上次基准 → 红绿灯 → 退化则 exit 1。

用法：
  python -m scripts.eval_gate            # 跑并存基准，与上次 golden 对比
  python -m scripts.eval_gate --no-save  # 只看不存
  python -m scripts.eval_gate --tol 0.02 # 容差（默认 0，退化即红）
"""

import argparse
import json
from pathlib import Path
from typing import Any

from app.agents import TutorRouter
from app.eval_metrics import run_golden_eval
from app.rag.store import KeywordRetriever
from app.settings import settings
from app.test_records import TestRecordStore

# 越大越好、参与红绿灯判定的核心指标
CORE_METRICS = ("route_accuracy", "retrieval_hit_rate", "guard_recall")


def load_items(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            items.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no} 不是合法 JSONL") from exc
    return items


def compare(current: dict[str, Any], baseline: dict[str, Any] | None, tol: float) -> tuple[list[str], bool]:
    """逐核心指标对比，返回（红绿灯行, 是否有退化）。"""
    lines: list[str] = []
    regressed = False
    for m in CORE_METRICS:
        cur = float(current.get(m, 0.0))
        if baseline is None:
            lines.append(f"  {m:<20} {cur:.4f}  (首次基准，无对比)")
            continue
        base = float(baseline.get(m, 0.0))
        delta = cur - base
        if delta > tol:
            mark = "↑ 改善"
        elif delta < -tol:
            mark = "↓ 退化"
            regressed = True
        else:
            mark = "= 持平"
        lines.append(f"  {m:<20} {base:.4f} → {cur:.4f}  {mark} ({delta:+.4f})")
    return lines, regressed


def main() -> int:
    parser = argparse.ArgumentParser(description="黄金集质量回归 gate")
    parser.add_argument("--input", type=Path, default=Path("eval/golden.jsonl"))
    parser.add_argument("--no-save", action="store_true", help="只看不存")
    parser.add_argument("--tol", type=float, default=0.0, help="退化容差，默认 0")
    args = parser.parse_args()

    items = load_items(args.input)
    router = TutorRouter()
    retriever = KeywordRetriever(settings.sqlite_path)

    def predict_route(query: str) -> str:
        retrieved = [c.as_dict() for c in retriever.search(query, limit=settings.retrieval_limit)]
        return router.answer(query, retrieved).route

    def retrieve(query: str) -> list[dict[str, Any]]:
        return [c.as_dict() for c in retriever.search(query, limit=settings.retrieval_limit)]

    report = run_golden_eval(items, predict_route, retrieve)

    store = TestRecordStore(settings.data_dir)
    prev = store.recent_eval_runs(limit=1, kind="golden_eval")
    baseline = prev[0]["report"] if prev else None

    lines, regressed = compare(report, baseline, args.tol)
    print("=== 黄金集质量回归 ===")
    print(f"样本数 total={report['total']}")
    print("\n".join(lines))
    if report["misroute_examples"]:
        print(f"误路由 {len(report['misroute_examples'])} 例：{report['misroute_examples'][:5]}")
    if report["miss_examples"]:
        print(f"检索漏命中 {len(report['miss_examples'])} 例：{report['miss_examples'][:5]}")

    if not args.no_save:
        store.append_eval_run(report, input_path=str(args.input), limit=None, kind="golden_eval")

    if regressed:
        print("\n[RED] 检测到质量退化，gate 失败（exit 1）。")
        return 1
    print("\n[GREEN] 无退化，gate 通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
