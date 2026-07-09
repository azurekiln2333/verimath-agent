# Congruent Number Problem

> **Source**: https://kconrad.math.uconn.edu/blurbs/congnumber.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE CONGRUENT NUMBER PROBLEM
KEITH CONRAD
1. Introduction
A right triangle is called rational when its legs and hypotenuse are all rational numbers.
Examples of rational right triangles include Pythagorean triples like (3, 4, 5). We can scale
such triples to get other rational right triangles, like (3/2, 2, 5/2). Of course, usually when
two sides are rational the third side is not rational, such as the (1, 1,
√
2) right triangle.
Any rational right triangle has a rational area, but not all (positive) rational numbers
can occur as the area of a rational right triangle. For instance, no rational right triangle has
area 1. This was proved by Fermat. The question we will examine here is: which rational
numbers occur as the area of a rational right triangle?
Deﬁnition 1.1. A positive rational number n is called a congruent number if there is a
rational right triangle with area n: there are rational a, b, c > 0 such that a2 + b2 = c2 and
(1/2)ab = n.
In Figure 1 are rational right triangles with respective areas 5, 6, and 7, so these three
numbers are congruent numbers.
Figure 1. Rational right triangles with respective areas 5, 6, and 7.
This use of the word congruent has nothing to do (directly) with congruences in modular
arithmetic. The etymology will be explained in Section 3. The history of congruent numbers
can be found in [3, Chap. XVI], where it is indicated that an Arab manuscript called the
search for congruent numbers the “principal object of the theory of rational right triangles.”
The congruent number problem asks for a description of all congruent numbers. Since
scaling a triangle changes its area by a square factor, and every rational number can be
multiplied by a suitable rational square to become a squarefree integer (e.g., 18/7 = 32·2/7,
1

<!-- page 2 -->
2
KEITH CONRAD
so multiplying by (7/3)2 produces the squarefree integer 14), we can focus our attention in
the congruent number problem on squarefree positive integers. For instance, to say 1 is not
a congruent number means no rational square is a congruent number.
When n is squarefree in Z+, to show n is a congruent number we just need to ﬁnd an
integral right triangle whose area has squarefree part n. Then writing the area as m2n
shows scaling the sides by m produces a rational right triangle with area n.
In Section 2, the parametrization of Pythagorean triples will be used to construct a lousy
algorithm generating all congruent numbers.
The equivalence of the congruent number
problem with a problem about rational squares in arithmetic progressions is in Section
3. Section 4 gives an equivalence between the congruent number problem and the search
for rational points on y2 = x3 −n2x where y ̸= 0, which ultimately leads to a solution
of the congruent number problem (depending in part on the Birch and Swinnerton-Dyer
conjecture, a famous open problem in mathematics). In the appendices we explain some
algebraically mysterious formulas from our treatment using projective geometry and give a
relation between the congruent number problem and other Diophantine equations.
Acknowledgments. I thank Lucas David-Roesler for generating the pictures.
2. A bad algorithm
There is a parametric formula for primitive Pythagorean triples, and we will use it to
make a small list of squarefree congruent numbers. A primitive triple (with even second
leg) is (k2 −ℓ2, 2kℓ, k2 + ℓ2) where k > ℓ> 0, (k, ℓ) = 1, and k ̸≡ℓmod 2. In Table 1 we
list such primitive triples where k + ℓ≤9. The squarefree part of the area is listed in the
last column. Each number in the fourth column is a congruent number and each number
in the ﬁfth column is also a congruent number. The ﬁnal row of the table explains how a
rational right triangle with area 5 can be found.
k
ℓ
(a, b, c)
(1/2)ab
Squarefree part
2
1
(3, 4, 5)
6
6
4
1
(15, 8, 17)
60
15
3
2
(5, 12, 13)
30
30
6
1
(35, 12, 37)
210
210
5
2
(21, 20, 29)
210
210
4
3
(7, 24, 25)
84
21
8
1
(63, 16, 65)
504
126
7
2
(45, 28, 53)
630
70
5
4
(9, 40, 41)
180
5
Table 1. Congruent Numbers.
Notice 210 shows up twice in Table 1. Do other numbers which occur once also occur
again? We will return to this question later.
Table 1 can be extended as k + ℓincreases, and each squarefree congruent number even-
tually occurs in the last column: if the squarefree number m is the area of a rational right
triangle with sides a/d, b/d, and c/d, using minimal common denominator d, then (a, b, c) is
a primitive Pythagorean triple with area md2, whose squarefree part is m. Alas, the table is
not systematic in the appearance of the last column: we can’t tell by building the table when

<!-- page 3 -->
THE CONGRUENT NUMBER PROBLEM
3
any particular number should occur, if at all, in the last column, so this method of generat-
ing (squarefree) congruent numbers is not a good algorithm. For instance, 53 is a congruent
number, but it shows up for the ﬁrst time when k = 1873180325 and ℓ= 1158313156. (The
corresponding right triangle has area 53 · 2978556542849787902.)
Tables of congruent numbers are in 10th century Arabic manuscripts, where 5 and 6
appear [3, p. 459]. Fibonacci found in the 13th century that 7 is congruent and he stated
that 1 is not congruent (no rational right triangle has area equal to a perfect square). The
ﬁrst proof of that is by Fermat and a proof likely due to him shows 2 is not congruent [12,
pp. 75–77]. That 3 is not congruent is due to Genocchi [4, pp. 101-103], who showed primes
p ≡3 mod 8 are not congruent. Hemenway [5, §1.3] translated the argument into English.
Theorem 2.1 (Fermat, 1640). The number 1 is not congruent.
Proof. We will use the method of descent, which was discovered by Fermat on this very
problem. Our argument is adapted from [2, pp. 658–659].
Assume a rational right triangle has area 1. Call the sides a/d, b/d, and c/d, where a, b, c,
and d are positive integers, so a2 + b2 = c2 and (1/2)ab = d2. (In other words, if some
rational right triangle has area 1 then some Pythagorean triangle has area equal to a perfect
square. The converse is true too.) Clearing the denominator in the second equation,
(2.1)
a2 + b2 = c2,
ab = 2d2.
We will show (2.1) has no positive integer solutions.
Assume there is a solution to (2.1) in positive integers. Let’s show there is then a solution
where a and b are relatively prime. Set g = (a, b), so g | a and g | b. Then g2 | c2 and
g2 | 2d2, so g | c and g | d (why?). Divide a, b, c, and d by g to get another 4-tuple of
positive integers satisfying (2.1) with (a, b) = 1. So we may now focus on showing (2.1) has
no solution in positive integers with the extra condition that (a, b) = 1.
We will do this using Fermat’s method of descent: construct a new 4-tuple of positive
integers a′, b′, c′, d′ satisfying (2.1) with (a′, b′) = 1 and 0 < c′ < c. Repeating this enough
times, we reach a contradiction. Several times in the descent process we will use the following
(or minor variations on it): two positive relatively prime integers whose product is a perfect
square must each be perfect squares.
Now we start the descent. Since ab = 2d2 and a and b are relatively prime, a or b is even
but not both. Then c2 = a2 + b2 is odd, so c is odd. Since ab is twice a square, (a, b) = 1,
and a and b are positive, one is a square and the other is twice a square. The roles of a and
b are symmetric, so without loss of generality a is even and b is odd. Then
a = 2k2,
b = ℓ2
for some positive integers k and ℓ, with ℓodd (because b is odd). The ﬁrst equation in (2.1)
now looks like 4k4 + b2 = c2, so c+b
2
c−b
2
= k4. Because b and c are both odd and relatively
prime, (c + b)/2 and (c −b)/2 are relatively prime. Therefore
c + b
2
= r4,
c −b
2
= s4
for some relatively prime positive integers r and s. Solve for b and c by adding and sub-
tracting these equations:
b = r4 −s4,
c = r4 + s4,
so ℓ2 = b = (r2 + s2)(r2 −s2). The factors r2 + s2 and r2 −s2 are relatively prime: any
common factor would be odd (since ℓis odd) and divides the sum 2r2 and the diﬀerence

<!-- page 4 -->
4
KEITH CONRAD
2s2, so is a factor of (r2, s2) = 1. Since the product of r2 + s2 and r2 −s2 is an odd square
and one of these is positive, the other is positive and
(2.2)
r2 + s2 = t2,
r2 −s2 = u2
for odd positive integers t and u which are relatively prime. Since u2 ≡1 mod 4, r2 −s2 ≡
1 mod 4, which forces r to be odd and s to be even.1 Solving for r2 in (2.2),
(2.3)
r2 = t2 + u2
2
=
t + u
2
2
+
t −u
2
2
,
where (t ± u)/2 ∈Z since t and u are odd.
Equation (2.3) will give us a “smaller” version of (2.1). Setting
a′ = t + u
2
,
b′ = t −u
2
,
c′ = r,
we have a′2 + b′2 = c′2. From (t, u) = 1 we get (a′, b′) = 1. Moreover, using (2.2), a′b′ =
(t2 −u2)/4 = 2s2/4 = 2(s/2)2. Let d′ = s/2 ∈Z, so we have a new solution (a′, b′, c′, d′) to
(2.1). Since 0 < c′ = r ≤r4 < r4 + s4 = c, by descent we get a contradiction.
□
Theorem 2.1 leads to a weird proof that
√
2 is irrational. If
√
2 were rational then
√
2,
√
2, and 2 would be the sides of a rational right triangle with area 1. This is a contradiction
of 1 not being a congruent number!
3. Relation to Arithmetic Progressions of Three Squares
The squares 1, 25, 49 form an arithmetic progression with common diﬀerence 24, whose
squarefree part is 6. This is related to 6 being a congruent number, by the next theorem.
Theorem 3.1. Let n > 0. There is a one-to-one correspondence between right triangles
with area n and 3-term arithmetic progressions of squares with common diﬀerence n: the
sets
{(a, b, c) : a2 + b2 = c2, (1/2)ab = n},
{(r, s, t) : s2 −r2 = n, t2 −s2 = n}
are in one-to-one correspondence by
(a, b, c) 7→((b −a)/2, c/2, (b + a)/2),
(r, s, t) 7→(t −r, t + r, 2s).
Proof. It is left to the reader to check the indicated functions take values in the indicated
sets, and that the correspondences are inverses of one another: if you start with an (a, b, c)
and make an (r, s, t) from it, and then form an (a′, b′, c′) from this (r, s, t), you get back the
original (a, b, c). Similarly, starting with an (r, s, t), producing an (a, b, c) from it and then
producing an (r′, s′, t′) from that returns the same (r, s, t) you started with.
□
How could the correspondence in Theorem 3.1 be discovered? When s2 −r2 = n and
t2 −s2 = n, adding gives t2 −r2 = 2n, so (t −r)(t + r) = 2n. This suggests using a = t −r
and b = t + r. Then a2 + b2 = 2(t2 + r2) = 2(2s2) = (2s)2, so use c = 2s.
For rational n > 0, the correspondence in Theorem 3.1 preserves rationality and positiv-
ity/monotonicity: (a, b, c) is a rational triple if and only if (r, s, t) is a rational triple, and
0 < a < b < c if and only if 0 < r < s < t. So n is congruent if and only if there is a rational
square s2 such that s2 −n and s2 + n are squares. Note the correspondence in Theorem 3.1
involves not the squares in arithmetic progression but their square roots r, s, and t.
1Odd squares are 1 mod 4 and even squares are 0 mod 4, so the only way r2 −s2 can be 1 mod 4 is for r to
be odd and s to even,

<!-- page 5 -->
THE CONGRUENT NUMBER PROBLEM
5
Example 3.2. For n = 6, using (a, b, c) = (3, 4, 5) in Theorem 3.1 produces (r, s, t) =
(1/2, 5/2, 7/2), whose termwise squares are the arithmetic progression 1/4, 25/4, 49/4 with
common diﬀerence 6.
Example 3.3. Taking n = 5 and (a, b, c) = (3/2, 20/3, 41/6), the correspondence in The-
orem 3.1 yields (r, s, t) = (31/12, 41/12, 49/12): the rational squares (31/12)2, (41/12)2,
(49/12)2 are an arithmetic progression with common diﬀerence 5.
Example 3.4. Since Fermat showed 1 and 2 are not congruent numbers, there is no arith-
metic progression of 3 rational squares with common diﬀerence 1 or 2 (or, more generally,
common diﬀerence a nonzero square or twice a nonzero square).
We now can explain the origin of the peculiar name “congruent number.” Fibonacci, in
his book Liber Quadratorum (Book of Squares) from 1225, called an integer n a congruum
if there is an integer x such that x2 ± n are both squares. This means x2 −n, x2, x2 + n
is a 3-term arithmetic progression of squares. Fibonacci’s motivation for writing his book
was the study of 3-term arithmetic progressions of integral (rather than rational) squares.
Both words congruum and congruence come from the Latin congruere, which means “to
meet together” (to congregate!). A congruum is a number related to three integer squares
in a kind of agreement (having a common diﬀerence). Considering a congruum multiplied
by rational squares (e.g., 24 · (1/2)2 = 6) gives the congruent numbers.
4. The Curve y2 = x3 −n2x
Whether or not n is congruent is related to solvability of pairs of equations: ﬁrst, by
deﬁnition we need to solve a2 + b2 = c2 and (1/2)ab = n in positive rational numbers a,
b, and c. In Section 3 we saw this is equivalent to solving a second pair of equations in
positive rational numbers: s2 −r2 = n and t2 −s2 = n. It turns out that the congruent
number property is also equivalent to (nontrivial) rational solvability of the single equation
y2 = x3 −n2x.
This equation has three obvious rational solutions: (0, 0), (n, 0), and (−n, 0). These are
the solutions with y = 0.
Theorem 4.1. For n > 0, there is a one-to-one correspondence between the following two
sets:
{(a, b, c) : a2 + b2 = c2, (1/2)ab = n},
{(x, y) : y2 = x3 −n2x, y ̸= 0}.
Mutually inverse correspondences between these sets are
(a, b, c) 7→
 nb
c −a, 2n2
c −a

,
(x, y) 7→
x2 −n2
y
, 2nx
y , x2 + n2
y

.
Proof. This is a direct calculation left to the reader. We divide by c−a in the ﬁrst formula,
and c ̸= a automatically since if c = a then b = 0, but (1/2)ab = n is nonzero. Restricting
y to a nonzero value is necessary since we divide by y in the second formula.
□
Remark 4.2. It is of course natural to wonder how the correspondence in Theorem 4.1
could be discovered in the ﬁrst place. See the appendix.
The correspondence in Theorem 4.1 preserves positivity: if a, b, and c are positive then
(c−a)(c+a) = b2 > 0, so c−a is positive and thus x = nb/(c−a) > 0 and y = 2n2/(c−a) > 0.
In the other direction, if x and y are positive then from y2 = x3 −n2x = x(x2 −n2) we see
x2 −n2 has to be positive, so a, b, and c are all positive. Also, for rational n > 0, (a, b, c)

<!-- page 6 -->
6
KEITH CONRAD
is rational if and only if (x, y) is rational. Any solution to a2 + b2 = c2 and (1/2)ab = n
needs a and b to have the same sign (since ab = 2n > 0), and by a sign adjustment there
is a rational solution with a, b, and c all positive if there is any rational solution at all.
Therefore a rational number n > 0 is congruent if and only if the equation y2 = x3 −n2x
has a rational solution (x, y) with y ̸= 0; we don’t have to pay attention to whether or not
x and y are positive.
A positive rational number n is not congruent if and only if the only rational solutions to
y2 = x3 −n2x have y = 0: (0, 0), (n, 0), and (−n, 0). For example, since 1 is not congruent
(Theorem 2.1), the only rational solutions to y2 = x3 −x have y = 0.
Example 4.3. Since 6 is the area of a (3, 4, 5) right triangle, the equation y2 = x3 −36x
has a rational solution with y ̸= 0. The solution corresponding to the (3, 4, 5) right triangle
by Theorem 4.1 is (x, y) = (12, 36). See Figure 2.
(12, 36)
r
Figure 2. The rational point (12, 36) on y2 = x3 −36x.
Example 4.4. From the rational right triangle (3/2, 20/3, 41/6) with area 5, Theorem 4.1
gives us a rational solution to y2 = x3 −25x: (x, y) = (25/4, 75/8). If we allow sign changes
on the coordinates of (3/2, 20/3, 41/6), Theorem 4.1 will give us new rational solutions to
y2 = x3 −25x. Using the triples of the form (±3/2, ±20/3, ±41/6) where the ﬁrst two
coordinates have the same sign, the new solutions we get to y2 = x3 −25x are collected in
Table 2 and they are plotted on y2 = x3 −25x in Figure 3.
Example 4.5. A rational solution to y2 = x3 −49x is (25, 120). Theorem 4.1 produces
from this solution the rational right triangle (24/5, 35/12, 337/60) with area 7, which we
met already in Figure 1.
Example 4.6. In Table 1 we found two rational right triangles with area 210: (35, 12, 37)
and (21, 20, 29). Using Theorem 4.1, these triangles lead to two rational solutions to y2 =
x3 −2102x: (1260, 44100) and (525, 11025), respectively.
In Figure 4, the line through
(1260, 44100) and (525, 11025) meets the curve y2 = x3−2102x in a third point (240, −1800).

<!-- page 7 -->
THE CONGRUENT NUMBER PROBLEM
7
Signs on (3/2, 20/3, 41/6)
(x, y)
(+, +, +)
(25/4, 75/8)
(+, +, −)
(−4, −6)
(−, −, +)
(−4, 6)
(−, −, −)
(25/4, −75/8)
Table 2. Solutions to y2 = x3 −25x.
(−4, 6)
(−4, −6)
(25
4 , 75
8 )
(25
4 , −75
8 )
Figure 3. Some rational points on y2 = x3 −25x.
Its second coordinate is negative, but the point (240, 1800) is also on that curve, and it leads
by Theorem 4.1 to the new rational right triangle (15/2, 56, 113/2) with area 210.
Example 4.7. Suppose (a, b, c) satisﬁes a2 + b2 = c2 and (1/2)ab = n. Such a solution
gives rise to seven additional ones: (−a, −b, −c) and
(a, b, −c),
(−a, −b, c),
(b, a, c),
(b, a, −c),
(−b, −a, c),
(−b, −a, −c).
These algebraic modiﬁcations have a geometric interpretation in terms of constructing new
points from old ones on the curve y2 = x3 −n2x using secant lines. Say (a, b, c) corresponds
to (x, y) by Theorem 4.1, so y ̸= 0. From the point (x, y) on the curve we get automatically
a second point: (x, −y). This corresponds by Theorem 4.1 to (−a, −b, −c). What points
on the curve correspond to the six remaining algebraic modiﬁcations above?
Well, there are three obvious points on the curve which have nothing to do with our
particular (x, y), namely (0, 0), (n, 0), and (−n, 0). The line through (x, y) and (0, 0) meets
the curve in the point (−n2/x, −n2y/x2), which corresponds by Theorem 4.1 to (a, b, −c).
More generally, the three lines through (x, y) and each of (0, 0), (n, 0), and (−n, 0) meet
the curve in three additional points, and their reﬂections across the x-axis are an additional
three points (which are where the lines through (x, −y) and each of (0, 0), (n, 0), and (−n, 0)
meet the curve). See Table 3 and Figure 5. The corresponding triples from Theorem 4.1
are collected in Table 4 and are exactly what we were looking for.

<!-- page 8 -->
8
KEITH CONRAD
(240, −1800)
(525,11025)
(1260,44100) r
r
rr
Figure 4. New rational point on y2 = x3 −2102x from a secant line. (Not
drawn to scale.)
P0
P4
(0,0)
(−n, 0)
(n, 0)
P5
P1
P3
P7
P2
P6
r
r
r
r
r
r
r
r
r
r
r
r
r
r
Figure 5. Intersecting y2 = x3 −n2x with lines through P0 and (0, 0),
(n, 0), (−n, 0), and reﬂected points.
We have seen that the following properties of a positive rational number n are equivalent:
• there is a rational right triangle with area n,
• there is a 3-term arithmetic progression of rational squares with common diﬀerence
n,
• there is a rational solution to y2 = x3 −n2x with y ̸= 0.

<!-- page 9 -->
THE CONGRUENT NUMBER PROBLEM
9
First Point
Second Point
Third Point
(x, y)
(0, 0)
(−n2/x, −n2y/x2)
(x, −y)
(0, 0)
(−n2/x, n2y/x2)
(x, y)
(n, 0)
(n(x + n)/(x −n), 2n2y/(x −n)2)
(x, −y)
(n, 0)
(n(x + n)/(x −n), −2n2y/(x −n)2)
(x, y)
(−n, 0)
(−n(x −n)/(x + n), 2n2y/(x + n)2)
(x, −y)
(−n, 0)
(−n(x −n)/(x + n), −2n2y/(x + n)2)
Table 3. Third Intersection Point of a Line with y2 = x3 −n2x.
Pair
Triple
(x, y)
(a, b, c)
(x, −y)
(−a, −b, −c)
(−n2/x, −n2y/x2)
(a, b, −c)
(−n2/x, n2y/x2)
(−a, −b, c)
(n(x + n)/(x −n), 2n2y/(x −n)2)
(b, a, c)
(n(x + n)/(x −n), −2n2y/(x −n)2)
(−b, −a, −c)
(−n(x −n)/(x + n), 2n2y/(x + n)2)
(−b, −a, c)
(−n(x −n)/(x + n), −2n2y/(x + n)2)
(b, a, −c)
Table 4. Theorem 4.1 and Sign Changes.
The viewpoint of the equation y2 = x3 −n2x lets us use the geometry of the curve to
do something striking: produce a new rational right triangle with area n from two known
triangles. We saw an instance of this in Example 4.6. Notice there is nothing in the deﬁnition
of a congruent number which suggests it is possible to produce a new rational right triangle
with area n from two known ones. We can even ﬁnd a new rational right triangle with area
n from just one such triangle, by using a tangent line in place of a secant line. Given a
rational point (x0, y0) on y2 = x3 −n2x with y0 ̸= 0, draw the tangent line to this curve
at the point (x0, y0). This line will meet the curve in a second rational point, and that
can be converted into a new rational right triangle with area n using the correspondence of
Theorem 4.1 (and removing any signs on a, b, c if they turn out negative.)
Example 4.8. In Example 4.6, we found a third rational right triangle from two known
ones by intersecting the line through the points (1260, 44100) and (525, 11025) with y2 =
x3 −2102x. We can ﬁnd a new rational right triangle with area 210 from the single point
(1260, 44100) by using the tangent line to y2 = x3 −2102x at (1260, 44100). The tangent is
y = 107
2 x −23310
and it meets the curve in the second point (1369/4, −39997/8). See Figure 6. By Theorem
4.1, this point corresponds to (a, b, c) = (−1081/74, −31080/1081, −2579761/79994), which
after removing signs is the rational right triangle (1081/74, 31080/1081, 2579761/79994),
whose area is 210.
Example 4.9. The (3, 4, 5) right triangle with area 6 corresponds to the point (12, 36)
on the curve y2 = x3 −36x, as we saw already in Example 4.3. The tangent line to this
curve at the point (12, 36) is y = (11/2)x −30, which meets the curve in the second point

<!-- page 10 -->
10
KEITH CONRAD
  1369
4 , −39997
8

(1260,44100) r
r
Figure 6. New rational point on y2 = x3 −2102x from a tangent line. (Not
drawn to scale.)
(25/4, 35/8) = (6.25, 4.375).
Let’s repeat the tangent process on this new point.
The
tangent line to the curve at (25/4, 35/8) has equation
y = 1299
140 x −6005
112 ,
which meets the curve in the new point
(4.1)
1442401
19600 , 1726556399
2744000

≈(73.59, 629.21).
This is illustrated in Figure 7, where the second tangent line meets the curve outside the
range of the picture.2
A larger view, showing where the second tangent line meets the
curve, is in Figure 8. (The axes in Figures 7 and 8 are not given equal scales, which is
why the same tangent line in the two ﬁgures appears to have diﬀerent slopes.)
Using
Theorem 4.1, (25/4, 35/8) corresponds to the rational right triangle with area 6 having
sides (7/10, 120/7, 1201/70). The rational right triangle with area 6 corresponding to the
point in (4.1) has sides
(4.2)
1437599
168140 , 2017680
1437599, 2094350404801
241717895860

.
Armed with 3 rational right triangles with area 6, we can ﬁnd 3 arithmetic progressions
of rational squares using Theorem 3.1. The (3, 4, 5) triangle, as we saw in Example 3.2,
yields the arithmetic progression 1/4, 25/4, 49/4. The (7/10, 120/7, 1201/70) right triangle
yields the arithmetic progression
1151
140
2
,
1201
140
2
,
1249
140
2
.
2The inﬂection points on the curve in Figure 7, for x > 0, occur where x =
q
12(3 + 2
√
3) ≈8.8.

<!-- page 11 -->
THE CONGRUENT NUMBER PROBLEM
11
  25
4 , 35
8

(12,36)
r
r
Figure 7. Close view of successive tangents to y2 = x3 −36x starting from (12, 36).
r
r
r
Figure 8. Far view of successive tangents to y2 = x3 −36x starting from
(12, 36). (Not drawn to scale.)
The right triangle with sides in (4.2) yields the arithmetic progression
1727438169601
483435791720
2
,
2094350404801
483435791720
2
,
 77611083871
483435791720
2
.
All of these arithmetic progressions of squares have common diﬀerence 6.

<!-- page 12 -->
12
KEITH CONRAD
Remark 4.10. The secant method is a way to “add” points and the tangent method is
essentially the special case of “doubling” a point.3 These tangent and secant constructions
can be used to give the rational points on y2 = x3 −n2x the structure of an abelian group
in which, for rational n > 0, any rational point (x, y) with y ̸= 0 has inﬁnite order. (This is
not at all obvious.) Therefore the curve y2 = x3 −n2x has inﬁnitely many rational points as
soon as it has just one rational point with y ̸= 0, so there are inﬁnitely many rational right
triangles with area n provided there is one example and there are inﬁnitely many 3-term
arithmetic progressions of rational squares with common diﬀerence n provided there is one
example. In terms of Table 1, this means any area arising in the table at least once will
arise in the table inﬁnitely often.4
The importance of thinking about congruent numbers in terms of the curves y2 = x3−n2x
goes far beyond this interesting construction of new rational right triangles with area n from
old ones: this viewpoint in fact leads to a tentative solution of the whole congruent number
problem! In 1983, Tunnell [10] used arithmetic properties of y2 = x3 −n2x (a particular
example of an elliptic curve) to discover a previously unknown elementary necessary condi-
tion on congruent numbers and he was able to prove the condition is suﬃcient if a certain
other conjecture is true.
Theorem 4.11 (Tunnell). Let n be a squarefree positive integer. Set
f(n)
=
#{(x, y, z) ∈Z3 : x2 + 2y2 + 8z2 = n},
g(n)
=
#{(x, y, z) ∈Z3 : x2 + 2y2 + 32z2 = n},
h(n)
=
#{(x, y, z) ∈Z3 : x2 + 4y2 + 8z2 = n/2},
k(n)
=
#{(x, y, z) ∈Z3 : x2 + 4y2 + 32z2 = n/2}.
For odd n, if n is congruent then f(n) = 2g(n). For even n, if n is congruent then h(n) =
2k(n). Moreover, if the weak Birch and Swinnerton–Dyer conjecture is true for the curve
y2 = x3 −n2x then the converse of both implications is true: f(n) = 2g(n) implies n is
congruent when n is odd and h(n) = 2k(n) implies n is congruent when n is even.
The weak Birch and Swinnerton–Dyer conjecture, which we won’t describe here, is one
of the most important conjectures in mathematics. (It is on the list of Clay Millenium
Prize problems.) Several years before Tunnell proved his theorem, Stephens [9] showed the
weak Birch and Swinnerton–Dyer conjecture implies any positive integer n ≡5, 6, 7 mod 8
is a congruent number. Tunnell’s achievement was discovering the enumerative criterion
for congruent numbers and its relation to the weak Birch and Swinnerton–Dyer conjecture.
For background on the ideas in Tunnell’s theorem, see [6] and [7]. In [8, pp. 112–114] the
particular case of prime congruent numbers is considered.
Tunnell’s theorem provides an unconditional method of proving a squarefree positive
integer n is not congruent (show f(n) ̸= 2g(n) or h(n) ̸= 2k(n), depending on the parity of
n), and a conditional method of proving n is congruent (conditional, that is, on the weak
Birch and Swinnerton-Dyer conjecture for the curve y2 = x3 −n2x).
3The process of getting new rational points from known ones in the congruent number problem goes back
to Turri`ere [11] in 1915, who worked with the points (r, s, t) lying on the two surfaces s2 + n = t2 and
s2 −n = r2, which intersect in a curve that is essentially y2 = x3 −n2x.
4The two rational points on y2 = x3 −2102x which correspond to the repetition of 210 in Table 1 are
independent in the group law: they do not have a common multiple.

<!-- page 13 -->
THE CONGRUENT NUMBER PROBLEM
13
Example 4.12. Since f(1) = g(1) = 2 and f(3) = g(3) = 4, we have f(n) ̸= 2g(n) for
n = 1 and 3, so Tunnell’s criterion shows 1 and 3 are not congruent.
Example 4.13. Since h(2) = k(2) = 2, we have h(2) ̸= 2k(2), so Tunnell’s criterion shows
2 is not congruent.
Example 4.14. Since f(5) = g(5) = 0 and f(7) = g(7) = 0, we have f(n) = 2g(n) for n = 5
and 7. Tunnell’s theorem says 5 and 7 are congruent if the weak Birch and Swinnerton-Dyer
conjecture is true for y2 = x3 −25x and y2 = x3 −49x. Unconditionally, we saw earlier
that 5 and 7 are congruent.
Example 4.15. Since h(10) = 4 and k(10) = 4, h(10) ̸= 2k(10), so Tunnell’s theorem says
10 is not a congruent number.
Example 4.16. We will show (conditionally) that any squarefree positive integer n sat-
isfying n ≡5, 6, 7 mod 8 is a congruent number.
Tunnell’s theorem tells us to check
that f(n) = 2g(n) when n ≡5, 7 mod 8 and h(n) = 2k(n) when n ≡6 mod 8.
Since
x2 +2y2 ̸≡5, 7 mod 8 for any integers x and y, f(n) = 0 and g(n) = 0 when n ≡5, 7 mod 8,
so f(n) = 2g(n). When n ≡6 mod 8 we have n/2 ≡3 mod 4, so x2 ̸≡n/2 mod 4 for any in-
teger x. Therefore h(n) = 0 and k(n) = 0 when n ≡6 mod 8, so h(n) = 2k(n). This shows
n is congruent if the weak Birch and Swinnerton-Dyer conjecture is true for y2 = x3 −n2x.
Appendix A. Discovering Theorem 4.1
Fix a real number n ̸= 0. The real solutions (a, b, c) to each of the equations
(A.1)
a2 + b2 = c2,
1
2ab = n,
describe a surface in R3, so it is reasonable to expect these two surfaces intersect in a curve.
We want an equation for that curve, which will be y2 = x3 −n2x in the right choice of
coordinates. Two approaches will be described, one algebraic and the other geometric. The
sign on n will be irrelevant, so we allow any n ̸= 0 rather than n > 0.
The algebra is simpliﬁed by introducing a cross-term in the equation a2 + b2 = c2. Let
c = t + a, which turns this equation into b2 = t2 + 2at, or equivalently
(A.2)
2at = b2 −t2.
Since ab = 2n is nonzero, neither a nor b is 0, so we can write a = 2n/b and substitute it
into (A.2):
4nt
b
= b2 −t2.
Multiplying through by b makes this
4nt = b3 −t2b.
Divide by t3 (t ̸= 0, as otherwise a = c and then b = 0, but ab = 2n ̸= 0):
4n
t2 =
b
t
3
−b
t.
Multiply through by n3:
2n2
t
2
=
nb
t
3
−n2
nb
t

.

<!-- page 14 -->
14
KEITH CONRAD
Set x = nb/t and y = 2n2/t, so y2 = x3 −n2x. Then x = nb/(c −a) and y = 2n2/(c −a),
as in Theorem 4.1.
We now turn to a geometric explanation of Theorem 4.1, taking greater advantage of the
interpretation of the two equations in (A.1) as surfaces which meet in a curve. Rather than
working with the equations as surfaces in R3, we will work in the projective space P3(R)
by homogenizing the two equations. This doesn’t change the ﬁrst equation in (A.1), but
makes the second one (1/2)ab = nd2.
Letting [a, b, c, d] be the homogeneous coordinates of a typical point in P3(R), the two
equations
(A.3)
a2 + b2 = c2,
1
2ab = nd2
each deﬁne surfaces in P3(R). Let C be the intersection of these surfaces (a curve). There
are points on C with b = 0, namely [a, b, c, d] = [1, 0, ±1, 0]. These points are not in the usual
aﬃne space inside P3(R), and we will use one of these points in a geometric construction.
Let’s project through the point P := [1, 0, 1, 0] to map C to the plane
Π := {[0, b, c, d]}
and ﬁnd the equation for the image of C in this plane. The point P lies on C and not in Π.
For each Q ∈C other than P, the line PQ in P3(R) meets Π in a unique point. Call this
point f(Q). When Q = P, intersect the tangent line to C at P with the plane Π to deﬁne
f(P). We have deﬁned a function f : C →Π.
Computing a formula for f necessitates a certain about of computation to see what
happens. Suppose ﬁrst that Q = [a, b, c, d] is not P. The line through P and Q is the set of
points
[λ + µa, µb, λ + µc, µd],
which meets Π where λ = −µa, making
f(Q) = [0, µb, µ(c −a), µd] = [0, b, c −a, d].
As for f(P), the tangent planes to each of the surfaces a2 + b2 = c2 and (1/2)ab = nd2 in
P3(R) at the point P are the planes a = c and b = 0, so the tangent line at P is the set of
points
[a, 0, a, d],
which meets Π in [0, 0, 0, 1], so f(P) = [0, 0, 0, 1]. Thus
f([a, b, c, d]) =
(
[0, b, c −a, d],
if [a, b, c, d] ̸= [1, 0, 1, 0],
[0, 0, 0, 1],
if [a, b, c, d] = [1, 0, 1, 0].
As an exercise, check f is injective. (Hint: Since (1/2)ab = nd2, b and d determine a if
b ̸= 0.)
All points in the plane Π have ﬁrst coordinate 0. Identify Π with P2(R) by dropping
this coordinate, which turns f into the function g: C →P2(R) where
(A.4)
g([a, b, c, d]) =
(
[b, a −c, d],
if [a, b, c, d] ̸= [1, 0, 1, 0],
[0, 0, 1],
if [a, b, c, d] = [1, 0, 1, 0].
We have mapped our curve C to the projective plane P2(R). What is an equation for
the image g(C)? For Q = [a, b, c, d] on C, write g(Q) = [x, z, y]. (This ordering of the
coordinates will make formulas come out in close to the expected way more quickly.) When

<!-- page 15 -->
THE CONGRUENT NUMBER PROBLEM
15
Q ̸= [1, 0, 1, 0] (that is, a ̸= c), (A.4) says we can use x = b, y = d, and z = c −a ̸= 0.5 The
equations in (A.3) become a2 + x2 = (a + z)2 and (1/2)ax = ny2, so
x2 = 2az + z2,
ax = 2ny2.
Since z ̸= 0, we can solve for a in the ﬁrst equation, so a is determined by x, y, and z.
Multiplying the ﬁrst equation by x and the second by 2z, x3 = 2axz + xz2 = 4ny2z + xz2.
Thus
4ny2z = x3 −xz2.
Set X = x, Y = 2ny, and Z = z/n to ﬁnd Y 2Z = X3 −n2XZ2, which is the homogeneous
form of Y 2 = X3 −n2X.
Tracing this correspondence out explicitly from the start, if we begin with [a, b, c, d] on
C where d ̸= 0 (the standard aﬃne part of C), its image [X, Z, Y ] in P2(R) is

b, c −a
n
, 2nd

= [nb, c −a, 2n2d] =
 nb
c −a, 1, 2n2d
c −a

.
Since d ̸= 0 implies a ̸= c, using inhomogeneous coordinates with middle coordinate 1 in
P2(R) the point (a, b, c) goes to (nb/(c −a), 2n2/(c −a)), which is the transformation in
Theorem 4.1.
As an exercise in these techniques, consider the problem of classifying triangles with a
given area n > 0 and a given angle θ. (Taking θ = π/2 is the congruent number problem.)
Let a, b, c be the side lengths of the triangle, with c the length of the edge opposite the
angle θ. The equations in (A.1) are replaced by
(A.5)
a2 + b2 −2ab cos θ = c2,
1
2ab sin θ = n.
(If there is a solution with rational a, b, c, and n then cos θ and sin θ must be rational.)
Show the solutions (a, b, c) of (A.5) are in one-to-one correspondence with the solutions
(x, y) of the equation
y2
=
x3 + 2n cos θ
sin θ
x2 −n2x
=
x

x + ncos θ + 1
sin θ
 
x + ncos θ −1
sin θ

,
with y ̸= 0. The correspondence should specialize to that in Theorem 4.1 when θ = π/2.
Appendix B. Other Diophantine Equations
In Table 5, the ﬁrst two columns show how to convert the sides (a, b, c) of a rational
right triangle with area 1 into a positive rational solution of the equation y2 = x4 −1 and
conversely. (These correspondences are not inverses, but they do show a positive rational
solution in the ﬁrst column leads to a positive rational solution in the second column, and
conversely.) The last two columns give a (bijective) correspondence between rational right
triangles with area 2 and positive rational solutions of y2 = x4 + 1. So showing 1 and 2
are not congruent numbers is the same as showing the equations y2 = x4 ± 1 don’t have
solutions in positive rational numbers.
A positive rational solution (x, y) to y2 = x4 ± 1 can be turned into a positive integral
solution (u, v, w) of w2 = u4 ± v4 by clearing a common denominator, and we can go in
5The cross term t = c −a in the algebraic method is precisely z, so now we get a geometric interpretation
of this cross term as a coordinate in a projection map to a plane.

<!-- page 16 -->
16
KEITH CONRAD
a2 + b2 = c2,
y2 = x4 −1
a2 + b2 = c2,
y2 = x4 + 1
1
2ab = 1
1
2ab = 2
x = c/2
a = y/x
x = a/2
a = 2x
y = |a2 −b2|/4
b = 2x/y
y = ac/4
b = 2/x
c = (x4 + 1)/xy
c = 2y/x
Table 5. Correspondences between rational right triangles with area 1 and
y2 = x4 ± 1.
reverse by dividing by v4. That 1 and 2 are not congruent is therefore the same as the
equations w2 = u4 ± v4 having no positive integer solutions. The reader is referred to [1,
pp. 252–256] for a proof by descent that w2 = u4 ± v4 has no positive integer solutions.
That the congruent number property for 1 and 2 is equivalent to the solvability of a single
equation in positive rational numbers (y2 = x4 −1 for 1 and y2 = x4 + 1 for 2) generalizes:
n is congruent if and only if y2 = x4 −n2 has a positive rational solution and if and only
if y2 = x4 + 4n2 has a positive rational solution. See Table 6, where the ﬁrst two columns
turn rational right triangles with area n into positive rational solutions of y2 = x4 −n2 and
conversely, and the last two columns do the same with y2 = x4 + 4n2. As in Table 5, the
correspondences in the ﬁrst two columns of Table 6 are not inverses of each other, but the
correspondences in the last two columns are inverses. (When n = 2 the equation in Table
6 is y2 = x4 + 16 rather than y2 = x4 + 1 as in Table 5. We can easily pass from the former
to the latter by replacing y with 4y and x with 2x.) The equivalence of n being congruent
with y2 = x4 −n2 having a positive rational solution is due to Lucas (1877).
a2 + b2 = c2,
y2 = x4 −n2
a2 + b2 = c2,
y2 = x4 + 4n2
1
2ab = n
1
2ab = n
x = c/2
a = y/x
x = a
a = x
y = |a2 −b2|/4
b = 2nx/y
y = ac
b = 2n/x
c = (x4 + n2)/xy
c = y/x
Table 6. More correspondences between rational right triangles and Dio-
phantine equations.
We pulled the equations y2 = x4 −n2 and y2 = x4 + 4n2 out of nowhere. How could
they be discovered? The arithmetic progression viewpoint on congruent numbers (Theorem
3.1) leads to one of them. If n is congruent, there are rational squares r2, s2, and t2 with
s2 −r2 = n and t2 −s2 = n. Then r2 = s2 −n and t2 = s2 + n, so multiplication gives
(rt)2 = s4 −n2 and we’ve solved y2 = x4 −n2 in positive rational numbers.
Remark B.1. For t ̸= 0, solutions to y2 = x4 + t and to Y 2 = X3 −4tX are in a one-to-
one correspondence, by (x, y) 7→(2t/(y −x2), 4tx/(y −x2)) and (X, Y ) 7→(Y/2X, (Y 2 +
8tX)/4X2).
In particular, solutions to y2 = x4 −n2 correspond to solutions to Y 2 =
X3 + (2n)2X, which is not the equation Y 2 = X3 −(2n)2X and thus isn’t related to
whether or not 2n is a congruent number. Explicit examples show the lack of a general
connection between n and 2n being congruent: 5 is congruent but 10 is not, while 3 is not
congruent but 6 is.

<!-- page 17 -->
THE CONGRUENT NUMBER PROBLEM
17
References
[1] D. M. Burton, “Elementary Number Theory,” 6th ed., McGraw-Hill, New York, 2007.
[2] W. A. Coppel, “Number Theory: An Introduction to Mathematics. Part B,” Springer-Verlag, New York,
2006.
[3] L. E. Dickson, “History of the Theory of Numbers,” Vol. II, Chelsea, New York, 1952.
[4] A. Genocchi, “Sopra Tre Scritti Inediti di Leonardo Pisano Pubblicati da Baldassarre Boncompagni:
Note Analitiche,” Tipograﬁa delle Belle Arti, Rome, 1855. URL https://archive.org/details/
sopratrescritti00genogoog/mode/2up.
[5] B. Hemenway, On Recognizing Congruent Primes, M. Sc. Thesis, Simon Fraser University, 2006. URL
https://summit.sfu.ca/item/6418.
[6] G. Henniart, Congruent Numbers, Elliptic Curves, and Modular Forms, translation by F. Lemmermeyer.
URL http://www.fen.bilkent.edu.tr/~franz/publ/guy.pdf.
[7] N. Koblitz, “Introduction to Elliptic Curves and Modular Forms,” 2nd ed., Springer–Verlag, New York,
1993.
[8] A. Knapp, “Elliptic Curves,” Princeton Univ. Press, Princeton, 1992.
[9] N. M. Stephens, Congruence properties of congruent numbers, Bull. London Math. Soc. 7 (1975), 182–
184.
[10] J. Tunnell, A Classical Diophantine Problem and Modular Forms of Weight 3/2, Invent. Math. 72
(1983), 323–334.
[11] E. Turri`ere, Le Probl`eme de Jean de Palerme et de L´eonard de Pise, L’Enseignement Math. 17 (1915),
315–324. URL https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1915%3A17#478.
[12] A. Weil, “Number Theory; an Approach through History from Hammurapi to Legendre,” Birkhauser,
Boston, 1984.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*