# Reducibleallp

> **Source**: https://kconrad.math.uconn.edu/blurbs/reducibleallp.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
AN IRREDUCIBLE THAT FACTORS MODULO ALL PRIMES
KEITH CONRAD
Let α =
√
2 +
√
3. To ﬁnd a monic polynomial in Q[T] with root α, start by squaring α:
α2 = 2 + 2
√
6 + 3 = 5 + 2
√
6 =⇒α2 −5 = 2
√
6
=⇒(α2 −5)2 = 24
=⇒α4 −10α2 + 25 = 24.
Thus α4−10α2+1 = 0, so
√
2+
√
3 is a root of T 4−10T 2+1. This polynomial has four roots
in R:
√
2+
√
3 ≈3.1462,
√
2−
√
3 ≈−.3178, −
√
2+
√
3 ≈.3178, and −
√
2−
√
3 ≈−3.1462.
Theorem 1. The polynomial T 4 −10T 2 + 1 is irreducible in Q[T].
Proof. If the polynomial were reducible, it could be expressed as a linear times a cubic in
Q[T] or as a product of two quadratics in Q[T].
If there were a linear factor in Q[T] then T 4 −10T 2 + 1 would have a rational root. But
the square of every root is 5 ± 2
√
6, which is irrational since
√
6 is irrational.
If T 4 −10T 2 +1 were a product of two quadratics in Q[T], then without loss of generality
those factors are both monic. There are four roots in R, so by unique factorization in R[T]
a monic quadratic factor in Q[T] must be (T −r)(T −s) for two of the real roots r and s.
Therefore in a factorization into monic quadratics, one of the two factors has root
√
2 +
√
3
and the factor with that root is one of the following:
(T −(
√
2 +
√
3))(T −(
√
2 −
√
3)) = T 2 −2
√
2T −1,
(T −(
√
2 +
√
3))(T −(−
√
2 +
√
3)) = T 2 −2
√
3T + 1,
(T −(
√
2 +
√
3))(T −(−
√
2 −
√
3)) = T 2 −(5 + 2
√
6).
All of these have an irrational coeﬃcient, so there are no quadratic factors in Q[T]. This
completes the proof that T 4 −10T 2 + 1 is irreducible in Q[T].
□
For T 4 −10T 2 + 1 neither standard irreducibility test in Q[T] – reduction mod p or the
Eisenstein criterion – can prove its irreducibility: for each prime p, T 4 −10T 2 + 1 mod p is
reducible and for no c ∈Z is (T + c)4 −10(T + c)2 + 1 Eisenstein at p.
Theorem 2. For each c ∈Z, (T + c)4 −10(T + c)2 + 1 not an Eisenstein polynomial.
Proof. Suppose for some c ∈Z and prime p that (T + c)4 −10(T + c)2 + 1 is Eisenstein at
a prime p. Since
(T + c)4 −10(T + c)2 + 1 = T 4 + 4cT 3 + (6c2 −10)T 2 + (4c3 −20c)T + (c4 −10c2 + 1)
= T 4 + 4cT 3 + 2(3c2 −5)T 2 + 4c(c2 −5)T + (c4 −10c2 + 1)
we have p | 4c, so p = 2 or p | c. If p | c then the constant term c4 −10c2 + 1 is not divisible
by p, which contradicts the Eisenstein condition at p. Therefore p = 2, so c4 −10c2 + 1 is
even, which implies c is odd. Then c2 ≡1 mod 8, so c4 −10c2 + 1 ≡1 −10 + 1 ≡0 mod 8,
which contradicts the Eisenstein condition at 2.
□

<!-- page 2 -->
2
KEITH CONRAD
Before we show T 4 −10T 2 + 1 mod p is reducible for every prime p, the data below for
p ≤43 support this claim.
p
T 4 −10T 2 + 1 mod p
p
T 4 −10T 2 + 1 mod p
2
(T + 1)4
19
(T 2 + 4)(T 2 + 5)
3
(T 2 + 1)2
23
(T + 2)(T −2)(T + 11)(T −11)
5
(T 2 + 2)(T 2 −2)
29
(T 2 + 8)(T 2 + 11)
7
(T 2 + T −1)(T 2 −T −1)
31
(T 2 + 15T −1)(T 2 −15T −1)
11
(T 2 + T + 1)(T 2 −T + 1)
37
(T 2 + 7T + 1)(T 2 −7T + 1)
13
(T 2 + 5T + 1)(T 2 −5T + 1)
41
(T 2 + 7T −1)(T 2 −7T −1)
17
(T 2 + 5T −1)(T 2 −5T −1)
43
(T 2 + 9)(T 2 + 24)
Theorem 3. For each prime p, T 4 −10T 2 + 1 mod p is reducible.
Proof. The polynomial T 4 −10T 2 + 1 has three monic quadratic factorizations in R[T],
found from the monic quadratic factors appearing in the proof of Theorem 2 and their
conjugates. Here are the monic quadratic factorizations:
T 4 −10T 2 + 1 = (T 2 −2
√
2T −1)(T 2 + 2
√
2T −1),
= (T 2 −2
√
3T + 1)(T 2 + 2
√
3T + 1),
= (T 2 −(5 + 2
√
6))(T 2 −(5 −2
√
6)).
For each prime p, at least one of these factorizations makes sense mod p. In Fp[T], the
ﬁrst factorization makes sense if 2 is a square mod p, the second factorization makes sense
if 3 is a square mod p, and the third factorization makes sense if 6 is a square mod p.
For example, take p = 7.
Since 2 ≡32 mod 7, if we replace
√
2 with 3 in the ﬁrst
quadratic factorization of T 4 −10T 2 + 1 and treat coeﬃcients as elements of F7 then
(T 2 −(2 · 3)T −1)(T 2 + (2 · 3)T −1) = (T 2 + T −1)(T 2 −T −1) mod 7
= T 4 −32 + 1 mod 7
= T 4 −102 + 1 mod 7.
Taking p = 5, since 6 ≡12 mod 5 we can replace
√
6 with 1 in the third quadratic factor-
ization of T 4 −10T 2 + 1 to get a factorization modulo 5:
(T 2 −(5 + 2 · 1))(T 2 −(5 −2 · 1)) = (T 2 −7)(T 2 −3) mod 5
= T 4 −102 + 21 mod 5
= T 4 −102 + 1 mod 5.
In elementary number theory, it can be shown that for each prime p and integers a and
b, if a mod p and b mod p are not squares mod p then ab mod p is a square mod p.1 Taking
a = 2 and b = 3, for each prime p at least one of 2, 3, or 6 has to be a square mod p,
and that gives meaning in Fp[T] to at least one of the monic quadratic factorizations of
T 4 −10T 2 + 1. Thus for each prime p, T 4 −10T 2 + 1 mod p is reducible.
□
In a similar way, for integers a and b such that a, b ,and ab are all not perfect squares,
√a +
√
b is a root of T 4 −2(a + b)T 2 + (a −b)2 and this polynomial is irreducible in Q[T]
and for all primes p it has no Eisenstein translate at p and it is reducible mod p.
1This is related to Euler’s criterion for quadratic residues.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*