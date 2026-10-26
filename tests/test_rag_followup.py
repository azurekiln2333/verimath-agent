"""Regression cases for Chinese recall, grounded excerpts and follow-up context."""
from __future__ import annotations

import pytest

from app.model_client import ModelMessage
from app.rag.context import retrieval_query
from app.rag.loaders import RawDocument
from app.rag.sources import SourceLedger, format_sources_for_prompt
from app.rag.store import KeywordRetriever, build_query_terms, content_key


def note(text, title="数学笔记", **metadata):
    return RawDocument(source="synthetic", text=text, metadata={"title": title, **metadata})


@pytest.mark.parametrize("query, text", [
    ("极坐标换元", "极坐标中面积元带有 r 因子。"),
    ("三角恒等变形", "三角恒等式可用于降低三角函数的幂次。"),
    ("这里的三角变换是什么", "三角恒等式包含倍角公式。"),
    ("高斯分布", "正态分布由均值和方差决定。"),
    ("Jacobian", "雅可比行列式描述坐标变换的局部面积缩放。"),
])
def test_compound_and_alias_queries_retrieve_available_notes(tmp_path, query, text):
    store = KeywordRetriever(tmp_path / "rag.sqlite")
    store.add_chunks([note(text)])
    assert store.search(query)[0].text == text


@pytest.mark.parametrize("query", ["这一步是怎么得到的", "为什么要乘r", "这里为什么这样", "2026 42", "what is this"])
def test_generic_words_and_numbers_do_not_retrieve_unrelated_courses(tmp_path, query):
    store = KeywordRetriever(tmp_path / "rag.sqlite")
    store.add_chunks([note("这一步得到回归方程，2026 年第 42 页。")])
    assert store.search(query) == []


def test_no_early_candidate_limit_and_format_duplicates_do_not_hide_notes(tmp_path):
    store = KeywordRetriever(tmp_path / "rag.sqlite")
    notes = [note(f"正态分布仅被顺带提到。练习编号 {i}") for i in range(80)]
    notes.extend([
        note("[!note]\n中心极限定理连接独立和与[[正态分布]]。", "中心极限定理"),
        note("**中心极限定理**连接独立和与正态分布。", "中心极限定理"),
        note("正态分布的概率密度呈钟形。", "正态分布", topic="正态分布", quality_score="0.9"),
    ])
    store.replace_chunks(notes)
    assert store.search("正态分布", limit=1)[0].metadata["title"] == "正态分布"
    results = store.search("中心极限定理", limit=4)
    assert len(results) == 1
    assert store.stats()["chunks"] == 83  # Read-time dedup never deletes documents.


def test_dedup_preserves_different_mathematical_claims():
    assert content_key("x + 1 = 2") != content_key("x - 1 = 2")
    assert content_key("x = 1") != content_key("x = 2")


@pytest.mark.parametrize("punctuated", [True, False])
def test_deep_hit_reaches_both_source_card_and_model(tmp_path, punctuated):
    store = KeywordRetriever(tmp_path / "rag.sqlite")
    filler = "背景说明。" if punctuated else "背景说明"
    text = filler * 300 + "雅可比表示局部面积缩放因子。" + filler * 300
    store.add_chunks([note(text)])
    source = store.search("雅可比")[0].as_dict()
    assert "雅可比" in source["text"] and len(source["text"]) <= 700
    assert "雅可比" in source["excerpt"][:160]
    assert "雅可比" in format_sources_for_prompt([source])


HISTORY = [ModelMessage("user", "二重积分如何使用极坐标换元"),
           ModelMessage("assistant", "极坐标中的雅可比是 r，用来计算面积元。")]


@pytest.mark.parametrize("query", ["这一步是怎么得到的", "为什么要乘r", "积分限为什么是这样"])
def test_short_followup_inherits_recent_subject(query):
    resolved = retrieval_query(query, HISTORY)
    assert resolved.startswith(query) and "极坐标" in resolved
    assert "雅可比" in resolved


@pytest.mark.parametrize("query", ["什么是正态分布", "换个话题，解释正态分布", "另外一个问题：这是什么"])
def test_new_subject_does_not_inherit_old_integral(query):
    assert retrieval_query(query, HISTORY) == query


def test_later_subject_stops_followup_from_crossing_topic_boundary():
    history = HISTORY + [ModelMessage("user", "什么是正态分布"), ModelMessage("assistant", "高斯分布由均值和方差决定。")]
    resolved = retrieval_query("这里是什么意思", history)
    assert "正态分布" in resolved and "极坐标" not in resolved
    assert retrieval_query("这一步怎么得到的", []) == "这一步怎么得到的"


def test_all_initial_sources_are_visible_and_tool_sources_continue_numbering():
    sources = [{"chunk_id": i, "text": f"资料{i}", "metadata": {}} for i in range(1, 6)]
    assert "[5]" in format_sources_for_prompt(sources)
    ledger = SourceLedger(sources[:2])
    text = ledger.add([sources[1], sources[2], sources[2]])
    assert "[2]" in text and "[3]" in text and "[1]" not in text
    assert len(ledger.sources) == 3
    assert "[1]" in SourceLedger().add([sources[2]])  # Separate answer, separate numbering.
