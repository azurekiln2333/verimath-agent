# Splitting of Short Exact Sequences for Groups

> **Source**: https://kconrad.math.uconn.edu/blurbs/splittinggp.pdf
> **Author**: Keith Conrad
> **Topic**: group_theory

<!-- page 1 -->

## 1. Introduction

A sequence of groups and group homomorphisms

$$H \xrightarrow{\alpha} G \xrightarrow{\beta} K$$

is called *exact* at $G$ if $\operatorname{im} \alpha = \ker \beta$. This means two things: the image of $\alpha$ is killed by $\beta$ ($\beta(\alpha(h)) = 1$ for all $h \in H$), so $\operatorname{im} \alpha \subset \ker \beta$, and also *only* the image of $\alpha$ is killed by $\beta$ (if $\beta(g) = 1$ then $g = \alpha(h)$ for some $h$), so $\ker \beta \subset \operatorname{im} \alpha$. For example, to say $1 \to G \xrightarrow{f} K$ is exact at $G$ means $f$ is injective, and to say $H \xrightarrow{f} G \to 1$ is exact at $G$ means $f$ is surjective. There is no need to label the homomorphisms coming out of 1 or going to 1 since there is only one possible choice. If the group operations are written additively, we may use 0 in place of 1 for the trivial group.

A *short exact sequence* of groups is a sequence of groups and group homomorphisms

$$(1.1) \quad 1 \longrightarrow H \xrightarrow{\alpha} G \xrightarrow{\beta} K \longrightarrow 1$$

which is exact at $H$, $G$, and $K$. That means $\alpha$ is injective, $\beta$ is surjective, and $\operatorname{im} \alpha = \ker \beta$.

A more general exact sequence can have lots of terms:

$$(1.2) \quad G_1 \xrightarrow{\alpha_1} G_2 \xrightarrow{\alpha_2} \cdots \xrightarrow{\alpha_{n-1}} G_n,$$

and it must be exact at each $G_i$ for $1 < i < n$. Exact sequences can also be of infinite length in one or both directions. We will only deal with short exact sequences here.

Exact sequences first arose in algebraic topology, and the later development of homological algebra (the type of algebra underlying algebraic topology) spread exact sequences into the rest of mathematics.

**Example 1.1.** The determinant on $\mathrm{GL}_2(\mathbf{R})$ gives rise to a short exact sequence

$$1 \longrightarrow \mathrm{SL}_2(\mathbf{R}) \longrightarrow \mathrm{GL}_2(\mathbf{R}) \xrightarrow{\det} \mathbf{R}^\times \longrightarrow 1.$$

**Example 1.2.** When $N \triangleleft G$ we have a short exact sequence

$$(1.3) \quad 1 \longrightarrow N \longrightarrow G \longrightarrow G/N \longrightarrow 1,$$

where the map from $N$ to $G$ is inclusion, and the map from $G$ to $G/N$ is reduction mod $N$.

This example is the prototype for all short exact sequences, as we'll see below.

**Example 1.3.** For two groups $H$ and $K$, the direct product $H \times K$ fits into the short exact sequence

$$1 \longrightarrow H \longrightarrow H \times K \longrightarrow K \longrightarrow 1,$$

where the map out of $H$ is embedding to the first factor ($h \mapsto (h, 1)$) and the map out of $H \times K$ is projection to the second factor ($(h, k) \mapsto k$).

<!-- page 2 -->

**Example 1.4.** For two groups $H$ and $K$, together with an action of $K$ on $H$ by automorphisms (a homomorphism $\varphi \colon K \to \operatorname{Aut}(H)$), the semidirect product $H \rtimes_\varphi K$ fits into the short exact sequence

$$1 \longrightarrow H \longrightarrow H \rtimes_\varphi K \longrightarrow K \longrightarrow 1,$$

where the maps are the same as in the previous example: $h \mapsto (h, 1)$ and $(h, k) \mapsto k$.

Every short exact sequence (1.1) is a disguised form of (1.3). Indeed, even though in (1.1) the group $H$ may not literally be a subgroup of $G$ and the group $K$ may not literally be a quotient group of $G$, $\alpha$ restricts to an isomorphism of $H$ with the subgroup $\alpha(H) ( = \ker \beta)$ of $G$ and $\beta$ induces an isomorphism $\overline{\beta}$ of the quotient group $G/\alpha(H) = G/\ker \beta$ with $K$. Therefore we can place the general short exact sequence (1.1) and a short exact sequence of the type (1.3) in a commutative diagram

$$(1.4) \quad \begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \alpha & & \downarrow \mathrm{id} & & \downarrow \overline{\beta} & & \\ 1 & \longrightarrow & \alpha(H) & \longrightarrow & G & \longrightarrow & G/\ker \beta & \longrightarrow & 1 \end{array}$$

where the bottom short exact sequence is a special case of (1.3). The vertical maps are all isomorphisms, and in this sense (1.1) looks like (1.3): they are linked to each other through compatible isomorphisms of groups in the same positions in the two short exact sequences. (The compatibility of the isomorphisms simply means the diagram (1.4) commutes.)

In Section 2 we will look at some more examples of short exact sequences. Then in Section 3, which is the most important part, we will see how direct products and semidirect products of groups can be characterized in terms of short exact sequences with extra structure. Section 4 discusses the idea of two short exact sequences being alike in broad terms.

## 2. Examples

When $N \triangleleft G$, knowing $N$ and $G/N$ does not usually tell us what $G$ is. That is, nonisomorphic groups can have isomorphic normal subgroups with isomorphic quotient groups. For example, $D_4 \not\cong Q_8$ but $\langle r^2 \rangle \cong \{\pm 1\} (\cong \mathbf{Z}/2\mathbf{Z})$ and $D_4/\langle r^2 \rangle \cong Q_8/\{\pm 1\} (\cong (\mathbf{Z}/2\mathbf{Z})^2)$. In terms of short exact sequences, the two short exact sequences

$$1 \longrightarrow \langle r^2 \rangle \longrightarrow D_4 \longrightarrow D_4/\langle r^2 \rangle \longrightarrow 1$$

and

$$(2.1) \quad 1 \longrightarrow \{\pm 1\} \longrightarrow Q_8 \longrightarrow Q_8/\{\pm 1\} \longrightarrow 1$$

have isomorphic first groups and isomorphic third groups, but nonisomorphic middle groups. Here is a third example like these, with an abelian group in the middle:

$$0 \longrightarrow \mathbf{Z}/2\mathbf{Z} \longrightarrow \mathbf{Z}/2\mathbf{Z} \times (\mathbf{Z}/2\mathbf{Z})^2 \longrightarrow (\mathbf{Z}/2\mathbf{Z})^2 \longrightarrow 0.$$

This is the short exact sequence for a direct product, as in Example 1.3.

Here are two examples of short exact sequences with first group $\mathbf{Z}/4\mathbf{Z}$ and third group $\mathbf{Z}/2\mathbf{Z}$, but nonisomorphic groups in the middle:

$$0 \longrightarrow \mathbf{Z}/4\mathbf{Z} \longrightarrow \mathbf{Z}/4\mathbf{Z} \times \mathbf{Z}/2\mathbf{Z} \longrightarrow \mathbf{Z}/2\mathbf{Z} \longrightarrow 0$$

$$0 \longrightarrow \mathbf{Z}/4\mathbf{Z} \longrightarrow \mathbf{Z}/8\mathbf{Z} \longrightarrow \mathbf{Z}/2\mathbf{Z} \longrightarrow 0,$$

where the map $\mathbf{Z}/4\mathbf{Z} \to \mathbf{Z}/8\mathbf{Z}$ in the second short exact sequence is doubling ($x \bmod 4 \mapsto 2x \bmod 8$). The other maps are all the obvious ones.

<!-- page 3 -->

Here are two short exact sequences with first and third groups equal to $\mu_m$ ($m > 1$) but nonisomorphic groups in the middle:

$$1 \longrightarrow \mu_m \longrightarrow \mu_m \times \mu_m \longrightarrow \mu_m \longrightarrow 1$$

and

$$1 \longrightarrow \mu_m \xrightarrow{\iota} \mu_{m^2} \xrightarrow{z \mapsto z^m} \mu_m \longrightarrow 1.$$

The first short exact sequence is the usual one for a direct product. In the second short exact sequence, $\iota$ is the inclusion. The middle groups $\mu_m \times \mu_m$ and $\mu_{m^2}$ are not isomorphic since $\mu_m \times \mu_m$ is not cyclic (no element of order $m^2$).

## 3. Direct and Semidirect Products

For two groups $H$ and $K$, an important "lifting" problem is the determination of all groups $G$ having a normal subgroup isomorphic to $H$ and corresponding quotient group isomorphic to $K$. Such $G$ are the groups that fit into a short exact sequence $1 \to H \to G \to K \to 1$. There is always at least one such $G$, namely $H \times K$. More generally, a semidirect product $H \rtimes_\varphi K$ always sits in a short exact sequence having kernel $H$ and image $K$ (Example 1.4). Not all short exact sequences arise from semidirect products.

**Example 3.1.** In the short exact sequence (2.1), $Q_8$ is not isomorphic to a semidirect product of $\{\pm 1\}$ and $Q_8/\{\pm 1\} \cong (\mathbf{Z}/2\mathbf{Z})^2$ since such a semidirect product has more than 1 element of order 2 while $Q_8$ has only one element of order 2.

Since semidirect products are "known," short exact sequences made with them are considered "known" (even though semidirect products may seem like a subtle way to create groups). It is important to recognize if a short exact sequence $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ is essentially that for a direct product $H \times K$ or semidirect product $H \rtimes_\varphi K$. The next two theorems give such criteria in terms of a left inverse for $\alpha$ and a right inverse for $\beta$.

**Theorem 3.2.** *Let $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ be a short exact sequence of groups. The following are equivalent:*

*(1) There is a homomorphism $\alpha' \colon G \to H$ such that $\alpha'(\alpha(h)) = h$ for all $h \in H$.*

*(2) There is an isomorphism $\theta \colon G \to H \times K$ such that the diagram*

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \times K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

*commutes, where the bottom row is the short exact sequence for a direct product.*

The commutative diagram in (2) says that $\theta$ identifies $\alpha$ with the embedding $H \to H \times K$ and $\beta$ with the projection $H \times K \to K$. So the point of (2) is not simply that $G$ is isomorphic to $H \times K$, but it is in a way that turns $\alpha$ and $\beta$ into the standard maps from $H$ to $H \times K$ and from $H \times K$ to $K$.

The key point of (1) is that $\alpha'$ is a homomorphism. Merely from $\alpha$ being injective, there is a *function* $\alpha' \colon G \to H$ such that $\alpha'(\alpha(h)) = h$ for all $h$, for instance the function

$$\alpha'(g) = \begin{cases} 1, & \text{if } g \notin \alpha(H), \\ h, & \text{if } g = \alpha(h). \end{cases}$$

<!-- page 4 -->

But this $\alpha'$ is almost surely not a homomorphism.

*Proof.* (1) $\Rightarrow$ (2): Define $\theta \colon G \to H \times K$ by

$$\theta(g) = (\alpha'(g), \beta(g)).$$

This is a homomorphism since $\alpha'$ and $\beta$ are homomorphisms. To see $\theta$ is injective, suppose $\theta(g) = (1, 1)$, so $\alpha'(g) = 1$ and $\beta(g) = 1$. From exactness at $G$, the condition $\beta(g) = 1$ implies $g = \alpha(h)$ for some $h \in H$. Then $1 = \alpha'(g) = \alpha'(\alpha(h)) = h$, so $g = \alpha(h) = \alpha(1) = 1$.

To show $\theta$ is surjective, let $(h, k) \in H \times K$. Since $\beta$ is onto, $k = \beta(g)$ for some $g \in G$. Since $\ker \beta = \operatorname{im} \alpha$, the general inverse image of $k$ under $\beta$ is $g\alpha(x)$ for $x \in H$. We want to find $x \in H$ such that $\alpha'(g\alpha(x)) = h$, so then $\theta(g\alpha(x)) = (h, k)$. Since $\alpha'$ is a homomorphism, the condition $\alpha'(g\alpha(x)) = h$ is equivalent to $\alpha'(g)x = h$, so *define* $x = \alpha'(g)^{-1}h$. Then

$$\theta(g\alpha(x)) = (\alpha'(g\alpha(x)), \beta(g\alpha(x))) = (h, k),$$

so $\theta$ is an isomorphism from $G$ to $H \times K$.

Next, we want to check the diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \times K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

commutes. In the first square

$$\begin{array}{ccc} H & \xrightarrow{\alpha} & G \\ \downarrow \mathrm{id} & & \downarrow \theta \\ H & \longrightarrow & H \times K \end{array}$$

taking $h \in H$ along the top and right has the effect $h \mapsto \alpha(h) \mapsto (\alpha'(\alpha(h)), \beta(\alpha(h))) = (h, 1)$, which is also the result of taking $h$ along the left and bottom. In the second square

$$\begin{array}{ccc} G & \xrightarrow{\beta} & K \\ \downarrow \theta & & \downarrow \mathrm{id} \\ H \times K & \longrightarrow & K \end{array}$$

taking $g \in G$ along the top and right has the effect $g \mapsto \beta(g) \mapsto \beta(g)$, and going along the left and bottom leads to $g \mapsto (\alpha'(g), \beta(g)) \mapsto \beta(g)$. So the diagram commutes.

(2) $\Rightarrow$ (1): Suppose there is an isomorphism $\theta \colon G \to H \times K$ such that

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \times K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

commutes. For $g \in G$, $\theta(g) \in H \times K$ has second coordinate $\beta(g)$ from commutativity of the second square. Let $\alpha'(g)$ denote the first coordinate:

$$\theta(g) = (\alpha'(g), \beta(g)).$$

<!-- page 5 -->

Then $\alpha' \colon G \to H$ is a function and $\theta$ is a homomorphism, so $\alpha'$ is a homomorphism. The commutativity of the first square implies $\theta(\alpha(h)) = (h, 1)$, so $(\alpha'(\alpha(h)), \beta(\alpha(h))) = (h, 1)$, so $\alpha'(\alpha(h)) = h$ for all $h \in H$.

The proof shows that the homomorphisms $\alpha'$ in (1) and the isomorphisms $\theta$ in (2) are in bijection by the formula $\theta(g) = (\alpha'(g), \beta(g))$ for all $g \in G$.

**Theorem 3.3.** *Let $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ be a short exact sequence. The following are equivalent:*

*(1) There is a homomorphism $\beta' \colon K \to G$ such that $\beta(\beta'(k)) = k$ for all $k \in K$.*

*(2) There is a homomorphism $\varphi \colon K \to \operatorname{Aut}(H)$ and an isomorphism $\theta \colon G \to H \rtimes_\varphi K$ such that the diagram*

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \rtimes_\varphi K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

*commutes, where the bottom short exact sequence is the usual one for a semidirect product.*

As with Theorem 3.2, the key part of (1) is that $\beta'$ is a homomorphism. From surjectivity of $\beta$, there is a function $\beta' \colon K \to G$ such that $\beta(\beta'(k)) = k$ for all $k \in K$, for instance set $\beta'(k)$ for each $k$ to be a solution[^1] to $\beta(g) = k$. But usually this $\beta'$ is not a *homomorphism*.

*Proof.* (1) $\Rightarrow$ (2): From the homomorphism $\beta'$ we have to create an action $\varphi$ of $K$ on $H$ by automorphisms and an isomorphism of $G$ with $H \rtimes_\varphi K$. Using $\beta'$, we can make $K$ act on $H$ using conjugation in $G$: for $k \in K$ and $h \in H$, $\beta'(k)\alpha(h)\beta'(k^{-1}) \in \ker \beta$ since

$$\beta(\beta'(k)\alpha(h)\beta'(k^{-1})) = \beta(\beta'(k))\beta(\alpha(h))\beta(\beta'(k^{-1})) = k \cdot 1 \cdot k^{-1} = 1.$$

Since $\ker \beta = \operatorname{im} \alpha$, we can write $\beta'(k)\alpha(h)\beta'(k^{-1}) = \alpha(h')$ for an $h' \in H$, and $h'$ is unique since $\alpha$ is injective. This $h'$ is determined by $h$ and $k$. We write $h'$ as $\varphi_k(h)$, so $\varphi_k(h)$ denotes the unique element of $H$ such that

$$(3.1) \quad \beta'(k)\alpha(h)\beta'(k)^{-1} = \alpha(\varphi_k(h)),$$

where $\beta'(k^{-1}) = \beta'(k)^{-1}$ since $\beta'$ is a homomorphism. Since $\varphi_k(h) \in H$, we get a function $\varphi_k \colon H \to H$. We will show $\varphi_k \in \operatorname{Aut}(H)$ and $k \mapsto \varphi_k$ is a homomorphism $K \to \operatorname{Aut}(H)$.

First, setting $k = 1$ in (3.1), $\alpha(h) = \alpha(\varphi_1(h))$, so $\varphi_1(h) = h$ for all $h \in H$. Thus $\varphi_1 = \mathrm{id}_H$. Next we check $\varphi_k \colon H \to H$ is a homomorphism for each $k \in K$. For $h_1$ and $h_2$ in $H$, $\varphi_k(h_1 h_2)$ is characterized by the equation $\beta'(k)\alpha(h_1 h_2)\beta'(k)^{-1} = \alpha(\varphi_k(h_1 h_2))$. The left side is

$$\begin{aligned} \beta'(k)\alpha(h_1)\alpha(h_2)\beta'(k)^{-1} &= \beta'(k)\alpha(h_1)\beta'(k)^{-1}\beta'(k)\alpha(h_2)\beta'(k)^{-1} \\ &= \alpha(\varphi_k(h_1))\alpha(\varphi_k(h_2)) \\ &= \alpha(\varphi_k(h_1)\varphi_k(h_2)), \end{aligned}$$

so by injectivity of $\alpha$ we have $\varphi_k(h_1)\varphi_k(h_2) = \varphi_k(h_1 h_2)$.

Next we show $\varphi_{k_1} \circ \varphi_{k_2} = \varphi_{k_1 k_2}$. For $h \in H$, $\varphi_{k_1 k_2}(h)$ is characterized by the equation

$$\beta'(k_1 k_2)\alpha(h)\beta'(k_1 k_2)^{-1} = \alpha(\varphi_{k_1 k_2}(h)),$$

<!-- page 6 -->

and the left side is

$$\begin{aligned} \beta'(k_1)\beta'(k_2)\alpha(h)\beta'(k_2)^{-1}\beta'(k_1)^{-1} &= \beta'(k_1)\alpha(\varphi_{k_2}(h))\beta'(k_1)^{-1} \quad \text{by (3.1)} \\ &= \alpha(\varphi_{k_1}(\varphi_{k_2}(h))), \end{aligned}$$

so $\varphi_{k_1}(\varphi_{k_2}(h)) = \varphi_{k_1 k_2}(h)$, so $\varphi_{k_1} \circ \varphi_{k_2} = \varphi_{k_1 k_2}$. In particular, $\varphi_k \circ \varphi_{k^{-1}} = \varphi_1$ and $\varphi_{k^{-1}} \circ \varphi_k = \varphi_1$, so $\varphi_k \in \operatorname{Aut}(H)$ and $k \mapsto \varphi_k$ is a homomorphism $K \to \operatorname{Aut}(H)$. We have proved that (3.1) provides an action of $K$ on $H$ by automorphisms, so we have the semidirect product $H \rtimes_\varphi K$.

To get an isomorphism $G \to H \rtimes_\varphi K$, it is easier to go in the other direction. Let $\gamma \colon H \rtimes_\varphi K \to G$ by

$$\gamma(h, k) = \alpha(h)\beta'(k).$$

To check $\gamma$ is a homomorphism,

$$\begin{aligned} \gamma((h_1, k_1)(h_2, k_2)) &= \gamma(h_1 \varphi_{k_1}(h_2), k_1 k_2) \\ &= \alpha(h_1 \varphi_{k_1}(h_2))\beta'(k_1 k_2) \\ &= \alpha(h_1)\alpha(\varphi_{k_1}(h_2))\beta'(k_1)\beta'(k_2) \\ &= \alpha(h_1)(\beta'(k_1)\alpha(h_2)\beta'(k_1)^{-1})\beta'(k_1)\beta'(k_2) \quad \text{by (3.1)} \\ &= \alpha(h_1)\beta'(k_1)\alpha(h_2)\beta'(k_2) \\ &= \gamma(h_1, k_1)\gamma(h_2, k_2). \end{aligned}$$

To show $\gamma$ is injective, if $\gamma(h, k) = 1$ then $\alpha(h)\beta'(k) = 1$. Applying $\beta$ to both sides, $\beta(\alpha(h))\beta(\beta'(k)) = \beta(1) = 1$, so $k = 1$. Then $\alpha(h) \cdot 1 = 1$, so $h = 1$ since $\alpha$ is injective.

To show $\gamma$ is surjective, pick $g \in G$. We want to find $h \in H$ and $k \in K$ such that $\alpha(h)\beta'(k) = g$. Applying $\beta$ to both sides, $\beta(\alpha(h))\beta(\beta'(k)) = \beta(g)$, so $k = \beta(g)$. So we *define* $k := \beta(g)$ and then ask if there is $h \in H$ such that $\alpha(h) = g\beta'(k^{-1}) = g\beta'(\beta(g)^{-1})$. Since $\operatorname{im} \alpha = \ker \beta$, whether or not there is such an $h$ is equivalent to checking $g\beta'(\beta(g)^{-1}) \in \ker \beta$:

$$\begin{aligned} \beta(g\beta'(\beta(g)^{-1})) &= \beta(g)\beta(\beta'(\beta(g)^{-1})) \\ &= \beta(g)\beta(g)^{-1} \\ &= 1. \end{aligned}$$

Thus $\gamma \colon H \rtimes_\varphi K \to G$ is an isomorphism. Let $\theta = \gamma^{-1}$ be the inverse isomorphism.

Finally, to show the diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \rtimes_\varphi K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

commutes, it is equivalent to show the "flipped" diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \uparrow \mathrm{id} & & \uparrow \gamma & & \uparrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \rtimes_\varphi K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

commutes. For $h \in H$, going around the first square along the left and top has the effect $h \mapsto h \mapsto \alpha(h)$, and going around the other way has the effect $h \mapsto (h, 1) \mapsto \gamma(h, 1) = \alpha(h)\beta'(1) = \alpha(h)$. In the second square, for $(h, k) \in H \rtimes_\varphi K$ going around the left and top has the effect $(h, k) \mapsto \beta(\gamma(h, k)) = \beta(\alpha(h))\beta(\beta'(k)) = k$, while going around the other way has the effect $(h, k) \mapsto k \mapsto k$.

<!-- page 7 -->

(2) $\Rightarrow$ (1): In the proof that (1) $\Rightarrow$ (2), $\gamma(h, k) = \alpha(h)\beta'(k)$, so $\gamma(1, k) = \beta'(k)$. This *suggests* that when we have an isomorphism $\theta \colon G \to H \rtimes_\varphi K$ that we define $\beta' \colon K \to G$ by $\beta'(k) = \theta^{-1}(1, k)$. This is a homomorphism since $k \mapsto (1, k)$ is a homomorphism and $\theta^{-1}$ is a homomorphism. The composite $\beta(\beta'(k)) = \beta(\theta^{-1}(1, k))$ equals $k$ from commutativity of the diagram

$$\begin{array}{ccc} G & \xrightarrow{\beta} & K \\ \uparrow \theta^{-1} & & \uparrow \mathrm{id} \\ H \rtimes_\varphi K & \longrightarrow & K. \end{array}$$

**Definition 3.4.** A short exact sequence $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ is said to *split* if it fits the conditions of Theorem 3.3, so there is an isomorphism $G \to H \rtimes K$ for some semidirect product structure that makes $\alpha$ look the usual embedding $H \to H \rtimes K$ and makes $\beta$ look like the usual projection $H \rtimes K \to K$.

A split short exact sequence essentially corresponds to the standard short exact sequence for a semidirect product. The short exact sequence with $Q_8$ in (2.1) is not split.

Since $H \rtimes_\varphi K$ might not be isomorphic to $H \times K$, the first conditions in Theorems 3.2 and 3.3 are not equivalent: for a short exact sequence of groups $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$, if there is a homomorphism $\beta' \colon K \to G$ such that $\beta(\beta'(k)) = k$ for all $k$ there need not be a homomorphism $\alpha' \colon G \to H$ such that $\alpha'(\alpha(h)) = h$ for all $h$.

**Example 3.5.** For even $n \geq 6$, let $G = D_n$, $H = \langle r^2, s \rangle$, and $K = \langle rs \rangle$. Since $H$ and $K$ are complementary subgroups of $G$ and $H \triangleleft G$, $G = HK \cong H \rtimes_\varphi K$ where $K$ acts on $H$ by conjugation. Since $H \times K \cong D_{n/2} \times \mathbf{Z}/(2)$, if $n/2$ is even then $H \times K$ has a center of order 4 ($D_{n/2}$ has a center of order 2) while $G$ has a center of order 2, so $G \not\cong H \times K$.

When $G$ is abelian, (3.1) simplifies to $\alpha(h) = \alpha(\varphi_k(h))$ for all $k$ and $h$, so $h = \varphi_k(h)$. Thus $K$ acts trivially on $H$, so $H \rtimes_\varphi K = H \times K$. Therefore Theorems 3.2 and 3.3 provide three equivalent conditions on $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ when $G$ is *abelian*:

(1) There is a homomorphism $\alpha' \colon G \to H$ such that $\alpha'(\alpha(h)) = h$ for all $h \in H$.

(2) There is a homomorphism $\beta' \colon K \to G$ such that $\beta(\beta'(k)) = k$ for all $k \in K$.

(3) There is an isomorphism $\theta \colon G \to H \times K$ such that the diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \longrightarrow & H \times K & \longrightarrow & K & \longrightarrow & 1 \end{array}$$

commutes, where the bottom row is the short exact sequence for a direct product.

## 4. Equivalent Short Exact Sequences

We said in the introduction that every short exact sequence (1.1) is basically like a short exact sequence of type (1.3), and made the idea precise in terms of a commutative diagram (1.4) having both short exact sequences (1.1) and (1.3) appearing in it as the rows, and the columns being isomorphisms. This idea of two short exact sequences being basically alike can be applied more generally. Say $1 \to H_1 \xrightarrow{\alpha_1} G_1 \xrightarrow{\beta_1} K_1 \to 1$ and $1 \to H_2 \xrightarrow{\alpha_2} G_2 \xrightarrow{\beta_2} K_2 \to 1$ are *equivalent* if they fit into a commutative diagram

<!-- page 8 -->

$$(4.1) \quad \begin{array}{ccccccccc} 1 & \longrightarrow & H_1 & \xrightarrow{\alpha_1} & G_1 & \xrightarrow{\beta_1} & K_1 & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & H_2 & \xrightarrow{\alpha_2} & G_2 & \xrightarrow{\beta_2} & K_2 & \longrightarrow & 1 \end{array}$$

where the vertical maps are isomorphisms. For example, (1.4) shows every short exact sequence is equivalent to a short exact sequence of type (1.3). Note that, as in (1.4), we do *not* insist for equivalence of short exact sequences that the first and third isomorphisms in (4.1) are the identity (the first and third groups in each row need not even be equal), unlike for the commutative diagrams in Theorems 3.2 and 3.3. The idea behind the commutativity of (4.1) is that the middle groups $G_1$ and $G_2$ are isomorphic in such a way that the images of the first groups $H_1$ and $H_2$ sit inside the middle groups in similar ways, and the third groups $K_1$ and $K_2$ are homomorphic images of the middle groups in similar ways.

Here is a concrete example of equivalent short exact sequences:

$$(4.2) \quad 1 \longrightarrow A_3 \longrightarrow S_3 \xrightarrow{\operatorname{sgn}} \{\pm 1\} \longrightarrow 1$$

and

$$(4.3) \quad 0 \longrightarrow \mathbf{Z}/3\mathbf{Z} \longrightarrow \operatorname{Aff}(\mathbf{Z}/3\mathbf{Z}) \xrightarrow{\det} (\mathbf{Z}/3\mathbf{Z})^\times \longrightarrow 1,$$

where the first map in (4.2) is inclusion and the first map in (4.3) is $b \mapsto \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$. These are equivalent because there is a commutative diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & A_3 & \longrightarrow & S_3 & \xrightarrow{\operatorname{sgn}} & \{\pm 1\} & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 0 & \longrightarrow & \mathbf{Z}/3\mathbf{Z} & \longrightarrow & \operatorname{Aff}(\mathbf{Z}/3\mathbf{Z}) & \xrightarrow{\det} & (\mathbf{Z}/3\mathbf{Z})^\times & \longrightarrow & 1 \end{array}$$

where (4.2) and (4.3) are the rows and the vertical maps are all isomorphisms.

Theorem 3.2 gives us a condition for detecting when a short exact sequence $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ is equivalent to the usual short exact sequence for $H \times K$ from Example 1.3 with the first and third vertical maps being the identities on $H$ and $K$.

**Example 4.1.** Let $H = K = \mathbf{Z}$ and let $a$ and $b$ be relatively prime integers. We have a short exact sequence

$$0 \longrightarrow \mathbf{Z} \xrightarrow{\alpha} \mathbf{Z} \times \mathbf{Z} \xrightarrow{\beta} \mathbf{Z} \longrightarrow 0$$

where $\alpha(n) = (an, bn)$ and $\beta(x, y) = bx - ay$. (That $\ker \beta \subset \operatorname{im} \alpha$ uses relatively primality of $a$ and $b$.) This is not the usual short exact sequence for $\mathbf{Z} \times \mathbf{Z}$, but it is equivalent to it: there are $u$ and $v$ in $\mathbf{Z}$ such that $1 = au + bv$, and using them we have the commutative diagram

<!-- page 9 -->

$$\begin{array}{ccccccccc} 0 & \longrightarrow & \mathbf{Z} & \xrightarrow{\alpha} & \mathbf{Z} \times \mathbf{Z} & \xrightarrow{\beta} & \mathbf{Z} & \longrightarrow & 0 \\ & & \downarrow \mathrm{id} & & \downarrow \theta & & \downarrow \mathrm{id} & & \\ 0 & \longrightarrow & \mathbf{Z} & \longrightarrow & \mathbf{Z} \times \mathbf{Z} & \longrightarrow & \mathbf{Z} & \longrightarrow & 0 \end{array}$$

where $\theta(x, y) = (ux + vy, bx - ay)$, and the bottom short exact sequence is the usual one for $\mathbf{Z} \times \mathbf{Z}$. The inverse of $\theta$ is $(x, y) \mapsto (ax + vy, bx - uy)$.

Here is a short exact sequence $1 \to H \xrightarrow{\alpha} H \times K \xrightarrow{\beta} K \to 1$ that is not equivalent to the usual one for a direct product.

**Example 4.2.** Let $H = \mathbf{Z}$ and $K = (\mathbf{Z}/m\mathbf{Z})^{\mathbf{N}}$ (countable direct product of copies of $\mathbf{Z}/m\mathbf{Z}$) where $m \geq 2$. We have a short exact sequence

$$(4.4) \quad 0 \longrightarrow \mathbf{Z} \xrightarrow{\alpha} \mathbf{Z} \times (\mathbf{Z}/m\mathbf{Z})^{\mathbf{N}} \xrightarrow{\beta} (\mathbf{Z}/m\mathbf{Z})^{\mathbf{N}} \longrightarrow 0$$

where $\alpha(x) = (mx, \mathbf{0})$ and $\beta(x, \mathbf{y}) = (x \bmod m, \mathbf{y})$. (If $K$ had finitely many coordinates, then to define $\beta(x, \mathbf{y})$ we'd have to do something like drop a coordinate of $\mathbf{y}$ and the condition $\ker \beta \subset \operatorname{im} \alpha$ would fail.) If (4.4) were equivalent to the usual short exact sequence for $\mathbf{Z} \times (\mathbf{Z}/m\mathbf{Z})^{\mathbf{N}}$ then there would be a homomorphism $\alpha' \colon \mathbf{Z} \times (\mathbf{Z}/m\mathbf{Z})^{\mathbf{N}} \to \mathbf{Z}$ such that $\alpha'(\alpha(x)) = x$ for all $x \in \mathbf{Z}$. Then $x = \alpha'(mx, \mathbf{0}) = \alpha'(m(x, \mathbf{0})) = m\alpha'(x, \mathbf{0})$ in $\mathbf{Z}$, which is a contradiction when $x$ is not divisible by $m$ (*e.g.*, $x = 1$). Thus (4.4) is not equivalent to the usual short exact sequence for a direct product.

**Remark 4.3.** It turns out that all short exact sequences $1 \to H \xrightarrow{\alpha} H \times K \xrightarrow{\beta} K \to 1$ with a direct product in the middle are equivalent to the usual short exact sequence in Example 1.3 if (i) $H$ and $K$ are finitely generated abelian groups, as in Example 4.1, or (ii) $H$ and $K$ are finite groups. See https://mathoverflow.net/questions/80002.

Theorem 3.3 tells us when $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ is equivalent to the usual short exact sequence for some semidirect product $H \rtimes_\varphi K$ with the first and third vertical maps being the identities on $H$ and $K$. (The first and third maps being identities is an *extra* condition, not part of the definition of equivalence.)

The notion of equivalent short exact sequences is an equivalence relation: any short exact sequence $1 \to H \xrightarrow{\alpha} G \xrightarrow{\beta} K \to 1$ is equivalent to itself from the commutative diagram

$$(4.5) \quad \begin{array}{ccccccccc} 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \\ & & \downarrow \mathrm{id} & & \downarrow \mathrm{id} & & \downarrow \mathrm{id} & & \\ 1 & \longrightarrow & H & \xrightarrow{\alpha} & G & \xrightarrow{\beta} & K & \longrightarrow & 1 \end{array}$$

and using inverse isomorphisms in the vertical rows of (4.1) gives a commutative diagram where the two rows are interchanged, so the notion of equivalent short exact sequences is symmetric. For transitivity, we can combine two commutative diagrams

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H_1 & \xrightarrow{\alpha_1} & G_1 & \xrightarrow{\beta_1} & K_1 & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & H_2 & \xrightarrow{\alpha_2} & G_2 & \xrightarrow{\beta_2} & K_2 & \longrightarrow & 1 \end{array}$$

<!-- page 10 -->

and

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H_2 & \xrightarrow{\alpha_2} & G_2 & \xrightarrow{\beta_2} & K_2 & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & H_3 & \xrightarrow{\alpha_3} & G_3 & \xrightarrow{\beta_3} & K_3 & \longrightarrow & 1 \end{array}$$

into the commutative diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H_1 & \xrightarrow{\alpha_1} & G_1 & \xrightarrow{\beta_1} & K_1 & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & H_2 & \xrightarrow{\alpha_2} & G_2 & \xrightarrow{\beta_2} & K_2 & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & H_3 & \xrightarrow{\alpha_3} & G_3 & \xrightarrow{\beta_3} & K_3 & \longrightarrow & 1 \end{array}$$

and then use the composite of the pairs of vertical isomorphisms to eliminate the middle row and get the commutative diagram

$$\begin{array}{ccccccccc} 1 & \longrightarrow & H_1 & \xrightarrow{\alpha_1} & G_1 & \xrightarrow{\beta_1} & K_1 & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & H_3 & \xrightarrow{\alpha_3} & G_3 & \xrightarrow{\beta_3} & K_3 & \longrightarrow & 1 \end{array}$$

with isomorphisms as the vertical maps.

Here is the analogue of homomorphisms for short exact sequences. A *morphism* from $1 \to H_1 \xrightarrow{\alpha_1} G_1 \xrightarrow{\beta_1} K_1 \to 1$ to $1 \to H_2 \xrightarrow{\alpha_2} G_2 \xrightarrow{\beta_2} K_2 \to 1$ is a commutative diagram (4.1) where the vertical maps are homomorphisms rather than isomorphisms. An example of a morphism of short exact sequences is (for $m > 1$)

$$\begin{array}{ccccccccc} 1 & \longrightarrow & \mathrm{SL}_2(\mathbf{Z}) & \longrightarrow & \mathrm{GL}_2(\mathbf{Z}) & \xrightarrow{\det} & \{\pm 1\} & \longrightarrow & 1 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 1 & \longrightarrow & \mathrm{SL}_2(\mathbf{Z}/m\mathbf{Z}) & \longrightarrow & \mathrm{GL}_2(\mathbf{Z}/m\mathbf{Z}) & \xrightarrow{\det} & (\mathbf{Z}/m\mathbf{Z})^\times & \longrightarrow & 1, \end{array}$$

where the vertical maps are the natural mod $m$ reduction maps. The identity morphism for a short exact sequence is (4.5). Our argument that equivalence of short exact sequences is transitive also shows how to compose two morphisms to get a third: compose vertical homomorphisms in the same positions in the two diagrams. What we called equivalence of two short exact sequences is the concept of isomorphism: a morphism of short exact sequences that admits an inverse morphism (one whose composite with the original morphism on both sides gives the identity morphism for the two short exact sequences).

[^1]: Here we use the Axiom of Choice.
