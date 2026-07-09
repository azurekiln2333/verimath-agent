# Characters of Finite Abelian Groups

> Source: https://kconrad.math.uconn.edu/blurbs/grouptheory/charthy.pdf
> Author: Keith Conrad
> Topic: group_theory

<!-- page 1 -->

## 1. Introduction

The theme we will study is an analogue on finite abelian groups of Fourier analysis on $\mathbf{R}$. A Fourier series on the real line is the following type of series in sines and cosines:
$$f(x) = \sum_{n \geq 0} a_n \cos(nx) + \sum_{n \geq 1} b_n \sin(nx).$$
This is $2\pi$-periodic. Since $e^{inx} = \cos(nx) + i\sin(nx)$ and $e^{-inx} = \cos(nx) - i\sin(nx)$, a Fourier series can also be written in terms of complex exponentials:
$$f(x) = \sum_{n \in \mathbf{Z}} c_n e^{inx},$$
where the summation runs over all integers ($c_0 = a_0$, $c_n = \frac{1}{2}(a_n - b_n i)$ for $n > 0$, and $c_n = \frac{1}{2}(a_{|n|} + b_{|n|} i)$ for $n < 0$). The convenient algebraic property of $e^{inx}$, which is not shared by sines and cosines, is that it is a group homomorphism from $\mathbf{R}$ to the unit circle $S^1 = \{z \in \mathbf{C}: |z| = 1\}$:
$$e^{in(x+x')} = e^{inx} e^{inx'}.$$

We now replace the real line $\mathbf{R}$ with a finite abelian group. Here is the analogue of the functions $e^{inx}$.

**Definition 1.1.** A *character* of a finite abelian group $G$ is a homomorphism $\chi: G \to S^1$.

We will usually write abstract groups multiplicatively, so $\chi(g_1 g_2) = \chi(g_1)\chi(g_2)$ and $\chi(1) = 1$.

**Example 1.2.** The *trivial* character of $G$ is the homomorphism $\mathbf{1}_G$ defined by $\mathbf{1}_G(g) = 1$ for all $g \in G$.

**Example 1.3.** Let $G$ be cyclic of order 4 with generator $\gamma$. Since $\gamma^4 = 1$, a character $\chi$ of $G$ has $\chi(\gamma)^4 = 1$, so $\chi$ takes only four possible values at $\gamma$, namely $1$, $i$, $-1$, or $-i$. Once $\chi(\gamma)$ is known, the value of $\chi$ elsewhere is determined by multiplicativity: $\chi(\gamma^j) = \chi(\gamma)^j$. So we get four characters, whose values can be placed in a table. See Table 1.

| | $1$ | $\gamma$ | $\gamma^2$ | $\gamma^3$ |
|---|---|---|---|---|
| $\mathbf{1}_G$ | 1 | 1 | 1 | 1 |
| $\chi_1$ | 1 | $i$ | $-1$ | $-i$ |
| $\chi_2$ | 1 | $-1$ | 1 | $-1$ |
| $\chi_3$ | 1 | $-i$ | $-1$ | $i$ |

**Table 1.**

<!-- page 2 -->

When $G$ has size $n$ and $g \in G$, for each character $\chi$ of $G$ we have $\chi(g)^n = \chi(g^n) = \chi(1) = 1$, so the values of $\chi$ lie among the $n$th roots of unity in $S^1$. More precisely, the order of $\chi(g)$ divides the order of $g$ (which divides $|G|$).

Characters on finite abelian groups were first studied in number theory, which is a source of many interesting finite abelian groups. For instance, Dirichlet used characters of the group $(\mathbf{Z}/(m))^\times$ to prove that when $(a,m) = 1$ there are infinitely many primes $p \equiv a \bmod m$. The quadratic reciprocity law of elementary number theory is concerned with a deep property of a particular character, the Legendre symbol. Fourier series on finite abelian groups have applications in engineering: signal processing (the fast Fourier transform [1, Chap. 9]) and error-correcting codes [1, Chap. 11].

A context for appreciating this account of characters on finite abelian groups is in Section 2 on Fourier analysis on the real line. In Section 3 we will run through some properties of characters of a finite abelian group $G$ and introduce its dual groups. In particular, we will see that $G$ is isomorphic to its dual group, but not naturally, and $G$ is naturally isomorphic to its double-dual group (Pontryagin duality). Section 4 uses characters of $G$ to develop a finite analogue of Fourier series. In Section 6 we use characters of $(\mathbf{Z}/p\mathbf{Z})^\times$ to count solutions to a congruence mod $p$. In Section 5 we use characters to prove a structure theorem for finite abelian groups. In Section 7 we look at duality on group homomorphisms. Characters are used in Section 8 to factor the group determinant of a finite abelian group. In Section 9, we decompose linear $G$-actions into common eigenspaces indexed by characters of $G$.

Our notation is completely standard, but we make two remarks about it. For a complex-valued function $f(x)$, the complex-conjugate function is usually denoted $\overline{f}(x)$ instead of $\overline{f(x)}$ to stress that conjugation creates a new function. (We sometimes use the overline notation also to mean the reduction $\overline{g}$ into a quotient group.) For $n \geq 1$, we write $\mu_n$ for the group of $n$th roots of unity in the unit circle $S^1$. It is a cyclic group of size $n$.

Exercises.

1. Make a character table for $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$, with columns labeled by elements of the group and rows labeled by characters, as in Table 1.
2. Let $G$ be a finite nonabelian simple group. (Examples include $A_n$ for $n \geq 5$.) Show the only group homomorphism $\chi: G \to S^1$ is the trivial map.

## 2. Classical Fourier Analysis

This section serves as motivation for our later treatment of finite abelian groups, where there will be no convergence issues (just finite sums!), so we take a soft approach and sidestep analytic technicalities that a serious treatment of Fourier analysis on $\mathbf{R}$ demands.

Fourier analysis for periodic functions on $\mathbf{R}$ is based on the functions $e^{inx}$ for $n \in \mathbf{Z}$. Every "reasonably nice" function $f: \mathbf{R} \to \mathbf{C}$ of period $2\pi$ can be expanded into a series
$$f(x) = \sum_{n \in \mathbf{Z}} c_n e^{inx},$$
where the sum runs over $\mathbf{Z}$ and the $n$th Fourier coefficient $c_n$ can be recovered as an integral:
$$c_n = \frac{1}{2\pi} \int_0^{2\pi} f(x)e^{-inx}\, dx. \tag{2.1}$$
This formula for $c_n$ can be explained by replacing $f(x)$ in (2.1) by its Fourier series and integrating termwise (for "reasonably nice" functions this termwise integration is analytically justifiable), using the formula
$$\frac{1}{2\pi} \int_0^{2\pi} e^{imx}e^{-inx}\, dx = \begin{cases} 1, & \text{if } m = n, \ 0, & \text{if } m \neq n. \end{cases}$$
An important link between a function $f(x)$ and its Fourier coefficients $c_n$ is given by Parseval's formula
$$\sum_{n \in \mathbf{Z}} |c_n|^2 = \frac{1}{2\pi} \int_0^{2\pi} |f(x)|^2\, dx.$$

<!-- page 3 -->

Rather than working with functions $f: \mathbf{R} \to \mathbf{C}$ having period $2\pi$, formulas look cleaner using functions $f: \mathbf{R} \to \mathbf{C}$ having period 1. The basic exponentials become $e^{2\pi inx}$ and the Fourier series and coefficients for $f$ are
$$f(x) = \sum_{n \in \mathbf{Z}} c_n e^{2\pi inx}, \quad c_n = \int_0^1 f(x)e^{-2\pi inx}\, dx. \tag{2.2}$$
Parseval's formula becomes
$$\sum_{n \in \mathbf{Z}} |c_n|^2 = \int_0^1 |f(x)|^2\, dx. \tag{2.3}$$
Note $c_n$ in (2.2) is not the same as $c_n$ in (2.1).

In addition to Fourier series there are Fourier integrals. The *Fourier transform* of a function $f$ that decays rapidly at $\pm\infty$ is the function $\widehat{f}: \mathbf{R} \to \mathbf{C}$ defined by the integral formula
$$\widehat{f}(y) = \int_{\mathbf{R}} f(x)e^{-2\pi ixy}\, dx.$$
The analogue of the expansion (2.2) of a periodic function into a Fourier series is the Fourier inversion formula, which expresses $f$ in terms of its Fourier transform $\widehat{f}$:
$$f(x) = \int_{\mathbf{R}} \widehat{f}(y)e^{2\pi ixy}\, dy.$$
Define a Hermitian inner product of two functions $f_1$ and $f_2$ from $\mathbf{R}$ to $\mathbf{C}$ by the integral
$$\langle f_1, f_2 \rangle = \int_{\mathbf{R}} f_1(x)\overline{f_2}(x)\, dx \in \mathbf{C},$$
Plancherel's theorem compares the inner product of two functions and the inner product of their Fourier transforms:
$$\langle \widehat{f_1}, \widehat{f_2} \rangle = \langle f_1, f_2 \rangle. \tag{2.4}$$
In particular, when $f_1 = f_2 = f$ the result is
$$\int_{\mathbf{R}} |\widehat{f}(y)|^2\, dy = \int_{\mathbf{R}} |f(x)|^2\, dx,$$
which is called Parseval's formula since it is an analogue of (2.3).

The *convolution* of two functions $f_1$ and $f_2$ from $\mathbf{R}$ to $\mathbf{C}$ is a new function from $\mathbf{R}$ to $\mathbf{C}$ defined by
$$f_1 * f_2(x) = \int_{\mathbf{R}} f_1(t)f_2(x-t)\, dt$$
and the Fourier transform turns this convolution into pointwise multiplication:
$$\widehat{f_1 * f_2}(y) = \widehat{f_1}(y)\widehat{f_2}(y).$$

<!-- page 4 -->

**Example 2.1.** A Gaussian is a function of the form $ae^{-bx^2}$, where $b > 0$. For example, the Gaussian $(1/\sqrt{2\pi})e^{-(1/2)x^2}$ is important in probability theory. The Fourier transform of a Gaussian is another Gaussian and the convolution of two Gaussians is another Gaussian:
$$\int_{\mathbf{R}} ae^{-bx^2}e^{-2\pi ixy}\, dx = \sqrt{\frac{\pi}{b}}ae^{-\pi^2 y^2/b} \tag{2.5}$$
and
$$f_1(x) = e^{-b_1 x^2}, \quad f_2(x) = e^{-b_2 x^2} \implies (f_1 * f_2)(x) = \sqrt{\frac{\pi}{b_1 + b_2}}e^{-(b_1 b_2/(b_1+b_2))x^2}.$$
The formula (2.5) says that a highly peaked Gaussian (large $b$) has a Fourier transform that is a spread out Gaussian (small $\pi^2/b$) and *vice versa*. More generally, a function and its Fourier transform can't both be highly localized; this is a mathematical incarnation of Heisenberg's uncertainty principle from physics.[^1]


<!-- page 5 -->
When $b = \pi$, (2.5) tells us that $ae^{-\pi x^2}$ is its own Fourier transform. Functions equal to their Fourier transform are called *self-dual*, and $e^{-\pi x^2}$ is the simplest nonzero example.

A link between Fourier series and Fourier integrals is the *Poisson summation formula*: for a "nice" function $f: \mathbf{R} \to \mathbf{C}$ that decays rapidly enough at $\pm\infty$,
$$\sum_{n \in \mathbf{Z}} f(n) = \sum_{n \in \mathbf{Z}} \widehat{f}(n), \tag{2.6}$$
where $\widehat{f}(y) = \int_{\mathbf{R}} f(x)e^{-2\pi ixy}\, dx$. For example, when $f(x) = e^{-bx^2}$ (with $b > 0$), the Poisson summation formula says
$$\sum_{n \in \mathbf{Z}} e^{-bn^2} = \sum_{n \in \mathbf{Z}} \sqrt{\frac{\pi}{b}}e^{-\pi^2 n^2/b}.$$
To prove the Poisson summation formula, we use Fourier series. Periodize $f(x)$ as
$$F(x) = \sum_{n \in \mathbf{Z}} f(x+n).$$
Since $F(x+1) = F(x)$, write $F$ as a Fourier series: $F(x) = \sum_{n \in \mathbf{Z}} c_n e^{2\pi inx}$. Then
$$c_n = \int_0^1 F(x)e^{-2\pi inx}\, dx = \int_0^1 \left(\sum_{m \in \mathbf{Z}} f(x+m)
ight)e^{-2\pi inx}\, dx$$
$$= \sum_{m \in \mathbf{Z}} \int_0^1 f(x+m)e^{-2\pi inx}\, dx = \sum_{m \in \mathbf{Z}} \int_m^{m+1} f(x)e^{-2\pi inx}\, dx$$
$$= \int_{\mathbf{R}} f(x)e^{-2\pi inx}\, dx = \widehat{f}(n).$$
Therefore the expansion of $F(x)$ into a Fourier series is equivalent to
$$\sum_{n \in \mathbf{Z}} f(x+n) = \sum_{n \in \mathbf{Z}} \widehat{f}(n)e^{2\pi inx}, \tag{2.7}$$

<!-- page 6 -->
which becomes the Poisson summation formula (2.6) by setting $x = 0$.

If we replace a sum over $\mathbf{Z}$ with a sum over a one-dimensional lattice $L = a\mathbf{Z}$ in $\mathbf{R}$, where $a \neq 0$, the Poisson summation formula becomes
$$\sum_{\lambda \in L} f(\lambda) = \frac{1}{|a|}\sum_{\mu \in L^\perp} \widehat{f}(\mu),$$
where $L^\perp = (1/a)\mathbf{Z}$ is the "dual lattice":
$$L^\perp = \{\mu \in \mathbf{R}: e^{2\pi i\lambda\mu} = 1 \text{ for all } \lambda \in L\}.$$
For example, $\mathbf{Z}^\perp = \mathbf{Z}$.

There are several conventions for the definition of the Fourier transform as well as the inner product and convolution of functions. Tables 2 and 3 collect a number of different $2\pi$-conventions. The first two columns of Tables 2 and 3 are definitions and the other columns are theorems.

| $\widehat{f}(y)$ | $\langle f_1, f_2 \rangle$ | $f(x)$ | $\langle \widehat{f_1}, \widehat{f_2} \rangle$ |
|---|---|---|---|

<!-- page 7 -->
| $\int_{\mathbf{R}} f(x)e^{-2\pi ixy}\, dx$ | $\int_{\mathbf{R}} f_1(x)\overline{f_2}(x)\, dx$ | $\int_{\mathbf{R}} \widehat{f}(y)e^{2\pi ixy}\, dy$ | $\langle f_1, f_2 \rangle$ |
| $\int_{\mathbf{R}} f(x)e^{-ixy}\, dx$ | $\int_{\mathbf{R}} f_1(x)\overline{f_2}(x)\, dx$ | $\frac{1}{2\pi}\int_{\mathbf{R}} \widehat{f}(y)e^{ixy}\, dy$ | $2\pi\langle f_1, f_2 \rangle$ |
| $\frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} f(x)e^{-ixy}\, dx$ | $\frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} f_1(x)\overline{f_2}(x)\, dx$ | $\frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} \widehat{f}(y)e^{ixy}\, dy$ | $\langle f_1, f_2 \rangle$ |

**Table 2.**

| $\widehat{f}(y)$ | $(f_1 * f_2)(x)$ | $\widehat{f_1 * f_2}(y)$ |
|---|---|---|
| $\int_{\mathbf{R}} f(x)e^{-2\pi ixy}\, dx$ | $\int_{\mathbf{R}} f_1(y)f_2(x-y)\, dy$ | $\widehat{f_1}(y)\widehat{f_2}(y)$ |
| $\int_{\mathbf{R}} f(x)e^{-ixy}\, dx$ | $\int_{\mathbf{R}} f_1(y)f_2(x-y)\, dy$ | $\widehat{f_1}(y)\widehat{f_2}(y)$ |
| $\frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} f(x)e^{-ixy}\, dx$ | $\frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} f_1(t)f_2(x-t)\, dt$ | $\widehat{f_1}(y)\widehat{f_2}(y)$ |


<!-- page 8 -->
**Table 3.**

When the Fourier transform is defined using $\widehat{f}(y) = \frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} f(x)e^{-ixy}\, dx$, the function $e^{-\pi x^2}$ is no longer self-dual, but $e^{-(1/2)x^2}$ is self-dual. You need to know how the Fourier transform is defined to say that a particular function is self-dual.

Exercises.

1. Without dwelling on analytic subtleties, check from Fourier inversion that $\widehat{\widehat{f}}(x) = f(-x)$ (if the Fourier transform is defined suitably).
2. If $f$ is a real-valued even function, show its Fourier transform is also real-valued and even (assuming the Fourier transform of $f$ is meaningful).
3. For a function $f: \mathbf{R} \to \mathbf{C}$ and $c \in \mathbf{R}$, let $g(x) = f(x+c)$. Define the Fourier transform of a function $h$ by $\widehat{h}(y) = \int_{\mathbf{R}} h(x)e^{-2\pi ixy}\, dx$. If $f$ has a Fourier transform, show $g$ has Fourier transform $\widehat{g}(y) = e^{2\pi icy}\widehat{f}(y)$.
4. The Poisson summation formula over $\mathbf{R}$ was obtained by setting $x = 0$ in (2.7). Conversely, show that (2.7) for the function $f$ follows from the Poisson summation formula for the function $g(t) = f(t+x)$.

<!-- page 9 -->
5. Assuming the Fourier inversion formula holds for a definition of the Fourier transform as in Table 2, check that for all $\alpha$ and $\beta$ in $\mathbf{R}^\times$ that if we set
$$ (\mathcal{F}f)(y) = \alpha \int_{\mathbf{R}} f(x)e^{-ibeta xy}\, dx $$
for all $x$ then
$$ f(x) = \frac{\beta}{2\pialpha} \int_{\mathbf{R}} (\mathcal{F}f)(y)e^{ibeta xy}\, dy. $$
(If $\beta = 2\pialpha^2$ then these two equations are symmetric in the roles of $f$ and $\mathcal{F}f$ except for a sign in the exponential term.) Considering $\mathcal{F}f$ to be the Fourier transform of $f$, show $e^{-(1/2)\beta x^2}$ is self-dual.

Exercises.


## 3. Characters of Finite Abelian Groups

<!-- page 7 -->

For a finite abelian group $G$, a *character* of $G$ is a homomorphism $\chi: G \to S^1$, where $S^1 = \{z \in \mathbf{C}: |z| = 1\}$ is the unit circle in $\mathbf{C}$ under multiplication. Since $G$ is finite, $\chi(g)$ is a root of unity for each $g \in G$.

The set of characters of $G$ is denoted $\widehat{G}$. Under pointwise multiplication, $\widehat{G}$ is an abelian group: for $\chi_1, \chi_2 \in \widehat{G}$, define $(\chi_1\chi_2)(g) = \chi_1(g)\chi_2(g)$. The identity element is the trivial character $\mathbf{1}_G$ sending every $g \in G$ to 1, and the inverse of $\chi$ is $\overline{\chi}$, where $\overline{\chi}(g) = \overline{\chi(g)} = \chi(g)^{-1} = \chi(g^{-1})$.

**Theorem 3.1.** *For a finite abelian group $G$, the character group $\widehat{G}$ is a finite abelian group of order $|G|$.*

We will prove this theorem through a series of results. First, we show characters separate elements of $G$.

**Lemma 3.2.** *For each nontrivial $g \in G$, there is a character $\chi$ of $G$ such that $\chi(g) \neq  1$.*

*Proof.* The subgroup $\langle g \rangle$ is cyclic. If $g$ has order $m$, there is an isomorphism $\langle g \rangle \to \mu_m \subset S^1$ sending $g$ to $e^{2\pi i/m}$. This is a character of $\langle g \rangle$ that is nontrivial on $g$. We extend it to a character of $G$ using the next theorem. $\square$

**Theorem 3.3.** *Let $H$ be a subgroup of a finite abelian group $G$. Every character of $H$ extends to a character of $G$.*

*Proof.* We induct on $[G:H]$. If $[G:H] = 1$ there is nothing to prove. Assume $[G:H] > 1$ and pick $g \in G \setminus H$. Let $d \geq 1$ be minimal such that $g^d \in H$. Then $H' = \langle H, g \rangle = \{hg^j: h \in H, 0 \leq j < d\}$ and $[H':H] = d$.

Given a character $\chi$ on $H$, we extend it to $H'$ by choosing $\chi(g) = z \in S^1$ such that $z^d = \chi(g^d)$. Such a $z$ exists since every element of $S^1$ has a $d$th root in $S^1$. Then $\chi(hg^j) = \chi(h)z^j$ defines a character on $H'$ extending $\chi$. Since $[G:H'] < [G:H]$, by induction $\chi$ extends from $H'$ to $G$. $\square$

<!-- page 8 -->

**Theorem 3.4.** *For a finite abelian group $G$, $|\widehat{G}| = |G|$.*

*Proof.* By Lemma 3.2, for each nontrivial $g \in G$ there exists $\chi \in \widehat{G}$ with $\chi(g) \neq  1$. Consider the map $G \to \widehat{\widehat{G}}$ sending $g$ to the character "evaluate at $g$" on $\widehat{G}$. This map is injective by Lemma 3.2, so $|G| \leq |\widehat{\widehat{G}}|$.

We show $|\widehat{G}| \leq |G|$ by induction on $|G|$. When $|G| = 1$, $|\widehat{G}| = 1$. For $|G| > 1$, pick a nontrivial cyclic subgroup $C = \langle g \rangle$ of $G$. Every character of $G$ restricts to a character of $C$, and there are $|C|$ characters of $C$. For each character $\psi$ of $C$, the characters of $G$ restricting to $\psi$ are in bijection with the characters of $G$ that are trivial on $C$, i.e., characters of $G/C$. By induction $|\widehat{G/C}| = |G/C|$, so $|\widehat{G}| = |C| \cdot |G/C| = |G|$. $\square$

Combined with the injection $G \hookrightarrow \widehat{\widehat{G}}$, Theorem 3.4 gives $|G| \leq |\widehat{\widehat{G}}| = |\widehat{G}| = |G|$, so the map $G \to \widehat{\widehat{G}}$ is a bijection.

**Theorem 3.5** (Pontryagin duality). *For a finite abelian group $G$, the natural map $G \to \widehat{\widehat{G}}$ sending $g$ to "evaluate at $g$" is an isomorphism.*

<!-- page 9 -->

**Example 3.6.** The characters of $\mathbf{Z}/(m)$ are $\chi_k: j \mapsto e^{2\pi ijk/m}$ for $k = 0, 1, \ldots, m-1$. The character group $\widehat{\mathbf{Z}/(m)}$ is isomorphic to $\mathbf{Z}/(m)$ via $k \mapsto \chi_k$.

**Example 3.7.** For $G = \mathbf{Z}/(2) \times \mathbf{Z}/(2) = \{(0,0), (1,0), (0,1), (1,1)\}$, the characters are $\chi_{(a,b)}(x,y) = (-1)^{ax+by}$ for $(a,b) \in G$. The character table is:

| | $(0,0)$ | $(1,0)$ | $(0,1)$ | $(1,1)$ |
|---|---|---|---|---|
| $\chi_{(0,0)}$ | 1 | 1 | 1 | 1 |
| $\chi_{(1,0)}$ | 1 | $-1$ | 1 | $-1$ |
| $\chi_{(0,1)}$ | 1 | 1 | $-1$ | $-1$ |
| $\chi_{(1,1)}$ | 1 | $-1$ | $-1$ | 1 |

**Table 1.** Character table of $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$

<!-- page 10 -->

**Theorem 3.8.** *Let $G$ be a finite abelian group and $H$ a subgroup. The characters of $G/H$ are in bijection with the characters of $G$ that are trivial on $H$.*

*Proof.* If $\psi$ is a character of $G/H$, then $\chi = \psi \circ \pi$ (where $\pi: G \to G/H$ is the projection) is a character of $G$ trivial on $H$. Conversely, if $\chi$ is a character of $G$ trivial on $H$, then $\chi$ factors through $G/H$ to give a character $\psi$ of $G/H$. These maps are inverse to each other. $\square$

**Theorem 3.9.** *For finite abelian groups $G_1$ and $G_2$, $\widehat{G_1 \times G_2} \cong \widehat{G_1} \times \widehat{G_2}$.*

*Proof.* A character of $G_1 \times G_2$ is determined by its restrictions to $G_1 \times \{1\}$ and $\{1\} \times G_2$, giving the isomorphism. $\square$

**Theorem 3.10.** *For a cyclic group $G = \langle g \rangle$ of order $n$, $\widehat{G} \cong G$.*

*Proof.* The characters are $\chi_k: g^j \mapsto e^{2\pi ijk/n}$ for $k = 0, 1, \ldots, n-1$, and $\chi_k \chi_l = \chi_{k+l \bmod n}$. $\square$

**Theorem 3.11.** *For $G = \mathbf{Z}/(m)$, $\widehat{G} \cong \mathbf{Z}/(m)$.*

*Proof.* This follows from Theorem 3.10 since $\mathbf{Z}/(m)$ is cyclic of order $m$. $\square$

<!-- page 11 -->

**Theorem 3.12.** *For a finite abelian group $G \cong \mathbf{Z}/(n_1) \times \cdots \times \mathbf{Z}/(n_k)$, we have $\widehat{G} \cong G$.*

*Proof.* By Theorems 3.9 and 3.10, $\widehat{G} \cong \widehat{\mathbf{Z}/(n_1)} \times \cdots \times \widehat{\mathbf{Z}/(n_k)} \cong \mathbf{Z}/(n_1) \times \cdots \times \mathbf{Z}/(n_k) = G$. $\square$

**Theorem 3.13.** *For every finite abelian group $G$, $G \cong \widehat{G}$.*

*Proof.* This follows from Theorem 3.12 and the structure theorem for finite abelian groups (Theorem 5.2, proved later using characters). $\square$

**Theorem 3.14.** *Let $G$ be a finite abelian group. The characters of $G$ separate points: if $g_1 \neq g_2$ in $G$, there exists $\chi \in \widehat{G}$ with $\chi(g_1) \neq \chi(g_2)$.*

*Proof.* Apply Lemma 3.2 to $g_1 g_2^{-1} \neq 1$. $\square$

**Theorem 3.15.** *For a finite abelian group $G$, the characters of $G$ form a basis for the space $L(G)$ of complex-valued functions on $G$.*

*Proof.* Since $|\widehat{G}| = |G| = \dim L(G)$, it suffices to show the characters are linearly independent. Suppose $\sum_\chi c_\chi \chi = 0$. Evaluating at each $g \in G$ and using Theorem 4.1 (orthogonality), we get $c_\chi = 0$ for all $\chi$. $\square$

Exercises.

1. Let's find the characters of the additive group $(\mathbf{Z}/(m))^r$, an $r$-fold direct product.
   (a) For $k \in \mathbf{Z}/(m)$, let $\chi_k: \mathbf{Z}/(m) \to S^1$ by

<!-- page 10 -->
   $$\chi_k(j) = e^{2\pi ijk/m},$$
   so $\chi_k(1) = e^{2\pi ik/m}$. Show $\chi_0, \chi_1, \ldots, \chi_{m-1}$ are all the characters of $\mathbf{Z}/(m)$ and $\chi_k\chi_l = \chi_{k+l}$.
   (b) Let $r \geq 1$. For $r$-tuples $\mathbf{a}, \mathbf{b}$ in $(\mathbf{Z}/(m))^r$, let
   $$\mathbf{a} \cdot \mathbf{b} = a_1b_1 + \cdots + a_rb_r \in \mathbf{Z}/(m)$$
   be the usual dot product. For $\mathbf{k} \in (\mathbf{Z}/(m))^r$, let $\chi_{\mathbf{k}}(\mathbf{j}) = e^{2\pi i(\mathbf{j}\cdot\mathbf{k})/m}$. Show the functions $\chi_{\mathbf{k}}$ are all the characters of $(\mathbf{Z}/(m))^r$ and $\chi_{\mathbf{k}}\chi_{\mathbf{l}} = \chi_{\mathbf{k}+\mathbf{l}}$.
2. Show the following are equivalent properties of a character $\chi$: $\chi(g) = \pm 1$ for all $g$, $\overline{\chi}(g) = \chi(g)$ for all $g$, and $\chi^2 = \mathbf{1}_G$.
3. Describe the error in the following bogus proof of Theorem 3.4. Let $m = [G:H]$ and pick a set of coset representatives $g_1, \ldots, g_m$ for $G/H$. Given a character $\chi$ on $H$, define $\widetilde{\chi}$ on $G$ by first picking the $m$ ($= [G:H]$) values $\widetilde{\chi}(g_i)$ for $1 \leq i \leq m$ and then writing each $g \in G$ in the (unique) form $g_ih$ and defining $\widetilde{\chi}(g) = \widetilde{\chi}(g_i)\chi(h)$. This defines $\widetilde{\chi}$ on $G$, and since we had to make $m$ choices there are $m$ characters.
4. Let $G$ be a finite abelian group of order $n$ and $g \in G$ have order $m$. Show
$$\prod_{\chi \in \widehat{G}}(1 - \chi(g)T) = (1 - T^m)^{n/m}.$$
5. For finite nonabelian $G$, show the characters of $G$ (that is, homomorphisms $G \to S^1$) separate elements modulo $[G,G]$: $\chi(g_1) = \chi(g_2)$ for all $\chi$ if and only if $g_1 = g_2$ in $G/[G,G]$.
6. This exercise will give an interpretation of characters as eigenvectors. For a finite abelian group $G$ and $g \in G$, let $T_g: L(G) \to L(G)$ by $(T_gf)(x) = f(gx)$.
   (a) Show the $T_g$'s are commuting linear transformations and each character of $G$ is an eigenvector of each $T_g$.
   (b) If $f$ is a simultaneous eigenvector of all the $T_g$'s, show $f(1) 

<!-- page 11 -->\neq 0$ (if $f(1) = 0$ conclude $f$ is identically zero, but the zero vector is not an eigenvector) and then after rescaling $f$ so $f(1) = 1$ deduce that $f$ is a character of $G$. Thus the characters of $G$ are the simultaneous eigenvectors of the $T_g$'s, suitably normalized.
   (c) Show the $T_g$'s are each diagonalizable. Deduce from this and parts (a) and (b) that $\widehat{G}$ is a basis of $L(G)$, so $|\widehat{G}| = \dim L(G) = |G|$. (This gives a different proof that $G$ and $\widehat{G}$ have the same size.)
7. For a subgroup $H$ of a finite abelian group $G$, let
$$H^\perp = \{\chi \in \widehat{G}: \chi = 1 \text{ on } H\}.$$
These are the characters of $G$ that are trivial on $H$. For example, $G^\perp = \{\mathbf{1}_G\}$ and $\{1\}^\perp = \widehat{G}$. Note $H^\perp \subset \widehat{G}$ and $H^\perp$ depends on $H$ and $G$.
Show $H^\perp$ is a subgroup of $\widehat{G}$, it is isomorphic to $\widehat{G/H}$, and $\widehat{G}/(H^\perp) \cong \widehat{H}$. In particular, $|H^\perp| = [G:H]$.
8. Let $G$ be finite abelian and $H \subset G$ be a subgroup.
   (a) Viewing $H^{\perp\perp} = (H^\perp)^\perp$ in $G$ using Pontryagin duality, show $H^{\perp\perp} = H$. (Hint: The inclusion in one direction is easy. Count sizes for the other inclusion.)
   (b) Show for each $m$ dividing $|G|$ that
   $$|\{H \subset G: |H| = m\}| = |\{H \subset G: [G:H] = m\}|$$
   by associating $H$ to $H^\perp$ and using a (fixed) isomorphism of $G$ with $\widehat{G}$.
   (c) For a finite abelian group $G$, part b says the number of subgroups of $G$ with index 2 is equal to the number of elements of $G$ with order 2. Use this idea to count the number of subgroups of $(\mathbf{Z}/(m))^\times$ with index 2. (The answer depends on the number of odd prime factors of $m$ and the highest power of 2 dividing $m$.)
   (d) Show, for a prime $p$, that the number of subspaces of $(\mathbf{Z}/(p))^n$ with dimension $d$ equals the number of subspaces with dimension $n-d$.
9. For a finite abelian group $G$, let $G[n] = \{g \in G: g^n = 1\}$ and $G^n = \{g^n: g \in G\}$. Both are subgroups of $G$. Prove $G[n]^\perp = (\widehat{G})^n$ and $(G^n)^\perp = \widehat{G}[n]$ in $\widehat{G}$.
## 4. Finite Fourier Series

<!-- page 12 -->

We will introduce the analogue of Fourier series on finite abelian groups.

Let $G$ be a finite abelian group. Set

$$L(G) = \{f: G \to \mathbf{C}\},$$

the $\mathbf{C}$-valued functions on $G$. This is a $\mathbf{C}$-vector space of functions. Every $f \in L(G)$ can be expressed as a linear combination of the delta-functions $\delta_g$ from (3.3):

(4.1)
$$f = \sum_{g \in G} f(g)\delta_g.$$

Indeed, evaluate both sides at each $x \in G$ and we get the same value. The functions $\delta_g$ span $L(G)$ by (4.1) and they are linearly independent: if $\sum_g a_g \delta_g = 0$ then evaluating the sum at $x \in G$ shows $a_x = 0$. Thus the functions $\delta_g$ are a basis of $L(G)$, so $\dim L(G) = |G|$.

The next theorem is the first step leading to an expression for each $\delta_g$ as a linear combination of characters of $G$, which will lead to a Fourier series expansion of $f$. It is the first time we *add* character values.

<!-- page 13 -->

**Theorem 4.1.** *Let $G$ be a finite abelian group. Then*

$$\sum_{g \in G} \chi(g) = \begin{cases} |G|, & \text{if } \chi = \mathbf{1}_G, \ 0, & \text{if } \chi \neq \mathbf{1}_G, \end{cases} \quad \sum_{\chi \in \widehat{G}} \chi(g) = \begin{cases} |G|, & \text{if } g = 1, \ 0, & \text{if } g \neq 1. \end{cases}$$

*Proof.* Let $S = \sum_{g \in G} \chi(g)$. If $\chi$ is trivial on $G$ then $S = |G|$. If $\chi$ is not trivial on $G$, say $\chi(g_0) \neq 1$. Then $\chi(g_0)S = \sum_{g \in G} \chi(gg_0) = \sum_{g \in G} \chi(g) = S$, so $S = 0$.

The second formula in the theorem can be viewed as an instance of the first formula via Pontryagin duality: the second sum is a sum of the character "evaluate at $g$" over the group $\widehat{G}$, and this character on $\widehat{G}$ is nontrivial when $g \neq 1$ by Pontryagin duality. $\square$

Theorem 4.1 says the sum of a nontrivial character over a group vanishes and the sum of all characters of a group evaluated at a nontrivial element vanishes, so the sum of the elements in each row and column of a character table of $G$ is zero except the row for the trivial character and the column for the identity element. Check this in Table 1.

**Corollary 4.2.** *For characters $\chi_1$ and $\chi_2$ in $\widehat{G}$ and $g_1$ and $g_2$ in $G$,*

$$\sum_{g \in G} \chi_1(g)\overline{\chi_2}(g) = \begin{cases} |G|, & \text{if } \chi_1 = \chi_2, \ 0, & \text{if } \chi_1 \neq \chi_2, \end{cases} \quad \sum_{\chi \in \widehat{G}} \chi(g_1)\overline{\chi}(g_2) = \begin{cases} |G|, & \text{if } g_1 = g_2, \ 0, & \text{if } g_1 \neq g_2. \end{cases}$$

*Proof.* In the first equation of Theorem 4.1 let $\chi = \chi_1\overline{\chi_2}$. In the second equation of Theorem 4.1 let $g = g_1 g_2^{-1}$. (Alternatively, after proving the first equation for all $G$ we observe that the second equation is a special case of the first by Pontryagin duality.) $\square$

The equations in Corollary 4.2 are called the *orthogonality relations*. They say that the character table of $G$ has orthogonal rows and orthogonal columns when we define orthogonality of two $n$-tuples of complex numbers as vanishing of their Hermitian inner product: in $\mathbf{C}^n$: $\langle (z_1, \ldots, z_n), (w_1, \ldots, w_n) \rangle := \sum_{k=1}^n z_k \overline{w_k}$.

**Example 4.3.** Let $G = (\mathbf{Z}/(m))^\times$. For $a \in (\mathbf{Z}/(m))^\times$ and $p$ a prime not dividing $m$,

$$\frac{1}{\varphi(m)} \sum_{\chi \bmod m} \overline{\chi}(a)\chi(p) = \begin{cases} 1, & \text{if } p \equiv a \bmod m, \ 0, & \text{if } p 
ot\equiv a \bmod m, \end{cases}$$

where the sum runs over the characters of $(\mathbf{Z}/(m))^\times$. (Since $p$ is prime, $p$ not dividing $m$ forces $p$ to be in $(\mathbf{Z}/(m))^\times$.) This identity was used by Dirichlet in his proof that there are infinitely many primes $p \equiv a \bmod m$.

By the second equation in Corollary 4.2 we can express the delta-functions in terms of characters:

$$\sum_{\chi \in \widehat{G}} \chi(g)\overline{\chi}(x) = |G|\delta_g(x) \implies \delta_g(x) = \frac{1}{|G|} \sum_{\chi \in \widehat{G}} \overline{\chi}(g)\chi(x).$$

<!-- page 14 -->

Substituting this formula for $\delta_g$ into (4.1) gives

$$f(x) = \sum_{g \in G} f(g)\left(\frac{1}{|G|} \sum_{\chi \in \widehat{G}} \overline{\chi}(g)\chi(x)
ight)$$
$$= \sum_{\chi \in \widehat{G}} \sum_{g \in G} \frac{1}{|G|} f(g)\overline{\chi}(g)\chi(x)$$
(4.2)
$$= \sum_{\chi \in \widehat{G}} c_\chi \chi(x),$$

where

(4.3)
$$c_\chi = \frac{1}{|G|} \sum_{g \in G} f(g)\overline{\chi}(g).$$

The expansion (4.2) is the Fourier series for $f$.

Equation (4.3) is similar to the formula for the coefficient $c_n$ of $e^{inx}$ in (2.1): an integral over $[0, 2\pi]$ divided by $2\pi$ is replaced by a sum over $G$ divided by $|G|$ and $f(x)e^{-inx}$ is replaced by $f(g)\overline{\chi}(g)$. The number $e^{-inx}$ is the conjugate of $e^{inx}$, which is also the relation between $\overline{\chi}(g)$ and $\chi(g)$. Equation (4.2) shows $\widehat{G}$ is a spanning set for $L(G)$. Since $|\widehat{G}| = |G| = \dim L(G)$, $\widehat{G}$ is a basis for $L(G)$.

**Definition 4.4.** If $f \in L(G)$ then its *Fourier transform* $\widehat{f} \in L(\widehat{G})$ is given by

$$\widehat{f}(\chi) = \sum_{g \in G} f(g)\overline{\chi}(g).$$

By (4.2) and (4.3),

(4.4)
$$f(x) = \frac{1}{|G|} \sum_{\chi \in \widehat{G}} \widehat{f}(\chi)\chi(x).$$

Equation (4.4), called the *Fourier inversion formula*, lets us recover $f$ from $\widehat{f}$.

**Remark 4.5.** Classically the Fourier transform of a function $\mathbf{R} \to \mathbf{C}$ is another function $\mathbf{R} \to \mathbf{C}$. The finite Fourier transform, however, is defined on the dual group instead of on the original group. We can also interpret the classical Fourier transform to be a function of characters. For $y \in \mathbf{R}$ let $\chi_y(x) = e^{ixy}$. Then $\chi_y: \mathbf{R} \to S^1$ is a character and $\widehat{f}(y)$ could be viewed as $\widehat{f}(\chi_y) = \int_{\mathbf{R}} f(x)\overline{\chi_y}(x)\,dx$, so $\widehat{f}$ is a function of characters rather than of numbers.

**Example 4.6.** Let $f = \delta_g$. Then $\widehat{f}(\chi) = \overline{\chi}(g) = \chi(g^{-1})$. Notice $f$ vanishes at all but one element of $G$ while $\widehat{f}$ is nonzero on all of $\widehat{G}$.

**Example 4.7.** Let $f = \psi$ be a character of $G$. Then $\widehat{f}(\chi) = \sum_g \psi(g)\overline{\chi}(g) = |G|\delta_\psi(\chi)$, so $\widehat{f} = |G|\delta_\psi$. Here $f$ is nonzero on all of $G$ and $\widehat{f}$ is nonzero at only one element of $\widehat{G}$.

The Fourier transform on $\mathbf{R}$ interchanges highly spread and highly peaked Gaussians. Examples 4.6 and 4.7 suggest a similar phenomenon in the finite case. The next theorem is a general result in that direction (a finite version of Heisenberg uncertainty). It is the only time (outside Appendix B) when we will use inequalities with characters of finite abelian groups.

<!-- page 15 -->

**Theorem 4.8.** *Let $f: G \to \mathbf{C}$ be a function on a finite abelian group $G$ that is not identically zero. Then*

(4.5)
$$|\operatorname{supp} f| \cdot |\operatorname{supp} \widehat{f}| \geq |G|,$$

*where $\operatorname{supp}$ denotes the support of a function (the set of points where the function is nonzero).*

*Proof.* We expand $f$ into a Fourier series and make estimates. Since

$$f(x) = \sum_{\chi \in \widehat{G}} \frac{1}{|G|} \widehat{f}(\chi)\chi(x),$$

we have

(4.6)
$$|f(x)| \leq \sum_{\chi \in \widehat{G}} \frac{1}{|G|} |\widehat{f}(\chi)| \leq \frac{|\operatorname{supp} \widehat{f}|}{|G|} \max_{\chi \in \widehat{G}} |\widehat{f}(\chi)|.$$

By the definition of $\widehat{f}(\chi)$,

(4.7)
$$|\widehat{f}(\chi)| \leq \sum_{g \in G} |f(g)|.$$

Let $m = \max_{g \in G} |f(g)|$, so $m > 0$ since $f$ is not identically zero. Then (4.7) implies $|\widehat{f}(\chi)| \leq m|\operatorname{supp} f|$, and feeding this into (4.6) yields

$$|f(x)| \leq \frac{m|\operatorname{supp} f||\operatorname{supp} \widehat{f}|}{|G|}.$$

Maximizing over all $x \in G$ implies $m \leq m|\operatorname{supp} f||\operatorname{supp} \widehat{f}|/|G|$. Divide both sides by $m$ and the desired inequality drops out. $\square$

In Examples 4.6 and 4.7, inequality (4.5) is an equality, so Theorem 4.8 is sharp.

Since $L(G)$ is spanned by the characters of $G$ and the delta-functions, linear identities in $L(G)$ can be verified by checking them on characters or delta-functions. For example, define a Hermitian inner product on $L(G)$ by the rule

(4.8)
$$\langle f_1, f_2 \rangle_G = \frac{1}{|G|} \sum_{g \in G} f_1(g)\overline{f_2}(g) \in \mathbf{C}.$$

We will prove Plancherel's theorem for $G$:

$$\langle f_1, f_2 \rangle_G = \frac{1}{|G|} \langle \widehat{f_1}, \widehat{f_2} \rangle_{\widehat{G}}$$

for all $f_1$ and $f_2$ in $L(G)$. (Compare to (2.4).) To check this identity, which is linear in both $f_1$ and $f_2$, it suffices to check it when $f_1$ and $f_2$ are characters. By Corollary 4.2, for characters $\chi_1$ and $\chi_2$ of $G$ we have

$$\langle \chi_1, \chi_2 \rangle_G = \begin{cases} 1, & \text{if } \chi_1 = \chi_2, \ 0, & \text{if } \chi_1 \neq \chi_2. \end{cases}$$

Since $\widehat{\chi} = |G|\delta_\chi$ (Example 4.7),

$$\frac{1}{|G|} \langle \widehat{\chi_1}, \widehat{\chi_2} \rangle_{\widehat{G}} = |G|\langle \delta_{\chi_1}, \delta_{\chi_2} \rangle_{\widehat{G}} = \sum_{\chi \in \widehat{G}} \delta_{\chi_1}(\chi)\overline{\delta_{\chi_2}}(\chi) = \begin{cases} 1, & \text{if } \chi_1 = \chi_2, \ 0, & \text{if } \chi_1 \neq \chi_2. \end{cases}$$

<!-- page 16 -->

This verifies Plancherel's theorem for $G$. The special case where $f_1 = f_2 = f$ is a single function from $G$ to $\mathbf{C}$ gives us Parseval's formula for $G$:

(4.9)
$$\sum_{g \in G} |f(g)|^2 = \frac{1}{|G|} \sum_{\chi \in \widehat{G}} |\widehat{f}(\chi)|^2.$$

Let's look at Fourier transforms for functions on a cyclic group. By writing a cyclic group in the form $\mathbf{Z}/(m)$, we can make an isomorphism with the dual group explicit: every character of $\mathbf{Z}/(m)$ has the form $\chi_k: j \mapsto e^{2\pi ijk/m}$ for a unique $k \in \mathbf{Z}/(m)$ (Exercise 3.1). The Fourier transform of a function $f: \mathbf{Z}/(m) \to \mathbf{C}$ can be viewed as a function on $\mathbf{Z}/(m)$:

(4.10)
$$\widehat{f}(k) := \sum_{j \in \mathbf{Z}/(m)} f(j)\overline{\chi_k}(j) = \sum_{j \in \mathbf{Z}/(m)} f(j)e^{-2\pi ijk/m}.$$

This is like viewing the Fourier transform of a function on $\mathbf{R}$ as a function on $\mathbf{R}$.

**Example 4.9.** Let $f: \mathbf{Z}/(8) \to \mathbf{C}$ be a function with period 2 having values 1 and 2. See Table 4. The Fourier transform of $f$ vanishes except at 0 and 4, which are the multiples of the frequency of $f$ (how often the period repeats).

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $f(n)$ | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |
| $\widehat{f}(n)$ | 12 | 0 | 0 | 0 | $-4$ | 0 | 0 | 0 |

**Table 4.**

**Example 4.10.** Let $f: \mathbf{Z}/(8) \to \mathbf{C}$ have the periodic values 5, 3, 1, and 1. Both $f$ and its Fourier transform are in Table 5. Now $f$ has frequency 2 (its period repeats twice) and the Fourier transform vanishes except at 0, 2, 4, and 6, which are multiples of the frequency.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $f(n)$ | 5 | 3 | 1 | 1 | 5 | 3 | 1 | 1 |
| $\widehat{f}(n)$ | 20 | 0 | $8-4i$ | 0 | 4 | 0 | $8+4i$ | 0 |

**Table 5.**

**Example 4.11.** Consider a function $f: \mathbf{Z}/(45) \to \mathbf{C}$ with the four successive repeating values 1, 8, 19, 17 starting with $f(0) = 1$. It is not a periodic function on $\mathbf{Z}/(45)$ since 4 does not divide 45, but the sequence 1, 8, 19, 17 repeats nearly 11 times. (The value of $f(44)$ is 1.) A calculation of $|\widehat{f}(n)|$, which is plotted below, reveals peaks in red at $n = 0, 11, 22, 23$, and 34 that are all at least 3 times as high as nearby values. This can't be shown to scale near 0, 11, and 34, which is why the values there have arrowheads on top. These peaks in $|\widehat{f}(n)|$ occur approximately at multiples of the approximate frequency!

As Examples 4.9 and 4.10 suggest, the Fourier transform of a periodic function on $\mathbf{Z}/(m)$ knows the frequency of the original function by the positions where the Fourier transform has nonzero values (Exercise 4.4). For *nearly* periodic functions on $\mathbf{Z}/(m)$, the approximate frequency is reflected in where the Fourier transform takes on its largest values. This idea is used in Shor's quantum algorithm for integer factorization [2], [3, Chap. 17], where it is convenient to redefine the Fourier transform (4.10) by dividing the sum by $\sqrt{m}$, which has the effect of making the Fourier transform a unitary operator on the functions $\mathbf{Z}/(m) \to \mathbf{C}$. See Exercise 4.11.

Exercises.

1. Let $G$ be a finite abelian group, $H$ be a subgroup of $G$, and $K$ be a subgroup of $\widehat{G}$. Show

$$\sum_{h \in H} \chi(h) = \begin{cases} |H|, & \text{if } \chi \text{ is trivial on } H, \ 0, & \text{otherwise}, \end{cases} \quad \sum_{\chi \in K} \chi(g) = \begin{cases} |K|, & \text{if } \chi(g) = 1 \text{ for all } \chi \in K, \ 0, & \text{otherwise}. \end{cases}$$

2. Let $f: \mathbf{Z}/(8) \to \mathbf{C}$ take the four values $a, b, c$, and $d$ twice in this order. Compute $\widehat{f}(n)$ explicitly and determine some values for $a, b, c$, and $d$ such that $\widehat{f}(n)$ is nonzero for $n = 0, 2$, and 6, but $\widehat{f}(4) = 0$.

3. For a subgroup $H$ of a finite abelian group $G$, let $\delta_H$ be the function that is 1 on $H$ and 0 off of $H$. Show the Fourier transform of $\delta_H$ is $\widehat{\delta_H} = |H|\delta_{H^\perp}$. How do the supports of $\delta_H$ and its Fourier transform compare with the inequality (4.5)?

4. Let $H$ be a subgroup of a finite abelian group $G$.

<!-- page 17 -->

(a) Suppose $f: G \to \mathbf{C}$ is constant on $H$-cosets (it is $H$-periodic). For $\chi \in \widehat{G}$ with $\chi 
otin H^\perp$, show $\widehat{f}(\chi) = 0$. Thus the Fourier transform of an $H$-periodic function on $G$ is supported on $H^\perp$.

(b) If $f: \mathbf{Z}/(m) \to \mathbf{C}$ has period $d$ where $d \mid m$, show $\widehat{f}: \mathbf{Z}/(m) \to \mathbf{C}$ is supported on the multiples of $m/d$. (See Examples 4.9 and 4.10.)

5. Find the analogue of Exercise 2.3 for functions on a finite abelian group.

<!-- page 18 -->

6. Let $f: G \to \mathbf{C}$.

a) Show $f(g) \in \mathbf{R}$ for all $g$ if and only if $\overline{\widehat{f}(\chi)} = \widehat{f}(\overline{\chi})$ for all $\chi$.

b) Show $\widehat{f}(\chi) \in \mathbf{R}$ for all $\chi$ if and only if $\overline{f(g)} = f(g^{-1})$ for all $g$.

7. Let $G$ be a finite abelian group and $H$ be a subgroup. For a function $f: G \to \mathbf{C}$, Poisson summation on $G$ says

$$\frac{1}{|H|} \sum_{h \in H} f(h) = \frac{1}{|G|} \sum_{\chi \in H^\perp} \widehat{f}(\chi),$$

where $H^\perp$ is as in Exercise 3.7. Prove this formula in two ways:

a) Copy the classical proof sketched in Section 2 (start with the function $F(x) = \sum_{h \in H} f(xh)$, which is $H$-periodic so it defines a function on $G/H$) to obtain

(4.11)
$$\frac{1}{|H|} \sum_{h \in H} f(xh) = \frac{1}{|G|} \sum_{\chi \in H^\perp} \widehat{f}(\chi)\chi(x)$$

for all $x \in G$ and then set $x = 1$.

b) By linearity in $f$ of both sides of the desired identity, verify Poisson summation directly on the delta-functions of $G$. (Corollary 3.7 and Example 4.6 will be useful.)

8. Let $T_g: L(G) \to L(G)$ be as in Exercise 3.6.

(a) Show $\widehat{T_g f} = \chi(g)\widehat{f}$ for all $f \in L(G)$.

(b) Show for all $f_1$ and $f_2$ in $L(G)$ that $\langle T_g f_1, T_g f_2 \rangle_G = \langle f_1, f_2 \rangle_G$.

9. Let $f \in L(G)$, so $\widehat{f}$ is in $L(\widehat{G})$ and $\widehat{\widehat{f}}$ is in $L(\widehat{\widehat{G}})$.

(a) Viewing $\widehat{\widehat{G}}$ as $G$ by Pontryagin duality, show $\widehat{\widehat{f}}(g) = |G|f(g^{-1})$.

(b) For a subgroup $H$ in $G$, define the $H$-average of $f$ and the $H$-cutoff of $f$ to be the following functions on $G$:

$$\operatorname{Avg}_H(f)(g) = \frac{1}{|H|} \sum_{h \in H} f(gh), \quad \operatorname{Cut}_H(f)(g) = \begin{cases} f(g), & \text{if } g \in H, \ 0, & \text{if } g 
otin H. \end{cases}$$

Check the identity $\widehat{\operatorname{Avg}_H(f)} = \operatorname{Cut}_{H^\perp}(\widehat{f})$ of functions on $\widehat{G}$ and then take the Fourier transform of both sides to get an identity of functions on $G$, which will be (4.11) as $x$ varies. (This shows that Poisson summation is essentially equivalent to the fact that the Fourier transform exchanges the operators $\operatorname{Avg}_H$ on $L(G)$ and $\operatorname{Cut}_{H^\perp}$ on $L(\widehat{G})$, or equivalently $\operatorname{Cut}_H$ on $L(G)$ and $\operatorname{Avg}_{H^\perp}$ on $L(\widehat{G})$.)

10. Let $G$ be a finite abelian group. For $f_1$ and $f_2$ in $L(G)$, define their *convolution* $f_1 * f_2: G \to \mathbf{C}$ by

$$(f_1 * f_2)(g) = \sum_{h \in G} f_1(h)f_2(gh^{-1}).$$

(a) Show $\delta_g * \delta_h = \delta_{gh}$, so $L(G)$ under convolution is a commutative $\mathbf{C}$-algebra isomorphic to the group ring $\mathbf{C}[G]$.

(b) Show $\widehat{f_1 * f_2}(\chi) = \widehat{f_1}(\chi)\widehat{f_2}(\chi)$, so the Fourier transform turns convolution into pointwise multiplication.

(c) Show $\delta_g * f = T_{g^{-1}}(f)$ and $\chi * f = \widehat{f}(\chi)\chi$ in two ways: by a direct calculation or by computing the Fourier transform of both sides and using (b).

<!-- page 19 -->

(d) For each $\chi \in \widehat{G}$, the function $h_\chi: L(G) \to \mathbf{C}$ given by $h_\chi(f) = \widehat{f}(\chi)$ is a $\mathbf{C}$-algebra homomorphism by (b). Does every $\mathbf{C}$-algebra homomorphism from $L(G)$ to $\mathbf{C}$ arise in this way?

11. On every finite abelian group $G$, rescale the definition of the Fourier transform by dividing by $\sqrt{|G|}$:

$$\widehat{f}(\chi) := \frac{1}{\sqrt{|G|}} \sum_{g \in G} f(g)\overline{\chi}(g).$$

Verify the following new versions of Fourier inversion and Plancherel's theorem:


<!-- page 20 -->
$f(g) = \frac{1}{\sqrt{|G|}} \sum_\chi \widehat{f}(\chi)\chi(g)$ and $\langle f_1, f_2 \rangle_G = \langle \widehat{f_1}, \widehat{f_2} \rangle_{\widehat{G}}$.

Check that this new Fourier transform sends convolution on $L(G)$ (Exercise 4.10) to multiplication only if we redefine convolution using division by $\sqrt{|G|}$:

$$(f_1 * f_2)(g) := \frac{1}{\sqrt{|G|}} \sum_{h \in G} f_1(h)f_2(gh^{-1}).$$


## 5. Structure of Finite Abelian Groups

We will now put characters to work by using them to prove each finite abelian group is a direct product of cyclic groups. This result was used in the proof of Theorem 3.13, that $G \cong \widehat{G}$, but that work will not be used here, so no circular reasoning occurs.

The following theorem shows that every cyclic subgroup of maximal size in a finite abelian group can be split off as a direct factor. Characters get used in an essential way in the proof.

**Theorem 5.1.** *Let $G$ be a finite abelian group and let $g \in G$ have maximal order in $G$. There is a subgroup $H \subset G$ such that $G \cong H \times \langle g \rangle$.*

*Proof.* Let $n$ be the order of $g$. The subgroup $\langle g \rangle$ of $G$ is cyclic of order $n$. In $S^1$ there is a cyclic subgroup of order $n$, namely $\mu_n$. Since cyclic groups of the same order are isomorphic, there is an isomorphism $\langle g \rangle \to \mu_n$, so $g$ is mapped to a root of unity of order $n$. This isomorphism can be viewed as a character of $\langle g \rangle$. Extend this to a character of $G$ (Theorem 3.3), so we have a character $\chi: G \to S^1$ such that $\chi(g)$ has order $n$. The image $\chi(G)$ contains $\mu_n$, and it turns out to be no larger.

*Claim:* $\chi(G) = \mu_n$.

Since $\chi(G)$ is a finite subgroup of $S^1$, it is cyclic (all finite subgroups of $S^1$ are cyclic). Therefore $\chi(G) = \langle \chi(\gamma) \rangle$ for some $\gamma \in G$. Since $\chi(G)$ contains $\mu_n$, $\chi(G) = \mu_{nn'}$ where $n' \geq 1$. Thus $\chi(\gamma)$ has order $nn'$. Let $\gamma$ have order $d$ in $G$, so $\gamma^d = 1$ in $G$ and thus $\chi(\gamma)^d = 1$ in $S^1$. That implies $nn' \mid d$, so $nn' \leq d$. Since $n$ is the maximal order of the elements in $G$, $d \leq n$. The relations $nn' \leq d$ and $d \leq n$ imply $n' = 1$, so $\chi(G) = \mu_n$. This proves the claim.

Set $H = \ker \chi$. Then $H \cap \langle g \rangle = \{1\}$ since $\chi$ is one-to-one on $\langle g \rangle$ by construction. For each $x \in G$, $\chi(x) \in \chi(G) = \mu_n = \chi(\langle g \rangle)$, so $\chi(x) = \chi(g^j)$ for some $j$. Therefore $h := xg^{-j}$ is in $H$ and $x = hg^j$. This proves that the multiplication map $H \times \langle g \rangle \to G$ where $(h, g^j) \mapsto hg^j$ is surjective. It is a homomorphism and its kernel is trivial, so $G \cong H \times \langle g \rangle$. $\square$

**Theorem 5.2.** *Every finite abelian group $G$ is isomorphic to a product of cyclic groups:*

$$G \cong \mathbf{Z}/(n_1) \times \mathbf{Z}/(n_2) \times \cdots \times \mathbf{Z}/(n_k).$$

*Proof.* Induct on $|G|$. The result is clear when $|G| = 1$. When $|G| > 1$, let $n$ be the maximal order of the elements of $G$, so $G \cong H \times \mathbf{Z}/(n)$ by Theorem 5.1. Since $|H| < |G|$, by induction $H$ is isomorphic to a direct product of cyclic groups, so $G$ is also isomorphic to a direct product of cyclic groups. $\square$

Theorem 5.2 can be refined: $G$ is a direct product of cyclic groups with the extra feature that $n_1 \mid n_2 \mid \cdots \mid n_k$. To prove this, use the fact that the order of each element of a finite abelian group $G$ divides the maximal order of the elements of $G$ (Theorem A.3).

Exercises.

1. What is the structure (as a direct product of cyclic groups) of the finite abelian groups whose nontrivial characters all have order 2?

2. Mimic the proof of Theorem 5.1 to decompose $(\mathbf{Z}/(20))^\times$ (of size 8) and $(\mathbf{Z}/(45))^\times$ (of size 24) into a direct product of cyclic groups.

3. Show by an explicit counterexample that the following is false: if two subgroups $H$ and $K$ of a finite abelian group $G$ are isomorphic then there is an automorphism of $G$ that restricts to an isomorphism from $H$ to $K$.

4. For a finite abelian group $G$, show the maximum order of the elements of $G$ and the number $|G|$ have the same prime factors. (Hint: If $g$ has order $n$ and there is an element $h$ of prime order $p$ where $p 
mid n$, what is the order of $gh$?)

This is false in general for nonabelian $G$, as shown in the table below where $g(n)$ (called Landau's function) is the maximal order of the elements of $S_n$. For $n \geq 3$ in the table, some prime factor of $n! = |S_n|$ does not divide $g(n)$.

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $g(n)$ | 1 | 2 | 3 | 4 | 6 | 6 | 12 | 15 | 20 | 30 | 30 | 60 | 60 | 84 | 105 |

**Table 6.** Maximal order of elements of $S_n$

5. Let $G$ be a finite abelian group and $F$ be a field containing a full set of $|G|$th roots of unity. (So $x^{|G|} = 1$ has $|G|$ solutions in $F$.) Define characters of $G$ to be group homomorphisms $\chi: G \to F^\times$ and write the set of all such characters as $\widehat{G}$.

a) Construct a character table for $\mathbf{Z}/(4)$ and $(\mathbf{Z}/(2))^2$ when $F$ is the field $\mathbf{Z}/(5)$.

b) Prove every lemma, theorem, and corollary from Section 3 for the new meaning of $\widehat{G}$. There is no longer complex conjugation on character values, but the inverse of $\chi$ is still the function $g \mapsto \chi(g^{-1}) = \chi(g)^{-1}$. (Hint: For each $d$ dividing $|G|$, $x^d = 1$ has $d$ distinct solutions in $F^\times$, which form a cyclic group.)

c) Prove Theorem 4.1 and Corollary 4.2 for $F$-valued characters of $G$.

d) Set $L(G, F)$ to be the functions $G \to F$. This is an $F$-vector space in the same way that $L(G)$ is a complex vector space. For each function $f \in L(G, F)$, define its Fourier transform $\widehat{f} \in L(\widehat{G}, F)$ by $\widehat{f}(\chi) = \sum_{g \in G} f(g)\chi(g^{-1})$. Prove the Fourier inversion formula and Plancherel's theorem in this context. (Note: If the field $F$ has characteristic $p$ then $1/|G|$ in the Fourier inversion formula makes sense in $F$ since $p$ doesn't divide $|G|$ -- why?)

e) Check everything you have done goes through if the assumption that $x^{|G|} = 1$ has a full set of solutions in $F$ is weakened to $x^m = 1$ having a full set of solutions in $F$, where $m$ is the maximal order of the elements of $G$. For example, if $G = (\mathbf{Z}/(2))^d$ then $m = 2$ and we can use $F = \mathbf{Z}/(3)$.


## 6. Existence of Solutions to a Mordell Equation mod $p$

<!-- page 21 -->

For $k \in \mathbf{Z}$, an equation of the form $y^2 = x^3 + k$ is called a *Mordell equation*. When $k \neq 0$, it is a hard theorem that such an equation has only finitely many integral solutions $(x, y)$, which could include having no integral solutions.[^3] For example, the integral solutions of $y^2 = x^3 - 4$ are $(2, \pm 2)$ and $(5, \pm 11)$, and $y^2 = x^3 - 5$ has no integral solutions. Using characters, we will show for each $k \in \mathbf{Z}$ that the congruence $y^2 \equiv x^3 + k \bmod p$ modulo a prime $p$ always has a solution.

For a character $\chi$ on $(\mathbf{Z}/(p))^\times$, extend $\chi$ to $\mathbf{Z}/(p)$ by setting $\chi(0) = 0$. Then $\chi(ab) = \chi(a)\chi(b)$ for all $a, b \in \mathbf{Z}/(p)$.

**Lemma 6.1.** *If $p$ is prime and $d \mid (p-1)$, then there is a character $\chi$ of $(\mathbf{Z}/(p))^\times$ with order $d$, and for each $a \in \mathbf{Z}/p\mathbf{Z}$,*

$$|\{x \in \mathbf{Z}/(p): x^d \equiv a \bmod p\}| = 1 + \chi(a) + \chi(a)^2 + \cdots + \chi(a)^{d-1}.$$

*Proof.* The group $(\mathbf{Z}/(p))^\times$ is cyclic of order $p-1$,[^4] so $|\{x \in \mathbf{Z}/(p): x^d \equiv 1 \bmod p\}| = d$ since $d \mid (p-1)$. Thus

(6.1)
$$|\{x \in \mathbf{Z}/(p): x^d \equiv a \bmod p\}| = \begin{cases} d, & \text{if } a 
ot\equiv 0 \bmod p \text{ and } a \text{ is a } d\text{th power mod } p, \ 1, & \text{if } a \equiv 0 \bmod p, \ 0, & \text{if } a \text{ is not a } d\text{th power mod } p. \end{cases}$$

The character group of $(\mathbf{Z}/(p))^\times$ is cyclic of order $p-1$ by Theorem 3.11, so $(\mathbf{Z}/(p))^\times$ has a character of order $d$. Call such a character $\chi$. For each $a \in \mathbf{Z}/(p)$, we'll show that $1 + \chi(a) + \chi(a)^2 + \cdots + \chi(a)^{d-1}$ has the same values as in (6.1).

- If $a$ is a nonzero $d$th power mod $p$, say $a \equiv b^d \bmod p$, then $\chi(a) = \chi(b^d) = \chi(b)^d = 1$ since $\chi^d$ is identically 1 on $(\mathbf{Z}/(p))^\times$, so $1 + \chi(a) + \chi(a)^2 + \cdots + \chi(a)^{d-1} = d$.

- If $a \equiv 0 \bmod p$ then $\chi(a) = 0$, so $1 + \chi(a) + \chi(a)^2 + \cdots + \chi(a)^{d-1} = 1$.

- Lastly, if $a$ is in $(\mathbf{Z}/(p))^\times$ and is not a $d$th power, we'll show $\chi(a) \neq 1$, so by summing a finite geometric series,

$$1 + \chi(a) + \chi(a)^2 + \cdots + \chi(a)^{d-1} = \frac{\chi(a)^d - 1}{\chi(a) - 1} = \frac{1 - 1}{\chi(a) - 1} = 0,$$

which would complete the proof.

Let $g$ be a generator of $(\mathbf{Z}/(p))^\times$ and write $a = g^k$ for $k \in \mathbf{Z}$.

*Step 1:* $\chi(g)$ has order $d$. Since $\chi$ has order $d$, $\chi(g)^d = 1$, so $\chi(g)$ has order dividing $d$. Since $\chi((\mathbf{Z}/(p))^\times) = \langle \chi(g) \rangle$, if $\chi(g)$ has order less than $d$ then $\chi$ as a character has order less than $d$, which $\chi$ doesn't. Thus $\chi(g)$ has order $d$.

*Step 2:* $\chi(a) \neq 1$. If $\chi(a) = 1$ then $\chi(g)^k = 1$, so $d \mid k$ by Step 1. Then $a = g^k$ is a $d$th power, which isn't the case, so $\chi(a) \neq 1$. $\square$

**Theorem 6.2.** *For each prime $p$ and integer $k$, the number of solutions $(x, y)$ in $\mathbf{Z}/(p)$ to $y^2 \equiv x^3 + k \bmod p$ is $p$ if $p \equiv 1 \bmod 3$ and is at least 2 if $p 
ot\equiv 1 \bmod 3$.*

*Proof.* **Case 1:** $p 
ot\equiv 1 \bmod 3$.

Since $3 
mid (p-1)$ we have $(3, p-1) = 1$, so cubing is a bijection $\mathbf{Z}/(p) \to \mathbf{Z}/(p)$ (on $(\mathbf{Z}/(p))^\times$ it is injective and thus surjective since the group is finite), so for each $y \in \mathbf{Z}/(p)$

<!-- page 22 -->

there is a unique $x \in \mathbf{Z}/(p)$ such that $y^2 - k \equiv x^3 \bmod p$. Thus the number of solutions in $\mathbf{Z}/(p)$ of $y^2 \equiv x^3 + k \bmod p$ is $p$.

**Case 2:** $p \equiv 1 \bmod 3$.

If $k \equiv 0 \bmod p$, then the congruence is $y^2 \equiv x^3 \bmod p$, which has the $p$ solutions $(t^2, t^3)$ for $t \in \mathbf{Z}/(p)$ (and in fact no further solutions[^5]). So now we can assume $k 
ot\equiv 0 \bmod p$.

Since $3 \mid (p-1)$, there is a cubic character $\chi$ on $(\mathbf{Z}/(p))^\times$, meaning $\chi$ has order 3, and the inverse $\chi^2$ of $\chi$ is the complex conjugate $\overline{\chi}$. Since $p$ is odd, there is a quadratic character $\psi$ on $(\mathbf{Z}/(p))^\times$ (it's the Legendre symbol). To count solutions to $y^2 \equiv x^3 + k \bmod p$ we will count solutions $(a, b)$ to the simpler equation $b \equiv a + k \bmod p$ and then count how often $a$ is a cube mod $p$ and $b$ is a square mod $p$.

By Lemma 6.1, the number of ways $a$ is a cube mod $p$ is $1 + \chi(a) + \chi(a)^2 = 1 + \chi(a) + \overline{\chi}(a)$, and the number of ways $b$ is a square mod $p$ is $1 + \psi(b)$. Let $N_p(k)$ be the number of mod $p$ solutions to $y^2 \equiv x^3 + k \bmod p$, so

$$N_p(k) = \sum_{(a,b)} (1 + \chi(a) + \overline{\chi}(a))(1 + \psi(b)) = \sum_a (1 + \chi(a) + \overline{\chi}(a))(1 + \psi(a+k)),$$

where the first sum runs over all $(a, b)$ mod $p$ for which $b \equiv a + k \bmod p$. (Note $a$ or $b$ determines the other mod $p$.) Expanding out the second sum, we get a sum over all $a$ mod $p$ with each summand having 6 terms:

$$N_p(k) = \sum_a (1 + \chi(a) + \overline{\chi}(a) + \psi(a+k) + \chi(a)\psi(a+k) + \overline{\chi}(a)\psi(a+k)).$$

Split this up into 6 sums. The first sum is $p$ since the number of possible $a$ mod $p$ is $p$. The second and third sums, $\sum_a \chi(a)$ and $\sum_a \overline{\chi}(a)$, are 0 since the sum of a nontrivial multiplicative character over $\mathbf{Z}/(p)$ is 0 (a term where $a = 0$ can be dropped since $\chi(0) = 0$ and $\overline{\chi}(0) = 0$). Similarly, $\sum_a \psi(a+k) = \sum_a \psi(a) = 0$ using a change of variables $a \mapsto a-k$. We're left with

$$N_p(k) = p + \sum_a \chi(a)\psi(a+k) + \sum_a \overline{\chi}(a)\psi(a+k).$$

Since $k 
ot\equiv 0 \bmod p$, we can make the change of variables $a \mapsto ka$ in both sums and pull out the character values at $k$:

$$N_p(k) = p + \chi(k)\psi(k)\sum_a \chi(a)\psi(a+1) + \overline{\chi}(k)\psi(k)\sum_a \overline{\chi}(a)\psi(a+1).$$

Replace $a$ mod $p$ with $-a$ mod $p$ in the sums:

$$N_p(k) = p + \chi(-k)\psi(k)\sum_a \chi(a)\psi(1-a) + \overline{\chi}(-k)\psi(k)\sum_a \overline{\chi}(a)\psi(1-a).$$

Set $J = \sum_a \chi(a)\psi(1-a)$, so $\overline{J} = \sum_a \overline{\chi}(a)\psi(1-a)$ since $\psi$-values are $\pm 1$. Thus

$$N_p(k) = p + \chi(-k)\psi(k)J + \overline{\chi}(-k)\psi(k)\overline{J} = p + 2\operatorname{Re}(\chi(-k)\psi(k)J).$$

For each $z \in \mathbf{C}$, $|\operatorname{Re}(z)| \leq \sqrt{|z|}$, so $|N_p(k) - p| \leq 2\sqrt{|J|}$. Since $\chi$ and $\psi$ are nontrivial multiplicative characters mod $p$ and $\chi\psi$ is nontrivial, $|J| = \sqrt{p}$.[^6] Thus $|N_p(k) - p| \leq 2\sqrt{p}$,

<!-- page 23 -->

so $N_p(k) \geq p - 2\sqrt{p}$. The function $x - 2\sqrt{x}$ on $(0, \infty)$ is increasing for $x > 1$. If $p \equiv 1 \bmod 3$ then $p \geq 7$, so $N_p(k) \geq p - 2\sqrt{p} \geq 7 - 2\sqrt{7} \approx 1.7$, so $N_p(k) \geq 2$. $\square$

By an explicit search for solutions of $y^2 \equiv x^3 + k \bmod 7$ as $k$ varies, the number of solutions is 2 if $k \equiv 4 \bmod 7$ (namely $(0, \pm 2)$), 3 if $k \equiv 6 \bmod 7$ (namely $(1, 0)$, $(2, 0)$, and $(4, 0)$), and at least 6 for other $k$ mod 7. After 7, the next prime that is 1 mod 3 is 13 and $13 - 2\sqrt{13} \approx 5.7$, so $N_p(k) \geq 6$ if $p \equiv 1 \bmod 3$ and $p > 7$.

Exercises.

1. For prime $p$ and $n \in \mathbf{Z}^+$, set $d = (n, p-1)$. For $r \in \mathbf{Z}$, let $\varphi_r: (\mathbf{Z}/(p))^\times \to (\mathbf{Z}/(p))^\times$ by $\varphi_r(x) = x^r$.

a) Show $\varphi_n$ and $\varphi_d$ have the same image and same kernel. (Hint: $d$ is a $\mathbf{Z}$-linear combination of $n$ and $p-1$.) For example, on $(\mathbf{Z}/(11))^\times$, show $\varphi_4$ and $\varphi_2$ have image $\{1, 3, 4, 5, 9\}$ and kernel $\{1, 10\}$.

b) For nonzero $a$ in $\mathbf{Z}/(p)$, use (a) to show the equations $x^n = a$ and $x^d = a$ have the same number of solutions in $\mathbf{Z}/(p)$.

c) Find all solutions of $x^4 = 3$ and of $x^2 = 3$ in $\mathbf{Z}/(11)$. (There are two solutions in each case.)

d) For nonzero $a$ in $\mathbf{Z}/(p)$, show $x^n + y^n = a$ and $x^d + y^d = a$ have the same number of solutions in $\mathbf{Z}/(p)$.

2. Let $p$ be prime, $a$ be nonzero in $\mathbf{Z}/(p)$, and $d$ be a positive factor of $p-1$. We want to estimate the number of solutions of $x^d + y^d = a$ in $\mathbf{Z}/(p)$.

a) For a polynomial $f(x)$ with coefficients in $\mathbf{Z}/(p)$, let $N(f(x) = a)$ be the number of solutions of $f(x) = a$ in $\mathbf{Z}/(p)$. By Lemma 6.1, $(\mathbf{Z}/(p))^\times$ has a character $\chi$ of order $d$ and we set $\chi(0) = 0$. Show

$$N(x^d + y^d = a) = \sum_{\substack{b,c \in \mathbf{Z}/(p) \ b+c=a}} N(x^d = b)N(y^d = c)$$

$$= \sum_{b \in \mathbf{Z}/(p)} \left(1 + \sum_{i=1}^{d-1} \chi(b)^i
ight)\left(1 + \sum_{j=1}^{d-1} \chi(a-b)^j
ight).$$

b) When $a \neq 0$ in $\mathbf{Z}/(p)$, expand the product in (a) and rearrange terms to show

$$N(x^d + y^d = a) = p + \sum_{1 \leq i,j \leq d-1} \sum_{b \in \mathbf{Z}/(p)} \chi(b)^i \chi(a-b)^j$$

$$= p + \sum_{1 \leq i,j \leq d-1} \chi(a)^{i+j} \sum_{b \in \mathbf{Z}/(p)} \chi(b)^i \chi(1-b)^j.$$

c) For characters $\psi$ and $\psi'$ on $(\mathbf{Z}/(p))^\times$, set $J(\psi, \psi') = \sum_{b \in \mathbf{Z}/(p)} \psi(b)\psi'(1-b)$ (it is called a Jacobi sum), so by (b), if $a \neq 0$ in $\mathbf{Z}/(p)$ then

$$N(x^d + y^d = a) = p + \sum_{1 \leq i,j \leq d-1} \chi(a)^{i+j} J(\chi^i, \chi^j).$$

<!-- page 24 -->

For a nontrivial character $\psi$ on $(\mathbf{Z}/(p))^\times$, $J(\psi, \overline{\psi}) = -\psi(-1)$.[^7] Use that to show

$$N(x^d + y^d = a) = p + 1 - N(x^d = -1) + \sum_{\substack{1 \leq i,j \leq d-1 \ i+j \neq d}} \chi(a)^{i+j} \sum_{b \in \mathbf{Z}/(p)} \chi(b)^i \chi(1-b)^j.$$

d) When $\psi$, $\psi'$, and $\psi\psi'$ are all nontrivial, $|J(\psi, \psi')| = \sqrt{p}$.[^8] Use that and (c) to show for nonzero $a$ in $\mathbf{Z}/(p)$ that

$$|N(x^d + y^d = a) - (p+1)| \leq d + (d-1)(d-2)\sqrt{p}$$

e) Use part (d) and Exercise 6.1(d) to show for $n \in \mathbf{Z}^+$ and sufficiently large $p$ (depending only on $n$) that for each $a \in (\mathbf{Z}/(p))^\times$ the equation $x^n + y^n = a$ has a solution in $\mathbf{Z}/(p)$ where $x$ and $y$ are both nonzero.

## 7. Dual Homomorphisms

The set $\operatorname{Hom}(G_1, G_2)$ of all homomorphisms from the abelian group $G_1$ to the abelian group $G_2$ forms an abelian group under pointwise multiplication

**Theorem 7.1.** *Let $G_1$ and $G_2$ be finite abelian groups. For a homomorphism $f: G_1 \to G_2$, set $f^*: \widehat{G_2} \to \widehat{G_1}$ by $f^*(\chi) = \chi \circ f$. Then $f^*$ is a group homomorphism and the map sending $f$ to $f^*$ gives a group isomorphism*

$$\operatorname{Hom}(G_1, G_2) \cong \operatorname{Hom}(\widehat{G_2}, \widehat{G_1}).$$

*Proof.* If $f: G_1 \to G_2$ is a homomorphism and $\chi \in \widehat{G_2}$, then for $g$ and $g'$ in $G_1$ we have

$$\chi(f(gg')) = \chi(f(g)f(g')) = \chi(f(g))\chi(f(g')),$$

so $f^*(\chi) := \chi \circ f$ lies in $\widehat{G_1}$. Thus we get the map $\operatorname{Hom}(G_1, G_2) \to \operatorname{Hom}(\widehat{G_2}, \widehat{G_1})$ as advertised. Check $(ff')^* = f^*(f')^*$, so $f \mapsto f^*$ is a homomorphism.

Repeating this idea leads to a group homomorphism $\operatorname{Hom}(\widehat{G_2}, \widehat{G_1}) \to \operatorname{Hom}(\widehat{\widehat{G_1}}, \widehat{\widehat{G_2}})$. By Pontryagin duality it is a homomorphism $\operatorname{Hom}(\widehat{G_2}, \widehat{G_1}) \to \operatorname{Hom}(G_1, G_2)$ and the composite

$$\operatorname{Hom}(G_1, G_2) \to \operatorname{Hom}(\widehat{G_2}, \widehat{G_1}) \to \operatorname{Hom}(G_1, G_2)$$

turns out to be (after unwinding definitions, left to the reader) the identity function. Therefore our original map $\operatorname{Hom}(G_1, G_2) \to \operatorname{Hom}(\widehat{G_2}, \widehat{G_1})$ is a group isomorphism. $\square$

The homomorphism $f^*: \widehat{G_2} \to \widehat{G_1}$ is called the *dual homomorphism* to $f$.

Exercises.

1. For a homomorphism $f: G_1 \to G_2$, show $(\ker f)^\perp = \operatorname{im} f^*$ in $\widehat{G_1}$ and $(\operatorname{im} f)^\perp = \ker f^*$ in $\widehat{G_2}$.

2. Show the isomorphism $\operatorname{Hom}(G, G) \cong \operatorname{Hom}(\widehat{G}, \widehat{G})$ in Theorem 7.1 coming from the identity map on $G$ associates $g \mapsto g^m$ in $\operatorname{Hom}(G, G)$ with $\chi \mapsto \chi^m$ in $\operatorname{Hom}(\widehat{G}, \widehat{G})$.


## 8. Abelian Group Determinants

<!-- page 25 -->

Consider a square $n \times n$ matrix where each row is a cyclic shift of the previous row:

(8.1)
$$\begin{pmatrix} X_0 & X_1 & X_2 & \cdots & X_{n-1} \ X_{n-1} & X_0 & X_1 & \cdots & X_{n-2} \ X_{n-2} & X_{n-1} & X_0 & \cdots & X_{n-3} \ \vdots & \vdots & \vdots & \ddots & \vdots \ X_1 & X_2 & X_3 & \cdots & X_0 \end{pmatrix}$$

Its determinant is called a *circulant*. When $n$ is 2 and 3, the circulants are

$$\begin{vmatrix} X_0 & X_1 \ X_1 & X_0 \end{vmatrix} = X_0^2 - X_1^2 \quad \text{and} \quad \begin{vmatrix} X_0 & X_1 & X_2 \ X_2 & X_0 & X_1 \ X_1 & X_2 & X_0 \end{vmatrix} = X_0^3 + X_1^3 + X_2^3 - 3X_0 X_1 X_2.$$

These factor as

$$(X_0 + X_1)(X_0 - X_1) \quad \text{and} \quad (X_0 + X_1 + X_2)(X_0 + \omega X_1 + \omega^2 X_2)(X_0 + \omega^2 X_1 + \omega X_2),$$

where $\omega = e^{2\pi i/3}$.

If we think about the variables $X_i$ as being indexed by $\mathbf{Z}/(n)$ then the $(i, j)$ entry of (8.1) is $X_{j-i}$. More generally, for a finite group $G$, index a set of variables $X_g$ by $G$ and form the matrix indexed by $G \times G$ where the $(g, h)$ entry is $X_{gh^{-1}}$. (The circulant is the determinant of the matrix $(X_{j-i}) = (X_{i-j})^\top$.) The determinant is called the *group determinant* of $G$:

(8.2)
$$\Delta(G) = \det(X_{gh^{-1}}).$$

This is a homogeneous polynomial of degree $|G|$ with integer coefficients. A circulant is the group determinant of a cyclic group.

Circulants of order 2 and 3 are products of linear factors with roots of unity as coefficients. Dedekind and Burnside each proved the same property for the group determinant of every finite abelian group, but Dedekind's approach revealed more structure in the factors: the roots of unity in a given linear factor are the values of one of the characters of the group!

**Theorem 8.1** (Dedekind). *If $G$ is a finite abelian group then its group determinant factors into linear factors over the complex numbers:*

$$\det(X_{gh^{-1}}) = \prod_{\chi \in \widehat{G}} \left(\sum_{g \in G} \chi(g) X_g
ight).$$

*Proof.* We will realize $(X_{gh^{-1}})$ as the matrix for a linear transformation and then find its diagonalization to compute its determinant.

Let $V = \mathbf{C}[G]$ be the group ring of $G$. For each $v \in V$, define the linear map $L_v: V \to V$ to be (left) multiplication by $v$: $L_v(x) = vx$. We will compute the matrix for $L_v$ with respect to the basis $G$ of $V$. Writing $v = \sum_{g \in G} a_g g$ we have for each $h \in G$

$$L_v(h) = \sum_{g \in G} a_g gh = \sum_{g \in G} a_{gh^{-1}} g,$$

so the matrix for $L_v$ with respect to the basis $G$ is $(a_{gh^{-1}})$.

<!-- page 26 -->

Another basis for $\mathbf{C}[G]$ is the set of formal sums $\sum_{g \in G} \chi(g)g$, one for each character $\chi$ of $G$: the number of such sums has the right size to be a basis, and for a linear relation

$$\sum_\chi c_\chi \left(\sum_{g \in G} \chi(g)g
ight) = 0$$

in $\mathbf{C}[G]$ we get $\sum_\chi c_\chi \chi(g) = 0$ for all $g$ (the coefficient of each $g$ is 0), so every $c_\chi$ is 0 by Fourier inversion.

This new basis of $\mathbf{C}[G]$, indexed by the characters, consists of eigenvectors for $L_v$:

$$L_v\left(\sum_{h \in G} \chi(h)h
ight) = \left(\sum_{g \in G} a_g g
ight)\left(\sum_{h \in G} \chi(h)h
ight)$$
$$= \sum_{k \in G} \left(\sum_{gh=k} a_g \chi(h)
ight) k$$
$$= \sum_{k \in G} \left(\sum_{g \in G} a_g \chi(g^{-1})\chi(k)
ight) k$$
$$= \left(\sum_{g \in G} a_g \chi(g^{-1})
ight)\left(\sum_{k \in G} \chi(k)k
ight).$$

Since $\det(L_v)$ is the product of the eigenvalues of $L_v$ for an eigenbasis,

$$\det(a_{gh^{-1}}) = \prod_{\chi \in \widehat{G}} \left(\sum_{g \in G} a_g \overline{\chi}(g)
ight).$$

If we interchange the roles of $\chi$ and $\overline{\chi}$ in this product then we obtain

$$\det(a_{gh^{-1}}) = \prod_{\chi \in \widehat{G}} \left(\sum_{g \in G} a_g \chi(g)
ight).$$

Thus the multivariable polynomials $\det(X_{gh^{-1}})$ and $\prod_{\chi \in \widehat{G}} \sum_{g \in G} \chi(g) X_g$ are equal on all of $\mathbf{C}^n$, so they must be the same polynomial. $\square$

**Example 8.2.** Taking $G = \mathbf{Z}/(n)$ and $\zeta_n = e^{2\pi i/n}$,

$$\begin{vmatrix} X_0 & X_1 & \cdots & X_{n-1} \ X_{n-1} & X_0 & \cdots & X_{n-2} \ \vdots & \vdots & \ddots & \vdots \ X_1 & X_2 & \cdots & X_0 \end{vmatrix} = \prod_{j=0}^{n-1} \left(\sum_{k=0}^{n-1} \zeta_n^{jk} X_k
ight)$$
$$= \prod_{j=0}^{n-1} (X_0 + \zeta_n^j X_1 + \cdots + \zeta_n^{(n-1)j} X_{n-1}).$$

Applications of the factorization of the group determinant for abelian (not necessarily cyclic) groups can be found in [4, \S5.5].

<!-- page 27 -->

If $G$ is a nonabelian group then its group determinant has an irreducible factor with degree greater than 1. Studying irreducible factors of the group determinant for nonabelian $G$ led Frobenius to discover representation theory and the correct extension of the notion of a character to (finite) nonabelian groups.

Exercises.

1. Check the factorization of the group determinant for $\mathbf{Z}/(4)$.

2. Compute and factor the group determinant of $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$.

3. If $G$ is nonabelian, show the polynomial $\Delta(G)$ in (8.2) is divisible by $\sum_{g \in G} X_g$, and more generally by $\sum \chi(g)X_g$ for each homomorphism $\chi: G \to S^1$.

## 9. Eigenspace Decomposition

In high school math we first learn about even and odd functions $\mathbf{R} \to \mathbf{R}$: an even function satisfies $f(-x) = f(x)$ for all $x$ and an odd function satisfies $f(-x) = -f(x)$ for all $x$. For example, $x^2$ and $\cos x$ are even while $x^3$ and $\sin x$ are odd. Every function $\mathbf{R} \to \mathbf{R}$ is expressible as a sum of an even and odd function:

(9.1)
$$f(x) = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2},$$

where the first term on the right is even and the second term on the right is odd. Moreover, that expression as a sum of even and odd functions is unique: if $f(x) = E(x) + O(x)$ where $E$ and even and $O$ is odd, then $f(-x) = E(-x) + O(-x) = E(x) - O(x)$, so $f(x) + f(-x) = 2E(x)$ and $f(x) - f(-x) = 2O(x)$. Therefore $E(x) = (f(x) + f(-x))/2$ and $O(x) = (f(x) - f(-x))/2$. The formulas for the even and odd parts of $f$ are based on averaging and anti-averaging $f(x)$ and $f(-x)$.

This type of decomposition occurs in other settings where there is an additive mapping that iterates twice to the identity map (like $f(x) \mapsto f(-x)$ above, where $f(-(-x)) = f(x)$). Here are two more examples.

(1) Complex conjugation (where $\overline{\overline{z}} = z$) leads to an "even/odd" decomposition of each complex number $z$ as the unique sum of a real number (where $\overline{w} = w$) and a purely imaginary number (where $\overline{w} = -w$): for $z = a + bi$, $\overline{z} = a - bi$ and

$$z = \frac{z + \overline{z}}{2} + \frac{z - \overline{z}}{2} = a + bi.$$

(2) The matrix transpose (where $M^{\top\top} = M$) leads to the unique expression of each square matrix over a field not of characteristic 2 as a sum of matrices that are symmetric ($M^\top = M$) and skew-symmetric ($M^\top = -M$):

$$A = \frac{A + A^\top}{2} + \frac{A - A^\top}{2}.$$

(3) The swap operator on real or complex-valued functions of two variables ($f(x, y) \mapsto f(y, x)$) leads to the unique expression of each such function as a sum of functions that are symmetric ($F(y, x) = F(x, y)$) and anti-symmetric ($F(y, x) = -F(x, y)$):

$$f(x, y) = \frac{f(x, y) + f(y, x)}{2} + \frac{f(x, y) - f(y, x)}{2}.$$

<!-- page 28 -->

We will now see an analogue of this for finite abelian groups acting on complex vector spaces. For a group $G$ and complex vector space $V$, a *linear action of $G$ on $V$*[^9] is an action $G \times V \to V$ where $v \mapsto gv$ is linear for each $g \in G$: $g(v + w) = gv + gw$ and $g(cv) = c(gv)$ for all $g \in G$, $v$ and $w$ in $V$, and $c \in \mathbf{C}$.

**Example 9.1.** When $V$ is the space of all functions $\mathbf{C} \to \mathbf{C}$, the group $\mu_n$ of $n$th roots of unity acts on $V$ by interior scaling: for $r \in \mu_n$ and $f \in V$, let the function $r \cdot f$ be given by

$$(r \cdot f)(z) = f(rz).$$

For instance, $((-1) \cdot f)(z) = f(-z)$.

This is a linear action of $\mu_n$ on $V$: $r \cdot (f_1 + f_2) = r \cdot f_1 + r \cdot f_2$ for all $r \in \mu_n$ and $f_1, f_2 \in V$, and $r \cdot (cf) = c(r \cdot f)$ for all $r \in \mu_n$, $c \in \mathbf{C}$, and $f \in V$.

**Example 9.2.** When $V$ is the space of all functions $\mathbf{C} \to \mathbf{C}$, the group $\mu_n$ of $n$th roots of unity acts on $V$ by exterior scaling: for $r \in \mu_n$ and $f \in V$, let the function $rf$ be given by

$$(r \cdot f)(z) = rf(z).$$

For instance, $((-1) \cdot f)(z) = -f(z)$.

This is a linear action of $\mu_n$ on $V$ that is not the same as the action in the previous example (when $n \geq 2$).

**Theorem 9.3.** *Let $G$ be a finite abelian group and $V$ be a complex vector space on which $G$ acts linearly. For a character $\chi$ of $G$, set $V(\chi) = \{v \in V: gv = \chi(g)v \text{ for all } g \in G\}$. This is a subspace of $G$ and*

$$V = \bigoplus_{\chi \in \widehat{G}} V(\chi).$$

We call $V(\chi)$ the $\chi$-*eigenspace* of $V$: it's the elements of $V$ on which the effect of each $g$ in $G$ is given by multiplication by the number $\chi(g)$. So $V(\chi)$ is a common eigenspace of all $g \in G$, where their eigenvalues are the numbers $\chi(g)$ associated to a single character of $G$. For instance, $V(\mathbf{1}_G) = \{v \in V: gv = v \text{ for all } g \in G\}$ is the set of fixed points for all $g$.

*Proof.* It's left to the reader to check each $V(\chi)$ is a subspace of $V$. To show $V$ is the direct sum of all $V(\chi)$, first we'll show $V = \sum_\chi V(\chi)$ and then we'll show the sum is direct.

For $v \in V$, here is its piece in $V(\chi)$: set

(9.2)
$$v_\chi = \frac{1}{|G|} \sum_{g \in G} \overline{\chi}(g)gv.$$

We'll show $v_\chi \in V(\chi)$ for all $\chi$ and $v = \sum_\chi v_\chi$, so $V = \sum_\chi V(\chi)$.

<!-- page 29 -->

Showing $v_\chi \in V(\chi)$ means showing $hv_\chi = \chi(h)v_\chi$ for each $h \in G$. From the definition of $v_\chi$ and linearity of the action of $G$ on $V$, for each $h \in G$ we have

$$hv_\chi = \frac{1}{|G|} \sum_{g \in G} \overline{\chi}(g)(hg)v$$
$$= \frac{1}{|G|} \sum_{g \in G} \overline{\chi}(h^{-1}g)gv$$
$$= \frac{1}{|G|} \sum_{g \in G} \overline{\chi}(h^{-1})\overline{\chi}(g)gv$$
$$= \frac{\chi(h)}{|G|} \sum_{g \in G} \overline{\chi}(g)gv$$
$$= \chi(h)v_\chi.$$

The $v_\chi$'s sum up to $v$:

$$\sum_\chi v_\chi = \sum_\chi \frac{1}{|G|} \sum_{g \in G} \overline{\chi}(g)gv = \frac{1}{|G|} \sum_{g \in G} \sum_\chi \overline{\chi}(g)gv = \frac{1}{|G|} \sum_{g \in G} \left(\sum_\chi \overline{\chi}(g)
ight) gv.$$

The inner sum is 0 unless $\chi$ is trivial, at which the inner sum is $|\widehat{G}|$, which equals $|G|$, so $\sum_\chi v_\chi = (1/|G|)|G|v = v$. Thus $V = \sum_\chi V(\chi)$.

To show the sum of the subspaces $V(\chi)$ is a direct sum means showing that if $\sum_\chi w_\chi = 0$ for $w_\chi \in V(\chi)$, then each $w_\chi$ is 0. Pick $g \in G$ and $\psi \in \widehat{G}$. Let $g$ act on both sides of the equation $0 = \sum_\chi w_\chi$, so $0 = \sum_\chi gw_\chi = \sum_\chi \chi(g)w_\chi$ since $w_\chi \in V(\chi)$. Multiplying through this equation by $\overline{\psi}(g)$, $0 = \sum_\chi \chi(g)\overline{\psi}(g)w_\chi$. Sum both sides over all $g$ in $G$:

$$0 = \sum_g \sum_\chi \chi(g)\overline{\psi}(g)w_\chi = \sum_\chi \left(\sum_g \chi(g)\overline{\psi}(g)
ight) w_\chi.$$

The coefficient of $w_\chi$ on the right is 0 unless $\chi = \psi$, when the coefficient is $|G|$. Therefore $0 = |G|w_\psi$. Since $|G| \neq 0$ in $\mathbf{C}$, we get $w_\psi = 0$ and this holds for each $\psi$ in $\widehat{G}$. That proves the decomposition $V = \sum_\chi V(\chi)$ is a direct sum decomposition. $\square$

**Example 9.4.** Let $|G| = 2$, with $G = \{1, \varepsilon\}$ and $\widehat{G} = \{\mathbf{1}_G, \chi\}$. Then $\chi(1) = 1$ and $\chi(\varepsilon) = -1$, so (9.2) in this case says each $v \in V$ is $v_{\mathbf{1}_G} + v_\chi$, where $v_{\mathbf{1}_G} = (v + \varepsilon v)/2$ and $v_\chi = (v - \varepsilon v)/2$, which satisfy $\varepsilon v_{\mathbf{1}_G} = v_{\mathbf{1}_G}$ and $\varepsilon v_\chi = -v_\chi$. This decomposition of $v$ into two parts is just like the even/odd decompositions at the start of this section.

**Example 9.5.** Consider the interior scaling action of $\mu_n$ on functions $\mathbf{C} \to \mathbf{C}$ in Example 9.1. The characters of $\mu_n$ are the power functions $\chi_j(r) = r^j$ for $j = 0, \ldots, n-1$ and $V(\chi_j) = \{f \in V: f(rz) = r^j f(z) \text{ for all } z \in \mathbf{C}\}$. Each $f: \mathbf{C} \to \mathbf{C}$ is a sum $\sum_{j=0}^{n-1} f_j$ where $f_j(rz) = r^j f(z)$ for all $z \in \mathbf{C}$ and by (9.2)

(9.3)
$$f_j(z) = \frac{1}{n} \sum_{r \in \mu_n} \overline{\chi_j}(r)(r \cdot f)(z) = \frac{1}{n} \sum_{r \in \mu_n} r^{-j} f(rz).$$

When $n = 2$ this says $f(z) = f_0(z) + f_1(z)$ where $f_0(z) = (f(z) - f(-z))/2$ is even and $f_1(z) = (f(z) - f(-z))/2$ is odd.

<!-- page 30 -->

When $n = 4$ this says $f(z) = f_0(z) + f_1(z) + f_2(z) + f_3(z)$ where $f_0(iz) = f_0(z)$, $f_1(iz) = if_1(z)$, $f_2(iz) = -f_2(z)$, and $f_3(z) = -if_3(z)$. Here are formulas for each of these functions, as special cases of (9.3):

$$f_0(z) = \frac{f(z) + f(iz) + f(-z) + f(-iz)}{4},$$
$$f_1(z) = \frac{f(z) - if(iz) - f(-z) + if(-iz)}{4},$$
$$f_2(z) = \frac{f(z) - f(iz) + f(-z) - f(-iz)}{4},$$
$$f_3(z) = \frac{f(z) + if(iz) - f(-z) - if(-iz)}{4}.$$

**Example 9.6.** For the exterior scaling action of $\mu_n$ on functions $\mathbf{C} \to \mathbf{C}$ in Example 9.2, where $\mu_n$ has characters $\chi_j(r) = r^j$ for $j = 0, \ldots, n-1$, the $\chi_j$-eigenspace

$$V(\chi_j) = \{f \in V: rf(z) = r^j f(z) \text{ for all } z \in \mathbf{C}\}$$

vanishes for nontrivial $\chi_j$: when $1 \leq j \leq n-1$ and $r$ is a nontrivial $n$th root of unity, $r \neq r^j$, so the only way $rf(z) = r^j f(z)$ is if $f(z) = 0$. Easily $V = V(\mathbf{1}) = \{f \in V: rf(z) = rf(z) \text{ for all } z \in \mathbf{C}\}$.

As an example, take $n = 2$ and $R: \mathbf{C} \to \mathbf{C}$ by $R(z) = -z$, so $R$ has order 2. (If we view $\mathbf{C}$ as $\mathbf{R}^2$ then this is a 180-degree rotation of the plane.) The group $G = \{I, R\}$ of order 2 acts linearly on $\mathbf{C}$ and the whole space "looks odd" under the effect of $R$: when $\chi$ is the nontrivial character of $G$, $\mathbf{C}(\mathbf{1}) = \mathbf{C}$ and $\mathbf{C}(\chi) = \{0\}$.

Exercises.

1. Let $V = \{aX + bX^2: a, b \in \mathbf{C}\}$, on which $G = \mathbf{Z}/(4)$ acts by interior scaling: $(r \cdot f)(X) = f(rX)$. Let $\chi_j(r) = r^j$ for $0 \leq j \leq 3$ and show $V(\chi_0) = V(\chi_3) = \{0\}$ while $V(\chi_1) = \mathbf{C}X$ and $V(\chi_2) = \mathbf{C}X^2$.

2. This exercise builds on Exercise 1.1, which is about characters of $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$.

a) When $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$ acts linearly on a complex vector space $V$, compute $v_\chi$ for each $v \in V$ and character $\chi$ of $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$.

b) Let $V = \mathbf{C}(X)$ be the rational functions over $\mathbf{C}$ and define two linear mappings $\sigma: V \to V$ and $\tau: V \to V$ by $\sigma(f(X)) = f(-X)$ and $\tau(f(X)) = f(1/X)$. Each has order 2 and $\sigmatau = \tau\sigma$ is the linear map $f(X) \mapsto f(-1/X)$. The group $G = \langle \sigma, \tau \rangle = \{1, \sigma, \tau, \sigmatau\}$ is isomorphic to $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$, so the action of $G$ on $\mathbf{C}(X)$ can be regarded as a linear action of $\mathbf{Z}/(2) \times \mathbf{Z}/(2)$ on $\mathbf{C}(X)$.

For each $f(X) \in \mathbf{C}(X)$, compute formulas for $f_\chi$ where $\chi$ runs through the characters of $G$ and check directly that the effect of $g$ on $f_\chi(X)$ is $\chi(g)f(X)$ for each $g \in G$.


## Appendix A. All Orders and Maximal Order

We will use characters of finite abelian groups to prove that in a finite abelian group $G$, the order of each element of $G$ divides the maximal order of the elements of $G$. Although this result can proved in a shorter way without characters, the point here is to see characters used.

<!-- page 31 -->

**Lemma A.1.** *For positive $d$ and $m$ with $d \mid m$, the natural reduction $(\mathbf{Z}/(m))^\times \to (\mathbf{Z}/(d))^\times$ is onto: when $(a, d) = 1$, there is $b$ such that $b \equiv a \bmod d$ and $(b, m) = 1$.*

*Proof.* Let $\widetilde{d}$ be the product of the prime powers in $m$ whose primes divide $d$, so $m = \widetilde{d}n$ with $(\widetilde{d}, n) = 1$. (For example, if $m = 90$ and $d = 6$ then $\widetilde{d} = 18$ and $n = 5$.) Then $d \mid \widetilde{d}$. By the Chinese remainder theorem we can find $b \in \mathbf{Z}$ satisfying

$$b \equiv a \bmod \widetilde{d}, \quad b \equiv 1 \bmod n.$$

Then $b \equiv a \bmod d$ and $b$ is relatively prime to $m$ since it is relatively prime to $d$ (a factor of $\widetilde{d}$) and to $n$. $\square$

**Lemma A.2.** *Let $G$ be a finite abelian group. If $x \in G$ has order $m$ and $y \in G$ has order $n$ then there is a character $\chi: G \to S^1$ such that $\chi(x)$ has order $m$ and $\chi(y)$ has order $n$.*

*Proof.* The subgroup $\langle x \rangle$ is cyclic of order $m$, so there is an isomorphism $\chi: \langle x \rangle \cong \mu_m$. In particular, $\chi(x)$ has order $m$. Following the proof of Lemma 3.2, we can extend $\chi$ to a character on $\langle x, y \rangle$ (and then all the way up to $G$) by sending $y$ to a solution $z \in S^1$ of the equation $z^d = \chi(y^d)$, where $d \geq 1$ is minimal such that $y^d \in \langle x \rangle$. We will show $z$ can be picked to have order $n$ in $S^1$.

Since $y^n = 1 \in \langle x \rangle$, $d$ divides $n$. Then $y^d$ has order $n/d$, so $\chi(y^d)$ has order $n/d$ because $\chi$ is one-to-one on $\langle x \rangle$. Write $\chi(y^d) = e^{2\pi i\ell/(n/d)} = e^{2\pi i\ell d/n}$, where $(\ell, n/d) = 1$. By Lemma A.1, there is an $\ell' \equiv \ell \bmod n/d$ such that $(\ell', n) = 1$. Since $\ell'd \equiv \ell d \bmod n$, $\chi(y^d) = e^{2\pi i\ell'd/n}$. Set $z = e^{2\pi i\ell'/n}$, which has order $n$. Since $z^k = \chi(y^d)$, we can set $\chi(y) = z$. $\square$

Lemma A.2 does not extend to more than two arbitrary elements in $G$. For instance, if $G = \mu_2 \times \mu_2$ then no character on $G$ sends all three non-identity elements in $G$ to $-1$. (Why?)

**Theorem A.3.** *Let $G$ be a finite abelian group. The order of each element in $G$ divides the maximal order of the elements of $G$.*

*Proof.* We will show that when $G$ has elements of orders $m$ and $n$, there is an element of $G$ of order $[m, n]$. Then if $m$ is the maximal order among all the elements of $G$, and $n$ is the order of some element of $G$, $[m, n]$ is the order of some element so $[m, n] \leq m$. That inequality can only occur when $[m, n] = m$, so $n \mid m$, which is what we want to show.

By Lemma A.2, there is a character $\chi$ on $G$ such that $\chi(g)$ has order $m$ and $\chi(h)$ has order $n$. Write $\chi(g) = e^{2\pi ia/m}$ and $\chi(h) = e^{2\pi ib/n}$, where $(a, m) = 1$ and $(b, n) = 1$.

The roots of unity $e^{2\pi i/m}$ and $e^{2\pi i/n}$ are in $\chi(G)$. For instance, letting $aa' \equiv 1 \bmod m$, $\chi(g^{a'}) = \chi(g)^{a'} = e^{2\pi iaa'/m} = e^{2\pi i/m}$. The argument for $e^{2\pi i/n}$ is similar. Write $mu + nv = (m, n)$ for some integers $u$ and $v$, so the equation $mn = [m, n](m, n)$ can be rewritten as

$$\frac{1}{[m, n]} = \frac{(m, n)}{mn} = \frac{mu + nv}{mn} = u\frac{1}{n} + v\frac{1}{m}.$$

Thus

$$e^{2\pi i/[m,n]} = (e^{2\pi i/n})^u(e^{2\pi i/m})^v \in \chi(G),$$

say $e^{2\pi i/[m,n]} = \chi(t)$. The order of $t$ in $G$ is divisible by the order of $\chi(t)$ in $S^1$, so $t$ has order divisible by $[m, n]$. Thus, raising $t$ to a suitable power, we obtain an element of $G$ with order $[m, n]$. $\square$


## Appendix B. Functions of Two Variables

<!-- page 32 -->

When analyzing a function of several variables, it is a common theme to decompose it into a sum of products of functions of one variable. For instance, to solve a PDE like the heat equation $\partial_t u - c\partial_x^2 u = 0$, first separable solutions of the form $u(x, t) = g(x)h(t)$ are classified. It is too much to hope that a general solution is separable, but in nice situations there are theorems guaranteeing that a general solution can be written as an infinite series of separable solutions: $u(x, t) = \sum_{n \geq 1} g_n(x)h_n(t)$. This is where expansions in Fourier series first appeared in mathematics.

Using characters, and in particular Parseval's formula, we will give an example of a function of two variables that is provably not a sum of products of functions of one variable.

**Lemma B.1.** *Fix a positive integer $N$. For vectors $(z_1, \ldots, z_N)$ and $(w_1, \ldots, w_N)$ in $\mathbf{C}^N$,*

$$\left|\sum_{j,k=1}^N e^{-2\pi ijk/N} z_j w_k
ight| \leq \sqrt{N} \left(\sum_{j=1}^N |z_j|^2
ight)^{1/2} \left(\sum_{k=1}^N |w_k|^2
ight)^{1/2}.$$

*Proof.* Write the double sum as an iterated single sum:

$$\sum_{j,k=1}^N e^{-2\pi ijk/N} z_j w_k = \sum_{j=1}^N \left(\sum_{k=1}^N e^{-2\pi ijk/N} w_k
ight) z_j = \sum_{j=1}^N \widehat{f}(j) z_j,$$

where $f: \mathbf{Z}/(N) \to \mathbf{C}$ by $f(k) = w_k$. The right side brings in the Fourier transform of $f$, where we think about $\widehat{f}$ as a function on $\mathbf{Z}/(N)$ by identifying $\mathbf{Z}/(N)$ with its own dual group as in Exercise 3.1.

Using the Cauchy-Schwarz inequality,

$$\left|\sum_{j=1}^N \widehat{f}(j) z_j
ight| \leq \left(\sum_{j=1}^N |\widehat{f}(j)|^2
ight)^{1/2} \left(\sum_{j=1}^N |z_j|^2
ight)^{1/2}.$$

By Parseval's formula on $\mathbf{Z}/(N)$, $\sum_{j=1}^N |\widehat{f}(j)|^2 = N \sum_{k=1}^N |f(k)|^2 = N \sum_{k=1}^N |w_k|^2$. $\square$

**Theorem B.2.** *It is impossible to write*

$$e^{2\pi ixk} = \sum_{n \geq 1} g_n(x)h_n(k),$$

*where $x \in [0, 1]$, $k \in \mathbf{Z}$, the functions $g_n: [0, 1] \to \mathbf{C}$ and $h_n: \mathbf{Z} \to \mathbf{C}$ are each bounded, and $\sum_{n \geq 1} \|g_n\|_{\sup}\|h_n\|_{\sup} < \infty$, where $\|\cdot\|_{\sup}$ is the sup-norm on bounded functions.*

*Proof.* Assume there is a series expansion

$$e^{2\pi ixk} = \sum_{n \geq 1} g_n(x)h_n(k)$$

for all $x \in [0, 1]$ and $k \in \mathbf{Z}$, where $c := \sum_{n \geq 1} \|g_n\|_{\sup}\|h_n\|_{\sup} < \infty$. Then the series is absolutely convergent for all $x$ and $k$. Pick $N \geq 1$ and $x_1, \ldots, x_N \in [0, 1]$. Then

$$\sum_{j,k=1}^N e^{-2\pi ijk/N} e^{2\pi ix_j k} = \sum_{j,k=1}^N e^{-2\pi ijk/N} \left(\sum_{n \geq 1} g_n(x_j)h_n(k)
ight) = \sum_{n \geq 1} \sum_{j,k=1}^N e^{-2\pi ijk/N} g_n(x_j)h_n(k).$$

<!-- page 33 -->

Then

$$\left|\sum_{j,k=1}^N e^{-2\pi ijk/N} e^{2\pi ix_j k}
ight| = \left|\sum_{n \geq 1} \sum_{j,k=1}^N e^{-2\pi ijk/N} g_n(x_j)h_n(k)
ight|$$
$$\leq \sum_{n \geq 1} \left|\sum_{j,k=1}^N e^{-2\pi ijk/N} g_n(x_j)h_n(k)
ight|$$
$$\leq \sum_{n \geq 1} \sqrt{N} \left(\sum_{j=1}^N |g_n(x_j)|^2
ight)^{1/2} \left(\sum_{k=1}^N |h_n(k)|^2
ight)^{1/2}$$

by Lemma B.1. Since $\sum_{j=1}^N |g_n(x_j)|^2 \leq N\|g_n\|_{\sup}^2$ and $\sum_{k=1}^N |h_n(k)|^2 \leq N\|h_n\|_{\sup}^2$,

$$\left|\sum_{j,k=1}^N e^{-2\pi ijk/N} e^{2\pi ix_j k}
ight| \leq \sum_{n \geq 1} \sqrt{N}\sqrt{N}\|g_n\|_{\sup}\sqrt{N}\|h_n\|_{\sup} \leq N^{3/2}c.$$

Now set $x_j = j/N$:

$$\sum_{j,k=1}^N e^{-2\pi ijk/N} e^{2\pi ix_j k} = \sum_{j,k=1}^N e^{-2\pi ijk/N} e^{2\pi ijk/N} = N^2,$$

so $N^2 \leq N^{3/2}c$ for all $N \geq 1$. This is false when $N$ is large enough ($N > c^2$). $\square$

This theorem says we can't write $e^{2\pi ixk} = \sum_{n \geq 1} g_n(x)h_n(k)$ where the functions $g_n$ and $h_n$ are bounded and the series converges absolutely (since convergence of $\sum_{n \geq 1} \|g_n\|_{\sup}\|h_n\|_{\sup}$ implies absolute convergence). Could there be such a series representation of $e^{2\pi ixk}$ that is conditionally convergent?


## References

[1] A. Terras, "Fourier Analysis on Finite Groups and Applications," Cambridge Univ. Press, Cambridge, 1999.

[2] P. Shor, *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*, https://arxiv.org/abs/quant-ph/9508027v2.

[3] W. Trappe and L. Washington, "Introduction to Cryptography with Coding Theory," Prentice-Hall, Upper Saddle River, NJ 2002.

[4] L. Washington, "Introduction to Cyclotomic Fields," 2nd ed., Springer-Verlag, New York, 2000.

[5] N. Wiener, "I am a Mathematician," MIT Press, Cambridge, 1964.

---

## Footnotes

[^3]: At $k = 0$, the equation is $y^2 = x^3$, which has infinitely many integral solutions $(x, y) = (t^2, t^3)$ for $t \in \mathbf{Z}$.

[^4]: See https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf for many proofs of this.

[^5]: If $F$ is any field, the solutions of $y^2 = x^3$ in $F$ are all of the form $(t^2, t^3)$ as $t$ runs over $F$: if $x \neq 0$, set $t = y/x \neq 0$, so $t^2 = y^2/x^2 = x^3/x^2 = x$ and $t^3 = y^3/x^3 = y^3/y^2 = y$. That shows all solutions $(x, y)$ where $x \neq 0$ have the form $(t^2, t^3)$ where $t \in F^\times$, and $(0, 0)$ also has that form with $t = 0$.

[^6]: See Corollary 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

[^7]: See Theorem 2.5 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

[^8]: See Corollary 2.4 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf.

[^9]: This is called a representation of $G$ on $V$.

