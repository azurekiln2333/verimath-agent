# Irrationality of pi and e

> **Source**: https://kconrad.math.uconn.edu/blurbs/irrational.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
IRRATIONALITY OF π AND e
KEITH CONRAD
1. Introduction
Numerical estimates for π have been found in records of several ancient civilizations.
These estimates were all based on inscribing and circumscribing regular polygons around a
circle to get upper and lower bounds on the area (and thus upper and lower bounds on π
after dividing the area by the square of the radius). Such estimates are accurate to a few
decimal places. Around 1600, Ludolph van Ceulen gave an estimate for π to 35 decimal
places. He spent many years of his life on this calculation, using a polygon with 262 sides!
With the advent of calculus in the 17-th century, a new approach to the calculation of π
became available: inﬁnite series. For instance, if we integrate
1
1 + t2 = 1 −t2 + t4 −t6 + t8 −t10 + · · · ,
−1 < t < 1
from t = 0 to t = x when −1 < x < 1, then we ﬁnd
(1.1)
arctan x = x −x3
3 + x5
5 −x7
7 + x9
9 −x11
11 + · · · .
This is also true at x = 1, and since arctan 1 = π/4, we get
(1.2)
π
4 = 1 −1
3 + 1
5 −1
7 + 1
9 −1
11 + · · · ,
a result found by Leibniz in 1673 [2, pp. 247-248] and over 100 years earlier in India [9].1
Despite the beauty of (1.2), which expresses π in terms of the odd numbers, it converges far
too slowly to be numerically useful. For example, truncating the series at 1000 terms and
multiplying by 4 gives the estimate π ≈3.1405, which is only good to two decimal places.
Other formulas for π in terms of arctan values are (see Appendix C for details)
π
4 = arctan 1
2 + arctan 1
3
= 2 arctan 1
3 + arctan 1
7
= 4 arctan 1
5 −arctan 1
239.
The series in (1.1) converges more rapidly when x is smaller, so these other formulas lead
to good estimates of π. The last such calculation before computers was by Shanks [10] in
1873. He claimed to get π to 707 places. In the 1940s, the ﬁrst computer estimate for π
showed Shanks made an error in the 528-th digit, so his further calculations were wrong!
Our interest here is not to ponder ever more elaborate methods of estimating π, but
to prove something about the structure of this number: it is irrational. That is, π is not
a ratio of integers. The idea of the proof is to argue by contradiction. This is also the
1In 1671, Gregory discovered (1.1), but there is no indication he saw it gives a formula for π at x = 1.
1

<!-- page 2 -->
2
KEITH CONRAD
principle behind the simpler proof that the number
√
2 is irrational. However, there is an
essential diﬀerence between proofs that
√
2 is irrational and proofs that π is irrational. One
can prove
√
2 is irrational using only algebraic manipulations with a hypothetical rational
expression for
√
2 to reach a contradiction. But all known proofs of the irrationality of π
are based on techniques from calculus, which can be used to prove irrationality of other
numbers, such as e and rational powers of e (aside from e0 = 1).
The remaining sections are organized as follows. In Section 2, we prove π is irrational
with deﬁnite integrals. Irrationality of e is proved by inﬁnite series in Section 3. A general
discussion about irrationality proofs is in Section 4, and we apply those ideas to prove
irrationality of nonzero rational powers of e in Section 5. In Section 6 we introduce complex
numbers into a proof from Section 5 in order to obtain another proof that π is irrational.
2. Irrationality of π
The ﬁrst proof that π is irrational is due to Lambert [7] in 1761. His proof involves an
analytic device that is not covered in calculus courses: continued fractions. (A discussion of
this work is in [5, pp. 68–78].) The irrationality proof for π we give here is due to Niven [8]
and uses integrals instead of continued fractions.
Theorem 2.1. The number π is irrational.
Proof. For a nice function f(x), a double integration by parts shows
Z
f(x) sin x dx = −f(x) cos x + f′(x) sin x −
Z
f′′(x) sin x dx.
Therefore (using sin(0) = 0, cos(0) = 1, sin(π) = 0, and cos(π) = −1),
Z π
0
f(x) sin x dx = (f(0) + f(π)) −
Z π
0
f′′(x) sin x dx.
In particular, if f(x) is a polynomial of even degree, say 2n, then repeating this calculation
n times (or reasoning by induction) gives us
(2.1)
Z π
0
f(x) sin x dx = F(0) + F(π),
where F(x) = f(x) −f′′(x) + f(4)(x) −· · · + (−1)nf(2n)(x).
To prove π is irrational, we argue by contradiction. Assume π = p/q for positive integers
p and q (since π > 0). We are going to apply (2.1) to a carefully (and mysteriously!) chosen
polynomial f(x) and wind up with an integer that lies between 0 and 1. No such integer
exists, so we have a contradiction and therefore π is irrational.
For a positive integer n, set
(2.2)
fn(x) = qn xn(π −x)n
n!
= xn(p −qx)n
n!
.
This polynomial of degree 2n depends on n (and on π!). We are going to apply (2.1) to this
polynomial and ﬁnd a contradiction when n becomes large.
Before working out the consequences of (2.1) for f(x) = fn(x), we note the polynomial
fn(x) has two important properties:
• for 0 < x < π, fn(x) is positive and (when n is large) very small,
• all the derivatives of fn(x) at x = 0 and x = π are integers.

<!-- page 3 -->
IRRATIONALITY OF π AND e
3
To show the ﬁrst property is true, the positivity of fn(x) for 0 < x < π is immediate from
its deﬁning formula. To bound fn(x) from above when 0 < x < π, note that 0 < π −x < π,
so 0 < x(π −x) < π2. Therefore
(2.3)
0 < fn(x) ≤qn
π2n
n!

= (qπ2)n
n!
.
The upper bound tends to 0 as n →∞, so the upper bound is less than 1 for large n.
To show the second property is true, ﬁrst take x = 0. The coeﬃcient of xj in fn(x) is
f(j)
n (0)/j!. Since fn(x) = xn(p −qx)n/n! and p and q are integers, the binomial theorem
tells us the coeﬃcient of xj can also be written as cj/n! for an integer cj. Therefore
(2.4)
f(j)
n (0) = j!
n!cj.
Since fn(x) has its lowest degree nonvanishing term in degree n, cj = 0 for j < n, so
f(j)
n (0) = 0 for j < n. For j ≥n, j!/n! is an integer, so f(j)
n (0) is an integer by (2.4).
To see the derivatives of fn(x) at x = π are also integers, we use the identity fn(π −x) =
fn(x). Diﬀerentiate both sides j times and set x = 0 to get (−1)jf(j)
n (π) = f(j)
n (0) for all j.
Therefore, since the right side is an integer, the left side is an integer too. This concludes
the proof of the two important properties of fn(x).
Now look at (2.1) when f = fn. All derivatives of fn at 0 and π are integers, so the right
side of (2.1) is an integer when f = fn (see the deﬁnition of F(x)). Thus
R π
0 fn(x) sin x dx is
an integer for each n. Since fn(x) and sin x are positive on (0, π), this integral is a positive
integer. However, when n is large, |fn(x) sin x| ≤|fn(x)| ≤(qπ2)n/n! by (2.3). As n →∞,
(qπ2)n/n! →0. Therefore
R π
0 fn(x) sin x dx is a positive integer less than 1 when n is very
large. This is a contradiction, so π is irrational.
□
This proof is quite puzzling. How did Niven choose the polynomials fn(x) or know to
compute the integral (2.1)? Here is a reworking of Niven’s proof in terms of recursions, due
to Markov and Zhou [15].
Proof. Set
(2.5)
In =
Z π
0
(x(π −x))n
n!
sin x dx.
The integrand is continuous and positive on (0, π), so In > 0. By explicit calculation, I0 = 2
and I1 = 4:
I0 =
Z π
0
sin x dx = −cos x

π
0
= −(−1) + 1 = 2
and using integration by parts,
I1 =
Z π
0
(πx −x2) sin x dx
= π
Z π
0
x sin x dx −
Z π
0
x2 sin x dx
= π(−x cos x + sin x)

π
0
−(−x2 cos x + 2x sin x + 2 cos x)

π
0
= π(−π(−1) −0) −((−π2(−1) + 0 −2) −2)
= 4.

<!-- page 4 -->
4
KEITH CONRAD
Using integration by parts twice, for n ≥2 we have In = (4n −2)In−1 −π2In−2. (This is
worked out in Appendix A.) Using that recursion and the initial values I0 = 2 and I1 = 4,
explicit values of In for small n can be worked out. The table below gives results for n ≤6.
n
In
0
2
1
4
2
−2π2 + 24
3
−24π2 + 240
4
2π4 −360π2 + 3360
5
60π4 −6720π2 + 60480
6
−2π6 + 1680π4 −151200π2 + 1330560
This suggests we can always write In in the form
(2.6)
In = cn,nπn + cn−1,nπn−1 + · · · + c1,nπ + c0,n.
for some integers c0,n, . . . , cn,n, and it’s left to the reader to prove this by induction using
the recursion for In and its ﬁrst two values.
Now assume π is rational, so π = p/q for some positive integers p and q. By (2.6), qnIn =
Pn
k=0 ck,nqnπk = Pn
k=0 ck,nqn−kpk ∈Z. Since In > 0, we have qnIn ∈Z+. At the same
time, since |x(π −x)| ≤π2 for 0 ≤x ≤π we have the bound |qnIn| ≤qn R π
0 ((π2)n/n!) dx =
π((qπ2)n/n!), so In →0 as n →∞. This contradicts qnIn being a positive integer for all n,
so we have a contradiction. Thus π is irrational.
□
3. Irrationality of e
We turn now to a proof that e is irrational. This was ﬁrst established by Euler [3] in
1737 using continued fractions. We will prove the irrationality in a more direct manner,
using inﬁnite series, by an argument of Fourier from 1815.2
Theorem 3.1. The number e is irrational.
Proof. Write
e = 1 + 1 + 1
2! + 1
3! + · · · .
For a positive integer n,
e =

1 + 1 + 1
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
1 + 1 + 1
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
The second term in parentheses is positive and less than the geometric series
1
n + 1 +
1
(n + 1)2 +
1
(n + 1)3 + · · · = 1
n.
Therefore
(3.1)
0 < e −

1 + 1 + 1
2! + 1
3! + · · · + 1
n!

<
1
n · n!.
2While the proof of Fourier appeared in [13, pp. 339-341] in 1815, it was not written by him. It is
attributed to Fourier right after the proof.

<!-- page 5 -->
IRRATIONALITY OF π AND e
5
Write 1 + 1 + 1/2! + · · · + 1/n! in (3.1) as a fraction with common denominator n!: it is
pn/n! with pn ∈Z, so (3.1) says 0 < e −pn/n! < 1/(n · n!). Clear the denominator n! to get
(3.2)
0 < n!e −pn < 1
n.
So far everything we have done involves no unproved assumptions. Now we introduce the
rationality assumption. If e is rational, then e = a/b for positive integers a and b, and
n!e = n!a/b = (n!/b)a is an integer when n is large, since n!/b is an integer once n ≥b.
That makes n!e −pn = (n!/b)a −pn an integer inside the open interval (0, 1/n) by (3.2),
which is absurd since 1/n ≤1. We have a contradiction, so e is irrational.
□
Remark 3.2. We can prove Theorem 3.1 in a manner similar to the second proof of
irrationality of π, by using the integrals
(3.3)
Jn =
Z 1
0
(x(1 −x))n
n!
ex dx,
which are positive since the integrand is positive when 0 < x < 1. If 0 ≤x ≤1, then
0 ≤x(1 −x) ≤1 and ex ≤e, so Jn ≤
R 1
0 (e/n!) dx ≤e/n!. We have J0 = e −1, J1 = −e + 3,
and Jn = −(4n −2)Jn−1 + Jn−2 for n ≥2 using integration by parts (see Appendix A for
details). Further values are J2 = 7e−19 and J3 = −71e+193. Quite generally, Jn = ane+bn
for some integers an and bn, so if e is rational with e = p/q for some p and q in Z+, then
qJn = anp + bnq is an integer for all n. It’s positive since q and Jn are, and qJn < qe/n!,
which is less than 1 for large n. Thus qJn is an integer between 0 and 1 for large n, which
is a contradiction.
4. General Ideas
It’s time to think more systematically. A basic principle we need to understand is that
numbers can be proved to be irrational if they can be approximated “too well” by rationals.
Of course each number can be approximated arbitrarily closely by rational numbers: use a
truncated decimal expansion. For instance, we can approximate
√
2 = 1.41421356... by
(4.1)
14142
10000 = 1.4142,
1414213
1000000 = 1.414213.
With truncated decimals, we achieve close estimates at the expense of rather large denom-
inators. To see what this is all about, compare the above approximations with
(4.2)
99
70 = 1.41428571...,
1393
985 = 1.41421319...,
where we have achieved just as close an approximation with much smaller denominators
(e.g., the second one is accurate to 6 decimal places with a denominator of only 3 digits).
These rational approximations to
√
2 are, in the sense of denominators, much better than
the ones we ﬁnd from decimal truncation.
To measure the “quality” of an approximation of a real number α by a rational number
p/q, we should think not about the diﬀerence |α −p/q| being small in an absolute sense,
but about the diﬀerence being substantially smaller than 1/q (thus tying the error with the
size of the denominator in the approximation). In other words, we want
|α −p/q|
1/q
= q
α −p
q
 = |qα −p|
to be small in an absolute sense.

<!-- page 6 -->
6
KEITH CONRAD
Measuring the approximation of α by p/q using |qα−p| rather than |α−p/q| admittedly
takes some getting used to, if you are new to the idea. Consider what it says about our
approximations to
√
2. For example, from (4.1) we have
|10000
√
2 −14142| = .135623,
|1000000
√
2 −1414213| = .562373,
and these are not small when measured against 1/10000 = .0001 or 1/1000000 = .000001.
On the other hand, from the approximations to
√
2 in (4.2) we have
|70
√
2 −99| = .005050,
|985
√
2 −1393| = .000358,
which are small when measured against 1/70 = .014285 and 1/985 = .001015. We see
vividly that 99/70 and 1393/985 really should be judged as “good” rational approximations
to
√
2 while the decimal truncations are “bad” rational approximations to
√
2.
The importance of this point of view is that it gives us a general strategy for proving
numbers are irrational, as follows.
Theorem 4.1. Let α ∈R. If there is a sequence of integers pn, qn such that qnα −pn ̸= 0
and |qnα −pn| →0 as n →∞, then α is irrational.
In other words, if α admits a “very good” sequence of rational approximations, then α
must be irrational.
Proof. Since 0 < |qnα −pn| < 1 for large n, by hypothesis, we must have qn ̸= 0 for large
n. Therefore, since only large n is what matters, we may change terms at the start and
assume qn ̸= 0 for all n.
To prove α is irrational, suppose it is rational: α = a/b, where a and b are integers with
b ̸= 0. Then
α −pn
qn
 =

a
b −pn
qn
 =

qna −pnb
bqn
 .
Clearing the denominator qn,
|qnα −pn| =

qna −pnb
b
 .
Since this is not zero, the integer qna −pnb is nonzero. Therefore |qna −pnb| ≥1, so
|qnα −pn| ≥1
|b|.
This positive lower bound contradicts |qnα −pn| tending to 0, so α is irrational.
□
It turns out the condition in Theorem 4.1 is not just suﬃcient to prove irrationality, but
it is also necessary: if α is irrational then there is a sequence of integers pn, qn such that
|qnα −pn| is not zero and tends to 0 as n →∞. We will not have a need for this necessity
(except maybe for its psychological boost) and therefore omit the proof. See [6, p. 277].
Of course, to use Theorem 4.1 to prove irrationality of a number α we need to ﬁnd the
integers pn and qn. For the number e, these integers can be found directly from truncations
to the inﬁnite series for e, as we saw in (3.2).
In other words, rather than saying e is
irrational because the proof of Theorem 3.1 shows in the end that rationality of e leads
to an integer between 0 and 1, we can say e is irrational because the proof of Theorem
3.1 exhibits a sequence of good rational approximations to e. In other words, the proof of
Theorem 3.1 can stop at (3.2) and then appeal to Theorem 4.1.

<!-- page 7 -->
IRRATIONALITY OF π AND e
7
While other powers of e are also irrational, it is not feasible to prove their irrationality
by adapting the proof of Theorem 3.1. For instance, what happens if we try to prove e2
is irrational from taking truncations of the inﬁnite series e2 = P
k≥0 2k/k!? Writing the
truncated sum Pn
k=0 2k/k! in reduced form as, say, an/bn, numerical data suggest bne2 −an
does not tend to 0, (For example, the value of bne2 −an at n = 22, 23, and 24 is roughly
.0026, 1.4488, and .3465. Since the corresponding values of bn have 12, 16, and 17 decimal
digits, these diﬀerences are not small by comparison with 1/bn, so the approximations an/bn
to e2 are not that good.) Thus, these rational approximations to e2 probably won’t ﬁt the
conditions of Theorem 4.1 to let us prove the irrationality of e2. (However, a well-chosen
subsequence of the partial sums does work. See Appendix B.)
5. Irrationality of rational powers of e
To ﬁnd good rational approximations to positive integral powers of e (good enough, that
is, to establish irrationality of those powers), we will not use a series expansion, but rather
use the interaction between ex and integration. Some of the mysterious ideas from Niven’s
proof of the irrationality of π will show up in this context.
We will use Theorem 4.1 to prove the following generalization of the irrationality of e.
Theorem 5.1. For every positive integer a, ea is irrational.
Before we prove Theorem 5.1, we note two immediate corollaries.
Corollary 5.2. When r is a nonzero rational number, er is irrational.
Proof. Since e−r = 1/er, it suﬃces to take r > 0. Then r = a/b for positive integers a and b.
If er is rational, so is (er)b = ea, but this contradicts Theorem 5.1. Thus er is irrational.
□
Corollary 5.3. For each positive rational number r ̸= 1, ln r is irrational.
Proof. The number ln r is nonzero. If ln r is rational, then Corollary 5.2 tells us eln r is
irrational. But eln r = r is rational. We have a contradiction, so ln r is irrational.
□
The proof of Theorem 5.1 will use the following lemma, which tells us how to integrate
e−xf(x) when f(x) is a polynomial.
Lemma 5.4 (Hermite). Let f(x) be a polynomial of degree m ≥0. For every real number
a > 0,
Z a
0
e−xf(x) dx =
m
X
j=0
f(j)(0) −e−a
m
X
j=0
f(j)(a).
Proof. We compute
R
e−xf(x) dx by integration by parts, taking u = f(x) and dv = e−xdx.
Then du = f′(x)dx and v = −e−x, so
Z
e−xf(x) dx = −e−xf(x) +
Z
e−xf′(x) dx.
Repeating this process on the new indeﬁnite integral, we eventually obtain
Z
e−xf(x) dx = −e−x
m
X
j=0
f(j)(x).
Now evaluate the right side at x = a and x = 0 and subtract.
□

<!-- page 8 -->
8
KEITH CONRAD
Remark 5.5. It is interesting to make a special case of this lemma explicit: for f(x) = xn,
Z a
0
e−xxn dx = n! −1
ea
n
X
j=0
n(n −1) · · · (n −j + 1)an−j.
Letting a →∞(n is ﬁxed), the second term on the right tends to 0, so
R ∞
0 e−xxn dx = n!.
This integral formula for n! is due to Euler.
Now we prove Theorem 5.1.
Proof. Rewrite Hermite’s lemma (Lemma 5.4) by multiplying through by ea:
(5.1)
ea
Z a
0
e−xf(x) dx = ea
m
X
j=0
f(j)(0) −
m
X
j=0
f(j)(a).
Equation (5.1) is valid for every positive number a and polynomial f(x). Let a be a positive
integer at which ea is assumed to be rational. We want to use for f(x) a polynomial (actually,
a sequence of polynomials fn(x)) with two properties:
• the left side of (5.1) is positive and (when n is large) very small,
• all the derivatives of the polynomial at x = 0 and x = a are integers.
Then the right side of (5.1) will have the properties of the diﬀerences qnα −pn in Theorem
4.1, with α = ea and the two sums on the right side of (5.1) being pn and qn.
Our choice of f(x) is
(5.2)
fn(x) = xn(x −a)n
n!
,
where n ≥1 is to be determined.
(Note the similarity with (2.2) in the proof of the
irrationality of π!) In other words, we consider the equation
(5.3)
ea
Z a
0
e−xfn(x) dx = ea
2n
X
j=0
f(j)
n (0) −
2n
X
j=0
f(j)
n (a).
We can see (5.3) is positive by looking at the left side. The number a is positive and the
integrand e−xfn(x) = e−xxn(x −a)n/n! on the interval (0, a) is positive, so the integral is
positive. Now we estimate the size of (5.3) by estimating the integral on the left side. By
the change of variables x = ay on the left side of (5.3),
Z a
0
e−xfn(x) dx = a2n+1
Z 1
0
e−ay yn(y −1)n
n!
dy,
so we can bound the left side of (5.3) from above by
0 < ea
Z a
0
e−xfn(x) dx ≤eaa2n+1
n!
Z 1
0
e−ay dy.
As a function of n, this upper bound is a constant times (a2)n/n!. As n →∞, this bound
tends to 0.
To see that, for each integer n ≥1, the derivatives f(j)
n (0) and f(j)
n (a) are integers for every
j ≥0, ﬁrst note that the equation fn(a −x) = fn(x) tells us after repeated diﬀerentiation
that (−1)jf(j)
n (a) = f(j)
n (0). Therefore it suﬃces to show all the derivatives of fn(x) at
x = 0 are integers. The proof that all f(j)
n (0) are integers is just like that in the proof of
Theorem 2.1, so the details are left to the reader to check. (The general principle is this:

<!-- page 9 -->
IRRATIONALITY OF π AND e
9
for a polynomial g(x) that has integer coeﬃcients and is divisible by xn, all derivatives of
g(x)/n! at x = 0 are integers.)
The ﬁrst property of the fn’s tells us that qnea −pn is positive, where pn = P2n
j=0 f(j)
n (a)
and qn = P2n
j=0 f(j)
n (a), and qnea −pn tends to 0 as n →∞. The second property of the
fn’s tells us that pn and qn are integers. Therefore the hypotheses of Theorem 4.1 are met,
so ea is irrational.
□
What really happened in this proof? We actually wrote down some very good rational
approximations to ea. They came from values of the polynomial
Fn(x) =
2n
X
j=0
f(j)
n (x).
Indeed, Theorem 5.1 tells us Fn(a)/Fn(0) is a “good” rational approximation to ea when n
is large. (The dependence of Fn(x) on a is hidden in the formula for fn(x).) The following
table illustrates this for a = 2, where the entry at n = 1 is pretty bad since F1(0) = 0.
n
|Fn(0)e2 −Fn(2)|
1
4
2
1.5562
3
.43775
4
.09631
5
.01739
6
.00266
7
.00035
8
.00004
If we take a = 1, the rational approximations we get for ea = e by this method are
diﬀerent from the partial sums Pn
k=0 1/k!.
Although the proofs of Theorems 2.1 and 5.1 are similar in the sense that both used
estimates on integrals, the proof of Theorem 2.1 did not show π is irrational by exhibiting a
sequence of good rational approximations to π. The proof of Theorem 2.1 was an “integer
between 0 and 1” proof by contradiction.
No good rational approximations to π were
produced in that proof. It is simply harder to get our grips on π than it is on powers of e.
Remark 5.6. The irrationality of er for positive rational r can be proved by an “integer be-
tween 0 and 1” method, as indicated in [15]: use the integrals Jn,r =
R r
0 (x(r−x))n/n! ex dx,
the bounds 0 < Jn,r < (r2n/n!)rer, and the recursion Jn,r = −(4n −2)Jn−1,r + r2Jn−2,r
for n ≥2. Show from the recursion that Jn,r = an(r)er + bn(r) where an(r) and bn(r) are
polynomials in r with integral coeﬃcients of degree at most n. Write r = A/B for positive
integers A and B. If er is rational, say er = p/q, then the formula for Jn,r in terms of er
implies BnqJn,r is a positive integer that’s at most q(Br2)n/n!, which is impossible for large
n since q(Br2)n/n! →0 as n →∞.
6. Returning to irrationality of π
The proof of Theroem 5.1 gives a broader context for the proof in Theorem 2.1 that π
is irrational. In fact, by thinking about Theorem 5.1 in the complex plane, we are led to a
slightly diﬀerent proof of Theorem 2.1.

<!-- page 10 -->
10
KEITH CONRAD
Proof. We are going to use Hermite’s lemma for complex a, where integrals from 0 to a are
obtained using a path of integration between 0 and a (such as the straightline path). The
deﬁnition of ea for complex a is the inﬁnite series P
n≥0 an/n!. In particular, for real t,
breaking up the series for eit into its real and imaginary parts yields
eit = cos t + i sin t.
Thus |eit| = 1 and eiπ = −1. Consider Hermite’s lemma at a = iπ:
(6.1)
Z iπ
0
e−xf(x) dx =
m
X
j=0
f(j)(0) +
m
X
j=0
f(j)(iπ).
Extending (5.2) to the complex plane, we will use in (6.1) f(x) = fn(x) = xn(x −iπ)n/n!
for some large n to be determined later (so m = 2n as before). To put (6.1) in a more
appealing form, we apply the change of variables x = iπy. The left side of (6.1) becomes
(6.2)
Z iπ
0
e−xfn(x) dx = i(−1)nπ2n+1
Z 1
0
e−iπy yn(y −1)n
n!
dy.
Let gn(y) = yn(y −1)n/n! (which does not involve i or π), so fn(iπy) = (iπ)2ngn(y) and
diﬀerentiating j times gives
(6.3)
(iπ)jf(j)
n (iπy) = (iπ)2ng(j)
n (y).
Feeding (6.2) and (6.3) into (6.1), with f = fn,
(6.4)
i(−1)nπ2n+1
Z 1
0
e−iπygn(y) dy =
2n
X
j=0
(iπ)2n−jg(j)
n (0) +
2n
X
j=0
(iπ)2n−jg(j)
n (1).
This is the key equation in the proof. It serves the role for us now that (5.3) did in the
proof of irrationality of powers of e. Notice the numbers g(j)
n (0) and g(j)
n (1) are all integers.
Suppose (at last) that π is rational, say with positive denominator q. For j < n, g(j)
n (x)
vanishes at x = 0 and x = 1, so the sums in (6.4) really only need to start at j = n. That
means the largest power of π in the (nonzero) terms on the right side of (6.4) is πn, so the
largest denominator on the right side of (6.4) is qn. Multiply both sides by qn:
(6.5)
i(−q)nπ2n+1
Z 1
0
e−iπygn(y) dy =
2n
X
j=0
(iπ)2n−jqng(j)
n (0) +
2n
X
j=0
(iπ)2n−jqng(j)
n (1).
We estimate the left side of (6.5). Since |eiπy| = 1, an estimate of the left side is
qnπ2n+1
Z 1
0
e−iπygn(y) dy
 ≤qnπ2n+1
n!
= π(qπ2)n
n!
.
As n →∞, this bound tends to 0.
On the other hand, since the nonzero terms in the sums on the right side of (6.5) only
start showing up at the j = n term, and π2n−jqn ∈Z for n ≤j ≤2n, the right side of (6.5)
is in the integral lattice Z + Zi. It is nonzero, as we see by looking at the real part of the
left side of (6.5), which is
(−q)nπ2n+1
Z 1
0
sin(πy)gn(y) dy = (−q)nπ2n+1
Z 1
0
sin(πy)yn(y −1)n
n!
dy.

<!-- page 11 -->
IRRATIONALITY OF π AND e
11
The integrand here has constant sign on (0, 1), so (6.5) is in Z + Zi and doesn’t vanish for
integers n ≥1 since the real part is not 0. A sequence of nonzero elements of Z + Zi can’t
tend to 0. We have a contradiction, so π is irrational.
□
We used complex numbers in the above proof to stress the close connection to the proof
of Theorem 5.1. If you take the real part of every equation in the above proof (especially
starting with (6.4)), then you will ﬁnd a proof of the irrationality of π that avoids complex
numbers. (For instance, we showed (6.5) is nonzero by looking only at the real part, so
taking real parts everywhere should not damage the logic of the proof.) By taking real
parts, the goal of the proof changes slightly. Instead of showing the rationality of π leads
to a nonzero element of Z + Zi with absolute value less than 1, showing the rationality of π
leads to a nonzero integer with absolute value less than 1. Is such a “real” proof basically
the same as the ﬁrst proof we gave that π is rational? As a check, try to adapt the ﬁrst
proof of Theorem 2.1 to get the following.
Corollary 6.1. The number π2 is irrational.
Proof. Run through the previous proof, starting at (6.4), but now assume π2 is rational
with denominator q ∈Z. While it is no longer true that π2n−jqn ∈Z for n ≤j ≤2n, we
instead have π2n−jqn ∈Z for j even and π2n−jqn ∈(1/π)Z for j odd. Since i2n−j is real
when j is even and imaginary when j is odd, we now have (6.5) lying in the set Z + Z(i/π),
whose nonzero elements are not arbitrarily small.
□
If you write up all the details in this proof and take the real part of every equation, you
will have the proof of the irrationality of π in [12, Chap. 16].
The numbers π and e are not just irrational, but transcendental. That is, neither number
is the root of a nonzero polynomial with rational coeﬃcients.
(For comparison,
√
2 is
irrational but it is a solution of x2 −2 = 0, so it is in some sense linked to the rational
numbers through this equation.) Proofs of their transcendence can be found in [1, Chap. 1],
[4, Chap. II], and [11, Chap. 2].
There is a proof that e is transcendental that is not
too much more complicated than our proof of Theorem 5.1. The idea is to use Hermite’s
lemma and a construction of a sequence of rational functions whose values give good rational
approximations simultaneously to several integral powers of e, not only to one power like ea.3
The construction of such rational functions generalizes the fn(x)’s in Theorem 5.1, which
gave good rational approximations to ea. By comparison to this, proving transcendence of
π is much more involved than proving its irrationality.
Historically, progress on π always trailed that of e. Euler proved e is irrational in 1737,
and Lambert proved irrationality of non-zero rational powers of e and irrationality of π in
1761. Their proofs used continued fractions, not integrals. (Lambert’s proof for π was really
a result about values of tan x: when r is a nonzero rational number where tan r is deﬁned,
Lambert proved tan r is irrational. Then by tan(π/4) = 1, π/4 must be irrational, so π is
irrational.) Transcendence proofs for e and π came 100 years later, in the work of Hermite
(1873) and Lindemann (1882). In addition to e and π, the numbers 2
√
2, log 2, and eπ are
known to be transcendental. The status of 2e, πe, π
√
2, e + π, e log 2, and Euler’s constant
γ = limn→∞
Pn
k=1 1/k −log n is still open. Surely these numbers are all transcendental,
but it is not yet proved that even one of them is irrational.
3See https://kconrad.math.uconn.edu/blurbs/analysis/transcendence-e.pdf.

<!-- page 12 -->
12
KEITH CONRAD
Appendix A. Recursions using integration by parts
For the integrals
In =
Z π
0
(x(π −x))n
n!
sin x dx
and
Jn =
Z 1
0
(x(1 −x))n
n!
ex dx
that were met in (2.5) and (3.3), we want to derive the recursions
(A.1)
In = (4n −2)In−1 −π2In−2
and
Jn = −(4n −2)Jn−1 + Jn−2
for n ≥2 using integration by parts.
Letting fn(x) = (x(π−x))n
n!
, we have f′
n(x) = (x(π−x))n−1
(n−1)!
(π −2x), so fn(0) = fn(π) = 0 for
n ≥1 and f′
n(0) = f′
n(π) = 0 for n ≥2. Therefore by integration by parts where u = fn(x)
and dv = sin x dx, so du = f′
n(x) dx and v = −cos x,
Z π
0
(x(π −x))n
n!
sin x dx =
Z π
0
fn(x) sin x dx
= −fn(x) cos x

π
0
+
Z π
0
f′
n(x) cos x dx
=
Z π
0
f′
n(x) cos x dx.
By integration by parts where u = f′
n(x) and dv = cos x dx, so du = f′′
n(x) dx and v = sin x,
Z π
0
f′
n(x) cos x dx =f′
n(x) sin x

π
0
−
Z π
0
f′′
n(x) sin x dx = −
Z π
0
f′′
n(x) sin x dx.
Combining these,
In =
Z π
0
fn(x) sin x dx =
Z π
0
f′
n(x) cos x dx = −
Z π
0
f′′
n(x) sin x dx.
We can write f′′
n(x) in terms of fn−1(x) and fn−2(x):
f′′
n(x) = (f′
n(x))′
=
(x(π −x))n−1
(n −1)!
(π −2x)
′
= (x(π −x))n−1
(n −1)!
(−2) + (x(π −x))n−2
(n −2)!
(π −2x)2
= −2fn−1(x) + (π −2x)2fn−2(x).
Since (π −2x)2 = π2 −4πx + 4x2 = π2 −4x(π −x),
f′′
n(x) = −2fn−1(x) + π2fn−2(x) −4x(π −x)(x(π −x))n−2
(n −2)!
= −2fn−1(x) + π2fn−2(x) −4(n −1)fn−1(x)
= −(4n −2)fn−1(x) + π2fn−2(x).
(A.2)
Multiply by sin x and integrate over [0, π] to get the recursion for In in (A.1):
In = −
Z π
0
f′′
n(x) sin x dx =
Z π
0
((4n−2)fn−1(x)−π2fn−2(x)) sin x dx = (4n−2)In−1−π2In−2.

<!-- page 13 -->
IRRATIONALITY OF π AND e
13
Switching to Jn, let gn(x) = (x(1−x))n
n!
, so Jn =
R 1
0 gn(x)ex dx. Since gn and g′
n vanish
at 0 and 1 when n ≥2, Jn =
R 1
0 g′′
n(x)ex dx (not −
R 1
0 g′′
n(x) dx) after integrating by parts
twice. The analogue of (A.2) for gn is
g′′
n(x) = −(4n −2)gn−1(x) + gn−2(x),
so multiplying by ex and integrating over [0, 1] gives us Jn = −(4n −2)Jn−1 + Jn−2.
Appendix B. Irrationality of e2
In Section 4, we saw that the partial sums of the Taylor series for ex at x = 2, namely the
sums Pn
k=0 2k/k!, do not seem to be a sequence of rational approximations to e2 that allow
us to prove e2 is irrational via Theorem 4.1. This was circumvented in Theorem 5.1, where
the nonzero integral powers of e (not just e2) were proved to be irrational using rational
approximations coming from something other than the Taylor series for ex. What we will
show here is that the partial sums Pn
k=0 2k/k! can, after all, be used to prove irrationality
of e2 by focusing on a certain subsequence of the partial sums and exploiting a peculiar
property of 2. The argument we give is due to Benoit Cloitre.
Write Pn
k=0 2k/k! in reduced form as an/bn. Then e2 > an/bn, so bne2 −an > 0. While
numerical data suggest bne2 −an does not go to 0 as n →∞, it turns out that these nonzero
diﬀerences tend to 0 as n runs through the powers of 2. The table below has some limited
evidence in this direction.
n
bne2 −an
2
2.389
4
.3890
8
.5526
16
.0881
32
.0006
64
.0211
128
.0005
256
.0001
If these diﬀerences do tend to 0, then this proves e2 is irrational by Theorem 4.1. To
prove this phenomenon is real, we use Lagrange’s form of the remainder to estimate the
diﬀerence between e2 and Pn
k=0 2k/k! before setting n to be a power of 2. Lagrange’s form
of the remainder says: for an inﬁnitely diﬀerentiable function f and integer n ≥0,
f(x) =
n
X
k=0
f(k)(0)
k!
xk + f(n+1)(c)
(n + 1)! xn,
where c is between 0 and x. Taking f to be the exponential function and x = 2,
e2 =
n
X
k=0
2k
k! +
ec2n
(n + 1)!,
where 0 < c < 2. Bring the sum to the left side, multiply by n!/2n, and take absolute
values:
(B.1)

n!
2n e2 −n!
2n
n
X
k=0
2k
k!
 ≤
e2
n + 1.

<!-- page 14 -->
14
KEITH CONRAD
Set
cn = n!
2n
n
X
k=0
2k
k! ,
dn = n!
2n ,
so cn/dn = Pn
k=0 2k/k! = an/bn and (B.1) says |dne2−cn| ≤e2/(n+1). Thus |dne2−cn| →0
as n →∞and dne2−cn ̸= 0. Be careful: the numbers cn and dn are not themselves integers
(as we will see), so the expression |dne2 −cn| is not quite in a form suitable for immediate
application of Theorem 4.1. But we can get good control on the denominators of cn and
dn.
Writing cn = (1/2n) Pn
k=0(n!/k!)2k, since n!/k! is an integer cn is an integer divided by
2n, so cn has a 2-power denominator in reduced form. Since dn is an integer divided by 2n,
its reduced form denominator is also a power of 2. What are the powers of 2 in the reduced
form for cn and dn?
For a nonzero rational number r, write ord2(r) for the power of 2 appearing in r,
e.g., ord2(40) = 3 and ord2(21/20) = −2.
By unique prime factorization, ord2(rr′) =
ord2(r)+ord2(r′) for nonzero rationals r and r′. Another important formula is ord2(r+r′) =
min(ord2(r), ord2(r′)) when ord2(r) ̸= ord2(r′) and r + r′ ̸= 0. (These properties both re-
semble the degree on polynomials and rational functions, except the degree has a max where
ord2 has a min on sums.)
We want to compute ord2(cn) and ord2(dn). As dn = n!/2n is simpler than cn, we look at
it ﬁrst. Since ord2(dn) = ord2(n!/2n) = ord2(n!) −n, we bring in a formula for the highest
power of 2 in a factorial, due to Legendre: ord2(n!) = n −s2(n), where s2(n) is the sum of
the base 2 digits of n. For example, 6! = 24 · 32 · 5 and 6 = 2 + 22, so 6 −s2(6) = 6 −2 = 4
matches ord2(6!). With this formula of Legendre,
ord2(dn) = ord2(n!) −n = (n −s2(n)) −n = −s2(n).
For n ≥1 this is negative (there is at least one nonzero base 2 digit in n, so s2(n) ≥1),
which proves dn is not an integer.
What about ord2(cn)? Writing
cn =
n
X
k=0
n!2k
2nk! = n!
2n + n! · 2
2n · 1 + n! · 4
2n · 2 + n! · 23
2n · 6 + · · · + 1,
each term has at worst a 2-power denominator since n!/k! ∈Z when 0 ≤k ≤n. To ﬁgure
out the power of 2 in the denominator we will compute ord2(n!2k/2nk!). For k = 0 this is
ord2(n!/2n) = −s2(n). For k ≥1 this is
ord2(n!) + k −n −ord2(k!) = −s2(n) + s2(k) > −s2(n)
since s2(k) ≥1.
Therefore every term in the sum for cn beyond the k = 0 term has
a larger 2-power divisibility than the k = 0 term, which means ord2(cn) is the same as
ord2(n!/2n) = −s2(n). In other words, cn and dn have the same denominator: 2s2(n).
If we let n be a power of 2 then cn and dn have denominator 21 = 2, so 2cn and 2dn are
integers. Then the estimate
0 < |2dne2 −2cn| = 2|dne2 −cn| ≤
2e2
n + 1 →0
proves e2 is irrational by Theorem 4.1.
It is natural to ask if the same argument yields a proof that ep is irrational for prime
p > 2 using the Taylor series for ex at x = p. Let cn = (n!/pn) Pn
k=0 pk/k! and dn = n!/pn,

<!-- page 15 -->
IRRATIONALITY OF π AND e
15
so |dnep −cn| ≤ep/(n + 1) as before. Legendre’s formula for ordp(n!), the highest power
of p in n!, is (n −sp(n))/(p −1), where sp(n) is the sum of the base p digits of n. The
fractions cn and dn have the same p-power denominator, with exponent ordp(n!) −n =
n(1 −1/(p −1)) + sp(n)/(p −1). Alas, for p > 2 this exponent of p in the denominator of
cn and dn blows up with n because 1 −1/(p −1) > 0 for p > 2. When p = 2 this exponent
in the denominator is s2(n), which can stay bounded by restricting n to the powers of 2.
Appendix C. Deriving formulas for π/4
We will prove formulas for π/4 presented in the introduction:
π
4 = arctan 1
2 + arctan 1
3,
(C.1)
π
4 = 2 arctan 1
3 + arctan 1
7,
(C.2)
π
4 = 4 arctan 1
5 −arctan 1
239.
(C.3)
The proofs will use the following addition formula for arctan x.
Theorem C.1. If x, y, and (x + y)/(1 −xy) are in (0, π/2) and 0 < xy < 1, then
(C.4)
arctan x + arctan y = arctan
 x + y
1 −xy

.
Proof. By the tangent addition formula
tan(θ1 + θ2) = tan θ1 + tan θ2
1 −tan θ1 tan θ2
and the identity tan(arctan t) = t when t ∈(−π/2, π/2), the two sides of (C.4) have common
tangent value (x + y)/(1 −xy). Thus the two sides of (C.4) are equal provided they are in
(−π/2, π/2). The right side of (C.4) is in (0, π/2) since arctan-values on positive numbers
are in (0, π/2). That the left side of (C.4) is in (0, π/2) follows from arctan t < t when t > 0
since it implies 0 < arctan x + arctan y < x + y < (x + y)/(1 −xy) < π/2.
□
To derive (C.1), set x = 1/2 and y = 1/3 in Theorem C.1: since (x + y)/(1 −xy) =
(5/6)/(5/6) = 1 < π/2,
arctan 1
2 + arctan 1
3 = arctan
 x + y
1 −xy

= arctan 1 = π
4 .
To derive (C.2), ﬁrst we compute 2 arctan(1/3) by using x = y = 1/3 in Theorem C.1:
(x + y)/(1 −xy) = (2/3)/(8/9) = 3/4 < 1 < π/2, so
2 arctan 1
3 = arctan 1
3 + arctan 1
3 = arctan
 x + y
1 −xy

= arctan 3
4.
Now use Theorem C.1 with x = 3/4 and y = 1/7: (x + y)/(1 −xy) = (25/28)/(25/28) = 1,
so
2 arctan 1
3 + arctan 1
7 = arctan 3
4 + arctan 1
7 = arctan
 x + y
1 −xy

= arctan 1 = π
4 .
To derive (C.3), rewrite it as
arctan 1 + arctan 1
239 = 4 arctan 1
5.

<!-- page 16 -->
16
KEITH CONRAD
To prove this, we’ll rewrite both sides as a common arctan value. Set x = 1 and y = 1/239
in Theorem C.1: (x + y)/(1 −xy) = 240/238 = 120/119 ≈1.008 < π/2, so
(C.5)
arctan 1 + arctan 1
239 = arctan
 x + y
1 −xy

= arctan 120
119.
Next, set x = y = 1/5 in Theorem C.1: (x+y)/(1−xy) = (2/5)/(24/25) = 5/12 < 1 < π/2,
so
2 arctan 1
5 = arctan 1
5 + arctan 1
5 = arctan x + y
1 −xy = arctan 5
12.
When x = y = 5/12 in Theorem C.1, (x+y)/(1−xy) = (5/6)/(119/144) = 120/119 < π/2,
so
4 arctan 1
5 = 2 · 2 arctan 1
5 = 2 arctan 5
12 = arctan
 x + y
1 −xy

= arctan 120
119.
That matches (C.5), so we have proved (C.3).
Remark C.2. Formula (C.3) is due to Machin in 1706 and was used by Shanks [10] in his
calculation of 707 digits of π that was in error after the 527th decimal place.
As an exercise, use Theorem C.1 to prove an 1896 formula of St¨ormer [14]:
π
4 = 6 arctan 1
8 + 2 arctan 1
57 + arctan 1
239.
First show 6 arctan(1/8) = arctan(186416/201663) and 2 arctan(1/57) = arctan(57/1624).
References
[1] A. Baker, “Transcendental Number Theory,” Cambridge Univ. Press, Cambridge, 1975.
[2] C. H. Edwards, Jr., “The Historical Development of the Calculus,” Springer-Verlag, New York, 1979.
[3] L. Euler De fractionibus continuis dissertatio, Commentarii Academiae Scientiarum Petropolitanae 9
(1744), 98–137. URL https://scholarlycommons.pacific.edu/euler-works/71/.
[4] A. O. Gelfond, “Transcendental and Algebraic Numbers,” Dover, New York, 1960.
[5] E. Hairer and G. Wanner, “Analysis by its History,” Springer-Verlag, New York, 1996.
[6] K. Ireland and M. Rosen, “A Classical Introduction to Modern Number Theory,” 2nd ed., Springer-
Verlag, New York, 1990.
[7] J. H. Lambert, M´emoire sur quelques propri´et´es remarquables des quantit´es transcendantes cir-
culaires et logarithmiques, Histoire de l’Acad´emie Royale des Sciences et Belles-Lettres de Berlin,
Ann´ee 1761 17 1768, 265–322. URL http://www.bibnum.education.fr/mathematiques/theorie-des-
nombres/lambert-et-l-irrationalite-de-p-1761. English translation at https://hal.archives-
ouvertes.fr/hal-02984214/document.
[8] I. Niven, A simple proof that π is irrational, Bull. Amer. Math. Soc. 53 (1947), 509.
[9] R. Roy, The Discovery of the Series Formula for π by Leibniz, Gregory and Nilakanth, Math. Mag. 63
(1990), 291–306.
[10] W. Shanks, On the extension of the numerical value of π, Proceedings of the Royal Society of London
21 (1873), 318-319. URL https://royalsocietypublishing.org/doi/pdf/10.1098/rspl.1872.0066.
[11] A. Shidlovskii, “Transcendental Numbers,” de Gruyter, Berlin 1989.
[12] M. Spivak, “Calculus,” 2nd ed., Publish or Perish, Wilmington, Del., 1967.
[13] J. de Stainville, “M´elange d’analyse Alg´ebrique et de G´eom´etrie,” Courcier, Paris, 1815. URL http://
www.bibnum.education.fr/mathematiques/theorie-des-nombres/melange-d-analyse-algebrique-et-
de-geometrie.
[14] C. St¨ormer, Sur l’Application de la Th´eorie des Nombres Entiers Complexes `a la Solution en Nombres
Rationels x1, x2, . . . , xn, c1, c2, . . . , k, de l’´Equation c1arctg x1 + c2arctg x2 + · · · + cnarctg xn = kπ/4,
Archiv for Mathematik og Naturvidenskab 19 (1896), 75–85.
[15] L. Zhou and L. Markov, Recurrent Proofs of the Irrationality of Certain Trigonometric Values, Amer.
Math. Monthly 117 (2010), 360–362.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*