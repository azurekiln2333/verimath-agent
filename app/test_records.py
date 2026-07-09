from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any


class TestRecordStore:
    """离线评测记录存储。落 a2a.sqlite 的 eval_runs 表；首次启动懒迁移旧 JSONL。
    返回结构与旧 JSONL 版本一致：{created_at, kind, input_path, limit, report}。"""

    __test__ = False

    def __init__(self, data_dir: Path, db_path: Path | None = None) -> None:
        self.data_dir = data_dir
        self.path = data_dir / "eval_runs.jsonl"  # 保留旧文件用于迁移，不再写入
        self.db_path = db_path or (data_dir / "a2a.sqlite")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._init_db()
        self._migrate_jsonl_if_needed()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS eval_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at REAL NOT NULL,
                    kind TEXT NOT NULL DEFAULT 'offline_eval',
                    input_path TEXT NOT NULL,
                    limit_n INTEGER,
                    report_json TEXT NOT NULL
                )
                """
            )

    def _migrate_jsonl_if_needed(self) -> None:
        """表为空且旧 JSONL 存在时，一次性导入（按 created_at+input_path 幂等）。"""
        with self._connect() as conn:
            count = conn.execute("SELECT COUNT(*) FROM eval_runs").fetchone()[0]
            if count or not self.path.exists():
                return
            for line in self.path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                conn.execute(
                    "INSERT INTO eval_runs (created_at, kind, input_path, limit_n, report_json)"
                    " VALUES (?, ?, ?, ?, ?)",
                    (
                        rec.get("created_at", time.time()),
                        rec.get("kind", "offline_eval"),
                        rec.get("input_path", ""),
                        rec.get("limit"),
                        json.dumps(rec.get("report", {}), ensure_ascii=False),
                    ),
                )

    def append_eval_run(
        self,
        report: dict[str, Any],
        *,
        input_path: str,
        limit: int | None,
        kind: str = "offline_eval",
    ) -> dict[str, Any]:
        record = {
            "created_at": time.time(),
            "kind": kind,
            "input_path": input_path,
            "limit": limit,
            "report": report,
        }
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO eval_runs (created_at, kind, input_path, limit_n, report_json)"
                " VALUES (?, ?, ?, ?, ?)",
                (record["created_at"], record["kind"], input_path, limit,
                 json.dumps(report, ensure_ascii=False)),
            )
        return record

    def recent_eval_runs(
        self, limit: int = 20, kind: str | None = None
    ) -> list[dict[str, Any]]:
        limit = max(1, min(limit, 100))
        with self._connect() as conn:
            if kind is None:
                rows = conn.execute(
                    "SELECT created_at, kind, input_path, limit_n, report_json"
                    " FROM eval_runs ORDER BY id DESC LIMIT ?",
                    (limit,),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT created_at, kind, input_path, limit_n, report_json"
                    " FROM eval_runs WHERE kind = ? ORDER BY id DESC LIMIT ?",
                    (kind, limit),
                ).fetchall()
        return [
            {
                "created_at": row["created_at"],
                "kind": row["kind"],
                "input_path": row["input_path"],
                "limit": row["limit_n"],
                "report": json.loads(row["report_json"]),
            }
            for row in rows
        ]
