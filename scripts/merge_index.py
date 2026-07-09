#!/usr/bin/env python3
"""Merge browser-extracted + network-crawled index data into unified output."""
import json
import shutil
from datetime import date
from pathlib import Path

PROJECT = Path(r"E:\windows_ext\Desktop\华为智能体\xiaoyi-a2a-stat-tutor")
OUT_DIR = PROJECT / "corpus" / "public_index"
NEW_DIR = PROJECT / "corpus" / "public_index_new"
JSONL_PATH = PROJECT / ".data" / "public_math_index.jsonl"
NEW_JSONL = PROJECT / ".data" / "public_math_index_new.jsonl"

TODAY = date.today().isoformat()
SITES_INFO = {
    "terrytao": ("Terence Tao's Blog", "https://terrytao.wordpress.com/"),
    "etsu": ("ETSU Gardner Courses", "https://faculty.etsu.edu/gardnerr/courses.htm"),
    "kconrad": ("Keith Conrad Expository Papers", "https://kconrad.math.uconn.edu/"),
    "arxiv": ("arXiv Mathematics", "https://arxiv.org/list/math/recent"),
    "mitocw": ("MIT OpenCourseWare Mathematics", "https://ocw.mit.edu/"),
    "openstax": ("OpenStax Mathematics Textbooks", "https://openstax.org/subjects/math"),
    "paulnotes": ("Paul's Online Math Notes", "https://tutorial.math.lamar.edu/"),
    "nlab": ("nLab", "https://ncatlab.org/nlab/show/HomePage"),
    "proofwiki": ("ProofWiki", "https://proofwiki.org/wiki/Main_Page"),
    "euclid": ("Project Euclid Open Access", "https://projecteuclid.org/"),
    "stacks": ("Stacks Project", "https://stacks.math.columbia.edu/"),
}

# Load existing JSONL (browser data)
all_entries = []
if JSONL_PATH.exists():
    for line in JSONL_PATH.read_text(encoding="utf-8").strip().split("\n"):
        if line.strip():
            all_entries.append(json.loads(line))
    print(f"Loaded {len(all_entries)} existing entries from {JSONL_PATH.name}")

# Load new JSONL (network crawl)
if NEW_JSONL.exists():
    new_count = 0
    seen_urls = {e["url"] for e in all_entries}
    for line in NEW_JSONL.read_text(encoding="utf-8").strip().split("\n"):
        if line.strip():
            obj = json.loads(line)
            if obj["url"] not in seen_urls:
                all_entries.append(obj)
                seen_urls.add(obj["url"])
                new_count += 1
    print(f"Added {new_count} new entries from {NEW_JSONL.name}")

# Write merged JSONL
with open(JSONL_PATH, "w", encoding="utf-8") as f:
    for e in all_entries:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(f"Merged JSONL: {JSONL_PATH} ({len(all_entries)} total entries)")

# Copy new Markdown files to main output dir
OUT_DIR.mkdir(parents=True, exist_ok=True)
if NEW_DIR.exists():
    for md in NEW_DIR.glob("*.md"):
        dest = OUT_DIR / md.name
        shutil.copy2(md, dest)
        print(f"Copied {md.name} -> {dest}")

# Regenerate all Markdown from merged JSONL (ensures consistency)
by_site = {}
for e in all_entries:
    by_site.setdefault(e["site"], []).append(e)

for site_key, site_entries in by_site.items():
    name, home = SITES_INFO.get(site_key, (site_key, ""))
    path = OUT_DIR / f"{site_key}_index.md"
    by_topic = {}
    for e in site_entries:
        by_topic.setdefault(e["topic"], []).append(e)

    lines = []
    lines.append(f"# {name} - 公开资源索引\n")
    lines.append(f"> 来源：{home}  ")
    lines.append(f"> 采集时间：{TODAY}  ")
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
            lines.append(f"- **{e['title']}**")
            lines.append(f"  - URL: {e['url']}")
            lines.append(f"  - 类型: {e['resource_type']} | 级别: {e['level']}")
            lines.append(f"  - 摘要: {e['summary_zh']}")
            lines.append(f"  - 说明: {e.get('notes', '')}\n")

    lines.append("## 使用建议\n")
    lines.append("本索引适合作为 RAG 知识库的补充参考来源。")
    lines.append("在回答问题时可引用这些公开资源的链接，引导用户前往原始页面深入学习。")
    lines.append("请勿将本索引中的链接用于批量下载或绕过原始站点的访问限制。\n")

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Regenerated: {path.name} ({len(site_entries)} entries)")

# Cleanup temp dir
if NEW_DIR.exists():
    shutil.rmtree(NEW_DIR)
    print(f"Cleaned up {NEW_DIR}")
if NEW_JSONL.exists():
    NEW_JSONL.unlink()
    print(f"Cleaned up {NEW_JSONL}")

print(f"\nDone! Total: {len(all_entries)} entries across {len(by_site)} sites.")
