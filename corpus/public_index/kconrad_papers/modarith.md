# Modular Arithmetic

> **Source**: https://kconrad.math.uconn.edu/blurbs/modarith.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
MODULAR ARITHMETIC
KEITH CONRAD
1. Introduction
We will deﬁne the notion of congruent integers (with respect to a modulus) and develop
some basic ideas of modular arithmetic. Applications of modular arithmetic are given to
divisibility tests and to block ciphers in cryptography.
Modular arithmetic lets us carry out algebraic calculations on integers with a system-
atic disregard for terms divisible by a certain number (called the modulus). This kind of
“reduced algebra” is essential background for the mathematics of computer science, coding
theory, primality testing, and much more.
2. Integer congruences
The following deﬁnition was introduced by Gauss in his Disquisitiones Arithmeticae
(Arithmetic Investigations) in 1801.
Deﬁnition 2.1 (Gauss). Let m be an integer. For a, b ∈Z, we write
a ≡b mod m
and say “a is congruent to b modulo m” if m | (a −b).
Example 2.2. Check 18 ≡4 mod 7, −20 ≡13 mod 11, and 19 ≡3 mod 2.
Remark 2.3. The parameter m is called the modulus, not the modulo. The symbol ≡in
LaTeX is written as \equiv, but it is always pronounced “congruent,” never “equivalent”.
(The LaTeX command \cong is for the congruence symbol ∼= in elementary geometry.)
We always have m ≡0 mod m, and more generally mk ≡0 mod m for any k ∈Z. In
fact,
a ≡0 mod m ⇐⇒m | a,
so the congruence relation includes the divisibility relation as a special case: the multi-
ples of m are exactly the numbers that “look like 0” modulo m. Because multiples of m
are congruent to 0 modulo m, we will see that working with integers modulo m is tanta-
mount to systematically ignoring additions and subtractions by multiples of m in algebraic
calculations.
Since a ≡b mod m if and only if b = a+mk for some k ∈Z, adjusting an integer modulo
m is the same as adding (or subtracting) multiples of m to it. Thus, if we want to ﬁnd a
positive integer congruent to −18 mod 5, we can add a multiple of 5 to −18 until we go
positive. Adding 20 does the trick: −18 + 20 = 2, so −18 ≡2 mod 5 (check!).
There is a useful analogy between integers modulo m and angle measurements (in radians,
say). In both cases, the objects involved admit diﬀerent representations, e.g., the angles 0,
2π, and −4π are the same, just as
2 ≡12 ≡−13 mod 5.
1

<!-- page 2 -->
2
KEITH CONRAD
Every angle can be put in “standard” form as a real number in the interval [0, 2π). There
is a similar convention for the “standard” representation of an integer modulo m using
remainders, as follows.
Theorem 2.4. Let m ∈Z be a nonzero integer. For each a ∈Z, there is a unique r with
a ≡r mod m and 0 ≤r < |m|.
Proof. Using division with remainder in Z, there are q and r in Z such that
a = mq + r,
0 ≤r < |m|.
Then m | (a −r), so a ≡r mod m.
To show r is the unique number in the range {0, 1, . . . , |m| −1} that is congruent to
a mod m, suppose two numbers in this range work:
a ≡r mod m,
a ≡r′ mod m,
where 0 ≤r, r′ < |m|. Then we have
a = r + mk,
a = r′ + mℓ
for some k and ℓin Z, so the remainders r and r′ have diﬀerence
r −r′ = m(ℓ−k).
This is a multiple of m, and the bounds on r and r′ tell us |r −r′| < |m|. A multiple of m
has absolute value less than |m| only if it is 0, so r −r′ = 0, which means r′ = r.
□
Example 2.5. Taking m = 2, every integer is congruent modulo 2 to exactly one of 0 and 1.
Saying n ≡0 mod 2 means n = 2k for some integer k, so n is even, and saying n ≡1 mod 2
means n = 2k + 1 for some integer k, so n is odd. We have a ≡b mod 2 precisely when a
and b have the same parity: both are even or both are odd.
Example 2.6. Every integer is congruent mod 4 to exactly one of 0, 1, 2, or 3. Congruence
mod 4 is a reﬁnement of congruence mod 2: even numbers are congruent to 0 or 2 mod 4 and
odd numbers are congruent to 1 or 3 mod 4. For instance, 10 ≡2 mod 4 and 19 ≡3 mod 4.
Congruence mod 4 is related to Master Locks. Every combination on a Master Lock is a
triple of numbers (a, b, c) where a, b, and c vary from 0 to 39. Each number has 40 choices,
with b ̸= a and c ̸= b (perhaps c = a). This means the number of combinations could be
up to 40 · 392 = 60840, but in fact the true number of combinations is a lot smaller: every
combination has c ≡a mod 4 and b ≡a + 2 mod 4, so once some number in a combination
is known the other two numbers are each limited to 10 choices (among the 40 numbers
in {0, 1, . . . , 39} exactly 10 will be congruent to a particular value mod 4). Thus the real
number of Master Lock combinations is 40 · 102 = 4000.
Example 2.7. Every integer is congruent modulo 7 to exactly one of 0, 1, 2, . . . , 6. The
choice is the remainder when the integer is divided by 7. For instance, 20 ≡6 mod 7 and
−32 ≡3 mod 7.
Deﬁnition 2.8. We call {0, 1, 2, . . . , |m|−1} the standard representatives for integers mod-
ulo m.
In practice m > 0, so the standard representatives modulo m are {0, 1, 2, . . . , m −1}. In
fact, congruence modulo m and modulo −m are the same relation (just look back at the
deﬁnition), so usually we never talk about negative moduli. Nevertheless, Theorem 2.4 is
stated for any modulus m ̸= 0 for completeness.

<!-- page 3 -->
MODULAR ARITHMETIC
3
By Theorem 2.4, there are |m| incongruent integers modulo m. We can represent each
integer modulo m by one of the standard representatives, just like we can write any fraction
in a reduced form. There are many other representatives which could be used, however,
and this will be important in the next section.
3. Modular Arithmetic
When we add and multiply fractions, we can change the representation (that is, use a
diﬀerent numerator and denominator) and the results are the same. We will meet a similar
idea with addition and multiplication modulo m.
Theorem 3.1. If a ≡b mod m and b ≡c mod m then a ≡c mod m.
Proof. By hypothesis, a −b = mk and b −c = mℓfor some integers k and ℓ. Adding the
equations, a −c = m(k + ℓ) and k + ℓ∈Z, so a ≡c mod m.
□
This result is called transitivity of congruences. We will usually use it without comment
in our calculations below.
The following theorem is the key algebraic feature of congruences in Z: they behave well
under addition and multiplication.
Theorem 3.2. If a ≡b mod m and c ≡d mod m, then
a + c ≡b + d mod m and ac ≡bd mod m.
Proof. We want to show (a + c) −(b + d) and ac −bd are multiples of m. Write a = b + mk
and c = d + mℓfor k and ℓin Z. Then
(a + c) −(b + d) = a −b + c −d = m(k + ℓ),
so a + c ≡b + d mod m. For multiplication,
ac −bd
=
(b + mk)(d + mℓ) −bd
=
m(kd + bℓ+ mkℓ),
so ac ≡bd mod m.
□
Example 3.3. Check 11 ≡5 mod 6, −2 ≡4 mod 6, and 11 · (−2) ≡5 · 4 mod 6.
Example 3.4. What is the standard representative for 172 mod 19? You could compute
172 = 289 and then divide 289 by 19 to ﬁnd a remainder of 4, so 172 ≡4 mod 19. Another
way is to notice 17 ≡−2 mod 19, so 172 ≡(−2)2 ≡4 mod 19. That was quicker, and it
illustrates the meaning of multiplication being independent of the choice of representative.
Sometimes one representative can be more convenient than another.
Example 3.5. If we want to compute 104 mod 19, compute successive powers of 10 but
reduce modulo 19 each time the answer exceeds 19: using the formula 10k = 10 · 10k−1 and
writing ≡for congruence modulo 19,
101 = 10, 102 = 100 ≡5, 103 ≡10 · 5 = 50 ≡12, 104 ≡10 · 12 = 120 ≡6.
Thus 104 ≡6 mod 19. Theorem 3.2 says this kind of procedure leads to the right answer,
since multiplication modulo 19 is independent of the choice of representatives, so we can
always replace a larger integer with a smaller representative of it modulo 19 without aﬀecting
the results of (further) algebraic operations modulo 19.
Corollary 3.6. If a ≡b mod m and k ∈Z+ then ak ≡bk mod m.

<!-- page 4 -->
4
KEITH CONRAD
Proof. This follows from the second congruence in Theorem 3.2 using induction on k. Details
are left to the reader.
□
Remark 3.7. Do not try to extend Corollary 3.6 to fractional exponents until you have
much more experience in modular arithmetic. Extracting roots is not repeated multiplica-
tion, and extracting roots in modular arithmetic could be undeﬁned or have unexpected
behavior compared with your experience extracting roots in R.
For example, in R all positive numbers are perfect squares, but x2 ≡2 mod 5 has no
solution (that is, no integer x satisﬁes that congruence). Positivity is really a meaningless
concept mod m: every integer is congruent to a positive integer and a negative integer mod
m (just add and subtract a suitably large multiple of m to the integer). There is no good
notion of ordering mod m.
In R you know x2 = y2 ⇒x = ±y, but it is false that a2 ≡b2 mod m ⇒a ≡±b mod m
in general. Consider 42 ≡12 mod 15 with 4 ̸≡±1 mod 15.
In R you are used to x3 = y3 ⇒x = y. But 23 ≡13 mod 7 and 2 ̸≡1 mod 7.
When we add and multiply modulo m, we are carrying out modular arithmetic.
Theorem 3.8. If ax ≡ay mod m and (a, m) = 1 then x ≡y mod m.
Proof. We are told that m | (ax −ay), so m | a(x −y).
Since also (a, m) = 1, by a
consequence of Bezout’s identity m | (x −y), so x ≡y mod m.
□
Example 3.9. The following interpretation of Theorem 3.8 was pointed out to me by
Nathaniel Harris. The table of integers below has rows listing 14 consecutive numbers at
a time. In each column, the multiples of 3 (in red) are 3 rows apart, the multiples of 5 (in
orange) are 5 rows apart, and the multiples of 9 (in blue) are 9 rows apart. Why is this?
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
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
The pattern is due to 3, 5, and 9 being relatively prime to 14: if (a, 14) = 1 and ax and
ay are in the same column, then ax ≡ay mod 14, so x ≡y mod 14 by Theorem 3.8. Thus
x and y diﬀer by a multiple of 14, so the ﬁrst multiple of a after ax in the same column as
ax is a(x + 14) = ax + 14a: that’s a rows after ax. For a = 2, a = 4, and a = 7, all not
relatively prime to 14, the nearest multiples of a in a column are less than a rows apart.
That addition and multiplication can be carried out on integers modulo m without having
the answer change (modulo m) if we replace an integer by a congruent integer is similar
to other computations in mathematics. In elementary school, you learned that addition
and multiplication of fractions is independent of the particular choice of numerator and
denominator for the fractions, e.g., 1/2 + 3/5 = 11/10 and 2/4 + 9/15 = 66/60 = 11/10.

<!-- page 5 -->
MODULAR ARITHMETIC
5
In calculus, the formula
R b
a f(x) dx = F(b) −F(a) for deﬁnite integrals is independent of
the choice of antiderivative F(x) for f(x): any two antiderivatives for f(x) on [a, b] diﬀer
by a constant, so the diﬀerence F(b) −F(a) doesn’t change if we change F(x) to another
antiderivative of f(x): (F(b) + C) −(F(a) + C) = F(b) −F(a).
Deﬁnition 3.10. The integers mod m under addition and multiplication is denoted Z/(m).
Other notations you may meet for Z/(m) are Zm and Z/mZ.
Example 3.11. Here are the elements of Z/(5):
{. . . , −15, −10, −5, 0, 5, 10, 15, . . . },
{. . . , −14, −9, −4, 1, 6, 11, 16, . . . },
{. . . , −13, −8, −3, 2, 7, 12, 17, . . . },
{. . . , −12, −7, −2, 3, 8, 13, 18, . . . },
{. . . , −11, −6, −1, 4, 9, 14, 19, . . . }.
These ﬁve sets consist of integers congruent to each other mod 5 and are called congruence
classes mod 5. A representative from each congruence class usually stands for the whole
congruence class. In bold type is a set of representatives for the congruence classes mod 5:
0, 1, 2, 3, and 4. That is the standard choice. Another set of representatives is 5, 6, −3,
18, and −6 (since 5 ≡0 mod 5, 6 ≡1 mod 5, −3 ≡2 mod 5, and so on).
Integers in the same congruence class are like real numbers representing the same angle,
such as π and 3π.
They’re diﬀerent ways of representing the “same thing”.
Just as π
and 3π are not the same in R but become “the same” in as angles, think that way about
congruence classes: 1 and 6 are not the same in Z but they are the same modulo 5.
4. First application: Divisibility tests
A basic application of modular arithmetic is the explanation of divisibility tests in terms
of digits. We will look at three such tests. They describe when a positive integer n is
divisible by certain numbers in terms of its base 10 expansion
(4.1)
n = ck10k + ck−110k−1 + · · · + c1 · 10 + c0,
where 0 ≤ci ≤9. For example, n = 7405 has c3 = 7, c2 = 4, c1 = 0, and c0 = 5.
Theorem 4.1. The number n is divisible by 3 if and only if the sum of its digits Pk
i=0 ci
is divisible by 3.
Proof. To say n is divisible by 3 is the same as saying n ≡0 mod 3. Thus, we will show
n ≡0 mod 3 if and only if Pk
i=0 ci ≡0 mod 3.
The key point is this: 10 ≡1 mod 3.
Multiplying both sides of this congruence by
themselves, 102 ≡12 mod 3, so 102 ≡1 mod 3. In the same way, 10i ≡1 mod 3 for all i ≥0
by induction. Then
ck10k + ck−110k−1 + · · · + c1 · 10 + c0 ≡ck + ck−1 + · · · + c1 + c0 mod 3
since each 10i can be replaced with 1 when we work mod 3. Since 3 | n if and only if
n ≡0 mod 3, which is equivalent to Pk
i=0 ci ≡0 mod 3, n being divisible by 3 is equivalent
to the sum of the digits of n being divisible by 3.
□
Example 4.2. Let n = 84435. The sum of the digits is 8 + 4 + 4 + 3 + 5 = 24, which is
divisible by 3, so 84435 is divisible by 3. Indeed, 84435 = 3 · 28145.

<!-- page 6 -->
6
KEITH CONRAD
Theorem 4.3. The number n is divisible by 9 if and only if the sum of its digits Pk
i=0 ci
is divisible by 9.
Proof. The only important property of 3 in the proof of Theorem 4.1 was the condition
10 ≡1 mod 3. Since 10 ≡1 mod 9 too, we get the same test for divisibility by 9 as we did
for divisibility by 3, with the same proof.
□
Example 4.4. Again taking n = 84435, the sum of the digits is 24, which is not divisible
by 9, so n is not divisible by 9 either. In fact, 84435 leaves a remainder of 6 when divided
by 9: 84435 = 9 · 9381 + 6.
Theorem 4.5. The number n is divisible by 11 if and only if the alternating sum of its
digits Pk
i=0(−1)ici is divisible by 11.
Proof. We know n is divisible by 11 if and only if n ≡0 mod 11. Write n as in (4.1). Since
10 ≡−1 mod 11, we can rewrite the base 10 expansion of n, viewed modulo 11, as
n ≡ck(−1)k + ck−1(−1)k−1 + · · · + c1(−1) + c0 mod 11.
This is the alternating sum of the digits, so n ≡0 mod 11 if and only if the alternating sum
of the digits is ≡0 mod 11, which means the alternating sum is divisible by 11.
□
Example 4.6. If n = 84d35, which digit d permits 11 | n? We need 8 −4 + d −3 + 5 ≡
0 mod 11, or equivalently 6 + d ≡0 mod 11. Then d ≡5 mod 11, so we need d = 5 since d
is a decimal digit. Thus 84535 is a multiple of 11. As an explicit check, 84535 = 11 · 7685.
5. Solving equations in Z/(m)
In school you learned how to solve polynomial equations like 2x+3 = 8 or x2 −3x+1 = 0
by the “rules of algebra”: cancellation (if a ̸= 0 and ax = ay then x = y), equals plus equals
are equal, and so on. When there is no simple formula for a solution, you might graph the
equation and estimate solutions numerically. This is in the setting of the real numbers.
We can also try to solve polynomial equations in modular arithmetic, counting solutions
as diﬀerent if they are incongruent to each other. We will focus on the simplest case of a
linear congruence ax ≡b mod m. Already in this case we will meet some phenomena with
no parallel in the case of a real linear equation (Examples 5.2 and 5.3 below).
Example 5.1. Let’s try to solve 8x ≡1 mod 11. If there is an answer, it can be represented
by one of 0, 1, 2, . . . , 10, so let’s run through the possibilities:
x mod 11
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
8x mod 11
0
8
5
2
10
7
4
1
9
6
3
The only solution is 7 mod 11: 8 · 7 = 56 ≡1 mod 11.
That problem concerned ﬁnding an inverse for 8 modulo 11. We can ﬁnd multiplicative
inverses for every nonzero element of Z/(11):
x
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
x−1
1
6
4
3
9
2
8
7
5
10
Check in each case that the product of the numbers in each column is 1 in Z/(11).
Example 5.2. Find a solution to 8x ≡1 mod 10. We run through the standard represen-
tatives for Z/(10), and ﬁnd no answer:
x
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
8x
0
8
6
4
2
0
8
6
4
2

<!-- page 7 -->
MODULAR ARITHMETIC
7
In retrospect, we can see a priori why there shouldn’t be an answer. If 8x ≡1 mod 10 for
some integer x, then we can lift the congruence up to Z in the form
8x + 10y = 1
for some y ∈Z. But this is absurd: 8x and 10y are even, so the left side is a multiple of 2
but the right side is not.
Example 5.3. The linear congruence 6x + 1 ≡4 mod 15 has three solutions!
In the
following table we can see the solutions are 3, 8, and 13:
x
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
11
12
13
14
6x + 1
1
7
13
4
10
1
7
13
4
10
1
7
13
4
10
These examples show us that a linear congruence ax ≡b mod m doesn’t have to behave
like real linear equations: there may be no solutions or more than one solution. In particular,
taking b = 1, we can’t always ﬁnd a multiplicative inverse for each nonzero element of Z/(m).
The obstruction to inverting 8 in Z/(10) can be extended to other moduli as follows.
Theorem 5.4. For integers a and m, the following three conditions are equivalent:
• there is a solution x in Z to ax ≡1 mod m,
• there are solutions x and y in Z to ax + my = 1,
• a and m are relatively prime.
Proof. Suppose ax ≡1 mod m for some x ∈Z. Then m | (1 −ax), so there is some y ∈Z
such that my = 1 −ax, so
ax + my = 1.
This equation implies a and m are relatively prime since any common factor of a and m
divides ax + my.
Finally, if a and m are relatively prime then by Bezout’s identity (a
consequence of back-substituting in Euclid’s algorithm) we can write ax + my = 1 for some
x and y in Z and reducing both sides mod m implies ax ≡1 mod m.
□
This explains Example 5.2, since 8 and 10 have a common factor of 2. Similarly, there is
no solution to 3x ≡1 mod 15 (common factor 3) or 35x ≡1 mod 77 (common factor 7).
Example 5.5. Since (8, 11) = 1, 8 has a multiplicative inverse in Z/(11). We found it by
an exhaustive search in Example 5.1, but now we can do it by a more systematic approach:
Euclid’s algorithm
11 = 8 · 1 + 3
8 = 3 · 2 + 2
3 = 2 · 1 + 1
Backwards substitution
1 = 3 −2
= 3 −(8 −3 · 2)
= 3 · 3 −8
= 3 · (11 −8) −8
= 3 · 11 −8 · 4
Reducing the equation 1 = 3 · 11 −8 · 4 modulo 11,
8(−4) ≡1 mod 11.
The inverse of 8 in Z/(11) is −4, or equivalently 7.

<!-- page 8 -->
8
KEITH CONRAD
To summarize: solving for x in the congruence ax ≡1 mod m is equivalent to solving
for integers x and y in the equation ax + my = 1 (be sure you see why!), and the latter
equation can be solved without any guesswork by reversing Euclid’s algorithm on a and m
when (a, m) = 1. If Euclid’s algorithm shows (a, m) ̸= 1, then there is no solution.
In the real numbers, every nonzero number has a multiplicative inverse.
This is not
generally true in modular arithmetic: if a ̸≡0 mod m it need not follow that we can solve
ax ≡1 mod m. (For instance, 4 ̸≡0 mod 6 and 4 mod 6 has no multiplicative inverse.)
The correct test for invertibility in Z/(m) is (a, m) = 1, which is generally stronger than
a ̸≡0 mod m. Although invertibility in Z/(m) is usually not the same as being nonzero in
Z/(m), there is an important case when these two ideas agree: m is prime.
Corollary 5.6. For prime p, an integer a is invertible in Z/(p) if and only if a ̸≡0 mod p.
Proof. If a mod p is invertible, then (a, p) = 1, so p does not divide a.
For the converse direction, suppose a ̸≡0 mod p. We show (a, p) = 1. Since (a, p) is a
(positive) factor of p, and p is prime, (a, p) is either 1 or p. (The proof would break down
here if p were not prime.) Since p does not divide a, (a, p) ̸= p, so (a, p) = 1. Therefore the
congruence ax ≡1 mod p has a solution.
□
The upshot of Corollary 5.6 is that our intuition from algebra over R carries over quite
well to algebra over Z/(p): every nonzero number has a multiplicative inverse in the system.
But Z/(m) for composite m is more delicate.
Why do we want to invert integers in Z/(m)? (By “inverting” we always mean “inverting
multiplicatively.”) One reason is its connection to inverting matrices with entries in Z/(m).
Your experience with linear algebra in R may suggest a square matrix with entries in Z/(m)
is invertible whenever its determinant is nonzero in Z/(m), but that is false.
Example 5.7. We work with matrices having entries in Z/(10).
Let A = ( 1 3
1 1 ).
The
determinant of A is −2 ≡8 mod 10, so det A ̸≡0 mod 10. However, there is no inverse for
A as a mod 10 matrix. We can see why by contradiction. Suppose there is an inverse matrix,
and call it B. Then AB ≡( 1 0
0 1 ) mod 10. (Congruence of matrices means congruence of
corresponding matrix entries on both sides.) Writing B = ( x y
z t ), we compute AB to get
( x+3z y+3t
x+z
y+t ) ≡( 1 0
0 1 ) mod 10. Then x + 3z ≡1 mod 10 and x + z ≡0 mod 10. The second
congruence says x ≡−z mod 10, and replacing x with −z in the ﬁrst congruence yields
2z ≡1 mod 10. But that’s absurd: 2z is even and 1 is odd, so 2z ̸≡1 mod 10. (Said
diﬀerently, if 2z ≡1 mod 10 then 2z = 1 + 10y for some integer y, so 2z −10y = 1, but the
left side is even and 1 is not even.)
As a real matrix, A is invertible and A−1 = ( −1/2
3/2
1/2 −1/2 ). This inverse makes no sense if
we try to reduce it modulo 10 (what is 1/2 mod 10?!?), and that suggests there should be
a problem if we try to invert A as a mod 10 matrix.
Let’s look at determinants in modular arithmetic. Suppose n × n matrices A and B
satisfy AB ≡In mod m. Taking determinants of both sides tells us (by Theorem 3.2) that
(det A)(det B) ≡1 mod m,
so det A is invertible in Z/(m). Invertibility of det A in Z/(m) is usually stronger than
det A ̸≡0 mod m.
For instance, the 2 × 2 matrix A in Example 5.7 has determinant
8 mod 10, which is not invertible. Thus A is not invertible mod 10. That is an easier way
to see A is not invertible than the calculations in Example 5.7!

<!-- page 9 -->
MODULAR ARITHMETIC
9
Example 5.8. Let m = 14 and A = ( 1 4
3 2 ) as a matrix with entries in Z/(14).
The
determinant of A is 2 −12 = −10 ≡4 mod 14, which is not invertible. Even though A has
a nonzero determinant, there is no matrix inverse for A over Z/(14).
We now see that we have to be able to recognize invertible elements of Z/(m) before
we can recognize invertible matrices over Z/(m), because an invertible matrix will have an
invertible determinant. If we want to do linear algebra over Z/(m) then we need Euclid’s
algorithm (and Bezout’s identity) to invert determinants.
6. Block ciphers
This last section gives a cryptographic application of linear algebra over Z/(m).
In
cryptography, we are interested in various methods of encoding and decoding text.
The simplest idea, going back to Julius Caesar, is called a shift cipher. Simply pick an
integer c and encode a letter by replacing it with the letter c places further along in the
alphabet (wrap around to the start of the alphabet from the end if necessary). For instance,
if we shift by 3, then we have
A 7→D, B 7→E, C 7→F, . . . , Z 7→C.
The message
DOODLE
is encoded as
GRRGOH.
The encoded message
XKFJXI
is decoded by shifting back by 3 letters to
ANIMAL.
The Caesar cipher has two critical ﬂaws. First of all, since there are only 26 shifts, an
adversary (who knows or suspects that the message was encoded with the Caesar cipher)
can simply decode the message with each of the 26 possible shifts until a meaningful de-
cryption is found. The second problem, which is illustrated in the examples above, is that
a letter gets encoded to the same letter every time. A cipher with this feature (called a
simple substitution cipher, whether or not the substitutions come from a cyclic shift of the
alphabet) is easily cracked by taking into account the frequency of letters in ordinary Eng-
lish text. For instance, the most common letter in ordinary English text is E, so the most
common letter in a text (of reasonable length) encoded by a simple substitution cipher is
probably the encrypted form of the letter E.
Before moving on to other cryptographic methods, we describe the Casesar cipher using
modular arithmetic. Identify the letters of the alphabet with two-digit strings:
(6.1)
A = 01, B = 02, . . . , Z = 26.
View the letters as elements of Z/(26).
The shift by 3, say, is the encryption function
E(x) ≡x + 3 mod 26. It is decrypted with D(y) ≡y −3 mod 26.
We can get something a bit more mathematically interesting than a shift cipher by
allowing scaling before translating: E(x) = ax + b, where (a, 26) = 1. A plain shift has
a = 1. Suppose a = 5 and b = 3. Then E(x) ≡5x+3 mod 26, so letting x = 1, 2, 3, . . . , 25, 0
gives the encoding
A 7→H, B 7→M, . . . , Z 7→C.

<!-- page 10 -->
10
KEITH CONRAD
The decryption is based on inverting a linear function: If y = 5x+3, then x = (1/5)(y −3).
In Z/(26), the inverse of 5 is 21 (check!), so the decryption function is D(y) = 21(y −3) =
21y + 15 (because 12(−3) = −36 ≡15 mod 26).
Using E(x) = 5x + 3 on Z/(26), check the encrypted version of DOODLE is now
WZZWKB.
While the introduction of the scaling before we shift enlarges the number of possible ciphers,
we are still encoding one letter at a time, and each letter gets encoded in the same way no
matter where it appears in the text, so a frequency analysis on a moderate amount of text
would let us determine the scaling and shift parameters.
We now use linear algebra over Z/(26) to encode blocks of text. This is called a block
cipher. We will describe the idea using two-letter blocks. For instance,
DOODLE
becomes
DO
OD
LE.
Each block can be viewed as a column vector over Z/(26):
D
O

=
 4
15

,
O
D

=
15
4

,
L
E

=
12
5

.
Pick a 2 × 2 matrix over Z/(26). For concreteness, take
A =

3
2
1
11

.
Our encoding algorithm will be the product of A with each vector, calculations being made
modulo 26:
A
 4
15

=
16
13

,
A
15
4

=
1
7

,
A
12
5

=
20
15

.
Turning each coordinate back into a letter, the encoded form of DOODLE is
PMAGTO.
Notice that the two D’s in DOODLE, as well as the two O’s, have been encoded by dif-
ferent letters. (Why did this happen?) Clearly this is a desirable feature from a security
standpoint.
Suppose we received the message
UPFOOU
and we know it was encoded by multiplication by the above matrix A = ( 3 2
1 11 ). Since
encoding is E(v) = Av, decoding is achieved by multiplication by the inverse of A: D(v) =
A−1v. When is a 2 × 2 matrix invertible? In a ﬁrst linear algebra course you learn that
a (square) matrix with real entries is invertible precisely when its determinant is nonzero,
and in the 2 × 2 case ( a b
c d ) has inverse
1
ad −bc

d
−b
−c
a

.
For matrices with entries in Z/(m), the rule for invertibility of a matrix is not that the
determinant is nonzero. For example, taking m = 26, the matrix ( 1 2
3 4 ) has determinant
−2 ≡24 mod 26, which is not 0 mod 26, but this matrix is not invertible mod 26: for no
2 × 2 matrix M is ( 1 2
3 4 )M ≡( 1 0
0 1 ) mod 26.

<!-- page 11 -->
MODULAR ARITHMETIC
11
Theorem 6.1. A 2 × 2 matrix with entries in Z/(m) has an inverse precisely when its
determinant is invertible in Z/(m), in which case its inverse is given by the same formula
as in the real case.
Proof. Let A be the matrix. If A has an inverse matrix B, so AB ≡( 1 0
0 1 ) mod m, then
taking determinants of both sides implies (det A)(det B) ≡1 mod m. Therefore det A is
invertible in Z/(m). Conversely, if det A is invertible in Z/(m) then the familiar inverse
matrix formula from (real) linear algebra actually makes sense if we apply it to the mod m
matrix A and a direct calculation shows the formula works as an inverse.
□
The matrix A = ( 3 2
1 11 ) over Z/(26) has determinant 31 ≡5 mod 26. The inverse of this
determinant (in Z/(26)) is 21. Therefore
A−1 = 21

11
−2
−1
3

≡

23
10
5
11

.
Call this matrix B. (Check AB = I2 and BA = I2.) The endoded message UPFOOU has
blocks
U
P

=
21
16

,
F
O

=
 6
15

,
O
U

=
15
21

,
so we decode by multiplying each vector by B on the left:
B
21
16

=
19
21

,
B
 6
15

=
 2
13

,
B
15
21

=
 9
20

.
Putting the output blocks back together and converting them into letters gives the decoded
message:
SUBMIT.
Of course, 2-block ciphers can be cracked using a frequency analysis on pairs of letters
rather than on individual letters. (As an example, Q is almost always followed by U in Eng-
lish.) The idea of a 2-block cipher extends to blocks of greater length using larger matrices.
A diﬃculty with a block cipher is that knowledge of the encryption and decryption matri-
ces are essentially equivalent: anyone who discovers the encryption matrix can compute its
inverse (the decryption matrix) using row reduction or other methods of computing matrix
inverses. This means the encryption matrix must be kept secret from your enemies. Until
the 1970s, everyone (outside US and British intelligence) thought encryption and decryp-
tion had to be more or less symmetric processes. But this is false: there are cryptographic
algorithms where the encryption process can be made public to the world and decryption
is still secure. Number theory is a source of such algorithms used in e-commerce, ATM
transactions, cell phone communications, etc.
We end with some exercises.
1. Explain why the matrix

5
3
7
1

can’t be used in a 2-block cipher. (Hint: Try to invert the matrix over Z/(26).)
2. Messages are encoded in blocks of length 2 using

4
1
1
3

You receive the encrypted message

<!-- page 12 -->
12
KEITH CONRAD
AAOGIXZC.
What is the original message, in plain English?

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*