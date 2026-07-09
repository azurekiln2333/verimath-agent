# Gaussnormlemma

> **Source**: https://kconrad.math.uconn.edu/blurbs/gaussnormlemma.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE GAUSS NORM AND GAUSS’S LEMMA
KEITH CONRAD
In algebra, the name “Gauss’s Lemma” is used to describe any of a circle of related results
about polynomials with integral coeﬃcients. Here are three.
The ﬁrst result, which can be found in [1, p. 528], says that a factorization in Q[T] of a
polynomial in Z[T] can be adjusted to be a factorization in Z[T] just by scaling the factors.
Theorem 1. If f(T) ∈Z[T] is nonzero and f(T) = g(T)h(T) in Q[T] then f(T) =
G(T)H(T) where G(T) and H(T) are in Z[T], G is a scalar multiple of g in Q[T] and H
is a scalar multiple of h in Q[T].
Example 2. Let f(T) = T 2 −4. Then f(T) = (3T −6)(T/3 −2/3) is a factorization
in Q[T]. Multiplying the ﬁrst factor by 1/3 and the second factor by 3, we get the more
familiar factorization f(T) = (T −2)(T + 2) in Z[T].
The second result, which is in [3, p. 40], is about primitive polynomials. A polynomial in
Z[T] is called primitive when its coeﬃcients are relatively prime when considered together.
For example, 6T 2 + 10T + 15 is primitive; even though each pair of coeﬃcients is not
relatively prime, the triple of coeﬃcients (6, 10, 15) is relatively prime and that makes the
polynomial primitive.
Theorem 3. If f(T) and g(T) are primitive in Z[T] then f(T)g(T) is primitive.
The third result was essentially stated by Gauss himself [2, Article 42].
Theorem 4. If f(T) is monic in Z[T] and f(T) = g(T)h(T) in Q[T] where g(T) and h(T)
are monic, then g(T) and h(T) are in Z[T].
We will prove these theorems with an extension of the p-adic absolute value from Q to
Q[T].
Deﬁnition 5. For a polynomial f(T) = P anT n in Q[T] and a prime p, deﬁne the p-adic
Gauss norm of f to be |f|p = maxn |an|p.
In this deﬁnition we are not specifying the degree of the polynomial f, but it doesn’t
matter since the maximum in the deﬁnition of |f|p is unaﬀected by additional coeﬃcients
that are 0. If f(T) = c is constant then |f|p = |c|p, so | · |p on Q[T] restricts to the p-adic
absolute value on Q.
Example 6. If f(T) = 6T 2 −(5/3)T + 4/7, we have |f|2 = max(1/2, 1, 1/4) = 1, |f|3 =
max(1/3, 3, 1) = 3, |f|5 = max(1, 1/5, 1) = 1, |f|7 = max(1, 1, 7) = 7, and |f|p = 1 for all
p > 7. Note Q
p |f|p = 21 and 21f(T) = 126T 2 −35T + 12 is a scalar multiple of f(T) with
integral coeﬃcients that is primitive. This idea will be used later.
To get used to the meaning of the p-adic Gauss norms as p varies, we show how to use
them to describe being primitive in Z[T].
Theorem 7. A polynomial f(T) in Q[T] is primitive in Z[T] if and only if |f|p = 1 for all
primes p.
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. If f is primitive in Z[T] then for each prime p we have |f|p = 1 because all the
coeﬃcients of f are integers (so |f|p ≤1) and at least one of its coeﬃcients is not divisible
by p (so |f|p = 1).
Conversely, assume for each prime p that |f|p = 1. Then each coeﬃcient of f has p-adic
absolute value at most 1 for all p, so each coeﬃcient of f is a p-adic integer for all p. A
rational number that is in Zp for all p is in Z, so f(T) ∈Z[T]. If f(T) were not primitive
then its coeﬃcients would share a common prime factor p and then |f|p < 1 for that p.
Therefore the assumption that |f|p = 1 for all p implies f is primitive.
□
Clearly |f|p ≥0 with equality if and only if f = 0, and easily |f + g|p ≤max(|f|p, |g|p)
and |fg|p ≤|f|p|g|p by the formulas for adding and multiplying polynomials together with
the strong triangle inequality. Perhaps surprisingly, | · |p is actually multiplicative on Q[T].
Theorem 8. For f and g in Q[T], |fg|p = |f|p|g|p.
Proof. If f = 0 or g = 0 then the equality is obvious, so we can assume f and g each have
some nonzero coeﬃcients: |f|p > 0 and |g|p > 0.
Write f(T) = P amT m and g(T) = P bnT n. (We don’t specify where the polynomials
stop; coeﬃcients equal 0 in large degrees.) Since |fg|p ≤|f|p|g|p, to prove |fg|p = |f|p|g|p
we seek a coeﬃcient in fg with absolute value |f|p|g|p. We will do this in two ways.
Method 1: Focus on where coeﬃcients of maximal absolute value in f and g ﬁrst occur.
Set |f|p = |aM|p with M minimal and |g|p = |bN|p with N minimal: |am|p < |aM|p for
m < M and |bn|p < |bN|p for n < N. (If either M or N is 0 then such an inequality is an
empty condition.) We seek a coeﬃcient in fg with absolute value |f|p|g|p and will ﬁnd it
in degree M + N.
The coeﬃcient of T M+N in fg is PM+N
m=0 ambM+N−m. The term in this sum at m = M
is aMbN. For 0 ≤m < M,
|ambM+N−m|p = |am|p|bM+N−m|p ≤|am|p|g|p = |am|p|bN|p < |aM|p|bN|p.
For M < m ≤M + N we have 0 ≤M + N −m < N, so
|ambM+N−m|p = |am|p|bM+N−m|p ≤|f|p|bM+N−m|p = |aM|p|bM+N−m|p < |aM|p|bN|p.
Thus |ambM+N−m|p < |aMbN|p for 0 ≤m ≤M + N with m ̸= M, so by the strong triangle
inequality we get

M+N
X
m=0
ambM+N−m

p
= |aMbN|p = |aM|p|bN|p = |f|p|g|p.
Method 2: Focus on where coeﬃcients of maximal absolute value in f and g last occur.
Now set |f|p = |aM|p with M maximal and |g|p = |bN|p with N maximal: |am|p < |aM|p
for m > M and |bn|p < |bN|p for n > N. We’ll see that a coeﬃcient in fg of p-adic absolute
value |f|p|g|p occurs in degree M + N.
The coeﬃcient of T M+N in fg is PM+N
m=0 ambM+N−m and the term in this sum at m = M
is aMbN. If 0 ≤m < M then M + N −m > N, so
|ambM+N−m|p = |am|p|bM+N−m|p ≤|f|p|bM+N−n|p = |aM|p|bM+N−n|p < |aM|p|bN|p.
For M < m ≤M + N,
|ambM+N−m|p = |am|p|bM+N−m|p ≤|am|p|g|p = |am|p|bN|p < |aM|p|bN|p.

<!-- page 3 -->
THE GAUSS NORM AND GAUSS’S LEMMA
3
Thus |ambM+N−m|p < |aMbN|p for 0 ≤m ≤M + N with m ̸= M, so by the strong triangle
inequality we get

M+N
X
m=0
ambM+N−m

p
= |aMbN|p = |aM|p|bN|p = |f|p|g|p.
□
The proof of Theorem 8 did not need the coeﬃcients to be rational: Deﬁnition 5 for the
prime p makes sense on Qp[T], not just Q[T] (where p can vary), and Theorem 8 holds on
Qp[T] by the same proof. While we only need one of the methods in the proof of Theorem 8,
there are generalizations of Theorem 8 from polynomials to diﬀerent types of p-adic power
series – the formal power series Zp[[T]] and the restricted power series Qp⟨T⟩– where one
method works and the other doesn’t, so both are worthwhile. Gauss himself used the ﬁrst
method (on polynomials).
Remark 9. We can extend the ordinary absolute value on Q to Q[T] in the same way as we
did | · |p and the ordinary triangle inequality |f + g| ≤|f| + |g| trivially holds, but behavior
under multiplication is bad: |T + 1| = 1 but |(T + 1)n| = |T n + nT n−1 + · · · + 1| ≥n, so
|(T + 1)n| →∞as n →∞.
To prove Theorem 1 we use the following result that shows how to systematically scale a
polynomial in Q[T] to a primitive polynomial in Z[T] using all the Gauss norms on Q[T].
Lemma 10. For f(T) ∈Q[T] set A = Q
p |f|p. Then Af(T) is in Z[T] and is primitive.
The product over all p deﬁning A makes sense since |f|p = 1 for all but ﬁnitely many p.
Proof. For each integer n, the fact that |pn|p = 1/pn and |qn|p = 1 for primes q ̸= p tells us
that |A|p = ||f|p|p = 1/|f|p . Thus |Af|p = |A|p|f|p = 1 for all p, so Af(T) is primitive in
Z[T] by Theorem 7.
□
Proof of Theorem 1. Let A = Q
p |f|p, B = Q
p |g|p, and C = Q
p |h|p. Since |f|p =
|g|p|h|p for all p, taking the product of both sides over all p implies A = BC.
By Lemma 10, the polynomials F(T) = Af(T), G(T) = Bg(T), and H(T) = Ch(T)
are all in Z[T]. From f = gh we get F(T)/A = (G(T)/B)(H(T)/C) = G(T)H(T)/BC =
G(T)H(T)/A, so F(T) = G(T)H(T). Thus
f(T) = 1
AF(T) = 1
AG(T)H(T).
The coeﬃcients of f are integers, so 1/|f|p ∈Z for all p and thus 1/A ∈Z. Therefore
(1/A)G(T) ∈Z[T], so renaming (1/A)G(T) as G(T) we are done.
Proof of Theorem 3. By (⇒) in Theorem 7, |f|p = 1 and |g|p = 1 for each prime p.
Thus |fg|p = |f|p|g|p = 1 for all p, so fg is primitive by (⇐) in Theorem 7.
Proof of Theorem 4. A monic in Z[T] is primitive, so |f|p = 1 for all p. Therefore
|g|p|h|p = 1. Since g and h are monic, |g|p ≥1 and |h|p ≥1, so the equation |g|p|h|p = 1
implies |g|p = 1 and |h|p = 1 for all p. Thus g and h are in Z[T] by (⇐) in Theorem 7.
References
[1] D. A. Cox, Galois Theory, 2nd ed., Wiley, 2012.
[2] C. F. Gauss, Disquisitiones Arithmeticae, Yale Univ. Press, 1966.
[3] J. Rotman, Galois Theory, 2nd ed., Springer, 2013.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*