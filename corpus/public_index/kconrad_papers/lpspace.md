# Lp Spaces for 0 < p < 1

> **Source**: https://kconrad.math.uconn.edu/blurbs/lpspace.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
Lp-SPACES FOR 0 < p < 1
KEITH CONRAD
1. Introduction
In a ﬁrst course in functional analysis, a great deal of time is spent with Banach spaces,
especially the interaction between such spaces and their dual spaces. Banach spaces are a
special type of topological vector space, and there are important topological vector spaces
that do not lie in the Banach category, such as the Schwartz spaces.
The most fundamental theorem about Banach spaces is the Hahn-Banach theorem, which
links the original Banach space with its dual space. What we want to illustrate here is a
wide collection of topological vector spaces where the Hahn-Banach theorem has no obvious
extension because the dual space is zero. The model for a topological vector space with
zero dual space will be Lp[0, 1] when 0 < p < 1. After proving the dual of this space is {0},
we’ll see how to make the proof work for other Lp-spaces, with 0 < p < 1. The argument
eventually culminates in a pretty theorem from measure theory (Theorem 4.2) that can be
understood at the level of a ﬁrst course on that subject.
2. Banach Spaces and Beyond
In this section, to provide some context, we recall some basic classes of vector spaces that
are important in analysis.
Throughout, our vector spaces are real vector spaces. All that we say would go through
with minimal change to complex vector spaces.
Deﬁnition 2.1. A norm on a vector space V is a function || · ||: V →R satisfying
• ||v|| ≥0, with equality if and only if v = 0,
• ||v + w|| ≤||v|| + ||w|| for all v and w in V .
• ||cv|| = |c|||v|| for all scalars c and v ∈V .
Given a norm on a vector space, we get a metric by d(v, w) = ||v −w||.
Example 2.2. On Rn, we have the sup-norm |x|sup = max1≤i≤n |xi| and the L2-norm
|x|2 = x · x = (Pn
i=1 |xi|2)1/2. The metric coming from the L2-norm is the usual notion of
distance on Rn. The metric on Rn coming from the sup-norm has balls that are actually
cubes. These two norms give rise to the same topology on Rn. Actually, all norms on Rn
give it the same topology.1
Example 2.3. The space C[0, 1] of continuous real-valued functions on [0, 1] has the sup-
norm |f|sup = supx∈[0,1] |f(x)| and the L2-norm |f|2 = (
R 1
0 |f(x)|2 dx)1/2. While functions
that are close in the sup-norm are close in the L2-norm, the converse is false: a function
whose graph is close to the x-axis except for a tall thin spike is near 0 in the L2-norm but
not in the sup-norm.
1See Theorem 2.7 in https://kconrad.math.uconn.edu/blurbs/topology/finite-dim-TVS.pdf.
1

<!-- page 2 -->
2
KEITH CONRAD
Deﬁnition 2.4. A Banach space is a vector space V equipped with a norm || · || such that,
with respect to the metric deﬁned by d(v, w) = ||v −w||, V is complete.
Example 2.5. Under either norm in Example 2.2, Rn is a Banach space.
Example 2.6. In the sup-norm, C[0, 1] is a Banach space (convergence in the sup-norm is
exactly the concept of uniform convergence). But in the L2-norm, C[0, 1] is not a Banach
space. That is, C[0, 1] is not complete for the L2-norm.
Deﬁnition 2.7. For a Banach space V , its dual space is the space of continuous linear
functionals V →R, and is denoted V ∗.
Continuity is important. We do not care about arbitrary linear functionals (as in linear
algebra), but only those that are continuous. One of the important features of a Banach
space is that we can use continuous linear functionals to separate points.
Theorem 2.8. Let V be a Banach space. For each non-zero v ∈V , there is a ϕ ∈V ∗such
that ϕ(v) ̸= 0. Thus, given distinct v and w in V , there is a ϕ ∈V ∗such that ϕ(v) ̸= ϕ(w).
Theorem 2.8 is a special case of the Hahn-Banach theorem, and can be found in texts on
functional analysis. Even this special case can’t be proved in a constructive way (when V
is inﬁnite-dimensional). Its general proof depends on the axiom of choice.
Example 2.9. On C[0, 1], the evaluation maps ea : f 7→f(a), for a ∈R, are linear func-
tionals. Since |f(a)| ≤|f|sup, each ea is continuous for the sup-norm. If f ̸= 0 in C[0, 1],
there is some a such that f(a) ̸= 0, and then ea(f) = f(a) ̸= 0.
Using the sup-norm topology on C[0, 1], the dual space C[0, 1]∗is the space of bounded
Borel measures (or Riemann-Stieltjes integrals) on [0, 1], with the evaluation maps ea cor-
responding to point masses.
Deﬁnition 2.10. A topological vector space is a (real) vector space V equipped with a
Hausdorﬀtopology in which addition V × V →V and scalar multiplication R × V →V
are continuous.
Note the Hausdorﬀcondition is part of the deﬁnition. We won’t be using non-Hausdorﬀ
spaces.
Example 2.11. For n ≥1, the usual topology on Rn makes it a topological vector space.
Using instead the discrete topology, indicated by writing Rn
d, does not make a topological
vector space: for nonzero v0 in Rn
d, {v0} is open and scalar multiplication R × {v0} →Rn
is continuous, so the inverse image of {v0} in R × {v0} is open. That is {(1, v0)}, and
R × {v0} is homeomorphic to R, so {1} is open in R, which is not true. In fact, the usual
topology on Rn is the only Hausdorﬀtopology that makes it a topological vector space2
and the only topological vector space over R with the discrete topology is the zero space3.
Example 2.12. Every Banach space is a topological vector space.
Deﬁnition 2.13. A subset of a vector space is called convex if, for all v and w in the subset,
the line segment tv + (1 −t)w, for 0 ≤t ≤1, is in the subset.
More generally, if a subset is convex and v1, . . . , vm are in the subset, then every weighted
sum Pm
i=1 civi with ci ≥0 and Pm
i=1 ci = 1 is in the subset. In particular, the subset contains
the average (1/m) Pm
i=1 vi.
2See Theorem 2.7 in https://kconrad.math.uconn.edu/blurbs/topology/finite-dim-TVS.pdf.
3See https://math.stackexchange.com/questions/492483.

<!-- page 3 -->
Lp-SPACES FOR 0 < p < 1
3
Deﬁnition 2.14. A topological vector space is called locally convex if the convex open sets
are a base for the topology: given an open set U around a point, there is a convex open set
C containing that point such that C ⊂U.
Example 2.15. Every Banach space is locally convex, since all open balls are convex. This
follows from the deﬁnition of a norm.
Since topological vector spaces are homogeneous (we can use addition to translate neigh-
borhoods around one point to neighborhoods around other points), the locally convex con-
dition can be checked by focusing at the origin: the open sets around 0 need to contain a
basis of convex open sets.
Example 2.16. The space C(R) of continuous real-valued functions on R does not have
the sup-norm over all of R as a norm: a continuous function on R could be unbounded.
But C(R) can be made into a locally convex topological vector space as follows. For each
positive integer n, deﬁne a “semi-norm” | · |n by
|f|n = sup
|x|≤n
|f(x)|.
This is just like a norm, except it might assign value 0 to a non-zero function. That is,
a function could vanish on [−n, n] without vanishing everywhere. Of course, if we take n
large enough, a non-zero continuous function will have non-zero n-th semi-norm, so the
total collection of semi-norms | · |n as n varies, rather than one particular semi-norm, lets
us distinguish diﬀerent functions from each other. Using these semi-norms, deﬁne a basic
open set around f ∈C(R) to be the set of all functions in C(R) that are close to f in a
ﬁnite number of semi-norms:
U(f; n1, . . . , nr) := {g ∈C(R) : |g −f|n1 < ε, . . . , |g −f|nr < ε}
for some n1, . . . , nr in Z+ and ε > 0. These subsets of C(R) are a basis for a topology on
C(R) that makes it a locally convex topological vector space.
Deﬁnition 2.17. When V is a topological vector space, its dual space V ∗is the space of
continuous linear functionals V →R.
Theorem 2.8 generalizes to all locally convex spaces, as follows.
Theorem 2.18. Let V be a locally convex topological vector space. For distinct v and w in
V , there is a ϕ ∈V ∗such that ϕ(v) ̸= ϕ(w).
Proof. See the chapters on locally convex spaces in [3] or [10].
□
Let’s meet some topological vector spaces that are not locally convex.
Example 2.19. Let L1/2[0, 1] be the set of all measurable functions f : [0, 1] →R such
that
R 1
0 |f(x)|1/2 dx < ∞, with functions equal almost everywhere identiﬁed. (We need to
make such an identiﬁcation, since integration does not distinguish between two functions
that diﬀer on a set of measure 0.)
Deﬁne a metric on L1/2[0, 1] by d(f, g) =
R 1
0 |f(x) −g(x)|1/2 dx. The topology L1/2[0, 1]
has from this metric is not locally convex. To see why, ﬁx an open ball around 0:
(2.1)
BR =

f ∈L1/2[0, 1] :
Z 1
0
|f(x)|1/2 dx < R


<!-- page 4 -->
4
KEITH CONRAD
where R > 0. We will show there is no convex open set around 0 in BR, which violates the
meaning of local convexity.
Suppose there were a convex open set C around 0 contained in BR, so the open ε-ball
around 0 is contained in C for some ε > 0. For n ≥1, select n disjoint intervals in [0, 1]
(they need not cover all of [0, 1]). Call them A1, A2, . . . , An. Set fk = (
ε
2µ(Ak))2χAk, where
µ is Lebesgue measure (so µ(Ak) is simply the length of Ak). Then
R 1
0 |fk(x)|1/2 dx = ε/2,
so every fk is in the open ε-ball around 0 and thus is in C. Since the fk’s are supported on
disjoint intervals in [0, 1], their average gn = (1/n) Pn
k=1 fk satisﬁes
Z 1
0
|gn(x)|1/2 dx =
1
n1/2
n
X
k=1
Z 1
0
|fk(x)|1/2 dx =
1
n1/2 nε
2 = n1/2ε
2
.
We can pick n large enough that n1/2ε/2 > R, which makes gn lie outside BR, so gn ̸∈C.
That contradicts the convexity of C.
Example 2.20. For 0 < p < 1, let Lp[0, 1] be the set of all functions f : [0, 1] →R that
are measurable and satisfy
R 1
0 |f(x)|p dx < ∞, with functions equal almost everywhere
identiﬁed. We deﬁne a metric on Lp[0, 1] by d(f, g) =
R 1
0 |f(x)−g(x)|p dx, and Lp[0, 1] with
the topology from this metric is not locally convex by exactly the same argument as in the
previous example (where p = 1/2). Indeed, in that example replace the exponent 1/2 in
the deﬁnition of fk with p, and at the end you’ll get
R 1
0 |gn(x)|p dx = n1−pε/2. This can be
made arbitrarily large by using large enough n, since 1 −p > 0, no open ball around 0 in
Lp[0, 1] contains a convex open set around 0.
This method of constructing topological vector spaces that are not locally convex is due
to Tychonoﬀ[11, pp. 768–769]. He used the space ℓ1/2 = {(xi) : P
i≥1
√xi < ∞} rather
than the function space L1/2[0, 1].
One can’t push a result like Theorem 2.18 to all topological vector spaces, as the next
result [4, Theorem 1] vividly illustrates.
Theorem 2.21. For 0 < p < 1, Lp[0, 1]∗= {0}. That is, the only continuous linear map
Lp[0, 1] →R is 0.
Proof. We argue by contradiction. Assume there is ϕ ∈Lp[0, 1]∗with ϕ ̸= 0. Then ϕ has
image R (a nonzero linear map to a one-dimensional space is surjective), so there is some
f ∈Lp[0, 1] such that |ϕ(f)| ≥1.
Using this choice of f, map [0, 1] to R by
s 7→
Z s
0
|f(x)|p dx.
This is continuous, so there is some s between 0 and 1 such that
(2.2)
Z s
0
|f(x)|p dx = 1
2
Z 1
0
|f(x)|p dx > 0.
Let g1 = fχ[0,s] and g2 = fχ(s,1], so f = g1 + g2 and |f|p = |g1|p + |g2|p. So
Z 1
0
|g1(x)|p dx =
Z s
0
|f(x)|p dx = 1
2
Z 1
0
|f(x)|p dx,

<!-- page 5 -->
Lp-SPACES FOR 0 < p < 1
5
hence
R 1
0 |g2(x)|p dx = 1
2
R 1
0 |f(x)|p dx. Since |ϕ(f)| ≥1, |ϕ(gi)| ≥1/2 for some i. Let
f1 = 2gi, so |ϕ(f1)| ≥1 and
R 1
0 |f1(x)|p dx = 2p R 1
0 |gi(x)|p dx = 2p−1 R 1
0 |f(x)|p dx. Note
2p−1 < 1 since p < 1.
Iterate this to get a sequence {fn} in Lp[0, 1] such that |ϕ(fn)| ≥1 and
d(fn, 0) =
Z 1
0
|fn(x)|p dx = (2p−1)n
Z 1
0
|f(x)|p dx →0,
which contradicts the continuity of ϕ.
□
3. More Spaces with Dual Space 0
We recall the deﬁnition of Lp-spaces for a measure space and then extend Theorem 2.21
quite generally.
Deﬁnition 3.1. Let (X, M, µ) be a measure space. For p > 0, set
Lp(µ) def
={f : X →R : f measurable and
Z
X
|f|p dµ < ∞},
with functions that are equal almost everywhere being identiﬁed with one another.
The metric used on Lp(µ) is
d(f, g) =
( R
X |f −g|p dµ
1/p ,
if p ≥1,
R
X |f −g|p dµ,
if 0 < p < 1.
The reason for these choices, and a discussion of common properties of Lp(µ) for all p > 0,
is discussed in the appendix.
The spaces Lp(µ) for p ≥1 have their metric coming from a norm, so they are locally
convex. We saw in Examples 2.19 and 2.20 that, for 0 < p < 1, Lp[0, 1] is not locally convex.
For a measure space (X, M, µ) and 0 < p < 1, is Lp(µ) ever locally convex?
Theorem 3.2. For 0 < p < 1, Lp(µ) is locally convex if and only if the measure µ assumes
ﬁnitely many values.
Proof. If µ takes ﬁnitely many values, then X is the disjoint union of ﬁnitely many atoms,
say B1, . . . , Bm. A measurable function is constant almost everywhere on each atom, so
Lp(µ) is topologically just Euclidean space (of dimension equal to the number of atoms of
ﬁnite measure), which is locally convex.
Now assume µ takes inﬁnitely many values. We will extend the idea from Example 2.19
to show Lp(µ) is not locally convex.
Since µ has inﬁnitely many values, there is a sequence of subsets Yi ⊂X such that
0 < µ(Y1) < µ(Y2) < . . . .
From the sets Yi, we can construct recursively a sequences of disjoint sets Ai such that
µ(Ai) > 0.
Fix ε > 0. Let fk = (ε/µ(Ak))1/pχAk, so
R
X |fk|p dµ = ε. If Lp(µ) is locally convex, then
every open set around 0 contains a convex open set around 0, which in turn contains some
ε-ball (and thus every fk). We will show an average of enough fk’s is arbitrarily far from 0
in the metric on Lp(µ), and that will contradict local convexity.
Let gn =
1
n
Pn
k=1 fk.
Since the fk’s are supported on disjoint sets,
R
X |gn|p dµ =
1
np
Pn
k=1 ε = εn1−p.
Since p < 1, εn1−p becomes arbitrarily large as n →∞.
Thus,
Lp(µ) is not locally convex.
□

<!-- page 6 -->
6
KEITH CONRAD
In Theorem 2.21, we saw Lp[0, 1]∗= {0}. Is the dual of Lp(µ), for general measure spaces
and 0 < p < 1, also {0} (when Lp(µ) is not locally convex)?
First we treat the boring case.
Theorem 3.3. If the measure µ contains an atom with ﬁnite measure, then Lp(µ)∗̸= {0}.
Proof. Let B be an atom with ﬁnite measure. Every measurable function f : X →R is
constant almost everywhere on B. Call the almost-everywhere common value ϕ(f). The
reader can check ϕ is a non-zero continuous linear functional on Lp(µ).
□
Example 3.4. For 0 < p < 1 the sequence space ℓp = Lp(N), where N has counting
measure, is not locally convex by Theorem 3.2 and has nonzero dual space by Theorem 3.3.
In fact (ℓp)∗is ℓ∞, where a sequence y ∈ℓ∞acts on ℓp by ϕy(x) = P
n≥1 xnyn: for a proof,
see [4, Theorem 6] or https://math.stackexchange.com/questions/1258557/.
Atoms with inﬁnite measure are invisible as far as integration is concerned (integrable
functions must vanish on them), so we may assume our measure space has no atoms of
inﬁnite measure.
What remains is the case of a nonatomic measure, and Theorem 2.21 generalizes to this
case as follows.
Theorem 3.5. If (X, M, µ) is a nonatomic measure space and 0 < p < 1, then Lp(µ)∗= 0.
Let’s try to prove Theorem 3.5 by understanding more conceptually the proof that
Lp[0, 1]∗= 0. To make that proof work in the setting of Theorem 3.5, suppose there is
a non-zero ϕ ∈Lp(µ)∗. Then, by scaling, there is an f ∈Lp(µ) such that |ϕ(f)| ≥1. We’d
it like to ﬁnd some A ∈M such that
(3.1)
Z
A
|f|p dµ = 1
2
Z
X
|f|p dµ.
Then set g1 = fχA and g2 = fχX−A, and repeating the ideas of the proof of Theorem 2.21
will eventually yield a contradiction, so Lp(µ)∗= 0.
But how do we construct A (depending on f) that makes (3.1) correct? When X = [0, 1],
as in Theorem 2.21, we considered the collection of integrals
Z s
0
|f|p dx
as s runs from 0 to 1. These are integrals over the sets [0, s], which can be thought of as a
“path” of intervals in the space of measurable subsets of [0, 1], starting with {0} and ending
with the whole space [0, 1]. The Intermediate Value Theorem helped us ﬁnd an s such that
R s
0 |f|p dx = (1/2)
R 1
0 |f|p dx.
To extend this idea to a measure space (X, M, µ) in place of [0, 1], note M can topologized
by the semi-metric dµ(A, B) = µ(A∆B), where ∆is the symmetric diﬀerence operation:
(3.2)
A∆B = A ∪B −A ∩B
(For instance, dµ(A, ∅) = µ(A).) With this metric, integration over measurable subsets of
X deﬁnes a function M →R by
(3.3)
νf(A) =
Z
A
|f|p dµ,
that is continuous.

<!-- page 7 -->
Lp-SPACES FOR 0 < p < 1
7
For each f ∈Lp(µ), suppose we can ﬁnd a path (continuous function) h: [0, 1] →M,
depending on f, such that
(3.4)
Z
h(0)
|f|p dµ = 0,
Z
h(1)
|f|p dµ =
Z
X
|f|p dµ.
Then composing h with νf gives the function
s 7→
Z
h(s)
|f|p dµ,
which is continuous from [0, 1] to R. We can apply the Intermediate Value Theorem to this
continuous function of s and thus ﬁnd an s such that
R
h(s) |f|p dµ = (1/2)
R
X |f|p dµ.
However, we haven’t explained how to construct a path in M satisfying (3.4). It is not
clear (to me) how to deﬁne such a path in M in general. We will use another approach, but
will return to this path idea at the end of the paper.
The key step to ﬁnish this proof of Theorem 3.5 is to reformulate the problem more
directly in terms of pure measure theory.
4. Values of a Measure
We start with a nonatomic measure space (X, M, µ), and p ∈(0, 1). For each f ∈Lp(µ),
the map νf : M →R given by (3.3) deﬁnes a ﬁnite measure on X (even if µ(X) = ∞). We
want to ﬁnd an A ∈M such that νf(A) = (1/2)νf(X), i.e., A cuts X in half as far as νf is
concerned.
Notice that νf depends not so much on f, but on |f|p, and this is a function in L1(µ, R).
Lemma 4.1. If (X, M, µ) is a nonatomic measure space, then for nonnegative F ∈L1(µ, R),
F dµ is a ﬁnite nonatomic measure.
Proof. Without loss of generality,
R
X F dµ > 0. Since F is measurable,
Z
X
F dµ =
sup
0≤g≤F
Z
X
g dµ,
where the sup is over simple g. For 0 ≤g ≤F, g is a step map, say
g =
X
αiχAi
with αi ≥0 and 0 < µ(Ai) < ∞.
Assume F dµ has an atom A, so ε =
R
A F dµ > 0 and for B ⊂A,
R
B F dµ = 0 or ε. Our
goal is to get the contradiction
R
A F dµ = 0. Since A is an atom for FχA, without loss of
generality F = 0 oﬀof A, so Ai ⊂A for all i. The continuity of integration as a function of
the set implies
lim
µ(B)→0
Z
B
F dµ = 0.
Since µ is nonatomic and 0 < µ(Ai) < ∞, Ai contains a subset B with arbitrarily small
positive measure. For such B,
R
B F dµ = 0 since B ⊂Ai ⊂A. Therefore
R
B g dµ = 0, so
g = 0 almost everywhere on B, so αi = 0 since µ(B) > 0. This is true for all i, so g = 0.
Thus
R
X F dµ = 0, so
R
A F dµ = 0, a contradiction.
□
Thus, for f ∈Lp(µ), the measure νf in (3.3) is a ﬁnite nonatomic measure on X.

<!-- page 8 -->
8
KEITH CONRAD
Theorem 4.2. If (X, M, ν) is a ﬁnite nonatomic measure space, then for all t in [0, ν(X)]
there is some A ∈M such that ν(A) = t.
Before proving Theorem 4.2, we note that Lemma 4.1 and Theorem 4.2 help us ﬁll in the
hole in our proof of Theorem 3.5. Indeed, when (X, M, µ) is nonatomic and f ∈Lp(µ, R),
Lemma 4.1 tells us |f|p dµ is a ﬁnite nonatomic measure on X, and Theorem 4.2 then tells
us there is an A ∈M such that
R
A |f|p dµ = 1
2
R
X |f|p dµ. Using this result and iteration,
we can show Lp(µ)∗= 0 for 0 < p < 1 by the ideas in the proof of Theorem 2.21.
Remark 4.3. There are theorems that say a ﬁnite nonatomic measure space (X, M, ν)
often looks like the Borel measurable subsets of [0, ν(X)] with Lebesgue measure. Then
the element of M corresponding to [0, t] solves Theorem 4.2. However, such theorems need
X or M to be suitable separable metric spaces. For our purposes, we do not need such
hypotheses, since all we are asking about is the set of values of the measure ν, not the
structure of X or M.
The proof of Theorem 4.2 we now give is taken from [9, Exercise 18-28, p. 247].
Proof. Let S1 = {A ∈M : ν(A) < t}. Choose A1 ∈S1 such that ν(A1) > sup{ν(A) : A ∈
S1} −1.
Let S2 = {A ∈M : ν(A) < t, A1 ⊂A}. Choose A2 ∈S2 such that ν(A2) > sup{ν(A) :
A ∈S2} −1/2.
Assuming Sn is deﬁned, choose An ∈Sn such that
ν(An) > sup{ν(A) : A ∈Sn} −1/n.
Then let Sn+1 = {A ∈M : ν(A) < t, An ⊂A}.
Now we have A1 ⊂A2 ⊂A3 ⊂· · · ⊂X. Deﬁne
A∞= ∪An ∈M,
so
(4.1)
ν(A∞) = lim ν(An) ≤t.
The rest of the proof is devoted to showing ν(A∞) = t.
If A∞⊂A and ν(A) < t, then A ∈Sn+1.
Thus ν(An+1) > ν(A) −1/(n + 1), so
ν(A∞) ≥ν(A), so ν(A) = ν(A∞).
We have shown ν(A∞) ≤t and a measurable set
containing A∞has measure ν(A∞) if its measure is less than t.
Having constructed A∞by a recursion from below, we now approach A∞by a recursion
from above. Let T1 = {B ∈M : ν(B) > t, A∞⊂B}. (For instance, X ∈T1.) Choose
B1 ∈T1 such that
ν(B1) < inf{ν(B) : B ∈T1} + 1.
Let T2 = {B ∈M : ν(B) > t, A∞⊂B ⊂B1}. If Tn is deﬁned, choose Bn ∈Tn such that
ν(Bn) < inf{ν(B) : B ∈Tn} + 1/n.
Let Tn+1 = {B ∈M : ν(B) > t, A∞⊂B ⊂Bn}. Repeat this for all n, so
A∞⊂· · · ⊂B3 ⊂B2 ⊂B1.
Let B∞= ∩Bn ∈M, so
(4.2)
ν(B∞) = lim ν(Bn) ≥t.
If A∞⊂B ⊂B∞and ν(B) > t, then B ∈Tn+1, so
ν(Bn+1) < ν(B) + 1/(n + 1),

<!-- page 9 -->
Lp-SPACES FOR 0 < p < 1
9
so ν(B∞) ≤ν(B), so ν(B) = ν(B∞).
Putting together what we have found for sets between A∞and B∞,
A∞⊂A, ν(A) < t =⇒ν(A) = ν(A∞),
A∞⊂B ⊂B∞, ν(B) > t =⇒ν(B) = ν(B∞).
We use this to show ν(B∞−A∞) = 0, which implies ν(A∞) = t and will ﬁnish the proof.
Notice we have yet to use the fact that ν is nonatomic.
Let Y ⊂B∞−A∞, so
A∞⊂Y ∪A∞⊂B∞,
Y ∩A∞= ∅.
If ν(Y ∪A∞) < t then ν(Y ∪A∞) = ν(A∞), so ν(Y ) = 0. If ν(Y ∪A∞) > t then ν(Y ∪A∞) =
ν(B∞), so ν(Y ) = ν(B∞−A∞). Thus, every measurable subset of B∞−A∞has measure
0, ν(B∞−A∞), or t−ν(A∞). Since ν is nonatomic, we conclude that ν(B∞−A∞) = 0.
□
For an alternate proof of Theorem 4.2, see [5, Lemma 2]. For an extension of Theorem
4.2 to vector-valued measures, see [6].
This completes a proof that, for 0 < p < 1, Lp-spaces of a nonatomic measure space
have zero dual space. The machinery of functional analysis is built on the Hahn-Banach
Theorem, so how can we study these kinds of Lp-spaces, or more generally a topological
vector space that is not locally convex? See [1].
5. Theorem 4.2 Using Convexity
We now give a second proof of Theorem 4.2 (which will give a second proof that Lp(µ)∗=
{0} when µ is nonatomic) based on an abstract convexity property for the measurable
subsets of a ﬁnite nonatomic measure space. The idea we use is brieﬂy indicated in [7,
Exercise 41.2, p. 174].
Start with a ﬁnite measure space (M, ν). (For instance, (M, µ) is a measure space and
ν = F dµ for some nonnegative F ∈L1(µ).) A metric can be introduced on (M, ν) by
dν(A, B) = ν(A∆B),
where ∆is the symmetric diﬀerence (see (3.2)). Here it is crucial that ν is a ﬁnite measure,
or this metric is not always deﬁned. Actually, dν is only a semimetric, so we look at M, the
metric space coming from M after elements at distance zero from one another are identiﬁed.
Step 1: The space M is complete.
Let {An} be dν-Cauchy sequence. Then (in fact, equivalently) {χAn} is an L1-Cauchy
sequence in L1(ν). Let f be an L1-limit of this sequence of characteristic functions. A
subsequence converges pointwise almost everywhere to f, so the set {x : f(x) = 1} is a
limit of {An} in M.
Step 2: Call a metric space (M, ρ) convex if for all x ̸= y in X there is some z ̸= x, y in M
such that ρ(x, y) = ρ(x, z) + ρ(z, y). Note such a z need not be uniquely determined by the
two distances ρ(x, z) and ρ(z, y). For example, take M = S2 with its surface metric, x the
north pole, y the south pole, and z an arbitrary point along a chosen latitude of M. (When
M ⊂Rn, this deﬁnition of convex might not match the usual notion: an open star-shaped
region in Rn is not convex in the usual sense but is convex in the abstract sense above.
However, for closed subsets of Rn using the induced metric from Rn, the above notion of
convex does match the usual meaning of the term.)
We show that (M, dν) is convex if (and only if!) ν is nonatomic.

<!-- page 10 -->
10
KEITH CONRAD
If M is convex and ν(A) > 0, so dν(A, ∅) > 0, then there exists a C such that dν(A, C) > 0,
dν(C, ∅) > 0, and dν(A, ∅) = dν(A, C) + dν(C, ∅). That is
ν(A∆C) > 0, ν(C) > 0, ν(A) = ν(A∆C) + ν(C).
Therefore ν(A∆C) = ν(A) −ν(C) > 0, so ν(C −A) = 0, so ν(C) = ν(A ∩C). This
implies 0 < ν(A ∩C) < ν(A). Since A ∩C ⊂A, this shows ν is nonatomic.
Conversely, if dν(A, B) > 0, we want to ﬁnd C such that dν(A, C) and dν(C, B) are both
positive and
dν(A, B) = dν(A, C) + dν(B, C),
that is
ν(A∆B) = ν(A∆C) + ν(B∆C).
If ν(A) or ν(B) is less than or equal to ν(A ∩B) (so A ⊂B or B ⊂A up to measure
zero), say ν(A) ≤ν(A ∩B). Then ν(A) = ν(A ∩B) and ν(B) = ν(A ∪B), so ν(A∆B) =
ν(B) −ν(A) > 0.
Choose Y ⊂B −A such that 0 < ν(Y ) < ν(B) −ν(A) and let C = Y ∪(A ∩B). Then
ν(A∆C) = ν(A) −ν(A ∩B) + ν(Y ) = ν(Y ) > 0,
ν(B∆C) = ν(B) −ν(A ∩B) −ν(Y ) = ν(B) −ν(A) −ν(Y ) > 0,
so
ν(A∆C) + ν(B∆C) = ν(B) −ν(A) = ν(A∆B).
If ν(A), ν(B) > ν(A ∩B), let C1 ⊂A −A ∩B and C2 ⊂B −A ∩B such that
0 < ν(C1) < ν(A) −ν(A ∩B),
0 < ν(C2) < ν(B) −ν(A ∩B).
Set C = C1 ∪C2 ∪(A ∩B). Then
A∆C = (A −C1 −A ∩B) ∪(B ∩C2), B∆C = (B −C2 −A ∩B) ∪(A ∩C1),
so
ν(A∆C) = ν(A) −ν(C1) −ν(A ∩B) + ν(C2) > ν(C2) > 0,
ν(B∆C) = ν(B) −ν(C2) −ν(A ∩B) + ν(C1) > ν(C1) > 0,
so
ν(A∆C) + ν(B∆C) = ν(A ∪B) −ν(A ∩B) = ν(A∆B).
Step 3: The ﬁnal step will actually be a generalization of Theorem 4.2 to metric spaces.
The application to (M, dν) for nonatomic ν will come by setting x = ∅and y = X in the
next claim.
Claim: For a complete convex metric space (M, ρ) and distinct points x and y in M with
0 ≤t ≤ρ(x, y), there is a z such that ρ(x, z) = t (and ρ(x, y) = ρ(x, z) + ρ(z, y)).
The proof of this claim will be a tortuous Zorniﬁcation.
First we deﬁne some notation. For a, b ∈M, let
[a, b] def
={c ∈M : ρ(a, b) = ρ(a, c) + ρ(c, b)}.
For instance, this set contains a and b. Intuitively, this is the set of points lying on geodesics
from a to b. It is helpful when reading the following discussion to draw many pictures of
line segments with points marked on them. Given t between 0 and ρ(x, y), we will ﬁnd a
z ∈[x, y] with ρ(x, z) = t.
Some simple properties of these “intervals” are:
(1) [a, b] = [b, a].

<!-- page 11 -->
Lp-SPACES FOR 0 < p < 1
11
(2) If c ∈[a, b] and b ∈[a, c], then ρ(b, c) = −ρ(b, c), so b = c.
Less simple properties are
(3) If b ∈[a, c] then [a, b], [b, c] ⊂[a, c].
(4) If b ∈[a, d] and c ∈[b, d] then [a, c], [b, d] ⊂[a, d] and [b, c] = [a, c] ∩[b, d] ⊂[a, d].
(We will only need that [b, c] lies in the intersection, not equality.)
Proof of (3): Without loss of generality, we show [a, b] ⊂[a, c]. For x in [a, b],
ρ(a, c) ≤ρ(a, x) + ρ(x, c)
≤ρ(a, x) + ρ(x, b) + ρ(b, c)
= ρ(a, b) + ρ(b, c)
= ρ(a, c).
Therefore x ∈[a, c].
Proof of (4): By (3), [b, d] ⊂[a, d] and [b, c] ⊂[b, d]. Therefore c ∈[a, d], so [a, c] ⊂[a, d],
so
ρ(a, d) = ρ(a, c) + ρ(c, d)
≤ρ(a, b) + ρ(b, c) + ρ(c, d)
= ρ(a, b) + ρ(b, d)
= ρ(a, d).
Therefore the inequality is an equality, so b ∈[a, c], so [b, c] ⊂[a, c]. Thus [b, c] ⊂[a, c]∩[b, d].
For the reverse inclusion, let x ∈[a, c] ∩[b, d]. Then
ρ(a, d) = ρ(a, b) + ρ(b, d)
= ρ(a, b) + ρ(b, c) + ρ(c, d)
≤ρ(a, b) + ρ(b, x) + ρ(x, c) + ρ(c, d)
= ρ(a, b) + ρ(b, d) −ρ(x, d) + ρ(a, c) −ρ(a, x) + ρ(c, d)
= 2ρ(a, d) −ρ(x, d) −ρ(a, x).
Rearranging terms, ρ(a, x) + ρ(x, d) ≤ρ(a, d), so there is equality throughout, so ρ(b, c) =
ρ(b, x) + ρ(x, c). Thus x ∈[b, c].
Now we are ready to investigate “geodesics” on M. For our ﬁxed x ∈M introduced in
the statement of Step 3, deﬁne a partial ordering on M that might be called “closer to x
on geodesics” by
z1 ≤z2 if and only if z1 ∈[x, z2].
In particular, z1 ≤z2 implies ρ(x, z1) ≤ρ(x, z2).
Let’s check this is a partial ordering.
If z1 ≤z2 and z2 ≤z1, then z1 ∈[x, z2] and z2 ∈[x, z1], so z1 = z2 by (2).
If z1 ≤z2 and z2 ≤z3 then z1 ∈[x, z2] and z2 ∈[x, z3]. By (1), z2 ∈[z3, x] and z1 ∈[z2, x].
Therefore by (4),
z1 ∈[z1, z2] ⊂[x, z3],
hence z1 ≤z3.
Deﬁne
A = {z ∈[x, y] : ρ(x, z) ≤t}.

<!-- page 12 -->
12
KEITH CONRAD
This set is nonempty, since it contains x. We want to apply Zorn’s Lemma to A with its
induced partial ordering and show a maximal element of A has distance t from x.
Let {zi}i∈I be a totally ordered subset of A. We want an upper bound. Let
s = sup
i∈I
ρ(x, zi) ≤t.
For ε > 0, there is some i0 such that
s −ε ≤ρ(x, zi0) ≤s,
so
s −ε ≤ρ(x, zi) ≤s
for all i ≥i0. For i0 ≤i ≤j, s −ε ≤ρ(x, zi) ≤s and
s −ε ≤ρ(x, zj) = ρ(x, zi) + ρ(zi, zj) ≤s
so ρ(zi, zj) ≤ε. Thus {zi} is a Cauchy net, so has a limit ℓby completeness of M. We
show this limit is an upper bound in A.
Taking limits,
ρ(x, y) = ρ(x, zi) + ρ(zi, y) =⇒ρ(x, y) = ρ(x, ℓ) + ρ(ℓ, y)
ρ(x, zi) ≤t =⇒ρ(x, ℓ) ≤t.
Thus ℓ∈A.
For i ≤j,
ρ(x, zj) = ρ(x, zi) + ρ(zi, zj).
Taking limits over j,
ρ(x, ℓ) = ρ(x, zi) + ρ(zi, ℓ),
so zi ∈[x, ℓ], so zi ≤ℓfor all i.
We have justiﬁed an application of Zorn’s Lemma to A. Let m be a maximal element.
That is, m ∈A, and if z ∈A with m ∈[x, z] then z = m.
Let B = {z ∈[y, m] : ρ(y, z) ≤ρ(x, y) −t}. Since y ∈B, B is nonempty. Our goal is to
show m ∈B, which is not obvious. Note that the deﬁnition of B depends on the existence
of a maximal element of A.
In B, introduce a partial ordering by z1 ≤z2 when z1 ∈[y, z2].
As above, B has a maximal element, m′. Since m ∈[x, y] and m′ ∈[m, y], we get by (4)
that
[m, m′] ⊂[x, m′] ∩[m, y] ⊂[x, y].
For z ∈[m, m′],
z ∈[x, y] =⇒ρ(x, y) = ρ(x, z) + ρ(y, z)
=⇒ρ(x, z) ≤t or ρ(y, z) ≤ρ(x, y) −t
=⇒z ∈A or z ∈B.
Also,
ρ(x, y) = ρ(x, z) + ρ(z, y)
≤ρ(x, m) + ρ(m, z) + ρ(z, y)
= ρ(x, m) + ρ(m, y) since z ∈[m, y]
= ρ(x, y) since m ∈[x, y].
Therefore ρ(x, z) = ρ(x, m) + ρ(m, z), so m ∈[x, z].

<!-- page 13 -->
Lp-SPACES FOR 0 < p < 1
13
We now have
ρ(x, y) = ρ(x, z) + ρ(z, y) since z ∈[x, y]
≤ρ(x, z) + ρ(z, m′) + ρ(m′, y)
= ρ(x, m′) + ρ(m′, y) since z ∈[x, m′]
= ρ(x, y) since m′ ∈[x, y].
Therefore ρ(y, z) = ρ(z, m′) + ρ(m′, y), so m′ ∈[y, z].
Thus if z ∈A, then m ∈[x, z] ⇒z = m. If z ∈B, then m′ ∈[y, z] ⇒z = m′. Therefore
[m, m′] = {m, m′}, so by convexity of M, m = m′, hence m ∈A ∩B. Therefore ρ(x, m) ≤t
and ρ(y, m) ≤ρ(x, y) −t, so
ρ(x, y) = ρ(x, m) + ρ(m, y) ≤ρ(x, y),
so ρ(x, m) = t. This concludes our second proof of Theorem 4.2.
6. Paths Linking Measurable Sets
Returning to the original idea of showing Lp(µ) has zero dual space (for nonatomic µ)
by ﬁnding a path in the space of measurable sets, the following possibility suggests itself.
Let (M, ρ) be a complete convex metric space. (Our second proof of Theorem 4.2 gives us
the motivating example.) Is M path connected? To try to show this, recall that we’ve seen
that for distinct x, y in M and 0 ≤t ≤ρ(x, y), there is zt ∈[x, y] such that ρ(x, zt) = t.
Perhaps if ρ(x, y) is small enough, each zt is unique, and this would let us construct paths
in M. For a proof that every complete convex metric space is path connected, see [2, Thm.
14.1, p. 41].
Appendix A. Analogies between p ≥1 and 0 < p < 1
In this appendix, we summarize common features of Lp(µ) for all p > 0.
Every Lp(µ) is a vector space. Closure under scaling is trivial. For closure under addition,
ﬁrst note that
|f(x) + g(x)| ≤|f(x)| + |g(x)| =⇒|f(x) + g(x)|p ≤(|f(x)| + |g(x)|)p
since the p-th power is increasing on [0, ∞) for all p > 0. Now we argue separately for p ≥1
and 0 < p < 1. When p ≥1, non-negative numbers a and b satisfy
(A.1)
(a + b)p ≤2pap + 2pbp
since a + b ≤2 max(a, b). Since |f(x) + g(x)| ≤|f(x)| + |g(x)|,
|f(x) + g(x)|p ≤(|f(x)| + |g(x)|)p ≤2p|f(x)|p + 2p|g(x)|p,
by (A.1), so
R
X |f + g|p dµ ≤2p R
X |f|p dµ + 2p R
X |g|p dµ < ∞. When 0 < p < 1 and a and
b are non-negative numbers,
(A.2)
(a + b)p ≤ap + bp.
Again starting from |f(x) + g(x)| ≤|f(x)| + |g(x)|,
(A.3)
|f(x) + g(x)|p ≤(|f(x)| + |g(x)|)p ≤|f(x)|p + |g(x)|p,
by (A.2), so
(A.4)
Z
X
|f + g|p dµ ≤
Z
X
|f|p dµ +
Z
X
|g|p dµ < ∞.

<!-- page 14 -->
14
KEITH CONRAD
For all p > 0, set
(A.5)
|f|p
def
=
Z
X
|f|p dµ
1/p
.
When f = g almost everywhere, |f|p = |g|p, so | · |p is well-deﬁned on Lp(µ).
For p ≥1, | · |p on Lp(µ) satisﬁes the triangle inequality:
|f + g|p ≤|f|p + |g|p.
This is called the Minkowski inequality for Lp-functions. It shows | · |p is a norm on Lp(µ).
When 0 < p < 1, |·|p in (A.5) has a ﬂipped triangle inequality: |f +g|p ≥|f|p +|g|p when
f and g have nonnegative values.4 For instance, when X = [0, 1] with Lebesgue measure
and p = 1/2, f = χ[0,1/2), and g = χ[1/2,1], we have |f +g|p = 1 and |f|p +|g|p = 21−1/p < 1.
Taking p-th roots in the deﬁnition of | · |p is the source of the problem.
For 0 < p < 1, a modiﬁed triangle inequality on Lp(µ) in the correct direction is
(A.6)
|f + g|p ≤2
1
p−1(|f|p + |g|p),
To prove (A.6), we follow [8, §15.9]. For c > 1, the function (tc + 1)/(t + 1)c for t ≥0 has a
unique minimum at t = 1 (it decreases for t in [0, 1] and increases for t in [1, ∞)). Therefore
(tc + 1)/(t + 1)c ≥21−c, so tc + 1 ≥21−c(t + 1)c. Writing t = a/b for a ≥0 and b > 0 and
multiplying through by bc,
(A.7)
ac + bc ≥21−c(a + b)c, so (a + b)c ≤2c−1(ac + bc).
This is obviously also true when b = 0. In (A.7), let c = 1/p for 0 < p < 1, a =
R
X |f|p dµ,
and b =
R
X |g|p dµ:
Z
X
|f|p dµ +
Z
X
|g|p dµ
1/p
≤2
1
p−1(|f|p + |g|p).
Combining this with (A.4), after taking the p-th root of both sides of (A.4), we get (A.6).
Having the triangle inequality up to a universal scaling factor, as in (A.6), is often
harmless. Alternatively, we could use
R
X |f|p dµ as a notion of distance from 0, without the
p-th root of the integral, since (A.4) shows the triangle inequality is valid for this. This is
the choice that we made earlier. For 0 < p < 1, set the metric on Lp(µ) to be
d(f, g) =
Z
X
|f −g|p dµ.
Whether or not we take the p-th root of
R
X |f −g|p dµ will not change the notion of
convergence on Lp(µ), but at least without the p-th root we get the standard triangle
inequality.
Some properties of the spaces Lp(µ) for p ≥1 are
• A sequence of measurable functions that is Lp-convergent has a subsequence that
converges pointwise almost everywhere.
• Lp(µ) is complete with respect to | · |p, and thus is a Banach space,
• (H¨older’s inequality) If p > 1, and q > 1 is chosen so that 1/p + 1/q = 1, then for
f ∈Lp(µ) and g ∈Lq(µ), the product fg lies in L1(µ) and |fg|1 ≤|f|p|g|q.
• If fn →f in Lp(µ), then |fn|p →|f|p in L1(µ).
4Some constraint on the values of f and g are needed here, since otherwise take g = −f to get 0 ≥
|f|p + |g|p, for f = g = 0 in Lp(µ).

<!-- page 15 -->
Lp-SPACES FOR 0 < p < 1
15
• When X is a locally compact Hausdorﬀspace, and µ is a regular Borel measure on
X, the space Cc(X) (continuous real-valued functions on X with compact support)
is dense in Lp(µ).
Since a 7→ap is an increasing function on [0, ∞) for p > 0, not just for p ≥1, some results
about Lp-spaces when p ≥1 work for 0 < p < 1. Here are some examples.
• For 0 < p < 1, a sequence of measurable functions that is Lp-convergent has a
subsequence that converges pointwise almost everywhere.
• For 0 < p < 1, Lp(µ) is complete.
• If 0 < p < 1 and fn →f in Lp(µ), then |fn|p →|f|p in L1(µ).
• When X is a locally compact Hausdorﬀspace, and µ is a regular Borel measure on
X, the space Cc(X) (continuous real-valued functions on X with compact support)
is dense in Lp(µ) for 0 < p < 1.
Actually, the third item needs a diﬀerent proof in the case 0 < p < 1. (The usual proof
when p > 1 uses H¨older’s inequality, which breaks down for 0 < p < 1.) Here is the proof.
For 0 < p < 1,
|f|p ≤|f −fn|p + |fn|p,
|fn|p ≤|f −fn|p + |f|p,
so
||f|p −|fn|p| ≤|f −fn|p.
Thus
Z
X
||f|p −|fn|p| dµ ≤
Z
X
|f −fn|p dµ →0.
Since, for 0 < p < 1, Lp(µ) is a topological vector space complete with respect to
a metric, we have notions of continuity, completeness, and boundedness here. Therefore
several consequences of the Baire category theorem as applied to Banach spaces carry over
without change to Lp(µ) for 0 < p < 1: the Open Mapping Theorem, the Closed Graph
Theorem, and the Principle of Uniform Boundedness.
References
[1] N. Adasch, B. Ernst, and D. Keim, Topological Vector Spaces. The Theory Without Convexity Conditions,
Lecture Notes in Mathematics 639, Springer-Verlag, New York, 1978.
[2] L. Blumenthal, Theory and Applications of Distance Geometry, Clarendon Press, Oxford, 1953.
[3] J. B. Conway, A Course in Functional Analysis, 2nd ed., Springer Verlag, New York, 1990.
[4] M. M. Day, “The spaces Lp with 0 < p < 1,” Bull. Amer. Math. Soc. 46 (1940), 816–823. URL https://
projecteuclid.org/download/pdf 1/euclid.bams/1183503236.
[5] P. R. Halmos, “On the Set of Values of a Finite Measure,” Bull. Amer. Math. Soc. 53 (1947), 138-141.
[6] P. R. Halmos, “The Range of a Vector Measure,” Bull. Amer. Math. Soc. 54 (1948), 416-421.
[7] P. R. Halmos, Measure Theory, Van Nostrand, New York, 1950.
[8] G. K¨othe, Topological Vector Spaces I, Springer-Verlag, New York, 1969.
[9] W. Pfeﬀer, Integrals and Measures, Marcel Dekker, New York, 1977.
[10] M. Reed and B. Simon, Functional Analysis I, Academic Press, San Diego, 1980.
[11] A. Tychonoﬀ, “Ein Fixpunktsatz,” Math. Ann. 111 (1935), 767–776.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*