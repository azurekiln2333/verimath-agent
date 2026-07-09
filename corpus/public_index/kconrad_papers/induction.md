# Examples of Proofs by Induction

> **Source**: https://kconrad.math.uconn.edu/blurbs/induction.pdf  
> **Author**: Keith Conrad  
> **Topic**: proof_writing  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
EXAMPLES OF PROOFS BY INDUCTION
KEITH CONRAD
1. Introduction
Mathematical induction is a method that allows us to prove inﬁnitely many similar
statements in a systematic way, by organizing them all in a deﬁnite order and showing
• the ﬁrst statement is correct (“base case”)
• if a particular but unspeciﬁed statement in the list is correct (“inductive hypothe-
sis”), then the statement after it in the list is correct (“inductive step”).
This implies all statements in the list are correct. It is not circular reasoning, but “spiraling
reasoning”. An analogy to falling dominos is common, but dominos are not inﬁnitely long.
The most basic results that are proved by induction are summation identities, such as
(1.1)
1 + 2 + 3 + · · · + n = n(n + 1)
2
for all integers n ≥1. View this identity as a separate statement for each n: S(1), S(2), S(3),
and so on, where S(n) is the (as yet unproved) statement in (1.1). At n = 1, each side of
(1.1) is 1, so S(1) is true. Next, if S(n) is true for some n ≥1, then to show S(n + 1) is
true we write 1 + 2 + · · · + n + (n + 1) in terms of 1 + 2 + · · · + n and use the truth of S(n):
1 + 2 + · · · + n + (n + 1) = (1 + 2 + · · · + n) + (n + 1)
= n(n + 1)
2
+ (n + 1)
since S(n) is assumed to be true
= n(n + 1) + 2(n + 1)
2
= (n + 1)(n + 2)
2
.
Equality of the ﬁrst and last expressions here is exactly what it means for S(n + 1) to be
true. We proved S(1) is true and proved for each n ≥1 that if S(n) is true, then S(n+1) is
true. Thus all of S(1), S(2), S(3), . . . are true, which proves (1.1) for all n ≥1. Understand
that we really did something. It’s not just “simplifying a formula” or voodoo magic!
Another way to prove the inductive step (for n ≥1, if S(n) is true then S(n + 1) is true)
is to add n + 1 to both sides of (1.1):
1 + 2 + · · · + n = n(n + 1)
2
=⇒1 + 2 + · · · + n + (n + 1) = n(n + 1)
2
+ (n + 1)
=⇒1 + 2 + · · · + n + (n + 1) = n(n + 1) + 2(n + 1)
2
=⇒1 + 2 + · · · + n + (n + 1) = (n + 1)(n + 2)
2
.
Advice. Proofs by induction may not be about algebraic identities, but they are always
about proving inﬁnitely many statements recursively. Know what those statements are each
1

<!-- page 2 -->
2
KEITH CONRAD
time! In the inductive step, earlier cases must help us derive the next case, but we don’t
always turn each case into the next case or start with the inductive hypothesis. There is no
single path through inductive proofs: the “next step” may need creativity.
We will meet proofs by induction involving linear algebra, polynomial algebra, calculus,
and exponents. In each proof, ﬁnd the statement depending on a positive integer. Check
how, in the inductive step, the inductive hypothesis is used. Some results below are about
all integers (positive, negative, and 0) so that you can see induction in that type of setting.
2. Linear Algebra
Theorem 2.1. For n × n matrices A and M, where M is invertible, (MAM−1)k =
MAkM−1 for all integers k ≥0.
If A is invertible, then that equation is true for all
integers k.
Proof. We argue by induction on the exponent k (not on n, the size of the matrix).
The equation (MAM−1)k = MAkM−1 is clear for k = 0: both sides are the n×n identity
matrix I. For k = 1, the equation (MAM−1)k = MAkM−1 says MAM−1 = MAM−1,
which is true. Here is a proof of k = 2:
(MAM−1)2 = (MAM−1)(MAM−1)
= MA(M−1M)AM−1
= MAIAM−1
= MAAM−1
= MA2M−1.
Now assume (MAM−1)k = MAkM−1 for some exponent k ≥1. Then
(MAM−1)k+1 = (MAM−1)k(MAM−1)
= (MAkM−1)(MAM−1)
by the inductive hypothesis
= MAk(M−1M)AM−1
= MAkIAM−1
= MAkAM−1
= MAk+1M−1,
which proves the inductive step. So the base case k = 1 is true for all A and M, and if the
k-th case is true for all A and M, then the (k + 1)-th case is true for all A and M. Thus
(MAM−1)k = MAkM−1 for all integers k ≥0 and all A and M.
When A is invertible, let’s prove (MAM−1)k = MAkM−1 for all k < 0. Set k = −K, so
K ≥1. We won’t use induction again with negative k, but simply calculate both sides to
see they’re equal by reducing ourselves to the case of positive exponents, which has already
been proved (by induction). Note: for all invertible B, B−K = (B−1)K for all K ≥1.
The matrices MA−1M and MAM−1 are inverses:
(MAM−1)(MA−1M−1) = MA(M−1M)A−1M−1 = MAA−1M−1 = MM−1 = I.
So (MAM−1)−1 = MA−1M−1. That tells us
(2.1)
(MAM−1)k = (MAM−1)−K = ((MAM−1)−1)K = (MA−1M−1)K.

<!-- page 3 -->
EXAMPLES OF PROOFS BY INDUCTION
3
The proved case of positive exponents tells us (MA−1M−1)K = M(A−1)KM−1 by replacing
A with A−1. Feeding that into (2.1),
(2.2)
(MAM−1)k = M(A−1)KM−1
Since Ak = A−K = (A−1)K, (2.2) becomes (MAM−1)k = MAkM−1, which is what we
wanted, so we’re done.
□
Theorem 2.2. Let A be a square matrix. Eigenvectors for A having distinct eigenvalues
are linearly independent: if v1, . . . , vr are eigenvectors for A, with Avi = λivi for distinct
scalars λ1, . . . , λr, then v1, . . . , vr are linearly independent.
Proof. We induct on r, the number of eigenvectors. The result is true if r = 1: eigenvectors
are not 0 and a single nonzero vector is linearly independent. Suppose r > 1 and the result
has been veriﬁed for all sets of fewer than r eigenvectors of A (with distinct eigenvalues).
Given r eigenvectors vi of A with distinct eigenvalues λi, suppose
(2.3)
c1v1 + c2v2 + · · · + crvr = 0
for some scalars ci. We want to prove each ci is 0.
Applying A to both sides of (2.3), we get
(2.4)
c1λ1v1 + c2λ2v2 + · · · + crλrvr = 0.
Now multiply through (2.3) by λ1:
(2.5)
c1λ1v1 + c2λ1v2 + · · · + crλ1vr = 0.
Subtracting (2.5) from (2.4) eliminates the ﬁrst term:
(2.6)
c2(λ2 −λ1)v2 + · · · + cr(λr −λ1)vr = 0.
By the inductive hypothesis, the r −1 eigenvectors v2, . . . , vr are linearly independent.
Therefore (2.6) tells us that ci(λi −λ1) = 0 for i = 2, 3, . . . , r. Since the eigenvalues are
distinct, λi −λ1 ̸= 0, so ci = 0 for i = 2, 3, . . . , r. Feeding this into (2.3) gives us c1v1 = 0,
so c1 = 0 as well since v1 ̸= 0. Thus every ci is 0.
□
3. Polynomial algebra
Theorem 3.1. Let f(x) be a nonconstant polynomial with real coeﬃcients and degree d.
Then f(x) has at most d real roots.
We can’t replace “at most d real roots” with “exactly d real roots” since there are
nonconstant real polynomials like x2 + 1 that have no real roots.
Proof. We induct on the degree d of f(x). Each step in the induction is about inﬁnitely
many polynomials: the theorem in degree 1, then in degree 2, then in degree 3, and so on.
The base case has d = 1. A polynomial of degree 1 with real coeﬃcients is of the form
f(x) = ax + b, where a and b are real and a ̸= 0. This has exactly one root, namely −b/a,
and thus at most one real root. That settles the theorem for d = 1.
Now assume the theorem is true for all polynomials of degree d with real coeﬃcients. We
will prove the theorem is true for all polynomials of degree d + 1 with real coeﬃcients.
A typical polynomial of degree d + 1 with real coeﬃcients is
(3.1)
f(x) = cd+1xd+1 + cdxd + · · · + c1x + c0,

<!-- page 4 -->
4
KEITH CONRAD
where cj ∈R and cd+1 ̸= 0. If f(x) has no real roots, then we’re done, since 0 ≤d + 1. If
f(x) has a real root, say r, then
(3.2)
0 = cd+1rd+1 + cdrd + · · · + c1r + c0.
Subtracting (3.2) from (3.1), the constant terms c0 cancel and we get
(3.3)
f(x) = cd+1(xd+1 −rd+1) + cd(xd −rd) + · · · + c1(x −r).
Each diﬀerence xj −rj for j = 1, 2, . . . , d + 1 has x −r as a factor:
xj −rj = (x −r)(xj−1 + rxj−2 + · · · + rixj−1−i + · · · + rj−2x + rj−1).
Write the more complicated second factor, a polynomial of degree j −1, as Qj,r(x). So
(3.4)
xj −rj = (x −r)Qj,r(x),
and substituting (3.4) into (3.3) gives
f(x)
=
d+1
X
j=1
cj(x −r)Qj,r(x)
=
(x −r)
d+1
X
j=1
cjQj,r(x)
=
(x −r)(cd+1
|{z}
̸=0
degree d
z
}|
{
Qd+1,r(x) + · · · + c1Q1,r(x)
|
{z
}
lower degree
).
(3.5)
Since cd+1Qd+1,r(x) is a polynomial of degree d, and each lower degree polynomial does not
decrease the degree when added to cd+1Qd+1,r(x), the second factor in (3.5) has degree d.
Each root of f(x) is either r or a root of the second factor in (3.5). Each Qj,r(x) has real
coeﬃcients and all cj are real, so the second factor in (3.5) has real coeﬃcients. We can
therefore apply the inductive hypothesis to the second factor and conclude that the second
factor in (3.5) has at most d real roots, so f(x) has at most d+1 real roots. As f(x) was an
arbitrary polynomial of degree d+1 with real coeﬃcients, we have shown that the d-th case
of the theorem being true implies the (d + 1)-th case is true. By induction on the degree,
the theorem is true for all nonconstant polynomials.
□
Our next two theorems use the truth of some earlier case to prove the next case, but
not necessarily the truth of the immediately previous case to prove the next case. This
approach is called the “strong” form of induction.
Theorem 3.2. Every nonconstant polynomial has an irreducible factor.
Recall that a nonconstant polynomial is called irreducible when its only factors are con-
stants and constant multiples of itself. For example, x is irreducible. It has factorizations
like 2(x/2) and 5(x/5), but those are trivial since one of the factors is constant. Warning:
a polynomial with no roots doesn’t have to be irreducible! Consider (x2 + 1)(x2 + 2).
Proof. We induct on the degree d of the nonconstant polynomial.
When d = 1, the polynomial is linear. Linear polynomials are irreducible, so the case
d = 1 is settled.

<!-- page 5 -->
EXAMPLES OF PROOFS BY INDUCTION
5
Assuming every nonconstant polynomial with degree ≤d has an irreducible factor, con-
sider a polynomial f(x) with degree d+1. If f(x) is irreducible, then f(x) has an irreducible
factor (namely itself). If f(x) is not irreducible, then we can factor f(x) into nonconstant
parts, say f(x) = g(x)h(x) where 1 ≤deg g(x), deg h(x) < d+1. By our (strong) inductive
assumption, g(x) has an irreducible factor, and this irreducible polynomial will also be a
factor of f(x) since g(x) is a factor of f(x). Thus f(x) has an irreducible factor and we are
done.
□
Theorem 3.3. Every nonconstant polynomial is a product of irreducible polynomials.
We include here the convention that an irreducible polynomial is considered to be a 1-
term product of irreducible polynomials. For example, x2+1 is irreducible and it is a 1-term
product of irreducibles.
Proof. We induct on the degree d of the nonconstant polynomial.
When d = 1, the polynomial is linear. Linear polynomials are irreducible, so the case
d = 1 is settled.
Assume every nonconstant polynomial with degree ≤d is a product of irreducible poly-
nomials. We want to prove every polynomial with degree d + 1 is a product of irreducible
polynomials. Let f(x) be a polynomial with degree d + 1. Either f(x) is irreducible or
it is not.
If f(x) is irreducible, then it is a 1-term product of irreducible polynomials.
(namely itself). If f(x) is not irreducible, then we can factor f(x) into nonconstant parts,
say f(x) = g(x)h(x) where 1 ≤deg g(x), deg h(x) < d + 1. By our (strong) inductive
assumption, g(x) and h(x) are each products of irreducible polynomials:
g(x) = p1(x) · · · pr(x),
h(x) = q1(x) · · · qs(x),
where pi(x) and qj(x) are irreducible polynomials. Then
f(x) = g(x)h(x) = p1(x) · · · pr(x)q1(x) · · · qs(x),
so f(x) is a product of irreducible polynomials.
□
While this last proof by induction shows every nonconstant polynomial has an irreducible
factorization, it does not tell us how to ﬁnd it! For example, it is not obvious how to write
x5 + 2x4 −2x2 −x + 1
as an explicit product of irreducible polynomials.
4. Calculus
A calculus analogue of proving summation identities by induction is proving derivative
identities by induction. Here is an example.
Theorem 4.1. For n ≥1, dn
dxn (ex2) = Pn(x)ex2, where Pn(x) is a polynomial of degree n.
Before working out the proof, let’s see how we could guess such a result by doing calcu-
lations for small n:
(1) The ﬁrst derivative of ex2 is 2xex2.
(2) The second derivative of ex2 is (2xex2)′, which is (4x2 + 2)ex2 by the product rule.
(3) The third derivative of ex2 is ((4x2 +2)ex2)′, which is (8x3 +12x)ex2 by the product
rule again.

<!-- page 6 -->
6
KEITH CONRAD
Each time we are getting a polynomial times ex2, and the degree of the polynomial matches
the order of the derivative. So the formulation of Theorem 4.1 is not a surprise based on
the initial examples. (They also suggest proving that Pn(x) has leading coeﬃcient 2n.)
Proof. We argue by induction on n.
Our base case is n = 0. The zeroth derivative of a function is the function itself, so
we want to know ex2 is P0(x)ex2 for a polynomial P0(x) of degree 0. This is true using
P0(x) = 1. Let’s check n = 1. The ﬁrst derivative (ex2)′ is 2xex2, so this is P1(x)ex2 for the
polynomial P1(x) = 2x, which has degree 1.
Now we do the inductive step. For n ≥1, assume
(4.1)
(ex2)(n) = Pn(x)ex2
for some polynomial Pn(x) of degree n. To compute (ex2)(n+1), we diﬀerentiate both sides
of (4.1) and obtain
(ex2)(n+1) = (Pn(x)ex2)′
by the inductive hypothesis
= Pn(x)(ex2)′ + ex2P ′
n(x)
by the product rule
= Pn(x)(2xex2) + P ′
n(x)ex2
= (2xPn(x) + P ′
n(x))ex2.
The ﬁrst factor here is 2xPn(x) + P ′
n(x). Since Pn(x) has degree n, 2xPn(x) has degree
n + 1 while P ′
n(x) has degree n −1. When you add polynomials with diﬀerent degrees, the
degree of the sum is the larger of the two degrees (in fact, the whole leading term of the
sum is the leading term of the larger degree polynomial). Therefore, setting Pn+1(x) :=
2xPn(x)+P ′
n(x), we have (ex2)(n+1) = Pn+1(x)ex2, where Pn+1(x) is a polynomial of degree
n + 1. That settles the inductive step and completes the proof.
□
This is not an interesting illustration of induction because the proof of the inductive step
is too routine (“diﬀerentiate both sides,” which is analogous to “adding something to both
sides” in the proof of a summation identity). Most uses of induction in calculus proofs are
not a matter of diﬀerentiating both sides of an identity. Here is an example.
Theorem 4.2. For all sets of diﬀerentiable functions f1(x), . . . , fn(x) where n ≥2,
(f1(x) · · · fn(x))′
f1(x) · · · fn(x)
= f′
1(x)
f1(x) + · · · + f′
n(x)
fn(x).
Proof. We induct on n, the number of functions.
The base case is n = 2 and it follows from the product rule
(f1(x)f2(x))′ = f′
1(x)f2(x) + f1(x)f′
2(x)
by dividing both sides by f1(x)f2(x):
(f1(x)f2(x))′
f1(x)f2(x)
= f′
1(x)f2(x) + f1(x)f′
2(x)
f1(x)f2(x)
= f′
1(x)
f1(x) + f′
2(x)
f2(x).
Now assume the result is true for all sets of n diﬀerentiable functions for some n ≥2. To
prove the result for all sets of n + 1 diﬀerentiable functions f1(x), . . . , fn+1(x), write their
product either as a product of two functions or as a product of n functions by collecting
some factors into a single function:
(4.2)
f1(x)f2(x) · · · fn+1(x) = (f1(x)f2(x) · · · fn(x)) · fn+1(x)

<!-- page 7 -->
EXAMPLES OF PROOFS BY INDUCTION
7
is a product of the two functions f1(x)f2(x) · · · fn(x) and fn+1(x), while
(4.3)
f1(x)f2(x) · · · fn+1(x) = (f1(x)f2(x))f3(x) · · · fn+1(x)
is a product of the n functions f1(x)f2(x), f3(x), . . . , fn+1(x).
Both (4.2) and (4.3) lead to separate approaches to the inductive step: use the base
case (all sets of 2 diﬀerentiable functions) and then the inductive hypothesis (all sets of n
diﬀerentiable functions) or use the inductive hypothesis and then the base case. For the
ﬁrst method, write
(f1(x) · · · fn+1(x))′
f1(x) · · · fn+1(x)
= ((f1(x) · · · fn(x)) · fn+1(x))′
(f1(x) · · · fn(x)) · fn+1(x)
= (f1(x) · · · fn(x))′
f1(x) · · · fn(x)
+ f′
n+1(x)
fn+1(x)
by the base case
= f′
1(x)
f1(x) + · · · + f′
n(x)
fn(x) + f′
n+1(x)
fn+1(x)
by the inductive hypothesis
and this is what we needed to show for n + 1 functions. For the second method, write
(f1(x) · · · fn+1(x))′
f1(x) · · · fn+1(x)
= ((f1(x)f2(x))f3(x) · · · fn+1(x))′
(f1(x)f2(x))f3(x) · · · fn+1(x)
= (f1(x)f2(x))′
f1(x)f2(x)
+ f′
3(x)
f3(x) + · · · + f′
n+1(x)
fn+1(x)
by the ind. hypothesis
= f′
1(x)
f1(x) + f′
2(x)
f2(x) + f′
3(x)
f3(x) + · · · + f′
n+1(x)
fn+1(x)
by the base case.
□
Remark 4.3. In the appendix we prove a second theorem by induction on the number of
terms.
Theorem 4.4. For x > 0 and integers n ≥0, ex > 1 + x + x2
2! + · · · + xn
n! .
This inequality is clear without induction, using the power series expansion for ex: ex =
P
k≥0 xk/k! for all real x, and when x > 0 the terms in the sum are all positive so we can
drop all the terms of the series past the nth term and the inequality of Theorem 4.4 drops
out. So why prove Theorem 4.4 by induction if we can prove the theorem quickly using
power series? Just to illustrate techniques!
Proof. We will prove the inequality by induction on n.
The base case n = 0 says: ex > 1 for x > 0. This is true since ex is an increasing function,
so ex > e0 = 1 when x is positive.
Now we make our inductive hypothesis:
(4.4)
ex > 1 + x + x2
2! + · · · + xn
n!
for all x > 0. We will derive the same inequality with n + 1 in place of n (for all x > 0).
We will actually give two diﬀerent approaches to the inductive step: the ﬁrst will use
integrals and the second will use derivatives. These approaches are logically independent of
each other and can be read in either order.
The Integral Approach: When f(x) > g(x) on an interval [a, b], their integrals over the
interval have the same inequality:
R b
a f(x) dx >
R b
a g(x) dx. This is also true if the functions

<!-- page 8 -->
8
KEITH CONRAD
are equal at an endpoint but otherwise satisfy f(x) > g(x). (We have in mind here only
continuous functions.)
We are going to apply this idea to the inequality (4.4). Our inductive hypothesis is that
(4.4) holds for every x > 0, but at x = 0 we get equality in (4.4) since both sides become
1. Therefore we can integrate both sides of (4.4) over every interval [0, t] where t > 0:
Z t
0
ex dx >
Z t
0

1 + x + x2
2! + · · · + xn
n!

dx.
Evaluating both sides,
et −1 > t + t2
2! + t3
3! + · · · +
tn+1
(n + 1)!.
Now add 1 to both sides and we have
et > 1 + t + t2
2! + t3
3! + · · · +
tn+1
(n + 1)!.
This has been derived for every t > 0, so we can now simply rename t as x and we have
completed the inductive step.
The Derivative Approach: The key idea we will use with derivatives is that a function
having a positive derivative on an interval is increasing on this interval. In particular, if
g(x) is diﬀerentiable for x ≥0 and g′(x) > 0 for x > 0 then g(x) > g(0) for x > 0. Make
sure you understand this idea before reading further.
We are assuming (4.4) holds for some n and all x > 0, and we want to use this to derive
the analogue of (4.4) for the next exponent n + 1: for all x > 0,
(4.5)
ex ?> 1 + x + x2
2! + · · · +
xn+1
(n + 1)!.
Well, let F(x) be the diﬀerence of the two sides of (4.5):
F(x) = ex −

1 + x + x2
2! + · · · + xn
n! +
xn+1
(n + 1)!

.
Our goal is to show F(x) > 0 if x > 0. Consider the derivative
F ′(x) = ex −

0 + 1 + x + · · · +
xn−1
(n −1)! + xn
n!

.
Our induction hypothesis (4.4) is exactly the statement that F ′(x) is positive for x > 0.
Therefore by our induction hypothesis F(x) is an increasing function for x ≥0, so F(x) >
F(0) when x > 0. Since F(0) = 0, we obtain F(x) > 0 for all x > 0, which completes the
inductive step using this second approach.
□
Notice how the inductive hypothesis was used in the two approaches to the inductive
step. In the integral approach, we integrated the inequality in the inductive hypothesis to
derive the inequality for the next exponent. In the derivative approach, on the other hand,
we did not start with the inductive hypothesis and “do something to both sides.” Instead,
we set up a convenient function F(x) related to what we wanted to show and used the
inductive hypothesis to tell us something relevant about the derivative of that function.
The following corollary of Theorem 4.4 is important: it says ex grows faster than every
ﬁxed integral power of x.

<!-- page 9 -->
EXAMPLES OF PROOFS BY INDUCTION
9
Corollary 4.5. For every integer n ≥0, ex
xn →∞and xn
ex →0 as x →∞.
Proof. Since ex/xn > 0 when x > 0, saying ex/xn →∞and xn/ex →0 are the same thing.
We will prove the ﬁrst version, that ex/xn →∞as x →∞. By Theorem 4.4,
ex > 1 + x + x2
2! + · · · + xn
n! +
xn+1
(n + 1)!
when x > 0. (Why did we use the inequality out to degree n + 1 instead of degree n? Read
on and you’ll see.) In particular, since all lower degree terms on the right side are positive
when x > 0,
ex >
xn+1
(n + 1)!
when x > 0. Divide both sides of this inequality by xn:
ex
xn >
x
(n + 1)!.
Here n is ﬁxed and x is an arbitrary positive real number. In this inequality, the right side
tends to ∞as x →∞. Therefore ex/xn →∞as x →∞. (We did not use induction in this
proof.)
□
From Corollary 4.5 we draw two further conclusions.
Corollary 4.6. For every polynomial p(x), p(x)
ex
→0 as x →∞.
Proof. By Corollary 4.5, xn/ex →0 as x →∞. Every polynomial is a sum of multiples of
such ratios: writing p(x) = adxd + ad−1xd−1 + · · · + a1x + a0, we have
p(x)
ex
= ad
xd
ex + ad−1
xd−1
ex
+ · · · + a1
x
ex + a0
1
ex .
Each xn/ex appearing here tends to 0 as x →∞, so p(x)/ex tends to 0 as x →∞.
□
Corollary 4.7. For every integer n ≥0, (log x)n
x
→0 as x →∞,
Proof. Set y = log x, so x = ey and (log x)n/x = yn/ey. We want to show yn/ey →0 as
x →∞. As x →∞, also y →∞. Therefore by Corollary 4.5, ey/yn →∞as x →∞, so
yn/ey →0 as x →∞.
□
Theorem 4.8. For n ≥0,
Z ∞
0
xne−x dx = n!.
Proof. We argue by induction on n. For n = 0,
Z ∞
0
e−x dx = −e−x

∞
0
= lim
b→∞−e−x

b
0
= lim
b→∞−e−b + 1 = 0 + 1 = 1.

<!-- page 10 -->
10
KEITH CONRAD
For n ≥1, we express
R ∞
0 xne−x dx in terms of
R ∞
0 xn−1e−x dx using integration by parts:
Z ∞
0
xne−x dx =
Z ∞
0
u dv
(u = xn, dv = e−x dx)
= uv

∞
0
−
Z ∞
0
v du
(du = nxn−1 dx, v = −e−x)
= −xn
ex

∞
0
+ n
Z ∞
0
xn−1e−x dx
= (0 −0) + n · (n −1)!
by Corollary 4.5 and the ind. hypothesis
= n!.
□
Theorem 4.9. The function ex is not “algebraic”: for no n ≥1 and polynomials c0(x),
c1(x), . . . , cn(x) that are not all identically zero can we have
(4.6)
cn(x)enx + cn−1(x)e(n−1)x + · · · + c1(x)ex + c0(x) = 0
for all x ∈R. In other words, if such a functional identity does hold then all the polynomial
coeﬃcients ck(x) are the zero polynomial.
The left side of (4.6) is a “polynomial in ex with polynomial coeﬃcients,” which can be
thought of as
(4.7)
cn(x)yn + cn−1(x)yn−1 + · · · + c1(x)y + c0(x)
where we have substituted ex for y. Since the ck(x)’s are polynomials in x, (4.7) is a two-
variable polynomial in x and y. The theorem is saying no two-variable polynomial P(x, y)
can have ex as a “root” in y. By comparison, the function x1/3 is a “root” of the two-variable
polynomial Q(x, y) = y3 −x: when we substitute x1/3 in for y, the result Q(x, x1/3) is the
zero function.
Proof. We argue by induction on n. Corollary 4.6 will play a role!
The base case is n = 1. Suppose
(4.8)
c1(x)ex + c0(x) = 0
for all x and some polynomials c0(x) and c1(x). We want to show c0(x) and c1(x) are both
the zero polynomial. Dividing by ex and re-arranging, we have
c1(x) = −c0(x)
ex
for all x. We now think about what this tells us as x →∞. The right side tends to 0 by
Corollary 4.6. This forces c1(x) to be the zero polynomial, since a non-zero polynomial does
not tend to 0 as x →∞: a non-zero constant polynomial keeps its constant value while a
non-constant polynomial tends to ±∞(depending on the sign of the leading coeﬃcient).
Now that we know c1(x) is identically zero, our original equation (4.8) becomes c0(x) = 0
for all x. This concludes the base case.
For the inductive step, assume for some n ≥1 that the only way to satisfy (4.6) for all x
is to have all coeﬃcients ck(x) equal to the zero polynomial. Then suppose there are n + 1
polynomials a0(x), . . . , an+1(x) such that
(4.9)
an+1(x)e(n+1)x + an(x)enx + · · · + a1(x)ex + a0(x) = 0
for all x. We want to show every ak(x) is the zero polynomial.

<!-- page 11 -->
EXAMPLES OF PROOFS BY INDUCTION
11
As in the base case, we divide this equation by an exponential, but now take it to be
e(n+1)x instead of ex:
an+1(x) + an(x)
ex
+ · · · + a1(x)
enx
+ a0(x)
e(n+1)x = 0.
Moving all but the ﬁrst term to the other side,
(4.10)
an+1(x) = −an(x)
ex
−· · · −a1(x)
enx
−a0(x)
e(n+1)x
for all x.
What happens in (4.10) when x →∞?
On the right, −an(x)/ex →0 by Corollary
4.6. Other terms have the form −ak(x)/e(n+1−k)x for k = 0, 1, . . . , n −1. Writing this as
−(ak(x)/ex)(1/e(n−k)x), it tends to 0 · 0 = 0 by Corollary 4.6 (since n −k > 0). Therefore
the right side of (4.10) tends to 0 as x →∞, so the polynomial an+1(x) must be the zero
polynomial (same argument as in the base case). This means the left-most term in (4.9)
disappears, so (4.9) becomes
an(x)enx + · · · + a1(x)ex + a0(x) = 0
for all x. This is a relation of degree n in ex, so by the inductive hypothesis (at last!) all
of its polynomial coeﬃcients are the zero polynomial. Therefore all the coeﬃcients of (4.9)
are the zero polynomial, which completes the inductive step.
□
Remark 4.10. Since the values of x that mattered in the limits are large values (we took
x →∞), we could have incorporated this into the statement of the theorem and obtained
a (slightly) stronger result: if there are polynomials c0(x), . . . , cn(x) such that
cn(x)enx + cn−1(x)e(n−1)x + · · · + c1(x)ex + c0(x) = 0
just for suﬃciently large x, then every ck(x) is the zero polynomial. The argument proceeds
exactly as before except we replace “for all x” by “for all suﬃciently large x” in each
occurrence. The logical structure of the argument is otherwise unchanged.
5. Integral exponents
Every nonzero real number a has a reciprocal 1/a = a−1. The integral powers an for
n ∈Z are deﬁned as follows:
• Recursively, a1 = a and an = an−1a for n ≥2 (or concretely, an = a · · · a
| {z }
n times
if n ≥1),
• a0 = 1,
• an = (a−1)|n| for n ≤−1 (e.g., a−3 = a−1a−1a−1).
In words, the speciﬁc powers a1 = a and a−1 = 1/a are deﬁned ﬁrst, the remaining nonzero
powers of a are repeated products of a1 or a−1, and a0 = 1.
To illustrate the use of induction on formulas with two parameters, we will prove the
following equations for all a ̸= 0 and arbitrary m and n in Z:
aman = am+n and (am)n = amn.
Theorem 5.1. For all a ̸= 0 and all integers m and n, aman = am+n.
Proof. We will ﬁrst prove this for arbitrary m ∈Z and all n ≥1, and then handle the
remaining cases (arbitrary m ∈Z and all n ≤0) by often reducing to the case where n ≥1.
First we will prove by induction on n ≥1 that for all a ̸= 0 and all m ∈Z, aman = am+n.
Call that statement S(n).

<!-- page 12 -->
12
KEITH CONRAD
Base case n = 1. Since an = a1 = a by deﬁnition, the desired equation aman ?= am+n for
all m ∈Z says when n = 1 that ama ?= am+1 for all m ∈Z. Let’s break this into separate
parts depending on the sign of m.
• If m ≥1, then the recursive deﬁnition of powers of a says am+1 = am+1−1a = ama.
• If m = 0, then ama = a0a = 1 · a = a and am+1 = a1 = a.
• If m = −1, then ama = a−1a = 1 and am+1 = a0 = 1.
• If m ≤−2, then set m = −M with M ≥2, so ama = a−Ma = (a−1)Ma =
(a−1)M−1a−1a = (a−1)M−1 = a−(M−1) = a−M+1 = am+1.
Inductive step. Assume for all a ̸= 0 and all m ∈Z that aman = am+n for some n ≥1.
We want to show for all a ̸= 0 and all m ∈Z that aman+1 = am+n+1. The term an+1 is
ana by the recursive deﬁnition of positive powers of a, so
aman+1 = am(ana) = (aman)a = am+na,
where the last equation comes from the inductive hypothesis, and am+na = am+n+1 by the
base case above using exponent m + n in the role of m (an arbitrary integer).
We have now proved by induction on n ≥1 that
(5.1)
aman = am+n for all a ̸= 0, all m ∈Z, and all n ≥1.
It remains to prove aman = am+n for all a ̸= 0, m ∈Z, and all n ≤0.
n = 0. Both sides of aman ?= am+n when n = 0 become am since a0 = 1, so the equation
is true in this case.
n < 0. Write n = −N, so N ∈Z+ and aman
?= am+n is the same as ama−N
?= am−N,
which is equivalent to am(a−1)N
?= am−N by the deﬁnition of negative exponents. The
validity of this equation would be unaﬀected by multiplying both sides by aN, so
(5.2)
am(a−1)N
?= am−N ⇐⇒am(a−1)NaN
?= am−NaN,
and on the right side am−NaN = a(m−N)+N = am by (5.1) with the exponents m and n there
replaced by m −N ∈Z and N ≥1. Thus we are reduced to proving am(a−1)NaN
?= am
for all N ≥1. This looks obvious since the product (a−1)NaN ought to be 1, but we did
not show that yet. To prove (a−1)NaN = 1 for all nonzero a and all N ≥1 we will use
induction on N.
For the base case N = 1, (a−1)NaN = (a−1)a = 1. For the inductive step, if (a−1)NaN =
1 for an N ≥1, then to obtain the same equation with N + 1 in the exponents,
(5.3)
(a−1)N+1aN+1 = (a−1)Na−1aN+1
by the recursive deﬁnition of positive powers of a−1. Write aN+1 as a1+N. By (5.1) with
m = 1 and n = N, a1+N = aaN. That turns (5.3) into
(a−1)N+1aN+1 = (a−1)Na−1aaN = (a−1)NaN
because a−1a = 1. We have (a−1)NaN = 1 by the inductive hypothesis, so (a−1)N+1aN+1 =
(a−1)NaN = 1. This ends the inductive step. We have shown (a−1)NaN = 1 for all N ≥1.
Returning to (5.2), we saw am−NaN = am using (5.1), and now we know am(a−1)NaN is
am · 1 = am, so we proved aman = am+n for all a ̸= 0, all m ∈Z, and all n < 0.
□
Theorem 5.2. For all a ̸= 0 and all integers m and n, (am)n = amn.

<!-- page 13 -->
EXAMPLES OF PROOFS BY INDUCTION
13
Proof. First we will treat the case n ≥1. Let S(n) be the statement for all a ̸= 0 and all
m ∈Z, (am)n = amn. We will prove S(n) is true for all n ≥1 by induction on n and then
treat the case n ≤0.
Base case n = 1.
Since everything to the power 1 is itself by deﬁnition, the desired
equation (am)n ?= amn when n = 1 says am ?= am, which is true.
Inductive step. Assume for all a ̸= 0 and all m ∈Z that (am)n = amn for some n ≥1.
We want to show for all a ̸= 0 and all m ∈Z that (am)n+1
?= am(n+1). By the recursive
deﬁnition of positive powers of am,
(5.4)
(am)n+1 = (am)nam.
From the inductive hypothesis, (am)n = amn, and plugging that into (5.4) tells us
(am)n+1 = amnam = amn+m,
where the last equation is a special case of Theorem 5.1 with exponents mn and m. Since
mn+m = m(n+1), we ﬁnally obtain (am)n+1 = am(n+1), which ﬁnishes the inductive step.
Now we turn to the case that n ≤0.
n = 0. Since the 0 power is 1 by deﬁnition, the desired equation (am)n ?= amn when n = 0
says (am)0 ?= a0, which says 1 ?= 1, and that’s true.
n < 0. Write n = −N, so N ∈Z+ and we want to show (am)−N
?= am(−N). The left
side is ((am)N)−1 by the deﬁnition of negative powers of am, and the right side is a−mN,
From what we already proved when the outer exponent is a positive integer and the inner
exponent is an arbitrary integer,
(am)N = amN.
Therefore we want to show
(amN)−1 ?= a−mN
for arbitrary m ∈Z. The left side denotes the (multiplicative) inverse of amN, and that is
a−mN thanks to Theorem 5.1 since that theorem tells us that amNa−mN = a0 = 1.
□
Appendix A. Another proof by induction on the number of terms
In Theorem 4.2 we proved an identity about derivatives by induction on the number of
functions in the identity. Here is another example of a theorem proved by induction on the
number of terms.
Theorem A.1. For all odd numbers a1, . . . , an where n ≥2, the product a1 · · · an is odd.
Proof. We induct on n, the number of odd numbers.
For the base case n = 2 we want to every product of two odd numbers a1 and a2 is odd.
Since these numbers are odd, a1 = 2k1 + 1 and a2 = 2k2 + 1 for some integers k1 and k2.
Then
a1a2 = (2k1 + 1)(2k2 + 1) = 4k1k2 + 2k1 + 2k2 + 1 = 2(2k1k2 + k1 + k2) + 1,
which is an odd number since 2k1k2 + k1 + k2 is an integer. That settles the base case.
Now assume for an n ≥2 that the result is true for all sets of n odd numbers. To prove
the result for n + 1, we want to show every set of n + 1 odd numbers a1, . . . , an+1 has a
product a1 · · · an+1 that is odd.

<!-- page 14 -->
14
KEITH CONRAD
A product of n + 1 numbers can be written either as a product of 2 numbers or as a
product of n numbers by collecting some factors into a single number:
(A.1)
a1a2 · · · an+1 = (a1a2 · · · an)an+1
is a product of the two numbers a1a2 · · · an and an+1, while
(A.2)
a1a2 · · · an+1 = a1a2 · · · an−1(anan+1)
is a product of the n numbers a1, a2, . . . , an−1, and anan+1.
Each of (A.1) and (A.2) leads to a proof of the inductive step: using (A.1) involves
the inductive hypothesis (all sets of n odd numbers) and then the base case (all sets of 2
odd numbers) while (A.2) involves the base case (all sets of 2 odd numbers) and then the
inductive hypothesis (all sets of n odd numbers).
First method. Write
a1a2 · · · anan+1 = (a1a2 · · · an)an+1
and the product a1a2 · · · an is odd by the inductive hypothesis (for n odd numbers). Then
(a1a2 · · · an)an+1 is a product of two odd numbers, a1a2 · · · an and an+1, so their product is
odd by the base case. Thus a1a2 · · · anan+1 is an odd number.
Second method. Write
a1a2 · · · anan+1 = a1a2 · · · an−1(anan+1).
The product anan+1 is an odd number by the base case, so a1a2 · · · an−1(anan+1) is a
product of n odd numbers: a1, a2, . . . , an−1, and anan+1. Therefore their product is odd
by the inductive hypothesis, which says a1a2 · · · an−1(anan+1) is odd, so a1a2 · · · anan+1 is
odd.
□

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*