# Quotient Groups

> **Source**: https://kconrad.math.uconn.edu/blurbs/quotientgroups.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
QUOTIENT GROUPS
KEITH CONRAD
1. Introduction
By thinking carefully about how we build the group Z/(m) from the group Z and its subgroup
mZ we will be led to an analogous “modular arithmetic” in an arbitrary group. The catch is that
the subgroups we are allowed to mod out by in a general group are not arbitrary as in the case of Z
(where every subgroup is some mZ), but are a special type of subgroup called a normal subgroup,
which we’ll describe in Section 2. A group modulo a normal subgroup is called a quotient group
and we’ll look at some examples and properties of quotient groups in Section 3.
2. Normal Subgroups
The elements of Z/(m) are congruence classes, and a congruence class mod m is a 2-sided
arithmetic progression
a + mZ = {. . . , a −2m, a −m, a, a + m, a + 2m, . . .}.
We add two elements in Z/(m) by adding representatives of the congruence classes:
(2.1)
a + b := a + b,
where a is shorthand for a+mZ. The point about (2.1) is that it is well-deﬁned, i.e., it’s independent
of the choice of representatives used from the two congruence classes: if a = a′ and b = b′ then
a + b = a′ + b′. That is, if a ≡a′ mod m and b ≡b′ mod m then a + b ≡a′ + b′ mod m.
Since a + mZ is the same thing as a coset of mZ in Z, we want to carry over the idea of addition
of integers modulo m to a multiplication of left cosets (or of right cosets) of a subgroup of a group:
if G is a group and H is a subgroup, could we deﬁne the product of two left cosets of H to be
another left coset of H by the rule
(2.2)
g1H · g2H ?= g1g2H.
Unfortunately this sometimes makes no sense, since it can depend on the choice of representatives
for the left cosets.
Example 2.1. Take G = D3 and H = ⟨s⟩= {1, s}. Then
rH = {r, rs} = rsH
and
r2H = {r2, r2s} = r2sH
However
r · r2H = H
while
rs · r2sH = rr−2ssH = r−1H ̸= H.
So even though r and rs are in the same left H-coset, and r2 and r2s are in the same left H-coset,
r · r2 and rs · r2s are not in the same left H-coset, so the left H-cosets they are in don’t match.
A similar problem happens for a deﬁnition like (2.2) with right cosets: Hr = Hr2s and Hr2 =
Hrs, but Hr · r2 = H while Hr2s · rs = Hr ̸= H.
1

<!-- page 2 -->
2
KEITH CONRAD
It turns out that for (2.2) to make sense as an operation on left cosets of H we need H to be a
special type of subgroup: one for which left and right cosets by each element are the same thing.
Deﬁnition 2.2. A subgroup N of a group G is called normal if gN = Ng for every g ∈G.
Equivalently, N is normal if gNg−1 = N for every g ∈G.1
The condition gN = Ng is not saying gn = ng for all n ∈N, but rather than for each n ∈N we
can write gn = n′g for some n′ ∈N, and ng = n′′g for some n′′ ∈N: the sets gN and Ng agree,
but not necessarily by having gn equal ng all the time.
Remark 2.3. Unlike cyclic subgroups or abelian subgroups, which are subgroups that happen to
be cyclic or abelian groups on their own, a normal subgroup is not a subgroup that’s a “normal
group,” since there is no such thing as a “normal group.” Whether or not a subgroup N of a group
G is a normal subgroup (that is, whether or not gN = Ng for every g ∈G) is not an internal
property of N, but depends on how N interacts with the larger group G it lies inside.
Example 2.4. In every group G both G and its trivial subgroup {e} are normal subgroups of G.
Example 2.5. If G is an abelian group then every subgroup of G is a normal subgroup, since the
order of multiplication doesn’t matter: gN = Ng because gn = ng for all g ∈G and n ∈N.
Example 2.6. The center Z of a group G is a normal subgroup since each element of Z commutes
with each element of G: gz = zg for all g ∈G and z ∈Z, so gZ = Zg. By similar reasoning,
each subgroup of the center of G is a normal subgroup of G. (This last part subsumes the previous
example, since if G is abelian its center is G, so subgroups of the center are all subgroups of G.)
Remark 2.7. The reasoning in the previous example depends on how the center Z interacts with
the whole group G. In particular, it is generally false that abelian subgroups are normal subgroups.
For example, ⟨s⟩= {1, s} is an abelian (and in fact cyclic) subgroup of Dn for n ≥3 but it is not
normal in Dn since r{1, s} = {r, rs}, {1, s}r = {r, sr}, and rs ̸= sr: sr = r−1s = rn−1s ̸= rs since
r has order n and n > 2. Thus r{1, s} ̸= {1, s}r.
Example 2.8. In Dn the subgroup H = ⟨r⟩= {1, r, r2, . . . , rn−1} is normal. To check gH = Hg
for each g ∈Dn, this is immediate if g ∈H since then gH = H and Hg = H. If g ̸∈H then g is
not a rotation so it is a reﬂection, say g = ris. Then
gH = risH = sr−iH = sH
because r−i ∈H, and
Hg = Hris = Hs
because ri ∈H, so we are reduced to checking sH = Hs:
sH = {s, sr, sr2, . . . , srn−1} = {s, r−1s, r−2s, . . . , r−(n−1)s}
and
Hs = {s, rs, r2s, . . . , rn−1s},
and the lists of elements in sH and Hs are the same (just in a diﬀerent order) since r−i = rn−i.
Example 2.8 is a special case of the following theorem.
1In the late 19th and early 20th centuries, normal subgroups had many other names, such as “invariant subgroups”
and “self-conjugate subgroups”. See https://math.stackexchange.com/questions/898977 for further synonyms,
which are all obsolete. The term “normal” is famous in mathematics for the wide number of unrelated meanings it
has in diﬀerent areas, as shown at https://en.wikipedia.org/wiki/Normal, but it’s not as bad as regular: https://
en.wikipedia.org/wiki/Regular.

<!-- page 3 -->
QUOTIENT GROUPS
3
Theorem 2.9. Every subgroup of index 2 in a group is a normal subgroup.
Proof. Let H have index 2 in the group G. For each g ∈G we want to show gH = Hg. If g ∈H
then this is immediate since gH = H and Hg = H. If g ̸∈H then gH ̸= H, so from H having
index 2 in G the coset gH is the other coset of H besides H, i.e., gH = G −H. For the same
reason, using right cosets, we have Hg ̸= H so Hg = G −H. Thus gH = G −H = Hg.
□
Example 2.10. Since [Sn : An] = 2, An is a normal subgroup of Sn.
The standard notation to indicate a subgroup H of a group G is normal is: H ◁G (not H∆G).
For example, mZ◁Z (Z is abelian), ⟨r⟩◁Dn (index-2 subgroup), and An ◁Sn (index-2 subgroup).
Let’s show that multiplying cosets of a normal subgroup by the rule (2.2) is well-deﬁned: it is
independent of the choice of representative.
Theorem 2.11. Let N ◁G. If g1N = g′
1N and g2N = g′
2N for some g1, g′
1, g2, g′
2 ∈G then
g1g2N = g′
1g′
2N.
Proof. Since g1N = g′
1N and g2N = g′
2N, we can write g1 = g′
1n1 and g2 = g′
2n2 for n1, n2 ∈N.
Then
g1g2 = g′
1n1g′
2n2 = g′
1(n1g′
2)n2.
Since N is a normal subgroup, n1g′
2 = g′
2n′
1 for some n′
1 ∈N. Then
g1g2 = g′
1(g′
2n′
1)n2 = g′
1g′
2(n′
1n2),
and n′
1n2 ∈N, so g1g2N = g′
1g′
2N.
□
We will build on this result in the next section to show the operation g1N · g2N = g1g2N makes
the cosets of N in G into a (new) group.
To verify that a subgroup H of a group G is a normal subgroup, often it is useful to think about
the condition gH = Hg as gHg−1 = H, and it turns out that to check gHg−1 = H for all g ∈G,
just checking the containment of the left side in the right side (for all g) is suﬃcient.
Theorem 2.12. A subgroup H of a group G is normal if and only if gHg−1 ⊂H for all g ∈G.
That is, gHg−1 = H for all g ∈G if and only if gHg−1 ⊂H for all g ∈G.
Proof. The direction (⇒) is immediate: if gHg−1 = H for all g ∈G then obviously gHg−1 ⊂H for
all g ∈G. For the more interesting direction (⇐), suppose gHg−1 ⊂H for all g ∈G. Replacing
g with g−1 (which we can do since the containment is assumed to hold for all g in G) we get
g−1Hg ⊂H for all g too.
Multiplying both sides of gHg−1 ⊂H on the right by g gives us
gH ⊂Hg, and multiplying both sides of g−1Hg ⊂H on the left by g gives us Hg ⊂gH. From
gH ⊂Hg and Hg ⊂gH we get gH = Hg.
□
Example 2.13. We will show SL2(R) ◁GL2(R).
By Theorem 2.12 it is suﬃcient to show
A SL2(R)A−1 ⊂SL2(R) for each A ∈GL2(R). For B ∈SL2(R), is ABA−1 ∈SL2(R)? Well,
det(ABA−1) = det(A) det(B) det(A−1) = det(A) det(B)
1
det A = det B = 1,
so ABA−1 ∈SL2(R).
Example 2.14. In Dn, ⟨r⟩is a normal subgroup since it has index 2 (Theorem 2.9), while ⟨s⟩=
{1, s} is not a normal subgroup of Dn since r⟨s⟩r−1 ̸⊂⟨s⟩:
rsr−1 = rrs = r2s ̸∈⟨s⟩.

<!-- page 4 -->
4
KEITH CONRAD
To prove a subgroup H of a group G is not normal, it suﬃces to show gHg−1 ̸⊂H for some
g ∈G, which means ghg−1 ̸∈H for some g ∈G and some h ∈H.2
Example 2.15. The subgroup Aﬀ(R) of GL2(R) is not normal, since ( 0 1
1 0 ) ∈GL2(R) and

0
1
1
0
 
a
b
0
1
 
0
1
1
0
−1
=

1
0
b
a

,
which is not in Aﬀ(R) if b ̸= 0 (and a is nonzero, say a = 1).
With Theorem 2.12 we can show a converse to Theorem 2.11 holds: if the rule (2.2) is well-
deﬁned then H must be a normal subgroup of G. Indeed, for g ∈G and h ∈H, hH = H = eH
and gH = gH, so having (2.2) be well-deﬁned at least requires hgH = egH, so hg ∈gH. Thus
g−1hg ∈H for all h ∈H and g ∈G. Since this is supposed to hold for all g, we can replace g with
g−1 to get ghg−1 ∈H for all h ∈H, so gHg−1 ⊂H for all g ∈G. Thus H ◁G by Theorem 2.12.
Remark 2.16. It is crucial in Theorem 2.12 that the quantiﬁcation runs over all g ∈G, since for
some H and g ∈G it can happen that gHg−1 ⊂H without having gHg−1 = H.3 For example,
let G = GL2(R) (or G = GL2(Q)) and H = {( 1 m
0 1 ) : m ∈Z}. Then H is a subgroup of G, and if
g = ( 2 0
0 1 ) then
g

1
m
0
1

g−1 =

2
0
0
1
 
1
m
0
1
 
2
0
0
1
−1
=

2
0
0
1
 
1
m
0
1
 
1/2
0
0
1

=

2
2m
0
1
 
1/2
0
0
1

=

1
2m
0
1

∈H
for all m ∈Z, so gHg−1 ⊂H, while
g−1

1
m
0
1

g =

1/2
0
0
1
 
1
m
0
1
 
2
0
0
1

=

1/2
m/a
0
1
 
2
0
0
1

=

1
m/2
0
1

,
which is not in H if m = 1, so g−1Hg ̸⊂H. Therefore gHg−1 ̸= H: the subgroup H of G is not a
normal subgroup.
More generally, if g = ( a 0
0 1 ) for an integer a ≥2 then
g

1
m
0
1

g−1 =

1
am
0
1

∈H
for all m ∈Z while
g−1

1
m
0
1

g =

1
m/a
0
1

2The property of a subgroup being normal is called its normality, not its normalcy, even though “normalcy” comes
from math: https://www.merriam-webster.com/words-at-play/did-warren-harding-coin-normalcy.
3This is impossible if H is ﬁnite, since then |gHg−1| = |H|, so a containment gHg−1 ⊂H forces equality.

<!-- page 5 -->
QUOTIENT GROUPS
5
is not in H if m = 1, so gHg−1 is a proper subset of H.
3. Quotient Groups
By Theorem 2.11, we can meaningfully multiply cosets of a normal subgroup N of a group G by
multiplying representatives for two cosets and passing to the coset of N the product lies in.
Deﬁnition 3.1. If N ◁G, deﬁne the product of two cosets g1N and g2N to be g1N ·g2N := g1g2N.
Nothing would change if we use right cosets of N because for a normal subgroup gN = Ng, so
the above deﬁnition is exactly the same thing as deﬁning Ng1 · Ng2 = Ng1g2.
Theorem 3.2. Using the above operation, the set of cosets of N in G is a group.
Proof. It is easy to see N is an identity for this operation on cosets of N:
N · gN = 1N · gN = 1gN = gN,
gN · N = gN = 1N = g1N = gN.
The inverse of gN is g−1N since their product in either order is the identity coset N:
gN · g−1N = gg−1N = 1N = N,
g−1N · gN = g−1gN = 1N = N.
Associativity of this multiplication on cosets follows from associativity of multiplication in G:
(gN · hN) · kN = ghN · kN = (gh)kN,
gN · (hN · kN) = gN · hkN = g(hk)N,
so from (gh)k = g(hk) we get (gh)kN = g(hk)N.
□
The collection of all cosets of a normal subgroup N of a group G is denoted G/N (and this is
pronounced “G mod N”). Its construction generalizes that of Z/(m): if G = Z and N = mZ then
Z/mZ under addition is exactly the same thing as congruence classes mod m under addition.
The group G/N is called the quotient group of G modulo N. Another term for G/N, which was
more widely used many years ago, is factor group (and that is still the standard term in some other
languages, e.g., Faktorgruppe in German.)4 While the collection of (left) cosets G/H = {gH : g ∈
G} for an arbitrary subgroup H in G is always a set, only when H is a normal subgroup does
G/H form a group using the rule (2.2), because if (2.2) is well-deﬁned then H must be a normal
subgroup of G.5 The name “quotient group” is explained at https://math.stackexchange.com/
questions/857539/who-named-quotient-groups and the following short theorem shows that the
size of G/N is related to quotients of integers when G is ﬁnite.
Theorem 3.3. If N ◁G with ﬁnite index then |G/N| = [G : N]. In particular, |G/N| = |G|/|N|
if G is ﬁnite.
Proof. The size of G/N is the number of cosets of N in G (left or right), which is [G : N]. If G is
ﬁnite and [G : N] = t, then t|N| = |G|, so |G/N| = t = |G|/|N|.
□
The notion of congruent integers in modular arithmetic carries over to all groups: in Z we say
a ≡b mod m when a −b ∈mZ, or equivalently when a = b + mk for some k ∈Z, so if N ◁G we
write g1 ≡g2 mod N when g1g−1
2
∈N, which is equivalent to g1 = ng2 = g2n′ for some n, n′ ∈N,
which is equivalent to g1N = g2N (we have g1g−1
2
∈N ⇔g1 ∈Ng2 = g2N ⇔g1N = g2N since
two cosets of N that overlap must be equal).
4Quotient groups were introduced by H¨older in 1889. He wrote G|N and called it a quotient of groups: see p. 31 in
https://eudml.org/doc/157433.
5If (2.2) is well-deﬁned then for all g ∈G and h ∈H, gH = ghH and g−1H = g−1H. Thus gg−1H = ghg−1H, so
H = ghg−1H. Thus ghg−1 ∈H for all g ∈G and h ∈H, so gHg−1 ⊂H for all g ∈G. Thus H ◁G by Theorem
2.12.

<!-- page 6 -->
6
KEITH CONRAD
As in Z/(m), where a denotes the congruence class a + mZ, we may write g for gN in G/N and
call g the reduction of g modulo N. In this notation, the group law in G/N is g1 g2 = g1g2 , with
identity 1 and g−1 = g−1. In additive notation, g1 + g2 = g1 + g2, the identity is 0, and −g = −g.
Theorem 3.4. Let G be a group and N ◁G. For g ∈G, g k = gk for all k ∈Z.
Proof. The case k ≥1 follows by induction. The case k = 0 is trivial. For k < 0, write k = −K
where K ≥1, so g K = gK. Then g k = g−K = (g K)−1 = gK−1 = (gK)−1 = g−K = gk.
□
Corollary 3.5. Let N ◁G and [G : N] < ∞. For each g ∈G, g[G:N] ∈N.
Proof. Let t = [G : N], so the group G/N has order t. For each g ∈G we have g t = 1 in G/N.
Therefore by Theorem 3.4, gt = 1, so gt ∈N.
□
Example 3.6. If G = Sn and N = An, so |G|/|N| = 2, the corollary says g2 ∈An for all g ∈Sn.
Indeed, whether or not g is an even or odd permutation, g2 is even since its sign is (±1)2 = 1.
Remark 3.7. In the setting of Corollary 3.5, the power map f : G →G where f(g) = g[G:N] has val-
ues in N, but it is not necessarily a homomorphism! Consider G = Sn and N = An, so [G : N] = 2.
The mapping Sn →Sn where σ 7→σ2 has values in An and is not a homomorphism when n ≥3 since
the squaring map on a group is a homomorphism if and only if the group is abelian: see Nonexample
5.2 in https://kconrad.math.uconn.edu/blurbs/grouptheory/homomorphisms.pdf. However,
if G is ﬁnite and N ⊂Z(G) then g 7→g[G:N] is a homomorphism from G to N: see https://math.
stackexchange.com/questions/842500.
When H is a non-normal subgroup of G with ﬁnite index, the conclusion of Corollary 3.5 with
H in place of N may have counterexamples: it need not be true that g|G|/|H| ∈H for all g ∈G.
For instance, if G = S3 and H = {(1), (12)}, so H ̸◁G and [G : H] = 3, then g3 ̸∈H if g is (13)
and (23).6
Theorem 3.8. Let G be a group and N ◁G.
(1) If G is abelian then G/N is abelian.
(2) If G is cyclic then G/N is cyclic.
Proof. (1) Pick two elements g and g′ of G/N. Then
g g′ = gg′,
g′ g = g′g,
Since G is commutative, gg′ = g′g in G, so gg′ = g′g in G/N. Thus g g′ = g′ g.
(2) Let G be cyclic with generator x, so every element of G has the form xk for some k ∈Z.
Thus every element of G/N is xk for some k ∈Z, and xk = x k by Theorem 3.4, so x is a generator
of G/N.
□
For the rest of this section we will look at some examples of quotient groups.
Example 3.9. Z/mZ: the quotient group Z/mZ is Z/(m), the integers modulo m under addition.
Example 3.10. R/2πZ: angles on the circle in radians are real numbers up to adding an integer
multiple of 2π. This is R/2πZ. For example, when we say “π = −π in radians” or “3π/2 = −π/2
in radians”, we are working with real numbers modulo 2πZ: in R/2πZ, π = −π and 3π/2 = −π/2.
In trigonometry you get used to adding angles while ignoring integer multiples of 2π, and that is
6If |G| is a prime power then g[G:H] ∈H for all subgroups H of G and all g ∈G, whether or not H ◁G. The key
term to look up is “subnormal subgroup.” All subgroups of a group of prime-power order are subnormal.

<!-- page 7 -->
QUOTIENT GROUPS
7
what addition and equality in R/2πZ are all about: a number in 2πZ is eﬀectively treated like 0.
Angles in degrees would be R/360Z under addition.
Example 3.11. R×/{±1}: when working with nonzero real numbers known only up to a sign, you
should be comfortable multiplying them while ignoring the sign: (±x)(±y) = ±xy where the signs
are chosen arbitrarily. For example if a = ±3 and b = ±5 for some unknown signs then deﬁnitely
ab = ±15. This type of multiplication up to a choice of sign is the same as working in R×/{±1},
since a coset of the subgroup {±1} in R× is {±x} = {x, −x} for x ∈R×.
So far our examples have been quotient groups of abelian groups, where every subgroup is normal.
Our remaining examples will be G/N where G is a nonabelian group.
Example 3.12. Sn/An: there are two cosets for An in Sn, namely (1) = (1)An = An (the even
permutations) and (12) = (12)An (the odd permutations). Therefore Sn/An = {(1), (12)}. The
group operation in Sn/An has (12) (12) = (12)(12) = (1). This group is cyclic of order 2.
Example 3.13. D8/Z(D8): the 16 elements of D8 are
1, r, r2, . . . , r7, s, rs, r2s, . . . , r7s
and the center Z(D8) is {1, r4}, with r−4 = r4. Let g = gZ(D8) = {g, r4g}. The size of D8/Z(D8)
is 16/2 = 8, and the cosets in D8/Z(D8) are
1 = {1, r4},
r = {r, r5},
r2 = {r2, r6},
r3 = {r3, r7},
s = {s, r4s},
rs = {rs, r5s},
r2s = {r2s, r6s},
r3s = {r3s, r7s}.
What does the group D8/Z(D8) look like?
Since r4 = r4 = 1 and smaller powers of r are not 1, r has order 4 in D8/Z(D8). The coset s is
not the identity since s ̸∈Z(D8) and s2 = s2 = 1, so s has order 2. Since rs = sr−1 in D8, we have
in D8/Z(D8)
r s = rs = sr−1 = s r−1 = s r−1,
so the multiplicative relations among r and s make D8/Z(D8) look like the group D4.
Example 3.14. GL2(R)/ SL2(R): ﬁrst we will show every coset has a unique representative of the
form ( δ 0
0 1 ) where δ ∈R×.
For A ∈GL2(R), let A be the coset A SL2(R) = {AB : B ∈SL2(R)} and set δ = det A. Then
( δ 0
0 1 ) has determinant δ too, so ( δ 0
0 1 )−1A has determinant (1/δ)δ = 1. Thus ( δ 0
0 1 )−1A ∈SL2(R),
so A ∈( δ 0
0 1 ) SL2(R). That shows A = ( δ 0
0 1 ), so each coset in GL2(R)/ SL2(R) is represented by a
matrix of the form ( δ 0
0 1 ). This δ is unique: if

δ
0
0
1

=

δ′
0
0
1

then ( δ 0
0 1 ) = ( δ′ 0
0 1 )B with det B = 1, so taking determinants of both sides implies δ = δ′ det B = δ′.
Having shown the matrices ( δ 0
0 1 ) represent the cosets in GL2(R)/ SL2(R), the multiplicative rule
( δ 0
0 1 )( δ′ 0
0 1 ) = ( δδ′ 0
0 1 ) for matrices implies the rule ( δ 0
0 1 ) · ( δ′ 0
0 1 ) = ( δδ′ 0
0 1 ) for cosets, so the quotient
group GL2(R)/ SL2(R) resembles the group R× under multiplication.
Example 3.15. GL2(Z/(m))/ SL2(Z/(m)): reasoning like in the previous example, with R× re-
placed by (Z/(m))×, each coset in GL2(Z/(m))/ SL2(Z/(m)) has a unique representative of the form
( δ 0
0 1 ) with δ ∈(Z/(m))×, and the quotient group GL2(Z/(m))/ SL2(Z/(m)) resembles (Z/(m))×
under multiplication.

<!-- page 8 -->
8
KEITH CONRAD
Don’t confuse quotient groups and subgroups! Even though the elements of Z/mZ have repre-
sentatives in Z, such as {0, 1, . . . , m −1}, the group Z/mZ is not a subgroup of Z: elements of
Z/mZ have ﬁnite order while nonzero elements of Z do not. For example, {0, 1, . . . , m −1} for
m ≥2 is not closed under addition, so this set of integers is in no way a subgroup of Z. Subgroups
are inside a group while quotient groups are a type of collapsing of a group, generalizing the way
R can be wrapped around to form the circle group R/2πZ.
4. Orders of elements in a quotient group
Let’s compare the order of an element in G to its order in G/N. To say g in G/N has order k
means gk = 1 and no smaller power has that property. In terms of G itself, this is saying gk ∈N
and k is the smallest positive integer with that property. Passing from G to G/N, the order of an
element can drop: from inﬁnite to ﬁnite or from ﬁnite to a smaller ﬁnite value.
Example 4.1. In the additive group Z, 1 has inﬁnite order while in Z/6Z, 1 = 1+ 6Z has order 6.
Example 4.2. In the quaternion group Q8, the subgroup {±1} is normal (it is the center of Q8)7.
The order of i in Q8 is 4 and the order of i in Q8/{±1} is 2 since i2 = −1 = 1 and i ̸= 1.
Example 4.3. For n ≥3, the n-cycle (12 . . . n) has order n in Sn, while its reduction in Sn/An has
order 1 or 2 since Sn/An is a group of order 2. For a permutation σ ∈Sn, the reduction σ = σAn
in Sn/An is trivial if σ is even and nontrivial if σ is odd, so σ has order 1 if σ is even and order 2
if σ is odd.
Example 4.4. Let G = Z/20Z and N = 10Z/20Z.
Then G is cyclic of order 20 and N =
{0, 10 mod 20} is a normal subgroup of order 2 (all subgroups of a cyclic group are normal). The
quotient group G/N is a cyclic group of order 20/2 = 10 by Theorem 3.8 and its proof shows each
generator of G reduces in G/N to a generator of G/N. For example, 1 mod 20 has order 20 in G,
while in G/N, 1 mod 20 has order 10. An element’s order dropped from 20 to 10 when we pass
from G to G/N. The order of 5 mod 20 in G is 4, while the order of 5 mod 20 in G/N is 2. The
order of 4 mod 20 in G and the order of 4 mod 20 in G/N are both 5.
Theorem 4.5. If G is a group with a normal subgroup N and g in G has ﬁnite order m, then the
order of g in G/N is a factor of m.
Proof. In G we have gm = 1, so in G/N we have gm = (gN)m = gmN = N = 1. Therefore g has
order dividing m.
□
If g in G/N has ﬁnite order k, then Theorem 4.5 tells us each coset representative of g in G has
order divisible by k (if the representative has ﬁnite order, e.g., if G is ﬁnite). There may or may
not be a representative of g with order k.
Example 4.6. Let G = Z/12Z = {0, 1, . . . 11 mod 12} and N = 2Z/12Z = {0, 2, 4, 6, 8, 10 mod 12}.
In G/N, 1 mod 12 has order 2 and its coset representatives in G are {1, 3, 5, 7, 9, 11 mod 12}, where
the representatives have order 12, 4, 12, 12, 4, and 12: no coset representative has order 2.
Example 4.7. In Q8/{±1} the element i has order 2 and its coset representatives in Q8 are ±i,
which both have order 4.
7In fact every subgroup of Q8 is a normal subgroup, even though Q8 is not abelian.

<!-- page 9 -->
QUOTIENT GROUPS
9
Example 4.8. In (Z/35Z)×, which has size 24, 11 mod 35 has order 3: ⟨11⟩= {1, 11, 16 mod 35}.
In (Z/35Z)× the order of 2 is 12, and the order of 2 drops from 12 to 4 when we pass to the
quotient group (Z/35Z)×/⟨11⟩, since the least positive power of 2 mod 35 that is inside ⟨11⟩=
{1, 11, 16 mod 35} is 24.
Corollary 4.9. If G is a ﬁnite group with a normal subgroup N such that the order |N| and index
[G : N] are relatively prime, then N is the only subgroup of G having its size: if H is a subgroup
of G such that |H| = |N| then H = N.
Proof. Let |N| = n. For h ∈H we have hn = 1 since |H| = n. In the quotient group G/N we get
h
n = 1, so the order of h divides n. Also the order of h divides |G/N|, so from (|N|, |G/N|) = 1
we get h = 1 in G/N. Thus h ∈N. This holds for all h ∈H, so H ⊂N, and thus H = N because
|H| = |N|.
□
Remark 4.10. This corollary does not say a subgroup with relatively prime order and index is
the only subgroup of its size, but rather that a normal subgroup with relatively prime order and
index is unique for its size. For instance, when G = S3, the subgroup A3 is normal in G and is the
only subgroup of its size (order is 3, index is 2), but {(1), (12)} is not normal in G and is not the
only subgroup of its size (order is 2, index is 3).
Although the order of g in a quotient group G/N might not “lift” to the order of some coset
representative of g in G, the next theorem shows the property of having p-power order (but not a
speciﬁc p-power order) can be lifted from G/N to G when G is ﬁnite.
Theorem 4.11. If G is a ﬁnite group, N ◁G, and g has p-power order in G/N for a prime p,
then some coset representative for g has p-power order in G.
Proof. Let g have order pr in G/N and g have order m in G, so pr | m by Theorem 4.5. Write
m = psn where p ∤n, so r ≤s. We will show g = ab where a and b are powers of g such that
aps = 1 and b ∈N with bn = 1, so g = a and a has p-power order.
Since ps and n are relatively prime, we can write 1 = psx + ny for some integers x and y. Then
g = g1 = gpsxgny = gnygpsx
where a := gny satisﬁes aps = gpsny = gmy = 1 and b := gpsx satisﬁes bn = gpsnx = gmx = 1. Since
r ≤s and gpr = 1, we have gps = 1, so gps ∈N. Thus b = gpsx ∈N, so g = ab ⇒g = a in G/N
with a having order dividing ps, which means a has p-power order.
□
In this proof, it turns out that a has order ps and b has order n. This is explained by Theorem
6.1 in https://kconrad.math.uconn.edu/blurbs/grouptheory/order.pdf, which shows a and
b are the unique commuting elements of G with orders ps and n that have product g.
Example 4.12. Let G = Z/90Z and N = 15Z/90Z, so G/N ∼= Z/15Z.
• In G/N, 5 has (additive) order 3 while in G, 5 has order 18 but 5 = 20 in G/N and 20 in
G has order 9.
• In G/N, 6 has (additive) order 5 while in G, 6 has order 30 but 6 = 36 in G/N and 36 in
G has order 5.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*