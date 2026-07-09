# Stirling's Formula

> **Source**: https://kconrad.math.uconn.edu/blurbs/stirling.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
STIRLING’S FORMULA
KEITH CONRAD
1. Introduction
Our goal is to prove the following asymptotic estimate for n!, called Stirling’s formula.
Theorem 1.1. As n →∞, n! ∼nn
en
√
2πn. That is, lim
n→∞
n!
(nn/en)
√
2πn = 1.
Example 1.2. Set n = 10: 10! = 3628800 and (1010/e10)
p
2π(10) = 3598695.61 . . . . The
diﬀerence between these, around 30104, is rather large by itself but is less than 1% of the
value of 10!. That is, Stirling’s approximation for 10! is within 1% of the correct value.
Stirling’s formula can also be expressed as an estimate for log(n!):
(1.1)
log(n!) = n log n −n + 1
2 log n + 1
2 log(2π) + εn,
where εn →0 as n →∞.
Example 1.3. Taking n = 10, log(10!) ≈15.104 and the logarithm of Stirling’s approxi-
mation to 10! is approximately 15.096, so log(10!) and its Stirling approximation diﬀer by
roughly .008.
Before proving Stirling’s formula we will establish a weaker estimate for log(n!) than
(1.1) that shows n log n is the right order of magnitude for log(n!). After proving Stirling’s
formula we will give some applications and then discuss a little bit of its history. Stirling’s
contribution to Theorem 1.1 was recognizing the role of the constant
√
2π.
2. Weaker version
Theorem 2.1. For all n ≥2, n log n −n < log(n!) < n log n, so log(n!) ∼n log n.
Proof. The inequality log(n!) < n log n is a consequence of the trivial inequality n! < nn.
Here are three methods of showing n log n −n < log(n!).
Method 1: A Riemann sum approximation for
R n
1 log x dx using right endpoints is log 2+
· · · + log n = log(n!), which overestimates, so log(n!) >
R n
1 log x dx = n log n −n + 1.
Method 2: The power series expansion of en is P
k≥0 nk/k!. Comparing en to the nth
term in the series gives us en > nn/n!, so n! > nn/en. Therefore log(n!) > n log n −n.
Method 3: For all k ≥1, e > (1 + 1/k)k. Multiplying this over k = 1, 2, . . . , n −1, we get
en−1 > nn−1/(n −1)! = nn/n!, so n! > enn/en. Thus log(n!) > n log n −n + 1.
Dividing through the inequality n log n −n < log(n!) < n log n by n log n, we obtain
1 −1/ log n < log(n!)/(n log n) < 1, so log(n!) ∼n log n.
□
We won’t use Theorem 2.1 in the proof of Theorem 1.1, but it’s worth proving Theorem
2.1 ﬁrst since the approximations log(n!) ≈n log n−n or log(n!) ≈n log n are how Stirling’s
formula is most often used in science. Large factorials occur when counting arrangements
of gas particles or quantum particles in diﬀerent macrostates, or ﬁles in data compression.
While the lower order terms 1
2 log n + 1
2 log(2π) in (1.1) are irrelevant in most scientiﬁc
applications of (1.1), they are used in calculations in quantum ﬁeld theory.
1

<!-- page 2 -->
2
KEITH CONRAD
Remark 2.2. In the proof of Theorem 2.1, the ﬁrst and third methods lead to upper bounds
on log(n!) that are sharper than n log n. By the ﬁrst method, using left endpoints implies
R n
1 log x dx > log((n −1)!) = log(n!) −log n, which leads to log(n!) < n log n −n + log n + 1.
(We can do slightly better with the trapezoid approximation, which is the average of the
left endpoint and right endpoint approximations. It tells us, since log x is concave down,
that
R n
1 log x dx > 1
2(log(n!) + log(n!) −log n) = log(n!) −1
2 log n, so log(n!) < n log n −
n + 1
2 log n + 1.) By the third method, the upper bound e < (1 + 1/k)k+1 multiplied over
k = 1, 2, . . . , n−1 leads to en−1 < nn/(n−1)! = nn+1/n!, so log(n!) < n log n−n+log n+1.
3. Proof of Stirling’s Formula
Any proof of Stirling’s formula needs to bring in a formula that involves π. One such
formula, which Stirling knew, is the Wallis product
π
2 = 2
1 · 2
3 · 4
3 · 4
5 · 6
5 · 6
7 · · · .
Another formula is the evaluation of the Gaussian integral from probability theory:
(3.1)
Z ∞
−∞
e−x2/2 dx =
√
2π.
This integral will be how
√
2π enters the proof of Stirling’s formula here, and another idea
from probability theory will also be used in the proof.
To prove Stirling’s formula, we begin with Euler’s integral for n!.
Theorem 3.1 (Euler). For n ≥0,
n! =
Z ∞
0
xne−x dx.
Proof. We will use induction and integration by parts. The case n = 0 is a direct calculation:
R ∞
0 e−x dx = −e−x|∞
0 = 0 −(−1) = 1. If n! =
R ∞
0 xne−x dx for some n, then
Z ∞
0
xn+1e−x dx =
Z ∞
0
u dv
where u = xn+1 and dv = e−x dx. Then du = (n + 1)xn dx and v = −e−x, so
Z ∞
0
xn+1e−x dx = uv

∞
0
−
Z ∞
0
v du
=
−xn+1
ex

∞
0
+
Z ∞
0
(n + 1)e−xxn dx
= lim
b→∞−bn+1
eb
+ 0 + (n + 1)
Z ∞
0
xne−x dx
= (n + 1)
Z ∞
0
xne−x dx,
which by induction is (n + 1)n! = (n + 1)!.1
□
Let’s consider the graph of y = xne−x for x ≥0. By calculus, the graph has a maximum
at x = n and inﬂection points at x = n + √n and x = n −√n. In Figure 1 is 1 ≤n ≤4.
These graphs, for larger n, look somewhat like bell curves from probability theory. In
probability, the density function of a normal random variable X with mean µ and standard
deviation σ has its maximum at µ and inﬂection points at µ+σ and µ−σ, and the random
1Using Theorem 3.1, n! =
R ∞
0
xne−x dx >
R ∞
n xne−x dx > nn R ∞
n e−x dx = nn/en for n ≥2, which is
another proof of the lower bound log(n!) > n log n −n in Theorem 2.1.

<!-- page 3 -->
STIRLING’S FORMULA
3
x
y
1
2
3
4
Figure 1. Plot of y = xne−x for 1 ≤n ≤4.
variable Z = (X −µ)/σ is then normal with mean 0 and standard deviation 1. Considering
the analogy µ ↔n and σ ↔√n, make the change of variables t = (x −n)/√n in Euler’s
integral for n!. This sends x = n to t = 0 and x = n ± √n to t = ±1, so
n! =
Z ∞
0
xne−x dx
=
Z ∞
−√n
(n + √nt)ne−(n+√nt)√n dt
= nn√n
en
Z ∞
−√n

1 +
t
√n
n
e−√nt dt.
(3.2)
The terms extracted out of the integral in (3.2) are exactly what appears in Stirling’s formula
except for the factor
√
2π, so to prove Stirling’s formula we will show
(3.3)

1 +
t
√n
n
e−√nt →e−t2/2
as n →∞, for each t, and then
(3.4)
Z ∞
−√n

1 +
t
√n
n
e−√nt dt →
Z ∞
−∞
e−t2/2 dt
(3.1)
=
√
2π
as n →∞.
Remark 3.2. There are two proofs of Stirling’s formula in [3] using a sequence of random
variables Xn with mean n and standard deviation √n, and the change of variables Tn =
(Xn −n)/√n. This same change of variables, in the form t = (x −n)/√n, is used without
motivation in the non-probabilistic proofs of Stirling’s formula in [17] and [18].
To prove (3.3) requires some care. If we handwave, as n →∞

1 +
t
√n
n
e−√nt =
 
1 +
t
√n
√n!√n
e−√nt ≈(et)
√ne−√nt = 1,
which is wrong. The mistake is that although (1 + t/√n)
√n →et as n →∞, it is not true
after raising both sides to the √n power that (1+t/√n)n behaves like e
√nt: approximately
equal numbers need not remain approximately equal when raised to a large power.

<!-- page 4 -->
4
KEITH CONRAD
To write the integral in (3.2) over the whole real line, set
fn(t) =
(
0,
if t ≤−√n,
(1 + t/√n)ne−√nt,
if t ≥−√n,
so n! = (nn√n/en)
R ∞
−∞fn(t) dt. Figure 2 is a plot of y = fn(t) for 1 ≤n ≤4 (solid)
compared to y = e−t2/2 (dashed). The graphs suggest that as n →∞, fn(t) →e−t2/2.
t
y
−1
−
√
2
−
√
3
−2
Figure 2. Plot of y = fn(t) for 1 ≤n ≤4 and y = e−t2/2.
Theorem 3.3. For each t ∈R, fn(t) →e−t2/2 as n →∞.
Proof. We will show log fn(t) →−t2/2 as n →∞. Since t is ﬁxed in the limit calculation,
we can focus on n that is large relative to |t|. For √n > |t|, i.e., n > t2, we have
fn(t) = (1 + t/√n)n
e
√nt
,
so
log(fn(t)) = n log

1 +
t
√n

−√nt.
For n > 4t2, |t/√n| < 1/2. We have log(1 + x) = x −x2/2 + O(|x|3) for |x| ≤1/2,2 so
log(fn(t)) = n
 t
√n −(t/√n)2
2
+ O((t/√n)3)

−√nt = −t2
2 + O(t3/√n).
As n →∞, the O-term tends to 0, so the limit is −t2/2.
□
To deduce from Theorem 3.3 that
R ∞
−∞fn(t) dt →
R ∞
−∞e−t2/2 dt, which would ﬁnish the
proof of Stirling’s formula by (3.4), we use the dominated convergence theorem: what is a
positive integrable function on R dominating |fn| = fn for all n? By Figure 2, one such
function should be
g(t) :=
(
e−t2/2,
if t < 0
f1(t),
if t ≥0 =
(
e−t2/2,
if t < 0,
(1 + t)e−t,
if t ≥0,
which is positive and integrable on R. To prove 0 ≤fn(t) ≤g(t) for all n and t, it’s obvious
for t ≤−√n since fn(t) = 0. To prove fn(t) ≤g(t) if t > −√n, take logarithms:
log fn(t) = n log

1 +
t
√n

−√nt
?
≤log g(t) =
(
−t2/2,
if −√n < t ≤0,
log(1 + t) −t,
if t ≥0.
2In [18] it’s shown for |x| ≤1/2 that log(1 + x) = x −x2/2 + O(|x|3/3) where the O-constant can be 2.

<!-- page 5 -->
STIRLING’S FORMULA
5
Case 1: log fn(t)
?
≤−t2/2 for −√n < t ≤0.
We will show the diﬀerence
(3.5)
log fn(t) + t2
2 = n log

1 +
t
√n

−√nt + t2
2
for −√n < t ≤0 is increasing, so the fact that it vanishes at t = 0 implies it is negative for
−√n < t < 0. The derivative of (3.5) is
n
1 + t/√n
1
√n −√n + t =
t2
t + √n,
which is positive for −√n < t < 0 since the numerator and denominator are both positive.
Case 2: log fn(t)
?
≤log(1 + t) −t for t ≥0. This is trivial for n = 1, since log f1(t) =
log(1 + t) −t for t ≥0. Thus we can take n > 1. We will show
(3.6)
log(1 + t) −t −log fn(t) = log(1 + t) −t −n log

1 +
t
√n

+ √nt
for t ≥0 is increasing, so the fact that it vanishes at t = 0 implies it is positive for t > 0.
The derivative of (3.6) is
1
1 + t −1 −
n
1 + t/√n
1
√n + √n =
(√n −1)t2
(t + 1)(t + √n),
which is positive since the numerator and denominator are positive when t > 0 and n ≥2.
Our proof of Stirling’s formula is now complete.
Remark. Similar to the proof that fn(t) ≤g(t), we can prove what is suggested by
Figure 2: fn+1(t) < fn(t) for t > 0 and fn+1(t) > fn(t) for −√n < t < 0, so fn(t) →e−t2/2
as n →∞from below for t < 0 and from above for t > 0. (At t = 0 we have fn(0) = 1 for
all n.) For t > −√n, both fn(t) and fn+1(t) are positive and
d
dt(log fn+1(t) −log fn(t)) = −t√n + 1
t + √n + 1 +
t√n
t + √n =
(√n −√n + 1)t2
(t + √n)(t + √n + 1),
which is negative for t > −√n except for being 0 at t = 0, so log(fn+1(t)/fn(t)) is decreasing
for t > −√n. Since fn+1(0)/fn(0) = 1, we get fn+1(t)/fn(t) > 1 for −√n < t < 0 and
fn+1(t)/fn(t) < 1 for t > 0.
4. Applications of Stirling’s formula
Example 4.1. The probability that ﬂipping a fair coin 2n times results in exactly n heads
and n tails is
 2n
n

(1
2)2n. What is a good estimate for the size of this number? Writing
 2n
n

as (2n)!
n!n! = (2n)!
n!2 , by Stirling’s formula
2n
n

∼((2n)2n/e2n)
p
2π(2n)
(nn/en)2(2πn)
= 22n
√πn,
so
 2n
n

(1
2)2n ∼1/√πn. This probability decays to 0 like 1/√n.
This same calculation occurs in the theory of random walks. Suppose a person moves
around the d-dimensional lattice Zd by jumping from any point to one of its 2d neighboring
points (diﬀering in one coordinate by ±1), with a move in each of the 2d directions being
equally likely.
If such a random walk starts at the origin, will it return to the origin
inﬁnitely often? Polya proved that if d = 1 or 2 then the probability of returning to the
origin inﬁnitely often is 1, while for d ≥3 this probability is 0. In picturesque language, a
drunkard who stumbles away from a bar by walking along a road or in a street grid is almost

<!-- page 6 -->
6
KEITH CONRAD
surely going to come back to the bar, but if he can ﬂy (d = 3) then it’s no longer certain
that he’ll return. The key to this result on random walks is that P
n≥1 1/nd/2 diverges for
d = 1 and 2, and converges for d ≥3. To see the connection to the coin problem above,
consider a random walk on Z (that is, d = 1). If a person starting at 0 takes steps left
and right by 1 unit with probability 1/2 each, then the probability the person returns to 0
after 2n steps (it’s impossible to return to 0 after an odd number of steps) is the probability
of taking n left steps and n right steps, so the probability is
 2n
n
   1
2
2n. The asymptotic
estimate 1/√πn from Stirling’s formula tells us that the sum of these probabilities over all n
diverges because P
n≥1 1/√n diverges, and this divergence leads to probability 1 that such
events (returning to 0) occur inﬁnitely often. Stirling’s formula can also be used to analyze
random walks in Zd when d ≥2.
Example 4.2. Let’s determine the number of digits in 100!. The number of digits in a
positive integer N is ⌊log10(N)⌋+ 1, so we want to compute ⌊log10(100!)⌋+ 1. From (1.1),
log10(100!) = log(100!)
log(10) ≈100.5 log(100) −100 + 1
2 log(2π)
log(10)
≈157.96.
To pin down the approximation well enough to be sure that ⌊log10(100!)⌋is 157 (and not
158), we use a sharper form of Stirling’s formula having upper and lower bounds:
1 <
n!
(nn/en)
√
2πn < e1/12n.
Taking logarithms,
0 < log(n!) −

n + 1
2

log n −n + 1
2 log(2π) <
1
12n.
Dividing by log 10,
0 < log10(n!) −(n + 1/2) log n −n + (1/2) log(2π)
log 10
<
1
12n log 10.
Let Sn be the term subtracted from log10(n!) above. Since 1/(12n log 10) ≤1/12 log 10 ≈
.036 < 1, ⌊log10(n!)]⌋is either ⌊Sn⌋or ⌊Sn⌋+ 1.
Taking n = 100, the diﬀerence between log10(100!) and S100 is bounded above by
1
1200 log 10 ≈.00036. Since S100 ≈157.96 . . . diﬀers from its nearest integer by more than
.00036, ⌊log10(100!)⌋= 157 and thus 100! has 158 digits. In a similar way, 1000! has 2568
digits and 10000! has 35660 digits.
Since 1/(12n log 10) →0, heuristically we expect ⌊log10(n!)⌋= ⌊Sn⌋most of the time,
but in rare instances an integer falls between ⌊log10(n!)⌋and ⌊Sn⌋. The ﬁrst n where this
happens, making ⌊log10(n!)⌋equal to ⌊Sn⌋+ 1 rather than ⌊Sn⌋, is the 13-digit number
n = 6,561,101,970,383. See [8].
Example 4.3. For each positive integer n, the volume Vn of the unit ball in Rn is
πn/2/Γ(n/2 + 1), where Γ(t) =
R ∞
0 xt−1e−x dx for t > 0, so n! = Γ(n + 1). In one, two, and
three dimensions the number Vn is 2, π, and (4/3)π, which is increasing. But for large n,
Vn actually tends to 0. (In fact Vn is increasing for 1 ≤n ≤5 and decreasing for n ≥5.)
For even n, Vn = πn/2/(n/2)! so by Stirling’s formula Vn ∼(2πe
n )n/2
1
√πn, which tends to 0
as n →∞. The same asymptotic estimate holds for odd n using an extension of Stirling’s
formula to the Γ-function.

<!-- page 7 -->
STIRLING’S FORMULA
7
Example 4.4. The Bernoulli numbers Bn are deﬁned by x/(ex −1) = P
n≥0(Bn/n!)xn.
They begin as
B0 = 1, B1 = −1
2, B2 = 1
6, B3 = 0, B4 = −1
30, B5 = 0, B6 = 1
42, B7 = 0, . . . .
For odd n > 1, Bn = 0. This sequence is important in number theory (values of the Riemann
zeta-function and early work on Fermat’s last theorem depend on them), topology (counting
exotic spheres), and numerical analysis (the Euler–Maclaurin summation formula). Initial
data suggest Bn is small for even n, but this is misleading: |Bn| →∞.
For instance,
|B20| ≈529 and |B100| has 79 digits before the decimal point. Using Stirling’s formula
and the Riemann zeta-function, we will give an asymptotic estimate on how large the even-
indexed Bernoulli numbers are.
For s > 1, the Riemann zeta-function ζ(s) = P
n≥1 1/ns converges and Euler gave a
formula for it at positive even integers: for each positive integer k,
ζ(2k) = (2π)2k|B2k|
2(2k)!
.
As s →∞we have ζ(s) →1, so as k →∞Stirling’s formula tells us
|B2k| = 2(2k)!ζ(2k)
(2π)2k
∼2(2k)!
(2π)2k ∼2(2k/e)2kp
2π(2k)
(2π)2k
= 4
√
πk
 k
πe
2k
.
Thus |B2k| tends to ∞very rapidly as k →∞.
5. History of Stirling’s Formula
Stirling’s formula ﬁrst arose from correspondence between Stirling and DeMoivre in the
1720s about DeMoivre’s work on approximating a binomial distribution by a normal dis-
tribution. DeMoivre had essentially discovered the Central Limit Theorem for the normal
approximation to the binomial distribution. The Central Limit Theorem is nowadays proved
without Stirling’s formula, and for special types of probability distributions it leads to proofs
of Stirling’s formula [7], [15], [20].
What DeMoivre showed in his work on approximating a binomial distribution was that
 2n
n
 1
22n ≈2.168(1−1/2n)2n
√2n−1
, with 2.168 being an approximation to a constant that DeMoivre
could express only as an inﬁnite series. For large n, (1 −1/2n)2n ≈1/e and √2n −1 ≈
√
2√n, so DeMoivre’s approximation is essentially (2.168/
√
2e)/√n.
Stirling found the
“true” value of 2.168 to be e
p
2/π, which turns DeMoivre’s approximation into 1/√πn, as
we found in Example 4.1.
Stirling’s treatment of approximations to log(n!) appeared in his book Methodus Diﬀeren-
tialis [22], as Example 2 after Proposition 28. An English translation is in [23, pp. 149–151].
Stirling’s contribution to the asymptotic estimate for log(n!) that is named after him is in
the identiﬁcation of the constant in the formula as 1
2 log(2π) = log
√
2π (without proof).
How did he realize the constant involves π? According to [13, p. 481], Stirling tabulated
log(n!), interpolated the sequence to factorials of half-integers, and observed agreement of
(−1/2)! with √π to 10 decimal places. Tweddle [23, p. 271] suggests Stirling found the link
with π through recognizing it in a numerical approximation or by a skillful use of the Wallis
product for π. In any case, DeMoivre proved
 2n
n
 1
22n ∼1/√πn using the Wallis product for
π in his book Miscellanea Analytica [6]. A discussion of DeMoivre’s work on this problem
is in [13, Chap. 24].
Stirling’s formula in the form log(n!) = n log n−n+ 1
2 log(n)+log
√
2π+εn, where εn →0
as n →∞, can be reﬁned to an asymptotic expansion called Stirling’s series that replaces

<!-- page 8 -->
8
KEITH CONRAD
εn with a series in powers of 1/n. This expansion is due to DeMoivre; a version using a
series in powers of 1/(n + 1/2) was found earlier by Stirling [12].
Here is a summary of diﬀerent ways that proofs of Stirling’s formula bring in π.
(1) The Wallis product for π/2: [5], [10].
(2) The Gaussian integral: [3], [7], [11], [14], [15], [16], [19], [20], [21], [24].
(3) In [1, Sect. 2.5, Chap. 5], the proof uses the formula Γ(z)Γ(1 −z) = π/ sin(πz).
(4) In [2, p. 24] the proof uses Γ(1/2) = √π.
(5) In [4], the proof uses √n/2n−1 = Qn
k=1 sin(kπ/2n).
(6) In [9], π comes from the formula Q
n≥1(1 −x2/n2) = sin(πx)/(πx).
References
[1] L. Ahlfors, Complex Analysis, 3rd ed., McGraw-Hill, New York, 1979.
[2] E. Artin, The Gamma Function, Holt, Reinhart, Winston, New York, 1964.
[3] C. R. Blyth and P. K. Pathak, “A Note on Easy Proofs of Stirling’s formula,” Amer. Math. Monthly 93
(1986), 376–379.
[4] R. B. Burckel, “Stirling’s Formula via Riemann Sums,” College Math. Journal 37 (2006), 300–307.
[5] A. J. Coleman, “A simple proof of Stirling’s formula,” Amer. Math. Monthly 58 (1951), 334–336.
[6] A. DeMovire, Miscellanea Analytica, London, 1730.
[7] P. Diaconis and D. Freedman, “An Elementary Proof of Stirling’s formula,” Amer. Math. Monthly 93
(1986), 123–125.
[8] N. D. Elkies, http://mathoverflow.net/questions/19170/how-good-is-kamenetskys-formula-for-
the-number-of-digits-in-n-factorial.
[9] W. Feller, “A Direct Proof of Stirling’s Formula,” Amer. Math. Monthly 74 (1967), 1223–1225.
[10] D. Fowler, “The Factorial Functions: Stirling’s Formula,” Math. Gazette, 84 (2000), 42–50.
[11] C. L. Frenzen, “A New Elementary Proof of Stirling’s Formula,” Math. Magazine 68 (1995), 55–58.
[12] J. G´elinas, Original proofs of Stirling’s series for log(n!), https://arxiv.org/abs/1701.06689.
[13] A. Hald, A History of Probability and Statistics and their Applications before 1750, Wiley, New York,
1990.
[14] W. K. Hayman, “A Generalisation of Stirling’s Formula,” J. Reine Angew. Math., 196 (1956), 67–95.
[15] R. A. Khan, “A probabilistic proof of Stirling’s Formula,” Amer. Math. Monthly 81 (1974), 366–369.
[16] G. Marsaglia and J. C. W. Marsaglia, “A New Derivation of Stirling’s Approximation to n!,” Amer.
Math. Monthly 97 (1990), 826–829.
[17] R. Michel, “On Stirling’s Formula,” Amer. Math. Monthly 109 (2002), 388–390.
[18] R. Michel, “The (n + 1)-th Proof of Stirling’s Formula,” Amer. Math. Monthly 115 (2008), 844–845.
[19] J. M. Patin, “A very short proof of Stirling’s formula,” Amer. Math. Monthly 96 (1989), 41–42.
[20] M. A. Pinsky, “Stirling’s Formula via the Poisson Distribution,” Amer. Math. Monthly 114 (2007),
256–258.
[21] D. Romik, “Stirling’s Approximation for n!: the Ultimate Short Proof?”, Amer. Math. Monthly 107
(2000), 556–557.
[22] J. Stirling, Methodus Diﬀerentialis: sive Tractatus de Summatione et Interpolatione Serierum Inﬁni-
tarum, London, 1730.
[23] I. Tweddle, James Stirling’s Methodus Diﬀerentialis: An Annotated Translation of Stirling’s Text,
Springer-Verlag, London, 2003.
[24] C. S. Wong, “A Note on the Central Limit Theorem,” Amer. Math. Monthly 84 (1977), 472.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*