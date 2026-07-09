# Cauchy's Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/cauchypf.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PROOF OF CAUCHY’S THEOREM
KEITH CONRAD
The converse of Lagrange’s theorem is false in general: if G is a ﬁnite group and d | |G|
then G need not have a subgroup of order d. For example,|A4| = 12 and A4 has no subgroup
of order 6. The converse is true for prime d. This is due to Cauchy [1] in 1844.
Theorem. (Cauchy) Let G be a ﬁnite group and p be a prime factor of |G|. Then G
contains an element of order p. Equivalently, G contains a subgroup of order p.
The equivalence of the existence of an element of order p and a subgroup of order p is
easy: an element of order p generates a subgroup of order p, and conversely a nonidentity
element of a subgroup of order p has order p because p is prime. By the way, when p | |G|
there need not be a subgroup of index p: A4 (or An for n ≥4) has no subgroup of index 2.
Cauchy stated his theorem for permutation groups (i.e., subgroups of Sn), not abstract
ﬁnite groups, since the concept of an abstract ﬁnite group was not yet available [2].
Before treating Cauchy’s theorem, let’s prove the special case p = 2.
If |G| is even,
consider all pairs {g, g−1}, where g ̸= g−1. This accounts for an even number of elements
of G. The g that are not part of such a pair are those satisfying g = g−1, i.e., g2 = e.
So if we count |G| mod 2, we can ignore pairs {g, g−1} where g ̸= g−1 and we get |G| ≡
|{g ∈G : g2 = e}| mod 2. One solution to g2 = e is e. If it were the only solution, then
|G| ≡1 mod 2, which is false. Thus some g0 ̸= e satisﬁes g2
0 = e, and that g0 has order 2.
Now we prove Cauchy’s theorem in the general case.
Proof. We will induct on |G|.1 Let n = |G|. Since p | n, n ≥p. The base case is n = p.
When |G| = p, each nonidentity element of G has order p since p is prime. Suppose n > p,
p | n, and the theorem is true for all groups of order less than n that is divisible by p.
We treat ﬁrst abelian G (using homomorphisms) and then nonabelian G (using conjugacy
classes).
Case 1: G is abelian.
Assume no element of G has order p and we will get a contradiction.
No element has order divisible by p: if g ∈G has order r and p | r then gr/p has order p.
Let G = {g1, g2, . . . , gn} and let gi have order mi, so each mi is not divisible by p. Let m
be the least common multiple of the mi’s, so m is not divisible by p and gm
i
= e for all i.
Because G is abelian, the function f : (Z/(m))n →G given by f(a1, . . . , an) = ga1
1 · · · gan
n
is
a homomorphism:2
f(a1, . . . , an)f(b1, . . . , bn) = f(a1 + b1, . . . , an + bn).
That is,
ga1
1 · · · gan
n gb1
1 · · · gbn
n = ga1
1 gb1
1 · · · gan
n gbn
n = ga1+b1
1
· · · gan+bn
n
1Proving theorems by induction on the order of the group is a very fruitful idea in group theory.
2This function is well-deﬁned because gm
i
= e for all i, so ga+mk
i
= ga
i for any k ∈Z.
1

<!-- page 2 -->
2
KEITH CONRAD
from commutativity of the gi’s. This homomorphism is surjective (each element of G is a
gi, and if ai = 1 and other aj’s are 0 then f(a1, . . . , an) = gi), so by the ﬁrst isomorphism
theorem (Z/(m))n/ ker f ∼= G. Therefore
|G| = |(Z/(m))n|
| ker f|
=
mn
| ker f|,
so |G|| ker f| = mn. Thus |G| is a factor of mn, but p divides |G| and mn is not divisible by
p, so we have a contradiction.
Case 2: G is nonabelian.
Assume no element of G has order p and we will get a contradiction.
In every proper subgroup H of G there is no element of order p (H may be abelian or
nonabelian), so by induction no proper subgroup of G has order divisible by p. For each
proper subgroup H, |G| = |H|[G : H] and |H| is not divisible by p while |G| is divisible by
p, so p | [G : H] for every proper subgroup H of G.
Since G is nonabelian it has some conjugacy classes with size greater than 1. Let these
be represented by g1, g2, . . . , gk. Conjugacy classes in G of size 1 are the elements in Z(G).
Since the conjugacy classes in G form a partition of G, computing |G| by adding the sizes
of its conjugacy classes implies
(1)
|G| = |Z(G)| +
k
X
i=1
(size of conj. class of gi) = |Z(G)| +
k
X
i=1
[G : Z(gi)],
where Z(gi) is the centralizer of gi. (For each g ∈G, its conjugacy class in G has size
equal to [G : Z(g)].) Since the conjugacy class of each gi has size greater than 1 we have
[G : Z(gi)] > 1, so Z(gi) ̸= G for all i. Therefore p | [G : Z(gi)]. In (1), the left side is
divisible by p and each index in the sum on the right side is divisible by p, so |Z(G)| is
divisible by p. Since no proper subgroup of G has order divisible by p, Z(G) has to be all
of G. That means G is abelian, which is a contradiction.
□
Reread this proof until you see how it hangs together. For instance, notice that we did
not need the nonabelian case to treat the abelian case, and the abelian case by itself did not
require induction. Quite a few books prove Cauchy’s theorem initially just for abelian groups
before developing suitable concepts (like conjugacy classes) to prove Cauchy’s theorem for
nonabelian groups. We needed the abelian case as part of the nonabelian case since in the
inductive step of Case 2, the proper subgroups Z(gi) of the nonabelian group G might be
abelian. (All subgroups of abelian groups are abelian while subgroups of nonabelian groups
can be abelian or nonabelian, so there is an asymmetry there.)
The proof above could be reorganized to treat the two cases in the reverse order, as
follows. If a ﬁnite group G with order divisible by p has no element of order p then ﬁrst
assume G is nonabelian and run through Case 2 (assuming the theorem is proved for all
groups of smaller order, abelian and nonabelian) to get a contradiction, so G must be
abelian. Then run through Case 1 to get a contradiction if G is abelian.
References
[1] A. L. Cauchy, M´emoire sur les arrangements que l’on peut former avec des lettres donn´ees et sur les
permutations ou substitutions `a l’aide desquelles on passe d’un arrangement `a un autre, pp. 151–252
in “Exercises d’Analyse et de Physique Math´ematique, Tome 3e,” Bachelier, Paris, 1844. Online at
https://archive.org/details/ecercicesdanaly03caucrich/page/n3/mode/2up.
[2] M. Meo, The mathematical life of Cauchy’s group theorem, Historia Math. 31 (2004), 196–221.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*