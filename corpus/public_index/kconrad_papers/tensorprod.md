# Tensor Products I

> **Source**: https://kconrad.math.uconn.edu/blurbs/tensorprod.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
TENSOR PRODUCTS
KEITH CONRAD
1. Introduction
Let R be a commutative ring and M and N be R-modules. (We always work with rings
having a multiplicative identity and modules are assumed to be unital: 1 · m = m for all
m ∈M.) The direct sum M ⊕N is an addition operation on modules. We introduce here a
product operation M ⊗R N, called the tensor product. We will start oﬀby describing what
a tensor product of modules is supposed to look like. Rigorous deﬁnitions are in Section 3.
Tensor products ﬁrst arose for vector spaces, and this is the only setting where they
occur in physics and engineering, so we’ll describe tensor products of vector spaces ﬁrst.
Let V and W be vector spaces over a ﬁeld K, and choose bases {ei} for V and {fj} for
W. The tensor product V ⊗K W is deﬁned to be the K-vector space with a basis of formal
symbols ei ⊗fj (we declare these new symbols to be linearly independent by deﬁnition).
Thus V ⊗K W is the formal sums P
i,j cijei ⊗fj with cij ∈K. Elements of V ⊗K W are
called tensors. For v ∈V and w ∈W, deﬁne v ⊗w to be the element of V ⊗K W obtained
by writing v and w in terms of the original bases of V and W and then expanding out v ⊗w
as if ⊗were a noncommutative product (allowing scalars to be pulled out).
For example, let V = W = R2 = Re1 + Re2, where {e1, e2} is the standard basis. (We
use the same basis for both copies of R2.) Then R2 ⊗R R2 is a 4-dimensional space with
basis e1 ⊗e1, e1 ⊗e2, e2 ⊗e1, and e2 ⊗e2. If v = e1 −e2 and w = e1 + 2e2, then
(1.1)
v ⊗w = (e1 −e2) ⊗(e1 + 2e2) := e1 ⊗e1 + 2e1 ⊗e2 −e2 ⊗e1 −2e2 ⊗e2.
Does v ⊗w depend on the choice of a basis of R2?
As a test, pick another basis, say
e′
1 = e1 + e2 and e′
2 = 2e1 −e2. Then v and w can be written as v = −1
3e′
1 + 2
3e′
2 and
w = 5
3e′
1 −1
3e′
2. By a formal calculation,
v ⊗w =

−1
3e′
1 + 2
3e′
2

⊗
5
3e′
1 −1
3e′
2

= −5
9e′
1 ⊗e′
1 + 1
9e′
1 ⊗e′
2 + 10
9 e′
2 ⊗e′
1 −2
9e′
2 ⊗e′
2,
and if you substitute into this last linear combination the deﬁnitions of e′
1 and e′
2 in terms
of e1 and e2, expand everything out, and collect like terms, you’ll return to the sum on the
right side of (1.1). This suggests that v ⊗w has a meaning in R2 ⊗R R2 that is independent
of the choice of a basis, although proving that might look daunting.
In the setting of modules, a tensor product can be described like the case of vector spaces,
but the properties that ⊗is supposed to satisfy have to be laid out in general, not just on a
basis (which may not even exist): for R-modules M and N, their tensor product M ⊗R N
(read as “M tensor N” or “M tensor N over R”) is an R-module spanned – not as a basis,
but just as a spanning set1 – by all symbols m ⊗n, with m ∈M and n ∈N, and these
1Recall a spanning set for an R-module is a subset whose ﬁnite R-linear combinations ﬁll up the module.
They always exist, since the entire module is a spanning set.
1

<!-- page 2 -->
2
KEITH CONRAD
symbols satisfy distributive laws:
(1.2)
(m + m′) ⊗n = m ⊗n + m′ ⊗n,
m ⊗(n + n′) = m ⊗n + m ⊗n′.
Also multiplication by r ∈R can be put into either side of ⊗: for m ∈M and n ∈N,
(1.3)
r(m ⊗n) = (rm) ⊗n = m ⊗(rn).
Therefore writing rm ⊗n is unambiguous: it is both r(m ⊗n) and (rm) ⊗n.
Formulas (1.2) and (1.3) in M ⊗R N should be contrasted with formulas in M ⊕N, where
(m + m′, n) = (m, n) + (m′, 0),
r(m, n) = (rm, rn).
In M ⊕N, an element (m, n) decomposes as (m, 0) + (0, n), but m ⊗n in M ⊗R N does
not break apart. While every element of M ⊕N is a pair (m, n), there are usually more
elements of M ⊗R N than the products m ⊗n. The general element of M ⊗R N, which is
called a tensor, is an R-linear combination2
r1(m1 ⊗n1) + r2(m2 ⊗n2) + · · · + rk(mk ⊗nk),
where k ≥1, ri ∈R, mi ∈M, and ni ∈N. Since ri(mi ⊗ni) = (rimi) ⊗ni, we can rename
rimi as mi and write the above linear combination as a sum
(1.4)
m1 ⊗n1 + m2 ⊗n2 + · · · + mk ⊗nk.
In the direct sum M ⊕N, equality is easy to deﬁne: (m, n) = (m′, n′) if and only if
m = m′ and n = n′. When are two sums of the form (1.4) equal in M ⊗R N? This is not
easy to say in terms of the description of a tensor product that we have given, except in
one case: M and N are free R-modules with bases {ei} and {fj}. In this case, M ⊗R N is
free with basis {ei ⊗fj}, so every element of M ⊗R N is a (ﬁnite) sum P
i,j cijei ⊗fj with
cij ∈R and two such sums are equal only when coeﬃcients of like terms are equal.
To describe equality in M ⊗R N when M and N don’t have bases, we will use a universal
mapping property of M ⊗R N. The tensor product is the ﬁrst concept in algebra whose
properties make consistent sense only by a universal mapping property, which is: M ⊗R N
is the universal object that turns bilinear maps on M × N into linear maps. As Jeremy
Kun [13] writes, M ⊗R N is the “gatekeeper” of all bilinear maps out of M × N.
After a discussion of bilinear (and multilinear) maps in Section 2, the deﬁnition and
construction of the tensor product is presented in Section 3. Examples of tensor products
are in Section 4. In Section 5 we will show how the tensor product interacts with some other
constructions on modules. Section 6 describes the important operation of base extension,
which is a process of using tensor products to turn an R-module into an S-module where S
is another ring. Finally, in Section 7 we describe the notation used for tensors in physics.
Here is a brief history of tensors and tensor products.
Tensor comes from the Latin
tendere, which means “to stretch.” In 1822 Cauchy introduced the Cauchy stress tensor
in continuum mechanics, and in 1861 Riemann created the Riemann curvature tensor in
geometry, but they did not use those names. In 1884, Gibbs [7, Chap. 3] introduced tensor
products of vectors in R3 with the label “indeterminate product”3 and applied it to study
strain on a body.
He extended the indeterminate product to n dimensions in 1886 [8].
2Compare with the polynomial ring R[X, Y ], whose elements are not only products f(X)g(Y ), but sums
of such products P
i,j aijXiY j. It turns out that R[X, Y ] ∼= R[X] ⊗R R[Y ] as R-modules (Example 4.12).
3Gibbs chose that label since this product was, in his words, “the most general form of product of two
vectors,” as it is subject to no laws except bilinearity, which must be satisﬁed by any operation deserving to
be called a product. In 1844, Grassmann created a special tensor called an “open product” [20, Chap. 3].

<!-- page 3 -->
TENSOR PRODUCTS
3
Voigt used tensors to describe stress and strain on crystals in 1898 [25], and the term tensor
ﬁrst appeared with its modern physical meaning there.4 In geometry Ricci used tensors in
the late 1800s and his 1901 paper [22] with Levi-Civita (in English in [15]) was crucial in
Einstein’s work on general relativity. Wide use of the term “tensor” in physics and math is
due to Einstein; Ricci and Levi-Civita called tensors by the bland name “systems”. Weyl’s
book on group theory and quantum mechanics called the tensor product of vector spaces V
and W a “product space” and denoted it by V × W [27, Chap. II, Sect. 10]. The notation
⊗is due to Murray and von Neumann in 1936 [17, Chap. II] for tensor products (they
wrote “direct products”) of Hilbert spaces.5 The tensor product of abelian groups A and
B, with that name but written as A ◦B instead of A ⊗Z B, is due to Whitney [28] in 1938.
Tensor products of modules over a commutative ring are due to Bourbaki [2] in 1948.
2. Bilinear Maps
We already described the elements of M ⊗R N as sums (1.4) subject to the rules (1.2)
and (1.3). The intention is that M ⊗R N is the “freest” object satisfying (1.2) and (1.3).
The essence of (1.2) and (1.3) is bilinearity. What does that mean?
A function B : M × N →P, where M, N, and P are R-modules, is called bilinear if it is
linear (that is, R-linear) in each argument when the other one ﬁxed:
(2.1)
B(m1 + m2, n) = B(m1, n) + B(m2, n),
B(rm, n) = rB(m, n),
(2.2)
B(m, n1 + n2) = B(m, n1) + B(m, n2),
B(m, rn) = rB(m, n).
So B(−, n) is a linear map M →P for each n and B(m, −) is a linear map N →P for each
m. In particular, B(0, n) = 0 and B(m, 0) = 0. Here are some examples of bilinear maps.
(1) The dot product v · w on Rn is a bilinear function Rn × Rn →R. More generally,
for A ∈Mn(R) the function ⟨v, w⟩= v · Aw is a bilinear map Rn × Rn →R.
(2) Matrix multiplication Mm,n(R)×Mn,p(R) →Mm,p(R) is bilinear. The dot product
is the special case m = p = 1 (writing v · w as v⊤w).
(3) The cross product v × w is a bilinear function R3 × R3 →R3.
(4) The determinant det: M2(R) →R is a bilinear function of matrix columns.
(5) For an R-module M, scalar multiplication R × M →M is bilinear.
(6) Multiplication R × R →R is bilinear.
(7) Set the dual module of M to be M∨= HomR(M, R). The dual pairing M∨×M →R
given by (ϕ, m) 7→ϕ(m) is bilinear.
(8) For ϕ ∈M∨and ψ ∈N∨, the map M × N →R where (m, n) 7→ϕ(m)ψ(n) is
bilinear.
(9) If M × N
B
−−→P is bilinear and P
L
−−→Q is linear, the composite M × N
L◦B
−−−−→Q
is bilinear. (This is a very important example. Check it!)
(10) From Section 1, the expression m ⊗n is supposed to be bilinear in m and n. That
is, we want the function M ×N →M ⊗R N given by (m, n) 7→m⊗n to be bilinear.
Here are a few examples of functions of two arguments that are not bilinear:
(1) For an R-module M, addition M ×M →M, where (m, m′) 7→m+m′, is usually not
bilinear: it is usually not additive in m when m′ is ﬁxed (that is, (m1 + m2) + m′ ̸=
(m1 + m′) + (m2 + m′) in general) or additive in m′ when m is ﬁxed.
4Writing i, j, and k for the standard basis of R3, Gibbs called a sum ai ⊗i + bj ⊗j + ck ⊗k with positive
a, b, and c a right tensor [7, p. 57], but I don’t know if this had an inﬂuence on Voigt’s terminology.
5I thank Jim Casey for bringing [17] to my attention.

<!-- page 4 -->
4
KEITH CONRAD
(2) For ϕ ∈M∨and ψ ∈N∨, the sum M × N →R given by (m, n) 7→ϕ(m) + ψ(n) is
usually not bilinear.
(3) Treat Mn(C) as a C-vector space. The function Mn(C) × Mn(C) →Mn(C) given
by (A, B) 7→AB is not bilinear. It is biadditive (i.e., additive in each component
when the other one is ﬁxed) but look at how scalar multiplication behaves in the
second component: for z ∈C, AzB is z(AB) rather than z(AB).
Why write bilinear functions as B : M × N →P, not as B : M ⊕N →P? Because
we don’t use a module structure on the domain. That’s why for addition R × R →R and
multiplication R×R →R, we might write addition as R⊕R →R (it is linear on R⊕R) but
we don’t do that for multiplication: it’s bilinear, but not linear, e.g., (r+r′)(s+s′) ̸= rs+r′s′
in general. Linear functions are generalized additions and bilinear functions are generalized
multiplications.
Don’t confuse a bilinear function on M × N with a linear function on
M ⊕N.
For R-modules M1, . . . , Mk, a function f : M1 × · · · × Mk →M is called multilinear
or k-multilinear if f(m1, . . . , mk) is linear (that is, R-linear) in each mi when the other
coordinates are ﬁxed. So 2-multilinear means bilinear. Here are some multilinear functions:
(1) The scalar triple product u · (v × w) is trilinear R3 × R3 × R3 →R.
(2) The function f(u, v, w) = (u · v)w is trilinear Rn × Rn × Rn →Rn.
(3) The function M∨× M × N →N given by (ϕ, m, n) 7→ϕ(m)n is trilinear.
(4) If B : M × N →P and B′ : P × Q →T are bilinear then M × N × Q →T by
(m, n, q) 7→B′(B(m, n), q) is trilinear.
(5) Multiplication R × · · · × R →R with k factors is k-multilinear.
(6) The determinant det: Mn(R) →R, as a function of matrix columns, is n-multilinear.
(7) If M1 ×· · ·×Mk
f
−−→M is k-multilinear and M
L
−−→N is linear then the composite
M1 × · · · × Mk
L◦f
−−−−→N is k-multilinear.
(8) For f : Rm →Rn and x ∈Rm, the kth derivative (Dkf)x : (Rm)k →Rn is k-
multilinear. (If you’re unfamiliar with 1st derivatives as linear maps, ignore this.)
The R-linear maps M →N form an R-module HomR(M, N) under addition of functions
and R-scaling. The R-bilinear maps M × N →P form an R-module BilR(M, N; P) in the
same way. However, unlike linear maps, bilinear maps are missing some features:
(1) There is no “kernel” of a bilinear map M × N →P since M × N is not a module.
(2) The image of a bilinear map M × N →P need not form a submodule.
Example 2.1. Deﬁne B : Rn × Rn →Mn(R) by B(v, w) = vw⊤, where v and w are
column vectors, so vw⊤is n × n. For example, when n = 2,
B
a1
a2

,
b1
b2

=
a1
a2

(b1, b2) =

a1b1
a1b2
a2b1
a2b2

.
Generally, if v = P aiei and w = P bjej in terms of the standard basis of Rn, then vw⊤is
the n × n matrix (aibj). This matrix is R-bilinear in v and w, so B is bilinear. For n ≥2
the image of B isn’t closed under addition, so it isn’t a subspace of Mn(R). Why? Each
matrix B(v, w) has rank 1 (or 0) since its columns are scalar multiples of v. The matrix
B(e1, e1) + B(e2, e2) = e1e⊤
1 + e2e⊤
2 =





1
0
· · ·
0
0
1
· · ·
0
...
...
...
...
0
0
· · ·
0






<!-- page 5 -->
TENSOR PRODUCTS
5
has a 2-dimensional image, so B(e1, e1) + B(e2, e2) ̸= B(v, w) for all v and w in Rn.
(Similarly, Pn
i=1 B(ei, ei) is the n × n identity matrix, which is not of the form B(v, w).)
3. Construction of the Tensor Product
A bilinear map M × N →P to an R-module P can be composed with a linear map
P →Q to get a map M × N →Q that is bilinear.
P
linear

M × N
bilinear
;
composite is bilinear!
# Q
We will construct the tensor product of M and N as a solution to a universal mapping
problem: ﬁnd an R-module T and bilinear map b: M × N →T such that every bilinear
map on M × N is the composite of the bilinear map b and a unique linear map out of T.
T
∃linear?

M × N
b
;
bilinear
# P
This is analogous to the universal mapping property of the abelianization G/[G, G] of a
group G: homomorphisms G −→A with abelian A are “the same” as homomorphisms
G/[G, G] −→A because every homomorphism f : G →A is the composite of the canonical
homomorphism π: G →G/[G, G] with a unique homomorphism ef : G/[G, G] →A.
G/[G, G]
ef

G
π
:
f
$ A
Deﬁnition 3.1. The tensor product M ⊗R N is an R-module equipped with a bilinear map
M × N
⊗
−−→M ⊗R N such that for each bilinear map M × N
B
−−→P there is a unique
linear map M ⊗R N
L
−−→P making the following diagram commute.
M ⊗R N
L

M × N
⊗
8
B
& P

<!-- page 6 -->
6
KEITH CONRAD
While the functions in the universal mapping property for G/[G, G] are all group ho-
momorphisms (out of G and G/[G, G]), functions in the universal mapping property for
M ⊗R N are not all of the same type: those out of M × N are bilinear and those out of
M ⊗R N are linear: bilinear maps out of M × N turn into linear maps out of M ⊗R N.
The deﬁnition of the tensor product involves not just a new module M ⊗R N, but also a
special bilinear map to it, ⊗: M ×N −→M ⊗R N. This is similar to the universal mapping
property for the abelianization G/[G, G], which requires not just G/[G, G] but also the
homomorphism π: G −→G/[G, G] through which all homomorphisms from G to abelian
groups factor. The universal mapping property requires ﬁxing this extra information.
Before building a tensor product, let’s show any two tensor products are essentially the
same. Let R-modules T and T ′, and bilinear maps M ×N
b
−−→T and M ×N
b′
−−→T ′, satisfy
the universal mapping property of the tensor product. From universality of M × N
b
−−→T,
the map M × N
b′
−−→T ′ factors uniquely through T: a unique linear map f : T →T ′ makes
(3.1)
T
f

M × N
b
;
b′
#
T ′
commute. From universality of M × N
b′
−−→T ′, the map M × N
b
−−→T factors uniquely
through T ′: a unique linear map f′ : T ′ →T makes
(3.2)
T ′
f′

M × N
b′
;
b
$ T
commute. We combine (3.1) and (3.2) into the commutative diagram
T
f

M × N
b′
/
b
#
b
;
T ′
f′

T

<!-- page 7 -->
TENSOR PRODUCTS
7
Removing the middle, we have the commutative diagram
(3.3)
T
f′◦f

M × N
b
;
b
# T
From universality of (T, b), a unique linear map T →T ﬁts in (3.3). The identity map
works, so f′ ◦f = idT . Similarly, f ◦f′ = idT ′ by stacking (3.1) and (3.2) together in the
other order. Thus T and T ′ are isomorphic R-modules by f and f′, so T ′ = f(T) and
T = f′(T ′). Also f ◦b = b′, which means f identiﬁes b with b′. So two tensor products of M
and N can be identiﬁed with each other in a unique way compatible6 with the distinguished
bilinear maps to them from M × N.
Theorem 3.2. A tensor product of M and N exists.
Proof. Consider M × N simply as a set. We form the free R-module on this set:
FR(M × N) =
M
(m,n)∈M×N
Rδ(m,n).
(This is an huge R-module. If R = R and M = N = R3 then FR(M × N) is a direct sum
of R6-many copies of R. The direct sum runs over all pairs of vectors from R3, not just
pairs coming from a basis of R3, and its components lie in R.) Let D be the submodule of
FR(M × N) spanned by all the elements
δ(m+m′,n) −δ(m,n) −δ(m′,n),
δ(m,n+n′) −δ(m,n) −δ(m,n′),
δ(rm,n) −δ(m,rn),
rδ(m,n) −δ(rm,n),
rδ(m,n) −δ(m,rn).
The quotient module by D will serve as the tensor product: set
M ⊗R N := FR(M × N)/D.
We write the coset δ(m,n) + D in M ⊗R N as m ⊗n.
From the deﬁnition of D, we get relations in FR(M × N)/D like
δ(m+m′,n) ≡δ(m,n) + δ(m′,n) mod D,
which is the same as
(m + m′) ⊗n = m ⊗n + m′ ⊗n
in M ⊗R N. Similarly, m ⊗(n + n′) = m ⊗n + m ⊗n′ and r(m ⊗n) = rm ⊗n = m ⊗rn in
M ⊗R N. These relations are the reason D was deﬁned the way it was, and they show that
the function M × N
⊗
−−→M ⊗R N given by (m, n) 7→m ⊗n is bilinear. (No other function
M × N →M ⊗R N will be considered except this one.)
Now we will show all bilinear maps out of M ×N factor uniquely through the bilinear map
M ×N →M ⊗R N that we just wrote down. Suppose P is an R-module and M ×N
B
−−→P
is a bilinear map. Treating M ×N simply as a set, so B is just a function on this set (ignore
its bilinearity), the universal mapping property of free modules extends B from a function
6The universal mapping property is not about modules T per se, but about pairs (T, b).

<!-- page 8 -->
8
KEITH CONRAD
M × N →P to a linear function ℓ: FR(M × N) →P with ℓ(δ(m,n)) = B(m, n), so the
diagram
FR(M × N)
ℓ

M × N
(m,n)7→δ(m,n)
7
B
' P
commutes. We want to show ℓmakes sense as a function on M ⊗R N, which means showing
ker ℓcontains D. From the bilinearity of B,
B(m + m′, n) = B(m, n) + B(m′, n),
B(m, n + n′) = B(m, n) + B(m, n′),
rB(m, n) = B(rm, n) = B(m, rn),
so
ℓ(δ(m+m′,n)) = ℓ(δ(m,n)) + ℓ(δ(m′,n)),
ℓ(δ(m,n+n′)) = ℓ(δ(m,n)) + ℓ(δ(m,n′)),
rℓ(δ(m,n)) = ℓ(δ(rm,n)) = ℓ(δ(m,rn)).
Since ℓis linear, these conditions are the same as
ℓ(δ(m+m′,n)) = ℓ(δ(m,n) + δ(m′,n)),
ℓ(δ(m,n+n′)) = ℓ(δ(m,n) + δ(m,n′)),
ℓ(rδ(m,n)) = ℓ(δ(rm,n)) = ℓ(δ(m,rn)).
Therefore the kernel of ℓcontains all the generators of the submodule D, so ℓinduces a
linear map L: FR(M × N)/D →P where L(δ(m,n) + D) = ℓ(δ(m,n)) = B(m, n), which
means the diagram
FR(M × N)/D
L

M × N
(m,n)7→δ(m,n)+D
7
B
( P
commutes. Since FR(M × N)/D = M ⊗R N and δ(m,n) + D = m ⊗n, the above diagram is
(3.4)
M ⊗R N
L

M × N
⊗
8
B
& P
and that shows every bilinear map B out of M × N comes from a linear map L out of
M ⊗R N such that L(m ⊗n) = B(m, n) for all m ∈M and n ∈N.
It remains to show the linear map M ⊗R N
L
−−→P in (3.4) is the only one that makes
(3.4) commute. We go back to the deﬁnition of M ⊗R N as a quotient of the free module

<!-- page 9 -->
TENSOR PRODUCTS
9
FR(M ×N). From the construction of free modules, every element of FR(M ×N) is a ﬁnite
sum
r1δ(m1,n1) + · · · + rkδ(mk,nk).
The reduction map FR(M × N) ↠FR(M × N)/D = M ⊗R N is linear, so every element of
M ⊗R N is a ﬁnite sum
(3.5)
r1(m1 ⊗n1) + · · · + rk(mk ⊗nk).
This means the elements m ⊗n in M ⊗R N span it as an R-module. Therefore linear maps
out of M ⊗R N are completely determined by their values on all the elements m ⊗n, so
there is at most one linear map M ⊗R N →P with the eﬀect m ⊗n 7→B(m, n). We have
created a linear map out of M ⊗R N with this very eﬀect in (3.4), so it is the only one.
□
Having shown a tensor product of M and N exists,7 its essential uniqueness lets us
call M ⊗R N “the” tensor product rather than “a” tensor product. Don’t forget that the
construction involves not only the module M ⊗R N but also the distinguished bilinear map
M × N
⊗
−−→M ⊗R N given by (m, n) 7→m ⊗n, through which all bilinear maps out of
M × N factor. We call this distinguished map the canonical bilinear map from M × N
to the tensor product.
Elements of M ⊗R N are called tensors, and will be denoted
by the letter t.
Tensors in M ⊗R N that have the form m ⊗n are called elementary
tensors. (Other names for elementary tensors are simple tensors, decomposable tensors,
pure tensors, and monomial tensors.) Just as elements of the free R-module FR(A) on a set
A are usually not of the form δa but are linear combinations of these, elements of M ⊗R N
are usually not elementary tensors8 but are linear combinations of elementary tensors
by the way we constructed M ⊗R N. In fact each tensor is a sum of elementary tensors
since r(m ⊗n) = (rm) ⊗n. This shows all elements of M ⊗R N have the form (1.4).
That every tensor is a sum of elementary tensors, but need not be an elementary tensor
itself, is a feature that confuses people who are learning about tensor products. One source
of the confusion is that in the direct sum M ⊕N every element is a pair (m, n), so why
shouldn’t every element of M ⊗R N have the form m ⊗n? Here are two related ideas to
keep in mind, so it seems less strange that not all tensors are elementary.
• The R-module R[X, Y ] is a tensor product of R[X] and R[Y ] (see Example 4.12)
and, as Eisenbud and Harris note in their book on schemes [5, p. 39], the study
of polynomials in two variables is more than the study of polynomials of the form
f(X)g(Y ). That is, most polynomials in R[X, Y ] are not f(X)g(Y ), but they are
all a sum of such products (and in fact they are sums of monomials aijXiY j).
7What happens if R is a noncommutative ring? If M and N are left R-modules and B is bilinear on
M × N then for all m ∈M, n ∈N, and r and s in R, rsB(m, n) = rB(m, sn) = B(rm, sn) = sB(rm, n) =
srB(m, n). Usually rs ̸= sr, so asking that rsB(m, n) = srB(m, n) for all m and n puts us in a delicate
situation! The correct tensor product M ⊗R N for noncommutative R uses a right R-module M, a left R-
module N, and a “middle-linear” map B where B(mr, n) = B(m, rn). In fact M ⊗R N is not an R-module
but just an abelian group! While we won’t deal with tensor products over a noncommutative ring, they are
important. They appear in the construction of induced representations of groups.
8For R ̸= 0, an explicit example of a nonelementary tensor in R2 ⊗R R2 will be provided in Example 4.11.
We essentially already met one in Example 2.1 when we saw e1e⊤
1 + e2e⊤
2 ̸= vw⊤for all v and w in Rn.

<!-- page 10 -->
10
KEITH CONRAD
• The role of elementary tensors among all tensors is like that of separable solutions
f(x)g(y) to a 2-variable PDE among all solutions.9 Solutions to a PDE may not be
separable. First we determine the separable solutions and then the general solution
as a sum (perhaps an inﬁnite sum) of separable solutions.
From now on forget the explicit construction of M ⊗R N as the quotient of an enormous
free module FR(M × N). It will confuse you more than it’s worth to try to think about
M ⊗R N in terms of its construction. What is more important to remember is the universal
mapping property of the tensor product, which we will start using systematically in the
next section. To get used to the bilinearity of ⊗, let’s prove two simple results.
Theorem 3.3. Let M and N be R-modules with respective spanning sets {xi}i∈I and
{yj}j∈J. The tensor product M ⊗R N is spanned linearly by the elementary tensors xi ⊗yj.
Proof. An elementary tensor in M ⊗R N is m⊗n. Let m = P
i aixi and n = P
j bjyj, where
the ai’s and bj’s are 0 for all but ﬁnitely many i and j. By bilinearity of ⊗,
m ⊗n =
X
i
aixi ⊗
X
j
bjyj =
X
i,j
aibjxi ⊗yj,
so each m ⊗n is a linear combination of the particular elementary tensors xi ⊗yj. Every
tensor is a sum of elementary tensors,10 so the xi ⊗yj’s span M ⊗R N as an R-module.
□
Example 3.4. Let e1, . . . , ek be the standard basis of Rk. The R-module Rk ⊗R Rk is
linearly spanned by the k2 elementary tensors ei ⊗ej. We will see later (Theorem 4.9) that
these elementary tensors are a basis of Rk ⊗R Rk, which for R a ﬁeld is consistent with the
physicist’s “deﬁnition” of tensor products of vector spaces from Section 1 using bases.
Theorem 3.5. In M ⊗R N, m ⊗0 = 0 and 0 ⊗n = 0.
Proof. This is just like the proof that a·0 = 0 in a ring: since m⊗n is additive in n with m
ﬁxed, m ⊗0 = m ⊗(0 + 0) = m ⊗0 + m ⊗0. Subtracting m ⊗0 from both sides, m ⊗0 = 0.
That 0 ⊗n = 0 follows by a similar argument.
□
Example 3.6. If A is a ﬁnite abelian group, Q ⊗Z A = 0 since every elementary tensor is
0: for a ∈A, let na = 0 for some positive integer n. Then in Q ⊗Z A, r ⊗a = n(r/n) ⊗a =
r/n⊗na = r/n⊗0 = 0. Every tensor is a sum of elementary tensors, and every elementary
tensor is 0, so all tensors are 0. (For instance, (1/3) ⊗(5 mod 7) = 0 in Q ⊗Z Z/7Z. Thus
we can have m ⊗n = 0 without m or n being 0.)
To show Q ⊗Z A = 0, we don’t need A to be ﬁnite, but only that each element of A has
ﬁnite order. Since Q/Z has that property, Q ⊗Z (Q/Z) = 0. Similarly, Q/Z ⊗Z Q/Z = 0.
Since M ⊗R N is spanned additively by elementary tensors, each linear (or just additive)
function out of M ⊗R N is determined on all tensors from its values on elementary tensors.
This is why linear maps on tensor products are in practice described only by their values
9In Brad Osgood’s notes on the Fourier transform [19, pp. 343-344], he writes about functions of the
form f1(x1)f2(x2) · · · fn(xn) “If you really want to impress your friends and confound your enemies, you can
invoke tensor products in this context. [ . . . ] People run in terror from the ⊗symbol. Cool.”
10We know this by our explicit construction of M ⊗RN. Can it be proved without using the construction?
Yes! If M × N
b→T is a tensor product of M and N, let T ′ in T be the submodule spanned by all b(m, n),
so b(M × N) ⊂T ′. Let M × N
b′
→T ′ be b with its image restricted to T ′. Prove this is also a tensor product
of M and N. Then in (3.2) for these tensor products, the image of b′ spans T ′ and f ′ : T ′ →T is surjective
since it is an isomorphism, so the image of b = f ′ ◦b′ spans T. Thus T ′ = T.

<!-- page 11 -->
TENSOR PRODUCTS
11
on elementary tensors. It is similar to describing a linear map between ﬁnite free modules
using a matrix. The matrix directly tells you only the values of the map on a particular
basis, but this information is enough to determine the linear map everywhere.
However, there is a key diﬀerence between basis vectors and elementary tensors: ele-
mentary tensors have lots of linear relations. A linear map out of R2 is determined by its
values on (1, 0), (2, 3), (8, 4), and (−1, 5), but those values are not independent: they have
to satisfy every linear relation the four vectors satisfy because a linear map preserves linear
relations. Similarly, a random function on elementary tensors generally does not extend
to a linear map on the tensor product: elementary tensors span the tensor product of two
modules, but they are not linearly independent.
Functions of elementary tensors can’t be created out of a random function of two variables.
For instance, the “functions” M ⊗R M →M where m ⊗m′ 7→m + m′ and m ⊗m′ 7→m
make no sense since m ⊗m′ = (−m) ⊗(−m′) but m + m′ is usually not −m −m′ and m is
usually not −m. The only good way to create linear maps out of M ⊗RN is by the universal
mapping property of M ⊗R N (it creates linear maps from bilinear maps), since all linear
relations among elementary tensors – from the obvious to the obscure – are built into the
universal mapping property. A lot of practice with this is in Section 4. Understanding how
the universal mapping property of M ⊗R N can be used to compute examples and to prove
properties of tensor products is the best way to get used to tensor products; if you can’t
construct functions out of M ⊗R N, then you don’t understand M ⊗R N.
The tensor product can be extended to allow more than two factors. Given k modules
M1, . . . , Mk, there is a module M1 ⊗R · · · ⊗R Mk that is universal for k-multilinear maps: it
admits a k-multilinear map M1 × · · · × Mk
⊗
−−→M1 ⊗R · · · ⊗R Mk and every k-multilinear
map out of M1 × · · · × Mk factors through this by composition with a unique linear map
out of M1 ⊗R · · · ⊗R Mk:
M1 ⊗R · · · ⊗R Mk
∃unique linear

M1 × · · · × Mk
⊗
5
multilinear
) P
The image of (m1, . . . , mk) in M1 ⊗R · · ·⊗R Mk is written m1 ⊗· · ·⊗mk. This k-fold tensor
product can be constructed as a quotient of the free module FR(M1 ×· · ·×Mk). It can also
be constructed using tensor products of modules two at a time:
(· · · ((M1 ⊗R M2) ⊗R M3) ⊗R · · · ) ⊗R Mk.
The canonical k-multilinear map to this R-module from M1 × · · · × Mk is (m1, . . . , mk) 7→
(· · · ((m1 ⊗m2) ⊗m3) · · · ) ⊗mk. This is not the same construction of the k-fold tensor
product using FR(M1 × · · · ×Mk), but it satisﬁes the same universal mapping property and
thus can serve the same purpose (all constructions of a tensor product of M1, . . . , Mk are
isomorphic to each other in a unique way compatible with the distinguished k-multilinear
maps to them from M1 × · · · × Mk).
The module M1 ⊗R · · · ⊗R Mk is spanned additively by all m1 ⊗· · · ⊗mk. Important
examples of the k-fold tensor product are tensor powers M⊗k of a single R-module M:
M⊗0 = R,
M⊗1 = M,
M⊗2 = M ⊗R M,
M⊗3 = M ⊗R M ⊗R M,

<!-- page 12 -->
12
KEITH CONRAD
and so on. (The formula M⊗0 = R is a convention, like a0 = 1.)
Let’s address a few beginner questions about the tensor product:
Questions
(1) What is m ⊗n?
(2) What does it mean to say m ⊗n = 0?
(3) What does it mean to say M ⊗R N = 0?
(4) What does it mean to say m1 ⊗n1 + · · · + mk ⊗nk = m′
1 ⊗n′
1 + · · · + m′
ℓ⊗n′
ℓ?
(5) How do tensor products make bilinear maps look like linear maps?
(6) Where do tensor products arise outside of mathematics?
(7) Is there a way to picture the tensor product?
Answers
(1) Strictly speaking, m⊗n is the image of (m, n) ∈M ×N under the canonical bilinear
map M × N
⊗
−−→M ⊗R N in the deﬁnition of the tensor product. Here’s another
answer, which is not a deﬁnition but more closely aligns with how m ⊗n occurs in
practice: m ⊗n is that element of M ⊗R N at which the linear map M ⊗R N →P
corresponding to a bilinear map M × N
B
−−→P takes the value B(m, n). Review
the proof of Theorem 3.2 and check this property of m ⊗n really holds.
(2) We have m ⊗n = 0 if and only if every bilinear map out of M × N vanishes at
(m, n). Indeed, if m ⊗n = 0 then for each bilinear map B : M × N →P we have a
commutative diagram
M ⊗R N
L

M × N
⊗
8
B
& P
for some linear map L, so B(m, n) = L(m ⊗n) = L(0) = 0. Conversely, if every
bilinear map out of M × N sends (m, n) to 0 then the canonical bilinear map
M × N →M ⊗R N, which is a particular example, sends (m, n) to 0. Since this
bilinear map actually sends (m, n) to m ⊗n, we obtain m ⊗n = 0.
A very important consequence is a tip about how to show a particular elementary
tensor m ⊗n is not 0: ﬁnd a bilinear map B out of M × N such that B(m, n) ̸= 0.
Remember this idea! It will be used in Theorem 4.9.
That m ⊗0 = 0 and 0 ⊗n = 0 is related to B(m, 0) = 0 and B(0, n) = 0 for each
bilinear map B on M × N. This gives another proof of Theorem 3.5.
As an exercise, check from the universal mapping property that m1⊗· · ·⊗mk = 0
in M1 ⊗R · · ·⊗R Mk if and only if all k-multilinear maps out of M1 ×· · ·×Mk vanish
at (m1, . . . , mk).
(3) The tensor product M ⊗R N is 0 if and only if every bilinear map out of M × N
(to all modules) is identically 0. First suppose M ⊗R N = 0. Then all elementary
tensors m⊗n are 0, so B(m, n) = 0 for all bilinear maps out of M ×N by the answer
to the second question. Thus B is identically 0. Next suppose every bilinear map
out of M ×N is identically 0. Then the canonical bilinear map M ×N
⊗
−−→M ⊗RN,
which is a particular example, is identically 0. Since this function sends (m, n) to

<!-- page 13 -->
TENSOR PRODUCTS
13
m ⊗n, we have m ⊗n = 0 for all m and n. Since M ⊗R N is additively spanned by
all m ⊗n, the vanishing of all elementary tensors implies M ⊗R N = 0.
Returning to Example 3.6, that Q ⊗Z A = 0 if each element of A has ﬁnite order
is another way of saying every Z-bilinear map out of Q×A is identically zero, which
can be veriﬁed directly: if B is such a map (into an abelian group) and na = 0 with
n ≥1, then B(r, a) = B(n(r/n), a) = B(r/n, na) = B(r/n, 0) = 0.
Turning this idea around, to show some tensor product module M ⊗R N is not
0, ﬁnd a bilinear map on M × N that is not identically 0.
(4) We have Pk
i=1 mi ⊗ni = Pℓ
j=1 m′
j ⊗n′
j if and only if for all bilinear maps B out
of M × N, Pk
i=1 B(mi, ni) = Pℓ
j=1 B(m′
j, n′
j). The justiﬁcation is along the lines
of the previous two answers and is left to the reader. For example, the condition
Pk
i=1 mi ⊗ni = 0 means Pk
i=1 B(mi, ni) = 0 for all bilinear maps B on M × N.
(5) For a bilinear map B : M × N →P, its bilinearity is (2.1) and (2.2), which say
B(m1 + m2, n) = B(m1, n) + B(m2, n),
B(rm, n) = rB(m, n),
B(m, n1 + n2) = B(m, n1) + B(m, n2),
B(m, rn) = rB(m, n).
For the associated linear map L: M ⊗R N →P, the bilinearity of B is the same as
L((m1 + m2) ⊗n) = L(m1 ⊗n) + L(m2 ⊗n),
L((rm) ⊗n) = rL(m ⊗n),
L(m ⊗(n1 + n2)) = L(m ⊗n1) + L(m ⊗n2),
L(m ⊗(rn)) = rL(m ⊗n).
Since (m1 + m2) ⊗n = m1 ⊗n + m2 ⊗n, m ⊗(n1 + n2) = m ⊗n1 + m ⊗n2,
(rm) ⊗n = r(m ⊗n), and m ⊗(rn) = r(m ⊗n), the four conditions on L above are
special cases of L(t + t′) = L(t) + L(t′) and L(rt) = rL(t), which is exactly what it
means for L to be linear.
(6) Tensors are used in physics and engineering (stress, elasticity, electromagnetism,
metrics, diﬀusion MRI), where they transform in a multilinear way under a change
in coordinates. The treatment of tensors in physics is discussed in Section 7.
(7) There isn’t a simple picture of a tensor (even an elementary tensor) analogous to
how a vector is an arrow. Some physical manifestations of tensors are in the previous
answer, but they won’t help you understand tensor products of modules.
Nobody is comfortable with tensor products at ﬁrst. Two quotes by Cathy O’Neil and
Johan de Jong11 nicely capture the phenomenon of learning about them:
• O’Neil: After a few months, though, I realized something. I hadn’t gotten any better
at understanding tensor products, but I was getting used to not understanding them.
It was pretty amazing. I no longer felt anguished when tensor products came up; I
was instead almost amused by their cunning ways.
• de Jong: It is the things you can prove that tell you how to think about tensor
products.
In other words, you let elementary lemmas and examples shape your
intuition of the mathematical object in question. There’s nothing else, no magical
intuition will magically appear to help you “understand” it.
Remark 3.7. Hassler Whitney, who ﬁrst deﬁned tensor products beyond the setting of
vector spaces, called abelian groups A and B a group pair relative to the abelian group C
if there is a Z-bilinear map A × B →C and wrote [28, p. 499] that “any such group pair
may be deﬁned by choosing a homomorphism” A ⊗Z B →C. So the idea that ⊗Z solves a
universal mapping problem is essentially due to Whitney.
11See http://mathbabe.org/2011/07/20/what-tensor-products-taught-me-about-living-my-life/.

<!-- page 14 -->
14
KEITH CONRAD
4. Examples of Tensor Products
Theorem 4.1. For positive integers a and b with d = (a, b), Z/aZ ⊗Z Z/bZ ∼= Z/dZ as
abelian groups. In particular, Z/aZ ⊗Z Z/bZ = 0 if and only if (a, b) = 1.
Proof. Since 1 spans Z/aZ and Z/bZ, 1 ⊗1 spans Z/aZ ⊗Z Z/bZ by Theorem 3.3. From
a(1 ⊗1) = a ⊗1 = 0 ⊗1 = 0 and b(1 ⊗1) = 1 ⊗b = 1 ⊗0 = 0,
the additive order of 1 ⊗1 divides a and b, and therefore also d, so |(Z/aZ ⊗Z Z/bZ)| ≤d.
To show Z/aZ⊗Z Z/bZ has size at least d, we create a Z-linear map from Z/aZ⊗Z Z/bZ
onto Z/dZ. Since d | a and d | b, we can reduce Z/aZ →Z/dZ and Z/bZ →Z/dZ in the
natural way. Consider the map Z/aZ × Z/bZ
B
−−→Z/dZ that is reduction mod d in each
factor followed by multiplication: B(x mod a, y mod b) = xy mod d. This is Z-bilinear, so
the universal mapping property of the tensor product says there is a (unique) Z-linear map
f : Z/aZ ⊗Z Z/bZ →Z/dZ making the diagram
Z/aZ ⊗Z Z/bZ
f

Z/aZ × Z/bZ
⊗
6
B
(
Z/dZ
commute, so f(x⊗y) = xy. In particular, f(x⊗1) = x, so f is onto. Therefore Z/aZ⊗ZZ/bZ
has size at least d, so the size is d and we’re done.
□
Example 4.2. The abelian group Z/3Z ⊗Z Z/5Z is 0. Such collapsing in a tensor product
often bothers people when they ﬁrst see it, but it’s means something concrete: each Z-
bilinear map B : Z/3Z × Z/5Z →A to an abelian group A is identically 0. That’s easy to
show directly: 3B(a, b) = B(3a, b) = B(0, b) = 0 and 5B(a, b) = B(a, 5b) = B(a, 0) = 0, so
B(a, b) is killed by 3Z + 5Z = Z. Thus B(a, b) is killed by 1, which means B(a, b) = 0.
In Z/aZ ⊗Z Z/bZ all tensors are elementary tensors: x ⊗y = xy(1 ⊗1) and a sum of
multiples of 1 ⊗1 is again a multiple, so Z/aZ ⊗Z Z/bZ = Z(1 ⊗1) = {x ⊗1 : x ∈Z}.
Note how the map f : Z/aZ ⊗Z Z/bZ →Z/dZ in the proof of Theorem 4.1 was created
from the bilinear map B : Z/aZ × Z/bZ →Z/dZ and the universal mapping property of
tensor products. To deﬁne a linear map out of M ⊗R N sending all elementary tensors
m ⊗n to speciﬁc places, always back up and start by deﬁning a bilinear map out of M × N
sending (m, n) to the place you want m⊗n to go. Make sure you show that map is bilinear!
Then the universal mapping property of the tensor product gives you a linear map out of
M ⊗R N sending m ⊗n to the place where (m, n) goes. As an anonymous student once
wrote, “If you don’t know what to do on a tensor products problem, build a well-chosen
bilinear map out of M × N because there’s basically nothing else you can do.”
Theorem 4.3. For ideals I and J in R, there is a unique R-module isomorphism
R/I ⊗R R/J ∼= R/(I + J)
where x ⊗y 7→xy. In particular, taking I = J = 0, R ⊗R R ∼= R by x ⊗y 7→xy.
For R = Z and nonzero I and J, this is Theorem 4.1.

<!-- page 15 -->
TENSOR PRODUCTS
15
Proof. Start with the function R/I × R/J →R/(I + J) given by (x mod I, y mod J) 7→
xy mod I + J. This is well-deﬁned and bilinear, so from the universal mapping property of
the tensor product we get a linear map f : R/I ⊗R R/J →R/(I + J) making the diagram
R/I ⊗R R/J
f

R/I × R/J
⊗
7
(x mod I,y mod J)7→xy mod I+J
'
R/(I + J)
commute, so f(x mod I ⊗y mod J) = xy mod I + J. To write down the inverse map, let
R →R/I⊗RR/J by r 7→r(1⊗1). This is linear, and when r ∈I the value is r⊗1 = 0⊗1 = 0.
Similarly, when r ∈J the value is 0. Therefore I + J is in the kernel, so we get a linear
map g: R/(I + J) →R/I ⊗R R/J by g(r mod I + J) = r(1 ⊗1) = r ⊗1 = 1 ⊗r.
To check f and g are inverses, a computation in one direction shows
f(g(r mod I + J)) = f(r ⊗1) = r mod I + J.
To show g(f(t)) = t for all t ∈R/I ⊗R R/J, we show each tensor is a scalar multiple of
1 ⊗1. An elementary tensor is x ⊗y = x1 ⊗y1 = xy(1 ⊗1), so sums of elementary tensors
are multiples of 1 ⊗1 and thus all tensors are multiples of 1 ⊗1. We have
g(f(r(1 ⊗1))) = rg(1 mod I + J) = r(1 ⊗1).
□
Remark 4.4. For ideals I and J, a few operations produce new ideals: I + J, I ∩J,
and IJ. The intersection I ∩J is the kernel of the linear map R →R/I ⊕R/J where
r 7→(r, r). Theorem 4.3 tells us I + J is the kernel of the linear map R →R/I ⊗R R/J
where r 7→r(1 ⊗1).
Theorem 4.5. For an ideal I in R and R-module M, there is a unique R-module isomor-
phism
(R/I) ⊗R M ∼= M/IM
such that r ⊗m 7→rm. In particular, taking I = (0), R ⊗R M ∼= M by r ⊗m 7→rm, so
R ⊗R R ∼= R as R-modules by r ⊗r′ 7→rr′.
Proof. We start with the bilinear map (R/I) × M →M/IM given by (r, m) 7→rm. From
the universal mapping property of the tensor product, we get a linear map f : (R/I)⊗RM →
M/IM where f(r ⊗m) = rm.
(R/I) ⊗R M
f

(R/I) × M
⊗
7
(r,m)7→rm
'
M/IM
To create an inverse map, start with the function M →(R/I) ⊗R M given by m 7→1 ⊗m.
This is linear in m (check!) and kills IM (generators for IM are products im for i ∈I and

<!-- page 16 -->
16
KEITH CONRAD
m ∈M, and 1⊗im = i⊗m = 0⊗m = 0), so it induces a linear map g: M/IM →(R/I)⊗RM
given by g(m) = 1 ⊗m.
To check f(g(m)) = m and g(f(t)) = t for all m ∈M/IM and t ∈(R/I) ⊗R M, we do
the ﬁrst one by a direct computation:
f(g(m)) = f(1 ⊗m) = 1 · m = m.
To show g(f(t)) = t for all t ∈M ⊗R N, we show all tensors in R/I ⊗R M are elementary.
An elementary tensor looks like r ⊗m = 1 ⊗rm, and a sum of tensors 1 ⊗mi is 1 ⊗P
i mi.
Thus all tensors look like 1 ⊗m. We have g(f(1 ⊗m)) = g(m) = 1 ⊗m.
□
Example 4.6. For every abelian group A, (Z/nZ) ⊗Z A ∼= A/nA as abelian groups by
m ⊗a 7→ma.
Remark 4.7. That R ⊗R M ∼= M by r ⊗m 7→rm says R-bilinear maps B out of R × M
can be identiﬁed with R-linear maps out of M, since B(r, m) = B(1, rm) by bilinearity and
B(1, −) is linear in the second component.
Remark 4.8. For an ideal I in R and R-module M there is an R-linear map I ⊗R M →
IM where i ⊗m 7→im, and it’s surjective (IM is spanned by all im, which are in the
image), but not necessarily injective! If R = Z, I = aZ, and M = Z/aZ for a ≥2 then
I ⊗R M = (aZ) ⊗Z (Z/aZ) ∼= Z/aZ by (ax) ⊗(y mod a) 7→xy mod a, but IM = {0}.
In this section so far, M or N in M ⊗R N has been R or R/I. Such a module contains
1 or 1, making all tensors in M ⊗R N elementary. Don’t be misled. Most tensors are not
elementary, and don’t think m⊗n = mn(1⊗1); 1 is not in a general module, so 1⊗1 usually
doesn’t make sense.12 The next theorem, which justiﬁes the discussion in the introduction
about bases for tensor products of free modules, will let us construct nonelementary tensors.
Theorem 4.9. If F and F ′ are free R-modules, with respective bases {ei}i∈I and {e′
j}j∈J,
then F ⊗R F ′ is a free R-module with basis {ei ⊗e′
j}(i,j)∈I×J.
Proof. The result is clear if F or F ′ is 0, so let them both be nonzero modules (hence R ̸= 0
and I and J are nonempty). By Theorem 3.3, {ei ⊗e′
j} spans F ⊗R F ′ as an R-module.
To show this spanning set is linearly independent, suppose P
i,j cijei ⊗e′
j = 0, where
all but ﬁnitely many cij are 0. We want to show every cij is 0. Pick two basis vectors
ei0 and e′
j0 in F and F ′. To show the coeﬃcient ci0j0 is 0, consider the bilinear function
F × F ′ →R by (v, w) 7→vi0wj0, where v = P
i viei and w = P
j wje′
j. (Here vi and wj are
coordinates in R.) By the universal mapping property of tensor products there is a linear
map f0 : F ⊗R F ′ →R such that f0(v ⊗w) = vi0wj0 on each elementary tensor v ⊗w.
F ⊗R F ′
f0

F × F ′
⊗
9
(v,w)7→ai0bj0
& R
12Each part of an elementary tensor in M ⊗R N belongs to M or to N.

<!-- page 17 -->
TENSOR PRODUCTS
17
In particular, f0(ei0 ⊗e′
j0) = 1 and f0(ei ⊗e′
j) = 0 for (i, j) ̸= (i0, j0). Applying f0 to the
equation P
i,j cijei ⊗e′
j = 0 in F ⊗R F ′ tells us ci0j0 = 0 in R. Since i0 and j0 are arbitrary,
all the coeﬃcients are 0.
□
Theorem 4.9 can be interpreted in terms of bilinear maps out of F × F ′. It says that all
bilinear maps out of F × F ′ are determined by their values on the pairs (ei, e′
j), and that
each assignment of values to these pairs extends in a unique way to a bilinear map out of
F × F ′. (The uniqueness of the extension is connected to the linear independence of the
elementary tensors ei ⊗e′
j.) This is the bilinear analogue of the existence and uniqueness
of a linear extension of a function from a basis of a free module to the whole module.
Example 4.10. Let K be a ﬁeld and V and W be nonzero K-vector spaces with ﬁnite
dimension. There are bases for V and W, say {e1, . . . , em} for V and {f1, . . . , fn} for W.
Theorem 4.9 shows each element of V ⊗K W is P
i,j cijei ⊗fj for unique cij ∈K. This
justiﬁes the description of tensor products on the ﬁrst page using bases.
Since all nonzero vector spaces have a (possibly inﬁnite) basis and Theorem 4.9 does not
assume the bases are ﬁnite, V ⊗K W ̸= 0 when V and W are arbitrary (possibly inﬁnite-
dimensional) nonzero K-vector spaces. Is that a special property of ﬁelds: when R is a
commutative ring such that M ⊗R N ̸= 0 for all nonzero R-modules M and N, must R be a
ﬁeld? If R is a domain, the answer is yes: if R is domain that’s not a ﬁeld then its fraction
ﬁeld K is bigger than R, so K and K/R are nonzero R-modules such that K ⊗R (K/R) = 0
(the case R = Z is in Example 3.6). When R might not be a domain, then like ﬁelds R has
just one maximal ideal (R is a local ring): if m and n are diﬀerent maximal ideals in R then
R/m and R/n are nonzero while R/m ⊗R R/n ∼= R/(m + n) = R/R = 0 by Theorem 4.3. A
characterization of the R where nonzero R-modules always have a nonzero tensor product
is at https://math.stackexchange.com/questions/3593619/.
Example 4.11. For R ̸= 0, let F and F ′ be ﬁnite free R-modules of rank ≥2 with bases
{e1, . . . , em} and {e′
1, . . . , e′
n}. In F ⊗R F ′, e1 ⊗e′
1 + e2 ⊗e′
2 is a tensor that is provably
not an elementary tensor. An elementary tensor in F ⊗R F ′ has the form
(4.1)
m
X
i=1
aiei ⊗
n
X
j=1
bje′
j =
m
X
i=1
n
X
j=1
aibjei ⊗e′
j.
The set of all ei ⊗e′
j is a basis of F ⊗R F ′ (Theorem 4.9), so if e1 ⊗e′
1 + e2 ⊗e′
2 equals (4.1)
for some ai and bj, then by comparing coeﬃcients
a1b1 = 1,
a1b2 = 0,
a2b1 = 0,
a2b2 = 1.
Since a1b1 = 1 and a2b2 = 1, a1 and b2 are invertible, contradicting a1b2 = 0. So e1 ⊗e′
1 +
e2 ⊗e′
2 is not an elementary tensor. Similarly, e1 ⊗e′
2 +e2 ⊗e′
1 is not an elementary tensor.13
Example 4.12. For R ̸= 0, R[X] ⊗R R[Y ] is a free R-module with basis {Xi ⊗Y j}i,j≥0,
so R[X] ⊗R R[Y ] is isomorphic to R[X, Y ] as R-modules by P cij(Xi ⊗Y j) 7→P cijXiY j.
More generally, R[X1, . . . , Xk] ∼= R[X]⊗k as R-modules with Xi corresponding to the tensor
1⊗· · ·⊗X ⊗· · ·⊗1 where X is in the ith position. The diﬀerence between ordinary products
and tensor products is like the diﬀerence between multiplying one-variable polynomials as
f(T)g(T) and as f(X)g(Y ).
13If F ′ = F, then (4.1) shows a necessary condition for Pn
i,j=1 cijei ⊗ej to be elementary is ciicjj = cijcji
for all i and j. When R = K is a ﬁeld this condition is also suﬃcient, so in Kn ⊗K Kn the elementary
tensors are characterized among all tensors by polynomial equations of degree 2. For more on this, see [9].

<!-- page 18 -->
18
KEITH CONRAD
Example 4.13. We return to Example 2.1. For v and w in Rn, B(v, w) = vw⊤∈Mn(R).
This is R-bilinear, so there is an R-linear map L: Rn ⊗R Rn →Mn(R) where L(v ⊗w) =
vw⊤for all elementary tensors v ⊗w. In Example 2.1 we saw that, for n ≥2, the image
of B in Mn(R) is not closed under addition. In particular, B(e1, e1) + B(e2, e2) is not of
the form B(v, w). This is a typical “problem” with bilinear maps. However, using tensor
products, B(e1, e1) + B(e2, e2) = L(e1 ⊗e1) + L(e2 ⊗e2) = L(e1 ⊗e1 + e2 ⊗e2), which is a
value of L.
In fact, L is an isomorphism. To prove this we use bases. By Theorem 4.9, Rn ⊗R Rn
has the basis {ei ⊗ej}. The value L(ei ⊗ej) = eie⊤
j is the matrix with 1 in the (i, j) entry
and 0 elsewhere, and these matrices are the standard basis of Mn(R). Therefore L sends a
basis to a basis, so it is an isomorphism of R-vector spaces.
Theorem 4.14. Let F be a free R-module with basis {ei}i∈I. For k ≥1, the kth tensor
power F ⊗k is free with basis {ei1 ⊗· · · ⊗eik}(i1,...,ik)∈Ik.
Proof. This is similar to the proof of Theorem 4.9.
□
Theorem 4.15. If M is an R-module and F is a free R-module with basis {ei}i∈I, then
every element of M ⊗R F has a unique representation in the form P
i∈I mi ⊗ei, where all
but ﬁnitely many mi equal 0.
Proof. This is vacuously true if F = 0 (I = ∅), so take F ̸= 0 (thus R ̸= 0). Using M as
a spanning set for M and {ei}i∈I as a spanning set for F, by Theorem 3.3 each element
of M ⊗R F is a linear combination of elementary tensors mi ⊗ei, where mi ∈M. Since
r(mi⊗ei) = (rmi)⊗ei, we can write every tensor in M ⊗R F as a sum of elementary tensors
of the form mi ⊗ei. So we have a surjective linear map f : L
i∈I M 7→M ⊗R F given by
f((mi)i∈I) = P
i∈I mi ⊗ei. (All but ﬁnitely many mi are 0, so the sum makes sense.)
To create an inverse to f, consider the function M × F →L
i∈I M where (m, P
i riei) 7→
(rim)i∈I. This function is bilinear (check!), so there is a linear map g: M ⊗R F →L
i∈I M
where g(m ⊗P
i riei) = (rim)i∈I.
To check f(g(t)) = t for all t in M ⊗R F, we can’t expect that all tensors in M ⊗R F are
elementary (an idea used in the proofs of Theorems 4.3 and 4.5), but we only need to check
f(g(t)) = t when t is an elementary tensor since f and g are additive and the elementary
tensors additively span M ⊗R F. (We will use this kind of argument a lot to reduce the
proof of an identity involving functions of all tensors to the case of elementary tensors even
though most tensors are not themselves elementary. The point is all tensors are sums of
elementary tensors and the formula we want to prove will involve additive functions.) An
elementary tensor looks like m ⊗P
i riei, and
f
 
g
 
m ⊗
X
i∈I
riei
!!
= f((rim)i∈I)
=
X
i∈I
rim ⊗ei
=
X
i∈I
m ⊗riei
= m ⊗
X
i∈I
riei.

<!-- page 19 -->
TENSOR PRODUCTS
19
These sums have ﬁnitely many terms (ri = 0 for all but ﬁnitely many i), from the deﬁnition
of direct sums. Thus f(g(t)) = t for all t ∈M ⊗R F.
For the composition in the other order,
g(f((mi)i∈I)) = g
 X
i∈I
mi ⊗ei
!
=
X
i∈I
g(mi ⊗ei) =
X
i∈I
(. . . , 0, mi, 0, . . . ) = (mi)i∈I.
Now that we know M ⊗R F ∼= L
i∈I M, with P
i∈I mi ⊗ei corresponding to (mi)i∈I, the
uniqueness of coordinates in the direct sum implies the sum representation P
i∈I mi ⊗ei is
unique.
□
Example 4.16. For a ring S ⊃R, elements of S ⊗R R[X] have unique expressions of the
form P
n≥0 sn ⊗Xn, so S ⊗R R[X] ∼= S[X] as R-modules by P
n≥0 sn ⊗Xn 7→P
n≥0 snXn.
Remark 4.17. When f and g are additive functions you can check f(g(t)) = t for all
tensors t by only checking it on elementary tensors, but it would be wrong to think you
have proved injectivity of a linear map f : M ⊗R N →P by only looking at elementary
tensors.14 That is, if f(m ⊗n) = f(m′ ⊗n′) ⇒m ⊗n = m′ ⊗n′, then it is not always true
that f(t) = f(t′) ⇒t = t′ for all t and t′ in M ⊗R N, since injectivity of a linear map is
not an additive property.15 This is the main reason that proving that a linear map out of
a tensor product is injective can require technique. As a special case, if you want to prove
a linear map out of a tensor product is an isomorphism, it might be easier to construct an
inverse map and check the composite in both orders is the identity than to show the original
map is injective and surjective.
Theorem 4.18. If M is a nonzero ﬁnitely generated R-module then M⊗k ̸= 0 for all k.
Proof. Necessarily R ̸= 0.
Write M = Rx1 + · · · + Rxd for minimal d ≥1.
Set N =
Rx1+· · ·+Rxd−1 (N = 0 if d = 1), so M = N+Rxd and xd ̸∈N. Set I = {r ∈R : rxd ∈N},
so I is an ideal in R and 1 ̸∈I, so I is a proper ideal. When we write an element m of M
in the form n + rx with n ∈N and r ∈R, n and r may not be well-deﬁned from m but
the value of r mod I is well-deﬁned: if n + rx = n′ + r′x then (r −r′)x = n′ −n ∈N, so
r ≡r′ mod I. Therefore the function Mk →R/I given by
(n1 + r1xd, . . . , nk + rkxd) 7→r1 · · · rd mod I
is well-deﬁned and multilinear (check!), so there is an R-linear map M⊗k →R/I such that
xd ⊗· · · ⊗xd
|
{z
}
k terms
7→1 mod I ̸= 0. That shows M⊗k ̸= 0.
□
Example 4.19. By Theorem 4.1, (Z/aZ)⊗2 ∼= Z/aZ as Z-modules.
Example 4.20. Tensor powers of a non-ﬁnitely generated module could vanish: (Q/Z)⊗2 =
0 as a Z-module (Example 3.6). This example is interesting because Q/Z is the union
of cyclic subgroups (1/a)Z/Z for all a ≥1, and each (1/a)Z/Z has a nonzero tensor
square:
((1/a)Z/Z)⊗2 ∼= (1/a)Z/Z by an argument like the one used to prove Theo-
rem 4.1. That ((1/a)Z/Z)⊗2 ̸= 0 while (Q/Z)⊗2 = 0 reﬂects something about bilinear
maps: there are Z-bilinear maps out of (1/a)Z/Z × (1/a)Z/Z that are not identically
14Unless every tensor in M ⊗R N is elementary, which is usually not the case.
15See Example 5.19 for an example of a linear map M ⊗R N →P that is not injective on M ⊗R N and
is injective on the elementary tensors in M ⊗R N.

<!-- page 20 -->
20
KEITH CONRAD
0, but every Z-bilinear map out of Q/Z × Q/Z is identically 0.
For example, the Z-
bilinear map (1/5)Z/Z × (1/5)Z/Z →Z/5Z given by (x/5, y/5) 7→xy mod 5 is nonzero
at (1/5, 1/5), but each bilinear map B out of Q/Z × Q/Z must vanish at (1/5, 1/5)
since B(1/5, 1/5) = B(1/5, 5/25) = B(5/5, 1/25) = B(1, 1/25) = B(0, 1/25) = 0. Thus
(1/5) ⊗(1/5) ̸= 0 in ((1/5)Z/Z)⊗2 while (1/5) ⊗(1/5) = 0 in (Q/Z)⊗2. The lesson is that
an elementary tensor requires context (which tensor product module is it in?).
The rest of this section is about tensor products when R is a domain, so R ̸= 0.
Theorem 4.21. Let R be a domain with fraction ﬁeld K and V be a K-vector space. There
is an R-module isomorphism K ⊗R V ∼= V , where x ⊗v 7→xv.
By Theorem 4.5, K ⊗K V ∼= V by x ⊗v 7→xv, but Theorem 4.21 is diﬀerent because the
scalars in the tensor product are from R.
Proof. Multiplication is a function K × V →V . It is R-bilinear, so the universal mapping
property of tensor products says there is an R-linear function f : K ⊗R V →V where
f(x ⊗v) = xv on elementary tensors. That says the diagram
K ⊗R V
f

K × V
⊗
8
& V
commutes, where the lower diagonal map is scalar multiplication. Since f(1 ⊗v) = v, f is
onto.
To show f is one-to-one, ﬁrst we show every tensor in K ⊗R V is elementary with 1 in
the ﬁrst component. For an elementary tensor x ⊗v, write x = a/b with a and b in R, and
b ̸= 0. Then
x ⊗v = a
b ⊗v = 1
b ⊗av = 1
b ⊗ab
b v = 1
bb ⊗a
b v = 1 ⊗a
b v = 1 ⊗xv.
Notice how we moved x ∈K across ⊗even though x need not be in R: we used K-scaling
in V to create b and 1/b on the right side of ⊗and bring b across ⊗from right to left, which
cancels 1/b on the left side of ⊗. This has the eﬀect of moving 1/b from left to right.
Thus all elementary tensors in K ⊗R V have the form 1⊗v for some v ∈V , so by adding,
every tensor is 1 ⊗v for some v. Now we can show f has trivial kernel: if f(t) = 0 then,
writing t = 1 ⊗v, we get v = 0, so t = 1 ⊗0 = 0.
□
Example 4.22. For V = K, K ⊗R K ∼= K as R-modules by x ⊗y 7→xy on elementary
tensors. For example, Q ⊗Z Q ∼= Q. If a ﬁeld K is inside a ﬁeld L then we can view L as a
K-vector space and K ⊗R L ∼= L as R-modules, e.g., Q ⊗Z R ∼= R as Z-modules.
Theorem 4.23. Let R be a domain with fraction ﬁeld K and V be a K-vector space. For
each nonzero R-module M inside K, M ⊗R V ∼= V as R-modules by m ⊗v 7→mv. In
particular, I ⊗R K ∼= K as R-modules for every nonzero ideal I in R.

<!-- page 21 -->
TENSOR PRODUCTS
21
Proof. The proof is largely like that for the previous theorem.16
Multiplication gives a
function M × V →V that is R-bilinear, so we get an R-linear map f : M ⊗R V →V where
f(m ⊗v) = mv. To show f is onto, we can’t look at f(1 ⊗v) as in the previous proof, since
1 is usually not in M. Instead we can just pick a nonzero m ∈M. Then for all v ∈V ,
f(m ⊗(1/m)v) = v.
To show f is injective, ﬁrst we show all tensors in M ⊗R V are elementary. This sounds
like our previous proof that all tensors in K ⊗R V are elementary, but M need not be K,
so our manipulations need to be more careful than before. (We can’t write (a/b) ⊗v as
(1/b) ⊗av, since 1/b usually won’t be in M.) Given a ﬁnite set of nonzero elementary
tensors mi ⊗vi, each mi is nonzero. Write mi = ai/bi with nonzero ai and bi in R. Let
a ∈R be the product of the ai’s and ci = a/ai ∈R, so a = aici = bicimi ∈M. In V we can
write vi = biciwi for some wi ∈V , so
mi ⊗vi = mi ⊗biciwi = bicimi ⊗wi = a ⊗wi.
The sum of these elementary tensors is a ⊗P
i wi, which is elementary.
Now suppose t ∈M ⊗R V is in the kernel of f. All tensors in M ⊗R V are elementary,
so we can write t = m ⊗v. Then f(t) = 0 ⇒mv = 0 in V , so m = 0 or v = 0, and thus
t = m ⊗v = 0.
□
Example 4.24. Let R = Z[
√
10] and K = Q(
√
10). The ideal I = (2,
√
10) in R is not
principal, so I ̸∼= R as R-modules. However, I ⊗R K ∼= R ⊗R K as R-modules since both
are isomorphic to K.
Theorem 4.25. Let R be a domain and F and F ′ be free R-modules. If x and x′ are
nonzero in F and F ′, then x ⊗x′ ̸= 0 in F ⊗R F ′.
Proof. If we were working with vector spaces this would be trivial, since x and x′ are each
part of a basis of F and F ′, so x ⊗x′ is part of a basis of F ⊗R F ′ (Theorem 4.9). In a
free module over a commutative ring, a nonzero element need not be part of a basis, so our
proof needs to be a little more careful. We’ll still uses bases, just not ones that necessarily
include x or x′.
Pick a basis {ei} for F and {e′
j} for F ′. Write x = P
i aiei and x′ = P
j a′
je′
j. Then
x ⊗x′ = P
i,j aia′
jei ⊗e′
j in F ⊗R F ′. Since x and x′ are nonzero, they each have some
nonzero coeﬃcient, say ai0 and a′
j0. Then ai0a′
j0 ̸= 0 since R is a domain, so x ⊗x′ has a
nonzero coordinate in the basis {ei ⊗e′
j} of F ⊗R F ′. Thus x ⊗x′ ̸= 0.
□
Remark 4.26. There is always a counterexample for Theorem 4.25 when R is not a domain.
Let F = F ′ = R and say ab = 0 with a and b nonzero in R. In R ⊗R R we have a ⊗b =
ab(1 ⊗1) = 0.
Theorem 4.27. Let R be a domain with fraction ﬁeld K and V be a K-vector space.
(1) For all R-modules M, there is an R-module isomorphism V ⊗RM ∼= V ⊗R(M/Mtor),
where Mtor is the torsion submodule of M.
(2) For R-modules M, if M is torsion then V ⊗R M = 0 and if M is not torsion and
V is nonzero then V ⊗R M ̸= 0.
(3) If M is an R-module and N is a submodule such that M/N is a torsion R-module
then V ⊗R N ∼= V ⊗R M as R-modules by v ⊗n 7→v ⊗n.
16Theorem 4.21 is just a special case of Theorem 4.23, but we worked it out separately ﬁrst since the
technicalities are simpler.

<!-- page 22 -->
22
KEITH CONRAD
Proof. (1) The map V × M →V ⊗R (M/Mtor) given by (v, m) 7→v ⊗m is R-bilinear, so
there is an R-linear map f : V ⊗R M →V ⊗R (M/Mtor) where f(v ⊗m) = v ⊗m.
To go the other way, the canonical R-bilinear map V ×M
⊗
−−→V ⊗RM vanishes at (v, m)
for m ∈Mtor: if rm = 0 for r ̸= 0 then v ⊗m = r(v/r) ⊗m = v/r ⊗rm = v/r ⊗0 = 0.
Thus we get an induced R-bilinear map V ×(M/Mtor) →V ⊗R M given by (v, m) 7→v ⊗m.
(The point is that an elementary tensor v ⊗m in V ⊗R M only depends on m through its
coset mod Mtor.) The universal mapping property of the tensor product now gives us an
R-linear map g: V ⊗R (M/Mtor) →V ⊗R M where g(v ⊗m) = v ⊗m.
The composites g ◦f and f ◦g are both R-linear and are the identity on elementary
tensors, so they are the identity on all tensors and thus f and g are inverse isomorphisms.
(2) It is immediate from (1) that V ⊗R M = 0 if M is a torsion module, since V ⊗R M ∼=
V ⊗R (M/Mtor) = V ⊗R 0 = 0. We could also prove this in a direct way, by showing all
elementary tensors in V ⊗R M are 0: for v ∈V and m ∈M, let rm = 0 with r ̸= 0, so
v ⊗m = r(v/r) ⊗m = v/r ⊗rm = v/r ⊗0 = 0. Thus all tensors in V ⊗R M are 0.
To show V ⊗R M ̸= 0 when M is not torsion and V ̸= {0}, from the isomorphism
V ⊗R M ∼= V ⊗R (M/Mtor), we replace M with M/Mtor and are reduced to the case when
M is torsion-free. For torsion-free M we will create a nonzero R-module and an R-linear
map onto it from V ⊗R M, so V ⊗R M ̸= 0. This will require a fair bit of work (as it usually
does to prove a tensor product of R-modules doesn’t vanish when they may not be free).
We will build an R-module KM of formal products xm with x ∈K and m ∈M. To
make this precise, use equivalence classes of ordered pairs in the same way that a fraction
ﬁeld is built out of a domain. On the product set K × M, deﬁne an equivalence relation by
(a/b, m) ∼(c/d, n) ⇐⇒adm = bcn in M.
Here a, b, c, and d are in R and b and d are not 0. The proof that this relation is well-deﬁned
(independent of the choice of numerators and denominators) and transitive requires M be
torsion-free (check!). As an example, (0, m) ∼(0, 0) for all m ∈M.
Deﬁne KM = (K × M)/ ∼and write the equivalence class of (x, m) as x · m. Give KM
the addition and K-scaling formulas
a
b · m + c
d · n = 1
bd · (adm + bcn),
x(y · m) = (xy) · m.
Check these operations on KM are well-deﬁned and make KM into a K-vector space (so
in particular an R-module). The function M →KM given by m 7→1 · m is injective: if
1 · m = 1 · m′ then (1, m) ∼(1, m′), so m = m′ in M. Thus KM ̸= 0 since M ̸= 0.
Pick v0 ̸= 0 in V and extend it to a basis of V . Using this basis, there is a K-linear
ϕ: V →K with ϕ(v0) = 1. The function V × M →KM where (v, m) 7→ϕ(v) · m is R-
bilinear and onto (since ϕ is onto), so there is a surjective R-linear map V ⊗R M
f
−−→KM
such that f(v ⊗m) = ϕ(v) · m. Since KM ̸= 0 we have V ⊗R M ̸= 0.
(3) Since N ⊂M, there is a natural R-bilinear map V × N →V ⊗R M, namely (v, n) 7→
v⊗n. So we get automatically an R-linear map f : V ⊗RN →V ⊗RM where f(v⊗n) = v⊗n
on elementary tensors. (This is not the identity: on the left v ⊗n is in V ⊗R N and on the
right v ⊗n is in V ⊗R M.)
To get a map inverse to f, we can’t have V ⊗R M →V ⊗R N by v ⊗m 7→v ⊗m, since
m may not be in N. The trick to use is that some nonzero R-multiple of m is in N, since
M/N is a torsion module: let V × M →V ⊗R N by (v, m) 7→(1/r)v ⊗rm where rm ∈N
for r ∈R −{0}. (Don’t try to simplify (1/r)v ⊗rm by moving r through ⊗from right to

<!-- page 23 -->
TENSOR PRODUCTS
23
left, since rm is in N but m usually is not.) We need to check (1/r)v ⊗rm is independent
of the choice of r ̸= 0 such that rm ∈N. If r′m ∈N with r′ ∈R −{0}, then
1
r′ v ⊗r′m = r
rr′ v ⊗r′m = 1
rr′ v ⊗rr′m = 1
rr′ v ⊗r′(rm) = r′
rr′ v ⊗rm = 1
rv ⊗rm.
Set V × M →V ⊗R N by (v, m) 7→(1/r)v ⊗rm where r ∈R −{0} satisﬁes rm ∈N. This
is well-deﬁned. Check it is R-bilinear, so we get an R-linear map g: V ⊗R M →V ⊗R N
where g(v ⊗m) = (1/r)v ⊗rm for rm ∈N with r ̸= 0. Check f(g(v ⊗m)) = v ⊗m and
g(f(v ⊗n)) = v ⊗n, so f ◦g and g ◦f are both the identity maps by additivity.
□
Corollary 4.28. With notation as in Theorem 4.27, v ⊗m = 0 in V ⊗R M if and only if
v = 0 or m ∈Mtor. In particular, Mtor = ker(M →K ⊗R M) where m 7→1 ⊗m.
Proof. If v = 0 then v ⊗m = 0 ⊗m = 0. If m ∈Mtor, with rm = 0 for some nonzero r ∈R,
then v ⊗m = (v/r)r ⊗m = (v/r) ⊗rm = (v/r) ⊗0 = 0.
Conversely, if v⊗m = 0 in V ⊗RM we will prove v = 0 or m ∈Mtor by assuming v ̸= 0 and
showing m ∈Mtor. By the natural R-linear map V ⊗R M →V ⊗R (M/Mtor) in the proof of
Theorem 4.27(1), from v⊗m = 0 in V ⊗RM we get v⊗m = 0 in V ⊗R(M/Mtor). From v ̸= 0
and M/Mtor being torsion-free, by the proof of Theorem 4.27(2) there is a K-linear map
ϕ: V →K such that ϕ(v) = 1 and there is an R-linear map V ⊗R (M/Mtor) →K(M/Mtor)
where v ⊗m 7→ϕ(v) · m = 1 · m, so 1 · m = 0 in K(M/Mtor). Thus m = 0 in M/Mtor by
the deﬁnition of equality in K(M/Mtor) and its zero element being 0 · 0, so m ∈Mtor.
□
Example 4.29. If x ∈R× and y/π is irrational, then x⊗(y mod πZ) ̸= 0 in R⊗Z (R/πZ)
since (R/πZ)tor = πQ/πZ. This is used in the modern form of Dehn’s solution to Hilbert’s
3rd problem, but Dehn’s own work was long before tensor products of Z-modules.
By
Theorem 4.27(1), R ⊗Z (R/πZ) ∼= R ⊗Z (R/πZ)/(πQ/πZ) ∼= R ⊗Z (R/πQ) as Z-modules.
5. General Properties of Tensor Products
The direct sum isomorphisms M ⊕N ∼= N ⊕M and (M ⊕N) ⊕P ∼= M ⊕(N ⊕P) have
tensor product analogues: M ⊗R N ∼= N ⊗R M and (M ⊗R N) ⊗R P ∼= M ⊗R (N ⊗R P).
Furthermore, ⊗R distributes over ⊕: M ⊗R (N ⊕P) ∼= (M ⊗R N) ⊕(M ⊗R P). How these
isomorphisms work is more important than their existence. Let’s begin.
Theorem 5.1. There is a unique R-module isomorphism M ⊗R N →N ⊗R M where
m ⊗n 7→n ⊗m.
Proof. We want to create a linear map M ⊗R N →N ⊗R M sending m ⊗n to n ⊗m. To
do this, we back up and start oﬀwith a map out of M × N to the desired target module
N ⊗R M. Deﬁne M × N →N ⊗R M by (m, n) 7→n ⊗m. This is a bilinear map since
n ⊗m is bilinear in m and n. Therefore by the universal mapping property of the tensor
product, there is a unique linear map f : M ⊗R N →N ⊗R M such that f(m ⊗n) = n ⊗m
on elementary tensors: the diagram
M ⊗R N
f

M × N
⊗
8
(m,n)7→n⊗m
&
N ⊗R M

<!-- page 24 -->
24
KEITH CONRAD
commutes.
Running through the above argument with the roles of M and N interchanged, there is a
unique linear map g: N ⊗R M →M ⊗R N where g(n ⊗m) = m ⊗n on elementary tensors.
We will show f and g are inverses of each other.
To show f(g(t)) = t for all t ∈N ⊗R M, it suﬃces to check this when t is an elementary
tensor, since both sides are R-linear (or even just additive) in t and N ⊗R M is spanned
by its elementary tensors: f(g(n ⊗m)) = f(m ⊗n) = n ⊗m. Therefore f(g(t)) = t for all
t ∈N ⊗R M. The proof that g(f(t)) = t for all t ∈M ⊗R N is similar. We have shown f
and g are inverses of each other, so f is an R-module isomorphism.
□
Theorem 5.2. There is a unique R-module isomorphism (M ⊗RN)⊗RP ∼= M ⊗R(N ⊗RP)
where (m ⊗n) ⊗p 7→m ⊗(n ⊗p).
Proof. By Theorem 3.3, (M ⊗R N) ⊗R P is linearly spanned by all (m ⊗n) ⊗p and M ⊗R
(N ⊗R P) is linearly spanned by all m ⊗(n ⊗p). Therefore linear maps out of these two
modules are determined by their values on these17 elementary tensors. So there is at most
one linear map (M ⊗RN)⊗RP →M ⊗R(N ⊗RP) with the eﬀect (m⊗n)⊗p 7→m⊗(n⊗p),
and likewise in the other direction.
To create such a linear map (M ⊗R N) ⊗R P →M ⊗R (N ⊗R P), consider the function
M × N × P →M ⊗R (N ⊗R P) given by (m, n, p) 7→m ⊗(n ⊗p). Since m ⊗(n ⊗p) is
trilinear in m, n, and p, for each p we get a bilinear map bp : M × N →M ⊗R (N ⊗R P)
where bp(m, n) = m ⊗(n ⊗p), which induces a linear map fp : M ⊗R N →M ⊗R (N ⊗R P)
such that fp(m ⊗n) = m ⊗(n ⊗p) on all elementary tensors m ⊗n in M ⊗R N.
Now we consider the function (M ⊗R N) × P →M ⊗R (N ⊗R P) given by (t, p) 7→fp(t).
This is bilinear! First, it is linear in t with p ﬁxed, since each fp is a linear function. Next
we show it is linear in p with t ﬁxed:
fp+p′(t) = fp(t) + fp′(t) and frp(t) = rfp(t)
for all p, p′, and r. Both sides of these identities are additive in t, so to check them it suﬃces
to check the case when t = m ⊗n:
fp+p′(m ⊗n) = (m ⊗n) ⊗(p + p′)
= (m ⊗n) ⊗p + (m ⊗n) ⊗p′
= fp(m ⊗n) + fp′(m ⊗n)
= (fp + fp′)(m ⊗n).
That frp(m ⊗n) = rfp(m ⊗n) is left to the reader. Since fp(t) is bilinear in p and t,
the universal mapping property of the tensor product tells us there is a unique linear map
f : (M ⊗R N) ⊗R P →M ⊗R (N ⊗R P) such that f(t ⊗p) = fp(t). Then f((m ⊗n) ⊗p) =
fp(m ⊗n) = m ⊗(n ⊗p), so we have found a linear map with the desired values on the
tensors (m ⊗n) ⊗p.
Similarly, there is a linear map g: M⊗R(N⊗RP) →(M⊗RN)⊗RP where g(m⊗(n⊗p)) =
(m⊗n)⊗p. Easily f(g(m⊗(n⊗p))) = m⊗(n⊗p) and g(f((m⊗n)⊗p)) = (m⊗n)⊗p. Since
these particular tensors linearly span the two modules, these identities extend by linearity
(f and g are linear) to show f and g are inverse functions.
□
17A general elementary tensor in (M ⊗R N) ⊗R P is not (m ⊗n) ⊗p, but t ⊗p where t ∈M ⊗R N and
t might not be elementary itself. Similarly, elementary tensors in M ⊗R (N ⊗R P) are more general than
m ⊗(n ⊗p).

<!-- page 25 -->
TENSOR PRODUCTS
25
Theorem 5.3. There is a unique R-module isomorphism
M ⊗R (N ⊕P) ∼= (M ⊗R N) ⊕(M ⊗R P)
where m ⊗(n, p) 7→(m ⊗n, m ⊗p).
Proof. Instead of directly writing down an isomorphism, we will put to work the essential
uniqueness of solutions to a universal mapping problem by showing (M ⊗R N) ⊕(M ⊗R P)
has the universal mapping property of the tensor product M ⊗R (N ⊕P). Therefore by
abstract nonsense these modules must be isomorphic. That there is an isomorphism whose
eﬀect on elementary tensors in M ⊗R(N ⊕P) is as indicated in the statement of the theorem
will fall out of our work.
For (M ⊗RN)⊕(M ⊗RP) to be a tensor product of M and N ⊕P, it needs a bilinear map
to it from M × (N ⊕P). Let b: M × (N ⊕P) →(M ⊗R N) ⊕(M ⊗R P) by b(m, (n, p)) =
(m ⊗n, m ⊗p).
This function is bilinear.
We verify the additivity of b in its second
component, leaving the rest to the reader:
b(m, (n, p) + (n′, p′)) = b(m, (n + n′, p + p′))
= (m ⊗(n + n′), m ⊗(p + p′))
= (m ⊗n + m ⊗n′, m ⊗p + m ⊗p′)
= (m ⊗n, m ⊗p) + (m ⊗n′, m ⊗p′)
= b(m, (n, p)) + b(m, (n′, p′)).
To show (M⊗RN)⊕(M⊗RP) and b have the universal mapping property of M⊗R(N⊕P)
and ⊗, let B : M × (N ⊕P) →Q be a bilinear map. We seek an R-linear map L making
(5.1)
(M ⊗R N) ⊕(M ⊗R P)
L

M × (N ⊕P)
b
5
B
* Q
commute. Being linear, L would be determined by its values on the direct summands, and
these values would be determined by the values of L on all pairs (m ⊗n, 0) and (0, m ⊗p)
by additivity. These values are forced by commutativity of (5.1) to be
L(m⊗n, 0) = L(b(m,(n, 0))) = B(m,(n, 0)) and L(0, m⊗p) = L(b(m,(0, p))) = B(m,(0, p)).
To construct L, the above formulas suggest the maps M × N →Q and M × P →Q
given by (m, n) 7→B(m, (n, 0)) and (m, p) 7→B(m, (0, p)). Both are bilinear, so there are
R-linear maps M ⊗R N
L1
−−−→Q and M ⊗R P
L2
−−−→Q where
L1(m ⊗n) = B(m, (n, 0)) and L2(m ⊗p) = B(m, (0, p)).
Deﬁne L on (M ⊗R N) ⊕(M ⊗R P) by L(t1, t2) = L1(t1) + L2(t2). (Notice we are deﬁning
L not just on ordered pairs of elementary tensors, but on all pairs of tensors. We need L1
and L2 to be deﬁned on the whole tensor product modules M ⊗R N and M ⊗R P.) The

<!-- page 26 -->
26
KEITH CONRAD
map L is linear since L1 and L2 are linear, and (5.1) commutes:
L(b(m, (n, p))) = L(b(m, (n, 0) + (0, p)))
= L(b(m, (n, 0)) + b(m, (0, p)))
= L((m ⊗n, 0) + (0, m ⊗p)) by the deﬁnition of b
= L(m ⊗n, m ⊗p)
= L1(m ⊗n) + L2(m ⊗p) by the deﬁnition of L
= B(m, (n, 0)) + B(m, (0, p))
= B(m, (n, 0) + (0, p))
= B(m, (n, p)).
Now that we’ve shown (M ⊗R N) ⊕(M ⊗R P) and the bilinear map b have the universal
mapping property of M ⊗R (N ⊕P) and the canonical bilinear map ⊗, there is a unique
linear map f making the diagram
(M ⊗R N) ⊕(M ⊗R P)
f

M × (N ⊕P)
b
5
⊗
)
M ⊗R (N ⊕P)
commute, and f is an isomorphism of R-modules because it transforms one solution of a
universal mapping problem into another. Taking (m, (n, p)) around the diagram both ways,
f(b(m, (n, p))) = f(m ⊗n, m ⊗p) = m ⊗(n, p).
Therefore the inverse of f is an isomorphism M ⊗R (N ⊕P) →(M ⊗R N) ⊕(M ⊗R P)
with the eﬀect m ⊗(n, p) 7→(m ⊗n, m ⊗p). We look at the inverse because the theorem is
saying something about an isomorphism out of M ⊗R (N ⊕P), which is the target of f.
□
Theorem 5.4. There is a unique R-module isomorphism
M ⊗R
M
i∈I
Ni ∼=
M
i∈I
(M ⊗R Ni)
where m ⊗(ni)i∈I 7→(m ⊗ni)i∈I.
Proof. The case I = ∅is vacuously true, so let I ̸= ∅. We modify the proof when |I| = 2 in
Theorem 5.3. The map b: M×(L
i∈I Ni) →L
i∈I(M⊗RNi) by b((m, (ni)i∈I)) = (m⊗ni)i∈I
is bilinear. We will show L
i∈I(M ⊗R Ni) and b have the universal mapping property of
M ⊗R
L
i∈I Ni and ⊗.
Let B : M × (L
i∈I Ni) →Q be bilinear. For each i ∈I the function M × Ni →Q where
(m, ni) 7→B(m, (. . . , 0, ni, 0, . . . )) is bilinear, so there is a linear map Li : M ⊗R Ni →Q
where Li(m⊗ni) = B(m, (. . . , 0, ni, 0, . . . )). Deﬁne L: L
i∈I(M ⊗RNi) →Q by L((ti)i∈I) =
P
i∈I Li(ti). All but ﬁnitely many ti equal 0, so the sum here makes sense, and L is linear.

<!-- page 27 -->
TENSOR PRODUCTS
27
It is left to the reader to check the diagram
L
i∈I(M ⊗R Ni)
L

M × L
i∈I Ni
b
6
B
) Q
commutes. A map L making this diagram commute has its value on (. . . , 0, m⊗ni, 0, . . . ) =
b(m, (. . . , 0, ni, 0, . . . )) determined by B, so L is unique. Thus L
i∈I(M ⊗R Ni) and the
bilinear map b to it have the universal mapping property of M ⊗R
L
i∈I Ni and the canonical
map ⊗, so there is an R-module isomorphism f making the diagram
L
i∈I(M ⊗R Ni)
f

M × L
i∈I Ni
b
6
⊗
(
M ⊗R
L
i∈I Ni
commute. Sending (m, (ni)i∈I) around the diagram both ways, f((m⊗ni)i∈I) = m⊗(ni)i∈I,
so the inverse of f is an isomorphism with the eﬀect m ⊗(ni)i∈I 7→(m ⊗ni)i∈I.
□
Remark 5.5. The analogue of Theorem 5.4 for direct products of R-modules has coun-
terexamples. While there is a natural R-linear map
(5.2)
M ⊗R
Y
i∈I
Ni →
Y
i∈I
(M ⊗R Ni)
where m ⊗(ni)i∈I 7→(m ⊗ni)i∈I, it may not be an isomorphism.18 Taking R = Z, M = Q,
and Ni = Z/piZ (i ≥1), the right side of (5.2) is 0 since Q ⊗Z (Z/piZ) = 0 for all i ≥1
(Example 3.6). The left side of (5.2) is Q ⊗Z
Q
i≥1 Z/piZ, which is not 0 by Theorem 4.27
since Q
i≥1 Z/piZ, unlike L
i∈I Z/piZ, is not a torsion abelian group.
In our proof of associativity of the tensor product, we started with a function on a
direct product M × N × P and collapsed this direct product to an iterated tensor product
(M ⊗R N) ⊗R P using bilinearity twice. It is useful to record a rather general result in that
direction, as a technical lemma for future convenience.
Theorem 5.6. Let M1, . . . , Mk, N be R-modules, with k > 2, and suppose
M1 × · · · × Mk−2 × Mk−1 × Mk
ϕ
−−→N
is a function that is bilinear in Mk−1 and Mk when other coordinates are ﬁxed. There is a
unique function
M1 × · · · × Mk−2 × (Mk−1 ⊗R Mk)
Φ
−−→N
18When R is a ﬁeld, so M and the Ni’s are vector spaces, (5.2) is an isomorphism.

<!-- page 28 -->
28
KEITH CONRAD
that is linear in Mk−1 ⊗R Mk when the other coordinates are ﬁxed and satisﬁes
(5.3)
Φ(m1, . . . , mk−2, mk−1 ⊗mk) = ϕ(m1, . . . , mk−2, mk−1, mk).
If ϕ is multilinear in M1, . . . , Mk, then Φ is multilinear in M1, . . . , Mk−2, Mk−1 ⊗R Mk.
Proof. Assuming a function Φ exists satisfying (5.3) and is linear in the last coordinate
when other coordinates are ﬁxed, its value everywhere is determined by additivity in the
last coordinate: write each tensor t ∈Mk−1 ⊗R Mk in the form t = Pp
i=1 xi ⊗yi, and then
Φ(m1, . . . , mk−2, t) = Φ
 
m1, . . . , mk−2,
p
X
i=1
xi ⊗yi
!
=
p
X
i=1
Φ(m1, . . . , mk−2, xi ⊗yi)
=
p
X
i=1
ϕ(m1, . . . , mk−2, xi, yi).
It remains to show Φ exists with the desired properties.
Fix mi ∈Mi for i = 1, . . . , k −2. Deﬁne ϕm1,...,mk−2 : Mk−1 × Mk →N by
ϕm1,...,mk−2(x, y) = ϕ(m1, . . . , mk−2, x, y).
By hypothesis ϕm1,...,mk−2 is bilinear in x and y, so from the universal mapping property of
the tensor product there is a linear map Φm1,...,mk−2 : Mk−1 ⊗R Mk →N such that
Φm1,...,mk−2(x ⊗y) = ϕm1,...,mk−2(x, y) = ϕ(m1, . . . , mk−2, x, y).
Deﬁne Φ: M1 × · · · × Mk−2 × (Mk−1 ⊗R Mk) →N by
Φ(m1, . . . , mk−2, t) = Φm1,...,mk−2(t).
Since Φm1,...,mk−2 is a linear function on Mk−1 ⊗R Mk, Φ(m1, . . . , mk−2, t) is linear in t when
m1, . . . , mk−2 are ﬁxed.
If ϕ is multilinear in M1, . . . , Mk we want to show Φ is multilinear in M1, . . . , Mk−2,
Mk−1 ⊗R Mk. We already know Φ is linear in Mk−1 ⊗R Mk when the other coordinates are
ﬁxed. To show Φ is linear in each of the other coordinates (ﬁxing the rest), we carry out
the computation for M1 (the argument is similar for other Mi’s): is
Φ(x + x′, m2, . . . , mk−2, t) ?= Φ(x, m2, . . . , mk−2, t) + Φ(x′, m2, . . . , mk−2, t)
Φ(rx, m2, . . . , mk−2, t) ?= rΦ(x, m2, . . . , mk−2, t)
when m2, . . . , mk−2, t are ﬁxed in M2, . . . , Mk−2, Mk−1⊗RMk? In these two equations, both
sides are additive in t so it suﬃces to verify these two equations when t is an elementary
tensor mk−1 ⊗mk. Then from (5.3), these two equations are true since we’re assuming ϕ is
linear in M1 (ﬁxing the other coordinates).
□
Theorem 5.6 is not speciﬁc to functions that are bilinear in the last two coordinates: any
two coordinates can be used when the function is bilinear in those two coordinates. For
instance, let’s revisit the proof of associativity of the tensor product in Theorem 5.2 to see
why the construction of the functions fp in the proof of Theorem 5.3 is a special case of
Theorem 5.6. Deﬁne
ϕ: M × N × P →M ⊗R (N ⊗R P)

<!-- page 29 -->
TENSOR PRODUCTS
29
by ϕ(m, n, p) = m ⊗(n ⊗p). This function is trilinear, so Theorem 5.6 says we can replace
M × N with its tensor product: there is a bilinear function
Φ: (M ⊗R N) × P →M ⊗R (N ⊗R P)
such that Φ(m ⊗n, p) = m ⊗(n ⊗p). Since Φ is bilinear, there is a linear function
f : (M ⊗R N) ⊗R P →M ⊗R (N ⊗R P)
such that f(t ⊗p) = Φ(t, p), so f((m ⊗n) ⊗p) = Φ(m ⊗n, p) = m ⊗(n ⊗p).
The remaining module properties we treat with the tensor product in this section in-
volve its interaction with the Hom-module construction, so in particular the dual module
construction (M∨= HomR(M, R)).
Theorem 5.7. For R-modules M, N, and P, there are R-module isomorphisms
BilR(M, N; P) ∼= HomR(M ⊗R N, P) ∼= HomR(M, HomR(N, P)).
Proof. The R-module isomorphism from BilR(M, N; P) to HomR(M ⊗R N, P) comes from
the universal mapping property of the tensor product: every bilinear map B : M × N →P
leads to a speciﬁc linear map LB : M ⊗R N →P, and all linear maps M ⊗R N →P
arise in this way. The correspondence B 7→LB is an isomorphism from BilN(M, N; P) to
HomR(M ⊗R N, P).
Next we explain why BilR(M, N; P) ∼= HomR(M, HomR(N, P)), which amounts to think-
ing about a bilinear map M × N →P as a family of linear maps N →P indexed by
elements of M. If B : M × N →P is bilinear, then for each m ∈M the function B(m, −)
is a linear map N →P. Deﬁne fB : M →HomR(N, P) by fB(m) = B(m, −). (That is,
fB(m)(n) = B(m, n).) Check fB is linear, partly because B is linear in its ﬁrst component
when the second component is ﬁxed.
Going in the other direction, if L: M →HomR(N, P) is linear then for each m ∈M we
have a linear function L(m): N →P. Deﬁne BL : M × N →P to be BL(m, n) = L(m)(n).
Check BL is bilinear.
It is left to the reader to check the correspondences B ⇝fB and L ⇝BL are each
linear and are inverses of each other, so BilR(M, N; P) ∼= HomR(M, HomR(N, P)) as R-
modules.
□
Here’s a high-level way of interpreting the isomorphism between the second and third
modules in Theorem 5.7. Write FN(M) = M ⊗R N and GN(M) = HomR(N, M), so FN
and GN turn R-modules into new R-modules. Theorem 5.7 says
HomR(FN(M), P) ∼= HomR(M, GN(P)).
This is analogous to the relation between a matrix A and its transpose A⊤inside dot
products:
Av · w = v · A⊤w
for all vectors v and w. So FN and GN are “transposes” of each other. Actually, FN and
GN are called adjoints of each other because pairs of operators L and L′ in linear algebra
that satisfy the relation Lv · w = v · L′w for all vectors v and w are called adjoints and the
relation between FN and GN looks similar.
Corollary 5.8. For R-modules M and N, there are R-module isomorphisms
BilR(M, N; R) ∼= (M ⊗R N)∨∼= HomR(M, N∨) ∼= HomR(N, M∨).

<!-- page 30 -->
30
KEITH CONRAD
Proof. Using P = R in Theorem 5.7, we get BilR(M, N; R) ∼= (M ⊗RN)∨∼= HomR(M, N∨).
From M ⊗R N ∼= N ⊗R M we get (M ⊗R N)∨∼= (N ⊗R M)∨, and the second dual module
is isomorphic to HomR(N, M∨) by Theorem 5.7 with the roles of M and N there reversed
and P = R. Thus we have obtained isomorphisms between the desired modules.
The isomorphism between HomR(M, N∨) and HomR(N, M∨) amounts to viewing a map
in either Hom-module as as a bilinear map B : M × N →R.
□
The construction of M ⊗R N is “symmetric” in M and N in the sense that M ⊗R N ∼=
N ⊗R M in a natural way, but Corollary 5.8 is not saying HomR(M, N) ∼= HomR(N, M)
since those are not the Hom-modules in the corollary. For instance, if R = M = Z and
N = Z/2Z then HomR(M, N) ∼= Z/2Z and HomR(N, M) = 0.
Theorem 5.9. For R-modules M and N, there is a linear map M∨⊗R N →HomR(M, N)
sending each elementary tensor ϕ ⊗n in M∨⊗R N to the linear map M →N deﬁned by
(ϕ ⊗n)(m) = ϕ(m)n. This is an isomorphism M∨⊗R N →HomR(M, N) if M and N are
ﬁnite free. In particular, if F is ﬁnite free then F ∨⊗R F ∼= EndR(F) as R-modules.
Proof. We need to make an element of M∨and an element of N act together as a linear
map M →N. The function M∨× M × N →N given by (ϕ, m, n) 7→ϕ(m)n is trilinear.
Here the functional ϕ ∈M∨acts on m to give a scalar, which is then multiplied by n. By
Theorem 5.6, this trilinear map induces a bilinear map B : (M∨⊗R N) × M →N where
B(ϕ ⊗n, m) = ϕ(m)n. For t ∈M∨⊗R N, B(t, −) is in HomR(M, N), so we have a linear
map f : M∨⊗R N →HomR(M, N) by f(t) = B(t, −). (Explicitly, the elementary tensor
ϕ ⊗n acts as a linear map M →N by the rule (ϕ ⊗n)(m) = ϕ(m)n.)
Now let M and N be ﬁnite free. To show f is an isomorphism, we may suppose M and
N are nonzero. Pick bases {ej} of M and {e′
i} of N. (We use this indexing on the bases
because the standard way to represent a linear map as a matrix from a choice of bases
of M and N is to see where the map sends the jth basis element of M.) Then f makes
e∨
j ⊗e′
i act on M by sending each ek to e∨
j (ek)e′
i = δjke′
i. So f(e∨
j ⊗e′
i) ∈HomR(M, N)
sends ej to e′
i and sends every other basis element ek to 0. Writing elements of M and
N as coordinate vectors using their bases, HomR(M, N) becomes matrices and f(e∨
j ⊗e′
i)
becomes the matrix with a 1 in the (i, j) position and 0 elsewhere. Such matrices are a
basis of all matrices, so the image of f contains a basis of HomR(M, N) and thus f is onto.
To show f is one-to-one, suppose f(P
i,j cije∨
j ⊗e′
i) = O in HomR(M, N). Applying both
sides to ek, we get P
i,j cijδjke′
i = 0, which says P
i cike′
i = 0, so cik = 0 for all i and all k.
Thus every cij is 0. This concludes the proof that f is an isomorphism.
Let’s work out the inverse of f explicitly. For L ∈HomR(M, N), let L(ej) = P
i aije′
i,
so L has matrix representation (aij) with respect to the chosen bases of M and N. Write
L = f(P
i,j cije∨
j ⊗e′
i), with the coeﬃcients cij in R to be determined. Then
L(ek) =
X
i,j
cij(e∨
j ⊗e′
i)(ek) =
X
i
cike′
i,
so cik = aik. Thus cij = aij for all i and j, so the L ∈HomR(M, N) with matrix represen-
tation (aij) corresponds to the tensor P
i,j aije∨
j ⊗e′
i in M∨⊗R N.
It looks strange to use tensors indexed as e∨
j ⊗e′
i, so rewrite the isomorphism M∨⊗RN →
HomR(M, N) as N ⊗RM∨→HomR(M, N) with (n⊗ϕ)(m) = ϕ(m)n. Then P
i,j aije′
i⊗e∨
j
in N ⊗R M∨corresponds to the linear map M →N with matrix representation (aij) for
the chosen bases of M and N.
□

<!-- page 31 -->
TENSOR PRODUCTS
31
Remark 5.10. If M and N are not both ﬁnite free, the map M∨⊗R N →HomR(M, N)
in Theorem 5.9 may not be an isomorphism, or even injective or surjective. For example,
let p be prime, R = Z/p2Z, and M = N = R/pR as R-modules. Check that M∨∼= M,
M ⊗R M ∼= M, and HomR(M, M) ∼= M, but the map M∨⊗R M →HomR(M, M) in
Theorem 5.9 is identically 0 (it suﬃces to show each elementary tensor in M∨⊗R M acts
on M as 0). Notice M∨⊗R M and HomR(M, M) are isomorphic, but the natural linear
map between them happens to be identically 0.
Example 5.11. Finite-dimensional K-vector spaces V and W have ﬁnite bases, so Theorem
5.9 says V ∨⊗KW ∼= HomK(V, W) by sending each elementary tensor ϕ⊗w to the linear map
V →W given by the rule (ϕ⊗w)(v) = ϕ(v)w for all v ∈V and W ⊗KV ∨∼= HomK(V, W) by
sending each elementary tensor w ⊗ϕ to the linear map V →W where (w ⊗ϕ)(v) = ϕ(v)w
for all v ∈V . This is one of the most basic ways tensor products occur in linear algebra.
What is the isomorphism W ⊗K V ∨→HomK(V, W) really saying? For each w ∈W and
ϕ ∈V ∨, we get a linear map V →W by v 7→ϕ(v)w, whose image as v varies is the scalar
multiples of w (unless ϕ = 0). Since the expression ϕ(v)w is bilinear in ϕ and w, we can
regard the linear map V →W where v 7→ϕ(v)w as deﬁning an eﬀect of w ⊗ϕ on V , with
values in W, and all linear maps V →W are sums of such maps. This corresponds to the
fact that every matrix is a sum of matrices with at most one nonzero entry.
For instance, when V = W = K2 with basis e1 =
 1
0

and e2 =
 0
1

, let ϕ ∈K2 by
ϕ
 x
y

= x. Then (e2 ⊗ϕ)
 x
y

= xe2 =
 0
x

, so e2 ⊗ϕ = ( 0 0
1 0 ) as a linear map K2 →K2.
By the last paragraph of the proof of Theorem 5.9, the isomorphism W ⊗K V ∨→
HomK(V, W) can be described in terms of bases {e′
i} of W and {ej} of V by sending the
tensor P
i,j aije′
i ⊗e∨
j to the linear map L ∈HomK(V, W) where L(ej) = P
i aije′
i.
When M and N are ﬁnite free R-modules, the isomorphisms in Corollary 5.8 and Theorem
5.9 lead to a basis-free description of M ⊗RN making no mention of universal mapping
properties. Identify M with M∨∨by double duality, so the isomorphism in Theorem 5.9
with M∨in place of M assumes the form
M ⊗R N ∼= HomR(M∨, N),
where m ⊗n acts as a linear map M∨→N by the rule (m ⊗n)(ϕ) = ϕ(m)n.
Since
N ∼= N∨∨by double duality, HomR(M∨, N) ∼= HomR(M∨, (N∨)∨) ∼= BilR(M∨, N∨; R) by
Corollary 5.8. Therefore when M and N are ﬁnite free R-modules,
(5.4)
M ⊗R N ∼= BilR(M∨, N∨; R),
where m ⊗n acts as a bilinear map M∨× N∨→R by the rule (m ⊗n)(ϕ, ψ) = ϕ(m)ψ(n).
Similarly, M⊗k is isomorphic to the module of k-multilinear maps (M∨)k →R, with the
elementary tensor m1⊗· · ·⊗mk deﬁning the map sending (ϕ1, . . . , ϕk) to ϕ1(m1) · · · ϕk(mk).
The deﬁnition of the tensor product of ﬁnite-dimensional vector spaces in [1, p. 65] and
[18, p. 35] is essentially (5.4).19
It is a good exercise to check these interpretations of
m ⊗n as a member of HomR(M∨, N) and BilR(M∨, N∨; R) are identiﬁed with each other
by Corollary 5.8 and double duality.
19Using the ﬁrst isomorphism in Corollary 5.8 and double duality, M ⊗R N ∼= BilR(M, N; R)∨for ﬁnite
free M and N, where m ⊗n in M ⊗R N corresponds to the function B 7→B(m, n) in BilR(M, N; R)∨.
This is how tensor products of ﬁnite-dimensional vector spaces are deﬁned in [10, p. 40], namely V ⊗K W
is deﬁned to be the dual space to BilK(V, W; K).

<!-- page 32 -->
32
KEITH CONRAD
Watch out! The isomorphism (5.4) is false for general modules M and N (where double
duality doesn’t hold). There is always a linear map M ⊗R N →BilR(M∨, N∨; R) given on
elementary tensors by m ⊗n 7→[(ϕ, ψ) 7→ϕ(m)ψ(n)], but it need not be an isomorphism.
Example 5.12. Let p be prime, R = Z/p2Z, and M = R/pR. The R-modules M ⊗RM and
BilR(M∨, M∨; R) are isomorphic to each other (and to M), but the natural map M ⊗RM →
BilR(M∨, M∨; R) is identically 0.
Example 5.13. Let R = Z and M = N = Q. Since Q ⊗Z Q ∼= Q as Z-modules (Example
4.22) and Q∨= HomZ(Q, Z) = 0, the left side of (5.4) is nonzero and the right side is 0.
For ﬁnite-dimensional K-vector spaces V and W, the rank of a linear map L: V →W is
the dimension of the image L(V ). This is one of the most important numerical invariants
of L (e.g., the rank-nullity theorem). It has an interesting interpretation when L is viewed
as a tensor in V ∨⊗K W (or W ⊗K V ∨) by the isomorphism in Example 5.11, as follows.
Theorem 5.14. With notation as above, the rank of L: V →W is the smallest d ≥0 such
that L is a sum of d nonzero elementary tensors when L is viewed in V ∨⊗K W.
Proof. The result is trivial when L = O (rank is 0), so we can assume L ̸= O (positive
rank). Let r ≥1 be the rank of L. We will show (i) if L is a sum of d elementary tensors
then r ≤d and (ii) L is a sum of r (nonzero) elementary tensors.
Suppose L = ϕ1 ⊗w1 + · · · + ϕd ⊗wd. Then for each v ∈V , L(v) = Pd
i=1 ϕi(v)wi, which
is in the span of w1, . . . , wd. Thus L(V ) ⊂Span(w1, . . . , wd), so r = dimK L(V ) ≤d.
To prove L is a sum of r elementary tensors in V ∨⊗K W, let L(V ) have basis {e1, . . . , er}.
For v ∈V , write L(v) as a linear combination of the ei’s: L(v) = c1e1 + · · · + crer where
c1, . . . , cr ∈K. These coeﬃcients are uniquely determined for each v because e1, . . . , er are
linearly independent.20 Therefore each coeﬃcient is a function of v. Writing ci = ci(v),
(5.5)
L(v) = c1(v)e1 + · · · + cr(v)er.
Since L is K-linear, the coeﬃcient functions ci : V →K are each K-linear. For example, if
v and v′ are in V then
L(v) + L(v′) = (c1(v)e1 + · · · + cr(v)er) + (c1(v′)e1 + · · · + cr(v′)er) =
r
X
i=1
(ci(v) + ci(v′))ei
and
L(v + v′) =
r
X
i=1
ci(v + v′)ei,
so the equation L(v + v′) = L(v) + L(v′) and the linear independence of the ei’s implies
ci(v + v′) = ci(v) + ci(v′) for all i and all v and v′. Thus each ci is additive. In a similar
way, ci(av) = aci(v) for all a ∈K and v ∈V , so each ci is linear.
Because ci is a linear map from V to K it is in the dual space V ∨. Then (5.5) as an
identity for all v is another way of saying L = c1 ⊗e1 + · · · + cr ⊗er in V ∨⊗K W, so L is
a sum of r elementary tensors. These elementary tensors are all nonzero since we already
showed L can’t be a sum of fewer than r elementary tensors in V ∨⊗K W.21
□
20Diﬀerent v’s might have all the same coeﬃcients for L(v) if L is not injective.
21Here is a more direct way to show each elementary tensor ci ⊗ei is nonzero. Each ei is in L(V ) and is
not 0, so there is a v where L(v) = ei, and for that v we have ci(v) = 1 (and other cj(v) are 0). Thus ci ̸= 0
in V ∨, so ci ⊗ei is nonzero by Theorem 4.25 (or 4.9).

<!-- page 33 -->
TENSOR PRODUCTS
33
Inspired by Theorem 5.14, deﬁne the rank of a tensor t in M1 ⊗R · · · ⊗R Mk to be the
smallest number of nonzero elementary tensors that sum to t (the rank of the zero tensor is
0). For ﬁnite-dimensional vector spaces V and W, a tensor’s rank in V ⊗K W can be found
by viewing V or W as a dual space so tensors in V ⊗K W become linear maps.
Example 5.15. In R3⊗RR4 here is a sum of 12 elementary tensors built from the standard
bases e1, e2, e3 of R3 and e′
1, e′
2, e′
3, e′
4 of R4:
t = e1 ⊗e′
1 + 4e1 ⊗e′
2 + 2e1 ⊗e′
3 + 3e1 ⊗e′
4 + 2e2 ⊗e′
1 + 5e2 ⊗e′
2+
(5.6)
3e2 ⊗e′
3 + 4e2 ⊗e′
4 + e3 ⊗e′
1 + 7e3 ⊗e′
2 + 3e3 ⊗e′
3 + 5e3 ⊗e′
4.
To ﬁnd the rank of t, we convert t into a linear map R3 →R4 by identifying R3 with
its dual space so that R3 ⊗R R4 ∼= (R3)∨⊗R R4 ∼= HomR(R3, R4) and the Hom-space is
thought of as 4×3 matrices. View R3 (and R4) as column vectors and (R3)∨as row vectors
that act on column vectors by multiplication from the left. Then for v ∈R3 and w ∈R4,
v ⊗w: R3 →R4 by x 7→w(v⊤x) = (wv⊤)x. Since e′
ie⊤
j has 1 in the (i, j) component and
0 elsewhere, the tensor t above corresponds under R3 ⊗R R4 ∼= Hom(R3, R4) to the matrix
A =




1
2
1
4
5
7
2
3
3
3
4
5



.
Let the columns of A be w1, w2, and w3. The row reduced form of A is




1
0
3
0
1
−1
0
0
0
0
0
0



,
which tells us w1 and w2 are linearly independent and w3 = 3w1 −w2. Thus A has rank 2,
so t has rank 2: it is a sum of two elementary tensors. What could those two tensors be?!?
To ﬁnd two elementary tensors with sum t, we use the proof of Theorem 5.14.
Let
c1, c2 : R3 →R be coeﬃcient functions for A(v) = c1(v)w1 + c2(v)w2 as v runs over R3.
Using the basis vectors e1, e2, e3 of R3 in the role of v, we have
A(e1) = w1,
A(e2) = w2,
A(e3) = 3w1 −w2,
so c1 = e∨
1 + 3e∨
3 = (e1 + 3e3)∨and c2 = e∨
2 −e∨
3 = (e2 −e3)∨. Thus in R3 ⊗R R4,
t = (e1 + 3e3) ⊗w1 + (e2 −e3) ⊗w2,
which is a sum of two elementary tensors. In more explicit form,
(5.7)
t = (e1 + 3e3) ⊗(e′
1 + 4e′
2 + 2e′
3 + 3e′
4) + (e2 −e3) ⊗(2e′
1 + 5e′
2 + 3e′
3 + 4e′
4).
You can expand the right side of (5.7) to check you get (5.6), or in terms of matrices check
A = w1(e1 + 3e3)⊤+ w2(e2 −e3)⊤=




1
4
2
3



(1 0 3) +




2
5
3
4



(0 1
−1).
Example 5.16. If V is an n-dimensional vector space over K with a basis e1, . . . , en, then
Pn
i=1 ei⊗ei has tensor rank n: it is not a sum of fewer than n elementary tensors in V ⊗K V .

<!-- page 34 -->
34
KEITH CONRAD
To see why, use the isomorphism V ⊗KV →HomK(V, V ) where v⊗v′ 7→[w 7→(v·w)v′] on
elementary tensors, with v·w being the dot product with respect to the chosen basis of V : for
v = Pn
i=1 aiei and w = Pn
j=1 biei, v·w := Pn
i=1 aibi. Then ei·w = bi and w = Pn
i=1(ei·w)ei,
so ei ⊗ei 7→[w 7→(ei · w)ei = biei] and Pn
i=1 ei ⊗ei 7→[w 7→Pn
i=1(ei · w)ei = w]. That
means Pn
i=1 ei ⊗ei in V ⊗K V corresponds to the identity map in HomK(V, V ). The image
of the identity map on V has dimension n, so Pn
i=1 ei ⊗ei in V ⊗K V has tensor rank n.
The rank of a linear map from an m-dimensional vector space to an n-dimensional vector
space is at most min(m, n) and this minimum is easy to achieve: use an injective map if
m ≤n and a surjective map if m ≥n. Therefore the maximal rank among all tensors in
V ⊗K W is min(dimK V, dimK W). For example, if dimK V = n then every basis of V ⊗K V
consists of n2 tensors but each element of V ⊗K V is a sum of at most n elementary tensors
(which of course might not be linearly independent).
Computing the maximal rank among all tensors in a tensor product of three vector spaces
is hard in general. H˚astad [11] showed it is an NP-complete problem for vector spaces over
ﬁnite ﬁelds and an NP-hard problem for vector spaces over Q. If n ≥3, the maximal tensor
rank in the 3-fold tensor product (Cn)⊗3 is known for n = 3 (it’s 5) and is unknown for
n ≥4 (upper bounds are known, but not the exact maximum).22 In a tensor product of
three free modules over an integral domain, Shitov [23] showed computing tensor rank in
general is NP-hard and over Z in particular it is undecidable. To quote the title of [12],
“most tensor problems are NP-hard”.
As an application of tensor rank, we can settle an issue that was mentioned in Remark
4.17: give an example of a linear map M ⊗R N →P for some R, M, N, and P such that the
map is not injective on M ⊗R N and is injective on the elementary tensors in M ⊗R N. The
example below and the method leading up to it was pointed out to me by Darij Grinberg.
We begin with a necessary and suﬃcient condition to be injective on the elementary
tensors, in terms of tensor rank.
Theorem 5.17. A linear map f : M ⊗R N →P is injective on the elementary tensors in
M ⊗R N if and only if the only element of ker f with tensor rank at most 2 is 0.
Proof. First suppose f is injective on the elementary tensors. If f(t) = 0 and t has tensor
rank at most 2, then t can be written as m ⊗n −m′ ⊗n′ (if t has tensor rank at most 1,
we can use m′ = 0). Then 0 = f(t) = f(m ⊗n) −f(m′ ⊗n′), so f(m ⊗n) = f(m′ ⊗n′).
Since f is injective on elementary tensors, m ⊗n = m′ ⊗n′, so t = m ⊗n −m′ ⊗n′ = 0.
Conversely, suppose the only element of ker f with tensor rank at most 2 is 0. If two
elementary tensors m⊗n and m′⊗n′ satisfy f(m⊗n) = f(m′⊗n′), then f(m⊗n−m′⊗n′) =
0, so m ⊗n −m′ ⊗n′ is in ker f and has tensor rank at most 2, so this tensor is 0, which
implies m ⊗n = m′ ⊗n′.
□
Corollary 5.18. A linear map f : M ⊗R N →P is not injective on M ⊗R N and is
injective on the elementary tensors in M ⊗R N if and only if ker f is nonzero and each
nonzero element of ker f has tensor rank at least 3.
Proof. Saying f is not injective on M ⊗R N is equivalent to ker f being nonzero, and saying
f is injective on the elementary tensors of M ⊗R N is equivalent to ker f having no element
with tensor rank below 3 other than 0.
□
22See https://mathoverflow.net/questions/102559.

<!-- page 35 -->
TENSOR PRODUCTS
35
Example 5.19. Let V be a vector space over a ﬁeld K with dimension n ≥3. In V ⊗K V ,
the tensor t = Pn
i=1 ei ⊗ei has rank n (Example 5.16), so the natural reduction map
f : V ⊗K V →(V ⊗K V )/Kt is linear with nonzero kernel Kt. The nonzero elements of Kt
have tensor rank n ≥3, so f is injective on elementary tensors in V ⊗K V but not injective
on V ⊗K V by Corollary 5.18.
When dimK V = 2, there is nothing like Example 5.19: a linear map V ⊗K V →W
(arbitrary target space W) that’s injective on the elementary tensors has to be injective on
V ⊗K V because every element of V ⊗K V has tensor rank at most dimK V = 2, so the
criterion in Corollary 5.18 cannot be satisﬁed.
6. Base Extension
In algebra, there are many times a module over one ring is replaced by a related module
over another ring. For instance, in linear algebra it is useful to enlarge Rn to Cn, creating
in this way a complex vector space by letting the real coordinates be extended to complex
coordinates. In ring theory, irreducibility tests in Z[X] involve viewing a polynomial in
Z[X] as a polynomial in Q[X] or reducing the coeﬃcients mod p to view it in (Z/pZ)[X].
We will see that all these passages to modules with new coeﬃcients (Rn ⇝Cn, Z[X] ⇝
Q[X], Z[X] ⇝(Z/pZ)[X]) can be described in a uniform way using tensor products.
Let f : R →S be a homomorphism of commutative rings. We use f to consider a S-
module N as an R-module by rn := f(r)n.
In particular, S itself is an R-module by
rs := f(r)s. Passing from N as an S-module to N as an R-module in this way is called
restriction of scalars.
Example 6.1. If R ⊂S, f can be the inclusion map (e.g., R ,→C or Q ,→C). This is
how a C-vector space is thought of as an R-vector space or a Q-vector space.
Example 6.2. If S = R/I, f can be reduction modulo I: each R/I-module is also an
R-module by letting r act in the way that r mod I acts.
Here is a simple illustration of restriction of scalars.
Theorem 6.3. Let N and N′ be S-modules. An S-linear map N →N′ is also an R-linear
map when we treat N and N′ as R-modules.
Proof. Let ϕ: N →N′ be S-linear, so ϕ(sn) = sϕ(n) for all s ∈S and n ∈N. For r ∈R,
ϕ(rn) = ϕ(f(r)n) = f(r)ϕ(n) = rϕ(n),
so ϕ is R-linear.
□
As a notational convention, since we will be going back and forth between R-modules
and S-modules a lot, we will write M (or M′, and so on) for R-modules and N (or N′, and
so on) for S-modules. Since N is also an R-module by restriction of scalars, we can form
the tensor product R-module M ⊗R N, where
r(m ⊗n) = (rm) ⊗n = m ⊗rn,
with the third expression really being m ⊗f(r)n since rn := f(r)n.
The idea of base extension is to reverse the process of restriction of scalars. For an R-
module M we want to create an S-module of products sm that matches the old meaning
of rm if s = f(r). This new S-module is called an extension of scalars or base extension. It
will be the R-module S ⊗R M equipped with a speciﬁc structure of an S-module.

<!-- page 36 -->
36
KEITH CONRAD
Since S is a ring, not just an R-module, let’s try making S ⊗R M into an S-module by
(6.1)
s′(s ⊗m) := s′s ⊗m.
Is this S-scaling on elementary tensors well-deﬁned and does it extend to S-scaling on all
tensors?
Theorem 6.4. The additive group S ⊗R M has a unique S-module structure satisfying
(6.1), and this is compatible with the R-module structure in the sense that rt = f(r)t for all
r ∈R and t ∈S ⊗R M.
Proof. Suppose the additive group S ⊗R M has an S-module structure satisfying (6.1). We
will show the S-scaling on all tensors in S ⊗R M is determined by this. Each t ∈S ⊗R M
is a ﬁnite sum of elementary tensors, say
t = s1 ⊗m1 + · · · + sk ⊗mk.
For s ∈S,
st = s(s1 ⊗m1 + · · · + sk ⊗mk)
= s(s1 ⊗m1) + · · · + s(sk ⊗mk)
= ss1 ⊗m1 + · · · + ssk ⊗mk
by (6.1),
so st is determined, although this formula for it is not obviously well-deﬁned.
(Does a
diﬀerent expression for t as a sum of elementary tensors change st?)
Now we show there really is an S-module structure on S⊗RM satisfying (6.1). Describing
the S-scaling on S ⊗R M means creating a function S × (S ⊗R M) →S ⊗R M satisfying
the relevant scaling axioms:
(6.2)
1 · t = t,
s(t1 + t2) = st1 + st2,
(s1 + s2)t = s1t + s2t,
s1(s2t) = (s1s2)t.
For each s′ ∈S we consider the function S × M →S ⊗R M given by (s, m) 7→(s′s) ⊗m.
This is R-bilinear, so by the universal mapping property of tensor products there is an
R-linear map µs′ : S ⊗R M →S ⊗R M where µs′(s ⊗m) = (s′s) ⊗m on elementary tensors.
Deﬁne a multiplication S × (S ⊗R M) →S ⊗R M by s′t := µs′(t). This will be the scaling
of S on S ⊗R M. We check the conditions in (6.2):
(1) To show 1t = t means showing µ1(t) = t. On elementary tensors, µ1(s ⊗m) =
(1 · s) ⊗m = s ⊗m, so µ1 ﬁxes elementary tensors. Therefore µ1 ﬁxes all tensors by
additivity.
(2) s(t1 + t2) = st1 + st2 since µs is additive.
(3) Showing (s1 + s2)t = s1t + s2t means showing µs1+s2 = µs1 + µs2 as functions on
S ⊗R M. Both sides are additive functions, so it suﬃces to check they agree on
elementary tensors s ⊗m, where both sides have common value (s1 + s2)s ⊗m.
(4) To show s1(s2t) = (s1s2)t means µs1 ◦µs2 = µs1s2 as functions on S ⊗R M. Both
sides are additive functions of t, so it suﬃces to check they agree on elementary
tensors s ⊗m, where both sides have common value (s1s2s) ⊗m.
Let’s check the S-module structure on S ⊗R M is compatible with its original R-module
structure. For r ∈R, if we treat r as f(r) ∈S then scaling by f(r) on an elementary tensor
s⊗m has the eﬀect f(r)(s⊗m) = f(r)s⊗m. Since f(r)s is the deﬁnition of rs (this is how
we make S into an R-module), f(r)s⊗m = rs⊗m = r(s⊗m). Thus f(r)(s⊗m) = r(s⊗m),
so f(r)t = rt for all t in S ⊗R M by additivity.
□

<!-- page 37 -->
TENSOR PRODUCTS
37
By exactly the same kind of argument, M ⊗R S with S on the right has a unique S-
module structure where s′(m ⊗s) = m ⊗s′s. So whenever we meet S ⊗R M or M ⊗R S, we
know they are S-modules in a speciﬁc way. Moreover, these two S-modules are naturally
isomorphic: by Theorem 5.1, there is an isomorphism ϕ: S ⊗R M →M ⊗R S of R-modules
where ϕ(s⊗m) = m⊗s. To show ϕ is in fact an isomorphism of S-modules, all we need to do
is check S-linearity since ϕ is known to be additive and a bijection. To show ϕ(s′t) = s′ϕ(t)
for all s′ and t, additivity of both sides in t means we may focus on the case t = s ⊗m:
ϕ(s′(s ⊗m)) = ϕ((s′s) ⊗m) = m ⊗s′s = s′(m ⊗s) = s′ϕ(s ⊗m).
This idea of creating an S-module isomorphism by using a known R-module isomorphism
that is also S-linear will be used many more times, so watch for it.
We must be careful to refer to R-linear maps and S-linear maps, rather than just linear
maps, so that it is clear what our scalar ring is each time.
Example 6.5. In Theorem 4.5 we saw (R/I) ⊗R M ∼= M/IM as R-modules by r ⊗m 7→
rm. Since M/IM is naturally an R/I-module, and now we know (R/I) ⊗R M is an R/I-
module, the R-module isomorphism (R/I) ⊗R M ∼= M/IM turns out to be an R/I-module
isomorphism too since it is R/I-linear (check!).
Example 6.6. Set N = S ⊗R M, where M is an R-module. For an ideal J in S, JN is
an S-submodule of N and N/JN is an S/J-module. We have (S/J) ⊗R M ∼= N/JN as
S/J-modules, which generalizes the previous example (taking S = R).
To build that isomorphism, there is an S/J-linear mapping f : (S/J) ⊗R M →N/JN
where s ⊗m 7→s ⊗m on elementary tensors: build it ﬁrst as an R-linear mapping and
then check it is S-linear, and then S/J-linear. In the other direction, there is an S-linear
mapping N →(S/J) ⊗R M where s ⊗m 7→s ⊗m on elementary tensors: build it ﬁrst as
an R-linear mapping and then check it is S-linear. Then show it kills JN, so it induces
an S-linear mapping g: N/JN →(S/J) ⊗R M that is also S/J-linear. Check f and g are
inverses by looking at their values on the obvious spanning sets of their domains.
As an instance of (S/J) ⊗R M ∼= N/JN, take S = R[X] and J = XS, so S/J ∼= R as
R-modules and as R[X]-modules where X acts on R as 0. For an R-module M, N/XN =
N/JN ∼= (S/J) ⊗R M ∼= R ⊗R M ∼= M as R-modules. So if an R[X]-module N is the base
extension of an R-module M, then we can describe M up to isomorphism as N/XN.
Theorem 6.7. If F is a free R-module with basis {ei}i∈I then S ⊗R F is a free S-module
with basis {1 ⊗ei}i∈I.
Proof. Since S is an R-module, we know from Theorem 4.15 that every element of S ⊗R F
has a unique representation in the form P
i∈I si ⊗ei, where all but ﬁnitely many si equal 0.
Since si ⊗ei = si(1⊗ei) in the S-module structure on S ⊗R F, every element of S ⊗R F is a
unique S-linear combination P si(1 ⊗ei), which says {1 ⊗ei} is an S-basis of S ⊗R F.
□
Example 6.8. As an S-module, S ⊗RRn has S-basis {1⊗e1, . . . , 1⊗en} where {e1, . . . , en}
is the standard basis of Rn, so Sn ∼= S ⊗R Rn as S-modules by
(s1, . . . , sn) 7→
n
X
i=1
si(1 ⊗ei) =
n
X
i=1
si ⊗ei
because this map is S-linear (check!) and sends an S-basis to an S-basis. In particular,
S ⊗R R ∼= S as S-modules by s ⊗r 7→sr.

<!-- page 38 -->
38
KEITH CONRAD
For instance,
C ⊗R Rn ∼= Cn,
C ⊗R Mn(R) ∼= Mn(C)
as C-vector spaces, not just as R-vector spaces. For an ideal I in R, (R/I)⊗RRn ∼= (R/I)n,
not just as R-modules. as R/I-modules.
Example 6.9. As an S-module, S ⊗R R[X] has S-basis {1 ⊗Xi}i≥0, so S ⊗R R[X] ∼= S[X]
as S-modules23 by P
i≥0 si ⊗Xi 7→P
i≥0 siXi.
As particular examples, C ⊗R R[X] ∼= C[X] as C-vector spaces, Q ⊗Z Z[X] ∼= Q[X] as
Q-vector spaces and (Z/pZ) ⊗Z Z[X] ∼= (Z/pZ)[X] as Z/pZ-vector spaces.
Example 6.10. If we treat Cn as a real vector space, then its base extension to C is the
complex vector space C ⊗R Cn where c(z ⊗v) = cz ⊗v for c in C. Since Cn ∼= R2n as real
vector spaces, we have a C-vector space isomorphism
C ⊗R Cn ∼= C ⊗R R2n ∼= C2n.
That’s interesting: restricting scalars on Cn to make it a real vector space and then extend-
ing scalars back up to C does not give us Cn back, but instead two copies of Cn. The point
is that when we restrict scalars, the real vector space Cn forgets it is a complex vector
space. So the base extension of Cn from a real vector space to a complex vector space
doesn’t remember that it used to be a complex vector space.
Quite generally, if V is a ﬁnite-dimensional complex vector space and we view it as a real
vector space, its base extension C ⊗R V to a complex vector space is not V but a direct
sum of two copies of V . Let’s do a dimension check. Set n = dimC(V ), so dimR(V ) = 2n.
Then dimR(C⊗R V ) = dimR(C) dimR(V ) = 2(2n) = 4n and dimR(V ⊕V ) = 2 dimR(V ) =
2(2n) = 4n, so the two dimensions match. This match is of course not a proof that there
is a natural isomorphism C ⊗R V →V ⊕V of complex vector spaces. Work out such an
isomorphism as an exercise. The proof had better use the fact that V is already a complex
vector space to make sense of V ⊕V as a complex vector space.
To get our bearing on this example, let’s compare an S-module N with the S-module
S ⊗R N (where s′(s ⊗n) = s′s ⊗n). Since N is already an S-module, should S ⊗R N ∼= N?
If you think so, reread Example 6.10 (R = R, S = C, N = Cn). Scalar multiplication
S ×N →N is R-bilinear, so there is an R-linear map ϕ: S ⊗R N →N where ϕ(s⊗n) = sn.
This map is also S-linear: ϕ(st) = sϕ(t). To check this, since both sides are additive in t it
suﬃces to check the case of elementary tensors, and
ϕ(s(s′ ⊗n)) = ϕ((ss′) ⊗n) = ss′n = s(s′n) = sϕ(s′ ⊗n).
In the other direction, the function ψ: N →S ⊗R N where ψ(n) = 1 ⊗n is R-linear but is
generally not S-linear since ψ(sn) = 1⊗sn has no reason to be sψ(n) = s⊗n because we’re
using ⊗R, not ⊗S. We have created natural maps ϕ: S ⊗R N →N and ψ: N →S ⊗R N;
are they inverses? It’s unlikely, since ϕ is S-linear and ψ is generally not. But let’s work
out the composites and see what happens. In one direction,
ϕ(ψ(n)) = ϕ(1 ⊗n) = 1 · n = n.
In the other direction,
ψ(ϕ(s ⊗n)) = ψ(sn) = 1 ⊗sn ̸= s ⊗n
23We saw S ⊗R R[X] and S[X] are isomorphic as R-modules in Example 4.16 when S ⊃R, and it holds
now for all R
f
−−→S.

<!-- page 39 -->
TENSOR PRODUCTS
39
in general. So ϕ ◦ψ is the identity but ψ ◦ϕ is usually not the identity. Since ϕ ◦ψ = idN,
ψ is a section to ϕ, so N is a direct summand of S ⊗R N. Explicitly, S ⊗R N ∼= ker ϕ ⊕N
by s ⊗n 7→(s ⊗n −1 ⊗sn, sn) and its inverse map is (k, n) 7→k + 1 ⊗n. The phenomenon
that S ⊗R N is typically larger than N when N is an S-module can be remembered by the
example C ⊗R Cn ∼= C2n.
Theorem 6.11. For R-modules {Mi}i∈I, there is an S-module isomorphism
S ⊗R
M
i∈I
Mi ∼=
M
i∈I
(S ⊗R Mi).
Proof. This is vacuously true if I = ∅or R = 0, so take I ̸= ∅and R ̸= 0. Since S is an
R-module, by Theorem 5.4 there is an R-module isomorphism
ϕ: S ⊗R
M
i∈I
Mi →
M
i∈I
(S ⊗R Mi)
where ϕ(s ⊗(mi)i∈I) = (s ⊗mi)i∈I. To show ϕ is an S-module isomorphism, we just have
to check ϕ is S-linear, since we already know ϕ is additive and a bijection. It is obvious that
ϕ(st) = sϕ(t) when t is an elementary tensor, and since both ϕ(st) and sϕ(t) are additive
in t the case of general tensors follows.
□
Example 6.12. Let M be a torsion Z-module, so M = L
ℓM[ℓ∞] where the direct sum
runs over all primes ℓand M[ℓ∞] is the submodule of elements of M with ℓ-power order in
M. Then tensoring with the localization Z(p) for a prime p gives us
Z(p) ⊗Z M = Z(p) ⊗
M
ℓ
M[ℓ∞] =
M
ℓ
(Z(p) ⊗Z M[ℓ∞]).
When ℓ̸= p, Z(p) ⊗Z (M[ℓ∞]) = 0 since all elementary tensors there are 0, as ℓis a unit
in Z(p). Thus Z(p) ⊗Z M = Z(p) ⊗(M[p∞]), and Z(p) ⊗Z (M[p∞]) ∼= M[p∞] using natural
maps in both directions.
Thus when M = L
ℓZ/ℓZ, M is not ﬁnitely generated as a Z-module but each Z(p)⊗ZM
is ﬁnitely generated as a Z(p)-module since it is isomorphic to M[p∞] = Z/pZ.
The analogue of Theorem 6.11 for direct products of R-modules is false. The natural
S-linear map S ⊗R
Q
i∈I Mi →Q
i∈I(S ⊗R Mi) need not be an isomorphism. Here are two
examples.
• Q ⊗Z
Q
i≥1 Z/piZ is nonzero (Remark 5.5) but Q
i≥1(Q ⊗Z Z/piZ) is 0.
• Q⊗Z
Q
i≥1 Z is isomorphic as a Q-vector space not to Q
i≥1(Q⊗Z Z) ∼= Q
i≥1 Q, but
rather to the subgroup of Q
i≥1 Q consisting of rational sequences with a common
denominator. Under the natural map Q ⊗Z
Q
i≥1 Z →Q
i≥1 Q, the image of an
elementary tensor has coordinates with a common denominator, and each tensor
in Q ⊗Z
Q
i≥1 Z is a ﬁnite sum of elementary tenors, so its image in Q
i≥1 Q is a
sequence with a common denominator.
We now put base extensions to work. Let M be a ﬁnitely generated R-module, say with
n generators. That is the same as saying there is a linear surjection Rn ↠M. To say
M contains a subset of d linearly independent elements is the same as saying there is a
linear injection Rd ,→M. If both Rn ↠M and Rd ,→M, it is natural to suspect d ≤n,
i.e., the size of a spanning set should always be an upper bound on the size of a linearly
independent subset. Is it really true? If R is a ﬁeld, so modules are vector spaces, we can
use dimension inequalities on Rd, M, and Rn to see d ≤n. But if R is not a ﬁeld, then

<!-- page 40 -->
40
KEITH CONRAD
what? We will settle the issue in the aﬃrmative when R is a domain, by tensoring M with
the fraction ﬁeld of R to reduce to the case of vector spaces. We ﬁrst tensored R-modules
with the fraction ﬁeld of R as a special case of Theorem 4.27, but not much use was made
of the vector space structure of the tensor product with a ﬁeld. Now we exploit it.
Theorem 6.13. Let R be a domain with fraction ﬁeld K. For a ﬁnitely generated R-module
M, K ⊗R M is ﬁnite-dimensional as a K-vector space and dimK(K ⊗R M) is the maximal
number of R-linearly independent elements in M and is a lower bound on the size of a
spanning set for M. In particular, the size of each linearly independent subset of M is less
than or equal to the size of each spanning set of M.
Proof. If x1, . . . , xn is a spanning set for M as an R-module then 1 ⊗x1, . . . , 1 ⊗xn span
K ⊗R M as a K-vector space, so dimK(K ⊗R M) ≤n.
Let y1, . . . , yd be R-linearly independent in M.
We will show {1 ⊗yi} is K-linearly
independent in K ⊗R M, so d ≤dimK(K ⊗R M). Suppose Pd
i=1 ci(1 ⊗yi) = 0 with ci ∈K.
Write ci = ai/b using a common denominator b in R. Then 0 = 1/b⊗Pd
i=1 aiyi in K ⊗R M.
By Corollary 4.28, this implies Pd
i=1 aiyi ∈Mtor, so Pd
i=1 raiyi = 0 in M for some nonzero
r ∈R. By linear independence of the yi’s over R, every rai is 0, so every ai is 0 (R is a
domain). Thus every ci = ai/b is 0.
It remains to prove M has a linearly independent subset of size dimK(K ⊗R M). Let
{e1, . . . , ed} be linearly independent in M, withd maximal. (Since d ≤dimK(K ⊗R M),
there is a maximal d.) For every m ∈M, {e1, . . . , ed, m} has to be linearly dependent, so
there is a nontrivial R-linear relation
a1e1 + · · · + aded + am = 0.
Necessarily a ̸= 0, as otherwise all the ai’s are 0 by linear independence of the ei’s. In
K ⊗R M,
d
X
i=1
ai(1 ⊗ei) + a(1 ⊗m) = 0
and from the K-vector space structure on K ⊗R M we can solve for 1 ⊗m as a K-linear
combination of the 1⊗ei’s. Therefore {1⊗ei} spans K ⊗R M as a K-vector space. This set
is also linearly independent over K by the previous paragraph, so it is a basis and therefore
d = dimK(K ⊗R M).
□
While M has at most dimK(K⊗RM) linearly independent elements and this upper bound
is achieved, each spanning set has at least dimK(K ⊗R M) elements but this lower bound is
not necessarily reached. For example, if R is not a ﬁeld and M is a torsion module (e.g., R/I
for I a nonzero proper ideal) then K ⊗R M = 0 and M certainly doesn’t have a spanning
set of size 0 if M ̸= 0. It is also not true that ﬁniteness of dimK(K ⊗R M) implies M is
ﬁnitely generated as an R-module. Take R = Z and M = Q, so Q ⊗Z M = Q ⊗Z Q ∼= Q
(Example 4.22), which is ﬁnite-dimensional over Q but M is not ﬁnitely generated over Z.
The maximal number of linearly independent elements in an R-module M, for R a do-
main, is called the rank of M.24 This use of the word “rank” is consistent with its usage for
ﬁnite free modules as the size of a basis: if M is free with an R-basis of size n then K ⊗R M
has a K-basis of size n by Theorem 6.7.
24When R is not a domain, this concept of rank for R-modules is not quite the right one.

<!-- page 41 -->
TENSOR PRODUCTS
41
Example 6.14. A nonzero ideal I in a domain R has rank 1. We can see this in two ways.
First, any two nonzero elements in I are linearly dependent over R, so the maximal number
of R-linearly independent elements in I is 1. Second, K ⊗R I ∼= K as K-vector spaces (in
Theorem 4.23 we showed they are isomorphic as R-modules, but that isomorphism is also
K-linear; check!), so dimK(K ⊗R I) = 1.
Example 6.15. For a domain R with fraction ﬁeld K, a ﬁnitely generated R-module M
has rank 0 if and only if it is a torsion module, since K ⊗R M = 0 if and only if M is torsion.
Since K ⊗R M ∼= K ⊗R (M/Mtor) as K-vector spaces (the isomorphism between them
as R-modules in Theorem 4.27 is easily checked to be K-linear – check!), M and M/Mtor
have the same rank.
We return to general R, no longer a domain, and see how to make the tensor product of
an R-module and S-module into an S-module.
Theorem 6.16. Let M be an R-module and N be an S-module.
(1) The additive group M ⊗RN has a unique structure of S-module such that s(m⊗n) =
m ⊗sn for s ∈S. This is compatible with the R-module structure in the sense that
rt = f(r)t for r ∈R and t ∈M ⊗R N.
(2) The S-module M ⊗R N is isomorphic to (S ⊗R M) ⊗S N by sending m ⊗R n to
(1 ⊗R m) ⊗S n.
The point of part 2 is that it shows how the S-module structure on M ⊗R N can be
described as an ordinary S-module tensor product by base extending M to an S-module
S ⊗R M.
Part 2 has both R-module and S-module tensor products, and it is the ﬁrst
time that we must decorate the tensor product sign explicitly. Up to now it was actually
unnecessary, as all the tensor products were over R.
Writing S ⊗R M as M ⊗R S makes the isomorphism in part 2 notationally obvious, since
it becomes (M ⊗R S) ⊗S N ∼= M ⊗R N; this is similar to the “proof” of the chain rule in
diﬀerential calculus, dy/dx = (dy/du)(du/dx), by cancellation of du in the notation. This
kind of notational trick will be proved in greater generality in Theorem 6.26(3).
Proof. (1) This is similar to the proof of Theorem 6.4 (which is the special case N = S).
We just sketch the idea.
Since every tensor is a sum of elementary tensors, declaring how s ∈S scales elementary
tensors in M ⊗RN determines its scaling on all tensors. To show the rule s(m⊗n) = m⊗sn
really corresponds to an S-module structure, for each s ∈S we consider the function
M × N →M ⊗R N given by (m, n) 7→m ⊗sn. This is R-bilinear in m and n, so there is
an R-linear map µs : M ⊗R N →M ⊗R N such that µs(m ⊗n) = m ⊗sn on elementary
tensors. Deﬁne a multiplication S × (M ⊗R N) →M ⊗R N by st := µs(t). It is left to the
reader to check that the maps µs on M ⊗R N, as s varies, satisfy the scaling axioms that
make M ⊗R N an S-module.
To check rt = f(r)t for r ∈R and t ∈M ⊗R N, both sides are additive in t so it suﬃces
to check equality when t = m⊗n is an elementary tensor. In that case r(m⊗n) = m⊗rn =
m ⊗f(r)n = f(r)(m ⊗n).
(2) Let M × N →(S ⊗R M) ⊗S N by (m, n) 7→(1 ⊗R m) ⊗S n. We want to check this is
R-bilinear. Biadditivity is clear. For R-scaling, we have
(1 ⊗R rm) ⊗S n = (r(1 ⊗R m)) ⊗S n = (f(r)(1 ⊗R m)) ⊗S n = f(r)((1 ⊗R m) ⊗S n)

<!-- page 42 -->
42
KEITH CONRAD
and
(1 ⊗R m) ⊗S rn = (1 ⊗R m) ⊗S f(r)n = f(r)((1 ⊗R m) ⊗S n).
Now the universal mapping property of tensor products gives an R-linear map ϕ: M⊗RN →
(S ⊗R M)⊗S N where ϕ(m⊗R n) = (1⊗R m)⊗S n. This is exactly the map we were looking
for, but we only know it is R-linear so far. It is also S-linear: ϕ(st) = sϕ(t). To check this,
it suﬃces by additivity of ϕ to focus on the case of an elementary tensor:
ϕ(s(m ⊗R n)) = ϕ(m ⊗R sn) = (1 ⊗R m) ⊗S sn = s((1 ⊗R m) ⊗S n) = sϕ(m ⊗R n).
To show ϕ is an isomorphism, we create an inverse map (S ⊗R M)⊗S N →M ⊗R N. The
function S × M × N →M ⊗R N given by (s, m, n) 7→m ⊗sn is R-trilinear, so by Theorem
5.6 there is an R-bilinear map B : (S ⊗R M) × N →M ⊗R N where B(s ⊗m, n) = m ⊗sn.
This function is in fact S-bilinear:
B(st, n) = sB(t, n),
B(t, sn) = sB(t, n).
To check these equations, the additivity of both sides of the equations in t reduces us to
case when t is an elementary tensor. Writing t = s′ ⊗m,
B(s(s′ ⊗m), n) = B(ss′ ⊗m, n) = m ⊗ss′n = m ⊗s(s′n) = s(m ⊗s′n) = sB(s′ ⊗m, n)
and
B(s′ ⊗m, sn) = m ⊗s′(sn) = m ⊗s(s′n) = s(m ⊗s′n) = sB(s′ ⊗m, n).
Now the universal mapping property of the tensor product for S-modules tells us there is
an S-linear map ψ: (S ⊗R M) ⊗S N →M ⊗R N such that ψ(t ⊗n) = B(t, n).
It is left to the reader to check ϕ◦ψ and ψ ◦ϕ are identity functions, so ϕ is an S-module
isomorphism.
□
In addition to M ⊗R N being an S-module because N is, the tensor product N ⊗R M
in the other order has a unique S-module structure where s(n ⊗m) = sn ⊗m, and this is
proved in a similar way.
Example 6.17. For an S-module N, let’s show Rk ⊗R N ∼= Nk as S-modules. By Theorem
5.4, Rk ⊗R N ∼= (R⊗R N)k ∼= Nk as R-modules, an explicit isomorphism ϕ: Rk ⊗R N →Nk
being ϕ((r1, . . . , rk) ⊗n) = (r1n, . . . , rkn). Let’s check ϕ is S-linear: ϕ(st) = sϕ(t). Both
sides are additive in t, so we only need to check when t is an elementary tensor:
ϕ(s((r1, . . . , rk) ⊗n)) = ϕ((r1, . . . , rk) ⊗sn) = (r1sn, . . . , rksn) = sϕ((r1, . . . , rk) ⊗n).
To reinforce the S-module isomorphism
(6.3)
M ⊗R N ∼= (S ⊗R M) ⊗S N
from Theorem 6.16(2), let’s write out the isomorphism in both directions on appropriate
tensors:
m ⊗R n 7→(1 ⊗R m) ⊗S n,
(s ⊗R m) ⊗S n 7→m ⊗R sn.
Corollary 6.18. If M and M′ are isomorphic R-modules, and N is an S-module, then
M ⊗R N and M′ ⊗R N are isomorphic S-modules, as are N ⊗R M and N ⊗R M′.
Proof. We will show M ⊗R N ∼= M′ ⊗R N as S-modules. The other one is similar.
Let ϕ: M →M′ be an R-module isomorphism. To write down an S-module isomorphism
M ⊗R N →M′ ⊗R N, we will write down an R-module isomorphism that is also S-linear.
Let M × N →M′ ⊗R N by (m, n) 7→ϕ(m) ⊗n. This is R-bilinear (check!), so we get

<!-- page 43 -->
TENSOR PRODUCTS
43
an R-linear map Φ: M ⊗R N →M′ ⊗R N such that Φ(m ⊗n) = ϕ(m) ⊗n. This is also
S-linear: Φ(st) = sΦ(t). Since Φ is additive, it suﬃces to check this when t = m ⊗n:
Φ(s(m ⊗n)) = Φ(m ⊗sn) = ϕ(m) ⊗sn = s(ϕ(m) ⊗n) = sΦ(m ⊗n).
Using the inverse map to ϕ we get an R-linear map Ψ: M′ ⊗R N →M ⊗R N that is also
S-linear, and a computation on elementary tensors shows Φ and Ψ are inverses of each
other.
□
Example 6.19. We can use tensor products to prove the well-deﬁnedness of ranks of ﬁnite
free R-modules when R ̸= 0. Suppose Rm ∼= Rn as R-modules. Pick a maximal ideal m in
R (Zorn’s lemma) and R/m ⊗R Rm ∼= R/m ⊗R Rn as R/m-vector spaces by Corollary 6.18.
Therefore (R/m)m ∼= (R/m)n as R/m-vector spaces (Example 6.8), so taking dimensions of
both sides over R/m tells us m = n.
Here’s a conundrum. If N and N′ are both S-modules, then we can make N ⊗R N′ into
an S-module in two ways: s(n ⊗R n′) = sn ⊗R n′ and s(n ⊗R n′) = n ⊗R sn′. In the ﬁrst
S-module structure on N ⊗R N′, N′ only matters as an R-module. In the second S-module
structure, N only matters as an R-module. These two S-module structures on N ⊗R N′
are not generally the same because the tensor product is ⊗R, not ⊗S, so sn ⊗R n′ need not
equal n ⊗R sn′. But are the two S-module structures on N ⊗R N′ at least isomorphic to
each other? In general, no.
Example 6.20. Let R = Z and S = Z[
√
d] for nonsquare d ≡1 mod 4. Let I be the ideal
(2, 1 +
√
d) in S, so as a Z-module I = Z2 + Z(1 +
√
d). We will look at the S-module
structures on S ⊗Z I coming from scaling by S on the left and on the right.
As Z-modules, S and I are free of rank 2. When S ⊗Z I is an S-module by scaling by S
on the left, I only matters as a Z-module, so S ⊗Z I ∼= S ⊗Z Z2 as S-modules by Corollary
6.18. By Example 6.8, S ⊗Z Z2 ∼= S2 as S-modules. By making S ⊗Z I into an S-module
by scaling by S on the right, S ⊗Z I ∼= Z2 ⊗Z I ∼= I ⊕I as S-modules. If I ⊕I ̸∼= S2 as
S-modules then S ⊗Z I has diﬀerent S-module structures by S-scaling on the left and right.
The crucial property of I is that (check!) I2 = 2I, where I2 means the product II as an
ideal. That implies I is not a principal ideal in S: if I = αS then I2 = α2S, so α2S = 2αS,
which implies αS = 2S. However, 2S has index 4 in S while I has index 2 in S, so I is
nonprincipal. Thus I is not principal, so it is not a free S-module. Is it then obvious that
I ⊕I is not a free S-module? No! A direct sum of two nonfree modules can be free. For
instance, in Z[√−5] the ideals I = (3, 1+√−5) and J = (3, 1−√−5) are both nonprincipal
but it can be shown that I ⊕J ∼= Z[√−5] ⊕Z[√−5] as Z[√−5]-modules. The reason a
direct sum of non-free modules can sometimes be free is that there is more room to move
around in a direct sum than just within the direct summands, and this extra room might
contain a basis. So showing I ⊕I is not a free S-module requires work.
Using more advanced tools in multilinear algebra (speciﬁcally, exterior powers), one can
show that if I ⊕I ∼= S2 as S-modules then I ⊗S I ∼= S as S-modules. Then since multi-
plication gives a surjective S-linear map I ⊗S I ↠I2 (where x ⊗y 7→xy), there would be
a surjective S-linear map S ↠I2, which means I2 would be a principal ideal. However,
I2 = 2I and I is not principal, so I2 is not principal.
The lesson from this example is that if you want N ⊗R N′ to be an S-module where N
and N′ are S-modules, you have to specify whether S scales on the left or the right. That
two S-modules structures on N ⊗R N′ are the same or at least isomorphic needs a proof.
Here is one such example, where R is a domain and S = K is its fraction ﬁeld.

<!-- page 44 -->
44
KEITH CONRAD
Theorem 6.21. Let R be a domain, with fraction ﬁeld K. For K-vector spaces V and W,
the K-vector space structures on V ⊗R W using K-scaling on either the V or W factor are
the same.
Proof. The two K-vector space structures on V ⊗R W are based on either the formula
x(v ⊗R w) = xv ⊗R w on elementary tensors or the formula x(v ⊗R w) = v ⊗R xw on
elementary tensors, where x ∈K and we write ⊗R rather than ⊗in the elementary tensors
for emphasis.25 Proving that the two K-vector space structures on V ⊗R W agree amounts
to showing xv ⊗R w = v ⊗R xw for all x ∈K, v ∈V , and w ∈W. This is something we
dealt with back in the proof of Theorem 4.21, and now we’ll apply that argument again.
Write x = a/b with a, b ∈R and b ̸= 0. Then (xv) ⊗R w equals
a
b v

⊗R w = a
1
bv

⊗R w = 1
bv ⊗R aw = 1
bv ⊗R b
a
b w

= b
1
bv

⊗R
a
b w = v ⊗R
a
b w,
which is v ⊗R xw.
□
It would have been wrong to complete the proof by immediately writing xv ⊗R w =
v ⊗R xw, because we are working with an R-module tensor product and the scalar x is
not limited to R. We can say in one step that xv ⊗R w = v ⊗R xw when x ∈R, but
to say this holds when x ∈K needed justiﬁcation. (For comparison, in C ⊗R C we have
1 ⊗R i ̸= i ⊗R 1 since these are diﬀerent members of a basis. More generally, check using
bases that z ⊗R iw ̸= iz ⊗R w in C ⊗R C except when z or w is 0. This doesn’t violate
Theorem 6.21 since C is not the fraction ﬁeld of R.)
Corollary 6.22. With notation as in Theorem 6.21, V ⊗R W ∼= V ⊗K W as K-vector
spaces by v ⊗R w 7→v ⊗K w.
There is no ambiguity about what we mean by V ⊗R W as a K-vector space, since the
K-scaling via V or W is exactly the same by Theorem 6.21.
Proof. We will give two proofs.
The mapping V × W →V ⊗K W given by (v, w) 7→v ⊗K w is R-bilinear, so there is
a unique R-linear mapping ϕ: V ⊗R W →V ⊗K W given by ϕ(v ⊗R w) = v ⊗K w on
elementary tensors. To show ϕ is K-linear, it suﬃces to check ϕ(xt) = xϕ(t) when t is an
elementary tensor, so we want to check ϕ(x(v ⊗R w)) = x(v ⊗K w). By the deﬁnition of the
K-vector space structure on V ⊗R W, ϕ(x(v ⊗R w)) = ϕ((xv) ⊗R w) = (xv) ⊗K w, which is
x(v ⊗K w). (We could also say ϕ(x(v ⊗R w)) = ϕ(v ⊗R xw) = v ⊗K xw, which is x(v ⊗K w).)
The mapping V × W →V ⊗R W given by (v, w) 7→v ⊗R w is not just R-bilinear, but
K-bilinear. For example, (xv, w) 7→(xv) ⊗R w = x(v ⊗R w). Thus we get a K-linear map
ψ: V ⊗K W 7→V ⊗R W by ψ(v ⊗K w) = v ⊗R w. Since ϕ ◦ψ and ψ ◦ϕ are both additive
and ﬁx all elementary tensors (in V ⊗K W and V ⊗R W, respectively), they ﬁx all tensors
and thus ϕ and ψ are inverses. Therefore ϕ is an isomorphism of K-vector spaces.
Another reason V ⊗R W ∼= V ⊗K W as K-vector spaces is that V ⊗R W satisﬁes the
universal mapping property of V ⊗K W! Let’s check this. The canonical R-bilinear map
V × W →V ⊗R W is not just R-bilinear, but K-bilinear (why?). Then for each K-vector
25These scaling formulas are not really deﬁnitions of scalar multiplication by K on V ⊗R W, since tensors
are not unique sums of elementary tensors. That such scaling formulas are well-deﬁned operatios on V ⊗K W
requires creating the scaling functions as in the proof of part 1 of Theorem 6.16.

<!-- page 45 -->
TENSOR PRODUCTS
45
space U and K-bilinear map B : V × W →U, since B is R-bilinear the universal mapping
property of V ⊗R W tells us that there is a unique R-linear map L making the diagram
V ⊗R W
L

V × W
⊗R
8
B
& U
commute, and on account of the fact that U and V ⊗R W are already K-vector spaces you
can check that L is in fact K-linear (and is the only K-linear map that can ﬁt into the
above commutative diagram). Two solutions of a universal mapping property are uniquely
isomorphic to each other, so V ⊗RW ∼= V ⊗KW. More speciﬁcally, using for B the canonical
K-bilinear map V × W →V ⊗K W implies that the diagram
V ⊗R W
v⊗Rw7→v⊗Kw

V × W
⊗R
8
⊗K
&
V ⊗K W
commutes, and by universality the vertical map has to be an isomorphism.
□
Example 6.23. We saw in Example 4.29 that R⊗Z(R/πZ) ∼= R⊗Z(R/πQ) as Z-modules.
Both R and R/πQ are Q-vector spaces, so R ⊗Z (R/πQ) is a Q-vector space using Q-
scaling on either R or R/πQ.
By Corollary 6.22, R ⊗Z (R/πQ) ∼= R ⊗Q (R/πQ) as
Q-vector spaces. Diﬀerent descriptions of the Dehn invariant used to solve Hilbert’s 3rd
problem place values of that invariant in R ⊗Z (R/πZ), R ⊗Z (R/πQ), or R ⊗Q (R/πQ),
and the choice doesn’t really matter since they are essentially the same thing.
Example 6.24. Since R is a Q-vector space, R ⊗Z R ∼= R ⊗Q R as Q-vector spaces by
x ⊗Z y 7→x ⊗Q y. Is there a “formula” for R ⊗Q R? Yes and no. Since R is uncountable,
if {ei} is a Q-basis of R, then this basis has cardinality equal to the cardinality of R, and
R ⊗Q R has Q-basis {ei ⊗ej}, whose cardinality is also the same as R, so we could say
R ⊗Q R is isomorphic to R as Q-vector spaces. However, this isomorphism is completely
nonconstructive.
Recalling that R⊗R R ∼= R as R-vector spaces by x⊗R y 7→xy, might the Q-linear map
R⊗QR →R given by x⊗Qy 7→xy on elementary tensors be an isomorphism? It is obviously
surjective, but this map is far from being injective. For example, since π is transcendental
its powers 1, π, π2, . . . are linearly independent over Q, so the tensors πi ⊗Q πj in R ⊗Q R
are linearly independent over Q. (Zorn’s lemma lets us enlarge the powers of π to a Q-basis
of R, so the tensors πi ⊗Q πj are part of a Q-basis by Theorem 4.9 and thus are linearly
independent.) Then for n ≥2 the tensor πn ⊗1+πn−1 ⊗π +· · ·+π ⊗πn−1 −(n−1)(1⊗πn)
in R ⊗Q R is nonzero and its image in R is (n −1)πn −(n −1)πn = 0.
Another failed attempt at trying to make R ⊗Q R look like R concretely comes from
treating R ⊗Q R as a real vector space using scaling on the left (or on the right, but that

<!-- page 46 -->
46
KEITH CONRAD
is a diﬀerent scaling structure since π ⊗1 ̸= 1 ⊗π). Its dimension over R is inﬁnite by
Theorem 6.7, which is pretty far from the behavior of R as a real vector space.
Remark 6.25. Theorem 6.21 and its corollary remain true, by the same proofs, with
localizations in places of fraction ﬁelds. If R is a ring, D is a multiplicative subset of R,
and N and N′ are D−1R-modules, then the two D−1R-module structures on N ⊗R N′,
using D−1R-scaling on either N or N′, are the same: for x ∈D−1R, xn ⊗R n′ = n ⊗R xn′.
Moreover, the natural D−1R-module mapping N ⊗R N′ →N ⊗D−1R N′ determined by
n ⊗R n′ 7→n ⊗D−1R n′ on elementary tensors is an isomorphism of D−1R-modules.
The next theorem collects a number of earlier tensor product isomorphisms for R-modules
and shows the same maps are S-module isomorphisms when one of the R-modules in the
tensor product is an S-module.
Theorem 6.26. Let M and M′ be R-modules and N and N′ be S-modules.
(1) There is a unique S-module isomorphism
M ⊗R N →N ⊗R M
where m⊗n 7→n⊗m. In particular, S⊗RM and M ⊗RS are isomorphic S-modules.
(2) There are unique S-module isomorphisms
(M ⊗R N) ⊗R M′ →N ⊗R (M ⊗R M′)
where (m ⊗n) ⊗m′ 7→n ⊗(m ⊗m′) and
(M ⊗R N) ⊗R M′ ∼= M ⊗R (N ⊗R M′)
where (m ⊗n) ⊗m′ 7→m ⊗(n ⊗m′).
(3) There is a unique S-module isomorphism
(M ⊗R N) ⊗S N′ →M ⊗R (N ⊗S N′)
where (m ⊗n) ⊗n′ 7→m ⊗(n ⊗n′).
(4) There is a unique S-module isomorphism
N ⊗R (M ⊕M′) →(N ⊗R M) ⊕(N ⊗R M′)
where n ⊗(m, m′) 7→(n, m) ⊗(n, m′).
In the ﬁrst, second, and fourth parts, we are using R-module tensor products only and
then endowing them with S-module structure from one of the factors being an S-module
(Theorem 6.16). In the third part we have both ⊗R and ⊗S.
Proof. There is a canonical R-module isomorphism M ⊗R N →N ⊗R M where m ⊗n 7→
n ⊗m. This map is S-linear using the S-module structure on both sides (check!), so it is
an S-module isomorphism. This settles part 1.
Part 2, like part 1, only uses R-module tensor products, so there is an R-module isomor-
phism ϕ: (M ⊗RN)⊗RM′ →N ⊗R(M ⊗RM′) where ϕ((m⊗n)⊗m′) = n⊗(m⊗m′). Using
the S-module structure on M ⊗R N, (M ⊗R N) ⊗R M′, and N ⊗R (M ⊗R M′), ϕ is S-linear
(check!), so it is an S-module isomorphism. To derive (M ⊗R N)⊗R M′ ∼= M ⊗R (N ⊗R M′)
from (M ⊗R N) ⊗R M′ ∼= N ⊗R (M ⊗R M′), use a few commutativity isomorphisms.

<!-- page 47 -->
TENSOR PRODUCTS
47
Part 3 resembles associativity of tensor products. We will in fact derive part 3 from such
associativity for ⊗S:
(M ⊗R N) ⊗S N′ ∼= ((S ⊗R M) ⊗S N) ⊗S N′ by (6.3)
∼= (S ⊗R M) ⊗S (N ⊗S N′) by associativity of ⊗S
∼= M ⊗R (N ⊗S N′) by (6.3).
These successive S-module isomorphisms have the eﬀect
(m ⊗n) ⊗n′ 7→((1 ⊗m) ⊗n) ⊗n′
7→(1 ⊗m) ⊗(n ⊗n′)
7→m ⊗(n ⊗n′),
which is what we wanted.
For part 4, there is an R-module isomorphism N ⊗R (M ⊕M′) →(N ⊗R M)⊕(N ⊗R M′)
by Theorem 5.4. Now it’s just a matter of checking this map is S-linear using the S-module
structure on both sides coming from N being an S-module, and this is left to the reader.
As an alternate proof, we have a chain of S-module isomorphisms
N ⊗R (M ⊕M′) ∼= N ⊗S
 S ⊗R (M ⊕M′)

by part 1 and (6.3)
∼= N ⊗S ((S ⊗R M) ⊕(S ⊗R M′)) by Theorem 6.11
∼= (N ⊗S (S ⊗R M)) ⊕(N ⊗S (S ⊗R M′)) by Theorem 5.4
∼= (N ⊗R M) ⊕(N ⊗R M′) by part 1 and (6.3).
Of course one needs to trace through these isomorphisms to check the overall result has the
eﬀect intended on elementary tensors, and it does (exercise).
□
The last part of Theorem 6.26 extends to arbitrary direct sums: the natural R-module
isomorphism N ⊗R
L
i∈I Mi ∼= L
i∈I(N ⊗R Mi) is also an S-module isomorphism.
As an application of Theorem 6.26, we can show the base extension of an R-module
tensor product “is” the S-module tensor product of the base extensions:
Corollary 6.27. For R-modules M and M′, there is a unique S-module isomorphism
S ⊗R (M ⊗R M′) →(S ⊗R M) ⊗S (S ⊗R M′)
where s ⊗R (m ⊗R m′) 7→s((1 ⊗R m) ⊗S (1 ⊗R m′)).
Proof. Since M ⊗R M′ is additively spanned by all m ⊗m′, S ⊗R (M ⊗R M′) is additively
spanned by all s ⊗R (m ⊗R m′).
Therefore an S-linear (or even additive) map out of
S ⊗R (M ⊗R M′) is determined by its values on the tensors s ⊗R (m ⊗R m′).
We have the S-module isomorphisms
S ⊗R (M ⊗R M′) ∼= M ⊗R (S ⊗R M′) by Theorem 6.26(2)
∼= (S ⊗R M) ⊗S (S ⊗R M′) by (6.3).
The eﬀect of these isomorphisms on s ⊗R (m ⊗R m′) is
s ⊗R (m ⊗R m′) 7→m ⊗R (s ⊗R m′)
7→(1 ⊗R m) ⊗S (s ⊗R m′)
= (1 ⊗R m) ⊗S s(1 ⊗R m′)
= s((1 ⊗R m) ⊗S (1 ⊗R m′)),

<!-- page 48 -->
48
KEITH CONRAD
as desired. The eﬀect of the inverse isomorphism on (s1 ⊗R m) ⊗S (s2 ⊗R m′) is
(s1 ⊗R m) ⊗S (s2 ⊗R m′) 7→m ⊗R s1(s2 ⊗R m′)
= m ⊗R ((s1s2) ⊗R m′)
7→s1s2 ⊗R (m ⊗R m′).
□
Theorem 6.27 could also be proved by showing the S-module S ⊗R (M ⊗R M′) has the
universal mapping property of (S ⊗R M) ⊗S (S ⊗R M′) as a tensor product of S-modules.
That is left as an exercise.
Corollary 6.28. For R-modules M1, . . . , Mk,
S ⊗R (M1 ⊗R · · · ⊗R Mk) ∼= (S ⊗R M1) ⊗S · · · ⊗S (S ⊗Mk)
as S-modules, where s ⊗S (m1 ⊗R · · · ⊗R mk) 7→s((1 ⊗R m1) ⊗S · · · ⊗S (1 ⊗R mk)). In
particular, S ⊗R (M⊗Rk) ∼= (S ⊗R M)⊗Sk as S-modules.
Proof. Induct on k.
□
Example 6.29. For a real vector space V , C ⊗R (V ⊗R V ) ∼= (C ⊗R V ) ⊗C (C ⊗R V ).
The middle tensor product sign on the right is over C, not R. Note that C ⊗R (V ⊗R V ) ̸∼=
(C ⊗R V ) ⊗R (C ⊗R V ) when V ̸= 0, as the two sides have diﬀerent dimensions over R
(what are they?).
The base extension M ⇝S ⊗R M turns R-modules into S-modules in a systematic way.
So does M ⇝M ⊗R S, and this is essentially the same construction. This suggests there
should be a universal mapping problem about R-modules and S-modules that is solved by
base extension, and there is: it is the universal device for turning each R-linear map from
M to an S-module into an S-linear map of S-modules.
Theorem 6.30. Let M be an R-module. For every S-module N and R-linear map ϕ: M →
N, there is a unique S-linear map ϕS : S ⊗R M →N such that the diagram
M
m7→1⊗m
/
ϕ
 
S ⊗R M
ϕS
z
N
commutes.
This says the single R-linear map M →S ⊗R M from M to an S-module explains all
other R-linear maps from M to S-modules using composition of it with S-linear maps from
S ⊗R M to S-modules.
Proof. Assume there is such an S-linear map ϕS. We will derive a formula for it on elemen-
tary tensors:
ϕS(s ⊗m) = ϕS(s(1 ⊗m)) = sϕS(1 ⊗m) = sϕ(m).
This shows ϕS is unique if it exists.
To prove existence, consider the function S × M →N by (s, m) 7→sϕ(m). This is R-
bilinear (check!), so there is an R-linear map ϕS : S⊗RM →N such that ϕS(s⊗m) = sϕ(m).
Using the S-module structure on S ⊗R M, ϕS is S-linear.
□
For ϕ in HomR(M, N), ϕS is in HomS(S ⊗R M, N). Because ϕS(1 ⊗m) = ϕ(m), we can
recover ϕ from ϕS. But even more is true.

<!-- page 49 -->
TENSOR PRODUCTS
49
Theorem 6.31. Let M be an R-module and N be an S-module. The function ϕ 7→ϕS is
an S-module isomorphism HomR(M, N) →HomS(S ⊗R M, N).
How is HomR(M, N) an S-module? Values of these functions are in N, which is an S-
module, so each s ∈S turns each function M →N into a new function M →N by just
scaling the values by s.
Proof. For ϕ and ϕ′ in HomR(M, N), (ϕ + ϕ′)S = ϕS + ϕ′S and (sϕ)S = sϕS by checking
both sides are equal on all elementary tensors in S ⊗R M. Therefore ϕ 7→ϕS is S-linear.
Its injectivity is discussed above (ϕS determines ϕ).
For surjectivity, let h: S ⊗R M →N be S-linear. Set ϕ: M →N by ϕ(m) = h(1 ⊗m).
Then ϕ is R-linear and ϕS(s ⊗m) = sϕ(m) = sh(1 ⊗m) = h(s(1 ⊗m)) = h(s ⊗m), so
h = ϕS since both are additive and are equal at all elementary tensors.
□
The S-module isomorphism
(6.4)
HomR(M, N) ∼= HomS(S ⊗R M, N)
should be thought of as analogous to the R-module isomorphism
(6.5)
HomR(M, HomR(N, P)) ∼= HomR(M ⊗R N, P)
from Theorem 5.7, where −⊗R N is left adjoint to HomR(N, −). (In (6.5), N and P are
R-modules, not S-modules! We’re using the same notation as in Theorem 5.7.) If we look
at (6.4), we see S ⊗R −is applied to M on the right but nothing special is applied to N
on the left. Yet there is something diﬀerent about N on the two sides of (6.4). It is an
S-module on the right side of (6.4), but on the left side it is being treated as an R-module
(restriction of scalars). That changes N, but we have introduced no notation to reﬂect this.
We still just write it as N. Let’s now write ResS
R(N) to denote N as an R-module. It is the
same underlying additive group as N, but the scalars are now taken from (”restricted to”)
R by the rule rn := f(r)n. The isomorphism in (6.4) now has a more precise appearance:
(6.6)
HomR(M, ResS
R(N)) ∼= HomS(S ⊗R M, N).
So extension of scalars (from R-modules to S-modules) is left adjoint to restriction of scalars
(from S-modules to R-modules) in a similar way that −⊗RM is left adjoint to HomR(M, −).
Remark 6.32. In representation theory, Frobenius reciprocity is like (6.6). If you know
Frobenius reciprocity, recall it says HomC[G](IndG
H(W), V ) ∼= HomC[H](W, ResG
H(V )) when
G is a group, H is a subgroup, V is a G-representation, W is an H-representation, and IndG
H
and ResG
H are the induction and restriction operations on representations. In terms of group
rings, IndG
H(W) = C[G] ⊗C[H] W and ResG
H(W) = ResC[G]
C[H](W), so Frobenius reciprocity is
like (6.6) with R and S replaced by C[H] and C[G]. The catch is that the group rings C[H]
and C[G] are possibly noncommutative and we have not discussed how tensor products of
modules over noncommutative rings are even deﬁned (recall footnote 7).
Using our new notation for restriction of scalars, the important S-module isomorphism
(6.3) can be written more explicitly as
M ⊗R ResS
R(N) ∼= (S ⊗R M) ⊗S N,
Theorem 6.33. Let M be an R-module and N and P be S-modules. There is an S-module
isomorphism
HomS(M ⊗R N, P) ∼= HomR(M, ResS
R(HomS(N, P))).

<!-- page 50 -->
50
KEITH CONRAD
Example 6.34. Taking N = S, so M ⊗R N = M ⊗R S ∼= S ⊗R M, Theorem 6.33 says
HomS(S ⊗R M, P) ∼= HomR(M, ResS
R(P))
since HomS(S, P) ∼= P. This is (6.6) written in reverse order, recovering S ⊗R −being left
adjoint to ResS
R.
Example 6.35. Taking S = R, so N and P are now R-modules,
HomR(M ⊗R N, P) ∼= HomR(M, HomR(N, P)).
This recovers −⊗R N being left adjoint to HomR(N, −) for R-modules N.
These two consequences of Theorem 6.33 are results we have already seen, and in fact we
are going to use them in the proof, so they are together equivalent to Theorem 6.33.
Proof. Since M ⊗R N ∼= (S ⊗R M) ⊗S N as S-modules,
HomS(M ⊗R N, P) ∼= HomS((S ⊗R M) ⊗S N, P).
Since −⊗S N is left adjoint to HomS(N, −),
HomS((S ⊗R M) ⊗S N, P) ∼= HomS(S ⊗R M, HomS(N, P)).
Since S ⊗R −is left adjoint to ResS
R,
HomS(S ⊗R M, HomS(N, P)) ∼= HomR(M, ResS
R(HomS(N, P))).
Combining these three isomorphisms,
HomS(M ⊗R N, P) ∼= HomR(M, ResS
R(HomS(N, P))).
Here is an explicit (overall) isomorphism. If ϕ: M ⊗RN →P is S-linear there is an R-linear
map Lϕ : M →HomS(N, P) by Lϕ(m) = ϕ(m ⊗(−)). If ψ: M →HomS(N, P) is R-linear
then M × N →P by (m, n) 7→ψ(m)(n) is R-bilinear and ψ(m)(sn) = sψ(m)(n), so the
corresponding R-linear map eLψ : M ⊗R N →P where eLψ(m ⊗n) = ψ(m)(n) is S-linear.
The functions ϕ 7→Lϕ and ψ 7→eLψ are S-linear and are inverses.
□
7. Tensors in Physics
In physics and engineering, tensors are often deﬁned not in terms of multilinearity, but
by the way tensors look in diﬀerent coordinate systems. Here is a deﬁnition of a tensor
that can be found (more or less) in many physics textbooks. Let V be a vector space26
with dimension n ≥1. A tensor of rank 0 on V is a scalar. For k ≥1, a contravariant
tensor of rank k27 (on V ) is an object T with nk components in every coordinate system
of V such that if {T i1,...,ik}1≤i1,...,ik≤n and { eT i1,...,ik}1≤i1,...,ik≤n are the components of T in
two coordinate systems of V then
(7.1)
eT i1,...,ik =
X
1≤j1,...,jk≤n
T j1,...,jkai1j1 · · · aikjk,
where (aij) is the matrix is the matrix expressing the ﬁrst coordinate system of V in terms
of the second. In short, a contravariant tensor of rank k is a “quantity that transforms by
the rule (7.1).”
26Physicists are interested only in real or complex vector spaces.
27This meaning of the term “rank of a tensor” as the number of indices is unrelated to the meaning of
“rank of a tensor” near the end of Section 5 in terms of a sum of elementary tensors.

<!-- page 51 -->
TENSOR PRODUCTS
51
What is being described here, with components, is just an element of V ⊗k. To see this,
note that a coordinate system means a choice of a basis of V . For each basis28 {e1, . . . , en}
of V , in which T has components {T i1,...,ik}1≤i1,...,ik≤n, make these numbers the coeﬃcients
of the basis {ei1 ⊗· · · ⊗eik} of V ⊗k:
X
1≤i1,...,ik≤n
T i1,...,ikei1 ⊗· · · ⊗eik.
This belongs to V ⊗k. Let’s express this sum in terms of a second basis (“coordinate system”)
{f1, . . . , fn} of V . Writing ej = Pn
i=1 aijfi, the above sum equals, after a notational change,
X
1≤j1,...,jk≤n
T j1,...,jkej1 ⊗· · · ⊗ejk
=
X
1≤j1,...,jk≤n
T j1,...,jk
 n
X
i1=1
ai1j1fi1
!
⊗· · · ⊗


n
X
ik=1
aikjkfik


=
X
1≤i1,...,ik≤n


X
1≤j1,...,jk≤n
T j1,...,jkai1j1 · · · aikjk

fi1 ⊗· · · ⊗fik
=
X
1≤i1,...,ik≤n
eT i1,...,ikfi1 ⊗· · · ⊗fik
by (7.1).
So in physics, the components of a contravariant rank k tensor on V are the coeﬃcients of
an element of V ⊗k in some basis29 of V ⊗k. In physics, dim V is usually 3 or 4.
Switching from tensor powers of V to tensor powers of its dual space V ∨, we now want
to compare the representations of an element of (V ∨)⊗ℓin coordinate systems built from
the two dual bases e∨
1 , . . . , e∨
n and f∨
1 , . . . , f∨
n of V ∨. The formula we ﬁnd will be similar to
(7.1), but with a crucial change.
To align calculations with how they’re done in physics and diﬀerential geometry, from now
on write the dual bases of {e1, . . . , en} and {f1, . . . , fn} as {e1, . . . , en} and {f1, . . . , fn},
not {e∨
1 , . . . , e∨
n} and {f∨
1 , . . . , f∨
n }. So ei(ej) = fi(fj) = δij for all i and j.
For a basis {e1, . . . , en} of V and its dual basis {e1, . . . , en} in V ∨, general elements of V
and V ∨are written as Pn
i=1 ciei and Pn
i=1 ciei, respectively. A basis of V always has lower
indices and its coeﬃcients have upper indices, while a basis of V ∨always has upper indices.
and its coeﬃcients have lower indices. See the table below.
Space
Basis
Coeﬀ.
Element
V
ei
ci
P ciei
V ∨
ei
ci
P ciei
The convention of lower indices for a basis of V and for coeﬃcients of a basis in V ∨
and upper indices for a basis of V ∨and for coeﬃcients of a basis in V is consistent since
the coeﬃcients ai of the vector Pn
i=1 aiei in V are the values of e1, . . . , en on this vector:
coeﬃcients of a basis are coordinate functions, and coordinate functions of a basis of V lie
in V ∨while, by duality, coordinate functions of a basis of V ∨lie in (V ∨)∨∼= V .
28We really should speak of an ordered basis of V , since e1 ⊗e2 ̸= e2 ⊗e1.
29Strictly speaking we aren’t using every possible basis of V ⊗k but only bases of V ⊗k built as k-fold
elementary tensors from a basis of V .

<!-- page 52 -->
52
KEITH CONRAD
Pick a mathematician’s tensor T ∈(V ∨)⊗ℓand write it in the basis {ei1 ⊗· · · ⊗eiℓ} as
(7.2)
T =
X
1≤i1,...,iℓ≤n
Ti1,...,iℓei1 ⊗· · · ⊗eiℓ,
where the coeﬃcients have lower indices, not upper indices, to be consistent with the idea
that this is a dual object (lies in a tensor power of V ∨). To express T in terms of the second
basis {fi1 ⊗· · · ⊗fiℓ} of (V ∨)⊗ℓ, we want to express the ej’s in terms of the fi’s in V ∨.
We already wrote ej = Pn
i=1 aijfi in V for all j, and it turns out that
(7.3)
ej =
n
X
i=1
aijfi for all j =⇒fj =
n
X
i=1
ajiei for all j.
Indeed, the coeﬃcient of ei is fj(ei) = fj(P
k akifk) = aji. We see transposed matrix entries
(aji) on the right side of (7.3) in an essential way: j in (7.3) is the second index of aij and
the ﬁrst index of aji. It is a fact of life that passing to the dual space involves a transpose.
Alas, (7.3) gives a change of basis formula in V ∨for fj’s in terms of ei’s, which is not the
direction we need to transform the right side of (7.2) to a sum involving fi’s: we want the
ej’s in terms of the fi’s, not the fj’s in terms of the ei’s. So we need an inverse on top of
the transposing.
Writing the inverse of the matrix (aij) as (aij), the following table summarizes how a
change of basis matrix changes to describe a related change of basis.
Space
Start
End
Matrix
V
f1, . . . , fn
e1, . . . , en
(aij) – deﬁnition
V
e1, . . . , en
f1, . . . , fn
(aij) = (aij)−1
V ∨
e1, . . . , en
f1, . . . , fn
(aji) = (aij)⊤
V ∨
f1, . . . , fn
e1, . . . , en
(aji) = (aij)⊤
The third row of the table is (7.3) and the second and fourth rows of the table say
(7.4)
ej =
n
X
i=1
aijfi for all j =⇒fj =
n
X
i=1
aijei, and ej =
n
X
i=1
ajifi for all j.
Example 7.1. Let dim(V ) = 2 with bases {e1, e2} and {f1, f2}. Suppose that
e1 = f1 + 2f2 and e2 = 3f2.
It follows by simple algebra that
f1 = e1 −2
3e2 and f2 = 1
3e2.
Write these as ej = P2
i=1 aijfi and fj = P2
i=1 aijei for
(7.5)
(aij) =

1
0
2
3

and (aij) =

1
0
−2/3
1/3

,
which are inverses.
In V ∨, to write {f1, f2} in terms of {e1, e2} set f1 = ae1 + be2. Evaluating both sides at
f1 and f2 we have 1 = ae1(f1) + be2(f1) = a + b(−2/3) and 0 = ae1(f2) + be2(f2) = b(1/3).
Thus b = 0 and a = 1, so f1 = e1. Similarly, f2 = 2e1 + 3e2 and we can solve for e1 and e2:
f1 = e1 and f2 = 2e1 + 3e2 =⇒e1 = f1 and e2 = −2
3f1 + 1
3f2.

<!-- page 53 -->
TENSOR PRODUCTS
53
Then fj = P2
i=1 ajiei and ej = P2
i=1 ajifi, with coeﬃcients forming transposed matrices
to (7.5).
The change of basis we need for (7.2) is ej’s in terms of fi’s, so isolate that part of (7.4):
(7.6)
ej =
n
X
i=1
aijfi for all j =⇒ej =
n
X
i=1
ajifi for all j.
As a reminder, (aji) is the transpose of the inverse of the matrix (aij).
Returning to (7.2),
T =
X
1≤j1,...,jℓ≤n
Tj1,...,jℓej1 ⊗· · · ⊗ejℓ
=
X
1≤j1,...,jℓ≤n
Tj1,...,jℓ
 n
X
i1=1
aj1i1fi1
!
⊗· · · ⊗


n
X
iℓ=1
ajℓiℓfiℓ


by (7.6)
=
X
1≤i1,...,iℓ≤n


X
1≤j1,...,jℓ≤n
Tj1,...,jℓaj1i1 · · · ajℓiℓ

fi1 ⊗· · · ⊗fiℓ.
The component-based approach to (V ∨)⊗ℓis based on this calculation. A “quantity with
nk components that transforms by the rule”
(7.7)
eTi1,...,iℓ=
X
1≤j1,...,jℓ≤n
Tj1,...,jℓaj1i1 · · · ajℓiℓ
when passing from the basis {e1, . . . , en} to the basis {f1, . . . , fn} of V ∨, is called a covariant
tensor of rank ℓ. This is just an element of (V ∨)⊗ℓ, and (7.7) explains operationally how
diﬀerent coordinate representations of this tensor are related to one another.
The rules (7.1) for components in V ⊗k and (7.7) for components in (V ∨)⊗ℓare diﬀerent,
and not just on account of the convention about indices being upper on tensor components
in (7.1) and lower on tensor components in (7.7). If we place (7.1) and (7.7) side by side
and, to avoid being distracted by tensor index notational conventions, we temporarily make
all tensor-component indices lower and give the tensor components the same number of
indices (ℓ= k, so we are in V ⊗k and (V ∨)⊗k), we obtain this:
eTi1,...,ik =
X
1≤j1,...,jk≤n
Tj1,...,jkai1j1 · · · aikjk,
eTi1,...,ik =
X
1≤j1,...,jk≤n
Tj1,...,jkaj1i1 · · · ajkik.
We did not lower the indices of aji in the second sum because its indices reﬂect something
serious: (aij) is the matrix expressing a change of coordinates in V and (aji) is the matrix
expressing the dual change of coordinates in V ∨in the same direction (see (7.6)). The use of
aij or aji is the diﬀerence between the transformation rules in tensor powers of V and tensor
powers of V ∨. Both of the transformation rules involve a multilinear change of coordinates
(as evidenced by the multiple products in the sums), but in the ﬁrst rule the summation
indices appear in the multipliers airjr as the second index, while in the second rule the
summation indices appear in the multipliers ajrir as the ﬁrst index. This swap happens
because physicists always start a change of basis in V , and passing to the eﬀect in V ∨
necessitates a transpose (and inverse). The reason for systematically using upper indices
on tensor components satisfying (7.1) and lower indices on tensor components satisfying

<!-- page 54 -->
54
KEITH CONRAD
(7.7) is to know at a glance (with experience) what type of transformation rule the tensor
components will satisfy under a change in coordinates.
Here is some terminology about tensors that is used by physicists.
• A contravariant tensor of rank k, which is an indexed quantity T i1...ik that transforms
by (7.1), is also called a tensor of rank k with upper indices (easier to remember!).
• A covariant tensor of rank ℓ, which is an indexed quantity Tj1...jℓthat transforms
by (7.7), is also called a tensor of rank ℓwith lower indices.
• An indexed quantity T i1...ik
j1...jℓthat transforms by the rule
(7.8)
eT i1...ik
j1...jℓ=
X
1≤p1,...,pk≤n
1≤q1,...,qℓ≤n
T p1...pk
q1...qℓai1p1 · · · aikpkaq1j1 · · · aqℓjℓ
is called a tensor of type (k, ℓ) and rank k + ℓ. This “quantity” is just an element of
V ⊗k ⊗(V ∨)⊗ℓwritten in terms of elementary tensor product bases produced from
a basis of V (check!). For instance, elements of V ⊗V , V ⊗V ∨, and V ∨⊗V ∨are
rank 2 tensors. An element of V ⊗2 ⊗V ∨has rank 3 and its components are T i1i2
j
.
If we permute the order of the spaces in the tensor product from the conven-
tional “ﬁrst every V , then every V ∨,” then the indexing rule on tensors needs to be
adapted: V ⊗V ∨⊗V is not the same space as V ⊗V ⊗V ∨, so we shouldn’t write
its tensor components as T i1i2
j
. Write them as T i1 i2
j
, so that as we read indices
from left to right we see each index in the order its corresponding space appears in
V ⊗V ∨⊗V : upper indices for V and lower indices for V ∨.
Example 7.2. To compare transformation rules for rank 2 tensors in V ⊗2 (type (2,0)),
(V ∨)⊗2 (type (0,2)), and V ⊗V ∨(type (1,1)), let bases {e1, . . . , en} and {f1, . . . , fn} of V
be related by numbers aij as in (7.3) and (7.4): ej = P
i aijfi for all j.
Case 1: (2,0)-tensors. By (7.1), in V ⊗2 we have P
j1,j2 T j1j2ej1 ⊗ej2 = P
i1,i2 eT i1i2fi1 ⊗fi2
where
(7.9)
eT i1i2 =
X
j1,j2
T j1j2ai1j1ai2j2.
Case 2: (0,2)-tensors. In (V ∨)⊗2, P
j1,j2 Tj1j2ej1 ⊗ej2 = P
i1,i2 eTi1i2fi1 ⊗fi2 where
(7.10)
eTi1i2 =
X
j1,j2
Tj1j2aj1i1aj2i2,
with the matrix (aij) being the inverse of (aij), so ej = P
i ajifi for all j by (7.4).
Case 3: (1,1)-tensors. In V ⊗V ∨, P
j1,j2 T j1
j2 ej1 ⊗ej2 = P
i1,i2 eT i1
i2 fi1 ⊗fi2 where
(7.11)
eT i1
i2 =
X
j1,j2
T j1
j2 ai1j1aj2i2.
The n2 components of such tensors relative to the basis {e1, . . . , en} can be put into an
n × n matrix (T ij), (Tij), or (T i
j). We can rewrite (7.9), (7.10), and (7.11) so the sums on
the right look like formulas from multiplying 3 matrices:
eT i1i2 =
X
j1,j2
ai1j1T j1j2ai2j2,
eTi1i2 =
X
j1,j2
aj1i1Tj1j2aj2i2,
eT i1
i2 =
X
j1,j2
ai1j1T j1
j2 aj2i2.
The way indices in these sums repeat make the matrix of components of such a rank 2 tensor
transform as indicated in the table below (column 3).

<!-- page 55 -->
TENSOR PRODUCTS
55
Tensor space
Type
Transformation Rule
Meaning
V ⊗2
(2,0)
( eT ij) = (aij)(T ij)(aij)⊤
(V ∨)⊗2
(0,2)
( eTij) = (aij)⊤(Tij)(aij)
bilinear form on V
V ⊗V ∨
(1,1)
( eT i
j) = (aij)(T i
j)(aij)−1
linear map V →V
The (0,2)-tensors are bilinear forms on V (use (5.4) with M = N = V ∨and double
duality), such as an inner product or the Minkowski metric in special relativity. Column 3
in the (0,2) case is how a matrix representation of a bilinear form on V changes after a change
of basis. The (1,1)-tensors are linear maps V →V (by Example 5.11, V ⊗V ∨∼= Hom(V, V )).
Column 3 in the (1,1) case is how a matrix representation of a linear map V →V changes
after a change of basis. Warning: the “rank” of a linear map V →V in linear algebra (the
dimension of its image) has nothing to do with its “rank” in the above sense as a tensor in
V ⊗V ∨, which is always 2.
While V and V ∨are not literally equal, they are isomorphic. If we ﬁx an isomorphism
between them and use it to replace V ∨with V then the three diﬀerent spaces of rank 2
tensors can all be made to look like V ⊗2, a process called “raising indices” since it turns
Tij and T i
j into T ij. This is done often in geometry and physics since Rn is treated as
isomorphic to its dual space using the standard dot product to identify (Rn)∨with Rn.
Let’s compare how the mathematician and physicist think about a tensor:
• (Mathematician) Tensors belongs to a tensor space, which is a module – or in
geometry just a vector space – deﬁned by a multilinear universal mapping property.
• (Physicist) “Tensors are systems of components organized by one or more indices
that transform according to speciﬁc rules under a set of transformations.”30
In a tensor product of vector spaces, mathematicians and physicists can check two tensors
t and t′ are equal in the same way: check t and t′ have the same components in one
coordinate system. (Physicists don’t deal with modules that aren’t vector spaces, so they
always have bases available.) The reason mathematicians and physicists consider this to be
a suﬃcient test of equality is not the same. The mathematician thinks about the condition
t = t′ in a coordinate-free way and knows that to check t = t′ it suﬃces to check t and t′
have the same coordinates in one basis. The physicist considers the condition t = t′ to mean
(by deﬁnition!) that the components of t and t′ match in all coordinate systems, and the
multilinear transformation rule (7.7), or (7.8), on tensors implies that if the components of
t and t′ are equal in one coordinate system then they are equal in every coordinate system.
That’s why the physicist is content to look in just one coordinate system.
Consider Einstein’s description of tensors in a paper on general relativity [4, p. 157]:31
Let certain things (“tensors”) be deﬁned with respect to any system of co-
ordinates by a number of functions of the co-ordinates, called the “compo-
nents” of the tensor. There are then certain rules by which these components
can be calculated for a new system of co-ordinates, if they are known for the
original system of co-ordinates, and if the transformation connecting the two
systems is known. The things hereafter called tensors are further character-
ized by the fact that the equations of transformation for their components
are linear and homogeneous. Accordingly, all the components in the new
system vanish, if they all vanish in the original system.
30G. B. Arfken and H. J. Weber, Mathematical Methods for Physicists, 6th ed., p. 136.
31See https://einsteinpapers.press.princeton.edu/vol6-trans/169.

<!-- page 56 -->
56
KEITH CONRAD
Einstein’s “linear and homogeneous” transformation equations are what we call “multilin-
ear” equations.
An operation on tensors (like the ﬂip v ⊗w 7→w ⊗v on V ⊗2) is checked to be well-
deﬁned by the mathematician and physicist in diﬀerent ways. The mathematician checks
the operation respects the universal mapping property that deﬁnes tensor products, while
the physicist checks the explicit formula for the operation on elementary tensors changes
in diﬀerent coordinate systems by the tensor transformation rule (like (7.1)). The physicist
would say an operation on tensors makes sense because it transforms “tensorially” (like
a tensor), which in more expansive terms means that the formulas for the operation in
two diﬀerent coordinate systems are related by a multilinear change of variables. However,
textbooks on classical mechanics and quantum mechanics that treat tensors don’t seem
to use the word “multilinear,” even though that word describes exactly what is going on.
Instead, these textbooks nearly always say that a tensor’s components transform by a
“deﬁnite rule” or a “speciﬁc rule,” which doesn’t seem to have an actual meaning; isn’t
every computational rule a speciﬁc rule? Graduate textbooks on general relativity are an
exception to this habit: [3], [16], and [26] all deﬁne tensors in terms of multilinearity.32
Mathematicians and students in mathematics may be baﬄed about how physicists can
think about tensors just in terms of components. Conceptual deﬁnitions in math are very
nice, but the ugly component viewpoint of tensors is not only crucial to understanding how
tensors occur in physics, but they are also how tensors were used in mathematics in the ﬁrst
part of the 20th century33. Hassler Whitney, who we mentioned at the end of Section 3 as
the person who extended tensor products from vector spaces to abelian groups, expressed
his frustration like this [29, p. 114]: “I had to handle tensors; but how could I when I was
not permitted to see them, being only allowed to learn about their changing costumes under
changes of coordinates? I had somehow to grab the rascals, and look straight at them.”
The physical meaning of a vector is not just displacement, but linear displacement. For
instance, forces at a point combine in the same way that vectors add (this is an experi-
mental observation), so force is treated as a vector. The physical meaning of a tensor is
multilinear displacement.34. That means a quantity (mathematical or physical) whose de-
scription transforms under a change of coordinates in the same way as the components of
a tensor can be mathematically described as that type of tensor. Some examples of this in
physics, including the physical reasoning behind the eﬀect of a change of coordinates, are
in [6, Chap. 31].
Example 7.3. The most basic example of a rank-2 tensor in mechanics is the stress tensor.
When a force is applied to a body the stress it imparts at a point may not be in the
direction of the force but in some other direction (compressing a piece of clay, say, can push
it out orthogonally to the direction of the force), and this eﬀect is linear in the input, so
stress at a point is described by a linear transformation, and thus is a rank-2 tensor since
End(V ) ∼= V ∨⊗V (Example 5.11). Since stress from an applied force can act in diﬀerent
directions at diﬀerent points, the stress tensor is not really a single tensor but rather is a
varying family of tensors at diﬀerent points: stress is a tensor ﬁeld, which is a generalization
of a vector ﬁeld. A tensor ﬁeld on a manifold M (not a module!) can be deﬁned locally or
globally:
32I thank Don Marolf for bringing this point to my attention.
33The earliest reference I know that describes tensors using multilinearity instead of components with a
transformation rule is [21, pp. 179], from 1923, which confuses V with its dual space.
34Tensors are “multilinear functions of several directions” in [24, p. 9].

<!-- page 57 -->
TENSOR PRODUCTS
57
• (Locally) A (k, ℓ)-tensor ﬁeld on a manifold M is a choice of element in each tensor
product Tp(M)⊗k ⊗R Tp(M)∨⊗ℓof tangent and cotangent spaces at the points p on
M, varying smoothly with p,
• (Globally) A (k, ℓ)-tensor ﬁeld on a manifold M is an element of X(M)⊗k ⊗C∞(M)
X(M)∨⊗ℓwhere X(M) is the set of all vector ﬁelds on M viewed as a module over
the ring C∞(M) of smooth functions on M [14, Sect. 7.2, 7.3].
Tensors in many parts of physics (classical mechanics, electromagnetism, and relativity)
are always part of a tensor ﬁeld, so in physics the word “tensor” usually means “tensor
ﬁeld”. A change of variables between local coordinate systems x = {xi} and y = {yi} in
a region U of Rn involves partial derivatives ∂yi
∂xj or (in the reverse direction) ∂xi
∂yj : by the
chain rule,
∂
∂xj = P
i
∂yi
∂xj
∂
∂yi and
∂
∂yj = P
i
∂xi
∂yj
∂
∂xi . When working with tensor ﬁelds on U,
tensor transformation rules occur with ∂yi
∂xj and ∂xi
∂yj , which vary from point to point, in the
role of aij and aij. For example, a (2,0)-tensor ﬁeld (rank 2 tensor ﬁeld with upper indices)
on U is a doubly-indexed quantity T ij(x) in each coordinate system x at a point in U such
that in a second coordinate system y at the same point its components are
(7.12)
eT ij(y) =
n
X
k,ℓ=1
T kℓ(x) ∂yi
∂xk (x) ∂yj
∂xℓ(x),
which should be compared to (7.9).
Not every indexed quantity is a tensor: to be a tensor it must satisfy a multilinear
transformation law under every change of coordinates. An example of an indexed quantity
in diﬀerential geometry that is not a tensor is the Christoﬀel symbols Γk
ij (components
of a Levi-Civita connection). Under a change in coordinates they do not transform by a
multilinear change of variables, so they have 3 indices but they are not a rank 3 tensor.
To see a physicist introduce tensors (really, tensor ﬁelds) as indexed quantities, watch
Leonard Susskind’s lectures on general relativity on YouTube from 2009, particularly lecture
3 (tensors ﬁrst appear 42 minutes in, although some notation is introduced earlier) and
lecture 4. In lecture 5 tensor calculus (covariant diﬀerentiation of tensor ﬁelds) is introduced.
Physicists and engineers who think of tensors in terms of their components will say that
a physical law described with tensors is independent of coordinates because such a law in
one coordinate system has a similar description in any other coordinate system.
What
often goes unmentioned is that these physical laws are multilinear relations among tensor
components, which is the reason for independence of coordinates since the components of
a tensor transform multilinearly when coordinates change. I have seen some references for
physicists or engineers go as far as to assert the converse: a physical law that is independent
of coordinates must be expressible in terms of tensors, but that’s wrong: tensor ﬁelds are not
the only concept in geometry that is independent of coordinates. For example, connections
and spinor ﬁelds are geometric structures on (Riemannian) manifolds that are not tensors.
Tensors play an essential role in quantum mechanics, but for rather diﬀerent reasons
than we’ve already mentioned in physics. In classical mechanics, the states of a system
are modeled by the points on a ﬁnite-dimensional manifold, and when we combine two
systems the corresponding manifold is the direct product of the manifolds for the original
two systems.
The states of a quantum system, on the other hand, are represented by
the nonzero vectors (really, the 1-dimensional subspaces) in a complex Hilbert space, such
as L2(R6). (A point in R6 has three position and three momentum coordinates, which

<!-- page 58 -->
58
KEITH CONRAD
is the classical description of a particle.)
When we combine two quantum systems, its
corresponding Hilbert space is the tensor product of the original Hilbert spaces, essentially
because L2(R6 × R6) = L2(R6) ⊗C L2(R6), which is the analytic35 analogue of R[X, Y ] ∼=
R[X] ⊗R R[Y ]. Thus quantum states are related to tensors in a single tensor product of
Hilbert spaces, not to tensor ﬁelds. A video of a physicist introducing tensor products of
Hilbert spaces on YouTube is Frederic Schuller’s lecture 14 on quantum mechanics, where
he writes an elementary tensor as v ⊠w rather than v ⊗w to avoid confusion with the use
of ⊗in the notation of the vector space H1 ⊗C H2.
The diﬀerence between a direct product of manifolds M×N and a tensor product of vector
spaces H1 ⊗C H2 reﬂects mathematically some of the non-intuitive features of quantum
mechanics. Every point in M × N is a pair (x, y) where x ∈M and y ∈N, so we get
a direct link from a point in M × N to something in M and something in N. On the
other hand, most tensors in H1 ⊗C H2 are not elementary, and a non-elementary tensor
in H1 ⊗C H2 has no simple-minded description in terms of a pair of elements of H1 and
H2. Quantum states in H1 ⊗C H2 that correspond to non-elementary tensors are called
entangled states, and they reﬂect the diﬃculty of trying to describe quantum phenomena
for a combined system (e.g., the two-slit experiment) in terms of quantum states of the
two original systems individually. I’ve been told that physics students who get used to
computing with tensors in relativity by learning to work with the “transform by a deﬁnite
rule” description of tensors ﬁnd the role of tensors in quantum mechanics to be diﬃcult to
learn, because the conceptual role of tensors there is so diﬀerent. And probably it doesn’t
help students that physicists use “tensor” to mean both tensor ﬁelds and tensors.
Whether you want to think of tensors as objects in a space having a universal mapping
property, indexed quantities that satisfy a transformation rule, or a physical interpretation,
the advice of user mathwonk on the website PhysicsForums36 is worth remembering: It does
not matter what a “tensor” is, what matters is knowing what you are doing.
We’ll end this discussion of tensors in physics with a story. I was the math consultant
for the 4th edition of the American Heritage Dictionary of the English Language (2000).
The editors sent me all the words in the 3rd edition with mathematical deﬁnitions, and I
had to ﬁnd and correct the errors. Early on I came across a word I had never heard of
before: dyad. It was deﬁned in the 3rd edition as “an operator represented as a pair of
vectors juxtaposed without multiplication.” That’s a ridiculous deﬁnition, as it conveys no
meaning at all. I obviously had to ﬁx this deﬁnition, but ﬁrst I had to know what the word
meant! In a physics book37 a dyad is deﬁned as “a pair of vectors, written in a deﬁnite
order ab.” This is just as useless, but the physics book also does something with dyads,
which gives a clue about what they really are. The product of a dyad ab with a vector c is
a(b·c), where b·c is the usual dot product (a, b, and c are all vectors in Rn). This reveals
what a dyad is. Do you see it? Dotting with b is an element of the dual space (Rn)∨, so
the eﬀect of ab on c is reminiscient of the way V ⊗V ∨acts on V by (v ⊗ϕ)(w) = ϕ(w)v.
A dyad is the same thing as an elementary tensor v ⊗ϕ in Rn ⊗(Rn)∨. In the 4th edition
of the dictionary, I included two deﬁnitions for a dyad. For the general reader, a dyad is
35This tensor product should be completed, having inﬁnite sums of products f(x)g(y).
There are
more subtleties.
See http://www-users.math.umn.edu/∼garrett/m/v/nonexistence tensors.pdf and
https:// math.stackexchange.com/questions/2951879.
36See https://www.physicsforums.com/threads/christoffel-symbol-as-tensor.40177/.
37H. Goldstein, Classical Mechanics, 2nd ed., p. 194

<!-- page 59 -->
TENSOR PRODUCTS
59
“a function that draws a correspondence38 from any vector u to the vector (v · u)w and
is denoted vw, where v and w are a ﬁxed pair of vectors and v · u is the scalar product
of v and u. For example, if v = (2, 3, 1), w = (0, −1, 4), and u = (a, b, c), then the dyad
vw draws a correspondence from u to (2a + 3b + c)w.” The more concise second deﬁnition
was: a dyad is “a tensor formed from a vector in a vector space and a linear functional
on that vector space.” Unfortunately, the deﬁnition of “tensor” in the dictionary is “A set
of quantities that obey certain transformation laws relating the bases in one generalized
coordinate system to those of another and involving partial derivative sums. Vectors are
simple tensors.” That is really the deﬁnition of a tensor ﬁeld, and that sense of the word
tensor is incompatible with my concise deﬁnition of a dyad in terms of tensors.
More general than a dyad is a dyadic, which is a sum of dyads: ab+cd+. . . . So a dyadic
is a general tensor in Rn ⊗R (Rn)∨∼= HomR(Rn, Rn). In other words, a dyadic is an n × n
real matrix. The terminology of dyads and dyadics goes back to Gibbs [7, Chap. 3], who
championed the development of linear and multilinear algebra, including his indeterminate
product (that is, the tensor product), under the name “multiple algebra.”
References
[1] D. V. Alekseevskij, V. V. Lychagin, A. M. Vinogradov, “Geometry I,” Springer-Verlag, Berlin, 1991.
[2] N. Bourbaki, Livre II Alg`ebre Chapitre III (´etat 4) Alg`ebre Multilin´eaire, http://archives-bourbaki.
ahp-numerique.fr/files/original/97a9fed708bdde4dc55547ab5a8ff943.pdf.
[3] S. Carroll, “Spacetime and Geometry: An Introduction to General Relativity,” Benjamin Cummings,
2003.
[4] A. Einstein, The Foundation of the General Theory of Relativity (English translation), pp. 146–199 in
“The Collected Papers of Albert Einstein, Vol. 6: The Berlin Years: Writings, 1914-1917,” Princeton
Univ. Press, Princeton, 1997. URL https://einsteinpapers.press.princeton.edu/vol6-trans/158.
[5] D. Eisenbud and J. Harris, “The Geometry of Schemes”, Springer-Verlag, New York, 2000.
[6] R. P. Feynman, Chap. 31 of “The Feynman Letures on Physics, Vol. II,” Millennium edition, http://www.
feynmanlectures.caltech.edu/II 31.html.
[7] J. W. Gibbs, “Elements of Vector Analysis Arranged for the Use of Students in Physics,” Tuttle, More-
house & Taylor, New Haven, 1884. URL https://archive.org/details/elementsvectora00gibb.
[8] J. W. Gibbs, On Multiple Algebra, Proceedings of the American Association for the Advancement of
Science, 35 (1886). URL http://archive.org/details/onmultiplealgeb00gibbgoog.
[9] R. Grone, Decomposable Tensors as a Quadratic Variety, Proc. Amer. Math. Soc. 64 (1977), 227–230.
[10] P. Halmos, “Finite-Dimensional Vector Spaces,” Springer-Verlag, New York, 1974.
[11] J. H˚astad, Tensor rank is NP-complete, J. Algorithms 11 (1990), 644–654.
[12] C. J. Hillar and L-K. Lim, Most tensor problems are NP-hard, J. ACM 60 (2013), Art. 45, 39 pp.
[13] J. Kun, How to Conquer Tensorphobia, https://jeremykun.com/2014/01/17/how-to-conquer-tensor
phobia/.
[14] J. M. Lee, “Manifolds and Diﬀerential Geometry,” Amer. Math. Soc., Providence, 2009.
[15] R. Hermann, “Ricci and Levi-Civita’s Tensor Analysis Paper” Math Sci Press, Brookline, 1975.
[16] C. W. Misner, K. S. Thorne, and J. A. Wheeler, “Gravitation,” W. H. Freeman and Co., San Francisco,
1973.
[17] F. J. Murray and J. von Neumann, On Rings of Operators, Annals Math. 37 (1936), 116–229.
[18] B. O’Neill, “Semi-Riemannian Geometry,” Academic Press, New York, 1983.
[19] B. Osgood, Chapter 8 of The Fourier Transform and its Applications, http://see.stanford.edu/
materials/lsoftaee261/chap8.pdf.
[20] H-J Petsche, “Hermann Grassmann – Biography,” Birkh¨auser, Basel, 2009.
[21] G. Y. Rainich, Tensor analysis without coordinates, Proc. Natl. Acad. Sci. USA 9 (1923), 179-183.
[22] G. Ricci, T. Levi-Civita, M´ethodes de Calcul Diﬀ´erentiel Absolu et Leurs Applications, Math. Annalen
54 (1901), 125–201.
[23] Y. Shitov, How hard is the tensor rank?, https://arxiv.org/pdf/1611.01559.pdf.
38Yes, this terminology sucks. Blame the unknown editor at the dictionary for that one.

<!-- page 60 -->
60
KEITH CONRAD
[24] F. J. Temple, “Cartesian Tensors,” Wiley, New York, 1960.
[25] W. Voigt, Die fundamentalen physikalischen Eigenschaften der Krystalle in elementarer Darstellung,
Verlag von Veit & Comp., Leipzig, 1898.
[26] R. Wald, “General Relativity,” Univ. Chicago Press, Chicago, 1984.
[27] H. Weyl, “The Theory of Groups and Quantum Mechanics,” E. P. Dutton, New York, 1932.
[28] H. Whitney, Tensor Products of Abelian Groups, Duke Math. Journal 4 (1938), 495–528.
[29] H. Whitney, Moscow 1935: topology moving toward America, pp. 97–117 in “A Century of Mathematics
in America, Part I,” Amer. Math. Soc., Providence, 1988.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*