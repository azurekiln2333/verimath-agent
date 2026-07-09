# Subgroup Series I

> **Source**: https://kconrad.math.uconn.edu/blurbs/grouptheory/subgpseries1.pdf
> **Author**: Keith Conrad
> **Topic**: group_theory

<!-- page 1 -->

## 1. Introduction

If $N$ is a nontrivial proper normal subgroup of a finite group $G$ then $N$ and $G/N$ are smaller than $G$. While it is false that $G$ can be completely reconstructed from knowledge of $N$ and $G/N$ (see Example 1.1 below), it is nevertheless a standard technique in finite group theory to prove theorems about finite groups by induction on the size of the group and thereby use information about the smaller groups $N$ and $G/N$ to say something about $G$. Instead of using one normal subgroup, we will consider a (finite) series of subgroups

$$\{e\} = G_0 \lhd G_1 \lhd G_2 \lhd \cdots \lhd G_r = G \tag{1.1}$$

or

$$G = G_0 \rhd G_1 \rhd G_2 \rhd \cdots \rhd G_r = \{e\}, \tag{1.2}$$

where each $G_i$ is normal in the succeeding (or preceding) subgroup. The only difference between (1.1) and (1.2) is the indexing, starting from the bottom or the top. Both (1.1) and (1.2) are called *normal series* for $G$.[^1] *Note $\{e\}$ and $G$ are among the $G_i$'s.* We don't assume $G_i \lhd G$, but only that each subgroup is normal in the next larger subgroup (succeeding or preceding, depending on the indexing). The quotients $G_{i+1}/G_i$ of (1.1) and $G_i/G_{i+1}$ of (1.2) are called its *factors*. A normal series is a "filtration" of $G$ rather than a "decomposition" of $G$: it is a way to fill up $G$ rather than a way to break it apart.

**Example 1.1.** For $n \geq 3$, a normal series for $D_n$ is $\{1\} \lhd \langle r \rangle \lhd D_n$, with factors $\langle r \rangle \cong \mathbf{Z}/(n)$ and $D_n/\langle r \rangle \cong \mathbf{Z}/(2)$. A normal series for $\mathbf{Z}/(2n)$ is $\{0\} \lhd \langle 2 \bmod 2n \rangle \lhd \mathbf{Z}/(2n)$, whose factors are cyclic of orders $n$ and $2$. Thus non-isomorphic groups like $D_n$ and $\mathbf{Z}/(2n)$ can have normal series with isomorphic factors.

**Example 1.2.** If $G = H_1 \times H_2$ is a direct product of two groups then a normal series for $G$ is $\{(e,e)\} \lhd H_1 \times \{e\} \lhd H_1 \times H_2$ with factors $H_1 \times \{e\} \cong H_1$ and $(H_1 \times H_2)/(H_1 \times \{e\}) \cong H_2$. Similarly, a 3-fold direct product $H_1 \times H_2 \times H_3$ has the normal series

$$\{(e,e,e)\} \lhd H_1 \times \{e\} \times \{e\} \lhd H_1 \times H_2 \times \{e\} \lhd H_1 \times H_2 \times H_3$$

with successive factors isomorphic to $H_1$, $H_2$, and $H_3$. More generally, a group that is a direct product of finitely many groups admits a normal series whose factors are (isomorphic to) the subgroups appearing in the direct product.

While Example 1.2 shows a finite direct product decomposition of $G$ leads to a normal series for $G$, most normal series do *not* come from a direct product decomposition. For instance, the normal series for $D_n$ in Example 1.1 doesn't come from a direct product decomposition of $D_n$ into cyclic groups of orders 2 and $n$, since such a direct product would be abelian and $D_n$ is nonabelian.

[^1]: People who teach infinite series in calculus may caution students not to use "series" as a synonym for "sequence", but in group theory it is traditional to do exactly that.

<!-- page 2 -->

In Section 2 we will look at some further examples of normal series and state the important Jordan-Holder theorem (it is proved in an appendix). Section 3 will discuss how a normal series for a group becomes a normal series for related groups (subgroups, quotient groups, and direct products). Two special kinds of subgroup series, central and derived series, are the topics of Section 4. All of this general discussion is a prelude to Section 5, where we will examine two classes of groups defined in terms of normal series: nilpotent and solvable groups. Nilpotent groups are always solvable but not conversely.

## 2. Some Examples

**Example 2.1.** Each group $G$ has the normal series $\{e\} \lhd G$. This is the only normal series if $G$ is a simple group.

**Example 2.2.** Two normal series for $\mathbf{Z}/(6)$, with cyclic factors of order 2 and 3, are

$$\{0\} \lhd \langle 2 \rangle \lhd \mathbf{Z}/(6)$$

and

$$\{0\} \lhd \langle 3 \rangle \lhd \mathbf{Z}/(6).$$

**Example 2.3.** Three normal series for $D_4$ are

$$\{1\} \lhd \langle r^2 \rangle \lhd D_4, \quad \{1\} \lhd \langle r^2 \rangle \lhd \langle r \rangle \lhd D_4, \quad \{1\} \lhd \langle s \rangle \lhd \langle r^2, s \rangle \lhd D_4.$$

The second series is a refinement of the first. The factors of the first series are $\langle r^2 \rangle \cong \mathbf{Z}/(2)$ and $D_4/\langle r^2 \rangle \cong \mathbf{Z}/(2) \times \mathbf{Z}/(2)$, while the second and third normal series both have 3 cyclic groups of order 2 as their factors.

**Example 2.4.** A normal series for $S_4$ is

$$\{(1)\} \lhd A_4 \lhd S_4.$$

The subgroup $V = \{(1), (12)(34), (13)(24), (14)(23)\}$ is normal in $A_4$ (and $S_4$) and leads to the refined normal series

$$\{(1)\} \lhd V \lhd A_4 \lhd S_4. \tag{2.1}$$

This can be refined further to the normal series

$$\{(1)\} \lhd U \lhd V \lhd A_4 \lhd S_4, \tag{2.2}$$

where $U$ is a 2-element subgroup of $V$. (Although $U \lhd V$, $U$ is not normal in $A_4$ or $S_4$.) No further refinements are possible since each subgroup in (2.2) has prime index (2 or 3) in the next subgroup.

Our remaining examples involve matrix groups.

**Example 2.5.** For a field $F$, the group $\mathrm{Aff}(F)$ has the normal series

$$\left\{\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\right\} \lhd \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\} \lhd \left\{\begin{pmatrix} * & * \\ 0 & 1 \end{pmatrix}\right\}, \tag{2.3}$$

with factors isomorphic to $F$ and $F^\times$.

In Example 2.4, a normal series for $S_4$ was refined twice. Refining a normal series means creating a longer normal series by inserting subgroups between the subgroups already in the series. Repeating a subgroup already there is a trivial refinement.

When can the series (1.1) be refined nontrivially? If a factor $G_{i+1}/G_i$ is not a simple group then it has a proper nontrivial normal subgroup, which can be written as $N/G_i$

<!-- page 3 -->

where $G_i \subset N \subset G_{i+1}$. Since $N/G_i \lhd G_{i+1}/G_i$ we have $G_i \lhd N \lhd G_{i+1}$. Therefore we can insert $N$ into (1.1) and obtain a new normal series for $G$ with the same factors as before except $G_{i+1}/G_i$ has been replaced by the two nontrivial factors $G_{i+1}/N$ and $N/G_i$. When $G_{i+1}/G_i$ is a simple group, there are no normal subgroups of $G_{i+1}$ lying strictly between $G_i$ and $G_{i+1}$, so (1.1) can't be refined by inserting a group nontrivially between $G_i$ and $G_{i+1}$. Therefore (1.1) is unrefinable (that is, (1.1) admits only trivial refinements; unrefinable means nontrivially unrefinable) precisely when all the factors $G_{i+1}/G_i$ are simple or trivial.

**Definition 2.6.** An unrefinable normal series with no repetitions is a *composition series*.

Example 2.2 gives two composition series for $\mathbf{Z}/(6)$ and (2.2) is a composition series for $S_4$. The second and third normal series for $D_4$ in Example 2.3 are composition series.

If a normal series is thought of as something like a "factorization" for the group, then a refinement of a normal series is like a further factorization and a composition series is like a prime factorization. Having no repetitions is like avoiding factors of 1 in a factorization.

**Theorem 2.7.** *Every nontrivial finite group has a composition series. In a finite abelian group, every factor in a composition series has prime order.*

*Proof.* Let $G$ be a finite group with $|G| > 1$. It has a normal series, namely $\{e\} \lhd G$. If $G$ is a simple group then this is a composition series. Otherwise $G$ has a nontrivial proper normal subgroup $N$ and we have the normal series $\{e\} \lhd N \lhd G$. If $N$ and $G/N$ are simple groups then this is a composition series. Otherwise we can refine further. At each stage when $G$ has a normal series (1.1) with $G_i \neq G_{i+1}$ for all $i$,

$$|G| = [G_r : G_{r-1}] \cdots [G_2 : G_1][G_1 : G_0] \geq 2^r,$$

so the number of factors $r$ is bounded above in terms of the size of $G$. Therefore we can't continue to refine indefinitely, so at some point we will reach a composition series.

When $G$ is a finite abelian group, if $G_i \lhd G_{i+1}$ are two successive terms in a composition series then $G_{i+1}/G_i$ is an abelian simple group, so necessarily of prime order. $\square$

Infinite groups may or may not admit a composition series. In particular, $\mathbf{Z}$ has no composition series: if (1.1) is a normal series for $\mathbf{Z}$ then $G_1$ is infinite cyclic, so $G_1$ has a proper nontrivial subgroup that is obviously normal in $\mathbf{Z}$. Therefore (1.1) can be refined.

The following theorem for composition series is analogous to unique factorization in $\mathbf{Z}^+$.

**Theorem 2.8 (Jordan-Holder).** *If $G$ is a nontrivial group and*

$$\{e\} = G_0 \lhd G_1 \lhd G_2 \lhd \cdots \lhd G_r = G$$

*and*

$$\{e\} = \widetilde{G}_0 \lhd \widetilde{G}_1 \lhd \widetilde{G}_2 \lhd \cdots \lhd \widetilde{G}_s = G$$

*are two composition series for $G$ then $r = s$ and for some permutation $\pi \in S_r$ we have $\widetilde{G}_i/\widetilde{G}_{i-1} \cong G_{\pi(i)}/G_{\pi(i)-1}$ for $1 \leq i \leq r$.*

We don't need this result, so its proof is left to an appendix. This theorem was proved by Jordan in 1873, in the weaker form that $[G_i : G_{i-1}] = [\widetilde{G}_{\pi(i)} : \widetilde{G}_{\pi(i)-1}]$ for a suitable $\pi \in S_r$. That the quotient groups themselves are isomorphic was proved by Holder 16 years later. This theorem was an important milestone in the historical development of the abstract quotient group concept [18].

<!-- page 4 -->

**Example 2.9.** Two composition series for $D_6$ are

$$\{1\} \lhd \langle r^2 \rangle \lhd \langle r \rangle \lhd D_6$$

and

$$\{1\} \lhd \langle r^3 \rangle \lhd \langle r^3, s \rangle \lhd D_6.$$

The factors in these composition series are one cyclic group of order 3 and two cyclic groups of order 2. For instance, calling the subgroups in the first series $G_i$ and those in the second series $\widetilde{G}_i$, we have $\widetilde{G}_1/\widetilde{G}_0 \cong G_3/G_2$, $\widetilde{G}_2/\widetilde{G}_1 \cong G_2/G_1$, and $\widetilde{G}_3/\widetilde{G}_2 \cong G_1/G_0$. The Jordan-Holder theorem applies with $\pi = (13)$ (or $\pi = (123)$).

**Example 2.10.** Not only is the Jordan-Holder theorem an analogue of unique factorization in $\mathbf{Z}$, but unique factorization is the special case of the Jordan-Holder theorem for finite cyclic groups. Let's see why.

Pick an integer $n > 1$. A composition series for $\mathbf{Z}/(n)$ will have factors of prime order, since $\mathbf{Z}/(n)$ is abelian. If (1.1) is a composition series for $G = \mathbf{Z}/(n)$ and we set $p_i = |G_{i+1}/G_i|$, a prime number, then $n = p_1 p_2 \cdots p_r$. So composition series of $\mathbf{Z}/(n)$ yield prime factorizations of $n$. Conversely, writing $n = p_1 p_2 \cdots p_r$ with primes $p_i$, the series

$$\{0\} = \langle p_1 p_2 \cdots p_r \rangle \lhd \langle p_2 p_3 \cdots p_r \rangle \lhd \cdots \lhd \langle p_r \rangle \lhd \langle 1 \rangle = \mathbf{Z}/(n),$$

is a composition series for $\mathbf{Z}/(n)$ with factors of prime orders $p_1, p_2, \ldots, p_r$. Thus the primes and their multiplicities in a factorization of $n$ can be recovered from a suitable composition series for $\mathbf{Z}/(n)$. Comparing two composition series for $\mathbf{Z}/(n)$ shows, by the Jordan-Holder theorem, that $n$ has a unique prime factorization.

Roughly speaking, the Jordan-Holder theorem says that a group determines its composition series (assuming there is one at all). More precisely, a group determines the factors (up to isomorphism) and their multiplicities in a composition series. But you can't go the other way: non-isomorphic groups can have the same composition factors with the same multiplicities. For instance, for prime $p$ both $D_p$ and $\mathbf{Z}/(2p)$ have composition series with one factor of size 2 and one of size $p$, by Example 1.1.

A more natural way of decomposing a group, at first sight, is through direct products instead of through normal series. Call a nontrivial group $G$ *decomposable* if $G \cong H \times K$ for nontrivial groups $H$ and $K$. If a nontrivial group is not decomposable, call it *indecomposable*. Examples of indecomposable groups include nontrivial cyclic $p$-groups,[^2] $S_n$ for $n \geq 2$, and $\mathbf{Z}$. By an easy induction, each finite nontrivial group can be written as a direct product of indecomposable groups. Some infinite groups are (finite) direct products of indecomposable groups and others are not.

**Example 2.11.** The group $D_6 = \langle r, s \rangle$ has two indecomposable decompositions: $\langle r^2, s \rangle \times \langle r^3 \rangle$ and $\langle r^2, rs \rangle \times \langle r^3 \rangle$. The first groups in both cases are not equal but are isomorphic.

**Theorem 2.12 (Krull-Schmidt).** *If a group is isomorphic to $H_1 \times \cdots \times H_r$ and $K_1 \times \cdots \times K_s$, where the $H_i$'s and $K_j$'s are indecomposable, then $r = s$ and there is some $\pi \in S_r$ such that $H_i \cong K_{\pi(i)}$ for all $i$.*

*Proof.* See [14, Chap. II, \S3]. $\square$

The Krull-Schmidt theorem is nice to know, but it's really not the right way to think about "decomposing" nonabelian (finite) groups. Theorems of Krull-Schmidt type are more important in other areas of algebra than group theory. For instance, see [7].

[^2]: See Example 2.3 in https:

<!-- page 5 -->

## 3. Normal Series Under Group Constructions

We now look at how normal series behave under three constructions on groups: passage to a subgroup, passage to a quotient group, and direct products. As you will see, there is nothing really surprising in the results we find or the way we find them: the only way one can imagine concocting a normal series for a subgroup, quotient group, and direct product turns out to work. This material is primarily needed for technical work later. To fix ideas, we use an ascending normal series for $ as in (1.1).

If $ is a subgroup of $ then intersecting $ with each group in (1.1) yields

2918\{e\} = H_0 \lhd H_1 \lhd H_2 \lhd \cdots \lhd H_r = H, 	ag{3.1}2918

where  := H \cap G_i$. To see that  \lhd H_{i+1}$, and not just  \subset H_{i+1}$, the kernel of the natural homomorphism {i+1} 	o G_{i+1}/G_i$ is {i+1} \cap G_i = (H \cap G_{i+1}) \cap G_i = H \cap G_i = H_i$. Therefore not only is  \lhd H_{i+1}$ for all $, but also {i+1}/H_i$ is isomorphic to a subgroup of {i+1}/G_i$. This proves the following theorem.

**Theorem 3.1.** *If we intersect the normal series of $ in (1.1) with a subgroup $, we obtain the normal series (3.1) of $ whose successive factors are isomorphic to subgroups of the successive factors of (1.1).*

**Example 3.2.** View $ inside $ by labelling the vertices of a square in order as 1, 2, 3, 4. Let  = (1234)$,  = (24)$ (so  = \langle r, s angle$), and  = \langle (13)(24) angle = \langle r^2 angle$ in (2.2). Intersecting the normal series (2.2) of $ with $ gives a normal series for $: $\{(1)\} \lhd \langle r^2 angle \lhd \langle r^2, rs angle \lhd \langle r^2, rs angle \lhd D_4$. Notice the repetition.

**Corollary 3.3.** *When the factors in (1.1) belong to a class of groups closed under passage to subgroups, every subgroup of $ has a normal series whose factors are in that class.*

*Proof.* The construction we gave for a normal series of a subgroup from a normal series of the original group has factors that are (isomorphic to) subgroups of the factors in the original normal series. $\square$

**Example 3.4.** If $ admits a normal series whose factors are abelian then so do all subgroups of $.

Having created normal series for a subgroup, we now look at normal series for a quotient group. Let  \lhd G$ and (1.1) be a normal series for $. To construct a normal series for /N$, note that $ is a subgroup of $ and  \subset NG_{i+1}$, so

2924N = NG_0 \lhd NG_1 \lhd NG_2 \lhd \cdots \lhd NG_r = G. \tag{3.2}2924

The reason that  \lhd NG_{i+1}$ is that $ and {i+1}$ each normalize $ inside of $. Since $ is normal in $, it is normal in every group in (3.2), so we can reduce (3.2) modulo $ to get

2924\{\bar{e}\} = \overline{G}_0 \lhd \overline{G}_1 \lhd \overline{G}_2 \lhd \cdots \lhd \overline{G}_r = G/N, \tag{3.3}2924

where $\overline{G}_i := (NG_i)/N \cong G_i/(N \cap G_i)$. The natural map  \to \overline{G}_i$ is onto for all $, so the map {i+1} \to \overline{G}_{i+1}/\overline{G}_i$ is onto and kills $, so $\overline{G}_{i+1}/\overline{G}_i$ is isomorphic to a quotient group of {i+1}/G_i$ for all $. This proves the following theorem.

**Theorem 3.5.** *If (1.1) is a normal series of $ then (3.3) is a normal series of /N$ and its successive factors are quotient groups of the successive factors in (1.1).*


<!-- page 6 -->

**Corollary 3.6.** *When $ has a normal series whose factors belong to a class of groups closed under passage to quotient groups, then all quotient groups of $ have a normal series whose factors are in that class.*

**Example 3.7.** Continuing Example 3.4, if $ admits a normal series whose factors are abelian then so do all quotient groups of $.

Next we look at normal series for a direct product. Suppose (1.1) is a normal series for $, and another group $\widetilde{G}$ has the normal series

2927\{\tilde{e}\} = \widetilde{G}_0 \lhd \widetilde{G}_1 \lhd \widetilde{G}_2 \lhd \cdots \lhd \widetilde{G}_s = \widetilde{G}. \tag{3.4}2927

Then we can get a normal series for  \times \widetilde{G}$ with  + s$ factors:

2927G_0 \times \{\tilde{e}\} \lhd G_1 \times \{\tilde{e}\} \lhd \cdots \lhd G \times \{\tilde{e}\} \lhd G \times \widetilde{G}_1 \lhd \cdots \lhd G \times \widetilde{G}. \tag{3.5}2927

The successive inclusions here are either  \times \{\tilde{e}\} \subset G_{i+1} \times \{\tilde{e}\}$ or  \times \widetilde{G}_j \subset G \times \widetilde{G}_{j+1}$. The normality of $ in {i+1}$ and $\widetilde{G}_j$ in $\widetilde{G}_{j+1}$ make successive subgroups in (3.5) normal in each other, with quotient groups isomorphic to the factors in either (1.1) or (3.4).

**Theorem 3.8.** *If $ and $\widetilde{G}$ have normal series (1.1) and (3.4) then the direct product  \times \widetilde{G}$ has normal series (3.5), whose successive factors are isomorphic to the successive factors of (1.1) followed by the successive factors of (3.4).*

**Corollary 3.9.** *If two groups $ and $\widetilde{G}$ have normal series whose factors belong to a class of groups then  \times \widetilde{G}$ has a normal series whose factors are in that class.*

**Example 3.10.** If $ and $\widetilde{G}$ have normal series with abelian factors then so does  \times \widetilde{G}$.

## 4. Abelian and Central Series

In a group $, the center  = Z(G)$ and commutator subgroup 0$ play somewhat dual[^3] roles:

- Commutativity of $ is equivalent to both  = G$ and 0 = \{e\}$. (However, finiteness of /Z$ and 0$ are not equivalent, and the conditions  = \{e\}$ and 0 = G$ are not equivalent. See Remark 4.30.)
- Every subgroup of $ that is contained in $ is normal in $ since $ is abelian, while every subgroup of $ that contains 0$ is normal in $ since /[G, G]$ is abelian.
- Corollary 4.28 will put the construction of two subgroup series, based on $ and 0$, in dual positions: one is ascending, the other is descending, and they have the same number of terms.

If $ is nonabelian, a measure of how close this group is to being abelian could be based on how close $ is to $ or how close 0$ is to $\{e\}$. We will introduce three series of subgroups, two generalizing the commutator subgroup (called the derived series ^{(i)}$ and lower central series $, both tending down to $\{e\}$) and one generalizing the center (called the upper central series $ and tending up to $). These will be used to define solvable and nilpotent groups in Section 5. Before we introduce these three particular subgroup series, we define the general kinds of series they will all turn out to be examples of.

[^3]: Saying $ and 0$ are dual to each other is informal usage. It is not meant in the sense of category theory.


<!-- page 7 -->

**Definition 4.1.** An ascending series

$$\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G \tag{4.1}$$

and descending series

$$G = G_0 \supset G_1 \supset G_2 \supset \cdots \supset \{e\} \tag{4.2}$$

are called *abelian* if successive subgroups are normal in each other and all factors in the series ($G_{i+1}/G_i$ or $G_i/G_{i+1}$) are abelian. We don't assume $G$ is some $G_i$ in (4.1) or $\{e\}$ is some $G_i$ in (4.2).

We call (4.1) a *central series* if, for all $i$, $G_i \lhd G$ (stronger than $G_i \lhd G_{i+1}$!) and $G_{i+1}/G_i \subset Z(G/G_i)$. Similarly, (4.2) is called *central* if, for all $i$, $G_i \lhd G$ and $G_i/G_{i+1} \subset Z(G/G_{i+1})$.

In the definition of a central series, we need $G_i \lhd G$ to make sense of $G/G_i$ as a group.

A central series is an abelian series since, for instance, the condition $G_{i+1}/G_i \subset Z(G/G_i)$ implies $G_{i+1}/G_i$ is abelian. But the converse is false, since an abelian subgroup need not lie in the center of the group.

**Example 4.2.** The normal series for $\mathrm{Aff}(F)$ in Example 2.5 is abelian since its factors are isomorphic to $F$ and $F^\times$. But it is not central when $|F| > 2$ since $\left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\} \not\subset Z(\mathrm{Aff}(F))$.

Both abelian and central series can be described in terms of "commutator subgroups of two subgroups." For subgroups $H$ and $K$ in $G$, set

$$[H, K] = \langle [h, k] : h \in H, k \in K \rangle.$$

Two simple properties of this construction are: $[H, K] = [K, H]$ (since $[h, k]^{-1} = [k, h]$) and if $H$ and $K$ are normal in $G$ then $[H, K]$ is normal in $G$ (because $g[h, k]g^{-1} = [ghg^{-1}, gkg^{-1}]$). We have $[H, K] = \{e\}$ if and only if $hk = kh$ for all $h \in H$ and $k \in K$.

**Theorem 4.3.** *The series (4.1) is abelian if and only if $[G_{i+1}, G_{i+1}] \subset G_i$ for all $i$ and (4.2) is abelian if and only if $[G_i, G_i] \subset G_{i+1}$ for all $i.*

*The series (4.1) is central if and only if $[G, G_{i+1}] \subset G_i$ for all $i$ and (4.2) is central if and only if $[G, G_i] \subset G_{i+1}$ for all $i$.*

*Proof.* If (4.1) is abelian then $G_{i+1}/G_i$ is an abelian group for all $i$, so in $G_{i+1}/G_i$ we have $[\bar{x}, \bar{y}] = \bar{1}$ for all $x$ and $y$ in $G_{i+1}$. This is equivalent to $[x, y] \in G_i$ for all $x$ and $y$ in $G_{i+1}$, which is equivalent to $[G_{i+1}, G_{i+1}] \subset G_i$. The argument for when (4.2) is abelian is similar.

If (4.1) is central then elements of $G_{i+1}/G_i$ commute with elements of $G/G_i$, which is equivalent to $gg_{i+1} \equiv g_{i+1}g \bmod G_i$. That is the same as $[g, g_{i+1}] \in G_i$ for all $i$, so $[G, G_{i+1}] \subset G_i$. Conversely, suppose $[G, G_{i+1}] \subset G_i$. Then $[G, G_i] \subset G_i$ since $G_i \subset G_{i+1}$, so $gg_ig^{-1}g_i^{-1} \in G_i$ for all $g \in G$ and $g_i \in G_i$. That is equivalent to $gg_ig^{-1} \in G_i$, which means $gG_ig^{-1} \subset G_i$ for all $g \in G$, so $G_i \lhd G$. Returning now to the inclusion $[G, G_{i+1}] \subset G_i$, we can reduce this modulo $G_i$ to get $[G/G_i, G_{i+1}/G_i] = \{\bar{e}\}$ in $G/G_i$, so $G_{i+1}/G_i \subset Z(G/G_i)$.

The argument for when (4.2) is central is similar. $\square$

When (4.2) is an abelian series, so $[G_i, G_i] \subset G_{i+1}$ for all $i$ by Theorem 4.3, at $i = 0$ we get $[G, G] \subset G_1$. At $i = 1$, $[G_1, G_1] \subset G_2$, so $[[G, G], [G, G]] \subset G_2$ since $[G, G] \subset G_1$. This suggests introducing a collection of "iterated commutator subgroups" $G^{(i)}$ for $i \geq 0$ defined recursively by $G^{(0)} = G$, $G^{(1)} = G' = [G, G]$, $G^{(2)} = G'' = [G', G']$, and

$$G^{(i+1)} = (G^{(i)})' = [G^{(i)}, G^{(i)}]$$

<!-- page 8 -->

for $i \geq 0$. Then $G^{(i+1)}$ is the commutator subgroup of $G^{(i)}$, so $G^{(i+1)} \lhd G^{(i)}$ and $G^{(i)}/G^{(i+1)} = G^{(i)}/(G^{(i)})'$ is abelian. Since $[N, N] \lhd G$ if $N \lhd G$, we have $G^{(i)} \lhd G$ for all $i$ by induction, so the descending series

$$G = G^{(0)} \supset G' \supset G'' \supset \cdots \supset \{e\} \tag{4.3}$$

consists of normal subgroups of $G$ with successive abelian quotients.

**Definition 4.4.** The series (4.3) is called the *derived series* of $G$.

**Example 4.5.** If $G$ is abelian then $G' = \{e\}$.

**Example 4.6.** Let $G = D_n$. For $n \geq 3$, $D_n' = \langle r^2 \rangle$, which is abelian, so $D_n'' = \{1\}$. For $n = 1$ and 2, $D_n'$ is trivial since $D_1$ and $D_2$ are abelian. Thus every dihedral group has a derived series that reaches the identity in at most 2 steps.

**Example 4.7.** Let $G = A_n$ for $n \geq 3$. For $n \geq 5$, $A_n' = A_n$ since $[(abd), (ace)] = (abc)$ when $a, b, c, d, e$ are distinct. Thus $A_n^{(i)} = A_n$ for $i \geq 0$ when $n \geq 5$, so the derived series for $A_n$ does not reach the identity.

Since $A_4' = V$ (the normal 2-Sylow subgroup of $A_4$) and $V$ is abelian, $V'$ is trivial. Thus $A_4''$ is trivial. Since $A_3$ is abelian, $A_3'$ is trivial.

**Example 4.8.** Let $G = S_n$ for $n \geq 3$. We have $G' = [S_n, S_n] = A_n$. Therefore, by the previous example, $G^{(i)} = A_n$ for $i \geq 1$ when $n \geq 5$, so the derived series for $S_n$ does not reach the identity. On the other hand, $S_4' = A_4$ so $S_4'''$ is trivial, and $S_3' = A_3$ so $S_3''$ is trivial.

**Example 4.9.** Let $G = \mathrm{Heis}(F)$, the group of $3 \times 3$ upper-triangular matrices

$$\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}.$$

Then $G' = Z(G)$, which is abelian, so $G'' = \{I_3\}$.

**Example 4.10.** For $n \geq 1$, the group $\mathrm{Heis}_n(F)$ consists of $(n+2) \times (n+2)$ matrices

$$\begin{pmatrix} 1 & \mathbf{x} & z \\ 0 & I_n & \mathbf{y} \\ 0 & 0 & 1 \end{pmatrix} := \begin{pmatrix} 1 & x_1 & \cdots & x_n & z \\ 0 & 1 & \cdots & 0 & y_1 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & y_n \\ 0 & 0 & \cdots & 0 & 1 \end{pmatrix}$$

under matrix multiplication:

$$\begin{pmatrix} 1 & \mathbf{x} & z \\ 0 & 1 & \mathbf{y} \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & \mathbf{x}' & z' \\ 0 & 1 & \mathbf{y}' \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & \mathbf{x} + \mathbf{x}' & z + z' + \mathbf{x} \cdot \mathbf{y}' \\ 0 & 1 & \mathbf{y} + \mathbf{y}' \\ 0 & 0 & 1 \end{pmatrix}.$$

Writing these matrices as $(\mathbf{x}, \mathbf{y}, z)$, the group law and inversion are

$(\mathbf{x}, \mathbf{y}, z)(\mathbf{x}', \mathbf{y}', z') = (\mathbf{x} + \mathbf{x}', \mathbf{y} + \mathbf{y}', z + z' + \mathbf{x} \cdot \mathbf{y}'), \quad (\mathbf{x}, \mathbf{y}, z)^{-1} = (-\mathbf{x}, -\mathbf{y}, -z + \mathbf{x} \cdot \mathbf{y}),$

while the conjugation and commutator formulas are

$(\mathbf{x}, \mathbf{y}, z)(\mathbf{x}', \mathbf{y}', z')(\mathbf{x}, \mathbf{y}, z)^{-1} = (\mathbf{x}', \mathbf{y}', z' + \mathbf{x} \cdot \mathbf{y}' - \mathbf{x}' \cdot \mathbf{y})$

$[(\mathbf{x}, \mathbf{y}, z), (\mathbf{x}', \mathbf{y}', z')] = (\mathbf{0}, \mathbf{0}, \mathbf{x} \cdot \mathbf{y}' - \mathbf{x}' \cdot \mathbf{y}).$
<!-- page 9 -->

From this, $\mathrm{Heis}_n(F)' = Z(\mathrm{Heis}_n(F)) = \{(\mathbf{0}, \mathbf{0}, z) : z \in F\}$, so $\mathrm{Heis}_n(F)''$ is trivial.

**Example 4.11.** Let $G = \mathrm{Aff}(F)$. For $|F| > 2$, $G' = \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\}$, which is abelian, so $G'' = \{I_2\}$. For $|F| = 2$, $G$ is abelian, so $G' = \{I_2\}$.

**Example 4.12.** Let $G = \mathrm{GL}_2(F)$. When $|F| > 3$, it can be shown that $\mathrm{GL}_2(F)' = \mathrm{SL}_2(F)$ and $\mathrm{SL}_2(F)' = \mathrm{SL}_2(F)$ (these are not obvious), so $\mathrm{GL}_2(F)^{(i)} = \mathrm{SL}_2(F)$ for $i \geq 1$: the derived series for $\mathrm{GL}_2(F)$ stabilizes at $\mathrm{SL}_2(F)$ and never reaches the identity.

When $|F| = 3$, $\mathrm{GL}_2(F)' = \mathrm{SL}_2(F)$, which has order 24, and $\mathrm{SL}_2(F)'$ is the 2-Sylow subgroup of $\mathrm{SL}_2(F)$ and isomorphic to $Q_8$. Since $Q_8' = \{1\}$, $\mathrm{GL}_2(F)''' = \{I_3\}$ when $|F| = 3$. When $|F| = 2$, $\mathrm{GL}_2(F) \cong S_3$ so $\mathrm{GL}_2(F)'' = \{I_2\}$.

The following theorem tells us that the derived series controls the decay of all abelian series from below.

**Theorem 4.13.** *If (4.2) is an abelian series for $G$ then $G^{(i)} \subset G_i$ for all $i$. In particular, if $G$ has an abelian normal series then the derived series is a normal series.*

*Proof.* We have $G^{(0)} = G_0 = G$. Since $G/G_1$ is abelian by hypothesis, $G' \subset G_1$. Assuming $G^{(i)} \subset G_i$, since $G_i/G_{i+1}$ is abelian we get $G_i' \subset G_{i+1}$, so $G^{(i+1)} = (G^{(i)})' \subset G_i' \subset G_{i+1}$.

Now suppose $G$ has a normal series with abelian factors. A normal series has both $G$ and $\{e\}$ among the $G_i$'s, so we can index the series from the top down like (4.2). Then $G^{(i)} \subset G_i$ for all $i$ and $G_i = \{e\}$ for some $i$, so $G^{(i)} = \{e\}$ for some $i$. Therefore the derived series of $G$ reaches the identity and that makes it a normal series. $\square$

Theorem 4.13 shows that when $G$ admits an abelian normal series its derived series is its *shortest* descending abelian normal series: $G_r = \{e\}$ implies $G^{(r)} = \{e\}$, so no abelian normal series can reach the identity before the derived series does.

Now we look at central series (rather than abelian series) for a group $G$. Suppose it is written in descending form as in (4.2), so $[G, G_i] \subset G_{i+1}$ for all $i$ by Theorem 4.3. At $i = 0$ we get $[G, G] \subset G_1$. At $i = 1$, $[G, G_1] \subset G_2$, so $[G, [G, G]] \subset G_2$. This suggests introducing the subgroups $L_i$ defined by recursively by $L_0 = G$, $L_1 = [G, G] = G'$, $L_2 = [G, L_1] = [L_1, G]$, and for $i > 0$

$$L_{i+1} = [G, L_i] = [L_i, G].$$

Since $L_1 \lhd G$, $L_i \lhd G$ for all $i$ by induction. Therefore $L_{i+1} = [G, L_i] \subset L_i$, so

$$G = L_0 \supset L_1 \supset L_2 \supset \cdots \supset \{e\}. \tag{4.4}$$

Although $L_0 = G^{(0)}$ and $L_1 = G'$, usually $L_i \neq G^{(i)}$ for $i > 1$. By induction, $G^{(i)} \subset L_i$ for all $i$. We'll see how this looks for dihedral groups in an example below.

In $G/L_{i+1} = G/[L_i, G]$, the elements of $L_i$ commute with all elements of $G$, so $L_i/L_{i+1} \subset Z(G/L_{i+1})$. Therefore the $L_i$'s are a descending central series of $G$.

**Definition 4.14.** The series (4.4) is called the *lower central series* of $G$.

As with the derived subgroups $G^{(i)}$, the $L_i$'s might not form a normal series for $G$ since they may never reach $\{e\}$.

**Example 4.15.** If $G$ is abelian, $L_1 = \{e\}$.

**Example 4.16.** Let $G = D_n$. Then $L_1 = D_n' = \langle r^2 \rangle$. For odd $n$, $\langle r^2 \rangle = \langle r \rangle$ and $[D_n, \langle r \rangle] = \langle r^2 \rangle = \langle r \rangle$, so $L_i = \langle r \rangle$ for all $i \geq 1$. For even $n = 2^k m$, $L_i = \langle r^{2^i} \rangle$ for $1 \leq i \leq k$ and $L_i$ stops
<!-- page 10 -->

shrinking at $i = k$ since $r^{2^k}$ has odd order: $L_i = \langle r^{2^k} \rangle$ for $i \geq k$. So the lower central series reaches $\{1\}$ only when $n = 2^k$ is a power of 2, in which case $L_{k-1} \neq \{1\}$ and $L_k = \{1\}$.

The groups $D_1$ and $D_2$ are both abelian, so for them $L_1 = \{1\}$.

For a comparison, the derived series of $D_n$ reaches the identity in 2 steps and the lower central series of $D_n$ either stabilizes before the identity if $n$ is not a power of 2 or reaches the identity in $k$ steps if $n = 2^k$. So when the derived series and lower central series both reach the identity ($n = 2^k$), the derived series does so much more quickly.

In this example, we see the inclusion $G^{(i)} \subset L_i$ for a general group $G$ is quite weak compared to what actually happens when $G = D_n$: for $n = 2^k$, for instance, $G^{(i)}$ becomes trivial already at $i = 2$ while it takes the $L_i$'s $k$ steps to become trivial. Thus we get the idea that the derived series $G^{(i)}$ for a group $G$ might decay exponentially faster than the lower central series. In fact, the inclusion $G^{(i)} \subset L_i$ can always be strengthened to $G^{(i)} \subset L_{2^i - 1}$ for all $i$. (This follow by induction on $i$ from the commutator containment $[L_i, L_j] \subset L_{i+j+1}$.)

**Example 4.17.** Let $G = A_n$ for $n \geq 3$. When $n \geq 5$, $A_n' = A_n$ so $L_i = G$ for $i \geq 0$. When $n = 4$, $A_4' = V$ and $[A_4, V] = V$, so $L_i = L_1$ for $i \geq 1$. When $n = 3$, $L_1 = A_3'$ is trivial since $A_3$ is abelian.

**Example 4.18.** Let $G = S_n$ for $n \geq 3$. We have $L_1 = S_n' = A_n$. Since $[(ab), (abc)] = (abc)$ for distinct $a$, $b$, and $c$, $L_2 = [S_n, A_n] = A_n$, so $L_i = L_1$ for $i \geq 1$.

**Example 4.19.** Let $G = \mathrm{Heis}(F)$. Then $L_1 = [G, G] = Z$ (the Heisenberg group's commutator subgroup and center coincide), so $L_2 = [G, L_1] = \{I_3\}$.

**Example 4.20.** Let $G = \mathrm{Aff}(F)$. Then $L_1 = [G, G] = \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\}$ and $[G, L_1] = L_1$ since $\left[\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}\right] = \begin{pmatrix} 1 & (a-1)c \\ 0 & 1 \end{pmatrix}$, so $L_i = L_1$ for $i \geq 1$. Unlike its derived series, which reaches the identity in 2 steps, the lower central series of $\mathrm{Aff}(F)$ does not reach the identity.

**Example 4.21.** Let $G = \mathrm{GL}_2(F)$. When $|F| > 2$, $L_1 = G' = \mathrm{SL}_2(F)$ and $L_2 = [\mathrm{GL}_2(F), \mathrm{SL}_2(F)] = \mathrm{SL}_2(F)$, so $L_i = \mathrm{SL}_2(F)$ for all $i \geq 1$. When $|F| = 2$, $\mathrm{GL}_2(F) = \mathrm{SL}_2(F) \cong S_3$ and $[S_3, A_3] = A_3$, so $L_i = L_1$ for all $i \geq 1$.

The following theorem explains the "lower" label on the lower central series: descending central series are bounded below by the lower central series.

**Theorem 4.22.** *If (4.2) is a central series for $G$ then $L_i \subset G_i$ for all $i$. In particular, if $G$ has a normal central series then the lower central series is a normal series.*

*Proof.* To show $L_i \subset G_i$ for all $i$ we argue by induction. It is clear when $i = 0$. Assuming $L_i \subset G_i$, $L_{i+1} = [G, L_i] \subset [G, G_i]$. Since (4.2) is a (descending) central series, $[G, G_i] \subset G_{i+1}$, so $L_{i+1} \subset G_{i+1}$.

A normal central series can be indexed from the top down as in (4.2), so if $G_i = \{e\}$ for some $i$, then $L_i = \{e\}$ for some $i$, making the lower central series of $G$ a normal series. $\square$

Now we consider ascending central series (4.1), so $G_{i+1}/G_i \subset Z(G/G_i)$. We will define a sequence of "iterated centers" of $G$ that control the growth of a central series (4.1) from above, as the lower central series controls the decay of a central series (4.2) from below.

Set $Z_0 = \{e\}$ and $Z_1 = Z(G)$. Both are normal subgroups of $G$. Recursively, if we have defined a normal subgroup $Z_i \lhd G$, write the center of $G/Z_i$ as $Z_{i+1}/Z_i$:

$$Z_{i+1} = \{g \in G : gx \equiv xg \bmod Z_i \text{ for all } x \in G\}.$$
<!-- page 11 -->

(To compute this, determine the center of $G/Z_i$ and take its inverse image under the reduction map $G \to G/Z_i$ to find $Z_{i+1}$.) Since the center of a group is a normal subgroup, $Z_{i+1}/Z_i \lhd G/Z_i$, so $Z_{i+1} \lhd G$. We obtain an ascending series of subgroups

$$\{e\} = Z_0 \subset Z_1 \subset Z_2 \subset \cdots \subset G \tag{4.5}$$

where $Z_i \lhd G$ for all $i$ (so $Z_i \lhd Z_{i+1}$ for all $i$).

**Definition 4.23.** The series (4.5) is called the *upper central series* of $G$.

The recursive definitions of the three subgroup series $G^{(i)}$, $L_i$, and $Z_i$ are in Table 1.

| Name of Series | $H_0$ | $H_{i+1}$ | Direction |
|---|---|---|---|
| Derived | $G^{(0)} = G$ | $G^{(i+1)} = [G^{(i)}, G^{(i)}]$ | Descending |
| Lower Central | $L_0 = G$ | $L_{i+1} = [G, L_i] = [L_i, G]$ | Descending |
| Upper Central | $Z_0 = \{e\}$ | $Z_{i+1}/Z_i = Z(G/Z_i)$ | Ascending |

Table 1.

**Example 4.24.** If $G$ is abelian then $Z_1 = G$.

**Example 4.25.** We will determine the upper central series for the dihedral groups. Often we will use the following characterization of a dihedral group: a group of order $2k$ with generators $x$ and $y$ such that $x^k = e$, $y^2 = e$, and $yxy^{-1} = x^{-1}$ is isomorphic to $D_k$.

When $n$ is odd, $D_n$ has trivial center, so $Z_i = \{1\}$ for all $i$.

When $n = 2m$ with $m \geq 3$ odd, $Z_1 = \langle r^{n/2} \rangle$ and $D_n/Z_1 = \langle \bar{r}, \bar{s} \rangle$. In this quotient group, $\bar{r}$ has order $n/2$ and the group has generators with the relations of a dihedral group of order $n/2$, so $D_n/Z_1 \cong D_{n/2} = D_m$. Since $m$ is odd, $D_m$ has trivial center, so the center of $D_n/Z_1$ is trivial. Therefore $Z_2 = Z_1$ and $Z_i = Z_1$ for all $i \geq 1$.

Now suppose $n = 2^k m$ where $k \geq 2$ and $m \geq 3$ is odd. As before, $D_n$ has center $Z_1 = \langle r^{n/2} \rangle$ and $D_n/Z_1 = \langle \bar{r}, \bar{s} \rangle \cong D_{n/2}$. Now $n/2$ is even, so the center of $D_n/Z_1$ is $\langle \bar{r}^{n/4} \rangle$. Therefore $Z_2 = \langle r^{n/4} \rangle$ and $D_n/Z_2$ has order $n/4$ and generators satisfying the relations of a dihedral group of order $n/4$, so $D_n/Z_2 \cong D_{n/4}$. By induction, for $i \leq k$ we have $Z_i = \langle r^{n/2^i} \rangle$ and $D_n/Z_i \cong D_{n/2^i}$. Since $D_n/Z_k \cong D_m$ has trivial center ($m$ is odd with $m \geq 3$), $Z_{k+1} = Z_k$ so $Z_i = Z_k$ for $i \geq k$.

The remaining case is $n = 2^k$. The groups $D_1$ and $D_2$ are both abelian, so for them $Z_i = D_n$ for all $i$. Take now $k \geq 2$. As in the previous case, $Z_i = \langle r^{n/2^i} \rangle = \langle r^{2^{k-i}} \rangle$ and $D_n/Z_i \cong D_{n/2^i} = D_{2^{k-i}}$ for $0 \leq i \leq k-1$. Then $D_n/Z_{k-1} = \langle \bar{r}, \bar{s} \rangle \cong \mathbf{Z}/(2) \times \mathbf{Z}/(2) = D_2$, which is abelian (this never happened for $n$ not a power of 2), so $Z_k = D_n$.

That was a lot of computation, so let's summarize what happens. If $n$ is not a power of 2, then $n = 2^k m$ where $k \geq 0$ and $m \geq 3$ is odd. The upper central series for $D_n$ is

$$Z_0 = \{1\} \subset \langle r^{n/2} \rangle \subset \langle r^{n/4} \rangle \subset \langle r^{n/8} \rangle \subset \cdots \subset \langle r^{n/2^{k-1}} \rangle \subset \langle r^{n/2^k} \rangle = \langle r^m \rangle = Z_k$$

and $Z_i = \langle r^m \rangle$ for $i \geq k$. If $n$ is a power of 2, then $n = 2^k$. For $k \geq 2$, the upper central series for $D_{2^k}$ is

$$Z_0 = \{1\} \subset \langle r^{n/2} \rangle \subset \langle r^{n/4} \rangle \subset \langle r^{n/8} \rangle \subset \cdots \subset \langle r^{n/2^{k-1}} \rangle = \langle r^2 \rangle \subset D_{2^k} = Z_k$$

and $Z_i = D_{2^k}$ for $i \geq k$. If $n = 1$ or $n = 2$ then $Z_i = D_n$ for $i \geq 0$.

**Example 4.26.** Let $G = \mathrm{Heis}(F)$. Then $G/Z_1 \cong F^2$ is abelian, so $Z_2 = G$.
<!-- page 12 -->

| $G$ | $Z_i$ | $L_i$ |
|---|---|---|
| $D_m$, $m \geq 3$ odd | $\{1\}$ | $\langle r \rangle$, $i \geq 1$ |
| $D_{2^k m}$, $k \geq 1$, $m \geq 3$ odd | $\langle r^{n/2^k} \rangle$, $i \geq k$ | $\langle r^{2^k} \rangle$, $i \geq k$ |
| $A_n$, $n \geq 5$ | $\{(1)\}$ | $A_n$ |
| $A_4$ | $\{(1)\}$ | $V$ |
| $S_n$, $n \geq 3$ | $\{(1)\}$ | $A_n$, $i \geq 1$ |
| $\mathrm{Aff}(F)$, $|F| > 2$ | $\{I_2\}$ | $\left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\}$ |
| $\mathrm{GL}_2(F)$, $|F| > 2$ | $F^\times I_2$, $i \geq 1$ | $\mathrm{SL}_2(F)$, $i \geq 1$ |

Table 2.

In Table 2 are examples where the $Z_i$'s do not reach $G$ (and the $L_i$'s do not reach $\{e\}$).

**Theorem 4.27.** *If (4.1) is a central series for $G$ then $G_i \subset Z_i$ for all $i$. In particular, if $G$ has a normal central series then the upper central series is a normal series.*

This is an upper analogue of Theorem 4.22.

*Proof.* To show $G_i \subset Z_i$ we argue by induction. It is clear for $i = 0$. If $G_i \subset Z_i$ for some $i$, we want to show $G_{i+1} \subset Z_{i+1}$. By definition, $Z_{i+1}/Z_i$ is the center of $G/Z_i$. For $x \in G$ and $y \in G_{i+1}$, $xy \equiv yx \bmod G_i$ since $G_{i+1}/G_i \subset Z(G/G_i)$, so $xy \equiv yx \bmod Z_i$ by the inductive hypothesis. Letting $x$ run over $G$ we see that $y \bmod Z_i \in Z(G/Z_i) = Z_{i+1}/Z_i$, so $y \in Z_{i+1}$. Now letting $y$ vary shows $G_{i+1} \subset Z_{i+1}$.

A normal central series can be indexed from the bottom up as in (4.1), so if $G_i = G$ for some $i$ then $Z_i = G$ for some $i$, making the upper central series of $G$ a normal series. $\square$

For all $G$, $Z = G$ if and only if $[G, G] = \{e\}$. This is the case $i = 1$ of the following connection between the upper and lower central series.

**Corollary 4.28.** *For every group $G$, $Z_i = G$ for some $i$ if and only if $L_i = \{e\}$ for some $i$, in which case the least $i$'s for which these occur are the same.*

*Proof.* Suppose $Z_n = G$. Since $G$ is reached, the upper central series can be viewed as a descending normal central series by reversing the indices: set $G_i = Z_{n-i}$ for $i = 0, 1, \ldots, n$. Then for all $i$, Theorem 4.22 implies $L_i \subset G_i = Z_{n-i}$, so $L_n$ is trivial. The converse argument is similar, using Theorem 4.27. $\square$

**Remark 4.29.** A classical theorem about the center says that if $G/Z$ is cyclic then $G$ is abelian. This can be generalized: if $G/Z_i$ is cyclic for some $i \geq 1$ then $G = Z_i$. Indeed, $G/Z_{i-1}$ has center $Z_i/Z_{i-1}$ and the quotient of $G/Z_{i-1}$ by its center is isomorphic to $G/Z_i$, so if $G/Z_i$ is cyclic then by the classical theorem $G/Z_{i-1}$ equals its center $Z_i/Z_{i-1}$. That means $G = Z_i$. (This proof doesn't make sense for $i = 0$ and the result isn't even true then: take $G$ to be nontrivial and cyclic.)

**Remark 4.30.** Since commutativity of $G$ is equivalent to $G/Z$ and $[G, G]$ being trivial, we ask: are the finiteness of $G/Z$ and $[G, G]$ equivalent? Schur proved that if $G/Z$ is finite then $[G, G]$ is finite [4, pp. 60-61] [16, pp. 43-44]. However, if $[G, G]$ is finite then $G/Z$ need not be finite. (Examples are described on the first page of [12] or in [16, p. 44].) Schur's result was generalized by Baer to higher terms in the upper and lower central series: if $G/Z_i$ is finite then $L_i$ is finite (Schur's theorem is the case $i = 1$). Hall [10] proved a converse of Baer's theorem: if $L_i$ is finite then $G/Z_{2i}$ (not $G/Z_i$) is finite, and for each $i$ he gave an
<!-- page 13 -->

example where $L_i$ is finite and $G/Z_j$ is infinite for each $j < 2i$. So some term of the lower central series is finite if and only if some term of the upper central series has finite index, but this need not first occur at the same term in the two series.

The conditions $Z = \{e\}$ and $G = [G, G]$, as measures of extreme noncommutativity of $G$, are not equivalent. For instance, the group $S_n$ for $n \geq 3$ has trivial center while $[S_n, S_n] = A_n$. For prime $p > 3$, the group $\mathrm{SL}_2(\mathbf{Z}/(p))$ has center $\{\pm I_2\}$ and the group is equal to its commutator subgroup.

We did not define an "upper" counterpart to the derived series (bounding an abelian series from above in the setting of Theorem 4.13). As an exercise, formulate what it should mean for an ascending subgroup series (starting at $G_0 = \{e\}$) to be abelian and explain why there is no general construction of a subgroup series that will dominate every abelian series from above.

## 5. Nilpotent and Solvable Groups: Basic Properties

Nilpotent and solvable groups are groups in which the upper/lower central series or derived series are actually normal series, *i.e.*, these subgroup series reach "the end".

**Definition 5.1.** A group $G$ is called *nilpotent* when it satisfies the following equivalent conditions:

(1) $G$ has a normal central series,
(2) $L_i = \{e\}$ for some $i$,
(3) $Z_i = G$ for some $i$.

The name "nilpotent" for this group property comes from an analogy with ring theory, which can be explained for readers familiar with the connection between Lie groups and Lie algebras. In a ring, an element with a power equal to 0 is called nilpotent. So in a Lie algebra $\mathfrak{g}$, an element $x$ could be called nilpotent if the linear operator $y \mapsto [x, y]$ on $\mathfrak{g}$ is nilpotent in the sense of ring theory (some power of this operator is 0). A theorem of Engel says all the elements of a Lie algebra are nilpotent if and only if the Lie group corresponding to this Lie algebra has the properties in Definition 5.1, and thus this property on abstract groups is called nilpotency.

By Theorem 4.27, the upper and lower central series of a nilpotent group are its shortest central series. The least $i$ such that $Z_i = G$, or equivalently $L_i = \{e\}$, is called the *nilpotency class* of $G$. This is also the number of factors in the upper and lower central series. For example, $D_{2^k}$ has nilpotency class $k$ for $k \geq 2$. The only group of nilpotency class 0 is the trivial group. Groups of nilpotency class 1 are nontrivial abelian groups. Groups of nilpotency class 2 are nonabelian groups satisfying $[G, G] \subset Z$ (*i.e.*, $G/Z$ is nontrivial and abelian).[^4] We could even define nilpotent groups recursively using the nilpotency class: the trivial group has nilpotency class 0, and for $n > 0$ a group $G$ has nilpotency class $n$ when $G/Z(G)$ has nilpotency class $n - 1$. Then the nilpotent groups are those having nilpotency class $n$ for some positive integer $n$.

**Definition 5.2.** A group $G$ is called *solvable* when it satisfies the following equivalent conditions:

(1) $G$ has an abelian normal series,

[^4]: A theorem of Levi [17] says that $G$ has nilpotency class at most 2 if and only if the commutator operation $x * y := [x, y]$ is distributive over the group law ($x * (yz) = (x * y)(x * z)$) and also if and only if the commutator operation is associative.

<!-- page 14 -->

(2) $G^{(i)}$ is trivial for some $i$.

The term solvable comes from Galois theory, where it is shown that polynomials in $\mathbf{Q}[X]$ whose roots can be described in terms of nested radicals are precisely those whose Galois groups over $\mathbf{Q}$ are solvable groups in the above sense.

Speakers of British English use soluble instead of solvable.

Theorem 4.13 says the derived series of a solvable group is its shortest abelian normal series. The least $i$ such that $G^{(i)}$ is trivial, or equivalently the number of factors in the derived series, is called the *solvable length* (or *derived length*) of the group. For $n \geq 3$, $D_n$ has solvable length 2. The only group with solvable length 0 is the trivial group. Solvable length 1 means the group is nontrivial and abelian. Solvable length 2 means the group is nonabelian but its commutator subgroup is abelian. The collection of solvable groups could be defined recursively in terms of the solvable length: the trivial group has solvable length 0, and for $n > 0$ a group $G$ has solvable length $\leq n$ when there is an abelian normal subgroup $A \lhd G$ (not necessarily the center!) such that $G/A$ has solvable length $\leq n - 1$.

**Theorem 5.3.** *All nilpotent groups are solvable.*

*Proof.* A normal series that is central is abelian, so nilpotency implies solvability. Alternatively, in terms of the special subgroup series we introduced, $G^{(i)} \subset L_i$ for all $i$ (Theorem 4.13). If $G$ is nilpotent then for large $i$ the subgroup $L_i$ is trivial, so $G^{(i)}$ is trivial. $\square$

The converse of Theorem 5.3 is false: for odd $n \geq 3$, $D_n$ is solvable ($D_n''$ is trivial) but not nilpotent ($L_i = \langle r \rangle$ for $i \geq 1$).

| Nilpotent | Solvable |
|---|---|
| abelian | $S_3$, $A_4$, $S_4$ |
| $D_{2^k}$ | $D_n$ |
| $\mathrm{Heis}(F)$ | $\mathrm{Aff}(F)$ |
| $\mathrm{Heis}(\mathbf{Z}/(n))$ | $\mathrm{Aff}(\mathbf{Z}/(n))$ |
| finite $p$-group | |

Table 3.

Table 3 lists some nilpotent and solvable groups. Our calculations of central and derived series in Section 4 explain the first three rows. In the third row, the group $\mathrm{Heis}(\mathbf{Z}/(n))$ is nilpotent since $L_1 = \mathrm{Heis}(\mathbf{Z}/(n))' = Z(\mathrm{Heis}(\mathbf{Z}/(n)))$ so $L_2 = \{I_3\}$, or alternatively $\mathrm{Heis}(\mathbf{Z}/(n))/Z_1 \cong (\mathbf{Z}/(n))^2$ is abelian so $Z_2 = \mathrm{Heis}(\mathbf{Z}/(n))$. The group $\mathrm{Aff}(\mathbf{Z}/(n))$ is solvable since $\left\{\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\right\} \lhd \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\} \lhd \left\{\begin{pmatrix} * & * \\ 0 & 1 \end{pmatrix}\right\}$ is a normal series with abelian quotients $\mathbf{Z}/(n)$ and $(\mathbf{Z}/(n))^\times$. The reason finite $p$-groups (including $D_{2^k}$ and $\mathrm{Aff}(\mathbf{Z}/(2^k))$, which are 2-groups) are nilpotent is that nontrivial finite $p$-groups have nontrivial center, so the upper central series has to keep growing until it reaches the whole group. (Here are the details. Suppose $|G| = p^n > 1$. Then $Z_1$ is nontrivial. If some $Z_i$ is nontrivial and not equal to $G$ then $G/Z_i$ is a nontrivial finite $p$-group, so its center is nontrivial. Therefore $Z_{i+1}$ is strictly larger than $Z_i$. This can't continue indefinitely, so some $Z_i$ equals $G$.)

The most important examples of nilpotent and solvable groups are groups of triangular matrices (such as $\mathrm{Heis}(F)$ and $\mathrm{Aff}(F)$). They are treated in Appendix B.

The groups in the solvable column of Table 3 are not nilpotent except for $D_n$ and $\mathrm{Aff}(\mathbf{Z}/(n))$ when $n$ is a power of 2. This was shown for dihedral groups in Example 4.25 by an explicit computation of upper and lower central series. Once we have some properties of nilpotent groups under our belt, we will show in Example 5.8 that $\mathrm{Aff}(\mathbf{Z}/(n))$ is not nilpotent except when $n$ is a power of 2.

Missing from Table 3 are some groups whose derived series we computed: $S_n$ and $A_n$ for $n \geq 5$ and $\mathrm{GL}_2(F)$ and $\mathrm{SL}_2(F)$ for $|F| > 3$ are *not* solvable, since $S_n' = A_n$ and $A_n' = A_n$, and $\mathrm{GL}_2(F)' = \mathrm{SL}_2(F)$ and $\mathrm{SL}_2(F)' = \mathrm{SL}_2(F)$. (The nonsolvability of $S_n$ for $n \geq 5$ is responsible for the general polynomial of degree $n$ over $\mathbf{Q}$ not being solvable in radicals.) The smallest nonsolvable group is $A_5$, of order 60, and every nonsolvable group of order 60 is isomorphic to $A_5$.

We now proceed to churn through some tedious but basic properties of nilpotent and solvable groups, *e.g.*, relations to composition series and behavior under group constructions like subgroups and quotient groups. The really interesting mathematical properties begin with Theorem 5.15.

**Theorem 5.4.** *For a group $G$, the following are equivalent:*

  (1) *$G$ is nilpotent,*
  (2) *there is a series $\{e\} = G_0 \subset G_1 \subset \cdots \subset G_r = G$ for some $r$ such that $[G, G_{i+1}] \subset G_i$ for all $i$,*
  (3) *there is a series $G = G_0 \supset G_1 \supset \cdots \supset G_r = \{e\}$ for some $r$ such that $[G, G_i] \subset G_{i+1}$ for all $i$.*

*For a group $G$, the following are equivalent:*

  (1) *$G$ is solvable,*
  (2) *there is a series $G = G_0 \supset G_1 \supset \cdots \supset G_r = \{e\}$ for some $r$ such that $[G_i, G_i] \subset G_{i+1}$ for all $i$.*

*Proof.* Use Theorem 4.3. $\square$

**Theorem 5.5.** *For a nontrivial group $G$, the following are equivalent:*

  (1) *$G$ is finite and solvable,*
  (2) *$G$ has a normal series with factors of prime order,*
  (3) *$G$ has a composition series with factors of prime order.*

*Proof.* Easily (2) $\Rightarrow$ (1). To show (1) $\Rightarrow$ (2), assume $G$ has an abelian normal series. Index it as a descending series, say (1.2). If $G_i/G_{i+1}$ is a factor of (1.2) not of prime order, it has a proper cyclic subgroup of prime order, say $H/G_{i+1}$. Then $H$ lies strictly between $G_i$ and $G_{i+1}$ and $G_{i+1} \lhd H \lhd G_i$ (since $G_i/G_{i+1}$ is abelian). We therefore can add $H$ to our normal series and it remains an abelian series. Since we can nontrivially refine the series as long as it has a factor that is not of prime order, while at the same time a normal series for a finite group can't be nontrivially refined indefinitely, at some point we will reach an unrefinable abelian normal series for $G$. Its factors must be of prime order.

Since a normal series with factors of prime order is a composition series, (2) and (3) are obviously equivalent. $\square$

**Example 5.6.** The derived series for $S_4$ is (2.1). The factors of this series are not all of prime order, but (2.1) can be refined to (2.2), whose factors are of order 2 or 3. Notice -- and this is crucial -- the series (2.2) does not contain only normal subgroups of $S_4$: the subgroup $U$ is normal in $V$ but not in $S_4$. Theorem 5.5 would not be true if we only allowed normal series where each subgroup is normal in the whole group.

<!-- page 16 -->

In contrast to Theorem 5.5(3), there is no characterization of finite nilpotent groups in terms of a *composition series*. For example, $\mathbf{Z}/(12)$ is nilpotent (all abelian groups are nilpotent) while $A_4$ is not nilpotent, but both groups have a composition series with two cyclic factors of order 2 and one of order 3.

Nilpotency behaves well under standard constructions of new groups from old groups:

**Theorem 5.7.** *Nilpotency is closed under subgroups, quotient groups, and direct products.*

*Proof.* We will use the lower central series viewpoint. If $H \subset G$ and $N \lhd G$ then by induction $L_i(H) \subset L_i(G)$ and $L_i(G/N) = (NL_i(G))/N$ for all $i$. For groups $G$ and $\widetilde{G}$, $L_i(G \times \widetilde{G}) = L_i(G) \times L_i(\widetilde{G})$ for all $i$. Therefore if the lower central series of $G$ and $\widetilde{G}$ reach the identity, so do the lower central series for every subgroup of $G$, quotient group of $G$, and $G \times \widetilde{G}$. $\square$

**Example 5.8.** We now show $\mathrm{Aff}(\mathbf{Z}/(n))$ is not nilpotent if $n$ is not a power of 2. For odd $n \geq 3$, $\mathrm{Aff}(\mathbf{Z}/(n))$ is not nilpotent since its center is trivial. When $n$ is even and not a power of 2, write $n = 2^k m$ where $m \geq 3$ is odd. Then reduction mod $m$ gives a natural map $\mathbf{Z}/(n) \to \mathbf{Z}/(m)$ that can be applied to matrix groups and gives us a natural map $\mathrm{Aff}(\mathbf{Z}/(n)) \to \mathrm{Aff}(\mathbf{Z}/(m))$. This reduction map on the affine groups is onto (check!), so $\mathrm{Aff}(\mathbf{Z}/(m))$ is (isomorphic to) a quotient group of $\mathrm{Aff}(\mathbf{Z}/(n))$. Since $\mathrm{Aff}(\mathbf{Z}/(m))$ is not nilpotent, neither can $\mathrm{Aff}(\mathbf{Z}/(n))$ be nilpotent. (Similar reasoning shows $D_n$ is not nilpotent if $n$ is not a power of 2: writing $n = 2^k m$ with odd $m \geq 3$, $D_n/\langle r^{2^k} \rangle \cong D_m$ is not nilpotent, so $D_n$ has a non-nilpotent quotient and therefore is not itself nilpotent.

**Corollary 5.9.** *If $H$ and $K$ are normal subgroups of $G$ such that $G/H$ and $G/K$ are nilpotent then $G/(H \cap K)$ is nilpotent.*

*Proof.* The direct product $G/H \times G/K$ is nilpotent since $G/H$ and $G/K$ are nilpotent. The diagonal map $G \to G/H \times G/K$ has kernel $H \cap K$, so $G/(H \cap K)$ is isomorphic to a subgroup of a nilpotent group, and thus is nilpotent. $\square$

**Remark 5.10.** The same proof shows that if a property of groups is preserved by passage to subgroups and direct products, then when $H$ and $K$ are normal subgroups of a group $G$ such that $G/H$ and $G/K$ have the property, then $G/(H \cap K)$ has the property.

Solvability behaves well under group constructions, in fact slightly better than nilpotency:

**Theorem 5.11.** *Solvability is closed under subgroups, quotient groups, and direct products. Moreover, if $N \lhd G$ then $G$ is solvable if and only if $N$ and $G/N$ are solvable.*

*Proof.* We saw in examples in Section 3 that every subgroup, quotient group, and direct product of groups that admit an abelian series also admit an abelian series. In particular, if $N \lhd G$ then solvability of $G$ implies solvability of $N$ and $G/N$.

It remains to show that if $N$ and $G/N$ are solvable then so is $G$. We will do this in two ways. First we argue in terms of abelian normal series. The groups $N$ and $G/N$ both admit abelian normal series, say

$$\{e\} = H_0 \lhd H_1 \lhd \cdots \lhd H_r = N$$

and

$$\{\bar{e}\} = G_0/N \lhd G_1/N \lhd \cdots \lhd G_s/N = G/N$$

<!-- page 17 -->

where $H_{i+1}/H_i$ is abelian and $(G_{j+1}/N)/(G_j/N)$ is abelian for all $i$ and $j$. The normal series for $G/N$ lifts to a normal series from $N$ to $G$:

$$N = G_0 \lhd G_1 \lhd \cdots \lhd G_s = G,$$

and the factors here are isomorphic termwise to those in the series for $G/N$. Therefore these factors are all abelian. Tacking the abelian normal series for $N$ onto the start, we get

$$\{e\} = H_0 \lhd H_1 \lhd \cdots \lhd H_r = N = G_0 \lhd G_1 \lhd \cdots \lhd G_s = G,$$

which has abelian factors (either $H_{i+1}/H_i$ or $G_{j+1}/G_j$).

Next we argue in terms of the derived series eventually reaching the trivial subgroup. Since $G/N$ is solvable, its derived subgroups $(G/N)^{(i)}$ eventually become trivial. It's straightforward to check by induction that $(G/N)^{(i)} = (NG^{(i)})/N$, so solvability of $G/N$ implies that for large $i$, $NG^{(i)} = N$. Thus $G^{(i)} \subset N$. Since $N$ is solvable, $N^{(j)}$ is trivial for large $j$, so $(G^{(i)})^{(j)}$ is trivial for large $i$ and $j$. Since $(G^{(i)})^{(j)} = G^{(i+j)}$, some derived subgroup of $G$ is eventually trivial, so we obtain solvability of $G$. $\square$

**Remark 5.12.** That solvability of $N$ and $G/N$ implies solvability of $G$ gives a conceptual role for the class of all solvable groups: it is the smallest class of groups $\mathcal{C}$ containing the abelian groups and having the quotient-lifting property: if $N \lhd G$ and $N$ and $G/N$ are in $\mathcal{C}$ then $G$ is in $\mathcal{C}$.

**Corollary 5.13.** *Let $H$ and $K$ be normal subgroups of the group $G$.*

  (1) *If $G/H$ and $G/K$ are solvable then $G/(H \cap K)$ is solvable.*
  (2) *If $H$ and $K$ are solvable then so is $HK$.*

*Proof.* Part (1) follows by the same reasoning as in the proof of Corollary 5.9, or see Remark 5.10. For (2), since $H$ is solvable and $HK/H \cong K/(H \cap K)$ is solvable, $HK$ is solvable by Theorem 5.11. $\square$

We only need one of $H$ or $K$ to be normal in $G$ for (2) to work: the proof only used normality of $H$, not $K$.

By Corollary 5.13 every finite group has a unique maximal solvable normal subgroup, which contains all other solvable normal subgroups. The maximal solvable normal subgroup of $G$ is called the (solvable) *radical* of $G$ and is denoted $R(G)$. To say a group has trivial radical means there are no nontrivial solvable normal subgroups, or equivalently (since the second to last subgroup in the derived series has to be an abelian subgroup) there are no nontrivial abelian normal subgroups. A group with trivial radical must have a trivial center (since the center is an abelian normal subgroup), and an example of such a group is $S_n$ for $n \geq 5$, as well as all nonabelian simple groups. As an exercise using the quotient-lifting property of solvability, show $G/R(G)$ has trivial radical. We won't discuss the solvable radical further, but a construction similar to it (Borel subgroups) is important in the study of linear algebraic groups.

Comparing Corollaries 5.9 and 5.13, it is natural to ask if the nilpotent analogue of Corollary 5.13(2) is true: when $H$ and $K$ are nilpotent normal subgroups in $G$, is $HK$ also nilpotent? Yes (theorem of H. Fitting), but it can't be proved as we did for the solvable case because nilpotency of $N$ and $G/N$ doesn't generally imply nilpotency of $G$. (Consider $G = D_n$ and $N = \langle r \rangle$ with $n \geq 3$ odd.)

The next result gives a setting where nilpotency of $N$ and $G/N$ implies nilpotency of $G$.

<!-- page 18 -->

**Theorem 5.14.** *Let $G$ be a group and $N$ be a normal subgroup of $G$ with $N \subset Z_i$ for some $i$, where $Z_i$ is a member of the upper central series for $G$. If $G/N$ is nilpotent then $G$ is nilpotent.*

*Proof.* Since $G/Z_i$ is a quotient group of $G/N$, $G/Z_i$ is nilpotent. Since $Z_i \subset Z_{i+1} \subset Z_{i+2} \subset \cdots \subset G$,

$$Z_i/Z_i \subset Z_{i+1}/Z_i \subset Z_{i+2}/Z_i \subset \cdots \subset G/Z_i.$$

This is the upper central series for $G/Z_i$ (check!). If $G/Z_i$ is nilpotent we must have $Z_j/Z_i = G/Z_i$ for some $j \geq i$, so $Z_j = G$ for some $j$. Thus $G$ is nilpotent. $\square$

This proof did not explicitly assume or use the nilpotence of $N$, but its nilpotence is automatic since every $Z_i$ is nilpotent and we assumed $N \subset Z_i$ for some $i$. There is a result of Philip Hall in the spirit of Theorem 5.14 that looks close to a quotient-lifting property: if $N$ and $G/N'$ are nilpotent then $G$ is nilpotent. (Notice we use $G/N'$ and not $G/N$.)

We turn now to interesting structural properties of nilpotent and solvable groups.

Nilpotent groups include finite $p$-groups, and the next theorem shows some properties of finite $p$-groups generalize to all nilpotent groups (including infinite nilpotent groups).

**Theorem 5.15.** *If $G$ is a nontrivial nilpotent group then*

  (1) *for every nontrivial normal subgroup $N \lhd G$, $N \cap Z(G) \neq \{e\}$ and $[G, N] \neq N$,*
  (2) *for every proper subgroup $H$, $H \neq \mathrm{N}(H)$.*

*In particular, a nontrivial nilpotent group has nontrivial center and its commutator subgroup is a proper subgroup.*

*Proof.* (1): We have $Z_i = G$ for some $i \geq 1$. Therefore $N \cap Z_i$ is nontrivial for some $i$. Pick $i$ minimal, so $i \geq 1$. Since $[G, Z_i] \subset Z_{i-1}$, we have $[G, N \cap Z_i] \subset N \cap Z_{i-1}$. By minimality of $i$, $N \cap Z_{i-1}$ is trivial, so $[G, N \cap Z_i]$ is trivial. Thus $N \cap Z_i \subset Z(G) = Z_1$, so $N \cap Z_i \subset N \cap Z_1$. The reverse inclusion is clear, so $N \cap Z_1 = N \cap Z_i \neq \{e\}$.

To prove $[G, N] \neq N$, assume $[G, N] = N$. Then $N \subset [G, G] = L_1$, so $N = [G, N] \subset [G, L_1] = L_2$. By induction, $N \subset L_i$ for all $i$, and taking $i$ large enough implies $N$ is trivial, a contradiction.

Taking $N = G$ in (1) recovers the special case mentioned at the end of the theorem.

(2): Since $Z_0 = \{e\}$ and $Z_i = G$ for some $i$, there is some $i$ such that $Z_i \subset H$. Then $[H, Z_{i+1}] \subset [G, Z_{i+1}] \subset Z_i \subset H$, so $Z_{i+1} \subset \mathrm{N}(H)$. Picking $i$ maximal such that $Z_i \subset H$, the fact that $Z_{i+1} \not\subset H$ implies $H \neq \mathrm{N}(H)$. $\square$

**Corollary 5.16.** *If $G$ is a nilpotent group and $H$ is a subgroup of $G$ with finite index $n$, then $g^n \in H$ for all $g \in G$.*

*Proof.* If $H$ were a normal subgroup of $G$, this result would be immediate from the fact that $G/H$ is a group of order $n$. Although $H$ need not be normal, we can use the nilpotent condition on $G$ to create a normal series

$$H = H_0 \lhd H_1 \lhd H_2 \lhd \cdots \lhd H_r = G$$

leading from $H$ to $G$: set $H_1 = \mathrm{N}(H)$, $H_2 = \mathrm{N}(\mathrm{N}(H)) = \mathrm{N}(H_1)$, and $H_{i+1} = \mathrm{N}(H_i)$. Then $H_i \lhd H_{i+1}$ since every subgroup is normal in its normalizer, and Theorem 5.15(2) says $H_{i+1}$ properly contains $H_i$ if $H_i \neq G$. Since $[G : H]$ is finite, the $H_i$'s can't increase forever, so $H_r = G$ for $r \gg 0$.

For $g \in G$, write $g^n = g^{[G:H]}$ in the form

$$g^{[G:H]} = ((g^{[H_r:H_{r-1}]})^{[H_{r-1}:H_{r-2}]})^{\cdots [H_1:H_0]}.$$
By normality of the subgroups, the successive powers on the right are in $H_{r-1}, H_{r-2}, \ldots$, and finally in $H_0 = H$. $\square$

This corollary is false for the non-nilpotent group $S_3$ with $H = \{(1), (12)\}$. The index is 3 and $(13)^3 = (13) \notin H$.

**Remark 5.17.** Call a positive integer $n$ a *nilpotent number* if all groups of order $n$ are nilpotent. Call $n$ a *nontrivial center number* if all groups of order $n$ have nontrivial center. Since a nontrivial nilpotent group has nontrivial center, every nilpotent number is a nontrivial center number, but the converse is false. The first counterexample is at 28: all groups of order 28 have nontrivial center, but $D_{14}$ is a group of order 28 that is not nilpotent.

We will see in Theorem 5.31 that Theorem 5.15(2) fails for all non-nilpotent solvable groups: there is a proper subgroup $H$ such that $\mathrm{N}(H) = H$.

Nilpotent groups include abelian groups, and the next theorem is easy to check for abelian groups but remains true for all nilpotent groups.

**Theorem 5.18.** *If $G$ is a nilpotent group then*

  (1) *the elements of finite order in $G$ are a subgroup,*
  (2) *if $H$ and $K$ are subgroups of $G$ and $[G : H]$ is finite then $[K : H \cap K]$ is finite and $[K : H \cap K] \mid [G : H]$.*

*Proof.* For (1), see [15, pp. 111--112]. For (2), which is a consequence of Theorem 5.15(2), see [11, p. 7]. $\square$

For the second part of Theorem 5.18 in general groups, $[K : H \cap K] \leq [G : H]$ but divisibility may not occur.

**Theorem 5.19.** *If $G$ is a nontrivial solvable group then every nontrivial normal subgroup of $G$ contains a nontrivial abelian normal subgroup of $G$. In particular, if $G$ is a nontrivial solvable group of nonprime size then $G$ contains a nontrivial proper normal subgroup.*

This is a solvable analogue of Theorem 5.15(1); in the nilpotent case we can just intersect the normal subgroup with the center of $G$. This method doesn't work in the solvable case since solvable groups can have trivial center (such as $A_4$ and $S_4$).

*Proof.* Let $N \lhd G$ with $N$ nontrivial. Since $N$ is solvable, $N^{(i)} = \{e\}$ for some $i$. Take $i$ minimal, so $i \geq 1$. Then $N^{(i-1)}$ is nontrivial and $(N^{(i-1)})' = N^{(i)} = \{e\}$, so $N^{(i-1)}$ is abelian. It is normal in $G$ since all members of the derived series of $N$ are normal in $G$ (when $H$ is normal in $G$, so is $[H, H]$).

To show $G$ contains a nontrivial proper normal subgroup, run through the above argument with $N = G$ to obtain a nontrivial abelian normal subgroup of $G$, namely the last nontrivial term in the derived series is an abelian normal subgroup of $G$, and it is a proper subgroup if $G$ is nonabelian. If $G$ is abelian then we can use a nontrivial proper normal subgroup; such a subgroup exists unless $|G|$ is prime. $\square$

**Theorem 5.20.** *For a nontrivial finite group $G$,*

  - *$G$ is solvable if and only if every nontrivial quotient of $G$ has a nontrivial abelian normal subgroup,*
  - *$G$ is nilpotent if and only if every nontrivial quotient of $G$ has a nontrivial center.*

<!-- page 20 -->

*Proof.* Since quotients of solvable groups are solvable and quotients of nilpotent groups are nilpotent, the "only if" directions follow from nontrivial solvable groups having nontrivial abelian normal subgroups and nontrivial nilpotent groups having nontrivial centers (and the finiteness of $G$ is irrelevant).

We turn to the converse results. Suppose every nontrivial quotient of $G$ has a nontrivial abelian normal subgroup. Then $G$ itself has a nontrivial abelian normal subgroup, say $G_1$. If $G/G_1$ is abelian then $G$ is solvable by the quotient-lifting property. If $G/G_1$ is nonabelian then $G/G_1$ is at least nontrivial and then has a nontrivial abelian normal subgroup, which has the form $G_2/G_1$, so $G_2 \neq G_1$ and $G_2 \lhd G$. Now we have the normal series $\{e\} \lhd G_1 \lhd G_2 \lhd G$ where the first and second factors are abelian. If $G/G_2$ is abelian then $G$ is solvable. If $G/G_2$ is nonabelian then it has a nontrivial abelian normal subgroup $G_3/G_2$ and we can refine the normal series by inserting $G_3$. Continuing this procedure eventually leads to $G_i = G$ for $i \gg 0$ and the $G_i$'s are an abelian normal series of $G$, so $G$ is solvable.

Now suppose every nontrivial quotient of $G$ has a nontrivial center. Then $G$ has a nontrivial center $Z_1$. If $Z_1 = G$ then $G$ is abelian and thus nilpotent. If $Z_1 \neq G$ then $G/Z_1$ is a nontrivial quotient of $G$ so it has a nontrivial center, which is exactly $Z_2/Z_1$. As long as $Z_i \neq G$ the quotient $G/Z_i$ has a nontrivial center so $Z_{i+1} \neq Z_i$. Since $G$ is finite we eventually must have $Z_i = G$ for $i \gg 0$, so $G$ is nilpotent. $\square$

Our next theorem characterizes finite nilpotent groups very concretely.

**Theorem 5.21.** *A finite group is nilpotent if and only if all of its Sylow subgroups are normal, or equivalently the group is isomorphic to the direct product of its Sylow subgroups.*

*Proof.* Suppose $G$ is a finite nilpotent group. Let $P$ be a Sylow subgroup. To show $P \lhd G$ we will show the normalizer $\mathrm{N}(P)$ is $G$. From Sylow theory, $\mathrm{N}(\mathrm{N}(P)) = \mathrm{N}(P)$. No proper subgroup of a nilpotent group equals its normalizer, so we must have $\mathrm{N}(P) = G$. Conversely, suppose all the Sylow subgroups of $G$ are normal. Then $G$ is isomorphic to a direct product of its Sylow subgroups, by the Sylow theorems. The Sylow subgroups are finite $p$-groups, hence they are nilpotent, so their direct product is nilpotent too. $\square$

The thrust of Theorem 5.21 is that a finite group is nilpotent if and only if it is a direct product of $p$-groups (for varying primes $p$). So there is a special method of proving a finite group is nilpotent: show all of its Sylow subgroups are normal.

Theorem 5.21 leads to a number of characterizations of nilpotency of finite groups. One of the characterizations involves subnormal subgroups. A subnormal subgroup of a group is a normal subgroup of a normal subgroup of $\ldots$ of a normal subgroup of the group. Essentially, subnormality is the "transitive extension" of the relation of being a normal subgroup. In particular, every subnormal proper subgroup is normal in some larger subgroup, so $H \neq \mathrm{N}(H)$ when $H$ is subnormal.

**Theorem 5.22.** *For a nontrivial finite group $G$, the following are equivalent to nilpotency:*

  (1) *for every proper subgroup $H$, $H \neq \mathrm{N}(H)$,*
  (2) *every subgroup of $G$ is subnormal,*
  (3) *every nontrivial quotient group of $G$ has a nontrivial center,*
  (4) *elements of relatively prime order in $G$ commute,*
  (5) *if $d \mid |G|$ then there is a normal subgroup of size $d$.*

*Proof.* To show most of these properties imply nilpotency when $G$ is finite, we will show most of these properties, for a finite group, imply the Sylow subgroups are normal.

<!-- page 21 -->

We saw nilpotency implies (1) in Theorem 5.15. Now assume (1) is true. Let $P$ be a Sylow subgroup of $G$. From the Sylow theorems, $\mathrm{N}(\mathrm{N}(P)) = \mathrm{N}(P)$, so $\mathrm{N}(P)$ is its own normalizer. Therefore $\mathrm{N}(P) = G$ by (1), so $P \lhd G$. Thus all the Sylow subgroups of $G$ are normal, so $G$ is nilpotent.

If $G$ is nilpotent and $H$ is a proper subgroup with $Z_i \subset H$ then $Z_{i+1} \subset \mathrm{N}(H)$. (We showed this in the proof of Theorem 5.15(2).) Repeating this enough times shows an iterated normalizer of $H$ eventually equals $G$, so $H$ is subnormal. Conversely, if (2) is true then $H \neq \mathrm{N}(H)$ for every proper subgroup $H$, so $G$ is nilpotent by (1).

Since nilpotency of $G$ implies nilpotency of every quotient, (3) is immediate. Conversely, if (3) is true then $G/Z_i$ has a nontrivial center when $Z_i \neq G$. Therefore $Z_{i+1} \neq Z_i$ when $Z_i \neq G$. This can't continue indefinitely, so some $Z_i$ equals $G$.

If (4) is true let $P_1, \ldots, P_m$ be a set of nontrivial Sylow subgroups of $G$ for the different primes dividing $|G|$. Elements in $P_i$ and $P_j$ commute when $i \neq j$, by (4), so the map $P_1 \times \cdots \times P_m \to G$ given by $(x_1, \ldots, x_m) \mapsto x_1 \cdots x_m$ is a homomorphism between groups of equal size. Since the $x_i$'s commute and have relatively prime order, they multiply to the identity only when each $x_i$ is trivial, so this map is injective and thus is an isomorphism. This implies $G$ is a direct product of finite $p$-groups, so it is nilpotent. Conversely, to see that in a finite nilpotent group (4) is true, write $G$ as a direct product of its Sylow subgroups. In this product decomposition, two elements in $G$ with relatively prime order don't have a nontrivial component in a common $p$-Sylow coordinate, so they commute.

To show (5) is equivalent to nilpotency for finite groups, first recall (5) is true for finite $p$-groups (see Corollary 6.13 in https://kconrad.math.uconn.edu/blurbs/grouptheory/conjclass.pdf). Next, in a direct product of $p$-groups for different $p$, say $P_1 \times \cdots \times P_m$ where $|P_i| = p_i^{e_i}$, to construct a normal subgroup with size $d$ write $d = p_1^{f_1} \cdots p_m^{f_m}$ and use $H_1 \times \cdots \times H_m$ where $H_i$ is normal of size $p_i^{f_i}$ in $P_i$. Conversely, if (5) is true then letting $d$ be the maximal power of a prime dividing $|G|$ shows the Sylow subgroups are normal. $\square$

**Remark 5.23.** The analogue of Theorem 5.22(3) for subgroups (a finite group is nilpotent if and only if all of its nontrivial subgroups have nontrivial center) is false: the nonabelian semidirect product $\mathbf{Z}/(3) \rtimes \mathbf{Z}/(4)$ is not nilpotent (it has more than one 2-Sylow subgroup), but its proper subgroups are all cyclic and thus have nontrivial center. The properties in Theorem 5.22 are not equivalent to nilpotency when $G$ is infinite. For example, there are infinite groups with trivial center (hence not nilpotent) in which every proper subgroup $H$ has $H \neq \mathrm{N}(H)$. See [13].

The following interesting theorem of Philip Hall extends the Sylow theorems in solvable groups.

**Theorem 5.24** (P. Hall, 1928). *Let $G$ be a finite solvable group and $d$ be a divisor of $|G|$ such that $(d, |G|/d) = 1$. Then*

  (1) *there exists a subgroup of $G$ with size $d$,*
  (2) *all subgroups of $G$ with size $d$ are conjugate,*
  (3) *if $d' \mid d$ then each subgroup of $G$ with size $d'$ is inside a subgroup of $G$ with size $d$.*

*Proof.* See [15, pp. 140--141]. $\square$

There is an extra part of Hall's theorem that generalizes the congruence $n_p \equiv 1 \bmod p$ from Sylow theory. For that, see [9, Sect. 9.3].

For a prime $p$, writing the size of a group as $p^k m$ with $p$ not dividing $m$, subgroups of index $p^k$ are called *$p$-Sylow complements* (or just Sylow complements if $p$ is understood). If

<!-- page 22 -->

$P$ is a $p$-Sylow subgroup and $H$ is a $p$-Sylow complement then $P \cap H$ is trivial and the set $PH$ coincides with the whole group. This justifies the label "complement."

Several years after proving Theorem 5.24, Hall discovered that the only finite groups that satisfy all the conclusions of his theorem are solvable. In fact, the existence of complements to Sylow subgroups is sufficient:

**Theorem 5.25** (Hall, 1937). *A finite group is solvable if and only if every Sylow subgroup has a complement.*

*Proof.* See [6, pp. 890--892]. $\square$

**Corollary 5.26.** *If a finite group satisfies the converse of Lagrange's theorem (that is, there is a subgroup of every size dividing the size of the group), then it is solvable.*

*Proof.* Such a group contains $p$-Sylow complements for every prime $p$ dividing the size, so the group is solvable by Theorem 5.25. $\square$

A group satisfying the converse of Lagrange's theorem is called *Lagrangian*. Every nilpotent group is Lagrangian by Theorem 5.22(5), and the Lagrangian groups lie strictly between the nilpotent and solvable finite groups: $S_4$ is Lagrangian but not nilpotent, and $A_4$ is solvable but not Lagrangian. Since $S_4$ and $A_4 \times \mathbf{Z}/(2)$ are both Lagrangian while $A_4$ is not, the Lagrangian property is not closed under passage to subgroups or quotient groups. Let's be frank: the Lagrangian property has no real significance in group theory.

In Theorem 5.25, we do not insist the complement to the Sylow subgroup is normal. In fact, asking for Sylow complements to be normal (and not just to exist) provides a characterization of (finite) nilpotent groups and thus provides a nice parallel description of solvability and nilpotency for finite groups:

**Theorem 5.27.** *A finite group is nilpotent if and only if every Sylow subgroup has a normal complement.*

*Proof.* Exercise. $\square$

Returning to Theorem 5.25, although we don't discuss the proof it is worth recording that its first nontrivial step is Burnside's famous $p^a q^b$-theorem:

**Theorem 5.28** (Burnside, 1904). *If $|G| = p^a q^b$ for primes $p$ and $q$, then $G$ is solvable.*

*Proof.* See [6, pp. 886--890] for Burnside's original proof, by representation theory. A purely group-theoretic proof of the theorem was found in the early 1970s [20, pp. 216--222]. $\square$

The conclusion of the $p^a q^b$-theorem is generally false when $|G|$ has three prime factors, *e.g.*, $A_5$ and $S_5$ are not solvable and $|A_5| = 60 = 2^2 \cdot 3 \cdot 5$ and $|S_5| = 120 = 2^3 \cdot 3 \cdot 5$.

By the Sylow theorems, a group $G$ of order $p^a q^b$ has subgroups $P$ and $Q$ of orders $p^a$ and $q^b$. Then $P \cap Q$ is trivial, so $G = PQ$ by counting. With this in mind, here is a generalization of Burnside's $p^a q^b$ theorem using nilpotent subgroups in place of prime-power subgroups.

**Theorem 5.29.** *If $G$ is a finite group and $G = MN$ where $M$ and $N$ are nilpotent, then $G$ is solvable. More generally, a finite group $G$ is solvable if and only if there are nilpotent subgroups $N_1, N_2, \ldots, N_r$ such that $G = N_1 N_2 \cdots N_r$ with $N_i N_j = N_j N_i$ for all $i$ and $j$.*

A proof of this theorem is technical and is omitted. When $G$ is solvable, a nilpotent decomposition can be achieved using some of its Sylow subgroups, one for each prime dividing $|G|$. (Not all choices of Sylow subgroups will work since the commuting condition
$N_i N_j = N_j N_i$ may not hold for all the Sylow subgroups.) This was shown by Hall in 1937 and it generalizes the Sylow subgroup direct product decomposition for finite nilpotent groups. To prove, conversely, that a finite group admitting a decomposition into setwise commuting nilpotent subgroups is solvable uses Theorem 5.25 as a solvability criterion: the group is shown to have a Sylow complement for every prime. This converse direction was proved partially by Wielandt (1958) and in full by Kegel (1961), so Theorem 5.29 is called the Kegel-Wielandt theorem.

The next theorem is the deepest result about solvability of finite groups and illustrates the special role of the prime 2 in finite group theory.

**Theorem 5.30** (Feit-Thompson, 1963). *If $|G|$ is odd, then $G$ is solvable.*

*Proof.* See [8]. The proof is 255 pages long and occupies an entire volume of the Pacific Journal of Mathematics. $\square$

Since a nontrivial solvable group not of prime order contains a nontrivial proper normal subgroup (Theorem 5.19), all nonabelian finite simple groups have even order by the Feit-Thompson theorem. In particular, all nonabelian finite simple groups contain an element of order 2. This is the first step in the classification of the finite simple groups.

The classification of finite simple groups can be used to provide further characterizations of nilpotent and solvable finite groups:

  - $G$ is nilpotent if and only if $\mathrm{N}(P)$ is nilpotent for all Sylow subgroups $P$ of $G$ [3]. (After the fact, we must have $P \lhd G$ since $G$ is nilpotent, so in fact $\mathrm{N}(P) = G$ for all Sylow subgroups.)
  - $G$ is solvable if and only if its 2-Sylow and 3-Sylow subgroups have complements [1]. (Thus we only need to check the primes $p = 2$ and $p = 3$ in Theorem 5.25 to know a group is solvable.)

In addition to Hall's theorem about the existence and conjugacy of certain subgroups in solvable groups, there is another theorem of Carter [5] about conjugate subgroups in solvable groups:

**Theorem 5.31** (Carter, 1961). *Every finite solvable group contains a nilpotent subgroup $H$ such that $\mathrm{N}(H) = H$, and all such subgroups are conjugate.*

*Proof.* See [15, pp. 142--143]. $\square$

The subgroups described in this theorem (self-normalizing and nilpotent) are called *Carter subgroups*. The Carter subgroups of $S_3$, $S_4$, and $D_n$ are the 2-Sylow subgroups. While Carter subgroups always exist in finite solvable groups, they might not exist in a nonsolvable group (there are no Carter subgroups in $A_5$). However, whenever group theorists found more than one Carter subgroup in a nonsolvable group these subgroups always turned out to be conjugate. So the conjecture arose that the Carter subgroups of a finite group are conjugate when they exist. This is true, and its proof [21] depends on the classification of finite simple groups.

## Appendix A. Proof of the Jordan-Holder Theorem

We return to the Jordan-Holder theorem from Section 2. Recall its statement: if $G$ is a nontrivial group and

$$\{e\} = G_0 \lhd G_1 \lhd G_2 \lhd \cdots \lhd G_r = G \tag{A.1}$$

<!-- page 24 -->

and

$$\{e\} = \widetilde{G}_0 \lhd \widetilde{G}_1 \lhd \widetilde{G}_2 \lhd \cdots \lhd \widetilde{G}_s = G \tag{A.2}$$

are both composition series for $G$ (that means the factors in both series are simple groups) then $r = s$ and there is $\pi \in S_r$ such that $\widetilde{G}_i/\widetilde{G}_{i-1} \cong G_{\pi(i)}/G_{\pi(i)-1}$ for $1 \leq i \leq r$. To prove the Jordan-Holder theorem, the bulk of the work is contained in the following basic result, called the Schreier refinement theorem. It was proved by Schreier in 1928, nearly 40 years after Jordan proved the Jordan-Holder theorem.

**Theorem A.1** (Schreier). *For two normal series of a group, intermediate subgroups can be inserted to yield two new normal series for the group whose factor groups coincide up to isomorphism, counting multiplicity.*

*Proof.* This is a nice application of the ideas in Theorems 3.1 and 3.5. We follow an argument from [2].

Starting with (A.1), taking the intersection of each subgroup with $\widetilde{G}_{j+1}$ produces (by Theorem 3.1) the normal series

$$\{e\} \lhd \widetilde{G}_{j+1} \cap G_1 \lhd \widetilde{G}_{j+1} \cap G_2 \lhd \cdots \lhd \widetilde{G}_{j+1} \cap G_r = \widetilde{G}_{j+1}$$

for $\widetilde{G}_{j+1}$. Since $\widetilde{G}_j \lhd \widetilde{G}_{j+1}$, we can multiply each subgroup in this new normal series by $\widetilde{G}_j$ to get an analogue of (3.2):

$$\widetilde{G}_j \lhd \widetilde{G}_j(\widetilde{G}_{j+1} \cap G_1) \lhd \widetilde{G}_j(\widetilde{G}_{j+1} \cap G_2) \lhd \cdots \lhd \widetilde{G}_j(\widetilde{G}_{j+1} \cap G_r) = \widetilde{G}_{j+1}.$$

This is a chain of subgroups between $\widetilde{G}_j$ and $\widetilde{G}_{j+1}$ with each subgroup normal in the next one. In this series, there are $r$ factors. (Some factors might be trivial.) Linking these series together over $j = 0, 1, \ldots, s - 1$ produces a normal series for $G$ with $rs$ factors of the form

$$\widetilde{G}_j(\widetilde{G}_{j+1} \cap G_{i+1})/\widetilde{G}_j(\widetilde{G}_{j+1} \cap G_i) \tag{A.3}$$

as $i$ and $j$ vary from 0 to $r - 1$ and 0 to $s - 1$, respectively.

In the same way, intersecting the series (A.2) with $G_{i+1}$ and then multiplying the result by $G_i$ (which is normal in $G_{i+1}$) gives a series of subgroups between $G_i$ and $G_{i+1}$ that string together over all $i$ to a normal series of $G$ with $sr = rs$ factors of the form

$$G_i(G_{i+1} \cap \widetilde{G}_{j+1})/G_i(G_{i+1} \cap \widetilde{G}_j) \tag{A.4}$$

as $i$ and $j$ vary.

The two refinements we have made to (A.1) and (A.2) each have $rs$ factors, and we will show the quotient groups in (A.3) and (A.4) for the same $i$ and $j$ are isomorphic. These quotient groups both have the form $HJ/HK$ where the $J$ in both quotients is the same ($J = \widetilde{G}_{j+1} \cap G_{i+1}$), while the $H$'s and $K$'s in the two quotients are not (usually) the same. We do have $K \subset J$ both times, since $G_i \subset G_{i+1}$ and $\widetilde{G}_j \subset \widetilde{G}_{j+1}$.

To prove (A.3) and (A.4) are isomorphic, we want to simplify a group of the form $HJ/HK$ by cancelling the $H$'s, assuming $K \subset J$ (as in our application of interest). This should leave us with a certain quotient group of $J$ (recall $J$ in (A.3) and (A.4) are the same). To make this explicit, look at the natural map $f: J \to HJ/HK$. This is onto (since $H \subset HK$). If $x \in J$ is in the kernel then $x = hk$ for some $h \in H$ and $k \in K$, so $h = xk^{-1} \in J$ (because $K \subset J$), so $h \in H \cap J$. Therefore the kernel of $f$ is inside $(H \cap J)K$. Also $(H \cap J)K$ dies under $f$ since it is inside of $HK$, so $\ker f = (H \cap J)K$. That means $J/((H \cap J)K) \cong HJ/HK$, so we have expressed $HJ/HK$ as a quotient of $J$, at least up to isomorphism. In (A.3) and

<!-- page 25 -->

(A.4), the $H \cap J$ in one quotient equals the $K$ in the other. That is, the quotient groups in (A.3) and (A.4) are both isomorphic to

$$\frac{(G_{i+1} \cap \widetilde{G}_{j+1})}{(G_i \cap \widetilde{G}_{j+1})(G_{i+1} \cap \widetilde{G}_j)},$$

and thus they are isomorphic to each other. $\square$

The proof of the Jordan-Holder theorem is now easy.

*Proof.* If a group admits two composition series then Schreier's refinement theorem says they can be refined to two normal series whose factor groups coincide up to isomorphism, counting multiplicity. The key feature of a composition series is that it can only be refined in a trivial way, *i.e.*, by repeating some of the subgroups already in the series. Therefore the factors in a composition series of a group are the nontrivial factors in all of the refinements of the composition series. That shows two composition series of a group have the same (nontrivial) factors up to isomorphism, counting multiplicity. $\square$

One other use of the Schreier refinement theorem is that it shows if a group admits at least one composition series then every normal series for the group can be refined to a composition series. Indeed, start with a normal series and a composition series for the group and refine them by the Schreier refinement theorem to normal series for the group whose factor groups coincide up to isomorphism, counting multiplicity. Then the refinement of the original normal series will be a composition series after all repeated subgroups in its refinement are replaced with one copy of that subgroup.

Let's put the Jordan-Holder theorem to work.

**Corollary A.2.** *Suppose $f$ is a function defined on finite simple groups, with values in $\mathbf{Z}$, which has the same value on isomorphic simple groups. There is exactly one way to extend $f$ to a function on all finite groups satisfying the following two properties:*

  (a) *$f$ takes the same value on isomorphic groups,*
  (b) *$f(G) = f(N) + f(G/N)$ whenever $N \lhd G$.*

*Explicitly, $f(e) = 0$ and when $G$ is nontrivial with composition series (A.1),*

$$f(G) = \sum_{i=0}^{r-1} f(G_{i+1}/G_i). \tag{A.5}$$

*Proof.* First we assume $f$ exists satisfying (a) and (b), and show it must be given by (A.5) on nontrivial groups. Then we show (A.5) (along with $f(e) = 0$) satisfies (a) and (b).

When $G$ is trivial, let $N = G$. Then $f(G) = f(N) = f(G/N)$ by (a), so $f(G) = 0$ by (b).

When $G$ is nontrivial, let (A.1) be a composition series for $G$. If $r \geq 1$, then since $G_{r-1} \lhd G$ we have $f(G) = f(G_{r-1}) + f(G/G_{r-1})$ by (b). The series (A.1) with the top group removed is a composition series for $G_{r-1}$, so by induction on the length of a composition series, $f(G_{r-1}) = \sum_{i=0}^{r-2} f(G_{i+1}/G_i)$ (the sum is empty if $r = 1$). Adding $f(G/G_{r-1})$ to both sides recovers the formula (A.5) for $G$.

Conversely, we now define $f$ to be 0 on trivial groups and to have the value (A.5) on nontrivial finite groups $G$. We want to show (a) and (b) are satisfied. First, however, we need to check (A.5) is well-defined. What if we change the composition series for $G$? By the Jordan-Holder theorem, the set of simple factors in the two series are the same up to isomorphism and multiplicity. Therefore the sum in (A.5) is the same for all choices of composition series of $G$, so (A.5) is well-defined.

<!-- page 26 -->

Part (a) is now immediate: forming composition series for two isomorphic finite groups, we can use the isomorphism to transfer the composition series for one group over to the other group, leaving us with two composition series on the same group, and they yield the same value for (A.5) by Jordan-Holder.

To check (b), we build a composition series in a convenient way. Since (b) is clear if $N$ is trivial or if $N = G$, we may assume $N$ is neither $\{e\}$ nor $G$. Make a composition series for $G/N$, lift it up to $G$ to get a normal series from $N$ to $G$ with simple factors, and then tack on a composition series for $N$. The result is a composition series for $G$ containing $N$ as one term, with the (simple) factors from $G$ down to $N$ having the same (simple) factors up to isomorphism and multiplicity as the chosen composition series of $G/N$. Applying (A.5), the part of the sum using simple factors from subgroups of $N$ equals $f(N)$ and the rest of the sum equals $f(G/N)$. $\square$

In this proof, we really didn't need the values of $f$ to lie in $\mathbf{Z}$. They could lie in an abelian group and the proof goes through.

## Appendix B. Matrix Groups

Normal series for matrix groups are important. For a field $F$, the standard normal series for $\mathrm{GL}_n(F)$, when $n \geq 2$ (the case $n = 1$ is not interesting) is

$$\{I_n\} \lhd \mathrm{SL}_n(F) \lhd \mathrm{GL}_n(F),$$

The center of $\mathrm{SL}_n(F)$ is $\mu_n(F)I_n$ (scalar diagonal matrices with an $n$-th root of unity from $F$ on the diagonal), so we can refine the above series to

$$\{I_n\} \lhd \mu_n(F)I_n \lhd \mathrm{SL}_n(F) \lhd \mathrm{GL}_n(F).$$

The first and last quotients are abelian, while $\mathrm{SL}_n(F)/\mu_n(F)I_n = \mathrm{PSL}_n(F)$ is usually not abelian. This is usually not a composition series, *e.g.*, $\mu_n(F)$ is cyclic and thus can be decomposed further if it is not of prime order.

It can be shown that $[\mathrm{SL}_n(F), \mathrm{SL}_n(F)] = \mathrm{SL}_n(F)$ except when $n = 2$ and $|F| \leq 3$, so for $n > 2$ or $|F| > 3$ the derived series of $\mathrm{SL}_n(F)$ never gets lower than the full group. Thus $\mathrm{SL}_n(F)$ is not solvable, so $\mathrm{GL}_n(F)$ is also not solvable. If $n = 2$ and $|F| \leq 3$ then $\mathrm{GL}_2(F)$ is solvable, so $\mathrm{SL}_2(F)$ is solvable too. Neither of these groups is nilpotent.

Nilpotent and solvable matrix groups naturally occur among triangular matrices. For $n \geq 2$, let $\mathrm{T}_n(F)$ be the group of invertible upper triangular matrices in $\mathrm{GL}_n(F)$:

$$\begin{pmatrix} * & * & * & \cdots & * & * \\ 0 & * & * & \cdots & * & * \\ 0 & 0 & * & \cdots & * & * \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & * & * \\ 0 & 0 & 0 & \cdots & 0 & * \end{pmatrix}$$

(Although this makes sense when $n = 1$, with $\mathrm{T}_1(F) = F^\times$, this case is boring for our purposes so we don't pay attention to it.) It is useful to view $\mathrm{T}_n(F)$ as the stabilizer of the standard subspace filtration of $F^n = Fe_1 \oplus Fe_2 \oplus \cdots \oplus Fe_n$. Specifically, let $V_0 = \{0\}$ and $V_k = Fe_1 \oplus \cdots \oplus Fe_k$ for $k = 1, \ldots, n$. Then $F^n$ can be filled up by the $V_k$'s:

$$\{0\} = V_0 \subset V_1 \subset V_2 \subset \cdots \subset V_n = F^n.$$
A matrix $g \in \mathrm{M}_n(F)$ is in $\mathrm{T}_n(F)$ if and only if $g(V_k) = V_k$ for all $k$. (Having $g(V_k) \subset V_k$ for all $k$ is equivalent to $g$ being upper-triangular, while the more precise $g(V_k) = V_k$ for all $k$ forces each diagonal entry to be nonzero, hence the matrix is invertible.) The condition "$g(V_k) = V_k$ for all $k$" is closed under multiplication and inversion on $g$, which is the *non-tedious* way to show $\mathrm{T}_n(F)$ is a group.

We now introduce a normal series for $\mathrm{T}_n(F)$. Each $g \in \mathrm{T}_n(F)$ defines a linear map on the quotient spaces $V_\ell/V_k$ for $\ell > k$. For $i = 1, \ldots, n$, set

$$\mathrm{UT}_n^i(F) = \{g \in \mathrm{T}_n(F) : g|_{V_{k+i}/V_k} = \mathrm{id}. \text{ for } 0 \leq k \leq n - i\}$$

$$= \{g \in \mathrm{T}_n(F) : g|_{V_i} = \mathrm{id}_{V_i}, g(e_j) - e_j \in V_{j-i} \text{ for } j > i\}.$$

(The label UT stands for unipotent-triangular.) Thus $\mathrm{UT}_n(F) := \mathrm{UT}_n^1(F)$ is the subgroup consisting of matrices in $\mathrm{T}_n(F)$ with 1's along the main diagonal:

$$\begin{pmatrix} 1 & * & * & \cdots & * & * \\ 0 & 1 & * & \cdots & * & * \\ 0 & 0 & 1 & \cdots & * & * \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 1 & * \\ 0 & 0 & 0 & \cdots & 0 & 1 \end{pmatrix}. \tag{B.1}$$

For instance, $\mathrm{UT}_3(F) = \mathrm{Heis}(F)$. We will see that $\mathrm{T}_n(F)$ is solvable and its subgroup $\mathrm{UT}_n(F)$ is nilpotent. These are the most important examples of solvable and nilpotent groups in mathematics.

The matrices in $\mathrm{UT}_n^2(F)$ have 1's along the main diagonal and 0's along the superdiagonal:

$$\begin{pmatrix} 1 & 0 & * & \cdots & * & * \\ 0 & 1 & 0 & \cdots & * & * \\ 0 & 0 & 1 & \cdots & * & * \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 1 & 0 \\ 0 & 0 & 0 & \cdots & 0 & 1 \end{pmatrix}.$$

Notice the matrices in $\mathrm{UT}_n^2(F)$ have $2 \times 2$ identity matrices down the main diagonal. More generally, $\mathrm{UT}_n^i(F)$ for $1 \leq i \leq n$ consists of matrices in $\mathrm{T}_n(F)$ with $i \times i$ identity matrices down the main diagonal and arbitrary entries above them. (In terms of matrix entries, these matrices have 1's along the main diagonal and 0's in the first $i - 1$ upper diagonals that are parallel to and above the main diagonal.)

We have the subgroup series

$$\mathrm{T}_n(F) \supset \mathrm{UT}_n(F) \supset \mathrm{UT}_n^2(F) \supset \cdots \supset \mathrm{UT}_n^n(F) = \{I_n\}. \tag{B.2}$$

This is a normal series, since $\mathrm{UT}_n(F)$ is the kernel of the homomorphism $\mathrm{T}_n(F) \to (F^\times)^n$ that projects upper-triangular matrices onto their sequence of diagonal entries and, for $i \geq 1$, $\mathrm{UT}_n^{i+1}(F)$ is the kernel of the map $\mathrm{UT}_n^i(F) \to F^{n-i}$ that projects onto the $i$th upper diagonal (the first upper diagonal that is not automatically 0 in $\mathrm{UT}_n^i(F)$). The factors of (B.2) are

$$\mathrm{T}_n(F)/\mathrm{UT}_n(F) \cong (F^\times)^n, \quad \mathrm{UT}_n^i(F)/\mathrm{UT}_n^{i+1}(F) \cong F^{n-i} \tag{B.3}$$

<!-- page 28 -->

for $i = 1, \ldots, n - 1$. These are abelian, so $\mathrm{T}_n(F)$ is a solvable group. In terms of the derived series for $G = \mathrm{T}_n(F)$, when $F \neq \mathbf{Z}/(2)$, $G^{(i)} = \mathrm{UT}_n^{2^{i-1}}(F)$. (Notice the rapid decay of the derived series, which is exponential in $n$.)

The group $\mathrm{T}_n(F)$ is not nilpotent, because

$$[\mathrm{T}_n(F), \mathrm{UT}_n(F)] = \mathrm{UT}_n(F), \quad [\mathrm{T}_n(F), \mathrm{T}_n(F)] = \mathrm{UT}_n(F), \tag{B.4}$$

so the lower central series of $\mathrm{T}_n(F)$ is $L_i = \mathrm{UT}_n(F)$ for $i \geq 1$.

The group $\mathrm{UT}_n(F)$ has lower and upper central series

$$L_i = \mathrm{UT}_n^{i+1}(F), \quad Z_i = \mathrm{UT}_n^{n-i}(F),$$

so $\mathrm{UT}_n(F)$ is nilpotent. Its lower and upper central series are exactly the same except for the indexing running in the opposite orders in both series.

Here is a brief indication of the importance of the groups $\mathrm{T}_n(F)$ when $F = \mathbf{C}$. It is a theorem of linear algebra that every matrix in $\mathrm{GL}_n(\mathbf{C})$ is conjugate to an upper-triangular matrix. That means the subgroup $\mathrm{T}_n(\mathbf{C})$ and its conjugates fill up $\mathrm{GL}_n(\mathbf{C})$. So $\mathrm{GL}_n(\mathbf{C})$ is covered by a conjugacy class of solvable subgroups. Moreover, $\mathrm{T}_n(\mathbf{C})$ is connected and every *connected* solvable subgroup of $\mathrm{GL}_n(\mathbf{C})$ is conjugate to a subgroup of $\mathrm{T}_n(\mathbf{C})$ (Lie-Kolchin theorem). It is false that arbitrary solvable subgroups of $\mathrm{GL}_n(\mathbf{C})$ can be conjugated into $\mathrm{T}_n(\mathbf{C})$. For instance, the dihedral group $D_m$ can be embedded in $\mathrm{GL}_2(\mathbf{C})$ but it can't be embedded in $\mathrm{T}_2(\mathbf{C})$ since two noncommuting elements of order 2 in $\mathrm{T}_2(\mathbf{C})$ never have a product with finite order greater than 2 (like $rs$ and $s$ do in $D_m$).

We can express $\mathrm{T}_n(\mathbf{C})$ as a semidirect product using $\mathrm{UT}_n(\mathbf{C})$: $\mathrm{T}_n(\mathbf{C}) \cong \mathrm{UT}_n(\mathbf{C}) \rtimes (\mathbf{C}^\times)^n$, where $(\mathbf{C}^\times)^n$ corresponds to the subgroup of diagonal matrices in $\mathrm{T}_n(\mathbf{C})$, on which $\mathrm{UT}_n(\mathbf{C})$ acts by conjugation. More generally, in every connected subgroup $G \subset \mathrm{GL}_n(\mathbf{C})$ there is a maximal connected solvable normal subgroup $B \subset G$, and this subgroup $B$ can be expressed as a semidirect product of a nilpotent normal subgroup and a group isomorphic to a product of copies of $\mathbf{C}^\times$, just as with $\mathrm{T}_n(\mathbf{C})$.

The groups $\mathrm{T}_n(\mathbf{F})$ and $\mathrm{UT}_n(\mathbf{F})$ for finite $\mathbf{F}$ suggest an analogy between $\mathrm{GL}_n(\mathbf{F})$ and an arbitrary finite group $G$. The group $U = \mathrm{UT}_n(\mathbf{F})$ is a Sylow subgroup of $\mathrm{GL}_n(\mathbf{F})$ ($p$-Sylow with $p$ equal to the characteristic of $\mathbf{F}$), so we will take as its analogue in $G$ a Sylow subgroup, say $P$. In $\mathrm{GL}_n(\mathbf{F})$, $T = \mathrm{T}_n(\mathbf{F})$ equals the normalizer of $U$, so an analogue of $T$ in $G$ is the normalizer of $P$. This is recorded in Table 4.

| $\mathrm{GL}_n(\mathbf{F})$ | $G$ |
|---|---|
| $U = \mathrm{UT}_n(\mathbf{F})$ | Sylow subgroup $P$ |
| $T = \mathrm{T}_n(\mathbf{F})$ | $\mathrm{N}(P)$ |

Table 4.

Both $U$ and $P$ are nilpotent (they are groups of prime-power size), but $T$ is solvable while $\mathrm{N}(P)$ need not be solvable and $T/U \cong (\mathbf{F}^\times)^n$ is abelian while $\mathrm{N}(P)/P$ need not be abelian. Nevertheless, we will show that Table 4 can suggest fruitful ideas.

Let $D$ be the group of $n \times n$ invertible diagonal matrices over $\mathbf{F}$. This group is a "complement" to $U$ in $T$: $D$ and $U$ intersect trivially and $T = DU = UD$. We therefore ask if there is a subgroup $K \subset \mathrm{N}(P)$ such that $P \cap K$ is trivial and $\mathrm{N}(P) = PK$. There is! Our analogy has led us to guess a special case of an important theorem about finite groups.

<!-- page 29 -->

**Theorem B.1** (Schur-Zassenhaus). *If $H$ is a finite group and $N$ is a normal subgroup of $H$ such that $(|N|, |H/N|) = 1$, then there is a subgroup $K \subset H$ such that $N \cap K$ is trivial and $H = NK$. Moreover, all choices for $K$ are conjugate to each other.*

*Proof.* See [19, pp. 246--248]. The proof that all choices for $K$ are conjugate uses solvability of either $N$ or $H/N$. Why is at least one of these solvable? Since $N$ and $H/N$ have relatively prime orders, at least one of them has odd order (they can't both have even order!), so at least one of $N$ and $H/N$ is solvable by the Feit-Thompson theorem. That is all we will say about the proof. $\square$

Take $H = \mathrm{N}(P)$ and $N = P$ to get a complement to $P$ in $\mathrm{N}(P)$.

**Example B.2.** If $H = A_4$ and $N = V$, choices for $K$ include $\langle (123) \rangle$ and $\langle (124) \rangle$. These are conjugate.

Invoking the Feit-Thompson theorem in the proof the Schur-Zassenhaus theorem is quite out of proportion with the other details in the proof, so it's probably a good idea to check, when using the Schur-Zassenhaus theorem, if the solvability of $N$ or $H/N$ in the particular application is known *a priori* for elementary reasons. For instance, in the analogy we were building between $\mathrm{GL}_n(\mathbf{F})$ and an arbitrary finite group $G$, the role of $N$ is played by a Sylow subgroup $P$ (normal in $\mathrm{N}(P)$), which is nilpotent and therefore solvable. Hence, to say every Sylow subgroup of a finite group has a complementary subgroup inside its normalizer by the Schur-Zassenhaus theorem does not require appealing to the Feit-Thompson theorem, because the Sylow subgroup is trivially solvable.

## References

[1] Z. Arad and M. B. Ward, *New criteria for solvability of finite groups*, J. Algebra **77** (1982), 234--246.

[2] B. Baumslag, *A Simple Way of Proving the Jordan-Holder-Schreier Theorem*, Amer. Math. Monthly **113** (2006), 933--935.

[3] M. Bianchi, A. G. B. Mauri, and P. Hauck, *On finite groups with nilpotent Sylow-normalizers*, Arch. Math. (Basel) **47** (1986), 193--197.

[4] A. Borel, "Linear Algebraic Groups," 2nd ed., Springer-Verlag, New York, 1991.

[5] R. W. Carter, *Nilpotent self-normalizing subgroups of soluble groups*, Math. Z. **75** (1961), 136--139.

[6] D. Dummit and R. Foote, "Abstract Algebra," 3rd ed., Wiley, New York, 2004.

[7] A. Facchini, *The Krull-Schmidt theorem*, pp. 357--397 in: Handbook of algebra, Vol. 3, North-Holland, Amsterdam, 2003.

[8] W. Feit and J. Thompson, *Solvability of groups of odd order*, Pacific J. Math. **13** (1963), 775--1029.

[9] M. Hall, "Theory of Groups," Macmillan, New York, 1959.

[10] P. Hall, *Finite-by-nilpotent groups*, Proc. Cambridge Philos. Soc. **52** (1956), 611--616.

[11] P. Hall, "Edmonton Notes on Nilpotent Groups," Queen Mary College Mathematics Notes, Queen Mary College, London, 1969.

[12] P. Hilton, *On Variants of a Theorem of Schur*, Int. J. Math. Math. Sci **2005** (2005), 3269--3272.

[13] H. Heineken and I. J. Mohamed, *A group with trivial centre satisfying the normalizer condition*, J. Algebra **10** (1968), 368--376.

[14] T. Hungerford, "Algebra," Springer-Verlag, New York, 1974.

[15] M. I. Kargapolov and Y. I. Merzlyakov, "Fundamentals of the theory of groups," Springer-Verlag, New York, 1979.

[16] E. I. Khukhro, "Nilpotent Groups and Their Automorphisms," de Gruyter, Berlin, 1993.

[17] F. Levi, *Groups in which the commutator operation satisfies certain algebraic conditions*, J. Indian Math. Soc. **6** (1942), 87--97.

[18] J. Nicholson, *The Development and Understanding of the Concept of Quotient Group*, Historia Math. **20** (1993), 68--88.

[19] D. Robinson, "A Course in the Theory of Groups," 2nd ed., Springer-Verlag, New York, 1996.

<!-- page 30 -->

[20] M. Suzuki, "Group Theory II," Springer-Verlag, New York, 1986.

[21] E. P. Vdovin, *Carter subgroups of finite almost simple groups*, Algebra i Logika **46** (2007), 157--216.

[22] G. Zappa, *Remark on a recent paper of O. Ore*, Duke Math. J. **6** (1940), 511--512.
