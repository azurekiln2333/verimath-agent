# $L^p$-Spaces for $0 < p < 1$

> **Source**: https://kconrad.math.uconn.edu/blurbs/lpspace.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis

<!-- page 1 -->

## 1. Introduction

In a first course in functional analysis, a great deal of time is spent with Banach spaces, especially the interaction between such spaces and their dual spaces. Banach spaces are a special type of topological vector space, and there are important topological vector spaces that do not lie in the Banach category, such as the Schwartz spaces.

The most fundamental theorem about Banach spaces is the Hahn-Banach theorem, which links the original Banach space with its dual space. What we want to illustrate here is a wide collection of topological vector spaces where the Hahn-Banach theorem has no obvious extension because the dual space is *zero*. The model for a topological vector space with zero dual space will be $L^p[0, 1]$ when $0 < p < 1$. After proving the dual of this space is $\{0\}$, we'll see how to make the proof work for other $L^p$-spaces, with $0 < p < 1$. The argument eventually culminates in a pretty theorem from measure theory (Theorem 4.2) that can be understood at the level of a first course on that subject.

## 2. Banach Spaces and Beyond

In this section, to provide some context, we recall some basic classes of vector spaces that are important in analysis.

Throughout, our vector spaces are real vector spaces. All that we say would go through with minimal change to complex vector spaces.

**Definition 2.1.** A *norm* on a vector space $V$ is a function $\|\cdot\|: V \to \mathbf{R}$ satisfying

- $\|v\| \ge 0$, with equality if and only if $v = 0$,
- $\|v + w\| \le \|v\| + \|w\|$ for all $v$ and $w$ in $V$,
- $\|cv\| = |c|\|v\|$ for all scalars $c$ and $v \in V$.

Given a norm on a vector space, we get a metric by $d(v, w) = \|v - w\|$.

**Example 2.2.** On $\mathbf{R}^n$, we have the sup-norm $|\mathbf{x}|_{\sup} = \max_{1 \le i \le n} |x_i|$ and the $L^2$-norm $|\mathbf{x}|_2 = \mathbf{x} \cdot \mathbf{x} = (\sum_{i=1}^n |x_i|^2)^{1/2}$. The metric coming from the $L^2$-norm is the usual notion of distance on $\mathbf{R}^n$. The metric on $\mathbf{R}^n$ coming from the sup-norm has balls that are actually cubes. These two norms give rise to the same topology on $\mathbf{R}^n$. Actually, all norms on $\mathbf{R}^n$ give it the same topology.[^1]

**Example 2.3.** The space $C[0, 1]$ of continuous real-valued functions on $[0, 1]$ has the sup-norm $|f|_{\sup} = \sup_{x \in [0,1]} |f(x)|$ and the $L^2$-norm $|f|_2 = (\int_0^1 |f(x)|^2 \, \mathrm{d}x)^{1/2}$. While functions that are close in the sup-norm are close in the $L^2$-norm, the converse is false: a function whose graph is close to the $x$-axis except for a tall thin spike is near $0$ in the $L^2$-norm but not in the sup-norm.

[^1]: See Theorem 2.7 in https://kconrad.math.uconn.edu/blurbs/topology/finite-dim-TVS.pdf.

<!-- page 2 -->

**Definition 2.4.** A *Banach space* is a vector space $V$ equipped with a norm $\|\cdot\|$ such that, with respect to the metric defined by $d(v, w) = \|v - w\|$, $V$ is complete.

**Example 2.5.** Under either norm in Example 2.2, $\mathbf{R}^n$ is a Banach space.

**Example 2.6.** In the sup-norm, $C[0, 1]$ is a Banach space (convergence in the sup-norm is exactly the concept of uniform convergence). But in the $L^2$-norm, $C[0, 1]$ is not a Banach space. That is, $C[0, 1]$ is not complete for the $L^2$-norm.

**Definition 2.7.** For a Banach space $V$, its *dual space* is the space of continuous linear functionals $V \to \mathbf{R}$, and is denoted $V^*$.

Continuity is important. We do not care about arbitrary linear functionals (as in linear algebra), but only those that are continuous. One of the important features of a Banach space is that we can use continuous linear functionals to separate points.

**Theorem 2.8.** *Let $V$ be a Banach space. For each non-zero $v \in V$, there is a $\varphi \in V^*$ such that $\varphi(v) \ne 0$. Thus, given distinct $v$ and $w$ in $V$, there is a $\varphi \in V^*$ such that $\varphi(v) \ne \varphi(w)$.*

Theorem 2.8 is a special case of the Hahn-Banach theorem, and can be found in texts on functional analysis. Even this special case can't be proved in a constructive way (when $V$ is infinite-dimensional). Its general proof depends on the axiom of choice.

**Example 2.9.** On $C[0, 1]$, the evaluation maps $e_a: f \mapsto f(a)$, for $a \in \mathbf{R}$, are linear functionals. Since $|f(a)| \le |f|_{\sup}$, each $e_a$ is continuous for the sup-norm. If $f \ne 0$ in $C[0, 1]$, there is some $a$ such that $f(a) \ne 0$, and then $e_a(f) = f(a) \ne 0$.

Using the sup-norm topology on $C[0, 1]$, the dual space $C[0, 1]^*$ is the space of bounded Borel measures (or Riemann-Stieltjes integrals) on $[0, 1]$, with the evaluation maps $e_a$ corresponding to point masses.

**Definition 2.10.** A *topological vector space* is a (real) vector space $V$ equipped with a Hausdorff topology in which addition $V \times V \to V$ and scalar multiplication $\mathbf{R} \times V \to V$ are continuous.

Note the Hausdorff condition is part of the definition. We won't be using non-Hausdorff spaces.

**Example 2.11.** For $n \ge 1$, the usual topology on $\mathbf{R}^n$ makes it a topological vector space. Using instead the discrete topology, indicated by writing $\mathbf{R}^n_d$, does not make a topological vector space: for nonzero $\mathbf{v}_0$ in $\mathbf{R}^n_d$, $\{\mathbf{v}_0\}$ is open and scalar multiplication $\mathbf{R} \times \{\mathbf{v}_0\} \to \mathbf{R}^n$ is continuous, so the inverse image of $\{\mathbf{v}_0\}$ in $\mathbf{R} \times \{\mathbf{v}_0\}$ is open. That is $\{(1, \mathbf{v}_0)\}$, and $\mathbf{R} \times \{\mathbf{v}_0\}$ is homeomorphic to $\mathbf{R}$, so $\{1\}$ is open in $\mathbf{R}$, which is not true. In fact, the usual topology on $\mathbf{R}^n$ is the only Hausdorff topology that makes it a topological vector space[^2] and the only topological vector space over $\mathbf{R}$ with the discrete topology is the zero space[^3].

**Example 2.12.** Every Banach space is a topological vector space.

**Definition 2.13.** A subset of a vector space is called *convex* if, for all $v$ and $w$ in the subset, the line segment $tv + (1 - t)w$, for $0 \le t \le 1$, is in the subset.

More generally, if a subset is convex and $v_1, \ldots, v_m$ are in the subset, then every weighted sum $\sum_{i=1}^m c_i v_i$ with $c_i \ge 0$ and $\sum_{i=1}^m c_i = 1$ is in the subset. In particular, the subset contains the average $(1/m)\sum_{i=1}^m v_i$.

[^2]: See Theorem 2.7 in https://kconrad.math.uconn.edu/blurbs/topology/finite-dim-TVS.pdf.
[^3]: See https://math.stackexchange.com/questions/492483.

<!-- page 3 -->

**Definition 2.14.** A topological vector space is called *locally convex* if the convex open sets are a base for the topology: given an open set $U$ around a point, there is a convex open set $C$ containing that point such that $C \subset U$.

**Example 2.15.** Every Banach space is locally convex, since all open balls are convex. This follows from the definition of a norm.

Since topological vector spaces are homogeneous (we can use addition to translate neighborhoods around one point to neighborhoods around other points), the locally convex condition can be checked by focusing at the origin: the open sets around $0$ need to contain a basis of convex open sets.

**Example 2.16.** The space $C(\mathbf{R})$ of continuous real-valued functions on $\mathbf{R}$ does not have the sup-norm over all of $\mathbf{R}$ as a norm: a continuous function on $\mathbf{R}$ could be unbounded. But $C(\mathbf{R})$ can be made into a locally convex topological vector space as follows. For each positive integer $n$, define a "semi-norm" $|\cdot|_n$ by

$$|f|_n = \sup_{|x| \le n} |f(x)|.$$

This is just like a norm, except it might assign value $0$ to a non-zero function. That is, a function could vanish on $[-n, n]$ without vanishing everywhere. Of course, if we take $n$ large enough, a non-zero continuous function will have non-zero $n$-th semi-norm, so the total collection of semi-norms $|\cdot|_n$ as $n$ varies, rather than one particular semi-norm, lets us distinguish different functions from each other. Using these semi-norms, define a basic open set around $f \in C(\mathbf{R})$ to be the set of all functions in $C(\mathbf{R})$ that are close to $f$ in a finite number of semi-norms:

$$U(f; n_1, \ldots, n_r) := \{g \in C(\mathbf{R}) : |g - f|_{n_1} < \varepsilon, \ldots, |g - f|_{n_r} < \varepsilon\}$$

for some $n_1, \ldots, n_r$ in $\mathbf{Z}^+$ and $\varepsilon > 0$. These subsets of $C(\mathbf{R})$ are a basis for a topology on $C(\mathbf{R})$ that makes it a locally convex topological vector space.

**Definition 2.17.** When $V$ is a topological vector space, its *dual space* $V^*$ is the space of continuous linear functionals $V \to \mathbf{R}$.

Theorem 2.8 generalizes to all locally convex spaces, as follows.

**Theorem 2.18.** *Let $V$ be a locally convex topological vector space. For distinct $v$ and $w$ in $V$, there is a $\varphi \in V^*$ such that $\varphi(v) \ne \varphi(w)$.*

*Proof.* See the chapters on locally convex spaces in [3] or [10]. $\square$

Let's meet some topological vector spaces that are *not* locally convex.

**Example 2.19.** Let $L^{1/2}[0, 1]$ be the set of all measurable functions $f: [0, 1] \to \mathbf{R}$ such that $\int_0^1 |f(x)|^{1/2} \, \mathrm{d}x < \infty$, with functions equal almost everywhere identified. (We need to make such an identification, since integration does not distinguish between two functions that differ on a set of measure $0$.)

Define a metric on $L^{1/2}[0, 1]$ by $d(f, g) = \int_0^1 |f(x) - g(x)|^{1/2} \, \mathrm{d}x$. The topology $L^{1/2}[0, 1]$ has from this metric is *not* locally convex. To see why, fix an open ball around $0$:

$$B_R = \left\{f \in L^{1/2}[0, 1] : \int_0^1 |f(x)|^{1/2} \, \mathrm{d}x < R\right\} \tag{2.1}$$

<!-- page 4 -->

where $R > 0$. We will show there is no convex open set around $0$ in $B_R$, which violates the meaning of local convexity.

Suppose there were a convex open set $C$ around $0$ contained in $B_R$, so the open $\varepsilon$-ball around $0$ is contained in $C$ for some $\varepsilon > 0$. For $n \ge 1$, select $n$ disjoint intervals in $[0, 1]$ (they need not cover all of $[0, 1]$). Call them $A_1, A_2, \ldots, A_n$. Set $f_k = \left(\frac{\varepsilon}{2\mu(A_k)}\right)^2 \chi_{A_k}$, where $\mu$ is Lebesgue measure (so $\mu(A_k)$ is simply the length of $A_k$). Then $\int_0^1 |f_k(x)|^{1/2} \, \mathrm{d}x = \varepsilon/2$, so every $f_k$ is in the open $\varepsilon$-ball around $0$ and thus is in $C$. Since the $f_k$'s are supported on disjoint intervals in $[0, 1]$, their average $g_n = (1/n)\sum_{k=1}^n f_k$ satisfies

$$\int_0^1 |g_n(x)|^{1/2} \, \mathrm{d}x = \frac{1}{n^{1/2}} \sum_{k=1}^n \int_0^1 |f_k(x)|^{1/2} \, \mathrm{d}x = \frac{1}{n^{1/2}} n \frac{\varepsilon}{2} = \frac{n^{1/2}\varepsilon}{2}.$$

We can pick $n$ large enough that $n^{1/2}\varepsilon/2 > R$, which makes $g_n$ lie outside $B_R$, so $g_n \notin C$. That contradicts the convexity of $C$.

**Example 2.20.** For $0 < p < 1$, let $L^p[0, 1]$ be the set of all functions $f: [0, 1] \to \mathbf{R}$ that are measurable and satisfy $\int_0^1 |f(x)|^p \, \mathrm{d}x < \infty$, with functions equal almost everywhere identified. We define a metric on $L^p[0, 1]$ by $d(f, g) = \int_0^1 |f(x) - g(x)|^p \, \mathrm{d}x$, and $L^p[0, 1]$ with the topology from this metric is not locally convex by exactly the same argument as in the previous example (where $p = 1/2$). Indeed, in that example replace the exponent $1/2$ in the definition of $f_k$ with $p$, and at the end you'll get $\int_0^1 |g_n(x)|^p \, \mathrm{d}x = n^{1-p}\varepsilon/2$. This can be made arbitrarily large by using large enough $n$, since $1 - p > 0$, no open ball around $0$ in $L^p[0, 1]$ contains a convex open set around $0$.

This method of constructing topological vector spaces that are not locally convex is due to Tychonoff [11, pp. 768--769]. He used the space $\ell^{1/2} = \{(x_i) : \sum_{i \ge 1} \sqrt{x_i} < \infty\}$ rather than the function space $L^{1/2}[0, 1]$.

One can't push a result like Theorem 2.18 to all topological vector spaces, as the next result [4, Theorem 1] vividly illustrates.

**Theorem 2.21.** *For $0 < p < 1$, $L^p[0, 1]^* = \{0\}$. That is, the only continuous linear map $L^p[0, 1] \to \mathbf{R}$ is $0$.*

*Proof.* We argue by contradiction. Assume there is $\varphi \in L^p[0, 1]^*$ with $\varphi \ne 0$. Then $\varphi$ has image $\mathbf{R}$ (a nonzero linear map to a one-dimensional space is surjective), so there is some $f \in L^p[0, 1]$ such that $|\varphi(f)| \ge 1$.

Using this choice of $f$, map $[0, 1]$ to $\mathbf{R}$ by

$$s \mapsto \int_0^s |f(x)|^p \, \mathrm{d}x.$$

This is continuous, so there is some $s$ between $0$ and $1$ such that

$$\int_0^s |f(x)|^p \, \mathrm{d}x = \frac{1}{2} \int_0^1 |f(x)|^p \, \mathrm{d}x > 0. \tag{2.2}$$

Let $g_1 = f\chi_{[0,s]}$ and $g_2 = f\chi_{(s,1]}$, so $f = g_1 + g_2$ and $|f|^p = |g_1|^p + |g_2|^p$. So

$$\int_0^1 |g_1(x)|^p \, \mathrm{d}x = \int_0^s |f(x)|^p \, \mathrm{d}x = \frac{1}{2} \int_0^1 |f(x)|^p \, \mathrm{d}x,$$

<!-- page 5 -->

hence $\int_0^1 |g_2(x)|^p \, \mathrm{d}x = \frac{1}{2} \int_0^1 |f(x)|^p \, \mathrm{d}x$. Since $|\varphi(f)| \ge 1$, $|\varphi(g_i)| \ge 1/2$ for some $i$. Let $f_1 = 2g_i$, so $|\varphi(f_1)| \ge 1$ and $\int_0^1 |f_1(x)|^p \, \mathrm{d}x = 2^p \int_0^1 |g_i(x)|^p \, \mathrm{d}x = 2^{p-1} \int_0^1 |f(x)|^p \, \mathrm{d}x$. Note $2^{p-1} < 1$ since $p < 1$.

Iterate this to get a sequence $\{f_n\}$ in $L^p[0, 1]$ such that $|\varphi(f_n)| \ge 1$ and

$$d(f_n, 0) = \int_0^1 |f_n(x)|^p \, \mathrm{d}x = (2^{p-1})^n \int_0^1 |f(x)|^p \, \mathrm{d}x \to 0,$$

which contradicts the continuity of $\varphi$. $\square$

## 3. More Spaces with Dual Space $0$

We recall the definition of $L^p$-spaces for a measure space and then extend Theorem 2.21 quite generally.

**Definition 3.1.** Let $(X, \mathcal{M}, \mu)$ be a measure space. For $p > 0$, set

$$L^p(\mu) \stackrel{\mathrm{def}}{=} \left\{f: X \to \mathbf{R} : f \text{ measurable and } \int_X |f|^p \, \mathrm{d}\mu < \infty\right\},$$

with functions that are equal almost everywhere being identified with one another.

The metric used on $L^p(\mu)$ is

$$d(f, g) = \begin{cases} \left(\int_X |f - g|^p \, \mathrm{d}\mu\right)^{1/p}, & \text{if } p \ge 1, \\ \int_X |f - g|^p \, \mathrm{d}\mu, & \text{if } 0 < p < 1. \end{cases}$$

The reason for these choices, and a discussion of common properties of $L^p(\mu)$ for all $p > 0$, is discussed in the appendix.

The spaces $L^p(\mu)$ for $p \ge 1$ have their metric coming from a norm, so they are locally convex. We saw in Examples 2.19 and 2.20 that, for $0 < p < 1$, $L^p[0, 1]$ is not locally convex. For a measure space $(X, \mathcal{M}, \mu)$ and $0 < p < 1$, is $L^p(\mu)$ ever locally convex?

**Theorem 3.2.** *For $0 < p < 1$, $L^p(\mu)$ is locally convex if and only if the measure $\mu$ assumes finitely many values.*

*Proof.* If $\mu$ takes finitely many values, then $X$ is the disjoint union of finitely many atoms, say $B_1, \ldots, B_m$. A measurable function is constant almost everywhere on each atom, so $L^p(\mu)$ is topologically just Euclidean space (of dimension equal to the number of atoms of finite measure), which is locally convex.

Now assume $\mu$ takes infinitely many values. We will extend the idea from Example 2.19 to show $L^p(\mu)$ is not locally convex.

Since $\mu$ has infinitely many values, there is a sequence of subsets $Y_i \subset X$ such that

$$0 < \mu(Y_1) < \mu(Y_2) < \cdots.$$

From the sets $Y_i$, we can construct recursively a sequences of disjoint sets $A_i$ such that $\mu(A_i) > 0$.

Fix $\varepsilon > 0$. Let $f_k = (\varepsilon/\mu(A_k))^{1/p} \chi_{A_k}$, so $\int_X |f_k|^p \, \mathrm{d}\mu = \varepsilon$. If $L^p(\mu)$ is locally convex, then every open set around $0$ contains a convex open set around $0$, which in turn contains some $\varepsilon$-ball (and thus every $f_k$). We will show an average of enough $f_k$'s is arbitrarily far from $0$ in the metric on $L^p(\mu)$, and that will contradict local convexity.

Let $g_n = \frac{1}{n} \sum_{k=1}^n f_k$. Since the $f_k$'s are supported on disjoint sets, $\int_X |g_n|^p \, \mathrm{d}\mu = \frac{1}{n^p} \sum_{k=1}^n \varepsilon = \varepsilon n^{1-p}$. Since $p < 1$, $\varepsilon n^{1-p}$ becomes arbitrarily large as $n \to \infty$. Thus, $L^p(\mu)$ is not locally convex. $\square$

<!-- page 6 -->

In Theorem 2.21, we saw $L^p[0, 1]^* = \{0\}$. Is the dual of $L^p(\mu)$, for general measure spaces and $0 < p < 1$, also $\{0\}$ (when $L^p(\mu)$ is not locally convex)?

First we treat the boring case.

**Theorem 3.3.** *If the measure $\mu$ contains an atom with finite measure, then $L^p(\mu)^* \ne \{0\}$.*

*Proof.* Let $B$ be an atom with finite measure. Every measurable function $f: X \to \mathbf{R}$ is constant almost everywhere on $B$. Call the almost-everywhere common value $\varphi(f)$. The reader can check $\varphi$ is a non-zero continuous linear functional on $L^p(\mu)$. $\square$

**Example 3.4.** For $0 < p < 1$ the sequence space $\ell^p = L^p(\mathbf{N})$, where $\mathbf{N}$ has counting measure, is not locally convex by Theorem 3.2 and has nonzero dual space by Theorem 3.3. In fact $(\ell^p)^*$ is $\ell^\infty$, where a sequence $\mathbf{y} \in \ell^\infty$ acts on $\ell^p$ by $\varphi_\mathbf{y}(\mathbf{x}) = \sum_{n \ge 1} x_n y_n$: for a proof, see [4, Theorem 6] or https://math.stackexchange.com/questions/1258557/.

Atoms with infinite measure are invisible as far as integration is concerned (integrable functions must vanish on them), so we may assume our measure space has no atoms of infinite measure.

What remains is the case of a nonatomic measure, and Theorem 2.21 generalizes to this case as follows.

**Theorem 3.5.** *If $(X, \mathcal{M}, \mu)$ is a nonatomic measure space and $0 < p < 1$, then $L^p(\mu)^* = 0$.*

Let's try to prove Theorem 3.5 by understanding more conceptually the proof that $L^p[0, 1]^* = 0$. To make that proof work in the setting of Theorem 3.5, suppose there is a non-zero $\varphi \in L^p(\mu)^*$. Then, by scaling, there is an $f \in L^p(\mu)$ such that $|\varphi(f)| \ge 1$. We'd it like to find some $A \in \mathcal{M}$ such that

$$\int_A |f|^p \, \mathrm{d}\mu = \frac{1}{2} \int_X |f|^p \, \mathrm{d}\mu. \tag{3.1}$$

Then set $g_1 = f\chi_A$ and $g_2 = f\chi_{X - A}$, and repeating the ideas of the proof of Theorem 2.21 will eventually yield a contradiction, so $L^p(\mu)^* = 0$.

But how do we construct $A$ (depending on $f$) that makes (3.1) correct? When $X = [0, 1]$, as in Theorem 2.21, we considered the collection of integrals

$$\int_0^s |f|^p \, \mathrm{d}x$$

as $s$ runs from $0$ to $1$. These are integrals over the sets $[0, s]$, which can be thought of as a "path" of intervals in the space of measurable subsets of $[0, 1]$, starting with $\{0\}$ and ending with the whole space $[0, 1]$. The Intermediate Value Theorem helped us find an $s$ such that $\int_0^s |f|^p \, \mathrm{d}x = (1/2) \int_0^1 |f|^p \, \mathrm{d}x$.

To extend this idea to a measure space $(X, \mathcal{M}, \mu)$ in place of $[0, 1]$, note $\mathcal{M}$ can topologized by the semi-metric $d_\mu(A, B) = \mu(A \Delta B)$, where $\Delta$ is the symmetric difference operation:

$$A \Delta B = A \cup B - A \cap B \tag{3.2}$$

(For instance, $d_\mu(A, \emptyset) = \mu(A)$.) With this metric, integration over measurable subsets of $X$ defines a function $\mathcal{M} \to \mathbf{R}$ by

$$\nu_f(A) = \int_A |f|^p \, \mathrm{d}\mu, \tag{3.3}$$

that is *continuous*.

<!-- page 7 -->

For each $f \in L^p(\mu)$, suppose we can find a path (continuous function) $h: [0, 1] \to \mathcal{M}$, depending on $f$, such that

$$\int_{h(0)} |f|^p \, \mathrm{d}\mu = 0, \quad \int_{h(1)} |f|^p \, \mathrm{d}\mu = \int_X |f|^p \, \mathrm{d}\mu. \tag{3.4}$$

Then composing $h$ with $\nu_f$ gives the function

$$s \mapsto \int_{h(s)} |f|^p \, \mathrm{d}\mu,$$

which is continuous from $[0, 1]$ to $\mathbf{R}$. We can apply the Intermediate Value Theorem to this continuous function of $s$ and thus find an $s$ such that $\int_{h(s)} |f|^p \, \mathrm{d}\mu = (1/2) \int_X |f|^p \, \mathrm{d}\mu$.

However, we haven't explained how to construct a path in $\mathcal{M}$ satisfying (3.4). It is not clear (to me) how to define such a path in $\mathcal{M}$ in general. We will use another approach, but will return to this path idea at the end of the paper.

The key step to finish this proof of Theorem 3.5 is to reformulate the problem more directly in terms of pure measure theory.

## 4. Values of a Measure

We start with a nonatomic measure space $(X, \mathcal{M}, \mu)$, and $p \in (0, 1)$. For each $f \in L^p(\mu)$, the map $\nu_f: \mathcal{M} \to \mathbf{R}$ given by (3.3) defines a finite measure on $X$ (even if $\mu(X) = \infty$). We want to find an $A \in \mathcal{M}$ such that $\nu_f(A) = (1/2)\nu_f(X)$, *i.e.*, $A$ cuts $X$ in half as far as $\nu_f$ is concerned.

Notice that $\nu_f$ depends not so much on $f$, but on $|f|^p$, and this is a function in $L^1(\mu, \mathbf{R})$.

**Lemma 4.1.** *If $(X, \mathcal{M}, \mu)$ is a nonatomic measure space, then for nonnegative $F \in \mathcal{L}^1(\mu, \mathbf{R})$, $F \, \mathrm{d}\mu$ is a finite nonatomic measure.*

*Proof.* Without loss of generality, $\int_X F \, \mathrm{d}\mu > 0$. Since $F$ is measurable,

$$\int_X F \, \mathrm{d}\mu = \sup_{0 \le g \le F} \int_X g \, \mathrm{d}\mu,$$

where the sup is over simple $g$. For $0 \le g \le F$, $g$ is a step map, say

$$g = \sum \alpha_i \chi_{A_i}$$

with $\alpha_i \ge 0$ and $0 < \mu(A_i) < \infty$.

Assume $F \, \mathrm{d}\mu$ has an atom $A$, so $\varepsilon = \int_A F \, \mathrm{d}\mu > 0$ and for $B \subset A$, $\int_B F \, \mathrm{d}\mu = 0$ or $\varepsilon$. Our goal is to get the contradiction $\int_A F \, \mathrm{d}\mu = 0$. Since $A$ is an atom for $F\chi_A$, without loss of generality $F = 0$ off of $A$, so $A_i \subset A$ for all $i$. The continuity of integration as a function of the set implies

$$\lim_{\mu(B) \to 0} \int_B F \, \mathrm{d}\mu = 0.$$

Since $\mu$ is nonatomic and $0 < \mu(A_i) < \infty$, $A_i$ contains a subset $B$ with arbitrarily small *positive* measure. For such $B$, $\int_B F \, \mathrm{d}\mu = 0$ since $B \subset A_i \subset A$. Therefore $\int_B g \, \mathrm{d}\mu = 0$, so $g = 0$ almost everywhere on $B$, so $\alpha_i = 0$ since $\mu(B) > 0$. This is true for all $i$, so $g = 0$. Thus $\int_X F \, \mathrm{d}\mu = 0$, so $\int_A F \, \mathrm{d}\mu = 0$, a contradiction. $\square$

Thus, for $f \in L^p(\mu)$, the measure $\nu_f$ in (3.3) is a finite nonatomic measure on $X$.

<!-- page 8 -->

**Theorem 4.2.** *If $(X, \mathcal{M}, \nu)$ is a finite nonatomic measure space, then for all $t$ in $[0, \nu(X)]$ there is some $A \in \mathcal{M}$ such that $\nu(A) = t$.*

Before proving Theorem 4.2, we note that Lemma 4.1 and Theorem 4.2 help us fill in the hole in our proof of Theorem 3.5. Indeed, when $(X, \mathcal{M}, \mu)$ is nonatomic and $f \in L^p(\mu, \mathbf{R})$, Lemma 4.1 tells us $|f|^p \, \mathrm{d}\mu$ is a finite nonatomic measure on $X$, and Theorem 4.2 then tells us there is an $A \in \mathcal{M}$ such that $\int_A |f|^p \, \mathrm{d}\mu = \frac{1}{2} \int_X |f|^p \, \mathrm{d}\mu$. Using this result and iteration, we can show $L^p(\mu)^* = 0$ for $0 < p < 1$ by the ideas in the proof of Theorem 2.21.

**Remark 4.3.** There are theorems that say a finite nonatomic measure space $(X, \mathcal{M}, \nu)$ often looks like the Borel measurable subsets of $[0, \nu(X)]$ with Lebesgue measure. Then the element of $\mathcal{M}$ corresponding to $[0, t]$ solves Theorem 4.2. However, such theorems need $X$ or $\mathcal{M}$ to be suitable separable metric spaces. For our purposes, we do not need such hypotheses, since all we are asking about is the set of values of the measure $\nu$, not the structure of $X$ or $\mathcal{M}$.

The proof of Theorem 4.2 we now give is taken from [9, Exercise 18-28, p. 247].

*Proof.* Let $S_1 = \{A \in \mathcal{M} : \nu(A) < t\}$. Choose $A_1 \in S_1$ such that $\nu(A_1) > \sup\{\nu(A) : A \in S_1\} - 1$.

Let $S_2 = \{A \in \mathcal{M} : \nu(A) < t, A_1 \subset A\}$. Choose $A_2 \in S_2$ such that $\nu(A_2) > \sup\{\nu(A) : A \in S_2\} - 1/2$.

Assuming $S_n$ is defined, choose $A_n \in S_n$ such that

$$\nu(A_n) > \sup\{\nu(A) : A \in S_n\} - 1/n.$$

Then let $S_{n+1} = \{A \in \mathcal{M} : \nu(A) < t, A_n \subset A\}$.

Now we have $A_1 \subset A_2 \subset A_3 \subset \cdots \subset X$. Define

$$A_\infty = \cup A_n \in \mathcal{M},$$

so

$$\nu(A_\infty) = \lim \nu(A_n) \le t. \tag{4.1}$$

The rest of the proof is devoted to showing $\nu(A_\infty) = t$.

If $A_\infty \subset A$ and $\nu(A) < t$, then $A \in S_{n+1}$. Thus $\nu(A_{n+1}) > \nu(A) - 1/(n + 1)$, so $\nu(A_\infty) \ge \nu(A)$, so $\nu(A) = \nu(A_\infty)$. We have shown $\nu(A_\infty) \le t$ and a measurable set containing $A_\infty$ has measure $\nu(A_\infty)$ if its measure is less than $t$.

Having constructed $A_\infty$ by a recursion from below, we now approach $A_\infty$ by a recursion from above. Let $T_1 = \{B \in \mathcal{M} : \nu(B) > t, A_\infty \subset B\}$. (For instance, $X \in T_1$.) Choose $B_1 \in T_1$ such that

$$\nu(B_1) < \inf\{\nu(B) : B \in T_1\} + 1.$$

Let $T_2 = \{B \in \mathcal{M} : \nu(B) > t, A_\infty \subset B \subset B_1\}$. If $T_n$ is defined, choose $B_n \in T_n$ such that

$$\nu(B_n) < \inf\{\nu(B) : B \in T_n\} + 1/n.$$

Let $T_{n+1} = \{B \in \mathcal{M} : \nu(B) > t, A_\infty \subset B \subset B_n\}$. Repeat this for all $n$, so

$$A_\infty \subset \cdots \subset B_3 \subset B_2 \subset B_1.$$

Let $B_\infty = \cap B_n \in \mathcal{M}$, so

$$\nu(B_\infty) = \lim \nu(B_n) \ge t. \tag{4.2}$$

If $A_\infty \subset B \subset B_\infty$ and $\nu(B) > t$, then $B \in T_{n+1}$, so

$$\nu(B_{n+1}) < \nu(B) + 1/(n + 1),$$

<!-- page 9 -->

so $\nu(B_\infty) \le \nu(B)$, so $\nu(B) = \nu(B_\infty)$.

Putting together what we have found for sets between $A_\infty$ and $B_\infty$,

$$A_\infty \subset A, \nu(A) < t \implies \nu(A) = \nu(A_\infty),$$

$$A_\infty \subset B \subset B_\infty, \nu(B) > t \implies \nu(B) = \nu(B_\infty).$$

We use this to show $\nu(B_\infty - A_\infty) = 0$, which implies $\nu(A_\infty) = t$ and will finish the proof. Notice we have yet to use the fact that $\nu$ is nonatomic.

Let $Y \subset B_\infty - A_\infty$, so

$$A_\infty \subset Y \cup A_\infty \subset B_\infty, \quad Y \cap A_\infty = \emptyset.$$

If $\nu(Y \cup A_\infty) < t$ then $\nu(Y \cup A_\infty) = \nu(A_\infty)$, so $\nu(Y) = 0$. If $\nu(Y \cup A_\infty) > t$ then $\nu(Y \cup A_\infty) = \nu(B_\infty)$, so $\nu(Y) = \nu(B_\infty - A_\infty)$. Thus, every measurable subset of $B_\infty - A_\infty$ has measure $0$, $\nu(B_\infty - A_\infty)$, or $t - \nu(A_\infty)$. Since $\nu$ is nonatomic, we conclude that $\nu(B_\infty - A_\infty) = 0$. $\square$

For an alternate proof of Theorem 4.2, see [5, Lemma 2]. For an extension of Theorem 4.2 to vector-valued measures, see [6].

This completes a proof that, for $0 < p < 1$, $L^p$-spaces of a nonatomic measure space have zero dual space. The machinery of functional analysis is built on the Hahn-Banach Theorem, so how can we study these kinds of $L^p$-spaces, or more generally a topological vector space that is not locally convex? See [1].

## 5. Theorem 4.2 Using Convexity

We now give a second proof of Theorem 4.2 (which will give a second proof that $L^p(\mu)^* = \{0\}$ when $\mu$ is nonatomic) based on an abstract convexity property for the measurable subsets of a finite nonatomic measure space. The idea we use is briefly indicated in [7, Exercise 41.2, p. 174].

Start with a finite measure space $(\mathcal{M}, \nu)$. (For instance, $(\mathcal{M}, \mu)$ is a measure space and $\nu = F \, \mathrm{d}\mu$ for some nonnegative $F \in L^1(\mu)$.) A metric can be introduced on $(\mathcal{M}, \nu)$ by

$$d_\nu(A, B) = \nu(A \Delta B),$$

where $\Delta$ is the symmetric difference (see (3.2)). Here it is crucial that $\nu$ is a finite measure, or this metric is not always defined. Actually, $d_\nu$ is only a semimetric, so we look at $\overline{\mathcal{M}}$, the metric space coming from $\mathcal{M}$ after elements at distance zero from one another are identified.

**Step 1:** The space $\overline{\mathcal{M}}$ is complete.

Let $\{A_n\}$ be $d_\nu$-Cauchy sequence. Then (in fact, equivalently) $\{\chi_{A_n}\}$ is an $L^1$-Cauchy sequence in $L^1(\nu)$. Let $f$ be an $L^1$-limit of this sequence of characteristic functions. A subsequence converges pointwise almost everywhere to $f$, so the set $\{x : f(x) = 1\}$ is a limit of $\{A_n\}$ in $\overline{\mathcal{M}}$.

**Step 2:** Call a metric space $(M, \rho)$ *convex* if for all $x \ne y$ in $X$ there is some $z \ne x, y$ in $M$ such that $\rho(x, y) = \rho(x, z) + \rho(z, y)$. Note such a $z$ need not be uniquely determined by the two distances $\rho(x, z)$ and $\rho(z, y)$. For example, take $M = S^2$ with its surface metric, $x$ the north pole, $y$ the south pole, and $z$ an arbitrary point along a chosen latitude of $M$. (When $M \subset \mathbf{R}^n$, this definition of convex might not match the usual notion: an *open* star-shaped region in $\mathbf{R}^n$ is not convex in the usual sense but is convex in the abstract sense above. However, for closed subsets of $\mathbf{R}^n$ using the induced metric from $\mathbf{R}^n$, the above notion of convex does match the usual meaning of the term.)

We show that $(\overline{\mathcal{M}}, d_\nu)$ is convex if (and only if!) $\nu$ is nonatomic.

<!-- page 10 -->

If $\overline{\mathcal{M}}$ is convex and $\nu(A) > 0$, so $d_\nu(A, \emptyset) > 0$, then there exists a $C$ such that $d_\nu(A, C) > 0$, $d_\nu(C, \emptyset) > 0$, and $d_\nu(A, \emptyset) = d_\nu(A, C) + d_\nu(C, \emptyset)$. That is

$$\nu(A \Delta C) > 0, \nu(C) > 0, \nu(A) = \nu(A \Delta C) + \nu(C).$$

Therefore $\nu(A \Delta C) = \nu(A) - \nu(C) > 0$, so $\nu(C - A) = 0$, so $\nu(C) = \nu(A \cap C)$. This implies $0 < \nu(A \cap C) < \nu(A)$. Since $A \cap C \subset A$, this shows $\nu$ is nonatomic.

Conversely, if $d_\nu(A, B) > 0$, we want to find $C$ such that $d_\nu(A, C)$ and $d_\nu(C, B)$ are both positive and

$$d_\nu(A, B) = d_\nu(A, C) + d_\nu(B, C),$$

that is

$$\nu(A \Delta B) = \nu(A \Delta C) + \nu(B \Delta C).$$

If $\nu(A)$ or $\nu(B)$ is less than or equal to $\nu(A \cap B)$ (so $A \subset B$ or $B \subset A$ up to measure zero), say $\nu(A) \le \nu(A \cap B)$. Then $\nu(A) = \nu(A \cap B)$ and $\nu(B) = \nu(A \cup B)$, so $\nu(A \Delta B) = \nu(B) - \nu(A) > 0$.

Choose $Y \subset B - A$ such that $0 < \nu(Y) < \nu(B) - \nu(A)$ and let $C = Y \cup (A \cap B)$. Then

$$\nu(A \Delta C) = \nu(A) - \nu(A \cap B) + \nu(Y) = \nu(Y) > 0,$$

$$\nu(B \Delta C) = \nu(B) - \nu(A \cap B) - \nu(Y) = \nu(B) - \nu(A) - \nu(Y) > 0,$$

so

$$\nu(A \Delta C) + \nu(B \Delta C) = \nu(B) - \nu(A) = \nu(A \Delta B).$$

If $\nu(A), \nu(B) > \nu(A \cap B)$, let $C_1 \subset A - A \cap B$ and $C_2 \subset B - A \cap B$ such that

$$0 < \nu(C_1) < \nu(A) - \nu(A \cap B), \quad 0 < \nu(C_2) < \nu(B) - \nu(A \cap B).$$

Set $C = C_1 \cup C_2 \cup (A \cap B)$. Then

$$A \Delta C = (A - C_1 - A \cap B) \cup (B \cap C_2), \quad B \Delta C = (B - C_2 - A \cap B) \cup (A \cap C_1),$$

so

$$\nu(A \Delta C) = \nu(A) - \nu(C_1) - \nu(A \cap B) + \nu(C_2) > \nu(C_2) > 0,$$

$$\nu(B \Delta C) = \nu(B) - \nu(C_2) - \nu(A \cap B) + \nu(C_1) > \nu(C_1) > 0,$$

so

$$\nu(A \Delta C) + \nu(B \Delta C) = \nu(A \cup B) - \nu(A \cap B) = \nu(A \Delta B).$$

**Step 3:** The final step will actually be a generalization of Theorem 4.2 to metric spaces. The application to $(\overline{\mathcal{M}}, d_\nu)$ for nonatomic $\nu$ will come by setting $x = \emptyset$ and $y = X$ in the next claim.

*Claim:* For a complete convex metric space $(M, \rho)$ and distinct points $x$ and $y$ in $M$ with $0 \le t \le \rho(x, y)$, there is a $z$ such that $\rho(x, z) = t$ (and $\rho(x, y) = \rho(x, z) + \rho(z, y)$).

The proof of this claim will be a tortuous Zornification.

First we define some notation. For $a, b \in M$, let

$$[a, b] \stackrel{\mathrm{def}}{=} \{c \in M : \rho(a, b) = \rho(a, c) + \rho(c, b)\}.$$

For instance, this set contains $a$ and $b$. Intuitively, this is the set of points lying on geodesics from $a$ to $b$. It is helpful when reading the following discussion to draw many pictures of line segments with points marked on them. Given $t$ between $0$ and $\rho(x, y)$, we will find a $z \in [x, y]$ with $\rho(x, z) = t$.

Some simple properties of these "intervals" are:

(1) $[a, b] = [b, a]$.

<!-- page 11 -->

(2) If $c \in [a, b]$ and $b \in [a, c]$, then $\rho(b, c) = -\rho(b, c)$, so $b = c$.

Less simple properties are

(3) If $b \in [a, c]$ then $[a, b], [b, c] \subset [a, c]$.

(4) If $b \in [a, d]$ and $c \in [b, d]$ then $[a, c], [b, d] \subset [a, d]$ and $[b, c] = [a, c] \cap [b, d] \subset [a, d]$.

(We will only need that $[b, c]$ lies in the intersection, not equality.)

Proof of (3): Without loss of generality, we show $[a, b] \subset [a, c]$. For $x$ in $[a, b]$,

$$\rho(a, c) \le \rho(a, x) + \rho(x, c) \le \rho(a, x) + \rho(x, b) + \rho(b, c) = \rho(a, b) + \rho(b, c) = \rho(a, c).$$

Therefore $x \in [a, c]$.

Proof of (4): By (3), $[b, d] \subset [a, d]$ and $[b, c] \subset [b, d]$. Therefore $c \in [a, d]$, so $[a, c] \subset [a, d]$, so

$$\rho(a, d) = \rho(a, c) + \rho(c, d) \le \rho(a, b) + \rho(b, c) + \rho(c, d) = \rho(a, b) + \rho(b, d) = \rho(a, d).$$

Therefore the inequality is an equality, so $b \in [a, c]$, so $[b, c] \subset [a, c]$. Thus $[b, c] \subset [a, c] \cap [b, d]$.

For the reverse inclusion, let $x \in [a, c] \cap [b, d]$. Then

$$\rho(a, d) = \rho(a, b) + \rho(b, d) = \rho(a, b) + \rho(b, c) + \rho(c, d) \le \rho(a, b) + \rho(b, x) + \rho(x, c) + \rho(c, d) = \rho(a, b) + \rho(b, d) - \rho(x, d) + \rho(a, c) - \rho(a, x) + \rho(c, d) = 2\rho(a, d) - \rho(x, d) - \rho(a, x).$$

Rearranging terms, $\rho(a, x) + \rho(x, d) \le \rho(a, d)$, so there is equality throughout, so $\rho(b, c) = \rho(b, x) + \rho(x, c)$. Thus $x \in [b, c]$.

Now we are ready to investigate "geodesics" on $M$. For our fixed $x \in M$ introduced in the statement of Step 3, define a partial ordering on $M$ that might be called "closer to $x$ on geodesics" by

$$z_1 \le z_2 \text{ if and only if } z_1 \in [x, z_2].$$

In particular, $z_1 \le z_2$ implies $\rho(x, z_1) \le \rho(x, z_2)$.

Let's check this is a partial ordering.

If $z_1 \le z_2$ and $z_2 \le z_1$, then $z_1 \in [x, z_2]$ and $z_2 \in [x, z_1]$, so $z_1 = z_2$ by (2).

If $z_1 \le z_2$ and $z_2 \le z_3$ then $z_1 \in [x, z_2]$ and $z_2 \in [x, z_3]$. By (1), $z_2 \in [z_3, x]$ and $z_1 \in [z_2, x]$. Therefore by (4),

$$z_1 \in [z_1, z_2] \subset [x, z_3],$$

hence $z_1 \le z_3$.

Define

$$A = \{z \in [x, y] : \rho(x, z) \le t\}.$$

<!-- page 12 -->

This set is nonempty, since it contains $x$. We want to apply Zorn's Lemma to $A$ with its induced partial ordering and show a maximal element of $A$ has distance $t$ from $x$.

Let $\{z_i\}_{i \in I}$ be a totally ordered subset of $A$. We want an upper bound. Let

$$s = \sup_{i \in I} \rho(x, z_i) \le t.$$

For $\varepsilon > 0$, there is some $i_0$ such that

$$s - \varepsilon \le \rho(x, z_{i_0}) \le s,$$

so

$$s - \varepsilon \le \rho(x, z_i) \le s$$

for all $i \ge i_0$. For $i_0 \le i \le j$, $s - \varepsilon \le \rho(x, z_i) \le s$ and

$$s - \varepsilon \le \rho(x, z_j) = \rho(x, z_i) + \rho(z_i, z_j) \le s$$

so $\rho(z_i, z_j) \le \varepsilon$. Thus $\{z_i\}$ is a Cauchy net, so has a limit $\ell$ by completeness of $M$. We show this limit is an upper bound in $A$.

Taking limits,

$$\rho(x, y) = \rho(x, z_i) + \rho(z_i, y) \implies \rho(x, y) = \rho(x, \ell) + \rho(\ell, y)$$

$$\rho(x, z_i) \le t \implies \rho(x, \ell) \le t.$$

Thus $\ell \in A$.

For $i \le j$,

$$\rho(x, z_j) = \rho(x, z_i) + \rho(z_i, z_j).$$

Taking limits over $j$,

$$\rho(x, \ell) = \rho(x, z_i) + \rho(z_i, \ell),$$

so $z_i \in [x, \ell]$, so $z_i \le \ell$ for all $i$.

We have justified an application of Zorn's Lemma to $A$. Let $m$ be a maximal element. That is, $m \in A$, and if $z \in A$ with $m \in [x, z]$ then $z = m$.

Let $B = \{z \in [y, m] : \rho(y, z) \le \rho(x, y) - t\}$. Since $y \in B$, $B$ is nonempty. Our goal is to show $m \in B$, which is *not* obvious. Note that the definition of $B$ depends on the existence of a maximal element of $A$.

In $B$, introduce a partial ordering by $z_1 \le z_2$ when $z_1 \in [y, z_2]$.

As above, $B$ has a maximal element, $m'$. Since $m \in [x, y]$ and $m' \in [m, y]$, we get by (4) that

$$[m, m'] \subset [x, m'] \cap [m, y] \subset [x, y].$$

For $z \in [m, m']$,

$$z \in [x, y] \implies \rho(x, y) = \rho(x, z) + \rho(y, z)$$

$$\implies \rho(x, z) \le t \text{ or } \rho(y, z) \le \rho(x, y) - t$$

$$\implies z \in A \text{ or } z \in B.$$

Also,

$$\rho(x, y) = \rho(x, z) + \rho(z, y) \le \rho(x, m) + \rho(m, z) + \rho(z, y) = \rho(x, m) + \rho(m, y) \text{ since } z \in [m, y] = \rho(x, y) \text{ since } m \in [x, y].$$

Therefore $\rho(x, z) = \rho(x, m) + \rho(m, z)$, so $m \in [x, z]$.

<!-- page 13 -->

We now have

$$\rho(x, y) = \rho(x, z) + \rho(z, y) \text{ since } z \in [x, y] \le \rho(x, z) + \rho(z, m') + \rho(m', y) = \rho(x, m') + \rho(m', y) \text{ since } z \in [x, m'] = \rho(x, y) \text{ since } m' \in [x, y].$$

Therefore $\rho(y, z) = \rho(z, m') + \rho(m', y)$, so $m' \in [y, z]$.

Thus if $z \in A$, then $m \in [x, z] \implies z = m$. If $z \in B$, then $m' \in [y, z] \implies z = m'$. Therefore $[m, m'] = \{m, m'\}$, so by *convexity* of $M$, $m = m'$, hence $m \in A \cap B$. Therefore $\rho(x, m) \le t$ and $\rho(y, m) \le \rho(x, y) - t$, so

$$\rho(x, y) = \rho(x, m) + \rho(m, y) \le \rho(x, y),$$

so $\rho(x, m) = t$. This concludes our second proof of Theorem 4.2.

## 6. Paths Linking Measurable Sets

Returning to the original idea of showing $L^p(\mu)$ has zero dual space (for nonatomic $\mu$) by finding a path in the space of measurable sets, the following possibility suggests itself. Let $(M, \rho)$ be a complete convex metric space. (Our second proof of Theorem 4.2 gives us the motivating example.) Is $M$ path connected? To try to show this, recall that we've seen that for distinct $x, y$ in $M$ and $0 \le t \le \rho(x, y)$, there is $z_t \in [x, y]$ such that $\rho(x, z_t) = t$. Perhaps if $\rho(x, y)$ is small enough, each $z_t$ is unique, and this would let us construct paths in $M$. For a proof that every complete convex metric space is path connected, see [2, Thm. 14.1, p. 41].

## Appendix A. Analogies Between $p \ge 1$ and $0 < p < 1$

In this appendix, we summarize common features of $L^p(\mu)$ for all $p > 0$.

Every $L^p(\mu)$ is a vector space. Closure under scaling is trivial. For closure under addition, first note that

$$|f(x) + g(x)| \le |f(x)| + |g(x)| \implies |f(x) + g(x)|^p \le (|f(x)| + |g(x)|)^p$$

since the $p$-th power is increasing on $[0, \infty)$ for all $p > 0$. Now we argue separately for $p \ge 1$ and $0 < p < 1$. When $p \ge 1$, non-negative numbers $a$ and $b$ satisfy

$$(a + b)^p \le 2^p a^p + 2^p b^p \tag{A.1}$$

since $a + b \le 2\max(a, b)$. Since $|f(x) + g(x)| \le |f(x)| + |g(x)|$,

$$|f(x) + g(x)|^p \le (|f(x)| + |g(x)|)^p \le 2^p |f(x)|^p + 2^p |g(x)|^p,$$

by (A.1), so $\int_X |f + g|^p \, \mathrm{d}\mu \le 2^p \int_X |f|^p \, \mathrm{d}\mu + 2^p \int_X |g|^p \, \mathrm{d}\mu < \infty$. When $0 < p < 1$ and $a$ and $b$ are non-negative numbers,

$$(a + b)^p \le a^p + b^p. \tag{A.2}$$

Again starting from $|f(x) + g(x)| \le |f(x)| + |g(x)|$,

$$|f(x) + g(x)|^p \le (|f(x)| + |g(x)|)^p \le |f(x)|^p + |g(x)|^p, \tag{A.3}$$

by (A.2), so

$$\int_X |f + g|^p \, \mathrm{d}\mu \le \int_X |f|^p \, \mathrm{d}\mu + \int_X |g|^p \, \mathrm{d}\mu < \infty. \tag{A.4}$$

<!-- page 14 -->

For all $p > 0$, set

$$|f|_p \stackrel{\mathrm{def}}{=} \left(\int_X |f|^p \, \mathrm{d}\mu\right)^{1/p}. \tag{A.5}$$

When $f = g$ almost everywhere, $|f|_p = |g|_p$, so $|\cdot|_p$ is well-defined on $L^p(\mu)$.

For $p \ge 1$, $|\cdot|_p$ on $L^p(\mu)$ satisfies the triangle inequality:

$$|f + g|_p \le |f|_p + |g|_p.$$

This is called the Minkowski inequality for $L^p$-functions. It shows $|\cdot|_p$ is a norm on $L^p(\mu)$.

When $0 < p < 1$, $|\cdot|_p$ in (A.5) has a flipped triangle inequality: $|f + g|_p \ge |f|_p + |g|_p$ when $f$ and $g$ have nonnegative values.[^4] For instance, when $X = [0, 1]$ with Lebesgue measure and $p = 1/2$, $f = \chi_{[0, 1/2)}$, and $g = \chi_{[1/2, 1]}$, we have $|f + g|_p = 1$ and $|f|_p + |g|_p = 2^{1-1/p} < 1$. Taking $p$-th roots in the definition of $|\cdot|_p$ is the source of the problem.

For $0 < p < 1$, a modified triangle inequality on $L^p(\mu)$ in the correct direction is

$$|f + g|_p \le 2^{\frac{1}{p} - 1}(|f|_p + |g|_p). \tag{A.6}$$

To prove (A.6), we follow [8, §15.9]. For $c > 1$, the function $(t^c + 1)/(t + 1)^c$ for $t \ge 0$ has a unique minimum at $t = 1$ (it decreases for $t$ in $[0, 1]$ and increases for $t$ in $[1, \infty)$). Therefore $(t^c + 1)/(t + 1)^c \ge 2^{1-c}$, so $t^c + 1 \ge 2^{1-c}(t + 1)^c$. Writing $t = a/b$ for $a \ge 0$ and $b > 0$ and multiplying through by $b^c$,

$$a^c + b^c \ge 2^{1-c}(a + b)^c, \text{ so } (a + b)^c \le 2^{c-1}(a^c + b^c). \tag{A.7}$$

This is obviously also true when $b = 0$. In (A.7), let $c = 1/p$ for $0 < p < 1$, $a = \int_X |f|^p \, \mathrm{d}\mu$, and $b = \int_X |g|^p \, \mathrm{d}\mu$:

$$\left(\int_X |f|^p \, \mathrm{d}\mu + \int_X |g|^p \, \mathrm{d}\mu\right)^{1/p} \le 2^{\frac{1}{p} - 1}(|f|_p + |g|_p).$$

Combining this with (A.4), after taking the $p$-th root of both sides of (A.4), we get (A.6).

Having the triangle inequality up to a universal scaling factor, as in (A.6), is often harmless. Alternatively, we could use $\int_X |f|^p \, \mathrm{d}\mu$ as a notion of distance from $0$, without the $p$-th root of the integral, since (A.4) shows the triangle inequality is valid for this. This is the choice that we made earlier. For $0 < p < 1$, set the metric on $L^p(\mu)$ to be

$$d(f, g) = \int_X |f - g|^p \, \mathrm{d}\mu.$$

Whether or not we take the $p$-th root of $\int_X |f - g|^p \, \mathrm{d}\mu$ will not change the notion of convergence on $L^p(\mu)$, but at least without the $p$-th root we get the standard triangle inequality.

Some properties of the spaces $L^p(\mu)$ for $p \ge 1$ are

- A sequence of measurable functions that is $L^p$-convergent has a subsequence that converges pointwise almost everywhere.
- $L^p(\mu)$ is complete with respect to $|\cdot|_p$, and thus is a Banach space,
- (Hölder's inequality) If $p > 1$, and $q > 1$ is chosen so that $1/p + 1/q = 1$, then for $f \in L^p(\mu)$ and $g \in L^q(\mu)$, the product $fg$ lies in $L^1(\mu)$ and $|fg|_1 \le |f|_p |g|_q$.
- If $f_n \to f$ in $L^p(\mu)$, then $|f_n|^p \to |f|^p$ in $L^1(\mu)$.

[^4]: Some constraint on the values of $f$ and $g$ are needed here, since otherwise take $g = -f$ to get $0 \ge |f|_p + |g|_p$, for $f = g = 0$ in $L^p(\mu)$.

<!-- page 15 -->

- When $X$ is a locally compact Hausdorff space, and $\mu$ is a regular Borel measure on $X$, the space $C_c(X)$ (continuous real-valued functions on $X$ with compact support) is dense in $L^p(\mu)$.

Since $a \mapsto a^p$ is an increasing function on $[0, \infty)$ for $p > 0$, not just for $p \ge 1$, some results about $L^p$-spaces when $p \ge 1$ work for $0 < p < 1$. Here are some examples.

- For $0 < p < 1$, a sequence of measurable functions that is $L^p$-convergent has a subsequence that converges pointwise almost everywhere.
- For $0 < p < 1$, $L^p(\mu)$ is complete.
- If $0 < p < 1$ and $f_n \to f$ in $L^p(\mu)$, then $|f_n|^p \to |f|^p$ in $L^1(\mu)$.
- When $X$ is a locally compact Hausdorff space, and $\mu$ is a regular Borel measure on $X$, the space $C_c(X)$ (continuous real-valued functions on $X$ with compact support) is dense in $L^p(\mu)$ for $0 < p < 1$.

Actually, the third item needs a different proof in the case $0 < p < 1$. (The usual proof when $p > 1$ uses Hölder's inequality, which breaks down for $0 < p < 1$.) Here is the proof. For $0 < p < 1$,

$$|f|^p \le |f - f_n|^p + |f_n|^p, \quad |f_n|^p \le |f - f_n|^p + |f|^p,$$

so

$$\big||f|^p - |f_n|^p\big| \le |f - f_n|^p.$$

Thus

$$\int_X \big||f|^p - |f_n|^p\big| \, \mathrm{d}\mu \le \int_X |f - f_n|^p \, \mathrm{d}\mu \to 0.$$

Since, for $0 < p < 1$, $L^p(\mu)$ is a topological vector space complete with respect to a metric, we have notions of continuity, completeness, and boundedness here. Therefore several consequences of the Baire category theorem as applied to Banach spaces carry over without change to $L^p(\mu)$ for $0 < p < 1$: the Open Mapping Theorem, the Closed Graph Theorem, and the Principle of Uniform Boundedness.

## References

[1] N. Adasch, B. Ernst, and D. Keim, *Topological Vector Spaces. The Theory Without Convexity Conditions*, Lecture Notes in Mathematics 639, Springer-Verlag, New York, 1978.

[2] L. Blumenthal, *Theory and Applications of Distance Geometry*, Clarendon Press, Oxford, 1953.

[3] J. B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer Verlag, New York, 1990.

[4] M. M. Day, "The spaces $L^p$ with $0 < p < 1$," *Bull. Amer. Math. Soc.* **46** (1940), 816--823. URL https://projecteuclid.org/download/pdf_1/euclid.bams/1183503236.

[5] P. R. Halmos, "On the Set of Values of a Finite Measure," *Bull. Amer. Math. Soc.* **53** (1947), 138-141.

[6] P. R. Halmos, "The Range of a Vector Measure," *Bull. Amer. Math. Soc.* **54** (1948), 416-421.

[7] P. R. Halmos, *Measure Theory*, Van Nostrand, New York, 1950.

[8] G. Köthe, *Topological Vector Spaces I*, Springer-Verlag, New York, 1969.

[9] W. Pfeffer, *Integrals and Measures*, Marcel Dekker, New York, 1977.

[10] M. Reed and B. Simon, *Functional Analysis I*, Academic Press, San Diego, 1980.

[11] A. Tychonoff, "Ein Fixpunktsatz," *Math. Ann.* **111** (1935), 767--776.
