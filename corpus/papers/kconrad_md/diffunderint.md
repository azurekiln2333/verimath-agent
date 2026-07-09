# Differentiating Under the Integral Sign

> **Source**: https://kconrad.math.uconn.edu/blurbs/diffunderint.pdf
> **Author**: Keith Conrad
> **Topic**: analysis

<!-- page 1 -->

I had learned to do integrals by various methods shown in a book[^1] that my high school physics teacher Mr. Bader had given me. [It] showed how to differentiate parameters under the integral sign -- it's a certain operation. It turns out that's not taught very much in the universities; they don't emphasize it. But I caught on how to use that method, and I used that one damn tool again and again. [If] guys at MIT or Princeton had trouble doing a certain integral, [then] I come along and try differentiating under the integral sign, and often it worked. So I got a great reputation for doing integrals, only because my box of tools was different from everybody else's, and they had tried all their tools on it before giving the problem to me.[^2]

Richard Feynman [5, pp. 71--72][^3]

## 1. Introduction

The method of differentiation under the integral sign, due to Leibniz in 1697 [4], concerns integrals depending on a parameter, such as $\int_0^1 x^2 e^{-tx}\,\mathrm{d}x$. Here $t$ is the extra parameter. (Since $x$ is the variable of integration, $x$ is *not* a parameter.) In general, we might write such an integral as

$$\int_a^b f(x,t)\,\mathrm{d}x, \tag{1.1}$$

where $f(x,t)$ is a function of two variables like $f(x,t) = x^2 e^{-tx}$.

**Example 1.1.** Let $f(x,t) = (2x + t^3)^2$. Then $\int_0^1 f(x,t)\,\mathrm{d}x = \int_0^1 (2x + t^3)^2\,\mathrm{d}x$. An anti-derivative of $(2x + t^3)^2$ with respect to $x$ is $\frac{1}{6}(2x + t^3)^3$, so

$$\int_0^1 (2x + t^3)^2\,\mathrm{d}x = \left.\frac{(2x+t^3)^3}{6}\right|_{x=0}^{x=1} = \frac{(2+t^3)^3 - t^9}{6} = \frac{4}{3} + 2t^3 + t^6.$$

This answer is a function of $t$, which makes sense since the integrand depends on $t$. We integrate over $x$ and are left with something that depends only on $t$, not $x$.

An integral like $\int_a^b f(x,t)\,\mathrm{d}x$ is a function of $t$, so we can ask about its $t$-derivative, assuming that $f(x,t)$ is nicely behaved. The rule, called *differentiation under the integral sign*, is that the $t$-derivative of the integral of $f(x,t)$ is the integral of the $t$-derivative of $f(x,t)$:

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_a^b f(x,t)\,\mathrm{d}x = \int_a^b \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x. \tag{1.2}$$

<!-- page 2 -->

If you are used to thinking mostly about functions with one variable, not two, keep in mind that (1.2) involves integrals and derivatives with respect to *separate* variables: integration with respect to $x$ and differentiation with respect to $t$.

**Example 1.2.** We saw in Example 1.1 that $\int_0^1 (2x + t^3)^2\,\mathrm{d}x = 4/3 + 2t^3 + t^6$, whose $t$-derivative is $6t^2 + 6t^5$. According to (1.2), we can also compute the $t$-derivative of the integral like this:

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_0^1 (2x+t^3)^2\,\mathrm{d}x = \int_0^1 \frac{\partial}{\partial t}(2x+t^3)^2\,\mathrm{d}x$$
$$= \int_0^1 2(2x+t^3)(3t^2)\,\mathrm{d}x$$
$$= \int_0^1 (12t^2 x + 6t^5)\,\mathrm{d}x$$
$$= \left.6t^2 x^2 + 6t^5 x\right|_{x=0}^{x=1}$$
$$= 6t^2 + 6t^5.$$

The answer agrees with our first, more direct, calculation.

We will apply (1.2) in many examples, and Section 12 presents a justification. It is also used to prove theorems: see Sections 11 and 13 and a proof of the Cramer--Rao bound in statistics.

## 2. Euler's Factorial Integral in a New Light

For integers $n \geq 0$, Euler's integral formula for $n!$ is

$$\int_0^\infty x^n e^{-x}\,\mathrm{d}x = n!, \tag{2.1}$$

which can be obtained by repeated integration by parts starting from the formula

$$\int_0^\infty e^{-x}\,\mathrm{d}x = 1 \tag{2.2}$$

when $n = 0$. Now we are going to derive Euler's formula in another way, by repeated differentiation after introducing a parameter $t$ into (2.2).

For $t > 0$, let $x = tu$. Then $\mathrm{d}x = t\,\mathrm{d}u$ and (2.2) becomes

$$\int_0^\infty t e^{-tu}\,\mathrm{d}u = 1.$$

Dividing by $t$ and writing $u$ as $x$ (why is this not a problem?), we get

$$\int_0^\infty e^{-tx}\,\mathrm{d}x = \frac{1}{t}. \tag{2.3}$$

This is a parametric form of (2.2), where both sides are now functions of $t$. We need $t > 0$ in order that $e^{-tx}$ is integrable over the region $x \geq 0$.

Now we bring in differentiation under the integral sign. Differentiate both sides of (2.3) with respect to $t$, using (1.2) to treat the left side. We obtain

$$\int_0^\infty -x e^{-tx}\,\mathrm{d}x = -\frac{1}{t^2},$$

<!-- page 3 -->

so

$$\int_0^\infty x e^{-tx}\,\mathrm{d}x = \frac{1}{t^2}. \tag{2.4}$$

Differentiate both sides of (2.4) with respect to $t$, again using (1.2) to handle the left side. We get

$$\int_0^\infty -x^2 e^{-tx}\,\mathrm{d}x = -\frac{2}{t^3}.$$

Taking out the sign on both sides,

$$\int_0^\infty x^2 e^{-tx}\,\mathrm{d}x = \frac{2}{t^3}. \tag{2.5}$$

If we continue to differentiate each new equation with respect to $t$ a few more times, we obtain

$$\int_0^\infty x^3 e^{-tx}\,\mathrm{d}x = \frac{6}{t^4},$$

$$\int_0^\infty x^4 e^{-tx}\,\mathrm{d}x = \frac{24}{t^5},$$

and

$$\int_0^\infty x^5 e^{-tx}\,\mathrm{d}x = \frac{120}{t^6}.$$

Do you see the pattern? It is

$$\int_0^\infty x^n e^{-tx}\,\mathrm{d}x = \frac{n!}{t^{n+1}}. \tag{2.6}$$

We have used the presence of the extra variable $t$ to get these equations by repeatedly applying $\mathrm{d}/\mathrm{d}t$. Now specialize $t$ to 1 in (2.6). We obtain

$$\int_0^\infty x^n e^{-x}\,\mathrm{d}x = n!,$$

which is our old friend (2.1). Voila!

The idea that made this work is introducing a parameter $t$, using calculus on $t$, and then setting $t$ to a particular value so it disappears from the final formula. In other words, sometimes *to solve a problem it is useful to solve a more general problem*. Compare (2.1) to (2.6).

## 3. A Damped Sine Integral

We are going to use differentiation under the integral sign to prove

$$\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2} - \arctan t \tag{3.1}$$

for $t > 0$.

Call this integral $F(t)$ and set $f(x,t) = e^{-tx}(\sin x)/x$, so $(\partial/\partial t)f(x,t) = -e^{-tx}\sin x$. Then

$$F'(t) = -\int_0^\infty e^{-tx}(\sin x)\,\mathrm{d}x.$$

The integrand $e^{-tx}\sin x$, as a function of $x$, can be integrated by parts:

$$\int e^{ax}\sin x\,\mathrm{d}x = \frac{(a\sin x - \cos x)}{1 + a^2}e^{ax}.$$

<!-- page 4 -->

Applying this with $a = -t$ and turning the indefinite integral into a definite integral,

$$F'(t) = -\int_0^\infty e^{-tx}(\sin x)\,\mathrm{d}x = \left.\frac{(t\sin x + \cos x)}{1+t^2}e^{-tx}\right|_{x=0}^{x=\infty}.$$

As $x \to \infty$, $t\sin x + \cos x$ oscillates a lot, but in a bounded way (since $\sin x$ and $\cos x$ are bounded functions), while the term $e^{-tx}$ decays exponentially to 0 since $t > 0$. So the value at $x = \infty$ is 0. Therefore

$$F'(t) = -\int_0^\infty e^{-tx}(\sin x)\,\mathrm{d}x = -\frac{1}{1+t^2}.$$

We *know* an explicit antiderivative of $1/(1+t^2)$, namely $\arctan t$. Since $F(t)$ has the same $t$-derivative as $-\arctan t$, they differ by a constant: for some number $C$,

$$\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = -\arctan t + C \quad \text{for } t > 0. \tag{3.2}$$

We've computed the integral, up to an additive constant, without finding an antiderivative of $e^{-tx}(\sin x)/x$.

To compute $C$ in (3.2), let $t \to \infty$ on both sides. Since $|(\sin x)/x| \leq 1$, the absolute value of the integral on the left is bounded from above by $\int_0^\infty e^{-tx}\,\mathrm{d}x = 1/t$, so the integral on the left in (3.2) tends to 0 as $t \to \infty$. Since $\arctan t \to \pi/2$ as $t \to \infty$, equation (3.2) as $t \to \infty$ becomes $0 = -\pi/2 + C$, so $C = \pi/2$. Feeding this back into (3.2),

$$\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2} - \arctan t \quad \text{for } t > 0. \tag{3.3}$$

If we let $t \to 0^+$ in (3.3), this equation suggests that

$$\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2}, \tag{3.4}$$

which is true and it is important in signal processing and Fourier analysis. It is a delicate matter to derive (3.4) from (3.3) since the integral in (3.4) is not absolutely convergent. Details are provided in Appendix A.

## 4. The Gaussian Integral

The improper integral formula

$$\int_{-\infty}^\infty e^{-x^2/2}\,\mathrm{d}x = \sqrt{2\pi} \tag{4.1}$$

is fundamental to probability theory and Fourier analysis. The function $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ is called a Gaussian, and (4.1) says the integral of the Gaussian over the whole real line is 1.

To prove (4.1) using differentiation under the integral sign, we are going to aim not at (4.1), but at an equivalent formula over the range $x \geq 0$:

$$\int_0^\infty e^{-x^2/2}\,\mathrm{d}x = \frac{\sqrt{2\pi}}{2} = \sqrt{\frac{\pi}{2}}. \tag{4.2}$$

Call the integral on the left $I$.

For $t \in \mathbf{R}$, set

$$F(t) = \int_0^\infty \frac{e^{-t^2(1+x^2)/2}}{1+x^2}\,\mathrm{d}x.$$

<!-- page 5 -->

Then $F(0) = \int_0^\infty \mathrm{d}x/(1+x^2) = \pi/2$ and $F(\infty) = 0$. Differentiating under the integral sign,

$$F'(t) = \int_0^\infty -t e^{-t^2(1+x^2)/2}\,\mathrm{d}x = -t e^{-t^2/2}\int_0^\infty e^{-(tx)^2/2}\,\mathrm{d}x.$$

Make the substitution $y = tx$, with $\mathrm{d}y = t\,\mathrm{d}x$, so

$$F'(t) = -e^{-t^2/2}\int_0^\infty e^{-y^2/2}\,\mathrm{d}y = -I e^{-t^2/2}.$$

For $b > 0$, integrate both sides from 0 to $b$ and use the Fundamental Theorem of Calculus:

$$\int_0^b F'(t)\,\mathrm{d}t = -I\int_0^b e^{-t^2/2}\,\mathrm{d}t \implies F(b) - F(0) = -I\int_0^b e^{-t^2/2}\,\mathrm{d}t.$$

Letting $b \to \infty$,

$$0 - \frac{\pi}{2} = -I^2 \implies I^2 = \frac{\pi}{2} \implies I = \sqrt{\frac{\pi}{2}}.$$

I learned this approach from Michael Rozman [12], who modified an idea on a Math Stackexchange question [3], and in a slightly less elegant form it appeared much earlier in [17].

By the same method we can calculate $I_z = \int_0^\infty e^{-zx^2/2}\,\mathrm{d}x$ for $z \in \mathbf{C}$ with $\mathrm{Re}(z) > 0$, so $I = I_1$. Generalizing $I^2 = \pi/2$, we get $I_z^2 = \pi/(2z)$, so $I_z = \pm\sqrt{\pi/2}/\sqrt{z}$, where $\sqrt{z}$ is the principal square root (with argument in $(-\pi/4, \pi/4)$). The sign on the right side is $+$ when $z = 1$, so by continuity in $z$ we have $I_z = \sqrt{\pi/2}/\sqrt{z}$ for all $z$ with $\mathrm{Re}(z) > 0$.

## 5. Higher Moments of the Gaussian

For every integer $n \geq 0$ we want to compute a formula for

$$\int_{-\infty}^\infty x^n e^{-x^2/2}\,\mathrm{d}x. \tag{5.1}$$

(Integrals of the type $\int x^n f(x)\,\mathrm{d}x$ for $n = 0, 1, 2, \ldots$ are called the *moments* of $f(x)$, so (5.1) is the $n$-th moment of the Gaussian.) When $n$ is odd, (5.1) vanishes since $x^n e^{-x^2/2}$ is an odd function. What if $n = 0, 2, 4, \ldots$ is even?

The first case, $n = 0$, is the Gaussian integral (4.1):

$$\int_{-\infty}^\infty e^{-x^2/2}\,\mathrm{d}x = \sqrt{2\pi}. \tag{5.2}$$

To get formulas for (5.1) when $n \neq 0$, we follow the same strategy as our treatment of the factorial integral in Section 2: stick a $t$ into the exponent of $e^{-x^2/2}$ and then differentiate repeatedly with respect to $t$.

For $t > 0$, replacing $x$ with $\sqrt{t}\,x$ in (5.2) gives

$$\int_{-\infty}^\infty e^{-tx^2/2}\,\mathrm{d}x = \frac{\sqrt{2\pi}}{\sqrt{t}}. \tag{5.3}$$

Differentiate both sides of (5.3) with respect to $t$, using differentiation under the integral sign on the left:

$$\int_{-\infty}^\infty -\frac{x^2}{2}e^{-tx^2/2}\,\mathrm{d}x = -\frac{\sqrt{2\pi}}{2t^{3/2}},$$

so

$$\int_{-\infty}^\infty x^2 e^{-tx^2/2}\,\mathrm{d}x = \frac{\sqrt{2\pi}}{t^{3/2}}. \tag{5.4}$$

<!-- page 6 -->

Differentiate both sides of (5.4) with respect to $t$. After removing a common factor of $-1/2$ on both sides, we get

$$\int_{-\infty}^\infty x^4 e^{-tx^2/2}\,\mathrm{d}x = \frac{3\sqrt{2\pi}}{t^{5/2}}. \tag{5.5}$$

Differentiating both sides of (5.5) with respect to $t$ a few more times, we get

$$\int_{-\infty}^\infty x^6 e^{-tx^2/2}\,\mathrm{d}x = \frac{3 \cdot 5\sqrt{2\pi}}{t^{7/2}},$$

$$\int_{-\infty}^\infty x^8 e^{-tx^2/2}\,\mathrm{d}x = \frac{3 \cdot 5 \cdot 7\sqrt{2\pi}}{t^{9/2}},$$

and

$$\int_{-\infty}^\infty x^{10} e^{-tx^2/2}\,\mathrm{d}x = \frac{3 \cdot 5 \cdot 7 \cdot 9\sqrt{2\pi}}{t^{11/2}}.$$

Quite generally, when $n$ is even

$$\int_{-\infty}^\infty x^n e^{-tx^2/2}\,\mathrm{d}x = \frac{1 \cdot 3 \cdot 5 \cdots (n-1)}{t^{(n+1)/2}}\sqrt{2\pi},$$

where the numerator is the product of the positive odd integers from 1 to $n-1$ (understood to be the empty product 1 when $n = 0$).

In particular, taking $t = 1$ we have computed (5.1):

$$\int_{-\infty}^\infty x^n e^{-x^2/2}\,\mathrm{d}x = 1 \cdot 3 \cdot 5 \cdots (n-1)\sqrt{2\pi}.$$

As an application of (5.4), we now compute $(\tfrac{1}{2})! := \int_0^\infty x^{1/2}e^{-x}\,\mathrm{d}x$, where the notation $(\tfrac{1}{2})!$ and its definition are inspired by Euler's integral formula (2.1) for $n!$ when $n$ is a nonnegative integer. Using the substitution $u = x^{1/2}$ in $\int_0^\infty x^{1/2}e^{-x}\,\mathrm{d}x$, we have

$$\left(\frac{1}{2}\right)! = \int_0^\infty x^{1/2}e^{-x}\,\mathrm{d}x$$
$$= \int_0^\infty u e^{-u^2}(2u)\,\mathrm{d}u$$
$$= 2\int_0^\infty u^2 e^{-u^2}\,\mathrm{d}u$$
$$= \int_{-\infty}^\infty u^2 e^{-u^2}\,\mathrm{d}u$$
$$= \frac{\sqrt{2\pi}}{2^{3/2}} \quad \text{by (5.4) at } t = 2$$
$$= \frac{\sqrt{\pi}}{2}.$$

## 6. A Cosine Transform of the Gaussian

We are going to compute

$$F(t) = \int_0^\infty \cos(tx)e^{-x^2/2}\,\mathrm{d}x$$

<!-- page 7 -->

by looking at its $t$-derivative:

$$F'(t) = \int_0^\infty -x\sin(tx)e^{-x^2/2}\,\mathrm{d}x. \tag{6.1}$$

This is *good* from the viewpoint of integration by parts since $-xe^{-x^2/2}$ is the derivative of $e^{-x^2/2}$. So we apply integration by parts to (6.1):

$$u = \sin(tx), \quad \mathrm{d}v = -xe^{-x^2}\,\mathrm{d}x$$

and

$$\mathrm{d}u = t\cos(tx)\,\mathrm{d}x, \quad v = e^{-x^2/2}.$$

Then

$$F'(t) = \int_0^\infty u\,\mathrm{d}v$$
$$= \left.uv\right|_0^\infty - \int_0^\infty v\,\mathrm{d}u$$
$$= \left.\frac{\sin(tx)}{e^{x^2/2}}\right|_{x=0}^{x=\infty} - t\int_0^\infty \cos(tx)e^{-x^2/2}\,\mathrm{d}x$$
$$= \left.\frac{\sin(tx)}{e^{x^2/2}}\right|_{x=0}^{x=\infty} - tF(t).$$

As $x \to \infty$, $e^{x^2/2}$ blows up while $\sin(tx)$ stays bounded, so $\sin(tx)/e^{x^2/2}$ goes to 0. Therefore

$$F'(t) = -tF(t).$$

We *know* the solutions to this differential equation: constant multiples of $e^{-t^2/2}$. So

$$\int_0^\infty \cos(tx)e^{-x^2/2}\,\mathrm{d}x = Ce^{-t^2/2}$$

for some constant $C$. To find $C$, set $t = 0$. The left side is $\int_0^\infty e^{-x^2/2}\,\mathrm{d}x$, which is $\sqrt{\pi/2}$ by (4.2). The right side is $C$. Thus $C = \sqrt{\pi/2}$, so we are done: for all real $t$,

$$\int_0^\infty \cos(tx)e^{-x^2/2}\,\mathrm{d}x = \sqrt{\frac{\pi}{2}}e^{-t^2/2}.$$

**Remark 6.1.** If we want to compute $G(t) = \int_0^\infty \sin(tx)e^{-x^2/2}\,\mathrm{d}x$, with $\sin(tx)$ in place of $\cos(tx)$, then in place of $F'(t) = -tF(t)$ we have $G'(t) = 1 - tG(t)$, and $G(0) = 0$. From the differential equation, $(e^{t^2/2}G(t))' = e^{t^2/2}$, so $G(t) = e^{-t^2/2}\int_0^t e^{x^2/2}\,\mathrm{d}x$. So while $\int_0^\infty \cos(tx)e^{-x^2/2}\,\mathrm{d}x = \sqrt{\frac{\pi}{2}}e^{-t^2/2}$, the integral $\int_0^\infty \sin(tx)e^{-x^2/2}\,\mathrm{d}x$ is impossible to express in terms of elementary functions.

## 7. The Gaussian Times a Logarithm

We will compute

$$\int_0^\infty (\log x)e^{-x^2}\,\mathrm{d}x.$$

Integrability at $\infty$ follows from rapid decay of $e^{-x^2}$ at $\infty$, and integrability near $x = 0$ follows from the integrand there being nearly $\log x$, which is integrable on $[0,1]$, so the integral makes sense. (This example was brought to my attention by Harald Helfgott.)

<!-- page 8 -->

We already know $\int_0^\infty e^{-x^2}\,\mathrm{d}x = \sqrt{\pi}/2$, but how do we find the integral when a factor of $\log x$ is inserted into the integrand? Replacing $x$ with $\sqrt{x}$ in the integral,

$$\int_0^\infty (\log x)e^{-x^2}\,\mathrm{d}x = \frac{1}{4}\int_0^\infty \frac{\log x}{\sqrt{x}}e^{-x}\,\mathrm{d}x. \tag{7.1}$$

To compute this last integral, the key idea is that $(\mathrm{d}/\mathrm{d}t)(x^t) = x^t \log x$, so we get a factor of $\log x$ in an integral after differentiation under the integral sign if the integrand has an exponential parameter: for $t > -1$ set

$$F(t) = \int_0^\infty x^t e^{-x}\,\mathrm{d}x.$$

(This is integrable for $x$ near 0 since for small $x$, $x^t e^{-x} \approx x^t$, which is integrable near 0 since $t > -1$.) Differentiating both sides with respect to $t$,

$$F'(t) = \int_0^\infty x^t(\log x)e^{-x}\,\mathrm{d}x,$$

so (7.1) tells us the number we are interested in is $F'(-1/2)/4$.

The function $F(t)$ is well-known under a different name: for $s > 0$, the $\Gamma$-function at $s$ is defined by

$$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x}\,\mathrm{d}x,$$

so $\Gamma(s) = F(s-1)$. Therefore $\Gamma'(s) = F'(s-1)$, so $F'(-1/2)/4 = \Gamma'(1/2)/4$. For the rest of this section we work out a formula for $\Gamma'(1/2)/4$ using properties of the $\Gamma$-function; there is no more differentiation under the integral sign.

We need two standard identities for the $\Gamma$-function:

$$\Gamma(s+1) = s\Gamma(s), \quad \Gamma(s)\Gamma\!\left(s+\frac{1}{2}\right) = 2^{1-2s}\sqrt{\pi}\,\Gamma(2s). \tag{7.2}$$

The first identity follows from integration by parts. Since $\Gamma(1) = \int_0^\infty e^{-x}\,\mathrm{d}x = 1$, the first identity implies $\Gamma(n) = (n-1)!$ for every positive integer $n$. The second identity, called the duplication formula, is subtle. For example, at $s = 1/2$ it says $\Gamma(1/2) = \sqrt{\pi}$. A proof of the duplication formula can be found in many complex analysis textbooks. (The integral defining $\Gamma(s)$ makes sense not just for real $s > 0$, but also for complex $s$ with $\mathrm{Re}(s) > 0$, and the $\Gamma$-function is usually regarded as a function of a complex, rather than real, variable.)

Differentiating the first identity in (7.2),

$$\Gamma'(s+1) = s\Gamma'(s) + \Gamma(s), \tag{7.3}$$

so at $s = 1/2$

$$\Gamma'\!\left(\frac{3}{2}\right) = \frac{1}{2}\Gamma'\!\left(\frac{1}{2}\right) + \Gamma\!\left(\frac{1}{2}\right) = \frac{1}{2}\Gamma'\!\left(\frac{1}{2}\right) + \sqrt{\pi} \implies \Gamma'\!\left(\frac{1}{2}\right) = 2\left(\Gamma'\!\left(\frac{3}{2}\right) - \sqrt{\pi}\right). \tag{7.4}$$

Differentiating the second identity in (7.2),

$$\Gamma(s)\Gamma'\!\left(s+\frac{1}{2}\right) + \Gamma'(s)\Gamma\!\left(s+\frac{1}{2}\right) = 2^{1-2s}(-\log 4)\sqrt{\pi}\,\Gamma(2s) + 2^{1-2s}\sqrt{\pi}\,2\Gamma'(2s). \tag{7.5}$$

Setting $s = 1$ here and using $\Gamma(1) = \Gamma(2) = 1$,

$$\Gamma'\!\left(\frac{3}{2}\right) + \Gamma'(1)\Gamma\!\left(\frac{3}{2}\right) = (-\log 2)\sqrt{\pi} + \sqrt{\pi}\,\Gamma'(2). \tag{7.6}$$

<!-- page 9 -->

We compute $\Gamma(3/2)$ by the first identity in (7.2) at $s = 1/2$: $\Gamma(3/2) = (1/2)\Gamma(1/2) = \sqrt{\pi}/2$ (we already computed this at the end of Section 5). We compute $\Gamma'(2)$ by (7.3) at $s = 1$: $\Gamma'(2) = \Gamma'(1) + 1$. Thus (7.6) says

$$\Gamma'\!\left(\frac{3}{2}\right) + \Gamma'(1)\frac{\sqrt{\pi}}{2} = (-\log 2)\sqrt{\pi} + \sqrt{\pi}(\Gamma'(1) + 1) \implies \Gamma'\!\left(\frac{3}{2}\right) = \sqrt{\pi}\left(-\log 2 + \frac{\Gamma'(1)}{2}\right) + \sqrt{\pi}.$$

Feeding this formula for $\Gamma'(3/2)$ into (7.4),

$$\Gamma'\!\left(\frac{1}{2}\right) = \sqrt{\pi}(-2\log 2 + \Gamma'(1)).$$

It turns out that $\Gamma'(1) = -\gamma$, where $\gamma \approx .577$ is Euler's constant. Thus, at last,

$$\int_0^\infty (\log x)e^{-x^2}\,\mathrm{d}x = \frac{\Gamma'(1/2)}{4} = -\frac{\sqrt{\pi}}{4}(2\log 2 + \gamma).$$

## 8. Logs in the Denominator, Part I

Consider the following integral over $[0,1]$, where $t > 0$:

$$\int_0^1 \frac{x^t - 1}{\log x}\,\mathrm{d}x.$$

Since $1/\log x \to 0$ as $x \to 0^+$, the integrand vanishes at $x = 0$. As $x \to 1^-$, $(x^t - 1)/\log x \to t$. Therefore when $t$ is fixed the integrand is a continuous function of $x$ on $[0,1]$, so the integral is not an improper integral.

The $t$-derivative of this integral is

$$\int_0^1 \frac{x^t \log x}{\log x}\,\mathrm{d}x = \int_0^1 x^t\,\mathrm{d}x = \frac{1}{t+1},$$

which we recognize as the $t$-derivative of $\log(t+1)$. Therefore

$$\int_0^1 \frac{x^t - 1}{\log x}\,\mathrm{d}x = \log(t+1) + C$$

for some $C$. To find $C$, let $t \to 0^+$. On the right side, $\log(1+t)$ tends to 0. On the left side, the integrand tends to 0: $|(x^t - 1)/\log x| = |(e^{t\log x} - 1)/\log x| \leq t$ because $|e^a - 1| \leq |a|$ when $a \leq 0$. Therefore the integral on the left tends to 0 as $t \to 0^+$. So $C = 0$, which implies

$$\int_0^1 \frac{x^t - 1}{\log x}\,\mathrm{d}x = \log(t+1) \tag{8.1}$$

for all $t > 0$, and it's obviously also true for $t = 0$. Another way to compute this integral is to write $x^t = e^{t\log x}$ as a power series and integrate term by term, which is valid for $-1 < t < 1$.

Under the change of variables $x = e^{-y}$, (8.1) becomes

$$\int_0^\infty \left(e^{-y} - e^{-(t+1)y}\right)\frac{\mathrm{d}y}{y} = \log(t+1). \tag{8.2}$$

<!-- page 10 -->

## 9. Logs in the Denominator, Part II

We now consider the integral

$$F(t) = \int_2^\infty \frac{\mathrm{d}x}{x^t \log x}$$

for $t > 1$. The integral converges by comparison with $\int_2^\infty \mathrm{d}x/x^t$. We know that "at $t = 1$" the integral diverges to $\infty$:

$$\int_2^\infty \frac{\mathrm{d}x}{x\log x} = \lim_{b\to\infty}\int_2^b \frac{\mathrm{d}x}{x\log x}$$
$$= \lim_{b\to\infty}\left.\log\log x\right|_2^b$$
$$= \lim_{b\to\infty}\log\log b - \log\log 2$$
$$= \infty.$$

So we expect that as $t \to 1^+$, $F(t)$ should blow up. But *how* does it blow up? By analyzing $F'(t)$ and then integrating back, we are going to show $F(t)$ behaves essentially like $-\log(t-1)$ as $t \to 1^+$.

Using differentiation under the integral sign, for $t > 1$

$$F'(t) = \int_2^\infty \frac{\partial}{\partial t}\left(\frac{1}{x^t\log x}\right)\mathrm{d}x$$
$$= \int_2^\infty \frac{x^{-t}(-\log x)}{\log x}\,\mathrm{d}x$$
$$= -\int_2^\infty \frac{\mathrm{d}x}{x^t}$$
$$= -\left.\frac{x^{-t+1}}{-t+1}\right|_{x=2}^{x=\infty}$$
$$= \frac{2^{1-t}}{1-t}.$$

We want to bound this derivative from above and below when $t > 1$. Then we will integrate to get bounds on the size of $F(t)$.

For $t > 1$, the difference $1 - t$ is negative, so $2^{1-t} < 1$. Dividing both sides of this by $1 - t$, which is negative, reverses the sense of the inequality and gives

$$\frac{2^{1-t}}{1-t} > \frac{1}{1-t}.$$

This is a lower bound on $F'(t)$. To get an upper bound on $F'(t)$, we want to use a lower bound on $2^{1-t}$. Since $e^a \geq a + 1$ for all $a$ (the graph of $y = e^x$ lies on or above its tangent line at $x = 0$, which is $y = x + 1$),

$$2^x = e^{x\log 2} \geq (\log 2)x + 1$$

for all $x$. Taking $x = 1 - t$,

$$2^{1-t} \geq (\log 2)(1-t) + 1. \tag{9.1}$$

When $t > 1$, $1 - t$ is negative, so dividing (9.1) by $1 - t$ reverses the sense of the inequality:

$$\frac{2^{1-t}}{1-t} \leq \log 2 + \frac{1}{1-t}.$$

<!-- page 11 -->

This is an upper bound on $F'(t)$. Putting the upper and lower bounds on $F'(t)$ together,

$$\frac{1}{1-t} < F'(t) \leq \log 2 + \frac{1}{1-t} \tag{9.2}$$

for all $t > 1$.

We are concerned with the behavior of $F(t)$ as $t \to 1^+$. Let's integrate (9.2) from $a$ to 2, where $1 < a < 2$:

$$\int_a^2 \frac{\mathrm{d}t}{1-t} < \int_a^2 F'(t)\,\mathrm{d}t \leq \int_a^2 \left(\log 2 + \frac{1}{1-t}\right)\mathrm{d}t.$$

Using the Fundamental Theorem of Calculus,

$$\left.-\log(t-1)\right|_a^2 < \left.F(t)\right|_a^2 \leq \left.((\log 2)t - \log(t-1))\right|_a^2,$$

so

$$\log(a-1) < F(2) - F(a) \leq (\log 2)(2-a) + \log(a-1).$$

Manipulating to get inequalities on $F(a)$, we have

$$(\log 2)(a-2) - \log(a-1) + F(2) \leq F(a) < -\log(a-1) + F(2).$$

Since $a - 2 > -1$ for $1 < a < 2$, $(\log 2)(a-2)$ is greater than $-\log 2$. This gives the bounds

$$-\log(a-1) + F(2) - \log 2 \leq F(a) < -\log(a-1) + F(2).$$

Writing $a$ as $t$, we get

$$-\log(t-1) + F(2) - \log 2 \leq F(t) < -\log(t-1) + F(2),$$

so $F(t)$ is a bounded distance from $-\log(t-1)$ when $1 < t < 2$. In particular, $F(t) \to \infty$ as $t \to 1^+$.

## 10. A Trigonometric Integral

For positive numbers $a$ and $b$, the arithmetic-geometric mean inequality says $(a+b)/2 \geq \sqrt{ab}$ (with equality if and only if $a = b$). Let's iterate the two types of means: for $k \geq 0$, define $\{a_k\}$ and $\{b_k\}$ by $a_0 = a$, $b_0 = b$, and

$$a_k = \frac{a_{k-1} + b_{k-1}}{2}, \quad b_k = \sqrt{a_{k-1}b_{k-1}}$$

for $k \geq 1.

**Example 10.1.** If $a_0 = 1$ and $b_0 = 2$, then Table 2 gives $a_k$ and $b_k$ to 16 digits after the decimal point. Notice how rapidly they are getting close to each other!

| $k$ | $a_k$ | $b_k$ |
|-----|-------|-------|
| 0 | 1 | 2 |
| 1 | 1.5 | 1.4142135623730950 |
| 2 | 1.4571067811865475 | 1.4564753151219702 |
| 3 | 1.4567910481542588 | 1.4567910139395549 |
| 4 | 1.4567910310469069 | 1.4567910310469068 |

Table 1. Iteration of arithmetic and geometric means.

<!-- page 12 -->

Gauss showed that for all $a > 0$ and $b > 0$, the sequences $\{a_k\}$ and $\{b_k\}$ converge very rapidly to a common limit, which he called the *arithmetic-geometric mean* of $a$ and $b$ and wrote as $M(a,b)$. For example, $M(1,2) \approx 1.456791031046906$. Gauss discovered an integral formula for $1/M(a,b)$:

$$\frac{1}{M(a,b)} = \frac{2}{\pi}\int_0^{\pi/2}\frac{\mathrm{d}x}{\sqrt{a^2\cos^2 x + b^2\sin^2 x}}.$$

There is no elementary formula for this integral, but if we change the exponent $1/2$ in the square root to a positive integer $n$ then we can work out all the integrals

$$F_n(a,b) = \frac{2}{\pi}\int_0^{\pi/2}\frac{\mathrm{d}x}{(a^2\cos^2 x + b^2\sin^2 x)^n}$$

using repeated differentiation under the integral sign with respect to both $a$ and $b$. (This example, with a different normalization and no context for where the integral comes from, is Example 4 on the Wikipedia page for the Leibniz integral rule.)

For $n = 1$ we can do a direct integration:

$$F_1(a,b) = \frac{2}{\pi}\int_0^{\pi/2}\frac{\mathrm{d}x}{a^2\cos^2 x + b^2\sin^2 x}$$
$$= \frac{2}{\pi}\int_0^{\pi/2}\frac{\sec^2 x}{a^2 + b^2\tan^2 x}\,\mathrm{d}x$$
$$= \frac{2}{\pi}\int_0^\infty \frac{\mathrm{d}u}{a^2 + b^2 u^2} \quad \text{where } u = \tan x$$
$$= \frac{2}{\pi a^2}\int_0^\infty \frac{\mathrm{d}u}{1 + (b/a)^2 u^2}$$
$$= \frac{2}{\pi ab}\int_0^\infty \frac{\mathrm{d}v}{1 + v^2} \quad \text{where } v = (b/a)u$$
$$= \frac{1}{ab}.$$

Now let's differentiate $F_1(a,b)$ with respect to $a$ and with respect to $b$, both by its integral definition and by the formula we just computed for it:

$$\frac{\partial F_1}{\partial a} = \frac{2}{\pi}\int_0^{\pi/2}\frac{-2a\cos^2 x}{(a^2\cos^2 x + b^2\sin^2 x)^2}\,\mathrm{d}x, \quad \frac{\partial F_1}{\partial a} = -\frac{1}{a^2 b}$$

and

$$\frac{\partial F_1}{\partial b} = \frac{2}{\pi}\int_0^{\pi/2}\frac{-2b\sin^2 x}{(a^2\cos^2 x + b^2\sin^2 x)^2}\,\mathrm{d}x, \quad \frac{\partial F_1}{\partial b} = -\frac{1}{ab^2}.$$

Since $\sin^2 x + \cos^2 x = 1$, by a little algebra we can get a formula for $F_2(a,b)$:

$$F_2(a,b) = \frac{2}{\pi}\int_0^{\pi/2}\frac{\mathrm{d}x}{(a^2\cos^2 x + b^2\sin^2 x)^2}$$
$$= -\frac{1}{2a}\frac{\partial F_1}{\partial a} - \frac{1}{2b}\frac{\partial F_1}{\partial b}$$
$$= \frac{1}{2a^3 b} + \frac{1}{2ab^3}$$
$$= \frac{a^2 + b^2}{2a^3 b^3}.$$

<!-- page 13 -->

We can get a recursion expressing $F_n(a,b)$ in terms of $\partial F_{n-1}/\partial a$ and $\partial F_{n-1}/\partial b$ in general: for $n \geq 2$,

$$\frac{\partial F_{n-1}}{\partial a} = \frac{2}{\pi}\int_0^{\pi/2}\frac{-2(n-1)a\cos^2 x}{(a^2\cos^2 x + b^2\sin^2 x)^n}\,\mathrm{d}x, \quad \frac{\partial F_{n-1}}{\partial b} = \frac{2}{\pi}\int_0^{\pi/2}\frac{-2(n-1)b\sin^2 x}{(a^2\cos^2 x + b^2\sin^2 x)^n}\,\mathrm{d}x,$$

so

$$F_n(a,b) = -\frac{1}{2(n-1)a}\frac{\partial F_{n-1}}{\partial a} - \frac{1}{2(n-1)b}\frac{\partial F_{n-1}}{\partial b} = -\frac{1}{2(n-1)}\left(\frac{1}{a}\frac{\partial F_{n-1}}{\partial a} + \frac{1}{b}\frac{\partial F_{n-1}}{\partial b}\right).$$

A few sample calculations of $F_n(a,b)$ using this, starting from $F_1(a,b) = 1/(ab)$, are

$$F_2(a,b) = \frac{a^2+b^2}{2a^3 b^3}, \quad F_3(a,b) = \frac{3a^4+2a^2 b^2+3b^4}{6a^5 b^5}, \quad F_4(a,b) = \frac{5a^6+3a^4 b^2+3a^2 b^4+5b^6}{12a^7 b^7}.$$

## 11. Smoothly Dividing by $t$

Let $h\colon \mathbf{R} \to \mathbf{R}$ be smooth (that is, infinitely differentiable) such that $h(0) = 0$. The ratio $h(t)/t$ makes sense for $t \neq 0$, and it also can be given a reasonable meaning at $t = 0$: from the definition of the derivative, when $t \to 0$ we have

$$\frac{h(t)}{t} = \frac{h(t) - h(0)}{t - 0} \to h'(0).$$

Therefore the function

$$r(t) = \begin{cases} h(t)/t, & \text{if } t \neq 0, \\ h'(0), & \text{if } t = 0 \end{cases} \tag{11.1}$$

is continuous for all $t$. At $t \neq 0$, $r(t)$ is smooth by the definition of $r(t)$, the quotient rule, and induction. What about at $t = 0$?

**Theorem 11.1.** *When $h\colon \mathbf{R} \to \mathbf{R}$ is smooth and $h(0) = 0$, the function $r(t)$ in (11.1) is smooth at $t = 0$.*

**Remark 11.2.** This is easy to prove when $h(t)$ has a power series representation around $t = 0$, so the significance of the theorem is that it holds only assuming $h(t)$ is smooth, without being locally expressible by power series. An example of such a function is $h(t) = e^{-1/t^2}$ for $t \neq 0$ and $h(0) = 0$.

*Proof.* To analyze $r(t)$ near $t = 0$, we will find a different formula for it that avoids taking separate cases at $t \neq 0$ and $t = 0$ by writing $h(t)$ in a clever way with differentiation under the integral sign. Start from

$$h(t) = \int_0^t h'(u)\,\mathrm{d}u.$$

(This is correct since $h(0) = 0$.) For $t \neq 0$, introduce the change of variables $u = tx$, so $\mathrm{d}u = t\,\mathrm{d}x$. At the boundary, if $u = 0$ then $x = 0$. If $u = t$ then $x = 1$ (we can divide the equation $t = tx$ by $t$ because $t \neq 0$). Therefore

$$h(t) = \int_0^1 h'(tx)t\,\mathrm{d}x = t\int_0^1 h'(tx)\,\mathrm{d}x.$$

Dividing by $t$ when $t \neq 0$, we get

$$r(t) = \frac{h(t)}{t} = \int_0^1 h'(tx)\,\mathrm{d}x.$$

<!-- page 14 -->

The left and right sides don't have $t$ in the denominator. Are they equal at $t = 0$ too? The left side at $t = 0$ is $r(0) = h'(0)$. The right side is $\int_0^1 h'(0)\,\mathrm{d}x = h'(0)$ too, so

$$r(t) = \int_0^1 h'(tx)\,\mathrm{d}x \tag{11.2}$$

for all $t$, including $t = 0$. This is a formula for $h(t)/t$ where there is no longer a $t$ being divided!

Now we're set to use differentiation under the integral sign. The way we have set things up here, we want to differentiate with respect to $t$; the integration variable on the right is $x$. We can use differentiation under the integral sign on (11.2) when the integrand is differentiable. Since the integrand is infinitely differentiable, $r(t)$ is infinitely differentiable!

Explicitly,

$$r'(t) = \int_0^1 x h''(tx)\,\mathrm{d}x$$

and

$$r''(t) = \int_0^1 x^2 h'''(tx)\,\mathrm{d}x$$

and more generally

$$r^{(k)}(t) = \int_0^1 x^k h^{(k+1)}(tx)\,\mathrm{d}x$$

for all $k \geq 0$. In particular, $r^{(k)}(0) = \int_0^1 x^k h^{(k+1)}(0)\,\mathrm{d}x = h^{(k+1)}(0)/(k+1)$. $\square$

**Remark 11.3.** Whitney [15][^4] proved that every smooth *even* function $h\colon \mathbf{R} \to \mathbf{R}$ is a smooth function of $t^2$: $h(t) = g(t^2)$ where $g\colon \mathbf{R} \to \mathbf{R}$ is smooth. This is straightforward when $h$ is locally expressible by power series around 0 (an even power series at 0 has no odd powers of $t$, and thus is a power series in $t^2$), but without such an assumption it is more subtle.

## 12. Counterexamples and Justification

We have seen many examples where differentiation under the integral sign can be carried out with interesting results, but we have not actually stated conditions under which (1.2) is valid. Something does need to be checked. In [14], an incorrect use of differentiation under the integral sign due to Cauchy is discussed, where a divergent integral is evaluated as a finite expression. Here are two other examples where differentiation under the integral sign does not work.

**Example 12.1.** It is pointed out in [9, Example 6] that the formula

$$\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2},$$

which we discussed at the end of Section 3, leads to an erroneous instance of differentiation under the integral sign. Rewrite the formula as

$$\int_0^\infty \frac{\sin(ty)}{y}\,\mathrm{d}y = \frac{\pi}{2} \tag{12.1}$$

for $t > 0$ by the change of variables $x = ty$. Then differentiation under the integral sign implies

$$\int_0^\infty \cos(ty)\,\mathrm{d}y = 0,$$

but the left side doesn't make sense.

<!-- page 15 -->

The next example shows that even if both sides of (1.2) make sense, they need not be equal.

**Example 12.2.** For real numbers $x$ and $t$, let

$$f(x,t) = \begin{cases} \dfrac{xt^3}{(x^2+t^2)^2}, & \text{if } x \neq 0 \text{ or } t \neq 0, \\ 0, & \text{if } x = 0 \text{ and } t = 0. \end{cases}$$

Note $f(x,0) = 0$ for all $x$. Let

$$F(t) = \int_0^1 f(x,t)\,\mathrm{d}x.$$

When $t \neq 0$,

$$F(t) = \int_0^1 \frac{xt^3}{(x^2+t^2)^2}\,\mathrm{d}x$$
$$= \int_{t^2}^{1+t^2}\frac{t^3}{2u^2}\,\mathrm{d}u \quad (\text{where } u = x^2 + t^2)$$
$$= -\frac{t^3}{2u}\bigg|_{u=t^2}^{u=1+t^2}$$
$$= -\frac{t^3}{2(1+t^2)} + \frac{t^3}{2t^2}$$
$$= \frac{t}{2(1+t^2)}.$$

This is true when $t = 0$ too: $F(0) = \int_0^1 f(x,0)\,\mathrm{d}x = \int_0^1 0\,\mathrm{d}x = 0$, so $F(t) = t/(2(1+t^2))$ for all $t$. Therefore $F(t)$ is differentiable and

$$F'(t) = \frac{1-t^2}{2(1+t^2)^2}$$

for all $t$. In particular, $F'(0) = \frac{1}{2}$.

Now we compute $\frac{\partial}{\partial t}f(x,t)$ and then $\int_0^1 \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x$. Since $f(0,t) = 0$ for all $t$, $f(0,t)$ is differentiable in $t$ and $\frac{\partial}{\partial t}f(0,t) = 0$. For $x \neq 0$, $f(x,t)$ is differentiable in $t$ and

$$\frac{\partial}{\partial t}f(x,t) = \frac{(x^2+t^2)^2(3xt^2) - xt^3 \cdot 2(x^2+t^2)2t}{(x^2+t^2)^4}$$
$$= \frac{xt^2(x^2+t^2)(3(x^2+t^2) - 4t^2)}{(x^2+t^2)^4}$$
$$= \frac{xt^2(3x^2 - t^2)}{(x^2+t^2)^3}.$$

Combining both cases ($x = 0$ and $x \neq 0$),

$$\frac{\partial}{\partial t}f(x,t) = \begin{cases} \dfrac{xt^2(3x^2-t^2)}{(x^2+t^2)^3}, & \text{if } x \neq 0, \\ 0, & \text{if } x = 0. \end{cases} \tag{12.2}$$

In particular $\frac{\partial}{\partial t}\big|_{t=0}f(x,t) = 0$. Therefore at $t = 0$ the left side of the "formula"

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_0^1 f(x,t)\,\mathrm{d}x = \int_0^1 \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x$$

<!-- page 16 -->

is $F'(0) = 1/2$ and the right side is $\int_0^1 \frac{\partial}{\partial t}\big|_{t=0}f(x,t)\,\mathrm{d}x = 0$. The two sides are unequal!

The problem in this example is that $\frac{\partial}{\partial t}f(x,t)$ is not a continuous function of $(x,t)$. Indeed, the denominator in the formula in (12.2) is $(x^2+t^2)^3$, which has a problem near $(0,0)$. Specifically, while this derivative vanishes at $(0,0)$, if we let $(x,t) \to (0,0)$ along the line $x = t$, then on this line $\frac{\partial}{\partial t}f(x,t)$ has the value $1/(4x)$, which does not tend to 0 as $(x,t) \to (0,0)$.

**Theorem 12.3.** *The equation*

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_a^b f(x,t)\,\mathrm{d}x = \int_a^b \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x,$$

*where $a$ could be $-\infty$ and $b$ could be $\infty$, is valid at a real number $t = t_0$ in the sense that both sides exist and are equal, provided the following two conditions hold:*

- *$f(x,t)$ and $\frac{\partial}{\partial t}f(x,t)$ are continuous functions of two variables when $x$ is in the range of integration and $t$ is in some interval around $t_0$,*
- *for $t$ in some interval around $t_0$ there are upper bounds $|f(x,t)| \leq A(x)$ and $|\frac{\partial}{\partial t}f(x,t)| \leq B(x)$, both bounds being independent of $t$, such that $\int_a^b A(x)\,\mathrm{d}x$ and $\int_a^b B(x)\,\mathrm{d}x$ exist.*

*Proof.* See [10, pp. 337--339], which uses the definition of the derivative and the Mean Value Theorem. If the interval of integration is infinite, $\int_a^b A(x)\,\mathrm{d}x$ and $\int_a^b B(x)\,\mathrm{d}x$ are improper. A second proof [10, p. 340] obtains the theorem from the Fundamental Theorem of Calculus and swapping the order of a double integral.[^5] $\square$

In Table 2 we include choices for $A(x)$ and $B(x)$ for the functions we have treated. Since the calculation of a derivative at a point only depends on an interval around the point, we have replaced a $t$-range such as $t > 0$ with $t \geq c > 0$ in some cases to obtain choices for $A(x)$ and $B(x)$.

| Section | $f(x,t)$ | $x$ range | $t$ range | $t$ we want | $A(x)$ | $B(x)$ |
|---------|----------|-----------|-----------|-------------|--------|--------|
| 2 | $x^n e^{-tx}$ | $[0,\infty)$ | $t \geq c > 0$ | 1 | $x^n e^{-cx}$ | $x^{n+1}e^{-cx}$ |
| 3 | $e^{-tx}\frac{\sin x}{x}$ | $(0,\infty)$ | $t \geq c > 0$ | 0 | $e^{-cx}$ | $e^{-cx}$ |
| 4 | $\frac{1}{1+x^2}e^{-t^2(1+x^2)/2}$ | $[0,\infty)$ | $t \geq c > 0$ | all $t \geq 0$ | $\frac{1}{1+x^2}$ | $\frac{1}{\sqrt{e}}e^{-c^2 x^2/2}$ |
| 5 | $x^n e^{-tx^2}$ | $\mathbf{R}$ | $t \geq c > 0$ | 1 | $x^n e^{-cx^2}$ | $x^{n+2}e^{-cx^2}$ |
| 6 | $\cos(tx)e^{-x^2/2}$ | $[0,\infty)$ | $\mathbf{R}$ | all $t$ | $e^{-x^2/2}$ | $|x|e^{-x^2/2}$ |
| 7 | $x^{t-1}e^{-x}$ | $(0,\infty)$ | $0 < t \leq c$ | $1/2, 1, 3/2, 2$ | $x^{c-1}e^{-x}$ | $x^{c-1}|\log x|e^{-x}$ |
| 8 | $\frac{x^t - 1}{\log x}$ | $(0,1]$ | $0 < t < c$ | 1 | $\frac{1-x^c}{\log x}$ | 1 |
| 9 | $\frac{1}{x^t\log x}$ | $[2,\infty)$ | $t \geq c > 1$ | $t > 1$ | $\frac{1}{x^2\log x}$ | $\frac{1}{x^c}$ |
| 11 | $x^k h^{(k+1)}(tx)$ | $[0,1]$ | $|t| < c$ | 0 | $\max_{|y|\leq c}|h^{(k+1)}(y)|$ | $\max_{|y|\leq c}|h^{(k+2)}(y)|$ |

Table 2. Summary

We did not put the function from Section 10 in the table since it would make the width too long and it depends on two parameters. Putting the parameter into the coefficient of $\cos^2 x$ in Section 10, we can take $f(x,t) = 1/(t^2\cos^2 x + b^2\sin^2 x)^n$ for $x \in [0,\pi/2]$, $0 < c \leq t \leq c'$ (that is, keep $t$ bounded away from 0 and $\infty$), $A(x) = 1/(c^2\cos^2 x + b^2\sin^2 x)^n$ and $B(x) = 2c'n/(c^2\cos^2 x + b^2\sin^2 x)^{n+1}$.

<!-- page 17 -->

**Corollary 12.4.** *If $a(t)$ and $b(t)$ are both differentiable on an open interval $(c_1, c_2)$, then*

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_{a(t)}^{b(t)} f(x,t)\,\mathrm{d}x = \int_{a(t)}^{b(t)} \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x + f(b(t),t)b'(t) - f(a(t),t)a'(t)$$

*for $(x,t) \in [\alpha,\beta] \times (c_1,c_2)$, where $\alpha < \beta$ and the following conditions are satisfied:*

- *$f(x,t)$ and $\frac{\partial}{\partial t}f(x,t)$ are continuous on $[\alpha,\beta] \times (c_1,c_2)$,*
- *for all $t \in (c_1,c_2)$, $a(t) \in [\alpha,\beta]$ and $b(t) \in [\alpha,\beta]$,*
- *for $(x,t) \in [\alpha,\beta] \times (c_1,c_2)$, there are upper bounds $|f(x,t)| \leq A(x)$ and $|\frac{\partial}{\partial t}f(x,t)| \leq B(x)$ such that $\int_\alpha^\beta A(x)\,\mathrm{d}x$ and $\int_\alpha^\beta B(x)\,\mathrm{d}x$ exist.*

*Proof.* This is a consequence of Theorem 12.3 and the chain rule for multivariable functions. Set a function of three variables

$$I(t,a,b) = \int_a^b f(x,t)\,\mathrm{d}x$$

for $(t,a,b) \in (c_1,c_2) \times [\alpha,\beta] \times [\alpha,\beta]$. (Here $a$ and $b$ are not functions of $t$, but variables.) Then

$$\frac{\partial I}{\partial t}(t,a,b) = \int_a^b \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x, \quad \frac{\partial I}{\partial a}(t,a,b) = -f(a,t), \quad \frac{\partial I}{\partial b}(t,a,b) = f(b,t), \tag{12.3}$$

where the first formula follows from Theorem 12.3 (its hypotheses are satisfied for each $a$ and $b$ in $[\alpha,\beta]$) and the second and third formulas are the Fundamental Theorem of Calculus. For differentiable functions $a(t)$ and $b(t)$ with values in $[\alpha,\beta]$ for $c_1 < t < c_2$, by the chain rule

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_{a(t)}^{b(t)} f(x,t)\,\mathrm{d}x = \frac{\mathrm{d}}{\mathrm{d}t}I(t,a(t),b(t))$$
$$= \frac{\partial I}{\partial t}(t,a(t),b(t))\frac{\mathrm{d}t}{\mathrm{d}t} + \frac{\partial I}{\partial a}(t,a(t),b(t))\frac{\mathrm{d}a}{\mathrm{d}t} + \frac{\partial I}{\partial b}(t,a(t),b(t))\frac{\mathrm{d}b}{\mathrm{d}t}$$
$$= \int_{a(t)}^{b(t)}\frac{\partial f}{\partial t}(x,t)\,\mathrm{d}x - f(a(t),t)a'(t) + f(b(t),t)b'(t) \text{ by (12.3)}. \quad \square$$

A version of differentiation under the integral sign for $t$ a complex variable is in [11, pp. 392--393].

**Example 12.5.** For a parametric integral $\int_a^t f(x,t)\,\mathrm{d}x$ with $a$ fixed, Corollary 12.4 tells us

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_a^t f(x,t)\,\mathrm{d}x = \int_a^t \frac{\partial}{\partial t}f(x,t)\,\mathrm{d}x + f(t,t) \tag{12.4}$$

for $(x,t) \in [\alpha,\beta] \times (c_1,c_2)$ provided that (i) $f$ and $\partial f/\partial t$ are continuous for $(x,t) \in [\alpha,\beta] \times (c_1,c_2)$, (ii) $\alpha \leq a \leq \beta$ and $(c_1,c_2) \subset [\alpha,\beta]$, and (iii) there are bounds $|f(x,t)| \leq A(x)$ and $|\frac{\partial}{\partial t}f(x,t)| \leq B(x)$ for $(x,t) \in [\alpha,\beta] \times (c_1,c_2)$ such that the integrals $\int_\alpha^\beta A(x)\,\mathrm{d}x$ and $\int_\alpha^\beta B(x)\,\mathrm{d}x$ both exist.

We will apply (12.4) to the integral

$$F(t) = \int_0^t \frac{\log(1+tx)}{1+x^2}\,\mathrm{d}x$$

for $t \geq 0$. Obviously $F(0) = 0$. Here $f(x,t) = \log(1+tx)/(1+x^2)$ and $\frac{\partial}{\partial t}f(x,t) = \frac{x}{(1+tx)(1+x^2)}$. To include $t = 0$ in the setting of Corollary 12.4, the open $t$-interval should include 0. Therefore we're going to consider $F(t)$ for small negative $t$ too.

Use $(x,t) \in [-\delta, 1/(2\varepsilon)] \times (-\varepsilon, 1/(2\delta))$ for small $\varepsilon$ and $\delta$ (between 0 and $1/2$). In the notation of Corollary 12.4, $\alpha = -\delta$, $\beta = 1/(2\varepsilon)$, $c_1 = -\varepsilon$, and $c_2 = 1/(2\delta)$. To have $(c_1,c_2) \subset [\alpha,\beta]$ is equivalent to requiring $\varepsilon < \delta$ (e.g., $\varepsilon = \delta/2$). We chose the bounds on $x$ and $t$ to keep $1 + xt$

<!-- page 18 -->

away from 0: $-1/2 < xt < 1/(4\varepsilon\delta)$, so $1/2 < 1 + xt < 1 + 1/(4\varepsilon\delta)$.[^6] That makes $|\log(1+xt)|$ bounded above and $1+xt$ bounded below, so $|f|$ and $|\partial f/\partial t|$ are both bounded above by constants (depending on $\varepsilon$ and $\delta$), so (12.4) is justified with $A(x)$ and $B(x)$ being constant functions for $x \in [\alpha,\beta]$. Thus when $0 < \varepsilon < \delta < 1$ and $-\varepsilon < t < 1/(2\delta)$,

$$F'(t) = \int_0^t \frac{x}{(1+tx)(1+x^2)}\,\mathrm{d}x + \frac{\log(1+t^2)}{1+t^2}$$
$$= \int_0^t \frac{1}{1+t^2}\left(\frac{-t}{1+tx} + \frac{t}{1+x^2} + \frac{x}{1+x^2}\right)\mathrm{d}x + \frac{\log(1+t^2)}{1+t^2}.$$

After antidifferentiating the three terms in the integral with respect to $x$,

$$F'(t) = \left(\frac{-1}{1+t^2}\log(1+tx) + \frac{t}{1+t^2}\arctan(x) + \frac{\log(1+x^2)}{2(1+t^2)}\right)\bigg|_0^t + \frac{\log(1+t^2)}{1+t^2}$$
$$= \frac{-\log(1+t^2)}{1+t^2} + \frac{t\arctan(t)}{1+t^2} + \frac{\log(1+t^2)}{2(1+t^2)} + \frac{\log(1+t^2)}{1+t^2}$$
$$= \frac{t\arctan(t)}{1+t^2} + \frac{\log(1+t^2)}{2(1+t^2)}. \tag{12.5}$$

Letting $\delta \to 0^+$ shows (12.5) holds for all $t \geq 0$. By the Fundamental Theorem of Calculus

$$F(t) = F(t) - F(0) = \int_0^t F'(y)\,\mathrm{d}y = \int_0^t \left(\frac{y\arctan(y)}{1+y^2} + \frac{\log(1+y^2)}{2(1+y^2)}\right)\mathrm{d}y.$$

Using integration by parts on the first integrand with $u = \arctan(y)$ and $\mathrm{d}v = \frac{y}{1+y^2}\,\mathrm{d}y$,

$$F(t) = \left.uv\right|_0^t - \int_0^t v\,\mathrm{d}u + \int_0^t \frac{\log(1+y^2)}{2(1+y^2)}\,\mathrm{d}y$$
$$= \left.\arctan(y)\frac{\log(1+y^2)}{2}\right|_0^t - \int_0^t \frac{\log(1+y^2)}{2(1+y^2)}\,\mathrm{d}y + \int_0^t \frac{\log(1+y^2)}{2(1+y^2)}\,\mathrm{d}y$$
$$= \frac{1}{2}\arctan(t)\log(1+t^2),$$

so

$$\int_0^t \frac{\log(1+tx)}{1+x^2}\,\mathrm{d}x = \frac{1}{2}\arctan(t)\log(1+t^2). \tag{12.6}$$

for $t \geq 0$. Both sides are odd functions of $t$, so (12.6) holds for all $t$. Setting $t = 1$,

$$\int_0^1 \frac{\log(1+x)}{1+x^2}\,\mathrm{d}x = \frac{1}{2}\arctan(1)\log 2 = \frac{\pi\log 2}{8}. \tag{12.7}$$

The equation (12.7) is derived in another way in Exercise 16.

## 13. The Fundamental Theorem of Algebra

By differentiating under the integral sign we will prove the fundamental theorem of algebra: each nonconstant polynomial $p(z)$ with coefficients in $\mathbf{C}$ has a root in $\mathbf{C}$. The proof is by Schep [13].

<!-- page 19 -->

Arguing by contradiction, assume $p(z) \neq 0$ for all $z \in \mathbf{C}$. For $r \geq 0$, consider the following integral around a circle of radius $r$ centered at the origin:

$$I(r) = \int_0^{2\pi}\frac{\mathrm{d}\theta}{p(re^{i\theta})}.$$

This integral makes sense since the denominator is never 0, so $1/p(z)$ is continuous on $\mathbf{C}$. Let $f(\theta,r) = 1/p(re^{i\theta})$, so $I(r) = \int_0^{2\pi} f(\theta,r)\,\mathrm{d}\theta$.

We will prove three properties of $I(r)$:

1. Theorem 12.3 can be applied to $I(r)$ for $r > 0$,
2. $I(r) \to 0$ as $r \to \infty$,
3. $I(r) \to I(0)$ as $r \to 0^+$ (continuity at $r = 0$).

Taking these for granted, let's see how a contradiction occurs. For $r > 0$,

$$I'(r) = \int_0^{2\pi}\frac{\partial}{\partial r}f(\theta,r)\,\mathrm{d}\theta = \int_0^{2\pi}\frac{-p'(re^{i\theta})e^{i\theta}}{p(re^{i\theta})^2}\,\mathrm{d}\theta.$$

Since

$$\frac{\partial}{\partial\theta}f(\theta,r) = \frac{-p'(re^{i\theta})}{p(re^{i\theta})^2}ire^{i\theta} = ir\frac{\partial}{\partial r}f(\theta,r),$$

for $r > 0$ we have

$$I'(r) = \int_0^{2\pi}\frac{\partial}{\partial r}f(\theta,r)\,\mathrm{d}\theta = \int_0^{2\pi}\frac{1}{ir}\frac{\partial}{\partial\theta}f(\theta,r)\,\mathrm{d}\theta = \frac{1}{ir}f(\theta,r)\bigg|_{\theta=0}^{\theta=2\pi} = \frac{1}{ir}\left(\frac{1}{p(r)} - \frac{1}{p(r)}\right) = 0.$$

Thus $I(r)$ is *constant* for $r > 0$. Since $I(r) \to 0$ as $r \to \infty$, the constant is zero: $I(r) = 0$ for $r > 0$. Since $I(r) \to I(0)$ as $r \to 0^+$ we get $I(0) = 0$, which is false since $I(0) = 2\pi/p(0) \neq 0$.

It remains to prove the three properties of $I(r)$.

(1) **Theorem 12.3 can be applied to $I(r)$ for $r > 0$:** Since $p(z)$ and $p'(z)$ are both continuous on $\mathbf{C}$, the functions $f(\theta,r)$ and $(\partial/\partial r)f(\theta,r)$ are continuous for $\theta \in [0,2\pi]$ and all $r \geq 0$. This confirms the first condition in Theorem 12.3.

For each $r_0 > 0$ the set $\{(\theta,r) : \theta \in [0,2\pi], r \in [0,2r_0]\}$ is closed and bounded, so the functions $f(\theta,r)$ and $(\partial/\partial r)f(\theta,r)$ are both bounded above by a constant (independent of $r$ and $\theta$) on this set. The range of integration $[0,2\pi]$ is finite, so the second condition in Theorem 12.3 is satisfied using constants for $A(\theta)$ and $B(\theta)$.

(2) **$I(r) \to 0$ as $r \to \infty$:** Let $p(z)$ have leading term $cz^d$, with $d = \deg p(z) \geq 1$. As $r \to \infty$, $|p(re^{i\theta})|/|re^{i\theta}|^d \to |c| > 0$, so for all large $r$ we have $|p(re^{i\theta})| \geq |c|r^d/2$. For such large $r$,

$$|I(r)| \leq \int_0^{2\pi}\frac{\mathrm{d}\theta}{|p(re^{i\theta})|} \leq \int_0^{2\pi}\frac{\mathrm{d}\theta}{|c|r^d/2} = \frac{4\pi}{|c|r^d},$$

and the upper bound tends to 0 as $r \to \infty$ since $d > 0$, so $I(r) \to 0$ as $r \to \infty$.

(3) **$I(r) \to I(0)$ as $r \to 0^+$:** For $r > 0$,

$$I(r) - I(0) = \int_0^{2\pi}\left(\frac{1}{p(re^{i\theta})} - \frac{1}{p(0)}\right)\mathrm{d}\theta \implies |I(r) - I(0)| \leq \int_0^{2\pi}\left|\frac{1}{p(re^{i\theta})} - \frac{1}{p(0)}\right|\mathrm{d}\theta. \tag{13.1}$$

Since $1/p(z)$ is continuous at 0, for $\varepsilon > 0$ there is $\delta > 0$ such that $|z| < \delta \implies |1/p(z) - 1/p(0)| < \varepsilon$. Therefore if $0 < r < \delta$, (13.1) implies $|I(r) - I(0)| \leq \int_0^{2\pi}\varepsilon\,\mathrm{d}\theta = 2\pi\varepsilon$. Let $\varepsilon \to 0^+$ and we're done.

<!-- page 20 -->

## 14. An Example Needing a Change of Variables

Our next example is taken from [1, pp. 78, 84--86]. For all $t \in \mathbf{R}$, we will show by differentiation under the integral sign that

$$\int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = \pi e^{-|t|}. \tag{14.1}$$

For example,

$$\int_{\mathbf{R}}\frac{\cos x}{1+x^2}\,\mathrm{d}x = \frac{\pi}{e}, \quad \int_{\mathbf{R}}\frac{\cos(2x)}{1+x^2}\,\mathrm{d}x = \frac{\pi}{e^2}, \quad \int_{\mathbf{R}}\frac{\cos x}{4+x^2}\,\mathrm{d}x = \frac{1}{2}\int_{\mathbf{R}}\frac{\cos(2x)}{1+x^2}\,\mathrm{d}x = \frac{\pi}{2e^2}.$$

In (14.1), set $f(x,t) = \cos(tx)/(1+x^2)$. Since $f(x,t)$ is continuous and $|f(x,t)| \leq 1/(1+x^2)$, the integral in (14.1) exists for all $t$. A graph of $\pi e^{-|t|}$ is in Figure 1. Note $\pi e^{-|t|}$ is *not* differentiable at 0, so we shouldn't expect to prove (14.1) at $t = 0$ by differentiation under the integral sign.

<!-- Figure 1. Graph of y = \pi e^{-|t|}. -->

We'll verify (14.1) at $t = 0$ using elementary calculus:

$$\int_{\mathbf{R}}\frac{\mathrm{d}x}{1+x^2} = \left.\arctan x\right|_{-\infty}^\infty = \frac{\pi}{2} - \frac{-\pi}{2} = \pi. \tag{14.2}$$

Since the integral in (14.1) is an even function of $t$, to compute the integral for $t \neq 0$ it suffices to treat the case $t > 0$.[^7]

Set

$$F(t) = \int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x.$$

If we try to compute $F'(t)$ for $t > 0$ using differentiation under the integral sign, we get

$$F'(t) \stackrel{?}{=} \int_{\mathbf{R}}\frac{\partial}{\partial t}\left(\frac{\cos(tx)}{1+x^2}\right)\mathrm{d}x = -\int_{\mathbf{R}}\frac{x\sin(tx)}{1+x^2}\,\mathrm{d}x. \tag{14.3}$$

No upper bound $|\frac{\partial}{\partial t}f(x,t)| \leq B(x)$ for $t > 0$ in Theorem 12.3 justifies differentiating $F(t)$ under the integral sign or that even implies $F(t)$ is differentiable for $t > 0$. Indeed, for $x$ near a large odd multiple of $(\pi/2)/t$, the integrand in (14.3) is approximately $x/(1+x^2) \approx 1/x$, which is not integrable for large $x$. That does not mean (14.3) is false, but if we did not see (14.1) already then we might think $F(t)$ is differentiable for all $t$ even though $F(t)$ is *not* differentiable at $t = 0$.

<!-- page 21 -->

Even though we raised suspicions about (14.3), let's use it without focusing on rigor for now:

$$F'(t) = -\int_{\mathbf{R}}\frac{x\sin(tx)}{1+x^2}\,\mathrm{d}x \tag{14.4}$$
$$= -\int_{\mathbf{R}}\frac{x^2\sin(tx)}{x(1+x^2)}\,\mathrm{d}x$$
$$= -\int_{\mathbf{R}}\frac{(1+x^2-1)\sin(tx)}{x(1+x^2)}\,\mathrm{d}x$$
$$= -\int_{\mathbf{R}}\frac{\sin(tx)}{x}\,\mathrm{d}x + \int_{\mathbf{R}}\frac{\sin(tx)}{x(1+x^2)}\,\mathrm{d}x.$$

Making the change of variables $u = tx$ in the first integral, since $t > 0$ we get

$$F'(t) = -\int_{\mathbf{R}}\frac{\sin(u)}{u}\,\mathrm{d}u + \int_{\mathbf{R}}\frac{\sin(tx)}{x(1+x^2)}\,\mathrm{d}x. \tag{14.5}$$

The first integral is a constant (it's $\pi$ by (A.2), but that's irrelevant), and it goes away if we differentiate both sides with respect to $t$ and once more use differentiation under the integral sign without justifying that:

$$F''(t) = \int_{\mathbf{R}}\frac{x\cos(tx)}{x(1+x^2)}\,\mathrm{d}x = \int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = F(t).$$

Each solution of $F''(t) = F(t)$ on $\mathbf{R}$ has the form $ae^t + be^{-t}$. Since $F(0) = \pi$ by (14.2), $a + b = \pi$. (This hides errors: the ODE for $F(t)$ was never shown at $t = 0$, and (14.4) and (14.5) are inconsistent about the value of $F'(0)$, with the first saying $F'(0) = 0$ and the second saying $F'(0) \neq 0$.) Thus

$$F(t) := \int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = ae^t + (\pi-a)e^{-t} = a(e^t - e^{-t}) + \pi e^{-t}. \tag{14.6}$$

To determine $a$, let $t \to \infty$ in (14.6). The integral there tends to 0 by the Riemann--Lebesgue lemma from Fourier analysis, but we can also explain it directly with integration by parts: letting $u = 1/(1+x^2)$ and $\mathrm{d}v = \cos(tx)\,\mathrm{d}x$, so $\mathrm{d}u = -2x/(1+x^2)^2\,\mathrm{d}x$ and $v = \sin(tx)/t$,

$$F(t) = \int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = \left.\frac{\sin(tx)}{t(1+x^2)}\right|_{x=-\infty}^{x=\infty} + \frac{2}{t}\int_{\mathbf{R}}\frac{x\sin(tx)}{(1+x^2)^2}\,\mathrm{d}x = \frac{2}{t}\int_{\mathbf{R}}\frac{x\sin(tx)}{(1+x^2)^2}\,\mathrm{d}x.$$

Since $|\sin(tx)| \leq 1$, $|F(t)| \leq C/t$ for a constant $C$ that's independent of $t$, so $F(t) \to 0$ as $t \to \infty$. Thus $a(e^t + e^{-t}) + \pi e^{-t} \to 0$ as $t \to \infty$. This implies $a = 0$, so $F(t) = \pi e^{-t}$ for $t > 0$, as in (14.1).[^8]

That derivation of (14.1) when $t > 0$ had several invalid steps. To derive it rigorously, we make a *change of variables*. Fixing $t > 0$, set $y = tx$, so $\mathrm{d}y = t\,\mathrm{d}x$ and

$$F(t) = \int_{\mathbf{R}}\frac{\cos y}{1+y^2/t^2}\frac{\mathrm{d}y}{t} = \int_{\mathbf{R}}\frac{t\cos y}{t^2+y^2}\,\mathrm{d}y. \tag{14.7}$$

This new second integral for $F(t)$ when $t > 0$ will be accessible to justifying differentiation under the integral sign. (Although the new integral in (14.7) is an odd function of $t$ while $F(t)$ is an even function of $t$, there is no contradiction since the new integral for $F(t)$ was derived *only* for $t > 0$.)

Fix $c' > c > 0$. For $t \in (c,c')$, the integrand in

$$\int_{\mathbf{R}}\frac{t\cos y}{t^2+y^2}\,\mathrm{d}y$$

<!-- page 22 -->

is bounded above in absolute value by $t/(t^2+y^2) \leq c'/(c^2+y^2)$, which is independent of $t$ and integrable over $\mathbf{R}$. The $t$-partial derivative of the integrand is $(y^2-t^2)(\cos y)/(t^2+y^2)^2$, which is bounded above in absolute value by $(y^2+t^2)/(t^2+y^2)^2 = 1/(t^2+y^2) \leq 1/(c^2+y^2)$, which is independent of $t$ and integrable over $\mathbf{R}$. This justifies the use of differentiation under the integral sign by Theorem 12.3: for $c < t < c'$, and hence for all $t > 0$ since we never specified $c$ or $c'$,

$$F'(t) = \int_{\mathbf{R}}\frac{\partial}{\partial t}\left(\frac{t\cos y}{t^2+y^2}\right)\mathrm{d}y = \int_{\mathbf{R}}\frac{y^2-t^2}{(t^2+y^2)^2}\cos y\,\mathrm{d}y.$$

Next we'll compute $F''(t)$ by differentiation under the integral sign on $F'(t)$. For $0 < c < t < c'$, check the $t$-partial derivative of the integrand is bounded above in absolute value by a function of $y$ that is independent of $t$ and is integrable over $\mathbf{R}$ (exercise), so by Theorem 12.3, for $t > 0$

$$F''(t) = \int_{\mathbf{R}}\frac{\partial^2}{\partial t^2}\left(\frac{t\cos y}{t^2+y^2}\right)\mathrm{d}y = \int_{\mathbf{R}}\frac{\partial^2}{\partial t^2}\left(\frac{t}{t^2+y^2}\right)\cos y\,\mathrm{d}y.$$

Check that $(\partial^2/\partial t^2)(t/(t^2+y^2)) = -(\partial^2/\partial y^2)(t/(t^2+y^2))$, so

$$F''(t) = -\int_{\mathbf{R}}\frac{\partial^2}{\partial y^2}\left(\frac{t}{t^2+y^2}\right)\cos y\,\mathrm{d}y.$$

Using integration by parts on this formula for $F''(t)$ *twice* (starting with $u = -\cos y$ and $\mathrm{d}v = (\partial^2/\partial y^2)(t/(t^2+y^2))$), we obtain for $t > 0$

$$F''(t) = -\int_{\mathbf{R}}\frac{\partial}{\partial y}\left(\frac{t}{t^2+y^2}\right)\sin y\,\mathrm{d}y = \int_{\mathbf{R}}\left(\frac{t}{t^2+y^2}\right)\cos y\,\mathrm{d}y = F(t).$$

The equation $F''(t) = F(t)$ for $t > 0$ is what we found by the nonrigorous method earlier.

How can we show $F(t) = ae^t + be^{-t}$ for $t > 0$ (not $t \in \mathbf{R}$)? One way is by a strong enough existence/uniqueness theorem for linear ODEs. To see another way, set $G(t) = F(t) + F'(t)$ for $t > 0$, so

$$G'(t) = F'(t) + F''(t) = F'(t) + F(t) = G(t).$$

Then $(G(t)/e^t)' = (e^t G'(t) - G(t)e^t)/e^{2t} = 0$, so $G(t)/e^t = c$ for $t > 0$, where $c$ is a constant. That makes $F(t) + F'(t) = ce^t$, so $F'(t) = -F(t) + ce^t$. Set $H(t) = F(t) - (c/2)e^t$ when $t > 0$. Then

$$H'(t) = F'(t) - \frac{c}{2}e^t = -\left(F(t) - \frac{c}{2}e^t\right)' = -H(t),$$

so $(H(t)/e^{-t})' = (e^{-t}H'(t) + H(t)e^{-t})/e^{-2t} = 0$. Thus $H(t)/e^{-t} = b$ for $t > 0$, where $b$ is a constant, so

$$F(t) = \frac{c}{2}e^t + H(t) = \frac{c}{2}e^t + be^{-t}$$

for $t > 0$. Setting $a = c/2$, there are constants $a$ and $b$ such that

$$F(t) := \int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = ae^t + be^{-t} \tag{14.8}$$

for $t > 0$. To determine $a$ and $b$, we look at (14.8) as $t \to 0^+$ and as $t \to \infty$.

As $t \to 0^+$, the integrand in (14.8) tends pointwise to $1/(1+x^2)$, so we expect $F(t)$ to tend to $F(0) = \int_{\mathbf{R}}\mathrm{d}x/(1+x^2) = \pi$ (see (14.2)) as $t \to 0^+$. To justify this, we will bound

$$|F(t) - F(0)| = \left|\int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x - \int_{\mathbf{R}}\frac{\mathrm{d}x}{1+x^2}\right| \leq \int_{\mathbf{R}}\frac{|\cos(tx)-1|}{1+x^2}\,\mathrm{d}x.$$

<!-- page 23 -->

For $N > 0$, break up the integral over $\mathbf{R}$ into the regions $|x| \leq N$ and $|x| \geq N$. We have

$$\int_{\mathbf{R}}\frac{|\cos(tx)-1|}{1+x^2}\,\mathrm{d}x \leq \int_{|x|\leq N}\frac{|\cos(tx)-1|}{1+x^2}\,\mathrm{d}x + \int_{|x|\geq N}\frac{2}{1+x^2}\,\mathrm{d}x$$
$$\leq \int_{|x|\leq N}\frac{t|x|}{1+x^2}\,\mathrm{d}x + \int_{|x|\geq N}\frac{2}{1+x^2}\,\mathrm{d}x$$
$$= t\int_{|x|\leq N}\frac{|x|}{1+x^2}\,\mathrm{d}x + 4\left(\frac{\pi}{2} - \arctan N\right).$$

We can make $\pi/2 - \arctan N$ as small as we wish by taking $N$ sufficiently large, and for such an $N$, we can make the first term as small as we wish by taking $t$ sufficiently small. Thus $F(t) \to F(0)$ as $t \to 0^+$. Returning to (14.8), letting $t \to 0^+$ we obtain $\pi = a + b$, so for all $t > 0$,

$$\int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = ae^t + (\pi-a)e^{-t} = a(e^t - e^{-t}) + \pi e^{-t}. \tag{14.9}$$

Letting $t \to \infty$ in (14.9), the left side tends to 0 by the estimate $|F(t)| \leq C/t$ derived (correctly) in the paragraph right after (14.6), so $a = 0$. Thus $F(t) = \pi e^{-t}$ for $t > 0$.

**Remark 14.1.** Now that we know $F(t) = \pi e^{-t}$ for $t > 0$, so $F'(t) = -\pi e^{-t}$, the formal differentiation under the integral sign that led to (14.3) suggests that

$$\int_{\mathbf{R}}\frac{x\sin(tx)}{1+x^2}\,\mathrm{d}x = \pi e^{-t} \quad \text{for } t > 0.$$

This integral is subtle: it is not absolutely convergent. The formula above can be justified by the residue theorem in complex analysis (defining $\int_{\mathbf{R}}$ as $\lim_{R\to\infty}\int_{-R}^R$). That formula is *not* true at $t = 0$: the integral at $t = 0$ is 0, but $\pi e^{-t}$ at $t = 0$ is $\pi$. The integral is discontinuous at $t = 0$.[^9]

## 15. Fourier Transform of a Gaussian

For a continuous function $f\colon \mathbf{R} \to \mathbf{C}$ that is rapidly decreasing at $\pm\infty$, its Fourier transform is the function $\mathcal{F}f\colon \mathbf{R} \to \mathbf{C}$ defined by

$$(\mathcal{F}f)(y) = \int_{-\infty}^\infty f(x)e^{-ixy}\,\mathrm{d}x = \int_{-\infty}^\infty f(x)(\cos(xy) - i\sin(xy))\,\mathrm{d}x. \tag{15.1}$$

For example, $(\mathcal{F}f)(0) = \int_{-\infty}^\infty f(x)\,\mathrm{d}x$. This integral transform shows up all over the place in pure and applied analysis. We will use differentiation under the integral sign to compute the Fourier transform of Gaussian functions $e^{-ax^2/2}$ where $a > 0$, first for $a = 1$ and then for all $a > 0$.

When $f(x) = e^{-x^2/2}$, differentiate both sides of the equation

$$(\mathcal{F}f)(y) = \int_{-\infty}^\infty e^{-x^2/2}e^{-ixy}\,\mathrm{d}x$$

with respect to $y$, using differentiation under the integral sign for the right side:

$$(\mathcal{F}f)'(y) = \int_{-\infty}^\infty -ix e^{-x^2/2}e^{-ixy}\,\mathrm{d}x = -i\int_{-\infty}^\infty x e^{-x^2/2}e^{-ixy}\,\mathrm{d}x. \tag{15.2}$$

Differentiation under the integral sign here can be justified by applying Theorem 12.3 to the real and imaginary parts of $(\mathcal{F}f)(y)$: let $f(x,y)$ be $e^{-x^2/2}\cos(xy)$ or $-e^{-x^2/2}\sin(xy)$, $A(x) = e^{-x^2/2}$, and $B(x) = |x|e^{-x^2/2}$ since $|\cos(xy)| \leq 1$ and $|\sin(xy)| \leq 1$ for all real numbers $x$ and $y$.

<!-- page 24 -->

Apply integration by parts (for complex-valued functions) to the last integral in (15.2) using $u = e^{-ixy}$ and $\mathrm{d}v = xe^{-x^2/2}\,\mathrm{d}x$, with $\mathrm{d}u = -iye^{-ixy}\,\mathrm{d}x$ and $v = -e^{-x^2/2}$:

$$\int_{-\infty}^\infty x e^{-x^2/2}e^{-ixy}\,\mathrm{d}x = \int_{-\infty}^\infty u\,\mathrm{d}v$$
$$= \left.uv\right|_{x=-\infty}^{x=\infty} - \int_{-\infty}^\infty v\,\mathrm{d}u$$
$$= \left.-\frac{e^{-ixy}}{e^{x^2/2}}v\right|_{x=-\infty}^{x=\infty} - iy\int_{-\infty}^\infty e^{-x^2/2}e^{-ixy}\,\mathrm{d}x$$
$$= -iy(\mathcal{F}f)(y).$$

Thus (15.2) becomes

$$(\mathcal{F}f)'(y) = -i(-iy)(\mathcal{F}f)(y) = -y(\mathcal{F}f)(y).$$

The solutions to the differential equation $g'(y) = -yg(y)$ are $g(y) = Ce^{-y^2/2}$ for constant $C$, so

$$f(x) = e^{-x^2/2} \implies (\mathcal{F}f)(y) = Ce^{-y^2/2}$$

for some $C$. To determine $C$, set $y = 0$ on both sides: $\int_{-\infty}^\infty e^{-x^2/2}\,\mathrm{d}x = C$. That integral is $\sqrt{2\pi}$ by Section 4 (another use of differentiation under the integral sign), so

$$f(x) = e^{-x^2/2} \implies (\mathcal{F}f)(y) = \sqrt{2\pi}e^{-y^2/2}. \tag{15.3}$$

For $a > 0$, we can calculate the Fourier transform of $e^{-ax^2/2}$ by a change of variables and (15.3):

$$\int_{-\infty}^\infty e^{-ax^2/2}e^{-ixy}\,\mathrm{d}x = \int_{-\infty}^\infty e^{-t^2/2}e^{-ity/\sqrt{a}}\frac{\mathrm{d}t}{\sqrt{a}} \quad \text{where } t = \sqrt{a}x$$
$$= \frac{1}{\sqrt{a}}(\mathcal{F}f)\left(\frac{y}{\sqrt{a}}\right)$$
$$= \frac{1}{\sqrt{a}}\sqrt{2\pi}e^{-(y/\sqrt{a})^2/2} \text{ by (15.3)}$$
$$= \sqrt{\frac{2\pi}{a}}e^{-y^2/(2a)}.$$

This calculation shows that, up to a scaling factor, a highly peaked Gaussian ($e^{-ax^2/2}$ for large $a$) has a Fourier transform that is spread out ($e^{-y^2/(2a)}$ for small $1/a$) and a spread out Gaussian ($e^{-ax^2/2}$ for small $a$) has a Fourier transform that is highly peaked ($e^{-y^2/(2a)}$ for large $1/a$). The Fourier transform's effect of exchanging highly peaked and spread out Gaussians is a mathematical expression of the Heisenberg Uncertainty Principle from quantum mechanics.

## 16. Exercises

1. For $t > 0$, show by calculus that $\int_0^\infty \frac{\mathrm{d}x}{x^2+t^2} = \frac{\pi}{2t}$ and then prove by differentiation under the integral sign that $\int_0^\infty \frac{\mathrm{d}x}{(x^2+t^2)^2} = \frac{\pi}{4t^3}$, $\int_0^\infty \frac{\mathrm{d}x}{(x^2+t^2)^3} = \frac{3\pi}{16t^5}$, and $\int_0^\infty \frac{\mathrm{d}x}{(x^2+t^2)^n} = \binom{2n-2}{n-1}\frac{\pi}{(2t)^{2n-1}}$ for all $n \geq 1$.

<!-- page 25 -->

2. Starting from the formula $\int_{\mathbf{R}}\frac{\cos(tx)}{1+x^2}\,\mathrm{d}x = \frac{\pi}{e^t}$ in (14.1) for $t > 0$, make a change of variables and then differentiate under the integral sign to prove $\int_{\mathbf{R}}\frac{\cos x}{(x^2+t^2)^2}\,\mathrm{d}x = \frac{\pi(t+1)}{2t^3 e^t}$ if $t > 0$.

3. From the formula $\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2} - \arctan t$ for $t > 0$, in Section 3, use a change of variables to obtain a formula for $\int_0^\infty e^{-ax}\frac{\sin(bx)}{x}\,\mathrm{d}x$ when $a$ and $b$ are positive. Then use differentiation under the integral sign with respect to $b$ to find a formula for $\int_0^\infty e^{-ax}\cos(bx)\,\mathrm{d}x$ when $a$ and $b$ are positive. (Differentiation under the integral sign with respect to $a$ will produce a formula for $\int_0^\infty e^{-ax}\sin(bx)\,\mathrm{d}x$, but that would be circular in our approach since we used that integral in our derivation of the formula for $\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x$ in Section 3.)

4. By the formula $\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2} - \arctan t$ for $t > 0$, let $x = ay$ for $a > 0$ to see

$$\int_0^\infty e^{-tay}\frac{\sin(ay)}{y}\,\mathrm{d}y = \frac{\pi}{2} - \arctan t,$$

so the integral on the left is independent of $a$ and thus has $a$-derivative 0. Differentiation under the integral sign, with respect to $a$, implies

$$\int_0^\infty e^{-tay}(\cos(ay) - t\sin(ay))\,\mathrm{d}y = 0.$$

Verify that this application of differentiation under the integral sign is valid when $a > 0$ and $t > 0$. What happens if $t = 0$?

5. Show $\int_0^\infty \frac{\sin(tx)}{x(x^2+1)}\,\mathrm{d}x = \frac{\pi}{2}(1 - e^{-t})$ for $t > 0$ by justifying differentiation under the integral sign and using (14.1).

6. Prove $\int_0^\infty e^{-tx}\frac{\cos x - 1}{x}\,\mathrm{d}x = \log\left(\frac{t}{\sqrt{1+t^2}}\right)$ for $t > 0$. What happens to the integral as $t \to 0^+$?

7. Prove $\int_0^\infty \frac{\log(1+t^2 x^2)}{1+x^2}\,\mathrm{d}x = \pi\log(1+t)$ for $t > 0$ (it is obvious for $t = 0$). Then deduce, for $a > 0$ and $b > 0$,

$$\int_0^\infty \frac{\log(1+a^2 x^2)}{b^2+x^2}\,\mathrm{d}x = \frac{\pi\log(1+ab)}{b}.$$

8. Prove $\int_0^\infty (e^{-x} - e^{-tx})\frac{\mathrm{d}x}{x} = \log t$ for $t > 0$ by justifying differentiation under the integral sign. This is (8.2) for $t > -1$. Deduce that $\int_0^\infty (e^{-ax} - e^{-bx})\frac{\mathrm{d}x}{x} = \log(b/a)$ for $a > 0$ and $b > 0$.

<!-- page 26 -->

9. Prove $\int_0^\infty e^{-\frac{1}{2}x^2 - \frac{t^2}{2x^2}}\,\mathrm{d}x = \sqrt{\frac{\pi}{2}}e^{-|t|}$ for all $t$ by justifying differentiation under the integral sign for $t > 0$.[^10] (As in Section 14, the integral is not differentiable at $t = 0$.) Deduce that $\int_0^\infty e^{-ax^2 - b/x^2}\,\mathrm{d}x = \frac{\sqrt{\pi}}{2\sqrt{a}}e^{-2\sqrt{ab}}$ for $a > 0$ and $b > 0$. (Hint: Let $F(t)$ be the integral. Use differentiation under the integral sign and a change of variables to show $F'(t) = -F(t)$ if $t > 0$.)

10. In calculus textbooks, formulas for the indefinite integrals

$$\int x^n\sin x\,\mathrm{d}x \quad \text{and} \quad \int x^n\cos x\,\mathrm{d}x$$

are derived recursively using integration by parts. Find formulas for these integrals when $n = 1, 2, 3, 4$ using differentiation under the integral sign starting with the formulas

$$\int \cos(tx)\,\mathrm{d}x = \frac{\sin(tx)}{t}, \quad \int \sin(tx)\,\mathrm{d}x = -\frac{\cos(tx)}{t}$$

for $t > 0$. The integrals $\int x^n e^{-x}\,\mathrm{d}x$ can be worked out in a similar way[^11] from $\int e^{-tx}\,\mathrm{d}x = e^{-tx}/t$ for $t > 0$.

11. Here is another approach to (12.7). For $t \in \mathbf{R}$ let $F(t) = \int_0^1 \frac{\log(1+tx)}{1+x^2}\,\mathrm{d}x$ (the upper bound of integration is 1, not $t$). Compute $F'(t)$ explicitly using a partial fraction decomposition and then show $F(1) = \int_0^1 F'(t)\,\mathrm{d}t = -F(1) + (\pi/4)\log 2$ to solve for $F(1)$.

12. If you are familiar with integration of complex-valued functions, show for $y \in \mathbf{R}$ that

$$\int_{-\infty}^\infty e^{-(x+iy)^2}\,\mathrm{d}x = \sqrt{2\pi}.$$

In other words, show the integral on the left side is independent of $y$. (Hint: Use differentiation under the integral sign to compute the $y$-derivative of the left side.)

## Appendix A. Justifying Passage to the Limit in a Sine Integral

In Section 3 we derived the equation

$$\int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2} - \arctan t \quad \text{for } t > 0, \tag{A.1}$$

which by naive passage to the limit as $t \to 0^+$ suggests that

$$\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2}. \tag{A.2}$$

To prove (A.2), we will show by *two methods* that $\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x$ exists and that as $t \to 0^+$,

$$\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x - \int_0^\infty e^{-tx}\frac{\sin x}{x}\,\mathrm{d}x = \int_0^\infty (1 - e^{-tx})\frac{\sin x}{x}\,\mathrm{d}x \to 0. \tag{A.3}$$

Then (A.3) implies (A.2) since $\int_0^\infty e^{-tx}(\sin x)/x\,\mathrm{d}x \to \pi/2$ as $t \to 0^+$ by (A.1).

<!-- page 27 -->

**Method 1: Alternating series.** On $[k\pi, (k+1)\pi]$ where $k$ is an integer, $\sin x = (-1)^k|\sin x|$, so convergence of $\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x = \lim_{b\to\infty}\int_0^b \frac{\sin x}{x}\,\mathrm{d}x$ is equivalent to convergence of the alternating series

$$\sum_{k\geq 0}\int_{k\pi}^{(k+1)\pi}\frac{\sin x}{x}\,\mathrm{d}x = \sum_{k\geq 0}(-1)^k\int_{k\pi}^{(k+1)\pi}\frac{|\sin x|}{x}\,\mathrm{d}x. \tag{A.4}$$

This series is not absolutely convergent: $1/x$ on $[k\pi, (k+1)\pi]$ has upper and lower bounds $1/k\pi$ and $1/(k+1)\pi$, so

$$\frac{2}{(k+1)\pi} \leq \int_{k\pi}^{(k+1)\pi}\frac{|\sin x|}{x}\,\mathrm{d}x \leq \frac{2}{k\pi} \tag{A.5}$$

since $\int_{k\pi}^{(k+1)\pi}|\sin x|\,\mathrm{d}x = 2$. Thus

$$\sum_{k\geq 0}\int_{k\pi}^{(k+1)\pi}\frac{|\sin x|}{x}\,\mathrm{d}x \geq \sum_{k\geq 0}\frac{2}{(k+1)\pi} = \frac{2}{\pi}\sum_{k\geq 1}\frac{1}{k} = \infty.$$

To show the alternating series (A.4) converges, we will use the alternating series test. The terms $a_k = \int_{k\pi}^{(k+1)\pi}\frac{|\sin x|}{x}\,\mathrm{d}x$ are monotonically decreasing:

$$a_{k+1} = \int_{(k+1)\pi}^{(k+2)\pi}\frac{|\sin x|}{x}\,\mathrm{d}x = \int_{k\pi}^{(k+1)\pi}\frac{|\sin(x+\pi)|}{x+\pi}\,\mathrm{d}x = \int_{k\pi}^{(k+1)\pi}\frac{|\sin x|}{x+\pi}\,\mathrm{d}x < a_k.$$

We have $a_k \leq 2/(k\pi)$ for $k \geq 1$ by (A.5), so $a_k \to 0$. Thus $\int_0^\infty \frac{\sin x}{x}\,\mathrm{d}x = \sum_{k\geq 0}(-1)^k a_k$ converges.

To show the right side of (A.3) tends to 0 as $t \to 0^+$, we write it as an alternating series. Writing the interval of integration $[0,\infty)$ as the union of intervals $[k\pi, (k+1)\pi)$ for $k \geq 0$,

$$\int_0^\infty (1-e^{-tx})\frac{\sin x}{x}\,\mathrm{d}x = \sum_{k\geq 0}(-1)^k I_k(t), \quad \text{where } I_k(t) = \int_{k\pi}^{(k+1)\pi}(1-e^{-tx})\frac{|\sin x|}{x}\,\mathrm{d}x. \tag{A.6}$$

Since $1 - e^{-tx} > 0$ for $t > 0$ and $x > 0$, the series $\sum_{k\geq 0}(-1)^k I_k(t)$ is alternating. The upper bound $1 - e^{-tx} < 1$ tells us $I_k(t) \leq 1/k$ for $k \geq 1$ by the same reasoning we used on $a_k$ above, so $I_k(t) \to 0$ as $k \to \infty$. To show the terms $I_k(t)$ are monotonically decreasing with $k$, set this up as the inequality

$$I_k(t) - I_{k+1}(t) > 0 \quad \text{for } t > 0. \tag{A.7}$$

Each $I_k(t)$ is a function of $t$ for all $t$, not just $t > 0$ (note $I_k(t)$ only involves integration on a bounded interval). The difference $I_k(t) - I_{k+1}(t)$ vanishes when $t = 0$ (in fact both terms are then 0), and $I_k'(t) = \int_{k\pi}^{(k+1)\pi}e^{-tx}|\sin x|\,\mathrm{d}x$ for all $t$ by differentiation under the integral sign, so (A.7) would follow from the derivative inequality $I_k'(t) - I_{k+1}'(t) > 0$ for $t > 0$. By a change of variables $y = x - \pi$ in the integral for $I_{k+1}'(t)$,

$$I_{k+1}'(t) = \int_{k\pi}^{(k+1)\pi}e^{-t(y+\pi)}|\sin(y+\pi)|\,\mathrm{d}y = e^{-t\pi}\int_{k\pi}^{(k+1)\pi}e^{-ty}|\sin y|\,\mathrm{d}y < I_k'(t).$$

This completes the proof that the series in (A.6) for $t > 0$ satisfies the alternating series test.

If we truncate the series $\sum_{k\geq 0}(-1)^k I_k(t)$ after the $N$th term, the magnitude of the error is no greater than the absolute value of the next term:

$$\sum_{k\geq 0}(-1)^k I_k(t) = \sum_{k=0}^N(-1)^k I_k(t) + r_N, \quad \text{where } |r_N| \leq |I_{N+1}(t)| \leq \frac{1}{N+1}.$$

<!-- page 28 -->

Since $0 \leq 1 - e^{-y} \leq y$ for $y \geq 0$,

$$\left|\sum_{k=0}^N(-1)^k I_k(t)\right| \leq \int_0^{(N+1)\pi}(1-e^{-tx})\frac{|\sin x|}{x}\,\mathrm{d}x = \int_0^{(N+1)\pi}t\,\mathrm{d}x = t(N+1)\pi.$$

Thus

$$\left|\int_0^\infty(1-e^{-tx})\frac{\sin x}{x}\,\mathrm{d}x\right| = \left|\sum_{k\geq 0}(-1)^k I_k(t)\right|$$
$$\leq \left|\sum_{k=0}^N(-1)^k I_k(t)\right| + |r_N|$$
$$\leq t(N+1)\pi + \frac{1}{N+1}.$$

For $\varepsilon > 0$ we can make the second term at most $\varepsilon/2$ by a suitable choice of $N$. Then the first term is at most $\varepsilon/2$ for all small enough $t$ (depending on $N$), and that shows (A.3) tends to 0 as $t \to 0^+$.

**Method 2: Integration by parts.** (I learned this approach from Lior Silberman.) We will show (A.2) converges by rewriting it as an absolutely convergent integral. Using $u = 1/x$ and $\mathrm{d}v = \sin x\,\mathrm{d}x$, we have $\mathrm{d}u = -\mathrm{d}x/x^2$ and let $v = 1 - \cos x$ (*not* $v = -\cos x$), so when $0 < a < b < \infty$,

$$\int_a^b\frac{\sin x}{x}\,\mathrm{d}x = \left.\frac{1-\cos x}{x}\right|_a^b + \int_a^b\frac{1-\cos x}{x^2}\,\mathrm{d}x. \tag{A.8}$$

In the first term on the right, $(1-\cos x)/x \to 0$ as $x \to 0^+$ and $x \to \infty$ due to $\cos x = 1 + O(x^2)$ when $x$ is small and $|(1-\cos x)/x| \leq 2/x$ when $x > 0$. In the integral on the right, $(1-\cos x)/x^2$ is absolutely integrable on $[0,\infty)$ since it is bounded near 0 due to $\cos x = 1 + O(x^2)$ when $x$ is small and since $|(1-\cos x)/x^2| \leq 2/x^2$ when $x \geq 1$. Thus we can let $a \to 0^+$ and $b \to \infty$ in (A.8) to see

$$\int_0^\infty\frac{\sin x}{x}\,\mathrm{d}x = \int_0^\infty\frac{1-\cos x}{x^2}\,\mathrm{d}x, \tag{A.9}$$

with the right side being absolutely convergent.

Next, we want to show

$$\lim_{t\to 0^+}\int_0^\infty(1-e^{-tx})\frac{\sin x}{x}\,\mathrm{d}x = 0.$$

We will rewrite the integral in absolutely convergent form and then show it tends to 0 in the limit. Let $u = (1-e^{-tx})/x$, $\mathrm{d}v = \sin x\,\mathrm{d}x$, $\mathrm{d}u = ((-1+(1+tx)e^{-tx})/x^2)\,\mathrm{d}x$, and $v = 1 - \cos x$ (*not* $v = -\cos x$). When $0 < a < b < \infty$,

$$\int_a^b(1-e^{-tx})\frac{\sin x}{x}\,\mathrm{d}x = \left.\frac{(1-e^{-tx})(1-\cos x)}{x}\right|_a^b + \int_a^b\frac{(1-(1+tx)e^{-tx})(1-\cos x)}{x^2}\,\mathrm{d}x. \tag{A.10}$$

In the first term on the right side, $0 \leq 1 - e^{-tx} < 1$ on $[0,\infty)$ and $(1-\cos x)/x \to 0$ as $x \to 0^+$ and $x \to \infty$ as we saw above. In the integral on the right side, the integrand is absolutely integrable on $[0,\infty)$ since it is bounded near 0 due to $\cos x = 1 + O(x^2)$ when $x$ is small and since $0 < (1+y)e^{-y} \leq 1$ when $y \geq 0$. Letting $a \to 0^+$ and $b \to \infty$ in (A.10), we get

$$\int_0^\infty(1-e^{-tx})\frac{\sin x}{x}\,\mathrm{d}x = \int_0^\infty\frac{(1-(1+tx)e^{-tx})(1-\cos x)}{x^2}\,\mathrm{d}x.$$

To show the integral on the right tends to 0 as $t \to 0^+$, we will break up the interval of integration into two intervals and make separate estimates. As a power series, $(1+y)e^{-y} = 1 - y^2/2 + y^3/3 - \cdots$

<!-- page 29 -->

is alternating, so $1 - y^2/2 < (1+y)e^{-y} \leq 1$ when $y \geq 0$. Thus $0 \leq 1 - (1+y)e^{-y} < y^2/2$, so when $0 < c < \infty$

$$0 < \int_0^c\frac{(1-(1+tx)e^{-tx})(1-\cos x)}{x^2}\,\mathrm{d}x \leq \int_0^c\frac{((tx)^2/2)(2)}{x^2}\,\mathrm{d}x = t^2 c.$$

Also

$$0 < \int_c^\infty\frac{(1-(1+tx)e^{-tx})(1-\cos x)}{x^2}\,\mathrm{d}x < \int_c^\infty\frac{1-\cos x}{x^2}\,\mathrm{d}x < \int_c^\infty\frac{2}{x^2}\,\mathrm{d}x = \frac{2}{c}.$$

Thus

$$0 < \int_0^\infty\frac{(1-(1+tx)e^{-tx})(1-\cos x)}{x^2}\,\mathrm{d}x < t^2 c + \frac{2}{c}$$

for all $c > 0$. Using $c = 1/t$, the upper bound is $t + 2t = 3t$, which tends to 0 as $t \to 0^+$.

**Remark A.1.** By (A.2) and (A.9), $\int_0^\infty \frac{1-\cos(tx)}{x^2}\,\mathrm{d}x = \frac{\pi}{2}t$ by the change of variables $u = tx$ for $t > 0$. That $\cos x$ is even and $\cos(0) = 0$ then implies $\int_0^\infty \frac{1-\cos(tx)}{x^2}\,\mathrm{d}x = \frac{\pi}{2}|t|$ for all $t$.

## Appendix B. An Example from the Book Feynman Studied

The book *Advanced Calculus* by Frederick Woods [16] is where Feynman learned differentiation under the integral sign. Figure 2 below has an example from the book: $\int_0^\infty e^{-\alpha x}(\sin x)/x\,\mathrm{d}x$ when $\alpha > 0$, which is our (3.1). Woods obtained the value $\pi/2 - \arctan(\alpha)$ and rewrote it as $\arctan(1/\alpha)$, which is valid when $\alpha > 0$ (not when $\alpha < 0$).

<!-- Figure 2. Page 154 in Woods' Advanced Calculus. -->

<!-- page 30 -->

The sections of this book discussing differentiation under the integral sign are 60, 61 (for bounded intervals), and 63 (for unbounded intervals), and there are exercises at the end of the chapter on pp. 159--163.

## References

[1] W. Appel, *Mathematics for Physics and Physicists*, Princeton Univ. Press, Princeton, 2007.

[2] W. Byerly, *Elements of the Integral Calculus*, 2nd ed., Ginn & Co., 1888. URL https://archive.org/details/cu31924004779447/page/n5.

[3] S. Cao, Integrating $\int_0^\infty e^{-x^2}\,\mathrm{d}x$ using Feynman's parametrization trick, URL (version: 2017-09-08): http://math.stackexchange.com/questions/390850/.

[4] Conifold, answer to Why is differentiation under the integral sign named the Leibniz rule?, URL (version: 2019-01-06): https://hsm.stackexchange.com/questions/8132.

[5] R. P. Feynman, *Surely You're Joking, Mr. Feynman!*, Bantam, New York, 1985.

[6] R. P. Feynman, *Mathematical Methods*, 1946 Cornell University notes by James C. Keck, http://james-keck-memorial-collection.unibs.it/JCKeck-papers/JCKeck-class-notes-from-Feynman's-course-on-Mathematical-Methods-at-Cornell-1946.pdf

[7] R. P. Feynman, *Hughes Lectures Vol. 3*, notes by John T. Neer, http://www.thehugheslectures.info/wp-content/uploads/lectures/FeynmanHughesLectures_Vol3.pdf.

[8] R. P. Feynman, *Hughes Lectures Vol. 5*, notes by John T. Neer, http://www.thehugheslectures.info/wp-content/uploads/lectures/FeynmanHughesLectures_Vol5.pdf.

[9] S. K. Goel and A. J. Zajta, "Parametric Integration Techniques," Math. Mag. **62** (1989), 318--322.

[10] S. Lang, *Undergraduate Analysis*, 2nd ed., Springer-Verlag, New York, 1997.

[11] S. Lang, *Complex Analysis*, 3rd ed., Springer-Verlag, New York, 1993.

[12] M. Rozman, "Evaluate Gaussian and Fresnel's integrals using differentiation under the integral sign," Course notes for Physics 2400 (UConn), Fall 2020. URL https://www.phys.uconn.edu/~rozman/Courses/P2400_20F/downloads/gaussian-type-integrals.pdf

[13] A. R. Schep, "A Simple Complex Analysis and an Advanced Calculus Proof of the Fundamental Theorem of Algebra," Amer. Math. Monthly **116** (2009), 67--68.

[14] E. Talvila, "Some Divergent Trigonometric Integrals," Amer. Math. Monthly **108** (2001), 432--436.

[15] H. Whitney, "Differentiable even functions," Duke Math. J. **10** (1943), 159-160.

[16] F. S. Woods, *Advanced Calculus*, New Edition, Ginn and Co., New York, 1934. URL https://archive.org/details/advancedcalculuswoods.

[17] J. van Yzeren, "Moivre's and Fresnel's Integrals by Simple Integration," Amer. Math. Monthly **86** (1979), 690--693.

[^1]: The book Feynman read was *Advanced Calculus* by Woods [16]. See Appendix B for an excerpt.
[^2]: See https://scientistseessquirrel.wordpress.com/2016/02/09/do-biology-students-need-calculus/ for a similar story with integration by parts in the first footnote.
[^3]: Just before this quote, Feynman wrote "One thing I never did learn was contour integration." Perhaps he meant that he never felt he learned it *well*, since he did know it. See [6, Lect. 14, 15, 17, 19], [7, p. 92], and [8, pp. 47--49]. A challenge he gave in [5, p. 176] suggests he didn't like contour integration.
[^4]: Or see https://mathoverflow.net/questions/72497/.
[^5]: This second proof is written with $b = \infty$, but the argument can be adapted to finite $b$.
[^6]: Since $-\delta \leq x \leq 1/(2\varepsilon)$ and $-\varepsilon < t < 1/(2\delta)$, $xt < \max(\varepsilon\delta, 1/(4\varepsilon\delta))$, and the maximum is $1/(4\varepsilon\delta)$ when $\varepsilon, \delta < 1/2$.
[^7]: If you know complex analysis, you can get (14.1) for $t > 0$ from the residue theorem, viewing $\cos(tx)$ as the real part of $e^{itx}$. If you know Fourier analysis, you can interpret (14.1) as saying $1/(1+x^2)$ has Fourier transform $\pi e^{-|t|}$, where a function $f(x)$ has Fourier transform $\hat{f}(t) = \int_{\mathbf{R}} f(x)e^{-ixt}\,\mathrm{d}x$.
[^8]: Some webpages and online videos compute integrals like $F(t)$ by this method with mistakes.