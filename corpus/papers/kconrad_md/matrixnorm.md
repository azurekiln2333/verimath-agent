# Computing the Norm of a Matrix

> **Source**: https://kconrad.math.uconn.edu/blurbs/matrixnorm.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra

<!-- page 1 -->

## 1. Introduction

In $\mathbf{R}^n$ there is a standard notion of length: the size of a vector $v = (a_1, \ldots, a_n)$ is

$$\|v\| = \sqrt{a_1^2 + \cdots + a_n^2}.$$

We will discuss in Section 2 the general concept of length in a vector space, called a norm, and then look at norms on matrices in Section 3. In Section 4 we'll see how the matrix norm that is closely connected to the standard norm on $\mathbf{R}^n$ can be computed from eigenvalues of an associated symmetric matrix.

## 2. Norms on Vector Spaces

Let $V$ be a vector space over $\mathbf{R}$. A *norm* on $V$ is a function $\|\cdot\|: V \to \mathbf{R}$ satisfying three properties:

(1) $\|v\| \ge 0$ for all $v \in V$, with equality if and only if $v = 0$,

(2) $\|v + w\| \le \|v\| + \|w\|$ for all $v$ and $w$ in $V$,

(3) $\|cv\| = |c|\,\|v\|$ for all $c \in \mathbf{R}$ and $v \in V$.

The same definition applies to complex vector spaces. From a norm on $V$ we get a metric on $V$ by $d(v, w) = \|v - w\|$. The triangle inequality for this metric is a consequence of the second property of norms.

**Example 2.1.** The standard norm on $\mathbf{R}^n$, using the standard basis $e_1, \ldots, e_n$, is

$$\left\|\sum_{i=1}^n a_i e_i\right\| = \sqrt{\sum_{i=1}^n a_i^2}.$$

This gives rise to the Euclidean metric on $\mathbf{R}^n$: $d(\sum a_i e_i, \sum b_i e_i) = \sqrt{\sum (a_i - b_i)^2}$.

**Example 2.2.** The sup-norm on $\mathbf{R}^n$ is

$$\left\|\sum_{i=1}^n a_i e_i\right\|_{\sup} = \max_i |a_i|.$$

This gives rise to the sup-metric on $\mathbf{R}^n$: $d(\sum a_i e_i, \sum b_i e_i) = \max_i |a_i - b_i|$.

**Example 2.3.** On $\mathbf{C}^n$ the standard norm and sup-norm are defined similarly to the case of $\mathbf{R}^n$, but we need $|z|^2$ instead of $z^2$ when $z$ is complex:

$$\left\|\sum_{i=1}^n a_i e_i\right\| = \sqrt{\sum_{i=1}^n |a_i|^2}, \quad \left\|\sum_{i=1}^n a_i e_i\right\|_{\sup} = \max_i |a_i|.$$

<!-- page 2 -->

A common way of placing a norm on a real vector space $V$ is by an *inner product*, which is a pairing $(\cdot, \cdot): V \times V \to \mathbf{R}$ that is

(1) bilinear: linear in each component when the other is fixed. Linearity in the first component means $(v + v', w) = (v, w) + (v', w)$ and $(cv, w) = c(v, w)$ for $v, v', w \in V$ and $c \in \mathbf{R}$, and similarly in the second component.

(2) symmetric: $(v, w) = (w, v)$.

(3) positive-definite: $(v, v) \ge 0$, with equality if and only if $v = 0$. The standard inner product on $\mathbf{R}^n$ is the dot product:

$$\left(\sum_{i=1}^n a_i e_i, \sum_{i=1}^n b_i e_i\right) = \sum_{i=1}^n a_i b_i.$$

For an inner product $(\cdot, \cdot)$ on $V$, a norm can be defined by the formula

$$\|v\| = \sqrt{(v, v)}.$$

That this is actually a norm on $V$ follows from the Cauchy--Schwarz inequality

$$(2.1) \qquad |(v, w)| \le (v, v)(w, w) = \|v\|\,\|w\|$$

as follows. For all $v$ and $w$ in $V$,

$$\|v + w\|^2 = (v + w, v + w)$$
$$= (v, v) + (v, w) + (w, v) + (w, w)$$
$$= \|v\|^2 + 2(v, w) + \|w\|^2$$
$$\le \|v\|^2 + 2|(v, w)| + \|w\|^2 \quad \text{since } a \le |a| \text{ for all } a \in \mathbf{R}$$
$$\le \|v\|^2 + 2\|v\|\,\|w\| + \|w\|^2 \quad \text{by (2.1)}$$
$$= (\|v\| + \|w\|)^2.$$

Taking (positive) square roots of both sides yields $\|v + w\| \le \|v\| + \|w\|$. A proof of the Cauchy--Schwarz inequality is in the appendix.

Using the standard inner product on $\mathbf{R}^n$, the Cauchy--Schwarz inequality assumes its classical form, proved by Cauchy in 1821:

$$\left|\sum_{i=1}^n a_i b_i\right| = \sqrt{\sum_{i=1}^n a_i^2 \cdot \sum_{i=1}^n b_i^2}.$$

The Cauchy--Schwarz inequality (2.1) is true for every inner product on a real vector space, not just the standard inner product on $\mathbf{R}^n$.

While the norm on $\mathbf{R}^n$ that comes from the standard inner product is the standard norm, the sup-norm on $\mathbf{R}^n$ does *not* arise from an inner product, *i.e.*, there is no inner product whose associated norm is the sup-norm.

Even though the sup-norm and the standard norm on $\mathbf{R}^n$ are not equal, they are each bounded by a constant multiple of the other one:

$$(2.2) \qquad \max_i |a_i| \le \sqrt{\sum_{i=1}^n a_i^2} \le \sqrt{n}\max_i |a_i|.$$

*i.e.*, $\|v\|_{\sup} \le \|v\| \le \sqrt{n}\,\|v\|_{\sup}$ for all $v \in \mathbf{R}^n$. Therefore the metrics these two norms give rise to determine the same notions of convergence: a sequence in $\mathbf{R}^n$ that is convergent with

<!-- page 3 -->

respect to one of the metrics is also convergent with respect to the other metric. Also $\mathbf{R}^n$ is complete with respect to both of these metrics.

The standard inner product on $\mathbf{R}^n$ is closely tied to transposition of $n \times n$ matrices. For $A = (a_{ij}) \in \operatorname{M}_n(\mathbf{R})$, let $A^\top = (a_{ji})$ be its transpose. Then for all $v, w \in \mathbf{R}^n$,

$$(2.3) \qquad (Av, w) = (v, A^\top w), \quad (v, Aw) = (A^\top v, w),$$

where $(\cdot, \cdot)$ is the standard inner product on $\mathbf{R}^n$.

We now briefly indicate what inner products are on complex vector spaces. An *inner product* on a complex vector space $V$ is a pairing $(\cdot, \cdot): V \times V \to \mathbf{C}$ that is

(1) linear on the left and conjugate-linear on the right: it is additive in each component with the other one fixed and $(cv, w) = c(v, w)$ and $(v, cw) = \bar{c}(v, w)$ for $c \in \mathbf{C}$.

(2) conjugate-symmetric: $(v, w) = \overline{(w, v)}$,

(3) positive-definite: $(v, v) \ge 0$, with equality if and only if $v = 0$.

The standard inner product on $\mathbf{C}^n$ is not the dot product, but has a conjugation in the second component:

$$(2.4) \qquad \left(\sum_{i=1}^n a_i e_i, \sum_{i=1}^n b_i e_i\right) = \sum_{i=1}^n a_i \bar{b}_i.$$

This standard inner product on $\mathbf{C}^n$ is closely tied to conjugate-transposition of $n \times n$ complex matrices. For $A = (a_{ij}) \in \operatorname{M}_n(\mathbf{C})$, let $A^* = \overline{A}^\top = (\overline{a_{ji}})$ be its conjugate-transpose. Then for all $v, w \in \mathbf{C}^n$,

$$(2.5) \qquad (Av, w) = (v, A^*w), \quad (v, Aw) = (A^*v, w).$$

An inner product on a complex vector space satisfies the Cauchy--Schwarz inequality, so it can be used to define a norm just as in the case of inner products on real vector spaces.

Although we will be focusing on norms on finite-dimensional spaces, the extension of these ideas to infinite-dimensional spaces is quite important in both analysis and physics (quantum mechanics). Speaking of physics, physicists define inner products on complex vector spaces as being linear on the right and conjugate-linear on the left. It's just a difference in notation, but leads to more differences, *e.g.*, the physicist's standard inner product on $\mathbf{C}^n$ is $(\sum_{i=1}^n a_i e_i, \sum_{i=1}^n b_i e_i) = \sum_{i=1}^n \overline{a_i} b_i$, which is the complex conjugate of the mathematician's standard inner product on $\mathbf{C}^n$ as defined earlier.

Exercises.

1. Letting $(\cdot, \cdot)_m$ be the dot product on $\mathbf{R}^m$ and $(\cdot, \cdot)_n$ be the dot product on $\mathbf{R}^n$, show for each $m \times n$ matrix $A$, $n \times m$ matrix $B$, $v \in \mathbf{R}^n$, and $w \in \mathbf{R}^m$ that $(Av, w)_m = (v, A^\top w)_n$ and $(v, Bw)_n = (B^\top v, w)_m$. When $m = n$ this becomes (2.3).

2. Verify (2.5).

## 3. Defining Norms on Matrices

*From now on, the norm and inner product on $\mathbf{R}^n$ and $\mathbf{C}^n$ are the standard ones.*

The set of $n \times n$ real matrices $\operatorname{M}_n(\mathbf{R})$ forms a real vector space. How should we define a norm on $\operatorname{M}_n(\mathbf{R})$? One idea is to view $\operatorname{M}_n(\mathbf{R})$ as $\mathbf{R}^{n^2}$ and use the sup-norm on $\mathbf{R}^{n^2}$

$$\|(a_{ij})\|_{\sup} = \max_{i,j} |a_{ij}|.$$

<!-- page 4 -->

or the standard norm on $\mathbf{R}^{n^2}$ (also called the *Frobenius norm* on $\operatorname{M}_n(\mathbf{R})$): $\|(a_{ij})\| = \sqrt{\sum a_{ij}^2}$. While these are used in numerical work, in pure math there is a better choice of a norm on $\operatorname{M}_n(\mathbf{R})$ than either of these. Before describing it, we use the sup-norm on $\operatorname{M}_n(\mathbf{R})$ to show that each $n \times n$ matrix changes the (standard) length of vectors in $\mathbf{R}^n$ by a uniformly bounded amount that depends only on $n$ and the matrix. For $v = (c_1, \ldots, c_n) \in \mathbf{R}^n$,

$$\|Av\| \le \sqrt{n}\,\|Av\|_{\sup} \quad \text{by (2.2)}$$
$$= \sqrt{n}\max_i \left|\sum_{j=1}^n a_{ij}c_j\right|$$
$$\le \sqrt{n}\max_i \sum_{j=1}^n |a_{ij}||c_j|$$
$$\le \sqrt{n}\max_i \sum_{j=1}^n |a_{ij}|\,\|v\|_{\sup}$$
$$\le n\sqrt{n}\max_{i,j}|a_{ij}|\,\|v\|_{\sup}$$
$$\le n\sqrt{n}\max_{i,j}|a_{ij}|\,\|v\| \quad \text{by (2.2)}.$$

Let $C = n\sqrt{n}\max|a_{ij}|$. This is a constant depending on the dimension $n$ of the space and the matrix $A$, but not on $v$, and $\|Av\| \le C\|v\|$ for all $v$. By linearity, $\|Av - Aw\| \le C\|v - w\|$ for all $v, w \in \mathbf{R}^n$.

Let's write down the above calculation as a lemma.

**Lemma 3.1.** *For each $A \in \operatorname{M}_n(\mathbf{R})$, there is a $C \ge 0$ such that $\|Av\| \le C\|v\|$ for all $v \in \mathbf{R}^n$.*

The constant $C$ we wrote down might not be optimal. Perhaps there is a smaller constant $C' < C$ such that $\|Av\| \le C'\|v\|$ for all $v \in \mathbf{R}^n$. We will get a norm on $\operatorname{M}_n(\mathbf{R})$ by assigning to each $A \in \operatorname{M}_n(\mathbf{R})$ the least $C \ge 0$ such that $\|Av\| \le C\|v\|$ for all $v \in \mathbf{R}^n$, where the vector norms in $\|Av\|$ and $\|v\|$ are the standard ones on $\mathbf{R}^n$.

**Theorem 3.2.** *For each $A \in \operatorname{M}_n(\mathbf{R})$, there is a unique real number $b \ge 0$ such that*

*(i) $\|Av\| \le b\|v\|$ for all $v \in \mathbf{R}^n$,*

*(ii) $b$ is minimal: if $\|Av\| \le C\|v\|$ for all $v \in \mathbf{R}^n$, then $b \le C$.*

*Proof.* We first show by a scaling argument that $\|Av\| \le b\|v\|$ for all $v \in \mathbf{R}^n$ if and only if $\|Av\| \le b$ for all $v \in \mathbf{R}^n$ with $\|v\| = 1$. The direction ($\Rightarrow$) is clear by using $\|v\| = 1$. For the direction ($\Leftarrow$), when $v = 0$ we trivially have $\|Av\| = 0 = b\|v\|$. When $v \ne 0$ let $c = \|v\|$, so $c > 0$ and the vector $v/c$ has norm $1$ ($\|v/c\| = |1/c|\,\|v\| = (1/\|v\|)\|v\| = 1$), so by hypothesis $\|A(v/c)\| \le b$, which implies $(1/|c|)\|Av\| \le b$ by linearity. Now multiply both sides by $|c|$ to get $\|Av\| \le bc = b\|v\|$.

Therefore the theorem is saying the set $\{\|Av\| : \|v\| = 1\}$ has a (finite) maximum value, which is $b$. This is what we will prove.

The matrix $A$ as a function $\mathbf{R}^n \to \mathbf{R}^n$ is continuous since the components of $Av$ are linear functions of the components of $v$, and hence they are each continuous in $v$. The standard norm $\|\cdot\|: \mathbf{R}^n \to \mathbf{R}$ is also continuous since it is the square root of a polynomial function of the coordinates. Finally, since the unit sphere in $\mathbf{R}^n$, $\{v \in \mathbf{R}^n : \|v\| = 1\}$, is compact

<!-- page 5 -->

its continuous image $\{\|Av\| : \|v\| = 1\}$ in $\mathbf{R}$ is also compact. Every compact subset of $\mathbf{R}$ contains a maximum point, so we are done. $\square$

**Definition 3.3.** For $A \in \operatorname{M}_n(\mathbf{R})$, $\|A\|$ is the smallest nonnegative real number satisfying the inequality $\|Av\| \le \|A\|\,\|v\|$ for all $v \in \mathbf{R}^n$. This is called the *operator norm* of $A$.

Theorem 3.2 shows $\|A\|$ exists and is the maximum of $\|Av\|$ when $v$ runs over the unit sphere in $\mathbf{R}^n$, so in plain English, $\|A\|$ is the largest amount by which $A$ stretches a vector on the unit sphere of $\mathbf{R}^n$. The next theorem shows the operator norm on $\operatorname{M}_n(\mathbf{R})$ is a vector space norm and has a host of other nice properties.

**Theorem 3.4.** *For $A, B \in \operatorname{M}_n(\mathbf{R})$ and $v, w \in \mathbf{R}^n$,*

*(i) $\|A\| \ge 0$, with equality if and only if $A = O$.*

*(ii) $\|A + B\| \le \|A\| + \|B\|$.*

*(iii) $\|cA\| = |c|\,\|A\|$ for $c \in \mathbf{R}$.*

*(iv) $\|AB\| \le \|A\|\,\|B\|$. It is typically false that $\|AB\| = \|A\|\,\|B\|$.*

*(v) $\|A\| = \|A^\top\|$.*

*(vi) $\|AA^\top\| = \|A^\top A\| = \|A\|^2$. Thus $\|A\| = \sqrt{\|AA^\top\|} = \sqrt{\|A^\top A\|}$.*

*(vii) $|(Av, w)| \le \|A\|\,\|v\|\,\|w\|$.*

*(viii) $\|A\|_{\sup} \le \|A\| \le n\sqrt{n}\,\|A\|_{\sup}$ and $\operatorname{M}_n(\mathbf{R})$ is complete with respect to the metric coming from the operator norm.*

*Proof.* (i) It is obvious that $\|A\| \ge 0$. If $\|A\| = 0$ then for all $v \in \mathbf{R}^n$ we have $\|Av\| \le 0\,\|v\| = 0$, so $\|Av\| = 0$. Thus $Av = 0$ for all $v \in \mathbf{R}^n$, so $A = O$. The converse is trivial.

(ii) For all $v \in \mathbf{R}^n$,

$$\|(A + B)v\| = \|Av + Bv\|$$
$$\le \|Av\| + \|Bv\|$$
$$\le \|A\|\,\|v\| + \|B\|\,\|v\|$$
$$= (\|A\| + \|B\|)\,\|v\|.$$

Since $\|A + B\|$ is the *least* $C \ge 0$ such that $\|(A + B)v\| \le C\|v\|$ for all $v \in \mathbf{R}^n$, $\|A + B\| \le \|A\| + \|B\|$.

(iii) Left to the reader.

(iv) For all $v \in \mathbf{R}^n$, $\|(AB)v\| = \|A(Bv)\| \le \|A\|\,\|Bv\| \le \|A\|\,\|B\|\,\|v\|$, so the minimality property of the operator norm implies $\|AB\| \le \|A\|\,\|B\|$.

To show that generally $\|AB\| \ne \|A\|\,\|B\|$, note that if $\|AB\| = \|A\|\,\|B\|$ for all $A$ and $B$ in $\operatorname{M}_n(\mathbf{R})$ then for nonzero $A$ and $B$ we'd have $\|AB\| \ne 0$, so $AB \ne O$. That is, the product of two nonzero matrices is always nonzero. This is false when $n > 1$, since there are many nonzero matrices whose square is zero. (We sometimes do have $\|AB\| = \|A\|\,\|B\|$: see Exercise 3.2.)

(v) For all $v \in \mathbf{R}^n$, we get by (2.3) that

$$\|Av\|^2 = |(Av, Av)| = |(v, A^\top Av)| \le \|v\|\,\|A^\top Av\|$$

by Cauchy--Schwarz. This last expression is $\le \|A^\top A\|\,\|v\|^2$, so

$$\|Av\| \le \sqrt{\|A^\top A\|}\,\|v\|.$$

<!-- page 6 -->

The *least* $C \ge 0$ such that $\|Av\| \le C\|v\|$ for all $v \in \mathbf{R}^n$ is $\|A\|$, so $\|A\| \le \sqrt{\|A^\top A\|}$. Squaring both sides,

$$(3.1) \qquad \|A\|^2 \le \|A^\top A\| \le \|A^\top\|\,\|A\|.$$

Dividing by $\|A\|$ when $A \ne O$, we get $\|A\| \le \|A^\top\|$. This is also obvious if $A = O$, so

$$(3.2) \qquad \|A\| \le \|A^\top\|$$

for all $A \in \operatorname{M}_n(\mathbf{R})$. Now replace $A$ by $A^\top$ in (3.2) to get

$$\|A^\top\| \le \|(A^\top)^\top\| = \|A\|,$$

so $\|A\| = \|A^\top\|$.

(vi) Feeding the conclusion of (v) back into (3.1),

$$\|A\|^2 \le \|A^\top A\| \le \|A^\top\|\,\|A\| = \|A\|^2,$$

so $\|A\|^2 = \|A^\top A\|$. Using $A^\top$ in place of $A$ here, we get $\|A\|^2 = \|AA^\top\|$ since $\|A^\top\| = \|A\|$.

(vii) Use Cauchy--Schwarz: $|(Av, w)| \le \|Av\|\,\|w\| \le \|A\|\,\|v\|\,\|w\|$.

(viii) Set $v = e_j$ and $w = e_i$ in (vii):

$$|a_{ij}| = |(Ae_j, e_i)| \le \|A\|.$$

Therefore $\|A\|_{\sup} \le \|A\|$. The other inequality follows from the calculation leading up to Lemma 3.1.

That $\operatorname{M}_n(\mathbf{R})$ is complete with respect to the metric $d(A, B) = \|A - B\|$ coming from the operator norm follows from completeness of $\operatorname{M}_n(\mathbf{R})$ with respect to the metric coming from the sup-norm (view $\operatorname{M}_n(\mathbf{R})$ as $\mathbf{R}^{n^2}$) and the fact that these two norms on $\operatorname{M}_n(\mathbf{R})$ are bounded by constant multiples of each other. $\square$

The operator norm on $\operatorname{M}_n(\mathbf{R})$ interacts nicely with the multiplicative structure on $\operatorname{M}_n(\mathbf{R})$ and the standard inner product on $\mathbf{R}^n$ (parts (iv) through (vii) of Theorem 3.4). However, unlike the standard norm on $\mathbf{R}^n$, the operator norm on $\operatorname{M}_n(\mathbf{R})$ is impossible to calculate from its definition in all but the simplest cases. For instance, it is clear that $\|I_n\| = 1$, so $\|cI_n\| = |c|$ for all $c \in \mathbf{R}$. But what is

$$\left\|\begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}\right\|?$$

By the last part of Theorem 3.4, this norm is bounded above by $2\sqrt{2}(4) = 8\sqrt{2} \approx 11.3$. In the next section we will give a formula for the operator norm on $\operatorname{M}_n(\mathbf{R})$ that will allow us to compute $\left\|\begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}\right\|$ easily, and it will turn out to be $\approx 5.5$.

Exercises.

1. Rework this section for rectangular matrices that need not be square. For $A$ in $\operatorname{M}_{m,n}(\mathbf{R})$, define its operator norm $\|A\|_{m,n}$ to be the least $b \ge 0$ such that $\|Av\|_m \le b\|v\|_n$ for all $v \in \mathbf{R}^n$, where the subscripts in the inequality indicate the standard norm on the Euclidean space of the relevant dimension ($m$ or $n$). Show $\|A\|_{m,n}$ exists and

$$\|A\|_{m,n} = \|A^\top\|_{n,m} = \sqrt{\|AA^\top\|_{m,m}} = \sqrt{\|A^\top A\|_{n,n}}.$$

You will want to use the relationship between the transpose on $\operatorname{M}_{m,n}(\mathbf{R})$ and dot products on $\mathbf{R}^m$ and $\mathbf{R}^n$ in Exercise 2.1.

<!-- page 7 -->

2. An $n \times n$ *rotation matrix* is a matrix $R \in \operatorname{M}_n(\mathbf{R})$ such that $RR^\top = I_n$ (equivalently, $R^\top R = I_n$), which is the same as the condition $\langle Rv, Rw\rangle = \langle v, w\rangle$ for all $v$ and $w$ in $\mathbf{R}^n$. Prove $\|R\| = 1$ and for every $n \times n$ real matrix $A$, $\|AR\| = \|A\|$ and $\|RA\| = \|A\|$. (Hint: use the submultiplicativity property of the operator norm in Theorem 3.4(iv).)

3. Define an operator norm on $\operatorname{M}_n(\mathbf{C})$ and establish an analogue of Theorem 3.4. Is it true that a matrix in $\operatorname{M}_n(\mathbf{C})$ generally has the same operator norm as its transpose? For a real $n \times n$ matrix, show its operator norm as an element of $\operatorname{M}_n(\mathbf{R})$ equals its operator norm as an element of $\operatorname{M}_n(\mathbf{C})$.

## 4. A Computational Formula for the Operator Norm on $\operatorname{M}_n(\mathbf{R})$

The key idea to compute the operator norm of $A \in \operatorname{M}_n(\mathbf{R})$ is that Theorem 3.4(vi) tells us $\|A\|$ is the square root of the operator norm of $AA^\top$ and $A^\top A$. What makes $AA^\top$ and $A^\top A$ special is that they are symmetric (equal to their own transposes), *e.g.*, $(AA^\top)^\top = (A^\top)^\top A^\top = AA^\top$.[^1] The following theorem gives a formula for operator norms of symmetric matrices and that will lead to an operator norm formula on all matrices in $\operatorname{M}_n(\mathbf{R})$.

**Theorem 4.1.** *(1) If $A \in \operatorname{M}_n(\mathbf{R})$ satisfies $A^\top = A$ then all the eigenvalues of $A$ are real and*

$$(4.1) \qquad \|A\| = \max_{\text{eigenvalues } \lambda \text{ of } A} |\lambda|.$$

*(2) For all $A \in \operatorname{M}_n(\mathbf{R})$, the eigenvalues of $AA^\top$ and $A^\top A$ are all nonnegative.*

*Proof. Proof of (1).* To prove that when $A^\top = A$ all the eigenvalues of $A$ are real, let $A$ act on $\mathbf{C}^n$ in the obvious way. Using the standard inner product (2.4) on $\mathbf{C}^n$ (not the dot product!), we have by (2.5) that for all $v \in \mathbf{C}^n$,

$$(Av, v) = (v, A^*v) = (v, \overline{A}^\top v) = (v, A^\top v) = (v, Av).$$

For an eigenvalue $\lambda \in \mathbf{C}$ of $A$, let $v \in \mathbf{C}^n$ be a corresponding eigenvector. Then

$$(Av, v) = (\lambda v, v) = \lambda(v, v), \quad (v, Av) = (v, \lambda v) = \bar{\lambda}(v, v),$$

so $\lambda = \bar{\lambda}$ since $(v, v) = \|v\|^2 \ne 0$ (eigenvectors are nonzero). Thus $\lambda$ is real.

To prove (4.1), we give two arguments.

**Method 1.** We will use a fundamental property of real symmetric matrices called the *Spectral Theorem*. It says that each symmetric matrix $A \in \operatorname{M}_n(\mathbf{R})$ has a basis of mutually orthogonal eigenvectors in $\mathbf{R}^n$.[^2] Let $v_1, \ldots, v_n$ be a basis of mutually orthogonal eigenvectors for $A$, with corresponding eigenvalues $\lambda_1, \ldots, \lambda_n$. What is special about orthogonal vectors is that their squared lengths add (the Pythagorean theorem): if $(v, w) = 0$ then

$$\|v + w\|^2 = (v + w, v + w) = (v, v) + 2(v, w) + (w, w) = (v, v) + (w, w) = \|v\|^2 + \|w\|^2$$

and likewise for a sum of more than two mutually orthogonal vectors.

Order the eigenvalues of $A$ so that $|\lambda_1| \le \cdots \le |\lambda_n|$. For each $v \in \mathbf{R}^n$, write it in terms of the basis of eigenvectors as

$$v = c_1 v_1 + \cdots + c_n v_n.$$

[^1]: This is also true if $A \in \operatorname{M}_{m,n}(\mathbf{R})$ is a rectangular matrix, which makes Section 4 applicable to operator norms of rectangular matrices by Exercise 3.1.
[^2]: The Spectral Theorem includes the assertion that all eigenvalues of $A$ are real, which we showed above.

<!-- page 8 -->

Then

$$Av = c_1 A(v_1) + \cdots + c_n A(v_n) = c_1 \lambda_1 v_1 + \cdots + c_n \lambda_n v_n.$$

Since the $v_i$'s are mutually perpendicular, their scalar multiples $c_i \lambda_i v_i$ are mutually perpendicular. Therefore

$$\|Av\|^2 = \|c_1 \lambda_1 v_1\|^2 + \cdots + \|c_n \lambda_n v_n\|^2$$
$$= c_1^2 \lambda_1^2 \|v_1\|^2 + \cdots + c_n^2 \lambda_n^2 \|v_n\|^2$$
$$\le c_1^2 \lambda_n^2 \|v_1\|^2 + \cdots + c_n^2 \lambda_n^2 \|v_n\|^2 \quad \text{since } |\lambda_i| \le |\lambda_n|$$
$$= \lambda_n^2(c_1^2\|v_1\|^2 + \cdots + c_n^2\|v_n\|^2)$$
$$= \lambda_n^2(\|c_1 v_1\|^2 + \cdots + \|c_n v_n\|^2)$$
$$= \lambda_n^2\|c_1 v_1 + \cdots + c_n v_n\|^2$$
$$= \lambda_n^2\|v\|^2,$$

so $\|Av\| \le |\lambda_n|\,\|v\|$. Since this inequality holds for all $v$ in $\mathbf{R}^n$, we have $\|A\| \le |\lambda_n|$. To prove $\|A\| = |\lambda_n|$ it now suffices to find a single nonzero vector $v$ such that $\|Av\| = |\lambda_n|\,\|v\|$. For that we can use $v = v_n$ since $Av_n = \lambda_n v_n$.

**Method 2.** Our second method of proving (4.1) is a technique that is part of an approach to proving the Spectral Theorem. It uses a refined version of (4.1) that includes another formula for $\|A\|$ when $A^\top = A$:

$$(4.2) \qquad \|A\| = \max_{\|v\|=1} |(Av, v)| = \max_{\text{eigenvalues } \lambda \text{ of } A} |\lambda|.$$

If you don't want to read through this second method, read ahead to find the proof of (2).

To show $\|A\| = \max_{\|v\|=1} |(Av, v)|$ when $A^\top = A$, first we have by Theorem 3.4(vii) that $|(Av, v)| \le \|A\|\,\|v\|^2 = \|A\|$ if $\|v\| = 1$, so $\max_{\|v\|=1} |(Av, v)| \le \|A\|$. That maximum does exist: the function $f(v) = |(Av, v)|$ from $\mathbf{R}^n$ to $[0, \infty)$ is continuous, so $f$ achieves a maximum value on the unit sphere $\{v \in \mathbf{R}^n : \|v\| = 1\}$ since that sphere is compact (every continuous real-valued function on a compact set achieves maximum and minimum values). To prove the reverse inequality $\|A\| \le \max_{\|v\|=1} |(Av, v)|$, set $m = \max_{\|v\|=1} |(Av, v)| \ge 0$. We'll show

$$(4.3) \qquad \|Av\| \le m\|v\|$$

for all $v \in \mathbf{R}^n$, so $\|A\| \le m$ by the definition of $\|A\|$.

For nonzero $v$ in $\mathbf{R}^n$, $v/\|v\|$ has norm $1$, so $|(A(v/\|v\|), v/\|v\|)| \le m$. Since $A(v/\|v\|) = (Av)/\|v\|$, we get $|(Av, v)| \le m\|v\|^2$. This inequality is obvious when $v = 0$, so it holds for all $v$ in $\mathbf{R}^n$. We now use the Polarization Identity, which is valid for every inner product and linear map $A$:

$$(A(v + w), v + w) - (A(v - w), v - w) = 2((Av, w) + (Aw, v)).$$

Just expand the left side by additivity to get the right side, thus verifying the identity. When $A = A^\top$, the right side is $4(Av, w)$. Therefore if we take absolute values of both

[^3]: This formula for $\|A\|$ has counterexamples if $A^\top \ne A$: for $A = \begin{pmatrix}0 & -1\\1 & 0\end{pmatrix}$, $(Av, v) = 0$ for all $v$ and $A \ne O$.

<!-- page 9 -->

sides,

$$4|(Av, w)| \le m\|v + w\|^2 + m\|v - w\|^2$$
$$= m((v + w, v + w) + (v - w, v - w))$$
$$= 2m((v, v) + (w, w))$$
$$= 2m(\|v\|^2 + \|w\|^2).$$

When $\|v\| = 1$ and $\|w\| = 1$, this implies $4|(Av, w)| \le 4m$, so $|(Av, w)| \le m$ if $\|v\| = \|w\| = 1$. Scaling, this implies for all $v$ and $w$ in $\mathbf{R}^n$ that $|(Av, w)| \le m\|v\|\,\|w\|$. Now set $w = Av$. We get

$$\|Av\|^2 = |(Av, Av)| \le m\|v\|\,\|Av\|.$$

Therefore $\|Av\| \le m\|v\|$ if $Av \ne 0$. It is also obvious if $Av = 0$, so we have proved (4.3), which proves the first equation in (4.2).

To prove the rest of (4.2), let $\lambda$ be an eigenvalue of $A$ and $v$ be a corresponding eigenvector in $\mathbf{R}^n$. (We already showed every eigenvalue of $A$ is real when $A = A^\top$, so each eigenvalue of $A$ has a real eigenvector.) We can normalize $v$ so that $\|v\| = 1$. Then $Av = \lambda v \Rightarrow \|Av\| = \|\lambda v\| = |\lambda|\,\|v\| = |\lambda|$, so $|\lambda| = \|Av\| \le \|A\|\,\|v\| = \|A\|$. Therefore the maximal absolute value of the eigenvalues of $A$ is at most $\|A\|$. To finish the proof of (4.2), we'll show $\|A\|$ or $-\|A\|$ is an eigenvalue of $A$, by using the formula $\|A\| = \max_{\|v\|=1} |(Av, v)|$ that we already proved.

Let $v' \in \mathbf{R}^n$ satisfy $\|v'\| = 1$ and $|(Av', v')| = \|A\|$. Set $\alpha = (Av', v') = \pm\|A\|$. We will show $Av' = \alpha v'$, so $\alpha$ is an eigenvalue of $A$:

$$\|Av' - \alpha v'\|^2 = (Av' - \alpha v', Av' - \alpha v')$$
$$= (Av', Av') - \alpha(Av', v') - \alpha(v', Av') + \alpha^2(v', v')$$
$$= \|Av'\|^2 - \alpha(Av', v') - \alpha(A^\top v', v') + \alpha^2.$$

Since $A^\top = A$,

$$\|Av'\|^2 - \alpha(Av', v') - \alpha(Av', v') + \alpha^2 = \|Av'\|^2 - \alpha^2 - \alpha^2 + \alpha^2 = \|Av'\|^2 - \alpha^2$$

and $\|Av'\| \le \|A\|\,\|v'\| = \|A\|$, so

$$0 \le \|Av' - \alpha v'\|^2 \le \|A\|^2 - \alpha^2 = \|A\|^2 - \|A\|^2 = 0.$$

Therefore $\|Av' - \alpha v'\| = 0$, so $Av' = \alpha v'$.

**Proof of (2).** Since $AA^\top$ and $A^\top A$ are both symmetric, all their eigenvalues are real. Let $\lambda \in \mathbf{R}$ be an eigenvalue of $AA^\top$ with corresponding eigenvector $v \in \mathbf{R}^n$, and let $\mu \in \mathbf{R}$ be an eigenvalue of $A^\top A$ with corresponding eigenvector $w \in \mathbf{R}^n$. Using the standard inner product on $\mathbf{R}^n$,

$$0 \le (Aw, Aw) = (w, A^\top Aw) = (w, \mu w) = \mu(w, w).$$

Then $\mu \ge 0$ since $(w, w) = \|w\|^2 > 0$. Similarly,

$$0 \le (A^\top v, A^\top v) = (v, AA^\top v) = (v, \lambda v) = \lambda(v, v).$$

Since $(v, v) = \|v\|^2 > 0$, it follows that $\lambda \ge 0$. $\square$

**Remark 4.2.** The second equality in (4.2), $\max_{\|v\|=1} |(Av, v)| = \max_\lambda |\lambda|$, is also true without the absolute values: the maximum value of $(Av, v)$ over all $v \in \mathbf{R}^n$ with $\|v\| = 1$ is the maximum eigenvalue of $A$. And if we order all the eigenvalues of a real symmetric

<!-- page 10 -->

$n \times n$ matrix $A$ as $\lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$ then the $k$th smallest eigenvalue $\lambda_k$ has a "min-max" formula:

$$\lambda_k = \min_W \max_{\substack{w \in W \\ \|w\|=1}} (Aw, w),$$

where the minimum runs over all subspaces $W$ of $\mathbf{R}^n$ with dimension $k$. (At $k = n$, the only such $W$ is $\mathbf{R}^n$, so the biggest eigenvalue of $A$ is the maximum of $(Aw, w)$ where $w$ runs over vectors in $\mathbf{R}^n$ with unit length.) If instead we order the eigenvalues of $A$ from greatest to least as $\mu_1 \ge \mu_2 \ge \cdots \ge \mu_n$ (so $\mu_k = \lambda_{n+1-k}$), then the $k$th largest eigenvalue $\mu_k$ has a "max-min" formula:

$$\mu_k = \max_W \min_{\substack{w \in W \\ \|w\|=1}} (Aw, w),$$

where the maximum runs over all subspaces $W$ of $\mathbf{R}^n$ with dimension $k$.[^4]

**Corollary 4.3.** *For $A \in \operatorname{M}_n(\mathbf{R})$, $\|A\|$ is the square root of the largest eigenvalue of $AA^\top$ and is the square root of the largest eigenvalue of $A^\top A$.*

*Proof.* By Theorem 3.4(vi), $\|A\| = \sqrt{\|AA^\top\|} = \sqrt{\|A^\top A\|}$. Now use (4.1), with $AA^\top$ and $A^\top A$ in place of $A$. $\square$

**Remark 4.4.** This corollary, without proof, goes back to Peano [3, p. 454] using $A^\top A$. On the same page Peano introduced the operator norm on $\operatorname{M}_n(\mathbf{R})$ from Definition 3.3 and proved Theorem 3.4(ii) and (iv). In the same year (1888) Peano [4] introduced the first axiomatic treatment of real vector spaces (which he called "linear systems") of arbitrary dimension and linear operators on them; it was ahead of its time and largely forgotten, including by Peano himself. The main inspiration for the development of abstract linear algebra came from work on normed vector spaces by Banach in the 1920s [2].

**Example 4.5.** Let's compute the operator norm of the $2 \times 2$ matrix

$$A = \begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}.$$

Since

$$AA^\top = \begin{pmatrix}5 & 11\\11 & 25\end{pmatrix},$$

the characteristic polynomial of $AA^\top$ is $X^2 - 30X + 4$, which has eigenvalues $15 \pm \sqrt{221} \approx .13, 29.86$. Therefore the operator norm of $A$ is $\sqrt{15 + \sqrt{221}}$, so for all $\binom{x}{y} \in \mathbf{R}^2$,

$$\left\|\begin{pmatrix}5x + 11y\\11x + 25y\end{pmatrix}\right\| \le \sqrt{15 + \sqrt{221}}\left\|\binom{x}{y}\right\|,$$

and $\sqrt{15 + \sqrt{221}} \approx 5.46$ is the smallest number with that property.

**Example 4.6.** For the $2 \times 2$ matrix

$$A = \begin{pmatrix}3 & 2\\1 & 2\end{pmatrix},$$

we have

$$AA^\top = \begin{pmatrix}13 & 7\\7 & 5\end{pmatrix},$$

[^4]: See https://en.wikipedia.org/wiki/Min-max_theorem.

<!-- page 11 -->

which has characteristic polynomial $X^2 - 18X + 16$ and eigenvalues $9 \pm \sqrt{65}$, so $\|A\| = \sqrt{9 + \sqrt{65}} \approx 4.13$.

The matrix $A$ has characteristic polynomial $X^2 - 5X + 4 = (X - 1)(X - 4)$, so its eigenvalues are $1$ and $4$. This makes $A$ conjugate to the diagonal matrix $D = \begin{pmatrix}4 & 0\\0 & 1\end{pmatrix}$: $A = UDU^{-1}$, where $U = \begin{pmatrix}2 & 1\\1 & -1\end{pmatrix}$. Since $D$ is symmetric, $\|D\| = 4 < \|A\|$. This illustrates that conjugate matrices like $A$ and $D$ need not have the same operator norm, although matrices that are conjugate by a rotation matrix have the same operator norm: $\|RAR^{-1}\| = \|A\|$ if $RR^\top = I_n$ (see Exercise 3.2). The conjugating matrix $U$ is not a rotation matrix.

Computing the operator norm of $A$ amounts to finding the largest eigenvalue of a related symmetric matrix ($AA^\top$ or $A^\top A$). In practice, for large symmetric matrices the largest eigenvalue is *not* computed by calculating the roots of its characteristic polynomial. More efficient algorithms for calculating eigenvalues are available (*e.g.*, QR algorithm or Lanczos algorithm).

Exercises.

1. For $A \in \operatorname{M}_{m,n}(\mathbf{R})$, show the eigenvalues of the $m \times m$ matrix $AA^\top$ and the $n \times n$ matrix $A^\top A$ are nonnegative. (The nonzero eigenvalues of these matrices are also equal. For all $A \in \operatorname{M}_{m,n}(\mathbf{R})$ and $B \in \operatorname{M}_{n,m}(\mathbf{R})$, the matrices $AB \in \operatorname{M}_m(\mathbf{R})$ and $BA \in \operatorname{M}_n(\mathbf{R})$ have the same nonzero eigenvalues.)

2. If you worked out properties of operator norms of rectangular matrices in Exercise 3.1, then show the operator norm of the $2 \times 3$ matrix

$$\begin{pmatrix}1 & 2 & 3\\4 & 5 & 6\end{pmatrix}$$

is $\sqrt{(91 + \sqrt{8065})/2}$.

3. If we use a norm on $\mathbf{R}^n$ other than the standard norm, the corresponding operator norm on $\operatorname{M}_n(\mathbf{R})$ will be different from the one we have worked with here. When $\mathbf{R}^n$ has a norm $\|\cdot\|'$, the related operator norm of a matrix $A \in \operatorname{M}_n(\mathbf{R})$ is the least $b \ge 0$ such that $\|Av\|' \le b\|v\|'$ for all $v \in \mathbf{R}^n$. Let's consider this in two examples: the sup-norm $\|(x_1, \ldots, x_n)\|_{\sup} = \max|x_i|$ and the 1-norm $\|(x_1, \ldots, x_n)\|_1 = \sum_{i=1}^n |x_i|$.

(a) For all $v \in \mathbf{R}^n$, show $\|Av\|_{\sup} \le r_A\|v\|_{\sup}$ where $r_A = \max_{1 \le i \le n}\sum_{j=1}^n |a_{ij}|$. The number $r_A$ is the maximum sum of the absolute values along the *rows* of $A$.

(b) For each row $(a_{i1}, \ldots, a_{in})$ of $A$, show there is a vector $v_i$ in $\mathbf{R}^n$ with coordinates from $\{\pm 1\}$ such that the $i$th entry of $Av_i$ equals $|a_{i1}| + \cdots + |a_{in}|$. Conclude that there is a nonzero $v \in \mathbf{R}^n$ such that $\|Av\|_{\sup} = r_A\|v\|_{\sup}$ where $r_A$ is the number in part (a). Thus the operator norm of $A$ when using the sup-norm on $\mathbf{R}^n$ is $r_A$.

(c) For all $v \in \mathbf{R}^n$, show $\|Av\|_1 \le c_A\|v\|_1$ where $c_A = \max_{1 \le j \le n}\sum_{i=1}^n |a_{ij}|$, which is the maximum sum of the absolute values along the *columns* of $A$.

(d) Let $e_k$ be the $k$th standard basis vector of $\mathbf{R}^n$. Show $\|Ae_k\|_1 = \sum_{i=1}^n |a_{ik}|$ and conclude there is a nonzero $v \in \mathbf{R}^n$ such that $\|Av\|_1 = c_A\|v\|_1$, so the operator norm of $A$ when using the 1-norm on $\mathbf{R}^n$ is $c_A$.

**Note:** For $p \ge 1$ the *p-norm* on $\mathbf{R}^n$ is $\|(x_1, \ldots, x_n)\|_p = \sqrt[p]{\sum|x_i|^p}$. The standard norm on $\mathbf{R}^n$ is the 2-norm and the sup-norm is a limit of $p$-norms: $\|v\|_\infty = \lim_{p \to \infty}\|v\|_p$. It is unlikely that there is an efficient algorithm to compute the operator $p$-norm of a general $n \times n$ real matrix when $p \ne 1, 2, \infty$; see [1].

<!-- page 12 -->

4. Generalize Theorem 4.1 to give a computational formula for the operator norm of matrices in $\operatorname{M}_n(\mathbf{C})$.

## Appendix A. Proof of Cauchy-Schwarz Inequality

We give a proof of the Cauchy--Schwarz inequality that was found by Schwarz [5, p. 344] in 1888. It is a clever trick with quadratic polynomials and the context in which Schwarz discovered it is described in [6, pp. 10--11]. (The whole book [6] is recommended as a lively account of fundamental inequalities in mathematics.)

Let $V$ be a real vector space with an inner product $(\cdot, \cdot)$. Pick $v$ and $w$ in $V$. Our goal is to show

$$|(v, w)| \le \|v\|\,\|w\|.$$

This is obvious if $v$ or $w$ is $0$, so assume both are nonzero. For all $t \in \mathbf{R}$, $(v + tw, v + tw) \ge 0$. The left side can be expanded to be a quadratic polynomial in $t$:

$$(v + tw, v + tw) = (v, v) + (v, tw) + (tw, v) + (tw, tw)$$
$$= (v, v) + t(v, w) + t(w, v) + t^2(w, w)$$
$$= \|v\| + 2(v, w)t + \|w\|\,t^2.$$

This is quadratic since $\|w\| > 0$. A quadratic polynomial in $t$ has nonnegative values for all $t$ if and only if its discriminant is $\le 0$, so

$$(2(v, w))^2 - 4\|v\|\,\|w\| \le 0,$$

which is equivalent to $|(v, w)| \le \|v\|\,\|w\|$, and that completes the proof!

**Remark A.1.** We have equality $|(v, w)| = \|v\|\,\|w\|$ if and only if the quadratic polynomial above has a double real root $t$, and at that root we get $(v + tw, v + tw) = 0$, so $v + tw = 0$ in $V$ and thus $v$ and $w$ are linearly dependent. The converse direction, that linear dependence implies equality in the Cauchy--Schwarz inequality, is left to the reader (also in the case that $v$ or $w$ is $0$).

## References

[1] J. M. Hendrickx, A. Olshevsky, Matrix $p$-norms are NP-hard to approximate if $p \ne 1, 2, \infty$, *SIAM J. Matrix Anal. Appl.* **31** (2010), 2802--2812. URL https://arxiv.org/abs/0908.1397.

[2] G. H. Moore, The Axiomatization of Linear Algebra: 1875--1940, *Historia Mathematica* **22** (1995), 262--303. URL https://core.ac.uk/download/pdf/82128888.pdf.

[3] G. Peano, Intégration par séries des équations différentielles linéaires, *Mathematische Annalen* **32** (1888), 450--456. URL https://eudml.org/doc/157389.

[4] G. Peano, "Calcolo Geometrico secondo l'Ausdehnungslehre di H. Grassmann, preceduto dalle operazioni della logica deduttiva," Fratelli Bocca, Turin, 1888. URL http://mathematica.sns.it/opere/138/.

[5] H. A. Schwarz, Über ein die Flächen kleinsten Flächeninhalts betreffendes Problem der Variationsrechnung, *Acta Soc. Scient. Fenn.* **15** (1888), 315--362. URL https://www.biodiversitylibrary.org/item/52183#page/323/mode/1up.

[6] J. M. Steele, "The Cauchy--Schwarz Master Class: An Introduction to the Art of Mathematical Inequalities," Cambridge Univ. Press, Cambridge, 2004.
