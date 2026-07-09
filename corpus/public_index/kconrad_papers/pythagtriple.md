# Pythagorean Triples

> **Source**: https://kconrad.math.uconn.edu/blurbs/pythagtriple.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PYTHAGOREAN TRIPLES
KEITH CONRAD
1. Introduction
A Pythagorean triple is a triple of positive integers (a, b, c) where a2 + b2 = c2. Examples
include (3, 4, 5), (5, 12, 13), and (8, 15, 17). Below is an ancient Babylonian tablet listing
15 Pythagorean triples. It is called Plimpton 322 (George Arthur Plimpton donated it to
Columbia University). For more information about it, see [1].
Plimpton 322
Some Pythagorean triples are scalar multiples of other triples: (6, 8, 10) is twice (3, 4, 5).
We call a triple (a, b, c) primitive when the three integers have no common factor. For any
triple (a, b, c), if d is the greatest common divisor of all three terms then (a/d, b/d, c/d) is a
primitive triple and the original triple is a scalar multiple of this, so ﬁnding all Pythagorean
triples is basically the same as ﬁnding all primitive Pythagorean triples. Our goal is to
describe the primitive Pythagorean triples.
We will be using diﬀerent characterizations of primitive triples, as described in the fol-
lowing lemma.
Lemma 1.1. For a Pythagorean triple (a, b, c), the following properties are equivalent:
(1) a, b, and c have no common factor, i.e., the triple is primitive,
(2) a, b, and c are pairwise relatively prime,
(3) two of a, b, and c are relatively prime.
Proof. To show (1) implies (2), we prove the contrapositive. If (2) fails then two of a, b, and
c have a common prime factor. Suppose a prime p divides a and b. Then c2 = a2 + b2 is
divisible by p, and since p | c2 also p | c, so p is a common factor of a, b, and c. A similar
argument works using a common prime factor of a and c or of b and c. Thus (1) fails.
It is easy to see that (2) implies (3) and (3) implies (1).
□
1

<!-- page 2 -->
2
KEITH CONRAD
Theorem 1.2. If (a, b, c) is a primitive Pythagorean triple then one of a or b is even and
the other is odd. Taking b to be even,
(1.1)
a = k2 −ℓ2,
b = 2kℓ,
c = k2 + ℓ2
for integers k and ℓwith k > ℓ> 0, (k, ℓ) = 1, and k ̸≡ℓmod 2. Conversely, for such
integers k and ℓthe above formulas yield a primitive Pythagorean triple.
k
ℓ
a
b
c
2
1
3
4
5
3
2
5
12
13
4
1
15
8
17
4
3
7
24
25
Table 1. Examples of Primitive Triples
Table 1 lists examples of k and ℓfor some primitive triples. Notice the triple (8, 15, 17)
occurs in the table as (15, 8, 17) due to the convention in Theorem 1.2 that the middle term
of the triple is even. Since k ̸≡ℓmod 2, one of k and ℓis even and the other is odd. The
ﬁrst two rows in Table 1 shows either k or ℓcan be even; it depends on the triple (a, b, c).
How it depends on the triple will be seen at the end of Section 3.
Let’s ﬁrst check that the formula in Theorem 1.2 always yields primitive Pythagorean
triples. For all k and ℓin Z, the formula
(k2 −ℓ2)2 + (2kℓ)2 = (k2 + ℓ2)2
is true, so (k2 −ℓ2, 2kℓ, k2 + ℓ2) is a Pythagorean triple when k > ℓ> 0.1 When (k, ℓ) = 1
and k ̸≡ℓmod 2, let’s check (k2 −ℓ2, 2kℓ, k2 + ℓ2) is a primitive triple. This follows (by
Lemma 1.1) from showing k2 −ℓ2 and k2 + ℓ2 are relatively prime. If d is a (positive)
common divisor of k2 −ℓ2 and k2 + ℓ2 then d divides their sum and diﬀerence, which are
2k2 and 2ℓ2. Since k2 + ℓ2 and k2 −ℓ2 are odd, d is odd, so d | k2 and d | ℓ2. Since k and ℓ
are relatively prime, so are k2 and ℓ2, so d = 1.
If we relax any of the conditions on k and ℓin Theorem 1.2 we won’t get a primitive
Pythagorean triple. For instance, taking k = 3 and ℓ= 1 produces the triple (8, 6, 10). The
condition k ̸≡ℓmod 2 is violated here.
In the next two sections we will show in two ways, one algebraic and the other geometric,
that every primitive Pythagorean triple (a, b, c) arises in the form given by Theorem 1.2:
using unique factorization in Z and using intersections of lines and circles. Then we will
put the parametric formula in Theorem 1.2 to work and see some generalizations.
2. Proof of Theorem 1.2 by algebra
To show that one of a and b is odd and the other is even, suppose a and b are both
odd. Then a2 ≡b2 ≡1 mod 4, so c2 = a2 + b2 ≡2 mod 4. However, 2 mod 4 is not a
1Euclid, in Lemma 1 to Prop.
29 in Book X of his Elements, says a geometric formula equivalent to
(a, b, c) = (mn, (m2 −n2)/2, (m2 + n2)/2), where m ≡n mod 2, produces Pythagorean triples. This is (1.1)
with m = k + ℓand n = k −ℓ. See http://aleph0.clarku.edu/∼djoyce/elements/bookX/propX29.html
for a conversion of Euclid’s geometric Lemma 1 to an algebraic formula. Euclid did not claim his formula
gives all primitive triples. Who showed it does? See https://hsm.stackexchange.com/questions/14778.

<!-- page 3 -->
PYTHAGOREAN TRIPLES
3
square. Thus a or b is even. If both a and b are even the triple (a, b, c) is not primitive, a
contradiction. That shows one of a or b is odd and the other is even, so c2 = a2 + b2 is odd.
Taking b to be the even choice among a and b (swap their order if necessary), rewrite
a2 + b2 = c2 as
b2 = c2 −a2 = (c + a)(c −a).
Both a and c are odd, so c + a and c −a are even. Dividing by 4,
(2.1)
b
2
2
= c + a
2
c −a
2
.
The two integers on the right, (c+a)/2 and (c−a)/2, are relatively prime: if d is a common
divisor then it divides their sum and diﬀerence, which are c and a, and those are relatively
prime, so d = 1. Since c > a > 0, both factors on the right side of (2.1) are positive. Now
we’ll use the following lemma, which is a consequence of unique factorization in Z.
Lemma 2.1. If xy = z2 where x, y, z ∈Z+ and (x, y) = 1, then x and y are both squares.
Proof. The result is clear when x or y is 1, so let x, y > 1. Write them both in terms of
their prime factorizations:
x = pe1
1 · · · pek
k ,
y = qf1
1 · · · qfℓ
ℓ
for distinct primes p1, . . . , pk and q1, . . . , qℓand positive exponents ei and fj. No pi and qj
are equal since (x, y) = 1.
We have
xy = pe1
1 · · · pek
k qf1
1 · · · qfℓ
ℓ= z2.
In z2, each prime factor of z has even multiplicity, so the ei’s and fj’s are even by unique
factorization, say ei = 2e′
i and fj = 2f′
j. Then
x = (pe′
1
1 · · · p
e′
k
k )2,
y = (qf′
1
1 · · · q
f′
ℓ
ℓ)2,
so x and y are both squares.
□
Applying the lemma to x = (c + a)/2,y = (c −a)/2, and z = b/2 in (2.1),
(2.2)
c + a
2
= k2,
c −a
2
= ℓ2
for some k and ℓin Z+. We noted already that (c + a)/2 and (c −a)/2 are relatively prime,
so k and ℓare relatively prime. Adding and subtracting the equations in (2.2),
c = k2 + ℓ2 ,
a = k2 −ℓ2 ,
so
b
2
2
= k2ℓ2 =⇒b2 = 4k2ℓ2 =⇒b = 2kℓ,
the last step holding because b, k, and ℓare positive.
It remains to show k ̸≡ℓmod 2. If k ≡ℓmod 2, then k and ℓare both even or both
odd. Since k and ℓare relatively prime, they are not both even. If they were both odd
then k2 + ℓ2, 2kℓ, and k2 −ℓ2 would all be even, contradicting primitivity of (a, b, c). Thus
k ̸≡ℓmod 2.

<!-- page 4 -->
4
KEITH CONRAD
3. Proof of Theorem 1.2 by geometry
Pythagorean triples are connected to points on the unit circle: if a2 + b2 = c2 then
(a/c)2 + (b/c)2 = 1. So we get a rational point (a/c, b/c) on the unit circle x2 + y2 = 1.
For a primitive Pythagorean triple (a, b, c), the ﬁrst paragraph of the previous proof
shows we can take a odd and b even. Having done that, draw the line through (−1, 0) and
(a/c, b/c) as in the ﬁgure below. Its slope is
m =
b/c
1 + a/c =
b
a + c
and the line passes through (−1, 0), so the equation of the line is y = m(x + 1).
(−1, 0)
(a/c, b/c)
Substituting the equation for the line into the equation for the unit circle gives us an
equation whose roots are the x-coordinates of the two points on both the line and the circle:
1 = x2 + y2 = x2 + (m(x + 1))2 = (1 + m2)x2 + 2m2x + m2,
so
(3.1)
(1 + m2)x2 + 2m2x + m2 −1 = 0.
Since (−1, 0) and (a/c, b/c) lie on both the line and the circle, the two roots of (3.1) are −1
and a/c. The sum of the roots is −2m2/(1 + m2), so
−1 + a
c = −2m2
1 + m2 .
Thus
a
c = 1 −
2m2
1 + m2 = 1 −m2
1 + m2 .
Since (a/c, b/c) is on the line y = m(x + 1),
b
c = m
a
c + 1

= m
1 −m2
1 + m2 + 1

=
2m
1 + m2 .
Since m is the slope of a line connecting (−1, 0) to a point on the unit circle in the ﬁrst
quadrant, 0 < m < 1. Write m = b/(a + c) in reduced form as m = ℓ/k with relatively
prime k and ℓin Z+. Since m < 1, k > ℓ. Formulas for the reduced fractions a/c and b/c
in terms of m are
(3.2)
a
c = 1 −(ℓ/k)2
1 + (ℓ/k)2 = k2 −ℓ2
k2 + ℓ2

<!-- page 5 -->
PYTHAGOREAN TRIPLES
5
and
(3.3)
b
c =
2(ℓ/k)2
1 + (ℓ/k)2 =
2kℓ
k2 + ℓ2 .
By deﬁnition, k and ℓare relatively prime. Let’s check that k ̸≡ℓmod 2. If k ≡ℓmod 2
then k and ℓare both even or both odd, and they are not both even since they are relatively
prime. So k and ℓare odd. Then the fraction 2kℓ/(k2 + ℓ2) in (3.3) has an even numerator
and denominator, so it simpliﬁes further:
2kℓ
k2 + ℓ2 =
kℓ
(k2 + ℓ2)/2.
The numerator on the right is odd, so the numerator of the reduced form of this fraction
(divide numerator and denominator by their greatest common factor) is odd. The reduced
form is b/c by (3.3), so b is odd. But b is even by hypothesis, so we have a contradiction.
Thus k and ℓare not both odd, so k ̸≡ℓmod 2.
From the end of Section 1, the three numbers k2−ℓ2, 2kℓ, and k2+ℓ2 form a Pythagorean
triple and the ﬁrst and third numbers are relatively prime, so the triple is primitive by
Lemma 1.1. Therefore the fractions on the right in (3.2) and (3.3) are in reduced form. The
fractions a/c and b/c are also in reduced form since the triple (a, b, c) is primitive, so the
(positive) numerators and denominators match:
a = k2 −ℓ2,
b = 2kℓ,
c = k2 + ℓ2.
This concludes the geometric proof of Theorem 1.2.
Remark 3.1. While this derivation was motivated by geometry, the calculations were pure
algebra and we could formulate them without any reference to a picture. That is, if we have
numbers x and y where x2 + y2 = 1 and x ̸= −1, we can (without motivation) deﬁne the
number m by declaring it to ﬁt the condition y = m(x + 1), namely deﬁne m = y/(x + 1).
Substituting m(x + 1) for y in x2 + y2 = 1 tells us
x2 + m2(x + 1)2 = 1,
and expanding the square gives
0 = (1 + m2)x2 + 2m2x + (m2 −1) = (1 + m2)(x + 1)

x + m2 −1
1 + m2

,
so from x ̸= −1 we have x = (1 −m2)/(1 + m2) and y = m(x + 1) = 2m/(1 + m2).
One nice consequence of our geometric derivation of the formula for primitive Pythagorean
triples (a, b, c) is that it tells us which of k or ℓwill be even. The formula
m =
b
a + c = ℓ
k
says that ℓ/k is the reduced form fraction for b/(a + c). We know either ℓor k is even. We
will have k even when a+c is divisible by a higher power of 2 than b is, and ℓis even when b
is divisible by a higher power of 2 than a+c is. For instance, in the triple (3, 4, 5), a+c = 8
and b = 4, so k is even. (Here k = 2 and ℓ= 1.) The triple (5, 12, 13) has a + c = 18 = 2 · 9
and b = 12 = 22 · 3, so ℓis even. (Here k = 3 and ℓ= 2.)

<!-- page 6 -->
6
KEITH CONRAD
4. Applications
Using the parametric formula for primitive Pythagorean triples, we can address questions
concerning relations among the sides of a primitive right triangle.
The famous triples (3, 4, 5), and (5, 12, 13), have consecutive terms. What are all the
Pythagorean triples (a, b, c) with a pair of consecutive terms (either a and b, or b and c)?
Such a triple is primitive since consecutive integers are relatively prime.
First suppose a and b (the two legs) are consecutive. That a −b = ±1 means
(k2 −ℓ2) −2kℓ= ±1.
This can be rewritten as
(k −ℓ)2 −2ℓ2 = ±1,
where k −ℓis positive and odd and ℓis positive. Conversely, if we have a solution to
x2 −2y2 = ±1 in Z+, then necessarily x is odd and (x, y) = 1. Let k = x + y and ℓ= y,
so k > ℓ> 0, (k, ℓ) = 1, and k ̸≡ℓmod 2. Thus (k2 −ℓ2, 2kℓ, k2 + ℓ2) is a primitive triple,
so ﬁnding Pythagorean triples whose legs diﬀer by 1 is the same as ﬁnding positive integer
solutions to the Pell equation x2 −2y2 = ±1. Some examples are in Table 2.
x
y
k
ℓ
a
b
c
1
1
2
1
3
4
5
3
2
5
2
21
20
29
7
5
12
5
119
120
169
17
12
29
12
697
696
985
41
29
70
29
4059
4060
5741
Table 2. Consecutive Legs
Even if two legs in a primitive triple don’t diﬀer by 1, the formula for their diﬀerence is
still (k −ℓ)2 −2ℓ2, so the possible diﬀerences between legs in a primitive triple are precisely
the odd values of x2 −2y2 for positive integers x and y. Not every odd number can arise
in this way, e.g., the equation x2 −2y2 = 5 has no integral solution (why?), so no primitive
Pythagorean triple has its legs diﬀering by 5.
When a leg and hypotenuse diﬀer by 1, the story is much simpler. The hypotenuse is
odd, so it must diﬀer by 1 from the even leg. The diﬀerence is
k2 + ℓ2 −2kℓ= (k −ℓ)2,
which is an odd square. This is 1 only if k = ℓ+ 1 (recall k > ℓby convention), leading to
the triple (2ℓ+ 1, 2ℓ2 + 2ℓ, 2ℓ2 + 2ℓ+ 1). The ﬁrst four examples are in Table 3.
ℓ
2ℓ+ 1
2ℓ2 + 2ℓ
2ℓ2 + 2ℓ+ 1
1
3
4
5
2
5
12
13
3
7
24
25
4
9
40
41
Table 3. Consecutive Leg and Hypotenuse

<!-- page 7 -->
PYTHAGOREAN TRIPLES
7
Now we look at a connection between Pythagorean triples and pairs of reducible quadratic
polynomials, taken from [2]. Here “reducible” means integral coeﬃcients. While
x2 + 4x + 3 = (x + 1)(x + 3) and x2 + 4x −3 is irreducible,
we have
x2 + 5x + 6 = (x + 2)(x + 3) and x2 + 5x −6 = (x −1)(x + 6).
Are there more examples like the second one, where integral polynomials x2 + mx + n and
x2 + mx −n both factor? Here m and n are nonzero.
If we ask what happens when the sign of m changes, the answer is not interesting. Indeed,
if x2 +mx+n = (x−r1)(x−r2) then x2 −mx+n = (x+r1)(x+r2), so either both of these
factor (with integral coeﬃcients) or both don’t. Therefore in our question on x2 + mx ± n,
we may assume m > 0. Since the issue is about sign changes on n, we may take n > 0 also.
By the quadratic formula, the roots of x2 + mx ± n are −m ±
√
m2 ± 4n
2
, which are
integers exactly when m2 ± 4n = □. (Note m2 ± 4n ≡m mod 2, so the numerator is even
when the discriminant is a perfect square.) So we can factor x2 + mx + n and x2 + mx −n
if and only if
m2 −4n = d2,
m2 + 4n = e2,
d and e ∈Z.
Then d2 + e2 = 2m2, so d ≡e mod 2. Solving,
m2 = d2 + e2
2
=
e + d
2
2
+
e −d
2
2
.
Thus we have a Pythagorean triple (without a speciﬁed even term)
e −d
2
, e + d
2
, m

,
e −d
2
< e + d
2
< m.
As an exercise, show this Pythagorean triple is primitive if and only if (m, n) = 1.
There is a one-to-one correspondence
Pythagorean triples (a, b, c) with a < b < c ←→reducible x2 + mx ± n,
given by
(a, b, c) 7→x2 + cx ± ab
2 ,
x2 + mx ± n 7→
e −d
2
, e + d
2
, m

,
with m2 −4n = d2 and m2 + 4n = e2.
The table below shows some corresponding
Pythagorean triples and reducible x2 + mx ± n. In particular, the example x2 + 5x ± 6
corresponds to the (3, 4, 5) triple and thus is the simplest example.
a
b
c
m
n
x2 + mx + n
x2 + mx −n
3
4
5
5
6
(x + 2)(x + 3)
(x −1)(x + 6)
5
12
13
13
30
(x + 3)(x + 10)
(x −2)(x + 15)
8
15
17
17
60
(x + 5)(x + 12)
(x −3)(x + 20)
20
21
29
29
210
(x + 14)(x + 15)
(x −6)(x + 35)
Using the formula for primitive Pythagorean triples, we can now write a formula for all
the reducible pairs of polynomials x2 + mx ± n where (m, n) = 1:
x2 + (k2 + ℓ2)x ± kℓ(k2 −ℓ2),
where k > ℓ> 0, (k, ℓ) = 1, and k ̸≡ℓmod 2. As an exercise, work out the factorization of
this polynomial explicitly in terms of k and ℓ.

<!-- page 8 -->
8
KEITH CONRAD
5. Generalizations
Our two derivations of the parametric formula for primitive Pythagorean triples, one
algebraic and the other geometric, are each worthwhile: they let us extend Theorem 1.2 in
diﬀerent directions.2
The algebraic proof of Theorem 1.2 carries over to Pythagorean triples of polynomials in
R[T]. These are polynomials f(T), g(T), and h(T) in R[T] that satisfy
f(T)2 + g(T)2 = h(T)2.
One example of such a triple is (T 2 −1, 2T, T 2 + 1).
Can we describe all polynomial
Pythagorean triples?
There are two features of the Pythagorean triples of integers that play no role when we
look at Pythagorean triples of polynomials:
(1) The special attention to positive solutions of a2 + b2 = c2 is ignored. We allow any
polynomial solutions to f2 + g2 = h2 with the only restriction being that f, g, and
h are all nonzero.
(2) The number 2 is an invertible constant in R[T], so the even/odd aspect that occurs
for integral Pythagorean triples simply drops out of consideration. Being divisible
by 2 is not important in R[T] since everything is divisible by 2: f(T) = 2(f(T)/2)
in R[T].
We will call a Pythagorean triple of polynomials (f, g, h) primitive if the terms in it are
pairwise relatively prime. This is the same as any two of the polynomials being relatively
prime, and is also the same as (f, g, h) not being a non-constant multiple of another triple
(polynomial analogue of Lemma 1.1).
Theorem 5.1. The primitive Pythagorean triples (f(T), g(T), h(T)) in R[T] are given by
the formulas
f(T) = c(k(T)2 −ℓ(T)2),
g(T) = ±2ck(T)ℓ(T),
h = ±c(k(T)2 + ℓ(T)2)
where c ∈R× and k(T) and ℓ(T) are relatively prime in R[T].
Proof. This is left as an exercise in adapting the techniques in the algebraic proof of Theorem
1.2. Note that if two polynomials are relatively prime and multiply to a squared polynomial,
the two polynomials have to be squares up to constant multiple. This follows from unique
factorization in R[T].
□
The geometric proof of Theorem 1.2 gives us a non-trigonometric parametrization of the
points on the unit circle: for each point (x0, y0) on the circle x2 +y2 = 1 other than (−1, 0),
has the form
(5.1)
x0 = 1 −m2
1 + m2 ,
y0 =
2m
1 + m2
where m = y0/(x0 + 1).
The formulas in (5.1) for x0 and y0 arise by looking at the
intersection points of the circle x2 + y2 = 1 and the line y = m(x + 1), where the linear
2Other ways of getting the parametric formula use more advanced ideas: a proof based on factoring in the
Gaussian integers is in Theorem 8.3 in https://kconrad.math.uconn.edu/blurbs/ugradnumthy/Zinotes.
pdf and a proof based on Hilbert’s Theorem 90 from Galois theory is at the end of Section 4 of https://
kconrad.math.uconn.edu/blurbs/galoistheory/linearchar.pdf.

<!-- page 9 -->
PYTHAGOREAN TRIPLES
9
equation describes the lines through (−1, 0) other than a vertical line. The correspondences
(5.2)
m ⇝
1 −m2
1 + m2 ,
2m
1 + m2

,
(x, y) ⇝m =
y
1 + x,
between real numbers m and points on the unit circle (x, y) other than (−1, 0) are inverses
of each other, as the reader can check. Moreover, the formulas have arithmetic content: m
is rational if and only if x0 and y0 are both rational since the formulas in (5.2) both have
rational output if there is rational input. So (5.1) is well-suited to describe the rational
points on x2 + y2 = 1. See Table 4. Compare this to the trigonometric parametrization
(cos θ, sin θ), where nearly all rational points have messy corresponding angles θ.
m
x
y
1/2
3/5
4/5
1/3
4/5
3/5
2/5
21/29
20/29
7/9
16/65
63/65
Table 4. Rational points from slopes on x2 + y2 = 1
Comparing the rational parametrization of the unit circle in (5.1) and the trigonometric
parametrization (cos θ, sin θ), we can write (with some assistance from (5.2))
(5.3)
cos θ = 1 −m2
1 + m2 ,
sin θ =
2m
1 + m2 ,
m =
sin θ
1 + cos θ.
A point on the unit circle at angle θ relative to the origin and the positive x-axis makes an
angle θ/2 relative to the point (−1, 0) and the x-axis, as shown in the ﬁgure below. The slope
of a line equals the tangent of the angle the line makes with the x-axis, so m = tan(θ/2) .
(−1, 0)
(cos θ, sin θ)
θ
θ/2
The formulas in (5.3) have a connection to calculus. In terms of the substitution u =
tan(θ/2), which is motivated by the formula for the slope m above, we can write
cos θ = 1 −u2
1 + u2 ,
sin θ =
2u
1 + u2 ,
and
du = sec2
θ
2
 dθ
2 =

1 + tan2
θ
2
 dθ
2 = (1 + u2) dθ
2 =⇒dθ =
2
1 + u2 du.

<!-- page 10 -->
10
KEITH CONRAD
With these formulas, integrals of rational functions of cos θ and sin θ can be turned into inte-
grals of rational functions of u. This method of integration is called a tan(θ/2)-substitution
or a Weierstrass substitution.3 It is based on having two diﬀerent parametrizations of the
unit circle, which allow us to express an integral involving one of the parameterizations (with
trig functions) as an integral involving the other parametrization (with rational functions).
What we just did with rational points on the unit circle is not true just for that curve. If
we take any smooth conic in the plane (a smooth curve of degree 2: an ellipse, hyperbola,
or parabola) that is deﬁned by an equation having rational coeﬃcients and we know one
rational point on the conic, then slopes of lines through that point let us parametrize all
the other rational points on the conic. Here is an example of this idea using another circle.
Theorem 5.2. The rational points on the circle x2 + y2 = 2 other than (−1, 1) can be
described by the formula
1 + 2m −m2
m2 + 1
, m2 + 2m −1
m2 + 1

where m ∈Q.
A rational point (x, y) other than (−1, ±1) arises this way using m =
(y + 1)/(x + 1), and (−1, −1) arises this way using m = −1.
Proof. The point (−1, −1) lies on the circle. A non-vertical line through (−1, −1) has the
form y = m(x + 1) −1. Any line through (−1, −1) intersects the circle in a second point,
except for the tangent line y = −x −2 (where m = −1).
x
y
(−1, −1)
(−1, 1)
To ﬁnd the second point of intersection, substitute the equation of the line into the
equation x2 + y2 = 2 and solve for the two roots of the resulting quadratic in x: one
root is 1, and we can ﬁnd the other root by the same method as in the geometric proof
of Theorem 1.2. This will give the x-coordinate formula above, and substituting this into
y = m(x + 1) −1 gives the y-coordinate. The only rational point on x2 + y2 = 2 that we
don’t ﬁnd by this method is (−1, 1), which is the second intersection point of the circle
with the vertical line through (−1, −1). This vertical line is not described by an equation
of the form y = m(x + 1) −1. The parameter value that gives the point (−1, −1) itself is
m = −1, which is the slope of the tangent line to x2 + y2 = 2 at (−1, −1) (touching the
point (−1, −1) twice, in a sense).
□
Remark 5.3. Since x2 +y2 = 2 if and only if ((x−y)/2)2 +((x+y)/2)2 = 1, the geometric
proof of Theorem 1.2 yields (x −y)/2 = (1 −m2)/(1 + m2) and (x + y)/2 = 2m/(1 + m2).
Adding and subtracting these equations recovers the formulas for x and y in Theorem 5.2.
3See https://en.wikipedia.org/wiki/Weierstrass substitution.

<!-- page 11 -->
PYTHAGOREAN TRIPLES
11
Armed with the description of the rational points on x2 + y2 = 2 in Theorem 5.2, we
can get a description of the primitive integral solutions of a2 + b2 = 2c2, where primitive
means a, b, and c have no common factor (equivalently, this means any two of a, b, and c
are relatively prime, i.e., an analogue of Lemma 1.1 holds). In a primitive triple (a, b, c), a
and b both must be odd, so 2c2 ≡2 mod 8, hence c is odd as well. For Pythagorean triples,
the middle term was chosen to be the even one. The analogue of that here is that we take
c > 0 and pick the signs on a and b so that a ̸≡b mod 4. With these conventions, we have
a = k2 + 2kℓ−ℓ2,
b = ℓ2 + 2kℓ−k2,
c = k2 + ℓ2
where (k, ℓ) = 1, k ̸≡ℓmod 2, and k > 0. Conversely, any triple deﬁned by these formulas
is a primitive solution to a2 + b2 = 2c2 with b ̸≡a mod 4.
k
ℓ
a
b
c
1
2
1
7
5
1
−2
−7
−1
5
1
4
−7
23
17
4
1
23
−7
29
2
5
−1
41
29
Table 5. Primitive Solutions to a2 + b2 = 2c2
Integers satisfying a2 + b2 = 2c2 are not the sides of a right triangle, but they have
an arithmetic interpretation: since c2 =
1
2(a2 + b2), c2 is the average of a2 and b2.
In
other words, a2, c2, b2 is an arithmetic progression of squares (taking a2 < b2). From Table
5, squaring the entries in the a, b, and c columns yield three such progressions: 1, 25, 49
(common diﬀerence 24), 49, 289, 529 (common diﬀerence 240), and 1, 841, 1681 (common
diﬀerence 840). There are inﬁnitely many 3-term arithmetic progressions of squares in Z+,
and we can ﬁnd all of them from the parametrization of the rational points on x2 + y2 = 2
in Theorem 5.2.
What about 4-term arithmetic progressions of squares? That is a more complicated story.
See https://kconrad.math.uconn.edu/blurbs/ugradnumthy/4squarearithprog.pdf.
References
[1] W. Casselman, http://www.math.ubc.ca/∼cass/courses/m446-03/pl322/pl322.html.
[2] J. L. Poet and D. L. Vestal, Jr., “Curious Consequences of a Miscopied Quadratic,” College Math. J.
36 (2005), 273–277.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*