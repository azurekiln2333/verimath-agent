# Pell's Equation II

> **Source**: https://kconrad.math.uconn.edu/blurbs/pelleqn2.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PELL’S EQUATION, II
KEITH CONRAD
1. Introduction
In Part I we met Pell’s equation x2 −dy2 = 1 for nonsquare d in Z+.1
We stated
Lagrange’s theorem that every Pell equation has a nontrivial solution (an integral solution
besides (±1, 0)) and saw what all solutions to x2−dy2 = 1 are if there’s a nontrivial solution.
As in Part I, “solution” means integral solution. Here we will prove Lagrange’s theorem
in Section 2 and show in Section 3 how to ﬁnd all solutions of a generalized Pell equation
x2 −dy2 = n. Examples are in Section 4.
2. Pell’s Equation has a Nontrivial Solution
Our proof that x2−dy2 = 1 has a nontrivial solution will be nonconstructive. The starting
point is the following lemma about integral multiples of
√
d that are close to integers.
Lemma 2.1. For each nonsquare positive integer d, there are inﬁnitely many positive in-
tegers x and y such that |x −y
√
d| < 1/y.
The point here is not just that there are integral multiples of
√
d close to integers, but
the distance can be controlled by the multiplier on
√
d (inﬁnitely often).
Proof. We use the pigeonhole principle. For each integer m ≥2 consider the m+1 numbers
(2.1)
0,
√
d, 2
√
d, . . . , m
√
d.
The fractional part of every real number is in [0, 1). View [0, 1) as m half-open intervals
[0, 1/m), [1/m, 2/m), . . . , [(m −1)/m, 1). By the pigeonhole principle, two of the m + 1
numbers in (2.1), say a
√
d and b
√
d with a < b, have fractional parts in the same interval,
so
(2.2)
a
√
d = A + ε,
b
√
d = B + δ,
where A, B ∈Z and ε and δ lie in a common half-open interval [i/m, (i + 1)/m). Thus
|ε −δ| < 1
m.
This inequality is strict since [i/m, (i + 1)/m) is a half-open interval. Using (2.2),
|ε −δ| < 1
m =⇒
(a
√
d −A) −(b
√
d −B)
 < 1
m =⇒
(B −A) −(b −a)
√
d
 < 1
m.
Set x = B −A and y = b −a, so x and y are integers with 0 < y ≤m. Thus
(2.3)
|x −y
√
d| < 1
m ≤1
y.
This implies x is positive: since |x −y
√
d| < 1, x > y
√
d −1 ≥
√
d −1 > 0.
1See https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf.
1

<!-- page 2 -->
2
KEITH CONRAD
Having found a pair (x, y) in Z+ such that |x −y
√
d| < 1/y, to get a second such pair
choose m′ ∈Z+ where 1/m′ < |x −y
√
d|. (Such an m′ exists since x −y
√
d ̸= 0, as
√
d is
irrational.) Run through the argument above with m′ in place of m to ﬁnd x′ and y′ in Z+
such that |x′ −y′√
d| < 1/m′ with y′ ≤m′, so |x′ −y′√
d| < 1/y′. Since
(2.4)
|x′ −y′√
d| < 1
m′ < |x −y
√
d|,
the pair (x, y) is not the pair (x′, y′). By repeating this argument again to get a smaller
|x′′ −y′′√
d|, and so on, we are done.
□
Example 2.2. Let d = 7. We will give two solutions to |x −y
√
7| < 1/y. Taking m = 10,
among the fractional parts of k
√
7 for 0 ≤k ≤10 (given to two decimal places in the
table below) are three pairs of integers (a, b) where a
√
7 and b
√
7 lie in a common interval
[i/10, (i + 1)/10), so the fractional parts diﬀer by less than 1/10: (a, b) = (2, 5), (4, 7), and
(6, 9). For all three pairs, b −a = 3.
k
0
1
2
3
4
5
6
7
8
9
10
Fractional part of k
√
7
0
.64
.29
.93
.58
.22
.87
.52
.16
.81
.45
Using a = 2 and b = 5, we have
2
√
7 = 5.29 . . . , 5
√
7 = 13.22 . . . =⇒|(2
√
7−5)−(5
√
7−13)| < 1
10 =⇒|8−3
√
7| < 1
10 < 1
3,
so we can use (x, y) = (8, 3). The choices (a, b) = (4, 7) and (6,9) also lead to (x, y) = (8, 3).
To get another pair (x′, y′) in Z+ where |x′−y′√
7| < 1/y′, since |8−3
√
7| ≈.0627 > 1/20
look at the fractional parts of k
√
7 for 0 ≤k ≤20 and ﬁnd two fractional parts in the same
interval [i/20, (i+1)/20) so they diﬀer by less than 1/20. This happens when k is 0 and 14:
0
√
7 = 0,
14
√
7 = 37.0405 . . . ,
so
|(0
√
7 −0) −(14
√
7 −37)| ≈.04 < 1
20 =⇒|37 −14
√
7| < 1
20 < 1
14
and we can use (x′, y′) = (37, 14). This also happens when k is 2 and 19:
2
√
7 = 5.2915 . . . ,
19
√
7 = 50.2692 . . . ,
so
|(2
√
7 −5) −(19
√
7 −50)| ≈.02 < 1
20 =⇒|45 −17
√
7| < 1
20 < 1
14,
which means we can use (x′, y′) = (45, 17).
What we used about
√
d in Lemma 2.1 is that it is irrational and greater than 1. A
similar argument shows that for irrational α ∈R, |x −yα| < 1/y for inﬁnitely many pairs
of integers (x, y) with y > 0 (give up on requiring x > 0 if α < 0).
Theorem 2.3 (Lagrange). For every positive integer d that is not a square, the equation
x2 −dy2 = 1 has a nontrivial solution.

<!-- page 3 -->
PELL’S EQUATION, II
3
Proof. Lagrange’s proof [7, pp. 669–731] used continued fractions. In the proof here, we
will start by showing there’s a nonzero integer M such that x2 −dy2 = M has inﬁnitely
many solutions x and y in Z+. Then we’ll combine this with modular arithmetic to show
x2 −dy2 = 1 has a solution in Z+. The pigeonhole principle will be used twice.
By Lemma 2.1, |x −y
√
d| < 1/y for inﬁnitely many x and y in Z+. We will show
|x2 −dy2| < 1 + 2
√
d
for all such x and y. What matters here is that the upper bound does not involve x or y;
that it happens speciﬁcally to be 1 + 2
√
d is not crucial.
First we will bound x from above in terms of y:
x = x −y
√
d + y
√
d ≤|x −y
√
d| + y
√
d < 1
y + y
√
d ≤1 + y
√
d.
Then
|x2 −dy2| = (x + y
√
d)|x −y
√
d| < (1 + y
√
d + y
√
d)1
y = 1
y + 2
√
d ≤1 + 2
√
d.
Thus |x2 −dy2| < 1 + 2
√
d for inﬁnitely many pairs of positive integers (x, y). By the
pigeonhole principle, there is an M ∈Z with |M| < 1 + 2
√
d such that
(2.5)
x2 −dy2 = M
for inﬁnitely many pairs of positive integers (x, y). We know M ̸= 0 since
√
d is irrational.
For x and y in Z+ satisfying (2.5), reduce them mod |M|. By the pigeonhole principle, the
inﬁnitely many pairs (x mod |M|, y mod |M|) have a repetition inﬁnitely often since there
are ﬁnitely many pairs mod |M|. (Here we use M ̸= 0.) So there are (x1, y1) and (x2, y2)
in Z+ ﬁtting (2.5) such that x1 ≡x2 mod |M|, y1 ≡y2 mod |M|, and (x1, y1) ̸= (x2, y2).
Since x1 ≡x2 mod |M| and y1 ≡y2 mod |M|, we have x1 = x2 + Mk and y1 = y2 + Mℓ
for some k and ℓin Z. Then
x1 + y1
√
d = x2 + y2
√
d + M(k + ℓ
√
d),
x1 −y1
√
d = x2 −y2
√
d + M(k −ℓ
√
d).
Since M = x2
2 −dy2
2 = (x2 +y2
√
d)(x2 −y2
√
d), plugging this into the equations above gives
x1 + y1
√
d = (x2 + y2
√
d)(1 + (x2 −y2
√
d)(k + ℓ
√
d))
(2.6)
x1 −y1
√
d = (x2 −y2
√
d)(1 + (x2 + y2
√
d)(k −ℓ
√
d)).
(2.7)
Combine like terms in the second factor on the right in (2.6) to make it x+y
√
d with x, y ∈Z
(we don’t know they’re positive). The second factor on the right in (2.7) is x −y
√
d, so
x1 + y1
√
d = (x2 + y2
√
d)(x + y
√
d)
x1 −y1
√
d = (x2 −y2
√
d)(x −y
√
d).
Multiplying these last two equations together, we get M = M(x2−dy2). Thus x2−dy2 = 1.
We have x ̸= 0 since d > 0. If y = 0 then x = ±1. If (x, y) = (1, 0) then x1 = x2 and y1 = y2,
but this contradicts the fact that (x1, y1) and (x2, y2) are diﬀerent. If (x, y) = (−1, 0) then
x1 = −x2, but this contradicts the fact that x1 and x2 are positive. Thus y ̸= 0.
Since x ̸= 0 and y ̸= 0, by changing signs on x and y in case either is negative we get a
solution to x2 −dy2 = 1 with x and y in Z+.
□

<!-- page 4 -->
4
KEITH CONRAD
Remark 2.4. Without the congruences mod |M| in the proof, from just x2
1 −dy2
1 = M
and x2
2 −dy2
2 = M we can’t say x1 + y1
√
d = (x2 + y2
√
d)(x + y
√
d) where x, y ∈Z (and
x2 −dy2 = 1). For example, 52 −2·32 = 7, 32 −2·12 = 7 , and 5+3
√
2 = (3+
√
2)(9
7 + 4
7
√
2)
where (9/7, 4/7) is a solution to x2 −2y2 = 1, but it is not an integral solution.
3. Solving the Generalized Pell Equation
We saw in the previous section that Pell’s equation has a nontrivial solution.
Using
a nontrivial solution of Pell’s equation we will describe a method to write down all the
solutions of a generalized Pell equation x2 −dy2 = n, where n is a nonzero integer. In
particular, if such an equation has no solutions then the method will tell us that.
The key algebraic idea is that solutions to x2 −dy2 = n remain solutions when multiplied
by solutions of x2 −dy2 = 1: if a2 −db2 = 1 and x2 −dy2 = n then the coeﬃcients of the
product x′ + y′√
d := (a + b
√
d)(x + y
√
d) satisfy x′2 −dy′2 = n, which you can check.
Example 3.1. A solution of x2 −7y2 = 29 is (6, 1) and a solution of x2 −7y2 = 1 is (8, 3).
From (6 +
√
7)(8 + 3
√
7) = 69 + 26
√
7, a second solution of x2 −7y2 = 29 is (69, 26).
In words, we have shown a Pell multiple of a solution of x2 −dy2 = n is again a solution,
where a “solution” means either the pair (x, y) or the number x+y
√
d and a “Pell multiple”
of it means either the coeﬃcients (ax + dby, ay + bx) of the product (a + b
√
d)(x + y
√
d)
where a2 −db2 = 1 or the product itself. The special case n = 1 is a result we saw in Part
I: the product of two Pell solutions is again a Pell solution (for the same d, of course).
Being a Pell multiple is a symmetric relation: if x′ + y′√
d = (x + y
√
d)(a + b
√
d) where
a2 −db2 = 1 then x + y
√
d = (x′ + y′√
d)(a −b
√
d) and a2 −d(−b)2 = 1. To check if two
numbers x + y
√
d and x′ + y′√
d are Pell multiples, form their ratio and rationalize the
denominator to check the coeﬃcients are integers that satisfy Pell’s equation. For example,
1 +
√
3 is a Pell multiple of 1 −
√
3 since their ratio is −2 −
√
3, which is a solution of
x2 −3y2 = 1, while 4+
√
3 and 4−
√
3 are not Pell multiples since their ratio (19+8
√
3)/13
does not even have integer coeﬃcients.
Our goal is to show there is a ﬁnite list of solutions to x2 −dy2 = n such that every
other solution is a Pell multiple of one of them. That is, up to allowing multiplication by
Pell solutions to generate new solutions there are only ﬁnitely many essentially diﬀerent
solutions of a generalized Pell equation.
Example 3.2. We’ll see in Example 4.1 that the integral solutions of x2 −6y2 = 3 occur
as x + y
√
6 = ±(3 +
√
6)(5 + 2
√
6)k for some k ∈Z, where 52 −6 · 22 = 1, so each solution
x + y
√
6 is a Pell multiple of 3 +
√
6.
Theorem 3.3. Fix u = a + b
√
d where a2 −db2 = 1 with a and b in Z+.
For each
n ∈Z −{0}, every integral solution of x2 −dy2 = n is (x′ + y′√
d)uk where x′2 −dy′2 = n,
k ∈Z, and
(3.1)
|x′| ≤
p
|n|(√u + 1/√u)
2
and |y′| ≤
p
|n|(√u + 1/√u)
2
√
d
.
If n > 0 then we can take |y′| ≤√n(√u −1/√u)/(2
√
d) < √nu/(2
√
d).
Proof. We will use absolute values and logarithms. For (x, y) ∈Z2 −{(0, 0)} deﬁne
L(x + y
√
d) = (log |x + y
√
d|, log |x −y
√
d|) ∈R2.

<!-- page 5 -->
PELL’S EQUATION, II
5
The crucial algebraic property is L(αβ) = L(α) + L(β) for all α and β in Z[
√
d] −{0}.
Check this. In particular, L(αk) = kL(α) for k ∈Z.
Since (a + b
√
d)(a −b
√
d) = a2 −db2 = ±1, we have |a −b
√
d| = 1/u > 0, so
L(u) = log(log u, log(1/u)) = (log u, −log u) = (log u)(1, −1).
This vector is linearly independent of (1, 1) since log u > 0 (we have u > 1 since u = a+b
√
d
with a and b in Z+), so {(1, 1), L(u)} is a basis of R2. Thus when x2 −dy2 = n we have
(3.2)
L(x + y
√
d) = c1(1, 1) + c2L(u)
for some real numbers c1 and c2. See Figure 1.
(1, 1)
L(u)
L(x + y
√
d)
c1(1, 1)
c2L(u)
1
1
−1
Figure 1. L(x + y
√
d) as a linear combination of L(1) and L(u).
Writing out the coordinates on both sides of (3.2),
(log |x + y
√
d|, log |x −y
√
d|) = (c1 + c2 log u, c1 −c2 log u).
Adding the coordinates lets us solve for c1:
c1 = log |x + y
√
d| + log |x −y
√
d|
2
= log |(x + y
√
d)(x −y
√
d)|
2
= log |n|
2
.
Thus when x2 −dy2 = n, (3.2) becomes
(3.3)
L(x + y
√
d) = log |n|
2
(1, 1) + c2L(u).
Let k ∈Z minimize |c2 −k| so δ := c2 −k has |δ| ≤1
2. Then (3.3) says
L(x + y
√
d) = log |n|
2
(1, 1) + (k + δ)L(u) = log |n|
2
(1, 1) + kL(u) + δL(u).
Since kL(u) = L(uk), we have
(3.4)
L((x + y
√
d)u−k) = L(x + y
√
d) −kL(u) = log |n|
2
(1, 1) + δL(u).
Set x′ + y′√
d = (x + y
√
d)u−k, which has integer coeﬃcients since u and u−1 have integer
coeﬃcients, so x + y
√
d = (x′ + y′√
d)uk where x′2 −dy′2 = n (since a2 −db2 = 1) and
(3.5)
(log |x′ + y′√
d|, log |x′ −y′√
d|) =
log |n|
2
+ δ log u, log |n|
2
−δ log u

.

<!-- page 6 -->
6
KEITH CONRAD
One of ±δ is ≤0 and the other is ≥0. Since |δ| ≤1
2 and log u > 0, the coordinate in
(3.5) where ±δ ≥0 is at most (log |n|)/2 + (log u)/2 = log
p
|n|u and the coordinate where
±δ ≤0 is at most (log |n|)/2 = log
p
|n|. Therefore one of |x′ + y′√
d| or |x′ −y′√
d| is at
most
p
|n|u and the other is at most
p
|n|.
To bound |x′| and |y′| from bounds on |x′ + y′√
d| and |x′ −y′√
d|, we will use
(3.6)
|x′| = |(x′ + y′√
d) + (x′ −y′√
d)|
2
,
|y′| = |(x′ + y′√
d) −(x′ −y′√
d)|
2
√
d
.
Set s := max(|x′ + y′√
d|, |x′ −y′√
d|). The two numbers |x′ + y′√
d| and |x′ −y′√
d| have
product |x′2 −dy′2| = |n|, so these two numbers are s and |n|/s in some order. Thus
|x′| = |(x′ + y′√
d) + (x′ −y′√
d)|
2
≤|x′ + y′√
d| + |x′ −y′√
d|
2
= 1
2

s + |n|
s

.
We saw one of s or |n|/s is at most
p
|n|, so the other is at least
p
|n|. Since s is a maximum,
p
|n| ≤s ≤
p
|n|u. By calculus, t + |n|/t is increasing for t ≥
p
|n|, so
|x′| ≤1
2

s + |n|
s

≤1
2
 
p
|n|u +
|n|
p
|n|u
!
=
p
|n|(√u + 1/√u)
2
and
|y′| ≤|x′ + y′√
d| + |x′ −y′√
d|
2
√
d
=
1
2
√
d

s + |n|
s

≤
p
|n|(√u + 1/√u)
2
√
d
.
When n > 0, we can sharpen the bound on |y′|. The equation x′2 −dy′2 = n implies
x′ + y′√
d and x′ −y′√
d have the same sign (their product is positive). Since |x′ + y′√
d|
and |x′ −y′√
d| are s and n/s in some order, x′ + y′√
d and x′ −y′√
d are either s and n/s
in some order or −s and −n/s in some order. Either way,
|y′| = |(x′ + y′√
d) −(x′ −y′√
d)|
2
√
d
= |s −n/s|
2
√
d
.
Since √n ≤s ≤√nu, we have
p
n/u ≤n/s ≤√n, so s and n/s lie in the interval
[
p
n/u, √nu]. Therefore |s −n/s| is at most the length of that interval, which tells us
|y′| = |s −n/s|
2
√
d
≤
√nu −
p
n/u
2
√
d
=
√n
2
√
d
√u −1
√u

.
□
The bounds on |x′| and |y′| in Theorem 3.3 when n > 0 satisfy the generalized Pell
equation: if x′ = √n(√u + 1/√u)/2 and y′ = √n(√u −1/√u)/(2
√
d), then x′2 −dy′2 = n
(it’s not important what number u is). These bounds on |x′| and |y′| may not be in Z, but
we’ll see in Examples 4.1 and 4.4 that the bounds sometimes are in Z. In the appendix,
inﬁnitely many examples are given where the bounds in (3.1) are in Z and are the smallest
solution of x′2 −dy′2 = n in Z+.
Remark 3.4. The ﬁrst bounds I learned for |x′| and |y′| were |x′| ≤(|n| + u)/2 and
|y′| ≤(|n| + u)/(2
√
d), which is in [1, p. 244].
A careful reading of the derivation of
those bounds in [1] shows that |x′| ≤
p
|n|u and |y′| ≤
p
|n|u/d, which is sharper since
√
ab ≤(a+b)/2 (the arithmetic-geometric mean inequality), and that was what I originally
wrote in Theorem 3.3. That those bounds on |x′| and |y′| can be cut down by essentially

<!-- page 7 -->
PELL’S EQUATION, II
7
a factor of 2, as in (3.1), was shown to me by Yosei Lii, who also explained the drop by a
factor of 2 just from the triangle inequality in (3.6) without any calculus:
|x′ + y′√
d| + |x′ −y′√
d| ≤
p
|n|u +
p
|n| =
p
|n|(√u + 1),
so
(3.7)
|x′| =

(x′ + y′√
d) + (x′ −y′√
d)
2
 ≤|x′ + y′√
d| + |x′ −y′√
d|
2
≤
p
|n|(√u + 1)
2
and
(3.8)
|y′| =

(x′ + y′√
d) −(x′ −y′√
d)
2
√
d
 ≤|x′ + y′√
d| + |x′ −y′√
d|
2
√
d
≤
p
|n|(√u + 1)
2
√
d
.
The bounds (3.7) and (3.8) are weaker than the bounds in (3.1) since 0 < 1/√u < 1, but
the distinction between these two bounds on |x′| and |y′| is negligible in practice. I later
learned that the bounds in Theorem 3.3 were found by Chebyshev in 1851 [2, pp. 260, 262].
A generalization of the bound on |y′| in (3.1) is in [5, Theorem 4.5].
When n = 1, there is no guarantee that an integral solution (x′, y′) to x′2 −dy′2 = 1
ﬁtting the bounds on |x′| and |y′| in (3.1) is not the trivial solution (1, 0). More generally,
when n is a perfect square, an integral solution to x′2 −dy′2 = n ﬁtting (3.1) might have
y′ = 0. Of course Theorem 3.3 is useless when n = 1 since the bounds in this theorem
depend on already knowing a number u = a + b
√
d with a, b ∈Z+ where a2 −db2 = 1.
When n is not a perfect square, integral solutions (x′, y′) to x′2 −dy′2 = n must have y′ ̸= 0.
For example, the bounds in Theorem 3.3 can be used for n = −1 to determine whether
the so-called negative Pell equation x2 −dy2 = −1 has an integral solution once we know a
nontrivial solution to a2 −db2 = 1.
Corollary 3.5. For a generalized Pell equation x2 −dy2 = n with n ̸= 0 there is a ﬁnite
set of solutions such that every solution is a Pell multiple of one of these solutions.
Proof. We may assume there is a solution. To prove the conclusion, here are two proofs.
Proof #1: Each solution is a Pell multiple of a solution with |x| ≤
p
|n|(√u + 1/√u)/2
and |y| ≤
p
|n|(√u + 1/√u)/(2
√
d) by Theorem 3.3, so x and y have ﬁnitely many choices.
Proof #2: By the end of the proof of Theorem 2.3, if x2
1−dy2
1 = M and x2
2−dy2
2 = M with
x1 ≡x2 mod |M| and y1 ≡y2 mod |M| then we can write x2+y2
√
d = (x1+y1
√
d)(x+y
√
d)
where x2 −dy2 = 1. Thus x1 + y1
√
d and x2 + y2
√
d are Pell multiples. Replacing M with
n, all integral solutions of x2 −dy2 = n with the same reduction mod |n| are Pell multiples
of each other, so there are at most n2 diﬀerent solutions of x2 −dy2 = n up to Pell multiples
since there are at most n2 pairs of integers mod |n|.
□
The second proof of Corollary 3.5, unlike the ﬁrst, is not practical because it is not
computationally eﬀective: it doesn’t give a bounded range of x and y values that contain
the solutions of x2 −dy2 = n up to a Pell multiple. In particular, the second proof can’t
show x2 −dy2 = n has no solutions while the ﬁrst proof can, as we’ll see in Example 4.5.
Remark 3.6. For the negative Pell equation x2−dy2 = −1, with squarefree d, the existence
of a solution in Z requires no prime factor of d to be 3 mod 4. Among squarefree d > 0 with
no prime factor that is 3 mod 4, the proportion for which x2 −dy2 = −1 has a solution in
Z is 1 −Q
odd j≥1(1 −1/2j) (≈58%) by a theorem of Koymans and Pagano [6].

<!-- page 8 -->
8
KEITH CONRAD
4. Examples of Theorem 3.3
We now apply Theorem 3.3 in several examples to see how it works in practice. In all
cases but the last one we’ll have n > 0, so we’ll use the bound on |y′| at the end of the
theorem rather than the bound on |y′| in (3.1).
Example 4.1. We will describe all the solutions of x2 −6y2 = 3 in integers. An obvious
solution is (3, 1) and its sign changes in coordinates (3, −1), (−3, 1), and (−3, −1). What
are all the integral solutions?
As a positive solution of a2 −6b2 = 1 we will take (a, b) = (5, 2), so set u = 5 + 2
√
6.
By the end of Theorem 3.3, |y′| ≤
p
|n|(√u −1/√u)/(2
√
d) =
√
3(√u −1/√u)/(2
√
6) = 1,
which forces y′ to be 1, 0, or −1. Solutions to x′2 −6y′2 = 3 with such y′-values are (±3, 1)
and (±3, −1). (In particular, the bound on |y′| at the end of Theorem 3.3 is optimal in this
case.) Thus the integral solutions of x2 −6y2 = 3 have the form
x+y
√
6 = (±3+
√
6)(5+2
√
6)k = (±3+
√
6)uk
or
(±3−
√
6)(5+2
√
6)k = (±3−
√
6)uk,
where k ∈Z. Up to multiplication by powers of u, there are four solutions:
3 +
√
6,
−3 +
√
6,
3 −
√
6,
−3 −
√
6.
These four solutions are related in pairs by powers of u: 3 −
√
6 = (3 +
√
6)u−1, and
−3+
√
6 = (−3−
√
6)u−1. Therefore every solution of x2 −6y2 = 3 in integers has the form
x + y
√
6 = ±(3 +
√
6)(5 + 2
√
6)k
for some k ∈Z and this list has no repetitions.
Taking k = 0, 1, 2, the values of (3+
√
6)(5+2
√
6)k are 3+
√
6, 27+11
√
6, and 267+109
√
6,
so the ﬁrst three solutions of x2 −6y2 = 3 in Z+ are (3, 1), (27, 11), and (267, 109).
Example 4.2. We will completely solve x2 −7y2 = 57 in integers.
One nontrivial solution of a2−7b2 = 1 is (8, 3), so set u = 8+3
√
7. By the end of Theorem
3.3, |y′| ≤
√
57(√u −1/√u)/(2
√
7) ≈5.33. The integral solutions to x′2 −7y′2 = 57 for
such y′ are (x′, y′) = (±8, ±1) and (±13, ±4).
The integral solutions of x2 −7y2 = 57 therefore have the form
(4.1)
x + y
√
7 = ±(8 ±
√
7)uk
or
± (13 ± 4
√
7)uk
with k ∈Z. No pair of numbers among 13 ± 4
√
7 and 8 ±
√
7 has a ratio that is a power of
u (in fact, no pair has a ratio of the form m + n
√
7 with m, n ∈Z). Therefore (4.1) has no
repetitions.
The solution (x, y) = (20, 7) appears in (4.1) as 20 + 7
√
7 = (13 −4
√
7)u.
Example 4.3. We will completely solve x2 −19y2 = 36 in integers. An obvious pair of
solutions is (±6, 0). What are the rest?
A nontrivial solution of a2 −19b2 = 1 in positive integers is (170, 39) (this solution has
the smallest positive b), so let u = 170 + 39
√
19.
By the end of Theorem 3.3, |y′| ≤
√
36(√u −1/√u)/(2
√
19) ≈12.65, so (x′, y′) = (±6, 0) and (±44, ±10).
Therefore the
integral solutions to x2 −19y2 = 36 have the form
x + y
√
19 = ±6uk
or
± (44 ± 10
√
19)uk
with k ∈Z. These solutions have no repetitions since no pair among 6, −6, 44 + 10
√
19,
and 44 −10
√
19 has a ratio that is a power of u.
The solution (x, y) = (70, 16) appears as 70 + 16
√
7 = (44 −10
√
19)u.

<!-- page 9 -->
PELL’S EQUATION, II
9
Example 4.4. We will completely solve x2 −103y2 = 2 in integers.
A solution of a2 −103b2 = 1 in positive integers is (227528, 22419) (this solution has the
smallest positive b), so let u = 227528 + 22419
√
103. By the end of Theorem 3.3, |y′| ≤
√
2(√u−1/√u)/(2
√
103) = 47. The only nonnegative y′ in this range where x′2−103y′2 = 2
for some x′ ∈Z is y′ = 47, for which x′ = ±477. (As in Example 4.1, the bound on |y′| this
time is optimal.) Therefore the integral solutions to x2 −103y2 = 2 have the form
x + y
√
103 = ±(477 ± 47
√
103)uk
with k ∈Z. These solutions have repetitions since 477 −47
√
103 = (477 + 47
√
103)/u,2 so
the integral solutions to x2 −103y2 = 2 without repetitions are
x + y
√
103 = ±(477 + 47
√
103)uk.
Example 4.5. We will show x2 −37y2 = 11 has no integral solution.
A solution of a2 −37b2 = 1 is (73, 12), so let u = 73 + 12
√
37. By the end of Theorem
3.3, |y′| ≤
√
11(√u −1/√u)/(2
√
37) ≈3.27. For no y′ in this range is x′2 −37y′2 = 11 for
an x′ ∈Z, so the equation x2 −37y2 = 11 has no solution in Z.
Example 4.6. We will show x2 −194y2 = −1 has no integral solution.
A solution of a2 −194b2 = 1 is (195, 14).
Using u = 195 + 14
√
194 in (3.1), since
n = −1 < 0, |y′| ≤
√
1(√u + 1)/(2
√
194) ≈0.71 < 1. The only choice is y′ = 0, for which
x′2 −194y′2 = −1 has no integral solution x′. Thus x2 −34y2 = −1 has no solution in Z.
Example 4.7. We will show x2 −733y2 = 383 has no integral solution.
A solution of a2−733b2 = 1 is (195307849, 7213860),3 so let u = 195307849+7213860
√
733.
Since
√
383(√u −1/√u)/(2
√
733) ≈7143.19, we use a computer to search through all y′
from 0 to 7143 and in no case is 733y′2 + 383 a perfect square. Therefore x2 −733y2 = 383
has no solution in Z.
At the end of Remark 3.4 it was mentioned that the bounds |y′| ≤
p
|n|(√u+1/√u)/(2
√
d)
(for all n) and |y′| ≤√n(√u −1/√u)/(2
√
d) (for n > 0) are not in practice substantially
better than the bound |y′| ≤
p
|n|(√u + 1)/(2
√
d). The table below illustrates this by
comparing such bounds for most of the examples in this section (those where n > 0).
Example
x2 −dy2 = n
√n(√u −1/√u)/(2
√
d)
√n(√u + 1)/(2
√
d)
4.1
x2 −6y2 = 3
1
1.46
4.2
x2 −7y2 = 57
5.33
7.12
4.3
x2 −19y2 = 36
12.65
13.37
4.4
x2 −103y2 = 2
47
47.06
4.5
x2 −37y2 = 11
3.27
3.56
4.7
x2 −733y2 = 383
7143.19
7143.55
The website https://www.alpertron.com.ar/QUAD.HTM will give you all the solutions
to x2 −dy2 = n as a recursive sequence (xn, yn) or tell you there are no integral solutions.
Although Theorem 3.3 provides a general method to show x2 −dy2 = n has no solutions,
the lack of solutions can often be proved more simply using congruences, as seen in Part I.
2If x2 −dy2 = ±2, then the ratio (x + y
√
d)/(x −y
√
d) is a unit in Z[
√
d].
3Yes, this is the smallest solution in positive integers a and b.

<!-- page 10 -->
10
KEITH CONRAD
Example 4.8. There is no solution to x2 −37y2 = 2 in Z since x2 −37y2 ≡2 mod 4 has
no solution: the congruence is x2 −y2 ≡2 mod 4 and the squares mod 4 are 0 and 1, which
don’t diﬀer by 2.
Congruence methods do not always suﬃce to prove there are no solutions in Z. The
equations x2 −37y2 = 11 and x2 −194y2 = −1, which we met in Examples 4.5 and
4.6, are instances of this.
They have no Z-solutions but they have rational solutions:
x2 −37y2 = 11 has solutions (9/2, 1/2) and (32/3, 5/3), and x2 −194y2 = −1 has solutions
(13/5, 1/5) and (5/13, 1/13). From these pairs of rational solutions it can be shown that
x2 −37y2 ≡11 mod m and x2 −194y2 ≡−1 mod m are each solvable for all m ≥2.
Exercise. Use the method of Example 4.5 to show x2 −37y2 = n has no solution in Z
for n = 3, 5, 6, 7, 8, 10.
For n = 5, 6, 8, and 10 the lack of Z-solutions to x2−37y2 = n can also be proved in a more
elementary way, as with n = 2, by showing there is no solution to either x2−37y2 ≡n mod 4
or x2 ≡n mod 37. This doesn’t work for n = 3 or n = 7, just as we saw it doesn’t for
n = 11: for all m ≥2 there is a solution to x2 −37y2 ≡3 mod m and x2 −37y2 ≡7 mod m.
5. Using Continued Fractions
In this section, for those who know about continued fractions, we will explain how Pell
and generalized Pell equations can be solved with continued fractions. The link between
continued fractions and generalized Pell equations is due to the next theorem of Lagrange
[4, Art. 38].
Theorem 5.1. If positive integers x and y satisfy x2 −dy2 = n with |n| <
√
d then x/y is
a convergent to the continued fraction of
√
d.
Proof. Our argument is taken from [9, p. 204]. A basic theorem about continued fractions
is that for a real number α, if x and y are integers with y ̸= 0 and |x/y −α| < 1/(2y2)
then x/y = p/q for some convergent p/q to α. (We can’t say x = p and y = q unless we
know gcd(x, y) = 1 and y > 0, and we’re not assured gcd(x, y) = 1 in general unless n is
squarefree.) Taking α =
√
d, if x2 −dy2 = n with |n| <
√
d and x, y > 0 then

x
y −
√
d
 =
|n|
y2(x/y +
√
d)
<
√
d
y2(x/y +
√
d)
=
1
y2(x/(y
√
d) + 1)
,
so to show |x/y −
√
d| < 1/(2y2), and hence x/y is a convergent to
√
d, it suﬃces to prove
x/(y
√
d) > 1, or equivalently x > y
√
d. If n > 0 then x2 −dy2 = n > 0 =⇒x2 > dy2, so
x > y
√
d since x and y are positive.
If n < 0 then x2 −dy2 < 0 =⇒x < y
√
d and our argument breaks down. Instead of
looking at x/y as an approximation to
√
d, look at y/x as an approximation to 1/
√
d:

y
x −1
√
d
 =
|n|
√
dx(y
√
d + x)
=
|n|
dx2(y/x + 1/
√
d)
<
1
x2(
√
dy/x + 1)
.
This is less than 1/(2x2) if
√
dy/x > 1, or equivalently x < y
√
d, which is true, so y/x is a
convergent to 1/
√
d. If
√
d = [a1, a2, a3, . . . ] then a1 ≥1 so 1/
√
d = [0, a1, a2, . . . ],4 which
4A continued fraction [a1, a2, a3, . . .] with a1 < 0 has a much more complicated rule for the continued
fraction of its reciprocal than when a1 ≥0: see https://kconrad.math.uconn.edu/blurbs/ugradnumthy/
contfrac-neg-invert.pdf. Fortunately we’re not dealing with a1 < 0 here.

<!-- page 11 -->
PELL’S EQUATION, II
11
means the convergents to
√
d are the reciprocals of the convergents to 1/
√
d after the initial
convergent 0. Thus y/x being a convergent to 1/
√
d makes x/y a convergent to
√
d.
□
Corollary 5.2. For each positive solution to x2 −dy2 = ±1, there is a convergent p/q to
√
d such that x = p and y = q.
Proof. Apply Theorem 5.1 with n = ±1. In this case gcd(x, y) = 1 and y > 0, so x and y
are the numerator and denominator of a convergent to
√
d.
□
This corollary was the basis for Lagrange’s proof that Pell’s equation x2 −dy2 = 1 has
a nontrivial solution. He proved
√
d has a periodic continued fraction and explained where
to ﬁnd the positive solutions of x2 −dy2 = 1 among the convergents to
√
d.
Example 5.3. The continued fraction of
√
6 is [2, 2, 4], and the table of convergents below
suggests (and it is true) that every other convergent provides a solution to x2 −6y2 = 1.
2
2
4
2
4
2
4
2
4
2
4
0
1
2
5
22
49
218
485
2158
4801
21362
47525
211462
1
0
1
2
9
20
89
198
881
1960
8721
19402
86329
x2−6y2
−2
1
−2
1
−2
1
−2
1
−2
1
−2
Not only is the continued fraction of
√
d periodic, but so is x2 −dy2 when x/y runs
through the convergents to
√
d. All distinct values of x2 −dy2 when x/y is a convergent
to
√
d occur before the last term in the second period of the continued fraction. This and
Theorem 5.1 let us determine all n with 0 < |n| <
√
d such that x2 −dy2 = n has a solution.
Example 5.4. Since
√
13 = [3, 1, 1, 1, 1, 6], we compute x2 −13y2 in the table below where
x/y runs through convergents just before the second 6. Since
√
13 ≈3.6, the table tells us
the only n with 0 < |n| <
√
13 for which x2 −13y2 = n is solvable in Z are ±1 and ±3.
(Although ±4 appears in the bottom row of the table, | ± 4| >
√
13.)
3
1
1
1
1
6
1
1
1
1
0
1
3
4
7
11
18
119
137
256
393
649
1
0
1
1
2
3
5
33
38
71
109
180
x2−13y2
−4
3
−3
4
−1
4
−3
3
−4
1
If |n| >
√
d then solvability of x2−dy2 = n can be connected to solvability of x2−dy2 = n′
for some nonzero integer n′ where |n′| < |n|. Iterating this, eventually the case |n| <
√
d
is reached and we already explained how that can be settled using the continued fraction
of
√
d. Such a reduction process goes back to Lagrange [8, pp. 422–426], and more recent
references are [3, pp. 454-457] and [9, pp. 210–213]. We’ll illustrate this with two examples
that were treated in the previous section using Theorem 3.3.
Example 5.5. Consider x2 −6y2 = 3 with x, y ∈Z. Note 3 >
√
6. Reducing the equation
mod 3, we get x2 ≡0 mod 3, so x ≡0 mod 3. This is equivalent to x = 3z for z ∈Z, so
x2 −6y2 = 3 ⇐⇒9z2 −6y2 = 3
⇐⇒3z2 −2y2 = 1
⇐⇒−2y2 + (3z2 −1) = 0.

<!-- page 12 -->
12
KEITH CONRAD
Viewing the left side of the last equation as a quadratic polynomial in y, its discriminant
02 −4 · (−2) · (3z2 −1) = 4(6z2 −2)
is a perfect square, so 6z2 −2 = t2 for some t ∈Z, Write this as t2 −6z2 = −2 and note t is
even. Conversely, if integers t and z ﬁt t2−6z2 = −2 then x = 3z and y = ±
√
4t2/(2(−2)) =
±t/2 are integers that satisfy x2 −6y2 = 3.
If t, z ∈Z+ satisfy t2 −6z2 = −2 then t/z is a convergent to
√
6 since | −2| <
√
6. By
the table in Example 5.3 the ﬁrst three solutions of t2 −6z2 = −2 in Z+ are (t, z) = (2, 1),
(22, 9), and (218, 89), leading to (x, y) = (3z, t/2) = (3, 1), (27, 11), and (267, 109).
Example 5.6. Consider x2 −37y2 = 11 with x, y ∈Z. Note 11 >
√
37. We have x2 ≡
37y2 ≡(2y)2 mod 11, so x ≡±2y mod 11. Write x = ±2y + 11z with z ∈Z. Then
x2 −37y2 = 11 ⇐⇒(±2y + 11z)2 −37y2 = 11
⇐⇒−33y2 ± 44yz + (121z2 −11) = 0
⇐⇒−3y2 ± 4yz + (11z2 −1) = 0.
For the quadratic polynomial in y to be solvable in Z, its discriminant
(4z)2 −4 · (−3) · (11z2 −1) = 4(37z2 −3)
is a perfect square, so 37z2 −3 = t2 for some t ∈Z. Write this as t2 −37z2 = −3. All
steps are reversible, so if t2 −37z2 = −3 and y in Z ﬁts −3y2 ± 4yz + (11z2 −1) = 0 then
(x, y) = (±2y + 11z, y) satisﬁes x2 −37y2 = 11.
If t, z ∈Z+ satisfy t2 −37z2 = −3 then t/z is a convergent to
√
37 since | −3| <
√
37.
Testing the convergents p/q of the ﬁrst two periods of the continued fraction for
√
37, which
is [6, 12, 12, 12, . . . ], the only values of p2 −37q2 are ±1. Since −3 isn’t a value of p2 −37q2,
t2 −37z2 = −3 has no solution in Z and thus x2 −37y2 = 11 has no solution in Z, which
we found by another method in Example 4.5.
Exercise. Use the method of Example 5.6 to show x2 −37y2 = 7 has no solution in Z
by relating it to t2 −37z2 = −4.
Appendix A. Optimality of the bounds in Theorem 3.3
In Examples 4.1 and 4.4, the bound on |x′| in (3.1) and the bound on |y′| at the end of
Theorem 3.3 if n > 0 are the only solution in Z+ within the range of those bounds:
• the ﬁrst solution to x2 −6y2 = 3 in Z+ is (x, y) = (3, 1), and in Example 4.1 with
u = 5 + 2
√
6, √n(√u + 1/√u)/2 = 3 and √n(√u −1/√u)/(2
√
d) = 1,
• the ﬁrst solution to x2−103y2 = 2 in Z+ is (x, y) = (477, 47) and in Example 4.4 with
u = 227528+22419
√
103, √n(√u+1/√u)/2 = 477 and √n(√u−1/√u)/(2
√
d) = 47.
A third example is x2−23y2 = 2. The least unit greater than 1 in Z[
√
23] is u = 24+5
√
23,
with norm 1. Theorem 3.3 says integral solutions of x2 −23y2 = 2 are powers of u times
solutions where |x| ≤
√
2(√u + 1/√u)/2 = 5 and |y| ≤
√
2(√u −1/√u)/(2
√
23) = 1. The
only solution in that range in positive integers is (x, y) = (5, 1).
This naturally raises the question: are there inﬁnitely many equations x2−dy2 = n where
the bounds on |x′| and |y′| from Theorem 3.3 for n > 0 are optimal? Yes!
Theorem A.1. For an integer m ≥2, let d = m2 −2. The bounds on |x′| and |y′| in
Theorem 3.3 for the equation x2 −dy2 = 2 are |x′| ≤m and |y′| ≤1, and the only solution
in positive integers within those bounds is (x′, y′) = (m, 1).

<!-- page 13 -->
PELL’S EQUATION, II
13
The family of equations x2 −(m2 −2)y2 = 2 has x2 −23y2 = 2 as the special case m = 5.
Proof. The equation x2 −(m2 −2)y2 = 2 has no integral solution when y = 0, and when
y = 1 we have x = m.
For m ≥2, the smallest solution of a2 −(m2 −2)b2 = 1 in positive integers is (a, b) =
(m2 −1, m). Equivalently, the least unit of norm 1 that’s greater than 1 in Z[
√
m2 −2] is
m2 −1 + m
√
m2 −2: when m = 2, the fundamental unit of Z[
√
2] is 1 +
√
2, with norm
−1, and (1 +
√
2)2 = 3 + 2
√
2 = m2 −1 + m
√
m2 −2, while when m ≥3, the fundamental
unit of Z[
√
m2 −2] is m2 −1 + m
√
m2 −2 and it has norm 1. In Theorem 3.3, we can set
u = m2 −1 + m
√
m2 −2,
We will show the bounds from Theorem 3.3 for integral solutions of x2−(m2−2)y2 = 2 are
|x′| ≤m and |y′| ≤1. That makes the bounds from Theorem 3.3 optimal since (i) (x′, y′) =
(m, 1) is a solution, (ii) there’s no solution when y′ = 0, and (iii) when x′2 −(m2 −2)y′2 = 2
and y′ > 1, we have x′2 ≥4(m2 −2) + 2 > m2, so x′ > m.
To show the bounds on |x′| and |y′| from Theorem 3.3 are m and 1 means
√
2(√u + 1/√u)
2
= m,
√
2(√u −1/√u)
2
√
m2 −2
= 1.
Since u > 1, these equations are true if the squares of both sides are true, so we will check
u + 2 + 1/u
2
= m2,
u −2 + 1/u
2(m2 −2) = 1.
Both equations are equivalent to u2−2(m2−1)u+1 = 0, and u is a root of t2−2(m2−1)t+1
by the quadratic formula.
□
Theorem A.2. For an integer m ≥1, let d = 4m2 + 2. The bounds on |x′| and |y′| in
Theorem 3.3 for the equation x2 −dy2 = 2m2 + 1 are |x′| ≤2m2 + 1 and |y′| ≤m, and
(x, y) = (2m2 + 1, m) is a solution.
The equation x2 −(4m2 + 2)y2 = 2m2 + 1 becomes x2 −6y2 = 3 when m = 1.
In contrast to Theorem A.1, the smallest solution to x2 −(4m2 + 2)y2 = 2m2 + 1 in
positive integers might not be (x, y) = (2m2 + 1, m), but it does appear to be most of
the time. For 1 ≤m ≤100, there is no solution in positive integers where y ≤m −1
with three exceptions: m = 11 ((x, y) = (27, 1)), m = 12 ((x, y) = (51, 2)), and m = 70
((x, y) = (297, 2) and a second solution (1683, 12)). It would be nice to have a proof that
for inﬁnitely many m there is no solution in positive integers where y ≤m −1.
Proof. It is easy to check that (x, y) = (2m2+1, m) is a solution of x2−(4m2+2)y2 = 2m2+1.
View 4m2 + 2 as M2 + 2 for the even value M = 2m. For M ≥1, the fundamental
unit of Z[
√
M2 + 2] is M2 + 1 + M
√
M2 + 2 and it has norm 1, so the smallest solution
of a2 −(M2 + 2)b2 = 1 in positive integers is (a, b) = (M2 + 1, M). Letting M = 2m, in
Theorem 3.3 with d = M2 + 2 = 4m2 + 2, we can set u = (2m)2 + 1 + 2m
p
(2m)2 + 2 =
4m2 + 1 + 2m
√
4m2 + 2. In Theorem 3.3 we’ll show the bounds on |x′| and |y′| using u as
above are |x′| ≤2m2 + 1 and |y′| ≤m:
√
2m2 + 1(√u + 1/√u)
2
= 2m2 + 1,
√
2m2 + 1(√u −1/√u)
2
√
4m2 + 2
= m.
Since u > 1, these equations are true if the squares of both sides are true, so we will check
u + 2 + 1
u = 4(2m2 + 1),
u −2 + 1
u = 8m2.

<!-- page 14 -->
14
KEITH CONRAD
Both equations are equivalent to u2−(8m2+2)u+1 = 0, and u is a root of t2−(8m2+2)t+1
by the quadratic formula.
□
Is there an inﬁnite family of generalized Pell equations, including x2 −103y2 = 2 as a
special case, where the bounds on |x′| and |y′| in Theorem 3.3 are (inﬁnitely) often the ﬁrst
solution in positive integers? Here is my only attempt at answering this. Let’s think of 103
as m2 + 3 for m = 10. In terms of this m, the minimal solution (x, y) = (477, 47) has the
form (4m2 + 7m + 7, 4m + 7), and it’s straightforward to check
(4m2 + 7m + 7)2 −(m2 + 3)(4m + 7)2 = 8m2 −70m −98,
so we can view x2 −103y2 = 2 as the special case of x2 −(m2 + 3)y2 = 8m2 −70m −98 for
m = 10. Check 8m2 −70m −98 > 0 if m ≥10 (8t2 −70t −98 has larger root 9.97 . . .).
For m = 10 we are in Example 4.4, where the bounds on |x′| and |y′| in Theorem 3.3 for
x2 −103y2 = 2 are its ﬁrst solution (477, 47).
For m = 11, we have m2 + 3 = 124, 8m2 −70m −98 = 100, and the fundamental unit
of Z[
√
124] is 4620799 + 414960
√
124, with norm 1. Using this unit as u, the bounds on
|x′| and |y′| for x2 −124y2 = 100 in Theorem 3.3 are |x′| ≤15200 and |y′| ≤1365, but
(15200, 1365) is not the smallest solution in positive integers: two smaller solutions are
(134, 12) and (568, 51), with (4m2 + 7m + 7, 4m + 7) = (568, 51) when m = 11. (Of course
there is also the solution (x′, y′) = (10, 0).)
For m = 12, we have m2 + 3 = 147, 8m2 −70m −98 = 214, and the fundamental unit
of Z[
√
147] = Z[7
√
3] is 97 + 8
√
147, with norm 1. Using this unit as u, the bounds on
|x′| and |y′| for x2 −147y2 = 214 in Theorem 3.3 are |x′| ≤102.401 . . . and |y′| ≤8.359 . . .
(not integers). The only positive integer solution of x2 −147y2 = 214 in that range is
(x′, y′) = (19, 1), and the solution (x′, y′) = (4m2 + 7m + 7, 4m + 7) = (667, 55) is outside
that range. So in short, this attempt at ﬁtting x2 −103y2 = 2 into a nice inﬁnite family
where the bounds in Theorem 3.3 are optimal appears to be a failure.
References
[1] W. W. Adams, L. J. Goldstein, “Introduction to Number Theory,” Prentice-Hall, Englewood Cliﬀs, NJ,
1976.
[2] P. L. Chebyshev, Sur les formes quadratiques, J. Math. Pures Appl. 16 (1851), 257–282. URL https://
eudml.org/doc/234874.
[3] G. Chrystal, “Algebra, an Elementary Text-Book, Part II” Adam and Charles Black, Edinburgh, 1889.
URL https://archive.org/details/algebraanelemen08chrygoog/page/n7/mode/2up.
[4] L. Euler, “Elements of Algebra,” Longman, Hurst, Rees, Orme and Co., London 1822. URL
https://archive.org/details/elementsalgebra00lagrgoog/mode/2up.
[5] D. Flath, “Introduction to Number Theory,” Wiley-Interscience, New York, 1989.
[6] P. Koymans and C. Pagano, On Stevenhagen’s conjecture, https://arxiv.org/abs/2201.13424.
[7] J. L. Lagrange, Solution d’un probl`eme d’arithm´etique, Oeuvres de Lagrange, Tome I, Gauthier-
Villars, Paris, 1867, 669–731. URL https://archive.org/details/oeuvresdelagrang01lagr/page/
668/mode/2up.
[8] J. L. Lagrange, Sur la solution des probl`emes ind´etermin´es du second degr´e, Oeuvres de Lagrange, Tome
II, Gauthier-Villars, Paris, 1868, 377–535. URL https://archive.org/details/uvresdelagrange09nat
igoog/page/n389/mode/2up.
[9] J. E. Shockley, “Introduction to Number Theory,” Holt, Rinehart and Winston, New York, 1967.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*