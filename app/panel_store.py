"""Durable display history and visualization jobs, separate from model context windows."""
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
import uuid
from contextlib import contextmanager
from collections.abc import Iterator
from pathlib import Path
from typing import Any


ACTIVE = {"queued", "running"}


class PanelStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS panel_messages (
                    seq INTEGER PRIMARY KEY AUTOINCREMENT,
                    message_id TEXT NOT NULL UNIQUE,
                    session_id TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL DEFAULT '',
                    status TEXT NOT NULL DEFAULT 'completed',
                    metadata_json TEXT NOT NULL DEFAULT '{}',
                    visualization_state TEXT NOT NULL DEFAULT 'none',
                    created_at REAL NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_panel_messages_session
                    ON panel_messages(session_id, seq);
                CREATE TABLE IF NOT EXISTS panel_offers (
                    offer_id TEXT PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    message_id TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_panel_offers_message
                    ON panel_offers(session_id, message_id);
                CREATE TABLE IF NOT EXISTS panel_artifact_jobs (
                    job_id TEXT PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    message_id TEXT NOT NULL,
                    offer_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    retry_of TEXT UNIQUE,
                    result_json TEXT,
                    error TEXT,
                    created_at REAL NOT NULL,
                    updated_at REAL NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_panel_jobs_session
                    ON panel_artifact_jobs(session_id, created_at);
            """)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def import_legacy(self) -> None:
        """Idempotently copy old display history; never truncate the original tables."""
        with self.connect() as db:
            if not db.execute("SELECT 1 FROM sqlite_master WHERE name='interactions'").fetchone():
                return
            rows = db.execute("SELECT * FROM interactions i WHERE channel='panel' AND NOT EXISTS "
                              "(SELECT 1 FROM panel_messages m WHERE m.message_id=i.task_id || ':assistant') "
                              "ORDER BY created_at,id").fetchall()
            for row in rows:
                metadata = {"route": row["route"], "sources": json.loads(row["sources_json"]),
                            "flags": json.loads(row["flags_json"])}
                for role, text in (("user", row["query"]), ("assistant", row["answer"])):
                    db.execute(
                        "INSERT OR IGNORE INTO panel_messages "
                        "(message_id,session_id,task_id,role,content,metadata_json,created_at) VALUES (?,?,?,?,?,?,?)",
                        (f"{row['task_id']}:{role}", row["session_id"], row["task_id"], role,
                         text, json.dumps(metadata, ensure_ascii=False), row["created_at"]),
                    )

    def begin_turn(self, session_id: str, task_id: str, query: str, metadata: dict) -> str:
        with self.connect() as db:
            for role, text, status in (("user", query, "completed"), ("assistant", "", "streaming")):
                db.execute(
                    "INSERT OR IGNORE INTO panel_messages "
                    "(message_id,session_id,task_id,role,content,status,metadata_json,created_at) VALUES (?,?,?,?,?,?,?,?)",
                    (f"{task_id}:{role}", session_id, task_id, role, text, status,
                     json.dumps(metadata, ensure_ascii=False), time.time()),
                )
        return f"{task_id}:assistant"

    def finish_turn(self, message_id: str, content: str, status: str, metadata: dict,
                    visualization_state: str = "none") -> None:
        with self.connect() as db:
            db.execute(
                "UPDATE panel_messages SET content=?,status=?,metadata_json=?,visualization_state=? WHERE message_id=?",
                (content, status, json.dumps(metadata, ensure_ascii=False), visualization_state, message_id),
            )

    def message(self, session_id: str, message_id: str) -> dict | None:
        with self.connect() as db:
            row = db.execute("SELECT * FROM panel_messages WHERE session_id=? AND message_id=?",
                             (session_id, message_id)).fetchone()
        return self._message(row) if row else None

    def turn_query(self, session_id: str, message_id: str) -> str:
        """Resolve the original question by task ownership, including legacy message IDs."""
        with self.connect() as db:
            row = db.execute("SELECT u.content FROM panel_messages u JOIN panel_messages a "
                             "ON u.session_id=a.session_id AND u.task_id=a.task_id "
                             "WHERE a.session_id=? AND a.message_id=? AND u.role='user' LIMIT 1",
                             (session_id, message_id)).fetchone()
        return row[0] if row else ""

    def recommendation_context(self, session_id: str, message_id: str) -> dict:
        """Read the opening question and earlier dialogue, without loading Canvas payloads."""
        with self.connect() as db:
            message = db.execute("SELECT seq FROM panel_messages WHERE session_id=? AND message_id=?",
                                 (session_id, message_id)).fetchone()
            if not message:
                return {"opening_question": "", "recent": []}
            opening = db.execute("SELECT content FROM panel_messages WHERE session_id=? AND seq<? "
                                 "AND role='user' ORDER BY seq LIMIT 1", (session_id, message["seq"])).fetchone()
            rows = db.execute("SELECT role,content FROM panel_messages WHERE session_id=? AND seq<? "
                              "ORDER BY seq DESC LIMIT 8", (session_id, message["seq"])).fetchall()
        return {"opening_question": opening[0] if opening else "",
                "recent": [dict(row) for row in reversed(rows)]}

    @staticmethod
    def _message(row: sqlite3.Row) -> dict:
        item = dict(row)
        item.update(json.loads(item.pop("metadata_json")))
        return item

    def messages(self, session_id: str, before: int | None = None, limit: int = 100) -> list[dict]:
        with self.connect() as db:
            rows = db.execute(
                "SELECT * FROM panel_messages WHERE session_id=? AND seq<? ORDER BY seq DESC LIMIT ?",
                (session_id, before or 2**63-1, max(1, min(limit, 200))),
            ).fetchall()
        items = [self._message(row) for row in reversed(rows)]
        offers = self.offers(session_id)
        jobs = self.jobs(session_id)
        for item in items:
            item["visualization_offers"] = [o for o in offers if o["message_id"] == item["message_id"]]
            item["artifact_jobs"] = [j for j in jobs if j["message_id"] == item["message_id"]]
        return items

    def sessions(self, limit: int = 100) -> list[dict]:
        with self.connect() as db:
            rows = db.execute("""
                SELECT m.session_id, MIN(m.created_at) AS created_at, MAX(m.created_at) AS updated_at,
                       COUNT(*) AS message_count,
                       (SELECT content FROM panel_messages f WHERE f.session_id=m.session_id AND f.role='user'
                        ORDER BY f.seq LIMIT 1) AS title
                FROM panel_messages m GROUP BY m.session_id ORDER BY updated_at DESC LIMIT ?
            """, (max(1, min(limit, 200)),)).fetchall()
        return [dict(row) for row in rows]

    def set_visualization_state(self, message_id: str, state: str) -> None:
        with self.connect() as db:
            db.execute("UPDATE panel_messages SET visualization_state=? WHERE message_id=?", (state, message_id))

    def patch_metadata(self, session_id: str, message_id: str, values: dict) -> None:
        """Merge asynchronous recommendations without replacing answer metadata."""
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT metadata_json FROM panel_messages WHERE session_id=? AND message_id=?",
                             (session_id, message_id)).fetchone()
            if row:
                metadata = {**json.loads(row[0]), **values}
                db.execute("UPDATE panel_messages SET metadata_json=? WHERE session_id=? AND message_id=?",
                           (json.dumps(metadata, ensure_ascii=False), session_id, message_id))

    def add_offer(self, session_id: str, message_id: str, payload: dict) -> dict:
        key = f"{message_id}:{payload.get('title', '')}:{payload.get('tier', '')}"
        offer_id = hashlib.sha256(key.encode()).hexdigest()[:24]
        offer = {**payload, "offer_id": offer_id, "session_id": session_id, "message_id": message_id}
        with self.connect() as db:
            db.execute("INSERT OR IGNORE INTO panel_offers VALUES (?,?,?,?)",
                       (offer_id, session_id, message_id, json.dumps(offer, ensure_ascii=False)))
            db.execute("UPDATE panel_messages SET visualization_state='ready' WHERE message_id=?", (message_id,))
        return self.public_offer(offer)

    @staticmethod
    def public_offer(offer: dict) -> dict:
        return {key: offer[key] for key in ("offer_id", "session_id", "message_id", "title", "caption", "tier") if key in offer}

    def offer(self, session_id: str, message_id: str, offer_id: str) -> dict | None:
        with self.connect() as db:
            row = db.execute("SELECT payload_json FROM panel_offers WHERE session_id=? AND message_id=? AND offer_id=?",
                             (session_id, message_id, offer_id)).fetchone()
        return json.loads(row[0]) if row else None

    def offers(self, session_id: str) -> list[dict]:
        with self.connect() as db:
            rows = db.execute("SELECT payload_json FROM panel_offers WHERE session_id=?", (session_id,)).fetchall()
        return [self.public_offer(json.loads(row[0])) for row in rows]

    def create_job(self, session_id: str, message_id: str, offer_id: str, retry_of: str | None = None) -> dict:
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if not db.execute("SELECT 1 FROM panel_offers WHERE session_id=? AND message_id=? AND offer_id=?",
                              (session_id, message_id, offer_id)).fetchone():
                raise ValueError("未找到该回答的可视化候选")
            rows = db.execute("SELECT * FROM panel_artifact_jobs WHERE session_id=? AND message_id=? AND offer_id=? "
                              "ORDER BY created_at DESC", (session_id, message_id, offer_id)).fetchall()
            if rows:
                latest = dict(rows[0])
                if not retry_of or latest["status"] in ACTIVE or latest.get("retry_of") == retry_of:
                    return self._job(latest)
                if latest["job_id"] != retry_of:
                    raise ValueError("重试目标已更新，请刷新任务状态")
            elif retry_of:
                raise ValueError("未找到要重试的任务")
            job_id = uuid.uuid4().hex
            now = time.time()
            db.execute("INSERT INTO panel_artifact_jobs "
                       "(job_id,session_id,message_id,offer_id,status,retry_of,created_at,updated_at) "
                       "VALUES (?,?,?,?,'queued',?,?,?)", (job_id, session_id, message_id, offer_id, retry_of, now, now))
            row = db.execute("SELECT * FROM panel_artifact_jobs WHERE job_id=?", (job_id,)).fetchone()
        return self._job(row)

    @staticmethod
    def _job(row: Any) -> dict:
        item = dict(row)
        result = item.pop("result_json", None)
        item["artifact"] = json.loads(result) if result else None
        return item

    def jobs(self, session_id: str) -> list[dict]:
        with self.connect() as db:
            rows = db.execute("SELECT * FROM panel_artifact_jobs WHERE session_id=? ORDER BY created_at", (session_id,)).fetchall()
        return [self._job(row) for row in rows]

    def job(self, job_id: str, session_id: str | None = None) -> dict | None:
        with self.connect() as db:
            row = db.execute("SELECT * FROM panel_artifact_jobs WHERE job_id=?", (job_id,)).fetchone()
        return self._job(row) if row and (session_id is None or row["session_id"] == session_id) else None

    def claim_job(self) -> dict | None:
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT * FROM panel_artifact_jobs WHERE status='queued' ORDER BY created_at LIMIT 1").fetchone()
            if not row:
                return None
            db.execute("UPDATE panel_artifact_jobs SET status='running',updated_at=? WHERE job_id=?", (time.time(), row["job_id"]))
        return {**self._job(row), "status": "running"}

    def finish_job(self, job_id: str, status: str, artifact: dict | None = None, error: str | None = None) -> None:
        with self.connect() as db:
            db.execute("UPDATE panel_artifact_jobs SET status=?,result_json=?,error=?,updated_at=? "
                       "WHERE job_id=? AND status IN ('queued','running')",
                       (status, json.dumps(artifact, ensure_ascii=False) if artifact else None, error, time.time(), job_id))

    def recover(self) -> None:
        with self.connect() as db:
            db.execute("UPDATE panel_artifact_jobs SET status='interrupted',error='服务已重启，请重试',updated_at=? "
                       "WHERE status IN ('queued','running')", (time.time(),))
            db.execute("UPDATE panel_messages SET status='interrupted' WHERE status='streaming'")
            db.execute("UPDATE panel_messages SET visualization_state='none' WHERE visualization_state='checking'")
            rows = db.execute("SELECT message_id,metadata_json FROM panel_messages WHERE role='assistant'").fetchall()
            for row in rows:
                metadata = json.loads(row["metadata_json"])
                if metadata.get("followups_state") == "checking":
                    metadata["followups_state"] = "interrupted"
                    db.execute("UPDATE panel_messages SET metadata_json=? WHERE message_id=?",
                               (json.dumps(metadata, ensure_ascii=False), row["message_id"]))

    def artifact_state(self, session_id: str) -> dict:
        with self.connect() as db:
            pending = db.execute("SELECT message_id FROM panel_messages WHERE session_id=? AND visualization_state='checking'",
                                 (session_id,)).fetchall()
            rows = db.execute("SELECT message_id,metadata_json FROM panel_messages WHERE session_id=? AND role='assistant'",
                              (session_id,)).fetchall()
        suggestions = [{"message_id": row["message_id"], "session_id": session_id,
                        "followups": meta.get("followups", []), "followups_state": meta["followups_state"],
                        "followups_stage": meta.get("followups_stage", ""),
                        "followups_error": meta.get("followups_error", "")}
                       for row in rows if (meta := json.loads(row["metadata_json"])).get("followups_state")]
        suggestions_checking = [item["message_id"] for item in suggestions if item["followups_state"] == "checking"]
        jobs = self.jobs(session_id)
        return {"offers": self.offers(session_id), "jobs": jobs,
                "checking": [row[0] for row in pending],
                "suggestions": suggestions, "suggestions_checking": suggestions_checking,
                "pending": bool(pending or suggestions_checking) or any(j["status"] in ACTIVE for j in jobs)}
