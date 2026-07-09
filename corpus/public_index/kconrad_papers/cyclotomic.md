# Cyclotomic Extensions

> **Source**: https://kconrad.math.uconn.edu/blurbs/cyclotomic.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
CYCLOTOMIC EXTENSIONS
KEITH CONRAD
1. Introduction
For a positive integer n, an nth root of unity in a ﬁeld is a solution to zn = 1, or
equivalently is a root of T n −1. There are at most n diﬀerent nth roots of unity in a ﬁeld
since T n −1 has at most n roots in a ﬁeld. A root of unity is an nth root of unity for
some n. The only roots of unity in R are ±1, while in C there are n diﬀerent nth roots of
unity for each n, namely e2πik/n for 0 ≤k ≤n −1 and they form a group of order n. In
characteristic p there is no pth root of unity besides 1: if xp = 1 in characteristic p then
0 = xp −1 = (x −1)p, so x = 1. That is strange, but it is a key feature of characteristic p,
e.g., it makes the pth power map x 7→xp on ﬁelds of characteristic p injective.
For a ﬁeld K, an extension of the form K(ζ), where ζ is a root of unity, is called a
cyclotomic extension of K. The term cyclotomic means “circle-dividing,” which comes from
the fact that the nth roots of unity in C divide a circle into n arcs of equal length, as in Figure
1 when n = 7. The important algebraic fact we will explore is that cyclotomic extensions
of every ﬁeld have an abelian Galois group; we will look especially at cyclotomic extensions
of Q and ﬁnite ﬁelds. There are not many general methods known for constructing abelian
extensions (that is, Galois extensions with abelian Galois group); cyclotomic extensions are
essentially the only construction that works over all ﬁelds. Other constructions of abelian
extensions are Kummer extensions, Artin-Schreier-Witt extensions, and Carlitz extensions,
but these all require special conditions on the base ﬁeld.
1
Figure 1. The 7th roots of unity.
The nth roots of unity in a ﬁeld form a group under multiplication. It’s obvious that this
group in C is cyclic from the analytic formula for them, with generator e2πi/n. In a general
ﬁeld there is no formula, but these roots of unity are still a cyclic group.
Theorem 1.1. The group of nth roots of unity in a ﬁeld is cyclic. More generally, every
ﬁnite subgroup of the nonzero elements of a ﬁeld is a cyclic group.
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. Let F be a ﬁeld and G be a ﬁnite subgroup of F ×. From the general theory of
abelian groups, if there are elements in G with orders n1 and n2 then there is an element
of G with order the least common multiple [n1, n2]. Letting N be the maximal order of
all the elements of G, we will show the order of every element in G divides N. If n is the
order of some element in G then there is an element of G with order [n, N] ≥N. Since N is
the maximal order we have [n, N] ≤N, so [n, N] = N, which implies n divides N (why?).
Thus every element of G is a root of T N −1, which implies |G| ≤N (the number of roots
of a polynomial in a ﬁeld is at most its degree). At the same time, since the order of each
element divides the size of the group we have N | |G|. Hence N = |G|, which means some
element of G has order |G|, so G is cyclic.
□
Example 1.2. For each prime p, the group (Z/(p))× is cyclic by Theorem 1.1 since these
are the nonzero elements in the ﬁeld Z/(p) and they form a ﬁnite group. More generally, if
F is a ﬁnite ﬁeld then F × is a cyclic group.
Watch out! Theorem 1.1 does not imply (Z/(pr))× is cyclic for r > 1, since the ring
Z/(pr) is not a ﬁeld for r > 1. The theorem is simply silent about this. In fact, for other
reasons, (Z/(pr))× is cyclic for p ̸= 2 but usually not if p = 2, e.g., (Z/(8))× is not cyclic.
For a cyclotomic extension K(ζ)/K set n to be the order of ζ as a root of unity: the least
exponent making ζn = 1. Then T n −1 has every power of ζ as a root, so it has n diﬀerent
roots: T n −1 is separable over K. Conversely, if T n −1 is separable over K then it has n dif-
ferent roots, they are a group under multiplication, and Theorem 1.1 guarantees it is cyclic:
there is a root of unity of order n among the nth roots of unity. Therefore when we con-
struct cyclotomic extensions K(ζ)/K little is lost by assuming T n −1 is separable over K.
That is equivalent to T n −1 being relatively prime to its derivative nT n−1 in K[T], which
is equivalent to n ̸= 0 in K: char(K) = 0, or char(K) = p and (p, n) = 1. We assume this
is the case in all we do below.
When there are n diﬀerent nth roots of unity, we denote the group of them by µn.1 For
instance, in C we have µ2 = {1, −1} and µ4 = {1, −1, i, −i}. In F7, µ3 = {1, 2, 4}. A
generator of µn is denoted ζn. That is, ζn denotes a root of unity of order n. Watch out!
An nth root of unity is a solution to zn = 1 but that doesn’t mean it has order n. For
example, 1 is an nth root of unity for every n ≥1. An nth root of unity that has order n
is called a primitive nth roots of unity (zn = 1 and zj ̸= 1 for j < n). For example, −1 in
C is a 4th root of unity but not a primitive 4th root of unity. For a ∈Z, the order of ζa
n
is n/(a, n),2 so ζa
n is a primitive nth root of unity if and only if (a, n) = 1. Therefore when
a ﬁeld contains n diﬀerent nth roots of unity it contains ϕ(n) primitive nth roots of unity,
where ϕ(n) = |(Z/(n))×|. The primitive nth roots of unity are the generators of µn, and
when n ≥3 there is not a unique generator e.g., if ζn is one generator then ζ−1
n
is another
one), so writing ζn always involves making a choice of generator.
Any two primitive nth roots of unity in a ﬁeld are powers of each other, so the ﬁeld K(ζn)
is independent of the choice of ζn. We will often write this ﬁeld as K(µn): adjoining one
primitive nth root of unity is the same as adjoining all nth roots of unity.
2. Embedding the Galois group
When T n −1 is separable over K, K(µn)/K is Galois since K(µn) is the splitting ﬁeld
of T n −1 over K. What is its Galois group?
1Anytime we write µn it is understood to contain n elements.
2See Theorem 3.13(3) in https://kconrad.math.uconn.edu/blurbs/grouptheory/order.pdf.

<!-- page 3 -->
CYCLOTOMIC EXTENSIONS
3
Lemma 2.1. For σ ∈Gal(K(µn)/K) there is an integer a = aσ that is relatively prime to
n such that σ(ζ) = ζa for all ζ ∈µn.
Proof. Let ζn be a generator of µn (that is, a primitive nth root of unity), so ζn
n = 1 and
ζj
n ̸= 1 for 1 ≤j < n. Since σ is multiplicative and injective, σ(ζn)n = 1 and σ(ζn)j ̸= 1
for 1 ≤j < n, so σ(ζn) is a primitive nth root of unity. This implies σ(ζn) = ζa
n where
(a, n) = 1. Each ζ ∈µn has the form ζk
n for some k, so
σ(ζ) = σ(ζk
n) = σ(ζn)k = (ζa
n)k = (ζk
n)a = ζa.
□
The exponent a in Lemma 2.1 is well-deﬁned modulo n: ζa
n = ζb
n ⇒a ≡b mod n because
ζn has order n. Thus we can think of a = aσ as an element of the group (Z/(n))×.
Example 2.2. The primitive 7th roots of unity are the 7th roots of unity besides 1, and
they are all roots of (T 7 −1)/(T −1) = T 6 + T 5 + T 4 + T 3 + T 2 + T + 1. This polynomial
is irreducible over Q because it becomes Eisenstein at 7 when we replace T with T + 1:
(T + 1)7 −1
(T + 1) −1 = T 6 + 7T 5 + 21T 4 + 35T 3 + 35T 2 + 21T + 7.
This implies, for instance, that ζ7 and ζ2
7 have the same minimal polynomial over Q. Since,
moreover, Q(ζ7) = Q(ζ2
7), there is an automorphism σ ∈Gal(Q(µ7)/Q) with the eﬀect
σ(ζ) = ζ2 for all ζ ∈µ7. It is FALSE that σ(α) = α2 for all α ∈Q(µ7), since squaring is
not additive in characteristic 0. ONLY on the 7th roots of unity is σ being described as a
power map. Elsewhere σ is determined from additivity and multiplicativity, e.g.,
σ(4ζ5
7 −11ζ7 + 9) = 4(ζ2
7)5 −11ζ2
7 + 9 = 4ζ3
7 −11ζ2
7 + 9.
Theorem 2.3. The mapping
Gal(K(µn)/K) →(Z/(n))×
where σ 7→aσ mod n, from σ(ζ) = ζaσ for all ζ ∈µn, is an injective group homomorphism.
Proof. Pick σ and τ in Gal(K(µn)/K). For a primitive nth root of unity ζn,
(στ)(ζn) = σ(τ(ζn)) = σ(ζaτ
n ) = σ(ζn)aτ = (ζaσ
n )aτ = ζaσaτ
n
.
Also (στ)(ζn) = ζaστ
n
, so ζaστ
n
= ζaσaτ
n
. Since ζn has order n, aστ ≡aσaτ mod n. This shows
σ 7→aσ mod n is a homomorphism from Gal(K(µn)/K) to (Z/(n))×.
When σ is in the kernel, aσ ≡1 mod n, so σ(ζn) = ζn. Also σ ﬁxes all the elements of
K, so σ is the identity on K(ζn) = K(µn), so σ is the identity in Gal(K(µn)/K).
□
Since (Z/(n))× is abelian, the embedded subgroup Gal(K(µn)/K) is abelian. We have
proved that cyclotomic extensions are always abelian. Whenever we view Gal(K(µn)/K)
in (Z/(n))×, it will always be understood to be by the embedding in Theorem 2.3.
Example 2.4. Complex conjugation is an automorphism of Q(µn)/Q with order 2. Un-
der the embedding of Gal(Q(µn)/Q) into (Z/(n))×, complex conjugation corresponds to
−1 mod n since ζ = ζ−1 for every root of unity ζ.
The embedding of Gal(K(µn)/K) into (Z/(n))× may not be surjective; that depends on
K. For instance, if K = R and n ≥3 then K(µn)/K = C/R is a quadratic extension. The
nontrivial R-automorphism of C is complex conjugation, whose eﬀect on roots of unity in
C is to invert them: ζ = ζ−1. Therefore the embedding Gal(C/R) ,→(Z/(n))× for n ≥3
has image {±1 mod n}, which is smaller than (Z/(n))× unless n = 2, 3, 4, or 6.

<!-- page 4 -->
4
KEITH CONRAD
We will ﬁgure out the image in Theorem 2.3 in two important examples: K = Q and
K = Fp. In the ﬁrst case the embedding Gal(K(µn)/K) →(Z/(n))× is surjective, while in
the second case the embedding need not be surjective but we can still describe the image.
Theorem 2.5. The embedding Gal(Q(µn)/Q) ,→(Z/(n))× is an isomorphism.
Proof. Let ζn be a primitive nth root of unity over Q.
The size of Gal(Q(µn)/Q) =
Gal(Q(ζn)/Q) is the number of Q-conjugates of ζn, which is at most ϕ(n) = |(Z/(n))×|.
To prove Gal(Q(µn)/Q) ,→(Z/(n))× is a surjection we will show for all a ∈Z such that
(a, n) = 1 that ζn and ζa
n are Q-conjugate: their minimal polynomials over Q agree.
Since ζa
n only depends on a mod n, we can take a > 0, and in fact a > 1.
Write
a = p1p2 · · · pr as a product of primes pi, each not dividing n (some pi’s could coincide).
To show ζn and ζa
n have the same minimal polynomial over Q, it suﬃces to show for each
prime p not dividing n that every primitive nth root of unity and its pth power have the
same minimal polynomial over Q, since then the successive pairs of primitive nth roots of
unity
ζn,
ζp1
n ,
ζp1p2
n
,
ζp1p2p3
n
,
. . . ,
ζp1p2···pr
n
= ζa
n
have the same minimal polynomial over Q since each is a prime power of the previous one.
For an arbitrary primitive nth root of unity ζn over Q, assume ζn and ζp
n are not Q-
conjugate for some prime p not dividing n. We will get a contradiction. Let f(T) be the
minimal polynomial of ζn over Q and g(T) be the minimal polynomial of ζp
n over Q, so
g(T) ̸= f(T). The polynomials f(T) and g(T) are in Z[T] since they both divide T n −1
and every monic factor of T n −1 in Q[T] is in Z[T] by Gauss’ lemma.
Every nth root of unity is a root of T n −1, so f(T) and g(T) each divide T n −1 in Q[T].
They are diﬀerent monic irreducibles, so T n −1 = f(T)g(T)h(T) for a monic h(T) ∈Q[T].
By Gauss’ lemma, h(T) ∈Z[T]. Reducing this equation modulo p,
(2.1)
T n −1 = f(T)g(T)h(T)
in Fp[T]. The polynomial T n −1 is separable in Fp[T] since p doesn’t divide n, so (2.1) tells
us that f(T) and g(T) are relatively prime in Fp[T]. Because f(T) and g(T) are monic,
their reductions f(T) and g(T) have the same degrees as f(T) and g(T), so the reductions
are nonconstant.
Since g(ζp
n) = 0, g(T p) has ζn as a root, so f(T) | g(T p) in Q[T]. Write g(T p) = f(T)k(T)
for some monic k(T) in Q[T]. We have k(T) ∈Z[T] by Gauss’ lemma (why?). Reduce the
equation g(T p) = f(T)k(T) modulo p and use the formula g(T p) = g(T)p in Fp[T] to get
g(T)p = f(T)k(T)
in Fp[T]. Thus every irreducible factor of f(T) in Fp[T] is a factor of g(T) (and there are
irreducible factors since f(T) is nonconstant). That contradicts relative primality of f(T)
and g(T) in Fp[T].
□
Remark 2.6. The proof of Theorem 2.5 above goes back to Dedekind [2]. Its appearance in
van der Waerden’s Moderne Algebra in 1930 made it the standard proof in later books. Here
is another proof of Theorem 2.5, due to Landau [5]. Let f(T) be the minimal polynomial of
ζn over Q, so f(T) is monic in Z[T] as explained above. We want to show when (a, n) = 1
that f(ζa
n) = 0. For all integers k ≥1 write f(T k) = f(T)Qk(T) + Rk(T) in Z[T], where
Rk = 0 or deg Rk < deg f. Since Rk(T) is 0 or has degree less than deg f = [Q(ζn) : Q],
Rk(T) is determined by Rk(ζn) = f(ζk
n), so Rk(ζn) only depends on k mod n. In particular,
every Rk(T) is one of R1(T), R2(T), . . . , Rn(T).

<!-- page 5 -->
CYCLOTOMIC EXTENSIONS
5
For prime p, Rp(ζn) = f(ζp
n) = f(ζp
n) −f(ζn)p, so Rp(T) is the remainder when f(T p) −
f(T)p is divided by f(T). From f(T)p ≡f(T p) mod p we get f(T p)−f(T)p ∈pZ[T], which
implies (why?) that Rp(T) ∈pZ[T]. Let C be the largest absolute value of all coeﬃcients
in R1(T), R2(T), . . . , Rn(T). Since there are inﬁnitely many primes (!), pick a prime p > C.
The polynomial Rp(T) must be 0: its coeﬃcients are smaller in absolute value then C
and are divisible by p, which exceeds C. Therefore f(T p) = f(T)Qp(T) when p > C, so
f(ζp
n) = 0. This implies, by iteration, that f(ζk
n) = 0 for the positive integers k whose
prime factors all exceed C. If (a, n) = 1 and a > 1, deﬁne k := a + n Q
p≤C,(p,a)=1 p. Then
k ≡a mod n, so (k, n) = 1. The two terms in the sum deﬁning k are relatively prime, so
every prime factor of this k is larger than C (why?), which implies 0 = f(ζk
n) = f(ζa
n).
Remark 2.7. An introductory discussion of cyclotomic extensions of Q would not be
complete without mentioning a deep theorem of Kronecker and Weber: every ﬁnite abelian
extension of Q lies inside a cyclotomic extension of Q. This is false for a base ﬁeld K that
is a ﬁnite extension of Q larger than Q: some ﬁnite abelian extension of K does not lie in
a cyclotomic extension of K. For instance, if K = Q(i) then K( 4√1 + i)/K is abelian but
for no n is K( 4√1 + i) ⊂K(ζn).
Now we turn to Galois groups of cyclotomic extensions of the ﬁnite ﬁeld Fp.
Theorem 2.8. When n is not divisible by the prime p, the image of Gal(Fp(µn)/Fp) in
(Z/(n))× under the standard embedding is ⟨p mod n⟩. In particular, [Fp(µn) : Fp] is the
order of p mod n.
Proof. The polynomial T n −1 is separable in Fp[T] and the general theory of ﬁnite ﬁelds
tells us Gal(Fp(µn)/Fp) is generated by the pth power map ϕp : x 7→xp for all x in Fp(µn).
The standard embedding of Gal(Fp(µn)/Fp) into (Z/(n))× associates to ϕp the congruence
class a mod n where ϕp(ζ) = ζa for all ζ ∈µn. Then ζp = ζa, so a ≡p mod n. Therefore
the standard embedding of Gal(Fp(µn)/Fp) into (Z/(n))× turns ϕp into p mod n. Since ϕp
generates the Galois group, the image of the Galois group in (Z/(n))× is ⟨p mod n⟩, so the
size of the Galois group is the order of p in (Z/(n))×.
□
Example 2.9. The degree [Fp(µ7) : Fp] is the order of p mod 7 that is 1, 2, 3, or 6 (if
p ̸= 7). The ﬁeld diagram below gives some examples.
Q(µ7)
6
F2(µ7)
3
F3(µ7)
6
F13(µ7)
2
F29(µ7)
1
Q
F2
F3
F13
F29
These are all consistent with how (T 7 −1)/(T −1) = T 6 + T 5 + · · · + T + 1 factors modulo
each of the primes: into irreducibles of common degree [Fp(µ7) : Fp].
T 6+T 5+T 4+T 3+T 2+T +1 ≡(T 3 + T + 1)(T 3 + T 2 + 1) mod 2
≡irreducible mod 3
≡(T 2 + 3T + 1)(T 2 + 5T + 1)(T 2 + 6T + 1) mod 13
≡(T −7)(T −16)(T −20)(T −23)(T −24)(T −25) mod 29.

<!-- page 6 -->
6
KEITH CONRAD
For the cyclic group Gal(Fp(µn)/Fp) to be as big as Gal(Q(µn)/Q) ∼= (Z/(n))× is equiv-
alent to saying ⟨p mod n⟩= (Z/(n))×, so (Z/(n))× must be a cyclic group and p mod n is
a generator of it. The groups (Z/(n))× are usually not cyclic (like n = 8 or n = 15), so the
standard embedding Gal(Fp(µn)/Fp) ,→(Z/(n))× is usually not surjective.
Theorem 2.8 generalizes to all ﬁnite ﬁelds Fq as a base ﬁeld. A proof is left to the reader.
Theorem 2.10. Let Fq be a ﬁnite ﬁeld with prime power order q. When n is relatively prime
to q, the image of Gal(Fq(µn)/Fq) in (Z/(n))× is ⟨q mod n⟩. In particular, [Fq(µn) : Fq]
is the order of q mod n.
3. Composites and Intersections of Cyclotomic Extensions
When T n −1 and T m −1 are separable over K, the composite ﬁeld K(µm)K(µn) equals
K(µ[m,n]). Indeed, both K(µm) and K(µn) lie in K(µ[m,n]), so their composite does too.
For the reverse inclusion, a primitive root of unity of order [m, n] can be obtained by
multiplying suitable mth and nth roots of unity (why?), so µ[m,n] ⊂K(µm)K(µn), which
implies K(µ[m,n]) ⊂K(µm)K(µn). Therefore K(µm)K(µn) = K(µ[m,n]).
It is natural to guess that a counterpart of K(µm)K(µn) = K(µ[m,n]) for intersections
is K(µm) ∩K(µn) = K(µ(m,n)). The inclusion ⊃is easy, but the other inclusion can be
FALSE! It’s possible for m and n to be relatively prime and K(µm) ∩K(µn) to be larger
than K(µ1) = K. Matt Emerton pointed out to me the following simple example.
Example 3.1. If K = Q(
√
3) then K(ζ4) = K(i) = Q(
√
3, i) = Q(
√
3, √−3) = K(ζ3)
because ζ3 = (−1 + √−3)/2. Since K(ζ4) and K(ζ3) are equal and larger than K itself,
their intersection is larger than K(ζ(4,3)) = K.
Here are some more examples.
Example 3.2. For n ≥3, complex conjugation on Q(ζn) is an automorphism of order 2.
Its ﬁxed ﬁeld (the real numbers in Q(ζn)) is denoted Q(ζn)+. Show as an exercise that
Q(ζn)+ = Q(ζn + ζ−1
n ) and [Q(ζn) : Q(ζn)+] = 2. For each pair of relatively prime integers
m and n both at least 3, one ﬁeld K such that K(µm) ∩K(µn) ̸= K is K = Q(ζmn)+.
Since [Q(ζmn) : K] = 2 and K ⊂R, K(ζm) = Q(ζmn) and K(ζn) = Q(ζmn).
Thus
K(ζm) ∩K(ζn) = Q(ζmn) is larger than K. Taking m = 4 and n = 3 we get Example 3.1:
Q(ζ12)+ = Q(
√
3).
Example 3.3. Using Theorem 2.8,
F3(µ5) ∩F3(µ7) = F34 ∩F36 = F32 ̸= F3.
This weirdness does not happen when the base ﬁeld is the rational numbers.
Theorem 3.4. For all positive integers m and n, Q(µm)∩Q(µn) = Q(µ(m,n)); in particular,
if (m, n) = 1 then Q(µm) ∩Q(µn) = Q.
Proof. By Theorem 2.5, [Q(µN) : Q] = |(Z/(N))×| = ϕ(N) for all positive integers N.
There is a formula for ϕ(N) in terms of the prime factors of N:
(3.1)
ϕ(N) = N
Y
p|N

1 −1
p

.
Since Q(µd) ⊂Q(µm) when d | m, we have Q(µ(m,n)) ⊂Q(µm) ∩Q(µn). To show this
containment is an equality we will show Q(µm)∩Q(µn) and Q(µ(m,n)) have the same degree
over Q.

<!-- page 7 -->
CYCLOTOMIC EXTENSIONS
7
For ﬁnite Galois extensions L1/K and L2/K in a common ﬁeld, we have [L1L2 : K] =
[L1 : K][L2 : K]/[L1 ∩L2 : K]. The composite ﬁeld Q(µm)Q(µn) is Q(µ[m,n]), so
[Q(µ[m,n]) : Q] = [Q(µm)Q(µn) : Q] = [Q(µm) : Q][Q(µn) : Q]
[Q(µm) ∩Q(µn) : Q] .
Replacing each [Q(µN) : Q] on the right side with ϕ(N),
(3.2)
[Q(µm) ∩Q(µn) : Q] = ϕ(m)ϕ(n)
ϕ([m, n]) .
Using (3.1), (3.2) becomes
[Q(µm) ∩Q(µn) : Q] =
m Q
p|m(1 −1/p) · n Q
p|n(1 −1/p)
[m, n] Q
p|[m,n](1 −1/p)
.
Since [m, n](m, n) = mn, the ratio mn/[m, n] is (m, n). The prime factors of [m, n] are
those dividing either m or n, so the ratio of products over primes is the product of 1 −1/p
over all primes dividing both m and n, which means the prime factors of (m, n). Therefore
[Q(µm) ∩Q(µn) : Q] = (m, n)
Y
p|(m,n)

1 −1
p

= ϕ((m, n)),
which is [Q(µ(m,n)) : Q], so Q(µm)∩Q(µn) has the same degree over Q as Q(µ(m,n)), hence
the ﬁelds are equal since we already saw one is a subﬁeld of the other.
□
4. Coincidences of Cyclotomic Fields over Q
Knowing the degree of cyclotomic extensions of Q lets us determine when two cyclotomic
ﬁelds can coincide.
For example, Q(ζ3) = Q(ζ6) since −ζ3 has order 6.
More simply,
Q(ζ1) = Q(ζ2) = Q since ζ1 = 1 and ζ2 = −1. Here is the general result in this direction.
Theorem 4.1. Let m and n be positive integers.
(1) The number of roots of unity in Q(µm) is [2, m].
(2) If m ̸= n then Q(µm) = Q(µn) if and only if min(m, n) = k and max(m, n) = 2k
for an odd k.
Proof. 1) Our argument is adapted from [1, p. 158]. The root of unity −ζm is in Q(µm)
and has order 2m if m is odd and m if m is even, hence order [2, m] in general. Thus
µ[2,m] ⊂Q(µm).
If Q(µm) contains an rth root of unity then Q(µr) ⊂Q(µm), and taking degrees over
Q shows ϕ(r) ≤ϕ(m). As r →∞, ϕ(r) →∞(albeit erratically)3 so there is a largest r
satisfying µr ⊂Q(µm). Since µmµr = µ[m,r] is in Q(µm) we have [m, r] ≤r, so [m, r] = r.
Write r = ms. By (3.1), for all a and b in Z+ we have
(4.1)
ϕ(ab) = ϕ(a)ϕ(b)(a, b)
ϕ((a, b))
,
so
ϕ(r) = ϕ(ms) = ϕ(m)ϕ(s)
(m, s)
ϕ((m, s)) ≥ϕ(m)ϕ(s).
3This follows from showing a bound ϕ(r) ≤B implies an upper bound on r. For prime powers pe dividing
r, ϕ(pe) ≤B since ϕ(pe) | ϕ(r), so pe−1(p −1) ≤B. Then 2e−1 ≤B and p −1 ≤B, so we get upper bounds
on p and on e, which gives an upper bound on r by unique factorization.

<!-- page 8 -->
8
KEITH CONRAD
Since Q(µm) = Q(µr) for the maximal r, computing degrees over Q shows ϕ(m) = ϕ(r) ≥
ϕ(m)ϕ(s), so 1 ≥ϕ(s). Thus ϕ(s) = 1, so s = 1 or 2, so r = m or r = 2m. That is, the
number of roots of unity in Q(µm) is either m or 2m. If m is even then ϕ(2m) = 2ϕ(m) >
ϕ(m), so r ̸= 2m. Thus when m is even the number of roots of unity in Q(µm) is m. If m
is odd then −ζm has order 2m, so the number of roots of unity in Q(µm) is 2m. In general
the number of roots of unity in Q(µm) is [2, m].
2) If Q(µm) = Q(µn) then [2, m] = [2, n] by part (1), so m = n if m and n have the same
parity. We assume m ̸= n, so they have opposite parity. For even m (and odd n) we get
m = 2n, and for odd m (and even n) we get 2m = n.
□
Remark 4.2. Theorem 4.1 suggests two ways to parametrize cyclotomic extensions of Q
without duplication: as Q(µm) for m not twice an odd integer (m ̸≡2 mod 4) or for m
equal to twice an odd integer (m ≡2 mod 4). In the ﬁrst convention, Q(µm) contains 2m
roots of unity. The ﬁrst convention, where m ̸≡2 mod 4, is commonly used since certain
important results about these ﬁelds take on a simpler appearance with that convention.
When are there coincidences among diﬀerent “real” cyclotomic ﬁelds Q(µn)+?
Theorem 4.3. If Q(µm)+ = Q(µn)+ then Q(µm) = Q(µn) except for the cyclotomic ﬁelds
Q(µ1), Q(µ3), and Q(µ4), which are diﬀerent but all have Q(µn)+ = Q.
Proof. We will break up the proof into two cases.
Case 1: Q(µm)+ = Q(µn)+ = Q.
We will show that Q(µn)+ = Q if and only if Q(µn) is Q(µ1), Q(µ3), or Q(µ4). It’s easy
to see those three ﬁelds have Q(µn)+ = Q. To prove the converse, we can assume n ≥3.
Then [Q(µn) : Q(µn)+] = 2 (Example 3.2), so [Q(µn)+ : Q] = ϕ(n)/2. If Q(µn)+ = Q
then ϕ(n)/2 = 1, so ϕ(n) = 2. The only such n are 3, 4, and 6, and Q(µ3) = Q(µ6).
Case 2: Q(µm)+ = Q(µn)+ ̸= Q.
For general positive integers m and n, Q(µm)+ ∩Q(µn)+ = Q(µ(m,n))+ since both
sides are the real numbers in Q(µm) ∩Q(µn). (We are using Theorem 3.4 here.) So if
Q(µm)+ = Q(µn)+ then
(4.2)
Q(µm)+ = Q(µn)+ = Q(µd)+,
where d = (m, n). By the hypothesis of Case 2, the ﬁelds in (4.2) are not Q, so m, n, d ≥5.
All we’ll really need is that these three numbers are at least 3.
Computing degrees over Q in (4.2), ϕ(m)/2 = ϕ(d)/2, so ϕ(m) = ϕ(d). This is a strong
restriction since d | m. Writing m = dm′, we’ll see that m′ is 1 or 2: using (4.1),
ϕ(m) = ϕ(dm′) = ϕ(d)ϕ(m′)
(d, m′)
ϕ((d, m′)) = ϕ(m)ϕ(m′)
(d, m′)
ϕ((d, m′)) ≥ϕ(m)ϕ(m′).
Thus 1 ≥ϕ(m′), so ϕ(m′) = 1. Thus m′ is 1 or 2. Then 1 = ϕ(m′)(d, m′)/ϕ((d, m′)) =
(d, m′)/ϕ((d, m′)), so (d, m′) = ϕ((d, m′)). The only positive integer equal to its ϕ-value is
1, so (d, m′) = 1. If m′ = 1 then m = d, so Q(µm) = Q(µd). If m′ = 2, then m = dm′ = 2d
with (d, 2) = 1, so d is odd. Thus Q(µm) = Q(µ2d) = Q(µd).
Going through the previous paragraph with n in place of m, we get Q(µn) = Q(µd) too,
so Q(µm) = Q(µn).
□
Theorem 4.4. If E/Q is a ﬁnite extension that contains no proper abelian extensions of
Q then Gal(E(µn)/E) ∼= (Z/(n))× for all n ≥1, or equivalently [E(µn) : E] = ϕ(n).

<!-- page 9 -->
CYCLOTOMIC EXTENSIONS
9
Proof. From Galois theory, for ﬁnite extensions L/K and F/K, [LF : F] = [L : L ∩F]
if L/K is Galois. Therefore [E(µn) : E] = [Q(µn)E : E] = [Q(µn) : Q(µn) ∩E]. The
intersection Q(µn) ∩E is an abelian extension of Q since every subﬁeld of Q(µn) is abelian
over Q. Therefore by hypothesis Q(µn) ∩E = Q, so [E(µn) : E] = [Q(µn) : Q] = ϕ(n).
□
Example 4.5. A non-Galois extension E/Q of prime degree, like Q(
p√
2)/Q for odd primes
p, satisﬁes the hypothesis of Theorem 4.4, so Gal(E(µn)/E) ∼= (Z/(n))× for all n.
5. Cyclotomic polynomials
In the complex numbers, all primitive nth roots of unity are Q-conjugate and therefore
have a common minimal polynomial in Q[T]. It is called the nth cyclotomic polynomial and
is denoted Φn(T). Explicitly,
Φn(T) =
Y
1≤k≤n
(k,n)=1
(T −e2πik/n).
Here are the ﬁrst 10 cyclotomic polynomials.
Φ1(T) = T −1
Φ2(T) = T + 1
Φ3(T) = T 2 + T + 1
Φ4(T) = T 2 + 1
Φ5(T) = T 4 + T 3 + T 2 + T + 1
Φ6(T) = T 2 −T + 1
Φ7(T) = T 6 + T 5 + T 4 + T 3 + T 2 + T + 1
Φ8(T) = T 4 + 1
Φ9(T) = T 6 + T 3 + 1
Φ10(T) = T 4 −T 3 + T 2 −T + 1
For all n ≥1, Φn(T) is monic of degree ϕ(n) in Q[T] and Φn(T) is irreducible over Q.
Here are some identities involving these polynomials, where p is a prime:
(1) T n −1 = Q
d|n Φd(T),
(2) Φn(T) = T ϕ(n)Φn(1/T) for n ≥2,
(3) Φp(T) = T p−1 + T p−2 + · · · + T + 1,
(4) Φpr(T) = Φp(T pr−1)[= T (p−1)pr−1 + T (p−2)pr−1 + · · · + T pr−1 + 1],
(5) Φ2n(T) = Φn(−T) for odd n,
(6) Φpr1
1 ···p
rk
k (T) = Φp1···pk(T pr1−1
1
···p
rk−1
k
), and more generally Φmn(T) = Φn(T m) if all
prime factors of m divide n,
(7) if (p, m) = 1 then Φprm(T) = Φm(T pr)/Φm(T pr−1).
Except for the ﬁrst formula, these identities can be checked by showing the right side has
the correct degree and one correct root to be the cyclotomic polynomial on the left side.
(Two monic irreducible polynomials with a common root are equal.) The ﬁrst identity can
be regarded as a recursive deﬁnition of the cyclotomic polynomials.
Example 5.1. Since Φ2(T) = T + 1, we have Φ8(T) = Φ2(T 4) = T 4 + 1. Since Φ3(T) =
T 2+T +1, Φ6(T) = Φ3(−T) = T 2−T +1 and Φ24(T) = Φ6(T 4) = Φ3(−T 4) = T 12−T 4+1.
Theorem 5.2. For all n ≥1, Φn(T) ∈Z[T].
Proof. Let ζn be a primitive nth root of unity in C, so Φn(T) is its minimal polynomial
over Q. Since T n −1 vanishes at ζn, Φn(T) divides T n −1 in Q[T]. Since Φn(T) and T n −1
are both monic and T n −1 ∈Z[T], by Gauss’ lemma Φn(T) ∈Z[T].
□

<!-- page 10 -->
10
KEITH CONRAD
The sequence of cyclotomic polynomials is an interesting example where initial data can
be misleading: the coeﬃcients of the ﬁrst 100 cyclotomic polynomials are all 0 or ±1, but
this pattern is not true in general! For instance, Φ105(T) has a coeﬃcient −2 for T 41 and
T 7 (the other coeﬃcients are 0 and ±1). Why does it take so long for a coeﬃcient besides
0 and ±1 to occur? Well, the ﬁfth and sixth cyclotomic polynomial identities above show
the nonzero coeﬃcients of all cyclotomic polynomials are determined by the coeﬃcients of
the Φn(T) where n is a product of distinct odd primes. The polynomial Φp(T) only has
coeﬃcient 1 and it can be shown [4] that Φpq(T) only has coeﬃcients 0 and ±1 when p
and q are diﬀerent primes. Therefore each n with at most 2 odd prime factors only has
coeﬃcients among 0 and ±1. The ﬁrst positive integer that does not have at most 2 odd
prime factors is 3·5·7 = 105 > 100, which shows Φ105(T) is the ﬁrst cyclotomic polynomial
that even has a chance to have a coeﬃcient other than 0 and ±1. By a theorem of Schur, if
n has t odd prime factors then Φn(T) has coeﬃcient −(t−1) (thus predicting the coeﬃcient
of −2 in Φ105(T)). To produce large coeﬃcients in Φn(T) we should give n a lot of diﬀerent
odd prime factors and numbers below 100 have at most 2 odd prime factors.
Cyclotomic polynomials for prime-power n, say n = pr, can be written down concretely:
Φpr(T) =
T pr −1
T pr−1 −1 =
p−1
X
k=0
T pr−1k.
Theorem 5.3. The polynomial Φpr(T + 1) is Eisenstein with respect to p.
Proof. The constant term of Φpr(T + 1) is
Φpr(1) =
p−1
X
k=0
1pr−1k = p,
which is divisible by p just once. To show the non-leading coeﬃcients are all multiples of
p, we reduce the coeﬃcients mod p. Since, in Fp[T], T pr −1 = (T −1)pr and T pr−1 −1 =
(T −1)pr−1, we have (reducing coeﬃcients mod p)
Φpr(T) =
T pr −1
T pr−1 −1 = (T −1)pr−pr−1 in Fp[T],
so
Φpr(T + 1) = T pr−pr−1 in Fp[T].
The degree of Φpr(T + 1) is pr −pr−1, so all its non-leading coeﬃcients are 0 in Fp, which
means the coeﬃcients as integers are multiples of p.
□
Using the Eisenstein irreducibility criterion, Φpr(T + 1) is irreducible in Q[T], so Φpr(T)
is irreducible in Q[T]. Therefore [Q(µpr) : Q] = pr −pr−1 = |(Z/(pr))×|, so the embedding
Gal(Q(µpr)/Q) ,→(Z/(pr))× is an isomorphism. This is an alternate proof of Theorem 2.5
when n is a prime power that is simpler than the proof we gave before.
Cyclotomic polynomials can be used to prove some results that don’t appear to be about
roots of unity in the ﬁrst place. One such result is an elementary proof that for each n > 1
there are inﬁnitely many primes p ≡1 mod n [6, Cor. 2.11]. A second result is a proof of
Wedderburn’s theorem that all ﬁnite division rings are commutative [3, Thm. 13.1].
Since cyclotomic polynomials are in Z[T], let’s reduce them modulo p and ask how they
factor. It suﬃces to look at Φn(T) = Φn(T) mod p when (p, n) = 1 since reducing the

<!-- page 11 -->
CYCLOTOMIC EXTENSIONS
11
seventh algebraic identity for cyclotomic polynomials at the start of this section gives us
(5.1)
Φprm(T) = Φm(T)pr−pr−1 mod p
in Fp[T] when (p, m) = 1.
Theorem 5.4. When the prime p does not divide n, the monic irreducible factors of
Φn(T) ∈Fp[T] are distinct and each has degree equal to the order of p mod n.
Proof. Since Φn(T) | (T n −1) in Z[T], this divisibility relation is preserved when reducing
modulo p, so Φn(T) is separable in Fp[T] because T n −1 is separable in Fp[T]. (Here we
need (p, n) = 1.)
Let α be a root of Φn(T) in an extension of Fp.
We will show that α inherits the
expected algebraic property of being a primitive nth root of unity. Since Φn(T) | T n −1,
from Φn(α) = 0 we have αn = 1. If α were not of order n then it has some order m that
properly divides n. Then α is a root of T m −1 = Q
d|m Φd(T), so Φd(α) = 0 for some d
properly dividing n. Since d | n, T n −1 is divisible by Φn(T)Φd(T), so α is a double root
of T n −1, but T n −1 has no repeated roots. Therefore we have a contradiction, so α is a
primitive nth root of unity.
Let π(T) be an irreducible factor of Φn(T) in Fp[T] and let α denote a root of π(T).
Then α is a primitive nth root of unity, so deg π = [Fp(α) : Fp] is the order of p mod n by
Theorem 2.8.
□
Example 5.5. The polynomial Φ5(T) = T 4+T 3+T 2+T +1 factors over Fp into irreducible
factors whose degrees equal the order of p mod 5. For example, T 4 + T 3 + T 2 + T + 1 is
irreducible in F3[T] since 3 mod 5 has order 4, while
T 4 + T 3 + T 2 + T + 1 = (T −3)(T −4)(T −5)(T −9)
in F11[T] with irreducible factors of degree 1 since 11 mod 5 has order 1, and
T 4 + T 3 + T 2 + T + 1 = (T 2 + 5T + 1)(T 2 + 15T + 1)
in F19[T] with irreducible factors of degree 2 since 19 mod 5 has order 2.
Example 5.6. The polynomial Φ7(T) = T 6 + T 5 + T 4 + T 3 + T 2 + T + 1 factors over Fp
into irreducible factors whose degrees equal the order of p mod 7. For example, 2 mod 7 has
order 3 so Φ7(T) factors over F2 into a product of irreducible cubics:
T 6 + T 5 + T 4 + T 3 + T 2 + T + 1 = (T 3 + T + 1)(T 3 + T 2 + 1)
in F2[T]. This explains what happened in Example 2.9: if ζ is a primitive 7th root of unity
in characteristic 2, then it and ζ3 are roots of the two diﬀerent cubics on the right side: one
has roots ζ, ζ2, and ζ4, while the other has roots ζ3, (ζ3)2 = ζ6, and (ζ3)4 = ζ5.
Corollary 5.7. The reduction Φn(T) is irreducible in Fp[T] if and only if (p, n) = 1 and
p mod n is a generator of (Z/(n))×.
Proof. If Φn(T) is irreducible in Fp[T] then (p, n) = 1 by (5.1), so Theorem 5.4 tells us
the order of p mod n is ϕ(n): p mod n generates (Z/(n))×. Conversely, if (p, n) = 1 and
p mod n is a generator of (Z/(n))× then Theorem 5.4 tells us the irreducible factors of
Φn(T) in Fp[T] have degree ϕ(n) = deg(Φn(T)), so Φn(T) is irreducible.
□

<!-- page 12 -->
12
KEITH CONRAD
Thus many cyclotomic polynomials are examples of irreducible polynomials in Z[T] that
factor modulo every prime: if (Z/(n))× is not a cyclic group then there is no generator for
(Z/(n))×, so Corollary 5.7 says there is no prime p such that Φn(T) mod p is irreducible.
In other words, Φn(T) mod p factors for all primes p.
Example 5.8. The least n such that (Z/(n))× is non-cyclic is n = 8, and Φ8(T) = T 4 + 1.
This polynomial is reducible mod p for all p. Here are some factorizations of T 4 + 1 mod p.
Φ8(T) ≡(T + 1)4 mod 2,
Φ8(T) ≡(T 2 + T + 2)(T 2 + 2T + 2) mod 3,
Φ8(T) ≡(T 2 + 2)(T 2 + 3) mod 5,
Φ8(T) ≡(T 2 + 3T + 1)(T 2 + 4T + 1) mod 7,
Φ8(T) ≡(T 2 + 3T + 10)(T 2 + 8T + 10) mod 11,
Φ8(T) ≡(T −2)(T −8)(T −9)(T −15) mod 17,
Φ8(T) ≡(T 2 + 6T + 18)(T 2 + 13T + 18) mod 19,
Φ8(T) ≡(T 2 + 5T + 1)(T 2 + 18T + 1) mod 23,
Φ8(T) ≡(T 2 + 12)(T 2 + 17) mod 29,
Φ8(T) ≡(T 2 + 8T + 1)(T 2 + 23T + 1) mod 31.
References
[1] Z. I. Borevich and I. R. Shafarevich, “Number Theory,” Academic Press, New York, 1966.
[2] R. Dedekind, Beweis f¨ur die Irreductibilit¨at der Kreisteilungs-Gleichungen, J. Reine Angew. Math. 54
(1857), 27–30.
[3] T. Y. Lam, “A First Course in Noncommutative Rings,” Springer-Verlag, New York, 1991.
[4] T. Y. Lam and K. H. Cheung, On the cyclotomic polynomial Φpq(T), Amer. Math. Monthly 103 (1996),
562–564.
[5] E. Landau, ¨Uber die Irreduzibilit¨at der Kreisteilungsgleichung, Math. Zeitschrift 29 (1929), 462.
[6] L. Washington, “Introduction to Cyclotomic Fields,” 2nd ed., Springer-Verlag, New York, 1997.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*