# Roots and Irreducible Polynomials

> **Source**: https://kconrad.math.uconn.edu/blurbs/rootirred.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
ROOTS AND IRREDUCIBLES
KEITH CONRAD
1. Introduction
This handout discusses relationships between roots of irreducible polynomials and ﬁeld
extensions. Throughout, the letters K, L, and F are ﬁelds and Fp = Z/(p) is the ﬁeld of
p elements. When f(X) ∈K[X], we will say f(X) is a polynomial “over” K. Sections 2
and 3 describe some general features of roots of polynomials. In the later sections we look
at roots of polynomials in Fp[X].
2. Roots in larger fields
For most ﬁelds K, there are polynomials in K[X] without a root in K. Consider X2 + 1
in R[X] or X3 −2 in F7[X]. If we are willing to enlarge the ﬁeld, then we can discover
some roots. This is due to Kronecker, by the following argument.
Theorem 2.1. Let K be a ﬁeld and f(X) be nonconstant in K[X]. There is a ﬁeld extension
of K containing a root of f(X).
Proof. It suﬃces to prove the theorem when f(X) = π(X) is irreducible (why?).
Set F = K[t]/(π(t)), where t is an indeterminate. Since π(t) is irreducible in K[t], F is a
ﬁeld. Inside of F we have K as a subﬁeld: the congruence classes represented by constants.
There is also a root of π(X) in F, namely the class of t. Indeed, writing t for the congruence
class of t in F, the congruence π(t) ≡0 mod π(t) becomes the equation π(t) = 0 in F.
□
Example 2.2. Consider X2 + 1 ∈R[X], which has no root in R. The ring R[t]/(t2 + 1) is
a ﬁeld containing R. In this ﬁeld t2 = −1, so the polynomial X2 + 1 has the root t in the
ﬁeld R[t]/(t2 + 1). The reader should recognize R[t]/(t2 + 1) as an algebraic version of the
complex numbers: congruence classes are represented by a + bt with t2 = −1.
When an irreducible polynomial over a ﬁeld K picks up one root in a larger ﬁeld, there
need not be more roots in that ﬁeld. This is an important point to keep in mind. A simple
example is X3 −2 in Q[X], which has only one root in R, namely
3√
2. There are two more
roots in C, but they do not live in R. (Incidentally, the ﬁeld extension of Q constructed by
Theorem 2.1 which contains a root of X3 −2, namely Q[t]/(t3 −2), is much smaller than
the real numbers, e.g., it is countable.)
By repeating the construction in the proof of Theorem 2.1 several times, we can always
create a ﬁeld with a full set of roots for our polynomial. We state this as a corollary, and
give a proof by induction on the degree.
Corollary 2.3. Let K be a ﬁeld and f(X) = cmXm + · · · + c0 be in K[X] with degree
m ≥1. There is a ﬁeld L ⊃K such that in L[X],
(2.1)
f(X) = cm(X −α1) · · · (X −αm).
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. We induct on the degree m. The case m = 1 is clear, using L = K. By Theorem
2.1, there is a ﬁeld F ⊃K such that f(X) has a root in F, say α1. Then in F[X],
f(X) = (X −α1)g(X),
where deg g(X) = m −1. The leading coeﬃcient of g(X) is also cm.
Since g(X) has smaller degree than f(X), by induction on the degree there is a ﬁeld
L ⊃F (so L ⊃K) such that g(X) decomposes into linear factors in L[X], so we get the
desired factorization of f(X) in L[X].
□
Corollary 2.4. Let f(X) and g(X) be nonconstant in K[X]. They are relatively prime in
K[X] if and only if they do not have a common root in an extension ﬁeld of K.
Proof. Assume f(X) and g(X) are relatively prime in K[X]. Then we can write
f(X)u(X) + g(X)v(X) = 1
for some u(X) and v(X) in K[X]. If there were an α in an ﬁeld extension of K which is a
common root of f(X) and g(X), then substituting α for X in the above polynomial identity
makes the left side 0 while the right side is 1. This is a contradiction, so f(X) and g(X)
have no common root in a ﬁeld extension of K.
Now assume f(X) and g(X) are not relatively prime in K[X]. Say h(X) ∈K[X] is a
(nonconstant) common factor. There is a ﬁeld extension of K in which h(X) has a root,
and this root will be a common root of f(X) and g(X).
□
Although adjoining one root of an irreducible in Q[X] to the rational numbers does not
always produce the other roots in the same ﬁeld (such as with X3 −2), the situation in
Fp[X] is much simpler. We will see later (Theorem 5.4) that for an irreducible in Fp[X], a
larger ﬁeld which contains one root must contain all the roots. Here are two examples.
Example 2.5. The polynomial X3 −2 is irreducible in F7[X].
It has a root in F =
F7[t]/(t3 −2), namely t. It also has two other roots in F, 2t and 4t.
Example 2.6. The polynomial X3 + X2 + 1 is irreducible in F5[X]. In the ﬁeld F =
F5[t]/(t3 + t2 + 1), the polynomial has the root t and also the roots 2t2 + 3t and 3t2 + t + 4.
3. Divisibility and roots in K[X]
There is an important connection between roots of a polynomial and divisibility by linear
polynomials. For f(X) ∈K[X] and α ∈K, f(α) = 0 ⇐⇒(X −α) | f(X). The next result
is an analogue for divisibility by higher degree polynomials in K[X], provided they are
irreducible. (All linear polynomials are irreducible.)
Theorem 3.1. Let π(X) be irreducible in K[X] and let α be a root of π(X) in some larger
ﬁeld. For h(X) in K[X], h(α) = 0 ⇐⇒π(X) | h(X) in K[X].
Proof. If h(X) = π(X)g(X), then h(α) = π(α)g(α) = 0.
Now assume h(α) = 0. Then h(X) and π(X) have a common root, so by Corollary 2.4
they have a common factor in K[X]. Since π(X) is irreducible, this means π(X) | h(X)
in K[X]. To see this argument more directly, suppose h(α) = 0 and π(X) does not divide
h(X). Then (because π is irreducible) the polynomials π(X) and h(X) are relatively prime
in K[X] so we can write
π(X)u(X) + h(X)v(X) = 1
for some u(X), v(X) ∈K[X]. Substitute α for X and the left side vanishes. The right side
is 1 so we have a contradiction.
□

<!-- page 3 -->
ROOTS AND IRREDUCIBLES
3
Example 3.2. Take K = Q and π(X) = X2 −2. It has a root
√
2 ∈R. For h(X) ∈Q[X],
h(
√
2) = 0 ⇐⇒(X2 −2) | h(X). This equivalence breaks down if we allow h(X) to come
from R[X]: try h(X) = X −
√
2.
The following theorem, which we will not explicitly use further in this handout, shows
that divisibility relations in K[X] can be checked by working over a larger ﬁeld.
Theorem 3.3. Let K be a ﬁeld and L be a larger ﬁeld. For f(X) and g(X) in K[X],
f(X) | g(X) in K[X] if and only if f(X) | g(X) in L[X].
Proof. It is clear that divisibility in K[X] implies divisibility in the larger L[X]. Conversely,
suppose f(X) | g(X) in L[X]. Then
g(X) = f(X)h(X)
for some h(X) ∈L[X]. By the division algorithm in K[X],
g(X) = f(X)q(X) + r(X),
where q(X) and r(X) are in K[X] and r(X) = 0 or deg r < deg f. Comparing these two
formulas for g(X), the uniqueness of the division algorithm in L[X] implies q(X) = h(X)
and r(X) = 0. Therefore g(X) = f(X)q(X), so f(X) | g(X) in K[X].
□
Notice how the uniqueness in the division algorithm for polynomials (over ﬁelds) plays a
role in the proof.
4. Raising to the p-th power in characteristic p
The rest of this handout is concerned with applications of the preceding ideas to poly-
nomials in Fp[X].
What we see will be absorbed later into the general ideas of Galois
theory, but already at this point some interesting results can be made rather explicit (e.g.,
Corollary 4.4 and Theorem 5.4) without a lot of general machinery.
The most important operation in characteristic p is the p-th power map x 7→xp because
is not just multiplicative, but also additive:
Lemma 4.1. Let A be a commutative ring with prime characteristic p. Pick a and b in A.
a) (a + b)p = ap + bp.
b) When A is a domain, ap = bp =⇒a = b.
Proof. a) By the binomial theorem,
(a + b)p = ap +
p−1
X
k=1
p
k

ap−kbk + bp.
For 1 ≤k ≤p −1, the integer
 p
k

is a multiple of p (why?), so the intermediate terms are
0 in A.
b) Now assume A is a domain and ap = bp. Then 0 = ap−bp = (a−b)p. (Note (−1)p = −1
for p ̸= 2, and also for p = 2 since 2 = 0 =⇒−1 = 1 in A.) Since A is a domain, a −b = 0,
so a = b.
□
Lemma 4.2. Let F be a ﬁeld containing Fp. For c ∈F, c ∈Fp ⇐⇒cp = c.
Proof. Every element c of Fp satisﬁes the equation cp = c. Conversely, solutions to this
equation are the roots of Xp −X, which has at most p roots in F. The elements of Fp
already fulﬁll this upper bound, so there are no further roots in characteristic p.
□

<!-- page 4 -->
4
KEITH CONRAD
Theorem 4.3. For all f(X) ∈Fp[X], f(X)pr = f(Xpr) for r ≥0. If F is a ﬁeld of
characteristic p other than Fp, this is not always true in F[X].
Proof. Writing
f(X) = cmXm + cm−1Xm−1 + · · · + c1X + c0,
Lemma 4.1a with A = Fp[X] gives
f(X)p = (cmXm + cm−1Xm−1 + · · · + c1X + c0)p
= cp
mXmp + cp
m−1Xp(m−1) + · · · + cp
1Xp + cp
0
= cm(Xp)m + cm−1(Xp)m−1 + · · · + c1Xp + c0,
since cp = c for all c ∈Fp. The last expression is f(Xp). Applying this result r times, we
ﬁnd f(X)pr = f(Xpr).
If F has characteristic p and is not Fp, then F contains an element c which is not in Fp.
Then cp ̸= c by Lemma 4.2, so the constant polynomial f(X) = c (or a monomial cXd)
does not satisfy f(X)p = f(Xp).
□
Let f(X) ∈Fp[X] be nonconstant, with degree m. Let L ⊃Fp be a ﬁeld over which
f(X) decomposes into linear factors, i.e., (2.1) holds. It is possible that some of the roots
of f(X) are multiple roots. As long as that does not happen, the following corollary says
something about the p-th powers of the roots.
Corollary 4.4. When f(X) ∈Fp[X] has distinct roots, raising all roots of f(X) to the
p-th power permutes the roots:
{αp
1, . . . , αp
m} = {α1, . . . , αm}.
Proof. Let S = {α1, · · · , αm}. Since f(X)p = f(Xp) by Theorem 4.3, the p-th power of
each root of f(X) is again a root of f(X). Therefore raising to the p-th power deﬁnes a
function ϕ: S →S. By Lemma 4.1b, ϕ takes diﬀerent values on diﬀerent elements of S.
Since S is a ﬁnite set, ϕ must assume each element of S as a value (in the language of set
theory, a one-to-one function from a ﬁnite set to itself is onto), so ϕ is a permutation of
S.
□
Example 4.5. Consider X3 + X2 + 1 ∈F5[X]. In Example 2.6, we found a ﬁeld F ⊃F5
in which the polynomial has roots t, 2t2 + 3t, and 3t2 + t + 4. If we raise these to the ﬁfth
power, then t5 = 3t2 + t + 4, (2t2 + 3t)5 = t, and (3t2 + t + 4)5 = 2t2 + 3t.
5. Roots of irreducibles in Fp[X]
All the roots of an irreducible polynomial in Q[X] are not generally expressible in terms
of a particular root, with X3 −2 being a typical example. (The ﬁeld Q(
3√
2) contains only
one root to this polynomial, not all 3 roots.) However, the situation is markedly simpler
over ﬁnite ﬁelds. In this section we will make explicit the relations among the roots of
an irreducible polynomial in Fp[X]. In short, we can obtain all roots from one root by
repeatedly taking p-th powers. The precise statement is in Theorem 5.4.
Lemma 5.1. For h(X) in Fp[X] with degree m, Fp[X]/(h(X)) has size pm.
Proof. By the division algorithm in Fp[X], every congruence class modulo h(X) contains a
unique remainder from division by h(X). These remainders are the polynomials
cm−1Xm−1 + · · · + c1X + c0,

<!-- page 5 -->
ROOTS AND IRREDUCIBLES
5
with cj ∈Fp. (Note cm−1 = 0 if the remainder has small degree.) There are pm such
representatives.
□
Lemma 5.2. When F is a ﬁnite ﬁeld with size q, cq = c for all c in F.
Proof. For c ̸= 0 in F, cq−1 = 1 (since F × is a group of size q −1) so multiplying through
by c shows cq = c. This last equation is obviously satisﬁed also by c = 0.
□
Theorem 5.3. Let π(X) be irreducible of degree d in Fp[X].
a) In Fp[X], π(X) | (Xpd −X).
b) For n ≥0, π(X) | (Xpn −X) ⇐⇒d | n.
Proof. The divisibility in (a) in the same as the congruence Xpd ≡X mod π(X), or equiva-
lently the equation X
pd
= X in Fp[X]/(π(X)). Such an equation follows immediately from
Lemmas 5.1 and 5.2, using the ﬁeld Fp[X]/(π(X)).
To prove (⇐=) in (b), write n = kd. Starting with X ≡Xpd mod π(X) (from (a)) and
applying the pd-th power to both sides k times, we obtain
X ≡Xpd ≡Xp2d ≡· · · ≡Xp(k−1)d ≡Xpkd = Xpn mod π(X).
Thus π(X) | (Xpn −X) in Fp[X].
Now we prove (=⇒) in (b). We assume
(5.1)
Xpn ≡X mod π(X)
and want to show d | n. Write n = dq + r with 0 ≤r < d. We will show r = 0.
We have Xpn = Xpdqpr = (Xpdq)pr. Since d | dq, Xpdq ≡X mod π(X) by (⇐=), so
Xpn ≡Xpr mod π(X). Thus, by (5.1),
(5.2)
Xpr ≡X mod π(X).
This tells us that one particular element of Fp[X]/(π(X)), the class of X, is equal to its own
pr-th power. Let’s extend this property to all elements of Fp[X]/(π(X)). For f(X) ∈Fp[X],
f(X)pr = f(Xpr) by Theorem 4.3. Combining with (5.2),
f(X)pr ≡f(X) mod π(X).
Therefore in Fp[X]/(π(X)) the congruence class of f(X) is equal to its own pr-th power.
As f(X) is a general polynomial in Fp[X], we have proved every element of Fp[X]/(π(X))
is its own prth power (in Fp[X]/(π(X))).
Consider now the polynomial T pr −T. When r > 0, this is a polynomial with degree
pr > 1, and we have found pd diﬀerent roots of this polynomial in Fp[X]/(π(X)) (namely,
every element of this ﬁeld is a root). Therefore pd ≤pr, so d ≤r. But, recalling where r
came from, r < d. This is a contradiction, so r = 0. That proves d | n.
□
Theorem 5.4. Let π(X) be irreducible in Fp[X] with degree d and F ⊃Fp be a ﬁeld in
which π(X) has a root, say α. Then π(X) has roots α, αp, αp2, · · · , αpd−1. These d roots
are distinct; more precisely, when i and j are nonnegative, αpi = αpj ⇐⇒i ≡j mod d.
Proof. Since π(X)p = π(Xp) by Theorem 4.3, we see αp is also a root of π(X), and likewise
αp2, αp3, and so on by iteration.
Once we reach αpd we have cycled back to the start:
αpd = α by Theorem 5.3a. (Write the divisibility in Theorem 5.3a as an equation in Fp[X]
and then substitute α for X.)

<!-- page 6 -->
6
KEITH CONRAD
Now we will show for i, j ≥0 that αpi = αpj ⇐⇒i ≡j mod d. Since αpd = α, the
implication (⇐=) is straightforward.
To argue in the other direction, we may suppose
without loss of generality that i ≤j, say j = i + k with k ≥0. Then
αpi = αpi+k = (αpk)pi.
Applying Lemma 4.1b to this equality i times, with A = F, we have α = αpk. Therefore α
is a root of Xpk −X, so π(X) | (Xpk −X) in Fp[X] by Theorem 3.1. We conclude d | k by
Theorem 5.3b, so i ≡j mod d.
□
Since π(X) has at most d = deg π roots in a ﬁeld containing Fp, Theorem 5.4 tells us
α, αp, . . . , αpd−1 are a complete set of roots of π(X) and these roots are distinct.
Example 5.5. The polynomial X3 + X + 1 is irreducible in F2[X].
In the ﬁeld F =
F2[t]/(t3 + t + 1), one root of the polynomial is t. The other two roots are t2 and t4.
If we wish to write the third root without going beyond the second power of t, note
t4 ≡t2 + t mod t3 + t + 1. Therefore, the roots of X3 + X + 1 in F are t, t2, and t2 + t.
Now we can remove the mystery behind the discovery of the roots in Example 2.6. There
was no guessing or brute-force searching involved.
The roots are t, t5, and t25.
Then
remainders modulo t3 + t2 + 1 (in F5[t]) were computed for t5 and t25.
6. Finding irreducibles in Fp[X]
A nice application of Theorem 5.3 is the next result, which is due to Gauss. It describes
all irreducible polynomials of a given degree in Fp[X] as factors of a certain polynomial.
Theorem 6.1. Let n ≥1. In Fp[X],
(6.1)
Xpn −X =
Y
d|n
Y
deg π=d
πmonic
π(X),
where π(X) is irreducible.
Let’s look at some examples to understand what the theorem is telling us, before giving
the proof.
Example 6.2. We factor X2n −X in F2[X] for n = 1, 2, 3, 4. We have
X2 −X = X(X + 1),
X4 −X = X(X + 1)(X2 + X + 1),
X8 −X = X(X + 1)(X3 + X + 1)(X3 + X2 + 1),
X16 −X = X(X −1)(X2 + X + 1)(X4 + X + 1)(X4 + X3 + 1)(X4 + X3 + X2 + X + 1).
The following table lists all the irreducibles of each small degree in F2[X]:
n
Irreducibles of degree n in F2[X]
1
X, X + 1
2
X2 + X + 1
3
X3 + X + 1, X3 + X2 + 1
4
X4 + X + 1, X4 + X3 + 1, X4 + X3 + X2 + X + 1

<!-- page 7 -->
ROOTS AND IRREDUCIBLES
7
Proof. From Theorem 5.3, the irreducible factors of Xpn −X in Fp[X] are the irreducibles
with degree dividing n. What remains is to show that each monic irreducible factor of
Xpn −X appears only once in the factorization.
Let π(X) be an irreducible factor of
Xpn −X in Fp[X]. We want to show π(X)2 does not divide Xpn −X.
There is a ﬁeld F in which π(X) has a root, say α.
We will work in F[X].
Since
π(X) | (Xpn −X), Xpn −X = π(X)k(X), so αpn = α. Then in F[X],
Xpn −X = Xpn −X −0
= Xpn −X −(αpn −α)
= (X −α)pn −(X −α) by Lemma 4.1a
= (X −α)((X −α)pn−1 −1).
The second factor in this last expression does not vanish at α, so (X −α)2 does not divide
Xpn −X. Therefore π(X)2 does not divide Xpn −X in Fp[X].
□
Let Np(n) be the number of monic irreducibles of degree n in Fp[X].
For instance,
Np(1) = p. On the right side of (6.1), for each d dividing n there are Np(d) diﬀerent monic
irreducible factors of degree d. Taking degrees of both sides of (6.1),
(6.2)
pn =
X
d|n
dNp(d)
for all n ≥1. Looking at this formula over all n lets us invert it to get a formula for Np(n).
Example 6.3. Np(2) = p2 −p
2
,
Np(3) = p3 −p
3
,
Np(12) = p12 −p6 −p4 + p2
12
.
A formula for Np(n) for all n ≥1 can be derived from (6.1) using the M¨obius inversion
formula, which we omit.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*