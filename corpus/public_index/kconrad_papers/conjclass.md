# Conjugation in a Group

> **Source**: https://kconrad.math.uconn.edu/blurbs/conjclass.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
CONJUGATION IN A GROUP
KEITH CONRAD
1. Introduction
A reﬂection across one line in the plane is, geometrically, just like a reﬂection across every
other line. That is, while reﬂections across two diﬀerent lines in the plane are not strictly
the same, they have the same type of eﬀect. Similarly, two diﬀerent transpositions in Sn are
not the same permutation but have the same type of eﬀect: swap two elements and leave
everything else unchanged. The concept that makes the notion of “diﬀerent, but same type
of eﬀect” precise is called conjugacy.
In a group G, two elements g and h are called conjugate when
h = xgx−1
for some x ∈G.
This relation is symmetric, since g = yhy−1 with y = x−1.
When
h = xgx−1, we say x conjugates g to h. (Warning: when some people say “x conjugates g
to h” they might mean h = x−1gx instead of h = xgx−1.)
Example 1.1. The table below lists all σ(12)σ−1 for σ ∈S3.
σ
(1)
(12)
(13)
(23)
(123)
(132)
σ(12)σ−1
(12)
(12)
(23)
(13)
(23)
(13)
The conjugates of (12) are in the second row (each appearing twice): (12), (13), and (23).
So all transpositions in S3 are conjugate. We will see in Theorem 5.4 that all transpositions
in Sn are conjugate to each other.
In Appendix A we will prove that reﬂections across two lines in the plane are conjugate
to each other in the group of all isometries of the plane.
Example 1.2. A sequence of moves S on Rubik’s cube, like swapping the top front corners
without aﬀecting other corners, can be applied to other parts of the cube by ﬁnding a second
sequence of moves A that brings other pieces into the positions that S aﬀects, and carrying
out the sequence of moves ASA−1 (written by cubers as ASA′). Conjugate moves in the
group of all moves on the cube are the same type of move on diﬀerent parts of the cube.
See https://www.youtube.com/watch?v= Zv3YcQeNVI during 2:25 to 3:10 for examples.
It is useful to collect conjugate elements in a group together, and these are called conju-
gacy classes. Examples of them are in Section 2. Some theorems about conjugate elements
are proved in Section 3. We’ll look at conjugate elements of Dn in Section 4 and conjugate
permutations in Sn and An in Section 5. In Section 6 we will introduce some subgroups
that are related to conjugacy and use them to prove some theorems about ﬁnite p-groups,
such as a classiﬁcation of groups of order p2 and the existence of a normal (!) subgroup of
every order dividing the order of a p-group.
1

<!-- page 2 -->
2
KEITH CONRAD
2. Conjugacy classes: definition and examples
For an element g of a group G, its conjugacy class is the set of elements conjugate to it:
{xgx−1 : x ∈G}.
Example 2.1. If G is abelian then xgx−1 = g for all x, g ∈G: every g is its own conjugacy
class. This characterizes abelian groups: to say each g ∈G is its own conjugacy class means
xgx−1 = g for all x and g in G, which says xg = gx for all x and g, so G is abelian.
Example 2.2. The conjugacy class of (12) in S3 is {(12), (13), (23)}, as we saw in Example
1.1. Similarly, the reader can check the conjugacy class of (123) is {(123), (132)}. The
conjugacy class of (1) is just {(1)}. So S3 has three conjugacy classes:
{(1)},
{(12), (13), (23)},
{(123), (132)}.
Example 2.3. In D4 = ⟨r, s⟩, there are ﬁve conjugacy classes:
{1},
{r2},
{r, r3},
{s, r2s},
{rs, r3s}.
The members of a conjugacy class of D4 are diﬀerent but have the same type of eﬀect on a
square: r and r3 are a 90 degree rotation in some direction, s and r2s are a reﬂection across
a diagonal, and rs and r3s are a reﬂection across an edge bisector.
Example 2.4. There are ﬁve conjugacy classes in Q8:
{1},
{−1},
{i, −i},
{j, −j},
{k, −k}.
Example 2.5. There are four conjugacy classes in A4:
{(1)},
{(12)(34), (13)(24), (14)(23)},
{(123), (243), (134), (142)},
{(132), (234), (143), (124)}.
Notice the 3-cycles (123) and (132) are not conjugate in A4. All 3-cycles in A4 are conjugate
in the larger group S4, e.g., (132) = (23)(123)(23)−1 and the conjugating permutation (23)
is not in A4.
In these examples, diﬀerent conjugacy classes in a group are disjoint: they don’t overlap
at all. This will be proved in general in Section 3. Also, the sizes of diﬀerent conjugacy
classes are not all the same, but these sizes all divide the size of the group. We will see in
Section 6 why this is true.
The idea of conjugation can be applied not just to elements, but to subgroups. If H ⊂G
is a subgroup and g ∈G, the set
gHg−1 = {ghg−1 : h ∈H}
is a subgroup of G, called naturally enough a conjugate subgroup to H. It’s a subgroup
since it contains the identity (e = geg−1) and is closed under multiplication and inversion:
(ghg−1)(gh′g−1) = g(hh′)g−1 and (ghg−1)−1 = gh−1g−1. Unlike diﬀerent conjugacy classes,
diﬀerent conjugate subgroups are not disjoint: they all contain the identity.
Example 2.6. While D4 has 5 conjugacy classes of elements (Example 2.3), it has 8
conjugacy classes of subgroups. In total there are 10 subgroups of D4:
⟨1⟩= {1},
⟨s⟩= {1, s},
⟨rs⟩= {1, rs},
⟨r2s⟩= {1, r2s},
⟨r3s⟩= {1, r3s},
⟨r⟩= {1, r, r2, r3},
⟨r2⟩= {1, r2},
⟨r2, s⟩= {1, r2, s, r2s},
⟨r2, rs⟩= {1, r2, rs, r3s},
D4.
In this list the subgroups ⟨s⟩and ⟨r2s⟩are conjugate, as are ⟨rs⟩and ⟨r3s⟩: check r⟨s⟩r−1 =
⟨r2s⟩and r⟨rs⟩r−1 = ⟨r3s⟩. The other six subgroups of D4 are conjugate only to themselves.

<!-- page 3 -->
CONJUGATION IN A GROUP
3
We will not discuss conjugate subgroups much, but the concept is important. For in-
stance, a subgroup is conjugate only to itself precisely when it is a normal subgroup.
3. Some basic properties of conjugacy classes
Lemma 3.1. In a group, (xgx−1)n = xgnx−1 for all positive integers n.
Proof. This is left to the reader as an exercise using induction. The equation is in fact true
for all n ∈Z.
□
Theorem 3.2. All the elements of a conjugacy class have the same order.
Proof. This is saying g and xgx−1 have the same order. By Lemma 3.1, (xgx−1)n = xgnx−1
for all n ∈Z+, so if gn = 1 then (xgx−1)n = xgnx−1 = xx−1 = e, and if (xgx−1)n = 1 then
xgnx−1 = e, so gn = x−1x = e. Thus (xgx−1)n = 1 if and only if gn = 1, so g and xgx−1
have the same order.
□
The converse to Theorem 3.2 is false: elements of the same order in a group need not be
conjugate in that group. This is clear in abelian groups, where diﬀerent elements are never
conjugate but could have the same order. Looking at the nonabelian examples in Section
2, in D4 there are ﬁve elements of order two spread across 3 conjugacy classes. Similarly,
there are non-conjugate elements of equal order in Q8 and A4. But in S3, elements of equal
order in S3 are conjugate. Amazingly, this is the largest example of a ﬁnite group where
that property holds: up to isomorphism, the only nontrivial ﬁnite groups where all elements
of equal order are conjugate are Z/(2) and S3. A proof is given in [3] and [7], and depends
on the classiﬁcation of ﬁnite simple groups. A conjugacy problem about S3 that remains
open, as far as I know, is the conjecture that S3 is the only nontrivial ﬁnite group (up to
isomorphism) in which diﬀerent conjugacy classes all have diﬀerent sizes.
Corollary 3.3. If H is a cyclic subgroup of G then every subgroup conjugate to H is cyclic.
Proof. Writing H = ⟨y⟩= ⟨yn : n ∈Z},
gHg−1 = {gyng−1 : n ∈Z} = {(gyg−1)n : n ∈Z} = ⟨gyg−1⟩,
so gHg−1 is cyclic with a generator being a conjugate (by g) of a generator of H.
□
Let’s verify the observation in Section 2 that diﬀerent conjugacy classes are disjoint.
Theorem 3.4. Let G be a group and g, h ∈G. If the conjugacy classes of g and h overlap,
then the conjugacy classes are equal.
Proof. We need to show every element conjugate to g is also conjugate to h, and vice versa.
Since the conjugacy classes overlap, we have xgx−1 = yhy−1 for some x and y in the group.
Therefore
g = x−1yhy−1x = (x−1y)h(x−1y)−1,
so g is conjugate to h. Each element conjugate to g is zgz−1 for some z ∈G, and
zgz−1 = z(x−1y)h(x−1y)−1z−1 = (zx−1y)h(zx−1y)−1,
which shows each element of G that is conjugate to g is also conjugate to h. To go the other
way, from xgx−1 = yhy−1 write h = (y−1x)g(y−1x)−1 and carry out a similar calculation.
□

<!-- page 4 -->
4
KEITH CONRAD
Theorem 3.4 says each element of a group belongs to just one conjugacy class. We call
an element of a conjugacy class a representative of that class.
A conjugacy class consists of all xgx−1 for ﬁxed g and varying x. Instead we can look
at all xgx−1 for ﬁxed x and varying g.
That is, instead of looking at all the elements
conjugate to g we look at all the ways x can conjugate the elements of the group. This
“conjugate-by-x” function is denoted γx : G →G, so γx(g) = xgx−1.
Theorem 3.5. Each conjugation function γx : G →G is an automorphism of G.
Proof. For all g and h in G,
γx(g)γx(h) = xgx−1xhx−1 = xghx−1 = γx(gh),
so γx is a homomorphism. Since h = xgx−1 if and only if g = x−1hx, the function γx has
inverse γx−1, so γx is an automorphism of G.
□
Theorem 3.5 explains why conjugate elements in a group G are “the same except for the
point of view”: they are linked by an automorphism of G, namely some map γx. This means
an element of G and its conjugates in G have the same group-theoretic properties, such as:
having the same order, being an m-th power, being in the center, and being a commutator.
Likewise, a subgroup H and its conjugates gHg−1 have the same group-theoretic properties.
Automorphisms of G having the form γx are called inner automorphisms. They are the
only automorphisms that can be written down without knowing extra information about G
(such as being told G is abelian or that G is a particular matrix group). For some G every
automorphism of G is an inner automorphism. This is true for the groups Sn when n ̸= 6
(that’s right: S6 is the only symmetric group with an automorphism that isn’t conjugation
by a permutation). The groups GLn(R) when n ≥2 have extra automorphisms: since
(AB)⊤= B⊤A⊤and (AB)−1 = B−1A−1, the function f(A) = (A⊤)−1 on GLn(R) is an
automorphism and it is not inner.
Here is a simple result where inner automorphisms tell us something about all automor-
phisms of a group.
Theorem 3.6. If G is a group with trivial center, then the group Aut(G) also has trivial
center.
Proof. Let ϕ ∈Aut(G) and assume ϕ commutes with all other automorphisms. We will see
what it means for ϕ to commute with an inner automorphism γx. For g ∈G,
(ϕ ◦γx)(g) = ϕ(γx(g)) = ϕ(xgx−1) = ϕ(x)ϕ(g)ϕ(x)−1
and
(γx ◦ϕ)(g) = γx(ϕ(g)) = xϕ(g)x−1,
so having ϕ and γx commute means, for all g ∈G, that
ϕ(x)ϕ(g)ϕ(x)−1 = xϕ(g)x−1 ⇐⇒x−1ϕ(x)ϕ(g) = ϕ(g)x−1ϕ(x),
so x−1ϕ(x) commutes with every value of ϕ. Since ϕ is onto, x−1ϕ(x) ∈Z(G). The center
of G is trivial, so ϕ(x) = x. This holds for all x ∈G, so ϕ is the identity automorphism.
We have proved the center of Aut(G) is trivial.
□

<!-- page 5 -->
CONJUGATION IN A GROUP
5
4. Conjugacy classes in Dn
In the group Dn we will show rotations are conjugate only to their inverses and reﬂections
are either all conjugate or fall into two conjugacy classes.
Theorem 4.1. The conjugacy classes in Dn are as follows.
(1) If n is odd,
• the identity element: {1},
• (n −1)/2 conjugacy classes of size 2: {r±1}, {r±2}, . . . , {r±(n−1)/2},
• all the reﬂections: {ris : 0 ≤i ≤n −1}.
(2) If n is even,
• two conjugacy classes of size 1: {1}, {r
n
2 },
• n/2 −1 conjugacy classes of size 2: {r±1}, {r±2}, . . . , {r±( n
2 −1)},
• the reﬂections fall into two conjugacy classes: {r2is : 0 ≤i ≤
n
2 −1} and
{r2i+1s : 0 ≤i ≤n
2 −1}.
Proof. Every element of Dn is ri or ris for some integer i. Therefore to ﬁnd the conjugacy
class of an element g we will compute rigr−i and (ris)g(ris)−1.
The formulas
rirjr−i = rj,
(ris)rj(ris)−1 = r−j
as i varies show the only conjugates of rj in Dn are rj and r−j. Explicitly, the basic formula
srjs−1 = r−j shows us rj and r−j are conjugate; we need the more general calculation to
be sure there is nothing further that rj is conjugate to.
To ﬁnd the conjugacy class of s, we compute
risr−i = r2is,
(ris)s(ris)−1 = r2is.
As i varies, r2is runs through the reﬂections in which r occurs with an exponent divisible
by 2. If n is odd then every integer modulo n is a multiple of 2 (since 2 is invertible mod n
we can solve k ≡2i mod n for i no matter what k is). Therefore when n is odd
{r2is : i ∈Z} = {rks : k ∈Z},
so every reﬂection in Dn is conjugate to s. When n is even, however, we only get half the
reﬂections as conjugates of s. The other half are conjugate to rs:
ri(rs)r−i = r2i+1s,
(ris)(rs)(ris)−1 = r2i−1s.
As i varies, this gives us {rs, r3s, . . . , rn−1s}.
□
That reﬂections in Dn form either one or two conjugacy classes, depending on the parity
of n, corresponds to a geometric feature of reﬂections: for odd n all reﬂections in Dn look
the same (Figure 1) – reﬂecting across a line connecting a vertex and the midpoint on the
opposite side – but for even n the reﬂections in Dn fall into two types –the revens reﬂect
across a line through pairs of opposite vertices and the rodds reﬂect across a line through
midpoints of opposite sides (Figure 2).
5. Conjugacy classes in Sn and An
The following tables list a representative from each conjugacy class in Sn and An for
3 ≤n ≤6, along with the size of the conjugacy classes. Conjugacy classes disjointly cover
a group, by Theorem 3.4, so the conjugacy class sizes add up to n! for Sn and n!/2 for An.

<!-- page 6 -->
6
KEITH CONRAD
Figure 1. Lines of Reﬂection for n = 3 and n = 5.
Figure 2. Lines of Reﬂection for n = 4 and n = 6.
S3
A3
Rep.
(1)
(123)
(12)
(1)
(123)
(132)
Size
1
2
3
1
1
1
S4
A4
Rep.
(1)
(12)(34)
(12)
(1234)
(123)
(1)
(12)(34)
(123)
(132)
Size
1
3
6
6
8
1
3
4
4
S5
Rep.
(1)
(12)
(12)(34)
(123)
(12)(345)
(12345)
(1234)
Size
1
10
15
20
20
24
30
A5
Rep.
(1)
(12345)
(21345)
(12)(34)
(123)
Size
1
12
12
15
20
S6
Rep.
(1)
(12)
(12)(34)(56)
(123)
(123)(456)
(12)(34)
Size
1
15
15
40
40
45
Rep.
(1234)
(12)(3456)
(123456)
(12)(345)
(12345)
Size
90
90
120
120
144
A6
Rep.
(1)
(123)
(123)(456)
(12)(34)
(12345)
(23456)
(1234)(56)
Size
1
40
40
45
72
72
90

<!-- page 7 -->
CONJUGATION IN A GROUP
7
Notice elements of An can be conjugate in Sn while not being conjugate in An, such as
(123) and (132) for n = 3 and n = 4. (See Example 2.5.) The permutations in S3 and S4
that conjugate (123) to (132) are not even, so (123) and (132) are not conjugate in A3 or
A4. They are conjugate in A5: (132) = σ(123)σ−1 for σ = (23)(45).
As a ﬁrst step in describing conjugacy classes in Sn, let’s ﬁnd the conjugates of a k-cycle.
Theorem 5.1. For each cycle (i1i2 . . . ik) in Sn and each σ ∈Sn,
σ(i1i2 . . . ik)σ−1 = (σ(i1)σ(i2) . . . σ(ik)).
Before proving this formula, let’s see in two examples how it works.
Example 5.2. In S5, let σ = (13)(254). Then
σ(1432)σ−1 = (13)(254)(1432)(245)(13) = (1532)
while (σ(1)σ(4)σ(3)σ(2)) = (3215) since σ(1) = 3, σ(4) = 2, σ(3) = 1, and σ(2) = 5.
Clearly (1532) = (3215).
Example 5.3. In S7, let σ = (13)(265). Then
σ(73521)σ−1 = (13)(265)(73521)(256)(13) = (12637)
and (σ(7)σ(3)σ(5)σ(2)σ(1)) = (71263) = (12637).
Now we prove Theorem 5.1.
Proof. Let π = σ(i1i2 . . . ik)σ−1.
We want to show π is the cyclic permutation of the
numbers σ(i1), σ(i2), . . . , σ(ik). That means two things:
• Show π sends σ(i1) to σ(i2), σ(i2) to σ(i3), . . . , and ﬁnally σ(ik) to σ(i1).
• Show π does not move a number other than σ(i1), . . . , σ(ik).
The second step is essential. Just knowing a permutation cyclically permutes certain num-
bers does not mean it is the cycle built from those numbers, since it could move other
numbers we haven’t looked at yet. (For instance, if π(1) = 2 and π(2) = 1, π need not be
(12). The permutation (12)(345) also has that behavior.)
What does π do to σ(i1)? The eﬀect is
π(σ(i1)) = (σ(i1i2 . . . ik)σ−1)(σ(i1)) = ((σ(i1i2 . . . ik)σ−1σ)(i1) = σ(i1i2 . . . ik)(i1) = σ(i2).
(The “(i1)” at the ends is not a 1-cycle, but denotes the point where a permutation is being
evaluated.)
Similarly, π(σ(i2)) = σ(i1i2 . . . ik)(i2) = σ(i3), and so on up to π(σ(ik)) =
σ(i1i2 . . . ik)(ik) = σ(i1).
Now pick a number a that is not among σ(i1), . . . , σ(ik). We want to show π(a) = a.
That means we want to show σ(i1i2 . . . ik)σ−1(a) = a. Since a ̸= σ(ij) for j = 1, . . . , k, also
σ−1(a) is not ij for j = 1, . . . , k. Therefore the cycle (i1i2 . . . ik) does not move σ−1(a), so
its eﬀect on σ−1(a) is to keep it as σ−1(a). Hence
π(a) = (σ(i1i2 . . . ik)σ−1)(a) = σ(i1i2 . . . ik)(σ−1(a)) = σ(σ−1(a)) = a.
□
We now know that every conjugate of a cycle is also a cycle of the same length. Is the
converse true, i.e., if two cycles have the same length are they conjugate?
Theorem 5.4. All cycles of the same length in Sn are conjugate.

<!-- page 8 -->
8
KEITH CONRAD
Proof. Pick two k-cycles, say
(a1 a2 . . . ak),
(b1 b2 . . . bk).
Choose σ ∈Sn so that σ(a1) = b1, . . . , σ(ak) = bk, and let σ be an arbitrary bijection from
the complement of {a1, . . . , ak} to the complement of {b1, . . . , bk}. Then, using Theorem
5.1, we see conjugation by σ carries the ﬁrst k-cycle to the second.
□
For instance, the transpositions (2-cycles) in Sn form a single conjugacy class, as we saw
for S3 in the introduction.
Now we consider the conjugacy class of an arbitrary permutation in Sn, not necessarily
a cycle. It will be convenient to introduce some terminology. Writing a permutation as a
product of disjoint cycles, arrange the lengths of those cycles in increasing order, including
1-cycles if there are ﬁxed points. These lengths are called the cycle type of the permutation.1
For instance, in S7 the permutation (12)(34)(567) is said to have cycle type (2, 2, 3). When
discussing the cycle type of a permutation, we include ﬁxed points as 1-cycles. For instance,
(12)(35) in S5 is (4)(12)(35) and has cycle type (1, 2, 2). If we view (12)(35) in S6 then it
is (4)(6)(12)(35) and has cycle type (1, 1, 2, 2).
The cycle type of a permutation in Sn is just a set of positive integers that add up to n,
which is called a partition of n. There are 7 partitions of 5:
5, 1 + 4, 2 + 3, 1 + 1 + 3, 1 + 2 + 2, 1 + 1 + 1 + 2, 1 + 1 + 1 + 1 + 1.
Thus, the permutations of S5 have 7 cycle types. Knowing the cycle type of a permutation
tells us its disjoint cycle structure except for how the particular numbers fall into the cycles.
For instance, a permutation in S5 with cycle type (1, 2, 2) could be (1)(23)(45), (2)(35)(14),
and so on. This cycle type of a permutation is exactly the level of detail that conjugacy
measures in Sn: two permutations in Sn are conjugate precisely when they have the same
cycle type. Let’s understand how this works in an example ﬁrst.
Example 5.5. We consider two permutations in S5 of cycle type (2, 3):
π1 = (24)(153),
π2 = (13)(425).
To conjugate π1 to π2, let σ be the permutation in S5 that sends the terms appearing in π1
to the terms appearing in π2 in exactly the same order: σ =
 24153
13425

= (14352). Then
σπ1σ−1 = σ(24)(153)σ−1 = σ(24)σ−1σ(153)σ−1 = (σ(2)σ(4))(σ(1)σ(5)σ(3)) = (13)(425),
so σπ1σ−1 = π2.
If we had written π1 and π2 diﬀerently, say as
π1 = (42)(531),
π2 = (13)(542),
then π2 = σπ1σ−1 where σ =
 42531
13542

= (1234).
Lemma 5.6. If π1 and π2 are disjoint permutations in Sn, then σπ1σ−1 and σπ2σ−1 are
disjoint permutations for all σ ∈Sn.
Proof. Being disjoint means no number is moved by both π1 and π2. That is, there is no i
such that π1(i) ̸= i and π2(i) ̸= i. If σπ1σ−1 and σπ2σ−1 are not disjoint, then they both
move some number, say j. Then (check!) σ−1(j) is moved by both π1 and π2, which is a
contradiction.
□
1A more descriptive label might be “disjoint cycle structure”, but the standard term is “cycle type”.

<!-- page 9 -->
CONJUGATION IN A GROUP
9
Theorem 5.7. Two permutations in Sn are conjugate if and only if they have the same
cycle type.
Proof. Pick π ∈Sn. Write π as a product of disjoint cycles. By Theorem 3.5 and Lemma
5.6, σπσ−1 will be a product of the σ-conjugates of the disjoint cycles for π, and these
σ-conjugates are disjoint cycles with the same respective lengths. Therefore σπσ−1 has the
same cycle type as π.
For the converse direction, we need to explain why permutations π1 and π2 with the same
cycle type are conjugate. Suppose the cycle type is (m1, m2, . . . ). Then
π1 = (a1 a2 . . . am1
|
{z
}
m1 terms
)(am1+1 am1+2 . . . am1+m2
|
{z
}
m2 terms
) · · ·
and
π2 = (b1 b2 . . . bm1
|
{z
}
m1 terms
)(bm1+1 bm1+2 . . . bm1+m2
|
{z
}
m2 terms
) · · · ,
where the cycles here are disjoint.
To carry π1 to π2 by conjugation in Sn, deﬁne the
permutation σ ∈Sn by: σ(ai) = bi for all i. Then σπ1σ−1 = π2 by Theorems 3.5 and 5.4.
(This is exactly the method used to ﬁnd σ in Example 5.5.)
□
Remark 5.8. Theorem 5.7 has real-world signiﬁcance: it is a property of permutations
that helped the Polish cryptographer Marian Rejewski and his colleagues break an early
version of the German military’s Enigma code in the years before World War II [5].
A permutation’s conjugacy class in Sn is determined by its cycle type, which is a partition
of n, so the number of conjugacy classes in Sn is the number of partitions of n. The number
of partitions of n is denoted p(n). Below is a table of some values, which for n ≤6 agree
with the number of conjugacy classes in Sn in the tables at the start of this section.
n
1
2
3
4
5
6
7
8
9
10
11
12
13
14
p(n)
1
2
3
5
7
11
15
22
30
42
56
77
101
135
The function p(n) grows quickly, e.g., S100 has p(100) = 190,569,292 conjugacy classes.
Using Theorem 5.7, there is a type of converse to Theorem 3.2: elements of equal order
in a group need not be conjugate in the group, but they are conjugate in a suitable larger
group.
Corollary 5.9. Each ﬁnite group G can be embedded in a larger group where all elements
of G with equal order become conjugate.
Proof. From Cayley’s theorem we can embed G into a symmetric group by associating to
each g ∈G the permutation ℓg : G →G where ℓg(x) = gx. By labeling the elements of G
as {g1, . . . , gn} we can make each permutation of G look like a permutation of {1, . . . , n},
and that makes the mapping g 7→ℓg an injective homomorphism G →Sn, where n = |G|.
Let g ∈G have order m, so m | n. Left multiplication of g on G, as a permutation of G, is
a product of disjoint m-cycles (x gx g2x · · · gm−1x). The cycle decomposition of ℓg will have
|G|/m disjoint m-cycles. Therefore the cycle type of the permutation ℓg in Sn depends on
g only through its order m. For another element g′ in G with order m, ℓg′ as a permutation
of G has the same cycle type as ℓg, so ℓg and ℓg′ are conjugate in Sn by Theorem 5.7.
□
Example 5.10. In the group G = Z/(10), 2 and 4 have order 5 and are not conjugate in G
since G is abelian. When we view G in S10 using Cayley’s theorem, ℓ2 = (02468)(13579) and

<!-- page 10 -->
10
KEITH CONRAD
ℓ4 = (04826)(15937). These are conjugate in S10: ℓ4 = σℓ2σ−1, where σ =
 0123456789
0145892367

=
(2486)(3597).
Corollary 5.9 is also true for inﬁnite G, by using inﬁnite symmetric groups in the proof.
Let’s now look at conjugacy classes in An. If π is an even permutation, then σπσ−1 is
also even, so a conjugacy class in Sn that contains one even permutation contains only even
permutations. However, two permutations π1 and π2 in An can have the same cycle type
(and thus be conjugate in Sn) while not being conjugate in An. The point is that we might
be able to get π2 = σπ1σ−1 for some σ ∈Sn without being able to do this for σ ∈An.
Example 5.11. The 3-cycles (123) and (132) are conjugate in S3: (23)(123)(23)−1 = (132).
However, (123) and (132) are not conjugate in A3 because A3 is abelian.
Example 5.12. The 3-cycles (123) and (132) are conjugate in S4 (by (23)) but they are
not conjugate in A4. To see this, let’s determine all possible σ ∈S4 that conjugate (123) to
(132). For σ ∈S4, the condition σ(123)σ−1 = (132) is the same as (σ(1)σ(2)σ(3)) = (132).
There are three possibilities:
• σ(1) = 1, so σ(2) = 3 and σ(3) = 2, and necessarily σ(4) = 4. Thus σ = (23).
• σ(1) = 3, so σ(2) = 2 and σ(3) = 1, and necessarily σ(4) = 4. Thus σ = (13).
• σ(1) = 2, so σ(2) = 1 and σ(3) = 3, and necessarily σ(4) = 4. Thus σ = (12).
Therefore the only possible σ’s are transpositions, which are not in A4.
It would be nice if each conjugacy class in An is determined by its cycle type, as in Sn,
but we have met counterexamples: (123) and (132) are not conjugate in A3 or A4. How
does a conjugacy class of even permutations in Sn break up into conjugacy classes in An?
There are two possibilities: the conjugacy class remains a conjugacy class in An or it breaks
up into two conjugacy classes of equal size in An. A glance at the earlier tables of conjugacy
classes in An with small n shows this happening. For instance,
• there is one class of 8 3-cycles in S4, but two classes of 4 3-cycles in A4,
• there is one class of 24 5-cycles in S5, but two classes of 12 5-cycles in A5,
• there is one class of 144 5-cycles in S6, but two classes of 72 5-cycles in A6.
A rule that describes when each possibility occurs is as follows, but a proof is omitted.
Theorem 5.13. For π ∈An, its conjugacy class in Sn is a single conjugacy class in An
or it breaks into two conjugacy classes in An of equal size. The second case happens if and
only if the lengths in the cycle type of π are distinct odd numbers.
Here is a table of the cycle types describing two conjugacy classes in An for 4 ≤n ≤14.
For example, the permutations in A6 of cycle type (1, 5) fall into two conjugacy classes and
the permutations in A8 of cycle type (1, 7) or (3, 5) each fall into two conjugacy classes.
n
4
5
6
7
8
9
10
11
12
13
14
Cycle
(1,3)
(5)
(1,5)
(7)
(1,7)
(9)
(1,9)
(11)
(1,11)
(13)
(1,13)
type
(3,5)
(1,3,5)
(3,7)
(1,3,7)
(3,9)
(1,3,9)
(3,11)
in An
(5,7)
(1,5,7)
(5,9)
The following table lists the number of conjugacy classes in An for small n.
n
1
2
3
4
5
6
7
8
9
10
11
12
13
14
Number conj. classes in An
1
1
3
4
5
7
9
14
18
24
31
43
55
72

<!-- page 11 -->
CONJUGATION IN A GROUP
11
6. Centralizers and the class equation
We saw in Theorem 3.4 that diﬀerent conjugacy classes do not overlap.
Thus, they
provide a way of covering the group by disjoint sets. This is analogous to the left cosets of
a subgroup providing a disjoint covering of the group.
For g ∈G, let Kg denote its conjugacy class in G:
Kg = {xgx−1 : x ∈G}.
If the diﬀerent conjugacy classes are Kg1, Kg2, . . . , Kgr, then
(6.1)
|G| = |Kg1| + |Kg2| + · · · + |Kgr|.
Equation (6.1) plays the role for conjugacy classes in G that the formula |G| = |H|[G : H]
plays for cosets of H in G.
Let’s see how (6.1) looks for some groups from Section 2.
Example 6.1. For G = S3, by Example 2.2
6 = |K(1)| + |K(123)| + |K(12)| = 1 + 2 + 3.
Example 6.2. For G = D4, by Example 2.3
8 = |K1| + |Kr2| + |Kr| + |Ks| + |Krs| = 1 + 1 + 2 + 2 + 2.
Example 6.3. For G = Q8, by Example 2.4
8 = |K1| + |K−1| + |Ki| + |Kj| + |Kk| = 1 + 1 + 2 + 2 + 2.
Example 6.4. For G = A4, by Example 2.5
12 = |K(1)| + |K(12)(34)| + |K(123)| + |K(132)| = 1 + 3 + 4 + 4.
Each conjugacy class in a ﬁnite group divides the size of the group. We see this in the
examples above. Now we will prove it in general.
Theorem 6.5. If G is a ﬁnite group then each conjugacy class in G has size dividing |G|.
Theorem 6.5 is not an immediate consequence of Lagrange’s theorem since a conjugacy
class is not a subgroup except for the one-element conjugacy class of the identity element.
It turns out that the size of a conjugacy class is always the index of a subgroup, and that
will explain why its size divides the size of the group.
Deﬁnition 6.6. For a group G, its center Z(G) is the set of elements of G commuting with
everything:
Z(G) = {g ∈G : gx = xg for all x ∈G}.
For g ∈G, its centralizer Z(g) is the set of elements of G commuting with g:
Z(g) = {x ∈G : xg = gx}.
The notation Z comes from German: center is Zentrum and centralizer is Zentralisator.
Some English language books use the letter C: C(G) = Z(G) and C(g) = Z(g).
The
center of the group and the centralizer of each element of the group are subgroups. Their
connection is that the center is the intersection of all centralizers: Z(G) = T
g∈G Z(g).
Theorem 6.7. For each g ∈G, its conjugacy class has the same size as the index of its
centralizer:
|{xgx−1 : x ∈G}| = [G : Z(g)].

<!-- page 12 -->
12
KEITH CONRAD
Proof. Consider the function f : G →Kg where f(x) = xgx−1. This function is onto, since
by deﬁnition every element of Kg is xgx−1 for some x ∈G. We will now examine when f
takes the same value at elements of G.
For x and x′ in G, we have xgx−1 = x′gx′−1 if and only if
gx−1x′ = x−1x′g.
Therefore x−1x′ commutes with g, i.e., x−1x′ ∈Z(g), so x′ ∈xZ(g). Although x and x′
may be diﬀerent, they lie in the same left coset of Z(g):
(6.2)
f(x) = f(x′) =⇒xZ(g) = x′Z(g).
Conversely, suppose xZ(g) = x′Z(g). Then x = x′z for some z ∈Z(g), so zg = gz.
Therefore x and x′ conjugate g in the same way:
f(x) = xgx−1
= (x′z)g(x′z)−1
= x′zgz−1x′−1
= x′gzz−1x′−1
= x′gx′−1
= f(x′).
Since we have shown that the converse of (6.2) is true, the function f : G →Kg takes
the same value at two elements precisely when they are in the same left coset of Z(g).
Therefore the number of diﬀerent values of f is the number of diﬀerent left cosets of Z(g)
in G, and by deﬁnition that is the index [G : Z(g)]. Since f is surjective, we conclude that
|Kg| = [G : Z(g)].
□
Now we can prove Theorem 6.5.
Proof. By Theorem 6.7, the size of the conjugacy class of g is the index [G : Z(g)], which
divides |G|.
□
Returning to (6.1), we rewrite it in the form
(6.3)
|G| =
r
X
i=1
[G : Z(gi)] =
r
X
i=1
|G|
|Z(gi)|.
The conjugacy classes of size 1 are exactly those containing elements of the center of G (i.e.,
those gi such that Z(gi) = G). Combining all of these 1’s into a single term, we get
(6.4)
|G| = |Z(G)| +
X
i′
|G|
|Z(gi′)|,
where the sum is now carried out only over those conjugacy classes Kgi′ with more than
one element. In the terms of this sum, |Z(gi′)| < |G|. Equation (6.4) is called the class
equation. The diﬀerence between the class equation and (6.1) is that we have combined the
terms contributing to the center of G into a single term.
Here is a good application of the class equation.
Theorem 6.8. When G is a nontrivial ﬁnite p-group it has a nontrivial center: some
element of G other than the identity commutes with every element of G.

<!-- page 13 -->
CONJUGATION IN A GROUP
13
Proof. Let |G| = pn, where n > 0. Consider a term [G : Z(gi′)] in the class equation, where
gi′ does not lie in Z(G). Then Z(gi′) ̸= G, so the index [G : Z(gi′)] is a factor of |G| other
than 1. It is one of {p, p2, . . . , pn}, and hence is divisible by p. In the class equation, all
terms in the sum over i′ are multiples of p.
Also, the left side of the class equation is a multiple of p, since |G| = pn. So the class
equation forces p | |Z(G)|. Since the center contains the identity, and has size divisible by
p, it must contain non-identity elements as well.
□
With a little extra work we can generalize Theorem 6.8.
Theorem 6.9. If G is a nontrivial ﬁnite p-group and N is a nontrivial normal subgroup
of G then N ∩Z(G) ̸= {e}.
Proof. Since N is a normal subgroup of G, a conjugacy class in G that meets N lies entirely
inside of N (that is, if g ∈N then xgx−1 ∈N for all x ∈G). Let Kg1, . . . , Kgs be the
diﬀerent conjugacy classes of G that lie inside N, so
(6.5)
|N| = |Kg1| + · · · + |Kgs|.
(Note that elements of N can be conjugate in G without being conjugate in N, so breaking
up N into its G-conjugacy classes in (6.5) is a coarser partitioning of N than breaking it into
N-conjugacy classes.) The left side of (6.5) is a power of p greater than 1. Each term on
the right side is a conjugacy class in G, so |Kgi| = [G : Z(gi)], where Z(gi) is the centralizer
of gi in G. This index is a power of p greater than 1 except when gi ∈Z(G), in which case
|Kgi| = 1. The gi’s in N with |Kgi| = 1 are elements of N ∩Z(G). Therefore if we reduce
(6.5) modulo p we get
0 ≡|N ∩Z(G)| mod p,
so |N ∩Z(G)| is divisible by p. Since |N ∩Z(G)| ≥1 the intersection N ∩Z(G) contains a
non-identity term.
□
Remark 6.10. The ﬁniteness assumption in Theorem 6.8 is important: there are inﬁnite
p-groups with trivial center! Here is an example. Consider the set G of inﬁnite mod p
square matrices ( M O
O I∞) where I∞is an inﬁnite identity matrix mod p and M is a ﬁnite
upper triangular square matrix of the form







1
a12
· · ·
a1 n−1
a1n
0
1
· · ·
a2 n−1
a2n
...
...
...
...
...
0
0
· · ·
1
an−1 n
0
0
· · ·
0
1







where there are 1’s on the main diagonal and the entries aij above the main diagonal are
arbitrary in Z/(p). Because each row or column of a matrix in G has only ﬁnitely many
nonzero elements, matrix multiplication in G makes sense. To show G is a group under
matrix multiplication, by borrowing the upper left 1 in I∞we can write

M
O
O
I∞

=


M
O
O
O
1
O
O
O
I∞


and thereby view the inﬁnite matrix as having an (n + 1) × (n + 1) upper left part instead
of an n × n upper left part. In this way all pairs of matrices ( M O
O I∞) and ( N O
O I∞) in G can

<!-- page 14 -->
14
KEITH CONRAD
be considered to have M and N of the same size. Then we obtain a block multiplication
formula (check!)
( M O
O I∞)( N O
O I∞) = ( MN O
O
I∞).
Since the n × n upper triangular mod p
matrices with 1’s on the main diagonal form a group, it follows that G is a group. Since M
has p-power order, each element of G has p-power order. Thus G is an “inﬁnite p-group.”
To show G has trivial center, each non-identity element of G is ( M O
O I∞), where M is n×n
for some n and M ̸= In. We have the following equations in 2n × 2n matrices:
(6.6)

M
O
O
In
 
In
In
O
In

=

M
M
O
In

and

In
In
O
In
 
M
O
O
In

=

M
In
O
In

.
Set A = ( M O
O In ) and B = ( In In
O In ), which are 2n × 2n matrices, and (6.6) says AB = ( M M
O In )
and BA = ( M In
O In ). Since M ̸= In, AB ̸= BA. Embed A and B in G as ( A O
O I∞) and
( B O
O I∞), so A and B not commuting implies ( A O
O I∞) and ( B O
O I∞) don’t commute in G. Since
( A O
O I∞) = ( M O
O I∞), ( M O
O I∞) ̸∈Z(G).
The following corollary is the standard ﬁrst application of Theorem 6.8.
Corollary 6.11. For all primes p, every group of order p2 is abelian. More precisely, a
group of order p2 is isomorphic to Z/(p2) or to Z/(p) × Z/(p).
Proof. Let G be a group with order p2. By Lagrange, non-identity elements in G have order
p or p2.
If there is an element of G with order p2, then G is cyclic and therefore isomorphic to
Z/(p2) (in many ways). We may henceforth assume G has no element of order p2. That
means every non-identity element of G has order p.
From Theorem 6.8, there is a non-identity element in the center of G. Call it a. Since a
has order p, ⟨a⟩is not all of G. Choose b ∈G −⟨a⟩. Then b also has order p. We are going
to show powers of a and powers of b provide an isomorphism of G with Z/(p) × Z/(p). Let
f : Z/(p) × Z/(p) →G by
f(i, j) = aibj.
This is well-deﬁned since a and b have order p. It is a homomorphism since powers of a are
in the center:
f(i, j)f(i′, j′) = (aibj)(ai′bj′)
= aiai′bjbj′
= ai+i′bj+j′
= f(i + i′, j + j′)
= f((i, j) + (i′, j′)).
The kernel is trivial: if f(i, j) = e then ai = b−j. This is a common element of ⟨a⟩∩⟨b⟩,
which is trivial. Therefore ai = bj = e, so i = j = 0 in Z/(p).
Since f has trivial kernel it is injective. The domain and target have the same size, so f
is surjective and thus is an isomorphism.
□
Corollary 6.12. A ﬁnite p-group ̸= {e} has a normal subgroup of order p.
Proof. Let G be a ﬁnite p-group with |G| > 1. By Theorem 6.8, Z(G) is a nontrivial p-
group. Pick g ∈Z(G) with g ̸= e. The order of g is pr for some r ≥1. Therefore gpr−1 has
order p, so Z(G) contains a subgroup of order p, which must be normal in G since every
subgroup of Z(G) is a normal subgroup of G.
□

<!-- page 15 -->
CONJUGATION IN A GROUP
15
We can bootstrap Corollary 6.12 to non-prime sizes by inducting on a stronger hypothesis.
Corollary 6.13. If G is a nontrivial ﬁnite p-group with size pn then there is a normal
subgroup of size pj for every j = 0, 1, . . . , n.
Proof. We argue by induction on n. The result is clear if n = 1. Suppose n ≥2 and the
theorem is true for p-groups of size pn−1. If |G| = pn then it has a normal subgroup N
of size p by the preceding corollary. Then |G/N| = pn−1, so for 0 ≤j ≤n −1 there is a
normal subgroup of G/N with size pj. The pullback of this subgroup to G is normal and
has size pj · |N| = pj+1.
□
Example 6.14. Let G = D4. Its subgroups of size 2 are ⟨s⟩, ⟨rs⟩, ⟨r2s⟩, ⟨r3s⟩, and ⟨r2⟩.
Only the last one is normal. The subgroups of size 4 are ⟨r⟩and ⟨r2, s⟩. Both are normal.
Appendix A. Conjugacy in plane geometry
We will show that all reﬂections in R2 are conjugate to reﬂection across the x-axis in an
appropriate group of transformations of the plane.
Deﬁnition A.1. An isometry of R2 is a function f : R2 →R2 that preserves distances: for
all points P and Q in R2, the distance between f(P) and f(Q) is the same as the distance
between P and Q.
Isometries of R2 include: translations, rotations, and reﬂections.2 Isometries are invert-
ible (this requires proof, or include it in the deﬁnition if you want to be lazy about it), and
under composition isometries form a group.
There are two ways to describe points of the plane algebraically, using vectors or complex
numbers. We will work with points as complex numbers. The point (a, b) is considered as
the complex number a + bi. We measure the distance to a + bi from 0 with the absolute
value
|a + bi| =
p
a2 + b2,
and the distance between a + bi and c + di is the absolute value of their diﬀerence:
|(a + bi) −(c + di)| =
p
(a −c)2 + (b −d)2.
To each complex number z = a + bi, we have its complex conjugate z = a −bi. By an
explicit calculation, complex conjugation respects sums and products:
z + z′ = z + z′,
zz′ = zz′.
Two important algebraic properties of the absolute value on C are its behavior on prod-
ucts and on complex conjugates:
|zz′| = |z||z′|,
|z| = |z|.
In particular, if |w| = 1 then |wz| = |z|.
An example of a reﬂection across a line in the plane is complex conjugation:
s(z) = z.
This is reﬂection across the x-axis. It preserves distance:
|s(z) −s(z′)| = |z −z′| = |z −z′| = |z −z′|.
2A full description of isometries of R2 includes glide reﬂections. See https://kconrad.math.uconn.edu/
blurbs/grouptheory/isometrycpx.pdf or https://kconrad.math.uconn.edu/blurbs/grouptheory/isome
tryR2.pdf.

<!-- page 16 -->
16
KEITH CONRAD
We will compare this reﬂection with the reﬂection across another line, ﬁrst treating other
lines through the origin and then treating lines that may not pass through the origin.
Pick a line through the origin that makes an angle, say θ, with respect to the positive
x-axis. We can rotate the x-axis onto that line by rotating the x-axis counterclockwise
around the origin through an angle of θ. A rotation around the origin, in terms of complex
numbers, is multiplication by the number cos θ + i sin θ, which has absolute value 1. Let’s
denote counterclockwise rotation around the origin by θ by rθ:
(A.1)
rθ(z) = (cos θ + i sin θ)z,
| cos θ + i sin θ| = 1.
Every rotation rθ preserves distances:
|rθ(z) −rθ(z′)| = |(cos θ + i sin θ)(z −z′)| = |(cos θ + i sin θ)||z −z′| = |z −z′|.
Composing rotations around the origin amounts to adding angles: rθ ◦rϕ = rθ+ϕ.
In
particular, r−1
θ
= r−θ since rθ ◦r−θ = r0, which is the identity (r0(z) = z).
Now let’s think about some reﬂections besides complex conjugation. Let sθ be the reﬂec-
tion across the line through the origin making an angle of θ with the positive x-axis. (In
particular, complex conjugation is s0.) Draw some pictures to convince yourself visually
the reﬂection sθ is the composite of
• rotation of the plane by an angle of −θ to bring the line of reﬂection onto the x-axis,
• reﬂection across the x-axis,
• rotation of the plane by θ to return the line to its original position.
This says
(A.2)
sθ = rθsr−θ = rθsr−1
θ .
So we see, in this algebraic formula, that a reﬂection across each line through the origin
is conjugate, in the group of isometries of the plane, to reﬂection across the x-axis. The
conjugating isometry is the rotation rθ that takes the line through the origin at angle θ to
the x-axis.
In order to compare complex conjugation to reﬂection across an arbitrary line, which need
not pass through the origin, we bring in additional isometries: translations. A translation
in the plane can be viewed as adding a particular complex number, say w, to every complex
number: tw(z) = z + w. This is an isometry since
|tw(z) −tw(z′)| = |(z + w) −(z′ + w)| = |z −z′|.
Note tw ◦tw′ = tw+w′, and the inverse of tw is t−w: t−1
w = t−w.
In order to describe reﬂection across an arbitrary line in terms of complex conjugation,
we need to describe an arbitrary line. A line makes a deﬁnite angle with respect to the
positive x-direction (how far it tilts). Call that angle θ. Now pick a point on the line. Call
it, say, w. Our line is the only line in the plane that passes through w at an angle of θ
relative to the positive x-direction.
We can carry out reﬂection across this line in terms of reﬂection across the line parallel
line to it through the origin by using translations, in 3 steps:
• translate back by w (that is, apply t−w) to carry the original line to a line through
the origin at the same angle θ,
• reﬂect across this line through the origin (apply sθ),
• translate by w to return the line to its original position (apply tw).

<!-- page 17 -->
CONJUGATION IN A GROUP
17
Putting this all together, with (A.2), reﬂection across the line through w that makes an
angle of θ with the positive x-direction is the composite
(A.3)
twsθt−w = tw(rθsr−1
θ )t−1
w = twrθs(twrθ)−1.
This is a conjugate of complex conjugation s in the group of isometries in the plane.
Let’s summarize what we have shown.
Theorem A.2. In the group of isometries of the plane, reﬂection across a line is conjugate
to reﬂection across the x-axis.
Example A.3. Reﬂection across the horizontal line y = b corresponds to θ = 0 and w = bi.
That is, this reﬂection is tbist−bi: translate down by b, reﬂect across the x-axis, and then
translate up by b.
Appendix B. Bounding a Group’s Size by its Number of Conjugacy Classes
Up to isomorphism there obviously are only ﬁnitely many ﬁnite groups with a given size.
What might be more surprising is that, up to isomorphism, there are only ﬁnitely many
ﬁnite groups with a given number of conjugacy classes. The following theorem was proved
by Landau [9] in 1903.
Theorem B.1. The size of a ﬁnite group can be bounded above from knowing the number
of its conjugacy classes.
Proof. When there is only one conjugacy class, the group is trivial. Now ﬁx a positive
integer k > 1 and let G be a ﬁnite group with k conjugacy classes represented by g1, . . . , gk
(this includes gi’s in the center). Recall (6.3):
(B.1)
|G| =
k
X
i=1
|G|
|Z(gi)|.
Dividing (B.1) by |G|,
(B.2)
1 = 1
n1
+ 1
n2
+ · · · + 1
nk
,
where ni = |Z(gi)|, Each ni exceeds 1 when G is nontrivial. Write the ni’s in increasing
order, with possible repetitions:
(B.3)
n1 ≤n2 ≤· · · ≤nk.
Each ni is at most |G|, and when g ∈Z(G) we have |Z(g)| = |G|, so nk = |G|. Since
ni ≥n1 for all i, (B.2) implies
1 ≤k
n1
,
so
(B.4)
n1 ≤k.
Then, using ni ≥n2 for i ≥2,
1 ≤1
n1
+ k −1
n2
.

<!-- page 18 -->
18
KEITH CONRAD
Thus 1 −1/n1 ≤(k −1)/n2, so
(B.5)
n2 ≤
k −1
1 −1/n1
.
By induction,
(B.6)
nm ≤
k + 1 −m
1 −( 1
n1 + · · · +
1
nm−1 )
for m ≥2.
Since (B.4) bounds n1 from above by k and (B.6) bounds each of n2, . . . , nk from above
in terms of earlier ni’s, there are only a ﬁnite number of k-tuples (n1, . . . , nk). The k-tuples
among these that satisfy (B.2) can be tabulated. We saw earlier that nk = |G|, so the
(n1, . . . , nk) satisfying (B.2) and (B.3) with the largest value for nk gives an upper bound
on the size of a ﬁnite group that has k conjugacy classes.
□
The number of conjugacy classes in a ﬁnite group is called the class number of the group.3
The identity element is its own conjugacy class, so the only ﬁnite group with class number
1 is the trivial group.
Burnside [4, p. 461–462] and Miller [10] in 1911 independently
determined all ﬁnite groups (up to isomorphism) with class number 2, 3, 4, and 5. Poland
[11] determined the groups with class number 6 and 7. A complete list of groups with class
number k is known for k ≤14 [13]. Results for k ≤7 are below.4
A group of order n has at most n conjugacy classes, and there are n conjugacy classes if
and only if the group is abelian. Therefore a list of ﬁnite groups with k conjugacy classes
will include all the abelian groups of order k. When k ≥3, k is the number of conjugacy
classes of at least one non-abelian group: D2k−3. By Theorem 4.1, the conjugacy classes
in D2k−3 are {1}, {r±i} for 1 ≤i ≤k −2, and the conjugacy class of all reﬂections, so the
number of conjugacy classes is 1 + (k −2) + 1 = k.
Example B.2. Taking k = 2, the only solution to (B.2) is (2, 2). Thus a ﬁnite group
with two conjugacy classes must have order 2, and this works since groups of order 2 are
abelian. There are inﬁnite groups with exactly two conjugacy classes, but they are not easy
to describe: see https://mathoverflow.net/questions/146799.
Example B.3. When k = 3, the (n1, n2, n3) satisfying (B.2) and (B.3) are (2,4,4), (2,3,6),
and (3,3,3). Thus |G| ≤6. The group S3 ∼= D3 has size 6 with 3 conjugacy classes while
Z/(3) has size 3 with 3 conjugacy classes.
Example B.4. When k = 4, there are 14 solutions to (B.2) and (B.3), such as (4,4,4,4)
and (2,3,7,42). The second 4-tuple is the solution with the largest value of n4, so a ﬁnite
group with 4 conjugacy classes has size at most 42. In actuality, the ﬁnite groups with 4
conjugacy classes are Z/(4), (Z/(2))2, D5, and A4, so the largest order of such a group is
12.
Example B.5. When k = 5, there are 148 solutions to (B.2) and (B.3), and the largest
n5 that occurs is 1806. The ﬁnite groups with 5 conjugacy classes are Z/(5), Q8, D4, D7,
Aﬀ(Z/(5)), S4, A5, and the nonabelian group of size 21, so the largest order of such a group
is |A5| = 60.
3The term “class number” is used in algebraic number theory with an entirely diﬀerent meaning as the
size of the ideal class group of a number ﬁeld.
4For more information, see https://mathoverflow.net/questions/237499.

<!-- page 19 -->
CONJUGATION IN A GROUP
19
Example B.6. The ﬁnite groups with 6 conjugacy classes are Z/(6), D6, D9, Z/(3)⋊Z/(4),
Z/(3) ⋊S3, Aﬀ(F9), {( a b
0 1 ) : a, b ∈F9, a4 = 1}, and PSL2(Z/(7)). The largest order among
these 8 groups is |PSL2(Z/(7))| = 168.
In the semidirect products Z/(3)⋊Z/(4) and Z/(3)⋊S3, the action of Z/(4) on Z/(3) and
S3 on Z/(3) is by inversion through natural homomorphisms to {±1}: k mod 4 7→(−1)k
and σ 7→sign(σ).
Example B.7. The 12 ﬁnite groups with 7 conjugacy classes are Z/(7), D8, D11, S5, A6,
Aﬀ(Z/(7)), SL2(Z/(3)), {( a b
0 1 ) : a, b ∈Z/(13), a3 = 1}, {( a b
0 1 ) : a, b ∈Z/(13), a4 = 1},
{( a b
0 1 ) : a, b ∈Z/(11), a5 = 1}, Q16 (generalized quaternion group of order 16),5 and the
subgroup of order 16 in GL2(Z/(3)). The group of largest order is |A6| = 360.
For each k ∈Z+, all suﬃciently large ﬁnite groups have more than k conjugacy classes
by Theorem B.1. Let c(n), for n ≥1, be the fewest number of conjugacy classes among all
groups of order n. so c(n) →∞as n →∞. Can this growth be quantiﬁed? In 1963, Brauer
showed c(n) ≥log2 log2 n for n ≥2 (note log2 log2 2 = 0). In 1992, Pyber [12] gave an expo-
nential improvement by essentially removing one logarithm: c(n) ≥A log2(n)/(log2 log2 n)8
for some constant A > 0. His proof relies on the classiﬁcation of ﬁnite simple groups. Almost
20 years later, Keller [8] in 2011 reduced the exponent in Pyber’s lower bound from 8 to 7. In
2015, Baumeister, Mar´oti, and Tong-Viet [1] reduced the exponent to an arbitrary number
greater than 3: for all ε > 0 there is Aε > 0 such that c(n) ≥Aε log2 n/(log2(log2 n))3+ε for
n ≥3. Their proof, like the earlier work, uses the classiﬁcation of ﬁnite simple groups. It is
natural to guess that c(n) ≥A log2 n for some A > 0. Bertram [2] conjectured c(n) > log3 n
for n ≥1.
There is a logarithmic upper bound on c(n) for inﬁnitely many n: for prime p, the set of
mod p polynomials modulo xp+2 with constant term 0, which is
{x + a2x2 + · · · + ap+1xp+1 mod xp+2 : ai ∈Z/(p)},
forms a ﬁnite group under composition (not under multiplication!)6 with order pp and turns
out to have at most p3 conjugacy classes [6, Sect. 3.3]. For large p, p3 is logarithmically
smaller than pp: setting n = pp, so log n = p log p > p (for p ≥3), we have p3 < (log n)3.
Therefore c(n) < (log n)3 when n = pp for all odd primes p. This is not true for p = 2, since
all groups of order 4 are abelian, so c(4) = 4 > 1 > (log 2)3.
For all n, a group of order n has at most n conjugacy classes, so c(n) ≤n, and c(n) = n
if all groups of order n are abelian. That occurs inﬁnitely often, e.g., when n is prime.
References
[1] B. Baumeister, A. Mar´oti, and H. P. Tong-Viet, Finite groups have more conjugacy classes, Forum Math.
29 (2017), 259–275.
[2] E. A. Bertram, New reductions and logarithmic lower bounds for the number of conjugacy classes inﬁnite
groups, Bull. Aust. Math. Soc. 87 (2013), 406–424.
[3] A. Bensaid and R. W. van der Waall, On ﬁnite groups all of whose elements of equal order are conjugate,
Simon Stevin 65 (1991), 361–374.
[4] W. Burnside, “Theory of groups of ﬁnite order,” 2nd ed., Cambridge Univ. Press, Cambridge, 1911. URL
https://catalog.hathitrust.org/Record/000419368.
5See https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf.
6For p = 2 this group is abelian, since all groups of order 4 are, but for p ≥3 this group is nonabelian
since f(x) = x + x2 and g(x) = x + x3 don’t commute: f(g(x)) = x + x2 + x3 + 2x4 mod x5 and g(f(x)) =
x + x2 + x3 + 3x4 mod x5.

<!-- page 20 -->
20
KEITH CONRAD
[5] C. Christensen, Polish Mathematicians Finding Patterns in Enigma Messages, Amer. Math. Monthly
80 (2007), 247–273. URL https://www.maa.org/sites/default/files/pdf/upload library/22/Allen
doerfer/christensen247.pdf.
[6] P. Etingof, On some properties of quantum doubles of ﬁnite groups, J. Algebra 394 (2013), 1–6. URL
https://arxiv.org/pdf/1208.4874.pdf.
[7] P. Fitzpatrick, Order conjugacy in ﬁnite groups, Proc. Roy. Irish Acad. Sect. A 85 (1985), 53–58.
[8] T. M. Keller, Finite groups have even more conjugacy classes, Israel J. Math. 181 (2011), 433–444.
[9] E. Landau, ¨Uber die Klassenzahl der bin¨aren quadratischen Formen von negativer Discriminante, Math.
Ann. 56 (1903), 671-676. URL https://eudml.org/doc/158080.
[10] G. A. Miller, Groups involving only a small number of sets of conjugate operators, Arch. Math.
und Phys. 17 (1911), 199–204. URL https://babel.hathitrust.org/cgi/pt?id=njp.32101033960566
&view=1up&seq=221.
[11] J. Poland, Finite groups with a given number of conjugate classes, Canadian J. Math. 20 (1968),
456–464.
[12] L. Pyber, Finite groups have many conjugacy classes, J. London Math. Soc. 46 (1992), 239–249.
[13] A. Vera-L´opez and J. Sangroniz, The ﬁnite groups with thirteen and fourteen conjugacy classes, Math.
Nachr. 280 (2007), 676–694.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*