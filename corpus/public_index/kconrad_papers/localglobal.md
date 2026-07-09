# The Local-Global Principle

> **Source**: https://kconrad.math.uconn.edu/blurbs/localglobal.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE LOCAL-GLOBAL PRINCIPLE
KEITH CONRAD
1. Introduction
Hensel created p-adic numbers near the start of the 20th century and they had some early
positive inﬂuences: Hensel used them to solve a conjecture of Dedekind about discriminants
in algebraic number theory and they directly inspired Steinitz [10] to develop a general
theory of ﬁelds in order to account for the p-adic numbers alongside previously known ﬁelds
of numbers and functions. (See [8] for a discussion of Steinitz’s paper in English.) Most
mathematicians viewed p-adic numbers with suspicion, perhaps in part because of their
unclear foundations and Hensel’s mistaken proof by p-adic numbers that e is transcendental.
The ﬁrst indication that the p-adic numbers for all p together have a conceptual role in
mathematics came in the 1920s when Hasse discovered that Minkowski’s work on quadratic
forms over the rational numbers could be streamlined by expressing the results in terms
of quadratic forms over the real numbers and all p-adic numbers. Hasse became a strong
advocate of this point of view for number theory, which came to be called the local-global
principle or Hasse principle. Roughly speaking, it states
a theorem or property holds over Q if and only if it holds over R and Qp for all p
or, more generally,
study a problem over Q by studying it in R and all Qp.
The local-global principle is not a deﬁnite theorem, but more of a philosophy. It plays a
role comparable in number theory to the idea in geometry of studying global properties of
a curve or surface through the local geometric properties near each point on the curve or
surface. We call Q a global ﬁeld and the ﬁelds R and Qp local ﬁelds.1
We will see what the local–global principle is about by taking a classical theorem about
sums of two squares in the integers and reformulating it as a theorem in R and every Zp.
A few examples will show the deﬁciency of working with Zp and what is gained by working
with Qp instead. Then we will state Hasse’s version of Minkowski’s theorem on quadratic
forms over Qp as an example where the local–global principle works.
Next we will see
counterexamples to the local–global principle. Finally we will discuss a local–global result
for powers and for heights.
2. Sums of two squares in Z
Here is a classical theorem about sums of two squares, stated without proof.
Theorem 2.1 (Euler). A positive integer m can be written as a sum of two squares if and
only if each prime p dividing m with p ≡3 mod 4 has even multiplicity as a factor of m.
1More generally, any ﬁnite extension of Q is considered to be a global ﬁeld and any ﬁnite extension of
Qp is considered to be a local ﬁeld. The completion of a global ﬁeld at any nontrivial absolute value is a
local ﬁeld.
1

<!-- page 2 -->
2
KEITH CONRAD
Example 2.2. Let m = 15 = 3 · 5. Its only prime factor that is congruent to 3 mod 4 is
3, which divides 15 only once. You can check that 15 is not a sum of two squares. The
number m = 45 = 32 · 5 is divisible by 3 two times and 45 = 9 + 36 = 32 + 62.
To reformulate Theorem 2.1 in terms of p-adic numbers, we describe when a (nonzero)
p-adic integer is a sum of two squares in Zp.
Theorem 2.3. For a prime p ≡1 mod 4, every p-adic integer is a sum of two squares of
p-adic integers.
Proof. If p ≡1 mod 4 then a theorem of Fermat from number theory says −1 mod p is a
square: −1 ≡s2
0 mod p for some integer s0. Then Hensel’s lemma lifts that up to saying
s2 + 1 = 0 has a solution in Zp: f(x) = x2 + 1 has f(s0) ≡0 mod p and f′(s0) = 2s0 ̸≡
0 mod p.
For each t in Zp,
(1 + t)2 + (s(t −1))2 = 1 + 2t + t2 −(t2 −2t + 1) = 4t,
so t = ((1 + t)/2)2 + (s(t −1)/2)2 and the numbers (1 + t)/2 and s(t −1)/2 are in Zp since
p ̸= 2.
□
Theorem 2.4. For a prime p ≡3 mod 4, a nonzero p-adic integer t is a sum of two squares
in Zp if and only if ordp(t) is even.
Proof. Write t = peu, with e ≥0 and u ∈Z×
p .
Step 1: We can write u = x2 + y2 for some x and y in Zp.
This will follow from the pigeonhole principle to solve the equation as a congruence mod
p ﬁrst and then from Hensel’s lemma to lift the solution mod p to a solution in Zp. We
start by considering the two sets
A = {y2 mod p : 0 ≤y ≤p −1},
B = {u −x2 mod p : 0 ≤x ≤p −1}.
For odd prime p, the number of squares in Z/(p), including 0, is (p + 1)/2.
Therefore
|A| = (p + 1)/2 and |B| = (p + 1)/2. Since |A| + |B| = p + 1 > |Z/(p)|, the sets A and
B must overlap by the pigeonhole principle: there are x0 and y0 from 0 to p −1 such that
y2
0 ≡u −x2
0 mod p, so u ≡x2
0 + y2
0 mod p. At least one of x0 or y0 is nonzero modulo p.
Since the congruence is symmetric in x0 and y0 we can assume without loss of generality
that x0 ̸≡0 mod p. Then deﬁne
f(X) = X2 + (y2
0 −u) ∈Zp[X].
We have f(x0) ≡0 mod p and f′(x0) = 2x0 ̸≡0 mod p, so by Hensel’s lemma there is an
x ∈Zp such that f(x) = 0, so x2 + y2
0 = u.
Step 2: e is even.
Write e = 2k. Then t = p2ku = p2k(x2 + y2) by Step 1, so t = (pkx)2 + (pky)2.
Step 3: e is odd.
Assuming t = x2 + y2 in Zp we will get a contradiction. Since ordp(t) is odd we can’t
have x or y equal to 0 (otherwise t would be a square, hence of even p-adic valuation). We
also must have ordp(x) = ordp(y), since if the two valuations were not equal then x2 and y2
would have diﬀerent valuations, making ordp(t) = max(2 ordp(x), 2 ordp(y)), which is even.
Write x = pnv and y = pnw where n ≥0 and v and w are in Z×
p . Then
t = x2 + y2 = p2n(v2 + w2).

<!-- page 3 -->
THE LOCAL-GLOBAL PRINCIPLE
3
Since ordp(t) is odd, v2 + w2 can’t be in Z×
p , so v2 + w2 ≡0 mod p. Thus v2 ≡−w2 mod p,
so −1 ≡(v/w)2 mod p. Therefore −1 is a square in Z/(p), and it is a classical fact that
−1 mod p is not a square if p ≡3 mod 4.2
□
Theorem 2.5. A nonzero 2-adic integer 2eu with u ∈Z×
2 is a sum of two squares in Z2 if
and only if u ≡1 mod 4.
Proof. Case 1: u ≡1 mod 4.
Lifting to modulus 8, either u ≡1 mod 8 or u ≡5 mod 8. Either way we will show u is
a sum of two squares in Z2.
If u ≡1 mod 8 then u = s2 = s2+02 for some s ∈Z2. If u ≡5 mod 8 then u/5 ≡1 mod 8,
so u/5 = s2 for some s ∈Z2 and that makes u = 5s2 = s2 + (2s)2.
The number 2 = 1 + 1 is a sum of two squares, and u is a sum of two squares. A product
of sums of two squares is a sum of two squares, from the classical identity
(a2 + b2)(c2 + d2) = (ac −bd)2 + (ad + bc)2,
so 2eu is a sum of two squares in Z2 for all e ≥0.
Case 2: u ≡3 mod 4.
Assume t = 2eu is a sum of two squares in Z2. Since 1/2 = 1/4 + 1/4 is a sum of two
squares in Q, u = t(1/2)e is a sum of two squares in Q2. We will now show a 2-adic integer
that is 3 mod 4 can’t be a sum of two squares in Q2, so we get a contradiction.
Suppose u = x2 + y2 in Q2. If x and y are both 2-adic integers then u ≡x2 + y2 mod 4;
the only squares mod 4 are 0 and 1, whose sum two at a time can be 0, 1, or 2 mod 4,
but not 3 mod 4. Therefore x or y is not in Z2. Without loss of generality x ̸∈Z2. Then
y2 = u −x2 with |x2|2 = |x|2
2 > 1 = |u|2, so |y2|2 = |u −x2|2 = |x2|2 > 1 by the strong
triangle inequality. Set |x|2 = 2n with n ≥1, so |y|2 = 2n too. Writing x = v/2n and
y = w/2n for 2-adic units v and w, we have v2 + w2 = 4nu ≡0 mod 4. Since units square
to 1 mod 4 we have v2 + w2 ≡2 mod 4, and that is a contradiction.
□
Here is Theorem 2.1 in terms of p-adic numbers.
Theorem 2.6. A nonzero integer is a sum of two squares in Z if and only if it is a sum of
two squares in R and in every Zp.
Proof. An integer that is a sum of two squares in Z is obviously a sum of two squares in R
and in every Zp.
Conversely, assume a nonzero integer m is a sum of two squares in R and in every Zp.
For a prime p dividing m with p ≡3 mod 4, its multiplicity ordp(m) is even by Theorem
2.4. Since m is assumed to be a sum of two squares in R we have m > 0. Then Theorem
2.1 implies m is a sum of two squares in Z.
□
This proof of Theorem 2.6 made no use of Theorems 2.3 (p ≡1 mod 4) or 2.5 (p = 2).
We could have dropped the use of R in Theorem 2.6 by looking instead at m in Z2: once
we know ordp(m) is even for primes p dividing m that are 3 mod 4, so the p-power in m is a
power of p2, which is ≡1 mod 4, we see that each odd prime power dividing m is 1 mod 4,
so m = ±2em′ where m′ ≡1 mod 4. Theorem 2.5 then implies ±m′ ≡1 mod 4, so the ±
sign has to be +.
2Here is a proof by contradiction: if −1 ≡s2 mod p then raising both sides to the (p −1)/2 power we get
(−1)(p−1)/2 ≡sp−1 ≡1 mod p by Fermat’s little theorem, and also (p −1)/2 is odd since p ≡3 mod 4, so
(−1)(p−1)/2 = −1. Thus −1 ≡1 mod p, a contradiction.

<!-- page 4 -->
4
KEITH CONRAD
3. The Local–Global Principle for quadratic forms
If we consider quadratic forms Q(x, y) = ax2 +by2 with a, b ∈Z−{0}, not just x2 +y2, it
is not true that being able to solve Q(x, y) = m in R and each Zp implies there is a solution
in Z.
Example 3.1. Consider x2 + 11y2 = 3. It obviously has no integer solutions, but has a
solution in R and each Zp. Solvability in R is clear, and solvability in Zp for p ̸= 2 or 11
follows from solving the congruence x2 ≡3 −11y2 mod p using the pigeonhole principle (as
in the proof of Theorem 2.4) and then applying Hensel’s lemma.
To prove solvability in Z2, from 3/11 ≡1 mod 8 we see that 3/11 is a square in Z2, so
we can solve 02 + 11y2 = 3 in Z2.
In Z11, since 3 ≡52 mod 11 we can solve x2 + 11 · 02 = 3 in Z11.
Example 3.2. Consider 2x2 + 7y2 = 1.
There are no integer solutions, but there is
a real solution and there is a solution in Zp for p ̸= 2 or 7 by solving the congruence
2x2 ≡1 −7y2 mod p with the pigeonhole principle and then using Hensel’s lemma.
In Z2 with x = 1 the equation becomes y2 = −1/7, which has a 2-adic solution since
−1/7 ≡1 mod 8.
In Z7 we can solve 2x2 = 1 by Hensel’s lemma since 1/2 ≡4 mod 7.
Using reduction and the Chinese remainder theorem, a polynomial equation with integer
coeﬃcients that has solutions in Zp for all p has a solution as a congruence mod m for all
m ≥2: x2 + 11y2 ≡3 mod m and 2x2 + 7y2 ≡1 mod m are both solvable for all m. Thus
we see that being able to solve a polynomial equation as a congruence in every modulus
does not imply (in general) that we can ﬁnd a solution to the polynomial equation in Z.
While the equations in the previous two examples lack integer solutions, they both have
rational solutions. For example, x2 + 11y2 = 3 has solutions (1/2, 1/2) and (4/3, 1/3) and
2x2 +7y2 = 1 has solutions (1/3, 1/3) and (3/5, 1/5). This is a clue that solutions in Q and
Qp might be a more robust concept than solutions in Z and Zp, and this turns out to be
the case.
Theorem 3.3 (Hasse–Minkowski). Let Q(x1, . . . , xn) be a quadratic form with rational
coeﬃcients.
1) For c ∈Q× the equation Q(x) = c has a solution in Q if and only if it has a solution
in R and every Qp.
2) The equation Q(x) = 0 has a solution in Q besides (0, . . . , 0) if and only if it has a
solution in R and every Qp besides (0, . . . , 0).
Moreover, in both cases when n ≥2, the solvability in Qp is automatic unless p = 2 or some
coeﬃcient3 of Q(x) is not in Z×
p .
The point of the last part of the Hasse–Minkowski theorem is that solvability in R and
every Qp actually does not involve an inﬁnite set of completions, but only ﬁnitely many:
R, Q2, and Qp for the odd primes p dividing a numerator or denominator of a coeﬃcient
of Q(x).
The signiﬁcance of reducing the task of solving an equation in rational numbers to solving
it in real and p-adic numbers instead (where the solutions in diﬀerent completions need
not have any a priori connection to each other) is that it is much easier to determine if a
3This is actually correct only if Q is in diagonal form: Q = a1x2
1 + · · · + anx2
n, with no mixed terms.
Every quadratic form with rational coeﬃcients can be put into diagonal form by a linear change of variables.

<!-- page 5 -->
THE LOCAL-GLOBAL PRINCIPLE
5
polynomial equation has a solution in a complete ﬁeld than in a ﬁeld like Q: an approximate
solution can often be reﬁned to an exact solution using limits. For example, the equation
x2 + y2 −z2 = c clearly has a real solution for every c ∈Q× because we see both plus and
minus signs. The condition for a quadratic form equation over Qp to be solvable in Qp is
a bit harder than checking signs of coeﬃcients, but it is algorithmic and can be found in
detailed treatments of the Hasse–Minkowski theorem. (See [5].)
4. Counterexamples
If we move beyond quadratic forms, which have degree 2, to polynomial equations of
degree 3 or higher, then we ﬁnd more counterexamples to the local-global principle for
Z-solutions as we saw in Examples 3.1 and 3.2 and also even counterexamples to the local–
global principle for Q-solutions.
Example 4.1. The equation y2 = x3 −51 has the rational solution (1375/9, 50986/27),
which is a solution in Zp for p ̸= 3. At p = 3 set x = 1 to make the equation y2 = −50,
which has a solution in Z3 since −50 ≡1 mod 3. Therefore the equation y2 = x3 −51 has
a solution in R (obviously) and in each Zp,4 but by methods of algebraic number theory or
elliptic curves it can be shown this equation has no solution in integers.
Example 4.2. Here is a famous example of Selmer [9]: the cubic equation
3x3 + 4y3 + 5z3 = 0
has a solution other than (0, 0, 0) in R and in each Qp, but it has no solution in Q other
than (0, 0, 0).
In R we have the solution ( 3p
5/3, 0, −1). To show there is a solution besides (0, 0, 0) in
each Qp we follow a method I learned from Kevin Buzzard. The basic idea is to show there
is a nonzero solution modulo p and then lift that solution p-adically by Hensel’s lemma. We
will separately treat the cases p = 3, p = 5, and p ̸= 3 or 5.
To ﬁnd a 3-adic solution, set x = 0 and z = −1, making the equation 4y3 −5 = 0, or
y3 = 5/4. Although 5/4 ≡−1 mod 9 and −1 is a 3-adic cube, this congruence modulo 9
isn’t sharp enough to conclude by Hensel’s lemma that 5/4 is a 3-adic cube: to use Hensel’s
lemma (in the form |f(α)|3 < |f′(α)|2
3), we seek an α ∈Z×
3 such that |α3 −5/4|3 < 1/9,
i.e., α3 ≡5/4 mod 27. The choice α = 2 works, so 5/4 is a 3-adic cube and we can solve
Selmer’s equation in Q3 as (0, y, −1) where y3 = 5/4 in Z3.
If p ̸= 3 and the p-adic integer a is a nonzero cube mod p then a is a cube in Z×
p by
Hensel’s lemma for X3 −a. In particular, for p = 5, set y = −1 and z = −1 to make
Selmer’s equation 3x3 −4 −5 = 0, or x3 = 3. Since 3 ≡23 mod 5, by Hensel’s lemma for
X3 −3 with approximate solution 2 we see that 3 is a 5-adic cube. We get a 5-adic solution
to Selmer’s equation as (x, −1, −1) where x3 = 3 in Z5.
From now on let p be a prime other than 3 or 5 (this includes allowing p = 2). Then
3, 5 ̸≡0 mod p. We are going to look at the group (Z/(p))×, which is cyclic of order p −1.
What proportion of the group is ﬁlled up by cubes?
• If p ≡1 mod 3 then the cubes in (Z/(p))× are a subgroup of index 3.
• If p ̸≡1 mod 3 then (3, p −1) = 1, so every number in (Z/(p))× is a cube.
If 3 mod p is a cube then 3 is a cube in Zp by Hensel’s lemma for X3 −3, so we can solve
Selmer’s equation as (x, −1, −1) where x3 = 3 in Qp.
4More generally, for every integer k the equation y2 = x3 + k has a solution in R and in every Zp.

<!-- page 6 -->
6
KEITH CONRAD
If 3 mod p is not a cube then not all numbers in (Z/(p))× are cubes. Thus p ≡1 mod
3, so the nonzero cubes mod p are a subgroup of (Z/(p))× that has index 3 and coset
representatives {1, 3, 9}: for every a ̸≡0 mod p we have a ≡b3, 3b3, or 9b3 mod p for some
b ̸≡0 mod p. We will apply this with a = 5.
• If 5 ≡b3 mod p then 5 is a cube in Zp by Hensel’s lemma for X3 −5, and we can
solve Selmer’s equation as (−y, y, −1) where y3 = 5 in Zp.
• If 5 ≡3b3 mod p then 5/3 is a cube in Zp by Hensel’s lemma and we can solve
Selmer’s equation as (x, 0, −1) where x3 = 5/3.
• If 5 ≡9b3 mod p then 5 · 3 = 15 is a cube in Zp by Hensel’s lemma and we can solve
Selmer’s equation as (3t, 5, −7) where t3 = 15. That is, 3a3 + 4b3 + 5c3 = 0 where
a = 3t, b = 5, and c = −7. By homogeneity there is a solution (3t/7, 5/7, −1) too.
This completes the proof that Selmer’s equation has local solutions everywhere. That the
equation has no rational solution besides (0, 0, 0) is harder. There are proofs using algebraic
number theory [4] or elliptic curves [3, pp. 86–87].
This example implies 3x3 + 4y3 = 5 has a solution in R and every Qp since in each
completion we found a solution to 3x3 + 4y3 + 5z3 = 0 where z = −1.
Even though the local–global principle for cubic equations is not always true, the Birch
and Swinnerton-Dyer conjecture describes a relationship between the behavior of rational
solutions of cubic equations (elliptic curves) and their real and p-adic solutions.
5. Local–global principle for powers
We start with a simple example of how the local–global principle manifests itself for
powers of rational numbers.
Theorem 5.1. A rational number is an nth power in Q if and only if it is an nth power
in R and every Qp.
Proof. The “only if” direction is clear. Assume now that r ∈Q and we can solve xn = r in
R and in each Qp. To prove r is an nth power in Q we can assume r ̸= 0.
For each prime p appearing in r (in either the numerator or denominator), the assumption
that r is an nth power in Qp implies ordp(r) is divisible by n.
Therefore every prime
appearing in r shows up within an nth power, so r = ±sn for some s ∈Q. If n is odd then
we can absorb the sign into s and r is an nth power in Q. if n is even then the fact that r
is an nth power in R forces r > 0, so r = sn is again an nth power in Q.
□
This theorem was not hard to prove, but it has reﬁnements that lie deeper. For example,
when n = 2 there is a local–global theorem for rational squares that allows any ﬁnite
number of completions to be removed without changing the conclusion: if r ∈Q× and r
is a square in all but at most ﬁnitely many completions from R and each Qp then in fact
r = s2 for some s ∈Q×. Since the proof of Theorem 5.1 was based on looking in Qp for
each p dividing the numerator or denominator of r, proving Theorem 5.1 without having
each Qp available is a challenge. As an example, how could we prove −2 is not a square
in Q from local considerations if we are not allowed to work in R and Q2? We could do
this by working in Q5 since −2 is not a square there (because −2 mod 5 is not a square),
and if we are not allowed to work in Q5 either then we could work in Q7 (where −2 is not
a square). More generally, it can be shown from the quadratic reciprocity law in number
theory that −2 is not a square in Qp if p ≡5, 7 mod 8 and also that there are inﬁnitely

<!-- page 7 -->
THE LOCAL-GLOBAL PRINCIPLE
7
many primes satisfying each of those congruence conditions, so we can always show −2 is
not a square using local considerations if any ﬁnite number of completions is removed.
Theorem 5.1 with ﬁnitely many completions removed works not just for n = 2, but for all
n up to 7. That is, if 2 ≤n ≤7 then the nth powers in Q× are precisely the nonzero rational
numbers that are nth powers in all but ﬁnitely many completions of Q. However, when
n = 8 the pattern breaks: being an 8th power in all but at most ﬁnitely many completions
of Q need not imply being an 8th power in Q.
Example 5.2. We show 16 is an 8th power in every completion of Q except Q2. Write
X8 −16 = (X4 −4)(X4 + 4) = (X2 −2)(X2 + 2)(X2 + 2X + 2)(X2 −2X + 2).
The two quadratic factors both have discriminant −4, so there is an 8th root of 16 in a
completion of Q as long as that completion contains a square root of 2 or −2 or −4.
Clearly 2 is a square in R. For each odd prime p, one of the numbers 2, −2, or −4 is a
square in (Z/(p))× (more generally, if a, b ̸≡0 mod p then a, b, or ab is a square in (Z/(p))×
– this is because the squares in (Z/(p))× are a subgroup of index 2), so 2, −2, or −4 is a
square in Qp by Hensel’s lemma. Therefore 16 an 8th power in every completion of Q other
than Q2, where it obviously is not since ord2(16) is not a multiple of 8.
A similar example occurs for each n divisible by 8 (and not for any other n): 2n/2 is an
nth power in each Qp and R except for Q2. Indeed, in each of those ﬁelds we can write
16 = x8 so 2n/2 = 16n/8 = xn. Here is a version of this story using just modular arithmetic
rather than anything p-adic.
Theorem 5.3. For a ∈Z, if xn ≡a mod p is solvable for all but ﬁnitely many primes p
then a = bn for some b ∈Z if 8 ∤n, and a is either bn or 2n/2bn for some b ∈Z if 8 | n.
When p ∤n and p ∤a, solvability of the mod p congruence xn ≡a mod p in Z/(p) and
solvability of the equation xn = a in Zp are equivalent by Hensel’s lemma.
Theorem 5.3 was ﬁrst proved by Trost [11] in 1934.5 Nobody noticed and the theorem was
rediscovered by Ankeny and Rogers [1] in 1951. The criterion describing when a nonzero
number in Q or any ﬁnite extension of Q is an nth power if it is an nth power in all but
ﬁnitely many completions is called the Grunwald–Wang Theorem [14]. It was originally just
Grunwald’s theorem (1933), with no exceptional case recognized when 8 | n, until Wang [12]
found a counterexample to it 15 years after Grunwald’s paper appeared [6] and 6 years after
Whaples [13] had published a second proof of Grunwald’s incorrect theorem. The setting in
which Wang worked was suﬃciently technical that the very simple form of Example 5.2 as
a counterexample was not noticed for a while. That is probably how [1] could appear a few
years after [12] in the same journal with no mention of their connection or the link to [11].
6. Local-global principle for heights
In number theory, a useful way to measure the computational complexity of a rational
number r is by the size of its numerator and denominator when r is written in reduced
form: if r = a/b where a and b are relatively prime integers, we set the height of r to be
(6.1)
H(r) = max(|a|, |b|).
(The numerator and denominator in reduced form are only deﬁned up to scaling by −1, but
this ambiguity does not aﬀect the value of the height.) For example, H(0) = max(0, 1) = 1,
5For prime n, a proof of Trost’s theorem is in [7, pp. 57–58] for n = 2 and [7, pp. 220-221] for n ̸= 2.

<!-- page 8 -->
8
KEITH CONRAD
H(2/3) = 3, and H(−9/6) = H(−3/2) = 3. The height is always a positive integer, so
H(r) ≥1. While there are inﬁnitely many rational numbers with ordinary absolute value
up to a given bound, there are only ﬁnitely many rational numbers having height up to a
given bound.6 This makes the height a useful means of counting rational numbers.
The formula (6.1) is biased towards the archimedean absolute value on Q. There turns
out to be an alternate formula for the height with two beneﬁts: all the absolute values on Q
participate on an equal footing and the formula does not require r to be written in reduced
form. We present it in Theorem 6.2 below after a brief but important lemma.
Lemma 6.1 (Product formula). For r ∈Q×, Q
v |r|v = 1, where v runs over primes and
∞, with | · |∞being the archimedean absolute value on Q.
Proof. Since |r|p = 1 when p does not divide the numerator or denominator of r, the product
Q
v |r|v has only ﬁnitely many terms in it that might not be 1. Writing r = a/b for nonzero
integers a and b, we have Q
v |r|v = (Q
v |a|v)/(Q
v |b|v), so it suﬃces to prove the lemma
when r = a is an integer. If a = ±1 then Q
v |a|v = 1 since each |a|v is 1. Otherwise
write a by its prime factorization: a = ±pe1
1 · · · pek
k where the pi are distinct primes. Then
|a|∞= pe1
1 · · · pek
k , |a|pi = 1/pei
i , and |a|p = 1 if p ̸∈{p1, . . . , pk}, so
Y
v
|a|v = |a|∞|a|p1 · · · |a|pk = pe1
1 · · · pek
k
1
pe1
1
· · · 1
pek
k
= 1.
□
The product formula seems innocuous, but it is a fundamental result gluing together all
the diﬀerent absolute values of Q and can in fact be taken as a starting point for algebraic
number theory [2].
Theorem 6.2. Let r ∈Q be rational. Then
H(r) =
Y
v
max(|r|v, 1),
where the product runs over all absolute values of Q.7
Example 6.3. If r = 3/2 then |r|v = 1 for v ̸∈{∞, 2, 3} and
Y
v
max(|r|v, 1) = max(|r|∞, 1) max(|r|2, 1) max(|r|3, 1) = 3
2 · 2 · 1 = 3 = H(r).
If r = 2/3 then
Y
v
max(|r|v, 1) = max(|r|∞, 1) max(|r|2, 1) max(|r|3, 1) = 1 · 1 · 3 = 3 = H(r).
Proof. In the product Q
v max(|r|v, 1) only ﬁnitely many factors are not 1 since that is true
about |r|v. Therefore this inﬁnite product is really just a ﬁnite product, with the terms not
equal to 1 depending on r.
Let the reduced form of r be a/b. Then
Y
v
max(|r|v, 1) =
Y
v
max
a
b

v , 1

.
6Explicitly, |{r ∈Q : H(r) ≤x}| = (12/π2)x2 + O(x log x) as x →∞.
7Strictly speaking we should say something like all “normalized” absolute values of Q, since
p
| · |∞and
| · |3
7 are also absolute values. We are using a set of absolute values on Q that ﬁt together into the product
formula.

<!-- page 9 -->
THE LOCAL-GLOBAL PRINCIPLE
9
Multiplying this by 1 in the form Q
v |b|v, from the product formula, we get
Y
v
max
a
b

v , 1

=
Y
v
|b|v
Y
v
max
|a|v
|b|v
, 1

=
Y
v
|b|v max
|a|v
|b|v
, 1

=
Y
v
max (|a|v, |b|v)
and now we use the fact that a and b are relatively prime integers: for each prime p, |a|p ≤1
and |b|p ≤1, with either |a|p = 1 or |b|p = 1 because p can’t divide both a and b. Thus
max(|a|p, |b|p) = 1 for all p, so
Y
v
max (|a|v, |b|v) = max(|a|∞, |b|∞),
which by deﬁnition is the height of r.
□
More generally, for n ≥1 and rational numbers r0, . . . , rn that are not all 0 we have
(6.2)
Y
v
max(|r0|v, . . . , |rn|v) = max(|a0|∞, . . . , |an|∞)
where a0, . . . , an are the numerators of the ri’s when we write them with a least common
denominator d: ri = ai/d for all i. (Necessarily the numerators a0, . . . , an are relatively
prime as an n-tuple, since otherwise d would not be a least common denominator.) When
n = 1, r0 = r, and r1 = 1 we recover Theorem 6.2 from (6.2) since r = a/b and 1 = b/b
is the representation of r and 1 with least common denominator when a/b is the reduced
form of r.
If we replace ri in (6.2) with sri for some common factor s ∈Q× then the left side of
(6.2) is unchanged by the product formula (Q
v |s|v = 1). This makes (6.2) the starting
point for the study of heights on projective n-space over Q.
References
[1] N. C. Ankeny and C. A. Rogers, A Conjecture of Chowla, Annals of Math. 53 (1951), 541–550.
[2] E. Artin and G. Whaples, Axiomatic Characterization of Fields by the Product Formula for Valuations,
Bull. Amer. Math. Soc. 51 (1945), 469–492.
[3] J. W. S. Cassels, “Lectures on Elliptic Curves,” Cambridge Univ. Press, Cambridge, 1991.
[4] K. Conrad, Selmer’s Example, https://kconrad.math.uconn.edu/blurbs/gradnumthy/selmerexample.
pdf.
[5] A. Gamzon, The Hasse–Minkowski Theorem, UConn Honors Thesis, 2006. URL http://digital
commons.uconn.edu/srhonors theses/17/.
[6] W. Grunwald, Ein allgemeines Existenztheorem f¨ur algebraische Zahlk¨orper, J. Reine Angew. Math. 169
(1933), 103–107.
[7] K. Ireland and M. Rosen, “A Classical Introduction to Modern Number Theory,” 2nd ed., Springer,
1990.
[8] P. Roquette, In Memoriam Ernst Steinitz, http://www.rzuser.uni-heidelberg.de/∼ci3/STEINITZ.pdf.
[9] E. Selmer, The Diophantine equation ax3 + by3 + cz3 = 0, Acta Arithmetica 85 (1951), 203–362.
[10] E. Steinitz, Algebraische Theorie der K¨orper, J. reine angew. Math. 137 (1910), 167-309
[11] E. Trost, Zur Theorie der Potenzreste, Nieuw Arch. Wisk. 18 (1934), 58–61.
[12] S. Wang, A Counter-Example to Grunwald’s Theorem, Annals of Math. 49 (1948), 1008–1009.
[13] G. Whaples, Non-analytic class ﬁeld theory and Grunwald’s theorem, Duke Math. J. 9 (1942), 455–473.
[14] Wikipedia, Grunwald–Wang Theorem, https://en.wikipedia.org/wiki/Grunwald-Wang_theorem.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*