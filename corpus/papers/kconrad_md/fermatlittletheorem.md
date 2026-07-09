# Fermat's Little Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/fermatlittletheorem.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory

<!-- page 1 -->

## 1. Introduction

When we compute powers of nonzero numbers modulo a prime $p$, something striking happens for powers of different numbers: they are all $1$ when the exponent is $p - 1$.

**Example 1.1.** The tables below show powers of nonzero numbers mod $5$ and mod $7$. In the first table all fourth powers are $1$, and in the second table all sixth powers are $1$.

| $k$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $1^k \bmod 5$ | 1 | 1 | 1 | 1 |
| $2^k \bmod 5$ | 2 | 4 | 3 | 1 |
| $3^k \bmod 5$ | 3 | 4 | 2 | 1 |
| $4^k \bmod 5$ | 4 | 2 | 4 | 1 |

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $1^k \bmod 7$ | 1 | 1 | 1 | 1 | 1 | 1 |
| $2^k \bmod 7$ | 2 | 4 | 1 | 2 | 4 | 1 |
| $3^k \bmod 7$ | 3 | 2 | 6 | 4 | 5 | 1 |
| $4^k \bmod 7$ | 4 | 2 | 1 | 4 | 2 | 1 |
| $5^k \bmod 7$ | 5 | 4 | 6 | 2 | 3 | 1 |
| $6^k \bmod 7$ | 6 | 1 | 6 | 1 | 6 | 1 |

These tables illustrate a property of primes going back to Fermat in 1640 when he tried to factor numbers of the form $a^n - 1$ [11, pp. 54-55].

**Theorem 1.2 (Fermat).** *For prime $p$ and every integer $a \not\equiv 0 \bmod p$, $a^{p-1} \equiv 1 \bmod p$.*

This is called *Fermat's little theorem*.[^1] Fermat's own version was expressed essentially as $p \mid (a^{p-1} - 1)$ when $p \nmid a$. After proving the theorem, we will see how it leads to a method of proving many numbers are composite without needing to factoring them.

## 2. Proof of Fermat's Little Theorem

To prove Fermat's little theorem, we will write down the same list mod $p$ in two different ways and compare their products.

*Proof.* We have a prime $p$ and an arbitrary integer $a \not\equiv 0 \bmod p$. To show $a^{p-1} \equiv 1 \bmod p$, consider nonzero integers modulo $p$ in the standard range:

$$S = \{1, 2, 3, \ldots, p - 1\}.$$

We will compare $S$ with the set obtained by multiplying the elements of $S$ by $a$:

$$aS = \{a, a \cdot 2, a \cdot 3, \ldots, a(p - 1)\}.$$

The elements of $S$ represent the nonzero numbers modulo $p$ and (the key point!) the elements of $aS$ *also* represent the nonzero numbers modulo $p$. That is, every nonzero number mod $p$ is congruent to exactly one number in $aS$. Indeed, for any $b \not\equiv 0 \bmod p$, the congruence $ax \equiv b \bmod p$ has a solution $x$ since $a \bmod p$ is invertible, and necessarily $x \not\equiv 0 \bmod p$ (since $b \not\equiv 0 \bmod p$). Adjusting $x$ modulo $p$ to lie between $1$ and $p - 1$ we have $x \in S$, so $ax \in aS$ and thus $b \bmod p$ is represented by an element of $aS$. Different elements of $aS$ never represent the same number mod $p$ since $ax \equiv ay \bmod p \implies x \equiv y \bmod p$, and different elements of $S$ are not congruent mod $p$.

<!-- page 2 -->

Since $S$ and $aS$ become the same set when reduced modulo $p$, the product of the numbers in each set must be the same modulo $p$:

$$1 \cdot 2 \cdot 3 \cdots (p - 1) \equiv a(a \cdot 2)(a \cdot 3) \cdots (a(p - 1)) \bmod p.$$

Pulling the $p - 1$ copies of $a$ to the front of the product on the right, we get

$$1 \cdot 2 \cdot 3 \cdots (p - 1) \equiv a^{p-1}(1 \cdot 2 \cdot 3 \cdots (p - 1)) \bmod p.$$

Cancel $1, 2, 3, \ldots, p - 1$ on both sides (all are invertible mod $p$) and get $1 \equiv a^{p-1} \bmod p$. $\square$

**Remark 2.1.** We were led to $1 \cdot 2 \cdot 3 \cdots (p - 1) = (p - 1)!$ modulo $p$, but we did *not* calculate it, since after creating this product on both sides of a congruence we canceled it term by term. It turns out there is a simple formula for this product: $(p - 1)! \equiv -1 \bmod p$ when $p$ is prime. This is called Wilson's theorem. It is irrelevant to proving Fermat's little theorem.

Fermat said in 1640 that he proved this theorem [11, p. 56], but no record of his proof is known. The first published proof is by Euler in 1736 [4]: for prime $p$ and $a \in \mathbf{Z}^+$ he proved that if $p \mid (a^p - a)$ then $p \mid ((a+1)^p - (a+1))$, so $p \mid (a^p - a)$ for every $a \in \mathbf{Z}^+$ by induction on $a$. Since $a^p - a = a(a^{p-1} - 1)$, if $p \nmid a$ then $p \mid (a^{p-1} - 1)$, so $a^{p-1} \equiv 1 \bmod p$, which is Fermat's little theorem. Euler's second proof [5] is based on showing $(a + b)^p - a^p - b^p$ is divisible by $p$ for all integers $a$ and $b$. Euler's third proof [6] is based on what we now call cosets in group theory (applied to a specific type of group). The proof we use is due to Ivory [9] from 1806.

Let's illustrate the idea behind our proof of Fermat's little theorem when $p = 7$.

**Example 2.2.** When $p = 7$, $S = \{1, 2, 3, 4, 5, 6\}$. Taking $a = 2$, if we double the elements of $S$ we get $2S = \{2, 4, 6, 8, 10, 12\}$. This is not the same set of integers as $S$, but $2S$ turns into $S$ when we reduce it mod $7$:

$$2 \equiv 2, \quad 4 \equiv 4, \quad 6 \equiv 6, \quad 8 \equiv 1, \quad 10 \equiv 3, \quad 12 \equiv 5.$$

Similarly, $3S = \{3, 6, 9, 12, 15, 18\}$ and, modulo $7$,

$$3 \equiv 3, \quad 6 \equiv 6, \quad 9 \equiv 2, \quad 12 \equiv 5, \quad 15 \equiv 1, \quad 18 \equiv 4.$$

For any $a \not\equiv 0 \bmod 7$, the sets $\{1, 2, 3, 4, 5, 6\}$ and $\{a, 2a, 3a, 4a, 5a, 6a\}$ turn into the same list mod $7$, so their products are the same modulo $7$:

$$1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \equiv a \cdot 2a \cdot 3a \cdot 4a \cdot 5a \cdot 6a \equiv a^6(1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6) \bmod 7.$$

Canceling the common factors $1, 2, 3, 4, 5$, and $6$ from both sides, since they are all nonzero mod $7$, we are left with $1 \equiv a^6 \bmod 7$.

## 3. Using Fermat's Little Theorem to Prove Compositeness

A crucial feature of Fermat's little theorem is that it is a property of *every* integer $a \not\equiv 0 \bmod p$. To emphasize that, let's rewrite Fermat's little theorem like this:

If $p$ is a prime number then $a^{p-1} \equiv 1 \bmod p$ for *all* integers $a \not\equiv 0 \bmod p$.

The power $a^{p-1}$ makes sense if we replace the prime exponent $p$ with an arbitrary positive integer exponent $m \geq 2$, so the contrapositive of Fermat's little theorem says:

<!-- page 3 -->

If $m \geq 2$ and $a^{m-1} \not\equiv 1 \bmod m$ for *some* integer $a \not\equiv 0 \bmod m$ then $m$ is composite.

This suggests a way to prove a number $m \geq 2$ is composite without having to factor it: just find a single integer $a \not\equiv 0 \bmod m$ for which $a^{m-1} \not\equiv 1 \bmod m$. It suffices to search for such $a$ in the range $\{1, 2, \ldots, m - 1\}$.

**Definition 3.1.** Call $a \in \{1, 2, \ldots, m - 1\}$ a *Fermat witness* for $m$ if $a^{m-1} \not\equiv 1 \bmod m$.

**Example 3.2.** Let $m = 48703$. Since $2^{m-1} \equiv 11646 \not\equiv 1 \bmod m$, the number $48703$ must be composite and $2$ is a Fermat witness for $m$. We know this without knowing how to factor $48703$ into a product of smaller numbers. Of course you can use a computer to rapidly determine that the prime factorization of $m$ is $113 \cdot 431$, but that is a separate issue.

**Example 3.3.** Let $m = 80581$. Since $2^{m-1} \equiv 1 \bmod m$, there is no contradiction and $2$ is not a Fermat witness. Maybe $m$ is prime. But $3^{m-1} \equiv 76861 \not\equiv 1 \bmod m$, so $3$ is a Fermat witness proving that $80581$ is composite, but the reason we know $m$ is composite does not tell us how to factor $m$.

**Example 3.4.** Let $m = 2^{2^5} + 1 = 4294967297$. The numbers $2^{2^k} + 1$ are prime when $k = 0, 1, 2, 3$, and $4$, so Fermat guessed that $m$ is prime, but it is not: while $2^{m-1} \equiv 1 \bmod m$, it turns out that $3^{m-1} \equiv 3029026160 \not\equiv 1 \bmod m$, so $3$ is a Fermat witness that proves $m$ is composite without revealing a nontrivial factor of $m$. Euler discovered $641$ is a factor of $m$ about 100 years after Fermat mistakenly said $m$ is prime.

These two examples illustrate a point that is at first hard to believe: proving a number is composite and factoring a number in a nontrivial way are *not* the same task. It is often easier to prove a number *has* a nontrivial factorization than it is to *find* a nontrivial factorization. (Cryptographic protocols used on the internet depend on this distinction.) There are large numbers known to be composite but for which no nontrivial factor is known.

The process of selecting an $a$ in $\{1, 2, \ldots, m - 1\}$ and then computing $a^{m-1} \bmod m$ to check whether $a^{m-1} \not\equiv 1 \bmod m$ (in which case $a$ is definitely composite) or $a^{m-1}t \equiv 1 \bmod m$ (in which case $a$ is possibly, but not provably, prime), is called the *Fermat test* on $m$. In practice, composite numbers $m$ having hundreds of digits can usually have their compositeness revealed by running the Fermat test on $m$ just a few times until a Fermat witness is found.

A reason it is computationally efficient to compute $a^{m-1} \bmod m$ is that when you ask a computer to calculate a large power of a number, such as $a^{48702}$ in Example 3.2, the computer is *not* carrying out anything close to $48000$ multiplications. There is a much faster way! By writing the exponent $48702$ in binary, the calculation of $a^{48702}$ turns into repeated squaring and can be done with far fewer multiplications than the size of the exponent.

**Example 3.5.** Since $48702 = 2 + 2^2 + 2^3 + 2^4 + 2^5 + 2^9 + 2^{10} + 2^{11} + 2^{12} + 2^{13} + 2^{15}$, we can write

$$a^{48702} = a^2 a^{2^2} a^{2^3} a^{2^4} a^{2^5} a^{2^9} a^{2^{10}} a^{2^{11}} a^{2^{12}} a^{2^{13}} a^{2^{15}}, \tag{3.1}$$

which is a product of $11$ numbers. Each $a^{2^k}$ is the result of squaring $a$ successively $k$ times. If we compute $a^{2^k}$ for $k = 1, 2, \ldots, 15$ and save that data, then the number of multiplications we need to get $a^{48702}$ is quite small: $15$ squarings to get from $a^2$ to $a^{2^{15}}$, and then $10$ multiplications of the different values of $a^{2^k}$ on the right side of (3.1). That is a total of just $15 + 10 = 25$ multiplications to determine $a^{48702}$.

<!-- page 4 -->

**Remark 3.6.** How many multiplications are needed to compute $a^N$? If $2^d \leq N < 2^{d+1}$ then writing $N$ in binary makes $a^N$ a product of terms from $\{a, a^2, a^4, \ldots, a^{2^d}\}$. We need $d$ repeated squarings to get each of these terms and at most $d$ multiplications of these terms to get $a^N$, which is a total of *at most* $2d \leq 2\log_2 N$ multiplications. This is much less than $N$ when $N$ is even moderately big. If $N = 48702$ then $2\log_2 N \approx 31.14$, while we found $a^{48702}$ in Example 3.5 needs $25$ multiplications, showing how $2\log_2 N$ works as an upper bound on the number of required multiplications.

Another aspect that keeps computations under control is that we are interested not in $a^{m-1}$ itself as a raw integer, but in $a^{m-1} \bmod m$. When $m$ is large, calculating $a^{m-1}$ in $\mathbf{Z}$ and then reducing it mod $m$ takes much longer than computing $(a \bmod m)^{m-1}$: doing repeated squaring mod $m$ and reducing intermediate products mod $m$ every time keeps the output from ever getting much larger than the size of $m$ itself. For example, using the computer algebra package Sage to determine $11^{56052360} \bmod 56052361$, the calculation of $11^{56052360}$ in $\mathbf{Z}$ followed by reduction modulo $56052361$ took $2.210$ seconds while the calculation of $(11 \bmod 56052361)^{56052360}$ took $17$ microseconds (that's $17$ millionths of a second). The first calculation took $130{,}000$ times as long as the second one.

If we run the Fermat test on $m$ with $10$ values of $a$ and don't find a Fermat witness, you may think $m$ surely must be prime. But that is not the case! There are composite $m$ for which its Fermat witnesses are rare.

**Definition 3.7.** A composite $m$ for which there are no Fermat witnesses relatively prime to $m$ is called a *Carmichael number*. Equivalently, $m$ is a Carmichael number when $m$ is composite and for all $a$ in $\{1, 2, \ldots, m - 1\}$ such that $(a, m) = 1$, we have $a^{m-1} \equiv 1 \bmod m$.

The idea here is that always $a^{m-1} \equiv 1 \bmod m \implies (a, m) = 1$, so $(a, m) > 1 \implies a^{m-1} \not\equiv 1 \bmod m$. Thus an $a$ where $(a, m) > 1$ is not a Fermat witness for $m$. A composite number $m$ is a Carmichael number when its only Fermat witness are the "obvious" choices, meaning those $a$ from $1$ and $m - 1$ that are not relatively prime to $m$.

The name "Carmichael number" honors Robert Carmichael, who found several such numbers in the early 20th century. Here are the first five Carmichael numbers:

$$561, \quad 1105, \quad 1729, \quad 2465, \quad 2821.$$

**Example 3.8.** Let $m = 13079177569$. This number is composite and it turns out that $a^{m-1} \not\equiv 1 \bmod m$ only when $(a, m) > 1$, so $m$ is a Carmichael number: the Fermat witnesses for this $m$ are the $a$ in $\{1, 2, \ldots, m - 1\}$ such that $(a, m) > 1$. The number of such $a$ is $18483553$, which seems large, but that has $8$ digits while $m$ has $11$ digits. The proportion of Fermat witnesses for $m$ is around $.14\%$. (That is not a typo: $.14\% = .0014$ is much smaller than $1\%$.) Using a random number generator to pick random numbers in $\{1, 2, \ldots, m - 1\}$, it took $50$ trials until I found a Fermat witness for $m$.

Alford, Granville, and Pomerance [1] proved that there are infinitely many Carmichael numbers, so there's never a point beyond which they stop appearing.

When we run the Fermat test on $m$ many times without finding a Fermat witness, we should be morally convinced not that $m$ is prime, but instead that $m$ is either a prime number or a Carmichael number.[^2]

[^1]: This label for the theorem is universal now, but appears to go back only to the early 20th century, *e.g.*, [8, p. 103]. See <https://johnbcosgrave.com/archive/fermat's_little_theorem.htm>. Older names for this result include Fermat's simple theorem [2, §24], [3] or just Fermat's theorem [7, Art. 50], [10, p. 7].
[^2]: As Tom Roby likes to say, Carmichael numbers belong to the Fermat witness protection program.

<!-- page 5 -->

## References

[1] W. R. Alford, A. Granville, C. Pomerance, There are infinitely many Carmichael numbers, *Ann. of Math.* **139** (1994), 703--722.

[2] R. D. Carmichael, "The Theory of Numbers," J. Wiley & Sons, New York, 1914. URL <https://archive.org/details/theoryofnumbers00carmuoft/page/n5/mode/2up>.

[3] J. Chernick, On Fermat's simple theorem, *Bull. Amer. Math. Soc.* **45** (1939), 269--274.

[4] L. Euler, Theorematum quorundam ad numeros primos spectantium demonstratio, *Commentarii Academiae Scientiarum Imperialis Petropolitanae* **8** (1736), 141--146. URL <https://scholarlycommons.pacific.edu/euler-works/54/>.

[5] L. Euler, Theoremata circa divisores numerorum, *Novi Commentarii Academiae Scientiarum Imperialis Petropolitanae* **1** (1750), 20--48. URL <https://scholarlycommons.pacific.edu/euler-works/134/>.

[6] L. Euler, Theoremata circa residua ex divisione potestatum relicta, *Novi Commentarii Academiae Scientiarum Imperialis Petropolitanae* **7** (1761), 49--82. URL <https://scholarlycommons.pacific.edu/euler-works/262/>.

[7] C. F. Gauss, "Disquisitiones Arithmeticae," trans. by A. A. Clarke, Yale Univ. Press, New Haven, 1966.

[8] K. Hensel, "Zahlentheorie," G. J. Goschen, Berlin, 1913. URL <https://archive.org/details/zahlentheorie00hens/mode/2up>.

[9] J. Ivory, Demonstration of a theorem respecting prime numbers, *New series of The Mathematical Repository* **1** (II) (1806), 6--8. URL <https://books.google.com/books/about/New_series_of_The_mathematical_repositor.html?id=atULAAAAQAAJ>.

[10] C. Jordan, "Traité des Substitutions," Gauthier-Villars, Paris, 1870. URL <https://archive.org/details/traitdessubsti00jorduoft/page/n7/mode/2up>.

[11] A. Weil, "Number Theory: An Approach Through History from Hammurapi to Legendre," Birkhauser, Boston, 1984.
