# The Infinitude of the Primes

> **Source**: https://kconrad.math.uconn.edu/blurbs/infinitudeofprimes.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory

<!-- page 1 -->

## 1. Introduction

The sequence of prime numbers

$$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, \ldots, 1873, 1877, 1879, 1889, 1901, \ldots$$

never ends. This result has many proofs. The oldest one appears as Proposition 20 in Book IX of *Euclid's Elements*.[^1] We'll discuss Euclid's proof and two more, due to Euler and Erdos. Other proofs can be found in [10, Chap. 1].

## 2. Euclid's Proof

Euclid's proof of the infinitude of the primes uses the fact that all integers greater than 1 have a prime factor, so let's discuss that first.

**Lemma 2.1.** *Every integer greater than 1 has a prime factor.*

*Proof.* We argue by (strong) induction that each integer $n > 1$ has a prime factor. For the base case $n = 2$, 2 is prime and is a factor of itself.

Now assume $n > 2$ all integers greater than 1 and less than $n$ have a prime factor. To show $n$ has a prime factor, we take cases.

*Case 1:* $n$ is prime.

Since $n$ is a factor of itself, $n$ has a prime factor when $n$ is prime.

*Case 2:* $n$ is not prime.

Since $n$ is not prime, it has a factorization $n = ab$ where $1 < a, b < n$. Then by the inductive hypothesis, $a$ has a prime factor, say $p$. Since $p \mid a$ and $a \mid n$, also $p \mid n$ and thus $n$ has prime factor $p$. $\square$

**Remark 2.2.** Another approach to proving this lemma is showing each integer greater than 1 is a product of primes.

Now we present the main result.

**Theorem 2.3.** *There are infinitely many primes.*

*Proof.* (Euclid) To show there are infinitely many primes, we'll show that every finite list of primes is missing a prime number, so the list of all primes can't be finite.

There are prime numbers, such as 2. Suppose $p_1, \ldots, p_r$ is a finite list of prime numbers. We want to show this is not the full list of the primes. Consider the number

$$N = p_1 \cdots p_r + 1.$$

[^1]: This book is most well-known as a systematic account of plane and solid geometry, but it does have parts that are about divisibility and prime numbers.

<!-- page 2 -->

Since $N > 1$, it has a prime factor $p$ by Lemma 2.1. The prime $p$ can't be any of $p_1, \ldots, p_r$ since $N$ has remainder 1 when divided by each $p_i$. Therefore $p$ is a prime not on our list, so the set of primes can't be finite. $\square$

Some people misunderstand that proof by thinking that it says if $p_1, \ldots, p_r$ are all prime then $p_1 \cdots p_r + 1$ is prime. That is not generally true! It starts out looking correct: $2 + 1 = 3$ is prime, $2 \cdot 3 + 1 = 7$ is prime, $2 \cdot 3 \cdot 5 + 1 = 31$ is prime, $2 \cdot 3 \cdot 5 \cdot 7 + 1 = 211$ is prime, and $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 + 1 = 2311$ is prime, but

$$2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \cdot 509$$

is *not* prime. (More simply, $2 \cdot 7 + 1 = 15$ and $3 \cdot 5 + 1 = 16$ are not prime.) Euclid's proof tells us that we can always find a prime outside of a finite list of primes $p_1, \ldots, p_r$ by using any prime factor of $p_1 \cdots p_r + 1$, but the number $p_1 \cdots p_r + 1$ itself need not be prime.

The ancient Greeks did all math from a geometric perspective, so they had no way to express the general case in arguments we would handle with algebraic notation. Euclid's actual proof of Theorem 2.3 does not show "there are more than $r$ primes for each $r$" as we did above: it only treats $r = 3$, but in a way that is suggestive of the general case. See <http://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX20.html>.

Let's try to use Euclid's proof as a method of finding new primes, by taking the *smallest* prime factor of $p_1 \cdots p_r + 1$ at each step as a new prime to add to our list:

- 2 is prime and $2 + 1 = 3$ is prime,
- $2 \cdot 3 + 1 = 7$ is prime,
- $2 \cdot 3 \cdot 7 + 1 = 43$ is prime,
- $2 \cdot 3 \cdot 7 \cdot 43 + 1 = 1807 = 13 \cdot 139$,
- $2 \cdot 3 \cdot 7 \cdot 43 \cdot 13 + 1 = 23479 = 53 \cdot 443$,
- $2 \cdot 3 \cdot 7 \cdot 43 \cdot 13 \cdot 53 + 1 = 1244335 = 5 \cdot 248867$.

So far this list of primes in the order they appear is $2, 3, 7, 43, 13, 53, 5$. This way of creating new primes was studied by Mullin [8] in 1963 and is called the Euclid-Mullin sequence. Further terms in this sequence are on the OEIS webpage <https://oeis.org/A000945>: 11 is the 12th term, 17 is the 13th term, and 19 is the 36th term. Mullin asked if every prime number appears as some term in this sequence; this is an unsolved problem.

Mullin also considered a similar algorithm to generate new primes by using the *largest* prime factor of $p_1 \cdots p_r + 1$ at each step. This "second Euclid-Mullin sequence" starts off as $2, 3, 7, 43, 139, 50207, 340999$. If this list is continued, some primes are known to never show up in it, such as all primes from 5 to 47 [5]. In fact, infinitely many primes are missing from this sequence [2], [9].

## 3. Generalizing Euclid's Proof

By adapting Euclid's proof of the infinitude of all primes, we can prove certain arithmetic progressions contain infinitely many primes. For example, each prime $p \neq 2$ is $1 \bmod 4$ or $3 \bmod 4$, while each prime $p \neq 3$ is $1 \bmod 3$ or $2 \bmod 3$. The primes in these arithmetic progressions seem to go on indefinitely:

$$\begin{aligned} \{p \equiv 1 \bmod 4\} &= \{5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, \ldots\}, \\ \{p \equiv 3 \bmod 4\} &= \{7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, \ldots\}, \\ \{p \equiv 1 \bmod 3\} &= \{7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, \ldots\}, \\ \{p \equiv 2 \bmod 3\} &= \{5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, \ldots\}. \end{aligned}$$

<!-- page 3 -->

We'll show three of these lists of primes are infinite by adapting Euclid's proof.

**Theorem 3.1.** *There are infinitely many primes $p \equiv 3 \bmod 4$.*

*Proof.* One such prime is 3. If $p_1, \ldots, p_r$ are primes that are each $3 \bmod 4$, let

$$N = 4p_1 p_2 \cdots p_r - 1,$$

so $N > 1$ since $N \geq 4 \cdot 3 - 1 = 11$. Clearly $N$ is odd, so $N$ is not divisible by 2 or by any of $p_1, \ldots, p_r$. Since $N \equiv -1 \equiv 3 \bmod 4$, the prime factors of $N$ are not all $1 \bmod 4$; otherwise $N \equiv 1 \bmod 4$, because an integer greater than 1 is the product of its primes factors to some powers. This contradicts the fact that $N \equiv 3 \bmod 4$. Thus $N$ has a prime factor $p$ that is $3 \bmod 4$. This prime is different from $p_1, \ldots, p_r$, since $N \equiv 0 \bmod p$ while $N \equiv -1 \not\equiv 0 \bmod p_i$ for all $i$, so there are infinitely many primes that are $3 \bmod 4$. $\square$

If we try prove there are infinitely many primes $p \equiv 1 \bmod 4$ in the same way, then we run into a problem. The start of the proof is okay: we know primes that are $1 \bmod 4$, such as 5, and if $p_1, \ldots, p_r$ are primes that are each $1 \bmod 4$, let

$$N = 4p_1 p_2 \cdots p_r + 1,$$

so $N > 1$ and $N \equiv 1 \bmod 4$. For the next step we want $N$ to have at least one prime factor that is $1 \bmod 4$, but this is *false*: $4 \cdot 5 + 1 = 21 = 3 \cdot 7$ and $4 \cdot 5 \cdot 17 + 1 = 341 = 11 \cdot 31$, where the prime factors (3, 7, 11, and 31) are all $3 \bmod 4$. Thus we don't get a new prime that's $1 \bmod 4$ by looking at the prime factors of $N$.

In order to fix this problem, we will use the following property related to deciding when $-1 \bmod p$ can be a square, *i.e.* when $-1 \equiv x^2 \bmod p$ has a solution.

**Lemma 3.2.** *Let $p$ be an odd prime. If $-1 \equiv x^2 \bmod p$ for some $x \in \mathbf{Z}$, then $p \equiv 1 \bmod 4$.*

*Proof.* If $-1 \equiv x^2 \bmod p$ for some $x \in \mathbf{Z}$, then raise both sides to the $(p-1)/2$ power: $(-1)^{(p-1)/2} \equiv x^{p-1} \bmod p$, and $x^{p-1} \equiv 1 \bmod p$ by Fermat's little theorem since $x \not\equiv 0 \bmod p$. Thus $(-1)^{(p-1)/2} \equiv 1 \bmod p$. In $\mathbf{Z}$, $(-1)^{(p-1)/2}$ is $\pm 1$ and $-1 \not\equiv 1 \bmod p$ since $p > 2$. Thus $(-1)^{(p-1)/2}$ is *not* $-1$, so $(-1)^{(p-1)/2} = 1$. This makes the exponent $(p-1)/2$ even, and when $(p-1)/2 = 2k$ with $k \in \mathbf{Z}$ we have $p = 1 + 4k$, so $p \equiv 1 \bmod 4$. $\square$

**Theorem 3.3.** *There are infinitely many primes $p \equiv 1 \bmod 4$.*

*Proof.* One such prime is 5. If $p_1, \ldots, p_r$ are primes that are each $1 \bmod 4$, let

$$N = (2p_1 p_2 \cdots p_r)^2 + 1 = 4(p_1 \cdots p_r)^2 + 1,$$

so $N > 1$ since $N \geq 4 \cdot 25 + 1 = 101$. Thus $N$ has a prime factor $p$. Clearly $N$ is odd, so $p$ is odd. Since $N \equiv 0 \bmod p$ while $N \equiv 1 \bmod p_i$ for all $i$, $p \notin \{p_1, \ldots, p_r\}$. It remains to show $p \equiv 1 \bmod 4$ (yes, *every* prime factor of $N$ turns out to be $1 \bmod 4$).

The condition $N \equiv 0 \bmod p$ can be rewritten as $(2p_1 \cdots p_r)^2 \equiv -1 \bmod p$. Since $p$ is odd, $p \equiv 1 \bmod 4$ by Lemma 3.2. Since this prime is not any $p_i$, there are infinitely many primes that are $1 \bmod 4$. $\square$

Now let's look at primes modulo 3.

**Theorem 3.4.** *There are infinitely many primes $p \equiv 2 \bmod 3$.*

*Proof.* One such prime is 2. If $p_1, \ldots, p_r$ are primes that are each $2 \bmod 3$, let

$$N = 3p_1 p_2 \cdots p_r - 1.$$

<!-- page 4 -->

Then $N$ is not divisible by 3 or by any of $p_1, \ldots, p_r$. Since $N > 1$, $N$ has a prime factor. Since $N \equiv -1 \equiv 2 \bmod 3$, the prime factors of $N$ are not all $1 \bmod 3$; otherwise $N \equiv 1 \bmod 3$. Therefore $N$ has a prime factor $p$ that is $2 \bmod 3$. The prime $p$ is different from $p_1, \ldots, p_r$, since $N \equiv 0 \bmod p$ while $N \equiv -1 \not\equiv 0 \bmod p_i$ for all $i$, so there are infinitely many primes that are $2 \bmod 3$. $\square$

There is an elementary proof of the infinitude of primes $p \equiv 1 \bmod 3$ that is similar to the proof of Theorem 3.3, but we omit the argument, which depends on knowing a pattern that describes when $-3 \equiv x^2 \bmod p$ is solvable.

If there are going to be infinitely many primes in an arithmetic progression $p \equiv a \bmod m$ then we need $(a, m) = 1$: if $d := (a, m) > 1$ then an integer $n \equiv a \bmod m$ is divisible by $d$ and thus $n$ is composite unless $d$ is prime and $n = d$, *e.g.*, $(2, 10) = (4, 10) = 2 > 1$ and there is just one prime $p \equiv 2 \bmod 10$ and there are no primes $p \equiv 4 \bmod 10$. It turns out that the condition $(a, m) = 1$ is not just necessary for there to be infinitely many primes $p \equiv a \bmod m$, but it is sufficient as well! This is a famous theorem of Dirichlet.

**Theorem 3.5 (Dirichlet, 1837).** *If $a$ and $m$ are relatively prime positive integers, there are infinitely many primes $p \equiv a \bmod m$: the arithmetic progression $\{a + mn : n \geq 0\}$ has infinitely many primes $p$.*

For example, the primes $p$ with units digit 7, namely $p \equiv 7 \bmod 10$, starts out as

$$17, 37, 47, 57, 67, 97, 107, 127, 137, 157, 167, 197, 227, 257, 277, \ldots$$

and never ends. Proving Dirichlet's theorem in the general case involves methods of analysis such as limits and infinite series, going far beyond what Euclid used to show there are infinitely many primes. Even special cases of Dirichlet's theorem can be hard. I am not aware of any elementary method showing the set of primes $p \equiv 7 \bmod 10$ is infinite.

There are many unsolved problems about patterns in prime numbers. For example, it is believed that there are infinitely many primes of the following kinds:

- prime pairs $p$ and $p + 2$ that differ by 2, such as 3 and 5, 101 and 103, and 1277 and 1279 (these are called *twin primes*),
- primes of the form $2^n - 1$, such as $2^2 - 1 = 3$, $2^3 - 1 = 7$, $2^{13} - 1 = 8191$, and $2^{17} - 1 = 131071$ (these are called *Mersenne primes*),
- primes of the form $n^2 + 1$, such as $2^2 + 1 = 5$, $4^2 + 1 = 17$, $26^2 + 1 = 677$, and $40^2 + 1 = 1601$.

## 4. Euler's Proof

In 1737, Euler [7, Theorem 7] found a proof of the infinitude of the primes that is based on the divergence of the harmonic series. This unexpected link between a property of prime numbers and calculus (infinite series) could be considered the start of the subject of *analytic number theory*, which studies properties of $\mathbf{Z}$ using the tools of real and complex analysis. While Euclid's proof used the fact that each integer greater than 1 has a prime factor, Euler's proof will rely on unique factorization in $\mathbf{Z}^+$.

**Theorem 4.1.** *There are infinitely many primes.*

*Proof.* (Euler) For a prime $p$, the ratio $1/(1 - 1/p)$ can be expanded into a geometric series:

$$\frac{1}{1 - 1/p} = 1 + \frac{1}{p} + \frac{1}{p^2} + \frac{1}{p^3} + \frac{1}{p^4} + \cdots$$

<!-- page 5 -->

We will now multiply together these ratios for different primes. To see what can be obtained, let's look at the product of these terms for the primes 2, 3, and 5: $\frac{1}{1-1/2}\frac{1}{1-1/3}\frac{1}{1-1/5}$ equals

$$\left(1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots\right)\left(1 + \frac{1}{3} + \frac{1}{9} + \frac{1}{27} + \cdots\right)\left(1 + \frac{1}{5} + \frac{1}{25} + \frac{1}{125} + \cdots\right),$$

and if we multiply together one term from each series (this is the distributive law for multiplying infinite series, and it is valid when multiplying convergent series of positive numbers) we will get unit fractions $1/n$ where $n$ is a product of powers of 2, 3, and 5:

$$1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{8} + \frac{1}{9} + \frac{1}{10} + \frac{1}{12} + \frac{1}{15} + \frac{1}{16} + \frac{1}{18} + \frac{1}{20} + \frac{1}{24} + \cdots \tag{4.1}$$

This looks like the harmonic series, but it is missing terms $1/n$ where $n$ has a prime factor greater than 5, such as terms $1/7$, $1/11$, and $1/14$. If we multiply by additional factors $1/(1 - 1/p)$ for more primes $p$ we'll introduce into (4.1) new terms $1/n$ where $n$ has prime factors involving the new primes and the ones we already used (2, 3, and 5). Because of unique factorization in $\mathbf{Z}^+$, each term $1/n$ that appears will do so just once. Therefore if we multiply together $1/(1 - 1/p)$ for *all* the primes,[^2] (4.1) turns into the sum of $1/n$ over all positive integers $n$:

$$\prod_p \frac{1}{1 - 1/p} = \sum_{n \geq 1} \frac{1}{n}, \tag{4.2}$$

where the product on the left (denoted $\Pi$, like $\Sigma$ for sum) runs over all prime numbers.

Since the harmonic series diverges, (4.2) tells us that the left side can *not* be a product of finitely many terms. Therefore there are infinitely many terms in the product, so there are infinitely many primes. $\square$

By taking logarithms of a product over primes, Euler showed something new about primes when we sum their reciprocals:

**Corollary 4.2.** *The infinite series $\sum_p 1/p$, where $p$ runs over the primes, diverges.*

*Proof.* For $N \geq 2$, multiply out

$$\prod_{p \leq N} \frac{1}{1 - 1/p} = \prod_{p \leq N} \left(1 + \frac{1}{p} + \frac{1}{p^2} + \frac{1}{p^3} + \frac{1}{p^4} + \cdots\right),$$

where the product is over primes $p$ up to $N$, by multiplying together one term from each of the geometric series on the right. We obtain unit fractions $1/n$ that include every integer $n \leq N$, since the prime factors of such $n$ are all at most $N$. We'll also get unit fractions $1/n$ for other $n$. Therefore

$$\sum_{n \leq N} \frac{1}{n} < \prod_{p \leq N} \frac{1}{1 - 1/p}. \tag{4.3}$$

As $N \to \infty$ the left side of (4.3) tends to $\infty$ as $N$ does, so the right side of (4.3) tends to $\infty$ too. That isn't really telling us anything new, since (4.2) already says $\prod_p \frac{1}{1-1/p} = \infty$.

[^2]: An infinite product, like an infinite series, is a limit of partial products: $a_1 a_2 a_3 \cdots = \lim_{k \to \infty} a_1 a_2 \cdots a_k$.

<!-- page 6 -->

We can get something new from (4.3) by taking logarithms of both sides before letting $N$ tend to $\infty$: logarithms turn products into sums and $\log x$ is increasing, so (4.3) implies

$$\log\left(\sum_{n \leq N} \frac{1}{n}\right) \leq \sum_{p \leq N} \log \frac{1}{1 - 1/p}. \tag{4.4}$$

On the right, $\log(1/(1 - 1/p)) = -\log(1 - 1/p)$. Recall for $|x| < 1$ that the power series for $-\log(1 - x)$ is $\sum_{n \geq 1} x^n/n = x + x^2/2 + x^3/3 + \cdots$, so for small $x$ we have $-\log(1 - x) \approx x + x^2/2$. We need a definite inequality here, not just "$\approx$", and for that increase $x^2/2$ up to $x^2$: for $0 < x \leq 1/2$, verify by calculus that $-\log(1 - x) < x + x^2$ (see the graph below).

![Graph of y = x + x^2 and y = -log(1-x)](graph.png)

Using $x = 1/p$ for prime $p$, so $x \leq 1/2$, we have $-\log(1 - 1/p) < 1/p + 1/p^2$. Thus

$$\sum_{p \leq N} -\log(1 - 1/p) < \sum_{p \leq N} \left(\frac{1}{p} + \frac{1}{p^2}\right).$$

Combining this with (4.4),

$$\log\left(\sum_{n \leq N} \frac{1}{n}\right) < \sum_{p \leq N} \frac{1}{p} + \sum_{p \leq N} \frac{1}{p^2}. \tag{4.5}$$

Now let $N \to \infty$: the left side tends to $\infty$ since $\sum_{n \leq N} 1/n \to \infty$ and on the right side $\sum_{p \leq N} 1/p^2$ has a finite limit as $N \to \infty$ since $\sum_{n \geq 1} 1/n^2$ converges. Therefore (4.5) implies $\sum_{p \leq N} 1/p \to \infty$ as $N \to \infty$, so $\sum_p 1/p = \infty$. $\square$

Since $\sum_{n \geq 1} 1/n = \infty$ and $\sum_p 1/p = \infty$ while $\sum_{n \geq 1} 1/n^2 < \infty$, the primes are "more dense" among the positive integers than the squares.

Although $\sum_p 1/p = \infty$, the divergence is *extremely* slow. For example, $\sum_{p < 10^8} 1/p \approx 3.174975$. The partial sums $\sum_{p \leq N} 1/p$ diverge at the rate $\log(\log N)$, which Euler knew: the last line of his paper where he proved infinitude of the primes [7] says

$$\frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + \frac{1}{11} + \text{etc.} = l.l\infty,$$

where $l$ was Euler's notation for natural logarithms.

In a MathOverflow post about the importance of rigor[^3], the top answer by Richard Borcherds says "I once got a letter from someone who had overwhelming numerical evidence that the sum of the reciprocals of primes is slightly bigger than 3 (he may have conjectured the limit was $\pi$). The sum is in fact infinite, but diverges so slowly (like $\log \log n$) that one gets no hint of this by computation." We saw $\sum_{p < 10^8} 1/p$ is slightly above 3. Since

[^3]: See <https://mathoverflow.net/questions/37610>.

<!-- page 7 -->

the solution to $\log(\log x) = 4$ is a 24-digit number, a calculator or computer will never give convincing evidence of the divergence of $\sum_p 1/p$.

Corollary 4.2 was important historically in number theory: it suggests a way to prove a set $S$ of primes is infinite is to show the sum $\sum_{p \in S} 1/p = \infty$. And that is how Dirichlet proved his theorem about primes in arithmetic progressions: when $(a, m) = 1$, Dirichlet proved there are infinitely many primes $p \equiv a \bmod m$ by proving $\sum_{p \equiv a \bmod m} 1/p = \infty$.

Earlier we mentioned the unsolved problem of infinitude of the twin primes, which are prime pairs that differ by 2. If $T$ is the set of all primes $p$ such that $p + 2$ is also prime, might $\sum_{p \in T} 1/p$ be infinite? That would imply there are infinitely many twin primes. Unfortunately, $\sum_{p \in T} 1/p$ is known to converge (which doesn't contradict the possibility that $T$ is infinite: infinite series can converge). The convergence of $\sum_{p \in T} 1/p$ was proved by Brun [3] in 1919. The convergent series $B_2 := \sum_{p \in T}(1/p + 1/(p+2))$ is called Brun's constant. It is known to be less than 2.4 and is expected to be approximately 1.902. Estimating $B_2$ is a difficult problem, and work on this in 1994 led to the discovery of a bug in an Intel Pentium chip.

## 5. Counting Primes

For positive $x$, the number of primes less than or equal to $x$ is written as $\pi(x)$. For example, $\pi(10) = |\{2, 3, 5, 7\}| = 4$ and $\pi(12.7) = |\{2, 3, 5, 7, 11\}| = 5$. Because there are infinitely many primes, $\pi(x) \to \infty$ as $x \to \infty$. Euclid's proof that there are infinitely many primes implies the following crude lower bound on $\pi(x)$.

**Theorem 5.1.** *For $x \geq 2$, $\pi(x) > \log(\log x)$.*

*Proof.* We will give two proofs. The first is based on Euclid's proof of the infinitude of the primes and the second proof is based on Euler's proof.

First proof. If $p_1, \ldots, p_n$ are the first $n$ primes, then Euclid's proof tells us that a prime factor of $p_1 \cdots p_n + 1$ is a new prime, so $p_{n+1} \leq p_1 \cdots p_n + 1$. Using this inequality, we can show by induction that $p_n \leq 2^{2^{n-1}}$ for all $n \geq 1$: it's true when $n = 1$ since $2 \leq 2^{2^1-1}$, and if that upper bound on primes is true for $p_1, \ldots, p_k$ then

$$p_{k+1} \leq p_1 p_2 \cdots p_k + 1 \leq 2 \cdot 2^2 \cdots 2^{2^{k-1}} + 1 = 2^{1+2+\cdots+2^{k-1}} + 1 = 2^{2^k - 1} + 1,$$

and that last number is at most $2^{2^k}$ since $\frac{1}{2}x + 1 \leq x$ for $x \geq 2$ (take $x = 2^{2^k}$).

That $p_n \leq 2^{2^{n-1}}$ for all $n \geq 1$ means the number of primes up to $2^{2^{n-1}}$ is at least $n$, so $\pi(2^{2^{n-1}}) \geq n$ for $n \geq 1$. For $x \geq 2$, choose the integer $n \geq 1$ such that $2^{n-1} \leq \log_2 x < 2^n$. Then $x \geq 2^{2^{n-1}}$, so $\pi(x) \geq \pi(2^{2^{n-1}}) \geq n > \log_2(\log_2 x)$. Since $0 < \log 2 < 1$, $\log_2(y) = (\log y)/(\log 2) > \log y$ for $y > 0$, so $\log_2(\log_2 x) > \log(\log x)$.

Second proof. In inequality (4.3), on the right side $1/(1 - 1/p) \leq 2$, so

$$\sum_{n \leq N} \frac{1}{n} < \prod_{p \leq N} \frac{1}{1 - 1/p} \leq 2^{\pi(N)}.$$

On the left side, by using a Riemann sum approximation to $\int_1^{N+1} dx/x$ with rectangles of width 1 we have

$$\sum_{n \leq N} \frac{1}{n} > \int_1^{N+1} \frac{dx}{x} = \log(N + 1).$$

<!-- page 8 -->

Therefore $\log(N + 1) < 2^{\pi(N)}$ when $N \geq 2$. For $x \geq 2$, letting $N \leq x < N + 1$ for an integer $N$, we get

$$\log x < \log(N + 1) < 2^{\pi(N)} = 2^{\pi(x)} < e^{\pi(x)},$$

so $\pi(x) > \log(\log x)$. $\square$

This lower bound $\pi(x) > \log(\log x)$ is extremely weak: the true order of magnitude of $\pi(x)$ for large $x$ is $x/\log x$, meaning that the ratio $\pi(x)/(x/\log x)$ tends to 1 as $x \to \infty$. That is called the Prime Number Theorem.

## 6. Erdos's Proof

In a footnote to a short paper [6] on divergence of the series $\sum_p 1/p$ over the primes, Erdos gave the following combinatorial proof that there are infinitely many primes.

**Theorem 6.1.** *There are infinitely many primes.*

*Proof.* Suppose there are finitely many primes $p_1, p_2, \ldots, p_r$. Each positive integer up to $N$ can be written uniquely as $a^2 b$ where $a$ is a positive integer and $b$ is squarefree. Since $a \leq \sqrt{N}$, the number of choices for $a$ is at most $\sqrt{N}$. Since $b$ is a product of distinct primes and there are $r$ primes (including an empty product for $b = 1$), the number of choices of $b$ is $2^r$. Therefore the number of possibilities for $a^2 b$ is at most $\sqrt{N} 2^r$. There are $N$ positive integers up to $N$, so $N \leq \sqrt{N} 2^r$. By algebra, $N \leq 2^{2r}$. This is a contradiction for large enough $N$. $\square$

This argument leads to an improvement on the lower bound $\pi(x) > \log(\log x)$ that we saw earlier.

**Corollary 6.2.** *For every integer $N \geq 2$, $\pi(N) > (\log N)/(2 \log 2)$.*

*Proof.* Let $r = \pi(N)$. Running through the proof of Theorem 6.1 with $p_1, \ldots, p_r$ being the set of primes up to $N$ (not the set of all primes), by writing positive integers as $a^2 b$ for squarefree $b$ we find that the number of integers up to $N$ is at most $\sqrt{N} 2^r$. Therefore $N \leq \sqrt{N} 2^r = \sqrt{N} 2^{\pi(N)}$, so $\pi(N) \geq (\log_2 N)/2 = (\log N)/(2 \log 2)$. $\square$

We can improve on the lower bound in Corollary 6.2 by using a result called Bertrand's postulate: for each integer $n \geq 2$, there is a prime number lying strictly between $n$ and $2n$.[^4]

**Theorem 6.3.** *Bertrand's postulate implies $\pi(x) > \log x$ for all $x \geq 3$.*

The inequality $\pi(x) > \log x$ is false for $e < x < 3$, where $\pi(x) = 1 < \log x$.

*Proof.* For $x \geq 8$, let $2^k \leq x < 2^{k+1}$ for an integer $k$. The $k - 1$ open intervals $(2, 4), (4, 8), (8, 16), \ldots, (2^{k-1}, 2^k)$ each contain a prime number and all of them are all less than $x$, so $\pi(x) \geq k - 1$. This lower bound on $\pi(x)$ does not include the prime 2 and for the interval $(4, 8)$ we counted just one prime in it but there are two primes in it. Therefore

$$\pi(x) \geq (k - 1) + 2 = k + 1 > \log_2 x > \log x$$

for $x \geq 8$. For $3 \leq x < 5$, $\log x < 2 \leq \pi(x)$ and for $5 \leq x \leq 8$, $\log x < 3 \leq \pi(x)$. $\square$

[^4]: The label "Bertrand's postulate" is used for historical reasons. It would be better described as Bertrand's conjecture. He conjectured it in order to prove the symmetric group $S_m$ has no subgroup with index between 2 and $m$ when $m \geq 3$ [1, p. 129]. It was later proved by Chebyshev [4, Sect. VI].

<!-- page 9 -->

## References

[1] J. Bertrand, "Memoire sur le nombre de valeurs que peut prendre une fonction quand on y permute les lettres qu'elle renferme," *J. l'Ecole Roy. Polytech.* **18** (1845), 123–140. URL <https://books.google.com/books?id=Tso6AQAAAMAJ&pg=PA123#v=onepage&q&f=false>.

[2] A. Booker, "On Mullin's second sequence of primes," *Integers* **12** (2012), 1167–1177.

[3] V. Brun, "La serie $1/5+1/7+1/11+1/13+1/17+1/19+1/29+1/31+1/41+1/43+1/59+1/61+\ldots$, ou les denominateurs sont nombres premiers jumeaux est convergente ou finie," *Bull. Sci. Math* **43** (1919), 100–104, 124–128. URL <https://gallica.bnf.fr/ark:/12148/bpt6k96292009/f104.image>.

[4] P. L. Chebyshev, "Memoire sur les nombres premiers," *J. Math. Pures et Appl.* **17** (1852), 366–390. URL <http://sites.mathdoc.fr/JMPA/PDF/JMPA_1852_1_17_A19_0.pdf>.

[5] C. D. Cox and A. J. van der Poorten, "On a sequence of prime numbers," *J. Austral. Math. Soc.* **8** (1968), 571–574.

[6] P. Erdos, "Uber die Reihe $\sum 1/p$," *Mathematica (Zutphen)* **B7** (1938), 1–2. URL <https://users.renyi.hu/~p_erdos/1938-13.pdf>.

[7] L. Euler, "Variae observationes circa series infinitas," *Commentarii academiae scientiarum Petropolitanae* **9** (1744), 160–188. URL <http://eulerarchive.maa.org/pages/E072.html>.

[8] A. A. Mullin, "Recursive function theory (A modern look at a Euclidean idea)," *Bull. Amer. Math. Soc.* **69** (1963), 737.

[9] P. Pollack and E. Trevino, "The primes that Euclid forgot," *Amer. Math. Monthly* **121** (2014), 433–437.

[10] P. Ribenboim, *The Book of Prime Number Records*, Springer-Verlag, New York, 1988.
