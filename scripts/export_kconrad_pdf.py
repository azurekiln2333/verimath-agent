#!/usr/bin/env python3
"""
Export Keith Conrad PDFs to page images + extract text.

Phase 1: PyMuPDF get_text() for fast text extraction
Phase 2: Export pages as PNG for Read-tool OCR of formula-heavy pages

Output: corpus/papers/kconrad_md/{name}.md
"""
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF required. Install: pip install pymupdf")
    sys.exit(1)

PROJECT = Path(r"E:\windows_ext\Desktop\华为智能体\xiaoyi-a2a-stat-tutor")
PAPERS_DIR = PROJECT / "corpus" / "papers" / "kconrad"
MD_DIR = PROJECT / "corpus" / "papers" / "kconrad_md"
IMG_DIR = PROJECT / "corpus" / "papers" / "kconrad_img"
MD_DIR.mkdir(parents=True, exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

# Matrix(2,2) = ~144 DPI, good balance between quality and file size
MATRIX = fitz.Matrix(2, 2)

def process_pdf(pdf_path: Path) -> tuple[str, int, list[Path]]:
    """Extract text + export images from a single PDF.

    Returns (full_text, page_count, image_paths).
    """
    doc = fitz.open(str(pdf_path))
    page_count = len(doc)
    texts = []
    image_paths = []

    # Create subdirectory for this paper's images
    paper_img_dir = IMG_DIR / pdf_path.stem
    paper_img_dir.mkdir(parents=True, exist_ok=True)

    for i, page in enumerate(doc):
        # Text extraction
        text = page.get_text("text")
        if text.strip():
            texts.append(f"<!-- page {i+1} -->\n{text.strip()}")

        # Image export (for OCR fallback)
        img_path = paper_img_dir / f"page_{i+1:03d}.png"
        if not img_path.exists():
            pix = page.get_pixmap(matrix=MATRIX)
            pix.save(str(img_path))
        image_paths.append(img_path)

    doc.close()
    return "\n\n".join(texts), page_count, image_paths


def text_to_markdown(title: str, text: str, source_url: str, topic: str) -> str:
    """Wrap extracted text into a Markdown document with metadata."""
    lines = [
        f"# {title}",
        "",
        f"> **Source**: {source_url}  ",
        f"> **Author**: Keith Conrad  ",
        f"> **Topic**: {topic}  ",
        f"> **License**: Public educational resource (link index only for original PDF)",
        "",
        "---",
        "",
        text,
        "",
        "---",
        "",
        "*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*",
    ]
    return "\n".join(lines)


# Topic inference from directory path
TOPIC_MAP = {
    "proofs": "proof_writing",
    "grouptheory": "group_theory",
    "ringtheory": "ring_theory",
    "linmultialg": "linear_algebra",
    "galoistheory": "galois_theory",
    "ugradnumthy": "number_theory",
    "gradnumthy": "number_theory",
    "analysis": "analysis",
    "topology": "topology",
}

# Title mapping (name -> human-readable title)
TITLES = {
    "writingtips": "Advice on Mathematical Writing",
    "induction": "Examples of Proofs by Induction",
    "binomcoeffintegral": "Proofs of Integrality of Binomial Coefficients",
    "welldefined": "Well-Defined Functions",
    "whygroups": "Why Groups?",
    "sign": "Sign of Permutations",
    "15puzzle": "The Fifteen Puzzle and Rubik's Cube",
    "order": "Order of Elements",
    "cyclicgp": "Subgroups of Cyclic Groups",
    "cyclicmodp": "Cyclicity of (Z/p)x",
    "coset": "Cosets and Lagrange's Theorem",
    "quotientgroups": "Quotient Groups",
    "homomorphisms": "Homomorphisms",
    "isomorphisms": "Isomorphisms",
    "gpisomlist": "Small Groups Up to Isomorphism",
    "groupsorder4and6": "Groups of Order 4 and 6",
    "group12": "Groups of Order 12",
    "groupsp2": "Groups of Order p^2",
    "groupsp3": "Groups of Order p^3",
    "genquat": "Generalized Quaternions",
    "conjclass": "Conjugation in a Group",
    "dihedral": "Dihedral Groups I",
    "dihedral2": "Dihedral Groups II",
    "cauchypf": "Cauchy's Theorem",
    "finite-abelian": "Decomposition of Finite Abelian Groups",
    "gpaction": "Group Actions",
    "transitive": "Transitive Group Actions",
    "sylowpf": "Sylow Theorems (Proof)",
    "sylowapp": "Sylow Theorems (Consequences)",
    "Ansimple": "Simplicity of An",
    "charthy": "Characters of Finite Abelian Groups",
    "semidirect-product": "Semidirect Products",
    "schurzass": "Schur-Zassenhaus Theorem",
    "maschke": "Maschke's Theorem over General Fields",
    "divthm": "Division Theorem in Z and R[T]",
    "countroots": "Counting Roots of Polynomials",
    "ideals": "Notes on Ideals",
    "euclideanrk": "Euclidean Domains",
    "noetherian-ring": "Noetherian Rings",
    "dimension": "Dimension",
    "minpolyandappns": "Minimal Polynomial",
    "semisimple": "Semisimple Operators",
    "diffeqdim": "Differential Equations and Linear Algebra",
    "linearrecursion": "Linear Recursions over All Fields",
    "matrixnorm": "The Norm of a Matrix",
    "pfister": "Pfister's Theorem on Sums of Squares",
    "moduleintro": "Introduction to Modules",
    "modulesoverPID": "Modules over a PID",
    "bilinearform": "Bilinear Forms",
    "universalmapping": "Universal Mapping Properties",
    "tensorprod": "Tensor Products I",
    "tensorprod2": "Tensor Products II",
    "extmod": "Exterior Powers",
    "symmfunction": "Symmetric Polynomials",
    "rootirred": "Roots and Irreducible Polynomials",
    "finitefields": "Finite Fields",
    "splittingfields": "Splitting Fields",
    "galoiscorr": "Galois Correspondence",
    "galoisappn": "Applications of Galois Theory",
    "cyclotomic": "Cyclotomic Extensions",
    "artinschreier": "The Artin-Schreier Theorem",
    "galoisdescent": "Galois Descent",
    "modarith": "Modular Arithmetic",
    "pythagtriple": "Pythagorean Triples",
    "fermatlittletheorem": "Fermat's Little Theorem",
    "eulerthm": "Euler's Theorem",
    "crt": "Chinese Remainder Theorem",
    "infinitudeofprimes": "The Infinitude of the Primes",
    "pelleqn1": "Pell's Equation I",
    "pelleqn2": "Pell's Equation II",
    "Zinotes": "Gaussian Integers",
    "congnumber": "Congruent Number Problem",
    "mordelleqn1": "Mordell's Equation",
    "idealfactor": "Unique Factorization of Ideals",
    "disc": "Discriminants and Ramified Primes",
    "unittheorem": "Dirichlet's Unit Theorem",
    "hensel": "Hensel's Lemma",
    "localglobal": "The Local-Global Principle",
    "fltreg": "Fermat's Last Theorem for Regular Primes",
    "kummer": "Kummer's Lemma",
    "stirling": "Stirling's Formula",
    "series": "Infinite Series",
    "gaussianintegral": "The Gaussian Integral",
    "logarctan": "The Logarithm and Arctangent",
    "irrational": "Irrationality of pi and e",
    "transcendence-e": "Transcendence of e",
    "diffunderint": "Differentiation Under the Integral Sign",
    "metricspaces": "Metric Spaces",
    "contraction": "The Contraction Mapping Theorem",
    "lpspace": "Lp Spaces for 0 < p < 1",
    "connnotpathconn": "Connected but Not Path Connected Spaces",
    "finite-dim-TVS": "Finite-Dimensional Topological Vector Spaces",
    "zorn1": "Zorn's Lemma I",
    "zorn2": "Zorn's Lemma II",
}

KC_BASE = "https://kconrad.math.uconn.edu/blurbs"


def infer_topic(pdf_path: Path) -> str:
    """Assign topic from known category mapping."""
    _MAP = {
        # Proofs
        "writingtips": "proof_writing", "induction": "proof_writing",
        "binomcoeffintegral": "proof_writing", "welldefined": "proof_writing",
        # Group Theory
        "whygroups": "group_theory", "sign": "group_theory", "15puzzle": "group_theory",
        "order": "group_theory", "cyclicgp": "group_theory", "countsubgpZpaZpb": "group_theory",
        "cyclicmodp": "group_theory", "coset": "group_theory", "quotientgroups": "group_theory",
        "homomorphisms": "group_theory", "isomorphisms": "group_theory",
        "gpisomlist": "group_theory", "A4noindex2": "group_theory",
        "groupsorder4and6": "group_theory", "group12": "group_theory",
        "groupsp2": "group_theory", "groupsp3": "group_theory", "group16": "group_theory",
        "genquat": "group_theory", "genset": "group_theory", "conjclass": "group_theory",
        "noncommutatorSL2": "group_theory", "2parametergroup": "group_theory",
        "dihedral": "group_theory", "dihedral2": "group_theory",
        "isometrycpx": "group_theory", "isometryR2": "group_theory", "isometryRn": "group_theory",
        "cauchypf": "group_theory", "cauchyapp": "group_theory",
        "finite-abelian": "group_theory", "gpaction": "group_theory",
        "transitive": "group_theory", "sylowpf": "group_theory",
        "sylowapp": "group_theory", "sylowmore": "group_theory",
        "allgrouporderncyclic": "group_theory", "Ansimple": "group_theory",
        "PSLnsimple": "group_theory", "charthy": "group_theory",
        "charthyshort": "group_theory", "semidirect-product": "group_theory",
        "subgpseries1": "group_theory", "subgpseries2": "group_theory",
        "splittinggp": "group_theory", "schurzass": "group_theory",
        "relativity": "group_theory", "maschke": "group_theory",
        "affineheisrep": "group_theory", "irrepdeg": "group_theory",
        "wordproblem": "group_theory",
        # Ring Theory
        "divthm": "ring_theory", "countroots": "ring_theory",
        "ringdefs": "ring_theory", "ideals": "ring_theory",
        "irredtestsoverQ": "ring_theory", "reducibleallp": "ring_theory",
        "irredselmerpoly": "ring_theory", "gaussnormlemma": "ring_theory",
        "euclideanrk": "ring_theory", "noetherian-ring": "ring_theory",
        "ufdapp": "ring_theory", "polynomial-properties": "ring_theory",
        "maxideal-polyring": "ring_theory", "primvector": "ring_theory",
        "algebras": "ring_theory", "quaternionalg": "ring_theory",
        # Linear / Multilinear Algebra
        "dimension": "linear_algebra", "minpolyandappns": "linear_algebra",
        "simulcomm": "linear_algebra", "potdiagonalizable": "linear_algebra",
        "semisimple": "linear_algebra", "diffeqdim": "linear_algebra",
        "linearrecursion": "linear_algebra", "matrixnorm": "linear_algebra",
        "descentPythag": "linear_algebra", "pfister": "linear_algebra",
        "hurwitzlinear": "linear_algebra", "hurwitzrepnthy": "linear_algebra",
        "sumsquareQF(T)": "linear_algebra", "moduleintro": "linear_algebra",
        "modulesoverPID": "linear_algebra", "alignedbases": "linear_algebra",
        "stablyfree": "linear_algebra", "noetherianmod": "linear_algebra",
        "dualmod": "linear_algebra", "dualspaceinfinite": "linear_algebra",
        "bilinearform": "linear_algebra", "univid": "linear_algebra",
        "univid2": "linear_algebra", "universalmapping": "linear_algebra",
        "splittingmodules": "linear_algebra", "complexification": "linear_algebra",
        "tensorprod": "linear_algebra", "tensorprod2": "linear_algebra",
        "extmod": "linear_algebra", "extmodbaseextn": "linear_algebra",
        # Galois Theory
        "symmfunction": "galois_theory", "rootirred": "galois_theory",
        "numbersoncircle": "galois_theory", "simpleradical": "galois_theory",
        "finitefields": "galois_theory", "tracenorm": "galois_theory",
        "tracenorm2": "galois_theory", "separable1": "galois_theory",
        "perfect": "galois_theory", "algclosure": "galois_theory",
        "algclosureshorter": "galois_theory", "splittingfields": "galois_theory",
        "separable2": "galois_theory", "splittingisom": "galois_theory",
        "galoiscorr": "galois_theory", "galoiscorrexamples": "galois_theory",
        "galoisappn": "galois_theory", "galoisaspermgp": "galois_theory",
        "galoiscorrthms": "galois_theory", "cubicquartic": "galois_theory",
        "cubicquarticallchar": "galois_theory", "cyclotomic": "galois_theory",
        "galoisSnAn": "galois_theory", "linearchar": "galois_theory",
        "artinschreier": "galois_theory", "galoisdescent": "galois_theory",
        # Undergraduate Number Theory
        "modarith": "number_theory", "modarithshort": "number_theory",
        "uniquefactnZF[T]": "number_theory", "analogypoly": "number_theory",
        "universaldivtest": "number_theory", "pythagtriple": "number_theory",
        "fermatlittletheorem": "number_theory", "fermattest": "number_theory",
        "eulerthm": "number_theory", "ordersmodm": "number_theory",
        "RSAnotes": "number_theory", "crt": "number_theory",
        "carmichaelkorselt": "number_theory", "minus1squaremodp": "number_theory",
        "infinitudeofprimes": "number_theory", "prime-patterns-1": "number_theory",
        "wieferich-primes": "number_theory", "squaresandinfmanyprimes": "number_theory",
        "primestopology": "number_theory", "fermat-numbers-and-factors": "number_theory",
        "perfect-numbers-mersenne": "number_theory", "lucas-lehmer-test": "number_theory",
        "solovaystrassen": "number_theory", "millerrabin": "number_theory",
        "irredtestFpT": "number_theory", "pelleqn1": "number_theory",
        "pelleqn2": "number_theory", "contfrac-neg-invert": "number_theory",
        "quadratic-integers": "number_theory", "Zinotes": "number_theory",
        "quadraticundergrad": "number_theory", "Picksumofsq": "number_theory",
        "descent": "number_theory", "descentbyeuler": "number_theory",
        "congnumber": "number_theory", "3squarearithprog": "number_theory",
        "4squarearithprog": "number_theory", "QuadraticResiduePatterns": "number_theory",
        # Graduate Number Theory
        "mordelleqn1": "number_theory", "quadraticgrad": "number_theory",
        "idealfactor": "number_theory", "dedekindf": "number_theory",
        "dedekind-index-thm": "number_theory", "disc": "number_theory",
        "totram": "number_theory", "nopowerbasis": "number_theory",
        "integersradical": "number_theory", "notfree": "number_theory",
        "classgroupKronecker": "number_theory", "classgpex": "number_theory",
        "relativeintandidealclasses": "number_theory", "SL2classno": "number_theory",
        "matrixconj": "number_theory", "unittheorem": "number_theory",
        "chevalleyunit": "number_theory", "frobeniuspf": "number_theory",
        "galois-Q-factor-mod-p": "number_theory", "dedekind-galois-res-field": "number_theory",
        "chebappn": "number_theory", "dirichleteuclid": "number_theory",
        "schurtheorem": "number_theory", "galoisselmerpoly": "number_theory",
        "different": "number_theory", "conductor": "number_theory",
        "Gauss-Jacobi-sums": "number_theory", "LfunctionGaussJacobi": "number_theory",
        "hensel": "number_theory", "multivarhensel": "number_theory",
        "equivabsvalues": "number_theory", "equivnorms": "number_theory",
        "localglobal": "number_theory", "primepowerunitsandGLnQ": "number_theory",
        "characterQ": "number_theory", "autRandQp": "number_theory",
        "infseriespadic": "number_theory", "mahlerexpansions": "number_theory",
        "strassmannapplication": "number_theory", "fltreg": "number_theory",
        "kummer": "number_theory", "carlitz": "number_theory",
        "cfthistory": "number_theory",
        # Analysis
        "stirling": "analysis", "series": "analysis",
        "gaussianintegral": "analysis", "logarctan": "analysis",
        "irrational": "analysis", "transcendence-e": "analysis",
        "diffunderint": "analysis", "metricspaces": "analysis",
        "contraction": "analysis", "contraction2": "analysis",
        "sequencespaceto0": "analysis", "lpspace": "analysis",
        "sumest": "analysis", "asymp": "analysis",
        "ordersofgrowth": "analysis", "series_acceleration": "analysis",
        "abelthm": "analysis", "TaylorRemainder": "analysis",
        "entropypost": "analysis", "arclengthIntbypartsPi": "analysis",
        # Topology
        "connnotpathconn": "topology", "finite-dim-TVS": "topology",
        # Other
        "zorn1": "algebra", "zorn2": "algebra",
        "fundthmalgcalculus": "algebra", "fundthmalglinear": "algebra",
        "propermaps": "algebra",
    }
    return _MAP.get(pdf_path.stem, "mathematics")


def main():
    pdfs = sorted(PAPERS_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in", PAPERS_DIR)
        print("Run download_kconrad_pdfs.py first.")
        sys.exit(1)

    print(f"Found {len(pdfs)} PDFs in {PAPERS_DIR}")
    print(f"Output: {MD_DIR}")
    print()

    processed = 0
    skipped = 0
    errors = []
    total_pages = 0

    for pdf_path in pdfs:
        name = pdf_path.stem
        md_path = MD_DIR / f"{name}.md"

        if md_path.exists() and md_path.stat().st_size > 100:
            print(f"  [skip] {name}.md (already exists)")
            skipped += 1
            continue

        print(f"  [{processed+1}/{len(pdfs)}] processing {name} ...", end=" ", flush=True)

        try:
            text, pages, img_paths = process_pdf(pdf_path)
            total_pages += pages

            title = TITLES.get(name, name.replace("-", " ").replace("_", " ").title())
            topic = infer_topic(pdf_path)
            source_url = f"{KC_BASE}/{name}.pdf"

            md_content = text_to_markdown(title, text, source_url, topic)
            md_path.write_text(md_content, encoding="utf-8")

            print(f"OK ({pages} pages, {len(text)} chars)")
            processed += 1
        except Exception as exc:
            print(f"ERROR: {exc}")
            errors.append((name, str(exc)))

    print(f"\n{'='*50}")
    print(f"Processed:   {processed}")
    print(f"Skipped:     {skipped}")
    print(f"Errors:      {len(errors)}")
    print(f"Total pages: {total_pages}")
    print(f"Total images: {total_pages}")
    print(f"Markdown:    {MD_DIR}")
    print(f"Images:      {IMG_DIR}")

    if errors:
        print("\nErrors:")
        for name, err in errors[:10]:
            print(f"  {name}: {err}")


if __name__ == "__main__":
    main()
