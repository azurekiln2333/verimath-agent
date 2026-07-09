from __future__ import annotations

import asyncio
import json
import sqlite3
import time
import uuid
from pathlib import Path
from typing import Any

_SCHEMA = """
CREATE TABLE IF NOT EXISTS task_runs (
    id TEXT PRIMARY KEY,
    created_at REAL NOT NULL,
    finished_at REAL,
    channel TEXT NOT NULL,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    query TEXT NOT NULL,
    route TEXT,
    status TEXT NOT NULL,
    use_model INTEGER NOT NULL DEFAULT 0,
    flags_json TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trace_id TEXT NOT NULL,
    session_id TEXT NOT NULL,
    seq INTEGER NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS tool_runs (
    id TEXT PRIMARY KEY,
    trace_id TEXT NOT NULL,
    parent_span_id TEXT,
    tool_name TEXT NOT NULL,
    seq INTEGER NOT NULL,
    started_at REAL NOT NULL,
    finished_at REAL,
    duration_ms REAL,
    status TEXT NOT NULL,
    input_json TEXT NOT NULL,
    output_json TEXT,
    error_type TEXT
);
"""
_SCHEMA_2 = """
CREATE TABLE IF NOT EXISTS traces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trace_id TEXT NOT NULL,
    ts REAL NOT NULL,
    event_type TEXT NOT NULL,
    payload_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS checkpoints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trace_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    ts REAL NOT NULL,
    state_json TEXT NOT NULL
);
"""

_INDEXES = """
CREATE INDEX IF NOT EXISTS idx_task_runs_created ON task_runs(created_at);
CREATE INDEX IF NOT EXISTS idx_task_runs_session ON task_runs(session_id);
CREATE INDEX IF NOT EXISTS idx_messages_trace ON messages(trace_id);
CREATE INDEX IF NOT EXISTS idx_tool_runs_trace ON tool_runs(trace_id);
CREATE INDEX IF NOT EXISTS idx_traces_trace ON traces(trace_id);
CREATE INDEX IF NOT EXISTS idx_checkpoints_trace ON checkpoints(trace_id);
"""


class TraceStore:
    """独立的 trace SQLite 存储。与主库隔离，开 WAL 降并发锁。"""

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init(self) -> None:
        with self._connect() as conn:
            conn.executescript(_SCHEMA)
            conn.executescript(_SCHEMA_2)
            conn.executescript(_INDEXES)

    def recorder(self, *, channel: str, session_id: str, task_id: str, query: str, use_model: bool) -> "TraceRecorder":
        return TraceRecorder(
            store=self,
            channel=channel,
            session_id=session_id,
            task_id=task_id,
            query=query,
            use_model=use_model,
        )

    def load_trace(self, trace_id: str) -> dict[str, Any]:
        """按 trace_id 回放：读回 task_run + 关联表，供审计/回放。"""
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            task = conn.execute("SELECT * FROM task_runs WHERE id = ?", (trace_id,)).fetchone()
            tool_runs = conn.execute(
                "SELECT * FROM tool_runs WHERE trace_id = ? ORDER BY seq", (trace_id,)
            ).fetchall()
            checkpoints = conn.execute(
                "SELECT * FROM checkpoints WHERE trace_id = ? ORDER BY ts", (trace_id,)
            ).fetchall()
            events = conn.execute(
                "SELECT * FROM traces WHERE trace_id = ? ORDER BY ts", (trace_id,)
            ).fetchall()
        return {
            "task_run": dict(task) if task else None,
            "tool_runs": [dict(r) for r in tool_runs],
            "checkpoints": [dict(r) for r in checkpoints],
            "events": [dict(r) for r in events],
        }


def _now() -> float:
    return time.time()


class TraceRecorder:
    """请求内只在内存攒 span/event，落库统一走 to_thread，失败静默（旁路不影响主链）。"""

    def __init__(self, *, store: TraceStore, channel: str, session_id: str, task_id: str, query: str, use_model: bool) -> None:
        self._store = store
        self.trace_id = uuid.uuid4().hex
        self.channel = channel
        self.session_id = session_id
        self.task_id = task_id
        self.query = query
        self.use_model = use_model
        self.created_at = _now()
        self.finished_at: float | None = None
        self.route: str | None = None
        self.status = "running"
        self.flags: dict[str, Any] = {}
        self._tool_runs: list[dict[str, Any]] = []
        self._checkpoints: list[dict[str, Any]] = []
        self._events: list[dict[str, Any]] = []
        self._messages: list[dict[str, Any]] = []
        self._seq = 0

    def checkpoint(self, stage: str, state: dict[str, Any] | None = None) -> None:
        self._checkpoints.append({"stage": stage, "ts": _now(), "state": state or {}})

    def event(self, event_type: str, payload: dict[str, Any] | None = None) -> None:
        self._events.append({"event_type": event_type, "ts": _now(), "payload": payload or {}})

    def message(self, role: str, content: str) -> None:
        self._seq += 1
        self._messages.append({"seq": self._seq, "role": role, "content": content, "ts": _now()})

    def start_tool_run(self, tool_name: str, payload: dict[str, Any], parent_span_id: str | None = None) -> dict[str, Any]:
        self._seq += 1
        span = {
            "id": uuid.uuid4().hex,
            "parent_span_id": parent_span_id,
            "tool_name": tool_name,
            "seq": self._seq,
            "started_at": _now(),
            "finished_at": None,
            "duration_ms": None,
            "status": "running",
            "input": payload,
            "output": None,
            "error_type": None,
        }
        self._tool_runs.append(span)
        return span

    def finish_tool_run(self, span: dict[str, Any], *, status: str, output: Any = None, error_type: str | None = None) -> None:
        span["finished_at"] = _now()
        span["duration_ms"] = round((span["finished_at"] - span["started_at"]) * 1000, 3)
        span["status"] = status
        span["output"] = output
        span["error_type"] = error_type

    def finish(self, *, status: str, route: str | None = None, flags: dict[str, Any] | None = None) -> None:
        self.status = status
        self.route = route
        self.finished_at = _now()
        if flags:
            self.flags = flags

    async def flush(self) -> None:
        try:
            await asyncio.to_thread(self._flush_sync)
        except Exception:
            pass  # trace 是旁路，落库失败绝不影响主链

    def _flush_sync(self) -> None:
        with self._store._connect() as conn:
            conn.execute(
                """
                INSERT INTO task_runs (id, created_at, finished_at, channel, session_id,
                    task_id, query, route, status, use_model, flags_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    finished_at=excluded.finished_at, route=excluded.route,
                    status=excluded.status, flags_json=excluded.flags_json
                """,
                (
                    self.trace_id, self.created_at, self.finished_at, self.channel,
                    self.session_id, self.task_id, self.query, self.route, self.status,
                    1 if self.use_model else 0, json.dumps(self.flags, ensure_ascii=False),
                ),
            )
            for m in self._messages:
                conn.execute(
                    "INSERT INTO messages (trace_id, session_id, seq, role, content, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                    (self.trace_id, self.session_id, m["seq"], m["role"], m["content"], m["ts"]),
                )
            for s in self._tool_runs:
                conn.execute(
                    """
                    INSERT INTO tool_runs (id, trace_id, parent_span_id, tool_name, seq,
                        started_at, finished_at, duration_ms, status, input_json, output_json, error_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        finished_at=excluded.finished_at, duration_ms=excluded.duration_ms,
                        status=excluded.status, output_json=excluded.output_json, error_type=excluded.error_type
                    """,
                    (
                        s["id"], self.trace_id, s["parent_span_id"], s["tool_name"], s["seq"],
                        s["started_at"], s["finished_at"], s["duration_ms"], s["status"],
                        json.dumps(s["input"], ensure_ascii=False),
                        None if s["output"] is None else json.dumps(s["output"], ensure_ascii=False),
                        s["error_type"],
                    ),
                )
            self._flush_events(conn)

    def _flush_events(self, conn: sqlite3.Connection) -> None:
        for c in self._checkpoints:
            conn.execute(
                "INSERT INTO checkpoints (trace_id, stage, ts, state_json) VALUES (?, ?, ?, ?)",
                (self.trace_id, c["stage"], c["ts"], json.dumps(c["state"], ensure_ascii=False)),
            )
        for e in self._events:
            conn.execute(
                "INSERT INTO traces (trace_id, ts, event_type, payload_json) VALUES (?, ?, ?, ?)",
                (self.trace_id, e["ts"], e["event_type"], json.dumps(e["payload"], ensure_ascii=False)),
            )
        self._messages.clear()
        self._tool_runs_flushed()

    def _tool_runs_flushed(self) -> None:
        self._checkpoints.clear()
        self._events.clear()
