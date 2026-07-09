from app.rag.loaders import RawDocument, chunk_document
from app.rag.store import KeywordRetriever, build_query_terms
from app.rag.whitelist import is_allowed_file


def test_keyword_retriever_roundtrip(tmp_path):
    db_path = tmp_path / "rag.sqlite"
    document = RawDocument(
        source="local",
        text="Welch t 检验适合两独立样本且方差不齐的均值比较。",
        metadata={
            "doc_id": "welch-note",
            "title": "Welch t 检验",
            "course": "数理统计",
            "chapter": "假设检验",
            "topic": "Welch t 检验",
            "doc_type": "self_note",
            "language": "zh",
            "provenance": "self",
            "source": "local",
            "origin_path": "local",
            "source_url": "",
            "license_status": "self_owned_or_authorized",
            "ingest_policy": "main",
            "quality_score": "0.92",
        },
    )
    chunks = chunk_document(document, chunk_size=80, overlap=10)
    store = KeywordRetriever(db_path)
    assert store.replace_chunks(chunks) == 1
    results = store.search("Welch t 检验", limit=3)
    assert len(results) == 1
    assert results[0].metadata["license_status"] == "self_owned_or_authorized"
    assert results[0].metadata["source_category"] == "自有笔记"


def test_keyword_retriever_handles_chinese_sentence_query(tmp_path):
    db_path = tmp_path / "rag.sqlite"
    document = RawDocument(
        source="local",
        text="中心极限定理说明，在独立同分布且方差有限时，样本均值标准化后近似服从正态分布。",
        metadata={
            "doc_id": "clt-note",
            "title": "中心极限定理",
            "course": "概率论",
            "chapter": "极限定理",
            "topic": "中心极限定理",
            "doc_type": "self_note",
            "language": "zh",
            "provenance": "self",
            "source": "local",
            "origin_path": "local",
            "source_url": "",
            "license_status": "self_owned_or_authorized",
            "ingest_policy": "main",
            "quality_score": "0.95",
        },
    )
    store = KeywordRetriever(db_path)
    assert store.replace_chunks(chunk_document(document, chunk_size=80, overlap=10)) == 1
    results = store.search("中心极限定理是什么？", limit=3)
    assert len(results) == 1
    assert results[0].metadata["topic"] == "中心极限定理"
    assert results[0].score > 1


def test_build_query_terms_extracts_domain_terms():
    terms = build_query_terms("中心极限定理是什么？和大数定律怎么区分")
    assert "中心极限定理" in terms
    assert "大数定律" in terms
    assert "是什么" not in terms


def test_whitelist_blocks_sensitive_files(tmp_path):
    root = tmp_path
    secret = root / "secret.pem"
    note = root / "note.pdf"
    assert is_allowed_file(secret, [root]) is False
    assert is_allowed_file(note, [root]) is True
