# Spaces That Are Connected but Not Path-Connected

> **Source**: https://kconrad.math.uconn.edu/blurbs/connnotpathconn.pdf
> **Author**: Keith Conrad
> **Topic**: topology

<!-- page 1 -->

## 1. Introduction

A topological space $X$ is called *connected* if it's impossible to write $X$ as a union of two nonempty disjoint open subsets: if $X = U \cup V$ where $U$ and $V$ are open subsets of $X$ and $U \cap V = \emptyset$ then one of $U$ or $V$ is empty. Intuitively, this means $X$ consists of one piece. A subset of a topological space is called connected if it is connected in the subspace topology. The most fundamental example of a connected set is the interval $[0, 1]$, or more generally any closed or open interval in $\mathbf{R}$.

Most reasonable-looking spaces that appear to be connected can be proved to be connected using properties of connected sets like the following [2, pp. 149--151]:

- if $f \colon X \to Y$ is continuous and $X$ is connected then $f(X)$ is connected,
- if $C$ is a connected subset of $X$ then $\overline{C}$ is connected and every set between $C$ and $\overline{C}$ is connected,
- if $C_i$ are connected subsets of $X$ and $\bigcap_i C_i \neq \emptyset$ then $\bigcup_i C_i$ is connected,
- a direct product of connected sets is connected.

Proving complicated fractal-like sets are connected can be a hard theorem, such as connectedness of the Mandelbrot set [1].

We call a topological space $X$ *path-connected* if, for every pair of points $x$ and $x'$ in $X$, there is a path in $X$ from $x$ to $x'$: there's a continuous function $p \colon [0, 1] \to X$ such that $p(0) = x$ and $p(1) = x'$. Since $q(t) = p(1 - t)$ is also continuous with $q(0) = p(1) = x'$ and $q(1) = p(0) = x$, we can think of a path going in either direction, $x$ to $x'$ or $x'$ to $x$. A subset $Y \subset X$ is called path-connected if any two points in $Y$ can be linked by a path taking values entirely inside $Y$.

Path-connectedness shares some properties of connectedness:

- if $f \colon X \to Y$ is continuous and $X$ is path-connected then $f(X)$ is path-connected,
- if $C_i$ are path-connected subsets of $X$ and $\bigcap_i C_i \neq \emptyset$ then $\bigcup_i C_i$ is path-connected,
- a direct product of path-connected sets is path-connected.

Compared to the list of properties of connectedness, we see one analogue is missing: every set lying between a path-connected subset and its closure is path-connected. In fact that property is not true in general.

For reasonable-looking subsets of Euclidean space, connectedness and path-connectedness are the same thing: one property holds if and only if the other property does. But the properties are not always the same. We will set out here the precise logical connection (pun intended): path-connectedness implies connectedness, but the converse direction is false and we'll give three explicit examples of a connected set that is not path-connected. The first two will use objects you can find around your house: a broom and a comb. Well, not quite. The examples will be figures made up of carefully arranged line segments in the plane, together with one extra point, that are infinite versions of a broom and a comb. All three examples will be path-connected subsets together with one limit point, and including the limit point will wreck path-connectedness.

<!-- page 2 -->

## 2. Path-Connectedness Implies Connectedness

**Theorem 2.1.** *Every path-connected space is connected.*

*Proof.* Let $X$ be path-connected. We will use paths in $X$ to show that if $X$ is not connected then $[0, 1]$ is not connected, which of course is a contradiction, so $X$ has to be connected.

Suppose $X$ is not connected, so we can write $X = U \cup V$ where $U$ and $V$ are nonempty disjoint open subsets. Pick $x \in U$ and $y \in V$. There is a path $p \colon [0, 1] \to X$ where $p(0) = x$ and $p(1) = y$. The partition of $X$ into $U$ and $V$ leads via this path to a partition of $[0, 1]$: $[0, 1] = A \cup B$ where $A = p^{-1}(U)$ and $B = p^{-1}(V)$.

Note $0 \in A$ and $1 \in B$, so $A$ and $B$ are nonempty subsets of $[0, 1]$. Obviously $A$ and $B$ are disjoint, since no point in $[0, 1]$ can have its $p$-value in both $U$ and $V$. Since $p$ is continuous and $U$ and $V$ are both open in $X$, $A$ and $B$ are both open in $[0, 1]$. Thus the equation $[0, 1] = A \cup B$ exhibits $[0, 1]$ as a disjoint union of two nonempty open subsets, which contradicts the connectedness of $[0, 1]$. $\square$

**Remark 2.2.** A second proof of Theorem 2.1 is based on a property of connectedness listed earlier: if $C_i$ are connected subsets and $\bigcap_i C_i \neq \emptyset$, then $\bigcup_i C_i$ is a connected subset. If $X$ is path-connected and we fix a point $x \in X$ then for each $y \in X$ there's a path $p_y$ in $X$ from $x$ to $y$, so we can cover $X$ by the images of these paths: $X = \bigcup_{y \in X} p_y([0, 1])$. Each $p_y([0, 1])$ is connected since the image of a connected set under a continuous function is connected, and since $x = p_y(0)$ for all $y \in X$, the different subsets $p_y([0, 1])$ have a nonempty intersection. Thus $X$ is connected. B. Conrad noted that this proof can be condensed to a sentence: "All roads lead to Rome" (or equivalently, all roads lead from Rome).

<!-- page 3 -->

## 3. Connectedness Does Not Imply Path-Connectedness

Examples of connected sets that are not path-connected all look weird in some way. We will describe two examples that are subsets of $\mathbf{R}^2$. The first one is called the deleted infinite broom. It is pictured below and consists of the closed line segments $L_n$ from $(0, 0)$ to $(1, 1/n)$ as $n$ runs over the positive integers together with the (red) point $(1, 0)$. The $x$-axis strictly between $0$ and $1$ is not part of this.

![Deleted infinite broom](page_002.png)

**Theorem 3.1.** *The deleted infinite broom is connected.*

*Proof.* Each point on $L_n$ can be linked to $(0, 0)$ by a path along $L_n$. By concatenating such paths, points on $L_m$ and $L_n$ can be linked by a path via $(0, 0)$ if $m \neq n$, so the union $\bigcup_{n \geq 1} L_n$ is path-connected and therefore is connected (Theorem 2.1). The point $(1, 0)$ is a limit point of $\bigcup_{n \geq 1} L_n$, so the deleted infinite broom lies between $\bigcup_{n \geq 1} L_n$ and its closure in $\mathbf{R}^2$. Therefore by the second property of connectedness in the introduction, the deleted infinite broom is connected. $\square$

**Remark 3.2.** The closure of $\bigcup_{n \geq 1} L_n$ is obtained by adjoining to this union the segment $L_\infty$ from $(0, 0)$ to $(1, 0)$, and the closure is called the infinite broom, which is why the space we care about is called the deleted infinite broom. The infinite broom is path-connected.

It makes sense intuitively that the deleted infinite broom is not path-connected: if a path starts at $(1, 0)$ and stays within the deleted infinite broom it is hard to imagine how the path could "make the leap" to the rest of the space. In other words, you should have a feeling that any path in the deleted infinite broom that starts at $(1, 0)$ has to be constant.

To prove that path property, we will first look at the endpoints of the segments $L_n$ that lie on the line $x = 1$ together with $(1, 0)$. The line $x = 1$ is homeomorphic to the real line, and rotating it by 90 degrees makes those endpoints and $(1, 0)$ look like the figure below, which is the number $0$ and $1/n$ for all $n \in \mathbf{Z}^+$.

$$0 \quad \cdots \quad \frac{1}{4} \quad \frac{1}{3} \quad \frac{1}{2} \quad 1$$

**Lemma 3.3.** *The set $\{0\} \cup \{1/n : n \in \mathbf{Z}^+\}$ with its subspace topology in $\mathbf{R}$ has one-element subsets as its only nonempty connected subsets.*

*Proof.* Let $C$ be a nonempty connected subset of $\{0\} \cup \{1/n : n \in \mathbf{Z}^+\}$. Assume $C$ contains some $1/n$. Since $\{1/n\}$ is both closed and open in this set, writing $C = \{1/n\} \cup (C - \{1/n\})$ expresses $C$ as a union of disjoint open subsets, so one of the subsets is empty. Thus $C - \{1/n\}$ is empty, so $C = \{1/n\}$. If $C$ does not contain any $1/n$ then the only choice is $C = \{0\}$. $\square$

**Remark 3.4.** A topological space whose only nonempty connected subsets are one-element subsets is called *totally disconnected*, so the set in Lemma 3.3 is totally disconnected. Other examples include $\mathbf{Q}$ with its standard topology as a subset of $\mathbf{R}$, and $\prod_{n \geq 1} \{1, -1\}$ with the product topology.

Lemma 3.3 is the key technical idea for proving the deleted infinite broom is not path-connected.

**Theorem 3.5.** *The deleted infinite broom is not path-connected.*

*Proof.* Denote the deleted infinite broom as $B$ and let $p \colon [0, 1] \to B$ be a path such that $p(0) = (1, 0)$. We will prove $p(t) = (1, 0)$ for all $t \in [0, 1]$, so no path in $B$ links $(1, 0)$ to any other point of $B$.

Let
$$A = \{t \in [0, 1] : p(t) = (1, 0)\}.$$
This is a nonempty subset of $[0, 1]$ since it contains $0$. Our goal is to show $A = [0, 1]$.

The set $A$ is closed in $[0, 1]$ since it is $p^{-1}((1, 0))$ and $p$ is continuous.

<!-- page 4 -->

Next we show $A$ is open in $[0, 1]$. This will require a lot more work than showing it is closed. For $t_0 \in A$ we want to find an open interval around $t_0$ in $[0, 1]$ that is also in $A$. By continuity of $p$ at $t_0$ there's a $\delta > 0$ such that if $t \in [0, 1]$ satisfies $|t - t_0| < \delta$ then $\|p(t) - p(t_0)\| < 1/2$, where $\|\cdot\|$ is the length of a vector in $\mathbf{R}^2$.[^1] Then $p(t) \neq (0, 0)$ since $\|p(t_0)\| = \|(1, 0)\| = 1 > 1/2$, so $p(t)$ has a positive $x$-coordinate for all $t \in [0, 1]$ satisfying $|t - t_0| < \delta$.

Consider the slope function $m \colon \{(x, y) \in \mathbf{R}^2 : x > 0\} \to \mathbf{R}$ defined by $m(x, y) = y/x$. This is the slope of the line connecting $(x, y)$ to $(0, 0)$ and it is clearly continuous. (We'd run into a problem if we tried to extend $m$ to the $y$-axis.) Since $p(t)$ has positive $x$-coordinate for all $t \in [0, 1]$ satisfying $|t - t_0| < \delta$, we can compose $p$ with $m$ to get the continuous function $t \mapsto m(p(t))$ mapping the interval $I := (t_0 - \delta, t_0 + \delta) \cap [0, 1]$ to $\mathbf{R}$. Since the values of $p$ on $I$ are in the deleted infinite broom without the origin, we get $m(p(I)) \subset \{0\} \cup \{1/n : n \in \mathbf{Z}^+\}$. The set $m(p(I))$ is connected since this is the image of a connected set $I$ under a continuous function. Therefore by Lemma 3.3, $m(p(I))$ is a single point. Since $t_0 \in I$ and $m(p(t_0)) = m(1, 0) = 0$, we get $m(p(I)) = 0$, so $I$ is an open set around $t_0$ in $[0, 1]$ that is contained in $A$. Thus $A$ is open in $[0, 1]$.

The only nonempty open and closed subset of $[0, 1]$ is $[0, 1]$, since $[0, 1]$ is connected. Therefore $A = [0, 1]$, which means $p(t) = (1, 0)$ for all $t \in [0, 1]$. $\square$

To understand the ideas in this argument, we apply them to a second subset of $\mathbf{R}^2$ that is connected but not path-connected, called the deleted comb space $D$. It is pictured below.

![Deleted comb space](page_004.png)

By definition, $D$ is the union of the interval $[0, 1]$ along the $x$-axis together with vertical line segments connecting $(1/n, 0)$ to $(1/n, 1)$ for $n \in \mathbf{Z}^+$ and the single (red) point $(0, 1)$:
$$D = ([0, 1] \times \{0\}) \cup \bigcup_{n \geq 1} (\{1/n\} \times [0, 1]) \cup (0, 1).$$
The $y$-axis strictly between $0$ and $1$ is not part of this.

**Theorem 3.6.** *The deleted comb space is connected but not path-connected.*

*Proof.* The set $D' = D - \{(0, 1)\}$ is obviously path-connected: there's a path in $D'$ linking any point in a bristle to the point on the $x$-axis at the end of that bristle, and any two points in $D'$ on the $x$-axis can obviously be linked by a path in $D'$ on the $x$-axis. Concatenating these constructions proves $D'$ is path-connected, and thus connected. Since $(0, 1)$ is a limit point of $D'$, $D$ lies between $D'$ and its closure, so $D$ is connected for the same reason the deleted infinite broom is connected. (The closure of $D'$ in $\mathbf{R}^2$ is $D$ together with the $y$-axis from $0$ to $1$, and it is path-connected.)

<!-- page 5 -->

To prove $D$ is not path-connected we'll show no path in $D$ links $(0, 1)$ to any other point: if $p \colon [0, 1] \to D$ has $p(0) = (0, 1)$ then $p(t) = (0, 1)$ for all $t$.

Let
$$A = \{t \in [0, 1] : p(t) = (0, 1)\}.$$
Since $0 \in A$, this is a nonempty subset of $[0, 1]$. We will show $A = [0, 1]$ by showing $A$ is open and closed in $[0, 1]$.

The set $A$ is closed since $A = p^{-1}((0, 1))$ and $p$ is continuous.

To show $A$ is open, choose $t_0 \in A$. From continuity of $p$, there's a $\delta > 0$ such that if $t \in [0, 1]$ satisfies $|t - t_0| < \delta$ then $\|p(t) - p(t_0)\| < 1/2$, so $\|p(t) - (0, 1)\| < 1/2$. No point on the $x$-axis is within $1/2$ of $(0, 1)$, so $p(t)$ is not on the $x$-axis when $t \in [0, 1]$ satisfies $|t - t_0| < \delta$.

In place of the slope function $m$ from the previous proof we will use the $x$-coordinate function. For points in $D$ that are not on the $x$-axis, their $x$-coordinate is $0$ or of the form $1/n$ for a positive integer $n$. The $x$-coordinate function $x \colon \mathbf{R}^2 \to \mathbf{R}$ is continuous and we can define a function $f \colon (t_0 - \delta, t_0 + \delta) \cap [0, 1] \to \mathbf{R}$ by $f(t) = x(p(t))$, which is continuous since it's the composition of continuous functions. Set $I := (t_0 - \delta, t_0 + \delta) \cap [0, 1]$, which is an open interval of $[0, 1]$ and thus is connected. Therefore $f(I)$ is connected and it belongs to $\{0\} \cup \{1/n : n \in \mathbf{Z}^+\}$, so $f(I)$ is a single point by Lemma 3.3. Since $t_0 \in I$ and $f(t_0) = x(p(t_0)) = x((0, 1)) = 0$ we get $f(I) = \{0\}$, so $I \subset A$. Therefore $A$ is open (for each $t_0 \in A$ some open interval around $t_0$ in $[0, 1]$ is also in $A$.) $\square$

Our third example of a topological space that is connected but not path-connected is the topologist's sine curve, pictured below, which is the union of the graph of $y = \sin(1/x)$ for $x > 0$ and the (red) point $(0, 0)$. (We stretch the graph horizontally to make its shape clearer, which doesn't affect the topological features.)

![Topologist's sine curve](page_005.png)

**Theorem 3.7.** *The topologist's sine curve is connected but not path-connected.*

*Proof.* The graph of $y = \sin(1/x)$ for $x > 0$, like any graph of a function, is path-connected and therefore is connected. Since $(0, 0)$ is a limit point of this graph, adjoining it to the graph gives us a connected set for the same reason the deleted infinite broom and deleted comb space are connected.

<!-- page 6 -->

Let $S$ denote the topologist's sine curve. To show $S$ is not path-connected, we'll show no path in $S$ links $(0, 0)$ to any other point in $S$. At first it might seem we could argue as in the first two examples, using the points in $S$ along the $x$-axis as a totally disconnected set analogous to the one in Lemma 3.3, but it does not seem to work; try it!

Suppose there is a path $p$ in $S$ from $(0, 0)$ to a point on the graph of $y = \sin(1/x)$ with $x > 0$. Let $x \colon \mathbf{R}^2 \to \mathbf{R}$ be the $x$-coordinate function, which is continuous. The path $p$ starts off on the $y$-axis and at some point has to "jump" onto the graph of $\sin(1/x)$, which is the points in $S$ with positive $x$-coordinate. Let $t_0$ be the time this happens; precisely, set
$$t_0 = \inf\{t \in [0, 1] : x(p(t)) > 0\}. \tag{3.1}$$
For $t < t_0$, $x(p(t)) = 0$. By continuity of $x \circ p$ at $t_0$, $x(p(t_0)) = \lim_{t \to t_0^-} x(p(t)) = 0$, so $p(t_0) = (0, 0)$. By continuity of $p$ at $t_0$, there is a $\delta > 0$ such that
$$t_0 \leq t < t_0 + \delta \Rightarrow \|p(t)\| < \frac{1}{2}. \tag{3.2}$$
We try to convey this visually in the picture below, where the red circle around $(0, 0) = p(t_0)$ has radius $1/2$.

![Topologist's sine curve with red circle](page_006.png)

By the definition of $t_0$ as an infimum, for this same $\delta$ there is a $t_1$ with $t_0 < t_1 < t_0 + \delta$ such that $a := x(p(t_1)) > 0$. The image $x(p([t_0, t_1]))$ is connected and contains $0 = x(p(t_0))$ and $a = x(p(t_1))$, and every connected subset of $\mathbf{R}$ is an interval, so
$$[0, a] \subset x(p([t_0, t_1])). \tag{3.3}$$
This contradicts continuity of $t \mapsto x(p(t))$ at $t_0$ by the picture above, because the graph of $\sin(1/x)$ is oscillating in and out of the red circle, so the $x$-values on $S$ inside the circle do *not* contain a whole interval like $[0, a]$. To turn this visual idea into a strict logical argument we look at where the peaks and troughs occur in $S$.

Since $\sin(\theta) = 1$ if and only if $\theta = (4k + 1)\frac{\pi}{2}$ and $\sin(\theta) = -1$ if and only if $\theta = (4k - 1)\frac{\pi}{2}$, where $k \in \mathbf{Z}$, we have $(x, \sin(1/x)) = (x, 1)$ if $x = 2/((4k + 1)\pi)$ and $(x, \sin(1/x)) = (x, -1)$ if $x = 2/((4k - 1)\pi)$ for $k \in \mathbf{Z}$. Such $x$-values get arbitrarily close to $0$ for large $k$, so there are such $x$-values of both kinds in $[0, a]$. Therefore by (3.3) we get $p(t') = (*, 1)$ and $p(t'') = (*, -1)$ for some $t'$ and $t''$ in $[t_0, t_1] \subset [t_0, t_0 + \delta)$. But $\|p(t')\| = \|(*, 1)\| > 1/2$ and $\|p(t'')\| = \|(*, -1)\| > 1/2$, which both contradict (3.2). $\square$

<!-- page 7 -->

The closures of the deleted infinite broom and deleted comb space are path-connected since all points in the closure are linked to $(0, 0)$ by a path in the closure, but the closure of the topologist's sine curve, which is obtained by adjoining the whole interval $\{0\} \times [-1, 1]$ on the $y$-axis to the graph,[^2] is *not* path-connected.

**Corollary 3.8.** *The closure of the topologist's sine curve is not path-connected.*

*Proof.* We modify the previous proof to show there is no path starting at a point in $\{0\} \times [-1, 1]$ and ending at a point on the graph of $y = \sin(1/x)$. Assuming there is such path, $p$, we have $x(p(0)) = 0$ and $x(p(1)) > 0$, so we can define $t_0$ as in (3.1) and $x(p(t_0)) = 0$. (It may not be that $p(t_0)$ is $(0, 0)$ anymore, but $p(t_0)$ does lie on the $y$-axis.) Choose $\delta$ so that
$$t_0 \leq t < t_0 + \delta \Rightarrow \|p(t) - p(t_0)\| < \frac{1}{2}.$$
Once again there's a $t_1 \in (t_0, t_0 + \delta)$ such that $x(p(t_1)) > 0$, so (3.3) holds where $a = x(p(t_1))$.

For some large $k$ we have $2/((4k \pm 1)\pi) \in [0, a]$ for both signs, so these are $x$-coordinates of $p(t')$ and $p(t'')$ for some $t'$ and $t''$ in $[t_0, t_1] \subset [t_0, t_0 + \delta)$: $p(t') = (*, 1)$ and $p(t'') = (*, -1)$. Since $\|p(t') - p(t_0)\| < 1/2$ and $\|p(t'') - p(t_0)\| < 1/2$, we get $\|p(t') - p(t'')\| < 1$, but $\|p(t') - p(t'')\| = \|(*, 1) - (*, -1)\| \geq \sqrt{(1 - (-1))^2} = 2 > 1$, a contradiction. $\square$

A local version of being path-connected is being *locally path-connected*, which means every neighborhood of each point contains an open set around the point that is path-connected. This property neither implies nor is implied by path-connectedness. For instance, the union $(0, 1) \cup (2, 3)$ with its topology from $\mathbf{R}$ is locally path-connected but is not path-connected: no path can involve points in both intervals. Here are three examples of topological spaces that are path-connected but not locally path-connected.

- The closure of the deleted infinite broom is path-connected but is not locally path-connected: small neighborhoods of $(0, 1/2)$ in it are not path-connected.
- The closure of the deleted comb space is path-connected but is not locally path-connected: small neighborhoods $(0, 1/2)$ in it are not path-connected.
- If we attach to the topologist's sine curve a path from $(0, 0)$ to $(1/\pi, 0)$ (the rightmost point where the curve crosses the $x$-axis) the resulting subset of $\mathbf{R}^2$ is path-connected but is not locally path-connected since no small neighborhood of $(0, 0)$ in it is path-connected. See https://math.stackexchange.com/questions/135463.

<!-- page 8 -->

## Appendix A. A Partial Converse to Theorem 2.1

There is an important case where a converse to Theorem 2.1 holds: open subsets of $\mathbf{R}^n$.

**Theorem A.1.** *If a nonempty open subset of $\mathbf{R}^n$ is connected then it is path-connected.*

*Proof.* Let $X$ be a nonempty open subset of $\mathbf{R}^n$ and pick $x \in X$. We want to show there is a path in $X$ from $x$ to every point in $X$. The special property of Euclidean space that we're going to use in the proof is that *balls in $\mathbf{R}^n$ are path-connected*.

Set
$$U = \{x' \in X : \text{there is a path in } X \text{ from } x \text{ to } x'\}.$$
This is a nonempty subset of $X$ since $x \in U$ (use the constant path $p \colon [0, 1] \to X$ where $p(t) = x$ for all $t$). We will show next that $U$ is open. Suppose $x' \in U$. Since $X$ is open in $\mathbf{R}^n$, there's an open ball $B$ in $\mathbf{R}^n$ such that $x' \in B \subset X$. For every point $b \in B$ there is a (straight line) path $p_1$ from $x'$ to $b$ that doesn't leave $B$ (so it doesn't leave $X$ either), and since $x' \in U$ there is a path $p_2$ in $X$ from $x$ to $x'$. Concatenating these paths together gives us a path in $X$ from $x$ to $b$. Strictly speaking, since paths are only defined with domain $[0, 1]$ we get a path from $x$ to $b$ by spending the first half of our time going from $x$ to $x'$ and the second half going from $x'$ to $b$: the function $p \colon [0, 1] \to X$ defined by
$$p(t) = \begin{cases} p_1(2t), & \text{if } 0 \leq t \leq \frac{1}{2}, \\ p_2(2t - 1), & \text{if } \frac{1}{2} \leq t \leq 1, \end{cases}$$
is continuous (since $p_1(1) = x' = p_2(0)$) and $p(0) = p_1(0) = x$, $p(1) = p_2(1) = b$. We have shown every $b \in B$ is in $U$, so to each $x' \in U$ there's an open ball around $x'$ that is entirely inside $U$ as well. Thus $U$ is open in $X$.

The complement of $U$ in $X$ is
$$V = \{x' \in X : \text{there is no path in } X \text{ from } x \text{ to } x'\}.$$
We want to prove $V = \emptyset$. If $V$ were nonempty and $x'$ is an element of $V$, then there is an open ball $B$ in $\mathbf{R}^n$ such that $x' \in B \subset X$. Since all points in $B$ can be linked to $x'$ by a path in $B$, if any point in $B$ were in $U$ then it could be linked by a path to $x$ in $X$ and we'd then be able to link $x$ and $x'$ by a path in $X$, which contradicts what it means for $x'$ to lie in $V$. Thus $B$ is disjoint from $U$, so $B \subset V$. Therefore $V$ is open in $X$ (every point in $V$ is contained in an open ball of $\mathbf{R}^n$ that's a subset of $V$).

The equation $X = U \cup V$ exhibits $X$ as a disjoint union of nonempty open subsets if $V \neq \emptyset$, which is a contradiction of the connectedness of $X$, so $V = \emptyset$. That means $U = X$, so *every* point in $X$ can be linked to $x$ by a path in $X$. Since this holds for all $x \in X$, $X$ is path-connected. $\square$

## References

[1] A. Douady and J. Hubbard, Itération des polynômes quadratiques complexes, *Comptes Rendus, Académie des Sciences, Paris* **294** (1982), 123--126.

[2] J. Munkres, "Topology, A First Course," Prentice-Hall, 1975.

[^1]: We're using here the $\varepsilon$-$\delta$ definition of continuity of $p \colon [0, 1] \to B$ at $t_0$ with $\varepsilon = 1/2$.

[^2]: Some people use the term "topologist's sine curve" to mean the closure of what we call the topologist's sine curve.
