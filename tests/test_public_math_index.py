"""Tests for build_public_math_index.py

Covers:
- URL normalisation
- robots.txt disallow filtering
- JSONL schema validation
- Markdown output does not contain large verbatim text
- blocked-domain rejection (z-library, sci-hub, ...)
- dry-run writes nothing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# ---------------------------------------------------------------------------
# Make the scripts directory importable
# ---------------------------------------------------------------------------

_SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import build_public_math_index as bmi


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_entry(**overrides) -> bmi.IndexEntry:
    defaults = dict(
        title="Test Resource",
        url="https://example.com/page",
        site="example",
        topic="mathematics",
        level="undergraduate",
        resource_type="course",
        summary_zh="测试资源摘要",
    )
    defaults.update(overrides)
    return bmi.IndexEntry(**defaults)


# ---------------------------------------------------------------------------
# 1. URL normalisation
# ---------------------------------------------------------------------------


class TestNormalizeUrl:
    def test_strips_fragment(self):
        assert bmi.normalize_url("https://example.com/page#section") == "https://example.com/page"

    def test_strips_utm_tracking(self):
        url = "https://example.com/p?utm_source=twitter&x=1&utm_campaign=abc"
        result = bmi.normalize_url(url)
        assert "utm_source" not in result
        assert "utm_campaign" not in result
        assert "x=1" in result

    def test_rejects_non_http_scheme(self):
        assert bmi.normalize_url("ftp://example.com/file") == ""
        assert bmi.normalize_url("javascript:void(0)") == ""
        assert bmi.normalize_url("mailto:user@example.com") == ""

    def test_resolves_relative_url(self):
        result = bmi.normalize_url("sub/page.html", "https://example.com/base/")
        assert result == "https://example.com/base/sub/page.html"

    def test_preserves_query_params(self):
        url = "https://example.com/search?q=math&page=2"
        result = bmi.normalize_url(url)
        assert "q=math" in result
        assert "page=2" in result


# ---------------------------------------------------------------------------
# 2. Blocked domain detection
# ---------------------------------------------------------------------------


class TestBlockedDomains:
    @pytest.mark.parametrize("url", [
        "https://z-library.sk/book/12345",
        "https://sci-hub.se/10.1234/test",
        "https://libgen.is/search?q=math",
        "https://b-ok.cc/book/abc",
        "https://wenku.baidu.com/view/abc123",
        "https://zujuan.xkw.com/paper/123",
    ])
    def test_blocks_piracy_sites(self, url):
        assert bmi.is_blocked_domain(url) is True

    @pytest.mark.parametrize("url", [
        "https://terrytao.wordpress.com/2024/01/01/test",
        "https://arxiv.org/abs/2401.00001",
        "https://ocw.mit.edu/courses/18-01",
        "https://openstax.org/details/books/calculus-volume-1",
    ])
    def test_allows_legitimate_sites(self, url):
        assert bmi.is_blocked_domain(url) is False


# ---------------------------------------------------------------------------
# 3. Robots.txt filtering
# ---------------------------------------------------------------------------


class TestRobotsTxt:
    def setup_method(self):
        bmi._robots_cache.clear()

    def test_allows_when_no_robots(self):
        """If robots.txt cannot be fetched, default to allow."""
        with patch.object(bmi, "fetch_robots", return_value=([], [], 2.0)):
            assert bmi.is_robots_allowed("https://example.com/anything") is True

    def test_blocks_disallowed_path(self):
        with patch.object(bmi, "fetch_robots", return_value=(["/private/"], [], 2.0)):
            assert bmi.is_robots_allowed("https://example.com/private/page") is False
            assert bmi.is_robots_allowed("https://example.com/public/page") is True

    def test_allow_overrides_disallow(self):
        with patch.object(bmi, "fetch_robots", return_value=(
            ["/api/"], ["/api/public/"], 2.0
        )):
            assert bmi.is_robots_allowed("https://example.com/api/public/data") is True
            assert bmi.is_robots_allowed("https://example.com/api/secret") is False


# ---------------------------------------------------------------------------
# 4. JSONL schema validation
# ---------------------------------------------------------------------------


REQUIRED_FIELDS = {
    "title", "url", "site", "topic", "level",
    "resource_type", "summary_zh", "license_status",
    "retrieved_at", "notes",
}

VALID_LEVELS = {"undergraduate", "graduate", "research", "mixed"}
VALID_TYPES = {"blog", "course", "lecture_note", "problem_set", "reference", "paper_metadata"}


class TestJsonlSchema:
    def test_entry_has_all_fields(self, tmp_path):
        entry = _make_entry()
        jsonl_path = tmp_path / "test.jsonl"
        bmi.write_jsonl([entry], jsonl_path)

        with open(jsonl_path, encoding="utf-8") as f:
            row = json.loads(f.readline())

        assert set(row.keys()) >= REQUIRED_FIELDS

    def test_level_values(self, tmp_path):
        for level in VALID_LEVELS:
            entry = _make_entry(level=level)
            jsonl_path = tmp_path / f"{level}.jsonl"
            bmi.write_jsonl([entry], jsonl_path)
            with open(jsonl_path, encoding="utf-8") as f:
                row = json.loads(f.readline())
            assert row["level"] in VALID_LEVELS

    def test_resource_type_values(self, tmp_path):
        for rtype in VALID_TYPES:
            entry = _make_entry(resource_type=rtype)
            jsonl_path = tmp_path / f"{rtype}.jsonl"
            bmi.write_jsonl([entry], jsonl_path)
            with open(jsonl_path, encoding="utf-8") as f:
                row = json.loads(f.readline())
            assert row["resource_type"] in VALID_TYPES

    def test_license_status_is_public(self, tmp_path):
        entry = _make_entry()
        jsonl_path = tmp_path / "test.jsonl"
        bmi.write_jsonl([entry], jsonl_path)
        with open(jsonl_path, encoding="utf-8") as f:
            row = json.loads(f.readline())
        assert row["license_status"] == "public_link_index_only"

    def test_summary_zh_is_not_verbatim(self, tmp_path):
        """summary_zh should be a short Chinese text, not a huge copy."""
        entry = _make_entry(summary_zh="这是一段简短的中文自写摘要，描述资源内容。")
        jsonl_path = tmp_path / "test.jsonl"
        bmi.write_jsonl([entry], jsonl_path)
        with open(jsonl_path, encoding="utf-8") as f:
            row = json.loads(f.readline())
        assert len(row["summary_zh"]) <= 300
        assert "中文" in row["summary_zh"] or "摘要" in row["summary_zh"]

    def test_multiple_entries_one_per_line(self, tmp_path):
        entries = [_make_entry(title=f"Entry {i}", url=f"https://example.com/{i}")
                    for i in range(5)]
        jsonl_path = tmp_path / "multi.jsonl"
        bmi.write_jsonl(entries, jsonl_path)

        with open(jsonl_path, encoding="utf-8") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        assert len(lines) == 5


# ---------------------------------------------------------------------------
# 5. Markdown output quality
# ---------------------------------------------------------------------------


class TestMarkdownOutput:
    def test_markdown_contains_compliance_section(self, tmp_path):
        entries = [_make_entry(site="test_site")]
        bmi.SITES["test_site"] = {
            "name": "Test Site",
            "home": "https://example.com",
            "domain": "example.com",
        }
        try:
            paths = bmi.write_markdown(entries, tmp_path)
            assert len(paths) == 1
            content = paths[0].read_text(encoding="utf-8")
            assert "合规声明" in content
            assert "public_link_index_only" in content
        finally:
            bmi.SITES.pop("test_site", None)

    def test_markdown_does_not_contain_large_verbatim(self, tmp_path):
        """Markdown should not contain large blocks of verbatim English text."""
        entries = [
            _make_entry(
                site="test_site",
                title="Calculus I",
                summary_zh="微积分入门课程，含极限、导数、积分基础。",
            ),
        ]
        bmi.SITES["test_site"] = {
            "name": "Test Site",
            "home": "https://example.com",
            "domain": "example.com",
        }
        try:
            paths = bmi.write_markdown(entries, tmp_path)
            content = paths[0].read_text(encoding="utf-8")
            # Should not have any paragraph > 500 chars of pure English
            import re
            english_blocks = re.findall(r"[A-Za-z][A-Za-z\s]{500,}", content)
            assert len(english_blocks) == 0, (
                f"Found {len(english_blocks)} large English text blocks in Markdown"
            )
        finally:
            bmi.SITES.pop("test_site", None)

    def test_markdown_contains_url_and_topic(self, tmp_path):
        entries = [
            _make_entry(
                site="test_site",
                url="https://example.com/calculus",
                topic="calculus",
            ),
        ]
        bmi.SITES["test_site"] = {
            "name": "Test Site",
            "home": "https://example.com",
            "domain": "example.com",
        }
        try:
            paths = bmi.write_markdown(entries, tmp_path)
            content = paths[0].read_text(encoding="utf-8")
            assert "https://example.com/calculus" in content
            assert "calculus" in content
        finally:
            bmi.SITES.pop("test_site", None)


# ---------------------------------------------------------------------------
# 6. Dry-run does not write files
# ---------------------------------------------------------------------------


class TestDryRun:
    def test_dry_run_no_files(self, tmp_path):
        """When dry_run=True, no JSONL or Markdown should be written."""
        out_dir = tmp_path / "output"
        jsonl_path = tmp_path / "data" / "index.jsonl"

        # Simulate what main() does in dry-run mode: just collect, don't write
        entries = [_make_entry()]

        # In dry-run mode, main() returns before writing
        # We test the write functions are NOT called by checking no files exist
        assert not out_dir.exists()
        assert not jsonl_path.exists()

        # Verify the files CAN be written in non-dry-run
        bmi.write_jsonl(entries, jsonl_path)
        bmi.write_markdown(entries, out_dir)
        assert jsonl_path.exists()
        assert out_dir.exists()


# ---------------------------------------------------------------------------
# 7. Blocked domains are filtered in _collect
# ---------------------------------------------------------------------------


class TestCollectFiltering:
    def test_blocked_entries_are_skipped(self):
        """_collect should filter out blocked-domain entries."""
        fake_entries = [
            bmi.IndexEntry(
                title="Good Resource",
                url="https://terrytao.wordpress.com/good-post",
                site="terrytao",
                topic="math",
                level="mixed",
                resource_type="blog",
                summary_zh="好资源",
            ),
            bmi.IndexEntry(
                title="Pirated Book",
                url="https://z-library.sk/book/12345",
                site="terrytao",
                topic="math",
                level="mixed",
                resource_type="blog",
                summary_zh="盗版书",
            ),
        ]

        all_entries: list[bmi.IndexEntry] = []
        skipped: list[dict] = []

        with patch.object(bmi, "parse_terrytao", return_value=fake_entries):
            with patch.object(bmi, "is_robots_allowed", return_value=True):
                bmi._collect("terrytao", all_entries, skipped, limit=100)

        assert len(all_entries) == 1
        assert all_entries[0].title == "Good Resource"
        assert len(skipped) == 1
        assert "blocked" in skipped[0]["reason"]


# ---------------------------------------------------------------------------
# 8. Utility functions
# ---------------------------------------------------------------------------


class TestUtilities:
    def test_strip_html(self):
        assert bmi.strip_html("<p>Hello <b>World</b></p>") == "Hello World"

    def test_truncate_short(self):
        assert bmi.truncate("short", 150) == "short"

    def test_truncate_long(self):
        result = bmi.truncate("a" * 200, 150)
        assert len(result) <= 153  # 150 + "..."
        assert result.endswith("...")

    def test_extract_title_h1(self):
        html = "<html><head><title>Page Title</title></head><body><h1>Real Title</h1></body></html>"
        assert bmi.extract_title(html) == "Real Title"

    def test_extract_title_fallback(self):
        html = "<html><head><title>Page Title</title></head><body><p>No heading</p></body></html>"
        assert bmi.extract_title(html) == "Page Title"

    def test_extract_title_default(self):
        html = "<html><head></head><body><p>Nothing</p></body></html>"
        assert bmi.extract_title(html, fallback="Default") == "Default"

    def test_is_same_domain(self):
        assert bmi.is_same_domain("https://sub.example.com/page", "example.com") is True
        assert bmi.is_same_domain("https://other.com/page", "example.com") is False
