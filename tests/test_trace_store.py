import asyncio
from pathlib import Path

from app.trace_store import TraceStore


def _run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def test_trace_roundtrip(tmp_path: Path):
    store = TraceStore(tmp_path / "trace.sqlite")
    rec = store.recorder(channel="panel", session_id="s1", task_id="t1", query="q", use_model=False)
    rec.checkpoint("received")
    span = rec.start_tool_run("rag_retrieve", {"query": "q", "limit": 4})
    rec.finish_tool_run(span, status="ok", output={"hits": 2})
    rec.event("retrieval", {"hits": 2})
    rec.message("user", "q")
    rec.message("assistant", "a")
    rec.checkpoint("final")
    rec.finish(status="completed", route="concept", flags={"trace_id": rec.trace_id})
    asyncio.run(rec.flush())

    data = store.load_trace(rec.trace_id)
    assert data["task_run"]["status"] == "completed"
    assert data["task_run"]["route"] == "concept"
    assert data["task_run"]["channel"] == "panel"
    assert len(data["tool_runs"]) == 1
    assert data["tool_runs"][0]["tool_name"] == "rag_retrieve"
    assert data["tool_runs"][0]["status"] == "ok"
    assert {c["stage"] for c in data["checkpoints"]} == {"received", "final"}
    assert len(data["events"]) == 1


def test_double_flush_is_idempotent(tmp_path: Path):
    store = TraceStore(tmp_path / "trace.sqlite")
    rec = store.recorder(channel="a2a", session_id="s2", task_id="t2", query="q2", use_model=True)
    rec.checkpoint("received")
    rec.finish(status="completed", route="method_selection")
    asyncio.run(rec.flush())
    asyncio.run(rec.flush())  # 第二次 flush 不应产生重复 checkpoint

    data = store.load_trace(rec.trace_id)
    assert len(data["checkpoints"]) == 1
    assert data["task_run"]["use_model"] == 1


def test_flush_failure_is_silent(tmp_path: Path):
    store = TraceStore(tmp_path / "trace.sqlite")
    rec = store.recorder(channel="panel", session_id="s3", task_id="t3", query="q3", use_model=False)
    store.db_path = Path("/nonexistent_dir_xyz/trace.sqlite")  # 迫使写失败
    rec.finish(status="completed")
    asyncio.run(rec.flush())  # 不应抛异常
