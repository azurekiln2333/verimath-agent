# Noncommutatorsl2

> **Source**: https://kconrad.math.uconn.edu/blurbs/noncommutatorSL2.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
A NONCOMMUTATOR IN SL2
KEITH CONRAD
In a group G, the commutator of two elements g and h is [g, h] := ghg−1h−1. Since
gh = [g, h]hg, we see g and h commute if and only if [g, h] = e. Thus the commutator of
g and h “measures” how far they are from commuting, and G is abelian if and only if all
commutators are trivial.
The set of commutators in G is closed under inversion and conjugation:
[g, h]−1 = (ghg−1h−1)−1 = hgh−1g−1 = [h, g],
(1) k[g, h]k−1 = kghg−1h−1k−1 = (kgk−1)(khk−1)(kg−1k−1)(kh−1k−1) = [kgk−1, khk−1].
However, the set of commutators is not always closed under multiplication.
An example of a group containing a product of commutators that is not a commuta-
tor is SL2(R): in this group −I2 = ( −1
0
0 −1 ) is a product of 4 commutators but is not a
commutator.1 The following theorem is a generalization of this property of −I2.
Theorem 1. Let F be a ﬁeld with more than 3 elements and 2 ̸= 0 in F. In SL2(F), −I2
is a product of 4 commutators, and −I2 is a commutator if and only if −1 = x2 + y2 for
some x and y in F.
This includes F = R since −1 is not a sum of two (or any number of) squares in R.
Saying 2 ̸= 0 in F is reasonable, since if 2 = 0 then −I2 = I2, which is uninteresting.
Proof. In SL2(F), I2 = (( 1 1
0 1 )(
1 0
−2 1 ))2. The matrices ( 1 1
0 1 ) and (
1 0
−2 1 ) are each commuta-
tors: since F has more than three elements it contains a nonzero a such that a2 ̸= 1, and
[( a
0
0 1/a ), ( 1 b
0 1 )] = ( 1 b(a2−1)
0
1
) and [( 1/a 0
0
a ), ( 1 0
c 1 )] = (
1
0
c(a2−1) 1 ) for all b and c in F, so by
letting b = 1/(a2 −1) and c = −2/(a2 −1) we realize ( 1 1
0 1 ) and (
1 0
−2 1 ) as commutators.
(When F = R we can use a = 2, b = 1/3, and c = −2/3.)
To show −I2 is a commutator in SL2(F) if and only if −1 = x2 + y2 for some x and y
in F, suppose ﬁrst that −I2 = [A, B] = ABA−1B−1 for some A and B in SL2(F). We may
assume we’re in the case that −1 is not a square in F, since if it is then it is also a sum of
two squares where one square is 0.
Step 1: A and B have trace 0.
Solving the equation −I2 = ABA−1B−1 for A,
A = −BAB−1 =⇒Tr(A) = Tr(−BAB−1) = −Tr(A) =⇒2 Tr(A) = 0 =⇒Tr(A) = 0,
where the last step depends on 2 ̸= 0 in F. That Tr(B) = 0 is similar.
Step 2: A−1 = −A, B−1 = −B, [A, B] = (AB)2, and Tr(AB) = 0.
A 2×2 matrix M of trace 0 has the form ( a
b
c −a ), and when it has determinant 1 we have
M−1 = ( −a −b
−c
a ) = −M. Therefore if A and B are in SL2(F) with trace 0, their commutator
is [A, B] = ABA−1B−1 = AB(−A)(−B) = (AB)2.
1In the group GL2(R), −I2 is a commutator: −I2 = [( −1 0
0 1 ), ( 0 1
1 0 )], where det( −1 0
0 1 ) = det( 0 1
1 0 ) = −1.

<!-- page 2 -->
2
KEITH CONRAD
Rewriting −I2 = ABA−1B−1 as AB = −BA, we have Tr(AB) = −Tr(BA) = −Tr(AB),
so 2 Tr(AB) = 0 and thus Tr(AB) = 0.
Step 3: −1 = x2 + y2 for some x and y in F. We’ll do this in two ways.
Method 1: Since Tr(A) = 0, we can write A = ( a
b
c −a ) . Since det A = 1, −a2 −bc = 1.
Then being in the case that −1 is not a square in F implies c ̸= 0.
Conjugating a commutator conjugates the elements being “commutated” by (1), so −I2 =
[CAC−1, CBC−1] for all C in SL2(F). Use C = ( 1 t
0 1 ), so CAC−1 = ( a+ct
∗
c
−(a+ct) ). Since
c ̸= 0, for a suitable t we have a + ct = 0. Put this t in C and rename CAC−1 and CBC−1
as A and B, so −I2 = [A, B] where A has diagonal entries 0: A = ( 0 −1/c
c
0 ). (The upper
right entry is −1/c since det A = 1.) Running through Steps 1 and 2 with this new A and
B, Tr(B) = 0 and [A, B] = (AB)2. Set B = ( x
y
z −x ). Then
−I2 = [A, B] = (AB)2 =

x2 + z2/c2
xy −xz/c2
−xz + xyc2
x2 + y2c2

.
From either diagonal entry, −1 is a sum of two squares in F.
Method 2: By Step 2, A−1 = −A, so A2 = −I2. Thus eigenvalues of A are square roots
of −1, which are not in F by the case we’re in, so A has no eigenvector in F 2. Hence for
nonzero v ∈F 2, Av ̸∈Fv, which implies B := {v, Av} is a basis of F 2. Since A2 = −I2,
the matrix for A relative to B is ( 0 −1
1
0 ), so UAU−1 = ( 0 −1
1
0 ) for an invertible matrix U in
M2(F), and det(UAU−1) = det A = 1. Similarly, det(UBU−1) = 1. Rename UAU−1 as A
and UBU−1 as B, so −I2 = [A, B] where A = ( 0 −1
1
0 ). By Step 1, Tr(B) = 0, so we can
write B = ( x
y
z −x ). Then AB = ( −z x
x y ). Since Tr(AB) = 0 by Step 2, −z + y = 0, so z = y.
Thus B = ( x
y
y −x ), so 1 = det B = −x2 −y2, which implies −1 = x2 + y2.2
Conversely, assume −1 = x2 + y2 with x and y in F. For A = ( 0 −1
1
0 ) and B = ( x
y
y −x ) in
SL2(F), [A, B] = (AB)2 = ( −y x
x y )2 = ( x2+y2
0
0
x2+y2 ) = −I2.
□
Example 2. In C, −1 = i2+02, so −I2 = [A, B] for A = ( 0 −1
1
0 ) and B = ( i
0
0 −i ) in SL2(C).
For odd primes p, −1 is a sum of two squares in Z/pZ, so −I2 is a commutator in
SL2(Z/pZ). This is also true in SL2(Z/2Z) since −I2 ≡I2 mod 2. Each ﬁnite ﬁeld contains
some Z/pZ, so −I2 is a commutator in SL2(F) when F is ﬁnite. Thus Theorem 1 doesn’t
give us a ﬁnite group in which some product of commutators is not a commutator. The
smallest such ﬁnite groups have order 96 and there are two of them up to isomorphism: see
https://math.stackexchange.com/questions/7811 and [1]. This is due to R. Guralnick
in his Ph.D. thesis. In both of these groups, there are 29 commutators and the subgroup
they generate has order 32. One such group is G = (Q8×(Z/(2))2)⋊Z/(3) where a generator
of Z/(3) acts on Q8 by the order 3 automorphism having the eﬀect i 7→j 7→k 7→i and it
acts on (Z/(2))2 through the order 3 automorphism ( 0 1
1 1 ) in GL2(Z/(2)).3
References
[1] L-C. Kappe and R. F. Morse, “On commutators in groups”, pp. 531-558 in Groups St. Andrews 2005,
Vol. 2, Cambridge Univ. Press (2007).
2This second approach to Step 3, when F = R, is one answer to the question about commutators on the
MO page https://mathoverflow.net/questions/44269.
3This group G can also be described as Q8 ⋊A4 where A4 acts nontrivially on Q8 through its cyclic
quotient A4/V ∼= Z/(3) where V is the unique 2-Sylow subgroup of A4.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*