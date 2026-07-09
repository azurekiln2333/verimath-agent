# Characters of Finite Abelian Groups

> **Source**: https://kconrad.math.uconn.edu/blurbs/charthy.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
CHARACTERS OF FINITE ABELIAN GROUPS
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
where the summation runs over all integers (c0 = a0, cn = 1
2(an −bni) for n > 0, and
cn = 1
2(a|n| + b|n|i) for n < 0). The convenient algebraic property of einx, which is not
shared by sines and cosines, is that it is a group homomorphism from R to the unit circle
S1 = {z ∈C : |z| = 1}:
ein(x+x′) = einxeinx′.
We now replace the real line R with a ﬁnite abelian group. Here is the analogue of the
functions einx.
Deﬁnition 1.1. A character of a ﬁnite abelian group G is a homomorphism χ: G →S1.
We will usually write abstract groups multiplicatively, so χ(g1g2) = χ(g1)χ(g2) and
χ(1) = 1.
Example 1.2. The trivial character of G is the homomorphism 1G deﬁned by 1G(g) = 1
for all g ∈G.
Example 1.3. Let G be cyclic of order 4 with generator γ. Since γ4 = 1, a character χ of
G has χ(γ)4 = 1, so χ takes only four possible values at γ, namely 1, i, −1, or −i. Once
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
i
−1
−i
χ2
1
−1
1
−1
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
When G has size n and g ∈G, for each character χ of G we have χ(g)n = χ(gn) = χ(1) =
1, so the values of χ lie among the nth roots of unity in S1. More precisely, the order of
χ(g) divides the order of g (which divides |G|).
Characters on ﬁnite abelian groups were ﬁrst studied in number theory, which is a source
of many interesting ﬁnite abelian groups. For instance, Dirichlet used characters of the group
(Z/(m))× to prove that when (a, m) = 1 there are inﬁnitely many primes p ≡a mod m. The
quadratic reciprocity law of elementary number theory is concerned with a deep property
of a particular character, the Legendre symbol. Fourier series on ﬁnite abelian groups have
applications in engineering: signal processing (the fast Fourier transform [1, Chap. 9]) and
error-correcting codes [1, Chap. 11].
A context for appreciating this account of characters on ﬁnite abelian groups is in Section
2 on Fourier analysis on the real line. In Section 3 we will run through some properties of
characters of a ﬁnite abelian group G and introduce its dual groups. In particular, we will
see that G is isomorphic to its dual group, but not naturally, and G is naturally isomorphic
to its double-dual group (Pontryagin duality). Section 4 uses characters of G to develop a
ﬁnite analogue of Fourier series. In Section 6 we use characters of (Z/pZ)× to count solutions
to a congruence mod p. In Section 5 we use characters to prove a structure theorem for
ﬁnite abelian groups. In Section 7 we look at duality on group homomorphisms. Characters
are used in Section 8 to factor the group determinant of a ﬁnite abelian group. In Section
9, we decompose linear G-actions into common eigenspaces indexed by characters of G.
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

<!-- page 3 -->
CHARACTERS OF FINITE ABELIAN GROUPS
3
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
An important link between a function f(x) and its Fourier coeﬃcients cn is given by Par-
seval’s formula
X
n∈Z
|cn|2 = 1
2π
Z 2π
0
|f(x)|2 dx.
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
Parseval’s formula becomes
(2.3)
X
n∈Z
|cn|2 =
Z 1
0
|f(x)|2 dx.
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
Deﬁne a Hermitian inner product of two functions f1 and f2 from R to C by the integral
⟨f1, f2⟩=
Z
R
f1(x)f2(x) dx ∈C,
Plancherel’s theorem compares the inner product of two functions and the inner product of
their Fourier transforms:
(2.4)
⟨bf1, bf2⟩= ⟨f1, f2⟩.
In particular, when f1 = f2 = f the result is
Z
R
| bf(y)|2 dy =
Z
R
|f(x)|2 dx,
which is called Parseval’s formula since it is an analogue of (2.3).
The convolution of two functions f1 and f2 from R to C is a new function from R to C
deﬁned by
(f1 ∗f2)(x) =
Z
R
f1(t)f2(x −t) dt
and the Fourier transform turns this convolution into pointwise multiplication:
\
f1 ∗f2(y) = bf1(y) bf2(y).

<!-- page 4 -->
4
KEITH CONRAD
Example 2.1. A Gaussian is a function of the form ae−bx2, where b > 0. For example, the
Gaussian (1/
√
2π)e−(1/2)x2 is important in probability theory. The Fourier transform of a
Gaussian is another Gaussian and the convolution of two Gaussians is another Gaussian:
(2.5)
Z
R
ae−bx2e−2πixy dx =
rπ
b ae−π2y2/b
and
f1(x) = e−b1x2,
f2(x) = e−b2x2 =⇒(f1 ∗f2)(x) =
r
π
b1 + b2
e−(b1b2/(b1+b2))x2.
The formula (2.5) says that a highly peaked Gaussian (large b) has a Fourier transform
that is a spread out Gaussian (small π2/b) and vice versa. More generally, a function and
its Fourier transform can’t both be highly localized; this is a mathematical incarnation of
Heisenberg’s uncertainty principle from physics.1
When b = π, (2.5) tells us that ae−πx2 is its own Fourier transform. Functions equal to
their Fourier transform are called self-dual, and e−πx2 is the simplest nonzero example.
A link between Fourier series and Fourier integrals is the Poisson summation formula:
for a “nice” function f : R →C that decays rapidly enough at ±∞,
(2.6)
X
n∈Z
f(n) =
X
n∈Z
bf(n),
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
b e−π2n2/b.
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
1Heisenberg discovered his uncertainty principle in 1926 and published it in 1927, but Norbert Wiener
lectured on a purely mathematical version of this idea in 1925 [5, pp. 106–108].

<!-- page 5 -->
CHARACTERS OF FINITE ABELIAN GROUPS
5
Therefore the expansion of F(x) into a Fourier series is equivalent to
(2.7)
X
n∈Z
f(x + n) =
X
n∈Z
bf(n)e2πinx,
which becomes the Poisson summation formula (2.6) by setting x = 0.
If we replace a sum over Z with a sum over a one-dimensional lattice L = aZ in R, where
a ̸= 0, the Poisson summation formula becomes
X
λ∈L
f(λ) = 1
|a|
X
µ∈L⊥
bf(µ),
where L⊥= (1/a)Z is the “dual lattice”:
L⊥= {µ ∈R : e2πiλµ = 1 for all λ ∈L}.
For example, Z⊥= Z.
There are several conventions for the deﬁnition of the Fourier transform as well as the
inner product and convolution of functions. Tables 2 and 3 collect a number of diﬀerent 2π-
conventions. The ﬁrst two columns of Tables 2 and 3 are deﬁnitions and the other columns
are theorems.
bf(y)
⟨f1, f2⟩
f(x)
⟨bf1, bf2⟩
R
R f(x)e−2πixy dx
R
R f1(x)f2(x) dx
R
R bf(y)e2πixy dy
⟨f1, f2⟩
R
R f(x)e−ixy dx
R
R f1(x)f2(x) dx
1
2π
R
R bf(y)eixy dy
2π⟨f1, f2⟩
1
√
2π
R
R f(x)e−ixy dx
1
√
2π
R
R f1(x)f2(x) dx
1
√
2π
R
R bf(y)eixy dy
⟨f1, f2⟩
Table 2.
bf(y)
(f1 ∗f2)(x)
\
f1 ∗f2(y)
R
R f(x)e−2πixy dx
R
R f1(y)f2(x −y) dy
bf1(y) bf2(y)
R
R f(x)e−ixy dx
R
R f1(y)f2(x −y) dy
bf1(y) bf2(y)
1
√
2π
R
R f(x)e−ixy dx
1
√
2π
R
R f1(t)f2(x −t) dt
bf1(y) bf2(y)
Table 3.
When the Fourier transform is deﬁned using bf(y) =
1
√
2π
R
R f(x)e−ixy dx, the function
e−πx2 is no longer self-dual, but e−(1/2)x2 is self-dual. You need to know how the Fourier
transform is deﬁned to say that a particular function is self-dual.
Exercises.
1. Without dwelling on analytic subtleties, check from Fourier inversion that bbf(x) =
f(−x) (if the Fourier transform is deﬁned suitably).
2. If f is a real-valued even function, show its Fourier transform is also real-valued and
even (assuming the Fourier transform of f is meaningful).

<!-- page 6 -->
6
KEITH CONRAD
3. For a function f : R →C and c ∈R, let g(x) = f(x + c). Deﬁne the Fourier
transform of a function h by bh(y) =
R
R h(x)e−2πixy dx. If f has a Fourier transform,
show g has Fourier transform bg(y) = e2πicy bf(y).
4. The Poisson summation formula over R was obtained by setting x = 0 in (2.7).
Conversely, show that (2.7) for the function f follows from the Poisson summation
formula for the function g(t) = f(t + x).
5. Assuming the Fourier inversion formula holds for a deﬁnition of the Fourier trans-
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
for a sign in the exponential term.) Considering Ff to be the Fourier transform of
f, show e−(1/2)βx2 is self-dual.
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

<!-- page 7 -->
CHARACTERS OF FINITE ABELIAN GROUPS
7
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

<!-- page 8 -->
8
KEITH CONRAD
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
Remark 3.8. Nowhere in the proof of Theorem 3.4 did we use the ﬁniteness of G. What
mattered was ﬁniteness of [G : H]. Inﬁnite abelian groups like Z or Zn can contain ﬁnite-
index subgroups, so it’s worth noting that we really proved that for each abelian group G,
a character on a ﬁnite-index subgroup H extends in [G : H] ways to a character on G.
This result for ﬁnite-index subgroups of inﬁnite G has applications to Hecke characters in
algebraic number theory.
Using Zorn’s lemma (the axiom of choice), not only the ﬁniteness of |G| but also the
ﬁniteness of [G : H] can be removed: a character of a subgroup H of an abelian group G
can be extended to a character of G (but the counting aspect with [G : H] is no longer
meaningful). In particular, Corollaries 3.6 and 3.7 are true for all abelian groups G.
Our deﬁnition of a character makes sense on nonabelian groups, but there will not be
enough such characters for Theorem 3.5 to hold if G is ﬁnite and nonabelian: a homomor-
phism χ: G →S1 must equal 1 on the commutator subgroup [G, G], which is a nontrivial

<!-- page 9 -->
CHARACTERS OF FINITE ABELIAN GROUPS
9
subgroup, so such homomorphisms can’t distinguish elements in [G, G] from each other. If
g ̸∈[G, G] then in the ﬁnite abelian group G/[G, G] the coset of g is nontrivial so there is a
character G/[G, G] →S1 that’s nontrivial on g. Composing this character with the reduc-
tion map G →G/[G, G] produces a homomorphism G →S1 that is nontrivial on g. There-
fore [G, G] = T
χ ker χ, where the intersection runs over all homomorphisms χ: G →S1.
This gives a “natural” explanation of why the commutator subgroup is normal in terms of
kernels of homomorphisms: kernels are normal and the intersection of normal subgroups is
normal. We put the word natural in quotes because appealing to the group G/[G, G] in
part of the argument means we had to use the normality of [G, G] anyway. (Using Zorn’s
lemma as in Remark 3.8, the intersection formula for [G, G] applies to all groups, not just
ﬁnite groups.)
Deﬁnition 3.9. For a character χ on a ﬁnite abelian group G, the conjugate character is
the function χ: G →S1 given by χ(g) := χ(g).
Since each complex number z with |z| = 1 has z = 1/z, χ(g) = χ(g)−1 = χ(g−1).
Deﬁnition 3.10. The dual group, or character group, of a ﬁnite abelian group G is the
set of homomorphisms G →S1 with the group law of pointwise multiplication of functions:
(χψ)(g) = χ(g)ψ(g). The dual group of G is denoted bG.
The trivial character of G is the identity in bG and the inverse of a character is its conjugate
character. Note bG is abelian since multiplication in C× is commutative.
Theorem 3.5 says in part that
(3.4)
|G| = | bG|.
In fact, the groups G and bG are isomorphic. First let’s check this on cyclic groups.
Theorem 3.11. If G is cyclic then G ∼= bG as groups.
Proof. We will show bG is cyclic. Then since G and bG have the same size they are isomorphic.
Let n = |G| and γ be a generator of G. Set χ: G →S1 by χ(γj) = e2πij/n for all j. For
other characters ψ ∈bG, we have ψ(γ) = e2πik/n for some integer k, so ψ(γ) = χ(γ)k. Then
ψ(γj) = ψ(γ)j = χ(γ)jk = χ(γj)k,
which shows ψ = χk. Therefore χ generates bG.
□
Lemma 3.12. If A and B are ﬁnite abelian groups, there is an isomorphism \
A × B ∼= bA× bB.
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
Theorem 3.13. If G is a ﬁnite abelian group then G is isomorphic to bG.

<!-- page 10 -->
10
KEITH CONRAD
Proof. The case when G is cyclic was Theorem 3.11. Lemma 3.12 extends easily to several
factors in a direct product:
(3.6)
(H1 × · · · × Hr) b ∼= bH1 × · · · × bHr.
When Hi is cyclic, bHi ∼= Hi, so (3.6) tells us that that dual group of H1 × · · · × Hr is
isomorphic to H1 × · · · × Hr. Every ﬁnite abelian group is isomorphic to a direct product
of cyclic groups, so the dual group of a ﬁnite abelian group is isomorphic to itself.
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
Theorem 3.14. Let G be a ﬁnite abelian group. The homomorphism G →bbG associating
to g ∈G the function “evaluate at g” is an isomorphism.
Proof. Since a ﬁnite abelian group and its dual group have the same size, a group and its
double-dual group have the same size, so it suﬃces to show this homomorphism is injective.
If g ∈G is in the kernel then every element of bG is 1 at g, so g = 1 by Theorem 3.5.
□
Theorem 3.14 is called Pontryagin duality. This label actually applies to a more general
result about characters of locally compact abelian groups.
Finite abelian groups are a
special case, where diﬃcult analytic techniques can be replaced by counting arguments.
The isomorphism between G and its double-dual group given by Pontryagin duality lets us
think about every ﬁnite abelian group G as a dual group (namely the dual group of bG).
The isomorphism in Pontryagin duality is natural: it does not depend on ad hoc choices
(unlike the isomorphism between a ﬁnite abelian group and its dual group).
To illustrate Pontryagin duality, consider the following theorem.
Theorem 3.15. Let G be a ﬁnite abelian group and m ∈Z.
a) For g ∈G, gm = 1 if and only if χ(g) = 1 for every χ ∈bG that is an mth power in
bG.
b) For g ∈G, g is an mth power in G if and only if χ(g) = 1 for every χ ∈bG satisfying
χm = 1G.
Proof. a) If gm = 1 and χ = ψm for some ψ ∈bG then
χ(g) = ψm(g) = ψ(g)m = ψ(gm) = ψ(1) = 1.
Conversely, suppose χ(g) = 1 whenever χ = ψm for some ψ ∈bG. Then for all ψ ∈bG we
have 1 = ψm(g) = ψ(gm), so gm = 1 by Theorem 3.5.
2If G is trivial or of order 2, then it has a unique generator, so in that case we could say the isomorphism
G ∼= bG is canonical.

<!-- page 11 -->
CHARACTERS OF FINITE ABELIAN GROUPS
11
b) If g = xm for some x ∈G then for every χ ∈bG such that χm = 1G we have
χ(g) = χ(x)m = χm(x) = 1.
Conversely, assume χ(g) = 1 for all χ such that χm = 1G. Such χ are identically 1 on the
subgroup Gm of mth powers in G. Conversely, every character of G that is trivial on the
subgroup Gm has mth power 1G (why?). Therefore χ(g) = 1 for all χ in bG that are trivial
on Gm, so g ∈Gm by Corollary 3.7.
□
Since Theorem 3.15 is a theorem about all ﬁnite abelian groups, by Pontryagin duality
we can swap the roles of G and bG in the theorem. Part a is equivalent to
χm = 1G ⇐⇒χ(g) = 1 for every g ∈G such that g = xm for some x ∈G
and part b is equivalent to
χ is an mth power in bG ⇐⇒χ(g) = 1 for all g ∈G such that gm = 1.
Exercises.
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
4. Let G be a ﬁnite abelian group of order n and g ∈G have order m. Show
Y
χ∈bG
(1 −χ(g)T) = (1 −T m)n/m.
5. For ﬁnite nonabelian G, show the characters of G (that is, homomorphisms G →S1)
separate elements modulo [G, G]: χ(g1) = χ(g2) for all χ if and only if g1 = g2 in
G/[G, G].
6. This exercise will give an interpretation of characters as eigenvectors. For a ﬁnite
abelian group G and g ∈G, let Tg : L(G) →L(G) by (Tgf)(x) = f(gx).
(a) Show the Tg’s are commuting linear transformations and each character of G
is an eigenvector of each Tg.
(b) If f is a simultaneous eigenvector of all the Tg’s, show f(1) ̸= 0 (if f(1) = 0
conclude f is identically zero, but the zero vector is not an eigenvector) and then

<!-- page 12 -->
12
KEITH CONRAD
after rescaling f so f(1) = 1 deduce that f is a character of G. Thus the characters
of G are the simultaneous eigenvectors of the Tg’s, suitably normalized.
(c) Show the Tg’s are each diagonalizable. Deduce from this and parts (a) and
(b) that bG is a basis of L(G), so | bG| = dim L(G) = |G|. (This gives a diﬀerent proof
that G and bG have the same size.)
7. For a subgroup H of a ﬁnite abelian group G, let
H⊥= {χ ∈bG : χ = 1 on H}.
These are the characters of G that are trivial on H. For example, G⊥= {1G} and
{1}⊥= bG. Note H⊥⊂bG and H⊥depends on H and G.
Show H⊥is a subgroup of bG, it is isomorphic to [
G/H, and bG/(H⊥) ∼= bH. In
particular, |H|⊥= [G : H].
8. Let G be ﬁnite abelian and H ⊂G be a subgroup.
(a) Viewing H⊥⊥= (H⊥)⊥in G using Pontryagin duality, show H⊥⊥= H.
(Hint: The inclusion in one direction is easy. Count sizes for the other inclusion.)
(b) Show for each m dividing |G| that
|{H ⊂G : |H| = m}| = |{H ⊂G : [G : H] = m}|
by associating H to H⊥and using a (ﬁxed) isomorphism of G with bG.
(c) For a ﬁnite abelian group G, part b says the number of subgroups of G with
index 2 is equal to the number of elements of G with order 2. Use this idea to count
the number of subgroups of (Z/(m))× with index 2. (The answer depends on the
number of odd prime factors of m and the highest power of 2 dividing m.)
(d) Show, for a prime p, that the number of subspaces of (Z/(p))n with dimension
d equals the number of subspaces with dimension n −d.
9. For a ﬁnite abelian group G, let G[n] = {g ∈G : gn = 1} and Gn = {gn : g ∈G}.
Both are subgroups of G. Prove G[n]⊥= ( bG)n and (Gn)⊥= bG[n] in bG.
4. Finite Fourier series
We will introduce the analogue of Fourier series on ﬁnite abelian groups.
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

<!-- page 13 -->
CHARACTERS OF FINITE ABELIAN GROUPS
13
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
The equations in Corollary 4.2 are called the orthogonality relations.
They say that
the character table of G has orthogonal rows and orthogonal columns when we deﬁne
orthogonality of two n-tuples of complex numbers as vanishing of their Hermitian inner
product: in Cn: ⟨(z1, . . . , zn), (w1, . . . , wn)⟩:= Pn
k=1 zkwk.
Example 4.3. Let G = (Z/(m))×. For a ∈(Z/(m))× and p a prime not dividing m,
1
ϕ(m)
X
χ mod m
χ(a)χ(p) =
(
1,
if p ≡a mod m,
0,
if p ̸≡a mod m,
where the sum runs over the characters of (Z/(m))×. (Since p is prime, p not dividing m
forces p to be in (Z/(m))×.) This identity was used by Dirichlet in his proof that there are
inﬁnitely many primes p ≡a mod m.
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

<!-- page 14 -->
14
KEITH CONRAD
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
Deﬁnition 4.4. If f ∈L(G) then its Fourier transform bf ∈L( bG) is given by
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
Equation (4.4), called the Fourier inversion formula, lets us recover f from bf.
Remark 4.5. Classically the Fourier transform of a function R →C is another function
R →C. The ﬁnite Fourier transform, however, is deﬁned on the dual group instead of on
the original group. We can also interpret the classical Fourier transform to be a function of
characters. For y ∈R let χy(x) = eixy. Then χy : R →S1 is a character and bf(y) could be
viewed as bf(χy) =
R
R f(x)χy(x) dx, so bf is a function of characters rather than of numbers.
Example 4.6. Let f = δg. Then bf(χ) = χ(g) = χ(g−1). Notice f vanishes at all but one
element of G while bf is nonzero on all of bG.
Example 4.7. Let f = ψ be a character of G. Then bf(χ) = P
g ψ(g)χ(g) = |G|δψ(χ), so
bf = |G|δψ. Here f is nonzero on all of G and bf is nonzero at only one element of bG.
The Fourier transform on R interchanges highly spread and highly peaked Gaussians.
Examples 4.6 and 4.7 suggest a similar phenomenon in the ﬁnite case. The next theorem is
a general result in that direction (a ﬁnite version of Heisenberg uncertainty). It is the only
time (outside Appendix B) when we will use inequalities with characters of ﬁnite abelian
groups.

<!-- page 15 -->
CHARACTERS OF FINITE ABELIAN GROUPS
15
Theorem 4.8. Let f : G →C be a function on a ﬁnite abelian group G that is not identically
zero. Then
(4.5)
| supp f| · | supp bf| ≥|G|,
where supp denotes the support of a function (the set of points where the function is
nonzero).
Proof. We expand f into a Fourier series and make estimates. Since
f(x) =
X
χ∈bG
1
|G|
bf(χ)χ(x),
we have
(4.6)
|f(x)| ≤
X
χ∈bG
1
|G|| bf(χ)| ≤| supp bf|
|G|
max
χ∈bG
| bf(χ)|.
By the deﬁnition of bf(χ),
(4.7)
| bf(χ)| ≤
X
g∈G
|f(g)|.
Let m = maxg∈G |f(g)|, so m > 0 since f is not identically zero.
Then (4.7) implies
| bf(χ)| ≤m| supp f|, and feeding this into (4.6) yields
|f(x)| ≤m| supp f|| supp bf|
|G|
.
Maximizing over all x ∈G implies m ≤m| supp f|| supp bf|/|G|. Divide both sides by m
and the desired inequality drops out.
□
In Examples 4.6 and 4.7, inequality (4.5) is an equality, so Theorem 4.8 is sharp.
Since L(G) is spanned by the characters of G and the delta-functions, linear identities
in L(G) can be veriﬁed by checking them on characters or delta-functions. For example,
deﬁne a Hermitian inner product on L(G) by the rule
(4.8)
⟨f1, f2⟩G =
1
|G|
X
g∈G
f1(g)f2(g) ∈C.
We will prove Plancherel’s theorem for G:
⟨f1, f2⟩G =
1
|G|⟨bf1, bf2⟩bG
for all f1 and f2 in L(G). (Compare to (2.4).) To check this identity, which is linear in
both f1 and f2, it suﬃces to check it when f1 and f2 are characters. By Corollary 4.2, for
characters χ1 and χ2 of G we have
⟨χ1, χ2⟩G =
(
1,
if χ1 = χ2,
0,
if χ1 ̸= χ2.
Since bχ = |G|δχ (Example 4.7),
1
|G|⟨c
χ1, c
χ2⟩bG = |G|⟨δχ1, δχ2⟩bG =
X
χ∈bG
δχ1(χ)δχ2(χ) =
(
1,
if χ1 = χ2,
0,
if χ1 ̸= χ2.

<!-- page 16 -->
16
KEITH CONRAD
This veriﬁes Plancherel’s theorem for G. The special case where f1 = f2 = f is a single
function from G to C gives us Parseval’s formula for G:
(4.9)
X
g∈G
|f(g)|2 =
1
|G|
X
χ∈bG
| bf(χ)|2.
Let’s look at Fourier transforms for functions on a cyclic group. By writing a cyclic
group in the form Z/(m), we can make an isomorphism with the dual group explicit: every
character of Z/(m) has the form χk : j 7→e2πijk/m for a unique k ∈Z/(m) (Exercise 3.1).
The Fourier transform of a function f : Z/(m) →C can be viewed as a function on Z/(m):
(4.10)
bf(k) :=
X
j∈Z/(m)
f(j)χk(j) =
X
j∈Z/(m)
f(j)e−2πijk/m.
This is like viewing the Fourier transform of a function on R as a function on R.
Example 4.9. Let f : Z/(8) →C be a function with period 2 having values 1 and 2. See
Table 4. The Fourier transform of f vanishes except at 0 and 4, which are the multiples of
the frequency of f (how often the period repeats).
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
1
2
1
2
1
2
1
2
bf(n)
12
0
0
0
−4
0
0
0
Table 4.
Example 4.10. Let f : Z/(8) →C have the periodic values 5, 3, 1, and 1. Both f and its
Fourier transform are in Table 5. Now f has frequency 2 (its period repeats twice) and the
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
Table 5.
Example 4.11. Consider a function f : Z/(45) →C with the four successive repeating
values 1, 8, 19, 17 starting with f(0) = 1. It is not a periodic function on Z/(45) since 4
does not divide 45, but the sequence 1, 8, 19, 17 repeats nearly 11 times. (The value of f(44)
is 1.) A calculation of | bf(n)|, which is plotted below, reveals peaks in red at n = 0, 11, 22, 23,
and 34 that are all at least 3 times as high as nearby values. This can’t be shown to scale
near 0, 11, and 34, which is why the values there have arrowheads on top. These peaks in
| bf(n)| occur approximately at multiples of the approximate frequency!

<!-- page 17 -->
CHARACTERS OF FINITE ABELIAN GROUPS
17
0
11
22 23
34
As Examples 4.9 and 4.10 suggest, the Fourier transform of a periodic function on Z/(m)
knows the frequency of the original function by the positions where the Fourier transform
has nonzero values (Exercise 4.4). For nearly periodic functions on Z/(m), the approximate
frequency is reﬂected in where the Fourier transform takes on its largest values. This idea
is used in Shor’s quantum algorithm for integer factorization [2], [3, Chap. 17], where it is
convenient to redeﬁne the Fourier transform (4.10) by dividing the sum by √m, which has
the eﬀect of making the Fourier transform a unitary operator on the functions Z/(m) →C.
See Exercise 4.11.
Exercises.
1. Let G be a ﬁnite abelian group, H be a subgroup of G, and K be a subgroup of bG.
Show
X
h∈H
χ(h) =
(
|H|,
if χ is trivial on H,
0,
otherwise,
X
χ∈K
χ(g) =
(
|K|,
if χ(g) = 1 for all χ ∈K,
0,
otherwise.
2. Let f : Z/(8) →C take the four values a, b, c, and d twice in this order. Compute
bf(n) explicitly and determine some values for a, b, c, and d such that bf(n) is nonzero
for n = 0, 2, and 6, but bf(4) = 0.
3. For a subgroup H of a ﬁnite abelian group G, let δH be the function that is 1 on
H and 0 oﬀof H. Show the Fourier transform of δH is c
δH = |H|δH⊥. How do the
supports of δH and its Fourier transform compare with the inequality (4.5)?
4. Let H be a subgroup of a ﬁnite abelian group G.
(a) Suppose f : G →C is constant on H-cosets (it is H-periodic). For χ ∈bG with
χ ̸∈H⊥, show bf(χ) = 0. Thus the Fourier transform of an H-periodic function on
G is supported on H⊥.
(b) If f : Z/(m) →C has period d where d | m, show bf : Z/(m) →C is supported
on the multiples of m/d. (See Examples 4.9 and 4.10.)
5. Find the analogue of Exercise 2.3 for functions on a ﬁnite abelian group.

<!-- page 18 -->
18
KEITH CONRAD
6. Let f : G →C.
a) Show f(g) ∈R for all g if and only if bf(χ) = bf(χ) for all χ.
b) Show bf(χ) ∈R for all χ if and only if f(g) = f(g−1) for all g.
7. Let G be a ﬁnite abelian group and H be a subgroup. For a function f : G →C,
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
where H⊥is as in Exercise 3.7. Prove this formula in two ways:
a) Copy the classical proof sketched in Section 2 (start with the function F(x) =
P
h∈H f(xh), which is H-periodic so it deﬁnes a function on G/H) to obtain
(4.11)
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
directly on the delta-functions of G. (Corollary 3.7 and Example 4.6 will be useful.)
8. Let Tg : L(G) →L(G) be as in Exercise 3.6.
(a) Show d
Tgf = χ(g) bf for all f ∈L(G).
(b) Show for all f1 and f2 in L(G) that ⟨Tgf1, Tgf2⟩G = ⟨f1, f2⟩G.
9. Let f ∈L(G), so bf is in L( bG) and bbf is in L( bbG).
(a) Viewing bbG as G by Pontryagin duality, show bbf(g) = |G|f(g−1).
(b) For a subgroup H in G, deﬁne the H-average of f and the H-cutoﬀof f to
be the following functions on G:
AvgH(f)(g) =
1
|H|
X
h∈H
f(gh),
CutH(f)(g) =
(
f(g),
if g ∈H,
0,
if g ̸∈H.
Check the identity
\
AvgH(f) = CutH⊥( bf) of functions on bG and then take the
Fourier transform of both sides to get an identity of functions on G, which will be
(4.11) as x varies. (This shows that Poisson summation is essentially equivalent
to the fact that the Fourier transform exchanges the operators AvgH on L(G) and
CutH⊥on L( bG), or equivalently CutH on L(G) and AvgH⊥on L( bG).)
10. Let G be a ﬁnite abelian group. For f1 and f2 in L(G), deﬁne their convolution
f1 ∗f2 : G →C by
(f1 ∗f2)(g) =
X
h∈G
f1(h)f2(gh−1).
(a) Show δg ∗δh = δgh, so L(G) under convolution is a commutative C-algebra
isomorphic to the group ring C[G].
(b) Show \
f1 ∗f2(χ) = bf1(χ) bf2(χ), so the Fourier transform turns convolution into
pointwise multiplication.
(c) Show δg ∗f = Tg−1(f) and χ ∗f = bf(χ)χ in two ways: by a direct calculation
or by computing the Fourier transform of both sides and using (b).

<!-- page 19 -->
CHARACTERS OF FINITE ABELIAN GROUPS
19
(d) For each χ ∈bG, the function hχ : L(G) →C given by hχ(f) = bf(χ) is a
C-algebra homomorphism by (b). Does every C-algebra homomorphism from L(G)
to C arise in this way?
11. On every ﬁnite abelian group G, rescale the deﬁnition of the Fourier transform by
dividing by
p
|G|:
bf(χ) :=
1
p
|G|
X
g∈G
f(g)χ(g).
Verify the following new versions of Fourier inversion and Plancherel’s theorem:
f(g) =
1
√
|G|
P
χ bf(χ)χ(g) and ⟨f1, f2⟩G = ⟨bf1, bf2⟩bG.
Check that this new Fourier transform sends convolution on L(G) (Exercise 4.10)
to multiplication only if we redeﬁne convolution using division by
p
|G|:
(f1 ∗f2)(g) :=
1
p
|G|
X
h∈G
f1(h)f2(gh−1).
5. Structure of finite abelian groups
We will now put characters to work by using them to prove each ﬁnite abelian group is
a direct product of cyclic groups. This result was used in the proof of Theorem 3.13, that
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

<!-- page 20 -->
20
KEITH CONRAD
H is isomorphic to a direct product of cyclic groups, so G is also isomorphic to a direct
product of cyclic groups.
□
Theorem 5.2 can be reﬁned: G is a direct product of cyclic groups with the extra feature
that n1 | n2 | · · · | nk. To prove this, use the fact that the order of each element of a ﬁnite
abelian group G divides the maximal order of the elements of G (Theorem A.3).
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
Table 6. Maximal order of elements of Sn
5. Let G be a ﬁnite abelian group and F be a ﬁeld containing a full set of |G|th roots
of unity. (So x|G| = 1 has |G| solutions in F.) Deﬁne characters of G to be group
homomorphisms χ: G →F × and write the set of all such characters as bG.
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

<!-- page 21 -->
CHARACTERS OF FINITE ABELIAN GROUPS
21
6. Existence of solutions to a Mordell equation mod p
For k ∈Z, an equation of the form y2 = x3 +k is called a Mordell equation. When k ̸= 0,
it is a hard theorem that such an equation has only ﬁnitely many integral solutions (x, y),
which could include having no integral solutions.3 For example, the integral solutions of
y2 = x3 −4 are (2, ±2) and (5, ±11), and y2 = x3 −5 has no integral solutions. Using
characters, we will show for each k ∈Z that the congruence y2 ≡x3 + k mod p modulo a
prime p always has a solution.
For a character χ on (Z/(p))×, extend χ to Z/(p) by setting χ(0) = 0. Then χ(ab) =
χ(a)χ(b) for all a, b ∈Z/(p).
Lemma 6.1. If p is prime and d | (p −1), then there is a character χ of (Z/(p))× with
order d, and for each a ∈Z/pZ,
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
The character group of (Z/(p))× is cyclic of order p −1 by Theorem 3.11, so (Z/(p))×
has a character of order d. Call such a character χ. For each a ∈Z/(p), we’ll show that
1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 has the same values as in (6.1).
• If a is a nonzero dth power mod p, say a ≡bd mod p, then χ(a) = χ(bd) = χ(b)d = 1
since χd is identically 1 on (Z/(p))×, so 1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 = d.
• If a ≡0 mod p then χ(a) = 0, so 1 + χ(a) + χ(a)2 + · · · + χ(a)d−1 = 1.
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
3At k = 0, the equation is y2 = x3, which has inﬁnitely many integral solutions (x, y) = (t2, t3) for t ∈Z.
4See https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf for many proofs of this.

<!-- page 22 -->
22
KEITH CONRAD
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
5If F is any ﬁeld, the solutions of y2 = x3 in F are all of the form (t2, t3) as t runs over F: if x ̸= 0, set
t = y/x ̸= 0, so t2 = y2/x2 = x3/x2 = x and t3 = y3/x3 = y3/y2 = y. That shows all solutions (x, y) where
x ̸= 0 have the form (t2, t3) where t ∈F ×, and (0, 0) also has that form with t = 0.
6See Corollary 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

<!-- page 23 -->
CHARACTERS OF FINITE ABELIAN GROUPS
23
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

<!-- page 24 -->
24
KEITH CONRAD
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
7. Dual Homomorphisms
The set Hom(G1, G2) of all homomorphisms from the abelian group G1 to the abelian
group G2 forms an abelian group under pointwise multiplication
Theorem 7.1. Let G1 and G2 be ﬁnite abelian groups. For a homomorphism f : G1 →G2,
set f∗: bG2 →bG1 by f∗(χ) = χ◦f. Then f∗is a group homomorphism and the map sending
f to f∗gives a group isomorphism
Hom(G1, G2) ∼= Hom( bG2, bG1).
Proof. If f : G1 →G2 is a homomorphism and χ ∈bG2, then for g and g′ in G1 we have
χ(f(gg′)) = χ(f(g)f(g′)) = χ(f(g))χ(f(g′)),
so f∗(χ) := χ ◦f lies in bG1.
Thus we get the map Hom(G1, G2) →Hom( bG2, bG1) as
advertised. Check (ff′)∗= f∗(f′)∗, so f 7→f∗is a homomorphism.
Repeating this idea leads to a group homomorphism Hom( bG2, bG1) →Hom( bbG1, bbG2). By
Pontryagin duality it is a homomorphism Hom( bG2, bG1) →Hom(G1, G2) and the composite
Hom(G1, G2) →Hom( bG2, bG1) →Hom(G1, G2)
turns out to be (after unwinding deﬁnitions, left to the reader) the identity function. There-
fore our original map Hom(G1, G2) →Hom( bG2, bG1) is a group isomorphism.
□
The homomorphism f∗: bG2 →bG1 is called the dual homomorphism to f.
Exercises.
1. For a homomorphism f : G1 →G2, show (ker f)⊥= im f∗in bG1 and (im f)⊥=
ker f∗in bG2.
2. Show the isomorphism Hom(G, G) ∼= Hom( bG, bG) in Theorem 7.1 coming from the
identity map on G associates g 7→gm in Hom(G, G) with χ 7→χm in Hom( bG, bG).
7See Theorem 2.5 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.
8See Corollary 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

<!-- page 25 -->
CHARACTERS OF FINITE ABELIAN GROUPS
25
8. Abelian group determinants
Consider a square n × n matrix where each row is a cyclic shift of the previous row:
(8.1)







X0
X1
X2
. . .
Xn−1
Xn−1
X0
X1
. . .
Xn−2
Xn−2
Xn−1
X0
. . .
Xn−3
...
...
...
...
...
X1
X2
X3
. . .
X0







Its determinant is called a circulant. When n is 2 and 3, the circulants are

X0
X1
X1
X0
 = X2
0 −X2
1
and

X0
X1
X2
X2
X0
X1
X1
X2
X0

= X3
0 + X3
1 + X3
2 −3X0X1X2.
These factor as
(X0 + X1)(X0 −X1)
and
(X0 + X1 + X2)(X0 + ωX1 + ω2X2)(X0 + ω2X1 + ωX2),
where ω = e2πi/3.
If we think about the variables Xi as being indexed by Z/(n) then the (i, j) entry of (8.1)
is Xj−i. More generally, for a ﬁnite group G, index a set of variables Xg by G and form the
matrix indexed by G×G where the (g, h) entry is Xgh−1. (The circulant is the determinant
of the matrix (Xj−i) = (Xi−j)⊤.) The determinant is called the group determinant of G:
(8.2)
∆(G) = det(Xgh−1).
This is a homogeneous polynomial of degree |G| with integer coeﬃcients. A circulant is the
group determinant of a cyclic group.
Circulants of order 2 and 3 are products of linear factors with roots of unity as coeﬃcients.
Dedekind and Burnside each proved the same property for the group determinant of every
ﬁnite abelian group, but Dedekind’s approach revealed more structure in the factors: the
roots of unity in a given linear factor are the values of one of the characters of the group!
Theorem 8.1 (Dedekind). If G is a ﬁnite abelian group then its group determinant factors
into linear factors over the complex numbers:
det(Xgh−1) =
Y
χ∈bG

X
g∈G
χ(g)Xg

.
Proof. We will realize (Xgh−1) as the matrix for a linear transformation and then ﬁnd its
diagonalization to compute its determinant.
Let V = C[G] be the group ring of G. For each v ∈V , deﬁne the linear map Lv : V →V
to be (left) multiplication by v: Lv(x) = vx. We will compute the matrix for Lv with
respect to the basis G of V . Writing v = P
g∈G agg we have for each h ∈G
Lv(h) =
X
g∈G
aggh =
X
g∈G
agh−1g,
so the matrix for Lv with respect to the basis G is (agh−1).

<!-- page 26 -->
26
KEITH CONRAD
Another basis for C[G] is the set of formal sums P
g∈G χ(g)g, one for each character χ
of G: the number of such sums has the right size to be a basis, and for a linear relation
X
χ
cχ

X
g∈G
χ(g)g

= 0
in C[G] we get P
χ cχχ(g) = 0 for all g (the coeﬃcient of each g is 0), so every cχ is 0 by
Fourier inversion.
This new basis of C[G], indexed by the characters, consists of eigenvectors for Lv:
Lv
 X
h∈G
χ(h)h
!
=

X
g∈G
agg


 X
h∈G
χ(h)h
!
=
X
k∈G

X
gh=k
agχ(h)

k
=
X
k∈G

X
g∈G
agχ(g−1)χ(k)

k
=

X
g∈G
agχ(g−1)


 X
k∈G
χ(k)k
!
.
Since det(Lv) is the product of the eigenvalues of Lv for an eigenbasis,
det(agh−1) =
Y
χ∈bG

X
g∈G
agχ(g)

.
If we interchange the roles of χ and χ in this product then we obtain
det(agh−1) =
Y
χ∈bG

X
g∈G
agχ(g)

.
Thus the multivariable polynomials det(Xgh−1) and Q
χ∈bG
P
g∈G χ(g)Xg are equal on all of
Cn, so they must be the same polynomial.
□
Example 8.2. Taking G = Z/(n) and ζn = e2πi/n,

X0
X1
. . .
Xn−1
Xn−1
X0
. . .
Xn−2
...
...
...
...
X1
X2
. . .
X0

=
n−1
Y
j=0
 n−1
X
k=0
ζjk
n Xk
!
=
n−1
Y
j=0
(X0 + ζj
nX1 + · · · + ζ(n−1)j
n
Xn−1).
Applications of the factorization of the group determinant for abelian (not necessarily
cyclic) groups can be found in [4, §5.5].

<!-- page 27 -->
CHARACTERS OF FINITE ABELIAN GROUPS
27
If G is a nonabelian group then its group determinant has an irreducible factor with
degree greater than 1. Studying irreducible factors of the group determinant for nonabelian
G led Frobenius to discover representation theory and the correct extension of the notion
of a character to (ﬁnite) nonabelian groups.
Exercises.
1. Check the factorization of the group determinant for Z/(4).
2. Compute and factor the group determinant of Z/(2) × Z/(2).
3. If G is nonabelian, show the polynomial ∆(G) in (8.2) is divisible by P
g∈G Xg, and
more generally by P χ(g)Xg for each homomorphism χ: G →S1.
9. Eigenspace decomposition
In high school math we ﬁrst learn about even and odd functions R →R: an even function
satisﬁes f(−x) = f(x) for all x and an odd function satisﬁes f(−x) = −f(x) for all x. For
example, x2 and cos x are even while x3 and sin x are odd.
Every function R →R is
expressible as a sum of an even and odd function:
(9.1)
f(x) = f(x) + f(−x)
2
+ f(x) −f(−x)
2
,
where the ﬁrst term on the right is even and the second term on the right is odd. Moreover,
that expression as a sum of even and odd functions is unique: if f(x) = E(x) + O(x)
where E and even and O is odd, then f(−x) = E(−x) + O(−x) = E(x) −O(x), so
f(x) + f(−x) = 2E(x) and f(x) −f(−x) = 2O(x). Therefore E(x) = (f(x) + f(−x))/2
and O(x) = (f(x) −f(−x))/2. The formulas for the even and odd parts of f are based on
averaging and anti-averaging f(x) and f(−x).
This type of decomposition occurs in other settings where there is an additive mapping
that iterates twice to the identity map (like f(x) 7→f(−x) above, where f(−(−x)) = f(x)).
Here are two more examples.
(1) Complex conjugation (where z = z) leads to an “even/odd” decomposition of each
complex number z as the unique sum of a real number (where w = w) and a purely
imaginary number (where w = −w): for z = a + bi, z = a −bi and
z = z + z
2
+ z −z
2
= a + bi.
(2) The matrix transpose (where M⊤⊤= M) leads to the unique expression of each
square matrix over a ﬁeld not of characteristic 2 as a sum of matrices that are
symmetric (M⊤= M) and skew-symmetric (M⊤= −M):
A = A + A⊤
2
+ A −A⊤
2
.
(3) The swap operator on real or complex-valued functions of two variables (f(x, y) 7→
f(y, x)) leads to the unique expression of each such function as a sum of functions
that are symmetric (F(y, x) = F(x, y)) and anti-symmetric (F(y, x) = −F(x, y)):
f(x, y) = f(x, y) + f(y, x)
2
+ f(x, y) −f(y, x)
2
.

<!-- page 28 -->
28
KEITH CONRAD
We will now see an analogue of this for ﬁnite abelian groups acting on complex vector
spaces. For a group G and complex vector space V , a linear action of G on V 9 is an action
G × V →V where v 7→gv is linear for each g ∈G: g(v + w) = gv + gw and g(cv) = c(gv)
for all g ∈G, v and w in V , and c ∈C.
Example 9.1. When V is the space of all functions C →C, the group µn of nth roots of
unity acts on V by interior scaling: for r ∈µn and f ∈V , let the function r · f be given by
(r · f)(z) = f(rz).
For instance, ((−1) · f)(z) = f(−z).
This is a linear action of µn on V : r·(f1 +f2) = r·f1 +r·f2 for all r ∈µn and f1, f2 ∈V ,
and r · (cf) = c(r · f) for all r ∈µn, c ∈C, and f ∈V .
Example 9.2. When V is the space of all functions C →C, the group µn of nth roots of
unity acts on V by exterior scaling: for r ∈µn and f ∈V , let the function rf be given by
(r · f)(z) = rf(z).
For instance, ((−1) · f)(z) = −f(z).
This is a linear action of µn on V that is not the same as the action in the previous
example (when n ≥2).
Theorem 9.3. Let G be a ﬁnite abelian group and V be a complex vector space on which
G acts linearly. For a character χ of G, set V (χ) = {v ∈V : gv = χ(g)v for all g ∈G}.
This is a subspace of G and
V =
M
χ∈bG
V (χ).
We call V (χ) the χ-eigenspace of V : it’s the elements of V on which the eﬀect of each g
in G is given by multiplication by the number χ(g). So V (χ) is a common eigenspace of all
g ∈G, where their eigenvalues are the numbers χ(g) associated to a single character of G.
For instance, V (1G) = {v ∈V : gv = v for all g ∈G} is the set of ﬁxed points for all g.
Proof. It’s left to the reader to check each V (χ) is a subspace of V . To show V is the direct
sum of all V (χ), ﬁrst we’ll show V = P
χ V (χ) and then we’ll show the sum is direct.
For v ∈V , here is its piece in V (χ): set
(9.2)
vχ =
1
|G|
X
g∈G
χ(g)gv.
We’ll show vχ ∈V (χ) for all χ and v = P
χ vχ, so V = P
χ V (χ).
9This is called a representation of G on V .

<!-- page 29 -->
CHARACTERS OF FINITE ABELIAN GROUPS
29
Showing vχ ∈V (χ) means showing hvχ = χ(h)vχ for each h ∈G. From the deﬁnition of
vχ and linearity of the action of G on V , for each h ∈G we have
hvχ =
1
|G|
X
g∈G
χ(g)(hg)v
=
1
|G|
X
g∈G
χ(h−1g)gv
=
1
|G|
X
g∈G
χ(h−1)χ(g)gv
= χ(h)
|G|
X
g∈G
χ(g)gv
= χ(h)vχ.
The vχ’s sum up to v:
X
χ
vχ =
X
χ
1
|G|
X
g∈G
χ(g)gv =
1
|G|
X
g∈G
X
χ
χ(g)gv =
1
|G|
X
g∈G
 X
χ
χ(g)
!
gv.
The inner sum is 0 unless χ is trivial, at which the inner sum is | bG|, which equals |G|, so
P
χ vχ = (1/|G|)|G|v = v. Thus V = P
χ V (χ).
To show the sum of the subspaces V (χ) is a direct sum means showing that if P
χ wχ = 0
for wχ ∈V (χ), then each wχ is 0. Pick g ∈G and ψ ∈bG. Let g act on both sides of the
equation 0 = P
χ wχ, so 0 = P
χ gwχ = P
χ χ(g)wχ since wχ ∈V (χ). Multiplying through
this equation by ψ(g), 0 = P
χ χ(g)ψ(g)wχ. Sum both sides over all g in G:
0 =
X
g
X
χ
χ(g)ψ(g)wχ =
X
χ
 X
g
χ(g)ψ(g)
!
wχ.
The coeﬃcient of wχ on the right is 0 unless χ = ψ, when the coeﬃcient is |G|. Therefore
0 = |G|wψ. Since |G| ̸= 0 in C, we get wψ = 0 and this holds for each ψ in bG. That proves
the decomposition V = P
χ V (χ) is a direct sum decomposition.
□
Example 9.4. Let |G| = 2, with G = {1, ε} and bG = {1G, χ}.
Then χ(1) = 1 and
χ(ε) = −1, so (9.2) in this case says each v ∈V is v1G + vχ, where v1G = (v + εv)/2 and
vχ = (v −εv)/2, which satisy εv1G = v1G and εvχ = −vχ. This decomposition of v into two
parts is just like the even/odd decompositions at the start of this section.
Example 9.5. Consider the interior scaling action of µn on functions C →C in Example
9.1. The characters of µn are the power functions χj(r) = rj for j = 0, . . . , n −1 and
V (χj) = {f ∈V : f(rz) = rjf(z) for all z ∈C}. Each f : C →C is a sum Pn−1
j=0 fj where
fj(rz) = rjf(z) for all z ∈C and by (9.2)
(9.3)
fj(z) = 1
n
X
r∈µn
χj(r)(r · f)(z) = 1
n
X
r∈µn
r−jf(rz).
When n = 2 this says f(z) = f0(z) + f1(z) where f0(z) = (f(z) −f(−z))/2 is even and
f1(z) = (f(z) −f(−z))/2 is odd.

<!-- page 30 -->
30
KEITH CONRAD
When n = 4 this says f(z) = f0(z) + f1(z) + f2(z) + f3(z) where f0(iz) = f0(z), f1(iz) =
if1(z), f2(iz) = −f2(z), and f3(z) = −if3(z). Here are formulas for each of these functions,
as special cases of (9.3):
f0(z) = f(z) + f(iz) + f(−z) + f(−iz)
4
,
f1(z) = f(z) −if(iz) −f(−z) + if(−iz)
4
,
f2(z) = f(z) −f(iz) + f(−z) −f(−iz)
4
,
f3(z) = f(z) + if(iz) −f(−z) −if(−iz)
4
.
Example 9.6. For the exterior scaling action of µn on functions C →C in Example 9.2,
where µn has characters χj(r) = rj for j = 0, . . . , n −1, the χj-eigenspace
V (χj) = {f ∈V : rf(z) = rjf(z) for all z ∈C}
vanishes for nontrivial χj: when 1 ≤j ≤n −1 and r is a nontrivial nth root of unity,
r ̸= rj, so the only way rf(z) = rjf(z) is if f(z) = 0. Easily V = V (1) = {f ∈V : rf(z) =
rf(z) for all z ∈C}.
As an example, take n = 2 and R: C →C by R(z) = −z, so R has order 2. (If we view
C as R2 then this is a 180-degree rotation of the plane.) The group G = {I, R} of order 2
acts linearly on C and the whole space “looks odd” under the eﬀect of R: when χ is the
nontrivial character of G, C(1) = C and C(χ) = {0}.
Exercises.
1. Let V = {aX + bX2 : a, b ∈C}, on which G = Z/(4) acts by interior scaling:
(r · f)(X) = f(rX). Let χj(r) = rj for 0 ≤j ≤3 and show V (χ0) = V (χ3) = {0}
while V (χ1) = CX and V (χ2) = CX2.
2. This exercise builds on Exercise 1.1, which is about characters of Z/(2) × Z/(2).
a) When Z/(2) × Z/(2) acts linearly on a complex vector space V , compute vχ
for each v ∈V and character χ of Z/(2) × Z/(2).
b) Let V = C(X) be the rational functions over C and deﬁne two linear mappings
σ: V →V and τ : V →V by σ(f(X)) = f(−X) and τ(f(X)) = f(1/X). Each has
order 2 and στ = τσ is the linear map f(X) 7→f(−1/X). The group G = ⟨σ, τ⟩=
{1, σ, τ, στ} is isomorphic to Z/(2) × Z/(2), so the action of G on C(X) can be
regarded as a linear action of Z/(2) × Z/(2) on C(X).
For each f(X) ∈C(X), compute formulas for fχ where χ runs through the
characters of G and check directly that the eﬀect of g on fχ(X) is χ(g)f(X) for
each g ∈G.
Appendix A. All orders and maximal order
We will use characters of ﬁnite abelian groups to prove that in a ﬁnite abelian group G,
the order of each element of G divides the maximal order of the elements of G. Although
this result can proved in a shorter way without characters, the point here is to see characters
used.

<!-- page 31 -->
CHARACTERS OF FINITE ABELIAN GROUPS
31
Lemma A.1. For positive d and m with d | m, the natural reduction (Z/(m))× →(Z/(d))×
is onto: when (a, d) = 1, there is b such that b ≡a mod d and (b, m) = 1.
Proof. Let ed be the product of the prime powers in m whose primes divide d, so m = edn
with (ed, n) = 1. (For example, if m = 90 and d = 6 then ed = 18 and n = 5.) Then d | ed.
By the Chinese remainder theorem we can ﬁnd b ∈Z satisfying
b ≡a mod ed,
b ≡1 mod n.
Then b ≡a mod d and b is relatively prime to m since it is relatively prime to d (a factor
of ed) and to n.
□
Lemma A.2. Let G be a ﬁnite abelian group. If x ∈G has order m and y ∈G has order
n then there is a character χ: G →S1 such that χ(x) has order m and χ(y) has order n.
Proof. The subgroup ⟨x⟩is cyclic of order m, so there is an isomorphism χ: ⟨x⟩∼= µm. In
particular, χ(x) has order m. Following the proof of Lemma 3.2, we can extend χ to a
character on ⟨x, y⟩(and then all the way up to G) by sending y to a solution z ∈S1 of the
equation zd = χ(yd), where d ≥1 is minimal such that yd ∈⟨x⟩. We will show z can be
picked to have order n in S1.
Since yn = 1 ∈⟨x⟩, d divides n.
Then yd has order n/d, so χ(yd) has order n/d
because χ is one-to-one on ⟨x⟩. Write χ(yd) = e2πiℓ/(n/d) = e2πiℓd/n, where (ℓ, n/d) = 1.
By Lemma A.1, there is an ℓ′ ≡ℓmod n/d such that (ℓ′, n) = 1. Since ℓ′d ≡ℓd mod n,
χ(yd) = e2πiℓ′d/n.
Set z = e2πiℓ′/n, which has order n.
Since zk = χ(yd), we can set
χ(y) = z.
□
Lemma A.2 does not extend to more than two arbitrary elements in G. For instance,
if G = µ2 × µ2 then no character on G sends all three non-identity elements in G to −1.
(Why?)
Theorem A.3. Let G be a ﬁnite abelian group. The order of each element in G divides
the maximal order of the elements of G.
Proof. We will show that when G has elements of orders m and n, there is an element of
G of order [m, n]. Then if m is the maximal order among all the elements of G, and n is
the order of some element of G, [m, n] is the order of some element so [m, n] ≤m. That
inequality can only occur when [m, n] = m, so n | m, which is what we want to show.
By Lemma A.2, there is a character χ on G such that χ(g) has order m and χ(h) has
order n. Write χ(g) = e2πia/m and χ(h) = e2πib/n, where (a, m) = 1 and (b, n) = 1.
The roots of unity e2πi/m and e2πi/n are in χ(G). For instance, letting aa′ ≡1 mod m,
χ(ga′) = χ(g)a′ = e2πiaa′/m = e2πi/m. The argument for e2πi/n is similar. Write mu + nv =
(m, n) for some integers u and v, so the equation mn = [m, n](m, n) can be rewritten as
1
[m, n] = (m, n)
mn
= mu + nv
mn
= u 1
n + v 1
m.
Thus
e2πi/[m,n] = (e2πi/n)u(e2πi/m)v ∈χ(G),
say e2πi/[m,n] = χ(t). The order of t in G is divisible by the order of χ(t) in S1, so t has
order divisible by [m, n]. Thus, raising t to a suitable power, we obtain an element of G
with order [m, n].
□

<!-- page 32 -->
32
KEITH CONRAD
Appendix B. Functions of Two Variables
When analyzing a function of several variables, it is a common theme to decompose it
into a sum of products of functions of one variable. For instance, to solve a PDE like the
heat equation ∂tu −c∂2
xu = 0, ﬁrst separable solutions of the form u(x, t) = g(x)h(t) are
classiﬁed. It is too much to hope that a general solution is separable, but in nice situations
there are theorems guaranteeing that a general solution can be written as an inﬁnite series
of separable solutions: u(x, t) = P
n≥1 gn(x)hn(t).
This is where expansions in Fourier
series ﬁrst appeared in mathematics.
Using characters, and in particular Parseval’s formula, we will give an example of a
function of two variables that is provably not a sum of products of functions of one variable.
Lemma B.1. Fix a positive integer N. For vectors (z1, . . . , zN) and (w1, . . . , wN) in CN,

N
X
j,k=1
e−2πijk/Nzjwk

≤
√
N


N
X
j=1
|zj|2


1/2  N
X
k=1
|wk|2
!1/2
.
Proof. Write the double sum as an iterated single sum:
N
X
j,k=1
e−2πijk/Nzjwk =
N
X
j=1
 N
X
k=1
e−2πijk/Nwk
!
zj =
N
X
j=1
bf(j)zj,
where f : Z/(N) →C by f(k) = wk. The right side brings in the Fourier transform of f,
where we think about bf as a function on Z/(N) by identifying Z/(N) with its own dual
group as in Exercise 3.1.
Using the Cauchy–Schwarz inequality,

N
X
j=1
bf(j)zj

≤


N
X
j=1
| bf(j)|2


1/2 

N
X
j=1
|zj|2


1/2
.
By Parseval’s formula on Z/(N), PN
j=1 | bf(j)|2 = N PN
k=1 |f(k)|2 = N PN
k=1 |wk|2.
□
Theorem B.2. It is impossible to write
e2πixk =
X
n≥1
gn(x)hn(k),
where x ∈[0, 1], k ∈Z, the functions gn : [0, 1] →C and hn : Z →C are each bounded, and
P
n≥1 ||gn||sup||hn||sup < ∞, where || · ||sup is the sup-norm on bounded functions.
Proof. Assume there is a series expansion
e2πixk =
X
n≥1
gn(x)hn(k)
for all x ∈[0, 1] and k ∈Z, where c := P
n≥1 ||gn||sup||hn||sup < ∞. Then the series is
absolutely convergent for all x and k. Pick N ≥1 and x1, . . . , xN ∈[0, 1]. Then
N
X
j,k=1
e−2πijk/Ne2πixjk =
N
X
j,k=1
e−2πijk/N

X
n≥1
gn(xj)hn(k)

=
X
n≥1
N
X
j,k=1
e−2πijk/Ngn(xj)hn(k).

<!-- page 33 -->
CHARACTERS OF FINITE ABELIAN GROUPS
33
Then

N
X
j,k=1
e−2πijk/Ne2πixjk

=

X
n≥1
N
X
j,k=1
e−2πijk/Ngn(xj)hn(k)

≤
X
n≥1

N
X
j,k=1
e−2πijk/Ngn(xj)hn(k)

≤
X
n≥1
√
N


N
X
j=1
|gn(xj)|2


1/2  N
X
k=1
|h(k)|2
!1/2
by Lemma B.1. Since PN
j=1 |gn(xj)|2 ≤N||gn||2
sup and PN
k=1 |hn(k)|2 ≤N||hn||2
sup,

N
X
j,k=1
e−2πijk/Ne2πixjk

≤
X
n≥1
√
N
√
N||gn||sup
√
N||hn||sup ≤N3/2c.
Now set xj = j/N:
N
X
j,k=1
e−2πijk/Ne2πixjk =
N
X
j,k=1
e−2πijk/Ne2πijk/N = N2,
so N2 ≤N3/2c for all N ≥1. This is false when N is large enough (N > c2).
□
This theorem says we can’t write e2πixk = P
n≥1 gn(x)hn(k) where the functions gn and hn
are bounded and the series converges absolutely (since convergence of P
n≥1 ||gn||sup||hn||sup
implies absolute convergence). Could there be such a series representation of e2πixk that is
conditionally convergent?
References
[1] A. Terras, “Fourier Analysis on Finite Groups and Applications,” Cambridge Univ. Press, Cambridge,
1999.
[2] P. Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum
Computer, http://arxiv.org/abs/quant-ph/9508027v2.
[3] W. Trappe and L. Washington, “Introduction to Cryptography with Coding Theory,” Prentice-Hall,
Upper Saddle River, NJ 2002.
[4] L. Washington, “Introduction to Cyclotomic Fields,” 2nd ed., Springer-Verlag, New York, 2000.
[5] N. Wiener, “I am a Mathematician,” MIT Press, Cambridge, 1964.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*