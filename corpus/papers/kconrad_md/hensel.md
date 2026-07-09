# Hensel's Lemma

> **Source**: https://kconrad.math.uconn.edu/blurbs/hensel.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
# Hensel's Lemma

**Keith Conrad**

## 1. Introduction

In the $p$-adic integers, congruences are approximations: for $a$ and $b$ in $\mathbf{Z}_p$, $a \equiv b \bmod p^n$ is the same as $|a - b|_p \leq 1/p^n$. Turning information modulo one power of $p$ into similar information modulo a higher power of $p$ can be interpreted as improving an approximation.

**Example 1.1.** The number 7 is a square mod 3: $7 \equiv 1^2 \bmod 3$. Although $7 \not\equiv 1^2 \bmod 9$, we can write 7 as a square mod 9 by replacing 1 with $1 + 3$: $7 \equiv (1 + 3)^2 \bmod 9$. Here are expressions of 7 as a square modulo further powers of 3:

$$7 \equiv (1 + 3 + 3^2)^2 \bmod 3^3,$$
$$7 \equiv (1 + 3 + 3^2)^2 \bmod 3^4,$$
$$7 \equiv (1 + 3 + 3^2 + 2 \cdot 3^4)^2 \bmod 3^5,$$
$$\dots$$
$$7 \equiv (1 + 3 + 3^2 + 2 \cdot 3^4 + 2 \cdot 3^7 + 3^8 + 3^9 + 2 \cdot 3^{10})^2 \bmod 3^{11}.$$

If we can keep going indefinitely then 7 is a perfect square in $\mathbf{Z}_3$ with square root

$$1 + 3 + 3^2 + 2 \cdot 3^4 + 2 \cdot 3^7 + 3^8 + 3^9 + 2 \cdot 3^{10} + \cdots.$$

That we can continue this indefinitely is due to Hensel's lemma, proved by Hensel in 1904 [4, Sect. 4, pp. 77-84] (see also [5, Chap. 4, Sect. 3-5]). It gives conditions under which the root of a polynomial mod $p$ lifts to a root in $\mathbf{Z}_p$, such as the polynomial $X^2 - 7$ with $p = 3$: its two roots mod 3 can both be lifted to square roots of 7 in $\mathbf{Z}_3$.

We will first give a basic version of Hensel's lemma, illustrate it with examples, and then other versions that can be applied in cases where the basic version is inadequate.

## 2. A Basic Version of Hensel's Lemma

**Theorem 2.1 (Hensel's lemma).** *If $f(X) \in \mathbf{Z}_p[X]$ and $a \in \mathbf{Z}_p$ satisfies*

$$f(a) \equiv 0 \bmod p, \quad f'(a) \not\equiv 0 \bmod p$$

*then there is a unique $\alpha \in \mathbf{Z}_p$ such that $f(\alpha) = 0$ in $\mathbf{Z}_p$ and $\alpha \equiv a \bmod p$.*

**Example 2.2.** Let $f(X) = X^2 - 7$. Then $f(1) = -6 \equiv 0 \bmod 3$ and $f'(1) = 2 \not\equiv 0 \bmod 3$, so Hensel's lemma tells us there is a unique 3-adic integer $\alpha$ such that $\alpha^2 = 7$ and $\alpha \equiv 1 \bmod 3$. We saw approximations to $\alpha$ in Example 1.1, *e.g.*, $\alpha \equiv 1 + 3 + 3^2 + 2 \cdot 3^4 \bmod 3^5$.

*Proof.* We will prove by induction that for each $n \geq 1$ there is an $a_n \in \mathbf{Z}_p$ such that

- $f(a_n) \equiv 0 \bmod p^n$,
- $a_n \equiv a \bmod p$.

(After proving this, we'll show it leads to a solution of $f(\alpha) = 0$ as a limit.) The case $n = 1$ is trivial, using $a_1 = a$. If the inductive hypothesis holds for $n$, we seek $a_{n+1} \in \mathbf{Z}_p$ such that

- $f(a_{n+1}) \equiv 0 \bmod p^{n+1}$,
- $a_{n+1} \equiv a \bmod p$.

<!-- page 2 -->

Since $f(a_{n+1}) \equiv 0 \bmod p^{n+1} \Rightarrow f(a_{n+1}) \equiv 0 \bmod p^n$, each root of $f(X) \bmod p^{n+1}$ reduces to a root of $f(X) \bmod p^n$. By the inductive hypothesis there is a root $a_n \bmod p^n$ such that $a_n \equiv a \bmod p$, so we seek a $p$-adic integer $a_{n+1}$ such that $a_{n+1} \equiv a_n \bmod p^n$ and $f(a_{n+1}) \equiv 0 \bmod p^{n+1}$. Writing

$$a_{n+1} = a_n + p^n t_n$$

for some $t_n \in \mathbf{Z}_p$ to be determined, can we make $f(a_n + p^n t_n) \equiv 0 \bmod p^{n+1}$?

To compute $f(a_n + p^n t_n) \bmod p^{n+1}$, we use a polynomial identity:

$$f(X + Y) = f(X) + f'(X)Y + g(X, Y)Y^2 \tag{2.1}$$

for some polynomial $g(X, Y) \in \mathbf{Z}_p[X, Y]$. This formula comes from isolating the first two terms in the binomial theorem: writing $f(X) = \sum_{i=0}^d c_i X^i$ we have

$$f(X + Y) = \sum_{i=0}^d c_i(X + Y)^i = c_0 + \sum_{i=1}^d (c_i(X^i + iX^{i-1}Y) + g_i(X, Y)Y^2),$$

where $g_i(X, Y) \in \mathbf{Z}[X, Y]$. Thus

$$f(X + Y) = \sum_{i=0}^d c_i X^i + \sum_{i=1}^d i c_i X^{i-1} Y + \sum_{i=1}^d g_i(X, Y) Y^2 = f(X) + f'(X)Y + g(X, Y)Y^2,$$

where $g(X, Y) = \sum_{i=1}^d c_i g_i(X, Y) \in \mathbf{Z}_p[X, Y]$. This gives us the desired identity.[^1]

To make (2.1) numerical, for all $x$ and $y$ in $\mathbf{Z}_p$ the number $z := g(x, y)$ is in $\mathbf{Z}_p$, so

$$x, y \in \mathbf{Z}_p \implies f(x + y) = f(x) + f'(x)y + zy^2, \text{ where } z \in \mathbf{Z}_p. \tag{2.2}$$

In this formula set $x = a_n$ and $y = p^n t_n$:

$$f(a_n + p^n t_n) = f(a_n) + f'(a_n)p^n t_n + z p^{2n} t_n^2 \equiv f(a_n) + f'(a_n) p^n t_n \bmod p^{n+1} \tag{2.3}$$

since $2n \geq n + 1$.

In $f'(a_n)p^n t_n \bmod p^{n+1}$, the factors $f'(a_n)$ and $t_n$ only matter mod $p$ since there is already a factor of $p^n$ present and the modulus is $p^{n+1}$. Recalling that $a_n \equiv a \bmod p$, we get $f'(a_n)p^n t_n \equiv f'(a) p^n t_n \bmod p^{n+1}$. Therefore from (2.3),

$$f(a_n + p^n t_n) \equiv 0 \bmod p^{n+1} \iff f(a_n) + f'(a) p^n t_n \equiv 0 \bmod p^{n+1}$$
$$\iff f'(a) t_n \equiv -f(a_n)/p^n \bmod p, \tag{2.4}$$

where the ratio $f(a_n)/p^n$ is in $\mathbf{Z}_p$ since we assumed that $f(a_n) \equiv 0 \bmod p^n$. There is a solution for $t_n$ in (2.4), a congruence mod $p$, since we assume $f'(a) \not\equiv 0 \bmod p$.

Armed with this choice of $t_n$ and setting $a_{n+1} = a_n + p^n t_n$, we have $f(a_{n+1}) \equiv 0 \bmod p^{n+1}$ and $a_{n+1} \equiv a_n \bmod p^n$, so in particular $a_{n+1} \equiv a \bmod p$. This completes the induction.

Starting with $a_1 = a$, our inductive argument has constructed a sequence $a_1, a_2, a_3, \ldots$ in $\mathbf{Z}_p$ such that $f(a_n) \equiv 0 \bmod p^n$ and $a_{n+1} \equiv a_n \bmod p^n$ for all $n$. The second condition, $a_{n+1} \equiv a_n \bmod p^n$, implies that $\{a_n\}$ is a Cauchy sequence in $\mathbf{Z}_p$. Let $\alpha$ be its limit in $\mathbf{Z}_p$. We want to show $f(\alpha) = 0$ and $\alpha \equiv a \bmod p$.

From $a_{n+1} \equiv a_n \bmod p^n$ for all $n$ we get $\alpha \equiv a_n \bmod p^n$ for all $m > n$, so $\alpha \equiv a_n \bmod p^n$ by letting $m \to \infty$. At $n = 1$ we get $\alpha \equiv a \bmod p$. For general $n$,

$$\alpha \equiv a_n \bmod p^n \implies f(\alpha) \equiv f(a_n) \equiv 0 \bmod p^n \implies |f(\alpha)|_p \leq \frac{1}{p^n}.$$

[^1]: The identity (2.1) is similar to Taylor's formula: $f(x+h) = f(x) + f'(x)h + (f''(x)/2!)h^2 + \cdots$. The catch is that terms in Taylor's formula have factorials in the denominator, which can require some extra care when reducing modulo powers of $p$: think about $f''(x)/2! \bmod 2$, for instance. What (2.1) essentially does is extract the first two terms of Taylor's formula and say that what remains has $p$-adic integral coefficients, so (2.1) can be reduced mod $p$, or mod $p^n$ for all $n \geq 1$.

<!-- page 3 -->

Since this estimate holds for all $n$, $f(lpha) = 0$.

It remains to show \$lpha$ is the unique root of $f(X)$ in $\mathbf{Z}_p$ that is congruent to $a mod p$. Suppose $f(eta) = 0$ and $eta \equiv a mod p$. To show $eta = lpha$ we will show $eta \equiv lpha mod p^n$ for all $n$. The case $n = 1$ is clear since $lpha$ and $eta$ are both congruent to $a mod p$. Suppose $n \geq 1$ and we know that $eta \equiv lpha mod p^n$. Then $eta = lpha + p^n \gamma_n$ with $\gamma_n \in \mathbf{Z}_p$, so a calculation similar to (2.3) implies

$$f(eta) = f(lpha + p^n \gamma_n) \equiv f(lpha) + f'(lpha) p^n \gamma_n mod p^{n+1}.$$
<!-- page 3 -->

Since this estimate holds for all $n$, $f(lpha) = 0$.

It remains to show $lpha$ is the unique root of $f(X)$ in $\mathbf{Z}_p$ that is congruent to $a mod p$. Suppose $f(eta) = 0$ and $eta \equiv a mod p$. To show $eta = lpha$ we will show $eta \equiv lpha mod p^n$ for all $n$. The case $n = 1$ is clear since $lpha$ and $eta$ are both congruent to $a mod p$. Suppose $n \geq 1$ and we know that $eta \equiv lpha mod p^n$. Then $eta = lpha + p^n \gamma_n$ with $\gamma_n \in \mathbf{Z}_p$, so a calculation similar to (2.3) implies

$$f(eta) = f(lpha + p^n \gamma_n) \equiv f(lpha) + f'(lpha) p^n \gamma_n mod p^{n+1}.$$

Both $lpha$ and $eta$ are roots of $f(X)$, so $0 \equiv f'(lpha) p^n \gamma_n mod p^{n+1}$. Thus $f'(lpha) \gamma_n \equiv 0 mod p$. Since $f'(lpha) \equiv f'(a) 
ot\equiv 0 mod p$, we have $\gamma_n \equiv 0 mod p$, which implies $eta \equiv lpha mod p^{n+1}$. $\square$

**Remark 2.3.** Since $a_n + p^n t_n mod p^{n+1}$ only depends on $t_n mod p$, and $t_n$ satisfying (2.4) is unique mod $p$, the $a_n \in \mathbf{Z}_p$ where (i) $f(a_n) \equiv 0 mod p^n$ and (ii) $a_n \equiv a mod p$ is unique modulo $p^n$. Or an argument similar to the last paragraph in the proof shows for each $n \geq 1$ that $f(X)$ has a unique root mod $p^n$ that reduces to $a mod p$. Either way, in Theorem 2.1 we can think about the uniqueness of the lifting of the mod $p$ root in two ways: it has a unique lifting to a root in $\mathbf{Z}_p$ or it has a unique lifting to a root in $\mathbf{Z}_p/(p^n)$ for all $n \geq 1$.

**Remark 2.4.** If $f(X) \in \mathbf{Z}[X]$ and $a \in \mathbf{Z}$, then $g(X, Y)$ in (2.1) is in $\mathbf{Z}[X, Y]$ and $z$ in (2.2) is in $\mathbf{Z}$. Use this to check that the inductive reasoning used in the proof before passing to a $p$-adic limit near the end holds with $\mathbf{Z}$ in place of $\mathbf{Z}_p$, so for all $n \geq 1$ there is an $a_n \in \mathbf{Z}$ such that $f(a_n) \equiv 0 mod p^n$ and $a_n \equiv a mod p$, and such $a_n$ is unique in $\mathbf{Z}/(p^n)$.

The rest of this section has applications of Hensel's lemma. The hypotheses $f(a) \equiv 0 mod p$ and $f'(a) 
ot\equiv 0 mod p$ in Hensel's lemma are equivalent to saying $a mod p$ is a *simple root* of $f(X) mod p$: $f(X) \equiv (X - a)g(X) mod p$ where $g(a) 
ot\equiv 0 mod p$.

**Example 2.5.** Let $f(X) = X^3 - 2$. We have $f(3) \equiv 0 mod 5$ and $f'(3) 
ot\equiv 0 mod 5$, or $X^3 - 2 \equiv (X - 3)(X^2 + 3X + 9) mod 5$ where the second factor does not vanish at 3 mod 5. By Hensel's lemma with $a = 3$ there is a unique cube root of 2 in $\mathbf{Z}_5$ that is congruent to 3 mod 5. It is $3 + 2 \cdot 5^2 + 2 \cdot 5^3 + \cdots$. Since $X^3 - 2 \equiv (X - 4)(X - 7)(X - 20) mod 31$, by Hensel's lemma there are three cube roots of 2 in $\mathbf{Z}_{31}$ and they are distinguished by their values modulo 31. These numbers begin as $4 + 9 \cdot 31 + 4 \cdot 31^2 + \cdots$, $7 + 13 \cdot 31 + 29 \cdot 31^2 + \cdots$, and $20 + 8 \cdot 31 + 28 \cdot 31^2 + \cdots$.

**Example 2.6.** Let $f(X) = X^3 - X^2 - 2 \equiv X^3 - X^2 \equiv X^2(X - 1) mod 2$, so $f(0) \equiv 0 mod 2$ and $f'(0) \equiv 0 mod 2$, while $f(1) \equiv 0 mod 2$ and $f'(1) 
ot\equiv 0 mod 2$: 0 is a multiple root mod 2 and 1 is a simple root mod 2. By Hensel's lemma with $a = 1$, there is a unique $lpha \in \mathbf{Z}_2$ such that $f(lpha) = 0$ and $lpha \equiv 1 mod 2$. Explicitly, $lpha = 1 + 2 + 2^4 + 2^5 + 2^{10} + \cdots$.

Although 0 is a root of $f(X) mod 2$, it does *not* lift to a root in $\mathbf{Z}_2$ since it does not even lift to a root mod 4: $f(0) \equiv 2 mod 4$ and $f(2) \equiv 2 mod 4$, so if $eta \in \mathbf{Z}_2$ and $eta \equiv 0 mod 2$ then $eta \equiv 0$ or $2 mod 4$ and therefore $f(eta) \equiv 2 
ot\equiv 0 mod 4$.

**Example 2.7.** Let $f(X) = X^3 - X^2 - 2X - 8 \equiv X^3 - X^2 \equiv X^2(X - 1) mod 2$. As in the previous example, 0 is a multiple root mod 2 and 1 is a simple root mod 2, so Hensel's lemma with $a = 1$ tells us $f(X)$ has a unique root $lpha \in \mathbf{Z}_2$ such that $lpha \equiv 1 mod 2$. Explicitly, $lpha = 1 + 2 + 2^2 + 2^4 + 2^6 + 2^9 + \cdots$.

Unlike the previous example, the multiple root 0 mod 2 lifts to roots in $\mathbf{Z}_2$, in fact to two of them, but we cannot explain this with the basic version of Hensel's lemma. We will return to this example in Example 4.4 after meeting a stronger version of Hensel's lemma.

**Example 2.8.** For each positive integer $n$ *not* divisible by $p$ and each $u \equiv 1 mod p\mathbf{Z}_p$, $u$ is an $n$th power in $\mathbf{Z}_p^	imes$. Apply Hensel's lemma to $f(X) = X^n - u$ with $a = 1$: $f(1) = 1 - u \equiv 0 mod p$ and $f'(1) = n 
ot\equiv 0 mod p$. Therefore there is a unique solution to $lpha^n = u$ in $\mathbf{Z}_p$ such that $lpha \equiv 1 mod p$. Example 1.1 is the case $u = 7$, $p = 3$, and $n = 2$: 7 has a unique 3-adic square root that is $\equiv 1 mod 3$.

<!-- page 4 -->

**Example 2.9.** For an *odd* prime $p$, suppose $u \in \mathbf{Z}_p^	imes$ is a square mod $p$. We will show $u$ is a square in $\mathbf{Z}_p^	imes$. For example, $2 \equiv 3^2 mod 7$ and that implies 2 is a square in $\mathbf{Z}_7^	imes$.

Write $u \equiv a^2 mod p$, so $a 
ot\equiv 0 mod p$. For the polynomial $f(X) = X^2 - u$ we have $f(a) \equiv 0 mod p$ and $f'(a) = 2a 
ot\equiv 0 mod p$, since $p$ is not 2, so Hensel's lemma tells us that $f(X)$ has a root in $\mathbf{Z}_p$ that reduces to $a mod p$, which means $u$ is a square in $\mathbf{Z}_p^	imes$. Conversely, if $u \in \mathbf{Z}_p^	imes$ is a $p$-adic square, say $u = v^2$, then $1 = |v|_p^2$, so $v \in \mathbf{Z}_p^	imes$ and $u \equiv v^2 mod p$. Thus the elements of $\mathbf{Z}_p^	imes$ that are squares in $\mathbf{Q}_p$ are precisely those that reduce to squares mod $p$. For example, the nonzero squares mod 7 are 1, 2, and 4, so $u \in \mathbf{Z}_7^	imes$ is a 7-adic square if and only if $u \equiv 1, 2, 	ext{or } 4 mod 7$.

This result can have problems when $p = 2$ because $2a \equiv 0 mod 2$. In fact the lifting of a square root mod 2 to a 2-adic square root really does have a problem: $3 \equiv 1^2 mod 2$ but 3 is not a square in $\mathbf{Z}_2$ since 3 is not a square mod 4 (the squares mod 4 are 0 and 1). And 3 is not a square in $\mathbf{Q}_2$ either because a hypothetical square root in $\mathbf{Q}_2$ would have to be in $\mathbf{Z}_2$: if $lpha^2 = 3$ in $\mathbf{Q}_2$ then $|lpha|_2^2 = |3|_2 = 1$, so $|lpha|_2 = 1$, and thus $lpha \in \mathbf{Z}_2^	imes \subset \mathbf{Z}_2$.

**Example 2.10.** For each integer $k$ between 0 and $p - 1$, $k^p \equiv k mod p$. Letting $f(X) = X^p - X$, we have $f(k) \equiv 0 mod p$ and $f'(k) = pk^{p-1} - 1 \equiv -1 
ot\equiv 0 mod p$. By Hensel's lemma there is a unique $\omega_k \in \mathbf{Z}_p$ such that $\omega_k^p = \omega_k$ and $\omega_k \equiv k mod p$. For instance, always $\omega_0 = 0$ and $\omega_1 = 1$, and when $p > 2$, $\omega_{p-1} = -1$. Other $\omega_k$ for $p > 2$ are more interesting. For $p = 5$, $\omega_k$ is a root of $X^5 - X = X(X^4 - 1) = X(X - 1)(X + 1)(X^2 + 1)$. Thus $\omega_2$ and $\omega_3$ in $\mathbf{Z}_5$ are square roots of $-1$:[^2]

$$\omega_2 = 2 + 5 + 2 \cdot 5^2 + 5^3 + 3 \cdot 5^4 + 4 \cdot 5^5 + 2 \cdot 5^6 + 3 \cdot 5^7 + \cdots,$$
$$\omega_3 = 3 + 3 \cdot 5 + 2 \cdot 5^2 + 3 \cdot 5^3 + 5^4 + 2 \cdot 5^6 + 5^7 + \cdots.$$

For general $p$ the numbers $\omega_k$ for $0 \leq k \leq p - 1$ are distinct since they are already distinct when reduced mod $p$, so $X^p - X = X(X^{p-1} - 1)$ splits completely in $\mathbf{Z}_p[X]$. Its roots in $\mathbf{Z}_p$ are 0 and $(p-1)$th roots of unity. The number $\omega_k$ in $\mathbf{Z}_p$ is called the ($p$-adic) *Teichmuller representative* for $k$: $\omega_k$ is the unique lifting of $k mod p$ to a root of $X^p - X$ in $\mathbf{Z}_p$.

**Example 2.11.** As an application to solving equations in $\mathbf{Q}_p$, not just $\mathbf{Z}_p$, for $p 
eq 2$ and $a \in \mathbf{Q}_p$ we will show the equation $y^2 = x^4 + a$ has a $p$-adic solution $(x, y)$ whenever $|x|_p$ is sufficiently large compared to $|a|_p$.

Rewrite the equation as $y^2 = x^4(1 + a/x^4)$. Since the first term $x^4$ is a square for all $x$, it suffices to find a condition on $x$ that implies $1 + a/x^4$ is a square in $\mathbf{Q}_p$. When $p 
eq 2$, such a condition is $|a/x^4|_p < 1$, *i.e.*, $|x|_p > |a|_p^{1/4}$: for such $x$, $a/x^4 \in p\mathbf{Z}_p$, so $1 + a/x^4 \equiv 1 mod p\mathbf{Z}_p$, and therefore $1 + a/x^4$ is a square in $\mathbf{Z}_p^	imes$ by Examples 2.8 or 2.9.

We will extend this to the case $p = 2$ in Example 4.6.

## 3. Roots of Unity in $\mathbf{Q}_p$ via Hensel's Lemma

Hensel's lemma is often considered to be a method of finding roots to polynomials, but the existence of a root is just one aspect. There is also a uniqueness part to Hensel's lemma: it tells us there is a unique root within a certain distance of an approximate root. We will use the uniqueness to find all of the roots of unity in $\mathbf{Q}_p$.

**Theorem 3.1.** *The roots of unity in $\mathbf{Q}_p$ are the $(p-1)$th roots of unity for $p$ odd and $\pm 1$ for $p = 2$.*

[^2]: Hensel found $\omega_2$ and $\omega_3$ to 4 digits when he factored $X^2 + 1$ over $\mathbf{Q}_5$, written by him as $K(5)$ [4, p. 77].

<!-- page 5 -->

*Proof.* If $x^n = 1$ in $\mathbf{Q}_p$ then $|x|_p^n = 1$, so $|x|_p = 1$. This means every root of unity in $\mathbf{Q}_p$ lies in $\mathbf{Z}_p^	imes$. Therefore we work in $\mathbf{Z}_p^	imes$ right from the start.

First let us consider roots of unity of order relatively prime to $p$. Assume $\zeta_1$ and $\zeta_2$ are roots of unity in $\mathbf{Z}_p^	imes$ with order prime to $p$. Letting $m$ be the product of the orders of these roots of unity, they are both roots of $f(X) = X^m - 1$ and $m$ is prime to $p$. Since $|f'(\zeta_i)|_p = |m\zeta_i^{m-1}|_p = 1$, the uniqueness aspect of Hensel's lemma implies that the only root $lpha$ of $X^m - 1$ satisfying $|lpha - \zeta_1|_p < 1$ is $\zeta_1$. So if $\zeta_2 \equiv \zeta_1 mod p\mathbf{Z}_p$ then $\zeta_2 = \zeta_1$: distinct roots of unity in $\mathbf{Z}_p^	imes$ having order prime to $p$ must be incongruent mod $p$. In Example 2.10 we found in each nonzero coset mod $p\mathbf{Z}_p$ a root of $X^{p-1} - 1$, and $p - 1$ is prime to $p$. Therefore each congruence class mod $p\mathbf{Z}_p$ contains a $(p-1)$th root of unity, so the only roots of unity of order prime to $p$ in $\mathbf{Q}_p$ are the roots of $X^{p-1} - 1$.

Now we consider roots of unity of $p$-power order. We will show the only $p$th root of unity in $\mathbf{Z}_p^	imes$ is 1 for odd $p$ and the only 4th roots of unity in $\mathbf{Z}_2^	imes$ are $\pm 1$. This implies the only $p$th power roots of unity in $\mathbf{Z}_p^	imes$ are 1 for odd $p$ and $\pm 1$ for $p = 2$. (For instance, if there were a nontrivial $p$-th power root of unity in $\mathbf{Q}_p$ for $p 
eq 2$ then there would be a root of unity in $\mathbf{Q}_p$ of order $p$, but we are going to show there are not any of those.) This part of the proof will not use Hensel's lemma.

We first consider odd $p$ and suppose $\zeta^p = 1$ in $\mathbf{Z}_p^	imes$ with $\zeta 
eq 1$. Since $\zeta^p \equiv \zeta mod p\mathbf{Z}_p$, we have $\zeta \equiv 1 mod p\mathbf{Z}_p$. Therefore $\zeta = 1 + py$ with $y \in \mathbf{Z}_p$. Since $\zeta$ is not 1, $\zeta$ is a root of $(X^p - 1)/(X - 1) = 1 + X + X^2 + \cdots + X^{p-1}$. For all integers $k \geq 0$, $\zeta^k = (1 + py)^k \equiv 1 + kpy mod p^2\mathbf{Z}_p$ by the binomial theorem, so

$$0 = 1 + \zeta + \zeta^2 + \cdots + \zeta^{p-1}$$
$$= \sum_{k=0}^{p-1} \zeta^k$$
$$\equiv \sum_{k=0}^{p-1} (1 + kpy) mod p^2\mathbf{Z}_p$$
$$\equiv p + rac{p(p-1)}{2} py mod p^2\mathbf{Z}_p. 	ag{3.1}$$

Since $p$ is odd, $(p-1)/2 \in \mathbf{Z}$, so (3.1) implies $0 \equiv p mod p^2$, which is a contradiction. Therefore there is no $p$th root of unity in $\mathbf{Q}_p$ other than 1.

Now we turn to $p = 2$. We want to show the only 4th roots of unity in $\mathbf{Z}_2^	imes$ are $\pm 1$. If $\zeta \in \mathbf{Z}_2^	imes$ is a 4th root of unity and $\zeta 
eq \pm 1$ then $\zeta^2 = -1$, so $\zeta^2 \equiv -1 mod 4\mathbf{Z}_2$. However,

$$\zeta \in \mathbf{Z}_2^	imes \implies \zeta \equiv 1 	ext{ or } 3 mod 4\mathbf{Z}_2 \implies \zeta^2 \equiv 1 mod 4\mathbf{Z}_2$$

and $1 
ot\equiv -1 mod 4\mathbf{Z}_2$. Thus there is no 4th root of unity in $\mathbf{Q}_2$ besides $\pm 1$.

For prime $p$, a root of unity is a (unique) product of a root of unity of $p$-power order and a root of unity of order prime to $p$, so the only roots of unity in $\mathbf{Q}_p$ are the roots of $X^{p-1} - 1$ for $p 
eq 2$ and $\pm 1$ for $p = 2$. $\square$

Here are the roots of $X^7 - X$ in $\mathbf{Z}_7$ besides $\omega_0 = 0$, $\omega_1 = 1$, and $\omega_6 = -1$.

$$\omega_2 = 2 + 4 \cdot 7 + 6 \cdot 7^2 + 3 \cdot 7^3 + 0 \cdot 7^4 + 2 \cdot 7^5 + 6 \cdot 7^6 + 2 \cdot 7^7 + \cdots,$$
$$\omega_3 = 3 + 4 \cdot 7 + 6 \cdot 7^2 + 3 \cdot 7^3 + 0 \cdot 7^4 + 2 \cdot 7^5 + 6 \cdot 7^6 + 2 \cdot 7^7 + \cdots,$$
$$\omega_4 = 4 + 2 \cdot 7 + 0 \cdot 7^2 + 3 \cdot 7^3 + 6 \cdot 7^4 + 4 \cdot 7^5 + 0 \cdot 7^6 + 4 \cdot 7^7 + \cdots,$$
$$\omega_5 = 5 + 2 \cdot 7 + 0 \cdot 7^2 + 3 \cdot 7^3 + 6 \cdot 7^4 + 4 \cdot 7^5 + 0 \cdot 7^6 + 4 \cdot 7^7 + \cdots.$$

<!-- page 6 -->

The 7-adic digits of $\omega_2$ and $\omega_3$ appear to be matching after the first digit, as do those in $\omega_4$ and $\omega_5$. More specifically, it looks like $\omega_3 - \omega_2 = 1$ and $\omega_5 - \omega_4 = 1$. Let us explain that from the factorization

$$X^7 - X = X(X^6 - 1) = X(X^3 - 1)(X^3 + 1) = X(X - 1)(X^2 + X + 1)(X + 1)(X^2 - X + 1).$$

Each $\omega_k$ is a root of one polynomial on the right side. Since $X^2 + X + 1$ has roots 2 mod 7 and 4 mod 7 in $\mathbf{Z}/(7)$, it has roots $\omega_2$ and $\omega_4$ in $\mathbf{Z}_7$. Its roots have sum $-1$ (why?), so $\omega_2 + \omega_4 = -1$. Also $\omega_2$ and $-\omega_5$ are both roots of $X^7 - X$ that reduce to 2 mod 7, so the uniqueness in Hensel's lemma implies $\omega_2 = -\omega_5$. Thus $\omega_5 - \omega_4 = -\omega_2 - (-1 - \omega_2) = 1$. It is left to the reader to explain why $\omega_3 - \omega_2 = 1$.

Using the roots of unity in $\mathbf{Q}_p$, the following theorem gives multiplicative decompositions of $\mathbf{Z}_p^	imes$ and $\mathbf{Q}_p^	imes$ that are analogues of $\mathbf{R}^	imes = \{\pm 1\} 	imes \mathbf{R}_{>0}$ and $\mathbf{C}^	imes = S^1 	imes \mathbf{R}_{>0}$. Write $\mu_n$ for the $n$th roots of unity.

**Theorem 3.2.** *For all $p$, $\mathbf{Z}_p^	imes = \mu_{p-1} 	imes (1 + p\mathbf{Z}_p)$ and $\mathbf{Q}_p^	imes = p^{\mathbf{Z}} 	imes \mathbf{Z}_p^	imes = p^{\mathbf{Z}} 	imes \mu_{p-1} 	imes (1 + p\mathbf{Z}_p)$. When $p = 2$, $\mathbf{Z}_2^	imes = \{\pm 1\} 	imes (1 + 4\mathbf{Z}_2)$ and $\mathbf{Q}_2^	imes = 2^{\mathbf{Z}} 	imes \mathbf{Z}_2^	imes = 2^{\mathbf{Z}} 	imes \{\pm 1\} 	imes (1 + 4\mathbf{Z}_2)$.*

*Proof.* Since $p^{\mathbf{Z}} 	imes \mathbf{Z}_p^	imes = \mathbf{Q}_p^	imes$ (by the map $(p^k, u) \mapsto p^k u$), it suffices to explain the decomposition $\mathbf{Z}_p^	imes = \mu_{p-1} 	imes (1 + p\mathbf{Z}_p)$ for all $p$ and $\mathbf{Z}_2^	imes = \{\pm 1\} 	imes (1 + 4\mathbf{Z}_2)$.

For each $u \in \mathbf{Z}_p^	imes$, Example 2.10 says there is a $(p-1)$th root of unity $\omega$ such that $u \equiv \omega mod p\mathbf{Z}_p$. Let $v = u/\omega$, so $v \in 1 + p\mathbf{Z}_p$ and $u = \omega v$. Such a decomposition of $u$ is unique, since if $u = \omega' v'$ where $\omega'^{p-1} = 1$ and $v' \in 1 + p\mathbf{Z}_p$ then reducing the equation $\omega v = \omega' v'$ modulo $p$ tells us $\omega \equiv \omega' mod p$, so $\omega = \omega'$ by the uniqueness of lifting roots of $X^p - X$ from $\mathbf{Z}/p\mathbf{Z}$ to $\mathbf{Z}_p$ in Hensel's lemma. Thus $\omega v = \omega v'$, so $v = v'$.

The map $\mu_{p-1} 	imes (1 + p\mathbf{Z}_p) 	o \mathbf{Z}_p^	imes$ given by $(\omega, v) \mapsto \omega v$ is a group homomorphism and the previous paragraph shows it is both surjective and injective, and thus bijective, so we can write $\mathbf{Z}_p^	imes = \mu_{p-1} 	imes (1 + p\mathbf{Z}_p)$. This decomposition is trivial when $p = 2$ since $\mu_{2-1} = \{1\}$, but in this case we can refine the decomposition by using the roots of unity $\pm 1$, which are distinguished modulo 4 rather than modulo 2. For $u \in \mathbf{Z}_2^	imes$ either $u \equiv 1 mod 4$ or $u \equiv 3 mod 4$, so there is one $\omega \in \{\pm 1\}$ such that $u \equiv \omega mod 4$. From this we get $\mathbf{Z}_2^	imes = \{\pm 1\} 	imes (1 + 4\mathbf{Z}_2)$ in the same way we showed $\mathbf{Z}_p^	imes = \mu_{p-1} 	imes (1 + p\mathbf{Z}_p)$. $\square$

## 4. A Stronger Version of Hensel's Lemma

The hypotheses of Theorem 2.1 are $f(a) \equiv 0 mod p$ and $f'(a) 
ot\equiv 0 mod p$. This means $a mod p$ is a *simple root* of $f(X) mod p$. We will now discuss a more general version of Hensel's lemma than Theorem 2.1. It can be applied to cases where $a mod p$ is a multiple root of $f(X) mod p$: $f(a) \equiv 0 mod p$ and $f'(a) \equiv 0 mod p$. This will allow us to describe squares in $\mathbf{Z}_2^	imes$ and, more generally, $p$th powers in $\mathbf{Z}_p^	imes$.

**Theorem 4.1 (Hensel's lemma).** *Let $f(X) \in \mathbf{Z}_p[X]$ and $a \in \mathbf{Z}_p$ satisfy*

$$|f(a)|_p < |f'(a)|_p^2.$$

*There is a unique $lpha \in \mathbf{Z}_p$ such that $f(lpha) = 0$ in $\mathbf{Z}_p$ and $|lpha - a|_p < |f'(a)|_p$. Moreover,*

1. *$|lpha - a|_p = |f(a)/f'(a)|_p < |f'(a)|_p$,*
2. *$|f'(lpha)|_p = |f'(a)|_p$.*

Since $f'(a) \in \mathbf{Z}_p$, $|f'(a)|_p \leq 1$. If $|f'(a)|_p = 1$ then the hypotheses of Theorem 4.1 reduce to those of Theorem 2.1: saying $|f(a)|_p < 1$ and $|f'(a)|_p = 1$ means $f(a) \equiv 0 mod p$ and $f'(a) 
ot\equiv 0 mod p$. Theorem 4.1 actually goes beyond the conclusions of Theorem 2.1 when the hypotheses of Theorem 2.1 hold, since we learn in Theorem 4.1 exactly how far away the root $lpha$ is from the approximate root $a$. But the main point of Theorem 4.1 is that it allows for the possibility that $|f'(a)|_p < 1$, which is not covered by Theorem 2.1 at all.

<!-- page 7 -->

We will prove Theorem 4.1 by two methods, in Sections 5 and 6. Here are some applications where the polynomial has a multiple root mod $p$.

**Example 4.2.** Let $f(X) = X^4 - 7X^3 + 2X^2 + 2X + 1$. Then $f(X) \equiv (X+1)^2(X^2+1) mod 3$ and we notice 2 mod 3 is a double root. Since $|f(2)|_3 = 1/27$ and $|f'(2)|_3 = |-42|_3 = 1/3$, the condition $|f(2)|_3 < |f'(2)|_3^2$ holds, so there is a unique root $lpha$ of $f(X)$ in $\mathbf{Z}_3$ such that $|lpha - 2|_3 < 1/3$, *i.e.*, $lpha \equiv 2 mod 9$.

In fact there are two roots of $f(X)$ in $\mathbf{Z}_3$:

$$2 + 3 + 2 \cdot 3^2 + 2 \cdot 3^3 + 2 \cdot 3^4 + 2 \cdot 3^6 + \cdots 	ext{ and } 2 + 3^2 + 3^4 + 2 \cdot 3^5 + 2 \cdot 3^6 + \cdots.$$

The second root reduces to 2 mod 9, and is $lpha$. The first root reduces to 5 mod 9, and its existence can be verified by checking $|f(5)|_3 = 1/27 < |f'(5)|_3^2 = 1/9$.

**Example 4.3.** Let $f(X) = X^3 - 10$ and $g(X) = X^3 - 5$. We have $f(X) \equiv (X-1)^3 mod 3$ and $g(X) \equiv (X-2)^3 mod 3$: 1 is an approximate 3-adic root of $f(X)$ and 2 is an approximate 3-adic root of $g(X)$. Can these be refined to 3-adic roots? The basic form of Hensel's lemma in Theorem 2.1 can not be used since the polynomials do not have simple roots mod 3. Instead we will use the stronger form of Hensel's lemma in Theorem 4.1.

Since $|f(1)|_3 = 1/9$ and $|f'(1)|_3 = 1/3$, we do not have $|f(1)|_3 < |f'(1)|_3^2$, so Theorem 4.1 can not be used on $f(X)$ with $a = 1$. However, $|f(4)|_3 = 1/27$ and $|f'(4)|_3 = 1/3$, so we can use Theorem 4.1 on $f(X)$ with $a = 4$: there is a unique root $lpha$ of $X^3 - 10$ in $\mathbf{Z}_3$ satisfying $|lpha - 4|_3 < 1/3$, so $lpha \equiv 4 mod 9$. The expansion of $lpha$ begins as $1 + 3 + 3^2 + 2 \cdot 3^6 + 3^7 + \cdots$.

Turning to $g(X)$, we have $|g(2)|_3 = 1/3$ and $|g'(2)|_3 = 1/9$, so we can not apply Theorem 4.1 with $a = 2$. In fact there is no root of $g(X)$ in $\mathbf{Q}_3$. If there were a root $lpha$ in $\mathbf{Q}_3$ then $lpha^3 = 5$, so $|lpha|_3 = 1$, and thus $lpha \in \mathbf{Z}_3$. Then $lpha^3 \equiv 5 mod 3^n$, so 5 would be a cube modulo every power of 3. But 5 is not a cube mod 9 (the only cubes mod 9 are 0, 1, and 8). Therefore the mod 3 root of $X^3 - 5$ does not lift to a 3-adic root of $X^3 - 5$.

**Example 4.4.** Let $f(X) = X^3 - X^2 - 2X - 8 \equiv X^3 - X^2 \equiv X^2(X - 1) mod 2$. By Example 2.7, $f(X)$ has a unique root $lpha = 1 + 2 + 2^2 + 2^4 + 2^6 + 2^9 + \cdots$ that is 1 mod 2. Now we will show there are two roots in $\mathbf{Z}_2$ that are 0 mod 2. Since $f(0) = -8$ and $f'(0) = -2$, we have $|f(0)|_2 = 1/8 < |f'(0)|_2^2 = 1/4$, so $f(X)$ has a unique root $eta$ in $\mathbf{Z}_2$ such that $|eta|_2 < 1/2$, meaning $eta \equiv 0 mod 4$. Also $f(2) = -8$ and $f'(2) = 6$, so $|f(2)|_2 = 1/8 < |f'(2)|_2^2 = 1/4$, so $f(X)$ has a unique root $\gamma$ in $\mathbf{Z}_2$ such that $|\gamma - 2|_2 < 1/2$, so $\gamma \equiv 2 mod 4$. Explicitly, $eta = 2^2 + 2^4 + 2^6 + 2^7 + 2^8 + 2^{10} + \cdots$ and $\gamma = 2 + 2^2 + 2^4 + 2^6 + 2^7 + 2^8 + 2^9 + \cdots$.

**Theorem 4.5.** *If $u \in \mathbf{Z}_2^	imes$ then $u$ is a square in $\mathbf{Q}_2$ if and only if $u \equiv 1 mod 8\mathbf{Z}_2$.*

*Proof.* If $u = v^2$ in $\mathbf{Q}_2$ then $1 = |v|_2^2$, so $v \in \mathbf{Z}_2^	imes$. In $\mathbf{Z}_2/8\mathbf{Z}_2 \cong \mathbf{Z}/8\mathbf{Z}$, the units are 1, 3, 5, and 7, whose squares are all congruent to 1 mod 8, so $u = v^2 \equiv 1 mod 8\mathbf{Z}_2$. To show, conversely, that all $u \in \mathbf{Z}_2^	imes$ satisfying $u \equiv 1 mod 8\mathbf{Z}_2$ are squares in $\mathbf{Z}_2^	imes$, let $f(X) = X^2 - u$ and use $a = 1$ in Theorem 4.1. We have $|f(1)|_2 = |1 - u|_2 \leq 1/8$ and $|f'(1)|_2 = |2|_2 = 1/2$, so $|f(1)|_2 < |f'(1)|_2^2$. Therefore $X^2 - u$ has a root in $\mathbf{Z}_2$, so $u$ is a square in $\mathbf{Z}_2$. $\square$

**Example 4.6.** We saw in Example 2.11 that for $p 
eq 2$ and $a \in \mathbf{Q}_p$, $y^2 = x^4 + a$ has a solution in $\mathbf{Q}_p$ when $|x|_p^4 > |a|_p$. With Theorem 4.5 we will get an analogue of this for $p = 2$.

Rewriting the equation as $y^2 = x^4(1 + a/x^4)$, we want $1 + a/x^4$ to be a square in $\mathbf{Q}_2$, and by Theorem 4.5 such a condition is $|a/x^4|_2 \leq 1/8$, since then $1 + a/x^4 \equiv 1 mod 8\mathbf{Z}_2$.

The same method, using the stronger version of Hensel's lemma, shows for prime $p$, $a \in \mathbf{Q}_p$, and $n \mid m$ in $\mathbf{Z}^+$ that the equation $y^n = x^m + a$ has a $p$-adic solution $(x, y)$ whenever $|x|_p$ is sufficiently large in terms of $|a|_p$, $m$, and $n$. Details are left to the reader.

**Theorem 4.7.** *If $p 
eq 2$ and $u \in \mathbf{Z}_p^	imes$, then $u$ is a $p$th power in $\mathbf{Q}_p$ if and only if $u$ is a $p$th power modulo $p^2$.*

<!-- page 8 -->

*Proof.* If $u = v^p$ in $\mathbf{Q}_p$ then $1 = |v|_p^p$, so $v \in \mathbf{Z}_p^	imes$: we only need to look for $p$th roots of $u$ in $\mathbf{Z}_p^	imes$. Let $f(X) = X^p - u$. In order to use Theorem 4.1 on $f(X)$, we seek an $a \in \mathbf{Z}_p^	imes$ such that $|f(a)|_p < |f'(a)|_p^2$. This means $|a^p - u|_p < |pa^{p-1}|_p^2 = 1/p^2$, or equivalently $a^p \equiv u mod p^3$. Provided $u$ is a $p$th power modulo $p^3$, Theorem 4.1 tells us that $X^p - u$ has a root in $\mathbf{Z}_p$, so $u$ is a $p$th power. The criterion in the theorem, however, has modulus $p^2$ rather than $p^3$. We need to do some work to bootstrap an approximate $p$th root from modulus $p^2$ to modulus $p^3$ in order to apply Theorem 4.1.

Suppose $u \equiv a^p mod p^2$ for some $a \in \mathbf{Z}_p$. Then $a \in \mathbf{Z}_p^	imes$ and $u/a^p \equiv 1 mod p^2$. Write $u/a^p \equiv 1 + p^2 c mod p^3$, where $0 \leq c \leq p - 1$. By the binomial theorem,

$$(1 + pc)^p = 1 + p(pc) + \sum_{k=2}^{p} inom{p}{k} (pc)^k.$$

The terms for $k \geq 3$ are obviously divisible by $p^3$ and the term at $k = 2$ is $inom{p}{2}(pc)^2 = rac{p-1}{2} p^3 c^2$, which is also divisible by $p^3$ since $p > 2$.

Therefore $(1 + pc)^p \equiv 1 + p^2 c mod p^3$, so $u/a^p \equiv (1 + pc)^p mod p^3$. Now we can write

$$rac{u}{a^p(1 + pc)^p} \equiv 1 mod p^3.$$

From Theorem 4.1, a $p$-adic integer that is congruent to 1 mod $p^3$ is a $p$th power (see the first paragraph again). Thus $u/(a^p(1 + pc)^p)$ is a $p$th power, so $u$ is a $p$th power. $\square$

Theorem 4.7 is false for $p = 2$: the criterion for an element of $\mathbf{Z}_2^	imes$ to be a 2-adic square needs modulus $2^3$, not modulus $2^2$, by Theorem 4.5. For instance, 5 mod 4 is a square but 5 is not a 2-adic square since $5 
ot\equiv 1 mod 8$. Theorem 4.7 explains what we found in Example 4.3: 10 is a 3-adic cube and 5 is not, since 10 mod 9 is a cube and 5 mod 9 is not a cube.

**Remark 4.8.** Hensel's lemma in Theorem 4.1 says a root mod $p$ lifts uniquely to a root in $\mathbf{Z}_p$ under weaker conditions than Hensel's lemma in Theorem 2.1, but there may not be a unique root mod $p^n$, unlike in Theorem 2.1 (Remark 2.3). Consider Example 4.3: in $\mathbf{Z}_3$, $X^3 = 10$ has one solution $1 + 3 + 3^2 + 2 \cdot 3^6 + \cdots$, but for $n \geq 2$, $X^3 \equiv 10 mod 3^n$ has 3 solutions, not 1. One of the solutions mod $3^n$ lifts to three solutions mod $3^{n+1}$ and two do not. (For instance, solutions mod 27 are 4, 13, and 22 and only 13 lifts to solutions mod 81, in fact to 13, 40, and 67 mod 27.) This is *consistent* with a unique root in $\mathbf{Z}_3$ since the 3 solutions mod $3^n$ are congruent modulo $3^{n-1}$ and thus are close: they have a common limit in $\mathbf{Z}_3$ as $n 	o \infty$.

Another example is $X^2 = 1$. It has two solutions in $\mathbf{Z}_2$, but $X^2 \equiv 1 mod 2^n$ for $n \geq 2$ has 4 solutions: $1, -1, 1 + 2^{n-1}$, and $-1 + 2^{n-1} mod 2^n$. As $n 	o \infty$, the first and third solutions mod $2^n$ tend to 1 and the second and fourth solutions mod $2^n$ tend to $-1$.

## 5. First Proof of Theorem 4.1: Newton's Method

Our first proof of Theorem 4.1 will use Newton's method and is a modification of [6, Chap. II, \S2, Prop. 2].

*Proof.* As in Newton's method from real analysis, define a sequence $\{a_n\}$ in $\mathbf{Q}_p$ by $a_1 = a$ and

$$a_{n+1} = a_n - rac{f(a_n)}{f'(a_n)} 	ag{5.1}$$

for $n \geq 1$. Set $t = |f(a)/f'(a)^2|_p < 1$. We will show by induction on $n$ that

- (i) $|a_n|_p \leq 1$, *i.e.*, $a_n \in \mathbf{Z}_p$,
- (ii) $|f'(a_n)|_p = |f'(a_1)|_p$,

- (iii) $|f(a_n)|_p \leq |f'(a_1)|_p^2 t^{2^{n-1}}$.

For $n = 1$ these conditions are all clear. Note in particular that we have equality in (iii) and $f'(a_1) 
eq 0$ since $|f(a_1)|_p < |f'(a_1)|_p^2$.

For the inductive step, we need two polynomial identities. The first one, for $F(X) \in \mathbf{Z}_p[X]$, is

$$F(X + Y) = F(X) + F'(X)Y + g(X, Y)Y^2 	ag{5.2}$$

for some $g(X, Y) \in \mathbf{Z}_p[X, Y]$. This is (2.1) from the proof of Theorem 2.1. So

$$x, y \in \mathbf{Z}_p \implies oxed{F(x + y) = F(x) + F'(x)y + zy^2, 	ext{ where } z \in \mathbf{Z}_p} 	ag{5.3}$$

with $z = g(x, y)$. The second polynomial identity we need is that for $F(X) \in \mathbf{Z}_p[X]$,

$$F(X) - F(Y) = (X - Y)G(X, Y)$$

for some $G(X, Y) \in \mathbf{Z}_p[X, Y]$. This comes from $X - Y$ being a factor of $X^i - Y^i$ for all $i \geq 1$. Writing $F(X) = \sum_{i=0}^m b_i X^i$,

$$F(X) - F(Y) = \sum_{i=1}^m b_i(X^i - Y^i)$$

and we can factor $X - Y$ out of each term on the right. For $x$ and $y$ in $\mathbf{Z}_p$, $G(x, y) \in \mathbf{Z}_p$, so

$$x, y \in \mathbf{Z}_p \implies oxed{|F(x) - F(y)|_p = |x - y|_p |G(x, y)|_p \leq |x - y|_p.} 	ag{5.4}$$

Assume (i), (ii), and (iii) are true for $n$. To prove (i) for $n + 1$, first note $a_{n+1}$ is defined since $f'(a_n) 
eq 0$ by (ii). To prove (i) it suffices to show $|f(a_n)/f'(a_n)|_p \leq 1$. Using (ii) and (iii) for $n$, we have $|f(a_n)/f'(a_n)|_p = |f(a_n)/f'(a_1)|_p \leq |f'(a_1)|_p t^{2^{n-1}} < 1$ since $t < 1$.

To prove (ii) for $n+1$, (iii) for $n$ implies $|f(a_n)|_p < |f'(a_1)|_p^2$ since $t < 1$ (and $|f'(a_1)|_p 
eq 0$), so by (5.4) with $F(X) = f'(X)$,

$$|f'(a_{n+1}) - f'(a_n)|_p \leq |a_{n+1} - a_n|_p = rac{|f(a_n)|_p}{|f'(a_n)|_p} = rac{|f(a_n)|_p}{|f'(a_1)|_p} < |f'(a_1)|_p = |f'(a_n)|_p,$$

so $|f'(a_{n+1})|_p = |f'(a_n)|_p = |f'(a_1)|_p$.

To prove (iii) for $n + 1$, we use (5.3) with $F(X) = f(X)$, $x = a_n$ and $y = -f(a_n)/f'(a_n)$:

$$f(a_{n+1}) = f(x + y) = f(a_n) + f'(a_n)\left(-rac{f(a_n)}{f'(a_n)}ight) + z\left(rac{f(a_n)}{f'(a_n)}ight)^2 = z\left(rac{f(a_n)}{f'(a_n)}ight)^2,$$

where $z \in \mathbf{Z}_p$. (Note $|y|_p = |f(a_n)|_p/|f'(a_n)|_p < 1$.) Thus, by (iii) for $n$,

$$|f(a_{n+1})|_p \leq \left|rac{f(a_n)}{f'(a_n)}ight|_p^2 = rac{|f(a_n)|_p^2}{|f'(a_1)|_p^2} \leq rac{|f'(a_1)|_p^4 t^{2^n}}{|f'(a_1)|_p^2} = |f'(a_1)|_p^2 t^{2^n}.$$

This completes the induction.

Now we show $\{a_n\}$ is Cauchy in $\mathbf{Q}_p$. From the recursive definition of this sequence,

$$|a_{n+1} - a_n|_p = \left|rac{f(a_n)}{f'(a_n)}ight|_p = rac{|f(a_n)|_p}{|f'(a_1)|_p} \leq |f'(a_1)|_p t^{2^{n-1}}, 	ag{5.5}$$

where we used (ii) and (iii). Thus $\{a_n\}$ is Cauchy. Let $lpha$ be its limit, so $|lpha|_p \leq 1$ by (i), *i.e.*, $lpha \in \mathbf{Z}_p$. Letting $n 	o \infty$ in (ii) and (iii) we get $|f'(lpha)|_p = |f'(a_1)|_p = |f'(a)|_p$ and $f(lpha) = 0$.

<!-- page 10 -->

To show $|lpha - a|_p = |f(a)/f'(a)|_p$, it is true if $f(a) = 0$ since then $a_n = a_1 = a$ for all $n$, so $lpha = a$.[^3] If $f(a) 
eq 0$ then we will show $|a_n - lpha|_p = |f(a)/f'(a)|_p$ for all $n \geq 2$ and let $n 	o \infty$. When $n = 2$ use the definition of $a_2$ in terms of $a_1 = a$. For all $n \geq 2$, by (5.5)

$$|a_{n+1} - a_n|_p \leq |f'(a_1)|_p t^{2^{n-1}} \leq |f'(a_1)|_p t^2 < |f'(a_1)|_p t = |f'(a)|_p t = \left|rac{f(a)}{f'(a)}ight|_p, 	ag{5.6}$$

where $t \in (0, 1)$ since $f(a) 
eq 0$. If $|a_n - lpha|_p = |f(a)/f'(a)|_p$ then $|a_{n+1} - a_n|_p < |a_n - lpha|_p$ by (5.6), so $|a_{n+1} - lpha|_p = |(a_{n+1} - a_n) + (a_n - lpha)|_p = |a_n - lpha|_p = |f(a)/f'(a)|_p$.

The last thing to do is show $lpha$ is the only root of $f(X)$ in the ball $\{x \in \mathbf{Z}_p : |x - a|_p < |f'(a)|_p\}$. This will not use anything about Newton's method. Assume $f(eta) = 0$ and $|eta - a|_p < |f'(a)|_p$. Since $|lpha - a|_p < |f'(a)|_p$ we have $|eta - lpha|_p < |f'(a)|_p$. Write $eta = lpha + h$, so $h \in \mathbf{Z}_p$. Then by (5.3) with $F(X) = f(X)$,

$$0 = f(eta) = f(lpha + h) = f(lpha) + f'(lpha)h + zh^2 = f'(lpha)h + zh^2$$

for some $z \in \mathbf{Z}_p$. If $h 
eq 0$ then $f'(lpha) = -zh$, so $|f'(lpha)|_p \leq |h|_p = |eta - lpha|_p < |f'(a)|_p$. But $|f'(lpha)|_p = |f'(a)|_p$, so we have a contradiction. Thus $h = 0$, so $eta = lpha$. $\square$

Before we give a second proof of Theorem 4.1, it is worth noting that the $a_n$'s converge to $lpha$ very rapidly. From the inequality $|a_{n+1} - a_n|_p \leq |f'(a_1)|_p t^{2^{n-1}}$ for all $n \geq 1$ we obtain by the strong triangle inequality $|a_m - a_n|_p \leq |f'(a_1)|_p t^{2^{n-1}}$ for all $m > n$. Letting $m 	o \infty$,

$$oxed{|lpha - a_n|_p \leq |f'(a_1)|_p t^{2^{n-1}} = |f'(a)|_p t^{2^{n-1}} = |f'(a)|_p \left|rac{f(a)}{f'(a)^2}ight|_p^{2^{n-1}}.} 	ag{5.7}$$

Since $|f(a)/f'(a)^2|_p < 1$, the exponent $2^{n-1}$ tells us that the number of initial $p$-adic digits in $a_n$ that agree with those in the limit $lpha$ is at least doubling at each step.

**Example 5.1.** Let $f(X) = X^2 - 7$ in $\mathbf{Q}_3[X]$. It has two roots in $\mathbf{Z}_3$:

$$r = 1 + 3 + 3^2 + 2 \cdot 3^4 + 2 \cdot 3^7 + 3^8 + 3^9 + \cdots,$$
$$s = 2 + 3 + 3^2 + 2 \cdot 3^3 + 2 \cdot 3^5 + 2 \cdot 3^6 + 3^8 + 3^9 + \cdots.$$

Starting with $a_1 = 1$, for which $|f(a_1)/f'(a_1)^2|_3 = 1/3$, Newton's recursion (5.1) has limit $lpha$ where $|lpha - a_1|_3 < |f'(a_1)|_3 = 1$, so $lpha \equiv a_1 \equiv 1 mod 3$. Thus $lpha = r$. For example,

$$a_4 = rac{977}{368} = 1 + 3 + 3^2 + 2 \cdot 3^4 + 2 \cdot 3^7 + 3^9 + 3^{10} + \cdots,$$

which has the same 3-adic digits as $r$ up through terms including $3^7$ (the first 8 digits). The estimate in (5.7) says $|r - a_n|_3 \leq |f'(a_1)|_3 (1/3)^{2^{n-1}} = (1/3)^{2^{n-1}}$ for all $n$. Using a computer, this inequality is an equality for $1 \leq n \leq 10$.

**Example 5.2.** Let $f(X) = X^2 - 17$ in $\mathbf{Q}_2[X]$. It has two roots in $\mathbf{Z}_2$:

$$r = 1 + 2^3 + 2^5 + 2^6 + 2^7 + 2^9 + \cdots,$$
$$s = 1 + 2 + 2^2 + 2^4 + 2^8 + \cdots.$$

Using Newton's recursion (5.1) for $f(X)$ with initial seed $a \in \mathbf{Z}_2^	imes$, we need $|a^2 - 17|_2 < |2a|_2^2$, which is the same as $a^2 \equiv 17 mod 8$, and this congruence works for all $a \in \mathbf{Z}_2^	imes$. Therefore (5.1) with $a_1 \in \mathbf{Z}_2^	imes$ converges to $r$ or $s$. Since $|f'(a)|_2 = 1/2$ for $a \in \mathbf{Z}_2^	imes$, (5.1) with $a_1 = a$ has a limit $lpha$ satisfying $|lpha - a|_2 < |f'(a)|_2 = 1/2$, so $lpha \equiv a mod 4$: if $a \equiv 1 mod 4$ then

[^3]: The case $f(a) = 0$ was not covered in an earlier draft and this omission was found when the proof here was formalized using the Lean theorem prover [8, p. 8].

<!-- page 11 -->

$lpha = r$, and if $a \equiv 3 mod 4$ then $lpha = s$. By (5.7), $|lpha - a_n|_2 \leq |f'(a)|_2 (|f(a)/f'(a)^2|_2)^{2^{n-1}} = (1/2)(4|a^2 - 17|_2)^{2^{n-1}}$. For a few choices of $a$, this inequality is an equality for $1 \leq n \leq 10$:

- When $a = 1$, $|r - a_n|_2 = (1/2)^{2^{n-1}+1}$ for $1 \leq n \leq 10$.
- When $a = 3$, $|s - a_n|_2 = (1/2)^{2^{n-1}+1}$ for $1 \leq n \leq 10$.
- When $a = 5$, $|r - a_n|_2 = (1/2)^{2^{n-1}+1}$ for $1 \leq n \leq 10$.

**Example 5.3.** Let us solve $X^2 - 1 = 0$ in $\mathbf{Q}_3$. This might seem silly, since we know the solutions are $\pm 1$, but let us check how an initial approximation affects the 3-adic limit. We use $a_1 = 2$. (If we used $a_1 = 1$ then $a_n = 1$ for all $n$, which is not interesting.) When $f(X) = X^2 - 1$ the recursion for Newton's method is

$$a_{n+1} = a_n - rac{f(a_n)}{f'(a_n)} = a_n - rac{a_n^2 - 1}{2a_n} = rac{a_n^2 + 1}{2a_n} = rac{1}{2}\left(a_n + rac{1}{a_n}ight).$$

Since $|f(2)|_3 = 1/3 < |f'(2)|_3^2$, Newton's recursion with $a_1 = 2$ converges in $\mathbf{Q}_3$. What is the limit? Since $a_1 \equiv -1 mod 3$, we have $a_n \equiv -1 mod 3$ for all $n$ by induction: if $a_n \equiv -1 mod 3$ then $a_{n+1} = (1/2)(a_n + 1/a_n) \equiv (1/2)(-1 + 1/(-1)) \equiv (1/2)(-2) \equiv -1 mod 3$. Thus $\lim_{n 	o \infty} a_n = -1$ in $\mathbf{Q}_3$. What makes this interesting is that in $\mathbf{R}$ all $a_n$ are positive so the sequence of rational numbers $\{a_n\}$ converges to 1 in $\mathbf{R}$ and to $-1$ in $\mathbf{Q}_3$. The table below illustrates the rapid convergence in $\mathbf{R}$ and $\mathbf{Q}_3$ (the 3-adic expansion of $-1$ is $ar{2} = 2222\ldots$).

| $n$ | $a_n$ | Decimal approx. | 3-adic approx. |
|-----|-------|-----------------|----------------|
| 1 | 2 | 2.00000000 | 20000000 |
| 2 | 5/4 | 1.25000000 | 22020202 |
| 3 | 41/40 | 1.02500000 | 22220222 |
| 4 | 3281/3280 | 1.00030487 | 22222222 |

Theorem 4.1 has Theorem 2.1 as the special case when $|f'(a)|_p = 1$. Using a change of variables, we will show Theorem 4.1 follows from Theorem 2.1, so the basic and strong versions of Hensel's lemma are in fact equivalent!

**Theorem 5.4.** *Theorem 2.1 implies Theorem 4.1.*

*Proof.* Suppose $f(X) \in \mathbf{Z}_p[X]$ and $a \in \mathbf{Z}_p$ satisfies $|f(a)|_p < |f'(a)|_p^2$. We will use Theorem 2.1 to show $f(X)$ has a unique root $lpha \in \mathbf{Z}_p$ such that $|lpha - a|_p < |f'(a)|_p$, and in fact $|lpha - a|_p = |f(a)/f'(a)|_p$ and $|f'(lpha)|_p = |f'(a)|_p$.

Since $|f(a)|_p < |f'(a)|_p^2$, set $b = f(a)/f'(a)^2$, so $f(a) = f'(a)^2 b$ and $|b|_p < 1$. A root $lpha \in \mathbf{Z}_p$ of $f(X)$ where $|lpha - a|_p < |f'(a)|_p$ is a root of the form $a + f'(a)s$ with $|s|_p < 1$. We thus want to show $f(a + f'(a)s) = 0$ for a unique $s \in \mathbf{Z}_p$ with $|s|_p < 1$ and also show that in fact $|s|_p = |f(a)/f'(a)^2|$. By the polynomial identity (5.2) with $F(X) = f(X)$, there is a polynomial $g(X, Y) \in \mathbf{Z}_p[X, Y]$ such that

$$f(X + Y) = f(X) + f'(X)Y + g(X, Y)Y^2,$$

so for all $s \in \mathbf{Z}_p$,

$$f(a + f'(a)s) = f(a) + f'(a)(f'(a)s) + g(a, f'(a)s)(f'(a)s)^2$$
$$= f'(a)^2 b + f'(a)^2 s + g(a, f'(a)s)f'(a)^2 s^2$$
$$= f'(a)^2(b + s + g(a, f'(a)s)s^2).$$

Set $h(X) = b + X + g(a, f'(a)X)X^2 \in \mathbf{Z}_p[X]$. Since $h(X)$ has constant term $b = f(a)/f'(a)^2$ and linear coefficient 1, $|h(0)|_p = |b|_p < 1$ and $|h'(0)|_p = |1|_p = 1$. Theorem 2.1 implies there is a unique $eta \in \mathbf{Z}_p$ such that $h(eta) = 0$ and $|eta|_p < 1$, so $lpha := a + f'(a)eta$ is the unique root of $f(X)$ in $\mathbf{Z}_p$ such that $|lpha - a|_p < |f'(a)|_p$.

<!-- page 12 -->

To show $|lpha - a|_p = |f(a)/f'(a)|_p$, rewrite this as $|eta|_p = |f(a)/f'(a)^2|_p$. If $eta = 0$ then $lpha = a$, so $f(a) = 0$ and thus $|f(a)/f'(a)^2|_p = 0 = |eta|_p$. If $eta 
eq 0$ then from

$$0 = h(eta) = b + eta + g(a, f'(a)eta)eta^2$$

we get $|b + eta|_p = |g(a, f'(a)eta)eta^2|_p \leq |eta|_p^2 < |eta|_p$, so $|eta|_p = |b|_p = |f(a)/f'(a)^2|_p$.

That $|f'(lpha)|_p = |f'(a)|_p$ follows from $|lpha - a|_p < |f'(a)|_p$: by (5.4), $|f'(lpha) - f'(a)|_p \leq |lpha - a|_p < |f'(a)|_p$, so $|f'(lpha)|_p = |f'(a)|_p$. $\square$

**Example 5.5.** Let $f(X) = X^3 - 10$ with approximate root $a = 4$ in $\mathbf{Z}_3$. We can not apply Theorem 2.1 directly to $f(X)$ to show there is a solution to $f(lpha) = 0$ in $\mathbf{Z}_3$ with $lpha$ close to 4 since $f'(4) = 48 \equiv 0 mod 3$. From the proof of Theorem 5.4 we compute

$$f(X+Y) = (X+Y)^3 - 10 = X^3 + 3X^2Y + 3XY^2 + Y^3 - 10 = f(X) + f'(X)Y + (3X+Y)Y^2.$$

Then

$$f(4+48X) = f(4) + f'(4)48X + (12+48X)(48X)^2 = 54 + 48^2 X + (12+48X)(48X)^2 = 48^2 h(X)$$

where

$$h(X) = rac{54}{48^2} + X + (12+48X)X^2 = rac{3}{128} + X + 12X^2 + 48X^3.$$

Since $h(0) \equiv 0 mod 3$ and $h'(0) = 1 
ot\equiv 0 mod 3$, $h(X)$ has a unique root $eta \in 3\mathbf{Z}_3$ and that gives us a root $lpha = 4 + 48eta$ of $f(X)$.

By Theorem 2.1, each solution of $h(x) \equiv 0 mod 3^n$ with $x \equiv 0 mod 3$ lifts uniquely to a solution of $h(x) \equiv 0 mod 3^{n+1}$ but such uniqueness of lifting at each "finite level" is not true for solving $f(x) \equiv 0 mod 3^n$; see Remark 4.8. This different behavior is compatible because of the 48 (a multiple of 3) appearing on both sides of $f(4 + 48X) = 48^2 h(X)$.

For example, suppose we want to solve $f(t) \equiv 0 mod 81$ in $\mathbf{Z}_3$ with $t \equiv 4 mod 3$. Then we can write $t = 4 + 48x$ with $x \in \mathbf{Z}_3$ since 48 is divisible by 3 just once, so

$$f(4 + 48x) \equiv 0 mod 81 \iff 48^2 h(x) \equiv 0 mod 81 \iff h(x) \equiv 0 mod 9.$$

Note the modulus decreased from 81 to 9. The unique solution of $h(x) \equiv 0 mod 9$ is 3 mod 9, and that is the same as $t = 4 + 48x \equiv 4 + 48 \cdot 3 \equiv 13 mod 27$. The modulus increased from 9 to 27 since congruences mod 9 are the same as congruences mod 27 when multiplying by 48. We have shown $f(t) \equiv 0 mod 81$ is the same as $t \equiv 13 mod 27$, and there are three liftings of 13 from mod 27 to mod 81: 13, 40, and 67.

## 6. Second Proof of Theorem 4.1: Contraction Mappings

Newton's method produces a sequence converging to a root of $f(X)$ by iterating the function $x - f(x)/f'(x)$ with initial value $a_1 = a$ where $|f(a)|_p < |f'(a)|_p^2$. A root can also be found with a different iteration $arphi(x) = x - f(x)/f'(a)$, where again $|f(a)|_p < |f'(a)|_p^2$. The denominator is $f'(a)$, not $f'(x)$, so it does not change. We will show $arphi$ is a contraction mapping on a suitable ball around $a$. Then the contraction mapping theorem will imply $arphi$ has a (unique) fixed point $lpha$ in that ball.[^4] The condition $arphi(lpha) = lpha$ says $lpha - f(lpha)/f'(a) = lpha$, so $f(lpha) = 0$ and we have a root of $f(X)$. Filling in the details leads to the following second proof of Theorem 4.1. If you are not interested in a second proof, go to the next section.

*Proof.* For $r \in [0, 1]$ to be determined, set $\overline{B}_a(r) = \{x \in \mathbf{Q}_p : |x - a|_p \leq r\}$, so $\overline{B}_a(r) \subset \mathbf{Z}_p$. Set

$$arphi(x) = x - rac{f(x)}{f'(a)}.$$

[^4]: There is an analogous method in real analysis to simplify Newton's method to the contraction mapping theorem by fixing the denominator in the recursion. See [2, Thm. 1.2, p. 164].

<!-- page 13 -->

We seek an $r$ such that $arphi$ maps $\overline{B}_a(r)$ back to itself and is a contraction on that ball.

To show $arphi$ is a contraction on some ball around $a$, we want to estimate

$$|arphi(x) - arphi(y)|_p = \left|x - y - rac{f(x) - f(y)}{f'(a)}ight|$$

for all $x$ and $y$ near $a$ in order to make this $\leq \lambda|x - y|_p$ for some $\lambda < 1$.

Write $f(X)$ as a polynomial in $X - a$, say $f(X) = \sum_{i=0}^d b_i(X - a)^i$. Then $b_0 = f(a)$, $b_1 = f'(a)$, and $b_i \in \mathbf{Z}_p$ for $i > 1$. For all $x$ and $y$ in $\mathbf{Q}_p$,

$$f(x) - f(y) = \sum_{i=1}^d b_i((x-a)^i - (y-a)^i) = f'(a)(x-y) + \sum_{i=2}^d b_i((x-a)^i - (y-a)^i),$$

so

$$arphi(x) - arphi(y) = x - y - rac{f(x) - f(y)}{f'(a)} = -rac{1}{f'(a)} \sum_{i=2}^d b_i((x-a)^i - (y-a)^i). 	ag{6.1}$$

(If $d \leq 1$ then the sum on the right is empty.) In the polynomial identity

$$X^i - Y^i = (X - Y)\sum_{j=0}^{i-1} X^{i-1-j} Y^j$$

for $i \geq 2$ set $X = x - a$ and $Y = y - a$. Then

$$|(x-a)^i - (y-a)^i|_p = |x - y|_p \left|\sum_{j=0}^{i-1} (x-a)^{i-1-j}(y-a)^jight|_p$$
$$\leq |x - y|_p \max_{0 \leq j \leq i-1} |x-a|_p^{i-1-j}|y-a|_p^j$$
$$\leq |x - y|_p \max(|x-a|_p, |y-a|_p)^{i-1}$$
$$\leq |x - y|_p \max(|x-a|_p, |y-a|_p)$$

when $|x - a|_p$ and $|y - a|_p$ are both at most 1. Therefore from (6.1),

$$|x-a|_p, |y-a|_p \leq 1 \implies |arphi(x) - arphi(y)|_p \leq rac{|x-y|_p \max(|x-a|_p, |y-a|_p)}{|f'(a)|_p},$$

so for $\lambda \in [0, 1)$,

$$|x-a|_p, |y-a|_p \leq \lambda|f'(a)|_p \implies |arphi(x) - arphi(y)|_p \leq \lambda|x - y|_p. 	ag{6.2}$$

If we can find $\lambda \in [0, 1)$, perhaps depending on $a$ and $f(X)$, such that

$$|x - a|_p \leq \lambda|f'(a)|_p \implies |arphi(x) - a|_p \leq \lambda|f'(a)|_p 	ag{6.3}$$

then (6.2) will tell us that $arphi$ is a contraction mapping on the closed ball around $a$ of radius $\lambda|f'(a)|_p$. We will see that if $|f(a)|_p < |f'(a)|_p^2$ then a choice for $\lambda$ is $|f(a)/f'(a)^2|_p$. In fact, we want to do more: show the condition $|f(a)|_p < |f'(a)|_p^2$ arises *naturally* by trying to make (6.3) work for some unknown $\lambda$.

For $\lambda \in (0, 1)$, when $|x - a|_p \leq \lambda|f'(a)|_p$ we have

$$|arphi(x) - a|_p \leq \lambda|f'(a)|_p \iff \left|x - a - rac{f(x)}{f'(a)}ight|_p \leq \lambda|f'(a)|_p \iff \left|rac{f(x)}{f'(a)}ight|_p \leq \lambda|f'(a)|_p.$$

<!-- page 14 -->

Returning to the formula $f(X) = \sum_{i=0}^d b_i(X - a)^i$, where $b_0 = f(a)$ and $b_1 = f'(a)$,

$$rac{f(x)}{f'(a)} = rac{f(a)}{f'(a)} + (x - a) + \sum_{i=2}^d rac{b_i}{f'(a)}(x - a)^i. 	ag{6.4}$$

When $|x - a|_p \leq \lambda|f'(a)|_p$, which is less than $|f'(a)|_p \leq 1$, we have for $i \geq 2$ that

$$\left|rac{b_i}{f'(a)}(x - a)^iight|_p \leq rac{|x - a|_p^2}{|f'(a)|_p} \leq \lambda^2|f'(a)|_p \leq \lambda|f'(a)|_p,$$

so by (6.4)

$$\left|rac{f(x)}{f'(a)}ight|_p \leq \lambda|f'(a)|_p \iff \left|rac{f(a)}{f'(a)}ight|_p \leq \lambda|f'(a)|_p \iff \left|rac{f(a)}{f'(a)^2}ight|_p \leq \lambda.$$

To make this occur for some $\lambda < 1$ is equivalent to requiring $|f(a)/f'(a)^2|_p < 1$. Therefore if $|f(a)|_p < |f'(a)|_p^2$ and we set $\lambda = |f(a)/f'(a)^2|_p$, the mapping $arphi(x) = x - f(x)/f'(a)$ is a contraction on the closed ball around $a$ with radius $\lambda|f'(a)|_p = |f(a)/f'(a)|_p$ and contraction constant $\lambda$. Any closed ball in $\mathbf{Q}_p$ is complete, so the contraction mapping theorem implies that the sequence $\{a_n\}$ defined recursively by $a_1 = a$ and

$$a_{n+1} = arphi(a_n) = a_n - rac{f(a_n)}{f'(a)} 	ag{6.5}$$

for $n \geq 1$ converges to the unique fixed point of $arphi$ in $\overline{B}_a(|f(a)/f'(a)|_p)$. By the definition of $arphi$, a fixed point of $arphi$ is the same thing as a zero of $f(X)$, so there is a unique $lpha$ in $\mathbf{Q}_p$ satisfying $f(lpha) = 0$ and $|lpha - a|_p \leq |f(a)/f'(a)|_p$.

To finish this proof of Theorem 4.1 we need to show $|lpha - a|_p = |f(a)/f'(a)|_p$, $lpha$ is the unique root of $f(X)$ in $\mathbf{Z}_p$ such that $|lpha - a|_p < |f'(a)|_p$, and $|f'(lpha)|_p = |f'(a)|_p$.

$|lpha - a|_p = |f(a)/f'(a)|_p$: We have $|a_2 - a|_p = |a_2 - a_1|_p = |f(a_1)/f'(a)|_p = |f(a)/f'(a)|_p$, and for all $n$

$$|a_{n+1} - a_n|_p = |arphi^n(a) - arphi^{n-1}(a)|_p = |arphi^{n-1}(arphi(a)) - arphi^{n-1}(a)|_p \leq \lambda^{n-1}|a_2 - a_1|_p < \left|rac{f(a)}{f'(a)}ight|_p.$$

Then $|a_n - a|_p = |f(a)/f'(a)|_p$ for all $n$ by induction, so $|lpha - a|_p = |f(a)/f'(a)|_p$ by letting $n 	o \infty$.

$lpha$ is the unique root of $f(X)$ such that $|lpha - a|_p < |f'(a)|_p$: This was proved at the end of the first proof of Theorem 4.1 without needing Newton's method. We will not rewrite the proof.

$|f'(lpha)|_p = |f'(a)|_p$: Since $a_1 = a$, of course $|f'(a_1)|_p = |f'(a)|_p$. If $|f'(a_n)|_p = |f'(a)|_p$ for some $n \geq 1$ then

$$|f'(a_{n+1}) - f'(a_n)|_p \leq |a_{n+1} - a_n|_p \leq \left|rac{f(a)}{f'(a)}ight|_p$$

where the first inequality is from (5.4) and the second inequality is from $a_n$ and $a_{n+1}$ both lying in the closed ball around $a$ of radius $|f(a)/f'(a)|_p$. Thus $|f'(a_{n+1}) - f'(a_n)|_p < |f'(a)|_p = |f'(a_n)|_p$, so $|f'(a_{n+1})|_p = |f'(a_n)|_p = |f'(a)|_p$. We have shown $|f'(a_n)|_p = |f'(a)|_p$ for all $n$, and letting $n 	o \infty$ gives us $|f'(lpha)|_p = |f'(a)|_p$. $\square$

It is worthwhile to compare the recursions from Newton's method and from the contraction mapping theorem:

- Newton's method: $a_{n+1} = a_n - \dfrac{f(a_n)}{f'(a_n)}$, with $a_1 = a$ and $|f(a)|_p < |f'(a)|_p^2$.
- Contraction mapping: $a_{n+1} = a_n - \dfrac{f(a_n)}{f'(a)}$, with $a_1 = a$ and $|f(a)|_p < |f'(a)|_p^2$.

<!-- page 15 -->

The difference is the denominators $f'(a_n)$ and $f'(a)$, and this has a profound effect on the rate of convergence. In Newton's method, (5.7) tells us

$$|lpha - a_n|_p \leq |f'(a)|_p \left|rac{f(a)}{f'(a)^2}ight|_p^{2^{n-1}}. 	ag{6.6}$$

To find an estimate on $|lpha - a_n|_p$ from the contraction mapping theorem, the recursion given by (6.5) implies $|a_{n+1} - a_n|_p = |arphi^{n-1}(a_2) - arphi^{n-1}(a_1)|_p \leq |a_2 - a_1|_p \lambda^{n-1}$ for all $n \geq 1$, where $a_2 - a_1 = f(a)/f'(a)$ and $\lambda = |f(a)/f'(a)^2|_p$. If $m > n$ the strong triangle inequality implies

$$|a_m - a_n|_p \leq \max_{n \leq j \leq m-1} |a_{j+1} - a_j|_p \leq |a_2 - a_1|_p \lambda^{n-1} = \left|rac{f(a)}{f'(a)}ight|_p \lambda^{n-1}.$$

Letting $m 	o \infty$ yields

$$oxed{|lpha - a_n|_p \leq \left|rac{f(a)}{f'(a)}ight|_p \left|rac{f(a)}{f'(a)^2}ight|_p^{n-1}.} 	ag{6.7}$$

The upper bound in (6.6) goes to 0 much faster than the upper bound in (6.7), so we *anticipate* that $|lpha - a_n|_p 	o 0$ faster when $\{a_n\}$ comes from Newton's recursion compared to the contraction mapping recursion. For instance, if $|f(a)/f'(a)^2|_p = 1/p$, then the bound in (6.6) goes to 0 like $(1/p)^{2^{n-1}}$ while in (6.7) the bound goes to 0 like $(1/p)^n$, so there is at least a doubling of correct $p$-adic digits in each step of Newton's recursion while we expect at most one new correct $p$-adic digit at each step by the contraction mapping recursion.

**Example 6.1.** Let $f(X) = X^2 - 7$ with $a = 1$, so $|f(a)/f'(a)^2|_3 = 1/3$. The sequence $\{a_n\}$ produced from the contraction mapping recursion (6.5) with $a_1 = 1$ has a limit $lpha$ and with a computer we find $|lpha - a_n|_3 = (1/3)^n$ for $1 \leq n \leq 10$. The sequence $\{a_n\}$ based on Newton's recursion in Example 5.1 with $a_1 = 1$ has the same limit $lpha$, but a computer tells us that $|lpha - a_n|_3 = (1/3)^{2^{n-1}}$ for $1 \leq n \leq 10$, which is much smaller than $(1/3)^n$.

## 7. The Inevitability of $|f(a)|_p < |f'(a)|_p^2$

In Theorem 4.1 we have $|f'(lpha)|_p = |f'(a)|_p 
eq 0$, so Hensel's lemma produces a simple root $lpha$ of $f(X)$ in $\mathbf{Z}_p$ that is close to $a$. The criterion $|f(a)|_p < |f'(a)|_p^2$ in Theorem 4.1 is not just a sufficient condition for there to be a simple root of $f(X)$ near $a$ but it is also necessary, as the next theorem makes precise.

**Theorem 7.1.** *If $f(X) \in \mathbf{Z}_p[X]$ has a simple root $lpha$ in $\mathbf{Z}_p$, then for all $a \in \mathbf{Z}_p$ that are close enough to $lpha$ we have $|f'(a)|_p = |f'(lpha)|_p$ and $|f(a)|_p < |f'(a)|_p^2$. In particular, these conditions hold when $|a - lpha|_p < |f'(lpha)|_p$.*

*Proof.* By (5.4) with $F(X) = f'(X)$, $|f'(lpha) - f'(a)|_p \leq |lpha - a|_p < |f'(lpha)|_p$. Thus $|f'(a)|_p = |f'(lpha)|_p$. By (5.3) with $F(X) = f(X)$,

$$f(a) = f(lpha + (a - lpha)) = f(lpha) + f'(lpha)(a - lpha) + z(a - lpha)^2 = f'(lpha)(a - lpha) + z(a - lpha)^2$$

for some $z \in \mathbf{Z}_p$. Both terms on the right side have absolute value less than $|f'(lpha)|_p^2$ since $|a - lpha|_p < |f'(lpha)|_p$, so $|f(a)|_p < |f'(lpha)|_p^2 = |f'(a)|_p^2$. $\square$

## 8. Hensel's Lemma for Power Series

Hensel's lemma can be applied to $p$-adic power series, not just polynomials. By "$p$-adic power series" we have in mind those with $\mathbf{Z}_p$-coefficients, which we will call power series "over $\mathbf{Z}_p$". We will consider such series of two types: those that converge on $\mathbf{Z}_p$ and those that converge on $p\mathbf{Z}_p$ but not necessarily on $\mathbf{Z}_p$ (*e.g.*, $e^X$ for $p > 2$). To prove Hensel's lemma for these two types of power series, we will use the following power series analogue of (5.3) and (5.4).

<!-- page 16 -->

**Lemma 8.1.** *Let $F(X)$ be a power series with coefficients in $\mathbf{Z}_p$ that converges on $\mathbf{Z}_p$.*

1. *For $x$ and $y$ in $\mathbf{Z}_p$, $F(x + y) = F(x) + F'(x)y + zy^2$ for some $z \in \mathbf{Z}_p$.*
2. *For $x$ and $y$ in $\mathbf{Z}_p$, $|F(x) - F(y)|_p \leq |x - y|_p$.*

*If $F(X)$ converges on $p\mathbf{Z}_p$ but not necessarily on $\mathbf{Z}_p$, then (1) and (2) are true for $x, y \in p\mathbf{Z}_p$.*

*Proof.* Let $F(X) = \sum_{i \geq 0} c_i X^i$, so $c_i \in \mathbf{Z}_p$. Convergence of $F(X)$ on $\mathbf{Z}_p$ implies $c_i 	o 0$ as $i 	o \infty$. To prove (1), the analogue of (5.3), for $x$ and $y$ in $\mathbf{Z}_p$ we have

$$F(x + y) = \sum_{i \geq 0} c_i(x + y)^i$$
$$= c_0 + \sum_{i \geq 1} c_i(x^i + ix^{i-1}y + g_i(x, y)y^2) 	ext{ where } g_i(x, y) \in \mathbf{Z}_p[x, y] \subset \mathbf{Z}_p$$
$$= \sum_{i \geq 0} c_i x^i + \sum_{i \geq 1} ic_i x^{i-1}y + \sum_{i \geq 2} c_i g_i(x, y)y^2,$$

where we can break apart the series since $|c_i|_p 	o 0$ as $i 	o \infty$ and the numbers $x$, $y$, and $g_i(x, y)$ are all in $\mathbf{Z}_p$ (all the series converge) with $g_1(x, y) = 0$. Thus

$$F(x + y) = F(x) + F'(x)y + zy^2$$

where $z = \sum_{i \geq 2} c_i g_i(x, y) \in \mathbf{Z}_p$.

To prove (2), the analogue of (5.4), we use $|x^i - y^i|_p \leq |x - y|_p$ for all $x, y \in \mathbf{Z}_p$ and $i \geq 0$:

$$F(x) - F(y) = \sum_{i \geq 1} c_i(x^i - y^i) \implies |F(x) - F(y)|_p \leq \max_{i \geq 1} |c_i|_p |x^i - y^i|_p \leq \max_{i \geq 1} |c_i|_p |x - y|_p,$$

which is at most $|x - y|_p$ since all $|c_i|_p$ are at most 1.

If $F(X)$ converges on $p\mathbf{Z}_p$ but not necessarily on $\mathbf{Z}_p$, so the coefficients $c_i$ are in $\mathbf{Z}_p$ but need not tend to 0, the proofs of (1) and (2) remain valid for $x, y \in p\mathbf{Z}_p$ after checking some details: in the proof of (1), the series for $F(x)$ and $F'(x)$ converge when $x \in \mathbf{Z}_p$, while the series $\sum_{i \geq 1} c_i g_i(x, y)$ converges since $|g_i(x, y)|_p \leq \max(|x|_p, |y|_p)^{i-2}$ by the binomial theorem that gave rise to $g_i(x, y)$. The proof of (2) carries over with no changes at all provided $x, y \in p\mathbf{Z}_p$ so that $F(x)$ and $F(y)$ converge. $\square$

Here is a power series version of Theorem 4.1 for series over $\mathbf{Z}_p$ that converge on $\mathbf{Z}_p$.

**Theorem 8.2.** *Let $f(X)$ be a power series with coefficients in $\mathbf{Z}_p$ that converges on $\mathbf{Z}_p$. If an $a \in \mathbf{Z}_p$ satisfies*

$$|f(a)|_p < |f'(a)|_p^2$$

*then there is a unique $lpha \in \mathbf{Z}_p$ such that $f(lpha) = 0$ in $\mathbf{Z}_p$ and $|lpha - a|_p < |f'(a)|_p$. Moreover,*

1. *$|lpha - a|_p = |f(a)/f'(a)|_p < |f'(a)|_p$,*
2. *$|f'(lpha)|_p = |f'(a)|_p$.*

In this theorem, $f'(a)$ makes sense for $a \in \mathbf{Z}_p$ since $f'(X)$ converges on $\mathbf{Z}_p$: the coefficients of $f(X)$ tend to 0 since $f(1)$ converges so the coefficients of $f'(X)$ also tend to 0 and thus $f'(X)$ converges on $\mathbf{Z}_p$.

*Proof.* Using Lemma 8.1 in place of (5.3) and (5.4), the proof of Theorem 4.1 using Newton's method carries over word for word to the setting of power series with $\mathbf{Z}_p$-coefficients that converge on $\mathbf{Z}_p$. $\square$

<!-- page 17 -->

**Remark 8.3.** Theorem 8.2 can also be proved by turning the power series $f(X)$ into a polynomial, thereby reducing to the polynomial case. The $p$-adic Weierstrass preparation theorem says $f(X) = W(X)U(X)$ where $W(X)$ is a polynomial in $\mathbf{Z}_p[X]$ and $U(X)$ is a unit power series with coefficients in $\mathbf{Z}_p$ that converges on $\mathbf{Z}_p$ (this means $U(X)V(X) = 1$ for some power series $V(X)$ with $\mathbf{Z}_p$-coefficients that converges on $\mathbf{Z}_p$). From $f(a) = W(a)U(a)$ and $U(a)V(a) = 1$ for all $a \in \mathbf{Z}_p$, roots of $f(X)$ in $\mathbf{Z}_p$ are the same as roots of $W(X)$ in $\mathbf{Z}_p$. If $|f(a)|_p < |f'(a)|_p^2$ then $|f(a)|_p = |W(a)|_p$ since $|U(a)|_p = 1$, and also $|f'(a)|_p = |W'(a)|_p$ since from $f'(a) = W'(a)U(a) + W(a)U'(a)$ and $|W(a)U'(a)|_p \leq |W(a)|_p = |f(a)|_p < |f'(a)|_p$ we must have $|f'(a)|_p = |W'(a)U(a)|_p = |W'(a)|_p$. Thus $|W(a)|_p < |W'(a)|_p^2$, so there is a unique $lpha \in \mathbf{Z}_p$ fitting the conclusion of Theorem 4.1 for $W(X)$. It is left to the reader to check $lpha$ also fits the uniqueness conditions in Theorem 8.2 for $f(X)$.

The basic version of Hensel's lemma is true for power series as a special case of the strong version proved above: if $f(X)$ is a power series over $\mathbf{Z}_p$ that converges on $\mathbf{Z}_p$ and an $a \in \mathbf{Z}_p$ satisfies $f(a) \equiv 0 mod p$ and $f'(a) 
ot\equiv 0 mod p$ then there is a unique $lpha \in \mathbf{Z}_p$ such that $f(lpha) = 0$ and $lpha \equiv a mod p$.

Like Theorem 5.4, the basic and strong form of Hensel's lemma for power series with $\mathbf{Z}_p$-coefficients that converge on $\mathbf{Z}_p$ are equivalent, with a proof similar to the polynomial case, but care is needed since part of the proof uses convergent power series in two variables. Details are left to the reader. Check also that Theorem 7.1 and its proof carry over to power series over $\mathbf{Z}_p$ that converge on $\mathbf{Z}_p$, where a simple root of a power series is a root at which the derivative is nonzero.

For power series over $\mathbf{Z}_p$ that converge on $p\mathbf{Z}_p$ but not necessarily on $\mathbf{Z}_p$, here is a version of Hensel's Lemma.

**Theorem 8.4.** *Let $f(X)$ be a power series with coefficients in $\mathbf{Z}_p$ that converges on $p\mathbf{Z}_p$. If an $a \in p\mathbf{Z}_p$ satisfies*

$$|f(a)|_p < |f'(a)|_p^2$$

*then there is a unique $lpha \in p\mathbf{Z}_p$ such that $f(lpha) = 0$ in $\mathbf{Z}_p$ and $|lpha - a|_p < |f'(a)|_p$. Moreover,*

1. *$|lpha - a|_p = |f(a)/f'(a)|_p < |f'(a)|_p$,*
2. *$|f'(lpha)|_p = |f'(a)|_p$.*

*Proof.* The proof of Theorem 8.2 (including its use of Lemma 8.1) carries over with the complete space $p\mathbf{Z}_p$ replacing the complete space $\mathbf{Z}_p$ as the set containing the approximate roots $a_n$ and the root $lpha$ that is their limit. $\square$

**Remark 8.5.** The reduction of Theorem 8.2 to the case of polynomials in Remark 8.3 applies to Theorem 8.4 too by using a $p$-adic Weierstrass preparation theorem for power series with $\mathbf{Z}_p$-coefficients that converge on $p\mathbf{Z}_p$ (but perhaps not on $\mathbf{Z}_p$).

In the proof of Hensel's lemma for polynomials by Newton's method, the bounds on $|f(a_n)|_p$ and $|a_{n+1} - a_n|_p$ carry over to Hensel's lemma for power series, whether in the form of Theorem 8.2 or 8.4: $|f(a_n)|_p \leq |f'(a)|_p(|f(a)|_p/|f'(a)^2|_p)^{2^{n-1}}$ and $|a_{n+1} - a_n|_p \leq |f'(a)|_p|f(a)/f'(a)^2|_p^{2^{n-1}}$. Using the strong triangle inequality in the second bound for $a_m - a_n = (a_m - a_{m-1}) + \cdots + (a_{n+1} - a_n)$ when $m > n$ and then letting $m 	o \infty$, we get the bound from (5.7) all over again, but this time for power series:

$$oxed{|lpha - a_n|_p \leq |f'(a)|_p \left|rac{f(a)}{f'(a)^2}ight|_p^{2^{n-1}}.} 	ag{8.1}$$

**Example 8.6.** For $c \in \mathbf{Z}_p$, set $(1 + X)^c = \sum_{n \geq 0} inom{c}{n} x^n$, where $inom{c}{n} = rac{c(c-1)\cdots(c-n+1)}{n!}$. Since $c$ is a $p$-adic limit of positive integers (use truncations of the $p$-adic expansion of $c$), the

<!-- page 18 -->

number $inom{c}{n}$ is a $p$-adic limit of integers and thus $inom{c}{n} \in \mathbf{Z}_p$. For $c \in \mathbf{Z}_p - \{0, 1, 2, 3, \ldots\}$, $inom{c}{n} \in \mathbf{Z}_p^	imes$ infinitely often (for those $n$ whose base $p$ expansion is an initial part of the $p$-adic expansion of $c$), so $(1 + X)^c$ has coefficients in $\mathbf{Z}_p$ that do not tend to 0 and thus $(1 + X)^c$ converges on $p\mathbf{Z}_p$ but not on $\mathbf{Z}_p$.

Consider $f(X) = (1 + X)^{\sqrt{7}} - 10$, where $\sqrt{7} = 1 + 3 + 3^2 + 2 \cdot 3^4 + \cdots$ in $\mathbf{Z}_3$. For each $a \in 3\mathbf{Z}_3$, $f(a) \equiv 0 mod 3$ and $f'(a) = \sqrt{7}(1 + a)^{\sqrt{7}-1} \equiv \sqrt{7} 
ot\equiv 0 mod 3$, so by Theorem 8.4 there is a unique solution to $f(lpha) = 0$ in $3\mathbf{Z}_3$ by using Newton's method with initial value $a_1 = a$. Taking $a = 0$, $f(a_1) = -9$ and $f'(a_1) = \sqrt{7} 
ot\equiv 0 mod 3$. Using (8.1) for $f(X) = (1 + X)^{\sqrt{7}} - 10$, $|lpha - a_n|_3 \leq (1/9)^{2^{n-1}} = (1/3)^{2^n}$. Taking $n = 3$,

$$lpha \equiv a_3 \equiv 3^2 + 2 \cdot 3^3 + 2 \cdot 3^4 + 3^5 + 2 \cdot 3^6 mod 3^8. 	ag{8.2}$$

The number on the right is 1926. As a reality check,[^5] let us confirm that $f(a_3)$ is 3-adically small. Since $|f(x) - f(y)|_3 \leq |x - y|_3$ for $x, y \in \mathbf{Z}_3$, $f(a_3) \equiv f(1926) mod 3^8$. Since 1926 is divisible by 9, so $1926^n \equiv 0 mod 3^8$ for $n \geq 4$, and the power series coefficients of $f(X)$ are all in $\mathbf{Z}_3$, $f(1926) \equiv -9 + \sum_{n=1}^3 inom{\sqrt{7}}{n} 1926^n mod 3^8$. With a computer, the right side is 0 mod $3^8$.

**Example 8.7.** For $p > 2$ and $c \in 1 + p\mathbf{Z}_p$, set $f(X) = e^X - c$. The $p$-adic disc of convergence for $e^X$ (and thus for $e^X - c$) on $\mathbf{Q}_p$ is $p\mathbf{Z}_p$. Since $f(0) = 1 - c$ and $f'(0) = 1$, we have $|f(0)|_p \leq 1/p$ and $|f'(0)|_p = 1$. Therefore Theorem 8.4 tells us there is a unique $lpha \in p\mathbf{Z}_p$ such that $e^lpha = c$ and $|lpha|_p < 1$, and in fact $|lpha|_p = |f(0)|_p = |c - 1|_p$. This $lpha$ in $p\mathbf{Z}_p$ for which $e^lpha = c$ is the $p$-adic logarithm of $c$.

By (8.1) with $a = 0$, $|lpha - a_n|_p \leq |1 - c|_p^{2^{n-1}}$. For instance, if we want to solve $e^lpha = -2$ for $lpha \in 3\mathbf{Z}_3$ and compute $lpha mod 3^5$, use Newton's method with $f(x) = e^x + 2$. Then $|lpha - a_n|_3 \leq |1 - (-2)|_3^{2^{n-1}} = 1/3^{2^{n-1}}$. The upper bound is at most $1/3^5$ for $n \geq 4$, so take $n = 4$. The Newton's method recursion is $a_{n+1} = a_n - f(a_n)/f'(a_n) = a_n - (e^{a_n} + 2)/e^{a_n} = a_n - 1 - 2/e^{a_n}$. By computer, the term for $a_4$ in the table below satisfies $e^{a_4} \equiv -2 mod 3^{15}$.

| $n$ | $a_n$ |
|-----|-------|
| 1 | 0 |
| 2 | $-3$ |
| 3 | $2 \cdot 3 + 2 \cdot 3^2 + 3^5 + 2 \cdot 3^7 + 2 \cdot 3^{10} + \cdots$ |
| 4 | $2 \cdot 3 + 2 \cdot 3^2 + 3^5 + 3^6 + 2 \cdot 3^8 + 3^9 + \cdots$ |

## 9. Hensel's Lemma Beyond $\mathbf{Q}_p$

The proofs of Hensel's lemma work for polynomials with coefficients in a field $K$ complete with respect to an absolute value satisfying the strong triangle inequality: $|x + y| \leq \max(|x|, |y|)$ for all $x$ and $y$ in $K$. Set $\mathfrak{o} = \{x \in K : |x| \leq 1\}$.

**Theorem 9.1.** *For $\mathfrak{o}$ as above and a polynomial $f(X)$ with coefficients in $\mathfrak{o}$, assume some $a \in \mathfrak{o}$ satisfies*

$$|f(a)| < |f'(a)|^2.$$

*Then there is a unique $lpha \in \mathfrak{o}$ such that $f(lpha) = 0$ in $\mathfrak{o}$ and $|lpha - a| < |f'(a)|$. Moreover,*

1. *$|lpha - a| = |f(a)/f'(a)| < |f'(a)|$,*
2. *$|f'(lpha)| = |f'(a)| 
eq 0$.*

*Conversely, if $f(X)$ has a simple root $lpha \in \mathfrak{o}$, then for $a \in K$ such that $|a - lpha| < |f'(lpha)|$ then we have $|f'(a)| = |f'(lpha)|$ and $|f(a)| < |f'(a)|^2$.*

[^5]: Should this be called a 3-adicity check, since we are not working over the reals?

<!-- page 19 -->

Theorems 5.4 and 7.1 also carry over to $\mathfrak{o}[X]$, with the same proofs (the proofs over $\mathbf{Z}_p$ were written specifically to make sure the proofs carry over to $\mathfrak{o}$ with no changes):

**Theorem 9.2.** *The following properties $\mathfrak{o}[X]$ are equivalent.*

1. *When $f(X) \in \mathfrak{o}[X]$ and there is an $a \in \mathfrak{o}$ such that $|f(a)| < 1$ and $|f'(a)| = 1$, there is a unique $lpha \in \mathfrak{o}$ such that $f(lpha) = 0$ in $\mathfrak{o}$ and $|lpha - a| < 1$,*
2. *When $f(X) \in \mathfrak{o}[X]$ and there is an $a \in \mathfrak{o}$ such that $|f(a)| < |f'(a)|^2$, there is a unique $lpha \in \mathfrak{o}$ such that $f(lpha) = 0$ in $\mathfrak{o}$ and $|lpha - a| < |f'(a)|$, and in fact $|lpha - a|_p = |f(a)/f'(a)|_p$.*

**Theorem 9.3.** *If $f(X) \in \mathfrak{o}[X]$ has a simple root $lpha$ in $\mathfrak{o}$, then for all $a \in \mathfrak{o}$ that are close enough to $lpha$ we have $|f'(a)| = |f'(lpha)|$ and $|f(a)| < |f'(a)|^2$. In particular, these conditions hold when $|a - lpha| < |f'(lpha)|$.*

For power series, everything written about power series with coefficients in $\mathbf{Z}_p$ in Section 8 carries over to power series with coefficients in $\mathfrak{o}$: all such power series converge on the maximal ideal $\mathfrak{m} = \{x \in \mathfrak{o} : |x| < 1\}$, and those with coefficients tending to 0 converge on $\mathfrak{o}$. We record below the statements of Hensel's lemma for both types of power series, leaving the proofs (similar to the polynomial case in most respects) to the reader.

**Theorem 9.4.** *Let $f(X)$ be a power series with coefficients in $\mathfrak{o}$ that converges on $\mathfrak{o}$. If an $a \in \mathfrak{o}$ satisfies*

$$|f(a)| < |f'(a)|^2$$

*then there is a unique $lpha \in \mathfrak{o}$ such that $f(lpha) = 0$ in $\mathfrak{o}$ and $|lpha - a| < |f'(a)|$. Moreover,*

1. *$|lpha - a| = |f(a)/f'(a)| < |f'(a)|$,*
2. *$|f'(lpha)| = |f'(a)|$.*

**Theorem 9.5.** *Let $f(X)$ be a power series with coefficients in $\mathfrak{o}$, so it converges on $\mathfrak{m}$. If an $a \in \mathfrak{m}$ satisfies*

$$|f(a)| < |f'(a)|^2$$

*then there is a unique $lpha \in \mathfrak{m}$ such that $f(lpha) = 0$ in $\mathfrak{o}$ and $|lpha - a| < |f'(a)|. Moreover,*

1. *$|lpha - a| = |f(a)/f'(a)| < |f'(a)|$,*
2. *$|f'(lpha)| = |f'(a)|$.*

## 10. Hensel's Lemma with Submultiplicative Absolute Values

We will formulate a version of Hensel's lemma where $\mathbf{Z}_p$ is replaced by a ring $A$ that is complete with respect to an absolute value similar to $|\cdot|_p$ where multiplicativity is replaced by submultiplicativity.

**Definition 10.1.** A *submultiplicative absolute value* $|\cdot|$ on a nonzero commutative ring $A$ is a function $|\cdot|: A 	o \mathbf{R}$ such that for all $a$ and $b$ in $A$,

- (i) $0 \leq |a| \leq 1$ with $|a| = 0$ if and only if $a = 0$,
- (ii) $|a + b| \leq \max(|a|, |b|)$ (strong triangle inequality),
- (iii) $|ab| \leq |a||b|$ (submultiplicative).

For an ordinary absolute value, $|1| = 1$ by multiplicativity since $|1| = |1^2| = |1|^2$. When we have submultiplicativity, we can still get $|1| = 1$ when $|a| \leq 1$ for all $a$: $|1| = |1^2| \leq |1|^2$ and $|1| > 0$, so $1 \leq |1|$. Since the reverse inequality $|1| \leq 1$ holds by definition, we get $|1| = 1$. Therefore $|-a| = |a|$: $|-a| \leq |-1||a| \leq |a|$ and $|a| = |-(-a)| \leq |-1||-a| \leq |-a|$.

On $A$ we have a metric $ho(a, b) = |a - b|$; (that $ho(a, b) = ho(b, a)$ follows from $|a - b| = |b - a|$ because $|x| = |-x|$). Many basic properties of $|\cdot|_p$ on $\mathbf{Z}_p$ remain true for a submultiplicative absolute value, with the same or very similar proofs. For example, addition and multiplication on $A$ are continuous and a sequence $\{a_n\}$ in $A$ is Cauchy if and only if $|a_{n+1} - a_n| 	o 0$.

<!-- page 20 -->

Before describing a form of Hensel's lemma for polynomials and power series with coefficients in a ring complete for a submultiplicative absolute value, let us describe a source of examples of submultiplicative absolute values using powers of an ideal.

Let $A$ be a nonzero commutative ring containing an ideal $I$ such that $igcap_{n \geq 0} I^n = \{0\}$, where $I^n$ is the $n$th power of $I$ as an ideal[^6]. For $a 
eq 0$ in $A$, set $|a|_I = (1/2)^n$ if $a \in I^n$ for $n$ as large as possible (there is a maximal $n$ such that $a \in I^n$ because $igcap_{n \geq 0} I^n = \{0\}$), and set $|0|_I = 0$. Then $0 \leq |a|_I \leq 1$ and $|a|_I = 0$ only when $a = 0$.[^7] We have $|a|_I ho = (1/2)^n \Rightarrow a \in I^n$ and $a \in I^n \Rightarrow |a|_I \leq (1/2)^n$ (the exponent $n$ in the second implication might not be maximal for the choice of $a$). That $|a + b|_I \leq \max(|a|_I, |b|_I)$ is left to the reader. The function $ho_I(a, b) = |a - b|_I$ is called the *$I$-adic metric* on $A$. To prove submultiplicativity of $|\cdot|_I$ on $A$, if $a$ and $b$ are nonzero in $A$ with $|a|_I = (1/2)^n$ and $|b|_I = (1/2)^m$ then $ab \in I^{n+m}$, so $|ab|_I \leq (1/2)^{n+m} = |a|_I |b|_I$. Obviously $|ab|_I \leq |a|_I |b|_I$ if $a$ or $b$ is 0.

We have $A = I^0 \supset I \supset I^2 \supset I^3 \supset \cdots$ and elements of $I^n$ are considered $I$-adically small if $n$ is large. A sequence $\{a_j\}$ in $A$ is *$I$-adically Cauchy* if for each $n \geq 1$ there is $j \geq 1$ such that $a_{j'} - a_{j''} \in I^n$ for all $j', j'' \geq j$. This is equivalent to $a_{j+1} - a_j \in I^n$ for all large $j$ (depending on $n$) and is the same as $\{a_j\}$ being a Cauchy sequence for the metric $ho_I$. We say $A$ is *$I$-adically complete* if each $I$-adic Cauchy sequence in $A$ converges in $A$.

An example of such a ring $A$ and ideal $I$ is $R[T]$ and $I = (T) = TR[T]$ where $R$ is a commutative ring. Then $I^n = (T^n)$, which is the set of polynomials with no terms in degree less than $n$, so $igcap_{n \geq 1} I^n = \{0\}$. The $I$-adic absolute value on $R[T]$ is called the $T$-adic absolute value and is denoted $|\cdot|_T$. We have $|f(T)|_T = (1/2)^n$ if and only if the lowest-degree nonzero term in $f(T)$ has degree $n$. The ring $R[T]$ is *not* $T$-adically complete since, for instance, the partial sums $s_n = 1 + T + T^2 + \cdots + T^n$ form a $T$-adic Cauchy sequence that has no limit in $R[T]$: $(1 - T)s_n = 1 - T^{n+1}$, which tends to 1, so if $\{s_n\}$ has a limit $s$ in $R[T]$ then $(1 - T)s = 1$, but $1 - T$ has no multiplicative inverse in $R[T]$.

Another example is the ring $R[[T]]$ of formal power series $\sum_{n \geq 0} c_n T^n$ with $c_n \in R$ and the ideal $I = (T) = TR[[T]]$ consisting of multiples of $T$ in $R[[T]]$ (the power series with constant term 0). The $T$-adic absolute value $|\cdot|_T$ on $R[[T]]$ is defined in the same way as on $R[T]$, and $R[T]$ is dense in $R[[T]]$: the sum of all terms in a power series with degree less than $n$ is in $R[T]$ and differs from the power series by a series in $I^n$, and we can take $n$ arbitrarily large. The ring $R[[T]]$ is $T$-adically complete: a $T$-adic Cauchy sequence has the coefficients in each degree eventually constant, leading to a candidate limit series in $R[[T]]$ that really is the limit of the sequence. So $R[[T]]$ is the $T$-adic completion of $R[T]$. For example, the sequence $s_n = 1 + T + T^2 + \cdots + T^n$ in $R[[T]]$ converges to $\sum_{n \geq 0} T^n$, which is a multiplicative inverse of $1 - T$.

More generally, consider the ring $R[T_1, \ldots, T_d]$ and $I = (T_1, \ldots, T_d)$, so $I^n$ is the polynomials in $R[T_1, \ldots, T_d]$ having no nonzero terms in degree below $n$. Then $|f(T_1, \ldots, T_d)|_I = (1/2)^n$ means the lowest-degree nonzero monomial in $f(T_1, \ldots, T_d)$ has degree $n$. This ring is not $I$-adically complete, but the ring $R[[T_1, \ldots, T_d]]$ of formal power series in $d$ indeterminates is complete with respect to its ideal $I = (T_1, \ldots, T_d)$ of formal power series with constant term 0 and $R[T_1, \ldots, T_d]$ is dense in $R[[T_1, \ldots, T_d]]$.

**Remark 10.2.** On $\mathbf{Z}[T]$ we can consider the $I$-adic absolute value when $I$ is $(p)$, $(T)$, and $(p, T)$. What is the difference?

1. Being $p$-adically small means all the coefficients are highly divisible by $p$.
2. Being $T$-adically small means the polynomial has no low-degree terms.
3. Being $(p, T)$-adically small means low-degree coefficients are highly divisible by $p$.

[^6]: $I^n$ is the ideal generated by $n$-fold products $a_1 \cdots a_n$ for $a_i \in I$. It is *more* than all $a^n$ for $a \in I$.
[^7]: The role of $1/2$ in the definition of $|a|_I$ when $a 
eq 0$ could be replaced by an arbitrary number strictly between 0 and 1. The main point is that $|a|_I$ is very small when $a \in I^n$ for large $n$.

<!-- page 21 -->

The $p$-adic completion of $\mathbf{Z}[T]$ is the set of power series $\sum_{n \geq 0} c_n T^n$ where $c_n \in \mathbf{Z}_p$ and $c_n 	o 0$, the $T$-adic completion of $\mathbf{Z}[T]$ is $\mathbf{Z}[[T]]$, and the $(p, T)$-adic completion of $\mathbf{Z}[T]$ is $\mathbf{Z}_p[[T]]$. The ring $\mathbf{Z}_p[[T]]$ is both $T$-adically and $(p, T)$-adically complete, but these notions of convergence are different. A sequence in $\mathbf{Z}_p[[T]]$ that converges $T$-adically also converges $(p, T)$-adically since $(T)^n \subset (p, T)^n$ as ideals in $\mathbf{Z}_p[[T]]$, but the converse is false: a sequence in $\mathbf{Z}_p$ that converges $p$-adically does not converge $T$-adically when viewed as constants in $\mathbf{Z}_p[[T]]$. And $\mathbf{Z}[T]$ is $(p, T)$-adically dense in $\mathbf{Z}_p[[T]]$ but is not $T$-adically dense in $\mathbf{Z}_p[[T]]$: for $c \in \mathbf{Z}_p - \mathbf{Z}$, no $f(T) \in \mathbf{Z}[T]$ satisfies $|c - f(T)|_T < 1$ since such an inequality forces $f(0) = c$ but $f(0) \in \mathbf{Z}$ and $c 
otin \mathbf{Z}$.

**Lemma 10.3.** *Let $A$ be a nonzero commutative ring that is complete with respect to a submultiplicative absolute value $|\cdot|$.*

1. *$|ua| = |a|$ for all $u \in A^	imes$ and $a \in A$.*
2. *If $y \in A$ satisfies $|y| < 1$ then $1 + y \in A^	imes$.*
3. *The units of $A$ are closed in $A^	imes$: if $\{u_n\}$ is a sequence in $A^	imes$ with a limit in $A$, then the limit is in $A^	imes$.*

*Proof.* (1) For $u \in A^	imes$ and $a \in A$, $|ua| \leq |u||a| \leq |a|$. For the reverse inequality, let $uv = 1$ in $A$, so $|a| = |ua(v)| \leq |ua||v| \leq |ua|$.

(2) We use a geometric series: the partial sums $s_n = 1 - y + y^2 - y^3 + \cdots + (-y)^n$ are a Cauchy sequence in $A$ by the strong triangle inequality since $|(-y)^n| \leq |y|^n 	o 0$ as $n 	o \infty$. Let $s = \lim_{n 	o \infty} s_n$ in $A$, so $(1 + y)s = \lim_{n 	o \infty} (1 + y)s_n = \lim_{n 	o \infty} 1 - (-y)^n = 1$. Thus $1 + y \in A^	imes$.

(3) Let $u_n 	o L$ in $A$. Set $v_n = 1/u_n$, so $v_{n+1} - v_n = v_n v_{n+1}(u_n - u_{n+1})$. Thus $|v_{n+1} - v_n| \leq |u_n - u_{n+1}| 	o 0$ as $n 	o \infty$. Therefore $\{v_n\}$ is Cauchy in $A$. Let $M$ be its limit, so $u_n v_n 	o LM$ by continuity of multiplication. Also $u_n v_n = 1$ for all $n$, so $LM = 1$. Thus $L \in A^	imes$. $\square$

**Example 10.4.** A power series $f(T) \in R[[T]]$ is a unit if and only if its constant term $f(0)$ is a unit in $R$. Indeed, if $f(T)g(T) = 1$ then the constant terms have product 1, so $f(0) \in R^	imes$. Conversely, if $f(0) \in R^	imes$ then we can prove $f(T) \in R[[T]]^	imes$ by writing $f(T) = f(0) + TF(T) = f(0)(1 + (1/f(0))TF(T))$. The first factor $f(0)$ is a unit in $R[[T]]$ since it is a unit in $R$ and the second factor $1 + (1/f(0))TF(T)$ is a unit in $R[[T]]$ by Lemma 10.3(2).

In contrast to $\mathbf{Z}_p$, where the condition $a \in \mathbf{Z}_p^	imes$ means the same thing as $|a|_p = 1$, there is a difference in $R[[T]]$ between $|f(T)|_T = 1$ and $f(T) \in R[[T]]^	imes$ unless $R$ is a field: a power series $f(T) \in R[[T]]$ has $|f(T)|_T = 1$ when its constant term is in $R - \{0\}$, while $f(T)$ is a unit in $R[[T]]$ only when its constant term is in $R^	imes$, and that is more restrictive than $|f(T)|_T = 1$ unless $R^	imes = R - \{0\}$ (*i.e.*, unless $R$ is a field). For instance, in $\mathbf{Z}[[T]]$ we have $|2 + T|_T = 1$ and $2 + T$ is not a unit in $\mathbf{Z}[[T]]$. More generally, if $A$ is a ring and $I$ is an ideal of $A$ such that $igcap_{n \geq 0} I^n = \{0\}$, if $a \in A^	imes$ then $|a|_I = (1/2)^0 = 1$ because no unit is contained in $I$ (otherwise the powers of $I$ could not have intersection $\{0\}$), but the converse might not be true.

Now we can present a basic form of Hensel's lemma in $A[X]$.

**Theorem 10.5.** *Let $f(X) \in A[X]$, where $A$ is a nonzero commutative ring complete with respect to a submultiplicative absolute value $|\cdot|$. If an $a \in A$ satisfies $|f(a)| < 1$ and $f'(a) \in A^	imes$ then there is a unique $lpha \in A$ such that $f(lpha) = 0$ in $A$ and $|lpha - a| < 1$. Moreover,*

1. *$|lpha - a| = |f(a)| < 1$,*
2. *$f'(lpha) \in A^	imes$.*

<!-- page 22 -->

Note the condition on $f'(a)$ is $f'(a) \in A^	imes$, *not* $|f'(a)| = 1$; being a unit in $A$ is potentially more precise than having absolute value 1.

*Proof.* The proof is like that of Theorem 4.1: set $a_1 = a$ and $a_{n+1} = a_n - f'(a_n)/f'(a_n)$ and check by induction that $f'(a_n) \in A^	imes$ and $|f(a_n)| \leq |f(a)|^{2^{n-1}}$ for all $n \geq 1$. You need to be careful not to use multiplicativity on $|\cdot|$ on all products, but it can be used if one factor in a product is a unit in $A$, by Lemma 10.3(1).

The sequence $\{a_n\}$ is Cauchy in $A$ since $|a_{n+1} - a_n| 	o 0$, and letting $lpha = \lim_{n 	o \infty} a_n$, we have $f(lpha) = 0$ since $|f(a_n)| 	o 0$ and polynomials in $A[X]$ are continuous on $A$. We have $f'(lpha) \in A^	imes$ by Lemma 10.3(3) since $f'(a_n) \in A^	imes$ for all $n$ and $f'(X)$ is a polynomial.

The proof that $|lpha - a| = |f(a)|$ is very similar to the case $A = \mathbf{Z}_p$. To prove $lpha$ is the unique root of $f(X)$ such that $|lpha - a| < 1$, we need to be a little more careful than in the case $A = \mathbf{Z}_p$ since $|\cdot|$ is submultiplicative rather than multiplicative. If $eta \in A$ satisfies $f(eta) = 0$ and $|eta - a| < 1$ then $|eta - lpha| < 1$, so $eta = lpha + h$ where $|h| < 1$. Then

$$0 = f(eta) = f(lpha + h) = f(lpha) + f'(lpha)h + zh^2 = f'(lpha)h + zh^2$$

for some $z \in A$. Then $f'(lpha)h = -zh^2$. Taking absolute values of both sides and using Lemma 10.3(1), $|h| = |-zh^2| \leq |h|^2$. Since $|h| < 1$, having $|h| \leq |h|^2$ forces $|h| = 0$, so $h = 0$ and thus $eta = lpha$. $\square$

**Example 10.6.** Let $A = \mathbf{Q}[[T]]$ and $f(X) = X^n - (1 + T) \in \mathbf{Q}[[T]][X] = A[X]$ where $n \geq 1$. Since $|f(1)|_T = |-T|_T < 1$ and $f'(1) = n \in A^	imes$, there is a unique $g(T) \in \mathbf{Q}[[T]]$ such that $g(T)^n = 1 + T$ and $|g(T) - 1|_T < 1$, meaning $g(T) \in 1 + T\mathbf{Q}[[T]]$. This $g(T)$ begins as $1 + (1/n)T + \cdots$ and is the power series $(1 + T)^{1/n}$ in $\mathbf{Q}[[T]]$ with constant term 1. Its full formula is $\sum_{k \geq 0} inom{1/n}{k} T^k$.

Note that if we use $A = \mathbf{Z}[[T]]$ and $f(X) = X^n - (1 + T) \in A[X]$ (same as before), then $|f(1)|_T < 1$ and $f'(1) = n$, so if $n \geq 2$ then $f'(1) 
otin A^	imes$ (a unit in $\mathbf{Z}[[T]]$ has constant term $\pm 1$ by Example 10.4) and there is no solution to $g(T)^n = 1 + T$ in $1 + T\mathbf{Z}[[T]]$: such a solution would also be a solution in $1 + T\mathbf{Q}[[T]]$ and we saw the unique solution in $1 + T\mathbf{Q}[[T]]$ has linear coefficient $1/n$, which is not an integer. This illustrates why in Theorem 10.5 we can not always replace "$f'(a) \in A^	imes$" with "$|f'(a)| = 1$".

We do not really need to replace $\mathbf{Z}[[T]]$ with $\mathbf{Q}[[T]]$ to find a power series solution to $X^n = 1 + T$: we just need $n$ to be a unit in $A$, so we could use $A = \mathbf{Z}[1/n][[T]]$. For example, $\sqrt{1 + T} \in \mathbf{Z}[1/2][[T]]$. Indeed,

$$\sqrt{1 + T} = 1 + rac{1}{2}T - rac{1}{2^3}T^2 + rac{1}{2^4}T^3 - rac{5}{2^7}T^4 + rac{7}{2^8}T^5 - rac{21}{2^{10}}T^6 + \cdots$$

and all coefficients have 2-power denominator. Similarly, $\sqrt[6]{1 + T} \in \mathbf{Z}[1/6][[T]]$:

$$\sqrt[6]{1 + T} = 1 + rac{1}{6}T - rac{15}{6^3}T^2 + rac{55}{6^4}T^3 - rac{8415}{6^7}T^4 + rac{38709}{6^8}T^5 - rac{1122561}{6^{10}}T^6 + \cdots.$$

Here is an analogue of Theorem 10.5 for roots of power series in $A[[X]]$. Every such series converges on $\{x \in A : |x| < 1\}$, and this is where we will describe a criterion for the existence of a root.

**Theorem 10.7.** *Let $f(X) \in A[[X]]$, where $A$ is a nonzero ring complete with respect to a submultiplicative absolute value $|\cdot|$. If some $a \in A$ such that $|a| < 1$ satisfies $|f(a)| < 1$ and $f'(a) \in A^	imes$ then there is a unique $lpha \in A$ such that $f(lpha) = 0$ in $A$ and $|lpha - a| < 1$. Moreover,*

1. *$|lpha - a| = |f(a)| < 1$,*
2. *$f'(lpha) \in A^	imes$.*

<!-- page 23 -->

*Proof.* The proof proceeds in the same way as that of Theorem 10.5, relying on an extension of Lemma 8.1 to power series with coefficients in $A$ rather than $\mathbf{Z}_p$. $\square$

**Example 10.8.** Let $A = \mathbf{Q}[[T]]$ and

$$f(X) = e^X - (1 + T) = -T + X + rac{1}{2}X^2 + \cdots \in A[[X]].$$

Since $|f(0)|_T = |-T|_T < 1$ and $f'(0) = 1$, there is a unique $g(T) \in T\mathbf{Q}[[T]]$ such that $f(g(T)) = 0$, meaning $g(T) \in T\mathbf{Q}[[T]]$ and $e^{g(T)} = 1 + T$. To find the coefficients of $g(T)$, differentiate both sides of the equation $e^{g(T)} = 1 + T$: $e^{g(T)}g'(T) = 1$, so

$$g'(T) = rac{1}{e^{g(T)}} = rac{1}{1 + T} = \sum_{n \geq 0} (-1)^n T^n.$$

Therefore $g(T) = \sum_{n \geq 0} ((-1)^n/(n+1))T^{n+1} = \sum_{n \geq 1} ((-1)^{n-1}/n)T^n$, which is the formal power series for $\log(1 + T)$ in $T\mathbf{Q}[[T]]$. The constant term of $g(T)$ is 0 since $g(T) \in T\mathbf{Q}[[T]]$.

**Example 10.9.** Let $A = \mathbf{Q}[[T]]$ and

$$f(X) = Xe^X - T = -T + X + X^2 + rac{1}{2}X^3 + \cdots \in A[[X]].$$

Since $|f(0)|_T = |-T|_T < 1$ and $f'(0) = 1$, there is a unique $W(T) \in T\mathbf{Q}[[T]]$ such that $f(W(T)) = 0$, meaning $W(T)e^{W(T)} = T$. The series for $W(T)$ is

$$T - T^2 + rac{3}{2}T^3 - rac{8}{3}T^4 + rac{125}{24}T^5 - rac{54}{5}T^6 + \cdots = \sum_{n \geq 0} rac{(-n)^{n-1}}{n!} T^n.$$

Classically, $W(T)$ as a function on $\mathbf{C}$ (initially near 0) is called Lambert's $W$-function.

**Example 10.10.** (Formal compositional inverse) Let $f(T) = c_1 T + \cdots \in TR[[T]]$ for a commutative ring $R$. We will show there is a $g(T) \in TR[[T]]$ such that $f(g(T)) = T$ if and only if $c_1 \in R^	imes$, in which case $g(T)$ is unique and we also have $g(f(T)) = T$.

Suppose $g(T) = b_1 T + \cdots \in TR[[T]]$ satisfies $f(g(T)) = T$. By a formal calculation, $f(g(T)) = c_1 b_1 T + 	ext{higher order terms}$. That is, since $g(T) \equiv b_1 T mod T^2$ we have $g(T)^n \equiv 0 mod T^2$ when $n \geq 2$, so $f(g(T)) \equiv c_1 g(T) \equiv c_1 b_1 T mod T^2$. If $f(g(T)) = T$ then $T \equiv c_1 b_1 T mod T^2$, so $c_1 b_1 = 1$ in $R$. Thus $c_1 \in R^	imes$.

Conversely, suppose $c_1 \in R^	imes$. We will use Theorem 10.7 with $A = R[[T]]$ and the power series $F(X) = f(X) - T \in A[[X]]$. Since $|F(0)|_T = |-T|_T < 1$ and $F'(0) = c_1 \in R^	imes \subset R[[T]]^	imes$, by Theorem 10.7 there is a unique $g(T) \in TR[[T]]$ such that $F(g(T)) = 0$, which means $f(g(T)) = T$.

Since $g(T)$ is in $TR[[T]]$, just like $f(T)$, we can run through the same reasoning with $g(T)$ in place of $f(T)$ by using $G(X) = g(X) - T$ in place of $F(X) = f(X) - T$ to see there is a unique $h(T) \in TR[[T]]$ such that $G(h(T)) = 0$, meaning $g(h(T)) = T$. Then $f(T) = f(g(h(T))) = h(T)$ since $f(g(T)) = T$. That proves $g(f(T)) = T$. For instance, in Example 10.8, rewriting $e^{\log(1+T)} = 1 + T$ as $F(\log(1 + T)) = T$ where $F(T) = e^T - 1$, we get $\log(1 + F(T)) = T$, or equivalently $\log(e^T) = T$.

The classical implicit function theorem says that if $f(x, y)$ is a $C^1$-function on an open set $U$ in $\mathbf{R}^2$ and at a point $(x_0, y_0)$ in $U$ we have $f(x_0, y_0) = 0$ and $f_y(x_0, y_0) 
eq 0$, then for all $x$ close enough to $x_0$ there is a unique $g(x)$ near $y_0$ such that $f(x, g(x)) = 0$, and $g$ is $C^1$ near $x_0$. Here is an analogue of this result for formal power series "near $(0, 0)$".

**Example 10.11.** (Formal implicit function theorem) Let $f(X, Y) = c_{10}X + c_{01}Y + \cdots$ in $R[[X, Y]]$, so $f(0, 0) = 0$ and $f_Y(0, 0) = c_{01}$. If $f_Y(0, 0) \in R^	imes$, then there is a unique power series $g(X) \in XR[[X]]$ such that $f(X, g(X)) = 0$. To prove this, view $R[[X, Y]]$ as

<!-- page 24 -->

$R[[X]][[Y]] = A[[Y]]$ where $A = R[[X]]$, which is $X$-adically complete. Viewing $f(X, Y)$ in $R[[X]][[Y]]$ means thinking of $f(X, Y)$ as a power series in $Y$ whose coefficients are power series in $X$. We have $|f(X, 0)|_X = |c_{10}X + \cdots|_X < 1$ and $f_Y(X, 0)$ is in $R[[X]]^	imes$ since its constant term $f_Y(0, 0)$ is a unit in $R$ (Example 10.4), so there is a unique $g(X) \in XR[[X]]$ such that $f(X, g(X)) = 0$ by Theorem 10.7 for power series in $Y$ with $A = R[[X]]$.

In particular, if $K$ is a field and $f(X, Y) \in K[[X, Y]]$ satisfies $f(0, 0) = 0$ and $f_Y(0, 0) 
eq 0$ then there is a unique $g(X) \in XK[[X]]$ such that $f(X, g(X)) = 0$. An example of this is $f(X, Y) = \cos X - 1 + \sin Y = X^2/2 + Y + \cdots$ in $\mathbf{Q}[[X]][[Y]]$. The constant term is 0 and the coefficient of $Y$ is nonzero in $\mathbf{Q}$, so there is a unique $g(X) \in X\mathbf{Q}[[X]]$ such that $\sin(g(X)) = 1 - \cos X$. The series $g(X)$ begins as $-(1/2)X^2 + (1/24)X^4 - (1/45)X^6 + \cdots$.

For a version of Hensel's lemma where $\mathbf{Z}_p$ is replaced by a complete local ring (possibly not an integral domain), see [3, Theorem 7.3]. For a version of Hensel's lemma dealing with zeros of several polynomials in several variables, see [1].

## Appendix A. Gauss' Work on $p$-adic Roots

While Hensel introduced $p$-adic numbers in the early 1900s, unpublished work by Gauss shows he was working with them over 50 years earlier. The scanned page below[^8] has the heading (in Latin) "Infinite Congruences" and begins with the equation

$$x^5 - 20x^4 - 86x^3 - 98x^2 + 80x + 3 \equiv 0 mod 241^\infty,$$

where the modulus $241^\infty$ suggests the use of $\mathbf{Z}_{241}$. (The number 241 is prime.) There are 5 roots in $\mathbf{Z}_{241}$, which start off as

$$2 + 191 \cdot 241 + \cdots, \quad 3 + 238 \cdot 241 + \cdots, \quad 4 + 192 \cdot 241 + \cdots, \quad 5 + 65 \cdot 241 + \cdots, \quad 6 + 37 \cdot 241 + \cdots$$

and below the equation are the first digits of the roots ("habet radices" = "has roots") and the coefficient of 241 in the first root.

![Gauss's handwritten page on infinite congruences](gauss_page.png)

[^8]: This is from https://math.stackexchange.com/questions/844756/history-of-p-adic-numbers.

<!-- page 25 -->

At the bottom left of the page, Gauss wrote $\sqrt{5} mod 11^\infty = 9\ 0\ 4\ 10\ 4\ 4$. The congruence $x^2 \equiv 5 mod 11$ has two roots, 4 and 7, which lead to two square roots of 5 in $\mathbf{Z}_{11}$, with the first one being

$$4 + 4 \cdot 11 + 10 \cdot 11^2 + 4 \cdot 11^3 + 0 \cdot 11^4 + 9 \cdot 11^5 + \cdots$$

and these have the digits Gauss had found, but he wrote the expansion right to left rather than left to right. The same 11-adic expansion appears in the middle of the page on the left side. Lemmermeyer [7, p. 3] explains this as a calculation mod $11^6$ of $\sqrt{5} = \sqrt{1 + 4 \cdot 11}/3$ using the binomial expansion of $\sqrt{1 + x}$ at $x = 44$ split into terms with positive coefficients and negative coefficients to get $\sqrt{1 + 4 \cdot 11} = 1 + 2 \cdot 11 + 9 \cdot 11^2 + 3 \cdot 11^3 + 1 \cdot 11^4 + 5 \cdot 11^5 mod 11^6$.

## References

[1] K. Conrad, *A multivariable Hensel's lemma*, URL https://kconrad.math.uconn.edu/blurbs/gradnumthy/multivarhensel.pdf.

[2] C. H. Edwards, Jr., "Advanced Calculus of Several Variables," Academic Press, New York, 1973.

[3] D. Eisenbud, "Commutative Algebra with a View to Algebraic Geometry," Springer-Verlag, New York, 1995.

[4] K. Hensel, *Neue Grundlagen der Arithmetik*, J. Reine Angew. Math. **127** (1904), 51-84 URL https://eudml.org/doc/149178.

[5] K. Hensel, "Theorie der algebraischen Zahlen," Teubner, Leipzig, 1908. URL https://archive.org/details/in.ernet.dli.2015.493154.

[6] S. Lang, "Algebraic Number Theory," 3rd ed., Springer-Verlag, New York, 1994.

[7] F. Lemmermeyer, *Gauss and p-adic numbers*, URL https://arxiv.org/pdf/2510.11559.

[8] R. Y. Lewis, *A Formal Proof of Hensel's Lemma over the p-adic Integers*, URL http://robertylewis.com/padics/padics.pdf.
