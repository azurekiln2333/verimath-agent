# Metric Spaces

> **Source**: https://kconrad.math.uconn.edu/blurbs/metricspaces.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
METRIC SPACES
KEITH CONRAD
1. Introduction
As calculus developed, eventually turning into analysis, concepts ﬁrst explored on the
real line (e.g., a limit of a sequence of real numbers) eventually extended to other spaces
(e.g., a limit of a sequence of vectors or of functions), and in the early 20th century a general
setting for analysis was formulated, called a metric space. It is a set on which a notion of
distance between each pair of elements is deﬁned, and in which notions from calculus in
R (open and closed intervals, convergent sequences, continuous functions) can be studied.
Many of the fundamental types of spaces used in analysis are metric spaces (e.g., Hilbert
spaces and Banach spaces), so metric spaces are one of the ﬁrst abstractions that has to be
mastered in order to learn analysis.
2. Metric spaces
In R, the magnitude of a number x is its absolute value |x| and the distance between two
numbers x and y is the absolute value of their diﬀerence:1 |x −y|. In Rm, the length of a
vector x = (x1, . . . , xm) is its norm ||x|| =
p
x2
1 + · · · + x2m and the distance between two
vectors x = (x1, . . . , xm) and y = (y1, . . . , ym) is the norm of their diﬀerence: ||x −y|| =
p
(x1 −y1)2 + · · · + (xm −ym)2.
The distance between points is essential in deﬁning limits, the central idea of calculus.
There are limits of function values and limits of sequences. Focusing on the case of sequences
(we will deal with limits and continuous functions in Section 8), we say a sequence {xn} of
real numbers has limit x, and write limn→∞xn = x or just xn →x, if for every ε > 0 there
is an N ≥1 (it is understood that N = Nε is an integer depending on ε) such that
n ≥N =⇒|xn −x| < ε.
For a sequence {xn} in Rm, we write limn→∞xn = x or xn →x for an x ∈Rm if for every
ε > 0 there is an N = Nε such that
n ≥N =⇒||xn −x|| < ε.
Distances are useful not only between points in Euclidean space, but also between func-
tions. For continuous functions f, g: [0, 1] →R, here are two diﬀerent ways of deﬁning how
far apart they are:
(2.1)
max
0≤x≤1 |f(x) −g(x)|,
Z 1
0
|f(x) −g(x)| dx.
What do these mean for the graphs of the functions below (in red and blue)?
1The bar notation for absolute values was created by Weierstrass in 1841. Earlier Cauchy [1, p. 453] had
written |x| as val.num.x since it was called the “numerical value” (valeur num´erique) of x.
1

<!-- page 2 -->
2
KEITH CONRAD
0
1
The ﬁrst formula in (2.1) is the length of the largest vertical line separating the graphs
(the dashed line in the diagram), so saying f and g are close in this way means their graphs
never get far apart from each other. The second formula is the area of the region over [0, 1]
that is enclosed by both graphs (“area between the curves”), so f and g are close in this
way if, roughly speaking, the graphs can only be far apart over small regions (thereby not
aﬀecting the total area between the curves that much).
The desire to create a single framework for all the known settings where limit ideas are
used inspired Maurice Fr´echet in his 1906 PhD thesis [3] to make the following deﬁnition.
Deﬁnition 2.1. A metric on a set X is a function d: X × X →R satisfying the following
three properties:
(i) d(x, y) ≥0 for all x and y in X, and d(x, y) = 0 if and only if x = y,
(ii) d(x, y) = d(y, x) for all x and y in X,
(iii) d(x, y) ≤d(x, z) + d(z, y) for all x, y, z ∈X.2
A set X together with a choice of a metric d on it is called a metric space and is denoted
(X, d), or just X if the metric3 is understood from context.
Property (iii) is called the triangle inequality. It abstracts the fact that the length of a
side of a triangle is at most the sum of the lengths of the other two sides (see ﬁgure below).
x
y
z
d(x, y)
d(z, y)
d(x, z)
Example 2.2. On Rm the Euclidean metric is
dE(x, y) = ||x −y|| =
p
(x1 −y1)2 + · · · + (xm −ym)2,
This is the usual distance used in Rm, and when we speak about Rm as a metric space
without specifying a metric, it’s the Euclidean metric that is intended.
To check dE is a metric on Rm, the ﬁrst two conditions in the deﬁnition are obvious.
The third condition is a consequence of the inequality ||x + y|| ≤||x|| + ||y|| (replace x and
x −z and y with z −y), and to show this inequality holds we will write ||x|| in terms of
2Condition (iii) is the same as d(x, z) + d(z, y) ≥d(x, y), but the deﬁnition never presents (iii) like that.
3In his thesis, Fr´echet did not use the term “metric,” but instead wrote ´ecart [3, p. 30], which is French for
“gap.” He wrote (A, B) instead of d(A, B).

<!-- page 3 -->
METRIC SPACES
3
the dot product: ||x||2 = x2
1 + · · · + x2
m = x · x, so
||x + y||2 = (x + y) · (x + y)
= x · x + x · y + y · x + y · y
= ||x||2 + 2x · y + ||y||2
≤||x||2 + 2|x · y| + ||y||2.
The famous Cauchy–Schwarz inequality says |x · y| ≤||x||||y||, so
||x + y||2 ≤||x||2 + 2||x||||y|| + ||y||2 = (||x|| + ||y||)2
and now take square roots.
A diﬀerent metric on Rm is
d∞(x, y) = max
1≤i≤m |xi −yi|.
Again, the ﬁrst two conditions of being a metric are clear, and to check the triangle inequality
we use the fact that it is known for the absolute value. If max |xi −yi| = |xk −yk| for a
particular k from 1 to m, then d∞(x, y) = |xk −yk|, so
d∞(x, y) ≤|xk −zk| + |zk −yk| ≤max
1≤i≤m |xi −zi| + max
1≤i≤m |zi −yi| = d∞(x, z) + d∞(z, x).
While the metrics dE and d∞on Rm are diﬀerent, they’re not that diﬀerent from each
other since each is bounded by a constant multiple of the other one:
(2.2)
dE(x, y) ≤√m d∞(x, y),
d∞(x, y) ≤dE(x, y).
Example 2.3. Let C[0, 1] be the space of all continuous functions [0, 1] →R. Two metrics
used on C[0, 1] are in (2.1):
d∞(f, g) = max
0≤x≤1 |f(x) −g(x)|,
d1(f, g) =
Z 1
0
|f(x) −g(x)| dx.
Checking these are metrics is left to the reader.4 Notice for d1 that the condition d1(f, g) =
0 =⇒f = g for being a metric uses continuity of the functions to know
R 1
0 |f(x)−g(x)| dx =
0 =⇒|f(x) −g(x)| = 0 for all x ∈[0, 1].5
Unlike with the two metrics on Rm in Example 2.2, while we have d1(f, g) ≤d∞(f, g)
there is no constant A > 0 that makes d∞(f, g) ≤Ad1(f, g) for all f and g. These metrics
d1 and d∞on C[0, 1] are quite diﬀerent. In terminology we’ll meet later, C[0, 1] is complete
for d∞but not for d1.
Example 2.4. If (X, d) is a metric space and Y is a nonempty subset of X, then Y with
the metric d|Y , which is d with its domain restricted to Y × Y , is a metric space (check!).
For example, any nonempty A ⊂R is a metric space with d(x, y) = |x −y| for x and y in
A.
4For d∞to make sense requires each continuous function on [0, 1] to have a maximum value. This is the
Extreme Value Theorem, which we’ll prove later as Theorem 8.2. It is convenient to have d∞available
strictly for examples before then.
5For p ≥1 the function dp(f, g) =
pqR 1
0 |f(x) −g(x)|p dx is a metric on C[0, 1], and as p →∞, dp(f, g) →
max0≤x≤1 |f(x) −g(x)|, which is why the metric d∞has the notation it does.

<!-- page 4 -->
4
KEITH CONRAD
Example 2.5. Every set X can be given the discrete metric
d(x, y) =
(
0,
if x = y,
1,
if x ̸= y,
which sets all pairs of (distinct) points in X at distance 1 from each other.
All three
conditions for being a metric are easy to check.
Example 2.6. If d is a metric on X, then the functions d′(x, y) = min(d(x, y), 1) and
d′′(x, y) = d(x, y)/(1 + d(x, y)) are also metrics on X. The only part that requires careful
checking is the triangle inequality, which is left to the reader. Note d′ and d′′ are both
bounded: they never take a value larger than 1.
These two metrics are similar to the
original metric d when d has value at most 1:
(2.3)
d(x, y) ≤1 =⇒d′(x, y) = d(x, y)
and
1
2d(x, y) ≤d′′(x, y) ≤d(x, y).
If d(x, y) > 1 then d′ and d′′ change the distance between x and y in diﬀerent ways: d′
redeﬁnes the distance to be 1, while d′′ makes the distance less than 1 in a smoother way.
3. Limit of a sequence in a metric space
Armed with a notion of distance, as codiﬁed in a choice of a metric, we can carry over
the deﬁnition of the limit of a sequence from Euclidean space to metric spaces.
Deﬁnition 3.1. For a sequence xn in a metric space (X, d), we say xn converges to x ∈X,
and write limn→∞xn = x or xn →x, if for every ε > 0 there is an N = Nε such that
n ≥N =⇒d(xn, x) < ε.
If a sequence in (X, d) has a limit we say the sequence is convergent.
Example 3.2. For x ∈X, the constant sequence {x, x, x, . . .} is convergent with limit x.
Similarly, an eventually constant sequence (xn = x for all large n) is convergent. This is
true no matter what metric is used.
Example 3.3. If d is the discrete metric on X then a convergent sequence must be even-
tually constant: if d(xn, x) < 1 for large n then xn = x for large n.
These examples are boring. The reader should know many interesting examples of con-
vergent sequences in R from calculus.
Saying xn →x in a metric space (X, d) is the same as saying d(xn, x) →0 in R:
convergence of a sequence to a speciﬁc value means the distance between the terms of the
sequence and that value tends to 0.
To get used to the terminology, let’s prove four intuitively reasonable theorems about
convergent sequences (try drawing a picture for each one).
Theorem 3.4. If a sequence {xn} in a metric space (X, d) converges then d(xn, xn+1) →0.
Proof. Showing the numbers d(xn, xn+1) tend to 0 means we want to show for every ε >
0 that there is an N such that n ≥N =⇒d(xn, xn+1) < ε.
(We don’t need to say
|d(xn, xn+1)| < ε since values of a metric are nonnegative.)
Say limn→∞xn = x. Using the triangle inequality,
d(xn, xn+1) ≤d(xn, x) + d(x, xn+1) = d(xn, x) + d(xn+1, x).

<!-- page 5 -->
METRIC SPACES
5
The two terms on the right get small when n is large, so d(xn, xn+1) gets small when n is
large. To be precise, for ε > 0 also ε/2 > 0, so there’s an N ≥1 such that for all m ≥N
we have d(xm, x) < ε/2. Therefore
n ≥N =⇒n + 1 ≥N =⇒d(xn, xn+1) ≤d(xn, x) + d(xn+1, x) < ε
2 + ε
2 = ε.
□
Remark 3.5. If we had stuck with ε rather than ε/2 all the way through the proof then
we’d get 2ε at the end instead of ε, and then we’d have to say “Now go back and replace ε
with ε/2 . . .” to get the desired conclusion. The idea of using ε/2 in place of ε in the middle
in order to get a single ε at the end is called an ε/2 argument. This type of reasoning occurs
all the time in analysis. Instead of ε/2 one might use ε/3, √ε, or ε/2n (the last one is good
if we have a whole sequence of terms that need bounds whose sum is still less than ε).
Theorem 3.6. Every subsequence of a convergent sequence in a metric space is also con-
vergent, with the same limit.
Proof. Let xn →x in (X, d) and let {xni} be a subsequence of {xn}. Then n1 < n2 < · · · .
Set yi = xni. We want to show yi →x.
For ε > 0 there is an N such that n ≥N =⇒d(xn, x) < ε. Since the integers ni are
increasing, we have ni ≥N if we go out far enough: there’s an I such that i ≥I =⇒ni ≥
N =⇒d(xni, x) < ε, so d(yi, x) < ε. Thus yi →x.
□
Theorem 3.7. In a metric space (X, d), if two sequences {xn} and {x′
n} converge to the
same value then d(xn, x′
n) →0.
Proof. Suppose xn →x and x′
n →x. Then d(xn, x′
n) ≤d(xn, x) + d(x, x′
n) = d(xn, x) +
d(x′
n, x) and the last two terms get small for large n. This suggests using an ε/2 argument.
For each ε > 0 there’s an N1 such that n ≥N1 =⇒d(xn, x) < ε/2 and an N2 such that
n ≥N2 =⇒d(x′
n, x) < ε/2. Set N = max(N1, N2), so
n ≥N =⇒d(xn, x′
n) ≤d(xn, x) + d(x′
n, x) < ε
2 + ε
2 = ε.
□
The converse to Theorem 3.7 is false: sequences for which d(xn, x′
n) →0 do not have
to converge. After all, let {xn} be an arbitrary sequence and let x′
n = xn for all n, so
d(xn, x′
n) = 0 all the time.
The next result is a partial converse to Theorem 3.7.
Theorem 3.8. In a metric space (X, d), if xn →x and {x′
n} is a sequence such that
d(xn, x′
n) →0 then x′
n →x.
Proof. This will be an ε/2 argument.
Pick ε > 0. We want to ﬁnd an N such that n ≥N =⇒d(x′
n, x) < ε.
There’s an N1 such that n ≥N1 =⇒d(xn, x) < ε/2. Since the real numbers d(xn, x′
n)
tend to 0, there’s an N2 such that n ≥N2 =⇒d(xn, x′
n) < ε/2. Setting N = max(N1, N2),
we have
n ≥N =⇒d(x′
n, x) ≤d(x′
n, xn) + d(xn, x) < ε
2 + ε
2 = ε.
□
Example 3.9. On Rm, because the metrics dE and d∞are each bounded above by a
constant multiple of the other (see (2.2)), we have dE(xn, x) →0 if and only if d∞(xn, x) →
0. Therefore convergence of sequences in Rm for both metrics means the same thing (with
the same limits).

<!-- page 6 -->
6
KEITH CONRAD
Example 3.10. In Example 2.6 we introduced two alternatives to a metric d that are both
bounded metrics: d′(x, y) = min(d(x, y), 1) and d′′(x, y) = d(x, y)/(1 + d(x, y)). Condition
(2.3) shows d′ and d′′ have the same convergent sequences and limits as d.
Example 3.11. In C[0, 1] consider the sequence of functions xn for n ≥1, graphed below.
0
1
This sequence converges to 0 in the metric d1 but not in the metric d∞:
d1(xn, 0) =
Z 1
0
|xn| dx =
1
n + 1 →0,
d∞(xn, 0) = max
0≤x≤1 |xn| = 1.
In fact the sequence {xn} in C[0, 1] has no limit at all relative to the metric d∞.
To prove {xn} has no limit in (C[0, 1], d∞), not just that the constant function 0 is not
a limit, we seek a property that all convergent sequences satisfy and the sequence {xn} in
(C[0, 1], d∞) does not satisfy. Theorem 3.4 tells us every convergent sequence in a metric
space has the distance between consecutive terms tending to 0. Might d∞(xn, xn+1) not
tend to 0? Well,
d∞(xn, xn+1) = max
0≤x≤1 |xn −xn+1| = max
0≤x≤1(xn −xn+1)
and by calculus xn −xn+1 = xn(1 −x) is is maximized on [0, 1] at x = n/(n + 1), where the
value is (n/(n + 1))n(1 −n/(n + 1)) ∼(1/e)(1/(n + 1)) →0. Our idea failed to help.
Rather than looking at the distance between consecutive terms in a sequence, we can look
at the distance between the nth and (2n)th terms. In the proof of Theorem 3.4 it wasn’t so
crucial that the terms from the sequence were consecutive. The exact same reasoning used
there works with the nth and (2n)th terms, so if the sequence {xn} in (C[0, 1], d∞) has a
limit then d∞(xn, x2n) →0 as n →∞. Since
d∞(xn, x2n) = max
0≤x≤1 |xn −x2n| = max
0≤x≤1 xn(1 −xn)
and the function xn(1−xn) on [0, 1] has its maximum value at x = 1/
n√
2, where xn(1−xn) =
(1/2)(1/2) = 1/4, which is independent of n, this proves {xn} has no limit in (C[0, 1], d∞).
To know what a metric on a set X means, know what it means to say two points are
close in that metric. For example, when we say fn →f in (C[0, 1], d∞), it means the graph
of fn is getting close to f uniformly (at the same rate) over all of [0, 1] as n →∞. A picture
of f (in blue) and an approximation fn (in red) in the metric d∞is pictured below.

<!-- page 7 -->
METRIC SPACES
7
0
1
y = f(x)
y = fn(x)
When fn →f in (C[0, 1], d∞) we say fn →f uniformly on [0, 1]. This implies pointwise
convergence: fn(a) →f(a) for each a ∈[0, 1] since
|fn(a) −f(a)| ≤max
0≤x≤1 |fn(x) −f(x)| = d∞(fn, f) →0.
However the converse is false:
if fn(a) →f(a) for each a ∈[0, 1] it does not mean
d∞(fn, f) →0. Pointwise convergence does not imply convergence can be controlled in
the same way simultaneously on the whole domain [0, 1]. Consider the functions fn(x) on
[0, 1] graphed below which are an isoceles triangle of height 1 over [0, 1/n] and 0 for x ≥1/n.
We have fn(0) = 0 for all n, and for each a ∈(0, 1] we have fn(a) = 0 for large enough n,
so fn(a) →0 for each a ∈[0, 1], but d∞(fn, 0) = 1 so fn does not get close to the function
0 as n gets large because every fn has a peak of height 1.
0
1
1/n
1
y = fn(x)
Changing metrics from d∞to d1, saying fn →f in (C[0, 1], d1) does not guarantee
pointwise convergence. For example, d1(xn, 0) →0 and numerically an →0 for 0 ≤a < 1,
but not at a = 1.
4. Cauchy sequences and completeness
One aspect of inﬁnite series that many students ﬁnd hard to understand is how conver-
gence tests really work: one may prove with the comparison test that P
k≥1 xk/k2 converges
for x in the interval [−1, 1], but what does it converge to? The subtlety here is that we are
saying something converges without identifying the limit in a concrete way. (Saying “the
series is what the limit is” sounds more circular than explanatory.) Often we want to prove
a sequence (of numbers or functions or shapes) has a limit even if we don’t yet have a tidy
name for the limiting object. How can convergence be detected before the limit is known?
A clue is in Theorem 3.4: if xn →x in a metric space (X, d) then d(xn, xn+1) →0. The
conclusion makes no reference to the original limit x. Unfortunately, this property that
the terms become “consecutively close” is not good enough to characterize convergence in

<!-- page 8 -->
8
KEITH CONRAD
general metric spaces. We saw this in Example 3.11, where the sequence of power functions
xn in (C[0, 1], d∞) does not converge but d∞(xn, xn+1) ∼(1/e)(1/(n+1)) →0. A more basic
example is the harmonic series, which diverges and its partial sums Hn = 1+1/2+· · ·+1/n
are consecutively close: |Hn −Hn+1| = 1/(n + 1) →0.
By making a slight change in the proof of Theorem 3.4, we get a much stronger conclusion
than consecutive closeness, and this stronger conclusion will be exactly what we need.
Theorem 4.1. If {xn} is a convergent sequence in a metric space (X, d) then the terms
of the sequence become “uniformly close”: for every ε > 0 there is an N ≥1 such that
m, n ≥N =⇒d(xm, xn) < ε.
Proof. We run through the proof of Theorem 3.4 and make a few changes. Letting x =
limn→∞xn, the triangle inequality tells us for all m and n that
d(xm, xn) ≤d(xm, x) + d(x, xn) = d(xm, x) + d(xn, x).
We now make an ε/2 argument. For every ε > 0 there’s an N ≥1 such that for all n ≥N
we have d(xn, x) < ε/2. Therefore
m, n ≥N =⇒d(xm, xn) ≤d(xm, x) + d(xn, x) < ε
2 + ε
2 = ε.
□
This concept of uniform closeness, which is a property of a sequence involving no direct
reference to a hypothetical limit, is much more stringent than consecutive closeness. For
example, if Hn = 1 + 1/2 + · · · + 1/n then the numbers Hn are consecutively close (that
is, |Hn −Hn+1| →0) but they are not uniformly close. It can be shown, for instance, that
|Hn −H2n| →log 2 ≈.693.
When calculus was acquiring rigorous foundations in the 19th century, it was realized that
uniform closeness in Theorem 4.1 captures the idea of convergence for sequences without
mentioning a limit for the sequence. This property is not actually called uniform closeness,
but is named in honor of Cauchy, who articulated and used it in the setting of inﬁnite series.
Deﬁnition 4.2. A sequence {xn} in a metric space (X, d) is called a Cauchy sequence if
for every ε > 0 there is an N = Nε such that for all m, n ≥N we have d(xm, xn) < ε.
Theorem 4.3. Every convergent sequence in a metric space is a Cauchy sequence.
Proof. This is Theorem 4.1.
□
Corollary 4.4. If (X, d) is a metric space and Y is a subset of X given the induced metric
d|Y , then each sequence in Y that converges in X is a Cauchy sequence in (Y, d|Y ).
Proof. A sequence {yn} in Y that converges in X is Cauchy in X by Theorem 4.3. Since
the metric d on X is the metric we are using on Y , the Cauchy property of {yn} in X can
be viewed as the Cauchy property in Y .
□
Example 4.5. Consider the interval (0, ∞) as a metric space using the absolute value
metric induced from R. We have 1/n →0 in R, but the sequence {1/n} has no limit in
(0, ∞) since 0 ̸∈(0, ∞). The sequence {1/n} is a Cauchy sequence in (0, ∞) by Corollary
4.4 but it is not a convergent sequence in (0, ∞).
Example 4.6. On Rm, the metrics dE and d∞satisfy d∞≤dE ≤√m d∞, so a sequence
in Rm is Cauchy with respect to one of these metrics if and only if it is Cauchy with respect
to the other one.

<!-- page 9 -->
METRIC SPACES
9
Being a Cauchy sequence means if you go out far enough into the sequence then all the
terms from some point onwards are as close together as you wish. While this property
is much stronger than being a consecutively close sequence, a sequence whose terms get
consecutively close rapidly enough is a Cauchy sequence. The next theorem says that being
consecutively close at least at the rate of a geometric progression is rapid enough.
Theorem 4.7. If {xn} is a sequence in a metric space (X, d) such that d(xn, xn+1) ≤arn
for all n, where a > 0 and 0 < r < 1, then {xn} is a Cauchy sequence.
Proof. For 1 ≤m < n, a massive use of the triangle inequality tells us
d(xm, xn) ≤d(xm, xm+1) + d(xm+1, xm+2) + · · · + d(xn−1, xn)
≤arm + arm+1 + · · · + arn−1
<
∞
X
k=m
ark
= arm
1 −r.
The bound d(xm, xn) < arm/(1 −r) is also true if m = n since d(xm, xm) = 0.
Since 0 < r < 1, the terms arn tend to 0 as n →∞. Now if we pick an ε > 0, choose
N large enough that rN < (1 −r)ε/a.
(Why (1 −r)ε/a and not ε?
You’ll soon see.)
For m, n ≥N, without loss of generality m ≤n so by our prior calculation d(xm, xn) <
arm/(1 −r) ≤arN/(1 −r), which is less than ε, so our sequence is Cauchy.
□
More generally, if d(xn, xn+1) ≤cn and the inﬁnite series P∞
n=1 cn in R converges then
{xn} is a Cauchy sequence.
Just as convergence is preserved when passing to a subsequence (Theorem 3.6), so is the
Cauchy property.
Theorem 4.8. Every subsequence of a Cauchy sequence in a metric space is also a Cauchy
sequence.
Proof. Adapt the proof of Theorem 3.6. Details are left to the reader.
□
Theorem 3.8 also has an analogue for Cauchy sequences.
Theorem 4.9. In a metric space (X, d), if {xn} is a Cauchy sequence and {x′
n} is a
sequence such that d(xn, x′
n) →0 then {x′
n} is a Cauchy sequence.
Proof. Use d(x′
m, x′
n) ≤d(x′
m, xm) + d(xm, xn) + d(xn, x′
n). and an ε/3 argument to adapt
the proof of Theorem 3.8.
□
A Cauchy sequence in a metric space X should be thought of as a sequence that wants
to have a limit in X, but we saw in Example 4.5 that not all Cauchy sequences in X
necessarily have a limit in X. If a metric space has a non-convergent Cauchy sequence
then we should imagine the space has a point missing where the “ideal limit” for that non-
convergent Cauchy sequence ought to be. A metric space in which all Cauchy sequences
converge has no missing points, and such spaces have a special name.
Deﬁnition 4.10. A metric space (X, d) is called complete if every Cauchy sequence in X
converges in X: if {xn} is Cauchy in X then there’s an x ∈X such that xn →x.

<!-- page 10 -->
10
KEITH CONRAD
Convergent sequences are always Cauchy (Theorem 4.3), and metric spaces are complete
when the converse is true, so Cauchy = convergent for sequences in complete metric spaces.
Analysis uses completeness of a metric since often the only way to construct a limit is to
create a Cauchy sequence ﬁrst and then pass to its limit.
Let’s take a look at some complete and incomplete metric spaces.
Example 4.11. The metric space R with the absolute value metric d(x, y) = |x −y| is
complete. A proof of this uses fundamental properties of the real numbers like the existence
of least upper bounds for nonempty bounded subsets of R. See [4, Theorem 10.11].
Example 4.12. The closed intervals [0, 1] and [0, ∞) with metric from R are complete.
The open intervals (0, 1) and (0, ∞) with metric from R are not complete: a sequence in
the interval that tends to 0 is Cauchy but does not converge in the interval.
Example 4.13. The rational numbers Q with the absolute value metric d(r, s) = |r −s|
are not complete. To prove this, pick an irrational real number L (like
√
2 or π) and let
rn be the sequence of decimal approximations to L truncated at the 1/10n place. Each
ﬁnite decimal is rational, so rn ∈Q. Since rn →L in R, {rn} is a Cauchy sequence in Q
(Corollary 4.4). However, {rn} has no limit in Q, so Q is not complete.
Example 4.14. The integers with the absolute value metric are complete: each Cauchy
sequence in Z (as a metric space inside R) is eventually constant. This is boring.
Example 4.15. A set X with the discrete metric on it (Example 2.5) is complete: if d
is the discrete metric and d(xm, xn) < 1 then xm = xn, so every Cauchy sequence for the
discrete metric is an eventually constant sequence, which clearly converges.
Example 4.16. The metric space (C[0, 1], d∞) is complete. A proof is in Appendix A.
Example 4.17. The metric space (C[0, 1], d1) is not complete. To prove this we will follow
the idea of Example 4.13 by writing down a discontinuous function that is a d1-limit of
continuous functions. Note the d1-metric makes sense for piecewise continuous functions on
[0, 1], since they are integrable.
In the picture below, let f(x) (in red) be the discontinuous function that’s 0 for 0 ≤x <
1/2 and 1 for 1/2 ≤x ≤1. For n ≥2 let fn(x) be a piecewise linear approximation (in
blue) breaking from values 0 and 1 at x = 1/2 ± 1/n, where it’s linear in between.
y = fn(x)
y = f(x)
0
1
1/2
1
The region below fn(x) and above the x-axis to the left of x = 1/2 is a right triangle
with a base of width 1/2 −(1/2 −1/n) = 1/n and height 1/2, so
Z 1
0
|fn(x) −f(x)| dx = 2
Z 1/2
0
|fn(x)| dx = 2 · 1
2
1
n
1
2 = 1
2n.

<!-- page 11 -->
METRIC SPACES
11
Therefore
d1(fm, fn) =
Z 1
0
|fm(x)−fn(x)| dx ≤
Z 1
0
|fm(x)−f(x)| dx+
Z 1
0
|f(x)−fn(x)| dx =
1
2m+ 1
2n,
which tends to 0 as m, n →∞. Thus {fn} is Cauchy in (C[0, 1], d1), but it has no limit in this
metric space. If fn →g in (C[0, 1], d1) then
R 1
0 |f(x)−g(x)| dx = 0, so
R b
0 |f(x)−g(x)| dx = 0
and
R 1
b |f(x) −g(x)| dx = 0 for all b in (0, 1). Using 0 < b < 1/2 in the ﬁrst integral and
1/2 < b < 1 in the second integral,
R b
0 |g(x)| dx = 0 for 0 < b < 1/2 and
R 1
b |1 −g(x)| dx = 0
for 1/2 < b < 1. Therefore g(x) = 0 for 0 ≤x < 1/2 and g(x) = 1 for 1/2 < x ≤1, but no
value can be assigned to g(1/2) to make this continuous.
When a metric space is not complete, like (Q, | · |) or (C[0, 1], d1), we want to “ﬁll in all
the holes” to create a complete metric space containing the original one. To describe this
larger space, we need one more concept.
Deﬁnition 4.18. A subset S ⊂X is called dense if every element of X is the limit of a
sequence in S or equivalently every open ball around an element of X contains an element
of S.
Example 4.19. The rational numbers are dense in R but the integers are not dense in R.
Deﬁnition 4.20. A completion of a metric space (X, d) is a complete metric space ( b
X, bd)
that contains X, the metric bd restricted to X is d, and X is a dense subset of b
X.
Example 4.21. The completion of (Q, | · |) is (R, | · |). If we think of R inside R2 as the
x-axis then the completion of Q is not R2 even though R2 is complete, since Q is not dense
in R2. The idea of a completion is ﬁlling in the holes (missing limits of Cauchy sequences)
and not adding anything more, which is why the completion of a metric space is required
to have the original metric space as a dense subset.
Theorem 4.22. Every metric space has a completion.
Proof. See Appendix A.
□
5. Open and closed subsets
In calculus, a lot of attention is paid to intervals: open intervals (a, b), closed intervals
[a, b], and half-open intervals (a, b] and [a, b). Allowing the endpoints to be ±∞introduces
the distinction between bounded and unbounded intervals. There are theorems about con-
tinuous or diﬀerentiable functions on intervals (Intermediate Value Theorem, Extreme Value
Theorem, Mean Value Theorem), deﬁnite integrals are deﬁned on intervals, and the set of
numbers where a power series converges is an interval. What is so special about intervals?
It turns out that the key feature of intervals for one application may be quite diﬀerent
from the key feature needed for another application. Over the next few sections we will
isolate several of these features and present the generalization of each one in metric spaces.
This leads to many special types of subsets of a metric space, such as open balls, closed
balls, compact subsets, and connected subsets. We will see that
• open intervals (a, b) with a, b ∈R generalize to open balls and connected subsets,
• closed intervals [a, b] with a, b ∈R generalize to closed balls, compact subsets, and
connected subsets.

<!-- page 12 -->
12
KEITH CONRAD
In this section we generalize open and closed intervals in R to open and closed balls of a
metric space. Throughout, (X, d) is a metric space.
Deﬁnition 5.1. For a ∈X and r ≥0, the open ball with center a and radius r is
B(a, r) = {x ∈X : d(a, x) < r}
and the closed ball with center a and radius r is
B(a, r) = {x ∈X : d(a, x) ≤r}.
When r = 0, B(a, 0) = ∅and B(a, 0) = {a} by the axioms for a metric. Some writers
only consider balls to have positive radius.
In a general metric space, the picture to have in mind of open and closed balls should be
discs in the plane: the interior of a disc for open balls and the interior of a disc together
with its boundary circle for closed balls, as shown below.
a
r
a
r
In speciﬁc metric spaces there are better pictures than these. In R, an open ball B(a, r)
is the open interval (a−r, a+r) and a closed ball B(a, r) is the closed interval [a−r, a+r].
Pictured below are the open and closed balls in (C[0, 1], d∞) of radius r around a function
f (in blue), consisting of all functions whose graph deviates by less than r or at most r from
the graph of f.
0
1
0
1
Deﬁnition 5.2. A subset of X is called bounded if it is contained in some ball B(a, r). A
subset that is not bounded is called unbounded.
Since B(a, r/2) ⊂B(a, r) ⊂B(a, r), talking about a subset being contained in an open
ball or a closed ball is the same thing: either case can be turned into the other by changing
the radius if necessary. For example, the deﬁnition of a bounded subset does not change if
we replace open balls in the deﬁnition with closed balls.
Theorem 5.3. Every convergent sequence in a metric space is bounded.

<!-- page 13 -->
METRIC SPACES
13
Proof. If xn →x then there’s an N such that n ≥N =⇒d(xn, x) < 1. Let
r = max(d(x1, x) + 1, . . . , d(xN−1, x) + 1, 1),
so d(xn, x) < r for all n ≥1. Thus the whole sequence is contained in B(x, r).
□
Theorem 5.4. Every Cauchy sequence in a metric space is bounded.
Proof. Let {xn} be Cauchy. There’s an N such that m, n ≥N =⇒d(xm, xn) < 1. In
particular, d(xN, xn) < 1 for n ≥N, so as in the proof of Theorem 5.3 (using xN here in
place of x there) an r can be found such that the whole sequence is in B(xN, r).
□
Since convergent sequences are Cauchy, Theorem 5.3 is a special case of Theorem 5.4.
Deﬁnition 5.5. A subset U ⊂X is called open if for each x ∈U there’s an r > 0 such that
B(x, r) ⊂U. We also consider the empty subset of X to be an open subset.
The idea behind the concept of a subset U being open is that the property of being in
U is stable under small perturbations: if we wiggle each element of U a little bit “in all
directions” then we stay inside of U. Exactly how much we can wiggle a point in U without
leaving U depends on how close we are to the “edge” of U.
Theorem 5.6. Every open ball B(a, r) in X is an open subset, and every open subset of
X is a union of open balls in X.
Proof. Since B(a, 0) = ∅is open in X by deﬁnition, we can assume r > 0. Pick b ∈B(a, r).
We want to ﬁnd an r′ > 0 such that B(b, r′) ⊂B(a, r). The picture below suggests using
r′ = r −d(a, b), which is positive since d(a, b) < r. A dashed circle with radius r′ is drawn
centered around b and just ﬁts inside B(a, r).
a
b
r
d(a, b)
r′
To show B(b, r′) ⊂B(a, r), pick x ∈B(b, r′).
By the triangle inequality d(x, a) ≤
d(x, b) + d(b, a) < r′ + d(a, b) = r, so x ∈B(a, r).
If U ⊂X is open then each point in U is the center of an open ball that’s inside U, by
deﬁnition, so U is a union of open balls.
□
A generic picture to have in mind for an open set in a metric space is a blob without its
boundary, as in the picture below.

<!-- page 14 -->
14
KEITH CONRAD
Theorem 5.7. In a metric space, if {Ui} is a collection of open subsets then S
i∈I Ui is
open. If U1, . . . , Un are ﬁnitely many open subsets then U1 ∩· · · ∩Un is open.
Proof. Each x ∈S
i∈I Ui is in some Ui, so there’s an open ball B(x, r) with r > 0 contained
in that Ui. Thus every point of the union is in an open ball that’s inside the union, so the
union is an open subset.
For the second part, we may assume each Ui is nonempty, since otherwise the intersection
is empty, and ∅is open by deﬁnition. Pick x ∈U1 ∩· · · ∩Un. For each j = 1, . . . , n we have
B(x, rj) ⊂Uj for some rj > 0, so B(x, r) ⊂U1 ∩· · · ∩Un when r = min(r1, . . . , rn) > 0.
□
It is false that the intersection of inﬁnitely many open sets has to be open. For example,
in R we can write [0, 1] = T
n≥1(−1/n, 1 + 1/n) and [0, 1] is not an open subset of R.
Deﬁnition 5.8. A subset C ⊂X is called closed if for each sequence in C that has a limit
in X, the limit is in C: if cn ∈C and cn →x ∈X then x ∈C. We also consider the empty
subset of X to be a closed subset.
A subset being closed means limit operations don’t take us outside the set. The following
picture is a closed blob. It includes the boundary curve, so no sequence in the closed blob
can have a limit outside the closed blob.
Theorem 5.9. Every closed ball B(a, r) in X is a closed subset.
Proof. We need to show for each sequence {xn} in B(a, r) with xn →x ∈X that x ∈B(a, r).
That is, if xn →x and d(a, xn) ≤r for all n then d(a, x) ≤r.
Assume to the contrary that d(a, x) > r.
We are going to prove from xn →x that
d(a, xn) > r for some n, which would be a contradiction since every xn is in B(a, r).
a
r
x y
xn
Consider the open ball with center x and radius r′ = d(a, x) −r. Then r′ > 0. The
picture above suggests that no element of B(x, r′) lies in B(a, r), and we can prove this
using the triangle inequality:
y ∈B(x, r′) =⇒d(a, x) ≤d(a, y) + d(y, x) < d(a, y) + r′ =⇒d(a, y) > d(a, x) −r′ = r,
so y ̸∈B(a, r).
Since xn →x, some xn is in B(x, r′), but we proved B(x, r′) is disjoint from B(a, r), so
xn ̸∈B(a, r) and that’s a contradiction. Thus “d(a, x) > r” is false, so d(a, x) ≤r.
□

<!-- page 15 -->
METRIC SPACES
15
Here is the “closed” counterpart of Theorem 5.7.
Theorem 5.10. In a metric space, if {Ci} is a collection of closed subsets then T
i∈I Ci is
closed. If C1, . . . , Cn are ﬁnitely many closed subsets then C1 ∪· · · ∪Cn is closed.
Proof. We can assume T
i∈I Ci ̸= ∅, since the empty set is closed by deﬁnition. Thus we
can assume each Ci is nonempty.
Call the metric space X and let {cn} be a sequence in T
i∈I Ci that converges to some
x ∈X. For each i ∈I we have {cn} ⊂Ci, so x ∈Ci since Ci is closed. Thus x ∈T
i∈I Ci.
For the second part, we can assume at least one of C1, . . . , Cn is nonempty, so the union
is nonempty. Let {cn} be a sequence in C1 ∪· · · ∪Cn with limit x ∈X. We want to show
x is in the union. A sequence has inﬁnitely many terms, so one of C1, . . . , Cn contains
inﬁnitely many terms of the sequence. That is, a subsequence of {cn} lies entirely inside
some Cj. Since each subsequence of a convergent sequence also converges with the same
limit (Theorem 3.6), and Cj is closed, it follows that x ∈Cj ⊂C1 ∪· · · ∪Cn.
□
It is false that the union of inﬁnitely many closed subsets has to be closed. For example,
in R we can write (0, 1) = S
n≥1[1/n, 1 −1/n] and (0, 1) is not a closed subset of R.
Theorem 5.11. Every closed subset of a complete metric space is complete.
Proof. Let C be a closed subset of X. Each Cauchy sequence in C is Cauchy in X, so it
has a limit x ∈X by completeness of X. Since C is a closed subset of X, we must have
x ∈C. Thus all Cauchy sequences in C converge in C, so C is complete.
□
Deﬁnition 5.12. A limit point of a subset S ⊂X is a point of X that is the limit of some
sequence in S.
Deﬁnition 5.13. The closure of a subset S ⊂X is the union of S and its limit points in
X. This set is denoted S.
Example 5.14. For all a ∈Rm and r > 0, B(a, r) = B(a, r): the closure of every
(nonempty) open ball in Rm is the closed ball with the same center and radius. In general
metric spaces, this intuitively appealing property might be false.
Theorem 5.15. For every subset S ⊂X, its closure S is closed in X and S is the smallest
closed subset of X containing S. In particular, S is closed if and only if S = S.
Proof. If S ⊂C ⊂X and C is closed in X then each limit point of S lies in C, so S ⊂C.
It remains to show S is closed.
Let {xn} be a sequence in S with limit x ∈X. Since each xn is a limit point of S, there’s
some sn ∈S such that d(xn, sn) < 1/n. Then xn →x and d(xn, sn) →0, so sn →x by
Theorem 3.8. Therefore x ∈S.
□
Dense subsets were deﬁned in Deﬁnition 4.18. They can also be described using closures.
Theorem 5.16. A subset S ⊂X is dense if and only if S = X.
Proof. Saying S is dense means every element of X is a limit point of S, so X ⊂S. The
reverse containment is true by deﬁnition.
□
We have developed properties of open subsets and closed subsets separately. The following
theorem shows they are in fact complementary concepts!
Theorem 5.17. A subset of X is open if and only if its complement is closed.

<!-- page 16 -->
16
KEITH CONRAD
Proof. Pick an open subset U. To prove its complement X −U is closed, we can assume
X −U ̸= ∅since the empty set is closed by deﬁnition.
Let {xn} be a sequence in X −U with limit x ∈X. To prove x ∈X −U, assume this is
not true, so x ∈U. Then there’s some r > 0 such that B(x, r) ⊂U. However, since xn →x
the ball B(x, r) must contain some xn, which is impossible since xn ∈X −U. Thus x ̸∈U.
Now pick a closed subset C. We want to prove its complement X −C is open, and as
before we can assume X −C ̸= ∅since the empty set is open by deﬁnition. Pick a point
x ∈X −C. We want to ﬁnd an r > 0 such that B(x, r) ⊂X −C. Assume there is no
such r, so for every r > 0 the ball B(x, r) contains an element of C. Using the sequence
of radii 1/n, for each n ≥1 the ball B(x, 1/n) contains some element, say xn, of C. Then
d(x, xn) < 1/n for all n, so xn →x. Since every xn is in C and C is closed, we deduce that
x ∈C too. That is a contradiction, so X −C is open.
□
Example 5.18. In R, (0, 1) is open and its complement (−∞, 0] ∪[1, ∞) is closed. The
interval [0, ∞) is closed and its complement (−∞, 0) is open.
Theorem 5.17 is not saying every subset of a metric space is open or closed. Most subsets
are neither. For example, in R the sets [0, 1) and [0, 1] ∪(2, 3) are neither open nor closed.
In light of Theorem 5.17, we now see that Theorems 5.7 and 5.10 are equivalent since
complements exchange unions and intersections as well as open and closed subsets. For
example, if Ci are closed subsets of X then their complements Ui = X −Ci are open
subsets and
X −
\
i∈I
Ci =
[
i∈I
(X −Ci) =
[
i∈I
Ui,
so from Theorem 5.6 saying S
i∈I Ui is open, Theorem 5.17 implies that T
i∈I Ci is closed.
6. Compact subsets
Closed bounded intervals are nice for functions: every continuous real-valued function on
a closed bounded interval is bounded and has maximum and minimum values (see below
on left), but 1/x on (0, 1) is unbounded above and has no minimum (see below on right).
0
1
1
0
1
1
What lies behind the better properties of continuous real-valued functions on closed
bounded intervals turns out to be a property of the interval having nothing to do with
functions: every sequence in a closed bounded interval has a subsequence converging in
that interval. Even if a sequence itself does not converge, some subsequence does. In a
general metric space X, subsets with this property get a special name.

<!-- page 17 -->
METRIC SPACES
17
Deﬁnition 6.1. A subset K of a metric space is called compact if every sequence in K has
a subsequence that converges in K.
The notion of a compact set (in a metric space) was ﬁrst deﬁned by Fr´echet. We will see in
Section 8 some reasons why it is important. It is not an exaggeration to say compactness is
one of the most important concepts in mathematics. Its initial applications were in analysis,
but it is used in geometry, number theory, and even mathematical logic.
Here we will give some examples (and non-examples) and discuss some properties. We
start with the fundamental example.
Theorem 6.2. Every closed bounded interval [a, b] in R is compact.
Proof. Pick a sequence {xn} in [a, b]. All the terms of the sequence are within distance b−a
of each other. To extract a convergent subsequence, we use a repeated bisection method.
Break up [a, b] into two halves: [a, b] = [a, m]∪[m, b] where m = (a+b)/2 is the midpoint.
Inﬁnitely many of the terms in the sequence {xn} have to be in [a, m] or inﬁnitely many
have to be in [m, b] (or maybe both happen). Focusing on a subinterval with inﬁnitely many
xn in it, we get a subsequence denoted x(1)
n
in which all terms are within (b −a)/2 of each
other. Take that subinterval we chose and divide it into left and right halves (overlapping
at the midpoint). Once again, inﬁnitely many terms of {x(1)
n } have to be in one of the two
halves, so by passing to the terms of the subsequence in such a half we get a new (reﬁned)
subsequence {x(2)
n } in which all the terms are within (b −a)/4 of each other.
Repeating this process, we get for each k ≥0 a subsequence {x(k)
n } with n = 1, 2, 3, . . .
in which all the terms are within (b −a)/2k of each other (with x(0)
n
= xn). The way we
construct these subsequences makes them nested:
{xn} = {x(0)
n } ⊃{x(1)
n } ⊃{x(2)
n } ⊃{x(3)
n } ⊃· · ·
Now set yn = x(n)
n
for n ≥1. The sequence {yn} is a subsequence of {xn} and |yn −yn+1| ≤
(b −a)/2n.
Since the sequence {yn} gets consecutively close at least as quickly as the
geometric progression (b−a)/2n, it is a Cauchy sequence by Theorem 4.7. By completeness
of R, the sequence yn has a limit in R, and this limit is in [a, b] since closed intervals are
closed subsets (Theorem 5.9). Thus {xn} has a subsequence that converges in [a, b].
□
Example 6.3. The open interval (0, 1) is not compact in R since the sequence 1/2, 1/3,
1/4, . . . , 1/n, . . . does not have a convergent subsequence within (0, 1): the sequence con-
verges to 0, so all of its subsequences converge to 0, but 0 ̸∈(0, 1). In a similar way, no
(nonempty) open interval in R is compact.6
Theorem 6.4. Every closed bounded box [a1, b1] × · · · × [am, bm] in Rm is compact.
Proof. Let xn = (xn1, . . . , xnm) be a sequence in the box. Look at the sequence of ﬁrst
components: {xn1} is a sequence in [a1, b1], so by compactness of this interval (Theorem
6.2) there is a convergent subsequence {xni1} where n1 < n2 < . . ., with limit y1 ∈[a1, b1].
Consider the subsequence xni = (xni1, . . . , xnim). The ﬁrst components converge to y1.
Look now at the second components xni2: it is a sequence in [a2, b2], so by compactness
6A student taking a real analysis course once told me the instructor focused a lot on [a, b] and the student
didn’t understand the big fuss about distinguishing between [a, b] and (a, b) since “they only diﬀer in two
points.” Those two points make a huge diﬀerence, since it’s why [a, b] is compact and (a, b) is not.

<!-- page 18 -->
18
KEITH CONRAD
of this interval there is a convergent subsequence xnij 2 with limit y2 ∈[a2, b2]. The corre-
sponding subsequence of ﬁrst components xnij 1 still converges to y1 since a subsequence of
a convergent sequence has the same limit (Theorem 3.6).
Now the sub-subsequence xnij in the box has its ﬁrst components converge to y1 and
its second components converge to y2. Repeating this argument until we exhaust all the
components, we will ﬁnally get a subsequence of {xn} in which the kth components have a
limit yk ∈[ak, bk], so that subsequence converges to (y1, . . . , ym), which is in the box.
□
Every bounded sequence in Rm lies in a closed bounded box, so Theorem 6.4 tells us
that every bounded sequence in Rm has a convergent subsequence.7
Theorem 6.5. Every closed and bounded subset of Rm is compact.
Proof. Let C be a closed and bounded subset of Rm and {cn} be a sequence in C. We want
to show {cn} has a subsequence that converges in C.
Since C is bounded in Rm it lies in some open ball B(a, r), which in turn lies in the
closed box [a1 −r, a1 + r] × · · · × [am −r, am + r]. This box is compact (Theorem 6.4), so
{cn} has a subsequence converging in this box, and the limit of this subsequence lies in C
since C is closed.
□
Example 6.6. Every closed ball in Rm is compact, since closed balls are closed subsets
and are clearly bounded.
Theorem 6.7. Every compact subset of a metric space is closed and bounded.
Proof. Let K be a compact subset of the metric space X.
K is closed: Suppose cn ∈K and cn →x ∈X. We want to show x ∈K. By compactness
of K, there is a subsequence cni with a limit c ∈K. When a sequence converges, every
subsequence converges to the same limit (Theorem 3.6), so cni →x. Thus c = x, so x ∈K.
K is bounded: We will prove, contrapositively, that an unbounded subset S of a metric
space is not compact. Pick s0 ∈S. Since S is unbounded, for each integer n ≥1 there is
an sn ∈S such that d(s0, sn) > n. It should be intuitively clear that the sequence {sn} is
not bounded. To prove this, we show every open ball in X can contain only ﬁnitely many
sn: if sn ∈B(a, r), and then
n < d(s0, sn) ≤d(s0, a) + d(a, sn) < d(s0, a) + r,
which is false for large enough n. Since no open ball contains inﬁnitely many sn, every
subsequence of {sn} is unbounded. Therefore no subsequence of {sn} can converge, since
convergent sequences are bounded (Theorem 5.3).
□
Theorems 6.5 and 6.7 together give the following important characterization of compact
subsets of Euclidean space.
Theorem 6.8. A subset of Rm is compact if and only if it is closed and bounded.8
Proof. By Theorem 6.7, a compact subset of every metric space is closed and bounded. By
Theorem 6.5, all closed and bounded subsets of Rm are compact.
□
Theorem 6.8 is not true in general metric spaces: a closed and bounded subset of a metric
space does not have to be compact. That is, the converse of Theorem 6.7 in some metric
spaces is false.
7This property of bounded sequences in Euclidean space is called the Bolzano–Weierstrass theorem.
8This is called the Heine–Borel theorem.

<!-- page 19 -->
METRIC SPACES
19
Example 6.9. On Rm change the Euclidean metric dE to a bounded metric min(1, dE) or
dE/(1+dE) from Example 2.6. Convergent sequences and limits in Rm for these metrics are
the same as for dE (Example 3.10), so they deﬁne the same closed subsets of Rm as dE does
and thus, by taking complements, the same open subsets of Rm as dE does. All (closed)
subsets of Rm are bounded for min(1, dE) and dE/(1+dE), but many closed subsets of Rm
are not compact.
Here’s a less weird counterexample to the converse of Theorem 6.7 (no strange metric).
Example 6.10. We will show in the complete metric space (C[0, 1], d∞) that the closed
unit ball B(0, 1) is not compact.9 The sequence of functions xn lies in this ball and we will
show it has no convergent subsequence. In Example 3.11 we showed this sequence is not
convergent, but saying it has no convergent subsequence is much stronger.
Suppose a subsequence {xni} has a limit f in (C[0, 1], d∞). For each a ∈[0, 1] we have
|ani −f(a)| ≤max
0≤x≤1 |xni −f(x)| = d∞(xni, f),
and since d∞(xni, f) →0 as i →∞it follows that ani →f(a) as i →∞. The exponents
n1, n2, . . . are increasing, so if 0 ≤a < 1 then ani →0. Thus f(a) = 0. If a = 1 then ani = 1
for all ni, so f(1) = 1. But the function that’s 0 on [0, 1) and 1 at 1 is not continuous.
The property of a subset S of a metric space X being compact can be described in a
completely diﬀerent way than with sequences and subsequences, using instead open cover-
ings: an open covering of S is a collection of open subsets Ui in X such that S ⊂S
i∈I Ui.
Here is a picture of an open covering of a closed ball in the plane.
Theorem 6.11. The following properties of a subset K ⊂X are equivalent.
(1) K is compact, i.e., every sequence in K has a subsequence converging in K.
(2) Every open covering of K in X has a ﬁnite subcovering: if K ⊂S
i∈I Ui where all
Ui are open in X then there are Ui1, . . . , Uin such that K ⊂Ui1 ∪· · · ∪Uin.
Proof. (1) =⇒(2):
Step 1: For each r > 0, K is contained in a ﬁnite union of balls of radius r centered at
points in K.
We prove this by contradiction: assume K is not in a ﬁnite union of balls B(x, r) for
x ∈K. Then starting with an x1 ∈K we can build a sequence {xn} inductively: if n ≥2
and we have x1, . . . , xn in K, by assumption K is not contained in B(x1, r) ∪· · · ∪B(xn, r),
so there’s some xn+1 ∈K that’s not in that union. The sequence {xn} we have made
has the property d(xn+1, xk) ≥r for k = 1, . . . , n and all n, which is equivalent to saying
d(xm, xn) ≥r for all pairs of distinct integers m and n.
9While compactness in (C[0, 1], d∞) is not the same as being closed and bounded, there is a set of conditions
in (C[0, 1], d∞) useful for analysis that is equivalent to compactness: look up the Arzel`a–Ascoli theorem.

<!-- page 20 -->
20
KEITH CONRAD
From (1), the sequence {xn} has a subsequence {xnj} with a limit x ∈K, so for all large
enough nj we have d(xnj, x) < r/2. Then for two diﬀerent large nj and nj′ we get
d(xnj, xnj′) < d(xnj, x) + d(x, xnj′) < r
2 + r
2 = r,
and that contradicts the property at the end of the previous paragraph. This ends Step 1.
Step 2: Let {Ui}i∈I be an open covering of K in X. Then there is a number r > 0 such
that for all x ∈K the ball B(x, r) is in some Ui. (Stop at this point and check for K = [0, 1]
and its open covering by the two intervals (−.3, .75) and (.5, 1.5) that this claim is true with
r = .25.)
We will prove r exists by assuming it does not and getting a contradiction. If there is no
such r then we can’t use the numbers 1/n for n = 1, 2, . . . as r, so for each n ≥1 there’s an
xn ∈K such that B(xn, 1/n) is not in each Ui. We have built a sequence {xn} in K, so by
(1) there is a subsequence {xnj} converging to some x ∈K. The point x has to be in some
member of the open covering, say x ∈Ui. Since Ui is open, we have B(x, 1/m) ⊂Ui for
some m ≥1. Since nj →∞and d(xnj, x) →0, for suitably large nj we have both nj > 2m
and d(xnj, x) < 1/(2m). For that nj we have the implication
y ∈B(xnj, 1/nj) =⇒d(y, x) ≤d(y, xnj) + d(xnj, x) < 1
nj
+ 1
2m <
1
2m + 1
2m = 1
m,
so B(xnj, 1/nj) ⊂B(x, 1/m) ⊂Ui, but that is a contradiction since no B(xn, 1/n) lies
inside a member of the open covering. Thus some r exists with the desired property.
Step 3: Every open covering {Ui} of K in X has a ﬁnite subcovering containing K.
Using r as in Step 2, by Step 1 there are x1, . . . , xn ∈K such that K ⊂Sn
k=1 B(xk, r). By
the choice of r, each B(xk, r) is in some Ui, so K is contained in a ﬁnite union of members
of the open covering. This completes the proof that (1) ⇒(2).
(2) =⇒(1): Let {xn} be a sequence in K.
We want to show (2) implies there is a
convergent subsequence, or equivalently the sequence {xn} has a limit point in K. (This
includes the possibility that a point occurs inﬁnitely often in the sequence, making it a
limit of a constant subsequence.) Assume there is no limit point: no point in K is the limit
of a subsequence of {xn}. Then for each y ∈K there must be an ry > 0 such that the
ball B(y, ry) contains only ﬁnitely many terms from {xn}: if every ball centered at y had
inﬁnitely many terms from {xn} in it then we could build a subsequence tending to y by
using radius 1, 1/2, 1/3, . . ..
The balls B(y, ry) for y ∈K are an open covering of K, so by (2) there is a ﬁnite
subcovering: K is contained in a union of ﬁnitely many of these balls. Each of these balls
has only ﬁnitely many terms from {xn} in it, so we’d get that the sequence {xn} has only
ﬁnitely many terms, which is absurd.
□
We call condition (2) in Theorem 6.11 the open covering criterion for compactness. It
leads to a second proof that compact subsets of metric spaces are closed and bounded
(Theorem 6.7).
Compact subsets are closed: (This will be similar to the proof that (2) =⇒(1) above.)
If {xn} is a sequence in K that converges to some x ∈X then we want to show x ∈K.
Every subsequence of {xn} also tends to x, so if x is not in K then every element of K
is contained in an open ball that contains only ﬁnitely many terms of the sequence {xn}.
(If this were not true then some point in K would be the limit of a subsequence, which is
impossible since all subsequences tend to x.) These open balls are an open covering of K,

<!-- page 21 -->
METRIC SPACES
21
so by the open covering criterion for compactness we can extract a ﬁnite subcovering, but
that implies the sequence has only ﬁnitely many terms, a contradiction.
Compact subsets are bounded: One open covering of K is S
x∈K B(x, 1). By the open
covering criterion for compactness there is a ﬁnite subcovering, so K ⊂Sn
k=1 B(xk, 1) for
some ﬁnite set of points x1, . . . , xn in K.
Thus K is in a ﬁnite union of balls, so it is
bounded.
As an application of the open covering formulation of compactness, we show that all
compact subsets of R, no matter how complicated they may be, share a property with
closed bounded intervals: they contain maximum and minimum elements.
Theorem 6.12. For every nonempty compact subset K of R there are a ∈K and b ∈K
such that all x ∈K satisfy a ≤x ≤b.
Proof. Suppose K does not have a maximum element. Then for each x ∈K there is y > x
in K, so x ∈(−∞, y). Thus K ⊂S
y∈K(−∞, y). This open covering of K has a ﬁnite
subcovering, say K ⊂(−∞, y1) ∪· · · ∪(−∞, yn) with yi ∈K. But max(y1, . . . , yn) is in K
and is not in the ﬁnite subcovering, so we have a contradiction. The proof that K has a
minimum element is similar.
□
If we try covering compact sets with subsets slightly diﬀerent from open subsets, there
may not be a ﬁnite subcovering. Consider [0, 1] covered by the intervals [1/(n + 1), 1/n]
together with {0}, or by the intervals [1/2 + 1/2n, 1] for n ≥2 together with [0, 1/2].
7. Connected subsets
A connected subset of a metric space is a subset that is in “one piece.” What does that
mean? It’s easier to say what it means not to be in one piece: the subset can be covered
by two disjoint open sets. For example, two closed discs in the plane that don’t overlap
should not be considered to be one piece. We can surround them by two open discs that
don’t overlap, as shown below.
Deﬁnition 7.1. A subset S of a metric space X is called connected if whenever S ⊂U ∪V
where U and V are disjoint open subsets of X, either S ⊂U or S ⊂V . Equivalently, S is
connected when it’s impossible to have S ⊂U ∪V for disjoint open subsets with S ∩U ̸= ∅
and S ∩V ̸= ∅.
Example 7.2. The empty set and one-point subsets are connected. Verifying other exam-
ples requires work.
To say a metric space X is connected means that writing X = U ∪V with U and V
disjoint open subsets of X requires U or V to be empty. Since U and V are complements
in X, saying U and V are open is the same as saying U is open and closed (or “clopen”),
so X being connected is equivalent to saying there are no subsets of X that are both open
and closed other than ∅and X.

<!-- page 22 -->
22
KEITH CONRAD
Theorem 7.3. Every interval in R is connected.
Proof. Step 1: Bounded open intervals are connected. We will show (0, 1) is connected, but
the same argument works with every open interval (a, b) where a < b in R.
Suppose (0, 1) ⊂U ∪V where U and V are disjoint open subsets of R. Assume (0, 1)∩U
and (0, 1) ∩V are both nonempty. Setting A = (0, 1) ∩U and B = (0, 1) ∩V , both A and
B are open and we have (0, 1) = A ∪B and A ∩B = ∅. Since A and B are nonempty by
assumption, pick a ∈A and b ∈B. Then a ̸= b, so without loss of generality a < b.
Set S = {x ∈A : x < b}, which is nonempty since a ∈S. Since S is bounded above it
has a least upper bound, say ℓ. Then a ≤ℓ≤b, so ℓ∈[a, b] ⊂(0, 1) = A ∪B.
If ℓwere in A, then ℓ̸= b so ℓ< b. Since A is an open set in R, some interval (ℓ−ε, ℓ+ε)
would lie in A. That means all numbers very close to ℓon its right lie in A, but such
numbers (taken close enough to ℓ) are less than b, and that contradicts ℓbeing an upper
bound on S. So ℓ̸∈A.
If ℓwere in B, which is also an open set in R, then some interval around ℓwould lie
entirely in B. However, since ℓis the least upper bound of S there must be elements of S
in every interval of the form (ℓ−δ, ℓ], and S ⊂A, so we have a contradiction. Thus ℓ̸∈B.
Since ℓis in neither A nor B, we have a ﬁnal contradiction, so (0, 1) is connected.
Step 2: Unbounded open intervals are connected. Consider the case of (0, ∞). Suppose
(0, ∞) ⊂U ∪V where U and V are disjoint open subsets of R. The interval contains 1,
and without loss of generality 1 ∈U. For all m > 1 we have (0, m) ⊂(0, ∞) ⊂U ∪V
and (0, m) ∩U ̸= ∅, so by connectedness of (0, m) we get (0, m) ⊂U. Since this holds
for all m > 1, we get (0, ∞) ⊂U. The same argument works for every unbounded open
interval with one endpoint in R. The only open interval left is R = (−∞, ∞). Write it as
(−∞, 2) ∪(0, ∞) and use each part separately (both contain 1) to see R is connected.
Step 3: Other intervals are connected. Let I be a non-open interval and I ⊂U ∪V for
disjoint open U and V in R. Let J be I without its ﬁnite endpoints, so J is an open interval
and thus we know J is connected. Since J ⊂U ∪V , either J ⊂U or J ⊂V . Without
loss of generality, J ⊂U. If an endpoint of I were in V then a small open interval around
that endpoint would be in V (since V is open in R), but this is absurd since each open
interval around an endpoint of I contains elements of J, which are all in U. Therefore ﬁnite
endpoints of I are in U too, so I ⊂U and this proves I is connected.
□
Theorem 7.4. Every nonempty subset of R that is not an interval is not connected.
Proof. Say S ⊂R is not an interval. Then S contains two points a and b, say with a < b,
and does not contain some point c in between them. Let U = (−∞, c) and V = (c, ∞).
Then U and V are disjoint open subsets of R, S ⊂U ∪V , a ∈S ∩U, and b ∈S ∩V .
□
Combining the last two theorems, the nonempty connected subsets of R are precisely the
intervals. There is no simple characterization of connected subsets of Rm for m > 1. In
practice nice subsets of Rm for m > 1 are proved to be connected by proving they have a
stronger, more visually intuitive, property called being path-connected.
Deﬁnition 7.5. A subset S of a metric space X is called path-connected if, for every pair
of points s and s′ in S, there is a continuous function p: [0, 1] →X such that p(t) ∈S for
all t, p(0) = s, and p(1) = s′.
We call such a function p a path from s to s′. Since q(t) = p(1 −t) is also continuous
with q(0) = p(1) = s′ and q(1) = p(0) = s, we can think of a path going in either direction,
from s to s′ or from s′ to s.

<!-- page 23 -->
METRIC SPACES
23
The picture to have of a path-connected space is the inside of the blob below, where every
pair of points can be linked by a path.
Theorem 7.6. Every path-connected subset of a metric space is connected.
Proving Theorem 7.6 requires information about continuous functions on metric spaces,
the topic of Section 8, so we defer the proof until then (see after Example 8.12). Using
Theorem 7.6 we can “see” right away that nice regions in R2, R3, or Rm for m > 3 are
connected because a path can be drawn within the region between every two of its points.
For example, the surface of a sphere or a solid ball in R3 are path-connected and thus are
connected. Theorem 7.6 does not imply [0, 1] is connected by being path connected since
the proof of Theorem 7.6 uses the connectedness of [0, 1]!
The converse of Theorem 7.6 is false: connectedness does not imply path-connectedness.
An example is the “inﬁnite broom” pictured below: it is the union of the closed line segments
Ln from (0, 0) to (1, 1/n) as n runs over positive integers together with the (red) point (1, 0).
The x-axis strictly between (0, 0) and (1, 0) is not part of the set. This is connected, but
there is no path from (1, 0) to another point of the set. See [2] for a proof.
(0,0)
(1,1)
(1,1/2)
(1,1/3)
(1,1/4)
(1,0)
There is an important partial converse to Theorem 7.6: for open subsets of Rm, being
connected implies being path connected. The proof is omitted.
The concept most unlike being connected is being totally disconnected. A subset of a
metric space is called totally disconnected if its only nonempty connected subsets are one-
element subsets (a point is always connected). Examples of totally disconnected subsets of
the metric space R include Z, Q, and fractals like the Cantor set. The p-adic integers and
p-adic numbers, for a prime p, are important totally disconnected metric spaces in number
theory. In Rm for m > 1 all open and closed balls are connected, which is a nice analogy

<!-- page 24 -->
24
KEITH CONRAD
with the one-dimensional case, but in a totally disconnected metric space no open or closed
balls are connected (aside from closed balls of radius 0, i.e., points).
8. Continuous functions between metric spaces
Up until now the only limits we have discussed in metric spaces were limits of sequences.
Now we turn to limiting values of functions deﬁned on a metric space, and speciﬁcally con-
tinuous functions on a metric space. This is where we will see the importance of connected
sets and compact sets.
Speciﬁcally, we want to prove the following two properties of continuous functions.
Theorem 8.1 (Intermediate Value Theorem). Let I be an interval and f : I →R be
continuous. If a < b in I and f(a) ̸= f(b) then for every y strictly between f(a) and f(b)
there is c ∈(a, b) such that f(c) = y.
Theorem 8.2 (Extreme Value Theorem). Every continuous real-valued function on a closed
bounded interval has maximum and minimum values: if f : [a, b] →R is continuous on a
closed bounded interval then there are m and M such that (i) m ≤f(x) ≤M for all x in
[a, b] and (ii) m and M are values of f(x).
The Extreme Value Theorem justiﬁes the deﬁnition of the metric d∞on C[0, 1] back in
Section 2 as a maximum value of a continuous function on [0, 1]. In contrast to the Extreme
Value Theorem, a continuous bounded function on an open interval doesn’t have to have
a maximum value, such as 1/x on (1, 2). Its values are bounded above by 1, but no value
of the function is greater than all other values. The diﬀerence between closed bounded
intervals and open intervals is that closed bounded intervals are compact, and we’ll see that
is what makes the Extreme Value Theorem work.
Before we prove theorems about continuous functions we have to deﬁne continuous func-
tions. The deﬁnition of continuity for a real-valued function on an interval, usually called the
(ε, δ)-deﬁnition, goes as follows. For a real number a and a real-valued function f(x) deﬁned
on an interval containing a, we say f(x) is continuous at a and write limx→a f(x) = f(a) if
for every ε > 0 there is a δ = δa,ε > 0 such that
|x −a| < δ =⇒|f(x) −f(a)| < ε.
If we have a real-valued function f : Rm →R, and a ∈Rm, then we say f(x) is continuous
at a and write limx→a f(x) = f(a) if for every ε > 0 there is a δ = δa,ε > 0 such that
||x −a|| < δ =⇒|f(x) −f(a)| < ε.
Notice the diﬀerent distances being used here, one on Rm (where the function is deﬁned)
and one on R (where the function takes its values).
Deﬁnition 8.3. A function f : X →Y between two metric spaces is called continuous at
a ∈X if for every ε > 0 there is a δ = δa,ε > 0 such that
dX(x, a) < δ =⇒dY (f(x), f(a)) < ε.
If f is continuous at each point of X then we say f is continuous on X.
As a warm-up, let’s show every metric is a continuous function on its metric space when
we view it as a function of one of its variables, keeping the other one ﬁxed.
Theorem 8.4. For a metric space (X, d) and point c ∈X, the function fc : X →R that is
“distance to c”, namely fc(x) = d(c, x), is continuous.

<!-- page 25 -->
METRIC SPACES
25
Proof. Pick a ∈X and ε > 0. We need a δ > 0 such that
d(x, a) < δ =⇒|fc(x) −fc(a)| < ε.
The inequality on the right says |d(c, x) −d(c, a)| < ε.
Using the triangle inequality in two ways,
d(c, a) ≤d(c, x) + d(x, a)
and
d(c, x) ≤d(c, a) + d(a, x),
so
d(c, a) −d(c, x) ≤d(x, a)
and
d(c, x) −d(c, a) ≤d(a, x).
Thus |d(c, x) −d(c, a)| ≤d(x, a). Therefore
d(x, a) < ε =⇒|d(c, x) −d(c, a)| ≤d(x, a) < ε
so we can use δ = ε.
□
Remark 8.5. By a two-way triangle inequality argument like the one used in this proof
(but not using anything like a choice of c), show
|d(x, y) −d(xn, yn)| ≤d(x, xn) + d(y, yn)
for xn, x, yn, y ∈X. Therefore if xn →x and yn →y in X then this inequality shows
d(xn, yn) →d(x, y), an intuitively reasonable property.
Theorem 8.6. For a metric space (X, d), the identity function X →X where x 7→x is
continuous.
Proof. This is straightforward, using δ = ε.
□
Theorem 8.7. Addition and multiplication, as functions R2 →R given by A(x, y) = x+y
and M(x, y) = xy, are both continuous.
Proof. First we prove continuity of addition. Pick (a, b) ∈R2 and ε > 0. We need δ > 0
such that
||(x, y) −(a, b)|| < δ =⇒|A(x, y) −A(a, b)| < ε.
We will use δ = ε/2.
If ||(x, y) −(a, b)|| < ε/2 then
p
(x −a)2 + (y −b)2 < ε/2, so |x −a| < ε/2 and |y −b| <
ε/2. Then
|A(x, y) −A(a, b)| = |(x + y) −(a + b)| ≤|x −a| + |y −b| < ε
2 + ε
2 = ε.
To prove multiplication is continuous we estimate |M(x, y) −M(a, b)| = |xy −ab|:
|xy −ab| = |(x −a)y + (y −b)a|
= |(x −a)(y −b) + (x −a)b + (y −b)a|
≤|x −a||y −b| + |x −a|b + |y −b|a.
Thus if |x −a| < δ and |y −b| < δ, then |xy −ab| < δ2 + δb + δa = δ(δ + b + a). If
(8.1)
δ ≤1
and
δ ≤
ε
1 + a + b
then δ(δ + b + a) ≤δ(1 + b + a) ≤ε. So pick δ = min(1, ε/(1 + a + b)) to make δ satisfy the
two inequalities in (8.1). Then
||(x, y) −(a, b)|| < δ =⇒|x −a|, |y −b| < δ
and our calculations above imply |xy −ab| < ε.
□

<!-- page 26 -->
26
KEITH CONRAD
In this proof notice that for continuity of multiplication our choice of δ depends not only
on ε, but also on the point (a, b) where we are checking continuity. This is typical: in
practice the choice for δ may depend on the point at which we are proving continuity. (In
the deﬁnition of continuity at a, we wrote δ = δa,ε.) This did not happen for addition,
where δ = ε/2 everywhere. Such “independence of the point” is special; it will lead later to
the concept of uniform continuity.
Theorem 8.8. A composition of continuous functions on metric spaces is continuous: if
f : X →Y and g: Y →Z are continuous then the composite function g ◦f : X →Z is
continuous.
Proof. Pick a ∈X and ε > 0. We have (g ◦f)(a) = g(f(a)). By the deﬁnition of continuity
of g at f(a), there’s an η > 0 (depending on f(a) and ε) such that
(8.2)
dY (y, f(a)) < η =⇒dZ(g(y), g(f(a))) < ε.
By the deﬁnition of continuity of f at a, there’s a δ > 0 (depending on η and a) such that
dX(x, a) < δ =⇒dY (f(x), f(a)) < η,
and by (8.2) that last inequality implies dZ(g(f(x)), g(f(a))) < ε.
□
Just as compactness has a formulation in terms of open sets rather than sequences (The-
orem 6.11), using open coverings, continuity of a function on a metric space also has a
formulation in terms of open sets rather than ε’s and δ’s. More precisely, continuity of a
function can be expressed in terms of inverse images of open sets. For a function f : X →Y
and a subset S ⊂Y , the inverse image f−1(S) means {x ∈X : f(x) ∈S}. An inverse image
of a function on a subset makes sense even if the function is not invertible. For example, if
f : R →R by f(x) = x2 then
f−1((0, 1)) = (−1, 0) ∪(0, 1)
f−1((−2, 2)) = (−
√
2,
√
2),
f−1((1, 2)) = (−
√
2, −1) ∪(1,
√
2),
f−1((−1, 0)) = ∅.
Inverse images of subsets under a function behave well for all set-theoretic operations: if
f : X →Y is a function then for subsets S and T in Y ,
f−1(S ∩T) = f−1(S) ∩f−1(T),
f−1(S ∪T) = f−1(S) ∪f−1(T),
S ⊂T =⇒f−1(S) ⊂f−1(T),
f−1(S −T) = f−1(S) −f−1(T),
where S −T = {s ∈S : s ̸∈T}.
(For example, if S = {0, 1} and T = {1, 2} then
S −T = {0}.)
We will use these properties without comment below.10
In particular,
f−1(Y −S) = X −f−1(S), so inverse images send complements to complements.
Theorem 8.9. A function f : X →Y between two metric spaces is continuous if and only
if the inverse image of every open set in Y is open in X: for all open U in Y , the set
f−1(U) = {x ∈X : f(x) ∈U} is open in X.
Proof. First suppose f ﬁts the (ε, δ)-deﬁnition of continuity on X, so f is continuous at
each element of X. For every open set U ⊂Y we want to show f−1(U) is open in X.
If f−1(U) = ∅then f−1(U) is open by our convention that the empty set is open, so
suppose f−1(U) ̸= ∅.
Pick a ∈f−1(U), so f(a) ∈U.
Since U is open in Y there’s
10Analogous formulas for images of subsets are true for unions and containments but false for intersections
and complements: use f(x) = x2 with A = {1, 2} and B = {1, −2} to see f(A ∩B) ̸= f(A) ∩f(B) and
f(A −B) ̸= f(A) −f(B).

<!-- page 27 -->
METRIC SPACES
27
some ε > 0 such that B(f(a), ε) ⊂U. By the (ε, δ)-deﬁnition of continuity at a, there
is a δ > 0 such that dX(x, a) < δ =⇒dY (f(x), f(a)) < ε.
This implication is saying
f(B(a, δ)) ⊂B(f(a), ε), so B(a, δ) ⊂f−1(B(f(a), ε)) ⊂f−1(U). This shows each a in
f−1(U) is contained in an open ball that’s contained in f−1(U), so f−1(U) is open in X.
Now we prove the converse. Suppose for all U open in Y we have f−1(U) open in X. For
every a ∈X we will prove f is continuous at a. For each ε > 0, the open ball B(f(a), ε) in
Y is open, so using B(f(a), ε) as U the inverse image f−1(B(f(a), ε)) is open in X and this
inverse image includes a. Thus there’s a δ > 0 such that B(a, δ) ⊂f−1(B(f(a), ε)), and
unwinding the notation this containment is saying that if dX(a, x) < δ then dY (f(a), f(x)) <
ε. That is exactly the (ε, δ)-deﬁnition of continuity of f at a.
□
It is false that continuous functions always send open sets to open sets. For example, the
squaring function R →R sends (−1, 1) to [0, 1). Continuity aligns with inverse images of
open sets, not images of open sets. C’est la vie.
Remark 8.10. Theorem 8.9 is an open-set formulation of continuity on a whole set, not
at a particular point. There is an open-set formulation of continuity at a point: f : X →Y
is continuous at a if and only if for all open U ⊂Y containing f(a) there is an open V ⊂X
containing a such that f(V ) ⊂U. Checking this matches the (ε, δ)-deﬁnition of continuity
at a is left to the reader: see Exercise 13.
Corollary 8.11. A function f : X →Y between two metric spaces is continuous if and
only if the inverse image of every closed set in Y is closed in X.
Proof. Theorem 5.17 tells us that open and closed subsets are complementary to each other.
For a closed subset C of Y , U = Y −C is open and f−1(U) = f−1(Y −C) = X −f−1(C).
Therefore f−1(C) is closed if and only if f−1(U) is open, so Theorem 8.9 tells us continuity
of f is equivalent to f−1 sending closed subsets to closed subsets.
□
Example 8.12. In R3, the sphere S2 = {(x, y, z) ∈R3 : x2 + y2 + z2 = 1} is closed. This
can be proved directly with sequences in S2 or by noting that f(x, y, z) = x2 + y2 + z2 is a
continuous function R3 →R, S2 = f−1(1), and {1} is closed in R.
To illustrate the open-set formulation of continuity of a function, we now prove Theorem
7.6: path-connected sets are connected. The proof will use connectedness of [0, 1].
Proof. Let S be a path-connected subset of a metric space X. We will use paths in S to
show that if S is not connected then [0, 1] is not connected, which is a contradiction, so S
is connected.
Suppose S is not connected, so we have S ⊂U ∪V where U and V are nonempty disjoint
open subsets of X. Pick s ∈S ∩U and s′ ∈S ∩V . There is a path p: [0, 1] →S where
p(0) = s and p(1) = s′. The partition of S into S ∩U and S ∩V leads via this path to a
partition of [0, 1]: [0, 1] = p−1(U) ∪p−1(V ). Set A = p−1(U) and B = p−1(V ). Both are
open subsets of [0, 1] since p is continuous.11
Note 0 ∈A and 1 ∈B, so A and B are nonempty. Obviously A and B are disjoint, since
no point in [0, 1] can have its p-value in both U and V . Thus the equation [0, 1] = A ∪B
exhibits [0, 1] as a disjoint union of two nonempty open subsets of [0, 1], which contradicts
the connectedness of [0, 1].
□
11In [0, 1], intervals of the form [0, ε) are open! This is the ball B(0, ε) in the metric space [0, 1], even though
the same interval is not open in R.

<!-- page 28 -->
28
KEITH CONRAD
Next we reprove Theorem 8.8 using open sets instead of ε’s and δ’s.
Proof. Let U be an arbitrary open set in Z. Then
(g ◦f)−1(U) = {x ∈X : (g ◦f)(x) ∈U}
= {x ∈X : g(f(x)) ∈U}
= {x ∈X : f(x) ∈g−1(U)}
= f−1(g−1(U)).
By continuity of g, g−1(U) is open in Y , and by continuity of f, f−1(g−1(U)) is open in X.
Thus g ◦f is continuous.
□
Think about why this proof of Theorem 8.8 and the ﬁrst proof of Theorem 8.8 really are
the same argument even though at ﬁrst glance they might look diﬀerent. Mathematicians
consider the second proof, using open sets, to be more elegant.
As a substantial application of continuity being preserved under composition, we will
prove polynomials with real coeﬃcients are continuous. We’ll need one lemma.
Lemma 8.13. Let f : R →R and g: R →R. If f and g are continuous then the function
R →R2 given by x 7→(f(x), g(x)) is continuous.
Proof. Set F : R →R2 by F(x) = (f(x), g(x)) and let U be an open set in R2. To prove
F −1(U) is open in R, we may assume F −1(U) ̸= ∅. Let a ∈F −1(U), so (f(a), g(a)) ∈U.
Around each point in U there is a small square, not just a small disc, centered at the
point and contained in U. See the picture below.
Thus for some suitably small ε > 0 we have (f(a)−ε, f(a)+ε)×(g(a)−ε, g(a)+ε) ⊂U.
By continuity of f and g, Vf = f−1((f(a) −ε, f(a) + ε)) and Vg = g−1((g(a) −ε, g(a) + ε))
are open in R and a ∈Vf ∩Vg ⊂F −1(U). Since Vf ∩Vg is open, it contains an interval
around a. Thus F −1(U) is open in R.
□
The converse to Lemma 8.13 is true as well: see Exercise 22.
Theorem 8.14. Every polynomial function in one variable with real coeﬃcients is a con-
tinuous function R →R.
Proof. We will use Theorem 8.8 to get continuity of all polynomials from that of constant
functions, f(x) = x, and addition and multiplication on R. In particular, no ε’s or δ’s or
open sets will appear. They were used in previous results that we will invoke.
First we prove by induction that xn is continuous for each positive integer n. When n = 1
this is the identity function (Theorem 8.6). For n ≥2 assume by induction that xn−1 is
continuous. We can think of the function xn as the composite R →R2 →R where the
ﬁrst function is x 7→(x, xn−1) and the second function is multiplication (x, y) 7→xy: their

<!-- page 29 -->
METRIC SPACES
29
composite is x 7→(x, xn−1) 7→xxn−1 = xn. The ﬁrst function is continuous by Lemma 8.13
and the second function is continuous by Theorem 8.7, so their composite is continuous.
Since xn is continuous, a general monomial cxn for c ∈R can be regarded as a composite
function R →R2 →R where the ﬁrst function is x 7→(c, xn) and the second function is
multiplication (x, y) 7→xy. The ﬁrst function is continuous by Lemma 8.13 since constant
functions12 and power functions are continuous.
The second function is continuous by
Theorem 8.7, so their composite is continuous.
Polynomials are ﬁnite sums of monomials, and we will prove they are continuous by
induction on the number of monomials in the polynomial. The base case of monomials was
proved above. A sum of two monomials, axm + bxn, is a composite function R →R2 →R
where the ﬁrst function is x 7→(axm, bxn) and the second function is addition (x, y) 7→x+y.
Both of these functions are continuous by the base case, Lemma 8.13, and Theorem 8.7, so
their composite is continuous. The general inductive step is left to the reader.
□
Theorem 8.15. For continuous f : X →Y and S compact in X, f(S) is compact in Y .
Proof. We will give two proofs, one using the convergent subsequence description of com-
pactness and the other using the open covering description of compactness.
First proof: Let {yn} be a sequence in f(S), so we can write yn = f(xn) for some
xn ∈S. By compactness of S, the sequence {xn} in S has a convergent subsequence, say
xni →x ∈S. Then by continuity, f(xni) →f(x), so yni →f(x) ∈f(S). We proved every
sequence in f(S) has a convergent subsequence, so f(S) is compact.
Second proof: Let {Ui} be an open covering of f(S), so f(S) ⊂S
i∈I Ui in Y . Then
S ⊂S
i∈I f−1(Ui), and each f−1(Ui) is open in X, so {f−1(Ui)} is an open covering of S
in X. By compactness of S there is a ﬁnite subcovering, say S ⊂f−1(U1) ∪· · · ∪f−1(Un).
Then f(S) ⊂U1 ∪· · · ∪Un, so every open covering of f(S) has a ﬁnite subcovering.
□
Unlike images, the inverse image of a compact set under a continuous function need not
be compact, e.g., f : R →R by f(x) = 1/(x2 + 1) is continuous and f−1([0, 1]) = R.
Theorem 8.16. For continuous f : X →Y and S connected in X, f(S) is connected in Y .
Proof. Suppose f(S) ⊂U ∪V where U and V are disjoint open subsets of Y .
Then
S ⊂f−1(U ∪V ) = f−1(U) ∪f−1(V ). The inverse images f−1(U) and f−1(V ) are open
in X, and they are disjoint since U and V are disjoint (if a ∈f−1(U) ∩f−1(V ) then
f(a) ∈U ∩V = ∅, a contradiction). Since S is connected, we have either S ⊂f−1(U) or
S ⊂f−1(V ), so f(S) ⊂U or f(S) ⊂V . Thus f(S) is connected.
□
Using Theorems 8.15 and 8.16 and our knowledge of connected and compact subsets of
R, we now prove the Intermediate and Extreme Value Theorems (Theorems 8.1 and 8.2).
Proof. (Intermediate Value Theorem) Let I be an interval and f : I →R be continuous.
Suppose a < b in I with f(a) ̸= f(b). The image f([a, b]) is connected in R by Theorem
8.16, so it must be an interval. An interval containing f(a) and f(b) contains all numbers
between them, so every y strictly between f(a) and f(b) is f(c) for some c ∈[a, b] ⊂I, and
c is not a or b since y is not f(a) or f(b).
□
Proof. (Extreme Value Theorem) Let f : [a, b] →R be continuous. Since [a, b] is compact
and connected, so is f([a, b]) by Theorems 8.15 and 8.16.
Connected subsets of R are
12Continuity of constant functions is easy to check.

<!-- page 30 -->
30
KEITH CONRAD
intervals, and compact intervals are closed and bounded, so f([a, b]) = [m, M] where m, M ∈
R. The conclusions of the Extreme Value Theorem follow from this.
□
Theorem 8.17. If X is a compact metric space and f : X →R is a continuous function
with positive values everywhere then there is some c > 0 such that f(x) ≥c for all x ∈X,
and we can take c = f(x0) for some x0 ∈X.
Proof. The image f(X) is compact in R by Theorem 8.15, so Theorem 6.12 implies there
is an x0 ∈X such that f(x) ≥f(x0) for all x ∈X. Set c = f(x0) > 0.
□
Positive continuous functions on non-compact spaces need not have a positive lower
bound. Consider 1/x as a function (0, ∞) →R. There is no c > 0 such that 1/x ≥c > 0
for all x > 0.
Corollary 8.18. If K is a compact subset of the metric space X then for each x ∈X the
distance from x to the elements of K has a minimum: there is some y0 ∈K such that
d(x, y) ≥d(x, y0) for all y ∈K.
Proof. Let f : K →R by f(y) = d(x, y). This is continuous by Theorem 8.4 so its image
f(K) is compact in R. By Theorem 6.12 (with K in that theorem being f(K) here) some
value d(x, y0) for y0 ∈K is a minimum value of f.
□
We now turn to the ﬁnal topic about continuous functions that we’ll discuss. It is an
important reﬁnement of continuity.
Deﬁnition 8.19. A function f : X →Y between two metric spaces is called uniformly
continuous if for every ε > 0 there is a δ = δε > 0 such that for all a ∈X,
dX(x, a) < δ =⇒dY (f(x), f(a)) < ε.
Uniform continuity is a special kind of continuity. It says δ can be chosen just in terms of
ε, independently of the point a (so we can choose δ “uniformly in a,” hence the name). See
the graphs of y = x2 and y = 2x below. For each we use ε = .75 and show in red the largest δ-
intervals around a = 1 and a = 2 on the x-axis that make |x−a| < δ =⇒|f(x)−f(a)| < .75.
For f(x) = x2 we need a shorter interval around a = 2 to keep the f-values within .75 of
f(2) than we need around a = 1 to keep f-values within .75 of f(1), but for f(x) = 2x
intervals of the same radius around 1 and 2 lead to intervals of the same radius around f(1)
and f(2). On R, linear functions are uniformly continuous while x2 is not.
x
y
2
4
y = x2
1
1
x
y
1
2
2
4
y = 2x

<!-- page 31 -->
METRIC SPACES
31
It is instructive to compare the deﬁnitions of continuity and uniform continuity using
quantiﬁer notation. Continuity of a function f : X →Y says
∀a ∈X ∀ε > 0 ∃δ > 0 s.t. ∀x ∈X, dX(x, a) < δ =⇒dY (f(x), f(a)) < ε.
while uniform continuity of a function f : X →Y says
∀ε > 0 ∃δ > 0 s.t. ∀a ∈X ∀x ∈X, dX(x, a) < δ =⇒dY (f(x), f(a)) < ε.
The only diﬀerence is where “∀a ∈X” appears: in continuity it is at the start while in
uniform continuity it is after δ. The order of quantiﬁers has a substantial impact on what
something means. A simpler example: it’s true that ∀x ∈R s.t. x > 0 ∃y ∈R s.t. y2 = x
(every positive real number has a real square root), but it’s false that ∃y ∈R s.t. ∀x ∈R s.t.
x > 0, y2 = x (there’s a universal square root of all positive numbers?). Deﬁnitions in real
analysis have many nested quantiﬁers, so it’s understandable why even a mathematician of
the stature of Cauchy, who introduced the (ε, δ)-deﬁnition13 of continuity, confused it with
uniform continuity in proofs.
Unlike continuity, uniform continuity can’t be described as a property at individual points
of the domain (why?). Also unlike continuity, there no way to convert uniform continuity
into a statement about general open subsets.14 Proofs about uniform continuity use (ε, δ)-
language.
The last general comment we have about uniform continuity is that in its deﬁnition a
and x play symmetric roles (they are quantiﬁed at the same time, unlike in the deﬁnition
of continuity), so we can express uniform continuity in a way that puts a and x on an equal
footing, which we therefore will write as x and x′. A function f : X →Y is called uniformly
continuous if for every ε > 0 there is a δ = δε > 0 such that for all x, x′ ∈X,
dX(x, x′) < δ =⇒dY (f(x), f(x′)) < ε.
This is the formulation of uniform continuity that we will use below. (Note: we are not
saying all x and x′ satisfy dX(x, x′) < δ, but rather that they satisfy the total implication
written above: if dX(x, x′) < δ then dY (f(x), f(x′)) < ε.)
Example 8.20. We saw before that x2 is not uniformly continuous on R, since for a given
ε the function values stay within ε of each other at larger numbers that are within δ of
each other only if δ is made progressively smaller. We can’t use the same δ as the points
get too big. But if we restrict ourselves to a bounded domain then x2 becomes uniformly
continuous. For instance, on the interval [−b, b] where b > 0,
|x −x′| < δ =⇒|x2 −x′2| = |x −x′||x + x′| < δ(|x| + |x′|) ≤δ(2b),
so to make |x2 −x′2| < ε when |x −x′| < δ in [−b, b] we can use δ = ε/(2b).
Example 8.21. For a > 0 the function 1/x on [a, ∞) is uniformly continuous:
|x −x′| < δ =⇒

1
x −1
x′
 = |x′ −x|
|x||x′| < δ
a2 ,
so we can make |1/x −1/x′| < ε if |x −x′| < δ in [a, ∞) using δ = a2ε.
Example 8.22. For a metric space (X, d) and c ∈X, the function fc(x) = d(c, x) is
uniformly continuous on X. This comes from the proof of Theorem 8.4, where we could use
δ = ε independently of the point x at which we were checking continuity of fc.
13Bolzano had developed similar ideas earlier, but his work was not widely read until after Cauchy.
14A partial translation into open sets is possible, but the family of all balls of a common radius has to be
given a special status, called a “uniformity”. We don’t get into that here.

<!-- page 32 -->
32
KEITH CONRAD
Here is the fundamental property that gives rise to uniformly continuous functions.
Theorem 8.23. A continuous function f : X →Y from a compact metric space to a metric
space is uniformly continuous.
This doesn’t say continuous functions can’t be uniformly continuous on non-compact
metric spaces (see Example 8.21), only that they must be uniformly continuous on compact
metric spaces.
Proof. We prove the theorem in two ways, using the subsequence description of compactness
and using the open covering description of compactness.
First proof (using subsequences): Our argument will be by contradiction, starting with
the assumption that f is not uniformly continuous. Figuring out what it means not to be
uniformly continuous is going to take up the bulk of the proof!
One way to say f is not uniformly continuous is to say it is not true that for every ε > 0
there is a δ > 0 such that all x and x′ in X satisfy dX(x, x′) < δ =⇒dY (f(x), f(x′)) < ε.
But this is not really progress; adding “It is not true that” to the start of a sentence in
order to negate it doesn’t usually let us understand the meaning of the negation.
The negation of a statement of the form “for every ε > 0 there is a δ > 0 such that
something happens” is “there is an ε > 0 such that for all δ > 0 the thing does not
happen.” Using quantiﬁer notation, for a proposition P the negation of
∀ε > 0 ∃δ > 0 s.t. P
is
∃ε > 0 s.t. ∀δ > 0 ∼P,
where ∼P is the negation of P. Negating turns ∀into ∃and vice versa.
For us, P is “all x and x′ in X satisfy dX(x, x′) < δ =⇒dY (f(x), f(x′)) < ε.” Its negation
is “some x and x′ in X satisfy dX(x, x′) < δ and dY (f(x), f(x′)) ≥ε”. (Observe “< ε”
turned into “≥ε” at the end, as a negation.) Putting everything together, the negation of
f being uniformly continuous says:
There is ε>0 s.t. for all δ>0, an x and x′ in X satisfy dX(x, x′)<δ & dY (f(x), f(x′))≥ε.
The numbers x and x′ here may depend on δ (each δ needs an example of x and x′).
Now that we can express what it means not to be uniformly continuous, assume f is not
uniformly continuous. For the special ε that occurs, use δ = 1/n with n = 1, 2, 3, . . .: for
each n there are xn and x′
n in X such that dX(xn, x′
n) < 1/n and dY (f(xn), f(x′
n)) ≥ε. We
have built two sequences in X: {xn} and {x′
n}. By compactness of X, some subsequence
{xni} of {xn} converges in X, say to x. Also x′
ni →x by Theorem 3.8. By continuity
of f, f(xni) →f(x) and f(x′
ni) →f(x), so dY (f(xni), f(x′
ni)) →0. This contradicts the
inequality dY (f(xn), f(x′
n)) ≥ε for all n, so we’re done.
Second proof (using open coverings): This proof will not be by contradiction. Pick ε > 0.
For each x ∈X, continuity of f at x implies there is some δx > 0 such that
(8.3)
dX(x, x′) < δx =⇒dY (f(x), f(x′)) < ε
2.
The balls B(x, δx) are an open covering of X, so by compactness there is a ﬁnite subcovering,
say by B(x1, δx1), . . . , B(xn, δxn). Set δ = min(δx1/2, . . . , δxn/2) > 0.

<!-- page 33 -->
METRIC SPACES
33
Pick x and x′ in X with dX(x, x′) < δ. We have x ∈B(xi, δxi/2) for some i = 1, . . . , n.
Then dX(x, xi) < δxi/2 < δxi, so dY (f(x), f(xi)) < ε/2 by (8.3). Also
dX(x′, xi) ≤dX(x′, x) + dX(x, xi) < δ + δxi
2 ≤δxi
2 + δxi
2 = δxi,
so dY (f(x′), f(xi)) < ε/2 by (8.3). Thus
dY (f(x), f(x′)) ≤dY (f(x), f(xi)) + dY (f(xi), f(x′)) < ε
2 + ε
2 = ε.
□
To illustrate the better control that is built into uniform continuity compared to conti-
nuity, we will prove uniformly continuous functions can be extended from dense subsets to
the whole space. This uses the following lemma about a property of uniformly continuous
functions that is not generally true for continuous functions.
Lemma 8.24. If f : X →Y is uniformly continuous and {xn} is a Cauchy sequence in X
then {f(xn)} is a Cauchy sequence in Y .
Proof. Pick ε > 0. By uniform continuity there is a δ > 0 such that for all x and x′ in
X satisfying dX(x, x′) < δ we have dY (f(x), f(x′)) < ε. Since {xn} is Cauchy in X, using
the value of δ there is an N ≥1 such that m, n ≥N =⇒dX(xm, xn) < δ. Then uniform
continuity implies dY (f(xm), f(xn)) < ε for m, n ≥N, so {f(xn)} is Cauchy in Y .
□
In contrast to this, a continuous function might not send Cauchy sequences to Cauchy
sequences: 1/x maps (0, ∞) →R and {1/n} is Cauchy in (0, ∞) but {1/(1/n)} = {n} is not
Cauchy in R. There is nothing strange about this: continuous functions, by deﬁnition, send
convergent sequences to convergent sequences, not Cauchy sequences to Cauchy sequences.
In an incomplete metric space, such as (0, ∞), Cauchy sequences need not be convergent.
Theorem 8.25. Let X and Y be metric spaces, with Y complete. For a dense subset D
of X, every uniformly continuous function f : D →Y uniquely extends to a continuous
function ef : X →Y , deﬁned by ef(x) = limn→∞f(xn), where {xn} is an arbitrary sequence
in D that converges to x. Moreover, ef is uniformly continuous.
Proof. If f has some extension to a continuous function ef on X then for each x ∈X, ef(x)
has to equal limn→∞f(xn) where {xn} is a sequence in D that converges to x (such a
sequence in D exists for each x since D is dense in X). Therefore ef on X is determined
by f on D, so the uniqueness of a (uniformly) continuous extension of f from D to X is
immediate. What we have to address is the existence of such an extension:
(1) For x ∈X, if xn →x where all xn are in D, then why does the sequence {f(xn)}
converge in Y ?
(2) For x ∈X, if xn →x and x′
n →x where all xn and x′
n are in D, then why does
limn→∞f(xn) = limn→∞f(x′
n) in Y ?
(3) Why does the function ef : X →Y deﬁned by ef(x) = limn→∞f(xn), if xn →x in
D, equal f on D and why is ef uniformly continuous?
Proof of (1). For x ∈X, let {xn} be a sequence in D such that xn →x. Then {xn} is a
Cauchy sequence in D. By Lemma 8.24 for the uniformly continuous function f : D →Y ,
{f(xn)} is a Cauchy sequence in Y , so this sequence has a limit since Y is complete.
Proof of (2). If {xn} and {x′
n} are two sequences in D that both tend to x, why do the
convergent sequences {f(xn)} and {f(x′
n)} in Y have the same limit? It suﬃces to show

<!-- page 34 -->
34
KEITH CONRAD
dY (f(xn), f(x′
n)) →0 (Theorem 3.8). That is, for every ε > 0 we want an N such that
n ≥N =⇒dY (f(xn), f(x′
n)) < ε.
From uniform continuity of f on D, for each ε > 0 there is a δ > 0 such that for all
a and b in D, dX(a, b) < δ =⇒dY (f(a), f(b)) < ε. Since xn →x and x′
n →x we have
dX(xn, x′
n) →0, so there’s some N such that n ≥N =⇒dX(xn, x′
n) < δ.
Therefore
n ≥N =⇒dY (f(xn), f(x′
n)) < ε, which is what we wanted.
Proof of (3). By (1) and (2), the deﬁnition
ef(x) := lim
n→∞f(xn) ∈Y
for x ∈X and a sequence {xn} in D with xn →x is independent of the choice of {xn}, so
ef is a genuine function from X to Y . In particular, if x ∈D then using xn = x for all n
shows ef(x) = limn→∞f(xn) = limn→∞f(x) = f(x), so ef restricts on D to f.
It remains to show ef is uniformly continuous. This will be an ε/3 argument.
By uniform continuity of f on D, for every ε > 0 there is δ > 0 such that
(8.4)
dX(a, b) < δ in D =⇒dY (f(a), f(b)) < ε
3.
Suppose x and x′ in X satisfy dX(x, x′) < δ. There are sequences {xn} and {x′
n} in D such
that xn →x and x′
n →x′. Then
dY ( ef(x), ef(x′))
≤
dY ( ef(x), ef(xn)) + dY ( ef(xn), ef(x′
n)) + dY ( ef(x′
n), ef(x′))
=
dY ( ef(x), f(xn)) + dY (f(xn), f(x′
n)) + dY (f(x′
n), ef(x′)).
(8.5)
Since, by deﬁnition, ef(x) is the limit of {f(xn)} and ef(x′) is the limit of {f(x′
n)}, for
large enough n both dY ( ef(x), f(xn)) and dY (f(x′
n), ef(x′)) are less than ε/3. Also for large
enough n, dX(xn, x′
n) < δ since xn and x′
n both tend to x, so dY (f(xn), f(x′
n)) < ε/3 for
large enough n by (8.4). Plugging this all into the inequality (8.5), for large enough n
dY ( ef(x), ef(x′)) ≤dY ( ef(x), f(xn)) + dY (f(xn), f(x′
n)) + dY (f(x′
n), ef(x′))
< ε
3 + ε
3 + ε
3
= ε.
□
Example 8.26. While 1/x is a uniformly continuous function [1, ∞) →R (Example 8.21
with a = 1), it is not a uniformly continuous function (0, 1] →R: if it were, then it would
extend continuously to [0, 1] →R by Theorem 8.25, but it does not.
The reader should show 1/x is not uniformly continuous on (0, 1] directly from the deﬁ-
nition of uniform continuity, without needing a result like Theorem 8.25. Use the negation
of uniform continuity from the proof of Theorem 8.23.
Example 8.27. On Q∩[1, 2], the function f(x) = 1/(x2−2) is continuous but not uniformly
continuous: if it were uniformly continuous then the function would extend to a continuous
function on [1, 2], which is clearly false due to a problem at x =
√
2.
Example 8.28. As a positive application of Theorem 8.23, for each a > 1 we use the
theorem to construct15 ax for irrational x > 0 from the case of rational x ≥0 and show ax
is continuous in x. To use Theorem 8.23 we restrict attention to bounded intervals of x.
15All we do could be adapted to 0 < a < 1, but we stick to a > 1 to keep the notation simple.

<!-- page 35 -->
METRIC SPACES
35
We will take for granted as background the existence of positive rational powers. For
each r ∈Q with r > 0, written as the ratio of positive integers m/n, the number ar = am/n
is the unique solution of xn = am in (1, ∞). Its existence and uniqueness follow from the
Intermediate Value Theorem since xn is continuous, increasing, and unbounded as x →∞
with value 1 at x = 1.
Claim 1: For positive integers N, 1 < a1/N < 1 + (a −1)/N.
Proof: For h > 0, (1 + h)N > 1 + Nh by the Binomial Theorem and 1 + Nh ≥a if
h ≥(a −1)/N. Thus h ≥(a −1)/N =⇒(1 + h)N > a, so if a1/N = 1 + h then we see
a1/N −1 = h < (a −1)/N, so a1/N < 1 + (a −1)/N.
From Claim 1, a1/N →1 as N →∞in Z.
Take for granted that aras = ar+s for rational r, s ≥0.
From this it follows that
0 ≤r < s =⇒ar < as: s −r > 0 =⇒as−r > 1 =⇒as = aras−r > ar. Then ar →1 as
r →0+ through rational numbers because it is true when r = 1/N and ar is increasing.
Claim 2: On each bounded interval Q ∩[0, M] for integers M ≥1, the function f(r) = ar
is uniformly continuous.
Proof: Pick a positive integer N and let r, s ∈Q ∩[0, M] satisfy |r −s| < 1/N. Suppose
r ≥s. Then
f(r) −f(s) = ar −as = as(ar−s −1) =⇒|f(r) −f(s)| ≤aM(ar−s −1).
From r −s < 1/N we get 1 ≤ar−s < a1/N < 1 + (a −1)/N by Claim 1, so 0 ≤ar−s −1 <
(a −1)/N. Thus |f(r) −f(s)| ≤aM(a−1)
N
. If instead r < s then we get the same bound by
switching the roles of r and s. Thus
r, s ∈Q ∩[0, M] and |r −s| < 1
N =⇒|f(r) −f(s)| ≤aM(a −1)
N
.
This implies uniform continuity on Q ∩[0, M]: for ε > 0 let δ = 1/N where N is chosen
large enough that aM(a −1)/N < ε.
By Claim 2 and Theorem 8.23, for each integer M ≥1 the function f(x) = ax on
Q ∩[0, M] uniquely extends to a uniformly continuous function on [0, M], which we will
also denoted by ax. For example, a
√
2 is the limit of ar for rationals r tending to
√
2. The
function ax on [0, M] for larger M has to agree with ax on [0, M] for smaller M since there’s
at most one continuous extension on each [0, M]. Therefore letting M →∞we get a single
continuous function ax for all x ≥0 that agrees with the originally deﬁned ax when the
exponent x is rational.
Exercises.
(1) On R, prove d(x, y) =
p
|x −y| is a metric but d(x, y) = (x −y)2 is not.
(2) Check the functions d∞and d1 on C[0, 1] in Example 2.3 are metrics.
(3) In the deﬁnition of a metric, prove the condition d(x, y) ≥0 in (i) is a consequence
of (ii) and (iii) by specializing the inequality in (iii) to the cases where some of x,
y, and z are equal. (That d(x, y) = 0 ⇐⇒x = y in (i) is not a consequence of (ii)
and (iii): look up the term “pseudometric”.)
(4) Check Example 2.4: if (X, d) is a metric space and Y is a nonempty subset of X
then Y together with the restriction of d to Y × Y is a metric space.
(5) Verify on each non-empty set that the discrete metric (Example 2.5) is a metric.
(6) Verify for a metric space (X, d) that the functions d′(x, y) = min(d(x, y), 1) and
d′′(x, y) = d(x, y)/(1 + d(x, y)) from Example 2.6 are both metrics on X.

<!-- page 36 -->
36
KEITH CONRAD
(7) In the deﬁnition of a limit of a sequence, prove the limit is unique: if xn →x and
xn →y then x = y. (This was implicitly assumed when we used limits.)
(8) Prove Theorem 4.8. (Don’t confuse Cauchy sequences with convergent sequences.)
(9) Let X be a metric space and Y be a subset, treated as a metric space using the
metric induced from X. Show every open set in the metric space Y has the form
U ∩Y where U is an open set in X, and conversely U ∩Y is open in Y when U
is open in X. (Hint: First treat the case of open balls in Y , and it may help to
distinguish open balls in X or Y with the same center and radius, using notation
like BX(y, r) and BY (y, r).)
(10) Let (X, d) be a metric space.
For a ∈X and 0 < r1 < r2, show the annulus
{x ∈X : r1 < d(a, x) < r2} is open and {x ∈X : r1 ≤d(a, x) ≤r2} is closed.
(11) Show every closed subset of a compact metric space is a compact subset by two
methods: using the convergent subsequence description of compactness and using
the open covering description of compactness.
(12) Show every Cauchy sequence with a convergent subsequence is itself convergent and
use that to show every compact subset of a metric space is complete for the induced
metric.
(13) Fill in the details from Remark 8.10: prove a function f : X →Y between two
metric spaces is continuous at a point a ∈X (based on the (ε, δ)-deﬁnition) if and
only if for every open U ⊂Y containing f(a) there is an open V ⊂X containing a
such that f(V ) ⊂U.
(14) Show each line in R2 is a closed subset in two ways: by the deﬁnition of a closed
subset and by Corollary 8.11. (Hint for the second way: show each line has the form
f−1(c) for some continuous function f : R2 →R and c ∈R.)
(15) For every interval I in R, construct a continuous function f : (0, 1) →R with
image I. Therefore the connectedness of (0, 1) implies the connectedness of all other
intervals by Theorem 8.16. Treat open, closed, and half-open intervals separately
and don’t forget to allow I to have endpoints ±∞.
(16) Prove the inequality in Remark 8.5.
(17) Let f : X →Y and g: X →Y be two continuous functions between the same metric
spaces. Show {x ∈X : f(x) = g(x)} is a closed subset of X.
(18) Let K1 and K2 be disjoint compact subsets of a metric space. Prove there is c > 0
such that d(x1, x2) ≥c for all x1 ∈K1 and x2 ∈K2. (This result is true when just
one of the subsets is compact, as long as the other is closed.) Give an example of
two disjoint non-compact closed subsets of R2 for which the conclusion is false for
those subsets (Hint: horizontal asymptote).
(19) Viewing R× as a metric space using the absolute value metric from R, show inversion
R× →R given by f(x) = 1/x is a continuous function. Then show all rational
functions with real coeﬃcients are continuous on R away from the numbers where
the denominator is 0.
(20) As suggested in Example 8.26, show 1/x is not uniformly continuous on (0, 1] directly
from the deﬁnition of uniform continuity, without using a result like Theorem 8.25.
(21) Is the function f(x) = √x on [0, ∞) uniformly continuous?
(22) For functions f : R →R and g: R →R, let F : R →R2 by F(x) = (f(x), g(x)).
Lemma 8.13 says that if f and g are continuous then F is continuous. Prove the
converse: if F is continuous then f and g are continuous.

<!-- page 37 -->
METRIC SPACES
37
(23) Convergence of f : [a, ∞) →R at ∞is deﬁned like in the case of sequences: f(x) has
limit L as x →∞if for every ε > 0 there is an N such that x ≥N ⇒|f(x)−L| < ε.
For a continuous function f : [a, ∞) →R, prove that if f(x) has a limit as x →∞
then f is uniformly continuous on [a, ∞). (Hint: on each interval [a, b] the function is
uniformly continuous, so focus on large x.) Show the converse has counterexamples
where f is bounded and also where f is unbounded.
(24) (Uniform continuity for diﬀerent metrics with the same open sets)
a) If f : (a, b) →R is injective, then prove df(x, x′) := |f(x) −f(x′)| is a metric
on (a, b).
b) Let g: (−1, 1) →R by g(x) = x/(1 −|x|). Show g is a continuous bijection
with inverse g−1(y) = y/(1 + |y|) that is continuous.
c) Use part (b) to prove that for a sequence {xn} and number L in (−1, 1),
dg(xn, L) →0 in R ⇐⇒|xn −L| →0 in R, where R has its usual metric in both
cases. Then show that implies dg and the usual metric on (−1, 1) give (−1, 1) the
same open sets. (Hint: see comments about convergence and limits in Example 6.9.)
d) Show the function g: (−1, 1) →R in part (b) is uniformly continuous when
(−1, 1) has the metric dg and R has its usual metric, while g is not uniformly con-
tinuous when (−1, 1) and R have their usual metrics. So by (c), uniform continuity
of a function between two metric spaces may not be preserved if a metric is replaced
by another metric having the same open sets. (Hint: See Example 8.26.)
(25) (Compactifying a half-inﬁnite interval) Let f : [0, ∞] →[0, 1] by f(x) = x/(1 + x)
if 0 ≤x < ∞and f(∞) = 1. (Graph y = x/(1 + x) to see how f looks on [0, ∞).)
a) Prove df(x, x′) = |f(x) −f(x′)| = |x/(1 + x) −x′/(1 + x′)| makes [0, ∞] a
metric space.
b) Prove the metric df makes [0, ∞] compact.
c) Prove the usual absolute value metric and df give [0, ∞) the same open sets.
d) When [0, ∞) is given the metric in part (a), prove a continuous function
g: [0, ∞) →R is uniformly continuous if and only if limx→∞g(x) exists.
This
equivalence is not true if [0, ∞) has it usual absolute value metric, as seen at the
end of Exercise 23. (Recall by the end of Exercise 24 that uniform continuity is
sensitive to the metric even if a change of metric doesn’t change the open sets.)
(26) Let (X, dX) and (Y, dY ) be metric spaces.
a) Prove X × Y can be made into a metric space by either of the functions
d1((x, y), (x′, y′)) = max(dX(x, x′), dY (y, y′)),
d2((x, y), (x′, y′)) =
p
dX(x, x′)2 + dY (y, y′)2
and that these metrics give X × Y the same open sets. (Hint for the last part: look
at the picture in the proof of Lemma 8.13.)
b) When X and Y are compact, show X × Y is compact when using the metrics
from part (a).
Appendix A. Proofs about completeness
In Example 4.16 we stated the following theorem, which we will now prove.
Theorem A.1. The metric space (C[0, 1], d∞) is complete.
Proof. Let {fn} be a Cauchy sequence in this space. We’ll show it has a limit in three steps.

<!-- page 38 -->
38
KEITH CONRAD
Step 1: Create a candidate limit function f : [0, 1] →R in the space.
For each a ∈[0, 1] the sequence of numbers {fn(a)} is Cauchy since
|fm(a) −fn(a)| ≤max
0≤x≤1 |fm(x) −fn(x)| = d∞(fm, fn)
and the value on the right is arbitrarily small for all large enough m and n. Therefore
limn→∞fn(a) exists by completeness of R. Call the limit f(a). We have deﬁned a
function f : [0, 1] →R using pointwise considerations.
Step 2: Show f is continuous.
This will be proved with an ε/3 argument.
Pick a ∈[0, 1] and ε > 0. We need to ﬁnd δ > 0 such that |x −a| < δ =⇒
|f(x) −f(a)| < ε.
Since {fn} is Cauchy, there is N such that m, n ≥N =⇒d∞(fm, fn) < ε/3, so
for all x ∈[0, 1] and m ≥N we have |fm(x) −fN(x)| < ε/3. Letting m →∞in this
inequality, |f(x) −fN(x)| ≤ε/3 for all x in [0, 1]. Thus for each x in [0, 1],
|f(x) −f(a)| ≤|f(x) −fn(x)| + |fN(x) −fN(a)| + |fN(a) −f(a)|
≤ε
3 + |fN(x) −fN(a)| + ε
3
= 2
3ε + |fN(x) −fN(a)|.
Since fN is continuous at a, there is δ > 0 such that |x−a| < δ =⇒|fN(x)−fN(a)| <
ε/3. Therefore
|x −a| < δ =⇒|f(x) −f(a)| ≤2
3ε + |fN(x) −fN(a)| < ε,
which proves f is continuous at each a ∈[0, 1].
Step 3: Show d∞(fn, f) →0.
We essentially repeat the beginning of Step 2. From {fn} being Cauchy there is
an N such that m, n ≥N =⇒d∞(fm, fn) < ε/3, so for all x ∈[0, 1] and m, n ≥N
we have |fm(x) −fn(x)| < ε/3. Letting m →∞here, we get |f(x) −fn(x)| ≤ε/3
for all x ∈[0, 1]. Therefore d∞(f, fn) ≤ε/3 < ε.
□
Remark A.2. Step 2 in the above proof can be adapted to uniform limits of continuous
functions between arbitrary metric spaces X and Y : if fn : X →Y is a sequence of con-
tinuous functions and f : X →Y is a function such that supx∈X dY (fn(x), f(x)) < ∞for
each n and it tends to 0 as n →∞then f is continuous (“a uniform limit of continuous
functions is continuous”). The analogue of the triangle inequality calculation in Step 2 is
dY (f(x), f(a)) ≤dY (f(x), fN(x)) + dY (fN(x), fN(a)) + dY (fN(a), f(a)),
with the ﬁrst and third term on the right being less than ε/3 for large enough N by the
uniform convergence assumption, and the middle term being less than ε/3 when x is close
enough to a in X by the continuity of fN at a.
Next we will prove Theorem 4.22, which we restate.
Theorem A.3. Every metric space has a completion.
Proof. Let the metric space be (X, d). We seek a complete metric space ( b
X, bd) containing
(X, d) as a dense subset. The purpose of the proof is to show some construction is possible,
but in practice nobody thinks about a completion by the way it will be constructed here.

<!-- page 39 -->
METRIC SPACES
39
In particular, analysts want to work with concrete complete metric spaces, not abstract
completions. More comments about creating completions will be given after the proof.
Before building b
X, here are properties it must have if it exists.
(1) Each bx ∈b
X is a limit of a sequence from X since X is dense in b
X: bx = limn→∞xn
with xn ∈X, so {xn} is a Cauchy sequence in b
X (Theorem 4.3) and thus is also a
Cauchy sequence in X since bd = d on X.
(2) A second Cauchy sequence {x′
n} in X converges to the same limit bx if and only if
bd(xn, x′
n) →0 (Theorems 3.7 and 3.8), which is the same as d(xn, x′
n) →0 since
bd = d on X.
(3) The metric on b
X can be expressed as a limit of values of the metric on X: if bx and
by are in b
X and xn →bx and yn →by with xn, yn ∈X, then d(xn, yn) →bd(bx, by) by
Remark 8.5 (because d(xn, yn) = bd(xn, yn)).
Since each element of b
X is a limit of a Cauchy sequence in X, and two Cauchy sequences
in X tend to the same value in b
X exactly when their termwise distance tends to 0, this
suggests an idea for how to deﬁne b
X: let it be the set of all Cauchy sequences in X, with
sequences identiﬁed when the termwise distance goes to 0. This will turn out to work, and
generalizes one of the constructions of R out of Q: a real number is an equivalence class of
Cauchy sequences of rational numbers relative to the absolute value on Q.
Let C be the set of all Cauchy sequences in X. Introduce a relation ∼on C by
{xn} ∼{yn} if d(xn, yn) →0.
It is left to the reader to check ∼is an equivalence relation on C. Denote the equivalence
class of {xn} in C as [xn], so
[xn] = {{yn} ∈C : d(xn, yn) →0}.
Embed X into C by viewing each x ∈X as the constant Cauchy sequence {x, x, x, . . .}.
For diﬀerent x and y in X, the constant sequences (x, x, x, . . .) and (y, y, y, . . .) are not
equivalent since d(x, y) > 0.
Deﬁne b
X to be the set of equivalence classes in C for the relation ∼. The motivation for
this deﬁnition of b
X is to have a set that has the ﬁrst and second properties that we already
observed a completion of (X, d) should have. To put a metric on b
X we will get motivation
from the third property listed above. It suggests the deﬁnition
bd([xn], [yn]) = lim
n→∞d(xn, yn).
There are now three things we need to verify:
(1) The function bd makes sense and is a metric on b
X.
(2) We can view X as a dense subset of b
X and bd restricts on X to be d.
(3) The metric space ( b
X, bd) is complete.
(1) bd makes sense and is a metric on b
X.
First we show for Cauchy sequences {xn} and {yn} in X that the sequence {d(xn, yn)}
in R is Cauchy, so it has a limit by completeness of R. (In the motivation to deﬁne bd
we discussed how a metric behaves on convergent sequences, but we are no longer dealing
with convergent sequences, only Cauchy sequences, so knowing the numbers d(xn, yn) have
a limit really requires a proof.) By the inequality in Remark 8.5,
|d(xm, ym) −d(xn, yn)| ≤d(xm, xn) + d(ym, yn).

<!-- page 40 -->
40
KEITH CONRAD
From the Cauchy property in X both d(xm, xn) and d(ym, yn) become arbitrarily small for
suﬃciently large m and n, so the above inequality tells us that the sequence {d(xn, yn)} is
Cauchy in R. Thus limn→∞d(xn, yn) exists.
Since b
X is not the Cauchy sequences in X, but equivalence classes of them, to show bd
makes sense we have to check its formula doesn’t change if we replace Cauchy sequences
by equivalent Cauchy sequences: if {xn} ∼{x′
n} and {yn} ∼{y′
n} in C, we need to show
limn→∞d(xn, yn) = limn→∞d(x′
n, y′
n). Once again we appeal to the inequality in Remark
8.5, writing it now in the form
|d(xn, yn) −d(x′
n, y′
n)| ≤d(xn, x′
n) + d(yn, y′
n).
The terms on the right side both tend to 0 as n →∞by the deﬁnition of the relation ∼, so
d(xn, yn) −d(x′
n, y′
n) →0 in R. Thus the convergent sequences {d(xn, yn)} and {d(x′
n, y′
n)}
in R have the same limit, and this ﬁnishes the proof that bd makes sense on b
X.
It is left to the reader to show bd is a metric on b
X. We raise one issue: the fact that
bd([xn], [yn]) = 0 =⇒[xn] = [yn]
relies on the equivalence relation used to deﬁne b
X. This is why it’s important for b
X to be
equivalence classes of Cauchy sequences in X and not the Cauchy sequences in X. If we
had tried to work with the Cauchy sequences as the primary object, then wanting a metric
on them would force us to introduce the equivalence relation ∼anyway.
(2) X can be viewed as a dense subset of b
X and bd = d on X.
Associate to x ∈X the equivalence class of the constant sequence where each term is x:
x := [(x, x, x, . . .)].
If x ̸= y in X then bd(x, y) = limn→∞d(x, y) = d(x, y) > 0. so the function X →b
X where
x 7→x is injective. This is how we view X as a subset of b
X, and the calculation we just
made shows bd = d on the copy of X inside b
X.
Why is the copy of X in b
X a dense subset? Pick an element [xn] of b
X and an ε > 0. We
want to ﬁnd an x ∈X such that x is within ε of [xn]. We’ll show that each element deep
enough into the Cauchy sequence {xn} can be used as x. Since {xn} is Cauchy, there’s an
N such that m, n ≥N =⇒d(xm, xn) < ε. Setting x = xN,
(A.1)
bd(x, [(x1, x2, x3, . . .)]) = lim
n→∞d(xN, xn) ≤ε.
Anyone who is pedantic can replace ε with ε/2 to make the limit strictly less than ε.
By the same reasoning, for all m ≥N we have bd(xm, [xn]) ≤ε, so [(x1, x2, x3, . . .)] is the
limit of {xm} as m →∞. This shows that, in a loose sense, each Cauchy sequence in X has
been turned into the limit of its own terms (but we have to work with equivalence classes
of Cauchy sequences to make everything proper).
(3) ( b
X, bd) is complete.
Let bx1, bx2, bx3, . . . be a Cauchy sequence of elements of b
X. (This is a “Cauchy sequence
of equivalence classes of Cauchy sequences from X,” but don’t think too hard about it that
way.) By (2), for each n ≥1 we can pick yn ∈X such that bd(bxn, yn) →0. (For example, we
can make the distance at most 1/n.) Then y1, y2, y3, . . . is Cauchy in b
X by Theorem 4.9,
so y1, y2, y3, . . . is Cauchy in X since d(ym, yn) = bd(ym, yn). Deﬁne by = [yn] in b
X. We will
show bxn →by.

<!-- page 41 -->
METRIC SPACES
41
Pick ε > 0. For all m and n,
bd(bxn, ym) ≤bd(bxn, yn) + bd(yn, ym) = bd(bxn, yn) + d(yn, ym).
For all suﬃciently large m and n (depending on ε) we can make bd(bxn, yn) < ε/2 by the
deﬁnition of yn and d(yn, ym) < ε/2 by the Cauchy property. Therefore bd(bxn, ym) < ε for
all suﬃciently large m and n. Since ym →by by (2), by continuity of metrics (Theorem 8.4)
lim
m→∞
bd(bxn, ym) = bd(bxn, by).
For suﬃciently large n, this limit is at most ε. That proves bxn →by in b
X.
□
The method we used to construct a completion is not the only approach. Here’s a second
one.
For a metric space X, let Cb(X) be the set of all continuous bounded functions
X →R. It is a metric space where the distance between functions f and g is deﬁned as
supx∈X |f(x) −g(x)|. (We use a supremum since a continuous bounded function might not
have a maximum; X may be non-compact.)
The space Cb(X) with this metric is complete. A proof can be made by adapting the
proof of Theorem 4.16, which is the special case X = [0, 1]. We can embed X into Cb(X) by
ﬁxing a choice of a ∈X and, in terms of this choice, associating to each y ∈X the function
fy : X →R given by fy(x) = d(y, x) −d(a, x). The function fy is continuous by Theorem
8.4 and it is bounded since |fy(x)| ≤d(a, y) for all x ∈X by the proof of Theorem 8.4.16 It
turns out that supx∈X |fy(x)−fz(x)| = d(y, z), so y 7→fy is an embedding of X into Cb(X)
and the metric on Cb(X) restricts to the metric d on X under this embedding. Closures
of subsets are closed (Theorem 5.15) and closed subsets of complete spaces are complete
(Theorem 5.11), so the closure of the embedded copy of X in Cb(X) is a completion of X.
The construction of a completion using equivalence classes of Cauchy sequences is more
robust than the method using Cb(X), since when X has additional structure that interacts
well with the metric (e.g., being a normed vector space or a ﬁeld), completing using equiv-
alence classes of Cauchy sequences shows the completion has the same additional structure
automatically, while this is not clear by embedding X into Cb(X).
Sometimes no abstract construction of a completion shows a particular feature of X
persists in its completion, so a more speciﬁc technique is needed to reveal that feature
in the completion. For example, the metric space of functions (C[0, 1], d1) is incomplete
(Example 4.17) and analysts want to think of elements in the completion as functions on
[0, 1]. Part of a course on measure theory is devoted to explaining why the completion
consists of certain real-valued functions on [0, 1].
References
[1] A.-L. Cauchy, “Cours d’Analyse de l’´Ecole Royale Polytechnique. 1re Partie:
Analyse Alg´ebrique,”
L’Imprimerie Royale, Debure Fr`eres, Paris, 1821. URL https://gallica.bnf.fr/ark:/12148/btv1b86
26657t/f9.item.
[2] K. Conrad, Spaces that are Connected but not Path-connected, https://kconrad.math.uconn.edu/
blurbs/topology/connnotpathconn.pdf.
[3] M. Fr´echet, “Sur quelques points du calcul fonctionnel,” Rendiconti del Circolo Matematico di Palermo 22
(1906), pp. 1–72. URL https://babel.hathitrust.org/cgi/pt?id=mdp.39015057352307;view=1up;
seq=9.
16It is more natural to convert points of X into continuous functions on X by associating to each y ∈X
the function x 7→d(y, x), but this function is not bounded if the metric on X takes arbitrarily large values.
Subtracting d(a, x) creates a bounded function.

<!-- page 42 -->
42
KEITH CONRAD
[4] K. A. Ross, “Elementary Analysis: The Theory of Calculus,” Springer-Verlag, New York, 1980.
[5] S. M. Srivastava, “How did Cantor Discover Set Theory and Topology?”, Resonance 19 (2014), 977–999.
URL https://www.ias.ac.in/article/fulltext/reso/019/11/0977-0999.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*