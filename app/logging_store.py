from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any


class InteractionLogger:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at REAL NOT NULL,
                    channel TEXT NOT NULL DEFAULT 'a2a',
                    session_id TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    route TEXT NOT NULL,
                    query TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    sources_json TEXT NOT NULL,
                    flags_json TEXT NOT NULL
                )
                """
            )
            columns = {
                row[1]
                for row in conn.execute("PRAGMA table_info(interactions)")
            }
            if "channel" not in columns:
                conn.execute("ALTER TABLE interactions ADD COLUMN channel TEXT NOT NULL DEFAULT 'a2a'")
            if "trace_id" not in columns:
                conn.execute("ALTER TABLE interactions ADD COLUMN trace_id TEXT")
            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_interactions_created_at
                ON interactions(created_at)
                """
            )

    def log(
        self,
        *,
        session_id: str,
        task_id: str,
        route: str,
        query: str,
        answer: str,
        sources: list[dict[str, Any]],
        flags: dict[str, Any],
        channel: str = "a2a",
        trace_id: str | None = None,
    ) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO interactions (
                    created_at, channel, session_id, task_id, route, query, answer,
                    sources_json, flags_json, trace_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    time.time(),
                    channel,
                    session_id,
                    task_id,
                    route,
                    query,
                    answer,
                    json.dumps(sources, ensure_ascii=False),
                    json.dumps(flags, ensure_ascii=False),
                    trace_id,
                ),
            )

    def recent(self, limit: int = 20, channel: str | None = None) -> list[dict[str, Any]]:
        limit = max(1, min(limit, 100))
        where = ""
        params: list[Any] = []
        if channel:
            where = "WHERE channel = ?"
            params.append(channel)
        params.append(limit)
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                f"""
                SELECT id, created_at, channel, session_id, task_id, route, query,
                       answer, sources_json, flags_json, trace_id
                FROM interactions
                {where}
                ORDER BY created_at DESC
                LIMIT ?
                """,
                params,
            ).fetchall()
        return [self._row_to_dict(row) for row in rows]

    def count(self, channel: str | None = None) -> int:
        where = ""
        params: list[Any] = []
        if channel:
            where = "WHERE channel = ?"
            params.append(channel)
        with self._connect() as conn:
            return int(conn.execute(f"SELECT COUNT(*) FROM interactions {where}", params).fetchone()[0])

    def _row_to_dict(self, row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "created_at": row["created_at"],
            "channel": row["channel"],
            "session_id": row["session_id"],
            "task_id": row["task_id"],
            "route": row["route"],
            "query": row["query"],
            "answer": row["answer"],
            "sources": json.loads(row["sources_json"] or "[]"),
            "flags": json.loads(row["flags_json"] or "{}"),
            "trace_id": row["trace_id"],
        }
