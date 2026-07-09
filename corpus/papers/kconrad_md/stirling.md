# Stirling's Formula

> **Source**: https://kconrad.math.uconn.edu/blurbs/stirling.pdf  
> **Author**: Keith Conrad  
> **Topic**: combinatorics

<!-- page 1 -->

## 1. Introduction

Our goal is to prove the following asymptotic estimate for $n!$, called Stirling's formula.

**Theorem 1.1.** *As $n \to \infty$, $n! \sim \dfrac{n^n}{e^n}\sqrt{2\pi n}$. That is, $\displaystyle\lim_{n \to \infty} \frac{n!}{(n^n/e^n)\sqrt{2\pi n}} = 1$.*

**Example 1.2.** Set $n = 10$: $10! = 3628800$ and $(10^{10}/e^{10})\sqrt{2\pi(10)} = 3598695.61\ldots$. The difference between these, around $30104$, is rather large by itself but is less than $1\%$ of the value of $10!$. That is, Stirling's approximation for $10!$ is within $1\%$ of the correct value.

Stirling's formula can also be expressed as an estimate for $\log(n!)$:

$$\log(n!) = n\log n - n + \frac{1}{2}\log n + \frac{1}{2}\log(2\pi) + \varepsilon_n, \tag{1.1}$$

where $\varepsilon_n \to 0$ as $n \to \infty$.

**Example 1.3.** Taking $n = 10$, $\log(10!) \approx 15.104$ and the logarithm of Stirling's approximation to $10!$ is approximately $15.096$, so $\log(10!)$ and its Stirling approximation differ by roughly $.008$.

Before proving Stirling's formula we will establish a weaker estimate for $\log(n!)$ than (1.1) that shows $n\log n$ is the right order of magnitude for $\log(n!)$. After proving Stirling's formula we will give some applications and then discuss a little bit of its history. Stirling's contribution to Theorem 1.1 was recognizing the role of the constant $\sqrt{2\pi}$.

## 2. Weaker Version

**Theorem 2.1.** *For all $n \geq 2$, $n\log n - n < \log(n!) < n\log n$, so $\log(n!) \sim n\log n$.*

*Proof.* The inequality $\log(n!) < n\log n$ is a consequence of the trivial inequality $n! < n^n$.

Here are three methods of showing $n\log n - n < \log(n!)$.

*Method 1:* A Riemann sum approximation for $\int_1^n \log x\, dx$ using right endpoints is $\log 2 + \cdots + \log n = \log(n!)$, which overestimates, so $\log(n!) > \int_1^n \log x\, dx = n\log n - n + 1$.

*Method 2:* The power series expansion of $e^n$ is $\sum_{k \geq 0} n^k/k!$. Comparing $e^n$ to the $n$th term in the series gives us $e^n > n^n/n!$, so $n! > n^n/e^n$. Therefore $\log(n!) > n\log n - n$.

*Method 3:* For all $k \geq 1$, $e > (1 + 1/k)^k$. Multiplying this over $k = 1, 2, \ldots, n-1$, we get $e^{n-1} > n^{n-1}/(n-1)! = n^n/n!$, so $n! > en^n/e^n$. Thus $\log(n!) > n\log n - n + 1$.

Dividing through the inequality $n\log n - n < \log(n!) < n\log n$ by $n\log n$, we obtain $1 - 1/\log n < \log(n!)/(n\log n) < 1$, so $\log(n!) \sim n\log n$. $\square$

We won't use Theorem 2.1 in the proof of Theorem 1.1, but it's worth proving Theorem 2.1 first since the approximations $\log(n!) \approx n\log n - n$ or $\log(n!) \approx n\log n$ are how Stirling's formula is most often used in science. Large factorials occur when counting arrangements of gas particles or quantum particles in different macrostates, or files in data compression. While the lower order terms $\frac{1}{2}\log n + \frac{1}{2}\log(2\pi)$ in (1.1) are irrelevant in most scientific applications of (1.1), they are used in calculations in quantum field theory.

<!-- page 2 -->

**Remark 2.2.** In the proof of Theorem 2.1, the first and third methods lead to upper bounds on $\log(n!)$ that are sharper than $n\log n$. By the first method, using left endpoints implies $\int_1^n \log x\, dx > \log((n-1)!) = \log(n!) - \log n$, which leads to $\log(n!) < n\log n - n + \log n + 1$. (We can do slightly better with the trapezoid approximation, which is the average of the left endpoint and right endpoint approximations. It tells us, since $\log x$ is concave down, that $\int_1^n \log x\, dx > \frac{1}{2}(\log(n!) + \log(n!) - \log n) = \log(n!) - \frac{1}{2}\log n$, so $\log(n!) < n\log n - n + \frac{1}{2}\log n + 1$.) By the third method, the upper bound $e < (1 + 1/k)^{k+1}$ multiplied over $k = 1, 2, \ldots, n-1$ leads to $e^{n-1} < n^n/(n-1)! = n^{n+1}/n!$, so $\log(n!) < n\log n - n + \log n + 1$.

## 3. Proof of Stirling's Formula

Any proof of Stirling's formula needs to bring in a formula that involves $\pi$. One such formula, which Stirling knew, is the Wallis product

$$\frac{\pi}{2} = \frac{2}{1} \cdot \frac{2}{3} \cdot \frac{4}{3} \cdot \frac{4}{5} \cdot \frac{6}{5} \cdot \frac{6}{7} \cdots.$$

Another formula is the evaluation of the Gaussian integral from probability theory:

$$\int_{-\infty}^{\infty} e^{-x^2/2}\, dx = \sqrt{2\pi}. \tag{3.1}$$

This integral will be how $\sqrt{2\pi}$ enters the proof of Stirling's formula here, and another idea from probability theory will also be used in the proof.

To prove Stirling's formula, we begin with Euler's integral for $n!$.

**Theorem 3.1 (Euler).** *For $n \geq 0$,*

$$n! = \int_0^{\infty} x^n e^{-x}\, dx.$$

*Proof.* We will use induction and integration by parts. The case $n = 0$ is a direct calculation: $\int_0^{\infty} e^{-x}\, dx = -e^{-x}\big|_0^{\infty} = 0 - (-1) = 1$. If $n! = \int_0^{\infty} x^n e^{-x}\, dx$ for some $n$, then

$$\int_0^{\infty} x^{n+1} e^{-x}\, dx = \int_0^{\infty} u\, dv$$

where $u = x^{n+1}$ and $dv = e^{-x}\, dx$. Then $du = (n+1)x^n\, dx$ and $v = -e^{-x}$, so

$$\int_0^{\infty} x^{n+1} e^{-x}\, dx = \left. uv \right|_0^{\infty} - \int_0^{\infty} v\, du = -\left.\frac{x^{n+1}}{e^x}\right|_0^{\infty} + \int_0^{\infty} (n+1)e^{-x}x^n\, dx = \lim_{b \to \infty} -\frac{b^{n+1}}{e^b} + 0 + (n+1)\int_0^{\infty} x^n e^{-x}\, dx = (n+1)\int_0^{\infty} x^n e^{-x}\, dx,$$

which by induction is $(n+1)n! = (n+1)!$.^[Using Theorem 3.1, $n! = \int_0^{\infty} x^n e^{-x}\, dx > \int_n^{\infty} x^n e^{-x}\, dx > n^n \int_n^{\infty} e^{-x}\, dx = n^n/e^n$ for $n \geq 2$, which is another proof of the lower bound $\log(n!) > n\log n - n$ in Theorem 2.1.] $\square$

Let's consider the graph of $y = x^n e^{-x}$ for $x \geq 0$. By calculus, the graph has a maximum at $x = n$ and inflection points at $x = n + \sqrt{n}$ and $x = n - \sqrt{n}$. In Figure 1 is $1 \leq n \leq 4$.

These graphs, for larger $n$, look somewhat like bell curves from probability theory. In probability, the density function of a normal random variable $X$ with mean $\mu$ and standard deviation $\sigma$ has its maximum at $\mu$ and inflection points at $\mu + \sigma$ and $\mu - \sigma$, and the random

<!-- page 3 -->

variable $Z = (X - \mu)/\sigma$ is then normal with mean $0$ and standard deviation $1$. Considering the analogy $\mu \leftrightarrow n$ and $\sigma \leftrightarrow \sqrt{n}$, make the change of variables $t = (x - n)/\sqrt{n}$ in Euler's integral for $n!$. This sends $x = n$ to $t = 0$ and $x = n \pm \sqrt{n}$ to $t = \pm 1$, so

$$n! = \int_0^{\infty} x^n e^{-x}\, dx = \int_{-\sqrt{n}}^{\infty} (n + \sqrt{n}t)^n e^{-(n + \sqrt{n}t)} \sqrt{n}\, dt = \frac{n^n \sqrt{n}}{e^n} \int_{-\sqrt{n}}^{\infty} \left(1 + \frac{t}{\sqrt{n}}\right)^n e^{-\sqrt{n}t}\, dt. \tag{3.2}$$

The terms extracted out of the integral in (3.2) are *exactly* what appears in Stirling's formula except for the factor $\sqrt{2\pi}$, so to prove Stirling's formula we will show

$$\left(1 + \frac{t}{\sqrt{n}}\right)^n e^{-\sqrt{n}t} \to e^{-t^2/2} \tag{3.3}$$

as $n \to \infty$, for each $t$, and then

$$\int_{-\sqrt{n}}^{\infty} \left(1 + \frac{t}{\sqrt{n}}\right)^n e^{-\sqrt{n}t}\, dt \to \int_{-\infty}^{\infty} e^{-t^2/2}\, dt \stackrel{(3.1)}{=} \sqrt{2\pi} \tag{3.4}$$

as $n \to \infty$.

**Remark 3.2.** There are two proofs of Stirling's formula in [3] using a sequence of random variables $X_n$ with mean $n$ and standard deviation $\sqrt{n}$, and the change of variables $T_n = (X_n - n)/\sqrt{n}$. This same change of variables, in the form $t = (x - n)/\sqrt{n}$, is used without motivation in the non-probabilistic proofs of Stirling's formula in [17] and [18].

To prove (3.3) requires some care. If we handwave, as $n \to \infty$

$$\left(1 + \frac{t}{\sqrt{n}}\right)^n e^{-\sqrt{n}t} = \left(\left(1 + \frac{t}{\sqrt{n}}\right)^{\sqrt{n}}\right)^{\sqrt{n}} e^{-\sqrt{n}t} \approx (e^t)^{\sqrt{n}} e^{-\sqrt{n}t} = 1,$$

which is wrong. The mistake is that although $(1 + t/\sqrt{n})^{\sqrt{n}} \to e^t$ as $n \to \infty$, it is not true after raising both sides to the $\sqrt{n}$ power that $(1 + t/\sqrt{n})^n$ behaves like $e^{\sqrt{n}t}$: approximately equal numbers need not remain approximately equal when raised to a large power.

<!-- page 4 -->

To write the integral in (3.2) over the whole real line, set

$$f_n(t) = \begin{cases} 0, & \text{if } t \leq -\sqrt{n}, \\ (1 + t/\sqrt{n})^n e^{-\sqrt{n}t}, & \text{if } t \geq -\sqrt{n}, \end{cases}$$

so $n! = (n^n\sqrt{n}/e^n) \int_{-\infty}^{\infty} f_n(t)\, dt$. Figure 2 is a plot of $y = f_n(t)$ for $1 \leq n \leq 4$ (solid) compared to $y = e^{-t^2/2}$ (dashed). The graphs suggest that as $n \to \infty$, $f_n(t) \to e^{-t^2/2}$.

**Theorem 3.3.** *For each $t \in \mathbf{R}$, $f_n(t) \to e^{-t^2/2}$ as $n \to \infty$.*

*Proof.* We will show $\log f_n(t) \to -t^2/2$ as $n \to \infty$. Since $t$ is fixed in the limit calculation, we can focus on $n$ that is large relative to $|t|$. For $\sqrt{n} > |t|$, *i.e.*, $n > t^2$, we have

$$f_n(t) = \frac{(1 + t/\sqrt{n})^n}{e^{\sqrt{n}t}},$$

so

$$\log(f_n(t)) = n\log\left(1 + \frac{t}{\sqrt{n}}\right) - \sqrt{n}t.$$

For $n > 4t^2$, $|t/\sqrt{n}| < 1/2$. We have $\log(1 + x) = x - x^2/2 + O(|x|^3)$ for $|x| \leq 1/2$,^[In [18] it's shown for $|x| \leq 1/2$ that $\log(1 + x) = x - x^2/2 + O(|x|^3/3)$ where the $O$-constant can be $2$.] so

$$\log(f_n(t)) = n\left(\frac{t}{\sqrt{n}} - \frac{(t/\sqrt{n})^2}{2} + O((t/\sqrt{n})^3)\right) - \sqrt{n}t = -\frac{t^2}{2} + O(t^3/\sqrt{n}).$$

As $n \to \infty$, the $O$-term tends to $0$, so the limit is $-t^2/2$. $\square$

To deduce from Theorem 3.3 that $\int_{-\infty}^{\infty} f_n(t)\, dt \to \int_{-\infty}^{\infty} e^{-t^2/2}\, dt$, which would finish the proof of Stirling's formula by (3.4), we use the dominated convergence theorem: what is a positive integrable function on $\mathbf{R}$ dominating $|f_n| = f_n$ for all $n$? By Figure 2, one such function should be

$$g(t) := \begin{cases} e^{-t^2/2}, & \text{if } t < 0 \\ f_1(t), & \text{if } t \geq 0 \end{cases} = \begin{cases} e^{-t^2/2}, & \text{if } t < 0, \\ (1 + t)e^{-t}, & \text{if } t \geq 0, \end{cases}$$

which is positive and integrable on $\mathbf{R}$. To prove $0 \leq f_n(t) \leq g(t)$ for all $n$ and $t$, it's obvious for $t \leq -\sqrt{n}$ since $f_n(t) = 0$. To prove $f_n(t) \leq g(t)$ if $t > -\sqrt{n}$, take logarithms:

$$\log f_n(t) = n\log\left(1 + \frac{t}{\sqrt{n}}\right) - \sqrt{n}t \stackrel{?}{\leq} \log g(t) = \begin{cases} -t^2/2, & \text{if } -\sqrt{n} < t \leq 0, \\ \log(1 + t) - t, & \text{if } t \geq 0. \end{cases}$$

<!-- page 5 -->

*Case 1:* $\log f_n(t) \leq -t^2/2$ for $-\sqrt{n} < t \leq 0$.

We will show the difference

$$\log f_n(t) + \frac{t^2}{2} = n\log\left(1 + \frac{t}{\sqrt{n}}\right) - \sqrt{n}t + \frac{t^2}{2} \tag{3.5}$$

for $-\sqrt{n} < t \leq 0$ is increasing, so the fact that it vanishes at $t = 0$ implies it is negative for $-\sqrt{n} < t < 0$. The derivative of (3.5) is

$$\frac{n}{1 + t/\sqrt{n}} \cdot \frac{1}{\sqrt{n}} - \sqrt{n} + t = \frac{t^2}{t + \sqrt{n}},$$

which is positive for $-\sqrt{n} < t < 0$ since the numerator and denominator are both positive.

*Case 2:* $\log f_n(t) \leq \log(1 + t) - t$ for $t \geq 0$. This is trivial for $n = 1$, since $\log f_1(t) = \log(1 + t) - t$ for $t \geq 0$. Thus we can take $n > 1$. We will show

$$\log(1 + t) - t - \log f_n(t) = \log(1 + t) - t - n\log\left(1 + \frac{t}{\sqrt{n}}\right) + \sqrt{n}t \tag{3.6}$$

for $t \geq 0$ is increasing, so the fact that it vanishes at $t = 0$ implies it is positive for $t > 0$. The derivative of (3.6) is

$$\frac{1}{1 + t} - 1 - \frac{n}{1 + t/\sqrt{n}} \cdot \frac{1}{\sqrt{n}} + \sqrt{n} = \frac{(\sqrt{n} - 1)t^2}{(t + 1)(t + \sqrt{n})},$$

which is positive since the numerator and denominator are positive when $t > 0$ and $n \geq 2$.

Our proof of Stirling's formula is now complete.

**Remark.** Similar to the proof that $f_n(t) \leq g(t)$, we can prove what is suggested by Figure 2: $f_{n+1}(t) < f_n(t)$ for $t > 0$ and $f_{n+1}(t) > f_n(t)$ for $-\sqrt{n} < t < 0$, so $f_n(t) \to e^{-t^2/2}$ as $n \to \infty$ from below for $t < 0$ and from above for $t > 0$. (At $t = 0$ we have $f_n(0) = 1$ for all $n$.) For $t > -\sqrt{n}$, both $f_n(t)$ and $f_{n+1}(t)$ are positive and

$$\frac{d}{dt}(\log f_{n+1}(t) - \log f_n(t)) = -\frac{t\sqrt{n+1}}{t + \sqrt{n+1}} + \frac{t\sqrt{n}}{t + \sqrt{n}} = \frac{(\sqrt{n} - \sqrt{n+1})t^2}{(t + \sqrt{n})(t + \sqrt{n+1})},$$

which is negative for $t > -\sqrt{n}$ except for being $0$ at $t = 0$, so $\log(f_{n+1}(t)/f_n(t))$ is decreasing for $t > -\sqrt{n}$. Since $f_{n+1}(0)/f_n(0) = 1$, we get $f_{n+1}(t)/f_n(t) > 1$ for $-\sqrt{n} < t < 0$ and $f_{n+1}(t)/f_n(t) < 1$ for $t > 0$.

## 4. Applications of Stirling's Formula

**Example 4.1.** The probability that flipping a fair coin $2n$ times results in *exactly* $n$ heads and $n$ tails is $\binom{2n}{n}(\frac{1}{2})^{2n}$. What is a good estimate for the size of this number? Writing $\binom{2n}{n}$ as $\frac{(2n)!}{n!n!} = \frac{(2n)!}{n!^2}$, by Stirling's formula

$$\binom{2n}{n} \sim \frac{((2n)^{2n}/e^{2n})\sqrt{2\pi(2n)}}{(n^n/e^n)^2(2\pi n)} = \frac{2^{2n}}{\sqrt{\pi n}},$$

so $\binom{2n}{n}(\frac{1}{2})^{2n} \sim 1/\sqrt{\pi n}$. This probability decays to $0$ like $1/\sqrt{n}$.

This same calculation occurs in the theory of random walks. Suppose a person moves around the $d$-dimensional lattice $\mathbf{Z}^d$ by jumping from any point to one of its $2d$ neighboring points (differing in one coordinate by $\pm 1$), with a move in each of the $2d$ directions being equally likely. If such a random walk starts at the origin, will it return to the origin infinitely often? Polya proved that if $d = 1$ or $2$ then the probability of returning to the origin infinitely often is $1$, while for $d \geq 3$ this probability is $0$. In picturesque language, a drunkard who stumbles away from a bar by walking along a road or in a street grid is almost

<!-- page 6 -->

surely going to come back to the bar, but if he can fly ($d = 3$) then it's no longer certain that he'll return. The key to this result on random walks is that $\sum_{n \geq 1} 1/n^{d/2}$ diverges for $d = 1$ and $2$, and converges for $d \geq 3$. To see the connection to the coin problem above, consider a random walk on $\mathbf{Z}$ (that is, $d = 1$). If a person starting at $0$ takes steps left and right by $1$ unit with probability $1/2$ each, then the probability the person returns to $0$ after $2n$ steps (it's impossible to return to $0$ after an odd number of steps) is the probability of taking $n$ left steps and $n$ right steps, so the probability is $\binom{2n}{n}(\frac{1}{2})^{2n}$. The asymptotic estimate $1/\sqrt{\pi n}$ from Stirling's formula tells us that the sum of these probabilities over all $n$ diverges because $\sum_{n \geq 1} 1/\sqrt{n}$ diverges, and this divergence leads to probability $1$ that such events (returning to $0$) occur infinitely often. Stirling's formula can also be used to analyze random walks in $\mathbf{Z}^d$ when $d \geq 2$.

**Example 4.2.** Let's determine the number of digits in $100!$. The number of digits in a positive integer $N$ is $\lfloor \log_{10}(N) \rfloor + 1$, so we want to compute $\lfloor \log_{10}(100!) \rfloor + 1$. From (1.1),

$$\log_{10}(100!) = \frac{\log(100!)}{\log(10)} \approx \frac{100.5\log(100) - 100 + \frac{1}{2}\log(2\pi)}{\log(10)} \approx 157.96.$$

To pin down the approximation well enough to be sure that $\lfloor \log_{10}(100!) \rfloor$ is $157$ (and not $158$), we use a sharper form of Stirling's formula having upper and lower bounds:

$$1 < \frac{n!}{(n^n/e^n)\sqrt{2\pi n}} < e^{1/12n}.$$

Taking logarithms,

$$0 < \log(n!) - \left(n + \frac{1}{2}\right)\log n - n + \frac{1}{2}\log(2\pi) < \frac{1}{12n}.$$

Dividing by $\log 10$,

$$0 < \log_{10}(n!) - \frac{(n + 1/2)\log n - n + (1/2)\log(2\pi)}{\log 10} < \frac{1}{12n\log 10}.$$

Let $S_n$ be the term subtracted from $\log_{10}(n!)$ above. Since $1/(12n\log 10) \leq 1/12\log 10 \approx .036 < 1$, $\lfloor \log_{10}(n!) \rfloor$ is either $\lfloor S_n \rfloor$ or $\lfloor S_n \rfloor + 1$.

Taking $n = 100$, the difference between $\log_{10}(100!)$ and $S_{100}$ is bounded above by $\frac{1}{1200\log 10} \approx .00036$. Since $S_{100} \approx 157.96\ldots$ differs from its nearest integer by more than $.00036$, $\lfloor \log_{10}(100!) \rfloor = 157$ and thus $100!$ has $158$ digits. In a similar way, $1000!$ has $2568$ digits and $10000!$ has $35660$ digits.

Since $1/(12n\log 10) \to 0$, heuristically we expect $\lfloor \log_{10}(n!) \rfloor = \lfloor S_n \rfloor$ most of the time, but in rare instances an integer falls between $\lfloor \log_{10}(n!) \rfloor$ and $\lfloor S_n \rfloor$. The first $n$ where this happens, making $\lfloor \log_{10}(n!) \rfloor$ equal to $\lfloor S_n \rfloor + 1$ rather than $\lfloor S_n \rfloor$, is the $13$-digit number $n = 6{,}561{,}101{,}970{,}383$. See [8].

**Example 4.3.** For each positive integer $n$, the volume $V_n$ of the unit ball in $\mathbf{R}^n$ is $\pi^{n/2}/\Gamma(n/2 + 1)$, where $\Gamma(t) = \int_0^{\infty} x^{t-1}e^{-x}\, dx$ for $t > 0$, so $n! = \Gamma(n+1)$. In one, two, and three dimensions the number $V_n$ is $2$, $\pi$, and $(4/3)\pi$, which is increasing. But for large $n$, $V_n$ actually *tends to $0$*. (In fact $V_n$ is increasing for $1 \leq n \leq 5$ and decreasing for $n \geq 5$.) For even $n$, $V_n = \pi^{n/2}/(n/2)!$ so by Stirling's formula $V_n \sim \left(\frac{2\pi e}{n}\right)^{n/2} \frac{1}{\sqrt{\pi n}}$, which tends to $0$ as $n \to \infty$. The same asymptotic estimate holds for odd $n$ using an extension of Stirling's formula to the $\Gamma$-function.

<!-- page 7 -->

**Example 4.4.** The Bernoulli numbers $B_n$ are defined by $x/(e^x - 1) = \sum_{n \geq 0} (B_n/n!)x^n$. They begin as

$$B_0 = 1,\ B_1 = -\frac{1}{2},\ B_2 = \frac{1}{6},\ B_3 = 0,\ B_4 = -\frac{1}{30},\ B_5 = 0,\ B_6 = \frac{1}{42},\ B_7 = 0,\ \ldots.$$

For odd $n > 1$, $B_n = 0$. This sequence is important in number theory (values of the Riemann zeta-function and early work on Fermat's last theorem depend on them), topology (counting exotic spheres), and numerical analysis (the Euler--Maclaurin summation formula). Initial data suggest $B_n$ is small for even $n$, but this is misleading: $|B_n| \to \infty$. For instance, $|B_{20}| \approx 529$ and $|B_{100}|$ has $79$ digits before the decimal point. Using Stirling's formula and the Riemann zeta-function, we will give an asymptotic estimate on how large the even-indexed Bernoulli numbers are.

For $s > 1$, the Riemann zeta-function $\zeta(s) = \sum_{n \geq 1} 1/n^s$ converges and Euler gave a formula for it at positive even integers: for each positive integer $k$,

$$\zeta(2k) = \frac{(2\pi)^{2k}|B_{2k}|}{2(2k)!}.$$

As $s \to \infty$ we have $\zeta(s) \to 1$, so as $k \to \infty$ Stirling's formula tells us

$$|B_{2k}| = \frac{2(2k)!\zeta(2k)}{(2\pi)^{2k}} \sim \frac{2(2k)!}{(2\pi)^{2k}} \sim \frac{2(2k/e)^{2k}\sqrt{2\pi(2k)}}{(2\pi)^{2k}} = 4\sqrt{\pi k}\left(\frac{k}{\pi e}\right)^{2k}.$$

Thus $|B_{2k}|$ tends to $\infty$ very rapidly as $k \to \infty$.

## 5. History of Stirling's Formula

Stirling's formula first arose from correspondence between Stirling and DeMoivre in the 1720s about DeMoivre's work on approximating a binomial distribution by a normal distribution. DeMoivre had essentially discovered the Central Limit Theorem for the normal approximation to the binomial distribution. The Central Limit Theorem is nowadays proved without Stirling's formula, and for special types of probability distributions it leads to proofs of Stirling's formula [7], [15], [20].

What DeMoivre showed in his work on approximating a binomial distribution was that $\binom{2n}{n}\frac{1}{2^{2n}} \approx 2.168\frac{(1 - 1/2n)^{2n}}{\sqrt{2n-1}}$, with $2.168$ being an approximation to a constant that DeMoivre could express only as an infinite series. For large $n$, $(1 - 1/2n)^{2n} \approx 1/e$ and $\sqrt{2n-1} \approx \sqrt{2}\sqrt{n}$, so DeMoivre's approximation is essentially $(2.168/\sqrt{2e})/\sqrt{n}$. Stirling found the "true" value of $2.168$ to be $e\sqrt{2/\pi}$, which turns DeMoivre's approximation into $1/\sqrt{\pi n}$, as we found in Example 4.1.

Stirling's treatment of approximations to $\log(n!)$ appeared in his book *Methodus Differentialis* [22], as Example 2 after Proposition 28. An English translation is in [23, pp. 149--151]. Stirling's contribution to the asymptotic estimate for $\log(n!)$ that is named after him is in the identification of the constant in the formula as $\frac{1}{2}\log(2\pi) = \log\sqrt{2\pi}$ (without proof). How did he realize the constant involves $\pi$? According to [13, p. 481], Stirling tabulated $\log(n!)$, interpolated the sequence to factorials of half-integers, and observed agreement of $(-1/2)!$ with $\sqrt{\pi}$ to $10$ decimal places. Tweddle [23, p. 271] suggests Stirling found the link with $\pi$ through recognizing it in a numerical approximation or by a skillful use of the Wallis product for $\pi$. In any case, DeMoivre proved $\binom{2n}{n}\frac{1}{2^{2n}} \sim 1/\sqrt{\pi n}$ using the Wallis product for $\pi$ in his book *Miscellanea Analytica* [6]. A discussion of DeMoivre's work on this problem is in [13, Chap. 24].

Stirling's formula in the form $\log(n!) = n\log n - n + \frac{1}{2}\log(n) + \log\sqrt{2\pi} + \varepsilon_n$, where $\varepsilon_n \to 0$ as $n \to \infty$, can be refined to an asymptotic expansion called Stirling's series that replaces

<!-- page 8 -->

$\varepsilon_n$ with a series in powers of $1/n$. This expansion is due to DeMoivre; a version using a series in powers of $1/(n + 1/2)$ was found earlier by Stirling [12].

Here is a summary of different ways that proofs of Stirling's formula bring in $\pi$.

1. The Wallis product for $\pi/2$: [5], [10].
2. The Gaussian integral: [3], [7], [11], [14], [15], [16], [19], [20], [21], [24].
3. In [1, Sect. 2.5, Chap. 5], the proof uses the formula $\Gamma(z)\Gamma(1-z) = \pi/\sin(\pi z)$.
4. In [2, p. 24] the proof uses $\Gamma(1/2) = \sqrt{\pi}$.
5. In [4], the proof uses $\sqrt{n}/2^{n-1} = \prod_{k=1}^n \sin(k\pi/2n)$.
6. In [9], $\pi$ comes from the formula $\prod_{n \geq 1}(1 - x^2/n^2) = \sin(\pi x)/(\pi x)$.

## References

[1] L. Ahlfors, *Complex Analysis*, 3rd ed., McGraw-Hill, New York, 1979.

[2] E. Artin, *The Gamma Function*, Holt, Reinhart, Winston, New York, 1964.

[3] C. R. Blyth and P. K. Pathak, "A Note on Easy Proofs of Stirling's formula," Amer. Math. Monthly **93** (1986), 376--379.

[4] R. B. Burckel, "Stirling's Formula via Riemann Sums," College Math. Journal **37** (2006), 300--307.

[5] A. J. Coleman, "A simple proof of Stirling's formula," Amer. Math. Monthly **58** (1951), 334--336.

[6] A. DeMoivre, *Miscellanea Analytica*, London, 1730.

[7] P. Diaconis and D. Freedman, "An Elementary Proof of Stirling's formula," Amer. Math. Monthly **93** (1986), 123--125.

[8] N. D. Elkies, http://mathoverflow.net/questions/19170/how-good-is-kamenetskys-formula-for-the-number-of-digits-in-n-factorial.

[9] W. Feller, "A Direct Proof of Stirling's Formula," Amer. Math. Monthly **74** (1967), 1223--1225.

[10] D. Fowler, "The Factorial Functions: Stirling's Formula," Math. Gazette, **84** (2000), 42--50.

[11] C. L. Frenzen, "A New Elementary Proof of Stirling's Formula," Math. Magazine **68** (1995), 55--58.

[12] J. Gelinas, Original proofs of Stirling's series for $\log(n!)$, https://arxiv.org/abs/1701.06689.

[13] A. Hald, *A History of Probability and Statistics and their Applications before 1750*, Wiley, New York, 1990.

[14] W. K. Hayman, "A Generalisation of Stirling's Formula," J. Reine Angew. Math., **196** (1956), 67--95.

[15] R. A. Khan, "A probabilistic proof of Stirling's Formula," Amer. Math. Monthly **81** (1974), 366--369.

[16] G. Marsaglia and J. C. W. Marsaglia, "A New Derivation of Stirling's Approximation to $n!$," Amer. Math. Monthly **97** (1990), 826--829.

[17] R. Michel, "On Stirling's Formula," Amer. Math. Monthly **109** (2002), 388--390.

[18] R. Michel, "The $(n+1)$-th Proof of Stirling's Formula," Amer. Math. Monthly **115** (2008), 844--845.

[19] J. M. Patin, "A very short proof of Stirling's formula," Amer. Math. Monthly **96** (1989), 41--42.

[20] M. A. Pinsky, "Stirling's Formula via the Poisson Distribution," Amer. Math. Monthly **114** (2007), 256--258.

[21] D. Romik, "Stirling's Approximation for $n!$: the Ultimate Short Proof?", Amer. Math. Monthly **107** (2000), 556--557.

[22] J. Stirling, *Methodus Differentialis: sive Tractatus de Summatione et Interpolatione Serierum Infinitarum*, London, 1730.

[23] I. Tweddle, James Stirling's *Methodus Differentialis*: An Annotated Translation of Stirling's Text, Springer-Verlag, London, 2003.

[24] C. S. Wong, "A Note on the Central Limit Theorem," Amer. Math. Monthly **84** (1977), 472.
