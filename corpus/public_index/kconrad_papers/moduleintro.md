# Introduction to Modules

> **Source**: https://kconrad.math.uconn.edu/blurbs/moduleintro.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
INTRODUCTORY NOTES ON MODULES
KEITH CONRAD
1. Introduction
One of the most basic concepts in linear algebra is linear combinations: of vectors, of polynomials,
of functions, and so on. For example, the polynomial 7 −2T + 3T 2 is a linear combination of 1, T,
and T 2: 7 · 1 −2 · T + 3 · T 2. The coeﬃcients used for linear combinations in a vector space are in
a ﬁeld, but there are many places where we meet linear combinations with coeﬃcients in a ring.
Example 1.1. In the ring Z[√−5] let p be the ideal (2, 1 + √−5), so by deﬁnition
p =

2x + (1 +
√
−5)y : x, y ∈Z[
√
−5]
	
= Z[
√
−5] · 2 + Z[
√
−5] · (1 +
√
−5),
which is the set of all linear combinations of 2 and 1 + √−5 with coeﬃcients in Z[√−5].
Such linear combinations do not provide unique representation: for x and y in Z[√−5],
x · 2 + y · (1 +
√
−5) = (x −(1 +
√
−5)) · 2 + (y + 2) · (1 +
√
−5).
So we can’t treat x and y as “coordinates” of 2x + (1 + √−5)y. In a vector space like Rn or Cn,
whenever there is a duplication of representations with a spanning set we can remove a vector from
the spanning set, but in p this is not the case: if we could reduce the spanning set {2, 1 + √−5} of
p to a single element α, then p = Z[√−5]α = (α) would be a principal ideal in Z[√−5], but it can
be shown that p is not a principal ideal.
Instead of reducing the size of {2, 1 + √−5} to get a nice spanning set for p with Z[√−5]-
coeﬃcients, we can try to do something else to standardize the representation of elements of p as
linear combinations: restrict coeﬃcients to Z. That works in this case because:
p =

2x + (1 +
√
−5)y : x, y ∈Z[
√
−5]
	
=

2(a + b
√
−5) + (1 +
√
−5)(c + d
√
−5) : a, b, c, d ∈Z
	
=

2a + 2
√
−5b + (1 +
√
−5)c + (−5 +
√
−5)d : a, b, c, d ∈Z
	
= Z · 2 + Z · 2
√
−5 + Z · (1 +
√
−5) + Z · (−5 +
√
−5).
Describing p in terms of linear combinations with Z-coeﬃcients made the spanning set grow. We
can shrink the spanning set back to {2, 1 + √−5} because the new members of this spanning set,
2√−5 and −5 + √−5, are Z-linear combinations of 2 and 1 + √−5:
2
√
−5 = (−1)2 + 2(1 +
√
−5)
and
−5 +
√
−5 = (−3)2 + (1 +
√
−5).
1

<!-- page 2 -->
2
KEITH CONRAD
Thus 2√−5 and −5 + √−5 are in Z · 2 + Z · (1 + √−5), so
p = Z · 2 + Z · (1 +
√
−5) =

2m + (1 +
√
−5)n : m, n ∈Z
	
.
Using coeﬃcients in Z rather than in Z[√−5], there is unique representation: if 2m+(1+√−5)n =
2m′ + (1 + √−5)n′ then
(2(m −m′) + (n −n′)) + (n −n′)
√
−5 = 0.
The real and imaginary parts are 0, so n = n′ and then m = m′. Thus, we can regard m and n as
“coordinates” for 2m + (1 + √−5)n, and the situation looks a lot closer to ordinary linear algebra.
Warning. That the set {2, 1 + √−5} has its Z[√−5]-linear combinations coincide with its Z-
linear combinations is something of a ﬂuke. In the ring Z[
√
d], the set of Z-linear combinations of
two elements generally does not coincide with the set of their Z[
√
d]-linear combinations.
The use of linear combinations with coeﬃcients coming from a ring rather than a ﬁeld suggests
the concept of “vector space over a ring,” which for historical reasons is not called a vector space
but instead a module.
Deﬁnition 1.2. For a commutative ring R, an R-module M is an abelian group M on which R
acts by additive maps respecting the ring structure of R when these maps are added and composed:
there is a scalar multiplication function R × M →M denoted by (r, m) 7→rm such that
(1) 1m = m for all m ∈M.
(2) r(m + m′) = rm + rm′ for all r ∈R and m, m′ ∈M.
(3) (r + r′)m = rm + r′m and (rr′)m = r(r′m) for all r, r′ ∈R and m ∈M.
In the special case when R = F is a ﬁeld, an F-module is just an F-vector space by another
name.
Example 1.3. The set Rn of ordered n-tuples in R with componentwise addition and scalar
multiplication by R as in linear algebra is an R-module.
Example 1.4. Every ideal I in R is an R-module with addition and scalar multiplication being
the operations in R.
Example 1.5. A quotient ring R/I for an ideal I is an R-module where r(x mod I) := rx mod I
for r ∈R and x ∈R. (It is easy to check that this is well-deﬁned and satisﬁes the axioms.) So I
and R/I are both R-modules, whereas in the language of ring theory, ideals and quotient rings are
not the same kind of object: an ideal is almost never a ring, for instance.
Example 1.6. The ring R[T] is an R-module using obvious addition and scalar multiplication.
Example 1.7. The set Map(R, R) of functions f : R →R under pointwise addition of functions
and the scalar multiplication (rf)(x) = r(f(x)) is an R-module.

<!-- page 3 -->
INTRODUCTORY NOTES ON MODULES
3
That addition in M is commutative actually follows from other axioms for R-modules: distribu-
tivity both ways on (1 + 1)(m + m′) shows m + m + m′ + m′ = m + m′ + m + m′, and canceling
the leftmost m’s and rightmost m′’s (addition on M is a group law) gives m + m′ = m′ + m for all
m and m′ in M.
We will show how many concepts from linear algebra (linear dependence/independence, basis,
linear transformation, subspace) can be formulated for modules. When the scalars are not a ﬁeld,
we encounter genuinely new phenomena. For example, the intuitive idea of linear independence in
a vector space as meaning no vector is a linear combination of the others is the wrong way to think
about linear independence in modules. As another example, in a vector space each spanning set
can be reﬁned to a basis, but a module with a ﬁnite generating set does not have to have a basis
(this is related to nonprincipal ideals). In the last section, we’ll see how the concept of a module
gives a new way to think about a question purely about matrices acting on vector spaces: for a
ﬁeld F and matrices A and B in Matn(F), deciding if A and B are conjugate in Matn(F) is the
same as deciding if two F[T]-module structures on F n (each one uses A or B) are isomorphic.
2. Basic definitions
In linear algebra the concepts of linear combination, linear transformation, isomorphism, sub-
space, and quotient space all make sense when the coeﬃcients are in a ring, not just a ﬁeld, so they
can all be adapted to the setting of modules with no real changes.
Deﬁnition 2.1. In an R-module M, an R-linear combination of elements m1, . . . , mk ∈M is
an element of M having the form
r1m1 + · · · + rkmk
where the ri’s are in R. If every element of M is a linear combination of m1, . . . , mk, we call
{m1, . . . , mk} a spanning set or generating set of M or say the mi’s span (or generate) M.
Linear combinations are the basic way to create new elements of a module from old ones, just
as in linear algebra in Rn. For instance, an ideal (a, b, c) = Ra + Rb + Rc in R is nothing other
than the set of R-linear combinations of a, b, and c in R.
Example 2.2. We can view the ideal I = (1+2i) in Z[i] as both a Z[i]-module and as a Z-module
in a natural way. As a Z[i]-module, we can get everywhere in I from 1+2i: I = Z[i](1+2i). As a Z-
module, we can get everywhere in I from 1+2i and i(1+2i) = −2+i since I = Z(1+2i)+Zi(1+2i) =
Z(1 + 2i) + Z(−2 + i).
Mostly we will be interested in modules with ﬁnite spanning sets, but there are some important
examples of modules that require inﬁnite spanning sets.
So let’s give the general deﬁnition of
spanning set, allowing inﬁnite ones.

<!-- page 4 -->
4
KEITH CONRAD
Deﬁnition 2.3. A spanning set of an R-module M is a subset {mi}i∈I of M such that every
m ∈M is a ﬁnite R-linear combination of the mi’s:
m =
X
i∈I
rimi,
where ri ∈R for all i and ri = 0 for all but ﬁnitely many i.
Notice in this deﬁnition that we require each linear combination of the mi’s to have only ﬁnitely
many nonzero coeﬃcients. (Of course, if there are only ﬁnitely many mi’s to begin with then this
is no constraint at all.) In analysis, vector spaces may be equipped with a topology and we can
talk about truly inﬁnite linear combinations using a notion of convergence. The preceding purely
algebraic concept of spanning set only makes sense with ﬁnite sums in the linear combinations.
Example 2.4. The powers 1, T, T 2, . . . span R[T] as an R-module, since every polynomial is an
R-linear combination of ﬁnitely many powers of T. There is no ﬁnite spanning set for R[T] as an R-
module since the R-linear combinations of a ﬁnite set of polynomials will only produce polynomials
of degree bounded by the largest degree of the polynomial in the ﬁnite set.
This is the simplest example of an R-module mathematicians care about that doesn’t have a
ﬁnite spanning set. Notice that as an R[T]-module rather than as an R-module, R[T] has a ﬁnite
spanning set, namely the element 1, since we can write f(T) = f(T) · 1.
Example 2.5. Let
R∞= {(r1, r2, r3, . . .) : rn ∈R}
be the set of all sequences in R, with componentwise addition and the natural scalar multiplication.
This makes R∞an R-module, and as in the previous example R∞doesn’t have a ﬁnite spanning
set (except in the silly case R = 0). But also the ﬁrst guess for an inﬁnite spanning set doesn’t
work: the sequences
ei = (0, 0, . . . ,
1
|{z}
i
, 0, 0, . . .)
for i ≥1 do not span R∞since a ﬁnite linear combination of the ei’s is a sequence with all terms
beyond some point equal to 0 and that doesn’t describe most elements of R∞.1 For instance, the
constant sequence (1, 1, 1, . . . ) is not in the R-span of the ei’s.
While the ei’s are not a spanning set of R∞as an R-module, is there a spanning set for R∞as
an R-module? Yes: use all of R∞. (And likewise every R-module M has M as a spanning set.)
That is kind of dumb, but it shows (for silly reasons) that R∞has a spanning set. Whether R∞
has a “nice” spanning set (in some reasonable sense of “nice”) is a question for another day.
Deﬁnition 2.6. An R-module M is called ﬁnitely generated when it has a ﬁnite spanning set
as an R-module.
We saw above that R[T] is not ﬁnitely generated as an R-module, but is ﬁnitely generated as
an R[T]-module. Finitely generated modules sound analogous to ﬁnite-dimensional vector spaces
1Unless R is the zero ring, but let’s not be ridiculous.

<!-- page 5 -->
INTRODUCTORY NOTES ON MODULES
5
(a vector space has a ﬁnite spanning set if and only if it is ﬁnite-dimensional), but the analogy is
rather weak: ﬁnitely generated modules can be very complicated when R is not a ﬁeld.
Deﬁnition 2.7. A R-linear transformation (or R-linear map) from an R-module M to an
R-module N is a function ϕ: M →N that is additive and commutes with scaling: ϕ(m + m′) =
ϕ(m) + ϕ(m′) and ϕ(rm) = rϕ(m) for all m, m′ ∈M and r ∈R. These can be combined into the
single condition
ϕ(rm + r′m′) = rϕ(m) + r′ϕ(m′),
for all m, m′ ∈M and r, r′ ∈R.
In words, this says ϕ sends R-linear combinations to R-linear combinations with the same
coeﬃcients.
(Taking r = r′ = 1 makes this the additive condition and taking r′ = 0 makes
this the scaling condition.)
We can also characterize a linear transformation as one satisfying
ϕ(rm + m′) = rϕ(m) + ϕ(m′), but that description is asymmetric while the concept of linear
transformation is not, so don’t use that description!
Example 2.8. Complex conjugation τ : C →C, where τ(z) = z, is an R-linear transformation
from C to C. It is not C-linear since cz is equal to c z rather than equal to cz.
Example 2.9. For α ∈Z[
√
2], let mα : Z[
√
2] →Z[
√
2] be mα(x) = αx. This is multiplication on
Z[
√
2] by a ﬁxed number α. It is Z-linear, since
mα(x + x′) = α(x + x′) = αx + αx′ = mα(x) + mα(x′)
for all x and x′ in Z[
√
2] and
mα(cx) = α(cx) = c(αx) = cmα(x)
for all c ∈Z and x ∈Z[
√
2]. Actually, if c is in Z[
√
2] then the last equation still holds, so mα is
also Z[
√
2]-linear (we’ll look at this more broadly in the next example), but usually mα is viewed
as being Z-linear.
Example 2.10. The R-linear maps ϕ: R →R are exactly the functions ϕ(x) = ax for some a ∈R.
Indeed, if ϕ is R-linear then ϕ(x) = ϕ(x · 1) = xϕ(1) = xa = ax where a = ϕ(1). And conversely,
letting ϕa : R →R for a ∈R by ϕa(x) = ax, this is R-linear since
(2.1) ϕa(x + y) = a(x + y) = ax + ay = ϕa(x) + ϕa(y),
ϕa(rx) = a(rx) = arx = rax = rϕa(x).
We used commutativity of multiplication in R in some steps of (2.1). The notions of an R-module
and an R-linear map between R-modules make sense even if R is not commutative, but then you
need to deﬁne left vs. right R-modules (on which side do you scale by R) in the same way that
there are left or right (or two-sided) ideals in a noncommutative ring and left or right group actions.
In fact, if R is possibly noncommutative then the “left” R-linear maps R →R are the right
multiplication maps ϕa(x) = xa (this agrees with ax if R is commutative). Indeed, if ϕ: R →R
is left R-linear then ϕ(x) = ϕ(x · 1) = xϕ(1) = xa where a = ϕ(1). Check x 7→xa is left R-linear

<!-- page 6 -->
6
KEITH CONRAD
using associativity of multiplication in R. The way x 7→xa and x 7→xb compose is opposite to the
way a and b multiply: ϕa(ϕb(x)) = ϕa(xb) = (xb)a = x(ba) = ϕba(x), so ϕa ◦ϕb is ϕba, not ϕab (if
ba ̸= ab). Tricky! It’s best to learn about modules over commutative rings ﬁrst.
Example 2.11. For positive integers m and n, each matrix A ∈Mn×m(R) deﬁnes an R-linear
transformation Rm →Rn by v 7→Av (the usual product of a matrix and a vector). Note the ﬂip in
the order of m and n in the size of the matrix and in the domain and target of the transformation.
Remark 2.12. In Section 3 we’ll deﬁne the concept of a basis for a ﬁnitely generated module.
Some ﬁnitely generated modules do not have a basis, such as a nonprincipal ﬁnitely generated ideal
(Example 3.7). For ﬁnitely generated modules M and N that have bases, it will turn out (just as
in linear algebra) that every linear transformation M →N can be described with a matrix as in
Example 2.11.
For modules without bases, there is nothing like a matrix available to describe a linear trans-
formation between them. This is the fundamental diﬀerence between vector spaces and modules:
matrices are insuﬃcient for describing linear maps between general modules, even between general
ﬁnitely generated modules.
Deﬁnition 2.13. An isomorphism of R-modules M and N is a bijective R-linear transformation
ϕ: M →N. If there is an isomorphism M →N we call M and N isomorphic and write M ∼= N.
The inverse of an isomorphism is also R-linear and thus is an isomorphism too.
Example 2.14. Consider Z[i] = Z + Zi and Z[
√
2] = Z + Z
√
2. They are rings and Z-modules.
As rings they are not isomorphic, because isomorphic rings have isomorphic unit groups and Z[i]×
is ﬁnite while Z[
√
2]× is inﬁnite (e.g., (1 +
√
2)n has multiplicative inverse (−1 +
√
2)n for all
n > 0). But as Z-modules they’re isomorphic to Z2 and thus are isomorphic to each other. Indeed,
Z2 →Z[i] by (a, b) 7→a + bi and Z2 →Z[
√
2] by (a, b) 7→a + b
√
2 are Z-module isomorphisms, and
a direct Z-module isomorphism from Z[i] to Z[
√
2] is a + bi 7→a + b
√
2.
Deﬁnition 2.15. For an R-linear transformation ϕ: M →N, its kernel is {m ∈M : ϕ(m) = 0}
and is denoted ker ϕ, and its image is {ϕ(m) : m ∈M}, denoted im ϕ.
Like group homomorphisms, an R-linear transformation ϕ is injective if and only if ker ϕ = {0}.
Being injective is a property that does not involve R-linearity, so we can think about whether ϕ is
injective just by treating ϕ as a group homomorphism, which makes it clear that this property is
the same as having kernel {0}.
Deﬁnition 2.16. If M is an R-module, an R-submodule of M is a subgroup N ⊂M such that
Rn ⊂N for all n ∈N.
An R-submodule is again an R-module, similar to a subgroup being a group. We will generally
abbreviate R-submodule to submodule, with R being understood.

<!-- page 7 -->
INTRODUCTORY NOTES ON MODULES
7
Example 2.17. Viewing R as an R-module, its submodules are precisely its ideals. This is very
important!
Whenever we have an R-module M and R contains a subring R′, we can think about M as an
R′-module too, in a natural way. We did this in Example 1.1 with the ideal p = (2, 1+√−5) inside
R = Z[√−5], viewing it ﬁrst as a Z[√−5]-module and then as a Z-module. Its representation as a
Z-module was nicer (leading to coordinates).
Example 2.18. In Z[i] the Z[i]-submodules all have the form Z[i]α since all ideals in Z[i] are prin-
cipal. In Z[i] its Z[i]-submodules (ideals) are also Z-submodules, but there are more Z-submodules
in Z[i] than ideals. For example, Z + Z · 2i = {a + 2bi : a, b ∈Z} is a Z-submodule of Z[i] that is
not an ideal (it isn’t preserved under multiplication by i).
Deﬁnition 2.19. If N ⊂M is a submodule, then the quotient group M/N has the natural scalar
multiplication r(m mod N) := rm mod N (easily checked to be well-deﬁned and to satisfy the
axioms to be an R-module). We call M/N a quotient module.
In particular, for ideals J ⊂I ⊂R, we can say that I/J is an ideal in R/J or (without mentioning
R/J) that I/J is an R-module.
It is straightforward to check that if ϕ: M →N is an R-linear transformation, the kernel and
image of ϕ are both R-modules (one is a submodule of M and the other is a submodule of N)
and the homomorphism theorems for groups carry over to theorems about linear transformations
of R-modules.
For example, an R-linear map ϕ: M →N induces an injective R-linear map
ϕ: M/ ker ϕ →N that is an isomorphism of M/ ker ϕ with im ϕ.
Deﬁnition 2.20. For R-modules M and N, their direct sum is
M ⊕N = {(m, n) : m ∈M, n ∈N}
with componentwise addition and with scaling deﬁned by
r(m, n) = (rm, rn).
More generally, for a collection of R-modules {Mi}i∈I, their direct sum is the R-module
M
i∈I
Mi = {(mi)i∈I : mi ∈Mi and all but ﬁnitely many mi are 0}
and their direct product is the R-module
Y
i∈I
Mi = {(mi)i∈I : mi ∈Mi} .
The construction of the direct sum and direct product of R-modules appears diﬀerent only when
the index set I is inﬁnite. In particular, we may write M ⊕N or M × N for this common notion
when given just two R-modules M and N.
Note M ∼= M ⊕{0} and N ∼= {0} ⊕N inside M ⊕N.

<!-- page 8 -->
8
KEITH CONRAD
As in group theory, there is a criterion for a module to be isomorphic to the direct product of two
submodules by addition: if L is an R-module with submodules M and N, we have M ⊕N ∼= L by
(m, n) 7→m+n if and only if M +N = L and M ∩N = {0}. (Addition from M ⊕N to L is R-linear
by the way the R-module structure on M ⊕N is deﬁned. Then the property M + N = L makes
the addition map surjective and the property M ∩N = {0} makes the addition map injective.)
3. Linear independence, bases, and free modules
Let M be an R-module. Recall a spanning set {mi}i∈I is a subset such that for each m ∈M,
m =
X
i∈I
rimi
where ri ∈R and ri = 0 for all but ﬁnitely many i.
Deﬁnition 3.1. In an R-module M, a subset {mi}i∈I is called linearly independent if the only
relation P
i rimi = 0 is the one where all ri are 0, and linearly dependent otherwise: there is
a relation P
i rimi = 0 where some ri is not 0. A subset of M is called a basis if it is a linearly
independent spanning set. A module that has a basis is called a free module, and if the basis is
ﬁnite then M is called a ﬁnite-free module.
Remark 3.2. In a vector space, {vi}i∈I is linearly independent if no vi is a linear combination
of the other vj’s. The equivalence of that with P
i civi = 0 ⇒all ci = 0 uses division by nonzero
scalars in a ﬁeld. In a module over a ring that is not a ﬁeld, we can’t divide scalars and the two
viewpoints of linear independence in vector spaces really are not the same in the setting of modules.
The description in terms of P
i civi = 0 is the right one to carry over to modules.
Example 3.3. If R ̸= 0 then the R-module Rn = {(r1, . . . , rn) : ri ∈R} has basis {e1, . . . , en}
where
ei = (0, . . . , 0,
1
|{z}
i
, 0, . . . , 0).
We can think of Rn as being the direct sum of its submodules Rei.
Example 3.4. If R ̸= 0 then the R-module R[T] has basis

1, T, T 2, T 3, . . .
	
.
Example 3.5. The ideal p = (2, 1+√−5) of Z[√−5] can be regarded as both a Z[√−5]-module and
a Z-module. The set {2, 1+√−5} is linearly dependent over Z[√−5] since r1 ·2+r2(1+√−5) = 0
where r1 = 1 + √−5 and r2 = −2 while it is linearly independent over Z and in fact is a basis of p
as a Z-module from Example 1.1.
It is not hard to check that in a module, every subset of a linearly independent subset is linearly
independent and every superset of a linearly dependent set is linearly dependent (the calculation
goes exactly as in linear algebra), but beware that a lot of the geometric intuition you have about
linear independence and bases for vector spaces in linear algebra over ﬁelds breaks down for modules

<!-- page 9 -->
INTRODUCTORY NOTES ON MODULES
9
over rings. The reason is that rings in general behave diﬀerently from ﬁelds: two nonzero elements
need not be multiples of each other and some nonzero elements could be zero divisors.
Perhaps the most basic intuition about linear independence in vector spaces that has to be used
with caution in a module is the meaning of linear independence. In a module, linear independence
is deﬁned to mean “no nontrivial linear relations,” but in a vector space linear independence
has an entirely diﬀerent-looking but equivalent formulation: no member of the subset is a linear
combination of the other members in the subset. This latter condition is a valid property of linearly
independent subsets in a module (check!) but it is not a characterization of linear independence in
modules in general:
Example 3.6. In M := Z as a Z-module, we cannot write either of the elements 2, 3 ∈M as a
Z-multiple of the other (only integer coeﬃcients allowed!), but the subset {2, 3} in M is linearly
dependent: a · 2 + b · 3 = 0 using a = 3 and b = −2.
So the key point is that in a module, if we have a linear dependence relation P rimi = 0 with
some ri0 ̸= 0 and we rewrite this as an equality ri0mi0 = P
i̸=i0(−ri)mi, in order to “divide out”
the ri0-multiplier on the left side as we would do in linear algebra we need a multiplicative inverse
r−1
i0 ∈R. Indeed, with such an inverse available we could multiply throughout by r−1
i0
to turn the
left side into 1 · mi0 = mi0 and the right side into P
i̸=i0(−rir−1
i0 )mi, thereby expressing mi0 as an
R-linear combination of the other mi’s.
Overall, when R is not a ﬁeld, there must exist some nonzero r ∈R that is not a unit (by deﬁnition
of “ﬁeld”!) and so passing from a non-trivial linear dependence relation to an expression of some
mi0 in terms of the others really runs into diﬃculties. This may seem like a minor issue but it
makes a huge diﬀerence, and causes the general structure of modules to be vastly more complicated
that that of vector spaces. Informally speaking, as the ideal theory of R gets more complicated it
becomes more diﬃcult to describe the structure of typical (even just ﬁnitely generated) R-modules.
The concept of linear independence as deﬁned above, rather than the more intuitive idea of no
element being a linear combination of others, turns out to be the right one to use for modules over
general rings.
Another surprise with modules is that, although every (nonzero) ﬁnitely generated vector space
has a basis, a nonzero ﬁnitely generated module need not have a basis: non-free modules exist in
great abundance over rings that are not ﬁelds. We’ve actually already seen an example, and here
it is again.
Example 3.7. Let R = Z[√−5] and let
p = (2, 1 +
√
−5) = 2R + (1 +
√
−5)R
as in Examples 1.1 and 3.5. Then

2, 1 + √−5
	
spans p as an R-module (by deﬁnition) but this
subset is linearly dependent:
2a + b(1 +
√
−5) = 0

<!-- page 10 -->
10
KEITH CONRAD
using a = 1 + √−5 and b = −2. More generally, all pairs x, y ∈p are linearly dependent over
R: ax + by = 0 using a = y and b = −x and one of these coeﬃcients a and b is nonzero unless
x = y = 0, in which case we can use a = b = 1. So a linearly independent subset of p has only one
member, which means a basis of p, if one exists, must have size 1. But if {α} were an R-basis for
p then p = Rα = (α), yet it is a fact that p is not principal. So p is an R-module without a basis.2
Here are more contrasts between ﬁnitely generated vector spaces and ﬁnitely generated modules.
(1) In a vector space every nonzero element is a linearly independent subset, but in a module
this can be false: in M := Z/6Z viewed as a Z-module the subset {2} in M is Z-linearly
dependent since 3 · 2 = 0.
(2) In a (ﬁnitely generated) vector space a maximal linearly independent subset is a spanning
set, but in a module this can be false: in Z as a Z-module the subset {2} is a maximal
linearly independent subset but Z · 2 ̸= Z.
(3) In a (ﬁnitely generated) vector space a minimal spanning set is linearly independent, but
in a module this can be false: in Z as a Z-module {2, 3} is a spanning set (because a =
3a−2a = a·3+(−a)·2) and is minimal (neither {2} nor {3} spans Z), but it is not linearly
independent since 0 = 2 · 3 + (−3) · 2.
(4) In a vector space every linearly independent subset can be enlarged to a basis and every
spanning set contains a basis, but in a module this can be false since a nonzero module need
not contain a basis (Example 3.7). This property is even false in a module that has a basis.
For example, Z as a Z-module has a basis, namely {1}, but {2} is a linearly independent
subset of Z that can’t be enlarged to a Z-basis of Z and {2, 3} is a spanning set of Z that
does not contain a Z-basis of Z.
(5) If V and W are ﬁnite-dimensional vector spaces (over the same ﬁeld) with the same di-
mension and ϕ: V →W is linear, then injectivity of ϕ is equivalent to surjectivity of ϕ.
This can be false for ﬁnite-free modules. View Z as a Z-module (with basis {1}) and let
ϕ: Z →Z by ϕ(m) = 2m. This is injective but not surjective.3
Even if a module is free (that is, has a basis), its submodules don’t have to inherit that property,
and if we restrict our attention to free modules there are still some contrasts with vector spaces:
(1) A submodule of a ﬁnite-free R-module need not be free. Let R = Z[√−5], viewed as an
R-module, and let p = (2, 1 + √−5) as in Examples 1.1, 3.5, and 3.7. Then R has R-basis
{1} while p is ﬁnitely generated but has no R-basis since the ideal p is not principal.
(2) A submodule of a ﬁnite-free R-module need not have a ﬁnite spanning set. An example
of this would be a ring R that has an ideal I that is not ﬁnitely generated. Then R has
R-basis {1} and I is a submodule without a ﬁnite spanning set. Such rings do exist (though
they are not as common to encounter in practice as you might expect); perhaps the most
2By the same reasoning, for every commutative ring R, a nonprincipal ideal in R is an R-module without a basis.
3Surprisingly, surjectivity of an R-linear map Rn →Rn, or more generally of an R-linear map M →M where M is
a ﬁnitely generated R-module, implies injectivity. See Theorem 5.3 in https://kconrad.math.uconn.edu/blurbs/
linmultialg/univid.pdf.

<!-- page 11 -->
INTRODUCTORY NOTES ON MODULES
11
natural example is the ring C∞(R) of smooth functions R →R with pointwise operations.
The functions in C∞(R) whose derivatives of all orders at 0 vanish (it contains the function
that’s e−1/x2 for x ̸= 0 and 0 for x = 0) is an ideal and can be shown not to be ﬁnitely
generated.
(3) A ﬁnite-free R-module can strictly contain a ﬁnite-free R-module with bases of the same
size (this never occurs in linear algebra: a subspace with the same ﬁnite dimension must
be the entire space). For example, with R = Z we can use M = Zd and N = (2Z)d where
d ≥1. More generally, for every domain R that is not a ﬁeld and every nonzero non-unit
a ∈R we can use M = Rd and N = (Ra)d.
4. Abelian groups vs. modules
What is a Z-module? It’s an abelian group M equipped with a map Z × M →M such that for
all m, m′ ∈M and a, a′ ∈Z,
(1) 1m = m,
(2) a(m + m′) = am + am′,
(3) (a + a′)m = am + a′m and (aa′)m = a(a′m).
Armed with these conditions, it’s easy to see by induction that for a ∈Z+,
am = m + m + · · · + m
|
{z
}
a times
.
It follows easily from this that
(−a)m = a(−m) = −m −m −· · · −m
|
{z
}
a times
,
and we also have (0)m = 0. Thus multiplication by Z on a Z-module is the usual concept of integral
multiples in an abelian group (or integral powers if we used multiplicative notation for the group
law in M), so an abelian group M has only one Z-module structure.
In other words, a Z-module is just another name for an abelian group, and its Z-submodules are
just its subgroups. A Z-linear transformation between two Z-modules is just a group homomor-
phism (“additive map”) between abelian groups, because the scaling condition ϕ(am) = aϕ(m)
with a ∈Z is true for all group homomorphims ϕ. (Warning. A nonabelian group is not a Z-
module! Modules always have commutative addition by deﬁnition, and we also saw at the end of
Section 1 that it is logically forced by the other conditions for being a module. You might also
recall the exercise from group theory that if (gh)2 = g2h2 for all elements g and h then gh = hg,
so g and h must commute.)
There are many concepts related to abelian groups that generalize in a useful way to R-modules.
If the concept can be expressed in terms of Z-linear combinations, then replace Z with R and
presto: you have the concept for R-modules. Below is a table of comparison of such concepts.

<!-- page 12 -->
12
KEITH CONRAD
Abelian group G
R-module M
Homomorphism
R-linear map
Subgroup
R-submodule
Cyclic: G = ⟨g⟩= {ng : n ∈Z}
Cyclic R-module: M = Rm for an m ∈M.
Finitely generated: G = ⟨g1, . . . , gk⟩= Zg1+· · ·+
Zgk.
Finitely generated R-module: M = Rm1 +
· · · + Rmk for some m1, . . . , mk ∈M.
Finite order: ng = 0 for an n ̸= 0.
Torsion element: rm = 0 for an r ̸= 0 in R
(a domain).
Torsion group: all elements of G have ﬁnite order.
Torsion module (R a domain): all elements
of M are torsion elements.
Torsion subgroup: {g ∈G : g has ﬁnite order}.
Torsion submodule of M (R al domain):
{m ∈M | rm = 0 for some r ̸= 0}.
Torsion-free abelian group: no elements of ﬁnite
order besides 0.
Torsion-free R-module (for a domain R): no
torsion elements besides 0.
Finite abelian group: ﬁnitely generated torsion
abelian group.
(False characterization of ﬁnite
nonabelian groups!)
Finitely generated torsion R-module (for a
domain R).
In the table, a cyclic module is an R-module for which there is an element whose R-multiples
give everything in the module Just that there is one element whose R-multiples give you everything
in the module. For example, an ideal in R is a cyclic R-module precisely when it is a principal
ideal. For an ideal I in R, R/I is a cyclic R-module since everything in R/I is an R-multiple of
1 mod I.
We have seen the fourth item in the table, ﬁnitely generated modules, earlier: a ﬁnitely generated
ideal is an example.
We require R to be a domain when discussing “torsion elements”4 since the set R −{0} needs
to be closed under multiplication in order for the concept of “torsion element” to be useful; e.g.,
if rm = 0 with r ̸= 0 and r′m′ = 0 with r′ ̸= 0 then (rr′)(m + m′) = 0 but we then want rr′ to
be nonzero. (For an example of what goes wrong when R isn’t a domain, consider R = Z/6Z as
an R-module, so the set of elements of R annihilated by a nonzero element of R is {0, 2, 3, 4}, and
this is not closed under addition! If we regard R as a Z-module (just an abelian group), then every
element of R is a Z-torsion element.)
Example 4.1. Let G = C×. This is an abelian group, so a Z-module, but written multiplicatively
(each m ∈Z acts on z ∈C× has value zm). Its torsion subgroup is all the roots of unity, an inﬁnite
subgroup.
So the torsion subgroup of an abelian group need not be ﬁnite (unless it is ﬁnitely
generated).
4The word “torsion” means “twistiness”. It entered group theory from algebraic topology: the nonorientability of
some spaces is related to the presence of nonzero elements of ﬁnite order in a homology group of the space. Then it
was natural to use the term torsion to refer to elements of ﬁnite order in an arbitrary abelian group, and replacing
integral multiples with ring multiples led to the term being used in module theory for the analogous concept.

<!-- page 13 -->
INTRODUCTORY NOTES ON MODULES
13
Example 4.2. Let U = Z[
√
2]× = ±(1 +
√
2)Z. This is an abelian group, so a Z-module (think
multiplicatively!). It is generated by {−1, 1 +
√
2} and has torsion subgroup {±1}.
Example 4.3. If I is a nonzero ideal in a domain R, then R/I is a torsion R-module: pick
c ∈I −{0}, and then for all m ∈R/I we have cm = 0 in R/I since Rc ⊂I. As a special case,
Z/kZ is a torsion abelian group when k is nonzero.
Example 4.4. Every vector space V over a ﬁeld F is torsion-free as an F-module: if cv = 0 and
c ̸= 0 then multiplying by c−1 gives c−1(cv) = 0, so (c−1c)v = 0, so v = 0. Thus the only F-torsion
element in V is 0.
The last entry in our table above says that for a domain R, the R-module analogue of a ﬁnite
abelian group is a ﬁnitely generated torsion R-module. One may think at ﬁrst that the module
analogue of a ﬁnite abelian group should be an R-module that is a ﬁnite set, but (for general R)
that is much too restrictive to be a useful deﬁnition.
Another way R-modules extend features of abelian groups is the structure of the mappings
between them. For two abelian groups A and B, written additively, the set of all group homomor-
phisms from A to B is also an abelian group, denoted Hom(A, B), where the sum ϕ + ψ of two
homomorphisms ϕ, ψ: A →B is deﬁned by pointwise addition: (ϕ + ψ)(a) := ϕ(a) + ψ(a). So
the set of all homomorphisms A →B can be given the same type of algebraic structure as A and
B. (This is not true for nonabelian groups. For groups G and H, the pointwise product of two
homomorphisms G →H is not usually a homomorphism if H is nonabelian.) Taking B = A, the
additive group Hom(A, A) is a ring using composition as multiplication.
Something similar happens for two R-modules M and N: the set of all R-linear maps M →N
is an R-module, denoted HomR(M, N), using pointwise addition and scaling, and when we take
N = M the set of R-linear maps M →M is a ring where the multiplication is composition.
Example 4.5. We saw in Example 2.11 that each A ∈Matn×m(R) leads to a function Rm →Rn
given by v 7→Av (the usual product of a matrix and a vector) and this is an R-linear transformation.
It can be shown that all R-linear maps Rm →Rn arise in this way, so HomR(Rm, Rn) ∼= Matn×m(R)
as R-modules. Similarly, HomR(Rn, Rn) ∼= Matn(R) as rings.
The ring structure on Hom(M, M) (all homomorphisms of M as an abelian group) gives a concise
abstract way to deﬁne what an R-module is. For each r ∈R, the scaling map m 7→rm on M is a
group homomorphism, and the axioms of an R-module are exactly that the map R →Hom(M, M)
associating to each r the function “multiply by r” is a ring homomorphism: the second axiom says
m 7→rm is in Hom(M, M) and the ﬁrst and third axioms say that sending r to “multiply elements
of M by r” is additive and multiplicative and preserves multiplicative identities. So an R-module
“is” an abelian group M together with a speciﬁed ring homomorphism R →Hom(M, M), with the
image of each r ∈R in Hom(M, M) being interpreted as the mapping “multiply by r” on M. This
is analogous to saying an action of a group G on a set X “is” a group homomorphism G →Sym(X).

<!-- page 14 -->
14
KEITH CONRAD
5. Isomorphisms of ideals as modules
Let’s take a look at the meaning of isomorphisms of modules in the context of ideals in a ring: for
ideals I, J ⊂R, when are I and J isomorphic as R-modules (i.e., when does there exist a bijective
R-linear map between I and J)?
Example 5.1. Let I = 2Z and J = 3Z in Z. Let ϕ: I →J by ϕ(x) = (3/2)x. (Even though
3/2 ̸∈Z we still have ϕ(I) ⊂J.) This is an isomorphism of Z-modules.
Even when two ideals are not principal, the simple scaling idea in the previous example completely
accounts for how two ideals could be isomorphic modules, at least in a domain:
Theorem 5.2. If R is a domain with fraction ﬁeld K, then ideals I and J in R are isomorphic
as R-modules if and only if I = cJ for some c ∈K×. In particular, I ∼= R as an R-module if and
only if I is a nonzero principal ideal.
Proof. When I ∼= J or when I = cJ for some c ∈K×, I = 0 if and only if J = 0, so we may
suppose now that I, J ̸= 0.
If I = cJ for some c ∈K×, then ϕ: I →J by ϕ(x) = 1
cx is R-linear: it is obviously additive and
ϕ(rx) = 1
crx = rϕ(x). Also, ϕ is a bijection with inverse ϕ−1 : J →I deﬁned by ϕ−1(y) = cy. So
I ∼= J as R-modules.
Now suppose, conversely, there is an R-module isomorphism ϕ: I →J. We seek c ∈K× such
that ϕ(x) = cx for all x ∈I. We’ll use the following trick: for all x, x′ ∈I, they are in R so
ϕ(xx′) = xϕ(x′) = x′ϕ(x).
In K, if x, x′ ̸= 0, we get
ϕ(x)
x
= ϕ(x′)
x′
.
So set c = ϕ(x)/x ∈K× where x ∈I −{0}; we just saw that this is independent of x. Then
ϕ(x) = cx for all x ∈I −{0}: this is obvious if x = 0 and holds by design of c if x ̸= 0. Thus,
J = ϕ(I) = cI.
Taking J = R, we have as a special case I ∼= R as an R-module if and only if I = cR for some
c ∈K×. Necessarily c = c · 1 ∈cR = I ⊂R, so I = cR with c ∈R −{0}. Such I are the nonzero
principal ideals in R.
□
Example 5.3. Let R = Z[√−5], p = (3, 1 + √−5) and q = (3, 1 −√−5). Complex conjugation is
Z-linear and from the description
p =

3a + (1 +
√
−5)b : a, b ∈Z[
√
−5]
	
we get p = (3, 1 −√−5) = q. So p and q are isomorphic as Z-modules since complex conjugation
is a Z-module isomorphism.
But are p and q isomorphic as R-modules? Complex conjugation on R is not R-linear (since cx
is equal to c x rather than equal to cx), so the isomorphism we gave between p and q as Z-modules

<!-- page 15 -->
INTRODUCTORY NOTES ON MODULES
15
doesn’t tell us how things go as R-modules. In any event, if p and q are to be somehow isomorphic
as R-modules then we deﬁnitely need a new bijection between them to show this! The previous
theorem tells us that the only way p and q can be isomorphic R-modules is if there is a nonzero
element of the fraction ﬁeld Q[√−5] that scales p to q, and it is not clear what such an element
might be.
It turns out that p and q are isomorphic as R-modules,5 with one isomorphism ϕ: p →q being
ϕ(x) = 2 + √−5
3
x.
(Of course this is also a Z-module isomorphism.) The way this isomorphism is discovered involves
some concepts in algebraic number theory. Here is a variant, also explained by algebraic number
theory, where the opposite conclusion holds: consider R′ = Z[√−14] and the ideals
p′ = (3, 1 +
√
−14)
and
q′ = (3, 1 −
√
−14)
that satisfy p′ = q′, so p′ ∼= q′ as Z-modules using complex conjugation. It turns out that p′ and q′
are not isomorphic as R′-modules, but proving that requires some work.
6. Applications to linear algebra
Example 6.1. Let V = R2. This is an R-vector space. It has a two-element spanning set over R;
e.g., ( 1
0 ) , ( 0
1 ). It is torsion-free as an R-module, as are all vector spaces (Example 4.4). But when
we introduce a matrix A acting on V , we can turn V into a ﬁnitely generated torsion module over
the domain R[T]. Here’s how that works.
Let A = ( 3 2
5 4 ). The eﬀect of A on R2 lets us put an action of R[T] on R2 through polynomial
values at A: for f(T) ∈R[T] and v ∈R2 declare
f(T) · v = f(A)v.
Concretely, T · v = Av, T 2 · v = A2v, and (T 2 −T) · v = (A2 −A)v. Check this makes V into an
R[T]-module, We can use as A an arbitrary matrix and we still get an R[T]-module structure on
V , but it might be a diﬀerent (nonisomorphic) R[T]-module for diﬀerent choices of A.
To get a feel for what making R2 into an R[T]-module gives us, let’s see that we can get anywhere
in R2 from the single vector ( 1
0 ) using the scalar multiplication by R[T] based on making T act
as the preceding explicit A (so R2 becomes a cyclic R[T]-module, no longer needing a 2-element
spanning set as it did when viewed as a vector space over R). For every vector
 x
y

, we will ﬁnd
a, b ∈R such that
(aT + b) ·
 
1
0
!
=
 
x
y
!
.
5The ideals (2, 1 + √−5) and (2, 1 −√−5) are also isomorphic R-modules, but something even stronger holds: they
are equal since the generators of each ideal are in the other ideal. This is from 1 + √−5 + 1 −√−5 = 2.

<!-- page 16 -->
16
KEITH CONRAD
This is the same as requiring6
  
3a
2a
5a
4a
!
+ bI2
!  
1
0
!
=
 
x
y
!
,
which means
 3a+b
5a

=
 x
y

. That is, we want 3a + b = x and 5a = y, which is to say a = y/5 and
b = x −3y/5. So
x
y

=
y
5T + x −3
5y
  
1
0
!
.
Thus when we view R2 as an R[T]-module in this way using A,
 1
0

is a generator of this module.
The characteristic polynomial of A is
χA(T) = det(T · I2 −A)
= det
  
T
0
0
T
!
−
 
3
2
5
4
!!
= det
 
T −3
−2
−5
T −4
!
= T 2 −7T + 2.
The Cayley-Hamilton theorem says the matrix A is killed by χA(T): χA(A) = A2−7A+2I2 = ( 0 0
0 0 ).
Therefore when we view R2 as an R[T]-module through the action of A on vectors, R2 is a
torsion module because the nonzero polynomial T 2 −7T + 2 ∈R[T] kills everything in V = R2:
(T 2 −7T + 2) · v = (A2 −7A + 2I2)v = Ov = 0.
Let’s compare: as an R-vector space, R2 is ﬁnitely generated and torsion-free, but as an R[T]-
module where T acts via A = ( 3 2
5 4 ), R2 is a ﬁnitely generated (cyclic) torsion module.
Example 6.2. If instead we take A = ( 1 0
0 1 ) then we can make R2 into an R[T]-module by letting
T act as the identity matrix: f(T) · v = f(I2)v. Now
f(I2) =
 
f(1)
0
0
f(1)
!
,
so f(I2)v = f(1)v is just a scalar multiple of v. Thus the only place that the new scalar mul-
tiplication by R[T] can move a given vector is to an R-multiple of itself. Therefore R2 in this
new R[T]-module structure is not a cyclic module as it was in the previous example. But R2 is
still ﬁnitely generated as an R[T]-module (the standard basis is a spanning set) and it is a torsion
module since (T −1)v = I2v −v = 0 (so all elements are killed by T −1).
Studying linear operators on Rn from the viewpoint of torsion modules over R[T] is the key
to unlocking the structure of matrices in a conceptual way because the structure theory for ﬁnite
abelian groups carries over to ﬁnitely generated torsion modules over a PID (like R[T]).
For
6When we substitute A for T in a polynomial f(T), the constant term c0 becomes c0I2.

<!-- page 17 -->
INTRODUCTORY NOTES ON MODULES
17
example, every ﬁnitely generated torsion module over a PID is a direct sum of cyclic modules,
generalizing the fact that any ﬁnite abelian group is a direct sum of cyclic groups.
Let’s now revisit the topic of isomorphisms of modules, this time with vector spaces over a
ﬁeld F viewed as F[T]-modules using an F-linear operator in the role of T-multiplication. Say
A, B ∈Matn(F) where F is a ﬁeld and n ≥1. Generalizing Examples 6.1 and 6.2, we can view
V = F n as an F[T]-module in two ways, by letting the action of T on V be A or B:
(6.1)
f(T) · v = f(A)(v)
or
(6.2)
f(T) · v = f(B)(v)
for f(T) ∈F[T]. Let VA be V with scalar multiplication by F[T] as in (6.1) (so T ·v = Av) and let
VB be V with scalar multiplication by F[T] as in (6.2) (T · v = Bv). Whether or not VA and VB
are isomorphic F[T]-modules turns out to be equivalent to whether or not A and B are conjugate
matrices:
Theorem 6.3. As F[T]-modules, VA ∼= VB if and only if B = UAU−1 for some U ∈GLn(F).
Proof. The proof will be almost entirely a matter of unwinding deﬁnitions.
Suppose ϕ: VA →VB is an F[T]-module isomorphism. This means ϕ is a bijection and
ϕ(v + v′) = ϕ(v) + ϕ(v′),
ϕ(f(T) · v) = f(T) · ϕ(v)
for all v, v′ ∈V and f(T) ∈F[T]. The second equation is the same as ϕ(f(A)v) = f(B)ϕ(v).
Polynomials are sums of monomials and knowing multiplication by T determines multiplication
by T i for all i ≥1, so the above conditions on ϕ are equivalent to
ϕ(v + v′) = ϕ(v) + ϕ(v′),
ϕ(cv) = cϕ(v),
ϕ(T · v) = T · ϕ(v)
for all v and v′ in V and c in F. The ﬁrst two equations say ϕ is F-linear and the last equation
says ϕ(Av) = Bϕ(v) for all v ∈V . So ϕ: V →V is an F-linear bijection and ϕ(Av) = Bϕ(v)
for all v ∈V . Since V = F n, every F-linear map ϕ: V →V is a matrix transformation: for some
U ∈Matn(F),
ϕ(v) = Uv.
Indeed, if there were such a matrix U then letting v run over the standard basis e1, . . . , en tells us the
i-th column of U is ϕ(ei), so turn around and deﬁne U to be the matrix [ϕ(e1) · · · ϕ(en)] ∈Matn(F)
having ith column ϕ(ei). Then ϕ and U have the same values on the ei’s and both are linear on
F n, so they have the same value at every vector in F n. Since ϕ is a bijection, U is invertible, i.e.,
U ∈GLn(F). Now the condition ϕ(Av) = Bϕ(v) for all v ∈V means
U(Av) = B(Uv) ⇐⇒Av = U−1BUv
for all v ∈V = F n. Letting v = e1, . . . , en tells us that A and U−1BU have the same ith column
for all i, so they are the same matrix: A = U−1BU, so B = UAU−1.

<!-- page 18 -->
18
KEITH CONRAD
Conversely, suppose there is an invertible matrix U ∈GLn(F) with B = UAU−1.
Deﬁne
ϕ: VA →VB by ϕ(v) = Uv. This is a bijection since U is invertible. It is also F-linear. To show
ϕ(f(T) · v) = f(T) · ϕ(v)
for all v ∈V and f(T) ∈F[T], it suﬃces by F-linearity to check
ϕ(T i · v) = T i · ϕ(v)
for all v ∈V and for i ≥0. For this to hold, it suﬃces to check ϕ(T · v) = T · ϕ(v) for all v ∈V .
This last condition just says ϕ(Av) = Bϕ(v) for all v ∈V . Since B = UAU−1, UA = BU, so
ϕ(Av) = U(Av) = (UA)v = (BU)v = B(Uv) = Bϕ(v)
for all v ∈V . What we wanted to check is true, so we are done.
□
Not only did this proof show an F[T]-module isomorphism of VA to VB exists exactly when
A and B are conjugate matrices in Matn(F), but it showed us the isomorphisms are exactly the
invertible matrices that conjugate A to B (solutions U of B = UAU−1).
The importance of
this theorem is that it places the“conjugation problem” for matrices in Matn(F) (the problem of
deciding when two matrices are conjugate) into the mainstream of abstract algebra as a special case
of the “isomorphism problem” for modules over F[T] (the problem of deciding when two modules
are isomorphic). The ring F[T] is a PID, and this viewpoint leads to a solution (called “rational
canonical form”) of the isomorphism problem for ﬁnitely generated torsion F[T]-modules, which
leads to a solution of the conjugation problem for matrices over a ﬁeld.
More generally, for each commutative ring R and matrices A and B in Matn(R), we can make
Rn into an R[T]-module in two ways (letting f(T) act on Rn as f(A) or as f(B)) and reasoning
as in the preceding calculations shows that these R[T]-module structures on Rn are isomorphic if
and only if B = UAU−1 for some U ∈GLn(R).7 These two module structures on Rn are torsion
thanks to the Cayley–Hamilton theorem in Matn(R). Thus the conjugation problem in Matn(R)
for a general commutative ring R is special case of the isomorphism problem for ﬁnitely generated
torsion R[T]-modules. Unfortunately, R[T] when R is not a ﬁeld is usually too complicated for
there to be a nice classiﬁcation of the ﬁnitely generated torsion R[T]-modules. Even the case when
R = F[X] for a ﬁeld F, so R[T]-modules are can be thought of as F[X, Y ]-modules, is very hard.
For example, see https://math.stackexchange.com/questions/641169/.
7The group GLn(R) of invertible matrices consists of exactly those U ∈Matn(R) where det U ∈R×, which is not
the condition det U ̸= 0 except when R is a ﬁeld (precisely the case when R× = R −{0}).

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*