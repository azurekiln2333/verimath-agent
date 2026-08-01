from __future__ import annotations

import hashlib
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from app.rag.loaders import RawDocument


DOMAIN_TERMS = (
    "中心极限定理",
    "大数定律",
    "随机变量",
    "概率分布",
    "期望",
    "方差",
    "协方差",
    "相关系数",
    "抽样分布",
    "置信区间",
    "假设检验",
    "p值",
    "显著性水平",
    "效应量",
    "t检验",
    "Welch",
    "独立样本",
    "配对样本",
    "非参数",
    "正态分布",
    "样本均值",
    "方差分析",
    "ANOVA",
    "卡方检验",
    "Fisher",
    "Bootstrap",
    "线性回归",
    "Logistic",
    "时间序列",
    "贝叶斯",
)

STOP_TERMS = {
    "什么",
    "怎么",
    "如何",
    "为何",
    "为什么",
    "请问",
    "帮我",
    "一个",
    "这个",
    "那个",
    "可以",
    "应该",
    "是不是",
    "是什么",
    "区别",
    "区分",
    "选择",
    "怎么选",
    "和",
    "与",
    "及",
    "或",
    "还是",
    "是",
    "的",
    "吗",
    "呢",
}

DOC_TYPE_WEIGHTS = {
    "self_note": 1.35,
    "lecture_note": 1.20,
    "public_reference": 1.10,
    "public_index_card": 0.90,
    "public_index_raw": 0.15,
    "public_reference_raw": 0.20,
    "exam_sheet": 0.25,
    "answer_key": 0.20,
}

CORPUS_CHUNK_COLUMNS = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "text": "TEXT NOT NULL",
    # 文本内容 SHA1 前 16 位，用于增量入库去重（见 add_chunks）。
    # 建索引后去重为 O(K log N) 定向查询，避免每次加载全表文本重算哈希。
    "text_hash": "TEXT NOT NULL DEFAULT ''",
    "doc_id": "TEXT NOT NULL DEFAULT ''",
    "title": "TEXT NOT NULL DEFAULT ''",
    "course": "TEXT NOT NULL DEFAULT 'unknown'",
    "chapter": "TEXT NOT NULL DEFAULT 'unknown'",
    "topic": "TEXT NOT NULL DEFAULT 'unknown'",
    "doc_type": "TEXT NOT NULL DEFAULT 'self_note'",
    "language": "TEXT NOT NULL DEFAULT 'unknown'",
    "provenance": "TEXT NOT NULL DEFAULT 'self'",
    "source": "TEXT NOT NULL DEFAULT ''",
    "origin_path": "TEXT NOT NULL DEFAULT ''",
    "source_url": "TEXT NOT NULL DEFAULT ''",
    "license_status": "TEXT NOT NULL DEFAULT 'unknown'",
    "ingest_policy": "TEXT NOT NULL DEFAULT 'main'",
    "quality_score": "REAL NOT NULL DEFAULT 0.0",
}


@dataclass(frozen=True)
class RetrievedChunk:
    chunk_id: int
    text: str
    score: float
    metadata: dict[str, str]
    excerpt: str = ""

    def as_dict(self) -> dict[str, object]:
        return {
            "chunk_id": self.chunk_id,
            "text": self.text,
            "score": self.score,
            "metadata": self.metadata,
            "excerpt": self.excerpt or self.text,
        }


class KeywordRetriever:
    """Small SQLite-backed retriever for the local POC.

    Chroma is intentionally not required at import time. The deployment can add
    a vector retriever later without changing the A2A route contract.
    """

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as conn:
            conn.execute(_create_table_sql())
            _ensure_schema(conn)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_corpus_course ON corpus_chunks(course)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_corpus_topic ON corpus_chunks(topic)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_corpus_doc_type ON corpus_chunks(doc_type)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_corpus_ingest_policy ON corpus_chunks(ingest_policy)")
            # text_hash 索引：支撑 add_chunks 的定向去重查询，以及存量回填的快速判空
            conn.execute("CREATE INDEX IF NOT EXISTS idx_corpus_text_hash ON corpus_chunks(text_hash)")
            # 一次性回填：老库升级到含 text_hash 列后，给空哈希行补算（索引让「无空行」时即时返回）
            _backfill_text_hashes(conn)

    def replace_chunks(self, chunks: Iterable[RawDocument]) -> int:
        self.init_db()
        rows = [
            (
                chunk.text,
                _text_hash(chunk.text),
                chunk.metadata.get("doc_id", ""),
                chunk.metadata.get("title", chunk.metadata.get("topic", "unknown")),
                chunk.metadata.get("course", "unknown"),
                chunk.metadata.get("chapter", "unknown"),
                chunk.metadata.get("topic", "unknown"),
                chunk.metadata.get("doc_type", "self_note"),
                chunk.metadata.get("language", "unknown"),
                chunk.metadata.get("provenance", "self"),
                chunk.metadata.get("source", chunk.source),
                chunk.metadata.get("origin_path", chunk.source),
                chunk.metadata.get("source_url", ""),
                chunk.metadata.get("license_status", "unknown"),
                chunk.metadata.get("ingest_policy", "main"),
                _coerce_float(chunk.metadata.get("quality_score"), default=0.0),
            )
            for chunk in chunks
            if chunk.text.strip()
        ]
        with self._connect() as conn:
            conn.execute("DELETE FROM corpus_chunks")
            conn.executemany(
                """
                INSERT INTO corpus_chunks (
                    text, text_hash, doc_id, title, course, chapter, topic, doc_type, language,
                    provenance, source, origin_path, source_url, license_status,
                    ingest_policy, quality_score
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                rows,
            )
        return len(rows)

    def add_chunks(self, chunks: Iterable[RawDocument]) -> int:
        """增量入库：直接 INSERT，不动现有数据（区别于 replace_chunks 的全量替换）。

        供「更新笔记」用：用户把自己的笔记分块后追加进库，后续检索优先命中
        doc_type=self_note（score_row 给 self_note 最高权重）。按文本哈希去重，
        避免同一段笔记重复提交导致检索结果扎堆。

        去重用 text_hash 列 + 索引定向查询：只对本批哈希做 IN 查询（O(K log N)），
        不再一次性加载全表文本重算哈希（旧实现的 O(N) 内存/性能风险）。
        """
        self.init_db()

        # 先按文本哈希对本批去重（同一次提交里的重复段落只留一份）
        candidates: list[tuple] = []   # (text, hash, ...metadata)
        seen_hashes: set[str] = set()
        for chunk in chunks:
            text = chunk.text.strip()
            if not text:
                continue
            h = _text_hash(text)
            if h in seen_hashes:
                continue
            seen_hashes.add(h)
            candidates.append(
                (
                    text,
                    h,
                    chunk.metadata.get("doc_id", ""),
                    chunk.metadata.get("title", chunk.metadata.get("topic", "unknown")),
                    chunk.metadata.get("course", "unknown"),
                    chunk.metadata.get("chapter", "unknown"),
                    chunk.metadata.get("topic", "unknown"),
                    chunk.metadata.get("doc_type", "self_note"),
                    chunk.metadata.get("language", "zh"),
                    chunk.metadata.get("provenance", "self"),
                    chunk.metadata.get("source", chunk.source),
                    chunk.metadata.get("origin_path", chunk.source),
                    chunk.metadata.get("source_url", ""),
                    chunk.metadata.get("license_status", "unknown"),
                    chunk.metadata.get("ingest_policy", "main"),
                    _coerce_float(chunk.metadata.get("quality_score"), default=0.0),
                )
            )
        if not candidates:
            return 0

        # 定向查询本批哈希里已存在于库的（索引命中，分批 IN 避免 SQL 变量数超限）
        with self._connect() as conn:
            existing_hashes = _existing_text_hashes(conn, seen_hashes)
        rows = [c for c in candidates if c[1] not in existing_hashes]
        if not rows:
            return 0

        with self._connect() as conn:
            conn.executemany(
                """
                INSERT INTO corpus_chunks (
                    text, text_hash, doc_id, title, course, chapter, topic, doc_type, language,
                    provenance, source, origin_path, source_url, license_status,
                    ingest_policy, quality_score
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                rows,
            )
        return len(rows)

    def search(self, query: str, limit: int = 4) -> list[RetrievedChunk]:
        self.init_db()
        terms = build_query_terms(query)
        if not terms:
            return []
        sql = """
            SELECT id, text, doc_id, title, course, chapter, topic, doc_type, language,
                   provenance, source, origin_path, source_url, license_status,
                   ingest_policy, quality_score
            FROM corpus_chunks
            WHERE text LIKE ? OR topic LIKE ? OR title LIKE ? OR course LIKE ? OR chapter LIKE ?
            LIMIT ?
        """
        candidate_limit = max(limit * 30, 50)
        rows: dict[int, sqlite3.Row] = {}
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            for term in terms:
                like = f"%{term}%"
                for row in conn.execute(sql, (like, like, like, like, like, candidate_limit)):
                    rows[row["id"]] = row
        scored_rows = [
            (score_row(row, terms), row)
            for row in rows.values()
            if score_row(row, terms) > 0
        ]
        scored_rows.sort(key=lambda item: (-item[0], item[1]["id"]))
        return [
            RetrievedChunk(
                chunk_id=row["id"],
                text=row["text"][:700],
                score=round(score, 4),
                metadata={
                    "doc_id": row["doc_id"],
                    "title": row["title"],
                    "course": row["course"],
                    "chapter": row["chapter"],
                    "topic": row["topic"],
                    "doc_type": row["doc_type"],
                    "language": row["language"],
                    "provenance": row["provenance"],
                    "source": row["source"],
                    "origin_path": row["origin_path"],
                    "source_url": row["source_url"],
                    "license_status": row["license_status"],
                    "ingest_policy": row["ingest_policy"],
                    "quality_score": _format_score(row["quality_score"]),
                    "source_category": source_category_label(
                        provenance=row["provenance"],
                        doc_type=row["doc_type"],
                        ingest_policy=row["ingest_policy"],
                    ),
                },
                excerpt=build_excerpt(row["text"], terms),
            )
            for score, row in scored_rows[:limit]
        ]

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def stats(self) -> dict[str, object]:
        self.init_db()
        with self._connect() as conn:
            total = conn.execute("SELECT COUNT(*) FROM corpus_chunks").fetchone()[0]
            courses = [
                {"course": row[0], "chunks": row[1]}
                for row in conn.execute(
                    """
                    SELECT course, COUNT(*)
                    FROM corpus_chunks
                    GROUP BY course
                    ORDER BY COUNT(*) DESC, course
                    LIMIT 12
                    """
                )
            ]
            doc_types = [
                {"doc_type": row[0], "chunks": row[1]}
                for row in conn.execute(
                    """
                    SELECT doc_type, COUNT(*)
                    FROM corpus_chunks
                    GROUP BY doc_type
                    ORDER BY COUNT(*) DESC, doc_type
                    LIMIT 12
                    """
                )
            ]
            policies = [
                {"ingest_policy": row[0], "chunks": row[1]}
                for row in conn.execute(
                    """
                    SELECT ingest_policy, COUNT(*)
                    FROM corpus_chunks
                    GROUP BY ingest_policy
                    ORDER BY COUNT(*) DESC, ingest_policy
                    LIMIT 12
                    """
                )
            ]
        return {"chunks": total, "courses": courses, "doc_types": doc_types, "policies": policies}


def build_query_terms(query: str) -> list[str]:
    normalized = normalize_text(query)
    terms: set[str] = set()
    lowered_query = normalized.lower()
    for term in DOMAIN_TERMS:
        if term.lower() in lowered_query:
            terms.add(term)

    for token in re.findall(r"[A-Za-z][A-Za-z0-9_+\-]*|[0-9]+(?:\.[0-9]+)?", normalized):
        if len(token) >= 2:
            terms.add(token)

    for block in re.findall(r"[\u4e00-\u9fff]+", normalized):
        for piece in split_chinese_block(block):
            terms.add(piece)

    return sorted(
        (term for term in terms if len(term) >= 2 and term not in STOP_TERMS),
        key=lambda value: (-len(value), value),
    )


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[，。！？、；：,.!?;:()\[\]{}<>《》“”\"']", " ", text)).strip()


_SENT_SPLIT_RE = re.compile(r"(?<=[。！？；.!?;])")


def build_excerpt(text: str, terms: list[str], max_chars: int = 240) -> str:
    """按句子边界截取命中词周围的整句，做干净展示摘录（离线确定性回退）。"""
    text = (text or "").strip()
    if not text:
        return ""
    sentences = [s.strip() for s in _SENT_SPLIT_RE.split(text) if s.strip()]
    if not sentences:
        return text[:max_chars]
    lowered = [s.lower() for s in sentences]
    hit = next(
        (i for i, s in enumerate(lowered) if any(t.lower() in s for t in terms)),
        0,
    )
    # 以命中句为中心，向两侧扩到 max_chars
    picked = [sentences[hit]]
    total = len(sentences[hit])
    left, right = hit - 1, hit + 1
    while total < max_chars and (left >= 0 or right < len(sentences)):
        if right < len(sentences) and total + len(sentences[right]) <= max_chars:
            picked.append(sentences[right])
            total += len(sentences[right])
            right += 1
        elif left >= 0 and total + len(sentences[left]) <= max_chars:
            picked.insert(0, sentences[left])
            total += len(sentences[left])
            left -= 1
        else:
            break
    excerpt = "".join(picked)
    return excerpt if len(excerpt) <= max_chars else excerpt[:max_chars]


def split_chinese_block(block: str) -> set[str]:
    pieces: set[str] = set()
    queue = [block]
    for stop_word in STOP_TERMS:
        next_queue: list[str] = []
        for item in queue:
            next_queue.extend(part for part in item.split(stop_word) if part)
        queue = next_queue
    for item in queue:
        if len(item) >= 2:
            pieces.add(item)
        if len(item) > 8:
            for size in (6, 5, 4, 3):
                for start in range(0, len(item) - size + 1):
                    piece = item[start : start + size]
                    if piece not in STOP_TERMS:
                        pieces.add(piece)
    return pieces


def score_row(row: sqlite3.Row, terms: list[str]) -> float:
    fields = (
        (row["topic"], 3.4),
        (row["title"], 3.0),
        (row["course"], 2.0),
        (row["chapter"], 1.8),
        (row["text"], 1.0),
    )
    lexical_score = 0.0
    topic_match_score = 0.0
    for term in terms:
        term_lower = term.lower()
        length_boost = 1.0 + min(len(term), 10) / 10
        for index, (value, weight) in enumerate(fields):
            if term_lower in str(value).lower():
                lexical_score += weight * length_boost
                if index <= 1:
                    topic_match_score += 0.8 * length_boost
    quality_score = _coerce_float(row["quality_score"], default=0.0) * 3.0
    doc_type_weight = DOC_TYPE_WEIGHTS.get(str(row["doc_type"]), 0.4)
    excerpt_quality = _excerpt_quality(str(row["text"]), terms)
    hold_penalty = -2.0 if str(row["ingest_policy"]) == "hold" else 0.0
    return lexical_score + topic_match_score + quality_score + doc_type_weight + excerpt_quality + hold_penalty


def source_category_label(provenance: str, doc_type: str, ingest_policy: str) -> str:
    if ingest_policy == "exam":
        return "题卷副库"
    if provenance == "self":
        return "自有笔记"
    if doc_type == "public_index_card":
        return "公开卡片"
    if doc_type in {"public_reference", "public_reference_raw"}:
        return "公开原文"
    return "公开资料" if provenance == "public" else "本地资料"


def _excerpt_quality(text: str, terms: list[str]) -> float:
    excerpt = build_excerpt(text, terms)
    if not excerpt:
        return 0.0
    lowered = excerpt.lower()
    hits = sum(1 for term in terms if term.lower() in lowered)
    density = hits / max(len(excerpt), 1)
    return min(1.2, hits * 0.2 + density * 40)


def _coerce_float(value: object, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _format_score(value: object) -> str:
    return f"{_coerce_float(value, default=0.0):.2f}"


def _create_table_sql() -> str:
    columns = ",\n                    ".join(
        f"{name} {definition}" for name, definition in CORPUS_CHUNK_COLUMNS.items()
    )
    return f"""
                CREATE TABLE IF NOT EXISTS corpus_chunks (
                    {columns}
                )
                """


def _ensure_schema(conn: sqlite3.Connection) -> None:
    existing = {
        row[1]
        for row in conn.execute("PRAGMA table_info(corpus_chunks)")
    }
    for name, definition in CORPUS_CHUNK_COLUMNS.items():
        if name == "id" or name in existing:
            continue
        conn.execute(f"ALTER TABLE corpus_chunks ADD COLUMN {name} {definition}")


def _text_hash(text: str) -> str:
    """文本内容 SHA1 前 16 位，用于增量入库去重。"""
    return hashlib.sha1((text or "").encode("utf-8")).hexdigest()[:16]


def _existing_text_hashes(conn: sqlite3.Connection, hashes: Iterable[str]) -> set[str]:
    """返回 hashes 中已存在于 corpus_chunks 的子集。

    用 text_hash 索引做定向 IN 查询（O(K log N)，K=本批哈希数），替代旧实现
    一次性加载全表文本重算哈希。分批避免 SQL 变量数超限（SQLite 默认上限 999，
    新版本 32766；按 500 分批保守取值）。
    """
    batch = [h for h in hashes if h]
    if not batch:
        return set()
    found: set[str] = set()
    chunk_size = 500
    for i in range(0, len(batch), chunk_size):
        part = batch[i:i + chunk_size]
        placeholders = ",".join("?" * len(part))
        for row in conn.execute(
            f"SELECT text_hash FROM corpus_chunks WHERE text_hash IN ({placeholders})",
            tuple(part),
        ):
            found.add(row[0])
    return found


def _backfill_text_hashes(conn: sqlite3.Connection) -> None:
    """老库升级迁移：给 text_hash 为空的存量行补算哈希。

    索引让「无空行」时的 LIMIT 查询即时返回，迁移完成后本函数近似 no-op。
    LIMIT 1000 + 增量 UPDATE：超大库分多次 init_db 调用逐步迁移完。
    """
    rows = conn.execute(
        "SELECT id, text FROM corpus_chunks WHERE text_hash = '' LIMIT 1000"
    ).fetchall()
    if not rows:
        return
    for cid, text in rows:
        conn.execute(
            "UPDATE corpus_chunks SET text_hash = ? WHERE id = ?",
            (_text_hash(text or ""), cid),
        )
