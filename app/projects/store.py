# -*- coding: utf-8 -*-
"""GateCraft 长任务最小状态机：ProjectStore + 阶段门。

W3 最小版：不接 HTTP 端点，供 agent 循环与未来 ADP 版本共享同一套
阶段定义与门判定。竞赛叙事的落点：单轮解答之外的「多阶段项目」证据。

阶段链（线代求解场景的最小闭环）：
  parse   → 题面解析（提取矩阵/算子）
  solve   → 内核求解（逐步 + 复算）
  verify  → 阶段门：verified=True 才放行
  writeup → 解答组织（报告/课件）

门规则（gate）：
  - verify 未通过（内核复算不一致）不得进 writeup
  - 每阶段最多 3 次重试（GateCraft 迭代上限），超限标记 blocked
"""
from __future__ import annotations

import sqlite3
import time
import uuid
from pathlib import Path
from typing import Any

STAGES = ("parse", "solve", "verify", "writeup")
MAX_ATTEMPTS = 3


class ProjectStore:
    """项目状态持久化（SQLite，独立于会话/聊天库）。"""

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
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
                CREATE TABLE IF NOT EXISTS projects (
                    project_id TEXT PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    title TEXT NOT NULL,
                    stage TEXT NOT NULL DEFAULT 'parse',
                    status TEXT NOT NULL DEFAULT 'in_progress',
                    attempts INTEGER NOT NULL DEFAULT 0,
                    verified INTEGER NOT NULL DEFAULT 0,
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL,
                    context_json TEXT NOT NULL DEFAULT '{}'
                )
                """
            )

    def create(self, session_id: str, title: str, context: dict[str, Any] | None = None) -> str:
        project_id = f"proj-{uuid.uuid4().hex[:12]}"
        now = time.time()
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO projects (project_id, session_id, title, created_at, updated_at, context_json)"
                " VALUES (?, ?, ?, ?, ?, ?)",
                (project_id, session_id, title, now, now,
                 sqlite3_json(context or {})),
            )
        return project_id

    def get(self, project_id: str) -> dict[str, Any] | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM projects WHERE project_id = ?", (project_id,)
            ).fetchone()
        return dict(row) if row else None

    def record_attempt(self, project_id: str) -> int:
        """当前阶段重试计数 +1，返回累计次数。超限置 blocked。"""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT attempts FROM projects WHERE project_id = ?", (project_id,)
            ).fetchone()
            if row is None:
                raise KeyError(project_id)
            attempts = row["attempts"] + 1
            status = "blocked" if attempts >= MAX_ATTEMPTS else "in_progress"
            conn.execute(
                "UPDATE projects SET attempts = ?, status = ?, updated_at = ? WHERE project_id = ?",
                (attempts, status, time.time(), project_id),
            )
        return attempts

    def set_verified(self, project_id: str, verified: bool) -> None:
        with self._connect() as conn:
            conn.execute(
                "UPDATE projects SET verified = ?, updated_at = ? WHERE project_id = ?",
                (1 if verified else 0, time.time(), project_id),
            )

    def advance(self, project_id: str) -> dict[str, Any]:
        """阶段门判定 + 推进。

        规则：
        - verify → writeup 必须 verified=1，否则拒绝并计一次重试
        - blocked 状态拒绝推进
        - 重试通过后 attempts 归零（进入新阶段重新计数）
        返回 {ok, stage, reason}。
        """
        with self._connect() as conn:
            row = conn.execute(
                "SELECT stage, status, verified, attempts FROM projects WHERE project_id = ?",
                (project_id,),
            ).fetchone()
        if row is None:
            raise KeyError(project_id)
        if row["status"] == "blocked":
            return {"ok": False, "stage": row["stage"], "reason": "attempts_exhausted"}
        idx = STAGES.index(row["stage"])
        if idx == len(STAGES) - 1:
            return {"ok": False, "stage": row["stage"], "reason": "already_final"}
        if row["stage"] == "verify" and not row["verified"]:
            attempts = self.record_attempt(project_id)
            return {"ok": False, "stage": "verify",
                    "reason": f"gate_failed_unverified (attempt {attempts}/{MAX_ATTEMPTS})"}
        next_stage = STAGES[idx + 1]
        with self._connect() as conn:
            conn.execute(
                "UPDATE projects SET stage = ?, attempts = 0, updated_at = ? WHERE project_id = ?",
                (next_stage, time.time(), project_id),
            )
        return {"ok": True, "stage": next_stage, "reason": "gate_passed"}


def sqlite3_json(obj: dict[str, Any]) -> str:
    import json
    return json.dumps(obj, ensure_ascii=False)
