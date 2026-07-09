# Group Actions

> **Source**: https://kconrad.math.uconn.edu/blurbs/gpaction.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
GROUP ACTIONS
KEITH CONRAD
1. Introduction
The symmetric group Sn behaves, by its very deﬁnition, as permutations of the set
{1, 2, . . . , n}. Dihedral groups Dn for n ≥3, while interpreted geometrically as certain mo-
tions of the plane preserving a regular n-gon, can be considered as a group of permutations
just of the n vertices; rigid motions of the vertices determine where the rest of the n-gon
goes. If we label the n vertices in a deﬁnite manner by the numbers from 1 to n then we
can view Dn as a subgroup of Sn.
Example 1.1. The labeling of the square below lets us regard the 90 degree counterclock-
wise rotation r in D4 as the 4-cycle (1234) and the reﬂection s across the horizontal line
bisecting the square as the transposition (24). The rest of the elements of D4, as permuta-
tions of the vertices, are in the table below the square.
1
2
3
4
1
r
r2
r3
s
rs
r2s
r3s
(1)
(1234)
(13)(24)
(1432)
(24)
(12)(34)
(13)
(14)(23)
If we label the vertices in a diﬀerent way (e.g., swap the labels 1 and 2), then we turn D4
into a diﬀerent subgroup of S4 (e.g., swapping 1 and 2 turns r into (2134) = (1342)).
More abstractly, if we are given a set X (not necessarily the set of vertices of a square),
then the set Sym(X) of all permutations of X is a group under composition, and the
subgroup Alt(X) of even permutations of X is a group under composition. If we list the
elements of X in a deﬁnite order, say as X = {x1, . . . , xn}, then we can think about Sym(X)
as Sn and Alt(X) as An, but a listing in a diﬀerent order leads to diﬀerent identiﬁcations
of Sym(X) with Sn and Alt(X) with An.1
The “abstract” symmetric groups Sym(X) really do arise naturally:
Theorem 1.2 (Cayley). Every ﬁnite group G can be embedded in a symmetric group.
Proof. To each g ∈G, deﬁne the left multiplication function ℓg : G →G, where ℓg(x) = gx
for x ∈G. Each ℓg is a permutation of G as a set, with inverse ℓg−1. So ℓg belongs to
Sym(G). Since ℓg1 ◦ℓg2 = ℓg1g2 (that is, g1(g2x) = (g1g2)x for all x ∈G), associating to g
1When X = ∅, consider Sym(X) and Alt(X) to be trivial groups. The number of permutations of a set
of size 0 is 0! = 1.
1

<!-- page 2 -->
2
KEITH CONRAD
the mapping ℓg gives a homomorphism of groups, G →Sym(G). This homomorphism is
one-to-one since ℓg determines g (after all, ℓg(e) = g). Therefore the correspondence g 7→ℓg
is an embedding of G as a subgroup of Sym(G).
□
Allowing a group to behave as a permutations of a set, as in the proof of Cayley’s theorem,
is a very useful idea, and when this happens we say the group is acting on the set.
Deﬁnition 1.3. An action of a group G on a set X is the choice, for each g ∈G, of a
permutation πg : X →X such that the following two conditions hold:
• πe is the identity: πe(x) = x for each x ∈X,
• for every g1 and g2 in G, πg1 ◦πg2 = πg1g2.
Example 1.4. The group Sn acts on X = {1, 2, . . . , n} in the usual way: πσ(i) = σ(i) for all
i. Then π1(i) = i for all i ∈X and πσ(πσ′(i)) = πσ(σ′(i)) = σ(σ′(i)) = (σσ′)(i) = πσσ′(i).
Example 1.5. Each group G acts on itself (X = G) by left multiplication functions. That
is, we set πg : G →G by πg(h) = gh for all g ∈G and h ∈G. Then the conditions for being
a group action are eh = h for all h ∈G and g1(g2h) = (g1g2)h for all g1, g2, h ∈G, which
are both true since e is an identity and multiplication in G is associative. (This is the idea
behind Cayley’s theorem.)
In practice, πg(x) is written simply as g · x or gx. This is not an actual multiplication
of elements from two possibly diﬀerent sets G and X. It is just the notation for the eﬀect
of g (really, the permutation g is associated to) on the element x that gives us an element
g · x in X. In this notation, the two conditions for a group action in Deﬁnition 1.3 take the
following form:
• for each x ∈X, e · x = x.
• for every g1, g2 ∈G and x ∈X, g1 · (g2 · x) = (g1g2) · x.
The basic idea in a group action is that the elements of a group are viewed as permutations
of a set so that composition of the corresponding permutations is compatible with the
operation in the group.
To get used to the notation, let’s prove a basic result.
Theorem 1.6. Let a group G act on the set X. If x ∈X, g ∈G, and y = g · x, then
x = g−1 · y. If x ̸= x′ then g · x ̸= g · x′.
Proof. From y = g · x we get g−1 · y = g−1 · (g · x) = (g−1g) · x = e · x = x. To show
x ̸= x′ =⇒gx ̸= gx′, we show the contrapositive: if g · x = g · x′ then applying g−1 to both
sides gives g−1 · (g · x) = g−1 · (g · x′), so (g−1g) · x = (g−1g) · x′, so x = x′.
□
There are various types of notation that are used to express the idea “G acts on X”, such
as G
⟳
X and G ↷X, but we will not use these here.
In the study of group actions, many concepts from group theory naturally occur:
• Cosets and conjugacy classes are special cases of orbits for a group action.
• The elements in a group that move one point to another in a group action form a
coset of a certain subgroup.
• Conjugate subgroups arise when comparing the group elements that ﬁx diﬀerent
points in the same orbit.
• Elements in the center of a group G, as well as normal subgroups of G, can be
interpreted as the ﬁxed points for certain actions of G.

<!-- page 3 -->
GROUP ACTIONS
3
Homomorphisms are also present: an action of the group G can be interpreted as a special
kind of homomorphism deﬁned on G. Here are the details.
Theorem 1.7. Actions of a group G on a set X are the same as group homomorphisms
from G to Sym(X), the group of permutations of X.
Proof. Suppose we have an action of G on X. We view g · x as a function of x (with g
ﬁxed). That is, for each g ∈G we have a function πg : X →X by πg(x) = g · x. The axiom
e · x = x
says πe is the identity function on X. The axiom
g1 · (g2 · x) = (g1g2) · x
says πg1 ◦πg2 = πg1g2, so composition of functions on X corresponds to multiplication in
G. Moreover, πg is an invertible function since πg−1 is an inverse: the composite of πg and
πg−1 is πe, which is the identity function on X. Therefore πg ∈Sym(X) and g 7→πg is a
homomorphism G →Sym(X).
Conversely, suppose we have a homomorphism f : G →Sym(X). For each g ∈G, we have
a permutation f(g) on X, and f(g1g2) = f(g1)◦f(g2). Setting g·x = f(g)(x) deﬁnes a group
action of G on X, since the homomorphism properties of f yield the deﬁning properties of
a group action.
□
From this viewpoint, the set of g ∈G that act trivially (g · x = x for all x ∈X) is simply
the kernel of the homomorphism G →Sym(X) associated to the action. Therefore those g
that act trivially on X are said to lie in the kernel of the action.
We will not often use the interpretation of Theorem 1.7 before Section 6. Until then we
take the more concrete viewpoint of a group action as a kind of product g · x of g with x,
taking values in X subject to the properties e · x = x and g1 · (g2 · x) = (g1g2) · x.
Here is an outline of later sections.
Section 2 describes several concrete examples of
group actions and also some general actions available for all groups. Section 3 describes the
important orbit-stabilizer formula. The short Section 4 isolates an important ﬁxed-point
congruence for actions of p-groups. Sections 5 and 6 give applications of group actions to
group theory. In Appendix A, group actions are used to derive three classical congruences
from number theory.
2. Examples
Example 2.1. We can make Rn act on itself by translations: for v ∈Rn, let Tv : Rn →Rn
by Tv(w) = w + v. The axioms for a group action are: T0(w) = w and Tv1(Tv2(w)) =
Tv1+v2(w). These are true from properties of vector addition:
w + 0 = w,
(w + v2) + v1 = w + (v1 + v2).
(This is a special case of Example 1.5 using additive notation.)
Example 2.2. For n ≥3, Dn acts on a regular n-gon as rigid motions. We can also view
Dn as acting just on the n vertices of a regular n-gon. This does not lose information, since
knowing where vertices go under a rigid motion determines where everything else goes. By
focusing on the action of Dn on the n vertices, and labelling them by 1, 2, . . . , n in some
way, we make Dn act on {1, 2, . . . , n} (the case n = 4 is Example 1.1).
We can also make Dn act on the set of diagonals of the regular n-gon, since a rigid motion
sends diagonals to diagonals.

<!-- page 4 -->
4
KEITH CONRAD
Example 2.3. The group GLn(R) acts on vectors in Rn in the usual way that a matrix
can be multiplied with a (column) vector: A · v = Av.
The axioms of a group action
are properties of matrix-vector multiplication: Inv = v and A(Bv) = (AB)v, which are
standard properties of matrix-vector multiplication. In this action, the origin 0 is ﬁxed by
every A while other vectors get moved around (as A varies).
Example 2.4. The group of aﬃne-linear transformations f : Rn →Rn, where f(v) =
Av + b with A ∈GLn(R) and b ∈Rn (an invertible linear map plus a translation), acts
on Rn by f · v = f(v) = Av + b for all v ∈Rn. In this action, the origin 0 is moved to
b. The aﬃne-linear mapping f knows what the A and b in its formula are: b is f(0) and
the columns of A are f(ei) −f(0) where 1 ≤i ≤n. Writing f as fA,b, the identity in the
group is fIn,0, multiplication is fA,b ◦fA′,b′ = fAA′,Ab′+b (compare both sides at each v),
and f−1
A,b = fA−1,−A−1b.
The axioms of a group action in this setting say fA,b · (fA′,b′ · v) = (fA,b ◦fA′,b′) · v for
all v ∈Rn, which the reader should check do hold.
Example 2.5. Let G be the group of aﬃne-linear transformations on (Z/2Z)2, meaning
maps f : (Z/2Z)2 →(Z/2Z)2 where f(v) = Av+b, with A ∈GL2(Z/2Z) and b ∈(Z/2Z)2.
Each f knows its A and b: b = f(0) and A has columns f(
 1
0

) −b and f(
 0
1

) −b. By
counting A’s and b’s, |G| = | GL2(Z/2Z)||(Z/2Z)2| = (6)(4) = 24. Is G ∼= S4?
Since each element of G is an invertible function (Z/2Z)2 →(Z/2Z)2, G acts on (Z/2Z)2.
(This is like the previous example, with Rn replaced by (Z/2Z)2.) Each element of G is
completely determined by its eﬀect on (Z/2Z)2, which has size 4, so the action of G on
(Z/2Z)2 gives us an injective homomorphism G →Sym((Z/2Z)2) ∼= S4. Since |G| = 24,
necessarily this homomorphism is an isomorphism, so G ∼= S4.
To interpret elements of G as permutations in S4, let’s label the elements of (Z/2Z)2 by
1, 2, 3, 4, say
 0
0

↔1,
 1
0

↔2,
 0
1

↔3, and
 1
1

↔4. To realize the permutation (12) in G
means ﬁnding an aﬃne linear map f on (Z/2Z)2 that swaps
 0
0

with
 1
0

and ﬁxes
 0
1

and
 1
1

(that f ﬁxes one of
 0
1

and
 1
1

forces f to ﬁx the other one since there’s nowhere left
for the other vector to go). Writing f(v) = Av + b, we need f
 0
0

=
 1
0

and f
 1
0

=
 0
0

,
so b =
 1
0

and A
 1
0

+ b =
 0
0

. Thus A
 1
0

= −b = b =
 1
0

: the ﬁrst column of A is
 1
0

.
That f
 0
1

=
 0
1

says A
 0
1

+
 1
0

=
 0
1

, so A
 0
1

=
 0
1

−
 1
0

=
 1
1

: the second column of A
is
 1
1

. Thus f(v) = ( 1 1
0 1 )v +
 1
0

.
Check you can derive on your own that the aﬃne-linear maps realizing (13) and (14) in
G are f(v) = ( 1 0
1 1 )v +
 0
1

and f(v) = ( 0 1
1 0 )v +
 1
1

. Don’t merely check those work: be
able to derive these expressions for f in each case.
Example 2.6. The laws of motion in physics to an observer should be the same at every
location, at every time, in every direction, and when traveling in a ﬁxed direction at a ﬁxed
speed. All of these conditions under which the laws of physics should not change can be
described by the action on R4 (spacetime) of a 10-dimensional group, both in relativistic
and non-relativistic settings. See Appendix B for more details.
Example 2.7. The group Sn acts on polynomials f(T1, . . . , Tn), by permuting the variables:
(2.1)
(σ · f)(T1, . . . , Tn) = f(Tσ(1), . . . , Tσ(n)).
The eﬀect is to replace Ti everywhere in f(T1, . . . , Tn) by Tσ(i). For example, (12)(23) =
(123) in S3 and (12)·((23)·(T2+T 2
3 )) = (12)·(T3+T 2
2 ) = T3+T 2
1 and (123)·(T2+T 2
3 ) = T3+T 2
1 ,
giving the same result both ways.

<!-- page 5 -->
GROUP ACTIONS
5
It’s obvious that (1) · f = f. To check that σ · (σ′ · f) = (σσ′) · f for all σ and σ′ in Sn,
so (2.1) is a group action of Sn on polynomials in n variables, σ′ · f replaces each Ti in f
with Tσ′(i). Applying σ to a polynomial replaces each Tj in it with Tσ(j), so it replaces each
Tσ′(i) with Tσ(σ′(i)). Therefore applying σ′ and then σ has the eﬀect
f(T1, . . . , Tn) σ′
7→f(Tσ′(1), . . . , Tσ′(n)) σ7→f(Tσ(σ′(1)), . . . , Tσ(σ′(n))).
The last expression is f(T(σσ′)(1), . . . , T(σσ′)(n)), which is σσ′ · f, so σ · (σ′ · f) = (σσ′) · f.
Since f and σ·f have the same degree, and if f is homogeneous then σ·f is homogeneous,
this action of Sn on polynomials in n variables can be restricted to the polynomials in n
variables with a ﬁxed degree or the homogeneous polynomials in n variables with a ﬁxed
degree. An example is Sn acting on homogeneous linear polynomials {a1T1 + · · · + anTn},
where
(2.2)
σ · (c1T1 + · · · + cnTn) = c1Tσ(1) + · · · + cnTσ(n) = cσ−1(1)T1 + · · · + cσ−1(n)Tn.
Lagrange’s study of the group action in Example 2.7 (ca. 1770) marked the ﬁrst system-
atic use of symmetric groups in algebra. Lagrange wanted to understand why nobody had
found an analogue of the quadratic formula for roots of a polynomial of degree greater than
four. He was not completely successful, although he found in this group action that there
are some diﬀerent features in the cases n ≤4 and n = 5.
Example 2.8. Here is a tricky example, so pay attention. Let Sn act on Rn by permuting
the coordinates: for σ ∈Sn and v = (c1, . . . , cn) ∈Rn, set πσ(v) = (cσ(1), . . . , cσ(n)).
For example, let n = 3, σ = (12), σ′ = (23), and v = (5, 7, 9). Then
πσ(πσ′(v)) = π(12)(π(23)(5, 7, 9)) = π(12)(5, 9, 7) = (9, 5, 7)
and
πσσ′(5, 7, 9) = π(123)(5, 7, 9) = (7, 9, 5),
which do not agree, so sending v to πσ(v) in Rn is not a group action of Sn on Rn.
A peculiar thing happens if we calculate πσ(πσ′(v)) and πσσ′(v) in general to see what is
going wrong, since it is easy to convince ourselves that we do have a group action:
πσ(πσ′(c1, . . . , cn)) = πσ(cσ′(1), . . . , cσ′(n))
= (cσ(σ′(1)), . . . , cσ(σ′(n)))
= (c(σσ′)(1), . . . , c(σσ′(n))
= πσσ′(c1, . . . , cn),
which suggests πσ ◦πσ′ = πσσ′, and that is not what we saw in the numerical example above.
What happened?!? The mistake really is in the general calculation, not the example. Try
to ﬁnd the error before reading further.
The mistake was in the second line, when we computed πσ(cσ′(1), . . . , cσ′(n)) by applying
σ to the indices σ′(i).
A vector does not remember the indices of its coordinates after
they are permuted: to compute π(12)(π(23)(5, 7, 9)) = π(12)(5, 9, 7), the next step treats
(5, 9, 7) as a new vector with coordinates indexed by 1, 2, 3 in that order even though the
coordinate order has changed from the original (5, 7, 9). The computation of πσ(v) always
needs coordinate indices for v to run from 1 to n in that order. Thus when computing
π(12)(π(23)(c1, c2, c3)) = π(12)(c1, c3, c2), in the next step write (c1, c3, c2) = (d1, d2, d3).
Then
π(12)(π(23)(c1, c2, c3)) = π(12)(c1, c3, c2) = π(12)(d1, d2, d3) = (d2, d1, d3) = (c3, c1, c2),

<!-- page 6 -->
6
KEITH CONRAD
which does not agree with
π(12)(23)(c1, c2, c3) = π(123)(c1, c2, c3) = (c2, c3, c1).
In general, for σ and σ′ in Sn, and v = (c1, . . . , cn) in Rn,
πσ(πσ′(v)) = πσ(cσ′(1), . . . , cσ′(n))
= πσ(d1, . . . , dn) where di = cσ′(i)
= (dσ(1), . . . , dσ(n))
= (cσ′(σ(1)), . . . , cσ′(σ(n)))
= (c(σ′σ)(1), . . . , c(σ′σ)(n))
= πσ′σ(v),
so πσ ◦πσ′ is πσ′σ, which is not πσσ′ on Rn if σ′σ ̸= σσ′ (e.g., n ≥3, σ = (12), σ′ = (23)).
A way to explain why πσ ◦πσ′ = πσ′σ without the trick of rewriting coordinates with
another letter is to express the formula πσ((c1, . . . , cn)) = (cσ(1), . . . , cσ(n)) as (πσ(v))i =
vσ(i) for i = 1, . . . , n (e.g., when v = (c1, . . . , cn) and i = 1, (πσ(v))i and vσ(i) are both
cσ(1)). Then for all v ∈Rn and i = 1, . . . , n,
(πσ(πσ′(v)))i = (πσ′(v))σ(i) = vσ′(σi) = v(σ′σ)(i) = (πσ′σ(v))i,
so πσ ◦πσ′ = πσ′σ on Rn.
To have an honest group action here, redeﬁne the eﬀect of Sn on Rn using inverses
in Sn: set σ · v = (cσ−1(1), . . . , cσ−1(n)), or equivalently (σ · v)i = vσ−1(i) for all i. Then
σ · (σ′ · v) = (σσ′) · v and we have a group action of Sn on Rn, which in fact is essentially
the action of Sn from the previous example on homogeneous linear polynomials (see (2.2)).
Indeed, if e1, . . . , en is the standard basis of Rn and v = Pn
i=1 ciei then
σ ·
n
X
i=1
ciei = (cσ−1(1), . . . , cσ−1(n)) =
n
X
i=1
cσ−1(i)ei =
n
X
i=1
cieσ(i),
which is how (2.2) looks with Ti in place of ei. In other words, the action of each σ ∈Sn
on Rn is R-linear and permutes the basis vectors {ei} (not the coeﬃcients!) in the same
way it permutes the indices: σ(ei) = eσ(i).
The lesson from these last two examples is that when Sn permutes variables in a poly-
nomial then it acts “directly”, but when Sn permutes coordinates in a vector then it has
to act using inverses. When Sn acts on variables or coordinates, it acts without inverses in
one case and with inverses in the other case, but it’s easy to forget which case is which. At
least remember that you need to be careful.
Example 2.9. Let G be a group acting on the set X, and S be a set. Write Map(X, S)
for the set of all functions f : X →S. It is natural to try deﬁning an action of G on the set
Map(X, S) by the rule
(2.3)
(πgf)(x) = f(gx),
where gx is the action of g ∈G on x ∈X. While πgf is a function X →S, sending each f
to πgf is usually not an action of G on Map(X, S) even though it is easy to confuse yourself
into thinking it is: for g and h in G, and x ∈X,
πg((πhf)(x)) = πg(f(hx)) = f(g(hx)) = f((gh)x) = (πghf)(x).

<!-- page 7 -->
GROUP ACTIONS
7
This holds for all x ∈X, so πg(πhf) = πghf, right? No. The calculation above is bogus
since the ﬁrst expression πg((πhf)(x)) is nonsense: (πhf)(x) = f(hx) belongs to S and no
action of G has been deﬁned on S, so πg(f(hx)) isn’t deﬁned. Even if G acts on S, πg is
applied to functions X →S, not to elements of S. The mistake was confusing (πgf)(x) in
(2.3) with the meaningless expression πg(f(x)).
A correct calculation is
(πg(πhf))(x) = (πhf)(gx) = f(h(gx)) = f((hg)x) = (πhgf)(x).
Therefore πg(πhf) = πhgf. This ﬂipping in the indices is similar to the false action in
Example 2.8. To get a group action of G on Map(X, S) when G already acts on X (from
the left), replace g with g−1 in (2.3): set
(g · f)(x) = f(g−1x).
Now
(g · (h · f))(x) = (h · f)(g−1x) = f(h−1(g−1x)) = f((gh)−1x) = ((gh) · f)(x),
so g · (h · f) = (gh) · f. This is a group action of G on Map(X, S).
If G is Sn, X is {1, . . . , n} with its natural Sn-action, and S = R, then Map(X, S) = Rn:
writing down a vector v = (c1, . . . , cn) amounts to listing the coordinates in order, and
a list of coordinates in order is a function f : {1, 2, . . . , n} →R where f(i) = ci.
The
deﬁnition (g · f)(i) = f(g−1i) amounts to saying g · (c1, . . . , cn) = (cg−1(1), . . . , cg−1(n)),
which is precisely the valid action of Sn on Rn at the end of Example 2.8.
There are three basic actions of a general group: left multiplication on itself, conju-
gation on itself, and left multiplication on the left cosets of a subgroup. All of these
will now be described. Read carefully!
Example 2.10. To make G act on itself by left multiplication, we let X = G and g · x (for
g ∈G and x ∈G) is the usual product of g and x in G. This example was used already in
the proof of Cayley’s theorem and in Example 1.5, and the deﬁnition of a group action is
satisﬁed by the axioms for multiplication in G, e.g., g1 ·(g2 ·x) = (g1g2)·x from associativity
in G.
Note that right multiplication of G on itself, given by rg(x) = xg for g and x in G, is
not an action since the order of composition gets reversed: rg1 ◦rg2 = rg2g1. But if we set
rg(x) = xg−1 then we do get an action. This could be called the action by right-inverse
multiplication (nonstandard terminology).
Example 2.11. To make G act on itself by conjugation, let X = G and let g · x = gxg−1.
Here g ∈G and x ∈G. Since e · x = exe−1 = x and
g1 · (g2 · x) = g1 · (g2xg−1
2 )
= g1(g2xg−1
2 )g−1
1
= (g1g2)x(g1g2)−1
= (g1g2) · x,
conjugation is a group action.
Example 2.12. For a subgroup H ⊂G, consider the left coset space G/H = {aH : a ∈G}.
(We do not care whether or not H ◁G, as we are just thinking about G/H as a set.) Let

<!-- page 8 -->
8
KEITH CONRAD
G act on G/H by left multiplication. That is, for g ∈G and a left coset aH (a ∈G), set
g · aH = gaH = {gy : y ∈aH}.
This is an action of G on G/H, since eaH = aH and
g1 · (g2 · aH) = g1 · (g2aH)
= g1g2aH
= (g1g2) · aH.
Example 2.10 is the special case when H is trivial.
Example 2.13. Let G = Z/(4) act on itself (X = G) by additions. For instance, addition
by 1 has the eﬀect 0 7→1 7→2 7→3 7→0. Therefore addition by 1 on Z/(4) is a 4-cycle (0123).
Addition by 2 has the eﬀect 0 7→2, 1 7→3, 2 7→0, and 3 7→1. Therefore, as a permutation
on Z/(4), addition by 2 is (02)(13), a product of two 2-cycles. The composition of these
two permutations is (0123)(02)(13) = (0321), which is the permutation of G described by
addition by 3, and 3 = 1+2 in Z/(4). (This is a special case of Example 2.10 using additive
notation.)
We return to the action of a group G on itself by left multiplication and by conjugation,
and extend these actions to subsets rather than just points.
Example 2.14. When A is a subset of G, and g ∈G, the subset gA = {ga : a ∈A} has the
same size as A. Therefore G acts by left multiplication on the set of subsets of G, or even
on the subsets with a ﬁxed size. Example 2.10 is the special case of one-element subsets of
G. Notice that, when H ⊂G is a subgroup, gH is usually not a subgroup of G, so the left
multiplication action of G on its subsets does not convert subgroups into other subgroups.
Example 2.15. As a special case of Example 2.14, let S4 act on the set of pairs from
{1, 2, 3, 4} by the rule σ · {a, b} = {σ(a), σ(b)}.
There are 6 pairs:
x1 = {1, 2}, x2 = {1, 3}, x3 = {1, 4}, x4 = {2, 3}, x5 = {2, 4}, x6 = {3, 4}.
The eﬀect of (12) on these pairs is
(12)x1 = x1,
(12)x2 = x4,
(12)x3 = x5,
(12)x4 = x2,
(12)x5 = x3,
(12)x6 = x6.
Thus, as a permutation of the set {x1, . . . , x6}, (12) acts like (x2x4)(x3x5). That is inter-
esting: we have made a transposition in S4 look like a product of two 2-cycles in S6. In
particular, we have made an odd permutation of {1, 2, 3, 4} look like an even permutation
on a new set. This is an embedding S4 ,→A6.
Example 2.16. Let G be a group. When A ⊂G, gAg−1 is a subset with the same size
as A. Moreover, unlike the left multiplication action of G on its subsets, the conjugation
action of G on its subsets transforms subgroups into subgroups: when H ⊂G is a subgroup,
gHg−1 is also a subgroup. For instance, three of the (seven) subgroups of S4 with size 4 are
{(1), (1234), (13)(24), (1432)},
{(1), (2134), (23)(14), (2431)},
{(1), (12)(34), (13)(24), (14)(23)}.
Under conjugation by S4, the ﬁrst two subgroups can be transformed into each other, but
neither of these subgroups can be conjugated to the third subgroup: the ﬁrst and second
subgroups have an element with order 4 while the third one does not.

<!-- page 9 -->
GROUP ACTIONS
9
While the left multiplication action of G on itself (Example 2.10) turns diﬀerent group
elements into diﬀerent permutations, the conjugation action of G on itself (Example 2.11)
can make diﬀerent group elements act in the same way: if g1 = g2z, where z is in the center
of G, then g1 and g2 have the same conjugation action on G. Group actions where diﬀerent
elements of the group act diﬀerently have a special name:
Deﬁnition 2.17. A group action of G on X is called faithful (or eﬀective) if diﬀerent
elements of G act on X in diﬀerent ways: when g1 ̸= g2 in G, there is an x ∈X such that
g1 · x ̸= g2 · x.
Note that when we say g1 and g2 act diﬀerently, we mean they act diﬀerently somewhere,
not everywhere. This is consistent with what it means to say two functions are not equal:
they take diﬀerent values somewhere, not everywhere.
Example 2.18. The action of G on itself by left multiplication is faithful: diﬀerent elements
send e to diﬀerent places.
Example 2.19. The action of G on itself by conjugation is faithful if and only if G has a
trivial center, because g1gg−1
1
= g2gg−1
2
for all g ∈G if and only if g−1
2 g1 is in the center of
G. When D4 acts on itself by conjugation, the action is not faithful since r2 acts trivially
(it is in the center), so 1 and r2 act in the same way.
Example 2.20. When H is a subgroup of G and G acts on G/H by left multiplication
(Example 2.12), g1 and g2 in G act in the same way on G/H precisely when g1gH = g2gH
for all g ∈G, which means g−1
2 g1 ∈T
g∈G gHg−1. So the left multiplication action of G on
G/H is faithful if and only if the subgroups gHg−1 (as g varies) have trivial intersection.
Example 2.21. The action of GL2(R) on R2 is faithful, since we can recover the columns
of a matrix by acting it on
 1
0

and
 0
1

.
Viewing group actions as homomorphisms (Theorem 1.7), a faithful action of G on X is
an injective homomorphism G →Sym(X). Nonfaithful actions are non-injective as group
homomorphisms. Many important homomorphisms are not injective.
Remark 2.22. What we have been calling a group action could be called a left group action,
while a right group action, denoted xg, has the properties xe = x and (xg1)g2 = x(g1g2).
The exponential notation xg in place of xg works well here, especially by writing the identity
in the group as 1: x1 = x and (xg1)g2 = xg1g2. The distinction between left and right actions
is how a product gg′ acts: in a left action g′ acts ﬁrst and g acts second, while in a right
action g acts ﬁrst and g′ acts second.
Right multiplication of G on itself (or more generally right multiplication of G on the
space of right cosets of a subgroup H) is an example of a right action. To take a more
concrete example, the action of GLn(R) on row vectors of length n is most naturally a right
action since the product vA (not Av) makes sense when v is a row vector and A ∈GLn(R).
The wrong deﬁnitions of actions πg in Examples 2.8 and 2.9, which were wrong because
formulas came out backwards (πg ◦πh = πhg) are legitimate right actions of G.
Many group theorists (unlike most other mathematicians) like to deﬁne the conjugate of
h by g as g−1hg instead of as ghg−1, and this convention ﬁts well with the right (but not
left) conjugation action: setting hg = g−1hg we have h1 = h and (hg1)g2 = hg1g2.
The diﬀerence between left and right actions of a group is largely illusory, since replacing
g with g−1 in the group turns left actions into right actions and conversely because inversion

<!-- page 10 -->
10
KEITH CONRAD
reverses the order of multiplication in G. We saw this idea at work in Examples 2.8, 2.9,
and 2.10. We will not use right actions (except in Example 3.26), so for us “group action”
means “left group action.”
3. Orbits and Stabilizers
The information encoded in a group action has two basic parts: one part tells us where
points go and the other part tells us how points stay put. The following terminology refers
to these ideas.
Deﬁnition 3.1. Let a group G act on a set X. For each x ∈X, its orbit is
Orbx = {g · x : g ∈G} ⊂X
and its stabilizer is
Stabx = {g ∈G : g · x = x} ⊂G.
(The stabilizer of x is often denoted Gx in the literature, where G is the group.) We call x
a ﬁxed point for the action when g · x = x for every g ∈G, that is, when Orbx = {x} (or
equivalently, when Stabx = G).
Writing the deﬁnition of orbits and stabilizers in words, the orbit of a point is a geometric
concept: the set of places where the point can be moved by the group action. The stabilizer
of a point is an algebraic concept: the set of group elements that ﬁx the point.
We will often refer to the elements of X as points and we will refer to the size of an orbit
as its length. If X = G, as in Examples 2.10 and 2.11, then we think about elements of G
as permutations when they act on G and as points when they are acted upon.
Example 3.2. When GL2(R) acts in the usual way on R2, the orbit of 0 is {0} since
A · 0 = 0 for every A in GL2(R). The stabilizer of 0 is GL2(R).
The orbit of
 1
0

is R2−{0}, in other words every nonzero vector can be obtained from
 1
0

by applying a suitable invertible matrix to it. Indeed, if
 a
b

̸= 0, then we have
 a
b

= ( a 1
b 0 )
 1
0

and
 a
b

= ( a 0
b 1 )
 1
0

. One of the matrices ( a 1
b 0 ) or ( a 0
b 1 ) is invertible (since a or b is not zero),
so
 a
b

is in the GL2(R)-orbit of
 1
0

. The stabilizer of
 1
0

is {( 1 x
0 y ) : y ̸= 0} ⊂GL2(R).
Example 3.3. When the group GL2(Z) acts in the usual way on Z2, the orbit of 0 is {0}
with stabilizer GL2(Z). But in contrast to Example 3.2, the orbit of
 1
0

under GL2(Z) is
not Z2 −{0}. Indeed, a matrix ( a b
c d ) in GL2(Z) sends
 1
0

to
 a
c

, which is a vector with
relatively prime coordinates since ad −bc = ±1. (For instance, GL2(Z) can’t send
 1
0

to
 2
0

.) Conversely, each vector
 m
n

in Z2 with relatively prime coordinates is in the GL2(Z)-
orbit of
 1
0

: we can solve mx + ny = 1 for some integers x and y, so ( m −y
n
x ) is in GL2(Z)
(its determinant is 1) and ( m −y
n
x )
 1
0

=
 m
n

.
Check as an exercise that the orbits in Z2 under the action of GL2(Z) are the vectors
whose coordinates have a ﬁxed greatest common divisor. Each orbit contains one vector of
the form
 d
0

for d ≥0, and the stabilizer of
 d
0

for d > 0 is {( 1 x
0 y ) : y = ±1} ⊂GL2(Z).
Example 3.4. Identifying Z/(2) with the subgroup {±In} of GLn(R) gives an action of
Z/(2) on Rn, where 0 acts as the identity and 1 acts by negation on Rn. We can restrict
this action of Z/(2) to the unit sphere of Rn, and then it is called the antipodal action since
its orbits are pairs of opposite points (which are called antipodal points) on the sphere.

<!-- page 11 -->
GROUP ACTIONS
11
Example 3.5. Let G be the Rubik’s cube group: all sequences of motions on the cube
(keeping center colors in place). This group acts on the 8 corner cubelets and 12 edge
cubelets, which are two diﬀerent orbits.
Example 3.6. For n ≥2, consider Sn in its natural action on {1, 2, . . . , n}. What is the
stabilizer of an integer i ∈{1, 2, . . . , n}? It is the set of permutations of {1, 2, . . . , n} ﬁxing
i, which can be thought of as the set of permutations of {1, 2, . . . , n} −{i}. This is an
isomorphic copy of Sn−1 inside Sn (once we identify {1, 2, . . . , n} −{i} in a deﬁnite manner
with the numbers from 1 to n −1). The stabilizer of each number in {1, 2, . . . , n} for the
natural action of Sn on {1, 2, . . . , n} is isomorphic to Sn−1.
Example 3.7. For n ≥2, the even permutations of {1, 2, . . . , n} that ﬁx a number k can be
identiﬁed with the even permutations of {1, 2, . . . , n} −{k}, so the stabilizer of each point
in the natural action of An is essentially An−1 up to relabelling.
Remark 3.8. When trying to think about a set as a geometric object, it is helpful to refer
to its elements as points, no matter what they might really be. For example, when we think
about G/H as a set on which G acts (by left multiplication), it is useful to think about
the cosets of H, which are the elements of G/H, as the points in G/H. At the same time,
though, a coset is a subset of G. There is a tension between these two interpretations: is a
left coset of H a point in G/H or a subset of G? It is both, and it is important to be able
to think about a coset in both ways.
All of our applications of group actions to group theory will ﬂow from the relations
between orbits, stabilizers, and ﬁxed points, which we now make explicit in our three basic
examples of group actions.
Example 3.9. When a group G acts on itself by left multiplication,
• there is one orbit (g = ge ∈Orbe),
• Staba = {g : ga = a} = {e} is trivial,
• there are no ﬁxed points (if |G| > 1).
Example 3.10. When a group G acts on itself by conjugation,
• the orbit of a is Orba = {gag−1 : g ∈G}, which is the conjugacy class of a,
• Staba = {g : gag−1 = a} = {g : ga = ag} is the centralizer of a, denoted Z(a),
• a is a ﬁxed point when it commutes with all elements of G, and thus the ﬁxed points
of conjugation form the center Z(G).
Example 3.11. When a group G acts on G/H (for a subgroup H) by left multiplication,
• there is one orbit (gH = g · H ∈OrbH),
• StabaH = {g : gaH = aH} = {g : a−1ga ∈H} = aHa−1,
• there are no ﬁxed points (if H ̸= G).
These examples illustrate several facts: an action need not have ﬁxed points (Example 3.9
with nontrivial G), diﬀerent orbits can have diﬀerent lengths (Example 3.10 with G = S3),
and the points in a common orbit don’t have to share the same stabilizer (Example 3.11 if
H is not a normal subgroup).
Example 3.12. When G acts on its subgroups by conjugation, StabH = {g : gHg−1 = H}
is the normalizer N(H) and the ﬁxed points are the normal subgroups of G.
When a group G acts on a set X, each subgroup H of G also acts on X. Let’s look at a
few examples.

<!-- page 12 -->
12
KEITH CONRAD
Example 3.13. When H acts on G by left multiplication,
• the orbit of a ∈G is {ha : h ∈H} = Ha, a right H-coset,
• Staba = {h : ha = a} = {e} is trivial,
• there are no ﬁxed points (if |H| > 1).
Example 3.14. When H acts on G by right-inverse multiplication (see Example 2.10),
• the orbit of a ∈G is Orba = {ah−1 : h ∈H} = aH, a left H-coset,
• Staba = {h : ah−1 = a} = {e} is trivial,
• there are no ﬁxed points (if |H| > 1).
Example 3.15. When H acts on G by conjugation,
• the H-orbit of a is Orba = {hah−1 : h ∈H}, which has no special name (this is the
elements of G that are H-conjugate to a),
• Staba = {h ∈H : hah−1 = a} = {h : ha = ah} is the elements of H commuting
with a (this is H ∩Z(a), where Z(a) is the centralizer of a in G).
• a is a ﬁxed point when it commutes with all elements of H.
In the summary table below, G is a group and H is a subgroup of G.
Group
Set
Action
Orbit of x
Stabilizer of x
Sn
{1, . . . , n}
σ · i = σ(i)
{1, . . . , n}
{σ : σ(x) = x} ∼= Sn−1
G
G
g · x = gx
G
{e}
G
G
g · x = gxg−1
Conj. class of x
{g : gx = xg}
H
G
h · x = hx
Hx
{e}
H
G
h · x = xh−1
xH
{e}
G
G/H
g · aH = gaH
G/H
aHa−1 (x = aH)
Here is the fundamental theorem about group actions.
Theorem 3.16. Let a group G act on a set X.
a) Diﬀerent orbits of the action are disjoint and form a partition of X.
b) For each x ∈X, Stabx is a subgroup of G and Stabgx = g Stabx g−1 for all g ∈G.
c) For each x ∈X, there is a bijection Orbx →G/ Stabx by gx 7→g Stabx.
More
concretely, gx = g′x if and only if g and g′ lie in the same left coset of Stabx, and diﬀerent
left cosets of Stabx correspond to diﬀerent points in Orbx. In particular, if x and y are in
the same orbit then {g ∈G : gx = y} is a left coset of Stabx, and
(3.1)
| Orbx | = [G : Stabx].
Parts b and c show the role of conjugate subgroups and cosets of a subgroup when working
with group actions. The formula in part (c) that relates the length of an orbit to the index
in G of a stabilizer for a point in the orbit, is called the orbit-stabilizer formula.
Proof. a) We prove diﬀerent orbits in a group action are disjoint by proving that two orbits
that overlap must coincide.2 Suppose Orbx and Orby have a common element z:
z = g1x,
z = g2y.
We want to show Orbx = Orby. It suﬃces to show Orbx ⊂Orby, since then we can switch
the roles of x and y to get the reverse inclusion.
2The argument will be similar to the proof that diﬀerent left cosets of a subgroup are disjoint: if the
cosets overlap they coincide.

<!-- page 13 -->
GROUP ACTIONS
13
For each point u ∈Orbx, write u = gx for some g ∈G. Since x = g−1
1 z,
u = g(g−1
1 z) = (gg−1
1 )z = (gg−1
1 )(g2y) = (gg−1
1 g2)y,
which shows us that u ∈Orby. Therefore Orbx ⊂Orby.
Every element of X is in some orbit (its own orbit), so the orbits partition X into disjoint
subsets.
b) To see that Stabx is a subgroup of G, we have e ∈Stabx since ex = x, and if
g1, g2 ∈Stabx, then
(g1g2)x = g1(g2x) = g1x = x,
so g1g2 ∈Stabx. Thus Stabx is closed under multiplication. Lastly,
gx = x =⇒g−1(gx) = g−1x =⇒x = g−1x,
so Stabx is closed under inversion.
To show Stabgx = g Stabx g−1, for all x ∈X and g ∈G, observe that
h ∈Stabgx ⇐⇒h · (gx) = gx
⇐⇒(hg)x = gx
⇐⇒g−1((hg)x) = g−1(gx)
⇐⇒(g−1hg)x = x
⇐⇒g−1hg ∈Stabx
⇐⇒h ∈g Stabx g−1,
so Stabgx = g Stabx g−1.
c) The condition gx = g′x is equivalent to x = (g−1g′)x, which means g−1g′ ∈Stabx,
or g′ ∈g Stabx. Therefore g and g′ have the same eﬀect on x if and only if g and g′ lie in
the same left coset of Stabx. (Recall that for all subgroups H of G, g′ ∈gH if and only if
g′H = gH.)
Since Orbx consists of the points gx for varying g, and we showed elements of G have
the same eﬀect on x if and only if they lie in the same left coset of Stabx, we get a bijection
between the points in the orbit of x and the left cosets of Stabx by gx 7→g Stabx. (Think
carefully about why this is well-deﬁned.) Therefore the cardinality of the orbit of x, which
is | Orbx | equals the cardinality of the left cosets of Stabx in G.
□
Example 3.17. For a in a ﬁnite group G, how large is it conjugacy class? The conjugacy
class is the orbit of a under the conjugation action of G on G, so (3.1) says the size of the
conjugacy class is the index [G : Staba], where
Staba = {g ∈G : gag−1 = a} = {g ∈G : ga = ag}.
This subgroup is the elements commuting with a, which is called the centralizer of a and is
written Z(a). (Note Z(a) is not the center Z(G), which is the elements commuting with all
of G.) Since [G : Z(a)] = |G|/|Z(a)| divides |G|, each conjugacy class has size dividing |G|.
For instance, the conjugacy classes of S3 are {(1)}, {(123), (132)}, and {(12), (13), (23)},
whose sizes 1, 2, and 3 are all factors of 6. The conjugacy classes of S4 are represented by
(1), (1234), (12)(34), (123), and (12) and their conjugacy classes have respective sizes 1, 6,
3, 8, and 6. All are factors of 24.

<!-- page 14 -->
14
KEITH CONRAD
Example 3.18. For n ≥2 and k ∈{1, . . . , n −1}, the group G = Sn acts on the k-element
subsets of {1, 2, . . . , n} in the usual way: σ({i1, . . . , ik}) = {σ(i1), . . . , σ(ik)}. This group
action has one orbit since {i1, . . . , ik} = σ({1, . . . , k}) where σ is the permutation
 1 2 ··· k
i1i2···ik

.
The number of k-element subsets of {1, . . . , n} is
 n
k

, by the combinatorial deﬁnition
of binomial coeﬃcients, so Theorem 3.16(c) implies
 n
k

= [Sn : Stab{1,...,k}]. What is the
stabilizer of {1, . . . , k}? It is all σ ∈Sn such that {σ(1), . . . , σ(k)} = {1, . . . , k} (equality of
sets, not ordered sets or k-tuples), which is the same as saying σ permutes {1, . . . , k} and
thus also permutes {k + 1, . . . , n}. Therefore Stab{1,...,k} ∼= Sk × Sn−k, so
n
k

= [Sn : Stab{1,...,k}] =
n!
k!(n −k)!.
This is a derivation of the standard formula for
 n
k

using group actions.
Example 3.19. That the orbits of a group action are disjoint includes as special cases
two basic disjointness results in group theory: the left cosets (resp., right cosets) of a
subgroup and the conjugacy classes of a group are disjoint. The left cosets (resp., right
cosets) of a subgroup are orbits for the action of that subgroup on the group by right-
inverse multiplication (resp., by left multiplication): see Examples 2.10, 3.13, and 3.14. The
conjugacy classes of a group are orbits for the action of the group on itself by conjugation
(see Examples 2.11 and 3.10).
Example 3.20. That each permutation σ in Sn has a disjoint cycle decomposition is a
special case of a group action on a set having disjoint orbits, where the group is ⟨σ⟩and the
set is {1, . . . , n}. This is best understood by ﬁrst looking at disjoint cycles in an example.
Let σ =
 123456789
518324967

in S9 and X = {1, 2, 3, 4, 5, 6, 7, 8, 9}. The way you learn to decompose
σ into disjoint cycles is to pick an x in X and apply σ repeatedly starting at x until you
return to x, then if some of X hasn’t been reached pick a new y in X and apply σ repeatedly
starting at y until you return to y, and so on until all of X has been reached:
• iterates of σ send 1 to 5, 2, and 1 (σ(1) = 5, σ2(1) = σ(5) = 2, σ3(1) = σ(2) = 1),
• 3 is not in {1, 5, 2} and it is sent by iterates of σ to 8, 6, 4, and 3 in that order,
• 7 is not in {1, 5, 2} or {3, 8, 6, 4} and it is sent by iterates of σ to 9 and 7.
All of X has been reached, so the ⟨σ⟩-orbits are {1, 5, 2}, {3, 8, 6, 4}, and {7, 9} and σ has
disjoint cycle decomposition (152)(3864)(79). Why are ⟨σ⟩-orbits the disjoint cycles of σ?
Using Theorem 3.16(c) let’s explain why the ⟨σ⟩-orbit that contains a number x is created
by repeatedly applying σ to x until we ﬁrst return to x and there are no previous repetitions.
Let σ have order m in Sn and let Stabx have order d. Then d | m since Stabx is a subgroup
of ⟨σ⟩and |Orbx| = |⟨σ⟩|/|Stabx| = m/d. Since σm/d has order d and a cyclic group like
⟨σ⟩has one subgroup per size, Stabx = ⟨σm/d⟩. The elements of Orbx are in bijection with
the left cosets of Stabx in ⟨σ⟩, which are the left cosets of ⟨σm/d⟩in ⟨σ⟩. As left coset
representatives we can use σr for 0 ≤r < m/d, so Orbx = {σr(x) : 0 ≤r < m/d} without
repetitions, and the very next number σm/d(x) is x since σm/d ∈Stabx.
Corollary 3.21. Let a ﬁnite group G act on a set X.
a) The length of every orbit in X divides the size of G.
b) Points in a common orbit have conjugate stabilizers, and in particular the size of the
stabilizer is the same for all points in an orbit.
Proof. a) For x ∈X, the length of the orbit of x is [G : Stabx], which divides |G|.

<!-- page 15 -->
GROUP ACTIONS
15
b) If x and y are in the same orbit, write y = gx. Then Staby = Stabgx = g Stabx g−1,
so the stabilizers of x and y are conjugate subgroups.
□
Example 3.22. In a ﬁnite group G, the size of every conjugacy class divides |G| since
conjugacy classes are orbits for an action of G on itself. We saw this in Example 3.17.
A converse of part (b) is not generally true: points with conjugate stabilizers need not
be in the same orbit. Even points with the same stabilizer need not be in the same orbit.
For example, if G acts on itself trivially then all points have stabilizer G and all orbits have
size 1. For a more interesting example, let A4 act on itself by conjugation. Then (123) and
(132) are in diﬀerent orbits (they are not conjugate in A4) but they each have stabilizer
{(1), (123), (132)}. The same feature is true of g and g−1 for every 3-cycle g ∈A4.
Corollary 3.23. Let a group G act on a set X, where X is ﬁnite. Let the diﬀerent orbits
of X be represented by x1, . . . , xt. Then
(3.2)
|X| =
t
X
i=1
| Orbxi | =
t
X
i=1
[G : Stabxi].
Proof. The set X can be written as the union of its orbits, which are mutually disjoint. The
orbit-stabilizer formula tells us how large each orbit is.
□
Example 3.24. Which elements of D6 commute with the reﬂection s? This is asking for
{g ∈D6 : gs = sg}. Three such elements are 1, s, and r3 (since rn/2 ∈Z(Dn) for even n).
Let’s interpret the condition gs = sg as gsg−1 = s: the task is now computing the
stabilizer of s when D6 acts on itself by conjugation.
To compute the stabilizer, let’s
ﬁrst compute the orbit: how many diﬀerent values of gsg−1 are there as g runs over D6?
Elements of D6 are rk (rotations) and rks (reﬂections, so equal to their inverses). From
rksr−k = r2ks,
(rks)s(rks)−1 = rkssrks = rkrks = r2ks
the diﬀerent gsg−1 as g varies in D6 is {revens} = {s, r2s, r4s}.
Since the D6-orbit of s has size 3, the stabilizer of s has index 3 in D6 and thus its size
is |D6|/3 = 12/3 = 4. We already know 1, s, and r3 are in the stabilizer, so being a group
means r3s is in the stabilizer too. That is a fourth element, and the stabilizer has size 4,
so {g ∈D6 : gs = sg} = {1, s, r3, r3s}.
Example 3.25. We examine now a geometric example. The ﬁgure F below is a hexagon
with an X drawn inside of it. Which elements of D6 preserve this ﬁgure when D6 acts in a
natural way on it?
F
For g ∈D6, g(F) = F means g ∈StabF . To compute StabF we ﬁrst compute the orbit
of F: it’s easier to ﬁgure out all the ways F can change than to ﬁgure out all the ways F
can stay the same, and these are related by the orbit-stabilizer formula. By rotating and
reﬂecting it is clear that g(F), as g runs over D6, has only the 3 results below.

<!-- page 16 -->
16
KEITH CONRAD
F
F ′
F ′′
Let r be the 60-degree counterclockwise rotation preserving the hexagonal shape and let
s be the reﬂection across the horizontal line bisecting F. Since F has an orbit of size 3,
its stabilizer in D6 has index 3, so | StabF | = |D6|/3 = 12/3 = 4. From the 180-degree
rotational symmetry of F, r3 ∈StabF . Since s(F) = F, s ∈StabF . Since StabF is a
subgroup of D6, StabF also contains r3s. Thus {1, r3, s, r3s} ⊂StabF , and we are done
since we know | StabF | = 4: StabF = {1, r3, s, r3s} = ⟨r3, s⟩.
While F ′ looks like F, it is not equal to F. What are StabF ′ and {g ∈D6 : g(F) = F ′}?
We can determine these as soon as we know just one g sending F to F ′. Since F ′ = r(F)
we can use g = r. Then Theorem 3.16(b) says
StabF ′ = Stabr(F) = r StabF r−1 = r{1, r3, s, r3s}r−1 = {1, r3, r2s, r5s}
and Theorem 3.16(c) says
{g ∈D6 : g(F) = F ′} = r StabF = r{1, r3, s, r3s} = {r, r4, rs, r4s}.
Similarly, since F ′′ = r−1(F ′′),
StabF ′′ = Stabr−1(F) = r−1 StabF (r−1)−1 = r−1{1, r3, s, r3s}r = {1, r3, r4s, rs}
and
{g ∈D6 : g(F) = F ′′} = r−1 StabF = r−1{1, r3, s, r3s} = {r5, r2, r5s, r2s}.
Example 3.26. The 2 × 2 matrices ( a b
c d ) ∈GL2(R) whose columns add up to 1 form a
subgroup H. This can be checked by a tedious calculation. It can also be seen by observing
that the column sums are the entries in the vector-matrix product (1 1)( a b
c d ), so the matrices
in H are those satisfying (1 1)( a b
c d ) = (1 1). So H is the stabilizer of (1 1) in the (right!)
action of GL2(R) on R2 – viewed as row vectors – by v · A = vA. Thus H is a subgroup
of GL2(R) since the stabilizers of a point are always a subgroup. (Theorem 3.16 for right
group actions should be formulated and checked by the reader.)
Moreover, because (0 1)( 0 −1
1
1 ) = (1 1), Stab(1 1) and Stab(0 1) are conjugate subgroups
in GL2(R). Since Stab(0 1) = {( a b
0 1 ) ∈GL2(R)} = Aﬀ(R), we have
H = Stab(1 1) = Stab(0 1)( 0 −1
1
1 ) =

0
−1
1
1
−1
Aﬀ(R)

0
−1
1
1

.
Example 3.27. As a cute application of the orbit-stabilizer formula we explain why |HK| =
|H||K|/|H∩K| for subgroups H and K of a ﬁnite group G. Here HK = {hk : h ∈H, k ∈K}
is the set of products, which usually is just a subset (not a subgroup) of G. To count the
size of HK, let the direct product group H ×K act on G like this: (h, k)·g = hgk−1. Check
this gives a group action (the group is H × K and the set is G) and HK is the orbit of e.
Therefore the orbit-stabilizer formula tells us
|HK| = |H × K|
| Stabe | =
|H||K|
|{(h, k) : (h, k) · e = e}|.

<!-- page 17 -->
GROUP ACTIONS
17
The condition (h, k) · e = e means hk−1 = e, so Stabe = {(h, h) : h ∈H ∩K}. Therefore
| Stabe | = |H ∩K| and |HK| = |H||K|/|H ∩K|.
Example 3.28. We now discuss the original form of Lagrange’s theorem in group theory.
He proved for each polynomial f(T1, . . . , Tn) in n variables that the number of diﬀerent
polynomials we get from f(T1, . . . , Tn) by permuting its variables is a factor of n!.
For instance, consider the polynomial T1 and n = 3. If we run through all six permuta-
tions of {T1, T2, T3}, and apply each to T1, we get 3 diﬀerent results: T1, T2, and T3. The
polynomial T1T 2
2 + T2T 2
3 + T3T 2
1 has only 2 possibilities under each change of variables:
itself and T2T 2
1 + T1T 2
3 + T3T 2
2 (check this). The polynomial T1 + T 2
2 + T 3
3 has 6 diﬀerent
possibilities. The number of diﬀerent polynomials in each case is a factor of 3!.
To explain Lagrange’s general observation, we apply the orbit-stabilizer formula to the
group action in Example 2.7. That is the action of Sn on n-variable polynomials by permuta-
tions of the variables. For an n-variable polynomial f(T1, . . . , Tn), the diﬀerent polynomials
we obtain by permuting its variables are exactly the polynomials in its Sn-orbit. By the
orbit-stabilizer formula, the number of diﬀerent polynomials we get from f(T1, . . . , Tn) by
permuting its variables is [Sn : Hf], where Hf = Stabf = {σ ∈Sn : σ·f = f}, and this index
divides n!. Cauchy introduced the term “index” in 1815 for the number of diﬀerent poly-
nomials we get from a single polynomial by permuting its variables, and its interpretation
as [Sn : Hf] is why we use the term index for [G : H] in group theory.
In a group action, the length of an orbit divides |G|, but the number of orbits usually
does not divide |G|. For example, D4 and Q8 each have 5 conjugacy classes, and 5 does not
divide 8. But there is an interesting relation between the number of orbits and the group
action.
Theorem 3.29. Let a ﬁnite group G act on a ﬁnite set X with r orbits. Then r is the
average number of ﬁxed points of the elements of the group:
r =
1
|G|
X
g∈G
| Fixg(X)|,
where Fixg(X) = {x ∈X : gx = x} is the set of elements of X ﬁxed by g.
Don’t confuse the set Fixg(X) with the ﬁxed points for the action: Fixg(X) is only the
points ﬁxed by the element g. The set of ﬁxed points for the action of G is the intersection
of the sets Fixg(X) as g runs over the group.
Proof. We will count {(g, x) ∈G × X : gx = x} in two ways.
By counting over g’s ﬁrst we have to add up the number of x’s with gx = x, so
|{(g, x) ∈G × X : gx = x}| =
X
g∈G
| Fixg(X)|.
Next we count over the x’s and have to add up the number of g’s with gx = x, i.e., with
g ∈Stabx:
|{(g, x) ∈G × X : gx = x}| =
X
x∈X
| Stabx |.
Equating these two counts gives
X
g∈G
| Fixg(X)| =
X
x∈X
| Stabx |.

<!-- page 18 -->
18
KEITH CONRAD
By the orbit-stabilizer formula, |G|/| Stabx | = | Orbx |, so
X
g∈G
| Fixg(X)| =
X
x∈X
|G|
| Orbx |.
Divide by |G|:
1
|G|
X
g∈G
| Fixg(X)| =
X
x∈X
1
| Orbx |.
Let’s consider the contribution to the right side from points in a single orbit. If an orbit
has n points in it, then the sum over the points in that orbit is a sum of 1/n for n terms,
and that is equal to 1. Thus the part of the sum over points in an orbit is 1, which makes
the sum on the right side equal to the number of orbits, which is r.
□
Theorem 3.29 is often called Burnside’s lemma, but it is not due to him [7]. He included
it in his book on group theory and attributed the result to Frobenius [1, §118].
Example 3.30. We will use a special case of Theorem 3.29 to prove for all a ∈Z and
m ∈Z+ that
(3.3)
m
X
k=1
a(k,m) ≡0 mod m.
When m = p is a prime number, the left side is (p −1)a + ap = (ap −a) + pa, so (3.3)
becomes ap ≡a mod p, which is Fermat’s little theorem. Thus (3.3) can be thought of as a
generalization of Fermat’s little theorem to all moduli that is essentially diﬀerent from the
generalization called Euler’s theorem, which says aϕ(m) ≡1 mod m if (a, m) = 1: (3.3) is
true for all a ∈Z.
Our setup leading to (3.3) starts with a ﬁnite group G and comes from [5]. For a positive
integer a, G acts on the set of functions Map(G, {1, 2, . . . , a}) by (g · f)(h) = f(g−1h) for
g, h ∈G. This is a special case of the group action at the end of Example 2.9, where G acts
on itself by left multiplication. We want to apply Theorem 3.29 to this action, so we need
to understand the ﬁxed points (really, ﬁxed functions) of each g ∈G. We have g · f = f if
and only if f(g−1h) = f(h) for all h ∈G, which is the same as saying f is constant on every
left coset ⟨g⟩h in G. The number of left cosets of ⟨g⟩in G is [G : ⟨g⟩] = m/ord(g), where
m = |G| and ord(g) is the order of g, so the number of functions ﬁxed by g is am/ord(g), since
the value of the function on each coset can be chosen arbitrarily in {1, . . . , a}. Therefore
Theorem 3.29 implies (1/m) P
g∈G am/ord(g) is a positive integer, so
(3.4)
X
g∈G
am/ord(g) ≡0 mod m.
Since (3.4) depends on a only by the value of a mod m, it holds for all a ∈Z, not just a > 0.
Taking G = Z/(m), each k ∈G has additive order m/(k, m), so (3.4) becomes
m
X
k=1
a(k,m) ≡0 mod m.
Next we turn to the idea of two diﬀerent actions of a group being essentially the same.
Deﬁnition 3.31. Two actions of a group G on sets X and Y are called equivalent if there
is a bijection f : X →Y such that f(gx) = g(f(x)) for all g ∈G and x ∈X.

<!-- page 19 -->
GROUP ACTIONS
19
Actions of G on two sets are equivalent when G permutes elements in the same way on
the two sets after matching up the sets appropriately. When f : X →Y is an equivalence of
group actions on X and Y , gx = x if and only if g(f(x)) = f(x), so the stabilizer subgroups
of x ∈X and f(x) ∈Y are the same.
Example 3.32. Let R× act on a linear subspace Rv0 ⊂Rn by scaling. This is equivalent
to the natural action of R× on R by scaling: let f : R →Rv0 by f(a) = av0. Then f is a
bijection and f(ca) = (ca)v0 = c(av0) = cf(a) for all c in R× and a ∈R.
Example 3.33. Let GL2(R) act on the set B of ordered bases (e1, e2) of R2 in the natural
way: for A ∈GL2(R), A(e1, e2) := (Ae1, Ae2) is another ordered basis of R2. This action
of GL2(R) on B is equivalent to the action of GL2(R) on itself by left multiplication. The
reason is that the columns of a matrix in GL2(R) are a basis of R2 (the ﬁrst and second
columns are an ordering of basis vectors: the ﬁrst column is the ﬁrst basis vector and the
second column is the second one) and two square matrices multiply through multiplication
on the columns: A( a b
c d ) = (A
 a
c

A
 b
d

). Letting f : B →GL2(R) by f(
 a
c

,
 b
d

) = ( a b
c d )
gives a bijection and f(A(e1, e2)) = A · f(e1, e2) for all A ∈GL2(R) and (e1, e2) ∈B.
Example 3.34. Let S3 act on its conjugacy class {(12), (13), (23)} by conjugation. This
action on a 3-element set, described in the ﬁrst half of Table 1 below, looks like the usual
action of S3 on {1, 2, 3} in the second half of Table 1 if we identify (12) with 3, (13) with 2,
and (23) with 1 (in short, identity (ij) with k where k ̸∈{i, j}). Then the action of S3 on
{(12), (13), (23)} by conjugation is equivalent to the natural action of S3 on {1, 2, 3}.
π
π(12)π−1
π(13)π−1
π(23)π−1
π(3)
π(2)
π(1)
(1)
(12)
(13)
(23)
3
2
1
(12)
(12)
(23)
(13)
3
1
2
(13)
(23)
(13)
(12)
1
2
3
(23)
(13)
(12)
(23)
2
3
1
(123)
(23)
(12)
(13)
1
3
2
(132)
(13)
(23)
(12)
2
1
3
Table 1.
Example 3.35. Let H and K be subgroups of G. The group G acts by left multiplication on
G/H and G/K. If H and K are conjugate subgroups then these actions are equivalent: ﬁx a
representation K = g0Hg−1
0
for some g0 ∈G and let f : G/H →G/K by f(gH) = gg−1
0 K.
This is well-deﬁned (independent of the coset representatives for gH) since, for h ∈H,
f(ghH) = ghg−1
0 K = ghg−1
0 g0Hg−1
0
= gHg−1
0
= gg−1
0 K.
The reader can check f(g(g′H)) = gf(g′H) for g ∈G and g′H ∈G/H, and f is a bi-
jection. (The mapping f might depend on g0, but that is not a problem. There can be
multiple equivalences between two equivalent group actions, just as there can be multiple
isomorphisms between two isomorphic groups.)
If H and K are nonconjugate then the actions of G on G/H and G/K are not equivalent:
corresponding points in equivalent actions have the same stabilizer subgroup, but the sta-
bilizer subgroups of left cosets in G/H are conjugate to H and those in G/K are conjugate
to K, and none of the former and latter are equal.

<!-- page 20 -->
20
KEITH CONRAD
The left multiplication action of G on a left coset space G/H has one orbit. It turns out
all actions with one orbit are essentially of this form:
Theorem 3.36. An action of G that has one orbit is equivalent to the left multiplication
action of G on some left coset space of G.
Proof. Suppose that G acts on the set X with one orbit. Fix x0 ∈X and let H = Stabx0.
We will show the action of G on X is equivalent to the left multiplication action of G on
G/H.
Every x ∈X has the form gx0 for some g ∈G, and all elements in a left coset gH have
the same eﬀect on x0: for all h ∈H, (gh)(x0) = g(hx0) = g(x0). Let f : G/H →X by
f(gH) = gx0. This is well-deﬁned, as we just saw. Moreover, f(g · g′H) = gf(g′H) since
both sides equal gg′(x0). We will show f is a bijection.
Since X has one orbit, X = {gx0 : g ∈G} = {f(gH) : g ∈G}, so f is onto.
If
f(g1H) = f(g2H) then g1x0 = g2x0, so g−1
2 g1x0 = x0. Since x0 has stabilizer H, g−1
2 g1 ∈H,
so g1H = g2H. Thus f is one-to-one.
□
A particular case of Theorem 3.36 says that an action of G is equivalent to the left
multiplication action of G on itself if and only if the action has one orbit and the stabilizer
subgroups are trivial.
Deﬁnition 3.37. The action of G on X is called free when every point has a trivial stabi-
lizer.
Example 3.38. The left multiplication action of a group on itself (Example 3.9) is free
with one orbit.
Example 3.39. The antipodal action of Z/(2) on a sphere (Example 3.4) is a free action.
There are uncountably many orbits.
Free actions show up often in topology. Example 3.39 is a typical example of that.
Example 3.40. For an integer n ≥2, let Xn be the set of roots of unity of order n in
C×, so3 |Xn| = ϕ(n). (For instance, X4 = {i, −i}.) The group (Z/(n))× acts on Xn by
a · ζ = ζa. (This is well-deﬁned since a ≡b mod n ⇒ζa = ζb.) Since every element of Xn is
a power of every other element of Xn using exponents relatively prime to n, this action of
(Z/(n))× has a single orbit. Since ζa = ζ only if a ≡1 mod n (ζ has order n), all stabilizers
are trivial (a free action). Thus (Z/(n))× acting on Xn is equivalent to the multiplication
action of (Z/(n))× on itself, except there is no naturally distinguished element of Xn (when
ϕ(n) > 1, i.e., n > 2) while 1 is a distinguished element of (Z/(n))×.
It is worth comparing faithful and free actions. An action is faithful (Deﬁnition 2.17)
when g1 ̸= g2 in G ⇒g1x ̸= g2x for some x ∈X (diﬀerent elements of G act diﬀerently
at some point in X) while an action is free when g1 ̸= g2 in G ⇒g1x ̸= g2x for all x ∈X
(diﬀerent elements of G act diﬀerently at every point of X). So all free actions are faithful.
Since g1x = g2x if and only if g−1
2 g1x = x, we can describe faithful and free actions in terms
of ﬁxed points: an action is faithful when each g ̸= e has Fixg(X) ̸= X while an action is
free when each g ̸= e has Fixg(X) = ∅.
3Having order n is more than just satisfying zn = 1: no smaller power can be 1, so Xn is not all nth
roots of unity when n > 1.

<!-- page 21 -->
GROUP ACTIONS
21
4. Actions of p-groups
The action of a group of prime power size has special features. When |G| = pk for a
prime p, we call G a p-group. For example, (Z/(5))× = {1, 2, 3, 4} and D4 are 2-groups.
The action of a p-group has special features. Because all subgroups of a p-group have p-
power index, the length of an orbit under an action by a p-group is divisible by p unless the
point is a ﬁxed point, when its orbit has length 1. This leads to an important congruence
modulo p for actions of a p-group.
Theorem 4.1 (Fixed Point Congruence). Let G be a ﬁnite p-group acting on a ﬁnite set
X. Then
|X| ≡|{ﬁxed points}| mod p.
Proof. Let the diﬀerent orbits in X be represented by x1, . . . , xt, so Corollary 3.23 leads to
(4.1)
|X| =
t
X
i=1
| Orbxi |.
Since | Orbxi | = [G : Stabxi] and |G| is a power of p, | Orbxi | ≡0 mod p unless Stabxi = G,
in which case Orbxi has length 1, i.e., xi is a ﬁxed point. Thus when we reduce both sides
of (4.1) modulo p, all terms on the right side vanish except for a contribution of 1 for each
ﬁxed point. That implies
|X| ≡|{ﬁxed points}| mod p.
□
Keep in mind that the congruence in Theorem 4.1 holds only for actions by groups with
prime-power size. When a group of size 9 acts we get a congruence mod 3, but when a
group of size 6 acts we do not get a congruence mod 2 or 3.
Corollary 4.2. Let G be a ﬁnite p-group acting on a ﬁnite set X. If |X| is not divisible
by p, then there is at least one ﬁxed point in X. If |X| is divisible by p, then the number of
ﬁxed points is a multiple of p (possibly 0).
Proof. When |X| is not divisible by p, neither is the number of ﬁxed points (by the ﬁxed
point congruence), so the number of ﬁxed points can’t equal 0 (after all, p | 0) and thus is
≥1. On the other hand, when |X| is divisible by p, then the ﬁxed point congruence shows
the number of ﬁxed points is ≡0 mod p, so this number is a multiple of p.
□
Example 4.3. Let G be a p-subgroup of GLn(Z/(p)), where n ≥1. Then there is a nonzero
v ∈(Z/(p))n such that gv = v for all g ∈G. Indeed, because G is a group of matrices it
naturally acts on the set V = (Z/(p))n. (The identity matrix is the identity function and
g1(g2v) = (g1g2)v by the rules of matrix-vector multiplication.) Since the set V has size
pn ≡0 mod p, the number of ﬁxed points is divisible by p. The number of ﬁxed points is
at least 1, since the zero vector is a ﬁxed point, so the number of ﬁxed points is at least p.
A nonzero ﬁxed point for a group of matrices can be interpreted as a simultaneous
eigenvector with eigenvalue 1. These are the only possible simultaneous eigenvectors for G
in (Z/(p))n since every element of G has p-power order and the only element of p-power
order in (Z/(p))× is 1 (so a simultaneous eigenvector for G in (Z/(p))n must have eigenvalue
1 for each element of the group).
Theorem 4.1 can be used to prove existence theorems about ﬁnite groups (nonconstruc-
tively) if we can interpret a problem in terms of ﬁxed points. For example, an element of a
group G is in the center precisely when it is a ﬁxed point for the conjugation action of G

<!-- page 22 -->
22
KEITH CONRAD
on itself. So if we want to show a class of groups has nontrivial centers then we can try to
show there are ﬁxed points for the conjugation action other than the identity element.
5. New Proofs Using Group Actions
In this section we prove two results using group actions (especially using Theorem 4.1):
ﬁnite p-groups have a nontrivial center and if p | |G| then G has an element of order p.
Theorem 5.1. Let G be a nontrivial p-group. Then the center of G has size divisible by p.
In particular, G has a nontrivial center.
This theorem is due to Sylow.4
Proof. The condition that a lies in the center of G can be written as a = gag−1 for all g, so
a is a ﬁxed by all conjugations. The main idea of the proof is to consider the action of G
on itself (X = G) by conjugation and count the ﬁxed points.
We denote the center of G, as usual, by Z(G). Since G is a p-group, and X = G here,
the ﬁxed point congruence (Theorem 4.1) implies |G| ≡|Z(G)| mod p. Since |G| is a power
of p, we get 0 ≡|Z(G)| mod p, so p | |Z(G)|. Because |Z(G)| ≥1, from p | |Z(G)| we get
|Z(G)| ≥p, so Z(G) ̸= {e}.
□
Corollary 5.2. For prime p, every group of order p2 is abelian.
Proof. Let |G| = p2. Nontrivial elements of G have order p or p2. If G has an element of
order p2, then G is cyclic, hence abelian. So assume nontrivial elements of G have order p.
By Theorem 5.1 there is x ̸= e in Z(G), so x has order p. Let y ̸∈⟨x⟩. Since x ∈Z(G),
x and y commute, so all powers xi and yj commute. Thus {xiyj : i, j ∈Z} is an abelian
subgroup of G. It is larger than ⟨x⟩since it contains y, so its order is p2 (the order divides
p2 and is bigger than p). Thus {xiyj : i, j ∈Z} = G, so G is abelian.
□
With almost no extra work than the proof of Theorem 5.1, we can prove a stronger result.
Theorem 5.3. For each nontrivial p-group G, N ∩Z(G) ̸= {e} for all nontrivial nor-
mal subgroups N ◁G. That is, every nontrivial normal subgroup meets the center of G
nontrivially.
Proof. Argue as in the proof of Theorem 5.1, but let G act on N by conjugation. Since N
is a nontrivial p-group, the ﬁxed point congruence (Theorem 4.1) implies N ∩Z(G) has size
divisible by p. Thus N ∩Z(G) is nontrivial.
□
Theorem 5.4 (Cauchy). Let G be a ﬁnite group and p be a prime factor of |G|. Then G
has an element of order p.
Proof. The argument we give is due to James McKay5. We are looking for solutions to the
equation gp = e other than g = e. It is not obvious in advance that there are such solutions.
What we will do is work with a more general equation that has lots of solutions and then
recognize solutions to the original equation gp = e as ﬁxed points under a group action on
the solution set of the more general equation.
4See p. 588 of Th´eor`emes sur les groupes de substitutions, Mathematische Annalen 5 (1872), 584–594;
URL https://eudml.org/doc/156588.
English translation by Robert Wilson, URL http://www.maths.
qmul.ac.uk/~raw/pubs_files/Sylow.pdf.
5J. McKay, Another Proof of Cauchy’s Theorem, Amer. Math. Monthly 66 (1959), 119.

<!-- page 23 -->
GROUP ACTIONS
23
We will generalize the equation gp = e to g1g2 · · · gp = e.
This is an equation in p
unknowns. If we are given choices for g1, . . . , gp−1 then gp is uniquely determined as the
inverse of g1g2 · · · gp−1. Therefore the total number of solutions to this equation is |G|p−1.
By comparison, we have no idea how many solutions there are to gp = e and we only know
one solution, the trivial one that we are not interested in.
Consider the solution set to the generalized equation:
X = {(g1, . . . , gp) : gi ∈G, g1g2 · · · gp = e}.
We noted above that |X| = |G|p−1, so this set is big. The nice feature of this solution
set is that cyclic shifts of one solution give us more solutions: if (g1, g2, . . . , gp) ∈X then
so is (g2, . . . , gp, g1). Indeed, g1 = (g2 · · · gp)−1 and elements commute with their inverses
so g2 · · · gpg1 = e. Successive shifting of coordinates in a solution can be interpreted as a
group action of Z/(p) on X: for j ∈Z/(p), let j · (g1, . . . , gp) = (g1+j, . . . , gp+j), where the
subscripts are interpreted modulo p. This shift is a group action. Since the group doing
the acting is the p-group Z/(p), the ﬁxed point congruence (Theorem 4.1) tells us
(5.1)
|G|p−1 ≡|{ﬁxed points}| mod p.
What are the points of X ﬁxed by Z/(p)? Cyclic shifts bring every coordinate eventually
into the ﬁrst position, so a ﬁxed point of X is one where all coordinates are equal. Calling
the common value g, we have (g, g, . . . , g) ∈X precisely when gp = e. Therefore (5.1)
becomes
(5.2)
|G|p−1 ≡|{g ∈G : gp = e}| mod p.
Up to this point we have not used the condition p | |G|. That is, (5.2) is valid for all ﬁnite
groups G and primes p. This will be useful in Appendix A.
Since p divides |G|, the left side of (5.2) vanishes modulo p, so the right side is a multiple
of p. Thus |{g ∈G : gp = e}| ≡0 mod p. Since |{g ∈G : gp = e}| > 0, there must be some
g ̸= e with gp = e.
□
Cauchy’s theorem has other proofs6 that handle abelian and nonabelian G in diﬀerent
ways. The above proof treats all ﬁnite groups in the same way.
Remark 5.5. Letting G be a ﬁnite group where p | |G|, (5.2) says
(5.3)
|{g ∈G : gp = e}| ≡0 mod p.
Frobenius proved a more general result: when d | |G|,
|{g ∈G : gd = e}| ≡0 mod d.
The divisor d need not be a prime. However, the proof is not as direct as the case of a
prime divisor, and we don’t look at this more closely.
6. More Applications of Group Actions to Group Theory
In Theorem 1.7 we saw how to interpret a group action of G as a homomorphism of G
to a symmetric group. We will now put this idea to use.
Theorem 6.1. Every nonabelian group of order 6 is isomorphic to S3.
6See https://kconrad.math.uconn.edu/blurbs/grouptheory/cauchypf.

<!-- page 24 -->
24
KEITH CONRAD
Proof. Let G be nonabelian with order 6. We will make G permute a set of size 3.
By Cauchy’s theorem, G has elements a of order 2 and b of order 3. If a and b commute,
then ab has order 6, so G is cyclic, which is not true. Thus a and b do not commute, so
bab−1 is not 1 or a. Set H := ⟨a⟩= {1, a}, which is not a normal subgroup of G since
bab−1 ̸∈H. There are 3 left H-cosets in G. Let G act on them by left multiplication. This
group action is a homomorphism ℓ: G →Sym(G/H) ∼= S3. If g ∈ker(ℓ) then gH = H, so
g ∈H. Thus ker(ℓ) is {1} or H. Since H ̸◁G, H can’t be a kernel, so ker(ℓ) = {1}: ℓis
injective. Both G and S3 have order 6, so ℓis an isomorphism G →S3.
□
Theorem 6.2. Let G be a ﬁnite group and H be a p-subgroup such that p | [G : H]. Then
p | [N(H) : H]. In particular, N(H) ̸= H.
We are not assuming here that G is a p-group. The case when G is a p-group as well will
show up in Corollary 6.4.
Proof. Let H (not G!) act on G/H by left multiplication. Since H is a p-group, the ﬁxed
point congruence Theorem 4.1 tells us
(6.1)
[G : H] ≡|{ﬁxed points}| mod p.
What is a ﬁxed point here? It is a coset gH such that hgH = gH for all h ∈H. That
means hg ∈gH for every h ∈H, which is equivalent to g−1Hg = H. This condition means
g ∈N(H), so the ﬁxed points are the cosets gH with g ∈N(H). Thus (6.1) says
[G : H] ≡[N(H) : H] mod p.
This congruence is valid for all p-subgroups H of a ﬁnite group G. When p | [G : H], we
read oﬀfrom the congruence that the index [N(H) : H] can’t be 1, so N(H) ̸= H.
□
Example 6.3. Let G = A4 and H = {(1), (12)(34)}. Then 2 | [G : H], so N(H) ̸= H. In
fact, N(H) = {(1), (12)(34), (13)(24), (14)(23)}.
Corollary 6.4. Let G be a ﬁnite p-group. Every subgroup of G with index p is a normal
subgroup.
Proof. We give two proofs.
First, let the subgroup be H, so H ⊂N(H) ⊂G.
Since
[G : H] = p, one of these inclusions is an equality.
By Theorem 6.2, N(H) ̸= H, so
N(H) = G. That means H ◁G.
For a second proof, consider the left multiplication action of G on the left coset space
G/H.
By Theorem 1.7, this action can be viewed as a group homomorphism ℓ: G →
Sym(G/H) ∼= Sp. Let K be the kernel of ℓ, so K ◁G. We will show H = K. The quotient
G/K embeds into Sp, so [G : K] | p!. Since [G : K] is a power of p, [G : K] = 1 or p.
Each g ∈K satisﬁes gH = H, so g ∈H. In other words, K ⊂H, so [G : K] > 1. Thus
[G : K] = p, so [H : K] = [G : K]/[G : H] = 1, i.e., H = K ◁G.
□
Corollary 6.5. Let G be a ﬁnite group and p be a prime with pn | |G|. Then there is a
chain of subgroups
{e} = H0 ⊂H1 ⊂· · · ⊂Hn ⊂G,
where |Hi| = pi.
Proof. We can take n ≥1. Since p | |G| there is a subgroup of size p by Cauchy’s theorem,
so we have H1. Assuming for some i < n we have a chain of subgroups up to Hi, we will
ﬁnd a subgroup Hi+1 with size pi+1 that contains Hi.

<!-- page 25 -->
GROUP ACTIONS
25
Since p | [G : Hi], by Theorem 6.2 p | [N(Hi) : Hi]. Since Hi ◁N(Hi), we can consider
the quotient group N(Hi)/Hi. It has size divisible by p, so by Cauchy’s theorem there
is a subgroup of size p.
The inverse image of this subgroup under the reduction map
N(Hi) →N(Hi)/Hi is a group Hi+1 of size p|Hi| = pi+1.
□
Theorem 6.6 (C. Jordan). If a nontrivial ﬁnite group acts on a ﬁnite set of size greater
than 1 and the action has only one orbit then some g ∈G has no ﬁxed points.
Proof. By Theorem 3.29,
1 =
1
|G|
X
g∈G
| Fixg(X)| =
1
|G|

|X| +
X
g̸=e
| Fixg(X)|

.
Assume all g ∈G have at least one ﬁxed point. Then
1 ≥
1
|G|(|X| + |G| −1) = 1 + |X| −1
|G|
.
Therefore |X| −1 ≤0, so |X| = 1. This is a contradiction.
□
Remark 6.7. Using the classiﬁcation of ﬁnite simple groups, it can be shown [3] that g in
Theorem 6.6 can be picked to have prime power order. There are examples showing it may
not be possible to pick a g with prime order.
Theorem 6.8. If a group G has a subgroup H with ﬁnite index, then (i) G has a normal
subgroup with ﬁnite index contained in H and (ii) ﬁnitely many subgroups of G contain H.
Proof. (i) Let G →Sym(G/H) be the left multiplication action and let N be its kernel.
Each n ∈N satisﬁes nxH = xH for all x ∈G, so in particular nH = H. Thus n ∈H, so
N ⊂H. Since G/N embeds into Sym(G/H), which is ﬁnite due to [G : H] being ﬁnite,
[G : N] is ﬁnite.
(ii) The subgroups of G that contain H also contain N and only ﬁnitely many subgroups
of G contain N since G/N is ﬁnite, so only ﬁnitely many subgroups of G contain H.
□
The following theorem, in a special case, is due to Poincar´e [2], [6, p. 410]. Its method
of proof is similar to Theorem 6.8(i), so that result is also often attributed to Poincar´e.
Theorem 6.9. If a group G has subgroups H and K with ﬁnite index, then G has a normal
subgroup with ﬁnite index contained in H ∩K. In particular, H ∩K has ﬁnite index in G.
Proof. Let G →Sym(G/H × G/K) be the left multiplication action of G on G/H × G/K,
where g(xH, yK) = (gxH, gyK). Let N be the kernel. Then the group G/N embeds into
the ﬁnite group Sym(G/H × G/K), so [G : N] is ﬁnite.
Each n ∈N satisﬁes nxH = xH and nyK = yK for all x, y ∈G, so in particular nH = H
and nK = K. Thus n ∈H ∩K, so N ⊂H ∩K. Thus [G : H ∩K] is ﬁnite.
□
Theorem 6.10. Let G be a ﬁnite group and H a proper subgroup. Then G ̸= S
g∈G gHg−1.
That is, the union of the subgroups conjugate to a proper subgroup do not ﬁll up the whole
group.
Proof. We will give two proofs. The second will use group actions.

<!-- page 26 -->
26
KEITH CONRAD
Each subgroup gHg−1 has the same size, namely |H|. How many diﬀerent conjugate
groups gHg−1 are there (as g varies)? For g1, g2 ∈G,
g1Hg−1
1
= g2Hg−1
2
⇐⇒g−1
2 g1Hg−1
1 g2 = H
⇐⇒g−1
2 g1H(g−1
2 g1)−1 = H
⇐⇒g−1
2 g1 ∈N(H)
⇐⇒g1 ∈g2 N(H)
⇐⇒g1 N(H) = g2 N(H).
Therefore the number of diﬀerent subgroups gHg−1 as g varies is [G : N(H)].
These
subgroups all contain the identity, so they are not disjoint. Therefore, on account of the
overlap at the identity, the size of S
g∈G gHg−1 is strictly less than
[G : N(H)]|H| =
|G|
| N(H)||H| =
|H|
| N(H)||G| ≤|G|,
so the union of all gHg−1 is not all of G.
For the second proof, we apply Theorem 6.6 to the action of G on X = G/H by left
multiplication. For a ‘point’ gH in G/H, its stabilizer is gHg−1. By Theorem 6.6, some
a ∈G has no ﬁxed points, which means a ̸∈S
g∈G gHg−1.
□
Remark 6.11. Theorem 6.10 is not always true for inﬁnite groups.
For instance, let
G = GL2(C). Every matrix in G has an eigenvector, so we can conjugate each matrix
in G to the form ( a b
0 d ).
Thus G = S
g∈G gHg−1, where H is the proper subgroup of
upper triangular matrices. Theorem 6.10 is true for inﬁnite G when the index [G : H] is
ﬁnite: by Theorem 6.8, G has a normal subgroup N with ﬁnite index contained in H, so if
G = S
g∈G gHg−1, then reducing both sides modulo N gives us G/N = S
g∈G/N g(H/N)g−1,
which contradicts Theorem 6.10 since G/N is ﬁnite.
Remark 6.12. Here is a deep application of Theorem 6.10 to number theory. Suppose a
polynomial f(X) in Z[X] is irreducible and has a root modulo p for every p. Then f(X) is
linear. The proof of this requires Theorem 6.10 and complex analysis.
Remark 6.13. If H ̸◁G, then S
g∈G gHg−1 need not be a subgroup, but it can be, e.g.,
if G = S4 and H = ⟨(12)⟩, then S
g∈G gHg−1 = {(1), (12)(34), (13)(24), (14)(23)} is the
unique normal subgroup of S4 with order 4. In general the subgroup of G generated by
S
g∈G gHg−1 is called the normal closure of H in G.
Corollary 6.14. If H is a proper subgroup of the ﬁnite group G, there is a conjugacy class
in G that is disjoint from H and its conjugate subgroups.
Proof. Pick an x ̸∈S
g∈G gHg−1 and use the conjugacy class of x.
□
Theorem 6.15. Let G be a ﬁnite group with |G| > 1, and p the smallest prime factor of
|G|. Every subgroup of G with index p is a normal subgroup.
Corollary 6.4 is a special case of Theorem 6.15.
Group actions don’t appear in the
statement of Theorem 6.15, but they will play a role in its proof. According to [4, pp. 3-4],
Theorem 6.15 was conjectured and proved by Ernst Straus when he was a student.
Proof. Let H be a subgroup of G with index p, so G/H is a set with size p. We will prove
H ◁G in two ways using group actions.

<!-- page 27 -->
GROUP ACTIONS
27
Method 1. We will show H is the kernel of a homomorphism out of G, and thus is a
normal subgroup of G. The argument will be similar to the second proof of Corollary 6.4.
Let G act on G/H by left multiplication, which (by Theorem 1.7) gives a group homo-
morphism
(6.2)
G →Sym(G/H) ∼= Sp.
This homomorphism sends each g ∈G to the permutation ℓg of G/H, where ℓg(aH) = gaH.
We will show this homomorphism has kernel H.
Write the kernel of the homomorphism (6.2) as K, so K◁G. The group G/K embeds into
Sp, so [G : K] | p!. Since [G : K] divides |G|, whose smallest prime factor is p, (|G|, p!) = p.
Therefore [G : K] is 1 or p. Each g ∈K satisﬁes gH = H, so g ∈H. Thus K ⊂H, so
[G : K] = [G : H][H : K] = p[H : K]. Thus [G : K] = p and [H : K] = 1, so H = K ◁G.
Method 2.7 Let H act on G/H by left multiplication, which (by Theorem 1.7) gives a
group homomorphism
(6.3)
H →Sym(G/H) ∼= Sp.
This action of H on a p-element set ﬁxes the coset H, so each orbit has size at most p−1. By
the orbit-stabilizer formula, an orbit has length dividing |H|, which divides |G|. The only
factor of |G| that’s at most p−1 is 1 (why?), so all orbits of the H-action in (6.3) have length
1. That means (6.3) is a trivial action: hgH = gH for each h ∈H and g ∈G. Therefore
g−1hgH = H, so g−1hg ∈H, which implies (as h varies) g−1Hg ⊂H, so g−1Hg = H since
both sides have the same size. Since this last equation holds for all g ∈G, H ◁G.
□
Some special cases of Theorem 6.15 are worth recording separately.
Corollary 6.16. Let G be a ﬁnite group.
a) If H is a subgroup with index 2, then H ◁G.
b) If G is a p-group and H is a subgroup with index p, then H ◁G.
c) If |G| = pq where p < q are diﬀerent primes, then each subgroup of G with size q is a
normal subgroup.
Proof. Parts (a) and (b) are immediate consequences of Theorem 6.15. For part c, note
that a subgroup with size q is a subgroup with index p. This completes the proof.
□
Part (a) can be checked directly, without the reasoning of Theorem 6.15: if [G : H] = 2
and a ̸∈H, then the two left cosets of H are H and aH, while the two right cosets of H
are H and Ha. Therefore aH = G −H = Ha, so H ◁G. Part (b) was already seen in
Corollary 6.4. (In fact, our second proof of Corollary 6.4 used the same idea as the proof
of Theorem 6.15.) Part (c) could also be checked directly with the Sylow theorems, which
show a subgroup of order q in G is not just normal but in fact unique. In Theorem 6.15,
these disparate results are uniﬁed into a single statement.
All of our applications of group actions in this section have been to ﬁnite groups. Here
is an application to inﬁnite groups.
Theorem 6.17. A ﬁnitely generated group has ﬁnitely many subgroups of index n for each
integer n ≥1.
7I learned this from the answer by Bar Alon at https://math.stackexchange.com/questions/164244/
normal-subgroup-of-prime-index.

<!-- page 28 -->
28
KEITH CONRAD
Proof. Let G be a ﬁnitely generated group and H be a subgroup with ﬁnite index, say n.
The left multiplication action of G on G/H is a group homomorphism ℓ: G →Sym(G/H).
In this action, the stabilizer of the coset H is H (gH = H if and only if g ∈H).
Pick an enumeration of the n cosets in G/H so that the coset H corresponds to the
number 1. This enumeration gives an isomorphism Sym(G/H) ∼= Sn, so we can make G
act on the set {1, 2, . . . , n} and the stabilizer of 1 is H. Therefore we have constructed from
each subgroup H ⊂G of index n an action of G on {1, 2, . . . , n} in which H is the stabilizer
of 1. Since H is recoverable from the action, the number of subgroups of G with index n is
bounded above by the number of homomorphisms G →Sn. Since G is ﬁnitely generated,
it has ﬁnitely many homomorphisms to the ﬁnite group Sn. Therefore G has ﬁnitely many
subgroups of index n.
□
I am not aware of a proof of this theorem that is fundamentally diﬀerent from the one
presented above.
This is probably a good place to warn the reader about a false property of ﬁnitely
generated groups: a subgroup of a ﬁnitely generated group need not be ﬁnitely generated!
However, every ﬁnite-index subgroup of a ﬁnitely generated group is ﬁnitely generated: if
the original group has d generators, a subgroup with index n has at most (d −1)n + 1
generators. This is due to Schreier.
Appendix A. Applications of Group Actions to Number Theory
We apply the ﬁxed point congruence in Theorem 4.1 and its consequence (5.2) to derive
three classical congruences modulo p: those of Fermat, Wilson, and Lucas.
Theorem A.1 (Fermat). If n ̸≡0 mod p, then np−1 ≡1 mod p.
Proof. It suﬃces to take n > 0, since (−1)p−1 ≡1 mod p. (This is obvious for odd p since
p −1 is even, and for p = 2 use −1 ≡1 mod 2.) Apply (5.2) with the additive group
G = Z/(n):
(A.1)
np−1 ≡|{a ∈Z/(n) : pa ≡0 mod n}| mod p.
Since (p, n) = 1, the congruence pa ≡0 mod n is equivalent to a ≡0 mod n, so the right
side of (A.1) is 1.
□
Theorem A.2 (Wilson). For a prime p, (p −1)! ≡−1 mod p.
Proof. We consider (5.2) for G = Sp:
0 ≡|{σ ∈Sp : σp = (1)}| mod p.
An element of Sp has p-th power (1) when it is (1) or a p-cycle. The number of p-cycles is
(p −1)!, and adding 1 to this gives the total count, so 0 ≡(p −1)! + 1 mod p.
□
Theorem A.3 (Lucas). Let p be a prime and n ≥m be nonnegative integers. Write them
in base p as
n = a0 + a1p + a2p2 + · · · + akpk,
m = b0 + b1p + b2p2 + · · · + bkpk,
with 0 ≤ai, bi ≤p −1. Then
n
m

≡
a0
b0
a1
b1

· · ·
ak
bk

mod p.

<!-- page 29 -->
GROUP ACTIONS
29
Proof. We will prove the congruence in the following form: when n ≥m ≥0, and n =
pn′ + a0 and m = pm′ + b0, where 0 ≤a0, b0 ≤p −1, we have
n
m

≡
a0
b0
n′
m′

mod p.
The reader should check this implies Lucas’ congruence by induction on n.
Decompose {1, 2, . . . , n} into a union of p blocks of n′ consecutive integers, from 1 to pn′,
followed by a ﬁnal block of length a0. That is, let
Ai = {in′ + 1, in′ + 2, . . . , (i + 1)n′}
for 0 ≤i ≤p −1, so
{1, 2, . . . , n} = A0 ∪A1 ∪· · · ∪Ap−1 ∪{pn′ + 1, . . . , pn′ + a0}.
For 1 ≤t ≤n′, let σt be the p-cycle
σt = (t, n′ + t, 2n′ + t, . . . , (p −1)n′ + t).
This cycle cyclically permutes the numbers in A0, A1, . . . , Ap−1 that are ≡t mod n′. The
σt’s for diﬀerent t are disjoint, so they commute. Set σ = σ1σ2 · · · σn′. Then σ has order p
as a permutation of {1, 2, . . . , n} (ﬁxing all numbers above pn′).
Let X be the set of m-element subsets of {1, 2, . . . , n}, so |X| =
 n
m

. Let the group ⟨σ⟩
act on X. Since σ has order p, Theorem 4.1 tells us
|X| ≡|{ﬁxed points}| mod p.
The left side is
 n
m

. We will show the right side is
 a0
b0
 n′
m′

.
When is an m-element subset M ⊂{1, 2, . . . , n} ﬁxed by σ? If M contains a number
from 1 to pn′ then σ-invariance implies M contains a number in the range from 1 to n′, i.e.,
M ∩A0 ̸= ∅. Let M contain q numbers in A0. Then M is the union of these numbers and
their translates into each of the p sets A0, . . . , Ap−1, along with some set of numbers from
pn′ + 1 to pn′ + a0, say ℓof those. Then |M| = pq + ℓ. Since M has size m = pm′ + b0, we
have b0 ≡ℓmod p. Both b0 and ℓlie in [0, p −1], so ℓ= b0. Thus q = m′.
Picking a ﬁxed point in X under σ is thus the same as picking m′ numbers from 1 to n′
and then picking b0 numbers from pn′ + 1 to pn′ + a0. Therefore the number of ﬁxed points
is
 n′
m′
 a0
b0

, even in the case when a0 < b0 (in which case there are 0 ﬁxed points, consistent
with
 a0
b0

= 0 in this case).
□
Appendix B. A group action in physics
In this section we expand on Example 2.6 about the transformations of space and time
under which the laws of physics should remain the same,
Our model for spacetime will be R4. In non-relativistic (classical) physics, points in R4
are labeled as (t, x) = (t, x, y, z), where t is time and x, y, z are 3 space coordinates. This is
called Galilean spacetime. In relativistic physics, R4 is called Minkowski spacetime and its
points are written as (ct, x) = (ct, x, y, z), where c is the speed of light. Since c is a speed
and t is time, ct has units of length, just like each component of x. (Physicists who work
in relativity choose units that make c = 1, so t as time or as length has the same value.)
Two diﬀerences between non-relativistic and relativistic physics are described in Table 2:
in non-relativistic physics, speeds are unlimited and motion in space does not aﬀect time,
while in relativistic physics speeds (of physical objects) stay below c and some motions that
we’ll see below mix time and space coordinates in nontrivial ways. Such mixing is why

<!-- page 30 -->
30
KEITH CONRAD
it’s good to make the time coordinate have the same units as the space coordinates by the
device of using ct in place of t.
Allowed speeds
Time/Space coordinates
Non-relativistic
Arbitrary
No mixing
Relativistic
Less than c
Mixing allowed
Table 2. Non-relativistic and relativistic comparisons
The basic transformations of spacetime that don’t change physical laws are (i) translations
in space and time, (ii) rotations of space, and (iii) traveling at a constant speed in a ﬁxed
direction. The transformations in (iii) are called “boosts” and are diﬀerent in non-relativistic
and relativistic physics. Transformations in (i) and (ii) are the same in both settings.
Non-relativistic spacetime transformations
(i) Translations in space and time. These are (t, x) 7→(t + s, x + y) for a time change
(or time shift) by s and space change by y.
(ii) Rotations of space. These are (t, x) 7→(t, Ax) where A is a rotation of R3 ﬁxing
the origin. Such rotations form the group O(3) = {A ∈M3(R) : AA⊤= I3}.
(iii) Boosts by velocity v (ﬁxed speed ||v|| and direction bv = v/||v||). A boost at speed
v along the positive x-axis is (t, x, y, z) 7→(t, tv + x, y, z). More generally, a boost
Bv by velocity v is Bv(t, x) = (t, tv + x). Here v is an arbitrary (velocity) vector
in R3. The eﬀect of Bv on (t, x) can be described as a 4 × 4 matrix transformation,
where we write the coordinates of v as (vx, vy, vz):




1
0
0
0
vx
1
0
0
vy
0
1
0
vz
0
0
1








t
x
y
z



.
The composition of non-relativistic boosts is a non-relativistic boost: Bv ◦Bw =
Bv+w.
Relativistic spacetime transformations
(i) Translations in space and time. These are (ct, x) 7→(c(t + s), x + y) for a time
change by s and space change by y. This is the same as (i) above, except for using
ct in the time coordinate.
(ii) Rotations of space. These are (ct, x) 7→(ct, Ax) where A ∈O(3). This matches (ii)
above except for using ct in the time coordinate.
(iii) Boosts by velocity v (ﬁxed speed ||v|| < c and direction bv = v/||v||). At speed v
along the positive x-axis it is (ct, x, y, z) 7→(cγ(t + xv/c2), γ(tv + x), y, z), where
γ = 1/
p
1 −v2/c2. More generally, the relativistic boost by velocity v is
(ct, x) 7→

γct + γ v
c · x, γtv + x + γ −1
||v||2 (x · v)v

,
(B.1)
where γ = 1/
p
1 −||v||2/c2 = 1/
p
1 −v · v/c2. The factor γ, which depends on the
speed ||v||, is greater than 1. Its ﬁrst-order approximation, by the binomial theorem,

<!-- page 31 -->
GROUP ACTIONS
31
is 1 + 1
2||v||2/c2. As a 4 × 4 matrix transformation, the relativistic boost by v is













γ
γvx
c
γvy
c
γvz
c
γvx
c
1 + (γ −1)v2
x
||v||2
(γ −1)vxvy
||v||2
(γ −1)vxvz
||v||2
γvy
c
(γ −1)vxvy
||v||2
1 + (γ −1)v2
y
||v||2
(γ −1)vyvz
||v||2
γvz
c
(γ −1)vxvz
||v||2
(γ −1)vyvz
||v||2
1 + (γ −1)v2
z
||v||2

























ct
x
y
z












.
As a compressed 2 × 2 matrix (with lower right entry being a 3 × 3 matrix), this is
(B.2)


γ
γv⊤/c
γv/c
I3 + (γ −1)vv⊤
||v||2



ct
x

.
When ||v|| is much smaller than c (that is, ||v||/c is nearly 0), γ is nearly 1 and this
makes the formula in (B.1) approximately (ct, tv + x). That is the non-relativistic
boost by v if points in Galilean spacetime are labeled as (ct, x), which illustrates
how relativistic physics turns into classical physics at speeds much slower than the
speed of light. (We are not taking into account here anything involving mass, which
has its own eﬀects in relativity even at low speeds.)
While non-relativistic boosts aﬀect only space coordinates, relativistic boosts af-
fect time and space coordinates, and as a result the composition of two relativistic
boosts need not be a relativistic boost.
Example B.1. We look at relativistic boosts along the positive x and y-axes, by (3/5)ce1
and by (3/5)ce2. Since γ((3/5)c) = 1/
p
1 −(3/5)2 = 5/4, these two boosts are
(B.3)




5/4
3/4
0
0
3/4
5/4
0
0
0
0
1
0
0
0
0
1




and




5/4
0
3/4
0
0
1
0
0
3/4
0
5/4
0
0
0
0
1



,
respectively. Their product in either order is not a relativistic boost: a relativistic boost
matrix is symmetric and the product of the matrices in (B.3) in either order is not sym-
metric.
In both non-relativistic and relativistic physics we can put the transformations of type
(i), (ii), and (iii) together into the action of a single group on R4.
Non-relativistic spacetime transformations
A translation vector (s, y) ∈R4 acts on R4 in the natural way: (s, y)(t, x) := (s+t, y+x).
A rotation matrix A ∈O(3) and velocity vector v ∈R3 act together on R4 by combining
a rotation of space and a boost:
(B.4)
(v, A)(t, x) = v · (A · (t, x)) = v · (t, Ax) = (t, tv + Ax).
The group of isometries of R3 is all functions x 7→v +Ax for v ∈R3 and A ∈O(3). Under
composition of functions, the group law on isometries is (v′, A′)(v, A) = (v′+A′v, A′A) and
this makes (B.4) an action on R4 by the isometry group of R3 (check!). Such transforma-
tions of R4 are called Galilean transformations. Non-relativistic boosts are the special case

<!-- page 32 -->
32
KEITH CONRAD
of (B.4) where A = I3, and that is why non-relativistic boosts are called “rotation-free”
Galilean transformations.
The group of isometries of Rn is denoted E(n) since distance is fundamental to the
geometry of Rn as Euclidean space. Combining the above actions on R4 by R4 and E(3),
(B.5)
(s, y)((v, A)(t, x)) = (s, y)(t, tv + Ax) = (s + t, y + tv + Ax).
Since
(v, A)((s, y)(t, x)) = (v, A)(s + t, y + x) = (s + t, (s + t)v + Ay + Ax),
the eﬀects of R4 and E(3) on R4 do not commute.
Make the pair ((s, y), (v, A)) ∈R4 × E(3) act on R4 according to (B.5):
(B.6)
((s, y), (v, A))(t, x) := (s + t, y + tv + Ax).
The composition of the eﬀects of ((s′, y′), (v′, A′)) and ((s, y), (v, A)) on (t, x) is
((s′, y′), (v′, A′))(((s, y), (v, A))(t, x)) = ((s′, y′), (v′, A′))(s + t, y + tv + Ax)
= (s′ + (s + t), y′ + (s + t)v′ + A′(y + tv + Ax))
= (s′ + s + t, (y′ + A′y + sv′) + t(v′ + A′v) + (A′A)x).
Writing the ﬁnal result as ((?, ?), (?, ?))(t, x) to ﬁt (B.6) says we should multiply elements
of R4 × E(3) by the rule
(B.7)
((s′, y′), (v′, A′))((s, y), (v, A)) = ((s′ + s, y′ + A′y + sv′), (v′ + A′v, A′A)).
Since elements of E(3) compose by (v′, A′)(v, A) = (v′ + A′v, A′A), we can rewrite (B.7) as
((s′, y′), (v′, A′))((s, y), (v, A)) = ((s′, y′) + (v′, A′)(s, y), (v′, A′)(v, A)),
where (v′, A′)(s, y) = (s, A′y + sv′), which is how E(3) acts on R4 by (B.4). Therefore
(B.7) can be described as a semidirect product group R4 ⋊ϕ E(3) , with ϕ coming from
(B.4). This semidirect product group is the Galilean group of Galilean spacetime R4. The
group R4 ⋊ϕ E(3) acts on R4 by (B.6) and the non-relativistic transformations (i), (ii), and
(iii) of R4 are special cases of (B.6) by taking some components in R4 ⋊ϕ E(3) to be trivial.
Remark B.2. In (B.6), the origin (t, x) = (0, 0) is ﬁxed if and only if (s, y) = (0, 0), so
the elements of the Galilean group ﬁxing the origin are the Galilean transformations. To
distinguish the full Galilean group from the subgroup ﬁxing the origin, the full group is called
the inhomogeneous Galiean group and the subgroup ﬁxing 0 is called the homogeneous
Galilean group, by analogy with linear functions mx + b from high school algebra being
“inhomogeneous” due to a constant term and the linear functions mx from linear algebra
being “homogeneous” due to the constant term being 0.
Relativistic spacetime transformations
The transformations (i), (ii), and (iii) of Minkowski spacetime combine to give the action
of a group on R4 by the same method as in the non-relativistic case. First we make R4 act
on Minkowski spacetime as time and space translations just as in the non-relativistic case:
for (ct, x) ∈R4 and (cs, y) ∈R4, set (cs, y)(ct, x) = (c(s + t), y + x). Each A ∈O(3) acts
on R4 by A(ct, x) = (ct, Ax). Each velocity vector v ∈R3 acts on R4 by the relativistic
boost (B.1). Putting these three transformations together leads to all the “symmetries” of
Minkowski spacetime, which have a complicated composition formula. These transforma-
tions and their products form the Poincar´e group. Its subgroup ﬁxing the origin is built
from rotations and boosts (no nonzero translations) and is called the Lorentz group.

<!-- page 33 -->
GROUP ACTIONS
33
The Galilean and Poincar´e groups both have dimension 4 + 6 = 10. Analogues on Rn+1
(n space coordinates and 1 time coordinate) have dimension (n + 1)(n + 2)/2.
References
[1] W. Burnside, Theory of Groups of Finite Order, Cambridge Univ. Press, Cambridge, 1897. URL
https://archive.org/details/in.ernet.dli.2015.168629/page/n183/mode/2up.
[2] Georg Essl, Answer to “Source of Poincar´e’s theorem on subgroups with ﬁnite index”, History
of Science and Mathematics Stack Exchange. April 21, 2025. URL https://hsm.stackexchange.
com/questions/18494
[3] B. Fein, W. M. Kantor, M. Schacher, Relative Brauer groups II, J. Reine Angew. Math. 328 (1981),
39–57.
[4] B. R. Gelbaum and J. M. H. Olmstead, Theorems and Counterexamples in Mathematics, Springer, New
York, 1990.
[5] I. M. Isaacs and M. R. Pournaki, “Generalizations of Fermat’s Little Theorem Using Group Theory,”
Amer. Math. Monthly 112 (2005), 734–740.
[6] H. Poincar´e, Les fonctions fuchsiennes et l’Arithm´etique, J. Math. Pures Appl. 3 (1887), 405–464. URL
https://www.numdam.org/item/JMPA 1887 4 3
405 0.pdf
[7] Wikipedia, Burnside’s lemma, http://en.wikipedia.org/wiki/Burnside%27s_lemma.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*