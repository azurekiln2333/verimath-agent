# Kummer's Lemma

> **Source**: https://kconrad.math.uconn.edu/blurbs/kummer.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
KUMMER’S LEMMA
KEITH CONRAD
Let p be an odd prime and ζ = ζp be a primitive pth root of unity. In the ring Z[ζ], the
pth power of every element is congruent to a rational integer mod p, since
(c0 + c1ζ + · · · + cp−2ζp−2)p ≡c0 + c1 + · · · + cp−2 mod p.
The number p is not prime in Z[ζ], as (p) = (1 −ζ)p−1, so congruence mod p is much
stronger than congruence mod 1 −ζ, where all classes have integer representatives.
Of course not every element of Z[ζ] that is congruent to a rational integer mod p is a
pth power, but Kummer discovered a case when this converse statement is true, for certain
primes and certain algebraic integers.
Theorem 1 (Kummer’s lemma). Let p be a regular prime and u ∈Z[ζ]× with u ≡a mod
pZ[ζ] for some rational integer a. Then u = vp for some v ∈Z[ζ]×.
This was used by Kummer to prove Case II of FLT for regular primes.1 The hypothesis
in Kummer’s lemma that u mod pZ[ζ] is congruent to an integer a is reformulated in the
appendix to eliminate the role of a.
For our purposes, an odd p will be called regular if the Bernoulli numbers B2, B4, . . . , Bp−3
are all prime to p. This is not the most conceptual description of regularity, but it is the form
in which we will be using the property in the proof. The usual formulation of regularity, in
terms of class numbers, allows for other proofs of Kummer’s lemma, by class ﬁeld theory
[3, §6, Chap. 13] or by p-adic L-functions [4, Theorem 5.36].
We will give here a p-adic proof of Kummer’s lemma, modifying the argument of Faddeev
from [1, §6, Chap. 5].
The proof of Kummer’s lemma requires knowing something about the unit group of Z[ζ].
Some obvious units in Z[ζ] are
εk
def
= ζk −1
ζ −1 ≡k mod ζ −1
for 1 ≤k ≤p −1. While ε1 = 1, the units εk for k > 1 are more interesting.
There is a convenient way to rewrite the εk. First, since ζ has odd order, some power of it
is a square root of ζ; indeed, ζ(p+1)/2 is a square root of ζ. However, η def
= −ζ(p+1)/2 turns out
to be the more convenient choice of square root, since when ζ = e2πi/p, ζ(p+1)/2 = −eiπ/p
while η = eiπ/p, the “nicer” square root of e2πi/p. Furthermore, choosing ζ = e2πi/p,
εk = η2k −1
η2 −1 = ηk
η · ηk −η−k
η −η−1 = ηk−1 sin(kπ/p)
sin(π/p) .
Let δk = sin(kπ/p)/ sin(π/p), so δk is a real (positive) unit.
The equation εk = ηk−1δk can be generalized to any unit of Z[ζ].
Lemma 2. Every unit u of Z[ζ] has the form u = ζru′, where u′ is a real unit.
1See https://kconrad.math.uconn.edu/blurbs/gradnumthy/fltreg.pdf.
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. Suppose u = ζru′. Then u = ζ−ru′, so we can divide and get u/u = ζ2r. This
suggests the idea of considering the ratio u/u and proving it is a root of unity. Well, u/u
and all of its Q-conjugates have absolute value 1, so it is a root of unity. Being in Q(ζ), we
must have u/u = ±ζa. If we can show the plus sign holds, then write a ≡2b mod p and set
u′ = u/ζb to end the proof.
Let’s work mod (1−ζ). Since all powers of ζ are congruent to 1, u ≡u, so 1 ≡±ζa ≡±1.
Since 1 ̸≡−1 mod (1 −ζ), the plus sign holds.
□
Let K = Q(ζ), Kp = Qp(ζ), A = Z[ζ], Ap = Zp[ζ], σj(ζ) = ζj, τ = σ−1 is complex
conjugation. Denote the “real” elements of Ap, i.e. the elements ﬁxed by τ, as A+
p . (A
similar deﬁnition can be made for K+
p , but we will only be focusing on real elements of Ap.)
The Teichm¨uller lift of an integer k to Zp will be written ω(k).
Lemma 3. In Qp(ζ), Xp−1 + p splits completely and there is a bijection between roots π of
Xp−1 + p and nontrivial pth roots of unity ζπ, by
π ≡ζπ −1 mod π2.
Proof. See [3, Lemma 3.1, Chap. 14].
□
Fix a choice of ζ, then ﬁx a root π of Xp−1 + p by π ≡ζ −1 mod π2.
Write τ(π) = θπ, where θp−1 = 1. Since π = τ 2(π) = θ2π, θ = ±1. Since τ(π) ̸= π,
τ(π) = −π. Thus π2 ∈A+
p .
Since p is odd, the minimal polynomial of π2 over Qp is X(p−1)/2 + p and Ap = Zp[π].
Lemma 4. A+
p = Zp[π2].
Proof. Left to the reader.
□
Set m = (p −1)/2 , so Zp[π2] has Zp-basis {1, π2, π4, . . . , π2(m−1)}.
Lemma 5. For x, y ≡1 mod π, | log x −log y| ≤|x −y|.
Proof. Since log x −log y = log(x/y) and |x −y| = |x/y −1|, without loss of generality
y = 1. Then x ≡1 mod π ⇒| log x| ≤|x −1|. We want to show that for k ≥1,

(x −1)k
k
 ≤|x −1|,
which is equivalent to
|x −1| ≤|k|1/(k−1).
Since |x −1| ≤|π| = (1/p)1/(p−1), we’re done.
□
Corollary 6. For u ∈Z[ζ]× with u ≡a mod p for some rational integer a, log(up−1) ∈
pA+
p .
Proof. Since up−1 ≡1 mod p, | log(up−1)| ≤|up−1 −1| ≤1/p, so log(up−1) ∈pAp. Writing
u = ζru′ for real u′ by Lemma 2, log(up−1) = log((u′)p−1) ∈A+
p .
□
Given a unit u ∈Z[ζ]×, write log(up−1) = Pm−1
i=0 biπ2i. A trace calculation shows b0 = 0:
for 1 ≤k ≤p −1,
TrKp/Qp(πk) =
p−1
X
j=1
σj(πk) =


p−1
X
j=1
ω(j)k

πk = 0.

<!-- page 3 -->
KUMMER’S LEMMA
3
So
p −1
2
b0 = TrKp/Qp(log(up−1)) = log(NKp/Qp(up−1)) = log(NK/Q(up−1)) = log(1) = 0.
For 2 ≤k ≤m, write log(εp−1
k
) = Pm−1
i=1 cikπ2i for some cik ∈Zp. The subscripts i and
k both run over sets of size m −1.
The next theorem is the technical heart of our preparations for Kummer’s lemma.
Theorem 7. The numbers {1, log(εp−1
2
), . . . , log(εp−1
m )} form a Zp-basis of A+
p precisely
when p is regular.
Proof. Since {1, π2, . . . , π2(m−1)} is a Zp-basis of A+
p , we shall check that the Zp-transition
matrix (cik) between {π2, . . . , π2(m−1)} and {log(εp−1
2
), . . . , log(εp−1
m )} has determinant in
Z×
p , or rather than its determinant mod p is nonzero.
Write
εp−1
k
= εp
k
ζ −1
ζk −1.
Since εk ≡k mod π,
εp
k ≡kp mod πp
≡kp mod πp−1 = −p
≡k mod p.
Therefore εp−1
k
≡k(ζ −1)/(ζk −1) mod p, so by Lemma 5,
log(εp−1
k
) ≡log(k(ζ −1)/(ζk −1)) mod p.
Let’s use the Dwork series E(X) = eX+Xp/p to express ζ in terms of π [3, Theorem 3.2,
Chap. 14]: E(π) = ζ and E(ω(k)π) = ζk. We will write ω(k)π as πk. So
εp−1
k
≡k ζ −1
ζk −1 mod p
= k E(π) −1
E(πk) −1
≡ω(k) E(π) −1
E(πk) −1 mod p
=
πk
E(πk) −1 · E(π) −1
π
.
Since ζk = E(πk) ≡1 + πk mod π2, we have
(1)
log(εp−1
k
) ≡log
E(π) −1
π

−log
E(πk) −1
πk

mod p.
Writing E(X) = P anXn, (E(π) −1)/π = P
n≥1 anπn−1. When is anπn−1 ≡0 mod p?
In [3, p. 322], en denotes anπn and some lower bound estimates on ordp(en) are proved
that imply ordp(anπn−1) ≥1 if n ≥p3/(p −1)2. But the lower bound is true for n ≥p.
Rather than work with the lower bound estimates in [3] to squeeze out this more delicate
information, we will use [2, Theorem 3.5], which gives a sharper lower bound on ordp(an).

<!-- page 4 -->
4
KEITH CONRAD
For n ≥p2, that bound is
ordp(an) ≥n
p2

2 +
1
p −1

−
1
p −1 ≥

2 +
1
p −1

−
1
p −1 = 2,
so ordp(anπn−1) ≥2 + (n −1)/(p −1) ≥2 + (p2 −1)/(p −1) = p + 3 ≥5. If p ≤n ≤p2 −1
then an is a p-adic integer since E(X) and the Artin–Hasse series have the same coeﬃcients
up through degree p2−1, so ordp(anπn−1) ≥(n−1)/(p−1) ≥(p−1)/(p−1) = 1. Therefore
E(π) −1
π
≡
p−1
X
n=1
anπn−1 ≡
p−1
X
n=1
πn−1
n!
mod p
since an = 1/n! for 0 ≤n ≤p −1. Thus
(2)
log
E(π) −1
π

≡log
 p−1
X
n=1
πn−1
n!
!
mod p.
The sum Pp−1
n=1 πn−1/n! looks like a truncation of the full series (eπ −1)/π. But the latter
makes no sense, since π is not in the disc of convergence of eX. Nevertheless, progress will
come from looking at the formal power series log((eX −1)/X).
Since we are computing logarithms only modulo p, we can truncate log series. To deter-
mine how far out we need to go, let’s ﬁgure out when |(x −1)n/n| ≤|p| for |x −1| ≤|π|.
Lemma 8. For n ≥p + 1, |πn/n| ≤|p|.
Proof. We need to determine when n/(p−1) ≥ordp(n)+1. If ordp(n) = 0, this holds when
n ≥p −1. If ordp(n) = 1, this holds as long as n ̸= p. If ordp(n) ≥2, this always holds.
□
The inequality in the lemma is true for n = p −1, but we won’t need this.
So if |x −1| ≤|π|, log x ≡Pp
n=1(−1)n−1 (x−1)n
n
mod p. The last term in the sum is more
subtle than the rest since it has a p in the denominator. So let’s isolate the last term.
Let
Lp−1(1 + T) def
=
p−1
X
n=1
(−1)n−1 T n
n ∈Zp[T],
so x ≡1 mod π ⇒log x ≡Lp−1(x) + (x −1)p/p mod p. Writing α = Pp−1
n=2 πn−1/n!, by (2)
log
E(π) −1
π

≡log(1 + α) ≡Lp−1(1 + α) + αp
p mod p.
Let’s compute the last term:
αp
p = 1
p
 
π
p−1
X
n=2
πn−2
n!
!p
= −π
 p−1
X
n=2
πn−2
n!
!p
.

<!-- page 5 -->
KUMMER’S LEMMA
5
For 2 ≤n ≤p −1, πn−2/n! ∈Ap, so
 p−1
X
n=2
πn−2
n!
!p
≡
p−1
X
n=2
πn−2
n!
p
mod p
≡
p−1
X
n=2
(πp)n−2
n!
mod p
≡1
2 mod p
since πp ≡0 mod p.
Thus
(3)
log
E(π) −1
π

≡Lp−1(1 + α) −π/2 mod p.
Since Lp−1(1 + T) ∈Zp[T], Lp−1(1 + α) = Lp−1
Pp−1
n=1 πn−1/n!

∈Zp[π]. We only care
about its expression mod p = −πp−1. Let’s compute the polynomial Lp−1(Pp−1
n=1 T n−1/n!)
in Zp[T]/T n−1. Actually, it turns out to be more convenient to work in Qp[[T]]/T p−1, where
we can use the full exponential and logarithm series, whose coeﬃcients are usually not in Zp.
Whatever we compute in this larger ring for Lp−1(Pp−1
n=1 T n−1/n!) must be in Zp[T]/T p−1.
For f(T) ∈1 + TQp[[T]], Lp−1(f(T)) ≡log(f(T)) mod T p, so from Pp−1
n=1
T n−1
n!
≡
eT −1
T
mod T p−1 we get
Lp−1
 p−1
X
n=1
T n−1
n!
!
≡Lp−1
eT −1
T

≡log
eT −1
T

mod T p−1.
This last expression is tractable, and is where Bernoulli numbers enter. To ﬁnd the expan-
sion for log((eT −1)/T), we diﬀerentiate the series:
d
dT log
eT −1
T

=
T
eT −1 · TeT −(eT −1)
T 2
=
eT
eT −1 −1
T
= 1 +
1
eT −1 −1
T
= 1
T

T +
T
eT −1 −1

= 1
T

T +
X
n≥1
Bn
n! T n


= 1
T

1
2T +
X
i≥1
B2i
(2i)!T 2i


= 1
2 +
X
i≥1
B2i
(2i)!T 2i−1.

<!-- page 6 -->
6
KEITH CONRAD
Integrating and noting the constant term must vanish,
log
eT −1
T

= T
2 +
X
i≥1
B2i
(2i)!2iT 2i ≡T
2 +
m−1
X
i=1
B2i
(2i)!2iT 2i mod T p−1.
So Lp−1(Pp−1
n=1 T n−1/n!) ≡T/2 + Pm−1
i=1 (B2i/(2i)!2i)T 2i in Zp[T]/T p−1, and by (3)
log
E(π) −1
π

≡
m−1
X
i=1
B2i
(2i)!2iπ2i mod p.
Similarly,
log
E(πk) −1
πk

≡
m−1
X
i=1
B2i
(2i)!2ik2iπ2i mod p
since πk ≡kπ mod p.
Putting these congruences together, we can compute log(εp−1
k
) mod p by (1):
log(εp−1
k
) ≡
m−1
X
i=1
B2i
(2i)!2i(1 −k2i)π2i mod p.
So cik ≡
B2i
(2i)!2i(1 −k2i) mod p. Therefore
det(cik) ≡
m−1
Y
i=1
−B2i
(2i)!(2i)

22 −1
32 −1
. . .
m2 −1
24 −1
34 −1
. . .
m4 −1
...
...
...
...
22(m−1) −1
32(m−1) −1
. . .
m2(m−1) −1

mod p.
We can rewrite the last determinant in Vandermonde form. It equals

1
0
. . .
0
1
22 −1
. . .
m2 −1
1
24 −1
. . .
m4 −1
...
...
...
...
1
22(m−1) −1
. . .
m2(m−1) −1

=

1
1
. . .
1
1
22
. . .
m2
1
24
. . .
m4
...
...
...
...
1
22(m−1)
. . .
m2(m−1)

=
Y
1≤i<j≤m
(j2 −i2)
̸≡0 mod p.
Therefore det(cik) ̸≡0 mod p precisely when none of B2, B4, . . . , B2(m−1) = Bp−3 is
divisible by p.
□
We now prove Kummer’s lemma.
Proof. First let’s show u is real, i.e. u is ﬁxed by complex conjugation. By Lemma 2,
u = ζru′ for u′ a real unit. So u′ ∈A+
p = Zp[π2]. Thus u′ ≡b mod π2 for some rational
integer b. Since ζr ≡1 + rπ mod π2, we have u ≡b + brπ mod π2. Since u is congruent to a
rational integer mod p and p = −πp−1, we must have br ≡0 mod p, so p | r, hence u = u′.
Without loss of generality, we may take u to be positive.
We will work in the group of real positive units of A = Z[ζ], since that group has no
torsion. Recall δk from before Lemma 2. By Theorem 7, the numbers log(δp−1
k
) = log(εp−1
k
)

<!-- page 7 -->
KUMMER’S LEMMA
7
are linearly independent over Qp for 2 ≤k ≤m, so the m −1 units δk are multiplicatively
independent over Z. There are m −1 of them, and A× has rank p−1
2
−1 = m −1 by the
Dirichlet Unit Theorem, so the subgroup generated by the δk’s has ﬁnite index in the group
of all units. In particular, for some positive integer n we have
(4)
un =
m
Y
k=2
δck
k
for ck ∈Z. Since the real positive units have no torsion, we may assume gcd(n, c2, . . . , cm) =
1. Raising both sides of (4) to the (p −1)th power and then taking logarithms, we get
n log(up−1) =
m−1
X
k=2
ck log(δp−1
k
).
By Corollary 6, log(up−1) ∈pA+
p , so all ck lie in pZp. Since they are rational integers, all
ck lie in pZ, so un is a pth power of a unit in Z[ζ]. From gcd(n, c2, . . . , cm) = 1 we see n is
prime to p, so u is a pth power of a unit in Z[ζ].
□
This proof of Kummer’s lemma used the units δk rather than the units εk only be-
cause we needed to work in a group of units where there is no torsion, so the assumption
gcd(n, c2, . . . , cm) = 1 could be used. While the assumption that p is regular implies that
the group generated by the units εk has no torsion (there is only the trivial linear relation
among their p-adic logarithms), it is not clear how to show the group generated by u and
the εk has no torsion. By working in the group of positive real units (where we proved u
lies) the torsion issue is easily handled.
In Faddeev’s proof of Kummer’s lemma in [1, §6, Chap. 5], which the proof here is based
on, the Dwork series E(X) = eX+Xp/p is not used. Instead, more systematic use is made of
truncations of the series eX (while E(X) is a “truncated” Artin-Hasse series). For instance,
since ζ = E(π), the congruence
E(π) −1
π
≡
p−1
X
n=1
πn−1
n!
mod p
that we used is the same as ζ ≡ep−1(π) mod πp, where ep−1(T) = Pp−1
n=0 T n/n!. This is
essentially [1, Lemma 3, p. 372] with k = 1 (and ep−1(T) is denoted there by E(T).)
Appendix A. Reformulation of hypothesis in Kummer’s lemma
Kummer’s lemma has an assumption on the unit u: u ≡a mod pZ[ζ] for some a ∈Z.
It is natural to ask how this can be checked in examples. The next theorem expresses the
assumption in a way that makes no reference to an integer a, and it works even if u is not
a unit (only in the conclusion of Kummer’s lemma is it essential that u is a unit).
Theorem 9. When p is prime and α ∈Z[ζ], we have α ≡a mod pZ[ζ] for some a ∈Z if
and only if αp ≡α mod pZ[ζ].
Proof. If α ≡a mod pZ[ζ] then αp ≡ap mod pZ[ζ]. Since ap ≡a mod pZ by Fermat’s little
theorem, αp ≡ap ≡a ≡α mod pZ[ζ].
To prove the converse, recall that as ideals (p) = (ζ −1)p−1 in Z[ζ] and the residue ﬁeld
of Z[ζ] at (ζ −1) is Fp. Setting π = ζ −1, for each k ∈Z+ every residue class in Z[ζ]/(πk)

<!-- page 8 -->
8
KEITH CONRAD
has a unique representative
(5)
a0 + a1π + · · · + ak−1πk−1 mod πkZ[ζ]
where 0 ≤ai ≤p −1 for all i.
Taking k = p −1, we can write α mod pZ[ζp] uniquely as
α ≡a0 + a1π + · · · + ap−2πp−2 mod pZ[ζ]
where 0 ≤ai ≤p −1 for i = 0, 1, . . . , p −2. Since Z[ζ]/(p) is a ring with characteristic p,
the p-th power map is additive on this ring. Since ap
i ≡ai mod pZ and πp ≡0 mod pZ[ζ],
αp ≡ap
0 + ap
1πp + · · · + ap
p−2πp(p−2) ≡ap
0 ≡a0 mod pZ[ζ].
Thus if αp ≡α mod pZ[ζ] then
a0 ≡a0 + a1π + · · · + ap−2πp−2 mod pZ[ζ],
which is the same as a1π + · · · + ap−2πp−2 ≡0 mod pZ[ζ]. That implies ai = 0 for i > 0, so
α ≡a0 mod pZ[ζ].
□
How often is an α in Z[ζ] congruent to an integer modulo (πk)? It happens for all α if
k = 1, since Z[ζ]/(π) ∼= Fp, so take k ≥2. By (5), Z[ζ]/(πk) has pk congruence classes
in total, while the condition that α mod pZ[ζ] is congruent to an integer means ai = 0 for
1 ≤i ≤k−1, so there are only p such congruence classes. Thus the proportion of congruence
classes mod (πk) that are represented by an integer is p/pk = 1/pk−1 ≤1/p ≤1/2.
Corollary 10. When p is prime, ζpr is a root of unity of order pr for some r ≥1, and
α ∈Z[ζpr], we have α ≡a mod pZ[ζpr] for some a ∈Z if and only if αp ≡α mod pZ[ζpr].
Proof. In Z[ζpr], which is the ring of integers of Q(ζpr), p is totally ramiﬁed with (p) =
(ζpr −1)ϕ(pr). Run through the proof of Theorem 9 with ζpr in place of ζ and ϕ(pr) in place
of p −1, which is ϕ(p).
□
Just as the natural map Z/(pk) →Zp/(pk) is an isomorphism for all k ∈Z+, the natural
map Z[ζpr]/(ζpr −1)k →Zp[ζpr]/(ζpr −1)k is an isomorphism for all k ∈Z+, so Corollary
10 is true with Zp[ζpr] in place of Z[ζpr].
References
[1] Z. I. Borevich and I. R. Shafarevich, “Number Theory,” Academic Press, New York, 1966.
[2] K. Conrad, Artin–Hasse-type series and roots of unity, http://www.math.uconn.edu/~kconrad/blurbs/
gradnumthy/AHrootofunity.pdf.
[3] S. Lang, “Cyclotomic Fields I and II,” Springer-Verlag, New York, 1994.
[4] L. Washington, “An Introduction to Cyclotomic Fields,” Springer-Verlag, New York, 1997.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*