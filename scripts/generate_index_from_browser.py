#!/usr/bin/env python3
"""Generate JSONL + Markdown index files from browser-extracted data."""
import json
import sys
from datetime import date
from pathlib import Path

TODAY = date.today().isoformat()
PROJECT = Path(r"E:\windows_ext\Desktop\华为智能体\xiaoyi-a2a-stat-tutor")
OUT_DIR = PROJECT / "corpus" / "public_index"
JSONL_PATH = PROJECT / ".data" / "public_math_index.jsonl"

def entry(title, url, site, topic, level, resource_type, summary_zh, notes=""):
    return {
        "title": title,
        "url": url,
        "site": site,
        "topic": topic,
        "level": level,
        "resource_type": resource_type,
        "summary_zh": summary_zh,
        "license_status": "public_link_index_only",
        "retrieved_at": TODAY,
        "notes": notes or "仅采集公开页面元数据与链接，不下载版权内容",
    }

# ── Terry Tao ──────────────────────────────────────────────
terrytao_entries = [
    entry(
        "What's new — Terence Tao 数学博客",
        "https://terrytao.wordpress.com/",
        "terrytao", "mathematics", "mixed", "blog",
        "陶哲轩个人学术博客，涵盖分析学、数论、组合数学、PDE等领域的前沿研究和解说。",
        "Terence Tao 个人学术博客，公开访问",
    ),
    entry(
        "A digestion of unit distance constructions",
        "https://terrytao.wordpress.com/2026/07/03/a-digestion-of-unit-distance-constructions/",
        "terrytao", "combinatorics", "graduate", "blog",
        "陶哲轩解说 Erdos 单位距离问题，涉及 OpenAI 和 Mythos 的新构造，使用 Golod-Shafarevich 塔等代数数论工具。",
    ),
    entry(
        "Spending symmetry (书籍)",
        "https://terrytao.wordpress.com/books/spending-symmetry/",
        "terrytao", "mathematics", "mixed", "reference",
        "陶哲轩著作《Spending Symmetry》介绍页，讨论对称性在数学中的应用。",
    ),
    entry(
        "Analysis I (书籍)",
        "https://terrytao.wordpress.com/books/analysis-i/",
        "terrytao", "analysis", "undergraduate", "reference",
        "陶哲轩教材《Analysis I》介绍页，实分析入门经典教材。",
    ),
    entry(
        "Career advice",
        "https://terrytao.wordpress.com/career-advice/",
        "terrytao", "mathematics", "mixed", "blog",
        "陶哲轩关于数学职业发展的建议合集，对研究生和本科生有参考价值。",
    ),
    entry(
        "On writing (数学写作)",
        "https://terrytao.wordpress.com/on-writing/",
        "terrytao", "mathematics", "mixed", "blog",
        "陶哲轩关于数学论文写作和表达的建议，含 LaTeX 排版和论证技巧。",
    ),
]

# ── ETSU Gardner Courses ────────────────────────────────────
ETSU_BASE = "https://faculty.etsu.edu/gardnerr"
etsu_raw = [
    ("Differential Equations", "Differential-Equations/sillab-fall26.htm", "differential_equations", "undergraduate"),
    ("Analysis 1", "4217/sillab-fall26.htm", "analysis", "graduate"),
    ("Graph Theory 1", "5340/sillab-fall26.htm", "graph_theory", "graduate"),
    ("syllabus archive", "courses-archive.htm", "mathematics", "mixed"),
    ("Course Notes on the ETSU Server", "courses-E.htm", "mathematics", "mixed"),
    ("Additional class notes", "notes-in-prep.htm", "mathematics", "mixed"),
    ("Real Analysis Part 1", "5210/notes1-G.htm", "analysis", "graduate"),
    ("Real Analysis Part 2", "5210/notes2-G.htm", "analysis", "graduate"),
    ("Real Analysis Part 3", "5210/notes3-G.htm", "analysis", "graduate"),
    ("Complex Analysis Core", "5510/notes-G.htm", "analysis", "graduate"),
    ("Complex Analysis Additional", "5510/notes2-G.htm", "analysis", "graduate"),
    ("Functional Analysis", "Func/notes-G.htm", "analysis", "graduate"),
    ("Groups (Abstract Algebra)", "5410/notes-groups-G.htm", "algebra", "graduate"),
    ("Rings and Modules", "5410/notes-rings-G.htm", "algebra", "graduate"),
    ("Fields (Algebra)", "5410/notes-fields-G.htm", "algebra", "graduate"),
    ("Theory of Matrices", "5090/notes-G.htm", "linear_algebra", "graduate"),
    ("Differential Geometry", "5310/notes-G.htm", "geometry", "graduate"),
    ("Graph Theory Notes (Bondy-Murty)", "5340/notes-Bondy-Murty-GT-G.htm", "graph_theory", "graduate"),
    ("Graph Theory 2", "5340/notes2-Bondy-Murty-GT-G.htm", "graph_theory", "graduate"),
    ("Mathematical Modeling Using Graph Theory", "5340/notes-Math-Modeling-GT-G.htm", "graph_theory", "graduate"),
    ("Algebraic Graph Theory", "5340/notes-Godsil-Royle-AlgebraicGT-G.htm", "graph_theory", "graduate"),
    ("General Topology", "5357/notes-G.htm", "topology", "graduate"),
    ("Algebraic Topology", "5357/notes2-G.htm", "topology", "graduate"),
    ("Analysis 1+ (Undergraduate)", "4217/notes-G.htm", "analysis", "undergraduate"),
    ("Analysis 2 (Undergraduate)", "4217/notes2-G.htm", "analysis", "undergraduate"),
    ("Complex Variables", "5337/notes-G.htm", "analysis", "undergraduate"),
    ("Complex Variables Applications", "5337/notes2-G.htm", "analysis", "undergraduate"),
    ("Abstract Algebra Part 1 (Undergrad)", "4127/notes-G.htm", "algebra", "undergraduate"),
    ("Abstract Algebra Part 2 (Undergrad)", "4127/notes2-G.htm", "algebra", "undergraduate"),
    ("Introduction to Knot Theory", "Knot-Theory/Notes-Livingston-G.htm", "topology", "undergraduate"),
    ("Introduction to Graph Theory", "5347/notes-Hartsfield-Ringel-G.htm", "graph_theory", "undergraduate"),
    ("Design Theory", "Design-Theory/Notes-Design-Theory-LR2-G.htm", "combinatorics", "undergraduate"),
    ("Geometry and History", "Geometry/Geometry-History-notes-G.htm", "geometry", "undergraduate"),
    ("Axiomatic Method", "Geometry/Geometry-notes-Wylie-G.htm", "geometry", "undergraduate"),
    ("Transformational Geometry", "Geometry/Geometry-notes-G.htm", "geometry", "undergraduate"),
    ("Projective Geometry", "Geometry/Projective-Geometry-notes-Wylie-G.htm", "geometry", "undergraduate"),
    ("Applied Mechanics 1 (Statics)", "2610/notes-G.htm", "applied_math", "undergraduate"),
    ("Genetics and Math Biology", "notes-bio-G.htm", "applied_math", "undergraduate"),
    ("Differential Equations 2", "Differential-Equations/DE-Boyce-DiPrima5-notes-G.htm", "differential_equations", "undergraduate"),
    ("Applied Hilbert Spaces", "Func/notes-Debnath-Mikusinski1-G.htm", "analysis", "graduate"),
    ("Ordinary Differential Equations (Applied)", "Differential-Equations/DE-Waltman-notes-G.htm", "differential_equations", "undergraduate"),
    ("Partial Differential Equations", "5610/PDE-Strauss-notes-G.htm", "differential_equations", "graduate"),
    ("Calculus 1", "1910/notes-14-G.htm", "calculus", "undergraduate"),
    ("Calculus 2", "1920/12/notes12-G.htm", "calculus", "undergraduate"),
    ("Calculus 3", "2110/notes-G.htm", "calculus", "undergraduate"),
    ("Linear Algebra", "2010/notes-G.htm", "linear_algebra", "undergraduate"),
    ("Differential Equations (Ross)", "Differential-Equations/DE-Ross4-notes-G.htm", "differential_equations", "undergraduate"),
    ("Mathematical Reasoning", "3000/Math-Reasoning-Gerstein-G.htm", "mathematics", "undergraduate"),
    ("Elementary Number Theory", "3120/Number-Theory-notes-G.htm", "number_theory", "undergraduate"),
    ("History of Math before 1600", "3040/notes-Eves6-G.htm", "history", "undergraduate"),
    ("History of Math after 1600", "3040/notes2-Eves6-G.htm", "history", "undergraduate"),
    ("Probability and Statistics", "1530/notes-G.htm", "statistics", "undergraduate"),
    ("Mathematical Statistics 1", "4047/notes-Hogg-McKean-Craig-G.htm", "statistics", "undergraduate"),
    ("Mathematical Statistics 2", "4047/notes-Hogg-McKean-Craig2-G.htm", "statistics", "graduate"),
    ("Astronomy", "Astronomy/Astro-Snow3-notes-G.htm", "applied_math", "undergraduate"),
    ("Precalculus 1 (Algebra)", "1710/notes-Precalculus-Sullivan10-G.htm", "calculus", "undergraduate"),
    ("Precalculus 2 (Trigonometry)", "1720/notes-G.htm", "calculus", "undergraduate"),
    ("Foundations and Structure of Math 1", "5025/notes-5025-G.htm", "mathematics", "undergraduate"),
]
etsu_entries = []
for title, path, topic, level in etsu_raw:
    etsu_entries.append(entry(
        title,
        f"{ETSU_BASE}/{path}",
        "etsu", topic, level, "course",
        f"ETSU Bob Gardner 教授数学课程笔记：{title}。公开免费访问，定期更新勘误。",
        "ETSU 教师公开课程页面，免费访问",
    ))

# ── Keith Conrad Expository Papers ──────────────────────────
KC_BASE = "https://kconrad.math.uconn.edu/blurbs"
kc_papers = [
    # Proofs
    ("Advice on mathematical writing", "proofs/writingtips.pdf", "proof_writing"),
    ("Examples of proofs by induction", "proofs/induction.pdf", "proof_writing"),
    ("Proofs of integrality of binomial coefficients", "proofs/binomcoeffintegral.pdf", "proof_writing"),
    ("Well-defined functions", "proofs/welldefined.pdf", "proof_writing"),
    # Group Theory
    ("Why groups?", "grouptheory/whygroups.pdf", "group_theory"),
    ("Sign of permutations", "grouptheory/sign.pdf", "group_theory"),
    ("The Fifteen puzzle (and Rubik's cube)", "grouptheory/15puzzle.pdf", "group_theory"),
    ("Order of elements", "grouptheory/order.pdf", "group_theory"),
    ("Subgroups of cyclic groups", "grouptheory/cyclicgp.pdf", "group_theory"),
    ("Cyclicity of (Z/p)x", "grouptheory/cyclicmodp.pdf", "group_theory"),
    ("Cosets and Lagrange's theorem", "grouptheory/coset.pdf", "group_theory"),
    ("Quotient groups", "grouptheory/quotientgroups.pdf", "group_theory"),
    ("Homomorphisms", "grouptheory/homomorphisms.pdf", "group_theory"),
    ("Isomorphisms", "grouptheory/isomorphisms.pdf", "group_theory"),
    ("Small groups up to isomorphism", "grouptheory/gpisomlist.pdf", "group_theory"),
    ("Groups of order 4 and 6", "grouptheory/groupsorder4and6.pdf", "group_theory"),
    ("Groups of order 12", "grouptheory/group12.pdf", "group_theory"),
    ("Groups of order p^2", "grouptheory/groupsp2.pdf", "group_theory"),
    ("Groups of order p^3", "grouptheory/groupsp3.pdf", "group_theory"),
    ("Generalized quaternions", "grouptheory/genquat.pdf", "group_theory"),
    ("Conjugation in a group", "grouptheory/conjclass.pdf", "group_theory"),
    ("Dihedral groups I", "grouptheory/dihedral.pdf", "group_theory"),
    ("Dihedral groups II", "grouptheory/dihedral2.pdf", "group_theory"),
    ("Cauchy's theorem (Proof)", "grouptheory/cauchypf.pdf", "group_theory"),
    ("Decomposition of finite abelian groups", "grouptheory/finite-abelian.pdf", "group_theory"),
    ("Group actions", "grouptheory/gpaction.pdf", "group_theory"),
    ("Transitive group actions", "grouptheory/transitive.pdf", "group_theory"),
    ("Sylow theorems (Proof)", "grouptheory/sylowpf.pdf", "group_theory"),
    ("Simplicity of An", "grouptheory/Ansimple.pdf", "group_theory"),
    ("Characters of finite abelian groups", "grouptheory/charthy.pdf", "group_theory"),
    ("Semidirect Products", "grouptheory/semidirect-product.pdf", "group_theory"),
    ("Schur-Zassenhaus theorem", "grouptheory/schurzass.pdf", "group_theory"),
    ("Maschke's theorem over general fields", "grouptheory/maschke.pdf", "group_theory"),
    # Ring Theory
    ("Division theorem in Z and R[T]", "ringtheory/divthm.pdf", "ring_theory"),
    ("Counting roots of polynomials", "ringtheory/countroots.pdf", "ring_theory"),
    ("Notes on ideals", "ringtheory/ideals.pdf", "ring_theory"),
    ("Euclidean domains", "ringtheory/euclideanrk.pdf", "ring_theory"),
    ("Noetherian rings", "ringtheory/noetherian-ring.pdf", "ring_theory"),
    # Linear / Multilinear Algebra
    ("Dimension", "linmultialg/dimension.pdf", "linear_algebra"),
    ("Minimal polynomial", "linmultialg/minpolyandappns.pdf", "linear_algebra"),
    ("Semisimple operators", "linmultialg/semisimple.pdf", "linear_algebra"),
    ("Differential equations and linear algebra", "linmultialg/diffeqdim.pdf", "linear_algebra"),
    ("Linear recursions over all fields", "linmultialg/linearrecursion.pdf", "linear_algebra"),
    ("The norm of a matrix", "linmultialg/matrixnorm.pdf", "linear_algebra"),
    ("Pfister's theorem on sums of squares", "linmultialg/pfister.pdf", "linear_algebra"),
    ("Introduction to modules", "linmultialg/moduleintro.pdf", "linear_algebra"),
    ("Modules over a PID", "linmultialg/modulesoverPID.pdf", "linear_algebra"),
    ("Bilinear forms", "linmultialg/bilinearform.pdf", "linear_algebra"),
    ("Universal mapping properties", "linmultialg/universalmapping.pdf", "linear_algebra"),
    ("Tensor products I", "linmultialg/tensorprod.pdf", "linear_algebra"),
    ("Tensor products II", "linmultialg/tensorprod2.pdf", "linear_algebra"),
    ("Exterior powers", "linmultialg/extmod.pdf", "linear_algebra"),
    # Galois Theory
    ("Symmetric polynomials", "galoistheory/symmfunction.pdf", "galois_theory"),
    ("Roots and irreducible polynomials", "galoistheory/rootirred.pdf", "galois_theory"),
    ("Finite fields", "galoistheory/finitefields.pdf", "galois_theory"),
    ("Splitting fields", "galoistheory/splittingfields.pdf", "galois_theory"),
    ("Galois correspondence", "galoistheory/galoiscorr.pdf", "galois_theory"),
    ("Applications of Galois theory", "galoistheory/galoisappn.pdf", "galois_theory"),
    ("Cyclotomic extensions", "galoistheory/cyclotomic.pdf", "galois_theory"),
    ("The Artin-Schreier theorem", "galoistheory/artinschreier.pdf", "galois_theory"),
    ("Galois descent", "galoistheory/galoisdescent.pdf", "galois_theory"),
    # Undergraduate Number Theory
    ("Modular arithmetic", "ugradnumthy/modarith.pdf", "number_theory"),
    ("Pythagorean triples", "ugradnumthy/pythagtriple.pdf", "number_theory"),
    ("Fermat's little theorem", "ugradnumthy/fermatlittletheorem.pdf", "number_theory"),
    ("Euler's theorem", "ugradnumthy/eulerthm.pdf", "number_theory"),
    ("Chinese remainder theorem", "ugradnumthy/crt.pdf", "number_theory"),
    ("Carmichael numbers and Korselt's criterion", "ugradnumthy/carmichaelkorselt.pdf", "number_theory"),
    ("The infinitude of the primes", "ugradnumthy/infinitudeofprimes.pdf", "number_theory"),
    ("Patterns in primes", "ugradnumthy/prime-patterns-1.pdf", "number_theory"),
    ("Pell's equation I", "ugradnumthy/pelleqn1.pdf", "number_theory"),
    ("Pell's equation II", "ugradnumthy/pelleqn2.pdf", "number_theory"),
    ("Gaussian integers", "ugradnumthy/Zinotes.pdf", "number_theory"),
    ("Quadratic integers", "ugradnumthy/quadratic-integers.pdf", "number_theory"),
    ("Congruent number problem", "ugradnumthy/congnumber.pdf", "number_theory"),
    # Graduate Number Theory
    ("Mordell's equation", "gradnumthy/mordelleqn1.pdf", "number_theory"),
    ("Unique factorization of ideals", "gradnumthy/idealfactor.pdf", "number_theory"),
    ("Discriminants and ramified primes", "gradnumthy/disc.pdf", "number_theory"),
    ("Dirichlet's unit theorem", "gradnumthy/unittheorem.pdf", "number_theory"),
    ("Hensel's lemma", "gradnumthy/hensel.pdf", "number_theory"),
    ("The local-global principle", "gradnumthy/localglobal.pdf", "number_theory"),
    ("Fermat's last theorem for regular primes", "gradnumthy/fltreg.pdf", "number_theory"),
    ("Kummer's lemma", "gradnumthy/kummer.pdf", "number_theory"),
    # Analysis
    ("Stirling's formula", "analysis/stirling.pdf", "analysis"),
    ("Infinite series", "analysis/series.pdf", "analysis"),
    ("The Gaussian integral", "analysis/gaussianintegral.pdf", "analysis"),
    ("The logarithm and arctangent", "analysis/logarctan.pdf", "analysis"),
    ("Irrationality of pi and e", "analysis/irrational.pdf", "analysis"),
    ("Transcendence of e", "analysis/transcendence-e.pdf", "analysis"),
    ("Differentiation under the integral sign", "analysis/diffunderint.pdf", "analysis"),
    ("Metric spaces", "analysis/metricspaces.pdf", "analysis"),
    ("The contraction mapping theorem", "analysis/contraction.pdf", "analysis"),
    ("Lp spaces for 0 < p < 1", "analysis/lpspace.pdf", "analysis"),
    # Topology
    ("Spaces connected but not path connected", "topology/connnotpathconn.pdf", "topology"),
    ("Finite-dimensional topological vector spaces", "topology/finite-dim-TVS.pdf", "topology"),
    # Zorn's lemma
    ("Zorn's lemma (I)", "zorn1.pdf", "algebra"),
    ("Zorn's lemma (II)", "zorn2.pdf", "algebra"),
]

kc_entries = []
for title, path, topic in kc_papers:
    level = "graduate" if path.startswith("gradnumthy") else "undergraduate"
    kc_entries.append(entry(
        title,
        f"{KC_BASE}/{path}",
        "kconrad", topic, level, "lecture_note",
        f"Keith Conrad 数学解说论文：{title}。以清晰严谨著称的本科/研究生数学补充材料。",
        "Keith Conrad 个人学术网站公开解说文档",
    ))

# ── Compile and write ──────────────────────────────────────
all_entries = terrytao_entries + etsu_entries + kc_entries

# Blocked domain safety check
BLOCKED = ["z-library", "zlib", "sci-hub", "scihub", "libgen", "baidu", "zujuan", "b-ok", "booksc", "bookzz"]
safe = [e for e in all_entries if not any(b in e["url"].lower() for b in BLOCKED)]
blocked = [e for e in all_entries if any(b in e["url"].lower() for b in BLOCKED)]

print(f"Total entries: {len(safe)}")
print(f"Blocked: {len(blocked)}")
for b in blocked:
    print(f"  BLOCKED: {b['url']}")

# Write JSONL
JSONL_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(JSONL_PATH, "w", encoding="utf-8") as f:
    for e in safe:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(f"Wrote JSONL: {JSONL_PATH}")

# Write Markdown per site
SITES_INFO = {
    "terrytao": ("Terence Tao's Blog", "https://terrytao.wordpress.com/"),
    "etsu": ("ETSU Gardner Courses", "https://faculty.etsu.edu/gardnerr/courses.htm"),
    "kconrad": ("Keith Conrad Expository Papers", "https://kconrad.math.uconn.edu/"),
}

OUT_DIR.mkdir(parents=True, exist_ok=True)
by_site = {}
for e in safe:
    by_site.setdefault(e["site"], []).append(e)

for site_key, site_entries in by_site.items():
    name, home = SITES_INFO[site_key]
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
            lines.append(f"  - 说明: {e['notes']}\n")

    lines.append("## 使用建议\n")
    lines.append("本索引适合作为 RAG 知识库的补充参考来源。")
    lines.append("在回答问题时可引用这些公开资源的链接，引导用户前往原始页面深入学习。")
    lines.append("请勿将本索引中的链接用于批量下载或绕过原始站点的访问限制。\n")

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote Markdown: {path} ({len(site_entries)} entries)")

print("\nDone!")
