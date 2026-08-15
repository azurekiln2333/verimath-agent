# -*- coding: utf-8 -*-
"""生成高代笔记来源评测集：从 腾讯云/知识库语料/高等代数 笔记提取查询，
写入 eval/seeds_gaodai.jsonl（golden.jsonl 同格式），并把笔记增量入库（幂等）。

设计（GRILLING_REPORT Q6：笔记只作评测集来源，不作微调）：
- 查询来自真实笔记主题（章节标题 + frontmatter tags），不是随机生成；
- must_retrieve=true 的查询必须能命中已入库的对应笔记（生成时自检）；
- expected_route 由「教学内容意图」标注（计算类→solution，概念类→concept），
  生成时用真实路由核对，不一致会打印告警（路由词表需与 manifest 同步）。

运行：.venv/Scripts/python.exe scripts/gen_gaodai_seeds.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from app.rag.loaders import RawDocument, chunk_document
from app.rag.store import KeywordRetriever
from app.settings import settings

NOTES_ROOT = Path(__file__).resolve().parents[1].parent / "腾讯云" / "知识库语料" / "高等代数"
EVAL_DIR = Path(__file__).resolve().parents[1] / "eval"
OUT = EVAL_DIR / "seeds_gaodai.jsonl"

# 计算类主题 → solution（含查询模板）；其余概念类 → concept
COMPUTE_TOPICS = {
    "逆矩阵": "逆矩阵怎么求？",
    "基础解系": "基础解系怎么求？",
    "行列式": "行列式怎么计算？",
    "线性方程组": "线性方程组怎么解？",
    "特征值": "特征值和特征向量怎么求？",
    "特征向量": "特征值和特征向量怎么求？",
    "可对角化": "怎么判断矩阵能不能对角化？",
    "二次型": "二次型怎么化标准形？",
    "正定": "正定矩阵怎么判断？",
    "施密特": "施密特正交化怎么做？",
    "正交基": "正交基怎么求？",
    "基变换": "基变换的过渡矩阵怎么求？",
    "线性相关": "怎么判断向量组的线性相关性？",
    # 泛化键（放最后，且命中时需通过 _matrix_guard）
    "矩阵": "矩阵的逆矩阵怎么求？",
}

# 计算词表：标签驱动的第二条查询若命中这些词则跳过（避免与主题查询重复/打架）
COMPUTE_VOCAB = set(COMPUTE_TOPICS) | {
    "过渡矩阵", "特征多项式", "秩", "零空间", "列空间", "特征子空间",
    "Jordan", "若尔当", "若当", "标准形", "惯性指数", "符号差", "配方法",
}

# 泛化标签：不产生查询
GENERIC_TAGS = {"高等代数", "线性代数", "代数", "数学"}


_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_TAG_RE = re.compile(r"^\s*-\s*(.+)$", re.MULTILINE)


def parse_note(path: Path) -> tuple[str, list[str], str]:
    """返回 (标题主题, tags, 正文)。frontmatter 剥离（tags 单独返回用于入库前缀）。"""
    raw = path.read_text(encoding="utf-8")
    body = raw
    tags: list[str] = []
    m = _FRONTMATTER_RE.match(raw)
    if m:
        tags = _TAG_RE.findall(m.group(1))
        body = raw[m.end():]
    tm = _TITLE_RE.search(body)
    title = tm.group(1).strip() if tm else path.stem
    # 去掉 "NN " 序号前缀
    title = re.sub(r"^\d+\s+", "", title)
    return title, [t.strip() for t in tags if t.strip()], body


def _matrix_guard(title: str) -> bool:
    """泛化键「矩阵」的保护：标题实指线性变换/向量空间时不用逆矩阵模板。"""
    if "线性变换" in title or "线性映射" in title or "向量空间" in title:
        return False
    return True


def topic_term(title: str) -> str:
    """主题词：取标题中最有区分度的部分（最长中文片段优先）。"""
    blocks = re.findall(r"[\u4e00-\u9fff]{2,}", title)
    if not blocks:
        return title
    return max(blocks, key=len)


def pick_queries(title: str, tags: list[str]) -> list[tuple[str, str]]:
    """按主题生成 (query, expected_route)。一个笔记 1-2 条。"""
    term = topic_term(title)
    queries: list[tuple[str, str]] = []
    for key, template in COMPUTE_TOPICS.items():
        if key not in title:
            continue
        if key == "矩阵" and not _matrix_guard(title):
            continue
        queries.append((template, "solution"))
        break
    if not queries:
        queries.append((f"什么是{term}？", "concept"))
    if len(queries) == 1:
        # 补一条 tag 驱动的概念查询：跳过计算词与泛化标签
        for tag in tags:
            if tag in COMPUTE_VOCAB or tag in GENERIC_TAGS:
                continue
            if tag not in term and len(tag) >= 2:
                queries.append((f"什么是{tag}？", "concept"))
                break
    return queries[:2]


def main() -> None:
    if not NOTES_ROOT.is_dir():
        print(f"笔记目录不存在：{NOTES_ROOT}")
        return 1
    retriever = KeywordRetriever(settings.sqlite_path)
    # 幂等重建：先清掉旧的 gaodai 笔记块（含早期无 tags 前缀的版本），再统一入库
    import sqlite3
    with sqlite3.connect(settings.sqlite_path) as conn:
        conn.execute("DELETE FROM corpus_chunks WHERE source LIKE 'gaodai_notes:%'")
    seeds: list[dict] = []
    ingested = 0
    notes = sorted(NOTES_ROOT.rglob("*.md"))
    for path in notes:
        book = path.parent.name
        title, tags, body = parse_note(path)
        if not body.strip():
            continue
        source = f"gaodai_notes:{book}/{path.name}"
        # tags 前缀进语料：frontmatter 不参与检索，但标签词是查询的自然命中点
        body_with_tags = ("笔记关键词：" + "、".join(tags) + "\n" + body) if tags else body
        doc = RawDocument(
            source=source,
            text=body_with_tags,
            metadata={
                "doc_id": f"gaodai-{book}-{path.stem}",
                "title": title,
                "course": "高等代数",
                "chapter": book,
                "topic": title,
                "doc_type": "self_note",
                "language": "zh",
                "provenance": "self",
                "origin_path": str(path),
                "ingest_policy": "main",
                "license_status": "self_owned_or_authorized",
                "source": source,
            },
        )
        ingested += retriever.add_chunks(chunk_document(doc))
        for i, (query, route) in enumerate(pick_queries(title, tags), start=1):
            seeds.append({
                "id": f"gaodai-{book.replace('（', '').replace('）', '')}-{path.stem.split(' ')[0]:0>2}-{i}",
                "query": query,
                "expected_route": route,
                "expected_topics": [title] + [t for t in tags if t not in title][:2],
                "must_retrieve": True,
                "note_source": str(path.relative_to(NOTES_ROOT.parents[1])),
            })

    # 自检：路由一致性 + 检索命中
    from app.agents import TutorRouter
    router = TutorRouter()
    misroutes: list[str] = []
    misses: list[str] = []
    for s in seeds:
        q = s["query"]
        retrieved = [c.as_dict() for c in retriever.search(q, limit=settings.retrieval_limit)]
        hay = " ".join(
            str(c.get("text", "")) + str(c.get("metadata", {}).get("topic", ""))
            for c in retrieved
        ).lower()
        if not any(t.lower() in hay for t in s["expected_topics"] if t):
            misses.append(s["id"] + " :: " + q)
        route = router.answer(q, retrieved).route
        if route != s["expected_route"]:
            misroutes.append(f"{s['id']} expected={s['expected_route']} got={route} :: {q}")

    EVAL_DIR.mkdir(exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        for s in seeds:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"notes: {len(notes)}, ingested chunks: {ingested}, seeds: {len(seeds)} -> {OUT}")
    if misroutes:
        print("路由不一致（需补 manifest 关键词）：")
        for line in misroutes:
            print("  " + line)
    else:
        print("路由自检：全部一致")
    if misses:
        print("检索漏命中（must_retrieve 未命中）：")
        for line in misses[:10]:
            print("  " + line)
    else:
        print("检索自检：全部命中")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
