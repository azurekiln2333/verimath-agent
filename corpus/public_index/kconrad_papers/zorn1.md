# Zorn's Lemma I

> **Source**: https://kconrad.math.uconn.edu/blurbs/zorn1.pdf  
> **Author**: Keith Conrad  
> **Topic**: algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
ZORN’S LEMMA AND SOME APPLICATIONS
KEITH CONRAD
1. Introduction
Zorn’s lemma is a result in set theory that appears in proofs of some non-constructive
existence theorems throughout mathematics. We will state Zorn’s lemma below and use it in
later sections to prove results in group theory, ring theory, linear algebra, and topology. In
an appendix we give an application of Zorn’s lemma to metric spaces. While Zorn’s lemma
has its origins in the early 20th century, it still retains a certain amount of “controversy”
and we discuss why this is the case in the last section.
The statement of Zorn’s lemma is not intuitive, and some of the terminology in it may be
unfamiliar, but after reading through the explanation of Zorn’s lemma and then the proofs
that use it you should be more comfortable with how it can be applied.
Zorn’s lemma: Let S be a partially ordered set. If every totally ordered subset of S has
an upper bound in S, then S contains a maximal element.
To understand Zorn’s lemma, we need to know four terms: partially ordered set, totally
ordered subset, upper bound, and maximal element.
A partial ordering on a (nonempty) set S is a binary relation on S, denoted ≤, which
satisﬁes the following properties:
• for all s ∈S, s ≤s,
• if s ≤s′ and s′ ≤s then s = s′,
• if s ≤s′ and s′ ≤s′′ then s ≤s′′.
When we ﬁx a partial ordering ≤on S, we refer to S (or, more precisely, to the pair
(S, ≤)) as a partially ordered set.
It is important to notice that we do not assume all pairs of elements in S are comparable
under ≤: for some s and s′ we may have neither s ≤s′ nor s′ ≤s. If all pairs of elements
can be compared (that is, for all s and s′ in S either s ≤s′ or s′ ≤s) then we say S is
totally ordered with respect to ≤.
Example 1.1. The usual ordering relation ≤on R or on Z+ is a partial ordering of these
sets. In fact it is a total ordering on either set. This ordering on Z+ is the basis for proofs
by induction.
Example 1.2. On Z+, declare a ≤b if a | b. This partial ordering on Z+ is diﬀerent from
the one in Example 1.1 and is called ordering by divisibility. It is one of the central relations
in number theory. (Proofs about Z+ in number theory sometimes work not by induction, but
by starting on primes, then extending to prime powers, and then extending to all positive
integers using prime factorization. Such proofs view Z+ through the divisibility relation
rather than through the usual ordering relation.) Unlike the ordering on Z+ in Example
1.1, Z+ is not totally ordered by divisibility: most pairs of integers are not comparable
under the divisibility relation. For instance, 3 doesn’t divide 5 and 5 doesn’t divide 3. The
subset {1, 2, 4, 8, 16, . . . } of powers of 2 is totally ordered under divisibility.
1

<!-- page 2 -->
2
KEITH CONRAD
Example 1.3. Let S be the set of all subgroups of a given group G. For H, K ∈S (that
is, H and K are subgroups of G), declare H ≤K if H is a subset of K. This is a partial
ordering, called ordering by inclusion. It is usually not a total ordering: for most groups G
there are subgroups H and K where H ̸⊂K and K ̸⊂H.
Example 1.4. Let S be the set of linearly independent subsets of Rn (or another vector
space). We can partially order S by inclusion: for two linearly independent subsets L and
L′ in Rn, set L ≤L′ if L ⊂L′.
Example 1.5. On Z+, declare a ≤b if b | a. Here one positive integer is “larger” than
another if it is a factor. This is called ordering by reverse divisibility.
Example 1.6. On the set of subgroups of a group G, declare subgroups H and K to satisfy
H ≤K if K ⊂H. This is a partial ordering on the subgroups of G, called ordering by
reverse inclusion.
In case you think ordering by reverse inclusion seems weird, let’s take a look again
at Example 1.2.
There positive integers are ordered by divisibility, and nothing seems
“backwards.” But let’s associate to each a ∈Z+ the subgroup aZ of Z. Every nonzero
subgroup of Z has the form aZ for a unique positive integer a, aZ = bZ if and only if a = b
(both a and b are positive), and a | b if and only if bZ ⊂aZ. For instance, 4 | 12 and
12Z ⊂4Z. Therefore the partial ordering on Z+ by divisibility (resp., reverse divisibility) is
essentially the same as the partial ordering on nonzero subgroups of Z by reverse inclusion
(resp., by inclusion). Partial ordering by reverse inclusion is used in the construction of
completions of groups and rings.
Example 1.7. Let A and B be sets. Let S be the set of functions deﬁned on some subset
of A with values in B. The subset can vary with the function, but the codomain is always
B. That is, S is the set of pairs (X, f) where X ⊂A and f : X →B. Two elements (X, f)
and (Y, g) in S are equal when X = Y and f(x) = g(x) for all x ∈X.
We can partially order S by declaring (X, f) ≤(Y, g) when X ⊂Y and g|X = f. This
means g is an extension of f to a larger subset of A. Let’s check the second property of a
partial ordering: if (X, f) ≤(Y, g) and (Y, g) ≤(X, f) then X ⊂Y and Y ⊂X, so X = Y .
Then the condition g|X = f means g = f as functions on their common domain, with the
same codomain B, so (X, f) = (Y, g) in S.
Example 1.8. If S is a partially ordered set for the relation ≤and T ⊂S, then the relation
≤provides a partial ordering on T. Thus T is a new partially ordered set under ≤. For
instance, the partial ordering by inclusion on the subgroups of a group restricts to a partial
ordering on the cyclic subgroups of a group.
In these examples, only Example 1.1 is totally ordered. This is typical: most naturally
occurring partial orderings are not total orderings.
However (and this is important) a
partially ordered set can have many subsets that are totally ordered. As a dumb example,
every one-element subset of a partially ordered set is totally ordered. A more interesting
illustration is at the end of Example 1.2 with the powers of 2 inside Z+ under divisibility.
As another example, if we partially order the subspaces of a vector space V by inclusion
then a tower of subspaces
W1 ⊂W2 ⊂W3 ⊂· · ·
where each subspace is a proper subset of the next one is a totally ordered subset of V .
Here is a result about totally ordered subsets that will be useful at a few points later.

<!-- page 3 -->
ZORN’S LEMMA AND SOME APPLICATIONS
3
Lemma 1.9. Let S be a partially ordered set. If {s1, . . . , sn} is a ﬁnite totally ordered
subset of S then there is an si such that sj ≤si for all j = 1, . . . , n.
Proof. The si’s are all comparable to each other; that’s what being totally ordered means.
Since we’re dealing with a ﬁnite set of pairwise comparable elements, there will be one that
is greater than or equal to them all in the partial ordering on S. The reader can formalize
this with a proof by induction on n, or think about the bubble sort algorithm
□
An upper bound on a subset T of a partially ordered set S is an s ∈S such that t ≤s for
all t ∈T. When we say T has an upper bound in S, we do not assume the upper bound is
in T itself; it is just in S.
Example 1.10. In R with its natural ordering, the subset Z has no upper bound while an
upper bound on the subset of negative real numbers is 0 (or a positive real number). No
upper bound on the negative real numbers is a negative real number.
Example 1.11. In the proper subgroups of Z ordered by inclusion, an upper bound on
{4Z, 6Z, 8Z} is 2Z since 4Z, 6Z, and 8Z all consist entirely of even numbers. (Note 4Z ⊂2Z,
not 2Z ⊂4Z.)
A maximal element m of a partially ordered set S is an element that is not below each
element to which it is comparable: for all s ∈S to which m is comparable, s ≤m.
Equivalently, m is maximal when the only s ∈S satisfying m ≤s is s = m. This does
not mean s ≤m for all s in S since we don’t insist that maximal elements are actually
comparable to all elements of S.
Example 1.12. If we partially order linearly independent subsets of Rn by containment,
then a maximal element is a linearly independent subset that is contained in no other
linearly independent subset, and that is what a basis of Rn is: the maximal elements are
the bases of Rn.
Example 1.13. If we partially order Z+ by reverse divisibility (so a ≤b means b | a),
the number 1 is a maximal element. In fact 1 is the only maximal element. This is not a
good example because 1 is comparable to everything in this relation, which is not a typical
feature of maximal elements.
Example 1.14. Consider the positive integers greater than 1 with the reverse divisibility
ordering: a ≤b when b | a. The maximal elements here are the positive integers with
no positive factor greater than 1 except themselves. These are the prime numbers, so the
primes are the maximal elements for the reverse divisibility relation on {2, 3, 4, 5, 6, . . . }.
Equivalently, if we partially order the proper subgroups of Z by inclusion then the maximal
elements are pZ for prime numbers p.
If s ≤m for all s ∈S then we call m a greatest element of S. The special feature of
a greatest element is being maximal and comparable to all of S. A greatest element of
S, when it exists, is the only maximal element of S. A partially ordered set that has no
greatest element could have many maximal elements. For example, the subgroups of Z
partially ordered by containment have Z as its greatest (and only maximal) element, while
the proper subgroups of Z partially ordered by inclusion have no greatest element and have
many maximal elements: subgroups pZ for prime p. We will not be concerned with greatest
elements and it’s best to forget about them here.
We now return to the statement of Zorn’s lemma:

<!-- page 4 -->
4
KEITH CONRAD
If every totally ordered subset of a partially ordered set S has an upper
bound in S, then S contains a maximal element.
All the terms being used here have now been deﬁned.1 Of course this doesn’t mean the
statement should be clearer!
Zorn’s lemma is very nonconstructive: when it can be applied, it provides no mechanism
to ﬁnd a maximal element whose existence it asserts and it says nothing about how many
maximal elements there are. Usually, as in Example 1.14, there are many maximal elements.
In a partially ordered set S we can speak about minimal elements just as much as maximal
elements: m ∈S is called minimal if m ≤s for all s ∈S to which m is comparable. Zorn’s
lemma can be stated in terms of minimal elements: if every totally ordered subset of a
partially ordered set S has a lower bound in S then S has a minimal element.
There
really is no need to use this formulation in practice, since by reversing the meaning of the
partial ordering (that is, using the reverse ordering) lower bounds become upper bounds
and minimal elements become maximal elements. Analogous to greatest elements are least
elements: m ∈S is a least element if m ≤s for all s ∈S, so m is both minimal and
comparable to all elements of S. In Z+ ordered in the standard way, each nonempty subset
has a least element but not necessarily a greatest element.
Zorn’s lemma is not intuitive, but it is logically equivalent to more intuitively plausible
statements in set theory like the Axiom of Choice, which says every Cartesian product
of nonempty sets is nonempty: if Xi (i ∈I) are nonempty sets then Q
i∈I Xi ̸= ∅. In
the set theory appendix to [21], Zorn’s lemma is derived from the Axiom of Choice. The
equivalence between Zorn’s lemma and the Axiom of Choice is proved in an appendix to
[25]. The reason for calling Zorn’s lemma a lemma rather than an axiom is purely historical.
Zorn’s lemma is also equivalent to the Well-Ordering theorem, which says every nonempty
set has a well-ordering: that is a total ordering on the set such that every nonempty subset
has a least element. Zorn’s lemma was introduced by Max Zorn in 1935 [32] to shorten proofs
in algebra that previously had used the Axiom of Choice or the Well-Ordering theorem.
We will discuss uses of Zorn’s lemma mostly in algebra, but it shows up in many other
areas. For instance, the most important result in functional analysis is the Hahn-Banach
theorem, whose proof uses Zorn’s lemma.
Another result from functional analysis, the
Krein-Milman theorem, is proved using Zorn’s lemma. (The Krein-Milman theorem is an
example where Zorn’s lemma proves the existence of something that is more naturally a
minimal element rather than a maximal element.) In topology, the most important theorem
about compact spaces is Tychonoﬀ’s theorem, and its proof uses Zorn’s lemma.
When dealing with objects that have a built-in ﬁniteness condition (such as ﬁnite-
dimensional vector spaces or ﬁnite products of spaces X1 × · · · × Xn), Zorn’s lemma can be
avoided by using ordinary induction in a suitable way (e.g., inducting on the dimension of
a vector space). The essential uses of Zorn’s lemma are for truly inﬁnite objects, where one
has to make inﬁnitely many choices at once in a rather extreme way. Tim Gowers2 gave a
nice description of when you can anticipate a proof will use Zorn’s lemma:
Typically, one is trying to build a structure of some kind [. . .]. The natural
way to do it appears to be to build the structure up in stages, but there are
too many stages for this to work straightforwardly. However, once one has
1The hypotheses refer to all totally ordered subsets of S, and a totally ordered subset might be uncount-
able. Therefore it is a bad idea to write about “totally ordered sequences,” since the label “sequence” is
often understood to refer to a countably indexed set. Just use the label “totally ordered subset.”
2See the end of https://gowers.wordpress.com/2008/08/12/how-to-use-zorns-lemma/.

<!-- page 5 -->
ZORN’S LEMMA AND SOME APPLICATIONS
5
an idea of what a stage is and what the building-up process is, one can wheel
out Zorn’s lemma to ﬁnish the job. The partially ordered set will consist
of all objects that might conceivably be stages in the construction, and one
of these objects will be smaller than another if it might conceivably come
before the other in the building-up process. If the resulting partial order
satisﬁes the chain condition and if a maximal element must be a structure
of the kind one is trying to build, then the proof is complete.
You will see this idea in action in the proofs coming up.
2. Applications to group theory
There are two common reasons that Zorn’s lemma is used: to ﬁnd a subset that is as
big as possible subject to some conditions or to show a function deﬁned on a subset can be
extended to the whole set while preserving certain technical conditions. We will illustrate
both ideas in this section within the setting of group theory.
A subgroup M of a nontrivial group G is called a maximal subgroup if M is a proper
subgroup of G and there is no subgroup strictly contained between M and G. This means
M is maximal for containment among the proper subgroups of G. (You may think a better
term would be “maximal proper subgroup” instead of “maximal subgroup,” but the term
“maximal subgroup” is standard.)
Example 2.1. Let’s show the maximal subgroups of Z are the subgroups pZ for prime p.
A proper subgroup of Z is mZ where m ̸= ±1, and mZ ⊂pZ where p is a prime factor of
m. Therefore a maximal subgroup of Z must be pZ for a prime p. Conversely, pZ for each
prime p is a maximal subgroup of Z since if aZ is a subgroup of Z such that pZ ⊂aZ ⊂Z
then a | p, so a = ±1 or ±p. Thus aZ equals Z or pZ.
Example 2.2. The additive group Q has no maximal subgroups. For every proper subgroup
H of Q, we’ll show there is a subgroup strictly between H and Q. First, [Q : H] = ∞:
if the index were ﬁnite, say n > 1, then the quotient group Q/H would have order n, so
nr ≡0 mod H for all r ∈Q. That means nQ ⊂H. Since nQ = Q, we get Q ⊂H and
thus H = Q, which contradicts [Q : H] > 1. Pick r ∈Q −H, so r ̸= 0. The subgroup
H + Zr of Q strictly contains H and we’ll show [H + Z⟨r⟩: H] is ﬁnite. Representatives
for the quotient group (H + Z⟨r⟩)/H can be chosen from integral multiples of r, and r in
(H + Z⟨r⟩)/H has ﬁnite order: write r = a/b for a, b ∈Z −{0} and pick a nonzero h = c/d
in H, where c, d ∈Z −{0}. Then bcr = ac = adh ∈H, so r in (H + Z⟨r⟩)/H has order at
most |bc|. Thus (H + Zr)/H is ﬁnite while Q/H is inﬁnite, so H ⫋H + Z⟨r⟩⫋Q.
The following theorem gives a condition under which a group has maximal subgroups.
Theorem 2.3. Let G be a nontrivial ﬁnitely generated group. Every proper subgroup of G
is contained in a maximal subgroup of G.
This theorem does not apply to Q since it is not ﬁnitely generated.
Proof. Let g1, . . . , gn be a ﬁnite (nonempty) generating set for G, so G = ⟨g1, . . . , gn⟩. For
a proper subgroup eG of G and 0 ≤j ≤n, set Gj = ⟨eG, g1, . . . , gj⟩, so
eG = G0 ⊂G1 ⊂· · · ⊂Gn = G.
Let ℓbe the largest integer from 0 to n−1 such that Gℓ̸= G. Then Gℓ+1 = ⟨Gℓ, gℓ+1⟩= G,
so gℓ+1 ̸∈Gℓ.

<!-- page 6 -->
6
KEITH CONRAD
Deﬁne a partially ordered set. Let
S = {H : H is a subgroup of G, Gℓ⊂H, gℓ+1 ̸∈H},
where subgroups in S are ordered by inclusion. The set S is nonempty since Gℓ∈S. We’ll
apply Zorn’s lemma to S to get a maximal subgroup of G that contains eG.
Totally ordered subsets of S have an upper bound in S. Let {Hi}i∈I be a totally ordered
subset of S. We will show the union H = S
i∈I Hi is an upper bound in S on every Hi.
Even though a union of subgroups need not be a subgroup in general (think about 2Z ∪3Z
inside Z), the fact that the subgroups Hi are totally ordered will make H a subgroup.
If h and h′ are in H then h ∈Hi and h′ ∈Hi′ for some subgroups Hi and Hi′. Since we are
working with a totally ordered set of subgroups in S, Hi ⊂Hi′ or Hi′ ⊂Hi. Without loss of
generality, Hi ⊂Hi′. Therefore h and h′ are in Hi′, so hh′ ∈Hi′ ⊂H. Also h−1 ∈Hi ⊂H.
Therefore H is a subgroup of G. We have H ∈S since (i) gℓ+1 ̸∈H and (ii) Gℓ⊂H. To
prove (i), suppose gℓ+1 ∈H. Then gℓ+1 ∈Hi for some i, but that contradicts the fact that
Hi belongs to S. So gℓ+1 ̸∈H. To prove (ii), since Gℓis contained in each Hi (or even just
one of them), Gℓis contained in their union, so Gℓ⊂H. Thus H ∈S.
Since H contains each Hi and H ∈S, H is an upper bound in S on {Hi}i∈I.
Use Zorn’s lemma. By Zorn’s lemma, S has a maximal element M: M is a subgroup of
G with Gℓ⊂M and gℓ+1 ̸∈M, and M is maximal for containment among all subgroups of
G with those two properties.
M is a maximal subgroup of G and contains eG. Since eG ⊂Gℓ⊂M, M contains eG. For
M to be a maximal subgroup of G means M is not contained in another proper subgroup
of G, with no further conditions: if M ⊂H ⊂G for a subgroup H ̸= M then H = G.
From Gℓ⊂M ⊂H, we have Gℓ⊂H. To show H = G, suppose gℓ+1 ̸∈H. Then H ∈S
(see the deﬁnition of S), and this contradicts the maximality of M in S. Therefore gℓ+1 ∈H,
so ⟨M, gℓ+1⟩⊂H. Since M contains Gℓ, ⟨M, gℓ+1⟩contains ⟨Gℓ, gℓ+1⟩= Gℓ+1 = G, so
G ⊂H. Thus H = G.
□
The proof of Theorem 2.3 exhibits a standard disconnect between upper bounds on totally
ordered subsets and maximal elements in the whole set. Consider proper subgroups of Z
under inclusion.
The maximal subgroups are pZ for prime numbers p.
The subgroups
{6Z, 12Z, 24Z} are totally ordered under inclusion, and in the proof of Theorem 2.3 the
upper bound created on this subset is the union 6Z ∪12Z ∪24Z = 6Z. (A ﬁnite totally
ordered subset of a partially ordered set always has one of its members as an upper bound
on the subset, by Lemma 1.9.) This upper bound is not a maximal subgroup of Z. So
the task of checking the hypotheses of Zorn’s lemma are satisﬁed is a completely separate
matter from applying Zorn’s lemma: an upper bound on a totally ordered subset does not
have to be a maximal element of the whole set. Remember that!
Our next application of Zorn’s lemma is to extending the domain of a homomorphism.
An abelian group D is called divisible if the function x 7→nx is surjective for every n ≥1.
(We write the group operation additively.) That is, for each d ∈D and n ≥1 there is an
x such that d = nx, so we can “divide” d by n (but x need not be unique). For example,
R/Z and Q are divisible groups while Z is not. Among multiplicative groups, C× and its
subgroup S1 are divisible. (The function x 7→e2πix sets up an isomorphism R/Z ∼= S1.)
Theorem 2.4. For every divisible group D, abelian group A, and subgroup B ⊂A, each
homomorphism f : B →D can be extended to a homomorphism ef : A →D.

<!-- page 7 -->
ZORN’S LEMMA AND SOME APPLICATIONS
7
Proof. Pick a ∈A with a ̸∈B. Then the subgroup ⟨B, a⟩= B + Za spanned by B and a
contains B. As a warm-up we will show how to extend f to this larger subgroup of A. (See
the diagram below.) Then we will bring in Zorn’s lemma.
A
⟨B, a⟩
"
B
̸=
f
/ D.
Consider how ⟨a⟩can meet B. The set {k ∈Z : ka ∈B} is a subgroup of Z, so it is 0 or
nZ for some n ≥1.
Case 1. {k ∈Z : ka ∈B} = 0. Then each element of ⟨B, a⟩is b + ka for unique b ∈B
and k ∈Z (why?). Deﬁne f′ : ⟨B, a⟩→D by f′(b + ka) = f(b), so f′|B = f. The mapping
f′ is a homomorphism since
f′((b1 + k1a) + (b2 + k2a)) = f′((b1 + b2) + (k1 + k2)a)
= f(b1) + f(b2)
= f′(b1 + k1a) + f′(b2 + k2a).
Case 2. {k ∈Z : ka ∈B} = nZ for some n ≥1. Then a positive multiple of a lies in B,
and na is that multiple with n minimal. The function f makes sense at na, but not at a.
If we can extend f to a homomorphism f′ : ⟨B, a⟩→D then f′(a) must satisfy the relation
nf′(a) = f′(na) = f(na). Here f(na) is already deﬁned while f′(a) is not. To deﬁne f′(a)
we need to ﬁnd an x ∈D such that nx = f(na) and then we set f′(a) to be that x. Because
D is divisible, there is an x ∈D such that nx = f′(a). Deﬁne f′(a) = x, and more generally
deﬁne
f′(b + ka) = f(b) + kx.
Is this well-deﬁned? Suppose
(2.1)
b + ka = b′ + k′a.
Then (k −k′)a = b′ −b ∈B, so k −k′ ∈nZ by the deﬁnition of n. Write k = k′ + nℓfor
some ℓ∈Z, so
f(b) + kx = f(b) + (k′ + nℓ)x
= f(b) + k′x + ℓ(nx)
= f(b) + k′x + ℓf(na)
= f(b + ℓna) + k′x.
Since b + ℓna = b + (k −k′)a = b + ka −k′a, and that’s b′ by (2.1). Thus
f(b) + kx = f(b′) + k′x,
so f′ : ⟨B, a⟩→D is well-deﬁned. It is left to the reader to show it is a homomorphism.
Now we show Zorn’s lemma can be applied.

<!-- page 8 -->
8
KEITH CONRAD
Deﬁne a partially ordered set. Let S be the set of pairs (C, g) where C is a subgroup
between B and A and g: C →D is a homomorphism that extends f (that is, g|B = f).
The picture is as follows.
A
C
g
 
B
f
/ D.
The set S is nonempty since (B, f) ∈S. Partially order S by declaring (C, g) ≤(C′, g′)
if C ⊂C′ and g′|C = g. That is, g′ extends g to the larger intermediate subgroup C′.
A
C′
g′

C
g
!
B
f
/ D.
Totally ordered subsets of S have an upper bound in S. If {(Ci, gi)}i∈I is a totally or-
dered subset of S, then it has an upper bound in S: use C = S
i∈I Ci as the subgroup (it
really is a subgroup, using an argument similar to S
i∈I Hi being a subgroup in the proof
of Theorem 2.3) and let g: C →D by g(x) = gi(x) if x ∈Ci. Is this well-deﬁned? Well,
supposing x is in Ci and Cj, we need to know gi(x) = gj(x). Either (Ci, gi) ≤(Cj, gj) or
(Cj, gj) ≤(Ci, gi) since the (Ci, gi)’s are totally ordered in S. If (Ci, gi) ≤(Cj, gj) then
Ci ⊂Cj and gj|Ci = gi, so gj(x) = gi(x). That gi(x) = gj(x) if (Cj, gj) ≤(Ci, gi) is proved
in the same way. Because each pair of elements in C lies in a common Ci by Lemma 1.9, g
is a homomorphism because each gi is a homomorphism. Since gi|B = f for all i, g|B = f.
Thus (C, g) ∈S and (C, g) is an upper bound on {(Ci, gi)}i∈I.
Use Zorn’s lemma. The hypotheses of Zorn’s lemma on S have been checked, so S has
a maximal element (M, h).
That is, M is a group between B and A, h: M →D is a
homomorphism and there is no extension of h to a homomorphism out of a larger subgroup
of A than M.
M = A, so h is deﬁned on all of A. We will show this by contradiction. If M ̸= A then
there is some a ∈A with a ̸∈M. By the argument used at the start of this proof, with B and

<!-- page 9 -->
ZORN’S LEMMA AND SOME APPLICATIONS
9
f there replaced by M and h here, h can be extended to a homomorphism h′ : ⟨M, a⟩→D.
A
⟨M, a⟩
h′
#
M
̸=
h
/ D.
Thus (M, h) ≤(⟨M, a⟩, h′) and (M, h) ̸= (⟨M, a⟩, h′), which contradicts the maximality of
(M, h). Hence M = A.
□
Corollary 2.5. Let D be a divisible group. If D is a subgroup of an abelian group A then D
is a direct factor in A: there is a direct product decomposition A = D × H (internal direct
product) for some subgroup H of A.
Proof. The identity function f : D →D is a homomorphism and D is a subgroup of A, so
f can be extended to a homomorphism ef : A →D by Zorn’s lemma, thanks to Theorem
2.4. We will show A = D × ker( ef).
For a ∈A, set d = ef(a). Since ef(d) = f(d) = d, ef(a) = ef(d). Thus h := a −d is in
ker( ef) and a = d + h. We have shown A = D + ker( ef). This decomposition is direct since
D ∩ker( ef) = {0}: if d ∈D ∩ker( ef) then 0 = ef(d) = f(d) = d.
□
Example 2.6. Since S1 is a divisible subgroup of C×, C× = S1 × H for a subgroup H of
C×. Indeed, we can use H = R>0: C× = S1 × R>0 by writing nonzero z in C as eiθr for
r = |z| and eiθ = z/|z| ∈S1. This is a situation where we don’t really need Corollary 2.5
to get a direct product decomposition of a group with the subgroup S1 as one factor.
Example 2.7. Let µ∞be the group of all roots of unity in C×. (A standard notation for
the nth roots of unity in C× is µn.) Since µ∞is a divisible subgroup of S1, S1 = µ∞×H for
a subgroup H of S1. In contrast to the previous example, the direct product decomposition
here is completely abstract and we only know it exists from the proof of Corollary 2.5, which
uses Zorn’s lemma. Speciﬁcally, in that proof there is no known concrete way to write down
a group homomorphism S1 →µ∞that is the identity on µ∞.
Example 2.8. Since Q is a divisible subgroup of R, R = Q × H for a subgroup H of R.
(This is an additive decomposition of R, not a multiplicative one, so writing R = Q ⊕H
might be better.) No such decomposition of R is known where H can be described explicitly.
Remark 2.9. The application of Zorn’s lemma in Theorem 2.4 generalizes from abelian
groups (Z-modules) to modules over a commutative ring R, and is called Baer’s charac-
terization of injective R-modules. (An R-module is injective when it is a direct summand
of each module it can be embedded in.) See [10, p. 396] or [25, p. 483]. Divisible abelian
groups are examples of injective Z-modules.
Let’s use Zorn’s lemma to do something crazy: show there is a “maximal” group. On the
set of all groups, deﬁne the partial ordering by inclusion. This is a partial ordering. If {Gi}
is a totally ordered set of groups, let G be the union of the Gi’s. Every pair of elements in
G is in a common Gi, so it is easy to deﬁne the group law in G (use the group law in Gi),
check it is well-deﬁned (independent of the Gi containing the two elements), and G contains

<!-- page 10 -->
10
KEITH CONRAD
all Gi’s. So now it seems, by Zorn’s lemma, that we should have a maximal group: a group
that is not contained in some larger group. This is absurd, since for each group G we can
create G × Z and literally (if you wish) replace the elements of G × {0} with the elements
of G to make G a genuine subset of G × Z. Then G is properly contained in another group
and we have contradicted maximality. What is the error?
The problem here is right at the start when we deﬁned our partially ordered set as the
“set of all groups.” This is the kind of set-theoretic looseness that leads to paradoxes (set
of all sets, etc.). In fact, the group-theoretic aspect of the construction was irrelevant for
the contradiction: if we just worked with sets and containment, the same argument goes
through to show there is a set contained in no other sets, which is false and contains the
same error as above: there is no “set of all sets” that one can partially order to make Zorn’s
lemma apply. Looking back now, perhaps with some suspicion, at the previous two proofs
where we created an upper bound on a totally ordered subset of a partially ordered set
relative to some kind of inclusion relation, the objects that we formed the union of were
subsets of a larger ﬁxed set (subgroups of a group). In that context the union really makes
sense. It doesn’t make sense to take arbitrary unions of arbitrary sets that a priori don’t
live in some common set. As an extreme case, we can’t take the union of “all sets” to ﬁnd
one set containing all others.
Here are a few exercises about Zorn’s lemma using ideas from this section.
Exercise. At the start of this section we saw Q has no maximal proper subgroup. By
imposing a constraint on the kind of subgroup, we can obtain maximal examples.
a) Use Zorn’s lemma to show the set of subgroups of Q that don’t contain 1 has maximal
elements: there is a subgroup M of Q such that (i) 1 ̸∈M and (ii) if M ⊂H ⊂Q and
1 ̸∈H then H = M. (Start by showing the set of such subgroups is not empty!)
b) Let M be a subgroup of Q maximal for the property of not containing 1.
Show
M ∩Z ̸= {0} (hint: if M ∩Z = {0} then consider M + nZ where n ≥2) and then show
M ∩Z = qZ for a prime q.
c) Show the numerator of each fraction in M is divisible by q from (b), so M ⊂Hq :=
{a/b : a, b ∈Z, q | a, q ∤b}. Elements of Hq are the fractions that “make sense” mod q.
d) For every prime p, deﬁne Hp := {a/b : a, b ∈Z, p | a, p ∤b}. Prove Hp is a subgroup
of Q, Hp ∩Z = pZ, and Hp is maximal among subgroups of Q not containing 1. Therefore
by (c), the maximal subgroups in (a) are the subgroups Hp.
e) Give an example of a proper subgroup of Q containing Hp. (It must contain 1.)
Exercise. Let A be an abelian group, written additively, such that all elements have
order dividing a ﬁxed positive integer m: ma = {0} for all a ∈A.
An example is an
arbitrary direct product A = Q
j∈J Z/(m), but examples can be far more complicated.
a) Suppose B is a subgroup of A and there is a homomorphism f : B →Z/(m). For each
a ∈A −B, show f can be extended to a homomorphism ⟨B, a⟩→Z/(m).
b) Use Zorn’s lemma to show for each subgroup B of A and homomorphism f : B →
Z/(m) that f can be extended to a homomorphism A →Z/(m).
c) If there is an a ∈A with order m, then use (b) to show A = ⟨a⟩×A′ for some subgroup
A′ of A.
Exercise. Let K and F be ﬁelds. There need not be a homomorphism K →F (e.g.,
K = Q and F = F2). But assume some subring of K admits a ring homomorphism to F
(e.g., if K has characteristic 0 then Z ⊂K and there is certainly a ring homomorphism

<!-- page 11 -->
ZORN’S LEMMA AND SOME APPLICATIONS
11
Z →F, while if K and F both have characteristic p > 0 then Z/(p) is a subﬁeld of K and
F so there is an inclusion homomorphism Z/(p) ,→F).
a) Let S be the set of pairs (A, f) where A is a subring of K and f : A →F is a ring
homomorphism, so S ̸= ∅by hypothesis. Partially order S by (A, f) ≤(B, g) if A ⊂B and
g|A = f. Show with Zorn’s lemma that S contains a maximal pair, which amounts to a
subring A ⊂K that admits a ring homomorphism f : A →F that can’t be extended to a
ring homomorphism out of a larger subring of K.
b) When K = Q and F = Z/(2), show the ring of fractions {m/n : m ∈Z, n ∈
Z −{0}, n is odd} admits a homomorphism to Z/(2) and is the ring part of a maximal pair
(A, f) in S. (Note Q itself is not part of a maximal pair since there is no ring homomorphism
from Q to Z/(2).) What is the kernel of this homomorphism?
c) If (A, f) is a maximal pair in S, show every element of A not in ker f is a unit in A, and
therefore ker f is the only maximal ideal in A. (A ring with only one maximal ideal is called
a local ring. Trying to ﬁnd a maximal subring of one ﬁeld that admits a homomorphism to
another ﬁeld gives rise, using Zorn’s lemma, to examples of local rings.)
3. Applications to ideals
The ideals in a commutative ring can be partially ordered by inclusion. The whole ring,
which is the unit ideal (1), is obviously maximal with respect to this ordering. But this is
boring and useless. Proper ideals that are maximal for inclusion among the proper ideals
are called the maximal ideals in the ring. (That is, a maximal ideal is understood to mean
a maximal proper ideal.) Let’s prove they always exist.
Theorem 3.1 (Krull). Every nonzero commutative ring contains a maximal ideal.
Proof. Let S be the set of proper ideals in a commutative ring R ̸= 0. Since the zero ideal
(0) is a proper ideal, S ̸= ∅. We partially order S by inclusion.
Let {Iα}α∈A be a totally ordered set of proper ideals in R. To write down an upper
bound for these ideals in S, it is natural to try their union I = S
α∈A Iα. As with subgroups
in the proof of Theorem 2.3, a union of ideals is not usually an ideal (try 2Z ∪3Z), but
since we are dealing with a union of a totally ordered set of ideals, the union turns out to
be an ideal. Make sure you can explain why.
If x and y are in I then x ∈Iα and y ∈Iβ for two of the ideals Iα and Iβ. Since this
set of ideals is totally ordered, Iα ⊂Iβ or Iβ ⊂Iα. Without loss of generality, Iα ⊂Iβ.
Therefore x and y are in Iβ, so x ± y ∈Iβ ⊂I. Hence I is an additive subgroup of R. The
reader can check rx ∈I for r ∈R and x ∈I, so I is an ideal in R.
Because I contains every Iα, I is an upper bound on the totally ordered subset {Iα}α∈A
provided it is actually in S: is I a proper ideal? Well, if I is not a proper ideal then 1 ∈I.
Since I is the union of the Iα’s, we must have 1 ∈Iα for some α, but then Iα is not a proper
ideal. That is a contradiction, so 1 ̸∈I. Thus I ∈S and we have shown every totally
ordered subset of S has an upper bound in S.
By Zorn’s lemma S contains a maximal element.
This maximal element is a proper
ideal of R that is maximal with respect to inclusion among all proper ideals (not properly
contained in another proper ideal of R). That means it is a maximal ideal of R.
□
Corollary 3.2. Every proper ideal in a nonzero commutative ring is contained in a maximal
ideal.

<!-- page 12 -->
12
KEITH CONRAD
Proof. Let R be the ring and I be a proper ideal in R. The quotient ring R/I is nonzero,
so it contains a maximal ideal by Theorem 3.1. The inverse image of this ideal under the
natural reduction map R →R/I is a maximal ideal of R that contains I.
□
It is crucial in the proof of Theorem 3.1 to have the multiplicative identity 1 available,
which lies in no proper ideal. For instance, the analogue of Theorem 3.1 for groups can
fail: the additive group Q contains no maximal proper subgroups, as we saw at the start of
Section 2. The importance of Theorem 3.1 in the foundations of commutative algebra is one
reason that rings should always have a multiplicative identity, at least if you are interested
in areas of math that depend on commutative algebra, e.g., number theory and algebraic
geometry. In this note, all commutative rings have 1.
The following important theorem concerns nilpotent elements. In a commutative ring,
an element r is called nilpotent if rn = 0 for some n ≥1.
Theorem 3.3 (Krull). The intersection of all prime ideals in a nonzero commutative ring
is the set of nilpotent elements in the ring.
This is striking: if we know an element in a nonzero commutative ring lies in every prime
ideal, then a power of it is 0. In the ring Z the result is obvious, since the prime ideals are
(0) and (p) for prime numbers p, and the intersection is obviously {0}, which is the only
nilpotent integer. A somewhat more interesting example is the ring Z/(12). Its prime ideals
are (2)/(12) and (3)/(12) (not (0)/(12)!), whose intersection is (6)/(12) = {0, 6 mod 12},
which is also (by inspection) all nilpotent elements of Z/(12).
Proof. Let R be a nonzero commutative ring. If r ∈R is nilpotent then rn = 0 for some
n ≥1. For each prime ideal P of R, rn ∈P, so r ∈P since P is a prime ideal. Thus every
nilpotent element of R is in the intersection of all prime ideals of R.
Now we want to show the intersection of all prime ideals of R consists only of nilpotent
elements: if r ∈P for all prime ideals P then rn = 0 for some n ≥1. How could this
be shown?
We will not try to prove rn = 0 for some n directly, but rather prove the
contrapositive statement: if r ∈R is not nilpotent then some prime ideal of R does not
contain r. So an element of R lying in all prime ideals of R must be nilpotent.
Since r is not nilpotent, rn ̸= 0 for every n ≥1. Consider the set S of all ideals I in R
that don’t contain a positive power of r:
I ∈S ⇐⇒{rn : n ≥1} ∩I = ∅.
The zero ideal (0) doesn’t meet {rn : n ≥1}, because r is not nilpotent, so S is nonempty.
We partially order S by inclusion. After checking the conditions for Zorn’s lemma can be
applied to S, we will show that a maximal element of S is a prime ideal.3 Since none of the
ideals in S contain r, we will have found a prime ideal of R not containing r.
Let {Iα}α∈A be a totally ordered set of ideals in S. Its union I is an ideal (same proof as
that in Theorem 3.1 – be sure you can write it up!). Since no Iα contains a positive power
of r, their union I does not contain a positive power of r either. Thus I ∈S, and since
Iα ⊂I for all α, I is an upper bound in S for the set of ideals Iα’s. Thus every totally
ordered subset of S contains an upper bound in S.
By Zorn’s lemma, S has a maximal element. Call it P, so P is an ideal in R that does not
contain a positive power of r and is maximal for this property (with respect to inclusion).
3Notice we are not deﬁning S to be a set of prime ideals, but only a set of ideals with a disjointness
property. That a maximal element of S is a prime ideal in R is going to be proved using maximality.

<!-- page 13 -->
ZORN’S LEMMA AND SOME APPLICATIONS
13
We write a maximal element of S as P because we’re going to show P is a prime ideal. The
ideal P is proper since r ̸∈P. Suppose x and y are in R and xy ∈P. To prove x ∈P
or y ∈P, assume otherwise: x ̸∈P and y ̸∈P. Then the ideals (x) + P and (y) + P are
both strictly larger than P,4 so they can’t lie in S. That means we have rm ∈(x) + P and
rn ∈(y) + P for some positive integers m and n:
rm = ax + p1,
rn = by + p2
where p1 and p2 are in P and a and b are in R. Now multiply:
rm+n = abxy + axp2 + byp1 + p1p2.
Since P is an ideal and p1, p2, xy ∈P, the right side is in P. Then rm+n ∈P, which
contradicts P being disjoint from {rk : k ≥1} (because P ∈S)5. Hence x ∈P or y ∈P, so
P is prime. By construction P contains no positive power of r, so in particular r ̸∈P.
□
Remark 3.4. Although the ideal P in the proof above is maximal with respect to inclusion
among the ideals in R that are disjoint from {r, r2, r3, . . . }, P need not be a maximal ideal
of R: a maximal ideal in a ring is maximal with respect to inclusion among all proper ideals
of the ring, while the proof above used Zorn’s lemma on a set of ideals in R that is usually
not all proper ideals. (For example, if R is the set of fractions with odd denominator and
r = 2 then S = {(0)}, so P = (0), which is not a maximal ideal of R.) Quite generally, if
S is a partially ordered set and S′ is a subset of S, a maximal element of S′ need not be a
maximal element of S. Make sure you understand that!
The intersection of all prime ideals is called the nilradical (because it is the nilpotent
elements) and the intersection of all maximal ideals is called the Jacobson radical (because
Nathan Jacobson studied it). Since every prime ideal is in a maximal ideal, the intersection
of the maximal ideals contains the intersection of the prime ideals and the containment can
be strict, although examples of such rings are not typically seen in a ﬁrst abstract algebra
course. If every prime ideal is the intersection of the maximal ideals containing it then the
ring is called a Jacobson ring and Theorem 3.3 with “prime ideal” replaced by “maximal
ideal” is true for Jacobson rings. An example of a non-Jacobson ring is an integral domain
R that is not a ﬁeld and has one maximal ideal M: the nilradical of R is {0} since R is an
integral domain and the Jacobson radical of R is M, which is not {0} since R is not a ﬁeld.
Such rings show up all over the place in commutative algebra and algebraic geometry, and
include the ring of formal power series F[[x]] where F is a ﬁeld and the ring of fractions a/b
where a, b ∈Z and b is odd (“localization of Z at the prime 2”).
Exercise. Use Zorn’s lemma to prove that if D is a nonempty multiplicatively closed
subset of a nonzero commutative ring R such that 0 ̸∈D, then there is an ideal in R that
is maximal with respect to being disjoint from D and such an ideal is a prime ideal. This
result is due to Krull [19, Lemma, p. 732], and it implies Theorem 3.1 when D = {1} and
it implies Theorem 3.3 when D = {1, r, r2, r3, . . .} for a non-nilpotent r ∈R.
4Here it is important that R contains 1, so x ∈(x) = xR.
5If we had deﬁned S to be the ideals in R that don’t include r, rather than no positive power of r, then
at this point we’d be stuck: we’d have r = ax + p1 and r = bx + p2, so then multiplying gives r2 ∈P, but
that would not be a contradiction since we didn’t require ideals of S to avoid containing r2. Seeing this
diﬃculty is a motivation for the deﬁnition of S in the proof.

<!-- page 14 -->
14
KEITH CONRAD
Corollary 3.5. For each proper ideal I in a nonzero commutative ring R,
\
P⊃I
P = {x ∈R : xn ∈I for some n ≥1},
where the intersection runs over the prime ideals of R that contain I.
Proof. If xn ∈I for some n ≥1, then for each prime ideal P ⊃I we have xn ∈P, so x ∈P.
Conversely, suppose x is in every prime ideal of R containing I. (There are prime ideals
containing I since there is a maximal ideal of R containing I.) The natural map R →R/I
identiﬁes the prime ideals in R that contain I with the prime ideals of R/I, so x is in every
prime ideal of R/I. Therefore by Theorem 3.3, x is nilpotent in R/I. This means xn = 0
for some n ≥1, so xn ∈I.
□
We used Zorn’s lemma to prove Theorem 3.3 since our point here is to see enough
applications of Zorn’s lemma that the basic principle behind its use becomes transparent,
but it turns out that Theorem 3.3 can also be proved using Corollary 3.2 about proper
ideals lying in a maximal ideal. The trick is to use a maximal ideal not in R itself but in
the polynomial ring R[X]. Here is that alternate proof of Theorem 3.3.
Proof. We will only address one direction: a non-nilpotent element r in a ring R lies outside
some prime ideal. (The other direction is easy; see the ﬁrst paragraph in the ﬁrst proof of
Theorem 3.3.) We will create such a prime ideal as the kernel of a homomorphism out of
R and r won’t be in the kernel.
In R[X], rX −1 is not a unit. Indeed, if we did have (rX −1)(cnXn +· · ·+c1X +c0) = 1
then equating coeﬃcients of like powers of X on both sides shows
−c0 = 1,
c0r −c1 = 0,
c1r −c2 = 0, . . . ,
cn−1r −cn = 0,
rcn = 0.
Thus c0 = −1, ci = ci−1r for 1 ≤i ≤n, and rcn = 0. So ci = −ri for 1 ≤i ≤n. Thus
0 = rcn = −rn+1, but r is not nilpotent. So rX−1 is not a unit in R[X]. (If r were nilpotent,
say rn = 0, then rX −1 is a unit in R[X] with inverse −(1+rX +r2X2 +· · ·+rn−1Xn−1).)
The ideal (rX −1) in R[X] is proper, since rX −1 is not a unit, so this ideal lies inside
a maximal ideal M of R[X] by Corollary 3.2. Now consider the composite homomorphism
R →R[X] →R[X]/M, where the ﬁrst map is inclusion and the second is reduction. Since
the target is a ﬁeld, the kernel in R is a prime ideal (the quotient of R by the kernel embeds
into the ﬁeld R[X]/M and thus must be an integral domain, as subrings of ﬁelds are integral
domains). Call the kernel P. Since rX ≡1 mod M, r is not in the kernel. Thus P is a
prime ideal in R not containing r. We’re done.
□
This proof can be streamlined if you know about localization of commutative rings. (If
you don’t, skip this paragraph.) For a commutative ring R and multiplicative subset S of
R, the localization RS is 0 if and only if 0 ∈S. Taking S = {1, r, r2, . . .} where r is not
nilpotent, RS is usually written as R[1/r]. (It is isomorphic to the ring R[X]/(rX −1) used
in the above proof.) Since R[1/r] ̸= {0}, R[1/r] contains a maximal ideal M and the image
of r in R[1/r] is a unit and thus is not in M. The kernel of the composite homomorphism
R →R[1/r] →R[1/r]/M is a prime ideal for the same reason given in the proof above.
We now leave maximal ideals and nilpotent elements, turning our attention to an inter-
esting theorem of Cohen [8, Theorem 2] about ﬁnitely generated ideals.
Theorem 3.6 (Cohen). If every prime ideal in a commutative ring is ﬁnitely generated
then every ideal in the ring is ﬁnitely generated.

<!-- page 15 -->
ZORN’S LEMMA AND SOME APPLICATIONS
15
Proof. We will prove the contrapositive: if there is some ideal in the ring R that is not
ﬁnitely generated then there is a prime ideal in R that is not ﬁnitely generated. We will
ﬁnd this prime ideal as an ideal maximal with respect to inclusion among the non-ﬁnitely
generated ideals. (Here again we should stress, as in Remark 3.4, that such prime ideals
need not be actual maximal ideals in R. They are only created as being maximal among
non-ﬁnitely generated ideals.)
Let S be the collection of all non-ﬁnitely generated ideals in R, so S ̸= ∅by assumption.
Partially order S by inclusion. For a totally ordered subset of ideals {Iα}α∈A in S, its union
I is an ideal containing each Iα. (That I is an ideal follows by the same argument as in the
proof of Theorem 3.1.) To know I is an upper bound on the Iα’s in S we have to show I is
not ﬁnitely generated. Well, if I were ﬁnitely generated, say I = (r1, . . . , rk), then each of
the generators is in some Iα and by total ordering on the ideals, these hypothetical ﬁnitely
many generators of I are all in a common Iα (Lemma 1.9). But then I lies inside that Iα,
so I equals that Iα, which shows that Iα is ﬁnitely generated. This is a contradiction, so I
is not ﬁnitely generated.
Now we can apply Zorn’s lemma: there exists a non-ﬁnitely generated ideal in R that is
maximal with respect to inclusion among the non-ﬁnitely generated ideals in R. Call such
an ideal P. We are going to prove by contradiction that P is a prime ideal of R. It is
certainly a proper ideal, since R = (1) is a ﬁnitely generated ideal, so if P is not a prime
ideal then there are x and y not in P such that xy ∈P. Since (x) + P is an ideal properly
containing P, (x) + P ̸∈S. Therefore (x) + P is ﬁnitely generated:
(x) + P = (r1, . . . , rk).
Write ri = cix+pi for i = 1, 2, . . . , k, where ci ∈R and pi ∈P. (We have no right to expect
the pi’s generate P. They only occur in the expressions for the ri’s.) Then every ri is in
the ideal (x, p1, . . . , pk), and conversely each pi is in the ideal P ⊂(x)+P = (r1, . . . , rk), so
(x) + P = (x, p1, . . . , pk).
For each p ∈P, since P ⊂(x) + P we can write
(3.1)
p = cx + a1p1 + · · · + akpk
with c and the ai’s in R. Then cx = p −P aipi ∈P, so c is in J = {r ∈R : rx ∈P}, which
is an ideal in R. Easily P ⊂J and y ∈J. Since y ̸∈P, J strictly contains P. Thus by
maximality of P among all the non-ﬁnitely generated ideals in R, J is ﬁnitely generated.
By (3.1), p ∈xJ + Pk
i=1 Rpi, so P ⊂xJ + Pk
i=1 Rpi. The reverse inclusion is easy (by the
deﬁnition of J), so
P = xJ +
k
X
i=1
Rpi.
Since J is ﬁnitely generated, this shows P is ﬁnitely generated. We have reached a contra-
diction, so P is a prime ideal.
□
Exercise. Use Zorn’s lemma to prove an analogue of Theorem 3.6 for principal ideals:
if every prime ideal in a commutative ring is principal then all ideals in the ring are prin-
cipal. (It is false that if every prime ideal has at most 2 generators then all ideals have at
most 2 generators, e.g., in C[X, Y ] the prime ideals have 1 or 2 generators but the ideal
(X2, XY, Y 2) can’t be generated by 2 elements. It is also false that if every maximal ideal is
principal then all ideals are principal: see https://mathoverflow.net/questions/81011.)

<!-- page 16 -->
16
KEITH CONRAD
We now generalize Theorem 3.6 to modules in place of rings. When M is an R-module
and a is an ideal of R, let aM denote the submodule of M that is spanned by all ﬁnite
products am for a ∈a and m ∈M. That is, aM is the set of all ﬁnite sums Pn
i=1 aimi with
n ≥1, ai ∈a and mi ∈M. Check this is a submodule of M. (We need to use ﬁnite sums
since the set of products am with a ∈a and m ∈M is usually not a submodule since it’s
not additively closed.)
Theorem 3.7 (Jothilingam [16]). Let M be a ﬁnitely generated R-module. If every sub-
module of the form pM with prime p is ﬁnitely generated then every submodule of M is
ﬁnitely generated.
When M = R, this is Theorem 3.6.
However, the proof of Theorem 3.7 has some
additional aspects at the end that don’t occur in Theorem 3.6, so we are proving the two
theorems separately. Our proof is based on an argument of Naghipour [23].
Proof. We will prove the contrapositive: if M has a submodule that is not ﬁnitely generated
then it has a submodule of the form pM with prime p that is not ﬁnitely generated.
Let S be the set of submodules of M that are not ﬁnitely generated, so S ̸= ∅by
assumption. Note M ̸∈S. Partially order S by inclusion. By the same kind of argument
as in the proof of Theorem 3.6, every totally ordered subset of S has an upper bound in S.
(Check the details!) Therefore we can apply Zorn’s lemma: S contains a maximal element.
Call one of them N. That is, N is a submodule of M that is not ﬁnitely generated and
(this is the key point) each submodule of M that properly contains N is ﬁnitely generated.
Note N ̸= M.
Will we show N = pM for some prime ideal p of R? No! There is so little control over
the maximal elements coming from Zorn’s lemma that we can’t expect this. Instead we will
show that
(1) p := AnnR(M/N) = {r ∈R : rM ⊂N} is a prime ideal of R,
(2) pM is not ﬁnitely generated.
To show p is prime, ﬁrst we note p ̸= R since N ⫋M. If p is not prime then there are x
and y in R with xy ∈p but x and y are not in p. From the deﬁnition of p, these conditions
on x and y mean
xyM ⊂N,
xM ̸⊂N,
yM ̸⊂N.
Thus xM + N properly contains N, so xM + N is ﬁnitely generated. Let a ﬁnite spanning
set of xM + N be xmi + ni (i = 1, . . . , k). (warning: n1, . . . , nk do not span N, as N is not
ﬁnitely generated.) Then
xM + N =
k
X
i=1
Rxmi +
k
X
i=1
Rni.
(Just check a spanning set of the module on each side is in the other side.) For all n ∈N ⊂
xM + N,
n = r1xm1 + · · · + rkxmk + r′
1n1 + · · · + r′
knk
= x(r1m1 + · · · + rkmk) + r′
1n1 + · · · + r′
knk
(3.2)
where ri, r′
i ∈R. Thus x(r1m1 + · · · + rkmk) ∈N, so r1m1 + · · · + rkmk lies in
L := {m ∈M : xM ⊂N},

<!-- page 17 -->
ZORN’S LEMMA AND SOME APPLICATIONS
17
which is a submodule of M. Note
N ⊂L,
yM ⊂L,
yM ̸⊂N.
Therefore N is a proper subset of L, so L is ﬁnitely generated. By (3.2),
n ∈xL +
k
X
i=1
Rni,
so
N ⊂xL +
k
X
i=1
Rni.
The reverse inclusion is straightforward (use the deﬁnition of L), so
N = xL +
k
X
i=1
Rni.
The right side is ﬁnitely generated, which is a contradiction since N is not ﬁnitely generated.
Thus p is a prime ideal in R.
(At this point, if we had been taking M = R as in Theorem 3.6, then N would be an
ideal and AnnR(M/N) = AnnR(R/N) would equal N, so N = p would be prime and we
would have ﬁnished proving Theorem 3.6.)
It remains to show pM is not ﬁnitely generated. What we will do is show N = pM + Q
for some ﬁnitely generated R-module Q. Then, since N is not ﬁnitely generated, pM can’t
be ﬁnitely generated either.
Since, by hypothesis, M is ﬁnitely generated, write M = Re1 + · · · + Reℓ. (We are not
assuming the ei’s are linearly independent, just that they form a spanning set.) Then M/N
is spanned over R by the reductions e1, . . . , ek, so
p = AnnR(M/N) =
ℓ\
i=1
AnnR(Rei).
The ideal p is inside each AnnR(Rei), but in fact it must equal one of these: if not then each
AnnR(Rei) contains an element ri outside p, but then the product of those ri’s (over all i) is
an element outside of p (because p is prime) while at the same time the product of the ri’s
kills each ei, so this product is in each annihilator and hence is in p. This is absurd, so p is the
annihilator of some Rei. Without loss of generality, p = AnnR(Re1) = {r ∈R : re1 ⊂N}.
Since p ̸= R, also e1 ̸= 0 in M/N, and thus e1 ̸∈N, so Re1 ̸⊂N. Therefore Re1 + N
properly contains N so it is ﬁnitely generated, say by rje1 + nj (j = 1, . . . , d). For n ∈N ⊂
Re1 + N, write
n =
d
X
j=1
aj(rje1 + nj) =


d
X
j=1
ajrj

e1 +
d
X
j=1
ajnj,
with aj ∈R. The coeﬃcient of e1 scales e1 into N by this equation, so the coeﬃcient of e1
is in p. Thus
N ⊂pe1 +
d
X
j=1
Rnj.

<!-- page 18 -->
18
KEITH CONRAD
The reverse inclusion is easy, so
N = pe1 +
d
X
j=1
Rnj ⊂pM +
d
X
j=1
Rnj ⊂N + N = N.
Thus N = pM +Pd
j=1 Rnj, so N not being ﬁnitely generated forces pM not to be ﬁnitely
generated, which is what we wanted to show.
□
Remark 3.8. In Theorems 3.3, 3.6, and 3.7, and the exercise after Theorem 3.6, an ideal
built with Zorn’s lemma turns out to be a prime ideal. Theorem 3.1 is also such a result,
since maximal ideals in a commutative ring are prime ideals. Lam and Reyes [20] describe
general conditions under which this kind of phenomenon occurs.
4. Applications to bases of vector spaces
We want to use Zorn’s lemma to prove an arbitrary nonzero vector space has a basis.
Let’s ﬁrst make sure we know what the label “basis” means when we are dealing with vector
spaces that may turn out to be inﬁnite-dimensional. For a nonzero vector space V over a
ﬁeld F, a basis of V is a subset B of V that is linearly independent (i.e., no ﬁnite subset of
B has a nontrivial F-linear relation) and spans V (i.e., every element of V is an F-linear
combination of ﬁnitely many elements of B).
Even if a basis is inﬁnite, ﬁniteness assumptions are built into linear independence and
spanning sets: linear independence involves a ﬁnite linear combination equal to 0, and span-
ning sets involve ﬁnitely many vectors at a time. In analysis, inﬁnite linear combinations
occur when a topology has been introduced on the vector space. Such a topological basis is
not covered by the use of the label “basis” here. Our more algebraically-oriented concept
of a basis, always using ﬁnite linear combinations, is called a Hamel basis.
Theorem 4.1 (Hausdorﬀ). Every nonzero vector space contains a basis.
This was proved by Hamel [12] in the special case of R as a vector space over Q in 1905.
The result in full generality is due to Hausdorﬀ[13, p. 295] in 1932.
Proof. The idea is that a basis can be constructed as a maximal linearly independent set,
and this maximal set will be found with Zorn’s lemma.
Let V be a nonzero vector space and let S be the set of linearly independent sets in V .
For instance, a single nonzero v ∈V is a linearly independent set, so {v} ∈S. Thus S ̸= ∅.
For two linearly independent sets L and L′ in V , declare L ≤L′ if L ⊂L′. This is
the partial ordering on S by inclusion. It is easy to see that every subset of a linearly
independent set is also a linearly independent set, so if L ∈S then every subset of L is also
in S.
Assume {Lα}α∈A is a totally ordered subset of S. That is, every Lα is a linearly inde-
pendent set in V and for each Lα and Lβ in our subset we have Lα ⊂Lβ or Lβ ⊂Lα. An
upper bound for the Lα’s in S is the union L = S
α∈A Lα. Well, we need to check L is really
a linearly independent set (so L ∈S); once that is settled then L is an upper bound in S
since Lα ⊂L for all α ∈A.
Pick a ﬁnite set of vectors v1, . . . , vn in L. We must show they are linearly independent.
Each vk is in some Lα, say v1 ∈Lα1, . . . , vn ∈Lαn. Since the Lα’s are totally ordered, one
of the sets Lα1, . . . , Lαn contains the others (Lemma 1.9). That means v1, . . . , vn are all in
a common Lα, so they are linearly independent.

<!-- page 19 -->
ZORN’S LEMMA AND SOME APPLICATIONS
19
Zorn’s lemma now tells us that S contains a maximal element: there is a linearly inde-
pendent set B in V that is not contained in a larger linearly independent set in V . We will
show B spans V , so it is a basis.
Let W be the span of B. That means W is the set of all ﬁnite F-linear combinations
Pk
i=1 civi with k ≥1, ci ∈F, and vi ∈B. If B does not span V then W ̸= V , so we can
pick v ∈V with v ̸∈W. Then B is a proper subset of B ∪{v}. We will show B ∪{v} is
linearly independent, which contradicts the maximality of B and thus proves W = V .
To prove B ∪{v} is linearly independent, assume otherwise: there is an expression
(4.1)
k
X
i=1
civi = 0
where the coeﬃcients are not all 0 and the vi’s are taken from B ∪{v}. Since the elements
of B are linearly independent, one of the vi’s with a nonzero coeﬃcient must be v. We can
re-index and suppose vk = v, so ck ̸= 0. We must have k ≥2, since otherwise c1v = 0,
which is impossible since v ̸= 0 and the coeﬃcient of v is nonzero. Then
ckv = −
k−1
X
i=1
civi.
Multiplying both sides by 1/ck,
v =
k−1
X
i=1

−ci
ck

vi,
which shows v ∈W. But v ̸∈W, so B ∪{v} is a linearly independent set.
□
Corollary 4.2. Every linearly independent subset of a nonzero vector space V can be
extended to a basis of V .
In particular, every subspace W of V is a direct summand:
V = W ⊕U for some subspace U of V .
Proof. Let L be a linearly independent subset of V . A basis of V containing L will be found
as a maximal linearly independent subset containing L.
Take S to be the set of linearly independent sets in V that contain L. For instance,
L ∈S, so S ̸= ∅. The same argument as in the proof of Theorem 4.1 shows every totally
ordered subset of S has an upper bound. (If the Lα’s are linearly independent sets in V
that each contain L then their union L also contains L, and L ∈S because the Lα’s are
totally ordered, by a kind of argument we’ve made before.)
By Zorn’s lemma there is a maximal element of S. This is a linearly independent set in
V that contains L and is maximal with respect to inclusion among all linearly independent
sets in S containing L. The proof that a maximal element of S is a basis of V follows just
as in the proof of Theorem 4.1.
To prove every subspace W ⊂V is a direct summand, let L be a basis of W. There is a
basis B of V containing L. Let U be the span of the complement B −L. It is left to the
reader to show V = W + U and W ∩U = {0}, so V = W ⊕U.
□
Corollary 4.3. Every spanning set of a nonzero vector space V contains a basis of V .
Proof. Let S be a spanning set of V . Consider the set of linearly independent subsets of S.
This is a nonempty set, as {v} is linearly independent for each v ∈S. Partially order the
set of linearly independent subsets of S by inclusion. If {Li} is a totally ordered subset then

<!-- page 20 -->
20
KEITH CONRAD
S
i Li is a linearly independent subset of S and an upper bound on the Li’s. So by Zorn’s
lemma there is a maximal element B: a linearly independent subset of S that is maximal
with respect to inclusion. We will show B is a spanning set for V so it is a basis. Because S
spans V , it is enough to show every element of S is in the span of B to know V is spanned
by B. If some v ∈S is not in the span of B then B ∪{v} is a linearly independent set and
it is a subset of S that strictly contains B. This contradicts the maximality of B in S.
□
Remark 4.4. To ﬁnd a basis of V inside a spanning set S, a natural ﬁrst idea might be to
ﬁnd a minimal spanning set of V inside of S rather than a maximal linearly independent
subset. The minimality of a spanning set would force its linear independence and thus give
us a basis. It is obvious how to use Zorn’s lemma here: consider the set of all spanning
sets of V inside S, and partially order it by reverse inclusion. If {Si} is a totally ordered
subset then the intersection T
i Si should be an upper bound on all the Si’s (we’re using
reverse inclusion, so an upper bound is a spanning set contained in every Si), and then
Zorn’s lemma gives us maximal elements, which will be minimal spanning sets. But there’s
a problem: how do you prove T
i Si is a spanning set? You can’t; it’s not generally true.
For example, let V = Q as a Q-vector space, enumerate the rationals as {r1, r2, r3, . . . }
and let Si equal Q with the ﬁrst i rationals removed. Each Si is a spanning set of Q as a
Q-vector space, and the Si’s are totally ordered by reverse inclusion, but their intersection
is empty. This is an instructive case where it seems clear how Zorn’s lemma should work,
but it doesn’t work!
Here are some amusing corollaries of the existence of bases in an arbitrary (especially
inﬁnite-dimensional) vector space.
Corollary 4.5 (Hamel). There is a function f : R →R satisfying f(x + y) = f(x) + f(y)
for all x, y ∈R that is not of the form f(x) = cx for some c ∈R.
Proof. Since Q ⊂R, we can think of R as a Q-vector space. In R, the numbers 1 and
√
2 are linearly independent over Q since
√
2 is irrational. The Q-linearly independent
subset {1,
√
2} of R can be extended to a Q-basis {ei} of R by Corollary 4.2. Deﬁne a
bijection f of the Q-basis by f(1) =
√
2, f(
√
2) = 1, and f(ei) = ei for ei ̸= 1 or
√
2. This
bijection extends to a Q-linear map f : R →R by f(P riei) = P rif(ei) on ﬁnite linear
combinations of the Q-basis, where ri ∈Q. Since f is Q-linear, it is an additive function
R →R. Since f(1) =
√
2 and f(
√
2) = 1, there is no c such that f(x) = cx for all x ∈R
(for x = 1 we’d need c =
√
2 and for x =
√
2 we’d need c = 1/
√
2).
□
In this proof, 1 and
√
2 can be replaced by two elements of an arbitrary Q-basis of R.
There is no known way to describe a function f as in Corollary 4.5 that avoids using a
Q-basis of R and there is no concrete formula for a Q-basis of R: it exists purely by Zorn’s
lemma.
Corollary 4.6. As abelian groups, Rn is isomorphic to R for each n ≥1.
Proof. Let {xi}i∈I be a Q-basis of R. Since Rn is an R-vector space with the obvious basis
{e1, . . . , en}, Rn as a Q-vector space has basis {xiej} where i ∈I and j ∈{1, . . . , n}. Since
I is inﬁnite, I × {1, . . . , n} has the same cardinality as I. Therefore the Q-bases of Rn and
R have the same cardinality.
Since I × {1, . . . , n} and I are in bijection, we can write a Q-basis of Rn using index
set I, say {xi}. Then a group isomorphism R →Rn is obtained by sending xi to xi and

<!-- page 21 -->
ZORN’S LEMMA AND SOME APPLICATIONS
21
extending this by Q-linearity: P
i rixi 7→P
i rixi for all ﬁnite Q-linear combinations of the
Q-basis of R.
□
Corollary 4.7. If G is a group with more than two elements then G has a nontrivial
automorphism.
Proof. If G is nonabelian then some element of G is not in the center, so conjugation by
that element is a nontrivial automorphism of G. If G is abelian then inversion (sending
each element to its inverse) is an automorphism, and it is nontrivial unless every element
is its own inverse. If G is abelian and every element is its own inverse then every element
is killed by 2 (x = −x =⇒2x = 0), so G is a vector space over Z/(2). Let {ei}i∈I be a
basis of G over Z/(2). If there is more than one basis element, then exchanging two basis
elements while ﬁxing the rest extends to an automorphism of G. The only case remaining
is a Z/(2)-vector space with a basis of size at most 1. Such groups are trivial or cyclic of
order 2, and their only automorphism is the identity.
□
In the proofs of Theorem 4.1 and Corollaries 4.2 and 4.3, we did not use commutativity
of the coeﬃcient ﬁeld under multiplication except at the end of the proof of Theorem 4.1,
where we wrote ci/ck. If we write that more carefully as c−1
k ci then the proof goes through
when the coeﬃcient ring is a division ring: multiply through on the left by c−1
k
to solve
for v as a linear combination of v1, . . . , vk−1. The proofs of Corollaries 4.2 and 4.3 also go
through with a division ring as the coeﬃcient ring: every nonzero vector space V over a
division ring has a basis, every linearly independent subset of V can be extended to a basis,
and every spanning set of V contains a basis.
Modules over commutative rings that are not ﬁelds need not have a basis. For example,
a nonprincipal ideal in a commutative ring R is an R-module without a basis: if a, b ∈R
are nonzero then they are R-linearly dependent since b · a + (−a) · b = 0, so a basis of an
ideal as an R-module can’t contain more than one element.6 In a module that has a basis,
a linearly independent subset need not extend to a basis and a submodule need not be a
direct summand. For instance, the one-element linearly independent set {(4, 6)} in Z2 can’t
be extended to a basis of Z2 and the submodule (2Z)2 is not a direct summand of Z2. The
reason our proofs for vector spaces over ﬁelds don’t carry over to Z-modules is that nonzero
integers generally don’t have inverses in Z.
5. Application to connected components
A subset C of a topological space X is called connected if, whenever C ⊂U ∪V for
disjoint open subsets U and V of X, either C ⊂U or C ⊂V . This means it is impossible to
decompose C into two parts that lie in disjoint open subsets of X. As a trivial example, one-
element subsets of X are connected. For a nontrivial example, it is fundamental property
of R that the open interval (0, 1) is connected, and more generally all intervals (a, b), (a, b],
[a, b), and [a, b] with a < b are connected. For n ≥1, every open ball in Rn together with
a subset of its boundary is connected.7
Lemma 5.1. If {Ci}i∈I is a collection of nonempty connected subsets of a topological space
X and whenever i ̸= j in I we have Ci ∩Cj ̸= ∅, then S
i∈I Ci is a connected subset of X.
6A nonzero ideal in R has a basis as an R-module if and only if it is a principal ideal with a generator
that is not a zero divisor.
7It suﬃces to prove open balls in Rn are connected, since it can be shown that if C is a connected subset
of X then each set lying between C and its closure C is connected.

<!-- page 22 -->
22
KEITH CONRAD
Proof. Set C = S
i∈I Ci and suppose C ⊂U ∪V where U and V are disjoint open subsets
of X. We want to prove C ⊂U or C ⊂V .
Fixing j ∈I, we have Cj ⊂U ∪V , so Cj ⊂U or Cj ⊂V by connectedness of Cj. Without
loss of generality, Cj ⊂U.
For each i ̸= j we have Ci∩Cj ̸= ∅. Since Ci∩Cj ⊂Cj ⊂U, Ci has nonempty intersection
with U, so Ci ⊂U by connectedness of Ci. Thus Cj ∪S
i∈I−{j} Ci ⊂U, so C ⊂U.
□
The set of nonzero real numbers R× = (−∞, 0) ∪(0, ∞) is not connected, but its two
parts (−∞, 0) and (0, ∞) are each connected and maximally so: they do not belong to a
larger connected subset of R×. This idea generalizes to all topological spaces.
Deﬁnition 5.2. A connected component of a topological space X is a connected subset C
that is maximal with respect to containment: C is connected, and if C ⊂eC ⊂X with eC
connected, then eC = C.
Example 5.3. For n ≥1, the topological space GLn(R) has two connected components:
invertible matrices with positive determinant and invertible matrices with negative deter-
minant.
Example 5.4. The topological space (R×)n has 2n connected components, where the
coordinates in each n-tuple have a ﬁxed sign (positive or negative).
Here are two basic properties of connected components of a topological space X.
(1) If X is nonempty then its connected components are nonempty since one-element
subsets of X are connected.
(2) Diﬀerent connected components of X are disjoint: this is obvious if X = ∅, and if
X ̸= ∅and C1 and C2 are connected components of X with C1 ∩C2 ̸= ∅then we
will prove C1 = C2. The union C1 ∪C2 is connected since C1 ∩C2 ̸= ∅(Lemma 5.1),
so from C1 ⊂C1 ∪C2 and maximality of connected components for containment we
get C1 = C1 ∪C2. Therefore C2 ⊂C1, and changing the roles of C1 and C2 gives us
C1 ⊂C2, so C1 = C2.8
The following theorem about the existence of connected components is analogous to the
existence of maximal ideals in nonzero commutative rings (Theorem 3.1).
Theorem 5.5. Every topological space has a connected component.
Proof. The theorem is obvious for the empty space, so let X be a nonempty topological
space. Let S be the collection of nonempty connected subsets of X. We have S ̸= ∅since
one-element subsets of X are in S. Partially order S by inclusion.
Let {Cα}α∈A be a totally ordered subset of S: each Cα is connected and for all α and β in
A we have either Cα ⊂Cβ or Cβ ⊂Cα. To write down an upper bound for the Cα’s in S, it
is natural to try their union C := S
α∈A Cα. As a set, C certainly contains all the Cα’s, but
is C connected? A union of connected subsets is not usually connected, such as (0, 1)∪(2, 3)
in R. However, for all α and β in A we have Cα ⊂Cβ or Cβ ⊂Cα, so Cα∩Cβ ̸= ∅. Therefore
all pairs of connected subsets in {Cα}α∈A have nonempty intersection, which implies the
union C := S
α∈A Cα is connected by Lemma 5.1, so C is an upper bound in S on the
totally ordered subset {Cα}α∈A. We have shown every totally ordered subset of S has an
upper bound in S.
8Since the closure of a connected subset is connected, by maximality a connected component has to be
its own closure, so connected components are also closed.

<!-- page 23 -->
ZORN’S LEMMA AND SOME APPLICATIONS
23
By Zorn’s lemma S contains a maximal element M. Since M is maximal with respect to
containment among connected subsets of X, M is a connected component of X.
□
Actually, what we really want is a result analogous to Corollary 3.2.
Theorem 5.6. Every nonempty connected subset of a topological space lies in a unique
connected component. In particular, every point in a nonempty topological space lies in a
unique connected component.
Proof. Let N be a nonempty connected subset of a topological space X and let S be the
collection of (nonempty) connected subsets of X that contain N. We have S ̸= ∅since
N ∈S.
For a totally ordered subset {Cα}α∈A of S the union C := S
α∈A Cα contains N and C is
connected since T
α∈A Cα contains N and therefore is nonempty (Lemma 5.1). Thus every
totally ordered subset of S has an upper bound in S.
By Zorn’s lemma S contains a maximal element M. A connected subset of X containing
M also contains N, so it must be M by maximality of M in S. That proves M is a connected
component of X. If M′ is a connected component of X containing N then N ⊂M ∩M′,
so M ∩M′ ̸= ∅. Thus M′ = M since diﬀerent connected components are disjoint.
□
Remark 5.7. The proof of Theorem 5.6 did not use the total ordering in the collection
{Cα}α∈A, which suggests this theorem is not as closely related to Zorn’s lemma as some
other applications of it such as Theorem 3.1. Indeed, the decomposition of X into connected
components can be proved without using Zorn’s lemma. Set x ∼x′ in X if x and x′ lie in a
common connected subset of X. Check this is an equivalence relation on X. Its equivalence
classes are the connected components of X and this shows each element of X belongs to a
(unique) connected component of X.
6. Equivalences and controversies with Zorn’s lemma
We used Zorn’s lemma to prove several existence theorems. Some of those results can be
reversed: Zorn’s lemma is equivalent (within Zermelo-Fraenkel set theory) to
• all nonzero vector spaces over all ﬁelds have a basis [5, 18],
• the existence of a maximal ideal in all nonzero commutative rings [1, 15],
• Theorem 2.4 [4, Theorem 2.1].
See [14, 26] for surveys on equivalents to, and consequences of, Zorn’s lemma.
Remark 6.1. We saw in Theorem 4.1 that Zorn’s lemma implies every nonzero vector space
over every ﬁeld has a basis. It is not obvious that Zorn’s lemma is also implied by every
nonzero vector space over every ﬁeld having a basis. How does that work? The proof deduces
the Axiom of Choice from the existence of bases. That the Axiom of Choice is equivalent
to Zorn’s lemma is a separate argument (we mentioned that in the later part of Section 1).
To deduce the Axiom of Choice from the existence of bases uses an abstract vector space
over a complicated ﬁeld of rational functions. A brief summary of the argument is given by
Noah Schweber in an answer at https://math.stackexchange.com/questions/1650069/.
Zorn’s lemma is not known to be a consequence of the existence of bases of vector spaces
over a speciﬁc ﬁeld of prior interest, like Q or R.
In topology, Tychonoﬀ’s theorem in its general form (allowing compact spaces that are
not Hausdorﬀ) is equivalent to Zorn’s lemma [14, Theorem 4.68], [17], but Tychonoﬀ’s
theorem only for products of compact Hausdorﬀspaces is equivalent to the existence of

<!-- page 24 -->
24
KEITH CONRAD
maximal ideals in all nonzero Boolean rings (the rings satisfying x2 = x for all x) [14,
Deﬁnition 2.15, Theorem 4.37] and that is strictly weaker than Zorn’s lemma.
In functional analysis, the Hahn-Banach theorem is weaker than Zorn’s lemma [24] while
the Krein-Milman theorem is equivalent to it [3]. The existence of a Haar measure on a gen-
eral locally compact Hausdorﬀtopological group was ﬁrst proved by Weil using Tychonoﬀ’s
theorem, which makes the existence of Haar measure rely on a property weaker than Zorn’s
lemma (see the previous paragraph). Cartan later proved the existence of Haar measure
using nothing resembling Tychonoﬀ’s theorem or Zorn’s lemma [9, Chap. 7].
Although Zorn’s lemma is used by the overwhelming majority of working mathematicians,
there is still a certain degree of caution surrounding it, in the sense that some mathemati-
cians may explicitly be attentive to the use of Zorn’s lemma in a proof. Why is this?
The cause is historical and tied up with the equivalence between Zorn’s lemma and the
Axiom of Choice, since the use of the Axiom of Choice led to extremely counterintuitive
theorems in the early 20th century.
• Cantor [7, p. 550] conjectured in 1883 that every set has a well-ordering, calling it
a “law of thought” (Denkgesetz). To show R in particular has a well-ordering was
included by Hilbert as part of the ﬁrst of his famous 23 problems in 1900. Zermelo
[29] proved Cantor’s conjecture in 1904 by using, for the ﬁrst time explicitly, the
Axiom of Choice.9 Most mathematicians refused to accept Zermelo’s result because
a well-ordering on R (or other uncountable sets) is impossible to imagine and the
idea of proving something exists without an explicit procedure to build it was not
yet a standard part of mathematics.10
• Shortly after Lebesgue introduced measure theory, Vitali [28] in 1905 gave the ﬁrst
example of a non-measurable subset of [0, 1] by using a set of representatives for
R/Q inside [0, 1]. Measure theory is inspired by basic geometric notions such as
length and area, so non-measurable subsets of R are impossible to imagine. Vitali’s
construction using a set of representatives for R/Q involves the Axiom of Choice.
• In 1905, Hamel [12] proved R has a basis as a vector space over Q with the help
of Zermelo’s Well-Ordering theorem, which had been proved with the Axiom of
Choice. Hamel used such a basis to show there are functions f : R →R satisfying
f(x+y) = f(x)+f(y) that are not of the form f(x) = cx for c ∈R. Such functions
are highly discontinuous and impossible to imagine in a concrete way.
• In 1924, the Banach–Tarski paradox appeared. It says a closed ball in R3 of radius
r > 0 can be broken up into ﬁnitely many (in fact, ﬁve) pieces that can then be
rearranged using only ﬁnitely many rigid motions of space (rotations and transla-
tions) to become a closed ball of radius r′ > 0 no matter what r and r′ are, such
as a ball the size of a pea being rearrangeable by rigid motions to a ball the size of
the Sun. What was counterintuitive about this to mathematicians was not closed
balls of diﬀerent radii having the same cardinality, but that the bijection could
be achieved using only rigid motions (so no scaling operations). The proof of the
Banach–Tarski paradox uses the Axiom of Choice to pick a collection of coset rep-
resentatives in the group SO(3) for a certain nonabelian subgroup generated by two
elements. Applying all of these coset representatives to a point in the ball will give
9The Axiom of Choice was used before Zermelo’s work without explicit awareness of it as a genuinely
new assumption [22, Chap. 1]. It wasn’t noticed since earlier consequences were not very controversial.
10An example of a non-constructive proof before Zermelo’s work was Hilbert’s proof in 1890 that all
ideals in C[X1, . . . , Xn] are ﬁnitely generated. The proof gave no algorithm for ﬁnding a generating set.

<!-- page 25 -->
ZORN’S LEMMA AND SOME APPLICATIONS
25
us a non-measurable subset of the ball.11 The Banach–Tarski paradox is a reﬁne-
ment of the Hausdorﬀparadox, which is a peculiar decomposition of a sphere that
appeared 10 years earlier and also depends on the Axiom of Choice.
The very negative reaction Zermelo received to his proof of the Well-Ordering theorem
led him to propose axioms for set theory in 1908 to clarify his reasoning [30, 31]. This is
where the term “Axiom of Choice” (Axiom der Auswahl) ﬁrst appeared. Few people cared
about Zermelo’s axioms at ﬁrst. They became the Zermelo–Fraenkel (ZF) axioms in 1922.
For many years it was unclear if the strange Axiom of Choice (strange due to its paradox-
ical consequences, as above) was consistent with the rest of set theory. This led to a habit of
keeping track of theorems proved with that axiom. In 1938 Go¨edel proved that the axioms
for ZFC set theory (ZF axioms plus the Axiom of Choice) are consistent if ZF set theory
is consistent, so the Axiom of Choice could not lead to a contradiction with ZF unless ZF
already has a contradiction within itself. Here is what Joel David Hamkins wrote:12
At least part of the explanation for why people continue to fuss as they
do over the Axiom of Choice is surely the historical fact that there was
a period of several decades during which the axiom was not known to be
relatively consistent with the other axioms of set theory. It was after all
not until 1938 that Goedel proved the relatively consistency of ZFC over
ZF [. . . ] and several more decades passed until Paul Cohen completed the
independence proof by proving that ¬AC is also relatively consistent with ZF
[. . . ]. It was during these intermediate times, and especially the time before
1938 when the axiom was not known to be consistent, that the increasingly
bizarre consequences of AC were being discovered, and so the habit naturally
developed to pay close attention to when the axiom was used. This habit
surely lessened after the independence results, but it was not dropped by
everyone.
Since Zorn’s lemma is equivalent to the Axiom of Choice, the special attention people
once paid to the use of the Axiom of Choice in proofs carried over to the use of Zorn’s
lemma. Although Zorn’s Lemma, the Axiom of Choice, and the Well-Ordering theorem
are all logically equivalent, their statements don’t sound similar at all, so they are not
psychologically equivalent. Jerry Bona described this state of aﬀairs in the following way,
based on his impressions when he was a student:
The Axiom of Choice is obviously true, the Well-Ordering theorem is obvi-
ously false, and who can tell about Zorn’s Lemma?
Appendix A. Application to metric spaces
In a real vector space V , the line between vectors v and w is deﬁned to be the set
{tv + (1 −t)w : 0 ≤t ≤1}. A subset of V is called convex if it contains the line between
every pair of points in the set. This notion of convexity, while very important in analysis,
depends heavily on the real vector space structure: we used real scalars between 0 and 1
and also vector addition. There is a notion of convexity in arbitrary metric spaces, whose
11Since SO(3) is uncountable and a subgroup of it with two generators is countable, coset representatives
of the subgroup are analogous to representatives for R/Q in [0, 1] in Vitali’s construction of a non-measurable
subset of R.
12See https://mathoverflow.net/questions/22927.

<!-- page 26 -->
26
KEITH CONRAD
deﬁnition is based on the idea that the “line” between two points should contain only points
in which the triangle inequality is an equality.
In a metric space (M, ρ), a subset S will be called convex if for every pair of distinct
elements x and y in S there is a z ̸= x, y in S such that ρ(x, y) = ρ(x, z) + ρ(z, y). We
circumvented the lack of a real vector space structure by not deﬁning the line between x
and y, but rather the points that ought to lie on such a “line.” (This deﬁnition of convex
does not quite match the notion in Euclidean space: an open star-shaped region of Rn is
not convex in the usual sense but is convex in the abstract sense above. However, for closed
subsets of Rn with the metric induced from Rn, the above notion of convex does match the
usual meaning of the term.)
It may appear that our deﬁnition is quite weak: we only assume there is one such z.
But by repeating the construction with x, y replaced by x, z, we can get more such points,
although we don’t have much control over the actual distances we can achieve for points
“between” x and y. Zorn’s lemma will oﬀer that control when we are in a complete space.
Theorem A.1. Let (M, ρ) be a complete convex metric space. For distinct points x and y in
M and t ∈[0, ρ(x, y)], there is a z ∈M such that ρ(x, z) = t (and ρ(x, y) = ρ(x, z)+ρ(z, y)).
Proof. We will use Zorn’s lemma twice. Also, we will need to use the formulation of com-
pleteness in terms of nets, not sequences: every Cauchy net in a complete metric space
converges.
First we deﬁne some notation. For a, b ∈M, let
[a, b] := {c ∈M : ρ(a, b) = ρ(a, c) + ρ(c, b)}.
For instance, this set contains a and b, and by hypothesis it contains a point besides a and b
when a ̸= b. Intuitively, [a, b] is the set of points lying on geodesics from a to b. It is helpful
when reading the following discussion to draw many pictures of line segments with points
marked on them. Given t between 0 and ρ(x, y), we will ﬁnd a z ∈[x, y] with ρ(x, z) = t.
Some simple properties of these “intervals” are:
(1) [a, b] = [b, a].
(2) If c ∈[a, b] and b ∈[a, c], then ρ(b, c) = −ρ(b, c), so b = c.
Less simple properties are
(3) If b ∈[a, c] then [a, b] ⊂[a, c] and [b, c] ⊂[a, c].
(4) If b ∈[a, d] and c ∈[b, d] then [a, c] ⊂[a, d], [b, d] ⊂[a, d], and [b, c] = [a, c] ∩[b, d] ⊂
[a, d]. (We will only need that [b, c] lies in the intersection, not equality.)
Proof of (3): Without loss of generality, we show [a, b] ⊂[a, c]. For p in [a, b],
ρ(a, c) ≤ρ(a, p) + ρ(p, c)
≤ρ(a, p) + ρ(p, b) + ρ(b, c)
= ρ(a, b) + ρ(b, c)
= ρ(a, c).
Therefore p ∈[a, c].

<!-- page 27 -->
ZORN’S LEMMA AND SOME APPLICATIONS
27
Proof of (4): By (3), [b, d] ⊂[a, d] and [b, c] ⊂[b, d]. Therefore c ∈[a, d], so [a, c] ⊂[a, d],
so
ρ(a, d) = ρ(a, c) + ρ(c, d)
≤ρ(a, b) + ρ(b, c) + ρ(c, d)
= ρ(a, b) + ρ(b, d)
= ρ(a, d).
Therefore the inequality is an equality, so b ∈[a, c], so [b, c] ⊂[a, c]. Thus [b, c] ⊂[a, c]∩[b, d].
For the reverse inclusion, let p ∈[a, c] ∩[b, d]. Then
ρ(a, d) = ρ(a, b) + ρ(b, d)
= ρ(a, b) + ρ(b, c) + ρ(c, d)
≤ρ(a, b) + ρ(b, p) + ρ(p, c) + ρ(c, d)
= ρ(a, b) + ρ(b, d) −ρ(p, d) + ρ(a, c) −ρ(a, p) + ρ(c, d)
= 2ρ(a, d) −ρ(p, d) −ρ(a, p).
Rearranging terms, ρ(a, p) + ρ(p, d) ≤ρ(a, d), so there is equality throughout, so ρ(b, c) =
ρ(b, p) + ρ(p, c). Thus p ∈[b, c].
Now we are ready to investigate “geodesics” on M coming out of x. Deﬁne a partial
ordering on M that might be called “closer to x on geodesics” by
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
This set is nonempty, since it contains x. We will apply Zorn’s Lemma to A with its induced
partial ordering and show a maximal element of A has distance t from x.
Let {zi}i∈I be a totally ordered subset of A. We want an upper bound. Let
s = sup
i∈I
ρ(x, zi) ≤t.
For each ε > 0, there is some i0 such that
s −ε ≤ρ(x, zi0) ≤s,
so
s −ε ≤ρ(x, zi) ≤s
for all i ≥i0. For i0 ≤i ≤j, s −ε ≤ρ(x, zi) ≤s and
s −ε ≤ρ(x, zj) = ρ(x, zi) + ρ(zi, zj) ≤s
so ρ(zi, zj) ≤ε. Thus {zi} is a Cauchy net, so has a limit ℓby completeness of M. We
show this limit is an upper bound in A.

<!-- page 28 -->
28
KEITH CONRAD
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
As above, every totally ordered subset of B has an upper bound in B, so by Zorn’s lemma
B contains a maximal element, m′. Since m ∈[x, y] and m′ ∈[m, y], we get by (4) that
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
We now have
ρ(x, y) = ρ(x, z) + ρ(z, y) since z ∈[x, y]
≤ρ(x, z) + ρ(z, m′) + ρ(m′, y)
= ρ(x, m′) + ρ(m′, y) since z ∈[x, m′]
= ρ(x, y) since m′ ∈[x, y].
Therefore ρ(y, z) = ρ(z, m′) + ρ(m′, y), so m′ ∈[y, z].
Thus if z ∈A then m ∈[x, z] =⇒z = m. If z ∈B, then m′ ∈[y, z] =⇒z = m′.
Therefore [m, m′] = {m, m′}, so by convexity of M, m = m′, hence m ∈A ∩B. Therefore
ρ(x, m) ≤t and ρ(y, m) ≤ρ(x, y) −t, so
ρ(x, y) = ρ(x, m) + ρ(m, y) ≤ρ(x, y),
so ρ(x, m) = t.
□

<!-- page 29 -->
ZORN’S LEMMA AND SOME APPLICATIONS
29
The z we constructed in the proof need not be unique. Consider M to be the sphere in
R3 with its surface metric, x and y to be the north and south poles and take z to be a point
on some chosen line of latitude. It is natural to expect that if ρ(x, y) is small enough, the z
in Theorem A.1 is unique, and this would let us construct paths in M. For a proof (without
Zorn’s lemma!) that every complete convex metric space is in fact path connected, see [6,
Theorem 14.1, p. 41].
References
[1] B. Banaschewski, A new proof that “Krull implies Zorn”, Math. Logic Quart. 40 (1994), 478–480.
[2] J. L. Bell and F. Jellett, On the relationship between the Boolean prime ideal theorem and two principles
in functional analysis, Bull. Acad. Polon. Sci. S´er. Sci. Math. Astronom. Phys. 19 (1971), 191–194.
[3] J. Bell and D. H. Fremlin, A geometric form of the axiom of choice, Fund. Math. 77 (1972), 167–170.
[4] A. Blass, Injectivity, projectivity, and the axiom of choice, Trans. Amer. Math. Soc. 255 (1979), 31–59.
[5] A. Blass, Existence of bases implies the axiom of choice, pp. 31–33 in: “Axiomatic set theory (Boulder,
Colo., 1983)”, Amer. Math. Soc., Providence, 1984. URL http://www.math.lsa.umich.edu/∼ablass/
bases-AC.pdf.
[6] L. Blumenthal, “Theory and Applications of Distance Geometry,” Clarendon Press, Oxford, 1953.
[7] G. Cantor, “Ueber unendliche, lineare Punktmannichfaltigkeiten. 5. Fortsetzung,” Math. Ann. 21 (1883),
545–591. URL https://eudml.org/doc/157080.
[8] I. S. Cohen, Commutative rings with restricted minimum condition, Duke Math. J. 17 (1950), 27–42.
[9] J. Diestel and A. Spalsbury, “The Joy of Haar Measure,” Amer. Math. Soc., Providence, 2014.
[10] D. Dummit and R. Foote, “Abstract Algebra,” 3rd ed., Wiley, New York, 2004.
[11] J. D. Halpern and A. L´evy, The Boolean prime ideal theorem does not imply the axiom of choice, pp.
83–134 in: “Axiomatic Set Theory (Proc. Sympos. Pure Math., Vol. XIII, Part I), Amer. Math. Soc.,
Providence, 1971.
[12] G. Hamel, Eine Basis aller Zahlen und die unstetigen L¨osungen der Funktionalgleichung f(x + y) =
f(x) + f(y) Math. Annalen 60 (1905), 459–462. URL https://eudml.org/doc/158202.
[13] F. Hausdorﬀ, Zur Theorie der linearen metrischen R¨aume, J. Reine Angew. Math. 167 (1932), 294–311.
URL https://eudml.org/doc/149812.
[14] H. Herrlich, “Axiom of Choice,” Springer-Verlag, Berlin, 2006.
[15] W. Hodges, Krull implies Zorn, J. London Math. Soc. 19 (1979), 285–287.
[16] P. Jothilingam, Cohen’s theorem and Eakin-Nagata theorem revisited, Comm. Algebra 28 (2000), 4861–
4866.
[17] J. Kelley, The Tychonoﬀproduct theorem implies the axiom of choice, Fund. Math. 37 (1950), 75–76.
[18] K. Keremedis, Bases for vector spaces over the two-element ﬁeld and the axiom of choice, Proc. Amer.
Math. Soc. 124 (1996), 2527–2531.
[19] W. Krull, Idealtheorie in Ringen ohne Endlichkeitsbedingung, Math. Annalen 101 (1929), 729–744. URL
https://eudml.org/doc/159366.
[20] T. Y. Lam and M. L. Reyes, A prime ideal principle in commutative algebra, J. Algebra 319 (2008),
3006–3027.
[21] S. Lang, “Algebra,” 3rd revised ed., Springer, New York, 2002.
[22] G. H. Moore, “Zermelo’s Axiom of Choice: its Origins, Development, and Inﬂuence,” Springer-Verlag,
New York, 1982.
[23] A. R. Naghipour, A Simple Proof of Cohen’s Theorem, Amer. Math. Monthly 112 (2005), 825–826.
[24] D. Pincus, The strength of the Hahn-Banach theorem, pp. 203–248 in “Victoria Symposium on Non-
standard Analysis (Univ. Victoria, Victoria, B.C., 1972),” Springer–Verlag, Berlin, 1974.
[25] J. Rotman, “Advanced Modern Algebra,” Prentice-Hall, Upper Saddle River, NJ, 2002.
[26] H. Rubin and J. Rubin, “Equivalents of the axiom of choice. II,” North-Holland, Amsterdam, 1985.
[27] B. Russell, “The Principles of Mathematics”, Cambridge Univ. Press, Cambridge, 1903. URL https://
archive.org/details/principlesofmath01russ.
[28] G. Vitali, Sul problema della misura dei gruppi di punti di una retta, Bologna: Tipograﬁa Gamberini e
Parmeggiani, 1905.
[29] E. Zermelo, Beweis, daß jede Menge wohlgeordnet werden kann, Math. Annalen 59 (1904), 514–516.
URL https://eudml.org/doc/158167.

<!-- page 30 -->
30
KEITH CONRAD
[30] E. Zermelo, Neuer Beweis f¨ur die M¨oglichkeit einer Wohlordnung, Math. Annalen 65 (1908), 107–128.
URL https://eudml.org/doc/158340.
[31] E. Zermelo, Untersuchungen ¨uber die Grundlagen der Mengenlehre. I, Math. Annalen 65 (1908), 261–
281. URL https://eudml.org/doc/158344.
[32] M. Zorn, A remark on method in transﬁnite algebra, Bull. Amer. Math. Soc. 41 (1935), 667–670. URL
https://www.ams.org/journals/bull/1935-41-10/S0002-9904-1935-06166-X/.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*