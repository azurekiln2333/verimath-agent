#!/usr/bin/env python3
"""OCR Keith Conrad page images to clean Markdown.

Usage:
    python scripts/ocr_kconrad_images.py [--limit N]

Requires: paddleocr, paddlepaddle, pillow

Install:
    pip install paddlepaddle paddleocr pillow
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "corpus" / "papers" / "kconrad_img"
MD_DIR = ROOT / "corpus" / "papers" / "kconrad_md"


def load_ocr_engine():
    """Lazy-load PaddleOCR to avoid slow import when not needed."""
    try:
        from paddleocr import PaddleOCR
    except ImportError:
        print("ERROR: paddleocr not installed.", file=sys.stderr)
        print("Run: pip install paddlepaddle paddleocr pillow", file=sys.stderr)
        sys.exit(1)

    # use_gpu=False for CPU-only; set True if you have CUDA
    ocr = PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False, show_log=False)
    return ocr


def ocr_page(ocr, img_path: Path) -> str:
    """OCR a single image and return text lines."""
    result = ocr.ocr(str(img_path), cls=True)
    if not result or not result[0]:
        return ""
    lines = []
    for line_data in result[0]:
        # line_data = [bbox, (text, confidence)]
        text = line_data[1][0]
        lines.append(text)
    return "\n".join(lines)


def process_paper(ocr, paper_name: str) -> str:
    """OCR all pages of a paper and return Markdown."""
    paper_img_dir = IMG_DIR / paper_name
    if not paper_img_dir.is_dir():
        return ""

    page_files = sorted(paper_img_dir.glob("page_*.png"))
    if not page_files:
        return ""

    md_parts = []
    for img_path in page_files:
        page_num = int(img_path.stem.split("_")[1])
        print(f"    OCR page {page_num}...", end="", flush=True)
        text = ocr_page(ocr, img_path)
        md_parts.append(f"<!-- page {page_num} -->\n{text}")
        print(f" {len(text)} chars")

    return "\n\n".join(md_parts)


# --- Title and topic metadata (same as export_kconrad_pdf.py) ---

def infer_topic(paper_name: str) -> str:
    TOPIC_MAP = {
        "irrational": "analysis", "euler_formula": "complex_analysis",
        "stirling": "analysis", "gamma": "analysis", "zeta": "analysis",
        "fourier": "analysis", "laplace": "analysis",
        "crt": "number_theory", "euler_phi": "number_theory",
        "fermat_little": "number_theory", "quadratic_residue": "number_theory",
        "legendre": "number_theory", "gauss_sum": "number_theory",
        "primality": "number_theory", "factoring": "number_theory",
        "pell": "number_theory", "continued_frac": "number_theory",
        "coset": "abstract_algebra", "sylow": "abstract_algebra",
        "lagrange": "abstract_algebra", "cauchy": "abstract_algebra",
        "isomorphism": "abstract_algebra", "homomorphism": "abstract_algebra",
        "galois": "galois_theory", "galois_theory": "galois_theory",
        "splitting_field": "galois_theory", "normal_ext": "galois_theory",
        "separable": "galois_theory", "discriminant": "algebra",
        "resultant": "algebra", "cyclotomic": "number_theory",
        "matrix": "linear_algebra", "determinant": "linear_algebra",
        "eigenvalue": "linear_algebra", "eigenvector": "linear_algebra",
        "diagonal": "linear_algebra", "jordan": "linear_algebra",
        "inner_product": "linear_algebra", "orthogonal": "linear_algebra",
        "quadratic_form": "linear_algebra", "bilinear": "linear_algebra",
        "topology": "topology", "compact": "topology", "connected": "topology",
        "metric": "topology", "continuity": "topology", "limit": "analysis",
        "sequence": "analysis", "series": "analysis", "convergence": "analysis",
        "uniform": "analysis", "integral": "analysis", "derivative": "analysis",
        "mean_value": "analysis", "taylor": "analysis", "power_series": "analysis",
        "ring": "abstract_algebra", "ideal": "abstract_algebra",
        "polynomial": "algebra", "field": "abstract_algebra",
        "group": "abstract_algebra", "permutation": "abstract_algebra",
        "symmetric_group": "abstract_algebra", "alternating": "abstract_algebra",
        "abelian": "abstract_algebra", "cyclic": "abstract_algebra",
        "p_group": "abstract_algebra", "solvable": "abstract_algebra",
        "nilpotent": "abstract_algebra", "free_group": "abstract_algebra",
        "presentation": "abstract_algebra",
        "prime": "number_theory", "divisibility": "number_theory",
        "gcd": "number_theory", "modular": "number_theory",
        "congruence": "number_theory", "order": "number_theory",
        "primitive_root": "number_theory", "log": "number_theory",
        "hash": "number_theory", "rsa": "cryptography",
        "elliptic": "number_theory", "p_adic": "number_theory",
        "valuation": "number_theory", "local_field": "number_theory",
        "algebraic_integer": "number_theory", "dedekind": "number_theory",
        "class_number": "number_theory", "dirichlet": "number_theory",
        "l_function": "number_theory", "riemann": "analysis",
        "category": "category_theory", "functor": "category_theory",
        "natural_trans": "category_theory", "limit_colimit": "category_theory",
        "adjoint": "category_theory",
        "set": "set_theory", "cardinality": "set_theory",
        "ordinal": "set_theory", "axiom_choice": "set_theory",
        "zorn": "set_theory", "well_order": "set_theory",
    }
    for key, topic in TOPIC_MAP.items():
        if key in paper_name.lower():
            return topic
    return "mathematics"


def main():
    parser = argparse.ArgumentParser(description="OCR Keith Conrad images to Markdown")
    parser.add_argument("--limit", type=int, default=0, help="Max papers to process (0 = all)")
    parser.add_argument("--paper", type=str, default="", help="Process only this paper name")
    args = parser.parse_args()

    if not IMG_DIR.is_dir():
        print(f"ERROR: Image directory not found: {IMG_DIR}", file=sys.stderr)
        sys.exit(1)

    MD_DIR.mkdir(parents=True, exist_ok=True)

    # Discover papers
    papers = sorted([d.name for d in IMG_DIR.iterdir() if d.is_dir()])
    if args.paper:
        papers = [p for p in papers if p == args.paper]
    if args.limit > 0:
        papers = papers[: args.limit]

    print(f"Found {len(papers)} papers to OCR")
    if not papers:
        return

    ocr = load_ocr_engine()
    print("PaddleOCR engine loaded")

    success = 0
    failed = []
    for i, paper_name in enumerate(papers, 1):
        print(f"\n[{i}/{len(papers)}] {paper_name}")
        t0 = time.time()
        try:
            md_text = process_paper(ocr, paper_name)
            if not md_text:
                print(f"  SKIP: no images found")
                continue

            # Build Markdown header
            topic = infer_topic(paper_name)
            title = paper_name.replace("_", " ").title()
            header = f"""# {title}

> **Source**: https://kconrad.math.uconn.edu/blurbs/{paper_name}.pdf
> **Author**: Keith Conrad
> **Topic**: {topic}
> **License**: Public educational resource (link index only for original PDF)

---

"""
            md_path = MD_DIR / f"{paper_name}.md"
            md_path.write_text(header + md_text, encoding="utf-8")
            elapsed = time.time() - t0
            print(f"  OK: {md_path} ({elapsed:.1f}s)")
            success += 1

        except Exception as e:
            print(f"  FAIL: {e}", file=sys.stderr)
            failed.append(paper_name)

    print(f"\n=== Done: {success} OK, {len(failed)} failed ===")
    if failed:
        print("Failed papers:", ", ".join(failed))


if __name__ == "__main__":
    main()
