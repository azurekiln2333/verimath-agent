# Group Actions

> Keith Conrad
> **Source:** https://kconrad.math.uconn.edu/blurbs/grouptheory/gpaction.pdf
> **Topic:** group_theory
> **License:** All papers by Keith Conrad

<!-- page 1 -->

## 1. Introduction

One of the most important ideas in group theory is that a group can "act" on a set. This concept unifies many constructions and allows us to use group theory to study symmetry, counting, and structural properties of groups and other mathematical objects.

The basic idea is simple: a **group action** is a way of interpreting the elements of a group as permutations or transformations of a set, in a manner compatible with the group operation.

**Definition 1.1.** Let $G$ be a group and $S$ a set. A (left) **action** of $G$ on $S$ is a map $G \times S \to S$, written $(g, s) \mapsto g \cdot s$, satisfying:
(1) $e \cdot s = s$ for all $s \in S$, where $e$ is the identity of $G$.
(2) $(g_1 g_2) \cdot s = g_1 \cdot (g_2 \cdot s)$ for all $g_1, g_2 \in G$ and $s \in S$.

When a group $G$ acts on a set $S$, we gain a powerful tool for studying both $G$ and $S$. The action allows us to apply the abstract structure of $G$ to understand the symmetries and properties of $S$, and conversely, properties of $S$ can reveal information about $G$.

The most fundamental result connecting groups to actions is Cayley's theorem, which shows that every group arises as a group of permutations.

**Theorem 1.2 (Cayley's Theorem).** Every group $G$ is isomorphic to a subgroup of $S_G$, the group of all permutations of $G$.

*Proof.* For each $g \in G$, define $\lambda_g : G \to G$ by $\lambda_g(x) = gx$. This is a bijection (with inverse $\lambda_{g^{-1}}$), so $\lambda_g \in S_G$. Define $\varphi : G \to S_G$ by $\varphi(g) = \lambda_g$. Then $\varphi(g_1 g_2) = \varphi(g_1) \circ \varphi(g_2)$ since $\lambda_{g_1 g_2}(x) = g_1 g_2 x = \lambda_{g_1}(\lambda_{g_2}(x))$. Also $\varphi$ is injective: if $\lambda_g = \text{id}$, then $gx = x$ for all $x$, so $g = e$.

This leads us to the formal definition of a group action and its basic properties.

**Definition 1.3.** A **group action** of a group $G$ on a set $S$ is a map $G \times S \to S$, $(g, s) \mapsto g \cdot s$, such that:
(1) $e \cdot s = s$ for all $s \in S$.
(2) $g_1 \cdot (g_2 \cdot s) = (g_1 g_2) \cdot s$ for all $g_1, g_2 \in G$ and $s \in S$.

We also say that $G$ acts on $S$, or $S$ is a $G$-set.

Group actions appear throughout mathematics. They provide a unified framework for studying symmetry in geometry, counting problems in combinatorics, and structural properties in algebra.

**Remark 1.4.** A right action is defined similarly, with $(s \cdot g_1) \cdot g_2 = s \cdot (g_1 g_2)$. We focus on left actions unless otherwise stated.

**Example 1.5.** The symmetric group $S_n$ acts on the set $\{1, 2, \ldots, n\}$ by $\sigma \cdot i = \sigma(i)$.

**Example 1.6.** Any group $G$ acts on itself by left multiplication: $g \cdot x = gx$. Cayley's theorem is a special case of this.

The connection between group actions and homomorphisms into symmetric groups is made precise in the following theorem.

**Theorem 1.7.** Let $G$ be a group and $S$ a set. Giving an action of $G$ on $S$ is equivalent to giving a homomorphism $\varphi : G \to S_S$.

*Proof.* Given an action $G \times S \to S$, define $\varphi(g)(s) = g \cdot s$. The action axioms ensure $\varphi(g) \in S_S$ and $\varphi$ is a homomorphism. Conversely, given $\varphi : G \to S_S$, define $g \cdot s = \varphi(g)(s)$. The homomorphism property ensures the action axioms hold.

**Corollary 1.8.** If $|G| = n$, then $G$ is isomorphic to a subgroup of $S_n$.

This is just the beginning. In the following sections, we will explore many examples of group actions, develop the theory of orbits and stabilizers, and see how group actions lead to powerful results in counting, number theory, and even physics.


<!-- page 3 -->

## 2. Examples of Group Actions

**Example 2.1 (Trivial action).** Every group $G$ acts on any set $S$ by $g \cdot s = s$ for all $g \in G$, $s \in S$. This is the **trivial action**.

**Example 2.2.** Every group $G$ acts on itself by left multiplication: $g \cdot x = gx$. This is the action used in Cayley's theorem.

**Example 2.3.** Every group $G$ acts on itself by **conjugation**: $g \cdot x = gxg^{-1}$. Let us verify: $e \cdot x = exe^{-1} = x$, and $(g_1 g_2) \cdot x = (g_1 g_2) x (g_1 g_2)^{-1} = g_1(g_2 x g_2^{-1})g_1^{-1} = g_1 \cdot (g_2 \cdot x)$.

**Example 2.4.** Let $H$ be a subgroup of $G$. Then $G$ acts on the set of left cosets $G/H$ by left multiplication: $g \cdot (aH) = (ga)H$.

**Example 2.5.** The dihedral group $D_n$ (of order $2n$) acts on the vertices of a regular $n$-gon. If we label the vertices $\{1, 2, \ldots, n\}$, this gives a homomorphism $D_n \to S_n$.

**Example 2.6.** The group $GL_n(F)$ acts on $F^n$ (column vectors) by matrix multiplication: $A \cdot v = Av$.

**Example 2.7.** The group $GL_n(F)$ acts on the set of $n \times n$ matrices over $F$ by conjugation: $A \cdot M = AMA^{-1}$.

**Example 2.8.** The symmetric group $S_n$ acts on $\{1, 2, \ldots, n\}$ by $\sigma \cdot i = \sigma(i)$.

**Example 2.9.** The group $S_n$ acts on $\mathbf{R}^n$ by permuting coordinates: $\sigma \cdot (x_1, \ldots, x_n) = (x_{\sigma^{-1}(1)}, \ldots, x_{\sigma^{-1}(n)})$.

**Example 2.10.** The group $S_n$ acts on the polynomial ring $R[X_1, \ldots, X_n]$ by permuting variables: $\sigma \cdot f(X_1, \ldots, X_n) = f(X_{\sigma^{-1}(1)}, \ldots, X_{\sigma^{-1}(n)})$. The polynomials fixed by all of $S_n$ are the **symmetric polynomials**.

**Example 2.11.** Let $G$ act on $S$. Then $G$ acts on the power set $\mathcal{P}(S)$ by $g \cdot A = \{g \cdot a : a \in A\}$ for $A \subseteq S$.

**Example 2.12.** Let $G$ act on $S$. Then $G$ acts on $S \times S$ by $g \cdot (s_1, s_2) = (g \cdot s_1, g \cdot s_2)$, and more generally on $S^n = S \times \cdots \times S$ ($n$ factors).

**Example 2.13.** Let $V$ be a vector space over $F$. The group $GL(V)$ acts on $V$ by $T \cdot v = T(v)$, and on the set of subspaces of $V$ by $T \cdot W = T(W)$.

**Example 2.14.** Let $G$ be a group acting on a set $S$, and let $s \in S$. The map $G \to S$ given by $g \mapsto g \cdot s$ is called the **orbit map** at $s$.

**Example 2.15.** The group $(\mathbf{Z}, +)$ acts on $\mathbf{R}$ by $n \cdot x = x + n$. This is a translation action.

**Example 2.16.** Let $G$ act on $S$ and $T$ be a set. Then $G$ acts on the set of functions $\text{Map}(T, S)$ by $(g \cdot f)(t) = g \cdot f(t)$.

**Example 2.17.** Let $N$ be a normal subgroup of $G$. Then $G$ acts on $N$ by conjugation: $g \cdot n = gng^{-1}$. This is well-defined since $N$ is normal.

**Example 2.18.** Let $G$ be a group and $\text{Aut}(G)$ its automorphism group. Then $\text{Aut}(G)$ acts on $G$ by $\varphi \cdot g = \varphi(g)$. The inner automorphisms $\text{Inn}(G) = \{\varphi_g : g \in G\}$ where $\varphi_g(x) = gxg^{-1}$ form a normal subgroup of $\text{Aut}(G)$.

**Example 2.19.** The group $G$ acts on the set of its subgroups by conjugation: $g \cdot H = gHg^{-1}$. The subgroups fixed by this action are exactly the normal subgroups of $G$.

**Example 2.20.** Let $G$ act on $S$ and $H \leq G$. Then $H$ also acts on $S$ by restriction. The $H$-orbits are contained in the $G$-orbits.

**Example 2.21.** Let $V$ be a finite-dimensional vector space. The group $GL(V)$ acts on the set of bases of $V$. Given a basis $\mathcal{B}$, the action is simply $T \cdot \mathcal{B} = \{T(b) : b \in \mathcal{B}\}$.

**Example 2.22.** Let $G$ be a group acting on itself by conjugation. The orbits are the **conjugacy classes** of $G$. The **center** $Z(G)$ is the set of elements whose conjugacy class is a singleton.


<!-- page 10 -->

## 3. Orbits and Stabilizers

**Definition 3.1.** Let $G$ act on a set $S$.
- The **orbit** of $s \in S$ is $\text{Orb}(s) = \{g \cdot s : g \in G\}$.
- The **stabilizer** of $s \in S$ is $\text{Stab}(s) = \{g \in G : g \cdot s = s\}$.

The set of orbits is denoted $S/G$ or $G \backslash S$. The number of orbits is $|S/G|$.

**Remark 3.2.** The stabilizer $\text{Stab}(s)$ is a subgroup of $G$: if $g \cdot s = s$ and $h \cdot s = s$, then $(gh) \cdot s = g \cdot (h \cdot s) = g \cdot s = s$, and $g^{-1} \cdot s = g^{-1} \cdot (g \cdot s) = (g^{-1}g) \cdot s = e \cdot s = s$.

The orbits partition the set $S$. This is a fundamental fact.

**Theorem 3.3.** The orbits of a group action partition the set $S$. That is, every element of $S$ belongs to exactly one orbit.

*Proof.* Define a relation on $S$ by $s_1 \sim s_2$ if $\text{Orb}(s_1) = \text{Orb}(s_2)$, or equivalently, if $s_2 = g \cdot s_1$ for some $g \in G$. This is an equivalence relation:
- Reflexive: $s = e \cdot s$, so $s \sim s$.
- Symmetric: if $s_2 = g \cdot s_1$, then $s_1 = g^{-1} \cdot s_2$, so $s_1 \sim s_2$.
- Transitive: if $s_2 = g_1 \cdot s_1$ and $s_3 = g_2 \cdot s_2$, then $s_3 = (g_2 g_1) \cdot s_1$, so $s_1 \sim s_3$.

Since equivalence relations partition the set, the orbits partition $S$.

**Definition 3.4.** The action of $G$ on $S$ is **transitive** if there is only one orbit, i.e., for any $s_1, s_2 \in S$, there exists $g \in G$ such that $g \cdot s_1 = s_2$.

**Example 3.5.** $GL_n(F)$ acts transitively on $F^n \setminus \{0\}$: given nonzero vectors $v, w$, there is an invertible matrix sending $v$ to $w$.

**Example 3.6.** $S_n$ acts transitively on $\{1, 2, \ldots, n\}$: for any $i, j$, there is a permutation sending $i$ to $j$.

**Example 3.7.** $D_n$ acts transitively on the vertices of a regular $n$-gon.

Now we come to the most important theorem about group actions.

**Theorem 3.8 (Orbit-Stabilizer Theorem).** Let $G$ act on $S$ and let $s \in S$. There is a bijection
$$\text{Orb}(s) \cong G / \text{Stab}(s)$$
given by $g \cdot s \leftrightarrow g\text{Stab}(s)$. In particular, if $G$ is finite,
$$|\text{Orb}(s)| = [G : \text{Stab}(s)] = \frac{|G|}{|\text{Stab}(s)|}.$$

*Proof.* Define $\varphi : G/\text{Stab}(s) \to \text{Orb}(s)$ by $\varphi(g\text{Stab}(s)) = g \cdot s$.

**Well-defined:** If $g' \text{Stab}(s) = g \text{Stab}(s)$, then $g^{-1}g' \in \text{Stab}(s)$, so $(g^{-1}g') \cdot s = s$, hence $g' \cdot s = g \cdot (g^{-1}g' \cdot s) = g \cdot s$.

**Injective:** If $g_1 \cdot s = g_2 \cdot s$, then $(g_2^{-1}g_1) \cdot s = s$, so $g_2^{-1}g_1 \in \text{Stab}(s)$, hence $g_1 \text{Stab}(s) = g_2 \text{Stab}(s)$.

**Surjective:** Every element of $\text{Orb}(s)$ has the form $g \cdot s$ for some $g \in G$.

**Corollary 3.9.** If $G$ is finite and acts on $S$, then $|\text{Orb}(s)|$ divides $|G|$ for every $s \in S$.

**Corollary 3.10.** If $p$ is the smallest prime dividing $|G|$ and $|\text{Orb}(s)| = p$, then $\text{Stab}(s)$ is a normal subgroup of $G$ of index $p$.

**Example 3.11.** Consider $S_n$ acting on the set of ordered $r$-tuples of distinct elements from $\{1, \ldots, n\}$. The stabilizer of $(1, 2, \ldots, r)$ is $S_{n-r}$ (permutations fixing $1, \ldots, r$), so the orbit has size $n!/(n-r)!$.

**Example 3.12.** Consider $D_n$ acting on the vertices of a regular $n$-gon. For any vertex $v$, $|\text{Stab}(v)| = 2$ (the identity and the reflection through $v$), so $|\text{Orb}(v)| = 2n/2 = n$.

**Example 3.13.** Consider $G$ acting on itself by conjugation. Then $\text{Orb}(x)$ is the conjugacy class of $x$, and $\text{Stab}(x) = C_G(x)$, the centralizer of $x$ in $G$.


**Definition 3.14.** The **class equation** of a finite group $G$ is
$$|G| = |Z(G)| + \sum_{i} [G : C_G(x_i)]$$
where $Z(G)$ is the center of $G$, and the $x_i$ are representatives of the conjugacy classes of size greater than 1.

This follows from the orbit-stabilizer theorem applied to the conjugation action.

**Lemma 3.15.** Let $G$ act on $S$, and let $N$ be a normal subgroup of $G$. Let $S^N = \{s \in S : n \cdot s = s \text{ for all } n \in N\}$ be the set of fixed points of $N$. Then $S^N$ is $G$-stable: if $s \in S^N$ and $g \in G$, then $g \cdot s \in S^N$.

*Proof.* Let $s \in S^N$ and $g \in G$. For any $n \in N$, we need to show $n \cdot (g \cdot s) = g \cdot s$. Since $N$ is normal, $g^{-1}ng \in N$, so $(g^{-1}ng) \cdot s = s$. Then $n \cdot (g \cdot s) = g \cdot ((g^{-1}ng) \cdot s) = g \cdot s$.

Now we turn to counting results. The most important is Burnside's lemma (also called the Cauchy-Frobenius lemma).

**Theorem 3.16.** Let $G$ be a finite group acting on a finite set $S$. Let $S^g = \{s \in S : g \cdot s = s\}$ be the set of fixed points of $g$. Then the number of orbits is
$$|S/G| = \frac{1}{|G|} \sum_{g \in G} |S^g|.$$

*Proof.* Count the set $X = \{(g, s) \in G \times S : g \cdot s = s\}$ in two ways.

First, summing over $g$: $|X| = \sum_{g \in G} |S^g|$.

Second, summing over $s$: $|X| = \sum_{s \in S} |\text{Stab}(s)|$.

By the orbit-stabilizer theorem, $|\text{Stab}(s)| = |G|/|\text{Orb}(s)|$. For a given orbit $O$, each $s \in O$ has $|\text{Stab}(s)| = |G|/|O|$. So the contribution of orbit $O$ to the sum is
$$\sum_{s \in O} |\text{Stab}(s)| = |O| \cdot \frac{|G|}{|O|} = |G|.$$

Since there are $|S/G|$ orbits, $|X| = |G| \cdot |S/G|$. Equating the two expressions: $|G| \cdot |S/G| = \sum_{g \in G} |S^g|$.

**Example 3.17.** Let $D_4$ act on the vertices $\{1, 2, 3, 4\}$ of a square. We count fixed points:
- Identity $e$: fixes all 4 vertices. $|S^e| = 4$.
- Rotation $r$ (90 degrees): no fixed vertices. $|S^r| = 0$.
- Rotation $r^2$ (180 degrees): no fixed vertices. $|S^{r^2}| = 0$.
- Rotation $r^3$ (270 degrees): no fixed vertices. $|S^{r^3}| = 0$.
- Reflection $s$ (horizontal): fixes vertices 1 and 3 (say). $|S^s| = 2$.
- Reflection $sr$: fixes no vertices. $|S^{sr}| = 0$.
- Reflection $sr^2$: fixes vertices 2 and 4. $|S^{sr^2}| = 2$.
- Reflection $sr^3$: fixes no vertices. $|S^{sr^3}| = 0$.

Number of orbits $= \frac{1}{8}(4 + 0 + 0 + 0 + 2 + 0 + 2 + 0) = \frac{8}{8} = 1$.

Indeed, $D_4$ acts transitively on the vertices, so there is one orbit.

**Example 3.18.** Let $G$ act on itself by conjugation. Then $S^g = C_G(g)$, the centralizer of $g$. The number of orbits is the number of conjugacy classes. Burnside's lemma gives:
$$\text{number of conjugacy classes} = \frac{1}{|G|} \sum_{g \in G} |C_G(g)|.$$

**Definition 3.19.** A group action is **free** if $\text{Stab}(s) = \{e\}$ for all $s \in S$. Equivalently, $g \cdot s = s$ implies $g = e$.

**Theorem 3.20.** If $G$ acts freely on $S$, then every orbit has size $|G|$.

*Proof.* By the orbit-stabilizer theorem, $|\text{Orb}(s)| = |G|/|\text{Stab}(s)| = |G|/1 = |G|$.

**Corollary 3.21.** If $G$ acts freely on $S$, then $|G|$ divides $|S|$.

**Example 3.22.** The group $G$ acts freely on itself by left multiplication (Cayley's theorem). Every orbit has size $|G|$, and there is one orbit.

**Example 3.23.** Let $H \leq G$. Then $H$ acts freely on $G$ by left multiplication. The orbits are the right cosets $Hg$, each of size $|H|$. This gives another proof of Lagrange's theorem.

**Definition 3.24.** The action of $G$ on $S$ is **faithful** if the only element fixing every point is the identity: $\bigcap_{s \in S} \text{Stab}(s) = \{e\}$. Equivalently, the associated homomorphism $G \to S_S$ is injective.

**Theorem 3.25.** Let $G$ act on $S$. The kernel of the associated homomorphism $\varphi : G \to S_S$ is $K = \bigcap_{s \in S} \text{Stab}(s)$. The action is faithful if and only if $K = \{e\}$.


<!-- page 21 -->

## 4. Actions of $p$-Groups

One of the most elegant applications of group actions is to the theory of $p$-groups. The key idea is to use a $p$-group acting on a set and count fixed points modulo $p$.

**Theorem 4.1.** Let $G$ be a $p$-group (i.e., $|G| = p^n$ for some prime $p$ and $n \geq 1$) acting on a finite set $S$. Then
$$|S| \equiv |S^G| \pmod{p}$$
where $S^G = \{s \in S : g \cdot s = s \text{ for all } g \in G\}$ is the set of fixed points.

*Proof.* The orbits partition $S$. For any $s \in S$, $|\text{Orb}(s)| = [G : \text{Stab}(s)] = |G|/|\text{Stab}(s)| = p^n/|\text{Stab}(s)|$.

If $s \in S^G$, then $\text{Stab}(s) = G$ and $|\text{Orb}(s)| = 1$.

If $s \notin S^G$, then $\text{Stab}(s) \neq G$, so $|\text{Stab}(s)| = p^k$ with $k < n$, and $|\text{Orb}(s)| = p^{n-k} \geq p$. In particular, $p$ divides $|\text{Orb}(s)|$.

Summing over all orbits:
$$|S| = \sum_{\text{orbits } O} |O| = |S^G| + \sum_{\substack{\text{orbits } O \ |O| > 1}} |O|.$$

Since each non-trivial orbit has size divisible by $p$:
$$|S| \equiv |S^G| \pmod{p}.$$

**Corollary 4.2.** If $G$ is a $p$-group, then $Z(G) \neq \{e\}$.

*Proof.* Let $G$ act on itself by conjugation. Then $S^G = Z(G)$ (the center), and $|S| = |G| = p^n$. By Theorem 4.1:
$$p^n \equiv |Z(G)| \pmod{p}.$$

Since $p$ divides $p^n$, we get $p$ divides $|Z(G)|$. Since $e \in Z(G)$, we have $|Z(G)| \geq 1$, so $|Z(G)| \geq p$. In particular, $Z(G) \neq \{e\}$.

**Corollary 4.3.** If $|G| = p^n$ with $n \geq 1$, then $G$ has a normal subgroup of order $p^k$ for every $0 \leq k \leq n$.

*Proof.* By induction on $n$. The base case $n = 1$ is trivial. For $n \geq 2$, by Corollary 4.2, $Z(G) \neq \{e\}$, so there exists $z \in Z(G)$ of order $p$. The subgroup $\langle z \rangle$ is normal in $G$ (since $z$ is central). Then $G/\langle z \rangle$ has order $p^{n-1}$, and by induction, it has normal subgroups of every order $p^k$ for $0 \leq k \leq n-1$. By the correspondence theorem, these lift to normal subgroups of $G$ containing $\langle z \rangle$.


<!-- page 22 -->

## 5. New Proofs of Classical Theorems Using Group Actions

Group actions can provide elegant new proofs of classical results. We present several examples.

**Theorem 5.1 (Cauchy's Theorem).** If $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ has an element of order $p$.

We give McKay's beautiful proof using group actions.

*Proof (McKay).* Consider the set
$$X = \{(g_1, g_2, \ldots, g_p) \in G^p : g_1 g_2 \cdots g_p = e\}.$$

The elements of $X$ are determined by the first $p-1$ entries (since $g_p = (g_1 \cdots g_{p-1})^{-1}$), so $|X| = |G|^{p-1}$. Since $p$ divides $|G|$, we have $p$ divides $|X|$.

Now let $\sigma = (1\ 2\ \cdots\ p) \in S_p$ act on $X$ by cyclic permutation:
$$\sigma \cdot (g_1, g_2, \ldots, g_p) = (g_p, g_1, g_2, \ldots, g_{p-1}).$$

We need to check this is well-defined. If $g_1 g_2 \cdots g_p = e$, then $g_p g_1 \cdots g_{p-1} = g_p(g_1 \cdots g_{p-1}) = g_p g_p^{-1} = e$ (since $g_1 \cdots g_{p-1} = g_p^{-1}$). Wait, let me redo this: from $g_1 g_2 \cdots g_p = e$, we get $g_p = (g_1 \cdots g_{p-1})^{-1}$. Then $g_p g_1 g_2 \cdots g_{p-1} = (g_1 \cdots g_{p-1})^{-1} (g_1 \cdots g_{p-1}) = e$. So the cyclic shift is indeed in $X$.

Since $\sigma$ generates a group of order $p$ acting on $X$, by Theorem 4.1:
$$|X| \equiv |X^{\langle \sigma \rangle}| \pmod{p}.$$

Since $p$ divides $|X|$, we get $p$ divides $|X^{\langle \sigma \rangle}|$.

A fixed point of $\sigma$ is a tuple $(g_1, \ldots, g_p)$ with $g_1 = g_2 = \cdots = g_p = a$ for some $a \in G$. The condition $g_1 \cdots g_p = e$ becomes $a^p = e$.

The tuple $(e, e, \ldots, e)$ is always a fixed point. Since $|X^{\langle \sigma \rangle}| \geq 1$ and $p$ divides $|X^{\langle \sigma \rangle}|$, we have $|X^{\langle \sigma \rangle}| \geq p \geq 2$. So there exists a fixed point $(a, a, \ldots, a)$ with $a \neq e$ and $a^p = e$. Since $a \neq e$ and $a^p = e$, the order of $a$ is $p$.

**Theorem 5.2.** Let $G$ be a finite group and $p$ a prime. If $p^k$ divides $|G|$, then the number of solutions to $x^{p^k} = e$ in $G$ is a multiple of $p^k$.

This was conjectured by Frobenius (1895) and first proved by Frobenius (1907). A simpler proof was given by Miller (1916).


<!-- page 23 -->

## 6. More Applications of Group Actions

We now present several further applications of group actions to group theory and number theory.

**Theorem 6.1 (Wilson's Theorem).** If $p$ is prime, then $(p-1)! \equiv -1 \pmod{p}$.

*Proof using group actions.* The group $(\mathbf{Z}/p\mathbf{Z})^\times$ is cyclic of order $p-1$. Let $g$ be a generator. The element $g^{(p-1)/2}$ has order 2, and is the unique element of order 2, which is $-1 \pmod{p}$.

Consider the action of $\langle -1 \rangle = \{1, -1\}$ on $(\mathbf{Z}/p\mathbf{Z})^\times$ by multiplication. The fixed points are elements $a$ with $-a \equiv a \pmod{p}$, i.e., $2a \equiv 0 \pmod{p}$, so $a \equiv 0$. But $0 \notin (\mathbf{Z}/p\mathbf{Z})^\times$. Wait, the fixed points are $a$ with $(-1) \cdot a = a$, i.e., $-a = a$, so $a = 0$. Since $a \in (\mathbf{Z}/p\mathbf{Z})^\times$, there are no fixed points.

Actually, let me use a more direct approach. In $(\mathbf{Z}/p\mathbf{Z})^\times$, pair each element with its inverse. The only elements that are their own inverse are $1$ and $-1$ (since $a^2 \equiv 1 \pmod{p}$ implies $a \equiv \pm 1$). So:
$$(p-1)! = \prod_{a=1}^{p-1} a = 1 \cdot (-1) \cdot \prod_{\substack{a=2 \ a \neq p-1}}^{p-2} a = (-1) \cdot 1 = -1 \pmod{p}$$
since the remaining elements pair up into pairs $(a, a^{-1})$ with product 1.

**Theorem 6.2.** Let $G$ be a finite group and $H$ a subgroup. Then $[G:H]$ divides $|G|$.

*Proof.* Consider the action of $G$ on the left cosets $G/H$ by left multiplication. This gives a homomorphism $\varphi : G \to S_n$ where $n = [G:H]$. Let $K = \ker \varphi$. Then $K$ is the largest normal subgroup of $G$ contained in $H$ (called the **core** of $H$, denoted $\text{core}(H)$).

By the first isomorphism theorem, $G/K$ embeds in $S_n$, so $|G/K|$ divides $n!$. Also, $[G:H] = [G/K : H/K]$, and $H/K$ is a subgroup of $G/K$. By Lagrange's theorem, $[G/K : H/K]$ divides $|G/K|$. Since $[G:H] = [G/K : H/K]$, we conclude $[G:H]$ divides $|G/K|$, which divides $|G|$.

**Theorem 6.3.** If $|G| = 2m$ where $m$ is odd, then $G$ has a normal subgroup of order $m$ (and index 2).

*Proof.* By Cauchy's theorem, $G$ has an element $g_0$ of order 2. Under the left regular representation $\varphi : G \to S_{2m}$ (from Cayley's theorem), $\varphi(g_0)$ is a permutation of the $2m$ elements of $G$.

The permutation $\varphi(g_0)$ acts by left multiplication by $g_0$. Since $g_0$ has order 2, each cycle of $\varphi(g_0)$ has length 1 or 2. The fixed points are elements $g$ with $g_0 g = g$, i.e., $g_0 = e$, which is impossible. So $\varphi(g_0)$ has no fixed points, and consists of $m$ disjoint transpositions.

The sign of a transposition is $-1$, so $\text{sgn}(\varphi(g_0)) = (-1)^m = -1$ (since $m$ is odd).

Thus $\varphi(g_0) \notin A_{2m}$. Consider the homomorphism $\text{sgn} \circ \varphi : G \to \{\pm 1\}$. Since $\text{sgn}(\varphi(g_0)) = -1$, this homomorphism is surjective. Its kernel $N$ is a normal subgroup of $G$ of index 2, so $|N| = m$.


**Theorem 6.4.** Let $G$ be a finite group of order $n$ and let $p$ be a prime. The number of subgroups of index $p$ in $G$ is congruent to $1 \pmod{p}$ if $G$ has a normal subgroup of index $p$, and is congruent to $0 \pmod{p}$ otherwise. More precisely, if $r$ is the number of normal subgroups of index $p$, then the total number of subgroups of index $p$ is congruent to $r \pmod{p}$.

*Proof.* Let $\mathcal{S}$ be the set of subgroups of index $p$ in $G$. The group $G$ acts on $\mathcal{S}$ by conjugation: $g \cdot H = gHg^{-1}$. This is well-defined since conjugation is an automorphism, so $[G : gHg^{-1}] = [G : H] = p$.

The fixed points of this action are the normal subgroups of index $p$. Let $r$ be the number of such subgroups.

For any $H \in \mathcal{S}$, $H$ has index $p$ in $G$. The stabilizer of $H$ under conjugation is $N_G(H)$, the normalizer of $H$. Since $H \leq N_G(H) \leq G$ and $[G:H] = p$ is prime, either $N_G(H) = H$ or $N_G(H) = G$.

If $N_G(H) = G$, then $H$ is normal in $G$, and the orbit of $H$ has size 1.

If $N_G(H) = H$, then the orbit of $H$ has size $[G : N_G(H)] = [G : H] = p$.

So the non-fixed orbits all have size $p$. By Theorem 4.1 (or just counting):
$$|\mathcal{S}| = r + (\text{sum of sizes of non-trivial orbits}) \equiv r \pmod{p}.$$

**Theorem 6.5 (Frobenius).** Let $G$ be a group of order $p^n$ and let $1 \leq k \leq n$. The number of subgroups of $G$ of order $p^k$ is congruent to $1 \pmod{p}$.

*Proof.* Let $\mathcal{S}$ be the set of subgroups of order $p^k$. The group $G$ acts on $\mathcal{S}$ by conjugation. The fixed points are the normal subgroups of order $p^k$.

For a non-fixed subgroup $H$, the orbit size is $[G : N_G(H)]$. Since $H \leq N_G(H)$ and $H$ is not normal, $N_G(H) \neq G$. Since $|G| = p^n$, we have $|N_G(H)| = p^j$ with $k \leq j < n$, so the orbit size $p^{n-j}$ is divisible by $p$.

By Theorem 4.1, $|\mathcal{S}| \equiv |\mathcal{S}^G| \pmod{p}$, where $\mathcal{S}^G$ is the set of normal subgroups of order $p^k$.

To complete the proof, we need to show $|\mathcal{S}^G| \equiv 1 \pmod{p}$. This follows by induction on $n$, using the fact that $G$ has a normal subgroup of order $p$ (from Corollary 4.3) and applying the correspondence theorem.

<!-- page 28 -->

## Appendix A: Applications to Number Theory

We collect here several number-theoretic results that can be proved using group actions.

**Theorem A.1 (Fermat's Little Theorem).** If $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$.

*Proof.* The group $(\mathbf{Z}/p\mathbf{Z})^\times$ has order $p-1$. By Lagrange's theorem, $a^{p-1} = 1$ in this group for any $a$.

**Theorem A.2 (Wilson's Theorem).** If $p$ is prime, then $(p-1)! \equiv -1 \pmod{p}$.

*Proof.* In $(\mathbf{Z}/p\mathbf{Z})^\times$, pair each element with its inverse. The only self-inverse elements are $1$ and $-1$. All other elements pair up, so $(p-1)! \equiv 1 \cdot (-1) = -1 \pmod{p}$.

**Theorem A.3 (Lucas' Theorem).** Let $p$ be prime. For $0 \leq r \leq m$,
$$\binom{mp}{rp} \equiv \binom{m}{r} \pmod{p}.$$

*Proof.* Let $\mathbf{Z}/p\mathbf{Z}$ act on the set $\{1, 2, \ldots, mp\}$ by $k \mapsto k + 1 \pmod{p}$ (within each block of $p$). More precisely, write $\{1, \ldots, mp\}$ as $m$ blocks of $p$ elements: $B_i = \{(i-1)p + 1, \ldots, ip\}$ for $i = 1, \ldots, m$. Let $\mathbf{Z}/p\mathbf{Z}$ act on each block by cyclic shift.

This induces an action on the set of $rp$-element subsets of $\{1, \ldots, mp\}$. The number of such subsets is $\binom{mp}{rp}$.

A subset $S$ of size $rp$ is a fixed point if and only if it is a union of complete orbits of the action. Each orbit is a complete block $B_i$ (of size $p$). So $S$ must be a union of $r$ blocks out of $m$. The number of such subsets is $\binom{m}{r}$.

By Theorem 4.1: $\binom{mp}{rp} \equiv \binom{m}{r} \pmod{p}$.


<!-- page 29 -->

## Appendix B: Applications to Physics

Group actions play a fundamental role in physics, particularly in the study of symmetry. We discuss two important examples: the Galilean group and the Poincare group.

### B.1 The Galilean Group

In Newtonian mechanics, the **Galilean group** is the group of transformations between inertial reference frames. These transformations preserve the laws of motion (Newton's laws).

A Galilean transformation has the form:
$$\mathbf{x}' = R\mathbf{x} + \mathbf{v}t + \mathbf{a}, \quad t' = t + b$$
where:
- $R \in O(3)$ is a rotation (or reflection),
- $\mathbf{v} \in \mathbf{R}^3$ is a boost velocity,
- $\mathbf{a} \in \mathbf{R}^3$ is a spatial translation,
- $b \in \mathbf{R}$ is a time translation.

The Galilean group $\text{Gal}$ can be written as a set of tuples $(R, \mathbf{v}, \mathbf{a}, b)$ with the group operation:
$$(R_2, \mathbf{v}_2, \mathbf{a}_2, b_2) \circ (R_1, \mathbf{v}_1, \mathbf{a}_1, b_1) = (R_2 R_1, R_2 \mathbf{v}_1 + \mathbf{v}_2, R_2 \mathbf{a}_1 + \mathbf{v}_2 b_1 + \mathbf{a}_2, b_1 + b_2).$$

This forms a group with identity $(I, \mathbf{0}, \mathbf{0}, 0)$ and inverse:
$$(R, \mathbf{v}, \mathbf{a}, b)^{-1} = (R^{-1}, -R^{-1}\mathbf{v}, -R^{-1}(\mathbf{a} - \mathbf{v}b), -b).$$

The Galilean group acts on Newtonian spacetime $\mathbf{R}^3 \times \mathbf{R}$ by:
$$(R, \mathbf{v}, \mathbf{a}, b) \cdot (\mathbf{x}, t) = (R\mathbf{x} + \mathbf{v}t + \mathbf{a}, t + b).$$

The Galilean group is a 10-dimensional Lie group: 3 parameters for rotations, 3 for boosts, 3 for spatial translations, and 1 for time translation.

**Physical significance:** The Galilean group encodes the symmetries of Newtonian mechanics:
- Rotational invariance: the laws of physics are the same in all directions.
- Boost invariance: the laws of physics are the same in all inertial frames.
- Spatial translation invariance: the laws of physics are the same at all locations.
- Time translation invariance: the laws of physics are the same at all times.

By Noether's theorem, each continuous symmetry corresponds to a conservation law:
- Rotational symmetry $\leftrightarrow$ conservation of angular momentum.
- Boost symmetry $\leftrightarrow$ center of mass motion.
- Spatial translation $\leftrightarrow$ conservation of momentum.
- Time translation $\leftrightarrow$ conservation of energy.

### B.2 The Poincare Group

In special relativity, the role of the Galilean group is played by the **Poincare group**. This is the group of isometries of Minkowski spacetime.

Minkowski spacetime is $\mathbf{R}^4$ with coordinates $(t, x, y, z)$ and the Minkowski metric:
$$ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2.$$

The Poincare group consists of transformations preserving this metric:
$$x'^\mu = \Lambda^\mu_{\ \nu} x^\nu + a^\mu$$
where $\Lambda \in O(1, 3)$ is a Lorentz transformation and $a^\mu \in \mathbf{R}^4$ is a spacetime translation.

The Lorentz group $O(1, 3)$ includes:
- Spatial rotations $SO(3)$ (3 parameters),
- Boosts (3 parameters),
- Parity $P$ (spatial inversion),
- Time reversal $T$.

The Poincare group is a 10-dimensional Lie group, like the Galilean group. However, the algebraic structure is quite different.

**Key differences from the Galilean group:**
- The Galilean group has a normal subgroup of time translations (absolute time).
- The Poincare group mixes space and time through boosts.
- The Galilean group is a solvable group (in its abelian part).
- The Poincare group has a more complex structure due to the non-compactness of boosts.

**Physical significance:** The Poincare group encodes the symmetries of special relativity and quantum field theory. By Wigner's classification (1939), the irreducible representations of the Poincare group correspond to elementary particles, characterized by:
- Mass $m$ (from the Casimir operator $P_\mu P^\mu = -m^2 c^2$),
- Spin $s$ (from the Pauli-Lubanski pseudovector $W_\mu$).

The connection between group actions and physics is deep and fundamental. Symmetry groups act on the space of physical states, and the irreducible representations of these groups classify the possible types of particles and their properties.


<!-- page 33 -->

## References

1. Keith Conrad, *Group actions*, https://kconrad.math.uconn.edu/blurbs/grouptheory/gpaction.pdf
2. Keith Conrad, *The symmetric group*, https://kconrad.math.uconn.edu/blurbs/grouptheory/Sn.pdf
3. Keith Conrad, *The sign of a permutation*, https://kconrad.math.uconn.edu/blurbs/grouptheory/sign.pdf
4. Keith Conrad, *Cauchy's theorem for abelian groups*, https://kconrad.math.uconn.edu/blurbs/grouptheory/cauchyab.pdf
5. John McKay, "Another proof of Cauchy's group theorem," *American Mathematical Monthly*, Vol. 66, No. 2 (1959), p. 119.
6. James E. Humphreys, *A Course in Group Theory*, Oxford Graduate Texts in Mathematics, Vol. 4, Oxford University Press, 1996.
7. Joseph J. Rotman, *An Introduction to the Theory of Groups*, 4th edition, Springer-Verlag, 1995.
