# The Gaussian Integral

> **Source**: https://kconrad.math.uconn.edu/blurbs/gaussianintegral.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  

<!-- page 1 -->

Let

$$I = \int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}\,\mathrm{d}x, \quad J = \int_0^{\infty} e^{-x^2}\,\mathrm{d}x, \quad \text{and} \quad K = \int_{-\infty}^{\infty} e^{-\pi x^2}\,\mathrm{d}x.$$

These positive numbers are related: $J = I/(2\sqrt{2})$ and $K = I/\sqrt{2\pi}$.

**Theorem.** *With notation as above, $I = \sqrt{2\pi}$, or equivalently $J = \sqrt{\pi}/2$, or equivalently $K = 1$.*

We will give multiple proofs of this. (Other lists of proofs are in [5] and [10].) It is subtle since $e^{-\frac{1}{2}x^2}$ has no simple antiderivative. For comparison, $\int_0^{\infty} xe^{-\frac{1}{2}x^2}\,\mathrm{d}x$ can be computed with the antiderivative $-e^{-\frac{1}{2}x^2}$ and equals $1$. In the last section, the Gaussian integral's history is presented.

## 1. First Proof: Polar Coordinates

The most widely known proof, due to Poisson [10, p. 3], expresses $J^2$ as a double integral and then uses polar coordinates. To start, write $J^2$ as an iterated integral using single-variable calculus:

$$J^2 = J\int_0^{\infty} e^{-y^2}\,\mathrm{d}y = \int_0^{\infty} Je^{-y^2}\,\mathrm{d}y = \int_0^{\infty}\left(\int_0^{\infty} e^{-x^2}\,\mathrm{d}x\right)e^{-y^2}\,\mathrm{d}y = \int_0^{\infty}\int_0^{\infty} e^{-(x^2+y^2)}\,\mathrm{d}x\,\mathrm{d}y.$$

View this as a double integral over the first quadrant. To compute it with polar coordinates, the first quadrant is $\{(r,\theta) : r \geq 0 \text{ and } 0 \leq \theta \leq \pi/2\}$. Writing $x^2 + y^2$ as $r^2$ and $\mathrm{d}x\,\mathrm{d}y$ as $r\,\mathrm{d}r\,\mathrm{d}\theta$,

$$J^2 = \int_0^{\pi/2}\int_0^{\infty} e^{-r^2}r\,\mathrm{d}r\,\mathrm{d}\theta = \int_0^{\infty} re^{-r^2}\,\mathrm{d}r \cdot \int_0^{\pi/2}\mathrm{d}\theta = -\frac{1}{2}e^{-r^2}\bigg|_0^{\infty} \cdot \frac{\pi}{2} = \frac{1}{2} \cdot \frac{\pi}{2} = \frac{\pi}{4}.$$

Since $J > 0$, $J = \sqrt{\pi}/2$.[^1] It is argued in [2] that this method can't be used on any other integral.

## 2. Second Proof: Another Change of Variables

Our next proof uses another change of variables to compute $J^2$. As before,

$$J^2 = \int_0^{\infty}\left(\int_0^{\infty} e^{-(x^2+y^2)}\,\mathrm{d}x\right)\mathrm{d}y.$$

[^1]: For a visualization of this calculation as a volume, in terms of $\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x$ instead of $J$, see https://www.youtube.com/watch?v=cy8r7WSuT1I. We'll do a volume calculation for $I^2$ in Section 5.

<!-- page 2 -->

Instead of using polar coordinates, set $x = yt$ in the inner integral ($y$ is fixed). Then $\mathrm{d}x = y\,\mathrm{d}t$ and

$$J^2 = \int_0^{\infty}\left(\int_0^{\infty} e^{-y^2(t^2+1)}y\,\mathrm{d}t\right)\mathrm{d}y = \int_0^{\infty}\left(\int_0^{\infty} ye^{-y^2(t^2+1)}\,\mathrm{d}y\right)\mathrm{d}t, \tag{2.1}$$

where the interchange of integrals is justified by Fubini's theorem for improper Riemann integrals. (The appendix gives an approach using Fubini's theorem for Riemann integrals on rectangles.) Since $\int_0^{\infty} ye^{-ay^2}\,\mathrm{d}y = \frac{1}{2a}$ for $a > 0$, we have

$$J^2 = \int_0^{\infty} \frac{\mathrm{d}t}{2(t^2+1)} = \frac{1}{2} \cdot \frac{\pi}{2} = \frac{\pi}{4},$$

so $J = \sqrt{\pi}/2$. This proof is due to Laplace [8, pp. 94--96] and historically precedes the widely used technique of the previous proof. We will see in Section 9 what Laplace's first proof was.

## 3. Third Proof: Differentiating Under the Integral Sign

For $t > 0$, set

$$A(t) = \left(\int_0^t e^{-x^2}\,\mathrm{d}x\right)^2.$$

The integral we want to calculate is $A(\infty) = J^2$ and then take a square root.

Differentiating $A(t)$ with respect to $t$ and using the Fundamental Theorem of Calculus,

$$A'(t) = 2\int_0^t e^{-x^2}\,\mathrm{d}x \cdot e^{-t^2} = 2e^{-t^2}\int_0^t e^{-x^2}\,\mathrm{d}x.$$

Let $x = ty$, so

$$A'(t) = 2e^{-t^2}\int_0^1 te^{-t^2y^2}\,\mathrm{d}y = \int_0^1 2te^{-(1+y^2)t^2}\,\mathrm{d}y.$$

The function under the integral sign is easily antidifferentiated *with respect to $t$*:

$$A'(t) = \int_0^1 -\frac{\partial}{\partial t}\frac{e^{-(1+y^2)t^2}}{1+y^2}\,\mathrm{d}y = -\frac{\mathrm{d}}{\mathrm{d}t}\int_0^1 \frac{e^{-(1+y^2)t^2}}{1+y^2}\,\mathrm{d}y.$$

Letting

$$B(t) = \int_0^1 \frac{e^{-t^2(1+x^2)}}{1+x^2}\,\mathrm{d}x,$$

we have $A'(t) = -B'(t)$ for all $t > 0$, so there is a constant $C$ such that

$$A(t) = -B(t) + C \tag{3.1}$$

for all $t > 0$. To find $C$, we let $t \to 0^+$ in (3.1). The left side tends to $\left(\int_0^0 e^{-x^2}\,\mathrm{d}x\right)^2 = 0$ while the right side tends to $-\int_0^1 \mathrm{d}x/(1+x^2) + C = -\pi/4 + C$. Thus $C = \pi/4$, so (3.1) becomes

$$\left(\int_0^t e^{-x^2}\,\mathrm{d}x\right)^2 = \frac{\pi}{4} - \int_0^1 \frac{e^{-t^2(1+x^2)}}{1+x^2}\,\mathrm{d}x.$$

Letting $t \to \infty$ in this equation, we obtain $J^2 = \pi/4$, so $J = \sqrt{\pi}/2$.

A comparison of this proof with the first proof is in [22].

<!-- page 3 -->

## 4. Fourth Proof: Another Differentiation Under the Integral Sign

Here is a second approach to finding $J$ by differentiation under the integral sign. I heard about it from Michael Rozman [15], who modified an idea on math.stackexchange [24], and in a slightly less elegant form it appeared much earlier in [20].

For $t \in \mathbf{R}$, set

$$F(t) = \int_0^{\infty} \frac{e^{-t^2(1+x^2)}}{1+x^2}\,\mathrm{d}x.$$

Then $F(0) = \int_0^{\infty} \mathrm{d}x/(1+x^2) = \pi/2$ and $F(\infty) = 0$. Differentiating under the integral sign,

$$F'(t) = \int_0^{\infty} -2te^{-t^2(1+x^2)}\,\mathrm{d}x = -2te^{-t^2}\int_0^{\infty} e^{-(tx)^2}\,\mathrm{d}x.$$

Make the substitution $y = tx$, with $\mathrm{d}y = t\,\mathrm{d}x$, so

$$F'(t) = -2e^{-t^2}\int_0^{\infty} e^{-y^2}\,\mathrm{d}y = -2Je^{-t^2}.$$

For $b > 0$, integrate both sides from $0$ to $b$ and use the Fundamental Theorem of Calculus:

$$\int_0^b F'(t)\,\mathrm{d}t = -2J\int_0^b e^{-t^2}\,\mathrm{d}t \implies F(b) - F(0) = -2J\int_0^b e^{-t^2}\,\mathrm{d}t.$$

Letting $b \to \infty$ in the last equation,

$$0 - \frac{\pi}{2} = -2J^2 \implies J^2 = \frac{\pi}{4} \implies J = \frac{\sqrt{\pi}}{2}.$$

## 5. Fifth Proof: A Volume Integral

Our next proof is due to T. P. Jameson [6] and was rediscovered by A. L. Delgado [4]. Revolve $z = e^{-\frac{1}{2}x^2}$ in the $xz$-plane around the $z$-axis to produce the "bell surface" $z = e^{-\frac{1}{2}(x^2+y^2)}$. See Figure 1, where the $z$-axis is vertical and passes through the top point, the $x$-axis lies just under the surface through the point $0$ in front, and the $y$-axis lies just under the surface through the point $0$ on the left. We will compute the volume $V$ below the surface and above the $xy$-plane in two ways.

First we compute $V$ by *horizontal slices*, which are discs: $V = \int_0^1 A(z)\,\mathrm{d}z$ where $A(z)$ is the area of the disc formed by slicing the surface at height $z$. Writing the radius of the disc at height $z$ as $r(z)$, $A(z) = \pi r(z)^2$. To compute $r(z)$, the surface cuts the $xz$-plane at a pair of points $(x, e^{-\frac{1}{2}x^2})$ where the height is $z$, so $e^{-\frac{1}{2}x^2} = z$. Thus $x^2 = -2\ln z$. Since $x$ is the distance of these points from the $z$-axis, $r(z)^2 = x^2 = -2\ln z$, so $A(z) = \pi r(z)^2 = -2\pi\ln z$. Therefore

$$V = \int_0^1 -2\pi\ln z\,\mathrm{d}z = -2\pi\left(z\ln z - z\right)\bigg|_0^1 = -2\pi\left(-1 - \lim_{z \to 0^+} z\ln z\right).$$

By L'Hospital's rule, $\lim_{z \to 0^+} z\ln z = 0$, so $V = 2\pi$. (A calculation of $V$ by shells is in [12].)

Next we compute $V$ by *vertical slices* in planes $x = \text{constant}$. Vertical slices are scaled bell curves: look at the black contour lines in Figure 1. The equation of the bell curve along the top of the vertical slice with $x$-coordinate $x$ is $z = e^{-\frac{1}{2}(x^2+y^2)}$, where $y$ varies and $x$ is fixed. Then

<!-- page 4 -->

<!-- Figure 1: The bell surface z = e^{-1/2(x^2+y^2)} -->

$$V = \int_{-\infty}^{\infty} A(x)\,\mathrm{d}x, \text{ where } A(x) \text{ is the area of the } x\text{-slice:}$$

$$A(x) = \int_{-\infty}^{\infty} e^{-\frac{1}{2}(x^2+y^2)}\,\mathrm{d}y = e^{-\frac{1}{2}x^2}\int_{-\infty}^{\infty} e^{-\frac{1}{2}y^2}\,\mathrm{d}y = e^{-\frac{1}{2}x^2}I.$$

Thus $V = \int_{-\infty}^{\infty} A(x)\,\mathrm{d}x = \int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}I\,\mathrm{d}x = I\int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}\,\mathrm{d}x = I^2$.

Comparing the two formulas for $V$, we have $2\pi = I^2$, so $I = \sqrt{2\pi}$.

## 6. Sixth Proof: The $\Gamma$-Function

For any integer $n \geq 0$, we have $n! = \int_0^{\infty} t^n e^{-t}\,\mathrm{d}t$. For $x > 0$ we define

$$\Gamma(x) = \int_0^{\infty} t^x e^{-t}\frac{\mathrm{d}t}{t},$$

so $\Gamma(n) = (n-1)!$ when $n \geq 1$. Using integration by parts, $\Gamma(x+1) = x\Gamma(x)$. One of the basic properties of the $\Gamma$-function [16, pp. 193--194] is

$$\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)} = \int_0^1 t^{x-1}(1-t)^{y-1}\,\mathrm{d}t. \tag{6.1}$$

<!-- page 5 -->

Set $x = y = 1/2$:

$$\Gamma\left(\frac{1}{2}\right)^2 = \int_0^1 \frac{\mathrm{d}t}{\sqrt{t(1-t)}}.$$

Note

$$\Gamma\left(\frac{1}{2}\right) = \int_0^{\infty} \sqrt{t}e^{-t}\frac{\mathrm{d}t}{t} = \int_0^{\infty} \frac{e^{-t}}{\sqrt{t}}\,\mathrm{d}t = \int_0^{\infty} \frac{e^{-x^2}}{x}2x\,\mathrm{d}x = 2\int_0^{\infty} e^{-x^2}\,\mathrm{d}x = 2J,$$

so $4J^2 = \int_0^1 \mathrm{d}t/\sqrt{t(1-t)}$. With the substitution $t = \sin^2\theta$,

$$4J^2 = \int_0^{\pi/2} \frac{2\sin\theta\cos\theta\,\mathrm{d}\theta}{\sin\theta\cos\theta} = 2\frac{\pi}{2} = \pi,$$

so $J = \sqrt{\pi}/2$. Equivalently, $\Gamma(1/2) = \sqrt{\pi}$. Any method that proves $\Gamma(1/2) = \sqrt{\pi}$ is also a method that calculates $\int_0^{\infty} e^{-x^2}\,\mathrm{d}x$.

## 7. Seventh Proof: Asymptotic Estimates

We will show $J = \sqrt{\pi}/2$ by a technique whose steps are based on [17, p. 371].

For $x \geq 0$, power series expansions show $1 + x \leq e^x \leq 1/(1-x)$. Reciprocating and replacing $x$ with $x^2$, we get

$$1 - x^2 \leq e^{-x^2} \leq \frac{1}{1+x^2} \tag{7.1}$$

for all $x \in \mathbf{R}$.

For any positive integer $n$, raise the terms in (7.1) to the $n$th power and integrate from $0$ to $1$:

$$\int_0^1 (1-x^2)^n\,\mathrm{d}x \leq \int_0^1 e^{-nx^2}\,\mathrm{d}x \leq \int_0^1 \frac{\mathrm{d}x}{(1+x^2)^n}.$$

Using the changes of variables $x = \sin\theta$ on the left, $x = y/\sqrt{n}$ in the middle, and $x = \tan\theta$ on the right,

$$\int_0^{\pi/2}(\cos\theta)^{2n+1}\,\mathrm{d}\theta \leq \frac{1}{\sqrt{n}}\int_0^{\sqrt{n}} e^{-y^2}\,\mathrm{d}y \leq \int_0^{\pi/4}(\cos\theta)^{2n-2}\,\mathrm{d}\theta < \int_0^{\pi/2}(\cos\theta)^{2n-2}\,\mathrm{d}\theta. \tag{7.2}$$

Set $I_k = \int_0^{\pi/2}(\cos\theta)^k\,\mathrm{d}\theta$, so $I_0 = \pi/2$, $I_1 = 1$, and (7.2) implies

$$\sqrt{n}I_{2n+1} \leq \int_0^{\sqrt{n}} e^{-y^2}\,\mathrm{d}y < \sqrt{n}I_{2n-2}. \tag{7.3}$$

We will show that as $k \to \infty$, $kI_k^2 \to \pi/2$. Then

$$\sqrt{n}I_{2n+1} = \frac{\sqrt{n}}{\sqrt{2n+1}}\sqrt{2n+1}I_{2n+1} \to \frac{1}{\sqrt{2}}\sqrt{\frac{\pi}{2}} = \frac{\sqrt{\pi}}{2}$$

and

$$\sqrt{n}I_{2n-2} = \frac{\sqrt{n}}{\sqrt{2n-2}}\sqrt{2n-2}I_{2n-2} \to \frac{1}{\sqrt{2}}\sqrt{\frac{\pi}{2}} = \frac{\sqrt{\pi}}{2},$$

so by (7.3), $\int_0^{\sqrt{n}} e^{-y^2}\,\mathrm{d}y \to \sqrt{\pi}/2$. Thus $J = \sqrt{\pi}/2$.

<!-- page 6 -->

To show $kI_k^2 \to \pi/2$, first we compute several values of $I_k$ explicitly by a recursion. Using integration by parts,

$$I_k = \int_0^{\pi/2}(\cos\theta)^k\,\mathrm{d}\theta = \int_0^{\pi/2}(\cos\theta)^{k-1}\cos\theta\,\mathrm{d}\theta = (k-1)(I_{k-2} - I_k),$$

so

$$I_k = \frac{k-1}{k}I_{k-2}. \tag{7.4}$$

Using (7.4) and the initial values $I_0 = \pi/2$ and $I_1 = 1$, the first few values of $I_k$ are computed and listed in Table 1.

| $k$ | $I_k$ | $k$ | $I_k$ |
|---|---|---|---|
| 0 | $\pi/2$ | 1 | 1 |
| 2 | $(1/2)(\pi/2)$ | 3 | 2/3 |
| 4 | $(3/8)(\pi/2)$ | 5 | 8/15 |
| 6 | $(15/48)(\pi/2)$ | 7 | 48/105 |

From Table 1 we see that

$$I_{2n}I_{2n+1} = \frac{1}{2n+1}\frac{\pi}{2} \tag{7.5}$$

for $0 \leq n \leq 3$, and this can be proved for all $n$ by induction using (7.4). Since $0 \leq \cos\theta \leq 1$ for $\theta \in [0, \pi/2]$, we have $I_k \leq I_{k-1} \leq I_{k-2} = \frac{k}{k-1}I_k$ by (7.4), so $I_{k-1} \sim I_k$ as $k \to \infty$. Therefore (7.5) implies

$$I_{2n}^2 \sim \frac{1}{2n}\frac{\pi}{2} \implies (2n)I_{2n}^2 \to \frac{\pi}{2}$$

as $n \to \infty$. Then

$$(2n+1)I_{2n+1}^2 \sim (2n)I_{2n}^2 \to \frac{\pi}{2}$$

as $n \to \infty$, so $kI_k^2 \to \pi/2$ as $k \to \infty$. This completes our proof that $J = \sqrt{\pi}/2$.

**Remark 7.1.** This proof is closely related to the fifth proof using the $\Gamma$-function. Indeed, by (6.1)

$$\frac{\Gamma\!\left(\frac{k+1}{2}\right)\Gamma\!\left(\frac{1}{2}\right)}{\Gamma\!\left(\frac{k+1}{2}+\frac{1}{2}\right)} = \int_0^1 t^{(k+1)/2+1}(1-t)^{1/2-1}\,\mathrm{d}t,$$

and with the change of variables $t = (\cos\theta)^2$ for $0 \leq \theta \leq \pi/2$, the integral on the right is equal to $2\int_0^{\pi/2}(\cos\theta)^k\,\mathrm{d}\theta = 2I_k$, so (7.5) is the same as

$$I_{2n}I_{2n+1} = \frac{\Gamma\!\left(\frac{2n+1}{2}\right)\Gamma\!\left(\frac{1}{2}\right)}{2\Gamma\!\left(\frac{2n+2}{2}\right)} \frac{\Gamma\!\left(\frac{2n+2}{2}\right)\Gamma\!\left(\frac{1}{2}\right)}{2\Gamma\!\left(\frac{2n+3}{2}\right)} = \frac{\Gamma\!\left(\frac{2n+1}{2}\right)\Gamma\!\left(\frac{1}{2}\right)^2}{4\Gamma\!\left(\frac{2n+1}{2}+1\right)} = \frac{\Gamma\!\left(\frac{2n+1}{2}\right)\Gamma\!\left(\frac{1}{2}\right)^2}{4\frac{2n+1}{2}\Gamma\!\left(\frac{2n+1}{2}\right)} = \frac{\Gamma\!\left(\frac{1}{2}\right)^2}{2(2n+1)}.$$

<!-- page 7 -->

By (7.5), $\pi = \Gamma(1/2)^2$. We saw in the fifth proof that $\Gamma(1/2) = \sqrt{\pi}$ if and only if $J = \sqrt{\pi}/2$.

## 8. Eighth Proof: Stirling's Formula

Besides the integral formula $\int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}\,\mathrm{d}x = \sqrt{2\pi}$ that we have been discussing, another place in mathematics where $\sqrt{2\pi}$ appears is in Stirling's formula:

$$n! \sim \frac{n^n}{e^n}\sqrt{2\pi n} \quad \text{as } n \to \infty.$$

In 1730 De Moivre proved $n! \sim C(n^n/e^n)\sqrt{n}$ for some positive number $C$ without being able to determine $C$. Stirling soon thereafter showed $C = \sqrt{2\pi}$ and wound up having the whole formula named after him. We will show that determining that the constant $C$ in Stirling's formula is $\sqrt{2\pi}$ is equivalent to showing that $J = \sqrt{\pi}/2$ (or, equivalently, that $I = \sqrt{2\pi}$).

Applying (7.4) repeatedly,

$$I_{2n} = \frac{2n-1}{2n}I_{2n-2} = \frac{(2n-1)(2n-3)}{(2n)(2n-2)}I_{2n-4} = \cdots = \frac{(2n-1)(2n-3)(2n-5)\cdots(5)(3)(1)}{(2n)(2n-2)(2n-4)\cdots(6)(4)(2)}I_0.$$

Inserting $(2n-2)(2n-4)(2n-6)\cdots(6)(4)(2)$ in the top and bottom,

$$I_{2n} = \frac{(2n-1)(2n-2)(2n-3)(2n-4)(2n-5)\cdots(6)(5)(4)(3)(2)(1)}{(2n)((2n-2)(2n-4)\cdots(6)(4)(2))^2}\frac{\pi}{2} = \frac{(2n-1)!}{2n(2^{n-1}(n-1)!)^2}\frac{\pi}{2}.$$

Applying De Moivre's asymptotic formula $n! \sim C(n/e)^n\sqrt{n}$,

$$I_{2n} \sim \frac{C((2n-1)/e)^{2n-1}\sqrt{2n-1}}{2n(2^{n-1}C((n-1)/e)^{n-1}\sqrt{n-1})^2}\frac{\pi}{2} = \frac{(2n-1)^{2n}\frac{1}{2n-1}\sqrt{2n-1}}{2n \cdot 2^{2(n-1)}Ce(n-1)^{2n}\frac{1}{(n-1)^2}(n-1)}\frac{\pi}{2}$$

as $n \to \infty$. For any $a \in \mathbf{R}$, $(1+a/n)^n \to e^a$ as $n \to \infty$, so $(n+a)^n \sim e^a n^n$. Substituting this into the above formula with $a = -1$ and $n$ replaced by $2n$,

$$I_{2n} \sim \frac{e^{-1}(2n)^{2n}\frac{1}{\sqrt{2n}}}{2n \cdot 2^{2(n-1)}Ce(e^{-1}n^n)^2\frac{1}{n^2}n}\frac{\pi}{2} = \frac{\pi}{C\sqrt{2n}}. \tag{8.1}$$

Since $I_{k-1} \sim I_k$, the outer terms in (7.3) are both asymptotic to $\sqrt{n}I_{2n} \sim \pi/(C\sqrt{2})$ by (8.1). Therefore

$$\int_0^{\sqrt{n}} e^{-y^2}\,\mathrm{d}y \to \frac{\pi}{C\sqrt{2}}$$

as $n \to \infty$, so $J = \pi/(C\sqrt{2})$. Therefore $C = \sqrt{2\pi}$ if and only if $J = \sqrt{\pi}/2$.

<!-- page 8 -->

## 9. Ninth Proof: The Original Proof

The original proof that $J = \sqrt{\pi}/2$ is due to Laplace [9] in 1774. (An English translation of Laplace's article is mentioned in the bibliographic citation for [9], with preliminary comments on that article in [19].) He wanted to compute

$$\int_0^1 \frac{\mathrm{d}x}{\sqrt{-\log x}}. \tag{9.1}$$

Setting $y = \sqrt{-\log x}$, this integral is $2\int_0^{\infty} e^{-y^2}\,\mathrm{d}y = 2J$, so we expect (9.1) to be $\sqrt{\pi}$.

Laplace's starting point for evaluating (9.1) was a formula of Euler:

$$\int_0^1 \frac{x^r\,\mathrm{d}x}{\sqrt{1-x^{2s}}} \int_0^1 \frac{x^{s+r}\,\mathrm{d}x}{\sqrt{1-x^{2s}}} = \frac{1}{s(r+1)}\frac{\pi}{2} \tag{9.2}$$

for positive $r$ and $s$. (Laplace himself said this formula held "whatever be" $r$ or $s$, but if $s < 0$ then the number under the square root is negative.) Accepting (9.2), let $r \to 0$ in it to get

$$\int_0^1 \frac{\mathrm{d}x}{\sqrt{1-x^{2s}}} \int_0^1 \frac{x^s\,\mathrm{d}x}{\sqrt{1-x^{2s}}} = \frac{1}{s}\frac{\pi}{2}. \tag{9.3}$$

Now let $s \to 0$ in (9.3). Then $1 - x^{2s} \sim -2s\log x$ by L'Hopital's rule, so (9.3) becomes

$$\left(\int_0^1 \frac{\mathrm{d}x}{\sqrt{-\log x}}\right)^2 = \pi.$$

Thus (9.1) is $\sqrt{\pi}$.

Euler's formula (9.2) looks mysterious, but we have met it before. In the formula let $x^s = \cos\theta$ with $0 \leq \theta \leq \pi/2$. Then $x = (\cos\theta)^{1/s}$, and after some calculations (9.2) turns into

$$\int_0^{\pi/2}(\cos\theta)^{(r+1)/s-1}\,\mathrm{d}\theta \int_0^{\pi/2}(\cos\theta)^{(r+1)/s}\,\mathrm{d}\theta = \frac{1}{(r+1)/s}\frac{\pi}{2}. \tag{9.4}$$

We used the integral $I_k = \int_0^{\pi/2}(\cos\theta)^k\,\mathrm{d}\theta$ before when $k$ is a nonnegative integer. This notation makes sense when $k$ is any positive real number, and then (9.4) assumes the form $I_\alpha I_{\alpha+1} = \frac{1}{\alpha+1}\frac{\pi}{2}$ for $\alpha = (r+1)/s - 1$, which is (7.5) with a possibly nonintegral index. Letting $r = 0$ and $s = 1/(2n+1)$ in (9.4) recovers (7.5). Letting $s \to 0$ in (9.3) corresponds to letting $n \to \infty$ in (7.5), so the proof in Section 7 is in essence a more detailed version of Laplace's 1774 argument.

## 10. Tenth Proof: Residue Theorem

We will calculate $\int_{-\infty}^{\infty} e^{-x^2/2}\,\mathrm{d}x$ using contour integrals and the residue theorem. However, we can't just integrate $e^{-z^2/2}$, as this function has no poles. For a long time nobody knew how to handle this integral using contour integration. For instance, in 1914 Watson [21, p. 79] wrote "Cauchy's theorem cannot be employed to evaluate all definite integrals; thus $\int_0^{\infty} e^{-x^2}\,\mathrm{d}x$ has not been evaluated except by other methods." In the 1940s several contour integral solutions were published using awkward contours such as parallelograms [11], [13, Sect. 5] (see [3, Exer. 9, p. 113] for a recent appearance). Our approach will follow Kneser [7, p. 121] (see also [14, pp. 413--414] or [23]), using a rectangular contour and the function

$$\frac{e^{-z^2/2}}{1 - e^{-\sqrt{\pi}(1+i)z}}.$$

<!-- page 9 -->

This function comes out of nowhere, so our first task is to motivate the introduction of this function.

We seek a meromorphic function $f(z)$ to integrate around the contour $\gamma_R$ in Figure 2, with vertices at $-R$, $R$, $R+ib$, and $-R+ib$, where $b$ will be fixed and we let $R \to \infty$.

<!-- Figure 2: Contour to compute Gaussian -->

Suppose $f(z) \to 0$ along the right and left sides of $\gamma_R$ uniformly as $R \to \infty$. Then by applying the residue theorem and letting $R \to \infty$, we would obtain (if the integrals converge)

$$\int_{-\infty}^{\infty} f(x)\,\mathrm{d}x + \int_{\infty}^{-\infty} f(x+ib)\,\mathrm{d}x = 2\pi i \sum_a \mathrm{Res}_{z=a}f(z),$$

where the sum is over poles of $f(z)$ with imaginary part between $0$ and $b$. This is equivalent to

$$\int_{-\infty}^{\infty} (f(x) - f(x+ib))\,\mathrm{d}x = 2\pi i \sum_a \mathrm{Res}_{z=a}f(z).$$

Therefore we want $f(z)$ to satisfy

$$f(z) - f(z+ib) = e^{-z^2/2}, \tag{10.1}$$

where $f(z)$ and $b$ need to be determined.

Let's try $f(z) = e^{-z^2/2}/d(z)$, for an unknown $d(z)$ whose zeros are poles of $f(z)$. We want

$$f(z) - f(z+\tau) = e^{-z^2/2} \tag{10.2}$$

for some $\tau$ (which will *not* be purely imaginary, so (10.1) doesn't quite work, but (10.1) is only motivation). Substituting $e^{-z^2/2}/d(z)$ for $f(z)$ in (10.2) gives us

$$e^{-z^2/2}\left(\frac{1}{d(z)} - \frac{e^{-\tau z - \tau^2/2}}{d(z+\tau)}\right) = e^{-z^2/2}. \tag{10.3}$$

Suppose $d(z+\tau) = d(z)$. Then (10.3) implies

$$d(z) = 1 - e^{-\tau z - \tau^2/2},$$

and with this definition of $d(z)$, $e^{-z^2/2}/d(z)$ satisfies (10.2) if and only if $e^{\tau^2} = 1$, or equivalently $\tau^2 \in 2\pi i\mathbf{Z}$. The simplest nonzero solution is $\tau = \sqrt{\pi}(1+i)$. From now on this is the value of $\tau$, so $e^{-\tau^2/2} = e^{-i\pi} = -1$ and $d(z) = 1 + e^{-\tau z}$. Set

$$f(z) = \frac{e^{-z^2/2}}{d(z)} = \frac{e^{-z^2/2}}{1 + e^{-\tau z}},$$

which is Kneser's function mentioned earlier. This function satisfies (10.2) and we henceforth ignore the motivation (10.1). Poles of $f(z)$ are at odd integral multiples of $\tau/2$.

We will integrate this $f(z)$ around the contour $\gamma_R$ in Figure 3, whose height $\sqrt{\pi}$ is $\mathrm{Im}(\tau)$.

<!-- page 10 -->

<!-- Figure 3: The contour gamma_R and poles of Kneser's function -->

The poles of $f(z)$ nearest the origin are plotted in Figure 3; they lie along the line $y = x$. The only pole of $f(z)$ inside $\gamma_R$ (for $R > \sqrt{\pi}/2$) is at $\tau/2$, so by the residue theorem

$$\int_{\gamma_R} f(z)\,\mathrm{d}z = 2\pi i\,\mathrm{Res}_{z=\tau/2}f(z) = 2\pi i \frac{e^{-\tau^2/8}}{(-\tau)e^{-\tau^2/2}} = \frac{2\pi i e^{3\tau^2/8}}{-\sqrt{\pi}(1+i)} = \frac{2\pi i e^{3\pi i/4}}{-\sqrt{\pi}(1+i)} = \sqrt{2\pi}.$$

Since the left and right sides of $\gamma_R$ have the same length, $\sqrt{\pi}$, for all $R$, to show the integral of $f$ along those sides tends to $0$ uniformly as $R \to \infty$, it suffices to show $f(z) \to 0$ uniformly along those sides as $R \to \infty$. Parametrize $z$ along the left and right sides as $-R+it$ and $R+it$ with $t$ running over $[0, \sqrt{\pi}]$ in one direction or the other (which won't matter since we'll be taking absolute values). Then, using the reverse triangle inequality in the denominator, when $R > \sqrt{\pi}$ (so $R > t$)

$$|f(R+it)| = \frac{|e^{-R^2/2-iRt+t^2/2}|}{|1+e^{-\tau(R+it)}|} \leq \frac{e^{-R^2/2}e^{t^2/2}}{|1-e^{-\mathrm{Re}(\tau(R+it))}|} \leq \frac{e^{-R^2/2}e^{\pi/2}}{1-e^{-\sqrt{\pi}(R-t)}} < \frac{e^{-R^2/2}e^{\pi/2}}{1-e^{-\sqrt{\pi}(R-\sqrt{\pi})}},$$

which tends to $0$ as $R \to \infty$. Also

$$|f(-R+it)| = \frac{|e^{-R^2/2+iRt+t^2/2}|}{|1+e^{-\tau(-R+it)}|} \leq \frac{e^{-R^2/2}e^{t^2/2}}{|1-e^{-\mathrm{Re}(\tau(-R+it))}|} \leq \frac{e^{-R^2/2}e^{\pi/2}}{e^{\sqrt{\pi}(R+t)}-1} < \frac{e^{-R^2/2}e^{\pi/2}}{e^{\sqrt{\pi}R}-1},$$

which tends to $0$ as $R \to \infty$. Thus

$$\sqrt{2\pi} = \int_{-\infty}^{\infty} f(x)\,\mathrm{d}x + \int_{\infty+i\sqrt{\pi}}^{-\infty+i\sqrt{\pi}} f(z)\,\mathrm{d}z = \int_{-\infty}^{\infty} f(x)\,\mathrm{d}x - \int_{-\infty}^{\infty} f(x+i\sqrt{\pi})\,\mathrm{d}x.$$

In the second integral, write $i\sqrt{\pi}$ as $\tau - \pi$ and use (real) translation invariance of $\mathrm{d}x$ to obtain

$$\sqrt{2\pi} = \int_{-\infty}^{\infty} f(x)\,\mathrm{d}x - \int_{-\infty}^{\infty} f(x+\tau)\,\mathrm{d}x = \int_{-\infty}^{\infty} (f(x) - f(x+\tau))\,\mathrm{d}x = \int_{-\infty}^{\infty} e^{-x^2/2}\,\mathrm{d}x \quad \text{by (10.2)}.$$

## 11. Eleventh Proof: Fourier Transforms

For a continuous function $f: \mathbf{R} \to \mathbf{C}$ that is rapidly decreasing at $\pm\infty$, its Fourier transform is the function $\mathcal{F}f: \mathbf{R} \to \mathbf{C}$ defined by

$$(\mathcal{F}f)(y) = \int_{-\infty}^{\infty} f(x)e^{-ixy}\,\mathrm{d}x. \tag{11.1}$$

For example, $(\mathcal{F}f)(0) = \int_{-\infty}^{\infty} f(x)\,\mathrm{d}x$. Here are three properties of the Fourier transform.

<!-- page 11 -->

- If $f$ is differentiable, then after using differentiation under the integral sign on the Fourier transform of $f$ we obtain

$$(\mathcal{F}f)'(y) = \int_{-\infty}^{\infty} -ixf(x)e^{-ixy}\,\mathrm{d}x = -i(\mathcal{F}(xf(x)))(y).$$

- Using integration by parts on the Fourier transform of $f$, with $u = f(x)$ and $\mathrm{d}v = e^{-ixy}\,\mathrm{d}x$, we obtain

$$(\mathcal{F}(f'))(y) = iy(\mathcal{F}f)(y).$$

- If we apply the Fourier transform twice then we recover the original function up to interior and exterior scaling:

$$(\mathcal{F}^2 f)(x) = 2\pi f(-x). \tag{11.2}$$

The $2\pi$ is admittedly a nonobvious scaling factor here, and the proof of (11.2) is nontrivial. We'll show the appearance of $2\pi$ in (11.2) is equivalent to the evaluation of $I$ as $\sqrt{2\pi}$.

Fixing $a > 0$, set $f(x) = e^{-ax^2}$, so

$$f'(x) = -2axf(x).$$

Applying the Fourier transform to both sides of this equation implies $iy(\mathcal{F}f)(y) = -2a\frac{1}{-i}(\mathcal{F}f)'(y)$, which simplifies to $(\mathcal{F}f)'(y) = -\frac{1}{2a}y(\mathcal{F}f)(y)$. The general solution of $g'(y) = -\frac{1}{2a}yg(y)$ is $g(y) = Ce^{-y^2/(4a)}$, so

$$f(x) = e^{-ax^2} \implies (\mathcal{F}f)(y) = Ce^{-y^2/(4a)}$$

for some constant $C$. We have $1/(4a) = a$ when $a = 1/2$, so set $a = 1/2$: if $f(x) = e^{-x^2/2}$ then

$$(\mathcal{F}f)(y) = Ce^{-y^2/2} = Cf(y). \tag{11.3}$$

Setting $y = 0$ in (11.3), the left side is $(\mathcal{F}f)(0) = \int_{-\infty}^{\infty} e^{-x^2/2}\,\mathrm{d}x = I$, so $I = Cf(0) = C$.

Applying the Fourier transform to both sides of (11.3) with $C = I$ and using (11.2), we get $2\pi f(-x) = I(\mathcal{F}f)(x) = I^2 f(x)$. At $x = 0$ this becomes $2\pi = I^2$, so $I = \sqrt{2\pi}$ since $I > 0$. That is the Gaussian integral calculation. If we didn't know that the constant on the right side of (11.2) is $2\pi$, whatever its value is would wind up being $I^2$, so saying $2\pi$ appears on the right side of (11.2) is equivalent to saying $I = \sqrt{2\pi}$.

There are other ways to define the Fourier transform besides (11.1), such as

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x)e^{-ixy}\,\mathrm{d}x \quad \text{or} \quad \int_{-\infty}^{\infty} f(x)e^{-2\pi ixy}\,\mathrm{d}x.$$

These transforms have properties similar to the transform as defined in (11.1), so they can be used in its place to compute the Gaussian integral. Let's see how such a proof looks using the second alternative definition, which we'll write as

$$(\widetilde{\mathcal{F}}f)(y) = \int_{-\infty}^{\infty} f(x)e^{-2\pi ixy}\,\mathrm{d}x.$$

For this Fourier transform, the analogue of the three properties above for $\mathcal{F}$ are

- $(\widetilde{\mathcal{F}}f)'(y) = -2\pi i(\widetilde{\mathcal{F}}(xf(x)))(y)$.
- $(\widetilde{\mathcal{F}}(f'))(y) = 2\pi iy(\widetilde{\mathcal{F}}f)(y)$.
- $(\widetilde{\mathcal{F}}^2 f)(x) = f(-x)$.

<!-- page 12 -->

The last property for $\widetilde{\mathcal{F}}$ looks nicer than that for $\mathcal{F}$, since there is no overall $2\pi$-factor on the right side (it has been hidden in the definition of $\widetilde{\mathcal{F}}$). On the other hand, the first two properties for $\widetilde{\mathcal{F}}$ have overall factors of $2\pi$ on the right side while the first two properties of $\mathcal{F}$ do not. You can't escape a role for $\pi$ or $2\pi$ somewhere in every possible definition of a Fourier transform.

Now let's run through the proof again with $\widetilde{\mathcal{F}}$ in place of $\mathcal{F}$. For $a > 0$, set $f(x) = e^{-ax^2}$. Applying $\widetilde{\mathcal{F}}$ to both sides of the equation $f'(x) = -2axf(x)$, $2\pi iy(\widetilde{\mathcal{F}}f)(y) = -2a\frac{1}{-(2\pi i)}(\mathcal{F}f)'(y)$, and that is equivalent to $(\widetilde{\mathcal{F}}f)'(y) = -\frac{2\pi^2}{a}y(\mathcal{F}f)(y)$. Solutions of $g'(y) = -\frac{2\pi^2}{a}yg(y)$ all look like $Ce^{-(\pi^2/a)y^2}$, so

$$f(x) = e^{-ax^2} \implies (\widetilde{\mathcal{F}}f)(y) = Ce^{-(\pi^2/a)y^2}$$

for a constant $C$. We want $\pi^2/a = \pi$ so that $e^{-(\pi^2/a)y^2} = e^{-\pi y^2} = f(y)$, which occurs for $a = \pi$. Thus when $f(x) = e^{-\pi x^2}$ we have

$$(\widetilde{\mathcal{F}}f)(y) = Ce^{-\pi y^2} = Cf(y). \tag{11.4}$$

When $y = 0$ in (11.4), this becomes $\int_{-\infty}^{\infty} e^{-\pi x^2}\,\mathrm{d}x = C$, so $C = K$: see the top of the first page for the definition of $K$ as the integral of $e^{-\pi x^2}$ over $\mathbf{R}$.

Applying $\widetilde{\mathcal{F}}$ to both sides of (11.4) with $C = K$ and using $(\widetilde{\mathcal{F}}^2 f)(x) = f(-x)$, we get $f(-x) = K(\widetilde{\mathcal{F}}f)(x) = K^2 f(x)$. At $x = 0$ this becomes $1 = K^2$, so $K = 1$ since $K > 0$. That $K = 1$, or in more explicit form $\int_{-\infty}^{\infty} e^{-\pi x^2}\,\mathrm{d}x = 1$, is equivalent to the evaluation of the Gaussian integral $I$ with the change of variables $y = \sqrt{2\pi}x$ in the integral for $K$.

## 12. History of the Gaussian Integral

The function $e^{-x^2/2}$, more commonly written as $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ ("normal distribution") so it has total integral $1$ over $\mathbf{R}$, plays an essential role in probability and statistics, and it was in such settings that this function was initially found. Three separate investigations led to it.

1. **Large sample approximation to binomial**: De Moivre [1, pp. 235-237] in 1733 found that a large number of samples from a binomial distribution with $p = 1/2$ can be approximated by a normal distribution. He did not write the Gaussian integral directly, but in [1, Cor. 2, p. 237] he estimated that the probability a binomial random variable with $p = 1/2$ is within a standard deviation of the mean from above is $.341344$. This is $\frac{1}{\sqrt{2\pi}}\int_0^1 e^{-x^2/2}\,\mathrm{d}x$. Such a role for the normal distribution did not make it stand out. De Moivre's work was generalized by Laplace in 1812 to binomial distributions with any $p$ in $(0,1)$. The normal approximation to the binomial for large sample sizes is a mainstay in probability and statistics courses.

2. **Distribution of Errors**: Gauss in 1809 (based on work starting in 1801) was led to $\frac{a}{\sqrt{\pi}}e^{-a^2x^2}$ in his astronomical work on locating the lost asteroid Ceres by the method of least squares. (At $a = 1/\sqrt{2}$ this is $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$.) To Gauss, such a function for suitable $a$ describes the distribution of errors in measurements: it is "the error curve". The difficulty in finding such a curve to model errors is hard to appreciate today, when the answer is known. In the 1770s, for example, Laplace proposed other error curves with corners or asymptotes at $x = 0$, as in Figure 4 below. In the second picture, $a$ is the largest imagined error.

3. **Central Limit Theorem**: Laplace, in his 1812 book *Theorie analytique des probabilites* [8], developed the first version of the Central Limit Theorem, which assigns a special role to the normal distribution.

The discovery of normally distributed data in the social sciences by Quetelet and others in the mid-19th century along with more general versions of the Central Limit Theorem solidified its role from then on. See [18] for more details. In that era, it was called the "Law of Error" or "the Error Curve". The name Central Limit Theorem is due to George Polya in 1920,[^2] and the widespread use of the name "normal distribution" is due to Karl Pearson.[^3]

[^2]: See https://mathoverflow.net/questions/44132.
[^3]: See https://mathshistory.st-andrews.ac.uk/Miller/mathword/n/.

<!-- page 13 -->

<!-- Figure 4: Laplace's error curves: (m/2)e^{-m|x|} in 1774 and (1/(2a))log(a/|x|) when |x| <= a in 1777. -->

## Appendix A. Redoing Section 2 Without Improper Integrals in Fubini's Theorem

In this appendix we will work out the calculation of the Gaussian integral in Section 2 without relying on Fubini's theorem for improper integrals. The key equation is (2.1), which we recall:

$$\int_0^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \int_0^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}y\right)\mathrm{d}t.$$

The calculation in Section 2 that the iterated integral on the right is $\pi/4$ does not need Fubini's theorem in any form. It is going from the iterated integral on the left to $\pi/4$ that used Fubini's theorem for improper integrals. The next theorem could be used as a substitute, and its proof will only use Fubini's theorem for integrals on rectangles.

**Theorem A.1.** *For $b > 1$ and $c > 1$,*

$$\int_0^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \frac{\pi}{4} + O\left(\frac{1}{b}\right) + O\left(\frac{1}{\sqrt{c}}\right).$$

Having $b \to \infty$ and $c \to \infty$ in Theorem A.1 makes the right side $\pi/4$ without changing the left side.

**Lemma A.2.**
1. *For all $x \in \mathbf{R}$, $e^{-x^2} \leq \frac{1}{x^2+1}$.*
2. *For $a > 0$, $\int_0^{\infty} \frac{\mathrm{d}x}{a^2x^2+1} = \frac{\pi}{2a}$.*
3. *For $a > 0$ and $c > 0$, $\int_c^{\infty} \frac{\mathrm{d}x}{a^2x^2+1} = \frac{1}{a}\left(\frac{\pi}{2} - \arctan(ac)\right)$.*
4. *For $a > 0$ and $c > 0$, $\int_c^{\infty} \frac{\mathrm{d}x}{a^2x^2+1} < \frac{1}{a^2c}$.*
5. *For $a > 0$, $\frac{\pi}{2} - \arctan a < \frac{1}{a}$.*

*Proof.* The proofs of (1), (2), and (3) are left to the reader. To prove (4), replace $1 + a^2t^2$ by the smaller value $a^2t^2$. To prove (5), write the difference as $\int_a^{\infty} \mathrm{d}x/(x^2+1)$ and then bound $1/(x^2+1)$ above by $1/x^2$. $\square$

<!-- page 14 -->

Now we prove Theorem A.1.

*Proof.* **Step 1.** For $b > 1$ and $c > 1$, we'll show the improper integral can be truncated to an integral over $[0,b] \times [0,c]$ plus error terms:

$$\int_0^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \int_0^b\left(\int_0^c ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y + O\left(\frac{1}{\sqrt{c}}\right) + O\left(\frac{1}{b}\right).$$

Subtract the integral on the right from the integral on the left and split the outer integral $\int_0^{\infty}$ into $\int_0^b + \int_b^{\infty}$:

$$\int_0^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y - \int_0^b\left(\int_0^c ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \int_0^b\left(\int_c^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y + \int_b^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y.$$

On the right side, we will show the **first iterated integral** is $O(1/\sqrt{c})$ and the **second iterated integral** is $O(1/b)$. The second iterated integral is simpler:

$$\int_b^{\infty}\left(\int_0^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \int_b^{\infty}\left(\int_0^{\infty} e^{-(yt)^2}\,\mathrm{d}t\right)ye^{-y^2}\,\mathrm{d}y \leq \int_b^{\infty}\left(\int_0^{\infty} \frac{\mathrm{d}t}{y^2t^2+1}\right)ye^{-y^2}\,\mathrm{d}y \quad \text{by Lemma A.2(1)} = \int_b^{\infty} \frac{\pi}{2y}ye^{-y^2}\,\mathrm{d}y \quad \text{by Lemma A.2(2)} = \frac{\pi}{2}\int_b^{\infty} e^{-y^2}\,\mathrm{d}y \leq \frac{\pi}{2}\int_b^{\infty} \frac{\mathrm{d}y}{y^2+1} \quad \text{by Lemma A.2(1)} = \frac{\pi}{2b} \quad \text{since } \frac{1}{y^2+1} < \frac{1}{y^2},$$

and this is $O(1/b)$. Returning to the first iterated integral,

$$\int_0^b\left(\int_c^{\infty} ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \int_0^b\left(\int_c^{\infty} e^{-(yt)^2}\,\mathrm{d}t\right)ye^{-y^2}\,\mathrm{d}y \leq \int_0^b\left(\int_c^{\infty} \frac{\mathrm{d}t}{y^2t^2+1}\right)ye^{-y^2}\,\mathrm{d}y \quad \text{by Lemma A.2(1)} = \int_0^1\left(\int_c^{\infty} \frac{\mathrm{d}t}{y^2t^2+1}\right)ye^{-y^2}\,\mathrm{d}y + \int_1^b\left(\int_c^{\infty} \frac{\mathrm{d}t}{y^2t^2+1}\right)ye^{-y^2}\,\mathrm{d}y \leq \int_0^1\left(\int_c^{\infty} \frac{\mathrm{d}t}{y^2t^2+1}\right)ye^{-y^2}\,\mathrm{d}y + \int_1^b \frac{1}{y^2c}ye^{-y^2}\,\mathrm{d}y \quad \text{by Lemma A.2(4)} = \int_0^1\left(\frac{\pi}{2} - \arctan(yc)\right)e^{-y^2}\,\mathrm{d}y + \frac{1}{c}\int_1^b \frac{\mathrm{d}y}{ye^{y^2}} \quad \text{by Lemma A.2(3)} \leq \int_0^1\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y + \frac{1}{c}\int_1^{\infty} \frac{\mathrm{d}y}{ye^{y^2}}.$$

<!-- page 15 -->

The last term is $O(1/c)$. We will show the first term is $O(1/\sqrt{c})$ by carefully splitting up $\int_0^1$.

For $0 < \varepsilon < 1$,

$$\int_0^1\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y = \int_0^{\varepsilon}\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y + \int_{\varepsilon}^1\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y.$$

Both integrals are positive, and the first one is less than $(\pi/2)\varepsilon$. The integrand of the second integral is less than $1/(yc)$ by Lemma A.2(5), so

$$\int_{\varepsilon}^1\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y < \int_{\varepsilon}^1 \frac{\mathrm{d}y}{yc} < \frac{1-\varepsilon}{\varepsilon c} < \frac{1}{\varepsilon c}.$$

Therefore

$$0 < \int_0^1\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y < \frac{\pi}{2}\varepsilon + \frac{1}{\varepsilon c}$$

for each $\varepsilon$ in $(0,1)$. Use $\varepsilon = 1/\sqrt{c}$ to get

$$0 < \int_0^1\left(\frac{\pi}{2} - \arctan(yc)\right)\mathrm{d}y < \frac{\pi}{2\sqrt{c}} + \frac{1}{\sqrt{c}} = O\left(\frac{1}{\sqrt{c}}\right).$$

That proves the **first iterated integral** is $O(1/\sqrt{c}) + O(1/c) = O(1/\sqrt{c})$ as $c \to \infty$.

**Step 2.** For $b > 0$ and $c > 0$, we will show

$$\int_0^b\left(\int_0^c ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \frac{\pi}{4} + O\left(\frac{1}{e^{b^2}}\right) + O\left(\frac{1}{c}\right).$$

By Fubini's theorem for continuous functions on a *rectangle* in $\mathbf{R}^2$,

$$\int_0^b\left(\int_0^c ye^{-(t^2+1)y^2}\,\mathrm{d}t\right)\mathrm{d}y = \int_0^c\left(\int_0^b ye^{-(t^2+1)y^2}\,\mathrm{d}y\right)\mathrm{d}t.$$

For the inner integral on the right, the formula $\int_0^b ye^{-ay^2}\,\mathrm{d}y = 1/(2a) - 1/(2ae^{ab^2})$ for $a > 0$ tells us

$$\int_0^b ye^{-(t^2+1)y^2}\,\mathrm{d}y = \frac{1}{2(t^2+1)} - \frac{1}{2(t^2+1)e^{(t^2+1)b^2}},$$

so

$$\int_0^c\left(\int_0^b ye^{-(t^2+1)y^2}\,\mathrm{d}y\right)\mathrm{d}t = \frac{1}{2}\int_0^c \frac{\mathrm{d}t}{t^2+1} - \frac{1}{2}\int_0^c \frac{\mathrm{d}t}{(t^2+1)e^{(t^2+1)b^2}} = \frac{1}{2}\arctan(c) - \frac{1}{2}\int_0^c \frac{\mathrm{d}t}{(t^2+1)e^{(t^2+1)b^2}}. \tag{A.1}$$

Let's estimate these last two terms. Since

$$\arctan(c) = \int_0^{\infty}\frac{\mathrm{d}t}{t^2+1} - \int_c^{\infty}\frac{\mathrm{d}t}{t^2+1} = \frac{\pi}{2} + O\left(\int_c^{\infty}\frac{\mathrm{d}t}{t^2}\right) = \frac{\pi}{2} + O\left(\frac{1}{c}\right)$$

and

$$\int_0^c \frac{\mathrm{d}t}{(t^2+1)e^{(t^2+1)b^2}} \leq \int_0^c \frac{\mathrm{d}t}{t^2+1}\frac{1}{e^{b^2}} \leq \int_0^{\infty}\frac{\mathrm{d}t}{t^2+1}\frac{1}{e^{b^2}} = O\left(\frac{1}{e^{b^2}}\right),$$

feeding these error estimates into (A.1) finishes Step 2. $\square$

<!-- page 16 -->

## References

[1] A. De Moivre, *The Doctrine of Chances*, 2nd ed., Woodfall, London, 1738. https://archive.org/details/bim_eighteenth-century_the-doctrine-of-chances_moivre-abraham-de_1738.

[2] D. Bell, "Poisson's remarkable calculation -- a method or a trick?" *Elem. Math.* **65** (2010), 29--36.

[3] C. A. Berenstein and R. Gay, *Complex Variables*, Springer-Verlag, New York, 1991.

[4] A. L. Delgado, "A Calculation of $\int_0^{\infty} e^{-x^2}\,\mathrm{d}x$," The College Math. J. **34** (2003), 321--323.

[5] H. Iwasawa, "Gaussian Integral Puzzle," Math. Intelligencer **31** (2009), 38--41.

[6] T. P. Jameson, "The Probability Integral by Volume of Revolution," Mathematical Gazette **78** (1994), 339--340.

[7] H. Kneser, *Funktionentheorie*, Vandenhoeck and Ruprecht, 1958.

[8] P. S. Laplace, *Theorie Analytique des Probabilites*, Courcier, 1812.

[9] P. S. Laplace, "Memoire sur la probabilite des causes par les evenements," Oeuvres Completes **8**, 27--65. (English trans. by S. Stigler as "Memoir on the Probability of Causes of Events," Statistical Science **1** (1986), 364--378.)

[10] P. M. Lee, http://www.york.ac.uk/depts/maths/histstat/normal_history.pdf.

[11] L. Mirsky, *The Probability Integral*, Math. Gazette **33** (1949), 279. URL http://www.jstor.org/stable/3611303.

[12] C. P. Nicholas and R. C. Yates, "The Probability Integral," Amer. Math. Monthly **57** (1950), 412--413.

[13] G. Polya, "Remarks on Computing the Probability Integral in One and Two Dimensions," pp. 63--78 in *Berkeley Symp. on Math. Statist. and Prob.*, Univ. California Press, 1949.

[14] R. Remmert, *Theory of Complex Functions*, Springer-Verlag, 1991.

[15] M. Rozman, "Evaluate Gaussian integral using differentiation under the integral sign," Course notes for Physics 2400 (UConn), Spring 2016.

[16] W. Rudin, *Principles of Mathematical Analysis*, 3rd ed., McGraw-Hill, 1976.

[17] M. Spivak, *Calculus*, W. A. Benjamin, 1967.

[18] S. Stahl, "The Evolution of the Normal Distribution," Math. Mag. **79** (2006), 96--113. URL https://www.jstor.org/stable/27642916.

[19] S. Stigler, "Laplace's 1774 Memoir on Inverse Probability," Statistical Science **1** (1986), 359--363.

[20] J. van Yzeren, "Moivre's and Fresnel's Integrals by Simple Integration," Amer. Math. Monthly **86** (1979), 690--693.

[21] G. N. Watson, *Complex Integration and Cauchy's Theorem*, Cambridge Univ. Press, Cambridge, 1914.

[22] http://gowers.wordpress.com/2007/10/04/when-are-two-proofs-essentially-the-same/#comment-239.

[23] http://math.stackexchange.com/questions/34767/int-infty-infty-e-x2-dx-with-complex-analysis.

[24] http://math.stackexchange.com/questions/390850/integrating-int-infty-0-e-x2-dx-using-feynmans-parametrization-trick.
