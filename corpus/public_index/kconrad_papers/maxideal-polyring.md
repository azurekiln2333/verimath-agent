# Maxideal Polyring

> **Source**: https://kconrad.math.uconn.edu/blurbs/maxideal-polyring.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
KEITH CONRAD
1. Introduction
Our goal here is to describe the maximal ideals in three types of polynomial rings:
K[x1, . . . , xn] when K is an algebraically closed ﬁeld, K[x1, . . . , xn] when K is an arbi-
trary ﬁeld, and Z[x]. The ﬁrst case has a particularly simple answer (although the proof
requires a fair bit of preliminary work), the second case is a combination of the ﬁrst case
and a group action, and the third case ties together Z and all ﬁnite ﬁelds (not just ﬁelds of
prime order).
The proofs in each case will use properties of integral ring extensions, which are a gen-
eralization of algebraic ﬁeld extensions to the setting of rings, so we will develop a few
results about integral ring extensions ﬁrst in Section 2. We’ll describe maximal ideals in
K[x1, . . . , xn] for all ﬁelds K in Section 3, use that description for algebraically closed K to
prove the Nullstellensatz in Section 4, and describe maximal ideals in Z[x] in Section 5.
2. Integral extensions
For a ﬁeld extension L/K, we call α in L algebraic over K when α is the root of a
nonconstant polynomial f(x) in K[x].
Scaling f by a nonzero constant in K does not
change its roots, so we can assume f(x) is monic by dividing f(x) by its leading coeﬃcient.
If the coeﬃcients of the polynomials do not form a ﬁeld then saying something is the root
of a monic polynomial is a more restrictive condition than it being the root of a general
(nonconstant) polynomial. The more restrictive condition (root of a monic polynomial) has
many of the useful properties of algebraic extensions.
Deﬁnition 2.1. Let B/A be an extension of commutative rings.1 We call b ∈B integral
over A if there is a monic f(x) ∈A[x] such that f(b) = 0. The ring B is called integral over
A or an integral ring extension of A if each element of B is integral over A.
Example 2.2. In Q(
√
5), numbers a + b
√
5 with a, b ∈Z are integral over Z since a + b
√
5
is a root of
(x −(a + b
√
5))(x −(a −b
√
5)) = x2 −2ax + (a2 −2b2),
which is monic in Z[x]. Other numbers in Q[
√
5] can be integral over Z. For example,
(1 +
√
5)/2 is not in Z[
√
5] but is integral over Z since it is a root of x2 −x −1.
Example 2.3. In a ring extension B/A, every a ∈A is integral over A since a is a root of
x −a.
Example 2.4. The number 1/2 is a root of 2x −1 in Z[x], but this does not directly say
whether or not 1/2 integral over Z since 2x −1 is not monic. In fact, 1/2 is not integral
over Z using an argument by contradiction: if some monic f(x) in Z[x] has f(1/2) = 0 and
we write f(x) = xn + an−1xn−1 + · · · + a1x + a0, then
0 = f
1
2

= 1
2n + an−1
2n−1 + · · · + a1
2 + a0,
1All rings here will be commutative, so we will henceforth stop using the label “commutative” each time.
1

<!-- page 2 -->
2
KEITH CONRAD
so multiplying through by 2n gives us
0 = 1 + 2an−1 + · · · + 2n−1a1 + 2na0,
which is impossible since the number on the right side is odd. In a similar way, a rational
number is integral over Z if and only if it is an integer: if a/b is rational in reduced form
and it is integral over Z, then running through an argument like the one we made with 1/2
shows b | an, so b = ±1 since (a, b) = 1. (This is essentially the rational roots theorem.)
By similar reasoning, if A is a UFD with fraction ﬁeld F, the only elements of F that
are integral over A are the elements of A. For example, taking A = Z[1/N] for N ∈Z+
and F = Q, the only rational numbers integral over Z[1/N] are those in Z[1/N].
Example 2.5. In Q(
√
5), (2+
√
5)/3 is a root of f(x) = x2 −(4/3)x−1/9, which is monic.
This does not tell us whether or not (2 +
√
5)/3 is integral over Z (it really isn’t), but we
can say (2 +
√
5)/3 is integral over Z[1/3] since f(x) is monic with coeﬃcients in Z[1/3].2
Example 2.6. If L/K is a ﬁeld extension, then elements of L are integral over K if and
only if they are algebraic over K because a polynomial in K[x] can be scaled within K[x]
to become monic without changing its roots.
We will prove two important properties of integrality for a ring extension B/A:
• if B/A is an integral ring extension where A and B are integral domains, then A is
a ﬁeld if and only if B is a ﬁeld (Theorem 2.7),
• the elements of B that are integral over A form a subring (Corollary 2.10).
Theorem 2.7. Let B/A be an integral ring extension of integral domains. Then B is a
ﬁeld if and only if A is a ﬁeld.
Proof. Suppose A is a ﬁeld. For nonzero b ∈B, we want to show b has a multiplicative
inverse in B, Let b be a root of a monic polynomial f(x) = xn +an−1xn−1 +· · ·+a1x+a0 in
A[x] and pick n to be as small as possible. Then the constant term a0 can’t be 0: if a0 = 0
then
0 = f(b) = bn + an−1bn−1 + · · · + a1b = b(bn−1 + an−1bn−2 + · · · + a1),
so bn−1 + an−1bn−2 + · · · + a1 = 0 since B is an integral domain and b ̸= 0. That equation
contradicts the minimality of n, so a0 ̸= 0.
Isolate the constant term in the equation f(b) = 0:
0 = bn + an−1bn−1 + · · · + a1b + a0 =⇒b(bn−1 + an−1bn−2 + · · · + a1) = −a0.
Since a0 ̸= 0 in A and A is a ﬁeld, −a0 has an inverse a′. Multiplying through the last
equation by a′,
b(a′bn−1 + a′an−1bn−2 + · · · + a′a1) = 1.
Thus b has an inverse in A[b] ⊂B. Since this holds for all nonzero b in B, B is a ﬁeld.
Now suppose B is a ﬁeld. Each nonzero a ∈A has a multiplicative inverse b in B. We
will show b ∈A. Since b is integral over A, we have a relation
bn + an−1bn−1 + · · · + a1b + a0 = 0
for some n ≥1 and a0, . . . , an−1 ∈A. Multiplying through the equation by an−1 and using
the relation ab = 1 kills oﬀall powers of b except a single b in the ﬁrst term:
b(ab)n−1 + an−1(ab)n−1 + · · · + a1an−2(ab) + an−1a0 = 0,
so
b + an−1 + · · · + a1an−2 + an−1a0 = 0.
All terms on the left after b are in A, so b ∈A.
□
2Note the common denominator of the coeﬃcients is 9 and Z[1/3] = Z[1/9] since 1/3 = 3(1/9).

<!-- page 3 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
3
To prove that the elements of B integral over A form a subring, we will need a characteri-
zation of integrality that is linearized (i.e., formulated in terms of modules). It is analogous
to the theorem that in a ﬁeld extension L/K, elements of L are algebraic over K if and
only if they lie in an intermediate ﬁeld extension that is ﬁnite-dimensional over K.
Theorem 2.8. For a ring extension B/A and b ∈B, the following are equivalent:
(i) b is integral over A;
(ii) the subring A[b] is a ﬁnitely generated A-module;
(iii) there is a subring of B containing A and b that is a ﬁnitely generated A-module.
Proof. (i) ⇒(ii): Say bn + an−1bn−1 + · · · + a1b + a0 = 0, where ai ∈A. Then
bn = −a0 −a1b −· · · −an−1bn−1 ∈A + Ab + · · · + Abn−1,
so
bn+1 ∈Ab + Ab2 + · · · + Abn ⊂A + Ab + · · · + Abn−1
since bn ∈Pn−1
i=0 Abi. By induction, bm ∈A + Ab + · · · + Abn−1 for all m ≥n, so
A[b] =
X
i≥0
Abi = A + Ab + · · · + Abn−1.
(ii) ⇒(iii): Use the subring A[b].
(iii) ⇒(i): Say R is a ring where A ⊂R ⊂B with b ∈R, and
R = Ax1 + Ax2 + · · · + Axn.
The xi’s are not all 0, since 1 ∈R and 1 ̸= 0. (We’re bypassing the trivial case that A
is the zero ring, whose only ring extension is itself. The theorem is obvious in that case.)
Multiplication by b sends R back to R, so
bxi = ai1x1 + · · · + ainxn,
aij ∈A.
Collect those equations over all i into a vector-matrix equation





bx1
bx2
...
bxn




=





a11
a12
· · ·
a1n
a21
a22
· · ·
a2n
...
...
...
...
an1
an2
· · ·
ann










x1
x2
...
xn




.
Thus
b





x1
x2
...
xn




=





a11
a12
· · ·
a1n
a21
a22
· · ·
a2n
...
...
...
...
an1
an2
· · ·
ann










x1
x2
...
xn




,
which implies
(2.1)
(bIn −(aij))





x1
x2
...
xn




=





0
0
...
0




.
Since the vector (x1, . . . , xn) is not zero, (2.1) says the matrix bIn −(aij) ∈Mn(B) is not
one-to-one on Bn. If B were an integral domain, then by looking at (2.1) over the fraction
ﬁeld of B would tell us the matrix bIn −(aij) has determinant 0. Since that determinant is
a monic polynomial expression in b with coeﬃcients in A, the equation det(bIn −(aij)) = 0
would show us b is integral over A.

<!-- page 4 -->
4
KEITH CONRAD
When B is not an integral domain, so B has zero divisors, the determinant of a square
matrix over B that is not injective (that is, it kills a nonzero vector) need not be 0. It turns
out that nevertheless det(bIn −(aij)), which is a monic polynomial in b with coeﬃcients in
A does equal 0, but we will need a result from linear algebra over rings to explain this.
In linear algebra, there is a “universal” formula for inverting a square matrix M: M−1 =
1
det M adj(M), where adj(M), called the classical adjoint of M, has (i, j) entry equal to the
determinant of the matrix M with row j and column i removed, multiplied by (−1)i+j.
(For example, adj( a b
c d ) = (
d −b
−c
a ).) This universal inverse formula doesn’t always make
sense, since the scalar det M might not be invertible, but adj(M) always makes sense since
its entries are just polynomials in the entries of M. Multiplying through the inverse matrix
formula by det M and by M gives the algebraic identity
adj(M)M = (det M)In.
This formula is valid for all square matrices over all (commutative) rings. It says we can
multiply each square matrix M by a particular second matrix to produce a diagonal matrix
with the number det M on the diagonal.
Let D(b) = det(bIn −(aij)) and multiply both sides of (2.1) on the left by adj(bIn −(aij))
to get
D(b)In





x1
x2
...
xn




=





0
0
...
0




=⇒D(b)





x1
x2
...
xn




=





0
0
...
0




.
Comparing coordinates,
D(b)xi = 0 for all i.
Since R = Ax1 + · · · + Axn,
D(b)r = 0 for all r ∈R.
Using r = 1, we get D(b) = 0. Since D(b) is a monic polynomial in b with coeﬃcients in A,
b is integral over A.
□
Remark 2.9. The proof of (iii) ⇒(i) had a simpler ending when B is an integral domain
(no need for classical adjoint matrices), and this is the only case we will be using later.
Corollary 2.10. In a ring extension B/A, the elements of B that are integral over A form
a subring containing A.
Proof. Let R be the set of elements of B that are integral over A, so A ⊂R. To show R is
a subring of B, we need to show for b and b′ in R that b ± b′ and bb′ are in R. Since b and
b′ are integral over R, the subrings A[b] and A[b′] are ﬁnitely generated A-modules, say
A[b] = A + Ab + · · · + Abm−1,
A[b′] = A + Ab′ + · · · + Ab′n−1,
where b is the root of a monic polynomial in A[x] of degree m and b′ is the root of a
monic polynomial in A[x] of degree n. Then the subring A[b, b′] is ﬁnitely generated as an
A-module:
A[b, b′] =
X
i,j≥0
Abib′j =
X
i≤m−1
j≤n−1
Abib′j.
Since this subring of B contains b ± b′ and bb′, and A[b, b′] is a ﬁnitely generated A-module,
b ± b′ and bb′ are integral over A by (iii) ⇒(i) in Theorem 2.8.
□
Our next and ﬁnal result on integral ring extensions is about ﬁnitely generated algebras,
rather than ﬁnitely generated modules. Let’s recall the diﬀerence in the two meanings of
“ﬁnitely generated” for A-modules and associative A-algebras.

<!-- page 5 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
5
• A ﬁnitely generated A-module is Aα1 + · · · + Aαn: all elements of the module come
from ﬁnitely many elements α1, . . . , αn by using their A-linear combinations.
• A ﬁnitely generated associative A-algebra has the form A[α1, . . . , αn]: all elements of
the A-algebra come from ﬁnitely many elements α1, . . . , αn by using their polynomial
expressions with A-coeﬃcients.
Finite generatedness of an A-module is about linear combinations of ﬁnitely many ele-
ments with coeﬃcients in A, while ﬁnite generatedness for an associative A-algebra is about
polynomials in ﬁnitely many elements with coeﬃcients in A. For example, Z[x] is a ﬁnitely
generated Z-algebra but is not a ﬁnitely generated Z-module since linear combinations of
ﬁnitely many polynomials don’t give us polynomials of arbitrarily large degree.
Theorem 2.11 (Zariski). Let L/K be a ﬁeld extension such that L is a ﬁnitely generated K-
algebra. Then L is ﬁnite-dimensional over K. In particular, L/K is an algebraic extension.
Proof. We present an argument of Azarang [1]. We will induct on the number of generators
of the top ﬁeld as an algebra over the bottom ﬁeld. Write L = K[α1, . . . , αn]. We will show
that if L is a ﬁnitely generated K-algebra then each αi is algebraic over K, as that implies
dimK(L) is ﬁnite (only ﬁnitely many powers of each αi are needed) and that in turn implies
each element of L is algebraic over K.
Base case n = 1. If n = 1 then L = K[α] for some α. If α is not algebraic over K
then K[α] ∼= K[t] (polynomial ring over K in one indeterminate t transcendental over K)
and this is not a ﬁeld. Therefore if K[α] is a ﬁeld then α must be algebraic over K. This
theorem we are proving is a generalization of the observation about α being algebraic over
K is equivalent to K[α] being ﬁnite-dimensional over K.
The case n = 2. We will derive the case n = 2 from n = 1 since all the key ideas for the
general inductive step are used when n = 2 but the notation is a little simpler.
Suppose the theorem is proved for n = 1 with arbitrary base ﬁelds. If L = K[α, β] is a
ﬁeld, we want to show α and β are algebraic over K. We will prove this by contradiction:
assume α or β is not algebraic over K, say β is transcendental over K. Rewrite β as t so it
looks transcendental over K. Then
L := K[t][α] ⊂K(t)[α] ⊂L
since L is a ﬁeld. Thus
L = K(t)[α],
which shows L is a ﬁeld generated as a K(t)-algebra by 1 element. By the base case, α is
algebraic over the ﬁeld K(t): f(α) = 0 for some monic f(x) ∈K(t)[x].
The coeﬃcients of f(x) are ratios of elements of K[t]. Let d(t) ∈K[t] be a common de-
nominator of the coeﬃcients of f(x), so f(x) is monic in K[t, 1/d(t)][x]. Thus the condition
f(α) = 0 tells us α is integral over the ring
R := K

t,
1
d(t)

.
Since L = K[t][α], L is a ﬁeld, and K[t] ⊂R ⊂L, L = R[α]. That α is integral over R
implies L is an integral ring extension of R (Corollary 2.10). Then L being a ﬁeld implies
R is a ﬁeld (Theorem 2.7). From K[t] ⊂R ⊂K(t), we conclude R = K(t).
We will show R ̸= K(t). All elements of R have denominators that are powers of d(t),
and d(t) has ﬁnitely many monic irreducible factors in K[t]. Since K[t] has inﬁnitely many
monic irreducibles (mimic Euclid’s proof of the inﬁnitude of primes in Z+), some monic
irreducible p(t) in K[t] is not a factor of d(t). Then 1/p(t) ∈K(t) but unique factorization
in K[t] implies 1/p(t) ̸∈R (if 1/p(t) ∈R then p(t) divides d(t)). This contradiction implies
α and β are algebraic over K, so L = K[α, β] is ﬁnite-dimensional over K.

<!-- page 6 -->
6
KEITH CONRAD
General inductive step. Suppose L = K[α1, . . . , αn] where n ≥2 and the theorem is
proved for all ﬁeld extensions where the top ﬁeld is ﬁnitely generated as an algebra over the
bottom ﬁeld and the number of algebra generators is n −1. To prove each αi is algebraic
over K, we argue by contradiction: assume some αi is not algebraic over K, and without
loss of generality let it be αn. Rewrrite αn as t. Then
L = K[t][α1, . . . , αn−1] ⊂K(t)[α1, . . . , αn−1] ⊂L,
so
L = K(t)[α1, . . . , αn−1].
Therefore L is a ﬁeld generated as a K(t)-algebra by n −1 elements, so α1, . . . , αn−1 are all
algebraic over K(t) by induction: fj(αj) = 0 for monic fj(x) ∈K(t)[x].
Since the coeﬃcients of fj(x) are ratios of elements of K[t], write d(t) for a common
denominator of the coeﬃcients of f1(x), . . . , fn−1(x).
That makes each fj(x) monic in
K[t, 1/d(t)][x], so α1, . . . , αn−1 are all integral over the ring
R := K

t,
1
d(t)

.
Since L = K[t][α1, . . . , αn−1], L is a ﬁeld, and K[t] ⊂R ⊂L, L = R[α1, . . . , αn−1]. From
α1, . . . , αn−1 all being integral over R, L is an integral extension of R (Corollary 2.10), so L
being a ﬁeld implies R is a ﬁeld (Theorem 2.7). Thus K[t] ⊂R ⊂K(t) implies R = K(t),
so K[t, 1/d(t)] = K(t). This is a contradiction (see n = 2), so α1, . . . , αn are algebraic over
K and L = K[α1, . . . , αn] is ﬁnite-dimensional over K.
□
Theorem 2.11 is called Zariski’s lemma and was proved by Zariski in 1947 [10].
Its
signiﬁcance is that it shows for ﬁeld extensions L/K, the linear and ring-theoretic notions
of ﬁniteness are equivalent: L is a ﬁnitely generated K-algebra if and only if L is a ﬁnite-
dimensional K-vector space. It is easy to see that if dimK(L) is ﬁnite then L is a ﬁnitely
generated K-algebra (if L = Pn
i=1 Kαi then L = K[α1, . . . , αn] since L is a ring). The less
clear converse direction is Zariski’s lemma. Our proof of Zariski’s lemma is similar to the
one in Fulton’s book [2, Sect. 1.10] except for the way integrality properties are applied.
Corollary 2.12. For each maximal ideal m in K[x1, . . . , xn], where K is a ﬁeld, the ﬁeld
K[x1, . . . , xn]/m is a ﬁnite extension of K.
Proof. In L := K[x1, . . . , xn]/m, set xi = xi mod m. Then L = K[x1, . . . , xn], so L is a ﬁeld
(since m is a maximal ideal) and is ﬁnitely generated as a K-algebra. By Theorem 2.11,
[L : K] is ﬁnite.
□
The next corollary generalizes the fact that when K is a ﬁeld, K(α) = K[α] if and only
if α is algebraic over K.
Corollary 2.13. For a ﬁeld K, we have K(α1, . . . , αn) = K[α1, . . . , αn] if and only if
α1, . . . , αn are all algebraic over K.
Proof. The equivalence when n = 1 is an elementary result about algebraic elements over a
ﬁeld, mentioned before the corollary. For n ≥2, if all αi are algebraic over K, then
K(α1, . . . , αn) = K(α1, . . . , αn−1)(αn) = K(α1, . . . , αn−1)[αn]
since αn is algebraic over K(α1, . . . , αn−1). We can assume K(α1, . . . , αn−1) = K[α1, . . . , αn−1]
by induction on n, so K(α1, . . . , αn) = K[α1, . . . , αn−1][αn] = K[α1, . . . , αn−1, αn].
Conversely, if K(α1, . . . , αn) = K[α1, . . . , αn], then the ﬁeld L := K(α1, . . . , αn) is a
ﬁnitely generated K-algebra, in which case Theorem 2.11 tells us the ﬁeld extension L/K
is ﬁnite, so each αi is algebraic over K.
□

<!-- page 7 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
7
3. Maximal ideals in polynomial rings over a field
Armed with Zariski’s lemma, or more precisely the corollary to it, we are ready to describe
the maximal ideals in K[x1, . . . , xn] for a ﬁeld K. We will ﬁrst treat the case when K is an
algebraically closed ﬁeld, where the description is especially simple.
Theorem 3.1. Let K be a ﬁeld.
(1) For c1, . . . , cn ∈K, the ideal (x1 −c1, . . . , xn −cn) in K[x1, . . . , xn] is maximal.
(2) If K is an algebraically closed ﬁeld then each maximal ideal of K[x1, . . . , xn] has the
form (x1 −c1, . . . , xn −cn) for unique c1, . . . , cn ∈K.
In particular, for algebraically closed K the maximal ideals in K[x1, . . . , xn] are the polyno-
mials in K[x1, . . . , xn] vanishing at some point in Kn and this sets up a bijection between
maximal ideals in K[x1, . . . , xn] and points in Kn.
Proof. (1) Let I = (x1 −c1, . . . , xn −cn). Since xi ≡ci mod I,
f(x1, . . . , xn) ≡f(c1, . . . , cn) mod I
for all f in K[x1, . . . , xn].
Thus f(c1, . . . , cn) = 0 if and only if f(x1, . . . , xn) ∈I, so
the evaluation homomorphism K[x1, . . . , xn] →K where f(x1, . . . , xn) 7→f(c1, . . . , cn)
has kernel I.
This homomorphism is surjective (elements of K map to themselves), so
K[x1, . . . , xn]/I ∼= K. The right side K is a ﬁeld, so I is maximal in K[x1, . . . , xn].
(2). Let m be a maximal ideal of K[x1, . . . , xn] when K is algebraically closed. The
ﬁeld K[x1, . . . , xn]/m is a ﬁnite extension of K by Corollary 2.12. Since K is algebraically
closed, its only ﬁnite extension is itself. Therefore K[x1, . . . , xn]/m has degree 1 over K, so
each coset mod m is represented by an element of K. Thus xi ≡ci mod m for some ci ∈K.
Then xi −ci ∈m, so (x1 −c1, . . . , xn −cn) ⊂m. That containment must be equality since
the ideal (x1 −c1, . . . , xn −cn) is maximal by (a).
If the ideals (x1 −c1, . . . , xn −cn) and (x1 −c′
1, . . . , xn −c′
n) in K[x1, . . . , xn] are equal
then ci −c′
i is contained in the ideal since it equals (ci −xi) −(c′
i −xi). A proper ideal in
K[x1, . . . , xn] can’t contain an element of K×, so ci −c′
i = 0 for all i. Thus ci = c′
i.
□
Example 3.2. Every maximal ideal in C[x1, . . . , xn] has the form (x1 −c1, . . . , xn −cn) for
unique c1, . . . , cn ∈C. That C is algebraically closed is equivalent to saying all maximal
ideals of C[x] have the form (x −c) for c ∈C. Therefore the description of maximal ideals
in C[x1, . . . , xn] for all n could be considered a generalization of the fundamental theorem
of algebra to multivariable polynomial rings over C.3
Remark 3.3. The bijection between points in Cn and maximal ideals in C[x1, . . . , xn] is
an important intuition in mathematics: in a commutative ring, think about its maximal
ideals as the points in a space. Besides C[x1, . . . , xn], two more rings where this intuition
holds are C(X, R) and C(X, C) – the continuous real-valued and complex-valued functions
on a compact Hausdorﬀspace X. The maximal ideals in each ring come from points of X:
mx = {f : f(x) = 0}. Moreover, X up to homeomorphism is determined by C(X, R) and
C(X, C) up to isomorphism (as a ring and as a C∗-algebra, respectively). This is called the
Gelfand–Kolmogorov theorem for C(X, R) and the Gelfand–Naimark theorem for C(X, C).
When K is not algebraically closed, maximal ideals in K[x1, . . . , xn] need not have the
form (x1 −c1, . . . , xn −cn) for some ci ∈K. For example, if p(x) is irreducible in K[x]
with deg p > 1 (there are always such irreducibles when K is not algebraically closed), the
ideal (p(x)) in K[x] is maximal and not of the form (x −c) where c ∈K. But there is a
connection between (p(x)) in K[x] and the maximal ideal (x−c) in K[x] where c is a root of
3A simpler generalization of the fundamental theorem of algebra to C[x1, . . . , xn] is that every nonconstant
polynomial equation f(x1, . . . , xn) = 0 in C[x1, . . . , xn] has a complex zero.

<!-- page 8 -->
8
KEITH CONRAD
p(x): (p(x)) = (x −c) ∩K[x], where (x −c) is an ideal in K[x]. Consider the maximal ideal
(x2 + 1) in R[x]: x2 + 1 has roots ±i and (x2 + 1) = (x −i) ∩R[x] = (x + i) ∩R[x], where
(x ± i) are ideals in C[x]. Indeed, a polynomial in R[x] has root i or −i if and only if it is
divisible by x2 +1 in R[x] (the minimal polynomial of ±i over R). This idea carries over to
maximal ideals in a polynomial ring over an arbitrary ﬁeld K and its algebraic closure K.
Theorem 3.4. Let K be a ﬁeld and K be an algebraic closure of K.
(1) For each c = (c1, . . . , cn) in K
n, set mc = (x1 −c1, . . . , xn −cn) in K[x1, . . . , xn].
The intersection
mc ∩K[x1, . . . , xn] = {f ∈K[x1, . . . , xn] : f(c) = 0}
is a maximal ideal of K[x1, . . . , xn].
(2) Every maximal ideal in K[x1, . . . , xn] arises in the above way.
Proof. (1) Evaluation at c is a homomorphism K[x1, . . . , xn] →K with image K[c1, . . . , cn],
which is K(c1, . . . , cn) since all ci are algebraic over K. The kernel is mc ∩K[x1, . . . , xn], so
(3.1)
K[x1, . . . , xn]/(mc ∩K[x1, . . . , xn]) ∼= K(c1, . . . , cn).
The right side is a ﬁeld, so mc ∩K[x1, . . . , xn] is a maximal ideal in K[x1, . . . , xn].
(2) Let m be a maximal ideal in K[x1, . . . , xn]. Then K[x1, . . . , xn]/m is a ﬁnite extension
of K (Corollary 2.12), so it is K-isomorphic to a subﬁeld of K: there is an embedding
ϕ: K[x1, . . . , xn]/m →K ﬁxing all of K. Set ci = ϕ(xi mod m). The composition
K[x1, . . . , xn] →K[x1, . . . , xn]/m
ϕ→K,
where the ﬁrst map is reduction mod m, is a ring homomorphism that is the identity on K
and sends each xi to ci, so the composite homomorphism K[x1, . . . , xn] →K is evaluation at
(c1, . . . , cn). Therefore the composite map has kernel mc∩K[x1, . . . , xn]. Also the composite
map has kernel m since ϕ is injective, so m = mc ∩K[x1, . . . , xn].
□
That maximal ideals in K[x1, . . . , xn] are {f ∈K[x1, . . . , xn] : f(c) = 0} for some c ∈K
n
gives two concrete descriptions of maximal ideals in K[x1, . . . , xn] for arbitrary K:
• the set of all polynomials in K[x1, . . . , xn] vanishing at some point c in K
n,
• kernels of K-algebra homomorphisms from K[x1, . . . , xn] to ﬁnite extensions of K.
These generalize the description of maximal ideals of K[x1, . . . , xn] when K is algebraically
closed, in which case K = K and the only ﬁnite extension of K is K. By (3.1), for a
maximal ideal m in K[x1, . . . , xn] the residue ﬁeld K[x1, . . . , xn]/m has degree 1 over K if
and only if m = mc when c ∈Kn, which means m = (x1 −c1, . . . , xn −cn) with ci ∈K.
Other maximal ideals have a residue ﬁeld with K-degree bigger than 1.
When K is not algebraically closed, diﬀerent maximal ideals in K[x1, . . . , xn] could lead
to the same maximal ideal in K[x1, . . . , xn]: for diﬀerent a and b in K
n, ma and mb could
intersect K[x1, . . . , xn] in the same way. For example, when passing from C[x] to R[x],
(x −i) ∩R[x] = (x2 + 1) = (x + i) ∩R[x]. (This is saying elements of R[x] that vanish
at i and at −i are the same, even though i ̸= −i.) We can relate i and −i by Gal(C/R):
they are in the same Galois orbit. It turns out the same kind of relation occurs between a
and b whenever ma and mb intersect K[x1, . . . , xn] in the same way. The group Aut(K/K)
will replace Gal(C/R), and we don’t write Gal(K/K) since K/K might not be a Galois
extension (it might not be separable).
Theorem 3.5. For a and b in K
n,
ma ∩K[x1, . . . , xn] = mb ∩K[x1, . . . , xn] ⇐⇒b = σ(a)
for some σ ∈Aut(K/K), where σ(a1, . . . , an) := (σ(a1), . . . , σ(an)).

<!-- page 9 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
9
Proof. (⇐) If b = σ(a) for some σ ∈Aut(K/K) then
f ∈ma ∩K[x1, . . . , xn] =⇒f(a) = 0 =⇒σ(f(a)) = σ(0) = 0.
Since f has coeﬃcients in K, σ(f(a)) = f(σ(a)) = f(b), so f(b) = 0. Thus
ma ∩K[x1, . . . , xn] ⊂mb ∩K[x1, . . . , xn].
Since a = σ−1(b), the reverse containment also holds.
(⇒) Let m denote the common maximal ideal ma ∩K[x1, . . . , xn] and mb ∩K[x1, . . . , xn].
From the end of the proof of Theorem 3.4, evaluation at a and at b give us two embed-
dings of K[x1, . . . , xn]/m into K that ﬁx K pointwise. The images of these embeddings
are K(a1, . . . , an) and K(b1, . . . , bn), mapping xi mod m to ai and to bi for all i. Since
K[x1, . . . , xn]/m is K-isomorphic to K(a1, . . . , an) and K(b1, . . . , bn), composing one of
these isomorphisms with the inverse of the other is a K-isomorphism σ: K(a1, . . . , an) →
K(b1, . . . , bn), where σ(ai) = bi for all i. Both K(a1, . . . , an) and K(b1, . . . , bn) have alge-
braic closure K, so by Zorn’s lemma σ extends (in many ways) to an automorphism of K.
Denoting one of these extensions still by σ, we have σ ∈Aut(K/K) and σ(a) = b.
□
Theorem 3.4 says each maximal ideal in K[x1, . . . , xn] comes from a point in K
n, and The-
orem 3.5 says diﬀerent points in K
n lead to the same maximal ideal in K[x1, . . . , xn] exactly
when they are in the same orbit of Aut(K/K). So the maximal ideals of K[x1, . . . , xn] for an
arbitrary ﬁeld K are in bijection not with Kn, but with the orbits of the group Aut(K/K)
acting componentwise on K
n.
This illustrates how theorems about algebraically closed
ﬁelds may generalize to all ﬁelds with the help of a group action by Aut(K/K).
Starting from Zariski’s lemma, we found properties of maximal ideals in K[x1, . . . , xn]
for all ﬁelds K. The reasoning can be brought back to the start for a cycle of equivalences.
Theorem 3.6. The following properties of ﬁelds are equivalent.
(1) Zariski’s lemma: for every ﬁeld K, a ﬁnitely generated K-algebra that is a ﬁeld is
ﬁnite-dimensional over K. (Theorem 2.11)
(2) For every ﬁeld K and maximal ideal m in K[x1, . . . , xn], K[x1, . . . , xn]/m is a ﬁnite-
dimensional over K (Corollary 2.12).
(3) For every ﬁeld K, each maximal ideal of K[x1, . . . , xn] is the set of all polynomials
vanishing at some point in K
n (Theorem 3.4).
(4) For every ﬁeld K, each maximal ideal of K[x1, . . . , xn] is the kernel of a surjective K-
algebra homomorphism K[x1, . . . , xn] →L where L is a ﬁeld such that [L : K] < ∞.
Proof. (1) ⇒(2): see the proof of Corollary 2.12.
(2) ⇒(3): see the proof of Theorem 3.4.
(3) ⇒(4): let m be a maximal ideal in K[x1, . . . , xn]. By (3), there is a point (c1, . . . , cn) ∈
K
n such that m is the kernel of the evaluation map ϕ: K[x1, . . . , xn] →K at (c1, . . . , cn).
Set αi = ϕ(xi) in K. The image of ϕ in K is L := K[α1, . . . , αn], which is a ﬁnite extension
of K since each αi is algebraic over K. Therefore m is the kernel of the surjective K-algebra
homomorphism K[x1, . . . , xn] →L and [L : K] < ∞.
(4) ⇒(1): Let F be a ﬁnitely generated K-algebra that is a ﬁeld and α1, . . . , αn be a
ﬁnite set of K-algebra generators of F, so F = K[α1, . . . , αn]. Evaluation of polynomials in
K[x1, . . . , xn] at (α1, . . . , αn) in F n is a K-algebra homomorphism ϕ: K[x1, . . . , xn] →F
that is surjective since the image of ϕ contains K and each αi. Since the image of ϕ is a
ﬁeld, m := ker ϕ is a maximal ideal, so by (4) there is a surjective K-algebra homomorphism
ψ: K[x1, . . . , xn] →L with kernel m where L is a ﬁnite extension ﬁeld of K, so
L = ψ(K[x1, . . . , xn]) ∼= K[x1, . . . , xn]/m ∼= F
as K-algebras. Thus dimK(F) = dimK(L) < ∞.
□

<!-- page 10 -->
10
KEITH CONRAD
4. The Nullstellensatz
Let K be an algebraically closed ﬁeld.
Polynomials in K[x1, . . . , xn] deﬁne functions
Kn →K by substitution of coordinates of a point in Kn for x1, . . . , xn. We link algebra
(polynomials) and geometry (subsets of Kn) by associating to each subset X of Kn the
polynomials vanishing on all of X, and to each subset S of K[x1, . . . , xn] its zero set in Kn.
I(X) := {f ∈K[x1, . . . , xn] : f(a) = 0 for all a ∈X},
Z(S) := {a ∈Kn : f(a) = 0 for all f ∈S}.
Example 4.1. For each point c = (c1, . . . , cn) in Kn,
(4.1)
I(c) = (x1 −c1, . . . , xn −cn)
by the proof of Theorem 3.1(1) and
(4.2)
Z(x1 −c1, . . . , xn −cn) = {c}
since the polynomials x1 −c1, . . . , xn −cn all vanish at point a = (a1, . . . , an) if and only if
ai = ci for all i. Two more examples: Z(0) = Kn and Z(1) = ∅.
It’s easy to see for non-empty subsets X and Y in Kn that X ⊂Y ⇒I(Y ) ⊂I(X) .
We deﬁne I(∅) = K[x1, . . . , xn] so that the implication holds even with the empty set.
For subsets S and T of K[x1, . . . , xn], S ⊂T ⇒Z(T) ⊂Z(S) . Therefore the operations
X ⇝I(X) and S ⇝Z(S) both reverse containments.
Note that I(X) is always an ideal in K[x1, . . . , xn] (hence the notation): if f and g in
K[x1, . . . , xn] vanish at all points of X then so do f ± g and hf for all h ∈K[x1, . . . , xn].
For a subset S of K[x1, . . . , xn], Z(S) = Z(⟨S⟩), where ⟨S⟩is the ideal generated by S.
Therefore in practice we will only look at zero sets of ideals in K[x1, . . . , xn]. For example,
Z(f) = Z((f)): an individual polynomial has the same zero set as the ideal it generates.
The most basic reason it is useful to work with ideals is that all ideals in K[x1, . . . , xn]
are ﬁnitely generated. Therefore each zero set Z(S) in Kn is always the zero set of ﬁnitely
many polynomials: Z(S) = Z(f1, . . . , fr) when ⟨S⟩= (f1, . . . , fr).
Deﬁnition 4.2. A subset V of Kn is called a variety when it is the zero set in Kn of a set
of polynomials in K[x1, . . . , xn]: V = Z(S) for some S ⊂K[x1, . . . , xn].4
Example 4.3. In K = K1, varieties in K are ﬁnite or K since ideals in K[x] are principal
and the zero set in K of a polynomial in K[x] is ﬁnite or K (zero set of the polynomial 0).
Conversely, each ﬁnite set {r1, . . . , rd} in K is Z(f) where f(x) = (x −r1) . . . (x −rd).
We have a mapping from varieties in Kn to ideals in K[x1, . . . , xn] and conversely by
V ⇝I(V ) and J ⇝Z(J), and these are inclusion-reversing. If we apply these twice then
we have easy containments
(4.3)
J ⊂I(Z(J)),
V ⊂Z(I(V ))
since polynomials in J vanish at the zero set of all polynomials in J and points in V are
zeros of all the polynomials that vanish on V . Are the containments equalities? For the
second containment, the answer is yes.
Theorem 4.4. For varieties V in Kn, Z(I(V )) = V .
4The term “variety” means an algebraic analogue of a manifold. Most languages besides English and
German use a cognate of the word “variety” for both varieties and manifolds. Context usually makes it clear
what is meant, but terms such as “algebraic variety” or “analytic/diﬀerentiable variety” could be used to
make a distinction.

<!-- page 11 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
11
Proof. We already saw V ⊂Z(I(V )), so it remains to show Z(I(V )) ⊂V .
Since V is a variety in Kn, V = Z(J) for some ideal J of K[x1, . . . , xn]. (Recall Z(S) =
Z(⟨S⟩) for subsets S of K[x1, . . . , xn].) Then J ⊂I(V ) by the ﬁrst containment in (4.3).
For each a in Z(I(V )), f(a) = 0 for all f ∈I(V ). From J ⊂I(V ), we get f(a) = 0 for all
f ∈J, so a ∈Z(J), and thus a ∈V .
□
We said at the start of the section that K is algebraically closed, but the notation and
terminology we introduced all make sense for arbitrary ﬁelds. Theorem 4.4 holds for all
ﬁelds K. In the following theorems, however, it is essential that K be algebraically closed.
Theorem 4.5. When K is algebraically closed, a variety V in Kn is a point if and only if
I(V ) is a maximal ideal in K[x1, . . . , xn].
Proof. If V = {c} is a point then I(V ) = (x1 −c1, . . . , xn −cn) by (4.1).
If I(V ) is maximal then I(V ) = (x1−c1, . . . , xn−cn) for some c1, . . . , cn ∈K by Theorem
3.1. Polynomials in I(V ) vanish on V by the deﬁnition of I(V ), so V ⊂Z(I(V )). By (4.2),
Z(x1 −c1, . . . , xn −cn) = {c}, so V ⊂{c}. Thus V is a point or V = ∅. If V = ∅then
I(V ) = I(∅) = K[x1, . . . , xn] by deﬁnition, which is not a maximal ideal. Thus V = {c}.
□
Theorem 4.6 (Weak Nullstellensatz). Let K be algebraically closed. If an ideal J in in
K[x1, . . . , xn] is proper, then Z(J) ̸= ∅.
That is, the polynomials in a proper ideal of
K[x1, . . . , xn] all vanish at some common point in Kn.
Proof. Since J is a proper ideal, there is a maximal ideal m in K[x1, . . . , xn] such that
J ⊂m.5 Then Z(m) ⊂Z(J), so we’re reduced to showing Z(m) ̸= ∅for maximal ideals m.
By Theorem 3.1, m = (x1 −c1, . . . , xn −cn), and Z(m) = (c1, . . . , cn) by (4.2).
□
The converse (if Z(J) ̸= ∅, then J is a proper ideal) is obvious, so when K is an alge-
braically closed ﬁeld, a system of polynomial equations f1 = 0, . . . , fr = 0 in K[x1, . . . , xn]
has a common solution in Kn if and only if the ideal (f1, . . . , fr) in K[x1, . . . , xn] is
proper.
Thus f1 = 0, . . . , fr = 0 has no solution in Kn only for the “obvious” reason
that Pn
i=1 figi = 1 for some gi in K[x1, . . . , xn].
To illustrate the close relation between generating sets of ideals and solving systems of
equations, we can reinterpret Gaussian elimination in linear algebra as a procedure to ﬁnd
a nice generating set for an ideal generated by linear polynomials in several variables. For
example, the process of Gaussian elimination
x + 2y = 5
3x −y = 4 ⇝x + 2y = 5
−7y = −11 ⇝x + 2y = 5
y = 11/7 ⇝x = 13/7
y = 11/7
corresponds to ﬁnding new generators for an ideal in Q[x, y]:
(x+2y−5, 3x−y−4) = (x+2y−5, −7y+11) = (x+2y−5, y−11/7) = (x−13/7, y−11/7).
Some systems of polynomial equations over an algebraically closed ﬁeld K have no
solution in K.
Linear algebra oﬀers many examples.
For a higher-degree example, if
f(x, y) = x3 + 2x2y + 3xy2 + y3 + c, g(x, y) = x2 + 2xy, and h(x, y) = y2 + 3xy, then
f(x, y) −xg(x, y) −yh(x, y) = c,
so when c ∈K× there is no solution to f = 0, g = 0, and h = 0 in K2 and no solution
in L2 for every ﬁeld L containing K. The weak Nullstellensatz implies that when K is
algebraically closed, checking if a system of polynomial equations with coeﬃcients in K has
a solution in a larger ﬁeld L is the same as checking for a solution in K.
5The existence of m containing J in an arbitrary nonzero commutative ring uses Zorn’s lemma, but since
K[x1, . . . , xn] is Noetherian we don’t need Zorn’s lemma here.

<!-- page 12 -->
12
KEITH CONRAD
Corollary 4.7. Let K be an algebraically closed ﬁeld. If a system of polynomial equations
f1 = 0, . . . , fr = 0 in K[x1, . . . , xn] has a solution in some ﬁeld extension L/K then the
system has a solution in K.
Proof. In K[x1, . . . , xn], the ideal (f1, . . . , fr) can’t be (1), since then f1g1 + · · · + frgr = 1
for some gi ∈K[x1, . . . , xn] and that prevents the system of equations f1 = 0, . . . , fr = 0
from having a solution in Ln when L ⊃K. Since the ideal (f1, . . . , fr) in K[x1, . . . , xn]
is proper and K is algebraically closed, the system of equations f1 = 0, . . . , fr = 0 has a
solution in Kn by the weak Nullstellensatz.
In more detail, the ideal (f1, . . . , fr) is in a maximal ideal m and m = (x1−c1, . . . , xn−cn)
for some ci ∈K, so (c1, . . . , cn) is a common solution to the system of equations f1 =
0, . . . , fr = 0.
□
Example 4.8. Let f1, . . . , fr be polynomials in Q[x1, . . . , xn]. If the system of polynomial
equations f1 = 0, . . . , fr = 0 has a complex solution (in Cn) then it has an algebraic solution
(in Q
n). That comes from applying Corollary 4.7 to the algebraically closed ﬁeld K = Q:
in brief, the ideal (f1, . . . , fr) in Q[x1, . . . , xn] can’t be (1) since that would forbid a solution
in Cn. Thus (f1, . . . , fr) is in a maximal ideal of Q[x1, . . . , xn], which gives us a solution to
the system of equations in Q
n from the description of maximal ideals in Q[x1, . . . , xn].
We are not saying a complex solution to f1 = 0, . . . , fr = 0 can somehow be converted
into a solution in Q, but only that the existence of a complex solution forces the existence
of an algebraic solution. Such a result may seem surprising, but if the fj are all linear
then it follows from linear algebra: a system of linear equations with Q-coeﬃcients that
has a solution in a larger ﬁeld also has a Q-solution. It is essential that we are looking at
polynomial equations. The transcendental equation sin x −1 = 0 has rational coeﬃcients
and complex solutions {±π/2 + 2πk : k ∈Z}, but no algebraic solution.
We will use the weak Nullstellensatz later in its contrapositive form: if Z(J) = ∅then
1 ∈J. That is, for algebraically closed K, a system of equations f1 = 0, . . . , fr = 0 in
K[x1, . . . , xn] can fail to have a solution in Kn only because f1g1 + · · · + frgr = 1 for some
gi ∈K[x1, . . . , xn]. That need not be a valid explanation when K is not algebraically closed.
For example, x2 + y2 + 1 has no zeros in R2 but this is not because (x2 + y2 + 1)g(x, y) = 1
for some g(x, y) ∈R[x, y].
Returning to the question about whether the containments in (4.3) are equalities, The-
orem 4.4 says “yes” for the second containment, but the answer to the ﬁrst containment is
“no.” An ideal J can be a proper subset of I(Z(J)). Here are two examples.
Example 4.9. In K[x, y] let J = (x2, xy, y2). Then Z(J) = {(0, 0)}, which is a point,
so I(Z(J)) = (x, y), which is strictly bigger than J. In terms of multiplication of ideals,
J = (x, y)2.
Example 4.10. In K[x], let Jk = (xk) for a positive integer k. Then Z(Jk) = {0} and
I(Z(Jk)) = (x), which is strictly bigger than Jk when k ≥2.
While each subset X of Kn leads to an ideal I(X), these ideals are not completely
arbitrary. They have a special property: if f ∈K[x1, . . . , xn] and fm ∈I(X) then f ∈I(X).
Indeed, if f(a)m = 0 for all a ∈X then f(a) = 0 for all a ∈X, so f ∈I(X).
Deﬁnition 4.11. An ideal J in a ring A is called a radical ideal when the following property
holds for all a ∈A: if am ∈J for some m ≥1 then a ∈J.
Example 4.12. We saw above that for every subset X of Kn, I(X) is a radical ideal.
Example 4.13. In the ring Z, where every ideal is principal, a nonzero ideal nZ is a radical
ideal if and only if n is squarefree (not divisible by the square of a prime number).

<!-- page 13 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
13
Example 4.14. Prime ideals are radical ideals: am ∈p ⇒a ∈p by the deﬁnition of an
ideal p being prime. Since maximal ideals are prime ideals, maximal ideals are radical ideals.
It’s easy to see that an intersection of radical ideals is a radical ideal, so an intersection of
prime ideals is a radical ideal even though an intersection of prime ideals is usually not a
prime ideal, e.g., in Z, 3Z ∩5Z = 15Z is a radical ideal but not a prime ideal.
An ideal that is not a radical ideal has a canonical radical ideal associated to it.
Deﬁnition 4.15. For an ideal J in the ring A, the radical of J is
Rad J = {a ∈A : am ∈J for some m ≥1}.
It is not hard to show Rad J is an ideal (it is additively closed by the binomial theorem).
Clearly J is a radical ideal if and only if Rad J = J. Another notation for Rad J is
√
J.
Theorem 4.16. For an ideal J, Rad J is the smallest radical ideal containing J.
Proof. It’s easy to see that J ⊂Rad J. If J′ is a radical ideal that contains J and a ∈Rad J,
so am ∈J for some m ≥1, then am ∈J′, so a ∈J′ since J′ is a radical ideal. Since this
holds for all a ∈Rad J, we get Rad J ⊂J′.
□
Let’s return to the containment J ⊂I(Z(J)) in (4.3). It is not necessarily an equality
(Examples 4.9 and 4.10) and we can reﬁne it in two ways using radicals of ideals.
• Since I(Z(J)) is a radical ideal containing J, Theorem 4.16 tells us Rad J ⊂I(Z(J)).
Perhaps I(Z(J)) = Rad J for each ideal J?
• Since a polynomial f ∈K[x1, . . . , xn] and its powers vanish at the same points in
Kn, Z(J) = Z(Rad J), so each zero set of an ideal can be described as the zero set
of a radical ideal. Perhaps I(Z(J)) = J when J is a radical ideal?
The answer to both questions is yes, and this is Hilbert’s Nullstellensatz [4, p. 320]. This
German term is two words: “Nullstellen + Satz” or “Zeros + theorem”, so “Theorem about
zeros”. The name is due to van der Waerden over 30 years after Hilbert’s proof.6
Theorem 4.17 (Nullstellensatz). When K is algebraically closed. I(Z(J)) = Rad J for
each ideal J in K[x1, . . . , xn]. Equivalently, I(Z(J)) = J for radical ideals J.
Writing J = (f1, . . . , fr), the harder containment I(Z(J)) ⊂Rad J is saying that if a
polynomial g ∈K[x1, . . . , xn] vanishes on Kn wherever the polynomials f1, . . . , fr all vanish,
then gm ∈(f1, . . . , fr) for some m ≥1.
Proof. Since Z(J) = Z(Rad J), the formulas I(Z(J)) = Rad J for all ideals J or I(Z(J)) =
J for radical ideals J are equivalent. We will prove I(Z(J)) = Rad J for all J.
Before the theorem we saw that Rad J ⊂I(Z(J)). To prove I(Z(J)) ⊂Rad J, write
J = (f1, . . . , fr) since ideals in K[x1, . . . , xn] are ﬁnitely generated.
Pick g ∈I(Z(J))
with g ̸= 0. Pass to an ideal in K[x1, . . . , xn, xn+1]: set J′ = (f1, . . . , fr, xn+1g −1) (the
“Rabinowitsch7 trick8 ”). Since g vanishes on Kn wherever all the fi vanish, g vanishes on
Kn+1 wherever all fi vanish (the new last coordinate in Kn+1 doesn’t aﬀect their values).
6See https://mathoverflow.net/questions/391718/first-use-of-term-hilberts-nullstellensatz.
7People say Rabinowitsch was George Rainich, but this is dubious: Rainich was a mathematical physicist.
See the answer by Georges Elencwajg and comments below it at https://mathoverflow.net/questions/
45185/pseudonyms-of-famous-mathematicians/45195.
8A conceptual explanation of this trick is at https://mathoverflow.net/questions/90661/the-rabino
witz-trick. Earlier proofs were much longer. Hilbert called his own proof “very cumbersome” [3, p. 10].

<!-- page 14 -->
14
KEITH CONRAD
So xn+1g −1 doesn’t vanish anywhere that all fi vanish (its value at such a point is −1).
That means Z(J′) = ∅, so the weak Nullstellensatz says J′ = K[x1, . . . , xn+1]. Thus 1 ∈J′:
1 =
r
X
j=1
hj(x1, . . . , xn, xn+1)fj(x1, . . . , xn) + h(x1, . . . , xn, xn+1)(xn+1g −1)
for some h1, . . . , hr, h in K[x1, . . . , xn+1]. In this polynomial identity, set xn+1 = 1/g (we
can do that since g ̸= 0) to get an equation in K[x1, . . . , xn, 1/g] that kills oﬀthe last term
on the right:
1 =
r
X
j=1
hj(x1, . . . , xn, 1/g)fj(x1, . . . , xn).
Multiply both sides by a power of g to clear the reciprocal powers of g from the right side.
When the powers of 1/g are cleared out on the right, we get gm ∈(f1, . . . , fr) = J for some
m ≥1, so g ∈Rad J.
□
Example 4.18. For algebraically closed K, let f be irreducible in K[x1, . . . , xn]. A poly-
nomial g in K[x1, . . . , xn] vanishes at all points in Kn where f vanishes if and only if f is a
factor of g: the polynomials that vanish where f vanishes are the elements of I(Z(f)), and
the Nullstellensatz says I(Z(f)) = Rad(f), which is (f) since f is irreducible. Therefore
g ∈I(Z(f)) is equivalent to g ∈(f), which means f | g.
Example 4.19. For algebraically closed K, let J = (x2, xy, z2) in K[x, y, z]. Then Z(J) =
{(0, b, 0) : b ∈K}, so I(Z(J)) = {g ∈K[x, y, z] : g(0, b, 0) = 0 for all b ∈K}. What is a
generating set of polynomials for this ideal? It contains x and z, so (x, z) ⊂I(Z(J)). We
will show the reverse containment I(Z(J)) ⊂(x, z) in two ways, so I(Z(J)) = (x, z).
Method 1. Write a polynomial g(x, y, z) as a polynomial in x and z whose coeﬃcients
are polynomials in y (that is, K[x, y, z] = K[y][x, z]). Say g = P
i,j cij(y)xizj (a ﬁnite sum)
where cij(y) ∈K[y]. The only term not divisible by x or z is the “constant term” c00(y).
For b ∈K, g(0, b, 0) = c00(b). Therefore if g(0, b, 0) = 0 for all b ∈K, c00(b) = 0 for all b.
That implies c00(y) = 0 since K is inﬁnite, so g(x, y, z) ∈(x, z).
Method 2. Since Z(I(J)) = Rad(J) (Nullstellensatz), we will show Rad(x2, xy, z2) ⊂
(x, z). If g ∈Rad(x2, xy, z2) then gm ∈(x2, xy, z2) ⊂(x, z) for some m ≥1. The ideal
(x, z) in K[x, y, z] is a prime ideal since K[x, y, z]/(x, z) ∼= K[y] is an integral domain, so
from gm ∈(x, z) we get g ∈(x, z).
The Nullstellensatz gives us a bijection between varieties in Kn and radical ideals in
K[x1, . . . , xn] if K is algebraically closed. This is called the variety–ideal correspondence.
Theorem 4.20. For algebraically closed ﬁelds K, the mappings V ⇝I(V ) and J ⇝Z(J)
between varieties in Kn and radical ideals in K[x1, . . . , xn] are inclusion-reversing bijections
that are inverses: Z(I(V )) = V for varieties V and I(Z(J)) = J for radical ideals J.
Proof. We have seen before that I(V ) is a radical ideal for each variety V , and Z(J) is a
variety in Kn by the deﬁnition of varieties. Since Z(J) = Z(Rad J), varieties have the form
Z(J) for radical ideals J. Therefore the mappings V ⇝I(V ) and J ⇝Z(J) pass from
varieties to radical ideals and conversely.
We saw before that these mappings are inclusion-reversing: V ⊂V ′ ⇒I(V ′) ⊂I(V ) and
J ⊂J′ ⇒Z(J′) ⊂Z(J). Theorem 4.4 tells us Z(I(V )) = V .
So far nothing we have mentioned requires K to be algebraically closed. The ﬁnal step,
that I(Z(J)) = J for radical ideals J, is the Nullstellensatz and here we rely on K being
algebraically closed.
□

<!-- page 15 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
15
Remark 4.21. When K is not algebraically closed, the mappings V ⇝I(V ) and J ⇝
Z(J) between varieties in Kn and radical ideals in K[x1, . . . , xn] make sense, are inclusion-
reversing, and Z(I(V )) = V for all V by Theorem 4.4, but J ̸= I(Z(J)) for some radical
ideals J.
For example, if f(x) ∈K[x] is irreducible with deg f > 1 (such f(x) exist
when K is not algebraically closed) then J := (f(x1)) in K[x1, . . . , xn] is prime since
f(x1) is irreducible in K[x1, . . . , xn] and Z(J) = ∅in Kn: if some (c1, . . . , cn) ∈Kn
is in Z(J) then f(c1) = 0, contradicting irreducibility of f(x1) since deg f > 1.
Thus
I(Z(J)) = I(∅) = K[x1, . . . , xn]. The ideal J is radical since J is prime, and J ̸= (1) since
f(x1) is nonconstant, so J ̸= I(Z(J)).
The variety–ideal correspondence in Theorem 4.20 has a striking similarity to the Ga-
lois correspondence between intermediate ﬁelds M in a ﬁnite Galois extension E/F and
subgroups H of Gal(E/F). Let’s examine this similarity further.
• The condition f(a) = 0 (for all f as a runs over V , or all a as f runs over J) is
analogous to the condition σ(α) = α (for all σ as α runs over M, or all α as σ runs
over H).
• The mappings between varieties in Kn and radical ideals in K[x1, . . . , xn] can be
deﬁned without assuming K is algebraically closed, and the two mappings in the
Galois correspondence can be deﬁned without assuming E/F is a Galois extension
(the group Aut(E/F) is ﬁnite when [E : F] is ﬁnite).
• Iterating the Z and I mappings from Theorem 4.20 in the order V ⇝I(V ) ⇝
Z(I(V )) returns us to the starting point V without assuming K is algebraically
closed (we have Z(I(V )) = V by Theorem 4.4), and iterating the Galois correspon-
dence in the order H ⇝EH ⇝Aut(E/EH) returns us to the starting point H
without assuming E/F is Galois (Aut(E/EH) = H by Artin’s theorem about ﬁnite
groups of automorphisms of a ﬁeld).
• The iterations J ⇝Z(J) ⇝I(Z(J)) and M ⇝Aut(E/M) ⇝MAut(E/M) lead to
containments: J ⊂I(Z(J)) and M ⊂MAut(E/M). Turning these containments into
equalities (J = I(Z(J)) for all J and M = MAut(E/M) for all M) genuinely needs
an extra assumption: to have I(Z(J)) = J for all radical ideals J in K[x1, . . . , xn]
requires K to be algebraically closed (there are always counterexamples when K
is not algebraically closed – see Remark 4.21) and to have MAut(E/M) = M for all
intermediate ﬁelds M in E/F requires E/F to be Galois (that EAut(E/F) = F is
equivalent to E/F being Galois).
From those comparisons, we assemble analogies in Table 1.
Variety–Ideal Correspondence
Galois Correspondence
K[x1, . . . , xn] for alg. closed K
Galois extension E/F
Varieties V in Kn
Subgroups H of Gal(E/F)
Kn (the biggest variety in Kn)
Gal(E/F) (the biggest subgroup)
Radical ideals J in K[x1, . . . , xn]
Intermediate ﬁelds M in E/F
V ⇝I(V ) = {f : f(a) = 0 for a ∈V }
H ⇝EH = {α : σ(α) = α for σ ∈H}
J ⇝Z(J) = {a : f(a) = 0 for f ∈J}
M ⇝Gal(E/M) = {σ : σ(α) = α for α ∈M}
Z(I(V )) = V (Theorem 4.4)
Gal(E/EH) = H (Artin’s theorem)
I(Z(J)) = J
MGal(E/M) = M
Table 1. Analogous correspondences
Remark 4.22. More examples of inclusion-reversing bijections between two partially or-
dered sets are (1) subspaces of a vector space V and its dual space V ∨(associate to W ⊂V

<!-- page 16 -->
16
KEITH CONRAD
all ϕ ∈V ∨such that ϕ(w) = 0 for all w ∈W, and to each subspace U of V ∨all w ∈V such
that ϕ(w) = 0 for all ϕ ∈U), (2) covering spaces and subgroups of a fundamental group,
(3) compact Riemann surfaces and ﬁnite extensions of C(z) (inside its algebraic closure).
We saw earlier that for an arbitrary subset S of K[x1, . . . , xn], Z(S) = Z(J) where
J = ⟨S⟩is the ideal generated by S. We can go further and replace J with Rad(J) without
changing the zero set in Kn, so Z(S) = Z(Rad(⟨S⟩)). This tells us how to write the zero set
of an arbitrary subset S of K[x1, . . . , xn] as the zero set of a radical ideal: use the radical
of the ideal generated by S.
Going the other way, if we start with an arbitrary subset X of Kn, then J := I(X)
is a radical ideal, so by the Nullstellensatz J = I(V ) for a unique variety V in Kn and
V = Z(J) = Z(I(X)). Thus each subset X of Kn leads to a variety V where X ⊂V and
the same polynomials in K[x1, . . . , xn] vanish on both X and V : I(X) = J = I(V ). How
is V “generated” from X? It is the smallest variety in Kn containing X. Indeed, if W is a
variety in Kn and X ⊂W then
X ⊂W =⇒I(W) ⊂I(X) = I(V ) =⇒Z(I(V )) ⊂Z(I(W)) =⇒V ⊂W,
where the last step is the Nullstellensatz. We can express this relation between V and X
using a topological language for subsets of Kn. The varieties in Kn satisfy the axioms of
closed sets for a topology: both Kn and ∅are varieties, and varieties in Kn are closed under
ﬁnite unions and arbitrary intersections since Z(J) ∪Z(J′) = Z(JJ′) and T
α Z(Jα) =
Z(P
α Jα).
For algebraically closed K, the topology on Kn whose closed sets are the
varieties in Kn is called the Zariski topology on Kn. It was introduced by Zariski [9] in
1944. Open sets for the Zariski topology are the complements in Kn of varieties.9 That V
is the smallest variety in Kn containing X is saying V is the Zariski closure of X: V = X
in the Zariski topology on Kn. That is analogous to [0, 1] being created from (0, 1) in R by
passing to the closure in the usual Euclidean topology on R.
Example 4.23. A polynomial f(x) in K[x] deﬁnes a continuous function K →K using the
Zariski topology since the inverse image of closed sets are closed: obviously f−1(K) = K,
and if {a1, . . . , am} is a ﬁnite subset of K then its inverse image f−1(a1) ∪· · · ∪f−1(am) in
K is ﬁnite if f ̸= 0 and is K is f = 0 since polynomial equations f(x) = ai have ﬁnitely
many solutions in K when f ̸= 0. Let’s compute a Zariski closure (closure of a subset in
the Zariski topology). If X is an inﬁnite subset of K then X = K in the Zariski topology
since the varieties in K are ∅, K, and ﬁnite subsets10: the only variety in K containing an
inﬁnite subset is K. This means each inﬁnite subset of K is a dense subset in the Zariski
topology on K. If that sounds weird, it is just a topological expression of the familiar fact
that polynomials in K[x] are determined by their values on an inﬁnite subset of K: if f(x)
and g(x) in K[x] are equal on an inﬁnite subset of K then f(x) −g(x) has inﬁnitely many
roots, so f(x) −g(x) = 0 in K[x]. This says that if f(a) = g(a) for inﬁnitely many a ∈K
then f(a) = g(a) for all a ∈K; doesn’t that make an inﬁnite subset of K look “dense” for
a topology on K when polynomials in K[x] are continuous for that topology on K?
Putting a topology on Kn, like the Zariski topology, is extremely important in algebraic
geometry (not so much for taking limits as in calculus, but for topological constructions
like sheaves) and this is another example of the analogy with the Galois correspondence.
9Here we will not use the Zariski topology on Kn when K is not algebraically closed. Algebraic geometry
over non-algebraically closed ﬁelds requires a reconsideration of what a variety should be, analogous to the
contrast between Theorems 3.1(2) and 3.4.
10For n ≥2, the Zariski topology on Kn is not the product topology: the diagonal {(c, c) : c ∈K} =
Z(y −x) is closed in the Zariski topology on K2 but not in the product topology of the Zariski topologies
on the two axes.

<!-- page 17 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
17
We said above that varieties in Kn are analogous to subgroups of a Galois group. When
Galois theory is generalized to inﬁnite algebraic ﬁeld extensions, it is important to put
a topology on the inﬁnite Galois group, called the Krull topology. (The Krull topology
on ﬁnite Galois groups is discrete, and thus of no interest.) The subgroups of the Galois
group that are relevant to the Galois correspondence for inﬁnite-degree extensions are the
subgroups that are closed in the Krull topology, which is analogous to the varieties in Kn
being (by deﬁnition) the closed subsets of Kn for the Zariski topology. The Krull topology
on an inﬁnite Galois group makes the Galois group compact, and Kn in the Zariski topology
is also compact, a property related to ideals in K[x1, . . . , xn] being ﬁnitely generated.
We assumed K is algebraically closed to show the maximal ideals in K[x1, . . . , xn] have an
especially simple form, to prove the weak Nullstellensatz, and to prove the Nullstellensatz.
In fact, all of these properties of a ﬁeld K are equivalent.
Theorem 4.24. Fix an integer n ≥1. For a ﬁeld K, the following properties are equivalent.
(1) K is algebraically closed.
(2) Each maximal ideal in K[x1, . . . , xn] is (x1 −c1, . . . , xn −cn) for some ci ∈K.
(3) (Weak Nulllstellensatz) For each proper ideal J in K[x1, . . . , xn], Z(J) ̸= ∅.
(4) (Nullstellensatz) For each ideal J in K[x1, . . . , xn], I(Z(J)) = Rad J.
Proof. (1) ⇒(2): see the proof of Theorem 3.1.
(2) ⇒(3): see the proof of the weak Nullstellensatz (Theorem 4.6), which is based on
the description of maximal ideals in K[x1, . . . , xn] rather than an explicit assumption of K
being algebraically closed.
(3) ⇒(4): see the proof of Theorem 4.17, which depends only the weak Nullstellensatz.
(4) ⇒(1): The contrapositive is proved (by example) in Remark 4.21: if K is not
algebraically closed then there is a radical (in fact prime) ideal J in K[x1, . . . , xn] such that
I(Z(J)) ̸= J.
□
5. Maximal and prime ideals in Z[x]
We now switch our attention to a polynomial ring over Z: what are the maximal ideals
in Z[x]? We will ﬁrst prove a result analogous to Zariski’s lemma (Theorem 2.11) for all
ﬁnitely generated Z-algebras (rings of the form Z[α1, . . . , αn], even if the subring generated
by 1 is Z/mZ rather than Z). We’ll apply the result to Z[x] in order to describe its maximal
ideals and then its prime ideals.
Theorem 5.1. If L is a ﬁeld that is a ﬁnitely generated Z-algebra then L is a ﬁnite ﬁeld.
Proof. Since L is a ﬁnitely generated Z-algebra, L = Z[α1, . . . , αn] for some α1, . . . , αn in
L. The (unique) ring homomorphism Z →L has kernel that is a prime ideal in Z (subrings
of L are integral domains), so the kernel is (0) or pZ for prime p.
Case 1: The kernel of Z →L is pZ. Then L has characteristic p, so L = Fp[α1. . . . , αn].
This shows L is a ﬁeld that is a ﬁnitely generated algebra over the ﬁeld Fp, so by Zariski’s
lemma, L is a ﬁnite extension of Fp and thus L is ﬁnite.
Case 2: The kernel of Z →L is (0). Then L has characteristic 0, so Z ⊂L and thus
Q ⊂L (since L is a ﬁeld). We will show this case is impossible.
Since L is a ﬁeld,
L = Z[α1, . . . , αn] ⊂Q[α1, . . . , αn] ⊂L,
so L = Q[α1, . . . , αn]. Thus L is a ﬁnitely generated Q-algebra that is a ﬁeld, so L/Q is a
ﬁnite extension by Zariski’s lemma. Therefore each αi is algebraic over Q: αi is the root of
a monic (irreducible) fi(x) ∈Q[x].

<!-- page 18 -->
18
KEITH CONRAD
Let d in Z+ be a common denominator of the coeﬃcients of f1(x), . . . , fn(x), so each
fi(x) is monic in Z[1/d][x]. Therefore each αi is integral over Z[1/d] for i = 1, . . . , n. From
L = Z[α1, . . . , αn] ⊂Z[1/d][α1, . . . , αn] ⊂L
we have L = Z[1/d][α1, . . . , αn], so L is integral over Z[1/d] (Corollary 2.10). Since L is a
ﬁeld, Z[1/d] must be a ﬁeld (Theorem 2.7), so Z[1/d] = Q. This is impossible: pick a prime
p that doesn’t divide d, so 1/p ∈Q but 1/p ̸∈Z[1/d]. Thus Case 2 can’t occur.
□
Note the similarity between the way a contradiction is reached at the end of Case 2 and
at the end of the proof of Zariski’s lemma: we can’t have Q = Z[1/d] for a positive integer
d and for ﬁelds K we can’t have K(t) = K[t][1/d(t)] for a monic d(t) ∈K[t].
Corollary 5.2. If R is a nonzero ring that is a ﬁnitely generated Z-algebra then R/m is a
ﬁnite ﬁeld for every maximal ideal m of R. In particular, every maximal ideal of R is the
kernel of a ring homomorphism from R onto a ﬁnite ﬁeld.
Proof. Since R is a ﬁnitely generated Z-algebra, R = Z[α1, . . . , αn] for some α1, . . . , αn in
R. The quotient ring R/m is Z[α1, . . . , αn], where αi = αi mod m, so R/m is a ﬁeld that is
a ﬁnitely generated Z-algebra. By Theorem 5.1, R/m is ﬁnite.
Since R/m is ﬁnite, m is the kernel of reduction R →R/m, which is a ring homomorphism
from R onto a ﬁnite ﬁeld.
□
Theorem 5.3. Here is a classiﬁcation of maximal ideals in Z[x].
(1) For a prime p and monic f(x) ∈Z[x] such that f(x) mod p is irreducible in Fp[x],
the ideal (p, f(x)) in Z[x] is maximal.
(2) For two maximal ideals (p, f(x)) and (q, g(x)) in Z[x] in the form described in (1),
we have (p, f(x)) = (q, g(x)) if and only if p = q and f(x) = g(x) in Fp[x].
(3) All maximal ideals in Z[x] arise in the above way. In particular, maximal ideals in
Z[x] have prime-power index, and for each prime power pd the number of maximal
ideals in Z[x] with index pd is the number of monic irreducibles of degree d in Fp[x].
For example the maximal ideals in Z[x] with prime index p are (p, x−a) for 0 ≤a ≤p−1,
the maximal ideals with index 8 are (2, x3 + x + 1) and (2, x3 + x2 + 1), and the maximal
ideals with index 9 are (3, x2 + 1), (3, x2 + x + 2), and (3, x2 + 2x + 2).
Proof. (1) If p is prime and f(x) ∈Z[x] is monic such that f(x) := f(x) mod p is irreducible
in Fp[x] then Z[x]/(p, f(x)) ∼= Fp[x]/(f(x)), which is a ﬁeld since the ideal generated by an
irreducible in Fp[x] is maximal. Thus (p, f(x)) is a maximal ideal in Z[x].
(2) Suppose (p, f(x)) = (q, g(x)), where f(x) and g(x) are monic in Z[x] with f(x) mod p
irreducible in Fp[x] and g(x) mod q irreducible in Fq[x]. Necessarily p = q since a proper
ideal in Z[x] can’t contain two diﬀerent primes (otherwise it contains 1, which is a con-
tradiction). If f(x) ̸= g(x) in Fp[x] then some Fp[x]-linear combination of f(x) and g(x)
is 1 (diﬀerent monic irreducibles in Fp[x] generate the unit ideal in Fp[x]).
Therefore
f(x)u(x) + g(x)v(x) = 1 + ph(x) for some u(x), v(x), h(x) ∈Z[x]. Since f(x), g(x), and p
are all in (p, f(x)), we get 1 = fu + gv −ph ∈(p, f(x)), which contradicts (p, f(x)) being a
proper ideal. Therefore f(x) = g(x) in Fp[x].
Conversely, if p = q and f(x) = g(x) in Fp[x] then g(x) ∈(p, f(x)), so (p, g(x)) ⊂
(p, f(x)), which implies (p, g(x)) = (p, f(x)) since both ideals are maximal in Z[x].
(3) Let M be a maximal ideal in Z[x]. We want to prove M = (p, f(x)) for a prime p and
monic f(x) ∈Z[x] such that f(x) mod p is irreducible in Fp[x]. By Corollary 5.2, Z[x]/M
is a ﬁnite ﬁeld, so it has positive characteristic: p = 0 in Z[x]/M, for a prime p, so p ∈M.

<!-- page 19 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
19
Since M contains p, the surjective reduction homomorphism Z[x] →Z[x]/M kills p and
thus it induces a surjective ring homomorphism Z[x]/(p) →Z[x]/M, or equivalently
ϕ: Fp[x] →Z[x]/M.
The kernel of this surjective homomorphism ϕ has to be a maximal ideal in Fp[x], so it
is (π(x)) for some monic irreducible π(x) in Fp[x]. Let f(x) be a monic lifting of π(x)
to Z[x]: f(x) is monic and π(x) = f(x) in Fp[x]. That ϕ(π(x)) = 0 in Z[x]/M implies
f(x) ≡0 mod M, so f(x) ∈M in Z[x]. Thus (p, f(x)) ⊂M. The ideal (p, f(x)) is maximal
by part (1) since f(x) mod p is irreducible in Fp[x], so the containment (p, f(x)) ⊂M
implies M = (p, f(x)).
□
The most important step in the proof of part (3) is that M ∩Z contains a prime number.
Our proof of that relies on Corollary 5.2, which depends on Theorem 5.1, which depends
on Zariski’s lemma. It’s reasonable to ask if we can prove M ∩Z contains a prime number
without having to prove Zariski’s lemma ﬁrst. Since M ∩Z is a prime ideal in Z, M ∩Z is
(0) or pZ for a prime p. Here is a proof of M ∩Z ̸= (0) that doesn’t depend on Zariski’s
lemma, but it has common features with the proof we gave of Zariski’s lemma.
We argue by contradiction. Assume M ∩Z = (0). The natural composite homomorphism
Z →Z[x] →Z[x]/M has kernel M ∩Z, which is (0), so the map is injective. Thus Z is a
subring of Z[x]/M. Set
F = Z[x]/M,
α = x mod M.
Then F = Z[x] = Z[α] as a ring. Since F is a ﬁeld (it’s a ring modulo a maximal ideal)
and it contains Z, F also contains Q. Deﬁne a ring homomorphism ϕ: Q[y] →F to be
evaluation a α: ϕ(f(y)) = f(α) for all f(y) ∈Q[y].
Since Z ⊂Q ⊂F and F is generated as a ring by Z and α, F is generated as a ring by
Q and α:
(5.1)
F = Z[α] = Q[α].
(This should already seem weird!) The map ϕ: Q[y] →F is onto since F = Q[α]. Since
F is a ﬁeld, ker ϕ is a maximal ideal in Q[y], so ker ϕ = (π(y)) for a monic irreducible
π(y) ∈Q[y]. That π(y) ∈ker ϕ implies 0 = ϕ(π(y)) = π(α) in F.
Let d ∈Z+ be a common denominator of the coeﬃcients of π(y), so π(y) is monic with
coeﬃcients in Z[1/d]. Thus the equation π(α) = 0 tells us α is integral over the ring Z[1/d].
Since Z ⊂Z[1/d] ⊂Q, (5.1) implies F = Z[1/d][α]. Since α is integral over Z[1/d], F is
an integral extension of Z[1/d] (Corollary 2.10). Since F is a ﬁeld, Z[1/d] is also a ﬁeld
(Theorem 2.7), That tells us Q = Z[1/d], which is impossible: for a prime p not dividing d,
1/p ∈Q but 1/p ̸∈Z[1/d].11 Thus M ∩Z ̸= (0).
Remark 5.4. This argument carries over to the case of R[x] where R is a PID with inﬁnitely
many nonassociate prime elements. For each maximal ideal M of R[x], M ∩R ̸= (0), so
M ∩R = (p) for a prime element p in R. Then the reasoning in the proof of Theorem 5.3(3)
shows M = (p, f(x)) where p is prime in R and f(x) ∈R[x] is monic such that f(x) mod p
is irreducible in (R/p)[x]. For example, this applies to R = K[y] where K is a ﬁeld, so each
maximal ideal in K[x, y] is (p(y), f(x, y)) where p(y) is irreducible in K[y] and f(x, y) is
monic in x and f(x, y) mod p(y) is irreducible in (K[y]/p(y))[x].
For an algebraically closed ﬁeld K, polynomials in K[x1, . . . , xn] generate the unit ideal if
and only if they have no common zero in Kn: “only if” is easy, and “if” is the contrapositive
of the weak Nullstellensatz. The next theorem gives an analogue of this in Z[x1, . . . , xn],
explaining when polynomials generate the unit ideal in terms of having no common zeros
over ﬁnite ﬁelds.
11Note the similarity to the end of the proof of Zariski’s lemma.

<!-- page 20 -->
20
KEITH CONRAD
Theorem 5.5. Let f1, . . . , fr be polynomials in Z[x1, . . . , xn]. The following conditions are
equivalent.
(1) (f1, . . . , fr) = (1) in Z[x1, . . . , xn].
(2) For every prime p, the reductions f1, . . . , fr in Fp[x1, . . . , xn] have no common zero
in F
n
p .
(3) For every prime p, the reductions f1, . . . , fr in Fp[x1, . . . , xn] have no common zero
in each ﬁnite extension of Fp.
Proof. (1) ⇒(2): If f1g1 + · · · + frgr = 1 in Z[x1, . . . , xn] then f1g1 + . . . + frgr = 1 in
Fp[x1, . . . , xn] for each prime p, so there is no common zero of the reductions fi in F
n
p .
(2) ⇒(3): Every element of Fp is in some ﬁnite extension of Fp, so every point in F
n
p is
in Fn for some ﬁnite extension F of Fp. So if f1, . . . , fr in Fp[x1, . . . , xn] have no common
zero in F
n
p , they have no common zero in Fn for each ﬁnite extension F of Fp (all ﬁnite
extensions of Fp are in Fp).
(3) ⇒(1): We will prove the contrapositive. If (f1, . . . , fr) ̸= (1) then we will show there
is a prime p and ﬁnite extension F of Fp such that f1, . . . , fr have a common zero in F n.
Since (f1, . . . , fr) ̸= (1) there is a maximal ideal m in Z[x1, . . . , xn] such that (f1, . . . , fr) ⊂
m. By Corollary 5.2, m is the kernel of a homomorphism ϕ from Z[x1, . . . , xn] onto a ﬁnite
ﬁeld F. Let p be the characteristic of F, so F is a ﬁnite extension of Fp. Set αi = ϕ(xi), so
(α1, . . . , αn) ∈Fn and for each f ∈Z[x1, . . . , xn],
ϕ(f(x1, . . . , xn)) = f(ϕ(x1), . . . , ϕ(xn)) = f(α1, . . . , αn) ∈F,
where f has the integral coeﬃcients of f reduced mod p (so the coeﬃcients are in Fp,
a subﬁeld of F). Thus ϕ is evaluation at (α1, . . . , αn), and the fact that (f1, . . . , fr) ⊂
m = ker(ϕ), tells us fi(α1, . . . , αn) = 0 in F for all i, so the polynomials f1, . . . , fn in
Fp[x1, . . . , xn] have the common zero (α1, . . . , αn) in Fn.
□
Example 5.6. Let f(x) = x4 −2 and g(x) = x3 + x + 5. They are relatively prime in Q[x],
so a Q[x]-linear combination is 1. Such a relation can be found with Euclid’s algorithm,
and after clearing the denominator it is
(8x2 −5x + 17)f(x) −(8x3 −5x2 + 9x −35)g(x) = 141 = 3 · 47
in Z[x]. So there is no common zero of f(x) mod p and g(x) mod p in Fp when p ̸= 3 or
47. In F3[x], f(x) = (x2 + x + 2)(x2 + 2x + 2) and g(x) = (x + 1)(x2 + 2x + 2), so f(x)
and g(x) have a common root in F9 (a root of x2 + 2x + 2 in characteristic 3). In F47[x],
f(x) = (x −17)(x −30)(x2 + 7) and g(x) = (x −17)(x2 + 17x + 8), so f(x) and g(x) have
the common root 17 in F47. Therefore the only maximal ideals in Z[x] containing f(x) and
g(x) are (3, x2 +2x+2) and (47, x−17). The ideals (f(x)) and (g(x)) in Z[x] are analogous
to curves in the plane, and saying the ideal (f(x), g(x)) lies in two maximal ideals is like
saying a pair of curves intersects in two points.
Example 5.7. In Z[x, y], let f(x, y) = x2 +y2, g(x, y) = x3 +y3, and h(x, y) = x(y+1)+1.
We’ll show the only p for which f = 0, g = 0, and h = 0 have a common solution in F
2
p is
p = 2, and the common solution is a point with coordinates in F4 (not F2).
Suppose in a ﬁeld of characteristic p that a2 + b2 = 0, a3 + b3 = 0, and a(b + 1) + 1 = 0.
The third equation shows a is not 0, and the ﬁrst or second equation then shows b is not 0.
Then (b/a)2 = −1 and (b/a)3 = −1. Taking ratios implies b/a = 1, so a = b. That turns
the three original equations into 2a2 = 0, 2a3 = 0, and a2 + a + 1 = 0. Since a is not 0,
we need 2 = 0 in the ﬁeld, so p = 2. Conversely, if a2 + a + 1 = 0 in characteristic 2 then
f(a, a) = 0, g(a, a) = 0, and h(a, a) = 0.

<!-- page 21 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
21
These calculations show the ideal (f, g, h) in Z[x, y] is contained in the maximal ideal
(2, x2 + x + 1, y −x), so (f, g, h) ̸= (1). Moreover, we showed (f, g, h) is contained in no
other maximal ideal of Z[x, y].
The description of maximal ideals in Z[x] extends to a description of prime ideals in Z[x].
Theorem 5.8. Here are the prime ideals p in Z[x] and their quotient rings Z[x]/p.
(i) p = (0), with quotient ring Z[x].
(ii) p = (p) for a prime number p with quotient ring Fp[x].
(iii) p = (π(x)) for nonconstant irreducible π(x) in Z[x] with quotient ring Z[α], where
π(α) = 0.
(iv) p = (p, f(x)) for a prime number p and monic f(x) ∈Z[x] such that f(x) mod p is
irreducible in Fp[x], with quotient ring the ﬁnite ﬁeld Fp[x]/(f(x)).
Example 5.9. Prime ideals of type (iii) include (2x−1) with quotient ring Z[1/2], (x2 +1)
with quotient ring Z[i], and (3x2 −10x + 1) with quotient ring Z[(5 +
√
22)/3].
Proof. The intersection p ∩Z is a prime ideal in Z, so it is (0) or pZ for a prime number p.
Case 1: p ∩Z = pZ for a prime p. Such p correspond under the reduction map Z[x] →
Z[x]/(p) to prime ideals in Z[x]/(p) ∼= Fp[x]. All p of types (ii) and (iv) occur this way.
The prime ideals in Fp[x] are (0) and maximal ideals (f(x)) where f(x) ∈Z[x] is monic
with f(x) := f(x) mod p being irreducible in Fp[x]. Lifting these back into Z[x], we get
the prime ideal (p) = pZ[x] and the maximal ideal (p, f(x)), with respective quotient rings
Fp[x] and Fp[x]/(f(x)).
Case 2: p∩Z = (0). All p of type (i) and (iii) occur this way. Henceforth suppose p ̸= (0).
Pick a nonzero element of p. It is not ±1, so it has an irreducible factorization in Z[x] and
thus an irreducible factor π(x) is in p. The polynomial π(x) is nonconstant since p∩Z = (0).
We will show p = (π(x)).
Since π(x) ∈p, (π(x)) ⊂p . To show p ⊂(π(x)), assume some g(x) ∈p is not divisible
by π(x). Then a nonconstant irreducible factor of g(x) is in p, say eπ(x). So π(x) and eπ(x)
are two nonconstant irreducible polynomials in p, and eπ(x) ̸= ±π(x) since π(x) ∤g(x).
At this point we bring in a description of the nonconstant irreducibles in Z[x]: they are
precisely the primitive polynomials in Z[x] (gcd of coeﬃcients is 1) that are irreducible in
Q[x]. Thus π(x) and eπ(x) are irreducible in Q[x] and are not constant multiples of each
other in Q[x] (since they are primitive and not equal up to sign). Thus π(x) and eπ(x) are
relatively prime irreducibles in Q[x], so π(x)u(x) + eπ(x)v(x) = 1 where u(x) and v(x) are
in Q[x]. Clearing denominators, π(x)a(x) + eπ(x)b(x) = c where a(x) and b(x) are in Z[x]
and c is a nonzero integer. Since π(x) and eπ(x) are in p we get c ∈p, which contradicts the
assumption that p ∩Z = (0). Thus p ⊂(π(x)), so p = (π(x)).
It remains to show for each nonconstant irreducible π(x) in Z[x] that the ideal (π(x)) in
Z[x] is a prime ideal and to compute the quotient ring Z[x]/(π(x)). Since Z[x] has unique
factorization, if π(x) | g(x)h(x) in Z[x] then π(x) | g(x) or π(x) | h(x), so (π(x)) is a prime
ideal in Z[x]. (It is not a maximal ideal because (π(x)) ∩Z = (0) and we saw in Theorem
5.3 that every maximal ideal in Z[x] contains a prime number.)
Let α be a root of π(x) in a ﬁeld extension of Q. Evaluation at α is a surjective ring
homomorphism Z[x] →Z[α]. We will show the kernel is (π(x)): if f(x) ∈Z[x] and f(α) = 0
then π(x) | f(x) in Z[x] (the converse is obvious). Since π(x) is irreducible in Q[x] and Q
is a ﬁeld, if f(x) ∈Z[x] and f(α) = 0 then π(x) | f(x) in Q[x]: f(x) = π(x)g(x) where
g(x) ∈Q[x]. Let c be a common denominator of the coeﬃcients of g(x): g(x) = G(x)/c
where G(x) ∈Z[x], so cf(x) = π(x)G(x) in Z[x]. Therefore π(x) | cf(x) in Z[x], and π(x)
is not constant, so unique factorization in Z[x] implies π(x) | f(x) in Z[x].
□

<!-- page 22 -->
22
KEITH CONRAD
The nonzero non-maximal prime ideals (p) and (π(x)) in Z[x] (as p and π(x) vary) have
no containment relations among them, so the possible chains of prime ideals in Z[x] are
(0) ⊂(p) ⊂m,
(0) ⊂(π(x)) ⊂m
for maximal ideals m. The m containing (p) have the form (p, f(x)) where p is prime and
f(x) mod p is irreducible, The m containing (π(x)) have the form (p, f(x)) where p is prime,
f(x) mod p is irreducible, and the image of π(x) in Fp[x]/(f(x)) is 0; this is equivalent
to f(x) | π(x) in Fp[x], so f(x) is an irreducible factor of π(x) in Fp[x]. Describing the
maximal ideals in Z[x] containing (π(x)) amounts to describing the irreducible factorization
of π(x) mod p in Fp[x] for each prime p.
Example 5.10. The maximal ideals in Z[x] containing (2x −1) are all (p, 2x −1) where p
is an odd prime.
Example 5.11. The maximal ideals in Z[x] containing (x2 + 1) are all (p, f(x)) where
f(x) | (x2 + 1) in Fp[x].
We take cases depending on the irreducible factorization of
x2 + 1 mod p and there are three possibilities:
• (2, x + 1),
• (p, x −r) and (p, x + r) where p ≡1 mod 4 and r2 ≡−1 mod p,
• (p, x2 + 1) where p ≡3 mod 4.
Pictures of all the prime ideals of Z[x] are famous in algebraic geometry, and can be
found at https://pbelmans.ncag.info/blog/atlas/.
Appendix A. Nullstellensatz for non-algebraically closed fields
In this appendix we extend the Nullstellensatz from algebraically closed ﬁelds to arbitrary
ﬁelds. For a ﬁeld K, let C/K be an algebraically closed extension (e.g., C = K). This will
be ﬁxed throughout our discussion. We will obtain a bijection between the radical ideals in
K[x1, . . . , xn] and the varieties in Cn “deﬁned over K”, which means being the zero set of
polynomials with coeﬃcients in K.
Deﬁnition A.1. A K-variety in Cn is the zero set in Cn of a subset S of K[x1, . . . , xn]:
ZCn(S) = {a ∈Cn : f(a) = 0 for all f ∈S}.
Replacing S with the ideal ⟨S⟩or with the radical of the ideal ⟨S⟩does not change the
zero set, so we can always suppose a K-variety in Cn is the zero set in Cn of a ﬁnite set of
polynomials in K[x1, . . . , xn] (ideals in this ring are ﬁnitely generated).
Example A.2. The polynomial x2 + y2 + 1 deﬁnes an R-variety in C2:
ZC2(x2 + y2 + 1) = {(z.w) ∈C2 : z2 + w2 + 1 = 0}.
This R-variety in C2 has no solutions in R2, but it has many complex solutions.
Deﬁnition A.3. For each K-variety V ⊂Cn, set
IK(V ) = {f ∈K[x1, . . . , xn] : f(a) = 0 for all a ∈V }.
This is a radical ideal in K[x1, . . . , xn].
Theorem A.4. For K-varieties V in Cn, ZCn(IK(V )) = V .
This is a generalization of Theorem 4.4 and the proof will be the same except for some
more care about polynomials having coeﬃcients in K rather than C.

<!-- page 23 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
23
Proof. It’s easy to see that V ⊂ZCn(IK(V )).
To show the reverse containment, write
V = ZCn(J) for a radical ideal J in K[x1, . . . , xn]. (This is how we use the condition that
V is a K-variety.) Then J ⊂IK(V ) = IK(ZCn(J)). For a ∈ZCn(IK(V )) and f ∈IK(V ),
f(a) = 0. In particular, for a ∈ZCn(IK(V )) and f ∈J, f(a) = 0. Thus a ∈ZCn(J) = V ,
so ZCn(IK(V )) ⊂V .
□
Here is a generalization of Theorem 4.5.
Theorem A.5. For a K-variety V in Cn, IK(V ) is a maximal ideal in K[x1, . . . , xn] if
and only if V is the Aut(C/K)-orbit of a point in K
n, which is the same thing as an
Aut(K/K)-orbit of a point in K
n.
Proof. First we address the relation between an Aut(C/K)-orbit and Aut(K/K)-orbit of a
point in K
n, which is contained in Cn. For a point a in K
n and σ ∈Aut(C/K), σ maps each
coordinate of a to an element of K since σ preserves algebraic relations over K. Thus the
Aut(C/K)-orbit of a is inside K
n and it is the Aut(K/K)-orbit of a since the restriction
mapping Aut(C/K) →Aut(K/K) is surjective by Zorn’s lemma (every K-isomorphism
K →K extends to a K-isomorphism C →C).
Let V be the Aut(C/K)-orbit of some a ∈K
n. Evaluation at a is a K-algebra homo-
morphism K[x1, . . . , xn] →K and its kernel m (a maximal ideal: why?) contains each
f ∈IK(V ). Thus IK(V ) ⊂m. Conversely, if f ∈m then f(a) = 0, so for all σ ∈Aut(C/K),
0 = σ(f(a)) = f(σ(a))
since f has coeﬃcients in K. Thus m ⊂IK(V ), so IK(V ) = m.
Now let IK(V ) be a maximal ideal in K[x1, . . . , xn]. Then IK(V ) is the kernel of an
evaluation homomorphism K[x1, . . . , xn] →K at some point a ∈K
n by Theorem 3.4, so
the polynomials in IK(V ) are polynomials in K[x1, . . . , xn] that vanish at a. Since V is a
K-variety, Theorem A.4 tells us
(A.1)
V = ZCn(IK(V )) = {b ∈Cn : f(b) = 0 when f(a) = 0}.
We want to show each b in V has coordinates in K and b = σ(a) for some σ ∈Aut(K/K).
Write a = (a1, . . . , an) and b = (b1, . . . , bn). Let ai have minimal polynomial πi(x) ∈
K[x]. Then πi(ai) = 0, so πi(xi) is in IK(V ) for i = 1, . . . , n. Since b ∈V , πi(bi) = 0 by
(A.1). Thus the coordinates of b are all in K, so b ∈K
n and (A.1) says
ma ∩K[x1, . . . , xn] ⊂mb ∩K[x1, . . . , xn].
Both intersections are maximal ideals by Theorem 3.4, so the containment is an equality
and b = σ(a) for some σ ∈Aut(K/K).
□
Comparing Theorem A.5 to Theorem 4.5 suggests that a “K-point of K
n” should be an
Aut(K/K)-orbit of a point in K
n. When K is algebraically closed, so K = K, this is the
classical notion of a point in Kn since Aut(K/K) is trivial.
Example A.6. Returning to Example A.2, the R-variety
ZC2(x2 + y2 + 1) = {(z.w) ∈C2 : z2 + w2 + 1 = 0}
has no classical real points. Pairs of complex-conjugate points, such as {(i, 0), (−i, 0)}, are
the R-points (of “degree 2” since it is a set of 2 related complex solutions).
Lemma A.7. For a ﬁeld extension L/K, let {eβ}β∈B be a K-basis: L = L
β∈B Keβ. Then
L[x1, . . . , xn] is a free K[x1, . . . , xn]-module with basis {eβ}β∈B.
For example, C[x, y] = R[x, y] + iR[x, y]. If that seems obvious then you understand
what the lemma is saying, except in general [L : K] could be inﬁnite (e.g., K = Q and
L = Q or L = C).

<!-- page 24 -->
24
KEITH CONRAD
Proof. The set {eβ} is a K[x1, . . . , xn]-linear spanning set of L[x1, . . . , xn].
Since each el-
ement of L is a ﬁnite K-linear combination of elements in {eβ} and each polynomial
f ∈L[x1, . . . , xn] have ﬁnitely many coeﬃcients, writing each of the coeﬃcients of f in
terms of the K-basis of L and then collecting monomials from K[x1, . . . , xn] that are mul-
tiplied by the same eβ shows f is a K[x1, . . . , xn]-linear combination of {eβ}.
K[x1, . . . , xn]-linear independence of {eβ}. Assume P
β∈B gβeβ = 0, where the sum has
ﬁnitely many terms gβ ∈K[x1, . . . , xn]. Because there are ﬁnitely many terms, there is an
upper bound on degrees of monomials appearing in each gβ, say degree d: gβ = P
|j|≤d aβjxj
where j = (j1, . . . , jj) is an n-tuple, xj = xj1
1 . . . xjn
n , and aβj ∈K. Then in L[x1, . . . , xn],
0 =
X
β∈B
gβeβ =
X
|j|≤d

X
β
aβjeβ

xj,
so by the meaning of equality in L[x1, . . . , xn] we get P
β aβjeβ = 0 for each j. Therefore
by K-linear independence of {eβ}, aβj = 0 for all β and j. Thus each gβ is 0.
□
Theorem A.8. For an ideal J in K[x1, . . . , xn] and ﬁeld extension L/K, if the extended
ideal JL[x1, . . . , xn] in L[x1, . . . , xn] equals L[x1, . . . , xn] then J = K[x1, . . . , xn].
Proof. Let {eβ}β∈B be a K-basis and we may assume 1 is an element of this basis, say
1 = eβ0. The ideal JL[x1, . . . , xn] consists of ﬁnite sums of products of elements in J times
elements in L[x1, . . . , xn]. Since L[x1, . . . , xn] has K[x1, . . . , xn]-basis {eβ}β∈B by Lemma
A.7 and JK[x1, . . . , xn] ⊂J, we have
JL[x1, . . . , xn] =
M
β∈B
Jeβ.
If JL[x1, . . . , xn] = L[x1, . . . , xn] then 1 ∈JL[x1, . . . , xn], so 1 = P
β∈B gβeβ (a ﬁnite
sum) where gβ ∈J.
From the coeﬃcient of eβ0 on both sides, 1 = gβ0 ∈J.
So J =
K[x1, . . . , xn].
□
Theorem A.9 (Weak Nullstellensatz over K). If J is a proper ideal in K[x1, . . . , xn] then
ZCn(J) ̸= ∅in Cn.
Proof. Since J ̸= (1) in K[x1, . . . , xn], JC[x1, . . . , xn] ̸= (1) in C[x1, . . . , xn] by Theorem
A.8. Thus JC[x1, . . . , xn] ⊂m for a maximal ideal m in C[x1, . . . , xn], so J ⊂m. Since C is
algebraically closed, m = (x1 −c1, . . . , xn −cn) for c1, . . . , cn ∈C, so (c1, . . . , cn) ∈ZCn(J).
Thus ZCn(J) ̸= ∅.
□
Corollary A.10. Let K be a ﬁeld and f1, . . . , fr ∈K[x1, . . . , xn]. The following conditions
are equivalent.
(1) The system of polynomial equations f1 = 0, . . . , fr = 0 has no solution in Cn.
(2) (f1, . . . , fr) = (1) in K[x1, . . . , xn].
The key point in the second condition is that the ideal generated by the fi in K[x1, . . . , xn]
is the unit ideal, not just the ideal generated by the fi in C[x1, . . . , xn].
Proof. It is obvious that the second condition implies the ﬁrst condition.
To show the
ﬁrst condition implies the second condition, set J = (f1, . . . , fr) in K[x1, . . . , xr]. The ﬁrst
condition says ZCn(J) = ∅, so Theorem A.9 tells us that J = (1): f1g1 + · · · + frgr = 1 for
some gi ∈K[x1, . . . , xn].
□
For example, if f1, . . . , fr ∈Q[x1, . . . , xn], then in order for the system of equations
f1 = 0, . . . , fr = 0 not to have a solution in Cn or Q
n, it is necessary and suﬃcient that
f1g1 + · · · + frgr = 1 for some gi ∈Q[x1, . . . , xn].

<!-- page 25 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
25
Theorem A.11 (Nullstellensatz over K). For each ideal J in K[x1, . . . , xn], IK(ZCn(J)) =
Rad J.
We can write J = (f1, . . . , fr) since ideals in K[x1, . . . , xn] are ﬁnitely generated. The
more interesting containment IK(ZCn(J)) ⊂Rad J says that if g ∈K[x1, . . . , xn] vanishes
on Cn (not just on Kn!) wherever f1, . . . , fr all vanish, then gm ∈J for some m ≥1. For
example, if f1, . . . , fr, g ∈Q[x1, . . . , xn] and f1(z) = . . . , = fr(z) = 0 ⇒g(z) = 0 for all
z ∈Cn, then gm ∈(f1, . . . , fr) in Q[x1, . . . , xn] for some m ≥1.
Proof. It is easy to check that Rad J ⊂IK(ZCn(J)). We will show IK(ZCn(J)) ⊂Rad J by
the Rabinowitsch trick.
The ideal J can be written as (f1, . . . , fr). For g ∈IK(ZCn(J)) such that g ̸= 0, deﬁne
an ideal in K[x1, . . . , xn, xn+1]:
J′ := (f1, . . . , fr, xn+1g −1)
Because g vanishes on Cn wherever f1, . . . , fr all vanish, the generators of J′ have no
common zero in Cn. Therefore ZCn(J′) = ∅, so the weak Nullstellensatz over K tells us
J′ = K[x1, . . . , xn+1]. Thus 1 ∈J′:
1 =
r
X
j=1
hj(x1, . . . , xn, xn+1)fj(x1, . . . , xn) + h(x1, . . . , xn, xn+1)(xn+1g −1)
for some h1, . . . , hr, h in K[x1, . . . , xn+1]. The rest of the proof proceeds just as in the proof
of the Nullstellensatz over algebraically closed ﬁelds.
□
Example A.12. For a ﬁeld K, let f be irreducible in K[x1, . . . , xn]. For g ∈K[x1, . . . , xn],
we’ll show g = 0 at all points in K
n where f = 0 if and only if f | g in K[x1, . . . , xn]. The
polynomials in K[x1, . . . , xn] that vanish in K
n where f vanishes form the ideal IK(ZKn(f)),
and by the Nullstellensatz over K that ideal in K[x1, . . . , xn] is Rad(f), which equals (f)
since f is irreducible in K[x1, . . . , xn]. Thus g ∈IK(ZKn(f)) is equivalent to f | g. We
have generalized Example 4.18 from algebraically closed ﬁelds K to all ﬁelds K.
Consider x2 −2y2 in Q[x, y]. It is irreducible since, viewed in Q[y][x], it is quadratic in x
with no root in Q[y] (think about the rational roots theorem over a UFD). If g(x, y) ∈Q[x, y]
satisﬁes g(a, b) = 0 for all a, b ∈Q such that a2 = 2b2 then (x2 −2y2) | g(x, y) in Q[x, y].
Note x2 −2y2 is not irreducible in Q[x, y].
Example A.13. For a ﬁeld K, set J = (x2, xy, z2) in K[x, y, z]. Then
ZK3(J) = {(0, b, 0) : b ∈K},
IK(ZK3(J)) = {g ∈K[x, y, z] : g(0, b, 0) = 0 for all b ∈K}.
As in Example 4.19, (x, z) ⊂IK(ZK3(J)) and the reverse containment IK(ZK3(J)) ⊂(x, z)
follows by either a concrete calculation (since K is inﬁnite) or by using the Nullstellensatz
over K (since (x, z) is a prime ideal in K[x, y, z] for all ﬁelds K).
It is important to use the zero set ZK3(x2, xy, z2) in K
3, not ZK3(x2, xy, z2) in K3. If
K = Fp then ZK3(x2, xy, z2) = {(0, b, 0) : b ∈Fp}, so yp −y ∈IK(ZK3(x2, xy, z2)) but
yp −y ̸∈(x, z). When we look at zero sets in K
3, or at least using ﬁelds strictly larger than
Fp, yp −y no longer vanishes at all (0, b, 0) since there are more than p choices for b.
Here is a generalization of the ideal–variety correspondence from algebraically closed
ﬁelds in Theorem 4.20 to all ﬁelds.

<!-- page 26 -->
26
KEITH CONRAD
Theorem A.14. The mappings V ⇝IK(V ) and J ⇝ZCn(J) between K-varieties in Cn
and radical ideals J in K[x1, . . . , xn] are inclusion-reversing bijections that are inverses:
ZCn(IK(V )) = V and IK(ZCn(J)) = J.
Proof. The mappings V ⇝IK(V ) and J ⇝ZCn(J) both make sense and it’s easy to see
V ⊂V ′ =⇒IK(V ′) ⊂IK(V ),
J ⊂J′ =⇒ZCn(J′) ⊂ZCn(J).
We have already seen that these mappings are inverses of each other: that ZCn(IK(V )) = V
for all K-varieties V in Cn is Theorem A.4, and that IK(ZCn(J)) = J for radical ideals J
in K[x1, . . . , xn] is immediate from the Nullstellensatz over K in Theorem A.11.
□
We conclude with an application of the weak Nullstellensatz over Q to comparing irre-
ducibility of polynomials over Q and Fp. Polynomials in Z[x] that are irreducible in Q[x]
need not be irreducible mod p for some p: x4 + 1 is irreducible in Q[x] but it is reducible
mod p for every p. However, if we compare irreducibility of a polynomial in Z[x1, . . . , xn]
over the algebraic closures Q and Fp then there is a connection by the following theorem
of Noether [5].
Theorem A.15. For nonconstant f ∈Z[x1, . . . , xn] of degree d, the following conditions
are equivalent:
(1) f is irreducible in Q[x1, . . . , xn],
(2) for all but ﬁnitely many p, f mod p is irreducible in Fp[x1, . . . , xn] of degree d.
When n = 1 this is a boring theorem, since irreducibility of single-variable polynomials
over an algebraically closed ﬁeld like Q or Fp means the polynomial is linear.
Example A.16. Let f(x, y) = x2 + y2 −7. This is irreducible in Q[x, y] since in Q[y][x]
it is Eisenstein at y −
√
7. For the same reason, f(x) mod p is irreducible in Fp[x, y] when
p ̸= 2, 7. It is reducible in F2[x, y], where f(x, y) = x2 + y2 + 1 = (x + y + 1)2, and also in
F7[x, y], where f(x, y) = x2 + y2 = (x + iy)(x −iy) with i2 = −1 in characteristic 7.
A few years before Noether proved Theorem A.15, Ostrowski [6] proved condition (1)
implies that for all but ﬁnitely many p, f mod p is irreducible over Fp (not Fp, a much
stronger condition).
Proof. The argument is based on considering “generic” factorizations of a polynomial into
lower-degree polynomials. This will let us interpret the reducibility of a multivariable poly-
nomial over a ﬁeld F as the existence of a common zero in F to a certain system of
multivariable polynomials.
When a prime p does not divide some nonzero coeﬃcient of f, f mod p has the same
degree as f, so deg(f mod p) = deg f for all but ﬁnitely many p. Therefore the theorem
is obvious if d = 1, since (i) all polynomials (in any number of indeterminates) of degree 1
over a ﬁeld are irreducible and (ii) deg(f mod p) = deg f for all but ﬁnitely many p. We
may now suppose d ≥2.
For a ﬁeld F, a polynomial of degree d in F[x] := F[x1, . . . , xn] is reducible when it is
a product of two polynomials in F[x] with degree less than d. Let’s look at a “universal”
product of polynomials in n indeterminates of degree j and d −j, where 1 ≤j ≤d −1.12
For an n-tuple of nonnegative integers α = (α1, . . . , αn), let Mα(x) = xα1
1 · · · xαn
n
be the
monomial with exponents from α and let |α| = α1 + · · · + αn be the degree of Mα(x). A
pair of “generic polynomials” of degree j and d −j in n indeterminates x1, . . . , xn is
gj(u, x) =
X
|α|≤j
uαMα(x),
hd−j(v, x) =
X
|β|≤d−j
vβMβ(x),
12We only need to consider 1 ≤j ≤d/2.

<!-- page 27 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
27
where the coeﬃcients {uα, vβ : |α| ≤j, |β| ≤d−j} are algebraically independent over Q.13
The product of these two polynomials involves monomials of degree up to d with coeﬃcients
in Z[u, v] := Z[{uα, vβ : |α| ≤j, |β| ≤d −j}]:
(A.2)
gj(u, x)hd−j(v, x) =
X
|γ|≤d
wγ,j(u, v)Mγ(x),
where wγ,j(u, v) ∈Z[u, v].
The coeﬃcients wγ,j(u, v) on the right side of (A.2) are polynomials in the indeterminate
coeﬃcients uα and vβ of the factors on the left side. For f(x) = P
|γ|≤d cγMγ(x) in R[x],
f(x) is a product of polynomials of degree at most j and d−j in R[x] if and only if the right
side of (A.2) equals f(x) for some uα’s and vβ’s in R. So when R is an integral domain,
f(x) is a product of polynomials of degree j and d −j in R[x] if and only if all
wγ,j(u, v) −cγ in Z[u, v] for |γ| ≤d have a common zero with uα and vβ in R.
Strictly speaking, specializing the uα’s and vβ’s to elements of R makes gj(u, x) and
hd−j(v, x) have degree at most j and d−j in R[x], but when deg f = d and R is an integral
domain, a decomposition of f(x) into factors of degree at most j and d −j in R[x] must
use factors of degree j and d −j.
With this description of reducibility, we can prove the equivalence of (1) and (2) using
R = Q and R = Fp.
(1) ⇒(2). Write f(x) = P
|γ|≤d cγMγ(x) where cγ ∈Z. From the discussion above,
f(x) is a product of polynomials of degree j and d −j over Q if and only if the system of
polynomials {wγ,j(u, v) −cγ : |γ| ≤d} in Z[u, v] has a common zero where each uα and
vβ is in Q.
Since f is irreducible over Q, for each j from 1 to d−1 there is no decomposition of f into
factors of degree j and d−j over Q, so the system of polynomials {wγ,j(u, v)−cγ : |γ| ≤d}
for each j has no common zero with coordinates in Q. These polynomials have rational
coeﬃcients, so the weak Nullstellensatz over Q (not the weak Nullstellensatz over Q) tells
us that the ideal generated by these polynomials in Q[u, v] contains 1: we can write
(A.3)
1 =
X
|γ|≤d
qγ,j(u, v)(wγ,j(u, v) −cγ)
for some qγ,j(u, v) ∈Q[u, v].
To show f(x) mod p is irreducible in Fp[x] for all but ﬁnitely many p, we want to reduce
(A.3) mod p. The polynomials wγ,j(u, v) −cγ have Z-coeﬃcients but qγ,j(u, v) has Q-
coeﬃcients, so let’s clear out a common denominator bj in Z+: qγ,j(u, v) = Qγ,j(u, v)/bj,
where Qγ,j(u, v) ∈Z[u, v]. Multiplying both sides of (A.3) by bj,
(A.4)
bj =
X
|γ|≤d
Qγ,j(u, v)(wγ,j(u, v) −cγ).
All coeﬃcients here are integers, so we can reduce (A.4) mod p. We will use p not dividing
the nonzero coeﬃcients of f(x), so f(x) mod p has degree d.
If f(x) mod p is reducible in Fp[x] then for some j in {1, . . . , d −1} it is a product of
polynomials of degree j and d −j in Fp[x], which implies the polynomials wγ,j(u, v) −cγ
over all γ with |γ| ≤d have a common zero {uα, vβ} where all the coordinates are in Fp.
Substituting these values for uα and vβ into the right side of (A.4) reduced mod p makes
each term in the sum on the right vanish in Fp, so bj = 0 in Fp. Thus p | bj. So when
p does not divide the nonzero coeﬃcients of f(x) and all of b1, . . . , bd−1, f(x) mod p has
13The exact number of n-tuples α with |α| = k is
 k+n−1
n−1

.

<!-- page 28 -->
28
KEITH CONRAD
degree d and has no factorization over Fp into two smaller-degree polynomials. Therefore
f(x) mod p is irreducible of degree d over Fp for all but ﬁnitely many primes p.
(2) ⇒(1). We will prove the contrapositive: if f is reducible in Q[x] then f(x) mod p is
reducible in Fp[x] for all but ﬁnitely many primes p. (Strictly speaking, the negation of (2)
is the apparently weaker condition that f(x) mod p is reducible in Fp[x] for inﬁnitely many
p.) Let f(x) = g(x)h(x) in Q[x] where deg g, deg h < d. We want to show this factorization
can be reduced mod p for all but ﬁnitely many p.
Let {ck} be the set of all nonzero coeﬃcients of g(x) and h(x). Each ck is in Q and
therefore is the root of a monic polynomial mk(x) in Q[x]. Intuitively, we should be able to
make sense of ck in Fp as long as p doesn’t divide a denominator of a coeﬃcient of mk(x).
We will use that idea to put the ﬁnitely many numbers ck into a ﬁnitely generated Z-algebra
in which each ck is a unit.
Let N be a positive integer that is divisible by
(i) all the denominators of the (rational) coeﬃcients of all mk(x),
(ii) the numerators of the (nonzero!) constant terms of all mk(x).
Let R be the Z-algebra generated by 1/N and all the nonzero coeﬃcients ck of g(x) and
h(x), so g(x) and h(x) are in R[x]. By (i), each mk(x) is monic in Z[1/N][x], so each ck
is integral over Z[1/N]. SinceR is generated by the ck’s as a Z[1/N]-algebra, integrality of
the ck’s over Z[1/N] makes all elements of R integral over Z[1/N] (Corollary 2.10) and R
is a ﬁnitely generated Z[1/N]-module. By (ii), the constant term of each mk(x) is a unit
in Z[1/N] and that makes each ck a unit in R: the proof of Theorem 2.7 shows that when
B/A is an integral ring extension and b ∈B is the root of a monic polynomial in A[x] with
constant term in A×, b is in B×. Use that with A = Z[1/N] and B = R.
From the factorization f(x) = g(x)h(x) in R[x] we will show f(x) mod p is reducible in
Fp[x] for each prime p where p ∤N.
When p ∤N, p ̸∈R×: if p ∈R× then 1/p would be integral over Z[1/N], so 1/p ∈Z[1/N]
(see the end of Example 2.4) and that’s false since p ∤N. Therefore R has a maximal ideal
m containing p (use for m a maximal ideal of R containing the proper ideal pR). The ﬁeld
R/m is ﬁnite by Corollary 5.2 and it has characteristic p since p ∈m. Reducing the equation
f(x) = g(x)h(x) in R[x] modulo m, f(x) = g(x)h(x) in (R/m)[x] ⊂Fp[x], so f(x) mod p
is reducible over Fp as long as g(x) and h(x) are not constant in (R/m)[x], and they are
nonconstant mod m since their nonzero coeﬃcients in R are in R× and thus the nonzero
coeﬃcients don’t vanish mod m no matter what maximal ideal m is used in R.
□
Corollary A.17. For nonconstant f ∈Z[x1, . . . , xn], if f mod p is irreducible over Fp for
inﬁnitely many p then f mod p is irreducible over Fp for all but ﬁnitely many p.
This is analogous to the fact that if F is an inﬁnite ﬁeld (like Fp) and f(x) ∈F[x] has
f(a) = 0 for inﬁnitely many a ∈F then f(a) = 0 for all a ∈F since a nonzero polynomial
in F[x] has only ﬁnitely many roots in F.
Proof. We will prove the contrapositive. If it’s not true that f mod p is irreducible over Fp
for all but ﬁnitely many p then f(x1, . . . , xn) is reducible over Q by the contrapositive of
(1) ⇒(2) in Theorem A.15. (Concerning the degree condition in (2), deg(f mod p) = deg f
for all but ﬁnitely many p since only ﬁnitely many primes divide the nonzero coeﬃcients of
f.) Then f mod p is reducible over Fp for all but ﬁnitely many p by the method of proof of
(2) ⇒(1) in Theorem A.15, so f mod p is irreducible over Fp for only ﬁnitely many p.
□
Remark A.18. It is very important in Corollary A.17 that the irreducibility is over the
algebraic closure Fp. The result is completely false over the ﬁnite ﬁeld Fp. For instance,

<!-- page 29 -->
MAXIMAL IDEALS IN POLYNOMIAL RINGS
29
x2 + 1 mod p is irreducible in Fp[x] if p ≡3 mod 4 and reducible in Fp[x] if p ̸≡3 mod 4,
and there are inﬁnitely many primes of both types.
How large does p have to be so that f mod p in Theorem A.15 is guaranteed to be
irreducible over Fp of degree d? A lower bound in [8, Corollary 2B, p. 193] is
(A.5)
p > (4||f||)k2k
where ||f|| is the sum of the absolute values of the coeﬃcients of f and k =
 n+d−1
n

. A
smaller lower bound is given in [7] for polynomials in two indeterminates:
(A.6)
p > (a(b + 1)b2 + (a + 1)(b −1)a2)ab+(b−1)/2H(f)2ab+b−1,
where H(f) is the maximum absolute value of the coeﬃcients of f, a is the x-degree of f,
and b is the y-degree of f.
Example A.19. The following example is taken from the start of [7]. Let
f(x, y) = x9y −9x9 −2x + 9y + 2.
This is irreducible in Q[x, y] by looking at in Q[x][y]: f(x, y) = (x9 + 9)y + (−9x9 −2x + 2)
is linear in y, so it is irreducible over Q(x), and it remains irreducible in Q[x][y] because
its coeﬃcients in Q[x] are relatively prime (the coeﬃcients have no common root). This is
a special case of irreducibility of nonconstant polynomials in R[y] when R is a UFD: it is
necessary and suﬃcient that the polynomial is irreducible over the fraction ﬁeld of R and
be primitive (coeﬃcients in R have gcd 1).
To apply (A.5) and (A.6) for a lower bound on the p making f(x, y) mod p irreducible
over Fp, note ||f|| = 23, k =
 2+10−1
2

= 55, H(f) = 9, a = 9, and b = 1. Then (A.5) gives
the shockingly large lower bound 9255255
and (A.6) gives the lower bound 189 · 918, which
is a 29-digit number. You may think the second lower bound is also absurdly large, but
f(x, y) mod p is reducible over Fp for a much larger p than you might expect: the coeﬃcients
x9 + 9 and −9x9 −2x + 2 have a common root 93470127633772547 mod p where p is the
18-digit prime 186940255267545011, so f(93470127633772547, y) = 0 in Fp[y]. Therefore in
Fp[x, y], f(x, y) mod p is reducible with factor x −93470127633772547. An explanation of
how that monster prime p can be found systematically using resultants is in my answer to
https://mathoverflow.net/questions/130783/.
In [5], Noether showed that for a ﬁeld F, irreducibility in F[x] of polynomials of degree d ≥
2 is a “coeﬃcient property”: there is a set of multivariable polynomials Gγ(y), depending
only on d, such that f(x) in F[x] is irreducible of degree d if and only if the polynomials
Gγ(y) don’t all vanish when the coeﬃcients of f(x) are substituted into the variables of all
Gγ(y). (A simple analogue of this is that ax2 +bx+c over a ﬁeld is a separable quadratic if
and only if a ̸= 0 and b2−4ac ̸= 0.) This is diﬀerent from how we worked with irreducibility
over F in the proof of Theorem A.15, where we expressed it in terms of certain multivariable
polynomials depending on f(x) not vanishing at all points (u, v) with coordinates uα and
vβ in F.
The polynomials Gγ(y) arise from treating nonzero polynomials in F[x] of degree at most
d as points in a projective space using coeﬃcients as coordinates, e.g., ax2 +bx+c becomes
[a : b : c] in the projective plane. (This is sensible because reducibility of a polynomial
over a ﬁeld is unaﬀected by scaling the coeﬃcients by a common nonzero factor.)
For
1 ≤j ≤d −1, let Pj,n be the projective space of coeﬃcients of nonzero polynomials in n
indeterminates over F of degree at most j and let µj : Pj,n×Pd−j,n →Pd,n be multiplication
of such polynomials (degree at most j times degree at most d −j has degree at most d).
Projective spaces can be given the Zariski topology (closed sets are zero sets of homogeneous

<!-- page 30 -->
30
KEITH CONRAD
polynomials) and the image of each µj turns out to be a Zariski closed subset of Pd,n because
projective spaces in algebraic geometry are proper (analogous to projective spaces over R
and C being compact and Hausdorﬀin their classical topology), so the polynomials in
F[x] that are reducible of degree d or have degree less than d form the Zariski closed set
S
1≤j≤d−1 µj(Pj,n × Pd−j,n) in Pd,n. A Zariski closed set is deﬁned by the vanishing of a
ﬁnite set of polynomials, and that is what the polynomials Gγ(y) are.
Interpreting nonzero polynomials of degree at most d as a projective space with coeﬃ-
cients being coordinates, and reducible polynomials of degree d plus polynomials of degree
less than d as a union of images of multiplication maps S
1≤j≤d−1 µj(Pj,n × Pd−j,n), can
be applied to real polynomials in one variable and leads to a proof of the Fundamental
Theorem of Algebra purely in terms of R, making no use of complex numbers. See Section
3 of https://kconrad.math.uconn.edu/blurbs/fundthmalg/propermaps.pdf.
References
[1] A. Azarang, A simple proof of Zariski’s lemma, Bull. Iranian Math. Soc. 43 (2017), 1529–1530. URL
https://arxiv.org/abs/1506.08376.
[2] W. Fulton, “Algebraic Curves,” Addison-Wesley, New York, 1989. URL http://www.math.lsa.umich.
edu/∼wfulton/CurveBook.pdf.
[3] J. Gray, Algebraic geometry between Noether and Noether – a forgotten chapter in the history of algebraic
geometry, Revue d’histoire des math´ematiques 3 (1997), 1–48. URL http://www.numdam.org/article/
RHM 1997
3 1 1 0.pdf.
[4] D. Hilbert, ¨Uber die vollen Invariantensysteme, Math. Ann. 42 (1893), 313–373. URL https://eudml.
org/doc/157652.
[5] E. Noether, Ein algebraisches Kriterium f¨ur absolute Irreduzibilit¨at, Math. Ann. 85 (1922), 26–33. URL
https://eudml.org/doc/158900.
[6] A. Ostrowski, Zur arithmetischen Theorie der algebraischen Gr¨ossen, Nachr. Ges. Wiss. G¨ottingen,
Math.-Phys. Klasse (1919), 279–298. URL https://eudml.org/doc/59056.
[7] W. M. Ruppert, Reducibility of polynomials f(x, y) modulo p, J. Number Theory 77 (1999), 62–70. URL
https://arxiv.org/abs/math/9808021v1.
[8] W. M. Schmidt, “Equations over Finite Fields: an Elementary Approach,” Lecture Notes in Mathematics
536, Springer-Verlag, Berlin, 1976.
[9] O. Zariski, The compactness of the Riemann manifold of an abstract ﬁeld of algebraic functions, Bull.
Amer. Math. Soc. 50 (1944), 683–691. URL https://www.ams.org/journals/bull/1944-50-10/S0002-
9904-1944-08206-2/S0002-9904-1944-08206-2.pdf.
[10] O. Zariski, A new proof of Hilbert’s Nullstellensatz, Bull. Amer. Math. Soc. 53 (1947), 362–368. URL
https://www.ams.org/journals/bull/1947-53-04/S0002-9904-1947-08801-7/S0002-9904-1947-0880
1-7.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*