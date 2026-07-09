# Irredselmerpoly

> **Source**: https://kconrad.math.uconn.edu/blurbs/irredselmerpoly.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
IRREDUCIBILITY OF xn −x −1
KEITH CONRAD
1. Introduction
In 1956, Selmer [2] proved the following irreducbility theorem.
Theorem 1.1 (Selmer). For all n ≥2, the polynomial xn −x −1 is irreducible in Q[x].
None of the standard irreducibility tests, such as reduction mod p or the Eisenstein
criterion, can be applied to xn −x −1 for general n. However, in a special case we can use
one of these tests: if n = p is prime then xp −x −1 is irreducible in Fp[x] and therefore is
irreducible in Q[x]. More generally, if a is an integer not divisible by p then xp −x −a is
irreducible in Q[x] because the polynomial is irreducible in Fp[x]: a proof of this is in many
books on abstract algebra or ﬁeld theory. Such a proof of irreducibility in Q[x] does not
extend to xpm −x −1 when m ≥2, since that polynomial is generally reducible in Fp[x].
Example 1.2. If an integer m ≥2 is not divisible by p then in characteristic p, a root of
xp −x −1/m is a root of xpm −x −1:
αp = α + 1
m =⇒αpk = α + k
m in characteristic p
for all k ≥1 by induction. Setting k = m gives us αpm = α+1. The polynomial xp−x−1/m
in Fp[x] is irreducible, so in Fp[x], xp −x −1/m is a nontrivial factor of xpm −x −1
2. Proof of irreducibility
Selmer’s original proof of Theorem 1.1 involves studying the distribution of the roots
of xn −x −1 in C, relying at the end on the arithmetic–geometric mean inequality. The
irreducibility proof that we give below is shorter and more algebraic. I learned it from
David Rohrlich, who in turn learned it from Michael Filaseta.
Proof. For nonzero f(x) = anxn + an−1xn−1 + · · · + a1x + a0 of degree n, let ef(x) be its
reciprocal polynomial:
ef(x) = a0xn + a1xn−1 + · · · + an−1x + an = xdeg ff(1/x).
We call ef(x) the reciprocal polynomial because its roots are the reciprocals of the roots of
f(x). More precisely, if f(x) has leading coeﬃcient a0 and f(0) ̸= 0 then
f(x) = a0(x −r1) · · · (x −rn) =⇒ef(x) = f(0)(x −1/r1) · · · (x −1/rn).
The following properties of this construction will be used below without comment:
• if f(0) ̸= 0 then deg f = deg ef and
≈
f = f,
• if f = gh then ef = egeh,
• for every nonzero constant c, f
cf = c ef,
1

<!-- page 2 -->
2
KEITH CONRAD
• if f(x) =
n
X
i=0
aixi has degree n then the xn-coeﬃcient of f(x) ef(x) is a2
0+a2
1+· · ·+a2
n.
Check all of these properties yourself. The last one is the most interesting.
The proof of the theorem will be presented in three steps.
Step 1: For n ≥2, xn −x −1 and its reciprocal polynomial have no common root in
characteristic 0.
The reciprocal polynomial is −xn −xn−1 + 1. If this shares a root with xn −x −1 in
characteristic 0, say α, then
(2.1)
αn = α + 1 and αn = −αn−1 + 1,
so −αn−1 = α. Thus αn = −α2. Substituting this into either equation in (2.1) gives us
−α2 = α+1, which implies α3 = 1, so every power of α is either 1, α, or α2. If αn = 1 then
the ﬁrst equation in (2.1) becomes 1 = α + 1, which is false since α ̸= 0. If αn = α then
α = α + 1, which is absurd. If αn = α2 then the two equations in (2.1) become α2 = α + 1
and α2 = −α + 1, so α = −α, but α ̸= 0. Thus a common root α in characteristic 0 doesn’t
exist.
Step 2: For f(x) ∈Z[x], assume f(0) ̸= 0 and f(x) and ef(x) have no common roots in
characteristic 0. If f(x) = g(x)h(x) for some nonconstant g(x) and h(x) in Z[x], then there
is a k(x) in Z[x] with deg k = deg f such that f ef = kek and k ̸= ±f or ± ef.
Since f(0) ̸= 0, both g(0) and h(0) are not 0, so deg eg = deg g and deg eh = deg h. Deﬁne
k(x) = g(x)eh(x).
Then deg k = deg g + deg eh = deg g + deg h = deg f and kek = (geh)(egh) = (gh)(egeh) = f ef. If
k and f are equal up to sign then geh and gh are equal up to sign, so eh and h are equal up
to sign, but then every root of h (it has roots since h is nonconstant) would be a common
root of f = gh and ef = egeh, which is a contradiction. The proof that k and ef are not equal
up to sign is similar with g in place of h.
Step 3: The polynomial xn −x −1, for n ≥2, is irreducible in Q[x].
We argue by contradiction, and can assume n > 2 since the case n = 2 can be checked
directly. If xn −x −1 is reducible in Q[x] then it factors into a product of two nonconstant
polynomials in Z[x]. Set f(x) = xn −x −1. By Steps 1 and 2, f ef = kek for some k ∈Z[x]
of degree n where k is not ±f or ± ef. Write k(x) = bnxn + bn−1xn−1 + · · · + b1x + b0, so
ek(x) = b0xn + b1xn−1 + · · · + bn−1x + bn. Then k(0)ek(0) = b0bn = f(0) ef(0) = (−1)(1) = −1
in Z, so bn = ±1 and b0 = −bn. Replacing k with −k doesn’t change deg k or kek, so with
a sign change we can make k monic: bn = 1. Then b0 = −1.
Comparing the coeﬃcients of xn in both f ef and kek,
12 + (−1)2 + (−1)2 = b2
0 + b2
1 + · · · + b2
n.
Since b2
n = 1 and b2
0 = 1, we get b2
1 + · · · + b2
n−1 = 1 in Z, so exactly one of b1, . . . , bn−1 is
±1 and the rest are 0: k(x) = xn + bixi −1 with 1 ≤i ≤n −1 and bi = ±1.
Let’s look at the terms of f ef and kek in degrees above n:
f ef = (xn −x −1)(−xn −xn−1 + 1) = −x2n −x2n−1 + xn+1 + · · ·
and
kek = (xn + bixi −1)(−xn + bixn−i + 1) = −x2n + bix2n−i −bixn+i + · · ·

<!-- page 3 -->
IRREDUCIBILITY OF xn −x −1
3
where · · · means terms of degree n or less. Thus
−x2n −x2n−1 + xn+1 + · · · = −x2n + bix2n−i −bixn+i + · · · .
The terms on the left have distinct degrees since 2n > 2n −1 > n + 1 (the last inequality
uses n > 2), so there are three terms on the left with degree greater than n. Therefore on
the right side 2n −i ̸= n + i (otherwise the right side would have only one term with degree
above n). If 2n−i > n+i then 2n−1 = 2n−i, so i = 1 and bi = −1, so k = xn −x−1 = f.
If n + i > 2n −i then 2n −1 = n + i, so i = n −1 and bi = 1, so k = xn + xn−1 −1 = −ef.
Recalling that k is not ±f or ± ef, we have reached a contradiction.
□
In the appendix we apply this method to more trinomials xn ± xm ± 1. For a further
application of this method, see https://mathoverflow.net/questions/404106.
Remark 2.1. Before Selmer’s work on xn −x −1, Perron [1] had proved irreducibility of
xn + ax ± 1 in Q[x] for all integers a such that |a| ≥3, and also for |a| = 2 provided 1 or
−1 are not roots (e.g., xn −2x + 1 has 1 as a root and x2m + 2x + 1 has −1 as a root).
Appendix A. More irreducible trinomials
The irreducibility argument we gave for xn −x−1 can be applied to nearly all trinomials
of the form xn ± xm ± 1, in the sense that it tells us exactly when they are irreducible.
Theorem A.1. For 1 < m < n with m ̸= n/2, and δ and ε equal to ±1, the polynomial
xn +δxm +ε is irreducible in Q[x] if and only if it has no root in common with its reciprocal
polynomial.
Proof. Let f(x) = xn + δxm + ε. Then ef(x) = εxn + δxn−m + 1 = ε(xn + εδxn−m + ε).
Since m ̸= n/2 the middle terms of f(x) and ef(x) have diﬀerent degrees, so f(x) and ef(x)
are not scalar multiples of each other. Therefore irreducibility of f(x) in Q[x] implies f(x)
and ef(x) have no common root.
Conversely, if f(x) and ef(x) have no common root then the proof of Theorem 1.1 goes
through with f(x) in place of xn −x −1. (As in that proof, the product f(x) ef(x) has three
terms of degree above n because m ̸= n/2.) Details are left to the reader.
□
Concretely, if m ̸= n/2 and δ, ε ∈{±1}, then xn + δxm + ε is irreducible except when it
has a root in common with xn + εδxn−m + ε.
Example A.2. Let’s apply Theorem A.1 to xn + x + 1.
Computer data suggest that
xn +x+1 is reducible if and only if n ≡2 mod 3 with n > 2, and that in this case x2 +x+1
is a factor of xn + x + 1. For example,
x5 + x + 1
=
(x2 + x + 1)(x3 −x2 + 1),
x8 + x + 1
=
(x2 + x + 1)(x6 −x5 + x3 −x2 + 1),
x11 + x + 1
=
(x2 + x + 1)(x9 −x8 + x6 −x5 + x3 −x2 + 1).
To prove x2 + x + 1 is a factor of xn + x + 1 if n ≡2 mod 3, work in Q[x]/(x2 + x + 1):
x2 ≡−x −1 and x3 ≡1, so x3j+2 + x + 1 ≡x2 + x + 1 ≡0.
Next we will prove that if xn + x + 1 is reducible in Q[x] then n ≡2 mod 3. By Theorem
A.1, reducibility implies xn + x + 1 and its reciprocal polynomial xn + xn−1 + 1 have a
common root, say α:
αn + α + 1 = 0 and αn + αn−1 + 1 = 0.

<!-- page 4 -->
4
KEITH CONRAD
Thus α = αn−1, so αn = α2, which makes both of the equations above α2 +α+1 = 0. That
implies α3 = 1, and deﬁnitely α ̸= 1, so from αn = α2 we must have n ≡2 mod 3.
Selmer [2] showed that when n ≡2 mod 3 and n > 2, so xn + x + 1 = (x2 + x + 1)gn(x),
the polynomial gn(x) is irreducible over Q.
The polynomials xn−x+1 and xn+x−1 have properties similar to Example A.2: in each
case there is a congruence condition on n mod 6 that gives the polynomial an automatic
low-degree factor, which is x2 −x + 1:
• xn −x + 1 is irreducible unless n ≡2 mod 6 with n > 2 (e.g., n = 8, 14, 20), when
x2 −x + 1 is a factor,
• xn + x −1 is irreducible unless n ≡5 mod 6 (e.g., n = 5, 11, 17), when x2 −x + 1 is
a factor.
For xn −x + 1 and xn + x −1, the congruence condition on n mod 6 above is equivalent to
the polynomial having a common root with its reciprocal polynomial, so by Theorem A.1
the congruence condition is equivalent to reducibility when n > 2.
Theorem A.1 avoids the case m = n/2. What happens in that case? Write n as 2m.
Corollary A.3. For all m ≥1 and δ = ±1, the polynomial x2m + δxm −1 is irreducible in
Q[x].
Proof. The proof of Theorem 1.1 still works when it is applied to both x2m + xm −1 and
x2m −xm −1 (here the degree n is 2m). Details are left to the reader.
□
All that remains is x2m+δxm+1, with constant term 1 and δ = ±1. Examples generated
by a computer suggest irreducibility is far less common than reducibility, as codiﬁed in the
following theorem.
Theorem A.4. For m ≥1, x2m + xm + 1 is irreducible over Q if and only if m is a power
of 3 and x2m −xm + 1 is irreducible over Q if and only if m = 2i3j for some nonnegative
integers i and j.
Proof. I learned the following argument from Dmitry Krachun.
There are two key points to keep in mind:
(1) x2 +x+1 is the minimal polynomial of primitive 3rd roots of unity and x2 −x+1 is
the minimal polynomial of primitive 6th roots of unity. In the notation of cyclotomic
polynomials, x2 + x + 1 = Φ3(x) and x2 −x + 1 = Φ6(x).
(2) If f(x) ∈Q[x] and f(xm) is irreducible then f(xd) is irreducible when d is a (pos-
itive) factor of m. Indeed, arguing with the contrapositive, if f(xd) = g(x)h(x) for
nonconstant g(x) and h(x) in Q[x], then f(xm) = g(xm/d)h(xm/d) and the polyno-
mials on the right side are nonconstant. We will use this when d = p is a prime
number: if f(xm) is irreducible over Q then so is f(xp) for prime factors p of m.
First we will show
x2m + xm + 1 is irreducible over Q =⇒m is a power of 3.
Set f(x) = x2 + x + 1, so x2m + xm + 1 = f(xm). If f(xm) is irreducible over Q then we
will show m is a power of 3 by showing for each prime p ̸= 3 that f(xp) is reducible, so the
only possible prime factor of m is 3. (See the second key point above.)
Let α be a root of x2 +x+1. The other root of x2 +x+1 is α−1 and α3 = 1, so powers αk
only depend on k modulo 3. For each prime p ̸= 3, p ≡±1 mod 3, so αp = α±1. Therefore

<!-- page 5 -->
IRREDUCIBILITY OF xn −x −1
5
f(αp) = f(α±1) = 0, so f(xp) is divisible by the minimal polynomial of α over Q, which is
x2 + x + 1. That makes f(xp) reducible since its degree 2p is greater than 2.
Next we will show
x2m −xm + 1 is irreducible over Q =⇒m = 2i3j for some i, j ≥0.
Now set f(x) = x2 −x + 1, so to prove f(xm) = x2m −xm + 1 can be irreducible only
when the prime factors of m are 2 or 3, it suﬃces by the reasoning used above to show
f(xp) is reducible for each prime p > 3.
Let β be a root of x2 −x + 1, so the other root is β−1 and β6 = 1, so βk only depends
on k modulo 6. For prime p > 3, p ≡±1 mod 6, so f(βp) = f(β±1) = 0. Thus f(xp) is
divisible by x2 + x + 1, which makes f(xp) reducible since its degree is greater than 2.
It remains to show that
m is a power of 3 =⇒Φ3(xm) = x2m + xm + 1 is irreducible over Q
and
m = 2i3j =⇒Φ6(xm) = x2m −xm + 1 is irreducible over Q.
These are both special cases (n = 3 and n = 6) of the following property of all cyclotomic
polynomials Φn(x): if m is a positive integer whose prime factors all divide n, then Φn(xm) =
Φmn(x). This polynomial identity is a consequence of both sides being monic of the same
degree (mϕ(n) = ϕ(mn) when all prime factors of m divide n), the right side being the
minimal polynomial over Q of all roots of unity of order mn, and the left side vanishing at
all roots of unity of order mn.1
□
References
[1] O. Perron, Neue Kriterien f¨ur die Irreduzibilit¨at algebraischer Gleichungen, J. reine angew. Math. 132
(1907), 288–307. URL https://eudml.org/doc/149269.
[2] E. Selmer, On the Irreducibility of Certain Trinomials, Math. Scand. 4 (1956), 287–302. URL https:
//eudml.org/doc/165635.
1In fact, for all positive integers m and n, Φn(xm) is irreducible over Q if and only if each prime factor
of m is a factor of n. This becomes Theorem A.4 when n is 3 and 6.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*