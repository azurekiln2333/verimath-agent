# Polynomial Properties

> **Source**: https://kconrad.math.uconn.edu/blurbs/polynomial-properties.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
NILPOTENTS, UNITS, AND ZERO DIVISORS FOR POLYNOMIALS
KEITH CONRAD
1. Introduction
Let A be a nonzero commutative ring.
We want to describe the following kinds of
polynomials in A[x], and more generally in A[x1, . . . , xd] for d ≥1:
• nilpotents,
• units,
• zero divisors.
These are easy to describe when A is an integral domain, since A[x1, . . . , xd] is an integral
domain too. The only nilpotent element is 0. The units are the units in A since deg(fg) =
deg f + deg g when f, g ̸= 0, so fg = 1 ⇒deg f, deg g = 0 ⇒f ∈A×, and the converse
is obvious. The only zero divisor is 0. To extend these results to polynomial rings whose
coeﬃcients are in an arbitrary nonzero commutative ring,1 we will focus ﬁrst on the case
d = 1. Most of the essential ideas for general d already appear when looking at d = 1,
although proving the theorem about zero divisors in A[x1, . . . , xd] when d > 1 will involve
some new concepts.
2. Properties of polynomials in one indeterminate
Theorem 2.1. A polynomial in A[x] is nilpotent if and only if all of its coeﬃcients are
nilpotent in A.
Proof. The nilpotent elements in a commutative ring form an ideal, by the binomial theorem,
and nilpotent elements of A are nilpotent in A[x]. Therefore if a polynomial in A[x] has
coeﬃcients that are nilpotent in A, then the polynomial is nilpotent in A[x].
Conversely, suppose f(x) in A[x] is nilpotent. To show all the coeﬃcients of f(x) are
nilpotent in A, we may focus on nonzero f(x) and induct on deg f. The case deg f = 0 is
easy. Suppose n ≥1 and the result is true for all polynomials of degree less than n. For a
nilpotent polynomial f(x) = a0 + a1x + · · · + anxn of degree n, say
f(x)k = 0
for some k ≥1. Looking at the coeﬃcient of xnk on both sides tells us ak
n = 0. Therefore
an is nilpotent in A. Since the nilpotent elements in A[x] form an ideal,
f(x) −anxn = a0 + a1x + · · · + an−1xn−1
is nilpotent in A[x] and is either 0 or has degree less than n. Either way, by induction all
ai for i ≤n −1 are nilpotent, so all the coeﬃcients of f(x) are nilpotent.
□
Theorem 2.2. A polynomial in A[x] is a unit if and only if its constant term is a unit in
A and its higher-degree coeﬃcients are all nilpotent.
1The running hypothesis that A ̸= {0} will not be regularly repeated.
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. In a commutative ring, if u is a unit and b is nilpotent, the sum u + b is a unit:
u + b = u(1 + b/u), and if bk = 0 then an elementary calculation shows 1 + b/u is a unit
with inverse being the ﬁnite geometric series
1 −b/u + (−b/u)2 + (−b/u)3 + · · · + (−b/u)k−1.
Intuitively, we are expanding 1/(1 −r) for r = −b/u into a geometric series P
i≥0 ri and
truncating it before the term where i = k since (−b/u)i = 0 for i ≥k. Thus u+b = u(1+b/u)
is a product of two units and therefore is a unit.
By that general argument, if f(x) in A[x] has constant term in A× and its higher-degree
coeﬃcients are all nilpotent, f(x) is a unit plus a nilpotent in A[x] by the previous theorem,
and therefore f(x) ∈A[x]×.
For the converse result, suppose f(x) = a0 + a1x + · · · + anxn is a unit in A[x], say
f(x)g(x) = 1 for some g(x) ∈A[x]. Looking at the constant terms on both sides shows
a0 ∈A×. Why are the higher-degree coeﬃcients of f(x) nilpotent? This uses a consequence
of Zorn’s lemma: in a nonzero commutative ring, the intersection of all the prime ideals
is the set of nilpotent elements in the ring.2 With this in mind, let p be a prime ideal in
A. The equation f(x)g(x) = 1 in A[x] implies after reducing coeﬃcients modulo p that
f(x)g(x) = 1 in (A/p)[x]. Since A/p is an integral domain, a unit in (A/p)[x] has degree 0
(see the introduction), so deg(f(x)) = 0. Thus all higher-degree coeﬃcients of f(x) belong
to p. Letting p run over all the prime ideals of A, each higher-degree coeﬃcient of f(x) is in
every prime ideal of A and therefore the higher-degree coeﬃcients of f(x) are nilpotent.
□
Example 2.3. In (Z/6Z)[x], the units are 1 and 5 (units in Z/6Z): the only nilpotent
element of Z/6Z is 0, so the higher-degree coeﬃcients of a unit in (Z/6Z)[x] must be 0.
Example 2.4. In (Z/45Z)[x], 8 + 15x is a unit (it equals 8(1 + 30x), which has inverse
17(1 −30x) = 17 + 30x), while 8 + 3x is not a unit: 3 is not nilpotent in Z/45Z.
The following theorem on zero divisors in polynomial rings is due to McCoy [1]. The result
is striking: for a polynomial to be a zero divisor means it is annihilated after multiplication
by a nonzero polynomial, but in fact it can be annihilated by a nonzero constant.
Theorem 2.5 (McCoy). A polynomial f(x) ∈A[x] is a zero divisor if and only if there is
some nonzero a ∈A such that af(x) = 0.
Proof. Obviously if af(x) = 0 for some nonzero a ∈A, then f(x) is a zero divisor.
To prove the more interesting converse direction, we follow Scott [3]. For a zero divisor
f(x) ∈A[x], g(x)f(x) = 0 for a nonzero g(x). Let g(x) have minimal degree such that
g(x)f(x) = 0. Assume deg(g(x)) > 0, so at least f(x) ̸= 0. We will get a contradiction, so
deg(g(x)) = 0: af(x) = 0 for some nonzero a ∈A.
Let
f(x) = a0 + a1x + · · · + anxn,
g(x) = b0 + b1x + · · · + bmxm
where an ̸= 0 and bm ̸= 0 with m ≥1. We have bmf(x) ̸= 0 by the minimality of deg(g(x)),
so bmai ̸= 0 for some i. Thus g(x)ai ̸= 0 for that i. Let j be maximal with g(x)aj ̸= 0, so
0 = g(x)f(x) = (b0 + b1x + · · · + bmxm)(a0 + a1x + · · · + ajxj),
2For a proof, see Theorem 3.3 in https://kconrad.math.uconn.edu/blurbs/zorn1.pdf.

<!-- page 3 -->
NILPOTENTS, UNITS, AND ZERO DIVISORS FOR POLYNOMIALS
3
where we drop the terms aixi from f(x) where i > j since g(x)ai = 0 for i > j. Looking at
the coeﬃcient of xm+j, bmaj = 0, so deg(g(x)aj) < deg(g(x)). (We have g(x)aj ̸= 0 by the
maximality of j, so deg(g(x)aj) makes sense.)
Since (g(x)aj)f(x) = aj(g(x)f(x)) = aj · 0 = 03 and deg(g(x)aj) < deg(g(x)), we have
contradicted minimality of deg(g(x)) among nonzero polynomials that annihilate f(x) by
multiplication. The assumption that deg(g(x)) > 0 is incorrect, so deg(g(x)) = 0.
□
Example 2.6. In (Z/6Z)[x], 2 + 3x is a not a zero divisor even though its coeﬃcients 2
and 3 are zero divisors since a(2 + 3x) ̸= 0 for nonzero a ∈Z/6Z by a direct calculation.
Corollary 2.7. For a polynomial f(x) = a0 + a1x + · · · + anxn in Z[x] and m ≥2,
f(x) mod m is a zero divisor in (Z/mZ)[x] if and only if gcd(a0, . . . , an, m) > 1.
Proof. If f(x) is a zero divisor, then by Theorem 2.5, af(x) ≡0 mod m where a ̸≡0 mod m.
Then aai ≡0 mod m for all i. Let d = (a, m), a = da′, and m = dm′. We have d ̸= m since
a ̸≡0 mod m, so m′ > 1. Dividing through the congruence aai ≡0 mod m (including the
modulus) by d, a′ai ≡0 mod m′, so m′ | a′ai. Since (a′, m′) = 1, m′ | ai for all i. Therefore
m′ is a common divisor of each coeﬃcient ai and of course m′ | m, so gcd(a0, . . . , an, m) ≥
m′ > 1.
Set c = gcd(a0, . . . , an, m) and suppose c > 1. If c = m then all the coeﬃcients of f(x)
are divisible by m, so f(x) mod m is 0 in (Z/mZ)[x] and therefore f(x) mod m is a zero
divisor. Now take 1 < c < m. All coeﬃcients of f(x) are divisible by c, so all coeﬃcients
of (m/c)f(x) are divisible by m and 1 < m/c < m.
Thus (m/c)f(x) ≡0 mod m and
m/c ̸≡0 mod m, so f(x) mod m is a zero divisor in (Z/mZ)[x].
□
Example 2.8. A zero divisor in (Z/6Z)[x] must have all coeﬃcients divisible by 2 or all
coeﬃcients divisible by 3.
3. Properties of polynomials in d indeterminates
Theorem 3.1. A polynomial in A[x1, . . . , xd] is nilpotent if and only if all of its coeﬃcients
are nilpotent in A.
Proof. As in the case d = 1, a polynomial in A[x1, . . . , xd] whose coeﬃcients are all nilpotent
in A is nilpotent in A[x1, . . . , xd] since nilpotent elements form an ideal.
To prove the converse, that a nilpotent polynomial has nilpotent coeﬃcients in A, we
induct on d. The case d = 1 is Theorem 2.1. Suppose d ≥2 and the converse is proved for
polynomials in d −1 indeterminates with coeﬃcients in an arbitrary nonzero commutative
ring. Let f ∈A[x1, . . . , xd] be nilpotent. Writing A[x1, . . . , xd] as A[x1, . . . , xd−1][xd], we
have f = Pn
i=0 cixi
d where ci ∈A[x1, . . . , xd−1] for i = 0, . . . , n. By the base case, each ci
is nilpotent in A[x1, . . . , xd−1], so by induction the A-coeﬃcients of each ci are nilpotent.
The A-coeﬃcients of all ci, as i runs from 0 to n, are the A-coeﬃcients of f, so all the
A-coeﬃcients of f are nilpotent.
□
Theorem 3.2. A polynomial in A[x1, . . . , xd] is a unit if and only if its constant term is a
unit in A and its higher-degree coeﬃcients are all nilpotent.
Proof. The proof of the“if” direction is identical to the case d = 1 in Theorem 2.2.
The “only if” direction is also proved in the same way as the “only if” direction of
Theorem 2.2, since (A/p)[x1, . . . , xd] is an integral domain for each prime ideal p of A.
□
3Here we use commutativity of multiplication in A. The theorem isn’t true for some noncommutative A.

<!-- page 4 -->
4
KEITH CONRAD
To prove an analogue of Theorem 2.5 (about zero divisors) for multivariable polynomials,
let’s ﬁrst try the case of two indeterminantes. Suppose f(x, y) is a zero divisor in A[x, y].
Viewing A[x, y] as A[y][x], write f(x, y) = Pn
i=0 ci(y)xi where ci(y) ∈A[y]. By Theorem
2.5 for the ring (A[y])[x], there is some nonzero c(y) ∈A[y] such that c(y)f(x, y) = 0, so
c(y)ci(y) = 0 for all ci(y) by looking at the coeﬃcient of each power of x in c(y)f(x, y).
Therefore each ci(y) is a zero divisor in A[y], so by Theorem 2.5 for the ring A[y], aici(y) = 0
for some ai ∈A where i = 0, . . . , n. Unfortunately, it is not clear that a0, . . . , an can be
chosen as the same element of A, and without that we don’t get af(x, y) = 0 for a nonzero
a ∈A. Nevertheless, that desired result is in fact true, not just in A[x, y] but in A[x1, . . . , xd]:
a zero divisor in A[x1, . . . , xd] is annihilated by a nonzero element of A. We will prove this
in two ways. The ﬁrst proof, due to McCoy [2], involves proving a stronger theorem about
ideals rather than polynomials. The second proof will use a total ordering on multivariable
monomials that will allow us to generalize the proof of Theorem 2.5 to the multivariable
setting rather easily, in contrast to the incomplete attempt at that in A[x, y] above.
Theorem 3.3 (McCoy). Let I be an ideal in A[x1, . . . , xd] such that gI = (0) for some
nonzero g ∈A[x1, . . . , xd]. Then aI = (0) for some nonzero a ∈A.
Proof. We will prove this using induction on d.
Base case d = 1. Our argument will be very similar to the proof of Theorem 2.5, with a
few diﬀerences because ideals in A[x] need not be principal.
Let I be an ideal in A[x] where g(x)I = (0) for a nonzero g(x) ∈A[x]. Let g(x) have
minimal degree subject to the condition g(x)I = (0). Assume deg(g(x)) > 0, so aI ̸= (0)
for all nonzero a ∈A. We will get a contradiction, so deg(g(x)) = 0: aI = (0) for some
nonzero a ∈A.
Write g(x) = b0 +b1x+· · ·+bmxm with m ≥1 and bm ̸= 0. Since bmI ̸= (0), bmf(x) ̸= 0
for some f(x) ∈I, so f(x) ̸= 0. Write f(x) = a0 + a1x + · · · + anxn. Since bmf(x) ̸= 0,
bmai ̸= 0 for some i, so g(x)ai ̸= 0 for some i. Let j be maximal with g(x)aj ̸= 0. Since
f(x) ∈I and g(x)I = (0), the product g(x)f(x) is 0:
0 = g(x)f(x) = (b0 + b1x + · · · + bmxm)(a0 + a1x + · · · + ajxj),
where we drop the terms aixi from f(x) where i > j since g(x)ai = 0 for i > j. Looking at
the coeﬃcient of xm+j, bmaj = 0, so deg(g(x)aj) < deg(g(x)). (We have g(x)aj ̸= 0 by the
maximality of j, so deg(g(x)aj) makes sense.)
For all F(x) in I (not just the f(x) above!), g(x)F(x) = 0 by the deﬁnition of g(x), so
(g(x)aj)F(x) = aj(g(x)F(x)) = aj · 0 = 0. Therefore (g(x)aj)I = (0) and deg(g(x)aj) <
deg(g(x)), which contradicts minimality of deg(g(x)) among nonzero polynomials that an-
nihilate I by multiplication. The assumption that the minimal value of deg(g(x)) is positive
is incorrect, so that minimal value is 0: there is a nonzero a ∈A such that aI = (0).
Inductive step. For d ≥2, assume the theorem is proved for polynomials in d −1 inde-
terminates over an arbitrary nonzero commutative ring. Let I be an ideal in A[x1, . . . , xd]
such that gI = (0) for some nonzero g ∈A[x1, . . . , xd] and give g the minimal possible de-
gree. We want to show that minimal degree is 0, so we’ll assume instead that the minimal
degree is positive and get a contradiction. View A[x1, . . . , xd] as (A[x1, . . . , xd−1])[xd], the
ring of polynomials in xd with coeﬃcients in A[x1, . . . , xd−1]. That makes I an ideal in
R[xd] where R = A[x1, . . . , xd−1]. By the base case of single-variable polynomials (with an
arbitrary coeﬃcient ring), from gI = (0) we get c(x1, . . . , xd−1)I = (0) for some nonzero
polynomial c(x1, . . . , xd−1) in R.

<!-- page 5 -->
NILPOTENTS, UNITS, AND ZERO DIVISORS FOR POLYNOMIALS
5
For each f ∈I, write
(3.1)
f =
n
X
i=0
cixi
d
where ci ∈R, and abbreviate c(x1, . . . , xd−1) to c, so c, c0, . . . , cn are all in R: they don’t
involve xd. From cI = (0) we get cf = 0, so cci = 0 by looking at the coeﬃcients of diﬀerent
powers of xd in cf. This means c multiplied by each coeﬃcient in R of each polynomial
in I is 0. Let J be the ideal in R generated by the coeﬃcients in R of the polynomials
in I (written as polynomials in xd). Then cJ = (0), where c ∈R and J is an ideal in R.
Since R = A[x1, . . . , xd−1], by the inductive hypothesis aJ = 0 for some nonzero a ∈A.
Returning to arbitrary f in I written as in (3.1), the condition aJ = (0) implies aci = 0
since all ci’s are in J, so af = Pn
i=0 acixi
d = 0. This holds for all f in I, so aI = (0).
□
Corollary 3.4. If f is a zero divisor in A[x1, . . . , xd] then af = 0 for some nonzero a ∈A.
Proof. We are assuming gf = 0 for some nonzero g ∈A[x1, . . . , xd] and can apply Theorem
3.3 to the principal ideal I = (f): from gI = (gf) = (0), we get aI = (0) for some nonzero
a ∈A, so af = 0.
□
Our second proof of Corollary 3.4 will not use induction on d, and instead will use an
ordering on the monomials in A[x1, . . . , xd] that gives them a total ordering: two diﬀerent
monomials are always comparable (one being greater than the other). This will give us an
unambiguous notion of leading term and degree (valued in Nd rather than N) that will
allow the proof of Theorem 2.5 to be carried over rather easily to the multivariable setting.
Deﬁnition 3.5. For distinct d-tuples i = (i1, . . . , id) and j = (j1, . . . , jd) in Nd, set i > j
if, for the ﬁrst r such that ir ̸= jr, we have ir > jr. Write i ≥j if i > j or i = j.
Example 3.6. In N4, (5, 1, 1, 3) > (3, 0, 2, 4) and (3, 0, 3, 1) > (3, 0, 2, 4).
Example 3.7. In Nd, 0 < i for all i ̸= 0.
For all d-tuples i and j in Nd, either i = j, i > j, or j > i, so Nd is totally ordered by >.
(For example, i > 0 for all i ̸= 0.) This way of ordering of d-tuples is called lexicographic
(i.e., dictionary) ordering since it resembles the way words are ordered in the dictionary
alphabetically if we think of one word as “greater” than another if it comes later in the
dictionary. Alphabetical order compares words by the ﬁrst letter, if that letter is the same
the words are compared by the second letter, and so on. While words in a dictionary have
varying length, we are using lexicographic ordering only to compare sequences in N with
the same number of terms.
Lemma 3.8. Lexicographic ordering on Nd has the following properties.
(1) (Total ordering) For all i and j, exactly one of i = j or i < j or j < i holds.
(2) (Transitivity) If i < j and j < k then i < k. The same is true with ≤in place of <.
(3) (Compatibility with addition) If i ≤i′ and j ≤j′ then i + j ≤i′ + j′, and if either
inequality in the hypothesis is strict then the inequality in the conclusion is strict.
Proof. (1) If i ̸= j, then there is an r where ir ̸= jr in N. Let r be the least index where
this happens. If ir < jr then i < j, and if jr < ir then j < i.
(2) Let r be the least index where ir, jr, and kr are not all equal. We must have ir ̸= jr or
jr ̸= kr (if both were equalities then ir = jr = kr, which isn’t true). Since earlier coordinates
in i, j, and k are all equal, either ir < jr or jr < kr because i < j and j < k. Therefore

<!-- page 6 -->
6
KEITH CONRAD
ir ≤jr ≤kr with at least one inequality being strict, so ir < kr and earlier coordinates in i
and k are equal. Thus i < k.
This result for ≤is the same argument as with < except we have the extra cases where
i and j may coincide or j and k may coincide, which makes things easier.
(3) Rather than take cases based on where i and i′ may ﬁrst diﬀer or where j and j′ may
ﬁrst diﬀer, observe that i ≤i′ ⇒i + k ≤i′ + k for all k: this is obvious when i = i′, and
when i < i′ the only way ir + kr diﬀers from i′
r + kr is if ir ̸= i′
r, and the ﬁrst time this
happens we have ir < i′
r, so ir + kr < i′
r + kr.
Now we use that twice together with the transitivity in (2). If i ≤i′ and j ≤j′, then
i + j ≤i′ + j = j + i′ ≤j′ + i′ = i′ + j′ =⇒i + j ≤i′ + j′.
The case of < in place of ≤is analogous.
□
In N with its usual ordering, there are ﬁnitely many elements below a given element, but
this is not true in Nd for d ≥2 with lexicographic ordering: there can be inﬁnitely many
d-tuples below some d-tuple. For instance, (0, b) < (1, 0) for all b ∈N. But Nd does share
with N the following important ordering property.
Lemma 3.9. When Nd has lexicographic ordering, each nonempty subset of Nd has a least
element.
The least element in the subset has to be unique since lexicographic ordering is a total
ordering on Nd.
Proof. Let S be a nonempty subset of Nd. The idea behind getting a least element of S
is as follows. The ﬁrst coordinates of d-tuples in S are a nonempty subset of N and thus
have a least element ℓ1. If d = 1 then ℓ1 is the least element of S. For d ≥2, among the
elements of S with ﬁrst coordinate ℓ1, their second coordinates are a nonempty subset of
N and thus have a least element ℓ2. If d = 2 then (ℓ1, ℓ2) is the least element of S. For
d ≥3, among the elements of S with ﬁrst coordinate ℓ1 and second coordinate ℓ2, their
third coordinates are a nonempty subset of N and thus have a least element ℓ3. Continue
this way up through the dth coordinate. The d-tuple (ℓ1, ℓ2, . . . , ℓd) in S is the least element
of S by the deﬁnition of lexicographic ordering on Nd.
It is left to the reader to rewrite this argument as a proper proof by induction on d.
□
A polynomial f ∈A[x1, . . . , xd] is a sum of the form
f =
X
i1,...,id≥0
ai1,...,idxi1
1 · · · xid
d
where ai1,...,id ∈A and only ﬁnitely many coeﬃcients can be nonzero. Abbreviate this sum
to multi-index form as P
i aixi, where xi := xi1
1 · · · xid
d for i = (i1, . . . , id). Note xixj = xi+j.
(In the notation P
i, only ﬁnitely many terms are nonzero.) When f ̸= 0, lexicographic
ordering lets us compare the diﬀerent nonzero monomials appearing in f, which leads to
the following concepts that generalize degree and leading terms on A[x].
Deﬁnition 3.10. Write f in A[x1, . . . , xd] as P
i aixi. If f ̸= 0, the multidegree of f is the
lexicographically largest index in Nd of a nonzero monomial in f:
mdeg f = max{i : ai ̸= 0} ∈Nd.
The multidegree of the zero polynomial is not deﬁned. If f ̸= 0 and mdeg f = n, we call
anxn the leading term of f and an the leading coeﬃcient of f.

<!-- page 7 -->
NILPOTENTS, UNITS, AND ZERO DIVISORS FOR POLYNOMIALS
7
We can separate the leading term of a nonzero f of multidegree n from its other nonzero
terms to get
f = anxn +
X
i<n
aixi.
Because multidegrees are totally ordered, a nonzero polynomial in A[x1, . . . , xd] has a unique
leading term and a unique leading coeﬃcient in A.
Example 3.11. In Z[x1, x2], let f = 7x1x5
2+3x8
2+9. Since max((1, 5), (0, 8), (0, 0)) = (1, 5)
in N2, mdeg(f) = (1, 5) and lead(7x1x5
2 + 3x8
2 + 9) = 7.
Example 3.12. In A[x1, . . . , xd], mdeg(x1) = (1, 0, . . . , 0) and mdeg(xd) = (0, 0, . . . , 1).
Example 3.13. The polynomials with multidegree 0 are the nonzero constants.
Our deﬁnition of multidegree is speciﬁc to calling x1 the “ﬁrst” indeterminate, x2 the
“second” indeterminate, and so on up to xd being the “last” one. There is nothing intrinsic
about declaring x1 the “ﬁrst” indeterminate: there are d! diﬀerent lexicographic orderings
based on which coordinate in Nd we want to consider ﬁrst, second, and so on. Having
made a choice, the corresponding multidegree function permits us to prove theorems about
multivariable polynomials by ordering them according to their multidegree in the same way
theorems about single-variable polynomials are proved by ordering them by degree.
Remark 3.14. A simpler way to order nonzero multivariable polynomials f is by their “to-
tal degree”, which is the largest sum of exponents among the nonzero monomials appearing
in f, e.g., x1x5
2 + x8
2 has total degree 8. This degree function on nonzero polynomials in
A[x1, . . . , xd] has values in N rather than Nd. It is useful for some purposes, but not for
what we want to do because it does not provide a unique leading term for nonzero polyno-
mials A[x1, . . . , xd] when d > 1 since diﬀerent monomials in d indeterminates can have the
same total degree. For instance, x1x5
2, x3
1x3
2, and x6
2 all have total degree 6. By contrast, in
the lexicographic ordering x3
1x3
2 > x1x5
2 > x6
2.
Now we’ll prove Corollary 3.4 a second way. Compare it to the proof of Theorem 2.5.
Theorem 3.15. If f is a zero divisor in A[x1, . . . , xd] then af = 0 for some nonzero a ∈A.
Proof. For a zero divisor f ∈A[x1, . . . , xd], gf = 0 for some nonzero g. We can pick such
g with minimal multidegree in Nd: the set {g ∈A[x1, . . . , xn] : gf = 0 and g ̸= 0} is
nonempty and the multidegrees of polynomials in this set are a nonempty subset of Nd, so
there is a least multidegree for polynomials in that set by Lemma 3.9.
When mdeg(g) is least, assume mdeg(g) ̸= 0. Then mdeg(g) > 0 and f ̸= 0. We will
show egf = 0 where eg ̸= 0 and mdeg(eg) < mdeg(g). That contradicts mdeg(g) being least,
so mdeg(g) = 0, which means af = 0 for some nonzero a ∈A.
Set n = mdeg(f) and m = mdeg(g) in Nd, so
f =
X
i
aixi = anxn + lower multidegree terms,
g = bmxm + lower multidegree terms,
where an ̸= 0 and bm ̸= 0 in A. Since af ̸= 0 for all nonzero a in A, bmf ̸= 0. Therefore
bmai ̸= 0 for some i, so gai ̸= 0 for that i. Let j be maximal in Nd with gaj ̸= 0, so gai = 0
for i > j.
It is crucial that we are using a total ordering on monomials, both to have
unique leading terms for f and g and to have a unique maximal j such that ajg ̸= 0. (If we

<!-- page 8 -->
8
KEITH CONRAD
ordered multivariable polynomials by total degree instead of multidegree, there would not
be a unique leading term for nonzero polynomials when d ≥2.)
Since gf = 0,
0 = gf = (bmxm + lower multidegree terms)

ajxj + lower multidegree terms

,
where we dropped the terms aixi from f in the product when i > j since gai = 0 for i > j.
By Lemma 3.8, the only xm+j-term on the right is (bmxm)(ajxj) = bmajxm+j, so bmaj = 0.
Since bmxm is the leading term of g and bmaj = 0, mdeg(gaj) < m = mdeg(g), where
gaj ̸= 0 by maximality of j, so mdeg(gaj) makes sense.
Since (gaj)f = ajgf = aj · 0 = 0 and mdeg(gaj) < mdeg(g), we have contradicted the
minimality of mdeg(g) among nonzero polynomials g in A[x1, . . . , xd] such that gf = 0 if
we assume mdeg(g) > 0. Therefore mdeg(g) = 0, so if f is a zero divisor in A[x1, . . . , xd]
then af = 0 for some nonzero a in A.
□
Corollary 3.16. For f = P
i aixi in Z[x1, . . . , xd] and m ≥2, f mod m is a zero divisor
in (Z/mZ)[x1, . . . , xd] if and only if gcd({ai}, m) > 1.
Proof. The case d = 1 is proved in Corollary 2.7 and that proof works with no changes for
all d.
□
Corollary 3.17. For f = P
i aixi in Z[x1, . . . , xd], gcd({ai}) = 1 if and only if f mod m
is not a zero divisor in (Z/mZ)[x1, . . . , xd] for all m ≥2.
Proof. If gcd({ai}) = 1, then for m ≥2 we have gcd({ai}, m) = 1, so f mod m is not a zero
divisor in (Z/mZ)[x1, . . . , xd] by Corollary 3.16.
If gcd({ai}) > 1, set b = gcd({ai}). For all m such that gcd(b, m) > 1 (such as m being
a multiple of b), gcd({ai}, m) = gcd(b, m) > 1 and therefore f mod m is a zero divisor in
(Z/mZ)[x1, . . . , xd] by Corollary 3.16.
□
References
[1] N. H. McCoy, “Remarks on divisors of zero,” Amer. Math. Monthly 49 (1942), 286–295. Online at
https://www.jstor.org/stable/pdf/2303094.
[2] N. H. McCoy, “Annihilators in polynomial rings,” Amer. Math. Monthly 64 (1957), 28–29. Online at
https://www.jstor.org/stable/2309082.
[3] W. R. Scott, “Divisors of zero in polynomial rings,” Amer. Math. Monthly 61 (1954), 336. Online at
https://www.jstor.org/stable/pdf/2307474.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*