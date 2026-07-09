#!/usr/bin/env python3
"""
build_public_math_index.py
--------------------------
Build a lightweight public-math-resource index (JSONL + Markdown).

Only collects:  title, URL, topic tags, short Chinese summary, source notes.
NEVER downloads copyrighted full text (PDFs, books, papers).
Respects robots.txt, sets a descriptive User-Agent, and enforces a 2-second
minimum delay between requests.

Usage:
    python scripts/build_public_math_index.py --dry-run
    python scripts/build_public_math_index.py --limit 50
    python scripts/build_public_math_index.py --output-dir corpus/public_index
    python scripts/build_public_math_index.py --sites terrytao etsu kconrad
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from datetime import date, timezone, datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

# ---------------------------------------------------------------------------
# Lazy HTTP client
# ---------------------------------------------------------------------------

_client = None  # module-level singleton


def _get_client():
    global _client
    if _client is None:
        import httpx
        _client = httpx.Client(
            headers={
                "User-Agent": (
                    "XiaoyiStatTutor/0.1 "
                    "(educational resource indexer; +https://github.com/xiaoyi-a2a-stat-tutor)"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            },
            timeout=30.0,
            follow_redirects=True,
            max_redirects=5,
        )
    return _client


def http_get(url: str, *, raise_on_error: bool = False) -> Optional[str]:
    """GET *url* respecting per-domain robots.txt crawl-delay (min 2 s)."""
    netloc = urlparse(url).netloc
    delay = get_crawl_delay(netloc) if netloc else 2.0
    delay = max(delay, 2.0)
    time.sleep(delay)
    try:
        resp = _get_client().get(url)
        if resp.status_code >= 400:
            if raise_on_error:
                resp.raise_for_status()
            print(
                f"  HTTP {resp.status_code}: {url}",
                file=sys.stderr,
            )
            return None
        text = resp.text
        # Handle UTF-16 pages that leak null bytes into text
        if "\x00" in text:
            text = text.replace("\x00", "")
        return text
    except Exception as exc:
        print(f"  fetch error: {url} ({exc})", file=sys.stderr)
        if raise_on_error:
            raise
        return None


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BLOCKED_DOMAINS: set[str] = {
    "z-library",
    "zlib",
    "sci-hub",
    "scihub",
    "libgen",
    "baidu",
    "zujuan",
    "b-ok",
    "b-ok.cc",
    "booksc",
    "bookzz",
}

SITES: dict[str, dict] = {
    "terrytao": {
        "name": "Terence Tao's Blog",
        "home": "https://terrytao.wordpress.com/",
        "domain": "terrytao.wordpress.com",
    },
    "etsu": {
        "name": "ETSU Gardner Courses",
        "home": "https://faculty.etsu.edu/gardnerr/courses.htm",
        "domain": "faculty.etsu.edu",
    },
    "kconrad": {
        "name": "Keith Conrad Expository Papers",
        "home": "https://kconrad.math.uconn.edu/",
        "domain": "kconrad.math.uconn.edu",
    },
    "arxiv": {
        "name": "arXiv Mathematics",
        "home": "https://arxiv.org/list/math/recent",
        "domain": "arxiv.org",
    },
    "mitocw": {
        "name": "MIT OpenCourseWare Mathematics",
        "home": "https://ocw.mit.edu/search/?q=mathematics&d=courses",
        "domain": "ocw.mit.edu",
    },
    "openstax": {
        "name": "OpenStax Mathematics Textbooks",
        "home": "https://openstax.org/subjects/math",
        "domain": "openstax.org",
    },
    "paulnotes": {
        "name": "Paul's Online Math Notes",
        "home": "https://tutorial.math.lamar.edu/",
        "domain": "tutorial.math.lamar.edu",
    },
    "nlab": {
        "name": "nLab",
        "home": "https://ncatlab.org/nlab/show/HomePage",
        "domain": "ncatlab.org",
    },
    "proofwiki": {
        "name": "ProofWiki",
        "home": "https://proofwiki.org/wiki/Main_Page",
        "domain": "proofwiki.org",
    },
    "euclid": {
        "name": "Project Euclid Open Access",
        "home": "https://projecteuclid.org/",
        "domain": "projecteuclid.org",
    },
    "stacks": {
        "name": "Stacks Project",
        "home": "https://stacks.math.columbia.edu/",
        "domain": "stacks.math.columbia.edu",
    },
}


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------


@dataclass
class IndexEntry:
    title: str
    url: str
    site: str
    topic: str
    level: str  # undergraduate | graduate | research | mixed
    resource_type: str  # blog | course | lecture_note | problem_set | reference | paper_metadata
    summary_zh: str
    license_status: str = "public_link_index_only"
    retrieved_at: str = field(default_factory=lambda: date.today().isoformat())
    notes: str = "仅采集公开页面元数据与链接，不下载版权内容"


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

# Pre-compiled patterns
_RE_HTML_TAG = re.compile(r"<[^>]+>")
_RE_MULTI_SPACE = re.compile(r"\s+")
_RE_TITLE_TAG = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_RE_H1_TAG = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
_RE_H2_TAG = re.compile(r"<h2[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
_RE_HREF = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)


def is_blocked_domain(url: str) -> bool:
    """Return True if *url* belongs to a blocked (piracy/unauthorised) domain."""
    url_lower = url.lower()
    return any(bd in url_lower for bd in BLOCKED_DOMAINS)


def normalize_url(url: str, base: str = "") -> str:
    """Resolve *url* against *base*, strip fragments and tracking params."""
    if base:
        url = urljoin(base, url)
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return ""
    # Remove fragment and common tracking params
    query = parsed.query
    for tracking in ("utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"):
        query = re.sub(rf"&?{tracking}=[^&]*", "", query).lstrip("&")
    return parsed._replace(fragment="", query=query).geturl()


def is_same_domain(url: str, domain: str) -> bool:
    return urlparse(url).netloc.endswith(domain)


def strip_html(text: str) -> str:
    """Remove HTML tags and collapse whitespace."""
    return _RE_MULTI_SPACE.sub(" ", _RE_HTML_TAG.sub(" ", text)).strip()


def truncate(text: str, max_chars: int = 150) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "..."


def extract_title(html_text: str, fallback: str = "") -> str:
    """Try <h1>, then <title>, then *fallback*."""
    m = _RE_H1_TAG.search(html_text)
    if m:
        t = strip_html(m.group(1))
        if t:
            return truncate(t, 200)
    m = _RE_TITLE_TAG.search(html_text)
    if m:
        t = strip_html(m.group(1))
        if t:
            return truncate(t, 200)
    return fallback


def extract_text(html_text: str, max_chars: int = 2000) -> str:
    body = strip_html(html_text)
    return body[:max_chars]


# ---------------------------------------------------------------------------
# Robots.txt
# ---------------------------------------------------------------------------

_robots_cache: dict[str, tuple[list[str], list[str], float]] = {}
# key = netloc, value = (disallow_paths, allow_paths, crawl_delay)


def fetch_robots(netloc: str) -> tuple[list[str], list[str], float]:
    """Return (disallow_paths, allow_paths, crawl_delay) for *netloc*."""
    if netloc in _robots_cache:
        return _robots_cache[netloc]

    robots_url = f"https://{netloc}/robots.txt"
    disallow: list[str] = []
    allow: list[str] = []
    crawl_delay = 2.0

    try:
        import httpx
        resp = httpx.get(robots_url, timeout=10, follow_redirects=True)
        if resp.status_code == 200:
            relevant = False
            for raw_line in resp.text.splitlines():
                line = raw_line.split("#", 1)[0].strip()
                if not line or ":" not in line:
                    continue
                key, _, val = line.partition(":")
                key = key.strip().lower()
                val = val.strip()
                if key == "user-agent":
                    relevant = val == "*" or "xiaoyi" in val.lower()
                elif relevant:
                    if key == "disallow" and val:
                        disallow.append(val)
                    elif key == "allow" and val:
                        allow.append(val)
                    elif key == "crawl-delay":
                        try:
                            crawl_delay = max(2.0, float(val))
                        except ValueError:
                            pass
    except Exception:
        pass

    result = (disallow, allow, crawl_delay)
    _robots_cache[netloc] = result
    return result


def is_robots_allowed(url: str) -> bool:
    parsed = urlparse(url)
    disallow, allow, _delay = fetch_robots(parsed.netloc)
    path = parsed.path or "/"
    # Allow rules take precedence
    for pattern in allow:
        if path.startswith(pattern):
            return True
    for pattern in disallow:
        if path.startswith(pattern):
            return False
    return True


def get_crawl_delay(netloc: str) -> float:
    _d, _a, delay = fetch_robots(netloc)
    return delay


# ---------------------------------------------------------------------------
# Site-specific parsers
# ---------------------------------------------------------------------------


def _collect(
    site_key: str,
    entries: list[IndexEntry],
    skipped: list[dict],
    limit: int,
) -> None:
    """Dispatch to the correct parser and collect results."""
    fn_map = {
        "terrytao": parse_terrytao,
        "etsu": parse_etsu,
        "kconrad": parse_kconrad,
        "arxiv": parse_arxiv,
        "mitocw": parse_mitocw,
        "openstax": parse_openstax,
        "paulnotes": parse_paulnotes,
        "nlab": parse_nlab,
        "proofwiki": parse_proofwiki,
        "euclid": parse_euclid,
        "stacks": parse_stacks,
    }
    fn = fn_map.get(site_key)
    if fn is None:
        print(f"  unknown site: {site_key}", file=sys.stderr)
        return

    site_name = SITES[site_key]["name"]
    print(f"  [{site_name}] starting ...")
    new_entries = fn(limit=limit)
    for entry in new_entries:
        if is_blocked_domain(entry.url):
            skipped.append({"url": entry.url, "reason": "blocked domain"})
            continue
        if not is_robots_allowed(entry.url):
            skipped.append({"url": entry.url, "reason": "robots.txt disallow"})
            continue
        entries.append(entry)
    print(f"  [{site_name}] collected {len(new_entries)} entries")


# ---- Terry Tao ------------------------------------------------------------


def parse_terrytao(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    sitemap_url = "https://terrytao.wordpress.com/sitemap.xml"

    xml_text = http_get(sitemap_url)
    if not xml_text:
        return entries

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        print(f"  sitemap parse error: {exc}", file=sys.stderr)
        return entries

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [loc.text for loc in root.findall(".//sm:loc", ns) if loc.text]

    # Prefer blog post pages (contain /category/) over tag/category archives
    blog_urls = [u for u in locs if "/category/" in u]
    other_urls = [u for u in locs if "/category/" not in u]
    urls = (blog_urls + other_urls)[:limit]

    domain = SITES["terrytao"]["domain"]
    for url in urls:
        if not is_same_domain(url, domain):
            continue
        html = http_get(url)
        if not html:
            continue
        title = extract_title(html, fallback=url.rsplit("/", 2)[-2] or url)
        body = extract_text(html)
        entries.append(
            IndexEntry(
                title=title,
                url=url,
                site="terrytao",
                topic="mathematics",
                level="mixed",
                resource_type="blog",
                summary_zh=truncate(
                    f"陶哲轩数学博客文章，涵盖分析学、数论、组合数学等领域。"
                    f"本页主题为{truncate(title, 60)}",
                    150,
                ),
                notes="Terence Tao 个人学术博客，公开访问",
            )
        )
    return entries


# ---- ETSU Gardner ---------------------------------------------------------


def parse_etsu(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    home = SITES["etsu"]["home"]
    domain = SITES["etsu"]["domain"]

    html = http_get(home)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    topic_map = {
        "stat": "statistics",
        "prob": "probability",
        "alg": "algebra",
        "calc": "calculus",
        "geom": "geometry",
        "analys": "analysis",
        "linear": "linear_algebra",
        "discrete": "discrete_math",
        "number": "number_theory",
    }

    seen: set[str] = set()
    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, home)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if not any(ext in url.lower() for ext in (".htm", ".html", ".php", "/")):
            continue
        seen.add(url)

        page_html = http_get(url)
        if not page_html:
            continue
        title = extract_title(page_html, fallback=Path(urlparse(url).path).stem)

        topic = "mathematics"
        url_lower = url.lower()
        for key, val in topic_map.items():
            if key in url_lower:
                topic = val
                break

        entries.append(
            IndexEntry(
                title=title,
                url=url,
                site="etsu",
                topic=topic,
                level="undergraduate",
                resource_type="course",
                summary_zh=f"ETSU 数学课程页面，由 Gardner 教授维护。主题为{truncate(title, 50)}",
                notes="ETSU 教师公开课程页面",
            )
        )
    return entries


# ---- Keith Conrad ---------------------------------------------------------


def parse_kconrad(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []

    # Keith Conrad's expository papers page
    papers_url = "https://kconrad.math.uconn.edu/blurbs/"
    domain = SITES["kconrad"]["domain"]

    html = http_get(papers_url)
    if not html:
        # Fallback: try main page
        html = http_get(SITES["kconrad"]["home"])
        if not html:
            return entries
        papers_url = SITES["kconrad"]["home"]

    links = _RE_HREF.findall(html)
    topic_map = {
        "algebra": "algebra",
        "number": "number_theory",
        "analysis": "analysis",
        "topolog": "topology",
        "prob": "probability",
        "linear": "linear_algebra",
        "group": "group_theory",
        "field": "field_theory",
        "ring": "ring_theory",
        "galois": "galois_theory",
        "p-adic": "number_theory",
        "modular": "number_theory",
    }

    seen: set[str] = set()
    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, papers_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        seen.add(url)

        title = Path(urlparse(url).path).stem.replace("_", " ").replace("-", " ")
        if not title or title in ("", "index", "blurbs"):
            continue

        topic = "mathematics"
        url_lower = url.lower()
        title_lower = title.lower()
        for key, val in topic_map.items():
            if key in url_lower or key in title_lower:
                topic = val
                break

        entries.append(
            IndexEntry(
                title=title,
                url=url,
                site="kconrad",
                topic=topic,
                level="undergraduate",
                resource_type="lecture_note",
                summary_zh=f"Keith Conrad 数学解说笔记，主题为{truncate(title, 50)}。公开教育资源。",
                notes="Keith Conrad 个人学术网站公开解说文档",
            )
        )
    return entries


# ---- arXiv ----------------------------------------------------------------


def parse_arxiv(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    categories = {
        "math.ST": ("statistics", "统计学"),
        "math.PR": ("probability", "概率论"),
        "math.CO": ("combinatorics", "组合数学"),
        "math.NT": ("number_theory", "数论"),
        "math.AG": ("algebraic_geometry", "代数几何"),
        "math.AP": ("analysis", "分析学"),
        "math.CA": ("analysis", "经典分析"),
        "math.LA": ("linear_algebra", "线性代数"),
    }

    for cat_id, (topic, topic_zh) in categories.items():
        if len(entries) >= limit:
            break
        url = f"https://arxiv.org/list/{cat_id}/recent"
        html = http_get(url)
        if not html:
            continue

        entries.append(
            IndexEntry(
                title=f"arXiv {cat_id} Recent Papers",
                url=url,
                site="arxiv",
                topic=topic,
                level="research",
                resource_type="paper_metadata",
                summary_zh=f"arXiv {cat_id} 分类最新论文列表页面（{topic_zh}）。仅采集元数据链接索引。",
                notes="arXiv 公开论文列表，仅索引不下载全文",
            )
        )

    return entries


# ---- MIT OCW ---------------------------------------------------------------


def parse_mitocw(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    search_url = "https://ocw.mit.edu/search/?q=mathematics&d=courses"
    domain = SITES["mitocw"]["domain"]

    html = http_get(search_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, search_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        # MIT OCW course URLs look like /courses/18-01-... or /courses/18.01...
        if "/courses/" not in url:
            continue
        seen.add(url)

        page_html = http_get(url)
        title = ""
        if page_html:
            title = extract_title(page_html)
        if not title:
            parts = urlparse(url).path.strip("/").split("/")
            if len(parts) >= 2:
                title = parts[-1].replace("-", " ").title()
            else:
                title = "MIT OCW Mathematics Course"

        entries.append(
            IndexEntry(
                title=title,
                url=url,
                site="mitocw",
                topic="mathematics",
                level="undergraduate",
                resource_type="course",
                summary_zh=f"MIT OpenCourseWare 数学课程。主题为{truncate(title, 50)}",
                notes="MIT OCW 开放课程，CC BY-NC-SA 许可",
            )
        )
    return entries


# ---- OpenStax --------------------------------------------------------------


def parse_openstax(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    home_url = "https://openstax.org/subjects/math"
    domain = SITES["openstax"]["domain"]

    html = http_get(home_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, home_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if "/details/books/" not in url:
            continue
        seen.add(url)

        title_match = re.search(r"/details/books/([^/?]+)", url)
        title = (title_match.group(1).replace("-", " ").title() if title_match
                 else "OpenStax Math Textbook")

        entries.append(
            IndexEntry(
                title=title,
                url=url,
                site="openstax",
                topic="mathematics",
                level="undergraduate",
                resource_type="reference",
                summary_zh=f"OpenStax 开放教材《{truncate(title, 40)}》，免费公开使用，含习题与示例。",
                notes="OpenStax 开放教育资源，CC BY 许可",
            )
        )
    return entries


# ---- Paul's Online Math Notes ----------------------------------------------


def parse_paulnotes(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    home_url = "https://tutorial.math.lamar.edu/"
    domain = SITES["paulnotes"]["domain"]

    html = http_get(home_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    topic_map = {
        "calc": "calculus",
        "algebra": "algebra",
        "de": "differential_equations",
        "diff": "differential_equations",
    }
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, home_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if url.rstrip("/") == home_url.rstrip("/"):
            continue
        if any(skip in url.lower() for skip in ("sites/", "cgi-bin/", "css", "images")):
            continue
        seen.add(url)

        title = Path(urlparse(url).path).stem.replace("_", " ").replace("-", " ").title()
        if not title:
            continue

        topic = "mathematics"
        url_lower = url.lower()
        for key, val in topic_map.items():
            if key in url_lower:
                topic = val
                break

        entries.append(
            IndexEntry(
                title=f"Paul's Notes: {title}",
                url=url,
                site="paulnotes",
                topic=topic,
                level="undergraduate",
                resource_type="lecture_note",
                summary_zh=f"Paul 在线数学笔记，主题为{truncate(title, 50)}。含详细例题与解法。",
                notes="Paul's Online Math Notes 公开教育资源",
            )
        )
    return entries


# ---- nLab ------------------------------------------------------------------


def parse_nlab(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    home_url = "https://ncatlab.org/nlab/show/HomePage"
    domain = SITES["nlab"]["domain"]

    html = http_get(home_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, home_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if "/show/" not in url:
            continue
        # Skip meta pages
        if any(skip in url for skip in ("HomePage", "AllPages", "RecentChanges", "Search", "Forum")):
            continue
        seen.add(url)

        title_match = re.search(r"/show/([^/?#]+)", url)
        title = (title_match.group(1).replace("+", " ").replace("_", " ")
                 if title_match else "nLab Article")

        entries.append(
            IndexEntry(
                title=f"nLab: {title}",
                url=url,
                site="nlab",
                topic="mathematics",
                level="graduate",
                resource_type="reference",
                summary_zh=f"nLab 数学百科条目：{truncate(title, 60)}。范畴论视角的数学参考资源。",
                notes="nLab 开放百科，CC BY-SA",
            )
        )
    return entries


# ---- ProofWiki -------------------------------------------------------------


def parse_proofwiki(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    home_url = "https://proofwiki.org/wiki/Main_Page"
    domain = SITES["proofwiki"]["domain"]

    html = http_get(home_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, home_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if "/wiki/" not in url:
            continue
        if any(skip in url for skip in (
            "Main_Page", "Special:", "Help:", "Template:",
            "Category:", "ProofWiki:", "User:", "File:",
        )):
            continue
        seen.add(url)

        title_match = re.search(r"/wiki/([^/?#]+)", url)
        title = (title_match.group(1).replace("_", " ")
                 if title_match else "ProofWiki Article")

        entries.append(
            IndexEntry(
                title=f"ProofWiki: {title}",
                url=url,
                site="proofwiki",
                topic="mathematics",
                level="undergraduate",
                resource_type="reference",
                summary_zh=f"ProofWiki 数学证明百科条目：{truncate(title, 60)}。含完整证明过程。",
                notes="ProofWiki 开放百科，CC BY-SA",
            )
        )
    return entries


# ---- Project Euclid --------------------------------------------------------


def parse_euclid(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    home_url = "https://projecteuclid.org/journals"
    domain = SITES["euclid"]["domain"]

    html = http_get(home_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, home_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if "/journals/" not in url or url.rstrip("/") == home_url.rstrip("/"):
            continue
        seen.add(url)

        title_match = re.search(r"/journals/([^/?#]+)", url)
        title = (title_match.group(1).replace("-", " ").title()
                 if title_match else "Project Euclid Journal")

        entries.append(
            IndexEntry(
                title=f"Project Euclid: {title}",
                url=url,
                site="euclid",
                topic="mathematics",
                level="research",
                resource_type="paper_metadata",
                summary_zh=f"Project Euclid 开放获取数学期刊：{truncate(title, 50)}。仅索引元数据。",
                notes="Project Euclid 开放获取期刊，部分全文开放",
            )
        )
    return entries


# ---- Stacks Project --------------------------------------------------------


def parse_stacks(limit: int = 100) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    toc_url = "https://stacks.math.columbia.edu/"
    domain = SITES["stacks"]["domain"]

    html = http_get(toc_url)
    if not html:
        return entries

    links = _RE_HREF.findall(html)
    seen: set[str] = set()

    for href in links:
        if len(entries) >= limit:
            break
        url = normalize_url(href, toc_url)
        if not url or url in seen:
            continue
        if not is_same_domain(url, domain):
            continue
        if any(skip in url.lower() for skip in ("license", "download", ".pdf", "tag", "help")):
            continue
        seen.add(url)

        title = Path(urlparse(url).path).stem.replace("-", " ").title() or "Stacks Project Chapter"

        entries.append(
            IndexEntry(
                title=f"Stacks Project: {title}",
                url=url,
                site="stacks",
                topic="algebraic_geometry",
                level="graduate",
                resource_type="reference",
                summary_zh=f"Stacks Project 代数几何参考资源：{truncate(title, 50)}。开放协作编写。",
                notes="Stacks Project 开放资源，GNU FDL / MIT 双许可",
            )
        )
    return entries


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------


def write_jsonl(entries: list[IndexEntry], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")
    print(f"wrote JSONL: {path}  ({len(entries)} entries)")


def write_markdown(entries: list[IndexEntry], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    by_site: dict[str, list[IndexEntry]] = {}
    for entry in entries:
        by_site.setdefault(entry.site, []).append(entry)

    written: list[Path] = []
    for site_key, site_entries in by_site.items():
        info = SITES.get(site_key, {"name": site_key, "home": "", "domain": ""})
        path = output_dir / f"{site_key}_index.md"

        # Group by topic
        by_topic: dict[str, list[IndexEntry]] = {}
        for e in site_entries:
            by_topic.setdefault(e.topic, []).append(e)

        lines: list[str] = []
        lines.append(f"# {info['name']} - 公开资源索引\n")
        lines.append(f"> 来源：{info['home']}  ")
        lines.append(f"> 采集时间：{date.today().isoformat()}  ")
        lines.append(f"> 条目数：{len(site_entries)}\n")
        lines.append("## 合规声明\n")
        lines.append("- 本文件仅包含公开页面的标题、URL 和自写中文短摘要")
        lines.append("- 未下载或复制任何受版权保护的全文内容")
        lines.append("- 所有链接均为公开可访问的合法来源")
        lines.append("- license_status: public_link_index_only\n")
        lines.append("## 主题分类\n")

        for topic, topic_entries in sorted(by_topic.items()):
            lines.append(f"### {topic} ({len(topic_entries)} 条)\n")
            for e in topic_entries:
                lines.append(f"- **{e.title}**")
                lines.append(f"  - URL: {e.url}")
                lines.append(f"  - 类型: {e.resource_type} | 级别: {e.level}")
                lines.append(f"  - 摘要: {e.summary_zh}")
                lines.append(f"  - 说明: {e.notes}\n")

        lines.append("## 使用建议\n")
        lines.append("本索引适合作为 RAG 知识库的补充参考来源。")
        lines.append("在回答问题时可引用这些公开资源的链接，引导用户前往原始页面深入学习。")
        lines.append("请勿将本索引中的链接用于批量下载或绕过原始站点的访问限制。\n")

        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(path)
        print(f"wrote Markdown: {path}  ({len(site_entries)} entries)")

    return written


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build public math resource index (JSONL + Markdown)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be collected without writing files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum entries per site (default: 100)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("corpus/public_index"),
        help="Output directory for Markdown files (default: corpus/public_index)",
    )
    parser.add_argument(
        "--jsonl-path",
        type=Path,
        default=Path(".data/public_math_index.jsonl"),
        help="Output path for JSONL file (default: .data/public_math_index.jsonl)",
    )
    parser.add_argument(
        "--sites",
        nargs="+",
        default=["terrytao", "etsu", "kconrad"],
        choices=sorted(SITES.keys()),
        help="Sites to crawl (default: terrytao etsu kconrad)",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Public Math Resource Index Builder")
    print("=" * 60)
    print(f"Sites:  {', '.join(args.sites)}")
    print(f"Limit:  {args.limit} per site")
    print(f"Output: {args.output_dir.resolve()}")
    print(f"JSONL:  {args.jsonl_path.resolve()}")
    print(f"Dry-run: {args.dry_run}")
    print()

    # Pre-check robots.txt for all selected sites
    print("Checking robots.txt ...")
    for site_key in args.sites:
        domain = SITES[site_key]["domain"]
        disallow, allow, delay = fetch_robots(domain)
        print(f"  {domain}: {len(disallow)} disallow rules, crawl-delay={delay}s")
    print()

    # Collect entries
    all_entries: list[IndexEntry] = []
    skipped: list[dict] = []

    for site_key in args.sites:
        _collect(site_key, all_entries, skipped, args.limit)

    # Blocked-domain post-filter (belt-and-suspenders)
    filtered: list[IndexEntry] = []
    for entry in all_entries:
        if is_blocked_domain(entry.url):
            skipped.append({"url": entry.url, "reason": "blocked domain (post-filter)"})
        else:
            filtered.append(entry)
    all_entries = filtered

    print()
    print(f"Total entries: {len(all_entries)}")
    print(f"Skipped:       {len(skipped)}")

    if args.dry_run:
        print("\n--- DRY RUN: entries that would be written ---")
        for e in all_entries[:20]:
            print(f"  [{e.site}] {e.title}")
            print(f"         {e.url}")
        if len(all_entries) > 20:
            print(f"  ... and {len(all_entries) - 20} more")
        if skipped:
            print(f"\n--- DRY RUN: {len(skipped)} entries that would be skipped ---")
            for s in skipped[:10]:
                print(f"  {s['reason']}: {s['url']}")
        print("\nDry-run complete. No files written.")
        return 0

    # Write output
    write_jsonl(all_entries, args.jsonl_path)
    written_md = write_markdown(all_entries, args.output_dir)

    print("\n" + "=" * 60)
    print("RAG integration:")
    print(f"  Add the following path to CORPUS_WHITELIST in .env:")
    print(f"  {args.output_dir.resolve()}")
    print(f"\n  Then run:")
    print(f"  python scripts/build_corpus.py --license-status public_link_index_only")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
