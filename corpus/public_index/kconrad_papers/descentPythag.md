# Descentpythag

> **Source**: https://kconrad.math.uconn.edu/blurbs/descentPythag.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PYTHAGOREAN DESCENT
KEITH CONRAD
1. Introduction
A Pythagorean triple is a triple of positive integers (a, b, c) such that a2 + b2 = c2.
Examples include (3, 4, 5), (5, 12, 13), and (6, 8, 10). A Pythagorean triple is called primitive
if a, b, and c have no common factor greater than 1. For example, (3, 4, 5) and (5, 12, 13) are
primitive while (6, 8, 10) is not. In any primitive Pythagorean triple one of a and b is odd
and the other is even: if a and b were both even then c would be even, violating primitivity,
and if a and b were both odd then c2 = a2 + b2 ≡1 + 1 ≡2 mod 4, which has no solution.
Since the roles of a and b are symmetric, we will assume throughout that b is even.
In 1934, Berggren [3] showed every primitive Pythagorean triple (a, b, c) with b even can
be generated from the triple (3, 4, 5) by a 3-fold ascent using the three matrices
(1.1)


1
−2
2
2
−1
2
2
−2
3

,


−1
2
2
−2
1
2
−2
2
3

,


1
2
2
2
1
2
2
2
3

.
Labeling the matrices in (1.1) as A, B, and C, respectively, the start of the ascent to new
primitive triples is illustrated in the diagram below, where the branches coming out of each
node from left to right are obtained by applying A, then B, then C.
(3,4,5)
A
B
C
(5,12,13)
(15,8,17)
(21,20,29)
A
B
C
(7,24,25)
(45,28,53)
(55,48,73)
A
B
C
(33,56,65)
(35,12,37)
(65,72,97)
A
B
C
(39,80,89)
(77,36,85)
(119,120,169)
Berggren discovered the matrices in (1.1) algebraically, as follows. Suppose (a, b, c) is a
solution to x2+y2 = z2. He sought a nonzero k that makes (a+k, b+k, c+k) another solution
1

<!-- page 2 -->
2
KEITH CONRAD
to this equation. From the two conditions a2 + b2 = c2 and (a + k)2 + (b + k)2 = (c + k)2,
we must have k = 2(c −a −b) (so k < 0 if a, b, and c are positive), and therefore
(1.2)


a + k
b + k
c + k

=


−a −2b + 2c
−2a −b + 2c
−2a −2b + 3c

=


−1
−2
2
−2
−1
2
−2
−2
3




a
b
c

.
The triples (−a, b, c), (a, −b, c), and (−a, −b, c) also satisfy x2 + y2 = z2, and if a nonzero
k is added to each coordinate of these in order to get another solution of x2 + y2 = z2, the
new triple in each case is a linear transformation of (a, b, c) by the matrices in (1.1). These
three matrices were rediscovered later by Barning [2, p. 3] and Hall [4, p. 377], based on the
same motivation as Berggren. They are also in an exercise with solution in [6, pp. 84-85].
We will describe Berggren’s tree of Pythagorean triples geometrically, using reﬂections
for the orthogonal group of x2 + y2 −z2. Each step of Berggren’s tree will be broken up
into 2 or 3 steps, each one involving a single reﬂection.
I thank Gabe Feinberg, Harold Erazo, and Pria Louka for comments and corrections.
2. Review of Reflections
In R3 we want to work out a formula for reﬂecting across a plane through the origin. To
each plane through the origin there is a unique orthogonal line through the origin. We’ll
describe how to reﬂect across the plane by using a vector on its orthogonal line.
Theorem 2.1. For any nonzero vector w ∈R3 let sw : R3 →R3 be the reﬂection across
the plane through the origin orthogonal to w. Then for all v ∈R3,
(2.1)
sw(v) = v −2 v · w
||w||2 w = v −2 v · w
w · ww.
Proof. The reﬂection sw should be linear, ﬁx the plane through the origin orthogonal to w,
and negate vectors on the line through w. Writing any v ∈R3 as aw + u, with a ∈R and
u ⊥w, we need
sw(v) = sw(aw) + sw(u) = −aw + u = aw + u −2aw = v −2aw.
Since v · w = (aw + u) · w = a(w · w), we can solve for a and obtain (2.1).
□
The formula for sw in (2.1) is written entirely in terms of the dot product, which is closely
related to the quadratic form x2 + y2 + z2 = (x, y, z) · (x, y, z) that provides R3 with its
usual notion of length. For a more general quadratic form Q(x, y, z) = ax2 + by2 + cz2 with
all nonzero coeﬃcients1 that might have negative values, we deﬁne its associated bilinear
form to be ⟨v, w⟩=
1
2(Q(v + w) −Q(v) −Q(w)) (when Q is the sum of squares, this
bilinear form is the dot product) Explicitly, if v = (x1, y1, z1) and w = (x2, y2, z2) then
⟨v, w⟩= ax1x2 + by1y2 + cz1z2. Using this bilinear form in place of the dot product, we can
promote (2.1) into a deﬁnition of reﬂections associated to Q: for each w ∈R3 such that
Q(w) ̸= 0,2 deﬁne sw : R3 →R3 by the formula
(2.2)
sw(v) = v −2 ⟨v, w⟩
⟨w, w⟩w.
1More generally, any nondegenerate quadratic form on R3 can be brought into the diagonal shape ax2 +
by2 + cz2 with all nonzero coeﬃcients by some linear change of variables.
2If Q is indeﬁnite, meaning it has coeﬃcients of both signs, then some nonzero w can have Q(w) = 0.
For instance, if Q(x, y, z) = x2 + y2 −z2 then Q(1, 1, 0) = 0.

<!-- page 3 -->
PYTHAGOREAN DESCENT
3
Here are some of properties of sw:
• sw : R3 →R3 is linear,
• sw(w) = −w and sw(v) = v if ⟨v, w⟩= 0,
• Q(sw(v)) = Q(v) for all v,
• sw(sw(v)) = v for all v.
The ﬁrst and second properties generalize properties of ordinary reﬂections, while the third
property is analogous to the length-preserving property of ordinary reﬂections. The third
property also tells us that if Q(v) = 0 then Q(sw(v)) = 0 as well, which is only interesting
when Q is indeﬁnite, and this is going to be exactly the type of quadratic form we work
with later. The fourth property makes inverting sw easy: it is its own inverse.
The orthogonal group of Q, denoted OQ(R), is the set of all linear transformations
A: R3 →R3 preserved by Q: Q(Av) = Q(v) for all v ∈R3. For instance, when Q(w) ̸= 0
the map sw in (2.2) belongs to the group OQ(R). The Cartan–Dieudonne theorem says
that every element of OQ(R) is a product of at most 3 reﬂections.3
3. The Orthogonal Group of x2 + y2 −z2.
We return to the Pythagorean equation a2+b2 = c2. Writing it as a2+b2−c2 = 0, we are
inspired to think about the quadratic form Q(x, y, z) = x2+y2−z2 and its orthogonal group
OQ(R). Barning [2] and Berggren [3] both observed that the matrices in (1.1) preserve Q,
but they didn’t say anything about them being reﬂections for Q.
We will use the reﬂections in OQ(R) associated to the ﬁve vectors e1 = (1, 0, 0), e2 =
(0, 1, 0), e3 = (0, 0, 1), e1 + e2 = (1, 1, 0), and e1 + e2 + e3 = (1, 1, 1), and denote them by
s1, s2, s3, s12, and s123. The ﬁrst three reﬂections are sign changes in coordinates:
(3.1)
s1(x, y, z) = (−x, y, z),
s2(x, y, z) = (x, −y, z),
s3(x, y, z) = (x, y, −z).
For example, (x, −y, −z) = s3(s2(x, y, z)) = s2(s3(x, y, z)). The reﬂection associated to
(1, 1, 0) is
(3.2)
s12(x, y, z) = (x, y, z) −(x + y)(1, 1, 0) = (−y, −x, z).
The reﬂection associated to (1, 1, 1) is
s123(x, y, z) = (x, y, z) −2(x + y −z)(1, 1, 1)
= (−x −2y + 2z, −2x −y + 2z, −2x −2y + 3z),
(3.3)
so the matrix for s123 is4
(3.4)


−1
−2
2
−2
−1
2
−2
−2
3

,
which is Berggren’s matrix in (1.2). The matrices in (1.1) are
(3.5)
A = s123s1,
B = s123s2,
C = s123s1s2,
3Cartan showed each orthogonal transformation of Rn with respect to the standard quadratic form
x2
1+· · ·+x2
n is a product of at most n reﬂections in Rn if n ≥2. See Theorem A.4 and the paragraph following
it in https://kconrad.math.uconn.edu/blurbs/grouptheory/isometryRn.pdf. Dieudonne generalized this
to other quadratic forms.
4Our matrix actions are all from the left, not right, so although we write vectors in coordinates as row
vectors, like (x, y, z), they need to be treated as column vectors when acted on by matrices.

<!-- page 4 -->
4
KEITH CONRAD
respectively5 This can be checked by a direct calculation, and it also follows from how
Berggren found the matrices in (1.1) by carrying out his algebraic idea with (3.4) on
(−a, b, c), (a, −b, c), and (−a, −b, c). Since reﬂections are their own inverse, A−1 = s1s123,
B−1 = s2s123, and C = s2s1s123.
The (a, b, c) ∈Z3 such that a2 + b2 = c2, allowing nonpositive coordinates, are the null
vectors of Q in Z3. A vector (a, b, c) ∈Z3 is called primitive when its coordinates have gcd 1,
so (3, 4, 5) and (3, −4, −5) are primitive null vectors of Q. Each element of OQ(Z) preserves
primitivity of an integral vector (more generally, it preserves the gcd of the coordinates of
an integral vector) since the inverse of a matrix in OQ(Z) is an integral matrix.
Theorem 3.1. Let Q(x, y, z) = x2 + y2 −z2. The group OQ(Z) acts transitively on the
primitive null vectors of Q in Z3.
Proof. We will prove this by descent, using reﬂections in OQ(Z) to decrease the overall size
of the coordinates of a vector.
Choose an integral vector (a, b, c) such that a2 + b2 = c2 and (a, b, c) ̸= (0, 0, 0). This
vector may have some negative coordinates, and by applying s1, s2, or s3 to (a, b, c) we can
make sign changes so that all the coordinates are nonnegative. Then from the condition
a2 + b2 = c2 we have 0 ≤a, b ≤c.
Assume neither a nor b is 0, so both are positive. Then
(3.6)
0 < a < c,
0 < b < c,
0 < c < a + b,
where the last inequality comes from c2 = a2 + b2 < a2 + 2ab + b2 = (a + b)2.
Let’s pass from (a, b, c) to s123(a, b, c) using (3.4).
The coordinates of this reﬂection
satisfy
(3.7)
−a < −a −2b + 2c < a,
−b < −2a −b + 2c < b,
−c < −2a −2b + 3c < c,
since each of these inequalities is equivalent to one of the inequalities in (3.6) except for
−c < −2a −2b + 3c, which is equivalent to a + b < 2c and that is immediate from a < c
and b < c in (3.6).
By (3.7), the coordinates of s123(a, b, c) are, in absolute value, less than the corresponding
coordinates of (a, b, c). Apply the reﬂections si to make the new coordinates all nonnegative
and then, if neither of the ﬁrst two coordinates is 0, use the reﬂection s123 once again to
shrink the absolute value of the coordinates further. Eventually we must reach an integral
null vector for Q with one of the ﬁrst two coordinates being 0. That means it has the form
(a, 0, ±a) or (0, b, ±b). If we had started oﬀwith a primitive null vector then every null
vector we produce using reﬂections is primitive too, so the ﬁnal primitive null vector with
ﬁrst or second coordinate 0 is one of the following:
(1, 0, 1), (1, 0, −1), (−1, 0, 1), (−1, 0, −1), (0, 1, 1), (0, 1, −1), (0, −1, 1), (0, −1, −1).
Using the reﬂections s1, s2, and s3, which create sign changes, all of these vectors can be
reached from (1, 0, 1) or (0, 1, 1), and we can pass from (1, 0, 1) to (0, 1, 1) using s2s12 (the
general eﬀect of s12 is in (3.2)), so the primitive integral null vectors for Q are all in the
same orbit of OQ(Z). In particular, applying elements of OQ(Z) to the primitive triple
(3, 4, 5) will lead to every primitive Pythagorean triple.
□
Example 3.2. Let v = (9, 40, 41), which is a primitive Pythagorean triple.
Step 1: s123(v) = (−7, 24, 25), so we pass to s1s123(v) = (7, 24, 25).
5We can also write C as s123s2s1 since s1 and s2 commute.

<!-- page 5 -->
PYTHAGOREAN DESCENT
5
Step 2: s123(7, 24, 25) = (−5, 12, 13), so we pass to s1s123(7, 24, 25) = (5, 12, 13).
Step 3: s123(5, 12, 13) = (−3, 4, 5), so we pass to s1s123(5, 12, 13) = (3, 4, 5).
Since A = s123s1 by (3.5) and reﬂections are their own inverse, A−1 = s1s123. Thus
(3, 4, 5) = A−1(5, 12, 13) = A−2(7, 24, 25) = A−3(9, 40, 41),
so
(9, 40, 41) = A3(3, 4, 5),
where A is the ﬁrst matrix in (1.1). The appearance of A3 here means that if we extend
Berggren’s tree on the ﬁrst page one more step then we’d see (9, 40, 41) at the top of the
next column.
Example 3.3. Let v = (65, 72, 97), which is a primitive Pythagorean triple.
Step 1: s123(v) = (−15, −8, 17), so s1s2s123(v) = (15, 8, 17).
Step 2: s123(15, 8, 17) = (3, −4, 5), so s2s123(15, 8, 17) = (3, 4, 5).
Thus (3, 4, 5) = (s2s123)(s1s2s123)(65, 72, 97) = B−1C−1(65, 72, 97), so
(65, 72, 97) = CB(3, 4, 5),
and this is consistent with the location of (65, 72, 97) in the tree on the ﬁrst page.
Here is a proof that Berggren’s tree has every primitive Pythagorean triple exactly once.
Corollary 3.4 (Berggren). Each primitive Pythagorean triple (a, b, c) with even b is ob-
tained from (3, 4, 5) by applying to it a product of matrices g1g2 · · · gm where each gi is A,
B, or C in (1.1), and this product is unique6: if
g1g2 · · · gm(3, 4, 5) = g′
1g′
2 · · · g′
n(3, 4, 5),
where gi, g′
j ∈{A, B, C} then m = n and gi = g′
i for all i.
Proof. From the proof of Theorem 3.1, a primitive Pythagorean triple (a, b, c) can be brought
down to (1, 0, 1) or (0, 1, 1) using only s1, s2, and s123 provided that for positive a, b, c the
triple s123(a, b, c) has a positive third coordinate, since it makes applying s3 unnecessary.
Showing s123(a, b, c) has a positive third coordinate is equivalent to showing
3c
?> 2a + 2b.
If we square both sides and use c2 = a2 + b2, this inequality is the same as
9c2 > 4(a + b)2 ⇐⇒9(a2 + b2) > 4(a2 + b2 + 2ab) ⇐⇒a2 + b2 > 8
5ab ⇐⇒a
b + b
a > 8
5.
By calculus, t + 1/t ≥2 for t > 0, and 2 > 8/5, so 3c > 2a + 2b in any Pythagorean triple
(a, b, c).
In contrast to the third coordinate of s123(a, b, c) being positive when a, b, and c are
positive, we will show one of the ﬁrst two coordinates of s123(a, b, c) is negative.
(For
example, look at the eﬀect of s123 in each step of Examples 3.2 and 3.3.) Assume, to the
contrary, that the ﬁrst two coordinates of s123(a, b, c) are both nonnegative. By the formula
for s123 in (3.3), −a −2b + 2c ≥0 and −2a −b + 2c ≥0, which can be rewritten as
a + 2b ≤2c,
2a + b ≤2c.
Since a, b, and c are positive, squaring each of these inequalities implies
a2 + 4ab + 4b2 ≤4c2,
4a2 + 4ab + b2 ≤4c2.
6To get (3, 4, 5) itself we apply the empty product with m = 0.

<!-- page 6 -->
6
KEITH CONRAD
Since c2 = a2 + b2, we get
4ab ≤3a2,
4ab ≤3b2,
so 4b ≤3a and 4a ≤3b. Adding these, 4(a + b) ≤3(a + b), which is false since a + b > 0.
Since s1, s2, and s123 don’t change the parity of the middle coordinate, if b is even then
(a, b, c) is eventually brought down to (1, 0, 1), not (0, 1, 1):
(3.8)
(1, 0, 1) = gm · · · g2g1(a, b, c),
where each gi is s1, s2, or s123. More precisely, this product of gi’s is built from products
s1s123, s2s123, and s1s2s123, where the reﬂections s1 and s2 serve to make all coordinates
positive before the descent continues (see Examples 3.2 and 3.3).
There is an s1 or s2
(or both) after each application of s123 because at least one of the ﬁrst two coordinates of
s123(a, b, c) is negative if a, b, and c are all positive.
We can bring the reﬂections gi in (3.8) from the right side to the left side by inverting
them. A reﬂection is its own inverse, so
(3.9)
(a, b, c) = g1g2 · · · gm(1, 0, 1).
Here the product of gi’s is built from products of (s1s123)−1 = s123s1 = A, (s2s123)−1 =
s123s2 = B, and (s1s2s123)−1 = s123s2s1 = C. Because A(1, 0, 1) = (3, 4, 5), B(1, 0, 1) =
(1, 0, 1), and C(1, 0, 1) = (3, 4, 5), if the left side of (3.9) has a, b, c > 0 then the right
side can’t be a product only of B’s. Therefore g1g2 · · · gm(1, 0, 1) can be rewritten to have
(3, 4, 5) at the start (right end) by combining (1, 0, 1) with the ﬁrst A or C that is applied to
it. This proves every primitive Pythagorean triple with even b appears in Berggren’s tree.
Our last step is to show each primitive triple occurs just once in the tree. It suﬃces to
show each triple (a, b, c) with even b other than (3, 4, 5) has a unique parent in the tree: if
(a, b, c) ̸= (3, 4, 5) then just one of the three triples
A−1(a, b, c) = s1s123(a, b, c), B−1(a, b, c) = s2s123(a, b, c), and C−1(a, b, c) = s1s2s123(a, b, c)
has all positive coordinates. We already showed s123(a, b, c) has a positive third coordinate
and its ﬁrst two coordinates are not both ≥0. Therefore just one of s1, s2, or s1s2 applied
to s123(a, b, c) produces a triple with all positive coordinates unless s123(a, b, c) has one of its
ﬁrst two coordinates equal to 0. Since s123(a, b, c) is primitive with even second coordinate,
we must have s123(a, b, c) = (−1, 0, 1), so (a, b, c) = s123(−1, 0, 1) = (3, 4, 5).
□
Remark 3.5. Since A−1 = s1s123, B−1 = s2s123, and C−1 = s1s2s123 are all s123 followed
by (not preceded by!) sign changes on one or both of the ﬁrst two coordinates, if you want
to descend the tree from a speciﬁed primitive Pythagorean triple (a, b, c) all the way down
to (3, 4, 5), it doesn’t matter which of A−1, B−1, or C−1 you apply to (a, b, c). All three
results will be the same up to sign changes, so after applying any of them simply pass to
the absolute values of the coordinates (that is eﬀectively applying s1, s2, or s1s2) and then
repeat the process.
Corollary 3.6. The group OQ(Z) is generated by the ﬁve reﬂections
s1,
s2,
s3,
s123,
s12.
Proof. The proof of Theorem 3.1 used only these ﬁve reﬂections to carry any primitive null
vector of Q in Z3 to (1, 0, 1), so OQ(Z) is generated by these reﬂections and the matrices
ﬁxing (1, 0, 1).
Therefore it remains to show that the stabilizer subgroup of (1, 0, 1) in
OQ(Z) lies in the group generated by the ﬁve reﬂections.

<!-- page 7 -->
PYTHAGOREAN DESCENT
7
A calculation (see the Appendix) shows the stabilizer of (1, 0, 1) in OQ(Z) consists of
matrices of the form


1 −2m2
−2m
2m2
2m
1
−2m
−2m2
−2m
1 + 2m2


or


1 −2m2
2m
2m2
2m
−1
−2m
−2m2
2m
1 + 2m2


for m ∈Z. The ﬁrst matrix is (s2s123)m and the second matrix is (s2s123)ms2.
□
We used s12 only to link (1, 0, 1) and (0, 1, 1) at the end of the proof of Theorem 3.1. The
other four reﬂections in the generating set all reduce to the identity mod 2, so the subgroup
of OQ(Z) they generate can’t send (1, 0, 1) to (0, 1, 1), or (3, 4, 5) to (4, 3, 5).
4. Other Matrices Generating Pythagorean Triples
In the literature there are other methods of generating primitive Pythagorean triples
using matrices. We present two of them.
Method 1: Price [5] used the following three 3 × 3 matrices to generate the primitive
Pythagorean triples starting from (3, 4, 5):
(4.1)


2
1
−1
−2
2
2
−2
1
3

,


2
1
1
2
−2
2
2
−1
3

,


2
−1
1
2
2
2
2
1
3

.
Calling these A′, B′, and C′, we have the following start to an alternate tree of triples.
(3,4,5)
A′
B′
C′
(5,12,13)
(15,8,17)
(7,24,25)
A′
B′
C′
(9,40,41)
(35,12,37)
(11,60,61)
A′
B′
C′
(21,20,29)
(55,48,73)
(39,80,89)
A′
B′
C′
(13,84,85)
(63,16,65)
(15,112,113)
Price writes at the end of [5] that this method of generating Pythagorean triples is “less
geometric” than Berggren’s matrices, but A′, B′, and C′ can be interpreted geometrically.
Each has determinant ±8, so they don’t preserve Q(x, y, z) = x2 + y2 −z2, but they almost
preserve it: Q(A′v) = 4Q(v), Q(B′v) = 4Q(v), and Q(C′v) = 4Q(v) for all v in R3.
Therefore A′, B′, and C′ preserve the cone x2 + y2 −z2 = 0, where Pythagorean triples lie.
A short search reveals how to write B′ and C′ in terms of A′ and reﬂections in OQ(Z):
B′ = s1A′s1s2,
C′ = s123s1A′.

<!-- page 8 -->
8
KEITH CONRAD
Method 2: Instead of working in R3, Alperin [1] uses the 3-dimensional space N of 2 × 2
matrices ( s
t
u −s ) with trace 0, equipped with the quadratic form Q′( s
t
u −s ) = s2 + tu =
−det( s
t
u −s ). The subset of matrices in N with determinant 0 is the replacement for the
cone {(x, y, z) : x2 + y2 −z2 = 0} in R3.
The quadratic spaces (R3, Q) and (N, Q′)
are isomorphic by f(x, y, z) = (
y
x−z
x+z
y ), and primitive integral solutions to a2 + b2 = c2
correspond to integral matrices ( m
n
k −m ) where m2+nk = 0 and gcd(m, n, k) = 2. Berggren’s
three matrices (1.1) appear on [1, p. 813]: U−is A, L+ is B, and U+ is C.
Appendix A. Calculating the Stabilizer of (1, 0, 1).
We will calculate the stabilizer of (1, 0, 1) in OQ(Z), for the proof of Corollary 3.6. Since
Q(v) = v · Jv, where J = diag(1, 1, −1), we have OQ(R) = {M ∈M3(R) : M⊤JM = J}.
From M ﬁxing (1, 0, 1), it has the form
M =


a
b
1 −a
c
d
−c
e
f
1 −e

.
The condition M⊤JM = J implies
a2 + c2 −e2 = 1,
(A.1)
ab + cd −ef = 0,
(A.2)
−a2 + a −c2 + e2 −e = 0,
(A.3)
b2 + d2 −f2 = 1,
(A.4)
−ab −cd + ef + b −f = 0.
(A.5)
Adding (A.1) and (A.3), e = a −1. Adding (A.2) and (A.5), f = b, and feeding that into
(A.4) gives us d2 = 1, so d = ±1. Substituting these into (A.1) and (A.2) gives us
c2 + 2a −2 = 0,
cd + b = 0.
Thus a = 1 −c2/2 and b = −cd, so
(A.6)
M =


1 −c2/2
−cd
c2/2
c
d
−c
−c2/2
−cd
1 + c2/2

.
Conversely, any such matrix ﬁxes (1, 0, 1) and satisﬁes M⊤JM = J (this requires d2 = 1),
so (A.6) describes the stabilizer of (1, 0, 1) in OQ(R). To be in OQ(Z) requires c to be an
even number. Writing c = 2m with m ∈Z, (A.6) becomes
(A.7)


1 −2m2
−2md
2m2
2m
d
−2m
−2m2
−2md
1 + 2m2


where d = ±1. When d = m = 1 this is


−1
−2
2
2
1
−2
−2
−2
3

= s2s123.

<!-- page 9 -->
PYTHAGOREAN DESCENT
9
When d = 1, the matrix in (A.7) is (s2s123)m, and when d = −1 it is (s2s123)ms2.
References
[1] R. C. Alperin, The Modular Tree of Pythagoras, Amer. Math. Monthly 112 (2005), 807–816.
[2] F. J. M. Barning, Over Pythagorese en bijna-Pythagorese driehoeken en een generatieproces met behulp
van unimodulaire matrices, Math. Centrum, Amsterdam, Dept. Pure Math. ZW-011 (1963), 37 pages.
[3] B. Berggren, Pytagoreiska trianglar, Tidskrift f¨or Element¨ar Matematik, Fysik och Kemi 17 (1934),
129–139.
[4] A. Hall, Genealogy of Pythagorean Triads, The Math. Gazette 54 (1970), 377–379.
[5] H. L. Price, The Pythagorean Tree: A New Species, http://arxiv.org/abs/0809.4324.
[6] J. Roberts, “Elementary Number Theory: A Problem Oriented Approach,” MIT Press, Cambridge, MA
1977.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*