from __future__ import annotations

import sys
from pathlib import Path

from app.rag.loaders import RawDocument, load_document
from app.rag.store import KeywordRetriever


_SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import curate_public_corpus as cpc


def test_load_document_parses_canonical_frontmatter(tmp_path):
    path = tmp_path / "self_note.md"
    path.write_text(
        """---
doc_id: "self-clt"
title: "中心极限定理主档"
course: "概率论"
chapter: "极限定理"
topic: "中心极限定理"
doc_type: "self_note"
language: "zh"
provenance: "self"
license_status: "self_owned_or_authorized"
origin_path: "self_note.md"
source_url: ""
ingest_policy: "main"
quality_score: "0.95"
---

# 中心极限定理

中心极限定理说明，在独立同分布且方差有限时，样本均值标准化后近似服从正态分布。
""",
        encoding="utf-8",
    )
    document = load_document(path)
    assert document.metadata["doc_id"] == "self-clt"
    assert document.metadata["doc_type"] == "self_note"
    assert document.metadata["ingest_policy"] == "main"
    assert document.metadata["quality_score"] == "0.95"
    assert document.text.startswith("# 中心极限定理")


def test_raw_public_index_defaults_to_hold_policy(tmp_path):
    path = tmp_path / "corpus" / "public_index" / "demo_index.md"
    path.parent.mkdir(parents=True)
    path.write_text(
        "# Demo Public Index\n\n> 来源：https://example.com\n\n## 合规声明\n- 仅索引卡\n",
        encoding="utf-8",
    )
    document = load_document(path, license_status="self_owned_or_authorized")
    assert document.metadata["provenance"] == "public"
    assert document.metadata["doc_type"] == "public_index_raw"
    assert document.metadata["ingest_policy"] == "hold"
    assert document.metadata["license_status"] == "public_link_index_only"


def test_curate_public_reference_card_has_canonical_metadata(tmp_path):
    path = tmp_path / "gaussianintegral.md"
    path.write_text(
        """# The Gaussian integral

> **Source**: https://example.com/gaussianintegral.pdf
> **Author**: Keith Conrad
> **Topic**: analysis

## 1. Introduction

Some notes.

## 2. Proof

More notes.
""",
        encoding="utf-8",
    )
    rendered = cpc.build_reference_card(path)
    assert 'doc_type: "public_reference"' in rendered
    assert 'ingest_policy: "public"' in rendered
    assert 'license_status: "public_web_reference"' in rendered
    assert "中文摘要卡" in rendered
    assert "高斯积分" in rendered or "Gaussian integral" in rendered


def test_retriever_prefers_curated_card_over_raw_public_text(tmp_path):
    db_path = tmp_path / "rag.sqlite"
    curated = RawDocument(
        source="curated",
        text="高斯积分是分析学中的经典积分，常用于正态分布推导。",
        metadata={
            "doc_id": "curated-gaussian",
            "title": "高斯积分中文卡",
            "course": "数学分析",
            "chapter": "公开参考资料",
            "topic": "analysis",
            "doc_type": "public_reference",
            "language": "zh",
            "provenance": "public",
            "source": "curated",
            "origin_path": "curated",
            "source_url": "https://example.com/gaussianintegral.pdf",
            "license_status": "public_web_reference",
            "ingest_policy": "public",
            "quality_score": "0.76",
        },
    )
    raw = RawDocument(
        source="raw",
        text="高斯积分是分析学中的经典积分，常用于正态分布推导。",
        metadata={
            "doc_id": "raw-gaussian",
            "title": "The Gaussian integral",
            "course": "数学分析",
            "chapter": "Keith Conrad",
            "topic": "analysis",
            "doc_type": "public_reference_raw",
            "language": "en",
            "provenance": "public",
            "source": "raw",
            "origin_path": "raw",
            "source_url": "https://example.com/gaussianintegral.pdf",
            "license_status": "public_web_reference",
            "ingest_policy": "hold",
            "quality_score": "0.26",
        },
    )
    store = KeywordRetriever(db_path)
    assert store.replace_chunks([raw, curated]) == 2
    results = store.search("高斯积分", limit=2)
    assert results[0].metadata["doc_type"] == "public_reference"
    assert results[0].metadata["source_category"] == "公开原文"
