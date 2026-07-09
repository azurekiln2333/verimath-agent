# Fermat's Little Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/fermatlittletheorem.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
FERMAT’S LITTLE THEOREM
KEITH CONRAD
1. Introduction
When we compute powers of nonzero numbers modulo a prime p, something striking
happens for powers of diﬀerent numbers: they are all 1 when the exponent is p −1.
Example 1.1. The tables below show powers of nonzero numbers mod 5 and mod 7. In
the ﬁrst table all fourth powers are 1, and in the second table all sixth powers are 1.
k
1
2
3
4
1k mod 5
1
1
1
1
2k mod 5
2
4
3
1
3k mod 5
3
4
2
1
4k mod 5
4
2
4
1
k
1
2
3
4
5
6
1k mod 7
1
1
1
1
1
1
2k mod 7
2
4
1
2
4
1
3k mod 7
3
2
6
4
5
1
4k mod 7
4
2
1
4
2
1
5k mod 7
5
4
6
2
3
1
6k mod 7
6
1
6
1
6
1
These tables illustrate a property of primes going back to Fermat in 1640 when he tried
to factor numbers of the form an −1 [11, pp. 54-55].
Theorem 1.2 (Fermat). For prime p and every integer a ̸≡0 mod p, ap−1 ≡1 mod p.
This is called Fermat’s little theorem.1 Fermat’s own version was expressed essentially as
p | (ap−1 −1) when p ∤a. After proving the theorem, we will see how it leads to a method
of proving many numbers are composite without needing to factoring them.
2. Proof of Fermat’s Little Theorem
To prove Fermat’s little theorem, we will write down the same list mod p in two diﬀerent
ways and compare their products.
Proof. We have a prime p and an arbitrary integer a ̸≡0 mod p. To show ap−1 ≡1 mod p,
consider nonzero integers modulo p in the standard range:
S = {1, 2, 3, . . . , p −1}.
We will compare S with the set obtained by multiplying the elements of S by a:
aS = {a, a · 2, a · 3, . . . , a(p −1)}.
The elements of S represent the nonzero numbers modulo p and (the key point!)
the
elements of aS also represent the nonzero numbers modulo p.
That is, every nonzero
number mod p is congruent to exactly one number in aS. Indeed, for any b ̸≡0 mod p,
the congruence ax ≡b mod p has a solution x since a mod p is invertible, and necessarily
1This label for the theorem is universal now, but appears to go back only to the early 20th century, e.g.,
[8, p. 103]. See https://johnbcosgrave.com/archive/fermat’s little theorem.htm. Older names for
this result include Fermat’s simple theorem [2, §24], [3] or just Fermat’s theorem [7, Art. 50], [10, p. 7].
1

<!-- page 2 -->
2
KEITH CONRAD
x ̸≡0 mod p (since b ̸≡0 mod p). Adjusting x modulo p to lie between 1 and p −1 we have
x ∈S, so ax ∈aS and thus b mod p is represented by an element of aS. Diﬀerent elements
of aS never represent the same number mod p since ax ≡ay mod p =⇒x ≡y mod p, and
diﬀerent elements of S are not congruent mod p.
Since S and aS become the same set when reduced modulo p, the product of the numbers
in each set must be the same modulo p:
1 · 2 · 3 · · · · · (p −1) ≡a(a · 2)(a · 3) · · · (a(p −1)) mod p.
Pulling the p −1 copies of a to the front of the product on the right, we get
1 · 2 · 3 · · · · · (p −1) ≡ap−1(1 · 2 · 3 · · · · · (p −1)) mod p.
Cancel 1, 2, 3, . . . , p−1 on both sides (all are invertible mod p) and get 1 ≡ap−1 mod p.
□
Remark 2.1. We were led to 1·2·3 · · · (p−1) = (p−1)! modulo p, but we did not calculate
it, since after creating this product on both sides of a congruence we canceled it term by
term. It turns out there is a simple formula for this product: (p−1)! ≡−1 mod p when p is
prime. This is called Wilson’s theorem. It is irrelevant to proving Fermat’s little theorem.
Fermat said in 1640 that he proved this theorem [11, p. 56], but no record of his proof is
known. The ﬁrst published proof is by Euler in 1736 [4]: for prime p and a ∈Z+ he proved
that if p | (ap −a) then p | ((a + 1)p −(a + 1)), so p | (ap −a) for every a ∈Z+ by induction
on a. Since ap −a = a(ap−1 −1), if p ∤a then p | (ap−1 −1), so ap−1 ≡1 mod p, which
is Fermat’s little theorem. Euler’s second proof [5] is based on showing (a + b)p −ap −bp
is divisible by p for all integers a and b. Euler’s third proof [6] is based on what we now
call cosets in group theory (applied to a speciﬁc type of group). The proof we use is due to
Ivory [9] from 1806.
Let’s illustrate the idea behind our proof of Fermat’s little theorem when p = 7.
Example 2.2. When p = 7, S = {1, 2, 3, 4, 5, 6}. Taking a = 2, if we double the elements
of S we get 2S = {2, 4, 6, 8, 10, 12}. This is not the same set of integers as S, but 2S turns
into S when we reduce it mod 7:
2 ≡2, 4 ≡4, 6 ≡6, 8 ≡1, 10 ≡3, 12 ≡5.
Similarly, 3S = {3, 6, 9, 12, 15, 18} and, modulo 7,
3 ≡3, 6 ≡6, 9 ≡2, 12 ≡5, 15 ≡1, 18 ≡4.
For any a ̸≡0 mod 7, the sets {1, 2, 3, 4, 5, 6} and {a, 2a, 3a, 4a, 5a, 6a} turn into the same
list mod 7, so their products are the same modulo 7:
1 · 2 · 3 · 4 · 5 · 6 ≡a · 2a · 3a · 4a · 5a · 6a ≡a6(1 · 2 · 3 · 4 · 5 · 6) mod 7.
Canceling the common factors 1, 2, 3, 4, 5, and 6 from both sides, since they are all nonzero
mod 7, we are left with 1 ≡a6 mod 7.
3. Using Fermat’s Little Theorem to Prove Compositeness
A crucial feature of Fermat’s little theorem is that it is a property of every integer
a ̸≡0 mod p. To emphasize that, let’s rewrite Fermat’s little theorem like this:
If p is a prime number then ap−1 ≡1 mod p for all integers a ̸≡0 mod p.
The power ap−1 makes sense if we replace the prime exponent p with an arbitrary positive
integer exponent m ≥2, so the contrapositive of Fermat’s little theorem says:

<!-- page 3 -->
FERMAT’S LITTLE THEOREM
3
If m ≥2 and am−1 ̸≡1 mod m for some integer a ̸≡0 mod m then m is composite.
This suggests a way to prove a number m ≥2 is composite without having to factor it: just
ﬁnd a single integer a ̸≡0 mod m for which am−1 ̸≡1 mod m. It suﬃces to search for such
a in the range {1, 2, . . . , m −1}.
Deﬁnition 3.1. Call a ∈{1, 2, . . . , m −1} a Fermat witness for m if am−1 ̸≡1 mod m.
Example 3.2. Let m = 48703. Since 2m−1 ≡11646 ̸≡1 mod m, the number 48703 must be
composite and 2 is a Fermat witness for m. We know this without knowing how to factor
48703 into a product of smaller numbers. Of course you can use a computer to rapidly
determine that the prime factorization of m is 113 · 431, but that is a separate issue.
Example 3.3. Let m = 80581. Since 2m−1 ≡1 mod m, there is no contradiction and 2 is
not a Fermat witness. Maybe m is prime. But 3m−1 ≡76861 ̸≡1 mod m, so 3 is a Fermat
witness proving that 80581 is composite, but the reason we know m is composite does not
tell us how to factor m.
Example 3.4. Let m = 225 + 1 = 4294967297. The numbers 22k + 1 are prime when
k = 0, 1, 2, 3, and 4, so Fermat guessed that m is prime, but it is not: while 2m−1 ≡1 mod m,
it turns out that 3m−1 ≡3029026160 ̸≡1 mod m, so 3 is a Fermat witness that proves m is
composite without revealing a nontrivial factor of m. Euler discovered 641 is a factor of m
about 100 years after Fermat mistakenly said m is prime.
These two examples illustrate a point that is at ﬁrst hard to believe: proving a number is
composite and factoring a number in a nontrivial way are not the same task. It is often easier
to prove a number has a nontrivial factorization than it is to ﬁnd a nontrivial factorization.
(Cryptographic protocols used on the internet depend on this distinction.) There are large
numbers known to be composite but for which no nontrivial factor is known.
The process of selecting an a in {1, 2, . . . , m −1} and then computing am−1 mod m to
check whether am−1 ̸≡1 mod m (in which case a is deﬁnitely composite) or am−1t ≡
1 mod m (in which case a is possibly, but not provably, prime), is called the Fermat test
on m. In practice, composite numbers m having hundreds of digits can usually have their
compositeness revealed by running the Fermat test on m just a a few times until a Fermat
witness is found.
A reason it is computationally eﬃcient to compute am−1 mod m is that when you ask a
computer to calculate a large power of a number, such as a48702 in Example 3.2, the computer
is not carrying out anything close to 48000 multiplications. There is a much faster way! By
writing the exponent 48702 in binary, the calculation of a48702 turns into repeated squaring
and can be done with far fewer multiplications than the size of the exponent.
Example 3.5. Since 48702 = 2 + 22 + 23 + 24 + 25 + 29 + 210 + 211 + 212 + 213 + 215, we
can write
(3.1)
a48702 = a2a22a23a24a25a29a210a211a212a213a215,
which is a product of 11 numbers. Each a2k is the result of squaring a successively k times. If
we compute a2k for k = 1, 2, . . . , 15 and save that data, then the number of multiplications
we need to get a48702 is quite small: 15 squarings to get from a2 to a215, and then 10
multiplications of the diﬀerent values of a2k on the right side of (3.1). That is a total of
just 15 + 10 = 25 multiplications to determine a48702.

<!-- page 4 -->
4
KEITH CONRAD
Remark 3.6. How many multiplications are needed to compute aN? If 2d ≤N < 2d+1
then writing N in binary makes aN a product of terms from {a, a2, a4, . . . , a2d}. We need d
repeated squarings to get each of these terms and at most d multiplications of these terms
to get aN, which is a total of at most 2d ≤2 log2 N multiplications. This is much less than
N when N is even moderately big. If N = 48702 then 2 log2 N ≈31.14, while we found
a48702 in Example 3.5 needs 25 multiplications, showing how 2 log2 N works as an upper
bound on the number of required multiplications.
Another aspect that keeps computations under control is that we are interested not in
am−1 itself as a raw integer, but in am−1 mod m. When m is large, calculating am−1 in
Z and then reducing it mod m takes much longer than computing (a mod m)m−1: doing
repeated squaring mod m and reducing intermediate products mod m every time keeps
the output from ever getting much larger than the size of m itself. For example, using
the computer algebra package Sage to determine 1156052360 mod 56052361, the calculation
of 1156052360 in Z followed by reduction modulo 56052361 took 2.210 seconds while the
calculation of (11 mod 56052361)56052360 took 17 microseconds (that’s 17 millionths of a
second). The ﬁrst calculation took 130,000 times as long as the second one.
If we run the Fermat test on m with 10 values of a and don’t ﬁnd a Fermat witness, you
may think m surely must be prime. But that is not the case! There are composite m for
which its Fermat witnesses are rare.
Deﬁnition 3.7. A composite m for which there are no Fermat witnesses relatively prime
to m is called a Carmichael number. Equivalently, m is a Carmichael number when m is
composite and for all a in {1, 2, . . . , m−1} such that (a, m) = 1, we have am−1 ≡1 mod m.
The idea here is that always am−1 ≡1 mod m =⇒(a, m) = 1, so (a, m) > 1 =⇒am−1 ̸≡
1 mod m. Thus an a where (a, m) > 1 is not a Fermat witness for m. A composite number
m is a Carmichael number when its only Fermat witness are the “obvious” choices, meaning
those a from 1 and m −1 that are not relatively prime to m.
The name “Carmichael number” honors Robert Carmichael, who found several such
numbers in the early 20th century. Here are the ﬁrst ﬁve Carmichael numbers:
561, 1105, 1729, 2465, 2821.
Example 3.8. Let m = 13079177569. This number is composite and it turns out that
am−1 ̸≡1 mod m only when (a, m) > 1, so m is a Carmichael number: the Fermat witnesses
for this m are the a in {1, 2, . . . , m −1} such that (a, m) > 1. The number of such a is
18483553, which seems large, but that has 8 digits while m has 11 digits. The proportion of
Fermat witnesses for m is around .14%. (That is not a typo: .14% = .0014 is much smaller
than 1%.) Using a random number generator to pick random numbers in {1, 2, . . . , m −1},
it took 50 trials until I found a Fermat witness for m.
Alford, Granville, and Pomerance [1] proved that there are inﬁnitely many Carmichael
numbers, so there’s never a point beyond which they stop appearing.
When we run the Fermat test on m many times without ﬁnding a Fermat witness, we
should be morally convinced not that m is prime, but instead that m is either a prime
number or a Carmichael number.2
2As Tom Roby likes to say, Carmichael numbers belong to the Fermat witness protection program.

<!-- page 5 -->
FERMAT’S LITTLE THEOREM
5
References
[1] W. R. Alford, A. Granville, C. Pomerance, There are inﬁnitely many Carmichael numbers, Ann. of Math.
139 (1994), 703–722.
[2] R. D. Carmichael, “The Theory of Numbers,” J. Wiley & Sons, New York, 1914. URL https://archive.
org/details/theoryofnumbers00carmuoft/page/n5/mode/2up.
[3] J. Chernick, On Fermat’s simple theorem, Bull. Amer. Math. Soc. 45 (1939), 269–274.
[4] L. Euler, Theorematum quorundam ad numeros primos spectantium demonstratio, Commentarii
Academiae Scientiarum Imperialis Petropolitanae 8 (1736), 141–146. URL https://scholarlycommons.
pacific.edu/euler-works/54/.
[5] L. Euler, Theoremata circa divisores numerorum, Novi Commentarii Academiae Scientiarum Imperialis
Petropolitanae 1 (1750), 20–48. URL https://scholarlycommons.pacific.edu/euler-works/134/.
[6] L. Euler, Theoremata circa residua ex divisione potestatum relicta, Novi Commentarii Academiae
Scientiarum Imperialis Petropolitanae 7 (1761), 49–82. URL https://scholarlycommons.pacific.
edu/euler-works/262/.
[7] C. F. Gauss, “Disquisitiones Arithmeticae,” trans. by A. A. Clarke, Yale Univ. Press, New Haven, 1966.
[8] K. Hensel, “Zahlentheorie,” G. J. G¨oschen, Berlin, 1913. URL https://archive.org/details/zahlen
theorie00hens/mode/2up.
[9] J. Ivory, Demonstration of a theorem respecting prime numbers, New series of The Mathemati-
cal Repository 1 (II) (1806), 6–8. URL https://books.google.com/books/about/New series of The
mathematical repositor.html?id=atULAAAAYAAJ.
[10] C. Jordan, “Trait´e des Substitutions,” Gauthier-Villars, Paris, 1870. URL https://archive.org/
details/traitdessubsti00jorduoft/page/n7/mode/2up.
[11] A. Weil, “Number Theory: An Approach Through History from Hammurapi to Legendre,” Birkhauser,
Boston, 1984.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*