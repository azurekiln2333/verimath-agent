# Universal Mapping Properties

> **Source**: https://kconrad.math.uconn.edu/blurbs/universalmapping.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
UNIVERSAL MAPPING PROPERTIES
KEITH CONRAD
The construction of a new algebraic object from old ones is often deﬁned by formulas
for the elements of the new object and operations in it. Two examples are quotient groups
G/N and product groups G1 × G2: G/N consists of cosets gN multiplied by the rule
gN · g′N = gg′N and G1 × G2 consists of ordered pairs (g1, g2) with gi ∈Gi and operations
deﬁned componentwise.
There is another way to describe such constructions: say how the new object is related (by
mappings) to all other objects of a similar type. This lets us characterize a new object up
to a unique isomorphism. Studying mathematical objects by their interactions with similar
objects, rather than by an explicit construction of the object, is analogous to studying
elementary particles by smashing them together (except math is much less expensive). Our
examples will be from group theory, ring theory, and module theory.
• Group theory: cyclic groups, quotient groups, abelianizations, direct products
• Ring theory: quotient ring, direct product, fraction ﬁeld
• Module theory: cyclic modules, quotient modules, direct products, direct sums, and
free modules.
In an appendix we discuss the universal mapping property for the product topology,
quotient topology, and completion of a metric space.
1. Cyclic groups
Fix n ≥1. All cyclic groups of order n (e.g. Z/nZ and µn) are isomorphic, but not
uniquely: the isomorphism depends on a choice of generator in each group. Changing the
generator of either group changes the isomorphism between the groups.
Example 1.1. The groups µ10 and (Z/11Z)× are both cyclic of order 10. A generator of
µ10 is ζ = e2πi/10. The generators of (Z/11Z)× are 2, 6, 7, and 8, and each choice leads to
a diﬀerent isomorphism µ10 →(Z/11Z)×:
f1(ζa) = 2a mod 11,
f2(ζa) = 6a mod 11,
f3(ζa) = 7a mod 11,
f4(ζa) = 8a mod 11.
Theorem 1.2. Let C be a cyclic group of order n with generator c.
(1) For each group G and γ ∈G such that γn = 1, there is a unique homomorphism
f : C →G such that f(c) = γ.
(2) If G is cyclic of order n and γ in G has order n then f in (1) is an isomorphism.
Saying γn = 1 means γ has order dividing n, not order equal to n. Perhaps γ = 1.
Proof. Since each element of C is a power of c, a homomorphism C →G is completely
determined by its value on c. If f : C →G is a homomorphism such that f(c) = γ, then
f(cj) = γj for all j. This formula is a group homomorphism:
• the deﬁnition of f(cj) makes sense, since cj = cj′ ⇒j ≡j′ mod n (c has order n),
which implies γj = γj′ (since γn = 1),
1

<!-- page 2 -->
2
KEITH CONRAD
• f is a homomorphism since all elements of C are powers of c and f(cjck) = f(cj+k) =
γj+k = γjγk = f(cj)f(ck).
If G is cyclic of order n and γ has order n then f(C) = ⟨f(c)⟩= ⟨γ⟩= G, so f is
surjective. A surjective homomorphism of two ﬁnite groups of equal order is injective, so f
is an isomorphism.
□
This theorem is telling us that by including the choice of generator of C as part of the
data we keep track of, we rigidiﬁed the situation: there is exactly one homomorphism. Let’s
consider all pairs (G, γ) where G is a group and γ is an element of G such that γn = 1.
Deﬁnition 1.3. A pair (G, γ) where γn = 1 is called an n-marked group. If G is cyclic of
order n and γ generates G then (G, γ) is called a cyclic n-marked group.
Example 1.4. Some n-marked groups are (Z/nZ, a) for each a ∈Z/nZ, (C×, ζ) where ζ is
an nth root of unity in C, and (G, e), for arbitrary G. When n = 4, (S5, (12)) is an example.
If (G, γ) is an n-marked group, so is (G, γa) for each integer a, since (γa)n = (γn)a = 1.
The n-marked group (Z/nZ, a) is a cyclic n-marked group only when (a, n) = 1 because
that is when a generates Z/nZ.
Deﬁnition 1.5. A morphism of n-marked groups f : (G1, γ1) →(G2, γ2) is a group homo-
morphism f : G1 →G2 such that f(γ1) = γ2.
Example 1.6. For each n-marked group (G, γ), the identity mapping id: G →G gives us
a morphism (G, γ) →(G, γ).
Example 1.7. For the 4-marked groups (µ4, i) and (R×, −1), the mapping f : (µ4, i) →
(R×, −1) where f(ik) = (−1)k is a morphism. There is no morphism in the other direction
(R×, −1) →(µ4, i) since it would be a homomorphism R× →µ4 mapping −1 to i and a
group homomorphism can’t send an element of order 2 to an element of order 4. (There
are homomorphisms R× →µ4, such as x 7→sign(x), or the trivial homomorphism x 7→1,
but there is none sending −1 to i.)
Example 1.8. A composition of morphisms is a morphism: if f1 : (G1, γ1) →(G2, γ2) and
f2 : (G2, γ2) →(G3, γ3) are morphisms then f2 ◦f1 : G1 →G3 is a group homomorphism
such that (f2◦f1)(γ1) = f2(f1(γ1)) = f2(γ2) = γ3, so we have a morphism f2◦f1 : (G1, γ1) →
(G3, γ3).
Using this new terminology of morphisms of n-marked groups, we can express the ﬁrst
part of Theorem 1.2 as follows. If (C, c) is a cyclic n-marked group then
for every n-marked group (G, γ), there is a unique morphism (C, c) →(G, γ).
That we can map a cyclic n-marked group (C, c) to each n-marked group in exactly one
way (by a morphism, not a random function) is called the universal mapping property of
cyclic n-marked groups (cyclic groups of order n with a choice of generator). The term
“universal” refers to (C, c) being related to every n-marked group.
Example 1.9. If (C, c) is a cyclic n-marked group then the unique morphism (C, c) →(C, c)
is the identity mapping on C. In concrete terms, this is saying that a homomorphism C →C
that ﬁxes c has to ﬁx all powers of c and thus ﬁxes all of C since C = ⟨c⟩.
Now we reach a key point: two n-marked groups satisfying the universal mapping prop-
erty above are isomorphic in a unique way respecting their chosen elements of order n.

<!-- page 3 -->
UNIVERSAL MAPPING PROPERTIES
3
Theorem 1.10. If (A, a) and (B, b) are n-marked groups that satisfy the universal mapping
property of cyclic n-marked groups then the unique morphism (A, a) →(B, b) is a group
isomorphism A →B sending a to b.
Proof. Pay close attention to this argument. It makes no use of the group structure of A
or B. The uniqueness aspect of the universal mapping property is all we need to rely on.
By the universal mapping property of cyclic n-marked groups, there are unique mor-
phisms f : (A, a) →(B, b) and f′ : (B, b) →(A, a). The compositions f′ ◦f : (A, a) →(A, a)
and f ◦f′ : (B, b) →(B, b) are morphisms (Example 1.8). The identity morphisms (A, a) →
(A, a) and (B, b) →(B, b) also exist (Example 1.9), so by uniqueness f′ ◦f = idA and
f ◦f′ = idB.
□
Since we know cyclic n-marked groups (C, c) really exist and they satisfy the universal
mapping property of cyclic n-marked groups, the isomorphism in Theorem 1.10 tells us
that every n-marked group (A, a) satisfying the universal mapping property of cyclic n-
marked group has A cyclic of order n and ⟨a⟩= A. Bare cyclic groups of order n are not
characterized by a universal mapping property. Cyclic groups of order n together with a
choice of generator (i.e., cyclic n-marked groups of order n) are being characterized.
Deﬁnition 1.11. An isomorphism of n-marked groups f : (G1, γ1) →(G2, γ2) is a mor-
phism (G1, γ1) →(G2, γ2) that is bijective as a function from G1 to G2.
This means f : G1 →G2 is a group isomorphism and f(γ1) = γ2. The inverse isomor-
phism f−1 is an isomorphism (G2, γ2) →(G1, γ1) since it is bijective and f−1(γ2) = γ1.
Using this terminology, two cyclic n-marked groups have a unique isomorphism between
them. This is often expressed by saying a cyclic n-marked group is “unique up to unique
isomorphism” and it is a fancy way of expressing the second part of Theorem 1.2.
2. Quotient groups
We turn now to quotient groups. Fix a group G and normal subgroup N ◁G. The
reduction homomorphism πN : G →G/N that sends g to gN has kernel N. An important
property of G/N with πN is: when G
f
−−→eG is a homomorphism from G to an arbitrary
group eG such that f is trivial on N (N ⊂ker f), there is a unique homomorphism f : G/N →
eG making the following diagram commute (“f factors through the quotient”).
G
f
/
πN
!
eG
G/N
f
=
The reason f is unique is that commutativity says f(gN) = f(g) for all g ∈G and every
element of G/N is some gN, so f is completely determined.
It is useful to rotate the above diagram to put πN and f on a more equal footing.
(2.1)
G
πN
}
f

G/N
f
/ eG

<!-- page 4 -->
4
KEITH CONRAD
Think of f in (2.1) as sending the pair (G/N, πN) to the pair ( eG, f).
Deﬁnition 2.1. An N-trivial group is a pair ( eG, f) where eG is a group and f : G →eG is
a homomorphism from G to eG that is trivial on N.
One example of an N-trivial group is (G/N, πN). Another is ( eG, f) for arbitrary eG and
f : G →eG being the trivial homomorphism that sends all of G to the identity in eG. Note
the group G in which N is a normal subgroup is part of the deﬁnition of an N-trivial group!
Deﬁnition 2.2. For two N-trivial groups (G1, f1) and (G2, f2), a morphism from the ﬁrst
to the second is a homomorphism G1
h
−−→G2 such that the following diagram commutes.
G
f2
 
f1
~
G1
h
/ G2
We call this morphism h an isomorphism if it is an isomorphism from G1 to G2.
Example 2.3. For an N-trivial group ( eG, f), the identity mapping on eG deﬁnes a morphism
G
f

f

eG
id
/ eG
and we call this the identity morphism of ( eG, f). This is an analogue of Example 1.6.
Example 2.4. The composition of two morphisms is a morphism: if h1 : (G1, f1) →(G2, f2)
and h2 : (G2, f2) →(G3, f3) are morphisms of N-trivial groups then in the left diagram
G
f1
}
f2

f3
!
G1
h1
/ G2
h2
/ G3
G
f1
~
f3
 
G1
h2◦h1
/ G3
the left triangle and right triangle commute, so the big triangle commutes:
(h2 ◦h1) ◦f1 = h2 ◦(h1 ◦f1) = h2 ◦f2 = f3.
Thus the diagram on the right, where the middle arrow has been removed, is commutative,
so h2 ◦h1 : (G1, f1) →(G3, f3) is a morphism. This is an analogue of Example 1.8.
The uniqueness of f ﬁtting in (2.1) is called the universal mapping property of G/N
(really, of G/N together with πN : G →G/N). This refers to the following property.
Deﬁnition 2.5. An N-trivial group (U, ϕ) is called universal if for each N-trivial group
( eG, f), there is a unique morphism (U, ϕ) →( eG, f): there is a unique homomorphism
U →eG making the following diagram commute.
G
ϕ

f

U
/ eG

<!-- page 5 -->
UNIVERSAL MAPPING PROPERTIES
5
One universal N-trivial group is (G/N, πN). Let’s show all others are isomorphic to it.
Theorem 2.6. If (U1, ϕ1) and (U2, ϕ2) are universal N-trivial groups then there is a unique
morphism (U1, ϕ1) →(U2, ϕ2) and it is an isomorphism.
Proof. Since (U1, ϕ1) and (U2, ϕ2) are universal N-trivial groups, there is a unique morphism
from each to the other: we have commutative diagrams
G
ϕ1
~
ϕ2
 
U1
h
/ U2
G
ϕ2
~
ϕ1
 
U2
k
/ U1
for unique group homomorphisms h and k. We’ll show h and k are inverses, so in fact they
are group isomorphisms. Put the diagrams above together in two ways to get new diagrams.
G
ϕ1
~
ϕ2

ϕ1
 
U1
h
/ U2
k
/ U1
G
ϕ2
~
ϕ1

ϕ2
 
U2
k
/ U1
h
/ U2
In these diagrams the smaller triangles commute, so the big ones commute. For example,
(k ◦h) ◦ϕ1 = k ◦(h ◦ϕ1) = k ◦ϕ2 = ϕ1.
Now remove the middle parts of the diagrams to get the following commutative diagrams.
G
ϕ1
~
ϕ1
 
U1
k◦h
/ U1
G
ϕ2
~
ϕ2
 
U2
h◦k
/ U2
Since (U1, ϕ1) is a universal N-trivial group, only one homomorphism can appear where k◦h
does in the ﬁrst commutative diagram. Since idU1 ﬁts, k ◦h = idU1. Similarly, h ◦k = idU2
by the second commutative diagram and (U2, ϕ2) being a universal N-trivial group. Thus
U1 ∼= U2 by inverse group isomorphisms h and k.
U1
h
4 U2
k
t
□
Here is a “practical” use of universal N-trivial groups being isomorphic to each other.
Theorem 2.7. For a group G, let N and N′ be normal subgroups such that N′ ⊂N ⊂G.
Then (G/N′)/(N/N′) ∼= G/N as groups.
Proof. The composition G
πN′
−−−→G/N′
π
−−→(G/N′)/(N/N′), where πN′ and π are reduction
maps, is a homomorphism trivial on N, so ((G/N′)/(N/N′), π ◦πN′) is an N-trivial group.
We’ll show this N-trivial group is universal.
Then, since (G/N, πN) is also a universal
N-trivial group, (G/N′)/(N/N′) ∼= G/N by Theorem 2.6.

<!-- page 6 -->
6
KEITH CONRAD
Let G
f
−−→eG be a homomorphism that is trivial on N. Since N′ ⊂N, f is trivial on N′,
so there is a unique homomorphism f′ : G/N′ →eG making the following diagram commute.
G
πN′
}
f

G/N′
f′
/ eG
The mapping f′ is trivial on N/N′ since f′(nN′) = f′(πN′(n)) = f(n), which is trivial. So
a unique homomorphism f′′ : (G/N′)/(N/N′) →eG makes the following diagram commute,
where π is a reduction map.
G/N′
π
w
f′
!
(G/N′)/(N/N′)
f′′
/ eG
Sticking these diagrams together creates the following larger commutative diagram on the
left, which we simplify on the right by removing anything directly involving G/N′.
G
πN′
|
f

G/N′
π
w
f′
!
(G/N′)/(N/N′)
f′′
/ eG
G
π◦πN′
z
f

(G/N′)/(N/N′)
f′′
/ eG
Therefore to each N-trivial group ( eG, f) there is a homomorphism f′′ : (G/N′)/(N/N′) →eG
such that f′′ ◦(π ◦πN′) = f. This means, for each g ∈G, that
f(g) = f′′((π ◦πN′)(g)) = f′′(π(gN′)) = f′′(gN/N′),
where g = gN′. Each element of (G/N′)/(N/N′) is gN/N′ for some g, so f′′ is determined
by ﬁtting in the commutative diagram on the right. Thus f′′ is the only homomorphism such
that f′′ ◦(π ◦πN′) = f, making the N-trivial group ((G/N′)/(N/N′), π ◦πN′) universal.
□
Remark 2.8. Since ((G/N′)/(N/N′), π ◦πN′) and (G/N, πN) are both universal N-trivial
groups, there is a unique isomomorphism h: (G/N′)/(N/N′) →G/N making the diagram
G
π◦πN′
x
πN
!
(G/N′)/(N/N′)
h
/ G/N
commute, by Theorem 2.6. Commutativity means, for each g ∈G, that
h((π ◦πN′)(g)) = πN(g) =⇒h(π(gN′)) = gN =⇒h(gN/N′) = gN ,

<!-- page 7 -->
UNIVERSAL MAPPING PROPERTIES
7
where g = gN′. The formula in the box is the isomorphism (G/N′)/(N/N′) →G/N seen
in an algebra course where these groups are proved isomorphic as part of the isomorphism
theorems for groups without mentioning universal mapping properties.
A way to think about the isomorphism h: (U1, ϕ1) →(U2, ϕ2) between two universal
N-trivial groups is that the commutativity of
G
ϕ1
~
ϕ2
 
U1
h
/ U2
makes the isomorphism h “turn” ϕ1 into ϕ2. For example, since (G/N, πN) is a universal
N-trivial group and (i) ker πN = N (not just N ⊂ker πN) and (ii) πN(G) = G/N, every
universal N-trivial group (U, ϕ) has similar properties: ker ϕ = N and ϕ(G) = U. Indeed,
letting h: (G/N, πN) →(U, ϕ) be the (unique) isomorphism between them, so h ◦πN = ϕ,
we have
ϕ(g) = 1 =⇒h(πN(g)) = 1 =⇒πN(g) = 1 =⇒g ∈N
since h is injective, so N ⊂ker ϕ ⊂N. Thus ker ϕ = N. Also
ϕ(G) = h(πN(G)) = h(G/N) = U
since h and πN are surjective. So ϕ: G →U is onto with kernel N, just like πN : G →G/N.
This way of proving a universal N-trivial group (U, ϕ) has ker ϕ = N and ϕ(G) = U uses
our knowledge of these properties for the particular universal N-trivial group (G/N, πN).
It turns out that these two properties can be shown without knowing a speciﬁc construction
of a universal N-trivial group: it follows purely from reasoning based on the deﬁnition of a
universal N-trivial group and its uniqueness up to unique isomorphism, as we now show.
Theorem 2.9. If (U, ϕ) is a universal N-trivial group then ker ϕ = N.
Proof. By the deﬁnition of an N-trivial group, ϕ is trivial on N, so N ⊂ker ϕ. We want to
get the reverse containment: ker ϕ ⊂N, so ker ϕ = N.
For every N-trivial group ( eG, f), there is a (unique) homomorphism h: U →eG such that
the following diagram commutes.
G
ϕ

f

U
h
/ eG
From this commutativity, if g ∈ker ϕ then f(g) = h(ϕ(g)) = h(1) = 1 (all homomorphisms
are trivial on the identity element), so g ∈ker f. Thus ker ϕ ⊂ker f for every N-trivial
group ( eG, f). A particular N-trivial group is (G/N, πN), for which ker πN = N, so ker ϕ ⊂
N. Thus ker ϕ = N.1
□
Theorem 2.10. If (U, ϕ) is a universal N-trivial group then ϕ(G) = U.
1This proof used G/N and the reduction map πN : G →G/N, but it did not rely on knowing (G/N, πN)
is a universal N-trivial group.

<!-- page 8 -->
8
KEITH CONRAD
Proof. The image ϕ(G) is a subgroup of U. We want to show ϕ(G) = U. We will not use
quotient groups in any way at all.
Since ϕ: G →U is a homomorphism, so is G →ϕ(G) also given by g 7→ϕ(g). Call this
map ϕ′, so ϕ′ : G →ϕ(G) is ϕ with the target restricted to ϕ(G). Since ϕ′ is trivial on N,
(ϕ(G), ϕ′) is an N-trivial group.
Step 1. (ϕ(G), ϕ′) is a universal N-trivial group.
For each N-trivial group ( eG, f), we want a unique morphism (ϕ(G), ϕ′) →( eG, f).
Existence of a morphism (ϕ(G), ϕ′) →( eG, f). Since (U, ϕ) is a universal N-trivial group
there is a unique homomorphism U
h
−−→eG making the following diagram commute.
G
ϕ

f

U
h
/ eG
The deﬁnition of ϕ(G) and ϕ′ : G →ϕ(G) give us the following commutative diagram,
where “incl.” is inclusion.
G
ϕ′
}
ϕ

ϕ(G)
incl.
/ U
Stick these diagrams together to get the following commutative diagram.
G
ϕ′
}
ϕ

f

ϕ(G) incl.
/ U
h
/ eG
Thus h ◦incl. is a morphism (ϕ(G), ϕ′) →( eG, f) (Example 2.4).
Uniqueness of a morphism (ϕ(G), ϕ′) →( eG, f). If k is such a morphism then k(ϕ′(g)) =
f(g), so k(ϕ(g)) = f(g) for g ∈G. The last formula shows k is determined as a function on
ϕ(G), so the morphism k is unique.
Step 2. ϕ(G) = U, so ϕ is surjective.
By Step 1, (ϕ(G), ϕ′) is a universal N-trivial group, so Theorem 2.6 tells us that there is
an isomorphism ψ: (ϕ(G), ϕ′) →(U, ϕ), which means the following diagram commutes.
G
ϕ′
}
ϕ

ϕ(G)
ψ
/ U
We know ψ is surjective since it is a group isomorphism and ϕ′ is surjective by its deﬁnition,
so ϕ = ψ ◦ϕ′ is surjective. Thus U = ϕ(G).
□
3. The abelianization of a group
The commutator subgroup [G, G] is the subgroup of G generated by all commutators
[x, y] := xyx−1y−1
for x, y ∈G.

<!-- page 9 -->
UNIVERSAL MAPPING PROPERTIES
9
Since [x, y]−1 = [y, x], [G, G] is the set of all ﬁnite products of commutators. (Note: in many
groups G, each element of [G, G] is a commutator, but in general a product of commutators
need not be a commutator, so [G, G] can be larger than the set of commutators.2) What
makes [G, G] important? We’ll give two answers, as Theorems 3.2 and 3.4.
Lemma 3.1. The subgroup [G, G] is normal in G,
Proof. In G, conjugation by a ﬁxed element (h 7→ghg−1) is an automorphism, so it sends
commutators to commutators and products of commutators to products of commutators:
g[x, y]g−1 = g(xyx−1y−1)g−1
= gxg−1 · gyg−1 · (gxg−1)−1 · (gyg−1)−1
= [gxg−1, gyg−1]
and therefore
g[x1, y1] · · · [xn, yn]g−1 = g[x1, y1]g−1 · · · g[xn, yn]g−1
= [gx1g−1, gy1g−1] · · · [gxng−1, gyng−1].
Therefore g[G, G]g−1 ⊂[G, G] for all g ∈G, so [G, G] ◁G.
□
Theorem 3.2. The group G/[G, G] is abelian, and G/N is abelian if and only if [G, G] ⊂N.
Proof. Commutators in G become trivial in G/[G, G], so reducing the equation xy = [x, y]yx
modulo [G, G] tells us x y = y x for all x and y in G, so G/[G, G] is abelian.
If G/N is abelian then for all x and y in G, x y = y x in G/N, so [x, y] = 1 in G/N, or in
other words [x, y] ∈N. A subgroup containing all commutators must contain the subgroup
they generate, so [G, G] ⊂N. Another way to say this is that the homomorphism πN : G →
G/N is trivial on commutators since commutators go to commutators by a homomorphism
and G/N is abelian, so [x, y] ∈ker πN = N for all x, y ∈G. Thus [G, G] ⊂N.
□
Since abelian quotients G/N have [G, G] ⊂N, G/N ∼= (G/[G, G])/(N/[G, G]), so G/[G, G]
is an abelian quotient of G that explains all others (every quotient group of an abelian group
is abelian). We can also say G/[G, G] is the largest abelian quotient of G since working
modulo [G, G] trivializes the least amount of G to get an abelian quotient of G.
Deﬁnition 3.3. For a group G, its quotient G/[G, G] is called the abelianization of G.
Rather than explain the role of [G, G] in terms of its relation to all abelian quotient groups
of G, the following theorem gives a relation to homomorphisms from G to all abelian groups.
Theorem 3.4. If f : G →A is a homomorphism from G to an abelian group A then there
is a unique homomorphism f : G/[G, G] →A making the following diagram commute, where
π: G →G/[G, G] is the reduction map.
G
f
/
π
$
A
G/[G, G]
f
:
2See https://kconrad.math.uconn.edu/blurbs/grouptheory/noncommutatorSL2.pdf.

<!-- page 10 -->
10
KEITH CONRAD
Proof. If we have a group homomorphism f : G −→A where A is abelian, then f is trivial
on commutators: in A:
f(xyx−1y−1) = f(x)f(y)f(x)−1f(y)−1 = 1.
Therefore [x, y] ∈ker f for all x, y ∈G, so [G, G] ⊂ker f. That means we get an induced
homomorphism f : G/[G, G] →A where f(g[G, G]) = f(g) for all g ∈G. This is the unique
homomorphism ﬁtting into the commutative diagram in the theorem: if the diagram
G
f
/
π
$
A
G/[G, G]
h
:
commutes for some homomorphism h: G/[G, G] →A then for each g ∈G,
h(g) = h(π(g)) = f(g),
so h = f.
□
Rotating the commutative diagram in the statement of Theorem 3.4 to be
G
π
z
f

G/[G, G]
f
/ A
suggests thinking about the situation like this: reduction π: G →G/[G, G] is one homo-
morphism from G to an abelian group and all other homomorphisms f : G →A for abelian
A are explained by composing π with homomorphisms f from G/[G, G] to abelian groups:
Theorem 3.4 shows f and f determine each other.
To turn this into a universal mapping property, ﬁx the group G and consider as objects
of study all homomorphisms G
f
−−→A where the varying group A is abelian. We won’t
make up a name for these as before with “n-marked groups” and “N-trivial groups”.
Example 3.5. Reduction G
π
−−→G/[G, G] from G to its abelianization is such an object.
Deﬁnition 3.6. Given two such objects G
f1
−−→A1 and G
f2
−−→A2, a morphism from the
ﬁrst to the second is a group homomorphism A1
h
−−→A2 such that the following diagram
commutes.
G
f2
 
f1
~
A1
h
/ A2
We call h an isomorphism if it is an isomorphism from A1 to A2.
Example 3.7. For each G
f
−−→A we have the identity morphism of this object to itself.
G
f

f

A
id
/ A

<!-- page 11 -->
UNIVERSAL MAPPING PROPERTIES
11
Example 3.8. For morphisms h1 and h2 in the commutative diagrams below the target
G
f1
~
f2
 
A1
h1
/ A2
G
f2
~
f3
 
A2
h2
/ A3
G
f2
−−→A2 of h1 is the source of h2, so we can compose them by sticking the diagrams
together to get a larger commutative diagram and then ignoring the middle arrow just as
in Example 2.4.
G
f1
}
f2

f3
!
A1
h1
/ A2 h2
/ A3
G
f1
~
f3
 
A1
h2◦h1
/ A3
Deﬁnition 3.9. Among all homomorphisms from G to abelian groups, say G
ϕ
−−→U is
universal if for each G
f
−−→A there is a unique homomorphism U →A making the following
diagram commute,
G
ϕ

f

U
/ A
Equivalently, a universal object has a unique morphism to all other such objects.
Example 3.10. Reduction G
π
−−→G/[G, G] to the abelianization of G is a universal object
by Theorem 3.4. Rotate the diagram in that theorem to make it resemble the diagram
above (U = G/[G, G], ϕ = π). We say G/[G, G], which really means G
π
−−→G/[G, G], is
“universal for homomorphisms from G to abelian groups.”
Theorem 3.11. If (U1, ϕ1) and (U2, ϕ2) are universal objects in the sense of Deﬁnition
3.9, then there is a unique morphism (U1, ϕ1) →(U2, ϕ2) and it is an isomorphism.
Proof. This is the same proof as that of Theorem 2.6.
Since (U1, ϕ1) and (U2, ϕ2) are
universal, we have commutative diagrams
G
ϕ1
~
ϕ2
 
U1
h
/ U2
G
ϕ2
~
ϕ1
 
U2
k
/ U1
for unique group homomorphisms h and k. Compose h and k in both orders to get new
diagrams.
G
ϕ1
~
ϕ2

ϕ1
 
U1
h
/ U2
k
/ U1
G
ϕ2
~
ϕ1

ϕ2
 
U2
k
/ U1
h
/ U2

<!-- page 12 -->
12
KEITH CONRAD
Since the smaller triangles in each diagram commute, so do the big triangles, Removing the
middle parts of the diagrams gives us the following commutative diagrams.
G
ϕ1
~
ϕ1
 
U1
k◦h
/ U1
G
ϕ2
~
ϕ2
 
U2
h◦k
/ U2
Since (U1, ϕ1) is universal, only one homomorphism can be appear where k ◦h does in the
ﬁrst commutative diagram. Since idU1 ﬁts, k ◦h = idU1. Similarly, h ◦k = idU2 by the
second commutative diagram and (U2, ϕ2) being universal. Therefore h and k are inverse
isomorphisms between U1 and U2.
□
Since G
π
−−→G/[G, G] is a “universal homomorphism from G to abelian groups,” all
other universal objects G
ϕ
−−→U are disguised versions of it by Theorem 3.11: there is an
isomorphism between the groups G/[G, G] and U that turns π into ϕ. The next corollary
is a consequence.
Corollary 3.12. If G
ϕ
−−→U is universal for homomorphisms from G to abelian groups
then ker ϕ = [G, G] and ϕ(G) = U.
Proof. We know G
π
−−→G/[G, G] is universal, so by Theorem 3.11 there is an isomorphism
h: G/[G, G] →U making the following diagram commute.
G
π
z
ϕ

G/[G, G]
h
/ U
Then ϕ(g) = 1 ⇐⇒h(π(g)) = 1 ⇐⇒π(g) = 1 since h is injective, so ker ϕ = ker π =
[G, G]. Since h and π are surjective, ϕ = h ◦π is surjective, so ϕ(G) = U.
□
Remark 3.13. This corollary can also be proved in the style of Theorems 2.9 and 2.10,
making fuller use of the abstract universal mapping property and Theorem 3.11, never
needing knowledge of any speciﬁc example of a universal object.
4. Direct product of groups
Fix groups G1 and G2.
We will describe a universal mapping property of the group
G1 × G2 with componentwise operations. As in the previous examples, we need to think
about G1 × G2 not by itself but equipped with extra mapping data. In this case, the extra
data are the projection homomorphisms
pr1 : G1 × G2 →G1
pr2 : G1 × G2 →G2
where pr1(g1, g2) = g1 and pr2(g1, g2) = g2. These can be put together in a diagram:
G1 × G2
pr2
$
pr1
z
G1
G2
What is special about G1 × G2 together with its projection homomorphisms to G1 and G2
is that it “explains” pairs of homomorphisms from all groups to G1 and G2.

<!-- page 13 -->
UNIVERSAL MAPPING PROPERTIES
13
Theorem 4.1. For every pair of homomorphisms f1, f2 from an arbitrary group G to G1
and G2
G
f1
~
f2
 
G1
G2
set f : G →G1 ×G2 by f(g) = (f1(g), f2(g)). It is the unique homomorphism G →G1 ×G2
that makes the following big diagram commute.
G
f1


f2

G1 × G2
pr1
z
pr2
$
G1
G2
Proof. Step 1. The mapping f in the theorem is a homomorphism.
This is a simple calculation: since f1 and f2 are homomorphisms, for each g ∈G
f(gg′) = (f1(gg′), f2(gg′)) = (f1(g)f1(g′), f2(g)f2(g′)) = (f1(g), f2(g))(f1(g′), f2(g′)),
which is f(g)f(g′).
Step 2. Using f as the homomorphism G →G1 × G2, the big diagram commutes.
By the deﬁning formula f(g) = (f1(g), f2(g)), the ﬁrst component function of f is f1 and
the second component function of f is f2. Thus pr1 ◦f = f1 and pr2 ◦f = f2, which is what
it means for the big diagram to commute.
Step 3. A unique homomorphism h: G →G1 × G2 makes the big diagram commute.
Suppose h: G →G1 × G2 is a homomorphism making the big diagram commute. Write
each value of h as h(g) = (a(g), b(g)), so
a(g) = pr1(h(g)) = f1(g)
and
b(g) = pr2(h(g)) = f2(g).
Thus h(g) = (f1(g), f2(g)) for all g, so h must be the homomorphism we already met.
□
To formulate Theorem 4.1 as a universal mapping property for G1 × G2, consider as
new objects of interest all (G, f1, f2) where G is an arbitrary group and f1 : G →G1 and
f2 : G →G2 are homomorphisms from G to ﬁxed groups G1 and G2. As a diagram, (G, f1, f2)
looks like this.
G
f2
 
f1
~
G1
G2
Deﬁnition 4.2. Given any two such objects
G
f1
~
f2
 
G1
G2
and
G′
f′
1
~
f′
2
 
G1
G2

<!-- page 14 -->
14
KEITH CONRAD
a morphism from (G, f1, f2) to (G′, f′
1, f′
2) is a homomorphism h: G →G′ such that the
following big diagram commutes.
G
f1

f2

h

G′
f′
1
~
f′
2
 
G1
G2
Call a morphism h an isomorphism if it is a group isomorphism from G to G′.
We are now viewing things vertically rather than horizontally: morphisms go “from top
to bottom” rather than “from left to right”. Think of h: (G, f1, f2) →(G′, f′
1, f′
2) as turning
G into G′, f1 into f′
1, and f2 into f′
2 by commutativity of the big diagram.
Example 4.3. For each triple (G, f1, f2), the identity id: G →G gives us a morphism from
(G, f1, f2) to itself.
G
f1

f2

id

G
f1
~
f2
 
G1
G2
Example 4.4. Morphisms h: (G, f1, f2) →(G′, f′
1, f′
2) and h′ : (G′, f′
1, f′
2) →(G′′, f′′
1 , f′′
2 )
can be composed. The two commuting diagrams of group homomorphisms
G
f1

f2

h

G′
f′
1
~
f′
2
 
G1
G2
G′
f′
1

f′
2

h′

G′′
f′′
1
}
f′′
2
!
G1
G2
can be placed on top of each other to get the large commuting diagram on the left, which
becomes the one on the right after removing some parts linked to G′ (it still commutes).
G
f1

h

f2

G′
f′
1

h′

f′
2

G′′
f′′
1
}
f′′
2
!
G1
G2
G
f1

h′◦h

f2

G′′
f′′
1
}
f′′
2
!
G1
G2

<!-- page 15 -->
UNIVERSAL MAPPING PROPERTIES
15
By the diagram on the right h′ ◦h: (G, f1, f2) →(G′′, f′′
1 , f′′
2 ) is a morphism.
Theorem 4.1 says for each (G, f1, f2) there is a unique morphism in the direction
(G, f1, f2) →(G1 × G2, pr1, pr2).
The previous universal properties we met (for cyclic groups, quotient groups, and abelian-
izations) have the universal object as a source of a unique morphism, but a direct product
turns out to be the target of a unique morphism instead. That motivates the next deﬁnition.
Deﬁnition 4.5. An object (U, ϕ1, ϕ2) is called universal if every (G, f1, f2) admits a unique
morphism to (U, ϕ1, ϕ2).
Example 4.6. The triple (G1 × G2, pr1, pr2) is universal by Theorem 4.1.
Let’s think carefully about the directions of the arrows here. Why is it easier to write
down a homomorphism G →G1 × G2 rather than G1 × G2 →G?
The ﬁrst kind of
homomorphism only requires homomorphisms G →G1 and G →G2 and they don’t have
to be related in any way. On the other hand, if you want to write down a homomorphism
G1 × G2 →G that goes out of a direct product, there are nontrivial constraints: (x, 1)
and (1, y) commute in G1 × G2, so a homomorphism out of G1 × G2 needs the images of
G1 × {1} and {1} × G2 to commute in G. If G is nonabelian, this is a serious constraint.3
Trying to combine arbitrary homomorphisms G1 →G and G2 →G in some universal way
to get a homomorphism out of some new group G1 ∗G2 →G is related not to G1 × G2 but
to the free product of G1 and G2, which is complicated even when G1 and G2 are abelian,
e.g. for Z/2Z and Z/3Z, their direct product is cyclic of order 6 while their free product is
isomorphic to the inﬁnite group SL2(Z)/{±I2}. The lesson is that for groups,
it is easier to make a homomorphism to a direct product rather than from a direct product.
Aside from reversing the direction of all the arrows, arguments from before about univer-
sal objects being “uniquely isomorphic” carry over to the setting of direct products. Let’s
check this.
Theorem 4.7. If (U, ϕ1, ϕ2) and (U′, ϕ′
1, ϕ′
2) are both universal then there is a unique
morphism (U, ϕ1, ϕ2) →(U′, ϕ′
1, ϕ′
2) and it is an isomorphism.
Proof. There are unique homomorphisms h: U →U′, and k: U′ →U ﬁtting into the
following commutative diagrams.
U
ϕ1

ϕ2

h

U′
ϕ′
1
~
ϕ′
2
 
G1
G2
U′
ϕ′
1

ϕ′
2

k

U
ϕ1
}
ϕ2
!
G1
G2
3If all the groups are abelian, there is no constraint at all and we get what would be called a direct sum
rather than a direct product.

<!-- page 16 -->
16
KEITH CONRAD
Composing these in both orders as in Example 4.4, we get commutative diagrams
U
ϕ1

k◦h

ϕ2

U
ϕ1
~
ϕ2
 
G1
G2
U′
ϕ′
1

h◦k

ϕ′
2

U′
ϕ′
1
~
ϕ′
2
 
G1
G2
Since idU ﬁts in the left diagram in place of k◦h and idU′ ﬁts in the right diagram in place of
h◦k, uniqueness of the homomorphism by universality implies k ◦h = idU and h◦k = idU′.
Therefore h and k are inverse isomorphisms between (U, ϕ1, ϕ2) and (U′, ϕ′
1, ϕ′
2).
□
5. Review and initial/final objects
Let’s review some constructions on groups characterized by a universal mapping property.
(1) Cyclic group of order n for a positive integer n.
Among all groups G containing a chosen element γ such that γn = 1, a cyclic
group C of order n and a chosen generator c “come ﬁrst”: there is a unique homo-
morphism C →G such that c 7→γ.
(2) Quotient group G/N for a group G and normal subgroup N.
Among all homomorphisms G →eG that are trivial on N, the reduction map
πN : G →G/N “comes ﬁrst”: there is a unique homomorphism G/N →eG making
the following diagram commute.
G
πN
}

G/N
/ eG
(3) Abelianization of G.
Among all homomorphisms G →A where A is abelian, the reduction map π: G →
G/[G, G] “comes ﬁrst”: there is a unique homomorphism G/[G, G] →A making the
following diagram commute.
G
π
z

G/[G, G]
/ A
(4) Direct product G1 × G2 of two groups G1 and G2.
Among all (G, f1, f2) where G is a group and fi : G →G1 and f2 : G →G2 are
homomorphisms, the direct product G1 ×G2 and its projections pr1 : G1 ×G2 →G1
and pr2 : G1×G2 →G2 “comes last”: there is a unique homomorphism G →G1×G2

<!-- page 17 -->
UNIVERSAL MAPPING PROPERTIES
17
making the following diagram commute.
G



G1 × G2
pr1
z
pr2
$
G1
G2
In each of these settings we described a collection of objects and morphisms (maps)
between them so that we can compose suitable morphisms (when the target object of
the ﬁrst morphism equals the source object of the second morphism) and we can make a
particular construction of interest into an object that is “universal’ in the sense of having
a unique morphism to or from all other similar objects.
Each object has an identity morphism, and that is used to show two universal objects in
each setting must have exactly one isomorphism between them: a universal object is “unique
up to unique isomorphism” by a proof that is the same argument every time. These settings
are called categories. A precise deﬁnition will not be given here (see textbooks for that),
but the following examples of categories shows the wide scope of the concept.
• Groups and group homomorphisms
• Abelian groups and group homomorphisms
• Finite groups and group homomorphisms
• Rings and ring homomorphisms
• Commutative rings and ring homomorphisms
• Fields and ﬁeld homomorphisms
• Vector spaces over a ﬁeld F and F-linear maps
• Finite-dimensional vector spaces over a ﬁeld F and F-linear maps
• Modules over a commutative ring R and R-linear maps
• Metric spaces and isometries (dY (f(x), f(x′)) = dX(x, x′))
• Metric spaces and Lipschitz maps (dY (f(x), f(x′)) ≤CdX(x, x′) for some C ≥0)
• Topological spaces and continuous maps
• Smooth manifolds and smooth maps
None of these categories include our earlier examples. Here are the categories we created
for them.
• For ﬁxed n ≥1, all pairs (G, γ) where G is a group and γ ∈G satisﬁes γn = 1
• For ﬁxed G and N ◁G, all pairs ( eG, f) where eG is a group and f : G →eG is a group
homomorphism that is trivial on N
• For ﬁxed G, all pairs (A, f) where A is abelian and f : G →A is a group homomor-
phism
• For ﬁxed G1 and G2, all triples (G, f1, f2) where G is a group and f1 : G →G1 and
f2 : G →G2 are group homomorphisms
In a category C, each object A has an identity morphism id: A →A. An initial object in
C is an object in C that has a unique morphism to every other object in C. A ﬁnal object
in C is an object in C that has a unique morphism from every other object in C. What
we have been calling a “universal mapping property” of some construction is really just an
initial or ﬁnal object in some category. Initial and ﬁnal objects in a category don’t have

<!-- page 18 -->
18
KEITH CONRAD
to exist (examples are below), but if they do exist then they are “unique up to unique
isomorphism”: two initial objects have a unique morphism between them and it has to be
isomorphism, and likewise for ﬁnal objects.
What is an isomorphism of two objects in a category? This should generalize the idea of
group isomorphisms, ring isomorphisms, and homeomorphisms of topological spaces. The
deﬁnition we used earlier for a morphism to be called an isomorphism is not really the correct
one. It works well in many algebraic settings, where bijective homomorphisms always have
inverse maps that are homomorphisms. But in topology, a continuous bijection may not have
a continuous inverse: continuity of the inverse is part of the deﬁnition of a homeomorphism
(topological isomorphism). The correct deﬁnition of a morphism f : A →B between two
objects A and B in a category being an isomorphism is that there is an inverse morphism
g: B →A, meaning g ◦f = idA and f ◦g = idB.
Let’s look for initial and ﬁnal objects in some categories.
(1) Is there an initial object in the category of groups, i.e., a group that admits a unique
group homomorphism to all groups?
?
/ G
Yes: the trivial group. And obviously trivial groups are uniquely isomorphic.
You might wonder why Z doesn’t ﬁt the deﬁnition of an initial object in the
category of groups. After all, for each group G and g ∈G, there is a unique group
homomorphism Z −→G taking 1 to g by n 7→gn. Isn’t that what initial objects are
all about? No: we had to pick an element g ﬁrst, and changing g changes the group
homomorphism. Moreover, there is nothing group-theoretically special about 1 in
Z compared to −1.4 In addition to a group homomorphism Z →G where n 7→gn
there is the group homomorphism Z →G where n 7→g−n.
We could consider instead the category of “marked groups”: pairs (G, g) where
g ∈G, with a morphism of marked groups (G, g) →(G′, g′) being a group homo-
morphism G →G′ such that g 7→g′. Is there an “initial” marked group?
?
/ (G, g)
Yes: (Z, 1) ﬁts. While a trivial group {0} is an initial object in the category of
groups, the marked trivial group ({0} , 0) is not an initial object: there is a group
homomorphism {0} →Z, but it does not send {0} to 1.
(2) Is there a ﬁnal group?
G
/ ?
The trivial group works here, and ({0} , 0) is a ﬁnal object in the category of marked
groups.
(3) Is there an initial ring?
?
/ R
Yes: the ring Z admits a unique ring homomorphism to every other ring: 1 in Z
has to go to 1 in R and everything else is then determined.
(4) Is there a ﬁnal ring?
R
/ ?
Yes: the zero ring {0} admits a unique ring homomorphism from every other ring.
Note Z is by no means a ﬁnal ring, e.g., there is no ring homomorphism Q →Z
4Of course there is a big diﬀerence between 1 and −1 in Z from the viewpoint of ring theory.

<!-- page 19 -->
UNIVERSAL MAPPING PROPERTIES
19
since it would be injective and there are no subﬁelds of Z (or it would have to map
Q× to Z×, which is too small).
(5) Is there an initial ﬁeld?
?
/ F
No. But if we ﬁx the characeristic of the ﬁeld (0 or a prime p) then there is an
initial ﬁeld: Q for ﬁelds of characteristic 0 and Z/pZ for ﬁelds of characteristic p.
(6) Is there a ﬁnal ﬁeld?
F
/ ?
No. Even if we ﬁx the characteristic, there is still no ﬁnal ﬁeld. Field homomor-
phisms are always injective, so a ﬁnal ﬁeld would limit the possible cardinality of
other ﬁelds, and there is no such restriction even if we ﬁx the characteristic.
6. Universal mapping properties with rings
Having seen universal mapping properties at work in detail for several constructions in
group theory, we’ll treat examples in ring theory more concisely.
(1) Quotient rings.
For a commutative ring R and ideal I ⊂R, the universal mapping property for
R/I is analogous to that for quotient groups.
Theorem 6.1. Let R be a commutative ring and I be an ideal. For every ring
homomorphism f : R →S such that f vanishes on I, there is a unique ring homo-
morphism f : R/I →S making the following diagram commute, where πI : R →R/I
is the reduction map.
R
πI
}
f

R/I
f
/ S
As with quotient groups, this theorem is just as much about the reduction map
R
πI
−−−→R/I as it is about the ring R/I. Both the ring R/I and the mapping πI
should be considered together.
To express this theorem as a universal mapping property, convert it into a state-
ment about an initial object in a category by ﬁxing the ring R and ideal I and
deﬁning the category of all pairs (S, f) where f : R →S is a ring homomorphism
that vanishes on I, with a morphism (S, f) →(S′, f′) being a ring homomorphism
h: S →S′ that makes the following diagram commute.
R
f

f′
 
S
h
/ S′
(2) Direct product of rings
For two commutative rings R1 and R2, the product ring R1 × R2 with compo-
nentwise operations admits projection homomorphisms pr1 : R1 × R2 →R1 and
pr2 : R1 × R2 →R2.

<!-- page 20 -->
20
KEITH CONRAD
Theorem 6.2. Let R1 and R2 be a commutative rings. For every commutative ring
R and pair of ring homomorphisms f1 : R →R1 and r2 : R →R2, the mapping
f : R →R1 × R2 where f(r) = (f1(r), f2(r)) is the unique ring homomorphism
R →R1 × R2 that makes the following diagram commute.
R
f1


f2

R1 × R2
pr1
z
pr2
$
R1
R2
This is a universal mapping property for product rings in the same sense as for
product groups, by building a category with the product ring (and its projection
maps) as a ﬁnal object: the category of all triples (R, f1, f2) where f1 : R →R1 and
f2 : R →R2 are ring homomorphisms, and a morphism (R, f1, f2) →(R′, f′
1, f′
2) is
a ring homomorphism h: R →R′ that makes the following diagram commute.
R
f1

f2

h

R′
f′
1
~
f′
2
 
R1
R2
(3) Fraction ﬁelds
An integral domain R has a fraction ﬁeld F, which is all formal ratios a/b where
a, b ∈R with b ̸= 0, and a/b = c/d when ad = bc in R. We embed R into F by
sending a ∈R to a/1 in F. To avoid details of the construction of F, we’ll compare
F to other ﬁelds by emphasizing structural features in a universal mapping property.
For R = Z and F = Q, what is special about Q is that it is a minimal ﬁeld
containing Z. For a general integral domain R, its fraction ﬁeld should be a minimal
ﬁeld containing R. That means every ﬁeld K containing R, or more generally every
ﬁeld K that is the target of an injective ring homomorphism R →K, contains the
subﬁeld generated by the image of R, and this should look like a copy of the fraction
ﬁeld of R within K. That motivates the next theorem about fraction ﬁelds.
Theorem 6.3. Let R be an integral domain with fraction ﬁeld F and embedding
ι: R →F from the deﬁnition of fraction ﬁelds. For every ﬁeld K and injective ring
homomorphism f : R →K, there is a unique ring homomorphism ϕ: F →K that
makes the following diagram commute.
R
ι

f
 
F
ϕ
/ K
This makes the fraction ﬁeld of R (and the embedding ι: R →F of R into its
fraction ﬁeld) an initial object of the following category: all pairs (K, f) where

<!-- page 21 -->
UNIVERSAL MAPPING PROPERTIES
21
f : R →K is an injective ring homomorphism5 and a morphism (K, f) →(K′, f′)
is a ﬁeld homomorphism h: K →K′ that makes the following diagram commute.
R
f
~
f′
 
K
h
/ K′
7. Universal mapping properties with modules
Let R be a commutative ring. The important maps between R-modules are R-linear
maps. Below we present theorems giving a context in which particular constructions of
R-modules have a universal mapping property. We’ll be more concise here than we were
with rings; it is left to the reader to formulate the appropriate category in which the module
construction becomes either an initial object or a ﬁnal object.
(1) Cyclic modules.
Every cyclic R-module is isomorphic to the R-module R/I for an ideal I, where
I is the annihilator ideal of a generator of the module.
Theorem 7.1. For an ideal I in R, let C = Rc be a cyclic R-module with a chosen
generator c whose annihilator ideal AnnR(c) = {r ∈R : rc = 0} equals I.
For each R-module M containing an element m such that I ⊂AnnR(m), there is
a unique R-linear map f : C →M such that f(c) = m.
(2) Quotient modules.
Theorem 7.2. Let M be an R-module and N be a submodule. For every R-module
P and R-linear map f : M →P such that f vanishes on N, there is a unique R-
linear map f : M/N →P making the following diagram commute, where πN : M →
M/N is the reduction map.
M
πN
|
f

M/N
f
/ P
(3) Direct product of R-modules.
Our discussion of direct products of groups and rings used only two groups and
two rings. We’ll allow an arbitrary collection of factors in a direct product module
Y
i∈I
Mi = {(mi)i∈I : mi ∈Mi} .
This makes it easier to see a diﬀerence with direct sums (coming up next).
As with most product constructions, what is important are the projection maps
prj : Q
i∈I Mi →Mj for each j ∈I, which are all R-linear. Diﬀerent projection
maps don’t have anything to do with each other, so the next theorem uses a separate
commutative diagram for each prj, rather than one diagram involving all of them
as we did with a product of two groups and two rings.
5Not all homomorphisms from an integral domain to a ﬁeld have to be injective: consider Z →Z/pZ for
primes p.

<!-- page 22 -->
22
KEITH CONRAD
Theorem 7.3. For each R-module N and R-linear maps fi : N →Mi for i ∈I,
there is a unique R-linear map f : N −→Q
i∈I Mi making the following diagrams
commute for all j.
N
f
/
fj

Q
i∈I Mi
prj
{
Mj
This f is the function where f(n) = (fi(n))i∈I for all n ∈N.
(4) Direct sum of R-modules.
In a direct sum
M
i∈I
Mi = {(mi)i∈I : mi ∈Mi, all but ﬁnitely many mi = 0} ,
each element is built from ﬁnitely many pieces (its nonzero components). We can
embed Mi into the direct sum using the ith component (and zero elsewhere), which
makes the Mi’s submodules of the direct sum and they span it (using ﬁnite R-linear
combinations). While direct product modules have projection maps out, direct sum
modules have embedding maps in: ιj : Mj →L
i∈I Mi.
Theorem 7.4. For each R-module N and R-linear maps fi : Mi →N for i ∈
I, there is a unique R-linear map L
i∈I Mi →N making the following diagrams
commute for all j.
Mj
ιj
z
fj

L
i∈I Mi
f
/ N
This f is the function where f(P
i mi) = P
i fi(mi) for all P
i mi ∈L
i∈I Mi.
Comparing this to Theorem 7.3, the universal mapping properties of direct prod-
ucts and direct sums turn into one another by formally reversing all the arrows:
maps N →Mi become Mi →N, f : N →Q
i∈I Mi becomes f : L
i∈I Mi →N, and
prj : Q
i∈I Mi →Mj becomes ιj : Mj →L
i∈I Mi.
(5) Free R-modules.
For a set X, the embedding i: X ,→FR(X) to the free R-module on X by x 7→δx
is one function from X to an R-module. It explains all other functions from X to
R-modules by the following theorem.
Theorem 7.5. Let X be a set. For each R-module M and function f : X →M,
there is a unique R-linear map FR(X) →M making the following diagram commute.
X
ι
{
f
 
FR(X)
/ M
One reason for naming FR(X) a “free” R-module on X is that it is an R-module
containing X (or at least a subset that looks like X) as a basis, so the elements

<!-- page 23 -->
UNIVERSAL MAPPING PROPERTIES
23
of X are free of R-linear relations when viewed in FR(X). Theorem 7.5 provides
another reason for the label “free”: to write down an R-linear function from FR(X)
to an R-module M, we need to send the elements of X somewhere in M and there
is complete freedom in doing this, since each function X →M uniquely extends to
an R-linear function FR(X) →M.
When X is a ﬁnite set of size n, so FR(X) ∼= Rn, the theorem simply says each
function from a basis of Rn to an R-module M extends uniquely to a linear function
Rn →M.
Appendix A. Some universal mapping properties outside of algebra
We brieﬂy present here universal mapping properties for the product topology, the quo-
tient topology, and the completion of a metric space.
(1) Product topology.
For topological spaces Xi, the product topology on
Y
i∈I
Xi = {(xi)i∈I : xi ∈Xi}
makes all projection maps prj : Q
i∈I Xi →Xj continuous and it is the smallest
such topology on the product space. That could be considered a nice aspect of the
product topology: projections are important, so making them continuous should
be the minimal requirement we have for a topology put on Q
i∈I Xi. The following
theorem promotes continuity of the projection maps to a universal mapping property
for Q
i∈I Xi and its projections.
Theorem A.1. For each topological space Y and continuous maps fi : Y →Xi for
i ∈I, there is a unique continuous map f : Y →Q
i∈I Xi, where Q
i∈I Xi has the
product topology, that makes the following diagram commute for every j.
Y
f
/
fj

Q
i∈I Xi
prj
{
Xj
This f is the function where f(y) = (fi(y))i∈I for each y ∈Y .
(2) Quotient topology.
For an equivalence relation ∼on a topological space X, we have the canonical
surjective mapping π: X →X/∼that sends each x ∈X to its equivalence class
[x] with respect to ∼. The quotient topology on X/∼, where a subset U of X/∼
is called open if and only if π−1(U) is open in X, is the smallest topology on X/∼
that makes π: X →X/∼continuous. That π is continuous on X and constant
on ∼-equivalence classes leads to the following universal mapping property for the
quotient space X/∼and π.
Theorem A.2. Let X be a topological space and ∼be an equivalence relation on X.
For each topological space Y and continuous function f : X →Y such that x ∼x′ ⇒
f(x) = f(x′) for all x and x′ in X, there is a unique continuous map f : X/∼→Y ,

<!-- page 24 -->
24
KEITH CONRAD
where X/∼has the quotient topology, that makes the following diagram commute.
X
π
}
f

X/∼
f
/ Y
This f is the function where f([x]) = f(x) for each x ∈X.
(3) Completion of a metric space.
The completion of a metric space (X, dX) is a complete metric space ( b
X, c
dX) into
which X embeds isometrically (preserving distances) with a dense image. The point
of having a dense image is that it makes the closure of X in b
X equal to b
X. For
instance the completion of Q with respect to the metric d(r, s) = |r −s| is R, not
C, even though C is a complete metric space into which the metric space Q has an
isometric embedding.
There are multiple ways to show a metric space has a completion.6 Here is a
universal mapping property for completions, which is applicable no matter what
method is used to show the completion exists.
Theorem A.3. Let (X, dX) be a metric space. For each complete metric space
(C, dC) and isometry f : X →C, there is a unique isometry bf : b
X →C that makes
the following diagram commute, where iX : X →b
X is an isometric embedding of X
into a completion of X.
(X, dX)
iX
y
f
%
( b
X, c
dX)
bf
/ (C, dC)
The commutativity of this diagram says a completion of X maps uniquely to all
other complete metric spaces C in which there is an isometric embedding of X.
6See the appendix of https://kconrad.math.uconn.edu/blurbs/analysis/metricspaces.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*