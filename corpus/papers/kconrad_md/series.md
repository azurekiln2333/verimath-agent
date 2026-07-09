# Infinite Series

> **Source**: [kconrad.math.uconn.edu/blurbs/analysis/series.pdf](https://kconrad.math.uconn.edu/blurbs/analysis/series.pdf)  
> **Author**: Keith Conrad  
> **Topic**: analysis

<!-- page 1 -->

## 1. Introduction

The two basic concepts of calculus, differentiation and integration, are defined in terms of limits (Newton quotients and Riemann sums). In addition to these is a third fundamental limit process: infinite series. The label *series* is just another name for a sum. An infinite series is a "sum" with infinitely many terms, such as

$$1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots + \frac{1}{n^2} + \cdots. \tag{1.1}$$

The idea of an infinite series is familiar from decimal expansions, for instance the expansion

$$\pi = 3.14159265358979\ldots$$

can be written as

$$\pi = 3 + \frac{1}{10} + \frac{4}{10^2} + \frac{1}{10^3} + \frac{5}{10^4} + \frac{9}{10^5} + \frac{2}{10^6} + \frac{6}{10^7} + \frac{5}{10^8} + \frac{3}{10^9} + \frac{5}{10^{10}} + \frac{8}{10^{11}} + \cdots,$$

so $\pi$ is an "infinite sum" of fractions. Decimal expansions like this show that an infinite series is not a paradoxical idea, although it may not be clear how to deal with non-decimal infinite series like (1.1) at the moment.

Infinite series provide two conceptual insights into the nature of the basic functions met in high school (rational functions, trigonometric and inverse trigonometric functions, exponential and logarithmic functions). First of all, these functions can be expressed in terms of infinite series, and in this way all these functions can be approximated by *polynomials*, which are the simplest kinds of functions. That simpler functions can be used as approximations to more complicated functions lies behind the method which calculators and computers use to calculate approximate values of functions. The second insight we will have using infinite series is the close relationship between functions which seem at first to be quite different, such as exponential and trigonometric functions. Two other applications we will meet are a proof by calculus that there are infinitely many primes and a proof that $e$ is irrational.

## 2. Definitions and Basic Examples

Before discussing infinite series we discuss finite ones. A finite series is a sum

$$a_1 + a_2 + a_3 + \cdots + a_N,$$

where the $a_i$'s are real numbers. In terms of $\Sigma$-notation, we write

$$a_1 + a_2 + a_3 + \cdots + a_N = \sum_{n=1}^{N} a_n.$$

<!-- page 2 -->

For example,

$$\sum_{n=1}^{N} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{N}. \tag{2.1}$$

The sum in (2.1) is called a *harmonic sum*, for instance

$$1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} = \frac{137}{60}.$$

A very important class of finite series, more important than the harmonic ones, are the *geometric series*

$$1 + r + r^2 + \cdots + r^N = \sum_{n=0}^{N} r^n. \tag{2.2}$$

An example is

$$\sum_{n=0}^{10} \left(\frac{1}{2}\right)^n = \sum_{n=0}^{10} \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^{10}} = \frac{2047}{1024} \approx 1.999023.$$

The geometric series (2.2) can be summed up exactly, as follows.

**Theorem 2.1.** *When $r \neq 1$, the series (2.2) is*

$$1 + r + r^2 + \cdots + r^N = \frac{1 - r^{N+1}}{1 - r} = \frac{r^{N+1} - 1}{r - 1}.$$

*Proof.* Let

$$S_N = 1 + r + \cdots + r^N.$$

Then

$$rS_N = r + r^2 + \cdots + r^{N+1}.$$

These sums overlap in $r + \cdots + r^N$, so subtracting $rS_N$ from $S_N$ gives

$$(1 - r)S_N = 1 - r^{N+1}.$$

When $r \neq 1$ we can divide and get the indicated formula for $S_N$. $\square$

**Example 2.2.** For any $N \geq 0$,

$$1 + 2 + 2^2 + \cdots + 2^N = \frac{2^{N+1} - 1}{2 - 1} = 2^{N+1} - 1.$$

**Example 2.3.** For any $N \geq 0$,

$$1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^N} = \frac{1 - (1/2)^{N+1}}{1 - 1/2} = 2 - \frac{1}{2^N}.$$

It is sometimes useful to adjust the indexing on a sum, for instance

$$1 + 2 \cdot 2 + 3 \cdot 2^2 + 4 \cdot 2^3 + \cdots + 100 \cdot 2^{99} = \sum_{n=1}^{100} n 2^{n-1} = \sum_{n=0}^{99} (n+1) 2^n. \tag{2.3}$$

<!-- page 3 -->

Comparing the two $\Sigma$'s in (2.3), notice how the renumbering of the indices affects the expression being summed: if we subtract 1 from the bounds of summation on the $\Sigma$ then we add 1 to the index "on the inside" to maintain the same overall sum. As another example,

$$3^2 + \cdots + 9^2 = \sum_{n=3}^{9} n^2 = \sum_{n=0}^{6} (n+3)^2.$$

Whenever the index is shifted down (or up) by a certain amount on the $\Sigma$ it has to be shifted up (or down) by a compensating amount inside the expression being summed so that we are still adding the same numbers. This is analogous to the effect of an additive change of variables in an integral, *e.g.*,

$$\int_0^1 (x+5)^2 \, dx = \int_5^6 u^2 \, du = \int_5^6 x^2 \, dx,$$

where $u = x + 5$ (and $du = dx$). When the variable inside the integral is changed by an additive constant, the bounds of integration are changed additively in the opposite direction.

Now we define the meaning of infinite series, such as (1.1). The basic idea is that we look at the sum of the first $N$ terms, called a *partial sum*, and see what happens in the limit as $N \to \infty$.

**Definition 2.4.** Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of real numbers. The *infinite series* $\sum_{n \geq 1} a_n$ is defined to be

$$\sum_{n \geq 1} a_n = \lim_{N \to \infty} \sum_{n=1}^{N} a_n.$$

If the limit exists in $\mathbf{R}$ then we say $\sum_{n \geq 1} a_n$ is *convergent*. If the limit does not exist or is $\pm\infty$ then $\sum_{n \geq 1} a_n$ is called *divergent*.

Notice that we are not really adding up all the terms in an infinite series at once. We only add up a finite number of the terms and then see how things behave in the limit as the (finite) number of terms tends to infinity: an infinite series is defined to be the limit of its sequence of partial sums.

**Example 2.5.** Using Example 2.3,

$$\sum_{n \geq 0} \frac{1}{2^n} = \lim_{N \to \infty} \sum_{n=0}^{N} \frac{1}{2^n} = \lim_{N \to \infty} 2 - \frac{1}{2^N} = 2.$$

So $\displaystyle\sum_{n \geq 0} \frac{1}{2^n}$ is a convergent series and its value is 2.

Building on this example we can compute exactly the value of any infinite geometric series.

**Theorem 2.6.** *For $x \in \mathbf{R}$, the (infinite) geometric series $\sum_{n \geq 0} x^n$ converges if $|x| < 1$ and diverges if $|x| \geq 1$. If $|x| < 1$ then*

$$\sum_{n \geq 0} x^n = \frac{1}{1 - x}.$$

*Proof.* For $N \geq 0$, Theorem 2.1 tells us

$$\sum_{n=0}^{N} x^n = \begin{cases} (1 - x^{N+1})/(1 - x), & \text{if } x \neq 1, \\ N + 1, & \text{if } x = 1. \end{cases}$$

<!-- page 4 -->

When $|x| < 1$, $x^{N+1} \to 0$ as $N \to \infty$, so

$$\sum_{n \geq 0} x^n = \lim_{N \to \infty} \sum_{n=0}^{N} x^n = \lim_{N \to \infty} \frac{1 - x^{N+1}}{1 - x} = \frac{1}{1 - x}.$$

When $|x| > 1$ the numerator $1 - x^N$ does not converge as $N \to \infty$, so $\sum_{n \geq 0} x^n$ diverges. (Specifically, the limit is $\infty$ if $x > 1$ and the partial sums oscillate between values tending to $\infty$ and $-\infty$ if $x < -1$.)

What if $|x| = 1$? If $x = 1$ then the $N$-th partial sum is $N + 1$ so the series $\sum_{n \geq 0} 1^n$ diverges (to $\infty$). If $x = -1$ then $\sum_{n=0}^{N} (-1)^n$ oscillates between 1 and 0, so again the series $\sum_{n \geq 0} (-1)^n$ is divergent. $\square$

We will see that Theorem 2.6 is the fundamental example of an infinite series. Many important infinite series will be analyzed by comparing them to a geometric series (for a suitable choice of $x$).

If we start summing a geometric series not at 1, but at a higher power of $x$, then we can still get a simple closed formula for the series, as follows.

**Corollary 2.7.** *If $|x| < 1$ and $m \geq 0$ then*

$$\sum_{n \geq m} x^n = x^m + x^{m+1} + x^{m+2} + \cdots = \frac{x^m}{1 - x}.$$

*Proof.* The $N$-th partial sum (for $N \geq m$) is

$$x^m + x^{m+1} + \cdots + x^N = x^m(1 + x + \cdots + x^{N-m}).$$

As $N \to \infty$, the sum inside the parentheses becomes the standard geometric series, whose value is $1/(1 - x)$. Multiplying by $x^m$ gives the asserted value. $\square$

**Example 2.8.** If $|x| < 1$ then $x + x^2 + x^3 + \cdots = x/(1 - x)$.

A divergent geometric series can diverge in different ways: the partial sums may tend to $\infty$ or tend to both $\infty$ and $-\infty$ or oscillate between 1 and 0. The label "divergent series" does *not* always mean the partial sums tend to $\infty$. All "divergent" means is "not convergent." Of course in a particular case we may know the partial sums do tend to $\infty$, and then we would say "the series diverges to $\infty$."

The convergence of a series is determined by the behavior of the terms $a_n$ for large $n$. If we change (or omit) any initial set of terms in a series we do not change the convergence of divergence of the series.

Here is the most basic general feature of convergent infinite series.

**Theorem 2.9.** *If the series $\sum_{n \geq 1} a_n$ converges then $a_n \to 0$ as $n \to \infty$.*

*Proof.* Let $S_N = a_1 + a_2 + \cdots + a_N$ and let $S = \sum_{n \geq 1} a_n$ be the limit of the partial sums $S_N$ as $N \to \infty$. Then as $N \to \infty$,

$$a_N = S_N - S_{N-1} \to S - S = 0. \qquad \square$$

While Theorem 2.9 is formulated for convergent series, its main importance is as a "divergence test": if the general term in an infinite series does not tend to 0 then the series diverges. For example, Theorem 2.9 gives another reason that a geometric series $\sum_{n \geq 0} x^n$ diverges if $|x| \geq 1$, because in this case $x^n$ does not tend to 0: $|x^n| = |x|^n \geq 1$ for all $n$.

<!-- page 5 -->

It is an unfortunate fact of life that the converse of Theorem 2.9 is generally false: if $a_n \to 0$ we have no guarantee that $\sum_{n \geq 0} a_n$ converges. Here is the standard illustration.

**Example 2.10.** Consider the *harmonic series* $\displaystyle\sum_{n \geq 1} \frac{1}{n}$. Although the general term $\dfrac{1}{n}$ tends to 0 it turns out that

$$\sum_{n \geq 1} \frac{1}{n} = \infty.$$

To show this we will compare $\sum_{n=1}^{N} 1/n$ with $\int_1^N dt/t = \log N$. When $n \leq t$, $1/t \leq 1/n$. Integrating this inequality from $n$ to $n + 1$ gives $\int_n^{n+1} dt/t \leq 1/n$, so

$$\sum_{n=1}^{N} \frac{1}{n} \geq \sum_{n=1}^{N} \int_n^{n+1} \frac{dt}{t} = \int_1^{N+1} \frac{dt}{t} = \log(N+1).$$

Therefore the $N$-th partial sum of the harmonic series is bounded below by $\log(N+1)$. Since $\log(N+1) \to \infty$ as $N \to \infty$, so does the $N$-th harmonic sum, so the harmonic series diverges.

We will see later that the lower bound $\log(N+1)$ for the $N$-th harmonic sum is rather sharp, so the harmonic series diverges "slowly" since the logarithm function diverges slowly.

The divergence of the harmonic series is not just a counterexample to the converse of Theorem 2.9, but can be exploited in other contexts. Let's use it to prove something about prime numbers!

**Theorem 2.11.** *There are infinitely many prime numbers.*

*Proof.* (Euler) We will argue by contradiction: assuming there are only finitely many prime numbers we will contradict the divergence of the harmonic series.

Consider the product of $1/(1 - 1/p)$ as $p$ runs through all prime numbers. Sums are denoted with a $\Sigma$ and products are denoted with a $\Pi$ (capital pi), so our product is written as

$$\prod_p \frac{1}{1 - 1/p} = \frac{1}{1 - 1/2} \cdot \frac{1}{1 - 1/3} \cdot \frac{1}{1 - 1/5} \cdots.$$

Since we assume there are finitely many primes, this is a finite product. Now expand each factor into a geometric series:

$$\prod_p \frac{1}{1 - 1/p} = \prod_p \left(1 + \frac{1}{p} + \frac{1}{p^2} + \frac{1}{p^3} + \cdots\right).$$

Each geometric series is greater than any of its partial sums. Pick any integer $N \geq 2$ and truncate each geometric series at the $N$-th term, giving the inequality

$$\prod_p \frac{1}{1 - 1/p} > \prod_p \left(1 + \frac{1}{p} + \frac{1}{p^2} + \frac{1}{p^3} + \cdots + \frac{1}{p^N}\right). \tag{2.4}$$

On the right side of (2.4) we have a finite product of finite sums, so we can compute this using the distributive law ("super FOIL" in the terminology of high school algebra). That is, take one term from each factor, multiply them together, and add up all these products. What numbers do we get in this way on the right side of (2.4)?

A product of reciprocal integers is a reciprocal integer, so we obtain a sum of $1/n$ as $n$ runs over certain positive integers. Specifically, the $n$'s we meet are those whose *prime factorization* doesn't

<!-- page 6 -->

involve any prime with exponent greater than $N$. Indeed, for any positive integer $n > 1$, if we factor $n$ into primes as

$$n = p_1^{e_1} p_2^{e_2} \cdots p_r^{e_r}$$

then $e_i < n$ for all $i$. (Since $p_i \geq 2$, $n \geq 2^{e_i}$, and $2^m > m$ for any $m \geq 0$ so $n > e_i$.) Thus if $n \leq N$ any of the prime factors of $n$ appear in $n$ with exponent less than $n \leq N$, so $1/n$ is a number which shows up when multiplying out (2.4). Here we need to know we are working with a product over all primes.

Since $1/n$ occurs in the expansion of the right side of (2.4) for $n \leq N$ and all terms in the expansion are positive, we have the lower bound estimate

$$\prod_p \frac{1}{1 - 1/p} > \sum_{n=1}^{N} \frac{1}{n}. \tag{2.5}$$

Since the left side is independent of $N$ while the right side tends to $\infty$ as $N \to \infty$, this inequality is a contradiction so there must be infinitely many primes. $\square$

We end this section with some algebraic properties of convergent series: termwise addition and scaling.

**Theorem 2.12.** *If $\sum_{n \geq 1} a_n$ and $\sum_{n \geq 1} b_n$ converge then $\sum_{n \geq 1} (a_n + b_n)$ converges and*

$$\sum_{n \geq 1} (a_n + b_n) = \sum_{n \geq 1} a_n + \sum_{n \geq 1} b_n.$$

*If $\sum_{n \geq 1} a_n$ converges then for any number $c$ the series $\sum_{n \geq 1} c a_n$ converges and*

$$\sum_{n \geq 1} c a_n = c \sum_{n \geq 1} a_n.$$

*Proof.* Let $S_N = \sum_{n=1}^{N} a_n$ and $T_N = \sum_{n=1}^{N} b_n$. Set $S = \sum_{n \geq 1} a_n$ and $T = \sum_{n \geq 1} b_n$, so $S_N \to S$ and $T_N \to T$ as $N \to \infty$. Then by known properties of limits of sequences, $S_N + T_N \to S + T$ and $c S_N \to c S$ as $N \to \infty$. These are the conclusions of the theorem. $\square$

**Example 2.13.** We have

$$\sum_{n \geq 0} \left(\frac{1}{2^n} + \frac{1}{3^n}\right) = \frac{1}{1 - 1/2} + \frac{1}{1 - 1/3} = \frac{7}{2}$$

and

$$\sum_{n \geq 0} \frac{5}{4^n} = 5 \sum_{n \geq 0} \frac{1}{4^n} = 5 \frac{1}{1 - 1/4} = \frac{20}{3}.$$

## 3. Positive Series

In this section we describe several ways to show that an infinite series $\sum_{n \geq 1} a_n$ converges when $a_n > 0$ for all $n$.

There is something special about series where all the terms are positive. What is it? The sequence of partial sums is increasing: $S_{N+1} = S_N + a_N$, so $S_{N+1} > S_N$ for every $N$. An increasing sequence has two possible limiting behaviors: it converges or it tends to $\infty$. (That is, divergence can only happen in one way: the partial sums tend to $\infty$.) We can tell if an increasing sequence converges by showing it is bounded above. Then it converges and its limit is an upper bound on the whole sequence. If the terms in an increasing sequence are not bounded above then the sequence

<!-- page 7 -->

is unbounded and tends to $\infty$. Compare this to the sequence of partial sums $\sum_{n=0}^{N} (-1)^n$, which are bounded but do not converge (they oscillate between 1 and 0).

Let's summarize this property of positive series. If $a_n > 0$ for every $n$ and there is a constant $C$ such that all partial sums satisfy $\sum_{n=1}^{N} a_n < C$ then $\sum_{n \geq 1} a_n$ converges and $\sum_{n \geq 1} a_n \leq C$. On the other hand, if there is no upper bound on the partial sums then $\sum_{n \geq 1} a_n = \infty$. We will use this over and over again to explain various convergence tests for positive series.

**Theorem 3.1 (Integral Test).** *Suppose $a_n = f(n)$ where $f$ is a continuous decreasing positive function. Then $\sum_{n \geq 1} a_n$ converges if and only if $\int_1^{\infty} f(x)\,dx$ converges.*

*Proof.* We will compare the partial sum $\sum_{n=1}^{N} a_n$ and the "partial integral" $\int_1^N f(x)\,dx$.

Since $f(x)$ is a decreasing function,

$$n \leq x \leq n+1 \implies a_{n+1} = f(n+1) \leq f(x) \leq f(n) = a_n.$$

Integrating these inequalities between $n$ and $n + 1$ gives

$$a_{n+1} \leq \int_n^{n+1} f(x)\,dx \leq a_n, \tag{3.1}$$

since the interval $[n, n+1]$ has length 1. Therefore

$$\sum_{n=1}^{N} a_n \geq \sum_{n=1}^{N} \int_n^{n+1} f(x)\,dx = \int_1^{N+1} f(x)\,dx \tag{3.2}$$

and

$$\sum_{n=1}^{N} a_n = a_1 + \sum_{n=2}^{N} a_n \leq a_1 + \sum_{n=2}^{N} \int_{n-1}^{n} f(x)\,dx = f(1) + \int_1^N f(x)\,dx. \tag{3.3}$$

Combining (3.2) and (3.3),

$$\int_1^{N+1} f(x)\,dx \leq \sum_{n=1}^{N} a_n \leq f(1) + \int_1^N f(x)\,dx. \tag{3.4}$$

Assume that $\int_1^{\infty} f(x)\,dx$ converges. Since $f(x)$ is a positive function, $\int_1^N f(x)\,dx < \int_1^{\infty} f(x)\,dx$. Thus by the second inequality in (3.4)

$$\sum_{n=1}^{N} a_n < f(1) + \int_1^{\infty} f(x)\,dx,$$

so the partial sums are bounded above. Therefore the series $\sum_{n \geq 1} a_n$ converges.

Conversely, assume $\sum_{n \geq 1} a_n$ converges. Then the partial sums $\sum_{n=1}^{N} a_n$ are bounded above (by the whole series $\sum_{n \geq 1} a_n$). Every partial integral of $\int_1^{\infty} f(x)\,dx$ is bounded above by one of these partial sums according to the first inequality of (3.4), so the partial integrals are bounded above and thus the improper integral $\int_1^{\infty} f(x)\,dx$ converges. $\square$

**Example 3.2.** We were implicitly using the integral test with $f(x) = 1/x$ when we proved the harmonic series diverges in Example 2.10. For the harmonic series, (3.4) becomes

$$\log(N+1) \leq \sum_{n=1}^{N} \frac{1}{n} \leq 1 + \log N. \tag{3.5}$$

<!-- page 8 -->

Thus the harmonic series diverges "logarithmically." The following table illustrates these bounds when $N$ is a power of 10.

| $N$ | $\log(N+1)$ | $\sum_{n=1}^{N} 1/n$ | $1 + \log N$ |
|-----|-------------|----------------------|--------------|
| 10 | 2.398 | 2.929 | 3.303 |
| 100 | 4.615 | 5.187 | 5.605 |
| 1000 | 6.909 | 7.485 | 7.908 |
| 10000 | 9.210 | 9.788 | 10.210 |

**Table 1.**

**Example 3.3.** Generalizing the harmonic series, consider

$$\sum_{n \geq 1} \frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \frac{1}{4^p} + \cdots$$

where $p > 0$. This is called a *p-series*. Its convergence is related to the integral $\int_1^{\infty} dx/x^p$. Since the integrand $1/x^p$ has an anti-derivative that can be computed explicitly, we can compute the improper integral:

$$\int_1^{\infty} \frac{dx}{x^p} = \begin{cases} \frac{1}{p-1}, & \text{if } p > 1, \\ \infty, & \text{if } 0 < p \leq 1. \end{cases}$$

Therefore $\sum_{n \geq 1} 1/n^p$ converges when $p > 1$ and diverges when $0 < p \leq 1$. For example, $\sum_{n \geq 1} 1/n^2$ converges and $\sum_{n \geq 1} 1/\sqrt{n}$ diverges.

**Example 3.4.** The series $\displaystyle\sum_{n \geq 2} \frac{1}{n \log n}$ diverges by the integral test since

$$\int_2^{\infty} \frac{dx}{x \log x} = \log\log x \bigg|_2^{\infty} = \infty.$$

(We stated the integral test with a lower bound of 1 but it obviously adapts to series where the first index of summation is something other than 1, as in this example.)

**Example 3.5.** The series $\displaystyle\sum_{n \geq 2} \frac{1}{n(\log n)^2}$, with terms just slightly smaller than in the previous example, converges. Using the integral test,

$$\int_2^{\infty} \frac{dx}{x(\log x)^2} = -\frac{1}{\log x}\bigg|_2^{\infty} = \frac{1}{\log 2},$$

which is finite.

Because the convergence of a positive series is intimately tied up with the boundedness of its partial sums, we can determine the convergence or divergence of one positive series from another if we have an inequality in one direction between the terms of the two series. This leads to the following convergence test.

**Theorem 3.6 (Comparison test).** *Let $0 < a_n \leq b_n$ for all $n$. If $\sum_{n \geq 1} b_n$ converges then $\sum_{n \geq 1} a_n$ converges. If $\sum_{n \geq 1} a_n$ diverges then $\sum_{n \geq 1} b_n$ diverges.*

<!-- page 9 -->

*Proof.* Since $0 < a_n \leq b_n$ we have

$$\sum_{n=1}^{N} a_n \leq \sum_{n=1}^{N} b_n \tag{3.6}$$

and both sequences of partial sums are increasing or stay the same (they are "nondecreasing"). If $\sum_{n \geq 1} b_n$ converges then the partial sums on the right side of (3.6) are bounded, so the partial sums on the left side are bounded, and therefore $\sum_{n \geq 1} a_n$ converges because an increasing (really, a nondecreasing) bounded sequence of real numbers converges. If $\sum_{n \geq 1} a_n$ diverges then $\sum_{n=1}^{N} a_n \to \infty$ (see the second paragraph of this section again), so $\sum_{n=1}^{N} b_n \to \infty$, so $\sum_{n \geq 1} b_n$ diverges. $\square$

**Example 3.7.** If $0 \leq x < 1$ then $\sum_{n \geq 1} x^n/n$ converges since $x^n/n \leq x^n$ so the series is bounded above by the geometric series $\sum_{n \geq 1} x^n$, which converges. Notice that, unlike the geometric series, we are *not* giving any kind of closed form expression for $\sum_{n \geq 1} x^n/n$. All we are saying is that the series converges.

The series $\sum_{n \geq 1} x^n/n$ does not converge for $x \geq 1$: if $x = 1$ it is the harmonic series and if $x > 1$ then the general term $x^n/n$ tends to $\infty$ (not 0) so the series diverges to $\infty$.

**Example 3.8.** The integral test is a special case of the comparison test, where we compare $a_n$ with $\int_n^{n+1} f(x)\,dx$ and with $\int_{n-1}^{n} f(x)\,dx$.

Just as convergence of a series does not depend on the behavior of the initial terms of the series, what is important in the comparison test is an inequality $a_n \leq b_n$ for large $n$. If this inequality happens not to hold for small $n$ but does hold for all large $n$ then the comparison test still works. The following two examples use this "extended comparison test" when the form of the comparison test in Theorem 3.6 does not strictly apply (because the inequality $a_n \leq b_n$ doesn't hold for small $n$).

**Example 3.9.** If $0 \leq x < 1$ then $\sum_{n \geq 1} nx^n$ converges. This is obvious for $x = 0$. We can't get convergence for $0 < x < 1$ by a comparison with $\sum_{n \geq 1} x^n$ because the inequality goes the wrong way: $nx^n > x^n$, so convergence of $\sum_{n \geq 1} x^n$ doesn't help us show convergence of $\sum_{n \geq 1} nx^n$. However, let's write

$$nx^n = nx^{n/2} x^{n/2}.$$

Since $0 < x < 1$, $nx^{n/2} \to 0$ as $n \to \infty$, so $nx^{n/2} \leq 1$ for large $n$ (depending on the specific value of $x$, *e.g.*, for $x = 1/2$ the inequality is false at $n = 3$ but is correct for $n \geq 4$). Thus for *all large $n$* we have $nx^n \leq x^{n/2}$ so $\sum_{n \geq 1} nx^n$ converges by comparison with the geometric series $\sum_{n \geq 1} x^{n/2} = \sum_{n \geq 1} (\sqrt{x})^n$. We have not obtained any kind of closed formula for $\sum_{n \geq 1} nx^n$, however.

If $x \geq 1$ then $\sum_{n \geq 1} nx^n$ diverges since $nx^n \geq 1$ for all $n$, so the general term does not tend to 0.

**Example 3.10.** If $x \geq 0$ then the series $\sum_{n \geq 0} x^n/n!$ converges. This is obvious for $x = 0$. For $x > 0$ we will use the comparison test and the lower bound estimate $n! > n^n/e^n$. Let's recall that this lower bound on $n!$ comes from Euler's integral formula

$$n! = \int_0^{\infty} t^n e^{-t}\,dt > \int_n^{\infty} t^n e^{-t}\,dt > n^n \int_n^{\infty} e^{-t}\,dt = \frac{n^n}{e^n}.$$

Then for positive $x$

$$\frac{x^n}{n!} < \frac{x^n}{n^n/e^n} = \left(\frac{ex}{n}\right)^n. \tag{3.7}$$

<!-- page 10 -->

Here $x$ is fixed and we should think about what happens as $n$ grows. The ratio $ex/n$ tends to 0 as $n \to \infty$, so for large $n$ we have

$$\frac{ex}{n} < \frac{1}{2} \tag{3.8}$$

(any positive number less than 1 will do here; we just use $1/2$ for concreteness). Raising both sides of (3.8) to the $n$-th power,

$$\left(\frac{ex}{n}\right)^n < \frac{1}{2^n}.$$

Comparing this to (3.7) gives $x^n/n! < 1/2^n$ for large $n$, so the terms of the series $\sum_{n \geq 0} x^n/n!$ drop off faster than the terms of the convergent geometric series $\sum_{n \geq 0} 1/2^n$ when we go out far enough. The extended comparison test now implies convergence of $\sum_{n \geq 0} x^n/n!$ if $x > 0$.

**Example 3.11.** The series $\displaystyle\sum_{n \geq 1} \frac{1}{5n^2 + n}$ converges since $\dfrac{1}{5n^2 + n} < \dfrac{1}{5n^2}$ and $\displaystyle\sum_{n \geq 1} \frac{1}{5n^2}$ converges by Example 3.3.

Let's try to apply the comparison test to $\sum_{n \geq 1} 1/(5n^2 - n)$. The rate of growth of the $n$th term is like $1/(5n^2)$, but the inequality now goes the wrong way:

$$\frac{1}{5n^2} < \frac{1}{5n^2 - n}$$

for all $n$. So we can't quite use the comparison test to show $\sum_{n \geq 1} 1/(5n^2 - n)$ converges (which it does). The following limiting form of the comparison test will help here.

**Theorem 3.12 (Limit comparison test).** *Let $a_n, b_n > 0$ and suppose the ratio $a_n/b_n$ has a positive limit. Then $\sum_{n \geq 1} a_n$ converges if and only if $\sum_{n \geq 1} b_n$ converges.*

*Proof.* Let $L = \lim_{n \to \infty} a_n/b_n$. For all large $n$,

$$\frac{L}{2} < \frac{a_n}{b_n} < 2L,$$

so

$$\frac{L}{2} b_n < a_n < 2L b_n \tag{3.9}$$

for large $n$. Since $L/2$ and $2L$ are positive, the convergence of $\sum_{n \geq 1} b_n$ is the same as convergence of $\sum_{n \geq 1} (L/2)b_n$ and $\sum_{n \geq 1} (2L)b_n$. Therefore the first inequality in (3.9) and the comparison test show convergence of $\sum_{n \geq 1} a_n$ implies convergence of $\sum_{n \geq 1} b_n$. The second inequality in (3.9) and the comparison test show convergence of $\sum_{n \geq 1} b_n$ implies convergence of $\sum_{n \geq 1} a_n$. (Although (3.9) may not be true for all $n$, it is true for large $n$, and that suffices to apply the extended comparison test.) $\square$

The way to use the limit comparison test is to replace terms in a series by simpler terms which grow at the same rate (at least up to a scaling factor). Then analyze the series with those simpler terms.

**Example 3.13.** We return to $\displaystyle\sum_{n \geq 1} \frac{1}{5n^2 - n}$. As $n \to \infty$, the $n$th term grows like $1/5n^2$:

$$\frac{1/(5n^2 - n)}{1/5n^2} \to 1.$$

<!-- page 11 -->

Since $\sum_{n \geq 1} 1/(5n^2)$ converges, so does $\sum_{n \geq 1} 1/(5n^2 - n)$. In fact, if $a_n$ is any sequence whose growth is like $1/n^2$ up to a scaling factor then $\sum_{n \geq 1} a_n$ converges. In particular, this is a *simpler* way to settle the convergence in Example 3.11 than by using the inequalities in Example 3.11.

**Example 3.14.** To determine if

$$\sum_{n \geq 1} \sqrt{\frac{n^3 - n^2 + 5n}{4n^6 + n}}$$

converges we replace the $n$th term with the expression

$$\sqrt{\frac{n^3}{4n^6}} = \frac{1}{2n^{3/2}},$$

which grows at the same rate. The series $\sum_{n \geq 1} 1/(2n^{3/2})$ converges, so the original series converges.

The limit comparison test underlies an important point: the convergence of a series $\sum_{n \geq 1} a_n$ is not assured just by knowing if $a_n \to 0$, but it is assured if $a_n \to 0$ rapidly enough. That is, the *rate* at which $a_n$ tends to 0 is often (but not always) a means of explaining the convergence of $\sum_{n \geq 1} a_n$. The difference between someone who has an intuitive feeling for convergence of series and someone who can only determine convergence on a case-by-case basis using memorized rules in a mechanical way is probably indicated by how well the person understands the connection between convergence of a series and rates of growth (really, decay) of the terms in the series. Armed with the convergence of a few basic series (like geometric series and $p$-series), the convergence of most other series encountered in a calculus course can be determined by the limit comparison test if you understand well the rates of growth of the standard functions. One exception is if the series has a log term, in which case it might be useful to apply the integral test.

## 4. Series with Mixed Signs

All our previous convergence tests apply to series with positive terms. They also apply to series whose terms are eventually positive (just omit any initial negative terms to get a positive series) or eventually negative (negate the series, which doesn't change the convergence status, and now we're reduced to an eventually positive series). What do can we do for series whose terms are not eventually all positive or eventually all negative? These are the series with infinitely many positive terms and infinitely many negative terms.

**Example 4.1.** Consider the alternating harmonic series

$$\sum_{n \geq 1} \frac{(-1)^{n-1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \cdots.$$

The usual harmonic series diverges, but the alternating signs might have different behavior. The following table collects some of the partial sums.

| $N$ | $\sum_{n=1}^{N} (-1)^{n-1}/n$ |
|-----|-------------------------------|
| 10 | .6456 |
| 100 | .6882 |
| 1000 | .6926 |
| 10000 | .6930 |

**Table 2.**

<!-- page 12 -->

These partial sums are not clear evidence in favor of convergence: after 10,000 terms we only get *apparent stability* in the first 2 decimal digits. The harmonic series diverges slowly, so perhaps the alternating harmonic series diverges too (and slower).

**Definition 4.2.** An infinite series where the terms alternate in sign is called an *alternating series*.

An alternating series starting with a positive term can be written as $\sum_{n \geq 1} (-1)^{n-1} a_n$ where $a_n > 0$ for all $n$. If the first term is negative then a reasonable general notation is $\sum_{n \geq 1} (-1)^n a_n$ where $a_n > 0$ for all $n$. Obviously negating an alternating series of one type turns it into the other type.

**Theorem 4.3 (Alternating series test).** *An alternating series whose $n$-th term in absolute value tends monotonically to 0 as $n \to \infty$ is a convergent series.*

*Proof.* We will work with alternating series which have an initial positive term, so of the form $\sum_{n \geq 1} (-1)^{n-1} a_n$. Since successive partial sums alternate adding and subtracting an amount which, in absolute value, steadily tends to 0, the relation between the partial sums is indicated by the following inequalities:

$$s_2 < s_4 < s_6 < \cdots < s_5 < s_3 < s_1.$$

In particular, the even-indexed partial sums are an increasing sequence which is bounded above (by $s_1$, say), so the partial sums $s_{2m}$ converge. Since $|s_{2m+1} - s_{2m}| = |a_{2m+1}| \to 0$, the odd-indexed partial sums converge to the same limit as the even-indexed partial sums, so the sequence of all partial sums has a single limit, which means $\sum_{n \geq 1} (-1)^{n-1} a_n$ converges. $\square$

**Example 4.4.** The alternating harmonic series $\displaystyle\sum_{n \geq 1} \frac{(-1)^{n-1}}{n}$ converges.

**Example 4.5.** While the $p$-series $\sum_{n \geq 1} 1/n^p$ converges only for $p > 1$, the alternating $p$-series $\sum_{n \geq 1} (-1)^{n-1}/n^p$ converges for the wider range of exponents $p > 0$ since it is an alternating series satisfying the hypotheses of the alternating series test.

**Example 4.6.** We saw $\sum_{n \geq 1} x^n/n$ converges for $0 \leq x < 1$ (comparison to the geometric series) in Example 3.7. If $-1 \leq x < 0$ then $\sum_{n \geq 1} x^n/n$ converges by the alternating series test: the negativity of $x^n$ makes the terms $x^n/n$ alternate in sign. To apply the alternating series test we need

$$\left|\frac{x^{n+1}}{n+1}\right| < \left|\frac{x^n}{n}\right|$$

for all $n$, which is equivalent after some algebra to

$$|x| < \frac{n+1}{n}$$

for all $n$, and this is true since $|x| \leq 1 < (n+1)/n$.

**Example 4.7.** In Example 3.10 the series $\sum_{n \geq 0} x^n/n!$ was seen to converge for $x \geq 0$. If $x < 0$ the series is an alternating series. Does it fit the hypotheses of the alternating series test? We need

$$\left|\frac{x^{n+1}}{(n+1)!}\right| < \left|\frac{x^n}{n!}\right|$$

for all $n$, which is equivalent to

$$|x| < n + 1$$

<!-- page 13 -->

for all $n$. For each particular $x < 0$ this may not be true for all $n$ (if $x = -3$ it fails for $n = 1$ and 2), but it is definitely true for all sufficiently large $n$. Therefore the terms of $\sum_{n \geq 0} x^n/n!$ are an "eventually alternating" series. Since what matters for convergence is the long-term behavior and not the initial terms, we can apply the alternating series test to see $\sum_{n \geq 0} x^n/n!$ converges by just ignoring an initial piece of the series.

When a series has infinitely many positive and negative terms which are not strictly alternating, convergence may not be easy to check. For example, the trigonometric series

$$\sum_{n \geq 1} \frac{\sin(nx)}{n} = \sin x + \frac{\sin(2x)}{2} + \frac{\sin(3x)}{3} + \frac{\sin(4x)}{4} + \cdots$$

turns out to be convergent for every number $x$, but the arrangement of positive and negative terms in this series can be quite subtle in terms of $x$. The proof that this series converges uses the technique of summation by parts, which won't be discussed here.

While it is generally a delicate matter to show a non-alternating series with mixed signs converges, there is one useful property such series might have which does imply convergence. It is this: if the series with all terms made positive converges then so does the original series. Let's give this idea a name and then look at some examples.

**Definition 4.8.** A series $\sum_{n \geq 1} a_n$ is *absolutely convergent* if $\sum_{n \geq 1} |a_n|$ converges.

Don't confuse $\sum_{n \geq 1} |a_n|$ with $|\sum_{n \geq 1} a_n|$; absolute convergence refers to convergence if we drop the signs from the *terms* in the series, not from the series overall. The difference between $\sum_{n \geq 1} a_n$ and $|\sum_{n \geq 1} a_n|$ is at most a single sign, while there is a substantial difference between $\sum_{n \geq 1} a_n$ and $\sum_{n \geq 1} |a_n|$ if the $a_n$'s have many mixed signs; that is the difference which absolute convergence involves.

**Example 4.9.** We saw $\sum_{n \geq 1} x^n/n$ converges if $0 \leq x < 1$ in Example 3.7. Since $|x^n/n| = |x|^n/n$, the series $\sum_{n \geq 1} x^n/n$ is absolutely convergent if $|x| < 1$. Note the alternating harmonic series $\sum_{n \geq 1} (-1)^{n-1}/n$ is *not* absolutely convergent, however.

**Example 4.10.** In Example 3.10 we saw $\sum_{n \geq 0} x^n/n!$ converges for all $x \geq 0$. Since $|x^n/n!| = |x|^n/n!$, the series $\sum_{n \geq 0} x^n/n!$ is absolutely convergent for all $x$.

**Example 4.11.** By Example 3.9, $\sum_{n \geq 1} nx^n$ converges absolutely if $|x| < 1$.

**Example 4.12.** The two series

$$\sum_{n \geq 1} \frac{\sin(nx)}{n^2}, \quad \sum_{n \geq 1} \frac{\cos(nx)}{n^2},$$

where the $n$th term has denominator $n^2$, are absolutely convergent for any $x$ since the absolute value of the $n$th term is at most $1/n^2$ and $\sum_{n \geq 1} 1/n^2$ converges.

The relevance of absolute convergence is two-fold: 1) we can use the many convergence tests for positive series to determine if a series is absolutely convergent, and 2) absolute convergence implies ordinary convergence.

We just illustrated the first point several times. Let's show the second point.

**Theorem 4.13 (Absolute convergence test).** *Every absolutely convergent series is a convergent series.*

<!-- page 14 -->

*Proof.* We give two proofs. The first one, which is simpler, exploits special features of real numbers. The second proof can be applied in more general settings that use infinite series of numbers other than real numbers (*e.g.*, infinite series of complex numbers or infinite series of functions).

<u>First proof:</u> For all $n$ we have

$$-|a_n| \leq a_n \leq |a_n|,$$

so

$$0 \leq a_n + |a_n| \leq 2|a_n|.$$

Since $\sum_{n \geq 1} |a_n|$ converges, so does $\sum_{n \geq 1} 2|a_n|$ (to twice the value). Therefore by the *comparison test* we obtain convergence of $\sum_{n \geq 1} (a_n + |a_n|)$. Subtracting $\sum_{n \geq 1} |a_n|$ from this shows $\sum_{n \geq 1} a_n$ converges.

<u>Second proof:</u> To show $\sum_{n \geq 1} a_n$ converges, we want to show the partial sums

$$s_N = a_1 + a_2 + \cdots + a_N$$

have a limit. We will show the sequence of partial sums $\{s_N\}$ is a Cauchy sequence: for all $\varepsilon > 0$ there is a positive integer $M$ such that if $N, N' \geq M$ then $|s_N - s_{N'}| < \varepsilon$.

Since $\sum_{n \geq 1} |a_n|$ is assumed to converge, the partial sums

$$t_N = |a_1| + |a_2| + \cdots + |a_N|$$

form a Cauchy sequence: for all $\varepsilon > 0$ there is a positive integer $M$ such that if $N, N' \geq M$ then $|t_N - t_{N'}| < \varepsilon$. Taking $N \geq N'$ without loss of generality, we have $|t_N - t_{N'}| = |a_{N'+1}| + \cdots + |a_N|$, so

$$N \geq N' \geq M \implies |a_{N'+1}| + \cdots + |a_N| < \varepsilon.$$

Thus

$$N \geq N' \geq M \implies |s_N - s_{N'}| = |a_{N'+1} + \cdots + a_N| \leq |a_{N'+1}| + \cdots + |a_N| = |t_N - t_{N'}| < \varepsilon,$$

so $\{s_N\}$ is a Cauchy sequence and therefore it converges in $\mathbf{R}$. $\square$

We can now say the series $\sum_{n \geq 1} x^n/n$ and $\sum_{n \geq 1} nx^n$ converge for $|x| < 1$ and $\sum_{n \geq 0} x^n/n!$ converges for all $x$ by our treatment of these series for positive $x$ alone in Section 3. The argument we gave in Examples 4.6 and 4.7 for the convergence of $\sum_{n \geq 1} x^n/n$ and $\sum_{n \geq 1} x^n/n!$ when $x < 0$, using the alternating series test, can be avoided. (But we do need the alternating series test to show $\sum_{n \geq 1} x^n/n$ converges at $x = -1$.)

**Corollary 4.14.** *If $|a_n| \leq b_n$ and $\sum_{n \geq 1} b_n$ converges then $\sum_{n \geq 1} a_n$ converges.*

*Proof.* By the comparison test (Theorem 3.6), convergence of $\sum_{n \geq 1} b_n$ implies convergence of $\sum_{n \geq 1} |a_n|$, and by Theorem 4.13 $\sum_{n \geq 1} a_n$ converges. $\square$

A series which converges but is not absolutely convergent is called *conditionally convergent*. An example of a conditionally convergent series is the alternating harmonic series $\sum_{n \geq 1} (-1)^{n-1}/n$.

The distinction between absolutely convergent series and conditionally convergent series might seem kind of minor, since it involves whether or not a particular convergence test (the absolute convergence test) works on that series. But the distinction is actually profound, and is nicely illustrated by the following example of Dirichlet (1837).

**Example 4.15.** Let $L = 1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 + \cdots$ be the alternating harmonic series. Consider the *rearrangement* of the terms where we follow a positive term by two negative terms:

$$1 - \frac{1}{2} - \frac{1}{4} + \frac{1}{3} - \frac{1}{6} - \frac{1}{8} + \frac{1}{5} - \frac{1}{10} - \frac{1}{12} + \cdots$$

<!-- page 15 -->

If we add each positive term to the negative term following it, we obtain

$$\frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \frac{1}{10} - \frac{1}{12} + \cdots,$$

which is precisely half the alternating harmonic series (multiply $L$ by $1/2$ and see what you get termwise). Therefore, by rearranging the terms of the alternating harmonic series we obtained a new series whose sum is $(1/2)L$ instead of $L$. If $(1/2)L = L$, doesn't that mean $1 = 2$? What happened?

This example shows addition of terms in an infinite series is *not* generally commutative, unlike with finite series. In fact, this feature is characteristic of the conditionally convergent series, as seen in the following amazing theorem.

**Theorem 4.16 (Riemann, 1854).** *If an infinite series is conditionally convergent then it can be rearranged to sum up to any desired value. If an infinite series is absolutely convergent then all of its rearrangements converge to the same sum.*

For instance, the alternating harmonic series can be rearranged to sum up to 1, to $-5.673$, to $\pi$, or to any other number you wish. That we rearranged it in Example 4.15 to sum up to half its usual value was special only in the sense that we could make the rearrangement achieving that effect quite explicit.

Theorem 4.16, whose proof we omit, is called Riemann's rearrangement theorem. It indicates that absolutely convergent series are better behaved than conditionally convergent ones. The ordinary rules of algebra for finite series generally extend to absolutely convergent series but not to conditionally convergent series.

## 5. Power Series

The simplest functions are polynomials: $c_0 + c_1 x + \cdots + c_d x^d$. In differential calculus we learn how to locally approximate many functions by linear functions (the tangent line approximation). We now introduce an idea which will let us give an exact representation of functions in terms of "polynomials of infinite degree." The precise name for this idea is a power series.

**Definition 5.1.** A *power series* is a function of the form $f(x) = \sum_{n \geq 0} c_n x^n$.

For instance, a polynomial is a power series where $c_n = 0$ for large $n$. The geometric series $\sum_{n \geq 0} x^n$ is a power series. It only converges for $|x| < 1$. We have also met other power series, like

$$\sum_{n \geq 1} \frac{x^n}{n}, \quad \sum_{n \geq 1} nx^n, \quad \sum_{n \geq 0} \frac{x^n}{n!}.$$

These three series converge on the respective intervals $[-1, 1)$, $(-1, 1)$ and $(-\infty, \infty)$.

For any power series $\sum_{n \geq 0} c_n x^n$ it is a basic task to find those $x$ where the series converges. It turns out in general, as in all of our examples, that a power series converges on an interval. Let's see why.

**Theorem 5.2.** *If a power series $\sum_{n \geq 0} c_n x^n$ converges at $x = b \neq 0$ then it converges absolutely for $|x| < |b|$.*

*Proof.* Since $\sum_{n \geq 0} c_n b^n$ converges the general term tends to 0, so $|c_n b^n| \leq 1$ for large $n$. If $|x| < |b|$ then

$$|c_n x^n| = |c_n b^n| \left|\frac{x}{b}\right|^n,$$

<!-- page 16 -->

which is at most $|x/b|^n$ for large $n$. The series $\sum_{n \geq 0} |x/b|^n$ converges since it's a geometric series and $|x/b| < 1$. Therefore by the (extended) comparison test $\sum_{n \geq 0} |c_n x^n|$ converges, so $\sum_{n \geq 0} c_n x^n$ is absolutely convergent. $\square$

**Example 5.3.** If a power series converges at $-7$ then it converges on the interval $(-7, 7)$. We can't say for sure how it converges at 7.

**Example 5.4.** If a power series diverges at $-7$ then it diverges for $|x| > 7$: if it were to converge at a number $x$ where $|x| > 7$ then it would converge in the interval $(-|x|, |x|)$ so in particular at $-7$, a contradiction.

What these two examples illustrate, as consequences of Theorem 5.2, is that the values of $x$ where a power series $\sum_{n \geq 0} c_n x^n$ converges is an interval centered at 0, so of the form

$$(-r, r), \quad [-r, r), \quad (-r, r], \quad [-r, r]$$

for some $r$. We call $r$ the *radius of convergence* of the power series. The only difference between these different intervals is the presence or absence of the endpoints. All possible types of *interval of convergence* can occur: $\sum_{n \geq 0} x^n$ has interval of convergence $(-1, 1)$, $\sum_{n \geq 1} x^n/n$ has interval of convergence $[-1, 1)$, $\sum_{n \geq 1} (-1)^n x^n/n$ has interval of convergence $(-1, 1]$ and $\sum_{n \geq 1} x^n/n^2$ (a new example we have not met before) has interval of convergence $[-1, 1]$.

The radius of convergence and the interval of convergence are closely related but should not be confused. The interval is the actual set where the power series converges. The radius is simply the half-length of this set (and doesn't tell us whether or not the endpoints are included). If we don't care about convergence behavior on the boundary of the interval of convergence than we can get by just knowing the radius of convergence: the series always converges (absolutely) on the inside of the interval of convergence.

For the practical computation of the radius of convergence in basic examples it is convenient to use a new convergence test for positive series.

**Theorem 5.5 (Ratio test).** *If $a_n > 0$ for all $n$, assume*

$$q = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$$

*exists. If $q < 1$ then $\sum_{n \geq 1} a_n$ converges. If $q > 1$ then $\sum_{n \geq 1} a_n$ diverges. If $q = 1$ then no conclusion can be drawn.*

*Proof.* Assume $q < 1$. Pick $s$ between $q$ and 1: $q < s < 1$. Since $a_{n+1}/a_n \to q$, we have $a_{n+1}/a_n < s$ for all large $n$, say for $n \geq n_0$. Then $a_{n+1} < s a_n$ when $n \geq n_0$, so

$$a_{n_0+1} < s a_{n_0}, \quad a_{n_0+2} < s a_{n_0+1} < s^2 a_{n_0}, \quad a_{n_0+3} < s a_{n_0+2} < s^3 a_{n_0},$$

and more generally $a_{n_0+k} < s^k a_{n_0}$ for any $k \geq 0$. Writing $n_0 + k$ as $n$ we have

$$n \geq n_0 \implies a_n < s^{n-n_0} a_{n_0} = \frac{a_{n_0}}{s^{n_0}} s^n.$$

Therefore when $n \geq n_0$ the number $a_n$ is bounded above by a constant multiple of $s^n$. Hence $\sum_{n \geq 1} a_n$ converges by comparison to a constant multiple of the convergent geometric series $\sum_{n \geq 1} s^n$.

In the other direction, if $q > 1$ then pick $s$ with $1 < s < q$. An argument similar to the previous one shows $a_n$ grows at least as quickly as a constant multiple of $s^n$, but this time $\sum_{n \geq 1} s^n$ diverges since $s > 1$. So $\sum_{n \geq 1} a_n$ diverges too.

When $q = 1$ we can't make a definite conclusion since both $\sum_{n \geq 1} 1/n$ and $\sum_{n \geq 1} 1/n^2$ have $q = 1$. $\square$

<!-- page 17 -->

**Example 5.6.** We give a proof that $\sum_{n \geq 1} nx^n$ has radius of convergence 1 which is shorter than Examples 3.9 and 4.11. Take $a_n = |nx^n| = n|x|^n$. Then

$$\frac{a_{n+1}}{a_n} = \frac{n+1}{n}|x| \to |x|$$

as $n \to \infty$. Thus if $|x| < 1$ the series $\sum_{n \geq 1} nx^n$ is absolutely convergent by the ratio test. If $|x| > 1$ this series is divergent. Notice the ratio test does *not* tell us what happens to $\sum_{n \geq 1} nx^n$ when $|x| = 1$; we have to check $x = 1$ and $x = -1$ individually.

**Example 5.7.** A similar argument shows $\sum_{n \geq 1} x^n/n$ has radius of convergence 1 since

$$\frac{|x^{n+1}/(n+1)|}{|x^n/n|} = \frac{n}{n+1}|x| \to |x|$$

as $n \to \infty$.

**Example 5.8.** We show the series $\sum_{n \geq 0} x^n/n!$ converges absolutely for all $x$. Using the ratio test we look at

$$\frac{|x^{n+1}/(n+1)!|}{|x^n/n!|} = \frac{|x|}{n+1} \to 0$$

as $n \to \infty$. Since this limit is less than 1 for all $x$, we are done by the ratio test. The radius of convergence is infinite.

Power series are important for two reasons: they give us much greater flexibility to define new kinds of functions and many standard functions can be expressed in terms of a power series.

Intuitively, if a known function $f(x)$ has a power series representation on some interval around 0, say

$$f(x) = \sum_{n \geq 0} c_n x^n = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + c_4 x^4 + \cdots$$

for $|x| < r$, then we can guess a formula for $c_n$ in terms of the behavior of $f(x)$. To begin we have

$$f(0) = c_0.$$

Now we think about power series as something like "infinite degree polynomials." We know how to differentiate a polynomial by differentiating each power of $x$ separately. Let's *assume* this works for power series too in the interval of convergence:

$$f'(x) = \sum_{n \geq 1} n c_n x^{n-1} = c_1 + 2c_2 x + 3c_3 x^2 + 4c_4 x^3 + \cdots,$$

so we expect

$$f'(0) = c_1.$$

Now let's differentiate again:

$$f''(x) = \sum_{n \geq 2} n(n-1) c_n x^{n-2} = 2c_2 + 6c_3 x + 12c_4 x^2 + \cdots,$$

so

$$f''(0) = 2c_2.$$

Differentiating a third time (formally) and setting $x = 0$ gives

$$f^{(3)}(0) = 6c_3.$$

The general rule appears to be

$$f^{(n)}(0) = n! c_n,$$

<!-- page 18 -->

so we should have

$$c_n = \frac{f^{(n)}(0)}{n!}.$$

This procedure really is valid, according to the following theorem whose long proof is omitted.

**Theorem 5.9.** *Any function represented by a power series in an open interval $(-r, r)$ is infinitely differentiable in $(-r, r)$ and its derivatives can be computed by termwise differentiation of the power series.*

This means our previous calculations are justified: *if* a function $f(x)$ can be written in the form $\sum_{n \geq 0} c_n x^n$ in an interval around 0 then we *must* have

$$c_n = \frac{f^{(n)}(0)}{n!}. \tag{5.1}$$

In particular, a function has at most *one* expression as a power series $\sum_{n \geq 0} c_n x^n$ around 0. And a function which is not infinitely differentiable around 0 will definitely not have a power series representation $\sum_{n \geq 0} c_n x^n$. For instance, $|x|$ has no power series representation of this form since it is not differentiable at 0.

**Remark 5.10.** We can also consider power series $f(x) = \sum_{n \geq 0} c_n(x - a)^n$, whose interval of convergence is centered at $a$. In this case the coefficients are given by the formula $c_n = f^{(n)}(a)/n!$. For simplicity we will focus on power series "centered at 0" only.

**Remark 5.11.** Even if a power series converges on a closed interval $[-r, r]$, the power series for its derivative need not converge at the endpoints. Consider $f(x) = \sum_{n \geq 1} (-1)^n x^{2n}/n$. It converges for $|x| \leq 1$ but the derivative series is $\sum_{n \geq 1} 2(-1)^n x^{2n-1}$, which converges for $|x| < 1$.

**Remark 5.12.** Because a power series can be differentiated (*inside* its interval of convergence) termwise, we can discover solutions to a differential equation by inserting a power series with unknown coefficients into the differential equation to get relations between the coefficients. Then a few initial coefficients, once chosen, should determine all the higher ones. After we compute the radius of convergence of this new power series we will have found a solution to the differential equation in a specific interval. This idea goes back to Newton. It does not necessarily provide us with all solutions to a differential equation, but it is one of the standard methods to find some solutions.

**Example 5.13.** If $|x| < 1$ then $\displaystyle\sum_{n \geq 0} x^n = \frac{1}{1 - x}$. Differentiating both sides, for $|x| < 1$ we have

$$\sum_{n \geq 1} nx^{n-1} = \frac{1}{(1 - x)^2}.$$

Multiplying by $x$ gives us

$$\sum_{n \geq 1} nx^n = \frac{x}{(1 - x)^2},$$

so we have finally found a "closed form" expression for an infinite series we first met back in Example 3.9.

<!-- page 19 -->

**Example 5.14.** If there is a power series representation $\sum_{n \geq 0} c_n x^n$ for $e^x$ then (5.1) shows $c_n = 1/n!$. The only possible way to write $e^x$ as a power series is

$$\sum_{n \geq 0} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots.$$

Is this really a valid formula for $e^x$? Well, we checked before that this power series converges for all $x$. Moreover, calculating the derivative of this series reproduces the series again, so this series is a function satisfying $y'(x) = y(x)$. The only solutions to this differential equation are $Ce^x$ and we can recover $C$ by setting $x = 0$. Since the power series has constant term 1 (so its value at $x = 0$ is 1), its $C$ is 1, so this power series is $e^x$:

$$e^x = \sum_{n \geq 0} \frac{x^n}{n!}.$$

Loosely speaking, this means the polynomials

$$1, \quad 1 + x, \quad 1 + x + \frac{x^2}{2}, \quad 1 + x + \frac{x^2}{2} + \frac{x^3}{6}, \ldots$$

are good approximations to $e^x$. (Where they are good will depend on how far $x$ is from 0.) In particular, setting $x = 1$ gives an infinite series representation of the number $e$:

$$e = \sum_{n \geq 0} \frac{1}{n!} = 1 + \frac{1}{2} + \frac{1}{3!} + \frac{1}{4!} + \cdots. \tag{5.2}$$

Formula (5.2) can be used to verify an interesting fact about $e$.

**Theorem 5.15.** *The number $e$ is irrational.*

*Proof.* (Fourier) For any $n$,

$$\begin{aligned} e &= \left(1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!}\right) + \left(\frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \cdots\right) \\ &= \left(1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!}\right) + \frac{1}{n!}\left(\frac{1}{n+1} + \frac{1}{(n+2)(n+1)} + \cdots\right). \end{aligned}$$

The second term in parentheses is positive and bounded above by the geometric series

$$\frac{1}{n+1} + \frac{1}{(n+1)^2} + \frac{1}{(n+1)^3} + \cdots = \frac{1}{n}.$$

Therefore

$$0 < e - \left(1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!}\right) \leq \frac{1}{n \cdot n!}.$$

Write the sum $1 + 1/2! + \cdots + 1/n!$ as a fraction with common denominator $n!$, say as $p_n/n!$. Clear the denominator $n!$ to get

$$0 < n!e - p_n \leq \frac{1}{n}. \tag{5.3}$$

So far everything we have done involves no unproved assumptions. Now we introduce the rationality assumption. If $e$ is rational, then $n!e$ is an integer when $n$ is large (since any integer is a factor by $n!$ for large $n$). But that makes $n!e - p_n$ an integer located in the open interval $(0, 1)$, which is absurd. We have a contradiction, so $e$ is irrational. $\square$

<!-- page 20 -->

We return to the general task of representing functions by their power series. Even when a function is infinitely differentiable for all $x$, its power series could have a finite radius of convergence.

**Example 5.16.** Viewing $1/(1 + x^2)$ as $1/(1 - (-x^2))$ we have the geometric series formula

$$\frac{1}{1 + x^2} = \sum_{n \geq 0} (-x^2)^n = \sum_{n \geq 0} (-1)^n x^{2n}$$

when $|-x^2| < 1$, or equivalently $|x| < 1$. The series has a finite interval of convergence $(-1, 1)$ even though the function $1/(1 + x^2)$ has no bad behavior at the endpoints: it is infinitely differentiable at every real number $x$.

**Example 5.17.** Let $f(x) = \sum_{n \geq 1} x^n/n$. This converges for $-1 \leq x < 1$. For $|x| < 1$ we have

$$f'(x) = \sum_{n \geq 1} x^{n-1} = \sum_{n \geq 0} x^n = \frac{1}{1 - x}.$$

When $|x| < 1$, an antiderivative of $1/(1 - x)$ is $-\log(1 - x)$. Since $f(x)$ and $-\log(1 - x)$ have the same value (zero) at $x = 0$ they are equal:

$$-\log(1 - x) = \sum_{n \geq 1} \frac{x^n}{n}$$

for $|x| < 1$. Replacing $x$ with $-x$ and negating gives

$$\log(1 + x) = \sum_{n \geq 1} \frac{(-1)^{n-1}}{n} x^n \tag{5.4}$$

for $|x| < 1$. The right side converges at $x = 1$ (alternating series) and diverges at $x = -1$. It seems plausible, since the series equals $\log(1 + x)$ on $(-1, 1)$, that this should remain true at the boundary: does $\sum_{n \geq 1} (-1)^{n-1}/n$ equal $\log 2$? (Notice this is the alternating harmonic series.) We will return to this later.

In practice, if we want to show an infinitely differentiable function equals its associated power series $\sum_{n \geq 0} (f^{(n)}(0)/n!)x^n$ on some interval around 0 we need some kind of error estimate for the difference between $f(x)$ and the polynomial $\sum_{n=0}^{N} (f^{(n)}(0)/n!)x^n$. When the estimate goes to 0 as $N \to \infty$ we will have proved $f(x)$ is equal to its power series.

**Theorem 5.18.** *If $f(x)$ is infinitely differentiable then for all $N \geq 0$*

$$f(x) = \sum_{n=0}^{N} \frac{f^{(n)}(0)}{n!} x^n + R_N(x),$$

*where*

$$R_N(x) = \frac{1}{N!} \int_0^x f^{(N+1)}(t)(x - t)^N \, dt.$$

*Proof.* When $N = 0$ the desired result says

$$f(x) = f(0) + \int_0^x f'(t)\,dt.$$

This is precisely the fundamental theorem of calculus!

<!-- page 21 -->

We obtain the $N = 1$ case from this by integration by parts. Set $u = f'(t)$ and $dv = dt$. Then $du = f''(t)\,dt$ and we (cleverly!) take $v = t - x$ (rather than just $t$). Then

$$\begin{aligned} \int_0^x f'(t)\,dt &= f'(t)(t - x)\bigg|_{t=0}^{t=x} - \int_0^x f''(t)(t - x)\,dt \\ &= f'(0)x + \int_0^x f''(t)(x - t)\,dt, \end{aligned}$$

so

$$f(x) = f(0) + f'(0)x + \int_0^x f''(t)(x - t)\,dt.$$

Now apply integration by parts to this new integral with $u = f''(t)$ and $dv = (x - t)\,dt$. Then $du = f^{(3)}(t)\,dt$ and (cleverly) use $v = -(1/2)(x - t)^2$. The result is

$$\int_0^x f''(t)(x - t)\,dt = \frac{f''(0)}{2}x^2 + \frac{1}{2}\int_0^x f^{(3)}(t)(x - t)^2\,dt,$$

so

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{1}{2}\int_0^x f^{(3)}(t)(x - t)^2\,dt.$$

Integrating by parts several more times gives the desired result. $\square$

We call $R_N(x)$ a *remainder term*.

**Corollary 5.19.** *If $f$ is infinitely differentiable then the following conditions at the number $x$ are equivalent:*

- *$f(x) = \sum_{n \geq 0} (f^{(n)}(0)/n!)x^n$,*
- *$R_N(x) \to 0$ as $N \to \infty$.*

*Proof.* The difference between $f(x)$ and the $N$th partial sum of its power series is $R_N(x)$, so $f(x)$ equals its power series precisely when $R_N(x) \to 0$ as $N \to \infty$. $\square$

**Example 5.20.** In (5.4) we showed $\log(1 + x)$ equals $\sum_{n \geq 1} (-1)^{n-1} x^n/n$ for $|x| < 1$. What about at $x = 1$? For this purpose we want to show $R_N(1) \to 0$ as $N \to \infty$ when $f(x) = \log(1 + x)$. To estimate $R_N(1)$ we need to compute the higher derivatives of $f(x)$:

$$f'(x) = \frac{1}{1+x}, \quad f''(x) = -\frac{1}{(1+x)^2}, \quad f^{(3)}(x) = \frac{2}{(1+x)^3}, \quad f^{(4)}(x) = -\frac{6}{(1+x)^4},$$

and in general

$$f^{(n)}(x) = \frac{(-1)^{n-1}(n-1)!}{(1+x)^n}$$

for $n \geq 1$. Therefore

$$R_N(1) = \frac{1}{N!} \int_0^1 \frac{(-1)^N N!}{(1+t)^{N+1}}(1-t)^N\,dt = (-1)^N \int_0^1 \frac{(1-t)^N}{(1+t)^{N+1}}\,dt,$$

so

$$\begin{aligned} |R_N(1)| &\leq \int_0^1 \frac{dt}{(1+t)^{N+1}} \\ &= \frac{1}{N} - \frac{1}{N 2^N} \\ &\to 0 \end{aligned}$$

as $N \to \infty$. Since the remainder term tends to 0, $\log 2 = \sum_{n \geq 1} (-1)^{n-1}/n$.

<!-- page 22 -->

**Example 5.21.** Let $f(x) = \sin x$. Its power series is

$$\sum_{n \geq 0} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots,$$

which converges for all $x$ by the ratio test. We will show $\sin x$ equals its power series for all $x$. This is obvious if $x = 0$.

Since $\sin x$ has derivatives $\pm\cos x$ and $\pm\sin x$, which are bounded by 1, for $x > 0$

$$\begin{aligned} |R_N(x)| &= \frac{1}{N!}\left|\int_0^x f^{(N+1)}(t)(x - t)^N\,dt\right| \\ &\leq \frac{1}{N!}\int_0^x |x - t|^N\,dt \\ &\leq \frac{1}{N!}\int_0^x x^N\,dt \\ &= \frac{x^{N+1}}{N!}. \end{aligned}$$

This tends to 0 as $N \to \infty$, so $\sin x$ does equal its power series for $x > 0$.

If $x < 0$ then we can similarly estimate $|R_N(x)|$ and show it tends to 0 as $N \to \infty$, but we can also use a little trick because we know $\sin x$ is an odd function: if $x < 0$ then $-x > 0$ so

$$\sin x = -\sin(-x) = -\sum_{n \geq 0} (-1)^n \frac{(-x)^{2n+1}}{(2n+1)!}$$

from the power series representation of the sine function at positive numbers. Since $(-x)^{2n+1} = -x^{2n+1}$,

$$\sin x = -\sum_{n \geq 0} (-1)^n \frac{-x^{2n+1}}{(2n+1)!} = \sum_{n \geq 0} (-1)^n \frac{x^{2n+1}}{(2n+1)!},$$

which shows $\sin x$ equals its power series for $x < 0$ too.

**Example 5.22.** By similar work we can show $\cos x$ equals its power series representation everywhere:

$$\cos x = \sum_{n \geq 0} (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots.$$

The power series for $\sin x$ and $\cos x$ look like the odd and even degree terms in the power series for $e^x$. Is the exponential function related to the trigonometric functions? This idea is suggested because of their power series. Since $e^x$ has a series without the $(-1)^n$ factors, we can get a match between these series by working not with $e^x$ but with $e^{ix}$, where $i$ is a square root of $-1$. We have not defined infinite series (or even the exponential function) using complex numbers. However, assuming we could make sense of this then we would expect to have

$$\begin{aligned} e^{ix} &= \sum_{n \geq 0} \frac{(ix)^n}{n!} \\ &= 1 + ix - \frac{x^2}{2!} - i\frac{x^3}{3!} + \frac{x^4}{4!} + i\frac{x^5}{5!} + \cdots \\ &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots + i\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right) \\ &= \cos x + i\sin x. \end{aligned}$$

<!-- page 23 -->

For example, setting $x = \pi$ would say

$$e^{i\pi} = -1.$$

Replacing $x$ with $-x$ in the formula for $e^{ix}$ gives

$$e^{-ix} = \cos x - i\sin x.$$

Adding and subtracting the formulas for $e^{ix}$ and $e^{-ix}$ lets us express the real trigonometric functions $\sin x$ and $\cos x$ in terms of (complex) exponential functions:

$$\cos x = \frac{e^{ix} + e^{-ix}}{2}, \quad \sin x = \frac{e^{ix} - e^{-ix}}{2i}.$$

Evidently a deeper study of infinite series should make systematic use of complex numbers!

The following question is natural: who needs all the remainder estimate business from Theorem 5.18 and Corollary 5.19? After all, why not just *compute* the power series for $f(x)$ and find its radius of convergence? That has to be where $f(x)$ equals its power series. Alas, this is *false*.

**Example 5.23.** Let

$$f(x) = \begin{cases} e^{-1/x^2}, & \text{if } x \neq 0, \\ 0, & \text{if } x = 0. \end{cases}$$

It can be shown that $f(x)$ is infinitely differentiable at $x = 0$ and $f^{(n)}(0) = 0$ for all $n$, so the power series for $f(x)$ has every coefficient equal to 0, which means the power series is the zero function. But $f(x) \neq 0$ if $x \neq 0$, so $f(x)$ is *not* equal to its power series *anywhere* except at $x = 0$.

Example 5.23 shows that if a function $f(x)$ is infinitely differentiable for all $x$ and the power series $\sum_{n \geq 0} (f^{(n)}(0)/n!)x^n$ converges for all $x$, $f(x)$ need not equal its power series *anywhere* except at $x = 0$ (where they must agree since the constant term of the power series is $f(0)$). This is why there is non-trivial content in saying a function can be represented by its power series on some interval. The need for remainder estimates in general is important.
