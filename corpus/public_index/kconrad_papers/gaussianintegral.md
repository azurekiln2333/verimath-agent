# The Gaussian Integral

> **Source**: https://kconrad.math.uconn.edu/blurbs/gaussianintegral.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE GAUSSIAN INTEGRAL
KEITH CONRAD
Let
I =
Z ∞
−∞
e−1
2 x2 dx, J =
Z ∞
0
e−x2 dx,
and K =
Z ∞
−∞
e−πx2 dx.
These positive numbers are related: J = I/(2
√
2) and K = I/
√
2π.
Theorem. With notation as above, I =
√
2π, or equivalently J = √π/2, or equivalently K = 1.
We will give multiple proofs of this.
(Other lists of proofs are in [5] and [10].)
It is subtle
since e−1
2 x2 has no simple antiderivative. For comparison,
R ∞
0 xe−1
2 x2 dx can be computed with the
antiderivative −e−1
2 x2 and equals 1. In the last section, the Gaussian integral’s history is presented.
1. First Proof: Polar coordinates
The most widely known proof, due to Poisson [10, p. 3], expresses J2 as a double integral and
then uses polar coordinates. To start, write J2 as an iterated integral using single-variable calculus:
J2 = J
Z ∞
0
e−y2 dy =
Z ∞
0
Je−y2 dy =
Z ∞
0
Z ∞
0
e−x2 dx

e−y2 dy =
Z ∞
0
Z ∞
0
e−(x2+y2) dx dy.
View this as a double integral over the ﬁrst quadrant. To compute it with polar coordinates, the
ﬁrst quadrant is {(r, θ) : r ≥0 and 0 ≤θ ≤π/2}. Writing x2 + y2 as r2 and dx dy as r dr dθ,
J2 =
Z π/2
0
Z ∞
0
e−r2r dr dθ
=
Z ∞
0
re−r2 dr ·
Z π/2
0
dθ
= −1
2e−r2 
∞
0
· π
2
= 1
2 · π
2
= π
4 .
Since J > 0, J = √π/2.1 It is argued in [2] that this method can’t be used on any other integral.
2. Second Proof: Another change of variables
Our next proof uses another change of variables to compute J2. As before,
J2 =
Z ∞
0
Z ∞
0
e−(x2+y2) dx

dy.
1For a visualization of this calculation as a volume, in terms of
R ∞
−∞e−x2 dx instead of J, see https://www.
youtube.com/watch?v=cy8r7WSuT1I. We’ll do a volume calculation for I2 in Section 5.
1

<!-- page 2 -->
2
KEITH CONRAD
Instead of using polar coordinates, set x = yt in the inner integral (y is ﬁxed). Then dx = y dt and
(2.1)
J2 =
Z ∞
0
Z ∞
0
e−y2(t2+1)y dt

dy =
Z ∞
0
Z ∞
0
ye−y2(t2+1) dy

dt,
where the interchange of integrals is justiﬁed by Fubini’s theorem for improper Riemann integrals.
(The appendix gives an approach using Fubini’s theorem for Riemann integrals on rectangles.)
Since
Z ∞
0
ye−ay2 dy = 1
2a for a > 0, we have
J2 =
Z ∞
0
dt
2(t2 + 1) = 1
2 · π
2 = π
4 ,
so J = √π/2. This proof is due to Laplace [8, pp. 94–96] and historically precedes the widely used
technique of the previous proof. We will see in Section 9 what Laplace’s ﬁrst proof was.
3. Third Proof: Differentiating under the integral sign
For t > 0, set
A(t) =
Z t
0
e−x2 dx
2
.
The integral we want to calculate is A(∞) = J2 and then take a square root.
Diﬀerentiating A(t) with respect to t and using the Fundamental Theorem of Calculus,
A′(t) = 2
Z t
0
e−x2 dx · e−t2 = 2e−t2 Z t
0
e−x2 dx.
Let x = ty, so
A′(t) = 2e−t2 Z 1
0
te−t2y2 dy =
Z 1
0
2te−(1+y2)t2 dy.
The function under the integral sign is easily antidiﬀerentiated with respect to t:
A′(t) =
Z 1
0
−∂
∂t
e−(1+y2)t2
1 + y2
dy = −d
dt
Z 1
0
e−(1+y2)t2
1 + y2
dy.
Letting
B(t) =
Z 1
0
e−t2(1+x2)
1 + x2
dx,
we have A′(t) = −B′(t) for all t > 0, so there is a constant C such that
(3.1)
A(t) = −B(t) + C
for all t > 0. To ﬁnd C, we let t →0+ in (3.1). The left side tends to
Z 0
0
e−x2 dx
2
= 0 while
the right side tends to −
Z 1
0
dx/(1 + x2) + C = −π/4 + C. Thus C = π/4, so (3.1) becomes
Z t
0
e−x2 dx
2
= π
4 −
Z 1
0
e−t2(1+x2)
1 + x2
dx.
Letting t →∞in this equation, we obtain J2 = π/4, so J = √π/2.
A comparison of this proof with the ﬁrst proof is in [22].

<!-- page 3 -->
THE GAUSSIAN INTEGRAL
3
4. Fourth Proof: Another differentiation under the integral sign
Here is a second approach to ﬁnding J by diﬀerentiation under the integral sign. I heard about
it from Michael Rozman [15], who modiﬁed an idea on math.stackexchange [24], and in a slightly
less elegant form it appeared much earlier in [20].
For t ∈R, set
F(t) =
Z ∞
0
e−t2(1+x2)
1 + x2
dx.
Then F(0) =
R ∞
0 dx/(1 + x2) = π/2 and F(∞) = 0. Diﬀerentiating under the integral sign,
F ′(t) =
Z ∞
0
−2te−t2(1+x2) dx = −2te−t2 Z ∞
0
e−(tx)2 dx.
Make the substitution y = tx, with dy = t dx, so
F ′(t) = −2e−t2 Z ∞
0
e−y2 dy = −2Je−t2.
For b > 0, integrate both sides from 0 to b and use the Fundamental Theorem of Calculus:
Z b
0
F ′(t) dt = −2J
Z b
0
e−t2 dt =⇒F(b) −F(0) = −2J
Z b
0
e−t2 dt.
Letting b →∞in the last equation,
0 −π
2 = −2J2 =⇒J2 = π
4 =⇒J =
√π
2 .
5. Fifth Proof: A volume integral
Our next proof is due to T. P. Jameson [6] and was rediscovered by A. L. Delgado [4]. Revolve
z = e−1
2 x2 in the xz-plane around the z-axis to produce the “bell surface” z = e−1
2 (x2+y2). See
Figure 1, where the z-axis is vertical and passes through the top point, the x-axis lies just under
the surface through the point 0 in front, and the y-axis lies just under the surface through the
point 0 on the left. We will compute the volume V below the surface and above the xy-plane in
two ways.
First we compute V by horizontal slices, which are discs: V =
Z 1
0
A(z) dz where A(z) is the area
of the disc formed by slicing the surface at height z. Writing the radius of the disc at height z as
r(z), A(z) = πr(z)2. To compute r(z), the surface cuts the xz-plane at a pair of points (x, e−1
2 x2)
where the height is z, so e−1
2 x2 = z. Thus x2 = −2 ln z. Since x is the distance of these points from
the z-axis, r(z)2 = x2 = −2 ln z, so A(z) = πr(z)2 = −2πln z. Therefore
V =
Z 1
0
−2π ln z dz = −2π (z ln z −z)

1
0
= −2π(−1 −lim
z→0+ z ln z).
By L’Hospital’s rule, limz→0+ z ln z = 0, so V = 2π. (A calculation of V by shells is in [12].)
Next we compute V by vertical slices in planes x = constant. Vertical slices are scaled bell
curves: look at the black contour lines in Figure 1. The equation of the bell curve along the top
of the vertical slice with x-coordinate x is z = e−1
2 (x2+y2), where y varies and x is ﬁxed. Then

<!-- page 4 -->
4
KEITH CONRAD
Figure 1. The bell surface z = e−1
2 (x2+y2)
V =
Z ∞
−∞
A(x) dx, where A(x) is the area of the x-slice:
A(x) =
Z ∞
−∞
e−1
2 (x2+y2) dy = e−1
2 x2 Z ∞
−∞
e−1
2 y2 dy = e−1
2 x2I.
Thus V =
Z ∞
−∞
A(x) dx =
Z ∞
−∞
e−1
2 x2I dx = I
Z ∞
−∞
e−1
2 x2 dx = I2.
Comparing the two formulas for V , we have 2π = I2, so I =
√
2π.
6. Sixth Proof: The Γ-function
For any integer n ≥0, we have n! =
Z ∞
0
tne−t dt. For x > 0 we deﬁne
Γ(x) =
Z ∞
0
txe−t dt
t ,
so Γ(n) = (n −1)! when n ≥1. Using integration by parts, Γ(x + 1) = xΓ(x). One of the basic
properties of the Γ-function [16, pp. 193–194] is
(6.1)
Γ(x)Γ(y)
Γ(x + y) =
Z 1
0
tx−1(1 −t)y−1 dt.

<!-- page 5 -->
THE GAUSSIAN INTEGRAL
5
Set x = y = 1/2:
Γ
1
2
2
=
Z 1
0
dt
p
t(1 −t)
.
Note
Γ
1
2

=
Z ∞
0
√
te−t dt
t =
Z ∞
0
e−t
√
t dt =
Z ∞
0
e−x2
x 2x dx = 2
Z ∞
0
e−x2 dx = 2J,
so 4J2 =
R 1
0 dt/
p
t(1 −t). With the substitution t = sin2 θ,
4J2 =
Z π/2
0
2 sin θ cos θ dθ
sin θ cos θ
= 2π
2 = π,
so J = √π/2. Equivalently, Γ(1/2) = √π. Any method that proves Γ(1/2) = √π is also a method
that calculates
Z ∞
0
e−x2 dx.
7. Seventh Proof: Asymptotic estimates
We will show J = √π/2 by a technique whose steps are based on [17, p. 371].
For x ≥0, power series expansions show 1 + x ≤ex ≤1/(1 −x). Reciprocating and replacing x
with x2, we get
(7.1)
1 −x2 ≤e−x2 ≤
1
1 + x2 .
for all x ∈R.
For any positive integer n, raise the terms in (7.1) to the nth power and integrate from 0 to 1:
Z 1
0
(1 −x2)n dx ≤
Z 1
0
e−nx2 dx ≤
Z 1
0
dx
(1 + x2)n .
Using the changes of variables x = sin θ on the left, x = y/√n in the middle, and x = tan θ on the
right,
(7.2)
Z π/2
0
(cos θ)2n+1 dθ ≤
1
√n
Z √n
0
e−y2 dy ≤
Z π/4
0
(cos θ)2n−2 dθ <
Z π/2
0
(cos θ)2n−2 dθ.
Set Ik =
R π/2
0
(cos θ)k dθ, so I0 = π/2, I1 = 1, and (7.2) implies
(7.3)
√nI2n+1 ≤
Z √n
0
e−y2 dy < √nI2n−2.
We will show that as k →∞, kI2
k →π/2. Then
√nI2n+1 =
√n
√2n + 1
√
2n + 1I2n+1 →
1
√
2
rπ
2 =
√π
2
and
√nI2n−2 =
√n
√2n −2
√
2n −2I2n−2 →
1
√
2
rπ
2 =
√π
2 ,
so by (7.3),
Z √n
0
e−y2 dy →√π/2. Thus J = √π/2.

<!-- page 6 -->
6
KEITH CONRAD
To show kI2
k →π/2, ﬁrst we compute several values of Ik explicitly by a recursion.
Using
integration by parts,
Ik =
Z π/2
0
(cos θ)k dθ =
Z π/2
0
(cos θ)k−1 cos θ dθ = (k −1)(Ik−2 −Ik),
so
(7.4)
Ik = k −1
k
Ik−2.
Using (7.4) and the initial values I0 = π/2 and I1 = 1, the ﬁrst few values of Ik are computed and
listed in Table 1.
k
Ik
k
Ik
0
π/2
1
1
2
(1/2)(π/2)
3
2/3
4
(3/8)(π/2)
5
8/15
6
(15/48)(π/2)
7
48/105
Table 1.
From Table 1 we see that
(7.5)
I2nI2n+1 =
1
2n + 1
π
2
for 0 ≤n ≤3, and this can be proved for all n by induction using (7.4). Since 0 ≤cos θ ≤1 for
θ ∈[0, π/2], we have Ik ≤Ik−1 ≤Ik−2 =
k
k−1Ik by (7.4), so Ik−1 ∼Ik as k →∞. Therefore (7.5)
implies
I2
2n ∼1
2n
π
2 =⇒(2n)I2
2n →π
2
as n →∞. Then
(2n + 1)I2
2n+1 ∼(2n)I2
2n →π
2
as n →∞, so kI2
k →π/2 as k →∞. This completes our proof that J = √π/2.
Remark 7.1. This proof is closely related to the ﬁfth proof using the Γ-function. Indeed, by (6.1)
Γ(k+1
2 )Γ(1
2)
Γ(k+1
2
+ 1
2) =
Z 1
0
t(k+1)/2+1(1 −t)1/2−1 dt,
and with the change of variables t = (cos θ)2 for 0 ≤θ ≤π/2, the integral on the right is equal to
2
R π/2
0
(cos θ)k dθ = 2Ik, so (7.5) is the same as
I2nI2n+1 = Γ(2n+1
2
)Γ(1
2)
2Γ(2n+2
2
)
Γ(2n+2
2
)Γ(1
2)
2Γ(2n+3
2
)
= Γ(2n+1
2
)Γ(1
2)2
4Γ(2n+1
2
+ 1)
= Γ(2n+1
2
)Γ(1
2)2
42n+1
2
Γ(2n+1
2
)
=
Γ(1
2)2
2(2n + 1).

<!-- page 7 -->
THE GAUSSIAN INTEGRAL
7
By (7.5), π = Γ(1/2)2. We saw in the ﬁfth proof that Γ(1/2) = √π if and only if J = √π/2.
8. Eighth Proof: Stirling’s Formula
Besides the integral formula
Z ∞
−∞
e−1
2 x2 dx =
√
2π that we have been discussing, another place
in mathematics where
√
2π appears is in Stirling’s formula:
n! ∼nn
en
√
2πn as n →∞.
In 1730 De Moivre proved n! ∼C(nn/en)√n for some positive number C without being able to
determine C. Stirling soon thereafter showed C =
√
2π and wound up having the whole formula
named after him. We will show that determining that the constant C in Stirling’s formula is
√
2π
is equivalent to showing that J = √π/2 (or, equivalently, that I =
√
2π).
Applying (7.4) repeatedly,
I2n = 2n −1
2n
I2n−2
= (2n −1)(2n −3)
(2n)(2n −2)
I2n−4
...
= (2n −1)(2n −3)(2n −5) · · · (5)(3)(1)
(2n)(2n −2)(2n −4) · · · (6)(4)(2)
I0.
Inserting (2n −2)(2n −4)(2n −6) · · · (6)(4)(2) in the top and bottom,
I2n = (2n −1)(2n −2)(2n −3)(2n −4)(2n −5) · · · (6)(5)(4)(3)(2)(1)
(2n)((2n −2)(2n −4) · · · (6)(4)(2))2
π
2 =
(2n −1)!
2n(2n−1(n −1)!)2
π
2 .
Applying De Moivre’s asymptotic formula n! ∼C(n/e)n√n, ,
I2n ∼
C((2n −1)/e)2n−1√2n −1
2n(2n−1C((n −1)/e)n−1√n −1)2
π
2 =
(2n −1)2n
1
2n−1
√2n −1
2n · 22(n−1)Ce(n −1)2n
1
(n−1)2 (n −1)
π
2
as n →∞. For any a ∈R, (1 + a/n)n →ea as n →∞, so (n + a)n ∼eann. Substituting this into
the above formula with a = −1 and n replaced by 2n,
(8.1)
I2n ∼
e−1(2n)2n
1
√
2n
2n · 22(n−1)Ce(e−1nn)2 1
n2 n
π
2 =
π
C
√
2n.
Since Ik−1 ∼Ik, the outer terms in (7.3) are both asymptotic to √nI2n ∼π/(C
√
2) by (8.1).
Therefore
Z √n
0
e−y2 dy →
π
C
√
2
as n →∞, so J = π/(C
√
2). Therefore C =
√
2π if and only if J = √π/2.

<!-- page 8 -->
8
KEITH CONRAD
9. Ninth Proof: The original proof
The original proof that J = √π/2 is due to Laplace [9] in 1774. (An English translation of
Laplace’s article is mentioned in the bibliographic citation for [9], with preliminary comments on
that article in [19].) He wanted to compute
(9.1)
Z 1
0
dx
√−log x.
Setting y = √−log x, this integral is 2
R ∞
0 e−y2 dy = 2J, so we expect (9.1) to be √π.
Laplace’s starting point for evaluating (9.1) was a formula of Euler:
(9.2)
Z 1
0
xr dx
√
1 −x2s
Z 1
0
xs+r dx
√
1 −x2s =
1
s(r + 1)
π
2
for positive r and s. (Laplace himself said this formula held “whatever be” r or s, but if s < 0 then
the number under the square root is negative.) Accepting (9.2), let r →0 in it to get
(9.3)
Z 1
0
dx
√
1 −x2s
Z 1
0
xs dx
√
1 −x2s = 1
s
π
2 .
Now let s →0 in (9.3). Then 1 −x2s ∼−2s log x by L’Hopital’s rule, so (9.3) becomes
Z 1
0
dx
√−log x
2
= π.
Thus (9.1) is √π.
Euler’s formula (9.2) looks mysterious, but we have met it before. In the formula let xs = cos θ
with 0 ≤θ ≤π/2. Then x = (cos θ)1/s, and after some calculations (9.2) turns into
(9.4)
Z π/2
0
(cos θ)(r+1)/s−1 dθ
Z π/2
0
(cos θ)(r+1)/s dθ =
1
(r + 1)/s
π
2 .
We used the integral Ik =
R π/2
0
(cos θ)k dθ before when k is a nonnegative integer. This notation
makes sense when k is any positive real number, and then (9.4) assumes the form IαIα+1 =
1
α+1
π
2 for
α = (r+1)/s−1, which is (7.5) with a possibly nonintegral index. Letting r = 0 and s = 1/(2n+1)
in (9.4) recovers (7.5). Letting s →0 in (9.3) corresponds to letting n →∞in (7.5), so the proof
in Section 7 is in essence a more detailed version of Laplace’s 1774 argument.
10. Tenth Proof: Residue theorem
We will calculate
Z ∞
−∞
e−x2/2 dx using contour integrals and the residue theorem. However, we
can’t just integrate e−z2/2, as this function has no poles. For a long time nobody knew how to
handle this integral using contour integration.
For instance, in 1914 Watson [21, p. 79] wrote
“Cauchy’s theorem cannot be employed to evaluate all deﬁnite integrals; thus
Z ∞
0
e−x2 dx has not
been evaluated except by other methods.” In the 1940s several contour integral solutions were
published using awkward contours such as parallelograms [11], [13, Sect. 5] (see [3, Exer. 9, p. 113]
for a recent appearance). Our approach will follow Kneser [7, p. 121] (see also [14, pp. 413–414] or
[23]), using a rectangular contour and the function
e−z2/2
1 −e−√π(1+i)z .

<!-- page 9 -->
THE GAUSSIAN INTEGRAL
9
This function comes out of nowhere, so our ﬁrst task is to motivate the introduction of this function.
We seek a meromorphic function f(z) to integrate around the contour γR in Figure 2, with
vertices at −R, R, R + ib, and −R + ib, where b will be ﬁxed and we let R →∞.
Figure 2. Contour to compute Gaussian
Suppose f(z) →0 along the right and left sides of γR uniformly as R →∞. Then by applying
the residue theorem and letting R →∞, we would obtain (if the integrals converge)
Z ∞
−∞
f(x) dx +
Z −∞
∞
f(x + ib) dx = 2πi
X
a
Resz=af(z),
where the sum is over poles of f(z) with imaginary part between 0 and b. This is equivalent to
Z ∞
−∞
(f(x) −f(x + ib)) dx = 2πi
X
a
Resz=af(z).
Therefore we want f(z) to satisfy
(10.1)
f(z) −f(z + ib) = e−z2/2,
where f(z) and b need to be determined.
Let’s try f(z) = e−z2/2/d(z), for an unknown d(z) whose zeros are poles of f(z). We want
(10.2)
f(z) −f(z + τ) = e−z2/2
for some τ (which will not be purely imaginary, so (10.1) doesn’t quite work, but (10.1) is only
motivation). Substituting e−z2/2/d(z) for f(z) in (10.2) gives us
(10.3)
e−z2/2
 
1
d(z) −e−τz−τ 2/2
d(z + τ)
!
= e−z2/2.
Suppose d(z + τ) = d(z). Then (10.3) implies
d(z) = 1 −e−τz−τ 2/2,
and with this deﬁnition of d(z), e−z2/2/d(z) satisﬁes (10.2) if and only if eτ 2 = 1, or equivalently
τ 2 ∈2πiZ. The simplest nonzero solution is τ = √π(1 + i). From now on this is the value of τ, so
e−τ 2/2 = e−iπ = −1 and d(z) = 1 + e−τz. Set
f(z) = e−z2/2
d(z)
=
e−z2/2
1 + e−τz ,
which is Kneser’s function mentioned earlier. This function satisﬁes (10.2) and we henceforth ignore
the motivation (10.1). Poles of f(z) are at odd integral multiples of τ/2.
We will integrate this f(z) around the contour γR in Figure 3, whose height √π is Im(τ).

<!-- page 10 -->
10
KEITH CONRAD
Figure 3. The contour γR and poles of Kneser’s function
The poles of f(z) nearest the origin are plotted in Figure 3; they lie along the line y = x. The
only pole of f(z) inside γR (for R > √π/2) is at τ/2, so by the residue theorem
Z
γR
f(z) dz = 2πiResz=τ/2f(z) = 2πi
e−τ 2/8
(−τ)e−τ 2/2 =
2πie3τ 2/8
−√π(1 + i) =
2πie3πi/4
−√π(1 + i) =
√
2π.
Since the left and right sides of γR have the same length, √π, for all R, to show the integral of
f along those sides tends to 0 uniformly as R →∞, it suﬃces to show f(z) →0 uniformly along
those sides as R →∞. Parametrize z along the left and right sides as −R + it and R + it with t
running over [0, √π] in one direction or the other (which won’t matter since we’ll be taking absolute
values). Then, using the reverse triangle inequality in the denominator, when R > √π (so R > t)
|f(R + it)| = |e−R2/2−iRt+t2/2|
|1 + e−τ(R+it)|
≤
e−R2/2et2/2
|1 −e−Re(τ(R+it))| ≤
e−R2/2eπ/2
1 −e−√π(R−t) <
e−R2/2eπ/2
1 −e−√π(R−√π) ,
which tends to 0 as R →∞. Also
|f(−R + it)| = |e−R2/2+iRt+t2/2|
|1 + e−τ(−R+it)| ≤
e−R2/2et2/2
|1 −e−Re(τ(−R+it))| ≤e−R2/2eπ/2
e
√π(R+t) −1 < e−R2/2eπ/2
e
√πR −1 ,
which tends to 0 as R →∞. Thus
√
2π =
Z ∞
−∞
f(x) dx +
Z −∞+i√π
∞+i√π
f(z) dz =
Z ∞
−∞
f(x) dx −
Z ∞
−∞
f(x + i√π) dx.
In the second integral, write i√π as τ −π and use (real) translation invariance of dx to obtain
√
2π =
Z ∞
−∞
f(x) dx −
Z ∞
−∞
f(x + τ) dx =
Z ∞
−∞
(f(x) −f(x + τ)) dx =
Z ∞
−∞
e−x2/2 dx
by (10.2).
11. Eleventh Proof: Fourier transforms
For a continuous function f : R →C that is rapidly decreasing at ±∞, its Fourier transform is
the function Ff : R →C deﬁned by
(11.1)
(Ff)(y) =
Z ∞
−∞
f(x)e−ixy dx.
For example, (Ff)(0) =
R ∞
−∞f(x) dx. Here are three properties of the Fourier transform.

<!-- page 11 -->
THE GAUSSIAN INTEGRAL
11
• If f is diﬀerentiable, then after using diﬀerentiation under the integral sign on the Fourier
transform of f we obtain
(Ff)′(y) =
Z ∞
−∞
−ixf(x)e−ixy dx = −i(F(xf(x)))(y).
• Using integration by parts on the Fourier transform of f, with u = f(x) and dv = e−ixy dx,
we obtain
(F(f′))(y) = iy(Ff)(y).
• If we apply the Fourier transform twice then we recover the original function up to interior
and exterior scaling:
(11.2)
(F2f)(x) = 2πf(−x).
The 2π is admittedly a nonobvious scaling factor here, and the proof of (11.2) is nontrivial. We’ll
show the appearance of 2π in (11.2) is equivalent to the evaluation of I as
√
2π.
Fixing a > 0, set f(x) = e−ax2, so
f′(x) = −2axf(x).
Applying the Fourier transform to both sides of this equation implies iy(Ff)(y) = −2a 1
−i(Ff)′(y),
which simpliﬁes to (Ff)′(y) = −1
2ay(Ff)(y). The general solution of g′(y) = −1
2ayg(y) is g(y) =
Ce−y2/(4a), so
f(x) = e−ax2 =⇒(Ff)(y) = Ce−y2/(4a)
for some constant C. We have 1/(4a) = a when a = 1/2, so set a = 1/2: if f(x) = e−x2/2 then
(11.3)
(Ff)(y) = Ce−y2/2 = Cf(y).
Setting y = 0 in (11.3), the left side is (Ff)(0) =
R ∞
−∞e−x2/2 dx = I, so I = Cf(0) = C.
Applying the Fourier transform to both sides of (11.3) with C = I and using (11.2), we get
2πf(−x) = I(Ff)(x) = I2f(x). At x = 0 this becomes 2π = I2, so I =
√
2π since I > 0. That is
the Gaussian integral calculation. If we didn’t know that the constant on the right side of (11.2) is
2π, whatever its value is would wind up being I2, so saying 2π appears on the right side of (11.2)
is equivalent to saying I =
√
2π.
There are other ways to deﬁne the Fourier transform besides (11.1), such as
1
√
2π
Z ∞
−∞
f(x)e−ixy dx
or
Z ∞
−∞
f(x)e−2πixy dx.
These transforms have properties similar to the transform as deﬁned in (11.1), so they can be used
in its place to compute the Gaussian integral. Let’s see how such a proof looks using the second
alternative deﬁnition, which we’ll write as
( eFf)(y) =
Z ∞
−∞
f(x)e−2πixy dx.
For this Fourier transform, the analogue of the three properties above for F are
• ( eFf)′(y) = −2πi( eF(xf(x)))(y).
• ( eF(f′))(y) = 2πiy( eFf)(y).
• ( eF2f)(x) = f(−x).

<!-- page 12 -->
12
KEITH CONRAD
The last property for eF looks nicer than that for F, since there is no overall 2π-factor on the right
side (it has been hidden in the deﬁnition of eF). On the other hand, the ﬁrst two properties for eF
have overall factors of 2π on the right side while the ﬁrst two properties of F do not. You can’t
escape a role for π or 2π somewhere in every possible deﬁnition of a Fourier transform.
Now let’s run through the proof again with eF in place of F. For a > 0, set f(x) = e−ax2.
Applying eF to both sides of the equation f′(x) = −2axf(x), 2πiy( eFf)(y) = −2a
1
−(2πi)(Ff)′(y),
and that is equivalent to ( eFf)′(y) = −2π2
a y(Ff)(y). Solutions of g′(y) = −2π2
a yg(y) all look like
Ce−(π2/a)y2, so
f(x) = e−ax2 =⇒( eFf)(y) = Ce−(π2/a)y2
for a constant C. We want π2/a = π so that e−(π2/a)y2 = e−πy2 = f(y), which occurs for a = π.
Thus when f(x) = e−πx2 we have
(11.4)
( eFf)(y) = Ce−πy2 = Cf(y).
When y = 0 in (11.4), this becomes
R ∞
−∞e−πx2 dx = C, so C = K: see the top of the ﬁrst page for
the deﬁnition of K as the integral of e−πx2 over R.
Applying eF to both sides of (11.4) with C = K and using ( eF2f)(x) = f(−x), we get f(−x) =
K( eFf)(x) = K2f(x). At x = 0 this becomes 1 = K2, so K = 1 since K > 0. That K = 1, or
in more explicit form
R ∞
−∞e−πx2 dx = 1, is equivalent to the evaluation of the Gaussian integral I
with the change of variables y =
√
2πx in the integral for K.
12. History of the Gaussian integral
The function e−x2/2, more commonly written as
1
√
2πe−x2/2 (“normal distribution”) so it has total
integral 1 over R, plays an essential role in probability and statistics, and it was in such settings
that this function was initially found. Three separate investigations led to it.
(1) Large sample approximation to binomial: De Moivre [1, pp. 235-237] in 1733 found that a
large number of samples from a binomial distribution with p = 1/2 can be approximated by
a normal distribution. He did not write the Gaussian integral directly, but in [1, Cor. 2, p.
237] he estimated that the probability a binomial random variable with p = 1/2 is within a
standard deviation of the mean from above is .341344. This is
1
√
2π
R 1
0 e−x2/2 dx. Such a role
for the normal distribution did not make it stand out. De Moivre’s work was generalized by
Laplace in 1812 to binomial distributions with any p in (0, 1). The normal approximation
to the binomial for large sample sizes is a mainstay in probability and statistics courses.
(2) Distribution of Errors: Gauss in 1809 (based on work starting in 1801) was led to
a
√πe−a2x2
in his astronomical work on locating the lost asteroid Ceres by the method of least squares.
(At a = 1/
√
2 this is
1
√
2πe−x2/2.) To Gauss, such a function for suitable a describes the
distribution of errors in measurements: it is “the error curve”. The diﬃculty in ﬁnding
such a curve to model errors is hard to appreciate today, when the answer is known. In
the 1770s, for example, Laplace proposed other error curves with corners or asymptotes at
x = 0, as in Figure 4 below. In the second picture, a is the largest imagined error.
(3) Central Limit Theorem: Laplace, in his 1812 book Th´eorie analytique des probabilit´es [8],
developed the ﬁrst version of the Central Limit Theorem, which assigns a special role to
the normal distribution.
The discovery of normally distributed data in the social sciences by Quetelet and others in the
mid-19th century along with more general versions of the Central Limit Theorem solidiﬁed its role

<!-- page 13 -->
THE GAUSSIAN INTEGRAL
13
Figure 4. Laplace’s error curves: m
2 e−m|x| in 1774 and
1
2a log(a/|x|) when |x| ≤a in 1777.
from then on. See [18] for more details. In that era, it was called the “Law of Error” or “the Error
Curve”. The name Central Limit Theorem is due to George Polya in 1920,2 and the widespread
use of the name “normal distribution” is due to Karl Pearson.3
Appendix A. Redoing Section 2 without improper integrals in Fubini’s theorem
In this appendix we will work out the calculation of the Gaussian integral in Section 2 without
relying on Fubini’s theorem for improper integrals. The key equation is (2.1), which we recall:
Z ∞
0
Z ∞
0
ye−(t2+1)y2 dt

dy =
Z ∞
0
Z ∞
0
ye−(t2+1)y2 dy

dt.
The calculation in Section 2 that the iterated integral on the right is π/4 does not need Fubini’s
theorem in any form. It is going from the iterated integral on the left to π/4 that used Fubini’s
theorem for improper integrals. The next theorem could be used as a substitute, and its proof will
only use Fubini’s theorem for integrals on rectangles.
Theorem A.1. For b > 1 and c > 1,
Z ∞
0
Z ∞
0
ye−(t2+1)y2 dt

dy = π
4 + O
1
b

+ O
 1
√c

.
Having b →∞and c →∞in Theorem A.1 makes the right side π/4 without changing the left
side.
Lemma A.2.
(1) For all x ∈R, e−x2 ≤
1
x2 + 1.
(2) For a > 0
Z ∞
0
dx
a2x2 + 1 = π
2a.
(3) For a > 0 and c > 0,
Z ∞
c
dx
a2x2 + 1 = 1
a
π
2 −arctan(ac)

.
(4) For a > 0 and c > 0,
Z ∞
c
dx
a2x2 + 1 <
1
a2c.
(5) For a > 0, π
2 −arctan a < 1
a.
Proof. The proofs of (1), (2), and (3) are left to the reader. To prove (4), replace 1 + a2t2 by the
smaller value a2t2. To prove (5), write the diﬀerence as
R ∞
a dx/(x2 + 1) and then bound 1/(x2 + 1)
above by 1/x2.
□
2See https://mathoverflow.net/questions/44132.
3See https://mathshistory.st-andrews.ac.uk/Miller/mathword/n/.

<!-- page 14 -->
14
KEITH CONRAD
Now we prove Theorem A.1.
Proof. Step 1. For b > 1 and c > 1, we’ll show the improper integral can be truncated to an integral
over [0, b] × [0, c] plus error terms:
Z ∞
0
Z ∞
0
ye−(t2+1)y2 dt

dy =
Z b
0
Z c
0
ye−(t2+1)y2 dt

dy + O
 1
√c

+ O
1
b

.
Subtract the integral on the right from the integral on the left and split the outer integral
R ∞
0
into
R b
0 +
R ∞
b :
Z ∞
0
Z ∞
0
ye−(t2+1)y2 dt

dy −
Z b
0
Z c
0
ye−(t2+1)y2 dt

dy =
Z b
0
Z ∞
c
ye−(t2+1)y2 dt

dy
+
Z ∞
b
Z ∞
0
ye−(t2+1)y2 dt

dy.
On the right side, we will show the ﬁrst iterated integral is O(1/√c) and the second iterated integral
is O(1/b). The second iterated integral is simpler:
Z ∞
b
Z ∞
0
ye−(t2+1)y2 dt

dy =
Z ∞
b
Z ∞
0
e−(yt)2 dt

ye−y2 dy
≤
Z ∞
b
Z ∞
0
dt
y2t2 + 1

ye−y2 dy
by Lemma A.2(1)
=
Z ∞
b
π
2y ye−y2 dy
by Lemma A.2(2)
= π
2
Z ∞
b
e−y2 dy
≤π
2
Z ∞
b
dy
y2 + 1
by Lemma A.2(1)
= π
2b
since
1
y2 + 1 < 1
y2 ,
and this is O(1/b). Returning to the ﬁrst iterated integral,
Z b
0
Z ∞
c
ye−(t2+1)y2 dt

dy =
Z b
0
Z ∞
c
e−(yt)2 dt

ye−y2 dy
≤
Z b
0
Z ∞
c
dt
y2t2 + 1

ye−y2 dy
by Lemma A.2(1)
=
Z 1
0
Z ∞
c
dt
y2t2 + 1

ye−y2 dy +
Z b
1
Z ∞
c
dt
y2t2 + 1

ye−y2 dy
≤
Z 1
0
Z ∞
c
dt
y2t2 + 1

ye−y2 dy +
Z b
1
1
y2cye−y2 dy
by Lemma A.2(4)
=
Z 1
0
π
2 −arctan(yc)

e−y2 dy + 1
c
Z b
1
dy
yey2
by Lemma A.2(3)
≤
Z 1
0
π
2 −arctan(yc)

dy + 1
c
Z ∞
1
dy
yey2 .

<!-- page 15 -->
THE GAUSSIAN INTEGRAL
15
The last term is O(1/c). We will show the ﬁrst term is O(1/√c) by carefully splitting up
R 1
0 .
For 0 < ε < 1,
Z 1
0
π
2 −arctan(yc)

dy =
Z ε
0
π
2 −arctan(yc)

dy +
Z 1
ε
π
2 −arctan(yc)

dy.
Both integrals are positive, and the ﬁrst one is less than (π/2)ε. The integrand of the second
integral is less than 1/(yc) by Lemma A.2(5), so
Z 1
ε
π
2 −arctan(yc)

dy <
Z 1
ε
dy
yc < 1 −ε
εc
< 1
εc.
Therefore
0 <
Z 1
0
π
2 −arctan(yc)

dy < π
2 ε + 1
εc
for each ε in (0, 1). Use ε = 1/√c to get
0 <
Z 1
0
π
2 −arctan(yc)

dy <
π
2√c + 1
√c = O
 1
√c

.
That proves the ﬁrst iterated integral is O(1/√c) + O(1/c) = O(1/√c) as c →∞.
Step 2. For b > 0 and c > 0, we will show
Z b
0
Z c
0
ye−(t2+1)y2 dt

dy = π
4 + O
 1
eb2

+ O
1
c

.
By Fubini’s theorem for continuous functions on a rectangle in R2,
Z b
0
Z c
0
ye−(t2+1)y2 dt

dy =
Z c
0
Z b
0
ye−(t2+1)y2 dy

dt.
For the inner integral on the right, the formula
R b
0 ye−ay2 dy = 1/(2a) −1/(2aeab2) for a > 0 tells
us
Z b
0
ye−(t2+1)y2 dy =
1
2(t2 + 1) −
1
2(t2 + 1)e(t2+1)b2 ,
so
Z c
0
Z b
0
ye−(t2+1)y2 dy

dt = 1
2
Z c
0
dt
t2 + 1 −1
2
Z c
0
dt
(t2 + 1)e(t2+1)b2
= 1
2 arctan(c) −1
2
Z c
0
dt
(t2 + 1)e(t2+1)b2 .
(A.1)
Let’s estimate these last two terms. Since
arctan(c) =
Z ∞
0
dt
t2 + 1 −
Z ∞
c
dt
t2 + 1 = π
2 + O
Z ∞
c
dt
t2

= π
2 + O
1
c

and
Z c
0
dt
(t2 + 1)e(t2+1)b2 ≤
Z c
0
dt
t2 + 1
1
eb2 ≤
Z ∞
0
dt
t2 + 1
1
eb2 = O
 1
eb2

,
feeding these error estimates into (A.1) ﬁnishes Step 2.
□

<!-- page 16 -->
16
KEITH CONRAD
References
[1] A. De Moivre, The Doctrine of Chances, 2nd ed., Woodfall, London, 1738. https://archive.org/details/bim
eighteenth-century the-doctrine-of-chances moivre-abraham-de 1738.
[2] D. Bell, “Poisson’s remarkable calculation – a method or a trick?” Elem. Math. 65 (2010), 29–36.
[3] C. A. Berenstein and R. Gay, Complex Variables, Springer-Verlag, New York, 1991.
[4] A. L. Delgado, “A Calculation of
Z ∞
0
e−x2 dx,” The College Math. J. 34 (2003), 321–323.
[5] H. Iwasawa, “Gaussian Integral Puzzle,” Math. Intelligencer 31 (2009), 38–41.
[6] T. P. Jameson, “The Probability Integral by Volume of Revolution,” Mathematical Gazette 78 (1994), 339–340.
[7] H. Kneser, Funktionentheorie, Vandenhoeck and Ruprecht, 1958.
[8] P. S. Laplace, Th´eorie Analytique des Probabilit´es, Courcier, 1812.
[9] P. S. Laplace, “M´emoire sur la probabilit´e des causes par les ´ev`enemens,” Oeuvres Compl´etes 8, 27–65. (English
trans. by S. Stigler as “Memoir on the Probability of Causes of Events,” Statistical Science 1 (1986), 364–378.)
[10] P. M. Lee, http://www.york.ac.uk/depts/maths/histstat/normal history.pdf.
[11] L. Mirsky, The Probability Integral, Math. Gazette 33 (1949), 279. URL http://www.jstor.org/stable/
3611303.
[12] C. P. Nicholas and R. C. Yates, “The Probability Integral,” Amer. Math. Monthly 57 (1950), 412–413.
[13] G. Polya, “Remarks on Computing the Probability Integral in One and Two Dimensions,” pp. 63–78 in Berkeley
Symp. on Math. Statist. and Prob., Univ. California Press, 1949.
[14] R. Remmert, Theory of Complex Functions, Springer-Verlag, 1991.
[15] M. Rozman, “Evaluate Gaussian integral using diﬀerentiation under the integral sign,” Course notes for Physics
2400 (UConn), Spring 2016.
[16] W. Rudin, Principles of Mathematical Analysis, 3rd ed., McGraw-Hill, 1976.
[17] M. Spivak, Calculus, W. A. Benjamin, 1967.
[18] S. Stahl, “The Evolution of the Normal Distribution,” Math. Mag. 79 (2006), 96–113. URL https://www.jstor.
org/stable/27642916.
[19] S. Stigler, “Laplace’s 1774 Memoir on Inverse Probability,” Statistical Science 1 (1986), 359–363.
[20] J. van Yzeren, “Moivre’s and Fresnel’s Integrals by Simple Integration,” Amer. Math. Monthly 86 (1979),
690–693.
[21] G. N. Watson, Complex Integration and Cauchy’s Theorem, Cambridge Univ. Press, Cambridge, 1914.
[22] http://gowers.wordpress.com/2007/10/04/when-are-two-proofs-essentially-the-same/#comment-239.
[23] http://math.stackexchange.com/questions/34767/int-infty-infty-e-x2-dx-with-complex-analysis.
[24] http://math.stackexchange.com/questions/390850/integrating-int-infty-0-e-x2-dx-using-feynmans-
parametrization-trick

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*