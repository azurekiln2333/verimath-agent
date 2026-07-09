#!/usr/bin/env python3
"""Download Keith Conrad's expository PDF papers with rate limiting."""
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    import httpx
except ImportError:
    print("httpx is required. Install with: pip install httpx")
    sys.exit(1)

PROJECT = Path(r"E:\windows_ext\Desktop\华为智能体\xiaoyi-a2a-stat-tutor")
PAPERS_DIR = PROJECT / "corpus" / "papers" / "kconrad"
PAPERS_DIR.mkdir(parents=True, exist_ok=True)

KC_BASE = "https://kconrad.math.uconn.edu/blurbs"

# All 96 papers from browser extraction
PAPERS = [
    ("proofs/writingtips.pdf", "writingtips"),
    ("proofs/induction.pdf", "induction"),
    ("proofs/binomcoeffintegral.pdf", "binomcoeffintegral"),
    ("proofs/welldefined.pdf", "welldefined"),
    ("grouptheory/whygroups.pdf", "whygroups"),
    ("grouptheory/sign.pdf", "sign"),
    ("grouptheory/15puzzle.pdf", "15puzzle"),
    ("grouptheory/order.pdf", "order"),
    ("grouptheory/cyclicgp.pdf", "cyclicgp"),
    ("grouptheory/countsubgpZpaZpb.pdf", "countsubgpZpaZpb"),
    ("grouptheory/cyclicmodp.pdf", "cyclicmodp"),
    ("grouptheory/coset.pdf", "coset"),
    ("grouptheory/quotientgroups.pdf", "quotientgroups"),
    ("grouptheory/homomorphisms.pdf", "homomorphisms"),
    ("grouptheory/isomorphisms.pdf", "isomorphisms"),
    ("grouptheory/gpisomlist.pdf", "gpisomlist"),
    ("grouptheory/A4noindex2.pdf", "A4noindex2"),
    ("grouptheory/groupsorder4and6.pdf", "groupsorder4and6"),
    ("grouptheory/group12.pdf", "group12"),
    ("grouptheory/groupsp2.pdf", "groupsp2"),
    ("grouptheory/groupsp3.pdf", "groupsp3"),
    ("grouptheory/group16.pdf", "group16"),
    ("grouptheory/genquat.pdf", "genquat"),
    ("grouptheory/genset.pdf", "genset"),
    ("grouptheory/conjclass.pdf", "conjclass"),
    ("grouptheory/noncommutatorSL2.pdf", "noncommutatorSL2"),
    ("grouptheory/2parametergroup.pdf", "2parametergroup"),
    ("grouptheory/dihedral.pdf", "dihedral"),
    ("grouptheory/dihedral2.pdf", "dihedral2"),
    ("grouptheory/isometrycpx.pdf", "isometrycpx"),
    ("grouptheory/isometryR2.pdf", "isometryR2"),
    ("grouptheory/isometryRn.pdf", "isometryRn"),
    ("grouptheory/cauchypf.pdf", "cauchypf"),
    ("grouptheory/cauchyapp.pdf", "cauchyapp"),
    ("grouptheory/finite-abelian.pdf", "finite-abelian"),
    ("grouptheory/gpaction.pdf", "gpaction"),
    ("grouptheory/transitive.pdf", "transitive"),
    ("grouptheory/sylowpf.pdf", "sylowpf"),
    ("grouptheory/sylowapp.pdf", "sylowapp"),
    ("grouptheory/sylowmore.pdf", "sylowmore"),
    ("grouptheory/allgrouporderncyclic.pdf", "allgrouporderncyclic"),
    ("grouptheory/Ansimple.pdf", "Ansimple"),
    ("grouptheory/PSLnsimple.pdf", "PSLnsimple"),
    ("grouptheory/charthy.pdf", "charthy"),
    ("grouptheory/charthyshort.pdf", "charthyshort"),
    ("grouptheory/semidirect-product.pdf", "semidirect-product"),
    ("grouptheory/subgpseries1.pdf", "subgpseries1"),
    ("grouptheory/subgpseries2.pdf", "subgpseries2"),
    ("grouptheory/splittinggp.pdf", "splittinggp"),
    ("grouptheory/schurzass.pdf", "schurzass"),
    ("grouptheory/relativity.pdf", "relativity"),
    ("grouptheory/maschke.pdf", "maschke"),
    ("grouptheory/affineheisrep.pdf", "affineheisrep"),
    ("grouptheory/irrepdeg.pdf", "irrepdeg"),
    ("grouptheory/wordproblem.pdf", "wordproblem"),
    ("ringtheory/divthm.pdf", "divthm"),
    ("ringtheory/countroots.pdf", "countroots"),
    ("ringtheory/ringdefs.pdf", "ringdefs"),
    ("ringtheory/ideals.pdf", "ideals"),
    ("ringtheory/irredtestsoverQ.pdf", "irredtestsoverQ"),
    ("ringtheory/reducibleallp.pdf", "reducibleallp"),
    ("ringtheory/irredselmerpoly.pdf", "irredselmerpoly"),
    ("ringtheory/gaussnormlemma.pdf", "gaussnormlemma"),
    ("ringtheory/euclideanrk.pdf", "euclideanrk"),
    ("ringtheory/noetherian-ring.pdf", "noetherian-ring"),
    ("ringtheory/ufdapp.pdf", "ufdapp"),
    ("ringtheory/polynomial-properties.pdf", "polynomial-properties"),
    ("ringtheory/maxideal-polyring.pdf", "maxideal-polyring"),
    ("ringtheory/primvector.pdf", "primvector"),
    ("ringtheory/algebras.pdf", "algebras"),
    ("ringtheory/quaternionalg.pdf", "quaternionalg"),
    ("linmultialg/dimension.pdf", "dimension"),
    ("linmultialg/minpolyandappns.pdf", "minpolyandappns"),
    ("linmultialg/simulcomm.pdf", "simulcomm"),
    ("linmultialg/potdiagonalizable.pdf", "potdiagonalizable"),
    ("linmultialg/semisimple.pdf", "semisimple"),
    ("linmultialg/diffeqdim.pdf", "diffeqdim"),
    ("linmultialg/linearrecursion.pdf", "linearrecursion"),
    ("linmultialg/matrixnorm.pdf", "matrixnorm"),
    ("linmultialg/descentPythag.pdf", "descentPythag"),
    ("linmultialg/pfister.pdf", "pfister"),
    ("linmultialg/moduleintro.pdf", "moduleintro"),
    ("linmultialg/modulesoverPID.pdf", "modulesoverPID"),
    ("linmultialg/bilinearform.pdf", "bilinearform"),
    ("linmultialg/universalmapping.pdf", "universalmapping"),
    ("linmultialg/tensorprod.pdf", "tensorprod"),
    ("linmultialg/tensorprod2.pdf", "tensorprod2"),
    ("linmultialg/extmod.pdf", "extmod"),
    ("galoistheory/symmfunction.pdf", "symmfunction"),
    ("galoistheory/rootirred.pdf", "rootirred"),
    ("galoistheory/finitefields.pdf", "finitefields"),
    ("galoistheory/splittingfields.pdf", "splittingfields"),
    ("galoistheory/galoiscorr.pdf", "galoiscorr"),
    ("galoistheory/galoisappn.pdf", "galoisappn"),
    ("galoistheory/cyclotomic.pdf", "cyclotomic"),
    ("galoistheory/artinschreier.pdf", "artinschreier"),
    ("galoistheory/galoisdescent.pdf", "galoisdescent"),
    ("ugradnumthy/modarith.pdf", "modarith"),
    ("ugradnumthy/pythagtriple.pdf", "pythagtriple"),
    ("ugradnumthy/fermatlittletheorem.pdf", "fermatlittletheorem"),
    ("ugradnumthy/eulerthm.pdf", "eulerthm"),
    ("ugradnumthy/crt.pdf", "crt"),
    ("ugradnumthy/infinitudeofprimes.pdf", "infinitudeofprimes"),
    ("ugradnumthy/pelleqn1.pdf", "pelleqn1"),
    ("ugradnumthy/pelleqn2.pdf", "pelleqn2"),
    ("ugradnumthy/Zinotes.pdf", "Zinotes"),
    ("ugradnumthy/congnumber.pdf", "congnumber"),
    ("gradnumthy/mordelleqn1.pdf", "mordelleqn1"),
    ("gradnumthy/idealfactor.pdf", "idealfactor"),
    ("gradnumthy/disc.pdf", "disc"),
    ("gradnumthy/unittheorem.pdf", "unittheorem"),
    ("gradnumthy/hensel.pdf", "hensel"),
    ("gradnumthy/localglobal.pdf", "localglobal"),
    ("gradnumthy/fltreg.pdf", "fltreg"),
    ("gradnumthy/kummer.pdf", "kummer"),
    ("analysis/stirling.pdf", "stirling"),
    ("analysis/series.pdf", "series"),
    ("analysis/gaussianintegral.pdf", "gaussianintegral"),
    ("analysis/logarctan.pdf", "logarctan"),
    ("analysis/irrational.pdf", "irrational"),
    ("analysis/transcendence-e.pdf", "transcendence-e"),
    ("analysis/diffunderint.pdf", "diffunderint"),
    ("analysis/metricspaces.pdf", "metricspaces"),
    ("analysis/contraction.pdf", "contraction"),
    ("analysis/lpspace.pdf", "lpspace"),
    ("topology/connnotpathconn.pdf", "connnotpathconn"),
    ("topology/finite-dim-TVS.pdf", "finite-dim-TVS"),
    ("zorn1.pdf", "zorn1"),
    ("zorn2.pdf", "zorn2"),
]

DELAY = 2.5  # seconds between requests (kconrad has no explicit crawl-delay)
client = httpx.Client(
    headers={"User-Agent": "XiaoyiStatTutor/0.1 (educational resource indexer)"},
    timeout=60.0,
    follow_redirects=True,
)

downloaded = 0
skipped = 0
errors = []

for rel_path, name in PAPERS:
    pdf_path = PAPERS_DIR / f"{name}.pdf"
    if pdf_path.exists() and pdf_path.stat().st_size > 0:
        print(f"  [skip] {name}.pdf (already exists)")
        skipped += 1
        continue

    url = f"{KC_BASE}/{rel_path}"
    print(f"  [{downloaded+1}/{len(PAPERS)}] downloading {name}.pdf ...", end=" ", flush=True)

    try:
        time.sleep(DELAY)
        resp = client.get(url)
        if resp.status_code == 200 and len(resp.content) > 100:
            pdf_path.write_bytes(resp.content)
            size_kb = len(resp.content) / 1024
            print(f"OK ({size_kb:.0f} KB)")
            downloaded += 1
        else:
            print(f"FAIL (HTTP {resp.status_code}, {len(resp.content)} bytes)")
            errors.append((name, f"HTTP {resp.status_code}"))
    except Exception as exc:
        print(f"ERROR: {exc}")
        errors.append((name, str(exc)))

print(f"\n{'='*50}")
print(f"Downloaded: {downloaded}")
print(f"Skipped:    {skipped}")
print(f"Errors:     {len(errors)}")
if errors:
    for name, err in errors[:10]:
        print(f"  {name}: {err}")
print(f"Location:   {PAPERS_DIR}")
