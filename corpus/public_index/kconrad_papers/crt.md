# Chinese Remainder Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/crt.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE CHINESE REMAINDER THEOREM
KEITH CONRAD
We should thank the Chinese for their wonderful remainder theorem.
Glenn Stevens
1. Introduction
The Chinese remainder theorem says we can uniquely solve every pair of congruences
having relatively prime moduli.
Theorem 1.1. Let m and n be relatively prime positive integers. For all integers a and b,
the pair of congruences
x ≡a mod m,
x ≡b mod n
has a solution, and this solution is uniquely determined modulo mn.
What is important here is that m and n are relatively prime. There are no constraints
at all on a and b.
Example 1.2. The congruences x ≡6 mod 9 and x ≡4 mod 11 hold when x = 15, and
more generally when x ≡15 mod 99, and they do not hold for other x. The modulus 99 is
9 · 11.
We will prove the Chinese remainder theorem, including a version for more than two
moduli, and see some ways it is applied to study congruences.
2. A proof of the Chinese remainder theorem
Proof. First we show there is always a solution. Then we will show it is unique modulo mn.
Existence of Solution. To show that the simultaneous congruences
x ≡a mod m,
x ≡b mod n
have a common solution in Z, we give two proofs.
First proof: Write the ﬁrst congruence as an equation in Z, say x = a + my for some
y ∈Z. Then the second congruence is the same as
a + my ≡b mod n.
Subtracting a from both sides, we need to solve for y in
(2.1)
my ≡b −a mod n.
Since (m, n) = 1, we know m mod n is invertible.
Let m′ be an inverse for m mod n,
so mm′ ≡1 mod n. Multiplying through (2.1) by m′, we have y ≡m′(b −a) mod n, so
y ≡m′(b −a) + nz where z ∈Z. Then
x = a + my = a + m(m′(b −a) + nz) = a + mm′(b −a) + mnz.
1

<!-- page 2 -->
2
KEITH CONRAD
So if x satisﬁes the original two congruences it must have this form. Let’s now check this
expression, for every z ∈Z, really satisﬁes the original two congruences:
a + mm′(b −a) + mnz ≡a + 0 + 0 ≡a mod m
and
a + mm′(b −a) + mnz ≡a + 1(b −a) + 0 ≡b mod n.
Second proof: Write both congruences as equations in Z: x = a + my and x = b + nz
for integers y and z that need to be determined. (Why would it be a bad idea to write
x = a + my and x = b + ny?) The integers of the form a + my are the numbers that
are congruent to a mod m, and the integers of the form b + nz are the numbers that are
congruent to b mod n.
Finding a common solution to the two congruences amounts to
ﬁnding y and z in Z such that
a + my = b + nz,
which is the same as
(2.2)
my −nz = b −a.
Can we ﬁnd such y and z for all a, b, m, and n where (m, n) = 1? Bezout’s identity tells us 1
is a Z-linear combination of m and n, and therefore every integer is a Z-linear combination
of m and n (why?). Therefore integers y and z satisfying (2.2) exist.
Uniqueness of Solution. If x = c and x = c′ both satisfy
x ≡a mod m,
x ≡b mod n,
then we have c ≡c′ mod m and c ≡c′ mod n. Then m | (c −c′) and n | (c −c′). Since
(m, n) = 1, the product mn divides c −c′, which means c ≡c′ mod mn. This shows all
solutions to the initial pair of congruences are the same modulo mn.
□
3. Extension to more than two congruences
The Chinese remainder theorem can be extended from two congruences to an arbitrary
ﬁnite number of congruences, but we have to be careful about the way in which the moduli
are relatively prime. Consider the three congruences
x ≡1 mod 6,
x ≡4 mod 10,
x ≡7 mod 15.
While there is no common factor of 6, 10, and 15 greater than 1, these congruences do not
admit a common solution: every solution to the ﬁrst congruence is odd, while every solution
to the second congruence is even. When we have more than two moduli, we have to be
sensitive to the diﬀerence between saying the moduli are collectively relatively prime (no
common factor greater than 1 divides all the moduli) and pairwise relatively prime (each
pair of moduli have no common factor greater than 1). For instance, 6, 10, and 15 are
collectively relatively prime but not pairwise relatively prime. Here is a more general form
of the Chinese remainder theorem that allows more than two moduli.
Theorem 3.1. For r ≥2, let m1, m2, . . . , mr be nonzero integers that are pairwise rela-
tively prime: (mi, mj) = 1 for i ̸= j. Then, for all integers a1, a2, . . . , ar, the system of
congruences
x ≡a1 mod m1,
x ≡a2 mod m2,
. . . ,
x ≡ar mod mr,
has a solution, and this solution is uniquely determined modulo m1m2 · · · mr.
Example 3.2. The congruences x ≡1 mod 3, x ≡2 mod 5, x ≡2 mod 7 are satisﬁed when
x = 37, more generally for all x ≡37 mod 105 and for no other x. Note 105 = 3 · 5 · 7.

<!-- page 3 -->
THE CHINESE REMAINDER THEOREM
3
Proof. First we show there is always a solution. Then we will show it is unique modulo
m1m2 · · · mr.
Existence of Solution. We argue by induction on r. The base case r = 2 is Theorem
1.1, which has been proved already.
Now we pass to the inductive step. Suppose all simultaneous congruences with r pairwise
relatively prime moduli can be solved. Consider a system of simultaneous congruences with
r + 1 pairwise relatively prime moduli:
x ≡a1 mod m1,
. . . ,
x ≡ar mod mr,
x ≡ar+1 mod mr+1,
where (mi, mj) = 1 for all i ̸= j and the ai’s are arbitrary. By the inductive hypothesis,
there is a solution b to the ﬁrst r congruences, say
b ≡a1 mod m1,
b ≡a2 mod m2,
. . . ,
b ≡ar mod mr.
Now consider the system of two congruences
(3.1)
x ≡b mod m1m2 · · · mr,
x ≡ar+1 mod mr+1.
Since (mi, mr+1) = 1 for i = 1, 2, . . . , r, we have (m1m2 · · · mr, mr+1) = 1, so the two moduli
in (3.1) are relatively prime. Then by the case of two congruences, namely Theorem 1.1,
there is a solution to (3.1). Call it c. Since c ≡b mod m1m2 · · · mr, we have c ≡b mod mi
for i = 1, 2, . . . , r. From the choice of b we have b ≡ai mod mi for i = 1, 2, . . . , r. Therefore
c ≡ai mod mi for i = 1, 2, . . . , r. Also, c ≡ar+1 mod mr+1 from the choice of c, so we see
c satisﬁes the r + 1 given congruences.
This concludes the inductive step, so a solution exists.
Uniqueness of Solution. If x = c and x = c′ both satisfy
x ≡a1 mod m1,
x ≡a2 mod m2,
. . . ,
x ≡ar mod mr,
then we have c ≡c′ mod mi for i = 1, 2, . . . , r, so mi | (c −c′) for i = 1, 2, . . . , r. Since the
mi’s are pairwise relatively prime, their product m1m2 · · · mr divides c −c′, which means
c ≡c′ mod m1m2 · · · mr. This shows all solutions to the given system of congruences are
the same when viewed modulo m1m2 · · · mr.
□
4. Applications
The signiﬁcance of the Chinese remainder theorem is that it often reduces a question
about modulus mn, where (m, n) = 1, to the same question for modulus m and n separately.
In this way, questions about modular arithmetic can often be reduced to the special case of
prime power moduli. We will see how this works for several counting problems, often using
two features of modular arithmetic with two moduli:1
• if d | m it makes sense to reduce integers mod m to integers mod d: if x ≡y mod m
then x ≡y mod d. For example, if x ≡y mod 10 then x ≡y mod 5 since if x −y
is divisible by 10 then it is also divisible by 5. (In contrast, it makes no sense to
reduce x mod 10 to x mod 3, since there are congruent numbers mod 10 that are
incongruent mod 3, such as 1 and 11.)
• if x ≡y mod m and x ≡y mod n and (m, n) = 1 then x ≡y mod mn. This was
used in the uniqueness part of the proof of the Chinese remainder theorem.
Our ﬁrst application is to counting units mod m.
1The Chinese remainder theorem for two or more moduli that need not be prime powers has real-world
uses, such as determining a target range using multiple radar signals [1, Sec.10.5, 10.6].

<!-- page 4 -->
4
KEITH CONRAD
Theorem 4.1. For relatively prime positive integers m and n, ϕ(mn) = ϕ(m)ϕ(n).
Proof. We work with the sets
Um = {a mod m, (a, m) = 1},
Un = {b mod n, (b, n) = 1},
Umn = {c mod mn, (c, mn) = 1}.
Then |Um| = ϕ(m), |Un| = ϕ(n), and |Umn| = ϕ(mn). To show ϕ(mn) = ϕ(m)ϕ(n), we
will write down a bijection between Umn and Um × Un, which implies the two sets have the
same size, and that is what the theorem is saying (since |Um × Un| = ϕ(m)ϕ(n)).
Let f : Umn →Um × Un by the rule
f(c mod mn) = (c mod m, c mod n).
For c ∈Umn, we have (c, mn) = 1, so (c, m) and (c, n) equal 1, so c mod m and c mod n
are units. Let’s stop for a moment to take a look at an example of this function.
Take m = 3 and n = 5: U3 = {1, 2}, U5 = {1, 2, 3, 4}, and U15 = {1, 2, 4, 7, 8, 11, 13, 14}.
The following table shows the values of the function f on each number in U15. Notice that
the values ﬁll up all of U3 × U5 without repetition.
c mod 15
f(c mod 15)
1
(1, 1)
2
(2, 2)
4
(4, 4) = (1, 4)
7
(7, 7) = (1, 2)
8
(8, 8) = (2, 3)
11
(11, 11) = (2, 1)
13
(13, 13) = (1, 3)
14
(14, 14) = (2, 4)
There are 2 units modulo 3 and 4 units modulo 5, leading to 8 ordered pairs of units modulo
3 and units modulo 5: (1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), and (2,4). All these pairs
show up (and just once) in the second column of the table.
We return to the general situation and show f : Umn →Um × Un is a bijection.
To see that f is one-to-one, suppose f(k mod mn) = f(ℓmod mn). Then k ≡ℓmod m
and k ≡ℓmod n, so since (m, n) = 1 (aha!), we have k ≡ℓmod mn. That means k = ℓin
Umn, so f is one-to-one.
Now we show f is onto. Pick a pair (a mod m, b mod n) ∈Um × Un. By the Chinese
remainder theorem we can solve c ≡a mod m and c ≡b mod n for a c ∈Z. Is (c, mn) = 1?
Since a mod m is a unit and c ≡a mod m, c mod m is a unit so (c, m) = 1. Since b mod n
is a unit and c ≡b mod n, c mod n is a unit so (c, n) = 1. From (c, m) = 1 and (c, n) = 1 we
get (c, mn) = 1, so c ∈Umn. From the congruence conditions on c, we have f(c) = (a, b).
□
Corollary 4.2. For a positive integer m,
ϕ(m) = m
Y
p|m

1 −1
p

,
where the product runs over the primes p dividing m.
Proof. The formula is clear for m = 1 (interpreting an empty product as 1).
Now suppose m > 1, and factor m into prime powers:
m = pe1
1 pe2
2 · · · per
r .

<!-- page 5 -->
THE CHINESE REMAINDER THEOREM
5
The pei
i ’s are pairwise relatively prime. By an extension of Theorem 4.1 from two relatively
prime terms to an arbitrary number of pairwise relatively prime terms (just induct on the
number of terms), we have
ϕ(m) = ϕ(pe1
1 )ϕ(pe2
2 ) · · · ϕ(per
r ).
Now using the formula for ϕ on prime powers,
ϕ(m) = pe1−1
1
(p1 −1)pe2−1
2
(p2 −1) · · · per−1
r
(pr −1)
= pe1
1

1 −1
p1

pe2
2

1 −1
p2

· · · per
r

1 −1
pr

= m
Y
p|m

1 −1
p

.
□
Example 4.3. To compute ϕ(540) = ϕ(22 · 33 · 5), we have
ϕ(540) = 540

1 −1
2
 
1 −1
3
 
1 −1
5

= 540 · 1
2 · 2
3 · 4
5
= 18 · 8
= 144.
An alternate calculation is
ϕ(540) = ϕ(4)ϕ(27)ϕ(5)
= (4 −2)(27 −9)(5 −1)
= 2 · 18 · 4
= 144.
Example 4.4. A table of values of ϕ(m), as shown below, suggests that ϕ(m) is even when
m > 2, which is true. But not every positive even number is a value of the ϕ-function.
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
17
ϕ(m)
1
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
We will use the general formula for ϕ(m) to show for all odd primes q > 3 that there is
no solution to ϕ(m) = 2q2. (For example, taking q = 5, 7, and 11, ϕ(m) is never 50, 98,
or 242. But 2 · 32 = ϕ(33).) For each odd prime factor p of m, ϕ(m) is divisible by p −1,
which is even, so if m has more than 2 odd prime factors then ϕ(m) would be divisible by
4. Thus when ϕ(m) = 2q2, m has at most one odd prime factor, so m = 2e, 2epf, or pf (all
exponents are positive).
• If m = 2e then ϕ(m) = 2e−1 is a power of 2, which is not true.
• If m = pf then ϕ(m) = pf−1(p −1), so if this is 2q2 then pf−1(p −1)/2 = q2. If
f ≥2 then p | q2, so p = q and qf−1(q −1)/2 = q2. Every prime factor of (q −1)/2
has to be q, which is impossible, so (q −1)/2 = 1 and thus q = 3, so when q > 3 we
can’t have m = pf.
• If m = 2epf then ϕ(m) = ϕ(2e)ϕ(pf) = 2e−1(p −1)pf−1. The factor p −1 is even,
and if e ≥2 then 2e−1 is also even, which contradicts ϕ(m) = 2q2. Therefore e = 1,

<!-- page 6 -->
6
KEITH CONRAD
so m = 2pf and ϕ(m) = (p −1)pf−1 = ϕ(pf). By the previous case, if ϕ(pf) = 2q2
then q = 3.
We now leave units mod m and look at squares mod m.
Theorem 4.5. For m ∈Z+ with m ≥2, let Sm = {x2 mod m} be the set of squares modulo
m. When (m, n) = 1, |Smn| = |Sm| · |Sn|.
Note Sm is all squares modulo m, including 0. So S5 = {0, 1, 4}, for example.
Proof. We will use the Chinese remainder theorem twice.
If a ≡x2 mod mn then a ≡x2 mod m and a ≡x2 mod n. Thus a square modulo mn
reduces to a square modulo m and a square modulo n. So we have a function f : Smn →
Sm × Sn by f(a mod mn) = (a mod m, a mod n). Let’s take a look at an example.
Set m = 3 and n = 5, so S3 = {0, 1}, S5 = {0, 1, 4} and S15 = {0, 1, 4, 6, 9, 10}. The table
below gives the values of f on S15. The values ﬁll up S3 × S5 without repetition.
c mod 15
f(c mod 15)
0
(0, 0)
1
(1, 1)
4
(4, 4) = (1, 4)
6
(6, 6) = (0, 1)
9
(9, 9) = (0, 4)
10
(10, 10) = (1, 0)
Returning to the general case, to show f is one-to-one let’s suppose f(c mod mn) =
f(c′ mod mn). Then c ≡c′ mod m and c ≡c′ mod n, so c ≡c′ mod mn since (m, n) = 1.
To show f is onto, pick a pair of squares b mod m and c mod n, say b ≡y2 mod m and
c ≡z2 mod n. By the Chinese remainder theorem, there is an integer a satisfying
a ≡b mod m,
a ≡c mod n.
We want to say f(a) = (b, c), but is a mod mn a square? From the expressions for b mod m
and c mod n as squares, a ≡y2 mod m and a ≡z2 mod n, but y and z are not related to
each other. They certainly don’t have to be the same integer, so these two congruences on
their own don’t tell us a mod mn is a square. Using the Chinese remainder theorem again,
however, there is x ∈Z such that
x ≡y mod m,
x ≡z mod n,
so x2 ≡y2 mod m and x2 ≡z2 mod n. Therefore a ≡x2 mod m and a ≡x2 mod n, so
a ≡x2 mod mn, so a mod mn is in fact a square. Thus a ∈Smn and f(a) = (b, c).
□
Example 4.6. For a prime p, the number of nonzero squares mod p is (p −1)/2 and 0
is a square, so the total number of squares mod p is 1 + (p −1)/2 = (p + 1)/2. Thus
|Sp| = (p + 1)/2. So if n = p1p2 . . . pr is squarefree, |Sn| = |Sp1| · · · |Spr| = p1+1
2
· · · pr+1
2 . If
n = pe1
1 · · · per
r , we have |Sn| = |Spe1
1 | · · · |Sper
r |, so a formula for |Spe| when e > 1 (which we
don’t give here) would lead to a formula for |Sm| in general.
We turn now from counting all the squares mod m to counting how often something is a
square mod m.
Example 4.7. We can write 1 mod 15 as a square in four ways: 1 ≡12 ≡42 ≡92 ≡
142 mod 15.

<!-- page 7 -->
THE CHINESE REMAINDER THEOREM
7
Theorem 4.8. Let m ∈Z+ have prime factorization pe1
1 · · · per
r . For a ∈Z, the congruence
x2 ≡a mod m is solvable if and only if the separate congruences x2 ≡a mod pei
i are solvable
for i = 1, 2, . . . , r.
Furthermore, if the congruence x2 ≡a mod pei
i
has Ni solutions, then the congruence
x2 ≡a mod m has N1N2 · · · Nr solutions.
Example 4.9. The congruences x2 ≡1 mod 3 and x2 ≡1 mod 5 each have two solutions,
so x2 ≡1 mod 15 has 2 · 2 = 4 solutions; we saw the four square roots of 1 mod 15 before
the statement of Theorem 4.8.
Proof. If x ∈Z satisﬁes x2 ≡a mod m, then x2 ≡a mod pei
i for all i.
Conversely, suppose each of the congruences x2 ≡a mod pei
i
has a solution, say x2
i ≡
a mod pei
i
for some integers xi. Since the pei
i ’s are pairwise relatively prime, the Chinese
remainder theorem tells us there is an x such that x ≡xi mod pei
i
for all i. Then x2 ≡
x2
i mod pei
i
for all i, so x2 ≡a mod pei
i
for all i. Since x2 −a is divisible by each pei
i
it is
divisible by m, so x2 ≡a mod m.
To count the solutions modulo m, we again use the Chinese remainder theorem. Any
choice of solution xi mod pei
i for each i ﬁts together in exactly one way to a number x mod m,
and this number will satisfy x2 ≡a mod m. Therefore we can count solutions modulo m
by counting solutions modulo each pei
i and multiply the counts thanks to the independence
of the choice of solutions for diﬀerent primes.
□
Example 4.10. To decide if 61 is a square modulo 75, we check whether 61 is a square
modulo 3 and modulo 25. Since 61 ≡1 mod 3, it is a square modulo 3. Since 61 ≡11 ≡
62 mod 25, it is a square modulo 25. Therefore 63 is a square modulo 75. In fact, we can
get a square root by solving the congruences
x ≡1 mod 3,
x ≡6 mod 25.
A solution is x = 31, so 61 ≡312 mod 75.
Remark 4.11. It is crucial to remember that using the Chinese remainder theorem requires
the moduli to be relatively prime (more precisely, pairwise relatively prime). For a prime p
you may be able to prove results about modulus pk+1 from similar results for moduli p and
pk, but the proof won’t be based on the Chinese remainder theorem since p and pk are not
relatively prime. An example of such a result is that if p is an odd prime and a ̸≡0 mod p,
then for k ≥2, a mod pk is a square if and only if a mod p is a square. Proving that has
nothing to do with the Chinese remainder theorem.
If you scrutinize the proofs of Theorems 4.5 and 4.8 to see how it was important we were
working with squares, you’ll see that what really matters is that squaring is a polynomial
expression. With this in mind, we get the following two generalizations from squares to
values of other polynomials.
Theorem 4.12. Let f(x) be a polynomial with integer coeﬃcients. For a positive integer
m ≥2, let Nf(m) = |{f(x) mod m : 0 ≤x ≤m −1}| be the number of values of f on
diﬀerent integers mod m. If m has prime factorization
m = pe1
1 · · · per
r ,
then Nf(m) = Nf(pe1
1 ) · · · Nf(per
r ).
Proof. Proceed as in the proof of Theorem 4.5, which is the special case f(x) = x2.
□

<!-- page 8 -->
8
KEITH CONRAD
Theorem 4.13. Let f(x) be a polynomial with integer coeﬃcients. For a positive integer
m with prime factorization
m = pe1
1 · · · per
r ,
the congruence f(x) ≡0 mod m is solvable if and only if the congruences f(x) ≡0 mod pei
i
are each solvable.
Moreover, if f(x) ≡0 mod pei
i
has Ni solutions, then the congruence f(x) ≡0 mod m
has N1N2 · · · Nr solutions.
Proof. Argue as in the proof of Theorem 4.8, which is the special case f(x) = x2 −a.
□
Theorem 4.13 tells us that ﬁnding solutions to a polynomial equation modulo positive
integers is reduced by the Chinese remainder theorem to the case of understanding solutions
modulo prime powers.
Consider now the following situation: f(x) is a polynomial with integral coeﬃcients and
every value f(n), for n ∈Z, is either a multiple of 2 or a multiple of 3. For instance, if
f(x) = x2 −x then f(n) = n2 −n is even for all n. Or if f(x) = x3 −x then f(n) = n3 −n
is a multiple of 3 for all n. But these examples are kind of weak: what about a mixed
example where every f(n) is a multiple of 2 or 3 but some f(n) are multiples of 2 and not
3 while other f(n) are multiples of 3 and not 2? Actually, no such polynomial exists! The
only way f(n) can be divisible either by 2 or 3 for all n is if it is a multiple of 2 for all n or
a multiple of 3 for all n. To explain this, we will use the Chinese remainder theorem.
Theorem 4.14. Let f(x) be a polynomial with integral coeﬃcients. Suppose for a ﬁnite
set of primes p1, . . . , pr each f(n) for n ∈Z is divisible by some pi. Then there is a pi such
that each f(n) is divisible by that pi.
Proof. Suppose the conclusion is false. Then, for each pi, there is an ai ∈Z such that pi
does not divide f(ai). Said diﬀerently, f(ai) ̸≡0 mod pi.
Since the pi’s for i = 1, . . . , r are diﬀerent primes, we can use the Chinese remain-
der theorem to ﬁnd an integer a such that a ≡ai mod pi for i = 1, 2, . . . , r.
Then
f(a) ≡f(ai) mod pi for i = 1, 2, . . . , r (why?), so f(a) ̸≡0 mod pi for all i. However, the
assumption in the theorem was that every value of the polynomial on integers is divisible
by some pi, so we have a contradiction.
□
Remark 4.15. If f(x) is a polynomial with integral coeﬃcients and there is a ﬁnite set of
nonzero pairwise relatively prime integers m1, . . . , mr such that, for every integer n, f(n)
is divisible by some mi, then there is some mi such that mi | f(n) for every n ∈Z. The
proof of Theorem 4.14 carries over directly to this case, with mi replacing pi.
Our next application of the Chinese remainder theorem will describe examples where a
polynomial equation can have solutions mod m for all m ≥2 even without having integer
solutions, provided it has two “well-chosen” rational solutions. The idea is best explained
by an example.
Example 4.16. The equation 2x2 + 7y2 = 1 obviously has no solution in Z. It does have
solutions in Q, such as (x, y) = (1/3, 1/3) and (3/5, 1/5). We will use these two rational
solutions to show the congruence 2x2 + 7y2 ≡1 mod m is solvable for every m ≥2. The
key point is that the two pairs of rational solutions have relatively prime denominators, 3
and 5.

<!-- page 9 -->
THE CHINESE REMAINDER THEOREM
9
Write out the equations with their rational solutions and clear denominators:
2
1
3
2
+ 7
1
3
2
= 1 =⇒2 · 12 + 7 · 12 = 32,
2
3
5
2
+ 7
1
5
2
= 1 =⇒2 · 32 + 7 · 12 = 52.
For m ≥2, we can reduce both equations in integers modulo m:
(4.1)
2 · 12 + 7 · 12 ≡32 mod m,
2 · 32 + 7 · 12 ≡52 mod m.
We will consider these congruence separately, then together.
Case 1: m is not divisible by 3. We know 3 mod m has an inverse, say 3d ≡1 mod m.
Morally, d is “1/3 mod m”. Multiplying through the ﬁrst congruence in (4.1) by d2:
(4.2)
2 · 12 + 7 · 12 ≡32 mod m ⇒2d2 + 7d2 ≡1 mod m,
and the solution (d, d) mod m should be regarded as “(1/3, 1/3) mod m.”
Case 2: m is not divisible by 5. Some integer d′ satisﬁes 5d′ ≡1 mod m and multiplying
through the second congruence in (4.1) by d′2 gives us
(4.3)
2 · 32 + 7 · 12 ≡52 mod m ⇒2(3d′)2 + 7d′2 ≡1 mod m,
where the solution (3d′, d′) mod m should be regarded as “(3/5, 1/5) mod m.”
Case 3: m ≥2 is arbitrary. We want to show 2x2 + 7y2 ≡1 mod m is solvable. If m is
not divisible by 3 (but could be divisible by 5) then we can use (4.2). If m is not divisible
by 5 (but could be divisible by 3) then we can use (4.3). What do we do if m is divisible
by both 3 and 5? Use the Chinese remainder theorem!
Factor the biggest power of 3 from m: m = 3eM with e ≥1 and (3, M) = 1. (Since m is
divisible by 5, M > 1.)
• Since 3e is not divisible by 5, (4.3) tells us that 2(3d′)2 + 7d′2 ≡1 mod 3e where
5d′ ≡1 mod 3e. (The solution (3d′, d′) mod 3e is like “(3/5, 1/5) mod 3e.”)
• Since M is not divisible by 3, (4.2) tells us that 2d2 + 7d2 ≡1 mod M where 3d ≡
1 mod M. (The solution (d, d) mod M is like “(1/3, 1/3) mod M.”)
In order to solve 2x2 + 7y2 ≡1 mod m, we use integers x and y such that
x ≡3d′ mod 3e,
x ≡d mod M,
y ≡d′ mod 3e,
y ≡d mod M.
Such x and y exist by the Chinese remainder theorem. Then 2x2 + 7y2 ≡2(3d′)2 + 7d′2 ≡
1 mod 3e and 2x2 + 7y2 ≡2d2 + 7d2 ≡1 mod M, so 2x2 + 7y2 ≡1 mod 3eM .
For instance, take m = 105 = 3 · 5 · 7. Write m = 3M where M = 35. The inverse of
5 mod 3 is d′ = 2, so in place of (3/5, 1/5) use (3d′, d′) = (3 · 2, 2) mod 3 = (0, 2) mod 3.
The inverse of 3 mod 35 is d = 12, so in place of (1/3, 1/3) use (d, d) = (12, 12) mod 35.
Now we solve
x ≡0 mod 3,
x ≡12 mod 35,
y ≡2 mod 3,
y ≡12 mod 35,
which turns out to be x ≡12 mod 105, y ≡47 mod 105, and indeed 2 · 122 + 7 · 472 ≡
1 mod 105.
To check that you understand how this example worked, use the solutions (9/2, 1/2) and
(32/3, 5/3) of x2 −37y2 = 11 to show you can solve x2 −37y2 ≡11 mod m for every m ≥2.

<!-- page 10 -->
10
KEITH CONRAD
(It can be shown by other arguments that x2 −37y2 = 11 has no solution in Z, which makes
its solvability mod m for all m interesting!)
Theorem 4.17. If the equation ax2 + by2 = c, where a, b, c ∈Z, has two rational solutions
(k/d, ℓ/d) and (k′/d′, ℓ′/d′) where the denominators d and d′ are relatively prime then the
congruence ax2 + by2 ≡c mod m has a solution for every m ≥2.
Proof. Exercise, adapting the ideas of the preceding example. We can assume d > 1 and
d′ > 1, since if d = 1 or d′ = 1 then one of the rational solutions is an integral solution and
that will be a solution mod m directly for all m.
□
We need the two rational solutions in the theorem to have relatively prime denominators
in order to get a solution mod m for every m. Consider, for instance x2 −41y2 = 2, which
has the solution (x, y) = (7/2, 1/2). This is enough to get a solution to x2−41y2 ≡2 mod m
for all odd m > 1 by inverting 2 modulo m, but without an additional rational solution
having an odd denominator we don’t get a solution modulo m for m an arbitrary power of
2. And indeed, there is no solution to x2 −41y2 ≡2 mod 2e when e ≥2 since there is no
solution modulo 4.
Our ﬁnal application of the Chinese remainder theorem is to an interpolation problem,
to see that the scope of the Chinese remainder theorem goes beyond the setting of just the
integers.
Given n points in the plane, (a1, b1), . . . , (an, bn), with the ai’s distinct, we would like to
ﬁnd a polynomial f(T) in R[T] whose graph passes through these points: f(ai) = bi for
i = 1, 2, . . . , n. This task can be converted to a set of simultaneous congruences in R[T],
which can be solved using the Chinese remainder theorem in R[T], not Z. First let’s state
the Chinese remainder theorem for polynomials.
Theorem 4.18. For r ≥2, let m1(T), m2(T), . . . , mr(T) be nonzero polynomials in R[T]
which are pairwise relatively prime: (mi(T), mj(T)) = 1 for i ̸= j. Then, for all polynomials
a1(T), a2(T), . . . , ar(T) in R[T], the system of congruences
f(T) ≡a1(T) mod m1(T),
f(T) ≡a2(T) mod m2(T),
. . . ,
f(T) ≡ar(T) mod mr(T),
has a solution f(T) in R[T], and this solution is unique modulo m1(T)m2(T) · · · mr(T).
The proof of this is identical to that of the Chinese remainder theorem for Z, so we leave
it to the reader as an exercise.
Theorem 4.19. In R, pick two lists of n numbers a1, a2, . . . , an and b1, b2, . . . , bn where
the ai’s are distinct. There is a unique polynomial f(T) of degree < n in R[T], possibly 0,
such that f(ai) = bi for all i.
Proof. To say f(ai) = bi is the same as f(T) ≡bi mod T −ai (why?). Consider the system
of congruences
f(T) ≡b1 mod T −a1, f(T) ≡b2 mod T −a2, . . . , f(T) ≡bn mod T −an
for an unknown f(T) in R[T]. Since the ai’s are distinct, the polynomials T −a1, . . . , T −an
are pairwise relatively prime in R[T]. Therefore, by the Chinese remainder theorem in R[T],
there is an f(T) in R[T] satisfying all of the above congruences. It follows that f(ai) = bi
for all i.
We have no initial control over deg f for the common solution f. However, since we can
adjust f(T) modulo (T −a1) · · · (T −an) without changing the congruence conditions, we

<!-- page 11 -->
THE CHINESE REMAINDER THEOREM
11
can replace f(T) with its remainder under division by (T −a1) · · · (T −an), which has degree
n. Then deg f < n with f(ai) = bi for all i.
We have shown a desired f(T) exists. To see it is unique, suppose f1(T) and f2(T) both
have degree less than n and satisfy
f(T) ≡b1 mod T −a1, f(T) ≡b2 mod T −a2, . . . , f(T) ≡bn mod T −an.
Then, by the uniqueness in the Chinese remainder theorem, we have
f1(T) ≡f2(T) mod (T −a1) · · · (T −an).
Since f1(T) and f2(T) have degree less than n, this congruence modulo a polynomial of
degree n implies f1(T) = f2(T) in R[T].
□
The fact that polynomial interpolation is identical to solving a system of polynomial
congruences (with linear moduli) suggests that we should think about solving a system of
integer congruences as arithmetic interpolation.
There is nothing essential about R in Theorem 4.19 except that it’s a ﬁeld. The Chinese
remainder theorem goes through for F[T] with F a general ﬁeld, not just R, and Theorem
4.19 carries over to a general ﬁeld:
Theorem 4.20. Let F be a ﬁeld. For n distinct numbers a1, a2, . . . , an in F and arbitrary
numbers b1, b2, . . . , bn in F, which may have repetitions, there is a unique polynomial f(T)
of degree < n in F[T], possibly 0, such that f(ai) = bi for all i.
The proof is identical to that of Theorem 4.19.
References
[1] R. J. Sullivan, “Radar Foundations for Imaging and Advanced Concepts,” Scitech Publishing, 2004.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*