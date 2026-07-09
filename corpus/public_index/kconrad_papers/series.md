# Infinite Series

> **Source**: https://kconrad.math.uconn.edu/blurbs/series.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
INFINITE SERIES
KEITH CONRAD
1. Introduction
The two basic concepts of calculus, diﬀerentiation and integration, are deﬁned in terms of limits
(Newton quotients and Riemann sums). In addition to these is a third fundamental limit process:
inﬁnite series. The label series is just another name for a sum. An inﬁnite series is a “sum” with
inﬁnitely many terms, such as
(1.1)
1 + 1
4 + 1
9 + 1
16 + · · · + 1
n2 + · · · .
The idea of an inﬁnite series is familiar from decimal expansions, for instance the expansion
π = 3.14159265358979...
can be written as
π = 3 + 1
10 + 4
102 + 1
103 + 5
104 + 9
105 + 2
106 + 6
107 + 5
108 + 3
109 +
5
1010 +
8
1011 + · · · ,
so π is an “inﬁnite sum” of fractions. Decimal expansions like this show that an inﬁnite series is
not a paradoxical idea, although it may not be clear how to deal with non-decimal inﬁnite series
like (1.1) at the moment.
Inﬁnite series provide two conceptual insights into the nature of the basic functions met in
high school (rational functions, trigonometric and inverse trigonometric functions, exponential and
logarithmic functions). First of all, these functions can be expressed in terms of inﬁnite series, and
in this way all these functions can be approximated by polynomials, which are the simplest kinds
of functions. That simpler functions can be used as approximations to more complicated functions
lies behind the method which calculators and computers use to calculate approximate values of
functions. The second insight we will have using inﬁnite series is the close relationship between
functions which seem at ﬁrst to be quite diﬀerent, such as exponential and trigonometric functions.
Two other applications we will meet are a proof by calculus that there are inﬁnitely many primes
and a proof that e is irrational.
2. Definitions and basic examples
Before discussing inﬁnite series we discuss ﬁnite ones. A ﬁnite series is a sum
a1 + a2 + a3 + · · · + aN,
where the ai’s are real numbers. In terms of Σ-notation, we write
a1 + a2 + a3 + · · · + aN =
N
X
n=1
an.
1

<!-- page 2 -->
2
KEITH CONRAD
For example,
(2.1)
N
X
n=1
1
n = 1 + 1
2 + 1
3 + · · · + 1
N .
The sum in (2.1) is called a harmonic sum, for instance
1 + 1
2 + 1
3 + 1
4 + 1
5 = 137
60 .
A very important class of ﬁnite series, more important than the harmonic ones, are the geometric
series
(2.2)
1 + r + r2 + · · · + rN =
N
X
n=0
rn.
An example is
10
X
n=0
1
2
n
=
10
X
n=0
1
2n = 1 + 1
2 + 1
4 + · · · + 1
210 = 2047
1024 ≈1.999023.
The geometric series (2.2) can be summed up exactly, as follows.
Theorem 2.1. When r ̸= 1, the series (2.2) is
1 + r + r2 + · · · + rN = 1 −rN+1
1 −r
= rN+1 −1
r −1
.
Proof. Let
SN = 1 + r + · · · + rN.
Then
rSN = r + r2 + · · · + rN+1.
These sums overlap in r + · · · + rN, so subtracting rSN from SN gives
(1 −r)SN = 1 −rN+1.
When r ̸= 1 we can divide and get the indicated formula for SN.
□
Example 2.2. For any N ≥0,
1 + 2 + 22 + · · · + 2N = 2N+1 −1
2 −1
= 2N+1 −1.
Example 2.3. For any N ≥0,
1 + 1
2 + 1
4 + · · · + 1
2N = 1 −(1/2)N+1
1 −1/2
= 2 −1
2N .
It is sometimes useful to adjust the indexing on a sum, for instance
(2.3)
1 + 2 · 2 + 3 · 22 + 4 · 23 + · · · + 100 · 299 =
100
X
n=1
n2n−1 =
99
X
n=0
(n + 1)2n.

<!-- page 3 -->
INFINITE SERIES
3
Comparing the two Σ’s in (2.3), notice how the renumbering of the indices aﬀects the expression
being summed: if we subtract 1 from the bounds of summation on the Σ then we add 1 to the
index “on the inside” to maintain the same overall sum. As another example,
32 + · · · + 92 =
9
X
n=3
n2 =
6
X
n=0
(n + 3)2.
Whenever the index is shifted down (or up) by a certain amount on the Σ it has to be shifted up (or
down) by a compensating amount inside the expression being summed so that we are still adding
the same numbers. This is analogous to the eﬀect of an additive change of variables in an integral,
e.g.,
Z 1
0
(x + 5)2 dx =
Z 6
5
u2 du =
Z 6
5
x2 dx,
where u = x + 5 (and du = dx). When the variable inside the integral is changed by an additive
constant, the bounds of integration are changed additively in the opposite direction.
Now we deﬁne the meaning of inﬁnite series, such as (1.1). The basic idea is that we look at the
sum of the ﬁrst N terms, called a partial sum, and see what happens in the limit as N →∞.
Deﬁnition 2.4. Let a1, a2, a3, . . . be an inﬁnite sequence of real numbers.
The inﬁnite series
P
n≥1 an is deﬁned to be
X
n≥1
an = lim
N→∞
N
X
n=1
an.
If the limit exists in R then we say P
n≥1 an is convergent. If the limit does not exist or is ±∞
then P
n≥1 an is called divergent.
Notice that we are not really adding up all the terms in an inﬁnite series at once. We only add
up a ﬁnite number of the terms and then see how things behave in the limit as the (ﬁnite) number
of terms tends to inﬁnity: an inﬁnite series is deﬁned to be the limit of its sequence of partial sums.
Example 2.5. Using Example 2.3,
X
n≥0
1
2n = lim
N→∞
N
X
n=0
1
2n = lim
N→∞2 −1
2N = 2.
So
X
n≥0
1
2n is a convergent series and its value is 2.
Building on this example we can compute exactly the value of any inﬁnite geometric series.
Theorem 2.6. For x ∈R, the (inﬁnite) geometric series P
n≥0 xn converges if |x| < 1 and diverges
if |x| ≥1. If |x| < 1 then
X
n≥0
xn =
1
1 −x.
Proof. For N ≥0, Theorem 2.1 tells us
N
X
n=0
xn =
(
(1 −xN+1)/(1 −x),
if x ̸= 1,
N + 1,
if x = 1.

<!-- page 4 -->
4
KEITH CONRAD
When |x| < 1, xN+1 →0 as N →∞, so
X
n≥0
xn = lim
N→∞
N
X
n=0
xn = lim
N→∞
1 −xN+1
1 −x
=
1
1 −x.
When |x| > 1 the numerator 1 −xN does not converge as N →∞, so P
n≥0 xn diverges.
(Speciﬁcally, the limit is ∞if x > 1 and the partials sums oscillate between values tending to ∞
and −∞if x < −1.)
What if |x| = 1? If x = 1 then the N-th partial sum is N + 1 so the series P
n≥0 1n diverges
(to ∞). If x = −1 then PN
n=0(−1)n oscillates between 1 and 0, so again the series P
n≥0(−1)n is
divergent.
□
We will see that Theorem 2.6 is the fundamental example of an inﬁnite series. Many important
inﬁnite series will be analyzed by comparing them to a geometric series (for a suitable choice of x).
If we start summing a geometric series not at 1, but at a higher power of x, then we can still get
a simple closed formula for the series, as follows.
Corollary 2.7. If |x| < 1 and m ≥0 then
X
n≥m
xn = xm + xm+1 + xm+2 + · · · =
xm
1 −x.
Proof. The N-th partial sum (for N ≥m) is
xm + xm+1 + · · · + xN = xm(1 + x + · · · + xN−m).
As N →∞, the sum inside the parentheses becomes the standard geometric series, whose value is
1/(1 −x). Multiplying by xm gives the asserted value.
□
Example 2.8. If |x| < 1 then x + x2 + x3 + · · · = x/(1 −x).
A divergent geometric series can diverge in diﬀerent ways: the partial sums may tend to ∞or
tend to both ∞and −∞or oscillate between 1 and 0. The label “divergent series” does not always
mean the partial sums tend to ∞. All “divergent” means is “not convergent.” Of course in a
particular case we may know the partial sums do tend to ∞, and then we would say “the series
diverges to ∞.”
The convergence of a series is determined by the behavior of the terms an for large n. If we
change (or omit) any initial set of terms in a series we do not change the convergence of divergence
of the series.
Here is the most basic general feature of convergent inﬁnite series.
Theorem 2.9. If the series P
n≥1 an converges then an →0 as n →∞.
Proof. Let SN = a1 + a2 + · · · + aN and let S = P
n≥1 an be the limit of the partial sums SN as
N →∞. Then as N →∞,
aN = SN −SN−1 →S −S = 0.
□
While Theorem 2.9 is formulated for convergent series, its main importance is as a “divergence
test”: if the general term in an inﬁnite series does not tend to 0 then the series diverges. For
example, Theorem 2.9 gives another reason that a geometric series P
n≥0 xn diverges if |x| ≥1,
because in this case xn does not tend to 0: |xn| = |x|n ≥1 for all n.

<!-- page 5 -->
INFINITE SERIES
5
It is an unfortunate fact of life that the converse of Theorem 2.9 is generally false: if an →0 we
have no guarantee that P
n≥0 an converges. Here is the standard illustration.
Example 2.10. Consider the harmonic series
X
n≥1
1
n. Although the general term 1
n tends to 0 it
turns out that
X
n≥1
1
n = ∞.
To show this we will compare PN
n=1 1/n with
R N
1
dt/t = log N. When n ≤t, 1/t ≤1/n. Integrating
this inequality from n to n + 1 gives
R n+1
n
dt/t ≤1/n, so
N
X
n=1
1
n ≥
N
X
n=1
Z n+1
n
dt
t =
Z N+1
1
dt
t = log(N + 1).
Therefore the N-th partial sum of the harmonic series is bounded below by log(N + 1). Since
log(N + 1) →∞as N →∞, so does the N-th harmonic sum, so the harmonic series diverges.
We will see later that the lower bound log(N + 1) for the N-th harmonic sum is rather sharp,
so the harmonic series diverges “slowly” since the logarithm function diverges slowly.
The divergence of the harmonic series is not just a counterexample to the converse of Theorem
2.9, but can be exploited in other contexts. Let’s use it to prove something about prime numbers!
Theorem 2.11. There are inﬁnitely many prime numbers.
Proof. (Euler) We will argue by contradiction: assuming there are only ﬁnitely many prime numbers
we will contradict the divergence of the harmonic series.
Consider the product of 1/(1 −1/p) as p runs through all prime numbers. Sums are denoted
with a Σ and products are denoted with a Π (capital pi), so our product is written as
Y
p
1
1 −1/p =
1
1 −1/2 ·
1
1 −1/3 ·
1
1 −1/5 · · · .
Since we assume there are ﬁnitely many primes, this is a ﬁnite product. Now expand each factor
into a geometric series:
Y
p
1
1 −1/p =
Y
p

1 + 1
p + 1
p2 + 1
p3 + · · ·

.
Each geometric series is greater than any of its partial sums. Pick any integer N ≥2 and truncate
each geometric series at the N-th term, giving the inequality
(2.4)
Y
p
1
1 −1/p >
Y
p

1 + 1
p + 1
p2 + 1
p3 + · · · + 1
pN

.
On the right side of (2.4) we have a ﬁnite product of ﬁnite sums, so we can compute this using the
distributive law (“super FOIL” in the terminology of high school algebra). That is, take one term
from each factor, multiply them together, and add up all these products. What numbers do we get
in this way on the right side of (2.4)?
A product of reciprocal integers is a reciprocal integer, so we obtain a sum of 1/n as n runs over
certain positive integers. Speciﬁcally, the n’s we meet are those whose prime factorization doesn’t

<!-- page 6 -->
6
KEITH CONRAD
involve any prime with exponent greater than N. Indeed, for any positive integer n > 1, if we
factor n into primes as
n = pe1
1 pe2
2 · · · per
r
then ei < n for all i. (Since pi ≥2, n ≥2ei, and 2m > m for any m ≥0 so n > ei.) Thus if n ≤N
any of the prime factors of n appear in n with exponent less than n ≤N, so 1/n is a number which
shows up when multiplying out (2.4). Here we need to know we are working with a product over
all primes.
Since 1/n occurs in the expansion of the right side of (2.4) for n ≤N and all terms in the
expansion are positive, we have the lower bound estimate
(2.5)
Y
p
1
1 −1/p >
N
X
n=1
1
n.
Since the left side is independent of N while the right side tends to ∞as N →∞, this inequality
is a contradiction so there must be inﬁnitely many primes.
□
We end this section with some algebraic properties of convergent series: termwise addition and
scaling.
Theorem 2.12. If P
n≥1 an and P
n≥1 bn converge then P
n≥1(an + bn) converges and
X
n≥1
(an + bn) =
X
n≥1
an +
X
n≥1
bn.
If P
n≥1 an converges then for any number c the series P
n≥1 can converges and
X
n≥1
can = c
X
n≥1
an.
Proof. Let SN = PN
n=1 an and TN = PN
n=1 bn. Set S = P
n≥1 an and T = P
n≥1 bn, so SN →S
and TN →T as N →∞. Then by known properties of limits of sequences, SN + TN →S + T and
cSN →cS as N →∞. These are the conclusions of the theorem.
□
Example 2.13. We have
X
n≥0
 1
2n + 1
3n

=
1
1 −1/2 +
1
1 −1/3 = 7
2
and
X
n≥0
5
4n = 5
X
n≥0
1
4n = 5
1
1 −1/4 = 20
3 .
3. Positive series
In this section we describe several ways to show that an inﬁnite series P
n≥1 an converges when
an > 0 for all n.
There is something special about series where all the terms are positive.
What is it?
The
sequence of partial sums is increasing: SN+1 = SN +aN, so SN+1 > SN for every N. An increasing
sequence has two possible limiting behaviors: it converges or it tends to ∞. (That is, divergence
can only happen in one way: the partial sums tend to ∞.) We can tell if an increasing sequence
converges by showing it is bounded above. Then it converges and its limit is an upper bound on the
whole sequence. If the terms in an increasing sequence are not bounded above then the sequence

<!-- page 7 -->
INFINITE SERIES
7
is unbounded and tends to ∞. Compare this to the sequence of partial sums PN
n=0(−1)n, which
are bounded but do not converge (they oscillate between 1 and 0).
Let’s summarize this property of positive series. If an > 0 for every n and there is a constant
C such that all partial sums satisfy PN
n=1 an < C then P
n≥1 an converges and P
n≥1 an ≤C. On
the other hand, if there is no upper bound on the partial sums then P
n≥1 an = ∞. We will use
this over and over again to explain various convergence tests for positive series.
Theorem 3.1 (Integral Test). Suppose an = f(n) where f is a continuous decreasing positive
function. Then P
n≥1 an converges if and only if
R ∞
1 f(x) dx converges.
Proof. We will compare the partial sum PN
n=1 an and the “partial integral”
R N
1 f(x) dx.
Since f(x) is a decreasing function,
n ≤x ≤n + 1 =⇒an+1 = f(n + 1) ≤f(x) ≤f(n) = an.
Integrating these inequalities between n and n + 1 gives
(3.1)
an+1 ≤
Z n+1
n
f(x) dx ≤an.
since the interval [n, n + 1] has length 1. Therefore
(3.2)
N
X
n=1
an ≥
N
X
n=1
Z n+1
n
f(x) dx =
Z N+1
1
f(x) dx
and
(3.3)
N
X
n=1
an = a1 +
N
X
n=2
an ≤a1 +
N
X
n=2
Z n
n−1
f(x) dx = f(1) +
Z N
1
f(x) dx.
Combinining (3.2) and (3.3),
(3.4)
Z N+1
1
f(x) dx ≤
N
X
n=1
an ≤f(1) +
Z N
1
f(x) dx.
Assume that
R ∞
1 f(x) dx converges. Since f(x) is a positive function,
R N
1 f(x) dx <
R ∞
1 f(x) dx.
Thus by the second inequality in (3.4)
N
X
n=1
an < f(1) +
Z ∞
1
f(x) dx,
so the partial sums are bounded above. Therefore the series P
n≥1 an converges.
Conversely, assume P
n≥1 an converges. Then the partial sums PN
n=1 an are bounded above (by
the whole series P
n≥1 an). Every partial integral of
R ∞
1 f(x) dx is bounded above by one of these
partial sums according to the ﬁrst inequality of (3.4), so the partial integrals are bounded above
and thus the improper integral
R ∞
1 f(x) dx converges.
□
Example 3.2. We were implicitly using the integral test with f(x) = 1/x when we proved the
harmonic series diverges in Example 2.10. For the harmonic series, (3.4) becomes
(3.5)
log(N + 1) ≤
N
X
n=1
1
n ≤1 + log N.

<!-- page 8 -->
8
KEITH CONRAD
Thus the harmonic series diverges “logarithmically.” The following table illustrates these bounds
when N is a power of 10.
N
log(N + 1)
PN
n=1 1/n
1 + log N
10
2.398
2.929
3.303
100
4.615
5.187
5.605
1000
6.909
7.485
7.908
10000
9.210
9.788
10.210
Table 1.
Example 3.3. Generalizing the harmonic series, consider
X
n≥1
1
np = 1 + 1
2p + 1
3p + 1
4p + · · ·
where p > 0. This is called a p-series. Its convergence is related to the integral
R ∞
1
dx/xp. Since
the integrand 1/xp has an anti-derivative that can be computed explicitly, we can compute the
improper integral:
Z ∞
1
dx
xp =
(
1
p−1,
if p > 1,
∞,
if 0 < p ≤1.
Therefore P
n≥1 1/np converges when p > 1 and diverges when 0 < p ≤1. For example, P
n≥1 1/n2
converges and P
n≥1 1/√n diverges.
Example 3.4. The series
X
n≥2
1
n log n diverges by the integral test since
Z ∞
2
dx
x log x = log log x

∞
2
= ∞.
(We stated the integral test with a lower bound of 1 but it obviously adapts to series where the
ﬁrst index of summation is something other than 1, as in this example.)
Example 3.5. The series
X
n≥2
1
n(log n)2 , with terms just slightly smaller than in the previous
example, converges. Using the integral test,
Z ∞
2
dx
x(log x) = −
1
log x

∞
2
=
1
log 2,
which is ﬁnite.
Because the convergence of a positive series is intimately tied up with the boundedness of its
partial sums, we can determine the convergence or divergence of one positive series from another
if we have an inequality in one direction between the terms of the two series. This leads to the
following convergence test.
Theorem 3.6 (Comparison test). Let 0 < an ≤bn for all n. If P
n≥1 bn converges then P
n≥1 an
converges. If P
n≥1 an diverges then P
n≥1 bn diverges.

<!-- page 9 -->
INFINITE SERIES
9
Proof. Since 0 < an ≤bn we have
(3.6)
N
X
n=1
an ≤
N
X
n=1
bn
and both sequences of partial sums are increasing or stay the same (they are “nondecreasing”).
If P
n≥1 bn converges then the partial sums on the right side of (3.6) are bounded, so the partial
sums on the left side are bounded, and therefore P
n≥1 an converges because an increasing (really, a
nondecreasing) bounded sequence of real numbers converges. If P
n≥1 an diverges then PN
n=1 an →
∞(see the second paragraph of this section again), so PN
n=1 bn →∞, so P
n≥1 bn diverges.
□
Example 3.7. If 0 ≤x < 1 then P
n≥1 xn/n converges since xn/n ≤xn so the series is bounded
above by the geometric series P
n≥1 xn, which converges. Notice that, unlike the geometric series,
we are not giving any kind of closed form expression for P
n≥1 xn/n. All we are saying is that the
series converges.
The series P
n≥1 xn/n does not converge for x ≥1: if x = 1 it is the harmonic series and if x > 1
then the general term xn/n tends to ∞(not 0) so the series diverges to ∞.
Example 3.8. The integral test is a special case of the comparison test, where we compare an
with
R n+1
n
f(x) dx and with
R n
n−1 f(x) dx.
Just as convergence of a series does not depend on the behavior of the initial terms of the series,
what is important in the comparison test is an inequality an ≤bn for large n. If this inequality
happens not to hold for small n but does hold for all large n then the comparison test still works.
The following two examples use this “extended comparison test” when the form of the comparison
test in Theorem 3.6 does not strictly apply (because the inequality an ≤bn doesn’t hold for small
n).
Example 3.9. If 0 ≤x < 1 then P
n≥1 nxn converges. This is obvious for x = 0. We can’t
get convergence for 0 < x < 1 by a comparison with P
n≥1 xn because the inequality goes the
wrong way: nxn > xn, so convergence of P
n≥1 xn doesn’t help us show convergence of P
n≥1 nxn.
However, let’s write
nxn = nxn/2xn/2.
Since 0 < x < 1, nxn/2 →0 as n →∞, so nxn/2 ≤1 for large n (depending on the speciﬁc
value of x, e.g, for x = 1/2 the inequality is false at n = 3 but is correct for n ≥4).
Thus
for all large n we have nxn ≤xn/2 so P
n≥1 nxn converges by comparison with the geometric
series P
n≥1 xn/2 = P
n≥1(√x)n. We have not obtained any kind of closed formula for P
n≥1 nxn,
however.
If x ≥1 then P
n≥1 nxn diverges since nxn ≥1 for all n, so the general term does not tend to 0.
Example 3.10. If x ≥0 then the series P
n≥0 xn/n! converges. This is obvious for x = 0. For
x > 0 we will use the comparison test and the lower bound estimate n! > nn/en. Let’s recall that
this lower bound on n! comes from Euler’s integral formula
n! =
Z ∞
0
tne−t dt >
Z ∞
n
tne−t dt > nn
Z ∞
n
e−t dt = nn
en .
Then for positive x
(3.7)
xn
n! <
xn
nn/en =
ex
n
n
.

<!-- page 10 -->
10
KEITH CONRAD
Here x is ﬁxed and we should think about what happens as n grows. The ratio ex/n tends to 0 as
n →∞, so for large n we have
(3.8)
ex
n < 1
2
(any positive number less than 1 will do here; we just use 1/2 for concreteness). Raising both sides
of (3.8) to the n-th power,
ex
n
n
< 1
2n .
Comparing this to (3.7) gives xn/n! < 1/2n for large n, so the terms of the series P
n≥0 xn/n! drop
oﬀfaster than the terms of the convergent geometric series P
n≥0 1/2n when we go out far enough.
The extended comparison test now implies convergence of P
n≥0 xn/n! if x > 0.
Example 3.11. The series
X
n≥1
1
5n2 + n converges since
1
5n2 + n <
1
5n2 and
X
n≥1
1
5n2 converges by
Example 3.3.
Let’s try to apply the comparison test to P
n≥1 1/(5n2 −n). The rate of growth of the nth term
is like 1/(5n2), but the inequality now goes the wrong way:
1
5n2 <
1
5n2 −n
for all n. So we can’t quite use the comparison test to show P
n≥1 1/(5n2 −n) converges (which it
does). The following limiting form of the comparison test will help here.
Theorem 3.12 (Limit comparison test). Let an, bn > 0 and suppose the ratio an/bn has a positive
limit. Then P
n≥1 an converges if and only if P
n≥1 bn converges.
Proof. Let L = limn→∞an/bn. For all large n,
L
2 < an
bn
< 2L,
so
(3.9)
L
2 bn < an < 2Lbn
for large n. Since L/2 and 2L are positive, the convergence of P
n≥1 bn is the same as convergence
of P
n≥1(L/2)bn and P
n≥1(2L)bn. Therefore the ﬁrst inequality in (3.9) and the comparison test
show convergence of P
n≥1 an implies convergence of P
n≥1 bn. The second inequality in (3.9) and
the comparison test show convergence of P
n≥1 bn implies convergence of P
n≥1 an. (Although (3.9)
may not be true for all n, it is true for large n, and that suﬃces to apply the extended comparison
test.)
□
The way to use the limit comparison test is to replace terms in a series by simpler terms which
grow at the same rate (at least up to a scaling factor). Then analyze the series with those simpler
terms.
Example 3.13. We return to
X
n≥1
1
5n2 −n. As n →∞, the nth term grows like 1/5n2:
1/(5n2 −n)
1/5n2
→1.

<!-- page 11 -->
INFINITE SERIES
11
Since P
n≥1 1/(5n2) converges, so does P
n≥1 1/(5n2 −n). In fact, if an is any sequence whose
growth is like 1/n2 up to a scaling factor then P
n≥1 an converges. In particular, this is a simpler
way to settle the convergence in Example 3.11 than by using the inequalities in Example 3.11.
Example 3.14. To determine if
X
n≥1
r
n3 −n2 + 5n
4n6 + n
converges we replace the nth term with the expression
r
n3
4n6 =
1
2n3/2 ,
which grows at the same rate. The series P
n≥1 1/(2n3/2) converges, so the original series converges.
The limit comparison test underlies an important point: the convergence of a series P
n≥1 an
is not assured just by knowing if an →0, but it is assured if an →0 rapidly enough. That is,
the rate at which an tends to 0 is often (but not always) a means of explaining the convergence of
P
n≥1 an. The diﬀerence between someone who has an intuitive feeling for convergence of series and
someone who can only determine convergence on a case-by-case basis using memorized rules in a
mechanical way is probably indicated by how well the person understands the connection between
convergence of a series and rates of growth (really, decay) of the terms in the series. Armed with
the convergence of a few basic series (like geometric series and p-series), the convergence of most
other series encountered in a calculus course can be determined by the limit comparison test if you
understand well the rates of growth of the standard functions. One exception is if the series has a
log term, in which case it might be useful to apply the integral test.
4. Series with mixed signs
All our previous convergence tests apply to series with positive terms. They also apply to series
whose terms are eventually positive (just omit any initial negative terms to get a positive series)
or eventually negative (negate the series, which doesn’t change the convergence status, and now
we’re reduced to an eventually positive series). What do can we do for series whose terms are not
eventually all positive or eventually all negative? These are the series with inﬁnitely many positive
terms and inﬁnitely many negative terms.
Example 4.1. Consider the alternating harmonic series
X
n≥1
(−1)n−1
n
= 1 −1
2 + 1
3 −1
4 + 1
5 −1
6 + · · · .
The usual harmonic series diverges, but the alternating signs might have diﬀerent behavior. The
following table collects some of the partial sums.
N
PN
n=1(−1)n−1/n
10
.6456
100
.6882
1000
.6926
10000
.6930
Table 2.

<!-- page 12 -->
12
KEITH CONRAD
These partial sums are not clear evidence in favor of convergence: after 10,000 terms we only
get apparent stability in the ﬁrst 2 decimal digits. The harmonic series diverges slowly, so perhaps
the alternating harmonic series diverges too (and slower).
Deﬁnition 4.2. An inﬁnite series where the terms alternate in sign is called an alternating series.
An alternating series starting with a positive term can be written as P
n≥1(−1)n−1an where
an > 0 for all n. If the ﬁrst term is negative then a reasonable general notation is P
n≥1(−1)nan
where an > 0 for all n. Obviously negating an alternating series of one type turns it into the other
type.
Theorem 4.3 (Alternating series test). An alternating series whose n-th term in absolute value
tends monotonically to 0 as n →∞is a convergent series.
Proof. We will work with alterating series which have an initial positive term, so of the form
P
n≥1(−1)n−1an. Since successive partial sums alterate adding and subtracting an amount which,
in absolute value, steadily tends to 0, the relation between the partial sums is indicated by the
following inequalities:
s2 < s4 < s6 < · · · < s5 < s3 < s1.
In particular, the even-indexed partial sums are an increasing sequence which is bounded above
(by s1, say), so the partial sums s2m converge. Since |s2m+1 −s2m| = |a2m+1| →0, the odd-indexed
partial sums converge to the same limit as the even-indexed partial sums, so the sequence of all
partial sums has a single limit, which means P
n≥1(−1)n−1an converges.
□
Example 4.4. The alternating harmonic series
X
n≥1
(−1)n−1
n
converges.
Example 4.5. While the p-series P
n≥1 1/np converges only for p > 1, the alternating p-series
P
n≥1(−1)n−1/np converges for the wider range of exponents p > 0 since it is an alternating series
satisfying the hypotheses of the alternating series test.
Example 4.6. We saw P
n≥1 xn/n converges for 0 ≤x < 1 (comparison to the geometric series)
in Example 3.7. If −1 ≤x < 0 then P
n≥1 xn/n converges by the alternating series test: the
negativity of xn makes the terms xn/n alternate in sign. To apply the alternating series test we
need

xn+1
n + 1
 <

xn
n

for all n, which is equivalent after some algebra to
|x| < n + 1
n
for all n, and this is true since |x| ≤1 < (n + 1)/n.
Example 4.7. In Example 3.10 the series P
n≥0 xn/n! was seen to converge for x ≥0. If x < 0
the series is an alternating series. Does it ﬁt the hypotheses of the alternating series test? We need

xn+1
(n + 1)!
 <

xn
n!

for all n, which is equivalent to
|x| < n + 1

<!-- page 13 -->
INFINITE SERIES
13
for all n. For each particular x < 0 this may not be true for all n (if x = −3 it fails for n = 1 and
2), but it is deﬁnitely true for all suﬃciently large n. Therefore the terms of P
n≥0 xn/n! are an
“eventually alternating” series. Since what matters for convergence is the long-term behavior and
not the initial terms, we can apply the alternating series test to see P
n≥0 xn/n! converges by just
ignoring an initial piece of the series.
When a series has inﬁnitely many positive and negative terms which are not strictly alternating,
convergence may not be easy to check. For example, the trigonometric series
X
n≥1
sin(nx)
n
= sin x + sin(2x)
2
+ sin(3x)
3
+ sin(4x)
4
+ · · ·
turns out to be convergent for every number x, but the arrangement of positive and negative terms
in this series can be quite subtle in terms of x.
The proof that this series converges uses the
technique of summation by parts, which won’t be discussed here.
While it is generally a delicate matter to show a non-alternating series with mixed signs converges,
there is one useful property such series might have which does imply convergence. It is this: if the
series with all terms made positive converges then so does the original series. Let’s give this idea
a name and then look at some examples.
Deﬁnition 4.8. A series P
n≥1 an is absolutely convergent if P
n≥1 |an| converges.
Don’t confuse P
n≥1 |an| with | P
n≥1 an|; absolute convergence refers to convergence if we drop
the signs from the terms in the series, not from the series overall. The diﬀerence between P
n≥1 an
and | P
n≥1 an| is at most a single sign, while there is a substantial diﬀerence between P
n≥1 an
and P
n≥1 |an| if the an’s have many mixed signs; that is the diﬀerence which absolute convergence
involves.
Example 4.9. We saw P
n≥1 xn/n converges if 0 ≤x < 1 in Example 3.7. Since |xn/n| = |x|n/n,
the series P
n≥1 xn/n is absolutely convergent if |x| < 1. Note the alternating harmonic series
P
n≥1(−1)n−1/n is not absolutely convergent, however.
Example 4.10. In Example 3.10 we saw P
n≥0 xn/n! converges for all x ≥0. Since |xn/n!| =
|x|n/n!, the series P
n≥0 xn/n! is absolutely convergent for all x.
Example 4.11. By Example 3.9, P
n≥1 nxn converges absolutely if |x| < 1.
Example 4.12. The two series
X
n≥1
sin(nx)
n2
,
X
n≥1
cos(nx)
n2
,
where the nth term has denominator n2, are absolutely convergent for any x since the absolute
value of the nth term is at most 1/n2 and P
n≥1 1/n2 converges.
The relevance of absolute convergence is two-fold: 1) we can use the many convergence tests for
positive series to determine if a series is absolutely convergent, and 2) absolute convergence implies
ordinary convergence.
We just illustrated the ﬁrst point several times. Let’s show the second point.
Theorem 4.13 (Absolute convergence test). Every absolutely convergent series is a convergent
series.

<!-- page 14 -->
14
KEITH CONRAD
Proof. We give two proofs. The ﬁrst one, which is simpler, exploits special features of real numbers.
The second proof can be applied in more general settings that use inﬁnite series of numbers other
than real numbers (e.g., inﬁnite series of complex numbers or inﬁnite series of functions).
First proof: For all n we have
−|an| ≤an ≤|an|,
so
0 ≤an + |an| ≤2|an|.
Since P
n≥1 |an| converges, so does P
n≥1 2|an| (to twice the value). Therefore by the comparison
test we obtain convergence of P
n≥1(an + |an|). Subtracting P
n≥1 |an| from this shows P
n≥1 an
converges.
Second proof: To show P
n≥1 an converges, we want to show the partial sums
sN = a1 + a2 + · · · + aN
have a limit. We will show the sequence of partial sums {sN} is a Cauchy sequence: for all ε > 0
there is a positive integer M such that if N, N′ ≥M then |sN −sN′| < ε.
Since P
n≥1 |an| is assumed to converge, the partial sums
tN = |a1| + |a2| + · · · + |aN|
form a Cauchy sequence: for all ε > 0 there is a positive integer M such that if N, N′ ≥M then
|tN −tN′| < ε. Taking N ≥N′ without loss of generality, we have |tN −tN′| = |aN′+1| + · · · + |aN|,
so
N ≥N′ ≥M =⇒|aN′+1| + · · · + |aN| < ε.
Thus
N ≥N′ ≥M =⇒|sN −sN′| = |aN′+1 + · · · + aN| ≤|aN′+1| + · · · + |aN| = |tN −tN′| < ε,
so {sN} is a Cauchy sequence and therefore it converges in R.
□
We can now say the series P
n≥1 xn/n and P
n≥1 nxn converge for |x| < 1 and P
n≥0 xn/n!
converges for all x by our treatment of these series for positive x alone in Section 3. The argument
we gave in Examples 4.6 and 4.7 for the convergence of P
n≥1 xn/n and P
n≥1 xn/n! when x < 0,
using the alternating series test, can be avoided. (But we do need the alternating series test to
show P
n≥1 xn/n converges at x = −1.)
Corollary 4.14. If |an| ≤bn and P
n≥1 bn converges then P
n≥1 an converges.
Proof. By the comparison test (Theorem 3.6), convergence of P
n≥1 bn implies convergence of
P
n≥1 |an|, and by Theorem 4.13 P
n≥1 an converges.
□
A series which converges but is not absolutely convergent is called conditionally convergent. An
example of a conditionally convergent series is the alternating harmonic series P
n≥1(−1)n−1/n.
The distinction between absolutely convergent series and conditionally convergent series might
seem kind of minor, since it involves whether or not a particular convergence test (the absolute
convergence test) works on that series.
But the distinction is actually profound, and is nicely
illustrated by the following example of Dirichlet (1837).
Example 4.15. Let L = 1 −1/2 + 1/3 −1/4 + 1/5 −1/6 + · · · be the alternating harmonic series.
Consider the rearrangement of the terms where we follow a positive term by two negative terms:
1 −1
2 −1
4 + 1
3 −1
6 −1
8 + 1
5 −1
10 −1
12 + · · ·

<!-- page 15 -->
INFINITE SERIES
15
If we add each positive term to the negative term following it, we obtain
1
2 −1
4 + 1
6 −1
8 + 1
10 −1
12 + · · · ,
which is precisely half the alternating harmonic series (multiply L by 1/2 and see what you get
termwise). Therefore, by rearranging the terms of the alternating harmonic series we obtained a
new series whose sum is (1/2)L instead of L. If (1/2)L = L, doesn’t that mean 1 = 2? What
happened?
This example shows addition of terms in an inﬁnite series is not generally commutative, unlike
with ﬁnite series. In fact, this feature is characteristic of the conditionally convergent series, as
seen in the following amazing theorem.
Theorem 4.16 (Riemann, 1854). If an inﬁnite series is conditionally convergent then it can be
rearranged to sum up to any desired value. If an inﬁnite series is absolutely convergent then all of
its rearrangements converge to the same sum.
For instance, the alternating harmonic series can be rearranged to sum up to 1, to −5.673, to
π, or to any other number you wish. That we rearranged it in Example 4.15 to sum up to half
its usual value was special only in the sense that we could make the rearrangement achieving that
eﬀect quite explicit.
Theorem 4.16, whose proof we omit, is called Riemann’s rearrangement theorem. It indicates
that absolutely convergent series are better behaved than conditionally convergent ones.
The
ordinary rules of algebra for ﬁnite series generally extend to absolutely convergent series but not
to conditionally convergent series.
5. Power series
The simplest functions are polynomials: c0 + c1x + · · · + cdxd. In diﬀerential calculus we learn
how to locally approximate many functions by linear functions (the tangent line approximation).
We now introduce an idea which will let us give an exact representation of functions in terms of
“polynomials of inﬁnite degree.” The precise name for this idea is a power series.
Deﬁnition 5.1. A power series is a function of the form f(x) = P
n≥0 cnxn.
For instance, a polynomial is a power series where cn = 0 for large n. The geometric series
P
n≥0 xn is a power series. It only converges for |x| < 1. We have also met other power series, like
X
n≥1
xn
n ,
X
n≥1
nxn,
X
n≥0
xn
n! .
These three series converge on the respective intervals [−1, 1), (−1, 1) and (−∞, ∞).
For any power series P
n≥0 cnxn it is a basic task to ﬁnd those x where the series converges. It
turns out in general, as in all of our examples, that a power series converges on an interval. Let’s
see why.
Theorem 5.2. If a power series P
n≥0 cnxn converges at x = b ̸= 0 then it converges absolutely
for |x| < |b|.
Proof. Since P
n≥0 cnbn converges the general term tends to 0, so |cnbn| ≤1 for large n. If |x| < |b|
then
|cnxn| = |cnbn|
x
b

n
,

<!-- page 16 -->
16
KEITH CONRAD
which is at most |x/b|n for large n. The series P
n≥0 |x/b|n converges since it’s a geometric series
and |x/b| < 1. Therefore by the (extended) comparison test P
n≥0 |cnxn| converges, so P
n≥0 cnxn
is absolutely convergent.
□
Example 5.3. If a power series converges at −7 then it converges on the interval (−7, 7). We can’t
say for sure how it converges at 7.
Example 5.4. If a power series diverges at −7 then it diverges for |x| > 7: if it were to converge
at a number x where |x| > 7 then it would converge in the interval (−|x|, |x|) so in particular at
−7, a contradiction.
What these two examples illustrate, as consequences of Theorem 5.2, is that the values of x
where a power series P
n≥0 cnxn converges is an interval centered at 0, so of the form
(−r, r),
[−r, r),
(−r, r],
[−r, r]
for some r. We call r the radius of convergence of the power series. The only diﬀerence between
these diﬀerent intervals is the presence or absence of the endpoints. All possible types of interval
of convergence can occur: P
n≥0 xn has interval of convergence (−1, 1), P
n≥1 xn/n has interval of
convergence [−1, 1), P
n≥1(−1)nxn/n has interval of convergence (−1, 1] and P
n≥1 xn/n2 (a new
example we have not met before) has interval of convergence [−1, 1].
The radius of convergence and the interval of convergence are closely related but should not be
confused. The interval is the actual set where the power series converges. The radius is simply the
half-length of this set (and doesn’t tell us whether or not the endpoints are included). If we don’t
care about convergence behavior on the boundary of the interval of convergence than we can get
by just knowing the radius of convergence: the series always converges (absolutely) on the inside
of the interval of convergence.
For the practical computation of the radius of convergence in basic examples it is convenient to
use a new convergence test for positive series.
Theorem 5.5 (Ratio test). If an > 0 for all n, assume
q = lim
n→∞
an+1
an
exists.
If q < 1 then P
n≥1 an converges. If q > 1 then P
n≥1 an diverges. If q = 1 then no
conclusion can be drawn.
Proof. Assume q < 1. Pick s between q and 1: q < s < 1. Since an+1/an →q, we have an+1/an < s
for all large n, say for n ≥n0. Then an+1 < san when n ≥n0, so
an0+1 < san0,
an0+2 < san0+1 < s2an0,
an0+3 < san0+2 < s3an0,
and more generally an0+k < skan0 for any k ≥0. Writing n0 + k as n we have
n ≥n0 =⇒an < sn−n0an0 = an0
sn0 sn.
Therefore when n ≥n0 the number an is bounded above by a constant multiple of sn. Hence
P
n≥1 an converges by comparison to a constant multiple of the convergent geometric series P
n≥1 sn.
In the other direction, if q > 1 then pick s with 1 < s < q. An argument similar to the previous
one shows an grows at least as quickly as a constant multiple of sn, but this time P
n≥1 sn diverges
since s > 1. So P
n≥1 an diverges too.
When q = 1 we can’t make a deﬁnite conclusion since both P
n≥1 1/n and P
n≥1 1/n2 have
q = 1.
□

<!-- page 17 -->
INFINITE SERIES
17
Example 5.6. We give a proof that P
n≥1 nxn has radius of convergence 1 which is shorter than
Examples 3.9 and 4.11. Take an = |nxn| = n|x|n. Then
an+1
an
= n + 1
n
|x| →|x|
as n →∞. Thus if |x| < 1 the series P
n≥1 nxn is absolutely convergent by the ratio test. If |x| > 1
this series is divergent. Notice the ratio test does not tell us what happens to P
n≥1 nxn when
|x| = 1; we have to check x = 1 and x = −1 individually.
Example 5.7. A similar argument shows P
n≥1 xn/n has radius of convergence 1 since
|xn+1/(n + 1)|
|xn/n|
=
n
n + 1|x| →|x|
as n →∞.
Example 5.8. We show the series P
n≥0 xn/n! converges absolutely for all x. Using the ratio test
we look at
|xn+1/(n + 1)!|
|xn/n!|
=
|x|
n + 1 →0
as n →∞. Since this limit is less than 1 for all x, we are done by the ratio test. The radius of
convergence is inﬁnite.
Power series are important for two reasons: they give us much greater ﬂexibility to deﬁne new
kinds of functions and many standard functions can be expressed in terms of a power series.
Intuitively, if a known function f(x) has a power series representation on some interval around
0, say
f(x) =
X
n≥0
cnxn = c0 + c1x + c2x2 + c3x3 + c4x4 + · · ·
for |x| < r, then we can guess a formula for cn in terms of the behavior of f(x). To begin we have
f(0) = c0.
Now we think about power series as something like “inﬁnite degree polynomials.” We know how
to diﬀerentiate a polynomial by diﬀerentiating each power of x separately. Let’s assume this works
for power series too in the interval of convergence:
f′(x) =
X
n≥1
ncnxn−1 = c1 + 2c2x + 3c3x2 + 4c4x3 + · · · ,
so we expect
f′(0) = c1.
Now let’s diﬀerentiate again:
f′′(x) =
X
n≥2
n(n −1)cnxn−2 = 2c2 + 6c3x + 12c4x2 + · · · ,
so
f′′(0) = 2c2.
Diﬀerentiating a third time (formally) and setting x = 0 gives
f(3)(0) = 6c3.
The general rule appears to be
f(n)(0) = n!cn,

<!-- page 18 -->
18
KEITH CONRAD
so we should have
cn = f(n)(0)
n!
.
This procedure really is valid, according to the following theorem whose long proof is omitted.
Theorem 5.9. Any function represented by a power series in an open interval (−r, r) is inﬁnitely
diﬀerentiable in (−r, r) and its derivatives can be computed by termwise diﬀerentiation of the power
series.
This means our previous calculations are justiﬁed: if a function f(x) can be written in the form
P
n≥0 cnxn in an interval around 0 then we must have
(5.1)
cn = f(n)(0)
n!
.
In particular, a function has at most one expression as a power series P
n≥0 cnxn around 0. And
a function which is not inﬁnitely diﬀerentiable around 0 will deﬁnitely not have a power series
representation P
n≥0 cnxn. For instance, |x| has no power series representation of this form since
it is not diﬀerentiable at 0.
Remark 5.10. We can also consider power series f(x) = P
n≥0 cn(x −a)n, whose interval of
convergence is centered at a. In this case the coeﬃcients are given by the formula cn = f(n)(a)/n!.
For simplicity we will focus on power series “centered at 0” only.
Remark 5.11. Even if a power series converges on a closed interval [−r, r], the power series for
its derivative need not converge at the endpoints. Consider f(x) = P
n≥1(−1)nx2n/n. It converges
for |x| ≤1 but the derivative series is P
n≥1 2(−1)nx2n−1, which converges for |x| < 1.
Remark 5.12. Because a power series can be diﬀerentiated (inside its interval of convergence)
termwise, we can discover solutions to a diﬀerential equation by inserting a power series with
unknown coeﬃcients into the diﬀerential equation to get relations between the coeﬃcients. Then
a few initial coeﬃcients, once chosen, should determine all the higher ones. After we compute the
radius of convergence of this new power series we will have found a solution to the diﬀerential
equation in a speciﬁc interval. This idea goes back to Newton. It does not necessarily provide us
with all solutions to a diﬀerential equation, but it is one of the standard methods to ﬁnd some
solutions.
Example 5.13. If |x| < 1 then
X
n≥0
xn =
1
1 −x. Diﬀerentiating both sides, for |x| < 1 we have
X
n≥1
nxn−1 =
1
(1 −x)2 .
Multiplying by x gives us
X
n≥1
nxn =
x
(1 −x)2 ,
so we have ﬁnally found a “closed form” expression for an inﬁnite series we ﬁrst met back in
Example 3.9.

<!-- page 19 -->
INFINITE SERIES
19
Example 5.14. If there is a power series representation P
n≥0 cnxn for ex then (5.1) shows cn =
1/n!. The only possible way to write ex as a power series is
X
n≥0
xn
n! = 1 + x + x2
2 + x3
3! + x4
4! + · · · .
Is this really a valid formula for ex? Well, we checked before that this power series converges for
all x. Moreover, calculating the derivative of this series reproduces the series again, so this series is
a function satisfying y′(x) = y(x). The only solutions to this diﬀerential equation are Cex and we
can recover C by setting x = 0. Since the power series has constant term 1 (so its value at x = 0
is 1), its C is 1, so this power series is ex:
ex =
X
n≥0
xn
n! .
Loosely speaking, this means the polynomials
1,
1 + x,
1 + x + x2
2 ,
1 + x + x2
2 + x3
6 , . . .
are good approximations to ex. (Where they are good will depend on how far x is from 0.) In
particular, setting x = 1 gives an inﬁnite series representation of the number e:
(5.2)
e =
X
n≥0
1
n! = 1 + 1
2 + 1
3! + 1
4! + · · ·
Formula (5.2) can be used to verify an interesting fact about e.
Theorem 5.15. The number e is irrational.
Proof. (Fourier) For any n,
e
=

1 + 1
2! + 1
3! + · · · + 1
n!

+

1
(n + 1)! +
1
(n + 2)! + · · ·

=

1 + 1
2! + 1
3! + · · · + 1
n!

+ 1
n!

1
n + 1 +
1
(n + 2)(n + 1) + · · ·

.
The second term in parentheses is positive and bounded above by the geometric series
1
n + 1 +
1
(n + 1)2 +
1
(n + 1)3 + · · · = 1
n.
Therefore
0 < e −

1 + 1
2! + 1
3! + · · · + 1
n!

≤
1
n · n!.
Write the sum 1 + 1/2! + · · · + 1/n! as a fraction with common denominator n!, say as pn/n!. Clear
the denominator n! to get
(5.3)
0 < n!e −pn ≤1
n.
So far everything we have done involves no unproved assumptions. Now we introduce the rationality
assumption. If e is rational, then n!e is an integer when n is large (since any integer is a factor
by n! for large n). But that makes n!e −pn an integer located in the open interval (0, 1), which is
absurd. We have a contradiction, so e is irrational.
□

<!-- page 20 -->
20
KEITH CONRAD
We return to the general task of representing functions by their power series. Even when a
function is inﬁnitely diﬀerentiable for all x, its power series could have a ﬁnite radius of convergence.
Example 5.16. Viewing 1/(1 + x2) as 1/(1 −(−x2)) we have the geometric series formula
1
1 + x2 =
X
n≥0
(−x2)n =
X
n≥0
(−1)nx2n
when |−x2| < 1, or equivalently |x| < 1. The series has a ﬁnite interval of convergence (−1, 1) even
though the function 1/(1 + x2) has no bad behavior at the endpoints: it is inﬁnitely diﬀerentiable
at every real number x.
Example 5.17. Let f(x) = P
n≥1 xn/n. This converges for −1 ≤x < 1. For |x| < 1 we have
f′(x) =
X
n≥1
xn−1 =
X
n≥0
xn =
1
1 −x.
When |x| < 1, an antiderivative of 1/(1 −x) is −log(1 −x). Since f(x) and −log(1 −x) have the
same value (zero) at x = 0 they are equal:
−log(1 −x) =
X
n≥1
xn
n
for |x| < 1. Replacing x with −x and negating gives
(5.4)
log(1 + x) =
X
n≥1
(−1)n−1
n
xn
for |x| < 1. The right side converges at x = 1 (alternating series) and diverges at x = −1. It
seems plausible, since the series equals log(1 + x) on (−1, 1), that this should remain true at the
boundary: does P
n≥1(−1)n−1/n equal log 2? (Notice this is the alternating harmonic series.) We
will return to this later.
In practice, if we want to show an inﬁnitely diﬀerentiable function equals its associated power
series P
n≥0(f(n)(0)/n!)xn on some interval around 0 we need some kind of error estimate for the
diﬀerence between f(x) and the polynomial PN
n=0(f(n)(0)/n!)xn. When the estimate goes to 0 as
N →∞we will have proved f(x) is equal to its power series.
Theorem 5.18. If f(x) is inﬁnitely diﬀerentiable then for all N ≥0
f(x) =
N
X
n=0
f(n)(0)
n!
xn + RN(x),
where
RN(x) = 1
N!
Z x
0
f(N+1)(t)(x −t)N dt.
Proof. When N = 0 the desired result says
f(x) = f(0) +
Z x
0
f′(t) dt.
This is precisely the fundamental theorem of calculus!

<!-- page 21 -->
INFINITE SERIES
21
We obtain the N = 1 case from this by integration by parts. Set u = f′(t) and dv = dt. Then
du = f′′(t) dt and we (cleverly!) take v = t −x (rather than just t). Then
Z x
0
f′(t) dt
=
f′(t)(t −x)

t=x
t=0
−
Z x
0
f′′(t)(t −x) dt
=
f′(0)x +
Z x
0
f′′(t)(x −t) dt,
so
f(x) = f(0) + f′(0)x +
Z x
0
f′′(t)(x −t) dt.
Now apply integration by parts to this new integral with u = f′′(t) and dv = (x −t) dt. Then
du = f(3)(t) dt and (cleverly) use v = −(1/2)(x −t)2. The result is
Z x
0
f′′(t)(x −t) dt = f′′(0)
2
x2 + 1
2
Z x
0
f(3)(t)(x −t)2 dt,
so
f(x) = f(0) + f′(0)x + f′′(0)
2!
x2 + 1
2
Z x
0
f(3)(t)(x −t)2 dt.
Integrating by parts several more times gives the desired result.
□
We call RN(x) a remainder term.
Corollary 5.19. If f is inﬁnitely diﬀerentiable then the following conditions at the number x are
equivalent:
• f(x) = P
n≥0(f(n)(0)/n!)xn,
• RN(x) →0 as N →∞.
Proof. The diﬀerence between f(x) and the Nth partial sum of its power series is RN(x), so f(x)
equals its power series precisely when RN(x) →0 as N →∞.
□
Example 5.20. In (5.4) we showed log(1 + x) equals P
n≥1(−1)n−1xn/n for |x| < 1. What about
at x = 1? For this purpose we want to show RN(1) →0 as N →∞when f(x) = log(1 + x). To
estimate RN(1) we need to compute the higher derivatives of f(x):
f′(x) =
1
1 + x, f′′(x) = −
1
(1 + x)2 , f(3)(x) =
2
(1 + x)3 , f(4)(x) = −
6
(1 + x)4 ,
and in general
f(n)(x) = (−1)n−1(n −1)!
(1 + x)n
for n ≥1. Therefore
RN(1) = 1
N!
Z 1
0
(−1)NN!
(1 + t)N+1 (1 −t)N dt = (−1)N
Z 1
0
(1 −t)N
(1 + t)N+1 dt,
so
|RN(1)|
≤
Z 1
0
dt
(1 + t)N+1
=
1
N −
1
N2N
→
0
as N →∞. Since the remainder term tends to 0, log 2 = P
n≥1(−1)n−1/n.

<!-- page 22 -->
22
KEITH CONRAD
Example 5.21. Let f(x) = sin x. Its power series is
X
n≥0
(−1)n
x2n+1
(2n + 1)! = x −x3
3! + x5
5! −x7
7! + · · · ,
which converges for all x by the ratio test. We will show sin x equals its power series for all x. This
is obvious if x = 0.
Since sin x has derivatives ± cos x and ± sin x, which are bounded by 1, for x > 0
|RN(x)|
=
1
N!

Z x
0
f(N+1)(t)(x −t)N dt

≤
1
N!
Z x
0
|x −t|N dt
≤
1
N!
Z x
0
xN dt
=
xN+1
N! .
This tends to 0 as N →∞, so sin x does equal its power series for x > 0.
If x < 0 then we can similarly estimate |RN(x)| and show it tends to 0 as N →∞, but we can
also use a little trick because we know sin x is an odd function: if x < 0 then −x > 0 so
sin x = −sin(−x) = −
X
n≥0
(−1)n (−x)2n+1
(2n + 1)!
from the power series representation of the sine function at positive numbers. Since (−x)2n+1 =
−x2n+1,
sin x = −
X
n≥0
(−1)n −x2n+1
(2n + 1)! =
X
n≥0
(−1)n
x2n+1
(2n + 1)!,
which shows sin x equals its power series for x < 0 too.
Example 5.22. By similar work we can show cos x equals its power series representation every-
where:
cos x =
X
n≥0
(−1)n x2n
(2n)! = 1 −x2
2! + x4
4! −x6
6! + · · · .
The power series for sin x and cos x look like the odd and even degree terms in the power series
for ex. Is the exponential function related to the trigonometric functions? This idea is suggested
because of their power series. Since ex has a series without the (−1)n factors, we can get a match
between these series by working not with ex but with eix, where i is a square root of −1. We have
not deﬁned inﬁnite series (or even the exponential function) using complex numbers. However,
assuming we could make sense of this then we would expect to have
eix
=
X
n≥0
(ix)n
n!
=
1 + ix −x2
2! −ix3
3! + x4
4! + ix5
5! + · · ·
=
1 −x2
2! + x4
4! + · · · i

x −x3
3! + x5
5! −· · ·

=
cos x + i sin x.

<!-- page 23 -->
INFINITE SERIES
23
For example, setting x = π would say
eiπ = −1.
Replacing x with −x in the formula for eix gives
e−ix = cos x −i sin x.
Adding and subtracting the formulas for eix and e−ix lets us express the real trigonometric functions
sin x and cos x in terms of (complex) exponential functions:
cos x = eix + e−ix
2
,
sin x = eix −e−ix
2i
.
Evidently a deeper study of inﬁnite series should make systematic use of complex numbers!
The following question is natural: who needs all the remainder estimate business from Theorem
5.18 and Corollary 5.19? After all, why not just compute the power series for f(x) and ﬁnd its
radius of convergence? That has to be where f(x) equals its power series. Alas, this is false.
Example 5.23. Let
f(x) =
(
e−1/x2,
if x ̸= 0,
0,
if x = 0.
It can be shown that f(x) is inﬁnitely diﬀerentiable at x = 0 and f(n)(0) = 0 for all n, so the power
series for f(x) has every coeﬃcient equal to 0, which means the power series is the zero function.
But f(x) ̸= 0 if x ̸= 0, so f(x) is not equal to its power series anywhere except at x = 0.
Example 5.23 shows that if a function f(x) is inﬁnitely diﬀerentiable for all x and the power
series P
n≥0(f(n)(0)/n!)xn converges for all x, f(x) need not equal its power series anywhere except
at x = 0 (where they must agree since the constant term of the power series is f(0)). This is why
there is non-trivial content in saying a function can be represented by its power series on some
interval. The need for remainder estimates in general is important.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*