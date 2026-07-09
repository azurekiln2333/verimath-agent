# Ufdapp

> **Source**: https://kconrad.math.uconn.edu/blurbs/ufdapp.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
TWO APPLICATIONS OF UNIQUE FACTORIZATION
KEITH CONRAD
1. Introduction
We will use unique factorization to determine all integral solutions to certain equations.
Theorem 1.1. The integral solutions to y2 + y = x3 are (x, y) = (0, 0) and (0, −1).
Since y2 + y = y(y + 1), this says in words that the only integer which is a product of
two consecutive integers and is a cube is 0.
Theorem 1.2 (Fermat). The integral solutions to y2 = x3 −2 are (x, y) = (3, 5) and
(3, −5).
The proof of Theorem 1.1, which is really a warm-up for Theorem 1.2, will use unique
factorization in Z. Although Theorem 1.2 is only about integers, its proof will go beyond
Z and use unique factorization in the ring Z[√−2] = {a + b√−2 : a, b ∈Z}.
2. Proofs
Before we prove Theorems 1.1 and 1.2 we need a result about relatively prime numbers
whose product is a power. (We say elements in a ring with unique factorization are relatively
prime when they have no irreducible factor in common: their only common factors are
units.)
Theorem 2.1. Let R be a ring with unique factorization. If a, b, c ∈R are nonzero, ab = cn,
and a and b are relatively prime then there are units u and v in R, as well as elements a′
and b′ in R, such that a = ua′n and b = vb′n.
Proof. Decompose a, b, and c into irreducibles and collect together irreducible factors that
are equal up to unit multiple. This lets us write
a = upe1
1 pe2
2 · · · per
r ,
b = vp′f1
1 p′f2
2 · · · p′fs
s ,
c = wqg1
1 qg2
2 · · · qgt
t ,
where pi, p′
j, and qk are all irreducibles and u, v, and w are units. Since a and b are relatively
prime, no pi and p′
j are unit multiples. We have
ab = uvpe1
1 pe2
2 · · · per
r p′f1
1 p′f2
2 · · · p′fs
s
and
cn = wnqng1
1
qng2
2
· · · qngt
t
.
Comparing the irreducible factorizations of ab and cn shows from unique factorization that
each pi in a and p′
j in b has multiplicity divisible by n: each ei and fj is a multiple of n.
(Here is where we use relative primality of a and b.) Since all the ei’s are divisible by n, a
is u times an nth power. Similarly, b is v times an nth power.
□
1

<!-- page 2 -->
2
KEITH CONRAD
Example 2.2. Taking n = 2, in Z we have (−4)(−9) = 62 and −4 and −9 are each squares
up to unit multiple. Notice neither −4 nor −9 is a square, so the equality up to unit multiple
in the conclusion of Theorem 2.1 can’t be weakened in general.
Remark 2.3. There are counterexamples to the conclusion of Theorem 2.1 if we drop the
hypothesis that R has unique factorization. For example, in the ring Z[√−26] consider the
equation
(2.1)
(1 +
√
−26)(1 −
√
−26) = 33.
It can be shown that the only common factors of 1+√−26 and 1−√−26 are ±1, so 1+√−26
and 1 −√−26 are relatively prime. The only units in Z[√−26] are ±1 and the equation
1 + √−26 = ±(m + n√−26)3 has no integral solution (m, n): if there were an integral
solution, then taking squared absolute values of both sides in C tells us 27 = (m2 + 26n2)3,
so m2 + 26n2 = 3, which is impossible in Z. Thus Theorem 2.1 does not apply to Z[√−26].
In fact, (2.1) is an example of nonunique irreducible factorization in Z[√−26]: it can be
shown that 1 + √−26, 1 −√−26, and 3 are all irreducible in Z[√−26], and a product of
two irreducibles being equal to a product of three irreducibles violates part of the meaning
of unique factorization.
Now we are ready to prove the theorems from Section 1.
First we prove Theorem 1.1.
Proof. Suppose x and y are integers which satisfy y2 + y = x3. Write this as
y(y + 1) = x3.
Assuming neither y nor y + 1 is 0, these integers are relatively prime (consecutive integers
have no common factors except ±1) and we can apply Theorem 2.1: their product is a cube
so each one is a cube up to sign:
y = ±a3,
y + 1 = ±b3.
Since −1 is a cube, if there is a sign appearing then it can be absorbed into the cube and
then rename a and b. Thus we have
y = a3,
y + 1 = b3.
The integers y and y + 1 are consecutive, so a3 and b3 are consecutive cubes. The cubes
spread apart pretty quickly:
. . . , −64, −27, −8, −1, 0, 1, 8, 27, 64, . . . .
We see immediately that the only consecutive cubes are −1 and 0 and also 0 and 1. Since
y = a3 is the smaller of the two cubes, y = −1 or y = 0. We get x3 = y2 + y = 0 in both
cases. So (x, y) is (0, −1) or (0, 0).
These are the solutions we expected, although strictly speaking our argument assumed y
and y + 1 are not 0 in order to apply Theorem 2.1. So what we have really shown in this
case is that there is no solution with y not 0 or −1. For those two y-values we have the two
obvious solutions, so they are the only ones.
□
Now we prove Theorem 1.2.
Proof. Assume x and y are integers satisfying y2 = x3 −2. First we determine the parity
of x and y. If x is even then 8 | x3, so y2 ≡−2 ≡6 mod 8. However, a direct check of all

<!-- page 3 -->
TWO APPLICATIONS OF UNIQUE FACTORIZATION
3
integers modulo 8 shows the only squares modulo 8 are 0, 1, and 4. Thus x has to be odd,
so y is also odd. All we will need to know is that x is odd.
We now rewrite the equation y2 = x3 −2 as
(2.2)
x3 = y2 + 2 = (y +
√
−2)(y −
√
−2).
We have factored y2 +2 in Z[√−2] and will copy the idea in the proof of Theorem 1.1. One
new aspect is going to be our use of the norm function N(a + b√−2) = a2 + 2b2 on Z[√−2],
which is multiplicative and takes nonnegative values in Z.1 In particular, if α | β in Z[√−2]
then N(α) | N(β) in Z.
Our ﬁrst task is to show that the factors y + √−2 and y −√−2 in (2.2) are relatively
prime in Z[√−2]. Pick an arbitrary common divisor d of y + √−2 and y −√−2. We will
write down some divisibility relations involving d in Z[√−2], and then take norms down to
Z to show d = ±1.
A divisor of two numbers divides their diﬀerence, so d divides (y + √−2) −(y −√−2) =
2√−2, which doesn’t involve y. So d | 2√−2 in Z[√−2], and taking norms turns this into
N(d) | 8 in Z. At the same time, N(d) divides N(y + √−2) = y2 + 2 = x3, which is odd, so
N(d) is odd. The only odd positive divisor of 8 is 1, so N(d) = 1. Writing d = a + b√−2
we have a2 + 2b2 = 1, so (a, b) = (±1, 0), so d = ±1. Therefore y + √−2 and y −√−2 are
relatively prime.
Our next task is to use unique factorization in Z[√−2]. Equation (2.2) expresses a cube
in Z[√−2] on the left side as a product of relatively prime factors y + √−2 and y −√−2
on the right side. Therefore by unique factorization in Z[√−2] and Theorem 2.1, y + √−2
is a unit times a cube in Z[√−2]. The only units in Z[√−2] are ±1 since the only integral
solutions to a2 + 2b2 = 1 are (a, b) = (±1, 0). (This is a contrast with Z[
√
2], which has
inﬁnitely many units, such as the integral powers of 1 +
√
2.) Since ±1 are both cubes, a
unit in Z[√−2] times a cube is a cube, so y + √−2 is a cube: for some m and n in Z,
y +
√
−2 = (m + n
√
−2)3 = (m3 −6mn2) + (3m2n −2n3)
√
−2.
Equating real and imaginary parts,
y = m(m2 −6n2),
1 = n(3m2 −2n2).
From the second equation n = ±1. If n = 1 then 1 = 3m2 −2, so m2 = 1. Thus m = ±1,
which makes y = ±(1 −6) = ±5 and x3 = 25 + 2 = 27 so x = 3. We have recovered
the solutions (3, ±5). If n = −1 then 1 = −(3m2 −2), so 3m2 = 1. This has no integral
solutions, so we are done. The only integer solutions to y2 = x3 −2 are (3, ±5).
□
While y2 = x3 −2 has ﬁnitely many integral solutions, it has inﬁnitely many rational
solutions. The next simplest rational solutions of y2 = x3 −2 after (3, ±5) are
129
100, ± 383
1000

and
164323
29241 , ±66234835
5000211

.
1This norm function on Z[√−2] is the squared absolute value as complex numbers: a2+2b2 = |a+b√−2|2.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*