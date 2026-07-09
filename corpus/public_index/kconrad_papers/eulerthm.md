# Euler's Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/eulerthm.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
EULER’S THEOREM
KEITH CONRAD
1. Introduction
Fermat’s little theorem is an important property of integers to a prime modulus.
Theorem 1.1 (Fermat). For prime p and any a ∈Z such that a ̸≡0 mod p,
ap−1 ≡1 mod p.
For a composite modulus m, it is not generally true that if a ̸≡0 mod m, then am−1 ≡
1 mod m. Try m = 15 and a = 2: 214 ≡4 ̸≡1 mod 15. A correct extension of Fermat’s
little theorem to non-prime moduli requires a new way of thinking about the hypothesis in
Fermat’s little theorem. For prime p,
a ̸≡0 mod p ⇐⇒(a, p) = 1,
but these two conditions are not equivalent when p is replaced with a composite number.
It is the relative primality point of view on the right that lets Fermat’s little theorem be
extended to a general modulus, as Euler discovered.
Theorem 1.2 (Euler). For m ≥2 in Z+ and any a ∈Z such that (a, m) = 1,
aϕ(m) ≡1 mod m,
where ϕ(m) is the number of invertible integers modulo m.
When m = p is prime, all non-zero integers modulo p are invertible, so ϕ(p) = p −1 and
Euler’s theorem becomes Fermat’s little theorem.1
How do we compute ϕ(m)? Consider m = 12. To count the number of invertible integers
modulo 12, write down a set of representatives for integers modulo 12, such as
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12.
The numbers here that are invertible modulo 12 are 1, 5, 7, 11, so ϕ(12) = 4. Euler’s theorem
for m = 12 says a4 ≡1 mod 12 when (a, 12) = 1.
Being invertible modulo m is the same as being relatively prime to m (that is, we can
solve ax ≡1 mod m for x exactly when (a, m) = 1), so we can describe ϕ(m) concretely as
(1.1)
ϕ(m) = |{a : 1 ≤a ≤m, (a, m) = 1}|.
For example, ϕ(10) = |{1, 3, 7, 9}| = 4. Here is a small table of values derived from (1.1).2
m
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
ϕ(m)
1
2
2
4
2
6
4
6
4
10
4
12
6
8
8
16
1In 1914, Carmichael [1, pp. 47–48] called Euler’s theorem “Fermat’s general theorem” and he called
Fermat’s little theorem the “simple Fermat theorem”. These labels are now obsolete.
2The formula (1.1) is how ϕ(m) was ﬁrst deﬁned by Euler [3, §3]. He wrote πm instead of ϕ(m), e.g.,
π10 = 4. Euler used < m in (1.1) instead of ≤m, whose only eﬀect is to make π1 = 0 while ϕ(1) = 1. For
m > 1, πm = ϕ(m). The notation ϕ and the use of ≤m in (1.1) is due to Gauss [5, art. 39].
1

<!-- page 2 -->
2
KEITH CONRAD
It seems ϕ(m) is even for m > 2. To prove this, observe that when a mod m is invertible,
so is −a mod m. So using standard representatives modulo m, invertible numbers modulo
m come in pairs as {a, m −a}. This is a pair of diﬀerent numbers mod m, since if a ≡
m −a mod m for 0 < a < m then a = m −a (why?) so a = m/2 and m is even. But
(m/2, m) = m/2, and m/2 > 1 when m > 2, so m/2 mod m is not invertible. Thus, if
m > 2 the invertible numbers modulo m come in pairs {a, m −a mod m}, so ϕ(m) is even.3
2. From Fermat to Euler
Euler’s theorem has a proof that is quite similar to the proof of Fermat’s little theorem.
To stress the similarity, we review the proof of Fermat’s little theorem and then we will
make a couple of changes in that proof to get Euler’s theorem.
Here is a proof of Fermat’s little theorem (Theorem 1.1).
Proof. We have a prime p and an arbitrary a ̸≡0 mod p. To show ap−1 ≡1 mod p, consider
non-zero integers modulo p in the standard range:
S = {1, 2, 3, . . . , p −1}.
We will compare S with the set obtained by multiplying the elements of S by a:
aS = {a, a · 2, a · 3, . . . , a(p −1)}.
Elements of S represent the nonzero numbers mod p. We will show the elements of aS
also represent the nonzero numbers mod p: each nonzero number mod p is congruent to
exactly one number in aS.
When k ∈S we have ak ̸≡0 mod p since p ∤a and p ∤k
implies p ∤ak due to p being prime. Two diﬀerent elements of aS can’t represent the same
number mod p since ax ≡ay mod p =⇒x ≡y mod p due to a mod p being invertible and
x ≡y mod p ⇒x = y when 1 ≤x, y ≤p −1. Thus aS is p −1 numbers that reduce mod
p to p −1 diﬀerent nonzero numbers mod p, so aS reduces mod p to {1, . . . , p −1 mod p}
just as S does.
Since S and aS become the same thing when reduced modulo p, the product of the
numbers in each set must be the same modulo p:
1 · 2 · 3 · · · · · (p −1) ≡a(a · 2)(a · 3) · · · (a(p −1)) mod p.
Pulling the p −1 copies of a to the front of the product on the right, we get
1 · 2 · 3 · · · · · (p −1) ≡ap−1(1 · 2 · 3 · · · · · (p −1)) mod p.
Now cancel each of 1, 2, 3, . . . , p −1 on both sides (they are all invertible modulo p) and we
are left with 1 ≡ap−1 mod p.
□
Euler’s theorem can be proved in a pretty similar way to this by replacing the condition
“non-zero modulo p” with “relatively prime to m.”
Proof. We have a positive integer m and an a such that (a, m) = 1. To show aϕ(m) ≡
1 mod m, consider the units modulo m in the standard range:
S = {u1, u2, u3, . . . , uϕ(m)},
where 1 ≤ui ≤m −1, (ui, m) = 1, and the ui’s are distinct. (If m = p is prime we can use
ui = i for all i, but in general there isn’t a simple formula for the ith unit modulo m.)
3Not every even number is ϕ(m) for some m. For example, there is no m for which ϕ(m) is 14 or 26. A
longer list of even numbers that are not some ϕ(m) values is at https://oeis.org/A005277.

<!-- page 3 -->
EULER’S THEOREM
3
We will compare S with the set obtained by multiplying the elements of S by a:
aS = {au1, au2, au3, . . . , auϕ(m)}.
Since (a, m) = 1, a mod m is a unit and therefore aS consists of units modulo m. We will
show that aS represents all the units modulo m. Given any unit b mod m, the congruence
ax ≡b mod m is solvable since a mod m is invertible. The solution x is a unit modulo m
(why?), and placing x between 1 and m −1 makes ax a member of aS. Thus b mod m is
represented by an element of aS. If ax ≡ay mod m then x ≡y mod m since a mod m is
invertible, so the diﬀerent elements of S remain diﬀerent mod m after being multiplied by
a. Therefore aS is a set of representatives for the units modulo m (no duplicates).
Since the members of S and aS agree mod m, the products in each set agree mod m:
u1u2u3 · · · uϕ(m) ≡(au1)(au2)(au3) · · · (auϕ(m)) mod m.
Pulling the ϕ(m) copies of a to the front of the product on the right, we get
u1u2u3 · · · uϕ(m) ≡aϕ(m)u1u2u3 · · · uϕ(m) mod m.
Cancel ui on both sides (each ui is invertible mod m) and we get 1 ≡aϕ(m) mod m.4
□
Passing from Fermat’s little theorem to Euler’s theorem amounts to replacing non-zero
numbers modulo a prime p with invertible numbers (not non-zero numbers) for a general
modulus m. A common notation for such numbers in elementary number theory courses is5
Um = {a mod m : (a, m) = 1}.
The notation Um comes the fact that invertible numbers mod m are called units mod m.
Example 2.1. We have U5 = {1, 2, 3, 4} and U18 = {1, 5, 7, 11, 13, 17}.
When p is prime, Up = {1, 2, 3, . . . , p −1}. As a check that you understand this new
notation, be sure you understand why ϕ(m) = |Um|.
3. Computing ϕ(m) in special cases
The function ϕ(m) does not vary in a simple way from one integer to the next. See the
table near the end of Section 1. This is typical of functions in number theory that are based
on divisibility (or lack thereof). The right way to think about ϕ(m) is by thinking about
positive integers not using the m →m + 1 paradigm, but in terms of the progression
primes →prime powers →general case.
This progression is how the integers are best arranged from the viewpoint of divisibility:
primes are the building blocks for multiplication (rather than 1 being the building block for
addition), then come prime powers, and ﬁnally we get any positive integer as a product of
prime powers. With this in mind, we can get formulas for ϕ(m) directly from its deﬁnition
in the ﬁrst two cases of the above progression:
• ϕ(p) = p −1 since there are p −1 integers from 1 to p that are relatively prime to p.
• ϕ(pk) = pk−pk−1 = pk−1(p−1) for prime p and k ≥1 since among the integers from 1
to pk, those that are not relatively prime to pk are the multiples of p: p, 2p, 3p, . . . , pk.
There are pk−1 such numbers. Subtract this from pk to get ϕ(pk) = pk −pk−1.
4Euler’s own proof of his theorem [2, Theorems 7–11], [4, §195–213] diﬀers from the one presented above.
5Many mathematicians write (Z/(m))× for Um.

<!-- page 4 -->
4
KEITH CONRAD
Make sure you remember this explanation for why ϕ(pk) = pk −pk−1. (Warning: this
formula is false when p is not prime: ϕ(ak) < ak −ak−1 when a is composite and k ≥1.)
What about ϕ(m) when m has more than one prime factor? We will treat one case
here, which is important in elementary cryptography: m = pq is a product of two diﬀerent
primes. If 1 ≤a ≤pq and (a, pq) = 1, then a is neither a multiple of p nor a multiple of
q. The multiples of p in this range are p, 2p, . . . , qp and the multiples of q in this range are
q, 2q, . . . , pq. There are q numbers in the ﬁrst case and p numbers in the second case. The
two lists only overlap at pq (indeed, a positive integer divisible by p and q is divisible by pq,
so can’t be less than pq). Therefore, to compute ϕ(pq), we take away from pq the number
of terms in both lists without double-counting the common term:
ϕ(pq) = pq −p −q + 1 = p(q −1) −(q −1) = (p −1)(q −1).
This is interesting: ϕ(pq) = ϕ(p)ϕ(q) for diﬀerent primes p and q. (Warning: this formula
is false when p = q: ϕ(p2) = p2 −p = p(p −1) while ϕ(p)ϕ(p) = (p −1)2.)
With these formulas, we can make Euler’s theorem more explicit for certain moduli.
Example 3.1. When p is prime,
(a, p2) = 1 =⇒ap(p−1) ≡1 mod p2.
Example 3.2. When p and q are diﬀerent primes,
(a, pq) = 1 =⇒a(p−1)(q−1) ≡1 mod pq.
This example with modulus pq is related to the RSA cryptosystem.
4. Application: Periodic Decimal Expansions
With a calculator we can see that various fractions have periodic decimal expansions,
e.g., 3/7 = .428571428571 . . . has a repeating block of length 6.
Which numbers have
periodic expansions?
And is anything predictable about the period length?
To answer
these questions, we start by working in reverse. Let’s write down a periodic expansion and
try to see what kind of number it turns out to be. For simplicity, we focus on purely periodic
decimals, meaning those with a repeating block right at the start (like 3/7 above and unlike
19/55 = .345454545 . . . , which has the initial 3 that is not repeated).
If x = .c1c2. . .cd is a purely periodic decimal, where the periodic block we wrote down
has length d, each ci is repeated every d digits as we move through the decimal expansion
of x. For instance, c1 occurs in positions for 10−1, 10−(d+1), 10−(2d+1), and so on. The digit
c2 occurs in positions 10−2, 10−(d+2), 10−(2d+2), and so on.6 Therefore
x = c1
X
k≥0
1
10dk+1 + c2
X
k≥0
1
10dk+2 + · · · + cd
X
k≥0
1
10dk+d
=
 c1
10 + c2
102 + · · · + cd
10d
 X
k≥0
1
10dk
=
 c1
10 + c2
102 + · · · + cd
10d

1
1 −1/10d ,
6We don’t forbid the possibility that some of the ci’s are equal, e.g., .11111 . . . could be considered to
have repeating block “1” or repeating block “11.”

<!-- page 5 -->
EULER’S THEOREM
5
where we sum a geometric series in the last step. Write 1/(1 −1/10d) as 10d/(10d −1) and
use the 10d in the numerator to clear out powers of 10 in denominators of the other factor:
x = c110d−1 + c210d−2 + · · · + cd
10d −1
.
This is rational with denominator that is 1 less than a power of 10. The numerator can be
any positive integer with at most d decimal digits, so x is a fraction between 0 and 1.
Example 4.1. Let x = .33333 . . . . The repeating block has length 1, so from the calcula-
tions we made,
x =
3
10 −1 = 3
9 = 1
3.
Example 4.2. Let x = .002870028700287 . . . . The repeating block has length 5 (not 3;
include the periodic 0’s also), so
x =
287
105 −1 =
287
99999 =
7
2439.
In the last step, the greatest common divisor of 287 and 99999 is 41, so the numerator and
denominator are divided by 41.
We have shown that any number that has a purely periodic decimal expansion is rational
between 0 and 1 and admits an expression as a fraction whose denominator is 10d −1 for
some d. Now we want to go the other way: starting with a fraction, say 28/303, can we
decided if its decimal expansion is (purely) periodic or not?
The calculations above, passing from a purely periodic decimal for a number x to its
expression as a fraction with denominator 10d −1, can be read forwards and backwards.
Reading it in reverse shows that any fraction between 0 and 1 with a denominator of the
form 10d −1 has a purely periodic decimal expansion. So the numbers that have purely
periodic decimal expansions are precisely the fractions between 0 and 1 with a denominator
of the form 10d −1. Of course, a denominator having the form 10d −1 might not be the
reduced form denominator, e.g., 7/2439 from Example 4.2 has to be written as 287/99999
to get its denominator to be 1 less than a power of 10.
So we ask: is there a simple
description of the fractions that admit a representation (not necessarily reduced!) with a
denominator of the form 10d −1? Since 10d −1 is not divisible by 2 or 5, and the reduced
form denominator is a factor of any other denominator for the fraction, if a fraction has a
denominator 10d −1 then its reduced form denominator must be relatively prime to 10. It
turns out the converse is also true, and the key tool to prove this is Euler’s theorem:
Theorem 4.3. Any reduced form fraction a/b with (10, b) = 1 can be written as a fraction
with denominator 10d −1 for some d ≥1.
Moreover, the period length of the decimal
expansion for a/b is the smallest d ≥1 such that 10d ≡1 mod b. In particular, d ≤ϕ(b)
and the period length is independent of the numerator a.
Proof. Let the fraction be a/b, where (10, b) = 1. By Euler’s theorem, 10ϕ(b) ≡1 mod b.
That means 10ϕ(b)−1 is a multiple of b, so we can rewrite a/b as a fraction with denominator
10ϕ(b) −1.
Let d ≥1 be minimal such that 10d ≡1 mod b, so d ≤ϕ(b). Write 10d −1 = bn, so
a
b = an
bn =
an
10d −1,

<!-- page 6 -->
6
KEITH CONRAD
Since a/b < 1, we have an < bn = 10d −1. Therefore the base 10 expansion of an requires
no more than d digits, so we can write an = c110d−1 + c210d−2 + · · · + cd for some digits ci.
(Some of the top ci’s may be 0 if an is substantially less than 10d −1.)
Our earlier calculations showed that for any decimal digits c1, . . . , cd,
(4.1)
.c1c2 · · · cd = c110d−1 + c210d−2 + · · · + cd
10d −1
,
so a/b = (c110d−1 + · · · + cd)/(10d −1) has a periodic decimal expansion of length d.
To show d is the minimal period of the decimal expansion of a/b when d is the smallest
positive integer such that 10d ≡1 mod b, assume we could write a/b as a decimal expansion
with a repeating block of some length ℓ.
Then a/b can be written as a fraction with
denominator 10ℓ−1. Since a/b is the reduced form of the fraction, this means 10ℓ−1 is a
multiple of b, so 10ℓ≡1 mod b. Therefore ℓ≥d (why?), so d is the minimal period length
of the decimal expansion of a/b.
Since the least d such that 10d ≡1 mod b has nothing to do with a, we see that the
period length of a/b is independent of a (provided the fraction is written in reduced form,
i.e., (a, b) = 1).
□
Example 4.4. A numerical computation suggests the decimal expansions of 1/7, 2/7, 3/7,
4/7, 5/7, and 6/7 all have period length 6 and the decimal expansions of 1/303 and 28/303
both have period length 4. To prove this, check the least d such that 10d ≡1 mod 7 is 6
and the least d such that 10d ≡1 mod 303 is 4.
By seeing explicitly how 106 −1 is a multiple of 7 and 104 −1 is a multiple of 303, we
can even ﬁgure out (without a calculator) what the decimal expansions of these fractions
are. Since 106 −1 = 7 · 142857,
3
7 = 3 · 142857
7 · 143857 = 428571
106 −1 = .428571428571 . . . .
Since 104 −1 = 303 · 33,
28
303 = 28 · 33
303 · 33 =
924
104 −1 = .092409240924 . . . .
The whole theory of periodic decimals (e.g., determining which numbers have purely
periodic decimal expansions, and how long the periods can be) is explained by Euler’s
theorem and results related to it. So this is a concrete application of number theory to
explain a mystery from elementary school mathematics familiar to all students.
Remark 4.5. The requirement in Theorem 4.3 that a/b lie between 0 and 1 is a red herring.
This is best explained by an example. Consider 1543/303. To ﬁnd its decimal expansion,
ﬁrst extract the integer part. Since 1543 = 303 · 5 + 28, we have 1543/303 = 5 + 28/303. So
the decimal part of 1543/303 is the same as that of 28/303, and we can apply Theorem 4.3
to 28/303. Since 28/303 = .092409240924 . . . , we have 1543/303 = 5.092409240924 . . . .
In general, check that for any reduced form fraction a/b > 1, subtracting its integer part
leaves a fraction between 0 and 1 that still has b as its reduced form denominator, so the
period of the decimal expansion of a/b is still completely determined by b.
There are further interesting questions worth asking about decimal expansions:
(1) Which numbers have ﬁnite decimal expansions (such as 5/16 = .3125)?
(2) Which numbers have periodic decimal expansions with an initial nonrepeating block
(such as 7/15 = .466666 . . . )?

<!-- page 7 -->
EULER’S THEOREM
7
(3) If we compare all the reduced proper fractions with the same denominator b, some-
times they all have the same expansion as 1/b except for a digit shift, e.g.,
1/7 = .142857,
2/7 = .285714,
3/7 = .428571,
4/7 = .571428,
5/7 = .714285,
6/7 = .857142,
Can you explain when all the reduced fractions with denominator b have this feature?
(4) For some denominators, more than one digit sequence (up to shifting) occurs, e.g.,
there are two possibilities when the denominator is 13:
1/13 = .076923,
2/13 = .153846,
3/13 = .230769,
4/13 = .307692,
5/13 = .384615,
6/13 = .461538,
7/13 = .538461,
8/13 = .615384,
9/13 = .692307,
10/13 = .769230,
11/13 = .846153,
12/13 = .923076.
Each decimal expansion here is a cyclic shift of the expansion of 1/13 or 2/13.
The numerators of fractions above whose decimal expansions have the same digit
sequence up to a cyclic shift fall into two sets: {1, 3, 4, 9, 10, 12} and {2, 5, 6, 7, 8, 11}.
Is there a signiﬁcance to these two sets of numerators? More generally, among all
reduced fractions with a given denominator, can you predict which ones have decimal
digits that are cyclic shifts of each other?
Understanding decimal expansions for fractions would help “mechanize division” to save
time for astronomers and others who needed to do many computations. (Pocket calculators
only became available about 200 years later.) Papers by J. H. Lambert, J. Bernoulli, and
K. F. Hindenburg during the period 1760–1790 contained a mixture of rules and conjec-
tures about periodic decimals. They saw a connection between period lengths for prime
denominators and Fermat’s little theorem, for instance, but they oﬀered little explanation
of their observations. In 1793, the 16-year old Gauss came across these papers and a few
years later he settled nearly all basic questions in this area by a systematic use of modular
arithmetic7, putting his results in the sixth section of the Disquisitiones Arithmeticae.
5. Other Extensions of Fermat’s Little Theorem
Euler’s theorem is not the only generalization of Fermat’s little theorem to composite
moduli. To see another one, write the congruence in Fermat’s little theorem as
(5.1)
ap ≡a mod p.
For a ̸≡0 mod p, dividing by a shows this is the same as ap−1 ≡1 mod p, which is the usual
form of Fermat’s little theorem. The “advantage” of writing it as ap ≡a mod p is that now
the congruence holds for all a without exception. We will present here a few congruences
for composite moduli that each generalize (5.1) and work for all a without exception, unlike
Euler’s theorem.
7Two fractions a/b and a′/b with denominator b have the same decimal part if and only if a/b −a′/b
is an integer, which means a ≡a′ mod b. So the study of decimal expansions might be what led Gauss to
discover modular arithmetic in the ﬁrst place.

<!-- page 8 -->
8
KEITH CONRAD
First generalization. For all m ≥2 and all a ∈Z,
(5.2)
am ≡am−ϕ(m) mod m.
(The exponent m −ϕ(m) is positive since ϕ(m) ≤m −1 by the deﬁnition of ϕ(m).) When
m = p is prime, (5.2) says ap ≡ap−(p−1) ≡a mod p, which is (5.1). When m = pq is a
product of two diﬀerent primes, (5.2) says apq ≡ap+q−1 mod pq for all a ∈Z.
The congruence (5.2) for general m is true when (a, m) = 1 since am ≡am−ϕ(m)aϕ(m) ≡
am−ϕ(m) mod m by Euler’s theorem. To prove (5.2) for general a, it suﬃces to prove for
all prime powers pe dividing m (here e > 0) that am ≡am−ϕ(m) mod pe (taking for pe
the maximal powers of the prime factors of m, this congruence for each pe implies the
congruence mod m). We now take cases depending on whether or not p | a.
Case 1: p ∤a. In this case (a, pe) = 1, so aϕ(pe) ≡1 mod pe. The number ϕ(m) is divisible
by ϕ(pe), so aϕ(m) ≡1 mod pe and therefore am ≡am−ϕ(m)aϕ(m) ≡am−ϕ(m) mod pe.
Case 2: p | a. We will show pm−ϕ(m) ≡0 mod pe. Then am and am−ϕ(m) are both
0 mod pe since they are divisible by pm−ϕ(m), so they are congruent modulo pe.
When pe | m, ϕ(m) is divisible by ϕ(pe) = pe−1(p −1), so m and ϕ(m) are divisible by
pe−1. Therefore pm−ϕ(m) is a power of ppe−1, so we’d be done by showing pe−1 ≥e. The
smallest prime is 2, so pe−1 ≥2e−1, and 2e−1 ≥e for all e ≥1 by induction on e.
Second generalization. For all m ≥2 and all a ∈Z,
(5.3)
m−1
X
k=0
a(k,m) ≡0 mod m.
When m = p is prime, this becomes ap + (p −1)a ≡0 mod p, which is the same as
ap −a ≡0 mod p since the pa mod p term is 0 no matter what a is. So we have recovered
(5.1) as a special case. When m = pq with distinct primes p and q, (5.3) says
(5.4)
apq + (q −1)ap + (p −1)aq + (p −1)(q −1)a ≡0 mod pq.
for all a ∈Z. That’s quite diﬀerent from Euler’s congruence mod pq in Example 3.2.
In (5.3) the exponents are divisors of m, and collecting terms with the same exponent
yields
m−1
X
k=0
a(k,m) =
X
d|m
|{1 ≤k ≤m : (k, m) = d}|ad =
X
d|m
ϕ(m/d)ad,
where we leave it to the reader to show |{1 ≤k ≤m : (k, m) = d}| = ϕ(m/d) for each
(positive) divisor d of m. Thus (5.3) can be rewritten as
(5.5)
X
d|m
ϕ(m/d)ad ≡0 mod m
for all a ∈Z, and in the form (5.5) this congruence is due to MacMahon [8, p. 309] in the
1890s. A more recent account of (5.5), using group actions, is in [6, Theorem C].
Third generalization. Our last generalization of Fermat’s little theorem will use the
M¨obius function µ(n). This function on positive integers has values in {0, 1, −1} by the
following rules: µ(1) = 1, µ(p1 · · · pr) = (−1)r if the pi’s are distinct, and µ(n) = 0 if n has
a repeated prime factor. Here is a small table of values.
m
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
µ(m)
1
−1
−1
0
−1
1
−1
0
0
1
−1
0
−1
1
1
0

<!-- page 9 -->
EULER’S THEOREM
9
A generalization of Fermat’s little theorem involving the M¨obius function is that for all
m ≥2 and all a ∈Z,
(5.6)
X
d|m
µ(m/d)ad ≡0 mod m.
When m = p is prime this says ap −a ≡0 mod p, which is (5.1). When m = pq is a
product of distinct primes, this says apq −ap −aq +a ≡0 mod pq; the left side is not strictly
equal to the left side of (5.4), but they are congruent modulo pq since their diﬀerence is
q(ap −a) + p(aq −a) + pqa and each term here is a multiple of pq.
A proof of (5.6) can be found in [7] and [9]. A history of (5.6) and its extension to a
congruence using traces of integer matrices is in [10].
References
[1] R. D. Carmichael, “The Theory of Numbers,” J. Wiley & Sons, New York, 1914. URL https://archive.
org/details/theoryofnumbers00carmuoft/page/n5/mode/2up.
[2] L. Euler, Theoremata arithmetica nova methodo demonstrata, Novi Commentarii Academiae Scien-
tiarum Imperialis Petropolitanae 8 (1763), 74–104. URL https://scholarlycommons.pacific.edu/
euler-works/271/. German translation at https://arxiv.org/abs/1203.1993.
[3] L. Euler, Speculationes circa quasdam insignes proprietates numerorum, Acta Academiae Scientiarum
Imperialis Petropolitanae 4 (1784),
18–30. URL https://scholarlycommons.pacific.edu/euler-
works/564/. English translation at https://arxiv.org/abs/0705.3929v1.
[4] L. Euler, Tractatus de numerorum doctrina capita sedecim, quae supersunt, Commentationes Arithmeti-
cae 2 (1849), 503–575. URL https://scholarlycommons.pacific.edu/euler-works/792/.
[5] C. F. Gauss,“Disquisitiones Arithmeticae,” trans. by A. A. Clarke, Yale Univ. Press, New Haven, 1966.
[6] I. M. Isaacs and M. R. Pournaki, Generalizations of Fermat’s Little Theorem Using Group Theory, Amer.
Math. Monthly 112 (2005), 734–740.
[7] L. Levine, Fermat’s Little Theorem: A Proof by Function Iteration, Math. Mag. 72 (1999), 308–309.
[8] P. A. MacMahon, Applications of the Theory of Permutations in Circular Procession to the Theory of
Numbers, Proc. London Math. Soc. 23 (1891–2), 305–313.
[9] C. Smyth, A Coloring Proof of a Generalisation of Fermat’s Little Theorem, Amer. Math. Monthly 93
(1986), 469–471.
[10] H. Steinlein, Fermat’s Little Theorem and Gauss Congruence: Matrix Versions and Cyclic Permutations,
Amer. Math. Monthly 124 (2017), 548–553.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*