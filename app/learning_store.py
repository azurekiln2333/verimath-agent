from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any


class LearningStore:
    """最小学习记录 substrate：每 session 一行画像，聚合"学了什么"。
    不含推荐逻辑，仅供未来"下一步推荐"读取。落 a2a.sqlite。"""

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS learning_profiles (
                    session_id TEXT PRIMARY KEY,
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL,
                    turn_count INTEGER NOT NULL DEFAULT 0,
                    last_route TEXT,
                    last_active REAL,
                    route_counts_json TEXT NOT NULL DEFAULT '{}',
                    topics_json TEXT NOT NULL DEFAULT '[]',
                    major TEXT,
                    level TEXT
                )
                """
            )

    def record_turn(self, session_id: str, route: str, sources: list[dict[str, Any]] | None = None) -> None:
        """每轮问答后 UPSERT：turn_count+1、route 计数+1、并入命中 topic。"""
        if not session_id:
            return
        now = time.time()
        topics_new = _extract_topics(sources or [])
        with self._connect() as conn:
            row = conn.execute(
                "SELECT turn_count, route_counts_json, topics_json FROM learning_profiles"
                " WHERE session_id = ?",
                (session_id,),
            ).fetchone()
            if row is None:
                route_counts = {route: 1} if route else {}
                topics = _merge_topics([], topics_new)
                conn.execute(
                    "INSERT INTO learning_profiles (session_id, created_at, updated_at,"
                    " turn_count, last_route, last_active, route_counts_json, topics_json)"
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (session_id, now, now, 1, route, now,
                     json.dumps(route_counts, ensure_ascii=False),
                     json.dumps(topics, ensure_ascii=False)),
                )
            else:
                route_counts = json.loads(row["route_counts_json"])
                if route:
                    route_counts[route] = route_counts.get(route, 0) + 1
                topics = _merge_topics(json.loads(row["topics_json"]), topics_new)
                conn.execute(
                    "UPDATE learning_profiles SET updated_at = ?, turn_count = ?,"
                    " last_route = ?, last_active = ?, route_counts_json = ?, topics_json = ?"
                    " WHERE session_id = ?",
                    (now, row["turn_count"] + 1, route, now,
                     json.dumps(route_counts, ensure_ascii=False),
                     json.dumps(topics, ensure_ascii=False), session_id),
                )

    def get_profile(self, session_id: str) -> dict[str, Any] | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM learning_profiles WHERE session_id = ?", (session_id,)
            ).fetchone()
        if row is None:
            return None
        return {
            "session_id": row["session_id"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
            "turn_count": row["turn_count"],
            "last_route": row["last_route"],
            "last_active": row["last_active"],
            "route_counts": json.loads(row["route_counts_json"]),
            "topics": json.loads(row["topics_json"]),
            "major": row["major"],
            "level": row["level"],
        }

    def count(self) -> int:
        with self._connect() as conn:
            return conn.execute("SELECT COUNT(*) FROM learning_profiles").fetchone()[0]


def _extract_topics(sources: list[dict[str, Any]]) -> list[str]:
    topics: list[str] = []
    for src in sources:
        meta = src.get("metadata", {}) if isinstance(src, dict) else {}
        topic = meta.get("topic")
        if topic and topic not in topics:
            topics.append(topic)
    return topics


def _merge_topics(existing: list[str], new: list[str], cap: int = 50) -> list[str]:
    """最近学过的 topic 去重合并，新在前，上限 cap。"""
    merged = list(new)
    for t in existing:
        if t not in merged:
            merged.append(t)
    return merged[:cap]
