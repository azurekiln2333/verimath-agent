# Finite-Dimensional Topological Vector Spaces

> **Source**: https://kconrad.math.uconn.edu/blurbs/finite-dim-TVS.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra

<!-- page 1 -->

## 1. Introduction

For a real vector space $V$, a norm $\|\cdot\|$ on $V$ leads to a metric $d(v, w) = \|v - w\|$ and then to a topology for which vector addition and scalar multiplication on $V$ are both continuous. If $V$ is finite-dimensional it can have many different norms (such as the Euclidean norm or sup-norm relative to a basis of $V$), but it turns out that all norms on $V$ lead to the same topology on $V$. Thus a finite-dimensional real vector space has a canonical topology, namely the one coming from a norm on the space (the choice of norm does not matter). This is not generally true for infinite-dimensional spaces, *e.g.*, on $C[0, 1]$ the sup-norm and all the $L^p$-norms for different $p \geq 1$ define different topologies.

Another aspect of infinite-dimensional spaces is that there a topology can make vector addition and scalar multiplication continuous but the topology does not come from a norm. For example, the usual topology on the Schwartz space $S(\mathbf{R})$ is defined by a countable family of semi-norms $|f|_{m,n} = \sup_{x \in \mathbf{R}} |x^m f^{(n)}(x)|$ for $m, n \geq 0$ but not by one norm.[^1]

Can a finite-dimensional real vector space have a topology making the vector space operations continuous besides its norm topology? No, and explaining this is our goal.

## 2. Topological Vector Spaces and Basic Properties

**Definition 2.1.** A *topological vector space* over $\mathbf{R}$ is an $\mathbf{R}$-vector space $V$ with a Hausdorff topology making vector addition $V \times V \to V$ and scalar multiplication $\mathbf{R} \times V \to V$ continuous, where $V \times V$ and $\mathbf{R} \times V$ have the product topology and $\mathbf{R}$ has its usual topology.

We will often abbreviate "topological vector space" to TVS, and until Section 4 we will assume a TVS is a vector space over $\mathbf{R}$.

**Example 2.2.** Every vector space with a norm on it is a TVS using the topology from that norm. In particular, we view $\mathbf{R}^n$ as a TVS using its norm topology (the usual one).

**Example 2.3.** The Schwartz space $S(\mathbf{R})$ is a TVS and its topology does not come a norm.

**Example 2.4.** For $n \geq 1$, is $\mathbf{R}^n$ with the discrete topology a TVS? Perhaps surprisingly, it isn't. While addition $\mathbf{R}^n \times \mathbf{R}^n \to \mathbf{R}^n$ is continuous, scalar multiplication $\mathbf{R} \times \mathbf{R}^n \to \mathbf{R}^n$ (with the scalar component $\mathbf{R}$ having its usual topology) is *not* continuous: the inverse image of the open set $\{\mathbf{0}\}$ is $N := \mathbf{R} \times \{\mathbf{0}\} \cup \{0\} \times \mathbf{R}^n$. If this were open in $\mathbf{R} \times \mathbf{R}^n$ then it would contain a basic open set around $(0, \mathbf{v})$ for each nonzero $\mathbf{v}$ in $\mathbf{R}^n$, but such a basic open set is $U \times \{\mathbf{v}\}$ where $U$ is an open interval around 0 in $\mathbf{R}$ and $U \times \{\mathbf{v}\}$ is not in $N$. Thus a discrete $\mathbf{R}^n$ is not a TVS.

If $\mathbf{R}^n$ has the discrete topology and scalar multiplication $\mathbf{R} \times \mathbf{R}^n \to \mathbf{R}^n$ is continuous, then $\mathbf{R}$ must be discrete: for $\mathbf{v}_0 \neq \mathbf{0}$, $\mathbf{R} \times \{\mathbf{v}_0\} \to \mathbf{R}^n$ by $(c, \mathbf{v}_0) \mapsto c\mathbf{v}_0$ is continuous and $\{c\mathbf{v}_0\}$ is open, so its inverse image $\{(c, \mathbf{v}_0)\}$ is open and $\mathbf{R} \times \{\mathbf{v}_0\}$ is homeomorphic to $\mathbf{R}$.

[^1]: This is proved here: <https://math.stackexchange.com/questions/2375320>.

<!-- page 2 -->

**Definition 2.5.** If $V$ and $W$ are each a TVS, an *isomorphism* $L \colon V \to W$ is a continuous linear bijection such that its inverse is also continuous.

As in abstract algebra, the inverse of a linear bijection is automatically linear, so we did not include that condition in the definition of an isomorphism.

**Example 2.6.** For $n \geq 2$, $\mathbf{R}^n$ and $\mathbf{R}^{n-1} \times \mathbf{R}$ are isomorphic topological vector spaces by the meaning of the product topology.

Our aim is to prove the following result, due to Tychonoff [2, pp. 769–770].

**Theorem 2.7.** *For $n \in \mathbf{Z}^+$, each $n$-dimensional TVS $V$ is isomorphic to $\mathbf{R}^n$ with its usual topology. More precisely, if $\{e_1, \ldots, e_n\}$ is a basis of $V$ then the mapping $\mathbf{R}^n \to V$ given by $(a_1, \ldots, a_n) \mapsto a_1 e_1 + \cdots + a_n e_n$ is a TVS isomorphism.*

Since the usual topology on $\mathbf{R}^n$ comes from a norm, the isomorphism in Theorem 2.7 shows the topology on $V$ comes from a norm. For the rest of this section we develop some results that will be used in the proof of Theorem 2.7.

In a TVS $V$, translation $v \mapsto v + v_0$ for a fixed $v_0 \in V$ and scaling $v \mapsto a_0 v$ for a fixed nonzero $a_0 \in \mathbf{R}$ are both homeomorphisms $V \to V$. In particular, for an open set $U \subset V$ containing 0 and an arbitrary $v_0 \in V$, $v_0 + U$ is an open set in $V$ containing $v_0$ and all open sets in $V$ containing $v_0$ arise in this way: the topology near each point of a TVS looks like the topology near 0.

**Definition 2.8.** Let $V$ be a TVS. A subset $B$ of $V$ is called *balanced* if

$$|a| \leq 1 \Longrightarrow aB \subset B.$$

When the topology on $V$ comes from a norm, every open ball centered at the origin is balanced. In a general TVS there is no metric and therefore no balls, but balanced sets make sense.

**Lemma 2.9.** *Every open set containing $\mathbf{0}$ in a TVS contains a balanced open set around $\mathbf{0}$.*

This lemma is obvious when the topology comes from a norm, since we can use open balls centered at 0 with respect to the norm. Since the lemma tells us that balanced open sets are a neighborhood basis of 0 in $V$, they could be considered a replacement for open balls around 0 in a general TVS.

*Proof.* Let $U$ be an open set in the TVS $V$ with $0 \in U$. We want to find a balanced subset $B \subset U$ with $0 \in B$. Scalar multiplication $\mathbf{R} \times V \to V$ is continuous with $(0, 0) \mapsto 0$, so there is an $\varepsilon > 0$ and open $U_0$ around 0 in $V$ such that

$$|a| < \varepsilon \text{ and } v \in U_0 \Longrightarrow av \in U.$$

If $|a| < \varepsilon$ and $|t| \geq 1$ then $|a/t| \leq |a| < \varepsilon$, so $(a/t)U_0 \subset U$. Thus $aU_0 \subset tU$. Letting $t$ vary, $aU_0 \subset \bigcap_{|t| \geq 1} tU$. Since $aU_0$ is open for all nonzero $a$, the set $\bigcap_{|t| \geq 1} tU$ contains an open set around 0 in $V$. Let $B$ be the interior of $\bigcap_{|t| \geq 1} tU$, so $B$ is a nonempty open set in $V$ and $B \subset U$ (take $t = 1$). If $0 < |a| \leq 1$ then $|t| \geq 1 \Rightarrow |t/a| = |t|/|a| \geq |t| \geq 1$, so $B \subset (t/a)U$ and thus $aB \subset tU$. Letting $t$ vary, we get $aB \subset B$ since $aB$ is open. Thus $B$ is balanced. $\square$

**Lemma 2.10.** *A linear map $L \colon V \to W$, where $V$ and $W$ are topological vector spaces, is continuous if and only if for all open sets $U$ around $0$ in $W$, $L^{-1}(U)$ contains an open set around $0$ in $V$. That is, continuity of a linear map $V \to W$ is equivalent to continuity at $0$.*

<!-- page 3 -->

*Proof.* Proving $(\Rightarrow)$ is easy from the definition of continuity together with $L(0) = 0$.

To prove $(\Leftarrow)$, since $L$ is additive it suffices show for every open set $U$ around 0 in $W$ that $L^{-1}(U)$ is open in $V$. (Note the task is to show $L^{-1}(U)$ is *open*, which is stronger than the hypothesis that $L^{-1}(U)$ contains an open set around 0.)

Pick $v \in L^{-1}(U)$, so $L(v) \in U$. By continuity of addition in $W$, there is an open set $U'$ around 0 in $W$ such that $Lv + U' \subset U$. By hypothesis, $L^{-1}(U')$ contains an open set $U''$ around 0 in $V$, so $L(U'') \subset U'$. Then

$$L(v + U'') = L(v) + L(U'') \subset L(v) + U' \subset U,$$

so $v + U'' \subset L^{-1}(U)$. $\square$

The following result will not be used in what follows, but is a nice illustration of the defining properties of a TVS.

**Theorem 2.11.** *Let $V$ be a TVS. For each subspace $W$ of $V$, its closure $\overline{W}$ is a subspace.*

*Proof.* This could be proved with a direct use of the definition of closure: $v \in \overline{W}$ when every open set in $V$ that contains $v$ intersects $W$. Instead we will give a proof using a property of closures and homogeneity:

- the closure $\overline{A}$ of a subset $A$ is the smallest closed subset containing it: if $A \subset C$ and $C$ is closed then $\overline{A} \subset C$,
- if a subset $C$ is closed, then $v + C$ and $aC$ are closed for each $v \in V$ and $a \in \mathbf{R}^\times$.

To prove $\overline{W}$ is a subspace of $V$, we want to show $\overline{W} + \overline{W} \subset \overline{W}$ and $a\overline{W} \subset \overline{W}$ for all $a \in \mathbf{R}$. (The continuity of vector addition and scalar multiplication on a subspace are automatic, so every subspace of a TVS is a TVS, and replacing $a$ with $1/a$ when $a \neq 0$ shows $a\overline{W} = \overline{W}$ for $a \in \mathbf{R}^\times$.)

Since $W$ is a subspace, $W + W \subset W \subset \overline{W}$. Thus for each $w \in W$, $w + W \subset \overline{W}$, so $W \subset -w + \overline{W}$. The set $-w + \overline{W}$ is closed since $\overline{W}$ is closed, so $\overline{W} \subset -w + \overline{W}$. Thus $w + \overline{W} \subset \overline{W}$ for all $w \in W$, so $W + \overline{W} \subset \overline{W}$.

To improve this to $\overline{W} + \overline{W} \subset \overline{W}$, for each $v \in \overline{W}$ we have $W + v \subset \overline{W}$, so $W \subset -v + \overline{W}$. Since $-v + \overline{W}$ is closed, $\overline{W} \subset -v + \overline{W}$. Thus $v + \overline{W} \subset \overline{W}$, and since $v$ was arbitrary in $\overline{W}$ we get $\overline{W} + \overline{W} \subset \overline{W}$. (Try to reprove that now on your own.)

For scalar multiplication, $a\overline{W} = \overline{\{0\}} \subset \overline{W}$ when $a = 0$, so assume $a \in \mathbf{R}^\times$. From $W \subset \overline{W}$, $aW \subset W \subset \overline{W}$, so $W \subset (1/a)\overline{W}$. Since $a \in \mathbf{R}^\times$, $(1/a)\overline{W}$ is closed, so $\overline{W} \subset (1/a)\overline{W}$. Multiplying by $a$ gives us $a\overline{W} \subset \overline{W}$. $\square$

## 3. Proof of Theorem 2.7

*Proof.* Let $V$ be a TVS $V$ of dimension $n$ and $\{e_1, \ldots, e_n\}$ be a basis of $V$. Let $L \colon \mathbf{R}^n \to V$ by

$$L(a_1, \ldots, a_n) = a_1 e_1 + \cdots + a_n e_n.$$

This is a vector space isomorphism, so $L$ and $L^{-1}$ are linear. Since $V$ is a TVS, $L$ is continuous on account of the continuity of vector addition and scalar multiplication in $V$.

It remains to prove that $L^{-1}$ is continuous, where $L^{-1} \colon V \to \mathbf{R}^n$ by

$$L^{-1}(a_1 e_1 + \cdots + a_n e_n) = (a_1, \ldots, a_n).$$

Let $B_\varepsilon(\mathbf{0}) = \{\mathbf{v} \in \mathbf{R}^n : \|\mathbf{v}\| < \varepsilon\}$. As $\varepsilon$ varies, these balls are a basis for the topology at $\mathbf{0}$ in $\mathbf{R}^n$, so by Lemma 2.10, it suffices to prove for each $\varepsilon > 0$ that $(L^{-1})^{-1}(B_\varepsilon(\mathbf{0})) = L(B_\varepsilon(\mathbf{0}))$

<!-- page 4 -->

contains an open set around 0 in $V$. That is, we want to show there is an open set $U_\varepsilon$ around 0 in $V$ such that $U_\varepsilon \subset L(B_\varepsilon(\mathbf{0}))$, or equivalently $L^{-1}(U) \subset B_\varepsilon(\mathbf{0})$: $v \in U_\varepsilon \Rightarrow \|L^{-1}(v)\| < \varepsilon$.

The construction of $U_\varepsilon$ will use local compactness of $\mathbf{R}^n$ in its usual topology. Set

$$S = \{(a_1, \ldots, a_n) \in \mathbf{R}^n : \|(a_1, \ldots, a_n)\| = 1\},$$

the unit sphere in $\mathbf{R}^n$. It is compact, so $L(S)$ is compact in $V$ by continuity of $L$, and $0 \notin L(S)$ since $L$ is a bijection and $L(\mathbf{0}) = 0$. Then $V - L(S)$ is an open set containing 0, so by Lemma 2.9 there is a balanced open set $U$ in $V - L(S)$ that contains 0. For $u \in U$ and $0 < |t| \leq 1$, $tu \in U$ from $U$ being balanced. Thus $tu \notin L(S)$, so $\|L^{-1}(tu)\| \neq 1$. By linearity of $L^{-1}$ we can rewrite this as $\|L^{-1}(u)\| \neq 1/|t|$ when $0 < |t| \leq 1$. Therefore $\|L^{-1}(u)\| < 1$, so $L^{-1}$ sends $U$ into the open unit ball of $\mathbf{R}^n$. Now we can set $U_\varepsilon = \varepsilon U = \{\varepsilon u : u \in U\}$: this is a balanced open set in $V$ that contains 0 and

$$v \in U_\varepsilon \Longrightarrow v/\varepsilon \in U \Longrightarrow \|L^{-1}(v/\varepsilon)\| < 1 \Longrightarrow \|L^{-1}(v)\| < \varepsilon,$$

which is what we wanted to show. $\square$

It was not crucial in this proof that the norm on $\mathbf{R}^n$ is the Euclidean norm. We could have used an arbitrary norm on $\mathbf{R}^n$. That would change the meaning of the unit sphere $S$. For example, if we use the sup-norm on $\mathbf{R}^n$ with respect to the standard basis then $S = \{(a_1, \ldots, a_n) \in \mathbf{R}^n : \max |a_i| = 1\}$. Regardless of the choice of norm, the unit sphere in $\mathbf{R}^n$ for that norm is compact (since $\mathbf{R}^n$ is locally compact), so the proof still works with this other unit sphere.

The concept of a TVS makes sense also for complex vector spaces (replace $\mathbf{R}$-linearity with $\mathbf{C}$-linearity everywhere), and arguments like those above show for each $n \in \mathbf{Z}^+$ that every $n$-dimensional complex TVS is isomorphic as a TVS to $\mathbf{C}^n$. In the proof we replace compactness of the unit sphere in $\mathbf{R}^n$ by compactness of the unit sphere

$$\{(z_1, \ldots, z_n) : \|(z_1, \ldots, z_n)\| = 1\} \tag{3.1}$$

in $\mathbf{C}^n$, where $\|\cdot\|$ is the standard norm (or an arbitrary norm) on $\mathbf{C}^n$. (Watch out: for $n \geq 1$ the sphere (3.1) is the solution set to $|z_1|^2 + \cdots + |z_n|^2 = 1$, but *not* the solution set to $z_1^2 + \cdots + z_n^2 = 1$, which is finite for $n = 1$ and unbounded for $n \geq 2$!)

If you know about the $p$-adic numbers $\mathbf{Q}_p$ for primes $p$ (if you don't know about them, then ignore this paragraph), check for $n \in \mathbf{Z}^+$ that the proof of Theorem 2.7 can be adapted to every $n$-dimensional TVS over $\mathbf{Q}_p$: a choice of basis makes it isomorphic to $\mathbf{Q}_p^n$. Changing the proof to be valid over $\mathbf{Q}_p$ needs a few changes: in the proof of Theorem 2.7 replace $(-\varepsilon, \varepsilon)$ with $\{x \in \mathbf{Q}_p : |x|_p < \varepsilon\}$ and show it suffices to work with $\varepsilon = |a|_p$ for nonzero $p$-adic numbers $a$, and use the sup-norm on $\mathbf{Q}_p^n$ in order that $\|\mathbf{Q}_p\| = |\mathbf{Q}_p|_p$ (this says the sup-norm of an $n$-tuple is the $p$-adic absolute value of some $p$-adic scalar). The sup-norm unit sphere in $\mathbf{Q}_p^n$ is $\mathbf{Z}_p^n - (p\mathbf{Z}_p)^n$, which is compact from compactness of $\mathbf{Z}_p$, and this lets the use of compactness of unit spheres carry over from the real to the $p$-adic setting.

## 4. A Second Proof of Theorem 2.7

For certain applications in number theory it is important to have a version of Theorem 2.7 where the scalar field $\mathbf{R}$ (or $\mathbf{C}$) is replaced by fields that are not locally compact. (Examples occur in non-Archimedean analysis: $\mathbf{C}_p$ with its $p$-adic topology and $F((t))$ with its $t$-adic topology where $F$ is an infinite field; their unit spheres are not compact.) That the proof of Theorem 2.7 no longer works for a TVS over certain fields does not mean the theorem itself is false. What we need is a different proof of Theorem 2.7 that does not use compactness

<!-- page 5 -->

arguments, and such a proof is developed in this final section. We will continue to work in the setting of real topological vector spaces for concreteness. At the end will we discuss what changes are needed for a TVS over other fields.

**Remark 4.1.** If all vector spaces you care about are real or complex then you might not have much motivation to read the more abstract build-up below to a second proof of Theorem 2.7, since the first proof already handles the cases of interest to you.

In metric spaces, topological concepts (continuity, compactness, *etc.*) can be described with sequences. Sequences are inadequate for this purpose in general topological spaces (*e.g.*, compactness and sequential compactness are not equivalent), and our first task is to give a substitute for sequences in all topological spaces.

A sequence in a space $X$ is just a function $f \colon \mathbf{Z}^+ \to X$, where $f(1)$ is the first term, $f(2)$ is the second term, and so on. The ordering on $\mathbf{Z}^+$ allows us to speak about one term in a sequence being "farther out" than another. The next definition gives the language to generalize this idea to more abstract indexing sets than $\mathbf{Z}^+$ in its standard ordering.

**Definition 4.2.** A *directed set* is a set $I$ with a partial ordering denoted by $\geq$ such that

(1) $i \geq i$ in $I$,
(2) $i \geq j$ and $j \geq k$ in $I$ implies $i \geq k$,
(3) for all $i$ and $j$ in $I$ there is some $k \in I$ such that $k \geq i$ and $k \geq j$.

**Example 4.3.** Take $I = \mathbf{Z}^+$ with its usual ordering $\geq$.

**Example 4.4.** Take $I = \mathbf{Z}^+$ with $\geq$ being reverse divisibility: $i \geq j$ means $j \mid i$. The reader should check this makes $\mathbf{Z}^+$ into a directed set, and it is not like the previous example. For instance, $\{i : i \geq 3\} = 3\mathbf{Z}^+$ and this is missing infinitely many positive integers, whereas for the standard ordering $\geq$ on $\mathbf{Z}^+$, $\{i : i \geq 3\}$ contains all but 2 positive integers.

**Example 4.5.** Take $I$ to be the open subsets of a topological space $X$ that contain a specific point $x_0$, with the ordering by reverse containment: $U_1 \geq U_2$ means $U_1 \subset U_2$ (so $U_1$ is "farther out" than $U_2$ if $U_1$ is a smaller neighborhood of $x_0$ than $U_2$). The first two conditions of a directed set are clear. For the third one, if $U$ and $U'$ are open sets in $X$ containing $x_0$ then so is $U \cap U'$ and we have $U \cap U' \geq U$ and $U \cap U' \geq U'$.

Example 4.5 is the directed set we'll be interested in for applications in topology.

A difference between the relation $\geq$ on a directed set $I$ and the usual relation $\geq$ on $\mathbf{Z}^+$ from Example 4.3 is that not all pairs of elements in $I$ are comparable to each other. (In Example 4.4 this means not all $i$ and $j$ in $\mathbf{Z}^+$ have $i \mid j$ or $j \mid i$.) To make up for that, the third condition of a directed set implies that for two incomparable elements in $I$, a third element in $I$ is comparable to both of them and is "farther out" than either one. Another way of saying this is that for all $j$ and $j'$ in $I$, $\{i : i \geq j\} \cap \{i : i \geq j'\} \neq \emptyset$.

**Definition 4.6.** For a set $X$, a *net* in $X$ is a function $f \colon I \to X$ where $I$ is a directed set.

When $I = \mathbf{Z}^+$ with its usual ordering, a net with index set $I$ is just a sequence.

**Definition 4.7.** We say a net $\{x_i\}_{i \in I}$ in a topological space $X$ *converges* to a point $x$ in $X$ if for every open subset $U \subset X$ containing $x$ there is an $i_0 \in I$ such that $i \geq i_0 \Rightarrow x_i \in U$. We then write $x = \lim_i x_i$. (Another notation is: $x_i \to x$.)

To see the concept of a net at work, we prove two properties of nets that are familiar properties of sequences in metric spaces.

<!-- page 6 -->

**Theorem 4.8.** *In a Hausdorff space, the limit of a convergent net is unique: if a net $\{x_i\}$ in a Hausdorff space $X$ has limits $x$ and $x'$ then $x = x'$.*

*Proof.* Assume $x \neq x'$. Since $X$ is Hausdorff, there are open sets $U$ and $U'$ such that $x \in U$ and $x' \in U'$ with $U$ and $U'$ being disjoint. From the definition of a convergent net, there is $i_0 \in I$ such that $i \geq i_0 \Rightarrow x_i \in U$ and there is $j_0 \in I$ such that $j \geq j_0 \Rightarrow x_j \in U'$. By the definition of a directed set, there is some $k \in I$ such that $k \geq i_0$ and $k \geq j_0$. Then $x_k \in U$ and $x_k \in U'$, so $U \cap U' \neq \emptyset$. This is a contradiction. $\square$

**Theorem 4.9.** *Let $Y$ be a nonempty subset of a topological space $X$, with closure $\overline{Y}$. For $x \in X$, we have $x \in \overline{Y}$ if and only if $x = \lim_i y_i$ in $X$ for some net $\{y_i\}$ in $Y$.*

Note that the phrase "$x = \lim_i y_i$ in $X$" means we are using the limit of a net in $X$, not in $Y$, even if the net is a subset of $Y$ ($x$ may not be in $Y$). This is reasonable in light of the result analogous to Theorem 4.9 for closures in metric spaces using sequences.

*Proof.* $(\Leftarrow)$ Suppose $x = \lim_i y_i$ in $X$ for some net $\{y_i\}$ in $Y$. To prove $x \in \overline{Y}$, assume this is not the case. Then $x$ is in $X - \overline{Y}$, which is a nonempty open set in $X$, so a net in $X$ that converges to $x$ must contain some elements of $X - \overline{Y}$. This set is disjoint from $Y$, so no net from $Y$ can lie even partially in $X - \overline{Y}$.

$(\Rightarrow)$ Let $x \in \overline{Y}$. From basic topology,

$$\overline{Y} = \bigcap_{\substack{C \supset Y \\ C \text{ closed}}} C. \tag{4.1}$$

We will construct a net in $Y$ converging to $x$ that uses as the directed set $I$ all open sets around $x$ in $X$ ordered by reverse inclusion. For each $U \in I$ we must have $U \cap Y \neq \emptyset$: if $U$ did not meet $Y$ then $Y \subset X - U$, and $X - U$ is closed, so by (4.1) and $x$ lying in $\overline{Y}$ we have $x \in X - U$, but that contradicts $x$ lying in $U$.

Since $U$ meets $Y$, we can choose some $y_U \in U \cap Y$. Now we have a net $I \to X$ where $U \mapsto y_U$. The elements of the net $\{y_U\}$ all belong to $Y$, and for each open set $U$ around $x$,

$$U' \geq U \Longrightarrow U' \subset U \Longrightarrow y_{U'} \in U' \subset U.$$

Thus $\lim_U y_U = x$. $\square$

**Remark 4.10.** The sequential compactness description of a compact metric space, which says every sequence has a convergent subsequence, generalizes using nets to compactness in arbitrary topological spaces: a topological space is compact if and only if every net in it has a convergent subnet. We don't go into more detail except to say that the definition of a subnet (the analogue of a subsequence) is subtle. It is *not* the restriction of a net $f \colon I \to X$ to a subset of $I$, even if $I = \mathbf{Z}^+$ with its usual ordering $\geq$.

Our generalities about nets are over and now we focus on their use in topological vector spaces, where they lead to analogues of Cauchy sequences and completeness in metric spaces.

**Definition 4.11.** In a TVS $V$, call a net $\{v_i\}$ *Cauchy* if for every open set $U$ around 0 in $V$ there is an $i_0 \in I$ such that $j, k \geq i_0 \Rightarrow v_j - v_k \in U$.

The basic idea here is that the metric notion of $d(x, y)$ being small is replaced by the difference $v - w$ in $V$ being in an open set around 0. We are defining Cauchy nets only in a TVS, not in a general topological space. (They can also be defined in topological groups.)

To get used to this terminology, we prove two lemmas about Cauchy nets that sound familiar for sequences in metric spaces.

<!-- page 7 -->

**Lemma 4.12.** *Every convergent net in a TVS is a Cauchy net.*

*Proof.* Let $\{x_i\}$ be a convergent net in $V$, with limit $x$. Pick an open set $U$ around 0 in $V$.

Since $-U = \{-u : u \in U\}$ is also an open set containing 0, so is $U \cap -U$, and this intersection is symmetric: $x \in U \cap -U \Rightarrow -x \in U \cap -U$. Therefore by shrinking an open set around 0 in $V$ we can assume it is symmetric if we wish.

By continuity of addition in $V$, there is an open set $N$ around 0 in $V$ such that $N + N \subset U$, and by replacing $N$ with $N \cap -N$ we can also assume $v \in N \Rightarrow -v \in N$.

Since $x + N$ is an open set in $V$ containing $x$, by the definition of a convergent net there is an $i_0 \in I$ such that $i \geq i_0 \Rightarrow x_i - x \in N$. So if $j \geq i_0$ and $k \geq i_0$ we have $x_j - x \in N$ and $x_k - x \in N$. Then $-(x_k - x) \in N$ by the symmetry of $N$, so for $j, k \geq i_0$ we have $x_j - x_k = (x_j - x) - (x_k - x) \in N + N \subset U$. $\square$

**Lemma 4.13.** *If $V$ is a TVS and $W$ is a subspace of $V$, viewed as a TVS with the subspace topology, then a Cauchy net in $V$ that lies in $W$ is a Cauchy net in $W$.*

*Proof.* Let $\{w_i\}$ be a Cauchy net in $V$ with $w_i \in W$ for all $i$. For an open set $U$ around 0 in $W$, by the definition of the subspace topology we have $U = U' \cap W$ where $U'$ is open in $V$. From the definition of a Cauchy net in $V$, there's an $i_0 \in I$ such that $j, k \geq i_0 \Rightarrow w_j - w_k \in U'$. We always have $w_j - w_k \in W$, so $j, k \geq i_0 \Rightarrow w_j - w_k \in U' \cap W = U$. $\square$

**Definition 4.14.** We say a TVS $V$ is *complete* if every Cauchy net in $V$ converges in $V$.

**Lemma 4.15.** *For $n \in \mathbf{Z}^+$, $\mathbf{R}^n$ is a complete TVS over $\mathbf{R}$.*

Even though we know all Cauchy sequences in $\mathbf{R}^n$ converge, that alone doesn't prove Lemma 4.15 since Cauchy nets are much more general than Cauchy sequences, *e.g.*, the directed set for a net might be uncountable.

*Proof.* Let $\{\mathbf{v}_i\}$ be a Cauchy net in $\mathbf{R}^n$. Even though the directed set for this net might not be countable or totally ordered, we are going to link the net to countable (sequential) information.

In $\mathbf{R}^n$ there is an open ball of radius 1 centered around $\mathbf{0}$, so there is some $i_1 \in I$ such that

$$j, k \geq i_1 \Longrightarrow \|\mathbf{v}_j - \mathbf{v}_k\| < 1,$$

where $\|\cdot\|$ is the standard norm on $\mathbf{R}^n$.

For each $m \geq 2$ there is an open ball in $\mathbf{R}^n$ of radius $1/m$ centered around $\mathbf{0}$, so there is some $i_m \in I$ such that

$$j, k \geq i_m \Longrightarrow \|\mathbf{v}_j - \mathbf{v}_k\| < \frac{1}{m}. \tag{4.2}$$

Since $I$ is directed, we can choose $i_m$ in $I$ such that

$$i_m \geq i_1, \ldots, i_{m-1}. \tag{4.3}$$

Then using $k = i_m$ in (4.2), we have

$$j \geq i_m \Longrightarrow \|\mathbf{v}_j - \mathbf{v}_{i_m}\| < \frac{1}{m}. \tag{4.4}$$

Consider the *sequence* $\{\mathbf{v}_{i_m}\}_{m \geq 1} = \{\mathbf{v}_{i_1}, \mathbf{v}_{i_2}, \ldots\}$ in $\mathbf{R}^n$. For $\varepsilon > 0$ there is an $m \in \mathbf{Z}^+$ such that $1/m < \varepsilon/2$. (Why require less than $\varepsilon/2$ rather than less than $\varepsilon$? You'll see.) By (4.3), if $m', m'' \geq m$ in $\mathbf{Z}^+$ then $i_{m'}, i_{m''} \geq i_m$ in $I$, so by (4.4),

$$\|\mathbf{v}_{i_{m'}} - \mathbf{v}_{i_{m''}}\| \leq \|\mathbf{v}_{i_{m'}} - \mathbf{v}_{i_m}\| + \|\mathbf{v}_{i_{m''}} - \mathbf{v}_{i_m}\| < 1/m + 1/m = 2/m < \varepsilon,$$

<!-- page 8 -->

where the last inequality comes from the condition $1/m < \varepsilon/2$. Thus $\{\mathbf{v}_{i_m}\}$ is a *Cauchy sequence* in $\mathbf{R}^n$. By the ordinary completeness of $\mathbf{R}^n$, there is some $\mathbf{v}$ in $\mathbf{R}^n$ such that the sequence $\{\mathbf{v}_{i_m}\}$ converges to $\mathbf{v}$.

We now show $\mathbf{v}$ is the limit of the original Cauchy net $\{\mathbf{v}_i\}$. Pick an open set in $\mathbf{R}^n$ around $\mathbf{v}$; it has the form $\mathbf{v} + U$ where $U$ is an open set around $\mathbf{0}$ in $\mathbf{R}^n$. For some $M \in \mathbf{Z}^+$ the open $1/M$-ball around $\mathbf{0}$ is contained in $U$. By the meaning of convergence of sequences, there is an $m \in \mathbf{Z}^+$ such that $m' \geq m \Rightarrow \|\mathbf{v}_{i_{m'}} - \mathbf{v}\| < 1/(2M)$, so by making $m$ larger we can assume $m \geq 2M$. Then for $j \in I$,

$$j \geq i_m \xRightarrow{(4.3)} j \geq i_{2M} \xRightarrow{(4.4)} \|\mathbf{v}_j - \mathbf{v}_{i_{2M}}\| < \frac{1}{2M},$$

so

$$j \geq i_m \Longrightarrow \|\mathbf{v}_j - \mathbf{v}\| \leq \|\mathbf{v}_j - \mathbf{v}_{i_m}\| + \|\mathbf{v}_{i_m} - \mathbf{v}\| < \frac{1}{m} + \frac{1}{2M} \leq \frac{1}{2M} + \frac{1}{2M} = \frac{1}{M}.$$

Thus $\mathbf{v}_j - \mathbf{v} \in U$, so $\mathbf{v}_j \in \mathbf{v} + U$ for all $j \geq i_m$. $\square$

The definition of completeness of a TVS depends only the TVS structure (there is no metric space structure available in general), so completeness is preserved under TVS isomorphisms. Thus Theorem 4.15 tells us that every TVS over $\mathbf{R}$ that is isomorphic to some $\mathbf{R}^n$ as a TVS over $\mathbf{R}$ is also a complete TVS.

**Lemma 4.16.** *For a TVS $V$, a linear map $L \colon V \to \mathbf{R}$ is continuous if and only if its kernel is closed in $V$.*

*Proof.* If $L$ is continuous then $\ker L = L^{-1}(0)$ is closed in $V$ since $\{0\}$ is closed in $\mathbf{R}$.

Now suppose $\ker L$ is closed in $V$. To show $L$ is continuous, we can assume $L$ is not identically 0, so $L$ is surjective (the only linear subspaces of $\mathbf{R}$ are $\{0\}$ and $\mathbf{R}$). For $\varepsilon > 0$ we will show $L^{-1}((-\varepsilon, \varepsilon))$ contains an open set around 0 in $V$. The intervals $(-\varepsilon, \varepsilon)$ are a basis for the topology around 0 in $\mathbf{R}$, so continuity of $L$ then follows from Lemma 2.10.

Pick $a_0 \in \mathbf{R}$ with $0 < |a_0| < \varepsilon$. Since $L$ is surjective, $L(v_0) = a_0$ for some $v_0 \in V$. Then $L^{-1}(a_0) = v_0 + \ker L$, a closed subset of $V$. Its complement in $V$ is open and contains 0 since $L(0) = 0 \neq a_0$. Therefore by Lemma 2.9 there is a balanced open set $U$ around 0 in $V$ such that $U \subset V - L^{-1}(a_0)$. For all $v \in U$, if $L(v) \neq 0$ then $L(a_0 v/L(v)) = a_0 L(v)/L(v) = a_0$, so $a_0 v/L(v) \notin U$. Therefore, from $U$ being balanced, $|a_0/L(v)| > 1$, so $|L(v)| < |a_0| < \varepsilon$. If $L(v) = 0$ then also $|L(v)| < \varepsilon$. Thus $U \subset \{v \in V : |L(v)| < \varepsilon\} = L^{-1}((-\varepsilon, \varepsilon))$. $\square$

Now we are ready to give a second proof of Theorem 2.7.

*Proof.* We will argue by induction on $n$, the dimension of $V$.

$n = 1$: Pick $v_0 \neq 0$ in $V$. Let $L \colon \mathbf{R} \to V$ by $L(a) = av_0$. This is a vector space isomorphism. To show $L$ is continuous, view $L$ as the composite of maps $\mathbf{R} \to \mathbf{R} \times \{v_0\} \to V$ where the first map is $a \mapsto (a, v_0)$ and the second map is scalar multiplication on $v_0$. The first map is continuous by the definition of the product topology and the second map is continuous by the continuity of scalar multiplication $\mathbf{R} \times V \to V$.

It remains to prove that $L^{-1} \colon V \to \mathbf{R}$ by $av_0 \mapsto a$ is continuous. Since it is linear, it suffices by Lemma 4.16 to show the kernel is closed. In $V$ we have $\ker(L^{-1}) = \{0\}$, which is closed (all points in a Hausdorff space are closed).

$n \geq 1$: Assume the theorem is proved for each TVS with dimension $n - 1$. Let $V$ be an $n$-dimensional TVS over $\mathbf{R}$ with basis $\{e_1, \ldots, e_n\}$ and define $L \colon \mathbf{R}^n \to V$ by $L(a_1, \ldots, a_n) =$

<!-- page 9 -->

$\sum_{i=1}^n a_i e_i$. As in the first proof, $L$ is a vector space isomorphism and it is continuous, so all that remains to prove is that $L^{-1} \colon V \to \mathbf{R}^n$ is continuous, where

$$L^{-1}(a_1 e_1 + \cdots + a_n e_n) = (a_1, \ldots, a_n).$$

Inside $V$ is the $(n-1)$-dimensional subspace

$$W = \mathbf{R}e_1 + \cdots + \mathbf{R}e_{n-1},$$

which is a TVS over $\mathbf{R}$ using the subspace topology, and by induction there is a TVS isomorphism $\Phi \colon W \to \mathbf{R}^{n-1}$ by $\Phi(a_1 e_1 + \cdots + a_{n-1} e_{n-1}) = (a_1, \ldots, a_{n-1})$.[^2] Define $\varphi \colon V \to \mathbf{R}$ by $\varphi(a_1 e_1 + \cdots + a_n e_n) = a_n$. Then $\varphi$ is linear and

$$L^{-1}(v) = (\Phi(v - \varphi(v)e_n), \varphi(v))$$

for all $v \in V$. In the formula on the right we are implicitly identifying $\mathbf{R}^{n-1} \times \mathbf{R}$ with $\mathbf{R}^n$ as a TVS over $\mathbf{R}$, which is okay since they are isomorphic (Example 2.6.)

Since $\Phi$ is continuous and scaling is continuous on $V$, the above formula for $L^{-1}$ shows that continuity of $L^{-1}$ will follow from continuity of $\varphi$. Since $\varphi$ takes values in $\mathbf{R}$, Lemma 4.16 tells us that continuity of $\varphi$ is equivalent to $\ker(\varphi)$ being closed in $V$. The kernel of $\varphi$ is $W$ and $\dim(W) = n - 1$. Why is an $(n-1)$-dimensional subspace $W$ of $V$ closed in $V$?

Let $\overline{W}$ be the topological closure of $W$ in $V$ and pick $v \in \overline{W}$. We want to prove $v \in W$. Since $v$ is in the closure $\overline{W}$ we have $v = \lim_i w_i$ for some *net* $\{w_i\}$ that lies in $W$ (Theorem 4.9). Because $\{w_i\}$ is a convergent net in $V$, it is also a Cauchy net in $V$ by Lemma 4.12. Since every $w_i$ is in $W$, $\{w_i\}$ is a Cauchy net in $W$ by Lemma 4.13. Because $W \cong \mathbf{R}^{n-1}$ as a TVS over $\mathbf{R}$ and $\mathbf{R}^{n-1}$ is a complete TVS by Lemma 4.15, $W$ is a complete TVS. Therefore $\{w_i\}$ converges in $W$, say to $w$. Both $v$ and $w$ are limits of the Cauchy net $\{w_i\}$, and a TVS is Hausdorff by definition, so $v = w$ by Theorem 4.8. Thus $v \in W$, which finishes this second proof of Theorem 2.7. $\square$

**Remark 4.17.** The base case $n = 1$ relied on the reasoning behind Lemma 4.16 (and in particular Lemma 2.10). This is a nice example of a proof by induction where the base case is not a complete triviality.

The motivation for this second proof of Theorem 2.7, as mentioned at the start of this section, is that the proof and the background lemmas leading up to it apply with very minor changes to a finite-dimensional TVS over a field $K$ that is *complete with respect to a nontrivial absolute value*. There are many such $K$ where, in contrast to $\mathbf{R}$ and $\mathbf{C}$, the unit sphere $\{x \in K : |x| = 1\}$ in $K$ is not compact, so the first proof of Theorem 2.7 (in Section 3) can't be applied to a TVS over $K$. As an example of how lemmas for the second proof of Theorem 2.7 generalize, the proof of Lemma 4.15 can be used with minor changes to show $K^n$ with the topology coming from its sup-norm is a complete TVS over $K$: all Cauchy nets in $K^n$ converge. A related theorem is that all norms on a finite-dimensional $K$-vector space define the same topology on the space [1, Theorem 3.2], and this has a simpler proof when the unit sphere of $K$ is compact.

## References

[1] K. Conrad, "Equivalence of norms," <https://kconrad.math.uconn.edu/blurbs/gradnumthy/equiv_norms.pdf>.

[2] A. Tychonoff, "Ein Fixpunktsatz," *Math. Ann.* **111** (1935), 767–776. URL <https://eudml.org/doc/159810>.

[^2]: Here we are using $n > 1$: if $n = 1$ then $W = \{0\}$ and has no basis.
