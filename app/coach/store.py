"""学习过程仓库：把"学情证据"落盘，供侧栏、教师视角与追问机制共同使用。

与 learning_store（记住学生问过什么）的分工：
- learning_store.store 关注**内容偏好**（学过哪些主题、来源命中）；
- 这里关注**过程证据**：每次交互帮到了第几级、哪个误概念反复出现、
  「再讲一遍」的比例、独立完成率。这些正是"撤去 AI 之后的独立评价"
  所需要的原始数据 —— 工具没撤，但"依赖度"可度量。

存储用 SQLite（与 .data/ 下既有库一致，无新依赖），单文件可随身携带，
符合"本地优先、弱网可用"的产品定位。
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


_SCHEMA = """
CREATE TABLE IF NOT EXISTS learning_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    created_at TEXT NOT NULL,
    route TEXT NOT NULL,
    ladder_level INTEGER NOT NULL,
    misconception_ids TEXT NOT NULL,
    stuck INTEGER NOT NULL,
    requested_full INTEGER NOT NULL,
    source TEXT NOT NULL DEFAULT 'chat'
);
CREATE INDEX IF NOT EXISTS idx_events_session ON learning_events(session_id, id);
CREATE TABLE IF NOT EXISTS ladder_state (
    session_id TEXT PRIMARY KEY,
    level INTEGER NOT NULL,
    turns_at_level INTEGER NOT NULL,
    updated_at TEXT NOT NULL
);
"""


@dataclass(frozen=True)
class LearningEvent:
    session_id: str
    route: str
    ladder_level: int
    misconception_ids: list[str] = field(default_factory=list)
    stuck: bool = False
    requested_full: bool = False
    source: str = "chat"
    created_at: str = ""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class ProcessStore:
    """学习过程证据仓库。所有读写失败都应被调用方当作旁路失败忽略。"""

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        if db_path.parent and not db_path.parent.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._conn() as conn:
            conn.executescript(_SCHEMA)

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=5)
        conn.row_factory = sqlite3.Row
        return conn

    # -------------------------------------------------------------- 事件

    def record(self, event: LearningEvent) -> None:
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO learning_events"
                "(session_id, created_at, route, ladder_level, misconception_ids, stuck,"
                " requested_full, source) VALUES (?,?,?,?,?,?,?,?)",
                (
                    event.session_id, event.created_at or _now(), event.route,
                    event.ladder_level, json.dumps(event.misconception_ids, ensure_ascii=False),
                    1 if event.stuck else 0, 1 if event.requested_full else 0, event.source,
                ),
            )

    def events(self, session_id: str, limit: int = 200) -> list[dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT * FROM learning_events WHERE session_id=? ORDER BY id DESC LIMIT ?",
                (session_id, limit),
            ).fetchall()
        out = []
        for r in rows:
            d = dict(r)
            d["misconception_ids"] = json.loads(d["misconception_ids"] or "[]")
            out.append(d)
        return out

    # -------------------------------------------------------------- 阶梯状态

    def load_ladder(self, session_id: str) -> tuple[int, int]:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT level, turns_at_level FROM ladder_state WHERE session_id=?",
                (session_id,),
            ).fetchone()
        if not row:
            return 0, 0
        return int(row["level"]), int(row["turns_at_level"])

    def save_ladder(self, session_id: str, level: int, turns_at_level: int) -> None:
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO ladder_state(session_id, level, turns_at_level, updated_at)"
                " VALUES (?,?,?,?)"
                " ON CONFLICT(session_id) DO UPDATE SET level=excluded.level,"
                " turns_at_level=excluded.turns_at_level, updated_at=excluded.updated_at",
                (session_id, level, turns_at_level, _now()),
            )

    # -------------------------------------------------------------- 学情画像

    def profile(self, session_id: str, limit: int = 200) -> dict[str, Any]:
        """从事件流算出一张可解释的学情画像。

        指标刻意选成"教师一看就懂"的形式：
        - 帮助依赖度：平均帮助等级 / 4。越接近 1，学生越依赖完整解答。
        - 独立推进率：未求助（没卡住、没索要答案）的轮次占比。
        - 反复误区：同一误概念被触发 ≥2 次，才算"需要干预"。
        """
        events = self.events(session_id, limit=limit)
        n = len(events)
        if n == 0:
            return {
                "sessions": 0, "turns": 0, "avg_level": 0.0, "dependency": 0.0,
                "independent_rate": 0.0, "recurring_misconceptions": [],
                "ladder_histogram": {str(i): 0 for i in range(5)},
            }
        avg_level = sum(e["ladder_level"] for e in events) / n
        independent = sum(
            1 for e in events if not e["stuck"] and not e["requested_full"]
        ) / n
        counts: dict[str, int] = {}
        for e in events:
            for mid in e["misconception_ids"]:
                counts[mid] = counts.get(mid, 0) + 1
        histogram = {str(i): 0 for i in range(5)}
        for e in events:
            key = str(e["ladder_level"])
            histogram[key] = histogram.get(key, 0) + 1
        return {
            "sessions": 1,
            "turns": n,
            "avg_level": round(avg_level, 2),
            "dependency": round(avg_level / 4.0, 2),
            "independent_rate": round(independent, 2),
            "recurring_misconceptions": [
                {"id": k, "count": v} for k, v in sorted(counts.items(), key=lambda kv: -kv[1])
                if v >= 2
            ],
            "ladder_histogram": histogram,
        }


__all__ = ["LearningEvent", "ProcessStore"]
