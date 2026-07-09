# Affineheisrep

> **Source**: https://kconrad.math.uconn.edu/blurbs/affineheisrep.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
REPRESENTATIONS OF Aﬀ(Fq) AND Heis(Fq)
KEITH CONRAD
For each prime power q, we will construct all irreducible representations over C of the
groups Aﬀ(Fq) and Heis(Fq). To ﬁnd all of them, there are three parts:
• build as many irreducible representations as the number of conjugacy classes,
• show a representation is irreducible by checking its character has inner product 1
with itself (1-dimensional representations are automatically irreducible),
• show irreducible representations are nonisomorphic by checking their characters are
diﬀerent.
1. Representations of Aﬀ(Fq)
Let F be a ﬁeld. In Aﬀ(F), the group law is

a
b
0
1
 
a′
b′
0
1

=

aa′
ab′ + b
0
1

,

a
b
0
1
−1
=

1/a
−b/a
0
1

.
The notation Aﬀmeans “aﬃne,” which is the label in higher math for functions of the form
f(x) = ax + b,1 and such functions with a ̸= 0 compose in the same way matrices ( a b
0 1 )
multiply.
Two subgroups of Aﬀ(F) are

a
0
0
1

: a ̸= 0

,

1
b
0
1

: b ∈F

,
which are isomorphic to F × and F as groups. Matrices in Aﬀ(F) decompose into a product
of elements in these subgroups as

a
b
0
1

=

1
b
0
1
 
a
0
0
1

.
The product in the other order doesn’t work in the same way:

a
0
0
1
 
1
b
0
1

=

a
ab
0
1

.
Conjugation in Aﬀ(F) is
(1.1)

x
y
0
1
 
a
b
0
1
 
x
y
0
1
−1
=

a
bx −y(a −1)
0
1

.
By (1.1), Aﬀ(F) has trivial center unless F = F2, in which case Aﬀ(F) is abelian.2
Here are the conjugacy classes in Aﬀ(F):
1In school, functions ax + b are called linear, but in higher math such functions are linear only when
b = 0. Thus higher math needs a new name for ax + b when b might not be 0, and that name is “aﬃne
function”.
2Use x = y = 1 to see a matrix in the center of Aﬀ(F) has a = 1. If F ̸= F2, so F × ̸= {1}, then use
y = 0 and x ̸= 1 to see a matrix in the center of Aﬀ(F) has b = 0.
1

<!-- page 2 -->
2
KEITH CONRAD
• the identity matrix

1
0
0
1

,
• the set

1
b
0
1

: b ∈F ×

,
• for each a ∈F with a ̸= 0 and a ̸= 1, the set

a
b
0
1

: b ∈F

.
Taking F = Fq, in Aﬀ(Fq) there are a total of 1 + 1 + (q −2) = q conjugacy classes and
thus there are q irreducible representations of Aﬀ(Fq) over C.
One-dimensional representations: Since the upper left entry in Aﬀ(Fq) behaves
multiplicatively in the group law, for each homomorphism χ: F×
q →C× we get a one-
dimensional representation Aﬀ(Fq) →C× by

a
b
0
1

7→χ(a).
Since F×
q is cyclic of order q −1, there are q −1 such χ, so we get q −1 one-dimensional
representations of Aﬀ(Fq).
Remaining irreducible representation: From the count of conjugacy classes there is
one more irreducible representation of Aﬀ(Fq). Letting d denote its degree, from q−1+d2 =
| Aﬀ(Fq)| = q(q −1) we get d = q −1, so we seek a (q −1)-dimensional representation.
Consider the complex vector space V of functions f : Fq →C. This is q-dimensional. Let
each g ∈Aﬀ(Fq) act on V as a linear change of variables using g−1: (ρV (g)f)(x) = f(g−1x).
We need g−1 rather than g in the formula to get ρV (gh) = ρV (g)ρV (h). Explicitly,
(ρV ( a b
0 1 )f)(x) = f
1
ax −b
a

.
The constant functions in V form a one-dimensional subspace on which Aﬀ(Fq) acts trivially.
Another Aﬀ(Fq)-stable subspace of V is
W =


f ∈V :
X
x∈Fq
f(x) = 0



and ρV = ρW ⊕1, where ρW is the restriction of ρV to W. The dimension of W is q −1.
To show W is irreducible, we compute its character from that of V : χV = χW + 1. A
basis of V is the q delta-functions δt : Fq →C for t ∈Fq, where δt(x) is 0 for x ̸= t and
δt(t) = 1. Since ρV ( a b
0 1 )δt = δat+b, the matrix for ρV ( a b
0 1 ) with respect to the delta-basis of
V is a permutation matrix that describes how t 7→at + b permutes Fq. Thus
χV

a
b
0
1

= |{t ∈Fq : at + b = t in Fq}| =





1,
if a ̸= 1,
q,
if a = 1 and b = 0,
0,
if a = 1 and b ̸= 0.
Therefore
χW

a
b
0
1

= χV

a
b
0
1

−1 =





0,
if a ̸= 1,
q −1,
if a = 1 and b = 0,
−1,
if a = 1 and b ̸= 0.

<!-- page 3 -->
REPRESENTATIONS OF Aﬀ(Fq) AND Heis(Fq)
3
The inner product of χW with itself is
1
q(q −1)
X
g
χW (g)χW (g) =
1
q(q −1)((q −1)2 + (q −1)(−1)2) = (q −1)2 + (q −1)
q(q −1)
= 1,
so W is irreducible. It is a new irreducible representation since it’s not 1-dimensional, except
if q = 2, in which case ρW is nontrivial while the single one-dimensional representation
constructed earlier (q −1 = 1 if q = 2) is trivial (note Aﬀ(F2) ∼= F2).
2. Representations of Heis(Fq)
For a ﬁeld F, the group law in the Heisenberg group Heis(F) is
(2.1)


1
a
b
0
1
c
0
0
1




1
a′
b′
0
1
c′
0
0
1

=


1
a + a′
b + b′ + ac′
0
1
c + c′
0
0
1


with inverse formula


1
a
b
0
1
c
0
0
1


−1
=


1
−a
−b + ac
0
1
−c
0
0
1

.
Three subgroups of Heis(F) are





1
a
0
0
1
0
0
0
1

: a ∈F


,





1
0
b
0
1
0
0
0
1

: b ∈F


,





1
0
0
0
1
c
0
0
1

: c ∈F


,
which are each isomorphic as groups to the additive group of F. Note the subset





1
a
0
0
1
c
0
0
1

: a, c ∈F



is not a subgroup of Heis(F) since it’s not closed under multiplication.
Each matrix in Heis(F) is a product of matrices in the three subgroups above:
(2.2)


1
a
b
0
1
c
0
0
1

=


1
0
0
0
1
c
0
0
1




1
0
b
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
1
a
0
0
1
0
0
0
1

.
If we multiply these three matrices in the reverse order,


1
a
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
1
0
b
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
1
0
0
0
1
c
0
0
1

=


1
a
b + ac
0
1
c
0
0
1

.
Conjugation in Heis(F) is described by the formula
(2.3)


1
x
y
0
1
z
0
0
1




1
a
b
0
1
c
0
0
1




1
x
y
0
1
z
0
0
1


−1
=


1
a
b −az + cx
0
1
c
0
0
1

.
In particular, the center of Heis(F) is
(2.4)





1
0
b
0
1
0
0
0
1

: b ∈F


.

<!-- page 4 -->
4
KEITH CONRAD
Using the conjugation formula (2.3), we get the conjugacy classes in Heis(F):
• for each b ∈F, the single matrix





1
0
b
0
1
0
0
0
1




,
• for each pair (a, c) ∈F 2 −{(0, 0)}, the set





1
a
b
0
1
c
0
0
1

: b ∈F


.
When F = Fq, there are q + (q2 −1) = q2 + q −1 conjugacy classes in Heis(Fq), so this
group has q2 + q −1 irreducible representations over C.
One-dimensional representations: Fix a nontrivial homomorphism ψ: Fq →C×.
An example is ψ(a) = e2πiTrFq/Fp(a), where Fq has characteristic p and TrFq/Fp : Fq →Fp
is the trace map. (If q = p then ψ: Fp →C× by ψ(a) = e2πia/p.) Since the a and c terms
of a matrix in Heis(Fq) each combine additively under multiplication in Heis(Fq), for each
(x, y) ∈F2
q there is a 1-dimensional representation ψx,y : Heis(Fq) →C× given by
(2.5)
ψx,y


1
a
b
0
1
c
0
0
1

= ψ(xa + yc).
Check as an exercise that from ψ: Fq →C× being nontrivial, if ψx,y = ψx′,y′ then (x, y) =
(x′, y′) in F2
q, so {ψx,y : (x, y) ∈F2
q} is q2 irreducible representations of degree 1. (Hint:
ﬁrst show that if x ̸= 0 or y ̸= 0 then ψx,y is nontrivial, i.e., is not identically 1.)
Remaining irreducible representations: The number of remaining irreducible repre-
sentations is (q2+q−1)−q2 = q−1. Their degrees {di} satisfy q2+P d2
i = | Heis(Fq)| = q3,
so P d2
i = q3 −q2 = (q −1)q2. We will ﬁnd q −1 irreducible representations of degree q.
Let V , as before, be the q-dimensional vector space of functions f : Fq →C. We will
deﬁne three actions of Fq on V , and composing them in a suitable order will give an action
of the group Heis(Fq) on V . Fix a nontrivial homomorphism ψ: Fq →C×. For a, b, c ∈Fq,
deﬁne the linear maps σa : V →V , τb : V →V , and ϕc : V →V by
(σaf)(x) = f(x + a),
(τbf)(x) = ψ(b)f(x),
(ϕcf)(x) = ψ(cx)f(x).
For t ∈Fq, note τt multiplies each function in V by the number ψ(t) while ϕt multiplies
each function in V by the function ψ(tx).
Check σa ◦σa′ = σa+a′, τb ◦τb′ = τb+b′, and ϕc ◦ϕc′ = ϕc+c′ as functions V →V , so
a 7→σa, b 7→τb, c 7→ϕc are actions of Fq on V by linear maps. Check τb commutes with
both σa and ϕc, while σa and ϕc commute with each other up to scaling by a root of unity:
(2.6)
σa ◦τb = τb ◦σa,
ϕc ◦τb = τb ◦ϕc,
σa ◦ϕc = ψ(ac)ϕc ◦σa = τac ◦ϕc ◦σa.

<!-- page 5 -->
REPRESENTATIONS OF Aﬀ(Fq) AND Heis(Fq)
5
Using (2.6), the 3-fold composites σa ◦τb ◦ϕc compose as follows:
(σa ◦τb ◦ϕc) ◦(σa′ ◦τb′ ◦ϕc′) = σa ◦τb ◦(ϕc ◦σa′) ◦τb′ ◦ϕc′
= σa ◦τb ◦(τ−a′c ◦σa′ ◦ϕc) ◦τb′ ◦ϕc′
= σa ◦τb−a′c ◦σa′ ◦τb′ ◦ϕc ◦ϕc′
= σa ◦σa′ ◦τb−a′c ◦τb′ ◦ϕc ◦ϕc′
= σa+a′ ◦τb+b′−a′c ◦ϕc+c′.
This is almost like the way matrices in Heis(Fq) multiply in (2.1), and it would match
matrix multiplication if τb+b′−a′c were τb+b′+ac′. Matrices in Heis(Fq) decompose in (2.2)
using reverse alphabetical order, which suggests looking at ϕc◦τb◦σa instead. By calculations
as above,
(ϕc ◦τb ◦σa) ◦(ϕc′ ◦τb′ ◦σa′) = ϕc ◦τb ◦(σa ◦ϕc′) ◦τb′ ◦σa′
= ϕc ◦τb ◦(τac′ ◦ϕc′ ◦σa) ◦τb′ ◦σa′
= ϕc ◦τb+ac′ ◦ϕc′ ◦τb′ ◦σa ◦σa′
= ϕc ◦ϕc′ ◦τb+ac′ ◦τb′ ◦σa ◦σa′
= ϕc+c′ ◦τb+b′+ac′ ◦σa+a′.
This is exactly how matrices in Heis(Fq) multiply, so we can deﬁne a q-dimensional repre-
sentation ρψ of Heis(Fq) on V by
g =


1
a
b
0
1
c
0
0
1

7→ρψ(g) := ϕc ◦τb ◦σa.
As a formula, for f ∈V
(ρψ(g)f)(x) = (ϕcτbσaf)(x) = ψ(cx)(τbσaf)(x) = ψ(cx)ψ(b)f(x + a) = ψ(cx + b)f(x + a).
Let’s compute the character of ρψ. Using the basis {δt : t ∈Fq} of V , we have
g =


1
a
b
0
1
c
0
0
1

=⇒(ρψ(g)δt)(x) = ψ(cx + b)δt(x + a) =
(
ψ(c(t −a) + b),
if x = t −a,
0,
if x ̸= t −a,
so
ρψ(g)δt = ψ(c(t −a) + b)δt−a.
• If a ̸= 0, then the matrix of ρψ(g) with respect to the delta-basis has 0’s on the
main diagonal, so (Tr ρψ)(g) = 0.
• If a = 0, then the matrix of ρψ(g) with respect to the delta-basis has diagonal
entries ψ(ct + b), so (Tr ρψ)(g) = P
t∈Fq ψ(ct + b). If c ̸= 0 then this sum equals
P
x∈Fq ψ(x), which is 0 since ψ is nontrivial, and if c = 0 then this sum is qψ(b).
Thus the character χψ of ρψ is
(2.7)
χψ


1
a
b
0
1
c
0
0
1

=
(
qψ(b),
if a = c = 0,
0,
otherwise,

<!-- page 6 -->
6
KEITH CONRAD
so for each nontrivial homomorphism ψ: Fq →C×, the inner product of χψ with itself is
1
q3
X
g
χψ(g)χψ(g) = 1
q3
X
b∈Fq
qψ(b)qψ(b) = 1
q
X
b∈Fq
1 = 1.
There are q −1 nontrivial homomorphisms ψ: Fq →C×, and to each is a q-dimensional
irreducible representation ρψ of Heis(Fq). To prove ρψ’s for diﬀerent nontrivial ψ are non-
isomorphic, we show their characters χψ are distinct. This is a consequence of the formula
(2.8)
χψ


1
0
b
0
1
0
0
0
1

= qψ(b),
which is a special case of (2.7). It shows we can recover each nontrivial ψ from the character
χψ of the q-dimensional representation ρψ of Heis(Fq). (Alternatively, check for diﬀerent
nontrivial homomorphisms ψ1, ψ2 : Fq →C× that the inner product of the characters of
ρψ1 and ρψ2 is 0, so for diﬀerent nontrivial ψ’s the representations ρψ are nonisomorphic.)
The center of Heis(Fq), by (2.4), is
Zq :=





1
0
b
0
1
0
0
0
1

: b ∈Fq



∼= Fq,
so (2.8) tells us that each q-dimensional irreducible character χψ of Heis(Fq) is determined
by its restriction to Zq, since χψ on Zq is enough information to determine ψ on Fq, which
is all we need to compute χψ on Heis(Fq) in (2.7). In terms of representations rather than
characters, the deﬁnition of ρψ shows that ρψ on Zq is described by
ρψ


1
0
b
0
1
0
0
0
1

= τb : f 7→ψ(b)f
for all functions f ∈V , so ρψ restricted to Zq is enough information to recover ψ on Fq.
Each q-dimensional irreducible representation ρψ of Heis(Fq) is nontrivial on Zq. The
other irreducible representations of Heis(Fq) are 1-dimensional, and they are trivial on Zq
by (2.5).3 Thus the irreducible representations of Heis(Fq) that are nontrivial on Zq are
in bijection with the nontrivial characters of Zq by ρψ 7→ψ; this is an analogue of the
Stone-von Neumann theorem in mathematical physics about representations of Heis(R).4
More on the irreducible representations of Aﬀ(Fq) and Heis(Fq) is in [1, Chap. 16–18].
References
[1] A. Terras, “Fourier Analysis on Finite Groups and Applications,” Cambridge Univ. Press, 1999.
3The commutator subgroup of Heis(Fq) is its center, so that’s another reason 1-dimensional representa-
tions of Heis(Fq) are trivial on the center.
4See https://www-users.cse.umn.edu/∼garrett/m/repns/notes 2014-15/svn theorem.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*