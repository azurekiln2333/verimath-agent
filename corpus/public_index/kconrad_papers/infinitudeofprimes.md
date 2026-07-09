# The Infinitude of the Primes

> **Source**: https://kconrad.math.uconn.edu/blurbs/infinitudeofprimes.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE INFINITUDE OF THE PRIMES
KEITH CONRAD
1. Introduction
The sequence of prime numbers
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, . . . , 1873, 1877, 1879, 1889, 1901, . . .
never ends. This result has many proofs. The oldest one appears as Proposition 20 in Book
IX of Euclid’s Elements.1 We’ll discuss Euclid’s proof and two more, due to Euler and
Erd˝os. Other proofs can be found in [10, Chap. 1].
2. Euclid’s proof
Euclid’s proof of the inﬁnitude of the primes uses the fact that all integers greater than
1 have a prime factor, so let’s discuss that ﬁrst.
Lemma 2.1. Every integer greater than 1 has a prime factor.
Proof. We argue by (strong) induction that each integer n > 1 has a prime factor. For the
base case n = 2, 2 is prime and is a factor of itself.
Now assume n > 2 all integers greater than 1 and less than n have a prime factor. To
show n has a prime factor, we take cases.
Case 1: n is prime.
Since n is a factor of itself, n has a prime factor when n is prime.
Case 2: n is not prime.
Since n is not prime, it has a factorization n = ab where 1 < a, b < n. Then by the
inductive hypothesis, a has a prime factor, say p. Since p | a and a | n, also p | n and thus
n has prime factor p.
□
Remark 2.2. Another approach to proving this lemma is showing each integer greater
than 1 is a product of primes.
Now we present the main result.
Theorem 2.3. There are inﬁnitely many primes.
Proof. (Euclid) To show there are inﬁnitely many primes, we’ll show that every ﬁnite list
of primes is missing a prime number, so the list of all primes can’t be ﬁnite.
There are prime numbers, such as 2. Suppose p1, . . . , pr is a ﬁnite list of prime numbers.
We want to show this is not the full list of the primes. Consider the number
N = p1 · · · pr + 1.
1This book is most well-known as a systematic account of plane and solid geometry, but it does have
parts that are about divisibility and prime numbers.
1

<!-- page 2 -->
2
KEITH CONRAD
Since N > 1, it has a prime factor p by Lemma 2.1. The prime p can’t be any of p1, . . . , pr
since N has remainder 1 when divided by each pi. Therefore p is a prime not on our list,
so the set of primes can’t be ﬁnite.
□
Some people misunderstand that proof by thinking that it says if p1, . . . , pr are all prime
then p1 · · · pr + 1 is prime. That is not generally true! It starts out looking correct: 2 + 1
is prime, 2 · 3 + 1 = 7 is prime, 2 · 3 · 5 + 1 = 31 is prime, 2 · 3 · 5 · 7 + 1 = 211 is prime, and
2 · 3 · 5 · 7 · 11 + 1 = 2311 is prime, but
2 · 3 · 5 · 7 · 11 · 13 + 1 = 30031 = 59 · 509
is not prime. (More simply, 2 · 7 + 1 = 15 and 3 · 5 + 1 = 16 are not prime.) Euclid’s proof
tells us that we can always ﬁnd a prime outside of a ﬁnite list of primes p1, . . . , pr by using
any prime factor of p1 · · · pr + 1, but the number p1 · · · pr + 1 itself need not be prime.
The ancient Greeks did all math from a geometric perspective, so they had no way to
express the general case in arguments we would handle with algebraic notation. Euclid’s
actual proof of Theorem 2.3 does not show “there are more than r primes for each r” as
we did above: it only treats r = 3, but in a way that is suggestive of the general case. See
http://aleph0.clarku.edu/∼djoyce/java/elements/bookIX/propIX20.html.
Let’s try to use Euclid’s proof as a method of ﬁnding new primes, by taking the smallest
prime factor of p1 · · · pr + 1 at each step as a new prime to add to our list:
• 2 is prime and 2 + 1 = 3 is prime,
• 2 · 3 + 1 = 7 is prime,
• 2 · 3 · 7 + 1 = 43 is prime,
• 2 · 3 · 7 · 43 + 1 = 1807 = 13 · 139,
• 2 · 3 · 7 · 43 · 13 + 1 = 23479 = 53 · 443,
• 2 · 3 · 7 · 43 · 13 · 53 + 1 = 1244335 = 5 · 248867.
So far this list of primes in the order they appear is 2, 3, 7, 43, 13, 53, 5. This way of creating
new primes was studied by Mullin [8] in 1963 and is called the Euclid–Mullin sequence.
Further terms in this sequence are on the OEIS webpage https://oeis.org/A000945: 11
is the 12th term, 17 is the 13th term, and 19 is the 36th term. Mullin asked if every prime
number appears as some term in this sequence; this is an unsolved problem.
Mullin also considered a similar algorithm to generate new primes by using the largest
prime factor of p1 · · · pr + 1 at each step. This “second Euclid–Mullin sequence” starts oﬀ
as 2, 3, 7, 43, 139, 50207, 340999. If this list is continued, some primes are known to never
show up in it, such as all primes from 5 to 47 [5]. In fact, inﬁnitely many primes are missing
from this sequence [2], [9].
3. Generalizing Euclid’s proof
By adapting Euclid’s proof of the inﬁnitude of all primes, we can prove certain arithmetic
progressions contain inﬁnitely many primes. For example, each prime p ̸= 2 is 1 mod 4 or
3 mod 4, while each prime p ̸= 3 is 1 mod 3 or 2 mod 3. The primes in these arithmetic
progressions seem to go on indeﬁnitely:
{p ≡1 mod 4} = {5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, . . .},
{p ≡3 mod 4} = {7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, . . .},
{p ≡1 mod 3} = {7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, . . .},
{p ≡2 mod 3} = {5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, . . .}.

<!-- page 3 -->
THE INFINITUDE OF THE PRIMES
3
We’ll show three of these lists of primes are inﬁnite by adapting Euclid’s proof.
Theorem 3.1. There are inﬁnitely many primes p ≡3 mod 4.
Proof. One such prime is 3. If p1, . . . , pr are primes that are each 3 mod 4, let
N = 4p1p2 · · · pr −1,
so N > 1 since N ≥4 · 3 −1 = 11. Clearly N is odd, so N is not divisible by 2 or by
any of p1, . . . , pr. Since N ≡−1 ≡3 mod 4, the prime factors of N are not all 1 mod 4;
otherwise N ≡1 mod 4, because an integer greater than 1 is the product of its primes
factors to some powers. This contradicts the fact that N ≡3 mod 4. Thus N has a prime
factor p that is 3 mod 4. This prime is diﬀerent from p1, . . . , pr, since N ≡0 mod p while
N ≡−1 ̸≡0 mod pi for all i, so there are inﬁnitely many primes that are 3 mod 4.
□
If we try prove there are inﬁnitely many primes p ≡1 mod 4 in the same way, then we
run into a problem. The start of the proof is okay: we know primes that are 1 mod 4, such
as 5, and if p1, . . . , pr are primes that are each 1 mod 4, let
N = 4p1p2 · · · pr + 1,
so N > 1 and N ≡1 mod 4. For the next step we want N to have at least one prime factor
that is 1 mod 4, but this is false: 4 · 5 + 1 = 21 = 3 · 7 and 4 · 5 · 17 + 1 = 341 = 11 · 31,
where the prime factors (3, 7, 11, and 31) are all 3 mod 4. Thus we don’t get a new prime
that’s 1 mod 4 by looking at the prime factors of N.
In order to ﬁx this problem, we will use the following property related to deciding when
−1 mod p can be a square, i.e. when −1 ≡x2 mod p has a solution.
Lemma 3.2. Let p be an odd prime. If −1 ≡x2 mod p for some x ∈Z, then p ≡1 mod 4.
Proof. If −1 ≡x2 mod p for some x ∈Z, then raise both sides to the (p −1)/2 power:
(−1)(p−1)/2 ≡xp−1 mod p, and xp−1 ≡1 mod p by Fermat’s little theorem since x ̸≡0 mod
p. Thus (−1)(p−1)/2 ≡1 mod p. In Z, (−1)(p−1)/2 is ±1 and −1 ̸≡1 mod p since p > 2.
Thus (−1)(p−1)/2 is not −1, so (−1)(p−1)/2 = 1. This makes the exponent (p −1)/2 even,
and when (p −1)/2 = 2k with k ∈Z we have p = 1 + 4k, so p ≡1 mod 4.
□
Theorem 3.3. There are inﬁnitely many primes p ≡1 mod 4.
Proof. One such prime is 5. If p1, . . . , pr are primes that are each 1 mod 4, let
N = (2p1p2 · · · pr)2 + 1 = 4(p1 · · · pr)2 + 1,
so N > 1 since N ≥4 · 25 + 1 = 101. Thus N has a prime factor p. Clearly N is odd, so
p is odd. Since N ≡0 mod p while N ≡1 mod pi for all i, p ̸∈{p1, . . . , pr}. It remains to
show p ≡1 mod 4 (yes, every prime factor of N turns out to be 1 mod 4).
The condition N ≡0 mod p can be rewritten as (2p1 · · · pr)2 ≡−1 mod p. Since p is odd,
p ≡1 mod 4 by Lemma 3.2. Since this prime is not any pi, there are inﬁnitely many primes
that are 1 mod 4.
□
Now let’s look at primes modulo 3.
Theorem 3.4. There are inﬁnitely many primes p ≡2 mod 3.
Proof. One such prime is 2. If p1, . . . , pr are primes that are each 2 mod 3, let
N = 3p1p2 · · · pr −1.

<!-- page 4 -->
4
KEITH CONRAD
Then N is not divisible by 3 or by any of p1, . . . , pr. Since N > 1, N has a prime factor. Since
N ≡−1 ≡2 mod 3, the prime factors of N are not all 1 mod 3; otherwise N ≡1 mod 3.
Therefore N has a prime factor p that is 2 mod 3. The prime p is diﬀerent from p1, . . . , pr,
since N ≡0 mod p while N ≡−1 ̸≡0 mod pi for all i, so there are inﬁnitely many primes
that are 2 mod 3.
□
There is an elementary proof of the inﬁnitude of primes p ≡1 mod 3 that is similar to
the proof of Theorem 3.3, but we omit the argument, which depends on knowing a pattern
that describes when −3 ≡x2 mod p is solvable.
If there are going to be inﬁnitely many primes in an arithmetic progression p ≡a mod m
then we need (a, m) = 1: if d := (a, m) > 1 then an integer n ≡a mod m is divisible by
d and thus n is composite unless d is prime and n = d, e.g., (2, 10) = (4, 10) = 2 > 1 and
there is just one prime p ≡2 mod 10 and there are no primes p ≡4 mod 10. It turns out
that the condition (a, m) = 1 is not just necessary for there to be inﬁnitely many primes
p ≡a mod m, but it is suﬃcient as well! This is a famous theorem of Dirichlet.
Theorem 3.5 (Dirichlet, 1837). If a and m are relatively prime positive integers, there
are inﬁnitely many primes p ≡a mod m: the arithmetic progression {a + mn : n ≥0} has
inﬁnitely many primes p.
For example, the primes p with units digit 7, namely p ≡7 mod 10, starts out as
17, 37, 47, 57, 67, 97, 107, 127, 137, 157, 167, 197, 227, 257, 277, . . .
and never ends. Proving Dirichlet’s theorem in the general case involves methods of analysis
such as limits and inﬁnite series, going far beyond what Euclid used to show there are
inﬁnitely many primes. Even special cases of Dirichlet’s theorem can be hard. I am not
aware of any elementary method showing the set of primes p ≡7 mod 10 is inﬁnite.
There are many unsolved problems about patterns in prime numbers. For example, it is
believed that there are inﬁnitely many primes of the following kinds:
• prime pairs p and p + 2 that diﬀer by 2, such as 3 and 5, 101 and 103, and 1277 and
1279 (these are called twin primes),
• primes of the form 2n −1, such as 22 −1 = 3, 23 −1 = 7, 213 −1 = 8191, and
217 −1 = 131071 (these are called Mersenne primes),
• primes of the form n2 + 1, such as 22 + 1 = 5, 42 + 1 = 17, 262 + 1 = 677, and
402 + 1 = 1601.
4. Euler’s proof
In 1737, Euler [7, Theorem 7] found a proof of the inﬁnitude of the primes that is based
on the divergence of the harmonic series. This unexpected link between a property of prime
numbers and calculus (inﬁnite series) could be considered the start of the subject of analytic
number theory, which studies properties of Z using the tools of real and complex analysis.
While Euclid’s proof used the fact that each integer greater than 1 has a prime factor,
Euler’s proof will rely on unique factorization in Z+.
Theorem 4.1. There are inﬁnitely many primes.
Proof. (Euler) For a prime p, the ratio 1/(1−1/p) can be expanded into a geometric series:
1
1 −1/p = 1 + 1
p + 1
p2 + 1
p3 + 1
p4 + · · ·

<!-- page 5 -->
THE INFINITUDE OF THE PRIMES
5
We will now multiply together these ratios for diﬀerent primes. To see what can be obtained,
let’s look at the product of these terms for the primes 2, 3, and 5:
1
1−1/2
1
1−1/3
1
1−1/5 equals

1 + 1
2 + 1
4 + 1
8 + · · ·
 
1 + 1
3 + 1
9 + 1
27 + · · ·
 
1 + 1
5 + 1
25 +
1
125 + · · ·

,
and if we multiply together one term from each series (this is the distributive law for
multiplying inﬁnite series, and it is valid when multiplying convergent series of positive
numbers) we will get unit fractions 1/n where n is a product of powers of 2, 3, and 5:
(4.1)
1 + 1
2 + 1
3 + 1
4 + 1
5 + 1
6 + 1
8 + 1
9 + 1
10 + 1
12 + 1
15 + 1
16 + 1
18 + 1
20 + 1
24 + · · ·
This looks like the harmonic series, but it is missing terms 1/n where n has a prime factor
greater than 5, such as terms 1/7, 1/11, and 1/14. If we multiply by additional factors
1/(1 −1/p) for more primes p we’ll introduce into (4.1) new terms 1/n where n has prime
factors involving the new primes and the ones we already used (2, 3, and 5). Because of
unique factorization in Z+, each term 1/n that appears will do so just once. Therefore if
we multiply together 1/(1 −1/p) for all the primes,2 (4.1) turns into the sum of 1/n over
all positive integers n:
(4.2)
Y
p
1
1 −1/p =
X
n≥1
1
n,
where the product on the left (denoted Π, like Σ for sum) runs over all prime numbers.
Since the harmonic series diverges, (4.2) tells us that the left side can not be a product
of ﬁnitely many terms. Therefore there are inﬁnitely many terms in the product, so there
are inﬁnitely many primes.
□
By taking logarithms of a product over primes, Euler showed something new about primes
when we sum their reciprocals:
Corollary 4.2. The inﬁnite series P
p 1/p, where p runs over the primes, diverges.
Proof. For N ≥2, multiply out
Y
p≤N
1
1 −1/p =
Y
p≤N

1 + 1
p + 1
p2 + 1
p3 + 1
p4 + . . .

,
where the product is over primes p up to N, by multiplying together one term from each of
the geometric series on the right. We obtain unit fractions 1/n that include every integer
n ≤N, since the prime factors of such n are all at most N. We’ll also get unit fractions
1/n for other n. Therefore
(4.3)
X
n≤N
1
n <
Y
p≤N
1
1 −1/p
As N →∞the left side of (4.3) tends to ∞as N does, so the right side of (4.3) tends to
∞too. That isn’t really telling us anything new, since (4.2) already says Q
p
1
1−1/p = ∞.
2An inﬁnite product, like an inﬁnite series, is a limit of partial products: a1a2a3 · · · = limk→∞a1a2 · · · ak.

<!-- page 6 -->
6
KEITH CONRAD
We can get something new from (4.3) by taking logarithms of both sides before letting N
tend to ∞: logarithms turn products into sums and log x is increasing, so (4.3) implies
(4.4)
log

X
n≤N
1
n

≤
X
p≤N
log
1
1 −1/p
On the right, log(1/(1 −1/p)) = −log(1 −1/p). Recall for |x| < 1 that the power series for
−log(1 −x) is P
n≥1 xn/n = x + x2/2 + x3/3 + · · · , so for small x we have −log(1 −x) ≈
x + x2/2. We need a deﬁnite inequality here, not just “≈”, and for that increase x2/2 up
to x2: for 0 < x ≤1/2, verify by calculus that −log(1 −x) < x + x2 (see the graph below).
y
x
y = x + x2
y = −log(1 −x)
1/2
1
Using x = 1/p for prime p, so x ≤1/2, we have −log(1 −1/p) < 1/p + 1/p2. Thus
X
p≤N
−log(1 −1/p) <
X
p≤N
1
p + 1
p2

.
Combining this with (4.4),
(4.5)
log

X
n≤N
1
n

<
X
p≤N
1
p +
X
p≤N
1
p2 .
Now let N →∞: the left side tends to ∞since P
n≤N 1/n →∞and on the right side
P
p≤N 1/p2 has a ﬁnite limit as N →∞since P
n≥1 1/n2 converges. Therefore (4.5) implies
P
p≤N 1/p →∞as N →∞, so P
p 1/p = ∞.
□
Since P
n≥1 1/n = ∞and P
p 1/p = ∞while P
n≥1 1/n2 < ∞, the primes are “more
dense” among the positive integers than the squares.
Although P
p 1/p = ∞, the divergence is extremely slow. For example, P
p<108 1/p ≈
3.174975. The partial sums P
p≤N 1/p diverge at the rate log(log N), which Euler knew:
the last line of his paper where he proved inﬁnitude of the primes [7] says
1
2 + 1
3 + 1
5 + 1
7 + 1
11 + etc. = l. l ∞,
where l was Euler’s notation for natural logarithms.
In a MathOverﬂow post about the importance of rigor3, the top answer by Richard
Borcherds says “I once got a letter from someone who had overwhelming numerical evidence
that the sum of the reciprocals of primes is slightly bigger than 3 (he may have conjectured
the limit was π). The sum is in fact inﬁnite, but diverges so slowly (like log log n) that
one gets no hint of this by computation.” We saw P
p<108 1/p is slightly above 3. Since
3See https://mathoverflow.net/questions/37610.

<!-- page 7 -->
THE INFINITUDE OF THE PRIMES
7
the solution to log(log x) = 4 is a 24-digit number, a calculator or computer will never give
convincing evidence of the divergence of P
p 1/p.
Corollary 4.2 was important historically in number theory: it suggests a way to prove a
set S of primes is inﬁnite is to show the sum P
p∈S 1/p is ∞. And that is how Dirichlet
proved his theorem about primes in arithmetic progressions: when (a, m) = 1, Dirichlet
proved there are inﬁnitely many primes p ≡a mod m by proving P
p≡a mod m 1/p = ∞.
Earlier we mentioned the unsolved problem of inﬁnitude of the twin primes, which are
prime pairs that diﬀer by 2. If T is the set of all primes p such that p + 2 is also prime,
might P
p∈T 1/p be inﬁnite?
That would imply there are inﬁnitely many twin primes.
Unfortunately, P
p∈T 1/p is known to converge (which doesn’t contradict the possibility
that T is inﬁnite: inﬁnite series can converge). The convergence of P
p∈T 1/p was proved
by Brun [3] in 1919. The convergent series B2 := P
p∈T (1/p + 1/(p + 2)) is called Brun’s
constant.
It is known to be less than 2.4 and is expected to be approximately 1.902.
Estimating B2 is a diﬃcult problem, and work on this in 1994 led to the discovery of a bug
in an Intel Pentium chip.
5. Counting primes
For positive x, the number of primes less than or equal to x is written as π(x). For
example, π(10) = |{2, 3, 5, 7}| = 4 and π(12.7) = |{2, 3, 5, 7, 11}| = 5. Because there are
inﬁnitely many primes, π(x) →∞as x →∞. Euclid’s proof that there are inﬁnitely many
primes implies the following crude lower bound on π(x).
Theorem 5.1. For x ≥2, π(x) > log(log x).
Proof. We will give two proofs. The ﬁrst is based on Euclid’s proof of the inﬁnitude of the
primes and the second proof is based on Euler’s proof.
First proof. If p1, . . . , pn are the ﬁrst n primes, then Euclid’s proof tells us that a prime
factor of p1 · · · pn + 1 is a new prime, so pn+1 ≤p1 · · · pn + 1. Using this inequality, we can
show by induction that pn ≤22n−1 for all n ≥1: it’s true when n = 1 since 2 ≤221−1, and
if that upper bound on primes is true for p1, . . . , pk then
pk+1 ≤p1p2 · · · pk + 1 ≤2 · 22 · · · 22k−1 + 1 = 21+2+···+2k−1 + 1 = 22k−1 + 1,
and that last number is at most 22k since 1
2x + 1 ≤x for x ≥2 (take x = 22k).
That pn ≤22n−1 for all n ≥1 means the number of primes up to 22n−1 is at least n, so
π(22n−1) ≥n for n ≥1. For x ≥2, choose the integer n ≥1 such that 2n−1 ≤log2 x < 2n.
Then x ≥22n−1, so π(x) ≥π(22n−1) ≥n > log2(log2 x). Since 0 < log 2 < 1, log2(y) =
(log y)/(log 2) > log y for y > 0, so log2(log2 x) > log(log x).
Second proof. In inequality (4.3), on the right side 1/(1 −1/p) ≤2, so
X
n≤N
1
n <
Y
p≤N
1
1 −1/p ≤2π(N).
On the left side, by using a Riemann sum approximation to
R N+1
1
dx/x with rectangles of
width 1 we have
X
n≤N
1
n >
Z N+1
1
dx
x = log(N + 1).

<!-- page 8 -->
8
KEITH CONRAD
Therefore log(N +1) < 2π(N) when N ≥2. For x ≥2, letting N ≤x < N +1 for an integer
N, we get
log x < log(N + 1) < 2π(N) = 2π(x) < eπ(x),
so π(x) > log(log x).
□
This lower bound π(x) > log(log x) is extremely weak: the true order of magnitude of
π(x) for large x is x/ log x, meaning that the ratio π(x)/(x/ log x) tends to 1 as x →∞.
That is called the Prime Number Theorem.
6. Erd˝os’s proof
In a footnote to a short paper [6] on divergence of the series P
p 1/p over the primes,
Erd˝os gave the following combinatorial proof that there are inﬁnitely many primes.
Theorem 6.1. There are inﬁnitely many primes.
Proof. Suppose there are ﬁnitely many primes p1, p2, . . . , pr. Each positive integer up to
N can be written uniquely as a2b where a is a positive integer and b is squarefree. Since
a ≤
√
N, the number of choices for a is at most
√
N. Since b is a product of distinct primes
and there are r primes (including an empty product for b = 1), the number of choices of b
is 2r. Therefore the number of possibilities for a2b is at most
√
N2r. There are N positive
integers up to N, so N ≤
√
N2r. By algebra, N ≤22r. This is a contradiction for large
enough N.
□
This argument leads to an improvement on the lower bound π(x) > log(log x) that we
saw earlier.
Corollary 6.2. For every integer N ≥2, π(N) > (log N)/(2 log 2).
Proof. Let r = π(N). Running through the proof of Theorem 6.1 with p1, . . . , pr being
the set of primes up to N (not the set of all primes), by writing positive integers as a2b
for squarefree b we ﬁnd that the number of integers up to N is at most
√
N2r. Therefore
N ≤
√
N2r =
√
N2π(N), so π(N) ≥(log2 N)/2 = (log N)/(2 log 2).
□
We can improve on the lower bound in Corollary 6.2 by using a result called Bertrand’s
postulate: for each integer n ≥2, there is a prime number lying strictly between n and 2n.4
Theorem 6.3. Bertrand’s postulate implies π(x) > log x for all x ≥3.
The inequality π(x) > log x is false for e < x < 3, where π(x) = 1 < log x.
Proof. For x ≥8, let 2k ≤x < 2k+1 for an integer k. The k −1 open intervals (2, 4), (4, 8),
(8, 16), . . . , (2k−1, 2k) each contain a prime number and all of them are all less than x, so
π(x) ≥k −1. This lower bound on π(x) does not include the prime 2 and for the interval
(4, 8) we counted just one prime in it but there are two primes in it. Therefore
π(x) ≥(k −1) + 2 = k + 1 > log2 x > log x
for x ≥8. For 3 ≤x < 5, log x < 2 ≤π(x) and for 5 ≤x ≤8, log x < 3 ≤π(x).
□
4The label “Bertrand’s postulate” is used for historical reasons. It would be better described as Bertrand’s
conjecture. He conjectured it in order to prove the symmetric group Sm has no subgroup with index between
2 and m when m ≥3 [1, p. 129]. It was later proved by Chebyshev [4, Sect. VI].

<!-- page 9 -->
THE INFINITUDE OF THE PRIMES
9
References
[1] J. Bertrand, “M´emoire sur le nombre de valeurs que peut prendre une fonction quand on y permute les
lettres qu’elle renferme,” J. l’´Ecole Roy. Polytech. 18 (1845), 123–140. URL https://books.google.com/
books?id=Tso6AQAAMAAJ&pg=PA123#v=onepage&q&f=false.
[2] A. Booker, “On Mullin’s second sequence of primes,” Integers 12 (2012), 1167–1177.
[3] V. Brun, “La s´erie 1/5+1/7+1/11+1/13+1/17+1/19+1/29+1/31+1/41+1/43+1/59+1/61+. . ., o`u
les d´enominateurs sont nombres premiers jumeaux est convergente ou ﬁnie,” Bull. Sci. Math 43 (1919),
100–104, 124–128. URL https://gallica.bnf.fr/ark:/12148/bpt6k96292009/f104.image.
[4] P. L. Chebyshev, “M´emoire sur les nombres premiers,” J. Math. Pures et Appl. 17 (1852), 366–390. URL
http://sites.mathdoc.fr/ JMPA/PDF/JMPA 1852 1 17 A19 0.pdf.
[5] C. D. Cox and A. J. van der Poorten, “On a sequence of prime numbers,” J. Austral. Math. Soc. 8
(1968), 571–574.
[6] P. Erd˝os, “¨Uber die Reihe P 1/p,” Mathematica (Zutphen) B7 (1938), 1–2. URL https://users.renyi.
hu/∼p erdos/1938-13.pdf.
[7] L. Euler, “Variae observationes circa series inﬁnitas,” Commentarii academiae scientiarum Petropolitanae
9 (1744), 160–188. URL http://eulerarchive.maa.org/pages/E072.html.
[8] A. A. Mullin, “Recursive function theory (A modern look at a Euclidean idea),” Bull. Amer. Math. Soc.
69 (1963), 737.
[9] P. Pollack and E. Trevi˜no, “The primes that Euclid forgot,” Amer. Math. Monthly 121 (2014), 433–437.
[10] P. Ribenboim, The Book of Prime Number Records, Springer-Verlag, New York, 1988.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*