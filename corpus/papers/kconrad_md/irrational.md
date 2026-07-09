# Irrationality of $\pi$ and $e$

> **Source**: https://kconrad.math.uconn.edu/blurbs/analysis/irrational.pdf
> **Author**: Keith Conrad
> **Topic**: analysis

<!-- page 1 -->

## 1. Introduction

Numerical estimates for $\pi$ have been found in records of several ancient civilizations. These estimates were all based on inscribing and circumscribing regular polygons around a circle to get upper and lower bounds on the area (and thus upper and lower bounds on $\pi$ after dividing the area by the square of the radius). Such estimates are accurate to a few decimal places. Around 1600, Ludolph van Ceulen gave an estimate for $\pi$ to 35 decimal places. He spent many years of his life on this calculation, using a polygon with $2^{62}$ sides!

With the advent of calculus in the 17-th century, a new approach to the calculation of $\pi$ became available: infinite series. For instance, if we integrate

$$
\frac{1}{1 + t^2} = 1 - t^2 + t^4 - t^6 + t^8 - t^{10} + \cdots, \quad -1 < t < 1
$$

from $t = 0$ to $t = x$ when $-1 < x < 1$, then we find

$$
\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \frac{x^9}{9} - \frac{x^{11}}{11} + \cdots.
\tag{1.1}
$$

This is also true at $x = 1$, and since $\arctan 1 = \pi/4$, we get

$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \cdots,
\tag{1.2}
$$

a result found by Leibniz in 1673 [2, pp. 247-248] and over 100 years earlier in India [9].[^1] Despite the beauty of (1.2), which expresses $\pi$ in terms of the odd numbers, it converges far too slowly to be numerically useful. For example, truncating the series at 1000 terms and multiplying by 4 gives the estimate $\pi \approx 3.1405$, which is only good to two decimal places.

Other formulas for $\pi$ in terms of arctan values are (see Appendix C for details)

$$
\begin{aligned}
\frac{\pi}{4} &= \arctan\frac{1}{2} + \arctan\frac{1}{3} \\
&= 2\arctan\frac{1}{3} + \arctan\frac{1}{7} \\
&= 4\arctan\frac{1}{5} - \arctan\frac{1}{239}.
\end{aligned}
$$

The series in (1.1) converges more rapidly when $x$ is smaller, so these other formulas lead to good estimates of $\pi$. The last such calculation before computers was by Shanks [10] in 1873. He claimed to get $\pi$ to 707 places. In the 1940s, the first computer estimate for $\pi$ showed Shanks made an error in the 528-th digit, so his further calculations were wrong!

Our interest here is not to ponder ever more elaborate methods of estimating $\pi$, but to prove something about the *structure* of this number: it is irrational. That is, $\pi$ is not a ratio of integers. The idea of the proof is to argue by contradiction. This is also the

[^1]: In 1671, Gregory discovered (1.1), but there is no indication he saw it gives a formula for $\pi$ at $x = 1$.

<!-- page 2 -->

principle behind the simpler proof that the number $\sqrt{2}$ is irrational. However, there is an essential difference between proofs that $\sqrt{2}$ is irrational and proofs that $\pi$ is irrational. One can prove $\sqrt{2}$ is irrational using only algebraic manipulations with a hypothetical rational expression for $\sqrt{2}$ to reach a contradiction. But all known proofs of the irrationality of $\pi$ are based on techniques from calculus, which can be used to prove irrationality of other numbers, such as $e$ and rational powers of $e$ (aside from $e^0 = 1$).

The remaining sections are organized as follows. In Section 2, we prove $\pi$ is irrational with definite integrals. Irrationality of $e$ is proved by infinite series in Section 3. A general discussion about irrationality proofs is in Section 4, and we apply those ideas to prove irrationality of nonzero rational powers of $e$ in Section 5. In Section 6 we introduce complex numbers into a proof from Section 5 in order to obtain another proof that $\pi$ is irrational.

## 2. Irrationality of $\pi$

The first proof that $\pi$ is irrational is due to Lambert [7] in 1761. His proof involves an analytic device that is not covered in calculus courses: continued fractions. (A discussion of this work is in [5, pp. 68--78].) The irrationality proof for $\pi$ we give here is due to Niven [8] and uses integrals instead of continued fractions.

**Theorem 2.1.** *The number $\pi$ is irrational.*

*Proof.* For a nice function $f(x)$, a double integration by parts shows

$$
\int f(x) \sin x \, \mathrm{d}x = -f(x) \cos x + f'(x) \sin x - \int f''(x) \sin x \, \mathrm{d}x.
$$

Therefore (using $\sin(0) = 0$, $\cos(0) = 1$, $\sin(\pi) = 0$, and $\cos(\pi) = -1$),

$$
\int_0^\pi f(x) \sin x \, \mathrm{d}x = (f(0) + f(\pi)) - \int_0^\pi f''(x) \sin x \, \mathrm{d}x.
$$

In particular, if $f(x)$ is a polynomial of even degree, say $2n$, then repeating this calculation $n$ times (or reasoning by induction) gives us

$$
\int_0^\pi f(x) \sin x \, \mathrm{d}x = F(0) + F(\pi),
\tag{2.1}
$$

where $F(x) = f(x) - f''(x) + f^{(4)}(x) - \cdots + (-1)^n f^{(2n)}(x)$.

To prove $\pi$ is irrational, we argue by contradiction. Assume $\pi = p/q$ for positive integers $p$ and $q$ (since $\pi > 0$). We are going to apply (2.1) to a carefully (and mysteriously!) chosen polynomial $f(x)$ and wind up with an integer that lies between 0 and 1. No such integer exists, so we have a contradiction and therefore $\pi$ is irrational.

For a positive integer $n$, set

$$
f_n(x) = q^n \frac{x^n(\pi - x)^n}{n!} = \frac{x^n(p - qx)^n}{n!}.
\tag{2.2}
$$

This polynomial of degree $2n$ depends on $n$ (and on $\pi$!). We are going to apply (2.1) to this polynomial and find a contradiction when $n$ becomes large.

Before working out the consequences of (2.1) for $f(x) = f_n(x)$, we note the polynomial $f_n(x)$ has two important properties:

- for $0 < x < \pi$, $f_n(x)$ is positive and (when $n$ is large) very small,
- all the derivatives of $f_n(x)$ at $x = 0$ and $x = \pi$ are integers.

<!-- page 3 -->

To show the first property is true, the positivity of $f_n(x)$ for $0 < x < \pi$ is immediate from its defining formula. To bound $f_n(x)$ from above when $0 < x < \pi$, note that $0 < \pi - x < \pi$, so $0 < x(\pi - x) < \pi^2$. Therefore

$$
0 < f_n(x) \le q^n \left(\frac{\pi^{2n}}{n!}\right) = \frac{(q\pi^2)^n}{n!}.
\tag{2.3}
$$

The upper bound tends to 0 as $n \to \infty$, so the upper bound is less than 1 for large $n$.

To show the second property is true, first take $x = 0$. The coefficient of $x^j$ in $f_n(x)$ is $f_n^{(j)}(0)/j!$. Since $f_n(x) = x^n(p - qx)^n/n!$ and $p$ and $q$ are integers, the binomial theorem tells us the coefficient of $x^j$ can also be written as $c_j/n!$ for an integer $c_j$. Therefore

$$
f_n^{(j)}(0) = \frac{j!}{n!} c_j.
\tag{2.4}
$$

Since $f_n(x)$ has its lowest degree nonvanishing term in degree $n$, $c_j = 0$ for $j < n$, so $f_n^{(j)}(0) = 0$ for $j < n$. For $j \ge n$, $j!/n!$ is an integer, so $f_n^{(j)}(0)$ is an integer by (2.4).

To see the derivatives of $f_n(x)$ at $x = \pi$ are also integers, we use the identity $f_n(\pi - x) = f_n(x)$. Differentiate both sides $j$ times and set $x = 0$ to get $(-1)^j f_n^{(j)}(\pi) = f_n^{(j)}(0)$ for all $j$. Therefore, since the right side is an integer, the left side is an integer too. This concludes the proof of the two important properties of $f_n(x)$.

Now look at (2.1) when $f = f_n$. All derivatives of $f_n$ at 0 and $\pi$ are integers, so the right side of (2.1) is an integer when $f = f_n$ (see the definition of $F(x)$). Thus $\int_0^\pi f_n(x) \sin x \, \mathrm{d}x$ is an integer for each $n$. Since $f_n(x)$ and $\sin x$ are positive on $(0, \pi)$, this integral is a positive integer. However, when $n$ is large, $|f_n(x) \sin x| \le |f_n(x)| \le (q\pi^2)^n/n!$ by (2.3). As $n \to \infty$, $(q\pi^2)^n/n! \to 0$. Therefore $\int_0^\pi f_n(x) \sin x \, \mathrm{d}x$ is a positive integer less than 1 when $n$ is very large. This is a contradiction, so $\pi$ is irrational. $\square$

This proof is quite puzzling. How did Niven choose the polynomials $f_n(x)$ or know to compute the integral (2.1)? Here is a reworking of Niven's proof in terms of recursions, due to Markov and Zhou [15].

*Proof.* Set

$$
I_n = \int_0^\pi \frac{(x(\pi - x))^n}{n!} \sin x \, \mathrm{d}x.
\tag{2.5}
$$

The integrand is continuous and positive on $(0, \pi)$, so $I_n > 0$. By explicit calculation, $I_0 = 2$ and $I_1 = 4$:

$$
I_0 = \int_0^\pi \sin x \, \mathrm{d}x = -\cos x \Big|_0^\pi = -(-1) + 1 = 2
$$

and using integration by parts,

$$
\begin{aligned}
I_1 &= \int_0^\pi (\pi x - x^2) \sin x \, \mathrm{d}x \\
&= \pi \int_0^\pi x \sin x \, \mathrm{d}x - \int_0^\pi x^2 \sin x \, \mathrm{d}x \\
&= \pi(-x \cos x + \sin x)\Big|_0^\pi - (-x^2 \cos x + 2x \sin x + 2 \cos x)\Big|_0^\pi \\
&= \pi(-\pi(-1) - 0) - ((-\pi^2(-1) + 0 - 2) - 2) \\
&= 4.
\end{aligned}
$$

<!-- page 4 -->

Using integration by parts twice, for $n \ge 2$ we have $I_n = (4n - 2)I_{n-1} - \pi^2 I_{n-2}$. (This is worked out in Appendix A.) Using that recursion and the initial values $I_0 = 2$ and $I_1 = 4$, explicit values of $I_n$ for small $n$ can be worked out. The table below gives results for $n \le 6$.

| $n$ | $I_n$ |
|-----|-------|
| 0 | 2 |
| 1 | 4 |
| 2 | $-2\pi^2 + 24$ |
| 3 | $-24\pi^2 + 240$ |
| 4 | $2\pi^4 - 360\pi^2 + 3360$ |
| 5 | $60\pi^4 - 6720\pi^2 + 60480$ |
| 6 | $-2\pi^6 + 1680\pi^4 - 151200\pi^2 + 1330560$ |

This suggests we can always write $I_n$ in the form

$$
I_n = c_{n,n}\pi^n + c_{n-1,n}\pi^{n-1} + \cdots + c_{1,n}\pi + c_{0,n}.
\tag{2.6}
$$

for some integers $c_{0,n}, \ldots, c_{n,n}$, and it's left to the reader to prove this by induction using the recursion for $I_n$ and its first two values.

Now assume $\pi$ is rational, so $\pi = p/q$ for some positive integers $p$ and $q$. By (2.6), $q^n I_n = \sum_{k=0}^n c_{k,n} q^n \pi^k = \sum_{k=0}^n c_{k,n} q^{n-k} p^k \in \mathbf{Z}$. Since $I_n > 0$, we have $q^n I_n \in \mathbf{Z}^+$. At the same time, since $|x(\pi - x)| \le \pi^2$ for $0 \le x \le \pi$ we have the bound $|q^n I_n| \le q^n \int_0^\pi ((\pi^2)^n/n!) \, \mathrm{d}x = \pi((q\pi^2)^n/n!)$, so $I_n \to 0$ as $n \to \infty$. This contradicts $q^n I_n$ being a positive integer for all $n$, so we have a contradiction. Thus $\pi$ is irrational. $\square$

## 3. Irrationality of $e$

We turn now to a proof that $e$ is irrational. This was first established by Euler [3] in 1737 using continued fractions. We will prove the irrationality in a more direct manner, using infinite series, by an argument of Fourier from 1815.[^2]

**Theorem 3.1.** *The number $e$ is irrational.*

*Proof.* Write

$$
e = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots.
$$

For a positive integer $n$,

$$
\begin{aligned}
e &= \left(1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!}\right) + \left(\frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \cdots\right) \\
&= \left(1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!}\right) + \frac{1}{n!}\left(\frac{1}{n+1} + \frac{1}{(n+2)(n+1)} + \cdots\right).
\end{aligned}
$$

The second term in parentheses is positive and less than the geometric series

$$
\frac{1}{n+1} + \frac{1}{(n+1)^2} + \frac{1}{(n+1)^3} + \cdots = \frac{1}{n}.
$$

Therefore

$$
0 < e - \left(1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!}\right) < \frac{1}{n \cdot n!}.
\tag{3.1}
$$

[^2]: While the proof of Fourier appeared in [13, pp. 339-341] in 1815, it was not written by him. It is attributed to Fourier right after the proof.

<!-- page 5 -->

Write $1 + 1 + 1/2! + \cdots + 1/n!$ in (3.1) as a fraction with common denominator $n!$: it is $p_n/n!$ with $p_n \in \mathbf{Z}$, so (3.1) says $0 < e - p_n/n! < 1/(n \cdot n!)$. Clear the denominator $n!$ to get

$$
0 < n!e - p_n < \frac{1}{n}.
\tag{3.2}
$$

So far everything we have done involves no unproved assumptions. Now we introduce the rationality assumption. If $e$ is rational, then $e = a/b$ for positive integers $a$ and $b$, and $n!e = n!a/b = (n!/b)a$ is an integer when $n$ is large, since $n!/b$ is an integer once $n \ge b$. That makes $n!e - p_n = (n!/b)a - p_n$ an integer inside the open interval $(0, 1/n)$ by (3.2), which is absurd since $1/n \le 1$. We have a contradiction, so $e$ is irrational. $\square$

**Remark 3.2.** We can prove Theorem 3.1 in a manner similar to the second proof of irrationality of $\pi$, by using the integrals

$$
J_n = \int_0^1 \frac{(x(1-x))^n}{n!} e^x \, \mathrm{d}x,
\tag{3.3}
$$

which are positive since the integrand is positive when $0 < x < 1$. If $0 \le x \le 1$, then $0 \le x(1-x) \le 1$ and $e^x \le e$, so $J_n \le \int_0^1 (e/n!) \, \mathrm{d}x \le e/n!$. We have $J_0 = e - 1$, $J_1 = -e + 3$, and $J_n = -(4n-2)J_{n-1} + J_{n-2}$ for $n \ge 2$ using integration by parts (see Appendix A for details). Further values are $J_2 = 7e - 19$ and $J_3 = -71e + 193$. Quite generally, $J_n = a_n e + b_n$ for some integers $a_n$ and $b_n$, so if $e$ is rational with $e = p/q$ for some $p$ and $q$ in $\mathbf{Z}^+$, then $qJ_n = a_n p + b_n q$ is an integer for all $n$. It's positive since $q$ and $J_n$ are, and $qJ_n < qe/n!$, which is less than 1 for large $n$. Thus $qJ_n$ is an integer between 0 and 1 for large $n$, which is a contradiction.

## 4. General Ideas

It's time to think more systematically. A basic principle we need to understand is that numbers can be proved to be irrational if they can be approximated "too well" by rationals. Of course each number can be approximated arbitrarily closely by rational numbers: use a truncated decimal expansion. For instance, we can approximate $\sqrt{2} = 1.41421356\ldots$ by

$$
\frac{14142}{10000} = 1.4142, \quad \frac{1414213}{1000000} = 1.414213.
\tag{4.1}
$$

With truncated decimals, we achieve close estimates at the expense of rather large denominators. To see what this is all about, compare the above approximations with

$$
\frac{99}{70} = 1.41428571\ldots, \quad \frac{1393}{985} = 1.41421319\ldots,
\tag{4.2}
$$

where we have achieved just as close an approximation with much smaller denominators (*e.g.*, the second one is accurate to 6 decimal places with a denominator of only 3 digits). These rational approximations to $\sqrt{2}$ are, in the sense of denominators, much better than the ones we find from decimal truncation.

To measure the "quality" of an approximation of a real number $\alpha$ by a rational number $p/q$, we should think not about the difference $|\alpha - p/q|$ being small in an absolute sense, but about the difference being substantially smaller than $1/q$ (thus tying the error with the size of the denominator in the approximation). In other words, we want

$$
\frac{|\alpha - p/q|}{1/q} = q\left|\alpha - \frac{p}{q}\right| = |q\alpha - p|
$$

to be small in an absolute sense.

<!-- page 6 -->

Measuring the approximation of $\alpha$ by $p/q$ using $|q\alpha - p|$ rather than $|\alpha - p/q|$ admittedly takes some getting used to, if you are new to the idea. Consider what it says about our approximations to $\sqrt{2}$. For example, from (4.1) we have

$$
|10000\sqrt{2} - 14142| = .135623, \quad |1000000\sqrt{2} - 1414213| = .562373,
$$

and these are not small when measured against $1/10000 = .0001$ or $1/1000000 = .000001$. On the other hand, from the approximations to $\sqrt{2}$ in (4.2) we have

$$
|70\sqrt{2} - 99| = .005050, \quad |985\sqrt{2} - 1393| = .000358,
$$

which are small when measured against $1/70 = .014285$ and $1/985 = .001015$. We see vividly that $99/70$ and $1393/985$ really should be judged as "good" rational approximations to $\sqrt{2}$ while the decimal truncations are "bad" rational approximations to $\sqrt{2}$.

The importance of this point of view is that it gives us a general *strategy* for proving numbers are irrational, as follows.

**Theorem 4.1.** *Let $\alpha \in \mathbf{R}$. If there is a sequence of integers $p_n, q_n$ such that $q_n \alpha - p_n \ne 0$ and $|q_n \alpha - p_n| \to 0$ as $n \to \infty$, then $\alpha$ is irrational.*

In other words, if $\alpha$ admits a "very good" sequence of rational approximations, then $\alpha$ must be irrational.

*Proof.* Since $0 < |q_n \alpha - p_n| < 1$ for large $n$, by hypothesis, we must have $q_n \ne 0$ for large $n$. Therefore, since only large $n$ is what matters, we may change terms at the start and assume $q_n \ne 0$ for all $n$.

To prove $\alpha$ is irrational, suppose it is rational: $\alpha = a/b$, where $a$ and $b$ are integers with $b \ne 0$. Then

$$
\left|\alpha - \frac{p_n}{q_n}\right| = \left|\frac{a}{b} - \frac{p_n}{q_n}\right| = \left|\frac{q_n a - p_n b}{b q_n}\right|.
$$

Clearing the denominator $q_n$,

$$
|q_n \alpha - p_n| = \left|\frac{q_n a - p_n b}{b}\right|.
$$

Since this is not zero, the integer $q_n a - p_n b$ is nonzero. Therefore $|q_n a - p_n b| \ge 1$, so

$$
|q_n \alpha - p_n| \ge \frac{1}{|b|}.
$$

This positive lower bound contradicts $|q_n \alpha - p_n|$ tending to 0, so $\alpha$ is irrational. $\square$

It turns out the condition in Theorem 4.1 is not just sufficient to prove irrationality, but it is also necessary: if $\alpha$ is irrational then there is a sequence of integers $p_n, q_n$ such that $|q_n \alpha - p_n|$ is not zero and tends to 0 as $n \to \infty$. We will not have a need for this necessity (except maybe for its psychological boost) and therefore omit the proof. See [6, p. 277].

Of course, to use Theorem 4.1 to prove irrationality of a number $\alpha$ we need to *find* the integers $p_n$ and $q_n$. For the number $e$, these integers can be found directly from truncations to the infinite series for $e$, as we saw in (3.2). In other words, rather than saying $e$ is irrational because the proof of Theorem 3.1 shows in the end that rationality of $e$ leads to an integer between 0 and 1, we can say $e$ is irrational because the proof of Theorem 3.1 exhibits a sequence of good rational approximations to $e$. In other words, the proof of Theorem 3.1 can stop at (3.2) and then appeal to Theorem 4.1.

<!-- page 7 -->

While other powers of $e$ are also irrational, it is not feasible to prove their irrationality by adapting the proof of Theorem 3.1. For instance, what happens if we try to prove $e^2$ is irrational from taking truncations of the infinite series $e^2 = \sum_{k \ge 0} 2^k/k!$? Writing the truncated sum $\sum_{k=0}^n 2^k/k!$ in reduced form as, say, $a_n/b_n$, numerical data suggest $b_n e^2 - a_n$ does *not* tend to 0. (For example, the value of $b_n e^2 - a_n$ at $n = 22, 23$, and $24$ is roughly .0026, 1.4488, and .3465. Since the corresponding values of $b_n$ have 12, 16, and 17 decimal digits, these differences are not small by comparison with $1/b_n$, so the approximations $a_n/b_n$ to $e^2$ are not that good.) Thus, these rational approximations to $e^2$ probably won't fit the conditions of Theorem 4.1 to let us prove the irrationality of $e^2$. (However, a well-chosen *subsequence* of the partial sums does work. See Appendix B.)

## 5. Irrationality of Rational Powers of $e$

To find good rational approximations to positive integral powers of $e$ (good enough, that is, to establish irrationality of those powers), we will not use a series expansion, but rather use the interaction between $e^x$ and integration. Some of the mysterious ideas from Niven's proof of the irrationality of $\pi$ will show up in this context.

We will use Theorem 4.1 to prove the following generalization of the irrationality of $e$.

**Theorem 5.1.** *For every positive integer $a$, $e^a$ is irrational.*

Before we prove Theorem 5.1, we note two immediate corollaries.

**Corollary 5.2.** *When $r$ is a nonzero rational number, $e^r$ is irrational.*

*Proof.* Since $e^{-r} = 1/e^r$, it suffices to take $r > 0$. Then $r = a/b$ for positive integers $a$ and $b$. If $e^r$ is rational, so is $(e^r)^b = e^a$, but this contradicts Theorem 5.1. Thus $e^r$ is irrational. $\square$

**Corollary 5.3.** *For each positive rational number $r \ne 1$, $\ln r$ is irrational.*

*Proof.* The number $\ln r$ is nonzero. If $\ln r$ is rational, then Corollary 5.2 tells us $e^{\ln r}$ is irrational. But $e^{\ln r} = r$ is rational. We have a contradiction, so $\ln r$ is irrational. $\square$

The proof of Theorem 5.1 will use the following lemma, which tells us how to integrate $e^{-x} f(x)$ when $f(x)$ is a polynomial.

**Lemma 5.4 (Hermite).** *Let $f(x)$ be a polynomial of degree $m \ge 0$. For every real number $a > 0$,*

$$
\int_0^a e^{-x} f(x) \, \mathrm{d}x = \sum_{j=0}^{m} f^{(j)}(0) - e^{-a} \sum_{j=0}^{m} f^{(j)}(a).
$$

*Proof.* We compute $\int e^{-x} f(x) \, \mathrm{d}x$ by integration by parts, taking $u = f(x)$ and $\mathrm{d}v = e^{-x} \mathrm{d}x$. Then $\mathrm{d}u = f'(x) \mathrm{d}x$ and $v = -e^{-x}$, so

$$
\int e^{-x} f(x) \, \mathrm{d}x = -e^{-x} f(x) + \int e^{-x} f'(x) \, \mathrm{d}x.
$$

Repeating this process on the new indefinite integral, we eventually obtain

$$
\int e^{-x} f(x) \, \mathrm{d}x = -e^{-x} \sum_{j=0}^{m} f^{(j)}(x).
$$

Now evaluate the right side at $x = a$ and $x = 0$ and subtract. $\square$

<!-- page 8 -->

**Remark 5.5.** It is interesting to make a special case of this lemma explicit: for $f(x) = x^n$,

$$
\int_0^a e^{-x} x^n \, \mathrm{d}x = n! - \frac{1}{e^a} \sum_{j=0}^{n} n(n-1)\cdots(n-j+1) a^{n-j}.
$$

Letting $a \to \infty$ ($n$ is fixed), the second term on the right tends to 0, so $\int_0^\infty e^{-x} x^n \, \mathrm{d}x = n!$. This integral formula for $n!$ is due to Euler.

Now we prove Theorem 5.1.

*Proof.* Rewrite Hermite's lemma (Lemma 5.4) by multiplying through by $e^a$:

$$
e^a \int_0^a e^{-x} f(x) \, \mathrm{d}x = e^a \sum_{j=0}^{m} f^{(j)}(0) - \sum_{j=0}^{m} f^{(j)}(a).
\tag{5.1}
$$

Equation (5.1) is valid for every positive number $a$ and polynomial $f(x)$. Let $a$ be a positive integer at which $e^a$ is assumed to be rational. We want to use for $f(x)$ a polynomial (actually, a sequence of polynomials $f_n(x)$) with two properties:

- the left side of (5.1) is positive and (when $n$ is large) very small,
- all the derivatives of the polynomial at $x = 0$ and $x = a$ are integers.

Then the right side of (5.1) will have the properties of the differences $q_n \alpha - p_n$ in Theorem 4.1, with $\alpha = e^a$ and the two sums on the right side of (5.1) being $p_n$ and $q_n$.

Our choice of $f(x)$ is

$$
f_n(x) = \frac{x^n(x - a)^n}{n!},
\tag{5.2}
$$

where $n \ge 1$ is to be determined. (Note the similarity with (2.2) in the proof of the irrationality of $\pi$!) In other words, we consider the equation

$$
e^a \int_0^a e^{-x} f_n(x) \, \mathrm{d}x = e^a \sum_{j=0}^{2n} f_n^{(j)}(0) - \sum_{j=0}^{2n} f_n^{(j)}(a).
\tag{5.3}
$$

We can see (5.3) is positive by looking at the left side. The number $a$ is positive and the integrand $e^{-x} f_n(x) = e^{-x} x^n(x-a)^n/n!$ on the interval $(0, a)$ is positive, so the integral is positive. Now we estimate the size of (5.3) by estimating the integral on the left side. By the change of variables $x = ay$ on the left side of (5.3),

$$
\int_0^a e^{-x} f_n(x) \, \mathrm{d}x = a^{2n+1} \int_0^1 e^{-ay} \frac{y^n(y-1)^n}{n!} \, \mathrm{d}y,
$$

so we can bound the left side of (5.3) from above by

$$
0 < e^a \int_0^a e^{-x} f_n(x) \, \mathrm{d}x \le \frac{e^a a^{2n+1}}{n!} \int_0^1 e^{-ay} \, \mathrm{d}y.
$$

As a function of $n$, this upper bound is a constant times $(a^2)^n/n!$. As $n \to \infty$, this bound tends to 0.

To see that, for each integer $n \ge 1$, the derivatives $f_n^{(j)}(0)$ and $f_n^{(j)}(a)$ are integers for every $j \ge 0$, first note that the equation $f_n(a - x) = f_n(x)$ tells us after repeated differentiation that $(-1)^j f_n^{(j)}(a) = f_n^{(j)}(0)$. Therefore it suffices to show all the derivatives of $f_n(x)$ at $x = 0$ are integers. The proof that all $f_n^{(j)}(0)$ are integers is just like that in the proof of Theorem 2.1, so the details are left to the reader to check. (The general principle is this:

<!-- page 9 -->

for a polynomial $g(x)$ that has integer coefficients and is divisible by $x^n$, all derivatives of $g(x)/n!$ at $x = 0$ are integers.)

The first property of the $f_n$'s tells us that $q_n e^a - p_n$ is positive, where $p_n = \sum_{j=0}^{2n} f_n^{(j)}(a)$ and $q_n = \sum_{j=0}^{2n} f_n^{(j)}(a)$, and $q_n e^a - p_n$ tends to 0 as $n \to \infty$. The second property of the $f_n$'s tells us that $p_n$ and $q_n$ are integers. Therefore the hypotheses of Theorem 4.1 are met, so $e^a$ is irrational. $\square$

What really happened in this proof? We actually wrote down some very good rational approximations to $e^a$. They came from values of the polynomial

$$
F_n(x) = \sum_{j=0}^{2n} f_n^{(j)}(x).
$$

Indeed, Theorem 5.1 tells us $F_n(a)/F_n(0)$ is a "good" rational approximation to $e^a$ when $n$ is large. (The dependence of $F_n(x)$ on $a$ is hidden in the formula for $f_n(x)$.) The following table illustrates this for $a = 2$, where the entry at $n = 1$ is pretty bad since $F_1(0) = 0$.

| $n$ | $|F_n(0)e^2 - F_n(2)|$ |
|-----|------------------------|
| 1 | 4 |
| 2 | 1.5562 |
| 3 | .43775 |
| 4 | .09631 |
| 5 | .01739 |
| 6 | .00266 |
| 7 | .00035 |
| 8 | .00004 |

If we take $a = 1$, the rational approximations we get for $e^a = e$ by this method are *different* from the partial sums $\sum_{k=0}^n 1/k!$.

Although the proofs of Theorems 2.1 and 5.1 are similar in the sense that both used estimates on integrals, the proof of Theorem 2.1 did not show $\pi$ is irrational by exhibiting a sequence of good rational approximations to $\pi$. The proof of Theorem 2.1 was an "integer between 0 and 1" proof by contradiction. No good rational approximations to $\pi$ were produced in that proof. It is simply *harder* to get our grips on $\pi$ than it is on powers of $e$.

**Remark 5.6.** The irrationality of $e^r$ for positive rational $r$ can be proved by an "integer between 0 and 1" method, as indicated in [15]: use the integrals $J_{n,r} = \int_0^r (x(r-x))^n/n! \, e^x \, \mathrm{d}x$, the bounds $0 < J_{n,r} < (r^{2n}/n!)re^r$, and the recursion $J_{n,r} = -(4n-2)J_{n-1,r} + r^2 J_{n-2,r}$ for $n \ge 2$. Show from the recursion that $J_{n,r} = a_n(r)e^r + b_n(r)$ where $a_n(r)$ and $b_n(r)$ are polynomials in $r$ with integral coefficients of degree at most $n$. Write $r = A/B$ for positive integers $A$ and $B$. If $e^r$ is rational, say $e^r = p/q$, then the formula for $J_{n,r}$ in terms of $e^r$ implies $B^n q J_{n,r}$ is a positive integer that's at most $q(Br^2)^n/n!$, which is impossible for large $n$ since $q(Br^2)^n/n! \to 0$ as $n \to \infty$.

## 6. Returning to Irrationality of $\pi$

The proof of Theorem 5.1 gives a broader context for the proof in Theorem 2.1 that $\pi$ is irrational. In fact, by thinking about Theorem 5.1 in the *complex plane*, we are led to a slightly different proof of Theorem 2.1.

<!-- page 10 -->

*Proof.* We are going to use Hermite's lemma for complex $a$, where integrals from 0 to $a$ are obtained using a path of integration between 0 and $a$ (such as the straightline path). The definition of $e^a$ for complex $a$ is the infinite series $\sum_{n \ge 0} a^n/n!$. In particular, for real $t$, breaking up the series for $e^{it}$ into its real and imaginary parts yields

$$
e^{it} = \cos t + i \sin t.
$$

Thus $|e^{it}| = 1$ and $e^{i\pi} = -1$. Consider Hermite's lemma at $a = i\pi$:

$$
\int_0^{i\pi} e^{-x} f(x) \, \mathrm{d}x = \sum_{j=0}^{m} f^{(j)}(0) + \sum_{j=0}^{m} f^{(j)}(i\pi).
\tag{6.1}
$$

Extending (5.2) to the complex plane, we will use in (6.1) $f(x) = f_n(x) = x^n(x - i\pi)^n/n!$ for some large $n$ to be determined later (so $m = 2n$ as before). To put (6.1) in a more appealing form, we apply the change of variables $x = i\pi y$. The left side of (6.1) becomes

$$
\int_0^{i\pi} e^{-x} f_n(x) \, \mathrm{d}x = i(-1)^n \pi^{2n+1} \int_0^1 e^{-i\pi y} \frac{y^n(y-1)^n}{n!} \, \mathrm{d}y.
\tag{6.2}
$$

Let $g_n(y) = y^n(y-1)^n/n!$ (which does not involve $i$ or $\pi$), so $f_n(i\pi y) = (i\pi)^{2n} g_n(y)$ and differentiating $j$ times gives

$$
(i\pi)^j f_n^{(j)}(i\pi y) = (i\pi)^{2n} g_n^{(j)}(y).
\tag{6.3}
$$

Feeding (6.2) and (6.3) into (6.1), with $f = f_n$,

$$
i(-1)^n \pi^{2n+1} \int_0^1 e^{-i\pi y} g_n(y) \, \mathrm{d}y = \sum_{j=0}^{2n} (i\pi)^{2n-j} g_n^{(j)}(0) + \sum_{j=0}^{2n} (i\pi)^{2n-j} g_n^{(j)}(1).
\tag{6.4}
$$

*This* is the key equation in the proof. It serves the role for us now that (5.3) did in the proof of irrationality of powers of $e$. Notice the numbers $g_n^{(j)}(0)$ and $g_n^{(j)}(1)$ are all integers.

Suppose (at last) that $\pi$ is rational, say with positive denominator $q$. For $j < n$, $g_n^{(j)}(x)$ vanishes at $x = 0$ and $x = 1$, so the sums in (6.4) really only need to start at $j = n$. That means the largest power of $\pi$ in the (nonzero) terms on the right side of (6.4) is $\pi^n$, so the largest denominator on the right side of (6.4) is $q^n$. Multiply both sides by $q^n$:

$$
i(-q)^n \pi^{2n+1} \int_0^1 e^{-i\pi y} g_n(y) \, \mathrm{d}y = \sum_{j=0}^{2n} (i\pi)^{2n-j} q^n g_n^{(j)}(0) + \sum_{j=0}^{2n} (i\pi)^{2n-j} q^n g_n^{(j)}(1).
\tag{6.5}
$$

We estimate the left side of (6.5). Since $|e^{i\pi y}| = 1$, an estimate of the left side is

$$
\left|q^n \pi^{2n+1} \int_0^1 e^{-i\pi y} g_n(y) \, \mathrm{d}y\right| \le \frac{q^n \pi^{2n+1}}{n!} = \pi \frac{(q\pi^2)^n}{n!}.
$$

As $n \to \infty$, this bound tends to 0.

On the other hand, since the nonzero terms in the sums on the right side of (6.5) only start showing up at the $j = n$ term, and $\pi^{2n-j} q^n \in \mathbf{Z}$ for $n \le j \le 2n$, the right side of (6.5) is in the integral lattice $\mathbf{Z} + \mathbf{Z}i$. It is nonzero, as we see by looking at the real part of the left side of (6.5), which is

$$
(-q)^n \pi^{2n+1} \int_0^1 \sin(\pi y) g_n(y) \, \mathrm{d}y = (-q)^n \pi^{2n+1} \int_0^1 \sin(\pi y) \frac{y^n(y-1)^n}{n!} \, \mathrm{d}y.
$$

<!-- page 11 -->

The integrand here has constant sign on $(0, 1)$, so (6.5) is in $\mathbf{Z} + \mathbf{Z}i$ and doesn't vanish for integers $n \ge 1$ since the real part is not 0. A sequence of nonzero elements of $\mathbf{Z} + \mathbf{Z}i$ can't tend to 0. We have a contradiction, so $\pi$ is irrational. $\square$

We used complex numbers in the above proof to stress the close connection to the proof of Theorem 5.1. If you take the real part of every equation in the above proof (especially starting with (6.4)), then you will find a proof of the irrationality of $\pi$ that avoids complex numbers. (For instance, we showed (6.5) is nonzero by looking only at the real part, so taking real parts everywhere should not damage the logic of the proof.) By taking real parts, the goal of the proof changes slightly. Instead of showing the rationality of $\pi$ leads to a nonzero element of $\mathbf{Z} + \mathbf{Z}i$ with absolute value less than 1, showing the rationality of $\pi$ leads to a nonzero integer with absolute value less than 1. Is such a "real" proof basically the same as the first proof we gave that $\pi$ is rational? As a check, try to adapt the first proof of Theorem 2.1 to get the following.

**Corollary 6.1.** *The number $\pi^2$ is irrational.*

*Proof.* Run through the previous proof, starting at (6.4), but now assume $\pi^2$ is rational with denominator $q \in \mathbf{Z}$. While it is no longer true that $\pi^{2n-j} q^n \in \mathbf{Z}$ for $n \le j \le 2n$, we instead have $\pi^{2n-j} q^n \in \mathbf{Z}$ for $j$ even and $\pi^{2n-j} q^n \in (1/\pi)\mathbf{Z}$ for $j$ odd. Since $i^{2n-j}$ is real when $j$ is even and imaginary when $j$ is odd, we now have (6.5) lying in the set $\mathbf{Z} + \mathbf{Z}(i/\pi)$, whose nonzero elements are not arbitrarily small. $\square$

If you write up all the details in this proof and take the real part of every equation, you will have the proof of the irrationality of $\pi$ in [12, Chap. 16].

The numbers $\pi$ and $e$ are not just irrational, but transcendental. That is, neither number is the root of a nonzero polynomial with rational coefficients. (For comparison, $\sqrt{2}$ is irrational but it is a solution of $x^2 - 2 = 0$, so it is in some sense linked to the rational numbers through this equation.) Proofs of their transcendence can be found in [1, Chap. 1], [4, Chap. II], and [11, Chap. 2]. There is a proof that $e$ is transcendental that is not too much more complicated than our proof of Theorem 5.1. The idea is to use Hermite's lemma and a construction of a sequence of rational functions whose values give good rational approximations *simultaneously* to several integral powers of $e$, not only to one power like $e^a$.[^3] The construction of such rational functions generalizes the $f_n(x)$'s in Theorem 5.1, which gave good rational approximations to $e^a$. By comparison to this, proving transcendence of $\pi$ is much more involved than proving its irrationality.

Historically, progress on $\pi$ always trailed that of $e$. Euler proved $e$ is irrational in 1737, and Lambert proved irrationality of non-zero rational powers of $e$ and irrationality of $\pi$ in 1761. Their proofs used continued fractions, not integrals. (Lambert's proof for $\pi$ was really a result about values of $\tan x$: when $r$ is a nonzero rational number where $\tan r$ is defined, Lambert proved $\tan r$ is irrational. Then by $\tan(\pi/4) = 1$, $\pi/4$ must be irrational, so $\pi$ is irrational.) Transcendence proofs for $e$ and $\pi$ came 100 years later, in the work of Hermite (1873) and Lindemann (1882). In addition to $e$ and $\pi$, the numbers $2^{\sqrt{2}}$, $\log 2$, and $e^\pi$ are known to be transcendental. The status of $2^e$, $\pi^e$, $\pi^{\sqrt{2}}$, $e + \pi$, $e \log 2$, and Euler's constant $\gamma = \lim_{n \to \infty} \sum_{k=1}^n 1/k - \log n$ is still open. Surely these numbers are all transcendental, but it is not yet proved that even one of them is irrational.

[^3]: See https://kconrad.math.uconn.edu/blurbs/analysis/transcendence-e.pdf.

<!-- page 12 -->

## Appendix A. Recursions Using Integration by Parts

For the integrals

$$
I_n = \int_0^\pi \frac{(x(\pi - x))^n}{n!} \sin x \, \mathrm{d}x \quad \text{and} \quad J_n = \int_0^1 \frac{(x(1 - x))^n}{n!} e^x \, \mathrm{d}x
$$

that were met in (2.5) and (3.3), we want to derive the recursions

$$
I_n = (4n - 2)I_{n-1} - \pi^2 I_{n-2} \quad \text{and} \quad J_n = -(4n - 2)J_{n-1} + J_{n-2}
\tag{A.1}
$$

for $n \ge 2$ using integration by parts.

Letting $f_n(x) = \frac{(x(\pi - x))^n}{n!}$, we have $f_n'(x) = \frac{(x(\pi - x))^{n-1}}{(n-1)!}(\pi - 2x)$, so $f_n(0) = f_n(\pi) = 0$ for $n \ge 1$ and $f_n'(0) = f_n'(\pi) = 0$ for $n \ge 2$. Therefore by integration by parts where $u = f_n(x)$ and $\mathrm{d}v = \sin x \, \mathrm{d}x$, so $\mathrm{d}u = f_n'(x) \, \mathrm{d}x$ and $v = -\cos x$,

$$
\begin{aligned}
\int_0^\pi \frac{(x(\pi - x))^n}{n!} \sin x \, \mathrm{d}x &= \int_0^\pi f_n(x) \sin x \, \mathrm{d}x \\
&= -f_n(x) \cos x \Big|_0^\pi + \int_0^\pi f_n'(x) \cos x \, \mathrm{d}x \\
&= \int_0^\pi f_n'(x) \cos x \, \mathrm{d}x.
\end{aligned}
$$

By integration by parts where $u = f_n'(x)$ and $\mathrm{d}v = \cos x \, \mathrm{d}x$, so $\mathrm{d}u = f_n''(x) \, \mathrm{d}x$ and $v = \sin x$,

$$
\int_0^\pi f_n'(x) \cos x \, \mathrm{d}x = f_n'(x) \sin x \Big|_0^\pi - \int_0^\pi f_n''(x) \sin x \, \mathrm{d}x = -\int_0^\pi f_n''(x) \sin x \, \mathrm{d}x.
$$

Combining these,

$$
I_n = \int_0^\pi f_n(x) \sin x \, \mathrm{d}x = \int_0^\pi f_n'(x) \cos x \, \mathrm{d}x = -\int_0^\pi f_n''(x) \sin x \, \mathrm{d}x.
$$

We can write $f_n''(x)$ in terms of $f_{n-1}(x)$ and $f_{n-2}(x)$:

$$
\begin{aligned}
f_n''(x) &= (f_n'(x))' \\
&= \left(\frac{(x(\pi - x))^{n-1}}{(n-1)!}(\pi - 2x)\right)' \\
&= \frac{(x(\pi - x))^{n-1}}{(n-1)!}(-2) + \frac{(x(\pi - x))^{n-2}}{(n-2)!}(\pi - 2x)^2 \\
&= -2f_{n-1}(x) + (\pi - 2x)^2 f_{n-2}(x).
\end{aligned}
$$

Since $(\pi - 2x)^2 = \pi^2 - 4\pi x + 4x^2 = \pi^2 - 4x(\pi - x)$,

$$
\begin{aligned}
f_n''(x) &= -2f_{n-1}(x) + \pi^2 f_{n-2}(x) - 4x(\pi - x)\frac{(x(\pi - x))^{n-2}}{(n-2)!} \\
&= -2f_{n-1}(x) + \pi^2 f_{n-2}(x) - 4(n-1)f_{n-1}(x) \\
&= -(4n - 2)f_{n-1}(x) + \pi^2 f_{n-2}(x).
\end{aligned}
\tag{A.2}
$$

Multiply by $\sin x$ and integrate over $[0, \pi]$ to get the recursion for $I_n$ in (A.1):

$$
I_n = -\int_0^\pi f_n''(x) \sin x \, \mathrm{d}x = \int_0^\pi ((4n-2)f_{n-1}(x) - \pi^2 f_{n-2}(x)) \sin x \, \mathrm{d}x = (4n-2)I_{n-1} - \pi^2 I_{n-2}.
$$

<!-- page 13 -->

Switching to $J_n$, let $g_n(x) = \frac{(x(1-x))^n}{n!}$, so $J_n = \int_0^1 g_n(x) e^x \, \mathrm{d}x$. Since $g_n$ and $g_n'$ vanish at 0 and 1 when $n \ge 2$, $J_n = \int_0^1 g_n''(x) e^x \, \mathrm{d}x$ (not $-\int_0^1 g_n''(x) \, \mathrm{d}x$) after integrating by parts twice. The analogue of (A.2) for $g_n$ is

$$
g_n''(x) = -(4n - 2)g_{n-1}(x) + g_{n-2}(x),
$$

so multiplying by $e^x$ and integrating over $[0, 1]$ gives us $J_n = -(4n - 2)J_{n-1} + J_{n-2}$.

## Appendix B. Irrationality of $e^2$

In Section 4, we saw that the partial sums of the Taylor series for $e^x$ at $x = 2$, namely the sums $\sum_{k=0}^n 2^k/k!$, do not seem to be a sequence of rational approximations to $e^2$ that allow us to prove $e^2$ is irrational via Theorem 4.1. This was circumvented in Theorem 5.1, where the nonzero integral powers of $e$ (not just $e^2$) were proved to be irrational using rational approximations coming from something other than the Taylor series for $e^x$. What we will show here is that the partial sums $\sum_{k=0}^n 2^k/k!$ can, after all, be used to prove irrationality of $e^2$ by focusing on a certain subsequence of the partial sums and exploiting a peculiar property of 2. The argument we give is due to Benoit Cloitre.

Write $\sum_{k=0}^n 2^k/k!$ in reduced form as $a_n/b_n$. Then $e^2 > a_n/b_n$, so $b_n e^2 - a_n > 0$. While numerical data suggest $b_n e^2 - a_n$ does not go to 0 as $n \to \infty$, it turns out that these nonzero differences tend to 0 as $n$ runs through the powers of 2. The table below has some limited evidence in this direction.

| $n$ | $b_n e^2 - a_n$ |
|-----|-----------------|
| 2 | 2.389 |
| 4 | .3890 |
| 8 | .5526 |
| 16 | .0881 |
| 32 | .0006 |
| 64 | .0211 |
| 128 | .0005 |
| 256 | .0001 |

If these differences do tend to 0, then this proves $e^2$ is irrational by Theorem 4.1. To prove this phenomenon is real, we use Lagrange's form of the remainder to estimate the difference between $e^2$ and $\sum_{k=0}^n 2^k/k!$ before setting $n$ to be a power of 2. Lagrange's form of the remainder says: for an infinitely differentiable function $f$ and integer $n \ge 0$,

$$
f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} x^k + \frac{f^{(n+1)}(c)}{(n+1)!} x^n,
$$

where $c$ is between 0 and $x$. Taking $f$ to be the exponential function and $x = 2$,

$$
e^2 = \sum_{k=0}^{n} \frac{2^k}{k!} + \frac{e^c 2^n}{(n+1)!},
$$

where $0 < c < 2$. Bring the sum to the left side, multiply by $n!/2^n$, and take absolute values:

$$
\left|\frac{n!}{2^n} e^2 - \frac{n!}{2^n} \sum_{k=0}^{n} \frac{2^k}{k!}\right| \le \frac{e^2}{n+1}.
\tag{B.1}
$$

<!-- page 14 -->

Set

$$
c_n = \frac{n!}{2^n} \sum_{k=0}^{n} \frac{2^k}{k!}, \quad d_n = \frac{n!}{2^n},
$$

so $c_n/d_n = \sum_{k=0}^n 2^k/k! = a_n/b_n$ and (B.1) says $|d_n e^2 - c_n| \le e^2/(n+1)$. Thus $|d_n e^2 - c_n| \to 0$ as $n \to \infty$ and $d_n e^2 - c_n \ne 0$. Be careful: the numbers $c_n$ and $d_n$ are not themselves integers (as we will see), so the expression $|d_n e^2 - c_n|$ is not quite in a form suitable for immediate application of Theorem 4.1. But we can get good control on the denominators of $c_n$ and $d_n$.

Writing $c_n = (1/2^n) \sum_{k=0}^n (n!/k!) 2^k$, since $n!/k!$ is an integer $c_n$ is an integer divided by $2^n$, so $c_n$ has a 2-power denominator in reduced form. Since $d_n$ is an integer divided by $2^n$, its reduced form denominator is also a power of 2. What are the powers of 2 in the reduced form for $c_n$ and $d_n$?

For a nonzero rational number $r$, write $\mathrm{ord}_2(r)$ for the power of 2 appearing in $r$, *e.g.*, $\mathrm{ord}_2(40) = 3$ and $\mathrm{ord}_2(21/20) = -2$. By unique prime factorization, $\mathrm{ord}_2(rr') = \mathrm{ord}_2(r) + \mathrm{ord}_2(r')$ for nonzero rationals $r$ and $r'$. Another important formula is $\mathrm{ord}_2(r + r') = \min(\mathrm{ord}_2(r), \mathrm{ord}_2(r'))$ when $\mathrm{ord}_2(r) \ne \mathrm{ord}_2(r')$ and $r + r' \ne 0$. (These properties both resemble the degree on polynomials and rational functions, except the degree has a max where $\mathrm{ord}_2$ has a min on sums.)

We want to compute $\mathrm{ord}_2(c_n)$ and $\mathrm{ord}_2(d_n)$. As $d_n = n!/2^n$ is simpler than $c_n$, we look at it first. Since $\mathrm{ord}_2(d_n) = \mathrm{ord}_2(n!/2^n) = \mathrm{ord}_2(n!) - n$, we bring in a formula for the highest power of 2 in a factorial, due to Legendre: $\mathrm{ord}_2(n!) = n - s_2(n)$, where $s_2(n)$ is the sum of the base 2 digits of $n$. For example, $6! = 2^4 \cdot 3^2 \cdot 5$ and $6 = 2 + 2^2$, so $6 - s_2(6) = 6 - 2 = 4$ matches $\mathrm{ord}_2(6!)$. With this formula of Legendre,

$$
\mathrm{ord}_2(d_n) = \mathrm{ord}_2(n!) - n = (n - s_2(n)) - n = -s_2(n).
$$

For $n \ge 1$ this is negative (there is at least one nonzero base 2 digit in $n$, so $s_2(n) \ge 1$), which proves $d_n$ is not an integer.

What about $\mathrm{ord}_2(c_n)$? Writing

$$
c_n = \sum_{k=0}^{n} \frac{n! 2^k}{2^n k!} = \frac{n!}{2^n} + \frac{n! \cdot 2}{2^n \cdot 1} + \frac{n! \cdot 4}{2^n \cdot 2} + \frac{n! \cdot 2^3}{2^n \cdot 6} + \cdots + 1,
$$

each term has at worst a 2-power denominator since $n!/k! \in \mathbf{Z}$ when $0 \le k \le n$. To figure out the power of 2 in the denominator we will compute $\mathrm{ord}_2(n! 2^k / 2^n k!)$. For $k = 0$ this is $\mathrm{ord}_2(n!/2^n) = -s_2(n)$. For $k \ge 1$ this is

$$
\mathrm{ord}_2(n!) + k - n - \mathrm{ord}_2(k!) = -s_2(n) + s_2(k) > -s_2(n)
$$

since $s_2(k) \ge 1$. Therefore every term in the sum for $c_n$ beyond the $k = 0$ term has a larger 2-power divisibility than the $k = 0$ term, which means $\mathrm{ord}_2(c_n)$ is the same as $\mathrm{ord}_2(n!/2^n) = -s_2(n)$. In other words, $c_n$ and $d_n$ have the same denominator: $2^{s_2(n)}$.

If we let $n$ be a power of 2 then $c_n$ and $d_n$ have denominator $2^1 = 2$, so $2c_n$ and $2d_n$ are integers. Then the estimate

$$
0 < |2d_n e^2 - 2c_n| = 2|d_n e^2 - c_n| \le \frac{2e^2}{n+1} \to 0
$$

proves $e^2$ is irrational by Theorem 4.1.

It is natural to ask if the same argument yields a proof that $e^p$ is irrational for prime $p > 2$ using the Taylor series for $e^x$ at $x = p$. Let $c_n = (n!/p^n) \sum_{k=0}^n p^k/k!$ and $d_n = n!/p^n$,

<!-- page 15 -->

so $|d_n e^p - c_n| \le e^p/(n+1)$ as before. Legendre's formula for $\mathrm{ord}_p(n!)$, the highest power of $p$ in $n!$, is $(n - s_p(n))/(p - 1)$, where $s_p(n)$ is the sum of the base $p$ digits of $n$. The fractions $c_n$ and $d_n$ have the same $p$-power denominator, with exponent $\mathrm{ord}_p(n!) - n = n(1 - 1/(p-1)) + s_p(n)/(p-1)$. Alas, for $p > 2$ this exponent of $p$ in the denominator of $c_n$ and $d_n$ blows up with $n$ because $1 - 1/(p-1) > 0$ for $p > 2$. When $p = 2$ this exponent in the denominator is $s_2(n)$, which can stay bounded by restricting $n$ to the powers of 2.

## Appendix C. Deriving Formulas for $\pi/4$

We will prove formulas for $\pi/4$ presented in the introduction:

$$
\frac{\pi}{4} = \arctan\frac{1}{2} + \arctan\frac{1}{3},
\tag{C.1}
$$

$$
\frac{\pi}{4} = 2\arctan\frac{1}{3} + \arctan\frac{1}{7},
\tag{C.2}
$$

$$
\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}.
\tag{C.3}
$$

The proofs will use the following addition formula for $\arctan x$.

**Theorem C.1.** *If $x$, $y$, and $(x+y)/(1-xy)$ are in $(0, \pi/2)$ and $0 < xy < 1$, then*

$$
\arctan x + \arctan y = \arctan\left(\frac{x+y}{1-xy}\right).
\tag{C.4}
$$

*Proof.* By the tangent addition formula

$$
\tan(\theta_1 + \theta_2) = \frac{\tan\theta_1 + \tan\theta_2}{1 - \tan\theta_1 \tan\theta_2}
$$

and the identity $\tan(\arctan t) = t$ when $t \in (-\pi/2, \pi/2)$, the two sides of (C.4) have common tangent value $(x+y)/(1-xy)$. Thus the two sides of (C.4) are equal provided they are in $(-\pi/2, \pi/2)$. The right side of (C.4) is in $(0, \pi/2)$ since arctan-values on positive numbers are in $(0, \pi/2)$. That the left side of (C.4) is in $(0, \pi/2)$ follows from $\arctan t < t$ when $t > 0$ since it implies $0 < \arctan x + \arctan y < x + y < (x+y)/(1-xy) < \pi/2$. $\square$

To derive (C.1), set $x = 1/2$ and $y = 1/3$ in Theorem C.1: since $(x+y)/(1-xy) = (5/6)/(5/6) = 1 < \pi/2$,

$$
\arctan\frac{1}{2} + \arctan\frac{1}{3} = \arctan\left(\frac{x+y}{1-xy}\right) = \arctan 1 = \frac{\pi}{4}.
$$

To derive (C.2), first we compute $2\arctan(1/3)$ by using $x = y = 1/3$ in Theorem C.1: $(x+y)/(1-xy) = (2/3)/(8/9) = 3/4 < 1 < \pi/2$, so

$$
2\arctan\frac{1}{3} = \arctan\frac{1}{3} + \arctan\frac{1}{3} = \arctan\left(\frac{x+y}{1-xy}\right) = \arctan\frac{3}{4}.
$$

Now use Theorem C.1 with $x = 3/4$ and $y = 1/7$: $(x+y)/(1-xy) = (25/28)/(25/28) = 1$, so

$$
2\arctan\frac{1}{3} + \arctan\frac{1}{7} = \arctan\frac{3}{4} + \arctan\frac{1}{7} = \arctan\left(\frac{x+y}{1-xy}\right) = \arctan 1 = \frac{\pi}{4}.
$$

To derive (C.3), rewrite it as

$$
\arctan 1 + \arctan\frac{1}{239} = 4\arctan\frac{1}{5}.
$$

<!-- page 16 -->

To prove this, we'll rewrite both sides as a common arctan value. Set $x = 1$ and $y = 1/239$ in Theorem C.1: $(x+y)/(1-xy) = 240/238 = 120/119 \approx 1.008 < \pi/2$, so

$$
\arctan 1 + \arctan\frac{1}{239} = \arctan\left(\frac{x+y}{1-xy}\right) = \arctan\frac{120}{119}.
\tag{C.5}
$$

Next, set $x = y = 1/5$ in Theorem C.1: $(x+y)/(1-xy) = (2/5)/(24/25) = 5/12 < 1 < \pi/2$, so

$$
2\arctan\frac{1}{5} = \arctan\frac{1}{5} + \arctan\frac{1}{5} = \arctan\frac{x+y}{1-xy} = \arctan\frac{5}{12}.
$$

When $x = y = 5/12$ in Theorem C.1, $(x+y)/(1-xy) = (5/6)/(119/144) = 120/119 < \pi/2$, so

$$
4\arctan\frac{1}{5} = 2 \cdot 2\arctan\frac{1}{5} = 2\arctan\frac{5}{12} = \arctan\left(\frac{x+y}{1-xy}\right) = \arctan\frac{120}{119}.
$$

That matches (C.5), so we have proved (C.3).

**Remark C.2.** Formula (C.3) is due to Machin in 1706 and was used by Shanks [10] in his calculation of 707 digits of $\pi$ that was in error after the 527th decimal place.

As an exercise, use Theorem C.1 to prove an 1896 formula of Stormer [14]:

$$
\frac{\pi}{4} = 6\arctan\frac{1}{8} + 2\arctan\frac{1}{57} + \arctan\frac{1}{239}.
$$

First show $6\arctan(1/8) = \arctan(186416/201663)$ and $2\arctan(1/57) = \arctan(57/1624)$.

## References

[1] A. Baker, "Transcendental Number Theory," Cambridge Univ. Press, Cambridge, 1975.

[2] C. H. Edwards, Jr., "The Historical Development of the Calculus," Springer-Verlag, New York, 1979.

[3] L. Euler De fractionibus continuis dissertatio, *Commentarii Academiae Scientiarum Petropolitanae* **9** (1744), 98--137. URL https://scholarlycommons.pacific.edu/euler-works/71/.

[4] A. O. Gelfond, "Transcendental and Algebraic Numbers," Dover, New York, 1960.

[5] E. Hairer and G. Wanner, "Analysis by its History," Springer-Verlag, New York, 1996.

[6] K. Ireland and M. Rosen, "A Classical Introduction to Modern Number Theory," 2nd ed., Springer-Verlag, New York, 1990.

[7] J. H. Lambert, Memoire sur quelques proprietes remarquables des quantites transcendantes circulaires et logarithmiques, *Histoire de l'Academie Royale des Sciences et Belles-Lettres de Berlin, Annee 1761* **17** 1768, 265--322. URL http://www.bibnum.education.fr/mathematiques/theorie-des-nombres/lambert-et-l-irrationalite-de-p-1761. English translation at https://hal.archives-ouvertes.fr/hal-02984214/document.

[8] I. Niven, A simple proof that $\pi$ is irrational, *Bull. Amer. Math. Soc.* **53** (1947), 509.

[9] R. Roy, The Discovery of the Series Formula for $\pi$ by Leibniz, Gregory and Nilakanth, *Math. Mag.* **63** (1990), 291--306.

[10] W. Shanks, On the extension of the numerical value of $\pi$, Proceedings of the Royal Society of London **21** (1873), 318-319. URL https://royalsocietypublishing.org/doi/pdf/10.1098/rspl.1872.0066.

[11] A. Shidlovskii, "Transcendental Numbers," de Gruyter, Berlin 1989.

[12] M. Spivak, "Calculus," 2nd ed., Publish or Perish, Wilmington, Del., 1967.

[13] J. de Stainville, "Melange d'analyse Algebrique et de Geometrie," Courcier, Paris, 1815. URL http://www.bibnum.education.fr/mathematiques/theorie-des-nombres/melange-d-analyse-algebrique-et-de-geometrie.

[14] C. Stormer, Sur l'Application de la Theorie des Nombres Entiers Complexes a la Solution en Nombres Rationels $x_1, x_2, \ldots, x_n, c_1, c_2, \ldots, k$, de l'Equation $c_1 \mathrm{arctg}\, x_1 + c_2 \mathrm{arctg}\, x_2 + \cdots + c_n \mathrm{arctg}\, x_n = k\pi/4$, Archiv for Mathematik og Naturvidenskab **19** (1896), 75--85.

[15] L. Zhou and L. Markov, Recurrent Proofs of the Irrationality of Certain Trigonometric Values, *Amer. Math. Monthly* **117** (2010), 360--362.
