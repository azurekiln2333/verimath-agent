# Differentiation Under the Integral Sign

> **Source**: https://kconrad.math.uconn.edu/blurbs/diffunderint.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
KEITH CONRAD
I had learned to do integrals by various methods shown in a book1 that my high
school physics teacher Mr. Bader had given me. [It] showed how to diﬀerentiate
parameters under the integral sign – it’s a certain operation. It turns out that’s
not taught very much in the universities; they don’t emphasize it. But I caught on
how to use that method, and I used that one damn tool again and again. [If] guys
at MIT or Princeton had trouble doing a certain integral, [then] I come along and
try diﬀerentiating under the integral sign, and often it worked. So I got a great
reputation for doing integrals, only because my box of tools was diﬀerent from
everybody else’s, and they had tried all their tools on it before giving the problem
to me.2
Richard Feynman [5, pp. 71–72]3
1. Introduction
The method of diﬀerentiation under the integral sign, due to Leibniz in 1697 [4], concerns integrals
depending on a parameter, such as
R 1
0 x2e−tx dx. Here t is the extra parameter. (Since x is the
variable of integration, x is not a parameter.) In general, we might write such an integral as
(1.1)
Z b
a
f(x, t) dx,
where f(x, t) is a function of two variables like f(x, t) = x2e−tx.
Example 1.1. Let f(x, t) = (2x + t3)2. Then
Z 1
0
f(x, t) dx =
Z 1
0
(2x + t3)2 dx. An anti-derivative
of (2x + t3)2 with respect to x is 1
6(2x + t3)3, so
Z 1
0
(2x + t3)2 dx = (2x + t3)3
6

x=1
x=0
= (2 + t3)3 −t9
6
= 4
3 + 2t3 + t6.
This answer is a function of t, which makes sense since the integrand depends on t. We integrate
over x and are left with something that depends only on t, not x.
An integral like
R b
a f(x, t) dx is a function of t, so we can ask about its t-derivative, assuming
that f(x, t) is nicely behaved. The rule, called diﬀerentiation under the integral sign, is that the
t-derivative of the integral of f(x, t) is the integral of the t-derivative of f(x, t):
(1.2)
d
dt
Z b
a
f(x, t) dx =
Z b
a
∂
∂tf(x, t) dx.
1The book Feynman read was Advanced Calculus by Woods [16]. See Appendix B for an excerpt.
2See https://scientistseessquirrel.wordpress.com/2016/02/09/do-biology-students-need-calculus/ for
a similar story with integration by parts in the ﬁrst footnote.
3Just before this quote, Feynman wrote “One thing I never did learn was contour integration.” Perhaps he meant
that he never felt he learned it well, since he did know it. See [6, Lect. 14, 15, 17, 19], [7, p. 92], and [8, pp. 47–49].
A challenge he gave in [5, p. 176] suggests he didn’t like contour integration.
1

<!-- page 2 -->
2
KEITH CONRAD
If you are used to thinking mostly about functions with one variable, not two, keep in mind that
(1.2) involves integrals and derivatives with respect to separate variables: integration with respect
to x and diﬀerentiation with respect to t.
Example 1.2. We saw in Example 1.1 that
R 1
0 (2x + t3)2 dx = 4/3 + 2t3 + t6, whose t-derivative is
6t2 + 6t5. According to (1.2), we can also compute the t-derivative of the integral like this:
d
dt
Z 1
0
(2x + t3)2 dx =
Z 1
0
∂
∂t(2x + t3)2 dx
=
Z 1
0
2(2x + t3)(3t2) dx
=
Z 1
0
(12t2x + 6t5) dx
= 6t2x2 + 6t5x

x=1
x=0
= 6t2 + 6t5.
The answer agrees with our ﬁrst, more direct, calculation.
We will apply (1.2) in many examples, and Section 12 presents a justiﬁcation. It is also used to
prove theorems: see Sections 11 and 13 and a proof of the Cram´er–Rao bound in statistics.
2. Euler’s factorial integral in a new light
For integers n ≥0, Euler’s integral formula for n! is
(2.1)
Z ∞
0
xne−x dx = n!,
which can be obtained by repeated integration by parts starting from the formula
(2.2)
Z ∞
0
e−x dx = 1
when n = 0. Now we are going to derive Euler’s formula in another way, by repeated diﬀerentiation
after introducing a parameter t into (2.2).
For t > 0, let x = tu. Then dx = t du and (2.2) becomes
Z ∞
0
te−tu du = 1.
Dividing by t and writing u as x (why is this not a problem?), we get
(2.3)
Z ∞
0
e−tx dx = 1
t .
This is a parametric form of (2.2), where both sides are now functions of t. We need t > 0 in order
that e−tx is integrable over the region x ≥0.
Now we bring in diﬀerentiation under the integral sign. Diﬀerentiate both sides of (2.3) with
respect to t, using (1.2) to treat the left side. We obtain
Z ∞
0
−xe−tx dx = −1
t2 ,

<!-- page 3 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
3
so
(2.4)
Z ∞
0
xe−tx dx = 1
t2 .
Diﬀerentiate both sides of (2.4) with respect to t, again using (1.2) to handle the left side. We get
Z ∞
0
−x2e−tx dx = −2
t3 .
Taking out the sign on both sides,
(2.5)
Z ∞
0
x2e−tx dx = 2
t3 .
If we continue to diﬀerentiate each new equation with respect to t a few more times, we obtain
Z ∞
0
x3e−tx dx = 6
t4 ,
Z ∞
0
x4e−tx dx = 24
t5 ,
and
Z ∞
0
x5e−tx dx = 120
t6 .
Do you see the pattern? It is
(2.6)
Z ∞
0
xne−tx dx =
n!
tn+1 .
We have used the presence of the extra variable t to get these equations by repeatedly applying
d/dt. Now specialize t to 1 in (2.6). We obtain
Z ∞
0
xne−x dx = n!,
which is our old friend (2.1). Voil´a!
The idea that made this work is introducing a parameter t, using calculus on t, and then setting
t to a particular value so it disappears from the ﬁnal formula. In other words, sometimes to solve
a problem it is useful to solve a more general problem. Compare (2.1) to (2.6).
3. A damped sine integral
We are going to use diﬀerentiation under the integral sign to prove
(3.1)
Z ∞
0
e−tx sin x
x
dx = π
2 −arctan t
for t > 0.
Call this integral F(t) and set f(x, t) = e−tx(sin x)/x, so (∂/∂t)f(x, t) = −e−tx sin x. Then
F ′(t) = −
Z ∞
0
e−tx(sin x) dx.
The integrand e−tx sin x, as a function of x, can be integrated by parts:
Z
eax sin x dx = (a sin x −cos x)
1 + a2
eax.

<!-- page 4 -->
4
KEITH CONRAD
Applying this with a = −t and turning the indeﬁnite integral into a deﬁnite integral,
F ′(t) = −
Z ∞
0
e−tx(sin x) dx = (t sin x + cos x)
1 + t2
e−tx

x=∞
x=0
.
As x →∞, t sin x + cos x oscillates a lot, but in a bounded way (since sin x and cos x are bounded
functions), while the term e−tx decays exponentially to 0 since t > 0. So the value at x = ∞is 0.
Therefore
F ′(t) = −
Z ∞
0
e−tx(sin x) dx = −
1
1 + t2 .
We know an explicit antiderivative of 1/(1 + t2), namely arctan t.
Since F(t) has the same
t-derivative as −arctan t, they diﬀer by a constant: for some number C,
(3.2)
Z ∞
0
e−tx sin x
x
dx = −arctan t + C
for t > 0.
We’ve computed the integral, up to an additive constant, without ﬁnding an antiderivative of
e−tx(sin x)/x.
To compute C in (3.2), let t →∞on both sides. Since |(sin x)/x| ≤1, the absolute value of
the integral on the left is bounded from above by
R ∞
0 e−tx dx = 1/t, so the integral on the left in
(3.2) tends to 0 as t →∞. Since arctan t →π/2 as t →∞, equation (3.2) as t →∞becomes
0 = −π
2 + C, so C = π/2. Feeding this back into (3.2),
(3.3)
Z ∞
0
e−tx sin x
x
dx = π
2 −arctan t
for t > 0.
If we let t →0+ in (3.3), this equation suggests that
(3.4)
Z ∞
0
sin x
x
dx = π
2 ,
which is true and it is important in signal processing and Fourier analysis. It is a delicate matter to
derive (3.4) from (3.3) since the integral in (3.4) is not absolutely convergent. Details are provided
in Appendix A.
4. The Gaussian integral
The improper integral formula
(4.1)
Z ∞
−∞
e−x2/2 dx =
√
2π
is fundamental to probability theory and Fourier analysis.
The function
1
√
2πe−x2/2 is called a
Gaussian, and (4.1) says the integral of the Gaussian over the whole real line is 1.
To prove (4.1) using diﬀerentiation under the integral sign, we are going to aim not at (4.1), but
at an equivalent formula over the range x ≥0:
(4.2)
Z ∞
0
e−x2/2 dx =
√
2π
2
=
rπ
2 .
Call the integral on the left I.
For t ∈R, set
F(t) =
Z ∞
0
e−t2(1+x2)/2
1 + x2
dx.

<!-- page 5 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
5
Then F(0) =
R ∞
0
dx/(1 + x2) = π/2 and F(∞) = 0. Diﬀerentiating under the integral sign,
F ′(t) =
Z ∞
0
−te−t2(1+x2)/2 dx = −te−t2/2
Z ∞
0
e−(tx)2/2 dx.
Make the substitution y = tx, with dy = t dx, so
F ′(t) = −e−t2/2
Z ∞
0
e−y2/2 dy = −Ie−t2/2.
For b > 0, integrate both sides from 0 to b and use the Fundamental Theorem of Calculus:
Z b
0
F ′(t) dt = −I
Z b
0
e−t2/2 dt =⇒F(b) −F(0) = −I
Z b
0
e−t2/2 dt.
Letting b →∞,
0 −π
2 = −I2 =⇒I2 = π
2 =⇒I =
rπ
2 .
I learned this approach from Michael Rozman [12], who modiﬁed an idea on a Math Stackex-
change question [3], and in a slightly less elegant form it appeared much earlier in [17].
By the same method we can calculate Iz =
R ∞
0 e−zx2/2 dx for z ∈C with Re(z) > 0, so I = I1.
Generalizing I2 = π/2, we get I2
z = π/(2z), so Iz = ±
p
π/2/√z, where √z is the principal square
root (with argument in (−π/4, π/4)). The sign on the right side is + when z = 1, so by continuity
in z we have Iz =
p
π/2/√z for all z with Re(z) > 0.
5. Higher moments of the Gaussian
For every integer n ≥0 we want to compute a formula for
(5.1)
Z ∞
−∞
xne−x2/2 dx.
(Integrals of the type
R
xnf(x) dx for n = 0, 1, 2, . . . are called the moments of f(x), so (5.1) is the
n-th moment of the Gaussian.) When n is odd, (5.1) vanishes since xne−x2/2 is an odd function.
What if n = 0, 2, 4, . . . is even?
The ﬁrst case, n = 0, is the Gaussian integral (4.1):
(5.2)
Z ∞
−∞
e−x2/2 dx =
√
2π.
To get formulas for (5.1) when n ̸= 0, we follow the same strategy as our treatment of the factorial
integral in Section 2: stick a t into the exponent of e−x2/2 and then diﬀerentiate repeatedly with
respect to t.
For t > 0, replacing x with
√
tx in (5.2) gives
(5.3)
Z ∞
−∞
e−tx2/2 dx =
√
2π
√
t .
Diﬀerentiate both sides of (5.3) with respect to t, using diﬀerentiation under the integral sign on
the left:
Z ∞
−∞
−x2
2 e−tx2/2 dx = −
√
2π
2t3/2 ,
so
(5.4)
Z ∞
−∞
x2e−tx2/2 dx =
√
2π
t3/2 .

<!-- page 6 -->
6
KEITH CONRAD
Diﬀerentiate both sides of (5.4) with respect to t. After removing a common factor of −1/2 on
both sides, we get
(5.5)
Z ∞
−∞
x4e−tx2/2 dx = 3
√
2π
t5/2 .
Diﬀerentiating both sides of (5.5) with respect to t a few more times, we get
Z ∞
−∞
x6e−tx2/2 dx = 3 · 5
√
2π
t7/2
,
Z ∞
−∞
x8e−tx2/2 dx = 3 · 5 · 7
√
2π
t9/2
,
and
Z ∞
−∞
x10e−tx2/2 dx = 3 · 5 · 7 · 9
√
2π
t11/2
.
Quite generally, when n is even
Z ∞
−∞
xne−tx2/2 dx = 1 · 3 · 5 · · · (n −1)
t(n+1)/2
√
2π,
where the numerator is the product of the positive odd integers from 1 to n −1 (understood to be
the empty product 1 when n = 0).
In particular, taking t = 1 we have computed (5.1):
Z ∞
−∞
xne−x2/2 dx = 1 · 3 · 5 · · · (n −1)
√
2π.
As an application of (5.4), we now compute (1
2)! :=
R ∞
0 x1/2e−x dx, where the notation (1
2)! and
its deﬁnition are inspired by Euler’s integral formula (2.1) for n! when n is a nonnegative integer.
Using the substitution u = x1/2 in
R ∞
0 x1/2e−x dx, we have
1
2

! =
Z ∞
0
x1/2e−x dx
=
Z ∞
0
ue−u2(2u) du
= 2
Z ∞
0
u2e−u2 du
=
Z ∞
−∞
u2e−u2 du
=
√
2π
23/2
by (5.4) at t = 2
=
√π
2 .
6. A cosine transform of the Gaussian
We are going to compute
F(t) =
Z ∞
0
cos(tx)e−x2/2 dx

<!-- page 7 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
7
by looking at its t-derivative:
(6.1)
F ′(t) =
Z ∞
0
−x sin(tx)e−x2/2 dx.
This is good from the viewpoint of integration by parts since −xe−x2/2 is the derivative of e−x2/2.
So we apply integration by parts to (6.1):
u = sin(tx),
dv = −xe−x2 dx
and
du = t cos(tx) dx,
v = e−x2/2.
Then
F ′(t) =
Z ∞
0
u dv
= uv

∞
0
−
Z ∞
0
v du
= sin(tx)
ex2/2

x=∞
x=0
−t
Z ∞
0
cos(tx)e−x2/2 dx
= sin(tx)
ex2/2

x=∞
x=0
−tF(t).
As x →∞, ex2/2 blows up while sin(tx) stays bounded, so sin(tx)/ex2/2 goes to 0. Therefore
F ′(t) = −tF(t).
We know the solutions to this diﬀerential equation: constant multiples of e−t2/2. So
Z ∞
0
cos(tx)e−x2/2 dx = Ce−t2/2
for some constant C. To ﬁnd C, set t = 0. The left side is
R ∞
0 e−x2/2 dx, which is
p
π/2 by (4.2).
The right side is C. Thus C =
p
π/2, so we are done: for all real t,
Z ∞
0
cos(tx)e−x2/2 dx =
rπ
2 e−t2/2.
Remark 6.1. If we want to compute G(t) =
R ∞
0 sin(tx)e−x2/2 dx, with sin(tx) in place of cos(tx),
then in place of F ′(t) = −tF(t) we have G′(t) = 1−tG(t), and G(0) = 0. From the diﬀerential equa-
tion, (et2/2G(t))′ = et2/2, so G(t) = e−t2/2 R t
0 ex2/2 dx. So while
R ∞
0 cos(tx)e−x2/2 dx = p π
2 e−t2/2,
the integral
R ∞
0 sin(tx)e−x2/2 dx is impossible to express in terms of elementary functions.
7. The Gaussian times a logarithm
We will compute
Z ∞
0
(log x)e−x2 dx.
Integrability at ∞follows from rapid decay of e−x2 at ∞, and integrability near x = 0 follows from
the integrand there being nearly log x, which is integrable on [0, 1], so the integral makes sense.
(This example was brought to my attention by Harald Helfgott.)

<!-- page 8 -->
8
KEITH CONRAD
We already know
R ∞
0 e−x2 dx = √π/2, but how do we ﬁnd the integral when a factor of log x is
inserted into the integrand? Replacing x with √x in the integral,
(7.1)
Z ∞
0
(log x)e−x2 dx = 1
4
Z ∞
0
log x
√x e−x dx.
To compute this last integral, the key idea is that (d/dt)(xt) = xt log x, so we get a factor of
log x in an integral after diﬀerentiation under the integral sign if the integrand has an exponential
parameter: for t > −1 set
F(t) =
Z ∞
0
xte−x dx.
(This is integrable for x near 0 since for small x, xte−x ≈xt, which is integrable near 0 since
t > −1.) Diﬀerentiating both sides with respect to t,
F ′(t) =
Z ∞
0
xt(log x)e−x dx,
so (7.1) tells us the number we are interested in is F ′(−1/2)/4.
The function F(t) is well-known under a diﬀerent name: for s > 0, the Γ-function at s is deﬁned
by
Γ(s) =
Z ∞
0
xs−1e−x dx,
so Γ(s) = F(s −1). Therefore Γ′(s) = F ′(s −1), so F ′(−1/2)/4 = Γ′(1/2)/4. For the rest of this
section we work out a formula for Γ′(1/2)/4 using properties of the Γ-function; there is no more
diﬀerentiation under the integral sign.
We need two standard identities for the Γ-function:
(7.2)
Γ(s + 1) = sΓ(s),
Γ(s)Γ

s + 1
2

= 21−2s√πΓ(2s).
The ﬁrst identity follows from integration by parts. Since Γ(1) =
R ∞
0 e−x dx = 1, the ﬁrst identity
implies Γ(n) = (n −1)! for every positive integer n. The second identity, called the duplication
formula, is subtle. For example, at s = 1/2 it says Γ(1/2) = √π. A proof of the duplication formula
can be found in many complex analysis textbooks. (The integral deﬁning Γ(s) makes sense not just
for real s > 0, but also for complex s with Re(s) > 0, and the Γ-function is usually regarded as a
function of a complex, rather than real, variable.)
Diﬀerentiating the ﬁrst identity in (7.2),
(7.3)
Γ′(s + 1) = sΓ′(s) + Γ(s),
so at s = 1/2
(7.4)
Γ′
3
2

= 1
2Γ′
1
2

+ Γ
1
2

= 1
2Γ′
1
2

+ √π =⇒Γ′
1
2

= 2

Γ′
3
2

−√π

.
Diﬀerentiating the second identity in (7.2),
(7.5)
Γ(s)Γ′

s + 1
2

+ Γ′(s)Γ

s + 1
2

= 21−2s(−log 4)√πΓ(2s) + 21−2s√π2Γ′(2s).
Setting s = 1 here and using Γ(1) = Γ(2) = 1,
(7.6)
Γ′
3
2

+ Γ′(1)Γ
3
2

= (−log 2)√π + √πΓ′(2).

<!-- page 9 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
9
We compute Γ(3/2) by the ﬁrst identity in (7.2) at s = 1/2: Γ(3/2) = (1/2)Γ(1/2) = √π/2 (we
already computed this at the end of Section 5). We compute Γ′(2) by (7.3) at s = 1: Γ′(2) =
Γ′(1) + 1. Thus (7.6) says
Γ′
3
2

+ Γ′(1)
√π
2
= (−log 2)√π + √π(Γ′(1) + 1) =⇒Γ′
3
2

= √π

−log 2 + Γ′(1)
2

+ √π.
Feeding this formula for Γ′(3/2) into (7.4),
Γ′
1
2

= √π(−2 log 2 + Γ′(1)).
It turns out that Γ′(1) = −γ, where γ ≈.577 is Euler’s constant. Thus, at last,
Z ∞
0
(log x)e−x2 dx = Γ′(1/2)
4
= −
√π
4 (2 log 2 + γ).
8. Logs in the denominator, part I
Consider the following integral over [0, 1], where t > 0:
Z 1
0
xt −1
log x dx.
Since 1/ log x →0 as x →0+, the integrand vanishes at x = 0. As x →1−, (xt −1)/ log x →t.
Therefore when t is ﬁxed the integrand is a continuous function of x on [0, 1], so the integral is not
an improper integral.
The t-derivative of this integral is
Z 1
0
xt log x
log x
dx =
Z 1
0
xt dx =
1
t + 1,
which we recognize as the t-derivative of log(t + 1). Therefore
Z 1
0
xt −1
log x dx = log(t + 1) + C
for some C. To ﬁnd C, let t →0+. On the right side, log(1 + t) tends to 0. On the left side, the
integrand tends to 0: |(xt −1)/ log x| = |(et log x −1)/ log x| ≤t because |ea −1| ≤|a| when a ≤0.
Therefore the integral on the left tends to 0 as t →0+. So C = 0, which implies
(8.1)
Z 1
0
xt −1
log x dx = log(t + 1)
for all t > 0, and it’s obviously also true for t = 0. Another way to compute this integral is to write
xt = et log x as a power series and integrate term by term, which is valid for −1 < t < 1.
Under the change of variables x = e−y, (8.1) becomes
(8.2)
Z ∞
0

e−y −e−(t+1)y dy
y = log(t + 1).

<!-- page 10 -->
10
KEITH CONRAD
9. Logs in the denominator, part II
We now consider the integral
F(t) =
Z ∞
2
dx
xt log x
for t > 1. The integral converges by comparison with
R ∞
2
dx/xt. We know that “at t = 1” the
integral diverges to ∞:
Z ∞
2
dx
x log x = lim
b→∞
Z b
2
dx
x log x
= lim
b→∞log log x

b
2
= lim
b→∞log log b −log log 2
= ∞.
So we expect that as t →1+, F(t) should blow up. But how does it blow up? By analyzing F ′(t)
and then integrating back, we are going to show F(t) behaves essentially like −log(t−1) as t →1+.
Using diﬀerentiation under the integral sign, for t > 1
F ′(t) =
Z ∞
2
∂
∂t

1
xt log x

dx
=
Z ∞
2
x−t(−log x)
log x
dx
= −
Z ∞
2
dx
xt
= −x−t+1
−t + 1

x=∞
x=2
= 21−t
1 −t.
We want to bound this derivative from above and below when t > 1. Then we will integrate to get
bounds on the size of F(t).
For t > 1, the diﬀerence 1 −t is negative, so 21−t < 1. Dividing both sides of this by 1 −t, which
is negative, reverses the sense of the inequality and gives
21−t
1 −t >
1
1 −t.
This is a lower bound on F ′(t). To get an upper bound on F ′(t), we want to use a lower bound
on 21−t. Since ea ≥a + 1 for all a (the graph of y = ex lies on or above its tangent line at x = 0,
which is y = x + 1),
2x = ex log 2 ≥(log 2)x + 1
for all x. Taking x = 1 −t,
(9.1)
21−t ≥(log 2)(1 −t) + 1.
When t > 1, 1 −t is negative, so dividing (9.1) by 1 −t reverses the sense of the inequality:
21−t
1 −t ≤log 2 +
1
1 −t.

<!-- page 11 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
11
This is an upper bound on F ′(t). Putting the upper and lower bounds on F ′(t) together,
(9.2)
1
1 −t < F ′(t) ≤log 2 +
1
1 −t
for all t > 1.
We are concerned with the behavior of F(t) as t →1+. Let’s integrate (9.2) from a to 2, where
1 < a < 2:
Z 2
a
dt
1 −t <
Z 2
a
F ′(t) dt ≤
Z 2
a

log 2 +
1
1 −t

dt.
Using the Fundamental Theorem of Calculus,
−log(t −1)

2
a
< F(t)

2
a
≤((log 2)t −log(t −1))

2
a
,
so
log(a −1) < F(2) −F(a) ≤(log 2)(2 −a) + log(a −1).
Manipulating to get inequalities on F(a), we have
(log 2)(a −2) −log(a −1) + F(2) ≤F(a) < −log(a −1) + F(2)
Since a −2 > −1 for 1 < a < 2, (log 2)(a −2) is greater than −log 2. This gives the bounds
−log(a −1) + F(2) −log 2 ≤F(a) < −log(a −1) + F(2)
Writing a as t, we get
−log(t −1) + F(2) −log 2 ≤F(t) < −log(t −1) + F(2),
so F(t) is a bounded distance from −log(t−1) when 1 < t < 2. In particular, F(t) →∞as t →1+.
10. A trigonometric integral
For positive numbers a and b, the arithmetic-geometric mean inequality says (a + b)/2 ≥
√
ab
(with equality if and only if a = b). Let’s iterate the two types of means: for k ≥0, deﬁne {ak}
and {bk} by a0 = a, b0 = b, and
ak = ak−1 + bk−1
2
,
bk =
p
ak−1bk−1
for k ≥1.
Example 10.1. If a0 = 1 and b0 = 2, then Table 2 gives ak and bk to 16 digits after the decimal
point. Notice how rapidly they are getting close to each other!
k
ak
bk
0
1
2
1
1.5
1.4142135623730950
2
1.4571067811865475
1.4564753151219702
3
1.4567910481542588
1.4567910139395549
4
1.4567910310469069
1.4567910310469068
Table 1. Iteration of arithmetic and geometric means.

<!-- page 12 -->
12
KEITH CONRAD
Gauss showed that for all a > 0 and b > 0, the sequences {ak} and {bk} converge very rapidly to
a common limit, which he called the arithmetic-geometric mean of a and b and wrote as M(a, b).
For example, M(1, 2) ≈1.456791031046906. Gauss discovered an integral formula for 1/M(a, b):
1
M(a, b) = 2
π
Z π/2
0
dx
p
a2 cos2 x + b2 sin2 x
.
There is no elementary formula for this integral, but if we change the exponent 1/2 in the square
root to a positive integer n then we can work out all the integrals
Fn(a, b) = 2
π
Z π/2
0
dx
(a2 cos2 x + b2 sin2 x)n
using repeated diﬀerentiation under the integral sign with respect to both a and b. (This example,
with a diﬀerent normalization and no context for where the integral comes from, is Example 4 on
the Wikipedia page for the Leibniz integral rule.)
For n = 1 we can do a direct integration:
F1(a, b) = 2
π
Z π/2
0
dx
a2 cos2 x + b2 sin2 x
= 2
π
Z π/2
0
sec2 x
a2 + b2 tan2 x dx
= 2
π
Z ∞
0
du
a2 + b2u2
where u = tan x
=
2
πa2
Z ∞
0
du
1 + (b/a)2u2
=
2
πab
Z ∞
0
dv
1 + v2
where v = (b/a)u
= 1
ab.
Now let’s diﬀerentiate F1(a, b) with respect to a and with respect to b, both by its integral
deﬁnition and by the formula we just computed for it:
∂F1
∂a = 2
π
Z π/2
0
−2a cos2 x
(a2 cos2 x + b2 sin2 x)2 dx,
∂F1
∂a = −1
a2b
and
∂F1
∂b = 2
π
Z π/2
0
−2b sin2 x
(a2 cos2 x + b2 sin2 x)2 dx,
∂F1
∂b = −1
ab2 .
Since sin2 x + cos2 x = 1, by a little algebra we can get a formula for F2(a, b):
F2(a, b) = 2
π
Z π/2
0
dx
(a2 cos2 x + b2 sin2 x)2
= −1
2a
∂F1
∂a −1
2b
∂F1
∂b
=
1
2a3b +
1
2ab3
= a2 + b2
2a3b3 .

<!-- page 13 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
13
We can get a recursion expressing Fn(a, b) in terms of ∂Fn−1/∂a and ∂Fn−1/∂b in general: for
n ≥2,
∂Fn−1
∂a
= 2
π
Z π/2
0
−2(n −1)a cos2 x
(a2 cos2 x + b2 sin2 x)n dx,
∂Fn−1
∂b
= 2
π
Z π/2
0
−2(n −1)b sin2 x
(a2 cos2 x + b2 sin2 x)n dx,
so
Fn(a, b) = −
1
2(n −1)a
∂Fn−1
∂a
−
1
2(n −1)b
∂Fn−1
∂b
= −
1
2(n −1)
1
a
∂Fn−1
∂a
+ 1
b
∂Fn−1
∂b

.
A few sample calculations of Fn(a, b) using this, starting from F1(a, b) = 1/(ab), are
F2(a, b) = a2 + b2
2a3b3 ,
F3(a, b) = 3a4 + 2a2b2 + 3b4
6a5b5
,
F4(a, b) = 5a6 + 3a4b2 + 3a2b4 + 5b6
12a7b7
.
11. Smoothly dividing by t
Let h: R →R be smooth (that is, inﬁnitely diﬀerentiable) such that h(0) = 0. The ratio h(t)/t
makes sense for t ̸= 0, and it also can be given a reasonable meaning at t = 0: from the deﬁnition
of the derivative, when t →0 we have
h(t)
t
= h(t) −h(0)
t −0
→h′(0).
Therefore the function
(11.1)
r(t) =
(
h(t)/t,
if t ̸= 0,
h′(0),
if t = 0
is continuous for all t. At t ̸= 0, r(t) is smooth by the deﬁnition of r(t), the quotient rule, and
induction. What about at t = 0?
Theorem 11.1. When h: R →R is smooth and h(0) = 0, the function r(t) in (11.1) is smooth
at t = 0.
Remark 11.2. This is easy to prove when h(t) has a power series representation around t = 0, so
the signiﬁcance of the theorem is that it holds only assuming h(t) is smooth, without being locally
expressible by power series. An example of such a function is h(t) = e−1/t2 for t ̸= 0 and h(0) = 0.
Proof. To analyze r(t) near t = 0, we will ﬁnd a diﬀerent formula for it that avoids taking separate
cases at t ̸= 0 and t = 0 by writing h(t) in a clever way with diﬀerentiation under the integral sign.
Start from
h(t) =
Z t
0
h′(u) du.
(This is correct since h(0) = 0.) For t ̸= 0, introduce the change of variables u = tx, so du = t dx.
At the boundary, if u = 0 then x = 0. If u = t then x = 1 (we can divide the equation t = tx by t
because t ̸= 0). Therefore
h(t) =
Z 1
0
h′(tx)t dx = t
Z 1
0
h′(tx) dx.
Dividing by t when t ̸= 0, we get
r(t) = h(t)
t
=
Z 1
0
h′(tx) dx.

<!-- page 14 -->
14
KEITH CONRAD
The left and right sides don’t have t in the denominator. Are they equal at t = 0 too? The left
side at t = 0 is r(0) = h′(0). The right side is
R 1
0 h′(0) dx = h′(0) too, so
(11.2)
r(t) =
Z 1
0
h′(tx) dx
for all t, including t = 0. This is a formula for h(t)/t where there is no longer a t being divided!
Now we’re set to use diﬀerentiation under the integral sign. The way we have set things up
here, we want to diﬀerentiate with respect to t; the integration variable on the right is x. We can
use diﬀerentiation under the integral sign on (11.2) when the integrand is diﬀerentiable. Since the
integrand is inﬁnitely diﬀerentiable, r(t) is inﬁnitely diﬀerentiable!
Explicitly,
r′(t) =
Z 1
0
xh′′(tx) dx
and
r′′(t) =
Z 1
0
x2h′′′(tx) dx
and more generally
r(k)(t) =
Z 1
0
xkh(k+1)(tx) dx
for all k ≥0. In particular, r(k)(0) =
R 1
0 xkh(k+1)(0) dx = h(k+1)(0)/(k + 1).
□
Remark 11.3. Whitney [15]4 proved that every smooth even function h: R →R is a smooth
function of t2: h(t) = g(t2) where g: R →R is smooth. This is straightforward when h is locally
expressible by power series around 0 (an even power series at 0 has no odd powers of t, and thus is
a power series in t2), but without such an assumption it is more subtle.
12. Counterexamples and justification
We have seen many examples where diﬀerentiation under the integral sign can be carried out
with interesting results, but we have not actually stated conditions under which (1.2) is valid.
Something does need to be checked. In [14], an incorrect use of diﬀerentiation under the integral
sign due to Cauchy is discussed, where a divergent integral is evaluated as a ﬁnite expression. Here
are two other examples where diﬀerentiation under the integral sign does not work.
Example 12.1. It is pointed out in [9, Example 6] that the formula
Z ∞
0
sin x
x
dx = π
2 ,
which we discussed at the end of Section 3, leads to an erroneous instance of diﬀerentiation under
the integral sign. Rewrite the formula as
(12.1)
Z ∞
0
sin(ty)
y
dy = π
2
for t > 0 by the change of variables x = ty. Then diﬀerentiation under the integral sign implies
Z ∞
0
cos(ty) dy = 0,
but the left side doesn’t make sense.
4Or see https://mathoverflow.net/questions/72497/.

<!-- page 15 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
15
The next example shows that even if both sides of (1.2) make sense, they need not be equal.
Example 12.2. For real numbers x and t, let
f(x, t) =



xt3
(x2 + t2)2 ,
if x ̸= 0 or t ̸= 0,
0,
if x = 0 and t = 0.
Note f(x, 0) = 0 for all x. Let
F(t) =
Z 1
0
f(x, t) dx.
When t ̸= 0,
F(t) =
Z 1
0
xt3
(x2 + t2)2 dx
=
Z 1+t2
t2
t3
2u2 du
(where u = x2 + t2)
= −t3
2u

u=1+t2
u=t2
= −
t3
2(1 + t2) + t3
2t2
=
t
2(1 + t2).
This is true when t = 0 too: F(0) =
R 1
0 f(x, 0) dx =
R 1
0 0 dx = 0, so F(t) = t/(2(1 + t2)) for all t.
Therefore F(t) is diﬀerentiable and
F ′(t) =
1 −t2
2(1 + t2)2
for all t. In particular, F ′(0) = 1
2.
Now we compute ∂
∂tf(x, t) and then
R 1
0
∂
∂tf(x, t) dx. Since f(0, t) = 0 for all t, f(0, t) is diﬀeren-
tiable in t and ∂
∂tf(0, t) = 0. For x ̸= 0, f(x, t) is diﬀerentiable in t and
∂
∂tf(x, t) = (x2 + t2)2(3xt2) −xt3 · 2(x2 + t2)2t
(x2 + t2)4
= xt2(x2 + t2)(3(x2 + t2) −4t2)
(x2 + t2)4
= xt2(3x2 −t2)
(x2 + t2)3
.
Combining both cases (x = 0 and x ̸= 0),
(12.2)
∂
∂tf(x, t) =
(xt2(3x2−t2)
(x2+t2)3 ,
if x ̸= 0,
0,
if x = 0.
In particular
∂
∂t

t=0 f(x, t) = 0. Therefore at t = 0 the left side of the “formula”
d
dt
Z 1
0
f(x, t) dx =
Z 1
0
∂
∂tf(x, t) dx.

<!-- page 16 -->
16
KEITH CONRAD
is F ′(0) = 1/2 and the right side is
R 1
0
∂
∂t

t=0 f(x, t) dx = 0. The two sides are unequal!
The problem in this example is that
∂
∂tf(x, t) is not a continuous function of (x, t). Indeed, the
denominator in the formula in (12.2) is (x2 + t2)3, which has a problem near (0, 0). Speciﬁcally,
while this derivative vanishes at (0, 0), if we let (x, t) →(0, 0) along the line x = t, then on this
line ∂
∂tf(x, t) has the value 1/(4x), which does not tend to 0 as (x, t) →(0, 0).
Theorem 12.3. The equation
d
dt
Z b
a
f(x, t) dx =
Z b
a
∂
∂tf(x, t) dx,
where a could be −∞and b could be ∞, is valid at a real number t = t0 in the sense that both sides
exist and are equal, provided the following two conditions hold:
• f(x, t) and
∂
∂tf(x, t) are continuous functions of two variables when x is in the range of
integration and t is in some interval around t0,
• for t in some interval around t0 there are upper bounds |f(x, t)| ≤A(x) and | ∂
∂tf(x, t)| ≤
B(x), both bounds being independent of t, such that
R b
a A(x) dx and
R b
a B(x) dx exist.
Proof. See [10, pp. 337–339], which uses the deﬁnition of the derivative and the Mean Value The-
orem. If the interval of integration is inﬁnite,
R b
a A(x) dx and
R b
a B(x) dx are improper. A second
proof [10, p. 340] obtains the theorem from the Fundamental Theorem of Calculus and swapping
the order of a double integral.5
□
In Table 2 we include choices for A(x) and B(x) for the functions we have treated. Since the
calculation of a derivative at a point only depends on an interval around the point, we have replaced
a t-range such as t > 0 with t ≥c > 0 in some cases to obtain choices for A(x) and B(x).
Section
f(x, t)
x range
t range
t we want
A(x)
B(x)
2
xne−tx
[0, ∞)
t ≥c > 0
1
xne−cx
xn+1e−cx
3
e−tx sin x
x
(0, ∞)
t ≥c > 0
0
e−cx
e−cx
4
1
1+x2 e−t2(1+x2)/2
[0, ∞)
t ≥c > 0
all t ≥0
1
1+x2
1
√ee−c2x2/2
5
xne−tx2
R
t ≥c > 0
1
xne−cx2
xn+2e−cx2
6
cos(tx)e−x2/2
[0, ∞)
R
all t
e−x2/2
|x|e−x2/2
7
xt−1e−x
(0, ∞)
0 < t ≤c
1/2, 1, 3/2, 2
xc−1e−x
xc−1| log x|e−x
8
xt −1
log x
(0, 1]
0 < t < c
1
1−xc
log x
1
9
1
xt log x
[2, ∞)
t ≥c > 1
t > 1
1
x2 log x
1
xc
11
xkh(k+1)(tx)
[0, 1]
|t| < c
0
max
|y|≤c |h(k+1)(y)|
max
|y|≤c |h(k+2)(y)|
Table 2. Summary
We did not put the function from Section 10 in the table since it would make the width too long
and it depends on two parameters. Putting the parameter into the coeﬃcient of cos2 x in Section 10,
we can take f(x, t) = 1/(t2 cos2 x+b2 sin2 x)n for x ∈[0, π/2], 0 < c ≤t ≤c′ (that is, keep t bounded
away from 0 and ∞), A(x) = 1/(c2 cos2 x + b2 sin2 x)n and B(x) = 2c′n/(c2 cos2 x + b2 sin2 x)n+1.
5This second proof is written with b = ∞, but the argument can be adapted to ﬁnite b.

<!-- page 17 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
17
Corollary 12.4. If a(t) and b(t) are both diﬀerentiable on an open interval (c1, c2), then
d
dt
Z b(t)
a(t)
f(x, t) dx =
Z b(t)
a(t)
∂
∂tf(x, t) dx + f(b(t), t)b′(t) −f(a(t), t)a′(t)
for (x, t) ∈[α, β] × (c1, c2), where α < β and the following conditions are satisﬁed:
• f(x, t) and
∂
∂tf(x, t) are continuous on [α, β] × (c1, c2),
• for all t ∈(c1, c2), a(t) ∈[α, β] and b(t) ∈[α, β],
• for (x, t) ∈[α, β] × (c1, c2), there are upper bounds |f(x, t)| ≤A(x) and | ∂
∂tf(x, t)| ≤B(x)
such that
R β
α A(x) dx and
R β
α B(x) dx exist.
Proof. This is a consequence of Theorem 12.3 and the chain rule for multivariable functions. Set a
function of three variables
I(t, a, b) =
Z b
a
f(x, t) dx
for (t, a, b) ∈(c1, c2) × [α, β] × [α, β]. (Here a and b are not functions of t, but variables.) Then
(12.3)
∂I
∂t (t, a, b) =
Z b
a
∂
∂tf(x, t) dx,
∂I
∂a(t, a, b) = −f(a, t),
∂I
∂b (t, a, b) = f(b, t),
where the ﬁrst formula follows from Theorem 12.3 (its hypotheses are satisﬁed for each a and
b in [α, β]) and the second and third formulas are the Fundamental Theorem of Calculus. For
diﬀerentiable functions a(t) and b(t) with values in [α, β] for c1 < t < c2, by the chain rule
d
dt
Z b(t)
a(t)
f(x, t) dx = d
dtI(t, a(t), b(t))
= ∂I
∂t (t, a(t), b(t)) dt
dt + ∂I
∂a(t, a(t), b(t)) da
dt + ∂I
∂b (t, a(t), b(t)) db
dt
=
Z b(t)
a(t)
∂f
∂t (x, t) dx −f(a(t), t)a′(t) + f(b(t), t)b′(t) by (12.3).
□
A version of diﬀerentiation under the integral sign for t a complex variable is in [11, pp. 392–393].
Example 12.5. For a parametric integral
R t
a f(x, t) dx with a ﬁxed, Corollary 12.4 tells us
(12.4)
d
dt
Z t
a
f(x, t) dx =
Z t
a
∂
∂tf(x, t) dx + f(t, t)
for (x, t) ∈[α, β] × (c1, c2) provided that (i) f and ∂f/∂t are continuous for (x, t) ∈[α, β] × (c1, c2),
(ii) α ≤a ≤β and (c1, c2) ⊂[α, β], and (iii) there are bounds |f(x, t)| ≤A(x) and | ∂
∂tf(x, t)| ≤B(x)
for (x, t) ∈[α, β] × (c1, c2) such that the integrals
R β
α A(x) dx and
R β
α B(x) dx both exist.
We will apply (12.4) to the integral
F(t) =
Z t
0
log(1 + tx)
1 + x2
dx
for t ≥0. Obviously F(0) = 0. Here f(x, t) = log(1 + tx)/(1 + x2) and ∂
∂tf(x, t) =
x
(1+tx)(1+x2). To
include t = 0 in the setting of Corollary 12.4, the open t-interval should include 0. Therefore we’re
going to consider F(t) for small negative t too.
Use (x, t) ∈[−δ, 1/(2ε)] × (−ε, 1/(2δ)) for small ε and δ (between 0 and 1/2). In the notation
of Corollary 12.4, α = −δ, β = 1/(2ε), c1 = −ε, and c2 = 1/(2δ). To have (c1, c2) ⊂[α, β] is
equivalent to requiring ε < δ (e.g., ε = δ/2). We chose the bounds on x and t to keep 1 + xt

<!-- page 18 -->
18
KEITH CONRAD
away from 0: −1/2 < xt < 1/(4εδ), so 1/2 < 1 + xt < 1 + 1/(4εδ).6 That makes | log(1 + xt)|
bounded above and 1+tx bounded below, so |f| and |∂f/∂t| are both bounded above by constants
(depending on ε and δ), so (12.4) is justiﬁed with A(x) and B(x) being constant functions for
x ∈[α, β]. Thus when 0 < ε < δ < 1 and −ε < t < 1/(2δ),
F ′(t) =
Z t
0
x
(1 + tx)(1 + x2) dx + log(1 + t2)
1 + t2
=
Z t
0
1
1 + t2

−t
1 + tx +
t
1 + x2 +
x
1 + x2

dx + log(1 + t2)
1 + t2
.
After antidiﬀerentiating the three terms in the integral with respect to x,
F ′(t) =
 −1
1 + t2 log(1 + tx) +
t
1 + t2 arctan(x) + log(1 + x2)
2(1 + t2)

t
0
+ log(1 + t2)
1 + t2
= −log(1 + t2)
1 + t2
+ t arctan(t)
1 + t2
+ log(1 + t2)
2(1 + t2) + log(1 + t2)
1 + t2
= t arctan(t)
1 + t2
+ log(1 + t2)
2(1 + t2) .
(12.5)
Letting δ →0+ shows (12.5) holds for all t ≥0. By the Fundamental Theorem of Calculus
F(t) = F(t) −F(0) =
Z t
0
F ′(y) dy =
Z t
0
y arctan(y)
1 + y2
+ log(1 + y2)
2(1 + y2)

dy.
Using integration by parts on the ﬁrst integrand with u = arctan(y) and dv =
y
1+y2 dy,
F(t) = uv

t
0
−
Z t
0
v du +
Z t
0
log(1 + y2)
2(1 + y2) dy
= arctan(y)log(1 + y2)
2

t
0
−
Z t
0
log(1 + y2)
2(1 + y2) dy +
Z t
0
log(1 + y2)
2(1 + y2) dy
= 1
2 arctan(t) log(1 + t2),
so
(12.6)
Z t
0
log(1 + tx)
1 + x2
dx = 1
2 arctan(t) log(1 + t2).
for t ≥0. Both sides are odd functions of t, so (12.6) holds for all t. Setting t = 1,
(12.7)
Z 1
0
log(1 + x)
1 + x2
dx = 1
2 arctan(1) log 2 = π log 2
8
.
The equation (12.7) is derived in another way in Exercise 16.
13. The Fundamental Theorem of Algebra
By diﬀerentiating under the integral sign we will prove the fundamental theorem of algebra: each
nonconstant polynomial p(z) with coeﬃcients in C has a root in C. The proof is by Schep [13].
6Since −δ ≤x ≤1/(2ε) and −ε < t < 1/(2δ), xt < max(εδ, 1/(4εδ)), and the maximum is 1/(4εδ) when ε, δ < 1/2.

<!-- page 19 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
19
Arguing by contradiction, assume p(z) ̸= 0 for all z ∈C. For r ≥0, consider the following
integral around a circle of radius r centered at the origin:
I(r) =
Z 2π
0
dθ
p(reiθ).
This integral makes sense since the denominator is never 0, so 1/p(z) is continuous on C. Let
f(θ, r) = 1/p(reiθ), so I(r) =
R 2π
0
f(θ, r) dθ.
We will prove three properties of I(r):
(1) Theorem 12.3 can be applied to I(r) for r > 0,
(2) I(r) →0 as r →∞,
(3) I(r) →I(0) as r →0+ (continuity at r = 0).
Taking these for granted, let’s see how a contradiction occurs. For r > 0,
I′(r) =
Z 2π
0
∂
∂rf(θ, r) dθ =
Z 2π
0
−p′(reiθ)eiθ
p(reiθ)2
dθ.
Since
∂
∂θf(θ, r) = −p′(reiθ)
p(reiθ)2 ireiθ = ir ∂
∂rf(θ, r),
for r > 0 we have
I′(r) =
Z 2π
0
∂
∂rf(θ, r) dθ =
Z 2π
0
1
ir
∂
∂θf(θ, r) dθ = 1
ir f(θ, r)

θ=2π
θ=0
= 1
ir
 1
p(r) −
1
p(r)

= 0.
Thus I(r) is constant for r > 0. Since I(r) →0 as r →∞, the constant is zero: I(r) = 0 for r > 0.
Since I(r) →I(0) as r →0+ we get I(0) = 0, which is false since I(0) = 2π/p(0) ̸= 0.
It remains to prove the three properties of I(r).
(1) Theorem 12.3 can be applied to I(r) for r > 0:
Since p(z) and p′(z) are both continuous on C, the functions f(θ, r) and (∂/∂r)f(θ, r) are
continuous for θ ∈[0, 2π] and all r ≥0. This conﬁrms the ﬁrst condition in Theorem 12.3.
For each r0 > 0 the set {(θ, r) : θ ∈[0, 2π], r ∈[0, 2r0] is closed and bounded, so the functions
f(θ, r) and (∂/∂r)f(θ, r) are both bounded above by a constant (independent of r and θ) on this
set. The range of integration [0, 2π] is ﬁnite, so the second condition in Theorem 12.3 is satisﬁed
using constants for A(θ) and B(θ).
(2) I(r) →0 as r →∞: Let p(z) have leading term czd, with d = deg p(z) ≥1. As r →∞,
|p(reiθ)|/|reiθ|d →|c| > 0, so for all large r we have |p(reiθ)| ≥|c|rd/2. For such large r,
|I(r)| ≤
Z 2π
0
dθ
|p(reiθ)| ≤
Z 2π
0
dθ
|c|rd/2 = 4π
|c|rd ,
and the upper bound tends to 0 as r →∞since d > 0, so I(r) →0 as r →∞.
(3) I(r) →I(0) as r →0+: For r > 0,
(13.1)
I(r) −I(0) =
Z 2π
0

1
p(reiθ) −
1
p(0)

dθ =⇒|I(r) −I(0)| ≤
Z 2π
0

1
p(reiθ) −
1
p(0)
 dθ.
Since 1/p(z) is continuous at 0, for ε > 0 there is δ > 0 such that |z| < δ ⇒|1/p(z) −1/p(0)| < ε.
Therefore if 0 < r < δ, (13.1) implies |I(r) −I(0)| ≤
R 2π
0
ε dθ = 2πε. Let ε →0+ and we’re done.

<!-- page 20 -->
20
KEITH CONRAD
14. An example needing a change of variables
Our next example is taken from [1, pp. 78, 84-86]. For all t ∈R, we will show by diﬀerentiation
under the integral sign that
(14.1)
Z
R
cos(tx)
1 + x2 dx = πe−|t|.
For example,
Z
R
cos x
1 + x2 dx = π
e ,
Z
R
cos(2x)
1 + x2 dx = π
e2 ,
Z
R
cos x
4 + x2 dx = 1
2
Z
R
cos(2x)
1 + x2 dx = π
2e2 .
In (14.1), set f(x, t) = cos(tx)/(1+x2). Since f(x, t) is continuous and |f(x, t)| ≤1/(1+x2), the
integral in (14.1) exists for all t. A graph of πe−|t| is in Figure 1. Note πe−|t| is not diﬀerentiable
at 0, so we shouldn’t expect to prove (14.1) at t = 0 by diﬀerentiation under the integral sign.
Figure 1. Graph of y = πe−|t|.
We’ll verify (14.1) at t = 0 using elementary calculus:
(14.2)
Z
R
dx
1 + x2 = arctan x

∞
−∞
= π
2 −−π
2
= π.
Since the integral in (14.1) is an even function of t, to compute the integral for t ̸= 0 it suﬃces to
treat the case t > 0.7
Set
F(t) =
Z
R
cos(tx)
1 + x2 dx.
If we try to compute F ′(t) for t > 0 using diﬀerentiation under the integral sign, we get
(14.3)
F ′(t) ?=
Z
R
∂
∂t
cos(tx)
1 + x2

dx = −
Z
R
x sin(tx)
1 + x2 dx.
No upper bound | ∂
∂tf(x, t)| ≤B(x) for t > 0 in Theorem 12.3 justiﬁes diﬀerentiating F(t) under
the integral sign or that even implies F(t) is diﬀerentiable for t > 0. Indeed, for x near a large
odd multiple of (π/2)/t, the integrand in (14.3) is approximately x/(1 + x2) ≈1/x, which is not
integrable for large x. That does not mean (14.3) is false, but if we did not see (14.1) already then
we might think F(t) is diﬀerentiable for all t even though F(t) is not diﬀerentiable at t = 0.
7If you know complex analysis, you can get (14.1) for t > 0 from the residue theorem, viewing cos(tx) as the real
part of eitx. If you know Fourier analysis, you can interpret (14.1) as saying 1/(1 + x2) has Fourier transform πe−|t|,
where a function f(x) has Fourier transform bf(t) =
R
R f(x)e−ixt dx.

<!-- page 21 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
21
Even though we raised suspicions about (14.3), let’s use it without focusing on rigor for now:
F ′(t) = −
Z
R
x sin(tx)
1 + x2 dx
(14.4)
= −
Z
R
x2 sin(tx)
x(1 + x2) dx
= −
Z
R
(1 + x2 −1) sin(tx)
x(1 + x2)
dx
= −
Z
R
sin(tx)
x
dx +
Z
R
sin(tx)
x(1 + x2) dx.
Making the change of variables u = tx in the ﬁrst integral, since t > 0 we get
F ′(t) = −
Z
R
sin(u)
u
du +
Z
R
sin(tx)
x(1 + x2) dx.
(14.5)
The ﬁrst integral is a constant (it’s π by (A.2), but that’s irrelevant), and it goes away if we
diﬀerentiate both sides with respect to t and once more use diﬀerentiation under the integral sign
without justifying that:
F ′′(t) =
Z
R
x cos(tx)
x(1 + x2) dx =
Z
R
cos(tx)
1 + x2 dx = F(t).
Each solution of F ′′(t) = F(t) on R has the form aet + be−t. Since F(0) = π by (14.2), a + b = π.
(This hides errors: the ODE for F(t) was never shown at t = 0, and (14.4) and (14.5) are inconsistent
about the value of F ′(0), with the ﬁrst saying F ′(0) = 0 and the second saying F ′(0) ̸= 0.) Thus
(14.6)
F(t) :=
Z
R
cos(tx)
1 + x2 dx = aet + (π −a)e−t = a(et −e−t) + πe−t.
To determine a, let t →∞in (14.6). The integral there tends to 0 by the Riemann–Lebesgue
lemma from Fourier analysis, but we can also explain it directly with integration by parts: letting
u = 1/(1 + x2) and dv = cos(tx) dx, so du = −2x/(1 + x2)2 dx and v = sin(tx)/t,
F(t) =
Z
R
cos(tx)
1 + x2 dx =
sin(tx)
t(1 + x2)

x=∞
x=−∞
+ 2
t
Z
R
x sin(tx)
(1 + x2)2 dx = 2
t
Z
R
x sin(tx)
(1 + x2)2 dx.
Since | sin(tx)| ≤1, |F(t)| ≤C/t for a constant C that’s independent of t, so F(t) →0 as t →∞.
Thus a(et +e−t)+πe−t →0 as t →∞. This implies a = 0, so F(t) = πe−t for t > 0, as in (14.1).8
That derivation of (14.1) when t > 0 had several invalid steps. To derive it rigorously, we make
a change of variables. Fixing t > 0, set y = tx, so dy = t dx and
(14.7)
F(t) =
Z
R
cos y
1 + y2/t2
dy
t
=
Z
R
t cos y
t2 + y2 dy.
This new second integral for F(t) when t > 0 will be accessible to justifying diﬀerentiation under
the integral sign. (Although the new integral in (14.7) is an odd function of t while F(t) is an even
function of t, there is no contradiction since the new integral for F(t) was derived only for t > 0.)
Fix c′ > c > 0. For t ∈(c, c′), the integrand in
Z
R
t cos y
t2 + y2 dy
8Some webpages and online videos compute integrals like F(t) by this method with mistakes.

<!-- page 22 -->
22
KEITH CONRAD
is bounded above in absolute value by t/(t2 + y2) ≤c′/(c2 + y2), which is independent of t and
integrable over R. The t-partial derivative of the integrand is (y2 −t2)(cos y)/(t2 + y2)2, which
is bounded above in absolute value by (y2 + t2)/(t2 + y2)2 = 1/(t2 + y2) ≤1/(c2 + y2), which is
independent of t and integrable over R. This justiﬁes the use of diﬀerentiation under the integral
sign by Theorem 12.3: for c < t < c′, and hence for all t > 0 since we never speciﬁed c or c′,
F ′(t) =
Z
R
∂
∂t
 t cos y
t2 + y2

dy =
Z
R
y2 −t2
(t2 + y2)2 cos y dy.
Next we’ll compute F ′′(t) by diﬀerentiation under the integral sign on F ′(t). For 0 < c < t < c′,
check the t-partial derivative of the integrand is bounded above in absolute value by a function of
y that is independent of t and is integrable over R (exercise), so by Theorem 12.3, for t > 0
F ′′(t) =
Z
R
∂2
∂t2
 t cos y
t2 + y2

dy =
Z
R
∂2
∂t2

t
t2 + y2

cos y dy.
Check that (∂2/∂t2)(t/(t2 + y2)) = −(∂2/∂y2)(t/(t2 + y2)), so
F ′′(t) = −
Z
R
∂2
∂y2

t
t2 + y2

cos y dy.
Using integration by parts on this formula for F ′′(t) twice (starting with u = −cos y and dv =
(∂2/∂y2)(t/(t2 + y2)), we obtain for t > 0
F ′′(t) = −
Z
R
∂
∂y

t
t2 + y2

sin y dy =
Z
R

t
t2 + y2

cos y dy = F(t).
The equation F ′′(t) = F(t) for t > 0 is what we found by the nonrigorous method earlier.
How can we show F(t) = aet + be−t for t > 0 (not t ∈R)? One way is by a strong enough
existence/uniqueness theorem for linear ODEs. To see another way, set G(t) = F(t) + F ′(t) for
t > 0, so
G′(t) = F ′(t) + F ′′(t) = F ′(t) + F(t) = G(t).
Then (G(t)/et)′ = (etG′(t) −G(t)et)/e2t = 0, so G(t)/et = c for t > 0, where c is a constant. That
makes F(t) + F ′(t) = cet, so F ′(t) = −F(t) + cet. Set H(t) = F(t) −(c/2)et when t > 0. Then
H′(t) = F ′(t) −c
2et = −

F(t) −c
2et′
= −H(t),
so (H(t)/e−t)′ = (e−tH′(t)+H(t)e−t)/e−2t = 0. Thus H(t)/e−t = b for t > 0, where b is a constant,
so
F(t) = c
2et + H(t) = c
2et + be−t
for t > 0. Setting a = c/2, there are constants a and b such that
(14.8)
F(t) :=
Z
R
cos(tx)
1 + x2 dx = aet + be−t
for t > 0. To determine a and b, we look at (14.8) as t →0+ and as t →∞.
As t →0+, the integrand in (14.8) tends pointwise to 1/(1 + x2), so we expect F(t) to tend to
F(0) =
R
R dx/(1 + x2) = π (see (14.2)) as t →0+. To justify this, we will bound
|F(t) −F(0)| =

Z
R
cos(tx)
1 + x2 dx −
Z
R
dx
1 + x2
 ≤
Z
R
| cos(tx) −1|
1 + x2
dx.

<!-- page 23 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
23
For N > 0, break up the integral over R into the regions |x| ≤N and |x| ≥N. We have
Z
R
| cos(tx) −1|
1 + x2
dx ≤
Z
|x|≤N
| cos(tx) −1|
1 + x2
dx +
Z
|x|≥N
2
1 + x2 dx
≤
Z
|x|≤N
t|x|
1 + x2 dx +
Z
|x|≥N
2
1 + x2 dx
= t
Z
|x|≤N
|x|
1 + x2 dx + 4
π
2 −arctan N

.
We can make π/2−arctan N as small as we wish by taking N suﬃciently large, and for such an N,
we can make the ﬁrst term as small as we wish by taking t suﬃciently small. Thus F(t) →F(0)
as t →0+. Returning to (14.8), letting t →0+ we obtain π = a + b, so for all t > 0,
(14.9)
Z
R
cos(tx)
1 + x2 dx = aet + (π −a)e−t = a(et −e−t) + πe−t.
Letting t →∞in (14.9), the left side tends to 0 by the estimate |F(t)| ≤C/t derived (correctly)
in the paragraph right after (14.6), so a = 0. Thus F(t) = πe−t for t > 0.
Remark 14.1. Now that we know F(t) = πe−t for t > 0, so F ′(t) = −πe−t, the formal diﬀerenti-
ation under the integral sign that led to (14.3) suggests that
Z
R
x sin(tx)
1 + x2 dx = πe−t for t > 0.
This integral is subtle: it is not absolutely convergent. The formula above can be justiﬁed by the
residue theorem in complex analysis (deﬁning
R
R as limR→∞
R R
−R). That formula is not true at
t = 0: the integral at t = 0 is 0, but πe−t at t = 0 is π. The integral is discontinuous at t = 0.9
15. Fourier transform of a Gaussian
For a continuous function f : R →C that is rapidly decreasing at ±∞, its Fourier transform is
the function Ff : R →C deﬁned by
(15.1)
(Ff)(y) =
Z ∞
−∞
f(x)e−ixy dx =
Z ∞
−∞
f(x)(cos(xy) −i sin(xy)) dx.
For example, (Ff)(0) =
R ∞
−∞f(x) dx. This integral transform shows up all over the place in pure
and applied analysis. We will use diﬀerentiation under the integral sign to compute the Fourier
transform of Gaussian functions e−ax2/2 where a > 0, ﬁrst for a = 1 and then for all a > 0.
When f(x) = e−x2/2, diﬀerentiate both sides of the equation
(Ff)(y) =
Z ∞
−∞
e−x2/2e−ixy dx
with respect to y, using diﬀerentiation under the integral sign for the right side:
(15.2)
(Ff)′(y) =
Z ∞
−∞
−ixe−x2/2e−ixy dx = −i
Z ∞
−∞
xe−x2/2e−ixy dx.
Diﬀerentiation under the integral sign here can be justiﬁed by applying Theorem 12.3 to the real
and imaginary parts of (Ff)(y): let f(x, y) be e−x2/2 cos(xy) or −e−x2/2 sin(xy), A(x) = e−x2/2,
and B(x) = |x|e−x2/2 since | cos(xy)| ≤1 and | sin(xy)| ≤1 for all real numbers x and y.
9Since F(t) = πe−|t| for all t, in the sense of distributions F ′(t) = −πsgn(t)e−|t| and F ′′(t) = F(t) −2πδ(t).

<!-- page 24 -->
24
KEITH CONRAD
Apply integration by parts (for complex-valued functions) to the last integral in (15.2) using
u = e−ixy and dv = xe−x2/2 dx, with du = −iye−ixy dx and v = −e−x2/2:
Z ∞
−∞
xe−x2/2e−ixy dx =
Z ∞
−∞
u dv
= uv

x=∞
x=−∞
−
Z ∞
−∞
v du
= −e−ixy
ex2/2 v

x=∞
x=−∞
−iy
Z ∞
−∞
e−x2/2e−ixy dx
= −iy(Ff)(y).
Thus (15.2) becomes
(Ff)′(y) = −i(−i)y(Ff)(y) = −y(Ff)(y).
The solutions to the diﬀerential equation g′(y) = −yg(y) are g(y) = Ce−y2/2 for constant C, so
f(x) = e−x2/2 =⇒(Ff)(y) = Ce−y2/2
for some C. To determine C, set y = 0 on both sides:
R ∞
−∞e−x2/2 dx = C. That integral is
√
2π by
Section 4 (another use of diﬀerentiation under the integral sign), so
(15.3)
f(x) = e−x2/2 =⇒(Ff)(y) =
√
2πe−y2/2.
For a > 0, we can calculate the Fourier transform of e−ax2/2 by a change of variables and (15.3):
Z ∞
−∞
e−ax2/2e−ixy dx =
Z ∞
−∞
e−t2/2e−ity/√a dt
√a where t = √ax
=
1
√a(Ff)
 y
√a

=
1
√a
√
2πe−(y/√a)2/2 by (15.3)
=
r
2π
a e−y2/(2a).
This calculation shows that, up to a scaling factor, a highly peaked Gaussian (e−ax2/2 for large
a) has a Fourier transform that is spread out (e−y2/(2a) for small 1/a) and a spread out Gaussian
(e−ax2/2 for small a) has a Fourier transform that is highly peaked (e−y2/(2a) for large 1/a). The
Fourier transform’s eﬀect of exchanging highly peaked and spread out Gaussians is a mathematical
expression of the Heisenberg Uncertainty Principle from quantum mechanics.
16. Exercises
1. For t > 0, show by calculus that
Z ∞
0
dx
x2 + t2 = π
2t and then prove by diﬀerentiation under
the integral sign that
Z ∞
0
dx
(x2 + t2)2 = π
4t3 ,
Z ∞
0
dx
(x2 + t2)3 = 3π
16t5 , and
Z ∞
0
dx
(x2 + t2)n =
2n −2
n −1

π
(2t)2n−1 for all n ≥1.

<!-- page 25 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
25
2. Starting from the formula
Z
R
cos(tx)
1 + x2 dx = π
et in (14.1) for t > 0, make a change of variables
and then diﬀerentiate under the integral sign to prove
Z
R
cos x
(x2 + t2)2 dx = π(t + 1)
2t3et
if t > 0.
3. From the formula
Z ∞
0
e−tx sin x
x
dx = π
2 −arctan t for t > 0, in Section 3, use a change of
variables to obtain a formula for
Z ∞
0
e−ax sin(bx)
x
dx when a and b are positive. Then use dif-
ferentiation under the integral sign with respect to b to ﬁnd a formula for
Z ∞
0
e−ax cos(bx) dx
when a and b are positive. (Diﬀerentiation under the integral sign with respect to a will
produce a formula for
Z ∞
0
e−ax sin(bx) dx, but that would be circular in our approach since
we used that integral in our derivation of the formula for
Z ∞
0
e−tx sin x
x
dx in Section 3.)
4. By the formula
Z ∞
0
e−tx sin x
x
dx = π
2 −arctan t for t > 0, let x = ay for a > 0 to see
Z ∞
0
e−tay sin(ay)
y
dy = π
2 −arctan t,
so the integral on the left is independent of a and thus has a-derivative 0. Diﬀerentiation
under the integral sign, with respect to a, implies
Z ∞
0
e−tay(cos(ay) −t sin(ay)) dy = 0.
Verify that this application of diﬀerentiation under the integral sign is valid when a > 0
and t > 0. What happens if t = 0?
5. Show
Z ∞
0
sin(tx)
x(x2 + 1) dx = π
2 (1−e−t) for t > 0 by justifying diﬀerentiation under the integral
sign and using (14.1).
6. Prove
Z ∞
0
e−tx cos x −1
x
dx = log

t
√
1 + t2

for t > 0. What happens to the integral as
t →0+?
7. Prove
Z ∞
0
log(1 + t2x2)
1 + x2
dx = π log(1 + t) for t > 0 (it is obvious for t = 0). Then deduce,
for a > 0 and b > 0,
Z ∞
0
log(1 + a2x2)
b2 + x2
dx = π log(1 + ab)
b
.
8. Prove
Z ∞
0
(e−x −e−tx) dx
x = log t for t > 0 by justifying diﬀerentiation under the integral
sign. This is (8.2) for t > −1. Deduce that
Z ∞
0
(e−ax −e−bx) dx
x = log(b/a) for a > 0 and
b > 0.

<!-- page 26 -->
26
KEITH CONRAD
9. Prove
Z ∞
0
e−1
2 x2−t2
2x2 dx =
rπ
2 e−|t| for all t by justifying diﬀerentiation under the integral
sign for t > 0.10 (As in Section 14, the integral is not diﬀerentiable at t = 0.) Deduce that
Z ∞
0
e−ax2−b/x2 dx =
√π
2√ae−2
√
ab for a > 0 and b > 0. (Hint: Let F(t) be the integral. Use
diﬀerentiation under the integral sign and a change of variables to show F ′(t) = −F(t) if
t > 0.)
10. In calculus textbooks, formulas for the indeﬁnite integrals
Z
xn sin x dx and
Z
xn cos x dx
are derived recursively using integration by parts. Find formulas for these integrals when
n = 1, 2, 3, 4 using diﬀerentiation under the integral sign starting with the formulas
Z
cos(tx) dx = sin(tx)
t
,
Z
sin(tx) dx = −cos(tx)
t
for t > 0. The integrals
R
xne−x dx can be worked out in a similar way11 from
R
e−tx dx =
e−tx/t for t > 0.
11. Here is another approach to (12.7). For t ∈R let F(t) =
Z 1
0
log(1 + tx)
1 + x2
dx (the upper
bound of integration is 1, not t). Compute F ′(t) explicitly using a partial fraction decom-
position and then show F(1) =
R 1
0 F ′(t) dt = −F(1) + (π/4) log 2 to solve for F(1).
12. If you are familiar with integration of complex-valued functions, show for y ∈R that
Z ∞
−∞
e−(x+iy)2 dx =
√
2π.
In other words, show the integral on the left side is independent of y. (Hint: Use diﬀeren-
tiation under the integral sign to compute the y-derivative of the left side.)
Appendix A. Justifying passage to the limit in a sine integral
In Section 3 we derived the equation
(A.1)
Z ∞
0
e−tx sin x
x
dx = π
2 −arctan t
for t > 0,
which by naive passage to the limit as t →0+ suggests that
(A.2)
Z ∞
0
sin x
x
dx = π
2 .
To prove (A.2), we will show by two methods that
R ∞
0
sin x
x
dx exists and that as t →0+,
(A.3)
Z ∞
0
sin x
x
dx −
Z ∞
0
e−tx sin x
x
dx =
Z ∞
0
(1 −e−tx)sin x
x
dx →0.
Then (A.3) implies (A.2) since
R ∞
0 e−tx(sin x)/x dx →π/2 as t →0+ by (A.1).
10This example was brought to my attention by Gregory Markowsky. The earliest reference for it that I know is
a calculus textbook [2, p. 106–107] from 1888.
11This way to treat
R
x2e−x dx was on The Big Bang Theory: https://www.youtube.com/watch?v=2ZZC7UO7fvA.

<!-- page 27 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
27
Method 1: Alternating series. On [kπ, (k + 1)π] where k is an integer, sin x = (−1)k| sin x|, so
convergence of
R ∞
0
sin x
x
dx = limb→∞
R b
0
sin x
x
dx is equivalent to convergence of the alternating series
(A.4)
X
k≥0
Z (k+1)π
kπ
sin x
x
dx =
X
k≥0
(−1)k
Z (k+1)π
kπ
| sin x|
x
dx.
This series is not absolutely convergent: 1/x on [kπ, (k + 1)π] has upper and lower bounds 1/kπ
and 1/(k + 1)π, so
(A.5)
2
(k + 1)π ≤
Z (k+1)π
kπ
| sin x|
x
dx ≤2
kπ
since
R (k+1)π
kπ
| sin x| dx = 2. Thus
X
k≥0
Z (k+1)π
kπ
| sin x|
x
dx ≥
X
k≥0
2
(k + 1)π = 2
π
X
k≥1
1
k = ∞.
To show the alternating series (A.4) converges, we will use the alternating series test. The terms
ak =
R (k+1)π
kπ
| sin x|
x
dx are monotonically decreasing:
ak+1 =
Z (k+2)π
(k+1)π
| sin x|
x
dx =
Z (k+1)π
kπ
| sin(x + π)|
x + π
dx =
Z (k+1)π
kπ
| sin x|
x + π dx < ak.
We have ak ≤2/(kπ) for k ≥1 by (A.5), so ak →0. Thus
R ∞
0
sin x
x
dx = P
k≥0(−1)kak converges.
To show the right side of (A.3) tends to 0 as t →0+, we write it as an alternating series. Writing
the interval of integration [0, ∞) as the union of intervals [kπ, (k + 1)π) for k ≥0,
(A.6)
Z ∞
0
(1 −e−tx)sin x
x
dx =
X
k≥0
(−1)kIk(t),
where Ik(t) =
Z (k+1)π
kπ
(1 −e−tx)| sin x|
x
dx.
Since 1 −e−tx > 0 for t > 0 and x > 0, the series P
k≥0(−1)kIk(t) is alternating. The upper
bound 1 −e−tx < 1 tells us Ik(t) ≤1/k for k ≥1 by the same reasoning we used on ak above, so
Ik(t) →0 as k →∞. To show the terms Ik(t) are monotonically decreasing with k, set this up as
the inequality
(A.7)
Ik(t) −Ik+1(t) > 0 for t > 0.
Each Ik(t) is a function of t for all t, not just t > 0 (note Ik(t) only involves integration on a
bounded interval). The diﬀerence Ik(t) −Ik+1(t) vanishes when t = 0 (in fact both terms are then
0), and I′
k(t) =
R (k+1)π
kπ
e−tx| sin x| dx for all t by diﬀerentiation under the integral sign, so (A.7)
would follow from the derivative inequality I′
k(t) −I′
k+1(t) > 0 for t > 0. By a change of variables
y = x −π in the integral for I′
k+1(t),
I′
k+1(t) =
Z (k+1)π
kπ
e−t(y+π)| sin(y + π)| dy = e−tπ
Z (k+1)π
kπ
e−ty| sin y| dy < I′
k(t).
This completes the proof that the series in (A.6) for t > 0 satisﬁes the alternating series test.
If we truncate the series P
k≥0(−1)kIk(t) after the Nth term, the magnitude of the error is no
greater than the absolute value of the next term:
X
k≥0
(−1)kIk(t) =
N
X
k=0
(−1)kIk(t) + rN,
where |rN| ≤|IN+1(t)| ≤
1
N + 1.

<!-- page 28 -->
28
KEITH CONRAD
Since 0 ≤1 −e−y ≤y for y ≥0,

N
X
k=0
(−1)kIk(t)
 ≤
Z (N+1)π
0
(1 −e−tx)| sin x|
x
dx =
Z (N+1)π
0
t dx = t(N + 1)π.
Thus

Z ∞
0
(1 −e−tx)sin x
x
dx
 =

X
k≥0
(−1)kIk(t)

≤

N
X
k=0
(−1)kIk(t)
 + |rN|
≤t(N + 1)π +
1
N + 1.
For ε > 0 we can make the second term at most ε/2 by a suitable choice of N. Then the ﬁrst term
is at most ε/2 for all small enough t (depending on N), and that shows (A.3) tends to 0 as t →0+.
Method 2: Integration by parts. (I learned this approach from Lior Silberman.) We will show
(A.2) converges by rewriting it as an absolutely convergent integral. Using u = 1/x and dv =
sin x dx, we have du = −dx/x2 and let v = 1 −cos x (not v = −cos x), so when 0 < a < b < ∞,
(A.8)
Z b
a
sin x
x
dx = 1 −cos x
x

b
a
+
Z b
a
1 −cos x
x2
dx.
In the ﬁrst term on the right, (1 −cos x)/x →0 as x →0+ and x →∞due to cos x = 1 + O(x2)
when x is small and |(1−cos x)/x| ≤2/x when x > 0. In the integral on the right, (1−cos x)/x2 is
absolutely integrable on [0, ∞) since it is bounded near 0 due to cos x = 1 + O(x2) when x is small
and since |(1 −cos x)/x2| ≤2/x2 when x ≥1. Thus we can let a →0+ and b →∞in (A.8) to see
(A.9)
Z ∞
0
sin x
x
dx =
Z ∞
0
1 −cos x
x2
dx,
with the right side being absolutely convergent.
Next, we want to show
lim
t→0+
Z ∞
0
(1 −e−tx)sin x
x
dx = 0.
We will rewrite the integral in absolutely convergent form and then show it tends to 0 in the limit.
Let u = (1 −e−tx)/x, dv = sin x dx, du = ((−1 + (1 + tx)e−tx)/x2) dx, and v = 1 −cos x (not
v = −cos x). When 0 < a < b < ∞,
(A.10)
Z b
a
(1 −e−tx)sin x
x
dx = (1 −e−tx)(1 −cos x)
x

b
a
+
Z b
a
(1 −(1 + tx)e−tx)(1 −cos x)
x2
dx.
In the ﬁrst term on the right side, 0 ≤1 −e−tx < 1 on [0, ∞) and (1 −cos x)/x →0 as x →0+ and
x →∞as we saw above. In the integral on the right side, the integrand is absolutely integrable on
[0, ∞) since it is bounded near 0 due to cos x = 1+O(x2) when x is small and since 0 < (1+y)e−y ≤1
when y ≥0. Letting a →0+ and b →∞in (A.10), we get
Z ∞
0
(1 −e−tx)sin x
x
dx =
Z ∞
0
(1 −(1 + tx)e−tx)(1 −cos x)
x2
dx.
To show the integral on the right tends to 0 as t →0+, we will break up the interval of integration
into two intervals and make separate estimates. As a power series, (1+y)e−y = 1−y2/2+y3/3−· · ·

<!-- page 29 -->
DIFFERENTIATING UNDER THE INTEGRAL SIGN
29
is alternating, so 1 −y2/2 < (1 + y)e−y ≤1 when y ≥0. Thus 0 ≤1 −(1 + y)e−y < y2/2, so when
0 < c < ∞
0 <
Z c
0
(1 −(1 + tx)e−tx)(1 −cos x)
x2
dx ≤
Z c
0
((tx)2/2)(2)
x2
dx = t2c.
Also
0 <
Z ∞
c
(1 −(1 + tx)e−tx)(1 −cos x)
x2
dx <
Z ∞
c
1 −cos x
x2
dx <
Z ∞
c
2
x2 dx = 2
c.
Thus
0 <
Z ∞
0
(1 −(1 + tx)e−tx)(1 −cos x)
x2
dx < t2c + 2
c
for all c > 0. Using c = 1/t, the upper bound is t + 2t = 3t, which tends to 0 as t →0+.
Remark A.1. By (A.2) and (A.9),
R ∞
0
1−cos(tx)
x2
dx = π
2 t by the change of variables u = tx for
t > 0. That cos x is even and cos(0) = 0 then implies
R ∞
0
1−cos(tx)
x2
dx = π
2 |t| for all t.
Appendix B. An example from the book Feynman studied
The book Advanced Calculus by Frederick Woods [16] is where Feynman learned diﬀerentiation
under the integral sign. Figure 2 below has an example from the book:
R ∞
0 e−αx(sin x)/x dx when
α > 0, which is our (3.1). Woods obtained the value π/2−arctan(α) and rewrote it as arctan(1/α),
which is valid when α > 0 (not when α < 0).
Figure 2. Page 154 in Woods’ Advanced Calculus.

<!-- page 30 -->
30
KEITH CONRAD
The sections of this book discussing diﬀerentiation under the integral sign are 60, 61 (for bounded
intervals), and 63 (for unbounded intervals), and there are exercises at the end of the chapter on
pp. 159–163.
References
[1] W. Appel, Mathematics for Physics and Physicists, Princeton Univ. Press, Princeton, 2007.
[2] W. Byerly, Elements of the Integral Calculus, 2nd ed., Ginn & Co., 1888. URL https://archive.org/details/
cu31924004779447/page/n5.
[3] S. Cao, Integrating
R ∞
0
e−x2 dx using Feynman’s parametrization trick, URL (version: 2017-09-08): http://
math.stackexchange.com/questions/390850/.
[4] Conifold, answer to Why is diﬀerentiation under the integral sign named the Leibniz rule?, URL (version: 2019-
01-06): https://hsm.stackexchange.com/questions/8132.
[5] R. P. Feynman, Surely You’re Joking, Mr. Feynman!, Bantam, New York, 1985.
[6] R. P. Feynman, Mathematical Methods, 1946 Cornell University notes by James C. Keck, http://james-keck-
memorial-collection.unibs.it/JCKeck-papers/JCKeck-class-notes-from-Feynman’s-course-on-Mathematical
Methods-at-Cornell-1946.pdf
[7] R. P. Feynman, Hughes Lectures Vol. 3, notes by John T. Neer, http://www.thehugheslectures.info/wp-content/
uploads/lectures/FeynmanHughesLectures Vol3.pdf.
[8] R. P. Feynman, Hughes Lectures Vol. 5, notes by John T. Neer, http://www.thehugheslectures.info/wp-content/
uploads/lectures/FeynmanHughesLectures Vol5.pdf.
[9] S. K. Goel and A. J. Zajta, “Parametric Integration Techniques,” Math. Mag. 62 (1989), 318–322.
[10] S. Lang, Undergraduate Analysis, 2nd ed., Springer-Verlag, New York, 1997.
[11] S. Lang, Complex Analysis, 3rd ed., Springer-Verlag, New York, 1993.
[12] M. Rozman, “Evaluate Gaussian and Fresnel’s integrals using diﬀerentiation under the integral sign,”
Course notes for Physics 2400 (UConn), Fall 2020. URL https://www.phys.uconn.edu/∼rozman/Courses/
P2400 20F/downloads/gaussian-type-integrals.pdf
[13] A. R. Schep, “A Simple Complex Analysis and an Advanced Calculus Proof of the Fundamental Theorem of
Algebra,” Amer. Math. Monthly 116 (2009), 67–68.
[14] E. Talvila, “Some Divergent Trigonometric Integrals,” Amer. Math. Monthly 108 (2001), 432–436.
[15] H. Whitney, “Diﬀerentiable even functions,” Duke Math. J. 10 (1943), 159-160.
[16] F. S. Woods, Advanced Calculus, New Edition, Ginn and Co., New York, 1934. URL https://archive.org/
details/advancedcalculuswoods.
[17] J. van Yzeren, “Moivre’s and Fresnel’s Integrals by Simple Integration,” Amer. Math. Monthly 86 (1979),
690–693.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*