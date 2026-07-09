# Countsubgpzpazpb

> **Source**: https://kconrad.math.uconn.edu/blurbs/countsubgpZpaZpb.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
COUNTING SUBGROUPS OF Z/paZ × Z/pbZ
KEITH CONRAD
Fix a prime p. For nonnegative integers a, b, and d, we seek a formula for the number
Na,b,d of subgroups of order pd in Z/paZ × Z/pbZ:
Na,b,d = |{H ⊂Z/paZ × Z/pbZ : |H| = pd}|.
This is symmetric in a and b (Na,b,d = Nb,a,d), so when it is convenient we can limit attention
to the case a ≤b. Trivially Na,b,d = 0 if d > a + b, so we may assume 0 ≤d ≤a + b. For
1 ≤a ≤b, and a + b ≥d, we will see that
Na,b,d = 1 + p + p2 + · · · + pr,
where r = r(a, b) is a somewhat irregular function of a and b (the precise rule is given in
Theorem 3).
Throughout, we write
Ga,b = Z/paZ × Z/pbZ.
For an abelian group G, its m-torsion subgroup will be denoted G[m] = {g ∈G : gm = e}.
We will develop a recursive formula for Na,b,d that requires knowing in advance how many
cyclic subgroups there are of each size in Z/paZ × Z/pbZ. So ﬁrst we work out a formula
for the number of cyclic subgroups. Write it as
Ca,b,d = |{H ⊂Z/paZ × Z/pbZ : |H| = pd, H is cyclic}|.
Theorem 1. When 1 ≤a ≤b,
Ca,b,d =









1,
if d = 0,
pd−1 + pd,
if 1 ≤d ≤a,
pa,
if a + 1 ≤d ≤b (if a ̸= b),
0,
if b < d.
In particular, Ca,b,1 = 1 + p.
Proof. The cases d = 0 and d > b are clear. So we may assume 1 ≤d ≤b. To count
subgroups of order pd we count elements of order pd and then divide by ϕ(pd) (the number
of generators a cyclic group of order pd has). An element has order pd when it’s killed by
pd but not by pd−1, so
Ca,b,d = |Ga,b[pd]| −|Ga,b[pd−1]|
ϕ(pd)
.
How large is Ga,b[pi]? If 0 ≤i ≤a,
Ga,b[pi] = pa−iZ/paZ × pb−iZ/pbZ =⇒size is p2i.
If a ≤i ≤b,
Ga,b[pi] = Z/paZ × pb−iZ/pbZ =⇒size is pa+i.
If i > b,
Ga,b[pi] = Z/paZ × Z/pbZ =⇒size is pa+b.
1

<!-- page 2 -->
2
KEITH CONRAD
Putting this all together,
|Ga,b[pi]| =





p2i,
if 0 ≤i ≤a,
pa+i,
if a ≤i ≤b,
pa+b,
if i ≥b.
(The overlapping cases are consistent at i = a and i = b.)
Now we feed the above formula for |Ga,b[pi]| at i = d and i = d −1 into the formula for
Ca,b,d. If 1 ≤d ≤a,
Ca,b,d = p2d −p2(d−1)
pd−1(p −1) = p2d−2(p2 −1)
pd−1(p −1) = pd−1(p + 1) = pd−1 + pd.
If a < b and a + 1 ≤d ≤b,
Ca,b,d = pa+d −pa+d−1
pd−1(p −1)
= pa+d−1(p −1)
pd−1(p −1)
= pa.
□
Theorem 2. For 1 ≤a ≤b, we have
Na,b,0 = 1
and
Na,b,1 = Ca,b,1 = 1 + p.
If d ≥2 then
Na,b,d = Ca,b,d + Na−1,b−1,d−2.
Proof. A group of order p is cyclic, so
Na,b,1 = Ca,b,1 = 1 + p.
Now take d ≥2. We can distinguish cyclic from noncyclic subgroups of Ga,b using p-torsion.
The p-torsion in Ga,b is
Ga,b[p] = pa−1Z/paZ × pb−1Z/pbZ,
which has order p2, so
Ga.b/Ga,b[p] ∼= Z/pa−1Z × Z/pb−1Z ∼= Ga−1,b−1.
For a nontrivial subgroup H ⊂Ga,b, if H is cyclic then H[p] has order p, while if H is
noncyclic then H ∼= Z/pjZ × Z/pkZ for some positive integers j and k, so H[p] has order
p2. Since H[p] ⊂Ga,b[p] and Ga,b[p] has order p2, H[p] = Ga,b[p]. So
H not cyclic =⇒Ga,b[p] ⊂H ⊂Ga,b.
The converse is true as well, since Ga,b[p] ∼= (Z/pZ)2 contains more than one subgroup of
order p, so it can’t lie inside a cyclic group. So for 2 ≤d ≤a + b,
|{H ⊂Ga,b : |H| = pd, H not cyclic}|
=
|{H ⊂Ga,b/Ga,b[p] : |H| = pd−2}|
=
Na−1,b−1,d−2,
which leads to a recursive formula: Na,b,d is the number of cyclic subgroups of Ga,b with
order pd (which is Ca,b,d) plus the number of noncyclic subgroups of Ga,b with order pd
(which we just showed is Na−1,b−1,d−2 if d ≥2).
□

<!-- page 3 -->
COUNTING SUBGROUPS OF Z/paZ × Z/pbZ
3
Using Theorems 1 and 2 (and sometimes the equation Na,b,d = Na,b,a+b−d, which follows
from duality theory for ﬁnite abelian groups), the following formulas for Na,b,d are found
when 1 ≤a ≤b and 1 ≤d ≤5:
Na,b,1 = 1 + p,
Na,b,2 =





1,
if a = b = 1,
1 + p,
if a = 1, b ≥2,
1 + p + p2,
if a ≥2,
Na,b,3 =









1,
if a = 1, b = 2,
1 + p,
if a = 1, b ≥3; a = 2, b = 2,
1 + p + p2,
if a = 2, b ≥3,
1 + p + p2 + p3,
if a ≥3,
Na,b,4 =















1,
if a = 1, b = 3; a = 2, b = 2,
1 + p,
if a = 1, b ≥4; a = 2, b = 3,
1 + p + p2,
if a = 2, b ≥4; a = 3, b = 3,
1 + p + p2 + p3,
if a = 3, b ≥4,
1 + p + p2 + p3 + p4,
if a ≥4,
and
Na,b,5 =



















1,
if a = 1, b = 4; a = 2, b = 3,
1 + p,
if a = 1, b ≥5; a = 2, b = 4; a = 3, b = 3,
1 + p + p2,
if a = 2, b ≥5; a = 3, b = 4,
1 + p + p2 + p3,
if a = 3, b ≥5; a = 4, b = 4,
1 + p + p2 + p3 + p4,
if a = 4, b ≥5,
1 + p + p2 + p3 + p4 + p5,
if a ≥5.
Examine these according to the constraints on a and b for each formula for Na,b,d. The
pattern of cases where inequalities on b appear is obvious: a = 1, b ≥d, then a = 2, b ≥d,
then a = 3, b ≥d, and so on as a increases up to d −1. The remaining cases where a
and b both have speciﬁed values are organized according to increasing values of a + b for
1 ≤a ≤b ≤d −1. We are led to the following general theorem.
Theorem 3. If 1 ≤a ≤b, then
Na,b,d =









1 + p + · · · + pd,
if 0 ≤d ≤a,
1 + p + · · · + pa,
if a ≤d ≤b,
1 + p + · · · + pa+b−d,
if b ≤d ≤a + b,
0,
if a + b < d.
Proof. Use induction on b.
□
Example 4. When a = b,
Na,a,d =
(
1 + p + · · · + pd,
if 0 ≤d ≤a,
1 + p + · · · + p2a−d,
if a ≤d ≤2a.

<!-- page 4 -->
4
KEITH CONRAD
Theorem 3 says that as d increases from 0 to a+b, Na,b,d starts out as 1, 1+p, 1+p+p2, . . . ,
increasing by the next power of p each time until reaching 1 + p + · · · + pa at d = a. Then
Na,b,d stays at this value until d reaches b, after which the highest power of p is removed for
each successive value of d until Na,b,d reaches Na,b,a+b = 1.
Corollary 5. Suppose 1 ≤a ≤b.
1. If 1 ≤d ≤a then Na,b,d = Na,b,d−1 + pd.
2. If a < d ≤b then Na,b,d = Na,b,d−1.
3. If b < d ≤a + b then Na,b,d = Na,b,d−1 −pa+b−d+1.
In particular, Na,b,d ≡Na,b,d−1 mod pd if 1 ≤d ≤b but not necessarily if b < d ≤a + b.
Proof. From the description of how Na,b,d rises, plateaus, and then falls, this is obvious.
□
For each a, b, and d, observe that Na,b,d has the same formula for all p. So Na,b,d can be
described by a “universal” formula for all primes. More generally, if A is a ﬁnite abelian
p-group that is a product of cyclic groups of orders pe1, . . . , per (ei > 0), then the number
of subgroups of A with a particular order pd is a universal polynomial function of p (same
formula for all p) that is determined by d and the exponents ei. Even more generally, the
number of subgroups H of A such that H and A/H have speciﬁed cyclic decompositions is
given by a universal polynomial in p that is determined by the sizes of the cyclic components
of H, A/H, and A; these universal polynomials in p are called Hall polynomials. There is
also a formula, due to Delsarte, for the number of subgroups of A with a given isomorphism
type. See [1] and [2].
We can formulate Theorem 3 in terms of counting subgroups with a particular index
rather than a particular order.
Theorem 6. If 1 ≤a ≤b, let Ia,b,m be the number of subgroups of Z/paZ × Z/pbZ with
index pm. Then for 0 ≤m ≤a + b,
Ia,b,m =





1 + p + · · · + pm,
if 0 ≤m ≤a,
1 + p + · · · + pa,
if a ≤m ≤b,
1 + p + · · · + pa+b−m,
if b ≤m ≤a + b.
Proof. For 0 ≤m ≤a + b, a subgroup of Z/paZ × Z/pbZ has index pm if and only if it has
order pa+b−m, so Ia,b,m = Na,b,a+b−m. Now use the formulas in Theorem 3.
□
Corollary 7. For a ≥1 and m ≥0, the number of subgroups of Z/paZ × Z with index pm
is
(
1 + p + · · · + pm,
if 0 ≤m ≤a,
1 + p + · · · + pa,
if a ≤m.
Proof. If H ⊂Z/paZ × Z has index pm then for each M ≥m, we have {0} × pMZ ⊂H,
so the number of subgroups of Z/paZ × Z with index pm is the number of subgroups of
Z/paZ × Z/pMZ with index pm when M ≥m. Taking M large enough that also M ≥a,
the ﬁrst two formulas in Theorem 6 with b = M gives the desired counts.
□
References
[1] G. Constantine and R. S. Kulkarni, “On a result of S. Delsarte,” Proc. Amer. Math. Soc. 92 (1984),
149–152.
[2] S. Delsarte, “Fonctions de M¨obius sur les groupes ab´eliens ﬁnis,” Annals of Math. 49 (1948), 600–609.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*