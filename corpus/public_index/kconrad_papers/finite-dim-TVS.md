# Finite-Dimensional Topological Vector Spaces

> **Source**: https://kconrad.math.uconn.edu/blurbs/finite-dim-TVS.pdf  
> **Author**: Keith Conrad  
> **Topic**: topology  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
FINITE-DIMENSIONAL TOPOLOGICAL VECTOR SPACES
KEITH CONRAD
1. Introduction
For a real vector space V , a norm ||·|| on V leads to a metric d(v, w) = ||v −w|| and then
to a topology for which vector addition and scalar multiplication on V are both continuous.
If V is ﬁnite-dimensional it can have many diﬀerent norms (such as the Euclidean norm
or sup-norm relative to a basis of V ), but it turns out that all norms on V lead to the
same topology on V . Thus a ﬁnite-dimensional real vector space has a canonical topology,
namely the one coming from a norm on the space (the choice of norm does not matter).
This is not generally true for inﬁnite-dimensional spaces, e.g., on C[0, 1] the sup-norm and
all the Lp-norms for diﬀerent p ≥1 deﬁne diﬀerent topologies.
Another aspect of inﬁnite-dimensional spaces is that there a topology can make vector
addition and scalar multiplication continuous but the topology does not come from a norm.
For example, the usual topology on the Schwartz space S(R) is deﬁned by a countable
family of semi-norms |f|m,n = supx∈R |xmf(n)(x)| for m, n ≥0 but not by one norm.1
Can a ﬁnite-dimensional real vector space have a topology making the vector space op-
erations continuous besides its norm topology? No, and explaining this is our goal.
2. Topological vector spaces and basic properties
Deﬁnition 2.1. A topological vector space over R is an R-vector space V with a Haus-
dorﬀtopology making vector addition V × V →V and scalar multiplication R × V →V
continuous, where V ×V and R×V have the product topology and R has its usual topology.
We will often abbreviate “topological vector space” to TVS, and until Section 4 we will
assume a TVS is a vector space over R.
Example 2.2. Every vector space with a norm on it is a TVS using the topology from that
norm. In particular, we view Rn as a TVS using its norm topology (the usual one).
Example 2.3. The Schwartz space S(R) is a TVS and its topology does not come a norm.
Example 2.4. For n ≥1, is Rn with the discrete topology a TVS? Perhaps surprisingly,
it isn’t. While addition Rn × Rn →Rn is continuous, scalar multiplication R × Rn →Rn
(with the scalar component R having its usual topology) is not continuous: the inverse
image of the open set {0} is N := R × {0} ∪{0} × Rn. If this were open in R × Rn then
it would contain a basic open set around (0, v) for each nonzero v in Rn, but such a basic
open set is U × {v} where U is an open interval around 0 in R and U × {v} is not in N.
Thus a discrete Rn is not a TVS.
If Rn has the discrete topology and scalar multiplication R × Rn →Rn is continuous,
then R must be discrete: for v0 ̸= 0, R × {v0} →Rn by (c, v0) 7→cv0 is continuous and
{cv0} is open, so its inverse image {(c, v0)} is open and R × {v0} is homeomorphic to R.
1This is proved here: https://math.stackexchange.com/questions/2375320.
1

<!-- page 2 -->
2
KEITH CONRAD
Deﬁnition 2.5. If V and W are each a TVS, an isomorphism L: V →W is a continuous
linear bijection such that its inverse is also continuous.
As in abstract algebra, the inverse of a linear bijection is automatically linear, so we did
not include that condition in the deﬁnition of an isomorphism.
Example 2.6. For n ≥2, Rn and Rn−1 × R are isomorphic topological vector spaces by
the meaning of the product topology.
Our aim is to prove the following result, due to Tychonoﬀ[2, pp. 769–770].
Theorem 2.7. For n ∈Z+, each n-dimensional TVS V is isomorphic to Rn with its usual
topology. More precisely, if {e1, . . . , en} is a basis of V then the mapping Rn →V given by
(a1, . . . , an) 7→a1e1 + · · · + anen is a TVS isomorphism.
Since the usual topology on Rn comes from a norm, the isomorphism in Theorem 2.7
shows the topology on V comes from a norm. For the rest of this section we develop some
results that will be used in the proof of Theorem 2.7.
In a TVS V , translation v 7→v + v0 for a ﬁxed v0 ∈V and scaling v 7→a0v for a ﬁxed
nonzero a0 ∈R are both homeomorphisms V →V . In particular, for an open set U ⊂V
containing 0 and an arbitrary v0 ∈V , v0 + U is an open set in V containing v0 and all open
sets in V containing v0 arise in this way: the topology near each point of a TVS looks like
the topology near 0.
Deﬁnition 2.8. Let V be a TVS. A subset B of V is called balanced if
|a| ≤1 =⇒aB ⊂B.
When the topology on V comes from a norm, every open ball centered at the origin is
balanced. In a general TVS there is no metric and therefore no balls, but balanced sets
make sense.
Lemma 2.9. Every open set containing 0 in a TVS contains a balanced open set around 0.
This lemma is obvious when the topology comes from a norm, since we can use open
balls centered at 0 with respect to the norm. Since the lemma tells us that balanced open
sets are a neighborhood basis of 0 in V , they could be considered a replacement for open
balls around 0 in a general TVS.
Proof. Let U be an open set in the TVS V with 0 ∈U. We want to ﬁnd a balanced subset
B ⊂U with 0 ∈B. Scalar multiplication R × V →V is continuous with (0, 0) 7→0, so
there is an ε > 0 and open U0 around 0 in V such that
|a| < ε and v ∈U0 =⇒av ∈U.
If |a| < ε and |t| ≥1 then |a/t| ≤|a| < ε, so (a/t)U0 ⊂U. Thus aU0 ⊂tU. Letting t
vary, aU0 ⊂T
|t|≥1 tU. Since aU0 is open for all nonzero a, the set T
|t|≥1 tU contains an
open set around 0 in V . Let B be the interior of T
|t|≥1 tU, so B is a nonempty open set
in V and B ⊂U (take t = 1). If 0 < |a| ≤1 then |t| ≥1 ⇒|t/a| = |t|/|a| ≥|t| ≥1, so
B ⊂(t/a)U and thus aB ⊂tU. Letting t vary, we get aB ⊂B since aB is open. Thus B
is balanced.
□
Lemma 2.10. A linear map L: V →W, where V and W are topological vector spaces, is
continuous if and only if for all open sets U around 0 in W, L−1(U) contains an open set
around 0 in V . That is, continuity of a linear map V →W is equivalent to continuity at 0.

<!-- page 3 -->
FINITE-DIMENSIONAL TOPOLOGICAL VECTOR SPACES
3
Proof. Proving (⇒) is easy from the deﬁnition of continuity together with L(0) = 0.
To prove (⇐), since L is additive it suﬃces show for every open set U around 0 in W
that L−1(U) is open in V . (Note the task is to show L−1(U) is open, which is stronger than
the hypothesis that L−1(U) contains an open set around 0.)
Pick v ∈L−1(U), so L(v) ∈U. By continuity of addition in W, there is an open set U′
around 0 in W such that Lv + U′ ⊂U. By hypothesis, L−1(U′) contains an open set U′′
around 0 in V , so L(U′′) ⊂U′. Then
L(v + U′′) = L(v) + L(U′′) ⊂L(v) + U′ ⊂U,
so v + U′′ ⊂L−1(U).
□
The following result will not be used in what follows, but is a nice illustration of the
deﬁning properties of a TVS.
Theorem 2.11. Let V be a TVS . For each subspace W of V , its closure W is a subspace.
Proof. This could be proved with a direct use of the deﬁnition of closure: v ∈W when every
open set in V that contains v intersects W. Instead we will give a proof using a property
of closures and homogeneity:
• the closure A of a subset A is the smallest closed subset containing it: if A ⊂C and
C is closed then A ⊂C,
• if a subset C is closed, then v + C and aC are closed for each v ∈V and a ∈R×.
To prove W is a subspace of V , we want to show W +W ⊂W and aW ⊂W for all a ∈R.
(The continuity of vector addition and scalar multiplication on a subspace are automatic,
so every subspace of a TVS is a TVS, and replacing a with 1/a when a ̸= 0 shows aW = W
for a ∈R×.)
Since W is a subspace, W + W ⊂W ⊂W. Thus for each w ∈W, w + W ⊂W, so
W ⊂−w + W. The set −w + W is closed since W is closed, so W ⊂−w + W. Thus
w + W ⊂W for all w ∈W, so W + W ⊂W.
To improve this to W + W ⊂W, for each v ∈W we have W + v ⊂W, so W ⊂−v + W.
Since −v + W is closed, W ⊂−v + W. Thus v + W ⊂W, and since v was arbitrary in W
we get W + W ⊂W. (Try to reprove that now on your own.)
For scalar multiplication, aW = {0} ⊂W when a = 0, so assume a ∈R×. From W ⊂
W, aW ⊂W ⊂W, so W ⊂(1/a)W. Since a ∈R×, (1/a)W is closed, so W ⊂(1/a)W.
Multiplying by a gives us aW ⊂W.
□
3. Proof of Theorem 2.7
Proof. Let V be a TVS V of dimension n and {e1, . . . , en} be a basis of V . Let L: Rn →V
by
L(a1, . . . , an) = a1e1 + · · · + anen.
This is a vector space isomorphism, so L and L−1 are linear.
Since V is a TVS, L is
continuous on account of the continuity of vector addition and scalar multiplication in V .
It remains to prove that L−1 is continuous, where L−1 : V →Rn by
L−1(a1e1 + · · · + anen) = (a1, . . . , an).
Let Bε(0) = {v ∈Rn : ||v|| < ε}. As ε varies, these balls are a basis for the topology at 0 in
Rn, so by Lemma 2.10, it suﬃces to prove for each ε > 0 that (L−1)−1(Bε(0)) = L(Bε(0))

<!-- page 4 -->
4
KEITH CONRAD
contains an open set around 0 in V . That is, we want to show there is an open set Uε around
0 in V such that Uε ⊂L(Bε(0)), or equivalently L−1(U) ⊂Bε(0): v ∈Uε ⇒
L−1(v)
 < ε.
The construction of Uε will use local compactness of Rn in its usual topology. Set
S = {(a1, . . . , an) ∈Rn : ||(a1, . . . , an)|| = 1},
the unit sphere in Rn. It is compact, so L(S) is compact in V by continuity of L, and
0 ̸∈L(S) since L is a bijection and L(0) = 0. Then V −L(S) is an open set containing 0, so
by Lemma 2.9 there is a balanced open set U in V −L(S) that contains 0. For u ∈U and
0 < |t| ≤1, tu ∈U from U being balanced. Thus tu ̸∈L(S), so
L−1(tu)
 ̸= 1. By linearity
of L−1 we can rewrite this as
L−1(u)
 ̸= 1/|t| when 0 < |t| ≤1. Therefore
L−1(u)
 < 1,
so L−1 sends U into the open unit ball of Rn. Now we can set Uε = εU = {εu : u ∈U}:
this is a balanced open set in V that contains 0 and
v ∈Uε =⇒v/ε ∈U =⇒
L−1(v/ε)
 < 1 =⇒
L−1(v)
 < ε,
which is what we wanted to show.
□
It was not crucial in this proof that the norm on Rn is the Euclidean norm. We could
have used an arbitrary norm on Rn. That would change the meaning of the unit sphere
S. For example, if we use the sup-norm on Rn with respect to the standard basis then
S = {(a1, . . . , an) ∈Rn : max |ai| = 1}. Regardless of the choice of norm, the unit sphere
in Rn for that norm is compact (since Rn is locally compact), so the proof still works with
this other unit sphere.
The concept of a TVS makes sense also for complex vector spaces (replace R-linearity
with C-linearity everywhere), and arguments like those above show for each n ∈Z+ that
every n-dimensional complex TVS is isomorphic as a TVS to Cn. In the proof we replace
compactness of the unit sphere in Rn by compactness of the unit sphere
(3.1)
{(z1, . . . , zn) : ||(z1, . . . , zn)|| = 1}
in Cn, where ||·|| is the standard norm (or an arbitrary norm) on Cn. (Watch out: for n ≥1
the sphere (3.1) is the solution set to |z1|2 + · · · + |zn|2 = 1, but not the solution set to
z2
1 + · · · + z2
n = 1, which is ﬁnite for n = 1 and unbounded for n ≥2!)
If you know about the p-adic numbers Qp for primes p (if you don’t know about them,
then ignore this paragraph), check for n ∈Z+ that the proof of Theorem 2.7 can be adapted
to every n-dimensional TVS over Qp: a choice of basis makes it isomorphic to Qn
p. Changing
the proof to be valid over Qp needs a few changes: in the proof of Theorem 2.7 replace
(−ε, ε) with {x ∈Qp : |x|p < ε} and show it suﬃces to work with ε = |a|p for nonzero
p-adic numbers a, and use the sup-norm on Qn
p in order that
Qn
p
 = |Qp|p (this says the
sup-norm of an n-tuple is the p-adic absolute value of some p-adic scalar). The sup-norm
unit sphere in Qn
p is Zn
p −(pZp)n, which is compact from compactness of Zp, and this lets
the use of compactness of unit spheres carry over from the real to the p-adic setting.
4. A second proof of Theorem 2.7
For certain applications in number theory it is important to have a version of Theorem 2.7
where the scalar ﬁeld R (or C) is replaced by ﬁelds that are not locally compact. (Examples
occur in non-Archimedean analysis: Cp with its p-adic topology and F((t)) with its t-adic
topology where F is an inﬁnite ﬁeld; their unit spheres are not compact.) That the proof of
Theorem 2.7 no longer works for a TVS over certain ﬁelds does not mean the theorem itself
is false. What we need is a diﬀerent proof of Theorem 2.7 that does not use compactness

<!-- page 5 -->
FINITE-DIMENSIONAL TOPOLOGICAL VECTOR SPACES
5
arguments, and such a proof is developed in this ﬁnal section. We will continue to work
in the setting of real topological vector spaces for concreteness. At the end will we discuss
what changes are needed for a TVS over other ﬁelds.
Remark 4.1. If all vector spaces you care about are real or complex then you might
not have much motivation to read the more abstract build-up below to a second proof of
Theorem 2.7, since the ﬁrst proof already handles the cases of interest to you.
In metric spaces, topological concepts (continuity, compactness, etc.) can be described
with sequences. Sequences are inadequate for this purpose in general topological spaces
(e.g., compactness and sequential compactness are not equivalent), and our ﬁrst task is to
give a substitute for sequences in all topological spaces.
A sequence in a space X is just a function f : Z+ →X, where f(1) is the ﬁrst term,
f(2) is the second term, and so on. The ordering on Z+ allows us to speak about one term
in a sequence being “farther out” than another. The next deﬁnition gives the language to
generalize this idea to more abstract indexing sets than Z+ in its standard ordering.
Deﬁnition 4.2. A directed set is a set I with a partial ordering denoted by ≥such that
(1) i ≥i in I,
(2) i ≥j and j ≥k in I implies i ≥k,
(3) for all i and j in I there is some k ∈I such that k ≥i and k ≥j.
Example 4.3. Take I = Z+ with its usual ordering ≥.
Example 4.4. Take I = Z+ with ≥being reverse divisibility: i ≥j means j | i. The reader
should check this makes Z+ into a directed set, and it is not like the previous example. For
instance, {i : i ≥3} = 3Z+ and this is missing inﬁnitely many positive integers, whereas
for the standard ordering ≥on Z+, {i : i ≥3} contains all but 2 positive integers.
Example 4.5. Take I to be the open subsets of a topological space X that contain a
speciﬁc point x0, with the ordering by reverse containment: U1 ≥U2 means U1 ⊂U2 (so
U1 is “farther out” than U2 if U1 is a smaller neighborhood of x0 than U2). The ﬁrst two
conditions of a directed set are clear. For the third one, if U and U′ are open sets in X
containing x0 then so is U ∩U′ and we have U ∩U′ ≥U and U ∩U′ ≥U′.
Example 4.5 is the directed set we’ll be interested in for applications in topology.
A diﬀerence between the relation ≥on a directed set I and the usual relation ≥on Z+
from Example 4.3 is that not all pairs of elements in I are comparable to each other. (In
Example 4.4 this means not all i and j in Z+ have i | j or j | i.) To make up for that, the
third condition of a directed set implies that for two incomparable elements in I, a third
element in I is comparable to both of them and is “farther out” than either one. Another
way of saying this is that for all j and j′ in I, {i : i ≥j} ∩{i : i ≥j′} ̸= ∅.
Deﬁnition 4.6. For a set X, a net in X is a function f : I →X where I is a directed set.
When I = Z+ with its usual ordering, a net with index set I is just a sequence.
Deﬁnition 4.7. We say a net {xi}i∈I in a topological space X converges to a point x in X
if for every open subset U ⊂X containing x there is an i0 ∈I such that i ≥i0 ⇒xi ∈U.
We then write x = limi xi. (Another notation is: xi →x.)
To see the concept of a net at work, we prove two properties of nets that are familiar
properties of sequences in metric spaces.

<!-- page 6 -->
6
KEITH CONRAD
Theorem 4.8. In a Hausdorﬀspace, the limit of a convergent net is unique: if a net {xi}
in a Hausdorﬀspace X has limits x and x′ then x = x′.
Proof. Assume x ̸= x′. Since X is Hausdorﬀ, there are open sets U and U′ such that x ∈U
and x′ ∈U′ with U and U′ being disjoint. From the deﬁnition of a convergent net, there is
i0 ∈I such that i ≥i0 ⇒xi ∈U and there is j0 ∈I such that j ≥j0 ⇒xj ∈U′. By the
deﬁnition of a directed set, there is some k ∈I such that k ≥i0 and k ≥j0. Then xk ∈U
and xk ∈U′, so U ∩U′ ̸= ∅. This is a contradiction.
□
Theorem 4.9. Let Y be a nonempty subset of a topological space X, with closure Y . For
x ∈X, we have x ∈Y if and only if x = limi yi in X for some net {yi} in Y .
Note that the phrase “x = limi yi in X” means we are using the limit of a net in X, not
in Y , even if the net is a subset of Y (x may not be in Y ). This is reasonable in light of the
result analogous to Theorem 4.9 for closures in metric spaces using sequences.
Proof. (⇐) Suppose x = limi yi in X for some net {yi} in Y . To prove x ∈Y , assume this
is not the case. Then x is in X −Y , which is a nonempty open set in X, so a net in X that
converges to x must contain some elements of X −Y . This set is disjoint from Y , so no net
from Y can lie even partially in X −Y .
(⇒) Let x ∈Y . From basic topology,
(4.1)
Y =
\
C⊃Y
C closed
C.
We will construct a net in Y converging to x that uses as the directed set I all open sets
around x in X ordered by reverse inclusion. For each U ∈I we must have U ∩Y ̸= ∅: if
U did not meet Y then Y ⊂X −U, and X −U is closed, so by (4.1) and x lying in Y we
have x ∈X −U, but that contradicts x lying in U.
Since U meets Y , we can choose some yU ∈U ∩Y . Now we have a net I →X where
U 7→yU. The elements of the net {yU} all belong to Y , and for each open set U around x,
U′ ≥U =⇒U′ ⊂U =⇒yU′ ∈U′ ⊂U.
Thus limU yU = x.
□
Remark 4.10. The sequential compactness description of a compact metric space, which
says every sequence has a convergent subsequence, generalizes using nets to compactness
in arbitrary topological spaces: a topological space is compact if and only if every net in it
has a convergent subnet. We don’t go into more detail except to say that the deﬁnition of a
subnet (the analogue of a subsequence) is subtle. It is not the restriction of a net f : I →X
to a subset of I, even if I = Z+ with its usual ordering ≥.
Our generalities about nets are over and now we focus on their use in topological vector
spaces, where they lead to analogues of Cauchy sequences and completeness in metric spaces.
Deﬁnition 4.11. In a TVS V , call a net {vi} Cauchy if for every open set U around 0 in
V there is an i0 ∈I such that j, k ≥i0 ⇒vj −vk ∈U.
The basic idea here is that the metric notion of d(x, y) being small is replaced by the
diﬀerence v −w in V being in an open set around 0. We are deﬁning Cauchy nets only in a
TVS, not in a general topological space. (They can also be deﬁned in topological groups.)
To get used to this terminology, we prove two lemmas about Cauchy nets that sound
familiar for sequences in metric spaces.

<!-- page 7 -->
FINITE-DIMENSIONAL TOPOLOGICAL VECTOR SPACES
7
Lemma 4.12. Every convergent net in a TVS is a Cauchy net.
Proof. Let {xi} be a convergent net in V , with limit x. Pick an open set U around 0 in V .
Since −U = {−u : u ∈U} is also an open set containing 0, so is U ∩−U, and this
intersection is symmetric: x ∈U ∩−U ⇒−x ∈U ∩−U. Therefore by shrinking an open
set around 0 in V we can assume it is symmetric if we wish.
By continuity of addition in V , there is an open set N around 0 in V such that N+N ⊂U,
and by replacing N with N ∩−N we can also assume v ∈N ⇒−v ∈N.
Since x + N is an open set in V containing x, by the deﬁnition of a convergent net there
is an i0 ∈I such that i ≥i0 ⇒xi −x ∈N. So if j ≥i0 and k ≥i0 we have xj −x ∈N
and xk −x ∈N. Then −(xk −x) ∈N by the symmetry of N, so for j, k ≥i0 we have
xj −xk = (xj −x) −(xk −x) ∈N + N ⊂U.
□
Lemma 4.13. If V is a TVS and W is a subspace of V , viewed as a TVS with the subspace
topology, then a Cauchy net in V that lies in W is a Cauchy net in W.
Proof. Let {wi} be a Cauchy net in V with wi ∈W for all i. For an open set U around 0 in
W, by the deﬁnition of the subspace topology we have U = U′ ∩W where U′ is open in V .
From the deﬁnition of a Cauchy net in V , there’s an i0 ∈I such that j, k ≥i0 ⇒wj −wk ∈
U′. We always have wj −wk ∈W, so j, k ≥i0 ⇒wj −wk ∈U′ ∩W = U.
□
Deﬁnition 4.14. We say a TVS V is complete if every Cauchy net in V converges in V .
Lemma 4.15. For n ∈Z+, Rn is a complete TVS over R.
Even though we know all Cauchy sequences in Rn converge, that alone doesn’t prove
Lemma 4.15 since Cauchy nets are much more general than Cauchy sequences, e.g., the
directed set for a net might be uncountable.
Proof. Let {vi} be a Cauchy net in Rn. Even though the directed set for this net might
not be countable or totally ordered, we are going to link the net to countable (sequential)
information.
In Rn there is an open ball of radius 1 centered around 0, so there is some i1 ∈I such
that
j, k ≥i1 =⇒||vj −vk|| < 1,
where ||·|| is the standard norm on Rn.
For each m ≥2 there is an open ball in Rn of radius 1/m centered around 0, so there is
some im ∈I such that
(4.2)
j, k ≥im =⇒||vj −vk|| < 1
m.
Since I is directed, we can choose im in I such that
(4.3)
im ≥i1, . . . , im−1.
Then using k = im in (4.2), we have
(4.4)
j ≥im =⇒||vj −vim|| < 1
m.
Consider the sequence {vim}m≥1 = {vi1, vi2, . . .} in Rn. For ε > 0 there is an m ∈Z+
such that 1/m < ε/2. (Why require less than ε/2 rather than less than ε? You’ll see.) By
(4.3), if m′, m′′ ≥m in Z+ then im′, im′′ ≥im in I, so by (4.4),
vim′ −vim′′
 ≤
vim′ −vim
 +
vim′ −vim
 < 1/m + 1/m = 2/m < ε,

<!-- page 8 -->
8
KEITH CONRAD
where the last inequality comes from the condition 1/m < ε/2. Thus {vim} is a Cauchy
sequence in Rn. By the ordinary completeness of Rn, there is some v in Rn such that the
sequence {vim} converges to v.
We now show v is the limit of the original Cauchy net {vi}. Pick an open set in Rn
around v; it has the form v + U where U is an open set around 0 in Rn. For some M ∈Z+
the open 1/M-ball around 0 is contained in U. By the meaning of convergence of sequences,
there is an m ∈Z+ such that m′ ≥m ⇒
vim′ −v
 < 1/(2M), so by making m larger we
can assume m ≥2M. Then for j ∈I,
j ≥im
(4.3)
=⇒j ≥i2M
(4.4)
=⇒||vj −vi2M || <
1
2M ,
so
j ≥im =⇒||vj −v|| ≤||vj −vim|| + ||vim −v|| < 1
m +
1
2M ≤
1
2M +
1
2M = 1
M .
Thus vj −v ∈U, so vj ∈v + U for all j ≥im.
□
The deﬁnition of completeness of a TVS depends only the TVS structure (there is no
metric space structure available in general), so completeness is preserved under TVS iso-
morphisms. Thus Theorem 4.15 tells us that every TVS over R that is isomorphic to some
Rn as a TVS over R is also a complete TVS.
Lemma 4.16. For a TVS V , a linear map L: V →R is continuous if and only if its kernel
is closed in V .
Proof. If L is continuous then ker L = L−1(0) is closed in V since {0} is closed in R.
Now suppose ker L is closed in V . To show L is continuous, we can assume L is not
identically 0, so L is surjective (the only linear subspaces of R are {0} and R). For ε > 0
we will show L−1((−ε, ε)) contains an open set around 0 in V . The intervals (−ε, ε) are a
basis for the topology around 0 in R, so continuity of L then follows from Lemma 2.10.
Pick a0 ∈R with 0 < |a0| < ε. Since L is surjective, L(v0) = a0 for some v0 ∈V . Then
L−1(a0) = v0 +ker L, a closed subset of V . It complement in V is open and contains 0 since
L(0) = 0 ̸= a0. Therefore by Lemma 2.9 there is a balanced open set U around 0 in V such
that U ⊂V −L−1(a0). For all v ∈U, if L(v) ̸= 0 then L(a0v/L(v)) = a0L(v)/L(v) = a0,
so a0v/L(v) ̸∈U. Therefore, from U being balanced, |a0/L(v)| > 1, so |L(v)| < |a0| < ε. If
L(v) = 0 then also |L(v)| < ε. Thus U ⊂{v ∈V : |L(v)| < ε} = L−1((−ε, ε)).
□
Now we are ready to give a second proof of Theorem 2.7.
Proof. We will argue by induction on n, the dimension of V .
n = 1: Pick v0 ̸= 0 in V .
Let L: R →V by L(a) = av0.
This is a vector space
isomorphism. To show L is continuous, view L as the composite of maps R →R×{v0} →V
where the ﬁrst map is a 7→(a, v0) and the second map is scalar multiplication on v0. The
ﬁrst map is continuous by the deﬁnition of the product topology and the second map is
continuous by the continuity of scalar multiplication R × V →V .
It remains to prove that L−1 : V →R by av0 7→a is continuous. Since it is linear, it
suﬃces by Lemma 4.16 to show the kernel is closed. In V we have ker(L−1) = {0}, which
is closed (all points in a Hausdorﬀspace are closed).
n > 1: Assume the theorem is proved for each TVS with dimension n−1. Let V be an n-
dimensional TVS over R with basis {e1, . . . , en} and deﬁne L: Rn →V by L(a1, . . . , an) =

<!-- page 9 -->
FINITE-DIMENSIONAL TOPOLOGICAL VECTOR SPACES
9
Pn
i=1 aiei. As in the ﬁrst proof, L is a vector space isomorphism and it is continuous, so all
that remains to prove is that L−1 : V →Rn is continuous, where
L−1(a1e1 + · · · + anen) = (a1, . . . , an).
Inside V is the (n −1)-dimensional subspace
W = Re1 + · · · + Ren−1,
which is a TVS over R using the subspace topology, and by induction there is a TVS
isomorphism Φ: W →Rn−1 by Φ(a1e1 + · · · + an−1en−1) = (a1, . . . , an−1).2 Deﬁne ϕ: V →
R by ϕ(a1e1 + · · · + anen) = an. Then ϕ is linear and
L−1(v) = (Φ(v −ϕ(v)en), ϕ(v))
for all v ∈V . In the formula on the right we are implicitly identifying Rn−1 × R with Rn
as a TVS over R, which is okay since they are isomorphic (Example 2.6.)
Since Φ is continuous and scaling is continuous on V , the above formula for L−1 shows
that continuity of L−1 will follow from continuity of ϕ. Since ϕ takes values in R, Lemma
4.16 tells us that continuity of ϕ is equivalent to ker(ϕ) being closed in V . The kernel of ϕ
is W and dim(W) = n −1. Why is an (n −1)-dimensional subspace W of V closed in V ?
Let W be the topological closure of W in V and pick v ∈W. We want to prove v ∈W.
Since v is in the closure W we have v = limi wi for some net {wi} that lies in W (Theorem
4.9). Because {wi} is a convergent net in V , it is also a Cauchy net in V by Lemma 4.12.
Since every wi is in W, {wi} is a Cauchy net in W by Lemma 4.13. Because W ∼= Rn−1 as a
TVS over R and Rn−1 is a complete TVS by Lemma 4.15, W is a complete TVS. Therefore
{wi} converges in W, say to w. Both v and w are limits of the Cauchy net {wi}, and a
TVS is Hausdorﬀby deﬁnition, so v = w by Theorem 4.8. Thus v ∈W, which ﬁnishes this
second proof of Theorem 2.7.
□
Remark 4.17. The base case n = 1 relied on the reasoning behind Lemma 4.16 (and in
particular Lemma 2.10). This is a nice example of a proof by induction where the base case
is not a complete triviality.
The motivation for this second proof of Theorem 2.7, as mentioned at the start of this
section, is that the proof and the background lemmas leading up to it apply with very
minor changes to a ﬁnite-dimensional TVS over a ﬁeld K that is complete with respect to a
nontrivial absolute value. There are many such K where, in contrast to R and C, the unit
sphere {x ∈K : |x| = 1} in K is not compact, so the ﬁrst proof of Theorem 2.7 (in Section
3) can’t be applied to a TVS over K. As an example of how lemmas for the second proof of
Theorem 2.7 generalize, the proof of Lemma 4.15 can be used with minor changes to show
Kn with the topology coming from its sup-norm is a complete TVS over K: all Cauchy
nets in Kn converge. A related theorem is that all norms on a ﬁnite-dimensional K-vector
space deﬁne the same topology on the space [1, Theorem 3.2], and this has a simpler proof
when the unit sphere of K is compact.
References
[1] K. Conrad, “Equivalence of norms,” https://kconrad.math.uconn.edu/blurbs/gradnumthy/equiv
norms.pdf.
[2] A. Tychonoﬀ, “Ein Fixpunktsatz,” Math. Ann. 111 (1935), 767–776. URL https://eudml.org/doc/
159810.
2Here we are using n > 1: if n = 1 then W = {0} and has no basis.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*