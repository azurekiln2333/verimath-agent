# Tensor Products II

> **Source**: https://kconrad.math.uconn.edu/blurbs/tensorprod2.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
TENSOR PRODUCTS II
KEITH CONRAD
1. Introduction
Continuing our study of tensor products, we will see how to combine two linear maps
M −→M′ and N −→N′ into a linear map M ⊗R N →M′ ⊗R N′. This leads to ﬂat modules
and linear maps between base extensions. Then we will look at special features of tensor
products of vector spaces (including contraction), the tensor products of R-algebras, and
ﬁnally the tensor algebra of an R-module.
2. Tensor Products of Linear Maps
If M
ϕ
−−→M′ and N
ψ
−−→N′ are linear, then we get a linear map between the direct
sums, M ⊕N
ϕ⊕ψ
−−−−→M′ ⊕N′, deﬁned by (ϕ⊕ψ)(m, n) = (ϕ(m), ψ(n)). We want to deﬁne
a linear map M ⊗R N −→M′ ⊗R N′ such that m ⊗n 7→ϕ(m) ⊗ψ(n).
Start with the map M × N −→M′ ⊗R N′ where (m, n) 7→ϕ(m) ⊗ψ(n). This is R-
bilinear, so the universal mapping property of the tensor product gives us an R-linear map
M ⊗R N
ϕ⊗ψ
−−−−→M′ ⊗R N′ where (ϕ ⊗ψ)(m ⊗n) = ϕ(m) ⊗ψ(n), and more generally
(ϕ ⊗ψ)(m1 ⊗n1 + · · · + mk ⊗nk) = ϕ(m1) ⊗ψ(n1) + · · · + ϕ(mk) ⊗ψ(nk).
We call ϕ ⊗ψ the tensor product of ϕ and ψ, but be careful to appreciate that ϕ ⊗ψ is not
denoting an elementary tensor. This is just notation for a new linear map on M ⊗R N.
When M
ϕ
−−→M′ is linear, the linear maps N ⊗R M
1⊗ϕ
−−−−→N ⊗R M′ or M ⊗R N
ϕ⊗1
−−−−→
M′ ⊗R N are called tensoring with N. The map on N is the identity, so (1 ⊗ϕ)(n ⊗m) =
n ⊗ϕ(m) and (ϕ ⊗1)(m ⊗n) = ϕ(m) ⊗n. This construction will be particularly important
for base extensions in Section 4.
Example 2.1. Tensoring inclusion aZ
i
−−→Z with Z/bZ is aZ ⊗Z Z/bZ
i⊗1
−−−→Z ⊗Z Z/bZ,
where (i ⊗1)(ax ⊗y mod b) = ax ⊗(y mod b) = 1 ⊗(axy mod b) in Z ⊗Z Z/bZ. In Z/bZ,
⟨a mod b⟩= ⟨d mod b⟩where d = (a, b). Thus Z ⊗Z Z/bZ is spanned by 1 ⊗(1 mod b) and
the image of i ⊗1 is spanned by 1 ⊗(d mod b), so i ⊗1 has image Z/bZ if (a, b) = 1 and
image 0 if b | a. In particular, if a ≥2 and (a, b) = 1 then i ⊗1 is onto while i is not onto.
Example 2.2. Let A = ( a b
c d ) and A′ = ( a′ b′
c′ d′ ) in M2(R). Then A and A′ are both linear
maps R2 →R2, so A⊗A′ is a linear map from (R2)⊗2 = R2 ⊗R R2 back to itself. Writing e1
and e2 for the standard basis vectors of R2, let’s compute the matrix for A ⊗A′ on (R2)⊗2
1

<!-- page 2 -->
2
KEITH CONRAD
with respect to the basis {e1 ⊗e1, e1 ⊗e2, e2 ⊗e1, e2 ⊗e2}. By deﬁnition,
(A ⊗A′)(e1 ⊗e1) = Ae1 ⊗A′e1
= (ae1 + ce2) ⊗(a′e1 + c′e2)
= aa′e1 ⊗e1 + ac′e1 ⊗e2 + ca′e2 ⊗e1 + cc′e2 ⊗e2,
(A ⊗A′)(e1 ⊗e2) = Ae1 ⊗A′e2
= (ae1 + ce2) ⊗(b′e1 + d′e2)
= cb′e1 ⊗e1 + ad′e1 ⊗e2 + cb′e2 ⊗e2 + cd′e2 ⊗e2,
and similarly
(A ⊗A′)(e2 ⊗e1) = ba′e1 ⊗e1 + bc′e1 ⊗e2 + da′e2 ⊗e1 + dc′e2 ⊗e2,
(A ⊗A′)(e2 ⊗e2) = bb′e1 ⊗e1 + bd′e1 ⊗e2 + db′e2 ⊗e1 + dd′e2 ⊗e2.
Therefore the matrix for A ⊗A′ is




aa′
ab′
ba′
bb′
ac′
ad′
bc′
bd′
ca′
cb′
da′
db′
cc′
cd′
dc′
dd′



=
 aA′
bA′
cA′
dA′

.
So Tr(A ⊗A′) = a(a′ + d′) + d(a′ + d′) = (a + d)(a′ + d′) = (Tr A)(Tr A′), and det(A ⊗A′)
looks painful to compute from the matrix. We’ll do this later, in Example 2.7, in an almost
painless way.
If, more generally, A ∈Mn(R) and A′ ∈Mn′(R) then the matrix for A ⊗A′ with respect
to the standard basis for Rn ⊗R Rn′ is the block matrix (aijA′) where A = (aij). This
nn′ × nn′ matrix is called the Kronecker product of A and A′, and is not symmetric in the
roles of A and A′ in general (just as A ⊗A′ ̸= A′ ⊗A in general). In particular, In ⊗A′ has
block matrix representation (δijA′), whose determinant is (det A′)n.
The construction of tensor products (Kronecker products) of matrices has the following
application to ﬁnding polynomials with particular roots.
Theorem 2.3. Let K be a ﬁeld and suppose A ∈Mm(K) and B ∈Mn(K) have eigenvalues
λ and µ in K. Then A ⊗In + Im ⊗B has eigenvalue λ + µ and A ⊗B has eigenvalue λµ.
Proof. We have Av = λv and Bw = µw for some v ∈Km and w ∈Kn. Then
(A ⊗In + Im ⊗B)(v ⊗w) = Av ⊗w + v ⊗Bw
= λv ⊗w + v ⊗µw
= (λ + µ)(v ⊗w)
and
(A ⊗B)(v ⊗w) = Av ⊗Bw = λv ⊗µw = λµ(v ⊗w).
□

<!-- page 3 -->
TENSOR PRODUCTS II
3
Example 2.4. The numbers
√
2 and
√
3 are eigenvalues of A = ( 0 2
1 0 ) and B = ( 0 3
1 0 ). A
matrix with eigenvalue
√
2 +
√
3 is
A ⊗I2 + I2 ⊗B =




0
0
2
0
0
0
0
2
1
0
0
0
0
1
0
0



+




0
3
0
0
1
0
0
0
0
0
0
3
0
0
1
0




=




0
3
2
0
1
0
0
2
1
0
0
3
0
1
1
0



,
whose characteristic polynomial is T 4 −10T 2 + 1. So this is a polynomial with
√
2 +
√
3 as
a root.
Although we stressed that ϕ ⊗ψ is not an elementary tensor, but rather is the notation
for a linear map, ϕ and ψ belong to the R-modules HomR(M, M′) and HomR(N, N′), so
one could ask if the actual elementary tensor ϕ ⊗ψ in HomR(M, M′) ⊗R HomR(N, N′) is
related to the linear map ϕ ⊗ψ: M ⊗R N →M′ ⊗R N′.
Theorem 2.5. There is a linear map
HomR(M, M′) ⊗R HomR(N, N′) →HomR(M ⊗R N, M′ ⊗R N′)
that sends the elementary tensor ϕ ⊗ψ to the linear map ϕ ⊗ψ. When M, M′, N, and N′
are ﬁnite free, this is an isomorphism.
Proof. We adopt the temporary notation T(ϕ, ψ) for the linear map we have previously
written as ϕ ⊗ψ, so we can use ϕ ⊗ψ to mean an elementary tensor in the tensor product
of Hom-modules. So T(ϕ, ψ): M ⊗R N →M′ ⊗R N′ is the linear map sending every m ⊗n
to ϕ(m) ⊗ψ(n).
Deﬁne HomR(M, M′)×HomR(N, N′) →HomR(M ⊗RN, M′⊗RN′) by (ϕ, ψ) 7→T(ϕ, ψ).
This is R-bilinear. For example, to show T(rϕ, ψ) = rT(ϕ, ψ), both sides are linear maps
so to prove they are equal it suﬃces to check they are equal at the elementary tensors in
M ⊗R N:
T(rϕ, ψ)(m ⊗n) = (rϕ)(m) ⊗ψ(n) = rϕ(m) ⊗ψ(n) = r(ϕ(m) ⊗ψ(n)) = rT(ϕ, ψ)(m ⊗n).
The other bilinearity conditions are left to the reader.
From the universal mapping property of tensor products, there is a unique R-linear map
HomR(M, M′) ⊗R HomR(N, N′) →HomR(M ⊗R N, M′ ⊗R N′) where ϕ ⊗ψ 7→T(ϕ, ψ).
Suppose M, M′, N, and N′ are all ﬁnite free R-modules. Let them have respective bases
{ei}, {e′
i′}, {fj}, and {f′
j′}. Then HomR(M, M′) and HomR(N, N′) are both free with bases
{Ei′i} and { eEj′j}, where Ei′i : M →M′ is the linear map sending ei to e′
i′ and is 0 at other
basis vectors of M, and eEj′j : N →N′ is deﬁned similarly. (The matrix representation
of Ei′i with respect to the chosen bases of M and M′ has a 1 in the (i′, i) position and
0 elsewhere, thus justifying the notation.) A basis of HomR(M, M′) ⊗R HomR(N, N′) is

<!-- page 4 -->
4
KEITH CONRAD
{Ei′i ⊗eEj′j} and T(Ei′i ⊗eEj′j): M ⊗R N →M′ ⊗R N′ has the eﬀect
T(Ei′i ⊗eEj′j)(eµ ⊗fν) = Ei′i(eµ) ⊗eEj′j(fν)
= δµie′
i′ ⊗δνjf′
j′
=
(
e′
i′ ⊗f′
j′,
if µ = i and ν = j,
0,
otherwise,
so T(Ei′i⊗Ej′j) sends ei⊗fj to e′
i′⊗f′
j′ and sends other members of the basis of M⊗RN to 0.
That means the linear map HomR(M, M′) ⊗R HomR(N, N′) →HomR(M ⊗R N, M′ ⊗R N′)
sends a basis to a basis, so it is an isomorphism when the modules are ﬁnite free.
□
The upshot of Theorem 2.5 is that HomR(M, M′) ⊗R HomR(N, N′) naturally acts as
linear maps M ⊗R N →M′ ⊗R N′ and it turns the elementary tensor ϕ ⊗ψ into the linear
map we’ve been writing as ϕ ⊗ψ. This justiﬁes our use of the notation ϕ ⊗ψ for the linear
map, but it should be kept in mind that we will continue to write ϕ ⊗ψ for the linear map
itself (on M ⊗R N) and not for an elementary tensor in a tensor product of Hom-modules.
Properties of tensor products of modules carry over to properties of tensor products of
linear maps, by checking equality on all tensors. For example, if ϕ1 : M1 →N1, ϕ2 : M2 →
N2, and ϕ3 : M3 →N3 are linear maps, we have ϕ1 ⊗(ϕ2 ⊕ϕ3) = (ϕ1 ⊗ϕ2) ⊕(ϕ1 ⊗ϕ3)
and (ϕ1 ⊗ϕ2) ⊗ϕ3 = ϕ1 ⊗(ϕ2 ⊗ϕ3), in the sense that the diagrams
M1 ⊗R (M2 ⊕M3)

ϕ1⊗(ϕ2⊕ϕ3)
/ N1 ⊗R (N2 ⊕N3)

(M1 ⊗R M2) ⊕(M1 ⊗R M3)
(ϕ1⊗ϕ2)⊕(ϕ1⊗ϕ3)
/ (N1 ⊗R N2) ⊕(N1 ⊗R N3)
and
M1 ⊗R (M2 ⊗R M3)

ϕ1⊗(ϕ2⊗ϕ3) / N1 ⊗R (N2 ⊗R N3)

(M1 ⊗R M2) ⊗R M3
(ϕ1⊗ϕ2)⊗ϕ3 / (N1 ⊗R N2) ⊗R N3
commute, with the vertical maps being the canonical isomorphisms.
The properties of the next theorem are called the functoriality of the tensor product of
linear maps.
Theorem 2.6. For R-modules M and N, idM ⊗idN = idM⊗RN. For linear maps M
ϕ
−−→
M′, M′
ϕ′
−−→M′′, N
ψ
−−→N′, and N′
ψ′
−−−→N′′,
(ϕ′ ⊗ψ′) ◦(ϕ ⊗ψ) = (ϕ′ ◦ϕ) ⊗(ψ′ ◦ψ)
as linear maps from M ⊗R N to M′′ ⊗R N′′.
Proof. The function idM ⊗idN is a linear map from M ⊗R N to itself that ﬁxes every
elementary tensor, so it ﬁxes all tensors.
Since (ϕ′ ⊗ψ′) ◦(ϕ ⊗ψ) and (ϕ′ ◦ϕ) ⊗(ψ′ ◦ψ) are linear maps, to prove their equality it
suﬃces to check they have the same value at any elementary tensor m ⊗n, at which they
both have the value ϕ′(ϕ(m)) ⊗ψ′(ψ(n)).
□

<!-- page 5 -->
TENSOR PRODUCTS II
5
Example 2.7. The composition rule for tensor products of linear maps helps us compute
determinants of tensor products of linear operators. Let M and N be ﬁnite free R-modules
of respective ranks k and ℓ. For linear operators M
ϕ
−−→M and N
ψ
−−→N, we will compute
det(ϕ ⊗ψ) by breaking up ϕ ⊗ψ into a composite of two maps M ⊗R N →M ⊗R N:
ϕ ⊗ψ = (ϕ ⊗idN) ◦(idM ⊗ψ),
so the multiplicativity of the determinant implies det(ϕ ⊗ψ) = det(ϕ ⊗idN) det(idM ⊗ψ)
and we are reduced to the case when one of the “factors” is an identity map. Moreover, the
isomorphism M ⊗R N →N ⊗R M where m ⊗n 7→n ⊗m converts ϕ ⊗idN into idN ⊗ϕ, so
det(ϕ ⊗idN) = det(idN ⊗ϕ), so
det(ϕ ⊗ψ) = det(idN ⊗ϕ) det(idM ⊗ψ).
What are the determinants on the right side? Pick bases e1, . . . , ek of M and e′
1, . . . , e′
ℓof
N. We will use the kℓelementary tensors ei ⊗e′
j as a bases of M ⊗R N. Let [ϕ] be the
matrix of ϕ in the ordered basis e1, . . . , ek. Since (ϕ ⊗idN)(ei ⊗e′
j) = ϕ(ei) ⊗e′
j, let’s order
the basis of M ⊗R N as
e1 ⊗e′
1, . . . , ek ⊗e′
1, . . . , e1 ⊗e′
ℓ, . . . , ek ⊗e′
ℓ.
The kℓ× kℓmatrix for ϕ ⊗idN in this ordered basis is the block diagonal matrix





[ϕ]
O
· · ·
O
O
[ϕ]
· · ·
O
...
...
...
...
O
O
· · ·
[ϕ]




,
whose determinant is (det ϕ)ℓ.
Thus
(2.1)
det(ϕ ⊗ψ) = (det ϕ)ℓ(det ψ)k.
Note ℓis the rank of the module on which ψ is deﬁned and k is the rank of the module on
which ϕ is deﬁned. In particular, in Example 2.2 we have det(A ⊗A′) = (det A)2(det A′)2.
Let’s review the idea in this proof. Since N ∼= Rℓ, M ⊗R N ∼= M ⊗R Rℓ∼= M⊕ℓ. Under
such an isomorphism, ϕ ⊗idN becomes the ℓ-fold direct sum ϕ ⊕· · · ⊕ϕ, which has a block
diagonal matrix representation in a suitable basis. So its determinant is (det ϕ)ℓ.
Example 2.8. Taking M = N and ϕ = ψ, the tensor square ϕ⊗2 has determinant (det ϕ)2k.
Corollary 2.9. Let M be a free module of rank k ≥1 and ϕ: M →M be a linear map.
For every i ≥1, det(ϕ⊗i) = (det ϕ)iki−1.
Proof. Use induction and associativity of the tensor product of linear maps.
□
Remark 2.10. Equation (2.1) in the setting of vector spaces and matrices says det(A⊗B) =
(det A)ℓ(det B)k, where A is k ×k, B is ℓ×ℓ, and A⊗B = (aijB) is the matrix incarnation
of a tensor product of linear maps, called the Kronecker product of A and B at the end
of Example 2.2. While the label “Kronecker product” for the matrix A ⊗B is completely
standard, it is not historically accurate. It is based on Hensel’s attribution of the formula
for det(A ⊗B) to Kronecker, but the formula is due to Zehfuss. See [2].
Let’s see how the tensor product of linear maps behaves for isomorphisms, surjections,
and injections.

<!-- page 6 -->
6
KEITH CONRAD
Theorem 2.11. If ϕ: M →M′ and ψ: N →N′ are isomorphisms then ϕ ⊗ψ is an
isomorphism.
Proof. The composite of ϕ ⊗ψ with ϕ−1 ⊗ψ−1 in both orders is the identity.
□
Theorem 2.12. If ϕ: M →M′ and ψ: N →N′ are surjective then ϕ ⊗ψ is surjective.
Proof. Since ϕ ⊗ψ is linear, to show it is onto it suﬃces to show every elementary tensor in
M′⊗RN′ is in the image. For such an elementary tensor m′⊗n′, we can write m′ = ϕ(m) and
n′ = ψ(n) since ϕ and ψ are onto. Therefore m′ ⊗n′ = ϕ(m) ⊗ψ(n) = (ϕ ⊗ψ)(m ⊗n).
□
It is a fundamental feature of tensor products that if ϕ and ψ are both injective then
ϕ ⊗ψ might not be injective. This can occur even if one of ϕ or ψ is the identity function.
Example 2.13. Taking R = Z, let α: Z/pZ →Z/p2Z be multiplication by p: α(x) = px.
This is injective, and if we tensor with Z/pZ we get the linear map 1⊗α: Z/pZ⊗Z Z/pZ →
Z/pZ ⊗Z Z/p2Z with the eﬀect a ⊗x 7→a ⊗px = pa ⊗x = 0, so 1 ⊗α is identically 0 and
its domain is Z/pZ ⊗Z Z/pZ ∼= Z/pZ ̸= 0, so 1 ⊗α is not injective.
This provides an example where the natural linear map
HomR(M, M′) ⊗R HomR(N, N′) →HomR(M ⊗R N, M′ ⊗R N′)
in Theorem 2.5 is not an isomorphism; R = Z, M = M′ = N = Z/pZ, and N′ = Z/p2Z.
Because the tensor product of linear maps does not generally preserve injectivity, a tensor
has to be understood in context: it is a tensor in a speciﬁc tensor product module M ⊗R N.
If M ⊂M′ and N ⊂N′, it is generally false that M ⊗R N can be thought of as a submodule
of M′ ⊗R N′ since the natural map M ⊗R N →M′ ⊗R N′ may not be injective. We can
say it this way: a tensor product of submodules need not be a submodule.
Example 2.14. Since pZ ∼= Z as abelian groups, by pn 7→n, we have Z/pZ ⊗Z pZ ∼=
Z/pZ ⊗Z Z ∼= Z/pZ as abelian groups by a ⊗pn 7→a ⊗n 7→na mod p. Therefore 1 ⊗p in
Z/pZ ⊗Z pZ is nonzero, since the isomorphism identiﬁes it with 1 in Z/pZ. However, 1 ⊗p
in Z/pZ⊗Z Z is 0, since 1⊗p = p⊗1 = 0⊗1 = 0. (This calculation with 1⊗p doesn’t work
in Z/pZ ⊗Z pZ since we can’t bring p to the left side of ⊗and leave 1 behind, as 1 ̸∈pZ.)
It might seem weird that 1⊗p is nonzero in Z/pZ⊗ZpZ while 1⊗p is zero in the “larger”
abelian group Z/pZ ⊗Z Z! The reason there isn’t a contradiction is that Z/pZ ⊗Z pZ is not
really a subgroup of Z/pZ⊗Z Z even though pZ is a subgroup of Z. The inclusion mapping
i: pZ →Z gives us a natural mapping 1 ⊗i: Z/pZ ⊗Z pZ →Z/pZ ⊗Z Z, with the eﬀect
a ⊗pn 7→a ⊗pn, but this is not an embedding. In fact its image is 0: in Z/pZ ⊗Z Z,
a ⊗pn = pa ⊗n = 0 ⊗n = 0. The moral is that an elementary tensor a ⊗pn means
something diﬀerent in Z/pZ ⊗Z pZ and in Z/pZ ⊗Z Z.
This example also shows the image of M ⊗R N
ϕ⊗ψ
−−−−→M′ ⊗R N′ need not be isomorphic
to ϕ(M) ⊗R ψ(N), since 1 ⊗i has image 0 and Z/pZ ⊗Z i(pZ) ∼= Z/pZ ⊗Z Z ∼= Z/pZ.
Example 2.15. While Z/pZ ⊗Z Z ∼= Z/pZ, if we enlarge the second tensor factor Z to Q
we get a huge collapse: Z/pZ ⊗Z Q = 0 since a ⊗r = a ⊗p(r/p) = pa ⊗r/p = 0 ⊗r/p = 0.
In particular, 1 ⊗1 is nonzero in Z/pZ ⊗Z Z but 1 ⊗1 = 0 in Z/pZ ⊗Z Q.
In terms of tensor products of linear mappings, this example says that tensoring the
inclusion i: Z ,→Q with Z/pZ gives us a Z-linear map 1 ⊗i: Z/pZ ⊗Z Z →Z/pZ ⊗Z Q
that is not injective: the domain is isomorphic to Z/pZ and the target is 0.

<!-- page 7 -->
TENSOR PRODUCTS II
7
Darij Grinberg1 gave a nice clariﬁcation of this confusing situation: it is due to an abuse of
notation when writing elementary tensors as m⊗n without indicating the ambient modules
that m and n lie in. Including those modules in the notation, say by writing m ⊗n as
(m, M) ⊗R (n, N), would avoid the confusion at the cost of very clumsy notation.
Example 2.16. Here is an example of a linear map M →N that is injective and its tensor
square M⊗2 →N⊗2 is not injective.
Let R = A[X, Y ] where A is a nonzero commutative ring and I = (X, Y ) in R. The
natural map I →R is injective. We’ll show its tensor square I⊗2 →R⊗2 is not injective by
giving distinct tensors in I⊗2 that are equal in R⊗2. In R⊗2,
(2.2)
X ⊗Y = XY (1 ⊗1) and Y ⊗X = Y X(1 ⊗1) = XY (1 ⊗1),
so X ⊗Y = Y ⊗X in R⊗2. We will now show that X ⊗Y ̸= Y ⊗X in I⊗2. (The calculation
in (2.2) makes no sense in I⊗2 since 1 ̸∈I.) To show two tensors in I⊗2 are not equal, we’ll
construct a linear map out of I⊗2 with diﬀerent values at the two tensors. The function
I × I →A given by (f, g) 7→fX(0, 0)gY (0, 0), where fX and gY are partial derivatives
of f and g with respect to X and Y , is R-bilinear. (Treat the target A as an R-module
through multiplication by the constant term of polynomials in R, or just view A as R/I
with ordinary multiplication by R.) Thus there is an R-linear map I⊗2 →A sending any
elementary tensor f ⊗g to fX(0, 0)gY (0, 0). In particular, X ⊗Y 7→1 and Y ⊗X 7→0, so
X ⊗Y ̸= Y ⊗X in I⊗2.
It might seem weird that X ⊗Y and Y ⊗X are equal in R⊗2 but are not equal in I⊗2,
even though X and Y are elements of I and I ⊂R. We must be careful when we think
about a tensor t ∈I ⊗R I as a tensor in R ⊗R R. Letting i: I ,→R be the inclusion map,
thinking about t in R⊗2 means looking at i⊗2(t), where i⊗2 : I⊗2 →R⊗2. For the tensor
t = X ⊗Y −Y ⊗X in I⊗2, we computed above that t ̸= 0 but i⊗2(t) = 0, so i⊗2 is not
injective even though i is injective. In other words, the natural way to think of I ⊗R I
“inside” R ⊗R R is actually not an embedding. For polynomials f and g in I, you have to
distinguish between the tensor f ⊗g in I ⊗R I and the tensor f ⊗g in R ⊗R R.
Generalizing this, let R = A[X1, . . . , Xn] where n ≥2 and I = (X1, . . . , Xn).
The
inclusion i: I ,→R is injective but the nth tensor power (as R-modules) i⊗n : I⊗n →R⊗n
is not injective because the tensor
t :=
X
σ∈Sn
(sign σ)Xσ(1) ⊗· · · ⊗Xσ(n) ∈I⊗n
gets sent to P
σ∈Sn(sign σ)X1 · · · Xn(1 ⊗· · · ⊗1) in R⊗n, which is 0, but t is not 0 in
I⊗n because there is an R-linear map I⊗n →A sending t to 1: use a product of partial
derivatives at (0, 0, . . . , 0), as in the n = 2 case.
Remark 2.17. The ideal I = (X, Y ) in R = A[X, Y ] from Example 2.16 has another
interesting feature when A is a domain: it is a torsion-free R-module but I⊗2 is not:
X(X ⊗Y ) = X ⊗XY = Y (X ⊗X) and X(Y ⊗X) = XY ⊗X = Y (X ⊗X), so in I⊗2 we
have X(X ⊗Y −Y ⊗X) = 0, but X ⊗Y −Y ⊗X ̸= 0. Similarly, Y (X ⊗Y −Y ⊗X) = 0.
Thus a tensor product of torsion-free modules (even over a domain) need not be torsion-free.
While Example 2.16 tells us by an example that a tensor power of an injective linear map
need not be injective, here is a condition where injectivity holds.
1See https://math.stackexchange.com/questions/3452281.

<!-- page 8 -->
8
KEITH CONRAD
Theorem 2.18. Let ϕ: M →N be injective and ϕ(M) be a direct summand of N. For
k ≥0, ϕ⊗k : M⊗k →N⊗k is injective and the image is a direct summand of N⊗k.
Proof. Write N = ϕ(M) ⊕P. Let π: N ↠M by π(ϕ(m) + p) = m, so π is linear and
π ◦ϕ = idM. Then ϕ⊗k : M⊗k →N⊗k and π⊗k : N⊗k ↠M⊗k are linear maps and
π⊗k ◦ϕ⊗k = (π ◦ϕ)⊗k = id⊗k
M = idM⊗k,
so ϕ⊗k has a left inverse. That implies ϕ⊗k is injective and M⊗k is isomorphic to a direct
summand of N⊗k by criteria for when a short exact sequence of modules splits.
□
We can apply this to vector spaces: if V is a vector space and W is a subspace, there
is a direct sum decomposition V = W ⊕U (U is non-canonical), so tensor powers of the
inclusion W →V are injective linear maps W ⊗k →V ⊗k.
Other criteria for a tensor power of an injective linear map to be injective will be met in
Corollary 3.13 and Theorem 4.9.
We will now compute the kernel of M ⊗R N
ϕ⊗ψ
−−−−→M′ ⊗R N′ in terms of the kernels of
ϕ and ψ, assuming ϕ and ψ are onto.
Theorem 2.19. Let M
ϕ
−−→M′ and N
ψ
−−→N′ be R-linear and surjective. The kernel
of M ⊗R N
ϕ⊗ψ
−−−−→M′ ⊗R N′ is the submodule of M ⊗R N spanned by all m ⊗n where
ϕ(m) = 0 or ψ(n) = 0. That is, intuitively
ker(ϕ ⊗ψ) = (ker ϕ) ⊗R N + M ⊗R (ker ψ),
while rigorously in terms of the inclusion maps ker ϕ
i
−−→M and ker ψ
j
−−→N,
ker(ϕ ⊗ψ) = (i ⊗1)((ker ϕ) ⊗R N) + (1 ⊗j)(M ⊗R (ker ψ)).
The reason (ker ϕ)⊗RN +M ⊗R(ker ψ) is only an intuitive formula for the kernel of ϕ⊗ψ
is that, strictly speaking, these tensor product modules are not submodules of M ⊗R N.
Only after applying i ⊗1 and 1 ⊗j to them – and these might not be injective – do those
modules become submodules of M ⊗R N.
Proof. Both (i⊗1)((ker ϕ)⊗RN) and (1⊗j)(M ⊗R(ker ψ)) are killed by ϕ⊗ψ: if m ∈ker ϕ
and n ∈N then (ϕ ⊗ψ)((i ⊗1)(m ⊗n)) = (ϕ ⊗ψ)(m ⊗n) = ϕ(m) ⊗ψ(n) = 0 since2
ϕ(m) = 0. Similarly (1 ⊗j)(m ⊗n) is killed by ϕ ⊗ψ if m ∈M and n ∈ker ψ. Set
U = (i ⊗1)((ker ϕ) ⊗R N) + (1 ⊗j)(M ⊗R (ker ψ)),
so U ⊂ker(ϕ ⊗ψ), which means ϕ ⊗ψ induces a linear map
Φ: (M ⊗R N)/U →M′ ⊗R N′
where Φ(m ⊗n mod U) = (ϕ ⊗ψ)(m ⊗n) = ϕ(m) ⊗ψ(n). We will now write down an
inverse map, which proves Φ is injective, so the kernel of ϕ ⊗ψ is U.
Because ϕ and ψ are assumed to be onto, every elementary tensor in M′ ⊗R N′ has the
form ϕ(m) ⊗ψ(n). Knowing ϕ(m) and ψ(n) only determines m and n up to addition by
elements of ker ϕ and ker ψ. For m′ ∈ker ϕ and n′ ∈ker ψ,
(m + m′) ⊗(n + n′) = m ⊗n + m′ ⊗n + m ⊗n′ + m′ ⊗n′ ∈m ⊗n + U,
2The ﬁrst m ⊗n is in (ker ϕ) ⊗R N, while the second m ⊗n is in M ⊗R N.

<!-- page 9 -->
TENSOR PRODUCTS II
9
so the function M′ × N′ →(M ⊗R N)/U deﬁned by (ϕ(m), ψ(n)) 7→m ⊗n mod U is well-
deﬁned. It is R-bilinear, so we have an R-linear map Ψ: M′ ⊗R N′ →(M ⊗R N)/U where
Ψ(ϕ(m) ⊗ψ(n)) = m ⊗n mod U on elementary tensors.
Easily the linear maps Φ◦Ψ and Ψ◦Φ ﬁx spanning sets, so they are both the identity.
□
Remark 2.20. If we don’t assume ϕ and ψ are onto, Theorem 2.19 does not correctly
compute the kernel. For example, if ϕ and ψ are both injective then the formula for the
kernel in Theorem 2.19 is 0 while we know ϕ ⊗ψ need not be injective by Example 2.16.
Example 2.21. When I is an ideal in R and M and N are R-modules, let ϕ : M →M/IM
and ψ : N →N/IN be the natural maps. Theorem 2.19 tells us the map ϕ⊗ψ : M ⊗RN →
(M/IM) ⊗R (N/IN) has kernel spanned as an R-module by all m ⊗n where m ∈IM or
n ∈IN. The span of such elementary tensors is I(M ⊗R N) (why?), so
(M ⊗R N)/I(M ⊗R N) ∼= (M/IM) ⊗R (N/IN).
Unlike the kernel computation in Theorem 2.19, it is not easy to describe the torsion
submodule of a tensor product in terms of the torsion submodules of the original modules.
While (M ⊗RN)tor contains (i⊗1)(Mtor⊗RN)+(1⊗j)(M ⊗RNtor), with i: Mtor →M and
j : Ntor →N being the inclusions, it is not true that this is all of (M ⊗RN)tor, since M ⊗RN
can have nonzero torsion when M and N are torsion-free (so Mtor = 0 and Ntor = 0). We
saw this at the end of Example 2.16.
Corollary 2.22. If M
ϕ
−−→M′ is an isomorphism of R-modules and N
ψ
−−→N′ is surjec-
tive, then the linear map M ⊗R N
ϕ⊗ψ
−−−−→M′ ⊗R N′ has kernel (1⊗j)(M ⊗R (ker ψ)), where
ker ψ
j
−−→N is the inclusion.
Proof. This is immediate from Theorem 2.19 since ker ϕ = 0.
□
Corollary 2.23. Let f : R →S be a homomorphism of commutative rings and M ⊂N as
R-modules, with M
i
−−→N the inclusion map. The following are equivalent:
(1) S ⊗R M
1⊗i
−−−→S ⊗R N is onto.
(2) S ⊗R (N/M) = 0.
Proof. Let N
π
−−→N/M be the reduction map, so we have the sequence S ⊗R M
1⊗i
−−−→
S ⊗R N
1⊗π
−−−−→S ⊗R (N/M). The map 1 ⊗π is onto, and ker π = M, so ker(1 ⊗π) =
(1 ⊗i)(S ⊗R M). Therefore 1 ⊗i is onto if and only if ker(1 ⊗π) = S ⊗R N if and only if
1 ⊗π = 0, and since 1 ⊗π is onto we have 1 ⊗π = 0 if and only if S ⊗R (N/M) = 0.
□
Example 2.24. If M ⊂N and N is ﬁnitely generated, we show M = N if and only if the
natural map R/m ⊗R M
1⊗i
−−−→R/m ⊗R N is onto for all maximal ideals m in R, where
M
i
−−→N is the inclusion map. The “only if” direction is clear. In the other direction, if
R/m ⊗R M
1⊗i
−−−→R/m ⊗R N is onto then R/m ⊗R (N/M) = 0 by Corollary 2.23. Since N
is ﬁnitely generated, so is N/M, and we are reduced to showing R/m ⊗R (N/M) = 0 for all
maximal ideals m if and only if N/M = 0. When P is a ﬁnitely generated module, P = 0
if and only if P/mP = 0 for all maximal ideals3 m in R, so we can apply this to P = N/M
since P/mP ∼= R/m ⊗R P.
3P/mP = 0 ⇒P = mP ⇒Pm = mPm ⇒Pm = 0 by Nakayama’s lemma. From Pm = 0 for all maximal
ideals m, P = 0: for all x ∈P, x = 0 in Pm implies ax = 0 in P for some a ∈R −m. Thus AnnR(x) is not
in any maximal ideal of R, so AnnR(x) = R and thus x = 1 · x = 0.

<!-- page 10 -->
10
KEITH CONRAD
Corollary 2.25. Let f : R →S be a homomorphism of commutative rings and I be an
ideal in R[X1, . . . , Xn]. Write I · S[X1, . . . , Xn] for the ideal generated by the image of I in
S[X1, . . . , Xn]. Then
S ⊗R R[X1, . . . , Xn]/I ∼= S[X1, . . . , Xn]/(I · S[X1, . . . , Xn]).
as S-modules by s ⊗h mod I 7→sh mod I · S[X1, . . . , Xn].
Proof. The identity S →S and the natural reduction R[X1, . . . , Xn] ↠R[X1, . . . , Xn]/I
are both onto, so the tensor product of these R-linear maps is an R-linear surjection
(2.3)
S ⊗R R[X1, . . . , Xn] ↠S ⊗R (R[X1, . . . , Xn]/I)
and the kernel is (1 ⊗j)(S ⊗R I) by Theorem 2.19, where j : I →R[X1, . . . , Xn] is the
inclusion. Under the natural R-module isomorphism
(2.4)
S ⊗R R[X1, . . . , Xn] ∼= S[X1, . . . , Xn],
(1 ⊗j)(S ⊗R I) on the left side corresponds to I · S[X1, . . . , Xn] on the right side, so (2.3)
and (2.4) say
S[X1, . . . , Xn]/(I · S[X1, . . . , Xn]) ∼= S ⊗R (R[X1, . . . , Xn]/I).
as R-modules. The left side is naturally an S-module and the right side is too using extension
of scalars. It is left to the reader to check the isomorphism is S-linear.
□
Example 2.26. For h(X) ∈Z[X], Q ⊗Z Z[X]/(h(X)) ∼= Q[X]/(h(X)) as Q-vector spaces
and Z/mZ ⊗Z Z[X]/(h(X)) = (Z/mZ)[X]/(h(X)) as Z/mZ-modules where m > 1.
3. Flat Modules
Because a tensor product of injective linear maps might not be injective, it is important
to give a name to those R-modules N that always preserve injectivity, in the sense that
M
ϕ
−−→M′ being injective implies N ⊗R M
1⊗ϕ
−−−−→N ⊗R M′ is injective. (Notice the map
on N is the identity.)
Deﬁnition 3.1. An R-module N is called ﬂat if for all injective linear maps M
ϕ
−−→M′
the linear map N ⊗R M
1⊗ϕ
−−−−→N ⊗R M′ is injective.
The concept of a ﬂat module is pointless unless one has some good examples. The next
two theorems provide some.
Theorem 3.2. Any free R-module F is ﬂat: if the linear map ϕ: M →M′ is injective,
then 1 ⊗ϕ: F ⊗R M →F ⊗R M′ is injective.
Proof. When F = 0 it is clear, so take F ̸= 0 with basis {ei}i∈I.
From our previous
development of the tensor product, every element of F ⊗R M can be written as P
i ei ⊗mi
for a unique choice of mi ∈M, and similarly for F ⊗R M′.
For t ∈ker(1 ⊗ϕ), we can write t = P
i ei ⊗mi with mi ∈M. Then
0 = (1 ⊗ϕ)(t) =
X
i
ei ⊗ϕ(mi),
in F ⊗R M′, which forces each ϕ(mi) to be 0. So every mi is 0, since ϕ is injective, and we
get t = P
i ei ⊗0 = 0.
□
Note that in Theorem 3.2 we did not need to assume F has a ﬁnite basis.

<!-- page 11 -->
TENSOR PRODUCTS II
11
Theorem 3.3. Let R be a domain and K be its fraction ﬁeld. As an R-module, K is ﬂat.
This is not a special case of the previous theorem: if K were a free R-module then4
K = R, so whenever R is a domain that is not a ﬁeld (e.g., R = Z) the fraction ﬁeld of R
is a ﬂat R-module that is not a free R-module.
Proof. Let M
ϕ
−−→M′ be an injective linear map of R-modules. Every tensor in K ⊗R M is
elementary (use common denominators in K) and an elementary tensor in K ⊗R M is 0 if
and only if its ﬁrst factor is 0 or its second factor is torsion. (Here we are using properties
of K ⊗R M proved in part I.)
Supposing (1 ⊗ϕ)(t) = 0, we may write t = x ⊗m, so 0 = (1 ⊗ϕ)(t) = x ⊗ϕ(m).
Therefore x = 0 in K or ϕ(m) ∈M′
tor. If ϕ(m) ∈M′
tor then rϕ(m) = 0 for some nonzero
r ∈R, so ϕ(rm) = 0, so rm = 0 in M (ϕ is injective), which means m ∈Mtor. Thus x = 0
or m ∈Mtor, so t = x ⊗m = 0.
□
If M is a submodule of the R-module M′ then Theorem 3.3 says we can consider K ⊗RM
as a subspace of K ⊗R M′ since the natural map K ⊗R M →K ⊗R M′ is injective. (See
diagram below.) Notice this works even if M or M′ has torsion; although the natural maps
M →K ⊗R M and M′ →R K ⊗R M′ might not be injective, the map K ⊗R M →K ⊗R M′
is injective.
M  
ϕ
/

M′

K ⊗R M  
1⊗ϕ
/ K ⊗R M′
Example 3.4. The natural inclusion Z ,→Z/3Z ⊕Z is Z-linear and injective. Applying
Q⊗Z to both sides and using properties of tensor products turns this into the identity map
Q →Q, which is also injective.
Remark 3.5. Theorem 3.3 generalizes: for any commutative ring R and multiplicative set
D in R, the localization RD is a ﬂat R-module.
Theorem 3.6. If M is a ﬂat R-module and I is an ideal in R then I ⊗R M ∼= IM by
i ⊗m 7→im.
Proof. The inclusion I →R is injective. Applying ⊗RM to this makes an injective R-linear
map I ⊗RM →R⊗RM since M is ﬂat, and composing with the isomorphism R⊗RM ∼= M
where r ⊗m 7→rm makes the injective map I ⊗R M →M where i ⊗m 7→im. The image
is IM, so I ⊗R M ∼= IM as R-modules with the desired eﬀect on elementary tensors.
□
To say an R-module N is not ﬂat means there is some example of an injective linear map
M
ϕ
−−→M′ whose induced linear map N ⊗R M
1⊗ϕ
−−−−→N ⊗R M′ is not injective.
Example 3.7. For a nonzero torsion abelian group A, the natural map Z ,→Q is injective
but if we apply A⊗Z we get the map A →0, which is not injective, so A is not a ﬂat
Z-module. This includes nonzero ﬁnite abelian groups and the inﬁnite abelian group Q/Z.
4Any two nonzero elements of K are R-linearly dependent, so if K were a free R-module then it would
have a basis of size 1: K = Rx for some x ∈K. Therefore x2 = rx for some r ∈R, so x = r ∈R, which
implies K ⊂R, so K = R.

<!-- page 12 -->
12
KEITH CONRAD
Remark 3.8. Since Q/Z is not ﬂat as a Z-module, for a homomorphism of abelian groups
G
f
−−→G′ the kernel of Q/Z ⊗Z G
1⊗f
−−−−→Q/Z ⊗Z G′ need not be Q/Z ⊗ker f but could be
larger. Therefore it is not easy to determine the kernel of a group homomorphism after base
extension by Q/Z. Failure to take this into account created a gap in a proof of a widely
used theorem in knot theory. See [1, §8.3].
Example 3.9. If R is a domain with fraction ﬁeld K, any nonzero torsion R-module T
(meaning every element of T is killed by a nonzero element of R) is not a ﬂat R-module
since tensoring the inclusion R ,→K with T produces the R-linear map T →0, which is
not injective. In particular, the quotient module K/R is not a ﬂat R-module. The previous
example is the special case R = Z: Q/Z is not a ﬂat Z-module.
Theorem 3.10. If N is a ﬂat R-module and M
ϕ
−−→M′ is R-linear then the kernel of
N ⊗R M
1⊗ϕ
−−−−→N ⊗R M′ is N ⊗R ker ϕ, viewed as a submodule of N ⊗R M in a natural
way.
Proof. The diagram
ϕ(M)
i
#
M
m7→ϕ(m)
<
ϕ
/ M′
commutes, where i is the inclusion. Tensoring with N produces a commutative diagram
N ⊗R ϕ(M)
1⊗i
'
N ⊗R M
m⊗n7→m⊗ϕ(n)
7
1⊗ϕ
/ N ⊗R M′.
The map 1 ⊗i is injective since i is injective and N is ﬂat. Therefore the two maps out
of N ⊗R M above have the same kernel. The kernel of N ⊗R M −→N ⊗R ϕ(M) can be
computed by Corollary 2.22 to be the natural image of N ⊗R ker ϕ inside N ⊗R M, and we
can identify the image with N ⊗R ker ϕ since N is ﬂat.
□
Theorem 3.11. A tensor product of two ﬂat modules is ﬂat.
Proof. Let N and N′ be ﬂat. For any injective linear map M
ϕ
−−→M′, we want to show the
induced linear map (N ⊗R N′) ⊗R M
1⊗ϕ
−−−−→(N ⊗R N′) ⊗M′ is injective.
Since N′ is ﬂat, N′ ⊗R M
1⊗ϕ
−−−−→N′ ⊗R M′ is injective. Tensoring now with N, N ⊗R
(N′ ⊗R M)
1⊗(1⊗ϕ)
−−−−−−−→N ⊗R (N′ ⊗R M′) is injective since N is ﬂat. The diagram
N ⊗R (N′ ⊗R M) 
1⊗(1⊗ϕ)
/

N ⊗R (N′ ⊗M′)

(N ⊗R N′) ⊗R M
1⊗ϕ
/ (N ⊗R N′) ⊗M′
commutes, where the vertical maps are the natural isomorphisms, so the bottom map is
injective. Thus N ⊗R N′ is ﬂat.
□

<!-- page 13 -->
TENSOR PRODUCTS II
13
Theorem 3.12. Let M
ϕ
−−→M′ and N
ψ
−−→N′ be injective linear maps.
If the four
modules are all ﬂat then M ⊗R N
ϕ⊗ψ
−−−−→M′ ⊗R N′ is injective. More precisely, if M and
N′ are ﬂat, or M′ and N are ﬂat, then ϕ ⊗ψ is injective.
The precise hypotheses (M and N′ ﬂat, or M′ and N ﬂat) can be remembered using
dotted lines in the diagram below; if both modules connected by one of the dotted lines are
ﬂat, then ϕ ⊗ψ is injective.
M
ϕ
/ M′
N
ψ
/ N′
Proof. The trick is to break up the linear map ϕ ⊗ψ into a composite of linear maps ϕ ⊗1
and 1 ⊗ψ in the following commutative diagram.
M ⊗R N′
ϕ⊗1
'
M ⊗R N
1⊗ψ
8
ϕ⊗ψ
/ M′ ⊗R N′
Both ϕ ⊗1 and 1 ⊗ψ are injective since N′ and M are ﬂat, so their composite ϕ ⊗ψ
is injective. Alternatively, we can write ϕ ⊗ψ as a composite ﬁtting in the commutative
diagram
M′ ⊗R N
1⊗ψ
'
M ⊗R N
ϕ⊗1
8
ϕ⊗ψ
/ M′ ⊗R N′
and the two diagonal maps are injective from ﬂatness of N and M′, so ϕ⊗ψ is injective.
□
Corollary 3.13. Let M1, . . . , Mk, N1, . . . , Nk be ﬂat R-modules and ϕi : Mi →Ni be injec-
tive linear maps. Then the linear map
ϕ1 ⊗· · · ⊗ϕk : M1 ⊗R · · · ⊗R Mk →N1 ⊗· · · ⊗Nk
is injective. In particular, if ϕ: M →N is an injective linear map of ﬂat modules then the
tensor powers ϕ⊗k : M⊗k →N⊗k are injective for all k ≥1.
Proof. We argue by induction on k. For k = 1 there is nothing to show. Suppose k ≥2 and
ϕ1 ⊗· · · ⊗ϕk−1 is injective. Then break up ϕ1 ⊗· · · ⊗ϕk into the composite
(N1 ⊗R · · · ⊗R Nk−1) ⊗R Mk
1⊗ϕk
*
M1 ⊗R · · · ⊗R Mk−1 ⊗R Mk
(ϕ1⊗···⊗ϕk−1)⊗1
3
ϕ1⊗···⊗ϕk
/ N1 ⊗R · · · ⊗R Nk.
The ﬁrst diagonal map is injective because Mk is ﬂat, and the second diagonal map is
injective because N1 ⊗R · · · ⊗R Nk−1 is ﬂat (Theorem 3.11 and induction).
□
Corollary 3.14. If M and N are free R-modules and ϕ: M →N is an injective linear
map, any tensor power ϕ⊗k : M⊗k →N⊗k is injective.

<!-- page 14 -->
14
KEITH CONRAD
Proof. Free modules are ﬂat by Theorem 3.2.
□
Note the free modules in Corollary 3.14 are completely arbitrary. We make no assump-
tions about ﬁnite bases.
Corollary 3.14 is not a special case of Theorem 2.18 because a free submodule of a free
module need not be a direct summand (e.g., 2Z is not a direct summand of Z).
Corollary 3.15. If M is a free module and {m1, . . . , md} is a ﬁnite linearly independent
subset then for any k ≤d the dk elementary tensors
(3.1)
mi1 ⊗· · · ⊗mik where i1, . . . , ik ∈{1, 2, . . . , d}
are linearly independent in M⊗k.
Proof. There is an embedding Rd ,→M by Pd
i=1 riei 7→Pd
i=1 rimi. Since Rd and M are
free, the kth tensor power (Rd)⊗k →M⊗k is injective. This map sends the basis
ei1 ⊗· · · ⊗eik
of (Rd)⊗k, where i1, . . . , ik ∈{1, 2, . . . , d}, to the elementary tensors in (3.1), so they are
linearly independent in M⊗k
□
Corollary 3.15 is not saying the elementary tensors in (3.1) can be extended to a basis of
M⊗k, just as m1, . . . , md usually can’t be extended to a basis of M.
4. Tensor Products of Linear Maps and Base Extension
Fix a ring homomorphism R
f
−−→S. Every S-module becomes an R-module by restriction
of scalars, and every R-module M has a base extension S ⊗R M, which is an S-module. In
part I we saw S ⊗R M has a universal mapping property among all S-modules: an R-linear
map from M to any S-module “extends” uniquely to an S-linear map from S ⊗R M to the
S-module. We discuss in this section an arguably more important role for base extension:
it turns an R-linear map M
ϕ
−−→M′ between two R-modules into an S-linear map between
S-modules. Tensoring M
ϕ
−−→M′ with S gives us an R-linear map S ⊗R M
1⊗ϕ
−−−−→S ⊗R M′
that is in fact S-linear: (1 ⊗ϕ)(st) = s(1 ⊗ϕ)(t) for all s ∈S and t ∈S ⊗R M. Since
both sides are additive in t, to prove 1 ⊗ϕ is S-linear it suﬃces to consider the case when
t = s′ ⊗m is an elementary tensor. Then
(1 ⊗ϕ)(s(s′ ⊗m)) = (1 ⊗ϕ)(ss′ ⊗m) = ss′ ⊗ϕ(m) = s(s′ ⊗ϕ(m)) = s(1 ⊗ϕ)(s′ ⊗m).
We will write the base extended linear map 1⊗ϕ as ϕS to make the S-dependence clearer,
so
ϕS : S ⊗R M →S ⊗R M′ by ϕS(s ⊗m) = s ⊗ϕ(m).
Since 1 ⊗idM = idS⊗RM and (1 ⊗ϕ) ◦(1 ⊗ϕ′) = 1 ⊗(ϕ ◦ϕ′), we have (idM)S = idS⊗RM
and (ϕ ◦ϕ′)S = ϕS ◦ϕ′
S. That means the process of creating S-modules and S-linear maps
out of R-modules and R-linear maps is functorial.
If an R-linear map M
ϕ
−−→M′ is an isomorphism or is surjective then so is S ⊗R M
ϕS
−−−→
S ⊗R M′ (Theorems 2.11 and 2.12). But if ϕ is injective then ϕS need not be injective.
(Examples 2.13, 2.14, and 2.15, which all have S as a ﬁeld).
Theorem 4.1. Let R be a nonzero commutative ring. If Rm ∼= Rn as R-modules then
m = n. If there is a linear surjection Rm ↠Rn then m ≥n.

<!-- page 15 -->
TENSOR PRODUCTS II
15
Proof. Pick a maximal ideal m in R. Tensoring R-linear maps Rm ∼= Rn or Rm ↠Rn
with R/m produces R/m-linear maps (R/m)m ∼= (R/m)n or (R/m)m ↠(R/m)n. Taking
dimensions over the ﬁeld R/m implies m = n or m ≥n, respectively.
□
We can’t extend this method of proof to show a linear injection Rm ,→Rn forces m ≤n
because injectivity is not generally preserved under base extension. We will return to this
later when we meet exterior powers.
Theorem 4.2. Let R be a PID and M be a ﬁnitely generated R-module. Writing
M ∼= Rd ⊕R/(a1) ⊕· · · ⊕R/(ak),
where a1 | · · · | ak, the integer d equals dimK(K ⊗R M), where K is the fraction ﬁeld of R.
Therefore d is uniquely determined by M.
Proof. Tensoring the displayed R-module isomorphism by K gives a K-vector space iso-
morphism K ⊗R M ∼= Kd since K ⊗R (R/(ai)) = 0. Thus d = dimK(K ⊗R M).
□
Example 4.3. Let A = ( a b
c d ) ∈M2(R). Regarding A as a linear map R2 →R2, its base
extension AS : S ⊗R R2 →S ⊗R R2 is S-linear and S ⊗R R2 ∼= S2 as S-modules.
Let {e1, e2} be the standard basis of R2. An S-basis for S ⊗R R2 is {1⊗e1, 1⊗e2}. Using
this basis, we can compute a matrix for AS:
AS(1 ⊗e1) = 1 ⊗A(e1) = 1 ⊗(ae1 + ce2) = a(1 ⊗e1) + c(1 ⊗e2)
and
AS(1 ⊗e2) = 1 ⊗A(e2) = 1 ⊗(be1 + de2) = b(1 ⊗e1) + d(1 ⊗e2).
Therefore the matrix for AS is ( a b
c d ) ∈M2(S). (Strictly speaking, we should have entries
f(a), f(b), and so on.)
The next theorem says base extension doesn’t change matrix representations, as in the
previous example.
Theorem 4.4. Let M and M′ be nonzero ﬁnite-free R-modules and M
ϕ
−−→M′ be an
R-linear map. For any bases {ej} and {e′
i} of M and M′, the matrix for the S-linear map
S ⊗R M
ϕS
−−−→S ⊗R M′ with respect to the bases {1 ⊗ej} and {1 ⊗e′
i} equals the matrix for
ϕ with respect to {ej} and {e′
i}.
Proof. Say ϕ(ej) = P
i aije′
i, so the matrix of ϕ is (aij). Then
ϕS(1 ⊗ej) = 1 ⊗ϕ(ej) = 1 ⊗
X
i
aijei =
X
i
aij(1 ⊗ei),
so the matrix of ϕS is also (aij).
□
Example 4.5. Any n × n real matrix acts on Rn, and its base extension to C acts on
C ⊗R Rn ∼= Cn as the same matrix. An n × n integral matrix acts on Zn and its base
extension to Z/mZ acts on Z/mZ ⊗Z Zn ∼= (Z/mZ)n as the same matrix reduced mod m.
Theorem 4.6. Let M and M′ be R-modules. There is a unique S-linear map
S ⊗R HomR(M, M′) →HomS(S ⊗R M, S ⊗R M′)
sending s ⊗ϕ to the function sϕS : t 7→sϕS(t) and it is an isomorphism if M and M′ are
ﬁnite free R-modules. In particular, using M′ = M, there is a unique S-linear map
S ⊗R (M∨R) →(S ⊗R M)∨S

<!-- page 16 -->
16
KEITH CONRAD
where s ⊗ϕ 7→sϕS on elementary tensors, and it is an isomorphism if M is a ﬁnite-free
R-module.
The point of this theorem in the ﬁnite-free case is that it says base extension on linear
maps accounts (through S-linear combinations) for all S-linear maps between base extended
R-modules. This doesn’t mean every S-linear map is a base extension, which would be like
saying every tensor is an elementary tensor rather than just a sum of them.
Proof. The function S × HomR(M, M′) →HomS(S ⊗R M, S ⊗R M′) where (s, ϕ) 7→sϕS is
R-bilinear (check!), so there is a unique R-linear map
S ⊗R HomR(M, M′)
L
−−→HomS(S ⊗R M, S ⊗R M′)
such that L(s⊗ϕ) = sϕS. The map L is S-linear (check!). If M′ = R and we identify S⊗RR
with S as S-modules by multiplication, then L becomes an S-linear map S ⊗R (M∨R) →
(S ⊗R M)∨S.
Now suppose M and M′ are both ﬁnite free. We want to show L is an isomorphism. If
M or M′ is 0 it is clear, so we may take them both to be nonzero with respective R-bases
{ei} and {e′
j}, say. Then S-bases of S ⊗R M and S ⊗R M′ are {1 ⊗ei} and {1 ⊗e′
j}. An
R-basis of HomR(M, M′) is the functions ϕij sending ei to e′
j and other basis vectors ek of
M to 0. An S-basis of S ⊗R HomR(M, M′) is the tensors {1 ⊗ϕij}, and
L(1 ⊗ϕij)(1 ⊗ei) = (ϕij)S(1 ⊗ei) = (1 ⊗ϕij)(1 ⊗ei) = 1 ⊗ϕij(ei) = 1 ⊗e′
j
while L(1 ⊗ϕij)(1 ⊗ek) = 0 for k ̸= i. That means L sends a basis to a basis, so L is an
isomorphism.
□
Example 4.7. Taking R = R, S = C, M = Rn, and M′ = Rm, the theorem says
C ⊗R Mm,n(R) ∼= Mm,n(C) as complex vector spaces by sending the elementary tensor
z ⊗A for z ∈C and A ∈Mm,n(R) to the matrix zA. In particular, C⊗R Mn(R) ∼= Mn(C).
Example 4.8. Let R = Z/p2Z and S = R/pR as rings. Then S is an R-module by using
the natural reduction map R →S. Let M be the R-module S (an additive group of order
p). Note S is not a free R-module: pS = 0 and p ̸= 0 in R.
We have S ⊗R M = S ⊗R S ∼= S as S-modules.5 The natural linear map
(4.1)
S ⊗R (M∨R) →(S ⊗R M)∨S
has image 0: check that each ϕ in M∨R = HomR(R/pR, R) has values in pR, so the image
of 1 ⊗ϕ on the right side of (4.1) has values in pS, which is 0. The right side of (4.1) is not
0 since HomS(S, S) ∼= S, so (4.1) isn’t an isomorphism.
In Corollary 3.14 we saw the tensor powers of an injective linear map between free
modules over any commutative ring are all injective. Using base extension, we can drop the
requirement that the target module be free provided we are working over a domain.
Theorem 4.9. Let R be a domain and ϕ: M ,→N be an injective linear map where M is
free. Then ϕ⊗k : M⊗k →N⊗k is injective for any k ≥1.
5More generally, R/I ⊗R R/I ∼= R/I as R-modules and then also as R/I-modules where R/I scales
elementary tensors x ⊗y in R/I ⊗R R/I on the left (a(x ⊗y) = ax ⊗y).

<!-- page 17 -->
TENSOR PRODUCTS II
17
Proof. We have a commutative diagram
M⊗k

ϕ⊗k
/ N⊗k

K ⊗R M⊗k

1⊗(ϕ⊗k)
/ K ⊗R N⊗k

(K ⊗R M)⊗k
(1⊗ϕ)⊗k
/ (K ⊗R N)⊗k
where the top vertical maps are the natural ones (t 7→1 ⊗t) and the bottom vertical maps
are the base extension isomorphisms. (Tensor powers along the bottom are over K while
those on the ﬁrst and second rows are over R.) From commutativity, to show ϕ⊗k along
the top is injective it suﬃces to show the composite map along the left side and the bottom
is injective. The K-linear map map K ⊗R M
1⊗ϕ
−−−−→K ⊗R N is injective since K is a
ﬂat R-module, and therefore the map along the bottom is injective (tensor products of
injective linear maps of vector spaces are injective). The bottom vertical map on the left
is an isomorphism. The top vertical map on the left is injective since M⊗k is free and thus
torsion-free (R is a domain).
□
This theorem may not be true if M isn’t free. Look at Example 2.16.
5. Vector Spaces
Because all (nonzero) vector spaces have bases, the results we have discussed for modules
assume a simpler form when we are working with vector spaces. We will review what we
have done in the setting of vector spaces and then discuss some further special properties
of this case.
Let K be a ﬁeld. Tensor products of K-vector spaces involve no unexpected collapsing: if
V and W are nonzero K-vector spaces then V ⊗KW is nonzero and in fact dimK(V ⊗KW) =
dimK(V ) dimK(W) in the sense of cardinal numbers.
For any K-linear maps V
ϕ
−−→V ′ and W
ψ
−−→W ′, we have the tensor product linear
map V ⊗K W
ϕ⊗ψ
−−−−→V ′ ⊗K W ′ that sends v ⊗w to ϕ(v) ⊗ψ(w). When V
ϕ
−−→V ′ and
W
ψ
−−→W ′ are isomorphisms or surjective, so is V ⊗K W
ϕ⊗ψ
−−−−→V ′ ⊗K W ′ (Theorems
2.11 and 2.12). Moreover, because all K-vector spaces are free a tensor product of injective
K-linear maps is injective (Theorem 3.2).
Example 5.1. If V
ϕ
−−→W is an injective K-linear map and U is any K-vector space, the
K-linear map U ⊗K V
1⊗ϕ
−−−−→U ⊗K W is injective.
Example 5.2. A tensor product of subspaces “is” a subspace: if V ⊂V ′ and W ⊂W ′ the
natural linear map V ⊗K W →V ′ ⊗K W ′ is injective.
Because of this last example, we can treat a tensor product of subspaces as a subspace
of the tensor product. For example, if V
ϕ
−−→V ′ and W
ψ
−−→W ′ are linear then ϕ(V ) ⊂V ′
and ψ(W) ⊂W ′, so we can regard ϕ(V ) ⊗K ψ(W) as a subspace of V ′ ⊗K W ′, which we
couldn’t do with modules in general. The following result gives us some practice with this
viewpoint.

<!-- page 18 -->
18
KEITH CONRAD
Theorem 5.3. Let V ⊂V ′ and W ⊂W ′ where V ′ and W ′ are nonzero. Then V ⊗K W =
V ′ ⊗K W ′ if and only if V = V ′ and W = W ′.
Proof. Since V ⊗K W is inside both V ⊗K W ′ and V ′ ⊗K W, which are inside V ′ ⊗K W ′,
by reasons of symmetry it suﬃces to assume V ⊊V ′ and show V ⊗K W ′ ⊊V ′ ⊗K W ′.
Since V is a proper subspace of V ′, there is a linear functional ϕ: V ′ →K that vanishes
on V and is not identically 0 on V ′, so ϕ(v′
0) = 1 for some v′
0 ∈V ′. Pick nonzero ψ ∈W ′∨,
and say ψ(w′
0) = 1. Then the linear function V ′ ⊗K W ′ →K where v′ ⊗w′ 7→ϕ(v′)ψ(w′)
vanishes on all of V ⊗K W ′ by checking on elementary tensors but its value on v′
0 ⊗w′
0 is
1. Therefore v′
0 ⊗w′
0 ̸∈V ⊗K W ′, so V ⊗K W ′ ⊊V ′ ⊗K W ′.
□
When V and W are ﬁnite-dimensional, the K-linear map
(5.1)
HomK(V, V ′) ⊗K HomK(W, W ′) →HomK(V ⊗K W, V ′ ⊗K W ′)
sending the elementary tensor ϕ ⊗ψ to the linear map denoted ϕ ⊗ψ is an isomorphism
(Theorem 2.5). So the two possible meanings of ϕ⊗ψ (elementary tensor in a tensor product
of Hom-spaces or linear map on a tensor product of vector spaces) really match up. Taking
V ′ = K and W ′ = K in (5.1) and identifying K ⊗K K with K by multiplication, (5.1) says
V ∨⊗K W ∨∼= (V ⊗K W)∨using the obvious way of making a tensor ϕ ⊗ψ in V ∨⊗K W ∨
act on V ⊗K W, namely through multiplication of the values: (ϕ ⊗ψ)(v ⊗w) = ϕ(v)ψ(w).
By induction on the numbers of terms,
V ∨
1 ⊗K · · · ⊗K V ∨
k ∼= (V1 ⊗K · · · ⊗K Vk)∨
when the Vi’s are ﬁnite-dimensional. Here an elementary tensor ϕ1 ⊗· · · ⊗ϕk ∈Nk
i=1 V ∨
i
acts on an elementary tensor v1 ⊗· · · ⊗vk ∈Nk
i=1 Vi with value ϕ1(v1) · · · ϕk(vk) ∈K. In
particular,
(V ∨)⊗k ∼= (V ⊗k)∨
when V is ﬁnite-dimensional.
Let’s turn now to base extensions to larger ﬁelds. When L/K is any ﬁeld extension,6 base
extension turns K-vector spaces into L-vector spaces (V ⇝L ⊗K V ) and K-linear maps
into L-linear maps (ϕ ⇝ϕL := 1 ⊗ϕ). Provided V and W are ﬁnite-dimensional over K,
base extension of linear maps V −→W accounts for all the linear maps between L ⊗K V
and L ⊗K W using L-linear combinations, in the sense that the natural L-linear map
(5.2)
L ⊗K HomK(V, W) ∼= HomL(L ⊗K V, L ⊗K W)
is an isomorphism (Theorem 4.6). When we choose K-bases for V and W and use the
corresponding L-bases for L ⊗K V and L ⊗K W, the matrix representations of a K-linear
map V →W and its base extension by L are the same (Theorem 4.4). Taking W = K, the
natural L-linear map
(5.3)
L ⊗K V ∨∼= (L ⊗K V )∨
is an isomorphism for ﬁnite-dimensional V , using K-duals on the left and L-duals on the
right.7
6We allow inﬁnite or even non-algebraic extensions, such as R/Q.
7If we drop ﬁnite-dimensionality assumptions, (5.1), (5.2), and (5.3) are all still injective but generally
not surjective.

<!-- page 19 -->
TENSOR PRODUCTS II
19
Remark 5.4. We don’t really need L to be a ﬁeld; K-vector spaces are free and therefore
their base extensions to modules over any commutative ring containing K will be free
as modules over the larger ring.
For example, the characteristic polynomial of a linear
operator V
ϕ
−−→V could be deﬁned in a coordinate-free way using base extension of V from
K to K[T]: the characteristic polynomial of ϕ is the determinant of the linear operator
T ⊗idV −ϕK[T] : K[T] ⊗K V −→K[T] ⊗K V since det(T ⊗idV −ϕK[T]) = det(TIn −A),
where A is a matrix representation of ϕ.
We will make no ﬁnite-dimensionality assumptions in the rest of this section.
The next theorem tells us the image and kernel of a tensor product of linear maps of
vector spaces, with no surjectivity hypotheses as in Theorem 2.19.
Theorem 5.5. Let V1
ϕ1
−−−→W1 and V2
ϕ2
−−−→W2 be linear. Then
ker(ϕ1 ⊗ϕ2) = ker ϕ1 ⊗K V2 + V1 ⊗K ker ϕ2,
Im(ϕ1 ⊗ϕ2) = ϕ1(V1) ⊗K ϕ2(V2).
In particular, if V1 and V2 are nonzero then ϕ1 ⊗ϕ2 is injective if and only if ϕ1 and ϕ2
are injective, and if W1 and W2 are nonzero then ϕ1 ⊗ϕ2 is surjective if and only if ϕ1 and
ϕ2 are surjective.
Here we use the fact that in vector spaces a tensor product of subspaces is naturally a
subspace of the tensor product: ker ϕ1 ⊗K V2 can be identiﬁed with its image in V1 ⊗K V2
and ϕ1(V1)⊗K ϕ2(V2) can be identiﬁed with its image in W1⊗K W2 under the natural maps.
Unlike vector spaces, for modules injectivity of ϕ1 and ϕ2 doesn’t imply injectivity of
ϕ1 ⊗ϕ2 (Example 2.16), injectivity of ϕ1 ⊗ϕ2 doesn’t imply injectivity of ϕ1 and ϕ2 (tensor
id : Z/2Z →Z/2Z and projection Z/2Z ⊕Z/3Z →Z/2Z ⊕Z/3Z to the ﬁrst component),
and surjectivity of ϕ1 ⊗ϕ2 doesn’t imply surjectivity of ϕ1 and ϕ2 (Example 2.1).
Proof. First we handle the image of ϕ1 ⊗ϕ2. The diagrams
ϕ1(V1)
i1
#
ϕ2(V2)
i2
#
V1
v17→ϕ1(v1)
<
ϕ1
/ W1
V2
v27→ϕ2(v2)
<
ϕ2
/ W2
commute, with i1 and i2 being injections, so the composite diagram
ϕ1(V1) ⊗K ϕ2(V2)
i1⊗i2
(
V1 ⊗K V2
v1⊗v27→ϕ1(v1)⊗ϕ2(v2)
6
ϕ1⊗ϕ2
/ W1 ⊗K W2
commutes. As i1 ⊗i2 is injective, both maps out of V1 ⊗K V2 have the same kernel. The
kernel of the map V1 ⊗K V2 −→ϕ1(V1) ⊗K ϕ2(V2) can be computed by Theorem 2.19 to be
ker ϕ1 ⊗K V2 +V1 ⊗K ker ϕ2, where we identify tensor products of subspaces with a subspace
of the tensor product.
If ϕ1 ⊗ϕ2 is injective then its kernel is 0, so 0 = ker ϕ1 ⊗K V2 + V1 ⊗K ker ϕ2 from the
kernel formula. Therefore the subspaces ker ϕ1 ⊗K V2 and V1 ⊗K ker ϕ2 both vanish, so
ker ϕ1 and ker ϕ2 must vanish (because V2 and V1 are nonzero, respectively). Conversely,
if ϕ1 and ϕ2 are injective then we already knew ϕ1 ⊗ϕ2 is injective, but the formula for
ker(ϕ1 ⊗ϕ2) also shows us this kernel is 0.

<!-- page 20 -->
20
KEITH CONRAD
If ϕ1⊗ϕ2 is surjective then the formula for its image shows ϕ1(V1)⊗Kϕ2(V2) = W1⊗KW2,
so ϕ1(V1) = W1 and ϕ2(V2) = W2 by Theorem 5.3 (here we need W1 and W2 nonzero).
Conversely, if ϕ1 and ϕ2 are surjective then so is ϕ1⊗ϕ2 since that’s true for all modules.
□
Corollary 5.6. Let V ⊂V ′ and W ⊂W ′. Then
(V ′ ⊗K W ′)/(V ⊗K W ′ + V ′ ⊗K W) ∼= (V ′/V ) ⊗K (W ′/W).
Proof. Tensor the natural projections V ′
π1
−−−→V ′/V and W ′
π2
−−−→W ′/W to get a linear
map V ′ ⊗K W ′
π1⊗π2
−−−−−→(V ′/V ) ⊗K (W ′/W) that is onto with ker(π1 ⊗π2) = V ⊗K W ′ +
V ′ ⊗K W by Theorem 5.5.
□
Remark 5.7. It is usually false that (V ′ ⊗K W ′)/(V ⊗K W) ∼= (V ′/V ) ⊗K (W ′/W) since
V ⊗K W is usually too small to be the kernel of V ′ ⊗K W ′ →(V ′/V ) ⊗K (W ′/W)8. This
is a distinction between tensor products and direct sums, where (V ′ ⊕W ′)/(V ⊕W) ∼=
(V ′/V ) ⊕(W ′/W).
Corollary 5.8. Let V
ϕ
−−→W be a linear map and U be a K-vector space. The linear map
U ⊗K V
1⊗ϕ
−−−−→U ⊗K W has kernel and image
(5.4)
ker(1 ⊗ϕ) = U ⊗K ker ϕ and
Im(1 ⊗ϕ) = U ⊗K ϕ(V ).
In particular, for nonzero U the map ϕ is injective or surjective if and only if 1 ⊗ϕ has
that property.
Proof. This is immediate from Theorem 5.5 since we’re using the identity map on U.
□
Example 5.9. Let V
ϕ
−−→W be a linear map and L/K be a ﬁeld extension. The base
extension L ⊗K V
ϕL
−−−→L ⊗K W has kernel and image
ker(ϕL) = L ⊗K ker ϕ,
Im(ϕL) = L ⊗K Im(ϕ).
The map ϕ is injective if and only if ϕL is injective and ϕ is surjective if and only if ϕL is
surjective.
Let’s formulate this in the language of matrices. If V and W are ﬁnite-dimensional then
ϕ can be written as a matrix with entries in K once we pick bases of V and W. Then
ϕL has the same matrix representation relative to the corresponding bases of L ⊗K V and
L ⊗K W. Since the base extension of a free module to another ring doesn’t change the size
of a basis, dimL(L ⊗K Im(ϕ)) = dimK Im(ϕ) and dimL(L ⊗K ker(ϕ)) = dimK ker(ϕ). That
means ϕ and ϕL have the same rank and the same nullity: the rank and nullity of a matrix
in Mm×n(K) do not change when it is viewed in Mm×n(L) for any ﬁeld extension L/K.
In the rest of this section we will look at tensor products of many vector spaces at once.
Lemma 5.10. For v ∈V with v ̸= 0, there is ϕ ∈V ∨such that ϕ(v) = 1.
Proof. The set {v} is linearly independent, so it extends to a basis {vi}i∈I of V . Let v = vi0
in this indexing. Deﬁne ϕ: V →K by
ϕ
 X
i
civi
!
= ci0.
Then ϕ ∈V ∨and ϕ(v) = ϕ(vi0) = 1.
□
8Exception: V ′ = V and W = 0, or W ′ = W and V = 0.

<!-- page 21 -->
TENSOR PRODUCTS II
21
Theorem 5.11. Let V1, . . . , Vk be K-vector spaces and vi ∈Vi. Then v1 ⊗· · · ⊗vk = 0 in
V1 ⊗K · · · ⊗K Vk if and only if some vi is 0.
Proof. The direction (⇐) is clear. To prove (⇒), we show the contrapositive: if every vi
is nonzero then v1 ⊗· · · ⊗vk ̸= 0. By Lemma 5.10, for i = 1, . . . , k there is ϕi ∈V ∨
i
with
ϕi(vi) = 1. Then ϕ1 ⊗· · · ⊗ϕk is a linear map V1 ⊗K · · · ⊗K Vk →K having the eﬀect
v1 ⊗· · · ⊗vk 7→ϕ1(v1) · · · ϕk(vk) = 1 ̸= 0,
so v1 ⊗· · · ⊗vk ̸= 0.
□
Corollary 5.12. Let ϕi : Vi →Wi be linear maps between K-vector spaces for 1 ≤i ≤k.
Then the linear map ϕ1 ⊗· · · ⊗ϕk : V1 ⊗K · · · ⊗K Vk →W1 ⊗K · · · ⊗K Wk is O if and only
if some ϕi is O.
Proof. For (⇐), if some ϕi is O then (ϕ1⊗· · ·⊗ϕk)(v1⊗· · ·⊗vk) = ϕ1(v1)⊗· · ·⊗ϕk(vk) = 0
since ϕi(vi) = 0. Therefore ϕ1 ⊗· · · ⊗ϕk vanishes on all elementary tensors, so it vanishes
on V1 ⊗K · · · ⊗K Vk, so ϕ1 ⊗· · · ⊗ϕk = O.
To prove (⇒), we show the contrapositive: if every ϕi is nonzero then ϕ1 ⊗· · · ⊗ϕk ̸= O.
Since ϕi ̸= O, we can ﬁnd some vi in Vi with ϕi(vi) ̸= 0 in Wi. Then ϕ1 ⊗· · · ⊗ϕk sends
v1⊗· · ·⊗vk to ϕ1(v1)⊗· · ·⊗ϕk(vk). Since each ϕi(vi) is nonzero in Wi, the elementary tensor
ϕ1(v1) ⊗· · · ⊗ϕk(vk) is nonzero in W1 ⊗K · · · ⊗K Wk by Theorem 5.11. Thus ϕ1 ⊗· · · ⊗ϕk
takes a nonzero value, so it is not the zero map.
□
Corollary 5.13. If R is a domain and M and N are R-modules, for non-torsion x in M
and y in N, x ⊗y is non-torsion in M ⊗R N.
Proof. Let K be the fraction ﬁeld of R. The torsion elements of M ⊗R N are precisely the
elements that go to 0 under the map M ⊗R N →K ⊗R (M ⊗R N) sending t to 1 ⊗t. We
want to show 1 ⊗(x ⊗y) ̸= 0.
The natural K-vector space isomorphism K ⊗R (M ⊗R N) ∼= (K ⊗R M) ⊗K (K ⊗R N)
identiﬁes 1 ⊗(x ⊗y) with (1 ⊗x) ⊗(1 ⊗y).
Since x and y are non-torsion in M and
N, 1 ⊗x ̸= 0 in K ⊗R M and 1 ⊗y ̸= 0 in K ⊗R N. An elementary tensor of nonzero
vectors in two K-vector spaces is nonzero (Theorem 5.11), so (1 ⊗x) ⊗(1 ⊗y) ̸= 0 in
(K ⊗R M) ⊗K (K ⊗R N). Therefore 1 ⊗(x ⊗y) ̸= 0 in K ⊗R (M ⊗R N), which is what we
wanted to show.
□
Remark 5.14. If M and N are torsion-free, Corollary 5.13 is not saying M ⊗R N is
torsion-free. It only says all (nonzero) elementary tensors have no torsion. There could be
non-elementary tensors with torsion, as we saw at the end of Example 2.16.
In Theorem 5.11 we saw an elementary tensor in a tensor product of vector spaces is
0 only under the obvious condition that one of the vectors appearing in the tensor is 0.
We now show two nonzero elementary tensors in vector spaces are equal only under the
“obvious” circumstances.
Theorem 5.15. Let V1, . . . , Vk be K-vector spaces. Pick pairs of nonzero vectors vi, v′
i in
Vi for i = 1, . . . , k. Then v1 ⊗· · · ⊗vk = v′
1 ⊗· · · ⊗v′
k in V1 ⊗K · · · ⊗K Vk if and only if there
are nonzero constants c1, . . . , ck in K such that vi = civ′
i and c1 · · · ck = 1.
Proof. If vi = civ′
i for all i and c1 · · · ck = 1 then v1 ⊗· · · ⊗vk = c1v′
1 ⊗· · · ⊗ckv′
k =
(c1 · · · ck)v′
1 ⊗· · · ⊗v′
k = v′
1 ⊗· · · ⊗v′
k.
Now we want to go the other way. It is clear for k = 1, so we may take k ≥2.

<!-- page 22 -->
22
KEITH CONRAD
By Theorem 5.11, v1⊗· · ·⊗vk is not 0 since each vi is not 0. Fix ϕi ∈V ∨
i for 1 ≤i ≤k−1
such that ϕi(vi) = 1. (Such ϕi exist since v1, . . . , vk−1 are nonzero vectors.) For arbitrary
ϕ ∈V ∨
k , let hϕ = ϕ1 ⊗· · · ⊗ϕk−1 ⊗ϕ, so hϕ(v1 ⊗· · · ⊗vk−1 ⊗vk) = ϕ(vk). Also
hϕ(v1 ⊗· · · ⊗vk−1 ⊗vk) = hϕ(v′
1 ⊗· · · ⊗v′
k−1 ⊗v′
k) = ϕ1(v′
1) · · · ϕk−1(v′
k−1)ϕ(v′
k) = ϕ(ckv′
k),
where ck := ϕ1(v′
1) · · · ϕk−1(v′
k−1) ∈K. So we have
ϕ(vk) = ϕ(ckv′
k)
for arbitrary ϕ ∈V ∨
k . Therefore ϕ(vk −ckv′
k) = 0 for all ϕ ∈V ∨
k , so vk −ckv′
k = 0, which
says vk = ckv′
k.
In the same way, for every i = 1, 2, . . . , k there is ci in K such that vi = civ′
i. Then
v1⊗· · ·⊗vk = c1v′
1⊗· · ·⊗ckv′
k = (c1 · · · ck)(v′
1⊗· · ·⊗v′
k). Since v1⊗· · ·⊗vk = v′
1⊗· · ·⊗v′
k ̸= 0,
we get c1 · · · ck = 1.
□
Theorem 5.15 has an interesting interpretation in terms of subspaces. An elementary
tensor v1 ⊗· · · ⊗vk does not determine all the individual vectors vi, since they can each be
scaled by a nonzero element ci of K without changing v1 ⊗· · · ⊗vk as long as the product
of the ci’s is 1. That’s the easier direction of Theorem 5.15. What the harder direction
of Theorem 5.15 tells us is that such scaling is the only way we can change the vi’s while
keeping the elementary tensor v1 ⊗· · · ⊗vk unchanged. In other words, v1 ⊗· · · ⊗vk does
not determine the vi’s but it does determine the 1-dimensional subspaces Kvi in Vi. And
since scaling v1 ⊗· · · ⊗vk is the same as scaling one of the vi’s (any of them), the subspace
K(v1 ⊗· · · ⊗vk) determines the subspaces Kvi (the converse is much easier).
In quantum mechanics, the quantum states of a system are described by the nonzero
vectors in a complex Hilbert space H where a (nonzero) scalar multiple of a vector in
H determines the same quantum state as the original vector (this condition is motivated
by physics), so the states of a quantum system can be described by the 1-dimensional
subspaces of H instead of by the individual (nonzero) elements of H.9 When two quantum
systems with corresponding Hilbert spaces H1 and H2 are combined, the Hilbert space
for the combined system is the (completed) tensor product H1 ⊗C H2. In H1 ⊗C H2, a 1-
dimensional subspace C(v1⊗v2) spanned by an elementary tensor determines the individual
subspaces Cv1 and Cv2 of H1 and H2 by Theorem 5.15, but most 1-dimensional subspaces of
H1 ⊗C H2 are not spanned by an elementary tensor and thus do not “come from” particular
1-dimensional subspaces of H1 and H2. The non-elementary tensors in H1 ⊗C H2 describe
states that are called “entangled” and Schr¨odinger [4, p. 555] called this phenomenon “the
characteristic trait of quantum mechanics, the one that enforces its entire departure from
classical lines of thought [. . .] the best possible knowledge of a whole does not necessarily
include the best possible knowledge of all its parts.” He did not use the terminology of
tensor products, but you can see it at work in what he did say [4, p. 556], where his Hilbert
spaces are L2-spaces of functions on some Rn: “Let x and y stand for all the coordinates of
the ﬁrst and second systems respectively and Ψ(x, y) [stand for the] state of the composed
system [. . .]. What constitutes the entanglement is that Ψ is not a product of a function of
x and a function of y.” That is analogous to most elements of R[x, y] not being of the form
f(x)g(y), e.g., x3y −xy2 + 7 is an “entangled” polynomial.
Here is the analogue of Theorem 5.15 for linear maps (compare to Corollary 5.12).
9A nonzero vector in H, viewed as a quantum state, is often scaled to have length 1, but this still allows
ambiguity up to scaling by a complex number eiθ of absolute value 1, with θ called a phase-factor.

<!-- page 23 -->
TENSOR PRODUCTS II
23
Theorem 5.16. Let ϕi : Vi →Wi and ϕ′
i : Vi →Wi be nonzero linear maps between K-
vector spaces for 1 ≤i ≤k. Then ϕ1 ⊗· · · ⊗ϕk = ϕ′
1 ⊗· · · ⊗ϕ′
k as linear maps V1 ⊗K
· · · ⊗K Vk →W1 ⊗K · · · ⊗K Wk if and only if there are c1, . . . , ck in K such that ϕi = ciϕ′
i
and c1c2 · · · ck = 1.
Proof. Since each ϕi : Vi →Wi is not identically 0, for i = 1, . . . , k −1 there is vi ∈Vi such
that ϕi(vi) ̸= 0 in Wi. Then there is fi ∈W ∨
i such that fi(ϕi(vi)) = 1.
Pick any v ∈Vk and f ∈W ∨
k . Set hf = f1 ⊗· · · ⊗fk−1 ⊗f ∈(W1 ⊗K · · · ⊗K Wk)∨where
hf(w1 ⊗· · · ⊗wk−1 ⊗wk) = f1(w1) · · · fk−1(wk−1)f(wk).
Then
hf((ϕ1 ⊗· · · ⊗ϕk−1 ⊗ϕk)(v1 ⊗· · · ⊗vk−1 ⊗v)) = f1(ϕ1(v1)) · · · fk−1(ϕk−1(vk−1))f(ϕk(v)),
and since fi(ϕi(vi)) = 1 for i ̸= k, the value is f(ϕk(v)). Also
hf((ϕ′
1 ⊗· · · ⊗ϕ′
k−1 ⊗ϕ′
k)(v1 ⊗· · · ⊗vk−1 ⊗v)) = f1(ϕ′
1(v1)) · · · fk−1(ϕ′
k−1(vk−1))f(ϕ′
k(v)).
Set ck = f1(ϕ′
1(v1)) · · · fk−1(ϕ′
k−1(vk−1)), so the value is ckf(ϕ′
k(v)) = f(ckϕ′
k(v)). Since
ϕ1 ⊗· · · ⊗ϕk−1 ⊗ϕk = ϕ′
1 ⊗· · · ⊗ϕ′
k−1 ⊗ϕ′
k,
f(ϕk(v)) = f(ckϕ′
k(v)).
This holds for all f ∈W ∨
k , so ϕk(v) = ckϕ′
k(v). This holds for all v ∈Vk, so ϕk = ckϕ′
k as
linear maps Vk →Wk.
In a similar way, there is ci ∈K such that ϕi = ciϕ′
i for all i, so
ϕ1 ⊗· · · ⊗ϕk = (c1ϕ′
1) ⊗· · · ⊗(ckϕ′
k)
= (c1 · · · ck)ϕ′
1 ⊗· · · ⊗ϕ′
k
= (c1 · · · ck)ϕ1 ⊗· · · ⊗ϕk,
so c1 · · · ck = 1 since ϕ1 ⊗· · · ⊗ϕk ̸= O.
□
Remark 5.17. When the Vi’s and Wi’s are ﬁnite-dimensional, the tensor product of linear
maps between them can be identiﬁed with elementary tensors in the tensor product of
the vector spaces of linear maps (Theorem 2.5), so in this special case Theorem 5.16 is a
special case of Theorem 5.15. Theorem 5.16 does not assume the vector spaces are ﬁnite-
dimensional.
When we have k copies of a vector space V , any permutation σ ∈Sk acts on the direct
sum V ⊕k by permuting the coordinates:
(v1, . . . , vk) 7→(vσ−1(1), . . . , vσ−1(k)).
The inverse on σ is needed to get a genuine left group action (Check!). Here is a similar
action of Sk on the kth tensor power.
Corollary 5.18. For σ ∈Sk, there is a linear map Pσ : V ⊗k →V ⊗k such that
v1 ⊗· · · ⊗vk 7→vσ−1(1) ⊗· · · ⊗vσ−1(k)
on elementary tensors. Then Pσ ◦Pτ = Pστ for σ and τ in Sk.10
When dimK(V ) > 1, Pσ = Pτ if and only if σ = τ. In particular, Pσ is the identity map
if and only if σ is the identity permutation.
10If we used vσ(i) instead of vσ−1(i) in the deﬁnition of Pσ then we’d have Pσ ◦Pτ = Pτσ.

<!-- page 24 -->
24
KEITH CONRAD
Proof. The function V × · · · × V →V ⊗k given by
(v1, . . . , vk) 7→vσ−1(1) ⊗· · · ⊗vσ−1(k)
is multilinear, so the universal mapping property of tensor products gives us a linear map
Pσ with the indicated eﬀect on elementary tensors. It is clear that P1 is the identity map.
For any σ and τ in Sk, Pσ ◦Pτ = Pστ by checking equality of both sides at all elementary
tensors in V ⊗k. Therefore the injectivity of σ 7→Pσ is reduced to showing if Pσ is the
identity map on V ⊗k then σ is the identity permutation.
We prove the contrapositive. Suppose σ is not the identity permutation, so σ(i) = j ̸= i
for some i and j. Choose v1, . . . , vk ∈V all nonzero such that vi and vj are not on the
same line. (Here we use dimK V > 1.) If Pσ(v1 ⊗· · · ⊗vk) = v1 ⊗· · · ⊗vk then vj ∈Kvi by
Theorem 5.15, which is not so.
□
The linear maps Pσ provide an action of Sk on V ⊗k by linear transformations. We usually
write σ(t) for Pσ(t). Not only does Sk acts on V ⊗k but also the group GL(V ) acts on V ⊗k
via tensor powers of linear maps:
g(v1 ⊗· · · ⊗vk) := g⊗k(v1 ⊗· · · ⊗vk) = gv1 ⊗· · · ⊗gvk
on elementary tensors. These actions of the groups Sk and GL(V ) on V ⊗k commute with
each other: Pσ(g(t)) = g(Pσ(t)) for all t ∈V ⊗k. To verify that, since both sides are additive
in t, it suﬃces to check it on elementary tensors, which is left to the reader. This commuting
action of Sk and GL(V ) on V ⊗k leads to Schur–Weyl duality in representation theory.
A tensor t ∈V ⊗k satisfying Pσ(t) = t for all σ ∈Sk are called symmetric, and if
Pσ(t) = (sign σ)t for all σ ∈Sk we call t anti-symmetric or skew-symmetric. An example of
a symmetric tensor in V ⊗k is P
σ∈Sk Pσ(t) for any t ∈V ⊗k. For elementary t, this sum is
X
σ∈Sk
Pσ(v1⊗v2⊗· · ·⊗vk) =
X
σ∈Sk
vσ−1(1)⊗vσ−1(2)⊗· · ·⊗vσ−1(k) =
X
σ∈Sk
vσ(1)⊗vσ(2)⊗· · ·⊗vσ(k).
An example of an anti-symmetric tensor in V ⊗k is P
σ∈Sk(sign σ)vσ(1) ⊗vσ(2) ⊗· · · ⊗vσ(k).
Both symmetric and anti-symmetric tensors occur in physics. See Table 1.
Area
Name of Tensor
Symmetry
Mechanics
Stress
Symmetric
Strain
Symmetric
Elasticity
Symmetric
Moment of Inertia
Symmetric
Electromagnetism
Electromagnetic
Anti-symmetric
Polarization
Symmetric
Relativity
Metric
Symmetric
Stress-Energy
Symmetric
Table 1. Some tensors in physics.
The set of all symmetric tensors and the set of all anti-symmetric tensors in V ⊗k each
form subspaces. If K does not have characteristic 2, every tensor in V ⊗2 is a unique sum
of a symmetric and anti-symmetric tensor:
t = t + P(12)(t)
2
+ t −P(12)(t)
2
.

<!-- page 25 -->
TENSOR PRODUCTS II
25
(The map P(12) is the ﬂip automorphism of V ⊗2 sending v ⊗w to w ⊗v.) Concretely, if
{e1, . . . , en} is a basis of V then each tensor in V ⊗2 has the form P
i,j cijei ⊗ej, and it’s
symmetric if and only if cij = cji for all i and j, while it’s anti-symmetric if and only if
cij = −cji for all i and j (in particular, cii = 0 for all i).
For k > 2, the symmetric and anti-symmetric tensors in V ⊗k do not span the whole space.
There are additional subspaces of tensors in V ⊗k connected to the representation theory of
the group GL(V ). The appearance of representations of GL(V ) inside tensor powers of V
is an important role for tensor powers in algebra.
6. Tensor Contraction
Continuing the theme of the previous section, let V be a ﬁnite-dimensional vector space
over a ﬁeld K. The evaluation pairing V ×V ∨→K, where (v, ϕ) 7→ϕ(v), is K-bilinear and
thus induces a K-linear map c: V ⊗V ∨→K called a contraction11, where c(v ⊗ϕ) = ϕ(v).
This map is independent of the choice of a basis, but it’s worth seeing how this looks in a
basis. We adopt the notation of physicists and geometers for bases and coeﬃcients in V and
V ∨, as in the section about tensors in physics in the ﬁrst handout about tensor products:
for a basis {e1, . . . , en} of V , let {e1, . . . , en} be its dual basis in V ∨, with elements of V
written as P
i viei and elements of V ∨written as P
i viei. (Here vi, vi ∈K.) The space
V ⊗V ∨has basis {ei ⊗ej}i,j and c(ei ⊗ej) = ej(ei) = δij. For v ∈V and ew ∈V ∨, write
v = P
i viei and ew = P
j wjej, where vi, wj ∈K. Then
(6.1)
c(v ⊗ew) =
X
i,j
viwjej(ei) =
X
i
viwi.
The ﬁnal sum is independent of the basis used on V , since contraction comes from evaluating
V ∨on V and that does not depend on a choice of basis.
From the ﬁrst tensor product handout, V ⊗V ∨∼= HomK(V, V ) by
v ⊗ϕ 7→[w 7→ϕ(w)v]
on elementary tensors. This isomorphism converts contraction on V ⊗V ∨into a linear map
HomK(V, V ) →K that turns out to be the trace. Why? A tensor in V ⊗V ∨can be written
uniquely as a linear combination P
i,j T i
jei ⊗ej. The isomorphism V ⊗V ∨∼= HomK(V, V )
sends P
i,j T i
jei ⊗ej to the linear operator V →V that maps each ek to P
i,j T i
jej(ek)ei =
P
i,j T i
jδjkei = P
i T i
kei, so this linear operator V →V has matrix representation (T i
j) with
respect to the basis {ei}. The contraction of P
i,j T i
jei⊗ej is c(P
i,j T i
jei⊗ej) = P
i,j T i
jδij =
P
i T i
i , which is exactly the trace of the matrix (T i
j).
Contraction V ⊗V ∨→K generalizes to maps V ⊗k ⊗(V ∨)⊗ℓ→V ⊗(k−1) ⊗(V ∨)⊗(ℓ−1)
for k ≥1 and ℓ≥1 (recall V ⊗0 = K and (V ∨)⊗0 = K) that are linear and also called
contractions, as follows. For r ∈{1, . . . , k} and s ∈{1, . . . , ℓ}, the associated contraction
cr,s : V ⊗k ⊗(V ∨)⊗ℓ→V ⊗(k−1) ⊗(V ∨)⊗(ℓ−1) evaluates the rth tensorand in V ⊗k in the sth
11Here and elsewhere in this section, tensor products are always over K: ⊗= ⊗K.

<!-- page 26 -->
26
KEITH CONRAD
tensorand in (V ∨)⊗ℓ, leaving other tensorands untouched: on elementary tensors,
cr,s(v1 ⊗· · · ⊗vk ⊗ϕ1 ⊗· · · ⊗ϕℓ) = c(vr ⊗ϕs)
O
i̸=r
vi ⊗
O
j̸=s
ϕj
= ϕs(vr)
O
i̸=r
vi ⊗
O
j̸=s
ϕj.
How does cr,s look in a basis? For a basis {e1, . . . , en} of V and dual basis {e1, . . . , en} of
V ∨, a basis of V ⊗k ⊗(V ∨)⊗ℓis the nk+ℓelementary tensors ei1 ⊗· · · ⊗eik ⊗ej1 ⊗· · · ⊗ejℓ,
and
cr,s




X
i1,...,ik
j1,...,jℓ
T i1...ik
j1...jℓei1 ⊗· · · ⊗eik ⊗ej1 ⊗· · · ⊗ejℓ



=
X
i1,...,jℓ
ir,jsmissing
n
X
m=1
T i1···m···ik
j1···m···jℓ
O
a̸=r
eia⊗
O
b̸=s
ejb,
where the m appears in the rth slot of the superscript and the sth slot of the subscript of
the coeﬃcient on the right. The outer sum on the right initially runs over all sets of indices
and the coeﬃcient is multiplied by the numerical factor eis(eir), which is nonzero only for
is = ir (call this common value m, and its runs from 1 to n), when the factor is 1.
The contraction cr,s depends on its domain V ⊗k ⊗(V ∨)⊗ℓ, not just r and s (which are at
most k and ℓ, respectively). For example, on V ⊗2 ⊗V ∨and V ⊗2 ⊗(V ∨)⊗2, the contraction
c2,1 on elementary tensors is v ⊗w ⊗ϕ 7→ϕ(w)v and v ⊗w ⊗ϕ ⊗ψ 7→ϕ(w)v ⊗ψ. Using
bases, the contraction c2,1 on V ⊗2 ⊗V ∨is
(6.2)
c2,1




X
i1,i2
j1
T i1i2
j1
ei1 ⊗ei2 ⊗ej1



=
X
i1,i2
j1
T i1i2
j1
ej1(ei2) ei1 =
X
i1
 X
m
T i1m
m
!
ei1
and the contraction c2,1 on V ⊗2 ⊗(V ∨)⊗2 is
(6.3)
c2,1




X
i1,i2
j1,j2
T i1i2
j1j2ei1 ⊗ei2 ⊗ej1 ⊗ej2



=
X
i1,j2
 X
m
T i1m
mj2
!
ei1 ⊗ej2.
Remark 6.1. In physics and engineering, tensors are often described just by components
(coordinates), with summing over the basis being understood: P
i T iei is written as T i and
P
i,j Tijei ⊗ej is written as Tij. That components have indices in the opposite position
(up vs. down) to basis vectors needs to be known to reconstruct the tensor from how its
components are written. Another convention, which is widely used in geometry as well, is
that summation signs within a component (due to contraction or to applying the metric –
see below) are omitted and an implicit summation running from 1 to the dimension of V
is intended for each index repeated as both a superscript and subscript. This is called the
Einstein summation convention. For example, the most basic contraction V ⊗V ∨→K,
where P
i,j T i
jei ⊗ej 7→P
i T i
i , is written in this convention as
T i
j 7→T i
i .

<!-- page 27 -->
TENSOR PRODUCTS II
27
The contractions c2,1 in (6.2) and (6.3), on V ⊗2 ⊗V ∨and V ⊗2 ⊗(V ∨)⊗2 respectively, are
denoted in the Einstein summation convention as
T i1i2
j1
7→T i1i2
i2
,
T i1i2
j1j2 7→T i1i2
i2j2 .
Contraction only makes sense when we combine V and V ∨. We can’t contract V and V
– it doesn’t make sense to evaluate elements of V on V . However, if we have a preferred
isomorphism g: V →V ∨of vector spaces then we can use g to turn V into V ∨. We have
V ⊗V ∼= V ⊗V ∨using id. ⊗g and we can contract the right side. So we can contract on
V ⊗V after all, provided we use an isomorphism g from V to V ∨and remember what g is.
Contraction on V ⊗V (using g) means the composite map
(6.4)
V ⊗V
id.⊗g
−−−→V ⊗V ∨
c
−−−→K.
This depends on the choice of g but not on a choice of basis of V .
There should be nothing special about using g in the second tensorand in (6.4). We want
(6.5)
V ⊗V
g⊗id.
−−−→V ∨⊗V −−−→K
to be the same overall mapping as (6.4), where the second mapping in (6.5) is induced by
evaluation of V ∨on V . The agreement of (6.4) and (6.5) means g(v)(w) = g(w)(v) for all
v and w in V . This means that if we regard g: V →V ∨as a bilinear map V × V →K
by (v, w) 7→g(v)(w) or (v, w) 7→g(w)(v) we want the same result: we want g to be
symmetric as a bilinear form on V . To check a given g is symmetric, it enough to check this
on a basis {e1, . . . , en} of V : g(ei)(ej) = g(ej)(ei) in K for all i and j. Set gij = g(ei)(ej), so
g(ei) =
X
j
gijej for all i and gij = gji for all i, j from 1 to n: the matrix (gij) is symmetric.
We can think of the isomorphism g: V →V ∨as a bilinear map V ×V →K in two ways:
either as (v, w) 7→g(v)(w) or as (v, w) 7→g(w)(v). The fact that g is an isomorphism is
equivalent to g as a bilinear form on V being nondegenerate and is also equivalent to the
matrix (gij) coming from any basis of V (gij = g(ei)(ej)) being invertible. In practice we
always assume g is symmetric and nondegenerate as a bilinear form on V .
Let’s write g and then the contraction on V ⊗V from (6.4) or (6.5) in coordinates. Pick
a basis {e1, . . . , en} of V and dual basis {e1, . . . , en} of V ∨. For v = P
i viei in V , how does
g(v) look in the dual basis of V ∨? That gij = g(ei)(ej) means g(ei) = P
j gijej, so
g(v) = g
 X
i
viei
!
=
X
i
vig(ei) =
X
i
vi

X
j
gijej

=
X
j
 X
i
gijvi
!
ej.
Thus g(P
i viei) = P
j vjej, where vj =
X
i
gijvi =
X
i
gjivi
for all j (recall gij = gji).
The passage from the numbers {vi} (components of v) to the numbers {vj} (components
of g(v)) by multiplying each vi by gij and summing over all i is called lowering an index.
It is the coordinate version (using a basis of V and its dual basis in V ∨) of going from v in
V to g(v) in V ∨, which depends on g but not on the choice of basis of V .

<!-- page 28 -->
28
KEITH CONRAD
For x = P
i xiei and y = P
i yiei in V ⊗2, (6.4) has the following eﬀect on the elementary
tensor x ⊗y:
x ⊗y 7→x ⊗g(y)
=
 X
i
xiei
!
⊗

X
j
yjej


where yj =
X
k
gkjyk =
X
k
gjkyk
c7→
X
i
xiyi by (6.1).
Unwrapping the deﬁnition of yi terms of gij and yj (for j = 1, . . . , n),
X
i
xiyi =
X
i,j
gijxiyj.
This is usually not P
i xiyi unless gij = δij for all i and j. More generally, the contraction of
the tensor T = P
i,j T ijei⊗ej in V ⊗2 using g is the scalar P
i,j gijT ij in K. This contraction
is independent of the basis {e1, . . . , en} of V but depends on the isomorphism g: V →V ∨.
Example 6.2. Let g be an isomorphism V →V ∨that is symmetric (and nondegenerate)
as a bilinear form V × V →K. Applying g to the sth tensorand of V ⊗k, where k ≥2 and
1 ≤s ≤k, turns the tensor P
i1,...,ik T i1...ikei1 ⊗· · · ⊗eik into
X
i1,...,ik
T i1...ikei1 ⊗· · · ⊗g(eis) ⊗· · · ⊗eik =
X
i1,...,ik
T i1...ikei1 ⊗· · · ⊗
 X
i
giisei
!
|
{z
}
sth tensorand
⊗· · · ⊗eik
and contracting the rth and sth tensorands12 where r ̸= s gives us the following tensor in
V ⊗(k−2):
X
i1,...,ik
ir,is missing

X
ir,is
girisT i1...ik

ei1 ⊗· · · ⊗eik
|
{z
}
ir,is missing
.
Example 6.3. Let g be an isomorphism V →V ∨that is symmetric (and nondegenerate)
as a bilinear form V × V →K. For a rank 3 tensor T in V ⊗2 ⊗V ∨, we have the rank
3 tensors U = (g ⊗1 ⊗1)(T) ∈V ∨⊗V ⊗V ∨(not standard form with all V ’s ﬁrst) and
U′ = (g ⊗g ⊗1)(T) ∈(V ∨)⊗3. What do U and U′ look like in terms of how T looks?
Using a basis {e1, . . . , en} for V and dual basis {e1, . . . , en} for V ∨, in V ⊗2 ⊗V ∨let
T =
X
i1,i2
j1
T i1i2
j1
ei1 ⊗ei2 ⊗ej1.
Passing from V ⊗2 ⊗V ∨= V ⊗V ⊗V ∨to V ∨⊗V ⊗V ∨by g ⊗1 ⊗1 only aﬀects the ﬁrst
tensorand:
U = (g ⊗1 ⊗1)(T) =
X
i2
j1,j2
Ui2
j2j1ej2 ⊗ei2 ⊗ej1,
where Ui2
j2j1 =
X
i1
gi1j2T i1i2
j1
.
12While V ⊗(s−1) ⊗(V ∨) ⊗V ⊗(k−s) is not in standard form, the meaning of contraction using the rth
tensorand V and the sth tensorand V ∨should be obvious to the reader.

<!-- page 29 -->
TENSOR PRODUCTS II
29
Passing from V ⊗2⊗V ∨= V ⊗V ⊗V ∨to (V ∨)⊗3 by g⊗g⊗1 aﬀects the ﬁrst two tensorands:
U′ = (g ⊗g ⊗1)(T) =
X
j1,j2,j3
Uj2j3j1ej2 ⊗ej3 ⊗ej1,
where Uj2j3j1 =
X
i1,i2
gi1j2gi2j3T i1i2
j1
.
Remark 6.4. Putting the Einstein summation convention (Remark 6.1) to work, the con-
traction V ⊗V ∨→K sends viei⊗wjej to viwi, which is the same as vjwj and is independent
of the basis since it is simply evaluating V ∨on V . Using an isomorphism g: V →V ∨that is
symmetric (and nondegenerate) as a bilinear form V ×V →K, any v = viei in V turns into
g(v) = viei in V ∨where vi = gkivk = gikvk since (gij) is symmetric, and the contraction
V ⊗V →K that depends on g has the eﬀect xiei ⊗yjej 7→xiyi = xjyj = gijxiyj (remember
gij = gji!) and more generally T ijei ⊗ej 7→gijT ij. The contraction on V ⊗2 depends on g
but not on the basis of V . Contraction on V ⊗k, for k ≥2, using the rth and sth tensorand
is a linear map to V ⊗(k−2) with the eﬀect T i1...ikei1 ⊗· · · ⊗eik 7→girisT i1···ik ei1 ⊗· · · ⊗eik
|
{z
}
ir,is missing
.
For T i1i2
j1
in V ⊗V ⊗V ∨, if we lower the ﬁrst upper index we get gi1j2T i1i2
j1
in V ∨⊗V ⊗V ∨
and if we lower both upper indices then we get gi1j2gi2j3T i1i2
j1
in V ∨⊗V ∨⊗V ∨.
Contraction lets us map V ⊗k ⊗(V ∨)⊗ℓto V ⊗(k−1) ⊗(V ∨)⊗(ℓ−1) by combining a choice
of V and V ∨in V ⊗k ⊗(V ∨)⊗ℓusing evaluation to get scalars. We can use an isomorphism
g: V →V ∨to change any V in V ⊗k ⊗(V ∨)⊗ℓinto V ∨(in practice g is symmetric when
viewed as a bilinear form) and thus contract any two diﬀerent V tensorands (the result
depends on g). To contract two diﬀerent V ∨tensorands, use the inverse g−1 : V ∨→V ,
which as a bilinear form on V ∨is symmetric: writing g−1(ei) =
X
j
gijej , (gij) is the
inverse matrix to (gij) and is symmetric since (gij) is. We have g−1(P
i viei) = P
j vjej,
where vj =
X
i
gijvi . The passage from {vi} to {vj} is multiplying vi by gij and summing
over all i. It is called raising an index and depends on g: this is the coordinate version
(using a basis of V and its dual basis in V ∨) of going from elements of V ∨to elements of V
by g−1.13 Using g or g−1 in enough places lets us turn the mixed tensors of V ⊗k ⊗(V ∨)⊗ℓ
into pure tensors in V ⊗(k+ℓ) or (V ∨)⊗(k+ℓ).
The operations of raising/lowering an index and contraction do not depend on a choice
of basis of V . That is because raising/lowering an index is just applying a choice of isomor-
phism from V to V ∨or vice versa and contraction is based on the natural bilnear evaluation
map V ∨× V →K thought of as a linear map V ∨⊗V →K or V ⊗V ∨→K, and none
of these depend on bases. For physics or engineering students who don’t know about dual
spaces, the independence of basis for these operations is veriﬁed by tedious calculations
(if they care at all) and they check raising/lowering indices and contractions send tensors
to tensors by checking the output of such operations satisﬁes tensor transformation rules,
so it is a tensor. At least that it is how books for such students handle the tasks and it
might look like a miracle to those who can’t think about concepts without bases: what do
raising/lowering an index and multiplying by gij mean if you don’t know what V ∨is?
13Raising or lowering indices describes what happens to components in a basis. The basis undergoes the
opposite change (lowering or raising its indices).

<!-- page 30 -->
30
KEITH CONRAD
When K = R, a nondegenerate symmetric bilinear form g on V is called a metric on
V . This generalizes the dot product on Rn, so intuitively it is more like squared distance
than distance itself. (A metric in the sense of metric spaces is always nonnnegative, but g
as a bilinear form might be positive and negative.) There is an integer p from 0 to n and a
basis {e1, . . . , en} of V in which g(P
i xiei, P
j yjej) = Pp
i=1 xiyi −Pn
i=p+1 xiyi. For p = 0
or n one sum on the right is empty and that’s treated as 0. Here are two important special
cases.
• The case p = n means g(v, v) ≥0 with equality if and only if v = 0. Such g are
called positive-deﬁnite or inner products. They are used in Riemannian geometry.
• The cases p = 1 or p = n−1 are important in Lorentzian geometry, and in relativity
when n = 4.
7. Tensor Product of R-Algebras
Our tensor product isomorphisms of modules often involve rings, e.g., C ⊗R Mn(R) ∼=
Mn(C) as C-vector spaces (Example 4.7). Now we will show how to turn the tensor product
of two rings into a ring. Then we will revisit a number of previous module isomorphisms
where the modules are also rings and ﬁnd that the isomorphism holds at the level of rings.
Because we want to be able to say C ⊗R Mn(R) ∼= Mn(C) as rings, not just as vector
spaces (over R or C), and matrix rings are noncommutative, we are going to allow our
R-modules to be possibly noncommutative rings. But R itself remains commutative!
Our rings will all be R-algebras. An R-algebra is an R-module A equipped with an R-
bilinear map A × A →A, called multiplication or product. Bilinearity of multiplication
includes distributive laws for multiplication over addition as well as the extra rule
(7.1)
r(ab) = (ra)b = a(rb)
for r ∈R and a and b in B, which says R-scaling commutes with multiplication in the
R-algebra. We also want 1 · a = a for a ∈A, where 1 is the identity element of R.
Examples of R-algebras include the matrix ring Mn(R), a quotient ring R/I, and the
polynomial ring R[X1, . . . , Xn]. We will assume, except in Example 7.5, that our R-algebras
have associative multiplication and a multiplicative identity, so they are genuinely rings
(perhaps not commutative) and being an R-algebra just means they have a little extra
structure related to scaling by R. When an R-algebra contains R, (7.1) is a special case of
associative multiplication in the algebra.
The diﬀerence between an R-algebra and a ring is exactly like that between an R-module
and an abelian group. An R-algebra is a ring on which we have a scaling operation by R
that behaves nicely with respect to the addition and multiplication in the R-algebra, in the
same way that an R-module is an abelian group on which we have a scaling operation by
R that behaves nicely with respect to the addition in the R-module. While Z-modules are
nothing other than abelian groups, Z-algebras in our lexicon are nothing other than rings
(possibly noncommutative).
Because of the universal mapping property of the tensor product, to give an R-bilinear
multiplication A × A →A in an R-algebra A is the same thing as giving an R-linear map
A ⊗R A →A. So we could deﬁne an R-algebra as an R-module A equipped with an R-
linear map A ⊗R A
m
−−→A, and declare the product of a and b in A to be ab := m(a ⊗b).

<!-- page 31 -->
TENSOR PRODUCTS II
31
Associativity of multiplication can be formulated in tensor language: the diagram
A ⊗R A ⊗R A
1⊗m
/
m⊗1

A ⊗R A
m

A ⊗R A
m
/ A
commutes.
Theorem 7.1. Let A and B be R-algebras. There is a unique multiplication on A ⊗R B
making it an R-algebra such that
(7.2)
(a ⊗b)(a′ ⊗b′) = aa′ ⊗bb′
for all elementary tensors. The multiplicative identity is 1 ⊗1.
Proof. If there is an R-algebra multiplication on A⊗R B satisfying (7.2) then multiplication
between any two tensors is determined:
k
X
i=1
ai ⊗bi ·
ℓ
X
j=1
a′
j ⊗b′
j =
X
i,j
(ai ⊗bi)(a′
j ⊗b′
j) =
X
i,j
aia′
j ⊗bib′
j.
So the R-algebra multiplication on A ⊗R B satisfying (7.2) is unique if it exists at all. Our
task now is to write down a multiplication on A ⊗R B satisfying (7.2).
One way to do this is to deﬁne what left multiplication by each elementary tensor a⊗b on
A ⊗R B should be, by introducing a suitable bilinear map and making it into a linear map.
But rather than proceed by this route, we’ll take advantage of various maps we already know
between tensor products. Writing down an associative R-bilinear multiplication on A ⊗R B
with identity 1 ⊗1 means writing down an R-linear map (A ⊗R B) ⊗R (A ⊗R B) →A ⊗R B
satisfying certain conditions, and that’s what we’re going to do.
Let A ⊗R A
mA
−−−→A and B ⊗R B
mB
−−−→B be the R-linear maps corresponding to
multiplication on A and on B. Their tensor product mA ⊗mB is an R-linear map from
(A⊗R A)⊗R (B ⊗R B) to A⊗R B. Using the commutativity and associativity isomorphisms
on tensor products, there are natural isomorphisms
(A ⊗R B) ⊗R (A ⊗R B) ∼= ((A ⊗R B) ⊗R A) ⊗R B
∼= (A ⊗R (B ⊗R A)) ⊗R B
∼= (A ⊗R (A ⊗R B)) ⊗R B
∼= ((A ⊗R A) ⊗R B) ⊗R B
∼= (A ⊗R A) ⊗R (B ⊗R B).
Tracking the eﬀect of these maps on (a ⊗b) ⊗(a′ ⊗b′),
(a ⊗b) ⊗(a′ ⊗b′) 7→((a ⊗b) ⊗a′) ⊗b′
7→(a ⊗(b ⊗a′)) ⊗b′
7→(a ⊗(a′ ⊗b)) ⊗b′
7→((a ⊗a′) ⊗b) ⊗b′
7→(a ⊗a′) ⊗(b ⊗b′).

<!-- page 32 -->
32
KEITH CONRAD
Composing these isomorphisms with mA⊗mB makes a map (A⊗RB)⊗R(A⊗RB) →A⊗RB
that is R-linear and has the eﬀect
(a ⊗b) ⊗(a′ ⊗b′) 7→(a ⊗a′) ⊗(b ⊗b′) 7→aa′ ⊗bb′,
where mA ⊗mB is used in the second step. This R-linear map (A ⊗R B) ⊗R (A ⊗R B) →
A ⊗R B pulls back to an R-bilinear map (A ⊗R B) × (A ⊗R B) →A ⊗R B with the eﬀect
(a ⊗b, a′ ⊗b′) 7→aa′ ⊗bb′ on pairs of elementary tensors, which is what we wanted for our
multiplication on A ⊗R B. This proves A ⊗R B has a multiplication satisfying (7.2).
To prove 1 ⊗1 is an identity and multiplication in A ⊗R B is associative, we want
(1 ⊗1)t = t,
t(1 ⊗1) = t,
(t1t2)t3 = t1(t2t3)
for general tensors t, t1, t2, and t3 in A ⊗R B. These identities are additive in each tensor
appearing on both sides, so verifying these equations reduces to the case that the tensors
are all elementary, and this case is left to the reader.
□
Corollary 7.2. If A and B are commutative R-algebras then A ⊗R B is a commutative
R-algebra.
Proof. We want to check tt′ = t′t for all t and t′ in A ⊗R B. Both sides are additive in t, so
it suﬃces to check the equation when t = a⊗b is an elementary tensor: (a⊗b)t′ ?= t′(a⊗b).
Both sides of this are additive in t′, so we are reduced further to the special case when
t′ = a′ ⊗b′ is also an elementary tensor: (a ⊗b)(a′ ⊗b′) ?= (a′ ⊗b′)(a ⊗b). The validity of
this is immediate from (7.2) since A and B are commutative.
□
Example 7.3. Let’s look at the ring C ⊗R C. It is 4-dimensional as a real vector space,
and its multiplication is determined from linearity by the products of its standard basis
1 ⊗1, 1 ⊗i, i ⊗1, and i ⊗i. The tensor 1 ⊗1 is the multiplicative identity, so we’ll look at
the products of the three other basis elements, and since multiplication is commutative we
only need one product per basis pair:
(1 ⊗i)2 = 1 ⊗(−1) = −(1 ⊗1), (1 ⊗i)(i ⊗1) = i ⊗i, (1 ⊗i)(i ⊗i) = i ⊗(−1) = −(i ⊗1),
(i ⊗1)2 = (−1) ⊗1 = −(1 ⊗1),
(i ⊗1)(i ⊗i) = (−1) ⊗i = −(1 ⊗i),
(i ⊗i)2 = 1 ⊗1.
Setting x = i⊗1 and y = 1⊗i, we have C⊗R C = R+Rx+Ry +Rxy, where (±x)2 = −1
and (±y)2 = −1. This commutative ring is not a ﬁeld (−1 can’t have more than two square
roots in a ﬁeld), and in fact it is “clearly” the product ring (R+Rx)×(R+Ry) ∼= C×C with
componentwise operations. (Warning: an isomorphism C⊗RC →C×C is not obtained by
z ⊗w 7→(z, w) since that is not well-deﬁned: (−z) ⊗(−w) = z ⊗w but (−z, −w) ̸= (z, w)
in general. We’ll see an explicit isomorphism in Example 7.19.)
Example 7.4. The tensor product R ⊗Q R is isomorphic to R as a Q-vector space for
the nonconstructive reason that they have the same (inﬁnite) dimension over Q. When we
compare R ⊗Q R to R as commutative rings, they look very diﬀerent: the tensor product
ring has zero divisors. The elementary tensors
√
2 ⊗1 and 1 ⊗
√
2 are linearly independent
over Q and square to 2(1 ⊗1), so
(
√
2 ⊗1 + 1 ⊗
√
2)(
√
2 ⊗1 −1 ⊗
√
2) = 2 ⊗1 −1 ⊗2 = 0
with neither factor on the left side being 0.

<!-- page 33 -->
TENSOR PRODUCTS II
33
Example 7.5. Let R3 have the cross product × as multiplication: vw := v × w. This
is bilinear with vv = v × v = 0 for all v in R3 and it’s assumed the reader has seen the
products among the diﬀerent basis vectors i, j, and k, e.g., i × j = k and i × k = −j.
Since the cross product has no identity and is not associative, the proof of Theorem
7.1 except for its last paragraph (which is about multiplicative identities and associativity)
works on R3 ⊗R R3: it admits a unique multiplication such that on elementary tensors
(v ⊗w)(v′ ⊗w′) = vv′ ⊗ww′ = (v × v′) ⊗(w × w′).
The cross product on R3 satisﬁes the Jacobi identity: for all u, v and w in R3,
u(vw) + v(wu) + w(uv) = u × (v × w) + v × (w × u) + w × (u × v) = 0.
Such an identity does not hold for the multiplication on R3⊗RR3: when t = i⊗j, t′ = i⊗k,
and t′′ = j ⊗k,
t(t′t′′) + t′(t′′t) + t′′(tt′) = i ⊗j((i ⊗k)(j ⊗k)) + i ⊗k((j ⊗k)(i ⊗j)) + j ⊗k((i ⊗j)(i ⊗k))
= (i ⊗j)(ij ⊗kk) + (i ⊗k)(ji ⊗kj) + (j ⊗k)(ii ⊗jk)
= (i ⊗j)(ij ⊗0) + (i ⊗k)(−k ⊗−i) + (j ⊗k)(0 ⊗jk)
= 0 + (i ⊗k)(k ⊗i) + 0
= ik ⊗ki
= −j ⊗j,
which is not 0. This shows the tensor product g ⊗g of a Lie algebra g with itself may not
be a Lie algebra using the multiplication naturally inherited from the Lie bracket on g.
A homomorphism of R-algebras is a function between R-algebras that is both R-linear
and a ring homomorphism. An isomorphism of R-algebras is a bijective R-algebra homo-
morphism. That is, an R-algebra isomorphism is simultaneously an R-module isomorphism
and a ring isomorphism. For example, the reduction map R[X] →R[X]/(X2 +X +1) is an
R-algebra homomorphism (it is R-linear and a ring homomorphism) and R[X]/(X2+1) ∼= C
as R-algebras by a + bX 7→a + bi: this function is not just a ring isomorphism, but also
R-linear.
For any R-algebras A and B, there is an R-algebra homomorphism A →A ⊗R B by
a 7→a ⊗1 (check!). The image of A in A ⊗R B might not be isomorphic to A. For instance,
in Z ⊗Z (Z/5Z) (which is isomorphic to Z/5Z by a ⊗(b mod 5) = ab mod 5), the image
of Z by a 7→a ⊗1 is isomorphic to Z/5Z. There is also an R-algebra homomorphism
B →A ⊗R B by b 7→1 ⊗b. Even when A and B are noncommutative, the images of A and
B in A ⊗R B commute: (a ⊗1)(1 ⊗b) = a ⊗b = (1 ⊗b)(a ⊗1). This is like groups G and
H commuting in G × H even if G and H are nonabelian.
It is worth contrasting the direct product A × B (componentwise addition and multipli-
cation, with r(a, b) = (ra, rb)) and the tensor product A ⊗R B, which are both R-algebras.
The direct product A × B is a ring structure on the R-module A ⊕B, which is usually
quite diﬀerent from A ⊗R B as an R-module. There are natural R-algebra homomorphisms
A × B
π1
−−−→A and A × B
π2
−−−→B by projection, while there are natural R-algebra homo-
morphisms A →A ⊗R B and B −→A ⊗R B in the other direction (out of A and B to the
tensor product rather than to A and B from the direct product). The projections out of the
direct product A × B to A and B are both surjective, but the maps to the tensor product
A ⊗R B from A and B need not be injective, e.g., Z →Z ⊗Z Z/5Z. The maps A →A ⊗R B
and B →A⊗R B are ring homomorphisms and the images are subrings, but although there

<!-- page 34 -->
34
KEITH CONRAD
are natural functions A →A × B and B →A × B given by a 7→(a, 0) and b 7→(0, b), these
are not ring homomorphisms and the images are ideals rather than subrings.
Example 7.6. We saw in Example 7.3 that C⊗RC ∼= C×C as R-algebras. How do R⊗QR
and R×R compare? They are not isomorphic as real vector spaces since dimR(R×R) = 2
while dimR(R ⊗Q R) = dimQ(R) = ∞. An R-algebra isomorphism would in particular be
an R-vector space isomorphism, so R ⊗Q R ̸∼= R × R as R-algebras. To show R ⊗Q R is
not isomorphic to R × R just as rings, we’ll count square roots of 1. In R × R there are
four square roots of 1, namely (±1, ±1) using independent choices of signs, but in R ⊗Q R
there are at least six square roots of 1:
±(1 ⊗1),
±1
2(
√
2 ⊗
√
2)
and
± 1
3(
√
3 ⊗
√
3).
These six tensors look diﬀerent from each other, but how do we know they really are
diﬀerent? The numbers 1,
√
2, and
√
3 are linearly independent over Q (why?), so any
elementary tensors formed from these numbers in R⊗Q R are linearly independent over Q.
This proves the six elementary tensors above are distinct.
We will see in Example 7.18 that R ⊗Q R has inﬁnitely many square roots of 1.
The R-algebras A × B and A ⊗R B have dual universal mapping properties. For any
R-algebra C and R-algebra homomorphisms C
ϕ
−−→A and C
ψ
−−→B, there is a unique
R-algebra homomorphism C −→A × B making the diagram
C
ϕ

ψ


A × B
π1
{
π2
#
A
B
commute. For any R-algebra C and R-algebra homomorphisms A
ϕ
−−→C and B
ψ
−−→C
such that the images of A and B in C commute (ϕ(a)ψ(b) = ψ(b)ϕ(a)), there is a unique
R-algebra homomorphism A ⊗R B −→C making the diagram
A
ϕ
%
a7→a⊗1
#
B
ψ
y
b7→1⊗b
{
A ⊗R B

C
commute.
A practical criterion for showing an R-linear map of R-algebras is an R-algebra homo-
morphism is as follows. If ϕ: A →B is an R-linear map of R-algebras and {ai} is a spanning
set for A as an R-module (that is, A = P
i Rai), then ϕ is multiplicative as long as it is so
on these module generators: ϕ(aiaj) = ϕ(ai)ϕ(aj) for all i and j. Indeed, if this equation

<!-- page 35 -->
TENSOR PRODUCTS II
35
holds then
ϕ

X
i
riai ·
X
j
r′
jaj

= ϕ

X
i,j
rir′
jaiaj


=
X
i,j
rir′
jϕ(aiaj)
=
X
i,j
rir′
jϕ(ai)ϕ(aj)
=
X
i
riϕ(ai)
X
j
r′
jϕ(aj)
= ϕ
 X
i
riai
!
ϕ

X
j
r′
jaj

.
This will let us bootstrap a lot of known R-module isomorphisms between tensor products
to R-algebra isomorphisms by checking the behavior only on products of elementary tensors
(and checking the multiplicative identity is preserved, which is always easy). We give some
concrete examples before stating some general theorems.
Example 7.7. For ideals I and J in R, there is an isomorphism ϕ: R/I ⊗R R/J −→
R/(I + J) of R-modules where ϕ(x ⊗y) = xy. Then ϕ(1 ⊗1) = 1 and
ϕ((x ⊗y)(x′ ⊗y′)) = ϕ(xx′ ⊗yy′) = xx′yy′ = xy x′y′ = ϕ(x ⊗y)ϕ(x′ ⊗y′).
So R/I ⊗R R/J ∼= R/(I + J) as R-algebras, not just as R-modules. In particular, the
additive isomorphism Z/aZ ⊗Z Z/bZ ∼= Z/(a, b)Z is in fact an isomorphism of rings.
Example 7.8. There is an R-module isomorphism ϕ: R[X] ⊗R R[Y ] −→R[X, Y ] where
ϕ(f(X) ⊗g(Y )) = f(X)g(Y ). Let’s show it’s an R-algebra isomorphism: ϕ(1 ⊗1) = 1 and
ϕ((f1(X) ⊗g1(Y ))(f2(X) ⊗g2(Y ))) = ϕ(f1(X)f2(X) ⊗g1(Y )g2(Y ))
= f1(X)f2(X)g1(Y )g2(Y )
= f1(X)g1(Y )f2(X)g2(Y )
= ϕ(f1(X) ⊗g1(Y ))ϕ(f2(X) ⊗g2(Y )),
so R[X] ⊗R R[Y ] ∼= R[X, Y ] as R-algebras, not just as R-modules. (It would have suﬃced
to check ϕ is multiplicative on pairs of monomial tensors Xi ⊗Y j.)
In a similar way, the natural R-module isomorphism R[X]⊗k ∼= R[X1, . . . , Xn], where the
indeterminate Xi on the right corresponds on the left to the tensor 1 ⊗· · · ⊗X ⊗· · · ⊗1
with X in the ith position, is an isomorphism of R-algebras.
Example 7.9. When R is a domain with fraction ﬁeld K, K ⊗R K ∼= K as R-modules by
x ⊗y 7→xy. This sends 1 ⊗1 to 1 and preserves multiplication on elementary tensors, so it
is an isomorphism of R-algebras.
Example 7.10. Let F be a ﬁeld. When x and y are independent indeterminates over F,
F[x] ⊗F F[y] ∼= F[x, y] as F-algebras by Example 7.8. It is natural to think that we should
also have F(x) ⊗F F(y) ∼= F(x, y) as F-algebras, but this is always false! Why should it be
false, and is there a concrete way to think about F(x) ⊗F F(y)?

<!-- page 36 -->
36
KEITH CONRAD
Every tensor t in F(x)⊗F F(y) is a ﬁnite sum P
i,j fi(x)⊗gj(y). We can give all the fi(x)’s
a common denominator and all the gj(y)’s a common denominator, say fi(x) = ai(x)/b(x)
and gj(y) = cj(y)/d(y) where ai(x) ∈F[x] and cj(y) ∈F[y]. Then
t =
X
i,j
ai(x)
b(x) ⊗F
cj(y)
d(y) =
 1
b(x) ⊗
1
d(y)
 X
i,j
ai(x) ⊗cj(y).
Since F[x]⊗F F[y] ∼= F[x, y] as F-algebras by multiplication, this suggests comparing t with
the rational function we get by multiplying terms in each elementary tensor, which leads to
P
i,j ai(x)cj(y)
b(x)d(y)
.
The numerator is a polynomial in x and y, and every polynomial in F[x, y] has that form
(all polynomials in x and y are sums of polynomials in x times polynomials in y). The
denominator, however, is quite special: it is a single polynomial in x times a single polyno-
mial in y. Most rational functions in F(x, y) don’t have such a denominator. For example,
1/(1 −xy) can’t be written to have a denominator of the form b(x)d(y) (proof?).
To show F(x) ⊗F F(y) is isomorphic as an F-algebra to the rational functions in F(x, y)
having a denominator in the factored form b(x)d(y), show that the multiplication mapping
F(x) ⊗F F(y) →F(x, y) given by f(x) ⊗g(y) 7→f(x)g(y) on elementary tensors is an
embedding of F-algebras.
That it is an F-algebra homomorphism follows by the same
argument used in Example 7.8. It is left to the reader to show the kernel is 0 from the
known fact that the multiplication mapping F[x] ⊗F F[y] →F[x, y] is injective. (Hint:
Justify the idea of clearing denominators.) Thus F(x)⊗F F(y) is an integral domain that is
not a ﬁeld, since its image in F(x, y) is not a ﬁeld: the image contains F[x, y] but is smaller
than F(x, y). Concretely, the fact that 1 −xy is the image of 1 ⊗1 −x ⊗y but 1/(1 −xy)
is not in the image shows 1 ⊗1 −x ⊗y is not invertible in F(x) ⊗F F(y). (In terms of
localizations, F(x) ⊗F F(y) is isomorphic as an F-algebra to the localization of F[x, y] at
the multiplicative set of all products b(x)d(y).)
Example 7.11. For any R-module M, there is an S-linear map
S ⊗R EndR(M) −→EndS(S ⊗R M)
where s ⊗ϕ 7→sϕS = s(1 ⊗ϕ). Both sides are S-algebras. Check this S-linear map is
an S-algebra map. When M is ﬁnite free this map is a bijection (chase bases), so it is an
S-algebra isomorphism. For other M it might not be an isomorphism.
As a concrete instance of this, when M = Rn we get S ⊗R Mn(R) ∼= Mn(S) as S-algebras,
not just as S-modules. In particular, C ⊗R Mn(R) ∼= Mn(C) as C-algebras.
Example 7.12. If I is an ideal in R and A is an R-algebra, R/I ⊗R A ∼= A/IA ﬁrst as R-
modules, then as R-algebras (the R-linear isomorphism is also multiplicative and preserves
identities), and ﬁnally as R/I-algebras since the isomorphism is R/I-linear too.
Theorem 7.13. Let A, B, and C be R-algebras. The standard R-module isomorphisms
A ⊗R B ∼= B ⊗R A,
A ⊗R (B × C) ∼= (A ⊗R B) × (A ⊗R C)
(A ⊗R B) ⊗R C ∼= A ⊗R (B ⊗R C).
are all R-algebra isomorphisms.

<!-- page 37 -->
TENSOR PRODUCTS II
37
The distributivity of ⊗over × suggests denoting the direct product of algebras as a direct
sum with ⊕.
Proof. Exercise. Note the direct product of two R-algebras is the direct sum as R-modules
with componentwise multiplication, so ﬁrst just treat the direct product as a direct sum.
□
Corollary 7.14. For R-algebras A and B, A ⊗R Bn ∼= (A ⊗R B)n as R-algebras.
Proof. Induct on n. Note Bn here means the n-fold product ring, not B⊗n.
□
We turn now to base extensions. Fix a homomorphism f : R →S of commutative rings.
We can restrict scalars from S-modules to R-modules and extend scalars from R-modules to
S-modules. What about between R-algebras and S-algebras? An example is the formation
of C ⊗R Mn(R), which ought to look like Mn(C) as rings (really, as C-algebras) and not
just as complex vector spaces.
If A is an S-algebra, then we make A into an R-module in the usual way by ra = f(r)a,
and this makes A into an R-algebra (restriction of scalars). More interesting is extension
of scalars. For this we need a lemma.
Lemma 7.15. If A, A′, B, and B′ are all R-algebras and A
ϕ
−−→A′ and B
ψ
−−→B′ are
R-algebra homomorphisms then the R-linear map A ⊗R B
ϕ⊗ψ
−−−−→A′ ⊗R B′ is an R-algebra
homomorphism.
Proof. Exercise.
□
Theorem 7.16. Let A be an R-algebra.
(1) The base extension S ⊗R A, which is both an R-algebra and an S-module, is an
S-algebra by its S-scaling.
(2) If A
ϕ
−−→B is an R-algebra homomorphism then S ⊗R A
1⊗ϕ
−−−−→S ⊗R B is an
S-algebra homomorphism.
Proof. 1) We just need to check multiplication in S ⊗R A commutes with S-scaling (not
just R-scaling): s(tt′) = (st)t′ = t(st′). Since all three expressions are additive in t and t′,
it suﬃces to check this when t and t′ are elementary tensors:
s((s1 ⊗a1)(s2 ⊗a2)) ?= (s(s1 ⊗a1))(s2 ⊗a2) ?= (s1 ⊗a1)(s(s2 ⊗a2)).
From the way S-scaling on S ⊗R A is deﬁned, all these products equal ss1s2 ⊗a1a2.
2) For an R-algebra homomorphism A
ϕ
−−→B, the base extension S⊗RA
1⊗ϕ
−−−−→S⊗RB is
S-linear and it is an R-algebra homomorphism by Lemma 7.15. Therefore it is an S-algebra
homomorphism.
□
We can also give A ⊗R S an S-algebra structure by S-scaling and the natural S-module
isomorphism S ⊗R A ∼= A ⊗R S is an S-algebra isomorphism.
Example 7.17. Let I be an ideal in R[X1, . . . , Xn]. Check the S-module isomorphism
S ⊗R R[X1, . . . , Xn]/I ∼= S[X1, . . . , Xn]/(I · S[X1, . . . , Xn]) from Corollary 2.25 is an S-
algebra isomorphism.
In one-variable, with I = (h(X)) a principal ideal in R[X],14 Example 7.17 gives us an
S-algebra isomorphism
S ⊗R R[X]/(h(X)) ∼= S[X]/(hf(X)),
14Not all ideals in R[X] have to be principal, but this is just an example.

<!-- page 38 -->
38
KEITH CONRAD
where hf(X) is the result of applying f : R →S to the coeﬃcients of h(X). (If f : Z →
Z/pZ is reduction mod p, for instance, then hf(X) = h(X) mod p.) This isomorphism is
particularly convenient, as it lets us compute a lot of tensor products of ﬁelds.
Example 7.18. Writing Q(
√
2) as Q[X]/(X2 −2) (as a Q-algebra), we have
R ⊗Q Q(
√
2) ∼= R ⊗Q Q[X]/(X2 −2) ∼= R[X]/(X2 −2) ∼= R × R
as R-algebras since X2 −2 factors into distinct linear polynomials in R[X], and
R ⊗Q Q(
3√
2) ∼= R ⊗Q Q[X]/(X3 −2) ∼= R[X]/(X3 −2) ∼= R × C
as R-algebras since X3 −2 has irreducible factors in R[X] of degree 1 and 2.
More generally, we have an R-algebra isomorphism
R ⊗Q Q(
n√
2) ∼= R[X]/(Xn −2).
The Q-linear embedding Q(
n√
2) ,→R extends to an R-linear embedding R ⊗Q Q(
n√
2) →
R ⊗Q R that is multiplicative (it suﬃces to check that on elementary tensors), so the ring
R ⊗Q R contains a subring isomorphic to R[X]/(Xn −2). When n is odd, Xn −2 has
one linear factor and (n −1)/2 quadratic irreducible factors in R[X], so R[X]/(Xn −2) ∼=
R×C(n−1)/2 as R-algebras. Therefore R[X]/(Xn−2) contains 21+(n−1)/2 = 2(n+1)/2 square
roots of 1. Letting n →∞shows R ⊗Q R contains inﬁnitely many square roots of 1.
Example 7.19. We revisit Example 7.3, using Example 7.17:
C ⊗R C ∼= C ⊗R (R[X]/(X2 + 1)) ∼= C[X]/(X2 + 1) = C[X]/(X −i)(X + i) ∼= C × C
as R-algebras.
Let’s make the R-algebra isomorphism C ⊗R C ∼= C × C explicit, as it is not z ⊗w 7→
(z, w). Tracing the eﬀect of the isomorphisms on elementary tensors,
z ⊗(a + bi) 7→z ⊗(a + bX) 7→za + zbX 7→(za + zbi, za + ab(−i)) = (z(a + bi), z(a −bi)),
so z ⊗w 7→(zw, zw). Thus 1 ⊗1 7→(1, 1), z ⊗1 7→(z, z), and 1 ⊗w 7→(w, w).
In these examples, a tensor product of ﬁelds is not a ﬁeld. But the tensor product of
ﬁelds can be a ﬁeld (besides the trivial case K ⊗K K ∼= K). Here is an example.
Example 7.20. We have
Q(
√
2) ⊗Q Q(
√
3) ∼= Q(
√
2) ⊗Q Q[X]/(X2 −3) ∼= Q(
√
2)[X]/(X2 −3),
which is a ﬁeld because X2 −3 is irreducible in Q(
√
2)[X].
Example 7.21. As an example of a tensor product involving a ﬁnite ﬁeld and a ring,
Z/5Z ⊗Z Z[i] ∼= Z/5Z ⊗Z Z[X]/(X2 + 1) ∼= (Z/5Z)[X]/(X2 + 1) ∼= Z/5Z × Z/5Z
since X2 + 1 = (X −2)(X −3) in (Z/5Z)[X].
A general discussion of tensor products of ﬁelds is in [3, Sect. 8.18].
Theorem 7.22. If A is R-algebra and B is an S-algebra, then the S-module structure on
the R-algebra A ⊗R B makes it an S-algebra, and
A ⊗R B ∼= (A ⊗R S) ⊗S B
as S-algebras sending a ⊗b to (a ⊗1) ⊗b.

<!-- page 39 -->
TENSOR PRODUCTS II
39
Proof. It is left as an exercise to check the S-module and R-algebra structure on A ⊗R B
make it an S-algebra. As for the isomorphism, from part I we know there is an S-module
isomorphism with the indicated eﬀect on elementary tensors. This function sends 1 ⊗1 to
(1 ⊗1) ⊗1, which are the multiplicative identities. It is left to the reader to check this
function is multiplicative on products of elementary tensors too.
□
Theorem 7.22 is particularly useful in ﬁeld theory. Consider two ﬁeld extensions L/K
and F/K with an intermediate ﬁeld K ⊂E ⊂L, as in the following diagram.
L
F
E
K
Then there is a ring isomorphism
F ⊗K L ∼= (F ⊗K E) ⊗E L
which is also an isomorphism as E-algebras, F-algebras (from the left factor) and L-algebras
(from the right factor).
Theorem 7.23. Let A and B be R-algebras. There is an S-algebra isomorphism
S ⊗R (A ⊗R B) →(S ⊗R A) ⊗S (S ⊗R B)
by s ⊗(a ⊗b) 7→s((1 ⊗a) ⊗(1 ⊗b)).
Proof. By part I, there is an S-module isomorphism with the indicated eﬀect on tensors of
the form s ⊗(a ⊗b). This function preserves multiplicative identities and is multiplicative
on such tensors (which span S ⊗R (A ⊗R B)), so it is an S-algebra isomorphism.
□
8. The Tensor Algebra of an R-module
Modules don’t usually have a multiplication operation.
That is, R-modules are not
usually R-algebras. However, there is a construction that turns an R-module M into the
generating set of an R-algebra in the “minimal” way possible. This R-algebra is the tensor
algebra of M, which we’ll construct in this section.
To start oﬀ, let’s go over the diﬀerence between a generating set of an R-module and a
generating set of an R-algebra. When we say an R-module M is generated by m1, . . . , mn,
we mean every element of M is an R-linear combination of m1, . . . , mn.
When we say
an R-algebra A is generated by a1, . . . , an we mean every element of A is a polynomial in
a1, . . . , an with coeﬃcients in R, i.e., is an R-linear combination of products of the ai’s. For
example, the ring R[X] is both an R-module and an R-algebra, but as an R-module it is
generated by {1, X, X2, . . .} while as an R-algebra it is generated by X alone. A generating
set of an R-module is also called a spanning set, but the generating set of an R-algebra is
not called a spanning set (the term “span” is used for linear things).
To enlarge an R-module M to an R-algebra, we want to multiply elements in M without
having any multiplication deﬁned in advance. (As in Section 7, R-algebras are associative.)
The “most general” product m1m2 for m1 and m2 in M should be bilinear in m1 and m2,
so we want this product to be the elementary tensor m1 ⊗m2, which lives not in M but in

<!-- page 40 -->
40
KEITH CONRAD
M⊗2. Similarly, an expression like m1m2 + m3m4m5 using ﬁve elements from M should be
m1 ⊗m2 + m3 ⊗m4 ⊗m5 in M⊗2 ⊕M⊗3. This suggests creating an R-algebra as
M
k≥0
M⊗k = R ⊕M ⊕M⊗2 ⊕M⊗3 ⊕· · · ,
whose elements are formal sums P tk with tk ∈M⊗k and tk = 0 for all large k. We want
to multiply by the intuitive rule
(8.1)
X
k≥0
tk ·
X
ℓ≥0
t′
ℓ=
X
n≥0
 X
k+ℓ=n
tk ⊗t′
ℓ
!
,
where tk ⊗t′
ℓ∈M⊗n if k + ℓ= n. To show this multiplication makes the direct sum of all
M⊗k an R-algebra we use the following construction theorem.
Theorem 8.1. Let {Mk}k≥0 be a sequence of R-modules with M0 = R and let there be
R-bilinear mappings (“multiplications”) µk,ℓ: Mk × Mℓ→Mk+ℓfor all k and ℓsuch that
1) (scaling by R) µk,0 : Mk × R →Mk and µ0,ℓ: R × Mℓ→Mℓare both scaling by R:
µk,0(x, r) = rx and µ0,ℓ(r, y) = ry for r ∈R, x ∈Mk, and y ∈Mℓ,
2) (associativity) for k, ℓ, n ≥0 we have µk,ℓ+n(x, µℓ,n(y, z)) = µk+ℓ,n(µk,ℓ(x, y), z) in
Mk+ℓ+n for all x ∈Mk, y ∈Mℓ, and z ∈Mn.
The direct sum L
k≥0 Mk is an associative R-algebra with identity using the multiplication
rule P
k≥0 mk · P
ℓ≥0 m′
ℓ= P
n≥0
 P
k+ℓ=n µk,ℓ(mk, m′
ℓ)

.
Proof. The direct sum L
k≥0 Mk is automatically an R-module. It remains to check (i) the
multiplication deﬁned on the direct sum is R-bilinear, (ii) 1 ∈R = M0 is a multiplica-
tive identity, and (iii) multiplication is associative. The R-bilinearity of multiplication is a
bookkeeping exercise left to the reader. In particular, this includes distributivity of multi-
plication over addition. To prove multiplication has 1 as an identity and is associative, it
suﬃces by distributivity to consider only multiplication with factors from direct summands
Mk, in which case we can use the two properties of the maps µk,ℓin the theorem.
□
Lemma 8.2. For k, ℓ≥0, there is a unique bilinear map βk,ℓ: M⊗k × M⊗ℓ→M⊗(k+ℓ)
where βk,0(t, r) = rt, β0,ℓ(r, t) = rt, and for k, ℓ≥1, βk,ℓ(m1 ⊗· · · ⊗mk, m′
1 ⊗· · · ⊗m′
ℓ) =
m1 ⊗· · · ⊗mk ⊗m′
1 ⊗· · · ⊗m′
ℓon pairs of elementary tensors.
Proof. The cases k = 0 and ℓ= 0 are trivial, so let k, ℓ≥1. It suﬃces to construct a
bilinear βk,ℓwith the indicated values on pairs of elementary tensors; uniqueness is then
automatic since elementary tensors span M⊗k and M⊗ℓ.
Deﬁne f : M × · · · × M
|
{z
}
k times
× M × · · · × M
|
{z
}
ℓtimes
→M⊗(k+ℓ) by
f(m1, . . . , mk, m′
1, . . . , m′
ℓ) = m1 ⊗· · · ⊗mk ⊗m′
1 ⊗· · · ⊗m′
ℓ.
This is (k + ℓ)-multilinear. In particular, f is multilinear in the ﬁrst k factors when the
last ℓfactors are ﬁxed and it is multilinear in the last ℓfactors when the ﬁrst k factors are
ﬁxed, so we can collapse the ﬁrst k factors and the last ℓfactors into tensor powers to get

<!-- page 41 -->
TENSOR PRODUCTS II
41
a bilinear mapping βk,ℓ: M⊗k × M⊗ℓ→M⊗(k+ℓ) making the diagram
M⊗k × M⊗ℓ
βk,ℓ

(M × · · · × M) × (M × · · · × M)
(⊗,⊗)
3
f
+ M⊗(k+ℓ)
commute. (This collapsing is analogous to the proof of associativity of the tensor product
in part I.) By commutativity of the diagram, on a pair of elementary tensors we have
βk,ℓ(m1 ⊗· · · ⊗mk, m′
1 ⊗· · · ⊗m′
ℓ) = f(m1, . . . , mk, m′
1, . . . , mℓ)
= m1 ⊗· · · ⊗mk ⊗m′
1 ⊗· · · ⊗m′
ℓ.
□
Theorem 8.3. The M-module L
k≥0 M⊗k is an R-algebra using the multiplication in (8.1).
Proof. Use Theorem 8.1 with Mk = M⊗k and µk,ℓ= βk,ℓfrom Lemma 8.2. The ﬁrst prop-
erty of the maps µk,ℓin Theorem 8.1 is automatic from the deﬁnition of βk,0 and β0,ℓ. To
prove the second property of the maps µk,ℓin Theorem 8.1, namely µk,ℓ+n(t1, µℓ,n(t2, t3)) =
µk+ℓ,n(µk,ℓ(t1, t2), t3) in M⊗(k+ℓ+n) for all t1 ∈M⊗k, t2 ∈M⊗ℓ, and t3 ∈M⊗n, by multi-
linearity of each µk,ℓ= βk,ℓit suﬃces to consider the case when each ti is an elementary
tensor, in which case the equality is a simple calculation.
□
Deﬁnition 8.4. For an R-module M, its tensor algebra is T(M) := L
k≥0 M⊗k with
multiplication deﬁned by (8.1).
Since multiplication in T(M) is the tensor product, a generating set of M as an R-module
is a generating set of T(M) as an R-algebra.
Example 8.5. If M = R then M⊗k ∼= R as an R-module and T(M) ∼= R[X] with Xk
corresponding to the k-fold tensor 1 ⊗· · · ⊗1 in R⊗k.
Example 8.6. If M is a ﬁnite free R-module with basis e1, . . . , en then T(M) is the poly-
nomial ring over R in n noncommuting indeterminates e1, . . . , en: in M⊗2, ei ⊗ej ̸= ej ⊗ei
when i ̸= j, which says in T(M) that eiej ̸= ejei.
Remark 8.7. The tensor product construction of the polynomial ring over R in n non-
commuting indeterminates is quite diﬀerent from that of the tensor product construction
of the commutative polynomial ring R[X1, . . . , Xn]: the former is the tensor algebra T(Rn)
of a free R-module of rank n while the latter is R[X]⊗n (Example 7.8).
The mapping i: M →T(M) that identiﬁes M with the k = 1 component of T(M) is
R-linear and injective, so we can view M as a submodule of T(M) (the “degree 1” terms)
using i. Just as the bilinear map M × N →M ⊗R N is universal for R-bilinear maps from
M × N to all R-modules, the mapping i: M →T(M) is universal for R-linear maps from
M to all R-algebras.

<!-- page 42 -->
42
KEITH CONRAD
Theorem 8.8. Let M be an R-module. For each R-algebra A and R-linear map f : M →A,
there is a unique R-algebra map F : T(M) →A such that the diagram
T(M)
F

M
i
7
f
( A
commutes.
This says R-linear maps from M to an R-algebra A turn into R-algebra homomorphisms
from T(M) to A. It works by extending an R-linear map from M →A to an R-algebra map
T(M) →A by forcing multiplicativity, and there are no relations to worry about keeping
track of because T(M) is an R-algebra formed from M in the most general way possible.
Proof. First suppose there is an R-algebra map F that makes the indicated diagram com-
mute. For r ∈R, F(r) = r since F is an R-algebra homomorphism. Since T(M) is generated
as an R-algebra by M, an R-algebra homomorphism out of T(M) is determined by its values
on M, which really means its values on i(M). For m ∈M, we have F(i(m)) = f(m), and
thus there is at most one R-algebra homomorphism F that ﬁts into the above commutative
diagram.
To construct F, we will deﬁne it ﬁrst on each M⊗k in T(M) and then extend by additivity.
For k ≥1, the R-linear map f : M →A leads to an R-linear map f⊗k : M⊗k →A⊗k that is
m1⊗· · ·⊗mk 7→f(m1)⊗· · ·⊗f(mk) on elementary tensors. Multiplication on A gives us an
R-linear map A⊗k →A that is a1 ⊗· · · ⊗ak 7→a1 · · · ak on elementary tensors. Composing
this with f⊗k gives us an R-linear map Fk : M⊗k →A whose value on elementary tensors
is
Fk(m1 ⊗· · · ⊗mk) = f(m1) · · · f(mk).
Deﬁne F0 : M⊗0 →A by F0(r) = r · 1A for r ∈R. Finally, deﬁne F : T(M) →A by
F

X
k≥0
tk

=
X
k≥0
Fk(tk)
where tk ∈M⊗k and tk = 0 for large k. Since each Fk is R-linear and F0(1) = 1A, F
is R-linear and F(1) = 1A. To prove F is multiplicative, by linearity it suﬃces to check
F(xy) = F(x)F(y) where x is an elementary tensor in some M⊗k and y is an elementary
tensor in some M⊗ℓ. The cases k = 0 and ℓ= 0 are the linearity of F. If k, ℓ≥1, write
x = m1 ⊗· · · ⊗mk and y = m′
1 ⊗· · · ⊗m′
ℓ. Then xy = m1 ⊗· · · ⊗mk ⊗m′
1 ⊗· · · ⊗m′
ℓin
T(M), so
F(xy) = Fk+ℓ(xy) = f(m1) · · · f(mk)f(m′
1) · · · f(m′
ℓ)
and
F(x)F(y) = Fk(x)Fℓ(y)
= (f(m1) · · · f(mk))(f(m′
1) · · · f(m′
ℓ))
= f(m1) · · · f(mk)f(m′
1) · · · f(m′
ℓ).
Thus F(xy) = F(x)F(y).
□

<!-- page 43 -->
TENSOR PRODUCTS II
43
Tensor algebras are useful preliminary constructions for other structures that can be
deﬁned as a quotient of them, such as the exterior algebra of a module, the Cliﬀord algebra
of a quadratic form, and the universal enveloping algebra of a Lie algebra.
References
[1] S. Friedl, Eta invariants as sliceness obstructions and their relation to Casson–Gordon invariants, Algebr.
Geom. Topol. 4 (2004), 893–934. URL https://arxiv.org/pdf/math/0305402.
[2] H. V. Henderson and F. Pukelsheim, On the History of the Kronecker Product, Linear and Multilinear
Algebra 14 (1983), 113–120.
[3] N. Jacobson,“Basic Algebra II,” 2nd ed., W. H. Freeman & Co., New York, 1989.
[4] E. Schr¨odinger, Discussion of Probability Relations between Separated Systems, Math. Proc. Camb.
Philos. Society 31 (1935), 555–563. URL https://www.cambridge.org/core/journals/mathematical-
proceedings-of-the-cambridge-philosophical-society/article/discussion-of-probability-rela
tions-between-separated-systems/C1C71E1AA5BA56EBE6588AAACB9A222D.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*