# Primvector

> **Source**: https://kconrad.math.uconn.edu/blurbs/primvector.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PRIMITIVE VECTORS AND SLn
KEITH CONRAD
An n-tuple [a1, . . . , an] ∈Zn is called primitive when its coordinates are relatively prime
as an n-tuple. For instance, [6, 10, 15] is a primitive vector in Z3: even though its coordinates
are not pairwise relatively prime they are relatively prime as a triple. We use brackets rather
than parentheses for vectors so that we may reserve the use of parentheses for greatest
common divisors and ideals later.
Each primitive vector [a1, a2] ∈Z2 can be used as the ﬁrst row of an integral matrix
with determinant 1: since (a1, a2) = 1 we can write a1x + a2y = 1 for some x, y ∈Z, which
is equivalent to det( a1 a2
−y x ) = 1. This is a matrix in SL2(Z). There is a generalization to
longer primitive vectors:
Theorem 1. For n ≥2, a vector [a1, . . . , an] ∈Zn with (a1, . . . , an) = (1) is the ﬁrst row
of a matrix in SLn(Z).
Proof. See [4], where Theorem 1 is used to prove the structure theorem for ﬁnitely generated
abelian groups.
□
The converse of Theorem 1 is also true: for n ≥2, the ﬁrst row of a matrix in SLn(Z)
is a primitive vector, since expansion of the determinant along the ﬁrst row shows 1 is a
Z-linear combination of the entries in the ﬁrst row.
If we work in a commutative ring A, and call a vector [a1, . . . , an] ∈An primitive when
the ideal (a1, . . . , an) is the unit ideal of A, is it true that every primitive vector in An
is the ﬁrst row of a matrix in SLn(A)? The answer is no. The simplest example occurs
for the ring R = R[x, y, z]/(x2 + y2 + z2 −1), where the vector [x, y, z] ∈R3 is primitive
(because x · x + y · y + z · z = 1 in R) but [x, y, z] is not the ﬁrst row of a matrix in SL3(R)
(or even GL3(R)); this turns out to follow from the topological fact that every continuous
vector ﬁeld on the sphere vanishes somewhere. The technical buzzword here is “stably free
module” if you want to look up further references to this phenomenon.
Despite the failure of Theorem 1 to generalize to all commutative rings, it does generalize
to some rings besides Z. For instance, Theorem 1 generalizes to vectors with coordinates in
a PID. (The proof in [4] for A = Z only uses PID properties of Z, so it is valid for a PID;
or see [3, Lemma 5.20], which is essentially the proof from [4], including the same notation
and introducing a minor mistake.) Our interest is in a further generalization: by a nice use
of the Chinese remainder theorem, Theorem 1 can be proved for vectors with coordinates
coming from a Dedekind domain.
Theorem 2. Let A be a Dedekind domain. If n ≥2 and the ideal (a1, . . . , an) is the unit
ideal (1) = A then the n-tuple [a1, . . . , an] is the ﬁrst row of a matrix in SLn(A).
To prove this, following the ideas in [1], we ﬁrst establish two lemmas.
Lemma 3. Let A be a commutative ring and pick a vector v ∈An and a matrix U ∈SLn(A).
Then v is the ﬁrst row of a matrix in SLn(A) if and only if the product vU ∈An is the ﬁrst
row of a matrix in SLn(A).
1

<!-- page 2 -->
2
KEITH CONRAD
Proof. Suppose there is a matrix M ∈SLn(A) with ﬁrst row v.
Then MU ∈SLn(A)
has ﬁrst row vU. Conversely, if there is a matrix N ∈SLn(A) with ﬁrst row vU then
NU−1 ∈SLn(A) has ﬁrst row (vU)U−1 = v.
□
The following lemma about Dedekind domains will provide a reduction step in the proof
of Theorem 2.
Lemma 4. Let A be a Dedekind domain.
If n ≥3 and (a1, . . . , an) = (1) in A with
a1, . . . , an−2 not all 0 then there is some b ∈A such that (a1, . . . , an−2, an−1 + ban) = (1).
The point here is that we can turn a set of n generators of the unit ideal into a set of
n −1 generators by combining two terms in a particularly simple way.
Proof. By hypothesis, (a1, . . . , an−2) ̸= (0). If (a1, . . . , an−2) = (1) we can take b to be
an arbitrary element of A. So we may assume (a1, . . . , an−2) is neither (0) nor (1). Fac-
tor (a1, . . . , an−2) into primes as p1 · · · pr.
(Perhaps some pi are equal.)
In particular,
a1, . . . , an−2 belong to each pi.
For i = 1, 2, . . . , r, choose bi ∈A so that an−1 + bian ̸≡0 mod pi. Why is this possible?
Well, when an ̸≡0 mod pi we can solve an−1 +xan ≡1 mod pi since A/pi is a ﬁeld and then
set bi = x. When an ≡0 mod pi we can let bi be anything at all and we must check that
an−1 ̸≡0 mod pi: a1, a2, . . . , an−2 ∈pi and an ∈pi, so if an−1 ∈pi then (a1, . . . , an−1, an) ⊂
pi, but (a1, . . . , an−1, an) = (1), which is a contradiction.
Thus an−1 ̸≡0 mod pi when
an ≡0 mod pi.
Since the pi’s are maximal ideals in A, by the Chinese remainder theorem we can ﬁnd
b ∈A with b ≡bi mod pi for all i. (In case pi = pj for some i ̸= j, we should take care
to choose bi and bj to be equal in A, which is possible since the conditions constraining bi
and bj — an−1 + bian ̸≡0 mod pi and an−1 + bjan ̸≡0 mod pj — are the same.) Then
for all i, an−1 + ban ≡an−1 + bian ̸≡0 mod pi. So the principal ideal (an−1 + ban) is not
contained in p1, . . . , pr. We claim the ideal (a1, . . . , an−2, an−1 + ban) equals (1). Indeed, if
(a1, . . . , an−2, an−1 + ban) ̸= (1) it lies in some maximal ideal p. Then (a1, . . . , an−2) ⊂p,
so p ⊃p1 · · · pr. This implies p = pi for some i since p is prime and all pi are maximal.
However, an−1 + ban ≡0 mod p and by construction an−1 + ban ̸≡0 mod pi. So having
p = pi for some i is a contradiction.
□
Remark 5. We insist that n ≥3 and that one of a1, . . . , an−2 is nonzero in the hypothesis
of Lemma 4 because the lemma is false with n = 2, i.e., if (a, a′) = (1) there might not
be a b ∈A such that (a + ba′) = (1). For instance, let A = Z[
√
d] for nonsquare d ≤−2,
a = 1 +
√
d, and a′ = d. (Further take d ≡2, 3 mod 4 to be sure A is Dedekind.) Then
(1 +
√
d, d) = (1) but if there were b ∈Z[√−5] such that (1 +
√
d + bd) = (1) then
1 +
√
d + bd = ±1. Writing b = k + ℓ
√
d with k and ℓin Z, we have 1 + dk = ±1 and
1 + dℓ= 0. The second equation has no integral solution.
Now we prove Theorem 2.
Proof. The theorem is symmetric in the ai’s, since we can permute the columns of a matrix
to cause a desired permutation of the ai’s in the top row. This will yield a new matrix with
top row permuted as intended and determinant ±1. If the determinant is −1 then we can
make another matrix with determinant 1 and the same (permuted) top row. by multiplying
the entries of a row besides the ﬁrst row by −1.
If (a1, . . . , an) = (1) and only one ai is nonzero, without loss of generality (by the
previous paragraph) it is a1 that is nonzero.
Then a1 ∈A×, so the diagonal matrix

<!-- page 3 -->
PRIMITIVE VECTORS AND SLn
3
diag(a1, 1/a1, 1, . . . , 1) is in SLn(A) and has ﬁrst row [a1, 0, . . . , 0] = [a1, a2, . . . , an].
If
(a1, . . . , an) = (1) and only two ai’s are nonzero then without loss of generality a1 and a2
are nonzero. Then (a1, a2) = (1), so a1x + a2y = 1 for some x and y in A. Therefore
M = ( a1 a2
−y x ) lies in SL2(A) and the block matrix ( M
O
O In−2 ) is in SLn(A) with ﬁrst row
[a1, a2, 0, . . . , 0] = [a1, a2, a3, . . . , an].
This argument, in particular, veriﬁes the theorem
when n = 2.
Now take n ≥3 and assume the theorem has been proved for all sets of n −1 elements in
A that generate the unit ideal. If (a1, . . . , an−1, an) = (1), we may assume by the previous
paragraph that at least three of the ai’s are nonzero. By symmetry of the theorem in the
ai’s, we can take an−1 and an nonzero. At least one of a1, . . . , an−2 is nonzero, so Lemma
4 tells us (a1, . . . , an−2, an−1 + ban) = (1) for some b ∈A. Then the inductive hypothesis
implies [a1, . . . , an−2, an−1 + ban] is the ﬁrst row of a matrix M ∈SLn−1(A). Note that
[a1, a2, . . . , an]


In−2
O
O
O
1
0
O
b
1

= [a1, . . . , an−2, an−1 + ban, an],
where the n × n matrix on the left is clearly in SLn(A). The vector on the right side of this
equation is the ﬁrst row of the matrix

M
∗
O
1

∈SLn(A),
where ∗is the column vector in An−1 with top coordinate an and the remaining coordinates
equal to 0. Therefore [a1, a2, . . . , an] times a matrix in SLn(A) is the ﬁrst row of a matrix
in SLn(A), so [a1, . . . , an] is itself the ﬁrst row of a matrix in SLn(A) by Lemma 3.
□
Remark 6. The reason Theorem 2 is stated for Dedekind domains is that these are the
rings to which Lemma 4 applies. (Check that no other part of the proof of Theorem 2
uses the Dedekind property, e.g., Lemma 3 is valid for all commutative rings.) But in fact
the proof of Lemma 4 applies to a broader class of rings than Dedekind domains: it works
when A is a Noetherian domain where all nonzero prime ideals are maximal (such as an
order in a number ﬁeld, not just the maximal order). Indeed, a nonzero ideal in such a
ring contains – but might not equal – a product of nonzero prime ideals, and we can take
(a1, . . . , an−2) ⊃p1 · · · pr instead of (a1, . . . , an−2) = p1 · · · pr in the proof of Lemma 4. Then
each maximal ideal p containing (a1, . . . , an−2) has to be one of the pi’s. Check with this
change that the proof of Lemma 4 works for Noetherian domains in which all nonzero prime
ideals are maximal, so Theorem 2 is valid for such rings.
There is an extension of Theorem 2 to more than one vector. Given r ≤n vectors in
An, if they are the ﬁrst r rows of a matrix in GLn(A) then the r × r minors of the r × n
matrix formed from these (row) vectors will generate the unit ideal in A, as one sees by
expanding an n × n determinant as a linear combination of the r × r minors along the top.
The converse is also true for a ring A satisfying Theorem 2. A proof can be found in [2].
References
[1] I. Reiner, Unimodular Complements, Amer. Math. Monthly 63 (1956), 246–247.
[2] I. Reiner, Completion of Primitive Matrices, Amer. Math. Monthly 73 (1966), 380–381.
[3] J. Rotman, “Advanced Modern Algebra,” Prentice-Hall, Upper Saddle River, NJ, 2002.
[4] E. Schenkman, The Basis Theorem for Finitely Generated Abelian Groups, Amer. Math. Monthly 67
(1960), 770–771.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*