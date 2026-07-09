# Quaternionalg

> **Source**: https://kconrad.math.uconn.edu/blurbs/quaternionalg.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
QUATERNION ALGEBRAS
KEITH CONRAD
1. Introduction
A complex number is a sum a+bi with a, b ∈R and i2 = −1. Addition and multiplication
are given by the rules
(1.1) (a + bi) + (c + di) = (a + c) + (b + d)i,
(a + bi)(c + di) = (ac −bd) + (ad + bc)i.
This deﬁnition doesn’t explain what i “is”. In 1833, Hamilton [3, p. 81] proposed bypassing
the mystery about the meaning of i by declaring a + bi to be an ordered pair (a, b). That
is, he deﬁned C to be R2 with addition and multiplication rules inspired by (1.1):
(a, b) + (c, d) = (a + c, b + d),
(a, b)(c, d) = (ac −bd, ad + bc).
The additive identity is (0, 0), the multiplicative identity is (1, 0), and from addition and
scalar multiplication of real vectors we have (a, b) = (a, 0) + (0, b) = a(1, 0) + b(0, 1), which
looks like a + bi if we deﬁne i to be (0, 1). Real numbers occur as the pairs (a, 0).
Hamilton asked himself if it was possible to multiply triples (a, b, c) in a nice way that
extends multiplication of complex numbers (a, b) when they are thought of as triples (a, b, 0).
In 1843 he discovered a way to multiply in four dimensions, not three, at the cost of
abandoning commutativity of multiplication. His construction is called the quaternions.
After meeting the quaternions in Section 2, we will see in Section 3 how they can be gen-
eralized to a construction called a quaternion algebra. Sections 4 and 5 explore quaternion
algebras over ﬁelds not of characteristic 2.
2. Hamilton’s Quaternions
Deﬁnition 2.1. The quaternions are
H = {a + bi + cj + dk : a, b, c, d ∈R},
where the following multiplication conditions are imposed:
• i2 = j2 = k2 = −1,
• ij = k, ji = −k, jk = i, kj = −i, ki = j, ki = j, ik = −j,
• every a ∈R commutes with i, j, and k.
To remember the rules for multiplying i, j, and k by each other, put them in alphabetical
order around a circle as below. Products following this order get a plus sign, and products
going against the order get a minus sign, e.g., jk = i and ik = −j.
i
j
k
1

<!-- page 2 -->
2
KEITH CONRAD
The rules for multiplication among i, j, and k are enough, with the distributive law, to
multiply all quaternions.
Example 2.2. (i + j)(i −j) = i2 −ij + ji −j2 = −1 −k −k −(−1) = −2k, while
i2 −j2 = −1 −(−1) = 0.
Example 2.3. A quaternion with a = 0 is called a pure quaternion, and the square of a
pure quaternion is a negative sum of three squares:
(2.1)
(bi + cj + dk)2 = −b2 −c2 −d2.
The multiplicative rules involving i, j, and k can be derived from i2 = j2 = −1 and
ij = k = −ji using associativity, e.g.,
k2 = (ij)(ij) = (ij)(−ji) = i(−j2)i = i(−(−1))i = i2 = −1
and
jk = j(ij) = (ji)j = (−ij)j = −i(jj) = −i(−1) = i,
ik = i(ij) = (ii)j = −j.
While multiplication in H is typically noncommutative, multiplication in H by real num-
bers is commutative: aq = qa when a ∈R and q ∈H. This commuting property singles
out R inside H: the only quaternions that commute with all quaternions are real numbers
(Exercise 2.2). In the terminology of ring theory, the set of elements of a ring that commute
with every element of the ring is called the center of the ring, so the center of H is R. The
ring M2(R) also has center R: the matrices in M2(R) that commute with all matrices in
M2(R) are the scalar diagonal matrices ( a 0
0 a ) = aI2, which is a natural copy of R in M2(R).
For a quaternion q = a + bi + cj + dk, its conjugate q is deﬁned to be
q = a −bi −cj −dk.
This is analogous to complex conjugation on C, where a + bi = a−bi. Complex conjugation
interacts well with addition and multiplication in C:
z + w = z + w,
zw = z w.
For z = a + bi in C, zz = a2 + b2. The absolute value |a + bi| is deﬁned to be
√
a2 + b2, so
|z|2 = zz. If z ̸= 0 in C then |z| > 0 and 1/z = z/|z|2.
Conjugation on H has properties similar to conjugation on C: in H,
(2.2)
q1 + q2 = q1 + q2,
q1q2 = q2 q1,
q = q.
Note that conjugation switches the order of multiplication. The norm of q is
N(q) = qq = a2 + b2 + c2 + d2.
Check that q commutes with its conjugate: qq = qq.
Since q1q2 = q2 q1, the norm is
multiplicative:
(2.3)
N(q1q2) = q1q2q1q2 = q1q2q2 q1 = q1 N(q2)q1 = q1q1 N(q2) = N(q1) N(q2).
If q ̸= 0 then N(q) > 0, so q/ N(q) is an inverse for q on both the left and right:
q
q
N(q) =
q
N(q)q = N(q)
N(q) = 1.
Example 2.4. The quaternion i + j has conjugate −i −j and norm 2, so the inverse of
i + j is 1
2(−i −j).

<!-- page 3 -->
QUATERNION ALGEBRAS
3
A ring in which every nonzero element has a two-sided multiplicative inverse is called
a division ring, so H is a division ring. We set H× = H −{0}, just like with ﬁelds. A
commutative division ring is a ﬁeld, and the center of a division ring is a ﬁeld (Exercise
2.3). The quaternions were the ﬁrst example of a noncommutative division ring, and the
following theorem provides a conceptual role for them in algebra among all division rings.
Theorem 2.5 (Frobenius, 1878). Each division ring with center R that is ﬁnite-dimensional
as a vector space over R is isomorphic to R or H.
Proof. See [4, pp. 219–220].
□
Theorem 2.5 does not include C, even though it is a division ring and is ﬁnite-dimensional
over R, since the center of C is C, not R.
The term “conjugation” has two meanings: the operation q 7→q (generalizing complex
conjugation) and the operation x 7→qxq−1 for q ̸= 0 (conjugation in the sense of group
theory). The four-dimensional space H can be used to describe rotations in R3 by using
conjugation in the second sense on the three-dimensional subspace of pure quaternions in
H, which is described in Exercise 2.8 (a), (c). See also [2, Chap. 7] or [6, Sect. 5]. In
computer code, the composition of rotations when described in terms of multiplication of
quaternions has some advantages over other approaches to rotations (no “gimbal lock” and
less data to store: 4 coordinates of a quaternion vs. 9 components of a matrix). This makes
quaternions a practical tool in computer graphics (search on the internet for “slerp”).
The complex numbers are a 2-dimensional vector space over R, so the set EndR(C)
of all R-linear maps C →C is a noncommutative ring that is isomorphic to M2(R) by
using an R-basis of C to turn R-linear maps C →C into 2 × 2 real matrices. To each
complex number z = a + bi, associate the R-linear map mz : C →C, where mz(w) = zw.
Not only is each mz an R-linear map C →C, but mz is additive and multiplicative in z:
mz+z′ = mz + mz′ and mzz′ = mz ◦mz′ as mappings C →C. Therefore z 7→mz is a ring
homomorphism C →EndR(C) and it is injective since mz(1) = z.
Using the R-basis {1, i} for C, mz has matrix representation ( a −b
b
a ) since mz(1) = a + bi
(1st column) and mz(i) = zi = −b + ai (2nd column). Therefore a + bi 7→( a −b
b
a ) is an
embedding of rings C →M2(R).
That means the 2 × 2 real matrices ( a −b
b
a ) add and
multiply in the same way as complex numbers do in (1.1):

a
−b
b
a

+

c
−d
d
c

=

a + c
−(b + d)
b + d
a + c

,

a
−b
b
a
 
c
−d
d
c

=

ac −bd
−(ad + bc)
ad + bc
ac −bd

.
Complex conjugation and the squared absolute value of a complex number z can be de-
scribed in terms of matrix operations on [mz]: [mz] = [mz]⊤and |z|2 = det[mz].
To express H in terms of 2 × 2 complex matrices, we want to convert each quaternion
into a C-linear map H →H, since M2(C) consists of C-linear maps C2 →C2 and H is
2-dimensional as a complex vector space, so H ∼= C2 as C-vector spaces once we pick a
C-basis of H. This requires care because C does not commute with H, e.g., ij = −ji and
ik = −ki. We can view H as a left C-vector space (z · q = zq) or as a right C-vector space
(z · q = qz), and the choice aﬀects whether a particular mapping H →H is C-linear.
Example 2.6. For each q ∈H the mapping ℓq : H →H where ℓq(x) = qx for all x ∈H,
is C-linear when H is a right C-vector space but not when H is a left C-vector space: for

<!-- page 4 -->
4
KEITH CONRAD
z ∈C, q(xz) = (qx)z always, but typically q(zx) ̸= z(qx) (if x ̸= 0, z ∈C −R, and
q ∈H −C).
As both a left and right vector space over C, H has basis {1, j}: for a, b, c, d ∈R,
a + bi + cj + dk = (a + bi) + (c + di)j = (a + bi) + j(c −di).
Therefore each q ∈H can be written uniquely as z + wj for some z, w ∈C or as z + jw
for some z, w ∈C. Passing between {1, j} as a left C-basis and a right C-basis involves
complex conjugation of the coeﬃcient of j: since ij = −ji,
z + wj = z + jw,
z + jw = z + wj.
H as a right C-vector space. For q ∈H, let ℓq : H →H by ℓq(x) = qx. Each ℓq is
C-linear, e.g., ℓq(xz) = q(xz) = (qx)z = ℓq(x)z, and ℓq is additive and multiplicative in q
(e.g., ℓq1 ◦ℓq2 = ℓq1q2). We can recover q from ℓq since ℓq(1) = q. Therefore q 7→ℓq is an
embedding H →EndC(H) that is additive and multiplicative. Using the basis {1, j} for
H as a right C-vector space, if we write q = z + jw for z, w ∈C then ℓq(1) = q = z + jw
and ℓq(j) = qj = zj + jwj = jz + j(jw) = −w + jz. Therefore H embeds additively and
multiplicatively into M2(C) by
(2.4)
q = z + jw 7→[ℓq] =

z
−w
w
z

.
For example,
[ℓi] =

i
0
0
−i

,
[ℓj] =

0
−1
1
0

,
[ℓk] =

0
−i
−i
0

.
This embedding could be used to prove multiplication in H is associative since multiplication
is associative in M2(C).
H as a left C-vector space.
For q ∈H, let rq : H →H by rq(x) = xq.
This is C-
linear, e.g., rq(zx) = (zx)q = z(xq) = zrq(x). We use q in the deﬁnition of rq to make rq
multiplicative in q: for all x ∈H, (rq1 ◦rq2)(x) = xq2 q1 = xq1q2 = rq1q2(x), so rq1 ◦rq2 =
rq1q2. Since rq(1) = q, we can recover q from rq, so q 7→rq is an embedding H →EndC(H)
that is additive and multiplicative. Using the basis {1, j} for H as a left C-vector space, if
we write q = z + wj for z, w ∈C then
rq(1) = q = z + wj = z + j w = z −jw = z −wj
and
rq(j) = jq = j(z −wj) = zj −wjj = w + zj.
Therefore H embeds additively and multiplicatively into M2(C) by
(2.5)
q = z + wj 7→[rq] =

z
w
−w
z

.
For example,
[ri] =

−i
0
0
i

,
[rj] =

0
1
−1
0

,
[rk] =

0
−i
−i
0

.
While the two embeddings H →M2(C) in (2.4) and (2.5) are diﬀerent functions (they
have diﬀerent eﬀects on i and on j), their images are the same: in both cases, the image
is the set of complex matrices whose diagonal entries are complex conjugates and whose
oﬀ-diagonal entries are negative complex conjugates.

<!-- page 5 -->
QUATERNION ALGEBRAS
5
Conjugation on H and the norm on H can be described in terms of matrix operations
using either of the above 2 × 2 matrix representations of H: by writing
(2.6)
[ℓq] = [ℓq]
⊤and
N(q) = det[ℓq],
[rq] = [rq]
⊤and
N(q) = det[rq].
For example, the ﬁrst equation says the matrix representation of left multiplication by q on
H as a right C-vector space using the basis {1, j} is the transpose of the complex conjugate
of the matrix [ℓq].
Exercises.
1. Verify properties of quaternionic conjugation: q1 + q2 = q1 + q2, q1q2 = q2q1, q = q,
cq = cq for c ∈R, and q = q ⇔q ∈R.
2. Show the center of H is R: {q ∈H : qq′ = q′q for all q′ ∈H} = R.
3. Show the center of a division ring is a ﬁeld. (The main point is to show the inverse
of a nonzero element in the center is also in the center.)
4. Verify the equations in (2.6).
5. Let f : H →M2(C) by f(z+wj) = ( z −w
w
z ) where z, w ∈C. Show (i) f is an injective
ring homomorphism with the same image as (2.4) and (2.5), (ii) det([fq]) = N(q),
and (iii) f is not C-linear when H is viewed as either a left C-vector space or as a
right C-vector space.
6. Verify that the image of C in M2(R) under the embedding a + bi 7→( a −b
b a ) is
{A ∈M2(R) : ( 0 −1
1 0 )A = A( 0 −1
1 0 )} and the common image of H in M2(C) from the
embeddings (2.4) and (2.5) is {A ∈M2(C) : ( 0 −1
1 0 )A = A( 0 −1
1 0 )}, where A is the
matrix with entries that are complex conjugates of the entries of A.
7. For q ∈H×, let Rq : H →H by Rq(r) = qrq−1.
a) Show Rq is a ring automorphism of H.
b) Show Rq1 ◦Rq2 = Rq1q2. Does Rq1+q2 = Rq1 + Rq2?
c) For q, q′ ∈H×, show Rq(r) = Rq′(r) for all r ∈H if and only if q′ = cq for
some c ∈R×.
8. Let H0 = Ri + Rj + Rk. These are the pure quaternions. Deﬁne Tr: H →R by
Tr(q) = q + q = 2a, where a is the real component of q. The number Tr(q) is called
the trace of q. Then H0 = {q ∈H : Tr(q) = 0}.
a) Show Tr(qq′) = Tr(q′q) for all q and q′ in H. Use this to show Rq(H0) = H0
for all q ∈H×, where Rq is deﬁned in the previous exercise.
b) If Rq(r) = Rq′(r) for all r ∈H0, is q′ = cq for some c ∈R×?
c) Show H0 = {q ∈H : q2 ≤0}, and use this to prove in another way that
Rq(H0) = H0 for all q ∈H×.
d) For q ∈H, show q2 = −1 if and only if q = bi + cj + dk with b2 + c2 + d2 = 1.
That is, the solutions to q2 + 1 = 0 in H form a sphere of pure quaternions.
9. Identify H0 with R3 by bi + cj + dk ↔(b, c, d). If q = bi + cj + dk, write q for
(b, c, d) as a vector in R3.
a) Show multiplication of pure quaternions can be described in terms of the dot
product and cross product on R3: q1, q2 ∈H0 =⇒q1q2 = −(q1 · q2) + q1 × q2,
where the cross product q1 × q2 is computed in R3 and then viewed as a pure
quaternion. In particular, q1 and q2 are perpendicular in R3 if and only if q1 and
q2 anti-commute (that is, q1q2 = −q2q1).

<!-- page 6 -->
6
KEITH CONRAD
b) What are the constraints on the coordinates of x1i + x2j + x3k in order for it
to anti-commute with i + j?
c) For q1, q2, q3 ∈H0, show
q1 × (q2 × q3) = 1
2(q1q2q3 −q2q3q1).
3. Quaternion Algebras: Introduction
Let F be a ﬁeld. Hamilton’s quaternions H can be generalized to allow coeﬃcients in F:
H(F) = {a + bi + cj + dk : a, b, c, d, ∈F}
where i, j, and k have the same multiplicative rules as in H = H(R). Conjugation and the
norm on H(F) are deﬁned in the same way as in H, and their properties in (2.2) and (2.3)
continue to be valid. If F does not have characteristic 2, so 1 ̸= −1 in F, then the center
of H(F) is F. If F has characteristic 2 then H(F) is commutative. From now on, F is
assumed to have characteristic not 2.
Example 3.1. The ring H(Q) is a division ring since it is a subring of the division ring
H(R) and the inverse of a nonzero element q of H(Q) in H(R) is q/ N(q), which is in H(Q).
Example 3.2. The ring H(F7) is not a division ring: 22+32+12 = 0 in F7, so (2i+3j+k)2 =
−22 −32 −12 = 0 using (2.1) in H(F7).
A quaternion that squares to 0 can’t have a
multiplicative inverse, so 2i+3j +k is a nonzero element of H(F7) without a multiplicative
inverse in H(F7).
A broader generalization of H than H(F) was introduced by Dickson in 1906 [1].
Deﬁnition 3.3. A quaternion algebra over F is a ring containing F that is a 4-dimensional
vector space over F with a basis 1, u, v, w having the following multiplicative relations:
u2 ∈F ×, v2 ∈F ×, w = uv = −vu, and every c ∈F commutes with u and v. Setting
a = u2 and b = v2, this ring is denoted (a, b)F .
More explicitly, for a and b in F × the ring (a, b)F looks as follows. As a vector space
over F it can be written as
(a, b)F = F + Fu + Fv + Fw,
and the multiplicative relations among u, v, w, and elements of F are
• u2 = a and v2 = b,
• w := uv = −vu,
• every c ∈F commutes with u and v.
Example 3.4. In this notation H(F) = (−1, −1)F , so this is a quaternion algebra where
a = b = −1.
In Table 1 are products among u, v, and w, where each entry is the product of the
row label times the column label (in that order: multiplication is noncommutative). For
example, vw = v(uv) = (vu)v = −uv2 = −ub = −bu. Note u, v, and w each square to a
nonzero element of F and they anti-commute: uv = −vu, uw = −wu, and vw = −wv.
We can make a circular diagram for products of u, v, and w that is similar to the one
for i, j, and k. In the picture below we write u, v, and w in alphabetical order, with 1
on the arc from u to v, −b on the arc from v to w, and −a on the arc from w to u. The
product of two of u, v, and w is the third one times the number on the arc between the

<!-- page 7 -->
QUATERNION ALGEBRAS
7
u
v
w
u
a
w
av
v
−w
b
−bu
w
−av
bu
−ab
Table 1. Products of u, v, and w in (a, b)F .
two factors, with an additional sign if the multiplication is going against the arrows, e.g.,
vw = (−b)u = −bu and uw = −(−a)v = av.
u
v
w
1
−a
−b
Example 3.5. We have (2, 3)Q = Q + Qu + Qv + Qw where u2 = 2, v2 = 3, and
w = uv = −vu with w2 = −6.
The multiplicative rules on u, v, and w are consistent with the axioms of a ring because we
can realize the operations in (a, b)F as addition and multiplication of certain 2 × 2 matrices
(Exercise 3.8). Since F doesn’t have characteristic 2, (a, b)F is noncommutative because u
and v don’t commute. The center of (a, b)F is F (Exercise 3.2).
For q = x0 + x1u + x2v + x3w, deﬁne the conjugate and norm of q to be
(3.1)
q = x0 −x1u −x2v −x3w,
N(q) = qq = x2
0 −ax2
1 −bx2
2 + abx2
3.
As with H, qq = qq in (a, b)F and the calculations in (2.2) and (2.3) remain valid, so the
norm is a multiplicative function (a, b)F →F.
Example 3.6. For q = x0 + x1u + x2v + x3w in (2, 3)Q,
N(q) = x2
0 −2x2
1 −3x2
2 + 6x2
3.
Example 3.7. Generalizing Example 2.3, an element of (a, b)F with x0 = 0 is called a pure
quaternion. Its square is a scalar: for x, y, z ∈F,
(3.2)
(xu + yv + zw)2 = ax2 + by2 −abz2 ∈F.
This property essentially characterizes the pure quaternions (Exercise 3.6 ii).
Theorem 3.8. An element q of (a, b)F has a two-sided multiplicative inverse in (a, b)F if
and only if N(q) ̸= 0.
Proof. Suppose qq′ = 1 for some q′. Then N(q) N(q′) = N(1) = 1 in F, so N(q) ∈F ×.
Conversely, suppose N(q) ∈F ×. Since N(q) commutes with all elements of (a, b)F , the
equation N(q) = qq = qq can be rewritten as
q ·
1
N(q)q =
1
N(q)q · q = 1,
so q/ N(q) is a 2-sided inverse of q.
□
Here are quaternion algebras over Q besides H(Q) that are division rings.

<!-- page 8 -->
8
KEITH CONRAD
Theorem 3.9. Let a be an integer and p be an odd prime such that a ̸≡□mod p.1 Then
(a, p)Q is a division ring.
Proof. By Theorem 3.8, to show (a, p)Q is a division ring it suﬃces to show every nonzero
element of (a, p)Q has a nonzero norm. We will prove the contrapositive: an element of
(a, p)Q with norm 0 must be 0.
Let q = x0 + x1u + x2v + x3w in (a, p)Q. Using the formula for N(q) in (3.1),
N(q) = x2
0 −ax2
1 −px2
2 + apx2
3,
so we can’t show N(q) = 0 ⇒q = 0 using positivity as we can for H: N(q) can be either
positive or negative. To show N(q) = 0 ⇒q = 0, the property a ̸≡□mod p will be crucial.
If N(q) = 0 then
(3.3)
x2
0 −ax2
1 −px2
2 + apx2
3 = 0 =⇒x2
0 −ax2
1 = p(x2
2 −ax2
3).
Multiplying through the last equation by a common denominator of x0, x1, x2, and x3, we
can assume the xi’s are all in Z. Then if we reduce mod p,
x2
0 −ax2
1 ≡0 mod p =⇒x2
0 ≡ax2
1 mod p.
If x1 ̸≡0 mod p then we can solve for a mod p in the congruence to see that a ≡□mod p,
which is false. Therefore x1 ≡0 mod p, so x2
0 ≡0 mod p, and thus x0 ≡0 mod p. Then
in x2
0 −ax2
1 = p(x2
2 −ax2
3) the left side is divisible by p2, so x2
2 −ax2
3 ≡0 mod p, and an
argument similar to the one above shows x2 and x3 are divisible by p.
Since every xi is divisible by p, write xi = px′
i with x′
i ∈Z. Then
x2
0 −ax2
1 = p(x2
2 −ax2
3) =⇒p2(x′2
0 −ax′2
1 ) = p(p2)(x′2
2 −ax′2
3 ) =⇒x′2
0 −ax′2
1 = p(x′2
2 −ax′2
3 ).
This last equation is the same as the right side of (3.3), with x′
i in place of xi. Then as
before, each x′
i is divisible by p, so each xi is divisible by p2. Repeating this argument shows
each xi is divisible by arbitrarily high powers of p, so each xi must be 0.
□
Example 3.10. The rings (2, 3)Q and (2, 5)Q are division rings since 2 mod 3 and 2 mod 5
are not squares.
Example 3.11. For prime p with p ≡3 mod 4, (−1, p)Q is a division ring since −1 ̸≡
□mod p. We will look at (−1, p)Q for p ̸≡3 mod 4 in Example 4.19.
Remark 3.12. The converse of Theorem 3.9 is false: (a, p)Q can be a division ring when
a ≡□mod p. For example, 3 ≡□mod 11 and (3, 11)Q is a division ring (Example 4.2).
Quaternion algebras are related to hyperbolic manifolds [7], number theory [8, Chap. 5],
[9, §III.9], [10], and quadratic forms [5, Chap. III].
Exercises.
1. Verify the multiplication table for u, v, w in Table 1.
2. Show the center of (a, b)F is F.
3. Show the set of elements of (a, b)F that anti-commute with u is Fv + Fw, and the
elements of (a, b)F that anti-commute with u and square to b are those xv + yw
(x, y ∈F) such that x2 −ay2 = 1.
1Here and later, □means a square: something of the form x2. So a ̸≡□mod p it means a is not a square
mod p.

<!-- page 9 -->
QUATERNION ALGEBRAS
9
4. (Conjugation and norm)
a) Check properties of conjugation on (a, b)F : q1 + q2 = q1 + q2, q1q2 = q2q1,
q = q, cq = cq for c ∈F, and q = q ⇔q ∈F.
b) For q = x0 + x1u + x2v + x3w, show qq = qq = x2
0 −ax2
1 −bx2
2 + abx2
3.
5. For a ∈Z, show that if a ≡3 or 5 mod 8 then (a, 2)Q is a division ring. This should
be considered an analogue of Theorem 3.9 when p = 2.
6. Let (a, b)0
F = Fu + Fv + Fw be the pure quaternions in (a, b)F .
(i) If r is pure and q is invertible in (a, b)F , show qrq−1 is pure.
(Hint: Set
Tr(q) = q + q, show Tr has properties similar to the trace on H, and show (a, b)0
F =
{q ∈(a, b)F : Tr(q) = 0}.)
(ii) For q ∈(a, b)F , show q2 ∈F ⇐⇒q ∈F or q is pure. Therefore the pure
quaternions in (a, b)F are precisely the q satisfying q2 ∈F with q ̸∈F ×. (Hint:
write q = x0 + q0 where q0 is pure. Use the right side to compute q2, noting x0 and
q0 commute. By (3.2), q2
0 ∈F.)
7. Suppose a, b ∈R× with a > 0.
Show (a, b)Q becomes a subring of M2(R) by
mapping
1 7→

1
0
0
1

,
u 7→
√a
0
0
−√a

,
v 7→

0
−1
−b
0

,
w 7→

0
−√a
√ab
0

for the basis of (a, b)Q and extending this to all of (a, b)Q by Q-linearity.
8. Let’s generalize the embedding of H into M2(C) in (2.4) to an embedding of (a, b)F
into a 2 × 2 matrix ring.
For a ∈F ×, the ring F[t]/(t2 −a) is a ﬁeld if a ̸= □in F, while F[t]/(t2 −a) ∼=
F × F if a = □in F. Verify that the map (a, b)F →M2(F[t]/(t2 −a)) given by
1 7→

1
0
0
1

,
u 7→

t
0
0
−t

,
v 7→

0
−1
−b
0

,
w 7→

0
−t
bt
0

,
and extended to all of (a, b)F by F-linearity, is an injective ring homomorphism.
4. Isomorphisms Between Quaternion Algebras
An isomorphism between two quaternion algebras A and A′ over a ﬁeld F is a ring
isomorphism f : A →A′ that ﬁxes the elements of F (that is, f(c) = c for all c ∈F). To
show two quaternion algebras are isomorphic we will take a low-brow approach by working
with well-chosen bases of them.
Deﬁnition 4.1. A basis of (a, b)F having the form {1, e1, e2, e1e2} where e2
1 ∈F ×, e2
2 ∈F ×,
and e1e2 = −e2e1 is called a quaternionic basis of (a, b)F .
For instance, the deﬁning basis {1, u, v, w} of (a, b)F is a quaternionic basis. In a quater-
nionic basis, check that (e1e2)2 = −e2
1e2
2 ∈F × and e1, e2, e1e2 pairwise anti-commute.
There are quaternionic bases of (a, b)F other than {1, u, v, uv}, and diﬀerent choices of
a quaternionic basis reveal isomorphisms between diﬀerent quaternion algebras on account
of the multiplicative relations among the basis elements (recall w = uv and w2 = −ab):
(1) {1, v, u, vu} is a quaternionic basis of (a, b)F , so (a, b)F ∼= (b, a)F ,
(2) {1, u, w, uw} is a quaternionic basis of (a, b)F , so (a, b)F ∼= (a, −ab)F ,
(3) {1, v, w, vw} is a quaternionic basis of (a, b)F , so (a, b)F ∼= (b, −ab)F ,
(4) {1, cu, dv, (cu)(dv)} is a quaternionic basis of (a, b)F for all c, d ∈F ×, so (a, b)F ∼=
(ac2, bd2)F for all nonzero c and d in F.

<!-- page 10 -->
10
KEITH CONRAD
Example 4.2. The quaternion algebra (3, 11)Q is a division ring since (3, 11)Q ∼= (11, 3)Q
and 11 ̸≡□mod 3. Therefore we can use Theorem 3.9 with a = 11 and p = 3.
Using the second quaternionic basis above with b = 1 shows (a, −a)F ∼= (a, 1)F , and with
b = −1 shows (a, a)F ∼= (a, −1)F . Using the fourth quaternionic basis shows that (a, b)F
up to isomorphism depends on a and b only up to multiplication by nonzero squares in F ×.
For instance, (a, c2)F ∼= (a, 1)F and (c2, b)F ∼= (1, b)F ∼= (b, 1)F . The next theorem shows
the quaternion algebra (a, 1)F is a familiar ring.
Theorem 4.3. For all a ∈F ×, (a, 1)F ∼= M2(F).
This means the ring M2(F) is a quaternion algebra over F and that
(4.1)
(a, c2)F ∼= (a, −a)F ∼= M2(F).
Proof. Send the basis 1, u, v, w of (a, 1)F to M2(F) as follows:
1 7→

1
0
0
1

,
u 7→

0
1
a
0

,
v 7→

1
0
0
−1

,
w 7→

0
−1
a
0

.
Since 1 ̸= −1 in F, 1 and v are not sent to the same matrix. Extend this mapping by
F-linearity to a function (a, b)F →M2(F):
(4.2)
x0 + x1u + x2v + x3w 7→

x0 + x2
x1 −x3
a(x1 + x3)
x0 −x2

.
The image of 1, u, v, w in M2(F) is a linearly independent set, so by a dimension count this
F-linear mapping (a, b)F →M2(F) is a bijection. It ﬁxes F, in the sense that c ∈F in
(a, b)F goes to cI2 in M2(F). It is left to the reader to check (4.2) is multiplicative (Exercise
4.1).
□
Deﬁnition 4.4. We call M2(F), or a quaternion algebra isomorphic to M2(F), a trivial or
split quaternion algebra over F. If (a, b)F ̸∼= M2(F) we say (a, b)F is a non-split quaternion
algebra.
Example 4.5. Let F = R. Then
(a, b)R ∼=
(
H,
if a < 0 and b < 0,
M2(R),
if a > 0 or b > 0.
Example 4.6. Let F = C. All elements of C× are squares in C, so (a, b)C ∼= M2(C) for
all a and b in C×: all quaternion algebras over C are split.
These examples tell us that, up to isomorphism, there are two quaternion algebras over
R and one quaternion algebra over C. Over Q the situation is completely diﬀerent: there
are inﬁnitely many non-isomorphic quaternion algebras over Q. We’ll see this in Section 5.
Example 4.7. If p is prime and p ≡1 mod 4 then H(Fp) ∼= M2(Fp) since −1 is a square
in Fp. We’ll see in Corollary 4.24 that every quaternion algebra over Fp is isomorphic to
M2(Fp).
Example 4.8. The quaternion algebras (2, 3)Q and (2, 5)Q are both division rings (Example
3.10), but the quaternion algebras (2, 3)R and (2, 5)R are not division rings: both are
isomorphic to M2(R).
Deﬁnition 4.9. For a and b in Q× we say (a, b)Q splits over R if (a, b)R ∼= M2(R) and we
say (a, b)Q is non-split over R if (a, b)R ̸∼= M2(R) (that is, (a, b)R ∼= H).

<!-- page 11 -->
QUATERNION ALGEBRAS
11
For example, (2, 3)Q and (2, 5)Q both split over R, while H(Q) = (−1, −1)Q is non-split
over R. More generally, for a ﬁeld extension F ⊂K and a, b ∈F ×, we say (a, b)F splits
over K when (a, b)K ∼= M2(K).
Since (a, b)Q splits over R when a or b is positive, while (a, b)Q is non-split over R when
a and b are both negative, the formula for N(q) in (3.1) shows the norm on (a, b)Q has
positive and negative values when (a, b)Q splits over R, while the norm on (a, b)Q has only
positive values (and 0) when (a, b)Q is non-split over R. It is a hard theorem that the norm
mapping N: (a, b)Q →Q is surjective when (a, b)Q splits over R and has image Q≥0 if
(a, b)Q is non-split over R.
Example 4.10. Since (2, 3)Q is split over R, the equation x2
0 −2x2
1 −3x2
2 + 6x2
3 = r has a
rational solution for every r ∈Q.
There are analogies between quadratic ﬁelds Q(
√
d) and quaternion algebras (a, b)Q.
Real quadratic ﬁelds (when x2 −d splits into linear factors over R) are analogous to the
(a, b)Q that split over R and imaginary quadratic ﬁelds (when x2 −d does not split into
linear factors over R) are analogous to the (a, b)Q that are non-split over R. See Table 2.
Quadratic Field Q(
√
d)
Quaternion Algebra (a, b)Q
Real Quadratic (d > 0)
Split over R
Imaginary Quadratic (d < 0)
Non-split over R
Table 2. Analogous Quadratic Fields and Quaternion Algebras over Q.
Here are two examples of the analogies.
(1) Sign of norm values: There are norm functions N: Q(
√
d) →Q and N: (a, b)Q →
Q, where N(x + y
√
d) = x2 −dy2 for quadratic ﬁelds. If d > 0 the norm on Q(
√
d)
has both positive and negative values, while if d < 0 the norm on Q(
√
d) has only
positive values (and 0). If (a, b)Q splits over R then the norm on (a, b)Q has both
positive and negative values, while if (a, b)Q is non-split over R then the norm on
(a, b)Q has only positive values (and 0).
(2) Integral units: The ring Z[
√
d] is analogous to the ring (a, b)Z = Z + Zu + Zv + Zw.
Units in Z[
√
d] are those x + y
√
d with norm ±1, and units (invertible elements)
of (a, b)Z are the elements with norm ±1. If d > 0 there are inﬁnitely many units
in Z[
√
d] (theory of Pell’s equation), but if d < 0 the unit group of Z[
√
d] is ﬁnite.
If (a, b)Q splits over R then (a, b)Z has inﬁnitely many units, while if (a, b)Q is
non-split over R then (a, b)Z has ﬁnitely many units.
A more subtle analogy is that when d > 0 and (a, b)Q is split over R, the inﬁnitely
many units in Z[
√
d] and (a, b)Z both form ﬁnitely-generated groups.
Example 4.11. The quaternion algebra (2, 3)Q is split over R, so inﬁnitely many elements
of (2, 3)Z have norm ±1. Some examples are 1 + u (similar to 1 +
√
2 in Z[
√
2]), 2 + v
(similar to 2 +
√
3 in Z[
√
3]), and (1 + u)2(2 + v) = 6 + 4u + 3v + 2u.
The easiest way to know (a, b)F ∼= M2(F) is when b = □in F × (see (4.1)). There is
a weaker condition on b than being a square that still implies (a, b)F ∼= M2(F), and to
describe this condition we need to know something about numbers of the form x2 −ay2.
Lemma 4.12. For a ∈F ×, the set of nonzero x2 −ay2 with x, y ∈F is a subgroup of F ×.

<!-- page 12 -->
12
KEITH CONRAD
Proof. The number 1 has this form (x = 1, y = 0). Number of this form are closed under
multiplication since
(x2
1 −ay2
1)(x2
2 −ay2
2) = (x1x2 + ay1y2)2 −a(x1y2 + x2y1)2.
Nonzero numbers of this form are closed under inversion using the trivial identity 1/t = t/t2:
1
x2 −ay2 =
x2 −ay2
(x2 −ay2)2 =

x
x2 −ay2
2
−a

y
x2 −ay2
2
.
□
Deﬁnition 4.13. For a ∈F ×, let Na = Na(F) be the set of all nonzero x2 −ay2 where
x, y ∈F.
By Lemma 4.12 Na is a subgroup of F ×, and (F ×)2 ⊂Na using y = 0.
Theorem 4.14. If a is a square in F then Na = F ×.
Proof. Write a = c2 for c ∈F ×. Then x2 −ay2 = x2 −c2y2 = x2 −(cy)2 = (x −cy)(x + cy).
The change of variables x′ = x −cy and y′ = x + cy is invertible2 (x = (x′ + y′)/2 and
y = (y′ −x′)/(2c)), so Na = {x′y′ : x′, y′ ∈F ×}, which assumes all values in F × by choosing
y′ = 1.
□
Remark 4.15. The converse of Theorem 4.14 is generally false: Na could be F × without
a being a square in F. For instance, if F = Fp for odd primes p then we’ll see in Corollary
4.24 that Na = F×
p for all a ∈F×
p , but only half the elements of F×
p are squares. There are
important cases where the converse of Theorem 4.14 is true, such as F = Q and F = R
(and F = Qp for a prime p, if you know what Qp is).
We call Na the norm subgroup of F × associated to a, since x2−ay2 = (x+y√a)(x−y√a)
is usually called a norm.
Theorem 4.16. If b ∈Na then (a, b)F ∼= M2(F).
As a special case this includes (a, b)F ∼= M2(F) if b = □in F.
Proof. Write b = x2
0 −ay2
0 with x0 and y0 in F. The ring (a, b)F has a quaternionic basis
(Deﬁnition 4.1):
1,
u,
x0v + y0w,
u(x0v + y0w).
The fourth element is x0w + y0av by the formulas for uv and uw. Why is this a basis? It is
linearly independent since the 4th term is ay0v + x0w and the change of basis matrix from
v, w to x0v + y0w, ay0v + x0w has determinant | x0 y0
ay0 x0 | = b ̸= 0 (Exercise 4.10). Therefore
the above set of four elements of (a, b)F is linearly independent over F, so it is a basis of
(a, b)F . Why is this basis quaternionic? We have (x0v+y0w)2 = bx2
0 −aby2
0 = b2, and u and
x0v + y0w anti-commute. Therefore b ∈Na ⇒(a, b)F ∼= (a, b2)F ∼= (a, 1)F ∼= M2(F).
□
Example 4.17. We have (a, 1 −a)F ∼= M2(F) if a ̸= 0, 1 since 1 −a = x2 −ay2 with
x = y = 1.
Example 4.18. The quaternion algebra (3, 11)Q is a division ring since 11 ̸≡□mod 3
(Example 4.2), while (3, −11)Q ∼= M2(Q) since −11 = x2 −3y2 with x = 1 and y = 2.
Example 4.19. When p is a prime and p = 2 or p ≡1 mod 4, Fermat’s two-square
theorem says p is a sum of two squares in Z. Therefore p ∈N−1(Q), so (−1, p)Q ∼= M2(Q).
2Here it is crucial that F does not have characteristic 2.

<!-- page 13 -->
QUATERNION ALGEBRAS
13
Theorem 4.20. A quaternion algebra (a, b)F that is not a division ring is isomorphic to
M2(F).
Proof. Since we already know that (c2, b)F ∼= M2(F), we can assume a is not a square in F.
By Theorem 3.8, if (a, b)F is not a division ring it contains a nonzero element q with
N(q) = 0. Let q = x0 + x1u + x2v + x3w with its coeﬃcients not all equal to 0. Then
N(q) = 0 =⇒x2
0 −ax2
1 −bx2
2 + abx2
3 = 0 =⇒x2
0 −ax2
1 = b(x2
2 −ax2
3).
Since a is not a square in F, we must have x2
2 −ax2
3 ̸= 0 by contradiction: if x2
2 −ax2
3 = 0
then x3 = 0 (if x3 ̸= 0 we could solve for a to see it is a square in F), so also x2 = 0, and
that implies x2
0 −ax2
1 = 0, so also x1 = 0 and x0 = 0, but then q = 0.
Solving for b,
b = x2
0 −ax2
2
x2
2 −ax2
3
∈Na,
so (a, b)F ∼= M2(F) by Theorem 4.16.
□
By this theorem, all (a, b)F that are not isomorphic to M2(F) are division rings, so
Non-split quaternion algebras = quaternion algebras that are division rings.
Theorem 4.21. For a and b in F ×, (a, b)F ∼= M2(F) if and only if b ∈Na.
Proof. If b ∈Na then (a, b)F ∼= M2(F) by Theorem 4.16. Conversely, suppose (a, b)F ∼=
M2(F). To show b ∈Na, we can assume a is not a square in F ×, since if a were a square
then Na = F × by Theorem 4.14, so obviously b ∈Na. When (a, b)F is not a division ring
and a is not a square, the proof of Theorem 4.20 shows b ∈Na.
□
We have seen several suﬃcient conditions that imply (a, b)F ∼= M2(F):
• b = c2: (4.1).
• b = −a: (4.1).
• b = 1 −a: Example 4.17.
• b = x2 −ay2 for some x, y ∈F: Theorem 4.21.
The last condition includes the previous ones as special cases, and Theorem 4.21 tells us
the last condition is not only suﬃcient but necessary as well.
Remark 4.22. We consider M2(F) to be the “trivial” quaternion algebra, so the following
quaternion algebras (a, b)F are considered trivial: (a, c2)F , (a, −a)F , (a, 1 −a)F , and more
generally (a, x2−ay2)F . In other areas of math there are objects depending on two variables
that turn out to be “trivial” in situations that resemble the conditions above. Probably the
ﬁrst instance of this historically was the Hilbert symbol (a, b)p where p is a prime number
and a and b are nonzero rational numbers (or even nonzero p-adic numbers). The Steinberg
symbol {a, b}F for a ﬁeld F (of characteristic not 2) is a universal construction subject to
rules typiﬁed by {a, 1 −a}F being considered “trivial.”
Corollary 4.23. For a ﬁeld F not of characteristic 2, H(F) is a division ring if and only
if −1 is not a sum of two squares in F.
Proof. We will prove the negations of both conditions are equivalent: to say H(F) is not a
division ring means H(F) ∼= M2(F), and by Theorem 4.21, (−1, −1)F ∼= M2(F) if and only
if −1 = x2 −(−1)y2 = x2 + y2 for some x and y in F.
□
Corollary 4.24. For every odd prime p, all quaternion algebras over Fp are isomorphic to
M2(Fp).

<!-- page 14 -->
14
KEITH CONRAD
This includes Example 4.7 as a special case.
Proof. We will show for all nonzero a and b in Fp that b = x2 −ay2 for some x and y in Fp.
Write the equation b = x2 −ay2 as b + ay2 = x2. Let’s count how many values each side of
the equation has as x and y run over Fp. The total number of squares in Fp is (p + 1)/2
(not (p −1)/2, because we include 0 as a square), so |{x2 : x ∈Fp}| = (p + 1)/2, and since
a ̸= 0 we also have |{b + ay2 : y ∈Fp}| = (p + 1)/2. If the equation b + ay2 = x2 had no
solution in Fp then {x2} and {b + ay2} would be disjoint subsets of Fp, but their sizes add
up to (p + 1)/2 + (p + 1)/2 = p + 1 > Fp, so we’d have a contradiction. Therefore there
exist some x and y in Fp such that b + ay2 = x2.
□
In Theorem 4.21, the condition (a, b)F ∼= M2(F) is symmetric in a and b since (a, b)F ∼=
(b, a)F . Therefore the condition b ∈Na has to be symmetric in a and b even though it
doesn’t look symmetric in a and b at ﬁrst glance. (That is, being able to solve b = x2 −ay2
in F may not look obviously equivalent to being able to solve a = x2−by2 in F, particularly if
one of the squares in a solution is 0.) The following alternate form of Theorem 4.21 replaces
“b ∈Na” with conditions on an equation involving a and b that are visibly symmetric.
Theorem 4.25. For a and b in F ×, the following conditions are equivalent:
1) (a, b)F ∼= M2(F),
2) the equation ax2 + by2 = 1 has a solution (x, y) in F,
3) the equation ax2 + by2 = z2 has a solution (x, y, z) in F other than (0, 0, 0).
Proof. Exercise 4.12.
□
Corollary 4.26. For a and b in F ×, the following conditions are equivalent:
1) (a, b)F is a division ring,
2) the equation ax2 + by2 = 1 has no solution (x, y) in F,
3) the only solution to ax2 + by2 = z2 in F is (0, 0, 0).
Proof. Negate each part of Theorem 4.25.
□
In a quaternionic basis {1, e1, e2, e1e2} of (a, b)F , the basis elements besides 1 are in
(a, b)0
F : their squares are all in F × (this is true for e1 and e2 by the deﬁnition of a quater-
nionic basis, and (e1e2)2 = e1e2e1e2 = e1(−e1e2)e2 = −e2
1e2
2 ∈F ×), and that puts them
all in F or (a, b)0
F by Exercise 3.6(ii).
They can’t be in F since they are nonzero and
anti-commute with each other, so they are all in (a, b)0
F . The next theorem is a converse.
Theorem 4.27. In (a, b)F , every pure quaternion whose square is nonzero is part of a
quaternionic basis of (a, b)F .
Proof. Let e1 ∈(a, b)0
F be nonzero (we won’t use the whole assumption e2
1 ̸= 0 initially).
We will show there is a nonzero e2 in (a, b)0
F such that e1e2 = −e2e1. Rewrite that as
e1e2 + e2e1 = 0.
Let f : (a, b)0
F →(a, b)F by f(q) = e1q + qe1. This is F-linear. It turns out that f has
image in F, which by its linearity can be proved by checking this property on the deﬁning
basis u, v, w of (a, b)0
F : writing e1 = xu + yv + zw, where x, y, z ∈F,
f(u) = e1u + ue1
= (xu + yv + zw)u + u(xu + yv + zw)
= 2xu2 + y(vu + uv) + z(wu + uw)
= 2ax

<!-- page 15 -->
QUATERNION ALGEBRAS
15
since u2 = a and u, v, w pairwise anti-commute. Similarly, f(v) = 2by and f(w) = −2abz.
By F-linearity, the image of f is either 0 or F, and it is not 0 since at least one of f(u),
f(v), and f(w) is nonzero because (i) a and b are in F × and (ii) e1 being nonzero implies
at least one of its coeﬃcients x, y, z is nonzero. So f : (a, b)0
F →F is a linear map from
a 3-dimensional space onto a 1-dimensional space, which makes ker f have dimension 2.
Picking e2 to be any nonzero element of ker f, e2 ∈(a, b)0
F and 0 = f(e2) = e1e2 + e2e1, so
e1e2 = −e2e1: e1 and e2 anti-commute.
All elements of (a, b)0
F have square in F by (3.2), so e2
1 ∈F and e2
2 ∈F. By hypothesis,
e2
1 ̸= 0. We will show e2 in ker f can be chosen so that e2
2 ̸= 0. Then {1, e1, e2, e1e2} is
linearly independent by Exercise 4.2, so this is a quaternionic basis containing e1.
Let V = (a, b)0
F , U = Fe1, and W = ker f. To show W contains an e2 such that e2
2 ̸= 0,
we will assume the reader knows about quadratic spaces (vector spaces equipped with a
quadratic form, orthogonal bases, discriminants of quadratic forms, and so on), as it allows
us to reason geometrically rather than only algebraically. If you have not studied quadratic
spaces, perhaps this will motivate you to try. Set Q : V →F by Q(q) = q2. Writing
q = Xu + Y v + Zw with X, Y, Z ∈F, Q(q) = q2 = aX2 + bY 2 −abZ2, so Q is a non-
degenerate quadratic form on V due to its nonzero diagonal coeﬃcients a, b, and −ab. Its
associated bilinear form on V is B(q, q′) = aXX′ + bY Y ′ −abZZ′. Since
f(q) = Xf(u) + Y f(v) + Zf(w) = 2(axX + byY −abzZ) = 2B(e1, q),
W = ker f = e⊥
1 = U⊥, and e1 ̸∈W since f(e1) = 2(ax2 + by2 −abz2) = 2e2
1 ̸= 0. Thus V is
the direct sum of the orthogonal subspaces U and W = U⊥, so Q being nondegenerate on
V implies3 Q is nondegenerate on W and thus Q is not identically 0 on W: there is some
e2 ∈W such that Q(e2) ̸= 0, so e2 ∈ker f and e2
2 ̸= 0.
□
Corollary 4.28. For a, b, and c in F ×, the following conditions are equivalent:
(i) (a, b)F ∼= (c, ∗)F ,
(ii) c = q2 for some nonzero q ∈(a, b)0
F ,
(iii) c = ax2 + by2 −abz2 for some x, y, z ∈F that are not all 0.
Proof. Conditions (ii) and (iii) are equivalent because (xu + yv + zw)2 = ax2 + by2 −abz2
by (3.2).
To show (i) and (ii) are equivalent, ﬁrst assume (i). Then (a, b)F ∼= (c, d)F for some
d ∈F ×, so there is a quaternionic basis {1, e1, e2, e1e2} of (a, b)F such that c = e2
1. That
implies by Exercise 3.6(ii) that e1 is in F or is in (a, b)0
F , and e1 being in a basis that
includes 1 makes e1 ̸∈F. We have proved (ii).
Now assume (ii), so c = q2 where q ∈(a, b)0
F . Since c ∈F ×, q2 is nonzero. By Theorem
4.27, there is a quaternionic basis of (a, b)F having the form {1, q, q′, qq′}. Since c = q2, let
d = q′2 and this quaternionic basis shows (a, b)F ∼= (c, d)F . We have proved (i).
□
It turns out that every ﬁnite set of quaternion algebras over Q can be written as
(a, b1)Q, . . . , (a, bn)Q, which share the same a (they have a “common slot”), but this is not
true over all ﬁelds, e.g., when F = Q(t), the quaternion algebras (−1, −1)F and (−7, t)F
can’t both be written as (a, ∗)F with the same a in F ×.
Theorem 4.29. For a, b, c, d ∈F ×, if (a, b)F and (c, d)F are isomorphic quaternion algebras
over F then for every ﬁeld extension E/F, (a, b)E and (c, d)E are isomorphic
3See Theorem 6.8 in https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf.

<!-- page 16 -->
16
KEITH CONRAD
Proof. Let f : (a, b)F →(c, d)F be an isomorphism of quaternion algebras over F, with
(a, b)F having F-basis {1, u, v, uv} such that u2 = a, v2 = b, and uv = −vu.
Set
u′ = f(u) and v′ = f(v). Since f is F-linear and injective, the F-linear independence in
(a, b)F of {1, u, v, uv} implies F-linear independence in (c, d)F of {f(1), f(u), f(v), f(uv)} =
{1, f(u), f(v), f(u)f(v)} = {1, u′, v′, u′v′}, so {1, u′, v′, u′v′} is a basis of (c, d)F . This basis
is quaternionic since u′2 = f(u)2 = f(u2) = f(a) = a and v′2 = f(v)2 = f(v2) = f(b) = b,
which are in F ×, and u′v′ = f(uv) = f(−vu) = −v′u′. That shows how (c, d)F contains an
F-basis that makes it look like (a, b)F .
In (c, d)F there is an F-basis {1, w, z, wz} such that w2 = c, z2 = d, and wz = −zw. We
already built another F-basis {1, u′, v′, u′v′} of (c, d)F , and the expression of either F-basis
of (c, d)F as an F-linear combination of the other basis is invertible.
Now consider (a, b)E and (c, d)E where E is a ﬁeld extension of F. In (a, b)E is an E-
basis {1, u, v, uv} such that u2 = a, v2 = b, and uv = −vu, and in (c, d)E is an E-basis
{1, w, z, wz} such that w2 = c, z2 = d, and wz = −zw. The F-span of {1, w, z, wz} is a
copy of (c, d)F inside (c, d)E, and using an invertible F-linear transformation in the previ-
ous paragraph on {1, w, z, wz} shows (c, d)E has an E-basis with the same multiplicative
relations as the E-basis {1, u, v, uv} of (a, b)E. Thus (a, b)E ∼= (c, d)E as quaternion algebras
over E.
□
Corollary 4.30. For a, b, c, d ∈F ×, if there is a ﬁeld extension E/F such that ax2+by2 = 1
has a solution in E and cx2+dy2 = 1 does not have a solution in E, then (a, b)F and (c, d)F
are not isomorphic quaternion algebras over F.
Proof. Assume (a, b)F ∼= (c, d)F as quaternion algebras over F. Then (a, b)E ∼= (c, d)E as
quaternion algebras over E. By Theorem 4.25, ax2 + by2 = 1 having a solution in E makes
(a, b)E ∼= M2(E), and cx2 + dy2 = 1 having no solution in E makes (c, d)E ̸∼= M2(E), so we
have a contradiction.
□
Exercises.
1. Show (4.2) is multiplicative.
2. If e1, e2 ∈(a, b)F are not in F and satisfy the conditions e2
1 ∈F ×, e2
2 ∈F ×, and
e1e2 = −e2e1, then show {1, e1, e2, e1e2} is a linearly independent set, and thus is a
quaternionic basis of (a, b)F . Remember, F has characteristic ̸= 2. (Hint: Progres-
sively show the linear independence of {1, e1}, {1, e1, e2}, and then {1, e1, e2, e1e2}.
The second case will need e1e2 = −e2e1 and e2
1 ∈F ×, while the third case will need
e1e2 = −e2e1, e2
1 ∈F ×, and e2
2 ∈F ×.)
3. Under the isomorphism (a, 1)F ∼= M2(F) determined by
1 7→

1
0
0
1

,
u 7→

0
1
a
0

,
v 7→

1
0
0
−1

,
w 7→

0
−1
a
0

what element of (a, 1)F corresponds to the matrix ( 0 1
0 0 )?
4. Under the isomorphism (1, 1)F ∼= M2(F) as in the previous exercise (with a = 1),
let x0 +x1u+x2v +x3w in (1, 1)F correspond to ( α β
γ δ ) in M2(F). Write α, β, γ, δ in
terms of x0, x1, x2, x3 and vice versa. Check that, under this isomorphism, the norm
on (1, 1)F corresponds to the determinant on M2(F), but conjugation on (1, 1)F does
not correspond to the transpose on M2(F). What operation on M2(F) corresponds
to conjugation on (1, 1)F ?

<!-- page 17 -->
QUATERNION ALGEBRAS
17
5. When a ̸= −b in F ×, check {1, u + v, w, (u + v)w} is a quaternionic basis of (a, b)F .
Therefore (a, b)F ∼= (a + b, −ab)F . For example, (2, 3)Q ∼= (5, −6)Q.
6. Show −1 is not a sum of two squares in the ﬁeld Q(√−7), so H(Q(√−7)) is a
division ring. Is H(Q(√−2)) a division ring?
7. If a, b ∈F × satisfy a + b = c2 for some c ∈F, show (a, b) ∼= M2(F).
8. By Theorem 4.16,
b = x2
0 −ay2
0 for some x0, y0 ∈F =⇒(a, b)F ∼= M2(F)
by using the quaternionic basis {1, u, x0v + y0w, u(x0v + y0w)} of (a, b)F . What is
wrong with the following alternate proof of the above implication?
If x0 = 0, then y0 ̸= 0 and (a, b)F = (a, −ay2
0)F ∼= (a, −a)F ∼= M2(F).
If x0 ̸= 0, then (y0u + v)2 = x2
0 and the set {1, u, y0u + v, u(y0u + v)} is a basis
of (a, b)F , so (a, b)F ∼= (a, x2
0)F ∼= M2(F).
9. A quaternion algebra over F is isomorphic to M2(F) precisely when it has a nonzero
element with norm 0. Prove (a, −a)F ∼= M2(F) if a ̸= 0, and (a, 1 −a)F ∼= M2(F)
if a ̸= 0, 1 by ﬁnding speciﬁc nonzero elements in them with norm 0.
10. In F n, let v1 and v2 be linearly independent. For a, b, c, d ∈F, show av1 + bv2 and
cv1+dv2 are linearly independent in F n if and only if the determinant | a b
c d | = ad−bc
is nonzero.
11. Decide if the following are division rings: (2, −5)Q, (6, 10)Q, (6, −10)Q, (5, 11)Q,
(5, −11)Q.
12. Prove Theorem 4.25. Be careful not to assume x, y, or z is automatically nonzero.
5. Isomorphism and Norms
Theorem 4.21 can be expressed as: (a, b)F ∼= (a, 1)F if and only if b ∈Na. The following
theorem generalizes this.
Theorem 5.1. For a, b, b′ ∈F ×, (a, b)F ∼= (a, b′)F if and only if b/b′ ∈Na.
Proof. The direction (⇐) is much simpler, so we do that ﬁrst. Suppose b/b′ = x2
0 −ay2
0 for
some x0 and y0 in F. Let {1, u, v, uv} be the usual quaternionic basis of (a, b′)F . Check
that
(5.1)
1,
u,
x0v + y0w,
u(x0v + y0w),
is also a quaternionic basis of (a, b′)F . Here u2 = a and (x0v + y0w)2 = b′x2
0 −ab′y2
0 =
b′(b/b′) = b, so (a, b′)F ∼= (a, b)F .
To prove the reverse direction, that (a, b)F ∼= (a, b′)F ⇒b/b′ ∈Na, the isomorphic
quaternion algebras (a, b)F and (a, b′)F are either both division rings or both not division
rings.
First suppose (a, b)F and (a, b′)F are not division rings, so they are isomorphic to M2(F).
Then b ∈Na and b′ ∈Na by Theorem 4.21. Since Na is a subgroup of F ×, b/b′ ∈Na.
Next suppose (a, b)F and (a, b′)F are division rings, so in particular a is not a square in
F. Let {1, u, v, uv} be the standard quaternionic basis of (a, b′)F , so
u2 = a,
v2 = b′,
uv = −vu.
Since (a, b′)F ∼= (a, b)F , (a, b′)F contains a quaternionic basis {1, u0, v0, u0v0} where
u2
0 = a,
v2
0 = b,
u0v0 = −v0u0.

<!-- page 18 -->
18
KEITH CONRAD
The polynomial T 2 −a is irreducible over F since a is not a square in F, and both u and
u0 are roots of this polynomial in (a, b′)F , so Theorem B.2 implies u = qu0q−1 for some
nonzero q ∈(a, b′)F . Set ev = qv0q−1, so ev2 = (qv0q−1)(qv0q−1) = qv2
0q−1 = qbq−1 = b.
Then
u0v0 = −v0u0 =⇒(qu0q−1)(qv0q−1) = −(qv0q−1)(qu0q−1) =⇒uev = −evu.
The elements of (a, b′)F that anti-commute with u are Fv+Fw (Exercise 3.3), so ev = xv+yw
for some x and y in F. Then
b = ev2 = (xv + yw)2 = b′x2 −b′ay2 = b′(x2 −ay2) =⇒b
b′ ∈Na.
□
Remark 5.2. Theorem 5.1 gives us a new proof that (a, −ab)F ∼= (a, b)F : −a = x2 −ay2
with x = 0 and y = 1. It might appear that this theorem reproves (a, bc2)F ∼= (a, b)F
(c2 = x2 −ay2 with x = c and y = 0), but this is circular because we will be using that
isomorphism in the proof of Theorem 5.1.
Example 5.3. (2, 3)Q ∼= (2, 21)Q since 21/3 = 7 = x2 −2y2 using x = 3 and y = 1.
Example 5.4. To decide if the division rings (2, 3)Q and (2, 5)Q are isomorphic is equivalent
to deciding if 5/3 = x2 −2y2 for some rational numbers x and y. This equation has no
rational solution (Exercise 5.3a), so (2, 3)Q ̸∼= (2, 5)Q.
Corollary 5.5. For distinct primes p and q that are 3 mod 4, (−1, p)Q is not isomorphic
to (−1, q)Q.
Proof. If (−1, p)Q ∼= (−1, q)Q then q/p ∈N−1(Q), so q/p = x2 + y2 for some rational
numbers x and y. Write x and y with a common denominator: x = m/d and y = n/d with
integers m, n, and d where d ̸= 0. Then
(5.2)
qd2 = p(m2 + n2).
Since p ̸= q, m2 + n2 ≡0 mod q, so m2 ≡−n2 mod q. That implies q | n and then
q | m since −1 mod q is not a square, so the right side of (5.2) is divisible by q2. Thus
q | d, so in (5.2) the the numbers m, n, and d are all divisible by q. Writing m = qm′,
n = qn′, and d = qd′, divide through (5.2) by q2 to get qd′2 = p(m′2 + n′2), which is a
similar equation with m, n, and d are replaced by m/q, n/q, and d/q. Repeating this ad
inﬁnitum d is divisible by arbitrarily high powers of q, which is impossible. We have reached
a contradiction, so (−1, p)Q ̸≡(−1, q)Q.
□
There are inﬁnitely many primes congruent to 3 mod 4, so Corollary 5.5 shows there are
inﬁnitely many non-isomorphic quaternion algebras over Q!
Theorem 5.6. If f : A1 →A2 is an isomorphism of quaternion algebras over F then we
have f(q) = f(q) for all q ∈A1. In particular, N(f(q)) = N(q).
Proof. Once we show f(q) = f(q) for all q ∈A1 we get
N(f(q)) = f(q)f(q) = f(q)f(q) = f(qq) = f(N(q)) = N(q)
since N(q) ∈F and f ﬁxes all elements of F.
Write q = x0 + q0 where x0 ∈F and q0 is a pure quaternion in A1 (Example 3.7). Then
(5.3)
f(q) = f(x0 −q0) = x0 −f(q0).

<!-- page 19 -->
QUATERNION ALGEBRAS
19
We will show f(q0) is a pure quaternion in A2. This is obvious if q0 = 0, so assume q0 ̸= 0.
Since q0 is pure in A1 we have q2
0 ∈F by (3.2), so also f(q0)2 ∈F. By Exercise 3.6 ii, either
f(q0) is pure or f(q0) ∈F. We can’t have f(q0) ∈F since f(F) = F, f is injective, and
q0 ̸∈F (the only pure quaternion in F is 0). Thus f(q0) is pure, so f(q0) = −f(q0), which
turns (5.3) into
f(q) = x0 + f(q0) = x0 + f(q0) = f(x0 + q0) = f(q).
□
Corollary 5.7. If A1 and A2 are isomorphic quaternion algebras over F then the norm
maps A1 →F and A2 →F have the same image.
Proof. This is immediate from N(q) = N(f(q)) for an isomorphism f : A1 →A2.
□
Example 5.8. The quaternion algebras H(Q) and (2, 3)Q are division rings (for (2, 3)Q
see Example 3.10), but they are not isomorphic quaternion algebras over Q since the norm
on H(Q) is nonnegative and the norm on (2, 3)Q has negative values by Example 3.6.
Exercises.
1. In the proof of Theorem 5.1, show (5.1) is a quaternionic basis of (a, b)F .
2. Let a, b, b′ ∈F ×.
a) If (a, b)F ∼= M2(F), prove (a, b′)F ∼= (a, bb′)F .
(For example, if p = 2 or
p ≡1 mod 4, then we already know (p, −1)Q ∼= M2(Q), so (p, r)Q ∼= (p, −r)Q for all
r ∈Q×.) Is the converse true?
b) By part a, (2, 3)Q ∼= (2, −3)Q. Show (−2, 3)Q ∼= M2(Q) and (−2, −3)Q ∼=
H(Q).
3. If p is a prime number such that p ≡3 or 5 mod 8, then (p, 2)Q is a division ring by
Exercise 3.5.
a) Show the equation 5/3 = x2−2y2 has no rational solution, so (3, 2)Q ̸∼= (5, 2)Q.
(Hint: Mimic the proof of Corollary 5.5.)
b) For distinct primes p and q that are 3 or 5 mod 8 (this means p ≡3 or 5 mod 8
and q ≡3 or 5 mod 8), show (p, 2)Q is not isomorphic to (q, 2)Q.
c) Prove the converse of Exercise 3.5 is false by showing (15, 2)Q and (33, 2)Q are
division rings. Neither 15 nor 33 is 3 or 5 mod 8.
4. Generalize Corollary 5.5: if a ∈Z and p and q are distinct odd primes such that
a ̸≡□mod p and a ̸≡□mod q, then the division rings (a, p)Q and (a, q)Q are not
isomorphic. (That (a, p)Q and (a, q)Q are division rings is due to Theorem 3.9.)
Appendix A. Sum of square identities using C and H
In C, the fact that zw = z w implies a formula for the product of sums of two squares as
a sum of two squares:
(A.1)
(a2 + b2)(c2 + d2) = (ac −bd)2 + (ad + bc)2.
Writing z = a + bi and w = c + di, the left side is zzww and the right side is zwzw =
zwz w = zzww.

<!-- page 20 -->
20
KEITH CONRAD
Quaternionic multiplication in H leads to a four-square identity generalizing (A.1):
(a2
1 + b2
1 + c2
1 + d2
1)(a2
2 + b2
2 + c2
2 + d2
2) = (a1a2 −b1b2 −c2c2 −d1d2)2+
(a1b2 + b1a2 + c1d2 −d1c2)2+
(a1c2 −b1d2 + c1a2 + d1b2)2+
(a1d2 + b1c2 −c1b2 + d1a2)2.
To prove this, a sum of four squares is the norm of a quaternion: a2 + b2 + c2 + d2 =
N(a + bi + cj + dk). Letting q1 = a1 + b1i + c1j + d1k and q2 = a2 + b2i + c2j + d2k in
H, feeding these into the formula N(q1) N(q2) = N(q1q2) from (2.3) implies the four-square
identity above.
It’s hard to imagine the four-square identity could be found without quaternions, but
it was! Unbeknownst to Hamilton, the four-square identity was written down by Euler in
1748, a hundred years before the discovery of quaternions.
Appendix B. Conjugates in a division ring
The label “conjugates” in the heading of this appendix doesn’t refer to the conjugation
operation on a quaternion algebra, but rather to conjugation in the sense of group theory:
elements x and y in a group G are called conjugate when y = gxg−1 for some g ∈G. For a
division ring D, its nonzero elements are a group under multiplication and we call x and y
in D conjugate if y = dxd−1 for some d ∈D× = D −{0}.
When F is a ﬁeld, a polynomial of degree n in F[t] has at most n roots in F. Surprisingly,
over a division ring a polynomial of degree n can have more than n roots. For example, the
polynomial t2 + 1 has inﬁnitely many roots in H: by (2.1), a pure quaternion bi + cj + dk
with b2 + c2 + d2 = 1 is a root of t2 + 1. As if to compensate for there being more roots
than the degree, all these roots turn out to be conjugate to each other in the sense of group
theory: if x2 +1 = 0 and y2 +1 = 0 in H then y = qxq−1 for some q ∈H×. This is a special
case of the following general theorem of Dickson. Recall (Exercise 2.3) that the center of a
division ring is a ﬁeld.
Theorem B.1 (Dickson). Let D be a division ring with center F and f(t) be an irreducible
polynomial in F[t]. All roots of f(t) in D are conjugate to each other: if f(x) = 0 and
f(y) = 0 for x and y in D then y = dxd−1 for some d ∈D×.
A proof of Theorem B.1 can be found in [4, Theorem 16.8]. We use this result (in Section
5) only when dimF (D) < ∞and deg f = 2, so we’ll prove Theorem B.1 in this special case:
Theorem B.2. Let D be a division ring with center equal to a ﬁeld F, and assume
dimF (D) < ∞. If f(t) = t2 + c1t + c0 ∈F[t] is irreducible over F then x and y in D
that satisfy f(x) = 0 and f(y) = 0 are conjugate: y = dxd−1 for some d ∈D×.
Proof. We have x2 + c1x + c0 = 0 and y2 + c1y + c0 = 0. Therefore y2 + c1y = x2 + c1x,
and by adding yx to both sides we can write this equation in the clever way
y(y + x + c1) = (y + x + c1)x
If y + x + c1 ̸= 0 then set d = y + x + c1, so yd = dx and d ̸= 0 in D. Thus y = dxd−1.
What if y + x + c1 = 0? In that case, to ﬁnd a nonzero d that makes yd = dx requires
a bit of linear algebra. Deﬁne L: D →D by L(d) = dx −yd for all d ∈D. Since F is the

<!-- page 21 -->
QUATERNION ALGEBRAS
21
center, L is F-linear:
L(d1 + d2) = (d1 + d2)x −y(d1 + d2) = d1x −yd1 + d2x −yd2 = L(d1) + L(d2),
L(cd) = (cd)x −y(cd) = cdx −cyd = c(dx −yd) = cL(d),
where c ∈F. Since y+x+c1 = 0, L(d) = dx+(x+c1)d. This formula implies xL(d) = L(d)x:
xL(d) = x(dx + (x + c1)d) = xdx + (x2 + c1x)d = xdx −c0d,
L(d)x = dx2 + (x + c1)dx = d(−c1x −c0) + xdx + c1dx = xdx −c0d,
and these two values are equal. Thus L(d) commutes with x for all d ∈D.
Since f(x) = 0 and f(t) has no roots in F, x ̸∈F. All of L(D) commutes with x, and
not all of D commutes with x (otherwise x would be in the center of D, which is F), so
L(D) is a proper subspace of D: L is not surjective. A basic theorem from linear algebra
says a linear map V →V where dimF (V ) < ∞is one-to-one if and only if it is onto. Since
L: D →D is not onto and dimF (D) < ∞, L is is not one-to-one: ker L ̸= {0}. Therefore
some nonzero d ∈D satisﬁes L(d) = 0, which means dx = yd. Thus y = dxd−1.
□
References
[1] L. E. Dickson, “Linear algebras in which division is always uniquely possible,” Bull. Amer. Math. Soc.
12 (1905-6), 441–442.
[2] H.-D. Ebbinghaus et al., Numbers, Springer-Verlag, New York, 1990.
[3] W. Hamilton, Mathematical Papers, Vol. III, Algebra, Cambridge Univ. Press, 1967.
[4] T. Y. Lam, A First Course in Noncommutative Rings, Springer-Verlag, New York, 1991.
[5] T. Y. Lam, Introduction to Quadratic Forms over Fields, Amer. Math. Soc., Providence, 2005.
[6] T. Y. Lam, “Hamilton’s quaternions,” pp. 429–454 of Handbook of algebra, Vol. 3, North-Holland, Am-
sterdam, 2003.
[7] C. Maclachlan and A. Reid, The arithmetic of hyperbolic 3-manifolds, Springer-Verlag, New York, 2003.
[8] T. Miyake, Modular forms, Springer-Verlag, Berlin, 1989.
[9] J. H. Silverman, The Arithmetic of Elliptic Curves, Springer-Verlag, New York, 1986.
[10] M.-F. Vign´eras, Arithm´etique des alg`ebres de quaternions, Springer-Verlag, Berlin, 1980.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*