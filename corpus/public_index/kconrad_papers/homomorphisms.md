# Homomorphisms

> **Source**: https://kconrad.math.uconn.edu/blurbs/homomorphisms.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
HOMOMORPHISMS
KEITH CONRAD
1. Introduction
In group theory, the most important functions between two groups are those that “preserve” the
group operations, and they are called homomorphisms. A function f : G →H between two groups
is a homomorphism (or group homomorphism) when
f(xy) = f(x)f(y) for all x and y in G.
Here xy is in G and f(x)f(y) is in H, so a homomorphism from G to H is a function that transforms
the operation in G to the operation in H, even if the operation is not literally “multiplication”.
For example, a homomorphism f : R →R× satisﬁes f(x + y) = f(x)f(y) and a homomorphism
R× →R satisﬁes f(xy) = f(x) + f(y).
In Section 2 we will see how to interpret many elementary algebraic identities as homomorphisms,
involving the groups Z, R, R×, R>0, C, and C×. Section 3 describes some homomorphisms in lin-
ear algebra and modular arithmetic. Section 4 gives a few important examples of homomorphisms
between more abstract groups. Section 5 has examples of functions between groups that are not
homomorphisms. Finally, in Section 6 we discuss several elementary theorems about homomor-
phisms.
2. Familiar homomorphisms
The ﬁrst homomorphisms we will see involve functions at the level of precalculus, and include
identities such as the following:
c(x + y) = cx + cy,
|xy| = |x||y|,
(xy)2 = x2y2,
ax+y = axay,
(xy)c = xcyc,
loga(xy) = loga x + loga y,
Example 2.1. For each real number c, the formula c(x + y) = cx + cy for all x and y in R says
that the function Mc : R →R where Mc(x) = cx is a homomorphism.
Example 2.2. For all real numbers x and y, |xy| = |x||y|. Therefore the absolute value function
f : R× →R>0, given by f(x) = |x|, is a homomorphism. (We exclude 0, even though it works in
the formula, in order for the absolute value function to be a homomorphism on a group.)
Example 2.3. For x ∈R×, let s(x) be its sign: s(x) = 1 for x > 0 and s(x) = −1 for x < 0. Then
s(xy) = s(x)s(y) for all x and y in R×, so s: R× →{±1} is a homomorphism.
Example 2.4. For all real numbers x and y, (xy)2 = x2y2, so the squaring map f : R× →R×
where f(x) = x2 is a homomorphism. (We exclude 0 from the domain, even though (xy)2 = x2y2
when x or y is 0, in order to have the domain be a multiplicative group.) The squaring map is also
a homomorphism R× →R>0, R>0 →R×, and R>0 →R>0.
A function is not determined completely just by how you compute it, but also by the set on
which it is deﬁned and the set in which its values are considered to lie. Therefore the four ways
we described squaring as a homomorphism are diﬀerent functions, hence diﬀerent homomorphisms;
1

<!-- page 2 -->
2
KEITH CONRAD
squaring R× →R× is neither injective nor surjective, squaring R× →R>0 is surjective but not
injective, squaring R>0 →R× is injective but not surjective, and squaring R>0 →R>0 is injective
and surjective.
Example 2.5. Fix an integer n. For all real numbers x and y, (xy)n = xnyn, so the n-th power
map f : R× →R×, where f(x) = xn, is a homomorphism.
Example 2.6. For all positive numbers x and y, √xy = √x√y, so the square root function
f : R>0 →R>0, where f(x) = √x, is a homomorphism.
Example 2.7. Fix a nonzero real number a. Since am+n = aman for all integers m and n the
function f : Z →R× where f(n) = an satisﬁes f(m + n) = f(m)f(n) for all m and n, so f is a
homomorphism from the (additive) group Z to the (multiplicative) group R×.
Example 2.8. Fix nonzero real numbers a and b and let f : Z2 →R× by f(m, n) = ambn. For all
integer pairs (m, n) and (m′, n′), we have
f((m, n) + (m′, n′)) = f(m + m′, n + n′) = am+m′bn+n′ = amam′bnbn′
and
f(m, n)f(m′, n′) = ambnam′bn′.
The two computations produce the same answer, so f((m, n)+(m′, n′)) = f(m, n)f(m′, n′). There-
fore f is a homomorphism from Z2 (an additive group) to R× (a multiplicative group).
This can be extended to any ﬁnite number of bases: for any a1, . . . , ak in R× we get a homo-
morphism f : Zk →R× by f(m1, . . . , mk) = am1
1
· · · amk
k .
Example 2.9. Fix a positive real number a. We can raise a not just to integral powers, but to
arbitrary real powers (this is false for negative a). The equation ax+y = axay, valid for all real
numbers x and y, tells us that the exponential function with base a, sending x to ax, deﬁnes a
homomorphism R →R× and it is injective (that is, ax = ay ⇒x = y). The values of the function
ax are positive, and if we view ax as a function R →R>0 then this homomorphism is not just
injective but also surjective provided a ̸= 1.
Example 2.10. Fixing c > 0, the formula (xy)c = xcyc for positive x and y tells us that the
function f : R>0 →R>0 where f(x) = xc is a homomorphism.
Example 2.11. For a > 0 with a ̸= 1, the formula loga(xy) = loga x + loga y for all positive x and
y says that the base a logarithm loga : R>0 →R is a homomorphism.
The functions x 7→ax and x 7→loga x, from R to R>0 and from R>0 to R respectively, are
probably the most important examples of homomorphisms in precalculus. Let’s turn now to some
homomorphisms involving complex numbers.
Example 2.12. For a complex number z = a + bi, with real part a and imaginary part b, its
complex conjugate is z = a −bi. For all z and w in C,
(2.1)
z + w = z + w
and
zw = z w.
To verify these, we give names to the real and imaginary parts of z and w and compute both sides.
Writing z as a + bi and w as c + di for a, b, c, d ∈R, we have
z + w = (a + bi) + (c + di) = (a + c) + (b + d)i = (a + c) −(b + d)i
and
z + w = (a −bi) + (c −di) = (a + c) −(b + d)i,

<!-- page 3 -->
HOMOMORPHISMS
3
which both match. For multiplication,
zw = (a + bi)(c + di) = (ac −bd) + (ad + bc)i = (ac −bd) −(ad + bc)i
and
z w = (a −bi)(c −di) = (ac −bd) + (a(−d) + (−b)c)i = (ac −bd) −(ad + bc)i.
Therefore complex conjugation deﬁnes homomorphisms C →C and C× →C×.
Example 2.13. For a complex number z = a + bi, its absolute value is |z| =
√
a2 + b2. When
z and w are any complex numbers, |zw| = |z||w|, which implies that the absolute value function
on nonzero complex numbers is a homomorphism C× →R>0. (We have to exclude 0 from the
function to have a homomorphism, even though the formula itself is true when z or w is 0.)
To verify |zw| = |z||w|, write z = a + bi and w = c + di. Then
|zw| = |(a + bi)(c + di)| = |(ac −bd) + (ad + bc)i| =
p
(ac −bd)2 + (ad + bc)2
and
|z||w| =
p
a2 + b2p
c2 + d2 =
p
(a2 + b2)(c2 + d2) =
p
a2c2 + a2d2 + b2c2 + b2d2.
These don’t visibly look the same, but their equality falls out if we calculate |zw| a little further:
underneath the square root,
(ac −bd)2 + (ad + bc)2 = (a2c2 −2acbd + b2d2) + (a2d2 + 2adbc + b2c2),
and the two underlined terms on the right cancel. We are left with the sum of four terms that also
appear under the square root in |z||w|, so |zw| = |z||w|.
Here is a slicker way to see why |zw| = |z||w|. We had previously checked that complex conju-
gation is multiplicative (that is, zw = z w). Since a2 + b2 = (a + bi)(a −bi), we can write |z|2 = zz.
Then
|zw|2 = zwzw = zwz w = zzww = |z|2|w|2 = (|z||w|)2.
Since |zw| and |z||w| are nonnegative real numbers, from their squares being equal we know they
must be equal.
Example 2.14. The two addition laws for the sine and cosine functions are
(2.2)
sin(x + y) = sin x cos y + cos x sin y,
cos(x + y) = cos x cos y −sin x sin y.
These two separate formulas are complicated, but if we package them together as the real and
imaginary part of a single function with values in the complex numbers then (2.2) becomes cleaner:
letting f : R →C× by f(x) = cos x + i sin x, (2.2) is the same as f(x + y) = f(x)f(y). That is, if
you calculate the real and imaginary parts of f(x + y) and of f(x)f(y), then equality of the real
parts is the addition formula for cosine and equality of the imaginary parts is the addition formula
for sine. Therefore the equations (2.2) tell us that f is a homomorphism from R to C×. (The
values of f(x) are deﬁnitely not 0 because |f(x)| =
p
cos2 x + sin2 x = 1 for all x.)
3. Examples in linear algebra and modular arithmetic
Example 3.1. Fix an m × n matrix A. Using A we get a matrix transformation f : Rn →Rm by
f(x) = Ax. Both Rn and Rm are additive groups and the formula A(x + y) = Ax + Ay says that
f is a homomorphism.

<!-- page 4 -->
4
KEITH CONRAD
Example 3.2. For any 2 × 2 real matrices A and B, det(AB) = det(A) det(B). If we restrict our
attention to invertible matrices, whose determinants are nonzero, then we have a homomorphism
det: GL2(R) →R×.
(The identity det(AB) = det(A) det(B) can be checked by writing A = ( a b
c d ) and B = ( x y
z w ),
computing AB as a 2 × 2 matrix, then det(AB), and checking it equals det(A) det(B). If you take
a second course in linear algebra you may see slicker ways to understanding why the determinant
is multiplicative.)
Example 3.3. In the group Aﬀ(R) = {( a b
0 1 ) : a ∈R×, b ∈R}, the formula for multiplication is
(3.1)

a
b
0
1
 
c
d
0
1

=

ac
ad + b
0
1

.
The upper left matrix entry lies in the group R×, and under multiplication in Aﬀ(R) the upper
left entries multiply together, so we get a homomorphism f : Aﬀ(R) →R× by f( a b
0 1 ) = a. That
is, (3.1) tells us f(( a b
0 1 )( c d
0 1 )) = ac = f( a b
0 1 )f( c d
0 1 ).
Another way to think about this is that the upper left matrix entry in Aﬀ(R) is the determinant:
det( a b
0 1 ) = a, so multiplicativity of f is a special case of the multiplicativity of determinants.
Some of the previous examples work with Z/(m) in place of R and (Z/(m))× in place of R×.
Example 3.4. For each c ∈Z let Mc : Z/(m) →Z/(m) by Mc(x mod m) = cx mod m. The
algebraic formula c(x + y) ≡cx + cy mod m means Mc is a homomorphism.
Example 3.5. Fixing a positive integer n, the congruence (xy)n ≡xnyn mod m for all x and y in
Z implies that the n-th power map (Z/(m))× →(Z/(m))× is a homomorphism.
Here is what cubing (x 7→x3) looks like on (Z/(15))× and (Z/(21))×.
a mod 15
1
2
4
7
8
11
13
14
a3 mod 15
1
8
4
13
2
11
7
14
a mod 21
1
2
4
5
8
10
11
13
16
17
19
20
a3 mod 21
1
8
1
20
8
13
8
13
1
20
13
20
In the ﬁrst table, cubing permutes the elements of (Z/(15))×, while in the second table there are
only 4 cubes and each cube arises 3 times.
Example 3.6. Fixing an integer m ≥1, we deﬁne addition in Z/(m) by a + b = a + b. That is,
the addition on the left is deﬁned to be given by the formula on the right. Thus the reduction map
Z →Z/(m), where a 7→a (= a mod m), is a homomorphism by deﬁnition.
Example 3.7. We can reduce not only from Z to any Z/(m), but from any Z/(m) to Z/(d) where
d | m: if a ≡b mod m, so m | (a −b), then d | (a −b) too, so a ≡b mod d.
For instance,
19 ≡7 mod 6 and also 19 ≡7 mod 3. Let r: Z/(m) →Z/(d) by r(a mod m) = a mod d. This is a
homomorphism:
r(a mod m + b mod m) = r(a + b mod m)
= a + b mod d
= a mod d + b mod d
= r(a mod m) + r(b mod m).
Here we write a mod m and a mod d instead of a as in Example 3.6, because the latter notation is
now ambiguous on account of the use of two moduli, m and d, in this setup.

<!-- page 5 -->
HOMOMORPHISMS
5
Example 3.8. For positive integers m and d with d | m, the reduction map Z/(m) →Z/(d) is not
just additive, but multiplicative:
r(a mod m · b mod m) = r(ab mod m)
= ab mod d
= a mod d · b mod d
= r(a mod m)r(b mod m).
If we focus on invertible numbers, then reduction sends (Z/(m))× to (Z/(d))× since an inte-
ger relatively prime to m is also relatively prime to any factor of m. Thus the reduction map
(Z/(m))× →(Z/(d))×, where a mod m 7→a mod d, is a homomorphism.
Here are examples of reduction (Z/(15))× →(Z/(3))× and (Z/(21))× →(Z/(7))×, as tables.
a mod 15
1
2
4
7
8
11
13
14
a mod 3
1
2
1
1
2
2
1
2
a mod 21
1
2
4
5
8
10
11
13
16
17
19
20
a mod 7
1
2
4
5
1
3
4
6
2
3
5
6
In both tables, every value occurs the same number of times (4 times in the ﬁrst table and 2
times in the second table). We saw this in the tables at the end of Example 3.5: each value of a
homomorphism occurs equally often.
4. Other examples
Example 4.1. For any permutation σ ∈Sn, its sign sgn(σ) is ±1 and the formula sgn(σσ′) =
sgn(σ) sgn(σ′) for all σ and σ′ in Sn tells us that sgn: Sn →{±1} is a homomorphism.
Example 4.2. For any groups G and H there is always at least one homomorphism from G to
H, namely the trivial homomorphism f : G →H where f(x) = eH for all x ∈G. Every value of
f is the identity element of H. Then f(x)f(y) = eHeH = eH = f(xy). For some groups the only
homomorphism between them is the trivial homomorphism (e.g., G = Z/(3) and H = Z/(5)).
Example 4.3. Let G be an abelian group and n be an integer (positive, negative, or 0). The
formula
(gh)n = gnhn
for all g, h ∈G says that the nth power map G →G, where g 7→gn, is a homomorphism from G
to itself.
Warning: Power functions are usually not homomorphisms on nonabelian groups! For example,
in D4 we have (rs)3 = rs while r3s3 = r3s, and rs ̸= r3s because r ̸= r3, so f(x) = x3 on D4 is not
a homomorphism. The exact same calculation goes through in Dm for any m ≥3.
Example 4.4. In a group G, ﬁx an element g. Its powers satisfy
gm+n = gmgn
for all integers m and n, so we get a homomorphism Z →G given by n 7→gn is a homomorphism.
Note G doesn’t have to be abelian here; the only values we meet are powers of g, and powers of a
single element always commute with each other, whether or not the whole group is abelian.

<!-- page 6 -->
6
KEITH CONRAD
Example 4.5. Fix an element g in a group G. Conjugation by g is a function γg : G →G, given
by γg(x) = gxg−1, and it is a homomorphism:
γg(x)γg(y) = (gxg−1)(gyg−1) = gxg−1gyg−1 = gxyg−1 = γg(xy).
While power functions on abelian groups might not be invertible (e.g., squaring on R× is not
invertible since x2 = (−x)2), conjugation on any group by any element is always invertible: just
conjugate by the inverse element. Indeed,
γg−1(γg(x)) = γg−1(gxg−1) = g−1(gxg−1)g = g−1gxg−1g = x
for every x ∈G, so γg and γg−1 are inverses of each other.
5. Nonexamples
Nonexample 5.1. On the group GL2(R), let f(A) = A2, so f : GL2(R) →GL2(R). For most
A and B, f(AB) ̸= f(A)f(B). For instance, let A = ( 1 1
0 1 ) and B = ( 1 0
1 1 ). Then AB = ( 2 1
1 1 ), so
f(AB) = ( 2 1
1 1 )2 = ( 5 3
3 2 ), while f(A)f(B) = ( 1 1
0 1 )2( 1 0
1 1 )2 = ( 1 2
0 1 )( 1 0
2 1 ) = ( 5 2
2 1 ).
Nonexample 5.2. On any group G the nth power map G →G, where x 7→xn, makes sense, but
it usually is not a homomorphism when G is nonabelian. The previous example shows squaring on
GL2(R) is not a homomorphism. We saw after Example 4.3 that cubing on D4, or on Dm for any
m ≥3, is not a homomorphism.
When n = −1 or 2, the nth power map is a homomorphism from G to G only when G is abelian:
(xy)2 = x2y2 ⇐⇒xyxy = xxyy ⇐⇒yx = xy
and
(xy)−1 = x−1y−1 ⇐⇒(xy)−1 = (yx)−1 ⇐⇒xy = yx.
Nonexample 5.3. While det(AB) = det(A) det(B) for all 2 × 2 real matrices A and B, the deter-
minant M2(R) →R is not a homomorphism since M2(R) and R are not groups for multiplication.
Nonexample 5.4. For a 2×2 real matrix A, its exponential is deﬁned by the inﬁnite matrix series
exp(A) :=
X
n≥0
1
n!An = I2 + A + 1
2A2 + 1
6A3 + · · · .
In particular, exp(O) = I2 and exp(I2) = ( e 0
0 e ) = eI2. When A and B are commuting matrices,
exp(A + B) = exp(A) exp(B), so exp(A) exp(−A) = exp(O) = I2 by using B = −A.
Thus
exp(A) ∈GL2(R), so the 2 × 2 matrix exponential is a function M2(R) →GL2(R), from an
additive group to a multiplicative group. This is analogous to the classical function ex being a
function R →R×. However, the matrix exponential is not a homomorphism: exp(A + B) usually
is not exp(A) exp(B) when A and B don’t commute.
As a speciﬁc example, let A = ( 1 1
0 1 ) and B = ( 1 0
1 1 ). Check AB ̸= BA, exp(A) = ( e e
0 e ), and
exp(B) = ( e 0
e e ). Then exp(A) exp(B) = ( e e
0 e )( e 0
e e ) = ( 2e2 e2
e2 e2 ). Since A + B = ( 2 1
1 2 ) = I2 + C
where C = ( 1 1
1 1 ), and I2 and C commute, we have exp(A + B) = exp(I2 + C) = exp(I2) exp(C) =
e exp(C). Check by induction that Cn = 2n−1C for n ≥1, but not at n = 0. Then exp(C) =
I2 + P
n≥1(2n−1/n!)C = I2 + e2−1
2 C, so exp(A + B) = e(I2 + e2−1
2 C) = e( (e2+1)/2 (e2−1)/2
(e2−1)/2 (e2+1)/2 ) =
( (e3+e)/2 (e3−e)/2
(e3−e)/2 (e3+e)/2 ). Thus exp(A + B) ̸= exp(A) exp(B).

<!-- page 7 -->
HOMOMORPHISMS
7
Nonexample 5.5. In Example 3.3 we saw that the function f : Aﬀ(R) →R× by f( a b
0 1 ) = a is
a homomorphism. However, the function f : Aﬀ(R) →R by f( a b
0 1 ) = b is not a homomorphism.
Indeed, from the multiplication formula (3.1) we have f(( a b
0 1 )( c d
0 1 )) = ad+b, while f( a b
0 1 )+f( c d
0 1 ) =
b + d. These don’t match in general (anytime d ̸= 0 and a ̸= 1).
6. A few theorems about homomorphisms
Theorem 6.1. Let f : G →H be a homomorphism between two groups.
(1) f(eG) = eH, i.e., the identity in G goes to the identity in H.
(2) For all x ∈G, f(x−1) = f(x)−1.
(3) For all n ∈Z and x ∈G, f(xn) = f(x)n.
Proof. 1) Apply f to both sides of the equation eGeG = eG. We get f(eG)f(eG) = f(eG). Rewrite
that as f(eG)f(eG) = f(eG)eH and cancel f(eG) from both sides to get f(eG) = eH.
2) Apply f to both sides of the equation xx−1 = eG to get f(x)f(x−1) = f(eG), so f(x)f(x−1) =
eH by (1). Therefore f(x) is the inverse of f(x−1), so f(x−1) = f(x)−1.
3) We will prove this for n ≥1 by induction. That f(xn) = f(x)n when n = 1 is obvious.
Assuming f(xn) = f(x)n for some n ≥1, we get f(xn+1) = f(xnx) = f(xn)f(x) = f(x)nf(x) =
f(x)n+1; the 3rd equality at the end used the induction hypothesis.
For n = 0 the desired identity f(xn) = f(x)n is the same as f(eG) = eH, which we showed in
(1). For n < 0, write n = −N with N ≥1. Then
f(xn) = f(x−N) = f((xN)−1) = f(xN)−1 = (f(x)N)−1 = f(x)−N = f(x)n,
where the already proved cases of positive exponents and exponent −1 were used in the calculation.
□
Example 6.2. For an exponential function x 7→ax, which is a homomorphism R →R>0, Theorem
6.1 becomes the known identities a0 = 1, a−x = (ax)−1, and anx = (ax)n (note that in an additive
group such as R, the abstract multiplicative notation xn becomes nx).
Example 6.3. For a logarithm function x 7→loga x, which is a homomorphism R>0 →R, Theorem
6.1 becomes the identities loga(1) = 0, loga(1/x) = −loga x, and loga(xn) = n loga x.
Corollary 6.4. If f : G →H is a homomorphism and x ∈G has order n, then f(x) has order
dividing n.
Proof. Since x has order n, xn = eG. Applying f to both sides, f(x)n = eH, so the order of f(x)
divides n.
□
Example 6.5. In the second table of Example 3.8 we see the eﬀect of the reduction homomorphism
(Z/(21))× →(Z/(7))×. The number 11 mod 21 has order 6, while 11 mod 7 reduces to 4, which
has order 3. The number 8 mod 21 has order 2 , while 8 mod 7 it reduces to 1, which has order 1.
Theorem 6.6. The composition of homomorphisms is a homomorphism: if f1 : G1 →G2 and
f2 : G2 →G3 are homomorphisms, then the composite function f2 ◦f1 : G1 →G3 is a homomor-
phism.
Proof. This is straightforward: for all x and y in G1, we have
(f2 ◦f1)(xy) = f2(f1(xy)) = f2(f1(x)f1(y)) = f2(f1(x))f2(f1(y)) = (f2 ◦f1)(x)(f2 ◦f1)(y).
□
Example 6.7. The function f : GL2(R) →R>0 where f(A) = | det A| is a homomorphism since
it is the composition of the determinant det: GL2(R) →R× and absolute value | · |: R× →R>0,
which are both homomorphisms.

<!-- page 8 -->
8
KEITH CONRAD
For a function f : X →Y , the image of a subset A ⊂X is f(A) := {f(a) : a ∈A}, and the
inverse image of a subset B ⊂Y is f−1(B) := {x ∈X : f(x) ∈B}.
Example 6.8. Let f : R →R by f(x) = x2 + 1. (This is not a homomorphism, just a function.)
Then f({4, 8}) = {17, 65}, f−1({5}) = {2, −2}, f([1, 3]) = [2, 10], f−1([2, 10]) = [1, 3] ∪[−3, −1],
and f−1(1/2) = ∅.
Theorem 6.9. Let f : G →H be a homomorphism of groups.
(1) The image of a subgroup of G is a subgroup of H. In particular, f(G) is a subgroup of H.
(2) The inverse image of a subgroup of H is a subgroup of G.
Proof. 1) Let K be a subgroup of G, so f(K) = {f(k) : k ∈K}. Showing this is a subgroup of H
is a straightforward calculation using deﬁnitions:
• The identity of H is in f(K) since eH = f(eG) and eG ∈K.
• Pick any two elements of f(K). They have the form f(k) and f(k′) for some k and k′ in K.
Then their product is f(k)f(k′) = f(kk′), and kk′ ∈K since K is a subgroup of G. Thus
f(k)f(k′) ∈f(K).
• Pick any element of f(K). It has the form f(k) for some k ∈K. Its inverse is f(k)−1 =
f(k−1), and k−1 ∈K since K is a subgroup of G. Therefore f(k)−1 ∈f(K).
2) Choose a subgroup L of H. To see that f−1(L) is a subgroup of G we just check the deﬁnitions.
• Since f(eG) = eH ∈L, we get eG ∈f−1(L).
• Pick any two elements of f−1(L), say x and y. That means f(x) ∈L and f(y) ∈L. Since
L is a subgroup of H, f(x)f(y) ∈L, so f(xy) ∈L. Therefore xy ∈f−1(L).
• Pick any element of f−1(L), say x. Then f(x) ∈L. Since f(x−1) = f(x)−1, and L is a
subgroup of H, we have f(x)−1 ∈L. Therefore f(x−1) ∈L, so x−1 ∈f−1(L).
□
Example 6.10. By Example 3.5, cubing (Z/(21))× →(Z/(21))× has image {1, 8, 13, 20 mod 21},
and this is a subgroup of (Z/(21))×.
Example 6.11. By Example 3.5, cubing (Z/(21))× →(Z/(21))× on the subgroup ⟨2 mod 21⟩=
{1, 2, 4, 8, 16, 11} has image {1, 8 mod 21}, and this is a subgroup of (Z/(21))×.
Example 6.12. In (Z/(21))×, ⟨20 mod 21⟩= {1, 20}. By Example 3.5, the inverse image of {1, 20}
under the cubing map (Z/(21))× →(Z/(21))× is {x : x3 ≡1 or 20 mod 21} = {1, 4, 5, 16, 17, 20} =
⟨5⟩, and this is a subgroup of (Z/(21))×.
7. The kernel of a homomorphism
There is no simple test for showing a homomorphism is surjective in general, but here is a very
important way to show a homomorphism is injective.
Theorem 7.1. A homomorphism f : G →H is injective if and only if the unique solution to
f(x) = eH is eG.
The condition in this theorem is saying that when a homomorphism takes the value eH just once
(necessarily at x = eG) then there is at most one way it takes any other value.
Proof. First suppose f is injective. The condition f(x) = eH is the same as f(x) = f(eG), and by
injectivity of f this equality implies x = eG.
Now suppose the only solution to f(x) = eH is x = eG.
To show f is injective, suppose
f(g) = f(g′). Because f is a homomorphism, we can rewrite the condition f(g) = f(g′) in the form
f(something) = eH:
f(g) = f(g′) =⇒f(g)f(g′)−1 = eH =⇒f(g)f((g′)−1) = eH =⇒f(g(g′)−1) = eH.

<!-- page 9 -->
HOMOMORPHISMS
9
Therefore g(g′)−1 = eG, so g = g′.
□
We can see Theorem 7.1 at work in the tables at the end of Example 3.5: cubing on (Z/(15))×
is injective and 1 occurs as a value just once, while cubing on (Z/(21))× is not injective and 1
appears as a value several times. Similarly, the reduction homomorphisms (Z/(15))× →(Z/(3))×
and (Z/(21))× →(Z/(7))× in the tables at the end of Example 3.8 are not injective and 1 appears
as a value of each homomorphism multiple times.
Knowing how the identity occurs as the value of a homomorphism is important, and gets the
following name.
Deﬁnition 7.2. The kernel of a homomorphism f : G →H is the set of elements in G sent to the
identity:1
ker f = {x ∈G : f(x) = eH}.
Example 7.3. The squaring map R× →R× has kernel {±1}. This is the solution set to x2 = 1.
Example 7.4. From tables in Example 3.5, cubing (Z/(15))× →(Z/(15))× has trivial kernel {1}
and cubing (Z/(21))× →(Z/(21))× has kernel {1, 8, 13, 20 mod 21}.
Example 7.5. From tables in Example 3.8, the reduction homomorphism (Z/(15))× →(Z/(3))×
has kernel {1, 4, 7, 13 mod 15} and reduction (Z/(21))× →(Z/(7))× has kernel {1, 8 mod 21}.
Example 7.6. The sign homomorphism sgn: Sn →{±1} has kernel An, the alternating group on
n letters.
Example 7.7. The homomorphism Aﬀ(R) →R× from Example 3.3, where ( a b
0 1 ) 7→a, has kernel
{( 1 b
0 1 ) : b ∈R}.
Most homomorphisms from precalculus have trivial kernel, so the kernel is not something inter-
esting at that level. But it is something that is met in linear algebra, under a diﬀerent name:
Example 7.8. For an m × n matrix A, the homomorphism f : Rn →Rm where f(x) = Ax has
kernel {x ∈Rn : Ax = 0}. In linear algebra this kernel is known as the null space of A.
Here is a kernel of a homomorphism that is related to periodicity of the trigonometric functions.
Example 7.9. The homomorphism R →C× from Example 2.14, where x 7→cos x + i sin x, has
kernel
{x ∈R : cos x + i sin x = 1} = {x ∈R : cos x = 1 and sin x = 0} = 2πZ,
the integral multiples of 2π.
Theorem 7.10. The kernel of a homomorphism f : G →H is a subgroup of G.
Proof. This is a straightforward calculation using deﬁnitions:
• Since f(eG) = eH, eG ∈ker f.
• For all x and y in ker f, f(xy) = f(x)f(y) = eHeH = eH, so xy ∈ker f.
• For all x ∈ker f, f(x−1) = f(x)−1 = e−1
H = eH, so x−1 ∈ker f.
Theorem 7.10 is a special case of part 2 of Theorem 6.9, since ker f = {x ∈G : f(x) = eH} =
f−1({eH}), which is the inverse image of the trivial subgroup of H.
□
Theorem 7.11. If f : G →H is a homomorphism with kernel K, then f(x) = f(y) if and only if
y = xk for some k ∈K.
1The term kernel is due to Pontryagin in 1931: see https://eudml.org/doc/159508, footnote on p. 186. Earlier
authors, like van der Waerden, simply wrote about “elements of G that are mapped to the identity in H.”

<!-- page 10 -->
10
KEITH CONRAD
Proof. Suppose f(x) = f(y). We want to show y = xk for some k ∈K. Necessarily k = x−1y, so we
want to show x−1y ∈K. This is a direct calculation: f(x−1y) = f(x−1)f(y) = f(x)−1f(y) = eH.
Conversely, suppose y = xk where k ∈K. Then f(y) = f(xk) = f(x)f(k) = f(x).
□
Example 7.12. The squaring function R× →R× has kernel ±1, and Theorem 7.11 in this instance
says something familiar: x2 = y2 in R× if and only if y = ±x. The way this is seen in school is
x2 = y2 ⇐⇒y2 −x2 = 0 ⇐⇒(y + x)(y −x) = 0 ⇐⇒y + x = 0 or y −x = 0 ⇐⇒y = ±x.
This is not the way the proof of Theorem 7.11 works. Instead, that proof in this instance would
use only multiplication and division: for nonzero real numbers x and y,
x2 = y2 ⇐⇒y2
x2 = 1 ⇐⇒
y
x
2
= 1 ⇐⇒y
x = ±1 ⇐⇒y = ±x.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*