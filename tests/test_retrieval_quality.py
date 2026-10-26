from app.rag.loaders import clean_extracted_text
from app.main import citation_instruction, format_sources_for_prompt


def test_clean_removes_ligatures_and_control_chars():
    dirty = "deﬁnition\x07 of ﬂow"
    cleaned = clean_extracted_text(dirty)
    assert "definition" in cleaned
    assert "flow" in cleaned
    assert "\x07" not in cleaned


def test_clean_dehyphenates_linebreak_words():
    dirty = "proba-\nbility distribution"
    assert "probability" in clean_extracted_text(dirty)


def test_clean_drops_repeated_headers_and_page_numbers():
    dirty = "\n".join([
        "统计学讲义", "正文第一段有意义的内容一二三四五",
        "统计学讲义", "正文第二段也是有意义的内容六七八九十",
        "统计学讲义", "第 12 页", "正文第三段继续有意义的内容",
        "统计学讲义",
    ])
    cleaned = clean_extracted_text(dirty)
    assert "统计学讲义" not in cleaned      # 重复≥3次的页眉被剔除
    assert "第 12 页" not in cleaned        # 页码行被剔除
    assert "有意义的内容" in cleaned


def test_citation_instruction_distinguishes_search_miss_from_absent_coverage():
    rule = citation_instruction([])
    assert "本地资料未覆盖" not in rule
    assert "检索工具" in rule or "检索工具补查" in rule
    assert "若最终仍无相关来源" in rule
    assert "不得编造引用编号" in rule


def test_citation_instruction_with_sources_requires_inline_marks():
    rule = citation_instruction([{"text": "x", "metadata": {}}])
    assert "[1]" in rule
    assert "标注" in rule


def test_format_sources_includes_license_tag():
    sources = [{"text": "样本均值趋近正态", "metadata": {
        "course": "概率论",
        "topic": "CLT",
        "doc_type": "self_note",
        "ingest_policy": "main",
        "source_category": "自有笔记",
        "license_status": "self_owned_or_authorized",
    }}]
    out = format_sources_for_prompt(sources)
    assert "[1]" in out
    assert "license=self_owned_or_authorized" in out
    assert "source_category=自有笔记" in out
    assert "doc_type=self_note" in out
