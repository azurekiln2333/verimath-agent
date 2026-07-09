from __future__ import annotations

"""质量度量：机器可判定的路由/检索/守门指标。纯函数，不依赖 FastAPI。

替代 run_eval 里的虚假 source_hit_rate（只测"有没有来源"）：
retrieval_hit_rate 测"返回的对不对"——命中 chunk 是否含期望 topic。
"""

from typing import Any, Callable

VALID_ROUTES = {"concept", "method_selection", "learning_path", "exercise", "guard"}


def _chunk_haystack(chunk: dict[str, Any]) -> str:
    """把一个检索 chunk 的可判定文本拼成小写大字符串，供 topic 命中判断。"""
    meta = chunk.get("metadata", {}) if isinstance(chunk, dict) else {}
    parts = [
        str(chunk.get("text", "")),
        str(meta.get("topic", "")),
        str(meta.get("title", "")),
        str(meta.get("chapter", "")),
        str(meta.get("course", "")),
    ]
    return " ".join(parts).lower()


def _retrieval_hits_topic(retrieved: list[dict[str, Any]], expected_topics: list[str]) -> bool:
    """检索结果里任一 chunk 命中任一期望 topic 关键词即算命中。"""
    if not expected_topics:
        return bool(retrieved)
    hay = " ".join(_chunk_haystack(c) for c in retrieved)
    return any(t.lower() in hay for t in expected_topics if t)


def route_accuracy(items: list[dict[str, Any]], preds: list[str]) -> float:
    """路由预测准确率。items 与 preds 一一对应。"""
    if not items:
        return 0.0
    correct = sum(1 for it, p in zip(items, preds) if it.get("expected_route") == p)
    return round(correct / len(items), 4)


def retrieval_hit_rate(
    items: list[dict[str, Any]], retrievals: list[list[dict[str, Any]]]
) -> float:
    """真检索命中率：仅在 must_retrieve=true 的项上计分。
    must_retrieve=false（本地本不该覆盖）不参与分母，避免惩罚正确的"未覆盖"。"""
    scored = [(it, r) for it, r in zip(items, retrievals) if it.get("must_retrieve")]
    if not scored:
        return 1.0
    hits = sum(1 for it, r in scored if _retrieval_hits_topic(r, it.get("expected_topics", [])))
    return round(hits / len(scored), 4)


def guard_recall(items: list[dict[str, Any]], preds: list[str]) -> float:
    """守门召回：期望被守门的项里实际被守门的比例（防"该拦没拦"）。"""
    guard_items = [(it, p) for it, p in zip(items, preds) if it.get("expected_route") == "guard"]
    if not guard_items:
        return 1.0
    caught = sum(1 for _it, p in guard_items if p == "guard")
    return round(caught / len(guard_items), 4)


def _per_route_accuracy(items: list[dict[str, Any]], preds: list[str]) -> dict[str, float]:
    by_route: dict[str, list[bool]] = {}
    for it, p in zip(items, preds):
        exp = it.get("expected_route", "")
        by_route.setdefault(exp, []).append(exp == p)
    return {r: round(sum(v) / len(v), 4) for r, v in by_route.items() if v}


def run_golden_eval(
    items: list[dict[str, Any]],
    predict_route: Callable[[str], str],
    retrieve: Callable[[str], list[dict[str, Any]]],
) -> dict[str, Any]:
    """跑黄金集：predict_route(query)->route，retrieve(query)->chunks（as_dict 列表）。
    产出机器可判定报告，含 total 键（与 eval_runs 报告结构兼容）。"""
    preds: list[str] = []
    retrievals: list[list[dict[str, Any]]] = []
    misroute: list[dict[str, str]] = []
    miss: list[str] = []
    route_counts: dict[str, int] = {}
    for it in items:
        query = str(it.get("query", ""))
        route = predict_route(query)
        retrieved = retrieve(query)
        preds.append(route)
        retrievals.append(retrieved)
        route_counts[route] = route_counts.get(route, 0) + 1
        if it.get("expected_route") != route and len(misroute) < 20:
            misroute.append({"id": str(it.get("id", "")), "expected": it.get("expected_route", ""), "got": route})
        if it.get("must_retrieve") and not _retrieval_hits_topic(retrieved, it.get("expected_topics", [])):
            if len(miss) < 20:
                miss.append(str(it.get("id", "")))
    return {
        "total": len(items),
        "route_accuracy": route_accuracy(items, preds),
        "retrieval_hit_rate": retrieval_hit_rate(items, retrievals),
        "guard_recall": guard_recall(items, preds),
        "per_route_accuracy": _per_route_accuracy(items, preds),
        "route_counts": route_counts,
        "misroute_examples": misroute,
        "miss_examples": miss,
    }
