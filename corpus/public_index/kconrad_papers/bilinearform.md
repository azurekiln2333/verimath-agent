# Bilinear Forms

> **Source**: https://kconrad.math.uconn.edu/blurbs/bilinearform.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
BILINEAR FORMS
KEITH CONRAD
The geometry of Rn is controlled algebraically by the dot product. We will abstract
the dot product on Rn to a bilinear form on a vector space and study algebraic and geo-
metric notions related to bilinear forms (especially the concept of orthogonality in all its
manifestations: orthogonal vectors, orthogonal subspaces, and orthogonal bases).
Section 1 deﬁnes a bilinear form on a vector space and oﬀers examples of the two most
common types of bilinear forms: symmetric and alternating bilinear forms. In Section 2
we will see how a bilinear form looks in coordinates. Section 3 describes the important
condition of nondegeneracy for a bilinear form. Orthogonal bases for symmetric bilinear
forms are the subject of Section 4.
Symplectic bases for alternating bilinear forms are
discussed in Section 5. Quadratic forms are in Section 6 (characteristic not 2) and Section
7 (characteristic 2). The tensor product viewpoint on bilinear forms is brieﬂy discussed in
Section 8.
Vector spaces in Section 1 are arbitrary, but starting in Section 2 we will assume they are
ﬁnite-dimensional. It is assumed that the reader is comfortable with abstract vector spaces
and how to use bases of (ﬁnite-dimensional) vector spaces to turn elements of a vector space
into column vectors and linear maps between vector spaces into matrices. It is also assumed
that the reader is familiar with duality on ﬁnite-dimensional vector spaces: dual spaces, dual
bases, the dual of a linear map, and the natural isomorphism of ﬁnite-dimensional vector
spaces with their double duals (which identiﬁes the double dual of a basis with itself and
the double dual of a linear map with itself). For a vector space V we denote its dual space
as V ∨. The dual basis of a basis {e1, . . . , en} of V is denoted {e∨
1 , . . . , e∨
n}, so the e∨
i ’s are
the coordinate functions on V relative to that basis: e∨
i (ej) is 1 for i = j and 0 for i ̸= j.
Although V is naturally isomorphic to V ∨∨, students are always cautioned against iden-
tifying V with V ∨, since “there is no natural isomorphism.” In a nutshell, the subject of
bilinear forms is about what happens if we make an identiﬁcation of V with V ∨and keep
track of it. Diﬀerent identiﬁcations have diﬀerent geometric properties.
1. Definitions and examples
Deﬁnition 1.1. Let F be a ﬁeld and V be a vector space over F. A bilinear form on V is
a function B : V × V →F that is linear in each variable when the other one is ﬁxed. That
is,
B(v + v′, w) = B(v, w) + B(v′, w),
B(cv, w) = cB(v, w)
for all v, v′, w ∈V and c ∈F, and
B(v, w + w′) = B(v, w) + B(v, w′),
B(v, cw) = cB(v, w),
for all v, w, w′ ∈V and c ∈F.
We call B symmetric when
B(v, w) = B(w, v) for all v, w ∈V
1

<!-- page 2 -->
2
KEITH CONRAD
and skew-symmetric when
B(v, w) = −B(w, v) for all v, w ∈V.
We call B alternating when
B(v, v) = 0 for all v ∈V.
A bilinear space is a vector space equipped with a speciﬁc choice of bilinear form. We call
a bilinear space symmetric, skew-symmetric, or alternating when the chosen bilinear form
has that corresponding property.
A common synonym for skew-symmetric is anti-symmetric.
Example 1.2. The dot product v · w on Rn is a symmetric bilinear form.
Example 1.3. For a ﬁxed matrix A ∈Mn(R), the function f(v, w) = v · Aw on Rn is a
bilinear form, but not necessarily symmetric like the dot product. All examples of bilinear
forms are essentially generalizations of this construction.
Example 1.4. For any ﬁeld F, viewed as a 1-dimensional vector space over itself, multipli-
cation m: F ×F →F is a symmetric bilinear form and not alternating. It is skew-symmetric
when F has characteristic 2.
Example 1.5. A skew-symmetric and alternating bilinear form on R2 is
B((x, y), (x′, y′)) := xy′ −x′y = det

x
x′
y
y′

.
For example, B((2, 1), (3, 4)) = 5 and B((2, 1), (2, 1)) = 0. Viewing R2 as C by (x, y) ↔
x + iy, B(z, w) = Im(zw) = −Im(zw) for complex numbers z and w.
Among the three types of bilinear forms we have deﬁned (symmetric, skew-symmetric,
alternating), the ﬁrst and third types are more basic than the second. In fact, we now show
that a skew-symmetric bilinear form is just another name for a symmetric or an alternating
bilinear form, depending on whether or not the characteristic of the ﬁeld is 2.
Theorem 1.6. In all characteristics, an alternating bilinear form is skew-symmetric. In
characteristic not 2, a bilinear form is skew-symmetric if and only if it is alternating. In
characteristic 2, a bilinear form is skew-symmetric if and only if it is symmetric.
Proof. When B is alternating and v, w ∈V , expanding the right side of the equation
0 = B(v + w, v + w) shows
0 = B(v, v) + B(v, w) + B(w, v) + B(w, w) = B(v, w) + B(w, v),
so B(v, w) = −B(w, v).
Therefore alternating bilinear forms are skew-symmetric in all
characteristics (even in characteristic 2).
Outside of characteristic 2, a skew-symmetric
bilinear form is alternating since
B(v, v) = −B(v, v) =⇒2B(v, v) = 0 =⇒B(v, v) = 0.
That skew-symmetric and symmetric bilinear forms coincide in characteristic 2 is immediate
since 1 = −1 in characteristic 2.
□
Despite Theorem 1.6, the label “skew-symmetric” is still needed. One reason is that
it is used in preference to “alternating” by many geometers who work over R, where the
two notions coincide. Another reason is that the concept of bilinear form makes sense on
modules, not just vector spaces, and there are skew-symmetric bilinear forms on modules

<!-- page 3 -->
BILINEAR FORMS
3
that are neither symmetric nor alternating (Exercise 2.8). However, we will only deal with
bilinear forms on vector spaces.
Theorem 1.7. In characteristic not 2, every bilinear form B is uniquely expressible as a
sum B1 + B2, where B1 is symmetric and B2 is alternating (equivalently, skew-symmetric).
In characteristic 2, the alternating bilinear forms are a subset of the symmetric bilinear
forms.
Proof. The last part is immediate from Theorem 1.6. Now we work in characteristic not
2. For a bilinear form B, suppose we can write B = B1 + B2 with symmetric B1 and
alternating (so skew-symmetric) B2. Then for vectors v and w,
(1.1)
B(v, w) = B1(v, w) + B2(v, w)
and
B(w, v)
=
B1(w, v) + B2(w, v)
=
B1(v, w) −B2(v, w).
(1.2)
Adding and subtracting (1.1) and (1.2), we get formulas for B1 and B2 in terms of B:
(1.3)
B1(v, w) = B(v, w) + B(w, v)
2
,
B2(v, w) = B(v, w) −B(w, v)
2
.
Turning this reasoning around, the bilinear forms B1 and B2 deﬁned by (1.3) are symmetric
and alternating respectively, so we have established the existence and uniqueness of B1 and
B2.
□
Theorem 1.8. In characteristic not 2, a symmetric bilinear form B(v, w) is completely
determined by its values B(v, v) on the diagonal.
Proof. For any v and w,
1
2(B(v + w, v + w) −B(v, v) −B(w, w)) = 1
2(B(v, w) + B(w, v)) = B(v, w).
Note we used symmetry of B in the last equation.
□
The fact that, for symmetric B, we can recover the 2-variable function B(v, w) from the
1-variable function B(v, v) outside of characteristic 2 is called polarization. For instance, it
shows us that a symmetric bilinear form B is identically 0 if and only if B(v, v) = 0 for all
v (not just B(ei, ei) = 0 on a basis; see Example 1.10). Polarization will play an important
role when we treat quadratic forms later.
Let’s look at some more examples of bilinear forms.
Example 1.9. On R2, B((x, y), (x′, y′)) = xx′ −yy′ is symmetric. How is this formula
diﬀerent from the one in Example 1.5?
Example 1.10. On R2, B((x, y), (x′, y′)) = xy′+yx′ is symmetric. Since B((x, y), (x, y)) =
2xy, B(ei, ei) = 0 where {e1, e2} is the standard basis of R2.
Example 1.11. Fix a vector u in R3. For v and w in R3, let Bu(v, w) = u · (v × w), where
× is the cross product. This is alternating.
Example 1.12. Let V be a ﬁnite-dimensional vector space over F. On the vector space
EndF (V, V ), set B(L, L′) = Tr(LL′). This is called the trace form on EndF (V, V ). It is
bilinear since the trace is linear. It is symmetric since Tr(LL′) = Tr(L′L).

<!-- page 4 -->
4
KEITH CONRAD
Example 1.13. Let V be a ﬁnite-dimensional vector space over F with dual space V ∨. On
the vector space V ⊕V ∨, set
B((v, ϕ), (w, ψ)) = ψ(v) −ϕ(w).
This is alternating. (Symbolically, B((v, ϕ), (w, ψ)) = | ψ ϕ
w v |.) Can you interpret Example
1.5 in this context?
Example 1.14. Let’s look at an inﬁnite-dimensional example. On C[0, 1], the space of
real-valued continuous functions [0, 1] →R, the function B(f, g) =
R 1
0 f(x)g(x) dx is a
symmetric bilinear form. To get other examples of bilinear forms, choose any continuous
function k: [0, 1]2 →R and set
Bk(f, g) =
Z
[0,1]2 f(x)g(y)k(x, y) dx dy.
Can you ﬁnd a k that makes Bk = B? (The function k = 1 does not work.)
Example 1.15. On Cn, let H((z1, . . . , zn), (w1, . . . , wn)) = Pn
i=1 ziwi. Regarding Cn as a
real vector space, H is bilinear. But viewing Cn as a complex vector space, H is linear in
its ﬁrst component but it is not linear in its second component: H(v, cw) equals cH(v, w)
instead of cH(v, w). Therefore H is not bilinear. Moreover, H(v, w) = H(w, v). Pairings
such as H on a complex vector space, which are linear in one component, conjugate-linear
in the other component, and get conjugated when the arguments are exchanged, are called
Hermitian. Our focus is on bilinear forms.
A bilinear form is a generalization of the dot product, so the condition B(v, w) = 0 is
considered to be a generalization of perpendicularity. With this in mind, write v ⊥w when
B(v, w) = 0 and call v and w perpendicular or orthogonal. (We could write v ⊥B w to
stress the dependence of this notion of orthogonality on the choice of B, but this will not
be done.) Since B is bilinear, perpendicularity behaves linearly:
v ⊥w1, v ⊥w2 =⇒v ⊥(c1w1 + c2w2); v1 ⊥w, v2 ⊥w =⇒(c1v1 + c2v2) ⊥w
where c1, c2 ∈F. For a subspace W ⊂V and a vector v ∈V we write v ⊥W when v ⊥w
for all w ∈W and write W ⊥v similarly.
In a general bilinear space the ⊥relation might not be symmetric: we can have v ⊥w
and w ̸⊥v. That is, we could have B(v, w) = 0 and B(w, v) ̸= 0.
Example 1.16. On V = R2, let B((x, y), (x′, y′)) = xx′ + xy′ −x′y −yy′.
We have
(1, 0) ⊥(1, −1) but (1, −1) ̸⊥(1, 0).
Knowing the bilinear forms where v ⊥w ⇔w ⊥v (that is, the relation ⊥is symmetric)
is a key foundational result. Here it is.
Theorem 1.17. The perpendicularity relation on a bilinear space (V, B) is symmetric if
and only if B is either symmetric or alternating.
The proof is a series of elementary but somewhat tedious calculations. Nothing will be
lost by skipping the proof on a ﬁrst reading and coming back to it after the signiﬁcance of
the two types of bilinear forms becomes clearer.
Proof. If B is symmetric or alternating then we have B(v, w) = ±B(w, v), so B(v, w)
vanishes if and only if B(w, v) vanishes.

<!-- page 5 -->
BILINEAR FORMS
5
To prove the converse direction, assume ⊥is a symmetric relation. Pick any vectors
u, v, w ∈V . We ﬁrst will ﬁnd a linear combination av + bw such that (av + bw) ⊥u. This
is the same as
(1.4)
aB(v, u) + bB(w, u) = 0
since B is linear in its ﬁrst component.
We can achieve (1.4) using a = B(w, u) and
b = −B(v, u). Therefore set
x = B(w, u)v −B(v, u)w.
Then B(x, u) = 0, so B(u, x) = 0 by symmetry of the relation ⊥. Computing B(u, x) by
linearity of B in its second component and setting it equal to zero, we obtain
(1.5)
B(w, u)B(u, v) = B(v, u)B(u, w).
This holds for all u, v, w ∈V . We will show a bilinear form satisfying (1.5) is symmetric or
alternating.
Use w = u in (1.5):
(1.6)
B(u, u)B(u, v) = B(v, u)B(u, u).
Notice B(u, u) appears on both sides of (1.6). Thus, for all u and v in V ,
(1.7)
B(u, v) ̸= B(v, u) =⇒B(u, u) = 0 (and similarly B(v, v) = 0).
Now assume that the relation ⊥for B is symmetric and B is not a symmetric bilinear
form. We will prove B is alternating. By assumption, there are u0, v0 ∈V such that
(1.8)
B(u0, v0) ̸= B(v0, u0).
From this we will show B(w, w) = 0 for all w ∈V , relying ultimately on (1.7). Note by
(1.7) and (1.8) that
(1.9)
B(u0, u0) = 0,
B(v0, v0) = 0.
Pick any w ∈V . If B(u0, w) ̸= B(w, u0) or B(v0, w) ̸= B(w, v0) then (1.7) shows B(w, w) =
0. Therefore to prove B(w, w) = 0 for all w ∈V , we may assume
(1.10)
B(u0, w) = B(w, u0),
B(v0, w) = B(w, v0).
In (1.5), setting u = u0 and v = v0 tells us
B(w, u0)B(u0, v0) = B(v0, u0)B(u0, w).
On the left side we can rewrite B(w, u0) as B(u0, w) by (1.10), so
B(u0, w)(B(u0, v0) −B(v0, u0)) = 0.
This implies, by (1.8) and (1.10), that
(1.11)
B(u0, w) = B(w, u0) = 0.
Similarly, setting u = v0 and v = u0 in (1.5) tells us by (1.8) and (1.10) that
(1.12)
B(v0, w) = B(w, v0) = 0.
By (1.11), B(u0, v0 + w) = B(u0, v0) and B(v0 + w, u0) = B(v0, u0). These are distinct by
(1.8), so (1.7) with u = v0 + w and v = u0 implies
B(v0 + w, v0 + w) = 0.
Expanding this out, B(v0, v0) + B(v0, w) + B(w, v0) + B(w, w) = 0. By (1.9) and (1.12),
B(w, w) = 0.
□

<!-- page 6 -->
6
KEITH CONRAD
The proof of Theorem 1.17 did not assume ﬁnite-dimensionality and it used additivity
rather than linearity.
When ⊥is a symmetric relation on V , for any subspace W of V we set
(1.13)
W ⊥= {v ∈V : v ⊥w for all w ∈W} = {v ∈V : w ⊥v for all w ∈W}.
and call this the orthogonal space W ⊥. (This is often called the orthogonal complement
of W in the literature, although it may not really look like a complement: it can happen
that W + W ⊥̸= V .) For nonzero v ∈V , let v⊥= {v′ ∈V : v′ ⊥v}. In the notation
of (1.13), v⊥= (Fv)⊥. The notation W ⊥for a subspace W of a bilinear space V makes
sense only when V is symmetric or alternating. (A third class of vector spaces where a
perpendicularity relation is symmetric is the Hermitian spaces, as in Example 1.15, but
they are not bilinear spaces so Theorem 1.17 doesn’t include them.)
When perpendicularity for a general bilinear form is a symmetric relation, it can still
have nonintuitive features compared with the dot product on Rn. The main such feature
is v ⊥v with v ̸= 0. In the symmetric bilinear space of Example 1.9 we have (1, 1) ⊥(1, 1).
It takes time to become accustomed to the idea that the condition v ⊥v need not force
v = 0. Using the dot product as a bilinear form on Rn, for every subspace W we have
Rn = W ⊕W ⊥, but such a direct sum decomposition is not generally valid for subspaces
of other bilinear spaces. (A vector space V is called a direct sum of two subspaces W and
W ′ when V = W + W ′ and W ∩W ′ = {0}; the intersection condition is the same as saying
the representation of an element of V as a sum of an element of W and an element of W ′
is unique.) An example of a bilinear space V and a subspace W where V ̸= W ⊕W ⊥is
Example 1.9: V = R2 with B((x, y), (x′, y′)) = xx′ −yy′: the subspace W = R(1, 1) has
W ⊥= W, so W + W ⊥̸= R2.
Here are two constructions of new bilinear spaces from old ones.
• Subspace: If (V, B) is a bilinear space and W is a subspace of V , then B restricts
to a bilinear form on W, so we get a bilinear subspace denoted (W, B|W ) or simply
(W, B). (Strictly speaking, we should write B|W×W since B is a function of two
variables, but the more concise B|W shouldn’t cause confusion.) It is obvious that
if B is either symmetric, alternating, or skew-symmetric on V then that property is
inherited by any subspace.
• Direct Sum: If (V1, B1) and (V2, B2) are bilinear spaces over the same ﬁeld then
V1⊕V2 becomes a bilinear space using the bilinear form (B1⊕B2)((v1, v2), (v′
1, v′
2)) :=
B1(v1, v′
1) + B2(v2, v′
2). This formula is not mysterious; the idea is to treat V1 and
V2 separately, just as the direct sum treats V1 and V2 separately. In B1 ⊕B2 we pair
up the ﬁrst components, then the second components, and add.
If B1 and B2 are both symmetric, both alternating, or both skew-symmetric then
B1 ⊕B2 inherits this property.
Deﬁnition 1.18. The bilinear space (V1 ⊕V2, B1 ⊕B2) constructed above is called the
orthogonal direct sum of V1 and V2 and is denoted V1 ⊥V2.
Example 1.19. Thinking about R as a bilinear space under multiplication (Example 1.4),
R ⊥R is R2 with the dot product and the n-fold orthogonal direct sum R⊥n = R ⊥· · · ⊥R
is Rn with the dot product.
We embed V1 into the orthogonal direct sum V1 ⊥V2 in a natural way: v1 7→(v1, 0).
Similarly we embed V2 into V1 ⊥V2 by v2 7→(0, v2).

<!-- page 7 -->
BILINEAR FORMS
7
If V1 and V2 are subspaces of a bilinear space V then we write V1 ⊥V2 as a relation if
v1 ⊥v2 for all v1 ∈V1 and v2 ∈V2. This use of ⊥as a relation on subspaces is diﬀerent
from the use of ⊥in the construction of the orthogonal direct sum of two bilinear spaces.
Theorem 1.20. Let (V1, B1) and (V2, B2) be bilinear spaces. Viewing V1 and V2 as sub-
spaces of V1 ⊕V2 in the natural way, (B1 ⊕B2)|Vi = Bi. Both V1 ⊥V2 and V2 ⊥V1 relative
to B1 ⊕B2. These conditions determine B1 ⊕B2 as a bilinear form on V1 ⊕V2.
Proof. Since (B1 ⊕B2)((v1, 0), (v′
1, 0)) = B1(v1, v′
1), (B1 ⊕B2)|V1 = B1. In a similar way,
(B1 ⊕B2)|V2 = B2.
For v1 ∈V1 and v2 ∈V2,
(B1 ⊕B2)((v1, 0), (0, v2)) = B1(v1, 0) + B2(0, v2) = 0
and
(B1 ⊕B2)((0, v2), (v1, 0)) = B1(0, v1) + B2(v2, 0) = 0.
Therefore v1 ⊥v2 and v2 ⊥v1 in (V1 ⊕V2, B1 ⊕B2).
Let B0 be any bilinear form on V1 ⊕V2 such that B0|Vi = Bi and V1 ⊥V2 and V2 ⊥V1
relative to B0. Then
B0((v1, v2), (v′
1, v′
2)) = B0((v1, 0), (v′
1, 0)) + B0((v1, 0), (0, v′
2))+
B0((0, v2), (v′
1, 0)) + B0((0, v2), (0, v′
2))
= B0((v1, 0), (v′
1, 0)) + B0((0, v2), (0, v′
2))
= B1(v1, v′
1) + B2(v2, v′
2),
so B0 = B1 ⊕B2.
□
If a bilinear space V can be expressed as a direct sum of two subspaces W and W ′ with
the additional conditions that W ⊥W ′ and W ′ ⊥W then Theorem 1.20 shows V behaves
just like the orthogonal direct sum of W and W ′. Most decompositions of a bilinear space
into a direct sum of subspaces are not orthogonal direct sums since the subspaces may
not be mutually perpendicular.
This is already familiar from Rn, which admits many
decompositions into a direct sum of linear subspaces that are not mutually perpendicular.
We end this section with an important link between bilinear forms and the dual space.
For a bilinear form B on V , we can think about B(v, w) as a function of w with v ﬁxed or
a function of v with w ﬁxed. Taking the ﬁrst point of view, the function B(v, −) : V →F
sends each w to B(v, w). Since B is linear in its second component when the ﬁrst is ﬁxed,
w 7→B(v, w) is a linear map from V to F, so B(v, −) ∈V ∨for each v. Set LB : V →V ∨
by LB : v 7→B(v, −), so LB(v) = B(v, −).
The values of LB are in V ∨, so they are
functions on V (with the unknown substituted into the empty slot of B(v, −)).
Since
B(v + v′, w) = B(v, w) + B(v′, w) for all w, B(v + v′, −) = B(v, −) + B(v′, −) in V ∨, and
thus LB(v + v′) = LB(v) + LB(v′). Similarly, since B(cv, w) = cB(v, w), LB(cv) = cLB(v).
Thus LB is linear, so a bilinear form B on V gives a linear map LB from V to its dual space
V ∨. Since LB(v)(w) = (B(v, −))(w) = B(v, w), we can recover B from LB by evaluating
LB at each v ∈V and then evaluating LB(v) ∈V ∨at all w ∈V to get B(v, w).
Conversely, if we have a linear map L: V →V ∨then to each v ∈V we have L(v) ∈V ∨, so
we get a bilinear form B(v, w) := L(v)(w) such that B(v, −) = L(v). These correspondences
from bilinear forms on V to linear maps V →V ∨and back are inverses of one another.
In a similar way, from a bilinear form B we get functions B(−, w) ∈V ∨(sending v to
B(v, w)). Let RB : V →V ∨by RB : w 7→B(−, w), so RB(w) = B(−, w). The map RB

<!-- page 8 -->
8
KEITH CONRAD
is linear from V to V ∨, and passing from B to RB is a second one-to-one correspondence
between bilinear forms on V and linear maps V →V ∨(Exercise 1.6).
These two ways of viewing a bilinear form B as a linear map V →V ∨(using LB or RB)
are related through double duality:
Theorem 1.21. When V is ﬁnite-dimensional and B is a bilinear form on V , the linear
maps LB and RB are dual to each other.
Speciﬁcally, if we dualize LB : V →V ∨to
L∨
B : V ∨∨→V ∨and identify V ∨∨with V in the natural way then L∨
B = RB. Similarly,
R∨
B = LB.
Proof. For a linear map L: V →W, the dual L∨: W ∨→V ∨is deﬁned by
L∨(ϕ)(v) = ϕ(L(v))
for ϕ ∈W ∨and v ∈V . Taking W = V ∨, L = LB, and writing the elements of W ∨= V ∨∨
as evaluation maps at elements in V ,
L∨
B(evv′)(v) = evv′(LB(v)) = evv′(B(v, −)) = B(v, v′) = RB(v′)(v).
Thus L∨
B = RB when we identify V ∨∨with V in the usual way. The proof that R∨
B = LB
is similar, or dualize the equation L∨
B = RB.
□
There are two ways of identifying bilinear forms on V with linear maps V →V ∨because
a bilinear form is a function of two variables in V and we can take preference for one variable
over the other to get a linear map out of V . In Section 8, tensor products will be used to
interpret a bilinear form on V as a linear map without biasing LB over RB.
Exercises.
1. Let B be a bilinear form on V . Prove B is skew-symmetric if and only if the diagonal
function V →F given by v 7→B(v, v) is additive.
2. Show any alternating bilinear form on R3 is some Bu as in Example 1.11.
3. In Example 1.14, show Bk is symmetric if and only if k(x, y) = k(y, x) for all x and
y. What condition on k makes Bk alternating?
4. For a bilinear form B on an F-vector space V , show V × F is a group under the
operation (v, x)(w, y) = (v+w, x+y+B(v, w)). When V = F 2 and B((a, b), (c, d)) =
ad, this group is the 3-dimensional Heisenberg group over F.
5. Deﬁne a bilinear form on a module over a commutative ring and check any alter-
nating bilinear form is skew-symmetric. Show the converse is true if there is no
2-torsion in the ring (2x = 0 ⇒x = 0 for x in the ring).
6. Let Bil(V ) be the set of all bilinear forms on V . It is a vector space under addition
and scaling. For a bilinear form B on V , show the correspondence B →RB is
a vector space isomorphism from Bil(V ) to HomF (V, V ∨).
Here V need not be
ﬁnite-dimensional, but if dimF (V ) = n is ﬁnite, then dimF (Bil(V )) = n2.
7. Let B be a bilinear form on V . Set V ⊥L = {v ∈V : v ⊥V } and V ⊥R = {v ∈
V : V ⊥v}. Since B(v, w + w′) = B(v, w) when w′ ∈V ⊥R, LB induces a linear
map V →(V/V ⊥R)∨. Show this linear map has kernel V ⊥L, so we get a linear
embedding V/V ⊥L ,→(V/V ⊥R)∨. Use this and the analogous argument with RB
in place of LB to show dim V ⊥L = dim V ⊥R when V is ﬁnite-dimensional.

<!-- page 9 -->
BILINEAR FORMS
9
2. Bilinear forms and matrices
From now on, all vector spaces are understood to be ﬁnite-dimensional.
A linear transformation L: V →W between two ﬁnite-dimensional vector spaces over
F can be written as a matrix once we pick (ordered) bases for V and W. When V = W
and we use the same basis for the inputs and outputs of L then changing the basis leads to
a new matrix representation that is conjugate to the old matrix. In particular, the trace,
determinant, and (more generally) characteristic polynomial of a linear operator L: V →V
are well-deﬁned, independent of the choice of basis. In this section we will see how bilinear
forms and related constructions can be described using matrices.
We start with a concrete example. In addition to the dot product on Rn, additional
bilinear forms on Rn are obtained by throwing a matrix into one side of the dot product:
for an n×n real matrix M, the formula B(v, w) = v ·Mw is a bilinear form on Rn. It turns
out this kind of construction describes all bilinear forms on any ﬁnite-dimensional vector
space, once we ﬁx a basis.
Let V have dimension n ≥1 with basis {e1, . . . , en}. Pick v and w in V and express
them in this basis: v = Pn
i=1 xiei and w = Pn
j=1 yjej. For any bilinear form B on V , its
bilinearity gives
B(v, w) = B


n
X
i=1
xiei,
n
X
j=1
yjej


=
n
X
i=1
xiB

ei,
n
X
j=1
yjej


=
n
X
i=1
n
X
j=1
xiyjB(ei, ej).
Set M := (B(ei, ej)), which is an n × n matrix. By a calculation the reader can carry out,
(2.1)
B(v, w) = [v] · M[w]
for all v and w in V , where · on the right is the usual dot product on F n and
[v] =



x1
...
xn


,
[w] =



y1
...
yn



are the coordinate vectors of v and w for our choice of basis {e1, . . . , en}. The “coordi-
nate” isomorphism [·]: V →F n will refer to a ﬁxed choice of (ordered) basis {e1, . . . , en}
throughout a given discussion: [e1] is the ﬁrst standard basis vector of F n, [e2] is the second
standard basis vector of F n, and so on.
We call the matrix M = (B(ei, ej)) appearing in (2.1) the matrix associated to B in the
basis {e1, . . . , en}.
Example 2.1. The matrix associated to the dot product on F n in the standard basis of
F n is the identity matrix.
Example 2.2. In Example 1.5,
xy′ −x′y =

x
y

·

0
1
−1
0
 
x′
y′

.

<!-- page 10 -->
10
KEITH CONRAD
It is easy to read oﬀthe matrix from the formula on the left: there are no xx′ or yy′ terms,
so the diagonal entries of the matrix are 0. Since xy′ has coeﬃcient 1, the (1, 2) entry of
the matrix is 1. The term x′y = yx′ corresponds to the (2, 1) entry (because it involves the
second entry of
 x
y

and the ﬁrst entry of
 x′
y′

, in that order), which is the coeﬃcient −1.
Theorem 2.3. Let V be a vector space over F of dimension n ≥1. For a ﬁxed choice of
basis {e1, . . . , en} of V , which gives an isomorphism v 7→[v] from V to F n by coordinati-
zation, each bilinear form on V has the expression (2.1) for a unique n × n matrix M over
F and each n × n matrix M over F deﬁnes a bilinear form on V by (2.1).
Proof. We already showed each bilinear form looks like (2.1) once we choose a basis. It’s
easy to see for each M that (2.1) is a bilinear form on V . It remains to verify uniqueness.
If B(v, w) = [v] · N[w] for a matrix N then B(ei, ej) = [ei] · N[ej], which is the (i, j) entry
of N, so N = (B(ei, ej)).
□
Note the zero vector space has 1 bilinear form but no matrix. We will not be pedantic
about including the zero vector space in our discussion.
Example 2.4. Let V = Rn. Pick nonnegative integers p and q such that p + q = n. For
v = (x1, . . . , xn) and v′ = (x′
1, . . . , x′
n) in Rn, set
⟨v, v′⟩p,q := x1x′
1 + · · · + xpx′
p −xp+1x′
p+1 −· · · −xnx′
n
= v · ( Ip
O
O −Iq )v′.
This symmetric bilinear form is like the dot product, except the coeﬃcients involve p plus
signs and n −p = q minus signs. The dot product on Rn is the special case (p, q) = (n, 0).
Example 1.9 is the special case (p, q) = (1, 1).
The space Rn with the bilinear form ⟨·, ·⟩p,q is denoted Rp,q. We call Rp,q a pseudo-
Euclidean space when p and q are both positive. Example 1.9 is R1,1. The example R1,3
or R3,1 is called Minkowski space and arises in relativity theory.
A pseudo-Euclidean
space is the same vector space as Rn, but its geometric structure (e.g., the notion of
perpendicularity) is diﬀerent. The label Euclidean space is actually not just another name
for Rn as a vector space, but it is the name for the vector space Rn together with the
standard dot product on it as a bilinear form.
Bilinear forms are not linear maps, but we saw at the end of Section 1 that each bilinear
form B on V can be interpreted as a linear map V →V ∨in two ways, as LB and RB. The
matrix of B is the same as the matrix of one of these linear maps! Which one?
Theorem 2.5. If B is a bilinear form on V , the matrix for B in the basis {e1, . . . , en} of
V equals the matrix of the linear map RB : V →V ∨with respect to the given basis of V and
its dual basis in V ∨.
Proof. Let [·]: V →F n be the coordinate isomorphism coming from the basis in the theorem
and let [·]′ : V ∨→F n be the coordinate isomorphism using the dual basis. The matrix for
RB has columns [RB(e1)]′, . . . , [RB(en)]′. To compute the entries of the jth column, we
simply have to ﬁgure out how to write RB(ej) as a linear combination of the dual basis
{e∨
1 , . . . , e∨
n} of V ∨and use the coeﬃcients that occur.
There is one expression for RB(ej) in the dual basis:
RB(ej) = c1e∨
1 + · · · + cne∨
n

<!-- page 11 -->
BILINEAR FORMS
11
in V ∨, with unknown ci’s. To ﬁnd ci we just evaluate both sides at ei: the left side is
(RB(ej))(ei) = (B(−, ej))(ei) = B(ei, ej) and the right side is ci · 1 = ci. Therefore the
ith entry of the column vector [RB(ej)]′ is B(ei, ej), which means the matrix for RB is the
matrix (B(ei, ej)); they agree column-by-column.
□
In terms of a commutative diagram, Theorem 2.5 says
(2.2)
V
[·]

RB
/ V ∨
[·]′

F n
(B(ei,ej))
/ F n
commutes: [RB(v)]′ = (B(ei, ej))[v] for all v in V .
Remark 2.6. That the matrix associated to B is the matrix of RB rather than LB is
related to our convention that we view bilinear forms concretely using [v] · A[w] instead of
A[v] · [w]. If we adopted the latter convention then the matrix associated to B would equal
the matrix for LB.
Theorem 2.7. Let (V, B) be a bilinear space and let B have associated matrix M in some
basis. Then
(1) B is symmetric if and only if M⊤= M,
(2) B is skew-symmetric if and only if M⊤= −M,
(3) B is alternating if and only if M⊤= −M and the diagonal entries of M are zero.
Matrices satisfying the conditions in (1), (2), and (3) are called symmmetric, skew-
symmetric, and alternating matrices respectively.
Proof. The matrix M represents the linear map RB : V →V ∨using the given basis of V
and its dual basis. Since LB and RB are dual maps in the sense of Theorem 1.21, the matrix
representing LB in these same bases is M⊤. Since B is symmetric precisely when RB = LB,
the matrix condition for B to be symmetric is M = M⊤. Similarly, skew-symmetry of B
means RB = −LB, which becomes M = −M⊤in matrix language. The matrix condition
on an alternating form is left as an exercise.
□
The correspondence in (2.1) between bilinear forms and square matrices (once a basis is
chosen) behaves well for some natural operations with bilinear forms. For instance, given
bilinear forms B and eB on V , we can talk about their sum B + eB, a scalar multiple cB,
and the function with reversed arguments Br:
(B + eB)(v, w) = B(v, w) + eB(v, w),
(cB)(v, w) = cB(v, w),
Br(v, w) = B(w, v).
These are all bilinear forms on V . If we ﬁx a basis of V , so V is identiﬁed with F n and each
bilinear form on V is identiﬁed with an n × n matrix by (2.1), the sum and scalar multiple
of bilinear forms corresponds to the sum and scalar multiple of the corresponding matrices.
Conceptually, this means RB is linear in B. Since LBr = RB and RBr = LB, the matrix
associated to reversing the arguments is the transposed matrix.
Once we pick a basis of V , linear transformations V →V and bilinear forms on V both
get described by square matrices. Addition and scaling of either linear transformations or
bilinear forms pass to addition and scaling of the corresponding matrices, and composition
of linear transformations passes to multiplication of the corresponding matrices.
There

<!-- page 12 -->
12
KEITH CONRAD
is no natural operation for bilinear forms on V that corresponds to multiplication of the
corresponding matrices. This makes sense from the viewpoint of Exercise 1.6: bilinear forms
on V can be viewed as linear maps V →V ∨, and these can’t naturally be composed.
When a linear transformation L: V →V has matrix M in some basis, and C is the
change-of-basis matrix expressing a new basis in terms of the old basis, then the matrix
for L in the new basis is C−1MC. Let’s recall two proofs of this and then adapt them to
compute the way a change of basis changes the matrix for a bilinear form.
The change-of-basis matrix C, whose columns express the coordinates of the second basis
in terms of the ﬁrst basis, satisﬁes
(2.3)
[v]1 = C[v]2
for all v ∈V , where [·]i is the coordinate isomorphism of V with F n using the ith basis.
Indeed, both sides are linear in v, so it suﬃces to check this identity when v runs through
the second basis, which recovers the deﬁnition of C by its columns. Since [Lv]1 = M[v]1 for
all v ∈V ,
[Lv]2 = C−1[Lv]1
= C−1M[v]1
= C−1MC[v]2,
so we’ve proved the matrix for L in the second basis is C−1MC.
For a second proof, the identity (2.3) can be expressed as the commutative diagram
(2.4)
V
[·]2 
idV
/ V
[·]1

F n
C
/ F n
and the fact that M is the matrix for L in the ﬁrst basis means
(2.5)
V
[·]1 
L
/ V
[·]1

F n
M
/ F n
commutes. To ﬁnd the matrix for L in the second basis amounts to ﬁnding the linear map
for the bottom row that makes
V
[·]2 
L
/ V
[·]2

F n
?
/ F n
commute. Only one map ﬁts since the vertical maps in this diagram are isomorphisms, so
? = [·]2 ◦L ◦[·]−1
2 . But what is “?” concretely?
We can obtain such a commutative diagram as the boundary of the commutative diagram
with (2.5) in the middle and (2.4) on the two ends
V
[·]2 
idV
/ V
[·]1 
L
/ V
[·]1 
idV
/ V
[·]2 
F n
C
/ F n
M
/ F n
C−1
/ F n

<!-- page 13 -->
BILINEAR FORMS
13
where the composite across the top is L, so ? = C−1MC (since composition is written right
to left).
Theorem 2.8. Let C be a change-of-basis matrix on V . A bilinear form on V with matrix
M in the ﬁrst basis has matrix C⊤MC in the second basis.
Proof. Let B be the bilinear form in the theorem. For a short matrix-based proof of this
theorem, start with (2.3). It tells us1
B(v, w) = [v]1 · M[w]1 = C[v]2 · MC[w]2 = [v]2 · C⊤MC[w]2,
so the matrix for B in the second basis is C⊤MC.
Now we give a proof using commutative diagrams. By (2.2), the matrix M for B occurs
in the commutative diagram
(2.6)
V
[·]1

RB
/ V ∨
[·]′
1

F n
M
/ F n
where [·]′
1 is the coordinate isomorphism using the dual basis to the ﬁrst basis of V . Finding
the matrix for B in the second basis amounts to ﬁnding the matrix for the bottom row of
a commutative diagram
(2.7)
V
[·]2

RB
/ V ∨
[·]′
2

F n
?
/ F n
where [·]′
2 is the coordinate isomorphism for the dual basis of the second basis of V .
Dualizing the maps and spaces in (2.4) gives the commutative diagram2
(2.8)
F n
[·]∨
1 
C⊤
/ F n
[·]∨
2

V ∨
idV ∨
/ V ∨
and now we use Exercise 2.7: for any coordinate isomorphism [·]: V →F n for a basis of
V , the coordinate isomorphism [·]′ : V ∨→F n for the dual basis of V ∨is the inverse of the
dual map [·]∨: F n →V ∨(where F n is identiﬁed with its dual space using the dot product).
Therefore reversing the direction of the vertical maps in (2.8) by using their inverses lets us
rewrite (2.8) as
(2.9)
V ∨
[·]′
1 
idV ∨
/ V ∨
[·]′
2

F n
C⊤
/ F n
1In F n, Ax · y = x · A⊤y for any A ∈Mn(F). Apply this with A = C.
2When C : F n →F n is dualized and we think about (F n)∨as F n using the dot product, the dual map
to C is C⊤.

<!-- page 14 -->
14
KEITH CONRAD
so our desired diagram (2.7) can be found by sticking (2.4) and (2.9) on either side of (2.6)
and looking at the boundary:
V
[·]2

idV
/ V
[·]1

RB
/ V ∨
[·]′
1 
idV ∨
/ V ∨
[·]′
2 
F n
C
/ F n
M
/ F n
C⊤
/ F n
The composite across the top is RB and the composite along the bottom is C⊤MC, so
C⊤MC is our desired matrix.
□
Deﬁnition 2.9. Two bilinear forms B1 and B2 on the respective vector spaces V1 and V2
are called equivalent if there is a vector space isomorphism A: V1 →V2 such that
B2(Av, Aw) = B1(v, w)
for all v and w in V1.
Equivalence of bilinear forms is an equivalence relation. Concretely, if we write everything
in coordinates so V1 and V2 are replaced by F n (same n; otherwise there couldn’t possibly
be an equivalence of bilinear forms on the spaces), then Deﬁnition 2.9 says: two bilinear
forms on F n are equivalent when there is a linear change of variables turning one into the
other. In particular, when B1 and B2 are symmetric bilinear forms on F n, so they are
determined by their diagonal values B1(v, v) and B2(v, v) (Theorem 1.8), B1 and B2 are
equivalent when there is a linear change of variables turning B2(v, v) into B1(v, v).
Example 2.10. On R2, let
B(v, w) = v · ( 1 0
0 −1 )w,
eB(v, w) = v · ( 0
1/2
1/2
0 )w.
Both of these are symmetric. For v = w = (x, y), we have B(v, v) = x2 −y2 and eB(v, v) =
xy. Since x2 −y2 = (x + y)(x −y), we can pass from B to eB by the linear change of
variables x′ = x + y and y′ = x −y. Then B((x, y), (x, y)) = eB((x′, y′), (x′, y′)). Since
 x′
y′

= ( 1
1
1 −1 )
 x
y

, B(v, v) = eB(( 1
1
1 −1 )v, ( 1
1
1 −1 )v). Therefore B(v, w) = eB(( 1
1
1 −1 )v, ( 1
1
1 −1 )w),
so B and eB are equivalent by the matrix ( 1
1
1 −1 ).
In terms of commutative diagrams, B1 and B2 are equivalent when there is a vector space
isomorphism A: V1 →V2 such that the diagram
(2.10)
V1
A

RB1
/ V ∨
1
V2
RB2
/ V ∨
2
A∨
O
commutes. (Verify!)
We saw in Theorem 2.8 that matrix representations M1 and M2 of a single bilinear form
in two diﬀerent bases are related by the rule M2 = C⊤M1C for an invertible matrix C.
Let’s show this rule more generally links matrix representations of equivalent bilinear forms
on possibly diﬀerent vector spaces.

<!-- page 15 -->
BILINEAR FORMS
15
Theorem 2.11. Let bilinear forms B1 and B2 on V1 and V2 have respective matrix represen-
tations M1 and M2 in two bases. Then B1 is equivalent to B2 if and only if M1 = C⊤M2C
for some invertible matrix C.
Proof. The equivalence of B1 and B2 means, by (2.10), there is an isomorphism A: V1 →V2
such that A∨RB2A = RB1. Using the bases on Vi (i = 1, 2) in which Bi is represented by Mi
and the dual bases on V ∨
i , this equation is equivalent to C⊤M2C = M1, where C represents
A. (Invertibility of C is equivalent to A being an isomorphism.)
□
Example 2.12. Returning to Example 2.10, ( 1 0
0 −1 ) = C⊤(
0 1/2
1/2
0 )C for C = ( 1
1
1 −1 ).
Although all matrix representations of a linear transformation V →V have the same de-
terminant (det(C−1MC) = det M), the matrix representations of a bilinear form on V have
the same determinant only up to a nonzero square factor: det(C⊤MC) = (det C)2 det M.
Since equivalent bilinear forms can be represented by the same matrix using suitable bases,
the determinants of any matrix representations for two equivalent bilinear forms must dif-
fer by a nonzero square factor. This provides a suﬃcient (although far from necessary)
condition to show two bilinear forms are inequivalent.
Example 2.13. Let d be a squarefree positive integer. On Q2, the bilinear form Bd(v, w) =
v · ( 1 0
0 d )w has a matrix with determinant d, so diﬀerent (squarefree) d’s give inequivalent
bilinear forms on Q2. As bilinear forms on R2, however, these Bd’s are equivalent: ( 1 0
0 d ) =
C⊤I2C for C = ( 1
0
0
√
d ). Another way of putting this is that, relative to coordinates in the
basis {(1, 0), (0, 1/
√
d)} of R2, Bd looks like the dot product B1.
Example 2.14. When q is positive and even, ⟨·, ·⟩p,q and the dot product on Rp+q both are
represented by matrices with determinant 1, but they are not equivalent: the dot product
takes only nonnegative values at diagonal pairs (v, v) while ⟨·, ·⟩p,q assumes some negative
values on the diagonal when q > 0. We will see in Section 6 that all the bilinear forms
⟨·, ·⟩p,q (with p + q ﬁxed) are inequivalent for diﬀerent pairs (p, q).
Exercises.
1. Compute the matrix associated to the bilinear forms in Examples 1.9, 1.10, 1.11
and 1.16 relative to the standard basis of column vectors.
2. For v ∈R3, let Lv : R3 →R3 by Lv(w) = v × w. Set B(v, w) = Tr(LvLw). Show B
is a symmetric bilinear form on R3 and compute its matrix relative to the standard
basis of R3.
3. For x, y ∈F,
 x
y

·( 1 0
0 0 )
 x
y

= x2 and
 x
y

·(
1 1
−1 0 )
 x
y

= x2. Why doesn’t this contradict
Theorem 2.3?
4. Complete the proof of Theorem 2.7.
5. Show a matrix representation for the trace form on M2(F) (Example 1.12) has
determinant −1.
6. When V has dimension n, the vector space Bil(V ) of all bilinear forms on V has
dimension n2 (Exercise 1.6).
What are the dimensions of the two subspaces of
symmetric and alternating bilinear forms?
7. Let V be n-dimensional over F. Given a basis of V , let [·]: V →F n be the corre-
sponding coordinate isomorphism and let [·]′ : V ∨→F n be the coordinate isomor-
phism coming from the dual basis on V ∨. When we identify F n with its dual space

<!-- page 16 -->
16
KEITH CONRAD
using the dot product (that is, view elements of (F n)∨as the maps “dot with a ﬁxed
vector”), show the dual map [·]∨: F n →V ∨is the inverse of [·]′.
8. Let m ≥4 be even and B(v, w) = v · ( m/2
1
−1 m/2 )w for v, w ∈(Z/(m))2. Viewing
(Z/(m))2 as a Z/(m)-module, show B is a bilinear form that is skew-symmetric but
not symmetric or alternating. Where does the argument break down if m = 2?
3. Nondegenerate bilinear forms
Bilinear forms are represented by matrices, but there isn’t a natural operation on bilinear
forms that corresponds to multiplication of those matrices. However, there is a condition
on a bilinear form that corresponds to invertibility of its matrix representations.
Theorem 3.1. Let (V, B) be a bilinear space. The following conditions are equivalent:
(1) for some basis {e1, . . . , en} of V , the matrix (B(ei, ej)) is invertible,
(2) if B(v, v′) = 0 for all v′ ∈V then v = 0, or equivalently if v ̸= 0 then B(v, v′) ̸= 0
for some v′ ∈V ,
(3) every element of V ∨has the form B(v, −) for some v ∈V ,
(4) every element of V ∨has the form B(v, −) for a unique v ∈V .
When this occurs, every matrix representation for B is invertible.
Proof. The matrix (B(ei, ej)) is a matrix representation of the linear map RB : V →V ∨by
Theorem 2.5. So condition (1) says RB is an isomorphism.
The functions B(v, −) in V ∨are the values of LB : V →V ∨, so condition (2) says
LB : V →V ∨is injective.
Condition (3) says LB is surjective and (4) says LB is an
isomorphism.
Since LB is a linear map between vector spaces of the same dimension,
injectivity, surjectivity, and isomorphy are equivalent properties. So (2), (3), and (4) are
equivalent.
Since LB and RB are dual to each other (Theorem 1.21), (1) and (4) are
equivalent.
Diﬀerent matrix representations M and M′ of a bilinear form are related by M′ = C⊤MC
for some invertible matrix C, so if one matrix representation is invertible then so are the
others.
□
The key point of Theorem 3.1 is that V parametrizes its own dual space by the functions
B(v, −) exactly when a matrix for B is invertible. When this happens, each element of the
dual space is also described as B(−, v) for a some v, necessarily unique, by interchanging
the roles of LB and RB in the proof of Theorem 3.1.
Deﬁnition 3.2. Let (V, B) be a nonzero bilinear space. We call V or B nondegenerate if
the equivalent conditions in Theorem 3.1 hold. A bilinear space or bilinear form that is not
nondegenerate is called degenerate.
A bilinear form on V is essentially the same thing as a linear map V →V ∨(Exercise
1.6), so a choice of a nondegenerate bilinear form on V is really the same thing as a choice
of an isomorphism V →V ∨. Since V ∼= V ∨when V = {0}, for completeness the zero vector
space with its only (zero) bilinear form is considered to be nondegenerate although there is
no matrix.
Example 3.3. The dot product on Rn is nondegenerate: if v · w = 0 for all w ∈Rn,
then in particular v · v = 0, so v = 0. (Alternatively, the matrix representation for the dot
product in the standard basis is In, which is invertible.) Thus each element of (Rn)∨has

<!-- page 17 -->
BILINEAR FORMS
17
the form ϕ(w) = v · w for a unique v ∈Rn; the elements of (Rn)∨are just dotting with a
ﬁxed vector.
Example 3.4. The symmetric bilinear form ⟨·, ·⟩p,q that deﬁnes Rp,q (Example 2.4) is
nondegenerate: for nonzero v = (c1, . . . , cn) in Rp,q, it may happen that ⟨v, v⟩p,q = 0, but
certainly some coordinate ci is nonzero, so ⟨v, ei⟩p,q = ±ci ̸= 0 for that i. Alternatively, the
matrix for ⟨·, ·⟩p,q in the standard basis is M =

Ip
O
O
−Iq

, which is invertible. Thus each
ϕ ∈(Rp,q)∨looks like ϕ(w) = ⟨v, w⟩p,q for a unique v ∈Rp,q.
Letting n = p + q, Rp,q equals Rn as vector spaces, so their dual spaces are the same.
How can we reconcile the description of the dual space of Rp,q using ⟨·, ·⟩p,q above and the
dual space of Rn using the dot product from Example 3.3? Well, ⟨v, w⟩p,q = v · Mw, with
M symmetric and M = M−1. Therefore the dual space of Rp,q = Rn using ⟨·, ·⟩p,q and the
dot product match up as follows:
⟨v, −⟩p,q = Mv · (−),
v · (−) = ⟨Mv, −⟩p,q.
Example 3.5. Example 1.5 is nondegenerate: pairing a nonzero vector with at least one
of (1, 0) or (0, 1) will give a nonzero result. Alternatively, this bilinear form is represented
by an invertible matrix.
Example 3.6. The alternating bilinear form on V ⊕V ∨in Example 1.13 is nondegenerate.
Assume (v, ϕ) ∈(V ⊕V ∨)⊥, so ψ(v) = ϕ(w) for all w ∈V and ψ ∈V ∨. Taking for ψ the
zero dual vector, ϕ(w) = 0 for all w, so ϕ = 0. Therefore ψ(v) = 0 for all ψ ∈V ∨, so v = 0.
Example 3.7. Let’s see a degenerate bilinear form.
On R2 set B(v, w) = v · ( 1 0
0 0 )w.
In coordinates, B((x, y), (x′, y′)) = xx′. This is degenerate since the matrix ( 1 0
0 0 ) is not
invertible. We have (0, 1) ⊥w for all w. The matrix representing B is not invertible.
Remark 3.8. On a real vector space, a bilinear form B is called positive deﬁnite if B(v, v) >
0 for every v ̸= 0. The dot product on Rn is positive deﬁnite. A positive-deﬁnite bilinear
form B is nondegenerate since a vector v is zero if B(v, v) = 0. The idea behind non-
degeneracy, as a generalization of positive deﬁniteness, is that v = 0 if B(v, w) = 0 for all
w, not just if B(v, v) = 0. Equivalently, to show v ̸= 0 check B(v, w) ̸= 0 for some w that
need not be v itself (perhaps B(v, v) = 0 but B(v, w) ̸= 0 for some w).
Positive-deﬁnite symmetric bilinear forms play an important role in analysis (real Hilbert
spaces) and geometry (Riemannian manifolds). For geometers, the impetus to explore the
consequences of weakening positive deﬁnitness to nondegeneracy came from physics, where
the local model spaces in relativity theory are pseudo-Euclidean (Example 2.4); they carry
a symmetric bilinear form that is not positive deﬁnite but is nondegenerate. Real vector
spaces equipped with a nondegenerate alternating bilinear form are the local models for
phase spaces in Hamiltonian mechanics.
Remark 3.9. In quantum mechanics, whose underlying mathematics involves heavy doses
of linear algebra, the terms “degenerate” and “non-degenerate” are used with meanings that
are unrelated to their meaning here. For quantum physicists, “degenerate” is a label for an
eigenspace of a linear operator that has dimension greater than 1, while an eigenspace with
dimension 1 is “non-degenerate”. In that setting, degeneracy is related to the multiplicity of
an eigenvalue as a root of a characteristic polynomial: simple roots have “non-degenerate”
eigenspaces while a multiple root has a “degenerate” eigenspace.

<!-- page 18 -->
18
KEITH CONRAD
Example 3.10. Let g be a ﬁnite-dimensional Lie algebra over F and for each x ∈g set
ad(x) = [x, −] on g, i.e., ad(x)(y) = [x, y]. The symmetric bilinear form on g deﬁned by
B(x, x′) = Tr(ad(x)ad(x′)) is called the Killing form of g. If F has characteristic 0, g is
semisimple if and only if its Killing form is nondegenerate.
Example 3.11. Although R2,1 is nondegenerate, the plane spanned by v1 = (1, 0, 1) and
v2 = (0, 1, 0) inside R2,1 is degenerate (that is, the restriction of ⟨·, ·⟩2,1 to this plane is
degenerate) since v1 ⊥v1 and v1 ⊥v2. There are vectors in R2,1 that are not perpendicular
to v1, such as (1, 0, 0), but such vectors don’t lie in the plane of v1 and v2.
Example 3.11 is good to remember: a nondegenerate bilinear form on a vector space
might restrict to a degenerate bilinear form on a subspace! Such behavior is impossible if
F = R and B is positive deﬁnite (Remark 3.8): when B(v, v) > 0 for all nonzero v ∈V ,
this property remains true on every nonzero subspace W ⊂V , so the restriction B|W is
also positive deﬁnite and thus is also nondegenerate.
Theorem 3.12. Let V be a bilinear space that is either symmetric or alternating.
(1) For a subspace W of V , the following three conditions on W are equivalent:
(a) W is nondegenerate for the bilinear form on V ,
(b) W ∩W ⊥= {0},
(c) V = W ⊕W ⊥.
(2) If V is nondegenerate then dim W + dim W ⊥= dim V and (W ⊥)⊥= W.
In particular, if V is nondegenerate then a subspace W is nondegenerate if and only if
W ⊥is nondegenerate.
Part (1) characterizes the subspaces of a symmetric or alternating bilinear space V that
are nondegenerate: they are exactly the subspaces of V that don’t overlap with their orthog-
onal space in V except in {0}. The validity of the conditions in part (1) for the subspace
W = {0} is a reason for declaring the zero space to be nondegenerate.
Proof. Let B be the given bilinear form on V .
(a) ⇒(b): Suppose the subspace W of V is nondegenerate for B, meaning if B(w, w′) = 0
for all w′ ∈W then w = 0. This means the only element of W that lies in W ⊥is 0, so
W ∩W ⊥= {0}.
(b) ⇒(c): Now assume W ∩W ⊥= {0}. We will show V = W +W ⊥: every element of V is
the sum of an element of W and an element of W ⊥. The linear mapping W →W ∨given by
w 7→B(w, −)|W has kernel W ∩W ⊥, which is {0}. Since dim(W ∨) = dim(W), injectivity of
w 7→B(w, −)|W implies surjectivity. Therefore to each v ∈V the linear functional B(v, −)
on W has to be of the form B(w, −) for some w ∈W: B(v, w′) = B(w, w′) for all w′ ∈W.
Then B(v−w, w′) = 0 for all w′ ∈W, so v−w ∈W ⊥. Setting v−w = u, we have v = w+u
where w ∈W and u ∈W ⊥, so V = W + W ⊥.
The representation of each v ∈V as w + u with w ∈W and u ∈W ⊥is unique: if
v = w1 + u1 = w2 + u2 with wi ∈W and ui ∈W ⊥, then w1 −w2 = u2 −u1: the left
side is in W and the right side is in W ⊥, so from W ∩W ⊥= {0} we get w1 −w2 = 0 and
u2 −u1 = 0, so w1 = w2 and u1 = u2. The uniqueness of the representation as a sum from
each subspace is precisely what it means to say V = W ⊕W ⊥.
(c) ⇒(a): If V = W ⊕W ⊥, then the only element of W that is in W ⊥is 0, so if a vector
w ∈W satisﬁes B(w, w′) = 0 for all w′ ∈W then w = 0. That is what it means for W to
be nondegenerate for B.

<!-- page 19 -->
BILINEAR FORMS
19
(2) Consider how elements of v pair with elements in W. This amounts to looking at
the map v 7→B(v, −)|W , which is the composite of LB : V →V ∨with the restriction map
V ∨→W ∨. The ﬁrst is an isomorphism (since V is nondegenerate!) and the second is onto
(why?), so the composite is onto. The kernel of the composite is W ⊥, so V/W ⊥∼= W ∨.
Taking the dimension of both sides, dim V −dim W ⊥= dim W ∨= dim W.
Easily W ⊂(W ⊥)⊥: for w ∈W and v ∈W ⊥we have B(w, v) = 0, and quantifying over
all v ∈W ⊥shows w ∈(W ⊥)⊥, so W ⊂(W ⊥)⊥. From the dimension calculation above,
dim((W ⊥)⊥) = dim V −dim(W ⊥) = dim V −(dim V −dim W) = dim W.
A containment W ⊂(W ⊥)⊥where the smaller space has the same dimension as the larger
space must be an equality, so (W ⊥)⊥= W for all subspaces W of V .
Therefore the
nondegeneracy condition W ∩W ⊥= {0} is symmetric in the roles of W and W ⊥, so W is
nondegenerate if and only if W ⊥is.
□
Example 3.13. We continue with Example 3.11. Let W be the plane in R2,1 spanned by
(1, 0, 1) and (0, 1, 0). Since ⟨·, ·⟩2,1 is nondegenerate on R2,1, dim W + dim W ⊥= 3, so W ⊥
is one-dimensional. A direct calculation shows W ⊥= R(1, 0, 1). Since W ⊥⊂W, R2,1 is
not the (direct) sum of W and W ⊥, which is consistent with W being a degenerate subspace
of R2,1.
Example 3.14. We look at the symmetric bilinear space (R2, B) in Example 3.7, which
is degenerate.
Let W = R(1, 0).
This subspace is nondegenerate, so R2 = W ⊕W ⊥.
Indeed, W ⊥= R(0, 1). However, since the whole space is degenerate we need not have
(W ⊥)⊥= W, and in fact (W ⊥)⊥= R2. Thus W is nondegenerate but W ⊥is degenerate.
Remark 3.15. Do not confuse the conditions V = W ⊕W ⊥and dim W ⊥= dim V −dim W.
The ﬁrst implies the second, but the converse is false: W and W ⊥can overlap nontrivially
while their dimensions are still complementary! See Example 3.13. By Theorem 3.12, when
V is symmetric or alternating we have dim W ⊥= dim V −dim W if V is nondegenerate
and W is an arbitrary subspace or if V is arbitrary and W is a nondegenerate subspace.
Theorem 3.16. Let (V, B) be nondegenerate.
(1) Every hyperplane3 in V has the form {w : v ⊥w} for some v ̸= 0 and {w : w ⊥v′}
for some v′ ̸= 0.
(2) If B(v, w) = B(v, w′) for all v ∈V then w = w′.
(3) If A and A′ are linear maps V →V and B(v, Aw) = B(v, A′w) for all v and w in
V then A = A′.
(4) Every bilinear form on V looks like B(v, Aw) for some linear map A: V →V .
Proof. (1) Let H ⊂V be a hyperplane.
The quotient space V/H has dimension 1, so
it is (noncanonically) isomorphic to F. Pick an isomorphism V/H ∼= F. The composite
V →V/H ∼= F is a nonzero linear map to F, with kernel H, so H = ker ϕ for some nonzero
ϕ ∈V ∨. (This has nothing to do with bilinear forms: hyperplanes in V always are kernels
of nonzero elements of the dual space of V ; the converse is true as well.) Since (V, B) is
nondegenerate, ϕ = B(v, −) for some nonzero v and ϕ = B(−, v′) for some nonzero v′, so
H = {w : B(v, w) = 0} = {w : B(w, v′) = 0}.
3A hyperplane is a subspace with dimension n −1, where n = dim V ; they are the natural complements
to 1-dimensional subspaces.

<!-- page 20 -->
20
KEITH CONRAD
(2) The hypothesis of (2) says RB(w) = RB(w′), so w = w′ since RB is an isomorphism
(this is due to B being nondegenerate).
(3) By (2), Aw = A′w for all w, so A = A′.
(4) When A: V →V is linear, let ϕA : V × V →F by ϕA(v, w) = B(v, Aw). Then ϕA is
a bilinear form on V . The correspondence A 7→ϕA is a map from EndF (V, V ) to the space
Bil(V ) of all bilinear forms on V (Exercise 1.6), and it is linear. (That is, ϕA+A′ = ϕA +ϕA′
and ϕcA = cϕA.) Part (2) says A 7→ϕA is injective. Since EndF (V, V ) and Bil(V ) have the
same dimension, this correspondence is an isomorphism.
□
Concerning the second property in Theorem 3.16, quantifying over all v ∈V is important:
if we know B(v, w) = B(v, w′) for one v then we can’t conclude w = w′, even when V = Rn
with the dot product.
Although all bilinear forms on V have the form B(v, Aw) for some linear map A: V →V ,
we can certainly write down bilinear forms in other ways, such as (v, w) 7→B(Av, w).
Theorem 3.16(d) says this bilinear form can be written as (v, w) 7→B(v, A∗w) for some
linear map A∗: V →V .
Deﬁnition 3.17. When (V, B) is nondegenerate and A: V →V is linear, the unique linear
map A∗: V →V satisfying
(3.1)
B(Av, w) = B(v, A∗w)
for all v and w in V is called the adjoint of A relative to B.
Example 3.18. On F n, let B(v, w) = v ·w. For A ∈Mn(F), Av ·w = v ·A⊤w for all v and
w in F n, so the adjoint of A relative to the dot product is the transpose of A. This close
relation between the dot product and transpose is one of the reasons that the transpose is
important, especially when F = R.
Example 3.19. On R2, let B(v, w) = v · ( 3
0
0 −2 )w. Let A = ( a b
c d ), viewed as a linear map
R2 →R2. We want to work out the map A∗: R2 →R2. For v =
 x
y

and w =
 x′
y′

in R2,
B(Av, w) = 3(ax + by)x′ −2(cx + dy)y′
= 3axx′ + 3bx′y −2cxy′ −2dyy′.
Writing A∗= ( a∗b∗
c∗d∗),
B(v, A∗w) =
3x(a∗x′ + b∗y′) −2y(c∗x′ + d∗y′)
=
3a∗xx′ −2c∗x′y + 3b∗xy′ −2d∗yy′.
Coeﬃcients must match in the two formulas for B(Av, w) and B(v, A∗w), since bilinear
forms have the same matrix, so a∗= a, b∗= −(2/3)c, c∗= −(3/2)b, and d∗= d: ( a b
c d )∗=
(
a
−(2/3)c
−(3/2)b
d
). Notice ( a b
c d )∗has the same trace and determinant as ( a b
c d ).
Remark 3.20. If B is a degenerate bilinear form on V then every part of Theorem 3.16
fails to be true and the construction of adjoint linear maps does not work. For example, let
B : F 2 × F 2 →F by B(
 x1
y1

,
 x2
y2

) = x1x2. This bilinear form is represented by the nonin-
vertible matrix ( 1 0
0 0 ): B(v, w) = v·( 1 0
0 0 )w for v, w ∈F 2. When A = ( a b
c d ), B(A
 0
1

,
 1
0

) = b
and B(
 0
1

, A′ 1
0

) = 0 for every A′ ∈M2(F), so if b ̸= 0 then there is no A′ ∈M2(F) such
that B(Av, w) = B(v, A′w) for all v, w ∈F 2.

<!-- page 21 -->
BILINEAR FORMS
21
Let’s see how to compute the matrix of the adjoint of a linear map for abstract vector
spaces when bases are chosen. The formula will show that the adjoint on EndF (V, V ) and
transpose on Mn(F) are closely related.
Theorem 3.21. Let A: V →V be linear. Fix a basis of V . In terms of this basis, let
[A], [A∗], and M be the matrices for A, A∗, and B. Then
[A∗] = M−1[A]⊤M.
Proof. We will give two proofs.
For a matrix-algebra proof, the choice of basis on V gives an isomorphism [·]: V →F n.
Let’s write both sides of (3.1) in matrix form relative to the chosen basis. The left side is
[Av] · M[w] = [A][v] · M[w] = [v] · [A]⊤M[w]
and the right side is
[v] · M[A∗w] = [v] · M[A∗][w].
Since this holds for all v and w,
[A]⊤M = M[A∗],
which is equivalent to the desired formula since M is invertible.
For a diﬀerent proof, we use the fact that M is the matrix for RB (Theorem 2.5). Since
RBA∗= A∨RB (Exercise 3.22), A∗= R−1
B A∨RB as linear maps from V to V . Passing to
matrix representations, [A∗] = M−1[A]⊤M.
□
A bilinear form B on V is essentially the same thing as a linear map L: V →V ∨(Exercise
1.6), with B and L related by B(v, w) = (L(w))(v) and B is non-degenerate if and only if L
is an isomorphism. That is, a choice of non-degenerate bilinear form on V is equivalent to
a choice of isomorphism V →V ∨. From this point of view, the construction of the adjoint
linear map A∗: V →V from a linear map A: V →V is related to the construction of the
dual linear map A∨: V ∨→V ∨, which is not surprising since the matrix representations
of A and A∨(using a basis of V and dual basis of V ∨) are matrix transposes just like the
role of the matrix transpose for [A∗] in Theorem 3.21. Since dualizing is possible for linear
maps A: V →W where W doesn’t have to equal V , that suggests that if V and W are
each equipped with a nondegenerate bilinear form, there should be an adjoint linear map
A∗: W →V that is related to the dual linear map A∨: W ∨→V ∨; see Exercise 3.23.
We will put the construction of the adjoint A∗of a linear map A: V →V to work to
answer an interesting question: when (V, B) is a nondegenerate bilinear space, we want to
describe the linear maps A: V →V that preserve orthogonality for B:
(3.2)
v ⊥w =⇒Av ⊥Aw.
(We are not requiring ⇐⇒in (3.2), but only that A carries orthogonal vectors to orthogonal
vectors.) For instance, if B(Av, Aw) = B(v, w) for all v and w (that is, if A “preserves” B)
then (3.2) holds. But (3.2) can take place under more general circumstances: if there is a
scalar c ∈F such that B(Av, Aw) = cB(v, w) for all v and w then (3.2) still holds. It turns
out that this suﬃcient condition for (3.2) is also necessary when B is nondegenerate.
Theorem 3.22. Let (V, B) be nondegenerate. For a linear transformation A: V →V , the
following properties are equivalent:
(1) v ⊥w =⇒Av ⊥Aw for all v and w in V ,
(2) there is a constant c ∈F such that B(Av, Aw) = cB(v, w) for all v and w in V .
(3) there is a constant c ∈F such that A∗A = c idV .

<!-- page 22 -->
22
KEITH CONRAD
The heart of the proof of Theorem 3.22 is the following lemma from linear algebra that
characterizes scaling transformations geometrically (and has nothing to do with bilinear
forms).
Lemma 3.23. Let V be ﬁnite-dimensional over F and L: V →V be linear.
(i) If L maps each 1-dimensional subspace of V to itself then L is a scaling transformation:
Lv = cv for some c ∈F and all v ∈V .
(ii) If L maps each hyperplane of V to itself then L is a scaling transformation: Lv = cv
for some c ∈F and all v ∈V .
Another way of describing (i) is that the only linear map V →V that has all (nonzero)
vectors in V as eigenvectors is a scaling transformation on V . Part (ii) says that a linear map
L: V →V such that L(H) ⊂H for every hyperplane H ⊂V is a scaling transformation
on V . The application of this lemma to the proof of Theorem 3.22 will use the hyperplane
case of the lemma.
Proof. To prove (i), saying L carries a 1-dimensional subspace Fv to itself, for v ̸= 0 in V ,
means L(v) = cvv for some cv ∈F. We want to show all the constants cv (as v varies)
are the same. Then calling this common value c gives us Lv = cv for all v ̸= 0 and this is
trivially also true at v = 0, so we’d be done with the case of 1-dimensional subspaces.
Pick nonzero v and v′ in V . If v and v′ are linearly dependent then v = av′ for some
a ∈F ×. Applying L to both sides,
cvv = L(v) = L(av′) = aL(v′) = acv′v′ = cv′v,
so cv = cv′ (because v ̸= 0). If v and v′ are linearly independent, then consider the constants
associated to v, v′, and v + v′. Since L(v + v′) = Lv + Lv′,
cv+v′(v + v′) = cvv + cv′v′.
By linear independence of v and v′, cv+v′ = cv and cv+v′ = cv′, so cv = cv′.
Now we turn to part (ii): assume L(H) ⊂H for every hyperplane H ⊂V . We are going
to convert this condition about all hyperplanes in V into a condition about all 1-dimensional
subspaces of the dual space V ∨, to which part (i) can be applied.
The connection between hyperplanes in V and 1-dimensional subspaces of V ∨is that
each hyperplane in V has the form ker ϕ for a nonzero ϕ ∈V ∨, with ϕ being unique up to
scaling: if ϕ and ψ are nonzero in V ∨then ker ϕ = ker ψ if and only if ψ = cϕ for some
c ∈F ×, which is the same as ϕ and ψ spanning the same 1-dimensional subspace of V ∨.
Why are ϕ and ψ scalar multiples of each other if they have the same kernel?
Let
n = dim V and {e1, . . . , en−1} be a basis of the hyperplane ker ϕ = ker ψ. Pick en outside this
hyperplane, so en in V that is outside the span of {e1, . . . , en−1} and therefore {e1, . . . , en}
is a basis of V . For each v ∈V , we can write v = Pn
i=1 aivi for unique ai ∈F. Then
ϕ(v) =
n
X
i=1
aiϕ(ei) = anϕ(en),
ψ(v) =
n
X
i=1
aiψ(ei) = anψ(en).
Since en is not in the (common) kernel of ϕ or ψ, ϕ(en) and ψ(en) are in F ×. Setting c =
ϕ(en)/ψ(en) ∈F ×, which is a number that has nothing to do with v, ϕ(v) = an(cψ(en)) =
cψ(v). This holds for all v in V , so ϕ = cψ in V ∨.
The linear map L: V →V has a dual linear map L∨: V ∨→V ∨deﬁned by L∨(ϕ) = ϕ◦L
for all ϕ ∈V ∨(that is, (L∨(ϕ))(v) = ϕ(L(v)) for v ∈V ). The hypothesis L(H) ⊂H for

<!-- page 23 -->
BILINEAR FORMS
23
all hyperplanes H in V implies L∨maps all 1-dimensional subspaces of V ∨to themselves.
Why is that?
Pick a 1-dimensional subspace of V ∨, say Fϕ for some nonzero ϕ ∈V ∨. Then H := ker ϕ
is a hyperplane in V , so by hypothesis L(H) ⊂H. That is, if ϕ(v) = 0 then ϕ(L(v)) = 0.
Since ϕ ◦L = L∨(ϕ), we obtain that if ϕ(v) = 0 then (L∨(ϕ))(v) = 0, so ker ϕ ⊂ker L∨(ϕ).
Since H = ker ϕ is a hyperplane, ker L∨(ϕ) is either H or V . Let’s consider both possibilities
separately.
(i) If ker L∨(ϕ) = H then ker L∨(ϕ) = ker ϕ, so L∨(ϕ) and ϕ are nonzero scalar multi-
ples of each other: L∨(ϕ) = cϕϕ for some cϕ ∈F ×. Thus L∨(ϕ) ∈Fϕ.
(ii) If ker L∨(ϕ) = V then L∨(ϕ) is the zero functional in V ∨and then we certainly
have L∨(ϕ) ∈Fϕ.
Either way, L∨carries every nonzero element of V ∨to a scalar multiple of itself (perhaps
the zero multiple), so L∨carries each 1-dimensional subspace of V ∨back to itself.
Now apply part (i) to the vector space V ∨and linear map L∨: V ∨→V ∨: for some
c ∈F, L∨(ϕ) = cϕ for all ϕ ∈V ∨. Applying both sides of that equation to v ∈V , we get
ϕ(L(v)) = cϕ(v) = ϕ(cv) for all ϕ ∈V ∨. Two vectors in V at which all elements of the dual
space are equal must themselves be equal (think about applying all members of a dual basis
in V ∨to the vectors in V and what the equal values mean about the coordinates of those
two vectors for the basis of V having the chosen dual basis in V ∨). Therefore L(v) = cv in
V . This holds for all v ∈V , so L = c idV .
□
Now we prove Theorem 3.22.
Proof. Trivially (2) implies (1). To show (1) implies (2), (1) tells us that if B(v, w) = 0 then
B(Av, Aw) = 0, so B(v, A∗Aw) = 0. When v ̸= 0, {w : v ⊥w} is a hyperplane in V and
A∗A carries this hyperplane back to itself. Every hyperplane in V has the form {w : v ⊥w}
for some nonzero v (Theorem 3.16(1)), so A∗A carries every hyperplane of V into itself.
Therefore A∗A = c idV for some c ∈F by Lemma 3.23.
To show (2) and (3) are equivalent, (2) is the same as B(v, A∗Aw) = B(v, cw) for all v
and w, which is equivalent to A∗A = c idV by Theorem 3.16(3).
□
Example 3.24. Let B(v, w) = v · ( 3
0
0 −2 )w on R2. Theorem 3.22 says that a matrix ( a b
c d )
preserves B-orthogonality exactly when it aﬀects B-values by a universal scaling factor. We
will ﬁnd such a matrix, which will amount to solving a system of equations.
We found in Example 3.19 that
  a b
c d
∗=

a
−(2/3)c
−(3/2)b
d

, so

a
b
c
d
∗
a
b
c
d

=

a2 −(2/3)c2
ab −(2/3)cd
−(3/2)ab + cd
−(3/2)b2 + d2

.
The product is a scalar diagonal matrix when ab = (2/3)cd and a2 −(2/3)c2 = d2 −(3/2)b2.
Take b = 2 and c = 3 (to avoid denominators), so our conditions reduce to a = d. Therefore
A = ( a 2
3 a ), with A∗A = (a2 −6)I2. Let a = 4, just to ﬁx ideas, so A = ( 4 2
3 4 ) satisﬁes
B(Av, Aw) = 10B(v, w).
Example 3.25. On R2 let B(v, w) = v · (
0 1
−1 0 )w. This is the bilinear form from Example
1.5 and it’s nondegenerate since the matrix (
0 1
−1 0 ) is invertible. For all v ∈R2, v ⊥v (that
is, B(v, v) = 0). Therefore every 2 × 2 matrix A ∈M2(R) with a 1-dimensional image in
R2 satisﬁes Av ⊥Aw for all v and w in R2 (whether or not v ⊥w initially), so Theorem
3.22(1) and (2) are satisﬁed, where the constant in (2) is 0. Using the calculation of A∗in

<!-- page 24 -->
24
KEITH CONRAD
terms of A in Exercise 3.17, check A∗A = (det A)I2 = O since det A = 0 when A is not
surjective. So for such A, the constant in Theorem 3.22(3) is 0.
Although A∗satisﬁes many properties of the transpose (Exercise 3.19), there is an impor-
tant distinction: while (A⊤)⊤= A, sometimes A∗∗̸= A. Let’s see why. Applying Theorem
3.21 twice,
[A∗∗] = M−1M⊤[A](M−1)⊤M,
so A∗∗= A for all A only when M−1M⊤is a nonzero scalar matrix. (Abstractly, this means
R−1
B LB is a nonzero scaling transformation.) Right away we see that in the most important
cases of symmetric or alternating bilinear forms, where M⊤= ±M, we do have A∗∗= A,
but in other cases it need not happen. (An example is in Exercise 3.18.)
The conceptual reason that A∗∗might not equal A is that the deﬁnition of the adjoint
had a built-in bias: it is deﬁned to satisfy B(Av, w) = B(v, A∗w) for all v and w rather than
B(v, Aw) = B(A∗v, w) for all v and w. The second equation would deﬁne another adjoint
for A, just as LB and RB are alternate isomorphisms of V with V ∨. See Exercise 3.21.
Table 1 collects several constructions we have met.
Coordinate-free
Matrix Version
Bilinear form B
B(v, w) = [v] · M[w]
Change of basis
M ⇝C⊤MC
B is symmetric
M⊤= M
B is skew-symmetric
M⊤= −M
B is alternating
M⊤= −M, diagonals = 0
B is nondegenerate
M is invertible
A∗
M−1[A]⊤M
Table 1. Abstract and Concrete Viewpoints
Exercises.
1. In R2,2, let W be the plane spanned by (1, 0, 0, 0) and (0, 0, 1, 0). Compute W ⊥. Is
W a degenerate subspace?
2. Let (V, B) be a bilinear space with B not identically zero. If B is symmetric show
V has a one-dimensional nondegenerate subspace. If B is alternating show V has a
two-dimensional nondegenerate subspace.
3. Let (V, B) be symmetric or alternating. Show B induces a nondegenerate bilinear
form on V/V ⊥. Writing V = V ⊥⊕W for any subspace W that is complementary
to V ⊥, show W is nondegenerate.
4. A 2-dimensional symmetric or alternating bilinear space is called a hyperbolic plane
if it has a basis {v, w} such that v ⊥v, w ⊥w, and B(v, w) = 1 (so B(w, v) = ±1).
A pair of vectors with these three properties is called a hyperbolic pair. If V is a
nondegenerate symmetric or alternating bilinear space and v0 ⊥v0 for some nonzero
v0 in V , show every nondegenerate plane in V containing v0 is a hyperbolic plane
with v0 as one member of a hyperbolic pair except perhaps if F has characteristic
2 and B is symmetric but not alternating.

<!-- page 25 -->
BILINEAR FORMS
25
5. When F has characteristic 2 and B(v, w) = v · ( 1 1
1 0 )w for v, w ∈F 2, show (0, 1) ⊥
(0, 1) but there is no hyperbolic pair in F 2. Therefore the exceptional case in the
previous exercise does occur.
6. Check that the reasoning in Example 3.4 shows the dot product on every F n is
nondegenerate. Why doesn’t the argument in Example 3.3 show this?
7. Does the ﬁrst result in Theorem 3.16 characterize nondegeneracy? That is, if each
hyperplane in V has the form {w : v ⊥w} for some v ̸= 0, is V nondegenerate?
8. Show B in Exercise 2.8 is nondegenerate if and only if 4|m. (What should nonde-
generate mean?)
9. Fix a nondegenerate bilinear form B on V . For a linear map A: V →V , show the
bilinear form on V given by (v, w) 7→B(v, Aw) is nondegenerate if and only if A is
invertible.
10. If V1 and V2 are bilinear spaces, show their orthogonal direct sum V1 ⊥V2 is non-
degenerate if and only if V1 and V2 are nondegenerate.
11. Suppose V is symmetric or alternating, and nondegenerate. For any subspaces W1
and W2, show
(W1 + W2)⊥= W ⊥
1 ∩W ⊥
2 ,
(W1 ∩W2)⊥= W ⊥
1 + W ⊥
2 .
Show a subspace W is nondegenerate if and only if V = W + W ⊥.
12. Let V be symmetric or alternating with a subspace W such that dim W +dim W ⊥=
dim V . If U is a subspace of W ⊥such that U + W = V , then show U = W ⊥.
13. For a subspace W ⊂V , where dim V is ﬁnite, set W ′ = {ϕ ∈V ∨: ϕ(w) =
0 for all w ∈W}. Show dim W + dim W ′ = dim V .
14. Let (V, B) be nondegenerate, but not necessarily symmetric or alternating. For any
subspace W of V , set W ⊥L = {v ∈V : v ⊥W} and W ⊥R = {v ∈V : W ⊥v}. Show
W ⊥L and W ⊥R both have dimension dim V −dim W and W ⊥L⊥R = W ⊥R⊥L = W.
15. A bilinear map B : V ×W →F is called perfect if the induced linear maps V →W ∨
given by v 7→B(v, −), and W →V ∨given by w 7→B(−, w), are isomorphisms. For
example, the natural evaluation pairing V ×V ∨→F where (v, ϕ) 7→ϕ(v) is perfect,
and a bilinear form B : V × V →F is perfect exactly when it is nondegenerate.
For a subspace U ⊂V , set U⊥= {w ∈W : B(U, w) = {0}}. If B : V × W →F is
perfect, show the map U ×(W/U⊥) →F deﬁned by (u, w) = B(u, w) is well-deﬁned
and perfect.
16. Use Theorem 3.21 to recompute the adjoint in Example 3.19.
17. On R1,1, show ( a b
c d )∗= (
a −c
−b
d ) using Theorem 3.21. Relative to the bilinear form
on R2 from Example 1.5, show ( a b
c d )∗= ( −d
b
c −a ).
18. Let B(v, w) = v · ( 1 2
0 1 )w on R2. In (R2, B), show ( 0 1
1 0 )∗∗̸= ( 0 1
1 0 ).
19. With A ⇝A∗deﬁned as in (3.1), verify the following.
(1) (A1 + A2)∗= A∗
1 + A∗
2 and (cA)∗= cA∗,
(2) id∗
V = idV ,
(3) (A1A2)∗= A∗
2A∗
1,
(4) (A∗)−1 = (A−1)∗if A ∈GL(V ),
(5) det A∗= det A, Tr A∗= Tr A, and A and A∗have the same characteristic
polynomial.
20. Let n = dim V ≥2 and ﬁx an integer d from 1 to n−1. If L: V →V is a linear map
carrying every d-dimensional subspace to itself show L is a scaling transformation.

<!-- page 26 -->
26
KEITH CONRAD
(Hint: Show by induction on the subspace dimension that L sends every hyperplane
of V to itself, so Theorem 3.23 applies.)
21. If (V, B) is nondegenerate and A: V →V is linear, deﬁne an adjoint A† : V →V
by B(v, A(−)) = B(A†v, −) in V ∨: B(v, Aw) = B(A†v, w) for all v and w in V .
When B is represented by the matrix M in a basis, what is the matrix for A† in
that basis?
22. Let (V, B) be nondegenerate. The bilinear form B gives us two ways of identifying
V with V ∨: LB(v) = B(v, −) and RB(v) = B(−, v).
For a linear map A: V →V , the dual map A∨: V ∨→V ∨does not depend on
B, while A∗does. Show A∗ﬁts into the following commutative diagram, where the
columns are isomorphisms (depending on B).
V
RB 
A∗
/ V
RB

V ∨
A∨/ V ∨
What is the corresponding commutative diagram connecting A∨and A† in the
previous exercise?
23. Redo the material on adjoints in this section so it applies to linear maps between
diﬀerent nondegenerate bilinear spaces. If A: V1 →V2 is linear then the adjoint
should be a map A∗: V2 →V1. In particular, rework the previous exercise (and its
application to Theorem 3.21) in this setting.
4. Orthogonal bases
Part of the geometric structure of Rn is captured by the phrase “orthogonal basis.” This
is a basis of mutually perpendicular vectors, and the lines through these vectors provide an
orthogonal set of axes for Rn. Let’s generalize this idea.
Fix for this section a symmetric bilinear space (V, B).
Deﬁnition 4.1. A basis {e1, . . . , en} of V is orthogonal when ei ⊥ej = 0 for i ̸= j.
Our convention in the one-dimensional case, where there aren’t basis pairs {ei, ej} with
i ̸= j to compare, is that any basis is orthogonal. The zero bilinear space has no orthogonal
basis (its basis is empty).
Example 4.2. On R2, let B(v, w) = v ·( 2 0
0 3 )w. The basis {(1, 0), (0, 1)} is orthogonal with
respect to B.
Example 4.3. On R2, let B(v, w) = v · ( 0 1
1 0 )w. The basis {(1, 0), (0, 1)} is not orthogo-
nal: B((1, 0), (0, 1)) = 1. In fact, there is no orthogonal basis containing (1, 0) since the
only vectors orthogonal to (1, 0) are scalar multiples of (1, 0). (We will understand this
phenomenon better in Remark 4.9.) An orthogonal basis for B is {(1, 1), (1, −1)}.
Example 4.4. When B is identically zero, any basis of V is an orthogonal basis.
Geometrically, an orthogonal basis of V gives a decomposition of V into an orthogonal
direct sum of lines: V = W1 ⊥W2 ⊥· · · ⊥Wn, where Wi = Fei.
While Euclidean space has the more reﬁned notion of an orthonormal basis, we will ﬁnd
essentially no use for this idea. The reason is that it usually doesn’t exist! An orthonormal
basis should be an orthogonal basis {e1, . . . , en} in which B(ei, ei) = 1 for all i. But there is

<!-- page 27 -->
BILINEAR FORMS
27
no orthonormal basis in Example 4.2 using Q2 in place of R2 since the equation 2x2+3y2 = 1
has no rational solutions (Exercise 4.7).
The matrix representing a bilinear form in an orthogonal basis is diagonal, and thus is
a symmetric matrix. This is why we only deﬁned orthogonal bases for symmetric bilinear
spaces. Our basic task in this section is to prove any symmetric bilinear space (degenerate
or nondegenerate) admits an orthogonal basis provided the scalar ﬁeld F does not have
characteristic 2. In characteristic 2 we will see there are problems.
Lemma 4.5. If B is not identically zero and the characteristic of F is not 2 then B(v, v) ̸= 0
for some v ∈V .
Proof. See Theorem 1.8 for one proof. For another proof, let’s show the contrapositive. If
B(v, v) = 0 for all v then B is alternating, or equivalently (since we are not in characteristic
2) skew-symmetric. The only bilinear form that is both symmetric and skew-symmetric
outside of characteristic 2 is identically zero.
□
Lemma 4.6. Let v ∈V satisfy B(v, v) ̸= 0. Then V = Fv ⊥v⊥. If V is nondegenerate
then the subspace v⊥is nondegenerate.
Notice this is valid in characteristic 2.
Proof. Since B is nondegenerate on the subspace Fv, this lemma is a consequence of The-
orem 3.12, but we give a self-contained proof anyway.
Since B(v, v) ̸= 0, every element of F is a scalar multiple of B(v, v). For v′ ∈V , let
B(v′, v) = cB(v, v) for c ∈F. Then B(v′ −cv, v) = 0, so v′ −cv ∈v⊥. Therefore the
equation
v′ = cv + (v′ −cv)
shows V = Fv +v⊥. Since v ̸∈v⊥(because B(v, v) ̸= 0), we have Fv ∩v⊥= {0}. Therefore
V = Fv ⊕v⊥. This direct sum is an orthogonal direct sum since v ⊥w for every w ∈v⊥.
To show B is nondegenerate on v⊥when it is nondegenerate on V , suppose some v′ ∈v⊥
satisﬁes B(v′, w) = 0 for all w ∈v⊥. Since B(v′, v) = 0, B(v′, cv + w) = 0 for any c ∈F
and w ∈v⊥. Since Fv + v⊥= V , we have v′ = 0 by nondegeneracy of B on V . Thus B is
nondegenerate on v⊥.
□
Theorem 4.7. There is an orthogonal basis for V when F does not have characteristic 2.
Proof. We argue by induction on n = dim V . The result is automatic when n = 1, so take
n ≥2 and assume the theorem for spaces of smaller dimension.
If B is identically 0, then any basis of V is an orthogonal basis. If B is not identically 0,
then B(v, v) ̸= 0 for some v (Lemma 4.5). Using any such v, Lemma 4.6 says V = Fv ⊥v⊥.
Since v⊥is a symmetric bilinear space with dimension n −1, by induction there is an
orthogonal basis of v⊥, say {e1, . . . , en−1}. The set {e1, . . . , en−1, v} is a basis of V . Since
ei ⊥v for all i, this basis is orthogonal.
□
Taking into account how the matrix for a bilinear form changes when the basis changes,
Theorem 4.7 is equivalent to the following matrix-theoretic result: given any symmetric
matrix M over a ﬁeld of characteristic not 2, there exists an invertible matrix C such that
C⊤MC (not C−1MC) is a diagonal matrix.
Corollary 4.8. Let {e1, . . . , en} be an orthogonal basis for V . Then V is nondegenerate if
and only if ei ̸⊥ei for each i.

<!-- page 28 -->
28
KEITH CONRAD
Proof. The matrix for B associated to the orthogonal basis is diagonal, where the diagonal
entries are the numbers B(ei, ei). Non-degeneracy of B is equivalent to invertibility of this
diagonal matrix, which is equivalent to B(ei, ei) ̸= 0 for all i.
□
Remark 4.9. In Euclidean space, every nonzero vector is part of an orthogonal basis. The
proof of Theorem 4.7 generalizes this: in a symmetric bilinear space outside of characteristic
2, any vector v with v ̸⊥v is part of an orthogonal basis. (If v ⊥v then Corollary 4.8 says
v won’t be part of an orthogonal basis if V is nondegenerate, e.g., (1, 0, 1) is not part of
an orthogonal basis of R2,1 and (1, 0) is not part of an orthogonal basis in Example 4.3.)
Whether in Euclidean space or the more general setting of a symmetric bilinear space, the
inductive construction of an orthogonal basis is the same: pick a suitable starting vector
v, pass to the orthogonal space v⊥, which has dimension one less, and then induct on
the dimension of the space. In the proof of Lemma 4.6, the projection from V to v⊥via
v′ ⇝v′ −cv = v′ −(B(v′, v)/B(v, v))v is exactly the idea in the classical Gram-Schmidt
orthogonalization process.
Example 4.10. We look at Example 4.3 over a general ﬁeld F: on F 2 let B(v, w) =
v · ( 0 1
1 0 )w. When F does not have characteristic 2, the basis {(1, 1), (1, −1)} is orthogonal.
When F has characteristic 2, (1, 1) = (1, −1) so this construction of an orthogonal basis
breaks down. In fact, in characteristic 2 there is no orthogonal basis of (F 2, B). We give
two proofs.
First, suppose there is an orthogonal basis {v0, w0}. Since 2 = 0 in F, B((x, y), (x, y)) =
2xy = 0, so v0 ⊥v0. Since v0 is orthogonal to both v0 and w0, v0 ⊥F 2. This contradicts
nondegeneracy of B.
Our second proof is matrix-theoretic. In order for B to have an orthogonal basis, there
must be an invertible matrix C = ( a b
c d ) such that C⊤( 0 1
1 0 )C is a diagonal matrix. Since
C⊤( 0 1
1 0 )C = (
2ac
ad+bc
ad+bc
2bd ), the diagonal terms always vanish in characteristic 2. Therefore
this matrix can’t be a diagonal matrix in characteristic 2: it would then be the zero matrix,
but its determinant is −(det C)2 ̸= 0.
Despite the behavior of Example 4.10, there is something worthwhile to say about the
existence of an orthogonal basis for (nondegenerate) symmetric bilinear forms in character-
istic 2. But we need to know something more. The situation will be explained in Exercise
5.4.
Exercises.
1. On Q3, let B be the bilinear form represented by the symmetric matrix


1
2
1
2
1
2
1
2
0


in the standard basis. Find an orthogonal basis for B.
2. View M2(F) as a bilinear space relative to the trace form B(L, L′) = Tr(LL′) as
in Example 1.12. Show ( 1 0
0 0 ) ⊥( 0 1
0 0 ) and explain why ( 0 1
0 0 ) can’t be part of an
orthogonal basis. Find an orthogonal basis when F does not have characteristic 2.
Is there an orthogonal basis when F has characteristic 2?
3. Repeat the previous exercise with B(L, L′) = Tr(LL′⊤) on M2(F).
4. Here is a “proof” that when V is symmetric any v ̸= 0 is part of an orthogonal
basis. Let n = dim V . The orthogonal space v⊥has dimension n or n −1. Let H

<!-- page 29 -->
BILINEAR FORMS
29
be an (n −1)-dimensional subspace of v⊥. By induction H has an orthogonal basis
{e1, . . . , en−1}. Since ei ⊥v for all i, v is linearly independent from this basis so
{e1, . . . , en−1, v} is an orthogonal basis of V . Where is the error?
5. As a supplement to Remark 4.9, show when B is symmetric that a nonzero vector
v with B(v, v) = 0 is part of an orthogonal basis if and only if v ∈V ⊥.
6. Let V be symmetric. Show any orthogonal basis for a nondegenerate subspace of V
can be extended to an orthogonal basis of V . (Hint: Use Theorem 3.12.)
7. Show the equation 2x2 + 3y2 = 1 has no rational solutions. (Hint: If it did, clear
the denominator to write 2a2 +3b2 = c2 for integers a, b, and c, where none of them
are 0. Work mod 3 to show a, b, and c are all multiples of 3. Then divide a, b, and
c by 3 and repeat.)
8. Let (V, B) be nondegenerate and symmetric, so V ∼= V ∨by v 7→B(v, −). Under
this isomorphism, show that a basis of V is its own dual basis (a “self-dual” basis) if
and only if it is an orthonormal basis of (V, B), i.e., an orthogonal basis {e1, . . . , en}
where B(ei, ei) = 1 for all i. Does M2(R) with the trace form have a “self-dual”
basis?
5. Symplectic bases
We now turn from symmetric bilinear spaces to alternating bilinear spaces. Before we
ﬁnd a good analogue of orthogonal bases, we prove a dimension constraint on nondegenerate
alternating spaces.
Theorem 5.1. If (V, B) is a nondegenerate alternating bilinear space, then dim V is even.
Proof. First we give a proof valid outside of characteristic 2. When the characteristic is not
2, the alternating property is equivalent to skew-symmetry. Letting M be a matrix repre-
sentation for the bilinear form, skew-symmetry is equivalent to M = −M⊤by Theorem 2.7.
Taking determinants, det M = (−1)dim V det M. Since the bilinear form is nondegenerate,
M is invertible, so we can cancel det M: 1 = (−1)dim V . Since the characteristic is not 2,
dim V is even.
Now we prove dim V is even by a method that is valid in all characteristics. We induct
on the dimension. If dim V = 1 with basis {v}, then B is identically 0 since B(cv, c′v) =
cc′B(v, v) = 0. This contradicts nondegeneracy, so dim V ≥2. If dim V = 2 we are done,
so assume dim V > 2.
Pick v ̸= 0 in V . The function B(v, −): V →F is onto by nondegeneracy, so there is
w ∈V such that B(v, w) = 1. Let U = Fv + Fw, so dim U = 2. The matrix for B|U
with respect to the basis {v, w} is (
0 1
−1 0 ), which is invertible, so the restriction of B to
U is nondegenerate. By Theorem 3.12, V = U ⊕U⊥and the restriction of B to U⊥is
nondegenerate. By induction dim U⊥is even, so dim V is even.
□
Example 5.2. Let Bu be the alternating bilinear form on R3 in Example 1.11, with u ̸= 0.
Since the space has odd dimension Bu must be degenerate, and indeed (R3)⊥= Ru relative
to Bu.
The proof of Theorem 5.1 provides us, given any nonzero v ∈V , a second vector w ∈V
such that
• B(v, w) = 1,
• V = U ⊥U⊥, where U = Fv + Fw,
• the restrictions of B to U and U⊥are nondegenerate.

<!-- page 30 -->
30
KEITH CONRAD
Rather than getting a splitting of the space into a line and its orthogonal space, as in
Lemma 4.6, we get a splitting of the space into a plane and its orthogonal space.
Deﬁnition 5.3. Let (V, B) be nondegenerate and alternating with dimension 2m ≥2. A
symplectic basis of V is a basis e1, f1, . . . , em, fm such that B(ei, fi) = 1 and the planes
Ui = Fei + Ffi are mutually perpendicular.
There is a built-in asymmetry between the ei’s and fi’s when the characteristic is not 2
since B(ei, fi) = 1 and B(fi, ei) = −1.
Using induction on the dimension, starting with the decomposition V = U ⊥U⊥above,
our work so far in this section proves the following.
Theorem 5.4. Any nondegenerate alternating bilinear space has a symplectic basis.
There are two standard ways to order a symplectic basis: the ordering e1, f1, . . . , em, fm
and the ordering e1, . . . , em, f1, . . . , fm. We could call the ﬁrst ordering numerical and the
second ordering alphabetical, but that is nonstandard terminology.
In the plane Ui, the matrix of B|Ui with respect to the (ordered) basis {ei, fi} is (
0 1
−1 0 ), so
the matrix of B on V with respect to the (ordered) basis {e1, f1, . . . , em, fm} has m blocks
(
0 1
−1 0 ) along the main diagonal and 0 elsewhere:
(5.1)
[B] =
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

0
1
0
0
· · ·
0
0
−1
0
0
0
· · ·
0
0
0
0
0
1
· · ·
0
0
0
0
−1
0
· · ·
0
0
...
...
...
...
...
...
...
0
0
0
0
· · ·
0
1
0
0
0
0
· · ·
−1
0
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

.
The word symplectic is Greek for “complex.” An alternating bilinear space with a sym-
plectic basis is “almost complex,” for instance it is even-dimensional and in a suitable basis
the bilinear form is a matrix of blocks (
0 1
−1 0 ), which is the matrix for multiplication by i
on the complex numbers in the basis {i, 1}.
If we order the symplectic basis alphabetically as {e1, . . . , em, f1, . . . , fm}, then the matrix
for B looks like (
O
Im
−Im O ). The formula for B in these coordinates, writing a typical element
of F 2m as a pair of m-tuples (x, y), is
B((x, y), (x′, y′))
=
x1y′
1 −y1x′
1 + · · · + xmy′
m −ymx′
m
=

x1
x′
1
y1
y′
1
 + · · · +

xm
x′
m
ym
y′
m
 .
(5.2)
This is a sum of m copies of the basic alternating form in Example 1.5. Notice (5.1) and
(5.2) are determined by m = (1/2) dim V alone (except for the issue of the basis ordering).
The following is a precise statement along these lines.
Corollary 5.5. Any two nondegenerate alternating bilinear spaces with the same dimension
are equivalent.
Proof. The dimension is even. Write it as 2m. Using a suitable ordering of a symplectic
basis, the matrix for a nondegenerate alternating bilinear form is (
O
Im
−Im O ). Since all non-
degenerate alternating bilinear forms in dimension 2m can be brought to a common matrix
representation (in suitably chosen bases), these forms are equivalent by Theorem 2.11.

<!-- page 31 -->
BILINEAR FORMS
31
Alternatively, we can argue by induction.
We already know any two nondegenerate
alternating bilinear spaces in dimension 2 are equivalent (sending a symplectic basis {e, f} to
a symplectic basis {e′, f′} sets up the equivalence). Letting V and V ′ have dimension at least
4, split oﬀnondegenerate planes U and U′ from both: V = U ⊥U⊥and V ′ = U′ ⊥U′⊥.
From the 2-dimensional case, U and U′ are equivalent. By induction on the dimension, U⊥
and U′⊥are equivalent. Therefore V and V ′ are equivalent.
□
Thus, although there can be many inequivalent nondegenerate symmetric bilinear forms
in a given dimension depending on the ﬁeld (Example 2.13), over any ﬁeld there is essentially
just one nondegenerate alternating bilinear form in each even dimension and it looks like
(5.1) in suitable coordinates. The bilinear form on F 2m represented by the matrix (5.1)
relative to the standard basis is called the standard alternating bilinear form on F 2m, and
the standard basis of F 2m is a symplectic basis for it.
Suppose now that (V, B) is an alternating bilinear space that is degenerate: V ⊥̸= {0}.
What kind of basis can we use on V that is adapted to B? Pick any vector space complement
to V ⊥in V , and call it W: V = W ⊕V ⊥. (This decomposition is not canonical, since there
are many choices of W, although dim W = dim V −dim V ⊥is independent of the choice of
W.) Since W ∩V ⊥= {0}, B is nondegenerate on W. Therefore the restriction B|W has a
symplectic basis. Augmenting a symplectic basis of W with any basis of V ⊥gives a basis
of V with respect to which B is represented by a block diagonal matrix
(5.3)


O
Ir
O
−Ir
O
O
O
O
O

,
where 2r = dim W = dim(V/V ⊥). This matrix is completely determined by dim V and
dim V ⊥, so all alternating bilinear forms on vector spaces with a ﬁxed dimension and a ﬁxed
“level” of degeneracy (that is, a ﬁxed value for dim V ⊥) are equivalent. The nondegenerate
case is dim V ⊥= 0.
We end this section with an interesting application of Corollary 5.5 to the construction
of an “algebraic” square root of the determinant of alternating matrices. (Recall a matrix
M is called alternating when M⊤= −M and the diagonal entries of M equal 0.)
Lemma 5.6. The determinant of any invertible alternating matrix over a ﬁeld F is a
nonzero perfect square in F.
Proof. Let M be an invertible alternating n×n matrix. On F n, the bilinear form B(v, w) =
v · Mw is nondegenerate and alternating. Therefore n is even, say n = 2m, and B has the
matrix representation (
O
Im
−Im O ) in a suitable basis. Letting C be the change of basis from
the standard basis of F n to this other basis, C⊤MC = (
O
Im
−Im O ). Taking determinants,
(det C)2 det M = 1, so det M is a nonzero square in F.
□
Example 5.7. When n = 2,
det

0
x
−x
0

= x2.
Example 5.8. When n = 4,
det




0
x
y
z
−x
0
a
b
−y
−a
0
c
−z
−b
−c
0



= (xc −yb + az)2.

<!-- page 32 -->
32
KEITH CONRAD
Let’s look at the generic example of an alternating matrix in characteristic 0. For a
positive even integer n = 2m, let xij for 1 ≤i < j ≤n be independent indeterminates over
Q. The matrix
(5.4)
M(xij) =









0
x12
x13
x14
· · ·
x1n
−x12
0
x23
x24
· · ·
x2n
−x13
−x23
0
x34
· · ·
x3n
−x14
−x24
−x34
0
· · ·
x4n
· · ·
· · ·
· · ·
· · ·
...
· · ·
−x1n
−x2n
−x3n
−x4n
· · ·
0









is the “generic” alternating matrix over Q. View it as a matrix over the ﬁeld F = Q(xij)
obtained by adjoining all the xij’s to Q. (The total number of variables here is n(n−1)/2.)
The determinant lies in Z[xij]. It is not the zero polynomial, since for instance when we
set x12 = x34 = · · · = xn−1 n = 1 and the other xij’s to 0 we get the block diagonal matrix
with blocks (
0 1
−1 0 ), whose determinant is 1. Thus M(xij) ∈GLn(Q(xij)), so det M(xij) is
a nonzero perfect square in Q(xij) by Lemma 5.6.
Since the determinant of M(xij) actually lies in Z[xij], which is a unique factorization
domain and has fraction ﬁeld Q(xij), det M(xij) is a square in Z[xij]:
(5.5)
det(M(xij)) = (Pf(xij))2
for some integral polynomial Pf(xij) in the xij’s. This polynomial is called the Pfaﬃan of
M(xij). It is determined by (5.5) only up to an overall sign. Except for the determination of
this sign, which we will deal with in a moment, (5.5) shows by specializing the variables xij
into any ﬁeld, or any commutative ring for that matter, that there is a universal algebraic
formula for a square root of the determinant of an alternating matrix. Since det M(xij) is a
homogeneous polynomial of degree n, Pf(xij) is a homogeneous polynomial of degree n/2.
(We perhaps should write Pfn to indicate the dependence on n, but this is not done for the
determinant notation det and we follow that tradition for Pf too.)
To ﬁx the sign in the Pfaﬃan polynomial Pf(xij), we can specify the value of this poly-
nomial at one nonzero specialization of its variables. The matrix in (5.4) with each xi i+1
equal to 1 for odd i and the other xij’s equal to 0 has determinant 1, whose square roots
are ±1. Choosing the square root as 1 pins down the sign on the Pfaﬃan. That is, deﬁne
Pf(xij) to be the polynomial over Z satisfying (5.5) and the condition that Pf([B]) = 1
where [B] is the block matrix in (5.1). (Equivalently, we choose the sign on Pf(xij) so that
the coeﬃcient of x12x34 · · · x2m−1 2m in Pf(xij) is 1.) This makes the Pfaﬃan for n = 2 and
n = 4 the polynomials that are being squared on the right side in Examples 5.7 and 5.8,
e.g., Pf(x) = x (not −x).
When A = (aij) is an n × n alternating matrix, for even n, we write Pf A for the
specialization of Pf(xij) using xij = aij. Since a Pfaﬃan is a square root of a determinant,
you might think it should be multiplicative “up to sign.” However, the product of two
alternating matrices is not alternating even up to sign (try the 2× 2 case!), so we can’t talk
about the Pfaﬃan of a product of alternating matrices. Using Jordan algebras (a certain
type of nonassociative algebra), the Pfaﬃan can be interpreted as a kind of determinant.
See [5, Sect. 7].
Theorem 5.9. Let n be even. For n × n matrices M and C, where M is alternating,
Pf(C⊤MC) = (det C) Pf M.

<!-- page 33 -->
BILINEAR FORMS
33
Proof. This is obvious up to sign, by squaring both sides and using properties of the deter-
minant. The point is to pin down the sign correctly. It suﬃces to verify the equation as
a universal polynomial identity over Z where M = M(xij) is a generic n × n alternating
matrix in n(n −1)/2 variables and C = (yij) is a generic n × n matrix in n2 extra vari-
ables. Specialize C to be the n × n identity matrix. Then Pf(C⊤MC) becomes Pf M and
(det C) Pf M becomes Pf M, so the two sides of the identity are equal as polynomials.
□
Exercises.
1. In Example 1.11, ﬁnd a basis of R3 in which Bu has a matrix representation (5.3)
when u ̸= 0.
2. On F 2m with the standard alternating bilinear form represented by (
O
Im
−Im O ), show
a matrix ( A B
C D ) ∈M2m(F) acting on F 2m has adjoint matrix ( D⊤
−B⊤
−C⊤
A⊤).
3. Let V be m-dimensional over F and let B be the alternating bilinear form on V ⊕V ∨
from Example 1.13. It is nondegenerate by Example 3.6. When {e1, . . . , em} is a
basis of V and {e∨
1 , . . . , e∨
m} is the dual basis of V ∨, show {e1, e∨
1 , . . . , em, e∨
m} is a
symplectic basis of V ⊕V ∨and the matrix for B in these coordinates is (5.1).
4. Let (V, B) be nondegenerate and symmetric over a ﬁeld of characteristic 2. Re-
call the alternating bilinear forms are a subset of the symmetric bilinear forms in
characteristic 2. Prove (V, B) has an orthogonal basis if and only if B is not al-
ternating. (Hint: Without loss of generality, dim V ≥2. The only if direction is
trivial by Corollary 4.8. For the if direction, pick v0 such that a := B(v0, v0) ̸= 0.
Then v⊥
0 is nondegenerate by Lemma 4.6. If B is nonalternating on v⊥
0 then we’re
done by induction. If B is alternating on v⊥
0 then v⊥
0 has a symplectic basis, say
including a pair {e, f} with B(e, f) = 1, B(e, e) = 0, and B(f, f) = 0.
Show
B(v0 + e + f, v0 + e + f) ̸= 0 and B is nonalternating on (v0 + e + f)⊥.)
5. Check Example 5.8.
6. Let M be an n × n alternating matrix, where n is even.
(1) Show Pf(M⊤) = (−1)n/2 Pf M.
(2) If M is not invertible, show Pf M = 0. If M is invertible and C is an invertible
matrix such that C⊤MC is the matrix in (5.1), show Pf M = 1/ det C.
6. Quadratic forms
Concretely, a quadratic form is a homogeneous polynomial of degree 2, such as x2+y2+z2
or x2+5xy−y2. We call the ﬁrst one a diagonal quadratic form since it has no mixed terms.
The second quadratic form is not diagonal, but becomes so by completing the square:
x2 + 5xy −y2 =

x + 5
2y
2
−29
4 y2 = x′2 −29y′2,
where x′ = x + 5
2y and y′ = 1
2y.
The simplest n-variable quadratic form is x2
1 + · · · + x2
n, which plays an important role
in the geometry of Rn and is closely related to the dot product: we have
x2
1 + · · · + x2
n = v · v,

<!-- page 34 -->
34
KEITH CONRAD
where v = (x1, . . . , xn). Conversely, the dot product of two vectors v and w in Rn can be
expressed in terms of sums of squares:
(6.1)
v · w = 1
2(Q(v + w) −Q(v) −Q(w)),
where Q(x1, . . . , xn) = x2
1 + · · · + x2
n (check!).
When n = p + q, another quadratic form is
Qp,q(x1, . . . , xn) = x2
1 + · · · + x2
p −x2
p+1 −· · · −x2
p+q.
For v ∈Rn we have Qp,q(v) = ⟨v, v⟩p,q, and we can express ⟨·, ·⟩p,q in terms of Qp,q by a
formula similar to (6.1):
⟨v, w⟩p,q = 1
2(Qp,q(v + w) −Qp,q(v) −Qp,q(w)).
The relation (6.1) between a sum of squares (a particular quadratic form) and the dot
product (a particular bilinear form), as well as between Qp,q and ⟨·, ·⟩p,q, motivates the
following coordinate-free deﬁnition of a quadratic form.
Deﬁnition 6.1. A quadratic form on a vector space V over a ﬁeld F with characteristic
not 2 is a function Q: V →F such that
(1) Q(cv) = c2Q(v) for v ∈V and c ∈F,
(2) the function B(v, w) := 1
2(Q(v + w) −Q(v) −Q(w)) is bilinear.
We call B the bilinear form associated to Q. Note B is symmetric. The factor 1
2 is in
condition (2) because of (6.1). This is why we avoid ﬁelds where 2 = 0, although bilinearity
of B has nothing to do with a choice of nonzero scaling factor out front. Quadratic forms
in characteristic 2 are discussed in Section 7. We will often use (2) as
(6.2)
Q(v + w) = Q(v) + Q(w) + 2B(v, w).
In particular, note B(v, w) = 0 is equivalent to Q(v + w) = Q(v) + Q(w).
For the rest of this section, F does not have characteristic 2.
Deﬁnition 6.1 doesn’t require V to be ﬁnite-dimensional, but the examples and theorems
we discuss are in the ﬁnite-dimensional case. Call dim V the dimension of the quadratic
form. When we refer to a quadratic form “on F n” we think of F n as an F-vector space.
To connect the concrete and coordinate-free descriptions of quadratic forms, we show
that quadratic forms on a vector space are nothing other than homogeneous quadratic
polynomials once a basis is chosen. Starting with Q: V →F as in Deﬁnition 6.1, induction
on the number of terms in (6.2) gives
(6.3)
Q(v1 + · · · + vr) = Q(v1) + · · · + Q(vr) + 2
X
i<j
B(vi, vj)
for any r ≥2 and vectors vi ∈V . Therefore, if {e1, . . . , en} is a basis of V ,
Q(x1e1 + · · · + xnen)
=
n
X
i=1
Q(xiei) + 2
X
i<j
B(xiei, xjej)
=
n
X
i=1
aix2
i +
X
i<j
aijxixj,
(6.4)
where ai = Q(ei) and aij = 2B(ei, ej).
This exhibits Q as a homogeneous quadratic
polynomial in coordinates.

<!-- page 35 -->
BILINEAR FORMS
35
Conversely, let’s show any function V →F that is a homogeneous quadratic polynomial
in the coordinates of some basis is a quadratic form on V . Let Q(x1e1 + · · · + xnen) be a
polynomial as in (6.4). Easily Q(cv) = c2Q(v) for c ∈F. Letting v = x1e1 + · · · + xnen and
v′ = x′
1e1 + · · · + x′
nen, deﬁne
B(v, v′)
:=
1
2(Q(v + v′) −Q(v) −Q(v′))
=
n
X
i=1
aixix′
i + 1
2
X
1≤i<j≤n
aij(xix′
j + x′
ixj)
(6.5)
=
[v] · M[v′],
where
(6.6)
M =





a1
a12/2
· · ·
a1n/2
a12/2
a2
· · ·
a2n/2
...
...
...
...
a1n/2
a2n/2
· · ·
an




.
Therefore B is a bilinear form on V , so Q is a quadratic form on V .
Example 6.2. On EndF (V, V ) let Q(L) = Tr(L2). When V = F 2, Q(( x y
z t )) = x2+2yz+t2,
which is a quadratic form in 4 variables. To show Q is a quadratic form in general, for all
c ∈F we have Q(cL) = Tr((cL)2)) = Tr(c2L2) = c2Q(L) and 1
2(Q(L+L′)−Q(L)−Q(L′)) =
Tr(LL′), which is a bilinear form on EndF (V, V ) (Example 1.12).
We can express a quadratic form in terms of its associated bilinear form by setting w = v:
(6.7)
B(v, v) = 1
2(Q(2v) −2Q(v)) = 1
2(4Q(v) −2Q(v)) = Q(v),
so
(6.8)
Q(v) = B(v, v).
Conversely, every symmetric bilinear form B on V deﬁnes a quadratic form by the formula
(6.8), and the bilinear form associated to this quadratic form is B (this is “polarization”;
see Theorem 1.8). For example, Q is identically zero if and only if B is identically zero.
Outside of characteristic 2 there is a (linear) bijection between between quadratic forms
on V and symmetric bilinear forms on V . Once we choose a basis for V we get a further
(linear) bijection with n × n symmetric matrices, where n = dim V .
In matrix notation, writing B(v, w) = [v] · M[w] for a symmetric matrix M relative to a
choice of basis, (6.8) becomes Q(v) = [v] · M[v]. We call M the matrix associated to Q in
this basis. It is the same as the matrix associated to B in this basis. Concretely, when we
write Q as a polynomial (6.4), its matrix is (6.6).
Example 6.3. When Q is the sum of n squares quadratic form on F n, its matrix in the
standard basis of F n is In and Q(v) = v · v = v · Inv.
Example 6.4. The polynomial Q(x, y) = ax2 + bxy + cy2, as a quadratic form on F 2,
is represented by the matrix ( a
b/2
b/2
c ) in the standard basis: Q(x, y) =
 x
y

· ( a
b/2
b/2
c )
 x
y

.
Even though Q(x, y) =
 x
y

· ( a b
0 c )
 x
y

too, the matrix ( a b
0 c ) is not symmetric (for b ̸= 0) and
therefore is not considered a matrix for Q.

<!-- page 36 -->
36
KEITH CONRAD
When M is the matrix for Q in one basis, changing the basis changes the matrix for Q to
C⊤MC for some C ∈GLn(F). Since det(C⊤MC) = det(C)2 det(M), the number det(M)
as a function of Q is only well-deﬁned up to multiplication by a nonzero square in F.
Deﬁnition 6.5. The discriminant of the quadratic form Q is det M considered as a number
up to nonzero square factors in F, where M is any matrix for Q.
We write disc Q for the discriminant of Q, and although it is really only deﬁned up to a
nonzero square factor it is common to refer to any particular number in the square class of
disc Q as the discriminant of Q.
Example 6.6. The discriminant of the quadratic form in Example 6.4 equals ac −b2/4. In
particular, x2 −y2 has discriminant −1.
Theorem 6.7. Let Q be a quadratic form on an n-dimensional vector space over a ﬁeld of
characteristic not 2. In a suitable basis, Q is diagonalized:4
(6.9)
Q
 n
X
i=1
xiei
!
=
n
X
i=1
aix2
i ,
where ai = Q(ei). The discriminant of Q is a1a2 · · · an.
Proof. Let {e1, . . . , en} be an orthogonal basis of the symmetric bilinear form associated to
Q (Theorem 4.7). In this basis, the cross terms in (6.4) vanish and Q is diagonalized. The
matrix (6.6) for Q in this basis is diagonal, so disc Q is the product of the ai’s.
□
When (V, Q) is a quadratic space, we refer to the discriminant of Q as the discriminant
of V too, if Q is understood, and write it as disc V . For example, disc Rp,q = (−1)q where
the intended quadratic form on Rp,q is x2
1 + · · · + x2
p −x2
p+1 −· · · −x2
p+q.
Theorem 6.8. Let (V, Q) be a quadratic space. If there are orthogonal subspaces W and
U in V such that V = W ⊥U, then disc V = disc W disc U, where W and U are treated as
quadratic spaces using the restrictions of Q to W and U.
The equation disc V = disc W disc U is equality up to scaling by nonzero squares in F.
Proof. The quadratic form Q restricted to W and U can be diagonalized: there are orthog-
onal bases {w1, . . . , wr} of W and {u1, . . . , us} of U relative to which Q|W and Q|U are
diagonal quadratic forms:
Q(x1w1 + · · · + xrwr) = a1x2
1 + · · · + arx2
r,
Q(y1u1 + · · · + ysus) = b1y2
1 + · · · + bsy2
s,
where ai = Q(wi) and bj = Q(uj).
Since V = W ⊥U, {w1, . . . , wr, u1, . . . , us} is an
orthogonal basis of V , so
Q(x1w1 + · · · + xrwr + y1u1 + · · · + ysus) = a1x2
1 + · · · + arx2
r + b1y2
1 + · · · + bsy2
s.
Thus disc V = a1 · · · arb1 · · · bs = disc W disc U.
□
The construction of an orthogonal basis of a quadratic space can be carried out system-
atically from the bilinear form of the quadratic form. If Q = 0 on V then all bases of V are
orthogonal bases of (V, Q). If Q ̸= 0, pick any e1 ∈V such that Q(e1) ̸= 0. Then e1 ̸∈e⊥
1
since B(e1, e1) = Q(e1) ̸= 0, so L = Fe1 and L⊥are complementary orthogonal subspaces:
4Theorem 6.7 is special to degree 2.
In degree 3, f(x, y) = x2y is homogeneous and by an explicit
calculation no A ∈GL2(F) satisﬁes f(A
 x
y

) = ax3 + by3. Here F has any characteristic, even 2 or 3.

<!-- page 37 -->
BILINEAR FORMS
37
V = L ⊕L⊥and elements of L and L⊥are orthogonal, so V = L ⊥L⊥. If Q ̸= 0 on L⊥
then pick e2 ∈L⊥= e⊥
1 such that Q(e2) ̸= 0, so e1 and e2 are orthogonal and linearly inde-
pendent, and we can split oﬀFe2 inside L⊥with an orthogonal complementary subspace,
which has to be e⊥
1 ∩e⊥
2 . We seek an e3 in here with Q(e3) ̸= 0 when Q is not identically
0 on it, and so on. The process eventually reaches a subspace on which Q is identically 0.
If this is the subspace {0} then the vectors we have already picked are an orthogonal basis
with respect to which Q is diagonal. If this process reaches a nonzero subspace Z on which
Q is identically 0, then the vectors already picked are mutually orthogonal, and adjoining
to this list any basis for Z is an orthogonal basis of the whole space V , with respect to
which Q is diagonal.
Example 6.9. Consider Q(x, y, z) = xy + xz + yz. We want to write
Q = ax′2 + by′2 + cz′2
where x′, y′, z′ are linear in x, y, z and a, b, and c are constants. Blind algebraic calculation
is unlikely to diagonalize Q (try!), but thinking geometrically leads to a solution, as follows.
The bilinear form on F 3 for Q is
B(v, w) = 1
2 (Q(v + w) −Q(v) −Q(w)) = v ·


0
1/2
1/2
1/2
0
1/2
1/2
1/2
0

w.
Pick any vector at which Q doesn’t vanish, say e1 := (1, 0, 1). Then, using the above bilinear
form B, the space orthogonal to e1 is
e⊥
1 = {(x, y, z) : 1
2x + y + 1
2z = 0}.
One vector in here at which Q doesn’t vanish is e2 = (1, −1/2, 0). Since B(e2, (x, y, z)) =
−x/4 + y/2 + z/4, a vector v = (x, y, z) satisﬁes v ⊥e1 and v ⊥e2 when x/2 + y + z/2 = 0
and −x/4 + y/2 + z/4 = 0, so (after some algebra) (x, y, z) = (0, y, −2y). Taking y = 1
here, let e3 := (0, 1, −2). Then {e1, e2, e3} is an orthogonal basis of F 3 with respect to B
and in this basis
Q(x′e1 + y′e2 + z′e3) = Q(e1)x′2 + Q(e2)y′2 + Q(e3)z′2 = x′2 −1
2y′2 −2z′2,
so we diagonalized Q.
Corollary 6.10. Let Q be a quadratic form on V . An a ∈F × can occur as the coeﬃcient
of Q in some diagonalization if and only if a ∈Q(V ).
Proof. The coeﬃcients in a diagonalization of Q are the Q-values of an orthogonal basis, so
any nonzero coeﬃcient that occurs in a diagonalization is a Q-value.
Conversely, assume a ̸= 0 in F and a = Q(v) for some v. Then a = B(v, v), so by the
proof of Theorem 4.7 there is an orthogonal basis of V having ﬁrst vector v. The ﬁrst
coeﬃcient in the diagonalization of Q relative to this orthogonal basis is a by (6.4).
□
Example 6.11. The quadratic form 2x2 +3y2 on Q2 can’t be written in the form x′2 +by′2
by a linear change of variables on Q2: otherwise the coeﬃcient 1 is a value of 2x2 + 3y2 on
Q2, which is not true (Exercise 4.7).
Deﬁnition 6.12. For F-vector spaces V1 and V2, quadratic forms Qi on Vi are called
equivalent if there is a linear isomorphism A: V1 →V2 such that Q2(Av) = Q1(v) for all
v ∈V1.

<!-- page 38 -->
38
KEITH CONRAD
Example 6.13. The quadratic forms x2 −y2 and xy on F 2 are equivalent since x2 −y2 =
(x+y)(x−y) is a product (call it x′y′ if you wish), and the passage from (x, y) to (x+y, x−y)
is linear and invertible outside characteristic 2. This is just Example 2.10 in disguise.
Theorem 6.14. Quadratic forms are equivalent if and only if their associated bilinear forms
are equivalent in the sense of Deﬁnition 2.9.
Proof. Let Q1 and Q2 have associated bilinear forms B1 and B2. If Q2(Av) = Q1(v) for all
v ∈V then B2(Av, Av) = B1(v, v). Therefore B2(Av, Aw) = B1(v, w) for all v and w in V
(Theorem 1.8), so B1 and B2 are equivalent. The converse direction is trivial.
□
Deﬁnition 6.15. A quadratic form is called nondegenerate if a (symmetric) matrix repre-
sentation for it is invertible, i.e., its discriminant is nonzero. If the discirminant is 0, we
call the quadratic form degenerate.
Example 6.16. The quadratic form ax2 + bxy + cy2 on F 2 has discriminant ac −b2/4 =
−(1/4)(b2 −4ac), so this quadratic form is nondegenerate if and only if b2 −4ac ̸= 0.
Example 6.17. On R2, the quadratic form Q(x, y) = x2 −y2 is nondegenerate. On R3,
the quadratic form Q(x, y, z) = x2 −y2 is degenerate.
Table 2 collects diﬀerent descriptions of the same ideas for symmetric bilinear forms and
for quadratic forms.
Condition
Symm. Bil. Form
Quadratic Form
Matrix Rep.
B(v, w) = [v] · M[w]
Q(v) = [v] · M[v]
v ⊥w
B(v, w) = 0
Q(v + w) = Q(v) + Q(w)
Orthog. basis
B(ei, ej) = 0 (i ̸= j)
Q(P
i xiei) is diagonal
Equivalence
B2(Av, Aw) = B1(v, w)
Q2(Av) = Q1(v)
Nondegeneracy
det M ̸= 0
det M ̸= 0
Table 2. Comparisons
The next result puts some of this terminology to work.
Theorem 6.18. Let Q be a quadratic form on a two-dimensional space. The following
conditions on Q are equivalent:
(1) Q looks like x2 −y2 in a suitable basis,
(2) disc Q = −1 modulo nonzero squares,
(3) Q is nondegenerate and takes on the value 0 nontrivially.
Taking on the value 0 nontrivially means Q(v) = 0 for some v that is nonzero.
Proof. The ﬁrst property easily implies the second and third properties (since x2 −y2
vanishes at (x, y) = (1, 1)). We now show that the second property implies there is a basis
in which Q is x2 −y2 and that the third property implies the second property.
Assume disc Q = −1. Choosing an orthogonal basis {e1, e2} we have Q(x1e1 + x2e2) =
ax2
1 + bx2
2. Since ab = −1 mod (F ×)2, in a suitable basis Q looks like
ax2 −1
ay2 = a

x2 −y2
a2

= a

x + y
a
 
x −y
a

= (ax + y)

x −1
ay

.

<!-- page 39 -->
BILINEAR FORMS
39
Set x′ = ax+y and y′ = x−y/a, so in these coordinates (that is, in the basis e′
1 := ae1 +e2
and e′
2 := e1 −(1/a)e2) Q looks like x′y′, which can be written as a diﬀerence of squares by
a further linear change of variables (Example 2.10).
Assume now that Q is nondegenerate and takes the value 0 nontrivially. Pick an orthog-
onal basis {e1, e2} for Q, so Q(x1e1 + x2e2) = ax2
1 + bx2
2 where a and b are nonzero by
nondegeneracy of Q. For some x0 and y0 that are not both nonzero we have ax2
0 + by2
0 = 0,
so necessarily x0 and y0 are both nonzero. Writing b = −ax2
0/y2
0, we have
Q(x1e1 + x2e2) = ax2
1 −a
x2
0
y2
0

x2
2.
Thus disc(Q) = a(−a)(x2
0/y2
0) = −(ax0/y0)2, so disc(Q) = −1 up to a square factor.
□
We turn now to the classiﬁcation of nondegenerate quadratic forms up to equivalence over
certain ﬁelds: the real numbers, the complex numbers, and ﬁnite ﬁelds of odd characteristic.
Theorem 6.19. Every nondegenerate quadratic form on an n-dimensional complex vector
space is equivalent to x2
1 + · · · + x2
n on Cn. Every nondegenerate quadratic form on an
n-dimensional real vector space is equivalent to x2
1 + · · · + x2
p −x2
p+1 −· · · −x2
n on Rn for a
unique p between 0 and n.
Proof. In an orthogonal basis, an n-dimensional nondegenerate quadratic form is a sum of n
nonzero monomials aix2
i . Since ac2Q(v) = aQ(cv), a nonzero square factor c2 in a diagonal
coeﬃcient of Q can be removed by replacing the corresponding basis vector v with cv in
the basis. Over C every nonzero number is a square, so the coeﬃcients can be scaled to 1.
Thus any nondegenerate quadratic form over C looks like Pn
i=1 x2
i in a suitable basis. Over
R the positive coeﬃcients can be scaled to 1 and the negative coeﬃcients can be scaled to
−1.
We now show the quadratic forms x2
1 + · · · + x2
p −x2
p+1 −· · · −x2
n and y2
1 + · · · + y2
p′ −
y2
p′+1 −· · · −y2
n on Rn are equivalent only when p = p′. Equivalence means there is a single
quadratic form Q on Rn that looks like each polynomial in a suitable basis. Let Q look like
the ﬁrst polynomial in the basis {e1, . . . , en} and let it look like the second polynomial in
the basis {f1, . . . , fn}.
Let W be the span of e1, . . . , ep and let W ′ be the span of fp′+1, . . . , fn. For w ∈W,
Q(w) ≥0 with equality if and only if w = 0. For w′ ∈W ′, Q(w′) ≤0 with equality if and
only if w′ = 0. Therefore W ∩W ′ = {0}, so dim(W +W ′) = dim W +dim W ′ = p+(n−p′).
Since W + W ′ ⊂Rn, dim(W + W ′) ≤n, so p + n −p′ ≤n. Thus p ≤p′. By switching the
roles of the two bases we get the reverse inequality, so p = p′.
□
Corollary 6.20. When p + q = p′ + q′, ⟨·, ·⟩p,q and ⟨·, ·⟩p′,q′ are equivalent if and only if
p = p′ and q = q′.
Proof. By Theorem 6.14, ⟨·, ·⟩p,q and ⟨·, ·⟩p′,q′ are equivalent if and only if the corresponding
quadratic forms are equivalent, which means p = p′ (so also q = q′) by Theorem 6.19.
□
A nondegenerate quadratic form on Rn is determined up to equivalence by the pair (p, q)
coming from a diagonalization, where p is the number of plus signs and q = n −p is the
number of minus signs. This ordered pair (p, q) is called the signature of the quadratic
form.5 Once we know the dimension n, either p or q determines the other since p + q = n
(we have in mind only the nondegenerate case).
5Some authors refer to p alone as the signature.

<!-- page 40 -->
40
KEITH CONRAD
Deﬁnition 6.21. A quadratic form Q on a real vector space is called positive deﬁnite if
Q(v) > 0 for all v ̸= 0 and negative deﬁnite if Q(v) < 0 for all v ̸= 0.6
All positive-deﬁnite real quadratic forms with a common dimension n are equivalent to
a sum of n squares and thus are equivalent to each other. Similarly, all negative-deﬁnite
quadratic forms with a common dimension are equivalent to each other. Unlike the property
of being a sum of squares, positive deﬁniteness doesn’t depend on the choice of coordinates.
Example 6.22. We will put to use the normalization of a positive-deﬁnite quadratic form
as a sum of squares to compute the multivariable analogue of a Gaussian integral.
In one dimension,
R
R e−x2/2 dx =
√
2π, or equivalently
R
R e−πx2 dx = 1. We now consider
R
Rn e−πQ(v) dv where Q: Rn →R is a positive-deﬁnite quadratic form. Write Q(v) = v·Mv
in standard coordinates on Rn. Since Q is positive deﬁnite, it is a sum of n squares in some
basis, so for some A ∈GLn(R) we have Q(Av) = v · v. Thus A⊤MA = In. By a linear
change of variables in the integral,
Z
Rn e−πQ(v) dv =
Z
Rn e−πQ(Av) d(Av) = | det A|
Z
Rn e−πv·v dv.
The last integral breaks up into the product of n 1-dimensional integrals
R
R e−πxi2 dxi,
which are each 1, so
Z
Rn e−πQ(v) dv = | det A|.
Since A⊤MA = In, taking determinants gives (det A)2 det M = 1, so | det A| = 1/
√
det M.
Therefore
R
Rn e−πQ(v) dv = 1/
√
det M. where Q(v) = v · Mv.
Now we will classify nondegenerate quadratic forms over a ﬁnite ﬁeld of odd characteristic.
The essential property is that a quadratic form with high enough dimension always takes
on the value 0 nontrivially:
Theorem 6.23. Let F be a ﬁnite ﬁeld with odd characteristic and Q be a nondegenerate
quadratic form over F. If Q has dimension at least 3 then there is a solution to Q(v) = 0
with v ̸= 0.
Proof. First we handle the case of dimension 3. In an orthogonal basis, write
Q(xe1 + ye2 + ze3) = ax2 + by2 + cz2,
where a, b, and c are all nonzero. We will ﬁnd a solution to Q(v) = 0 with z = 1: the
equation ax2 + by2 + c = 0 has a solution in F.
Let q = |F|. The number of squares in F is (q + 1)/2. (There are (q −1)/2 nonzero
squares since the squaring map F× →F× is 2-to-1; thus its image has size (q −1)/2; add
1 to this count to include 02.) The two sets {ax2 : x ∈F} and {−by2 −c : y ∈F} are in
bijection with the set of squares, so each has size (q + 1)/2. Since F has q terms, the two
sets must overlap. At an overlap we have ax2 = −by2 −c, so ax2 + by2 + c = 0.
If Q has dimension greater than 3, write it in an orthogonal basis as
Q(x1e1 + x2e2 + · · · + xnen) = a1x2
1 + a2x2
2 + · · · + anx2
n,
where the ai’s are all nonzero. Set xi = 0 for i > 3 and x3 = 1. Then we are looking at
a1x2
1 + a2x2
2 + a3, which assumes the value 0 by the previous argument.
□
6A nondegenerate real quadratic form that is neither positive deﬁnite nor negative deﬁnite is called
indeﬁnite, such as x2 −y2.

<!-- page 41 -->
BILINEAR FORMS
41
The bound dim V ≥3 in Theorem 6.23 is sharp: the 2-dimensional quadratic form
x2 −cy2, where c is a nonsquare in F×, doesn’t take the value 0 except when x = y = 0.
The reason that taking on the value 0 nontrivially (that is, at a nonzero vector) matters
is the following result over any ﬁeld not of characteristic 2.
Theorem 6.24. If Q: V →F is a nondegenerate quadratic form that takes on the value 0
nontrivially then it takes on all values: Q(V ) = F.
Proof. Let B be the bilinear form for Q and let Q(v) = 0 with v ̸= 0. Since Q(cv) =
c2Q(v) = 0 and Q is not identically zero (otherwise it couldn’t be nondegenerate), dim V ≥
2. By nondegeneracy of Q (equivalently, of B), there is a w ∈V such that B(v, w) ̸= 0.
Then for any c ∈F,
Q(cv + w) = Q(cv) + Q(w) + 2B(cv, w) = Q(w) + 2B(v, w)c.
Since 2B(v, w) ̸= 0, this is a linear function of c and therefore takes on all values in F as c
varies.
□
Theorem 6.24 can be false for degenerate Q, e.g., Q(x, y) = x2 on R2, where Q(0, 1) = 0.
Deﬁnition 6.25. A quadratic form Q: V →F is universal if Q(V ) = F.
Example 6.26. On R3, x2 + y2 + z2 is not universal but x2 + y2 −z2 is.
Corollary 6.27. Every nondegenerate quadratic form of dimension ≥2 over a ﬁnite ﬁeld
F of characteristic not 2 is universal.
Proof. When the dimension is at least 3, Theorems 6.23 and 6.24 tell us the quadratic form
is universal. In two dimensions, after diagonalizing we want to know a polynomial of the
form ax2 + by2, for a and b in F×, takes on all values in F. This was explained in the
proof of Theorem 6.23, where we showed ax2 + by2 + c = 0 has a solution x, y ∈F for any
c ∈F×.
□
Theorem 6.28. Fix a nonsquare d ∈F×. For n ≥1, any nondegenerate quadratic form
on an n-dimensional vector space over F is equivalent to exactly one of
x2
1 + x2
2 + · · · + x2
n−1 + x2
n or x2
1 + x2
2 + · · · + x2
n−1 + dx2
n
on Fn. In particular, the dimension and discriminant determine a nondegenerate quadratic
form over F up to equivalence.
Proof. The two forms provided are inequivalent, since the ﬁrst has discriminant 1 and the
second has discriminant d, which are unequal in F×/(F×)2.
To see any n-dimensional nondegenerate quadratic form over F is equivalent to one of
these, we argue by induction on n. Any nondegenerate one-dimensional quadratic form in
coordinates is Q(x) = ax2, where (insofar as the equivalence class of Q is concerned) a only
matters up to a nonzero square factor. This gives us the two choices x2 and dx2.
When n ≥2, Corollary 6.27 tells us that Q takes on the value 1. By Corollary 6.10, there
is an orthogonal basis {e1, . . . , en} such that Q(e1) = 1:
Q(x1e1 + x2e2 + · · · + xnen) = x2
1 + a2x2
2 + · · · + anx2
n,
where ai ∈F×.
The quadratic form Q(x2e2 + · · · + xnen) = Q|e⊥
1 is nondegenerate of
dimension n −1, so by induction we can write it after a linear change of variables (not
involving x1) as y2
2 + · · · + y2
n−1 + ay2
n, where a = 1 or a = d. Add x2
1 to this and we’re
done.
□

<!-- page 42 -->
42
KEITH CONRAD
To give a sense of other techniques, we will redo the classiﬁcation of nondegenerate
quadratic forms over F by a second method, which gives a more “geometric” description of
the quadratic forms. First we introduce some terminology.
Deﬁnition 6.29. A quadratic space is a vector space along with a choice of quadratic form
on it. We call it nondegenerate when the underlying quadratic form is nondegenerate.
This is the analogue for quadratic forms of the notion of a bilinear space for bilinear
forms. Outside of characteristic 2 (which is the case throughout this section), quadratic
spaces are essentially the same thing as symmetric bilinear spaces. In Section 7 we will see
that this is no longer true in characteristic 2!
Deﬁnition 6.30. Two quadratic spaces (V1, Q1) and (V2, Q2) are called isomorphic if there
is a linear isomorphism A: V1 →V2 such that Q2(Av) = Q1(v) for all v ∈V1.
Deﬁnition 6.31. Let (V1, Q1) and (V2, Q2) be quadratic spaces over a common ﬁeld F.
Their orthogonal direct sum V1 ⊥V2 is the vector space V1 ⊕V2 with the quadratic form
Q(v1, v2) = Q1(v1) + Q2(v2).
We write V ⊥n for the n-fold orthogonal direct sum of a
quadratic space V with itself.
Example 6.32. If we view F as a 1-dimensional quadratic space with quadratic form
Q(x) = x2, the quadratic space F ⊥n is the vector space F n equipped with the standard
sum of n squares quadratic form.
Deﬁnition 6.33. Let Q: V →F be a quadratic form. A null vector for Q (or for V ) is
any nonzero v ∈V such that Q(v) = 0.
In terms of the associated bilinear form B, a null vector is a nonzero solution to B(v, v) =
0.
Null vectors are self-orthogonal nonzero vectors.
(Other names for null vectors are
isotropic vectors and singular vectors, the former being very widely used.) The spaces Rp,q
for positive p and q have plenty of null vectors. Theorem 6.23 says all nondegenerate qua-
dratic forms in dimension at least 3 over a ﬁnite ﬁeld (with characteristic not 2) have a null
vector, while Theorem 6.24 says any nondegenerate quadratic form outside of characteristic
2 with a null vector is universal.
Here is the key concept for our second approach to the classiﬁcation over ﬁnite ﬁelds.
Deﬁnition 6.34. A hyperbolic plane is a two-dimensional quadratic space where the qua-
dratic form looks like x2 −y2 in some basis.
We could just as well have used xy as the model quadratic form since x2 −y2 and xy
are equivalent (we are not in characteristic 2). A hyperbolic plane is denoted H, or H(F)
if the ﬁeld F is to be speciﬁed.
Example 6.35. The quadratic space R2,1, where the quadratic form is x2 + y2 −z2 =
x2 −z2 + y2, is isomorphic to H ⊥R since x2 −z2 gives us a hyperbolic plane and y2 is the
standard quadratic form on R = R1,0. More generally, in Rp,q if we collect an equal number
of x2
i and −x2
j together then what remains is a sum of squares (if p > q) or a negative sum
of squares (if q > p). So Rp,q = H⊥m ⊥W where m = min(p, q) and W is a quadratic
space of dimension |p −q| that is positive deﬁnite if p > q, negative deﬁnite if q > p, or {0}
if p = q.
Theorem 6.18 tells us that a hyperbolic plane is the same thing as a 2-dimensional nonde-
generate quadratic space with a null vector. The importance of the hyperbolic plane is in the

<!-- page 43 -->
BILINEAR FORMS
43
next result, which says that hyperbolic planes always explain null vectors in nondegenerate
quadratic spaces.
Theorem 6.36. Let (V, Q) be a nondegenerate quadratic space. If Q has a null vector then
V ∼= H ⊥W and W is nondegenerate.
Proof. Let Q(v) = 0 with v ̸= 0.
We will ﬁnd a second null vector for Q that is not
orthogonal to v.
Since (V, Q) is nondegenerate and v is nonzero, v⊥̸= V . Pick any u at all outside of v⊥,
so B(u, v) ̸= 0. We will ﬁnd a null vector of the form u + cv for some c ∈F. Then, since
B(u + cv, v) = B(u, v) + cB(v, v) = B(u, v), u + cv is not orthogonal to v.
For all c ∈F,
Q(u + cv) = Q(u) + Q(cv) + 2B(u, cv) = Q(u) + 2cB(u, v).
Let c = −Q(u)/2B(u, v), so Q(u + cv) = 0. Now rename u + cv as u, so u is a null vector
for Q and B(u, v) ̸= 0. Since v ⊥v and u ̸⊥v, u and v are linearly independent.
In Fu + Fv, Q(xu + yv) = 2xyB(u, v), which equals xy after scaling u so that B(u, v) =
1/2. (Since B(u, v) ̸= 0, B(au, v) = aB(u, v) becomes 1/2 for some a ∈F.) Now Fu + Fv
as a quadratic space is a hyperbolic plane, since xy and x2 −y2 are equivalent. Since a
hyperbolic plane is nondegenerate, V = (Fu+Fv) ⊥W where W = (Fu+Fv)⊥(Theorem
3.12).
□
Theorem 6.36 says that after a linear change of variables (that is, using a suitable basis),
a nondegenerate quadratic form with a null vector has the expression
Q(x1, x2, . . . , xn) = x2
1 −x2
2 + Q′(x3, . . . , xn).
The merit of Theorem 6.36 is that it conveys this algebraic fact in a more geometric way.
Let’s take another look at quadratic forms over a ﬁnite ﬁeld F (with odd characteristic).
If (V, Q) is a nondegenerate quadratic space over F with n := dim V ≥3, there is a null
vector in V (Theorem 6.23), so V ∼= H ⊥W and dim W = n −2. If dim W ≥3, there is a
null vector in W and we can split oﬀanother hyperbolic plane: V ∼= H⊥2 ⊥W ′. This can be
repeated until we reach a subspace of dimension ≤2, so V ∼= H⊥m ⊥U for m = [(n −1)/2]
and U is nondegenerate with dim U = 1 or 2. The analysis of U will duplicate our previous
work in low dimensions. If dim U = 1 then the underlying quadratic form on it is x2 or cx2
where c is a (ﬁxed) nonsquare in F×. If dim U = 2 then Q|U is universal (Corollary 6.27)
so we can write it as x2 −ay2 for some a ̸= 0. Here a only matters modulo squares, so we
can replace it with either 1 (if a is a square) or c (if a is not a square). The ﬁrst case gives
us a hyperbolic plane and the second doesn’t (no null vector). There are two choices for U
in both dimensions 1 and 2, which can be distinguished by their discriminants.
Since disc V = disc(H)m disc(U) = (−1)[(n−1)/2] disc U, we have once again shown that
there are 2 nondegenerate quadratic forms of each dimension over F, and they can be
distinguished from each other by their discriminant (modulo nonzero squares, as always).
Moreover, this second approach gives another way to express the two choices of quadratic
forms in each dimension. Choosing coordinates in a hyperbolic plane so the quadratic form
is xy rather than x2−y2, a nondegenerate n-dimensional quadratic form over F is equivalent
to
(6.10)
x1x2 + x3x4 + · · · + xn−3xn−2 +
(
xn−1xn, or
x2
n−1 −cx2
n,

<!-- page 44 -->
44
KEITH CONRAD
if n is even and
(6.11)
x1x2 + x3x4 + · · · + xn−4xn−3 + xn−2xn−1 +
(
x2
n, or
cx2
n,
if n is odd.
While this second classiﬁcation of quadratic forms over F appears more complicated than
Theorem 6.28, it more closely resembles the classiﬁcation of nondegenerate quadratic forms
over ﬁnite ﬁelds with characteristic 2 (Theorem 7.20 below).
We conclude this section with some odds and ends: a number of conditions equivalent
to nondegeneracy for a quadratic form and a theorem of Jordan and von Neumann on the
axioms for quadratic forms.
Theorem 6.37. Let Q be a quadratic form on V . The following conditions are equivalent:
(1) Q is nondegenerate, i.e., disc Q ̸= 0,
(2) there is no basis of V in which Q can be written as a polynomial in fewer than n
variables, where n = dim V ,
(3) using any basis of V to express Q as a polynomial function, the only common solution
in V to (∂Q/∂xi)(v) = 0 for all i is v = 0.
Proof. When dim V = 1, all three conditions are equivalent to Q not being identically 0, so
from now on we take dim V > 1. To show (1) and (2) are equivalent, assume (2): Q can’t
be written as a polynomial in fewer than n variables. Then relative to an orthogonal basis
{e1, . . . , en} the diagonal coeﬃcients Q(ei) are all nonzero, so (1) holds.
Now assume Q can be written in fewer than n variables. That is, we can decompose V as
a direct sum V1 ⊕V2 of two nonzero subspaces such that Q(v) = Q(v1) for all v ∈V , where
v1 is the projection of v onto its V1-component. We will show V ⊥̸= {0}, so Q is degenerate.
Note Q(V2) = {0}. Pick a nonzero w ∈V2. For any v ∈V1, Q(v + w) = Q(v). Therefore
Q(w) + 2B(v, w) = 0. Since Q(w) = 0, we have w ⊥v (because 2 ̸= 0). Therefore w ⊥V1.
For a second vector w′ ∈V2, Q(w + w′) = 0 and Q(w) = Q(w′) = 0, so 2B(w, w′) = 0. This
tells us w ⊥V2. Thus w ⊥V , so V ⊥̸= {0}. (In particular, we found a nonzero element of
V ⊥at which Q vanishes.)
We now show (1) and (3) are equivalent. Choose a basis and write Q as the polynomial
in (6.4). Then
∂Q
∂xk
=
X
i<k
aikxi + 2akxk +
X
k<j
akjxj,
so all the partial derivatives vanish at a point (c1, . . . , cn) if and only if
(6.12)





2a1
a12
· · ·
a1n
a12
2a2
· · ·
a2n
...
...
...
...
a1n
a2n
· · ·
2an










c1
c2
...
cn




=





0
0
...
0




.
The matrix here is twice the matrix for Q in (6.6). The partial derivatives of Q all vanish
simultaneously only at 0 in F n precisely when the matrix in (6.12) is invertible, which is
equivalent to the matrix in (6.6) being invertible (since 2 ̸= 0 in F), which is the deﬁnition
of Q being nondegenerate.
□
Remark 6.38. If we replace Q with a homogeneous polynomial of degree greater than 2,
the 2nd and 3rd properties of Theorem 6.37 are no longer the same [13, pp. 364, 376, 377].

<!-- page 45 -->
BILINEAR FORMS
45
Since Q is a homogeneous polynomial (once a basis is chosen), its zero set is naturally
a projective hypersurface. In terms of this hypersurface, the algebraic condition of nonde-
generacy for quadratic forms outside of characteristic 2 acquires a geometric interpretation
in dimension at least 3:
Corollary 6.39. Let V be an n-dimensional vector space over a ﬁeld F not of characteristic
2 and let Q be a nonzero quadratic form on V . Pick a basis to view Q as a homogeneous
polynomial function of n variables. If n ≥3 then Q is nondegenerate on V if and only if
the projective hypersurface Q = 0 in Pn−1(F) is irreducible and smooth. If n = 2 then the
solution set to Q = 0 in P1(F) contains 2 points if Q is nondegenerate and 1 point if Q is
degenerate.
Proof. Suppose n ≥3. If Q as a polynomial is reducible over F then Q = L1L2 where the
Li’s are linear forms (homogeneous of degree 1) over F. We will show from this factorization
that Q is degenerate on V , so any nondegenerate quadratic form on V is irreducible as a
polynomial over F when n ≥3.
The zero sets of L1 and L2 in F
n have a common nonzero point: this is obvious if L1 and
L2 are scalar multiples of each other, and if they are not scalar multiples then their zero
sets are hyperplanes in F
n whose intersection has codimension n −2 > 0. In either case,
let P be a common zero of L1 and L2 in F
n −{0}. Then
∂Q
∂xi

P
= L1(P) ∂L2
∂xi

P
+ L2(P) ∂L1
∂xi

P
= 0
for all i. Applying Theorem 6.37 to the polynomial Q as a quadratic form on F
n, we see
that disc Q = 0. Therefore Q is degenerate on V too. (Concretely, if there is a nonzero
vector in F
n at which all the partials of Q vanish then there is such a point in F n because
a matrix with entries in F that is not invertible over a larger ﬁeld is also not invertible over
F itself.)
If Q is nondegenerate on V it is an irreducible polynomial over F, so the hypersurface
Q = 0 in Pn−1(F) is deﬁned by a single irreducible polynomial over F. This hypersurface
is smooth since the partials ∂Q/∂xk do not all vanish at a common nonzero point in F
n.
Conversely, if this hypersurface is irreducible and smooth then the partials ∂Q/∂xk do not
all vanish at a common nonzero point in F
n, so Q is nondegenerate over F and and thus
over F (i.e., on V ).
When n = 2, write Q as ax2 + by2 in an orthogonal basis. This vanishes at two points
on P1(F) when a ̸= 0 and b ̸= 0, which is equivalent to Q being nondegenerate on V .
□
We have not yet mentioned an identity for quadratic forms called the parallelogram law:
(6.13)
Q(v + w) + Q(v −w) = 2(Q(v) + Q(w)).
To obtain this, replace w with −w in the equation Q(v + w) = Q(v) + Q(w) + 2B(v, w) to
get Q(v −w) = Q(v) + Q(w) −2B(v, w), and then add. The B-terms cancel. (When Q is
x2 + y2 in the plane, (6.13) says the sum of the squares of the diagonals of a parallelogram
is twice the sum of the squares of adjacent sides.) If instead we subtract, then we get
(6.14)
Q(v + w) −Q(v −w) = 4B(v, w).
Since (6.14) describes B in terms of Q-values (in a diﬀerent way than in (6.2)), could we
use (6.13) and (6.14) as an alternate set of conditions for deﬁning a quadratic form? This

<!-- page 46 -->
46
KEITH CONRAD
was examined by von Neumann and Jordan.7 They did not show Q is a quadratic form and
B is its bilinear form, but they came close:
Theorem 6.40. Let a function Q: V →F satisfy (6.13). Deﬁne B by (6.14). Then B is
symmetric, biadditive, and B(v, v) = Q(v).
Proof. We start by extracting a few properties from special cases of (6.13) and (6.14).
Setting w = v = 0 in (6.13) implies 2Q(0) = 4Q(0), so Q(0) = 0. Setting w = v in (6.13)
implies Q(2v) = 4Q(v). Setting w = −v in (6.13) implies Q(2v) = 2(Q(v) + Q(−v)), so
4Q(v) = 2Q(v)+2Q(−v). Therefore Q(−v) = Q(v). Now set w = 0 in (6.14): 0 = 4B(v, 0),
so B(v, 0) = 0. Set w = v in (6.14): Q(2v) = 4B(v, v), so B(v, v) = Q(v). Therefore
B(v, w) = 1
4(Q(v + w) −Q(v −w))
= 1
4(Q(v + w) + Q(v + w) −2(Q(v) + Q(w)))
by (6.13)
= 1
2(Q(v + w) −Q(v) −Q(w)),
which is symmetric in v and w (and is the kind of formula we expected to hold anyway).
It remains to show B is biadditive. Since B is symmetric, we will just show additivity in
the second component. From (6.14),
4(B(v, w1) + B(v, w2)) = Q(v + w1) −Q(v −w1) + Q(v + w2) −Q(v −w2)
= Q(v + w1) + Q(v + w2) −Q(v −w1) −Q(v −w2)
= 1
2(Q(2v + w1 + w2) + Q(w1 −w2))
−1
2(Q(2v −w1 −w2) + Q(w2 −w1)) by (6.13)
= 1
2(Q(2v + w1 + w2) −Q(2v −w1 −w2))
= 2B(2v, w1 + w2) by (6.14).
Dividing by 4,
(6.15)
B(v, w1) + B(v, w2) = 1
2B(2v, w1 + w2),
which is nearly what we want. Setting w2 = 0 in (6.15) and multiplying by 2, 2B(v, w1) =
B(2v, w1). Since w1 is arbitrary, we get 2B(v, w1 + w2) = B(2v, w1 + w2). Therefore the
right side of (6.15) is B(v, w1 + w2), so B is additive in its second component.
□
Bi-additivity implies Z-bilinearity. Therefore B in Theorem 6.40 is Q-bilinear if F has
characteristic 0 and Fp-bilinear if F has characteristic p, which means Q is a quadratic
form when F = Q or Fp. If F = R then Q in Theorem 6.40 is a quadratic form over R
if V is ﬁnite-dimensional and we add the extra assumption that Q is continuous (so B is
continuous and therefore is R-bilinear).
Exercises.
7This is the physicist P. Jordan who introduced Jordan algebras, rather than the mathematician C.
Jordan, as in Jordan canonical form.

<!-- page 47 -->
BILINEAR FORMS
47
1. Diagonalize x2+y2−z2+3xy−xz+6yz over Q. What is its signature as a quadratic
form over R?
2. When F has characteristic not 2, diagonalize Q(L) = Tr(L2) on M2(F) using the
orthogonal basis in Exercise 4.2.
3. When F has characteristic not 2, show det: M2(F) →F is a quadratic form. Find
its associated bilinear form and a diagonalization.
4. Show the quadratic forms x2+y2 and 3x2+3y2 over Q are inequivalent even though
they have the same discriminant (modulo squares).
5. Let K/F be a quadratic ﬁeld extension not in characteristic 2. Viewing K as an
F-vector space, show the norm map NK/F : K →F is a nondegenerate quadratic
form over F without null vectors.
6. Let K = Q(θ), where θ is the root of an irreducible cubic f(X) = X3 + aX + b
in Q[X]. Let Q: K →Q by Q(α) = TrK/Q(α2). Viewing K as a Q-vector space,
show Q is a quadratic form over Q which is determined up to equivalence by the
number 4a3 + 27b2. (Hint: Diagonalize Q.)
7. Let B be a bilinear form on V . (It need not be symmetric.) Show the function
Q(v) = B(v, v) is a quadratic form on V . What is its associated symmetric bilinear
form, in terms of B? How does this look in the language of matrices?
8. Let Q be a quadratic form on a real vector space V . If v and w in V satisfy Q(v) > 0
and Q(w) < 0, then show v and w are linearly independent and the plane spanned
by v and w has a null vector for Q. Must this plane have a basis of null vectors?
9. In Rp,q, let {e1, . . . , en} be an orthogonal basis. Show the number of ei’s such that
⟨ei, ei⟩p,q > 0 is p and the number such that ⟨ei, ei⟩p,q < 0 is q.
10. Let V be a nondegenerate real quadratic space of signature (p, q). Show p is geo-
metrically characterized as the maximal dimension of a positive-deﬁnite subspace of
V and q is the maximal dimension of a negative-deﬁnite subspace of V . If W is a
p-dimensional positive-deﬁnite subspace of V , show W ⊥is the unique q-dimensional
negative-deﬁnite subspace U such that U ⊥W.
11. Show that a nondegenerate quadratic form over an ordered ﬁeld has a well-deﬁned
signature relative to that ordering: after diagonalization, the number p of positive
coeﬃcients and q of negative coeﬃcients in the ordering is independent of the di-
agonalization. Therefore we can talk about the signature (p, q) of a nondegenerate
quadratic form over an ordered ﬁeld. (Hint: First show that in the 2-dimensional
case the diagonal coeﬃcients have opposite sign precisely when the quadratic form
takes both positive and negative values in the ordering.)
12. In the text we classiﬁed nondegenerate quadratic spaces over C, R, and ﬁnite ﬁelds
with odd characteristic. What about the degenerate case? Show a quadratic form
on V induces a quadratic form on V/V ⊥that is nondegenerate and then show a
quadratic space (V, Q) is determined up to isomorphism by the dimension of V ⊥
and the isomorphism class of the nondegenerate quadratic space V/V ⊥.
13. Let V be a real quadratic space that is possibly degenerate, and set d = dim V ⊥.
Let V/V ⊥, which is nondegenerate by the previous exercise, have signature (p, q).
Thus dim V = p + q + d.
(1) Show the maximal dimension of a positive-deﬁnite subspace of V is p and the
maximal dimension of a negative-deﬁnite subspace of V is q.
(2) If W is any p-dimensional positive-deﬁnite subspace of V show dim W ⊥= q+d
and W ⊥contains a q-dimensional negative-deﬁnite subspace.

<!-- page 48 -->
48
KEITH CONRAD
(3) On V = R3 let Q(x, y, z) = x2−y2. Check p = q = d = 1. Let W = R(1, 0, 0), a
p-dimensional positive-deﬁnite subspace of V . Find two diﬀerent q-dimensional
negative-deﬁnite subspaces of W ⊥.
7. Quadratic forms in characteristic 2
Fields of characteristic 2 have remained the pariahs of the theory.
W. Scharlau [12, p. 231]
The concrete deﬁnition of a quadratic form in characteristic 2 is just like that in other
characteristics: a function on a vector space that looks like a quadratic homogeneous poly-
nomial in some (equivalently, any) basis.
To give a coordinate-free deﬁnition, we copy
Deﬁnition 6.1 but leave out the 1
2.
Deﬁnition 7.1. A quadratic form on a vector space V over a ﬁeld F with characteristic 2
is a function Q: V →F such that
(1) Q(cv) = c2Q(v) for v ∈V and c ∈F,
(2) the function B(v, w) := Q(v + w) −Q(v) −Q(w) is bilinear.
We will often use condition (2) as
(7.1)
Q(v + w) = Q(v) + Q(w) + B(v, w).
The function B is called the bilinear form associated to Q. Formally, this B is double
the B from characteristic not 2. As in the case of characteristic not 2, we call dim V the
dimension of the quadratic form and whenever we refer to a quadratic form “on F n” we
view F n as an F-vector space.
From now on, V is ﬁnite-dimensional.
To see that Deﬁnition 7.1 turns a quadratic form into a quadratic homogeneous poly-
nomial in a basis, we argue in a similar manner to the case of characteristic not 2, except
certain factors of 2 will be missing.
Let Q: V →F satisfy Deﬁnition 7.1. Inducting on the number of terms in (7.1),
(7.2)
Q(v1 + · · · + vr) = Q(v1) + · · · + Q(vr) +
X
i<j
B(vi, vj)
for any r ≥2 and vectors vi ∈V . (It’s also true when r = 1 by taking the empty sum to
be 0.) Letting {e1, . . . , en} be a basis of V , we obtain from (7.2)
(7.3)
Q(x1e1 + · · · + xnen) =
n
X
i=1
aix2
i +
X
i<j
aijxixj,
where ai = Q(ei) and aij = B(ei, ej). Conversely, let Q: V →F be a function deﬁned by
(7.3) in a basis. For v = x1e1 + · · · + xnen we can write Q(v) = [v] · N[v], where N is the
upper-triangular (not symmetric!) matrix
(7.4)
N =





a1
a12
· · ·
a1n
0
a2
· · ·
a2n
...
...
...
...
0
0
· · ·
an




.

<!-- page 49 -->
BILINEAR FORMS
49
Clearly Q(cv) = c2Q(v). Letting v′ = x′
1e1 + · · · + x′
nen, deﬁne
B(v, v′)
:=
Q(v + v′) −Q(v) −Q(v′)
=
[v + v′] · N[v + v′] −[v] · N[v] −[v′] · N[v′]
=
[v] · (N + N⊤)[v′].
(7.5)
This is a symmetric bilinear form on V , so Q is a quadratic form on V . The matrix for B
is
(7.6)
N + N⊤=





0
a12
· · ·
a1n
a12
0
· · ·
a2n
...
...
...
...
a1n
a2n
· · ·
0




.
Formally, this is the matrix obtained by multiplying (6.6) by 2.
We could have used Deﬁnition 7.1 to deﬁne quadratic forms in all characteristics. This
is the approach taken in [2], [3], [8], and [9].
For instance, outside of characteristic 2
the connection between quadratic forms and symmetric bilinear forms becomes B(v, v) =
2Q(v) instead of B(v, v) = Q(v). While some redundancy from a separate treatment of
characteristic 2 would be avoided by using Deﬁnition 7.1 to deﬁne quadratic forms in all
characteristics, the bilinear form associated to Pn
i=1 x2
i would be twice the dot product.
We return to characteristic 2. The matrix for B in (7.6) doesn’t involve the diagonal co-
eﬃcients ai from (7.3). We have B = 0 if and only if all cross terms aij vanish (equivalently,
B = 0 if and only if Q has a diagonalization in some basis). When the characteristic is not
2 the cross terms of any quadratic form are 0 in a suitable basis, but we need cross terms
for Q in characteristic 2 if its associated symmetric bilinear form is not identically zero.
Example 7.2. Let F have characteristic 2 and let Q(x, y) = ax2 +bxy +cy2 be a quadratic
form on F 2. For v = (x, y) and v′ = (x′, y′) in F 2,
Q(v) =

x
y

·

a
b
0
c
 
x
y

and
B(v, v′) = Q(v + v′) −Q(v) −Q(v′)
= b(xy′ + x′y)
=

x
y

·

0
b
b
0
 
x′
y′

So B is nondegenerate if and only if b ̸= 0.
By deﬁnition, any quadratic form in characteristic 2 has an associated symmetric bilinear
form, but the correspondence from quadratic forms to symmetric bilinear forms in charac-
teristic 2 is neither injective nor surjective: diﬀerent quadratic forms like x2+xy and xy can
have the same symmetric bilinear form, and some symmetric bilinear forms like xx′ +yy′ do
not arise as the bilinear form of any quadratic form. In matrix language, every quadratic
form outside of characteristic 2 can be written as Q(v) = [v] · M[v] for some symmetric
matrix M, but this is not true in characteristic 2. A quadratic form in characteristic 2
with cross terms in a basis is not represented by a symmetric matrix in any basis. The
associated bilinear form, however, is always represented by a symmetric matrix. (See (7.5)

<!-- page 50 -->
50
KEITH CONRAD
and (7.6).) We have to be careful not to confuse a matrix like (7.4) for a quadratic form in
characteristic 2 with a matrix like (7.6) for its bilinear form.
A key observation is that the symmetric bilinear form associated to a quadratic form in
characteristic 2 is alternating:
B(v, v) = Q(2v) −2Q(v) = Q(0) −0 = 0.
(The matrix in (7.6) is indeed alternating.) In characteristic not 2, we were able to recover
Q from B since B(v, v) = Q(v), but in characteristic 2 we have B(v, v) = 0. Recall that
any alternating bilinear form is symmetric in characteristic 2. We should think about the
correspondence from Q to B in characteristic 2 as a map from quadratic forms to alternating
(not just symmetric) bilinear forms. Then it is surjective, but still never injective (Exercises
7.4 and 7.5). That is, there is nothing like polarization in characteristic 2, so knowledge of
B alone does not let us recover Q. Some concepts that can be discussed equally well in the
language of quadratic forms or symmetric bilinear forms outside of characteristic 2 may no
longer have formulations in both of these languages in characteristic 2.
One concept expressible in both languages is orthogonality of vectors. In characteristic
not 2, Q(v +w) = Q(v)+Q(w) if and only if B(v, w) = 0. This is also true in characteristic
2 (check!), so the condition v ⊥w, meaning B(v, w) = 0, can be described in terms of Q.
What is the characteristic 2 analogue of a diagonalization? Assume the bilinear form
B associated to an n-dimensional quadratic form Q in characteristic 2 is nondegenerate.
Then B is alternating and nondegenerate, so n = 2m is even and there is a symplectic basis
for B, say {e1, f1, . . . , em, fm}. When v1, . . . , vr are any vectors in V that are mutually
perpendicular (i.e., B(vi, vj) = 0 for i ̸= j), (7.2) becomes
Q(v1 + · · · + vr) = Q(v1) + · · · + Q(vr).
Therefore the expression of Q in the symplectic basis for B is
Q(x1e1 + y1f1 + · · · + xmem + ymfm)
=
m
X
i=1
Q(xiei + yifi)
=
m
X
i=1
(aix2
i + xiyi + biy2
i ),
(7.7)
where ai = Q(ei) and bi = Q(fi). Conversely, if a quadratic form Q looks like (7.7) in some
basis then its bilinear form B has the matrix representation (5.1) in a suitable ordering of
that basis (the coeﬃcients ai, bi don’t show up in B), so B is nondegenerate.
The expression (7.7) is a characteristic 2 analogue of the diagonalization (6.9) except
all quadratic forms outside characteristic 2 can be diagonalized while only those in char-
acteristic 2 whose bilinear form is nondegenerate admit a representation in the form (7.7).
Instead of writing Q as a sum of monomials ax2, we have written it as a sum of two-variable
quadratic forms ax2 + xy + by2. A matrix for Q in this symplectic basis is block diagonal
with blocks ( ai 1
0 bi ).
To extend (7.7) to the degenerate case, assume V ⊥̸= {0}.
Write
V = W ⊕V ⊥for some subspace complement W. Then B|W is nondegenerate, so choosing
a symplectic basis of W and tacking on any basis of V ⊥to create a basis of V gives Q the
expression
(7.8)
m
X
i=1
(aix2
i + xiyi + biy2
i ) +
r
X
k=1
ckz2
k,

<!-- page 51 -->
BILINEAR FORMS
51
where dim W = 2m and dim V ⊥= r. The coeﬃcients ck are the coeﬃcients from any choice
of basis for V ⊥. For instance, if Q vanishes at a nonzero vector in V ⊥then we can arrange
for some ck to be 0, so Q is a polynomial in fewer than n variables, where n = dim V .
We have referred already to the nondegeneracy of the bilinear form associated to a qua-
dratic form, but we have not yet deﬁned what it means for a quadratic form to be nonde-
generate. The following theorem will be needed for that.
Theorem 7.3. Let Q: V →F be a quadratic form in characteristic 2, with associated
bilinear form B. The following conditions are equivalent:
(1) the only v ∈V that satisﬁes Q(v) = 0 and B(v, w) = 0 for all w ∈V is v = 0,
(2) the function Q: V ⊥→F is injective,
(3) there is no basis of V in which Q can be written as a polynomial in fewer than n
variables, where n = dim V ,
(4) in any basis of V , the only common solution in V to Q(v) = 0 and (∂Q/∂xi)(v) = 0
for all i is v = 0.
This is an analogue of Theorem 6.37. Since Pn
k=1 xk(∂Q/∂xk) = 2Q, outside of charac-
teristic 2 the partials can all vanish only at a point where Q vanishes. But in characteristic
2 we have to explicitly include the condition Q(v) = 0 in (4).
Proof. Condition (1) is the same as saying the only element of V ⊥at which Q vanishes is
0. For v and v′ in V ⊥, Q(v + v′) = Q(v) + Q(v′), so the kernel of Q: V ⊥→F is 0 if and
only if Q|V ⊥is injective. Thus (1) and (2) are equivalent.
To show these conditions are equivalent to (3), a re-reading of the proof of Theorem 6.37
shows that even in characteristic 2 if Q is a polynomial in fewer than n variables in some
basis of V then V ⊥contains a nonzero vector at which Q vanishes. (One has to ignore
a few factors of 2 in that proof.) Conversely, if there is a nonzero vector in V ⊥at which
Q vanishes then the discussion surrounding (7.8) shows Q is a polynomial in fewer than n
variables relative to some basis of V .
We now show (4) is equivalent to (2). Write Q as in (7.3). Then
∂Q
∂xk
=
X
i<k
aikxi +
X
k<j
akjxj,
so the vanishing of all the partials of Q at a point (c1, . . . , cn) ∈F n is equivalent to
(7.9)





0
a12
· · ·
a1n
a12
0
· · ·
a2n
...
...
...
...
a1n
a2n
· · ·
0










c1
c2
...
cn




=





0
0
...
0




.
The matrix here, call it M, is a matrix for B: B(v, w) = [v]·M[w] (see (7.6)). If the partials
all vanish at a nonzero point in F n, say v, then M[v] = 0. Since M⊤= M, M[v] = 0 is
equivalent to B(v, w) = 0 for all w ∈V , which is equivalent to v ∈V ⊥. That is,
V ⊥=

v ∈V : ∂Q
∂xi
(v) = 0 for all i

.
Therefore a common solution in V to Q(v) = 0 and (∂Q/∂xi)(v) = 0 for all i is the same
as an element of ker(Q|V ⊥), so (4) is equivalent to (2).
□

<!-- page 52 -->
52
KEITH CONRAD
Deﬁnition 7.4. A quadratic form in characteristic 2 is called nondegenerate when the
equivalent conditions in Theorem 7.3 hold. Otherwise it is called degenerate.
Example 7.5. A nonzero 1-dimensional quadratic form is nondegenerate. In two dimen-
sions, the quadratic form ax2+bxy+cy2 on F 2 is nondegenerate if b ̸= 0 (i.e., V ⊥= {0}) or
if b = 0 (so V ⊥= V ) and ac is not a square in F. Otherwise it is degenerate. For instance,
xy on F 2 is nondegenerate while x2 + cy2 is nondegenerate if and only if c is a nonsquare
in F ×.
Example 7.6. Let Q(x, y, z) = x2 +xy +y2 +z2 be a quadratic form on F 3. Its associated
bilinear form is B((x, y, z), (x′, y′, z′)) = xy′ + x′y, so B is a degenerate bilinear form.
However, we will see Q is a nondegenerate quadratic form according to Deﬁnition 7.4.
In matrix notation,
Q(x, y, z) =


x
y
z

·


1
1
0
0
1
0
0
0
1




x
y
z


and the associated bilinear form has matrix


0
1
0
1
0
0
0
0
0

,
whose kernel is V ⊥= F(0, 0, 1). Since Q(0, 0, γ) = γ2, ker(Q|V ⊥) = {0}.
Remark 7.7. If B is nondegenerate (that is, V ⊥= {0}) then Q is nondegenerate. Some
authors deﬁne Q to be nondegenerate in characteristic 2 only when B is nondegenerate. This
rules out odd-dimensional examples. However, there are odd-dimensional nondegenerate
quadratic forms according to Deﬁnition 7.4, as we just saw.
In characteristic not 2, nondegeneracy of a quadratic form (deﬁned as invertibility of
a representative symmetric matrix, with equivalent conditions given in Theorem 6.37) is
unaﬀected by viewing it as a quadratic form over a larger base ﬁeld. This is not usually
true in characteristic 2.
Example 7.8. Let F have characteristic 2 and deﬁne Q on V = F 2 by Q(x, y) = x2 + cy2
where c is a nonsquare in F. Then V ⊥= V and Q is injective on V ⊥, so Q is nondegenerate
on F 2. But Q becomes degenerate on F
2 since c is a square in F.
Example 7.9. Letting c again be a nonsquare in F, the quadratic form xy + z2 + cw2 on
F 4 is nondegenerate, but it is degenerate on F
4 since the term z2 +cw2 becomes a complete
square so the quadratic form can be written as a polynomial in fewer than 4 variables.
Deﬁnition 7.10. Let F have characteristic 2 and Q: V →F be a quadratic form. A null
vector for Q is a nonzero v ∈V such that Q(v) = 0. We call Q universal if Q(V ) = F.
Quadratic forms Q1 : V1 →F and Q2 : V2 →F are called equivalent if there is a linear
isomorphism A: V1 →V2 such that Q2(Av) = Q1(v) for all v ∈V1.
Remark 7.11. These terms have the same meaning as they did outside of characteristic 2,
with one caveat: quadratic form equivalence and null vectors for a quadratic form outside
of characteristic 2 can always be deﬁned in terms of the associated bilinear form, but this
is false in characteristic 2.
For instance, in characteristic 2 B(v, v) = 0 for all v (B is
alternating) while the condition Q(v) = 0 is restrictive.

<!-- page 53 -->
BILINEAR FORMS
53
To get used to the characteristic 2 terminology in Deﬁnitions 7.4 and 7.10, note that
Q: V →F is nondegenerate precisely when V ⊥contains no null vectors for Q. (This is also
true outside of characteristic 2!) Equivalent quadratic forms either both have a null vector
or neither has a null vector. Any degenerate quadratic form has a null vector (just like in
characteristic not 2).
As further practice with the terminology we prove the following two theorems. The ﬁrst
one is a characteristic 2 analogue of Theorem 6.24.
Theorem 7.12. If Q is nondegenerate and has a null vector then it is universal.
Proof. The proof will be very close to that of Theorem 6.24, but note the few slight changes.
Let v be a null vector. Since Q(cv) = c2Q(v) = 0 and Q is not identically zero (otherwise
it couldn’t be nondegenerate), dim V ≥2. By nondegeneracy of Q there are no null vectors
in V ⊥, so v ̸∈V ⊥. Therefore there is a w ∈V such that B(v, w) ̸= 0. Then for any c ∈F,
Q(cv + w) = Q(cv) + Q(w) + B(cv, w) = Q(w) + B(v, w)c.
Since B(v, w) ̸= 0, this is a linear function of c and therefore takes on all values in F as c
varies.
□
Theorem 7.13. Let Q: V →F be a nondegenerate quadratic form. If Q has a null vector
e, then it has a second null vector f such that B(e, f) = 1 and B is nondegenerate on the
plane Fe + Ff.
Proof. Since Q is nondegenerate and e is a null vector, e ̸∈V ⊥. Therefore B(e, w) ̸= 0 for
some w ∈W, so e and w are linearly independent. We can scale w so B(e, w) = 1. Let
c = Q(w). Then e and f := ce + w are linearly independent null vectors and B(e, f) = 1,
so B is nondegenerate on the plane Fe ⊥Ff.
□
Theorem 7.13 resembles the initial part of the construction of a symplectic basis for
B, but it is a stronger condition to say v is a null vector of Q (that is, Q(v) = 0) than
to say B(v, v) = 0. Besides, Theorem 7.13 makes sense in odd dimensions, where B is
automatically degenerate and V has no symplectic basis.
We now turn to the classiﬁcation of nondegenerate quadratic forms over a ﬁnite ﬁeld F
with characteristic 2. We will use repeatedly that every element in F is a square.
We begin with a series of lemmas.
Lemma 7.14. Any quadratic form over F with dimension at least 3 has a null vector.
Proof. This is the characteristic 2 analogue of Theorem 6.23. The odd characteristic proof
used an orthogonal basis, which is not available in characteristic 2.
Let Q be the quadratic form and B be its associated bilinear form. Pick v ̸= 0 in V . We
may suppose Q(v) ̸= 0. Since dim v⊥≥n −1 ≥2, we can pick w ∈v⊥with w ̸∈Fv. Then
Q(w) = aQ(v) for some a ∈F. Write a = b2, so Q(w) = Q(bv) and w ̸= bv. Since w ⊥v,
Q(w + bv) = Q(w) + Q(bv) = 0 and w + bv ̸= 0.
□
The bound dim V ≥3 is sharp: there is a two-dimensional nondegenerate quadratic form
over F without null vectors (Exercise 7.3).
Remark 7.15. There is a uniform proof of Theorem 6.23 and Lemma 7.14 for all ﬁnite
ﬁelds using the Chevalley–Warning theorem [7, pp. 143–145].
Lemma 7.16. Any quadratic form over F that is not identically zero is universal.

<!-- page 54 -->
54
KEITH CONRAD
Proof. Let Q: V →F be a quadratic form and Q(v0) ̸= 0. For c ∈F, Q(cv0) = c2Q(v0).
Squaring on F is a bijection, so {c2Q(v0) : c ∈F} = F. Therefore Q is universal.
□
The analogous result for ﬁnite ﬁelds in odd characteristic (Corollary 6.27) required non-
degeneracy and dimension at least 2.
Lemma 7.17. If Q: V →F is nondegenerate then dim V ⊥≤1. More precisely, V ⊥= {0}
if dim V is even and dim V ⊥= 1 if dim V is odd.
Proof. Let B be the bilinear form attached to Q, so B is alternating. The induced alternat-
ing bilinear form on V/V ⊥is nondegenerate, so dim(V/V ⊥) is even. Therefore the second
part of the theorem (knowing dim V ⊥from the parity of dim V ) will follow once we know
dim V ⊥≤1.
Suppose V ⊥̸= {0} and v0 is a nonzero vector in V ⊥, so Q(v0) ̸= 0. We want to show
V ⊥= Fv0. For any v′ ∈V ⊥, Q(v′) = aQ(v0) for some a ∈F. Write a = b2 for some b ∈F.
Then Q(v′) = Q(bv0), so Q(v′ −bv0) = 0 (Q is additive on V ⊥). By nondegeneracy of Q,
v′ −bv0 = 0, so v′ = bv0. Therefore V ⊥= Fv0.
□
Remark 7.18. For quadratic forms Q: V →F over a ﬁnite ﬁeld with characteristic 2,
Remark 7.7 and Lemma 7.17 tell us that nondegeneracy of Q is the same as nondegeneracy
of its bilinear form when dim V is even.
In the classiﬁcation of quadratic forms over ﬁnite ﬁelds with odd characteristic, the dis-
criminant plays a key role. In characteristic 2 the discriminant is useless because every
element of F is a square. Instead of working with squares and nonsquares in the multi-
plicative group of the ﬁnite ﬁeld, we will work with values and nonvalues of the function
℘: F →F given by ℘(a) = a2 + a. The function ℘is additive and has kernel {0, 1}, so ℘
takes on half the values in F. Moreover, F/℘(F) has size 2, so the sum of two non-℘values
in F is a ℘-value. (Note the analogy to squaring nonzero numbers in odd characteristic,
where the kernel is {±1}, half the nonzero elements are squares, and the product of two
nonsquares is a square.)
Theorem 7.19. Fix c ∈F −℘(F). Let Q be a nondegenerate quadratic form on V where
dim V is 1, 2, or 3. Then Q is equivalent to one of the following:
(1) x2 in dimension 1,
(2) xy or x2 + xy + cy2 in dimension 2, and these are inequivalent,
(3) xy + z2 in dimension 3.
Proof. Any nondegenerate one-dimensional quadratic form looks like ax2 in a basis, and a
is a square in F, so the quadratic form is equivalent to x2.
We now turn to the two-dimensional case. The quadratic forms xy and x2 + xy + cy2 on
F2 are inequivalent, since the ﬁrst one has a null vector (such as (1, 0)) and the second one
does not: if it had a null vector (x0, y0) then y0 ̸= 0 and then c = (x0/y0)2 + x0/y0 ∈℘(F).
It remains, in the two-dimensional case, to show Q has one of the two indicated forms in
some basis. Since Q is universal by Lemma 7.16, pick v such that Q(v) = 1. By Lemma
7.17 V ⊥= {0}, so B is nondegenerate. Therefore there is a w such that B(v, w) = 1. Then
{v, w} is a basis of V and
Q(xv + yw) = Q(xv) + Q(yw) + B(xv, yw) = x2 + xy + Q(w)y2.
If Q(w) = a2 + a for some a, then
x2 + xy + Q(w)y2 = x2 + xy + (a2 + a)y2 = (x + ay)(x + (a + 1)y) = x′y′

<!-- page 55 -->
BILINEAR FORMS
55
where x′ = x + ay and y′ = x + (a + 1)y. Therefore Q is equivalent to xy. If Q(w) ̸= a2 + a
for any a then Q(w) = c in F/℘(F), so Q(w) + c = a2 + a for some a ∈F. Thus
x2 + xy + Q(w)y2 = x2 + xy + (a2 + a + c)y2 = (x + ay)2 + (x + ay)y + cy2,
which is the same as x2 + xy + cy2 after a linear change of variables.
Now we treat the three-dimensional case. By Lemma 7.14 there is a null vector, say e.
By Theorem 7.13 there is a null vector f such that B(e, f) = 1 and B is nondegenerate
on the plane Fe + Ff. In particular, this plane meets V ⊥in {0}. Lemma 7.17 says V ⊥
is one-dimensional, so any nonzero element of V ⊥along with e and f gives a basis of V .
Let g be a nonzero vector in V ⊥, so Q(g) ̸= 0 by nondegeneracy, Since Q(ag) = a2Q(g), by
rescaling g we can suppose Q(g) = 1. Since g ⊥(Fe + Ff),
Q(xe + yf + zg) = Q(xe + yf) + Q(zg) = xyB(e, f) + z2Q(g) = xy + z2,
which is what we want since {e, f, g} is a basis.
□
Theorem 7.20. Fix c ∈F −℘(F). For n ≥2, any n-dimensional nondegenerate quadratic
form over F is equivalent to exactly one of
x1x2 + x3x4 + · · · + xn−3xn−2 +
(
xn−1xn, or
x2
n−1 + xn−1xn + cx2
n
if n is even and
x1x2 + x3x4 + · · · + xn−2xn−1 + x2
n
if n is odd.
This is comparable to (6.10) and (6.11), except there is just one choice when n is odd.
The theorem is not asserting that the two choices in the even case are inequivalent, although
that does turn out to be true. We will return to this issue after proving the theorem.
Proof. We induct on n. By Theorem 7.19, we can suppose n ≥4.
Let Q be a nondegenerate quadratic form on V , where n = dim V . By Lemma 7.14 there
is a null vector for Q, say v. By Theorem 7.13, there is an independent null vector w such
that B(v, w) = 1 and B is nondegenerate on the plane U = Fv + Fw. Since Q has a null
vector in U, Q|U looks like xy in a suitable basis by Theorem 7.19.
Assume n is even. Then V ⊥= {0}: B is nondegenerate on V . Thus V = U ⊕U⊥and
B|U⊥is nondegenerate (Theorem 3.12). Therefore Q|U⊥is nondegenerate (Remark 7.18).
We are now done by induction.
Assume n is odd, so n ≥5. Then dim V ⊥= 1 by Lemma 7.17. Since Q is not identically
zero on V ⊥by nondegeneracy, Q|V ⊥is x2 in a suitable basis. Let W be a subspace of V
complementary to V ⊥: V = W ⊕V ⊥, dim W is even and B|W is nondegenerate. Therefore
(Remark 7.18) Q|W is nondegenerate. By the even-dimensional case (for dimension n −1)
Q|W is equivalent to one of
x1x2 + x3x4 + · · · + xn−4xn−3 +
(
xn−2xn−1, or
x2
n−2 + xn−2xn−1 + cx2
n−1.
Since Q = Q|W + Q|V ⊥and Q|V ⊥looks like x2
n in a suitable basis, the expression of Q in
the combined basis for W and V ⊥looks like one of
(7.10)
x1x2 + x3x4 + · · · + xn−4xn−3 +
(
xn−2xn−1 + x2
n, or
x2
n−2 + xn−2xn−1 + cx2
n−1 + x2
n.

<!-- page 56 -->
56
KEITH CONRAD
The two “end choices” here are xy + z2 and x2 + xy + cy2 + z2. By generalizing Example
7.6, x2 + xy + cy2 + z2 is a nondegenerate quadratic form on F 3. It is equivalent to xy + z2
by Theorem 7.19, so the two possible expressions for Q in (7.10) are equivalent.
□
We now explain why the two representative quadratic forms when n is even are inequiv-
alent.
The smallest case, n = 2, involves xy and x2 + xy + cy2 where c ̸∈℘(F). These can be
distinguished by counting null vectors in F2: xy has some and x2 + xy + cy2 has none. The
same idea works for even n > 2: the two n-dimensional quadratic forms in Theorem 7.20
don’t have the same number of null vectors, so they are inequivalent. We will prove this by
counting.
Deﬁnition 7.21. Let Q: V →F be a quadratic form over F. Set z(Q) = |{v ∈V : Q(v) =
0}|.
The number z(Q) is 1 more than the number of null vectors of Q.
Example 7.22. If V = F2 and Q: V →F is nondegenerate then Q is equivalent to
either xy or x2 + xy + cy2, where c ̸∈℘(F).
A calculation shows z(xy) = 2q −1 and
z(x2 + xy + cy2) = 1, where q = |F|.
Any nonzero quadratic form Q over F is universal (Lemma 7.16), so the sets Q−1(a) are
all nonempty as a varies in F. Moreover, Q takes on each nonzero value in F equally often:
if a ∈F× and we write a = b2, then the sets Q−1(a) and Q−1(1) are in bijection using
v ↔(1/b)v. However these sets need not be in bijection with Q−1(0), as we can see already
in the case of Q(x, y) = xy: |Q−1(a)| = q−1 for a ̸= 0 and |Q−1(0)| = 2q−1, where q = |F|.
The number z(Q) = |Q−1(0)| is therefore distinctive.
Lemma 7.23. Let Q: V →F be a quadratic form over F and set q = |F|. Writing h for
the quadratic form xy on F2,
z(Q ⊥h) = qz(Q) + (q −1)|V |,
where Q ⊥h is the quadratic form on V ⊕F2 given by (Q ⊥h)(v, u) = Q(v) + h(u).
Proof. The vanishing of (Q ⊥h)(v, u) is equivalent to Q(v) = h(u). We count this event
separately according to h(u) = 0 and h(u) ̸= 0:
z(Q ⊥h) = |{(v, u) : Q(v) = h(u)}|
=
X
u
|Q−1(h(u))|
=
X
h(u)=0
|Q−1(0)| +
X
h(u)̸=0
|Q−1(h(u))|
= z(h)z(Q) +
X
h(u)̸=0
|Q−1(1)|
= (2q −1)z(Q) + (q2 −z(h))|Q−1(1)|
= (2q −1)z(Q) + (q −1)2|Q−1(1)|.
We have |Q−1(1)| = (|V | −z(Q))/(q −1) since Q: V →F takes nonzero values equally
often. Substitute this into the formula for z(Q ⊥h) and simplify.
□

<!-- page 57 -->
BILINEAR FORMS
57
Theorem 7.24. For n = 2m with m ≥1,
z(x1x2 + x3x4 + · · · + xn−3xn−2 + xn−1xn) = q2m−1 + qm −qm−1
and
z(x1x2 + x3x4 + · · · + xn−3xn−2 + x2
n−1 + xn−1xn + cx2
n) = q2m−1 −qm + qm−1.
So the two quadratic forms for even n in Theorem 7.20 are inequivalent.
Proof. Induct on m, using Example 7.22 and Lemma 7.23.
□
Table 3 compares quadratic forms in diﬀerent characteristics. In the table QF means
quadratic form, SBF and ABF refer to symmetric/alternating bilinear forms, and F is a
ﬁnite ﬁeld.
Characteristic not 2
Characteristic 2
Bijection QF to SBF
Surjection QF to ABF
Q(v) = [v] · M[v], M symm.
Q(v) = [v] · N[v], N upper-tri.
B(v, w) = [v] · M[w]
B(v, w) = [v] · (N + N⊤)[w]
B(v, v) = Q(v)
B(v, v) = 0
B(v, w) = 0 ⇔Q(v + w) = Q(v) + Q(w)
Same
Q nondeg. 2-d w/ null vec. ⇒Q ∼xy
Same
Two nondeg. in each dim. over F
Same in even dim.,
one in each odd dim.
Table 3. Quadratic Form Comparisons
Another approach to the inequivalence of the two quadratic forms over F in each even
dimension is based on a characteristic 2 substitute for the discriminant: the Arf invariant.
It can be deﬁned fairly (but not completely!) generally, not just over ﬁnite ﬁelds. For F of
characteristic 2, let Q be a quadratic form over F whose bilinear form B is nondegenerate.
(This is only a special case of nondegenerate Q, but when F is ﬁnite it is exactly the case
of nondegenerate even-dimensional quadratic forms, which is the application we have in
mind anyway.) When Q is expressed as in (7.7), the Arf invariant of Q is deﬁned to be
the class of the sum Pm
i=1 aibi in the additive group F/℘(F). Equivalently, if n = 2m and
{e1, f1, . . . , em, fm} is a symplectic basis of V then the Arf invariant of Q is
(7.11)
m
X
i=1
Q(ei)Q(fi) mod ℘(F).
The quadratic form x2 + xy + cy2 has Arf invariant c.
The Arf invariant is an invariant: changing the symplectic basis changes (7.11) by an
element of ℘(F). See [4] or [11, pp. 340–341] for a proof. In particular, equivalent quadratic
forms having nondegenerate bilinear forms have the same Arf invariant.
The classiﬁcation of nondegenerate quadratic forms over ﬁnite ﬁelds with characteristic
2 extends to perfect ﬁelds. Lemmas 7.14, 7.16, and 7.17 work for perfect ﬁelds. Over any
perfect ﬁeld F of characteristic 2, there is one equivalence class of nondegenerate quadratic
forms in each odd dimension and |F/℘(F)| equivalence classes in each even dimension
(distinguished by the Arf invariant).
We end our discussion of quadratic forms in characteristic 2 with the terminology of
quadratic spaces.

<!-- page 58 -->
58
KEITH CONRAD
Deﬁnition 7.25. A quadratic space in characteristic 2 is a vector space over a ﬁeld of
characteristic 2 equipped with a choice of quadratic form on it.
If (V, Q) is a quadratic space in characteristic 2 then it provides us with an alternating
bilinear space (V, B), where B(v, w) = Q(v + w) −Q(v) −Q(w).
This correspondence
from quadratic spaces to alternating bilinear spaces in characteristic 2 is surjective but not
injective. That is, a quadratic space has more structure than an alternating bilinear space
in characteristic 2.
Deﬁnition 7.26. A hyperbolic plane in characteristic 2 is a two-dimensional quadratic space
in characteristic 2 where the quadratic form looks like xy in some basis.
Example 7.27. Let V = F 2, Q1(x, y) = x2 + xy, and Q2(x, y) = x2 + xy + cy2 where
c ∈F −℘(F). Both Q1 and Q2 have the same (nondegenerate) bilinear form B(v, w) =
v ·( 0 1
1 0 )w, but (V, Q1) is a hyperbolic plane while (V, Q2) is not. Thus a hyperbolic plane in
the sense of quadratic spaces in characteristic 2 is stronger than in the sense of alternating
bilinear spaces in characteristic 2 (Exercise 3.4).
Theorem 7.28. Let (V, Q) be a two-dimensional quadratic space. The following conditions
are equivalent:
(1) (V, Q) is a hyperbolic plane,
(2) Q is nondegenerate and has a null vector.
Proof. This proof will be diﬀerent from that of the analogous Theorem 6.18.
Clearly the ﬁrst condition implies the second. Now we show the converse. Let v be a
null vector for Q and let B be the bilinear form associated to Q. By Theorem 7.13 there is
a null vector w such that B(v, w) = 1. Using the basis {v, w},
Q(xv + yw) = Q(xv) + Q(yw) + B(xv, yw) = xyB(v, w) = xy.
□
Deﬁnition 7.29. Let F have characteristic 2 and (V1, Q1) and (V2, Q2) be quadratic spaces
over F. Their orthogonal direct sum V1 ⊥V2 is the vector space V1 ⊕V2 with the quadratic
form Q(v1, v2) = Q1(v1) + Q2(v2). The quadratic spaces (Vi, Qi) are called isomorphic if
there is a linear isomorphism A: V1 →V2 such that Q2(Av) = Q1(v) for all v ∈V1.
We used orthogonal direct sums already in Lemma 7.23 and all hyperbolic planes over F
are isomorphic.
Denoting a hyperbolic plane over F as H, Theorem 7.20 says every nondegenerate qua-
dratic space over ﬁnite F of characteristic 2 is isomorphic to H⊥m ⊥W where dim W ≤2.
This is like the situation in odd characteristic, except that when dim W = 1 there are two
choices for W in odd characteristic and one choice in characteristic 2.
For more on quadratic forms in characteristic 2, see [6], [8], [9], [10], and [11].
Exercises.
1. For F of characteristic 2, decide if the following quadratic forms are nondegenerate:
(1) Q(x, y, z) = ax2 + xy + by2 + cz2 on F 3 with c ̸= 0,
(2) Q(x, y, z, t) = xy + yz + zt on F 4,
(3) det: M2(F) →F,
(4) Q(L) = Tr(L2) on EndF (V, V ) for ﬁnite-dimensional V .
2. For c ∈℘(F), convert x2 + xy + cy2 to xy by an explicit linear change of variables.

<!-- page 59 -->
BILINEAR FORMS
59
3. Redo Exercise 6.5 when F has characteristic 2, but show the quadratic form NK/F
is nondegenerate if and only if K/F is separable. When F = F is ﬁnite show NK/F
looks like x2 + cxy + y2 in some basis, where T 2 + cT + 1 is irreducible over F. Is
this true for ﬁnite ﬁelds of odd characteristic?
4. Let V be n-dimensional over a ﬁeld F of characteristic 2. Let B be an alternating
bilinear form on V and {e1, . . . , en} be a basis of V . For a1, . . . , an in F, show there
is a unique quadratic form Q on V such that Q(ei) = ai for all i and the bilinear
form associated to Q is B.
5. When F has characteristic 2 and Q is a quadratic form on F n, let N be a matrix
representing Q in the standard basis: Q(v) = v · Nv for v ∈F n. Show a matrix
represents Q in the standard basis if and only if it has the form N + A where A is
an alternating matrix.
6. If ax2+xy+by2 and a′x2+xy+b′y2 are equivalent on F 2 where F has characteristic
2 then show explicitly that ab ≡a′b′ mod ℘(F). Do not assume F is perfect. Is the
converse true for all F?
7. Let n be a positive even integer and F be a ﬁnite ﬁeld with characteristic 2. For
a nondegenerate n-dimensional quadratic form Q over F, its Arf invariant (7.11)
is one of the two classes in F/℘(F). Set n+(Q) = |{v ∈V : Q(v) ∈℘(F)}| and
n−(Q) = |{v ∈V : Q(v) ̸∈℘(F)}|.
Use Theorem 7.24 to show these numbers
equal qn(qn ± 1)/2, with n+(Q) > n−(Q) when Q has Arf invariant ℘(F) and
n−(Q) > n+(Q) when Q has Arf invariant ̸= ℘(F). Therefore the Arf invariant of
Q is the class of F/℘(F) where Q takes the majority of its values. (Topologists call
this “Browder’s democracy” [1, Prop. III.1.18].)
8. Here is a “proof” that dimF (V ⊥) ≤1 for a nondegenerate Q over any ﬁeld F of
characteristic 2. By the deﬁnition of nondegeneracy, Q: V ⊥→F is injective, so
dimF (V ⊥) equals the F-dimension of its image. An injective map in linear algebra
does not increase dimensions, so dimF (V ⊥) ≤dimF F = 1. Where is the error?
8. Bilinear forms and tensor products
At the end of Section 1 we saw that a bilinear form B on a vector space V can be thought
of in two ways as a linear map V →V ∨, namely LB and RB. For ﬁnite-dimensional V
we saw in Section 2 that the matrix of B in a basis of V is also the matrix of RB, while
the matrix for LB is the transpose of that for RB since LB and RB are dual to each other
(Theorem 1.21). Having the matrix for B match that of RB rather than LB is due to the
convention that we write bilinear forms on F n as v · Aw rather than Av · w for matrices
A ∈Mn(F). Is there a way to think about a bilinear form as a linear map without taking
preference for RB over LB? Yes, using tensor products.
The tensor product construction turns bilinear maps into linear maps.
If we have a
bilinear form B : V ×V →F, we obtain for free a linear map TB : V ⊗F V →F characterized
by its values on simple tensors: TB(v ⊗w) = B(v, w). While LB and RB both map V to
V ∨, TB maps V ⊗F V to F. From any linear map T : V ⊗F V →F we get a bilinear form
BT : V × V →F by BT (v, w) = T(v ⊗w). The correspondences B ⇝TB and T ⇝BT
are bijections between the bilinear forms on V and the linear maps V ⊗F V →F. Linear
maps to F mean dual space, so the space Bil(V ) of all bilinear forms on V is naturally
identiﬁable with (V ⊗F V )∨, which is naturally isomorphic to V ∨⊗F V ∨= (V ∨)⊗2 using
(ϕ ⊗ψ)(v ⊗w) = ϕ(v)ψ(w). Thus the bilinear forms on V “are” the elements of (V ∨)⊗2.

<!-- page 60 -->
60
KEITH CONRAD
One new thing we can do with bilinear forms in the tensor product language is multiply
them in a natural way. This is worked out in Exercise 8.1. Recall that if we think about
bilinear forms on V as linear maps V →V ∨it makes no sense to compose such maps, so
multiplication of bilinear forms was a meaningless concept before.
Another advantage to tensor products is its use in extending a bilinear form to a larger
scalar ﬁeld. First we describe this construction without tensor products. When we write
a bilinear form as a matrix, so it becomes a bilinear form on F n, we can view it as a
bilinear form over a larger ﬁeld K ⊃F by having the same matrix act as a bilinear form on
Kn. (Why do this? Well, one might want to study a real bilinear form over the complex
numbers.) If we use a diﬀerent basis the bilinear form becomes a diﬀerent matrix, and
thus a diﬀerent bilinear form on Kn. This second bilinear form on Kn is equivalent to the
bilinear form on Kn from the ﬁrst matrix, so this operation passing from bilinear forms
over F to bilinear forms over K is well-deﬁned if the result is considered as a bilinear form
on Kn up to equivalence. Clearly it would be nicer if we had a coordinate-free way to pass
from a bilinear form over F to a bilinear form over K and not something deﬁned only up
to equivalence. Using tensor products as a device to extend scalars, we can achieve this. If
B : V × V →F is bilinear and K/F is a ﬁeld extension, then we obtain a bilinear form BK
on K ⊗F V whose values on pairs of simple tensors are given by
BK(α ⊗v, β ⊗w) = αβB(v, w).
That this formula yields a well-deﬁned bilinear form BK on K ⊗F V comes from the way
one constructs maps out of tensor products, and is left to the reader.8 Using an F-basis
for V as a K-basis for K ⊗F V , the matrix associated to BK is the same as the matrix
associated to B, so we recover the previous matrix-based construction.
In a similar way, a quadratic form Q: V →F can be extended to a quadratic form
QK : K ⊗F V →K, whose values on simple tensors are
QK(α ⊗v) = α2Q(v).
The bilinear form associated to QK is the extension to K of the bilinear form associated
to Q.
In concrete language, all we are doing here is writing a homogeneous quadratic
polynomial with coeﬃcients in F as a polynomial with its coeﬃcients viewed in K. The
tensor language makes the construction coordinate-free.
Returning to the issue of LB versus RB, we can consider the choice that is always available
between them by thinking about a general bilinear map V × W →U where V , W, and U
are any F-vector spaces. Such a bilinear map corresponds to a linear map V ⊗F W →U,
and there are natural isomorphisms
HomF (V ⊗F W, U) ∼= HomF (V, HomF (W, U)),
HomF (V ⊗F W, U) ∼= HomF (W, HomF (V, U)).
The ﬁrst isomorphism turns f ∈HomF (V ⊗F W, U) into v 7→[w 7→f(v⊗w)] and the second
isomorphism turns f into w 7→[v 7→f(v ⊗w)]. When W = V and U = F these are the two
diﬀerent isomorphisms (V ⊗F V )∨→HomF (V, V ∨) by B 7→LB and B 7→RB. In the most
general setting, though, LB and RB are analogues of linear maps between diﬀerent spaces.
8There is not just one construction of the tensor product, and diﬀerent constructions will produce only
equivalent bilinear forms over K, so we haven’t really removed the “up to equivalence” aspect of the con-
struction by comparison to the matrix viewpoint.
But the tensor construction is more elegant, and is
coordinate-free.

<!-- page 61 -->
BILINEAR FORMS
61
The two special classes of bilinear forms, symmetric and alternating, can be described in
the language of symmetric and exterior squares. Viewing a bilinear form as a linear map
V ⊗F V →F, it is symmetric when it kills all tensors of the form v ⊗w −w ⊗v and it
is alternating when it kills all tensors of the form v ⊗v. Therefore a symmetric bilinear
form B is the same thing as a linear map Sym2(V ) →F sending v · w to B(v, w), where
· is the symmetric product in Sym2(V ) (not the dot product, which only makes sense on
vectors in F n anyway). An alternating bilinear form B is the same thing as a linear map
Λ2(V ) →F sending v ∧w to B(v, w). Again, linear maps to F form the dual space, so
symmetric bilinear forms on V are the elements of Sym2(V )∨and alternating bilinear forms
on V are the elements of Λ2(V )∨. We can identify Sym2(V )∨with Sym2(V ∨) and Λ2(V )∨
with Λ2(V ∨).
While Sym2(V ) and Λ2(V ) are properly deﬁned as quotient spaces of V ⊗2, outside of
characteristic 2 we can identify these with subspaces of V ⊗2, using v ⊗w +w ⊗v in place of
v · w ∈Sym2(V ) and v ⊗w −w ⊗v in place of v ∧w ∈Λ2(V ). Using these identiﬁcations,
the formula v ⊗w =
1
2(v ⊗w + w ⊗v) + 1
2(v ⊗w −w ⊗v) on simple tensors shows
V ⊗2 = Sym2(V ) ⊕Λ2(V ). Replacing V with V ∨, we get
(8.1)
(V ∨)⊗2 = Sym2(V ∨) ⊕Λ2(V ∨),
outside of characteristic 2, which is the coordinate-free expression of a general bilinear form
as a unique sum of a symmetric and skew-symmetric bilinear form (Theorem 1.7).
Remark 8.1. The “ﬂip” automorphism on (V ∨)⊗2 = V ∨⊗F V ∨, where ϕ ⊗ψ 7→ψ ⊗ϕ on
simple tensors, has order 2. When F has characteristic not 2, (V ∨)⊗2 decomposes into the
{±1}-eigenspaces for the ﬂip automorphism, and this eigenspace decomposition is (8.1).
Exercises.
1. If (V1, B1) and (V2, B2) are bilinear spaces, show there is a unique bilinear form
“B1 ⊗B2” on V1 ⊗F V2 where (B1 ⊗B2)(v1 ⊗v2, v′
1 ⊗v′
2) := B1(v1, v′
1)B2(v2, v′
2).
(The proof that B1⊗B2 is well-deﬁned can be simpliﬁed using Exercise 1.6.) This can
be considered a multiplication for bilinear forms. If B1 and B2 are both symmetric,
show B1 ⊗B2 is symmetric.
If B1 and B2 are both alternating, or both skew-
symmetric, does B1 ⊗B2 inherit the same property?
2. Viewing bilinear forms on V as elements of (V ∨)⊗2, we can use B1 and B2 in the
previous exercise to form the simple tensor B1 ⊗B2 in (V ∨
1 )⊗2 ⊗F (V ∨
2 )⊗2, a vector
space that is naturally isomorphic to (V ∨
1 ⊗F V ∨
2 )⊗2. If we further identify V ∨
1 ⊗F V ∨
2
with (V1 ⊗F V2)∨, show that the simple tensor B1 ⊗B2 in (V ∨
1 )⊗2 ⊗F (V ∨
2 )⊗2 gets
identiﬁed with the function B1 ⊗B2 on (V1 ⊗F V2)⊗2 in the previous exercise.
3. For two ﬁnite-dimensional vector spaces V and W over F, where the characteristic
of F is not 2, a symmetric bilinear form B on V ⊗W is completely determined by
its values B(t, t) as t ranges over all tensors t ∈V ⊗F W (Theorem 1.8). This does
not say B is determined by its values B(v ⊗w, v ⊗w) on all elementary tensors,
since that is less information than knowledge of all B(t, t) (when V and W have
dimension greater than 1). But is knowing just the values B(v ⊗w, v ⊗w) enough
to determine B in general?
Take V = W = F 2, so V ⊗F W is 4-dimensional. Let {e1, e2} be the standard
basis of F 2, and in F 2 ⊗F F 2 set eij = ei ⊗ej, so {e11, e12, e21, e22} is a basis of

<!-- page 62 -->
62
KEITH CONRAD
F 2 ⊗F F 2.
Deﬁne two symmetric bilinear forms B and eB on F 2 ⊗F F 2 by the
following “symmetric” values on basis pairs:
• B(e11, e22) = B(e22, e11) = 1, all other B(eij, ekℓ) are 0,
• eB(e12, e21) = eB(e21, e12) = 1, all other eB(eij, ekℓ) are 0,
From the deﬁnitions, B ̸= eB on F 2 ⊗F F 2 (why?). However, show B(v⊗w, v⊗w) =
eB(v ⊗w, v ⊗w) for all v and w in F 2.
4. For bilinear spaces V1 and V2, describe the discriminant of V1 ⊗F V2 in terms of the
discriminants of V1 and V2. Conclude that V1 ⊗F V2 is nondegenerate if and only if
V1 and V2 are nondegenerate.
5. For quadratic spaces (V1, Q1) and (V2, Q2), show V1 ⊗F V2 becomes a quadratic
space using (Q1 ⊗Q2)(v1 ⊗v2) = Q1(v1)Q2(v2). If B1 and B2 are the bilinear forms
associated to Q1 and Q2 respectively, show the bilinear form associated to Q1 ⊗Q2
is B1 ⊗B2 from the ﬁrst exercise. Allow ﬁelds of characteristic 2.
6. Let (V1, Q1) and (V2, Q2) be nondegenerate quadratic spaces over a common ﬁeld not
of characteristic 2. Express the quadratic forms relative to orthogonal bases as Q1 =
P aix2
i and Q2 = P bjy2
j . Show the quadratic form Q1 ⊗Q2 has a diagonalization
P
i,j aibjz2
ij.
7. Let B and B′ be positive-deﬁnite symmetric bilinear forms on V and V ′, with
orthogonal bases {ei} in V and {e′
j} in V ′. Show the set of elementary tensors
{ei ⊗e′
j} is an orthogonal basis for the symmetric bilinear form B ⊗B′ on V ⊗R V ′,
and that B ⊗B′ is positive-deﬁnite.
8. (Continuation of Exercise 6.11) Let < be an ordering on a ﬁeld F.
When Q is
a nondegenerate quadratic form over F with signature (p, q) relative to <, deﬁne
sign<(Q) = p −q ∈Z. For nondegenerate quadratic forms Q and Q′ over F, show
sign<(Q ⊥Q′) = sign<(Q) + sign<(Q′) and sign<(Q ⊗Q′) = sign<(Q) sign<(Q′).9
In particular, if F = R and Q and Q′ are positive-deﬁnite then Q⊗Q′ is positive-
deﬁnite.
References
[1] W. Browder, “Surgery on Simply-Connected Manifolds,” Springer-Verlag, Berlin, 1972.
[2] C. Chevalley, “The Algebraic Theory of Spinors,” Columbia Univ. Press, New York, 1954.
[3] J. Dieudonne, “La G´eometrie des Groupes Classiques,” Springer-Verlag, Berlin, 1963.
[4] R. H. Dye, On the Arf Invariant, J. Algebra 53 (1978), 36–39.
[5] S. Garibaldi, The Characteristic Polynomial and Determinant are not ad hoc Constructions, Amer. Math.
Monthly 111 (2004), 761–778.
[6] L. C. Grove, “Classical Groups and Geometric Algebra,” Amer. Math. Society, Providence, 2002.
[7] K. Ireland and M. Rosen, “A Classical Introduction to Modern Number Theory,” 2nd ed., Springer-
Verlag, New York, 1990.
[8] I. Kaplansky, “Linear Algebra and Geometry: A Second Course,” Allyn & Bacon, Boston, 1969
[9] M-A. Knus, A. Merkurjev, M. Rost, J-P. Tignol, “The Book of Involutions,” Amer. Math. Soc., Provi-
dence, 1998.
[10] A. Pﬁster, “Quadratic Forms with Applications to Algebraic Geometry and Topology,” Cambridge
Univ. Press, Cambridge, 1995.
[11] W. Scharlau, “Quadratic and Hermitian Forms,” Springer-Verlag, Berlin, 1985.
9The behavior of sign< under ⊗explains why taking the diﬀerence in the order p −q is more natural
than in the order q −p; it would not be multiplicative in the other order.

<!-- page 63 -->
BILINEAR FORMS
63
[12] W. Scharlau, On the History of the Algebraic Theory of Quadratic Forms, pp. 229–259 in: “Quadratic
Forms and Their Applications,” E. Bayer-Fluckiger, D. Lewis, A. Ranicki eds., Amer. Math. Soc., Prov-
idence, 2000.
[13] D. Shapiro, “Compositions of Quadratic Forms,” de Gruyter, Berlin, 2000.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*