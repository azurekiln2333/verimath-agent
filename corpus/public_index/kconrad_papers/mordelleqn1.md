# Mordell's Equation

> **Source**: https://kconrad.math.uconn.edu/blurbs/mordelleqn1.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
EXAMPLES OF MORDELL’S EQUATION
KEITH CONRAD
1. Introduction
The equation y2 = x3 + k, for k ∈Z, is called Mordell’s equation1 due to Mordell’s work
on it throughout his life. A natural number-theoretic task is describing all of its solutions
in Z or Q, either qualitatively (decide if there are ﬁnitely or inﬁnitely many solutions in Z
or Q) or quantitatively (list or otherwise conveniently describe all such solutions). In 1920,
Mordell [10] showed that for each nonzero k ∈Z, y2 = x3 + k has ﬁnitely many integral
solutions. Rational solutions are a diﬀerent story: there may be ﬁnitely or inﬁnitely many,
depending on k. Whether there are ﬁnitely or inﬁnitely many rational solutions is connected
to a central topic in number theory: the rank of an elliptic curve.
Here we will describe all integral solutions to Mordell’s equation for some selected values
of k,2 and make a few comments at the end about rational solutions. For further examples
of the techniques we use to ﬁnd integral solutions, see [1, Chap. 14].
2. Examples without Solutions
To prove y2 = x3+k has no integral solution for speciﬁc values of k, we will use congruence
and quadratic residue considerations. Speciﬁcally, we will use the following descriptions of
when −1, 2, and −2 are squares modulo odd primes p, writing “□” to mean a square:
−1 ≡□mod p ⇐⇒p ≡1 mod 4,
2 ≡□mod p ⇐⇒p ≡1, 7 mod 8,
−2 ≡□mod p ⇐⇒p ≡1, 3 mod 8.
Our ﬁrst three theorems will use the criterion for −1 ≡□mod p.
Theorem 2.1. The equation y2 = x3 + 7 has no integral solutions.
Proof. Assume there is an integral solution (x, y). If x is even then y2 ≡7 mod 8, but
7 mod 8 is not a square. Therefore x is odd. Rewrite y2 = x3 + 7 as y2 + 1 = x3 + 8, so
(1)
y2 + 1 = x3 + 8 = (x + 2)(x2 −2x + 4).
Note x2 −2x + 4 = (x −1)2 + 3 is at least 3. Since x is odd, (x −1)2 + 3 ≡3 mod 4. Thus
x2 −2x + 4 has a prime factor p ≡3 mod 4: if not, all of its prime factors are 1 mod 4,
so x2 −2x + 4 ≡1 mod 4 since a positive integer is the product of its prime factors (this
isn’t true for −5: −5 ≡3 mod 4 and the prime factor of −5 is 1 mod 4). That contradicts
x2 −2x+4 ≡3 mod 4. From p | (x2 −2x+4) we get p | (y2 +1) by (1), so y2 +1 ≡0 mod p.
Thus −1 ≡□mod p, contradicting p ≡3 mod 4. This is V. A. Lebesgue’s method [8].
1Also called Bachet’s equation.
2Large tables of k and their integral solutions are at https://hhr-m.de/mordell/ and https://secure.
math.ubc.ca/∼bennett/BeGa-data.html.
1

<!-- page 2 -->
2
KEITH CONRAD
Here’s another approach, using the factor x + 2 instead of the factor x2 −2x + 4. Since
(as seen above) x is odd and y is even, x3 ≡x mod 4 (true for all odd x), so reducing
y2 = x3 + 7 modulo 4 gives us 0 ≡x + 3 mod 4, so x ≡1 mod 4. Then x + 2 ≡3 mod 4.
Moreover, x+2 > 0, since if x ≤−2 then x3 ≤−8, so x3 +7 ≤−1, which contradicts x3 +7
being a perfect square. From x + 2 being positive and congruent to 3 mod 4, it has a prime
factor p ≡3 mod 4, so y2 + 1 ≡0 mod p from (1) and we get a contradiction as before.
□
Theorem 2.2. The equation y2 = x3 −5 has no integral solutions.
Proof. Assuming there is a solution, reduce modulo 4:
y2 ≡x3 −1 mod 4.
Here is a table of values of y2 and x3 −1 modulo 4:
y
y2 mod 4
x
x3 −1 mod 4
0
0
0
3
1
1
1
0
2
0
2
3
3
1
3
2
The only common value of y2 mod 4 and x3 −1 mod 4 is 0, so y is even and x ≡1 mod 4.
Then rewrite y2 = x3 −5 as
(2)
y2 + 4 = x3 −1 = (x −1)(x2 + x + 1).
Since x ≡1 mod 4, x2 + x + 1 ≡3 mod 4, so x2 + x + 1 is odd. Moreover, x2 + x + 1 =
(x + 1/2)2 + 3/4 > 0, so x2 + x + 1 ≥3. Therefore x2 + x + 1 must have a prime factor
p ≡3 mod 4 (same reasoning as in the previous proof). Since p is a factor of x2 + x + 1, p
divides y2 + 4 by (2), so y2 + 4 ≡0 mod p. Therefore −4 ≡□mod p, so −1 ≡□mod p.
This implies p ≡1 mod 4, contradicting p ≡3 mod 4.
□
Theorem 2.3. The equation y2 = x3 + 11 has no integral solutions.
Proof. We will use ideas from the proofs of Theorems 2.1 and 2.2.
Assume there is an integral solution (x, y). Since 11 ≡−1 mod 4, the same reasoning as
in the proof of Theorem 2.2 shows x ≡1 mod 4.
Rewrite y2 = x3 + 11 as
(3)
y2 + 16 = x3 + 27 = (x + 3)(x2 −3x + 9).
The factor x2−3x+9 is positive (why?), and from x ≡1 mod 4 we get x2−3x+9 ≡3 mod 4,
so by the same reasoning as in the proof of Theorem 2.1, x2 −3x + 9 has a prime factor
p with p ≡3 mod 4. Therefore p | (y2 + 16) by (3), so −16 ≡□mod p. Since p is odd,
−1 ≡□mod p, and that contradicts p ≡3 mod 4.
□
Our next two theorems will rely on the condition for when 2 ≡□mod p.
Theorem 2.4. The equation y2 = x3 −6 has no integral solutions.
Proof. Assume there is an integral solution. If x is even then y2 ≡−6 ≡2 mod 8, but
2 mod 8 is not a square. Therefore x is odd, so y is odd and x3 = y2 + 6 ≡7 mod 8. Also
x3 ≡x mod 8 (true for all odd x), so x ≡7 mod 8.
Rewrite y2 = x3 −6 as
(4)
y2 −2 = x3 −8 = (x −2)(x2 + 2x + 4),

<!-- page 3 -->
EXAMPLES OF MORDELL’S EQUATION
3
with x2 + 2x + 4 ≡72 + 2 · 7 + 4 ≡3 mod 8. Since x2 + 2x + 4 = (x + 1)2 + 3 is positive,
it must have a prime factor p ≡±3 mod 8 because if all of its prime factors are ±1 mod 8
then x2 + 2x + 4 ≡±1 mod 8, which is not true. Let p be a prime factor of x2 + 2x + 4 with
p ≡±3 mod 8. Since p divides y2 −2 by (4), we get y2 ≡2 mod p. Thus 2 ≡□mod p, so
p ≡±1 mod 8, which is a contradiction.
We can get a contradiction using the factor x−2 also. Since x ≡7 mod 8, x−2 ≡5 mod 8.
Also x −2 > 0, since if x ≤2 and x −2 ≡5 mod 8 then x ≤−1, but then x3 −6 is negative
so it can’t be a perfect square. From x−2 being positive and congruent to 5 mod 8, it has a
prime factor p ≡±3 mod 8 and then y2 ≡2 mod p and we get a contradiction in the same
way as before.
□
Theorem 2.5. The equation y2 = x3 + 45 has no integral solutions.
Proof. Assume there is an integral solution. If y is odd then x3 = y2−45 ≡1−45 ≡4 mod 8,
which is impossible.
Therefore y is even, so x is odd.
Reducing the equation mod 4,
0 ≡x3 + 1 mod 4. Since x3 ≡x mod 4 for odd x, x ≡3 mod 4. Also, y is not a multiple of
3. If 3 | y then the equation y2 = x3 + 45 shows 3 divides x. Write x = 3x′ and y = 3y′, so
9y′2 = 27x′3 + 45, so y′2 = 3x′3 + 5, which implies y′2 ≡2 mod 3, and that is impossible.
We will now take cases depending on whether x ≡3 mod 8 or x ≡7 mod 8. (If you know
an elementary method that treats both cases in a uniform way, please tell me!)
Case 1: x ≡3 mod 8. Rewrite y2 = x3 + 45 as
(5)
y2 −72 = x3 −27 = (x −3)(x2 + 3x + 9).
The factor x2 + 3x + 9 = (x + 3/2)2 + 27/4 is positive and is congruent to 3 mod 8, so it
has a prime factor p ≡±3 mod 8. Feeding this into (5),
(6)
y2 ≡72 ≡2 · 62 mod p.
We can’t have p = 3 (just in case p ≡3 mod 8, this is something we need to deal with)
since it would imply y2 ≡0 mod 3, but we already checked y is not a multiple of 3. Since
p is not 3, (6) implies 2 ≡□mod p, so p ≡±1 mod 8, contradicting p ≡±3 mod 8.
Case 2: x ≡7 mod 8. Rewrite y2 = x3 + 45 as
(7)
y2 −18 = x3 + 27 = (x + 3)(x2 −3x + 9).
The factor x2 −3x + 9 = (x −3/2)2 + 27/4 is positive and is congruent to 5 mod 8, so it
has a prime factor p ≡±3 mod 8. From (7) we get y2 ≡18 ≡2 · 32 mod p. Arguing as in
Case 1, we again ﬁnd p ≡±1 mod 8, which is a contradiction.
□
In our next two theorems we will use the condition for when −2 ≡□mod p.
Theorem 2.6. The equation y2 = x3 + 6 has no integral solutions.
Proof. Mordell [11, p. 22-23], [12, p. 70] proved this using Z[
√
6]. The simpler method used
here, which resembles the proof of Theorem 2.4, is due to Shiv Gupta and Tracy Driehaus.
Assume there is an integral solution. First we will show x is odd, and in fact x ≡3 mod 8.
If x is even then y2 ≡6 mod 8, which is impossible.
Thus x is odd, so y is odd and
x3 = y2 −6 ≡−5 ≡3 mod 8. Since x3 ≡x mod 8, we have x ≡3 mod 8.
Rewrite y2 = x3 + 6 as
(8)
y2 + 2 = x3 + 8 = (x + 2)(x2 −2x + 4),
with x2 −2x + 4 ≡32 −2 · 3 + 4 ≡7 mod 8. For each prime factor p of x2 −2x + 4,
y2 +2 ≡0 mod p, so −2 ≡□mod p, and therefore p ≡1, 3 mod 8. Then since x2 −2x+4 =

<!-- page 4 -->
4
KEITH CONRAD
(x −1)2 + 3 is positive, x2 −2x + 4 is 1 or 3 mod 8. We showed before that this number is
7 mod 8, so we have a contradiction.
To get a contradiction using the factor x + 2, ﬁrst note that this number is positive,
since if x + 2 < 0 then y2 + 2 ≤0, which is impossible. For a prime p dividing x + 2,
y2 + 2 ≡0 mod p, so p ≡1 or 3 mod 8. Therefore x + 2 ≡1 or 3 mod 8. However, since
x ≡3 mod 8 we have x + 2 ≡5 mod 8, which is a contradiction.
□
Theorem 2.7. The equation y2 = x3 + 46 has no integral solutions.
Proof. Assume there is an integral solution. If x is even then y2 ≡6 mod 8, which has no
solution, so x is odd and y is odd. Thus y2 ≡1 mod 8 and x3 ≡x mod 8, so 1 ≡x+6 mod 8,
making x ≡3 mod 8.
Now rewrite y2 = x3 + 46 as
(9)
y2 + 18 = x3 + 64 = (x + 4)(x2 −4x + 16).
Since x ≡3 mod 8, the ﬁrst factor on the right side of (9) is 7 mod 8 and the second factor
is 5 mod 8. We will get a contradiction using either of these factors.
First we work with the quadratic factor x2 −4x + 16 = (x −2)2 + 12, which is positive.
Since it is 5 mod 8, it must have a prime factor p that is not 1 or 3 mod 8. Indeed, if all the
prime factors of x2 −4x + 16 are 1 or 3 mod 8 then so is x2 −4x + 16, since {1, 3 mod 8} is
closed under multiplication. But x2−4x+16 ̸≡1, 3 mod 8. The prime p, not being 3 mod 8,
is in particular not equal to 3. Also, p ̸= 2 since x2−4x+16 is odd. Since p | (x2−4x+16) we
get by (9) that p | (y2 + 18), so y2 ≡−18 mod p. Hence −18 ≡□mod p, so −2 ≡□mod p.
This implies p ≡1 or 3 mod 8. But p ̸≡1 or 3 mod 8, so we have a contradiction.
To get a contradiction using the factor x + 4, ﬁrst let’s check it is positive.
There
is no solution to y2 = x3 + 46 when y2 is a perfect square less than 46 (just try y2 =
0, 1, 4, 9, 16, 25, 36; there is no corresponding integral x), which means we must have x3 > 0,
so x > 0. Thus x + 4 > 1. Since x + 4 ≡7 mod 8, x + 4 must have a prime factor p that is
not 1 or 3 mod 8, just as before. The prime p is not 2 since x + 4 is odd, and p ̸= 3 since
p ̸≡3 mod 8. Then y2 ≡−18 mod p from (9) and we get a contradiction as before.
□
Our next theorem uses the conditions for −1 mod p and −2 mod p to be squares.
Theorem 2.8. The equation y2 = x3 −24 has no integral solutions.
Proof. We take our argument from [13, pp. 271–272], which is based on [14, p. 201].
Assuming there is an integral solution (x, y), we show x is even. Rewrite y2 = x3 −24 as
y2 + 16 = x3 −8 = (x −2)(x2 + 2x + 4).
The factor x2 +2x+4 equals (x+1)2 +3, which is at least 3. If x is odd then (x+1)2 +3 ≡
3 mod 4, so (x+1)2 +3 has a prime factor p such that p ≡3 mod 4. Then y2 ≡−16 mod p,
so −1 ≡□mod p. This contradicts the condition p ≡3 mod 4. Therefore x is even, so also
y is even.
From y2 = x3 −24 we get 8 | y2, so 4 | y. Write x = 2x′ and y = 4y′. Then 16y′2 =
8x′3−24, which implies 2y′2 = x′3−3, so x′ is odd and greater than 1. Rewrite 2y′2 = x′3−3
as
2(y′2 + 2) = x′3 + 1 = (x′ + 1)(x′2 −x′ + 1).
The factor x′2 −x′ + 1 is odd and greater than 1. Let p be a prime factor of it, so y′2 ≡
−2 mod p, which implies p ≡1 or 3 mod 8. Then x′2 −x′ +1 is a product of primes that are
all 1 or 3 mod 8, so x′2−x′+1 ≡1 or 3 mod 8. But y′2 ≡0, 1, or 4 mod 8 ⇒x′3 = 2y′2+3 ≡

<!-- page 5 -->
EXAMPLES OF MORDELL’S EQUATION
5
3 or 5 mod 8 ⇒x′ ≡3 or 5 mod 8. Then x′2 −x′ + 1 ≡1 −x′ + 1 ≡2 −x′ ≡5 or 7 mod 8.
That contradicts x′2 −x′ + 1 ≡1 or 3 mod 8.
□
Remark 2.9. Multiplying both sides of y2 = x3 +k by a sixth power a6 in Z leads to a new
Mordell equation Y 2 = X3 + a6k with X = a2x and Y = a3y, but it is not the case that all
integral solutions to Y 2 = X3 + a6k have to come from integral solutions to y2 = x3 + k by
that change of variables. For example, y2 = x3 + 11 has no integral solutions by Theorem
2.3 but 26 · 11 = 704 and Y 2 = X3 + 704 has the integral solutions (−7, ±19).
As an exercise, show each of the following has no integral solutions by methods like those
used above. In each case, begin by showing x is odd (this is trickiest for the third equation).
(1) y2 = x3 −3 (Hint: y2 + 4 = x3 + 1).
(2) y2 = x3 −9 (Hint: y2 + 1 = x3 −8).
(3) y2 = x3 −12 (Hint: y2 + 4 = x3 −8).
3. Examples with Solutions
We will now look at some instances of Mordell’s equation that have integral solutions.
The goal in each case is to ﬁnd all the integral solutions. The main tool we will use is
unique factorization (in diﬀerent settings), and after some successes we will see that this
technique eventually runs into diﬃculties.
We start with the case k = 16: the equation y2 = x3 +16. There are two obvious integral
solutions: (x, y) = (0, ±4). A numerical search does not reveal additional integral solutions,
so one might guess3 that (0, 4) and (0, −4) are the only integral solutions. To prove this,
we will use unique factorization in Z.
Theorem 3.1. The only integral solutions to y2 = x3 + 16 are (x, y) = (0, ±4).
Proof. First we determine the parity of an integral solution. Rewrite the equation as x3 =
y2 −16 = (y + 4)(y −4). If y is odd then (y + 4, y −4) = 1 (why?), so both y + 4 and y −4
are cubes because their product is a cube. They diﬀer by 8, and no odd cubes diﬀer by 8.
Hence y is even, so x is even.
The right side of y2 = x3 + 16 is divisible by 8, so 4 | y. Writing y = 4y′, 16y′2 = x3 + 16.
Therefore 4 | x. Write x = 4x′, so y′2 = 4x′3 + 1, showing y′ is odd. Write y′ = 2m + 1, so
4m2+4m+1 = 4x′3+1. Thus m2+m = x′3. Since m2+m = m(m+1) and (m, m+1) = 1,
the product m(m + 1) being a cube implies (since ±1 are cubes) both m and m + 1 are
cubes. The only consecutive cubes are among {−1, 0, 1}, so m or m + 1 is 0. Therefore
x′ = 0, so x = 0 and y = ±4.
□
For the next few results, we use unique factorization in Z[i] or Z[√−2].
Theorem 3.2. The only x, y ∈Z satisfying y2 = x3 −1 is (x, y) = (1, 0).
Proof. First we check the parity of an integral solution. Suppose x is even, so y2 +1 = x3 ≡
0 mod 8. Then y2 ≡−1 mod 8. But −1 mod 8 is not a square. We have a contradiction, so
x is odd, which means y has to be even.
Write the equation y2 = x3 −1 as
x3 = y2 + 1,
3It’s a tricky business to decide when to stop searching: y2 = x3+24 has integral solutions at x = −2, 1, 10,
and 8158 (and no others). Contrast that with y2 = x3 −24 in Theorem 2.8. The equation y2 = x3 −999
has integral solutions at x = 10, 12, 40, 147, 174, and 22480 (and no others) [17].

<!-- page 6 -->
6
KEITH CONRAD
which in Z[i] has the factored form
(10)
x3 = (y + i)(y −i).
If the two factors on the right side are relatively prime in Z[i], then since their product
is a cube, each factor must be a cube up to unit multiple, by unique factorization in Z[i].
Moreover, since every unit in Z[i] is a cube (1 = 13, −1 = (−1)3, i = (−i)3, −i = i3), unit
factors can be absorbed into the cubes. Thus, provided we show y+i and y−i are relatively
prime, (10) tells us y + i and y −i are themselves cubes.
To see that y +i and y −i are relatively prime, let δ be a common divisor. Since δ divides
(y + i) −(y −i) = 2i, N(δ) divides N(2i) = 4. Also N(δ) divides N(y + i) = y2 + 1 = x3,
which is odd. Therefore N(δ) divides 4 and is odd, which means N(δ) = 1, so δ is a unit.
Now that we know y + i and y −i are relatively prime, we must have (as argued already)
y + i = (m + ni)3
for some m, n ∈Z. Expanding the cube and equating real and imaginary parts,
y = m3 −3mn2 = m(m2 −3n2),
1 = 3m2n −n3 = n(3m2 −n2).
The equation on the right tells us n = ±1. If n = 1, then 1 = 3m2 −1, so 3m2 = 2, which
has no integer solution. If n = −1, then 1 = −(3m2 −1), so m = 0. Therefore y = 0, so
x3 = y2 + 1 = 1. Thus x = 1.
□
Theorem 3.3. The only x, y ∈Z satisfying y2 = x3 −4 are (x, y) = (2, ±2) and (5, ±11).
Proof. We rewrite y2 = x3 −4 in Z[i] as
(11)
x3 = y2 + 4 = (y + 2i)(y −2i).
We will show that both factors on the right are cubes. Let’s ﬁrst see why this leads to the
desired integral solutions. Write
y + 2i = (m + ni)3
for some m, n ∈Z. Equating real and imaginary parts,
y = m(m2 −3n2),
2 = n(3m2 −n2).
From the second equation, n = ±1 or n = ±2. In each case we try to solve for m in Z. The
cases that work out are n = 1 and m = ±1, and n = −2 and m = ±1. In the ﬁrst case,
y = ±(1 −3) = ±2 and x = 2, while in the second case y = ±(1 −3 · 4) = ±11 and x = 5.
It remains to show in (11) that y + 2i and y −2i are cubes. Since y2 ≡x3 mod 2 either
x and y are both even or they are both odd. We will consider these cases separately, since
they aﬀect the greatest common factor of y + 2i and y −2i.
First suppose x and y are both odd. We will show y + 2i and y −2i are relatively prime
in Z[i]. Let δ be a common divisor, so δ divides (y + 2i) −(y −2i) = 4i. Therefore N(δ)
divides N(4i) = 16. Since N(δ) also divides N(y + 2i) = y2 + 4 = x3, which is odd, we must
have N(δ) = 1, so δ is a unit. This means y + 2i and y −2i are relatively prime, so since
their product in (11) is a cube and every unit in Z[i] is a cube, y + 2i and y −2i are both
cubes.
Now suppose x and y are both even. Write x = 2x′ and y = 2y′, so 4y′2 = 8x′3 −4.
Dividing by 4, y′2 = 2x′3 −1. Therefore y′ is odd. We must have x′ odd too, as otherwise
y′2 ≡−1 mod 4, but −1 mod 4 is not a square. Writing
2x′3 = y′2 + 1 = (y′ + i)(y′ −i),

<!-- page 7 -->
EXAMPLES OF MORDELL’S EQUATION
7
the factors on the right each have even norm, so each is divisible by 1 + i. Divide the
equation by (1 + i)2 = 2i:
−ix′3 = y′ + i
1 + i
y′ −i
1 + i .
We will show the two factors on the right are relatively prime. Their diﬀerence is 2i/(1+i) =
1 + i, so each common divisor has norm dividing N(1 + i) = 2. Also each common divisor
divides x′3, so the norm divides N(x′3) = x′6, which is odd. Thus each common divisor
of (y′ + i)/(1 + i) and (y′ −i)/(1 + i) has norm 1, so is a unit. As before, we now know
(y′ + i)/(1 + i) is a cube, so
y + 2i = 2(y′ + i) = −i(1 + i)2(y′ + i) = i3(1 + i)3 y′ + i
1 + i
is a cube in Z[i]. Similarly, y −2i is a cube.
□
Theorem 3.4. The only integral solutions to y2 = x3 −2 are (x, y) = (3, ±5).
Proof. Suppose y2 = x3 −2 with integral x and y. As in the previous proof, ﬁrst we do a
parity check on x and y. If x is even then y2 ≡−2 mod 8, but −2 mod 8 is not a square.
Therefore x is odd, so y is also odd.
Write the relation between x and y as
x3 = y2 + 2.
In Z[√−2], we can rewrite this as
(12)
x3 = (y +
√
−2)(y −
√
−2).
The two factors on the right are relatively prime.
Indeed, let δ be a common divisor,
so δ divides their diﬀerence (y + √−2) −(y −√−2) = 2√−2, which means N(δ) divides
N(2√−2) = 8. At the same time, N(δ) divides N(y +√−2) = y2 +2, which is odd since y is
odd. So N(δ) must be 1, which means δ is a unit in Z[√−2], so y + √−2 and y −√−2 are
relatively prime in Z[√−2]. From (12) and unique factorization in Z[√−2], y + √−2 and
y −√−2 are both cubes up to unit multiple. The units in Z[√−2] are ±1, which are both
cubes, and therefore a unit multiple of a cube is also a cube. Hence y + √−2 and y −√−2
are both cubes.
Write
y +
√
−2 = (m + n
√
−2)3
for some m, n ∈Z. It follows that
y = m3 −6mn2 = m(m2 −6n2),
1 = 3m2n −2n3 = n(3m2 −2n2).
From the second equation, n = ±1. When n = 1 the second equation says 1 = 3m2 −2,
so m = ±1. Then y = ±1(1 −6) = ±5 and x3 = y2 + 2 = 27, so we recover the solutions
(x, y) = (3, ±5). When n = −1 we have 1 = −(3m2 −2 · 12) = −(3m2 −2), so 1 = 3m2,
which has no solution in Z.
□
Remark 3.5. Theorems 3.3 and 3.4 were challenges by Fermat to British mathematicians
[4, p. 533], [18, pp. 103, 113]. Fermat said he could solve them by inﬁnite descent, but gave
no details. Our proof of Theorems 3.3 and 3.4, like that of Theorem 3.2, studies integers of
the form y2 + n by factoring them in Z[√−n], which is an idea due to Euler.

<!-- page 8 -->
8
KEITH CONRAD
Our treatment of y2 = x3 + 16, y2 = x3 −1, y2 = x3 −4, and y2 = x3 −2 relied on
features of Z, Z[i], and Z[√−2]: they have unique factorization and each unit in them is a
cube.
As an exercise, show each of the following three Mordell equations has only the indicated
integral solutions by using methods like those above.
(1) y2 = x3 −8 in Z only for (x, y) = (2, 0). (Hint: Start by showing y is even.)
(2) y2 = x3 −16 has no integral solutions. (Hint: Start by showing y is odd.)
(3) y2 = x3 −64 in Z only for (x, y) = (4, 0). (Hint: Start by showing y is even.)
We can try the same techniques on y2 = x3 + k for other values of k. The next three
examples illustrate some new features that can occur.
Example 3.6. Consider Mordell’s equation with k = 1: y2 = x3 + 1. (Don’t confuse this
with y2 = x3 −1, which is in Theorem 3.2.) There are several obvious integral solutions:
(x, y) = (−1, 0), (0, ±1), and (2, ±3).
We will use unique factorization in Z to try to show these are the only integral solutions.4
This will need a lot more work than our use of unique factorization in Z to study y2 = x3+16
in Theorem 3.1.
Rewrite the equation y2 = x3 + 1 in the form
x3 = y2 −1 = (y + 1)(y −1).
The integers y + 1 and y −1 diﬀer by 2, so (y + 1, y −1) is either 1 or 2.
Case 1: y is even. Then y + 1 and y −1 are both odd, so (y + 1, y −1) = 1. (That is, two
consecutive odd integers are always relatively prime.) Since y + 1 and y −1 have a product
that is a cube and they are relatively prime, unique factorization in Z tells us that they
are both cubes or both the negatives of cubes. The negative of a cube is also a cube (since
−1 = (−1)3), so y + 1 and y −1 are both cubes:
y + 1 = a3,
y −1 = b3.
Subtracting, we have a3 −b3 = 2. Considering how cubes spread apart, the only cubes that
diﬀer by 2 are 1 and −1. So a3 = 1 and b3 = −1, meaning a = 1 and b = −1. Therefore
y + 1 = 1, so y = 0 and x = −1. The integral solution (−1, 0) of y2 = x3 + 1 is the only
one where y is even.
Case 2: y is odd, so x is even. We expect to show that the only such integral solutions
are (0, ±1) and (2, ±3). Since y+1 and y−1 are both even and diﬀer by 2, (y+1, y−1) = 2.
Either y ≡1 mod 4 or y ≡3 mod 4. Since (x, y) is a solution if and only if (x, −y) is a
solution, by negating y if necessary we may assume y ≡1 mod 4. Then y + 1 ≡2 mod 4
and y −1 ≡0 mod 4. Dividing the equation x3 = y2 −1 by 8, we have
x
2
3
= y + 1
2
· y −1
4
.
The two factors on the right are relatively prime, since y+1 and y−1 have greatest common
factor 2 and we have divided each of them by a multiple of 2. Since the product of (y −1)/2
and (y + 1)/4 is a cube and the factors are relatively prime, each of them is a cube:
y + 1
2
= a3,
y −1
4
= b3
4In fact, these are the only rational solutions of y2 = x3 + 1. That is due to Euler [5, Theorem 10]. A
proof by descent is at https://kconrad.math.uconn.edu/blurbs/ugradnumthy/descentbyeuler.pdf.

<!-- page 9 -->
EXAMPLES OF MORDELL’S EQUATION
9
with integers a and b. (Actually, at ﬁrst we can say (y + 1)/2 and (y −1)/4 are cubes up
to sign, but −1 = (−1)3 so, as before, we can absorb a sign into a and b if signs occur.)
Solving each equation for y,
(13)
2a3 −1 = y = 4b3 + 1,
so a3−2b3 = 1. We can spot right away two integral solutions to a3−2b3 = 1: (a, b) = (1, 0)
and (a, b) = (−1, −1). In the ﬁrst case, using (13) we get y = 1 (so x = 0) and in the second
case we get y = −3 (so x = 2). We have found two integral solutions to y2 = x3 + 1 when
y ≡1 mod 4: (0, 1) and (2, −3). Negating y produces the two solutions (0, −1) and (2, 3)
where y ≡3 mod 4.
Therefore if a3 −2b3 = 1 has no integral solution (a, b) besides (1, 0) and (−1, −1), the
equation y2 = x3+1 has no integral solutions besides the ﬁve we know.5 That the only inte-
gral solutions of a3−2b3 = 1 are (1, 0) and (−1, −1) is a special case of the following general
theorem of Delaunay and Nagell [3, pp. 223–226], [7, Sect. VII.3], [9, Sect. 3-9]: for each
nonzero integer d, the equation a3 −db3 = 1 has at most one integral solution (a, b) with b ̸=
0. The cases d > 0 and d < 0 are equivalent since the exponent is odd: a3−db3 = a3+d(−b)3.
Proving the Delaunay–Nagell theorem, even for the special case d = 2, introduces many
new complications (a proof of this special case, using p-adic analysis, is in [15, pp. 34–35]6 or
see https://kconrad.math.uconn.edu/blurbs/gradnumthy/x3-2y3=1.pdf), so we omit
a proof and refer the reader to the indicated references.
Example 3.7. Consider y2 = x3 −5. We have already seen in Theorem 2.2 that this
equation has no integral solutions by a method that only uses calculations in Z. Let’s try
to show there are no integral solutions using factorizations in Z[√−5].
Start with a parity check. If x is even then y2 ≡−5 ≡3 mod 8, but 3 mod 8 is not a
square. Therefore x is odd, so y is even.
Write the equation as
x3 = y2 + 5 = (y +
√
−5)(y −
√
−5).
Suppose δ is a common factor of y + √−5 and y −√−5. First of all, N(δ) divides y2 + 5,
which is odd. Second of all, since δ divides (y + √−5) −(y −√−5) = 2√−5, N(δ) divides
N(2√−5) = 20. Therefore N(δ) is 1 or 5. If N(δ) = 5 then 5 | (y2 + 5), so 5 | y. Then
x3 = y2 +5 ≡0 mod 5, so x ≡0 mod 5. Now x and y are both multiples of 5, so 5 = x3 −y2
is a multiple of 25, a contradiction. Hence N(δ) = 1, so δ is a unit. This shows y + √−5
and y −√−5 have no common factor in Z[√−5] except for units.
Since y + √−5 and y −√−5 are relatively prime and their product is a cube, they are
both cubes (the units in Z[√−5] are ±1, which are both cubes). Thus
y +
√
−5 = (m + n
√
−5)3
for some integers m and n, so
y = m3 −15mn2 = m(m2 −15n2),
1 = 3m2n −5n3 = n(3m2 −5n2).
5The converse is true too: every integral solution of a3 −2b3 = 1 leads to the integral solution (x, y) =
(2ab, 4b3 + 1) of y2 = x3 + 1, so if y2 = x3 + 1 only has the ﬁve integral solutions we know then from
a3 −2b3 = 1 we must have (2ab, 4b3 + 1) = (0, 1) or (2, −3) since these are the only (x, y) with y ≡1 mod 4,
and from this it easily follows that (a, b) = (1, 0) and (−1, −1).
6In fact, (1, 0) and (−1, −1) are the only rational solutions of x3 −2y3 = 1, a result ﬁrst due to Euler [6,
Part II, Sect. II, § 247].

<!-- page 10 -->
10
KEITH CONRAD
From the second equation, n = ±1. If n = 1 then 1 = 3m2 −5, so 3m2 = 6, which has no
integral solution. If n = −1 then 1 = −(3m2 −5), so 3m2 = 4, which also has no integral
solution. We appear to have recovered the fact that y2 = x3 −5 has no integral solutions.
Alas, there is an error in Example 3.7. When we wrote certain numbers in Z[√−5] as
cubes, we were implicitly appealing to unique factorization in Z[√−5], which is in fact false.
A counterexample to unique factorization in Z[√−5] is 6 = 2 · 3 = (1 + √−5)(1 −√−5).
That doesn’t mean the numbers in Z[√−5] that we wanted to be cubes might not be cubes,
but our justiﬁcation for those conclusions is certainly faulty. It is true in Z[√−5] that if
αβ is a cube and α and β are relatively prime then α and β are both cubes, but to explain
why requires new techniques to circumvent the lack of unique factorization.
Example 3.8. Consider y2 = x3 −26. Two obvious integral solutions are (3, ±1). Let’s
use factorizations in Z[√−26] to see if (3, ±1) are the only integral solutions.
If x is even then y2 ≡−26 ≡6 mod 8, but 6 mod 8 is not a square. Therefore x is odd,
so y is odd too. Rewrite x3 = y2 + 26 as x3 = (y + √−26)(y −√−26). Let δ be a common
factor of y+√−26 and y−√−26 in Z[√−26]. Then N(δ) divides y2+26, which is odd. Also
δ divides the diﬀerence (y + √−26) −(y −√−26) = 2√−26, so N(δ) divides 4 · 26 = 8 · 13.
Since N(δ) is odd, we see that N(δ) is 1 or 13. There is no element of Z[√−26] with norm
13, so N(δ) = 1. Therefore δ = ±1, so y + √−26 and y −√−26 have only ±1 as common
factors.
If we assume Z[√−26] has unique factorization, then since y + √−26 and y −√−26
multiply to a cube and they have only ±1 as common factors, each of them is a cube. Write
y +
√
−26 = (m + n
√
−26)3,
so
y = m3 −78mn2 = m(m2 −78n2),
1 = 3m2n −26n3 = n(3m2 −26n2).
The second equation tells us n = ±1. If n = 1 then 1 = 3m2 −26, so 3m2 = 27, which tells
us m = ±3. Then y = (±3)(9 −78) = ±207 and x3 = 2072 + 26 = 42875 = 353, so x = 35.
We have discovered new integral solutions to y2 = x3 −26, namely (x, y) = (35, ±207). If
n = −1 then 1 = −(3m2 −26), so 3m2 = 25, which has no integral solutions.
Having looked at both possible values of n, we discovered two unexpected integral so-
lutions, but we missed the obvious integral solutions (3, ±1)!
How could that happen?
The reason is that our argument was based on the assumption of unique factorization in
Z[√−26], but there is not unique factorization in Z[√−26]. A counterexample is
27 = 3 · 3 · 3 = (1 +
√
−26)(1 −
√
−26).
It is true that the only integral solutions to y2 = x3 −26 are (3, ±1) and (35, ±207), but a
valid proof has to get around the lack of unique factorization in Z[√−26].
4. Rational solutions
For k ∈Z, if we consider rational solutions to y2 = x3 + k instead of integral solutions,
the situation gets much more complicated. First of all, there could be rational solutions
even if there are no integral solutions. For instance, y2 = x3 + 11 has no integral solutions
by Theorem 2.3, but this equation has the rational solution (x, y) = (−7/4, 19/8). In fact,
y2 = x3+11 has inﬁnitely many rational solutions. Second of all, sometimes the only rational
solutions are the integral solutions, but proving that is much harder than determining all
the integral solutions.

<!-- page 11 -->
EXAMPLES OF MORDELL’S EQUATION
11
To emphasize the distinction between classifying integral and rational solutions, consider
y2 = x3+16. We proved the only integral solutions are (0, ±4) in Theorem 3.1. This does not
tell us whether there are rational solutions of y2 = x3+16 that are not integral. It turns out
there are no further rational solutions, and here is an application of that. If a3 +b3 = c3 for
nonzero integers a, b, and c, then the nonzero rational numbers (x, y) = (4bc/a2, 4+8(b/a)3)
satisfy y2 = x3 + 16. (I found this choice in [2], and moving terms around in the equation
a3 + b3 = c3 leads to other rational solutions of y2 = x3 + 16. What do you get from
c3 + (−b)3 = a3?) Proving the only rational solutions to y2 = x3 + 16 are (0, ±4) would
force x = 0, but x = 4bc/a2 ̸= 0, so knowing the only rational solutions of y2 = x3 + 16 are
(0, ±4) implies Fermat’s Last Theorem for exponent 3.
The following table describes all the integral solutions for the cases of Mordell’s equation
we have looked at. (The examples k = 1 and −26 were not fully justiﬁed above.)
k
Z-solutions of y2 = x3 + k
1
(−1, 0), (0, ±1), (2, ±3)
−1
(1, 0)
−2
(3, ±5)
−4
(2, ±2), (5, ±11)
−5
None
6
None
−6
None
7
None
11
None
16
(0, 4), (0, −4)
−24
None
−26
(3, ±1), (35, ±207)
45
None
46
None
In each case there are ﬁnitely many integral solutions, and y2 = x3 + k has ﬁnitely many
integral solutions for every nonzero k in Z. If we look at rational solutions, then we might
not get anything new, but we could get a lot that is new. See the next table.
k
Q-solutions of y2 = x3 + k
1
(−1, 0), (0, ±1), (2, ±3)
−1
(1, 0)
−2
Inﬁnitely many
−4
Inﬁnitely many
−5
None
6
None
−6
None
7
None
11
Inﬁnitely many
16
(0, 4), (0, −4)
−24
None
−26
Inﬁnitely many
45
None
46
Inﬁnitely many

<!-- page 12 -->
12
KEITH CONRAD
The equations above that have more rational solutions than integral solutions are y2 =
x3 −2, y2 = x3 −4, y2 = x3 + 11, y2 = x3 −26, and y2 = x3 + 46. Examples of rational
solutions to these equations that are not integral solutions are in the following table.
k
−2
−4
11
−26
46
Q-soln
129
100, 383
1000

106
9 , 1090
27


−7
4, 19
8

705
4 , 18719
8


−7
4, 51
8

References
[1] S. Alaca and K. S. Williams, “Introductory Algebraic Number Theory,” Cambridge Univ. Press, Cam-
bridge, 2004.
[2] T. R. Bendz, ¨Ofver diophantiska ekvationen xn + yn = zn, Ph.D. thesis, Uppsala Univ., 1901.
[3] J. W. S. Cassels, “Local Fields,” Cambridge Univ. Press, Cambridge, 1986.
[4] L. E. Dickson, “History of the Theory of Numbers,” Vol. II, Chelsea, Bronx, 1971.
[5] L. Euler, Theorematum quorundam arithmeticorum demonstrationes, Comm. Acad. Sci. Petrop. 10
(1738), 125–146. English translation URL https://scholarlycommons.pacific.edu/euler-works/98/.
[6] L. Euler, “Elements of Algebra,” 1770. English translation URL http://www.17centurymaths.com/
contents/euleralgebra.htm.
[7] A. Fr¨ohlich, M. J. Taylor, “Algebraic Number Theory,” Cambridge Univ. Press, Cambridge, 1993.
[8] V. A. Lebesgue, Notes sur quelques ´equations ind´etermin´ees, Nouvelles Annales de Math´ematiques, 2e
s´er., 8 (1869), 452–456.
[9] W. J. Leveque, “Topics in Number Theory, Volume II,” Addison-Wesley, Reading, MA, 1956.
[10] L. J. Mordell, A Statement by Fermat, Proceedings of the London Math. Soc. 18 (1920), v-vi.
[11] L. J. Mordell, “A Chapter in the Theory of Numbers,” Cambridge Univ. Press, 1947.
[12] L. J. Mordell, “Two Papers on Number Theory,” VEB Deutscher Verlag der Wissenschaften, Berlin,
1972.
[13] H. N. Shapiro, “Introduction to the Theory of Numbers,” Wiley, New York, 1983.
[14] H. N. Shapiro and G. H. Sparer, “Power-quadratic Diophantine Equations and Descent,” Comm. Pure
and Applied Math. 31 (1978), 185–203. (Corrections in 32 (1979), 277–279.)
[15] N. P. Smart, “The Algorithmic Resolution of Diophantine Equations,” Cambridge Univ. Press, Cam-
bridge, 1998.
[16] H. M. Stark, “An Introduction to Number Theory,” MIT Press, Cambridge, 1978.
[17] R. P. Steiner, On Mordell’s Equation y2 −k = x3: A Problem of Stolarsky, Math. Comp. 47 (1986),
703–714.
[18] A. Weil, “Number Theory: An Approach Through History; from Hammurapi to Legendre,” Birkh¨auser,
Boston, 1984.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*