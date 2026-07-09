# Applications of Galois Theory

> **Source**: https://kconrad.math.uconn.edu/blurbs/galoisappn.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
APPLICATIONS OF GALOIS THEORY
KEITH CONRAD
We’ll examine here several types of applications of Galois theory: examples of the Galois
correspondence in Section 1, theorems about ﬁeld extensions in Section 2, a description of
minimal polynomials in a Galois extension in Sections 3, and a brief indication of what lies
beyond Galois theory of ﬁnite extensions in Section 4.
1. Examples
Example 1.1. The ﬁeld extension Q(
√
2,
√
3)/Q is Galois of degree 4, so its Galois group
has order 4. The elements of the Galois group are determined by their values on
√
2 and
√
3. The Q-conjugates of
√
2 and
√
3 are ±
√
2 and ±
√
3, so we get at most four possible
automorphisms in the Galois group. See Table 1. Since the Galois group has order 4, these
4 possible assignments of values to σ(
√
2) and σ(
√
3) all really exist.
σ
σ(
√
2)
σ(
√
3)
id.
√
2
√
3
σ1
√
2
−
√
3
σ2
−
√
2
√
3
σ3
−
√
2
−
√
3
Table 1.
The automorphisms σ1, σ2, and σ3 in Table 1 have order 2. Since Gal(Q(
√
2,
√
3)/Q)
contains 3 elements of order 2, Q(
√
2,
√
3) has 3 subﬁelds Ki such that [Q(
√
2,
√
3) : Ki] = 2,
or equivalently [Ki : Q] = 4/2 = 2. Two such ﬁelds are Q(
√
2) and Q(
√
3). A third is
Q(
√
6) and that completes the list. Here is a diagram of all the subﬁelds.
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
In Table 1, the subgroup ﬁxing Q(
√
2) is ⟨σ1⟩, the subgroup ﬁxing Q(
√
3) is ⟨σ2⟩, and the
subgroup ﬁxing Q(
√
6) is ⟨σ3⟩(since (−
√
2)(−
√
3) =
√
2
√
3).
The eﬀect of Gal(Q(
√
2,
√
3)/Q) on
√
2 +
√
3 is given in Table 2.
The 4 values are
all diﬀerent, since
√
2 and
√
3 are linearly independent over Q. Therefore Q(
√
2,
√
3) =
Q(
√
2 +
√
3). The minimal polynomial of
√
2 +
√
3 over Q must be
(X −(
√
2 +
√
3))(X −(−
√
2 +
√
3))(X −(
√
2 −
√
3))(X −(−
√
2 −
√
3)) = X4 −10X2 + 1.
1

<!-- page 2 -->
2
KEITH CONRAD
σ
σ(
√
2)
σ(
√
3)
σ(
√
2 +
√
3)
id.
√
2
√
3
√
2 +
√
3
σ1
√
2
−
√
3
√
2 −
√
3
σ2
−
√
2
√
3
−
√
2 +
√
3
σ3
−
√
2
−
√
3
−
√
2 −
√
3
Table 2.
In particular, X4 −10X2 + 1 is irreducible in Q[X] since it’s a minimal polynomial over Q.
By similar reasoning, if a ﬁeld F does not have characteristic 2 and a and b are nonsquares
in F such that ab is not a square in F either, then [F(√a,
√
b) : F] = 4 and all the ﬁelds
between F and F(√a,
√
b) are as in the following diagram.
F(√a,
√
b)
F(√a)
F(
√
b)
F(
√
ab)
F
Furthermore, F(√a,
√
b) = F(√a +
√
b). The argument is as in the special case above.
Example 1.2. While Q(
4√
2)/Q is not Galois, Q(
4√
2) lies in Q(
4√
2, i), which is Galois over
Q. We will use Galois theory for Q(
4√
2, i)/Q to ﬁnd the intermediate ﬁelds in Q(
4√
2)/Q.
The Galois group of Q(
4√
2, i)/Q equals ⟨r, s⟩, where
r(
4√
2) = i
4√
2, r(i) = i and s(
4√
2) =
4√
2, s(i) = −i.
(Viewing elements of Q(
4√
2, i) as complex numbers, s acts on them like complex conjuga-
tion.) The group ⟨r, s⟩is isomorphic to D4, where r corresponds to a 90 degree rotation of
the square and s corresponds to a reﬂection across a diagonal. What is the subgroup H of
Gal(Q(
4√
2, i)/Q) corresponding to Q(
4√
2)?
(1.1)
Q(
4√
2, i)
{1}
2
2
Q(
4√
2)
H
4
4
Q
D4
Since s is a nontrivial element of the Galois group that ﬁxes Q(
4√
2), s ∈H. The size
of H is [Q(
4√
2, i) : Q(
4√
2)] = 2, so H = {1, s} = ⟨s⟩. By the Galois correspondence for
Q(
4√
2, i)/Q, ﬁelds strictly between Q(
4√
2) and Q correspond to subgroups of the Galois
group strictly between ⟨s⟩and ⟨r, s⟩. From the known subgroup structure of D4, the only
subgroup lying strictly between ⟨s⟩and ⟨r, s⟩is ⟨r2, s⟩. Therefore only one ﬁeld lies strictly
between Q(
4√
2) and Q. Since Q(
√
2) is such a ﬁeld it is the only one.

<!-- page 3 -->
APPLICATIONS OF GALOIS THEORY
3
Remark 1.3. While Galois theory provides the most systematic method to ﬁnd intermedi-
ate ﬁelds, it may be possible to argue in other ways. For example, suppose Q ⊂F ⊂Q(
4√
2)
with [F : Q] = 2. Then
4√
2 has degree 2 over F. Since
4√
2 is a root of X4 −2, its minimal
polynomial over F has to be a quadratic factor of X4 −2. There are three monic quadratic
factors with
4√
2 as a root, but only one of them, X2 −
√
2, has coeﬃcients in Q(
4√
2) (let
alone in R). Therefore X2 −
√
2 must be the minimal polynomial of
4√
2 over F, so
√
2 ∈F.
Since [F : Q] = 2, F = Q(
√
2) by counting degrees.
Example 1.4. Let’s explore Q(
4√
2, ζ8), where ζ8 = e2πi/8 is a root of unity of order 8,
whose minimal polynomial over Q is X4 + 1. Both Q(
4√
2) and Q(ζ8) have degree 4 over
Q. Since ζ2
8 = i, Q(
4√
2, ζ8) is a splitting ﬁeld over Q of (X4 −2)(X4 + 1) and therefore is
Galois over Q. What is its Galois group? We have the following ﬁeld diagram.
Q(
4√
2, ζ8)
≤4
≤4
Q(
4√
2)
4
Q(ζ8)
4
Q
Thus [Q(
4√
2, ζ8) : Q] is at most 16. We will see the degree is not 16: there are some hidden
algebraic relations between
4√
2 and ζ8.
Any σ ∈Gal(Q(
4√
2, ζ8)/Q) is determined by its values
(1.2)
σ(ζ8) = ζa
8
(a ∈(Z/8Z)×)
and
σ(
4√
2) = ib 4√
2 (b ∈Z/4Z).
There are 4 choices each for a and b. Taking independent choices of a and b, there are at
most 16 automorphisms in the Galois group. But the choices of a and b can not be made
independently because ζ8 and
4√
2 are linked to each other:
(1.3)
ζ8 + ζ−1
8
= e2πi/8 + e−2πi/8 = 2 cos
π
4

=
√
2 =
4√
2
2.
This says
√
2 belongs to both Q(ζ8) and Q(
4√
2). Here is a ﬁeld diagram that emphasizes
the common subﬁeld Q(
√
2) in Q(
4√
2) and Q(ζ8). This subﬁeld is the source of (1.3).
Q(
4√
2, ζ8)
≤4
≤4
Q(
4√
2)
2
Q(ζ8)
2
2
Q(
√
2)
2
Q(i)
2
Q
Rewriting ζ8 + ζ−1
8
=
√
2 as ζ2
8 −
√
2ζ8 + 1 = 0, ζ8 has degree at most 2 over Q(
4√
2).
Since ζ8 is not real, it isn’t inside Q(
4√
2), so it has degree 2 over Q(
4√
2).
Therefore

<!-- page 4 -->
4
KEITH CONRAD
[Q(
4√
2, ζ8) : Q] = 2 · 4 = 8 and the degrees marked as “≤4” in the diagram both equal 2.
We rewrite the ﬁeld diagram below.
Q(
4√
2, ζ8)
2
2
Q(
4√
2)
2
Q(ζ8)
2
2
Q(
√
2)
2
Q(i)
2
Q
Returning to the Galois group, (1.3) tells us the eﬀect of σ ∈Gal(Q(
4√
2, ζ8)/Q) on
4√
2
partially determines it on ζ8, and conversely: (σ(
4√
2))2 = σ(ζ8) + σ(ζ8)−1, which in the
notation of (1.2) is the same as
(1.4)
(−1)b = ζa
8 + ζ−a
8
√
2
.
Since ζ8 = e2πi/8 = (1 + i)/
√
2, a calculation shows ζa
8 + ζ−a
8
=
√
2 if a ≡1, 7 mod 8 and
ζa
8 + ζ−a
8
= −
√
2 if a ≡3, 5 mod 8 (note ζ7
8 = ζ−1
8
and ζ5
8 = ζ−3
8 ). Thus if a ≡1, 7 mod 8
we have (−1)b = 1, so b ≡0, 2 mod 4, while if a ≡3, 5 mod 8 we have (−1)b = −1, so
b ≡1, 3 mod 4. For example, σ can’t both ﬁx
4√
2 (b = 0) and send ζ8 to ζ3
8 (a = 3) because
(1.4) would not hold.
The simplest way to understand Q(
4√
2, ζ8) is to use a diﬀerent set of generators. Since
ζ8 = e2πi/8 = eπi/4 = (1 + i)/
√
2,
Q(
4√
2, ζ8) = Q(
4√
2, i),
and from the second representation we know its Galois group over Q is isomorphic to D4
with independent choices of where to send
4√
2 (to any fourth root of 2) and i (to any
square root of −1) rather than
4√
2 and ζ8. A diﬀerent choice of ﬁeld generators can make
it easier to see what the Galois group looks like. We also see immediately from the second
representation that [Q(
4√
2, ζ8) : Q] = 8.
Example 1.5. Let’s consider the splitting ﬁeld of X8 −2 over Q, which is Q(
8√
2, ζ8),
where ζ8 = e2πi/8 = (1 + i)/
√
2. While [Q(
8√
2) : Q] = 8 and [Q(ζ8) : Q] = 4, we’ll see that
[Q(
8√
2, ζ8) : Q] is 16, not 32, and determine Gal(Q(
8√
2, ζ8)/Q). It is a group of order 16,
but is not isomorphic to the dihedral group of order 16.
What we do will build on the previous example, where [Q(
4√
2, ζ8) : Q] is 8, not 16 (the
product of [Q(
4√
2) : Q] and [Q(ζ8) : Q]), since Q(
4√
2) and Q(ζ8) are not “independent”
over Q: the ﬁelds both contain
√
2
Since ζ8 ̸∈Q(
8√
2) but ζ2
8 −
√
2ζ8 + 1 = 0 by the algebraic relation (1.3), the degree of ζ8
over Q(
8√
2) is 2. Thus [Q(
8√
2, ζ8) : Q] = [Q(
8√
2, ζ8) : Q(
8√
2)][Q(
8√
2) : Q] = 2 · 8 = 16, so
| Gal(Q(
8√
2, ζ8)/Q)| = 16.
Each σ ∈Gal(Q(
4√
2, ζ8)/Q) is determined by the values
(1.5)
σ(ζ8) = ζa
8
(a ∈(Z/8Z)×)
and
σ(
8√
2) = ζb
8
8√
2 (b ∈Z/8Z).

<!-- page 5 -->
APPLICATIONS OF GALOIS THEORY
5
There is a condition linking a and b, from (1.3):
(1.6)
ζa
8 + ζ−a
8
= σ(ζ8 + ζ−1
8 ) = σ(
√
2) = σ(
8√
2
4) = σ(
8√
2)4 = (−1)b√
2.
(This is essentially the same as (1.4), excepts now b comes from Z/8Z instead of Z/4Z.) It
follows from (1.6), by reasoning like that in the previous example, that if a ≡1, 7 mod 8
then b is even and if a ≡3, 5 mod 8 then b is odd. Therefore, since b is in Z/8Z, there are
at most 4 values of b allowed for each value of a. That means Gal(Q(
8√
2, ζ8)/Q) has order
at most 16. Since we earlier showed the Galois group has order 16, the parity condition
on b for each a is the only constraint: Gal(Q(
8√
2, ζ8)/Q) consists of the automorphisms
described by (1.3) where (i) b is even if a ≡1, 7 mod 8 and (ii) b is odd if a ≡3, 5 mod 8.1
Here is a ﬁeld diagram, which is very far from showing all intermediate ﬁelds.
Q(
8√
2, ζ8)
4
2
Q(
8√
2)
4
Q(ζ8)
2
2
Q(
√
2)
2
Q(i)
2
Q
Each automorphism in Gal(Q(
8√
2, ζ8)/Q) can be written by (1.3) as σa,b where σa,b(ζ8) =
ζa
8 and σa,b(
8√
2) = ζb
8
8√
2. Two automorphisms σa,b and σc,d compose as follows:
σa,b(σc,d(ζ8)) = σa,b(ζc
8) = ζac
8 ,
σa,b(σc,d(
8√
2)) = σa,b(ζd
8
8√
2) = σa,b(ζ8)dσa,b(
8√
2) = ζad+b
8
8√
2.
This is how matrices ( a b
0 1 ) multiply: ( a b
0 1 )( c d
0 1 ) = ( ac ad+b
0
1
). Therefore Gal(Q(
8√
2, ζ8)/Q)
can be viewed as 2 × 2 mod 8 matrices by
σa,b 7→

a
b
0
1

where a ∈(Z/8Z)× and b ∈Z/8Z subject to the conditions
• b is even if a ≡1, 7 mod 8,
• b is odd if a ≡3, 5 mod 8.
This constraint on b given a, or on a given b, is important to remember, e.g., the matrix
( 1 1
0 1 ) is not in the Galois group: no σ has the eﬀect σ(ζ8) = ζ8 and σ(
8√
2) = ζ8
8√
2!
What group of order 16 is the Galois group? It is not isomorphic to the dihedral group
of order 16 since that dihedral group has 9 elements of order 2 (all 8 reﬂections and the
rotation r4) while the Galois group has 5 elements of order 2: ( 1 4
0 1 ), ( 7 0
0 1 ), ( 7 2
0 1 ), ( 7 4
0 1 ), and
( 7 6
0 1 ). (The mod 8 matrices ( 3 0
0 1 ) and ( 5 0
0 1 ) have order 2, but they are not in the Galois
group since a matrix of the form ( a 0
0 1 ) in the Galois group has a ≡1, 7 mod 8.)
The Galois group contains σ := ( 5 1
0 1 ), which has order 8. Its successive powers are in
the table below. An element of the Galois group with order 2 that is not a power of σ is
1A concise way of describing the two parity constraints on b mod 8 given a mod 8 is b ≡a2−1
8
mod 2.

<!-- page 6 -->
6
KEITH CONRAD
τ := ( 7 0
0 1 ). Since the Galois group has order 16, it is ⟨σ, τ⟩. By an explicit mod 8 matrix
calculation, τστ −1 = τστ = ( 5 7
0 1 ) = σ3.
k
1
2
3
4
5
6
7
8
σk
( 5 1
0 1 )
( 1 6
0 1 )
( 5 7
0 1 )
( 1 4
0 1 )
( 5 5
0 1 )
( 1 2
0 1 )
( 5 3
0 1 )
( 1 0
0 1 )
The group with two generators x and y where x has order 8, y has order 2, and yxy−1 = x3
is called the semidihedral group of order 16. You can look up information about it on the
page https://groupprops.subwiki.org/wiki/Semidihedral group:SD16. For example,
that webpage says this group has 3 subgroups of order 8, so by Galois theory Q(
8√
2, ζ8) has
3 quadratic ﬁelds. There are 3 quadratic ﬁelds in Q(ζ8): Q(
√
2), Q(i), and Q(i
√
2). Thus
these are all the quadratic ﬁelds of Q(
8√
2, ζ8).2 The webpage also says the 3 subgroups of
order 8 are isomorphic to Z/8Z, D4,3 and Q8, so the Galois group has a subgroup isomorphic
to each of these groups. For example, check σ ﬁxes i = ζ4
8, and since σ has order 8 we have
Gal(Q(
8√
2, ζ8)/Q(i)) = ⟨σ⟩∼= Z/8Z.
By determining which elements of the Galois group ﬁx
√
2 =
8√
2
4 and i
√
2, it is left as an
exercise to the reader to show
Gal(Q(
8√
2, ζ8)/Q(
√
2)) ∼= D4,
Gal(Q(
8√
2, ζ8)/Q(i
√
2)) ∼= Q8.
This concludes our look at Q(
8√
2, ζ8) and its Galois group over Q.
A Galois extension is said to have a given group-theoretic property (being abelian, non-
abelian, cyclic, etc.) when its Galois group has that property.
Example 1.6. Any quadratic extension of Q is an abelian extension since its Galois group
has order 2. It is also a cyclic extension.
Example 1.7. The extension Q(
3√
2, ω)/Q is called non-abelian since its Galois group is
isomorphic to S3, which is a non-abelian group. The term “non-abelian” has nothing to do
with the ﬁeld operations, which of course are always commutative.
Theorem 1.8. If L/K is a ﬁnite abelian extension then every intermediate ﬁeld is an
abelian extension of K. If L/K is cyclic then every intermediate ﬁeld is cyclic over K.
Proof. Every subgroup of an abelian group is a normal subgroup, so every ﬁeld F between
L and K is Galois over K and Gal(F/K) ∼= Gal(L/K)/ Gal(L/F). The quotient of an
abelian group by any subgroup is abelian, so Gal(F/K) is abelian.
Since the quotient of a cyclic group by any subgroup is cyclic, if L/K is cyclic then F/K
is cyclic too.
□
2. Applications to Field Theory
We will prove the complex numbers are algebraically closed (the “Fundamental Theorem
of Algebra”) using Galois theory and a small amount of analysis. We need one property of
the real numbers, one property of the complex numbers, and two properties of ﬁnite groups:
(1) Every odd degree polynomial in R[X] has a real root. In particular, no polynomial
of odd degree greater than 1 in R[X] is irreducible.
2In fact those 3 quadratic ﬁelds are the only quadratic ﬁelds in Q(
2k√
2, ζ2k) for k ≥2. This can be shown
by methods of algebraic number theory without having to compute Galois groups.
3That webpage follows the group theorist’s convention of writing the dihedral group of order 2n as D2n
instead of Dn, so it writes D8 instead of D4.

<!-- page 7 -->
APPLICATIONS OF GALOIS THEORY
7
(2) Every number in C has square roots in C.
(3) The ﬁrst Sylow theorem (existence of Sylow subgroups).
(4) A nontrivial ﬁnite p-group has a subgroup of index p.
The ﬁrst property is a consequence of the intermediate value theorem.
The second
property follows from writing a nonzero complex number as reiθ and then its square roots
are ±√reiθ/2. (For example, i = eiπ/2 and a square root of i is eiπ/4 =
1
√
2 +
i
√
2.) It is a nice
exercise to ﬁnd a square root of a + bi in terms of a and b. The third property is proved as
part of the Sylow theorems. The fourth property is often proved in the context of showing
ﬁnite p-groups are solvable; this can be found in most group theory textbooks.
Theorem 2.1. The complex numbers are algebraically closed.
Proof. We need to show any irreducible in C[X] has degree 1. If π(X) ∈C[X] is irreducible
and α is a root, then [C(α) : C] = deg π, so our task is the same as showing the only ﬁnite
extension of C is C itself.
Let E/C be a ﬁnite extension. Since E is a ﬁnite extension of R, and we’re in character-
istic 0, we can enlarge E/R to a ﬁnite Galois extension K/R. Since R ⊂C ⊂K, [K : R]
is even.
Let 2m ≥2 be the highest power of 2 dividing the size of G = Gal(K/R). There is a
subgroup H of G with order 2m (Property 3). Let F be the corresponding ﬁxed ﬁeld, so
[F : R] is odd.
K
2m
{1}
2m
F
odd
H
odd
C
2
R
G
Every α ∈F has degree over R dividing [F : R], so [R(α) : R] is odd. That means the
minimal polynomial of α in R[X] has odd degree. Irreducible polynomials in R[X] of odd
degree have degree 1 (Property 1), so [R(α) : R] = 1. Thus α ∈R, so F = R. Therefore
G = H is a 2-group.
K
{1}
2m−1
C
2
Gal(K/C)
2
R
G
The group Gal(K/C) has order 2m−1. If m ≥2 then Gal(K/C) has a subgroup of index
2 (Property 4), whose ﬁxed ﬁeld has degree 2 over C. Any quadratic extension of C has the
form C(
√
d) for some nonsquare d ∈C×. But every nonzero complex number has square

<!-- page 8 -->
8
KEITH CONRAD
roots in C (Property 2), so [C(
√
d) : C] is 1, not 2. We have a contradiction. Thus m = 1,
so K = C. Since C ⊂E ⊂K, we conclude that E = C.
□
Theorem 2.2. If L/K be Galois with degree pm, where p is a prime, then there is a chain
of intermediate ﬁelds
K = F0 ⊂F1 ⊂F2 ⊂· · · ⊂Fm = K
where [Fi : Fi−1] = p for i ≥1 and Fi/K is Galois.
Proof. The group Gal(L/K) is a ﬁnite group of order pm.
One of the consequences of
ﬁnite p-groups being solvable is the existence of a rising chain of subgroups from the trivial
subgroup to the whole group where each subgroup has index p in the next one and each
subgroup is normal in the whole group. Now apply the Galois correspondence.
□
The next application, which is an amusing technicality, is taken from [2, p. 67].
Theorem 2.3. Let p be a prime number. If K is a ﬁeld of characteristic 0 such that every
proper ﬁnite extension of K has degree divisible by p then every ﬁnite extension of K has
p-power degree.
Aside from examples resembling K = R (where p = 2 works), ﬁelds that ﬁt the conditions
of Theorem 2.3 are not easy to describe at an elementary level. But the technique of proof
is a pleasant use of elementary group theory.
Proof. Let L/K be a ﬁnite extension. We want to show [L : K] is a power of p. Since K
has characteristic 0, L/K is separable, so we can embed L in a ﬁnite Galois extension E/K.
Since [L : K] | [E : K], it suﬃces to show [E : K] is a power of p, i.e., show ﬁnite Galois
extensions of K have p-power degree.
By the ﬁrst Sylow theorem, Gal(E/K) contains a p-Sylow subgroup, say H. Let F = EH,
so [F : K] is the index of H in Gal(E/K). This index is prime to p by the deﬁnition of a
Sylow subgroup, so [F : K] is prime to p.
E
{1}
power of p
F
H
prime to p
K
Gal(E/K)
Every proper ﬁnite extension of K has degree divisible by p, so [F : K] = 1. Thus F = K
and [E : K] = [E : F] = |H| is a power of p.
□
Remark 2.4. Theorem 2.3 is true when K has positive characteristic, but then one has
to consider the possibility that K has inseparable extensions and additional reasoning is
needed. See [2, p. 67].
3. Applications to Minimal Polynomials
When L/K is a Galois extension and α ∈L, the Galois group Gal(L/K) provides us with
a systematic way to describe all the roots of the minimal polynomial of α over K: they are
the diﬀerent elements of the Galois orbit {σ(α) : σ ∈Gal(L/K)}. If we let Gal(L/K) act
on L[X], and not just L, by acting on polynomial coeﬃcients, then we can relate minimal
polynomials of the same number over diﬀerent ﬁelds using a Galois group.

<!-- page 9 -->
APPLICATIONS OF GALOIS THEORY
9
Theorem 3.1. Let L/K be a ﬁnite Galois extension and α lie in some extension of L with
minimal polynomial f(X) in L[X]. The minimal polynomial of α in K[X] is the product of
all the diﬀerent values of (σf)(X) as σ runs over Gal(L/K).
When α ∈L, so f(X) = X −α, we recover the construction of the minimal polynomial
of α in K[X] as Qr
j=1(X −σj(α)), where σ1(α), . . . , σr(α) are the distinct values of σ(α) as
σ runs over Gal(L/K).
Proof. Let π(X) denote the minimal polynomial of α over K. Since π(α) = 0 and f(X)
is the minimal polynomial of α over L, f(X) | π(X) in L[X]. For any σ ∈Gal(L/K),
f(X) | π(X) ⇒(σf)(X) | π(X) because (σπ)(X) = π(X).
Note (σf)(X) = (σif)(X) for some i. Each σif is monic irreducible in L[X] and there-
fore σif and σjf are relatively prime when i ̸= j. Thus π(X) is divisible by F(X) :=
Qr
i=1(σif)(X). For any σ ∈Gal(L/K), the set of polynomials (σσif)(X) are the same as
all (σif)(X) except it may be in a diﬀerent order, so
(σF)(X) =
r
Y
i=1
(σσif)(X) =
r
Y
i=1
(σif)(X) = F(X),
so the coeﬃcients of F(X) are in K. Since F(X) | π(X) and F(α) = 0, the meaning of
minimal polynomial implies F(X) = π(X).
□
Example 3.2. Consider X2 −
√
2 in Q(
√
2)[X]. It is irreducible since
√
2 is not a square in
Q(
√
2): if (a + b
√
2)2 =
√
2 with a, b ∈Q then a2 + 2b2 = 0, so a = b = 0, a contradiction.
The diﬀerent values of σ(X2−
√
2) = X2−σ(
√
2) as σ runs over Gal(Q(
√
2)/Q) are X2−
√
2
and X2 +
√
2, so the minimal polynomial over Q of the roots of X2 −
√
2 is
(X2 −
√
2)(X2 +
√
2) = X4 −2.
Since a minimal polynomial over a ﬁeld is just an irreducible polynomial over that ﬁeld
(with a particular root), we can formulate Theorem 3.1 in terms of irreducible polynomials
without mentioning roots: if f(X) is monic irreducible in L[X] then the product of the
diﬀerent (σf)(X), as σ runs over Gal(L/K), is irreducible in K[X]. Consider a potential
converse: if f(X) is monic in L[X] and the product of the diﬀerent polynomials (σf)(X),
as σ runs over Gal(L/K), is irreducible in K[X], then f(X) is irreducible in L[X]. This is
false: use L/K = Q(
√
2)/Q and f(X) = X2 −2. Here (σf)(X) = X2 −2 for either σ, so
the product of diﬀerent (σf)(X) is X2 −2, which is irreducible in K[X] but reducible in
L[X]. Yet there is a kernel of truth in this false converse. We just have to make sure the
coeﬃcients of f(X) don’t all lie in an extension of K that is smaller than L.
Theorem 3.3. Let L/K be a ﬁnite Galois extension. Suppose f(X) is monic in L[X] and
its coeﬃcients generate L over K. If the product of the diﬀerent polynomials (σf)(X), as
σ runs over Gal(L/K), is irreducible in K[X], then f(X) is irreducible in L[X].
This avoids the previous counterexample f(X) = X2 −2 with L/K = Q(
√
2)/Q, since
the coeﬃcients of f(X) do not generate Q(
√
2)/Q.
Proof. Since the coeﬃcients of f(X) generate L/K any σ in Gal(L/K) that is not the
identity changes at least one oﬀthe coeﬃcients of f(X). (Otherwise the coeﬃcients lie in
the ﬁeld ﬁxed by σ, which is a nontrivial subgroup of Gal(L/K) and a nontrivial subgroup
has a ﬁxed ﬁeld smaller than L.) It follows that for any distinct σ and τ in Gal(L/K), the

<!-- page 10 -->
10
KEITH CONRAD
polynomials (σf)(X) and (τf)(X) are diﬀerent: if σf = τf then (τ −1σ)f = f, so τ −1σ
ﬁxes the coeﬃcients of f and therefore σ = τ. Thus the hypothesis of the theorem is that
F(X) :=
Y
σ∈Gal(L/K)
(σf)(X).
is irreducible in K[X], where the product runs over all of Gal(L/K), and we want to show
f(X) is irreducible in L[X]. We will prove the contrapositive. Suppose f(X) is reducible
in L[X], so f(X) = g(X)h(X) in L[X] where g(X) and h(X) are nonconstant. Then
F(X) =
Y
σ∈Gal(L/K)
(σf)(X) =
Y
σ∈Gal(L/K)
(σg)(X)
Y
σ∈Gal(L/K)
(σh)(X) = G(X)H(X),
where G(X) and H(X) are in K[X] (why?). Since g(X) and h(X) have positive degree, so
do G(X) and H(X), and therefore F(X) is reducible in K[X].
□
Example 3.4. Consider Xn −
√
2 in Q(
√
2)[X]. Its coeﬃcients generate Q(
√
2)/Q. Since
(Xn −
√
2)(Xn +
√
2) = X2n −2
is irreducible over Q, Xn −
√
2 is irreducible in Q(
√
2)[X] for all n. The same kind of
argument shows Xn −(1 + 2
√
2) is irreducible over Q(
√
2)[X] for all n.
Corollary 3.5. Let L/K be a ﬁnite Galois extension. Suppose f(X) is monic in L[X], its
coeﬃcients generate L/K, and F(X) := Q
σ∈Gal(L/K)(σf)(X) is separable and irreducible
in K[X]. Then each (σf)(X) is irreducible in L[X] and if α is a root of f(X) then the
Galois closure of L(α)/K is the splitting ﬁeld of F(X) over K.
Proof. The irreducibility of f(X) in L[X] follows from Theorem 3.3.
The polynomials
(σf)(X) satisfy the same hypotheses as f(X), so they are all irreducible over L as well.
The minimal polynomial of α over K is F(X) and K(α)/K is separable since F(X) is
separable over K. Therefore L(α)/K is separable, so L(α) has a Galois closure over K.
A Galois extension of K that contains L(α) must contain all the K-conjugates of α and
hence must contain the splitting ﬁeld of F(X) over K. Conversely, the splitting ﬁeld of
F(X) over K is a Galois extension of K that contains α as well as all the roots of f(X),
so the extension contains the coeﬃcients of f(X). Those coeﬃcients generate L/K, so the
splitting ﬁeld of F(X) over K contains L(α).
□
There is nothing deep going on in this corollary. The point is that since the coeﬃcients
of f generate L, L is already inside the Galois closure of K(α)/K, so just by forming the
splitting ﬁeld of F(X) over K we pick up L inside it.
Example 3.6. Consider the extension Q(γ)/Q, where γ is a root of X3 −3X −1. This
cubic extension is Galois and the Q-conjugates of γ are 2 −γ2 and γ2 −γ −2. Let f(X) =
X3 −γX −1. The polynomials (σf)(X) as σ runs over the three elements of Gal(Q(γ)/Q)
are f(X), X3 −(2 −γ2)X −1, and X3 −(γ2 −γ −2)X −1. Their product is
F(X) = X9 −3X6 −3X5 + 2X3 + 3X2 −1,
which is irreducible mod 2 and thus is irreducible in Q[X]. Therefore the polynomials f(X),
X3 −(2 −γ2)X −1, and X3 −(γ2 −γ −2)X −1 are all irreducible over Q(γ)[X] and the
splitting ﬁeld of F(X) over Q is the smallest Galois extension of Q containing Q(γ, α),
where α is a root of f(X). According to PARI, the splitting ﬁeld of F(X) over Q has
degree 684 = 3 · 63.

<!-- page 11 -->
APPLICATIONS OF GALOIS THEORY
11
4. What Next?
There are two important aspects of ﬁeld extensions that are missing in a study of Galois
theory of ﬁnite extensions, and we brieﬂy address them: Galois theory for inﬁnite algebraic
extensions and transcendental extensions.
An algebraic extension L/K of inﬁnite degree is called Galois when it is separable and
normal.
This means each element of L is the root of a separable irreducible in K[X]
and each rreducible in K[X] with a root in L splits completely over L. One inﬁnite Galois
extension of Q is Q(µp∞) = S
n≥1 Q(µpn), the union of all p-th power cyclotomic extensions
of Q, where p is a prime. Even if an algebraic extension L/K is inﬁnite, any particular
element (or ﬁnite set of elements) in L is in a ﬁnite subextension of K, so knowledge of
ﬁnite extensions helps us understand inﬁnite algebraic extensions. In fact, another way of
describing an inﬁnite Galois extension is that it is a composite of ﬁnite Galois extensions.
For an inﬁnite Galois extension L/K, its Galois group Gal(L/K) is still deﬁned as the
group of K-automorphisms of L, and we can associate a subgroup of the Galois group
to each intermediate ﬁeld and an intermediate ﬁeld to each subgroup of the Galois group
just as in the ﬁnite case. However, this correspondence is no longer a bijection! This was
ﬁrst discovered by Dedekind, who saw in examples that diﬀerent subgroups of an inﬁnite
Galois group could have the same ﬁxed ﬁeld. So it looks like Galois theory for inﬁnite
extensions breaks down. But it isn’t really so. Krull realized that if you put a suitable
topology on the Galois group then a bijection can be given between all intermediate ﬁelds
and the closed subgroups in that topology. (See [1] and [3].) Every subgroup of the Galois
group is associated to the same ﬁeld as the closure of the subgroup in the Krull topology,
which explains Dedekind’s examples of diﬀerent subgroups with the same ﬁxed ﬁeld: one
subgroup is the closure of the other. The Krull topology on Galois groups not only rescued
Galois theory for inﬁnite extensions, but it gave a new impetus to the study of topological
groups. To understand inﬁnite Galois theory, ﬁrst learn about the p-adic numbers and their
topological and algebraic structure, as they are used in the simplest examples of interesting
inﬁnite Galois groups, such as Gal(Q(µp∞)/Q). Lectures on inﬁnite Galois theory are here.
Turning away from Galois extensions, the next most important class of ﬁeld extensions
are transcendental extensions. These are ﬁeld extensions in which some element of the top
ﬁeld is transcendental (that is, not algebraic) over the bottom ﬁeld. The simplest example
of a transcendental extension of a ﬁeld F is the ﬁeld F(T) of rational functions over F
in an indeterminate T, or more generally the ﬁeld F(T1, . . . , Tn) of rational functions in n
independent variables over F. This is called a pure transcendental extension. A general
transcendental extension is a mixture of algebraic and transcendental parts, such as F(x, y)
where x is transcendental over F and y2 = x3 −1.
Since transcendental extensions of F have inﬁnite degree, the notion of ﬁeld degree is no
longer important. In its place is the concept of transcendence degree, which is a nonlinear
analogue of a basis and measures how transcendental the extension is. The need to under-
stand transcendental ﬁeld extensions is not driven for its own sake, but for other areas of
mathematics, such as algebraic geometry.
References
[1] J. Bastida, “Field extensions and Galois theory,” Addison-Wesley, Reading, MA 1984.
[2] I. Kaplansky, “Fields and Rings,” 2nd ed., Univ. of Chicago Press, Chicago, 1972.
[3] P. Morandi, “Field and Galois theory,” Springer-Verlag, New York, 1996.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*