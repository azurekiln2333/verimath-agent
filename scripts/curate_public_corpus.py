from __future__ import annotations

import argparse
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parent.parent
RAW_PUBLIC_INDEX_DIR = PROJECT / "corpus" / "public_index"
RAW_KCONRAD_DIR = PROJECT / "corpus" / "papers" / "kconrad_md"
CURATED_ROOT = PROJECT / "corpus" / "curated"
PUBLIC_MAIN_DIR = CURATED_ROOT / "public_main"
INDEX_CARD_DIR = PUBLIC_MAIN_DIR / "index_cards"
REFERENCE_CARD_DIR = PUBLIC_MAIN_DIR / "reference_cards"
SELF_MAIN_DIR = CURATED_ROOT / "self_main"
EXAM_DIR = CURATED_ROOT / "exam"

SOURCE_LINE_PATTERNS = (
    re.compile(r"^\s*>\s*来源：\s*(\S+)\s*$", re.MULTILINE),
    re.compile(r"^\s*>\s*\*\*Source\*\*:\s*(\S+)\s*$", re.MULTILINE),
)
TOPIC_RE = re.compile(r"^\s*>\s*\*\*Topic\*\*:\s*([A-Za-z0-9_\-]+)\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
SECTION_RE = re.compile(r"^\s*##+\s+(.+?)\s*$", re.MULTILINE)

TOPIC_TO_COURSE = {
    "analysis": "数学分析",
    "group_theory": "抽象代数",
    "galois_theory": "抽象代数",
    "algebra": "抽象代数",
    "number_theory": "数论",
    "topology": "拓扑",
    "statistics": "数理统计",
    "probability": "概率论",
}

PHRASE_TRANSLATIONS = {
    "Gaussian integral": "高斯积分",
    "Metric spaces": "度量空间",
    "Contraction mapping theorem": "压缩映射定理",
    "Infinite series": "无穷级数",
    "Stirling's formula": "斯特林公式",
    "Finite fields": "有限域",
    "Galois correspondence": "伽罗瓦对应",
    "Galois descent": "伽罗瓦下降",
    "Symmetric polynomials": "对称多项式",
    "Roots and irreducible polynomials": "根与不可约多项式",
    "Splitting fields": "分裂域",
    "Differentiation under the integral sign": "积分号下求导",
    "The 15-Puzzle": "十五数码问题",
    "Rubik's Cube": "魔方",
    "Homomorphisms": "同态",
    "Isomorphisms": "同构",
    "Quotient groups": "商群",
    "Finite-dimensional": "有限维",
    "Linear recursion": "线性递推",
    "The logarithm and arctangent": "对数与反正切",
}

WORD_TRANSLATIONS = {
    "gaussian": "高斯",
    "galois": "伽罗瓦",
    "rubik": "魔方",
    "puzzle": "谜题",
    "group": "群",
    "groups": "群",
    "theory": "理论",
    "algebra": "代数",
    "analysis": "分析",
    "field": "域",
    "fields": "域",
    "integral": "积分",
    "series": "级数",
    "polynomial": "多项式",
    "polynomials": "多项式",
    "symmetric": "对称",
    "metric": "度量",
    "spaces": "空间",
    "space": "空间",
    "finite": "有限",
    "proof": "证明",
    "function": "函数",
    "functions": "函数",
    "dimension": "维数",
    "dimensions": "维数",
    "norm": "范数",
    "module": "模",
    "modules": "模",
    "ideal": "理想",
    "ideals": "理想",
    "ring": "环",
    "rings": "环",
    "topology": "拓扑",
    "topological": "拓扑",
    "theorem": "定理",
    "lemma": "引理",
    "proofs": "证明",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Curate local public math corpus into canonical Markdown cards.")
    parser.add_argument(
        "--output-dir",
        default=str(PUBLIC_MAIN_DIR),
        help="Target directory for curated public_main cards.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    counts = curate_public_corpus(output_dir=output_dir)
    print(
        "curated public corpus:",
        f"index_cards={counts['index_cards']}",
        f"reference_cards={counts['reference_cards']}",
        f"output={output_dir}",
    )
    return 0


def curate_public_corpus(output_dir: Path = PUBLIC_MAIN_DIR) -> dict[str, int]:
    index_dir = output_dir / "index_cards"
    reference_dir = output_dir / "reference_cards"
    index_dir.mkdir(parents=True, exist_ok=True)
    reference_dir.mkdir(parents=True, exist_ok=True)
    SELF_MAIN_DIR.mkdir(parents=True, exist_ok=True)
    EXAM_DIR.mkdir(parents=True, exist_ok=True)

    index_count = 0
    for path in sorted(RAW_PUBLIC_INDEX_DIR.glob("*_index.md")):
        target = index_dir / path.name
        target.write_text(build_index_card(path), encoding="utf-8")
        index_count += 1

    reference_count = 0
    for path in sorted(RAW_KCONRAD_DIR.glob("*.md")):
        target = reference_dir / f"{path.stem}_card.md"
        target.write_text(build_reference_card(path), encoding="utf-8")
        reference_count += 1

    return {"index_cards": index_count, "reference_cards": reference_count}


def build_index_card(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore").strip()
    title = extract_title(raw) or path.stem
    source_url = extract_source_url(raw)
    meta = {
        "doc_id": f"public-index-{slugify(path.stem)}",
        "title": title,
        "course": "数学公开资源",
        "chapter": path.stem.replace("_index", ""),
        "topic": title,
        "doc_type": "public_index_card",
        "language": "zh",
        "provenance": "public",
        "license_status": "public_link_index_only",
        "origin_path": str(path),
        "source_url": source_url,
        "ingest_policy": "public",
        "quality_score": "0.58",
    }
    return render_markdown(meta, raw)


def build_reference_card(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    title = extract_title(raw) or path.stem
    source_url = extract_source_url(raw)
    topic = extract_topic(raw) or path.parent.name
    course = TOPIC_TO_COURSE.get(topic, "公开数学参考")
    translated_title = rough_translate_title(title)
    sections = extract_sections(raw)[:6]
    meta = {
        "doc_id": f"public-kconrad-{slugify(path.stem)}",
        "title": title,
        "course": course,
        "chapter": "Keith Conrad",
        "topic": topic,
        "doc_type": "public_reference",
        "language": "zh",
        "provenance": "public",
        "license_status": "public_web_reference",
        "origin_path": str(path),
        "source_url": source_url,
        "ingest_policy": "public",
        "quality_score": "0.76",
    }
    keywords = build_keyword_line(title, topic)
    section_lines = "\n".join(f"- {section}" for section in sections) if sections else "- 原文以英文数学讲义结构展开"
    zh_title = translated_title or title
    body = (
        f"# {zh_title}\n\n"
        f"## 原始标题\n"
        f"- English: {title}\n"
        f"- Topic: {topic}\n"
        f"- 课程归类: {course}\n\n"
        f"## 中文摘要卡\n"
        f"这是一份 Keith Conrad 的英文公开数学讲义，适合数学与统计专业学生做延伸阅读。"
        f"回答时应优先用中文概括，再把这份资料作为原始论证、英文术语和进一步阅读入口。\n\n"
        f"## 使用建议\n"
        f"- 优先和本地中文主档配合使用，不直接把英文长段当作默认答案主体。\n"
        f"- 当本地主库缺少某个定义、例子或证明视角时，可引用这份资料补充背景。\n"
        f"- 需要原文时展示链接，不把整段英文原文直接搬运到回答里。\n\n"
        f"## 检索关键词\n"
        f"- {keywords}\n\n"
        f"## 原文结构线索\n"
        f"{section_lines}\n\n"
        f"## 延伸阅读\n"
        f"- 原始链接: {source_url or 'unknown'}\n"
        f"- 本地原文路径: {path}\n"
    )
    return render_markdown(meta, body.strip())


def render_markdown(metadata: dict[str, str], body: str) -> str:
    frontmatter = "\n".join(f'{key}: "{escape_frontmatter(value)}"' for key, value in metadata.items())
    return f"---\n{frontmatter}\n---\n\n{body.strip()}\n"


def extract_title(text: str) -> str:
    match = TITLE_RE.search(text)
    return match.group(1).strip() if match else ""


def extract_source_url(text: str) -> str:
    for pattern in SOURCE_LINE_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1).strip()
    return ""


def extract_topic(text: str) -> str:
    match = TOPIC_RE.search(text)
    return match.group(1).strip() if match else ""


def extract_sections(text: str) -> list[str]:
    sections: list[str] = []
    for match in SECTION_RE.finditer(text):
        section = match.group(1).strip()
        if section.startswith("page "):
            continue
        sections.append(section)
    return sections


def rough_translate_title(title: str) -> str:
    translated = title
    for source, target in sorted(PHRASE_TRANSLATIONS.items(), key=lambda item: -len(item[0])):
        translated = re.sub(re.escape(source), target, translated, flags=re.IGNORECASE)
    words = re.split(r"(\W+)", translated)
    output: list[str] = []
    for word in words:
        clean = word.strip()
        key = clean.lower()
        if key in WORD_TRANSLATIONS:
            output.append(WORD_TRANSLATIONS[key])
        else:
            output.append(word)
    rendered = "".join(output).strip()
    rendered = re.sub(r"\b(the|a|an)\b", "", rendered, flags=re.IGNORECASE)
    rendered = re.sub(r"\s{2,}", " ", rendered).strip(" -")
    return rendered


def build_keyword_line(title: str, topic: str) -> str:
    translated_title = rough_translate_title(title)
    title_terms = re.findall(r"[A-Za-z][A-Za-z0-9'\-]+", title)
    zh_topic = TOPIC_TO_COURSE.get(topic, topic)
    terms = [zh_topic, translated_title, *title_terms[:6]]
    deduped: list[str] = []
    for term in terms:
        if term and term not in deduped:
            deduped.append(term)
    return " / ".join(deduped)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "doc"


def escape_frontmatter(value: str) -> str:
    return str(value).replace('"', '\\"')


if __name__ == "__main__":
    raise SystemExit(main())
