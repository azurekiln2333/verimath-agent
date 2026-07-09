# Cauchyapp

> **Source**: https://kconrad.math.uconn.edu/blurbs/cauchyapp.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
CONSEQUENCES OF CAUCHY’S THEOREM
KEITH CONRAD
In this handout, we meet some basic consequences of Cauchy’s theorem in group theory.
These consequences do not depend on the proof of Cauchy’s theorem, but only on the
conclusion of the theorem.
1. Quick Consequences
Theorem 1.1. For a ﬁnite group G and a prime p, |G| is a power of p if and only if all
elements of G have p-power order.
What is special about prime powers for this theorem is that factors of a power of p are
again powers of p.
Proof. If |G| is a power of p, then the order of each element of G is a power of p since the
order of each element divides the size of the group.
Conversely, assume all elements of G have p-power order. To show |G| is a power of p,
suppose it is not, so |G| is divisible by a prime q ̸= p. Then, by Cauchy, G has an element
of order q, and that’s a contradiction of our assumption.
□
Theorem 1.2. If all non-identity elements of G have the same order, this order is a prime
p and |G| is a power of p.
Proof. If |G| has two prime factors, say p and q, then G contains elements of orders p and
q by Cauchy, which contradicts the hypothesis. Thus |G| has only one prime factor, say
|G| = pm for a prime p. The orders of a non-identity element could be {p, p2, . . . , pm}.
However, by Cauchy some g ∈G has order p, so the hypothesis tells us every non-identity
element of G has order p.
□
Example 1.3. Abelian groups ﬁtting the hypothesis of Theorem 1.2 are easy to write
down, e.g, (Z/(p))n where p is prime. Every non-zero element has order p. For a nonabelian
example, consider the Heisenberg group over Z/(p) when p is an odd prime. Every non-
identity element has order p. Can you ﬁnd a nonabelian example when p = 2?
Corollary 1.4. The size of every ﬁnite ﬁeld is a prime power.
Proof. Let F be a ﬁnite ﬁeld. Its size is at least 2 (since 1 ̸= 0 in F). We are going to think
about F as an additive group.
Each pair of non-zero elements a and b in F (possibly equal) have the same additive order,
since the function f(x) = (b/a)x is additive and invertible, and f sends a to f(a) = b. Thus
|F| is a prime power by Theorem 1.2.
□
Theorem 1.5. Let G be a ﬁnite group and k ∈Z. The function f(x) = xk on G is a
bijection if and only if (k, |G|) = 1.
When G is nonabelian, the kth power map is usually not a homomorphism. Nevertheless,
one can ask if it is a bijection or not.
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. Set n = |G|. First assume (k, n) = 1. Then we can solve kℓ≡1 mod n. Writing
kℓ= 1 + nm, every x ∈G satisﬁes xkℓ= xxnm = x. This shows the function x 7→xk on G
has inverse function x 7→xℓ, since (xk)ℓ= x and (xℓ)k = x for x ∈G. In particular, since
the kth power map on G admits an inverse function it is a bijection. Notice we did not use
Cauchy’s theorem for this direction.
Now assume (k, n) > 1. We will show the k-th power map on G is not a bijection. Since
k and n have a non-trivial common factor, they have a common prime factor, say p. Since
p | n, Cauchy’s theorem says G has an element of order p, say g. Then, since p | k, we have
gk = (gp)k/p = ek/p = e. (Why does it matter that k/p is an integer?) Thus the kth power
map is not a bijection, since it is not one-to-one: g and e both have kth power e.
□
Example 1.6. Check that cubing on D7 is a bijection while squaring is not, and raising to
the 5-th power is a bijection on A4.
2. Decomposing Abelian Groups
As a more involved use of Cauchy’s theorem, we describe how to decompose a ﬁnite
abelian group into subgroups of prime power size.
Theorem 2.1. Let G be ﬁnite abelian with |G| = ab, where (a, b) = 1. Then G is isomorphic
to a direct product A × B, where |A| = a and |B| = b.
Proof. If either a or b is 1, the result is clear: take A or B to be the trivial group.
Since |G| = ab, every g ∈G satisﬁes gab = e. For each m ≥1 the elements g satisfying
gm = e form a subgroup since G is abelian. Set
A = {g ∈G : ga = e},
B = {g ∈G : gb = e}.
These are both subgroups of G. (Note A is not the set of a-th powers in G. It is the
elements whose a-th power is the identity.)
We now show G = AB, i.e., every element of G is the product of an element of A and
an element of B. By Bezout, the relative primality of a and b lets us write
1 = ar + bs
for some r and s in Z. Therefore each g ∈G can be written as
g = gar+bs = (gr)a(gs)b.
Notice (gr)a ∈B since ((gr)a)b = (gr)ab = e, and similarly (gs)b ∈A. Therefore, re-ordering
the terms as
g = (gs)b(gr)a
expresses each g ∈G as the product of an element of A and an element of B, so G = AB.
Now we show G is isomorphic to the direct product A × B. Let f : A × B →G by
multiplication: f(x, y) = xy. This is a homomorphism, since
f((x, y)(x′, y′)) = f(xx′, yy′) = xx′yy′ = (xy)(x′y′) = f(x, y)f(x′, y′).
Note we used commutativity in the third equation. The previous paragraph showed G =
AB, so f is onto. To see f is one-to-one, we check the kernel is trivial. Suppose f(x, y) = e.
Then xy = e, so x = y−1. This equation shows x and y lie in A ∩B. The intersection
A∩B is trivial, since every element of A has order dividing a, every element of B has order
dividing b, and (a, b) = 1. Thus x and y are trivial, so (x, y) = (e, e) is the identity element
of A × B. That proves f has trivial kernel.

<!-- page 3 -->
CONSEQUENCES OF CAUCHY’S THEOREM
3
Now that we know f is an isomorphism of A × B with G, we can show |A| = a and
|B| = b. Because f is a bijection, |A × B| = |G|, so
(2.1)
|A||B| = ab.
We now show (|A|, b) = 1. For this we bring in (at last!) Cauchy’s theorem. If (|A|, b) ̸= 1
then some prime p dividing b will divide |A|. Then Cauchy tells us A has an element of
order p. But every element of A has order dividing a, and p does not divide a (since p | b
and (a, b) = 1). Thus (|A|, b) = 1. Similarly, (|B|, a) = 1. From (2.1), |A| | ab, so in fact
|A| | a. Arguing similarly, |B| | b. Therefore, by (2.1), |A| = a and |B| = b.
□
Corollary 2.2. Every ﬁnite abelian group is isomorphic to a direct product of ﬁnite abelian
groups with prime-power size.
Proof. Let G be a ﬁnite abelian group, with size n = pe1
1 · · · per
r . We can suppose n > 1 and
each ei is non-zero. Taking a = pe1
1 and b = n/a, we have (a, b) = 1, so Theorem 2.1 tells us
G is isomorphic to a direct product A × B, where |A| = a = pe1
1 and |B| = b = n/a. Since
a > 1, by induction on the size of the ﬁnite abelian group we can say B is isomorphic to a
direct product of groups of size pe2
2 , . . . , per
r .
□
3. Groups of Size pq
The rest of this handout provides a deeper use of Cauchy’s theorem. We will classify all
groups having size pq, where p and q are diﬀerent primes. The classiﬁcation, due to Netto
[1, pp. 146–148], says there are at most two possibilities up to isomorphism and describes
the two choices when they occur.
Theorem 3.1. Let p and q be distinct primes, with p < q. If q ̸≡1 mod p, then all groups
of size pq are cyclic. In particular, all groups of size pq are isomorphic. If q ≡1 mod p,
then up to isomorphism there are two groups of size pq: one is cyclic and one is nonabelian.
Example 3.2. Every group of size 15 is cyclic. Use p = 3 and q = 5, and 5 ̸≡1 mod 3.
Example 3.3. When p = 2 and q = 3, we already know two non-isomorphic groups of
size 6: Z/(6) and S3. The ﬁrst is cyclic and the second is not (it is non-abelian). Theorem
3.1 says every group of size 6 is isomorphic to one of these. Here is a table listing four
examples each of abelian and nonabelian groups of order 6. The groups in each column are
isomorphic to each other.
Abelian
Nonabelian
Z/(6)
S3
Z/(2) × Z/(3)
D3
(Z/(9))×
Aﬀ(Z/(3))
µ6
GL2(Z/(2))
Our proof of Theorem 3.1 will use the following lemma.
Lemma 3.4. Let G be a group of size pq, where p and q are prime with p < q. There is
only one subgroup of G with size q.
Notice the hypotheses are not symmetric in p and q; the lemma is about subgroups with
the larger prime order.

<!-- page 4 -->
4
KEITH CONRAD
Proof. By Cauchy, there is a subgroup of G with size q. This subgroup has prime size and
therefore is cyclic. Write it as ⟨g⟩.
In order to show ⟨g⟩is the only subgroup with size q, assume otherwise. Then there is
some h ∈G having order q such that h ̸∈⟨g⟩. Then ⟨h⟩∩⟨g⟩is trivial: this intersection is
a subgroup of ⟨h⟩that can’t be everything (because h ̸∈⟨g⟩), so it must be trivial because
the only proper subgroup of ⟨h⟩is trivial.
Consider the left cosets of ⟨g⟩represented by powers of h:
(3.1)
⟨g⟩, h⟨g⟩, h2⟨g⟩, . . . , hq−1⟨g⟩.
There are q cosets in this list. The total number of diﬀerent left ⟨g⟩-cosets is [G : ⟨g⟩] =
(pq)/q = p. Since p < q, two of the cosets in (3.1) must be equal, say hi⟨g⟩= hi′⟨g⟩with
0 ≤i < i′ ≤q −1. Then hi′−i ∈⟨g⟩, so we have a power of h other than the identity equal
to a power of g. This contradicts the previous paragraph, so h can’t exist. That is, every
element of G with order q lies in ⟨g⟩, so ⟨g⟩is the only subgroup with order q.
□
Example 3.5. Consider the group D5, of size 10. Here q = 5. There is one subgroup of
size 5: the rotations.
Now we are ready to prove part of Theorem 3.1.
Theorem 3.6. Let p, q be primes where p < q. Each abelian group of size pq is cyclic. If
q ̸≡1 mod p, then each group of size pq is cyclic.
Examples satisfying the condition q ̸≡1 mod p are 15 = 3 · 5, 35 = 5 · 7, 33, 65, 77, and
95. Every group with these sizes is cyclic.
Proof. Let G be a ﬁnite group with |G| = pq. By Cauchy’s theorem, G has an element a of
order p and an element b of order q. If G is abelian then ab has order pq, so G is cyclic.
The rest of the proof is devoted to showing that, when q ̸≡1 mod p, a and b must
commute even if we don’t assume in advance that G is abelian, so again we get that ab has
order pq and G is cyclic.
Write the desired condition ab = ba as: aba−1 = b. This is what we will show. Since
aba−1 is a conjugate of b, it has order q. Thus, by Lemma 3.4, aba−1 is a power of b, say
aba−1 = bk
for some integer k. By induction, amba−m = bkm for all m ≥1. Taking m = p gives
b = bkp.
Since b has order q, this equality implies kp ≡1 mod q, so k mod q has order either 1 or p
in (Z/(q))×, a group of size q −1. If the order is p, then p | (q −1), so q ≡1 mod p. But
q ̸≡1 mod p by hypothesis (aha). Thus the order of k in (Z/(q))× is 1, so k ≡1 mod q and
aba−1 = bk = b1 = b,
which means ab = ba.
□
So far we proved Theorem 3.1 if q ̸≡1 mod p and partially (i.e., for abelian groups) if
q ≡1 mod p. What about nonabelian groups of size pq for primes p < q if q ≡1 mod p?
There is always a nonabelian group of size pq when q ≡1 mod p. Here is one, constructed
as a subgroup of the aﬃne group Aﬀ(Z/(q)):
(3.2)
Ap,q =

x
y
0
1

∈Aﬀ(Z/(q)) : xp = 1 in Z/(q)

.

<!-- page 5 -->
CONSEQUENCES OF CAUCHY’S THEOREM
5
The reader can check this is a subgroup of Aﬀ(Z/(q)). To count its size, note there are q
choices for y, since we imposed no constraints on y. How many choices are there for x?
Since x ∈(Z/(q))× and p | (q −1) by hypothesis, Cauchy’s theorem tells us there is an
element of order p in (Z/(q))×, and thus its powers give at least p solutions to xp = 1 in
Z/(q). There can be no more than p solutions (see Theorem A.1), so there are exactly p
solutions. Thus, the solutions to xp = 1 in (Z/(q))× are a cyclic group of size p. Therefore
|Ap,q| = pq.
The group Ap,q is nonabelian, since the matrices ( 1 1
0 1 ) and ( x 0
0 1 ) don’t commute, where
x is an element of order p in (Z/(q))×.
Example 3.7. When p = 3 and q = 7, q ≡1 mod p. The solutions to x3 ≡1 mod 7 are 1,
2, and 4, so a nonabelian group of order 21 is
A3,7 =

x
y
0
1

: x = 1, 2, 4 in Z/(7), y ∈Z/(7)

.
Now we are ready to complete the proof of Theorem 3.1 with an analysis of the nonabelian
case when q ≡1 mod p.
Theorem 3.8. Let p and q be primes with p < q and q ≡1 mod p. Up to isomorphism,
the group Ap,q in (3.2) is the only nonabelian group of size pq.
Proof. Let G be a nonabelian group with size pq. By Cauchy, there is a ∈G with order p
and b ∈G with order q. If a and b commute, then ab has order pq, so G is cyclic. Since G
is nonabelian, a and b do not commute. Since ⟨a, b⟩has subgroups of size p and q, ⟨a, b⟩is
divisible by pq, so ⟨a, b⟩= G.
By Lemma 3.4 (here we use the condition p < q), all elements of order q in G are powers
of b, so aba−1 = bt for some t. We have t ̸≡1 mod q, as otherwise aba−1 = b, which would
imply ab = ba, but a and b do not commute.
For each k ≥0, conjugating b by a a total of k times gives
(3.3)
akba−k = btk.
Taking k = p, b = btp, so tp ≡1 mod q. Therefore t has order p in (Z/(q))×. Moreover,
raising both sides of (3.3) to an arbitrary integer power ℓyields
akbℓa−k = bℓtk,
so
(3.4)
akbℓ= bℓtkak.
This means each (non-negative) power of a to the left of a power of b can be placed on the
right side at the cost of changing the exponent of b. Thus,
(3.5)
G = ⟨a, b⟩= {bnam : m, n ≥0}.
Now we look at the group Ap,q in (3.2). The upper left entry of a matrix in this group is
an element of (Z/(q))× with order dividing p. Because the solutions to xp = 1 in (Z/(q))×
form a subgroup of size p and t has order p in (Z/(q))×, these solutions are exactly the

<!-- page 6 -->
6
KEITH CONRAD
powers of t. Therefore each matrix in Ap,q has the following form, where m, n ≥0:

tm
n
0
1

=

1
n
0
1
 
tm
0
0
1

=

1
1
0
1
n 
t
0
0
1
m
.
This suggests, since ( 1 1
0 1 ) has order q (like b) and ( t 0
0 1 ) has order p (like a), the following
function f : Ap,q →G:
f

tm
n
0
1

= bnam.
This function f is well-deﬁned, since m and n in ( tm n
0
1 ) only matter modulo p and q,
respectively.
To check f is an isomorphism, we must show it is a homomorphism (f(AB) = f(A)f(B)
for all A and B in Ap,q), one-to-one, and onto.
For the homomorphism property, pick A = ( tm n
0
1 ) and B = ( tm′ n′
0
1 ) in Ap,q. Then
f(AB) = f

tm
n
0
1
 
tm′
n′
0
1

= f

tm+m′
tmn′ + n
0
1

= btmn′+nam+m′
= bnbtmn′amam′
= bnambn′am′
by (3.4)
= f(A)f(B).
The reason f is onto is (3.5), which shows every element of G is a value of f.
That f : Ap,q →G is one-to-one is now automatic since f is onto and |Ap,q| = |G|. So
there is nothing more we need to do, but for the sake of illustrating technique we will check
f is one-to-one directly by showing its kernel is trivial. If f( tm n
0
1 ) = 1 then bnam = 1, so
am = b−n ∈⟨a⟩∩⟨b⟩.
This intersection is trivial since ⟨a⟩and ⟨b⟩are nontrivial groups whose sizes are relatively
prime, so am = 1 and bn = 1. Thus p | m and q | n, so ( tm n
0
1 ) = ( 1 0
0 1 ), which shows f has a
trivial kernel.
□
Corollary 3.9. For odd primes q, each group of order 2q is either cyclic or dihedral: it is
isomorphic to Z/(2q) or to Dq.
Proof. Taking p = 2 in Theorem 3.8, the subgroup Ap,q of Aﬀ(Z/(q)) is one of the matrix
models for Dq.
□
Remark 3.10. When p = q, groups of order pq = p2 can be classiﬁed up to isomorphism
and as in Theorem 3.1 there are two such groups, but both are abelian: one is cyclic and
the other is Z/(p) × Z/(p).
Remark 3.11. Recalling the deﬁnition D2 = Z/(2) × Z/(2), Corollary 3.9 is true at q = 2
since each group of order 4 is isomorphic to Z/(4) or Z/(2) × Z/(2). So Corollary 3.9 is
valid for all primes q.

<!-- page 7 -->
CONSEQUENCES OF CAUCHY’S THEOREM
7
Appendix A. Root Counting
We prove here a result on polynomials used to count the size of the group Ap,q in (3.2).
Theorem A.1. Let f(x) be a non-constant polynomial with coeﬃcients in Z/(p), of degree
d. Then f(x) has at most d roots in Z/(p).
To prove Theorem A.1, we use a lemma connecting roots and linear factors.
Lemma A.2. Let f(x) be a non-constant polynomial with coeﬃcients in Z/(p). For a in
Z/(p), f(a) = 0 if and only if x −a is a factor of f(x).
Example A.3. When the coeﬃcients are Z/(5) the polynomial f(x) = x3 −2 has f(3) = 0
and x3 −2 = (x −3)(x2 + 3x −1).
Proof. If x −a is a factor of f(x), then f(x) = (x −a)h(x). Substituting a for x shows
f(a) = 0.
Conversely, suppose f(a) = 0. Write the polynomial as
(A.1)
f(x) = cnxn + cn−1xn−1 + · · · + c1x + c0,
where cj ∈Z/(p) and cn ̸= 0. Then
(A.2)
0 = cnan + cn−1an−1 + · · · + c1a + c0.
Subtracting (A.2) from (A.1), the terms c0 cancel and we get
(A.3)
f(x) = cn(xn −an) + cn−1(xn−1 −an−1) + · · · + c1(x −a).
Since
xj −aj = (x −a)(xj−1 + axj−2 + · · · + aixj−1−i + · · · + aj−2x + aj−1),
each term on the right side of (A.3) has an x −a in it. Factor it out of each term in (A.3)
and obtain f(x) = (x −a)g(x) where g(x) is a polynomial with coeﬃcients in Z/(p).
□
Now we prove Theorem A.1.
Proof. We induct on the degree d of f(x). Note d ≥1.
A polynomial of degree 1 has the form f(x) = ax + b, where a and b are in Z/(p) and
a ̸= 0. This has exactly one root in Z/(p), namely −b/a, and thus at most one root in
Z/(p). That settles the theorem for d = 1.
Now assume the theorem is true for all polynomials with coeﬃcients in Z/(p) of degree
d. We verify the theorem for all polynomials with coeﬃcients in Z/(p) of degree d + 1.
A polynomial of degree d + 1 is
(A.4)
f(x) = cd+1xd+1 + cdxd + · · · + c1x + c0,
where cj ∈Z/(p) and cd+1 ̸= 0. If f(x) has no roots in Z/(p), then we’re done, since
0 ≤d + 1. If f(x) has a root in Z/(p), say r, then Lemma A.2 tells us f(x) = (x −r)g(x),
where g(x) is a polynomial with coeﬃcients in Z/(p) of degree d. We can therefore apply
the inductive hypothesis to g(x) and conclude that g(x) has at most d roots in Z/(p). Since
f(a) = (a −r)g(a) for all a ∈Z/(p) and a product of numbers in Z/(p) is 0 only when one
of the factors is 0 (this would be false if our modulus were composite rather than prime!),
we see that each root of f(x) in Z/(p) is either r or is a root of g(x). Thus, f(x) has at most
d + 1 roots in Z/(p). As f(x) was an arbitrary polynomial of degree d + 1 with coeﬃcients
in Z/(p), we are done with the inductive step.
□

<!-- page 8 -->
8
KEITH CONRAD
References
[1] E. Netto, The Theory of Substitutions and its Applications to Algebra, Register Publ. Co., Ann Arbor,
1892. Online at https://archive.org/details/theoryofsubstitu00nett/page/146.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*