# The Norm of a Matrix

> **Source**: https://kconrad.math.uconn.edu/blurbs/matrixnorm.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
COMPUTING THE NORM OF A MATRIX
KEITH CONRAD
1. Introduction
In Rn there is a standard notion of length: the size of a vector v = (a1, . . . , an) is
||v|| =
q
a2
1 + · · · + a2n.
We will discuss in Section 2 the general concept of length in a vector space, called a norm,
and then look at norms on matrices in Section 3. In Section 4 we’ll see how the matrix norm
that is closely connected to the standard norm on Rn can be computed from eigenvalues of
an associated symmetric matrix.
2. Norms on Vector Spaces
Let V be a vector space over R. A norm on V is a function ||·|| : V →R satisfying three
properties:
(1) ||v|| ≥0 for all v ∈V , with equality if and only if v = 0,
(2) ||v + w|| ≤||v|| + ||w|| for all v and w in V ,
(3) ||cv|| = |c| ||v|| for all c ∈R and v ∈V .
The same deﬁnition applies to complex vector spaces. From a norm on V we get a metric
on V by d(v, w) = ||v −w||. The triangle inequality for this metric is a consequence of the
second property of norms.
Example 2.1. The standard norm on Rn, using the standard basis e1, . . . , en, is


n
X
i=1
aiei

 =
v
u
u
t
n
X
i=1
a2
i .
This gives rise to the Euclidean metric on Rn: d(P aiei, P biei) =
pP(ai −bi)2.
Example 2.2. The sup-norm on Rn is


n
X
i=1
aiei


sup
= max
i
|ai|.
This gives rise to the sup-metric on Rn: d(P aiei, P biei) = max |ai −bi|.
Example 2.3. On Cn the standard norm and sup-norm are deﬁned similarly to the case
of Rn, but we need |z|2 instead of z2 when z is complex:


n
X
i=1
aiei

 =
v
u
u
t
n
X
i=1
|ai|2,


n
X
i=1
aiei


sup
= max
i
|ai|.
1

<!-- page 2 -->
2
KEITH CONRAD
A common way of placing a norm on a real vector space V is by an inner product, which
is a pairing (·, ·): V × V →R that is
(1) bilinear: linear in each component when the other is ﬁxed. Linearity in the ﬁrst
component means (v + v′, w) = (v, w) + (v′, w) and (cv, w) = c(v, w) for v, v′, w ∈V
and c ∈R, and similarly in the second component.
(2) symmetric: (v, w) = (w, v).
(3) positive-deﬁnite: (v, v) ≥0, with equality if and only if v = 0. The standard inner
product on Rn is the dot product:
 n
X
i=1
aiei,
n
X
i=1
biei
!
=
n
X
i=1
aibi.
For an inner product (·, ·) on V , a norm can be deﬁned by the formula
||v|| =
p
(v, v).
That this is actually a norm on V follows from the Cauchy–Schwarz inequality
(2.1)
|(v, w)| ≤(v, v)(w, w) = ||v|| ||w||
as follows. For all v and w in V ,
||v + w||2
=
(v + w, v + w)
=
(v, v) + (v, w) + (w, v) + (w, w)
=
||v||2 + 2(v, w) + ||w||2
≤
||v||2 + 2|(v, w)| + ||w||2
since a ≤|a| for all a ∈R
≤
||v||2 + 2 ||v|| ||w|| + ||w||2
by (2.1)
=
(||v|| + ||w||)2.
Taking (positive) square roots of both sides yields ||v + w|| ≤||v|| + ||w||. A proof of the
Cauchy–Schwarz inequality is in the appendix.
Using the standard inner product on Rn, the Cauchy–Schwarz inequality assumes its
classical form, proved by Cauchy in 1821:

n
X
i=1
aibi
 =
v
u
u
t
n
X
i=1
a2
i ·
n
X
I=1
b2
i .
The Cauchy–Schwarz inequality (2.1) is true for every inner product on a real vector space,
not just the standard inner product on Rn.
While the norm on Rn that comes from the standard inner product is the standard norm,
the sup-norm on Rn does not arise from an inner product, i.e., there is no inner product
whose associated norm is the sup-norm.
Even though the sup-norm and the standard norm on Rn are not equal, they are each
bounded by a constant multiple of the other one:
(2.2)
max
i
|ai| ≤
v
u
u
t
n
X
i=1
a2
i ≤√n max
i
|ai|.
i.e., ||v||sup ≤||v|| ≤√n ||v||sup for all v ∈Rn. Therefore the metrics these two norms give
rise to determine the same notions of convergence: a sequence in Rn that is convergent with

<!-- page 3 -->
COMPUTING THE NORM OF A MATRIX
3
respect to one of the metrics is also convergent with respect to the other metric. Also Rn
is complete with respect to both of these metrics.
The standard inner product on Rn is closely tied to transposition of n × n matrices. For
A = (aij) ∈Mn(R), let A⊤= (aji) be its transpose. Then for all v, w ∈Rn,
(2.3)
(Av, w) = (v, A⊤w),
(v, Aw) = (A⊤v, w),
where (·, ·) is the standard inner product on Rn.
We now brieﬂy indicate what inner products are on complex vector spaces. An inner
product on a complex vector space V is a pairing (·, ·): V × V →C that is
(1) linear on the left and conjugate-linear on the right: it is additive in each component
with the other one ﬁxed and (cv, w) = c(v, w) and (v, cw) = c(v, w) for c ∈C.
(2) conjugate-symmetric: (v, w) = (w, v),
(3) positive-deﬁnite: (v, v) ≥0, with equality if and only if v = 0.
The standard inner product on Cn is not the dot product, but has a conjugation in the
second component:
(2.4)
 n
X
i=1
aiei,
n
X
i=1
biei
!
=
n
X
i=1
aibi.
This standard inner product on Cn is closely tied to conjugate-transposition of n×n complex
matrices. For A = (aij) ∈Mn(C), let A∗= A
⊤= (aji) be its conjugate-transpose. Then
for all v, w ∈Cn,
(2.5)
(Av, w) = (v, A∗w),
(v, Aw) = (A∗v, w).
An inner product on a complex vector space satisﬁes the Cauchy–Schwarz inequality, so
it can be used to deﬁne a norm just as in the case of inner products on real vector spaces.
Although we will be focusing on norms on ﬁnite-dimensional spaces, the extension of
these ideas to inﬁnite-dimensional spaces is quite important in both analysis and physics
(quantum mechanics). Speaking of physics, physicists deﬁne inner products on complex
vector spaces as being linear on the right and conjugate-linear on the left.
It’s just a
diﬀerence in notation, but leads to more diﬀerences, e.g., the physicist’s standard inner
product on Cn is (Pn
i=1 aiei, Pn
i=1 biei) = Pn
i=1 aibi, which is the complex conjugate of the
mathematician’s standard inner product on Cn as deﬁned earlier.
Exercises.
1. Letting (·, ·)m be the dot product on Rm and (·, ·)n be the dot product on Rn,
show for each m × n matrix A, n × m matrix B, v ∈Rn, and w ∈Rm that
(Av, w)m = (v, A⊤w)n and (v, Bw)n = (B⊤v, w)m. When m = n this becomes
(2.3).
2. Verify (2.5).
3. Defining Norms on Matrices
From now on, the norm and inner product on Rn and Cn are the standard ones.
The set of n × n real matrices Mn(R) forms a real vector space. How should we deﬁne a
norm on Mn(R)? One idea is to view Mn(R) as Rn2 and use the sup-norm on Rn2
||(aij)||sup = max
i,j |aij|.

<!-- page 4 -->
4
KEITH CONRAD
or the standard norm on Rn2 (also called the Frobenius norm on Mn(R)): ||(aij)|| =
qP a2
ij.
While these are used in numerical work, in pure math there is a better choice of a norm
on Mn(R) than either of these. Before describing it, we use the sup-norm on Mn(R) to
show that each n × n matrix changes the (standard) length of vectors in Rn by a uniformly
bounded amount that depends only on n and the matrix. For v = (c1, . . . , cn) ∈Rn,
||Av||
≤
√n ||Av||sup
by (2.2)
=
√n max
i

n
X
j=1
aijcj

≤
√n max
i
n
X
j=1
|aij||cj|
≤
√n max
i
n
X
j=1
|aij| ||v||sup
≤
n√n max
i,j |aij| ||v||sup
≤
n√n max
i,j |aij| ||v||
by (2.2).
Let C = n√n max |aij|. This is a constant depending on the dimension n of the space and
the matrix A, but not on v, and ||Av|| ≤C ||v|| for all v. By linearity, ||Av −Aw|| ≤C ||v −w||
for all v, w ∈Rn.
Let’s write down the above calculation as a lemma.
Lemma 3.1. For each A ∈Mn(R), there is a C ≥0 such that ||Av|| ≤C ||v|| for all v ∈Rn.
The constant C we wrote down might not be optimal. Perhaps there is a smaller constant
C′ < C such that ||Av|| ≤C′ ||v|| for all v ∈Rn. We will get a norm on Mn(R) by assigning
to each A ∈Mn(R) the least C ≥0 such that ||Av|| ≤C ||v|| for all v ∈Rn, where the vector
norms in ||Av|| and ||v|| are the standard ones on Rn.
Theorem 3.2. For each A ∈Mn(R), there is a unique real number b ≥0 such that
(i) ||Av|| ≤b ||v|| for all v ∈Rn,
(ii) b is minimal: if ||Av|| ≤C ||v|| for all v ∈Rn, then b ≤C.
Proof. We ﬁrst show by a scaling argument that ||Av|| ≤b ||v|| for all v ∈Rn if and only if
||Av|| ≤b for all v ∈Rn with ||v|| = 1. The direction (⇒) is clear by using ||v|| = 1. For the
direction (⇐), when v = 0 we trivially have ||Av|| = 0 = b ||v||. When v ̸= 0 let c = ||v||, so
c > 0 and the vector v/c has norm 1 (||v/c|| = |1/c| ||v|| = (1/|c|) ||v|| = (1/ ||v||) ||v|| = 1), so
by hypothesis ||A(v/c)|| ≤b, which implies (1/|c|) ||Av|| ≤b by linearity. Now multiply both
sides by |c| to get ||Av|| ≤bc = b ||v||.
Therefore the theorem is saying the set {||Av|| : ||v|| = 1} has a (ﬁnite) maximum value,
which is b. This is what we will prove.
The matrix A as a function Rn →Rn is continuous since the components of Av are linear
functions of the components of v, and hence they are each continuous in v. The standard
norm ||·|| : Rn →R is also continuous since it is the square root of a polynomial function
of the coordinates. Finally, since the unit sphere in Rn, {v ∈Rn : ||v|| = 1}, is compact

<!-- page 5 -->
COMPUTING THE NORM OF A MATRIX
5
its continuous image {||Av|| : ||v|| = 1} in R is also compact. Every compact subset of R
contains a maximum point, so we are done.
□
Deﬁnition 3.3. For A ∈Mn(R), ||A|| is the smallest nonnegative real number satisfying
the inequality ||Av|| ≤||A|| ||v|| for all v ∈Rn. This is called the operator norm of A.
Theorem 3.2 shows ||A|| exists and is the maximum of ||Av|| when v runs over the unit
sphere in Rn, so in plain English, ||A|| is the largest amount by which A stretches a vector
on the unit sphere of Rn. The next theorem shows the operator norm on Mn(R) is a vector
space norm and has a host of other nice properties.
Theorem 3.4. For A, B ∈Mn(R) and v, w ∈Rn,
(i) ||A|| ≥0, with equality if and only if A = O.
(ii) ||A + B|| ≤||A|| + ||B||.
(iii) ||cA|| = |c| ||A|| for c ∈R.
(iv) ||AB|| ≤||A|| ||B||. It is typically false that ||AB|| = ||A|| ||B||.
(v) ||A|| = ||A⊤||.
(vi) ||AA⊤|| = ||A⊤A|| = ||A||2. Thus ||A|| =
p
||AA⊤|| =
p
||A⊤A||.
(vii) |(Av, w)| ≤||A|| ||v|| ||w||.
(viii) ||A||sup ≤||A|| ≤n√n ||A||sup and Mn(R) is complete with respect to the metric
coming from the operator norm.
Proof. (i) It is obvious that ||A|| ≥0. If ||A|| = 0 then for all v ∈Rn we have ||Av|| ≤0 ||v|| = 0,
so ||Av|| = 0. Thus Av = 0 for all v ∈Rn, so A = O. The converse is trivial.
(ii) For all v ∈Rn,
||(A + B)v||
=
||Av + Bv||
≤
||Av|| + ||Bv||
≤
||A|| ||v|| + ||B|| ||v||
=
(||A|| + ||B||) ||v|| .
Since ||A + B|| is the least C ≥0 such that ||(A + B)v|| ≤C ||v|| for all v ∈Rn, ||A + B|| ≤
||A|| + ||B||.
(iii) Left to the reader.
(iv) For all v ∈Rn, ||(AB)v|| = ||A(Bv)|| ≤||A|| ||Bv|| ≤||A|| ||B|| ||v||, so the minimality
property of the operator norm implies ||AB|| ≤||A|| ||B||.
To show that generally ||AB|| ̸= ||A|| ||B||, note that if ||AB|| = ||A|| ||B|| for all A and
B in Mn(R) then for nonzero A and B we’d have ||AB|| ̸= 0, so AB ̸= O. That is, the
product of two nonzero matrices is always nonzero. This is false when n > 1, since there
are many nonzero matrices whose square is zero. (We sometimes do have ||AB|| = ||A|| ||B||:
see Exercise 3.2.)
(v) For all v ∈Rn, we get by (2.3) that
||Av||2 = |(Av, Av)| = |(v, A⊤Av)| ≤||v|| ||A⊤Av||
by Cauchy–Schwarz. This last expression is ≤||A⊤A|| ||v||2, so
||Av|| ≤
q
||A⊤A|| ||v|| .

<!-- page 6 -->
6
KEITH CONRAD
The least C ≥0 such that ||Av|| ≤C ||v|| for all v ∈Rn is ||A||, so ||A|| ≤
p
||A⊤A||. Squaring
both sides,
(3.1)
||A||2 ≤||A⊤A|| ≤||A⊤|| ||A|| .
Dividing by ||A|| when A ̸= O, we get ||A|| ≤||A⊤||. This is also obvious if A = O, so
(3.2)
||A|| ≤||A⊤||
for all A ∈Mn(R). Now replace A by A⊤in (3.2) to get
||A⊤|| ≤||(A⊤)⊤|| = ||A|| ,
so ||A|| = ||A⊤||.
(vi) Feeding the conclusion of (v) back into (3.1),
||A||2 ≤||A⊤A|| ≤||A⊤|| ||A|| = ||A||2 ,
so ||A||2 = ||A⊤A||. Using A⊤in place of A here, we get ||A||2 = ||AA⊤|| since ||A⊤|| = ||A||.
(vii) Use Cauchy–Schwarz: |(Av, w)| ≤||Av|| ||w|| ≤||A|| ||v|| ||w||.
(viii) Set v = ej and w = ei in (vii):
|aij| = |(Aej, ei)| ≤||A|| .
Therefore ||A||sup ≤||A||. The other inequality follows from the calculation leading up to
Lemma 3.1.
That Mn(R) is complete with respect to the metric d(A, B) = ||A −B|| coming from
the operator norm follows from completeness of Mn(R) with respect to the metric coming
from the sup-norm (view Mn(R) as Rn2) and the fact that these two norms on Mn(R) are
bounded by constant multiples of each other.
□
The operator norm on Mn(R) interacts nicely with the multiplicative structure on Mn(R)
and the standard inner product on Rn (parts (iv) through (vii) of Theorem 3.4). However,
unlike the standard norm on Rn, the operator norm on Mn(R) is impossible to calculate
from its deﬁnition in all but the simplest cases. For instance, it is clear that ||In|| = 1, so
||cIn|| = |c| for all c ∈R. But what is



1
2
3
4

?
By the last part of Theorem 3.4, this norm is bounded above by 2
√
2(4) = 8
√
2 ≈11.3. In
the next section we will give a formula for the operator norm on Mn(R) that will allow us
to compute ||( 1 2
3 4 )|| easily, and it will turn out to be ≈5.5.
Exercises.
1. Rework this section for rectangular matrices that need not be square. For A in
Mm,n(R), deﬁne its operator norm ||A||m,n to be the least b ≥0 such that ||Av||m ≤
b ||v||n for all v ∈Rn, where the subscripts in the inequality indicate the standard
norm on the Euclidean space of the relevant dimension (m or n). Show ||A||m,n exists
and
||A||m,n = ||A⊤||n,m =
q
||AA⊤||m,m =
q
||A⊤A||n,n.
You will want to use the relationship between the transpose on Mm,n(R) and dot
products on Rm and Rn in Exercise 2.1.

<!-- page 7 -->
COMPUTING THE NORM OF A MATRIX
7
2. An n×n rotation matrix is a matrix R ∈Mn(R) such that RR⊤= In (equivalently,
R⊤R = In), which is the same as the condition ⟨Rv, Rw⟩= ⟨v, w⟩for all v and
w in Rn.
Prove ||R|| = 1 and for every n × n real matrix A, ||AR|| = ||A|| and
||RA|| = ||A||. (Hint: use the submultiplicativity property of the operator norm in
Theorem 3.4(iv).)
3. Deﬁne an operator norm on Mn(C) and establish an analogue of Theorem 3.4. Is it
true that a matrix in Mn(C) generally has the same operator norm as its transpose?
For a real n × n matrix, show its operator norm as an element of Mn(R) equals its
operator norm as an element of Mn(C).
4. A computational formula for the operator norm on Mn(R)
The key idea to compute the operator norm of A ∈Mn(R) is that Theorem 3.4(vi)
tells us ||A|| is the square root of the operator norm of AA⊤and A⊤A.
What makes
AA⊤and A⊤A special is that they are symmetric (equal to their own transposes), e.g.,
(AA⊤)⊤= (A⊤)⊤A⊤= AA⊤.1 The following theorem gives a formula for operator norms
of symmetric matrices and that will lead to an operator norm formula on all matrices in
Mn(R).
Theorem 4.1. (1) If A ∈Mn(R) satisﬁes A⊤= A then all the eigenvalues of A are real
and
(4.1)
||A|| =
max
eigenvalues λ of A |λ|.
(2) For all A ∈Mn(R), the eigenvalues of AA⊤and A⊤A are all nonnegative.
Proof. Proof of (1). To prove that when A⊤= A all the eigenvalues of A are real, let A
act on Cn in the obvious way. Using the standard inner product (2.4) on Cn (not the dot
product!), we have by (2.5) that for all v ∈Cn,
(Av, v) = (v, A∗v) = (v, A
⊤v) = (v, A⊤v) = (v, Av).
For an eigenvalue λ ∈C of A, let v ∈Cn be a corresponding eigenvector. Then
(Av, v) = (λv, v) = λ(v, v),
(v, Av) = (v, λv) = λ(v, v),
so λ = λ since (v, v) = ||v||2 ̸= 0 (eigenvectors are nonzero). Thus λ is real.
To prove (4.1), we give two arguments.
Method 1. We will use a fundamental property of real symmetric matrices called the
Spectral Theorem. It says that each symmetric matrix A ∈Mn(R) has a basis of mutually
orthogonal eigenvectors in Rn.2 Let v1, . . . , vn be a basis of mutually orthogonal eigenvectors
for A, with corresponding eigenvalues λ1, . . . , λn. What is special about orthogonal vectors
is that their squared lengths add (the Pythagorean theorem): if (v, w) = 0 then
||v + w||2 = (v + w, v + w) = (v, v) + 2(v, w) + (w, w) = (v, v) + (w, w) = ||v||2 + ||w||2
and likewise for a sum of more than two mutually orthogonal vectors.
Order the eigenvalues of A so that |λ1| ≤. . . ≤|λn|. For each v ∈Rn, write it in terms
of the basis of eigenvectors as
v = c1v1 + · · · + cnvn.
1This is also true if A ∈Mm,n(R) is a rectangular matrix, which makes Section 4 applicable to operator
norms of rectangular matrices by Exercise 3.1.
2The Spectral Theorem includes the assertion that all eigenvalues of A are real, which we showed above.

<!-- page 8 -->
8
KEITH CONRAD
Then
Av = c1A(v1) + · · · + cnA(vn) = c1λ1v1 + · · · + cnλnvn.
Since the vi’s are mutually perpendicular, their scalar multiples ciλivi are mutually perpen-
dicular. Therefore
||Av||2
=
||c1λ1v1||2 + · · · + ||cnλnvn||2
=
c2
1λ2
1 ||v1||2 + · · · + c2
nλ2
n ||vn||2
≤
c2
1λ2
n ||v1||2 + · · · + c2
nλ2
n ||vn||2
since |λi| ≤|λn|
=
λ2
n(c2
1 ||v1||2 + · · · + c2
n ||vn||2)
=
λ2
n(||c1v1||2 + · · · + ||cnvn||2)
=
λ2
n ||c1v1 + · · · + cnvn||2
=
λ2
n ||v||2 ,
so ||Av|| ≤|λn| ||v||. Since this inequality holds for all v in Rn, we have ||A|| ≤|λn|. To prove
||A|| = |λn| it now suﬃces to ﬁnd a single nonzero vector v such that ||Av|| = |λn| ||v||. For
that we can use v = vn since Avn = λnvn.
Method 2. Our second method of proving (4.1) is a technique that is part of an approach
to proving the Spectral Theorem. It uses a reﬁned version of (4.1) that includes another
formula for ||A|| when A⊤= A:
(4.2)
||A|| = max
||v||=1 |(Av, v)| =
max
eigenvalues λ of A |λ|.
If you don’t want to read through this second method, read ahead to ﬁnd the proof of (2).
To show ||A|| = max||v||=1 |(Av, v)| when3 A⊤= A, ﬁrst we have by Theorem 3.4(vii)
that |(Av, v)| ≤||A|| ||v||2 = ||A|| if ||v|| = 1, so max||v||=1 |(Av, v)| ≤||A||. That maximum
does exist: the function f(v) = |(Av, v)| from Rn to [0, ∞) is continuous, so f achieves a
maximum value on the unit sphere {v ∈Rn : ||v|| = 1} since that sphere is compact (every
continuous real-valued function on a compact set achieves maximum and minimum values).
To prove the reverse inequality ||A|| ≤max||v||=1 |(Av, v)|, set m = max||v||=1 |(Av, v)| ≥0.
We’ll show
(4.3)
||Av|| ≤m ||v||
for all v ∈Rn, so ||A|| ≤m by the deﬁnition of ||A||.
For nonzero v in Rn, v/ ||v|| has norm 1, so |(A(v/ ||v||), v/ ||v||)| ≤m. Since A(v/ ||v||) =
(Av)/ ||v||, we get |(Av, v)| ≤m ||v||2. This inequality is obvious when v = 0, so it holds for
all v in Rn. We now use the Polarization Identity, which is valid for every inner product
and linear map A:
(A(v + w), v + w) −(A(v −w), v −w) = 2((Av, w) + (Aw, v)).
Just expand the left side by additivity to get the right side, thus verifying the identity.
When A = A⊤, the right side is 4(Av, w). Therefore if we take absolute values of both
3This formula for ||A|| has counterexamples if A⊤̸= A: for A = ( 0 −1
1
0 ), (Av, v) = 0 for all v and A ̸= O.

<!-- page 9 -->
COMPUTING THE NORM OF A MATRIX
9
sides,
4|(Av, w)|
≤
m ||v + w||2 + m ||v −w||2
=
m((v + w, v + w) + (v −w, v −w))
=
2m((v, v) + (w, w))
=
2m(||v||2 + ||w||2).
When ||v|| = 1 and ||w|| = 1, this implies 4|(Av, w)| ≤4m, so |(Av, w)| ≤m if ||v|| = ||w|| = 1.
Scaling, this implies for all v and w in Rn that |(Av, w)| ≤m ||v|| ||w||. Now set w = Av. We
get
||Av||2 = |(Av, Av)| ≤m ||v|| ||Av|| .
Therefore ||Av|| ≤m ||v|| if Av ̸= 0. It is also obvious if Av = 0, so we have proved (4.3),
which proves the ﬁrst equation in (4.2).
To prove the rest of (4.2), let λ be an eigenvalue of A and v be a corresponding eigenvector
in Rn. (We already showed every eigenvalue of A is real when A = A⊤, so each eigenvalue
of A has a real eigenvector.) We can normalize v so that ||v|| = 1. Then Av = λv ⇒||Av|| =
||λv|| = |λ| ||v|| = |λ|, so |λ| = ||Av|| ≤||A|| ||v|| = ||A||. Therefore the maximal absolute value
of the eigenvalues of A is at most ||A||. To ﬁnish the proof of (4.2), we’ll show ||A|| or −||A||
is an eigenvalue of A, by using the formula ||A|| = max||v||=1 |(Av, v)| that we already proved.
Let v′ ∈Rn satisfy ||v′|| = 1 and |(Av′, v′)| = ||A||. Set α = (Av′, v′) = ± ||A||. We will
show Av′ = αv′, so α is an eigenvalue of A:
Av′ −αv′2
=
(Av′ −αv′, Av′ −αv′)
=
(Av′, Av′) −α(Av′, v′) −α(v′, Av′) + α2(v′, v′)
=
Av′2 −α(Av′, v′) −α(A⊤v′, v′) + α2.
Since A⊤= A,
Av′2 −α(Av′, v′) −α(Av′, v′) + α2 =
Av′2 −α2 −α2 + α2 =
Av′2 −α2
and ||Av′|| ≤||A|| ||v′|| = ||A||, so
0 ≤
Av′ −αv′2 ≤||A||2 −α2 = ||A||2 −||A||2 = 0.
Therefore ||Av′ −αv′|| = 0, so Av′ = αv′.
Proof of (2). Since AA⊤and A⊤A are both symmetric, all their eigenvalues are real. Let
λ ∈R be an eigenvalue of AA⊤with corresponding eigenvector v ∈Rn, and let µ ∈R be
an eigenvalue of A⊤A with corresponding eigenvector w ∈Rn. Using the standard inner
product on Rn,
0 ≤(Aw, Aw) = (w, A⊤Aw) = (w, µw) = µ(w, w).
Then µ ≥0 since (w, w) = ||w||2 > 0. Similarly,
0 ≤(A⊤v, A⊤v) = (v, AA⊤v) = (v, λv) = λ(v, v).
Since (v, v) = ||v||2 > 0, it follows that λ ≥0.
□
Remark 4.2. The second equality in (4.2), max||v||=1 |(Av, v)| = maxλ |λ|, is also true
without the absolute values: the maximum value of (Av, v) over all v ∈Rn with ||v|| = 1
is the maximum eigenvalue of A. And if we order all the eigenvalues of a real symmetric

<!-- page 10 -->
10
KEITH CONRAD
n×n matrix A as λ1 ≤λ2 ≤· · · ≤λn then the kth smallest eigenvalue λk has a “min-max”
formula:
λk = min
W
max
w∈W
||w||=1
(Aw, w),
where the minimum runs over all subspaces W of Rn with dimension k. (At k = n, the
only such W is Rn, so the biggest eigenvalue of A is the maximum of (Aw, w) where w runs
over vectors in Rn with unit length.) If instead we order the eigenvalues of A from greatest
to least as µ1 ≥µ2 ≥· · · ≥µn (so µk = λn+1−k), then the kth largest eigenvalue µk has a
“max-min” formula:
µk = max
W
min
w∈W
||w||=1
(Aw, w),
where the maximum runs over all subspaces W of Rn with dimension k.4
Corollary 4.3. For A ∈Mn(R), ||A|| is the square root of the largest eigenvalue of AA⊤
and is the square root of the largest eigenvalue of A⊤A.
Proof. By Theorem 3.4(vi), ||A|| =
p
||AA⊤|| =
p
||A⊤A||. Now use (4.1), with AA⊤and
A⊤A in place of A.
□
Remark 4.4. This corollary, without proof, goes back to Peano [3, p. 454] using A⊤A.
On the same page Peano introduced the operator norm on Mn(R) from Deﬁnition 3.3 and
proved Theorem 3.4(ii) and (iv). In the same year (1888) Peano [4] introduced the ﬁrst
axiomatic treatment of real vector spaces (which he called “linear systems”) of arbitrary
dimension and linear operators on them; it was ahead of its time and largely forgotten,
including by Peano himself. The main inspiration for the development of abstract linear
algebra came from work on normed vector spaces by Banach in the 1920s [2].
Example 4.5. Let’s compute the operator norm of the 2 × 2 matrix
A =

1
2
3
4

.
Since
AA⊤=

5
11
11
25

,
the characteristic polynomial of AA⊤is X2 −30X + 4, which has eigenvalues 15 ±
√
221 ≈
.13, 29.86. Therefore the operator norm of A is
p
15 +
√
221, so for all
 x
y

∈R2,


 5x + 11y
11x + 25y

 ≤
q
15 +
√
221


x
y

 ,
and
p
15 +
√
221 ≈5.46 is the smallest number with that property.
Example 4.6. For the 2 × 2 matrix
A =

3
2
1
2

,
we have
AA⊤=

13
7
7
5

,
4See https://en.wikipedia.org/wiki/Min-max theorem.

<!-- page 11 -->
COMPUTING THE NORM OF A MATRIX
11
which has characteristic polynomial X2 −18X + 16 and eigenvalues 9 ±
√
65, so ||A|| =
p
9 +
√
65 ≈4.13.
The matrix A has characteristic polynomial X2 −5X + 4 = (X −1)(X −4), so its
eigenvalues are 1 and 4.
This makes A conjugate to the diagonal matrix D = ( 4 0
0 1 ):
A = UDU−1, where U = ( 2
1
1 −1 ). Since D is symmetric, ||D|| = 4 < ||A||. This illustrates that
conjugate matrices like A and D need not have the same operator norm, although matrices
that are conjugate by a rotation matrix have the same operator norm:
RAR−1 = ||A|| if
RR⊤= In (see Exercise 3.2). The conjugating matrix U is not a rotation matrix.
Computing the operator norm of A amounts to ﬁnding the largest eigenvalue of a related
symmetric matrix (AA⊤or A⊤A). In practice, for large symmetric matrices the largest
eigenvalue is not computed by calculating the roots of its characteristic polynomial. More
eﬃcient algorithms for calculating eigenvalues are available (e.g., QR algorithm or Lanczos
algorithm).
Exercises.
1. For A ∈Mm,n(R), show the eigenvalues of the m × m matrix AA⊤and the n × n
matrix A⊤A are nonnegative. (The nonzero eigenvalues of these matrices are also
equal. For all A ∈Mm,n(R) and B ∈Mn,m(R), the matrices AB ∈Mm(R) and
BA ∈Mn(R) have the same nonzero eigenvalues.)
2. If you worked out properties of operator norms of rectangular matrices in Exercise
3.1, then show the operator norm of the 2 × 3 matrix

1
2
3
4
5
6

is
q
(91 +
√
8065)/2.
3. If we use a norm on Rn other than the standard norm, the corresponding operator
norm on Mn(R) will be diﬀerent from the one we have worked with here. When Rn
has a norm ||·||′, the related operator norm of a matrix A ∈Mn(R) is the least b ≥0
such that ||Av||′ ≤b ||v||′ for all v ∈Rn. Let’s consider this in two examples: the
sup-norm ||(x1, . . . , xn)||sup = max |xi| and the 1-norm ||(x1, . . . , xn)||1 = Pn
i=1 |xi|.
(a) For all v ∈Rn, show ||Av||sup ≤rA ||v||sup where rA = max1≤i≤n
Pn
j=1 |aij|.
The number rA is the maximum sum of the absolute values along the rows of A.
(b) For each row (ai1, . . . , ain) of A, show there is a vector vi in Rn with coordi-
nates from {±1} such that the ith entry of Avi equals |ai1| + · · · + |ain|. Conclude
that there is a nonzero v ∈Rn such that ||Av||sup = rA ||v||sup where rA is the number
in part (a). Thus the operator norm of A when using the sup-norm on Rn is rA.
(c) For all v ∈Rn, show ||Av||1 ≤cA ||v||1 where cA = max1≤j≤n
Pn
i=1 |aij|, which
is the maximum sum of the absolute values along the columns of A.
(d) Let ek be the kth standard basis vector of Rn. Show ||Aek||1 = Pn
i=1 |aik| and
conclude there is a nonzero v ∈Rn such that ||Av||1 = cA ||v||1, so the operator norm
of A when using the 1-norm on Rn is cA.
Note: For p ≥1 the p-norm on Rn is ||(x1, . . . , xn)||p =
ppP |xi|p. The stan-
dard norm on Rn is the 2-norm and the sup-norm is a limit of p-norms: ||v||∞=
limp→∞||v||p. It is unlikely that there is an eﬃcient algorithm to compute the oper-
ator p-norm of a general n × n real matrix when p ̸= 1, 2, ∞; see [1].

<!-- page 12 -->
12
KEITH CONRAD
4. Generalize Theorem 4.1 to give a computational formula for the operator norm of
matrices in Mn(C).
Appendix A. Proof of Cauchy-Schwarz inequality
We give a proof of the Cauchy–Schwarz inequality that was found by Schwarz [5, p. 344]
in 1888. It is a clever trick with quadratic polynomials and the context in which Schwarz
discovered it is described in [6, pp. 10–11]. (The whole book [6] is recommended as a lively
account of fundamental inequalities in mathematics.)
Let V be a real vector space with an inner product (·, ·). Pick v and w in V . Our goal
is to show
|(v, w)| ≤||v|| ||w|| .
This is obvious if v or w is 0, so assume both are nonzero. For all t ∈R, (v+tw, v+tw) ≥0.
The left side can be expanded to be a quadratic polynomial in t:
(v + tw, v + tw)
=
(v, v) + (v, tw) + (tw, v) + (tw, tw)
=
(v, v) + t(v, w) + t(w, v) + t2(w, w)
=
||v|| + 2(v, w)t + ||w|| t2.
This is quadratic since ||w|| > 0. A quadratic polynomial in t has nonnegative values for all
t if and only if its discriminant is ≤0, so
(2(v, w))2 −4 ||v|| ||w|| ≤0,
which is equivalent to |(v, w)| ≤||v|| ||w||, and that completes the proof!
Remark A.1. We have equality |(v, w)| = ||v|| ||w|| if and only if the quadratic polynomial
above has a double real root t, and at that root we get (v +tw, v +tw) = 0, so v +tw = 0 in
V and thus v and w are linearly dependent. The converse direction, that linear dependence
implies equality in the Cauchy–Schwarz inequality, is left to the reader (also in the case
that v or w is 0).
References
[1] J. M. Hendrickx, A. Olshevsky, Matrix p-norms are NP-hard to approximate if p ̸= 1, 2, ∞, SIAM J.
Matrix Anal. Appl. 31 (2010), 2802–2812. URL https://arxiv.org/abs/0908.1397.
[2] G. H. Moore, The Axiomatization of Linear Algebra: 1875–1940, Historia Mathematica 22 (1995), 262–
303. URL https://core.ac.uk/download/pdf/82128888.pdf.
[3] G. Peano, Int´egration par s´eries des ´equations diﬀ´erentielles lin´eaires, Mathematische Annalen 32 (1888),
450–456. URL https://eudml.org/doc/157389.
[4] G. Peano, “Calcolo Geometrico secondo l’Ausdehnungslehre di H. Grassmann, preceduto dalle operazioni
della logica deduttiva,” Fratelli Bocca, Turin, 1888. URL http://mathematica.sns.it/opere/138/.
[5] H. A. Schwarz,
¨Uber ein die Fl¨achen kleinsten Fl¨acheninhalts betreﬀendes Problem der Vari-
ationsrechnung,
Acta Soc. Scient. Fenn. 15 (1888),
315–362. URL https://www.biodiversity
library.org/item/52183#page/323/mode/1up.
[6] J. M. Steele, “The Cauchy–Schwarz Master Class: An Introduction to the Art of Mathematical Inequal-
ities,” Cambridge Univ. Press, Cambridge, 2004.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*