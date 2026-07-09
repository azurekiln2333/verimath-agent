# Dirichlet's Unit Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/unittheorem.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
DIRICHLET’S UNIT THEOREM
KEITH CONRAD
1. Introduction
Dirichlet’s unit theorem describes the structure of the unit group of orders in a number
ﬁeld.
Theorem 1.1 (Dirichlet, 1846). Let K be a number ﬁeld with r1 real embeddings and 2r2
pairs of complex conjugate embeddings. The unit group of an order in K is ﬁnitely generated
with r1 + r2 −1 independent generators of inﬁnite order.
More precisely, letting r = r1 + r2 −1, each order O in K contains multiplicatively inde-
pendent units ε1, . . . , εr of inﬁnite order such that every unit in O can be written uniquely
in the form
ζεm1
1
· · · εmr
r ,
where ζ is a root of unity in O and the mi’s are in Z. Abstractly, O× ∼= µ(O) × Zr1+r2−1,
where µ(O) is the ﬁnite cyclic group of roots of unity in O.
Units u1, . . . , uk are called multiplicatively independent, or just independent, when they
satisfy no multiplicative relations except the trivial one: um1
1
· · · umk
k
= 1 ⇒mi = 0 for all
i. It then follows that exponents in such a product are unique: if um1
1
· · · umk
k
= un1
1 · · · unk
k
then mi = ni for all i. This looks like linear independence, and that is exactly what it is:
when we view O× as a Z-module using its group law, multiplicative independence means
Z-linear independence.
If r1 > 0 then µ(O) = {±1} since ±1 are the only roots of unity in R. If r1 = 0 we could
still have µ(O) = {±1}, e.g., if O = Z[
√
d] for d < −1. (Note Z[√−1] has units {±1, ±i}.)
It is important that the unit groups of all orders in K have the same number of inde-
pendent generators of inﬁnite order: r1 + r2 −1. Therefore [O×
K : O×] is ﬁnite. A choice of
generators ε1, . . . , εr for O× (really, for the quotient group O×/µ(O)) is called a system of
fundamental units. We call r1 + r2 −1 the rank of the unit group.
The unit groups of orders in number ﬁelds were, historically, the ﬁrst important examples
of ﬁnitely generated abelian groups. Finding algorithms to produce explicit generators for
unit groups is one of the tasks of computational number theory.
In Section 2 we will look at some examples of the unit theorem. The theorem will be
proved in Section 3 and some more examples are described in Sections 4, 5, and 6.
2. Examples
Example 2.1. For Q(
√
2), r1 + r2 −1 = 1, so the unit group of each order in Q(
√
2) is
±εZ for some unit ε. In particular, Z[
√
2]× = ±(1 +
√
2)Z and Z[3
√
2]× = ±(17 + 12
√
2)Z.
Table 1 describes the unit group of the ring of integers of several number ﬁelds. Note
2 +
√
3 is a fundamental unit of Q(
√
3), but it is not part of a set of fundamental units in
the larger ﬁeld Q(
√
2,
√
3) since it is a square of a unit there: 2 +
√
3 = ((
√
2 +
√
6)/2)2.
1

<!-- page 2 -->
2
KEITH CONRAD
K
r1
r2
r1 + r2 −1
µ(OK)
O×
K
Q(
√
3)
2
0
1
±1
±(2 +
√
3)Z
Q(
√
5)
2
0
1
±1
±(1+
√
5
2
)Z
Q(ζ5)
0
2
1
µ10
µ10(1+
√
5
2
)Z
Q(
3√
2)
1
1
1
±1
±(1 +
3√
2 +
3√
4)Z
Q(
3√
6)
1
1
1
±1
±(1 −6
3√
6 + 3
3√
36)Z
Q(
4√
2)
2
1
2
±1
±(1 +
4√
2)Z(1 +
√
2)Z
Q(α)
3
0
2
±1
±αZ(α + 1)Z
Q(
√
2,
√
3)
4
0
3
±1
±(1 +
√
2)Z(
√
2 +
√
3)Z(
√
2+
√
6
2
)Z
Table 1. Unit group of OK. In row 7, α3 −3α −1 = 0.
Example 2.2. The unit group of an order is ﬁnite if and only if r1 +r2 −1 = 0. This means
(r1, r2) is (1, 0) or (0, 1), so K is Q or an imaginary quadratic ﬁeld. Moreover, the unit
group of each order in an imaginary quadratic ﬁeld is {±1} except for the maximal orders
Z[i] and Z[ζ3], whose units groups have size 4 and 6, respectively. There are a number of
important results in algebraic number theory that have a simpler form for Q and imaginary
quadratic ﬁelds than for other number ﬁelds, precisely because in these (and only these)
cases the unit group is ﬁnite.
Example 2.3. We have r1 + r2 −1 = 1 if and only if (r1, r2) = (2, 0), (1, 1), or (0, 2), i.e.,
K is real quadratic (e.g., Q(
√
2)), a cubic ﬁeld with only one real embedding (e.g., Q(
3√
2)),
or a totally complex quartic ﬁeld (e.g., Q(ζ5)).
Example 2.4. If K is a totally real cubic ﬁeld then r1 + r2 −1 = 2, so each order in K
has unit group of the form ±εZ
1 εZ
2 .
Example 2.5. We always have r1 + r2 −1 ≤n −1, where n = [K : Q] = r1 + 2r2. Easily
r1 + r2 −1 = n −1 if and only if r2 = 0, i.e., K is a totally real number ﬁeld.
Example 2.6. For a unit group with rank greater than 1 let’s see how to ﬁnd multiplicative
relations between units numerically, by discovering linear relations with logarithms ﬁrst. Set
K = Q(α) where α3 −3α −1 = 0. This is in Table 1. The polynomial f(T) = T 3 −3T −1
has 3 real roots, so O×
K has rank r1 + r2 −1 = 3 −1 = 2.
Before looking at O×
K, let’s show OK = Z[α]. Since disc(Z[α]) = −4(−3)3 −27(−1)2 =
81 = 34, [OK : Z[α]] divides 9. Therefore elements of OK when written in the basis {1, α, α2}
have coeﬃcients with denominator dividing 9. Since f(T + 1) = T 3 + 3T 2 −3 is Eisenstein
at 3 with α−1 as a root, elements of OK when written in the basis {1, α−1, (α−1)2} have
coeﬃcients with denominator prime to 3. This carries over to {1, α, α2}, so OK = Z[α].
(The Minkowski bound is exactly 2, and there is no prime ideal with norm 2 since T 3−3T −1
is irreducible modulo 2, so h(K) = 1: Z[α] is a PID.)
We now write down several units in Z[α]. For a, b ∈Q, NK/Q(aα + b) = −a3f(−b/a).
Check with this formula that α, α + 1, α −2, and 2α + 3 all have norm ±1, so they are all
in Z[α]×. The three roots of f(T) are α, 2 −α2, and α2 −α −2, so 2 −α2 and α2 −α −2
are in Z[α]×. The product of all three roots of f(T) is −f(0) = 1.
Since Z[α]× has rank 2, the 6 nontrivial units we just wrote down must admit some
nontrivial multiplicative relations. How can we ﬁnd such relations? We will use the three
diﬀerent embeddings K →R.
Call them σ1, σ2, and σ3.
The real roots of f(T) are

<!-- page 3 -->
DIRICHLET’S UNIT THEOREM
3
σ1(α), σ2(α), and σ3(α). Arranging the roots in increasing order,
σ1(α) = −1.532 . . . ,
σ2(α) = −.347 . . . ,
σ3(α) = 1.879 . . . .
For γ ∈K, NK/Q(γ) = σ1(γ)σ2(γ)σ3(γ). For u ∈O×
K, |σ1(u)σ2(u)σ3(u)| = 1. Taking
logarithms,
(2.1)
u ∈O×
K =⇒log |σ1(u)| + log |σ2(u)| + log |σ3(u)| = 0.
Deﬁne the logarithmic mapping L: K× →R3 by
L(γ) = (log |σ1(γ)|, log |σ2(γ)|, log |σ3(γ)|).
We will use such a map L in the proof of the general unit theorem. Here we will see how
L is useful computationally. Easily L is a group homomorphism and by (2.1), L(O×
K) is in
the hyperplane {(x, y, z) ∈R3 : x + y + z = 0}. The kernel of L in O×
K is {±1} (why?).
Table 2 gives numerical approximations to the images of some units under the mapping L.
γ
L(γ) (approx.)
α
(.4266, −1.0575, .6309)
α + 1
(−.6309, −.4266, 1.0575)
α −2
(1.2618, .8532, −2.1151)
2α + 3
(−2.7460, .8352, 1.9108)
2 −α2
(−1.0575, .6309, .4266)
α2 −α −2
(.6309, .4266, −1.0575)
Table 2. Log mapping on units.
The table suggests that L(α −2) = −2L(α + 1) = L(1/(α + 1)2), so α −2 = ±1/(α + 1)2.
The minus sign is needed since you can check purely algebraically that (α−2)(α+1)2 = −1.
By a computer algebra package, the 3 × 3 matrix (L(α) L(α + 1) L(2α + 3)) has (2, −3, 1)
in its kernel, so α2(α+1)−3(2α+3) has L-value 0. Therefore 2α+3 = ±α−2(α+1)3. Check
the plus sign holds. It looks like L(2−α2) = L(α+1)−L(α), so 2−α2 = ±(α+1)/α. Check
the minus sign holds. Since it looks like L(α2−α−2) = −L(α+1), α2−α−2 = ±1/(α+1).
Check the minus sign holds.
We suspect {α, α + 1} is a system of fundamental units for Z[α]× and will prove this in
Example 5.10.
3. Proof of the unit theorem
Our proof of the unit theorem is based on [5, Sect. 1.5] and [6, pp. 214–215] (see also [7,
p. 5]), and is deduced from a compactness theorem: the unit theorem is a consequence of a
certain group being compact.
We will use Minkowski’s convex-body theorem in our proof. This is a standard tool for
proofs of the unit theorem, although by comparison with typical applications of Minkowski’s
theorem we will be able to get by with a crudely chosen convex body: a suﬃciently large
ball will work.
Dirichlet did not use Minkowski’s theorem; he proved the unit theorem in 1846 while
Minkowski’s theorem appeared in 1889. Dirichlet’s substitute for the convex-body theorem
was the pigeonhole principle. (An account of Dirichlet’s proof in German is in [4, Sect.
183] and in English is in [8, Sect. 2.8–2.10].) Dirichlet did not state the unit theorem for
all orders, but only those of the form Z[α], since at that time these were the only kinds of

<!-- page 4 -->
4
KEITH CONRAD
orders that were considered. According to an oft-repeated story, the main idea for the proof
of the unit theorem came to Dirichlet while he attended a concert in the Sistine Chapel.1
We set some notation. As in the statement of the unit theorem, K is a number ﬁeld
of degree n, r1 is the number of real embeddings of K and 2r2 is the number of complex
embeddings of K (that is, embeddings K →C whose image is not in R), so n = r1 + 2r2.
Set V = Rr1 × Cr2, so dimR(V ) = n. The Euclidean embedding θK : K →V is deﬁned
using the real and complex embeddings of K, as follows. Let the real embeddings of K be
σ1, . . . , σr1 and let the complex embeddings of K be σr1+1, σr1+1, . . . , σr1+r2, σr1+r2, where
we collect the complex embeddings into conjugate pairs σj, σj. For α ∈K, we set2
θK(α) = (σ1(α), · · · , σr1(α), σr1+1(α), · · · , σr1+r2(α)) ∈V.
Algebraically, V is a commutative ring using component wise operations. Give V its natural
topology as a Euclidean space and all subsets of V will be given the subspace topology. A
particular subset we will care about is V × = (R×)r1 × (C×)r2.
Let N: V →R by
N(x1, . . . , xr1, z1, . . . , zr2) = x1 · · · xr1|z1|2 · · · |zr2|2 = x1 · · · xr1z1z1 · · · zr2zr2.
On the image of K in V , N looks like the norm: N(θK(α)) = NK/Q(α) for all α ∈K. Set
G = {v ∈V × : |N(v)| = 1}.
This is a subgroup of V ×, and it is closed in V since G is the inverse image of {1} under
the continuous map V →R given by v 7→|N(v)|. Thus G is a closed subgroup of V ×.
Let O be an order in K and set
U = θK(O×) = G ∩θK(O).
(Think “U = units”.) We have U ⊂G since O× = {α ∈O : |NK/Q(α)| = 1}. Since we give
G the subspace topology from V and the image of O in V under the Euclidean embedding
is discrete, U is discrete in G. We will be interested in the quotient group G/U.
Example 3.1. Let K = Q(
√
2) and O = OK = Z[
√
2]. Then V = R2 and N: V →R
by N(x, y) = xy. The Euclidean embedding θ: Q(
√
2) →R2 places Z[
√
2]× on the curve
G = {(x, y) ∈R2 : |xy| = 1}, a union of two hyperbolas. We know Z[
√
2]× = ±(1 +
√
2)Z
and U = θK(Z[
√
2]×) is a discrete subset of G (“equally spaced” in a multiplicative sense).
See Figure 1.
Let’s see how the subgroup U moves G around by multiplication in Figure 1. Multiplying
G by some u ∈U moves the arcs between consecutive points of U in Figure 1 to other arcs
between consecutive point, and it exchanges the hyperbolas y = 1/x and y = −1/x if
1For instance, in 1905 Minkowski [11, pp. 156–7] wrote “Es wird erz¨ahlt, da§ nach langj¨ahrigen verge-
blichen Bem¨uhungen um das schwierige Problem Dirichlet die L¨osung in Rom in der Sixtinischen Kapelle
w¨ahrend des Anh¨orens der Ostermusik ergr¨undet hat. Inwieweit dieses Faktum f¨ur die von manchen be-
hauptete Wahlverwandtschaft zwischen Mathematik und Musik spricht, wage ich nicht zu er¨ortern.” (trans-
lation: “People say that, after many years of unsuccessful eﬀorts in trying to solve this diﬃcult problem,
Dirichlet found the solution in Rome in the Sistine Chapel while listening to Easter music. I do not dare to
discuss to what extent this fact conﬁrms the conjectured (by some people) relationship between mathematics
and music.”)
2The Euclidean embedding of K, as deﬁned here, depends on the ordering of the diﬀerent real and complex
embeddings as well as on the choice of one complex embedding from each conjugate pair. A coordinate-free
way of deﬁning the Euclidean embedding uses tensor products: the natural mapping K →R ⊗Q K where
α 7→1 ⊗α is a ring homomorphism into a ﬁnite-dimensional real vector space of dimension n, just like V .

<!-- page 5 -->
DIRICHLET’S UNIT THEOREM
5
θ((1 +
√
2)2)
θ(1)
θ

−1
1+
√
2

θ(−(1 +
√
2))
θ(−(1 +
√
2)2) θ(−1)
θ

1
1+
√
2

θ(1 +
√
2)
s
s
s
s
s
s
s
s
Figure 1. Units in Z[
√
2] on G = {(x, y) ∈R2 : |xy| = 1}.
N(u) = −1. Multiplication by θ(−1) = (−1, −1) on G exchanges the two branches on each
hyperbola.
Modulo U each (x, y) ∈G is congruent to a point on the arc between θ(1) and θ((1+
√
2)2),
so the map [1, (1+
√
2)2] →G/U given by x 7→(x, 1/x)U is surjective and continuous, which
implies G/U is compact.
In Example 3.1 we used knowledge of the unit group of Z[
√
2] to see G/U is compact.
The key to proving the unit theorem is showing the compactness of G/U without knowing
the structure of the unit group in advance.
Lemma 3.2. For nonzero a in O, [O : (a)] = |NK/Q(a)|.
Proof. This follows from O being a free Z-module of rank [K : Q].
□
Lemma 3.3. For each positive integer N, ﬁnitely many a ∈O satisfy |NK/Q(a)| = N up
to multiplication by O×. That is, there are a1, . . . , ak ∈O, where k depends on N, such
that |NK/Q(ai)| = N and each a ∈O satisfying |NK/Q(a)| = N is a unit multiple of an ai.
Proof. If |NK/Q(a)| = N then [O : (a)] = N by Lemma 3.2, so NO ⊂(a) ⊂O. Since O/NO
is ﬁnite, there are only ﬁnitely many principal ideals between NO and O. Let (a1), . . . , (ak)
be those ideals. Then (a) = (ai) for some i, so a and ai are unit multiples.
□
Theorem 3.4. The group G/U is compact in the quotient topology.
Proof. We will ﬁnd a compact subset S of G that represents all cosets in G/U. The con-
tinuous map S →G/U is onto and thus G/U is compact. (Usually G itself is not compact.
See Figure 1.)
We begin with a remark about volumes. For v ∈V ×, multiplication of V = Rr1 × Cr2
by v is an R-linear map (hence continuous) given by a matrix with determinant N(v), so
for a region R ⊂V with ﬁnite volume, the volume of vR is |N(v)| times the volume of R.

<!-- page 6 -->
6
KEITH CONRAD
In particular, if v ∈G then vol(vR) = vol(R) because |N(v)| = 1. When R is compact so is
vR, by continuity of multiplication.
Pick a compact, convex, centrally symmetric region C ⊂V with vol(C) > 2n vol(θK(O)),
where the “volume” of the lattice θK(O) means the volume of a fundamental domain for
this lattice as a subset of V . For instance, C could be a large ball in V centered at the
origin. For each g ∈G, gC is also compact and centrally symmetric. It is convex too,
since multiplication by g on V is an invertible linear transformation, and invertible linear
transformations send convex sets to convex sets. Using g−1 instead of g, Minkowski’s convex
body theorem applies to g−1C and the lattice O ⊂V (we identify O with θK(O)):
g−1C ∩(O −{0}) ̸= ∅.
Let a be a nonzero element of O lying in g−1C. Then |NK/Q(a)| = |N(a)| ∈|N(g−1C)| =
|N(C)|, which is a bounded subset of R since C is compact. Note |N(C)| is independent of
g. The number |NK/Q(a)| is also an integer, so |NK/Q(a)| lies in a ﬁnite set (a bounded set
of integers is ﬁnite). Combining that with Lemma 3.3, there is a ﬁnite set {a1, . . . , am} of
nonzero elements of O such that every g−1C meets some aiO× = aiU, which implies every
gU meets some a−1
i C.
We have shown the quotient group G/U is represented by G ∩Sm
i=1 a−1
i C. The union
Sm
i=1 a−1
i C is a compact subset of V , since each a−1
i C is compact, and since G is closed
in V the intersection G ∩Sm
i=1 a−1
i C is compact in G. Hence G/U has a compact set of
representatives in G, so G/U is compact in the quotient topology.
□
Now we prove the unit theorem. Recall that, by deﬁnition, G = {v ∈V : |N(v)| = 1}.
Each element of V = Rr1 × Cr2 can be written in the form (x1, . . . , xr1, zr1+1, . . . , zr1+r2).
Deﬁne the logarithmic mapping L: V × →Rr1+r2 by
L(x1, . . . , zr1+r2) := (. . . , log |xi|, . . . , 2 log |zj|, . . . ),
where the coeﬃcients 2 in this formula are related to the exponents 2 in the deﬁnition of
N. The function L is a continuous group homomorphism and, for each g ∈G, L(g) lies in
the hyperplane
H = {(y1, . . . , yr1+r2) ∈Rr1+r2 :
X
i
yi = 0}.
It is easy to see that L(G) = H, so L(G) has dimension r1 + r2 −1 over R. What we really
care about is L(U), which provides a linearized geometric picture for U (once we determine
the kernel of L|U). The basic plan is to show L(U) is a “full” lattice in the hyperplane L(G)
and the kernel of L restricted to U is ﬁnite cyclic (coming from roots of unity in U).
First we treat the kernel of L|U. As a map out on V ×, L has compact kernel:
ker L = {±1}r1 × (S1)r2.
Every root of unity in U gets sent to 0 by L. Let’s check these are the only elements of
U = O× in ker L. Since U is closed in V × (all discrete subsets are closed), the kernel of
L|U is closed and thus (as a subset of {±1}r1 × (S1)r2) is compact. Since O is discrete in
V (it’s a lattice), U is discrete in V ×, so the kernel of L|U is also discrete (a subset of a
discrete set is discrete), so ker(L|U) is compact and discrete: it is ﬁnite! A subgroup of U
with ﬁnite order can only contain roots of unity. Therefore the elements of ker(L|U) are the
roots of unity in U = O×, which form a ﬁnite cyclic group since every ﬁnite subgroup of
K× is a cyclic group. (Warning: it is false that the kernel of L as a map out of K×, not U,
is only the roots of unity in K. An element of K× that has all of its Q-conjugates lying on

<!-- page 7 -->
DIRICHLET’S UNIT THEOREM
7
the unit circle is in the kernel of L. An example in Q(i) is 3/5 + (4/5)i, or more generally
a/c + (b/c)i where (a, b, c) is a Pythagorean triple. These are not algebraic integers if they
are not ±1 or ±i, so they don’t belong to U.)
Now we look at the image L(U) in the hyperplane L(G) ⊂Rr1+r2. We have already
seen (and used) that the group U is discrete in V ×, so it is also discrete in G.
The
image of a discrete set under a continuous map need not be discrete (consider Z2 →R
by (m, n) 7→m + n
√
2), but L(U) is discrete in L(G) since there are only ﬁnitely many
elements in L(U) that lie in a bounded region of Rr1+r2. Indeed, consider the box
{(y1, . . . , yr1+r2) ∈Rr1+r2 : |yi| ≤b}.
Suppose L(u) is in this box for some u ∈U. The real embeddings3 of u have absolute
value at most eb and the complex embeddings of u have absolute value at most eb/2. That
puts an upper bound in terms of b (and n = [K : Q]) on the coeﬃcients of the polynomial
Q
σ(T −σ(u)) ∈Z[T]. The coeﬃcients have only ﬁnitely many possibilities, since there are
ﬁnitely many integers with absolute value below a given bound, so there are ﬁnitely many
such polynomials. As u is a root of such a polynomial, there are ﬁnitely many choices for
u. This shows L(U) is discrete.
Since L(U) is a discrete subgroup of L(G) ∼= Rr1+r2−1, L(U) ∼= Zr′ where r′ ≤r1+r2−1.
Since L: G →L(G) is a continuous and surjective group homomorphism, the induced map
G/U →L(G)/L(U) is also continuous and surjective where both quotient groups get the
quotient topology. From Theorem 3.4, G/U is compact so L(G)/L(U) is compact. Since
L(G) is (r1+r2−1)-dimensional over R and L(U) has Z-rank r′ ≤r1+r2−1, compactness of
L(G)/L(U) forces r′ = r1 + r2 −1: Euclidean space modulo a discrete subgroup is compact
only when the subgroup has rank equal to the dimension of the space (e.g., R2/(Z × {0})
is a non-compact inﬁnite cylinder). That proves L(U) ∼= Zr1+r2−1 and L(U) is a lattice in
the hyperplane H.
We’re now basically done. Let ε1, . . . , εr (r = r1 + r2 −1) be elements of O× whose
Euclidean embeddings in U are a Z-basis of L(U). The εi’s are multiplicatively independent,
since the L(εi)’s are Z-linearly independent. For ε ∈O×, L(ε) = m1L(ε1) + · · · + mrL(εr)
for some mi ∈Z, so L(ε) = L(εm1
1
· · · εmr
r ). Since ker(L|U) is the Euclidean image of the
roots of unity in O×, ε = ζεm1
1
· · · εmr
r
where ζ ∈µ(O). This proves the unit theorem.
The most diﬃcult part of the proof of the unit theorem is showing there are r1 + r2 −1
independent units of inﬁnite order. For instance, using the logarithmic map it was not hard
for us to show L(U) is a discrete subgroup of L(G) ∼= Rr1+r2−1, so O× ∼= U ∼= W × Zr′
where r′ ≤r1 + r2 −1 and W is the group of roots of unity in O×. Thus O× has at most
r1 + r2 −1 independent units of inﬁnite order, but this alone doesn’t tell us there are units
of inﬁnite order in O×. The place in the proof where saw there are units of inﬁnite order
(if r1 + r2 −1 > 0) is when we went from r′ ≤r1 + r2 −1 to r′ = r1 + r2 −1. This happened
two paragraphs up and relied on G/U being compact.
4. Fundamental Unit in the Rank 1 Case
As noted already in Example 2.3, an order O in number ﬁeld K has a rank 1 unit group
precisely when K is real quadratic, cubic with 1 real embedding (that is, a cubic ﬁeld that
is not totally real), or a totally complex quartic ﬁeld. In the ﬁrst two cases, the only roots
3We are identifying U = θK(O×) with O× when we speak of real embeddings of u. If we did not make
that identiﬁcation, and wrote u = θK(α), then we would speak instead of real embeddings of α, which are
the initial coordinates of u.

<!-- page 8 -->
8
KEITH CONRAD
of unity in K are ±1, which are always in O, so O× = ±εZ.4 Viewing K in R, the choice
of ε > 1 is called the fundamental unit of O.
Example 4.1. Since Z[
√
2]× = ±(1 +
√
2)Z, the fundamental unit of Z[
√
2] is 1 +
√
2.
Example 4.2. Since Z[3
√
2]× = ±(17 + 12
√
2)Z, Z[3
√
2] has fundamental unit 17 + 12
√
2.
Example 4.3. In Example 4.9 we will show Z[
3√
6]× = ±(109 + 60
3√
6 + 33
3√
36)Z, so
109 + 60
3√
6 + 33
3√
36 ≈326.990 is the fundamental unit of Z[
3√
6].
In a real quadratic ﬁeld, one way to ﬁnd the fundamental unit in an order is by brute
force: if we write a unit greater than 1 as a+b
√
d or a+b(1+
√
d)/2 with a, b ∈Z, necessarily
a ≥0 and b ≥1 (check!). This allows one to systematically search for the smallest unit
greater than 1 by sifting through pairs of integers in the ﬁrst quadrant by increasing values
of a and b. (There is a more eﬃcient method, using continued fractions.)
To give examples of fundamental unit computations in the cubic case, we will use an
inequality due to Artin [1, pp. 169–170]. Mordell [12], near the end of his review of [1] in
1962, described Artin’s inequality as a “surprise” since “one would have thought that there
was not much opportunity for new results on cubic units”.
Theorem 4.4 (Artin). Let O be an order in a cubic ﬁeld K with r1 = 1. Viewing K in
R, if v > 1 is a unit of O× then | disc(O)| < 4v3 + 24.
Proof. This argument is similar to Artin’s in [1] and is a messy calculation. Consider reading
the corollary and its applications ﬁrst, and then return to this proof.
Since v is a unit and is not ±1, v ̸∈Q. Thus Q(v) = K, so Z[v] is an order inside O.
From Z[v] ⊂O, | disc(O)| ≤| disc(Z[v])|. We will show | disc(Z[v])| < 4v3 + 24.
Let σ: K →C be one of the non-real embeddings of K. Then NK/Q(v) = vσ(v)σ(v) =
v|σ(v)|2 > 0, so v has norm 1. Let x = √v (as a positive real number), so 1 = x2|σ(v)|2.
Therefore |σ(v)| = 1/x, so in polar form σ(v) = x−1eit for some real number t. Then
disc(Z[v]) = ((σ(v) −v)(σ(v) −v)(σ(v) −σ(v)))2
= ((x−1eit −x2)(x−1e−it −x2)(x−1eit −x−1e−it))2
= ((x−2 + x4 −2x cos t)(−2ix−1 sin t))2
= −4(sin2 t)(x3 + x−3 −2 cos t)2.
Since x > 1, x3 + x−3 > 2. Set a = (x3 + x−3)/2, so a > 1 and by taking absolute values,
| disc(Z[v])| = 4(sin2 t)(2a −2 cos t)2
= 16(1 −cos2 t)(a −cos t)2.
(4.1)
Set y = cos t, so y ∈[−1, 1]. Then (4.1) is
f(y) = 16(1 −y2)(a −y)2
and we want to maximize this on [−1, 1]. Let a maximum occur at y0. Since f(y) ≥0 on
[−1, 1] with f(1) = f(−1) = 0 and f(0) = 16a2 > 0, we have y0 ∈(−1, 1) and f′(y0) = 0.
By the product rule, f′(y) = 32(a −y)(2y2 −ay −1) and the root of the linear factor
is a, with a > 1 > y0, so from f′(y0) = 0 we have 2y2
0 −ay0 −1 = 0. Rewrite this as
(4.2)
ay0 = 2y2
0 −1.
4Don’t confuse ±εZ with ε±Z; the latter is just εZ.

<!-- page 9 -->
DIRICHLET’S UNIT THEOREM
9
Thus
(4.3)
| disc(Z[v])| = f(cos t) ≤f(y0) = 16(1 −y2
0)(a −y0)2.
Expanding (a −y0)2 and using the relation (4.2) a couple of times, we get
16(1 −y2
0)(a −y0)2 = 16(a2 + 1 −y4
0 −y2
0).
Substituting a = (x3 + x−3)/2 into this,
f(y0) = 16
x6
4 + 3
2 +
x−6
4
−y4
0 −y2
0

= 4x6 + 24 + 4(x−6 −4y4
0 −4y2
0)
= 4v3 + 24 + 4(x−6 −4y4
0 −4y2
0).
We will show x−6 < 4y2
0, so f(y0) < 4v3 + 24. Then by (4.3), | disc(Z[v])| < 4v3 + 24, as
desired.
Let h(y) = 2y2−ay−1, the quadratic factor of f′(y), so h(y0) = 0. Since h(−1) = 1+a > 0
and h(0) = −1 < 0, h(y) has a root in (−1, 0). And since h(1) = 1 −a < 0 and h(y) > 0
for large y, h(y) also has a root in (1, ∞). Thus −1 < y0 < 0. Since x > 1, the desired
inequality x−6 < 4y2
0 is the same as y0 < −1/(2x3). The graph of h(y) is a concave up
parabola and y0 is the smaller root of h(y), so to prove y0 < −1/(2x3) it is enough to show
h(−1/(2x3)) < 0:
h
 −1
2x3

=
2
4x6 +
a
2x3 −1 =
1
2x6 +
1
2x3
x3 + x−3
2
−1 =
3
4x6 −3
4 = 3
4
 1
x6 −1

< 0
since x > 1.
□
Remark 4.5. The condition on v in Theorem 4.4 is v > 1, not v > 0. If we could use
0 < v < 1 in Artin’s inequality, then replacing v with a high power of itself would imply
| disc(O)| < 24, which is false for all cubic orders with one exception. See Footnote 8 below.
Corollary 4.6. Let O be an order in a cubic ﬁeld K with r1 = 1. Viewing K inside R, let
ε > 1 be the fundamental unit of O. For each unit u > 1 in O×, if 4u3/m + 24 ≤| disc(O)|
for an integer m ≥2 then u = εk where 1 ≤k < m. In particular, if 4u3/2 + 24 ≤| disc(O)|
then u = ε.
Proof. The group O× is ±εZ, so u = εk for some positive integer k. Artin’s inequality using
v = ε says
| disc(O)| < 4ε3 + 24 = 4u3/k + 24.
If k ≥m then | disc(O)| < 4u3/k +24 ≤4u3/m +24 ≤| disc(O)|, so we have a contradiction.
Thus k < m.
□
Example 4.7. Let K = Q(
3√
2), so OK = Z[
3√
2]5 and disc(OK) = disc(T 3 −2) = −108.
Since
1 =
3√
2
3 −1 = (
3√
2 −1)(
3√
4 +
3√
2 + 1),
we have a unit u = 1 +
3√
2 +
3√
4 ≈3.847. Since 4u3/2 + 24 ≈54.185 ≤108, u is the
fundamental unit of OK.
5See Example 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/totram.pdf.

<!-- page 10 -->
10
KEITH CONRAD
Example 4.8. Let K = Q(α), where α3 + 2α + 1 = 0. The polynomial T 3 + 2T + 1 is
irreducible modulo 3, so K/Q is cubic. Since disc(T 3 + 2T + 1) = −59, which is squarefree,
OK = Z[α]. Clearly α is a unit. Since T 3 + 2T + 1 has one real root, approximately −.45,
which we identify with α using the real embedding of K, a unit greater than 1 is
u = −1
α ≈2.205.
Since 4u3/2 + 24 ≈37.10 ≤59, u is the fundamental unit of OK.
Example 4.9. Let K = Q(
3√
6), so OK = Z[
3√
6].6 This will be an example where a unit u
we ﬁnd will satisfy 4u3/2 + 24 > | disc(OK)|, so we will have to be more careful in the way
we use Corollary 4.6 to prove u is the fundamental unit of OK.
To ﬁnd units in OK, we seek two diﬀerent descriptions of a principal ideal in OK: if
(α) = (β) then α = βu where u is a unit. Here is a table of how the ﬁrst few primes p
decompose in OK, based on how T 3 −6 mod p decomposes.
p
T 3 −6 mod p
(p)
2
T 3
p3
2
3
T 3
p3
3
5
(T −1)(T 2 + T + 1)
p5p25
7
(T −3)(T −5)(T −6)
p7p′
7p′′
7
The only ideal of norm 2 is p2. We will prove p2 is principal by ﬁnding an element of
absolute norm 2. For c ∈Z, NK/Q(
3√
6 + c) = c3 + 6. Therefore NK/Q(
3√
6 −2) = −2, so
the ideal (
3√
6 −2) has norm 2 and must be p2. We have the equality of principal ideals
(2) = p3
2 = (
3√
6 −2)3 = ((
3√
6 −2)3),
so the numbers 2 and (
3√
6 −2)3 are equal up to a unit multiple in OK. Since (
3√
6 −2)3 ≈
−.0061, to get a unit greater than 1 we use the ratio7
u = −
2
(
3√
6 −2)3 ≈326.9908.
Since disc(OK) = disc(Z[
3√
6]) = disc(T 3 −6) = −972 and 4u3/2 + 24 ≈23675.75 > 972,
we can’t use Corollary 4.6 right away to say u is the fundamental unit of OK.
Let ε > 1 be the unknown fundamental unit of Z[
3√
6]. Does u = ε? Since u > 1, the
unit theorem implies u = εk for some k ≥1 and we want to show k = 1. Artin’s inequality
with v = ε says that in R,
| disc(OK)| < 4ε3 + 24 =⇒972 < 4u3/k + 24.
For large k this inequality fails, since the left side is 972 and the right side tends to 4+24 = 28
as k →∞. More precisely, since 4u3/4 + 24 ≈331.5 < 972, k is either 1, 2, or 3. How do
we rule out u = ε2 and u = ε3 in order to know u = ε?
Here’s a great idea: to prove an algebraic integer is not a square or cube, prove it is not a
square or cube modulo p for some prime ideal p. Looking at the above table of prime ideal
factorizations, we will use the ideals p5 and p7.
In OK/p5 ∼= Z/(5) we have
3√
6 ≡1 mod p5, so u ≡2/(2 −1)3 ≡2 mod p5. The nonzero
squares in Z/(5) are 1 and 4, so u is not a square in OK/p5 and thus is not a square in OK.
6See Example 2.10 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/totram.pdf.
7Explicitly, u = 109 + 60
3√
6 + 33
3√
36, but this representation will not be needed.

<!-- page 11 -->
DIRICHLET’S UNIT THEOREM
11
In OK/p7 ∼= Z/(7) we have
3√
6 ≡3 mod p7, so u ≡2/(2 −3)3 ≡−2 ≡5 mod p7. The
nonzero cubes in Z/(7) are 1 and 6, so u is not a cube in OK. (Using p′
7 or p′′
7 would have
led to the same conclusion.)
We have shown k = 1, so u = ε is the fundamental unit of Z[
3√
6].
Example 4.10. Let K = Q(α) where α3 −α −1 = 0. The polynomial T 3 −T −1 is
irreducible mod 5, so K/Q is cubic. The polynomial has one real root α ≈1.324, so r1 = 1.
Since disc(T 3 −T −1) = −23 is squarefree, OK = Z[α]. Clearly α is a unit in OK. It is
natural to wonder if α is the fundamental unit of OK since it is so close to 1 in the real
embedding. We can’t use Artin’s inequality because | disc(OK)| < 24,8 so for every unit
u > 1 and positive integer m, | disc(OK)| < 4u3/m + 24.
Since we know O×
K/{±1} is inﬁnite cyclic, to show α is the fundamental unit we show α
is the smallest unit greater than 1: no unit u ∈Z[α]× satisﬁes 1 < u < α. Let σ: K →C be
one of the complex embeddings of K, so NK/Q(u) = uσ(u)σ(u) = u|σ(u)|2 > 0. Therefore
NK/Q(u) = 1. Since u ̸∈Q, the minimal polynomial of u over Q is T 3 + aT 2 + bT −1 for
some integers a and b. The roots are u, σ(u), and σ(u), so
a = −(u + σ(u) + σ(u)),
b = uσ(u) + uσ(u) + σ(u)σ(u).
Then
|a| ≤u + 2|σ(u)|,
|b| ≤2u|σ(u)| + |σ(u)|2.
Since 1 = u|σ(u)|2, the bound 1 ≤u implies |σ(u)| ≤1, so from 1 < u < α we get
|a| < α + 2 ≈3.3,
|b| ≤2α + 1 ≈3.6.
Thus a and b both lie in {0, ±1, ±2, ±3}. There are 49 polynomials T 3 + aT 2 + bT −1
with a and b in that set. Such a polynomial having a unit u > 1 in OK as a root must
have discriminant of the form −23m2 because disc(Z[u]) = [OK : Z[u]]2 disc(OK). There
are four such polynomials, shown in the table below, including T 3 −T −1 itself. Each of
these polynomials has one real root that turns out to be a small power of α.9
Polynomial
Discriminant
Real Root
T 3−T −1
−23
α ≈1.324
T 3 −2T 2 + T −1
−23
α2 ≈1.754
T 3 −3T 2 + 2T −1
−23
α3 ≈2.324
T 3 −2T 2 −3T −1
−23
α4 ≈3.079
Since α is the smallest root in this list, it is the fundamental unit of OK.
Example 4.11. Let K = Q(α) where α3 −α −5 = 0. The polynomial T 3 −T −5 is
irreducible mod 3, so K/Q is cubic. The polynomial has one real root α ≈1.904, so r1 = 1.
Since disc(T 3 −T −5) = −671 = −11 · 61 is squarefree, OK = Z[α]. An example of a unit
is α −2: it is a root of
(T + 2)3 −(T + 2) −5 = T 3 + 6T 2 + 11T + 1,
so NK/Q(α −2) = −1. In R, α −2 ≈−.095, so a unit greater than 1 is u := −1/(α −2) ≈
10.43. Since 4u3/2 + 24 ≈158.81 ≤671, u is the fundamental unit of OK.
8 This ﬁeld K is the only cubic ﬁeld, up to isomorphism, with absolute discriminant less than 24, so OK
is the only cubic order with absolute discriminant less than 24.
9All the polynomials in the table have discriminant −23, but this is not true for the minimal polynomials
of all powers of α, e.g., α6 has minimal polynomial T 3 −5T 2 −2T −1 with discriminant −575 = −23 · 52.

<!-- page 12 -->
12
KEITH CONRAD
Example 4.12. We will show for all a ∈Z+ that f(T) = T 3 + aT −1 is irreducible over
Q with a unique real root α and Z[α]× = ±αZ (even if Z[α] is not the integers of Q(α)).
By the rational roots theorem, a rational root of f(T) must be ±1, and f(1) = a ̸= 0
and f(−1) = −a −2 ̸= 0. Thus f(T) is cubic with no rational root, so it is irreducible over
Q. From f(0) = −1 < 0 and f(1) = a > 0, f(T) has a real root α in (0, 1). This is the
only real root, either because disc(f(T)) = −4a3 −27 < 0 or because f′(x) = 3x2 + a > 0
for x ∈R, so f is increasing on R.10
Set u = 1/α, a unit in Z[α] with u > 1, so ±αZ = ±uZ. To prove Z[α]× = ±uZ we will
try to check 4u3/2 + 24 ≤| disc(Z[α])| so we can apply Corollary 4.6:
(4.4) 4u3/2 + 24 ≤| disc(Z[α])| ⇐⇒4
 1
α
3/2
+ 24
?
≤4a3 + 27 ⇐⇒1
?
≤(a2α)3/2 + 3
4α3/2.
This inequality turns out to be true for a ≥2: 1/a−1/a4 < α < 1/a since f(1/a) = 1/a3 > 0
and f(1/a −1/a4) = −(3(a6 −a3) + 1)/a12 < 0, so
(a2α)3/2 + 3
4α3/2 > (a2α)3/2 >

a −1
a2
3/2
> 1
since x −1/x2 is increasing for x > 0. This veriﬁes (4.4), so Z[α]× = ±(1/α)Z = ±αZ.
What if a = 1? In that case, 1/α ≈1.4655, so 4(1/α)3/2 + 24 ≈31.096 > 4a3 + 27. Since
4(1/α)3/3 + 24 ≈29.862 < 4a3 + 27, we have 1/α = ε or ε2 where ε is the fundamental unit
of Z[α]. To rule out 1/α = ε2 we will show 1/α is not a square in Z[α] by showing it’s not
a square mod p for some prime ideal p in Z[α]. Since disc(f(T)) = −31 is squarefree, Z[α]
is the ring of integers of Q(α).11 From f(T) = T 3 + T −1 ≡(T −2)(T 2 + 2T + 2) mod 3,
(3) = p3p9 with α ≡2 mod p3. Thus 1/α ≡2 mod p3, which isn’t a square in Z[α]/p3 ∼= F3.
Remark 4.13. We can use the family of rings Z[α] in the previous examples to show that
in Artin’s inequality | disc(O)| < 4v3 + 24, the coeﬃcient 4 and exponent 3 are “optimal”.
Suppose we always have | disc(O)| < AvB + C for universal constants A, B, and C. Take
O = Z[α] where α is a root of T 3 + aT −1 for a ∈Z+. Then the inequality for the unit
1/α that’s bigger than 1 becomes 4a3 + 27 < A(1/α)B + C. Dividing through by 4a3,
(4.5)
1 + 27
4a3 < A
4
1
a3αB + C
4a3 = A
4
aB−3
(aα)B + C
4a3 .
When a →∞, the left side of (4.5) tends to 1. From the bounds 1/a −1/a4 < α < 1/a in
the previous example, aα →1 as a →∞,12 so the right side of (4.5) tends to 0 if B < 3, to
A/4 if B = 3, and to ∞if B > 3. Therefore B ≥3, and if B = 3 then A/4 ≥1, so A ≥4.
If Artin’s inequality were changed to | disc(O)| < 4v3 + C, must C ≥24? An example
showing C is at least above 20 is O = Z[β] where β is a root of T 3 −2T 2 −T −1:
the polynomial has discriminant −87 and β ≈2.546 is the fundamental unit of Z[β], so
C > | −87| −4β3 ≈20.92. I don’t know any larger lower bound on C.
10f(T) is irreducible when a is not 0 or −2. It has three real roots for a ≤−3. The case a = −1 was
treated in Example 4.10.
11For a ≥2, the ring of integers of Q(α) is Z[α] when 4a3 + 27 is squarefree, but also many times when
4a3 + 27 is not squarefree: a = 3, 6, 12, 15, 21, 24, 30, 39, . . ..
12With a bit more care, the upper bound on α can be reduced from 1/a to 1/a −(1/2)/a4 when a ≥2.

<!-- page 13 -->
DIRICHLET’S UNIT THEOREM
13
We now consider rank 1 unit groups in two totally complex quartic ﬁelds: Q(ζ12) and
Q(ζ5). Each ﬁeld has a real quadratic subﬁeld (the ﬁxed ﬁeld of complex conjugation) and
norms down to that subﬁeld will help us determine a fundamental unit in the quartic ﬁeld.
Example 4.14. Let K = Q(ζ12) = Q(ζ3, ζ4) = Q(√−3, i) = Q(
√
3, i).
It has three
quadratic subﬁelds, as shown in the diagram below. In particular, K has the real quadratic
subﬁeld Q(
√
3), which has unit rank 1 with fundamental unit 2 +
√
3.
Q(ζ12)
Q(√−3)
Q(
√
3)
Q(i)
Q
Since complex conjugation on Q(ζ12) is an automorphism with order 2, Q(ζ12) has degree
2 over the ﬁxed ﬁeld of complex conjugation. That ﬁxed ﬁeld has to be Q(
√
3), either
because Q(√−3) and Q(i) are not ﬁxed by complex conjugation or because (using ζ12 =
e2πi/12) we have ζ12 + ζ−1
12 = 2 cos(2π/12) = 2 cos(π/6) =
√
3.
For each u ∈O×
K, u is also in O×
K, so uu ∈O×
K ∩R = O×
K ∩Q(
√
3) = Z[
√
3]×. Conversely,
if t ∈OK then tt ∈Z[
√
3], so if tt ∈Z[
√
3]× with inverse α ∈Z[
√
3], then t ∈O×
K because
t(tα) = 1 in OK.
In particular, ζ12 −1 is a unit in OK because
(ζ12 −1)(ζ12 −1) = (ζ12 −1)(ζ−1
12 −1) = 1 −(ζ12 + ζ−1
12 ) + 1 = 2 −(ζ12 + ζ−1
12 ) = 2 −
√
3,
which is a unit in Z[
√
3].
Setting u = ζ12 −1, we’ll show u is a fundamental unit of K. The roots of unity of K
are the powers of ζ12, and the unit theorem tells us there is a fundamental unit v in K, so
u = ζj
12vk for some integers j and k. Taking complex conjugates of both sides, u = ζ−j
12 vk,
so
2 −
√
3 = uu = (vv)k.
The product vv is a positive unit in Q(
√
3), and 2 −
√
3 = 1/(2 +
√
3) is a generator of the
positive units of Q(
√
3), so vv = (2 −
√
3)ℓfor some ℓ∈Z. Thus 2 −
√
3 = (2 −
√
3)kℓ, so
k = ±1. Therefore u is ζj
12v or ζj
12v−1, so u is a fundamental unit of K.
Example 4.15. Let K = Q(ζ5). It is cyclic over Q with one quadratic subﬁeld, Q(
√
5).
Q(ζ5)
Q(
√
5)
Q
A fundamental unit of Q(
√
5) is u = (1 +
√
5)/2. We will show u is also a fundamental
unit of K. The roots of unity in K are the 10th roots of unity: powers of −ζ5. Let v be

<!-- page 14 -->
14
KEITH CONRAD
a fundamental unit of K, so u = (−ζ5)jvk for some j, k ∈Z. Taking complex conjugates
of both sides, u = (−ζ5)−jvk since u is real, so u2 = (vv)k. Since vv is a positive unit in
Q(
√
5), vv = uℓfor some ℓ∈Z, so u2 = (uℓ)k = ukℓ, so kℓ= 2. Thus k is ±1 or ±2. If
k = ±1 then u is a fundamental unit of K. We will show k ̸= ±2.
Suppose k = ±2, so u = (−ζ5)jv2. That means u(−ζ5)−j is a square in OK, so it is also
a square in the residue ﬁelds OK/p for all prime ideals p. We’ll get a contradiction by using
p = (1 −ζ5), which is the unique prime in OK that lies over 5. In OK/(ζ5 −1) we have
ζ5 ≡1 and 5 ≡0, so u(−ζ5)−j ≡±u and u = (1 +
√
5)/2 ≡3. The ﬁeld OK/(ζ5 −1) has
order 5, so it is (uniquely) isomorphic to Z/5Z and ±3 are not squares in Z/5Z. Thus u is
not a square in OK/(ζ5−1), so u can’t be a square in OK. We have reached a contradiction.
Remark 4.16. Not all totally complex quartic ﬁelds can be treated like in the previous
two examples since some totally complex quartic ﬁelds have no (real) quadratic subﬁeld.
An example is K = Q(α) where α4 + 8α + 12. The polynomial T 4 + 8T + 12 is irreducible
over Q with no real roots and its Galois group over Q is isomorphic to A4. A quadratic
subﬁeld of K would correspond by Galois theory to an index-2 subgroup of A4, and A4 has
no such subgroup. Using a computer, a fundamental unit of K is 1
2α3 + α2 −1.
5. The regulator and some rank 2 unit groups
For an order O in a totally real cubic ﬁeld K, the rank of O× is 2 and the roots of unity
in K are ±1, so O× = ±εZ
1 εZ
2 , where ε1 and ε2 are multiplicatively independent (Example
2.4). We will address two topics in this section:
• how to show units in O are multiplicatively independent,
• how to show two independent units in O generate O×/{±1}.
Both of these will use an important numerical invariant of O× called its regulator.
Let σ1, σ2, σ3 be the diﬀerent real embeddings of K. From the proof of the unit theorem,
the mapping O× →R3 where
(5.1)
u →(log |σ1(u)|, log |σ2(u)|, log |σ3(u)|)
has kernel ±1 and image of rank 2 in the hyperplane H = {(x, y, z) ∈R3 : x + y + z = 0}.
Theorem 5.1. Multiplicative independence of u and v in O× is equivalent to R-linear
independence of (log |σ1(u)|, log |σ2(u)|, log |σ3(u)|) and (log |σ1(v)|, log |σ2(v)|, log |σ3(v)|).
Proof. We will prove multiplicative dependence in O× is equivalent to linear dependence of
the corresponding vectors in R3.
Set u = (log |σ1(u)|, log |σ2(u)|, log |σ3(u)|) and v = (log |σ1(v)|, log |σ2(v)|, log |σ3(v)|).
If u or v is ±1 then u or v is 0, so we have multiplicative dependence of units and linear
dependence of vectors. Now we may assume u and v are not ±1.
If u and v are multiplicatively dependent, then uavb = 1 for integers a and b that are
not both 0.
Feeding both sides of the equation into (5.1), we get the Z-linear relation
au + bv = 0, so u and v are R-linearly dependent.
Now assume u and v are R-linearly dependent. Since neither vector is 0, v = cu for
some c ∈R×. We will show c is in fact rational. Then c = m/n for nonzero integers m and
n, which means nv = mu, so um = ±vn and thus u2mv−2n = 1: u and v are multiplicatively
dependent. The rationality of c is subtle: R-linear dependence of vectors does not normally
imply Q-linear dependence. What makes this happen for u and v is that the image of O×
in H is a discrete subgroup and this image contains u and v.

<!-- page 15 -->
DIRICHLET’S UNIT THEOREM
15
Since the image of O× in the hyperplane H is a discrete subgroup, Zu + Zv is a discrete
subgroup of H (subgroups of discrete groups are discrete). Writing v as cu,
Zu + Zv = Zu + Zcu = (Z + Zc)u.
This is a subgroup of the linear subspace Ru in H. A diﬀerence between rational and
irrational c is that Z + Zc is discrete in R when c ∈Q and it is dense in R if c ̸∈Q.
(Explicitly, if c = m/n then Z + Zc = 1
n(Zn + Zm) = Z(d/n) where d = gcd(m, n).) So if c
is irrational, (Z + Zc)u has inﬁnitely many elements on the segment from 0 to u, and that
contradicts the discreteness of (Z + Zc)u in H. Hence c is rational and we’re done.
□
Example 5.2. Let α be a root of T 3 −3T −1, so α+1 is a root of (T −1)3 −3(T −1)−1 =
T 3 −3T 2 + 1: they are both units in Z[α]. We met these units in Example 2.6. The real
roots of T 3 −3T −1 are approximately −1.532, −.3472, and 1.879. That makes the vectors
in R3 associated to α and α + 1 approximately
(log(1.532), log(.3472), log(1.879)) ≈(.42, −1.05, .63)
and
(log(.532), log(.6527), log(2.879)) ≈(−.63, −.42, 1.05).
These vectors are linearly independent just from comparing the signs of the coordinates in
each vector. Therefore α and α + 1 are multiplicatively independent units.
The linear independence of two vectors (x, y, z) and (x′, y′, z′) in R3 is equivalent to the
nonvanishing of the determinant of some 2 × 2 submatrix of
(5.2)

x
y
z
x′
y′
z′

.
When the two rows lie in the hyperplane of vectors in R3 with coordinate sum 0, all three
2 × 2 determinants in (5.2) are equal up to sign. For example,
xz′ −zx′ = x(−x′ −y′) + (x + y)x′ = −xy′ + yx′ = −(xy′ −yx′).
Similarly, yz′ −zy′ = xy′ −yx′. Therefore the absolute value of the determinants of all the
2 × 2 submatrices in (5.2) are equal.
Deﬁnition 5.3. The regulator of two units u and v in O is the absolute value of any 2 × 2
determinant in (5.2) where the rows are the vectors associated u and v. This number is
denoted Reg(u, v).
The value of Reg(u, v) is independent of the ordering of the units since we are using
the absolute value of determinants. In terms of regulators, Theorem 5.1 says u and v are
multiplicatively independent if and only if Reg(u, v) ̸= 0.
Remark 5.4. The two rows in (5.2) span a parallelogram in H with area
√
3|xy′ −yx′|.
That gives Reg(u, v) a geometric meaning: it’s the area of the parallelogram spanned by
the vectors in H associated to u and v, up to the scaling factor
√
3.
Example 5.5. Let α be a root of T 3 −3T −1. By Example 2.6, α and α + 1 are units
in Z[α]. Writing the real roots of T 3 −3T −1 as σ1(α) ≈−1.532, σ2(α) ≈−.3472, and
σ3(α) ≈1.879,
Reg(α, α + 1) =
det

log |σ1(α)|
log |σ2(α)|
log |σ1(α) + 1|
log |σ2(α) + 1|
 ≈.8492 ̸= 0.
This is a second proof (after Example 5.2) that α and α + 1 are independent units.

<!-- page 16 -->
16
KEITH CONRAD
We have shown how to decide if two units in O are multiplicatively independent. Now
we develop a method of deciding if a pair of independent units in O× is fundamental.
Theorem 5.6. Let O be an order in a totally real cubic ﬁeld and ε1 and ε2 be fundamental
units of O. For a pair of units u1 and u2 in O×, write u1 = ±εa
1εb
2 and u2 = ±εc
1εd
2 for some
choice of signs. Then Reg(u1, u2) = |ad −bc| Reg(ε1, ε2), and if u1 and u2 are independent
units then |ad −bc| = [O× : ⟨−1, u1, u2⟩].
Proof. Let v1 = (x, y, z) and v2 = (x′, y′, z′) be the vectors in H associated to ε1 and
ε2, and u1 and u2 be the vectors in H associated to u1 and u2, so u1 = av1 + bv2 and
u2 = cv1 + dv2 in R3. Then we have an equation of 2 × 3 matrices:

u1
u2

=

av1 + bv2
cv1 + dv2

=

ax + bx′
ay + by′
az + bz′
cx + dx′
cy + dy′
cz + dz′

The ﬁrst 2 × 2 determinant is (ad −bc)(xy′ −x′y), so Reg(u1, u2) = |ad −bc| Reg(ε1, ε2).
To show |ad −bc| = [O× : ⟨−1, u1, u2⟩], we will compare quotient groups O×/⟨−1, u1, u2⟩
and (Zv1+Zv2)/(Zu1+Zu2). The homomorphism (5.1) gives an isomorphism O×/{±1} →
Zv1 + Zv2 that identiﬁes the subgroup ⟨−1, u1, u2⟩/{±1} with Zu1 + Zu2. Therefore we
have a group isomorphism
(O×/{±1})/(⟨−1, u1, u2⟩/{±1}) ∼= (Zv1 + Zv2)/(Zu1 + Zu2).
The index [Zv1 + Zv2 : Zu1 + Zu2] is the absolute value of the determinant of the matrix
expressing u1 and u2 in terms of v1 and v2.13 Therefore from
 u1
u2

= ( a b
c d )
 v1
v2

, the index
is |ab −bc|, so
|ad −bc| = [O×/{±1} : ⟨−1, u1, u2⟩/{±1}] = [O× : ⟨−1, u1, u2⟩].
□
Rewriting the conclusion of Theorem 5.6 as Reg(u1, u2) = [O× : ⟨−1, u1, u2⟩] Reg(ε1, ε2)
makes it resemble the discriminant-index formula disc(A) = [OK : A]2 disc(OK) where
A is an order in OK.
While discriminants are integers, regulators are expected to be
transcendental (when they are nonzero).
That doesn’t prevent their ratios from being
integers.
Corollary 5.7. In the notation of Theorem 5.6, all pairs of fundamental units in O have
the same regulator.
Proof. For fundamental units {u1, u2}, |ad −bc| = 1, so Reg(u1, u2) = Reg(ε1, ε2).
□
This corollary is analogous to all Z-bases of O having the same discriminant, which is
therefore called the discriminant of O. For similar reasons, we can now deﬁne Reg(O) to be
the regulator of any pair of fundamental units of O. Also we set Reg(K) to be Reg(OK),
just as disc(K) is deﬁned to be disc(OK).
For a pair of independent units u1 and u2 in O to be fundamental units means the index
[O× : ⟨−1, u1, u2⟩] is 1, or equivalently Reg(u1, u2)/ Reg(ε1, ε2) = 1. Since that regulator
ratio is in Z+, it is 1 as soon as we know it is less than 2:
O× = ⟨−1, u1, u2⟩⇐⇒Reg(u1, u2)
Reg(ε1, ε2) < 2.
Using the inequality on the right to prove u1 and u2 are fundamental units might seem
hopeless if we don’t already know a pair of fundamental units ε1 and ε2. To make that
13See Theorem 5.19 in https://kconrad.math.uconn.edu/blurbs/linmultialg/modulesoverPID.pdf.

<!-- page 17 -->
DIRICHLET’S UNIT THEOREM
17
inequality practical, we want an upper bound on the regulator ratio by using a lower bound
on Reg(ε1, ε2) that doesn’t use fundamental units. Here is such a lower bound, due to
Cusick [3, Theorem 1]. You might want to skip the proof ﬁrst and read later examples.
Theorem 5.8. Let K be a totally real cubic ﬁeld. If an order O in K has discriminant D
and regulator R, then
R ≥1
16(log(D/4))2.
Proof. There are 3 real embeddings of K. Identify K with one of them, so K ⊂R. Write
the other two real embeddings of K as α 7→α′ and α 7→α′′. Pick a unit u ∈O× with
u ̸= ±1. Label the Q-conjugates u, u′, u′′ as u0, u1, u2 so that |u0| ≥|u1| ≥|u2| .
Since u ∈O× −{±1} we have u ̸∈Q, so Z[u] has ﬁnite index in O and
(5.3)
disc(Z[u]) = [O : Z[u]]2 disc(O) = [O : Z[u]]2D ≥D.
Since disc(Z[u]) equals the discriminant of the minimal polynomial of u over Q,
(5.4) disc(Z[u]) = (u −u′)2(u −u′′)2(u′ −u′′)2 =

1 −u1
u0
2 
1 −u2
u0
2 
1 −u2
u1
2
u4
0u2
1,
where |u1/u0| ≤1 and |u2/u1| ≤1 by our convention on the ordering of |u0|, |u1|, and |u2|.
Set v = u1/u0 and w = u2/u1, so disc(Z[u]) = (1 −v)2(1 −vw)2(1 −w)2u4
0u2
1. From |v| ≤1
and |w| ≤1, 0 ≤(1 −v)(1 −w)(1 −vw) ≤2 by calculus. Feeding this and (5.4) into (5.3),
0 < D ≤disc(Z[u]) ≤4u4
0u2
1.
Dividing through by 4 and taking absolute values and then logarithms,
log
D
4

≤4 log |u0| + 2 log |u1|.
Set y0 = log |u0|, y1 = log |u1|, y2 = log |u2| , so y0 ≥y1 ≥y2 and y0+y1+y2 = 0. Therefore
log
D
4

≤4y0 + 2y1
= 2(2y0 + y1) = 2(−y1 −2y2)
= 2(λy0 + (λ −1)y1 + (λ −2)y2) for all λ
≤2
p
λ2 + (λ −1)2 + (λ −2)2
q
y2
0 + y2
1 + y2
2 by Cauchy−Schwarz
= 2
p
3λ2 −6λ + 5
q
y2
0 + y2
1 + y2
2
= 2
p
3λ2 −6λ + 5
p
(log |u0|)2 + (log |u1|)2 + (log |u2|)2
= 2
p
3λ2 −6λ + 5
p
(log |u|)2 + (log |u′|)2 + (log |u′′|)2.
The second square root doesn’t depend on λ, so to optimize this inequality use the minimal
value of 3λ2 −6λ + 5, which is 2 (at λ = 1):
(5.5)
log
D
4

≤2
√
2
p
(log |u|)2 + (log |u′|)2 + (log |u′′|)2.
Let ε1 and ε2 be a pair of fundamental units of O. We will express the right side of (5.5)
in terms of these units and then bound it above using R = Reg(ε1, ε2).

<!-- page 18 -->
18
KEITH CONRAD
Since |uu′u′′| = 1, on the right side of (5.5)
(log |u|)2 + (log |u′|)2 + (log |u′′|)2 = (log |u|)2 + (log |u′|)2 + (log |u| + log |u′|)2
= 2(log |u|)2 + 2(log |u|)(log |u′|) + 2(log |u′|)2.
(5.6)
We can write u = ±εx
1εy
2 for some integers x and y that are not both 0. For another real
embedding of K, u′ = ±(ε′
1)x(ε′
2)y with the same exponents. Set L1 = log |ε1|, L2 = log |ε2|,
M1 = log |ε′
1|, and M2 = log |ε′
2|, so log |u| = xL1 + yL2 and log |u′| = xM1 + yM2. In (5.6)
some algebra shows
2(log |u|)2 + 2(log |u|)(log |u′|) + 2(log |u′|)2 = Ax2 + 2Bxy + Cy2,
where A = 2(L2
1 + L1M1 + M2
1 ), B = 2L1L2 + L1M2 + L2M1 + 2M1M2, and C = 2(L2
2 +
L2M2 + M2
2 ), so (5.5) becomes
(5.7)
log
D
4

≤2
√
2
p
Ax2 + 2Bxy + Cy2.
The values of Ax2 + 2Bxy + Cy2 for (x, y) ∈Z2 −{(0, 0)} are positive. In fact these values
for (x, y) ∈R2 −{(0, 0)} are all positive since the discriminant (2B)2 −4AC = 4(B2 −AC)
is negative: check by tedious algebra that AC −B2 = 3(L1M2 −L2M1)2, and L1M2 −L2M1
is nonzero since L1M2 −L2M1 =
 L1 M1
L2 M2
 =

log |ε1| log |ε′
1|
log |ε2| log |ε′
2|
 = ±R ̸= 0, so AC −B2 > 0.
We derived (5.7) for all integers x and y that are not both 0. Since AC −B2 > 0, it can
be shown (see Theorem A.1) that for some x, y ∈Z that are not both 0, Ax2 +Bxy+Cy2 ≤
p
(4/3)(AC −B2) =
p
(4/3)(3R2) = 2R. Using that x and y in (5.7),
log
D
4

≤2
√
2
√
2R = 4
√
R,
so R ≥(1/16)(log(D/4))2.
□
Corollary 5.9. Let K be a totally real cubic ﬁeld and O be an order in K with discriminant
D and regulator R. If u1 and u2 are independent units in O such that
16 Reg(u1, u2)
(log(D/4))2
< m
then [O× : ⟨−1, u1, u2⟩] < m. In particular, if 16 Reg(u1, u2)/(log(D/4))2 < 2 then u1 and
u2 are fundamental units of O.
This is an analogue of Corollary 4.6 for totally real cubic ﬁelds.
Proof. We can bound the index [O× : ⟨−1, u1, u2⟩] above by m:
[O× : ⟨−1, u1, u2⟩] = Reg(u1, u2)
R
≤
Reg(u1, u2)
(log(D/4))2/16 < m.
□
Example 5.10. Let K = Q(α) where α3 −3α −1 = 0. Setting O = OK in Corollary 5.9,
16 Reg(α, α + 1)
(log(D/4))2
≈
16(.8492)
(log(81/4))2 ≈1.5 < 2
by Examples 2.6 and 5.5, so α and α + 1 are fundamental units of OK. A second pair
of fundamental units is {−α, −(α + 1)} = {β, β −1}, where β = −α, which is a root of
T 3 −3T + 1.

<!-- page 19 -->
DIRICHLET’S UNIT THEOREM
19
Example 5.11. Let K = Q(α), where α3 −4α −1 = 0. The polynomial T 3 −4T −1 has
discriminant 229, a prime, so OK = Z[α]. There are three real roots of the polynomial, so
O×
K has rank 2. Obviously α is a unit in OK. Another unit is α + 2, since it is a root of
(T −2)3 −4(T −2) −1 = T 3 −6T 2 + 8T −1.
We’ll show α and α + 2 are fundamental units of OK.
The real roots of T 3 −4T −1 are σ1(α) ≈−1.8608, σ2(α) ≈−.2541, and σ3(α) ≈2.1149,
so
Reg(α, α + 2) =
det

log |σ1(α)|
log |σ2(α)|
log |σ1(α) + 2|
log |σ2(α) + 2|
 ≈2.3554 ̸= 0.
Since disc(OK) = 229, we have
16 Reg(α, α + 2)
(log(D/4))2
≈2.3 < 3,
so [O×
K : ⟨−1, α, α + 2⟩] ≤2. We’ll show by contradiction the index is not 2, so it is 1.
Let’s look at O×
K/{±1} ∼= Z2 and its subgroup ⟨±α, ±(α + 2)⟩/{±1} of index at most 2.
The subgroups of Z2 with index 2 lie between Z2 and (2Z)2. Since Z2/(2Z)2 ∼= (Z/2Z)2
has three subgroups of index 2, there are three subgroups of Z2 with index 2: ⟨(2, 0), (0, 1)⟩,
⟨(0, 2), (1, 0)⟩, and ⟨(1, 1), (2, 0)⟩= ⟨(1, 1), (0, 2)⟩. Using the basis {(1, 0), (0, 1)} of Z2, each
subgroup of index 2 in Z2 has the double of (1, 0) or (0, 1) as a member of some basis.
Translating this into O×
K/{±1}, if its subgroup U := ⟨±α, ±(α + 2)⟩/{±1} has index 2
then the square of some fundamental unit of OK is a member of some (multiplicative) basis
of U. Which elements of U can be in a basis of U, and can it be a square in O×
K?
In Z2, the vectors
 a
b

that can be part of a basis must be primitive (have relatively prime
coordinates). Therefore an element of U that is part of a (multiplicative) basis of U must
be ±αa(α + 2)b where gcd(a, b) = 1. Thus a or b must be odd, so if ±αa(α + 2)b is a square
in O×
K then ±α or ±(α + 2) or ±α(α + 2) is a square in O×
K (corresponding to odd a and
even b, even a and odd b, and odd a and b, respectively). We’re going to show none of those
three units is a square in O×
K by ﬁnding prime ideals p in OK such that those three units
are not squares mod p. To handle the ambiguity of the ± signs, we’ll use p whose norm is
1 mod 4 which makes −1 a square mod p.
Since OK = Z[α] ∼= Z[T]/(T 3 −4T −1), we’ll factor p = 5, 13, 17, . . . to ﬁnd suitable p.
From Table 3 below, there is a prime p13 of norm 13 and p29 of norm 29, with α ≡5 mod p13
and α ≡16 mod p29.
p
T 3 −4T −1 mod p
(p)
5
irred.
(5)
13
(T −5)(T 2 + 5T + 8)
p13p169
17
irred.
(17)
29
(T −16)(T 2 + 16T + 20)
p29p292
Table 3. Factoring primes in OK.
In OK/p13 ∼= Z/13Z, α ≡5 and α + 2 ≡7. Since 5 and 7 are not squares in Z/13Z
while −1 is, neither ±α nor ±(α + 2) are squares in O×
K. Since 5 · 7 = 35 ≡9 mod 13 is a
square, this doesn’t show ±α(α+2) isn’t a unit square. To show that, we use the prime p29:

<!-- page 20 -->
20
KEITH CONRAD
±α(α + 2) ≡±16(18) ≡±(4 · 3)2 · 2 mod p29. In Z/29Z, ±2 are not squares, so ±α(α + 2)
is not a square in O×
K.
We have proved the index [O×
K/{±1} : U], which is at most 2, is not 2 and thus it is 1.
Therefore O×
K/{±1} = U, so α and α + 2 are fundamental units of OK.
Our next theorem gives us an inﬁnite family of examples of fundamental units in totally
real cubic orders.
Theorem 5.12. Fix an integer a. The polynomial fa(T) = T 3 −aT 2 −(a + 3)T −1 is
irreducible over Q, and if α is a root of fa(T) then Z[α]× = ±αZ(α + 1)Z.
The ﬁelds Q(α) where fa(α) = 0 are called the “simplest cubic ﬁelds” (terminology of
Dan Shanks [13]). The ring Z[α] is often, but not always, the ring of integers of Q(α).14
Theorem 5.12 is due to Thomas [15, Theorem 3.10] (a special case was pointed out earlier
by Shanks [13, p. 1138]) by methods diﬀerent from our approach based on Corollary 5.9.
Proof. By the rational roots theorem, a root of fa(T) in Q must be ±1 and neither is a
root: fa(1) = −2a −3 ̸= 0 and fa(−1) = 1 ̸= 0. Thus fa(T) is cubic with no root in Q, so
it is irreducible.
Let Ka = Q(α), where f(α) = 0. Clearly α is a unit in Z[α]. Since α + 1 is a root of
fa(T −1) = T 3 −(a + 3)T 2 + aT + 1,
α + 1 is also a unit in Z[α]. Check that disc(fa) = (a2 + 3a + 9)2 , a perfect square, so
Ka/Q is Galois. The roots of fa(T) are α, −1/(α+1), and −1/(−1/(α+1)+1) = −1−1/α,
which are all in Z[α] even if this is not the full ring of integers of Ka.
Step 1: The units α and α + 1 are multiplicatively independent.
We have
Reg(α, α + 1) = det

log |α|
log | −1/(α + 1)|
log |α + 1|
log | −1/(α + 1) + 1|

= det

log |α|
−log |α + 1|
log |α + 1|
log |α/(α + 1)|

= (log |α|)2 −(log |α|)(log |α + 1|) + (log |α + 1|)2.
(5.8)
For real x and y, x2 −xy + y2 > 0 unless x = y = 0. So from log |α| ̸= 0, Reg(α, α + 1) ̸= 0.
Step 2: Z[α] is invariant under Gal(Ka/Q).
Let σ ∈Gal(Ka/Q) be determined by σ(α) = −1/(α + 1) ∈Z[α], so Gal(Ka/Q) =
{1, σ, σ2} and σ(Z[α]) ⊂Z[α]. Applying σ to this containment twice, Z[α] ⊂σ(σ(Z[α])) ⊂
σ(Z[α]). Therefore σ(Z[α]) = Z[α], and also σ2(Z[α]) = Z[α].
Step 3: The group ⟨−1, α, α + 1⟩is invariant under Gal(Ka/Q).
It suﬃces to show this group is preserved by the automorphism σ from Step 2:
σ⟨−1, α, α + 1⟩=

−1, −
1
α + 1, −
1
α + 1 + 1

=

−1, α + 1,
α
α + 1

= ⟨−1, α, α + 1⟩.
Step 4: Reduce to the case a ≥−1.
Check f−a−3(T) = −fa(−T −1), so Ka = K−a−3. One root of f−a−3(T) is β := −α−1 =
−(α + 1), and β + 1 = −α. Therefore Z[β] = Z[α] and
⟨−1, β, β + 1⟩= ⟨−1, −(α + 1), −α⟩= ⟨−1, α, α + 1⟩,
14For 0 ≤a ≤10, the ring of integers of Q(α) is Z[α] except when a = 3 and 5.

<!-- page 21 -->
DIRICHLET’S UNIT THEOREM
21
so if we prove the theorem for an integer a then it is also true with −a −3 in place of a.
The involution a ↔−a −3 on R ﬁxes −3/2 and exchanges integers greater than and less
than −3/2 = −1.5, so we may assume a ≥−1.
Step 5: Prove the theorem when a ≥−1.
First we’ll treat a = −1. Then disc(Z[α]) = 49 and Reg(α, α + 1) ≈.5254 by Step 1, so
16 Reg(α, α + 1)
(log(disc(Z[α])/4))2 ≈
16(.5254)
(log(49/4))2 ≈1.3 < 2,
so α and α + 1 are fundamental units of Z[α] by Corollary 5.9.
We may now assume a ≥0.
The roots of fa(T) are in the disjoint intervals (−2, −1), (−1, 0), and (a + 1, a + 2) when
a ≥0 since fa has opposite signs at the endpoints: fa(−2) = −(2a+3) < 0, fa(−1) = 1 > 0,
fa(0) = −1 < 0, fa(a + 1) = −(2a + 3) < 0, and fa(a + 2) = a2 + 3a + 1 = (a + 1)2 + a > 0
(that last inequality would be incorrect for a = −1).
By Steps 2 and 3 we can let α be the largest real root of fa(T), so a + 1 < α < a + 2.
Using the regulator formula (5.8) in Step 1,
16 Reg(α, α + 1)
(log(disc(Z[α])/4))2 =
16 Reg(α, α + 1)
(log((a2 + 3a + 9)2/22))2
= 16((log |α|)2 −log |α| log |α + 1| + (log |α + 1|)2)
4(log((a2 + 3a + 9)/2))2
= 4((log α)(log α −log(α + 1)) + (log(α + 1))2)
(log((a2 + 3a + 9)/2))2
.
Since log α < log(α + 1) and α < a + 2 (all roots of fa(T) are less than a + 2),
(5.9)
16 Reg(α, α + 1)
(log(disc(Z[α])/4))2 <
4(log(α + 1))2
(log((a2 + 3a + 9)/2))2 <
4(log(a + 3))2
(log((a2 + 3a + 9)/2))2 .
For large a the right side of (5.9) is asymptotic to 4(log a)2/(log(a2))2 = 4(log a)2/4(log a)2 =
1, so it is less than 2 for large a. That proves the theorem for large a by Corollary 5.9. We
will now check more carefully that the right side of (5.9) is less than 2 for all a ≥0.
Since
4(log(a + 3))2
(log((a2 + 3a + 9)/2))2 < 2 ⇐⇒
log(a + 3)
log((a2 + 3a + 9)/2) <
1
√
2
⇐⇒a2 + 3a + 9
2
> (a + 3)
√
2,
we consider where F(x) := (x2 + 3x + 9)/2 −(x + 3)
√
2 is positive. Its graph looks positive
and increasing for x ≥2.5. Numerically, F(3) = 13.5 −6
√
2 ≈.897 > 0. With calculus we’ll
show F(x) is increasing for x ≥3, so F(x) > 0 for all x ≥3:
F ′(x) = x + 3
2 −
√
2(x + 3)
√
2−1
= x
2 + x + 3
2
−
√
2(x + 3)
√
2−1
= x
2 + (x + 3)
√
2−1
 
(x + 3)2−
√
2
2
−
√
2
!
,

<!-- page 22 -->
22
KEITH CONRAD
which is positive for x ≥3 if (1/2)(x + 3)2−
√
2 −
√
2 > 0, which is equivalent to x >
(2
√
2)1/(2−
√
2) −3 ≈2.899, so F ′(x) > 0 for x ≥3. We have proved the theorem for a ≥3.
For a = 0, 1, and 2, we return to (5.9) and focus on the middle term to show
(5.10)
4(log(α + 1))2
(log((a2 + 3a + 9)/2))2 < 2.
where α is the largest root of fa(T). By Table 4 below, (5.10) holds for a = 0, 1, and 2.
a
α
Ratio
0
1.879
1.97
1
2.651
1.91
2
3.507
1.78
Table 4. Left side of (5.10) for a = 0, 1, 2.
That completes the proof of the theorem.
□
Example 5.13. Let a = −1: α is a root of T 3 + T 2 −2T −1. The roots are 2 cos(2π/7) ≈
1.2469, 2 cos(4π/7) ≈−.4450, and 2 cos(6π/7) ≈−1.8019. Call one root α. The other roots
are −1/(α + 1) = α2 −2 and −α2 −α + 1 (the roots sum to −1). The product of the roots
is 1, so α(−1/(α + 1))(−α2 −α + 1) = 1. Thus −α2 −α + 1 = −α−1(α + 1). Another
unit is α −1 (root of T 3 + 4T 2 + 3T −1). To write α −1 = ±αm(α + 1)n for a choice of
sign and integral exponents m and n, use the logarithmic mapping L : Q(α)× →R3 where
L(γ) = (log |σ1(γ)|, log |σ2(γ)|, log |σ3(γ)|) for σ1(α) = 2 cos(2π/7), σ2(α) = 2 cos(4π/7),
and σ3(α) = 2 cos(6π/7). Using Table 5 below and a computer algebra package, L(α−1) =
L(α) −2L(α + 1), so α −1 = ±α(α + 1)−2. Since 2 cos(2π/7) > 1, using α = 2 cos(2π/7)
shows the correct sign is +: α −1 = α(α + 1)−2.
γ
L(γ) (approx.)
α
(.2207, −.8095, .5888)
α + 1
(.8095, −.5888, −.2207)
α −1
(−1.3984, .3681, 1.0303)
Table 5. Log mapping on units.
It is left to the reader to check α + 2, 2α + 1, and 4α −5 are units and to write each one
explicitly as ±αm(α + 1)n.
Cusick [3, Sect. 3] observed that the family of rings in Theorem 5.12 shows the constant
16 in the lower bound of Theorem 5.8 can’t be made smaller, as follows.
Corollary 5.14. Using the notation of Theorem 5.8, if O = Z[α] from Theorem 5.12 and
a →∞in Z+, then R/(log(D/4))2 →1/16.
Proof. Let α be the largest root of fa(T). Since a+1 < α < a+2 for a ≥0, α ∼a as a →∞.
As a →∞, check R = Reg(α, α + 1) ∼(log a)2 and (log(D/4))2 ∼4(log(a2))2 ∼16(log a)2,
so R/(log(D/4))2 ∼(log a)2/(16(log a)2) →1/16.
□
This ends our treatment of rank 2 units groups in the cubic case.15
15We do not discuss other cases where the unit rank is 2, which are (i) quartic with r1 = 2 like Q(
4√
2),
(ii) quintic with r1 = 1 like Q(
5√
2), (iii) and sextic with r1 = 0 like Q(ζ7).

<!-- page 23 -->
DIRICHLET’S UNIT THEOREM
23
For a set of units u1, . . . , ur in a number ﬁeld K (r = r1 + r2 −1), its regulator is deﬁned
in the following way. Write the real and complex embeddings of K as σ1, . . . , σr1+r2 where
for complex embeddings we include only one of each complex conjugate pair of complex
embeddings. Consider the r × (r + 1) matrix
(5.11)



N1 log |σ1(u1)|
· · ·
Nr1+r2 log |σr1+r2(u1)|
...
...
...
N1 log |σ1(ur)|
· · ·
Nr1+r2 log |σr1+r2(ur)|



where Nj = 1 if σj is a real embedding of K and Nj = 2 if σj is a complex (non-real)
embedding of K. (If K is totally real then all Nj’s are 1 and we don’t notice them.) The
purpose of including the factors Nj is that it makes the row sums all equal to 0: the ith
row sum is log |NK/Q(ui)| = log | ± 1| = 0. The matrix (5.11) does not depend on which
embedding of K from a pair of conjugate complex embeddings σ or σ is used for some σj
since |σ(α)| = |σ(α)| for α ∈K×.
Deﬁnition 5.15. The regulator Reg(u1, . . . , ur) is the absolute value of the determinant of
an r × r submatrix of (5.11).
Because all row sums equal 0, every r × r submatrix in (5.11) has the same determinant
up to sign. That makes Reg(u1, . . . , ur) independent of the ordering of the units. The only
time this deﬁnition makes no sense is when r = 0 (what’s a 0 × 0 submatrix?), which only
occurs if K is Q or imaginary quadratic. In that case the regulator is deﬁned to be 1.
Example 5.16. If K has unit rank 1 and u is a unit in K then Reg(u) = | log |u||. Note
this is unaﬀected by changing the sign of u or by replacing u with 1/u.
As in the totally real cubic case, Reg(u1, . . . , ur) ̸= 0 if and only if u1, . . . , ur are mul-
tiplicatively independent, and if we have two sets of independent units u1, . . . , ur and
v1, . . . , vr where ⟨ζ, u1, . . . , ur⟩⊂⟨ζ, v1, . . . , vr⟩for some root of unity ζ, then
Reg(u1, . . . , ur)
Reg(v1, . . . , vr) = [⟨ζ, v1, . . . , vr⟩: ⟨ζ, u1, . . . , ur⟩].
In particular, two sets of r independent units in K that generate the same group with some
roots of unity have equal regulators. That gives meaning to the next concept.
Deﬁnition 5.17. The regulator of an order O in K is the regulator of a set of fundamental
units of O and it is denoted Reg(O).
Example 5.18. The regulator of Z[
√
2] is log(1 +
√
2).
Example 5.19. By Example 4.7, Reg(Z[
3√
2]) = log(1 +
3√
2 +
3√
4).
Example 5.20. For a cubic order O with one real embedding, Artin’s inequality | disc(O)| <
4v3+24 can be rewritten as log v > (1/3) log((|D|−24))/4) where D = disc(O) and |D| > 24.
(There’s only one cubic order with |D| ≤24: see Example 4.10.) Taking for v the funda-
mental unit of O that’s greater than 1, Reg(O) = log v, so
(5.12)
Reg(O) > 1
3 log
|D| −24
4

,
which is analogous to Cusick’s lower bound R > (1/16)(log(D/4))2 in Theorem 5.8. Remark
4.13 tells us the denominator 3 in (5.12) can’t be made smaller.

<!-- page 24 -->
24
KEITH CONRAD
Example 5.21. Two units in Z[
4√
2] are 1+
√
2 and 1+
4√
2. There are two real embeddings
and one pair of complex embeddings. Using the two real embeddings,
Reg(Z[
4√
2]) =
det

log |1 +
√
2|
log |1 +
√
2|
log |1 +
4√
2|
log |1 −
4√
2|
 ≈2.158 ̸= 0,
so 1 +
√
2 and 1 +
4√
2 are multiplicatively independent. These turn out to be a pair of
fundamental units for Z[
4√
2], but we don’t discuss a proof. It was ﬁrst proved by Berwick
[2, p. 372] in 1932.
Silverman [14] proved for number ﬁelds K ̸= Q that there is a lower bound Reg(OK) >
a(log(b|DK|))r−r0, where r = r1+r2−1, r0 is the maximum unit rank of the proper subﬁelds
of K (so r0 = 0 if Q is the only proper subﬁeld of K), DK = disc(K), and a and b are
constants depending only on the degree of K over Q. The exponent r −r0 is expected to
be optimal. For cubic ﬁelds, r −r0 = r, which is consistent with the regulator lower bounds
in Example 5.20.
6. Units in a multiquadratic field
A biquadratic ﬁeld Q(√m, √n), where m, n, and mn are positive integers and not squares,
has unit rank 4 −1 = 3. There are three real quadratic subﬁelds, Q(√m), Q(√n), and
Q(√mn), and each has unit rank 1. A choice of one unit from each quadratic subﬁeld need
not be a set of 3 fundamental units for the biquadratic ﬁeld.
Example 6.1. In the ﬁeld Q(
√
2,
√
3), a system of fundamental units is 1 +
√
2,
√
2 +
√
3,
and
√
2+
√
6
2
(see Table 1).
Q(
√
2,
√
3)
Q(
√
2)
Q(
√
3)
Q(
√
6)
Q
Fundamental units for the three quadratic subﬁelds are u1 = 1 +
√
2, u2 = 2 +
√
3, and
u3 = 5 + 2
√
6. In terms of the fundamental units of Q(
√
2,
√
3), u2 =
 √
2+
√
6
2
2
and u3 =
(
√
2 +
√
3)2. In terms of the fundamental units of the quadratic subﬁelds, the fundamental
units we listed for Q(
√
2,
√
3) are u1, √u3, √u2.
Example 6.2. In the ﬁeld Q(
√
3,
√
5), a system of fundamental units is 1+
√
5
2
, 4 +
√
15,
and 3+
√
3+
√
5+
√
15
2
.
Q(
√
3,
√
5)
Q(
√
3)
Q(
√
5)
Q(
√
15)
Q

<!-- page 25 -->
DIRICHLET’S UNIT THEOREM
25
Fundamental units of the quadratic subﬁelds are u1 = 2+
√
3, u2 = 1+
√
5
2
, and u3 = 4+
√
15.
In terms of the fundamental units of Q(
√
3,
√
5), u1 = (4 +
√
15)−1 
3+
√
3+
√
5+
√
15
2
2
by
PARI. In terms of the fundamental units of the quadratic subﬁelds, the fundamental units
we listed for Q(
√
3,
√
5) are u2, u3, √u1u3.
Kuroda [9] showed that for every real biquadratic ﬁeld Q(√m, √n), with fundamental
units u1, u2, u3 for its 3 quadratic subﬁelds, a set of fundamental units for the biquadratic
ﬁeld is one of the following 7 lists up to relabeling the ui’s:
{u1, u2, u3}, {√u1, u2, u3}, {√u1u2, u2, u3}, {√u1u2u3, u2, u3},
{√u1, √u2, u3}, {√u1u2, √u3, u2}, {√u1u2, √u2u3, √u3u1}.
Examples 6.1 and 6.2 illustrate two of these possibilities and the list shows ⟨−1, u1, u2, u3⟩
has index 1, 2, 4, or 8 in the unit group of the biquadratic ﬁeld.
Consider now a general real multiquadratic ﬁeld
K = Q(
p
d1, . . . ,
p
dk),
where the di’s are nonsquare positive integers that are multiplicatively independent modulo
squares (that is, they are independent in Q×/(Q×)2). By Galois theory and induction,
[K : Q] = 2k and Gal(K/Q) ∼= (Z/2Z)k by making sign changes on every √di. The unit
rank of K is r1−1 = 2k−1, and this is also the number of quadratic subﬁelds: such subﬁelds
are of the form Q(√dI), where I = {i1, . . . , im} is a nonempty subset of {1, 2, . . . , k} and
dI = di1 · · · dim. Since each Q(√dI) has unit rank 1, it is natural to suspect that choosing
one unit (besides ±1) from each quadratic subﬁeld of K should give us a multiplicatively
independent set of units in K.
Theorem 6.3. With notation as above, let uI be a unit in Q(√dI) other than ±1. These
units are multiplicatively independent: if Q
I uaI
I = 1, where the exponents aI are in Z, then
each aI is 0.
Proof. Our argument is taken from [10, Lemma 2] (which includes some extraneous hy-
potheses on the di’s).
The special feature of a unit in a real quadratic ﬁeld is that its
Q-conjugate is, up to sign, its inverse: u′ = ±u−1. This fact will interact well with multi-
plication relations.
One Q-basis of K is all the square roots √dI together with 1 (we could set d∅= 1 and
1 =
p
d∅). For each nonempty subset J of {1, 2, . . . , k}, there is a σJ ∈Gal(K/Q) such that
σJ(√dJ) = −√dJ and σJ(√dI) = √dI for all I ̸= J. Since σJ is the identity on Q(√dI)
and is nontrivial on Q(√dJ), σJ(uI) = uI while σJ(uJ) = ±u−1
J .
Applying σJ to Q
I uaI
I
= 1 turns it into Q
I̸=J uaI
I · (±u−1
J )aJ = 1. Dividing one multi-
plicative relation by the other, (±u2
J)aJ = 1. Since uJ has inﬁnite order, aJ = 0.
□
Corollary 6.4. The units uI generate a subgroup of O×
K with ﬁnite index.
Proof. By their multiplicative independence, the uI’s generate a group of rank 2k −1, which
is the rank of O×
K.
□
Appendix A. Minimal nonzero value of a quadratic form
The following theorem is used near the end of the proof of Theorem 5.8.

<!-- page 26 -->
26
KEITH CONRAD
Theorem A.1. Let Q(x, y) = Ax2 + 2Bxy + Cy2 = (x y)( A B
B C )
 x
y

be a positive-deﬁnite
integral binary quadratic form with an even middle coeﬃcient, and set det(Q) := AC−B2 >
0. There is a nonzero vector (x0, y0) ∈Z2 such that 0 < Q(x0, y0) ≤
p
(4/3) det(Q).
Proof. Since AC −B2 > 0, we have A = Q(1, 0) > 0 and C = Q(0, 1) > 0. In fact, all
values of Q on R2 −{(0, 0)} are positive since
Q(x, y) = A

x2 + 2B
A xy + C
Ay2

= A
 
x + B
Ay
2
+ AC −B2
A2
y2
!
= A
 
x + B
Ay
2
+ det(Q)
A2
y2
!
> 0,
so the polynomial Q(x, y) on Z2 −{(0, 0)} has a minimum value in Z+. First assume A is
the minimum value of Q on Z2 −{(0, 0)}. Then we’ll reduce the general case to that case.
Step 1: A = min Q(x, y) where (x, y) runs over Z2 −{(0, 0)}.
Pick an integer x within 1/2 of −B/A: |x + B/A| ≤1/2. Then Q(x, 1) ≤A(1/2)2 +
det(Q)/A. From the minimality assumption on A,
A ≤Q(x, 1) ≤A
4 + det(Q)
A
,
so (3/4)A2 ≤det(Q). Therefore Q(1, 0) = A ≤
p
(4/3) det(Q).
Step 2: General Q.
Let min Q(x, y) = Q(x0, y0) > 0, where (x, y) runs over Z2 −{(0, 0)}. The integers x0
and y0 are relatively prime: setting d = gcd(x0, y0) and writing x0 = dx′
0 and y0 = dy′
0,
Q(x0, y0) = Q(dx′
0, dy′
0) = d2Q(x′
0, y′
0) ≥Q(x′
0, y′
0), so if d > 1 then the minimality of Q at
(x0, y0) is violated. Thus d = gcd(x0, y0) = 1.
There are x1 and y1 in Z such that x0y1 −y0x1 = 1, so the integral matrix M = ( x0 x1
y0 y1 )
is invertible as an integral matrix with determinant 1. Note M
 1
0

=
 x0
y0

.
Now we’ll make an invertible integral change of variables in Q(x, y). Set
eQ(x, y) = Q

M
x
y

=

M
x
y
⊤
A
B
B
C

M
x
y

= (x y)M⊤

A
B
B
C

M
x
y

.
The product M⊤( A B
B C )M is symmetric (it equals its transpose) and has integral entries
since M does. Its determinant is AC −B2 = det(Q) since det(M) = 1. Therefore if we
write M⊤( A B
B C )M as ( e
A e
B
e
B eC ), we have eQ(x, y) = eAx2 + 2 eBxy + eCy2 where det( eQ) = det(Q).
By Step 1, eQ(1, 0) = eA ≤
q
(4/3) det( eQ) =
p
(4/3) det(Q). Since eQ(1, 0) = Q(M
 1
0

) =
Q(x0, y0), we have 0 < Q(x0, y0) ≤
p
(4/3) det(Q).
□
References
[1] E. Artin, Theory of Algebraic Numbers, George Striker, Schildweg 12, G¨ottingen, 1959.
[2] W. E. H. Berwick, “Algebraic number-ﬁelds with two independent units,” Proc. London Math. Soc. 34
(1932), 360–378.
[3] T. Cusick, “Lower bounds for regulators,” pp. 63–73 in Number Theory, Noordwijkerhout 1983, LNM
1068, Springer, Berlin 1984.

<!-- page 27 -->
DIRICHLET’S UNIT THEOREM
27
[4] P. G. L. Dirichlet, Vorlesungen ¨uber Zahlentheorie, 4th ed., Vieweg und Sohn, Braunschweig, 1894. URL
https://archive.org/details/vorlesungenberz02dirigoog.
[5] R. Godement, Introduction `a la Th´eorie des Groups de Lie, Springer–Verlag, Berlin, 2003.
[6] E. Kleinert, “Units of Classical Orders: A Survey,” L’Enseignement Math. 40 (1994), 205–248.
[7] E. Kleinert, Units in Skew Fields, Birkha¨user, Basel, 2000.
[8] H. Koch, Number Theory: Algebraic Numbers and Functions, Amer. Math. Society, Providence, 2000.
[9] S. Kuroda, “¨Uber den Dirichletschen K¨orper,” J. Fac. Sci. Imp. Univ. Tokyo Sect. I 4 (1943), 383–406.
[10] F. Luca and I. E. Shparlinski, “On the Square-free Parts of ⌊en!⌋,” Glasgow Math. J. 49 (2007), 391–403.
[11] H. Minkowski, “Peter Gustav Lejeune Dirichlet und seine Bedeutung f¨ur die heutige Mathematik,”
Jahresbericht der Deutschen Mathematiker-Vereinigung 14 (1905), 149–163.
[12] L. J. Mordell, Review of E. Artin’s “Theory of Algebraic Numbers,” Bull. Amer. Math. Soc. 3 (1962),
162–166.
[13] D. Shanks, “The Simplest Cubic Fields,” Math. Comp. 28 (1974), 1137–1152.
[14] J. H. Silverman, “An inequality relating the regulator and the discriminant of a number ﬁeld,” J.
Number Theory 19 (1984), 437–442.
[15] E. Thomas, “Fundamental units for orders in certain cubic number ﬁelds,” J. Reine Angew. Math. 310
(1979), 33–55.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*