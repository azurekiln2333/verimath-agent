import json
from pathlib import Path

from app.eval_metrics import (
    VALID_ROUTES,
    guard_recall,
    retrieval_hit_rate,
    route_accuracy,
    run_golden_eval,
)

GOLDEN_PATH = Path(__file__).resolve().parent.parent / "eval" / "golden.jsonl"


def _chunk(topic="", text=""):
    return {"text": text, "metadata": {"topic": topic}}


def test_route_accuracy_counts_exact_matches():
    items = [{"expected_route": "concept"}, {"expected_route": "guard"}]
    assert route_accuracy(items, ["concept", "guard"]) == 1.0
    assert route_accuracy(items, ["concept", "concept"]) == 0.5
    assert route_accuracy([], []) == 0.0


def test_retrieval_hit_rate_only_scores_must_retrieve():
    items = [
        {"expected_topics": ["中心极限定理"], "must_retrieve": True},
        {"expected_topics": ["方差"], "must_retrieve": False},  # 不计分
    ]
    retrievals = [[_chunk(topic="中心极限定理")], []]
    assert retrieval_hit_rate(items, retrievals) == 1.0


def test_retrieval_hit_rate_detects_wrong_topic():
    # 返回了来源，但 topic 不对 —— 虚假 source_hit_rate 会算命中，真指标应判失分。
    items = [{"expected_topics": ["中心极限定理"], "must_retrieve": True}]
    retrievals = [[_chunk(topic="t检验", text="两样本均值比较")]]
    assert retrieval_hit_rate(items, retrievals) == 0.0


def test_guard_recall_catches_missed_guard():
    items = [{"expected_route": "guard"}, {"expected_route": "guard"}]
    assert guard_recall(items, ["guard", "concept"]) == 0.5
    assert guard_recall([{"expected_route": "concept"}], ["concept"]) == 1.0


def test_run_golden_eval_report_shape():
    items = [
        {"id": "a", "query": "q1", "expected_route": "concept",
         "expected_topics": ["中心极限定理"], "must_retrieve": True},
        {"id": "b", "query": "q2", "expected_route": "guard",
         "expected_topics": [], "must_retrieve": False},
    ]
    report = run_golden_eval(
        items,
        predict_route=lambda q: "concept" if q == "q1" else "guard",
        retrieve=lambda q: [_chunk(topic="中心极限定理")] if q == "q1" else [],
    )
    for key in ("total", "route_accuracy", "retrieval_hit_rate", "guard_recall",
                "per_route_accuracy", "route_counts", "misroute_examples", "miss_examples"):
        assert key in report
    assert report["total"] == 2
    assert report["route_accuracy"] == 1.0
    assert report["retrieval_hit_rate"] == 1.0
    assert report["guard_recall"] == 1.0


def test_golden_set_is_wellformed():
    lines = [l for l in GOLDEN_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(lines) >= 25
    seen_ids = set()
    for line in lines:
        it = json.loads(line)
        assert it["id"] not in seen_ids, f"重复 id: {it['id']}"
        seen_ids.add(it["id"])
        assert it["expected_route"] in VALID_ROUTES
        assert isinstance(it["must_retrieve"], bool)
        if it["must_retrieve"]:
            assert it["expected_topics"], f"{it['id']} must_retrieve 却无 expected_topics"


def test_store_kind_filter(tmp_path):
    from app.test_records import TestRecordStore

    store = TestRecordStore(tmp_path, db_path=tmp_path / "t.sqlite")
    store.append_eval_run({"total": 1}, input_path="x", limit=1, kind="offline_eval")
    store.append_eval_run({"total": 2}, input_path="y", limit=1, kind="golden_eval")
    golden = store.recent_eval_runs(limit=10, kind="golden_eval")
    assert len(golden) == 1 and golden[0]["report"]["total"] == 2
    assert len(store.recent_eval_runs(limit=10)) == 2  # 默认不过滤
