# Irredtestsoverq

> **Source**: https://kconrad.math.uconn.edu/blurbs/irredtestsoverQ.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
IRREDUCIBILITY TESTS IN Q[T]
KEITH CONRAD
1. Introduction
For a general ﬁeld F there is no simple way to determine if an arbitrary polynomial
in F[T] is irreducible.
Here we will focus on the case F = Q and describe two useful
irreducibility tests in Q[T] for monic polynomials in Z[T]. Let
f(T) = T n + an−1T n−1 + · · · + a1T + a0 ∈Z[T].
The two tests are
• Reduction mod p: for a prime p, reducing coeﬃcients of f(T) modulo p leads to
f(T) = T n + an−1T n−1 + · · · + a0 ∈(Z/pZ)[T].
If f(T) is irreducible in (Z/pZ)[T] for some p, then f is irreducible in Q[T].
• Eisenstein criterion: call f(T) Eisenstein at p if p | ai for all i and p2 ∤a0. If f is
Eisenstein for some p, then f is irreducible in Q[T].
These tests each depend on a choice of a prime number, but they use the prime number
in diﬀerent ways.
Example 1.1. The polynomial T 3 +T +1 is irreducible in (Z/2Z)[T], so every monic cubic
in Z[T] that reduces modulo 2 to T 3+T +1 is irreducible in Q[T], such as T 3−4T 2+3T +1.
Example 1.2. The polynomial T 6 + T + 1 is irreducible in Q[T] because it is irreducible
in (Z/2Z)[T]. To show irreducibility in (Z/2Z)[T], we just have to check it is not divisible
by any irreducibles of degree 1, 2, or 3 in (Z/2Z)[T]: there are two irreducibles of degree 1
(T and T + 1), one irreducible of degree 2 (T 2 + T + 1), and two irreducibles of degree 3
(T 3 + T + 1 and T 3 + T 2 + 1). This leaves us with a ﬁnite amount of computation, which
you should go through yourself.
Example 1.3. Let f(T) = T 3 −2. Then
f(T)
≡
T 3 mod 2,
f(T)
≡
T 3 + 1 mod 3
≡
(T + 1)(T 2 −T + 1) mod 3,
f(T)
≡
(T −3)(T 2 + 3T + 9) mod 5,
so f is reducible mod p for p = 2, 3, 5. However f(T) mod 7 is irreducible since f mod 7 has
degree 3 in (Z/7Z)[T] and has no root in Z/7Z: that is a ﬁnite check since Z/7Z is ﬁnite.
By the reduction mod p test at p = 7, T 3 −2 is irreducible in Q[T].
Remark 1.4. There are monic polynomials in Z[T] that are irreducible in Q[T] but are
reducible mod p for all p, e.g., T 4 −10T 2 + 1. So the reduction mod p test does not always
apply.
1

<!-- page 2 -->
2
KEITH CONRAD
Example 1.5. T 3 −2 is Eisenstein at 2, so it’s irreducible in Q[T]. This is a much easier
method for T 3 −2 than reduction mod p (Example 1.3).
Example 1.6. T n −2 is Eisenstein at 2 for any n ≥1, so it is irreducible in Q[T].
The usefulness of the Eisenstein criterion is that it lets us create irreducibles in Q[T] of
any degree we wish. (Note T −2 is Eisenstein at 2: the test could be used in degree 1, but
it is not necessary since all linear polynomials over a ﬁeld are irreducible.)
Example 1.7. An Eisenstein polynomial at 3 is T 19 + 6T 10 −9T 4 + 75.
2. Gauss’ Lemma
To prove the reduction mod p test and the Eisenstein criterion, we will prove the poly-
nomial in each test can’t be decomposed into lower-degree factors in Z[T]. How come that
implies irreducibility in Q[T]?
For comparison, T 2 + 1 is irreducible in R[T] but if we
enlarge R to C then T 2 +1 = (T +i)(T −i) in C[T] and the polynomial becomes reducible.
Passing from Z[T] to Q[T] never turns irreducibility into reducibility. This is traditionally
called Gauss’ lemma.
Theorem 2.1 (Gauss). If f(T) ∈Z[T] is monic and f(T) = g(T)h(T) in Q[T] where
deg g < deg f and deg h < deg f then we can write f(T) = g1(T)h1(T) in Z[T], where g1(T)
and h1(T) are scalar multiples of g(T) and h(T), respectively; in particular, deg g1(T) =
deg g(T) < deg f(T) and deg h1(T) = deg h(T) < deg f(T).
Therefore if a monic polynomial in Z[T] can’t be written as a product of lower-degree
polynomials in Z[T], it is irreducible in Q[T].
As an example, T 2 −1 in Q[T] is ((4/3)T −4/3)((3/4)T + 3/4), having linear factors,
and in Z[T] it is (T + 1)(T −1), also having linear factors.
Proof. Step 1: Use common denominators to factor a scalar multiple of f(T) in Z[T].
Let d and e be common denominators of the coeﬃcients of g(T) and h(T), respectively,
so g(T) = g0(T)/d and h(T) = h0(T)/e where g0(T) and h0(T) are both in Z[T]. Thus
f(T) = g(T)h(T) = g0(T)
d
h0(T)
e
=⇒def(T) = g0(T)h0(T).
This last equation takes place in Z[T].
Step 2: Use greatest common divisors to get factors of f(T) whose coeﬃcients are
relatively prime.
Factor out the greatest common divisor of the coeﬃcients of g0(T) and of the coeﬃcients
of h0(T):
g0(T) = ag1(T) and h0(T) = bh1(T) where a, b ∈Z+, the coeﬃcients of g1(T)
are relatively prime, and the coeﬃcients of h1(T) are relatively prime. Then
(2.1)
def(T) = g0(T)h0(T) = abg1(T)h1(T).
Step 3: Obtain a factorization of f(T) in Z[T].
We will show de = ab, so canceling this (nonzero) factor from both sides gives us f(T) =
g1(T)h1(T) in Z[T] where g1(T) = g0(T)/a = (d/a)g(T) and h1(T) = h0(T)/b = (e/b)h(T)
are scalar multiples of g(T) and h(T).
Since f(T) is monic, looking at the leading coeﬃcient on both sides of (2.1) we get
de = ab(lead g1)(lead h1)
in Z,

<!-- page 3 -->
IRREDUCIBILITY TESTS IN Q[T]
3
so ab | de. Let c = de/ab ∈Z+, so c ≥1 and (2.1) implies
(2.2)
cf(T) = g1(T)h1(T).
If c > 1 then it has a prime factor, say p. Reduce both sides of (2.2) modulo p: this turns
(2.2) into 0 = g1(T)h1(T) in (Z/pZ)[T]. Since (Z/pZ)[T] is an integral domain, one of g1(T)
or h1(T) is 0, which is another way of saying all the coeﬃcients of g1(T) are divisible by p
or all the coeﬃcients of h1(T) are divisible by p. Neither is possible, since the coeﬃcients
of g1(T) are relatively prime and the coeﬃcients of h1(T) are relatively prime. Therefore
c has no prime factor, so c = 1 and f(T) = g1(T)h1(T) is a factorization of f(T) in Z[T]
where the factors g1(T) and h1(T) are scalar multiples of g(T) and h(T).
□
A good way to think about the later part of this proof is that we applied the reduction
mod p homomorphism to turn an equation in Z[T] into an equation in (Z/pZ)[T] for a
suitably chosen prime p. We will apply this same idea in the proofs of both the reduction
mod p test and the Eisenstein criterion.
3. Reduction mod p
Theorem 3.1. If f(T) ∈Z[T] is monic and there is a prime p such that f(T) is irreducible
in (Z/pZ)[T] then f(T) is irreducible in Q[T].
Proof. By Gauss’ lemma, to prove f(T) is irreducible in Q[T] it suﬃces to show we can’t
write f(T) as a product of lower-degree factors in Z[T].
Assume f = gh for some g, h ∈Z[T] with deg g < deg f and deg h < deg f. We will get
a contradiction from this.
Looking at the leading coeﬃcients on both sides of f = gh we have 1 = (lead g)(lead h) in
Z, so g and h both have leading coeﬃcient 1 or both have leading coeﬃcient −1. Therefore,
after changing the signs on g and h if necessary, we can assume g and h are both monic in
Z[T]. Reduction mod p is a ring homomorphism Z[T] →(Z/pZ)[T], so it turns the equation
f = gh in Z[T] into f = gh in (Z/pZ)[T]. Since f is irreducible, one of g or h has degree 0
and the other has degree equal to that of f. Because f, g and h are all monic,
deg f
=
deg f,
deg g
=
deg g,
deg h
=
deg h.
Therefore one of g or h has degree equal to the degree of f, but this contradicts g and h
both having degree less than deg f.
□
4. The Eisenstein criterion
Theorem 4.1. If f(T) ∈Z[T] is monic and Eisenstein at a prime p then f(T) is irreducible
in Q[T].
Proof. By Gauss’ lemma it suﬃces, as in the proof of the reduction mod p test, to work in
Z[T]: assume f = gh for some g, h ∈Z[T] with deg g < deg f and deg h < deg f and get
a contradiction. As in the proof of the reduction mod p test, we can assume g and h are
both monic.
Write
f(T) = T n + an−1T n−1 + · · · a1T + a0 ∈Z[T]

<!-- page 4 -->
4
KEITH CONRAD
so p | ai for all i and p2 ∤a0. Passing from Z[T] to (Z/pZ)[T] by reduction mod p, the
equation f = gh implies f = gh in (Z/pZ)[T], so T n = gh in (Z/pZ)[T], and g and h are
monic since g and h are monic. Since T is irreducible in (Z/pZ)[T], unique factorization in
(Z/pZ)[T] tells us the only monic factors of T n in (Z/pZ)[T] are powers of T, so g = T r
and h = T s where
r = deg g = deg g > 0
and
s = deg h = deg h > 0.
Saying g = T r and h = T s means g and h have all of their non-leading coeﬃcients divisible
by p. So from r, s > 0 we see g(0) and h(0) are divisible by p. Thus
a0 = f(0) = g(0)h(0) ≡0 mod p2,
which is a contradiction of the Eisenstein condition.
□
Remark 4.2. The reduction mod p test and the Eisenstein criterion can be extended to
cover f(T) in Z[T] that are not necessarily monic by adding the condition that the leading
coeﬃcient of f(T) is not divisible by the prime being used (automatic if f(T) is monic).
(i) (Reduction mod p) If f(T) has leading coeﬃcient not divisible by a prime p and
f(T) is irreducible in (Z/pZ)[T] then f(T) is irreducible in Q[T]. For example,
5T 4 −T + 4 is irreducible in Q[T] since it is irreducible mod 3 (even though the
reduction mod 3 is not monic).
(ii) (Eisenstein) Call a non-constant f(T) in Z[T] Eisenstein at a prime p if its leading
coeﬃcient is not divisible by p, all lower-degree coeﬃcients are divisible by p, and the
constant term is not divisible by p2. For example, 3T 4−10T 2+15 is Eisenstein at 5.
The Eisenstein criterion says that every nonconstant polynomial that is Eisenstein
at some prime is irreducible in Q[T].
The proofs above can be modiﬁed to apply to non-monic f(T) by ﬁrst proving a version
of Gauss’ lemma that applies to non-monic polynomials in Z[T]. See the appendix.
5. Enough prime values implies irreducibility
The polynomial T 2 +1 is irreducible in Z[T], but that doesn’t mean its values at integers
have to be prime numbers: a2 + 1 is composite for all odd a ≥3 since m2 + 1 is even and
greater than 2. However, a2 + 1 is prime for many values of a, such as a = 1, 2, 4, 6, and 10.
It turns out if a polynomial in Z[T] takes enough prime values that proves its irreducibility!
Theorem 5.1. If f(T) ∈Z[T] is primitive of degree d ≥1 and there are at least 2d + 1
diﬀerent integers a such that |f(a)| is 1 or a prime number then f(T) is irreducible in Q[T].
Proof. By Gauss’ lemma it suﬃces to prove f(T) is irreducible in Z[T] to know it is irre-
ducible in Q[T]. Suppose f(T) = g(T)h(T) in Z[T] where deg g < deg f and deg h < deg f.
Then f(a) = g(a)h(a) for all a ∈Z. If |f(a)| is 1 or a prime number then g(a) = ±1 or
h(a) = ±1. Since g(T) assumes each value on Z at most deg g times and h(T) assumes each
value on Z at most deg h times, the number of integers a such that g(a) = ±1 or h(a) = ±1
is at most 2 deg g + 2 deg h = 2 deg f = 2d. So if |f(a)| is 1 or a prime number 2d + 1 times
then we have a contradiction, and thus f(T) is irreducible in Q[T].
□
Example 5.2. To show T 4 −10T 2 + 1 is irreducible in Q[T], we have |a4 −10a2 + 1| = 1
or a prime number at a = 0, ±2, ±4, ±6, ±8, which is 2 · 4 + 1 = 9 values.
Remark 5.3. A discussion of how many prime values (up to sign) a reducible polynomial
in Z[T] can have is in [2, Theorem 1].

<!-- page 5 -->
IRREDUCIBILITY TESTS IN Q[T]
5
Theorem 5.1, like the reduction mod p test and Eisenstein criterion, it is not always
directly applicable to prove irreducbility. For example, T 2 + T + 4 is irreducible but takes
only even values when T runs over the integers and is never ±2. There is a conjecture, due to
Bunyakovsky, that describes when a polynomial in Z[T] should take prime values inﬁnitely
often, and a change of variables can convert any irreducible polynomial to a form where
Bunyakovsky’s conjecture is expected to apply (see the end of [1]). However, Theorem 5.1
appears to be limited to proving irreducibility of individual polynomials rather than families
of polynomials such as T n −2 as n varies, which can be treated by the Eisenstein criterion.
6. Going beyond integer coefficients
The rings Z and F[X] are analogous (e.g., both have division with remainder, leading
to similar proofs in both cases that all of their ideals are principal). Therefore F[X, Y ] =
F[X][Y ] = F[Y ][X] is analogous to Z[X]. Our two irreducibility tests, regarded as tests for
irreducibility in Z[T] rather than in Q[T], can be adapted to F[X, Y ] by viewing a polyno-
mial in F[X, Y ] as a polynomial in one indeterminate whose coeﬃcients are polynomials in
the other indeterminate.
(i) (Reduction mod π(Y )) If f(X, Y ) ∈F[X, Y ] is monic in X and there is an irreducible
π(Y ) ∈F[Y ] such that f(X, Y ) mod π(Y ) ∈(F[Y ]/πF[Y ])[X] is irreducible, then
f(X, Y ) is irreducible in F[X, Y ].
(ii) (Eisenstein) If f(X, Y ) ∈F[X, Y ] is monic in X and, when written as Xn +
an−1(Y )Xn−1+· · ·+a1(Y )X+a0(Y ) in F[Y ][X], there is an irreducible π(Y ) ∈F[Y ]
such that π(Y ) | ai(Y ) for all i and π(Y )2 ∤a0(Y ) then f(X, Y ) is irreducible in
F[X, Y ].
The proofs of these irreducibility tests are very similar to the proofs over Q, using F[Y ]
in place of Z and depending on a suitable form of Gauss’ lemma: a polynomial in F[Y ][X]
that is monic in X and decomposes in F(Y )[X] into two factors with lower X-degree can be
rescaled to such a decomposition in F[Y ][X]. It is left to the reader to work out the proofs
of this version of Gauss lemma and of both irreducibility tests above. Here are examples to
illustrate the tests.
Example 6.1. The polynomial Xn + (Y + 5)X + (Y −1) in Q[X, Y ] is irreducible because
when we reduce it modulo Y +1 then in (Q[Y ]/(Y +1))[X] ∼= Q[X] it becomes Xn+4X −2,
which is irreducible over Q by the classical Eisenstein criterion at 2.
Example 6.2. For all n ≥1, the polynomial Xn −Y is irreducible in C[X, Y ] because it is
Eisenstein at Y : as a polynomial in X, its constant term is −Y (divisible by Y just once)
and all of its other non-leading coeﬃcients in X are 0 (all divisible by Y ).
Example 6.3. For all n ≥1, the polynomial Xn +Y n −1 is irreducible in C[X, Y ] because
it is Eisenstein at Y −1: as a polynomial in X, its constant term Y n −1 is divisible by
Y −1 exactly once and all of its other non-leading coeﬃcients in X are 0 (all divisible by
Y −1).
Both the reduction mod p test and the Eisenstein criterion can be generalized to K[T]
where K is a ﬁnite extension of Q, such as Q(i) or Q(
3√
2).1 However, formulating this
generalization correctly is beyond the scope of this handout. The main diﬃculty here is
1In fact, historically, the Eisenstein criterion was ﬁrst introduced by Eisenstein as a test for irreducibility of
polynomials in Q(i)[T], not Q[T].

<!-- page 6 -->
6
KEITH CONRAD
describing what the substitute for Z is in a ﬁnite extension of Q; it involves algebraic
integers, whose subtleties are explained in a course on algebraic number theory. Also prime
numbers in the irreducibility tests have to be replaced by prime ideals, and a prime number
might not generate a prime ideal in a ring larger than Z.
To illustrate a mistake caused by not properly understanding “primes” in ﬁnite extensions
of Q, f(T) = T 2 + 1 is irreducible in Q[T] because f(T + 1) = T 2 + 2T + 2 is Eisenstein
at 2, but it would be wrong to say T 2 + 1 is irreducible in Q(
√
2)[T] because f(T + 1) is
Eisenstein at 2 in Z[
√
2][T]: the number 2 is not prime in Z[
√
2], as 2 =
√
2
√
2.2 Until you
learn some algebraic number theory, be cautious about using either of the two irreducibility
tests from Q[T] directly in K[T] where K is a ﬁnite proper extension of Q.
7. Going too far beyond integer coefficients
While the previous section shows that the two irreducibility tests initially introduced for
polynomials in Z[T] have a broader scope, it is important not to push an irreducibility test
into a place where it makes no sense. In particular, DO NOT USE THE EISENSTEIN
CRITERION IN Fp[T]. Although T 3 −2T −2 is irreducible in F5[T] since it is cubic
without a root in F5, it is ﬂat-out wrong to say this polynomial is “Eisenstein at 2 in F5[T]”:
the number 2 in F5 is not prime there: 2 is invertible in Fp. The use of primality for the
(valid) Eisenstein criterion in Z[T] is a subtle interplay between the ﬁeld Q and its subring
Z whose ratios ﬁll up Q; the primes are from Z and Gauss’ lemma provides the reason that
we can pass from Q[T] to Z[T]. The ﬁeld F5 doesn’t have a subring analogous to Z with
primes in it.
Another way to see that saying T 3 −2T −2 is “Eisenstein at 2 in F5[T]” is a mistake is
that such reasoning should also apply over F3, and in F3[T] the polynomial T 3 −2T −2 is
reducible: T 3 −2T −2 ≡(T −1)(T 2 + T + 2) mod 3.
Appendix A. Relaxing the monicity condition
In Theorem 2.1 we presented Gauss’ lemma for monic polynomials in Z[T]. There is
a version of it that does not assume the polynomial is monic.
Instead we assume the
coeﬃcients have greatest common divisor 1.
Deﬁnition A.1. A polynomial f(T) = anT n + an−1T n−1 + · · · + a1T + a0 in Z[T] is called
primitive if gcd(a0, a1, . . . , an) = 1.
If any coeﬃcient is 1 then the polynomial is primitive. In particular, all monic polynomials
in Z[T] are primitive. An example of a primitive polynomial where no coeﬃcient is 1 is
6T 2 + 10T + 15: although each pair of coeﬃcients is not relatively prime, taken together
the triple (6, 10, 15) has greatest common divisor 1.
Theorem A.2. If f(T) ∈Z[T] is primitive and f(T) = g(T)h(T) in Q[T] where deg g <
deg f and deg h < deg f then we can write f(T) = g1(T)h1(T) in Z[T], where g1(T)
and h1(T) are scalar multiples of g(T) and h(T), respectively; in particular, deg g1(T) =
deg g(T) < deg f(T) and deg h1(T) = deg h(T) < deg f(T).
Therefore if a primitive polynomial in Z[T] can’t be written as a product of lower-degree
polynomials in Z[T], it is irreducible in Q[T].
2A valid reason that T 2 + 1 is irreducible over Q(
√
2) is that the polynomial has degree 2 and no root in
Q(
√
2), a subﬁeld of the real numbers.

<!-- page 7 -->
IRREDUCIBILITY TESTS IN Q[T]
7
Proof. We mimic the proof of Theorem 2.1. The reasoning in that proof leading to (2.1) did
not rely on f(T) being monic so it carries over. Let’s review the argument again: extracting
a common denominator in g(T) and h(T) lets us write g(T) = g0(T)/d and h(T) = h0(T)/e
where g0(T) and h0(T) are in Z[T] and d and e are in Z+, so
def(T) = g0(T)h0(T)
in Z[T]. Factoring out the greatest common divisor of the coeﬃcients of g0(T) and of h0(T)
lets us write g0(T) = ag1(T) and h0(T) = bh1(T), where a, b ∈Z+ and g1(T) and h1(T) are
primitive in Z[T]. Thus we get an analogue of (2.1):
(A.1)
def(T) = g0(T)h0(T) = abg1(T)h1(T).
where g1(T) = (d/a)g(T) and h1(T) = (e/b)h(T). From (A.1) we want to show de = ab, so
f(T) = g1(T)h1(T).
Write f(T) = anT n +an−1T n−1 +· · ·+a1T +a0, so gcd(a0, a1, . . . , an) = 1 by hypothesis.
In (A.1) the coeﬃcients on the left side are deai for i = 0, . . . , n while the coeﬃcients on
the right side are all multiples of ab. Therefore ab | deai for 0 ≤i ≤n, so ab is a factor of
gcd(dea0, dea1, . . . , dean) = de gcd(a0, a1, . . . , an) = de.
Set c = de/ab, so c ∈Z+ and (A.1) implies
(A.2)
cf(T) = g1(T)h1(T),
which looks just like (2.2). The rest of the proof of Theorem 2.1 after (2.2) can be repeated
here to prove c = 1, since all it depends on is g1(T) and h1(T) being primitive (no prime
number divides all the coeﬃcients of g1(T) or of h1(T)). Details are left to the reader. Thus
f(T) = g1(T)h1(T) in Z[T] with g1(T) a scalar multiple of g(T) and h1(T) a scalar multiple
of h(T).
□
Here is the reduction mod p test with an assumption of the polynomial being monic
replaced by the weaker assumption that it is primitive.
Theorem A.3. If f(T) ∈Z[T] is primitive and there is a prime p not dividing the leading
coeﬃcient of f(T) such that f(T) is irreducible in (Z/pZ)[T] then f(T) is irreducible in
Q[T].
Proof. The proof of Theorem 3.1 will carry over with a little more attention to the leading
coeﬃcients.
It suﬃces by Theorem A.2 to prove f(T) is not a product of lower-degree factors in Z[T]
in order to know it is not such a product in Q[T]. Assume f = gh for g, h ∈Z[T] with
deg g < deg f and deg h < deg f. Looking at the leading coeﬃcients on both sides of f = gh
we have lead f = (lead g)(lead h) in Z, so the leading coeﬃcients of g(T) and h(T) are not
divisible by p. Therefore the degrees of f, g and h don’t drop after reduction mod p:
deg f
=
deg f,
deg g
=
deg g,
deg h
=
deg h.
From f = gh in Z[T] we have f = gh in (Z/pZ)[T], and f being irreducible implies g or h
has degree 0 and the other has degree equal to that of f, which means g or h has degree
equal to that of f. That is a contradiction, just as in the proof of Theorem 3.1.
□

<!-- page 8 -->
8
KEITH CONRAD
Next we present the Eisenstein criterion without assuming the polynomial is monic. Call
f(T) = anT n + an−1T n−1 + · · · + a1T + a0 ∈Z[T]
an Eisenstein polynomial at a prime p if p ∤an, p | ai for i = 0, . . . , n −1, and p2 ∤a0.
The new condition here that we did not need to be explicit about in the monic case is that
p ∤an. For monic polynomials that condition is automatically satisﬁed when an = 1.
Theorem A.4. If f(T) ∈Z[T] is primitive and Eisenstein at a prime p then f(T) is
irreducible in Q[T].
Proof. Since f(T) is primitive, it suﬃces to assume f = gh for g, h ∈Z[T] with deg g < deg f
and deg h < deg f and get a contradiction. From the equation f = gh the leading coeﬃcients
of g and h are not divisible by p, so f, g, and h in Z[T] have the same respective degrees
as f, g, and h in (Z/pZ)[T].
Reducing both sides of f = gh modulo p, we get anT n = gh in (Z/pZ)[T]. By unique
factorization in (Z/pZ)[T], g = bT r and h = cT s for some nonzero constants b and c in
Z/pZ and nonnegative integers r and s. Then
r = deg g = deg g > 0
and
s = deg h = deg h > 0.
Therefore g(T) and h(T) both have constant term 0, so g(0) and h(0) vanish in Z/pZ. Thus
g(0) and h(0) are multiples of p (this is the same reasoning as in the proof of Theorem 4.1),
so
a0 = f(0) = g(0)h(0) ≡0 mod p2,
which contradicts the Eisenstein property of f(T).
□
All of these results carry over to F[X, Y ] as irreducibility tests for polynomials that are
primitive in X (meaning the coeﬃcients in F[Y ] have constant gcd). Formulations of the
results and their proofs are left to the reader. We give one example.
Example A.5. For n ≥2 the polynomial Y Xn+(Y +1)X +Y 2−1 in C[X, Y ] is irreducible
because it is primitive as a polynomial in X (the X-coeﬃcients Y , Y + 1, and Y 2 −1 are
collectively relatively prime in C[Y ]) and Eisenstein at Y + 1: the leading power of X is
not divisible by Y + 1, all other coeﬃcients are, and the constant term is divisible by Y + 1
but not (Y + 1)2.
References
[1] K. S. Brown, Irreducibility Criteria, http://www.mathpages.com/home/kmath406.htm.
[2] Y-G. Chen, G. Kun, G. Pete, I. Z. Ruzsa, and ´A. Tim´ar, ”Prime values of reducible polynomials, II,”
Acta Arith., 104 (2002), 117–127

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*