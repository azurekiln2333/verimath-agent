# Series for the Logarithm and Arctangent

> **Source**: https://kconrad.math.uconn.edu/blurbs/logarctan.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis

<!-- page 1 -->

## 1. Introduction

The purpose of this handout is twofold: review the derivation of the identities
$$
\log(1 + x) = \sum_{n \geq 1} (-1)^{n-1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} - \frac{x^6}{6} + \cdots \tag{1.1}
$$
and
$$
\arctan x = \sum_{n \geq 0} (-1)^n \frac{x^{2n+1}}{2n + 1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \frac{x^9}{9} - \frac{x^{11}}{11} + \cdots \tag{1.2}
$$
for $0 \leq x \leq 1$ and extend them to a range which includes negative values of $x$. Specifically, we want to show (1.1) is true for $-1 < x \leq 1$ and (1.2) is true for $-1 \leq x \leq 1$.

The main idea in both cases is an integration formula:
$$
\log(1 + x) = \int_0^x \frac{\mathrm{d}t}{1 + t}, \quad \arctan x = \int_0^x \frac{\mathrm{d}t}{1 + t^2}.
$$
These formulas connect both functions with the simpler function (integrand) $1/(1 - t)$ under a change of variables.

## 2. Geometric Series and Integration

We start with the finite geometric series
$$
1 + t + t^2 + \cdots + t^N = \frac{t^{N+1} - 1}{t - 1} = \frac{1 - t^{N+1}}{1 - t}.
$$
Here $t \neq 1$. We isolate the term $1/(1 - t)$:
$$
\frac{1}{1 - t} = 1 + t + t^2 + \cdots + t^N + \frac{t^{N+1}}{1 - t}. \tag{2.1}
$$
Again, this is valid for $t \neq 1$. Now we make two different changes of variable to turn the left side of (2.1) into an integrand adapted to the logarithm and arctangent functions. Replacing $t$ with $-t$ in (2.1) gives
$$
\begin{aligned}
\frac{1}{1 + t} &= 1 - t + t^2 + \cdots + (-1)^N t^N + (-1)^{N+1} \frac{t^{N+1}}{1 + t} \\
&= \sum_{n=0}^N (-1)^n t^n + (-1)^{N+1} \frac{t^{N+1}}{1 + t}. \tag{2.2}
\end{aligned}
$$
Here we must have $t \neq -1$.

<!-- page 2 -->

Replacing $t$ with $-t^2$ in (2.1) gives
$$
\begin{aligned}
\frac{1}{1 + t^2} &= 1 - t^2 + t^4 + \cdots + (-1)^N t^{2N} + (-1)^{N+1} \frac{t^{2(N+1)}}{1 + t^2} \\
&= \sum_{n=0}^N (-1)^n t^{2n} + (-1)^{N+1} \frac{t^{2(N+1)}}{1 + t^2}. \tag{2.3}
\end{aligned}
$$
Here $t$ can be any number: the denominator doesn't become 0 since $t^2$ is never $-1$.

These formulas for $1/(1 + t)$ and for $1/(1 + t^2)$ will now be integrated from 0 to $x$ (for variable $x$). Well, we have to make sure $-1$ is not between 0 and $x$ in the case of (2.2) since $1/(1 + t)$ blows up at $t = -1$. We will apply $\int_0^x (\cdots)\,\mathrm{d}t$ to (2.2) with $x > -1$. We obtain
$$
\int_0^x \frac{\mathrm{d}t}{1 + t} = \sum_{n=0}^N (-1)^n \int_0^x t^n\,\mathrm{d}t + (-1)^{N+1} \int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t,
$$
which is the same as
$$
\begin{aligned}
\log(1 + x) &= \sum_{n=0}^N (-1)^n \frac{x^{n+1}}{n + 1} + (-1)^{N+1} \int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t \\
&= \sum_{n=1}^{N+1} (-1)^{n-1} \frac{x^n}{n} + (-1)^{N+1} \int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t. \tag{2.4}
\end{aligned}
$$
Now put the sum on one side and the other terms on the other side:
$$
\sum_{n=1}^{N+1} (-1)^{n-1} \frac{x^n}{n} = \log(1 + x) + (-1)^N \int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t. \tag{2.5}
$$
Similarly, applying $\int_0^x (\cdots)\,\mathrm{d}t$ to (2.3) gives
$$
\int_0^x \frac{\mathrm{d}t}{1 + t^2} = \sum_{n=0}^N (-1)^n \int_0^x t^{2n}\,\mathrm{d}t + (-1)^{N+1} \int_0^x \frac{t^{2(N+1)}}{1 + t^2}\,\mathrm{d}t,
$$
which is the same as
$$
\arctan x = \sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{2n + 1} + (-1)^{N+1} \int_0^x \frac{t^{2(N+1)}}{1 + t^2}\,\mathrm{d}t.
$$
Isolating the sum on one side yields, after some algebra,
$$
\sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{2n + 1} = \arctan x + (-1)^N \int_0^x \frac{t^{2(N+1)}}{1 + t^2}\,\mathrm{d}t. \tag{2.6}
$$

Our remaining task is to show, for *suitable* fixed $x$, that the definite integrals on the right sides of (2.5) and (2.6) tend to 0 as $N \to \infty$. When that happens we obtain the series representations (1.1) and (1.2) for those values of $x$.

From this point of view, the important issue concerning the definite integrals in (2.5) and (2.6) is not to compute them exactly, but to *estimate* them and show in favorable cases through these estimates that the integrals tend to 0 as $N \to \infty$.

<!-- page 3 -->

## 3. The Logarithm Case

For the logarithm series (2.5), we will show
$$
\lim_{N \to \infty} \int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t = 0 \tag{3.1}
$$
for each $x$ in the half-open interval $(-1, 1]$.

First suppose $0 \leq x \leq 1$. When $t \in [0, x]$ we have
$$
0 \leq \frac{t^{N+1}}{1 + t} \leq t^{N+1}.
$$
Integrating these inequalities over the interval $[0, x]$ gives
$$
0 \leq \int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t \leq \int_0^x t^{N+1}\,\mathrm{d}t = \frac{x^{N+2}}{N + 2} \leq \frac{1}{N + 2}.
$$
Our integral of interest is squeezed between 0 and $1/(N + 2)$. As $N \to \infty$ the upper bound tends to 0, so (3.1) has been verified when $0 \leq x \leq 1$.

Now suppose $-1 < x < 0$. Write $x = -y$ with $0 < y < 1$. Then, using the change of variables $u = -t$,
$$
\begin{aligned}
\int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t &= (-1)^N \int_0^{-x} \frac{u^{N+1}}{1 - u}\,\mathrm{d}u \\
&= (-1)^N \int_0^y \frac{u^{N+1}}{1 - u}\,\mathrm{d}u.
\end{aligned}
$$
The integrand $u^{N+1}/(1 - u)$ is nonnegative for $0 \leq u \leq y$, so
$$
\left|\int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t\right| = \int_0^y \frac{u^{N+1}}{1 - u}\,\mathrm{d}u.
$$
To get an upper bound on the integral we replace the denominator $1 - u$ by the lower bound $1 - y$:
$$
0 \leq u \leq y \implies \frac{u^{N+1}}{1 - u} \leq \frac{u^{N+1}}{1 - y}.
$$
Therefore
$$
\left|\int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t\right| = \int_0^y \frac{u^{N+1}}{1 - u}\,\mathrm{d}u \leq \int_0^y \frac{u^{N+1}}{1 - y}\,\mathrm{d}u. \tag{3.2}
$$
Since $0 < y < 1$,
$$
\begin{aligned}
\int_0^y \frac{u^{N+1}}{1 - y}\,\mathrm{d}u &= \frac{1}{1 - y} \int_0^y u^{N+1}\,\mathrm{d}u \\
&= \frac{y^{N+2}}{(N + 2)(1 - y)} \\
&\leq \frac{1}{(N + 2)(1 - y)} \\
&= \frac{1}{(N + 2)(1 + x)}.
\end{aligned}
$$

<!-- page 4 -->

Feeding this back into (3.2) gives
$$
\left|\int_0^x \frac{t^{N+1}}{1 + t}\,\mathrm{d}t\right| \leq \frac{1}{(N + 2)(1 + x)}.
$$
For each $x$ in $(-1, 0)$, this upper bound tends to 0 as $N \to \infty$.

We have completed the derivation of (1.1) for $-1 < x \leq 1$.

## 4. The Arctangent Case

In (2.6) we want to show
$$
\lim_{N \to \infty} \int_0^x \frac{t^{2(N+1)}}{1 + t^2}\,\mathrm{d}t = 0
$$
for each $x$ in the closed interval $[-1, 1]$.

First we suppose $0 \leq x \leq 1$. If $0 \leq t \leq x$ then
$$
0 \leq \frac{t^{2(N+1)}}{1 + t^2} \leq t^{2(N+1)},
$$
so
$$
0 \leq \int_0^x \frac{t^{2(N+1)}}{1 + t^2}\,\mathrm{d}t \leq \int_0^x t^{2(N+1)}\,\mathrm{d}t = \frac{x^{2N+3}}{2N + 3} \leq \frac{1}{2N + 3}.
$$
As $N \to \infty$, the upper bound tends to 0 so the integral tends to 0.

Now suppose $-1 \leq x < 0$. Write $x = -y$ where $0 < y \leq 1$. Then, using the substitution $u = -t$,
$$
\int_0^x \frac{t^{2(N+1)}}{1 + t^2}\,\mathrm{d}t = -\int_0^{-x} \frac{u^{2(N+1)}}{1 + u^2}\,\mathrm{d}u = -\int_0^y \frac{u^{2(N+1)}}{1 + u^2}\,\mathrm{d}u.
$$
The integral on the right is exactly the kind we treated already: as $N \to \infty$ it tends to 0.

This completes the derivation of (1.2) for $-1 \leq x \leq 1$.
