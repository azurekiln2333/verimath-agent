# Galois Descent

> **Source**: https://kconrad.math.uconn.edu/blurbs/galoisdescent.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
GALOIS DESCENT
KEITH CONRAD
1. Introduction
Let L/K be a ﬁeld extension. A K-vector space W can be extended to an L-vector space
L ⊗K W, and W embeds into L ⊗K W by w 7→1 ⊗w. Under this embedding, when W ̸= 0
a K-basis {ei} of W turns into an L-basis {1 ⊗ei} of L ⊗K W. Passing from W to L ⊗K W
is called ascent. In the other direction, if we are given an L-vector space V ̸= 0, we may
ask how to describe the K-subspaces W ⊂V such that a K-basis of W is an L-basis of V .
Deﬁnition 1.1. For an L-vector space V , a K-subspace W such that a K-basis of W is an
L-basis of V is called a K-form of V .
For completeness, when V = 0 (so there is no basis), we regard W = 0 as a K-form of
V . The passage from an L-vector space V to a K-form of V is called descent. Whether we
can descend is the question of ﬁlling in the question mark in the ﬁgure below.
L
L ⊗K W
V
K
W
O
?
O
Example 1.2. A K-form of Ln is Kn since the standard K-basis of Kn is an L-basis of
Ln.
Example 1.3. A K-form of Mn(L) is Mn(K) since the standard K-basis of Mn(K) is an
L-basis of Mn(L).
Example 1.4. A K-form of L[X] is K[X] since the K-basis {1, X, X2, . . . } of K[X] is an
L-basis of L[X].
Example 1.5. Every L-vector space V has a K-form: when V ̸= 0 and we pick an L-basis
{ei} of V , its K-span is a K-form of V since the ei’s are linearly independent over K and
thus are a basis of their K-span.
When K = R and L = C, ascent (passing from W to C ⊗R W) is the process of
complexiﬁcation and descent is related to conjugations on complex vector spaces: an R-
form of a complex vector space is the ﬁxed set of a conjugation.
Our deﬁnition of a K-form involves a choice of basis. Let’s check this choice doesn’t
really matter:
Theorem 1.6. Let V be a nonzero L-vector space and W be a nonzero K-subspace of V .
The following conditions are equivalent:
(1) every K-basis of W is an L-basis of V ,
(2) some K-basis of W is an L-basis of V .
1

<!-- page 2 -->
2
KEITH CONRAD
(3) the L-linear map L⊗K W →V given by a⊗w 7→aw is an isomorphism of L-vector
spaces.
Proof. (1) ⇒(2): Obvious.
(2) ⇒(3): Suppose the K-basis {ei} of W is an L-basis of V . Then the L-linear map
L⊗K W →V given by a⊗w 7→aw sends 1⊗ei to ei so it identiﬁes L-bases of two L-vector
spaces. Therefore this map is an isomorphism.
(3) ⇒(1): Suppose L ⊗K W ∼= V as L-vector spaces by a ⊗w 7→aw. For a K-basis {ei}
of W, {1 ⊗ei} is an L-basis of L ⊗K W and therefore under the indicated isomorphism the
vectors 1 · ei = ei are an L-basis of V .
□
The second property of Theorem 1.6 is how we deﬁned a K-form. The ﬁrst property
shows the concept of a K-form is independent of the choice of basis. The third property
is the “right” deﬁnition of a K-form,1 although the other properties are arguably a better
way to understand what the concept is all about (or even to recognize it in concrete cases
like Examples 1.2, 1.3, and 1.4.)
In the C/R-case, R-forms of a complex vector space are parametrized by the conjugations
on V . Generalizing this, we will see that when L/K is a ﬁnite Galois extension, we can
parametrize the K-forms of an L-vector space V by keeping track of how Gal(L/K) can act
in a “semilinear” way on V .2 We will ﬁnd that for each semilinear action of Gal(L/K) on
a nonzero L-vector space V , there is an L-basis of Gal(L/K)-invariant vectors: that means
σ(v) = v for all σ ∈Gal(L/K).
References on this material are [1, pp. 295–296], [3, Chap. 17], and [5, pp. 66–68].
2. Galois descent on vector spaces
From now on we suppose L/K is a ﬁnite Galois extension and write G = Gal(L/K). We
will introduce an organized way for G to act on an L-vector space (which we will call a
G-structure), where G interacts in a reasonable way with scalar multiplication by L.
Deﬁnition 2.1. For an L-vector space V and σ ∈G, a σ-linear map r: V →V is an
additive function on V such that
(2.1)
r(av) = σ(a)r(v)
for all a in L and v in V .
When σ is the identity automorphism of L, r is L-linear. For general σ in G, r is K-linear
(take a ∈K in (2.1)), but it is not quite L-linear; the eﬀect of scaling by L on V is “twisted”
by σ when r is applied. When the reference to σ in (2.1) is not needed, the label semilinear
is used, but it should be kept in mind that a semilinear map is always relative to a choice
of ﬁeld automorphism σ of L.
Example 2.2. If V is a complex vector space and σ: C →C is complex conjugation, a
σ-linear map on V is a conjugate-linear map.
Example 2.3. On Ln, rσ(a1, . . . , an) = (σ(a1), . . . , σ(an)) is σ-linear.
Example 2.4. On Mn(L), rσ(aij) = (σ(aij)) is σ-linear.
1Among other things, the third property makes sense for the zero vector space without needing a separate
deﬁnition in that case.
2The concept of a K-form does not require L/K to be Galois, but in the Galois case we can say a lot
about all the K-forms.

<!-- page 3 -->
GALOIS DESCENT
3
Example 2.5. On L[X], rσ(Pd
i=0 aiXi) = Pd
i=0 σ(ai)Xi is σ-linear.
Example 2.6. When W is a K-vector space, we can apply σ to the “ﬁrst component” in
L ⊗K W: the function rσ = σ ⊗idW mapping L ⊗K W to itself by
rσ(a ⊗w) = σ(a) ⊗w
on simple tensors is σ-linear, since rσ(a′(a⊗w)) = rσ(a′a⊗w) = σ(a′a)⊗w = σ(a′)σ(a)⊗w =
σ(a′)(σ(a) ⊗w), so rσ(a′t) = a′rσ(t) for all t in L ⊗K W by additivity.
Since rσ(1 ⊗w) = 1 ⊗w and the condition rσ(a ⊗w) = σ(a) ⊗w is equivalent to
rσ(a(1 ⊗w)) = σ(a)rσ(1 ⊗w), this semilinear action of G on L ⊗K W is the unique one
that ﬁxes 1 ⊗W pointwise.
Deﬁnition 2.7. A G-structure on an L-vector space V is a set of functions rσ : V →V ,
one for each σ in G, such that rσ is σ-linear, r1 = idV , and rσ ◦rσ′ = rσσ′. When V is given
a G-structure, we say G acts semilinearly on V .
Example 2.8. When K = R and L = C, so G = Gal(C/R) is the identity and complex
conjugation, to describe a G-structure on a complex vector space V we only need to describe
the map r: V →V associated to complex conjugation, since by Deﬁnition 2.1 the map
associated to the identity of G has to be the identity. The conditions r must satisfy are:
r is additive, r(zv) = zr(v), and r2 = idV . This is nothing other than a conjugation on
V , so a choice of Gal(C/R)-structure on a complex vector space is the same as a choice of
conjugation on it.
Example 2.9. The maps rσ in Examples 2.3, 2.4, 2.5, and 2.6, as σ runs over G, are a
G-structure on Ln, Mn(L), L[X], and L ⊗K W. The G-structure in Example 2.6 is called
the standard G-structure on L ⊗K W.
Example 2.10. If ϕ: V →V ′ is an L-vector space isomorphism and V has a G-structure
{rσ}, there is a unique G-structure {r′
σ} on V ′ compatible with ϕ: r′
σ(v′) = ϕ(rσϕ−1(v′)):
V
ϕ
/
rσ

V ′
r′
σ

V
ϕ
/ V ′
Just as it is simpler to write group actions on sets as gx instead of πg(x) (where πg is
the permutation on X associated to g), it is simpler to write rσ(v) as just σ(v). In this
notation, the equation rσ(av) = σ(a)rσ(v) becomes σ(av) = σ(a)σ(v). So a G-structure on
an L-vector space V is a way of making the group G act semilinearly on V : each σ ∈G is
σ-linear on V , idL ∈G acts as idV , and σ(σ′(v)) = (σσ′)(v) for all σ and σ′ in G and v ∈V .
On a complex vector space V there is a one-to-one correspondence between R-forms of
V and conjugations on V . We will generalize this correspondence to one between K-forms
of an L-vector space and G-structures on the vector space. (This is a generalization since
Example 2.8 says conjugations on a complex vector space are basically the same thing as
Gal(C/R)-structures on the vector space.)
First we need several lemmas.
Lemma 2.11. Let V be an L-vector space with a G-structure and let V ′ be an L-subspace
that is preserved by G: for all σ ∈G, σ(V ′) ⊂V ′. Then the quotient vector space V/V ′ has
a G-structure deﬁned by σ(v + V ′) = σ(v) + V ′.

<!-- page 4 -->
4
KEITH CONRAD
Proof. We check that the action of G on V/V ′ is well-deﬁned: if v1 ≡v2 mod V ′ then
v1 −v2 ∈V ′, so for each σ ∈G we have σ(v1 −v2) ∈σ(V ′) ⊂V ′. Thus σ(v1) −σ(v2) ∈V ′,
so σ(v1) ≡σ(v2) mod V ′. That each σ acts σ-linearly on V/V ′ is clear, because the relevant
conditions are already satisﬁed on V and thus work out on coset representatives. Further
details are left to the reader.
□
Lemma 2.12. Let A be an abelian group and χ1, . . . , χn : A →L× be distinct homomor-
phisms. For an L-vector space V and v1, . . . , vn ∈V , if χ1(a)v1 + · · · + χn(a)vn = 0 for all
a ∈A then all vi are 0.
Proof. The special case V = L is the linear independence of characters. It is left as an
exercise to reread the proof of that special case and generalize the argument.
□
When V is an L-vector space with a G-structure, the ﬁxed set of G in V is
V G = {v ∈V : σ(v) = v for all σ ∈G}.
This is a K-subspace. When K = R and L = C, so a G-structure on V is a choice of
conjugation c on V , V G = {v ∈V : c(v) = v}.
Lemma 2.13. Let V be an L-vector space with a G-structure. Deﬁne a corresponding trace
map TrG : V →V by
TrG(v) =
X
σ∈G
σ(v).
Then TrG(V ) ⊂V G, and when v ̸= 0 in V there is a ∈L such that TrG(av) ̸= 0. In
particular, if V ̸= 0 then V G ̸= 0.
Proof. To show the values of TrG are in V G, for each σ′ ∈G
σ′(TrG(v)) =
X
σ∈G
σ′(σ(v)) =
X
σ∈G
(σ′σ)(v) =
X
σ∈G
σ(v) = TrG(v).
To show if v ̸= 0 that TrG(av) ̸= 0 for some a ∈L, we prove the contrapositive. Assume
for a ﬁxed v ∈V that TrG(av) = 0 for all a ∈L. Then
0 =
X
σ∈G
σ(av) =
X
σ∈G
σ(a)σ(v)
for all a ∈L. By Lemma 2.12 with A = L×, every σ(v) is 0. In particular, at σ = idL we
get v = 0.
□
Next is our main result linking K-forms and G-structures. We will use the tensor product
description of a K-form (from Theorem 1.6): a K-subspace W of an L-vector space V is a
K-form exactly when the natural L-linear map L⊗K W →V is an isomorphism of L-vector
spaces.
Theorem 2.14. Let V be an L-vector space. There is a bijection between the following
data on V :
(1) K-forms of V ,
(2) G-structures on V .
In brief, the correspondence from (1) to (2) is W ⇝L⊗KW with its standard G-structure
and the correspondence from (2) to (1) is V ⇝V G.

<!-- page 5 -->
GALOIS DESCENT
5
Proof. This is clear if V = 0 since {0} is the only K-form (even the only K-subspace) and
there is only one G-structure. So from now on take V ̸= 0. If we start with a K-form W of
V , so ϕ: L ⊗K W →V by a ⊗w 7→aw is an L-linear isomorphism, we get a G-structure
on V by using ϕ to transport the standard G-structure {rσ} on L ⊗K W (Example 2.6) to
a G-structure {σW }σ∈G on V (Example 2.10). We simply insist the diagrams
L ⊗K W
ϕ
/
rσ

V
σW

L ⊗K W
ϕ
/ V
commute for all σ ∈G. Explicitly, deﬁne σW : V →V by
σW
 X
i
aiwi
!
=
X
i
σ(ai)wi,
where ai ∈L and wi ∈W.
(The well-deﬁnedness of σW , where the wi’s are arbitrary
elements of W, depends on ϕ being an isomorphism of L-vector spaces.)
Conversely, if V has a G-structure then the K-subspace V G turns out to be a K-form on
V : the L-linear map f : L ⊗K V G →V by a ⊗w 7→aw is an isomorphism.
To show f is one-to-one, the case V G = 0 is easy. Suppose V G ̸= {0} and f(t) = 0 for
some t ∈L ⊗K V G. Write t as a sum of simple tensors, say t = P ai ⊗wi. This ﬁnite sum
can be arranged to have wi’s that are linearly independent over K: here we use V G ̸= 0
(Lemma 2.13). Then 0 = f(t) = P aiwi. We will show K-linearly independent vectors
in V G are L-linearly independent in V , hence all ai are 0 and this would mean t = 0 so
f is injective. To prove every K-linearly independent set in V G is L-linearly independent,
assume otherwise: there is a K-linearly independent set in V G that is L-linearly dependent:
such a dependence relation looks like
(2.2)
a1w1 + · · · + anwn = 0,
where w1, . . . , wn ∈V G and the ai’s in L are not all 0. Take (2.2) to be a nontrivial L-
linear relation among K-linearly independent vectors in V G of least length (least number of
terms). Then every ai is nonzero and n ≥2. By scaling, we may suppose an = 1. Applying
σ ∈G to (2.2), we get
(2.3)
σ(a1)w1 + · · · + σ(an)wn = 0.
Subtract (2.3) from (2.2):
(a1 −σ(a1))w1 + · · · + (an −σ(an))wn = 0.
The last term is 0 since an = 1, so this L-linear relation has n−1 terms. By the minimality
of n, such an L-linear relation among K-linearly independent vectors w1, . . . , wn−1 has to
be the trivial relation: ai −σ(ai) = 0 for i = 1, 2, . . . , n−1. So each ai is ﬁxed by all σ in G,
hence ai ∈K for i = 1, 2, . . . , n −1. Also an = 1 ∈K. But that means (2.2) is a nontrivial
linear dependence relation among the wi’s over K, that is impossible (the wi’s are linearly
independent over K). So we have a contradiction, which proves f is one-to-one.
To show f is onto, we look at the image f(L ⊗K V G), which is an L-subspace of V . This
image is stable under the action of G: on simple tensors a ⊗w in L ⊗K V G,
σ(f(a ⊗w)) = σ(aw) = σ(a)σ(w) = σ(a)w = f(σ(a) ⊗w),

<!-- page 6 -->
6
KEITH CONRAD
so by additivity of σ on V we have σ(f(L ⊗K V G)) ⊂f(L ⊗K V G). Therefore the quotient
space V := V/f(L ⊗K V G) inherits a G-structure from V by σ(v) = σ(v) (Lemma 2.11).
For v ∈V , TrG(v) ∈V G ⊂f(L ⊗K V G), so on V we have TrG(v) = TrG(v) = 0. Since all
elements of V have trace 0, V has to be 0 by Lemma 2.13. (A nonzero element of V would
have a nonzero L-multiple with nonzero trace.) Since V = 0, V = f(L ⊗K V G), so f is
onto.
In the C/R-case, the surjectivity of f : C ⊗R Vc →V for a complex vector space V with
a conjugation c is based on the equation
(2.4)
v = v + c(v)
2
+ iv −c(v)
2i
,
where the vectors 1
2(v + c(v)) and
1
2i(v −c(v)) are ﬁxed by c. The formula (2.4) can be
generalized to the L/K-case using TrG: if {α1, . . . , αd} is a K-basis of L then there are
{β1, . . . , βd} in L such that v = P
j αjTrG(βjv) for all v ∈V . That would give a second
proof of surjectivity of f.
It remains to check that our correspondences between K-forms of V and G-structures on
V are inverses of one another.
K-form to G-structure and back: Pick a K-form W of V . The corresponding G-structure
{σW : σ ∈G} on V is given by σW (P
i aiwi) := P
i σ(ai)wi for ai ∈L and wi ∈W. We
need to check the subspace V G = {v ∈V : σW (v) = v for all σ ∈G} associated to this
G-structure is W. Certainly W ⊂V G.
To show V G ⊂W, pick a K-basis {ei} of W. Since W is a K-form of V , each v ∈V
has the form v = P aiei with ai ∈L (all but ﬁnitely many coeﬃcients ai are 0). Then
σW (v) = P
i σ(ai)ei. If σW (v) = v for all σ ∈G then
X
i
(σ(ai) −ai)ei = 0
for all σ ∈G. The ei’s are linearly independent over L (because they are the basis of a
K-form of V ), so σ(ai) −ai = 0 for all ai and all σ ∈G. Thus all ai are in K, so v ∈W.
Thus V G ⊂W.3
G-structure to K-form and back: Given a G-structure on V , which we write simply as
v ⇝σ(v), the corresponding K-form is V G.
We have to check that the isomorphism
L ⊗K V G →V given by a ⊗w 7→aw transports the standard G-structure on L ⊗K V G to
the original G-structure we started with on V (rather than to some other G-structure on
V ). Under the isomorphism L⊗K V G →V , a tensor P
i ai⊗wi in L⊗K V G is identiﬁed with
P
i aiwi in V , and the standard G-structure on the tensor product is given by σ(P
i ai⊗wi) =
P
i σ(ai)⊗wi (for all σ ∈G), which goes over to P
i σ(ai)wi in V by the isomorphism. Since
the wi’s are in V G, P
i σ(ai)wi = σ(P
i aiwi), so the isomorphism from L ⊗K V G to V does
identify the standard G-structure on L ⊗K V G with the original G-structure on V .
□
The down-to-earth content of Theorem 2.14 is that when G acts semilinearly on V , there
is a spanning set of V over L consisting of G-invariant vectors. Using this is called Galois
descent.
Remark 2.15. Theorem 2.14 is true when L/K is an inﬁnite Galois extension and the
semilinear action G × V →V is continuous, where G has its proﬁnite topology and V has
the discrete topology. See [2, Lemma 5.8.1].
3That V G ⊂W can also be proved using the normal basis theorem.

<!-- page 7 -->
GALOIS DESCENT
7
Corollary 2.16. If V has a G-structure, K-independent vectors in V G are L-independent.
Proof. A K-independent subset of V G can be extended to a K-basis of V G, which is an
L-basis of V (since V G is a K-form of V ), so it is linearly independent over L.
□
Corollary 2.17. For a K-vector space W, with L ⊗K W given its standard G-structure,
(L ⊗K W)G = 1 ⊗W.
Proof. Exercise.
□
Example 2.18. Let X be a ﬁnite set on which the Galois group G = Gal(L/K) acts (by
permutations). Then the space V = Map(X, L) of all functions X →L is an L-vector
space under pointwise operations. A basis of V over L is {δx : x ∈X}. The group G acts
semilinearly on V : for each function f : X →L in V and each σ ∈G, deﬁne σ(f): X →L
so the diagram
X
f
/
σ

L
σ

X
σ(f)
/ L
commutes. This means σ(f)(σ(x)) = σ(f(x)) for all x ∈X, so
σ(f)(x) = σ(f(σ−1(x))).
This equation deﬁnes σ(f) as a function X →L. Let’s check σ: V →V is σ-linear. For
a ∈L, we want to check that σ(af) = σ(a)σ(f). Well, at each x ∈X,
(σ(af))(x) = σ((af)(σ−1(x)))
= σ(af(σ−1(x)))
= σ(a)σ(f(σ−1(x)))
= σ(a)(σ(f)(x)),
so σ(af) = σ(a)σ(f) as functions in Map(X, L). Check σ(δx) = δσ(x).
What is V G? It is natural to guess that V G equals Map(X, K), which is the K-span
of {δx : x ∈X}. As a small piece of evidence, Map(X, K) is a K-subspace of V with
K-dimension #X and dimK(V G) = dimL(V ) = #X too. However, the delta-functions δx
lie in Map(X, K) and σ(δx) = δx only when σ(x) = x. Therefore all the δx’s are in V G only
when G acts trivially on X. So V G is not Map(X, K) if G acts nontrivially on X. In fact,
V G = {f : σ(f) = f}
= {f : σ(f(σ−1(x))) = f(x) for all σ, x}
= {f : σ(f(x)) = f(σ(x)) for all σ, x},
so V G consists of the functions X →L that commute with the G-actions on X and L.
Functions satisfying σ(f(x)) = f(σ(x)) for all σ ∈G and x ∈X are called G-maps (they
respect the G-actions). Because V G spans V over L, every function X →L is an L-linear
combination of G-maps X →L.
If G acts trivially on X then V G = {f : σ(f(x)) = f(x) for all σ, x} = Map(X, K), so a
G-map X →L in this case is just a function X →K.

<!-- page 8 -->
8
KEITH CONRAD
We conclude this section by showing how to interpret Theorem 2.14 in terms of repre-
sentations. (If you don’t know representations of ﬁnite groups, you may want to skip the
rest of this section.) First let’s recall how you could discover that the ring C[G] should be
relevant to representations of G on complex vector spaces. Let’s stare at the formulas
(2.5)
ρ(σ)(cv) = cρ(σ)(v)
and
ρ(σ)(ρ(τ)v) = ρ(στ)(v)
for a representation ρ of G on a complex vector space V (here c ∈C and v ∈V ). Now
abstract these formulas by writing some neutral symbol eσ for ρ(σ) and taking away v:
introduce the C-vector space C[G] = L
σ∈G Ceσ with multiplication rules
(2.6)
eσc = ceσ
and
eσeτ = eστ
inspired by (2.5). Now C[G] is an associative ring with identity, and even a C-algebra since
C commutes with all the basis vectors eσ. We can consider a representation ρ of G on V as
a way of letting the basis vectors eσ act as C-linear maps V →V , by eσv = ρ(σ)(v), and
the conditions (2.5) and (2.6) say precisely that this makes V into a (left) C[G]-module.
Conversely, a left C[G]-module structure on V provides a representation of G on V by
focusing attention on how the eσ’s inside C[G] act on V (which doesn’t lose information
since the eσ’s span V ).
Now let’s look at G-structures on an L-vector space V , where G = Gal(L/K), with the
goal of ﬁnding an abstract ring whose module structures on an L-vector space V are the
same thing as G-structures on V .
A G-structure on V provides us with σ-linear maps
rσ : V →V for all σ ∈G, which means the rσ’s are additive and
(2.7)
r1(v) = v,
rσ(cv) = σ(c)rσ(v),
and
rσ(rτ(v)) = rστ(v)
for all c ∈L and v ∈V . Now let’s wipe v out of these equations and turn the maps rσ into
basis vectors eσ. Deﬁne the L-vector space C(G) = L
σ∈G Leσ and declare multiplication
in C(G) to be given by the rules
(2.8)
e1 = 1,
eσc = σ(c)eσ,
and
eσeτ = eστ
for σ and τ in G and c ∈L.4 This makes C(G) an associative ring with identity e1 (check!)
and C(G) is a K-algebra (since eσc = ceσ when c ∈K). If G is not trivial (that is, L ̸= K),
eσc is not ceσ for c ∈L −K, so C(G) is not an L-algebra (in the same way the quaternions
H are an R-algebra but not a C-algebra even though C ⊂H).
The multiplication rules (2.8) in C(G) are an abstract form of the way a G-structure
behaves, as described in (2.7): a G-structure on V is the same thing as a left C(G)-module
structure on V , where eσ acts on V as the σ-linear map rσ. Explicitly, if we have a G-
structure {rσ} on V then make V into a C(G)-module by the formula
 X
σ∈G
aσeσ
!
(v) =
X
σ∈G
aσrσ(v)
and, conversely, if V has a C(G)-module structure then focusing on how the basis vectors
eσ act on V gives us a G-structure (check speciﬁcally why each eσ is a σ-linear map on
V from the deﬁnition of a C(G)-module structure on V ). Theorem 2.14 therefore says, in
terms of C(G), that the K-forms of V are essentially the same thing as the C(G)-module
structures on V .
4Unlike the group ring C[G], the construction of C(G) depends essentially on G being a Galois group
since we use its action on L in the deﬁnition of the multiplication in (2.8).

<!-- page 9 -->
GALOIS DESCENT
9
The most basic example of a C(G)-module is L, on which G = Gal(L/K) acts by its
very nature as a Galois group and this extends to a C(G)-module structure via the formula
(P
σ∈G aσeσ)(x) = P
σ∈G aσσ(x) for all x ∈L. That every G-structure has an associated
K-form tells us something about C(G)-submodules of a C(G)-module. Let V be a nonzero
C(G)-module (which is a concise way of saying V is a nonzero L-vector space with a G-
structure). The existence of a K-form means V has an L-basis {vi} of G-invariant vectors:
V = L
i∈I Lvi and σ(vi) = vi for all σ ∈G. The line Lvi is preserved under the action
of G and L, hence under the action of C(G) = L
σ∈G Leσ. Therefore each Lvi is a C(G)-
submodule, and vi being G-invariant makes Lvi isomorphic to L as C(G)-modules by the
natural map xvi 7→x. (Warning: a C(G)-linear map is not L-linear since the eσ’s don’t
commute with L, unless G is trivial.) Thus all nonzero C(G)-modules are direct sums of
copies of L as a C(G)-module. This in fact is another way of thinking about the existence
of K-forms.
Indeed, suppose we knew (by some other method) that every nonzero C(G)-module is a
direct sum of C(G)-submodules that are each isomorphic to L as a C(G)-module. Then for
each nonzero L-vector space V with a G-structure, view V as a C(G)-module and break
it up as L
i∈I Vi where Vi ∼= L as C(G)-modules.
Let fi : L →Vi be a C(G)-module
isomorphism and set vi = fi(1). Then for σ ∈G, σ(vi) = σ(fi(1)) = fi(σ(1)) = fi(1) = vi,
so vi is a G-invariant vector. Since Lvi ⊂Vi and both are L-vector spaces of the same
ﬁnite K-dimension (because fi is a K-linear isomorphism, forgetting a little structure in
the process), Lvi = Vi. Now the direct sum decomposition V = L
i∈I Lvi reveals a K-form
for V , namely W = L
i∈I Kvi.
3. Applications to Vector Spaces
Our ﬁrst application of Galois descent is to systems of linear equations. If the equations
have coeﬃcients in K and there is a nonzero solution over L then there is also one over K.
Theorem 3.1. For a homogeneous system of linear equations in n unknowns with coef-
ﬁcients in K, the solutions in Ln are L-linear combinations of the solutions in Kn. In
particular, if there is a nonzero L-solution then there is a nonzero K-solution.
Proof. Write the system of linear equations in the form Ax = 0, where A is an m×n matrix
with entries in K (m being the number of equations). Let V ⊂Ln be the L-solutions of the
system: V = {v ∈Ln : Av = 0}. There is a standard semilinear (coordinatewise) action of
G on Ln, and because A has entries in K the G-action preserves V : if v ∈V then σ(v) ∈V
because σ(Av) = A(σ(v)) and σ(0) = 0. So we get a coordinatewise G-structure on V , and
by Theorem 2.14 V is spanned over L by its G-ﬁxed set V G = V ∩(Ln)G = V ∩Kn, which
are the solutions to Ax = 0 in Kn.
□
Theorem 3.1 is true without L/K being Galois: for a K-linear map A: Kn →Km, the
map 1 ⊗A: Ln →Lm satisﬁes im(1 ⊗A) = L · im(A).
Next we describe how descent behaves on subspaces: if V ′ ⊂V and we have a G-structure
on V , when does V ′ have a K-form in V G? The answer is connected to the preservation of
V ′ by the G-structure on V .
Theorem 3.2. Let V be an L-vector space with a G-structure. For an L-subspace V ′ ⊂V ,
the following conditions are equivalent:
(1) V ′ has an L-spanning set in V G,
(2) σ(V ′) ⊂V ′ for all σ ∈G,

<!-- page 10 -->
10
KEITH CONRAD
(3) σ(V ′) = V ′ for all σ ∈G,
(4) V ′ has a K-form in V G.
When these hold, the only K-form of V ′ in V G is V ′ ∩V G. If dimL(V ′) < ∞, these
conditions are the same as dimK(V ′ ∩V G) = dimL(V ′).
Proof. Everything is obvious if V ′ = 0, so we may take V ′ ̸= 0.
(1) ⇒(2): Suppose V ′ = P Lvi where vi ∈V G. Then for σ ∈G, σ(V ′) ⊂P σ(L)vi =
P Lvi = V ′.
(2) ⇒(1): Suppose σ(V ′) ⊂V ′ for all σ ∈G. Then the given G-structure on V is a
G-structure on V ′, so by Theorem 2.14 V ′ has an L-spanning set in (V ′)G ⊂V G.
(2) ⇒(3): Using σ−1 in place of σ, we have σ−1(V ′) ⊂V ′ so V ′ ⊂σ(V ′).
Thus
σ(V ′) = V ′ for all σ ∈G.
(3) ⇒(2): Obvious.
(3) ⇒(4): The G-structure on V is a G-structure on V ′, so (V ′)G is a K-form of V ′ and
(V ′)G ⊂V G.
(4) ⇒(2): For a K-form W ′ of V ′ in V G, V ′ = LW ′, so σ(V ′) ⊂Lσ(W ′) = LW ′ = V ′.
When these conditions hold, (V ′)G is a K-form of V ′, and (V ′)G = V ′ ∩V G. Suppose W ′
is a K-form of V ′ in V G. We want to show W ′ = (V ′)G. The natural map L ⊗K W ′ →V ′
given by a ⊗w′ 7→aw′ is an L-vector space isomorphism, and the transported G-structure
on V ′ from the standard G-structure on L ⊗K W ′ through this isomorphism is
σW ′(aw′) = σ(a)w′
for a ∈L and w′ ∈W ′. Since W ′ ⊂V G, in terms of the original G-structure on V we
have σ(a)w′ = σ(a)σ(w′) = σ(aw′) = σV G(aw′) = σ(V ′)G(aw′), so σW ′ = σ(V ′)G. By the
one-to-one correspondence between K-forms and G-structures on V ′, W ′ = (V ′)G.
Now assume dimL(V ′) is ﬁnite. We want to show the four conditions are equivalent to
dimK(V ′ ∩V G) = dimL(V ′). We will show this dimension constraint is equivalent to (1).
Let d = dimL(V ′).
Suppose (1) holds.
If V ′ has an L-spanning set in V G it has an L-basis in V G, say
v1, . . . , vd. Then for v′ ∈V ′, write v′ = Pd
i=1 aivi with ai ∈L. If v′ ∈V G too, then for
σ ∈G,
v′ = σ(v′) =
d
X
i=1
σ(ai)vi,
so linear independence of the vi’s over L implies ai = σ(ai) for all i (and σ), so ai ∈K
for all i. Thus v′ ∈Pd
i=1 Kvi, so V ′ ∩V G ⊂Pd
i=1 Kvi. The reverse inclusion is clear, so
dimK(V ′ ∩V G) = d = dimL(V ′).
Conversely, assume dimK(V ′ ∩V G) = dimL(V ′) and let {v1, . . . , vd} be a K-basis of
V ′ ∩V G. This basis has size d because of the dimension constraint. The vi’s are a K-
linearly independent set, so they are L-linearly independent since V G is a K-form of V .
Then P
i Lvi has L-dimension d and lies in V ′, whose L-dimension is d, so P
i Lvi = V ′,
which is condition (1).
□
Remark 3.3. Since K-independent vectors in V G are L-independent, for all V ′ we have
dimK(V ′ ∩V G) ≤dimL(V ′). Thus the dimension condition in Theorem 3.2 says V ′ ∩V G
has its biggest possible K-dimension.

<!-- page 11 -->
GALOIS DESCENT
11
Two conjugations on a complex vector space are related to each other by an automorphism
of the vector space. More generally, the next theorem says two G-structures on an L-vector
space are linked to each other by an automorphism of the vector space.
Theorem 3.4. Let {rσ} and {r′
σ} be two G-structures on an L-vector space V ̸= 0. There
is a ϕ ∈GL(V ) such that r′
σ = ϕrσϕ−1 for all σ ∈G: the diagram
(3.1)
V
ϕ
/
rσ

V
r′
σ

V
ϕ
/ V
commutes for all σ ∈G.
Here and later, GL(V ) means automorphisms of V as an L-vector space.
Proof. Let W = {v ∈V : rσ(v) = v for all σ ∈G} be the K-form of V for {rσ}. (It would
be bad to write this as V G since there are two G-structures we are dealing with on V and
thus the notation V G would be ambiguous.) Let W ′ = {v ∈V : r′
σ(v) = v for all σ ∈G}
be the K-form of V for {r′
σ}. The two diagrams
L ⊗K W
f
/
σW

V
rσ

L ⊗K W
f
/ V
L ⊗K W ′
f′
/
σW ′

V
r′
σ

L ⊗K W ′
f′
/ V
commute for all σ ∈G, where f and f′ are the natural L-linear maps (isomorphisms).
Since f and f′ are isomorphisms, dimK(W) = dimL(V ) = dimK(W ′) (these might be
inﬁnite cardinal numbers). Therefore there is a K-linear isomorphism ψ: W →W ′, its base
extension 1 ⊗ψ: L ⊗K W →L ⊗K W ′ is an L-linear isomorphism, and the diagram
L ⊗K W
1⊗ψ /
σW

L ⊗K W ′
σW ′

L ⊗K W
1⊗ψ
/ L ⊗K W ′
commutes for all σ ∈G: on a simple tensor a ⊗w, going along the top and right or
along the left and bottom sends this simple tensor to σ(a) ⊗ψ(w). Now combine the three
commutative diagrams to get the commutative diagram
V
f−1/
rσ

L ⊗K W
σW

1⊗ψ / L ⊗K W ′
σW ′

f′
/ V
r′
σ

V
f−1/ L ⊗K W
1⊗ψ
/ L ⊗K W ′
f′
/ V
for every σ ∈G.
The maps along the top and bottom don’t involve σ, and are all L-
linear isomorphisms. Call the (common) composite map along the top and bottom ϕ, so
ϕ ∈GL(V ), and remove the middle vertical maps to be left with a commutative diagram
of the form (3.1).
□

<!-- page 12 -->
12
KEITH CONRAD
Corollary 3.5. Let V be an L-vector space with two K-forms W and W ′. Let {σW } and
{σW ′} be the corresponding G-structures on V . There is ϕ ∈GL(V ) such that ϕ(W) = W ′
and the diagram
V
ϕ
/
σW

V
σW ′

V
ϕ
/ V
commutes for all σ ∈G.
Proof. By Theorem 3.4, there is ϕ ∈GL(V ) such that
V
ϕ
/
σW

V
σW ′

V
ϕ
/ V
commutes for all σ ∈G.
It remains to check ϕ(W) = W ′. We have W = {v ∈V : σW (v) = v for all σ ∈G}
and W ′ = {v ∈V : σW ′(v) = v for all σ ∈G}. So for w ∈W and σ ∈G, σW ′(ϕ(w)) =
ϕ(σW (w)) = ϕ(w). Thus ϕ(w) ∈W ′, so ϕ(W) ⊂W ′. For w′ ∈W ′, write w′ = ϕ(v) with
v ∈V . From σW ′(w′) = w′, σW ′(ϕ(v)) = ϕ(v), so ϕ(σW (v)) = ϕ(v). Since ϕ is injective,
σW (v) = v for all σ, so v ∈W. Thus W ′ ⊂ϕ(W).
□
Theorem 3.6. Let V1 and V2 be L-vector spaces equipped with G-structures. Let W1 and
W2 be the corresponding K-forms of V1 and V2. An L-linear map Φ: V1 →V2 is the L-linear
base extension of a K-linear map ϕ: W1 →W2 if and only if the diagram
V1
Φ
/
σW1

V2
σW2

V1
Φ
/ V2
commutes for all σ ∈G. Equivalently, the L-vector space HomL(V1, V2) has a G-structure
given by
σ(Φ) := σW2 ◦Φ ◦σ−1
W1
with corresponding K-form HomK(W1, W2).
Proof. Exercise.
□
We conclude this section with a reinterpretation of Theorem 3.4 in terms of modules, using
the ring C(G) = L
σ∈G Leσ introduced at the end of Section 2. We saw there that each
nonzero C(G)-module is a direct sum of copies of L as a C(G)-module. By the invariance
of dimension of vector spaces, this means a C(G)-module is completely determined up to
isomorphism by its L-dimension. In other words, the end of Section 2 shows that for a
nonzero L-vector space V , all C(G)-module structures on V are isomorphic to each other:
there is a C(G)-linear map ϕ: V →V that turns one C(G)-module structure into the other.
This is the same as saying ϕ is a L-linear automorphism of V such that ϕ(eσv) = eσϕ(v) (be
careful only to view V as a left L-vector space, considering how multiplication of it with G
inside of C(G) is twisted), and that equation for all σ is precisely the conclusion of Theorem
3.4 except it is given in the terminology of G-structures rather than C(G)-modules. So we

<!-- page 13 -->
GALOIS DESCENT
13
already had a proof of Theorem 3.4 at the end of Section 2 and it’s a lot more conceptual
than the proof we wrote out for Theorem 3.4.
This illustrates how useful it can be to
interpret G-structures as C(G)-module structures.
4. Applications to Ideals
Our next set of applications of Galois descent concern ideals in L[X1, . . . , Xn], which we
will abbreviate to L[X]. A basic question is whether an ideal in this ring is generated by
polynomials in K[X]. Let V = L[X] and let G act on V by acting on coeﬃcients. This
action is a G-structure on V with corresponding K-form W := V G = K[X]. For an ideal I
of L[X], IG = I ∩K[X] is an ideal in K[X]. Say an ideal I ⊂L[X] is deﬁned over K if it
has a generating set (as an ideal!) in K[X].
Example 4.1. In C[X, Y ], I = (X + iY 2, X −iY 2) is deﬁned over R since I = (X, Y 2).
Theorem 4.2. For an ideal I ⊂L[X], the following conditions are equivalent:
(1) I is deﬁned over K,
(2) σ(I) ⊂I for all σ ∈G,
(3) σ(I) = I for all σ ∈G.
Proof. It is trivial that (1) implies (2) since a generating set of I in K[X] is not changed
by σ. Since (2) is stated over all σ, from σ−1(I) ⊂I for all σ we get I ⊂σ(I) for all σ, so
σ(I) = I for all σ, which is (3). Finally, assuming (3), since σ(I) = I the Galois group G
acts semilinearly on I as an L-vector space, so by Galois descent on I, I has a spanning set
as an L-vector space in IG = I ∩K[X] ⊂K[X]. Since I is an ideal in L[X], an L-vector
space spanning set of I is also a generating set of I as an ideal.
□
Here is an example where L/K is non-Galois and Theorem 4.2 breaks down. Let K =
Fp(T), L = Fp(
p√
T), and I = (X −
p√
T) in L[X]. Then σ(I) = I for all σ ∈AutK(L)
(which is a trivial group), but I has no generator in K[X]. In fact, I ∩K[X] = (Xp −T),
so the ideal in L[X] generated by I ∩K[X] is smaller than I.
Remark 4.3. By Hilbert’s basis theorem,
I ∩K[X] = (f1, . . . , fr) =
r
X
i=1
K[X]fi
for some fi’s in K[X]. If I is deﬁned over K then by the proof of Theorem 4.2, I is spanned
as an L-vector space by polynomials in I ∩K[X]: I = P
j Lhj for some hj ∈I ∩K[X]. Each
hj is a K[X]-linear combination of the fi’s, so I ⊂Pr
i=1 L[X]fi and the reverse inclusion
holds since I is an ideal, so I = Pr
i=1 L[X]fi. That is, an ideal I in L[X] that is deﬁned
over K is ﬁnitely generated over L[X] by any ﬁnite set of ideal generators of I ∩K[X].
The special case of (3) ⇒(1) in Theorem 4.2 in one variable can be proved using Hilbert’s
Theorem 90 instead of Galois descent. Let I be an ideal in L[X]. Since L[X] is a PID,
I = (f) for some f ∈L[X]. Then τ(I) = (τ(f)) for all τ ∈G. Saying τ(I) = I for all τ ∈G
is equivalent to τ(f) = λτf for some λτ ∈L×. Apply an arbitrary σ ∈G to that equation:
σ(τ(f)) = σ(λτ)σ(f), so (στ)(f) = σ(λτ)λσf. Also (στ)(f) = λστf, so λστf = σ(λτ)λσf,
so λστ = σ(λτ)λσ since f ̸= 0. Hence the numbers {λσ : σ ∈G} are a 1-cocycle G →L×.
By the multiplicative form of Theorem 90, λσ = σ(α)/α for some α ∈L× and all σ ∈G, so
σ(f) = (σ(α)/α)f, so σ(f/α) = f/α for all σ ∈G. Thus f/α ∈K[X] and (f/α) = (f) as
ideals in L[X]. So (f) is deﬁned over K.

<!-- page 14 -->
14
KEITH CONRAD
The relations between Galois descent and cohomology go further. Let V be an L-vector
space with a G-structure. A 1-cocycle on V is a function c: G →V such that c(στ) =
c(σ) + σ(c(τ)).
Example 4.4. Fixing v ∈V , c(σ) = σ(v) −v is a 1-cocycle since
c(σ) + σ(c(τ)) = (σ(v) −v) + σ(τ(v) −v) = (στ)(v) −v = c(στ).
The additive form of Theorem 90 says all 1-cocycles c: G →L look like the example:
c(σ) = σ(α) −α for some α ∈L. Let’s recall a proof. For x ∈L, set y = P
τ∈G c(τ)τ(x).
For σ ∈G, σ(y) = P
τ σ(c(τ))(στ)(x) = P
τ(c(στ)−c(σ))(στ)(x) = P
τ(c(τ)−c(σ))τ(x) =
y −c(σ)TrL/K(x). Choose x so TrL/K(x) ̸= 0. Then c(σ) = z −σ(z) for z = y/TrL/K(x).
Set α = −z, so c(σ) = σ(α) −α.
Using Galois descent we can extend this from cocycles in L to cocycles in L-vector spaces
with a G-structure.
Theorem 4.5. For each L-vector space V with a G-structure, every 1-cocycle on V has the
form c(σ) = σ(v) −v for some v ∈V .
Proof. We may suppose V ̸= 0. Let {vi} be a K-basis of V G, so by Galois descent
V =
M
i
Lvi.
For a 1-cocycle c: G →V , write c(σ) = P
i aσ,ivi, where aσ,i ∈L.
Then the cocycle
condition c(στ) = c(σ) + σ(c(τ)) means
X
i
aστ,ivi =
X
i
aσ,ivi + σ
 X
i
aτ,ivi
!
=
X
i
aσ,ivi +
X
i
σ(aτ,i)vi
=
X
i
(aσ,i + σ(aτ,i)) vi,
so for each i, aστ,i = aσ,i+σ(aτ,i). Thus for each i, σ 7→aσ,i is a 1-cocycle in L. By Theorem
90, for each i there is bi ∈L such that aσ,i = σ(bi) −bi for all σ. Since aσ,i = 0 for all but
ﬁnitely many i, we can use bi = 0 for all but ﬁnitely many i. Then
c(σ) =
X
i
(σ(bi) −bi)vi =
X
i
σ(bi)vi −
X
i
bivi = σ(v) −v,
where v = P
i bivi.
□
Here is an important application of Theorem 4.5 to the Galois action on quotient rings
of L[X].
Theorem 4.6. Let I ⊂L[X] be an ideal deﬁned over K, so L[X]/I has a G-structure by
σ(f + I) = σ(f) + I (Lemma 2.11). For each f ∈L[X], the following are equivalent:
(1) σ(f) ≡f mod I for all σ ∈G,
(2) f ≡g mod I for some g ∈K[X].
Proof. It is trivial that the second condition implies the ﬁrst. For the more interesting
reverse direction, assume σ(f) ≡f mod I for all σ ∈G. Deﬁne c: G →I by c(σ) = σ(f)−f.

<!-- page 15 -->
GALOIS DESCENT
15
By a computation, c(σ) + σ(c(τ)) = c(στ) for all σ and τ in G, so c is a 1-cocycle in the
L-vector space I. By Theorem 4.5, c(σ) = σ(h) −h for some h ∈I, so
σ(f) −f = σ(h) −h
for all σ ∈G. Therefore f −h is ﬁxed by all σ ∈G, so f −h ∈K[X]. Set g = f −h, so
f ≡g mod I and g ∈K[X].
□
Even though ideals in L[X] are ﬁnitely generated as ideals, they are inﬁnite-dimensional
as L-vector spaces (except for the zero ideal), so it is crucial that Theorem 4.5 applies to
general vector spaces, not just ﬁnite-dimensional vector spaces.
These Galois descent features on ideals lead to applications in algebraic geometry. We
present two of them.
Theorem 4.7. Let V ⊂Ld be the zero set of f1, . . . , fr ∈K[X]. The ideal of all polynomials
in L[X] that vanish in Ld where the fi’s vanish has a generating set in K[X]. Equivalently,
the ideal I(V ) = {g ∈L[X] : g(P) = 0 for all P ∈V } is deﬁned over K.
Note that before Theorem 4.7 we’ve written V for a vector space. Now V is denoting an
algebraic variety, so it is deﬁnitely not a vector space in general!
There is nontrivial content to Theorem 4.7 because the ideal I(V ) need not be generated
by the fi’s themselves. For instance, in C2 let V be the zero set of f1 = X3
1 and f2 =
X2
1 −X1X2. Then I(V ) = (X1) whereas the ideal (f1, f2) is strictly contained in X1 (the
polynomials in the ideal (f1, f2) have no X1-term, but X1 of course does).
Proof. For P ∈V , fi(P) = 0 for all i, so fi(σ(P)) = 0 for all σ ∈G. Thus σ(P) ∈V , so
σ(V ) ⊂V for all σ ∈G, hence σ(V ) = V for all σ ∈G.
To show I(V ) is deﬁned over K, we show σ(I(V )) ⊂I(V ) for all σ ∈G. Pick f ∈I(V ) ⊂
L[X]. For σ ∈G and P ∈V , set Q = σ−1(P) ∈V . Then f(Q) = 0, and applying σ to
this gives (σf)(σ(Q)) = 0, so (σf)(P) = 0. Thus σ(f) ∈I(V ), so σ(I(V )) ⊂I(V ) for all
σ ∈I(V ). Therefore I(V ) is deﬁned over K.
□
Example 4.8. If V ⊂Cd is the zero set of some real polynomials f1, . . . , fr, then the ideal
I(V ) of complex polynomials vanishing on V is generated by real polynomials.
The proof of Theorem 4.7 is not constructive, so we don’t get a method to write down
generators of I(V ) in K[X] from the original polynomials fi in K[X] that deﬁne V .
Theorem 4.9. Let I ⊂L[X] be a homogeneous prime ideal deﬁned over K. Then L(I)G =
{g/h : g, h ∈K[X], h ̸∈I, g and h are homogeneous of equal degree}.
Proof. The inclusion ⊃is obvious. We work out the inclusion ⊂. Suppose g, h ∈L[X] are
homogeneous of equal degree, h ̸∈I, and g/h ∈L(I)G, which means σ(g/h) = g/h for all
σ in G. For σ ∈G, since h ̸∈I and σ(I) = I, σ(h) ̸∈I. Then Q
σ∈G σ(h) ̸∈I since I
is prime, and this product is in K[X] and is divisible by h. Write this product as hk, so
k ∈L[X]. Since g/h = gk/hk, by renaming gk as g and hk as h we don’t change g/h but
can now take h ∈K[X]. Then σ(g/h) = σ(g)/h, so σ(g) = g in L(I). Both σ(g) and g are
in L[I] = L[X]/I, so
σ(g) ≡g mod I
for all σ ∈G. Therefore Theorem 4.6 tells us g ≡eg mod I for some eg ∈K[X]. Since
g −eg ∈I, I is a homogeneous ideal, and g is a homogeneous polynomial, the homogeneous
parts of eg not of degree deg g are in I. Therefore without loss of generality eg is homogeneous
of the same degree as g. So g/h = eg/h in L(I), and eg and h are in K[I].
□

<!-- page 16 -->
16
KEITH CONRAD
5. Applications to Algebras
Our ﬁnal set of applications of Galois descent is to L-algebras. We understand the term
L-algebra to mean an L-vector space equipped with an L-bilinear multiplication law. We
will not assume the algebra is associative. Examples of L-algebras include Mn(L), L[X],
and a Lie algebra over L (which is not associative) such as gln(L). For a K-algebra A,
L ⊗K A is an L-algebra.
Deﬁnition 5.1. A K-form of an L-algebra A is a K-subalgebra A of A such that the
natural map L ⊗K A →A given by x ⊗a 7→xa is an isomorphism of L-algebras.
A K-form of an L-algebra is a K-form as an L-vector space, but it’s more than that: the
algebra structure needs to be respected.
If A is an L-algebra and A is a K-form of A then A is associative if and only if A is
associative and A is a Lie algebra over L if and only if A is a Lie algebra over K. The
reason is that the relevant properties (associativity or the Jacobi identity) are true on an
L-algebra if and only if they are true on an L-basis, and we can use a K-basis of A as an
L-basis of A.
Example 5.2. Two R-forms of the C-algebra M2(C) are M2(R) and the quaternions H,
viewed inside M2(C) by a+bi+cj +dk 7→( a+bi −c−di
c−di
a−bi ). Both are 4-dimensional R-algebras
whose standard R-basis is a C-basis of M2(C).
Since M2(R) and H are not isomorphic R-algebras (H is a division ring and M2(R)
is not), diﬀerent K-forms of an L-algebra need not be isomorphic K-algebras. This is an
important contrast with the linear theory (Theorem 3.4), where all K-forms of an L-vector
space are isomorphic as K-vector spaces. When working with algebras we have to keep tabs
on the multiplicative structure too, and that creates new possibilities.
As with K-forms of an L-vector space, K-forms of an L-algebra correspond to an ap-
propriate system of semilinear G-actions on the algebra. A G-structure on an L-algebra
A is a collection of maps rσ : A →A for all σ ∈G such that rσ is a σ-linear K-algebra
automorphism (not L-algebra automorphism!), ridL = idA, and rσ ◦rσ′ = rσσ′.
Example 5.3. The entrywise or coeﬃcientwise G-actions on Mn(L), gln(L), and L[X] as
L-vector spaces are also G-structures as L-algebras.
Example 5.4. If A is a K-algebra then the L-algebra L ⊗K A gets a standard G-structure
by
σA
 X
i
ci ⊗ai
!
:=
X
σ(ci) ⊗ai.
This is σ-linear (σA is additive and σA(ct) = σ(c)σA(t) for all c ∈L and t ∈L ⊗K A) and
also σA is multiplicative (σA(tt′) = σA(t)σA(t′)), so σA is a K-algebra automorphism of
L ⊗K A. Thinking of A just as a K-vector space, by the proof of Theorem 2.14 we have
(L ⊗K A)G = 1 ⊗A.
If A is an L-algebra with a G-structure, the ﬁxed set AG is a K-form of A as vector
spaces by Theorem 2.14. The space AG is also a K-algebra and the L-linear isomorphism
L ⊗K AG →A is an isomorphism of L-algebras, not just of L-vector spaces. So AG is a
K-form of A as an L-algebra. Thus G-structures leads to K-forms.
Conversely, if A is an L-algebra with a K-form A, the natural map L ⊗K A →A is an
L-algebra isomorphism and the standard G-structure on L ⊗K A in Example 5.4 can be

<!-- page 17 -->
GALOIS DESCENT
17
transported to a G-structure on A whose ﬁxed set is A. (This is an algebra analogue of
Example 2.10.) So K-forms on an L-algebra A leads to G-structures on A.
It can be no surprise at this point that Theorem 2.14 has an analogue for algebras: the
K-forms of A (as an algebra) are in one-to-one correspondence with the G-structures on A
(as an algebra). One just reads through the proof of Theorem 2.14 and checks the maps
constructed there between algebras are not just semilinear but also multiplicative.
Example 5.5. With respect to their standard G-structures, the K-forms of the L-algebras
Mn(L), gln(L), and L[X] are Mn(K), gln(K), and K[X].
For a C-algebra A, a Gal(C/R)-structure is determined by a conjugation on the algebra.
This is a function c: A →A such that c is semilinear with respect to complex conjugation
on C, is an R-algebra automorphism of A, and c2 = idA.
Example 5.6. The C-algebra M2(C) has R-forms M2(R) and H (embedded in M2(C) as
in Example 5.2). These are each the ﬁxed points of one of the following two conjugations
on M2(C):
c

α
β
γ
δ

=

α
β
γ
δ

,
c′

α
β
γ
δ

=

δ
−γ
−β
α

.
Note c′, whose ﬁxed set is H, is not an extension of the usual conjugation on quaternions,
as that doesn’t ﬁx all of H (also, the usual quaternionic conjugation reverses the order of
multiplication).
Let A be an L-algebra and A and A′ be two K-forms of A (as an L-algebra). Each
K-form provides A with a G-structure, say {rσ} and {r′
σ} for A and A′. Call A and A′
equivalent K-forms of A if there is a K-algebra isomorphism ψ: A →A′ commuting with
the G-actions: ψ(rσ(a)) = r′
σ(ψ(a)) for all a ∈A and σ ∈G. Because of examples like
M2(R) and H inside M2(C), not all K-forms of an L-algebra are equivalent, as the K-
forms may not be isomorphic K-algebras. The equivalence of K-forms of an L-algebra can
be described by the algebra analogue of Theorem 3.4 (where all K-forms are equivalent,
using an obvious notion of equivalence for vector spaces with G-structure):
Theorem 5.7. Let A be an L-algebra with K-forms A and A′. Write the corresponding
G-structures on A as {rσ} and {r′
σ}. Then A and A′ are equivalent K-forms of A if and
only if there is an L-algebra automorphism ϕ of A such that r′
σ = ϕrσϕ−1 for all σ ∈G:
the diagram
A
ϕ
/
rσ

A
r′
σ

A
ϕ
/ A
commutes for all σ ∈G.
Proof. (⇐) If there is such a ϕ then ϕ is a K-algebra automorphism of A, and for a ∈A,
ϕ(a) = r′
σ(ϕ(a)) for all σ, so ϕ(a) ∈A′. If ϕ(a) ∈A′ with a ∈A, then ϕ(rσ(a)) = ϕ(a), so
rσ(a) = a for all σ, so a ∈A. Thus ϕ(A) = A′, so ϕ restricts to a K-algebra isomorphism
from A to A′.
(⇒) Suppose there is a K-algebra isomorphism ψ: A →A′ such that ψ(rσ(a)) = r′
σ(ψ(a))
for all a ∈A. Base extend ψ to 1 ⊗ψ, an L-algebra isomorphism from L ⊗K A to L ⊗K A′.
These base extensions are both L-algebra isomorphic to A in a natural way, so 1 ⊗ψ can

<!-- page 18 -->
18
KEITH CONRAD
be regarded as an L-algebra automorphism ϕ of A. It is left to the reader to check with
this ϕ that the diagram commutes.
□
For our last application of Galois descent, we work out the structure of the L-algebra
L⊗KL, where scaling by L comes in the ﬁrst component: c(x⊗y) = cx⊗y on simple tensors.
For σ ∈G, let Lσ be L as a ring with L-scaling given by the twisted rule c · x = σ(c)x.
Then Lσ is an L-algebra. Set
A =
Y
σ∈G
Lσ,
whose elements are written in tuple notation as (xσ)σ. This is an L-algebra using compo-
nentwise operations. In particular, scaling by L on A is given by
c · (xσ)σ = (c · xσ)σ = (σ(c)xσ)σ.
Let τ ∈G act on A by
τ((xσ)σ) = (xστ)σ = (yσ)σ,
where yσ = xστ. To show this is a G-structure on A, it is easy to see that τ acts additively
and multiplicatively on A, and the identity of G acts on A as the identity map. For τ1 and
τ2 in G,
τ1(τ2((xσ)σ)) = τ1((yσ)σ) where yσ = xστ2
= (zσ),
where zσ = yστ1 = xστ1τ2. So
τ1(τ2((xσ)σ)) = (xστ1τ2)
= (τ1τ2)((xσ)σ).
Thus composing the actions of τ1 and τ2 on A gives the action of τ1τ2. Also
τ(c · (xσ)σ) = τ((σ(c)xσ)σ)
= (yσ)σ,
where yσ = (στ)(c)xστ = σ(τ(c))xστ and
τ(c)(τ((xσ)σ)) = τ(c)((xστ)σ)
= (τ(c) · xστ)σ
= (σ(τ(c))xστ)σ
= (yσ)σ,
so τ acts τ-linearly on A.
The ﬁxed set AG for this G-structure on A is {(xσ)σ : τ((xσ)σ) = (xσ)σ for all τ ∈G},
which amounts to xστ = xσ for all σ and τ, so all the coordinates are the same element,
say x, of L: AG = {(x)σ : x ∈L}. Thus L ∼= AG as K-algebras by x 7→(x)σ. (This map is
K-linear but not L-linear if #G > 1.)
Since L ∼= AG as K-algebras, L⊗K L ∼= L⊗K AG as L-algebras by α⊗β 7→α⊗(β)σ. By
Galois descent, L ⊗K AG ∼= A as L-algebras by α ⊗(β)σ 7→α · (β)σ = (α · β)σ = (σ(α)β)σ,
so
(5.1)
L ⊗K L ∼= A =
Y
σ∈G
Lσ

<!-- page 19 -->
GALOIS DESCENT
19
by α ⊗β 7→(σ(α)β)σ.
For an application of (5.1) to a proof of the normal basis theorem, see [4].
References
[1] N. Jacobson, “Lie Algebras,” Dover, New York, 1979.
[2] J. H. Silverman, “The Arithmetic of Elliptic Curves,” Springer-Verlag, New York, 1986.
[3] W. Waterhouse, “Introduction to Aﬃne Group Schemes,” Springer-Verlag, New York, 1979.
[4] W. Waterhouse, The Normal Basis Theorem, Amer. Math. Monthly 86 (1979), 212.
[5] D. J. Winter, “The Structure of Fields,” Springer-Verlag, New York, 1974.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*