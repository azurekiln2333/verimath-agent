# Algebras

> **Source**: https://kconrad.math.uconn.edu/blurbs/algebras.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
ALGEBRAS
KEITH CONRAD
1. Definitions and Examples
Let k be a ﬁeld. Both ﬁeld extensions K/k and matrix rings Md(k) are examples of rings
that are properly understood by taking into account the extra structure of a k-vector space.
We want to discuss, in general, vector spaces over k that have a ring structure compatible
with the scalar multiplication by elements of k.
Deﬁnition 1.1. A k-algebra A is a (possibly noncommutative) ring with identity that is
also a k-vector space, such that for α ∈k and a, b ∈A,
(1.1)
α(ab) = (αa)b = a(αb).
Example 1.2. A commutative ring containing k, such as a ﬁeld extension, the polynomial
ring k[X, Y ], or the formal power series ring k[[X]] is a k-algebra.
Example 1.3. The ring Md(k) under matrix addition and multiplication is a k-algebra.
This is called a matrix algebra over k.
Example 1.4. The group ring k[G] for a ﬁnite group G.
Example 1.5. The set Homk(V, V ) of k-linear maps of a k-vector space V to itself is a
k-algebra under addition and composition of linear maps.
Example 1.6. The set C([0, 1], R) of continuous functions [0, 1] →R is an R-algebra under
the usual pointwise addition and multiplication of functions.
While a k-algebra may be noncommutative, (1.1) tells us that elements of k are sup-
posed to commute multiplicatively with all the elements of a k-algebra. The next example
illustrates this point well.
Example 1.7. Since the center of the quaternions H is the real numbers, H is an R-algebra.
But H is not a C-algebra using usual quaternionic multiplication with complex numbers
since the only quaternions that commute with all quaternions are real numbers. Certainly
H can be given the structure of a complex vector space, by letting scalar multiplication be
left multiplication by the complex numbers. This is not the only type of complex vector
space structure one can give to H. Another one would be z ·q def
= qz, where q is a quaternion
and z is a complex number. But H is not a C-algebra by either of these C-vector space
structures.
Understand this example to keep clearly in mind the distinction between a
k-vector space and a k-algebra.
You may have seen these examples before, treated just as rings. The existence of the
ﬁeld k provides an extra basic structure, which is the main reason for isolating the concept
of a k-algebra.
Our deﬁnition of a k-algebra easily extends to the notion of an R-algebra for a commu-
tative ring R. That would be a ring A with identity that is also an R-module such that
1

<!-- page 2 -->
2
KEITH CONRAD
(1.1) is true for α ∈R and a and b in A. For example, Md(R) is an R-algebra and every
ring is a Z-algebra. We focus here on algebras over a ﬁeld for simplicity (e.g., bases are
automatically available).
For a k-algebra A, α 7→α · 1A for α ∈k is a ring homomorphism of k to the center of
A, and it must be injective if A ̸= 0 since ring homomorphisms from a ﬁeld to a nonzero
ring must be injective. Thus a more concrete way to think about a k-algebra is that it is a
ring containing k in the center. If we did not require our algebras to have a multiplicative
identity then we could not make this concrete observation, but all algebras of interest to us
will have an identity so we build that property into the deﬁnition. When deﬁning things
like k-algebra homomorphims, subalgebras, quotient algebras, and so forth, it is appropriate
not to identify the scalar ﬁeld k with its image in a particular k-algebra.1
Remark 1.8. We included a multiplicative identity in our deﬁnition of a k-algebra, and
that ﬁts the needs of algebraists quite well.
However, in analysis there are important
examples of algebras “without identity,” such as the real-valued continuous functions on R
with compact support. If there could be a multiplicative identity, it should be the constant
function 1, but that doesn’t have compact support.
We say a k-algebra A is ﬁnite-dimensional when it is ﬁnite-dimensional as a vector space
over k, and we write [A : k] = dimk(A). For example, C is a two-dimensional R-algebra
and an inﬁnite-dimensional Q-algebra, while Md(k) is a d2-dimensional k-algebra. The R-
algebra C([0, 1], R) is inﬁnite-dimensional. We will often use the term “ﬁnite k-algebra” to
mean “ﬁnite-dimensional k-algebra.”
An algebra is called commutative when multiplication in the algebra is commutative.
A subalgebra of a k-algebra A is a subset that is both a subring and a k-linear subspace,
hence a k-algebra in its own right. For example, the R-algebra H contains C as an R-
subalgebra. A k-algebra homomorphism f : A →B is a map between k-algebras that is
both k-linear and a ring homomorphism. Unlike the k-linear maps from A to itself, the
subset of k-algebra homomorphisms of A to itself is usually not even a vector space since
the sum of two k-algebra homomorphisms need not be a k-algbera homomorphism (it need
not be multiplicative). There is a natural notion of a k-algebra isomorphism. For example,
if V is a d-dimensional vector space over k, then choosing a k-basis of V yields a k-algebra
isomorphism
Homk(V, V ) ∼= Md(k).
The point is that this is not just an isomorphism of rings; it’s k-linear as well and we should
pay attention to this extra structure in the isomorphism.
Example 1.9. The bilinear map V ×V ∨→Homk(V, V ), which sends (v, ϕ) to the function
w 7→ϕ(w)v induces a k-linear map V ⊗k V ∨→Homk(V, V ). Given a basis e1, . . . , ed of
V , the simple tensors ei ⊗e∨
j correspond to the matrices with a 1 in the (i, j) position
and 0 elsewhere, so this k-linear map sends a basis to a basis and thus is a vector space
isomorphism. Since Homk(V, V ) is a k-algebra, we can transport the multiplication on it
back to V ⊗k V ∨. Can you describe this ring structure on V ⊗k V ∨directly?
Since multiplication by k commutes with every element of A, for each a ∈A there is a
k-algebra homomorphism
eva : k[X] →A
1If we replace the ﬁeld k with a commutative ring R then the mapping α 7→α·1A from R to an R-algebra
with identity might not be injective. An example is thinking of Z/10Z as a Z-algebra.

<!-- page 3 -->
ALGEBRAS
3
given by cnXn + · · · + c0 7→cnan + · · · + c0 · 1A, called evaluation at
a. Of course, for
f(X) ∈k[X], we often write f(a) for eva(f). If k were not in the center of A, then eva
need not be a homomorphism! For example, take A = H and k = C, which is an R-
subalgebra of H but is not in the center of H. Note that evj(X2 + 1) = j2 + 1 = 0 and
evj(X + i) evj(X −i) = (j + i)(j −i) = 2ij ̸= 0.
Imitating the notion of algebraic ﬁeld extensions, we say a ∈A is algebraic (over k) if
f(a) = 0 for some nonzero f ∈k[X]. We say A is an algebraic k-algebra if every element of
A is algebraic over k. For example, a ﬁnite ﬁeld extension K/k is an algebraic k-algebra.
More generally, a ﬁnite-dimensional k-algebra A is algebraic, by the same proof as for ﬁnite
ﬁeld extensions: for a ∈A and n = [A : k], the n+1 elements 1, a, . . . , an satisfy a nontrivial
k-linear relation, so a is algebraic over k.
A k-division algebra is a division ring that is also a k-algebra. For example, H is an
R-division algebra, and a Q-division algebra, although one usually views it only as an R-
division algebra. Our primary interest is in k-division algebras, such as ﬁelds containing k,
so on some occasions we will prove results only for the case of division algebras when the
proof for more general algebras is longer.
If K/k is a ﬁeld extension and A is a K-algebra, then A is also a k-algebra in the obvious
way. The proof of the transitivity formula for dimensions of ﬁnite extensions of ﬁelds carries
over to show that
[A : k] < ∞⇐⇒[A : k], [K : k] < ∞,
in which case [A : k] = [A : K][K : k]. For example, M3(C) is a 9-dimensional C-algebra,
an 18-dimensional R-algebra, and as a Q-algebra it is inﬁnite-dimensional.
We now introduce arguably the most important idea in this handout. Let A be a k-
algebra. To each a ∈A we associate the k-linear map ma : A →A given by left multiplica-
tion by a:
x 7→ax.
The map A →Homk(A, A) given by a 7→ma is a k-algebra homomorphism:
ma+b(x) = (a + b)(x) = ax + bx = ma(x) + mb(x) = (ma + mb)(x),
(ma ◦mb)(x) = ma(bx) = a(bx) = (ab)x = mab(x),
and
mαa(x) = (αa)x = α(ax) = α(ma(x)) = (αma)(x),
so ma is additive in a, multiplicative in a (note m1 is the identity map on A), and mαa =
αma. Since A has a multiplicative identity, we can recover a from ma by evaluating at 1:
ma(1) = a · 1 = a. Thus turning elements of A into left multiplication maps on A embeds
A in Homk(A, A) as a k-subalgebra.
Assume from now on that n = [A : k] < ∞. Choosing a k-basis of A lets us express
each ma as an n by n matrix [ma] acting on the left on column vectors of kn ∼= A (as
k-vector spaces). Thus A acting on itself by left multiplication lets us view A as matrices
over k. (analogy: every ﬁnite group lives in some symmetric group by having the group
act on itself by left multiplications).
For f(X) = P
i ciXi in k[X] and a and x in A,
mf(a)(x) = f(a)x = P
i ci(aix) = P
i ci(ma)i(x) = f(ma)(x), so mf(a) = f(ma) for all
a ∈A: a polynomial function of ma over k is left multiplication on A by that polynomial’s
value at a.
Example 1.10. If α ∈k, then with respect to any k-basis of A, [mα] is the scalar diagonal
matrix α · In, where n = [A : k].

<!-- page 4 -->
4
KEITH CONRAD
Example 1.11. A = C, k = R, basis = {1,i}. For a = a1 + a2i, [ma] equals

a1
−a2
a2
a1

.
Example 1.12. A = Q(√r) for r a nonsquare rational, k = Q, basis = {1,√r}.
For
a = a1 + a2
√r, [ma] equals

a1
a2r
a2
a1

.
Example 1.13. A = Q(θ) for θ a root of X3 −X −1, k = Q, basis = {1, θ, θ2}. For
a = a1 + a2θ + a3θ2, [ma] equals


a1
a3
a2
a2
a1 + a3
a2 + a3
a3
a2
a1 + a3

.
Example 1.14. A = H, k = R, basis = {1,i,j,k} (of course, the basis element k is not to
be confused with our generic label for a ﬁeld). For a = a1 + a2i + a3j + a4k, [ma] equals




a1
−a2
−a3
−a4
a2
a1
−a4
a3
a3
a4
a1
−a2
a4
−a3
a2
a1



.
Example 1.15. Let A = Md(k). Using the standard basis Eij ordered lexicographically, if
a = (aij) then [ma] equals
(aij) ⊗Id
in Md2(k) = Md(k) ⊗k Md(k).
Deﬁnition. Let A be an n-dimensional k-algebra, a ∈A. The characteristic polynomial
χa(X) of a is the usual characteristic polynomial of the linear map ma, namely
χa(X) = det(X · In −ma),
a monic polynomial in k[X] of degree n = [A : k].
By the Cayley-Hamilton theorem, χa(ma) = 0, so mχa(a) = χa(ma) = 0 = m0. Since
mχa(a) = m0, we have proven the following theorem.
Theorem 1.16. For a ﬁnite-dimensional k-algebra A, each a in A is a root of its charac-
teristic polynomial χa(X) ∈k[X].
Deﬁnition 1.17. For a ﬁnite-dimensional k-algebra A, the trace of a ∈A is the trace of
ma. The norm of a is the determinant of ma.
That is, the trace of a is TrA/k(ma) ∈k, usually written as TrA/k(a), so TrA/k : A →k.
(Sometimes you might see S or Sp used for trace since Spur is the German word for trace.)
The norm of a is det(ma) ∈k, usually written as NA/k(a), so NA/k : A →k. Note that the
constant term of χa(X) is χa(0) = (−1)nNA/k(a) and the coeﬃcient of Xn−1 is −TrA/k(a).
So up to sign, the trace and norm of a can be read from the characteristic polynomial, and
in a ﬁeld containing k in which χa splits, the roots of χa have sum equal to TrA/k(a) and

<!-- page 5 -->
ALGEBRAS
5
product equal to NA/k(a). In practice, there are more eﬃcient ways of computing traces
and norms. See Theorem 2.2 below.
Let’s look at some examples.
By Example 1.10, TrA/k(α) = nα and NA/k(α) = αn for all α ∈k.
In particular,
TrA/k(1) = n = [A : k].
By Example 1.11, χa1+a2i(X) = X2 −2a1X + a2
1 + a2
2. Thus
TrC/R(a1 + a2i) = 2a1,
NC/R(a1 + a2i) = a2
1 + a2
2.
By Example 1.12, χa1+a2
√r(X) = X2 −2a1X + a2
1 −ra2
2. Thus
TrQ(√r)/Q(a1 + a2
√r) = 2a1,
NQ(√r)/Q(a1 + a2
√r) = a2
1 −ra2
2.
By Example 1.13, TrQ(θ)/Q(a1 + a2θ + a3θ2) = 3a1 + 2a3 and
NQ(θ)/Q(a1 + a2θ + a3θ2) = a3
1 + a3
2 −a3
3 −a1a2
2 + a1a2
3 −a2a2
3 + 2a2
1a3 −3a1a2a3.
By Example 1.14, TrH/R(a1 + a2i + a3j + a4k) = 4a1 and
NH/R(a1 + a2i + a3j + a4k) = (a2
1 + a2
2 + a2
3 + a2
4)2.
By Example 1.15, χ(aij)(X) = det(X · Id2 −(aij) ⊗Id) = det((X · Id −(aij)) ⊗Id) =
det(X · Id −(aij))d, so TrMd(k)/k(aij) = d P aii = d · tr(aij) and NMd(k)/k(aij) = det(aij)d.
This gives the relation between the characteristic polynomial of a matrix in Md(k) as usually
deﬁned in linear algebra and as deﬁned when viewing Md(k) as a k-algebra: one is the d-th
power of the other.
For a, b ∈A and α ∈k, recall we saw that ma+b = ma + mb, mab = mamb, and mαa =
αma. Thus, taking traces and determinants on these equations, we ﬁnd that TrA/k : A →k
is k-linear (hence identically zero or surjective, since k is a one-dimensional k-vector space)
and NA/k : A →k is multiplicative. Obviously, NA/k : A× →k×. More generally, we have
Theorem 1.18. a ∈A× if and only if NA/k(a) ̸= 0.
Proof. Let χa(X) = Xn + cn−1Xn−1 + · · · + c0, where c0 = ±NA/k(a) ∈k. Since χa(a) = 0,
we have
(an−1 + cn−1an−2 + · · · + c1)a = −c0,
so if c0 ̸= 0 then we can divide by it and show a is invertible.
□
For a ∈A, k[a] is a commutative k-subalgebra of A. If a ∈A×, then k[a] is not neccesarily
a ﬁeld. For example, consider A = k[Y ]/(Y 2−1) with a being the class of Y . Then k[a] = A
is not a ﬁeld, but a2 = 1 so a is a unit in A. When A is a division ring, we’ll see below that
k[a] is a ﬁeld.
Let Ma = Ma(X) be the nonzero monic polynomial of least degree in k[X] with a as a
root. (Don’t confuse this with the notation Md(k) for a matrix algebra over k.) Recall our
standing assumption that [A : k] is ﬁnite, so Ma does exist since A/k is algebraic. We call
Ma the minimal polynomial of a. As usual, if f ∈k[X] then f(a) = 0 if and only if Ma | f
in k[X]. In particular, Ma | χa. However, the usual proof that minimal polynomials are
irreducible if the k-algebra is a ﬁeld does not work in general, since typically in A one has
xy = 0 without x or y equaling 0. If A is a division ring then the proof for ﬁelds does work,
so Ma is always irreducible when A is a division ring (left as exercise for the reader). As a
consequence, let’s show that if A is a division ring, then k[a] is a ﬁeld for each a ∈A. It is
certainly a commutative ring, so we only have to show that every nonzero element of k[a]

<!-- page 6 -->
6
KEITH CONRAD
has a multiplicative inverse. A typical element has the form f(a) for f ∈k[X]. If it is not
zero, then f(X) is not divisible by Ma(X) in k[X]. Since A is a division ring, Ma(X) is
irreducible in k[X], so there are g1, g2 ∈k[X] such that fg1 + Mag2 = 1 in k[X]. Taking
X = a we ﬁnd that f(a)g1(a) = 1 in k[a]. Thus, we may write k(a) for k[a] if A is a division
ring.
Since you are already familiar with the minimal polynomial for elements in a ﬁeld exten-
sion but perhaps not as familiar with the characteristic polynomial for such elements, there
may be some confusion between them. One way to understand the diﬀerence is by looking
at the degree. The characteristic polynomial of each element a ∈A has the same degree,
[A : k], while the minimal polynomial has varying degree, equal to [k[a] : k]. If A = k[a],
then deg(Ma) = [A : k] = deg(χa) and both Ma and χa are monic with Ma | χa, so
Ma = χa. In general, as we will see in the next section, for division algebras (in particular,
for ﬁeld extensions) the degree is essentially the only diﬀerence between the minimal and
characteristic polynomials, since one is a power of the other. The fact that characteristic
polynomials have a uniform degree for all elements accounts in part for why we will use
them sometimes instead of minimal polynomials when associating an element of an algebra
with a polynomial having that element as a root.
2. Basic Results
First we say something about division algebras over algebraically closed ﬁelds and over
ﬁnite ﬁelds. What are the ﬁnite division algebras over C? If D is a ﬁnite division algebra over
C, choose x ∈D. Since x is algebraic over C, it is a root of some polynomial f(X) ∈C[X].
Let f(X) = (X −z1) · · · · · (X −zn), so (since C is in the center of D) we have 0 = f(x) =
(x−z1)·· · ··(x−zn). Since D is a division ring, one of the factors x−zi is zero, so x = zi ∈C.
Thus, the only ﬁnite division algebra over C is C. (Why can’t we take D = H? It contains
C, of course, but it is not a C-algebra, since C is not in the center, which was the crucial
property one needs in order to conclude that f(x) = Q
i(x −zi).) In fact, we’ve actually
proven that the only algebraic C-division algebra (possibly inﬁnite-dimensional over C, a
priori!) is C. The exact same argument shows that the only algebraic division algebra over
an algebraically closed ﬁeld is the ﬁeld itself. Since the ﬁnite-dimensional division algebras
over a ﬁnite ﬁeld are precisely the ﬁnite division rings, we mention a famous theorem due
to Wedderburn: every ﬁnite division ring is commutative (see [2, §7.2] for a proof). Thus,
there are no noncommutative ﬁnite-dimensional division algebras over a ﬁnite ﬁeld.
Now we prove some theorems. Let’s show that in a k-division algebra, the characteristic
polynomial is a power of the minimal polynomial. In particular, the next result applies to
ﬁnite ﬁeld extensions of k.
Theorem 2.1. If D is a ﬁnite-dimensional k-division algebra, then for all a ∈D,
χa = Mdeg(χa)/deg(Ma)
a
= M[D:k]/[k[a]:k]
a
.
Thus, ND/k(a) = (−1)[D:k]Ma(0)[D:k]/[k[a]:k].
Proof. If a ∈k, then χa(X) = (X −a)n and Ma(X) = X −a, so the result is clear. Thus
assume a ̸∈k, so
Ma(X) = Xm + cm−1Xm−1 + · · · + c0,
with m > 1. By the deﬁnition of Ma, {1, a, . . . , am−1} is a k-basis of k[a]. Since k lies in
the center of D and D is a division ring and algebraic over k, k[a] is a ﬁeld, so D can be

<!-- page 7 -->
ALGEBRAS
7
viewed as a, say, left vector space over k[a]. Since k ⊂k[a] ⊂D, s = dimk[a](D) < ∞. Let
v1, . . . , vs be a k[a]-basis of D. Then
D =
s
M
j=1
k[a]vj =
s
M
j=1
m−1
M
i=0
kaivj,
so to compute χa(X) we use as an ordered k-basis of D the set
{v1, av1, . . . , am−1v1; . . . ; vs, avs, . . . , am−1vs}.
Note [D : k] = s[k[a] : k]. Since
a · am−1vj = −c0vj −c1avj −· · · −cm−1am−1vj,
we see that with respect to the above basis, [ma] is a block diagonal matrix with s m by m
diagonal blocks B equal to







0
0
0
−c0
1
0
0
. . .
−c1
0
1
0
−c2
...
...
...
0
0
0
. . .
−cm−1







.
Thus
χa(X)
=
det(X · Im −B)s
=
(Xm + cm−1Xm−1 + · · · + c0)s by induction on m
=
Ma(X)s.
Now set X = 0 and use the equation ND/k(a) = (−1)[D:k]χa(0) to get the formula for
ND/k(a).
□
All our concepts apply to a ﬁnite extension of ﬁelds. We now recover a more concrete
deﬁnition of trace and norm when A is a ﬁeld extension of k generated by one element. In
particular, the next result applies whenever k has characteristic 0 or is a ﬁnite ﬁeld or is
algebraically closed.
Theorem 2.2. Let k be a ﬁeld and K = k(θ) a ﬁnite separable extension of degree n, so
there are n distinct embeddings σ1, . . . , σn of K into an algebraic closure k of k. For each
a ∈K,
χa(X) =
Y
i
(X −σi(a)),
so TrK/k(a) = P
i σi(a) and NK/k(a) = Q
i σi(a).
Proof. Let
f(X) = (X −σ1(a)) · · · · · (X −σn(a)).
When K = k(a), the result is clear since χa = Ma. In general, χa = M[K:k(a)]
a
and every
embedding k(a) →k has [K : k(a)] distinct extensions to K →k. Thus, letting τ run over

<!-- page 8 -->
8
KEITH CONRAD
the distinct embeddings k(a) →k,
f(X)
=
(
Y
τ
X −τ(a))[K:k(a)]
=
M[K:k(a)]
a
=
χa(X).
□
For example, if k = Q and K = Q(√r) for r a nonsquare rational, then we can let
σ1(√r) = √r and σ2(√r) = −√r, so by the theorem,
χa1+a2
√r(X) = (X −(a1 + a2
√r))(X −(a1 −a2
√r)) = X2 −2a1X −(a2
1 −ra2
2),
which coincides with what we found before by doing a matrix calculation.
Corollary 2.3. For a ∈Fqn,
TrFqn/Fq(a) = a + aq + · · · + aqn−1 and NFqn/Fq(a) = a · aq · · · · · aqn−1.
Since the trace map from Fqn to Fq is a polynomial function of degree qn−1 and Fqn has
size qn, the trace map is not identically zero, so it is onto since it is Fq-linear. Letting γ be
a generator of F×
qn, we see NFqn/Fq(γ) = γ(qn−1)/(q−1) has (multiplicative) order q −1, so
the norm map from F×
qn to F×
q is onto.
We now consider a ﬁnite-dimensional L-algebra A with K a subﬁeld of L such that
[L : K] < ∞. We have ﬁnite-dimensional algebras A/L, A/K, and L/K. The next theorem
is called the transitivity of the trace.
Theorem 2.4. TrA/K = TrL/K◦TrA/L. In particular, if a ∈L then TrA/k(a) = [A :
L]TrL/K(a). If A is a ﬁeld, or even a division ring, then TrA/k(a) = [A : K[a]]TrK[a]/K(a).
Proof. Let (e1, . . . , em) be an ordered L-basis of A and (f1, . . . , fn) be an ordered K-basis
of L. Thus as an ordered K-basis of A we can use
(e1f1, . . . , e1fn; . . . ; emf1, . . . , emfn).
For a ∈A, let
aej =
m
X
i=1
cijei,
cijfs =
n
X
r=1
bijrsfr,
for cij ∈L and bijrs ∈K. Thus a(ejfs) = P
i
P
r bijrseifr. So
[ma]A/L = (cij),
[mcij]L/K = (bijrs),
[ma]A/K = ([mcij]L/K).
Thus
TrL/K(TrA/L(a))
=
TrL/K(
X
i
cii)
=
X
i
TrL/K(cii)
=
X
i
X
r
biirr
=
TrA/K(a).
□

<!-- page 9 -->
ALGEBRAS
9
We use Theorem 2.2 to establish a transitivity formula for norms in two cases.
Theorem 2.5. (i) Let L/K, K/k be ﬁnite extension ﬁelds, where k has characteristic 0 or
is ﬁnite or is algebraically closed. Then NL/k = NK/k◦NL/K.
(ii) If D is a ﬁnite-dimensional K-division algebra and k is a subﬁeld of K such that
[K : k] is ﬁnite, then for a ∈K, ND/k(a) = NK/k(ND/K(a)).
Proof. (i) Fix an algebraic closure k of k. Fix an embedding k ,→k. Let τ1, . . . , τm be the
distinct embeddings of K into k extending ψ. Each τi has n = [L : K] distinct extensions
σi1, . . . , σin to embeddings L →k. Thus
NK/k(NL/K(a))
=
m
Y
i=1
τi(NL/K(a))
=
m
Y
i=1
τi(τ −1
i
m
Y
j=1
σij(a))
=
Y
i,j
σij(a)
=
NL/k(a).
(ii) Let Ma(X) be the minimal polynomial of a in k[X]. By Theorem 2.1,
NK/k(ND/K(a))
=
NK/k(a[D:k])
=
(NK/k(a))[D:k]
=
((−1)[K:k]Ma(0)[K:k]/[k[a]:k])[D:K]
=
(−1)[D:k]Ma(0)[D:k]/[k[a]:k]
=
ND/k(a).
□
Remark 2.6. It is true more generally that for K/k a ﬁnite extension of ﬁelds and A a
ﬁnite-dimensional K-algebra that NA/k = NK/k ◦NA/K; see [1, Appendix B]. We will only
need here the transitivity of the norm map in the cases where we have proven it above.
We now describe how the characteristic polynomial varies over a division algebra.
Theorem 2.7. Let D be a ﬁnite k-division algebra, a ∈D. In k[X], let
χa(X) = (X −r1) · · · · · (X −rn).
For g(X) ∈k[X],
χg(a)(X) = (X −g(r1)) · · · · · (X −g(rn)).
In particular, χa+1(X) = χa(X−1) and χam(X) = (X−rm
1 )·· · ··(X−rm
n ), so ND/k(a+1) =
(−1)[D:k]χa(−1) and TrD/k(am) = P
i rm
i .
Proof. Let f(X) = (X −g(r1))·· · ··(X −g(rn)). The coeﬃcients are symmetric polynomials
in r1, . . . , rn, so by the symmetric function theorem f(X) ∈k[X]. Let Mg(a)(X) ∈k[X]
be the minimal polynomial of g(a) over k, so Mg(a) is irreducible in k[X] (since D is a
division ring). The ﬁelds k(a) and k(ri) are isomorphic k-algebras, so Mg(a) is the minimal
polynomial for g(ri) over k, since Mg(a) is irreducible monic in k[X] and has g(ri) as a root.

<!-- page 10 -->
10
KEITH CONRAD
Let π(X) be an irreducible monic factor of f in k[X]. Then π(g(ri)) = 0 for some i, so
Mg(a) | π in k[X]. Thus π = Mg(a), since both are monic and irreducible. Since f is monic,
we thus see that f is a power of Mg(a). By Theorem 2.1, χg(a) ∈k[X] is a power of Mg(a)
with degree [D : k] = n = deg(f), so f = χg(a).
□
The following theorem could have been part of the previous one, but we have chosen to
isolate it because its statement is worth remembering on its own. It gives a basic connection
between the norm and trace.
Theorem 2.8. Let D be an n-dimensional k-division algebra, for example a ﬁeld extension
of degree n. For a ∈D, let χa(X) = Xn + cn−1Xn−1 + · · · + c0 ∈k[X]. For all y ∈k,
ND/k(1 + ay)
=
1 −cn−1y + · · · + (−1)n−1c1yn−1 + (−1)nc0yn
=
1 + TrD/k(a)y + · · · + ND/k(a)yn,
so for ﬁxed a ∈D, y 7→ND/k(1 + ay) is a polynomial function in y ∈k.
Proof. We may assume y ̸= 0. In a splitting ﬁeld of χa, let χa(X) = Q
i(X −ri). By
Theorem 2.7, χ1+ay(X) = Q
i(X −(1 + yri)). Since y ∈k, y commutes with all elements of
D. So
ND/k(1 + ay)
=
(−1)nχ1+ay(0)
=
(−1)n Y
i
(−1 −yri)
=
(−y)n Y
i
(−1/y −ri)
=
(−y)nχa(−1/y)
=
(−y)n((−1/y)n + cn−1(−1/y)n−1 + · · · + c1(−1/y) + c0)
=
1 −cn−1y + · · · + (−1)n−1c1yn−1 + (−1)nc0yn.
□
Let A be a ﬁnite-dimensional k-algebra, say n = [A : k]. By choosing a k-basis of A,
we get an isomorphism A ∼= kn of k-vector spaces, allowing us to view the norm map
NA/k : A →k as a map kn →k. The next theorem shows that this is a polynomial map.
Note that the proof uses none of the theorems we have proven; it only uses the deﬁnition
of the norm map.
Theorem 2.9. For a k-basis e1, . . . , en of A, there is a P ∈k[X1, . . . , Xn] such that
NA/k(x1e1 + · · · + xnen) = P(x1, . . . , xn).
Proof. Let eiej = Pn
r=1 cijrer, cijr ∈k. For a = x1e1 + · · · + xnen with xi ∈k,
aej
=
X
r
xrerej
=
X
i
(
X
r
xrcrji)ei,
so with respect to the basis (e1, . . . , en), [ma] = (P
r xrcrji). Let
P(X1, . . . , Xn) = det(
X
r
crjiXr) ∈k[X1, . . . , Xn],

<!-- page 11 -->
ALGEBRAS
11
so NA/k(a) = P(x1, . . . , xn).
□
This concludes the results on algebras that we will need, but we make some additional
remarks for the interested reader. Since a 7→ma is an injective k-algebra homomorphism
from A to Homk(A, A), we see that the minimal polynomial Ma of a ∈A equals the
minimal polynomial of the linear map ma. By deﬁnition, the characteristic polynomial χa
of a equals the characteristic polynomial of the linear map ma. Thus, properties of minimal
or charactersitic polynomials of elements of a ﬁnite-dimensional k-algebra ought to follow
from properties of minimal or characteristic polynomials of matrices.
As an example of this principle, we show that Theorem 2.7 applies to all ﬁnite k-algebras,
not just division algebras. The characteristic polynomial of the linear map ma is Qn
i=1(X −
ri). By [3, Theorem 3.10, Chapter XIV], the characteristic polynomial of the linear map
g(ma) is Qn
i=1(X −g(ri)). Since g(ma) = mg(a), we are done. This implies that Theorem
2.8 is also true for ﬁnite k-algebras, since it is a formal consequence of Theorem 2.7.
Finally, note that in a ﬁnite k-algebra that is not a division algebra, χa is not necessarily
a power of Ma. For the relation between them when A is a matrix algebra (a fairly general
class of examples), see [3, §§2-3, Chapter XIV], where qa and Pa are written in place of Ma
and χa. See especially Theorem 2.1 and Theorem 3.5. The possible reducibility of Ma in
k[X] when A is not a division algebra can be viewed as the basic obstruction to χa being a
power of Ma.
Exercise. Let A be a ﬁnite k-algebra, a ∈A. Write
χa(X) = Xn + cn−1(a)Xn−1 + · · · + c1(a)X + c0(a),
so we view the coeﬃcients of χa as functions of a. For example, cn−1(a) = −TrA/k(a) and
c0(a) = (−1)nNA/k(a).
1. Show ci(ab) = ci(ba) for 0 ≤i ≤n −1 and a, b ∈A.
2. Show this is also true for Ma(X) in place of χa(X). How does this generalize to a
family fa(X) of polynomials such that fa(X) | χa(X) for all a?
References
[1] J.W.S. Cassels, Local Fields, Cambridge University Press, New York, 1986.
[2] I.N. Herstein, Topics In Algebra, 2nd ed., Wiley, New York, 1975.
[3] S. Lang, Algebra, 3rd ed., Addison-Wesley, New York, 1993.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*