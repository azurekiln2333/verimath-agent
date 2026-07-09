# Charthyshort

> **Source**: https://kconrad.math.uconn.edu/blurbs/charthyshort.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
KEITH CONRAD
1. Introduction
The theme we will study is an analogue on ﬁnite abelian groups of Fourier analysis on
R. A Fourier series on the real line is the following type of series in sines and cosines:
f(x) =
X
n≥0
an cos(nx) +
X
n≥1
bn sin(nx).
This is 2π-periodic. Since einx = cos(nx) + i sin(nx) and e−inx = cos(nx) −i sin(nx), a
Fourier series can also be written in terms of complex exponentials:
f(x) =
X
n∈Z
cneinx,
where c0 = a0, cn =
1
2(an −bni) for n > 0, and cn =
1
2(a|n| + b|n|i) for n < 0.
The
convenient algebraic property of einx, not shared by sines and cosines, is that it is a group
homomorphism from R to the unit circle S1 = {z ∈C : |z| = 1}:
ein(x+x′) = einxeinx′.
We now replace R with a ﬁnite abelian group. Here is the analogue of the functions einx.
Deﬁnition 1.1. A character of a ﬁnite abelian group G is a homomorphism χ: G →S1.
We will usually write abstract groups multiplicatively, so χ(g1g2) = χ(g1)χ(g2) and
χ(1) = 1.
Example 1.2. The trivial character of G is the homomorphism 1G deﬁned by 1G(g) = 1
for all g ∈G.
Example 1.3. Let G be cyclic of order 4 with generator γ. Since γ4 = 1, a character χ of
G has χ(γ)4 = 1, so χ takes only four possible values at γ, namely 1, −1, i, or −i. Once
χ(γ) is known, the value of χ elsewhere is determined by multiplicativity: χ(γj) = χ(γ)j.
So we get four characters, whose values can be placed in a table. See Table 1.
1
γ
γ2
γ3
1G
1
1
1
1
χ1
1
−1
1
−1
χ2
1
i
−1
−i
χ3
1
−i
−1
i
Table 1.
1

<!-- page 2 -->
2
KEITH CONRAD
When G has size n and g ∈G, for all characters χ of G we have χ(g)n = χ(gn) = χ(1) = 1,
so the values of χ lie among the nth roots of unity in S1. More precisely, the order of χ(g)
divides the order of g (which divides |G|).
Characters on ﬁnite abelian groups were ﬁrst studied in number theory, which is a source
of many interesting ﬁnite abelian groups. For instance, Dirichlet used characters of the group
(Z/(m))× to prove that when (a, m) = 1 there are inﬁnitely many primes p ≡a mod m. The
quadratic reciprocity law of elementary number theory is concerned with a deep property
of a particular character, the Legendre symbol. Fourier series on ﬁnite abelian groups have
applications in engineering: signal processing (the fast Fourier transform [1, Chap. 9]) and
error-correcting codes [1, Chap. 11].
To provide a context against which our development of characters on ﬁnite abelian groups
can be compared, Section 2 discusses classical Fourier analysis on the real line. In Section
3 we discuss some properties of characters of ﬁnite abelian groups and introduce their dual
groups. Section 4 uses characters of a ﬁnite abelian group to develop a ﬁnite analogue of
Fourier series. In Section 5 we use characters to prove a structure theorem for ﬁnite abelian
groups. In Section 6 we use characters to count solutions to a congruence mod p.
Our notation is completely standard, but we make two remarks about it. For a complex-
valued function f(x), the complex-conjugate function is usually denoted f(x) instead of
f(x) to stress that conjugation creates a new function. (We sometimes use the overline
notation also to mean the reduction g into a quotient group.) For n ≥1, we write µn for
the group of nth roots of unity in the unit circle S1. It is a cyclic group of size n.
Exercises.
1. Make a character table for Z/(2) × Z/(2), with columns labeled by elements of the
group and rows labeled by characters, as in Table 1.
2. Let G be a ﬁnite nonabelian simple group. (Examples include An for n ≥5.) Show
the only group homomorphism χ: G →S1 is the trivial map.
2. Classical Fourier analysis
This section serves as motivation for our later treatment of ﬁnite abelian groups, where
there will be no convergence issues (just ﬁnite sums!), so we take a soft approach and
sidestep analytic technicalities that a serious treatment of Fourier analysis on R demands.
Fourier analysis for periodic functions on R is based on the functions einx for n ∈Z.
Every “reasonably nice” function f : R →C of period 2π can be expanded into a series
f(x) =
X
n∈Z
cneinx,
where the sum runs over Z and the nth Fourier coeﬃcient cn can be recovered as an integral:
(2.1)
cn = 1
2π
Z 2π
0
f(x)e−inx dx.
This formula for cn can be explained by replacing f(x) in (2.1) by its Fourier series and in-
tegrating termwise (for “reasonably nice” functions this termwise integration is analytically
justiﬁable), using the formula
1
2π
Z 2π
0
eimxe−inx dx =
(
1,
if m = n,
0,
if m ̸= n.

<!-- page 3 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
3
Rather than working with functions f : R →C having period 2π, formulas look cleaner
using functions f : R →C having period 1. The basic exponentials become e2πinx and the
Fourier series and coeﬃcients for f are
(2.2)
f(x) =
X
n∈Z
cne2πinx,
cn =
Z 1
0
f(x)e−2πinx dx.
Note cn in (2.2) is not the same as cn in (2.1).
In addition to Fourier series there are Fourier integrals.
The Fourier transform of a
function f that decays rapidly at ±∞is the function bf : R →C deﬁned by the integral
formula
bf(y) =
Z
R
f(x)e−2πixy dx.
The analogue of the expansion (2.2) of a periodic function into a Fourier series is the Fourier
inversion formula, which expresses f in terms of its Fourier transform bf:
f(x) =
Z
R
bf(y)e2πixy dy.
Example 2.1. A Gaussian is a function of the form ae−bx2, where b > 0. For example, the
Gaussian (1/
√
2π)e−(1/2)x2 is important in probability theory. The Fourier transform of a
Gaussian is another Gaussian:
(2.3)
Z
R
ae−bx2e−2πixy dx =
rπ
b ae−π2y2/b.
This formula shows that a highly peaked Gaussian (large b) has a Fourier transform that is
a spread out Gaussian (small π2/b) and vice versa. More generally, there is a sense in which
a function and its Fourier transform can’t both be highly localized; this is a mathematical
incarnation of Heisenberg’s uncertainty principle from physics.1
There are several conventions for where 2π appears in the Fourier transform. Table 2
collects three diﬀerent 2π-conventions. The ﬁrst column of Table 2 is a deﬁnition and the
second column is a theorem (Fourier inversion).
bf(y)
f(x)
R
R f(x)e−2πixy dx
R
R bf(y)e2πixy dy
R
R f(x)e−ixy dx
1
2π
R
R bf(y)eixy dy
1
√
2π
R
R f(x)e−ixy dx
1
√
2π
R
R bf(y)eixy dy
Table 2.
A link between Fourier series and Fourier integrals is the Poisson summation formula:
for a “nice” function f : R →C that decays rapidly enough at ±∞,
(2.4)
X
n∈Z
f(n) =
X
n∈Z
bf(n),
1Heisenberg discovered his uncertainty principle in 1926 and published it in 1927, but Norbert Wiener
lectured on a purely mathematical version of this idea in 1925 [4, pp. 106–108].

<!-- page 4 -->
4
KEITH CONRAD
where bf(y) =
R
R f(x)e−2πixy dx. For example, when f(x) = e−bx2 (with b > 0), the Poisson
summation formula says
X
n∈Z
e−bn2 =
X
n∈Z
rπ
b e−π2n2/b,
To prove the Poisson summation formula, we use Fourier series. Periodize f(x) as
F(x) =
X
n∈Z
f(x + n).
Since F(x + 1) = F(x), write F as a Fourier series: F(x) = P
n∈Z cne2πinx. Then
cn =
Z 1
0
F(x)e−2πinx dx
=
Z 1
0
 X
m∈Z
f(x + m)
!
e−2πinx dx
=
X
m∈Z
Z 1
0
f(x + m)e−2πinx dx
=
X
m∈Z
Z m+1
m
f(x)e−2πinx dx
=
Z
R
f(x)e−2πinx dx
= bf(n).
Therefore the expansion of F(x) into a Fourier series is equivalent to
(2.5)
X
n∈Z
f(x + n) =
X
n∈Z
bf(n)e2πinx,
which becomes the Poisson summation formula (2.4) by setting x = 0.
Exercises.
1. Without dwelling on analytic subtleties, check from Fourier inversion that bbf(x) =
f(−x) (if the Fourier transform is deﬁned suitably).
2. For a function f : R →C and c ∈R, let g(x) = f(x + c). Deﬁne the Fourier
transform of a function h by bh(y) =
R
R h(x)e−2πixy dx. If f has a Fourier transform,
show g has Fourier transform bg(y) = e2πicy bf(y).
3. Assuming the Fourier inversion formula holds for a deﬁnition of the Fourier trans-
form as in Table 2, check that for all α and β in R× that if we set
(Ff)(y) = α
Z
R
f(x)e−iβxy dx
for all x then
f(x) =
β
2πα
Z
R
(Ff)(y)eiβxy dy.
(If β = 2πα2 then these two equations are symmetric in the roles of f and Ff except
for a sign in the exponential term.)

<!-- page 5 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
5
3. Finite Abelian Group Characters
We leave the real line and turn to the setting of ﬁnite abelian groups G. Our interest shifts
from the functions einx to characters: homomorphisms from G →S1. The construction of
characters of these groups begins with the case of cyclic groups.
Theorem 3.1. Let G be a ﬁnite cyclic group of size n with a chosen generator γ. There
are exactly n characters of G, each determined by sending γ to the diﬀerent nth roots of
unity in C.
Proof. We mimic Example 1.3, where G is cyclic of size 4. Since γ generates G, a character
is determined by its value on γ and that value must be an nth root of unity (not necessarily
of exact order n, e.g., 1G(γ) = 1), so there are at most n characters. We now write down
n characters.
Let ζ be an nth root of unity in C. Set χ(γj) = ζj for j ∈Z. This formula is well-deﬁned
(if γj = γk for two diﬀerent integer exponents j and k, we have j ≡k mod n so ζj = ζk),
and χ is a homomorphism.
Of course χ depends on ζ.
As ζ changes, we get diﬀerent
characters (their values at γ are changing), so in total we have n characters.
□
To handle characters of non-cyclic groups, the following lemma is critical.
Lemma 3.2. Let G be a ﬁnite abelian group, H ⊂G a proper subgroup, and χ: H →S1 a
character of H. For g ∈G −H, there is an extension of χ to a character on ⟨H, g⟩.
Proof. We want to extend χ to a character eχ of ⟨H, g⟩.
What is a possible value for eχ(g)? Since g ̸∈H, eχ(g) is not initially deﬁned. But some
nonzero power of g is in H (e.g., g|G| = 1 ∈H), and on these powers χ is deﬁned. Pick
d ≥1 minimal with gd ∈H. That is, d is the order of g in G/H, so d = [⟨H, g⟩: H]. If
there is a character eχ on ⟨, H, g that extends χ on H then eχ(g) must be an d-th root of
χ(gd) since we must have eχ(g)d = eχ(gd) = χ(gd). That is our clue: deﬁne eχ(g) ∈S1 to be
a solution to zd = χ(gd):
(3.1)
eχ(g)d = χ(gd).
Once we have chosen eχ(g) to satisfy (3.1), deﬁne eχ on ⟨H, g⟩by
(3.2)
eχ(hgi) := χ(h)eχ(g)i.
This formula covers all possible elements of ⟨H, g⟩, but is eχ well-deﬁned? Perhaps H and
⟨g⟩overlap nontrivially, so the expression of an element of ⟨H, g⟩in the form hgi is not
unique. We have to show this doesn’t lead to an inconsistency in the value of eχ in (3.2).
Suppose hgi = h′gi′. Then gi−i′ ∈H, so i′ ≡i mod d since d is the order of g in G/H.
Write i′ = i + dd′, so h = h′ai′−i = h′gdd′. The terms h, h′, and gd are in H, so
χ(h′)eχ(g)i′ = χ(h′)eχ(g)ieχ(g)dd′
= χ(h′)eχ(g)iχ(gd)d′ since eχ(g)d = χ(gd)
= χ(h′gdd′)eχ(g)i
= χ(h)eχ(g)i.
Therefore eχ: ⟨H, g⟩→S1 is a well-deﬁned function and it is easily checked to be a homo-
morphism. It restricts to χ on H.
□

<!-- page 6 -->
6
KEITH CONRAD
Theorem 3.3. For a ﬁnite abelian group G and subgroup H, each character of H can be
extended to a character of G.
Proof. Let χ: H →S1 be a character of H.
Since G is ﬁnite, it has a ﬁnite generating set {g1, . . . , gk} (e.g., {gi} could be a listing
of all the elements of G). Therefore we can build up a tower of subgroups from H to G by
adjoining the elements gi one at a time:
H ⊂⟨H, g1⟩⊂⟨H, g1, g2⟩⊂· · · ⊂⟨H, g1, . . . , gk⟩= G.
Each step along this tower has the form Hi ⊂⟨Hi, gi⟩, where H0 = H. By applying Lemma
3.2 at each step of the tower, χ can be extended as a character from H to H1 to H2, and
so on up to Hk = G.
□
Let’s reﬁne this to count the number of extensions of a character from H to G.
Theorem 3.4. For a ﬁnite abelian group G and subgroup H, each character of H can be
extended to a character of G in [G : H] ways.
Proof. We will induct on the index [G : H]. The result is clear when [G : H] = 1, i.e.,
H = G, so suppose [G : H] > 1 and the theorem is proved for characters on subgroups of
index smaller than [G : H].
Pick g ∈G with g ̸∈H, so
H ⊂⟨H, g⟩⊂G.
To extend a character χ: H →S1 to G, we at least need to be able to extend χ to a character
eχ on ⟨H, g⟩. Let’s count the number of ways to do that. Then we will use induction to
count the number of extension of each character from ⟨H, g⟩all the way up to G.
Let d be the smallest positive integer such that gd ∈H. An extension of χ on H to
a character eχ on ⟨H, g⟩is determined by eχ(g), and this value has to satisfy the condition
eχ(g)d = χ(gd). Each number in S1 has d diﬀerent d-th roots in S1, so there are d potential
values for eχ(g). The proof of Lemma 3.2 shows all of them really work.
The number of choices of eχ extending χ is the number of choices for eχ(g), which is
d = [⟨H, g⟩: H].
Since [G : ⟨H, g⟩] < [G : H], by induction on the index there are
[G : ⟨H, g⟩] extensions of each eχ to a character of G, so the number of extensions of a
character on H to a character on G is [G : ⟨H, g⟩][⟨H, g⟩: H] = [G : H].
□
Theorem 3.5. If g ̸= 1 in a ﬁnite abelian group G then χ(g) ̸= 1 for some character χ of
G. The number of characters of G is |G|.
Proof. The cyclic group ⟨g⟩is nontrivial, say of size n, so n > 1. In S1 there is a cyclic
subgroup of order n, namely the group µn of n-th roots of unity. There is an isomorphism
⟨g⟩∼= µn, which can be viewed as a character of ⟨g⟩. By Theorem 3.3, this character of ⟨g⟩
extends to a character of G and does not send g to 1.
To show G has |G| characters, apply Theorem 3.4 with H the trivial subgroup.
□
We have used two important features of S1 as the target group for characters: for each
d ≥1 the dth power map on S1 is d-to-1 (proof of Theorem 3.4) and for each n ≥1 there
is a cyclic subgroup of order n in S1 (proof of Theorem 3.5).
Corollary 3.6. If G is a ﬁnite abelian group and g1 ̸= g2 in G then there is a character of
G that takes diﬀerent values at g1 and g2.
Proof. Apply Theorem 3.5 to g = g1g−1
2 .
□

<!-- page 7 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
7
Corollary 3.6 shows the characters of G “separate” the elements of G: diﬀerent elements
of the group admit a character taking diﬀerent values on them.
Corollary 3.7. If G is a ﬁnite abelian group and H ⊂G is a subgroup and g ∈G with
g ̸∈H then there is a character of G that is trivial on H and not equal to 1 at g.
Proof. We work in the group G/H, where g ̸= 1. By Theorem 3.5 there is a character of
G/H that is not 1 at g. Composing this character with the reduction map G →G/H yields
a character of G that is trivial on H and not equal to 1 at g.
□
It is easy to ﬁnd functions on G that separate elements without using characters. For
g ∈G, deﬁne δg : G →{0, 1} by
(3.3)
δg(x) =
(
1,
if x = g,
0,
if x ̸= g.
These functions separate elements of the group, but characters do this too and have better
algebraic properties: they are group homomorphisms.
Our deﬁnition of a character makes sense on nonabelian groups, but there will not be
enough such characters for Theorem 3.5 to hold if G is ﬁnite and nonabelian: a homomor-
phism χ: G →S1 must equal 1 on the commutator subgroup [G, G], which is a nontrivial
subgroup, so such homomorphisms can’t distinguish elements in [G, G] from each other. If
g ̸∈[G, G] then in the ﬁnite abelian group G/[G, G] the coset of g is nontrivial so there
is a character G/[G, G] →S1 that’s nontrivial on g. Composing this character with the
reduction map G →G/[G, G] produces a homomorphism G →S1 that is nontrivial on g.
Deﬁnition 3.8. For a character χ on a ﬁnite abelian group G, the conjugate character is
the function χ: G →S1 given by χ(g) := χ(g).
Since a complex number z with |z| = 1 has z = 1/z, χ(g) = χ(g)−1 = χ(g−1).
Deﬁnition 3.9. The dual group of a ﬁnite abelian group G is the set of homomorphisms
G →S1 with the group law of pointwise multiplication of functions: (χψ)(g) = χ(g)ψ(g).
The dual group of G is denoted bG.
The trivial character of G is the identity in bG and the inverse of a character is its conjugate
character. Note bG is abelian since multiplication in C× is commutative.
Theorem 3.5 says in part that
(3.4)
|G| = | bG|.
In fact, the groups G and bG are isomorphic. First let’s check this on cyclic groups.
Theorem 3.10. If G is cyclic then G ∼= bG as groups.
Proof. We will show bG is cyclic. Then since G and bG have the same size they are isomorphic.
Let n = |G| and γ be a generator of G. Set χ: G →S1 by χ(γj) = e2πij/n for all j. For
other characters ψ ∈bG, we have ψ(γ) = e2πik/n for some integer k, so ψ(γ) = χ(γ)k. Then
ψ(γj) = ψ(γ)j = χ(γ)jk = χ(γj)k,
which shows ψ = χk. Therefore χ generates bG.
□
Lemma 3.11. If A and B are ﬁnite abelian groups, there is an isomorphism \
A × B ∼= bA× bB.

<!-- page 8 -->
8
KEITH CONRAD
Proof. Let χ be a character on A × B. Identify the subgroups A × {1} and {1} × B of
A × B with A and B in the obvious way. Let χA and χB be the restrictions of χ to A and
B respectively, i.e., χA(a) = χ(a, 1) and χB(b) = χ(1, b). Then χA and χB are characters
of A and B and χ(a, b) = χ((a, 1)(1, b)) = χ(a, 1)χ(1, b) = χA(a)χB(b). So we get a map
(3.5)
\
A × B →bA × bB
by sending χ to (χA, χB). It is left to the reader to check (3.5) is a group homomorphism.
Its kernel is trivial since if χA and χB are trivial characters then χ(a, b) = χA(a)χB(b) = 1,
so χ is trivial. Both sides of (3.5) have the same size by (3.4), so (3.5) is an isomorphism.
□
Theorem 3.12. If G is a ﬁnite abelian group then G is isomorphic to bG.
Proof. The case when G is cyclic was Theorem 3.10. Lemma 3.11 extends easily to several
factors in a direct product:
(3.6)
(H1 × · · · × Hr) b ∼= bH1 × · · · × bHr.
When Hi is cyclic, bHi ∼= Hi, so (3.6) tells us that that character group of H1 × · · · × Hr is
isomorphic to itself. Every ﬁnite abelian group is isomorphic to a direct product of cyclic
groups, so the character group of a ﬁnite abelian group is isomorphic to itself.
□
Although G and bG are isomorphic groups, there is not a natural isomorphism between
them, even when G is cyclic. For instance, to prove G ∼= bG when G is cyclic we had to
choose a generator. If we change the generator, then the isomorphism changes.2
The double-dual group bbG is the dual group of bG. Since G and bG are isomorphic, G and
bbG are isomorphic. However, while there isn’t a natural isomorphism from G to bG, there is
a natural isomorphism from G to bbG. The point is that there is a natural way to map G to
its double-dual group: associate to each g ∈G the function “evaluate at g,” which is the
function bG →S1 given by χ 7→χ(g). Here g is ﬁxed and χ varies. This is a character of bG,
since (χ1χ2)(g) = χ1(g)χ2(g) by deﬁnition.
Theorem 3.13. Let G be a ﬁnite abelian group. The homomorphism G →bbG associating
to g ∈G the function “evaluate at g” is an isomorphism.
Proof. Since a ﬁnite abelian group and its dual group have the same size, a group and its
double-dual group have the same size, so it suﬃces to show this homomorphism is injective.
If g ∈G is in the kernel then every element of bG is 1 at g, so g = 1 by Theorem 3.5.
□
Theorem 3.13 is called Pontryagin duality. This label actually applies to a more general
result about characters of locally compact abelian groups.
Finite abelian groups are a
special case, where diﬃcult analytic techniques can be replaced by counting arguments.
The isomorphism between G and its double-dual group given by Pontryagin duality lets us
think about a ﬁnite abelian group G as a dual group (namely the dual group of bG).
The isomorphism in Pontryagin duality is natural: it does not depend on ad hoc choices
(unlike the isomorphism between a ﬁnite abelian group and its dual group).
Exercises.
2If G is trivial or of order 2, then it has a unique generator, so in that case we could say the isomorphism
G ∼= bG is canonical.

<!-- page 9 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
9
1. Let’s ﬁnd the characters of the additive group (Z/(m))r, an r-fold direct product.
(a) For k ∈Z/(m), let χk : Z/(m) →S1 by
χk(j) = e2πijk/m,
so χk(1) = e2πik/m.
Show χ0, χ1, . . . , χm−1 are all the characters of Z/(m) and
χkχl = χk+l.
(b) Let r ≥1. For r-tuples a, b in (Z/(m))r, let
a · b = a1b1 + · · · + arbr ∈Z/(m)
be the usual dot product. For k ∈(Z/(m))r, let χk(j) = e2πi(j·k)/m. Show the
functions χk are all the characters of (Z/(m))r and χkχl = χk+l.
2. Show the following are equivalent properties of a character χ: χ(g) = ±1 for all g,
χ(g) = χ(g) for all g, and χ2 = 1G.
3. Describe the error in the following bogus proof of Theorem 3.4. Let m = [G : H]
and pick a set of coset representatives g1, . . . , gm for G/H. Given a character χ on
H, deﬁne eχ on G by ﬁrst picking the m (= [G : H]) values eχ(gi) for 1 ≤i ≤m and
then writing each g ∈G in the (unique) form gih and deﬁning eχ(g) = eχ(gi)χ(h).
This deﬁnes bχ on G, and since we had to make m choices there are m characters.
4. For ﬁnite nonabelian G, show the characters of G (that is, homomorphisms G →S1)
separate elements modulo [G, G]: χ(g1) = χ(g2) for all χ if and only if g1 = g2 in
G/[G, G].
5. This exercise will give an interpretation of characters as eigenvectors. For a ﬁnite
abelian group G and g ∈G, let Tg : L(G) →L(G) by (Tgf)(x) = f(gx).
(a) Show the Tg’s are commuting linear transformations and each character of G
is an eigenvector of each Tg.
(b) If f is a simultaneous eigenvector of all the Tg’s, show f(1) ̸= 0 (if f(1) = 0
conclude f is identically zero, but the zero vector is not an eigenvector) and then
after rescaling f so f(1) = 1 deduce that f is a character of G. Thus the characters
of G are the simultaneous eigenvectors of the Tg’s, suitably normalized.
(c) Show the Tg’s are each diagonalizable. Deduce from this and parts (a) and
(b) that bG is a basis of L(G), so | bG| = dim L(G) = |G|. (This gives a diﬀerent proof
that G and bG have the same size.)
6. For a subgroup H of a ﬁnite abelian group G, let
H⊥= {χ ∈bG : χ = 1 on H}.
These are the characters of G that are trivial on H. For example, G⊥= {1G} and
{1}⊥= bG. Note H⊥⊂bG and H⊥depends on H and G.
Show H⊥is a subgroup of bG, it is isomorphic to [
G/H, and bG/(H⊥) ∼= bH. In
particular, |H⊥| = [G : H].
7. Let G be ﬁnite abelian and H ⊂G be a subgroup.
(a) Viewing H⊥⊥= (H⊥)⊥in G using Pontryagin duality, show H⊥⊥= H.
(Hint: The inclusion in one direction is easy. Count sizes for the other inclusion.)
(b) Show for each m dividing |G| that
|{H ⊂G : |H| = m} = |{H ⊂G : [G : H] = m}|
by associating H to H⊥and using a (ﬁxed) isomorphism of G with bG.

<!-- page 10 -->
10
KEITH CONRAD
(c) For a ﬁnite abelian group G, part b says the number of subgroups of G with
index 2 is equal to the number of elements of G with order 2. Use this idea to count
the number of subgroups of (Z/(m))× with index 2. (The answer depends on the
number of odd prime factors of m and the highest power of 2 dividing m.)
(d) Show, for a prime p, that the number of subspaces of (Z/(p))n with dimension
d equals the number of subspaces with dimension n −d.
8. For a ﬁnite abelian group G, let G[n] = {g ∈G : gn = 1} and Gn = {gn : g ∈G}.
Both are subgroups of G. Prove G[n]⊥= ( bG)n and (Gn)⊥= bG[n] in bG.
4. Finite Fourier series
Let G be a ﬁnite abelian group. Set
L(G) = {f : G →C},
the C-valued functions on G. This is a C-vector space of functions. Every f ∈L(G) can
be expressed as a linear combination of the delta-functions δg from (3.3):
(4.1)
f =
X
g∈G
f(g)δg.
Indeed, evaluate both sides at each x ∈G and we get the same value. The functions δg
span L(G) by (4.1) and they are linearly independent: if P
g agδg = 0 then evaluating the
sum at x ∈G shows ax = 0. Thus the functions δg are a basis of L(G), so dim L(G) = |G|.
The next theorem is the ﬁrst step leading to an expression for each δg as a linear combi-
nation of characters of G, which will lead to a Fourier series expansion of f. It is the ﬁrst
time we add character values.
Theorem 4.1. Let G be a ﬁnite abelian group. Then
X
g∈G
χ(g) =
(
|G|,
if χ = 1G,
0,
if χ ̸= 1G,
X
χ∈bG
χ(g) =
(
|G|,
if g = 1,
0,
if g ̸= 1.
Proof. Let S = P
g∈G χ(g). If χ is trivial on G then S = |G|. If χ is not trivial on G, say
χ(g0) ̸= 1. Then χ(g0)S = P
g∈G χ(gg0) = P
g∈G χ(g) = S, so S = 0.
The second formula in the theorem can be viewed as an instance of the ﬁrst formula via
Pontryagin duality: the second sum is a sum of the character “evaluate at g” over the group
bG, and this character on bG is nontrivial when g ̸= 1 by Pontryagin duality.
□
Theorem 4.1 says the sum of a nontrivial character over a group vanishes and the sum
of all characters of a group evaluated at a nontrivial element vanishes, so the sum of the
elements in each row and column of a character table of G is zero except the row for the
trivial character and the column for the identity element. Check this in Table 1.
Corollary 4.2. For characters χ1 and χ2 in bG and g1 and g2 in G,
X
g∈G
χ1(g)χ2(g) =
(
|G|,
if χ1 = χ2,
0,
if χ1 ̸= χ2,
X
χ∈bG
χ(g1)χ(g2) =
(
|G|,
if g1 = g2,
0,
if g1 ̸= g2.
Proof. In the ﬁrst equation of Theorem 4.1 let χ = χ1χ2. In the second equation of Theorem
4.1 let g = g1g−1
2 . (Alternatively, after proving the ﬁrst equation for all G we observe that
the second equation is a special case of the ﬁrst by Pontryagin duality.)
□

<!-- page 11 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
11
The equations in Corollary 4.2 are called the orthogonality relations.
They say that
the character table of G has orthogonal rows and orthogonal columns when we deﬁne
orthogonality of two n-tuples of complex numbers as vanishing of their Hermitian inner
product in Cn: ⟨(z1, . . . , zn), (w1, . . . , wn)⟩:= Pn
k=1 zkwk.
By the second equation in Corollary 4.2 we can express the delta-functions in terms of
characters:
X
χ∈bG
χ(g)χ(x) = |G|δg(x) =⇒δg(x) =
1
|G|
X
χ∈bG
χ(g)χ(x).
Substituting this formula for δg into (4.1) gives
f(x) =
X
g∈G
f(g)

1
|G|
X
χ∈bG
χ(g)χ(x)


=
X
χ∈bG
X
g∈G
1
|G|f(g)χ(g)χ(x)
=
X
χ∈bG
cχχ(x),
(4.2)
where
(4.3)
cχ =
1
|G|
X
g∈G
f(g)χ(g).
The expansion (4.2) is the Fourier series for f.
Equation (4.3) is similar to the formula for the coeﬃcient cn of einx in (2.1): an integral
over [0, 2π] divided by 2π is replaced by a sum over G divided by |G| and f(x)e−inx is
replaced by f(g)χ(g). The number e−inx is the conjugate of einx, which is also the relation
between χ(g) and χ(g). Equation (4.2) shows bG is a spanning set for L(G). Since | bG| =
|G| = dim L(G), bG is a basis for L(G).
Deﬁnition 4.3. Let G be a ﬁnite abelian group. If f ∈L(G) then its Fourier transform is
the function bf ∈L( bG) given by
bf(χ) =
X
g∈G
f(g)χ(g).
By (4.2) and (4.3),
(4.4)
f(x) =
1
|G|
X
χ∈bG
bf(χ)χ(x).
Equation (4.4) is called the Fourier inversion formula since it tells us how to recover f from
its Fourier transform.
Remark 4.4. Classically the Fourier transform of a function R →C is another function
R →C. The ﬁnite Fourier transform, however, is deﬁned on the dual group instead of on
the original group. We can also interpret the classical Fourier transform to be a function of
characters. For y ∈R let χy(x) = eixy. Then χy : R →S1 is a character and bf(y) could be
viewed as bf(χy) =
R
R f(x)χy(x) dx, so bf is a function of characters rather than of numbers.

<!-- page 12 -->
12
KEITH CONRAD
Example 4.5. Let f = δg. Then bf(χ) = χ(g) = χ(g−1).
Let’s look at Fourier transforms for functions on a cyclic group. By writing a cyclic
group in the form Z/(m), we can make an isomorphism with the dual group explicit: every
character of Z/(m) has the form χk : j 7→e2πijk/m for a unique k ∈Z/(m) (Exercise 3.1).
The Fourier transform of a function f : Z/(m) →C can be viewed as a function on Z/(m):
(4.5)
bf(k) :=
X
j∈Z/(m)
f(j)χk(j) =
X
j∈Z/(m)
f(j)e−2πijk/m.
This is like viewing the Fourier transform of a function on R as a function of R.
Example 4.6. Let f : Z/(8) →C have the periodic values 5, 3, 1, and 1. Both f and its
Fourier transform are in Table 3. This f has frequency 2 (its period repeats twice) and the
Fourier transform vanishes except at 0, 2, 4, and 6, which are multiples of the frequency.
n
0
1
2
3
4
5
6
7
f(n)
5
3
1
1
5
3
1
1
bf(n)
20
0
8 −4i
0
4
0
8 + 4i
0
Table 3.
Example 4.7. Consider a function f : Z/(45) →C with the four successive repeating values
1, 8, 19, 17 starting with f(0) = 1. It is not a periodic function on Z/(45) since 4 does not
divide 45, but the sequence 1, 8, 19, 17 repeats nearly 11 times. (The value of f(44) is 1.)
A calculation of | bf(n)|, which is plotted below, reveals peaks in red at n = 0, 11, 22, 23, and
34 that are all at least 3 times as high as nearby values. This can’t be shown to scale near
0, 11, and 34, which is why the values there have arrowheads on top. These peaks in | bf(n)|
occur approximately at multiples of the approximate frequency!
0
11
22 23
34
As Example 4.6 suggests, the Fourier transform of a periodic function on Z/(m) knows
the frequency of the original function by the positions where the Fourier transform has

<!-- page 13 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
13
nonzero values (Exercise 4.2). For nearly periodic functions on Z/(m), the approximate
frequency is reﬂected in where the Fourier transform takes on its largest values. This idea
is used in Shor’s quantum algorithm for integer factorization [2], [3, Chap. 17].
Exercises.
1. Let f : Z/(8) →C take the four values a, b, c, and d twice in this order. Compute
bf(n) explicitly and determine some values for a, b, c, and d such that bf(n) is nonzero
for n = 0, 2, and 6, but bf(4) = 0.
2. Let H be a subgroup of a ﬁnite abelian group G.
(a) Suppose f : G →C is constant on H-cosets (it is H-periodic). For χ ∈bG with
χ ̸∈H⊥, show bf(χ) = 0. Thus the Fourier transform of an H-periodic function on
G is supported on H⊥.
(b) If f : Z/(m) →C has period d where d | m, show bf : Z/(m) →C is supported
on the multiples of m/d. (See Example 4.6.)
3. Let f : G →C.
a) Show f(g) ∈R for all g if and only if bf(χ) = bf(χ) for all χ.
b) Show bf(χ) ∈R for all χ if and only if f(g) = f(g−1) for all g.
4. Let G be a ﬁnite abelian group and H be a subgroup. For a function f : G →C,
Poisson summation on G says
1
|H|
X
h∈H
f(h) =
1
|G|
X
χ∈H⊥
bf(χ),
where H⊥is as in Exercise 3.6. Prove this formula in two ways:
a) Copy the classical proof sketched in Section 2 (start with the function F(x) =
P
h∈H f(xh), which is H-periodic so it deﬁnes a function on G/H) to obtain
(4.6)
1
|H|
X
h∈H
f(xh) =
1
|G|
X
χ∈H⊥
bf(χ)χ(x)
for all x ∈G and then set x = 1.
b) By linearity in f of both sides of the desired identity, verify Poisson summation
directly on the delta-functions of G. (Corollary 3.7 and Example 4.5 will be useful.)
5. Structure of finite abelian groups
We will now put characters to work by using them to prove each ﬁnite abelian group is
a direct product of cyclic groups. This result was used in the proof of Theorem 3.12, that
G ∼= bG, but that work will not be used here, so no circular reasoning occurs.
The following theorem shows that every cyclic subgroup of maximal size in a ﬁnite abelian
group can be split oﬀas a direct factor. Characters get used in an essential way in the proof.
Theorem 5.1. Let G be a ﬁnite abelian group and let g ∈G have maximal order in G.
There is a subgroup H ⊂G such that G ∼= H × ⟨g⟩.
Proof. Let n be the order of g. The subgroup ⟨g⟩of G is cyclic of order n. In S1 there
is a cyclic subgroup of order n, namely µn.
Since cyclic groups of the same order are
isomorphic, there is an isomorphism ⟨g⟩→µn, so g is mapped to a root of unity of order
n. This isomorphism can be viewed as a character of ⟨g⟩. Extend this to a character of G

<!-- page 14 -->
14
KEITH CONRAD
(Theorem 3.3), so we have a character χ: G →S1 such that χ(g) has order n. The image
χ(G) contains µn, and it turns out to be no larger.
Claim: χ(G) = µn.
Since χ(G) is a ﬁnite subgroup of S1, it is cyclic (all ﬁnite subgroups of S1 are cyclic).
Therefore χ(G) = ⟨χ(γ)⟩for some γ ∈G. Since χ(G) contains µn, χ(G) = µnn′ where
n′ ≥1. Thus χ(γ) has order nn′. Let γ have order d in G, so γd = 1 in G and thus
χ(γ)d = 1 in S1. That implies nn′ | d, so nn′ ≤d. Since n is the maximal order of the
elements in G, d ≤n. The relations nn′ ≤d and d ≤n imply n′ = 1, so χ(G) = µn. This
proves the claim.
Set H = ker χ. Then H ∩⟨g⟩= {1} since χ is one-to-one on ⟨g⟩by construction. For each
x ∈G, χ(x) ∈χ(G) = µn = χ(⟨g⟩), so χ(x) = χ(gj) for some j. Therefore h := xg−j is in
H and x = hgj. This proves that the multiplication map H × ⟨g⟩→G where (h, gj) 7→hgj
is surjective. It is a homomorphism and its kernel is trivial, so G ∼= H × ⟨g⟩.
□
Theorem 5.2. Every ﬁnite abelian group G is isomorphic to a product of cyclic groups:
G ∼= Z/(n1) × Z/(n2) × · · · × Z/(nk).
Proof. Induct on |G|. The result is clear when |G| = 1. When |G| > 1, let n be the maximal
order of the elements of G, so G ∼= H×Z/(n) by Theorem 5.1. Since |H| < |G|, by induction
H is isomorphic to a direct product of cyclic groups, so G is also isomorphic to a direct
product of cyclic groups.
□
Theorem 5.2 can be reﬁned: G is a direct product of cyclic groups with the extra feature
that n1 | n2 | · · · | nk. To prove this, use the fact that the order of each element of a ﬁnite
abelian group G divides the maximal order of the elements of G.
Exercises.
1. What is the structure (as a direct product of cyclic groups) of the ﬁnite abelian
groups whose nontrivial characters all have order 2?
2. Mimic the proof of Theorem 5.1 to decompose (Z/(20))× (of size 8) and (Z/(45))×
(of size 24) into a direct product of cyclic groups.
3. Show by an explicit counterexample that the following is false: if two subgroups H
and K of a ﬁnite abelian group G are isomorphic then there is an automorphism of
G that restricts to an isomorphism from H to K.
4. For a ﬁnite abelian group G, show the maximum order of the elements of G and
the number |G| have the same prime factors. (Hint: If g has order n and there is
an element h of prime order p where p ∤n, what is the order of gh?)
This is false in general for nonabelian G, as shown in the table below where g(n)
(called Landau’s function) is the maximal order of the elements of Sn. For n ≥3 in
the table, some prime factor of n! = |Sn| does not divide g(n).
n
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
g(n)
1
2
3
4
6
6
12
15
20
30
30
60
60
84
105
Table 4. Maximal order of elements of Sn
5. Let G be a ﬁnite abelian group and F be a ﬁeld containing a full set of |G|th roots
of unity. (So x|G| = 1 has |G| solutions in F.) Deﬁne characters of G to be group
homomorphisms χ: G →F × and write the set of all such characters as bG.

<!-- page 15 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
15
a) Construct a character table for Z/(4) and (Z/(2))2 when F is the ﬁeld Z/(5).
b) Prove every lemma, theorem, and corollary from Section 3 for the new meaning
of bG.
There is no longer complex conjugation on character values, but the
inverse of χ is still the function g 7→χ(g−1) = χ(g)−1.
(Hint: For each d
dividing |G|, xd = 1 has d distinct solutions in F ×, which form a cyclic group.)
c) Prove Theorem 4.1 and Corollary 4.2 for F-valued characters of G.
d) Set L(G, F) to be the functions G →F.
This is an F-vector space in the
same way that L(G) is a complex vector space. For each function f ∈L(G, F),
deﬁne its Fourier transform bf ∈L( bG, F) by bf(χ) = P
g∈G f(g)χ(g−1). Prove
the Fourier inversion formula and Plancherel’s theorem in this context. (Note:
If the ﬁeld F has characteristic p then 1/|G| in the Fourier inversion formula
makes sense in F since p doesn’t divide |G| – why?)
e) Check everything you have done goes through if the assumption that x|G| = 1
has a full set of solutions in F is weakened to xm = 1 having a full set of
solutions in F, where m is the maximal order of the elements of G. For example,
if G = (Z/(2))d then m = 2 and we can use F = Z/(3).
6. Existence of solutions to a Mordell equation mod p
For k ∈Z, an equation of the form y2 = x3 +k is called a Mordell equation. When k ̸= 0,
it is a hard theorem that such an equation has only ﬁnitely many integral solutions (x, y),
which could include having no integral solutions.3 For example, the integral solutions of
y2 = x3 −4 are (2, ±2) and (5, ±11), and the equation y2 = x3 −5 has no integral solutions.
Using characters, we will show the congruence y2 ≡x3 + k mod p modulo a prime p always
has a solution.
For a character χ on (Z/(p))×, extend χ to Z/(p) by setting χ(0) = 0. Then χ(ab) =
χ(a)χ(b) for all a, b ∈Z/(p).
Lemma 6.1. If p is prime and d | (p −1), there is a character χ of (Z/(p))× with order d,
and for each a ∈Z/pZ,
|{x ∈Z/(p) : xd ≡a mod p}| = 1 + χ(a) + χ(a)2 + · · · + χ(a)d−1.
Proof. The group (Z/(p))× is cyclic of order p −1,4 so |{x ∈Z/(p) : xd ≡1 mod p}| = d
since d | (p −1). Thus
(6.1) |{x ∈Z/(p) : xd ≡a mod p}| =





d,
if a ̸≡0 mod p and a is a dth power mod p,
1,
if a ≡0 mod p,
0,
if a is not a dth power mod p.
The character group of (Z/(p))× is cyclic of order p −1 by Theorem 3.10, so (Z/(p))×
has a character of order d. Call such a character χ. For each a ∈Z/(p), we’ll show that
1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 has the same values as in (6.1).
• If a is a nonzero dth power mod p, say a ≡bd mod p, then χ(a) = χ(bd) = χ(b)d = 1
since χd is identically 1 on (Z/(p))×, so 1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 = d.
• If a ≡0 mod p then χ(a) = 0, so 1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 = 1.
3When k = 0, the equation is y2 = x3 and has inﬁnitely many integral solutions (x, y) = (a2, a3) for a ∈Z.
4See https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf for many proofs of this.

<!-- page 16 -->
16
KEITH CONRAD
• Lastly, if a is in (Z/(p))× and is not a dth power, we’ll show χ(a) ̸= 1, so by summing
a ﬁnite geometric series,
1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 = χ(a)d −1
χ(a) −1 =
1 −1
χ(a) −1 = 0,
which would complete the proof.
Let g be a generator of (Z/(p))× and write a = gk for k ∈Z.
Step 1: χ(g) has order d. Since χ has order d, χ(g)d = 1, so χ(g) has order
dividing d. Since χ((Z/(p))×) = ⟨χ(g)⟩, if χ(g) has order less than d then χ as a
character has order less than d, which χ doesn’t. Thus χ(g) has order d.
Step 2: χ(a) ̸= 1. If χ(a) = 1 then χ(g)k = 1, so d | k by Step 1. Then a = gk is
a dth power, which isn’t the case, so χ(a) ̸= 1.
□
Theorem 6.2. For each prime p and integer k, the number of solutions (x, y) in Z/(p) to
y2 ≡x3 + k mod p is p if p ≡1 mod 3 and is at least 2 if p ̸≡1 mod 3.
Proof. Case 1: p ̸≡1 mod 3.
Since 3 ∤(p −1) we have (3, p −1) = 1, so cubing is a bijection Z/(p) →Z/(p) (on
(Z/(p))× it is injective and thus surjective since the group is ﬁnite), so for each y ∈Z/(p)
there is a unique x ∈Z/(p) such that y2 −k ≡x3 mod p. Thus the number of solutions in
Z/(p) of y2 ≡x3 + k mod p is p.
Case 2: p ≡1 mod 3.
If k ≡0 mod p, then the congruence is y2 ≡x3 mod p, which has the p solutions (t2, t3)
for t ∈Z/(p) (and in fact no further solutions5). So now we can assume k ̸≡0 mod p.
Since 3 | (p−1), there is a cubic character χ on (Z/(p))×, meaning χ has order 3, and the
inverse χ2 of χ is the complex conjugate χ. Since p is odd, there is a quadratic character ψ
on (Z/(p))× (it’s the Legendre symbol). To count solutions to y2 ≡x3 + k mod p we will
count solutions (a, b) to the simpler equation b ≡a + k mod p and then count how often a
is a cube mod p and b is a square mod p.
By Lemma 6.1, the number of ways a is a cube mod p is 1+χ(a)+χ(a)2 = 1+χ(a)+χ(a),
and the number of ways b is a square mod p is 1 + ψ(b). Let Np(k) be the number of mod
p solutions to y2 ≡x3 + k mod p, so
Np(k) =
X
(a,b)
(1 + χ(a) + χ(a))(1 + ψ(b)) =
X
a
(1 + χ(a) + χ(a))(1 + ψ(a + k)),
where the ﬁrst sum runs over all (a, b) mod p for which b ≡a + k mod p.
(Note a or
b determines the other mod p.) Expanding out the second sum, we get a sum over all
a mod p with each summand having 6 terms:
Np(k) =
X
a
(1 + χ(a) + χ(a) + ψ(a + k) + χ(a)ψ(a + k) + χ(a)ψ(a + k)).
Split this up into 6 sums. The ﬁrst sum is p since the number of possible a mod p is
p. The second and third sums, P
a χ(a) and P
a χ(a), are 0 since the sum of a nontrivial
multiplicative character over Z/(p) is 0 (a term where a = 0 can be dropped since χ(0) = 0
5If F is any ﬁeld, the solutions of y2 = x3 in F are all of the form (t2, t3) as t runs over F: if x ̸= 0, set
t = y/x ̸= 0, so t2 = y2/x2 = x3/x2 = x and t3 = y3/x3 = y3/y2 = y. That shows all solutions (x, y) where
x ̸= 0 have the form (t2, t3) where t ∈F ×, and (0, 0) also has that form with t = 0.

<!-- page 17 -->
CHARACTERS OF FINITE ABELIAN GROUPS (SHORT VERSION)
17
and χ(0) = 0). Similarly, P
a ψ(a+k) = P
a ψ(a) = 0 using a change of variables a 7→a−k.
We’re left with
Np(k) = p +
X
a
χ(a)ψ(a + k) +
X
a
χ(a)ψ(a + k).
Since k ̸≡0 mod p, we can make the change of variables a 7→ka in both sums and pull out
the character values at k:
Np(k) = p + χ(k)ψ(k)
X
a
χ(a)ψ(a + 1) + χ(k)ψ(k)
X
a
χ(a)ψ(a + 1).
Replace a mod p with −a mod p in the sums:
Np(k) = p + χ(−k)ψ(k)
X
a
χ(a)ψ(1 −a) + χ(−k)ψ(k)
X
a
χ(a)ψ(1 −a).
Set J = P
a χ(a)ψ(1 −a), so J = P
a χ(a)ψ(1 −a) since ψ-values are ±1. Thus
Np(k) = p + χ(−k)ψ(k)J + χ(−k)ψ(k)J = p + 2Re(χ(−k)ψ(k)J).
For each z ∈C, |Re(z)| ≤
p
|z|, so |Np(k) −p| ≤2
p
|J|. Since χ and ψ are nontrivial
multiplicative characters mod p and χψ is nontrivial, |J| = √p.6 Thus |Np(k) −p| ≤2√p,
so Np(k) ≥p−2√p. The function x−2√x on (0, ∞) is increasing for x > 1. If p ≡1 mod 3
then p ≥7, so Np(k) ≥p −2√p ≥7 −2
√
7 ≈1.7, so Np(k) ≥2.
□
By an explicit search for solutions of y2 ≡x3 + k mod 7 as k varies, the number of
solutions is 2 if k ≡4 mod 7 (namely (0, ±2)), 3 if k ≡6 mod 7 (namely (1, 0), (2, 0), and
(4, 0)), and at least 6 for other k mod 7. After 7, the next prime that is 1 mod 3 is 13 and
13 −2
√
13 ≈5.7, so Np(k) ≥6 if p ≡1 mod 3 and p > 7.
Exercises.
1. For prime p and n ∈Z+, set d = (n, p−1). For r ∈Z, let ϕr : (Z/(p))× →(Z/(p))×
by ϕr(x) = xr.
a) Show ϕn and ϕd have the same image and same kernel. (Hint: d is a Z-linear
combination of n and p −1.) For example, on (Z/(11))×, show ϕ4 and ϕ2 have
image {1, 3, 4, 5, 9} and kernel {1, 10}.
b) For nonzero a in Z/(p), use (a) to show the equations xn = a and xd = a have
the same number of solutions in Z/(p).
c) Find all solutions of x4 = 3 and of x2 = 3 in Z/(11). (There are two solutions
in each case.)
d) For nonzero a in Z/(p), show xn + yn = a and xd + yd = a have the same
number of solutions in Z/(p).
2. Let p be prime, a be nonzero in Z/(p), and d be a positive factor of p −1. We want
to estimate the number of solutions of xd + yd = a in Z/(p).
a) For a polynomial f(x) with coeﬃcients in Z/(p), let N(f(x) = a) be the
number of solutions of f(x) = a in Z/(p). By Lemma 6.1, (Z/(p))× has a character
6See Corollary 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

<!-- page 18 -->
18
KEITH CONRAD
χ of order d and we set χ(0) = 0. Show
N(xd + yd = a) =
X
b,c∈Z/(p)
b+c=a
N(xd = b)N(yd = c)
=
X
b∈Z/(p)
 
1 +
d−1
X
i=1
χ(b)i
! 
1 +
d−1
X
j=1
χ(a −b)j

.
b) When a ̸= 0 in Z/(p), expand the product in (a) and rearrange terms to show
N(xd + yd = a) = p +
X
1≤i,j≤d−1
X
b∈Z/(p)
χ(b)iχ(a −b)j
= p +
X
1≤i,j≤d−1
χ(a)i+j
X
b∈Z/(p)
χ(b)iχ(1 −b)j.
c) For characters ψ and ψ′ on (Z/(p))×, set J(ψ, ψ′) = P
b∈Z/(p) ψ(b)ψ′(1 −b) (it
is called a Jacobi sum), so by (b), if a ̸= 0 in Z/(p) then
N(xd + yd = a) = p +
X
1≤i,j≤d−1
χ(a)i+jJ(χi, χj).
For a nontrivial character ψ on (Z/(p))×, J(ψ, ψ) = −ψ(−1).7 Use that to show
N(xd + yd = a) = p + 1 −N(xd = −1) +
X
1≤i,j≤d−1
i+j̸=d
χ(a)i+j
X
b∈Z/(p)
χ(b)iχ(1 −b)j.
d) When ψ, ψ′, and ψψ′ are all nontrivial, |J(ψ, ψ′)| = √p.8 Use that and (c) to
show for nonzero a in Z/(p) that
|N(xd + yd = a) −(p + 1)| ≤d + (d −1)(d −2)√p
e) Use part (d) and Exercise 6.1(d) to show for n ∈Z+ and suﬃciently large p
(depending only on n) that for each a ∈(Z/(p))× the equation xn + yn = a has a
solution in Z/(p) where x and y are both nonzero.
References
[1] A. Terras, “Fourier Analysis on Finite Groups and Applications,” Cambridge Univ. Press, Cambridge,
1999.
[2] P. Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum
Computer, http://arxiv.org/abs/quant-ph/9508027v2.
[3] W. Trappe and L. Washington, “Introduction to Cryptography with Coding Theory,” Prentice-Hall,
Upper Saddle River, NJ 2002.
[4] N. Wiener, “I am a Mathematician,” MIT Press, Cambridge, 1964.
7See Theorem 2.5 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.
8See Corollary 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*