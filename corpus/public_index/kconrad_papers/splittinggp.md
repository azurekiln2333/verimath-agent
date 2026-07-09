# Splittinggp

> **Source**: https://kconrad.math.uconn.edu/blurbs/splittinggp.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SPLITTING OF SHORT EXACT SEQUENCES FOR GROUPS
KEITH CONRAD
1. Introduction
A sequence of groups and group homomorphisms
H
α
−−→G
β
−−→K
is called exact at G if im α = ker β. This means two things: the image of α is killed by β
(β(α(h)) = 1 for all h ∈H), so im α ⊂ker β, and also only the image of α is killed by β (if
β(g) = 1 then g = α(h) for some h), so ker β ⊂im α. For example, to say 1 −→G
f
−−→K
is exact at G means f is injective, and to say H
f
−−→G −→1 is exact at G means f is
surjective. There is no need to label the homomorphisms coming out of 1 or going to 1
since there is only one possible choice. If the group operations are written additively, we
may use 0 in place of 1 for the trivial group.
A short exact sequence of groups is a sequence of groups and group homomorphisms
(1.1)
1 −→H
α
−−→G
β
−−→K −→1
which is exact at H, G, and K. That means α is injective, β is surjective, and im α = ker β.
A more general exact sequence can have lots of terms:
(1.2)
G1
α1
−−−→G2
α2
−−−→· · ·
αn−1
−−−−→Gn,
and it must be exact at each Gi for 1 < i < n. Exact sequences can also be of inﬁnite
length in one or both directions. We will only deal with short exact sequences here.
Exact sequences ﬁrst arose in algebraic topology, and the later development of homologi-
cal algebra (the type of algebra underlying algebraic topology) spread exact sequences into
the rest of mathematics.
Example 1.1. The determinant on GL2(R) gives rise to a short exact sequence
1 −→SL2(R) −→GL2(R)
det
−−−→R× −→1.
Example 1.2. When N ◁G we have a short exact sequence
(1.3)
1 −→N −→G −→G/N −→1,
where the map from N to G is inclusion, and the map from G to G/N is reduction mod N.
This example is the prototype for all short exact sequences, as we’ll see below.
Example 1.3. For two groups H and K, the direct product H ×K ﬁts into the short exact
sequence
1 −→H −→H × K −→K −→1,
where the map out of H is embedding to the ﬁrst factor (h 7→(h, 1)) and the map out of
H × K is projection to the second factor ((h, k) 7→k).
1

<!-- page 2 -->
2
KEITH CONRAD
Example 1.4. For two groups H and K, together with an action of K on H by automor-
phisms (a homomorphism ϕ: K →Aut(H)), the semidirect product H ⋊ϕ K ﬁts into the
short exact sequence
1 −→H −→H ⋊ϕ K −→K −→1,
where the maps are the same as in the previous example: h 7→(h, 1) and (h, k) 7→k.
Every short exact sequence (1.1) is a disguised form of (1.3). Indeed, even though in (1.1)
the group H may not literally be a subgroup of G and the group K may not literally be a
quotient group of G, α restricts to an isomorphism of H with the subgroup α(H)(= ker β)
of G and β induces an isomorphism β of the quotient group G/α(H) = G/ ker β with K.
Therefore we can place the general short exact sequence (1.1) and a short exact sequence
of the type (1.3) in a commutative diagram
(1.4)
1
/ H
α
/
α

G
β
/
id

K
/
β

1
1
/ α(H)
/ G
/ G/ ker β
/ 1
where the bottom short exact sequence is a special case of (1.3). The vertical maps are all
isomorphisms, and in this sense (1.1) looks like (1.3): they are linked to each other through
compatible isomorphisms of groups in the same positions in the two short exact sequences.
(The compatibility of the isomorphisms simply means the diagram (1.4) commutes.)
In Section 2 we will look at some more examples of short exact sequences. Then in Section
3, which is the most important part, we will see how direct products and semidirect products
of groups can be characterized in terms of short exact sequences with extra structure.
Section 4 discusses the idea of two short exact sequences being alike in broad terms.
2. Examples
When N ◁G, knowing N and G/N does not usually tell us what G is. That is, noniso-
morphic groups can have isomorphic normal subgroups with isomorphic quotient groups.
For example, D4 ̸∼= Q8 but ⟨r2⟩∼= {±1}(∼= Z/2Z) and D4/⟨r2⟩∼= Q8/{±1}(∼= (Z/2Z)2). In
terms of short exact sequences, the two short exact sequences
1 −→⟨r2⟩−→D4 −→D4/⟨r2⟩−→1
and
(2.1)
1 −→{±1} −→Q8 −→Q8/{±1} −→1
have isomorphic ﬁrst groups and isomorphic third groups, but nonisomorphic middle groups.
Here is a third example like these, with an abelian group in the middle:
0 −→Z/2Z −→Z/2Z × (Z/2Z)2 −→(Z/2Z)2 −→0.
This is the short exact sequence for a direct product, as in Example 1.3.
Here are two examples of short exact sequences with ﬁrst group Z/4Z and third group
Z/2Z, but nonisomorphic groups in the middle:
0 −→Z/4Z −→Z/4Z × Z/2Z −→Z/2Z −→0
0 −→Z/4Z −→Z/8Z −→Z/2Z −→0,
where the map Z/4Z →Z/8Z in the second short exact sequence is doubling (x mod 4 7→
2x mod 8). The other maps are all the obvious ones.

<!-- page 3 -->
SPLITTING OF SHORT EXACT SEQUENCES FOR GROUPS
3
Here are two short exact sequences with ﬁrst and third groups equal to µm (m > 1) but
nonisomorphic groups in the middle:
1 −→µm −→µm × µm −→µm −→1
and
1 −→µm
ι
−−→µm2
z7→zm
−−−−−→µm −→1.
The ﬁrst short exact sequence is the usual one for a direct product. In the second short
exact sequence, ι is the inclusion. The middle groups µm × µm and µm2 are not isomorphic
since µm × µm is not cyclic (no element of order m2).
3. Direct and Semidirect Products
For two groups H and K, an important “lifting” problem is the determination of all
groups G having a normal subgroup isomorphic to H and corresponding quotient group
isomorphic to K. Such G are the groups that ﬁt into a short exact sequence 1 −→H −→
G −→K −→1. There is always at least one such G, namely H × K. More generally, a
semidirect product H ⋊ϕK always sits in a short exact sequence having kernel H and image
K (Example 1.4). Not all short exact sequences arise from semidirect products.
Example 3.1. In the short exact sequence (2.1), Q8 is not isomorphic to a semidirect
product of {±1} and Q8/{±1} ∼= (Z/2Z)2 since such a semidirect product has more than 1
element of order 2 while Q8 has only one element of order 2.
Since semidirect products are “known,” short exact sequences made with them are con-
sidered “known” (even though semidirect products may seem like a subtle way to create
groups). It is important to recognize if a short exact sequence 1 −→H
α
−−→G
β
−−→K −→1
is essentially that for a direct product H × K or semidirect product H ⋊ϕ K. The next two
theorems give such criteria in terms of a left inverse for α and a right inverse for β.
Theorem 3.2. Let 1 −→H
α
−−→G
β
−−→K −→1 be a short exact sequence of groups. The
following are equivalent:
(1) There is a homomorphism α′ : G →H such that α′(α(h)) = h for all h ∈H.
(2) There is an isomorphism θ: G →H × K such that the diagram
1
/ H
α
/
id

G
β
/
θ

K
/
id

1
1
/ H
/ H × K
/ K
/ 1
commutes, where the bottom row is the short exact sequence for a direct product.
The commutative diagram in (2) says that θ identiﬁes α with the embedding H →H ×K
and β with the projection H×K →K. So the point of (2) is not simply that G is isomorphic
to H × K, but it is in a way that turns α and β into the standard maps from H to H × K
and from H × K to K.
The key point of (1) is that α′ is a homomorphism. Merely from α being injective, there
is a function α′ : G →H such that α′(α(h)) = h for all h, for instance the function
α′(g) =
(
1,
if g ̸∈α(H),
h,
if g = α(h).

<!-- page 4 -->
4
KEITH CONRAD
But this α′ is almost surely not a homomorphism.
Proof. (1) ⇒(2): Deﬁne θ: G →H × K by
θ(g) = (α′(g), β(g)).
This is a homomorphism since α′ and β are homomorphisms. To see θ is injective, suppose
θ(g) = (1, 1), so α′(g) = 1 and β(g) = 1. From exactness at G, the condition β(g) = 1
implies g = α(h) for some h ∈H. Then 1 = α′(g) = α′(α(h)) = h, so g = α(h) = α(1) = 1.
To show θ is surjective, let (h, k) ∈H × K. Since β is onto, k = β(g) for some g ∈G.
Since ker β = im α, the general inverse image of k under β is gα(x) for x ∈H. We want to
ﬁnd x ∈H such that α′(gα(x)) = h, so then θ(gα(x)) = (h, k). Since α′ is a homomorphism,
the condition α′(gα(x)) = h is equivalent to α′(g)x = h, so deﬁne x = α′(g)−1h. Then
θ(gα(x)) = (α′(gα(x)), β(gα(x))) = (h, k),
so θ is an isomorphism from G to H × K.
Next, we want to check the diagram
1
/ H
α
/
id

G
β
/
θ

K
/
id

1
1
/ H
/ H × K
/ K
/ 1
commutes. In the ﬁrst square
H
α
/
id

G
θ

H
/ H × K
taking h ∈H along the top and right has the eﬀect h 7→α(h) 7→(α′(α(h)), β(α(h))) = (h, 1),
which is also the result of taking h along the left and bottom. In the second square
G
β
/
θ

K
id

H × K
/ K
taking g ∈G along the top and right has the eﬀect g 7→β(g) 7→β(g), and going along the
left and bottom leads to g 7→(α′(g), β(g)) 7→β(g). So the diagram commutes.
(2) ⇒(1): Suppose there is an isomorphism θ: G →H × K such that
1
/ H
α
/
id

G
β
/
θ

K
/
id

1
1
/ H
/ H × K
/ K
/ 1
commutes. For g ∈G, θ(g) ∈H × K has second coordinate β(g) from commutativity of
the second square. Let α′(g) denote the ﬁrst coordinate:
θ(g) = (α′(g), β(g)).

<!-- page 5 -->
SPLITTING OF SHORT EXACT SEQUENCES FOR GROUPS
5
Then α′ : G →H is a function and θ is a homomorphism, so α′ is a homomorphism. The
commutativity of the ﬁrst square implies θ(α(h)) = (h, 1), so (α′(α(h)), β(α(h))) = (h, 1),
so α′(α(h)) = h for all h ∈H.
□
The proof shows that the homomorphisms α′ in (1) and the isomorphisms θ in (2) are in
bijection by the formula θ(g) = (α′(g), β(g)) for all g ∈G.
Theorem 3.3. Let 1 −→H
α
−−→G
β
−−→K −→1 be a short exact sequence. The following
are equivalent:
(1) There is a homomorphism β′ : K →G such that β(β′(k)) = k for all k ∈K.
(2) There is a homomorphism ϕ: K →Aut(H) and an isomorphism θ: G →H ⋊ϕ K
such that the diagram
1
/ H
α
/
id

G
β
/
θ

K
/
id

1
1
/ H
/ H ⋊ϕ K
/ K
/ 1
commutes, where the bottom short exact sequence is the usual one for a semidirect
product.
As with Theorem 3.2, the key part of (1) is that β′ is a homomorphism. From surjectivity
of β, there is a function β′ : K →G such that β(β′(k)) = k for all k ∈K, for instance set
β′(k) for each k to be a solution1 to β(g) = k. But usually this β′ is not a homomorphism.
Proof. (1) ⇒(2): From the homomorphism β′ we have to create an action ϕ of K on H by
automorphisms and an isomorphism of G with H ⋊ϕ K. Using β′, we can make K act on
H using conjugation in G: for k ∈K and h ∈H, β′(k)α(h)β′(k−1) ∈ker β since
β(β′(k)α(h)β′(k−1)) = β(β′(k))β(α(h))β(β′(k−1)) = k · 1 · k−1 = 1.
Since ker β = im α, we can write β′(k)α(h)β′(k−1) = α(h′) for an h′ ∈H, and h′ is unique
since α is injective. This h′ is determined by h and k. We write h′ as ϕk(h), so ϕk(h)
denotes the unique element of H such that
(3.1)
β′(k)α(h)β′(k)−1 = α(ϕk(h)),
where β′(k−1) = β′(k)−1 since β′ is a homomorphism. Since ϕk(h) ∈H, we get a function
ϕk : H →H. We will show ϕk ∈Aut(H) and k 7→ϕk is a homomorphism K →Aut(H).
First, setting k = 1 in (3.1), α(h) = α(ϕ1(h)), so ϕ1(h) = h for all h ∈H.
Thus
ϕ1 = idH. Next we check ϕk : H →H is a homomorphism for each k ∈K. For h1 and h2
in H, ϕk(h1h2) is characterized by the equation β′(k)α(h1h2)β′(k)−1 = α(ϕk(h1h2)). The
left side is
β′(k)α(h1)α(h2)β′(k)−1
=
β′(k)α(h1)β′(k)−1β′(k)α(h2)β′(k)−1
=
α(ϕk(h1))α(ϕk(h2))
=
α(ϕk(h1)ϕk(h2)),
so by injectivity of α we have ϕk(h1)ϕk(h2) = ϕk(h1h2).
Next we show ϕk1 ◦ϕk2 = ϕk1k2. For h ∈H, ϕk1k2(h) is characterized by the equation
β′(k1k2)α(h)β′(k1k2)−1 = α(ϕk1k2(h)),
1Here we use the Axiom of Choice.

<!-- page 6 -->
6
KEITH CONRAD
and the left side is
β′(k1)β′(k2)α(h)β′(k2)−1β′(k1)−1
=
β′(k1)α(ϕk2(h))β′(k1)−1
by (3.1)
=
α(ϕk1(ϕk2(h))),
so ϕk1(ϕk2(h)) = ϕk1k2(h), so ϕk1 ◦ϕk2 = ϕk1k2.
In particular, ϕk ◦ϕk−1 = ϕ1 and
ϕk−1 ◦ϕk = ϕ1, so ϕk ∈Aut(H) and k 7→ϕk is a homomorphism K →Aut(H). We
have proved that (3.1) provides an action of K on H by automorphisms, so we have the
semidirect product H ⋊ϕ K.
To get an isomorphism G →H ⋊ϕ K, it is easier to go in the other direction.
Let
γ : H ⋊ϕ K →G by
γ(h, k) = α(h)β′(k).
To check γ is a homomorphism,
γ((h1, k1)(h2, k2))
=
γ(h1ϕk1(h2), k1k2)
=
α(h1ϕk1(h2))β′(k1k2)
=
α(h1)α(ϕk1(h2))β′(k1)β′(k2)
=
α(h1)(β′(k1)α(h2)β′(k1)−1)β′(k1)β′(k2)
by (3.1)
=
α(h1)β′(k1)α(h2)β′(k2)
=
γ(h1, k1)γ(h2, k2).
To show γ is injective, if γ(h, k) = 1 then α(h)β′(k) = 1. Applying β to both sides,
β(α(h))β(β′(k)) = β(1) = 1, so k = 1. Then α(h) · 1 = 1, so h = 1 since α is injective.
To show γ is surjective, pick g ∈G. We want to ﬁnd h ∈H and k ∈K such that
α(h)β′(k) = g. Applying β to both sides, β(α(h))β(β′(k)) = β(g), so k = β(g). So we
deﬁne k := β(g) and then ask if there is h ∈H such that α(h) = gβ′(k−1) = gβ′(β(g)−1).
Since im α = ker β, whether or not there is such an h is equivalent to checking gβ′(β(g)−1)) ∈
ker β:
β(gβ′(β(g)−1))
=
β(g)β(β′(β(g)−1))
=
β(g)β(g)−1
=
1.
Thus γ : H ⋊ϕ K →G is an isomorphism. Let θ = γ−1 be the inverse isomorphism.
Finally, to show the diagram
1
/ H
α
/
id

G
β
/
θ

K
/
id

1
1
/ H
/ H ⋊ϕ K
/ K
/ 1
commutes, it is equivalent to show the “ﬂipped” diagram
1
/ H
α
/ G
β
/ K
/ 1
1
/ H
/
id
O
H ⋊ϕ K
/
γ
O
K
/
id
O
1
commutes. For h ∈H, going around the ﬁrst square along the left and top has the eﬀect
h 7→h 7→α(h), and going around the other way has the eﬀect h 7→(h, 1) 7→γ(h, 1) =

<!-- page 7 -->
SPLITTING OF SHORT EXACT SEQUENCES FOR GROUPS
7
α(h)β′(1) = α(h). In the second square, for (h, k) ∈H ⋊ϕ K going around the left and top
has the eﬀect (h, k) 7→β(γ(h, k)) = β(α(h))β(β′(k)) = k, while going around the other way
has the eﬀect (h, k) 7→k 7→k.
(2) ⇒(1): In the proof that (1) ⇒(2), γ(h, k) = α(h)β′(k), so γ(1, k) = β′(k). This
suggests that when we have an isomorphism θ: G →H ⋊ϕ K that we deﬁne β′ : K →G by
β′(k) = θ−1(1, k). This is a homomorphism since k 7→(1, k) is a homomorphism and θ−1 is
a homomorphism. The composite β(β′(k)) = β(θ−1(1, k)) equals k from commutativity of
the diagram
G
β
/ K
H ⋊ϕ K
/
θ−1
O
K.
id
O
□
Deﬁnition 3.4. A short exact sequence 1 −→H
α
−−→G
β
−−→K −→1 is said to split if it ﬁts
the conditions of Theorem 3.3, so there is an isomorphism G →H ⋊K for some semidirect
product structure that makes α look the usual embedding H →H ⋊K and makes β look
like the usual projection H ⋊K →K.
A split short exact sequence essentially corresponds to the standard short exact sequence
for a semidirect product. The short exact sequence with Q8 in (2.1) is not split.
Since H ⋊ϕK might not be isomorphic to H ×K, the ﬁrst conditions in Theorems 3.2 and
3.3 are not equivalent: for a short exact sequence of groups 1 −→H
α
−−→G
β
−−→K −→1, if
there is a homomorphism β′ : K →G such that β(β′(k)) = k for all k there need not be a
homomorphism α′ : G →H such that α′(α(h)) = h for all h.
Example 3.5. For even n ≥6, let G = Dn, H = ⟨r2, s⟩, and K = ⟨rs⟩. Since H and K
are complementary subgroups of G and H ◁G, G = HK ∼= H ⋊ϕ K where K acts on H
by conjugation. Since H × K ∼= Dn/2 × Z/(2), if n/2 is even then H × K has a center of
order 4 (Dn/2 has a center of order 2) while G has a center of order 2, so G ̸∼= H × K.
When G is abelian, (3.1) simpliﬁes to α(h) = α(ϕk(h)) for all k and h, so h = ϕk(h).
Thus K acts trivially on H, so H ⋊ϕ K = H × K. Therefore Theorems 3.2 and 3.3 provide
three equivalent conditions on 1 −→H
α
−−→G
β
−−→K −→1 when G is abelian:
(1) There is a homomorphism α′ : G →H such that α′(α(h)) = h for all h ∈H.
(2) There is a homomorphism β′ : K →G such that β(β′(k)) = k for all k ∈K.
(3) There is an isomorphism θ: G →H × K such that the diagram
1
/ H
α
/
id

G
β
/
θ

K
/
id

1
1
/ H
/ H × K
/ K
/ 1
commutes, where the bottom row is the short exact sequence for a direct product.
4. Equivalent Short Exact Sequences
We said in the introduction that every short exact sequence (1.1) is basically like a
short exact sequence of type (1.3), and made the idea precise in terms of a commutative

<!-- page 8 -->
8
KEITH CONRAD
diagram (1.4) having both short exact sequences (1.1) and (1.3) appearing in it as the
rows, and the columns being isomorphisms. This idea of two short exact sequences being
basically alike can be applied more generally. Say 1 −→H1
α1
−−−→G1
β1
−−−→K1 −→1 and
1 −→H2
α2
−−−→G2
β2
−−−→K2 −→1 are equivalent if they ﬁt into a commutative diagram
(4.1)
1
/ H1
α1 /

G1
β1 /

K1
/

1
1
/ H2
α2 / G2
β2 / K2
/ 1
where the vertical maps are isomorphisms.
For example, (1.4) shows every short exact
sequence is equivalent to a short exact sequence of type (1.3). Note that, as in (1.4), we do
not insist for equivalence of short exact sequences that the ﬁrst and third isomorphisms in
(4.1) are the identity (the ﬁrst and third groups in each row need not even be equal), unlike
for the commutative diagrams in Theorems 3.2 and 3.3. The idea behind the commutativity
of (4.1) is that the middle groups G1 and G2 are isomorphic in such a way that the images
of the ﬁrst groups H1 and H2 sit inside the middle groups in similar ways, and the third
groups K1 and K2 are homomorphic images of the middle groups in similar ways.
Here is a concrete example of equivalent short exact sequences:
(4.2)
1 −→A3 −→S3
sgn
−−−→{±1} −→1
and
(4.3)
0 −→Z/3Z −→Aﬀ(Z/3Z)
det
−−−→(Z/3Z)× −→1,
where the ﬁrst map in (4.2) is inclusion and the ﬁrst map in (4.3) is b 7→( 1 b
0 1 ). These are
equivalent because there is a commutative diagram
1
/ A3
/

S3
sgn
/

{±1}
/

1
0
/ Z/3Z
/ Aﬀ(Z/3Z)
det
/ (Z/3Z)×
/ 1
where (4.2) and (4.3) are the rows and the vertical maps are all isomorphisms.
Theorem 3.2 gives us a condition for detecting when a short exact sequence 1 −→H
α
−−→
G
β
−−→K −→1 is equivalent to the usual short exact sequence for H × K from Example 1.3
with the ﬁrst and third vertical maps being the identities on H and K.
Example 4.1. Let H = K = Z and let a and b be relatively prime integers. We have a
short exact sequence
0 −→Z
α
−−→Z × Z
β
−−→Z −→0
where α(n) = (an, bn) and β(x, y) = bx −ay. (That ker β ⊂im α uses relatively primality
of a and b.) This is not the usual short exact sequence for Z × Z, but it is equivalent to it:
there are u and v in Z such that 1 = au + bv, and using them we have the commutative

<!-- page 9 -->
SPLITTING OF SHORT EXACT SEQUENCES FOR GROUPS
9
diagram
0
/ Z
α /
id

Z × Z
β
/
θ

Z
/
id

0
0
/ Z
/ Z × Z
/ Z
/ 0
where θ(x, y) = (ux + vy, bx −ay), and the bottom short exact sequence is the usual one
for Z × Z. The inverse of θ is (x, y) 7→(ax + vy, bx −uy).
Here is a short exact sequence 1 −→H
α
−−→H × K
β
−−→K −→1 that is not equivalent to
the usual one for a direct product.
Example 4.2. Let H = Z and K = (Z/mZ)N (countable direct product of copies of
Z/mZ) where m ≥2. We have a short exact sequence
(4.4)
0 −→Z
α
−−→Z × (Z/mZ)N
β
−−→(Z/mZ)N −→0
where α(x) = (mx, 0) and β(x, y) = (x mod m, y). (If K had ﬁnitely many coordinates,
then to deﬁne β(x, y) we’d have to do something like drop a coordinate of y and the
condition ker β ⊂im α would fail.) If (4.4) were equivalent to the usual short exact sequence
for Z × (Z/mZ)N then there would be a homomorphism α′ : Z × (Z/mZ)N →Z such that
α′(α(x)) = x for all x ∈Z. Then x = α′(mx, 0) = α′(m(x, 0)) = mα′(x, 0) in Z, which is
a contradiction when x is not divisible by m (e.g., x = 1). Thus (4.4) is not equivalent to
the usual short exact sequence for a direct product.
Remark 4.3. It turns out that all short exact sequences 1 −→H
α
−−→H × K
β
−−→K −→1
with a direct product in the middle are equivalent to the usual short exact sequence in
Example 1.3 if (i) H and K are ﬁnitely generated abelian groups, as in Example 4.1, or (ii)
H and K are ﬁnite groups. See https://mathoverflow.net/questions/80002.
Theorem 3.3 tells us when 1 −→H
α
−−→G
β
−−→K −→1 is equivalent to the usual short
exact sequence for some semidirect product H ⋊ϕ K with the ﬁrst and third vertical maps
being the identities on H and K. (The ﬁrst and third maps being identities is an extra
condition, not part of the deﬁnition of equivalence.)
The notion of equivalent short exact sequences is an equivalence relation: any short exact
sequence 1 −→H
α
−−→G
β
−−→K −→1 is equivalent to itself from the commutative diagram
(4.5)
1
/ H
α
/
id

G
β
/
id

K
/
id

1
1
/ H
α
/ G
β
/ K
/ 1
and using inverse isomorphisms in the vertical rows of (4.1) gives a commutative diagram
where the two rows are interchanged, so the notion of equivalent short exact sequences is
symmetric. For transitivity, we can combine two commutative diagrams
1
/ H1
α1 /

G1
β1 /

K1
/

1
1
/ H2
α2 / G2
β2 / K2
/ 1

<!-- page 10 -->
10
KEITH CONRAD
and
1
/ H2
α2 /

G2
β2 /

K2
/

1
1
/ H3
α3 / G3
β3 / K3
/ 1
into the commutative diagram
1
/ H1
α1 /

G1
β1 /

K1
/

1
1
/ H2
α2 /

G2
β2 /

K2
/

1
1
/ H3
α3 / G3
β3 / K3
/ 1
and then use the composite of the pairs of vertical isomorphisms to eliminate the middle
row and get the commutative diagram
1
/ H1
α1 /

G1
β1 /

K1
/

1
1
/ H3
α3 / G3
β3 / K3
/ 1
with isomorphisms as the vertical maps.
Here is the analogue of homomorphisms for short exact sequences. A morphism from
1 −→H1
α1
−−−→G1
β1
−−−→K1 −→1 to 1 −→H2
α2
−−−→G2
β2
−−−→K2 −→1 is a commutative
diagram (4.1) where the vertical maps are homomorphisms rather than isomorphisms. An
example of a morphism of short exact sequences is (for m > 1)
1
/ SL2(Z)
/

GL2(Z)
det
/

{±1}
/

1
1
/ SL2(Z/mZ)
/ GL2(Z/mZ) det
/ (Z/mZ)×
/ 1,
where the vertical maps are the natural mod m reduction maps. The identity morphism
for a short exact sequence is (4.5). Our argument that equivalence of short exact sequences
is transitive also shows how to compose two morphisms to get a third: compose vertical
homomorphisms in the same positions in the two diagrams. What we called equivalence
of two short exact sequences is the concept of isomorphism: a morphism of short exact se-
quences that admits an inverse morphism (one whose composite with the original morphism
on both sides gives the identity morphism for the two short exact sequences).

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*