"""Opt-in real-model checks of critical followups, using saved synthetic math dialogue.

Run: python scripts/followup_acceptance.py
Uses a temporary empty database. Reads no notes or production chat history.
The saved calculus run is the baseline; new questions use the current product path.
"""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


async def run(source: Path, output: Path) -> None:
    from app.artifact_jobs import ArtifactService
    from app.model_client import OpenAICompatibleClient
    from app.panel_store import PanelStore
    from app.settings import settings

    baseline = json.loads(source.read_text(encoding="utf-8"))
    assert baseline["case"] == "圆的切线、梯度与极坐标换元"
    assert baseline["status"] == "passed" and len(baseline["rounds"]) == 5
    output.mkdir(parents=True, exist_ok=True)
    client = OpenAICompatibleClient(settings)
    assert client.enabled, "Configured model is unavailable"
    timings, proposals, reviews, failures, calls = {}, {}, {}, {}, []

    class ObservedClient:
        enabled = True

        async def complete(self, messages, **kwargs):
            payload = json.loads(messages[-1].content)
            query = payload["本轮问题"]
            stage = "review" if "候选问题" in payload else "proposal"
            started = time.monotonic()
            try:
                raw = await client.complete(messages, **kwargs)
                (reviews if stage == "review" else proposals)[query] = json.loads(raw)
                return raw
            except Exception as exc:
                failures[query] = type(exc).__name__
                raise
            finally:
                seconds = round(time.monotonic() - started, 2)
                timings[query] = round(timings.get(query, 0) + seconds, 2)
                calls.append({"stage": stage, "seconds": seconds})
                print(json.dumps({"completed_call": len(calls), "stage": stage, "seconds": seconds}, ensure_ascii=False), flush=True)

    with tempfile.TemporaryDirectory(prefix="critical-followups-") as temporary:
        store = PanelStore(Path(temporary) / "panel.sqlite")
        service = ArtifactService(store, ObservedClient())
        cases = []
        for index, item in enumerate(baseline["rounds"], 1):
            mid = store.begin_turn("calculus", f"calculus-{index}", item["query"], {"route": "concept"})
            store.finish_turn(mid, item["content"], "completed", {"route": "concept"})
            cases.append({"id": f"calculus-{index}", "session_id": "calculus", "message_id": mid,
                          "query": item["query"], "baseline": item.get("followups", [])})

        holdouts = [
            ("clt", "样本量大以后，原始数据就变成正态吗？",
             "不会。中心极限定理描述的是样本均值的抽样分布。在独立同分布且方差有限的条件下，"
             "标准化的样本均值趋于标准正态。原始数据的总体分布可以一直偏态。"),
            ("pvalue", "p=0.03就说明这个效果很有用吗？",
             "不能。p值是在零假设成立时，得到当前或更极端结果的概率；它不等于零假设为真的概率。"
             "实际意义需要看差异的大小，p值不等于效果大小。"),
            ("thanks", "谢谢，今天先到这里。", "不客气，休息一下。"),
        ]
        for name, query, answer in holdouts:
            mid = store.begin_turn(name, name, query, {"route": "concept"})
            store.finish_turn(mid, answer, "completed", {"route": "concept"})
            cases.append({"id": name, "session_id": name, "message_id": mid, "query": query, "baseline": []})

        await client.start()
        try:
            for case in cases:
                service.discover(case["session_id"], case["message_id"])
            await asyncio.gather(*list(service.discoveries.values()))
            results = []
            for case in cases:
                message = store.message(case["session_id"], case["message_id"])
                results.append({**case, "state": message.get("followups_state"),
                                "seconds": timings.get(case["query"]),
                                "suggestions": message.get("followups", []),
                                "proposals": proposals.get(case["query"], {}).get("followups", []),
                                "review": reviews.get(case["query"]),
                                "reviewed": message.get("followups_reviewed", False),
                                "canvas_offers": store.offers(case["session_id"]),
                                "error_type": failures.get(case["query"])})
            report = {"status": "awaiting_semantic_review", "model": settings.model_name,
                      "calls": len(calls), "call_timings": calls, "cases": results,
                      "limits": ["Model judgments require semantic review; structural validation is not a correctness guarantee.",
                                 "The baseline was saved from the earlier live run, not a randomized controlled comparison."]}
            (output / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
            assert len(timings) == len(cases) and len(calls) <= len(cases) * 2
            assert all(item["state"] == "completed" for item in results), "Some model judgments did not complete"
            assert all(item["reviewed"] for item in results)
            assert results[0]["suggestions"]  # Quality filtering need not fill a fixed number of buttons.
            assert not results[-1]["suggestions"] and not results[-1]["canvas_offers"]
            for item in results:
                print(json.dumps({"case": item["id"], "seconds": item["seconds"],
                                  "questions": [q["label"] for q in item["suggestions"]]}, ensure_ascii=False), flush=True)
        finally:
            await service.stop()
            await client.aclose()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "build/calculus-acceptance-final/results.json")
    parser.add_argument("--output", type=Path, default=ROOT / "build/followup-acceptance")
    arguments = parser.parse_args()
    asyncio.run(run(arguments.source, arguments.output))
