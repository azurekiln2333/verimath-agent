# Isometryrn

> **Source**: https://kconrad.math.uconn.edu/blurbs/isometryRn.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
ISOMETRIES OF Rn
KEITH CONRAD
1. Introduction
An isometry of Rn is a function h: Rn →Rn that preserves the distance between vectors:
||h(v) −h(w)|| = ||v −w||
for all v and w in Rn, where ||(x1, . . . , xn)|| =
p
x2
1 + · · · + x2n.
Example 1.1. The identity transformation: id(v) = v for all v ∈Rn.
Example 1.2. Negation: −id(v) = −v for all v ∈Rn.
Example 1.3. Translation: ﬁxing u ∈Rn, let tu(v) = v + u. Easily ||tu(v) −tu(w)|| =
||v −w||.
Example 1.4. Rotations around points and reﬂections across lines in the plane are isome-
tries of R2. Formulas for these isometries will be given in Example 3.3 and Section 4.
The eﬀects of a translation, rotation (around the origin) and reﬂection across a line in
R2 are pictured below on sample line segments.
The composition of two isometries of Rn is an isometry. Is every isometry invertible? It
is clear that the three kinds of isometries pictured above (translations, rotations, reﬂections)
are each invertible (translate by the negative vector, rotate by the opposite angle, reﬂect a
second time across the same line).
In Section 2, we show the close link between isometries and the dot product on Rn,
which is more convenient to use than distances due to its algebraic properties. Section 3
is about the matrices that act as isometries on on Rn, called orthogonal matrices. Section
4 describes the isometries of R and R2 geometrically. In Appendix A, we will look more
closely at reﬂections in Rn.
1

<!-- page 2 -->
2
KEITH CONRAD
2. Isometries, dot products, and linearity
Using translations, we can reduce the study of isometries of Rn to the case of isometries
ﬁxing 0.
Theorem 2.1. Every isometry of Rn can be uniquely written as the composition t◦k where
t is a translation and k is an isometry ﬁxing the origin.
Proof. Let h: Rn →Rn be an isometry. If h = tw ◦k, where tw is translation by a vector
w and k is an isometry ﬁxing 0, then for all v in Rn we have h(v) = tw(k(v)) = k(v) + w.
Setting v = 0 we get w = h(0), so w is determined by h. Then k(v) = h(v)−w = h(v)−h(0),
so k is determined by h. Turning this around, if we deﬁne t(v) = v + h(0) and k(v) =
h(v)−h(0), then t is a translation, k is an isometry ﬁxing 0, and h(v) = k(v)+h(0) = tw◦k,
where w = h(0).
□
Theorem 2.2. For a function h: Rn →Rn, the following are equivalent:
(1) h is an isometry and h(0) = 0,
(2) h preserves dot products: h(v) · h(w) = v · w for all v, w ∈Rn.
Proof. The link between length and dot product is the formula
||v||2 = v · v.
Suppose h satisﬁes (1). Then for any vectors v and w in Rn,
(2.1)
||h(v) −h(w)|| = ||v −w||.
As a special case, when w = 0 in (2.1) we get ||h(v)|| = ||v|| for all v ∈Rn. Squaring both
sides of (2.1) and writing the result in terms of dot products makes it
(h(v) −h(w)) · (h(v) −h(w)) = (v −w) · (v −w).
Carrying out the multiplication,
(2.2)
h(v) · h(v) −2h(v) · h(w) + h(w) · h(w) = v · v −2v · w + w · w.
The ﬁrst term on the left side of (2.2) equals ||h(v)||2 = ||v||2 = v · v and the last term on
the left side of (2.2) equals ||h(w)||2 = ||w||2 = w · w. Canceling equal terms on both sides
of (2.2), we obtain −2h(v) · h(w) = −2v · w, so h(v) · h(w) = v · w.
Now assume h satisﬁes (2), so
(2.3)
h(v) · h(w) = v · w
for all v and w in Rn. Therefore
||h(v) −h(w)||2 = (h(v) −h(w)) · (h(v) −h(w))
= h(v) · h(v) −2h(v) · h(w) + h(w) · h(w)
= v · v −2v · w + w · w by (2.3)
= (v −w) · (v −w)
= ||v −w||2,
so ||h(v) −h(w)|| = ||v −w||. Thus h is an isometry. Setting v = w = 0 in (2.3), we get
||h(0)||2 = 0, so h(0) = 0.
□
Corollary 2.3. The only isometry of Rn ﬁxing 0 and the standard basis is the identity.

<!-- page 3 -->
ISOMETRIES OF Rn
3
Proof. Let h: Rn →Rn be an isometry that satisﬁes
h(0) = 0, h(e1) = e1, . . . , h(en) = en.
Theorem 2.2 says
h(v) · h(w) = v · w
for all v and w in Rn. Fix v ∈Rn and let w run over the standard basis vectors e1, e2, . . . , en,
so we see
h(v) · h(ei) = v · ei.
Since h ﬁxes each ei,
h(v) · ei = v · ei.
Writing v = c1e1 + · · · + cnen, we get
h(v) · ei = ci
for all i, so h(v) = c1e1 + · · · + cnen = v. As v was arbitrary, h is the identity on Rn.
□
It is essential in Corollary 2.3 that the isometry ﬁxes 0. An isometry of Rn ﬁxing the
standard basis without ﬁxing 0 need not be the identity! For example, reﬂection across the
line x + y = 1 in R2 is an isometry of R2 ﬁxing (1, 0) and (0, 1) but not 0 = (0, 0). See
below.
Theorem 2.4. For a function h: Rn →Rn, the following are equivalent:
(1) h is an isometry and h(0) = 0,
(2) h is linear, and the matrix A such that h(v) = Av for all v ∈Rn satisﬁes AA⊤= In.
Proof. Suppose h is an isometry and h(0) = 0. We want to prove linearity: h(v + w) =
h(v)+h(w) and h(cv) = ch(v) for all v and w in Rn and all c ∈R. The mapping h preserves
dot products by Theorem 2.2:
h(v) · h(w) = v · w
for all v and w in Rn. For the standard basis e1, . . . , en of Rn this says h(ei) · h(ej) =
ei · ej = δij, so h(e1), . . . , h(en) is an orthonormal basis of Rn. Thus two vectors in Rn are
equal if they have the same dot product with each of h(e1), . . . , h(en).
For all u in Rn we have
h(v + w) · h(u) = (v + w) · u
and
(h(v) + h(w)) · h(u) = h(v) · h(u) + h(w) · h(u) = v · u + w · u = (v + w) · u,

<!-- page 4 -->
4
KEITH CONRAD
so h(v + w) · h(u) = (h(v) + h(w)) · h(u) for all u. Letting u = e1, . . . , en shows h(v + w) =
h(v) + h(w). Similarly,
h(cv) · h(u) = (cv) · u = c(v · u) = c(h(v) · h(u)) = (ch(v)) · h(u),
so again letting u run through e1, . . . , en tells us h(cv) = ch(v). Thus h is linear.
Let A be the matrix for h: h(v) = Av for all v ∈Rn, where A has jth column h(ej). We
want to show AA⊤= In. Since h preserves dot products, the condition h(v) · h(w) = v · w
for all v, w ∈Rn says Av · Aw = v · w. The fundamental link between the dot product and
matrix transposes, which you should check, is that we can move a matrix to the other side
of a dot product by using its transpose:
(2.4)
v · Mw = M⊤v · w
for every n × n matrix M and v, w ∈Rn. Using M = A and Av in place of v in (2.4),
Av · Aw = A⊤(Av) · w = (A⊤A)v · w.
This is equal to v · w for all v and w, so (A⊤A)v · w = v · w for all v and w in Rn. Since
the (i, j) entry of a matrix M is Mej · ei, letting v and w run through the standard basis of
Rn tells us A⊤A = In, so A is invertible. An invertible matrix commutes with its inverse,
so A⊤A = In ⇒AA⊤= In.
For the converse, assume h(v) = Av for v ∈Rn where AA⊤= In. Trivially h ﬁxes 0. To
show h is an isometry, by Theorem 2.2 it suﬃces to show
(2.5)
Av · Aw = v · w
for all v, w ∈Rn. Since A and its inverse A⊤commute, we have A⊤A = In, so Av · Aw =
A⊤(Av) · w = (A⊤A)v · w = v · w.
□
Corollary 2.5. Isometries of Rn are invertible, the inverse of an isometry is an isometry,
and two isometries on Rn that have the same values at 0 and any basis of Rn are equal.
This gives a second proof of Corollary 2.3 as a special case.
Proof. Let h: Rn →Rn be an isometry. By Theorem 2.1, h = k + h(0) where k is an
isometry of Rn ﬁxing 0. Theorem 2.4 tells us there is an invertible matrix A such that
k(v) = Av for all v ∈Rn, so
h(v) = Av + h(0).
This has inverse h−1(v) = A−1(v −h(0)). In particular, h is surjective.
The isometry condition ||h(v)−h(w)|| = ||v−w|| for all v and w in Rn implies ||v−w|| =
||h−1(v) −h−1(w)|| for all v and w in Rn by replacing v and w in the isometry condition
with h−1(v) and h−1(w). Thus h−1 is an isometry of Rn.
If h1 and h2 are isometries of Rn that are equal on 0 and a basis then the functions
k1(v) = h1(v) −h1(0) and k2(v) = h2(v) −h2(0) are linear and are equal on that basis, so
by linearity k1 = k2 on Rn. That is, h1(v) −h1(0) = h2(v) −h2(0) for all v in Rn. Since
h1(0) = h2(0) we get h1 = h2 on Rn.
□
Remark 2.6. That isometries of Rn ﬁxing 0 are linear and invertible is a special case of
the following more general result: for a ﬁnite-dimensional vector space V over an arbitrary
ﬁeld and a nondegenerate bilinear form B on V , a function A: V →V for which B(v, w) =
B(A(v), A(w)) for all v and w in V must be linear and invertible. A more general version
of this is due to A. Vogt [3, Lemma 1.5, Theorem 2.4], and a proof can be found there
or in my answer at https://math.stackexchange.com/questions/137139. A physically

<!-- page 5 -->
ISOMETRIES OF Rn
5
interesting example of this over R besides Rn with its usual dot product is 4-dimensional
space (x, y, z, ct) with the indeﬁnite bilinear form associated to x2 +y2 +z2 −c2t2 in special
relativity (Minkowski spacetime).
Deﬁnition 2.7. In Rn, a set of n + 1 points P0, P1, . . . , Pn is said to be in general position
if they don’t all lie in a hyperplane.
This concept abstracts the idea of 3 points in R2 not being collinear. In the deﬁnition,
the hyperplanes in Rn are translated subspaces of dimension n −1, so they need not pass
through the origin. For example, a line in R2 need not be a linear subspace of R2 since a
line doesn’t have to contain the origin. Three points in R2 are in general position if no line
passes through all of them and four points in R3 are in general position if no plane passes
through all of them. Saying P0, P1, . . . , Pn are in general position in Rn does not mean these
n + 1 points are linearly independent as vectors in Rn, but rather that the n diﬀerences
P1 −P0, . . . , Pn −P0 are linearly independent vectors: a nontrivial linear relation would
place these n diﬀerences, along with 0, in a common subspace of dimension n−1, so adding
P0 to all of the diﬀerences and to 0 would put P0, P1, . . . , Pn in a common hyperplane.
Adding a common vector to points in general position keeps them in general position
since the added vector cancels out when taking diﬀerences.
Corollary 2.8. Let P0, P1, . . . , Pn be n + 1 points in Rn in “general position”. Two isome-
tries of Rn that are equal at P0, . . . , Pn are the same.
Proof. We know isometries of Rn are invertible. If h1 and h2 are isometries of Rn with the
same values at each Pi then h−1
2
◦h1 is an isometry that ﬁxes each Pi. Therefore to prove
h1 = h2 it suﬃces to show an isometry of Rn that ﬁxes P0, . . . , Pn is the identity.
Let h be an isometry of Rn such that h(Pi) = Pi for 0 ≤i ≤n. Set t(v) = v −P0, which
is a translation. Then tht−1 is an isometry with formula
(tht−1)(v) = h(v + P0) −P0.
Thus (tht−1)(0) = h(P0)−P0 = 0, so tht−1 is linear by Theorem 2.4. Also (tht−1)(Pi−P0) =
h(Pi) −P0 = Pi −P0.
Since P0, . . . , Pn are in general position, the diﬀerences P1 −P0, . . . , Pn −P0 form a basis
of Rn. Therefore by Corollary 2.5, tht−1 is the identity, so h is the identity.
□
3. Orthogonal matrices
We have seen that the isometries of Rn that ﬁx 0 come from matrices A such that
AA⊤= In. These matrices have a name.
Deﬁnition 3.1. An n × n matrix A is called orthogonal if AA⊤= In, or equivalently if
A⊤A = In.
A matrix is orthogonal when its transpose is its inverse.
Since det(A⊤) = det A, an
orthogonal matrix A satisﬁes (det A)2 = 1, so det A = ±1. (For n ≥2 not all matrices with
determinant ±1 are orthogonal, such as ( 3 1
5 2 ). The orthogonal 1 × 1 matrices are ±1.)
Example 3.2. Negation on Rn (Example 1.2) is an isometry that is described by the
matrix −In, which is orthogonal: (−In)(−In)⊤= (−In)(−In) = In.
Example 3.3. Let n = 2.
By algebra, AA⊤= I2 if and only if A = ( a −εb
b
εa ), where
a2+b2 = 1 and ε = ±1. Writing a = cos θ and b = sin θ, we get the matrices ( cos θ −sin θ
sin θ
cos θ ) and

<!-- page 6 -->
6
KEITH CONRAD
( cos θ
sin θ
sin θ −cos θ ). Algebraically, these types of matrices are distinguished by their determinants:
the ﬁrst type has determinant 1 and the second type has determinant −1.
The geometric eﬀects of these two types of matrices diﬀer. Below on the left, ( cos θ −sin θ
sin θ
cos θ )
is a counterclockwise rotation by angle θ around the origin. Below on the right, ( cos θ
sin θ
sin θ −cos θ )
is a reﬂection across the line through the origin at angle θ/2 with respect to the positive
x-axis. (Check ( cos θ
sin θ
sin θ −cos θ ) squares to the identity, as any reﬂection should.)
v
w
A(v)
A(w)
A = ( cos θ −sin θ
sin θ
cos θ )
v
w
A(v)
A(w)
A = ( cos θ
sin θ
sin θ −cos θ )
Let’s explain why ( cos θ
sin θ
sin θ −cos θ ) is a reﬂection at angle θ/2. See the ﬁgure below. Pick a
line L through the origin, say at an angle ϕ with respect to the positive x-axis. To ﬁnd a
formula for reﬂection across L, we’ll use a basis of R2 with one vector on L and the other
vector perpendicular to L. The unit vector u1 =
 cos ϕ
sin ϕ

lies on L and the unit vector
u2 =
 −sin ϕ
cos ϕ

is perpendicular to L. For any v ∈R2, write v = c1u1 + c2u2 with c1, c2 ∈R.
u1
L
ϕ
u2
v
c1u1
c2u2
−c2u2
s(v)
The reﬂection of v across L is s(v) = c1u1 −c2u2. Writing a = cos ϕ and b = sin ϕ (so
a2 + b2 = 1), in standard coordinates this becomes
(3.1)
v = c1u1 + c2u2 = c1
a
b

+ c2
−b
a

=

c1a −c2b
c1b + c2a

=

a
−b
b
a
 
c1
c2


<!-- page 7 -->
ISOMETRIES OF Rn
7
and in a similar way
s(v) = c1u1 −c2u2
=

a
b
b
−a
 
c1
c2

=

a
b
b
−a
 
a
−b
b
a
−1
v
by (3.1)
=

a
b
b
−a
 
a
b
−b
a

v
=

a2 −b2
2ab
2ab
−(a2 −b2)

v.
By the sine and cosine duplication formulas, the last matrix is ( cos(2ϕ)
sin(2ϕ)
sin(2ϕ) −cos(2ϕ) ). Therefore
( cos θ
sin θ
sin θ −cos θ ) is a reﬂection across the line through the origin at angle θ/2.
We return to orthogonal n × n matrices for any n ≥1. The geometric meaning of the
condition A⊤A = In is that the columns of A are mutually perpendicular unit vectors
(check!). From this we see how to create orthogonal matrices: starting with an orthonormal
basis of Rn, an n×n matrix having this basis as its columns (in any order) is an orthogonal
matrix, and all n × n orthogonal matrices arise in this way.
Let On(R) denote the set of n × n orthogonal matrices:
(3.2)
On(R) = {A ∈GLn(R) : AA⊤= In}.
Theorem 3.4. The set On(R) is a group under matrix multiplication.
Proof. Clearly In ∈On(R). If A and B are in On(R), then
(AB)(AB)⊤= ABB⊤A⊤= AA⊤= In,
so AB ∈On(R). For A ∈On(R), we have A−1 = A⊤and
(A−1)(A−1)⊤= A⊤(A⊤)⊤= A⊤A = In.
Therefore A−1 ∈On(R).
□
The link between isometries and dot products (Theorem 2.2) gives us a more geometric
description of On(R) than (3.2):
(3.3)
On(R) = {A ∈GLn(R) : Av · Aw = v · w for all v, w ∈Rn}.
The label “orthogonal matrix” is very unfortunate. It suggests that such matrices should
be the ones that preserve orthogonality of vectors:
(3.4)
v · w = 0 =⇒Av · Aw = 0
for all v and w in Rn. While orthogonal matrices do satisfy (3.4), since (3.4) is a special
case of the condition Av · Aw = v · w in (3.3), many matrices satisfy (3.4) and are not
orthogonal matrices! That is, orthogonal matrices (which, by deﬁnition, preserve all dot
products) are not the only matrices that preserve orthogonality of vectors (dot products
equal to 0). A simple example of a nonorthogonal matrix satisfying (3.4) is a scalar matrix
cIn, where c ̸= ±1. Since (cv) · (cw) = c2(v · w), cIn does not preserve dot products in
general but it does preserve dot products equal to 0. It’s natural to ask which matrices

<!-- page 8 -->
8
KEITH CONRAD
besides orthogonal matrices preserve orthogonality. Here is the complete answer, which
shows they are not that far from being orthogonal.
Theorem 3.5. An n × n real matrix A satisﬁes (3.4) if and only if A is a scalar multiple
of an orthogonal matrix.
Proof. If A = cA′ where A′ is orthogonal, then Av · Aw = c2(A′v · A′w) = c2(v · w), so if
v · w = 0 then Av · Aw = 0.
Now assume A satisﬁes (3.4). Then the vectors Ae1, . . . , Aen are mutually perpendicular,
so the columns of A are perpendicular to each other. We want to show that they have the
same length.
Note that ei + ej ⊥ei −ej when i ̸= j, so by (3.4) and linearity Aei + Aej ⊥Aei −Aej.
Writing this in the form (Aei + Aej) · (Aei −Aej) = 0 and expanding, we are left with
Aei · Aei = Aej · Aej, so ||Aei|| = ||Aej||.
Therefore the columns of A are mutually
perpendicular vectors with the same length. Call this common length c. If c = 0 then
A = O = 0·In. If c ̸= 0 then the matrix (1/c)A has an orthonormal basis as its columns, so
it is an orthogonal matrix. Therefore A = c((1/c)A) is a scalar multiple of an orthogonal
matrix.
□
Since a composition of isometries is an isometry and isometries are invertible with the
inverse of an isometry being an isometry, isometries form a group under composition. We
will describe the elements of this group and show how the group law looks in that description.
Theorem 3.6. For A ∈On(R) and w ∈Rn, the function hA,w : Rn →Rn given by
hA,w(v) = Av + w = (twA)(v)
is an isometry. Moreover, every isometry of Rn has this form for unique A and w.
Proof. The indicated formula always gives an isometry, since it is the composition of a
translation and orthogonal matrix transformation, which are both isometries.
To show every isometry of Rn has the form hA,w for some A and w, let h: Rn →Rn be
an isometry. By Theorem 2.1, h = k +h(0) where k is an isometry of Rn ﬁxing 0. Theorem
2.4 tells us there is an A ∈On(R) such that k(v) = Av for all v ∈Rn, so
h(v) = k(v) + h(0) = Av + h(0) = hA,w(v),
where w = h(0).
If hA,w = hA′,w′ as functions on Rn, then evaluating both sides at 0 gives w = w′.
Therefore Av + w = A′v + w for all v, so Av = A′v for all v, which implies A = A′.
□
Let Iso(Rn) denote the group of isometries of Rn. Its elements have the form hA,w by
Theorem 3.6. Here is what composition of such mappings looks like:
hA,w(hA′,w′(v)) = A(A′v + w′) + w
= AA′v + Aw′ + w
= hAA′,Aw′+w(v).
This is similar to the multiplication law in the ax + b group:

a
b
0
1
 
a′
b′
0
1

=

aa′
ab′ + b
0
1

.
In fact, if we write an isometry hA,w ∈Iso(Rn) as an (n + 1) × (n + 1) matrix ( A w
0 1 ), where
the 0 in the bottom is a row vector of n zeros, then the composition law in Iso(Rn) is

<!-- page 9 -->
ISOMETRIES OF Rn
9
multiplication of the corresponding (n+1)×(n+1) matrices, so Iso(Rn) can be viewed as a
subgroup of GLn+1(R), acting on Rn as the column vectors
 v
1

in Rn+1 (not a subspace!).
4. Geometric description of isometries of R and R2
Let’s classify the isometries of Rn for n = 1 and n = 2.
Since O1(R) = {±1}, the isometries of R are the functions h(x) = x+c and h(x) = −x+c
for c ∈R. (Of course, this case can be worked out easily without the earlier material.)
Now consider isometries of R2. Write an isometry h ∈Iso(R2) as h(v) = Av + w with
A ∈O2(R) and w ∈R2. By Example 3.3, A is a rotation or reﬂection, depending on det A.
There turn out to be four possibilities for h: translations, rotations, reﬂections, and glide
reﬂections. A glide reﬂection is the composition of a reﬂection and a nonzero translation in
a direction parallel to the line of reﬂection. A picture of a glide reﬂection is in the ﬁgure
below, where the (horizontal) line of reﬂection is dashed and the translation is a movement
to the right.
The image above, which includes “before” and “after” states, suggests a physical inter-
pretation of a glide reﬂection: it is the result of turning the plane in space like a half-turn
of a screw. A more picturesque image, suggested to me by Michiel Vermeulen, is the eﬀect
of successive steps with a left foot and then a right foot in the sand or snow (if your feet
are mirror reﬂections).
The possibilities for isometries of f are collected in Table 1 below. It describes how the
type of an isometry h is determined by det A and the geometry of the set of ﬁxed points of h
(solutions to h(v) = v): empty, a point, a line, or the plane. (The only isometry belonging
to more than one of the four possibilities is the identity, which is both a translation and a
rotation, so we make the identity its own row in the table.) The table also shows how a
description of the ﬁxed points can be obtained algebraically from A and w.
Isometry
Condition
Fixed pts
Identity
A = I2, w = 0
R2
Nonzero Translation
A = I2, w ̸= 0
∅
Nonzero Rotation
det A = 1, A ̸= I2
(I2 −A)−1w
Reﬂection
det A = −1, Aw = −w
w/2 + ker(A −I2)
Glide Reﬂection
det A = −1, Aw ̸= −w
∅
Table 1. Isometries of R2: h(v) = Av + w, A ∈O2(R).
To justify the information in the table we move down the middle column. The ﬁrst two
rows are obvious, so we start with the third row.

<!-- page 10 -->
10
KEITH CONRAD
Row 3: Suppose det A = 1 and A ̸= I2, so A = ( cos θ −sin θ
sin θ
cos θ ) for some θ and cos θ ̸= 1. We
want to show h is a rotation. First of all, h has a unique ﬁxed point: v = Av + w precisely
when w = (I2 −A)v. We have det(I2 −A) = 2(1 −cos θ) ̸= 0, so I2 −A is invertible and
p = (I2 −A)−1w is the ﬁxed point of h. Then w = (I2 −A)p = p −Ap, so
(4.1)
h(v) = Av + (p −Ap) = A(v −p) + p.
Since A is a rotation by θ around the origin, (4.1) shows h is a rotation by θ around P.
Rows 4, 5: Suppose det A = −1, so A = ( cos θ
sin θ
sin θ −cos θ ) for some θ and A2 = I2. We again
look at ﬁxed points of h. As before, h(v) = v for some v if and only if w = (I2 −A)v.
But unlike the previous case, now det(I2 −A) = 0 (check!), so I2 −A is not invertible and
therefore w may or may not be in the image of I2 −A. When w is in the image of I2 −A,
we will see that h is a reﬂection. When w is not in the image of I2 −A, we will see that h
is a glide reﬂection.
Suppose the isometry h(v) = Av + w with det A = −1 has a ﬁxed point. Then w/2 must
be a ﬁxed point. Indeed, let p be any ﬁxed point, so p = Ap + w. Since A2 = I2,
Aw = A(p −Ap) = Ap −p = −w,
so
h
w
2

= A
w
2

+ w = 1
2Aw + w = w
2 .
Conversely, if h(w/2) = w/2 then A(w/2) + w = w/2,, so Aw = −w.
Thus h has a ﬁxed point if and only if Aw = −w, in which case
(4.2)
h(v) = Av + w = A

v −w
2

+ w
2 .
Since A is a reﬂection across some line L through 0, (4.2) says h is a reﬂection across the
parallel line w/2 + L passing through w/2. See the ﬁgure below. (Algebraically, we can say
L = {v : Av = v} = ker(A −I2). Since A −I2 is not invertible and not identically 0, its
kernel really is 1-dimensional.)
L
w/2
w
w/2 + L
v
Av
h(v)
Now assume h has no ﬁxed point, so Aw ̸= −w. We will show h is a glide reﬂection. (The
formula h = Av+w shows h is the composition of a reﬂection and a nonzero translation, but
w need not be parallel to the line of reﬂection of A, which is ker(A−I2), so this formula for
h does not show directly that h is a glide reﬂection.) We will now take stronger advantage
of the fact that A2 = I2.
Since O = A2 −I2 = (A −I2)(A + I2) and A ̸= ±I2 (after all, det A = −1), A + I2 and
A −I2 are not invertible. Therefore the subspaces
W1 = ker(A −I2),
W2 = ker(A + I2)

<!-- page 11 -->
ISOMETRIES OF Rn
11
are both nonzero, and neither is the whole plane, so W1 and W2 are both one-dimensional.
We already noted that W1 is the line of reﬂection of A (ﬁxed points of A form the kernel of
A −I2). It turns out that W2 is the line perpendicular to W1. To see why, pick w1 ∈W1
and w2 ∈W2, so
Aw1 = w1,
Aw2 = −w2.
Then, since Aw1 · Aw2 = w1 · w2 by orthogonality of A, we have
w1 · (−w2) = w1 · w2.
Thus w1 · w2 = 0, so w1 ⊥w2.
Now we are ready to show h is a glide reﬂection. Pick nonzero vectors wi ∈Wi for i = 1, 2,
and use {w1, w2} as a basis of R2. Write w = h(0) in terms of this basis: w = c1w1 + c2w2.
To say there are no ﬁxed points for h is the same as Aw ̸= −w, so w ̸∈W2. That is, c1 ̸= 0.
Then
(4.3)
h(v) = Av + w = (Av + c2w2) + c1w1.
Since A(c2w2) = −c2w2, our previous discussion shows v 7→Av + c2w2 is a reﬂection
across the line c2w2/2 + W1. Since c1w1 is a nonzero vector in W1, (4.3) exhibits h as the
composition of a reﬂection across the line c2w2/2 + W1 and a nonzero translation by c1w1,
whose direction is parallel to the line of reﬂection, so h is a glide reﬂection.
We have now justiﬁed the information in Table 1. Each row describes a diﬀerent kind
of isometry. Using ﬁxed points it is easy to distinguish the ﬁrst four rows from each other
and to distinguish glide reﬂections from any isometry besides translations. A glide reﬂection
can’t be a translation since any isometry of R2 is uniquely of the form hA,w, and translations
have A = I2 while glide reﬂections have det A = −1.
Lemma 4.1. A composition of two reﬂections of R2 is a translation or a rotation.
Proof. The product of two matrices with determinant −1 has determinant 1, so the com-
position of two reﬂections has the form v 7→Av + w where det A = 1. Such isometries
are translations or rotations by Table 1 (consider the identity to be a trivial translation or
rotation).
□
In Example A.2 we will express any translation in Rn as the composition of two reﬂec-
tions.
Theorem 4.2. Each isometry of R2 is a composition of at most 2 reﬂections except for
glide reﬂections, which are a composition of 3 (and no fewer) reﬂections.
Proof. We check the theorem for each type of isometry in Table 1 besides reﬂections, for
which the theorem is obvious.
The identity is the square of any reﬂection.
For a translation t(v) = v + w, let A be the matrix representing the reﬂection across
the line w⊥. Then Aw = −w. Set s1(v) = Av + w and s2(v) = Av. Both s1 and s2 are
reﬂections, and (s1 ◦s2)(v) = A(Av) + w = v + w since A2 = I2.
Now consider a rotation, say h(v) = A(v −p) + p for some A ∈O2(R) with det A = 1
and p ∈R2. We have h = t ◦r ◦t−1, where t is translation by p and r(v) = Av is a rotation
around the origin. Let A′ be any reﬂection matrix (e.g., A′ = ( 1 0
0 −1 )). Set s1(v) = AA′v
and s2(v) = A′v. Both s1 and s2 are reﬂections and r = s1 ◦s2 (check). Therefore
(4.4)
h = t ◦r ◦t−1 = (t ◦s1 ◦t−1) ◦(t ◦s2 ◦t−1).

<!-- page 12 -->
12
KEITH CONRAD
The conjugate of a reﬂection by a translation (or by any isometry, for that matter) is another
reﬂection, as an explicit calculation using Table 1 shows. Thus, (4.4) expresses the rotation
h as a composition of 2 reﬂections.
Finally we consider glide reﬂections. Since this is the composition of a translation and
a reﬂection, it is a composition of 3 reﬂections. We can’t use fewer reﬂections to get a
glide reﬂection, since a composition of two reﬂections is either a translation or a rotation
by Lemma 4.1 and we know that a glide reﬂection is not a translation or rotation (or
reﬂection).
□
In Table 2 we record the minimal number of reﬂections whose composition can equal a
particular type of isometry of R2.
Isometry
Min. Num. Reﬂections
dim(ﬁxed set)
Identity
0
2
Nonzero Translation
2
0
Nonzero Rotation
2
0
Reﬂection
1
1
Glide Reﬂection
3
0
Table 2. Counting Reﬂections in an Isometry
That each isometry of R2 is a composition of at most 3 reﬂections can be proved geomet-
rically, without recourse to a prior classiﬁcation of all isometries of the plane. We will give
a rough sketch of the argument. We will take for granted (!) that an isometry that ﬁxes at
least two points is a reﬂection across the line through those points or is the identity. (This
is related to Corollary 2.3 when n = 2.) Pick any isometry h of R2. We may suppose h
is not a reﬂection or the identity (the identity is the square of any reﬂection), so h has at
most one ﬁxed point. If h has one ﬁxed point, say P, choose Q ̸= P. Then h(Q) ̸= Q and
the points Q and h(Q) lie on a common circle centered at P (because h(P) = P). Let s be
the reﬂection across the line through P that is perpendicular to the line connecting Q and
h(Q). Then s◦h ﬁxes P and Q, so s◦h is the identity or is a reﬂection. Thus h = s◦(s◦h)
is a reﬂection or a composition of two reﬂections. If h has no ﬁxed points, pick any point P.
Let s be the reﬂection across the perpendicular bisector of the line connecting P and h(P),
so s ◦h ﬁxes P. Thus s ◦h has a ﬁxed point, so our previous argument shows s ◦h is either
the identity, a reﬂection, or the composition of two reﬂections, so h is the composition of
at most 3 reﬂections.
A byproduct of this argument, which did not use the classiﬁcation of isometries, is another
proof that all isometries of R2 are invertible: any isometry is a composition of reﬂections
and reﬂections are invertible.
From the fact that all isometries ﬁxing 0 in R and R2 are rotations or reﬂections, the
following general description can be proved about isometries of any Euclidean space in terms
of rotations and reﬂections on one-dimensional and two-dimensional subspaces.
Theorem 4.3. If h is an isometry of Rn that ﬁxes 0 then there is an orthogonal decompo-
sition Rn = W1 ⊕W2 ⊕· · · ⊕Wm such that dim(Wi) = 1 or 2 for all i, and the restriction
of h to Wi is a rotation unless i = m and dim(Wm) = 1 and det h = −1, in which case the
restriction of h to Wm is a reﬂection.
Proof. See [1, Theorem 6.47] or [2, Cor. to Theorem 2].
□

<!-- page 13 -->
ISOMETRIES OF Rn
13
Appendix A. Reflections
A reﬂection is an isometry of Rn that ﬁxes all the points in a chosen hyperplane and
interchanges the position of points along each line perpendicular to that hyperplane at
equal distance from it. These isometries play a role that is analogous to transpositions in
the symmetric group. Reﬂections, like transpositions, have order 2.
Let’s look ﬁrst at reﬂections across hyperplanes that contain the origin. Let H be a
hyperplane containing the origin through which we wish to reﬂect. Set L = H⊥, so L is a
one-dimensional subspace. Every v ∈Rn can be written uniquely in the form v = w + u,
where w ∈H and u ∈L. The reﬂection across H, by deﬁnition, is the function
(A.1)
s(v) = s(w + u) = w −u.
That is, s ﬁxes H = u⊥and acts like −1 on L = Ru. From the formula deﬁning s, it is
linear in v. Since w ⊥u, ||s(v)|| = ||w|| + ||u|| = ||v||, so by linearity s is an isometry:
||s(v) −s(w)|| = ||s(v −w)|| = ||v −w||.
Since s is linear, it can be represented by a matrix. To write this matrix simply, pick an
orthogonal basis {v1, . . . , vn−1} of H and let vn be a nonzero vector in L = H⊥, so vn is
orthogonal to H. Then
s(c1v1 + · · · + cnvn) = c1v1 + · · · + cn−1vn−1 −cnvn.
The matrix for s has 1’s along the diagonal except for −1 in the last position:
(A.2)





c1
...
cn−1
−cn
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
1
· · ·
0
0
...
...
...
...
0
· · ·
1
0
0
· · ·
0
−1
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
c1
...
cn−1
cn




.
The matrix in (A.2) represents s relative to a convenient choice of basis. In particular, from
the matrix representation we see det s = −1: every reﬂection in On(R) has determinant
−1. Notice the analogy with transpositions in the symmetric group, which have sign −1.
We now derive another formula for s, which will look more complicated than what we
have seen so far but should be considered more fundamental. Fix a nonzero vector u on the
line L = H⊥. Since Rn = H ⊕L, any v ∈Rn can be written as w + cu, where w ∈H and
c ∈R. Since w ⊥L, v · u = c(u · u), so c = (v · u)/(u · u). Then
(A.3)
s(v) = w −cu = v −2cu = v −2v · u
u · uu.
The last expression is our desired formula for s(v). Note for all v that s(v) · u = −v · u.
It is standard to label the reﬂection across a hyperplane containing the origin using
a vector in the orthogonal complement to the hyperplane, so we write s in (A.3) as su.
This is the reﬂection in the hyperplane u⊥, so su(u) = −u. By (A.3), sau = su for any
a ∈R −{0}, which makes geometric sense since (au)⊥= u⊥, so the reﬂection in the
hyperplane orthogonal to u and to au is the same. Moreover, H is the set of points ﬁxed
by su, and we can conﬁrm this with (A.3): su(v) = 0 if and only if v · u = 0, which means
v ∈u⊥= H.
To get a formula for the reﬂection across any hyperplane in Rn (not just those containing
the origin), we use the following lemma to describe any hyperplane.

<!-- page 14 -->
14
KEITH CONRAD
Lemma A.1. Every hyperplane in Rn has the form Hu,c = {v ∈Rn : v · u = c} for some
nonzero u ∈Rn that is orthogonal to the hyperplane and some c ∈R. The hyperplane
contains 0 if and only if c = 0.
Proof. Let H be a hyperplane and choose w ∈H. Then H −w is a hyperplane containing
the origin. Fix a nonzero vector u that is perpendicular to H. Since H −w is a hyperplane
through the origin parallel to H, a vector v lies in H if and only if v −w ⊥u, which is
equivalent to v · u = w · u. Thus H = Hu,c for c = w · u.
□
Below are hyperplanes (lines) in R2 of the form H(2,1),c = {v : v · (2, 1) = c}.
c = 0 c = 2 c = 4
(2, 1)
w1
w2
As the ﬁgure suggests, the diﬀerent hyperplanes Hu,c as c varies are parallel to each other.
Speciﬁcally, if w ∈Hu,c then Hu,c = Hu,0 +w (check!). (The choice of w in Hu,c aﬀects how
Hu,0 is translated over to Hu,c, since adding w to Hu,0 sends 0 to w. Compare in the above
ﬁgure how Hu,0 is carried onto Hu,4 using translation by w1 and by w2.)
In the family of parallel hyperplanes {Hu,c : c ∈R}, we can replace u with any nonzero
scalar multiple, since Hau,c = Hu,c/a, so {Hu,c : c ∈R} = {Hau,c : c ∈R}. Geometrically
this makes sense, since the importance of u relative to the hyperplanes is that it is an
orthogonal direction, and au also provides an orthogonal direction to the same hyperplanes.
To reﬂect points across a hyperplane H, ﬁx a nonzero vector w ∈H. Geometric intuition
suggests that to reﬂect across H we can subtract w, then reﬂect across H −w (a hyperplane
through the origin), and then add w back. In the ﬁgure below, this corresponds to moving
from P to Q (subtract w from P) to Q′ (reﬂect Q across H −w) to P ′ (add w to Q′),
getting the reﬂection of P across H.
H −w
H
w
P
Q
Q′
P ′
Therefore reﬂection across H should be given by the formula
(A.4)
s′(v) = s(v −w) + w,

<!-- page 15 -->
ISOMETRIES OF Rn
15
where s is reﬂection across H −w. Setting H = Hu,c by Lemma A.1, where u is a nonzero
vector orthogonal to H, c = u · w (since w ∈H) and by (A.3) and (A.4)
(A.5)
s′(v) = (v −w) −2(v −w) · u
u · u
u + w = v −2
v · u −c
u · u

u.
The following properties show (A.5) is the reﬂection across the hyperplane Hu,c.
• If v ∈Hu,c then v · u = c, so (A.5) implies s′(v) = v: s′ ﬁxes points in Hu,c.
• For any v in Rn, the average 1
2(v + s′(v)), which is the midpoint of the segment
connecting v and s′(v), lies in Hu,c: it equals v −
  v·u−c
u·u

u, whose dot product with
u is c.
• For any v in Rn the diﬀerence v −s′(v), which is the direction of the segment
connecting v and s′(v), is perpendicular to Hu,c since, by (A.5), it lies in Ru = H⊥.
Example A.2. We use (A.5) to show any nonzero translation tu(v) = v + u is the compo-
sition of two reﬂections. Set H = u⊥= Hu,0 and write su for the reﬂection across H and
s′
u for the reﬂection across H + u, the hyperplane parallel to H that contains u. By (A.3)
and (A.5),
s′
u(su(v)) = su(v) −2
su(v) · u −u · u
u · u

u = su(v) −2
−v · u
u · u −1

u = v + 2u,
so s′
u ◦su = t2u. This is true for all u, so tu = s′
u/2 ◦su/2.
These formulas show any translation is a composition of two reﬂections across hyperplanes
perpendicular to the direction of the translation.
The ﬁgure below illustrates Example A.2 in the plane, with u being a vector along the
x-axis. Reﬂecting v and w across H = u⊥and then across H + u is the same as translation
of v and w by 2u.
u
2u
H
H + u
v
s(v)
s′(s(v))
w
s(w)
s′(s(w))
Theorem A.3. Let w and w′ be distinct in Rn. There is a unique reﬂection s in Rn such
that s(w) = w′. This reﬂection is in On(R) if and only if w and w′ have the same length.
Proof. A reﬂection taking w to w′ has a ﬁxed hyperplane that contains the average 1
2(w+w′)
and is orthogonal to w −w′. Therefore the ﬁxed hyperplane of a reﬂection taking w to w′
must be Hw−w′,c for some c. Since 1
2(w + w′) ∈Hw−w′,c, we have c = (w −w′) · 1
2(w + w′) =
1
2(w · w −w′ · w′). Thus the only reﬂection that could send w to w′ is the one across the
hyperplane Hw−w′, 1
2 (w·w−w′·w′).

<!-- page 16 -->
16
KEITH CONRAD
Let’s check that reﬂection across this hyperplane does send w to w′. Its formula, by
(A.5), is
s(v) = v −2

v · (w −w′) −c
(w −w′) · (w −w′)

(w −w′),
where c = 1
2(w · w −w′ · w′). When v = w, the coeﬃcient of w −w′ in the above formula
becomes −1, so s(w) = w −(w −w′) = w′.
If w and w′ have the same length then w · w = w′ · w′, so c = 0 and that means s has
ﬁxed hyperplane Hw−w′,0. Therefore s is a reﬂection ﬁxing 0, so s ∈On(R). Conversely, if
s ∈On(R) then s(0) = 0, which implies 0 ∈Hw−w′,c, so c = 0, and therefore w·w = w′ ·w′,
which means w and w′ have the same length.
To illustrate techniques, when w and w′ are distinct vectors in Rn with the same length
let’s construct a reﬂection across a hyperplane through the origin that sends w to w′ geo-
metrically, without using the algebraic formulas for reﬂections and hyperplanes.
If w and w′ are on the same line through the origin then w′ = −w (the only vectors on
Rw with the same length as w are w and −w). For the reﬂection s across the hyperplane
w⊥, s(w) = −w = w′.
If w and w′ are not on the same line through the origin then the span of w and w′ is a
plane. The vector v = w + w′ is nonzero and lies on the line in this plane that bisects the
angle between w and w′. (See the ﬁgure below.) Let u be a vector in this plane orthogonal
to v, so writing w = av +bu we have w′ = av −bu.1 Letting s be the reﬂection in Rn across
the hyperplane u⊥, which contains Rv (and contains more than Rv when n > 2), we have
s(v) = v and s(u) = −u, so s(w) = s(av + bu) = av −bu = w′.
w
w′
v
u
□
We have already noted that reﬂections in On(R) are analogous to transpositions in the
symmetric group Sn: they have order 2 and determinant −1, just as transpositions have
order 2 and sign −1. The next theorem, due to E. Cartan, is the analogue for On(R) of the
generation of Sn by transpositions.
Theorem A.4 (Cartan). The group On(R) is generated by its reﬂections.
Note that a reﬂection in On(R) ﬁxes 0 and therefore its ﬁxed hyperplane contains the
origin, since a reﬂection does not ﬁx any point outside its ﬁxed hyperplane.
1This is geometrically clear, but algebraically tedious. Since v = w +w′, we have w′ = v −w = (1−a)v −bu,
so to show w′ = av −bu we will show a = 1
2. Since v ⊥u, w · v = a(v · v). The vectors w and w′ have the
same length, so w · v = w · (w + w′) = w · w + w · w′ and v · v = (w + w′) · (w + w′) = 2(w · w + w · w′), so
w · v = 1
2(v · v). Comparing this with w · v = a(v · v), we have a = 1
2.

<!-- page 17 -->
ISOMETRIES OF Rn
17
Proof. We argue by induction on n. The theorem is trivial when n = 1, since O1(R) = {±1}.
Let n ≥2. (While the case n = 2 was treated in Theorem 4.2, we will reprove it here.)
Pick h ∈On(R), so h(en) and en have the same length. If h(en) ̸= en, by Theorem A.3
there is a (unique) reﬂection s in On(R) such that s(h(en)) = en, so the composite isometry
sh = s ◦h ﬁxes en. If h(en) = en then we can write s(h(en)) = en where s is the identity
on Rn. We will use s with this meaning (reﬂection or identity) below.
Any element of On(R) preserves orthogonality, so sh sends the hyperplane H := e⊥
n =
Rn−1 ⊕{0} back to itself and is the identity on the line Ren. Since e⊥
n = Rn−1 ⊕{0} has
dimension n−1, by induction2 there are a ﬁnite number of reﬂections s1, . . . , sm in H ﬁxing
the origin such that
sh|H = s1s2 · · · sm.
Any reﬂection H →H that ﬁxes 0 extends naturally to a reﬂection of Rn ﬁxing 0, by
declaring it to be the identity on the line H⊥= Ren and extending by linearity from the
behavior on H and H⊥.3 Write si for the extension of si to a reﬂection on Rn in this way.
Consider now the two isometries
sh,
s1s2 · · · sm
of Rn. They agree on H = e⊥
n and they each ﬁx en. Thus, by linearity, we have equality as
functions on Rn:
sh = s1s2 · · · sm.
Therefore h = s−1s1s2 · · · sm.
□
From the proof, if (sh)|H is a composition of m isometries of H ﬁxing 0 that are the
identity or reﬂections then h is a composition of m + 1 isometries of Rn ﬁxing 0 that are
the identity or reﬂections. Therefore every element of On(R) is a composition of at most n
elements of On(R) that are the identity or reﬂections (in other words, from m ≤n−1 we get
m+1 ≤n). If h is not the identity then such a decomposition of h must include reﬂections,
so by removing the identity factors we see h is a composition of at most n reﬂections.
The identity on Rn is a composition of 2 reﬂections. This establishes the stronger form of
Cartan’s theorem: every element of On(R) is a composition of at most n reﬂections (except
for the identity when n = 1, unless we use the convention that the identity is a composition
of 0 reﬂections).
Remark A.5. Cartan’s theorem can be deduced from the decomposition of Rn in Theorem
4.3. Let a be the number of 2-dimensional Wi’s and b be the number of 1-dimensional Wi’s,
so 2a + b = n and h acts as a rotation on any 2-dimensional Wi. By Theorem 4.2, any
rotation of Wi is a composition of two reﬂections in Wi. A reﬂection in Wi can be extended
to a reﬂection in Rn by setting it to be the identity on the other Wj’s. If Wi is 1-dimensional
then h is the identity on Wi except perhaps once, in which case b ≥1 and h is a reﬂection
on that Wi. Putting all of these reﬂections together, we can express h as a composition of
at most 2a reﬂections if b = 0 and at most 2a + 1 reﬂections if b ≥1. Either way, h is a
2Strictly speaking, since H is not Rn−1, to use induction we really should be proving the theorem not
just for orthogonal transformations of the Euclidean spaces Rn, but for orthogonal transformations of their
subspaces as well. The deﬁnition of an orthogonal transformation of a subspace W ⊂Rn is based on the
property (3.3): it is a linear transformation W →W that preserves dot products between all pairs of vectors
in W. We use (A.3) – rather than a matrix formula – to deﬁne a reﬂection across a hyperplane in a subspace.
3Geometrically, for n −1 ≥2 if s is a reﬂection on H ﬁxing the orthogonal complement of a line L in H,
then this extension of s to Rn is the reﬂection on Rn ﬁxing the orthogonal complement of L in Rn.

<!-- page 18 -->
18
KEITH CONRAD
composition of at most 2a + b = n reﬂections, with the understanding when n = 1 that the
identity is a composition of 0 reﬂections.
Example A.6. For 0 ≤m ≤n, we will show the orthogonal matrix







−1
0
· · ·
0
0
0
−1
· · ·
0
0
...
...
...
...
...
0
0
· · ·
1
0
0
0
· · ·
0
1







with m −1’s and n −m 1’s on the diagonal is a composition of m reﬂections in On(R) and
not less than m reﬂections in On(R).
Any reﬂection in On(R) has a ﬁxed hyperplane through 0 of dimension n −1. Therefore
a composition of r reﬂections in On(R) ﬁxes the intersection of r hyperplanes through the
origin, whose dimension is at least n−r (some hyperplanes may be the same). If h ∈On(R)
is a composition of r reﬂections and ﬁxes a subspace of dimension d then d ≥n −r, so
r ≥n −d. Hence we get a lower bound on the number of reﬂections in On(R) whose
composition can equal h in terms of the dimension of {v ∈Rn : h(v) = v}. For the above
matrix, the subspace of ﬁxed vectors is {0}m⊕Rn−m, which has dimension n−m. Therefore
the least possible number of reﬂections in On(R) whose composition could equal this matrix
is n −(n −m) = m, and this bound is achieved: the m matrices with −1 in one of the ﬁrst
m positions on the main diagonal and 1 elsewhere on the main diagonal are all reﬂections
in On(R) and their composition is the above matrix.
In particular, the isometry h(v) = −v is a composition of n and no fewer reﬂections in
On(R).
Corollary A.7. Every isometry of Rn is a composition of at most n + 1 reﬂections. An
isometry that ﬁxes at least one point is a composition of at most n reﬂections.
The diﬀerence between this corollary and Cartan’s theorem is that in the corollary we
are not assuming isometries, or in particular reﬂections, are taken from On(R), i.e., they
need not ﬁx 0.
Proof. Let h be an isometry of Rn. If h(0) = 0, then h belongs to On(R) (Theorem 2.4) and
Cartan’s theorem implies h is a composition of at most n reﬂections through hyperplanes
containing 0. If h(p) = p for some p ∈Rn, then we can change the coordinate system
(using a translation) so that the origin is placed at p. Then the previous case shows h is a
composition of at most n reﬂections through hyperplanes containing p.
Suppose h has no ﬁxed points. Then in particular, h(0) ̸= 0. By Theorem A.3 there is
some reﬂection s across a hyperplane in Rn such that s(h(0)) = 0. Then sh ∈On(R), so by
Cartan’s theorem sh is a composition of at most n reﬂections, and that implies h = s(sh)
is a composition of at most n + 1 reﬂections.
□
The proof of Corollary A.7 shows an isometry of Rn is a composition of at most n
reﬂections except possibly when it has no ﬁxed points.
Then n + 1 reﬂections may be
required. For example, when n = 2 nonzero translations and glide reﬂections have no ﬁxed
points, and the ﬁrst type requires 2 reﬂections while the second type requires 3 reﬂections.

<!-- page 19 -->
ISOMETRIES OF Rn
19
References
[1] S. H. Friedberg, A. J. Insel, and L. E. Spence, “Linear Algebra,” 4th ed., Pearson, Upper Saddle River
NJ, 2003.
[2] L. Rudolph, “The Structure of Orthogonal Transformations,” Amer. Math. Monthly 98 (1991), 349–352.
[3] A. Vogt, “On the linearity of form isometries,” SIAM Journal on Applied Mathematics 22 (1972), 553–
560.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*