# Differential Equations and Linear Algebra

> **Source**: https://kconrad.math.uconn.edu/blurbs/diffeqdim.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA
KEITH CONRAD
1. Introduction
We develop some results about linear diﬀerential equations with constant coeﬃcients
using linear algebra. Our concern is not cookbook methods to ﬁnd all the solutions to a
diﬀerential equation, but the computation of the dimension of the solution space.
Consider a homogeneous linear diﬀerential equation with constant (real) coeﬃcients:
(1.1)
y(n) + an−1y(n−1) + · · · + a1y′ + a0y = 0.
The “homogeneous” label means if y ﬁts the equation then so does cy for all constants c.
(If the right side were a nonzero function then cy would no longer be a solution and (1.1)
is then called “inhomogeneous.”) The “linear” part refers to the linear operator
(1.2)
Dn + an−1Dn−1 + · · · + a1D + a0I,
where D = d/dt is the basic diﬀerentiation operator on functions. (The j-th derivative
operator, for j ≥1, is Dj, and we consider the identity operator I as D0, since it is
standard to regard the zero-th derivative of a function as the function itself: D0(y) = y for
all functions y.) We call (1.2) an n-th order linear diﬀerential operator since the highest
derivative appearing in it is the n-th derivative. We want to show the solution space to
(1.1) is n-dimensional.
2. Passage to the Complex Case
A solution to (1.1) has to have at least n derivatives for the equation to make sense.
Then, by using (1.1) to write y(n) in terms of lower-order derivatives of y, induction shows
every solution to (1.1) has to be inﬁnitely diﬀerentiable. Let C∞(R) be the space of all
functions R →R that are inﬁnitely diﬀerentiable. This is an inﬁnite-dimensional vector
space, and it is this space in which we search for solutions of (1.1) because every solution
to (1.1) must be in here.
Let
(2.1)
p(t) = tn + an−1tn−1 + · · · + a1t + a0
be the polynomial having the coeﬃcients from (1.1).
Example 2.1. If y′′ −2y′ −3y = 0 then p(t) = t2 −2t −3.
The equation (1.1) can be written in the condensed form
p(D)(y) = 0.
That is, solutions y to (1.1) form the kernel of the diﬀerential operator p(D) on C∞(R).
This viewpoint, that solutions to a diﬀerential equation are the kernel of a linear operator
on C∞(R), is the link between diﬀerential equations and linear algebra. Warning: There
are many nonlinear diﬀerential equations, like y′′ = yy′ + y3, and the methods of linear
1

<!-- page 2 -->
2
KEITH CONRAD
algebra are not suﬃcient for their study. In particular, solutions to a nonlinear diﬀerential
equation do not form a vector space (e.g., the sum of two solutions is not a solution in
general).
When the polynomial p(t) factors, the operator p(D) factors in a similar way: if
(2.2)
p(t) = (t −c1) · · · (t −cn),
then
(2.3)
p(D) = (D −c1I) · · · (D −cnI).
Here D −cI is the operator sending y to y′ −cy.
Example 2.2. The polynomial p(t) = t2 −2t −3 factors as (t + 1)(t −3) and p(D) =
(D + I)(D −3I):
(D + I)(D −3I)(y) = (D + I)(y′ −3y)
= (y′ −3y)′ + (y′ −3y)
= y′′ −2y′ −3y
= p(D)(y).
Equation (2.3) expresses p(D) as a composite of ﬁrst-order diﬀerential operators D −
cjI. This decomposition of p(D) will reduce the study of n-th order constant-coeﬃcient
diﬀerential equations to the study of ﬁrst-order constant-coeﬃcient diﬀerential equations
by a clever use of linear algebra on an inﬁnite-dimensional space.
Real polynomials do not always factor into linear factors with real coeﬃcients, but the
fundamental theorem of algebra tells us that complex polynomials always factor into linear
factors with complex coeﬃcients (so, in particular, real polynomials always factor into
linear factors with complex coeﬃcients). Therefore we generalize our point of view and
consider equations like (1.1) with complex coeﬃcients in order to have the factorization (2.3)
available. For example, if y′′+y = 0 then (D2+I)(y) = 0 and the corresponding polynomial
is t2 + 1, which factors as (t + i)(t −i). We want to regard y′′ + y as (D + iI)(D −iI)(y),
and a meaning has to be given to D + iI and D −iI.
When we allow complex coeﬃcients in (1.1), we should no longer restrict solutions y to
real-valued functions. For instance, the diﬀerential equation y′ −iy = 0 has the interesting
complex solution y(t) = cos t+i sin t, while the only real-valued solution of y′ −iy = 0 is the
zero function y(t) = 0. Even if we only started out caring about real-valued solutions with
real coeﬃcients in (1.1), factoring p(t) into complex linear factors forces the complex case
on us for mathematical reasons. From now on, we consider (1.1) with complex coeﬃcients.
Let C∞(R, C) be the set of inﬁnitely-diﬀerentiable functions f : R →C. The domain
is still R; only the range has been enlarged. From now on D = d/dt is the diﬀerentiation
operator on C∞(R, C): if f(t) = g(t) + ih(t), where g(t) and h(t) are real-valued, then
f′(t) = g′(t) + ih′(t). Diﬀerentiation on complex-valued functions f : R →C satisﬁes the
sum rule and the product rule. Moreover, if f has derivative 0 then f is constant (since
g and h have derivative 0, so they are constant from real calculus). Every complex-valued
solution to (1.1) has at least n derivatives, and by induction all solutions are in fact inﬁnitely
diﬀerentiable just as in the real case, so solutions to (1.1) lie in C∞(R, C). Equation (2.2)
implies (2.3) when the roots cj are complex.
For c ∈R, the real solutions to the diﬀerential equation y′ = cy are the real scalar
multiples of ect. A similar result holds if c ∈C:

<!-- page 3 -->
DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA
3
Theorem 2.3. For c ∈C, the solutions to y′ = cy are the functions y(t) = rect for r ∈C.
Proof. Since (ect)′ = cect, every function y = rect satisﬁes y′ = cy. Conversely, suppose y′ =
cy. Then the ratio y/ect has derivative (ecty′ −y(ect)′)/(ect)2 = (ectcy −ycect)/(ect)2 = 0,
so y/ect is a constant. Call the constant r, so y = rect.
□
The equation y′ = cy is the same as y′ −cy = 0, so D −cI on C∞(R, C) has a one-
dimensional kernel with ect as a basis:
ker(D −cI) = Cect.
For example, the solution space of y′ = y is Cet and not just Ret. For other diﬀeren-
tial equations like y′ = iy, with honest complex coeﬃcients, there may be no real-valued
solutions besides the zero function while there are nonzero complex solutions.
Our study of (1.1) currently stands as follows. Solutions to (1.1), which lie in C∞(R, C),
form the kernel of the diﬀerential operator p(D). By the fundamental theorem of algebra
and (2.3), p(D) factors into a product of ﬁrst-order operators. We know the kernel of the
ﬁrst-order diﬀerential operator D −cI: it is one-dimensional with basis ect.
Our goal is to prove, roughly, that the complex solution space to (1.1) has dimension
n over C. In down-to-earth terms, this means there are n “basic” solutions to (1.1) in
C∞(R, C) such that the general solution is a linear combination of these n basic solutions
and none of these n basic solutions is a linear combination of the other basic solutions.
In linear algebra terms, this means an n-th order constant-coeﬃcient linear diﬀerential
operator p(D) has an n-dimensional kernel in C∞(R, C). While this second description
sounds more technical, it is the right way to think about the solutions of (1.1) in order to
reach our goal. (Our goal does not include the explicit description of all solutions to (1.1).
All we want to do is compute the dimension of the solution space.)
3. The Complex Case
To bootstrap our knowledge from the ﬁrst-order diﬀerential operators D −cI to the n-th
order diﬀerential operators p(D), we will use the following property of the operators D−cI.
Lemma 3.1. For each c ∈C, D −cI is onto. That is, for every f ∈C∞(R, C), there is a
u ∈C∞(R, C) such that u′ −cu = f.
Proof. First, we check the special case c = 0, which says for every f there is a u such that
u′ = f. This is just a matter of antidiﬀerentiating real and imaginary parts. Indeed, write
f(t) = a(t) + ib(t) and choose antiderivatives for a(t) and b(t), say A(t) =
R t
0 a(x) dx and
B(t) =
R t
0 b(x) dx. Then u(t) = A(t) + iB(t) has derivative a(t) + ib(t) = f(t), Since f(t) is
inﬁnitely diﬀerentiable and u′ = f, so is u. We’re done with the case c = 0.
Now we show each D −cI is onto, i.e., the diﬀerential equation u′ −cu = f, where f is
given, has a solution u in C∞(R, C). The strategy is to reduce to the previously treated
case c = 0 by a “change of coordinates.” Multiply through the equation by e−ct (which is
an invertible procedure, since ect is a nonvanishing function):
e−ctu′ −ce−ctu = e−ctf.
By the product rule, this equation is the same as
(e−ctu)′ = e−ctf.
This equation has the form v′ = g, where g = e−ctf is given and v is sought. That is the
case treated in the previous paragraph: pick antiderivatives for the real and imaginary parts

<!-- page 4 -->
4
KEITH CONRAD
of g(t) to get an antiderivative v(t) for g(t), and then multiply v(t) by ectto ﬁnd a solution
u.
□
Lemma 3.1 tells us the ﬁrst-order inhomogeneous diﬀerential equation u′ −cu = f can
always be solved when f ∈C∞(R, C).
The next lemma has nothing to do with diﬀerential equations. It is only about linear
algebra.
Lemma 3.2. Let V be a vector space over a ﬁeld F. Let T : V →V and U : V →V be
linear operators on V such that ker(T) and ker(U) are ﬁnite-dimensional. Assume U is
onto. Then ker(TU) is ﬁnite-dimensional and
dim ker(TU) = dim ker(T) + dim ker(U).
This lemma is tricky because your ﬁrst guess about how to prove it does not work: it is
not the case that a basis of ker(T) and a basis of ker(U) combine to give a basis of ker(TU).
For instance, let T and U both be D = d/dt on C∞(R, C) (or even on C∞(R), if you want
to work in a more familiar setting). Both ker(T) and ker(U) consist of constant functions,
but the kernel of TU = D2 = d2/dt2 has basis {1, t}, so it is not spanned by constant
functions.
Proof. This proof might at ﬁrst appear overly technical. If you need motivation to care
about the proof, see below how this lemma is applied to diﬀerential equations. Then come
back and read the proof.
Write m = dim ker(T) and n = dim ker(U). We want to prove dim ker(TU) = m + n.
Notice we do not even know yet that ker(TU) is ﬁnite-dimensional. First we will prove
ker(TU) is ﬁnite-dimensional, with a spanning set of m + n vectors, so dim ker(TU) ≤
m + n. Then we will prove the spanning set we ﬁnd for ker(TU) is linearly independent, so
dim ker(TU) = m + n.
Let v1, . . . , vm be a basis of ker(T) and w1, . . . , wn be a basis of ker(U).
For v ∈ker(TU), the equation (TU)(v) = 0 says T(Uv) = 0, so Uv is in the kernel of T:
Uv = c1v1 + · · · + cmvm
for some c1, . . . , cm ∈F.
To get anywhere with this equation, we use the hypothesis that U is onto to write the
vi’s in another way. Since U : V →V is onto, we can write vi = U(evi) for some evi in V .
Then the above equation becomes
Uv = c1U(ev1) + · · · + cmU(evm)
= U(c1ev1 + · · · + cmevm).
When U takes the same value at two vectors, the diﬀerence of those vectors is in the kernel
of U (just subtract and compute). Therefore
(3.1)
v = c1ev1 + · · · + cmevm + v′,
where v′ ∈ker(U). Writing v′ in terms of the basis w1, . . . , wn of ker(U) and feeding this
into (3.1), we have
v = c1ev1 + · · · + cmevm + d1w1 + · · · + dnwn
for some d1, . . . , dn ∈F.

<!-- page 5 -->
DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA
5
We have written a general element v of ker(TU) as a linear combination of m+n vectors:
the evi’s and the wj’s. Moreover, the evi’s and wj’s are in ker(TU):
(TU)(evi) = T(Uevi) = T(vi) = 0,
(TU)(wj) = T(Uwj) = T(0) = 0.
Since we have shown the evi’s and wj’s are a spanning set for ker(TU), this kernel has
dimension at most m + n.
To prove ev1, . . . , evm, w1, . . . , wn is a linearly independent set, suppose some F-linear com-
bination is 0:
(3.2)
c1ev1 + · · · + cmevm + d1w1 + · · · + dnwn = 0.
Applying U to this equation turns each evi into U(evi) = vi and turns each wj into U(wj) = 0,
so we ﬁnd
c1v1 + · · · + cmvm = 0.
The vi’s are (by their deﬁnition) linearly independent, so each ci is 0. This turns (3.2) into
d1w1 + · · · + dnwn = 0.
Now, since the wj’s are (by their deﬁnition) linearly independent, each dj is 0. Thus the
set {ev1, . . . , evm, w1, . . . , wn} spans ker(TU) and is linearly independent, so ker(TU) has
dimension m + n.
□
Remark 3.3. If V is ﬁnite-dimensional, there is another proof of Lemma 3.2, using the
rank-nullity theorem. However, we will not discuss this alternate proof for ﬁnite-dimensional
V because Lemma 3.2 for ﬁnite-dimensional V is useless for our intended application to
diﬀerential equations: the basic space of interest, C∞(R, C), is not ﬁnite-dimensional. This
is a good reason that linear algebra must not be developed exclusively on ﬁnite-dimensional
vector spaces: important applications of the ideas of linear algebra occur in contexts where
the spaces are inﬁnite-dimensional. This is especially true in applications of linear algebra
to analysis (diﬀerential equations, integral equations, Fourier series) and physics (quantum
mechanics).
There is a version of Lemma 3.2 even if U is not onto. However, a new idea has to be
introduced, the notion of the index of a linear operator. Lemma 3.2 generalizes to: the index
of a product of operators is the sum of the indices. You can read about this in textbooks
on functional analysis (speciﬁcally, look up Fredholm operators).
Now we are ready to prove our goal: the dimension of the solution space of (1.1) is n.
The proof is deceptively short. All the hard work has gone into the preliminary results.
Theorem 3.4. Let p(t) be a polynomial of the form (2.1) with complex coeﬃcients of
degree n ≥1 and let p(D) be the corresponding n-th order linear diﬀerential operator with
constant coeﬃcients. The solution space to p(D)(y) = 0 in C∞(R, C) is n-dimensional, or
equivalently ker(p(D)) has dimension n.
Proof. We induct on n, the degree of the polynomial p(t). The case n = 1 says: for c ∈C,
the operator D −cI on C∞(R, C) has a one-dimensional kernel. That is, the equation
y′ −cy = 0 has a one-dimensional solution space. We saw this before by explicit methods:
the solution space is Cect and has dimension 1.
Now assume the theorem is proved whenever p(t) has degree n. Let p(t) have degree
n + 1. We will prove ker(p(D)) has dimension n + 1.
By the fundamental theorem of algebra,
p(t) = (t −c1)(t −c2) · · · (t −cn)(t −cn+1)

<!-- page 6 -->
6
KEITH CONRAD
for some complex numbers c1, . . . , cn+1. (Some of the cj’s may be equal, but that doesn’t
matter for our purposes.) Set q(t) = (t −c1) · · · (t −cn), so p(t) = q(t)(t −cn+1). Therefore
p(D) = q(D)(D −cn+1I).
By the inductive hypothesis, ker(q(D)) has dimension n. By the base case, ker(D −cn+1I)
has dimension 1.
We now apply Lemma 3.2, taking V = C∞(R, C), T = q(D) and U = D −cn+1I. The
hypothesis in Lemma 3.2 that U is onto is true by Lemma 3.1. Thus, Lemma 3.2 tells us
p(D) has a ﬁnite-dimensional kernel, with
dimC(p(D)) = dimC(q(D)) + dimC(D −cn+1I) = n + 1.
We’re done!
□
This a rather curious state of aﬀairs. We have computed the size (i.e., the dimension)
of the complex solution space to each constant-coeﬃcient linear diﬀerential equation of the
form (1.1), but we have not indicated what the solutions are when n > 1! A careful rereading
will show the proofs of Lemmas 3.1 and 3.2 are constructive, so the proof of Theorem 3.4
really can be used to list a basis for the solution space of (1.1) when we factor p(t). We will
now see in some examples how to follow the method of proof of Lemma 3.2 to build a basis
of ker(TU) from bases of ker(T) and ker(U).
Example 3.5. Consider y′′−2y′−3y = 0. The polynomial is p(t) = t2−2t−3 = (t+1)(t−3).
Take T = D + I and U = D −3I, so p(D) = TU. A basis of ker(T) is e−t and a basis
of ker(U) is e3t. As in the proof of Lemma 3.2, we write e−t = U(ev) = ev′ −3ev and want
to solve for ev. First try ev = e−t: (e−t)′ −3(e−t) = 2e−t. This didn’t work, but if we scale
and instead use ev = (1/2)e−t then it works. So a basis of ker(p(D)) is {e3t, (1/2)e−t}, and
by scaling another basis is {e3t, e−t}. The general solution to y′′ −2y′ −3y = 0 is a linear
combination of e3t and e−t.
Example 3.6. Consider y′′ −2y′ + y = 0. The polynomial is p(t) = t2 −2t + 1 = (t −1)2,
which has 1 as a double root. Take T = D −I and U = D −I, so p(D) = TU. A basis of
ker(T) = ker(U) is et. Writing et = U(ev) = ev′ −ev, the function ev = tet works (check!) and
therefore a basis of ker(p(D)) is {et, tet}.
Example 3.7. Consider y′′ + y = 0. The polynomial is p(t) = t2 + 1 = (t + i)(t −i).
Take T = D + iI and U = D −iI, so p(D) = TU.
A basis of ker(T) is e−it and a
basis of ker(U) is eit. Writing e−it = U(ev) = ev′ −iev, we ﬁrst try ev = e−it. However,
(e−it)′ −i(e−it) = −2ie−it ̸= e−it. If we scale and use ev = −(1/2i)e−it then it works. Thus
a basis of ker(TU) is {eit, −(1/2i)e−it}, and by scaling again another basis is {eit, e−it}.
Another basis obtained from this one is {(eit +e−it)/2, (eit −e−it)/2i} = {cos t, sin t}, which
looks more familiar as the basic real solution of y′′+y = 0. The general solution to y′′+y = 0
is a linear combination of cos t and sin t.
Remark 3.8. A general constant-coeﬃcient linear diﬀerential operator could have a co-
eﬃcient an ̸= 1 in front of Dn. Since scaling a linear diﬀerential operator by a nonzero
constant (like 1/an) does not change the kernel or the order of the diﬀerential operator,
and makes the coeﬃcient of Dn equal to 1, our treatment of the “special” case an = 1 was
more or less a treatment of the general case.

<!-- page 7 -->
DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA
7
4. The Real Case
If the diﬀerential equation (1.1) has real coeﬃcients, we are naturally interested in the
real solutions, not all complex solutions. The above examples suggest that the complex
solution space will have a basis of real-valued functions (although in the last example we
had to work a little to ﬁnd it), so one may hope that the real solution space has dimension
n. This is true:
Theorem 4.1. Let p(t) be a polynomial with real coeﬃcients of degree n ≥1 and let p(D)
be the corresponding n-th order linear diﬀerential operator with constant coeﬃcients. The
solution space to p(D)(y) = 0 in C∞(R) is n-dimensional.
The basic idea behind Theorem 4.1 is that under fairly general circumstances a “real”
linear operator acting on a complex vector space has a real kernel of the same dimension
(over R) as the dimension of its complex kernel (over C).
For example, a diﬀerential
operator with real coeﬃcients sends real functions to other real functions, so it should be
considered a “real” operator. An example of a diﬀerential operator that is not “real” is
D −iI, which sends y(t) to y′(t) −iy(t). Real functions don’t get sent to real functions by
this operator (in general), and the diﬀerential equation y′ −iy = 0 has complex solution
space Ceit of dimension 1 over C and real solution space {0} of dimension 0 over R. So
the two dimensions don’t match!
To determine the dimension of the real solution space from the dimension of the complex
solution space requires another detour back through linear algebra. We temporarily forget
about diﬀerential equations and will return to them after Lemma 4.8 below.
Let V be a vector space over the complex numbers. We can consider V as a real vector
space by considering scaling by real numbers only. For instance, the complex scalar multiple
(2 + 3i)v is viewed as 2v + 3(iv), which is a real linear combination of v and iv.
Lemma 4.2. A complex vector space V is ﬁnite dimensional over C if and only if it is ﬁnite
dimensional over R, in which case dimR(V ) = 2 dimC(V ). More precisely, if V ̸= {0} and
{v1, . . . , vn} is a C-basis of V , then
(4.1)
{v1, iv1, v2, iv2, . . . , vn, ivn}
is an R-basis of V .
Proof. The result is clear if V is 0, so take V nonzero.
If V is ﬁnite dimensional over R then a ﬁnite basis of V as a real vector space is a
spanning set of V as a complex vector space, so V is ﬁnite dimensional over C.
Conversely, suppose V is ﬁnite dimensional over C with basis {v1, . . . , vn}. We will show
the set in (4.1) is a basis of V as a vector space over R, so dimR(V ) = 2n.
Spanning set: Each v ∈V is a C-linear combination of {v1, v2, . . . , vn}, say
v = (a1 + b1i)v1 + (a2 + b2i)v2 + · · · + (an + bni)vn
for some complex numbers aj + ibj. Distributing the scalar multiplication,
v = a1v1 + b1(iv1) + a2v2 + b2(iv2) + · · · + anvn + bn(ivn).
This exhibits v as a real linear combination of {v1, iv1, . . . , vn, ivn}, so this set is a spanning
set of V over R.
Linear Independence: Suppose in V that
c1v1 + c′
1(iv1) + c2v2 + c′
2(iv2) + · · · + cnvn + c′
n(ivn) = 0

<!-- page 8 -->
8
KEITH CONRAD
for real cj and c′
j. We want to show each cj and c′
j is 0. Rewrite the equation as
(c1 + ic′
1)v1 + (c2 + ic′
2)v2 + · · · + (cn + ic′
n)vn = 0.
Since {v1, . . . , vn} are linearly independent over C, each cj + ic′
j is 0. Therefore each cj and
c′
j is 0 because a complex number is 0 only when its real and imaginary parts are 0.
□
Deﬁnition 4.3. Let V be a vector space over C. A conjugation on V is an operation
V →V , denoted v 7→v∗, with the following three properties:
• For all v1, v2 ∈V , (v1 + v2)∗= v∗
1 + v∗
2.
• For all v ∈V and z ∈C, (zv)∗= zv∗(not zv∗).
• For all v ∈V , (v∗)∗= v.
In the following examples, you will see that a conjugation on a concrete complex vector
space is typically just the operation of taking the complex conjugate of the coordinates
(when the vector space is deﬁned through a device like coordinates).
Example 4.4. Take V = Cn. For v = (z1, . . . , zn) in Cn, set v∗= (z1, . . . , zn). That is,
v∗is just the vector with coordinates that are complex conjugates of the coordinates of v.
Example 4.5. Take V = Mn(C). For A = (aij) in Mn(C), set A∗= (aij). That is, A∗is
the matrix with components that are complex conjugates of those for A.
Example 4.6. A second conjugation on Mn(C) is (aij)∗= (aji). Here A∗is the conjugate
of the transposed matrix.
Example 4.7. Take V = C∞(R, C). For y(t) = a(t) + ib(t) ∈C∞(R, C), let y∗be the
function y∗(t) = y(t) = a(t)−ib(t). For example, if f(t) = sin t+iet, then f∗(t) = sin t−iet.
When V is a complex vector space with a conjugation operation, set
V + = {v ∈V : v∗= v}.
Here is what this means in the above examples. When V = Cn, V + is the set of n-tuples
whose coordinates are real, so V + = Rn. When V = Mn(C) in Example 4.5, V + is the
set of n × n matrices with real entries: V + = Mn(R). When V = Mn(C) in Example
4.6, V + is the set of matrices (aij) such that aji = aij. These are the complex matrices
whose diagonal terms are real and whose components symmetric across the main diagonal
are complex conjugates of each other. (Examples 4.5 and 4.6 remind us that the meaning
of V + depends on the speciﬁc conjugation used on V .) Finally, when V = C∞(R, C), V +
is the set of functions y(t) = a(t) + ib(t) such that b(t) = 0. That is, V + = C∞(R).
Notice V + is not a complex vector space since V + is not closed under complex scaling.
For instance, in Example 4.4, Rn is not a complex subspace of Cn. (In general, for all
nonzero v ∈V +, iv is not in V + since (iv)∗= iv∗= −iv is not iv again.) However, V + is
a subspace of V as a real vector space. For instance, Rn is a subspace of Cn when we view
Cn as a real vector space.
Lemma 4.8. Suppose V is a vector space over C and has a conjugation deﬁned on it. Then
V is ﬁnite-dimensional over C if and only if V + is ﬁnite-dimensional over R, and when
the spaces are ﬁnite dimensional each R-basis of V + is a C-basis of V . In other words,
dimR(V +) = dimC(V ).
Don’t confuse the conclusions of Lemmas 4.2 and 4.8. Consider V = C with conjugation
z 7→z: it has real dimension 2 and V + = R has real dimension 1.

<!-- page 9 -->
DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA
9
Proof. First suppose dimC(V ) is ﬁnite. Then if we view V as a real vector space, it is
ﬁnite-dimensional with dimR(V ) = 2 dimC(V ) by Lemma 4.2. Since V + is a subspace of V
as a real vector space, it follows that V + is a ﬁnite-dimensional real vector space.
Conversely, suppose dimR(V +) is ﬁnite and v1, . . . , vn is a basis of V + over R. We will
prove v1, . . . , vn is a basis of V over C.
First we treat linear independence over C. Suppose
(4.2)
c1v1 + · · · + cnvn = 0,
where cj = aj + ibj. Applying the conjugation operation,
c1v∗
1 + · · · + cnv∗
n = 0.
Since each vj is in V +, v∗
j = vj, so the above equation becomes
(4.3)
c1v1 + · · · + cnvn = 0.
Write cj = aj + ibj (aj, bj ∈R). Adding (4.2) and (4.3) kills oﬀthe imaginary parts of the
cj’s, and leaves us with
2a1v1 + · · · + 2anvn = 0.
Since the vj’s are linearly independent over R, each aj is 0. Similarly, subtracting (4.3)
from (4.2) gives
i2b1v1 + · · · + i2bnvn = 0.
Dividing by i converts this into a real linear combination of the vj’s equal to 0, and therefore
each bj is 0. That proves cj = aj + ibj is 0 for j = 1, 2, . . . , n, which settles the linear
independence.
Now we want to show {v1, . . . , vn} spans V over the complex numbers. Choose v ∈V .
We want to ﬁnd complex c1, . . . , cn such that
v = c1v1 + · · · + cnvn.
To show this can be done, notice that the conjugation operation on V is R-linear (but not
C-linear) and satisﬁes (v∗)∗= v, so we can write
v = w1 + iw2,
where w∗
1 = w1 and w∗
2 = w2. Concretely, w1 = (1/2)(v + v∗) and w2 = (1/2i)(v −v∗).
(This is like the formulas for the real and imaginary parts of a complex number z = x + iy:
x = (1/2)(z + z) and y = (1/2i)(z −z).) Thus, w1 and w2 are in V +. Using the basis
v1, . . . , vn of V +,
w1 = a1v1 + · · · + anvn,
w2 = b1v1 + · · · + bnvn,
where aj, bj ∈R. Thus,
v = w1 + iw2
= (a1v1 + · · · + anvn) + i(b1v1 + · · · + bnvn)
= (a1 + ib1)v1 + · · · + (an + ibn)vn,
so each v ∈V is a C-linear combination of the vj’s. That shows the vj’s span V over C.
□
Finally we are ready to prove Theorem 4.1.

<!-- page 10 -->
10
KEITH CONRAD
Proof. Let p(D) be a constant-coeﬃcient linear diﬀerential operator of order n with real
coeﬃcients. We want to show the real solution space to p(D)(y) = 0, which is a real vector
space, has dimension n over R.
Let V be the complex solution space to p(D)(y) = 0 in C∞(R, C). Therefore V has
dimension n as a complex vector space, by Theorem 3.4.
Write p(D) = Dn + an−1Dn−1 + · · · + a1D + a0I, with real aj. Then the diﬀerential
equation p(D)(y) = 0, when written out in full, is (1.1). When y satisﬁes (1.1), so does
the conjugate function y. Indeed, y(j) = y(j) and aj = aj, so conjugating the diﬀerential
equation shows y satisﬁes the diﬀerential equation. (This is false if the aj are not all real,
e.g., solutions to y′ −iy = 0 are usually not again solutions to the same equation after
conjugation.)
Since conjugates of complex solutions to p(D)(y) = 0 are again solutions, we can apply
Lemma 4.8 to V = C∞(R, C) with its conjugation operation: it tells us the subset V + is
an n-dimensional real vector space. Since y = y if and only if y is in C∞(R), V + is the
real solution space to p(D)(y) = 0, so we have proved the real solution space to (1.1) is
n-dimensional (over R).
□
Theorem 4.1 is a good example of the beneﬁts of ﬁrst working over C. Even if we are
only interested in real solutions of real diﬀerential equations, the way that one computes
the dimension of the real solution space is to ﬁrst prove a corresponding result for complex
solutions (as a complex vector space) and then use that to determine the dimension of the
real solution space.
5. Equations With Initial Conditions
Now that we have existence of solutions, we can prove uniqueness of solutions given
enough initial conditions. We will consider as initial conditions a speciﬁcation of the values
y(0), y′(0), . . . , y(n−1)(0). These are n pieces of information.
Lemma 5.1. If y satisﬁes (1.1) and y(j)(0) = 0 for 0 ≤j ≤n −1 then y(t) = 0 for all t.
Proof. We argue by induction on the order of the diﬀerential equation. When n = 1, the
equation is y′ + ay = 0, whose general solution is y(t) = re−at for some constant r. So if
y(0) = 0 then r = 0 and y(t) = 0 for all t.
Now suppose n ≥2 and the lemma is proved for constant-coeﬃcient linear diﬀerential
equations of order n −1. Write (1.1) as p(D)(y) = 0 and split oﬀone linear factor from the
polynomial p(t): p(t) = q(t)(t−c), where q(t) has degree n−1. Then p(D) = q(D)(D−cI),
so p(D)(y) = q(D)(D −cI)(y) = q(D)(y′ −cy). The diﬀerential equation (1.1) now looks
like
q(D)(y′ −cy) = 0,
which may look more complicated, but it really helps because it tells us that y′ −cy is the
solution of a diﬀerential equation of order n−1 (since q(D) is a diﬀerential operator of order
n−1). Moreover, for 0 ≤j ≤n−2 we have (y′−cy)(j)(0) = y(j+1)(0)−cy(j)(0) = 0−c·0 = 0.
(We needed j ≤n −2 so j + 1 ≤n −1 and therefore y(j+1)(0) = 0. So y′ −cy has its
derivatives at 0 through order n −2 equal to 0, hence by induction y′ −cy is the zero
function. Now by the base case we get from this that y(t) is the zero function.
□
Theorem 5.2. For every b0, b1, . . . , bn−1 ∈C, there is a unique solution to (1.1) satisfying
y(j)(0) = cj for 0 ≤j ≤n −1.

<!-- page 11 -->
DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA
11
Proof. First we check uniqueness, and then existence.
Uniqueness. If y and z are two solutions to (1.1) satisfying the same initial conditions,
then the diﬀerence y −z is a solution whose initial conditions are all 0, so by Lemma 5.1
we have y(t) −z(t) = 0 for all t, hence y and z are the same function.
Existence. Consider the linear map that turns a solution of (1.1) into its initial conditions:
y(t) 7→(y(0), y′(0), . . . , y(n−1)(0)) ∈Cn. This is a C-linear transformation from the n-
dimensional solution space to Cn. Lemma 5.1 tells us the transformation has kernel 0, so it
is injective. Both the solution space and Cn have the same dimension, so injectivity implies
surjectivity. That’s a fancy way of saying any given set of initial conditions is satisﬁed by
some solution of (1.1). So we’re done.
□
This treatment of linear diﬀerential equations has only covered equations with (real)
constant coeﬃcients. The coeﬃcients of a linear diﬀerential equation could be functions:
(5.1)
y(n) + an−1(t)y(n−1) + · · · + a1(t)y′ + a0(t)y = 0.
A particular example is
y′′ + (t2 −t)y′ −(sin t)y = 0.
Even if the coeﬃcients are varying with t, this diﬀerential equation is still linear in y:
solutions to such a diﬀerential equation form a vector space under addition and scaling: the
real solutions form a real vector space and the complex solutions form a complex vector
space. When the coeﬃcients aj(t) are continuous functions I →R on an open interval
I in R, the complex solution space is n-dimensional over C and the real solution space
is n-dimensional over R. (By Lemma 4.8, these dimension calculations for the real and
complex solution spaces are equivalent.)
Our proof of the dimension calculation in the constant-coeﬃcient case does not apply to
the case of non-constant coeﬃcients (why?), so analyzing (5.1) requires ideas from analysis
such as ﬁxed-point theorems. This result is found in many general treatments of diﬀerential
equations. It is usually called a global existence and uniqueness theorem for (5.1) subject
to initial conditions on y and its ﬁrst n −1 derivatives: y(t0) = c0, y′(t0) = c1, y′′(t0) =
c2, . . . , y(n−1)(t0) = cn−1, where t0 ∈I. That is, there is exactly one solution y(t) satisfying
(5.1) together with those initial conditions at t0, and this solution is deﬁned for all t ∈I.
The reason this implies the solution space of (5.1) is n-dimensional (for real or complex
solutions) is that the collection of n initial conditions (read each row separately)
y(t0) = 1, y′(t0) = 0, y′′(t0) = 0, . . . , y(n−1)(t0) = 0,
y(t0) = 0, y′(t0) = 1, y′′(t0) = 0, . . . , y(n−1)(t0) = 0,
...
y(t0) = 0, y′(t0) = 0, y′′(t0) = 0, . . . , y(n−1)(t0) = 1
leads to n solutions y0(t), y1(t), . . . , yn−1(t) of (5.1), and an arbitrary set of initial conditions
(5.2)
y(t0) = c0, y′(t0) = c1, y′′(t0) = c2, . . . , y(n−1)(t0) = cn−1
is satisﬁed by c0y0(t) + c1y1(t) + · · · + cn−1yn−1(t), so the uniqueness for solutions of (5.1)
implies the only solution satisfying (5.2) is c0y0(t) + c1y1(t) + · · · + cn−1yn−1(t). Therefore
y0(t), . . . , yn−1(t) form a basis of the solution space of (5.1).

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*