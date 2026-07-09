from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


CANONICAL_METADATA_KEYS = (
    "doc_id",
    "title",
    "course",
    "chapter",
    "topic",
    "doc_type",
    "language",
    "provenance",
    "license_status",
    "origin_path",
    "source_url",
    "ingest_policy",
    "quality_score",
    "source",
)

QUALITY_BY_DOC_TYPE = {
    "self_note": 0.92,
    "lecture_note": 0.82,
    "public_index_card": 0.58,
    "public_reference": 0.76,
    "public_index_raw": 0.24,
    "public_reference_raw": 0.26,
    "exam_sheet": 0.42,
    "answer_key": 0.36,
}

TOPIC_COURSE_MAP = {
    "analysis": "数学分析",
    "group_theory": "抽象代数",
    "galois_theory": "抽象代数",
    "number_theory": "数论",
    "linear_algebra": "线性代数",
    "topology": "拓扑",
    "algebra": "抽象代数",
    "statistics": "数理统计",
    "probability": "概率论",
}


# 常见连字 -> ASCII，PDF 抽取里很常见
_LIGATURES = {
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "ft",
    "ﬆ": "st",
}
# 控制字符（保留 \n \t），PDF 抽取残留的不可见噪音
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
# 纯页码/页眉页脚行（如 "第 12 页"、"- 3 -"、孤立数字）
_PAGE_NUM_RE = re.compile(r"^\s*(第?\s*\d+\s*页?|[-—]\s*\d+\s*[-—]|\d{1,4})\s*$")
_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
_MD_TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
_SOURCE_LINE_PATTERNS = (
    re.compile(r"^\s*>\s*\*\*Source\*\*:\s*(\S+)\s*$", re.MULTILINE),
    re.compile(r"^\s*>\s*来源：\s*(\S+)\s*$", re.MULTILINE),
    re.compile(r"^\s*-\s*URL:\s*(\S+)\s*$", re.MULTILINE),
)
_KCONRAD_TOPIC_RE = re.compile(r"^\s*>\s*\*\*Topic\*\*:\s*([A-Za-z0-9_\-]+)\s*$", re.MULTILINE)


def clean_extracted_text(text: str) -> str:
    """清洗 PDF/DOCX 抽取噪音：连字、控制字符、断词连字符、重复页眉页脚、多余空白。
    只做保守清洗，不改动数学内容语义。"""
    if not text:
        return ""
    for lig, repl in _LIGATURES.items():
        text = text.replace(lig, repl)
    text = unicodedata.normalize("NFKC", text)
    text = _CONTROL_RE.sub("", text)
    # 英文断词：行尾连字符 + 换行 -> 拼回单词（word-\nbreak -> wordbreak）
    text = re.sub(r"([A-Za-z])-\n([a-z])", r"\1\2", text)
    lines = [ln.strip() for ln in text.split("\n")]
    # 识别在多页重复出现的短行（页眉/页脚），出现>=3次且短的判为噪音
    counts = Counter(ln for ln in lines if ln and len(ln) <= 40)
    repeated = {ln for ln, c in counts.items() if c >= 3}
    kept: list[str] = []
    for ln in lines:
        if not ln:
            continue
        if _PAGE_NUM_RE.match(ln):
            continue
        if ln in repeated:
            continue
        kept.append(ln)
    text = "\n".join(kept).strip()
    return _clean_cjk(text)


# 句末标点：用于判断“句中断行”是否该合并
_SENT_END = "。！？；.!?;：:"
_CJK = r"一-鿿　-〿＀-￯"
# PDF 常在中文字符间误插空格
_CJK_SPACE_RE = re.compile(rf"(?<=[{_CJK}])[ \t]+(?=[{_CJK}])")


def _clean_cjk(text: str) -> str:
    """中文专项清洗（保守，不改数学语义）：字间误插空格、句中断行合并。"""
    if not text:
        return ""
    prev = None
    while prev != text:
        prev = text
        text = _CJK_SPACE_RE.sub("", text)
    out_lines: list[str] = []
    for ln in text.split("\n"):
        if (
            out_lines
            and out_lines[-1]
            and out_lines[-1][-1] not in _SENT_END
            and ln
            and re.match(rf"^[{_CJK}]", ln)
            and re.search(rf"[{_CJK}]$", out_lines[-1])
        ):
            out_lines[-1] += ln
        else:
            out_lines.append(ln)
    return "\n".join(out_lines).strip()


@dataclass(frozen=True)
class RawDocument:
    source: str
    text: str
    metadata: dict[str, str]


def load_document(path: Path, license_status: str = "self_owned_or_authorized") -> RawDocument:
    suffix = path.suffix.lower()
    frontmatter: dict[str, str] = {}
    if suffix in {".txt", ".md", ".markdown"}:
        raw_text = path.read_text(encoding="utf-8", errors="ignore")
        frontmatter, text = _parse_frontmatter(raw_text)
    elif suffix == ".pdf":
        text = clean_extracted_text(_read_pdf(path))
    elif suffix == ".docx":
        text = clean_extracted_text(_read_docx(path))
    else:
        raise ValueError(f"unsupported file extension: {suffix}")

    metadata = _build_document_metadata(
        path,
        text=text,
        frontmatter=frontmatter,
        default_license_status=license_status,
    )
    return RawDocument(source=str(path), text=text, metadata=metadata)


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    body = text[match.end() :]
    metadata: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            metadata[key] = value
    return metadata, body.lstrip()


def _build_document_metadata(
    path: Path,
    text: str,
    frontmatter: dict[str, str],
    default_license_status: str,
) -> dict[str, str]:
    defaults = _classify_path_defaults(path, text, default_license_status)
    merged = {**defaults, **{k: str(v) for k, v in frontmatter.items() if v is not None}}
    merged["source"] = str(path)
    merged["origin_path"] = merged.get("origin_path") or str(path)
    merged["title"] = merged.get("title") or _extract_markdown_title(text) or path.stem
    merged["topic"] = merged.get("topic") or _extract_topic(path, text, merged["title"])
    merged["course"] = merged.get("course") or _guess_course(path, text)
    merged["chapter"] = merged.get("chapter") or _guess_chapter(path)
    merged["source_url"] = merged.get("source_url") or _extract_source_url(text)
    merged["language"] = merged.get("language") or _detect_language(text)
    merged["doc_id"] = merged.get("doc_id") or _build_doc_id(path)
    merged["quality_score"] = _normalize_quality_score(
        merged.get("quality_score"),
        merged.get("doc_type", "self_note"),
    )
    for key in CANONICAL_METADATA_KEYS:
        merged.setdefault(key, "")
    return {key: str(value) for key, value in merged.items() if value is not None}


def _classify_path_defaults(path: Path, text: str, default_license_status: str) -> dict[str, str]:
    normalized = path.as_posix().lower()
    doc_type = "self_note"
    provenance = "self"
    ingest_policy = "main"
    license_status = default_license_status
    chapter = _guess_chapter(path)
    course = _guess_course(path, text)

    if "/corpus/curated/public_main/index_cards/" in normalized:
        doc_type = "public_index_card"
        provenance = "public"
        ingest_policy = "public"
        license_status = "public_link_index_only"
        course = "数学公开资源"
    elif "/corpus/curated/public_main/reference_cards/" in normalized:
        doc_type = "public_reference"
        provenance = "public"
        ingest_policy = "public"
        license_status = "public_web_reference"
        course = _course_from_text(text) or course
        chapter = "公开参考资料"
    elif "/corpus/papers/kconrad_md/" in normalized or "/corpus/public_index/kconrad_papers/" in normalized:
        doc_type = "public_reference_raw"
        provenance = "public"
        ingest_policy = "hold"
        license_status = "public_web_reference"
        course = _course_from_text(text) or "公开数学参考"
        chapter = "Keith Conrad"
    elif "/corpus/public_index/" in normalized:
        doc_type = "public_index_raw"
        provenance = "public"
        ingest_policy = "hold"
        license_status = "public_link_index_only"
        course = "数学公开资源"
        chapter = path.parent.name
    elif "/corpus/curated/exam/" in normalized or any(part.startswith("90_") for part in path.parts):
        doc_type = "exam_sheet"
        provenance = "self"
        ingest_policy = "exam"
        chapter = path.parent.name
    elif any(part.startswith("91_") for part in path.parts) or "答案评分" in str(path):
        doc_type = "answer_key"
        provenance = "self"
        ingest_policy = "exam"
        chapter = path.parent.name
    elif path.suffix.lower() in {".pdf", ".docx"}:
        doc_type = "lecture_note"

    return {
        "doc_type": doc_type,
        "provenance": provenance,
        "license_status": license_status,
        "origin_path": str(path),
        "source_url": _extract_source_url(text),
        "ingest_policy": ingest_policy,
        "quality_score": _normalize_quality_score("", doc_type),
        "course": course,
        "chapter": chapter,
        "title": _extract_markdown_title(text) or path.stem,
        "topic": _extract_topic(path, text, path.stem),
        "language": _detect_language(text),
    }


def _extract_markdown_title(text: str) -> str:
    match = _MD_TITLE_RE.search(text)
    return match.group(1).strip() if match else ""


def _extract_source_url(text: str) -> str:
    for pattern in _SOURCE_LINE_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1).strip()
    return ""


def _extract_topic(path: Path, text: str, fallback: str) -> str:
    match = _KCONRAD_TOPIC_RE.search(text)
    if match:
        return match.group(1).strip()
    parent = path.parent.name
    if parent and parent not in {"public_main", "reference_cards", "index_cards"}:
        return parent
    return fallback


def _course_from_text(text: str) -> str:
    topic_match = _KCONRAD_TOPIC_RE.search(text)
    if topic_match:
        topic = topic_match.group(1).strip()
        return TOPIC_COURSE_MAP.get(topic, "公开数学参考")
    return ""


def _normalize_quality_score(value: str | None, doc_type: str) -> str:
    if value:
        try:
            score = float(value)
        except ValueError:
            score = QUALITY_BY_DOC_TYPE.get(doc_type, 0.65)
    else:
        score = QUALITY_BY_DOC_TYPE.get(doc_type, 0.65)
    score = min(max(score, 0.0), 1.0)
    return f"{score:.2f}"


def _detect_language(text: str) -> str:
    if not text.strip():
        return "unknown"
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    if cjk >= 24 and cjk >= latin:
        return "zh"
    if latin >= 24 and latin > cjk:
        return "en"
    if cjk and latin:
        return "mixed"
    return "unknown"


def _build_doc_id(path: Path) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-") or "doc"
    digest = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:10]
    return f"{stem}-{digest}"


def _split_paragraphs(text: str) -> list[str]:
    """按空行/换行切段，保留段内文本；过滤空段。"""
    paras = re.split(r"\n\s*\n|\n", text)
    return [p.strip() for p in paras if p.strip()]


def _split_sentences(para: str) -> list[str]:
    """按中英文句末标点切句，标点跟随前句；无标点时整段作一句。"""
    parts = re.split(rf"(?<=[{_SENT_END}])", para)
    sents = [s.strip() for s in parts if s.strip()]
    return sents or ([para.strip()] if para.strip() else [])


def chunk_document(document: RawDocument, chunk_size: int = 900, overlap: int = 120) -> list[RawDocument]:
    """段落/句子感知切块：只在句子边界断开，保留段落结构，不再压平为一行。"""
    if not document.text.strip():
        return []
    units: list[str] = []
    for para in _split_paragraphs(document.text):
        if len(para) <= chunk_size:
            units.append(para)
        else:
            units.extend(_split_sentences(para))

    chunks: list[RawDocument] = []
    index = 0
    buf: list[str] = []
    buf_len = 0
    for unit in units:
        add_len = len(unit) + (1 if buf else 0)
        if buf and buf_len + add_len > chunk_size:
            chunks.append(_make_chunk(document, "\n".join(buf), index))
            index += 1
            keep: list[str] = []
            keep_len = 0
            for u in reversed(buf):
                if keep_len + len(u) > overlap:
                    break
                keep.insert(0, u)
                keep_len += len(u) + 1
            buf = keep
            buf_len = sum(len(u) + 1 for u in buf)
        buf.append(unit)
        buf_len += add_len
    if buf:
        chunks.append(_make_chunk(document, "\n".join(buf), index))
    return chunks


def _make_chunk(document: RawDocument, text: str, index: int) -> RawDocument:
    metadata = dict(document.metadata)
    metadata["chunk_index"] = str(index)
    return RawDocument(source=document.source, text=text, metadata=metadata)


def _read_pdf(path: Path) -> str:
    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise RuntimeError("PyMuPDF is required to index PDF files") from exc
    doc = fitz.open(path)
    return "\n".join(page.get_text("text") for page in doc)


def _read_docx(path: Path) -> str:
    try:
        import docx
    except ImportError as exc:
        raise RuntimeError("python-docx is required to index DOCX files") from exc
    document = docx.Document(path)
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def _guess_course(path: Path, text: str = "") -> str:
    parts = list(path.parts)
    for name in ("概率论", "数分高代", "高代数分", "数理统计", "回归分析", "时间序列"):
        if name in parts or name in path.name:
            return name
    if "/corpus/public_index/" in path.as_posix().lower():
        return "数学公开资源"
    if text:
        topic_course = _course_from_text(text)
        if topic_course:
            return topic_course
    return path.parent.name or "unknown"


def _guess_chapter(path: Path) -> str:
    parent = path.parent.name
    if parent and parent not in {"概率论", "数分高代", "高代数分"}:
        return parent
    return "unknown"
