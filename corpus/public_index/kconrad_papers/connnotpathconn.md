# Connected but Not Path Connected Spaces

> **Source**: https://kconrad.math.uconn.edu/blurbs/connnotpathconn.pdf  
> **Author**: Keith Conrad  
> **Topic**: topology  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SPACES THAT ARE CONNECTED BUT NOT PATH-CONNECTED
KEITH CONRAD
1. Introduction
A topological space X is called connected if it’s impossible to write X as a union of two
nonempty disjoint open subsets: if X = U ∪V where U and V are open subsets of X and
U ∩V = ∅then one of U or V is empty. Intuitively, this means X consists of one piece. A
subset of a topological space is called connected if it is connected in the subspace topology.
The most fundamental example of a connected set is the interval [0, 1], or more generally
any closed or open interval in R.
Most reasonable-looking spaces that appear to be connected can be proved to be con-
nected using properties of connected sets like the following [2, pp. 149–151]:
• if f : X →Y is continuous and X is connected then f(X) is connected,
• if C is a connected subset of X then C is connected and every set between C and
C is connected,
• if Ci are connected subsets of X and T
i Ci ̸= ∅then S
i Ci is connected,
• a direct product of connected sets is connected.
Proving complicated fractal-like sets are connected can be a hard theorem, such as connect-
edness of the Mandelbrot set [1].
We call a topological space X path-connected if, for every pair of points x and x′ in X,
there is a path in X from x to x′: there’s a continuous function p: [0, 1] →X such that
p(0) = x and p(1) = x′. Since q(t) = p(1 −t) is also continuous with q(0) = p(1) = x′
and q(1) = p(0) = x, we can think of a path going in either direction, x to x′ or x′ to x.
A subset Y ⊂X is called path-connected if any two points in Y can be linked by a path
taking values entirely inside Y .
Path-connectedness shares some properties of connectedness:
• if f : X →Y is continuous and X is path-connected then f(X) is path-connected,
• if Ci are path-connected subsets of X and T
i Ci ̸= ∅then S
i Ci is path-connected,
• a direct product of path-connected sets is path-connected.
Compared to the list of properties of connectedness, we see one analogue is missing: every
set lying between a path-connected subset and its closure is path-connected. In fact that
property is not true in general.
For reasonable-looking subsets of Euclidean space, connectedness and path-connectedness
are the same thing: one property holds if and only if it the other property does. But the
properties are not always the same. We will set out here the precise logical connection
(pun intended): path-connectedness implies connectedness, but the converse direction is
false and we’ll give three explicit examples of a connected set that is not path-connected.
The ﬁrst two will use objects you can ﬁnd around your house: a broom and a comb. Well,
not quite. The examples will be ﬁgures made up of carefully arranged line segments in the
plane, together with one extra point, that are inﬁnite versions of a broom and a comb. All
1

<!-- page 2 -->
2
KEITH CONRAD
three examples will be path-connected subsets together with one limit point, and including
the limit point will wreck path-connectedness.
2. Path-connectedness implies connectedness
Theorem 2.1. Every path-connected space is connected.
Proof. Let X be path-connected. We will use paths in X to show that if X is not connected
then [0, 1] is not connected, which of course is a contradiction, so X has to be connected.
Suppose X is not connected, so we can write X = U ∪V where U and V are nonempty
disjoint open subsets. Pick x ∈U and y ∈V . There is a path p: [0, 1] →X where p(0) = x
and p(1) = y. The partition of X into U and V leads via this path to a partition of [0, 1]:
[0, 1] = A ∪B where A = p−1(U) and B = p−1(V ).
Note 0 ∈A and 1 ∈B, so A and B are nonempty subsets of [0, 1]. Obviously A and
B are disjoint, since no point in [0, 1] can have its p-value in both U and V . Since p is
continuous and U and V are both open in X, A and B are both open in [0, 1]. Thus the
equation [0, 1] = A ∪B exhibits [0, 1] as a disjoint union of two nonempty open subsets,
which contradicts the connectedness of [0, 1].
□
Remark 2.2. A second proof of Theorem 2.1 is based on a property of connectedness listed
earlier: if Ci are connected subsets and T
i Ci ̸= ∅, then S
i Ci is a connected subset. If X is
path-connected and we ﬁx a point x ∈X then for each y ∈X there’s a path py in X from x
to y, so we can cover X by the images of these paths: X = S
y∈X py([0, 1]). Each py([0, 1]) is
connected since the image of a connected set under a continuous function is connected, and
since x = py(0) for all y ∈X, the diﬀerent subsets py([0, 1]) have a nonempty intersection.
Thus X is connected. B. Conrad noted that this proof can be condensed to a sentence: “All
roads lead to Rome” (or equivalently, all roads lead from Rome).
3. Connectedness does not imply path-connectedness
Examples of connected sets that are not path-connected all look weird in some way. We
will describe two examples that are subsets of R2. The ﬁrst one is called the deleted inﬁnite
broom.
It is pictured below and consists of the closed line segments Ln from (0, 0) to
(1, 1/n) as n runs over the positive integers together with the (red) point (1, 0). The x-axis
strictly between 0 and 1 is not part of this.
(0,0)
(1,1)
(1,1/2)
(1,1/3)
(1,1/4)
(1,0)

<!-- page 3 -->
SPACES THAT ARE CONNECTED BUT NOT PATH-CONNECTED
3
Theorem 3.1. The deleted inﬁnite broom is connected.
Proof. Each point on Ln can be linked to (0, 0) by a path along Ln. By concatenating
such paths, points on Lm and Ln can be linked by a path via (0, 0) if m ̸= n, so the union
S
n≥1 Ln is path-connected and therefore is connected (Theorem 2.1). The point (1, 0) is a
limit point of S
n≥1 Ln , so the deleted inﬁnite broom lies between S
n≥1 Ln and its closure
in R2. Therefore by the second property of connectedness in the introduction, the deleted
inﬁnite broom is connected.
□
Remark 3.2. The closure of S
n≥1 Ln is obtained by adjoining to this union the segment
L∞from (0, 0) to (1, 0), and the closure is called the inﬁnite broom, which is why the space
we care about is called the deleted inﬁnite broom. The inﬁnite broom is path-connected.
It makes sense intuitively that the deleted inﬁnite broom is not path-connected: if a path
starts at (1, 0) and stays within the deleted inﬁnite broom it is hard to imagine how the
path could “make the leap” to the rest of the space. In other words, you should have a
feeling that any path in the deleted inﬁnite broom that starts at (1, 0) has to be constant.
To prove that path property, we will ﬁrst look at the endpoints of the segments Ln that
lie on the line x = 1 together with (1, 0). The line x = 1 is homeomorphic to the real line,
and rotating it by 90 degrees makes those endpoints and (1, 0) look like the ﬁgure below,
which is the number 0 and 1/n for all n ∈Z+.
0
1
Lemma 3.3. The set {0}∪{1/n : n ∈Z+} with its subspace topology in R has one-element
subsets as its only nonempty connected subsets.
Proof. Let C be a nonempty connected subset of {0} ∪{1/n : n ∈Z+}. Assume C contains
some 1/n. Since {1/n} is both closed and open in this set, writing C = {1/n}∪(C −{1/n})
expresses C as a union of disjoint open subsets, so one of the subsets is empty.
Thus
C −{1/n} is empty, so C = {1/n}. If C does not contain any 1/n then the only choice is
C = {0}.
□
Remark 3.4. A topological space whose only nonempty connected subsets are one-element
subsets is called totally disconnected, so the set in Lemma 3.3 is totally disconnected. Other
examples include Q with its standard topology as a subset of R, and Q
n≥1{1, −1} with the
product topology.
Lemma 3.3 is the key technical idea for proving the deleted inﬁnite broom is not path-
connected.
Theorem 3.5. The deleted inﬁnite broom is not path-connected.
Proof. Denote the deleted inﬁnite broom as B and let p: [0, 1] →B be a path such that
p(0) = (1, 0). We will prove p(t) = (1, 0) for all t ∈[0, 1], so no path in B links (1, 0) to any
other point of B.
Let
A = {t ∈[0, 1] : p(t) = (1, 0)}
This is a nonempty subset of [0, 1] since it contains 0. Our goal is to show A = [0, 1].
The set A is closed in [0, 1] since it is p−1((1, 0)) and p is continuous.

<!-- page 4 -->
4
KEITH CONRAD
Next we show A is open in [0, 1]. This will require a lot more work than showing it is
closed. For t0 ∈A we want to ﬁnd an open interval around t0 in [0, 1] that is also in A.
By continuity of p at t0 there’s a δ > 0 such that if t ∈[0, 1] satisﬁes |t −t0| < δ then
||p(t) −p(t0)|| < 1/2, where || · || is the length of a vector in R2.1 Then p(t) ̸= (0, 0) since
||p(t0)|| = ||(1, 0)|| = 1 > 1/2, so p(t) has a positive x-coordinate for all t ∈[0, 1] satisfying
|t −t0| < δ.
Consider the slope function m: {(x, y) ∈R2 : x > 0} →R deﬁned by m(x, y) = y/x.
This is the slope of the line connecting (x, y) to (0, 0) and it is clearly continuous. (We’d
run into a problem if we tried to extend m to the y-axis.)
Since p(t) has positive x-
coordinate for all t ∈[0, 1] satisfying |t −t0| < δ, we can compose p with m to get the
continuous function t 7→m(p(t)) mapping the interval I := (t0 −δ, t0 + δ) ∩[0, 1] to R.
Since the values of p on I are in the deleted inﬁnite broom without the origin, we get
m(p(I)) ⊂{0} ∪{1/n : n ∈Z+}. The set m(p(I)) is connected since this is the image of a
connected set I under a continuous function. Therefore by Lemma 3.3, m(p(I)) is a single
point. Since t0 ∈I and m(p(t0)) = m(1, 0) = 0, we get m(p(I)) = 0, so I is an open set
around t0 in [0, 1] that is contained in A. Thus A is open in [0, 1].
The only nonempty open and closed subset of [0, 1] is [0, 1], since [0, 1] is connected.
Therefore A = [0, 1], which means p(t) = (1, 0) for all t ∈[0, 1].
□
To understand the ideas in this argument, we apply them to a second subset of R2 that
is connected but not path-connected, called the deleted comb space D. It is pictured below.
(0,0)
1
1
2
1
3
1
4
(0,1)
By deﬁnition, D is the union of the interval [0, 1] along the x-axis together with vertical
line segments connecting (1/n, 0) to (1/n, 1) for n ∈Z+ and the single (red) point (0, 1):
D = ([0, 1] × {0}) ∪
[
n≥1
({1/n} × [0, 1]) ∪(0, 1).
The y-axis strictly between 0 and 1 is not part of this.
Theorem 3.6. The deleted comb space is connected but not path-connected.
Proof. The set D′ = D −{(0, 1)} is obviously path-connected: there’s a path in D′ linking
any point in a bristle to the point on the x-axis at the end of that bristle, and any two points
in D′ on the x-axis can obviously be linked by a path in D′ on the x-axis. Concatenating
1We’re using here the ε-δ deﬁnition of continuity of p: [0, 1] →B at t0 with ε = 1/2.

<!-- page 5 -->
SPACES THAT ARE CONNECTED BUT NOT PATH-CONNECTED
5
these constructions proves D′ is path-connected, and thus connected. Since (0, 1) is a limit
point of D′, D lies between D′ and its closure, so D is connected for the same reason the
deleted inﬁnite broom is connected. (The closure of D′ in R2 is D together with the y-axis
from 0 to 1, and it is path-connected.)
To prove D is not path-connected we’ll show no path in D links (0, 1) to any other point:
if p: [0, 1] →D has p(0) = (0, 1) then p(t) = (0, 1) for all t.
Let
A = {t ∈[0, 1] : p(t) = (0, 1)}
Since 0 ∈A, this is a nonempty subset of [0, 1]. We will show A = [0, 1] by showing A is
open and closed in [0, 1].
The set A is closed since A = p−1((0, 1)) and p is continuous.
To show A is open, choose t0 ∈A. From continuity of p, there’s a δ > 0 such that if
t ∈[0, 1] satisﬁes |t −t0| < δ then ||p(t) −p(t0)|| < 1/2, so ||p(t) −(0, 1)|| < 1/2. No point
on the x-axis is within 1/2 of (0, 1), so p(t) is not on the x-axis when t ∈[0, 1] satisﬁes
|t −t0| < δ.
In place of the slope function m from the previous proof we will use the x-coordinate
function.
For points in D that are not on the x-axis, their x-coordinate is 0 or of the
form 1/n for a positive integer n. The x-coordinate function x: R2 →R is continuous
and we can deﬁne a function f : (t0 −δ, t0 + δ) ∩[0, 1] →R by f(t) = x(p(t)), which is
continuous since it’s the composition of continuous functions. Set I := (t0 −δ, t0 +δ)∩[0, 1],
which is an open interval of [0, 1] and thus is connected. Therefore f(I) is connected and it
belongs to {0} ∪{1/n : n ∈Z+}, so f(I) is a single point by Lemma 3.3. Since t0 ∈I and
f(t0) = x(p(t0)) = x((0, 1)) = 0 we get f(I) = {0}, so I ⊂A. Therefore A is open (for each
t0 ∈A some open interval around t0 in [0, 1] is also in A.)
□
Our third example of a topological space that is connected but not path-connected is
the topologist’s sine curve, pictured below, which is the union of the graph of y = sin(1/x)
for x > 0 and the (red) point (0, 0). (We stretch the graph horizontally to make its shape
clearer, which doesn’t aﬀect the topological features.)
y
x
0
Theorem 3.7. The topologist’s sine curve is connected but not path-connected.
Proof. The graph of y = sin(1/x) for x > 0, like any graph of a function, is path-connected
and therefore is connected. Since (0, 0) is a limit point of this graph, adjoining it to the

<!-- page 6 -->
6
KEITH CONRAD
graph gives us a connected set for the same reason the deleted inﬁnite broom and deleted
comb space are connected.
Let S denote the topologist’s sine curve. To show S is not path-connected, we’ll show no
path in S links (0, 0) to any other point in S. At ﬁrst it might seem we could argue as in
the ﬁrst two examples, using the points in S along the x-axis as a totally disconnected set
analogous to the one in Lemma 3.3, but it does not seem to work; try it!
Suppose there is a path p in S from (0, 0) to a point on the graph of y = sin(1/x) with
x > 0. Let x: R2 →R be the x-coordinate function, which is continuous. The path p
starts oﬀon the y-axis and at some point has to “jump” onto the graph of sin(1/x), which
is the points in S with positive x-coordinate. Let t0 be the time this happens; precisely, set
(3.1)
t0 = inf{t ∈[0, 1] : x(p(t)) > 0}.
For t < t0, x(p(t)) = 0. By continuity of x ◦p at t0, x(p(t0)) = limt→t−
0 x(p(t)) = 0, so
p(t0) = (0, 0). By continuity of p at t0, there is a δ > 0 such that
(3.2)
t0 ≤t < t0 + δ ⇒||p(t)|| < 1
2.
We try to convey this visually in the picture below, where the red circle around (0, 0) = p(t0)
has radius 1/2.
y
x
0
By the deﬁnition of t0 as an inﬁmum, for this same δ there is a t1 with t0 < t1 < t0 + δ
such that a := x(p(t1)) > 0. The image x(p([t0, t1])) is connected and contains 0 = x(p(t0))
and a = x(p(t1)), and every connected subset of R is an interval, so
(3.3)
[0, a] ⊂x(p([t0, t1])).
This contradicts continuity of t 7→x(p(t)) at t0 by the picture above, because the graph of
sin(1/x) is oscillating in and out of the red circle, so the x-values on S inside the circle do
not contain a whole interval like [0, a]. To turn this visual idea into a strict logical argument
we look at where the peaks and troughs occur in S.
Since sin(θ) = 1 if and only if θ = (4k +1)π
2 and sin(θ) = −1 if and only if θ = (4k −1)π
2 ,
where k ∈Z, we have (x, sin(1/x)) = (x, 1) if x = 2/((4k + 1)π) and (x, sin(1/x)) = (x, −1)
if x = 2/((4k −1)π) for k ∈Z. Such x-values get arbitrarily close to 0 for large k, so
there are such x-values of both kinds in [0, a]. Therefore by (3.3) we get p(t′) = (∗, 1) and
p(t′′) = (∗, −1) for some t′ and t′′ in [t0, t1] ⊂[t0, t0 + δ). But ||p(t′)|| = ||(∗, 1)|| > 1/2 and
||p(t′′)|| = ||(∗, −1)|| > 1/2, which both contradict (3.2).
□

<!-- page 7 -->
SPACES THAT ARE CONNECTED BUT NOT PATH-CONNECTED
7
The closures of the deleted inﬁnite broom and deleted comb space are path-connected
since all points in the closure are linked to (0, 0) by a path in the closure, but the closure of
the topologist’s sine curve, which is obtained by adjoining the whole interval {0} × [−1, 1]
on the y-axis to the graph,2 is not path-connected.
Corollary 3.8. The closure of the toplogist’s sine curve is not path-connected.
Proof. We modify the previous proof to show there is no path starting at a point in {0} ×
[−1, 1] and ending at a point on the graph of y = sin(1/x). Assuming there is such path, p,
we have x(p(0)) = 0 and x(p(1)) > 0, so we can deﬁne t0 as in (3.1) and x(p(t0)) = 0. (It
may not be that p(t0) is (0, 0) anymore, but p(t0) does lie on the y-axis.) Choose δ so that
t0 ≤t < t0 + δ ⇒||p(t) −p(t0)|| < 1
2.
Once again there’s a t1 ∈(t0, t0+δ) such that x(p(t1)) > 0, so (3.3) holds where a = x(p(t1)).
For some large k we have 2/((4k ± 1)π) ∈[0, a] for both signs, so these are x-coordinates
of p(t′) and p(t′′) for some t′ and t′′ in [t0, t1] ⊂[t0, t0 +δ): p(t′) = (∗, 1) and p(t′′) = (∗, −1).
Since ||p(t′) −p(t0)|| < 1/2 and ||p(t′′) −p(t0)|| < 1/2, we get ||p(t′) −p(t′′)|| < 1, but
||p(t′) −p(t′′)|| = ||(∗, 1) −(∗, −1)|| ≥
p
(1 −−1)2 = 2 > 1, a contradiction.
□
A local version of being path-connected is being locally path-connected, which means every
neighborhood of each point contains an open set around the point that is path-connected.
This property neither implies nor is implied by path-connectedness. For instance, the union
(0, 1) ∪(2, 3) with its topology from R is locally path-connected but is not path-connected:
no path can involve points in both intervals. Here are three examples of topological spaces
that are path-connected but not locally path-connected.
• The closure of the deleted inﬁnite broom is path-connected but is not locally path-
connected: small neighborhoods of (0, 1/2) in it are not path-connected.
• The closure of the deleted comb space is path-connected but is not locally path-
connected: small neighborhoods (0, 1/2) in it are not path-connected.
• If we attach to the topologist’s sine curve a path from (0, 0) to (1/π, 0) (the rightmost
point where the curve crosses the x-axis) the resulting subset of R2 is path-connected
but is not locally path-connected since no small neighborhood of (0, 0) in it is path-
connected. See https://math.stackexchange.com/questions/135463.
Appendix A. A partial converse to Theorem 2.1
There is an important case where a converse to Theorem 2.1 holds: open subsets of Rn.
Theorem A.1. If a nonempty open subset of Rn is connected then it is path-connected.
Proof. Let X be a nonempty open subset of Rn and pick x ∈X. We want to show there
is a path in X from x to every point in X. The special property of Euclidean space that
we’re going to use in the proof is that balls in Rn are path-connected.
Set
U = {x′ ∈X : there is a path in X from x to x′}.
This is a nonempty subset of X since x ∈U (use the constant path p: [0, 1] →X where
p(t) = x for all t). We will show next that U is open. Suppose x′ ∈U. Since X is open in
2Some people use the term “topologist’s sine curve” to mean the closure of what we call the topologist’s
sine curve.

<!-- page 8 -->
8
KEITH CONRAD
Rn, there’s an open ball B in Rn such that x′ ∈B ⊂X. For every point b ∈B there is a
(straight line) path p1 from x′ to b that doesn’t leave B (so it doesn’t leave X either), and
since x′ ∈U there is a path p2 in X from x to x′. Concatenating these paths together gives
us a path in X from x to b. Strictly speaking, since paths are only deﬁned with domain
[0, 1] we get a path from x to b by spending the ﬁrst half of our time going from x to x′ and
the second half going from x′ to b: the function p: [0, 1] →X deﬁned by
p(t) =
(
p1(2t), if 0 ≤t ≤1
2,
p2(2t −1), if 1
2 ≤t ≤1,
is continuous (since p1(1) = x′ = p2(0)) and p(0) = p1(0) = x, p(1) = p2(1) = b. We have
shown every b ∈B is in U, so to each x′ ∈U there’s an open ball around x′ that is entirely
inside U as well. Thus U is open in X.
The complement of U in X is
V = {x′ ∈X : there is no path in X from x to x′}.
We want to prove V = ∅. If V were nonempty and x′ is an element of V , then there is an
open ball B in Rn such that x′ ∈B ⊂X. Since all points in B can be linked to x′ by a
path in B, if any point in B were in U then it could be linked by a path to x in X and we’d
then be able to link x and x′ by a path in X, which contradicts what it means for x′ to lie
in V . Thus B is disjoint from U, so B ⊂V . Therefore V is open in X (every point in V is
contained in an open ball of Rn that’s a subset of V ).
The equation X = U ∪V exhibits X as a disjoint union of nonempty open subsets if
V ̸= ∅, which is a contradiction of the connectedness of X, so V = ∅. That means U = X,
so every point in X can be linked to x by a path in X. Since this holds for all x ∈X, X is
path-connected.
□
References
[1] A. Douady and J. Hubbard, It´eration des polynˆomes quadratiques complexes, Comptes Rendus, Acad´emie
des Sciences, Paris 294 (1982), 123–126.
[2] J. Munkres, “Topology, A First Course,” Prentice-Hall, 1975.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*