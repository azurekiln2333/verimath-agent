# The Contraction Mapping Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/contraction.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE CONTRACTION MAPPING THEOREM
KEITH CONRAD
1. Introduction
Let f : X →X be a mapping from a set X to itself. We call a point x ∈X a ﬁxed point
of f if f(x) = x. For example, if [a, b] is a closed interval then any continuous function
f : [a, b] →[a, b] has at least one ﬁxed point. This is a consequence of the intermediate
value theorem, as follows. Since f(a) ≥a and f(b) ≤b, we have f(b) −b ≤0 ≤f(a) −a.
The diﬀerence f(x) −x is continuous, so by the intermediate value theorem 0 is a value of
f(x) −x for some x ∈[a, b], and that x is a ﬁxed point of f. Of course, there could be more
than one ﬁxed point.
We will discuss here the most basic ﬁxed-point theorem in analysis. It is due to Banach
and appeared in his Ph.D. thesis (1920, published in 1922).
Theorem 1.1. Let (X, d) be a complete metric space and f : X →X be a map such that
d(f(x), f(x′)) ≤cd(x, x′)
for some 0 ≤c < 1 and all x and x′ in X. Then f has a unique ﬁxed point in X. Moreover,
for any x0 ∈X the sequence of iterates x0, f(x0), f(f(x0)), . . . converges to the ﬁxed point
of f.
When d(f(x), f(x′)) ≤cd(x, x′) for some 0 ≤c < 1 and all x and x′ in X, f is called a
contraction. A contraction shrinks distances by a uniform factor c less than 1 for all pairs
of points. Theorem 1.1 is called the contraction mapping theorem or Banach’s ﬁxed-point
theorem.
Example 1.2. A standard procedure to approximate a solution in R to the numerical
equation g(x) = 0, where g is diﬀerentiable, is to use Newton’s method: ﬁnd an approximate
solution x0 and then compute the recursively deﬁned sequence
xn = xn−1 −g(xn−1)
g′(xn−1).
This recursion amounts to iteration of the function f(x) = x −g(x)/g′(x) starting from
x = x0. A solution of g(x) = 0 is the same as a solution of f(x) = x: a ﬁxed point of f.
To use Newton’s method to estimate
√
3, we take g(x) = x2 −3 and seek a (positive)
root of g(x). The Newton recursion is
xn = xn−1 −x2
n−1 −3
2xn−1
= 1
2

xn−1 +
3
xn−1

,
so f(x) = (1/2)(x + 3/x). The ﬁxed points of f are the square roots of 3. In the following
table are iterations of f with three diﬀerent positive choices of x0.
1

<!-- page 2 -->
2
KEITH CONRAD
n
xn
xn
xn
0
1.5
1.9
10
1
1.75
1.7394736842
5.15
2
1.7321428571
1.7320666454
2.8662621359
3
1.7320508100
1.7320508076
1.9564607317
4
1.7320508075
1.7320508075
1.7449209391
5
1.7320508075
1.7320508075
1.7320982711
All three sequences of iterates in the table appear to be tending to
√
3 ≈1.7320508075688.
The last choice of x0 in the table is quite a bit further away from
√
3 so the iterations take
longer to start resembling
√
3.
To justify the application of the contraction mapping theorem to this setting, we need to
ﬁnd a complete metric space on which f(x) = (1/2)(x+3/x) is a contraction. The set (0, ∞)
doesn’t work, since this is not complete. The closed interval Xt = [t, ∞) is complete for any
t > 0. For which t is f(Xt) ⊂Xt and f a contraction on Xt? Well, the minimum of f(x) on
(0, ∞) is at x =
√
3, with f(
√
3) =
√
3, so for any t ≤
√
3 we have x ≥t =⇒f(x) ≥
√
3 ≥t,
hence f(Xt) ⊂Xt. To ﬁnd such a t for which f is a contraction on Xt, for any positive x
and x′ we have
f(x) −f(x′) = x −x′
2

1 −3
xx′

.
If x ≥t and x′ ≥t then 1 −3/t2 ≤1 −3/xx′ < 1. Therefore |1 −3/xx′| < 1 as long as
1−3/t2 > −1, which is equivalent to t2 > 3/2. Taking
p
3/2 < t ≤
√
3 (e.g., t = 3/2 = 1.5),
we have f : Xt →Xt and |f(x) −f(x′)| ≤(1/2)|x −x′| for x and x′ in Xt. The contraction
mapping theorem says the iterates of f starting at any x0 ≥t will converge to
√
3. How
many iterations are needed to approximate
√
3 to a desired accuracy will be addressed in
Section 2 after we prove the contraction mapping theorem.
Although (0, ∞) is not complete, iterations of f starting from any x > 0 will converge to
√
3; if we start below
√
3 then applying f will take us above
√
3 (because f(x) ≥
√
3 for all
x > 0) and the contraction mapping theorem on [
√
3, ∞) then kicks in to guarantee that
further iterations of f will converge to
√
3.
The contraction mapping theorem has many uses in analysis, both pure and applied.
After proving the theorem (Section 2) and discussing some generalizations (Section 3), we
will give one major application: Picard’s theorem (Section 4), which is the basic existence
and uniqueness theorem for ordinary diﬀerential equations. There are further applications of
the contraction mapping theorem to partial diﬀerential equations [18], to the Gauss–Seidel
method of solving systems of linear equations in numerical analysis [17, p. 269], to a proof
of the inverse function theorem [8], [15, pp. 221-223], and to Google’s Page Rank algorithm
[9], [12], [19]. A basic introductory account of the ideas of iteration and contraction in
analysis with a few applications is in [4], and a comprehensive treatment is in [20].
2. Proof of the Contraction Mapping Theorem
Recalling the notation, f : X →X is a contraction with contraction constant c. We want
to show f has a unique ﬁxed point, which can be obtained as a limit through iteration of
f from any initial value. To show f has at most one ﬁxed point in X, let a and a′ be ﬁxed
points of f. Then
d(a, a′) = d(f(a), f(a′)) ≤cd(a, a′).

<!-- page 3 -->
THE CONTRACTION MAPPING THEOREM
3
If a ̸= a′ then d(a, a′) > 0 so we can divide by d(a, a′) to get 1 ≤c, which is false. Thus
a = a′.
Next we want to show, for any x0 ∈X, that the recursively deﬁned iterates xn = f(xn−1)
for n ≥1 converge to a ﬁxed point of f.
How close is xn to xn+1?
For any n ≥1,
d(xn, xn+1) = d(f(xn−1), f(xn)) ≤cd(xn−1, xn). Therefore
d(xn, xn+1) ≤cd(xn−1, xn) ≤c2d(xn−2, xn−1) ≤· · · ≤cnd(x0, x1).
Using the expression on the far right as an upper bound on d(xn, xn+1) shows the xn’s are
getting consecutively close at a geometric rate. This implies the xn’s are Cauchy: for any
m > n, using the triangle inequality several times shows
d(xn, xm) ≤d(xn, xn+1) + d(xn+1, xn+2) + · · · + d(xm−1, xm)
≤cnd(x0, x1) + cn+1d(x0, x1) + · · · + cm−1d(x0, x1)
= (cn + cn+1 + · · · + cm−1)d(x0, x1)
≤(cn + cn+1 + cn+2 + · · · )d(x0, x1)
=
cn
1 −cd(x0, x1).
(2.1)
To prove from this bound that the xn’s are Cauchy, choose ε > 0 and then pick N ≥1 such
that (cN/(1 −c))d(x0, x1) < ε. Then for any m > n ≥N,
d(xn, xm) ≤
cn
1 −cd(x0, x1) ≤
cN
1 −cd(x0, x1) < ε.
This proves {xn} is a Cauchy sequence. Since X is complete, the xn’s converge in X. Set
a = limn→∞xn in X.
To show f(a) = a, we need to know that contractions are continuous. In fact, a con-
traction is uniformly continuous.
This is clear when c = 0 since then f is a constant
function. If c > 0 and we are given ε > 0, setting δ = ε/c implies that if d(x, x′) < δ then
d(f(x), f(x′)) ≤cd(x, x′) < cδ = ε. That proves f is uniformly continuous. Since f is then
continuous, from xn →a we get f(xn) →f(a). Since f(xn) = xn+1, f(xn) →a as n →∞.
Then f(a) and a are both limits of {xn}n≥0. From the uniqueness of limits, a = f(a). This
concludes the proof of the contraction mapping theorem.
Remark 2.1. When f : X →X is a contraction with constant c, any iterate fn is a
contraction with constant cn; the unique ﬁxed point of f will also be the unique ﬁxed point
of any fn.
Remark 2.2. The contraction mapping theorem admits a converse [3], [16, pp. 523–526].
If X is any set (not yet a metric space), c ∈(0, 1), and f : X →X is a function such
that each iterate fn : X →X has a unique ﬁxed point then there is a metric on X making
it a complete metric space such that, for this metric, f is a contraction with contraction
constant c. For instance, the function f : R →R given by f(x) = 2x has 0 as its unique
ﬁxed point, and the same applies to its iterates fn(x) = 2nx. Therefore there is a metric
on R with respect to which it is complete and the function x 7→2x is a contraction, so in
particular 2n →0 in this metric: how strange!
There are examples where f has a unique ﬁxed point but an iterate of f does not, such
as f : R →R by f(x) = 1 −x. Here f2(x) = f(f(x)) = x for all x in R.
Corollary 2.3. Let f : X →X be a contraction on a complete metric space and Y ⊂X be
a closed subset such that f(Y ) ⊂Y . Then the unique ﬁxed point of f is in Y .

<!-- page 4 -->
4
KEITH CONRAD
Proof. Since Y is a closed subset of a complete metric space, it is complete. Then we can
apply the contraction mapping theorem to f : Y →Y , so f has a ﬁxed point in Y . Since f
has only one ﬁxed point in X, it must lie in Y .
□
The proof of the contraction mapping theorem yields useful information about the rate
of convergence towards the ﬁxed point, as follows.
Corollary 2.4. Let f be a contraction mapping on a complete metric space X, with con-
traction constant c and ﬁxed point a. For any x0 ∈X, with f-iterates {xn}, we have the
estimates
(2.2)
d(xn, a) ≤
cn
1 −cd(x0, f(x0)),
(2.3)
d(xn, a) ≤cd(xn−1, a),
and
(2.4)
d(xn, a) ≤
c
1 −cd(xn−1, xn).
Proof. From (2.1), for m > n we have
d(xn, xm) ≤
cn
1 −cd(x0, x1) =
cn
1 −cd(x0, f(x0)).
The right side is independent of m. Let m →∞to get d(xn, a) ≤(cn/(1 −c))d(x0, f(x0)).
To derive (2.3), from a being a ﬁxed point we get
(2.5)
d(xn, a) = d(f(xn−1), f(a)) ≤cd(xn−1, a).
Applying the triangle inequality to d(xn−1, a) on the right side of (2.5) using the three
points xn−1, xn, and a,
d(xn, a) ≤c(d(xn−1, xn) + d(xn, a)),
and isolating d(xn, a) yields
d(xn, a) ≤
c
1 −cd(xn−1, xn).
That’s (2.4), so we’re done.
□
The three inequalities in Corollary 2.4 serve diﬀerent purposes. The inequality (2.2) tells
us, in terms of the distance between x0 and f(x0) = x1, how many times we need to iterate
f starting from x0 to be certain that we are within a speciﬁed distance from the ﬁxed point.
This is an upper bound on how long we need to compute. It is called an a priori estimate.
Inequality (2.3) shows that once we ﬁnd a term by iteration within some desired distance
of the ﬁxed point, all further iterates will be within that distance. However, (2.3) is not so
useful as an error estimate since both sides of (2.3) involve the unknown ﬁxed point. The
inequality (2.4) tells us, after each computation, how much closer we are to the ﬁxed point in
terms of the previous two iterations. This kind of estimate, called an a posteriori estimate,
is very important because if two successive iterations are nearly equal, (2.4) guarantees that
we are very close to the ﬁxed point. For example, if c = 2/3 and d(xn−1, xn) < 1/1010 then
(2.4) tells us d(xn, a) < 2/1010 < 1/109.

<!-- page 5 -->
THE CONTRACTION MAPPING THEOREM
5
Example 2.5. To compute
√
3 to 4 digits after the decimal point, we use the recursion
from Example 1.2:
√
3 is a ﬁxed point of f(x) = (1/2)(x + 3/x). In that example we saw a
contraction constant for f on [3/2, ∞) is c = 1/2. Taking x0 = 3/2, so |x0 −f(x0)| = 1/4,
(2.2) becomes
|xn −
√
3| ≤
1
2n+1 .
The right side is less than 1/104 for n = 13, which means x13 lies within 1/104 of
√
3.
However, this iteration gives us that much accuracy a lot sooner: x3 ≈1.732050810 and
x4 ≈1.732050807, so |x3 −x4| ≤10−8. By (2.4) with c = 1/2, |x4 −
√
3| ≤|x4 −x3|, so x4
gives us
√
3 accurately to 4 (and in fact a bit more) places after the decimal point.
The iteration we are using here to approximate
√
3 comes from Newton’s method, which
has its own error bounds separate from the bounds for general contraction mappings. When
Newton’s method converges, it does so doubly-exponentially (something like c2n and not
just cn), so essentially doubling the number of correct digits after each iteration while a
typical contraction mapping produces at most one new correct digit after each iteration
once the approximations get close enough to the ﬁxed point.
Example 2.6. Graphs of y = cos x and y = x intersect once (see the ﬁgure below), which
means the cosine function has a unique ﬁxed point in R. From the graph, this ﬁxed point
lies in [0, 1]. We will show this point can be approximated through iteration.
y = cos x
y = x
1
2
3
4
−4
−3
−2
−1
The function cos x is not a contraction mapping on R: there is no c ∈(0, 1) such that
| cos x −cos y| ≤c|x −y| for all x and y. Indeed, if there were such a c then |(cos x −
cos y)/(x −y)| ≤c whenever x ̸= y, and letting y →x implies | sin x| ≤c for all x, which is
false.
However, cos x is a contraction mapping on [0, 1]. First let’s check cos x maps [0, 1] to
[0, 1]. Since cosine is decreasing on [0, 1] and cos 1 ≈.54, cos([0, 1]) ⊂[0, 1]. To ﬁnd c < 1
such that | cos x −cos y| ≤c|x −y| for all x and y in [0, 1], we can’t get by with elementary
algebra as we did for the function (1/2)(x+3/x) in Example 1.2. We will use the mean-value
theorem: for any diﬀerentiable function f, f(x) −f(y) = f′(t)(x −y) for some t between
x and y, so bounding |(cos t)′| = | sin t| over [0, 1] will give us a contraction constant. Since
sin t is increasing on [0, 1], for all t in [0, 1] we have | sin t| = sin t ≤sin 1 ≈.84147. Therefore
| cos x −cos y| ≤.8415|x −y|,
for all x and y in [0, 1]. Since [0, 1] is complete, the contraction mapping theorem tells us
that there is a unique solution of cos x = x in [0, 1] and it can be found by iterating the
function cos x starting from any initial point in [0, 1].
Here are some iterations of cos x starting from x0 = 0:

<!-- page 6 -->
6
KEITH CONRAD
n
xn
0
0
1
1
2
.5403023
...
...
19
.7393038
20
.7389377
21
.7391843
22
.7390182
The estimates (2.2) and (2.4) with x0 = 0 become
(2.6)
|xn −a| ≤
.8415n
1 −.8415,
|xn −a| ≤
.8415
1 −.8415|xn−1 −xn|.
We can use these bounds to know with certainty a value of n for which |xn −a| < .001.
The ﬁrst bound falls below .001 for the ﬁrst time when n = 51, while the second one falls
below .001 much earlier, at n = 22.
Taking n = 22, the second upper bound on |x22 −a| in (2.6) is a little less than .0009, so
a lies between
x22 −.0009 ≈.7381 and x22 + .0009 ≈.7399.
The iterative process achieves the same accuracy in fewer steps if we begin the iteration
closer to the ﬁxed point.
Let’s start at x0 = .7 instead of at x0 = 0.
Here are some
iterations:
n
xn
0
.7
1
.7648421
2
.7214916
...
...
14
.7389324
15
.7391879
16
.7390158
Now (2.2) and (2.4) with x0 = .7 say
|xn −a| ≤
.8415n
1 −.8415|.7 −cos(.7)|,
|xn −a| ≤
.8415
1 −.8415|xn−1 −xn|.
The ﬁrst upper bound on |xn −a| falls below .001 for n = 35, and the second upper bound
falls below .001 when n = 16. Using the second bound, a lies between
x16 −.00092 ≈.7381 and x16 + .00092 ≈.7399.
Example 2.7. We can use the contraction mapping theorem to compute inverses using
the computationally “less expensive” operations of addition and multiplication. The linear
polynomial f(x) = mx + b has ﬁxed point b/(1 −m), and this function is a contraction
mapping on R when |m| < 1.
(In fact xn = mnx0 + (1 + m + m2 + · · · + mn−1)b =
mnx0 + mn−1
m−1 b, which implies that the three inequalities in Corollary 2.3 are in this case
all equalities, so that corollary is sharp: the convergence of iterates under a contraction
mapping can’t be any faster in general than what Corollary 2.3 says.) For s ̸= 0, to obtain
1/s as a ﬁxed point of f(x) we seek b and m such that b/(1 −m) = 1/s and |m| < 1.
Choosing b to satisfy |1 −bs| < 1, so b is an initial approximation to 1/s (their product is

<!-- page 7 -->
THE CONTRACTION MAPPING THEOREM
7
not too far from 1), the function f(x) = (1−bs)x+b is a contraction on R with ﬁxed point
1/s. For example, if |s−1| < 1 then we can use f(x) = (1−s)x+1. For this contraction and
x0 = 0, we have xn = 1 + (1 −s) + · · · + (1 −s)n, which means the convergence of geometric
series can be viewed as a special case of the contraction mapping theorem. (Logically this
is circular, since we used geometric series in the proof of the contraction mapping theorem;
see (2.1).)
We can also make iterations converge to 1/s using Newton’s method on g(x) = 1/x −s,
which amount to viewing 1/s as the ﬁxed point of f(x) = x −g(x)/g′(x) = 2x −sx2.
From the mean-value theorem (or the triangle inequality), check that f is a contraction on
[1/s −ε, 1/s + ε] when ε < 1/(2s). So if |x0 −1/s| < 1/(2s) then iterates of f starting at x0
will converge to 1/s by the contraction mapping theorem. This method of approximating
1/s converges much faster than the iterates of a linear polynomial: check by induction that
the nth iterate of f(x) is 1/s−(sx−1)2n/s, so if |x0 −1/s| < 1/(2s) then the nth iterate of
f at x0 diﬀers from 1/s by less than (1/2)2n(1/s), which decays to 0 exponentially rather
than geometrically.
3. Generalizations
In some situations a function is not a contraction but an iterate of it is. This turns out to
suﬃce to get the conclusion of the contraction mapping theorem for the original function.
Theorem 3.1. If X is a complete metric space and f : X →X is a mapping such that
some iterate fN : X →X is a contraction, then f has a unique ﬁxed point. Moreover, the
ﬁxed point of f can be obtained by iteration of f starting from any x0 ∈X.
Proof. By the contraction mapping theorem, fN has a unique ﬁxed point. Call it a, so
fN(a) = a. To show a is the only possible ﬁxed point of f, observe that a ﬁxed point of f
is a ﬁxed point of fN, and thus must be a. To show a really is a ﬁxed point of f, we note
that f(a) = f(fN(a)) = fN(f(a)), so f(a) is a ﬁxed point of fN. Therefore f(a) and a are
both ﬁxed points of fN. Since fN has a unique ﬁxed point, f(a) = a.
We now show that for any x0 ∈X the points fn(x0) converge to a as n →∞. Consider the
iterates fn(x0) as n runs through a congruence class modulo N. That is, pick 0 ≤r ≤N −1
and look at the points fNk+r(x0) as k →∞. Since
fNk+r(x0) = fNk(fr(x0)) = (fN)k(fr(x0)),
these points can be viewed (for each r) as iterates of fN starting at the point y0 = fr(x0).
Since fN is a contraction, these iterates of fN (from any initial point, such as y0) must
tend to a by the contraction mapping theorem. This limit is independent of the value of r
in the range {1, . . . , N −1}, so all N sequences {fNk+r(x0)}k≥1 tend to a as k →∞. This
shows
(3.1)
fn(x0) →a
as n →∞.
□
We will use Theorem 3.1 in Section 4 to solve diﬀerential equations.
Example 3.2. The graphs of y = e−x and y = x intersect once, so e−a = a for a unique
real number a. See the graph below.

<!-- page 8 -->
8
KEITH CONRAD
y = e−x
y = x
a 1
2
3
4
−4
−3
−2
−1
The function f(x) = e−x is not a contraction on R (for instance, |f(−2)−f(0)| ≈6.38 >
| −2 −0|), but its second iterate g(x) = f2(x) = e−e−x is a contraction on R: by the
mean-value theorem
g(x) −g(y) = g′(t)(x −y)
for some t between x and y, where |g′(t)| = |e−e−te−t| = e−(t+e−t) ≤e−1 (since t + e−t ≥1
for all real t). Hence f2 has contraction constant 1/e ≈.367 < 1. By Theorem 3.1 the
solution to e−a = a can be approximated by iteration of f starting with any real number.
Iterating f enough times with x0 = 0 suggests a ≈.567. To prove this approximation is
correct, one can generalize the error estimates in Corollary 2.4 to apply to a function having
an iterate as a contraction. Alternatively, check f([ε, 1]) ⊂[ε, 1] when 0 ≤ε ≤1/e, and
when 0 < ε ≤1/e the function f is a contraction on [ε, 1]. Therefore Corollary 2.4 can be
applied directly to f by starting iterates at any x0 ∈(0, 1].
Remark 3.3. When fN is a contraction, fN is continuous, but that does not imply f is
continuous. For example, let f : [0, 1] →[0, 1] by f(x) = 0 for 0 ≤x ≤1/2 and f(x) = 1/2
for 1/2 < x ≤1. Then f(f(x)) = 0 for all x, so f2 is a contraction but f is discontinuous.
It was important in the proof of the contraction mapping theorem that the contraction
constant c be strictly less than 1. That gave us control over the rate of convergence of
fn(x0) to the ﬁxed point since cn →0 as n →∞. If instead of f being a contraction we
suppose d(f(x), f(x′)) < d(x, x′) whenever x ̸= x′ in X then we lose that control and indeed
a ﬁxed point need not exist.
Example 3.4. Let I be a closed interval in R and f : I →I be diﬀerentiable with |f′(t)| < 1
for all t. Then the mean-value theorem implies |f(x)−f(x′)| < |x−x′| for x ̸= x′ in I. The
following three functions all ﬁt this condition, where I = [1, ∞) in the ﬁrst case and I = R
in the second and third cases:
f(x) = x + 1
x,
f(x) =
p
x2 + 1,
f(x) = log(1 + ex).
In each case, f(x) > x, so none of these functions has a ﬁxed point in I. (One could consider
∞to be a ﬁxed point, and fn(x) →∞as n →∞. See [5] for a general theorem in this
direction.)
Despite such examples, there is a ﬁxed-point theorem when d(f(x), f(x′)) < d(x, x′) for
all x ̸= x′ provided the space is compact, which is not the case in the previous example.
This theorem, which is next, is due to Edelstein [7].

<!-- page 9 -->
THE CONTRACTION MAPPING THEOREM
9
Theorem 3.5. Let X be a compact metric space. If f : X →X satisﬁes d(f(x), f(x′)) <
d(x, x′) when x ̸= x′ in X, then f has a unique ﬁxed point in X and the ﬁxed point can be
found as the limit of fn(x0) as n →∞for any x0 ∈X.
Proof. To show f has at most one ﬁxed point in X, suppose f has two ﬁxed points a ̸= a′.
Then d(a, a′) = d(f(a), f(a′)) < d(a, a′). This is impossible, so a = a′.
To prove f actually has a ﬁxed point, we will look at the function X →[0, ∞) given by
x 7→d(x, f(x)). This measures the distance between each point and its f-value. A ﬁxed
point of f is where this function takes the value 0.
Since X is compact, the function d(x, f(x)) takes on its minimum value: there is an
a ∈X such that d(a, f(a)) ≤d(x, f(x)) for all x ∈X. We’ll show by contradiction that a is
a ﬁxed point for f. If f(a) ̸= a then the hypothesis about f in the theorem (taking x = a
and x′ = f(a)) says
d(f(a), f(f(a))) < d(a, f(a)),
which contradicts the minimality of d(a, f(a)) among all numbers d(x, f(x)). So f(a) = a.
Finally, we show for any x0 ∈X that the sequence xn = fn(x0) converges to a as n →∞.
This can’t be done as in the proof of the contraction mapping theorem since we don’t have
the contraction constant to help us out. Instead we will exploit compactness.
If for some k ≥0 we have xk = a then xk+1 = f(xk) = f(a) = a, and more generally
xn = a for all n ≥k, so xn →a since the terms of the sequence equal a for all large n. Now
we may assume instead that xn ̸= a for all n. Then
0 < d(xn+1, a) = d(f(xn), f(a)) < d(xn, a),
so the sequence of numbers d(xn, a) is decreasing and positive. Thus it has a limit ℓ=
limn→∞d(xn, a) ≥0. We will show ℓ= 0 (so d(xn, a) →0, which means xn →a in X). By
compactness of X, the sequence {xn} has a convergent subsequence xni, say xni →y ∈X.
The function f is continuous, so f(xni) →f(y), which says xni+1 →f(y) as i →∞. Since
d(xn, a) →ℓas n →∞, d(xni, a) →ℓand d(xni+1, a) →ℓas i →∞. By continuity of
the metric, d(xni, a) →d(y, a) and d(xni+1, a) = d(f(xni), a) →d(f(y), a). Having already
shown these limits are ℓ,
(3.2)
d(y, a) = ℓ= d(f(y), a) = d(f(y), f(a)).
If y ̸= a then d(f(y), f(a)) < d(y, a), but this contradicts (3.2). So y = a, which means
ℓ= d(y, a) = 0. That shows d(xn, a) →0 as n →∞.
□
The proof of Edelstein’s theorem does not yield any error estimate on the rate of conver-
gence to the ﬁxed point, since we proved convergence to the ﬁxed point without having to
make estimates along the way. Edelstein did not assume for his main theorem in [7] that
X is compact, as in Theorem 3.5. He assumed instead that there is some x0 ∈X whose
sequence of iterates fn(x0) has a convergent subsequence and he proved this limit is the
unique ﬁxed point of f and that the whole sequence fn(x0) tends to that ﬁxed point.
It is natural to wonder if the compactness of X might force f in Theorem 3.5 to be a
contraction after all, so the usual contraction mapping theorem would apply. For instance,
the ratios d(f(x), f(x′))/d(x, x′) for x ̸= x′ are always less than 1, so they should be less
than or equal to some deﬁnite constant c < 1 from compactness (a continuous real-valued
function on a compact set achieves its supremum as a value). But this reasoning is bogus,
because d(f(x), f(x′))/d(x, x′) is deﬁned not on the compact set X × X but rather on
X × X −{(x, x) : x ∈X} where the diagonal is removed, and this is not compact (take a

<!-- page 10 -->
10
KEITH CONRAD
look at the special case X = [0, 1], for instance). There is no way to show f in Theorem 3.5
has to be a contraction since there are examples where it isn’t.
Example 3.6. Let f : [0, 1] →[0, 1] by f(x) =
1
1+x, so |f(x)−f(y)| = |x−y|/|(1+x)(1+y)|.
When x ̸= y we have |f(x) −f(y)|/|x −y| = 1/(1 + x)(1 + y) < 1, so |f(x) −f(y)| < |x −y|
and |f(x) −f(y)|/|x −y| gets arbitrarily close to 1 when x and y are suﬃciently close to 0.
Therefore f is not a contraction on [0, 1] with respect to the usual metric.
Theorem 3.5 says f has a unique ﬁxed point in [0, 1] and fn(x0) tends to this point as
n →∞for any choice of x0. Of course, it is easy to ﬁnd the ﬁxed point: x = 1/(1 + x) in
[0, 1] at x = (−1 +
√
5)/2 ≈.61803.
This example does not actually require Theorem 3.5. One way around it is to check that if
1/2 ≤x ≤1 then 1/2 ≤f(x) ≤2/3, so f : [1/2, 1] →[1/2, 1] with maxx∈[1/2,1] |f′(x)| = 4/9.
We could apply the contraction mapping theorem to f on [1/2, 1] to ﬁnd the ﬁxed point.
A second method is to check that f2(x) = (1 + x)/(2 + x) is a contraction on [0, 1] (the
derivative of (1 +x)/(2 + x) on [0, 1] has absolute value at most 1/4), so we could apply the
contraction mapping theorem to f2.
Example 3.7. Following [2], let f : [0, 1] →[0, 1] by f(x) = x/(1 + x).
Since |f(x) −
f(y)|/|x −y| = 1/(1 + x)(1 + y) for x ̸= y, the ratio |f(x) −f(y)|/|x −y| for x ̸= y can be
made arbitrarily close to 1 by taking x and y suﬃciently close to 0. What makes this example
diﬀerent from the previous one is that, since 0 is now the ﬁxed point, f does not restrict to
a contraction on any neighborhood of its ﬁxed point. Moreover, since fn(x) = x/(1 + nx),
for x ̸= y the ratio |fn(x)−fn(y)|/|x−y| = 1/(1+nx)(1+ny) is arbitrarily close to 1 when
x and y are suﬃciently close to 0, so no iterate fn is a contraction on any neighborhood of
the ﬁxed point in [0, 1].
A similar example on [0, 1] with 1 as the ﬁxed point uses g(x) = 1−f(1−x) = 1/(2−x).
4. Differential Equations
As a signiﬁcant application of the contraction mapping theorem, we will solve the initial
value problem
(4.1)
dy
dt = f(t, y),
y(t0) = y0
for “nice” functions f. A solution to (4.1) is a diﬀerentiable function y(t) deﬁned on a
neighborhood of t0 such that
dy
dt = f(t, y(t)),
y(t0) = y0.
Before stating the basic existence and uniqueness theorem for such initial value problems,
we look at some examples to appreciate the scope of the theorem we will prove.
Example 4.1. The initial value problem
dy
dt = y2,
y(0) = 1
has a unique solution passing through the point (0,1) that is found using separation of
variables and integration:
y(t) =
1
1 −t.

<!-- page 11 -->
THE CONTRACTION MAPPING THEOREM
11
Note that although the right side of the diﬀerential equation makes sense everywhere, the
solution blows up in ﬁnite time (at t = 1). See the blue curve in the ﬁgure below. Other
curves in the ﬁgure are other solutions to dy/dt = y2 with y(0) > 0 (having the form
y = 1/(c −t)).
1
2
3
Example 4.2. The initial value problem
dy
dt = y2 −t,
y(0) = 1
has a solution, but the solution can’t be expressed in terms of elementary functions or their
integrals (theorem of Liouville [14, p. 70 ﬀ.]). Like the previous example, the solution blows
up in ﬁnite time even though the right side makes sense everywhere. Take a look at the
slope ﬁeld digram below to be convinced visually of the ﬁnite blow-up time for the solution
curve passing through (0, 1); for a proof of this see Appendix A.

<!-- page 12 -->
12
KEITH CONRAD
Example 4.3. The initial value problem
dy
dt = y2/3,
y(0) = 0,
has two solutions: y(t) = 0 and y(t) = t3/27.
These examples show that to solve (4.1) in any kind of generality, we will have to be
satisﬁed with a solution that exists only locally (i.e., not everywhere that f makes sense),
and some constraint is needed on f to have a unique solution near t0.
The condition we will introduce on f(t, y) to guarantee a local unique solution is a
Lipschitz condition in the second variable.
That is, we will assume there is a constant
K > 0 such that |f(t, y1) −f(t, y2)| ≤K|y1 −y2| for all y1 and y2. The right side doesn’t
involve t, so this is a Lipschitz condition in the second variable that is uniform in the ﬁrst
variable.
Most functions are not globally Lipschitz.
For instance, the single-variable function
h(x) = x2 doesn’t satisfy |h(a) −h(b)| ≤K|a −b| for some K > 0 and all a and b. But any
function with continuous ﬁrst derivative is locally Lipschitz:
Lemma 4.4. Let U ⊂R2 be open and f : U →R be a C1-function. Then it is locally
Lipschitz in its second variable unifomly in the ﬁrst: for any (t0, y0) ∈U, there is a constant
K > 0 such that
|f(t, y1) −f(t, y2)| ≤K|y1 −y2|
for all t near t0 and all y1 and y2 near y0.
Proof. The open set U contains a rectangle around (t0, y0), say I × J. Here I and J are
closed intervals (of positive length) with t0 ∈I, y0 ∈J, and I × J ⊂U. Applying the
mean-value theorem to f in its second variable, for any t ∈I and y1 and y2 in J
f(t, y1) −f(t, y2) = ∂f
∂y (t, y3)(y1 −y2)
for some y3 between y1 and y2, depending possibly on t. Then
|f(t, y1) −f(t, y2)| =

∂f
∂y (t, y3)
 |y1 −y2| ≤sup
p∈I×J

∂f
∂y (p)
 |y1 −y2|.
Let K = supp∈I×J |(∂f/∂y)(p)|, which is ﬁnite since a continuous function on a compact
set is bounded.
□
Example 4.5. The function f(t, y) = sin(ty) is C1 on all of R2 and is Lipschitz on any
vertical strip [−R, R] × R: if |t| ≤R then for any y1 and y2 in R,
sin(ty1) −sin(ty2) = t cos(ty3)(ty1 −ty2)
for some y3 between y1 and y2. Therefore
| sin(ty1) −sin(ty2)| ≤t2|y1 −y2| ≤R2|y1 −y2|.
Example 4.6. The function f(t, y) = y2/3 is not C1 at (0, 0) and in fact is not even
Lipschitz in any neighborhood of (0, 0): if |y2/3
1
−y2/3
2
| ≤K|y1 −y2| for some K > 0 and
all y1, y2 near 0 then taking y2 = 0 shows |y2/3| ≤K|y| for all y near 0, but for y ̸= 0 that’s
the same as |y|−1/3 ≤K, and |y|−1/3 is unbounded as y →0.
Our next lemma controls the growth of a hypothetical solution to (4.1) near t0.

<!-- page 13 -->
THE CONTRACTION MAPPING THEOREM
13
Lemma 4.7. Let U ⊂R2 be open and f : U →R be continuous. For any (t0, y0) ∈U there
are r, R > 0 such that the rectangle [t0 −r, t0 + r] × [y0 −R, y0 + R] is in U and, for any
δ ∈(0, r], a solution y(t) to (4.1) that is deﬁned on [t0−δ, t0+δ] must satisfy |y(t)−y0| ≤R
for |t −t0| ≤δ.
U
t0 −r
t0
t0 + r
y0 + R
y0
y0 −R
Proof. Suppose y(t) satisﬁes (4.1) near t0. For t near t0, (t, y(t)) ∈U because U is open and
y(t) is continuous, so f(t, y(t)) makes sense. For t near t0,
R t
t0 f(s, y(s)) ds has t-derivative
f(t, y(t)), which is also the t-derivative of y(t), so by (4.1) y(t) and
R t
t0 f(s, y(s)) ds diﬀer
by a constant near t0. At t = t0 the diﬀerence is y(t0) −0 = y0, so
(4.2)
y(t) = y0 +
Z t
t0
f(s, y(s)) ds
for t near t0. Pick a rectangle
[t0 −r, t0 + r] × [y0 −R, y0 + R]
in U that is centered at (t0, y0) and let B > 0 be an upper bound of |f| on the rectangle.
For t near t0, (4.2) implies
(4.3)
|y(t) −y0| ≤B|t −t0|.
Notice B, r, and R are determined wholly by f and not by any solutions to (4.1).
Shrink r so that Br ≤R, i.e., replace r with min(r, R/B).
(We could alternatively
try to increase R to achieve this inequality, but increasing the size of the rectangle would
usually change B and there is also the constraint that the rectangle should be inside of U.)
Pick δ ∈(0, r] and suppose there is a solution y(t) to (4.1) for |t −t0| ≤δ. In particular,
(t, y(t)) ∈U for |t −t0| ≤δ. From (4.3), |y(t) −y0| ≤Br ≤R, so (t, y(t)) is in the rectangle
for |t −t0| ≤r.
□
Here is the key existence and uniqueness theorem for ODEs.
Theorem 4.8 (Picard). Let R = [a, b]×[y0 −R, y0 +R] ⊂R2 be a rectangle and f : R →R
be a continuous function on the rectangle that is Lipschitz in its second variable uniformly
in its ﬁrst variable. Let B > 0 be an upper bound on |f| over this rectangle. For t0 ∈[a, b],
let r = min(|t0 −a|, |t0 −b|). The initial value problem (4.1) has a unique solution on the
interval [t0 −r0, t0 + r0], where r0 = min(r, R/B).
In particular, if U ⊂R2 is open and f : U →R is C1 then (4.1) has a unique local
solution passing through any point in its domain.

<!-- page 14 -->
14
KEITH CONRAD
a
t0
b
y0 + R
y0
y0 −R
Proof. Set
M = {h ∈C[a, b] : |h(t) −y0| ≤R for t ∈[a, b]}.
The constant function h(t) = y0 is in M, so M ̸= ∅. For any h ∈M, the graph {(t, h(t)) :
t ∈[a, b]} lies in R. Giving C[a, b] the sup-norm || · · · ||sup, M is a closed subspace of C[a, b].
Since C[a, b] is complete in the sup-norm, M is also complete in the sup-norm.
Considering the formula (4.2), let F : M →M by
(4.4)
(Fh)(t) := y0 +
Z t
t0
f(s, h(s)) ds.
The integration makes sense, since (s, h(s)) ∈R for all s ∈[a, b], and moreover
|(Fh)(t) −y0| ≤B|t −t0| ≤Br ≤R,
so F(M) ⊂M. We will show the contraction mapping theorem can be applied to ﬁnd a
ﬁxed point of F in M. A ﬁxed point of F is a solution to (4.1) by the fundamental theorem
of calculus.
The solutions of (4.1) and (4.2) are the same. The advantage of (4.2) over (4.1) is that
continuous functions have continuous antiderivatives but they might not have a derivative;
integration is a “smoother” operation on functions than diﬀerentiation.
To illustrate diﬀerent techniques, we will show how the contraction mapping theorem can
be applied to ﬁnd a ﬁxed point of F in two ways:
(1) an iterate F n is a contraction on M for n ≫0, so Theorem 3.1 applies,
(2) F is a contraction on M using a norm other than the sup-norm, but in which M is
still complete.
Proof of (1): For h1, h2 ∈M and t ∈[a, b],
(Fh1)(t) −(Fh2)(t) =
Z t
t0
(f(s, h1(s)) −f(s, h2(s))) ds,
so
(4.5)
|(Fh1)(t) −(Fh2)(t)| ≤
Z
|[t0,t]|
|f(s, h1(s)) −f(s, h2(s))| ds,
where
R
|[t0,t]| denotes
R
[t0,t] if t0 ≤t and
R
[t,t0] if t < t0. We are assuming f is Lipschitz in
its second variable uniformly in the ﬁrst, say |f(t, y1) −f(t, y2)| ≤K|y1 −y2| for (t, y1) and

<!-- page 15 -->
THE CONTRACTION MAPPING THEOREM
15
(t, y2) in R. Then
|(Fh1)(t) −(Fh2)(t)| ≤
Z
|[t0,t]|
K|h1(s) −h2(s)| ds
(4.6)
≤K||h1 −h2||sup |t −t0|
(4.7)
≤K||h1 −h2||sup (b −a).
Thus ||Fh1 −Fh2||sup ≤K(b −a)||h1 −h2||sup . If K(b −a) < 1 then F is a contraction
on M. (This already gives us local existence and uniqueness of a solution by shrinking [a, b]
small enough around t0 so that b −a < 1/K. But we want to show there is a solution on
our original [a, b], so we proceed in a diﬀerent way.) To cover the case K(b −a) ≥1, we
look at how iterates of F shrink distances. Since
(F 2h1)(t) −(F 2h2)(t) =
Z t
t0
(f(s, (Fh1)(s)) −f(s, (Fh2)(s))) ds,
we get
|(F 2h1)(t) −(F 2h2)(t)| ≤
Z
|[t0,t]|
K|(Fh1)(s) −(Fh2)(s)| ds
by the Lipschitz condition
≤
Z
|[t0,t]|
K · K||h1 −h2||sup |s −t0| ds
by (4.7)
= K2||h1 −h2||sup
Z
|[t0,t]|
|s −t0| ds.
Since
R
|[t0,t]| |s −t0| ds = |t −t0|2/2 (check this separately for t ≥t0 and t < t0), we have
|(F 2h1)(t) −(F 2h2)(t)| ≤K2||h1 −h2||sup
|t −t0|2
2
= (K|t −t0|)2
2
||h1 −h2||sup .
By induction, using the formula
R
|[t0,t]| |s −t0|n ds = |t −t0|n+1/(n + 1) for n ≥0,
|(F nh1)(t) −(F nh2)(t)| ≤(K|t −t0|)n
n!
||h1 −h2||sup
for all n ≥0 and t ∈[a, b]. Since |t −t0| ≤b −a,
||F nh1 −F nh2||sup ≤(K(b −a))n
n!
||h1 −h2||sup .
When n ≫0, (K(b −a))n/n! < 1, so F n is a contraction on M in the sup-norm. Thus F
has a unique ﬁxed point in M by Theorem 3.1.
Proof of (2): Deﬁne a new norm || · || on C[a, b] by
||h|| := sup
t∈[a,b]
e−K|t−t0||h(t)|,
where K is the Lipschitz constant for f on R. To check this is a norm on C[a, b], for any
t ∈[a, b] we have
|h1(t) + h2(t)| ≤|h1(t)| + |h2(t)|,
so
e−K|t−t0||h1(t) + h2(t)| ≤e−K|t−t0||h1(t)| + e−K|t−t0||h2(t)| ≤||h1|| + ||h2||.

<!-- page 16 -->
16
KEITH CONRAD
Taking the sup of the left side over all t ∈[a, b] shows || · || satisﬁes the triangle inequality.
The other conditions to be a vector space norm are easily checked. How does || · || compare
to the sup-norm on C[a, b]? For t ∈[a, b],
e−K(b−a) ≤e−K|t−t0| ≤1,
so for any h ∈C[a, b]
e−K(b−a)|h(t)| ≤e−K|t−t0||h(t)| ≤|h(t)|.
Taking the sup over t ∈[a, b],
(4.8)
e−K(b−a)||h||sup ≤||h|| ≤||h||sup .
Thus || · || and the sup-norm bound each other from above and below up to scaling factors,
so these two norms have the same open sets and the same convergent sequences in C[a, b].
In particular, C[a, b] and its subset M are both complete relative to || · || since they are
complete with respect to the sup-norm.
Returning to (4.6), multiply both sides by e−K|t−t0|:
e−K|t−t0||(Fh1)(t) −(Fh2)(t)| ≤e−K|t−t0|
Z
|[t0,t]|
K|h1(s) −h2(s)| ds
= e−K|t−t0|
Z
|[t0,t]|
KeK|s−t0|e−K|s−t0||h1(s) −h2(s)| ds
≤e−K|t−t0|
Z
|[t0,t]|
KeK|s−t0|||h1 −h2|| ds
= ||h1 −h2||e−K|t−t0|
Z
|[t0,t]|
KeK|s−t0| ds.
To compute the integral in this last expression, we take cases depending on whether t0 ≤t
or t0 > t. If t0 ≤t then |t −t0| = t −t0 and |s −t0| = s −t0 for t0 ≤s ≤t, so
Z
|[t0,t]|
KeK|s−t0| ds =
Z t
t0
KeK(s−t0) ds = eK(t−t0) −1.
If t0 > t then |t −t0| = t0 −t and |s −t0| = t0 −s for t ≤s ≤t0, so
Z
|[t0,t]|
KeK|s−t0| ds =
Z t0
t
KeK(t0−s) ds = eK(t0−t) −1.
In either case the value is eK|t−t0| −1, so
e−K|t0−t|
Z
|[t0,t]|
KeK|s−t0| ds = e−K|t−t0|(eK|t−t0| −1) = 1 −e−K|t0−t|.
Therefore
e−K|t−t0||(Fh1)(t) −(Fh2)(t)| ≤||h1 −h2||(1 −e−K|t−t0|) ≤(1 −e−K(b−a))||h1 −h2||.
Taking the supremum of the left side over all t ∈[a, b],
||Fh1 −Fh2|| ≤(1 −e−K(b−a))||h1 −h2||.
Since K(b −a) > 0, 1 −e−K(b−a) < 1, so F : M →M is a contraction with respect to || · ||.
Since M is complete with respect to || · ||, there is a unique ﬁxed point of F in M by the
contraction mapping theorem.
□

<!-- page 17 -->
THE CONTRACTION MAPPING THEOREM
17
The proof of Picard’s theorem says that a solution to (4.1) near t0 can be found as a
limit of the sequence {yn(t)} where y0(t) = y0 is a constant function and
yn+1(t) = y0 +
Z t
t0
f(s, yn(s)) ds.
These functions yn(t), deﬁned recursively by integration, are called Picard iterates. Picard’s
proof of Theorem 4.8 appeared in 1890 [13] (30 years before Banach stated the general
contraction mapping theorem), and the basic idea was already used in a special case by
Liouville in 1837.
Remark 4.9. In the proof of Picard’s theorem we introduced an integral operator F in
(4.4) and gave two ways of showing it has a ﬁxed point. The same ideas can be used to prove
in two ways that for any continuous function f ∈C[a, b] the (Volterra) integral equation
y(t) = f(t) +
Z t
a
k(t, s)y(s) ds
has a unique solution y ∈C[a, b] for any given continuous f and k. See [11, pp. 75–76].
Corollary 4.10. If f : [a, b] × R →R is Lipschitz in its second variable uniformly in its
ﬁrst variable, then the diﬀerential equation (4.1) has a unique solution on [a, b] given any
initial condition at a point t0 ∈[a, b].
Proof. In the beginning of the proof of Picard’s theorem, the business with R and shrinking
the domain on which the diﬀerential equation is studied near t0 was carried out to put
ourselves in the position of having a domain where f is Lipschitz in its second variable uni-
formly in the ﬁrst variable and such that we deﬁne M to contain only continuous functions
whose graph remains in this domain for f. Therefore if we assume from the outset that f
has the relevant Lipschitz condition and its second variable runs over R, we can drop the
preliminary part of the proof of Theorem 4.8 from consideration and just take M = C[a, b].
Deﬁne F : M →M as in (4.4).
□
Example 4.11. The function f(t, y) = sin(ty) is Lipschitz in y uniformly in t on any set
of the form [−r, r] × R, so the diﬀerential equation dy/dt = sin(ty) with y(0) = 1 has a
unique solution on [−r, r] for all r. Thus the solution y is deﬁned on all of R.
Remark 4.12. If we drop the local Lipschitz condition on f then we lose the uniqueness of
the solution to (4.1), as we saw in Example 4.3, but we don’t lose existence. It is a theorem
of Peano that as long as f(t, y) is continuous, (4.1) will have a solution curve passing through
any point (t0, y0). In one method of proof [6, pp. 150–154], the basic idea is to express f
as the uniform limit of polynomial functions Pn(t, y) using the Stone-Weierstrass theorem.
Polynomials are C1, so by Picard’s theorem (essentially the contraction mapping theorem),
the initial value problems y′(t) = Pn(t, y), y(t0) = y0, are each uniquely locally solvable near
t0. Denote the solutions as yn. It can be shown, using a compactness theorem in spaces
of continuous functions, that some subsequence of the yn’s converges to a solution to the
original initial value problem y′ = f(t, y). For a second proof of Peano’s theorem, using a
diﬀerent ﬁxed-point theorem, see [20, Prop. 2.14].
Picard’s theorem is applicable to more general ﬁrst-order diﬀerential equations than (4.1),
such as
(4.9)
t2 + y2 +
dy
dt
2
= 1,
y(0) = 1
2.

<!-- page 18 -->
18
KEITH CONRAD
Setting t = 0 yields 1/4 + y′(0)2 = 1, so y′(0) = ±
√
3/2. We have to make a choice of
y′(0) before we can pin down a particular solution, since the diﬀerential equation does not
determine y′(0). Taking y′(0) =
√
3/2, we want to solve
dy
dt =
p
1 −t2 −y2,
y(0) = 1
2,
while taking y′(0) = −
√
3/2 leads to the equation
dy
dt = −
p
1 −t2 −y2,
y(0) = 1
2.
Each of these has a unique solution near t = 0 using Picard’s theorem.
More generally, a ﬁrst-order ordinary diﬀerential equation looks like g(t, y, y′) = 0 with
some initial conditions y(t0) = y0 and y′(t0) = z0 (so g(t0, y0, z0) = 0). Assuming g(t, y, z) is
a C1-function of 3 variables, as long as (∂g/∂z)(t0, y0, z0) ̸= 0 the implicit function theorem
tells us there is an open set U ⊃(t0, y0) in R2 and a C1-function f : U →R such that
z0 = f(t0, y0) and for all (t, y) near (t0, y0), g(t, y, z) = 0 if and only if z = f(t, y). Therefore
the diﬀerential equation g(t, y, y′) = 0 locally near (t0, y0, z0) looks like y′ = f(t, y), which is
exactly the kind of diﬀerential equation we solved locally and uniquely by Picard’s theorem.
So Picard’s theorem implies local existence and uniqueness of fairly general ﬁrst-order ODEs.
Picard’s theorem generalizes [1, Chap. 4] to a ﬁrst-order ordinary diﬀerential equation
with a vector-valued function:
dy
dt = f(t, y(t))
where f and y have values in Rn and f is C1. Essentially the only change needed to extend
the proof of Picard’s theorem from the 1-dimensional case to higher dimensions is the use of
an integral (rather than diﬀerential) form of the mean-value theorem to show a C1-function
is locally Lipschitz.
Appendix A. A Differential Inequality
In Example 4.2 it was stated that the initial value problem y′(t) = y(t)2 −t, y(0) = 1 has
a solution that blows up in ﬁnite time. To estimate the blow-up time, let Y (t) = 1/y(t) and
see where Y (t) = 0. From Y ′(t) = tY (t)2 −1 and Y (0) = 1, a computer algebra package
has Y (t) = 0 at t ≈1.125.
Theorem A.1. The solution to y′(t) = y(t)2−t satisfying y(0) = 1 is undeﬁned somewhere
before t = 1.221.
This is weaker than what numerics suggest (i.e., the blow-up time is around 1.125),
but proving something sharper requires a more careful analysis than we wish to develop.
An expert in non-linear ODEs told me that in practice nobody tries to prove very sharp
approximations for blow-up times (mere existence of a blow-up time usually suﬃces).
Proof. We know y(t) is deﬁned for small t > 0. Assume y(t) is deﬁned for 0 ≤t < c. We
will show for a suitable c that y(t) ≥c/(c −t) for 0 ≤t < c, so y(t) →∞as t →c+.
Therefore y(t) has to be undeﬁned for some t ≤c.

<!-- page 19 -->
THE CONTRACTION MAPPING THEOREM
19
Set z(t) = c/(c −t), with c still to be determined, so
d
dt(y −z) = y2 −t −dz
dt
= y2 −t −
c
(c −t)2
= y2 −z2 +

1 −1
c

z2 −t
= (y −z)(y + z) + (c −1)c
(c −t)2 −t
By calculus, (c−1)c/(c−t)2−t ≥0 for 0 ≤t < c as long as c−1 ≥(4/27)c2, which happens
for c between the two roots of x −1 = (4/27)x2. The roots are approximately 1.2207 and
5.5292. So taking c = 1.221, we have (y(t) −z(t))′ ≥(y(t) −z(t))(y(t) + z(t)) for 0 ≤t < c.
Using an integrating factor, this diﬀerential inequality is the same as
d
dt

e−
R t
0 (y(s)+z(s)) ds(y(t) −z(t))

≥0.
Since e−
R t
0 (y(s)+z(s)) ds(y(t) −z(t))|t=0 = 0, e−
R t
0 (y(s)+z(s)) ds(y(t) −z(t)) ≥0 for t ≥0, so
y(t) −z(t) ≥0 because the exponential factor is positive. Thus y(t) ≥z(t) = c/(c −t).
□
References
[1] V. I. Arnol’d, “Ordinary Diﬀerential Equations,” Springer-Verlag, New York, 1992.
[2] D. G. Bennett and B. Fisher, On a Fixed Point Theorem for Compact Metric Spaces, Math. Magazine
47 (1974), 40–41.
[3] C. Bessaga, On the Converse of the Banach Fixed-point Principle, Colloq. Math. 7 (1959), 41–43.
[4] V. Bryant, “Metric Spaces: Iteration and Application,” Cambridge Univ. Press, Cambridge, 1985.
[5] A. F. Beardon, Contractions on the real line, Amer. Math. Monthly 113 (2006), 557–558
[6] R. C. Buck (ed.), “Studies in Modern Analysis, Vol. 1,” Prentice-Hall, Englewood Cliﬀs, NJ, 1962.
[7] M. Edelstein, On Fixed and Periodic Points Under Contractive Mappings, J. London Math. Soc. 37
(1962), 74–79.
[8] M. Freeman, The Inverse as a Fixed Point in Function Space, Amer. Math. Monthly 83 (1976), 344–348.
[9] D. J. Higham and A. Taylor, The Sleekest Link Algorithm, http://citeseerx.ist.psu.edu/viewdoc/
download?doi=10.1.1.159.831&rep=rep1&type=pdf.
[10] J. E. Hutchinson, Fractals and Self-Similarity, Indiana Univ. Math. J. 30 (1981), 713–747.
[11] A. N. Kolmogorov and S. Fomin, “Introductory Real Analysis,” Dover, New York, 1970.
[12] A. Langville and C. Meyer, “Google’s PageRank and Beyond: The Science of Search Engine Rankings,”
Princeton Univ. Press, Princeton, 2006.
[13] E. Picard, M´emoire sur la th´eorie des ´equations aux d´eriv´ees partielles et la m´ethode des approximations
successives, J. Math. Pures et Appl. 6 (1890), 145–210.
[14] J. F. Ritt, “Integration in Finite Terms,” Columbia Univ. Press, New York, 1948.
[15] W. Rudin, “Principles of Mathematical Analysis,” 3rd ed., McGraw–Hill, New York, 1976.
[16] E. Schechter, “Handbook of Analysis and its Applications,” Academic Press, San Diego, 1997.
[17] C. Wagner, A Generic Approach to Iterative Methods, Math. Mag. 55 (1982), 259–273.
[18] W. Walter, An Elementary Proof of the Cauchy–Kowalevsky Theorem, Amer. Math. Monthly 92 (1985),
115–126.
[19] B. White, How Google Ranks Web Pages, http://citeseerx.ist.psu.edu/viewdoc/citations;
jsessionid=6CDD52D0B67B14A2248967A5164A5981?doi=10.1.1.498.5678.
[20] E. Zeidler, “Nonlinear Functional Analysis and its Applications I: Fixed-Point Theorems,” Springer-
Verlag New York, 1986.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*