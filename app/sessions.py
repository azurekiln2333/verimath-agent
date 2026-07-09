from __future__ import annotations

import json
import sqlite3
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class SessionState:
    session_id: str
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    history: list[dict[str, Any]] = field(default_factory=list)
    cancelled_tasks: set[str] = field(default_factory=set)
    answer_style: str = "rigorous"
    use_model: bool = True

    def touch(self) -> None:
        self.updated_at = time.time()


class SessionStore:
    """会话存储：内存 dict 作一级缓存，SQLite 写穿透 + 懒加载，重启不丢多轮上下文。
    方法签名与旧内存版本保持一致，调用方与测试无感。cancelled_tasks 纯运行期不持久化。"""

    def __init__(self, max_history_turns: int = 8, db_path: Path | None = None) -> None:
        self.max_history_turns = max_history_turns
        self.db_path = db_path
        self._sessions: dict[str, SessionState] = {}
        if self.db_path is not None:
            self._init_db()

    # ---- SQLite 底层 ----
    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id TEXT PRIMARY KEY,
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL,
                    answer_style TEXT NOT NULL DEFAULT 'rigorous',
                    use_model INTEGER NOT NULL DEFAULT 1
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS session_turns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    seq INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    ts REAL NOT NULL
                )
                """
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_session_turns_sid ON session_turns(session_id, seq)"
            )

    def _persist_session_row(self, state: SessionState) -> None:
        if self.db_path is None:
            return
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO sessions (session_id, created_at, updated_at, answer_style, use_model)"
                " VALUES (?, ?, ?, ?, ?)"
                " ON CONFLICT(session_id) DO UPDATE SET updated_at=excluded.updated_at,"
                " answer_style=excluded.answer_style, use_model=excluded.use_model",
                (state.session_id, state.created_at, state.updated_at,
                 state.answer_style, 1 if state.use_model else 0),
            )

    def _load_from_db(self, session_id: str) -> SessionState | None:
        if self.db_path is None:
            return None
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM sessions WHERE session_id = ?", (session_id,)
            ).fetchone()
            if row is None:
                return None
            turns = conn.execute(
                "SELECT role, content, ts FROM session_turns WHERE session_id = ?"
                " ORDER BY seq ASC", (session_id,),
            ).fetchall()
        state = SessionState(
            session_id=session_id,
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            answer_style=row["answer_style"],
            use_model=bool(row["use_model"]),
        )
        history = [{"role": t["role"], "content": t["content"], "ts": t["ts"]} for t in turns]
        state.history = history[-self.max_history_turns * 2 :]
        return state

    # ---- 对外 API（签名与内存版一致）----
    def create(self) -> SessionState:
        session_id = f"local-{uuid.uuid4().hex}"
        state = SessionState(session_id=session_id)
        self._sessions[session_id] = state
        self._persist_session_row(state)
        return state

    def get_or_create(self, session_id: str | None) -> SessionState:
        if session_id and session_id in self._sessions:
            state = self._sessions[session_id]
            state.touch()
            return state
        if session_id:
            state = self._load_from_db(session_id)
            if state is None:
                state = SessionState(session_id=session_id)
                self._persist_session_row(state)
            self._sessions[session_id] = state
            state.touch()
            return state
        return self.create()

    def append_turn(self, session_id: str, role: str, content: str) -> None:
        state = self.get_or_create(session_id)
        ts = time.time()
        state.history.append({"role": role, "content": content, "ts": ts})
        if len(state.history) > self.max_history_turns * 2:
            state.history = state.history[-self.max_history_turns * 2 :]
        state.touch()
        if self.db_path is not None:
            with self._connect() as conn:
                seq = conn.execute(
                    "SELECT COALESCE(MAX(seq), -1) + 1 FROM session_turns WHERE session_id = ?",
                    (session_id,),
                ).fetchone()[0]
                conn.execute(
                    "INSERT INTO session_turns (session_id, seq, role, content, ts)"
                    " VALUES (?, ?, ?, ?, ?)",
                    (session_id, seq, role, content, ts),
                )
            self._persist_session_row(state)

    def set_preferences(self, session_id: str, *, answer_style: str | None = None,
                        use_model: bool | None = None) -> SessionState:
        state = self.get_or_create(session_id)
        if answer_style is not None:
            state.answer_style = answer_style
        if use_model is not None:
            state.use_model = use_model
        state.touch()
        self._persist_session_row(state)
        return state

    def cancel(self, session_id: str, task_id: str) -> None:
        state = self.get_or_create(session_id)
        state.cancelled_tasks.add(task_id)
        state.touch()

    def is_cancelled(self, session_id: str, task_id: str) -> bool:
        state = self.get_or_create(session_id)
        return task_id in state.cancelled_tasks

    def clear_context(self, session_id: str) -> None:
        state = self.get_or_create(session_id)
        state.history.clear()
        state.cancelled_tasks.clear()
        state.touch()
        if self.db_path is not None:
            with self._connect() as conn:
                conn.execute("DELETE FROM session_turns WHERE session_id = ?", (session_id,))
            self._persist_session_row(state)
