# Pell's Equation I

> **Source**: https://kconrad.math.uconn.edu/blurbs/pelleqn1.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PELL’S EQUATION, I
KEITH CONRAD
1. Introduction
For a positive integer d that is not a square, an equation of the form
x2 −dy2 = 1
is called Pell’s equation. We are interested in solutions (x, y) where x and y are integers.
The term “solution” will always mean that kind of solution. The obvious solutions (x, y) =
(±1, 0) are called the trivial solutions. They are the only solutions where x = ±1 or y = 0
(separately). Solutions where x > 0 and y > 0 will be called positive solutions. Every
nontrivial solution can be made into a positive solution by changing the sign of x or y.
We don’t consider the case when d is a square, since if d = c2 with c ∈Z then x2 −dy2 =
x2 −(cy)2 and the only squares that diﬀer by 1 are 0 and 1, so x2 −(cy)2 = 1 =⇒x = ±1
and y = 0. Thus x2 −dy2 = 1 for square d only has the integral solutions (x, y) = (±1, 0).
In Section 2 we’ll show how solutions to Pell’s equation can be found. In Section 3 we’ll
discuss an elementary problem about polygonal numbers that is equivalent to a speciﬁc Pell
equation. Section 4 describes how to create new solutions of Pell’s equation if we know one
nontrivial solution and in Section 5 we will see how all solutions can be generated from a
minimal nontrivial solution. In Section 6 a generalized Pell equation is introduced, where
the right side is not 1. In Section 7 we look at the Pell-type equation with right side −1.
2. Examples of Solutions
To ﬁnd a nontrivial solution of x2 −dy2 = 1 by elementary methods, rewrite the equation
as x2 = dy2 +1 and then set y = 1, 2, 3, . . . until you reach a value where dy2 +1 is a perfect
square. Call that value x2 and then we have a solution (x, y).
Example 2.1. Two positive solutions of x2 −2y2 = 1 are (3, 2) and (17, 12), since 2y2 + 1
is a square when y = 2 and 12, where it has values 9 = 32 and 289 = 172. See below.
y
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
11
12
13
14
15
2y2 + 1
3
9
19
33
51
73
99
129
163
201
243
289
339
393
451
Square?
X
✓
X
X
X
X
X
X
X
X
X
✓
X
X
X
Example 2.2. Three positive solutions of x2 −3y2 = 1 are (2, 1) and (7, 4), and (26, 15),
as shown by the table below.
y
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
11
12
13
14
15
3y2 + 1
4
13
28
49
76
109
148
193
244
301
364
433
508
589
676
Square?
✓
X
X
✓
X
X
X
X
X
X
X
X
X
X
✓
1

<!-- page 2 -->
2
KEITH CONRAD
The table below gives a positive solution to x2 −dy2 = 1 for nonsquare d from 2 to 24
where x and y are as small as possible.
d
2
3
5
6
7
8
10
11
12
13
14
15
17
18
19
20
21
22
23
24
x
3
2
9
5
8
3
19
10
7
649
15
4
33
17
170
9
55
197
24
5
y
2
1
4
2
3
1
6
3
2
180
4
1
8
4
39
2
12
42
5
1
The theorem suggested by such data is a hard result of Lagrange.
Theorem 2.3 (Lagrange). For all d ∈Z+ that are not squares, the equation x2 −dy2 = 1
has a nontrivial solution.
This theorem, which will be proved in Part II1, is our hunting license to search for
solutions by tabulating dy2 + 1 until it takes a square value. We are guaranteed this search
will eventually terminate, but we are not assured how long it will take. In fact, the smallest
positive solution of x2 −dy2 = 1 can be unusually large compared to the size of d. The
table above illustrates this if we compare the smallest positive solutions when d = 12, 13,
and 14. As more extreme examples, see in the table below the smallest positive solutions
to x2 −dy2 = 1 when d = 61 and 109 compared with nearby values of d.
d
60
61
62
108
109
110
x
31
1766319049
63
1351
158070671986249
21
y
4
226153980
8
130
15140424455100
2
While Lagrange was the ﬁrst person to give a proof of Theorem 2.3, in 1768, a century
earlier Fermat claimed to have a proof and challenged other mathematicians in Europe to
prove it too. In a letter in 1657 he wrote that anyone failing this task should at least try
to ﬁnd a positive solution to x2 −61y2 = 1 and x2 −109y2 = 1, where he said he chose
small coeﬃcients “pour ne vous donner pas trop de peine” (so you don’t have too much
work). He clearly was being mischievous. Fermat had no idea that a nontrivial solution to
x2 −61y2 = 1 had been found in India (by Bhaskara II) 500 years before him.
3. Triangular–Square Numbers
A positive integer n is called triangular if n dots can be arranged like an equilateral
triangle. The ﬁrst four triangular numbers are 1 (a degenerate case), 3, 6, and 10. In the
pictures below, a new (shaded) side added to a triangular number leads to the next one.
T1 = 1
T2 = 3
T3 = 6
T4 = 10
For k ≥3, a k-gonal number is a positive integer n for which n dots can be arranged to
look like a regular k-gon. The ﬁrst four square and pentagonal numbers, corresponding to
k = 4 and k = 5, are shown below. Both sequences start with 1 as a degenerate case.
1See https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn2.pdf.

<!-- page 3 -->
PELL’S EQUATION, I
3
S1 = 1
S2 = 4
S3 = 9
S4 = 16
P1 = 1
P2 = 5
P3 = 12
P4 = 22
A formula for the nth square number Sn is obvious: Sn = n2. To get a formula for the
nth triangular and pentagonal numbers, Tn and Pn, the ﬁrst few values suggest how to
write them as a sum of terms in an arithmetic progression (which are their real deﬁnitions):
Tn = 1 + 2 + · · · + n =
n
X
k=1
k,
Pn = 1 + 4 + · · · + (3n −2) =
n
X
k=1
(3k −2).
This works for square numbers too: Sn = 1+3+· · ·+(2n−1) = Pn
k=1(2k −1) is n2. Using
the formula for the sum of terms in an arithmetic progression,
Tn = n(n + 1)
2
and
Pn = n(3n −1)
2
.
With these formulas we ﬁll in the table below of the ﬁrst 10 triangular, square, and pen-
tagonal numbers.
n
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
Tn
1
3
6
10
15
21
28
36
45
55
Sn
1
4
9
16
25
36
49
64
81
100
Pn
1
5
12
22
35
51
70
92
117
145
Besides the common value 1, we see 36 is both triangular and square: 36 = T8 = S6. Call
a positive integer a triangular–square number if it is both Tm for some m and Sn for some
n. Finding these numbers is the same as solving a particular Pell equation.
Theorem 3.1. Triangular–square numbers correspond to solutions of x2 −2y2 = 1 in
positive integers x and y.

<!-- page 4 -->
4
KEITH CONRAD
Proof. Using the formulas for Tm and Sn,
Tm = Sn ⇐⇒m(m + 1)
2
= n2
⇐⇒m2 + m = 2n2
⇐⇒

m + 1
2
2
−1
4 = 2n2
⇐⇒(2m + 1)2 −1 = 2(2n)2
⇐⇒(2m + 1)2 −2(2n)2 = 1.
Because every step is reversible, ﬁnding triangular–square numbers is equivalent to solving
x2 −2y2 = 1 in positive integers x and y where x = 2m + 1 is odd and y = 2n is even:
T(x−1)/2 = Sy/2. (While we want x = 2m+1 with m ≥1, we can say x > 0 instead of x ≥3
because the only solution of x2 −2y2 = 1 with x = 1 has y = 0, which is not positive.)
In the correspondence between triangular–square numbers and solutions of x2 −2y2 = 1,
we do not need to specify that x is odd and y is even since those constraints are forced by
the equation x2 −2y2 = 1. Indeed, rewriting it as x2 = 2y2 + 1 shows x2 is odd, so x is
odd. Then x = 2m + 1 for an integer m, and feeding that into the Pell equation makes
4m2 + 4m + 1 −2y2 = 1, so y2 = 2m2 + 2m. Thus y2 is even, so y is even.
□
Example 3.2. From the solutions (x, y) = (3, 2) and (17, 12) of x2 −2y2 = 1 we get the
triangular–square numbers T1 = S1 = 1 and T8 = S6 = 36 by writing x = 2m + 1 and
y = 2n in each case to ﬁnd m and n.
As practice with the ideas in the proof of Theorem 3.1, show that ﬁnding all square–
pentagonal numbers, which are numbers of the form Sm and Pn for some positive integers
m and n, is equivalent to solving x2 −6y2 = 1 in positive integers x and y satisfying the
constraint that x is one less than a multiple of 6. The ﬁrst three positive integer solutions
of x2 −6y2 = 1 are (5, 2), (49, 20), (485, 198), and the ﬁrst and third have x being one
less than a multiple of 6; they lead to the square–pentagonal numbers 1 = S1 = P1 and
9801 = S99 = P81 if you work out the details.
4. New Solutions from Old Solutions
We found in Section 2, by making a table, that two solutions of x2−2y2 = 1 are (3, 2) and
(17, 12). They are closely related when we convert the pair (x, y) into the number x + y
√
2:
(4.1)
17 + 12
√
2 = (3 + 2
√
2)2.
Let’s raise 3 + 2
√
2 to a few powers beyond the second:
(4.2) (3+2
√
2)3 = 99+70
√
2,
(3+2
√
2)4 = 577+408
√
2,
(3+2
√
2)5 = 3363+2378
√
2.
The coeﬃcient pairs (99,70), (577,408), and (3363,2378) are all solutions to x2 −2y2 = 1.
Similarly, we previously found three solutions of x2 −3y2 = 1: (2, 1), (7, 4), and (26, 15).
When we convert the pair (x, y) into the number x + y
√
3 we have
(4.3)
7 + 4
√
3 = (2 +
√
3)2
and
26 + 15
√
3 = (2 +
√
3)3.
The key to solving x2 −dy2 = 1 in Z is to study numbers of the form x + y
√
d where
x, y ∈Z. Such numbers are closed under multiplication:
(4.4)
(x + y
√
d)(x′ + y′√
d) = (xx′ + dyy′) + (xy′ + yx′)
√
d

<!-- page 5 -->
PELL’S EQUATION, I
5
and xx′ + dyy′ and xy′ + yx′ are both integers.2 This formula is similar to the rule for
multiplying complex numbers: (x + yi)(x′ + y′i) = (xx′ −yy′) + (xy′ + yx′)i, which is the
case d = −1 (for Pell’s equation we are taking d > 0).
Just as a complex number x + yi has a real part x and an imaginary part y, a number
x + y
√
d with x, y ∈Z has coeﬃcients x and y. The coeﬃcients of such a number are
unique: if x+y
√
d = x′ +y′√
d with x, y, x′, y′ ∈Z then x = x′ and y = y′. Indeed, if y ̸= y′
then
√
d = (x −x′)/(y′ −y) is rational, which is a contradiction (nonsquare integers have
irrational square roots). Thus y = y′, so x + y
√
d = x′ + y
√
d, which implies x = x′.
Theorem 4.1. If X2 −dY 2 = 1 has solutions (x, y) and (x′, y′) then the coeﬃcients of
(x + y
√
d)(x′ + y′√
d) are also a solution.
Proof. Using the coeﬃcients from (4.4) we compute
(xx′ + dyy′)2 −d(xy′ + yx′)2 = (x2x′2 + 2dxx′yy′ + d2y2y′2) −d(x2y′2 + 2xx′yy′ + y2x′2)
= x2x′2 + d2y2y′2 −dx2y′2 −dy2x′2
= x2(x′2 −dy′2) −dy2(x′2 −dy′2)
= (x2 −dy2)(x′2 −dy′2)
= 1.
□
Corollary 4.2. If X2−dY 2 = 1 has a solution (x, y) then the coeﬃcients of (x+y
√
d)k are
also a solution for all k ∈Z. In particular, this Pell equation has inﬁnitely many solutions
if it has a nontrivial solution.
Proof. The coeﬃcients of (x + y
√
d)k are solutions for k ≥1 by repeated multiplication
using Theorem 4.1. If (x, y) ̸= (±1, 0) then x + y
√
d ̸= ±1, so the powers (x + y
√
d)k for
k ≥1 are distinct and give us inﬁnitely many solutions of X2 −dY 2 = 1.
To show the coeﬃcients of (x + y
√
d)k are solutions for k < 0, write k = −K and set
(x + y
√
d)K = xK + yK
√
d with xK, yK ∈Z. Then x2
K −dy2
K = 1, so
(x + y
√
d)−K =
1
(x + y
√
d)K
=
1
xK + yK
√
d
=
xK −yK
√
d
(xK + yK
√
d)(xK −yK
√
d)
= xK −yK
√
d
x2
K −dy2
K
= xK −yK
√
d
and (xK, −yK) is a solution. Finally, the coeﬃcients of (x + y
√
d)0 are (1, 0).
□
Example 4.3. Since (3 + 2
√
2)4 = 577 + 408
√
2, we have (3 + 2
√
2)−4 = 577 −408
√
2.
If we were not dealing with solutions of Pell’s equation, negative powers might not have
integer coeﬃcients. e.g., (5 + 2
√
2)−1 = 5/17 −(2/17)
√
2.
2If we use a cube root instead of a square root, such sums would not be closed under multiplication, e.g.,
(1 +
3√
2)(1 −
3√
2) = 1 −
3√
4 ̸= x + y
3√
2 for x and y in Z.

<!-- page 6 -->
6
KEITH CONRAD
5. All Solutions to a Pell Equation
We will describe all solutions to x2 −dy2 = 1 using inequalities on numbers x + y
√
d.
Comparing the size of such numbers is not generally the same as comparing coeﬃcients:
x + y
√
d < x′ + y′√
d is not the same as x < x′ and y < y′. Consider 1 + 2
√
2 < 7 −
√
2.
But for Pell solutions, under a mild condition it is the same!
Lemma 5.1. If x2 −dy2 = 1 in Z and x + y
√
d > 1 then x ≥2 and y ≥1.
The example of x2 −3y2 = 1 for x = 2 and y = 1 shows the lower bounds on x and y
can be achieved.
Proof. The crucial point is that 1/(x + y
√
d) = x −y
√
d when x2 −dy2 = 1. Therefore
x + y
√
d > 1 > x −y
√
d > 0.
From x + y
√
d > x −y
√
d we get 2y
√
d > 0, so y > 0. Thus y ≥1 since y is an integer, so
x > y
√
d ≥
√
d > 1, which makes x ≥2.
□
Without a hypothesis like x2 −dy2 = 1 in Lemma 5.1 there are counterexamples: we can
have x + y
√
d > 1 when x < 1 or y < 0. For example, −2 + 3
√
2 > 1 and 5 −
√
2 > 1.
Lemma 5.2. Suppose x2 −dy2 = 1 and a2 −db2 = 1 in Z where x, y, a, b ≥0. Then
a + b
√
d < x + y
√
d ⇐⇒a < x and b < y ⇐⇒a < x or b < y.
Proof. The ﬁrst (⇐) is obvious.
To prove the ﬁrst (⇒), we have a ≥1 since a ≥0
by hypothesis and from a2 −db2 = 1 we can’t have a = 0 (why?).
Similarly, x ≥1.
Reciprocating the inequality of positive numbers
a + b
√
d < x + y
√
d
gives us
x −y
√
d < a −b
√
d.
Adding these inequalities, we get
(a + x) + (b −y)
√
d < (a + x) + (y −b)
√
d.
Subtracting a + x from both sides and dividing by
√
d we get b −y < y −b, so 2b < 2y and
thus b < y. Then a2 = 1 + db2 < 1 + dy2 = x2, so a < x from nonnegativity of a and x.
If a + b
√
d = x + y
√
d then a = x and b = y since
√
d is irrational. If a + b
√
d > x + y
√
d
then x + y
√
d < a + b
√
d, so x < a and y < b by swapping the roles of a and b with x and
y above. Thus the only way to have a < x or b < y is to have a + b
√
d < x + y
√
d.
□
Theorem 5.3. Assume x2 −dy2 = 1 has a solution in positive integers and let (x1, y1) be
such a solution where y1 is minimal. Then all solutions to x2 −dy2 = 1 in integers are, up
to sign, generated from (x1, y1) by taking integral powers of x1 + y1
√
d:
x + y
√
d = ±(x1 + y1
√
d)k
where k ∈Z. The solutions in positive integers have k ≥1 and the + sign out front.
Proof. By Corollary 4.2, for each k ∈Z the coeﬃcients of (x1 +y1
√
d)k satisfy x2 −dy2 = 1,
and clearly this is also true for coeﬃcients of −(x1 + y1
√
d)k.
Conversely, suppose integers x and y satisfy x2 −dy2 = 1. If x and y are positive we’ll
show x + y
√
d = (x1 + y1
√
d)k for some k ≥1.
Since x + y
√
d > 1 and the numbers

<!-- page 7 -->
PELL’S EQUATION, I
7
(x1 + y1
√
d)n for n = 0, 1, 2, . . . are an increasing sequence that starts at (x1 + y1
√
d)0 = 1
and tends to ∞, x + y
√
d lies between two powers of x1 + y1
√
d or equals one of them:
(5.1)
(x1 + y1
√
d)k ≤x + y
√
d < (x1 + y1
√
d)k+1
for some integer k ≥0. Dividing through (5.1) by (x1 + y1
√
d)k,
1 ≤(x + y
√
d)(x1 + y1
√
d)−k < x1 + y1
√
d.
The number (x + y
√
d)(x1 + y1
√
d)−k has coeﬃcients that are a Pell solution since Pell
solutions are closed under multiplying and raising to integer powers (Theorem 4.1, Corollary
4.2). Setting (x + y
√
d)(x1 + y1
√
d)−k = a + b
√
d for a, b ∈Z, we have a2 −db2 = 1 and
(5.2)
1 ≤a + b
√
d < x1 + y1
√
d.
If a + b
√
d > 1 then a and b are positive by Lemma 5.1, so b < y1 by (5.2) and Lemma 5.2.
This contradicts the minimality of y1 among positive Pell solutions, so a + b
√
d = 1. That
implies x + y
√
d = (x1 + y1
√
d)k. Since x ≥1 and y ≥1, k is not 0, so k ≥1.
What if x and y are not both positive? Then α := x + y
√
d is not in (1, ∞) by Lemma
5.1. If α ̸= ±1 then α is in one of the intervals (0, 1), (−1, 0), and (−∞, −1), so (exactly)
one of the numbers 1/α, −1/α, or −α is in (1, ∞). Each of these is a Pell solution too:
1
α =
1
x + y
√
d
= x −y
√
d,
−1
α = −(x −y
√
d) = −x + y
√
d,
−α = −x −y
√
d.
The number among these in (1, ∞) has positive coeﬃcients, so by our previous reasoning
±α±1 = (x1 +y1
√
d)K for some K ≥1 and some signs on the left side. Thus α = x+y
√
d =
±(x1 + y1
√
d)±K. If α = ±1 then it also arises in this way using K = 0.
□
Remark 5.4. For solutions x + y
√
d with x, y ∈Z+, the one with minimal y is also the
one with minimal x, since the coeﬃcients of (x1 + y1
√
d)k both increase with k.
Example 5.5. The positive solution of x2 −2y2 = 1 with least y-value is (3, 2), so every
positive solution comes from coeﬃcients of (3 + 2
√
2)n for n ≥1.
Example 5.6. The positive solution of x2 −3y2 = 1 with least y-value is (2, 1), so the
positive solutions are the coeﬃcients of (2 +
√
3)k for k ≥1.
Example 5.7. The positive solution of x2 −5y2 = 1 with least y-value is (9, 4), so every
positive solution comes from coeﬃcients of (9 + 4
√
5)k for k ≥1.
Example 5.8. For integral a ≥2, the positive solution of x2 −(a2 −1)y2 = 1 with least
y-value is (a, 1).3 Indeed, from y = 1 we get x2 = a2 −1 + 1 = a2, so x = a. Therefore the
solutions of x2 −(a2 −1)y2 = 1 in positive integers are the coeﬃcients of (a +
√
a2 −1)k for
k ≥1. The ﬁrst few powers are
(a +
p
a2 −1)1 = a +
p
a2 −1,
(a +
p
a2 −1)2 = 2a2 −1 + 2a
p
a2 −1,
(a +
p
a2 −1)3 = (4a3 −3a) + (4a2 −1)
p
a2 −1,
(a +
p
a2 −1)4 = (8a4 −8a2 + 1) + (8a3 −4a)
p
a2 −1.
3 The number a2 −1 is not a perfect square, since otherwise a2 −1 and a2 would be consecutive positive
integers that are perfect squares and that is impossible since successive positive squares spread out and the
least distance between them is 22 −12 = 3.

<!-- page 8 -->
8
KEITH CONRAD
Setting (a +
√
a2 −1)k = xk(a) + yk(a)
√
a2 −1, both xk(a) and yk(a) are polynomials with
integral coeﬃcients. They are called Chebyshev polynomials of the ﬁrst and second kind.
They grow quickly: it can be shown that ak ≤xk(a) ≤(2a)k and (2a −1)k−1 ≤yk(a) ≤
(2a)k−1.
Properties of xk(a) and yk(a) (in terms of growth and divisibility) have an application
to mathematical logic, in the solution of Hilbert’s Tenth Problem [1, Sect. 10.4], [2].
6. Generalized Pell Equations
The equation x2 −dy2 = n where n ∈Z −{0} is a generalized Pell equation. The special
case x2 −dy2 = −1 is called a negative Pell equation. To ﬁnd a solution (in Z) rewrite the
equation as x2 = dy2 + n and compute the right side for y = 1, 2, . . . until it’s a square.
In the tables below we try to solve x2 −2y2 = −1 and x2 −3y2 = −1. For 1 ≤y ≤15
two solutions are found for the ﬁrst equation, (1, 1) and (7, 5), and none for the second.
y
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
11
12
13
14
15
2y2 −1
1
7
17
31
49
71
97
127
161
199
241
287
337
391
449
Square?
✓
X
X
X
✓
X
X
X
X
X
X
X
X
X
X
y
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
11
12
13
14
15
3y2 −1
2
11
26
47
74
107
146
191
242
299
362
431
506
587
674
Square?
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
A longer search in the second case would be fruitless: x2 −3y2 = −1 has no integral
solutions. To prove some generalized Pell equation has no solution, an argument by con-
tradiction using modular arithmetic often works. Here are a few examples.
Example 6.1. If integers x and y satisfy x2 −3y2 = −1 then reduce both sides mod 3 to
get x2 ≡−1 mod 3. This congruence has no solution: the only squares mod 3 are 0 and 1.
Thus x2 −3y2 = −1 has no solution (in Z).
Example 6.2. The equation x2 −5y2 = 2 has no integral solution because reducing the
equation mod 5 makes it x2 ≡2 mod 5, which has no solution. By the same idea, the
generalized Pell equations x2 −5y2 = 3 and x2 −5y2 = 7 have no solutions.
Example 6.3. The equation x2 −5y2 = 6 has no solution, but we can’t prove this by
reducing both sides mod 5 to get x2 ≡6 mod 5, since that congruence has a solution so
there is no contradiction. Reduce mod 3 instead: the equation becomes x2−5y2 ≡0 mod 3,
or x2 ≡5y2 ≡2y2 mod 3. This too has a solution, namely (0, 0), so it doesn’t seem like
progress has been made. But this is progress because (0, 0) is the only solution mod 3, since
the squares mod 3 are 0 and 1, and the only way one of these is twice the other mod 3 is
when they’re both 0. Therefore if x2 −5y2 = 6 in Z then x and y are both multiples of 3.
That makes x2 −5y2 a multiple of 9, which contradicts it being 6.
We used modular arithmetic here (reducing mod 3), but in a more subtle way than in
the previous two examples.
Remark 6.4. The above three examples not only have no solutions in Z, but in fact have
no solutions in Q. In contrast, x2 −34y2 = −1 has no solution in Z but has solutions in Q,
such as (5/3, 1/3), (3/5, 1/5), (27/11, 5/11), and (3/29, 5/29).

<!-- page 9 -->
PELL’S EQUATION, I
9
Here is a problem about sums of squares whose solution is equivalent to solving a partic-
ular generalized Pell equation.
Theorem 6.5. Finding positive integers a and b satisfying
(6.1)
a2 + (a + 1)2 = b2 + (b + 1)2 + (b + 2)2
is the same as solving x2 −6y2 = 3 in positive integers x and y other than (3, 1).
Proof. Expanding the squares and combining like terms,
a2 + (a + 1)2 = b2 + (b + 1)2 + (b + 2)2 ⇐⇒2a2 + 2a + 1 = 3b2 + 6b + 5
⇐⇒2(a2 + a) = 3(b2 + 2b) + 4
⇐⇒2
 
a + 1
2
2
−1
4
!
= 3((b + 1)2 −1) + 4
⇐⇒((2a + 1)2 −1) = 6((b + 1)2 −1) + 8
⇐⇒(2a + 1)2 −6(b + 1)2 = 3.
All steps are reversible, so solving (6.1) for positive integers a and b is equivalent to solving
x2 −6y2 = 3 for odd x ≥3 and arbitrary y ≥2. Requiring x to be odd can be dropped
since it is forced by the equation x2 −6y2 = 3: the number x2 = 6y2 + 3 must be odd, so x
must be odd.
□
For a Pell equation x2 −dy2 = 1, multiplying two known solutions in the form x + y
√
d
leads to a third solution (Theorem 4.1). For a generalized Pell equation x2 −dy2 = n,
multiplying a known solution with a solution of the Pell equation x2 −dy2 = 1 leads to a
new solution of x2 −dy2 = n. The proof is like that of Theorem 4.1. Details are left to the
reader.
Example 6.6. One solution of x2 −6y2 = 3 is (3, 1). A nontrivial solution of x2 −6y2 = 1
is (5, 2). Therefore a second solution of x2 −6y2 = 3 comes from the coeﬃcients of
(3 +
√
6)(5 + 2
√
6) = 27 + 11
√
6.
Check 272 −6 · 112 = 3. In the context of Theorem 6.5 the solution (27, 11) of x2 −6y2 = 3
leads to a solution of (6.1): 2a + 1 = 27 ⇒a = 13 and b + 1 = 11 ⇒b = 10, so 132 + 142 =
102+112+122. This is more attractive if we swap the two sides: 102+112+122 = 132+142.
As an application of math to art, consider the painting in Figure 1 by Bogdanov-Belsky,
which is in the Tetryakov Gallery in Moscow. In it children have to calculate
102 + 112 + 122 + 132 + 142
365
in their heads. If they knew 102 + 112 + 122 = 132 + 142, they could ﬁnd the numerator
as 2(132 + 142), so only two squares would have to be computed instead of ﬁve. Since
2(132 + 142) = 2(169 + 196) = 2(365), dividing by 365 shows the fraction on the board is 2.
The bold artistic details on the blackboard and knowledge of the period when the painting
was produced help us ﬁnd the deeper meaning of this work of art: it is advocating for the
inclusion of generalized Pell equations in the math curriculum of 19th century peasants.

<!-- page 10 -->
10
KEITH CONRAD
Figure 1. Bogdanov-Belsky’s Mental Calculation (1895).
7. The negative Pell equation
We shift from a generalized Pell equation x2 −dy2 = n to the special case of the negative
Pell equation x2 −dy2 = −1. While a product of two solutions of x2 −dy2 = 1 is again
a solution (Theorem 4.1), this doesn’t quite work in the same way for the negative Pell
equation.
Theorem 7.1. If x2−dy2 = n and x′2−dy′2 = n′ then the coeﬃcients of (x+y
√
d)(x′+y′√
d)
are a solution of X2 −dY 2 = nn′.
Proof. By the proof of Theorem 4.1, from (x+y
√
d)(x′+y′√
d) = (xx′+dyy′)+(xy′+yx′)
√
d
we get
(xx′ + dyy′)2 −d(xy′ + yx′)2 = (x2 −dy2)(x′2 −dy′2) = nn′.
□
Therefore if (x, y) is a solution of X2 −dY 2 = −1, the coeﬃcients of (x + y
√
d)k for
k ∈Z+ are solutions of X2 −dY 2 = (−1)k: odd powers give solutions of X2 −dY 2 = −1
and even powers give solutions to X2 −dY 2 = 1.

<!-- page 11 -->
PELL’S EQUATION, I
11
Example 7.2. The equation x2 −2y2 = −1 has solution 1 +
√
2, whose initial powers are
1 +
√
2,
(1 +
√
2)2 = 3 + 2
√
2,
(1 +
√
2)3 = 7 + 5
√
2,
(1 +
√
2)4 = 17 + 12
√
2,
(1 +
√
2)5 = 41 + 29
√
2,
(1 +
√
2)6 = 99 + 70
√
2.
The coeﬃcients of the 1st, 3rd, and 5th powers are solutions of x2 −2y2 = −1, while the
coeﬃcients of the 2nd, 4th, and 6th powers are solutions of x2 −2y2 = 1.
The main point of this is that integral solutions of x2 −dy2 = −1 are not closed under
multiplication, but integral solutions of the equations x2 −dy2 = ±1 together are. We will
prove in Theorem 7.5 below an analogue for these two equations together of Theorem 5.3
for the Pell equation x2 −dy2 = 1.
Suppose the negative Pell equation X2−dY 2 = −1 has a solution (x, y) in Z. Then x ̸= 0
and y ̸= 0,4 so by changing signs on x and y there is a solution in Z+. The Pell equation
X2 −dY 2 = 1 then also has a solution in Z+ by using the coeﬃcients of (x + y
√
d)2.
We will show the positive integer solutions of X2 −dY 2 = −1, when they exist, can be
ordered by either the values of x or y, using the following analogues of Lemmas 5.1 and 5.2.
Lemma 7.3. If x2 −dy2 = −1 in Z and x + y
√
d > 1 then x ≥1 and y ≥1.
The lower bounds on x and y can be achieved: x2 −2y2 = −1 for x = 1 and y = 1.
Proof. We have 1/(x + y
√
d) = −(x −y
√
d) = −x + y
√
d, so
x + y
√
d > 1 > −x + y
√
d > 0.
From x + y
√
d > −x + y
√
d we get 2x > 0, so x > 0. Then x ≥1 since x is an integer, so
y
√
d > x > 0. Thus y > 0, so y ≥1.
□
Lemma 7.4. Suppose x2 −dy2 = −1 and a2 −db2 = −1 in Z where x, y, a, b ≥1. Then
a + b
√
d < x + y
√
d ⇐⇒a < x and b < y ⇐⇒a < x or b < y.
Proof. The ﬁrst (⇐) is obvious. To prove the ﬁrst (⇒), from x+y
√
d > a+b
√
d ≥1+
√
d > 1
reciprocating implies
a + b
√
d < x + y
√
d,
so we get
−x + y
√
d < −a + b
√
d.
Adding these inequalities gives us
(a −x) + (b + y)
√
d < (x −a) + (y + b)
√
d.
Subtracting (b + y)
√
d from both sides, we get a −x < x −a, so 2a < 2x and thus a < x.
Then db2 = 1 + a2 < 1 + x2 = dy2, so b < y from positivity of b and y.
That a < x and b < y is equivalent to a < x or b < y follows by the same reasoning as at
the end of the proof of Lemma 5.2.
□
By Lemma 7.4, the positive integer solutions to x2 −dy2 = −1 (when such solutions
exist) can be ordered by their ﬁrst coordinate or by their second coordinate. So it makes
sense to speak of the solution (x1, y1) in positive integers of x2 −dy2 = −1 (when it exists)
with minimal value of y1 (or x1). That is a basic ingredient in the next result, which is
analogous to Theorem 5.3.
4If d = 1 then the negative Pell equation has the solution (x, y) = (0, 1), but we always assume d is not
a square, so in particular d ̸= 1.

<!-- page 12 -->
12
KEITH CONRAD
Theorem 7.5. Assume x2 −dy2 = −1 has a solution in positive integers and let (x1, y1) be
that solution where y1 is minimal. The integral solutions to both equations x2 −dy2 = ±1
are, up to sign, generated from (x1, y1) by taking integral powers of x1 + y1
√
d:
x + y
√
d = ±(x1 + y1
√
d)k
for some sign and some k ∈Z. The integral solutions of x2 −dy2 = −1 have k odd and the
integral solutions of x2 −dy2 = 1 have k even.
Proof. For k ∈Z, the coeﬃcients of (x1 + y1
√
d)k satisfy x2 −dy2 = (−1)k, and this is also
true for coeﬃcients of −(x1 + y1
√
d)k.
To show all integral solutions of x2 −dy2 = ±1 are related to powers of x1 + y1
√
d, we
will reduce ourselves to what was shown in Theorem 5.3 for solutions of x2 −dy2 = 1 in Z+.
The Pell equation x2 −dy2 = 1 has a solution in positive integers, such as the coeﬃcients
of (x1 + y1
√
d)2. Let (X1, Y1) be the solution of x2 −dy2 = 1 in positive integers with
minimal Y1. We will show X1 + Y1
√
d = (x1 + y1
√
d)2.
By Theorem 5.3 and minimality of (X1, Y1), (x1+y1
√
d)2 = (X1+Y1
√
d)k for some k ≥1.
If k = 2ℓis even then (x1 + y1
√
d)2 = (X1 + Y1
√
d)2ℓ, so x1 + y1
√
d = ±(X1 + Y1
√
d)ℓ.
However, since X2
1 −dY 2
1 = 1, the coeﬃcients of 1 and
√
d in ±(X1+Y1
√
d)ℓﬁt the equation
x2 −dy2 = 1 while x2
1 −dy2
1 = −1. This is a contradiction, so k is odd: k = 2ℓ+ 1 where
ℓ≥0. Then
(x1 + y1
√
d)2 = (X1 + Y1
√
d)2ℓ+1 =⇒X1 + Y1
√
d = (x1 + y1
√
d)2(X1 + Y1
√
d)−2ℓ
= ((x1 + y1
√
d)(X1 −Y1
√
d)ℓ)2.
Set (x1 + y1
√
d)(X1 −Y1
√
d)ℓ= a + b
√
d, so a2 −db2 = −1 and
(7.1)
X1 + Y1
√
d = (a + b
√
d)2.
That implies 2ab = Y1 > 0, so a and b are nonzero with the same sign. By replacing a with
−a and b with −b in case a and b are negative, (7.1) holds for some a, b ∈Z+.
If ℓ> 0 then
(x1 + y1
√
d)2 = (X1 + Y1
√
d)2ℓ+1 > X1 + Y1
√
d = (a + b
√
d)2 > 1,
so x1 + y1
√
d > a + b
√
d by taking positive square roots. This implies y1 > b by Lemma
7.4, which contradicts the minimality of y1 among solutions to x2 −dy2 = −1 in Z+. Thus
ℓ= 0, so
(x1 + y1
√
d)2 = (X1 + Y1
√
d)2ℓ+1 = X1 + Y1
√
d.
Now we are ready to relate the solutions of x2 −dy2 = ±1 in positive integers to integral
powers of x1 + y1
√
d. Afterwards we’ll remove the condition that x > 0 and y > 0.
Case 1: if x2 −dy2 = −1 for x, y ∈Z+ then (x+y
√
d)2 has coeﬃcients that are a solution
of the Pell equation (right side being 1), so by Theorem 5.3
(x + y
√
d)2 = (X1 + Y1
√
d)k = (x1 + y1
√
d)2k
for some k ∈Z+. Taking positive square roots of both sides,
x + y
√
d = (x1 + y1
√
d)k.
Since x2 −dy2 = −1 and x2
1 −dy2
1 = −1, we have −1 = (−1)k by Theorem 7.1, so k is odd:
x + y
√
d is an odd power of x1 + y1
√
d.

<!-- page 13 -->
PELL’S EQUATION, I
13
Case 2: if x2 −dy2 = 1 for x, y ∈Z+ then by Theorem 5.3
x + y
√
d = (X1 + Y1
√
d)k = (x1 + y1
√
d)2k
for some k ∈Z+, so x + y
√
d is an even power of x1 + y1
√
d.
Combining Cases 1 and 2, the solutions to x2 −dy2 = ±1 in positive integers are the
coeﬃcients of (x1 + y1
√
d)K for K ∈Z+.
Now suppose x2 −dy2 = ε where ε = ±1 and the integers x and y are not both positive.
By Lemmas 5.1 and 7.3, α := x + y
√
d is not in (1, ∞). If α ̸= ±1 then α is in the interval
(0, 1), (−1, 0), or (−∞, −1), which makes (exactly) one of the numbers 1/α, −1/α, or −α
lie in (1, ∞). Each of these has coeﬃcients that equal x and y up to sign, and therefore
satisfy X2 −dY 2 = ε:
1
α = ε(x −y
√
d),
−1
α = −ε(x −y
√
d) = ε(−x + y
√
d),
−α = −x −y
√
d.
The number among these that lies in (1, ∞) has positive coeﬃcients (Lemmas 5.1 and 7.3
again), so by our previous reasoning ±α±1 = (x1 + y1
√
d)K for some K ≥1 and some signs
on the left side. Thus α = x + y
√
d = ±(x1 + y1
√
d)±K and ±K ̸= 0. If α = ±1 then
α = ±(x1 + y1
√
d)0.
□
Example 7.6. The solution of x2 −5y2 = −1 in Z+ with least y is (2, 1), so the solutions
in positive integers are the coeﬃcients of (2 +
√
5)k for odd k ≥1. The initial odd powers
after (2 +
p
(5))1 are
(2 +
√
5)3 = 38 + 17
√
5,
(2 +
√
5)5 = 682 + 305
√
5,
(2 +
√
5)7 = 12238 + 5473
√
5.
Example 7.7. For integral a ≥1, the positive solution of x2 −(a2 + 1)y2 = −1 with least
y is (a, 1).5 Therefore the solutions of x2 −(a2 + 1)y2 = ±1 in positive integers are the
coeﬃcients of (a +
√
a2 + 1)k for k ≥1. Here are the ﬁrst few powers:
(a +
p
a2 + 1)1 = a +
p
a2 + 1,
(a +
p
a2 + 1)2 = 2a2 + 1 + 2a
p
a2 + 1,
(a +
p
a2 + 1)3 = (4a3 + 3a) + (4a2 + 1)
p
a2 + 1,
(a +
p
a2 + 1)4 = (8a4 + 8a2 + 1) + (8a3 + 4a)
p
a2 + 1.
The coeﬃcients here are similar to those in powers of a +
√
a2 −1 in Example 5.8, except
the powers of a on the right side don’t have negative coeﬃcients. When a = 1, this is
Example 7.2.
References
[1] R. E. Hodel, An Introduction to Mathematical Logic, PWS Publishing Co., New York, 1995.
[2] J. P. Jones, Y. V. Matiyasevich, “Proof of Recursive Unsolvability of Hilbert’s Tenth Problem,” Amer.
Math. Monthly 98 (1991), 689–709.
5 The number a2 + 1 is not a perfect square, since otherwise a2 and a2 + 1 would be consecutive positive
integers that are perfect squares and that’s impossible.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*