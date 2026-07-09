# Discriminants and Ramified Primes

> **Source**: https://kconrad.math.uconn.edu/blurbs/disc.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
DISCRIMINANTS AND RAMIFIED PRIMES
KEITH CONRAD
1. Introduction
A prime number p is said to be ramiﬁed in a number ﬁeld K if the prime ideal factorization
(1.1)
(p) = pOK = pe1
1 · · · peg
g
has some ei greater than 1. If every ei equals 1, we say p is unramiﬁed in K.
Example 1.1. In Z[i], the only prime that ramiﬁes is 2: (2) = (1 + i)2.
Example 1.2. Let K = Q(α) where α is a root of f(T) = T 3 −9T −6.
Then 6 =
α3 −9α = α(α −3)(α + 3). For m ∈Z, α + m has minimal polynomial f(T −m) in Q[T],
so NK/Q(α + m) = −f(−m) = m3 −9m + 6 and the principal ideal (α −m) has norm
N(α −m) = |m3 −9m + 6|.
Therefore N(α) = 6, N(α −3) = 6, and N(α + 3) = 6.
It follows that (α) = p2p3,
(α −3) = p′
2p3, and (α + 3) = p′
2p3 (so, in particular, α + 3 and α −3 are unit multiples of
each other). Thus
(2)(3) = (6) = (α)(α −3)(α + 3) = p2p′2
2 p3
3,
so (2) = p2
2p′
2 and (3) = p3
3. This shows 2 and 3 are ramiﬁed in K. Note that one of the
exponents in the factorization of (2) exceeds 1 while the other equals 1.
One way to think about ramiﬁed primes is in terms of the ring structure of OK/(p). By
(1.1) and the Chinese Remainder Theorem,
(1.2)
OK/(p) ∼= OK/pe1
1 × · · · × OK/peg
g .
If some ei is greater than 1, then the quotient ring OK/pei
i has a nonzero nilpotent element
(use the reduction modulo pei
i
of any element of pi −pei
i ), so the product ring (1.2) has a
nonzero nilpotent element. If each ei equals 1, then OK/(p) is a product of (ﬁnite) ﬁelds,
and a product of ﬁelds has no nonzero nilpotent elements. Thus, p ramiﬁes in K if and only
if OK/(p) has a nonzero nilpotent element.
In Sections 2 and 3 we will prove the following result of Dedekind [2], which characterizes
the prime numbers ramifying in a number ﬁeld K in terms of its discriminant.1
Theorem 1.3 (Dedekind). For a number ﬁeld K, a prime p ramiﬁes in K if and only if p
divides the integer discZ(OK).
Recall discZ(OK) := discK/Q(α1, . . . , αn) where {α1, . . . , αn} is any Z-basis of OK. The
generalization of Theorem 1.3 to a relative extension of number ﬁelds is in Section 4.
1In [1, pp. 36-37], Dedekind said he announced this result for the ﬁrst time on September 20, 1871.
1

<!-- page 2 -->
2
KEITH CONRAD
2. A special case
We will ﬁrst consider Theorem 1.3 in the special case that there is an α ∈OK such that
K = Q(α) and p ∤[OK : Z[α]]. (If OK = Z[α] we can use the same α for all p.) The
treatment of the general case in Section 3 will not rely on the case that p ∤[OK : Z[α]]
for some α, but this special case is technically simpler. We will just sketch the basic ideas
behind it.
Proof. Assume for a prime p that there’s α ∈OK such that K = Q(α) and p ∤[OK : Z[α]].
Let f(T) be the minimal polynomial of α over Q, so f(T) is monic in Z[T].
and the
Dedekind–Kummer theorem tells us that the way pOK factors into prime ideals matches
the way f(T) mod p factors into monic irreducibles in (Z/pZ)[T].
Writing the prime ideal factorization of pOK as in (1.1), by deﬁnition p ramiﬁes in OK
if and only if some ei > 1. The factorization of the mod p reduction f(T) in (Z/pZ)[T]
matches (1.1), in the sense that
f(T) = πe1
1 · · · · πeg
g
for some distinct monic irreducibles πi ∈(Z/pZ)[T].
The irreducible polynomials πi(T)’s are separable (all irreducibles over a ﬁnite ﬁeld are
separable), so some ei > 1 if and only if f(T) has a repeated root in a splitting ﬁeld over
Z/pZ. This is equivalent to f(T) having discriminant 0, so p ramiﬁes in OK if and only if
disc(f) = 0 in Z/pZ.
Since the discriminant of a monic polynomial is a universal polynomial in its coeﬃcients
(consider the quadratic case, where T 2 + bT + c has discriminant b2 −4c), discriminants
of monic polynomials behave well under reduction: disc(f(T) mod p) = disc(f(T)) mod p.
Therefore disc(f(T)) = 0 in Z/pZ if and only if disc(f) ≡0 mod p. Thus p ramiﬁes in OK
if and only if p | disc(f). Since
disc(f) = disc(Z[α]) = [OK : Z[α]]2 discZ(OK)
and p ∤[OK : Z[α]], we have p | disc(f) if and only if p | discZ(OK).
□
3. The general case
To prove Theorem 1.3 for every prime number p, even if p | [OK : Z[α]] for all α ∈OK
such that K = Q(α),2 we will examine discriminants of ring extensions to show computing
the discriminant commutes with reduction mod p: discZ(OK) mod p = discZ/pZ(OK/(p)).
Then we will use (1.2) to write discZ/pZ(OK/(p)) as a product of discriminants of rings of
type OK/pe and compute the discriminants of these particular rings.
Deﬁnition 3.1. Let A be a commutative ring and B be a ring extension of A that is a
ﬁnite free A-module:
B = Ae1 ⊕· · · ⊕Aen.
Then we set
discA(e1, . . . , en) = det(TrB/A(eiej)) ∈A.
2Dedekind wrote in [1, p. 37] that he ﬁrst proved Theorem 1.3 in the special case of Section 2 above and
was able to prove the general case only after many unsuccessful attempts. He presented the special case ﬁrst
in [2, §3] since it’s much simpler than the method he used for the general case in [2, §§4-6].

<!-- page 3 -->
DISCRIMINANTS AND RAMIFIED PRIMES
3
Remark 3.2. The discriminant of a basis is an algebraic concept of “volume”. To explain
this viewpoint, we should think about TrB/A(xy) as an analogue of the dot product v · w in
Rn. For a basis v1, . . . , vn in Rn, the ordinary Euclidean volume of the parallelotope
( n
X
i=1
aivi : 0 ≤ai ≤1
)
having edges vi is
p
| det(vi · vj)|. The discriminant of an A-basis of B uses the A-valued
pairing ⟨x, y⟩= TrB/A(xy) on B in place of the R-valued dot product on Rn and we just
drop the absolute value and the square root when we make the algebraic analogue.
How are the discriminants of two A-module bases for B related? Pick a second basis
e′
1, . . . , e′
n of B as an A-module. Then
e′
i =
n
X
j=1
aijej,
where aij ∈A and the change of basis matrix (aij) has determinant in A×. Then
TrB/A(e′
ie′
j) = TrB/A
 n
X
k=1
aikek
n
X
ℓ=1
ajℓeℓ
!
=
n
X
k=1
n
X
ℓ=1
aik TrB/A(ekeℓ)ajℓ,
so
(TrB/A(e′
ie′
j)) = (aij)(TrB/A(eiej))(aij)⊤.
Therefore
discA(e′
1, . . . , e′
n) = (det(aij))2 discA(e1, . . . , en).
We set
discA(B) = discA(e1, . . . , en) ∈A
for any A-module basis {e1, . . . , en} of B. It is well-deﬁned up to a unit square. In particular,
the condition discA(B) = 0 is independent of the choice of basis.
Given a number ﬁeld K, ramiﬁcation of the prime p in K has been linked to the structure
of the ring OK/(p) in Section 1. Let’s look at the discriminant of this ring over Z/pZ. Letting
K have degree n over Q, the ring OK is a free rank-n Z-module, say
OK =
n
M
i=1
Zωi.
Reducing both sides modulo p,
OK/(p) =
n
M
i=1
(Z/pZ)ωi,
so OK/(p) is a vector space over Z/pZ of dimension n. The discriminant of OK is discZ(OK).
The next lemma says reduction modulo p commutes (in a suitable sense) with the formation
of discriminants.
Lemma 3.3. Choosing bases appropriately for OK and OK/(p),
discZ(OK) mod p = discZ/pZ(OK/(p)).

<!-- page 4 -->
4
KEITH CONRAD
Proof. Pick a Z-basis ω1, . . . , ωn of OK. The reductions ω1, . . . , ωn in OK/(p) are a Z/pZ-
basis, so the multiplication matrix [mx] for any x ∈OK, with respect to the basis {ωi},
reduces modulo p to the multiplication matrix [mx] for x on OK/(p) with respect to the
basis {ωi}. Therefore
Tr(OK/(p))/(Z/pZ)(x) = Tr(mx) = Tr(mx) mod p = TrOK/Z(x) mod p.
Thus, the mod p reduction of the matrix (TrOK/Z(ωiωj)) is (Tr(OK/(p))/(Z/pZ)(ωiωj)). Now
take determinants.
□
Lemma 3.4. Let A be a commutative ring and B1 and B2 be commutative ring extensions
of A that are each ﬁnite free A-modules. Then, choosing A-module bases appropriately,
discA(B1 × B2) = discA(B1) discA(B2).
Proof. Pick A-module bases for B1 and B2:
B1 =
m
M
i=1
Aei,
B2 =
n
M
j=1
Afj.
As an A-module basis for B1 × B2 we will use the m + n elements e1, . . . , em, f1, . . . , fn.
Since eifj = 0 in B1 × B2, the matrix whose determinant is discA(B1 × B2) is a block
diagonal matrix
(Tr(B1×B2)/A(eiek))
O
O
(Tr(B1×B2)/A(fjfℓ))

.
For any x ∈B1, multiplication by x on B1 × B2 kills the B2 component and acts on the
B1-component in the way x multiplies on B1, so a matrix for multiplication by x on B1×B2
is a matrix whose upper left block is a matrix for multiplication by x on B1 and other blocks
are 0. Thus
Tr(B1×B2)/A(x) = TrB1/A(x) for x ∈B1.
Similarly, Tr(B1×B2)/A(x) = TrB2/A(x) for x ∈B2. Thus
(Tr(B1×B2)/A(eiek))
O
O
(Tr(B1×B2)/A(fjfℓ))

=
(TrB1/A(eiek))
O
O
(TrB2/A(fjfℓ))

,
and taking determinants gives
discA(B1 × B2) = discA(B1) discA(B2).
□
Now we prove Theorem 1.3.
Proof. We have p | discZ(OK) if and only if discZ(OK) ≡0 mod p. By Lemma 3.3
discZ(OK) mod p = discZ/pZ(OK/(p)),
so p | discZ(OK) if and only if discZ/pZ(OK/(p)) = 0 in Z/pZ.
In (1.2), each factor OK/pei
i is a Z/pZ-vector space since p ∈pei
i . Using (1.2) and Lemma
3.4,
discZ/pZ(OK/(p)) =
g
Y
i=1
discZ/pZ(OK/pei
i ).
Therefore we need to show for any prime number p and prime-power ideal pe such that
pe | (p) that discZ/pZ(OK/pe) is 0 in Z/pZ if and only if e > 1. (Recall that the vanishing
of a discriminant is independent of the choice of basis.)

<!-- page 5 -->
DISCRIMINANTS AND RAMIFIED PRIMES
5
Suppose e > 1. Then any x ∈p −pe is a nonzero nilpotent element in OK/pe. By linear
algebra over ﬁelds, such an x can be used as part of a Z/pZ-basis of OK/pe, say {x1, . . . , xn}
with x = x1. Writing the trace map Tr(OK/pe)/(Z/pZ) as Tr for short, the ﬁrst column of the
matrix (Tr(xixj)) contains the numbers Tr(xix). These traces are all 0: xix is nilpotent,
so the linear transformation mxix on OK/pe is nilpotent and thus its eigenvalues all equal
zero. Since one column of the trace-pairing matrix (Tr(xixj)) is all 0, discZ/pZ(OK/pe) = 0.
Now suppose e = 1. Then OK/pe = OK/p is a ﬁnite ﬁeld of characteristic p. We want
to prove discZ/pZ(OK/p) ̸= 0. If this discriminant is 0, then (because OK/p is a ﬁeld) the
trace function Tr: OK/p →Z/pZ is identically zero. However, from the theory of ﬁnite
ﬁelds, this trace function can be written as a polynomial function:
Tr(t) = t + tp + tp2 + · · · + tpr−1,
where pr = |OK/p|. Since Tr(t) as a polynomial in t has smaller degree than the size of
OK/p, the function Tr(t) is not identically zero on OK/p. Therefore the discriminant of a
ﬁnite extension of Z/pZ does not equal zero.
□
4. The relative case
Ramiﬁed primes and discriminants can be deﬁned for an extension of number ﬁelds E/F
where the base ﬁeld F need not be Q. This is called the relative case, while the study of
number ﬁeld extensions with base ﬁeld Q is called the absolute case.
To deﬁne the discriminant of E/F, a direct copying of the deﬁnition over Q is possible
if OF is PID. In this case OE is a free OF -module. We say a prime π in OF is ramiﬁed in E
when the ideal πOE has a repeated prime ideal factor and is unramiﬁed otherwise. When
{α1, . . . , αn} is an OF -basis of OE the number discE/F (α1, . . . , αn) is nonzero in OF and
changing the OF -basis of OE changes this number by a unit square in OF .
Example 4.1. Let F = Q(i) and E = F(√−5). Then OF = Z[i] and it can be shown that
OE = OF [√−5] = Z[i][√−5], so {1, √−5} is a Z[i]-basis of OE. Since
discE/F (1,
√
−5) = det

TrE/F (1 · 1)
TrE/F (1 · √−5)
TrE/F (√−5 · 1)
TrE/F (√−5√−5)

= det

2
0
0
−10

= −20,
the discriminant of E/F is −20 up to a unit square in Z[i]. Another Z[i]-basis of OE is
{i, √−5} and discE/F (i, √−5) = det( −2
0
0 −10 ) = 20, which diﬀers from −20 by a unit square
factor −1 = i2.
Numbers in a PID that diﬀer by a unit factor have the same prime factors, so whether or
not a prime in OF divides discE/F (α1, . . . , αn) does not depend on the choice of OF -basis.
Here is how Theorem 1.3 generalizes to E/F when OF is a PID.
Theorem 4.2. For an extension of number ﬁelds E/F where OF is a PID, a prime π in F
ramiﬁes in E if and only if π divides discE/F (α1, . . . , αn) where {α1, . . . , αn} is an OF -basis
of OE.
Proof. Use the method of proof of Section 3 with Z replaced by OF .
□
Example 4.3. In Example 4.1, 20 has prime factorization −(1 + i)4(1 + 2i)(1 −2i), in Z[i]
so the primes in Z[i] that ramify in Z[i, √−5] are 1 + i, 1 + 2i, and 1 −2i.
What do we do when OF is not necessarily a PID? A (nonzero) prime ideal p in OF , is
called ramiﬁed in E if the ideal pOE has a repeated prime ideal factor in OE and unramiﬁed

<!-- page 6 -->
6
KEITH CONRAD
otherwise. It can be shown that when E = F(α) with α ∈OE and α has minimal polynomial
f(T) in F[T], the prime p is unramiﬁed in E if (but not necessarily only if) disc(f(T)) ̸≡
0 mod p. A nonzero number in OF has only ﬁnitely many prime ideal factors, so all but
ﬁnitely many prime ideals in OF are unramiﬁed in E.
The discriminant of E/F is an ideal in OF , called the discriminant ideal dE/F . It is deﬁned
as the ideal in OF generated by the numbers discE/F (α1, . . . , αn) where {α1, . . . , αn} runs
over all F-bases of E that are contained in OE.3 If one F-basis of E contained in OE is
in the OF -span of another F-basis of E contained in OE, then the discriminant of the ﬁrst
basis is a multiple of the discriminant of the second basis, so if OE has an OF -basis, then
dE/F is a principal ideal with the discriminant of any OF -basis of OE being a generator.
Theorem 1.3 has the following generalization to the relative case, whose proof is more
technical than that of Theorem 1.3 and is omitted.
Theorem 4.4. For an extension of number ﬁelds E/F, a prime p in F ramiﬁes in E if
and only if p divides the discriminant ideal dE/F .
References
[1] R. Dedekind, ¨Uber den Zusammenhang zwischen der Theorie der ideale und der Theorie der h¨oheren
Congruenzen, Abhandlungen der K¨oniglichen Gesellschaft der Wissenschaften in G¨ottingen 23 (1878),
3–37. URL https://eudml.org/doc/135827.
[2] R. Dedekind, ¨Uber die Discriminanten endlicher K¨orper, Abhandlungen der K¨oniglichen Gesellschaft
der Wissenschaften in G¨ottingen 29 (1882), 1–56. URL https://eudml.org/doc/135869.
3The ideal dE/F can be deﬁned in a second way using localizations: see https://math.stackexchange.
com/questions/4875752/. Some work is needed to show this way of deﬁning dE/F agrees with the ﬁrst way
presented above.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*