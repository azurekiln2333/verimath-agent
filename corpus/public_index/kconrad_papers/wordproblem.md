# Wordproblem

> **Source**: https://kconrad.math.uconn.edu/blurbs/wordproblem.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
WHY WORD PROBLEMS ARE HARD
KEITH CONRAD
1. Introduction
The title above is a joke. Many students in school hate word problems. We will discuss
here a speciﬁc question in group theory that happens to be named “the word problem” and
in general it can’t be solved. This does not mean word problems in school are pointless,
despite what Paige thinks in the FoxTrot cartoon below.
Before explaining what “the word problem” is we discuss decision problems. A decision
problem is, roughly, a question with a yes/no answer. Here are some examples.
• Are two given positive integers relatively prime?
• Is a given positive integer a prime number?
• Are two given matrices in GLn(Q) conjugate?
We call a decision problem decidable if there is an algorithm that always determines
(correctly!) whether or not each instance of the problem has the answer yes or no. Note we
are asking for one algorithm that handles all cases: we want to settle all instances of the
problem by common procedure. The decision problems above are all decidable:
• Euclid’s algorithm tells us in ﬁnitely many steps if two positive integers are relatively
prime.
• Trial division tells us in ﬁnitely many steps if a positive integer is prime. This may
be very ineﬃcient (e.g., for the number 282,589,933 −1), but it works.
• Conjugacy of matrices in GLn(Q) can be settled by comparing their rational canonical
forms (which is an algorithm taking ﬁnitely many steps, in part since rational numbers
are exactly computable numbers).
We will not give a rigorous deﬁnition of an algorithm, but standard ways to solve math
problems (Gaussian elimination in linear algebra, the Euclidean algorithm in number theory,
and so on) suggests what the concept is all about. A key point is its ﬁnite nature: an algo-
rithm is a procedure with ﬁnitely many steps, like a computer program or proof: programs
and proofs do not have inﬁnite length! To say a decision problem is decidable essentially
means there is an algorithm taking as input each instance of the problem and in ﬁnitely
many steps (the number of steps may vary with the input) terminating with a (correct!)
1

<!-- page 2 -->
2
KEITH CONRAD
yes/no answer; “inﬁnite loops” aren’t allowed. Inﬁnitely many diﬀerent algorithms, one for
each instance of a problem, isn’t what we mean by an algorithm.
A decision problem is intended to have an inherently ﬁnite or countable character to
it. Therefore a question like deciding if two real numbers are equal, or deciding if a real
number is equal to 0, is not considered a decision problem because it is inherently not about
countable objects. For example, you may think showing a real number is 0 shouldn’t be a
decision problem because if we know x = .000000 . . . to a large number of digits, at no ﬁnite
point can we really be sure x = 0, but that’s not why testing equality with 0 in R is not
a decision problem: comparing a real number with 0 need not use decimal expansions. (In
fact, the way we write something is part of the proper description of a decision problem. It
is trivial to decide if an integer is prime if we choose to represent integers by their prime
factorization, yet factoring is considered a hard problem! We normally think of decision
problems for positive integers in terms of representing integers in a way computers would
accept as input, such as their binary expansion.) Deciding if a real number equals 0 is not
considered decision problem because R is uncountable.
In the 1930s, Church and Turing proved independently that there are decision problems
that are undecidable. The particular decision problems they used (e.g., the halting problem
for Turing) were of interest in logic but were not based on another branch of mathematics
(linear algebra, group theory, topology, etc.). Therefore their work had no practical eﬀect
on areas of math outside of logic. Only about 20 years later were examples of undecidable
decision problems found elsewhere in mathematics, namely in group theory.
To explain these group-theoretic problems we will use groups described by a ﬁnite amount
of information even if the groups are inﬁnite, and this will made precise by the concepts of
ﬁnitely generated group, free group, and ﬁnitely presented group. The last concept, ﬁnitely
presented groups, is often not seen in abstract algebra courses. We will explain what each
of the terms means, including examples of each. Theorems will be stated without proofs.
2. Finitely generated groups
Deﬁnition 2.1. A group G is called ﬁnitely generated if it has ﬁnitely many elements
g1, . . . , gn such that every element of G is a ﬁnite product of powers of these elements, allowing
arbitrary integer exponents. We call the gi’s generators of G and write G = ⟨g1, . . . , gn⟩.
Example 2.2. Every ﬁnite group is ﬁnitely generated, using all of its elements as generators.
Example 2.3. The group Zn is inﬁnite, abelian, and ﬁnitely generated with n generators:
the vectors ei = (0, . . . , 1 . . . , 0) with 1 in the i-th component and 0 elsewhere for 1 ≤i ≤n.
Example 2.4. An inﬁnite nonabelian ﬁnitely generated group is

a
b
0
1

: a = ±1, b ∈Z

with generators ( −1 0
0 1 ) and ( 1 1
0 1 ):

1
b
0
1

=

1
1
0
1
b
,

−1
b
0
1

=

1
b
0
1
 
−1
0
0
1

=

1
1
0
1
b 
−1
0
0
1

.
The matrix ( −1 0
0 1 ) has order 2 while the matrix ( 1 1
0 1 ) has inﬁnite order. This group is also
generated by ( −1 0
0 1 ) and ( −1 0
0 1 )( 1 1
0 1 ) = ( −1 −1
0
1 ), which both have order 2: an inﬁnite group
can be generated by two elements of order 2.

<!-- page 3 -->
WHY WORD PROBLEMS ARE HARD
3
There are inﬁnite groups with two generators in which all elements of the group have ﬁnite
order, and in fact there are such groups where all non-identity elements have a common prime
order (Tarski monster). Such groups are known to exist for each prime ≥1009.
A ﬁnitely generated group is at most countable, but the converse is false: Q as an additive
group is countable but is not ﬁnitely generated: for each ﬁnite list of fractions, pick a
prime p not dividing one of the denominators of those fractions. Then 1/p is not in the
subgroup (additively) generated by that ﬁnite list. We don’t really need prime numbers in
that argument: for a ﬁnite list of fractions a1/b1, . . . , an/bn with ai, bi ∈Z and bi ≥1, the
fraction 1/(b1 · · · bn + 1) is not in the subgroup generated by the list since it is in reduced
form with a denominator that is relatively prime to each bi (and is greater than 1).
Finitely generated abelian groups have an elementary abstract structure: they are each
isomorphic to a direct product Zr × C1 × · · · × Ck, where r ≥0 and the Ci’s are ﬁnite
cyclic groups. But this does not mean ﬁnitely generated abelian groups that show up in
mathematics are always easy to understand! There are hard theorems in number theory
(e.g., Dirichlet’s unit theorem and the Mordell-Weil theorem) asserting that certain abelian
groups are ﬁnitely generated, and determining an explicit set of generators for such a group
(or perhaps even the number of generators of such a group) can be a hard computational
task.
3. Free groups
Deﬁnition 3.1. The free group on n letters, Fn, is a group generated by n elements x1, . . . , xn
that have “no relations”. Every element of Fn is just a string of symbols, like
x1x2
2x−1
3 x2x5
1x−3
2 ,
with the only cancellation allowed coming from xix−1
i
= 1 and x−1
i xi = 1.
The group F1 is inﬁnite cyclic, so F1 ∼= Z. For n ≥2, Fn is noncommutative. In fact,
two elements of Fn commute if and only they are powers of a common element of Fn. Every
element in Fn can be written in just one way as a product of powers of x1, . . . , xn, so when
n ≥2 the generating set {x1, . . . , xn} is like a noncommutative basis.
A natural source of free groups in mathematics is topology.
Example 3.2. Consider the plane with 2 points removed. Every path in the plane that
doesn’t go through the two missing points will go a deﬁnite number of times around each
point, with (say) counterclockwise turns counting positively and clockwise turns counting
negatively. Focusing only on paths that are loops starting and ending at a common point
in this twice-punctured plane, going once around each point in succession depends on which
point is looped around ﬁrst: the fundamental group of a twice-punctured plane is nonabelian1
and turns out to be isomorphic to the free group F2, with the two generators being loops
(up to homotopy) going once around just one of the two points.
More generally, the fundamental group of the plane with n points removed is isomorphic
to Fn. This shows that free groups are mathematical objects arising in areas other than pure
group theory.
The reason free groups are called “free” is that we can build homomorphisms out of them
by sending the xi’s anywhere we wish (free choice). This is like bases in vector spaces being
“free” for building linear mappings to other vector spaces: when you say where a basis goes,
1Pictures explaining this are at https://math.stackexchange.com/questions/1802198.

<!-- page 4 -->
4
KEITH CONRAD
there is a unique linear map with that eﬀect on the basis. Similarly, if G is a group with n
elements g1, . . . , gn in G (no restriction on them, and they could even all be equal), there is
a unique group homomorphism Fn →G such that xi 7→gi for i = 1, . . . , n.
All vector spaces have a basis, but not all groups are free, e.g., a nontrivial ﬁnite group is
not free: all elements have ﬁnite order, and an element of order 6, say, can be mapped under
a homomorphism only to elements of order dividing 6, so there’s a constraint on where it
could go under a homomorphism.
Every ﬁnitely generated group can be linked to some free group Fn by using quotient
groups.
Theorem 3.3. Every ﬁnitely generated group with n generators is a quotient group of Fn.
Proof. Let G have generators g1, . . . , gn. There’s a homomorphism f : Fn →G with f(xi) =
gi. It’s surjective since the image of f is a subgroup of G containing the generators g1, . . . , gn,
and the only such subgroup is G. Therefore G = Im(f) ∼= Fn/ ker f.
□
We deﬁned free groups with a ﬁnite number of generators. Replacing x1, . . . , xn in the
deﬁnition of Fn with a possibly inﬁnite alphabet, we get the concept of a free group in
general, and the reasoning in the proof of Theorem 3.3 shows every group is a quotient of
some free group.
A ﬁnitely generated group, as described in Deﬁnition 2.1, may look like a “nonabelian”
analogue of a ﬁnite-dimensional vector space. A subspace of an n-dimensional vector space
has dimension at most n. If a group G has n generators, does every subgroup have at most
n generators? Yes if G is abelian, but in general no.
Theorem 3.4. Every subgroup of ﬁnite index in a ﬁnitely generated group is ﬁnitely gener-
ated.
Watch out! Theorem 3.4 does not say the number of generators of the subgroup is at most
the number of generators of the original group, and for nonabelian groups often it is not.
Example 3.5. If G = Fn and [G : H] = m then H ∼= Fmn−m+1. When n = 1, mn−m+1 = 1
for all m ≥1, so the theorem says every ﬁnite-index subgroup of an inﬁnite cyclic group is
inﬁnite cyclic. When n > 1 and m > 1, mn −m + 1 > n so a proper subgroup of ﬁnite
index in a free group on ﬁnitely many – and at least two – letters requires more generators
than the original group. For example, inside F2 (n = 2) the subgroup ⟨x2, y2, xy⟩has index
2 (m = 2) and is isomorphic to F3 while the subgroup ⟨x3, y3, xy, yx⟩has index 3 (m = 3)
and is isomorphic to F4.
Theorem 3.6. A normal subgroup of Fn other than {1} is ﬁnitely generated if and only if
it has ﬁnite index.
Therefore a nontrivial normal subgroup of Fn with inﬁnite index is not ﬁnitely generated.
Example 3.7. The commutator subgroup [Fn, Fn] of Fn is normal and Fn/[Fn, Fn] ∼= Zn, so
[Fn, Fn] has inﬁnite index in Fn, and [Fn, Fn] is nontrivial for n ≥2 (since Fn is nonabelian),
so for n ≥2, [Fn, Fn] is not ﬁnitely generated by Theorem 3.6.
We have seen that the property “ﬁnitely generated” is not preserved when passing to
subgroups in general, but it is preserved if we stick to subgroups of ﬁnite index (Theorem
3.4). Perhaps surprisingly, being “free” is preserved for all subgroups.
Theorem 3.8 (Nielsen, Schreier). Every subgroup of a free group is free.

<!-- page 5 -->
WHY WORD PROBLEMS ARE HARD
5
This result is not limited to the groups Fn: free groups in Theorem 3.8 may have an inﬁnite
generating set (or an empty generating set: the trivial group is the free group on the empty
alphabet). The theorem was proved by Nielsen (1921) for ﬁnitely generated subgroups and
by Schreier (1926) for general subgroups. Their proofs were purely algebraic, but later a
proof was found by Baer and Levi (1936) that interprets the theorem through the lens of
topology: a free group can be made into a fundamental group of a space and each subgroup
is the fundamental group of a covering space. A second proof using topology was found
much later by Serre (1970).
The Nielsen–Schreier theorem may at ﬁrst seem trivial, because in a free group there are
“no relations” among the generators other than what comes from the axioms of group theory
(like xx−1 = 1), so how could a subgroup of a free group not be free? The subtlety is that the
generators of the original free group don’t have to lie in the subgroup, so how do you know
a subgroup has its own generators ﬁtting the condition for being a free group? If you still
don’t see the subtlety, consider the group Z = F1: proving every subgroup of Z is trivial or
inﬁnite cyclic (hence isomorphic to F∅or F1) requires some work since subgroups of Z need
not be given in a form that makes them obviously cyclic, e.g., 20Z + 36Z or the subgroup of
Z generated by all perfect numbers. Since 6 and 28 are perfect and (6, 28) = 2, the subgroup
generated by all perfect numbers is 2Z if all perfect numbers are even or Z if there is an
odd perfect number. Whether or not there is an odd perfect number is a famous unsolved
problem (it is expected that there is no odd perfect number), and until the problem is settled
it is impossible to compute the subgroup of Z generated by all perfect numbers. But we can
still say the abstract structure of this subgroup is inﬁnite cyclic.
Another property to compare between groups and subgroups is being nonabelian. Sub-
groups of a nonabelian group may or may not be nonabelian (the trivial subgroup certainly
is abelian).
When you have a property of a group that involves a choice of elements in the group (being
cyclic, being nonabelian, and being free are all such properties) and you pass to a subgroup
not containing those elements, it’s not clear if the subgroup should still satisfy the same
property. Sometimes the property may no longer hold (being nonabelian) and sometimes it
always does (being cyclic, being free). This is why Theorem 3.8 is substantial.
4. Finitely presented groups
We have seen that a normal subgroup of a ﬁnitely generated group need not be ﬁnitely
generated (Example 3.7). The property of a subgroup being ﬁnitely generated uses only the
operations of multiplication and inversion in the subgroup to create new elements from an
initial set of elements of the subgroup. In a normal subgroup, there is a further way to create
new elements of it from elements we already have in the subgroup: conjugation by elements
of the bigger group it’s normal in. If a normal subgroup of a ﬁnitely generated group can’t
be built from ﬁnitely many of its own elements by multiplication and inversion, it might be
built from ﬁnitely many of its own elements by multiplication, inversion, and conjugation by
the larger group it is normal in. In other words, a normal subgroup that is not generated by
ﬁnitely many of its elements might be generated by ﬁnitely many of its conjugacy classes.
Example 4.1. In F2 = ⟨x, y⟩, the subgroup [F2, F2] is not ﬁnitely generated, but it contains
the commutator [x, y] = xyx−1y−1 and [F2, F2] is generated by the single commutator [x, y]
together with all of its (inﬁnitely many) conjugates in F2. That means we can get all of
[F2, F2] by using in all possible ways the operations of multiplication and inversion on the

<!-- page 6 -->
6
KEITH CONRAD
elements in the conjugacy class of [x, y] in F2. This makes [F2, F2] “ﬁnitely generated” in a
wider sense than just by using the group law of F2 on [x, y] alone: we use the group law of
F2 on all conjugates of [x, y] in F2.
Deﬁnition 4.2. A group G is called ﬁnitely presented if it is isomorphic to Fn/N for some
n, where N is a normal subgroup of Fn that is generated by a ﬁnite subset R in Fn and all
the conjugates of elements of R in Fn.
A ﬁnitely presented group is a special type of ﬁnitely generated group. In the homomor-
phism Fn ↠G with kernel N, let gi ∈G be the image of xi, so G = ⟨g1, . . . , gn⟩. An element
of Fn is in N when setting each xi equal to gi turns the element of Fn into the identity in G.
For instance, having x2
1x3
2 ∈N means g2
1g3
2 = 1 in G, or equivalently g2
1 = g−3
2 . View N as
the “relations” among the gi’s generating G: all strings in the xi’s that are trivial when xi is
replaced by gi. So R is a ﬁnite set of “relations” explaining all relations among the gi’s (all ele-
ments of N). The conjugate of a relation is a relation: if f(g1, . . . , gn) = 1 where f(x1, . . . , xn)
is a product of powers of x1, . . . , xn, then w(g1, . . . , gn)f(g1 . . . , gn)w(g1, . . . , gn)−1 = 1 too
where w(x1, . . . , xn) is an arbitrary element of Fn.
We write a ﬁnitely presented group as ⟨X | R⟩where X = {x1, . . . , xn} consists of the
standard generators of Fn and R is a ﬁnite subset of Fn that generates N by multiplication,
inversion, and conjugation by Fn: N is the smallest normal subgroup of Fn containing R.
Equivalently, N is the subgroup generated by the conjugacy classes of the elements of R:
N is generated by ﬁnitely many conjugacy classes rather than just ﬁnitely many elements.2
Here R need not be a generating set of N; we need to include conjugates of elements of R
to get a generating set for N, so it is the conjugacy classes of elements of R that generate
N. The table below gives examples of ﬁnite presentations of groups.
G
Presentation of G
Z
⟨x | ∅⟩
Z/(n)
⟨x | xn⟩
Dn
⟨x, y | xn, y2, yxy−1x⟩
Z2
⟨x, y | xy(yx)−1⟩
Table 1. Finitely Presented Groups
The presentation of Dn in Table 1 comes from its description as having two generators r and
s where r has order n (so rn = 1), s has order 2 (so s2 = 1), and srs−1 = r−1 (so srs−1r = 1).
Since the condition rn = 1 does not require r to have order n and s2 = 1 does not require s
to have order 2, there are groups besides Dn with two generators satisfying the three rules
rn = 1, s2 = 1, and srs−1r = 1 (consider the trivial group, taking r and s to be trivial), but
Dn is the one with generators subject to those three rules and “no further information”. That
is what it means to be the quotient group of F2 = ⟨x, y⟩by the normal subgroup generated
by xn, y2, and yxy−1x. A rigorous proof that ⟨x, y | xn, y2, yxy−1x⟩∼= Dn is Theorem 1.1 in
https://kconrad.math.uconn.edu/blurbs/grouptheory/dihedral2.pdf.
Let’s look at three more group presentations.
2If a subset S of a group is closed under conjugation then the subgroup generated by S is a normal
subgroup. That is, the subgroup generated by a set of conjugacy classes in a group is a normal subgroup.

<!-- page 7 -->
WHY WORD PROBLEMS ARE HARD
7
Example 4.3. Let
G = ⟨x, y | x7, y4, xyx−1y⟩.
This is the “universal” group where x7 = 1, y4 = 1, and xyx−1 = y−1. You might think
intuitively that |G| = 7 · 4 = 28, just as |Dn| = 2n, but in fact G is cyclic of order 14.
Step 1: xy = yx. In G we have xyx−1 = y−1, so conjugating both sides by x gives us
x2yx−2 = xy−1x−1 = (xyx−1)−1 = (y−1)−1 = y,
so x2y = yx2: y commutes with x2. Then y commutes with all powers of x2, which includes
(x2)4 = x8 = x · x7 = x since x7 = 1.
Step 2: y2 = 1.
Since x and y commute, y−1 = xyx−1 = yxx−1 = y, so y2 = 1.
Step 3: G is cyclic of order 14.
Since x and y commute with x7 = 1 and y2 = 1, every element of G has the form xiyj
where 0 ≤i ≤6 and 0 ≤j ≤1, so |G| ≤14. We’ll show there is a homomorphism from G
onto Z/(14), so |G| = 14 and thus G ∼= Z/(14).
There is a (unique) homomorphism F2 →Z/(14) where x 7→2 and y 7→7. Its kernel
contains x7, y4, and xyx−1y, so this homomorphism F2 →Z/(14) induces a homomorphism
G →Z/(14). Its image contains ⟨2, 7 mod 14⟩= Z/(14), so we have a surjective homomor-
phism G →Z/(14).
Example 4.4. Let
G = ⟨x, y | xyx−1y−2, x−2y−1xy⟩.
In G, xyx−1y−2 = 1 and x−2y−1xy = 1, so xy = y2x and xy = yx2. Thus y2x = yx2.
Canceling y on the left sides gives yx = x2, and canceling x on the right gives y = x.
Therefore the equation xy = yx2 in G says x2 = x3, so x = 1 and thus y = 1: G is trivial!
Often the elements of R in ⟨X | R⟩are written as equations to make the constraints more
intuitive. In the case of G above, we might write G = ⟨x, y | xy = y2x, xy = yx2⟩.
Example 4.5. The ﬁnitely presented group ⟨x, y | x−1y2x = y3, y−1x2y = x3⟩is trivial, but
the proof that this group is trivial is rather tricky.3
The elements of a ﬁnitely presented group ⟨X | R⟩can be thought of as strings of symbols
taken from X, so these strings are called words in X.
They may collapse in the group
⟨X | R⟩, but not in the free group ⟨X⟩∼= Fn whose quotient Fn/N is the group ⟨X | R⟩. It
is in the free group ⟨X⟩where diﬀerent words live as independent elements.
Since ﬁnitely presented groups are ﬁnitely generated, ﬁnite-index subgroups of ﬁnitely
presented groups are ﬁnitely generated by Theorem 3.4. But are they ﬁnitely presented?
Theorem 4.6. Every subgroup of ﬁnite index in a ﬁnitely presented group is ﬁnitely pre-
sented.
Some subgroups of a ﬁnitely presented group are not ﬁnitely presented. This was ﬁrst
shown by Dehn (1911). Here is an example.
Example 4.7. The group F2 × F2 = ⟨x, y⟩× ⟨z, w⟩is ﬁnitely presented (it is not F4, since x
and y commute with z and w). Deﬁne the homomorphism f : F2 ×F2 →Z by x, y, z, w 7→1.
Then ker f is a ﬁnitely generated subgroup of F2×F2, with generators xy−1, xz−1, and xw−1,
but ker f is not ﬁnitely presented.
3See https://math.stackexchange.com/questions/66573.

<!-- page 8 -->
8
KEITH CONRAD
5. Decision problems about groups
Here are several decision problems about a ﬁnitely presented group G = ⟨X | R⟩. The
ﬁrst one is the problem in our title.
(1) Word Problem: Can we decide if two words in X are equal in G?
(2) Generalized Word Problem: Given words w1, . . . , wn, w in X, can we decide if w is
in the subgroup ⟨w1, . . . , wn⟩when viewed in G?
(3) Conjugacy Problem: Can we decide if two words in X are conjugate in G?
(4) Isomorphism Problem: Can we decide if two ﬁnitely presented groups ⟨X | R⟩and
⟨Y | S⟩are isomorphic? A special case of this: can we decide if a ﬁnitely presented
group is trivial?
Tietze posed the isomorphism problem for ﬁnitely presented groups in 1908. Dehn posed
the word problem and conjugacy problem in 1911. (Both Tietze and Dehn were topologists.
Much of the early work on ﬁnitely presented groups was motivated by the occurrence of such
groups in algebraic topology as fundamental groups.) The generalized word problem was
posed by Mihailova in 1958. For two ﬁnite presentations of a group, there is a systematic
way (Tietze transformations) to convert one into the other in ﬁnitely many steps, so the
above questions are each algorithmically insensitive to the choice of ﬁnite presentation.
Since g = h in a group if and only if gh−1 = e, the word problem in G = ⟨X | R⟩is
equivalent to the problem of deciding when words in X are trivial in G. If the conjugacy
problem can be settled in a speciﬁc group, then so can the word problem: g = h if and only
if gh−1 = e, and gh−1 = e if and only if gh−1 is conjugate to e. Thus a group for which the
word problem is undecidable is also a group for which the conjugacy problem is undecidable.
The word problem is decidable for some types of groups: Artin settled it for braid groups
in 1926, and it can be settled for ﬁnitely generated free groups by writing each word as
a “reduced word”. But in the 1950s Novikov and Boone independently proved there is a
ﬁnitely presented group for which the word problem is undecidable.4
Eventually it was
determined that each of the four decision problems above for ﬁnitely presented groups is
undecidable. The solutions use a group that encodes a known undecidable decision problem
from logic (the halting problem) in such a way that decidability of the group theory problem
implies decidability of the logic problem. Thus undecidability of the logic problem implies
undecidability of the group theory problem. While the original examples of undecidable
decision problems (like the halting problem) were not of direct research interest to non-
logicians, such problems were used in the construction of the groups that showed the group-
theoretic decision problems are undecidable. Currently, the shortest description of a concrete
ﬁnitely presented group with an undecidable word problem has the form ⟨X | R⟩where
|X| = 2 and |R| = 27.5
4In 1947, Markov and Post independently proved the word problem for ﬁnitely presented semigroups is
undecidable. A semigroup is a set with an associative binary operation, like Z+ under addition. Groups
have more structure than semigroups, such as inverses, so the undecidability of the word problem for ﬁnitely
presented semigroups does not imply undecidability of the word problem for ﬁnitely presented groups even
though every group is a semigroup.
5See https://eprint.iacr.org/2014/528.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*