# -*- coding: utf-8 -*-
"""线代内核答案基准回归：把 eval/seeds_linalg.jsonl 的每条答案用内核
verify_answer 重算比对，报告通过率。答案基准由 gen_linalg_seeds.py 生成
（确定性随机 + W2 手工精选），本脚本是它的验证端。

用法：
  .venv/Scripts/python.exe scripts/run_linalg_eval.py            # 全量
  .venv/Scripts/python.exe scripts/run_linalg_eval.py --op det   # 单算子
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from app.linalg.tool import verify_answer


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("eval/seeds_linalg.jsonl"))
    parser.add_argument("--op", default="", help="只跑指定算子（如 det/jordan）")
    args = parser.parse_args()

    seeds = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.op:
        seeds = [s for s in seeds if s["operation"] == args.op]

    ok_counts: Counter[str] = Counter()
    total_counts: Counter[str] = Counter()
    failures: list[str] = []
    for s in seeds:
        op = s["operation"]
        total_counts[op] += 1
        ok, actual = verify_answer(
            op, s["matrix"], s["expected"], b=s.get("b"),
        )
        if ok:
            ok_counts[op] += 1
        else:
            failures.append(f"{s['id']} op={op} expected={s['expected'][:60]} actual={actual[:60]}")

    total = len(seeds)
    passed = sum(ok_counts.values())
    print(f"linalg 答案基准：{passed}/{total} 通过")
    for op in sorted(total_counts):
        print(f"  {op:<16} {ok_counts[op]}/{total_counts[op]}")
    if failures:
        print("失败样例：")
        for line in failures[:10]:
            print("  " + line)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
