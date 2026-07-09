# Discriminants and Ramified Primes

> **Source**: https://kconrad.math.uconn.edu/blurbs/disc.pdf  
> **Author**: Keith Conrad  
> **Topic**: algebraic_number_theory

<!-- page 1 -->

## 1. Introduction

A prime number $p$ is said to be *ramified* in a number field $K$ if the prime ideal factorization

$$
(p) = p\mathcal{O}_K = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_g^{e_g} \tag{1.1}
$$

has some $e_i$ greater than 1. If every $e_i$ equals 1, we say $p$ is *unramified* in $K$.

**Example 1.1.** In $\mathbf{Z}[i]$, the only prime that ramifies is 2: $(2) = (1+i)^2$.

**Example 1.2.** Let $K = \mathbf{Q}(\alpha)$ where $\alpha$ is a root of $f(T) = T^3 - 9T - 6$. Then $6 = \alpha^3 - 9\alpha = \alpha(\alpha-3)(\alpha+3)$. For $m \in \mathbf{Z}$, $\alpha + m$ has minimal polynomial $f(T - m)$ in $\mathbf{Q}[T]$, so $\mathrm{N}_{K/\mathbf{Q}}(\alpha + m) = -f(-m) = m^3 - 9m + 6$ and the principal ideal $(\alpha - m)$ has norm

$$
\mathrm{N}(\alpha - m) = |m^3 - 9m + 6|.
$$

Therefore $\mathrm{N}(\alpha) = 6$, $\mathrm{N}(\alpha - 3) = 6$, and $\mathrm{N}(\alpha + 3) = 6$. It follows that $(\alpha) = \mathfrak{p}_2\mathfrak{p}_3$, $(\alpha - 3) = \mathfrak{p}_2'\mathfrak{p}_3$, and $(\alpha + 3) = \mathfrak{p}_2'\mathfrak{p}_3$ (so, in particular, $\alpha + 3$ and $\alpha - 3$ are unit multiples of each other). Thus

$$
(2)(3) = (6) = (\alpha)(\alpha - 3)(\alpha + 3) = \mathfrak{p}_2\mathfrak{p}_2'^2\mathfrak{p}_3^3,
$$

so $(2) = \mathfrak{p}_2^2\mathfrak{p}_2'$ and $(3) = \mathfrak{p}_3^3$. This shows 2 and 3 are ramified in $K$. Note that one of the exponents in the factorization of $(2)$ exceeds 1 while the other equals 1.

One way to think about ramified primes is in terms of the ring structure of $\mathcal{O}_K/(p)$. By (1.1) and the Chinese Remainder Theorem,

$$
\mathcal{O}_K/(p) \cong \mathcal{O}_K/\mathfrak{p}_1^{e_1} \times \cdots \times \mathcal{O}_K/\mathfrak{p}_g^{e_g}. \tag{1.2}
$$

If some $e_i$ is greater than 1, then the quotient ring $\mathcal{O}_K/\mathfrak{p}_i^{e_i}$ has a nonzero nilpotent element (use the reduction modulo $\mathfrak{p}_i^{e_i}$ of any element of $\mathfrak{p}_i - \mathfrak{p}_i^{e_i}$), so the product ring (1.2) has a nonzero nilpotent element. If each $e_i$ equals 1, then $\mathcal{O}_K/(p)$ is a product of (finite) fields, and a product of fields has no nonzero nilpotent elements. Thus, $p$ ramifies in $K$ if and only if $\mathcal{O}_K/(p)$ has a nonzero nilpotent element.

In Sections 2 and 3 we will prove the following result of Dedekind [2], which characterizes the prime numbers ramifying in a number field $K$ in terms of its discriminant.[^1]

**Theorem 1.3 (Dedekind).** *For a number field $K$, a prime $p$ ramifies in $K$ if and only if $p$ divides the integer $\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K)$.*

Recall $\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K) := \mathrm{disc}_{K/\mathbf{Q}}(\alpha_1, \ldots, \alpha_n)$ where $\{\alpha_1, \ldots, \alpha_n\}$ is any $\mathbf{Z}$-basis of $\mathcal{O}_K$. The generalization of Theorem 1.3 to a relative extension of number fields is in Section 4.

<!-- page 2 -->

## 2. A Special Case

We will first consider Theorem 1.3 in the special case that there is an $\alpha \in \mathcal{O}_K$ such that $K = \mathbf{Q}(\alpha)$ and $p \nmid [\mathcal{O}_K : \mathbf{Z}[\alpha]]$. (If $\mathcal{O}_K = \mathbf{Z}[\alpha]$ we can use the same $\alpha$ for all $p$.) The treatment of the general case in Section 3 will not rely on the case that $p \nmid [\mathcal{O}_K : \mathbf{Z}[\alpha]]$ for some $\alpha$, but this special case is technically simpler. We will just sketch the basic ideas behind it.

*Proof.* Assume for a prime $p$ that there's $\alpha \in \mathcal{O}_K$ such that $K = \mathbf{Q}(\alpha)$ and $p \nmid [\mathcal{O}_K : \mathbf{Z}[\alpha]]$. Let $f(T)$ be the minimal polynomial of $\alpha$ over $\mathbf{Q}$, so $f(T)$ is monic in $\mathbf{Z}[T]$, and the Dedekind–Kummer theorem tells us that the way $p\mathcal{O}_K$ factors into prime ideals matches the way $f(T) \bmod p$ factors into monic irreducibles in $(\mathbf{Z}/p\mathbf{Z})[T]$.

Writing the prime ideal factorization of $p\mathcal{O}_K$ as in (1.1), by definition $p$ ramifies in $\mathcal{O}_K$ if and only if some $e_i > 1$. The factorization of the mod $p$ reduction $\bar{f}(T)$ in $(\mathbf{Z}/p\mathbf{Z})[T]$ matches (1.1), in the sense that

$$
\bar{f}(T) = \pi_1^{e_1} \cdots \pi_g^{e_g}
$$

for some distinct monic irreducibles $\pi_i \in (\mathbf{Z}/p\mathbf{Z})[T]$.

The irreducible polynomials $\pi_i(T)$'s are separable (all irreducibles over a finite field are separable), so some $e_i > 1$ if and only if $\bar{f}(T)$ has a repeated root in a splitting field over $\mathbf{Z}/p\mathbf{Z}$. This is equivalent to $\bar{f}(T)$ having discriminant 0, so $p$ ramifies in $\mathcal{O}_K$ if and only if $\mathrm{disc}(\bar{f}) = 0$ in $\mathbf{Z}/p\mathbf{Z}$.

Since the discriminant of a monic polynomial is a universal polynomial in its coefficients (consider the quadratic case, where $T^2 + bT + c$ has discriminant $b^2 - 4c$), discriminants of monic polynomials behave well under reduction: $\mathrm{disc}(f(T) \bmod p) = \mathrm{disc}(f(T)) \bmod p$. Therefore $\mathrm{disc}(\bar{f}(T)) = 0$ in $\mathbf{Z}/p\mathbf{Z}$ if and only if $\mathrm{disc}(f) \equiv 0 \bmod p$. Thus $p$ ramifies in $\mathcal{O}_K$ if and only if $p \mid \mathrm{disc}(f)$. Since

$$
\mathrm{disc}(f) = \mathrm{disc}(\mathbf{Z}[\alpha]) = [\mathcal{O}_K : \mathbf{Z}[\alpha]]^2 \, \mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K)
$$

and $p \nmid [\mathcal{O}_K : \mathbf{Z}[\alpha]]$, we have $p \mid \mathrm{disc}(f)$ if and only if $p \mid \mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K)$. $\square$

## 3. The General Case

To prove Theorem 1.3 for every prime number $p$, even if $p \mid [\mathcal{O}_K : \mathbf{Z}[\alpha]]$ for all $\alpha \in \mathcal{O}_K$ such that $K = \mathbf{Q}(\alpha)$,[^2] we will examine discriminants of ring extensions to show computing the discriminant commutes with reduction mod $p$: $\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K) \bmod p = \mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/(p))$. Then we will use (1.2) to write $\mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/(p))$ as a product of discriminants of rings of type $\mathcal{O}_K/\mathfrak{p}^e$ and compute the discriminants of these particular rings.

**Definition 3.1.** Let $A$ be a commutative ring and $B$ be a ring extension of $A$ that is a finite free $A$-module:

$$
B = Ae_1 \oplus \cdots \oplus Ae_n.
$$

Then we set

$$
\mathrm{disc}_A(e_1, \ldots, e_n) = \det(\mathrm{Tr}_{B/A}(e_i e_j)) \in A.
$$

<!-- page 3 -->

**Remark 3.2.** The discriminant of a basis is an algebraic concept of "volume". To explain this viewpoint, we should think about $\mathrm{Tr}_{B/A}(xy)$ as an analogue of the dot product $v \cdot w$ in $\mathbf{R}^n$. For a basis $v_1, \ldots, v_n$ in $\mathbf{R}^n$, the ordinary Euclidean volume of the parallelotope

$$
\left\{\sum_{i=1}^n a_i v_i : 0 \leq a_i \leq 1\right\}
$$

having edges $v_i$ is $\sqrt{|\det(v_i \cdot v_j)|}$. The discriminant of an $A$-basis of $B$ uses the $A$-valued pairing $\langle x, y \rangle = \mathrm{Tr}_{B/A}(xy)$ on $B$ in place of the $\mathbf{R}$-valued dot product on $\mathbf{R}^n$ and we just drop the absolute value and the square root when we make the algebraic analogue.

How are the discriminants of two $A$-module bases for $B$ related? Pick a second basis $e_1', \ldots, e_n'$ of $B$ as an $A$-module. Then

$$
e_i' = \sum_{j=1}^n a_{ij} e_j,
$$

where $a_{ij} \in A$ and the change of basis matrix $(a_{ij})$ has determinant in $A^\times$. Then

$$
\mathrm{Tr}_{B/A}(e_i' e_j') = \mathrm{Tr}_{B/A}\!\left(\sum_{k=1}^n a_{ik} e_k \sum_{\ell=1}^n a_{j\ell} e_\ell\right) = \sum_{k=1}^n \sum_{\ell=1}^n a_{ik}\,\mathrm{Tr}_{B/A}(e_k e_\ell)\,a_{j\ell},
$$

so

$$
(\mathrm{Tr}_{B/A}(e_i' e_j')) = (a_{ij})(\mathrm{Tr}_{B/A}(e_i e_j))(a_{ij})^\top.
$$

Therefore

$$
\mathrm{disc}_A(e_1', \ldots, e_n') = (\det(a_{ij}))^2 \, \mathrm{disc}_A(e_1, \ldots, e_n).
$$

We set

$$
\mathrm{disc}_A(B) = \mathrm{disc}_A(e_1, \ldots, e_n) \in A
$$

for any $A$-module basis $\{e_1, \ldots, e_n\}$ of $B$. It is well-defined up to a unit square. In particular, the condition $\mathrm{disc}_A(B) = 0$ is independent of the choice of basis.

Given a number field $K$, ramification of the prime $p$ in $K$ has been linked to the structure of the ring $\mathcal{O}_K/(p)$ in Section 1. Let's look at the discriminant of this ring over $\mathbf{Z}/p\mathbf{Z}$. Letting $K$ have degree $n$ over $\mathbf{Q}$, the ring $\mathcal{O}_K$ is a free rank-$n$ $\mathbf{Z}$-module, say

$$
\mathcal{O}_K = \bigoplus_{i=1}^n \mathbf{Z}\omega_i.
$$

Reducing both sides modulo $p$,

$$
\mathcal{O}_K/(p) = \bigoplus_{i=1}^n (\mathbf{Z}/p\mathbf{Z})\bar{\omega}_i,
$$

so $\mathcal{O}_K/(p)$ is a vector space over $\mathbf{Z}/p\mathbf{Z}$ of dimension $n$. The discriminant of $\mathcal{O}_K$ is $\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K)$. The next lemma says reduction modulo $p$ commutes (in a suitable sense) with the formation of discriminants.

**Lemma 3.3.** *Choosing bases appropriately for $\mathcal{O}_K$ and $\mathcal{O}_K/(p)$,*

$$
\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K) \bmod p = \mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/(p)).
$$

<!-- page 4 -->

*Proof.* Pick a $\mathbf{Z}$-basis $\omega_1, \ldots, \omega_n$ of $\mathcal{O}_K$. The reductions $\bar{\omega}_1, \ldots, \bar{\omega}_n$ in $\mathcal{O}_K/(p)$ are a $\mathbf{Z}/p\mathbf{Z}$-basis, so the multiplication matrix $[m_x]$ for any $x \in \mathcal{O}_K$, with respect to the basis $\{\omega_i\}$, reduces modulo $p$ to the multiplication matrix $[m_{\bar{x}}]$ for $\bar{x}$ on $\mathcal{O}_K/(p)$ with respect to the basis $\{\bar{\omega}_i\}$. Therefore

$$
\mathrm{Tr}_{(\mathcal{O}_K/(p))/(\mathbf{Z}/p\mathbf{Z})}(\bar{x}) = \mathrm{Tr}(m_{\bar{x}}) = \mathrm{Tr}(m_x) \bmod p = \mathrm{Tr}_{\mathcal{O}_K/\mathbf{Z}}(x) \bmod p.
$$

Thus, the mod $p$ reduction of the matrix $(\mathrm{Tr}_{\mathcal{O}_K/\mathbf{Z}}(\omega_i \omega_j))$ is $(\mathrm{Tr}_{(\mathcal{O}_K/(p))/(\mathbf{Z}/p\mathbf{Z})}(\bar{\omega}_i \bar{\omega}_j))$. Now take determinants. $\square$

**Lemma 3.4.** *Let $A$ be a commutative ring and $B_1$ and $B_2$ be commutative ring extensions of $A$ that are each finite free $A$-modules. Then, choosing $A$-module bases appropriately,*

$$
\mathrm{disc}_A(B_1 \times B_2) = \mathrm{disc}_A(B_1)\,\mathrm{disc}_A(B_2).
$$

*Proof.* Pick $A$-module bases for $B_1$ and $B_2$:

$$
B_1 = \bigoplus_{i=1}^m Ae_i, \quad B_2 = \bigoplus_{j=1}^n Af_j.
$$

As an $A$-module basis for $B_1 \times B_2$ we will use the $m + n$ elements $e_1, \ldots, e_m, f_1, \ldots, f_n$. Since $e_i f_j = 0$ in $B_1 \times B_2$, the matrix whose determinant is $\mathrm{disc}_A(B_1 \times B_2)$ is a block diagonal matrix

$$
\begin{pmatrix} (\mathrm{Tr}_{(B_1 \times B_2)/A}(e_i e_k)) & O \\ O & (\mathrm{Tr}_{(B_1 \times B_2)/A}(f_j f_\ell)) \end{pmatrix}.
$$

For any $x \in B_1$, multiplication by $x$ on $B_1 \times B_2$ kills the $B_2$ component and acts on the $B_1$-component in the way $x$ multiplies on $B_1$, so a matrix for multiplication by $x$ on $B_1 \times B_2$ is a matrix whose upper left block is a matrix for multiplication by $x$ on $B_1$ and other blocks are 0. Thus

$$
\mathrm{Tr}_{(B_1 \times B_2)/A}(x) = \mathrm{Tr}_{B_1/A}(x) \quad \text{for } x \in B_1.
$$

Similarly, $\mathrm{Tr}_{(B_1 \times B_2)/A}(x) = \mathrm{Tr}_{B_2/A}(x)$ for $x \in B_2$. Thus

$$
\begin{pmatrix} (\mathrm{Tr}_{(B_1 \times B_2)/A}(e_i e_k)) & O \\ O & (\mathrm{Tr}_{(B_1 \times B_2)/A}(f_j f_\ell)) \end{pmatrix} = \begin{pmatrix} (\mathrm{Tr}_{B_1/A}(e_i e_k)) & O \\ O & (\mathrm{Tr}_{B_2/A}(f_j f_\ell)) \end{pmatrix},
$$

and taking determinants gives

$$
\mathrm{disc}_A(B_1 \times B_2) = \mathrm{disc}_A(B_1)\,\mathrm{disc}_A(B_2). \quad \square
$$

Now we prove Theorem 1.3.

*Proof.* We have $p \mid \mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K)$ if and only if $\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K) \equiv 0 \bmod p$. By Lemma 3.3

$$
\mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K) \bmod p = \mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/(p)),
$$

so $p \mid \mathrm{disc}_{\mathbf{Z}}(\mathcal{O}_K)$ if and only if $\mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/(p)) = \bar{0}$ in $\mathbf{Z}/p\mathbf{Z}$.

In (1.2), each factor $\mathcal{O}_K/\mathfrak{p}_i^{e_i}$ is a $\mathbf{Z}/p\mathbf{Z}$-vector space since $p \in \mathfrak{p}_i^{e_i}$. Using (1.2) and Lemma 3.4,

$$
\mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/(p)) = \prod_{i=1}^g \mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/\mathfrak{p}_i^{e_i}).
$$

Therefore we need to show for any prime number $p$ and prime-power ideal $\mathfrak{p}^e$ such that $\mathfrak{p}^e \mid (p)$ that $\mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/\mathfrak{p}^e)$ is $\bar{0}$ in $\mathbf{Z}/p\mathbf{Z}$ if and only if $e > 1$. (Recall that the vanishing of a discriminant is independent of the choice of basis.)

<!-- page 5 -->

Suppose $e > 1$. Then any $x \in \mathfrak{p} - \mathfrak{p}^e$ is a nonzero nilpotent element in $\mathcal{O}_K/\mathfrak{p}^e$. By linear algebra over fields, such an $\bar{x}$ can be used as part of a $\mathbf{Z}/p\mathbf{Z}$-basis of $\mathcal{O}_K/\mathfrak{p}^e$, say $\{\bar{x}_1, \ldots, \bar{x}_n\}$ with $\bar{x} = \bar{x}_1$. Writing the trace map $\mathrm{Tr}_{(\mathcal{O}_K/\mathfrak{p}^e)/(\mathbf{Z}/p\mathbf{Z})}$ as $\mathrm{Tr}$ for short, the first column of the matrix $(\mathrm{Tr}(\bar{x}_i \bar{x}_j))$ contains the numbers $\mathrm{Tr}(\bar{x}_i \bar{x})$. These traces are all $\bar{0}$: $\bar{x}_i \bar{x}$ is nilpotent, so the linear transformation $m_{\bar{x}_i \bar{x}}$ on $\mathcal{O}_K/\mathfrak{p}^e$ is nilpotent and thus its eigenvalues all equal zero. Since one column of the trace-pairing matrix $(\mathrm{Tr}(\bar{x}_i \bar{x}_j))$ is all $\bar{0}$, $\mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/\mathfrak{p}^e) = \bar{0}$.

Now suppose $e = 1$. Then $\mathcal{O}_K/\mathfrak{p}^e = \mathcal{O}_K/\mathfrak{p}$ is a finite field of characteristic $p$. We want to prove $\mathrm{disc}_{\mathbf{Z}/p\mathbf{Z}}(\mathcal{O}_K/\mathfrak{p}) \neq \bar{0}$. If this discriminant is $\bar{0}$, then (because $\mathcal{O}_K/\mathfrak{p}$ is a field) the trace function $\mathrm{Tr}: \mathcal{O}_K/\mathfrak{p} \to \mathbf{Z}/p\mathbf{Z}$ is identically zero. However, from the theory of finite fields, this trace function can be written as a polynomial function:

$$
\mathrm{Tr}(t) = t + t^p + t^{p^2} + \cdots + t^{p^{r-1}},
$$

where $p^r = |\mathcal{O}_K/\mathfrak{p}|$. Since $\mathrm{Tr}(t)$ as a polynomial in $t$ has smaller degree than the size of $\mathcal{O}_K/\mathfrak{p}$, the function $\mathrm{Tr}(t)$ is not identically zero on $\mathcal{O}_K/\mathfrak{p}$. Therefore the discriminant of a finite extension of $\mathbf{Z}/p\mathbf{Z}$ does not equal zero. $\square$

## 4. The Relative Case

Ramified primes and discriminants can be defined for an extension of number fields $E/F$ where the base field $F$ need not be $\mathbf{Q}$. This is called the relative case, while the study of number field extensions with base field $\mathbf{Q}$ is called the absolute case.

To define the discriminant of $E/F$, a direct copying of the definition over $\mathbf{Q}$ is possible if $\mathcal{O}_F$ is PID. In this case $\mathcal{O}_E$ is a free $\mathcal{O}_F$-module. We say a prime $\pi$ in $\mathcal{O}_F$ is *ramified* in $E$ when the ideal $\pi\mathcal{O}_E$ has a repeated prime ideal factor and is *unramified* otherwise. When $\{\alpha_1, \ldots, \alpha_n\}$ is an $\mathcal{O}_F$-basis of $\mathcal{O}_E$ the number $\mathrm{disc}_{E/F}(\alpha_1, \ldots, \alpha_n)$ is nonzero in $\mathcal{O}_F$ and changing the $\mathcal{O}_F$-basis of $\mathcal{O}_E$ changes this number by a unit square in $\mathcal{O}_F$.

**Example 4.1.** Let $F = \mathbf{Q}(i)$ and $E = F(\sqrt{-5})$. Then $\mathcal{O}_F = \mathbf{Z}[i]$ and it can be shown that $\mathcal{O}_E = \mathcal{O}_F[\sqrt{-5}] = \mathbf{Z}[i][\sqrt{-5}]$, so $\{1, \sqrt{-5}\}$ is a $\mathbf{Z}[i]$-basis of $\mathcal{O}_E$. Since

$$
\mathrm{disc}_{E/F}(1, \sqrt{-5}) = \det\begin{pmatrix} \mathrm{Tr}_{E/F}(1 \cdot 1) & \mathrm{Tr}_{E/F}(1 \cdot \sqrt{-5}) \\ \mathrm{Tr}_{E/F}(\sqrt{-5} \cdot 1) & \mathrm{Tr}_{E/F}(\sqrt{-5}\sqrt{-5}) \end{pmatrix} = \det\begin{pmatrix} 2 & 0 \\ 0 & -10 \end{pmatrix} = -20,
$$

the discriminant of $E/F$ is $-20$ up to a unit square in $\mathbf{Z}[i]$. Another $\mathbf{Z}[i]$-basis of $\mathcal{O}_E$ is $\{i, \sqrt{-5}\}$ and $\mathrm{disc}_{E/F}(i, \sqrt{-5}) = \det\bigl(\begin{smallmatrix} -2 & 0 \\ 0 & -10 \end{smallmatrix}\bigr) = 20$, which differs from $-20$ by a unit square factor $-1 = i^2$.

Numbers in a PID that differ by a unit factor have the same prime factors, so whether or not a prime in $\mathcal{O}_F$ divides $\mathrm{disc}_{E/F}(\alpha_1, \ldots, \alpha_n)$ does not depend on the choice of $\mathcal{O}_F$-basis.

Here is how Theorem 1.3 generalizes to $E/F$ when $\mathcal{O}_F$ is a PID.

**Theorem 4.2.** *For an extension of number fields $E/F$ where $\mathcal{O}_F$ is a PID, a prime $\pi$ in $F$ ramifies in $E$ if and only if $\pi$ divides $\mathrm{disc}_{E/F}(\alpha_1, \ldots, \alpha_n)$ where $\{\alpha_1, \ldots, \alpha_n\}$ is an $\mathcal{O}_F$-basis of $\mathcal{O}_E$.*

*Proof.* Use the method of proof of Section 3 with $\mathbf{Z}$ replaced by $\mathcal{O}_F$. $\square$

**Example 4.3.** In Example 4.1, 20 has prime factorization $-(1+i)^4(1+2i)(1-2i)$, in $\mathbf{Z}[i]$ so the primes in $\mathbf{Z}[i]$ that ramify in $\mathbf{Z}[i, \sqrt{-5}]$ are $1+i$, $1+2i$, and $1-2i$.

What do we do when $\mathcal{O}_F$ is not necessarily a PID? A (nonzero) prime ideal $\mathfrak{p}$ in $\mathcal{O}_F$ is called *ramified* in $E$ if the ideal $\mathfrak{p}\mathcal{O}_E$ has a repeated prime ideal factor in $\mathcal{O}_E$ and *unramified* otherwise.

<!-- page 6 -->

It can be shown that when $E = F(\alpha)$ with $\alpha \in \mathcal{O}_E$ and $\alpha$ has minimal polynomial $f(T)$ in $F[T]$, the prime $\mathfrak{p}$ is unramified in $E$ if (but not necessarily only if) $\mathrm{disc}(f(T)) \not\equiv 0 \bmod \mathfrak{p}$. A nonzero number in $\mathcal{O}_F$ has only finitely many prime ideal factors, so all but finitely many prime ideals in $\mathcal{O}_F$ are unramified in $E$.

The discriminant of $E/F$ is an ideal in $\mathcal{O}_F$, called the *discriminant ideal* $\mathfrak{d}_{E/F}$. It is defined as the ideal in $\mathcal{O}_F$ generated by the numbers $\mathrm{disc}_{E/F}(\alpha_1, \ldots, \alpha_n)$ where $\{\alpha_1, \ldots, \alpha_n\}$ runs over all $F$-bases of $E$ that are contained in $\mathcal{O}_E$.[^3] If one $F$-basis of $E$ contained in $\mathcal{O}_E$ is in the $\mathcal{O}_F$-span of another $F$-basis of $E$ contained in $\mathcal{O}_E$, then the discriminant of the first basis is a multiple of the discriminant of the second basis, so if $\mathcal{O}_E$ has an $\mathcal{O}_F$-basis, then $\mathfrak{d}_{E/F}$ is a principal ideal with the discriminant of any $\mathcal{O}_F$-basis of $\mathcal{O}_E$ being a generator.

Theorem 1.3 has the following generalization to the relative case, whose proof is more technical than that of Theorem 1.3 and is omitted.

**Theorem 4.4.** *For an extension of number fields $E/F$, a prime $\mathfrak{p}$ in $F$ ramifies in $E$ if and only if $\mathfrak{p}$ divides the discriminant ideal $\mathfrak{d}_{E/F}$.*

## References

[1] R. Dedekind, *Über den Zusammenhang zwischen der Theorie der ideale und der Theorie der höheren Congruenzen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften in Göttingen **23** (1878), 3–37. URL https://eudml.org/doc/135827.

[2] R. Dedekind, *Über die Discriminanten endlicher Körper*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften in Göttingen **29** (1882), 1–56. URL https://eudml.org/doc/135869.

[^1]: In [1, pp. 36–37], Dedekind said he announced this result for the first time on September 20, 1871.

[^2]: Dedekind wrote in [1, p. 37] that he first proved Theorem 1.3 in the special case of Section 2 above and was able to prove the general case only after many unsuccessful attempts. He presented the special case first in [2, §3] since it's much simpler than the method he used for the general case in [2, §§4–6].

[^3]: The ideal $\mathfrak{d}_{E/F}$ can be defined in a second way using localizations: see https://math.stackexchange.com/questions/4875752/. Some work is needed to show this way of defining $\mathfrak{d}_{E/F}$ agrees with the first way presented above.
