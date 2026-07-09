# Subgroup Series II

> **Source**: https://kconrad.math.uconn.edu/blurbs/subgpseries2.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory

<!-- page 1 -->

## 1. Introduction

In part I, we met nilpotent and solvable groups, defined in terms of normal series. Recalling the definitions, a group $G$ is called nilpotent if it admits a normal series

$$
\{e\} = G_0 \triangleleft G_1 \triangleleft G_2 \triangleleft \cdots \triangleleft G_r = G \tag{1.1}
$$

in which $G_i \triangleleft G$ and $G_{i+1}/G_i \subset Z(G/G_i)$ for all $i$. We call $G$ solvable if it admits a normal series (1.1) in which $G_{i+1}/G_i$ is abelian for all $i$. Every nilpotent group is solvable.

Nilpotent groups include finite $p$-groups. Some theorems about $p$-groups extend to nilpotent groups (*e.g.*, all nontrivial normal subgroups of a nilpotent group have a nontrivial intersection with the center). Nilpotency for finite groups has many characterizations.

**Theorem 1.1.** *For a nontrivial finite group $G$, the following are equivalent to nilpotency:*

1. *for every proper subgroup $H$, $H \neq \mathrm{N}(H)$,*
2. *every subgroup of $G$ is subnormal,*
3. *every nontrivial quotient group of $G$ has a nontrivial center,*
4. *elements of relatively prime order in $G$ commute,*
5. *if $d \mid |G|$ then there is a normal subgroup of size $d$,*
6. *the group is isomorphic to the direct product of its Sylow subgroups.*

We will meet other characterizations in Corollary 2.3 and Theorem 3.13.

In Section 2 we will look at the subgroup structure of nilpotent and solvable groups. Section 3 discusses two important nilpotent subgroups of a finite group: the Fitting subgroup and Frattini subgroup. In Section 4 we will meet supersolvable groups, which are a class of groups intermediate between nilpotent and solvable groups. In Section 5 we will discuss chief series, which are analogous to composition series and in terms of which nilpotent and supersolvable groups can be characterized. (While solvability can be defined in terms of composition series, that isn't true of nilpotency and supersolvability.)

## 2. Nilpotent and Solvable Groups: Subgroup Structure

Nilpotent and solvable groups have special features concerning their minimal normal subgroups and maximal subgroups. A minimal normal subgroup is a nontrivial normal subgroup that contains no other nontrivial normal subgroup. A maximal subgroup is a proper subgroup not contained in another proper subgroup. Nontrivial finite groups obviously have minimal normal subgroups and maximal subgroups. But an infinite abelian (hence nilpotent and solvable) group need not contain minimal normal subgroups (try $\mathbf{Z}$) or maximal subgroups (try $\mathbf{Q}$[^1]).

<!-- page 2 -->

**Remark 2.1.** Maximal normal subgroups naturally arise when constructing a composition series for a nontrivial finite group: let $G_0$ be $G$, $G_1$ be a maximal normal subgroup of $G_0$, $G_2$ be a maximal normal subgroup of $G_1$ (probably $G_2$ is not normal in $G$), $G_3$ be a maximal normal subgroup of $G_2$, and so on. When the process terminates at $\{e\}$ we will have a composition series where the subgroups descend rather than ascend as in (1.1).

**Theorem 2.2.** *If $G$ is a nontrivial nilpotent group then*

1. *every minimal normal subgroup has prime order and lies in the center,*
2. *every maximal subgroup $M$ is normal with prime index and contains the commutator subgroup,*
3. *if $G$ is finite and $p$ is a prime dividing $|G|$, there is a minimal normal subgroup of size $p$ and a maximal subgroup of index $p$.*

*Proof.* (1): Let $N$ be a minimal normal subgroup. Since $N$ is nontrivial and normal, $N \cap Z_1$ is nontrivial by nilpotency of $G$. Since $N \cap Z_1$ is a normal subgroup of $G$, by minimality of $N$ we have $N = N \cap Z_1$, so $N \subset Z_1$. Since $N$ is in the center of $G$, every subgroup of $N$ is a normal subgroup of $G$, so $N$ contains no proper nontrivial subgroups. It follows that $N$ is abelian and simple, so it has prime order.

(2): If $M$ is maximal then, since $M \neq \mathrm{N}(M)$ by nilpotency of $G$, we must have $\mathrm{N}(M) = G$, hence $M \triangleleft G$. The quotient group $G/M$ contains no proper nontrivial subgroups (otherwise we could lift one back to $G$ and violate the maximality of $M$), so $G/M$ has prime order. Then $G/M$ is abelian, so $G' \subset M$.

(3): Let $|G| = p^k m$ where $p$ does not divide $m$. We can write $G = P \times H$ where $P$ is the $p$-Sylow subgroup of $G$ and $H$ is the direct product of the Sylow subgroups for primes other than $p$. The center of $P$ is nontrivial and a subgroup of size $p$ in $Z(P)$ is a normal subgroup of $G$, necessarily minimal. The $p$-group $P$ contains a subgroup of index $p$, and its direct product with $H$ is a subgroup of $G$ with index $p$, which means it must be maximal. $\square$

**Corollary 2.3.** *A nontrivial finite group is nilpotent if and only if every maximal subgroup is normal.*

*Proof.* The "only if" direction follows from Theorem 2.2. Now assume every maximal subgroup of a finite group $G$ is normal, and let $P$ be a Sylow subgroup of $G$. Then $P \subset \mathrm{N}(P) \subset G$. If $\mathrm{N}(P) \neq G$ then $\mathrm{N}(P) \subset M \neq G$ with $M$ a maximal subgroup. Then $M \triangleleft G$. Since $P \subset M \subset G$, by Sylow theory $\mathrm{N}(M) = M$. Also $\mathrm{N}(M) = G$, since $M \triangleleft G$, so $M = G$. This is a contradiction, so $\mathrm{N}(P) = G$, which tells us all the Sylow subgroups of $G$ are normal, so $G$ is nilpotent. $\square$

**Theorem 2.4.** *If $G$ is a nontrivial finite solvable group then*

1. *every minimal normal subgroup is isomorphic to $(\mathbf{Z}/(p))^k$ for some prime $p$ and $k \geq 1$,*
2. *every maximal subgroup has prime-power index,*
3. *for some prime $p$ dividing $|G|$ there is a minimal normal $p$-subgroup,*
4. *for every prime $p$ dividing $|G|$ there is a maximal subgroup with $p$-power index.*

*Proof.* (1): Let $N$ be a minimal normal subgroup of $G$. Since $N$ is solvable and nontrivial, $N'$ is a proper subgroup of $N$. Since $N \triangleleft G$, $N' = [N, N] \triangleleft G$. Therefore by minimality of $N$ we must have $N' = \{e\}$, so $N$ is abelian. Let $p$ be a prime dividing $|N|$, so $\{x \in N : x^p = e\}$ is a nontrivial normal subgroup of $G$. Again by minimality of $N$, this subgroup is $N$, so $N$

<!-- page 3 -->

is a finite abelian group in which each element satisfies $x^p = e$. It follows that $N \cong (\mathbf{Z}/(p))^k$ for some $k$.

(2): We argue by induction on $|G|$. The result is clear if $|G|$ is a prime (or even a prime power), so we can assume $|G| \geq 6$, $|G|$ is not a prime and also that the result is true for solvable groups of smaller size. Let $M$ be a maximal subgroup of $G$. We want to show $[G : M]$ is a prime power. Let $N$ be a minimal normal subgroup in $G$, so $N \neq G$ (*e.g.*, the commutator subgroup of $G$ is a proper normal subgroup). Then $MN/N \subset G/N$, so $MN/N$ is solvable. Since $M \subset MN \subset G$, either $MN = M$ or $MN = G$ by maximality of $M$. In the first case $N \subset M$, so $M/N$ is a maximal subgroup of $G/N$. As $|G/N| < |G|$, by induction $[G/N : M/N]$ is a prime power. This index equals $[G : M]$. In the second case, $[G : M] = |G|/|M| = |MN|/|M| = |N|/|M \cap N|$, which is a prime power since $N$ is a $p$-group by (1).

(3): The group has a minimal normal subgroup, and by (1) this subgroup is a $p$-group for some prime $p$.

(4): We argue by induction on $|G|$. The result is clear if $|G|$ is a prime power (in particular, if $|G|$ is prime). Let $p$ be a prime dividing $|G|$ and $N$ be a minimal normal subgroup, so in particular $N$ has prime-power size (the prime is not necessarily $p$). Since $G/N$ is solvable, if $p \mid |G/N|$ then by induction $G/N$ has a maximal subgroup of $p$-power index, and the pullback of this subgroup to $G$ will be a maximal subgroup of $G$ with the same $p$-power index (in $G$). What if $p$ does not divide $|G/N|$? Then $p \mid |N|$, so $N$ must be a $p$-group, and therefore is a $p$-Sylow subgroup of $G$. Since $N$ is a normal subgroup with $(|N|, |G/N|) = 1$, by the Schur--Zassenhaus theorem there is a complement to $N$ in $G$: some $K \subset G$ has $N \cap K = \{e\}$ and $NK = G$, so $[G : K] = |N|$ is a power of $p$. A maximal subgroup of $G$ containing $K$ will have $p$-power index in $G$. $\square$

**Example 2.5.** A minimal normal subgroup of $S_4$ is $V \cong \mathbf{Z}/(2) \times \mathbf{Z}/(2)$.

Part (3) of the theorem can't be extended to all primes dividing $|G|$: there is no minimal normal 3-subgroup of $S_4$.

**Remark 2.6.** If $G$ is an infinite solvable group then part (1) of Theorem 2.4 can be extended to say every minimal normal subgroup $N$ is a vector space (over $\mathbf{Q}$ or some $\mathbf{Z}/(p)$ acting on $N$ as exponents). Here's how. The proof that $N$ is abelian goes through as before, so $x \mapsto x^b$ is a homomorphism $N \to N$ for all $b \in \mathbf{Z}$. Consider $N^p = \{x^p : x \in N\}$ for all primes $p$. These are normal subgroups of $G$, so they equal $N$ or $\{e\}$. If one of them is trivial then $N$ is a vector space over $\mathbf{Z}/(p)$ for that $p$. If instead $N^p = N$ for all $p$ then $x \mapsto x^p$ on $N$ is surjective with trivial kernel: $K_p := \{x \in N : x^p = e\}$ is a normal subgroup of $G$ contained in $N$, and $K_p \neq N$ since $N^p = N \neq \{e\}$ (minimal normal subgroups are nontrivial by definition), so $K_p = \{e\}$ for all $p$. Therefore $N$ is a torsion-free abelian group. The condition $N^p = N$ for all primes $p$ implies $N^b = N$ for all $b \in \mathbf{Z} - \{0\}$, so for each $x \in N$ and integers $a$ and $b$ with $b \neq 0$, $x^a = y^b$ for a unique $y \in N$. Define $x^{a/b} := y$ and check this gives $N$ the structure of a $\mathbf{Q}$-vector space.

Here is an analogue of nontrivial quotients of nilpotent groups having nontrivial center.

**Corollary 2.7.** *A nontrivial finite group is solvable if and only if every nontrivial quotient of it contains a nontrivial abelian normal subgroup.*

*Proof.* A nontrivial finite solvable group contains a nontrivial abelian normal subgroup, such as a minimal normal subgroup. Since every quotient of a solvable group is solvable,

<!-- page 4 -->

the "only if" direction is settled. For the "if" direction, we induct on the size of the group. For a group $G$ whose nontrivial quotients all contain nontrivial abelian normal subgroups, there is a nontrivial abelian normal subgroup $N$ in $G$. If $N = G$ then $G$ is abelian, hence solvable. Assuming $N \neq G$, both $N$ and $G/N$ are nontrivial with size less than $|G|$. Every quotient of $G/N$ is a quotient of $G$, so $G/N$ satisfies the hypotheses of the theorem. By induction, $G/N$ is solvable. As $N$ is abelian, it too is solvable. Therefore $N$ and $G/N$ are solvable, so $G$ is solvable. $\square$

It is false that a finite group is solvable if and only if its nontrivial subgroups all contain nontrivial abelian normal subgroups. For instance, $\mathrm{SL}_2(\mathbf{Z}/(5))$ satisfies $\mathrm{SL}_2(\mathbf{Z}/(5))' = \mathrm{SL}_2(\mathbf{Z}/(5))$, so the group is not solvable. But it has a nontrivial abelian normal subgroup, its center $\{\pm I_2\}$, and every nontrivial subgroup of $\mathrm{SL}_2(\mathbf{Z}/(5))$ is solvable and therefore also contains a nontrivial abelian normal subgroup.

## 3. The Fitting and Frattini Subgroups

Recall that the upper and lower central series $\{Z_i\}$ and $\{L_i\}$ of a group $G$ both reach the end (the upper one reaching $G$ and the lower one reaching $\{e\}$) precisely when $G$ is nilpotent, in which case the number of terms in both series is the same. The *nilpotency class* of $G$ is the least $c \geq 0$ such that $Z_c = G$ (equivalently, $L_c = \{e\}$), and $G$ is nontrivial abelian precisely when it has nilpotency class 1.

Using a theorem of Fitting (Theorem 3.2 below) we will construct two new subgroup series in each finite group, one ascending and the other descending, such that they both terminate at the end precisely when the group is solvable, and the nilpotent groups will be those where the process stops in one step.

Our starting point is a nilpotent analogue of the theorem that when $H$ and $K$ are solvable normal subgroups of $G$, $HK$ is solvable.

**Lemma 3.1.** *If $G$ is nilpotent of class $c$ then each subgroup and quotient group of $G$ has class at most $c$. If $G$ is nontrivial then $G/Z_i$ has class $c - i$.*

*Proof.* The proof that nilpotency is preserved when passing to subgroups and quotient groups shows that the nilpotence class does not grow when passing to subgroups or quotient groups of nilpotent groups. When $G$ is nontrivial, the upper central series for $G/Z_i$ is $Z_i/Z_i \subset Z_{i+1}/Z_i \subset \cdots \subset Z_c/Z_i = G/Z_i$ with $Z_{c-1}/Z_i \neq G/Z_i$. This series has $c - i$ factors. $\square$

**Theorem 3.2** (Fitting, 1938). *If $G$ is a group and $H$ and $K$ are nilpotent normal subgroups of $G$ then $HK$ is nilpotent normal in $G$.*

*Proof.* That $HK$ is a normal subgroup when $H$ and $K$ are normal is standard. To prove $HK$ is nilpotent, since $H$ and $K$ are normal in $HK$ we may as well take $G = HK$. That is, we will show that if a group $G$ is generated by two nilpotent normal subgroups $H$ and $K$ then it is also nilpotent.

Let $H$ have nilpotence class $c$ and $K$ have nilpotence class $d$. We will argue that $HK$ is nilpotent by induction on the sum $c + d$. The result is obvious if $c$ or $d$ is 0, so we may take $c$ and $d$ positive. The center of $H$, $Z(H)$, is a normal subgroup of $G = HK$. The quotient group $\overline{G} := G/Z(H)$ is generated by the subgroups $\overline{H} = H/Z(H)$ and $\overline{K} = KZ(H)/Z(H) \cong K/(Z(H) \cap K)$. Both $\overline{H}$ and $\overline{K}$ are normal subgroups of $\overline{G}$ and they are nilpotent. The class of $\overline{H}$ is $c - 1$ (Lemma 3.1) and the class of $\overline{K}$ is $\leq d$. Since

<!-- page 5 -->

$c - 1 + d < c + d$, by induction $\overline{G} = G/Z(H)$ is nilpotent. By a similar argument $G/Z(K)$ is nilpotent. Then, since $Z(H)$ and $Z(K)$ are normal in $G$, $G/(Z(H) \cap Z(K))$ is nilpotent. Since $Z(H) \cap Z(K) \subset Z(G)$, $G/Z(G)$ is a quotient group of $G/(Z(H) \cap Z(K))$ and therefore $G/Z(G)$ is nilpotent. Hence $G$ is nilpotent (if $G/Z_i(G)$ is nilpotent for some $i$ then $G$ is nilpotent). $\square$

Theorem 3.2 is false if we replace nilpotency with commutativity: in $D_4$ the subgroups $H = \langle r \rangle$ and $K = \langle r^2, s \rangle$ are abelian and normal, but $HK = D_4$ is not abelian (but it is nilpotent).

Theorem 3.2 need not hold without the normality condition on both $H$ and $K$: the subgroups $H = \langle r \rangle$ and $K = \langle s \rangle$ of $D_n$ are both nilpotent and only one of them is normal in $D_n$, but $HK = D_n$ is not nilpotent when $n \geq 3$ is odd.

The *Fitting subgroup* (or nilpotent radical) of a finite group $G$ is

$$
\mathrm{F}(G) = \text{unique maximal nilpotent normal subgroup of } G.
$$

That this subgroup makes sense follows from Fitting's theorem. If $G$ is nilpotent then $\mathrm{F}(G) = G$. When $n$ is not a power of 2, $\mathrm{F}(D_n) = \langle r \rangle$. The Fitting subgroups of the symmetric groups are $\mathrm{F}(S_3) = A_3$, $\mathrm{F}(S_4) = V$, and $\mathrm{F}(S_n) = \{(1)\}$ for $n \geq 5$. When $G$ is infinite, the Fitting subgroup of $G$ is defined to be the subgroup generated by the nilpotent normal subgroups, but it is not necessarily nilpotent itself. We will not discuss the Fitting subgroup of infinite groups.

The Fitting subgroup of a finite group $G$ is a direct product of its own Sylow subgroups, since $\mathrm{F}(G)$ is nilpotent. Since $\mathrm{F}(G)$ has a rather canonical status within $G$ (the nilpotent normal subgroup containing all others), the Sylow subgroups of $\mathrm{F}(G)$ are, not surprisingly, closely related to the Sylow subgroups of $G$:

**Theorem 3.3.** *For a finite group $G$ and a prime $p$, the $p$-Sylow subgroup of $\mathrm{F}(G)$ is the intersection of the $p$-Sylow subgroups of $G$.*

*Proof.* Let $\mathrm{Syl}_p(\mathrm{F}(G)) = \{Q\}$. Since $\mathrm{F}(G) \triangleleft G$ and $Q$ is a normal Sylow subgroup of $\mathrm{F}(G)$, $Q$ is normal in $G$. Therefore $Q$ lies in every $p$-Sylow subgroup of $G$. For the reverse inclusion, the intersection of the $p$-Sylow subgroups of $G$ is a normal $p$-subgroup of $G$, hence a normal nilpotent subgroup, so it lies in $\mathrm{F}(G)$. The group $Q$ is the unique $p$-Sylow in $\mathrm{F}(G)$, so the intersection of the $p$-Sylows of $G$ lies in $Q$. $\square$

Recall a subnormal subgroup is a subgroup linked to the whole group by a tower of subgroups that are normal in each other.

**Corollary 3.4.** *For each finite group $G$, its Fitting subgroup $\mathrm{F}(G)$ contains all nilpotent subnormal subgroups of $G$.*

*Proof.* Let $H \subset G$ be a subnormal subgroup, say

$$
H = H_0 \triangleleft H_1 \triangleleft \cdots \triangleleft H_r = G.
$$

We will prove quite generally that if $K$ is a finite group and $N \triangleleft K$ then $\mathrm{F}(N) \subset \mathrm{F}(K)$. Applying this to the above series from $H$ to $G$, we obtain $\mathrm{F}(H) \subset \mathrm{F}(H_1) \subset \cdots \subset \mathrm{F}(G)$, so if $H$ is nilpotent then $H = \mathrm{F}(H)$ and therefore $H \subset \mathrm{F}(G)$.

To show $N \triangleleft K \Longrightarrow \mathrm{F}(N) \subset \mathrm{F}(K)$ it suffices to show the $p$-Sylow subgroup of $\mathrm{F}(N)$ is inside the $p$-Sylow subgroup of $\mathrm{F}(K)$ (Fitting subgroups are nilpotent). By Theorem 3.3,

<!-- page 6 -->

for each prime $p$ the $p$-Sylow subgroup of $\mathrm{F}(N)$ is

$$
\bigcap_{P \in \mathrm{Syl}_p(N)} P.
$$

Since every $p$-Sylow of $N$ has the form $N \cap Q$ for some $p$-Sylow $Q$ of $K$ (and *vice versa*),

$$
\bigcap_{P \in \mathrm{Syl}_p(N)} P = \bigcap_{Q \in \mathrm{Syl}_p(K)} (N \cap Q) = N \cap \bigcap_{Q \in \mathrm{Syl}_p(K)} Q,
$$

and this last intersection is the intersection of $N$ with the $p$-Sylow subgroup of $\mathrm{F}(K)$. $\square$

Armed with the Fitting subgroup, we can give a solvable analogue of the theorem that nontrivial normal subgroups of nilpotent groups nontrivially intersect the center.

**Theorem 3.5.** *If $G$ is a nontrivial solvable group then every nontrivial normal subgroup $N$ contains a nontrivial abelian normal subgroup of $G$. In particular, when $G$ is finite $N \cap \mathrm{F}(G) \neq \{e\}$.*

*Proof.* We have $N \cap G^{(0)} = N \neq \{e\}$ and $N \cap G^{(i)} = \{e\}$ for large $i$ (since $G^{(i)}$ is trivial for large $i$). Choose $i \geq 1$ maximal such that $N \cap G^{(i)} \neq \{e\}$. Since $N' \subset N$ and $(G^{(i)})' = G^{(i+1)}$, $(N \cap G^{(i)})' \subset N \cap G^{(i+1)} = \{e\}$, so $N \cap G^{(i)}$ is abelian. It is normal in $G$ since $N$ and $G^{(i)}$ are both normal subgroups of $G$. Abelian groups are nilpotent, so $N \cap G^{(i)} \subset N \cap \mathrm{F}(G)$. $\square$

That a nontrivial finite solvable group has a nontrivial Fitting subgroup is analogous to a nontrivial nilpotent group having a nontrivial center. Constructing "higher" centers of a group leads to the upper central series, and we can similarly construct "higher" Fitting subgroups. For a (finite) group $G$, let $F_0 = \{e\}$ and $F_1 = \mathrm{F}(G)$. We have $\mathrm{F}(G) = G$ if and only if $G$ is nilpotent. If we have defined a normal subgroup $F_i \triangleleft G$, write $\mathrm{F}(G/F_i) = F_{i+1}/F_i$. This is normal in $G/F_i$, so $F_{i+1} \triangleleft G$. Thus we get an ascending series

$$
\{e\} = F_0 \subset F_1 \subset F_2 \subset \cdots \subset G
$$

where $F_i \triangleleft G$ for all $i$. Each quotient group $F_{i+1}/F_i$ is nilpotent by the definition of a Fitting subgroup. Going down instead of up, the lower central series of a finite group $G$ will eventually stabilize: set $L_\infty(G) = L_i(G)$ for large $i$. Then $L_\infty(G)$ is trivial if and only if $G$ is nilpotent. Define $E_0 = G$, $E_1 = L_\infty(G)$, and $E_{i+1} = L_\infty(E_i)$. We get a descending series

$$
G = E_0 \supset E_1 \supset E_2 \supset \cdots \supset \{e\},
$$

where $E_i \triangleleft G$ for all $i$. Each quotient group $E_i/E_{i+1}$ is nilpotent. (Hint: $G/N$ is nilpotent if and only if $L_\infty(G) \subset N$). These series $\{F_i\}$ and $\{E_i\}$ bound series with nilpotent factors from above and below in the same spirit of the upper and lower central series bounding ascending and descending central series from above and below (Corollary 3.4 is useful here), so $\{F_i\}$ is called the *upper nilpotent series* for $G$ and $\{E_i\}$ is called the *lower nilpotent series* for $G$. (Why doesn't a construction $Z_\infty$, analogous to $L_\infty$ but applied to the upper central series, lead to a worthwhile subgroup series in place of the $F_i$'s?) Just as with central series, $F_i = G$ for large $i$ if and only if $E_i = \{e\}$ for large $i$, and then the least $i$'s in both cases are equal (exercise). The least such $i$ is called the *Fitting length* (or *nilpotent length*, not to be confused with nilpotent class) of $G$. The trivial group has Fitting length 0, and a finite group has Fitting length 1 if and only if it is nontrivial and nilpotent.

<!-- page 7 -->

**Example 3.6.** Let $G = D_n$ with $n$ not a power of 2. Write $n = 2^k m$ for odd $m \geq 3$. Then $F_1 = \langle r \rangle$ and $D_n/F_1$ has size 2 (so it's nilpotent), hence $F_2 = D_n$. The subgroup $E_1 = L_\infty(D_n)$ is $\langle r^{2^k} \rangle$, which is abelian, so $E_2 = \{1\}$. Thus $D_n$ has Fitting length 2.

**Example 3.7.** Let $G = S_n$ for $n \geq 5$. Then $\mathrm{F}(G)$ is trivial, so $F_i$ is trivial for all $i \geq 0$. Since $L_\infty(S_n) = A_n$ and $L_\infty(A_n) = A_n$, $E_i = A_n$ for $i \geq 1$. There is no Fitting length.

**Theorem 3.8.** *A finite group has a Fitting length if and only if it is solvable.*

*Proof.* Suppose $G$ is a finite solvable group. If $F_i \neq G$ then $G/F_i$ is a nontrivial finite solvable group so its Fitting subgroup $F_{i+1}/F_i$ is nontrivial. Therefore $F_{i+1} \neq F_i$, so for large $i$ we must have $F_i = G$. Similarly, if $E_i \neq \{e\}$ then $E_{i+1} \neq E_i$ (because $E_{i+1} = L_\infty(E_i) \subset L_1(E_i) = E_i'$, which is a proper subgroup of $E_i$ because $E_i$ is a nontrivial solvable group). Therefore $E_i$ is trivial for large $i$.

Now suppose $G$ has a Fitting length. The upper nilpotent series is a normal series for $G$ with nilpotent factors. Since nilpotent groups are solvable and solvability of $N$ and $H/N$ implies solvability of $H$, we get solvability of $G$ by arguing inductively that every $F_i$ is solvable. $\square$

**Remark 3.9.** A group $G$ is called *metacyclic*, *metabelian*, or *metanilpotent* if it has a normal subgroup $N$ such that $N$ and $G/N$ are both cyclic, both abelian, or both nilpotent. This means the normal series $\{e\} \triangleleft N \triangleleft G$ has both factors cyclic or abelian or nilpotent, so these properties are preserved by passage to subgroups and quotient groups (but not direct products, since the direct product need not have such a series with 2 factors). All such groups are solvable since $N$ and $G/N$ are solvable. Check that metabelian is the same as having solvable length $\leq 2$ while (when $G$ is finite) metanilpotent is the same as having Fitting length $\leq 2$.

In addition to the Fitting subgroup, there is another important nilpotent subgroup of each finite group: its Frattini subgroup.

**Definition 3.10.** The *Frattini subgroup* of a finite group is the intersection of its maximal subgroups:

$$
\Phi(G) = \bigcap_{\text{max. } M} M.
$$

We set the trivial group to have trivial Frattini subgroup.

The intersection defining $\Phi(G)$ is preserved by conjugations, so $\Phi(G) \triangleleft G$. For instance, $\Phi(D_4) = \{1, r^2\}$ and $\Phi(S_n)$ is trivial for $n \geq 3$. (In particular, since $D_4$ is the 2-Sylow subgroup of $S_4$, we see that if $H \subset G$ then $\Phi(H)$ can be larger than $\Phi(G)$.) When $G$ is nilpotent, $G' \subset \Phi(G)$ by Theorem 2.2(2), so the quotient $G/\Phi(G)$ is abelian. In particular, $G/\Phi(G)$ is abelian when $G$ is a finite $p$-group.

**Theorem 3.11.** *Let $G$ be a finite $p$-group. The number of maximal subgroups of $G$ is $(p^n - 1)/(p - 1)$, where $G/\Phi(G)$ has $p^n - 1$ elements of order $p$.*

*Proof.* Maximal subgroups of $G$ each contain $\Phi(G)$, so $G$ and $G/\Phi(G)$ have the same number of maximal subgroups. Thus we focus on counting maximal subgroups of $G/\Phi(G)$.

Each maximal subgroup $M$ of $G$ is normal with index $p$ by Theorem 2.2. Since $G/M$ has order $p$, $g^p \in M$ for all $g \in G$, so $g^p \in \Phi(G)$ for all $g \in G$. Thus in $G/\Phi(G)$ all nontrivial elements have order $p$, so this finite abelian group must be a direct sum of cyclic groups of order $p$: $G/\Phi(G) \cong (\mathbf{Z}/(p))^n$ for some $n$. We will count maximal subgroups of $(\mathbf{Z}/(p))^n$.

<!-- page 8 -->

The maximal subgroups of $(\mathbf{Z}/(p))^n$ are the subgroups with index $p$. In every finite *abelian* group, the number of subgroups of order $d$ and index $d$ are the same for each $d$. Thus the number of subgroups of $(\mathbf{Z}/(p))^n$ with index $p$ equals the number of subgroups with order $p$. Let $s$ be the number of subgroups with order $p$. Each nonzero element generates such a subgroup and two such subgroups have trivial intersection, so $p^n - 1 = s(p - 1)$. Thus $s = (p^n - 1)/(p - 1)$, so $G$ has $(p^n - 1)/(p - 1)$ maximal subgroups, where $p^n - 1$ is the number of elements of $G/\Phi(G) \cong (\mathbf{Z}/(p))^n$ with order $p$. $\square$

Much more can be said (and used) about $G/\Phi(G)$ when $G$ is a finite $p$-group: look up the "Burnside basis theorem" in a group theory book.

**Theorem 3.12** (Frattini, 1885). *For every finite group $G$, $\Phi(G)$ is nilpotent.*

*Proof.* We will show all the Sylow subgroups of $\Phi(G)$ are normal subgroups of $\Phi(G)$, so $\Phi(G)$ is nilpotent[^2]. Let $P$ be a Sylow subgroup of $\Phi(G)$. Then $G = \Phi(G)\mathrm{N}_G(P)$ by the Frattini argument[^3]. If $P$ is not normal in $G$ then $\mathrm{N}_G(P) \neq G$. Let $M$ be a maximal subgroup of $G$ containing $\mathrm{N}_G(P)$, so $\Phi(G) \subset M$. Therefore $G = \Phi(G)\mathrm{N}_G(P) \subset M$, a contradiction, so $P \triangleleft G$, which implies $P \triangleleft \Phi(G)$. $\square$

Since, for each finite group $G$, $\Phi(G)$ is a nilpotent normal subgroup of $G$,

$$
\Phi(G) \subset \mathrm{F}(G).
$$

We can now give two more characterizations of nilpotency for finite groups (extending the list from Theorem 1.1 and Corollary 2.3).

**Theorem 3.13.** *For a nontrivial finite group $G$ the following are equivalent to nilpotency:*

1. *$G' \subset \Phi(G)$, i.e., $G' \subset M$ for every maximal subgroup $M$,*
2. *$G/\Phi(G)$ is nilpotent.*

*Proof.* By Theorem 2.2, every nilpotent group satisfies (2). Now assume (2). Then every maximal subgroup of $G$ is normal since all subgroups of $G$ that contain $G'$ are normal. Therefore $G$ is nilpotent by (1).

Nilpotence of $G$ implies (3) since every quotient of a nilpotent group is nilpotent. Now assume (3). Pick a Sylow subgroup $P$ of $G$. To show $P \triangleleft G$, first note that $(P\Phi(G))/\Phi(G)$ is a Sylow subgroup of $G/\Phi(G)$, so $(P\Phi(G))/\Phi(G) \triangleleft G/\Phi(G)$ by (3), which implies $P\Phi(G) \triangleleft G$. Set $N = P\Phi(G)$, so $N$ is a normal subgroup of $G$. Then $P$ is a Sylow subgroup of $N$ (why?), so by the Frattini argument, $G = N\mathrm{N}_G(P) = \mathrm{N}_G(P)N = \mathrm{N}_G(P)P\Phi(G) = \mathrm{N}_G(P)\Phi(G)$. If $\mathrm{N}_G(P) \neq G$ then $\mathrm{N}_G(P) \subset M$ for some maximal subgroup $M$ of $G$. Since $\Phi(G) \subset M$ too, $G = \mathrm{N}_G(P)\Phi(G) \subset M$, a contradiction. Thus $\mathrm{N}_G(P) = G$, so $P \triangleleft G$. $\square$

## 4. Supersolvable Groups

Having examined nilpotent and solvable groups, we turn now to a third class of groups: supersolvable groups. Among *finite* groups, these three classes of groups fit into the following chain of inclusions:

$$
\text{nilpotent} \subset \text{supersolvable} \subset \text{solvable},
$$

and examples show all inclusions are strict. Following the pattern set before with nilpotent and solvable groups, we'll see how supersolvable groups behave under group constructions

<!-- page 9 -->

(subgroup, quotient group, direct product) and the nature of their minimal normal subgroups and maximal subgroups.

Nilpotent and solvable groups can both be described in terms of particular normal series (the upper and lower central series or the derived series) whose constituent subgroups happen to be normal in the whole group. This is a stronger property than normal series require (each subgroup in the series only needs to be normal in the next subgroup of the series), and it is convenient to give series with this stronger property a name.

**Definition 4.1.** A normal series

$$
\{e\} = G_0 \triangleleft G_1 \triangleleft G_2 \triangleleft \cdots \triangleleft G_r = G
$$

or

$$
G = G_0 \triangleright G_1 \triangleright G_2 \triangleright \cdots \triangleright G_r = \{e\},
$$

where $G_i \triangleleft G$ for all $i$ is called an *invariant series*.

The word "invariant" comes from its obsolete meaning as "normal," in the context of subgroups. That is, normal subgroups used to be called invariant subgroups (invariant under conjugation, evidently).

**Example 4.2.** For every group $G$, $\{e\} \triangleleft G$ is an invariant series for $G$.

**Example 4.3.** The normal series

$$
\{(1)\} \triangleleft V \triangleleft A_4 \triangleleft S_4
$$

for $S_4$ is invariant, where

$$
V = \{(1), (12)(34), (13)(24), (14)(23)\} = \langle (12)(34), (13)(24) \rangle \cong (\mathbf{Z}/(2))^2.
$$

is the subgroup of permutations of type $(2, 2)$). However, the refinement

$$
\{(1)\} \triangleleft U \triangleleft V \triangleleft A_4 \triangleleft S_4,
$$

where $U$ is a subgroup of $V$ with size 2, is not invariant: the subgroup $U$ is not normal in $S_4$.

**Remark 4.4.** Recall that a subgroup $H$ at the bottom of a tower of successive normal subgroups $H = H_0 \triangleleft H_1 \triangleleft H_2 \triangleleft \cdots \triangleleft G$ is called a subnormal subgroup of $G$. So a normal series contains subnormal subgroups while an invariant series contains normal subgroups. Doesn't that sound like conflicting terminology? Naturally enough, some people prefer to label a normal series as a subnormal series and an invariant series as a normal series, so that subnormal series contain subnormal subgroups while normal series contain normal subgroups. It appears that most of the widely used algebra textbooks use the label "normal series" in accordance with our usage, so we will stick to that.

Here's the main object of interest for us.

**Definition 4.5.** A group $G$ is called *supersolvable* if it has an invariant cyclic series: each subgroup in the series is normal in $G$ and every factor is a cyclic group.

This term in British English is supersoluble.

Where does the label "supersolvable" come from? Since an invariant cyclic series is a normal cyclic series, every supersolvable group is solvable, and they're such a special type of solvable group that they are singled out by the extra decoration *super*solvable.

<!-- page 10 -->

**Example 4.6.** The dihedral group $D_n$ for $n \geq 3$ is supersolvable since it has the invariant cyclic series $\{1\} \subset \langle r \rangle \subset D_n$. (In particular, $S_3 \cong D_3$ is supersolvable.) Easily $D_1$ and $D_2$ are also supersolvable.

**Example 4.7.** The infinite dihedral group $\mathrm{Aff}(\mathbf{Z})$ is supersolvable: it has the invariant cyclic series $\{I_2\} \subset \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\} \subset \mathrm{Aff}(\mathbf{Z})$, with factors $\mathbf{Z}$ and $\{\pm 1\}$.

**Example 4.8.** The groups $A_4$ and $S_4$ are solvable, but *not* supersolvable. The only normal subgroups of $A_4$ are $\{(1)\}$, $V \cong (\mathbf{Z}/(2))^2$, and $A_4$, and $V$ is not cyclic, so $A_4$ has no invariant cyclic series. (The normal cyclic series $\{(1)\} \triangleleft U \triangleleft V \triangleleft A_4$ is not an invariant series for $A_4$ since $U$ is not normal in $A_4$.) The only normal subgroups of $S_4$ are $\{(1)\}$, $V$, $A_4$, and $S_4$. These can't be fit into an invariant cyclic series for the same reason $A_4$ has none. Obviously it is pretty tedious to show a group is not supersolvable in this way. Later we will see better ways to check finite groups are not supersolvable. In any case, $A_4$ and $S_4$ are basic examples of solvable groups that are not supersolvable. Remember them.

**Remark 4.9.** There is an ascending series of subgroups in each finite group whose behavior reflects supersolvability in the same way that the upper and lower central series and derived series are connected with nilpotency and solvability. See [1].

**Remark 4.10.** In Galois theory, it is believed (but not proved) that every finite group arises as a Galois group over $\mathbf{Q}$. This is not true when the base field is the $p$-adic numbers $\mathbf{Q}_p$ since the Galois group of a finite Galois extension of $\mathbf{Q}_p$ is solvable. It might not be supersolvable. For instance, $S_4$ and $A_4$ are solvable but not supersolvable and they occur as Galois groups over $\mathbf{Q}_2$: $x^4 + 2x + 2$ has Galois group $S_4$ over $\mathbf{Q}_2$ and $x^4 + 2x^3 + 2x^2 + 2$ has Galois group $A_4$ over $\mathbf{Q}_2$.

**Theorem 4.11.** *Supersolvable groups are closed under passage to subgroups, quotients, and direct products.*

*Proof.* The basic behavior of normal series of a group under passage to subgroups, quotient groups, and direct products carry over to invariant series with no changes whatsoever in the proofs. In particular, if a group admits an invariant series with cyclic factors then so does every subgroup and quotient group and direct product of such groups. The proofs are absolutely the same. It's just a matter of checking that all groups that are constructed in the proofs are normal in the whole group when the subgroups in the original series are normal in the whole group. $\square$

**Example 4.12.** The group $\mathrm{SL}_2(\mathbf{Z}/(3))$ is solvable but not supersolvable. It is solvable because the subgroup $\{\pm I_2\}$ and quotient $\mathrm{SL}_2(\mathbf{Z}/(3))/\{\pm I_2\} \cong A_4$ are solvable. This also shows (by Theorem 4.11) that $\mathrm{SL}_2(\mathbf{Z}/(3))$ is not supersolvable, since it has a quotient isomorphic to the nonsupersolvable group $A_4$.

**Example 4.13.** The groups $\mathrm{Aff}(\mathbf{Z}/(n))$ are supersolvable for all $n \geq 2$. To prove this, it suffices (by Theorem 4.11) to check $\mathrm{Aff}(\mathbf{Z}/(p^k))$ is supersolvable for all prime powers $p^k$, since $\mathrm{Aff}(\mathbf{Z}/(n))$ is a direct product of such groups by the Chinese remainder theorem. The invariant series

$$
\left\{\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\right\} \triangleleft \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix}\right\} \triangleleft \left\{\begin{pmatrix} * & * \\ 0 & 1 \end{pmatrix}\right\}
$$

for $\mathrm{Aff}(\mathbf{Z}/(p^k))$ has factors $\mathbf{Z}/(p^k)$ and $(\mathbf{Z}/(p^k))^\times$. The first factor is obviously cyclic for all $p$, and $(\mathbf{Z}/(p^k))^\times$ is cyclic for all odd primes $p$. Therefore $\mathrm{Aff}(\mathbf{Z}/(p^k))$ is supersolvable

<!-- page 11 -->

when $p \neq 2$. It remains to handle the case $p = 2$, and we will return to this point after Lemma 4.16.

**Corollary 4.14.** *Let $G$ be a group with normal subgroups $H$ and $K$. If $G/H$ and $G/K$ are supersolvable then $G/(H \cap K)$ is supersolvable.*

*Proof.* This follows from Theorem 4.11 by the same proof as for nilpotency and solvability. $\square$

When $G$ has normal subgroups $H$ and $K$ that are nilpotent or solvable, we saw in part I that $HK$ is nilpotent or solvable, respectively. The proof was easy in the solvable case, harder in the nilpotent case and it is impossible in the supersolvable case. That is, the supersolvable analogue is false: $HK$ need not be supersolvable when $H$ and $K$ are. We will see a counterexample after we have learned some more properties of supersolvable groups.

It is false in general that if $N$ and $G/N$ are supersolvable then $G$ is supersolvable. For instance, $V$ and $A_4/V$ are supersolvable, but $A_4$ is not supersolvable. Here is a weak substitute, however.

**Theorem 4.15.** *Let $G$ be a group and $N \triangleleft G$. If $N$ is cyclic and $G/N$ is supersolvable then $G$ is supersolvable.*

*Proof.* Lift an invariant cyclic series for $G/N$ up to $G$, so it ends in $N$, and then tack the identity subgroup on. $\square$

We already noted that every supersolvable group is solvable. How do the supersolvable groups compare to the nilpotent groups?

**Lemma 4.16.** *Every finite $p$-group is supersolvable.*

*Proof.* Let $|G|$ be a group of size $p^n$. When $n = 1$, $G$ is cyclic and therefore supersolvable. We now suppose $n > 1$ and that the theorem is true for $p$-groups of size less than $p^n$. Since $G$ is nilpotent, it has a normal subgroup $N \triangleleft G$ of size $p$. Then $G/N$ has size $p^{n-1}$, so $G/N$ is supersolvable by induction. Since $N$ is cyclic, $G$ is supersolvable by Theorem 4.15. $\square$

Now we can complete the remaining detail in Example 4.13. We had to show $\mathrm{Aff}(\mathbf{Z}/(2^k))$ is supersolvable. It's a finite 2-group, so we're done.

**Theorem 4.17.** *Every finite nilpotent group is supersolvable.*

*Proof.* Supersolvability is true for finite $p$-groups and thus also for direct products of finite $p$-groups. These are precisely the finite nilpotent groups. $\square$

Infinite nilpotent groups need not be supersolvable. The reason is that, since cyclic groups have a single generator, a supersolvable group must be finitely generated, so in particular countable. Therefore uncountable abelian groups are nilpotent but not supersolvable. It turns out that a nilpotent group is supersolvable if and only if it is finitely generated (proof omitted).

In an infinite nilpotent group the elements with finite order form a subgroup, but this need not hold in supersolvable groups. For example, $\mathrm{Aff}(\mathbf{Z})$ is supersolvable (Example 4.7) and the elements of finite order in $\mathrm{Aff}(\mathbf{Z})$ are $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and the matrices $\begin{pmatrix} -1 & b \\ 0 & 1 \end{pmatrix}$, that have order 2. Since $\begin{pmatrix} -1 & b \\ 0 & 1 \end{pmatrix}\begin{pmatrix} -1 & c \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & b-c \\ 0 & 1 \end{pmatrix}$, the elements of finite order in $\mathrm{Aff}(\mathbf{Z})$ are not a subgroup.

All three of our basic classes of groups -- nilpotent, solvable, and supersolvable -- can be characterized in terms of invariant series. A group is nilpotent if and only if it has an

<!-- page 12 -->

invariant *central* series (the upper and lower central series will work), a group is solvable if and only if it has an invariant *abelian* series (the derived series will work), and by definition a group is supersolvable if and only if it has an invariant *cyclic* series. While there is no difference between a finite group having a normal abelian series or a normal cyclic series (the former can be refined to the latter), there *is* a difference between a group having an invariant abelian series or an invariant cyclic series ($A_4$ has the former, namely $\{(1)\} \triangleleft V \triangleleft A_4$, but not the latter) and this motivates the introduction of supersolvability as a special kind of solvability.

A nontrivial finite solvable group has a normal series whose factors are cyclic of prime order. Here is the supersolvable analogue.

**Theorem 4.18.** *A nontrivial supersolvable group has an invariant series whose factors are infinite cyclic or cyclic of prime order. In particular, a nontrivial finite supersolvable group has an invariant series whose factors have prime order.*

*Proof.* We show how to refine each invariant cyclic series so that its finite cyclic factors have prime order. The catch is that unlike in a normal series we have to make sure our refinements produce new subgroups that are normal in the whole group. Let

$$
\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G_r = G \tag{4.1}
$$

be an invariant cyclic series with $G_i \triangleleft G$ and $G_{i+1}/G_i$ cyclic for all $i$. We may cut out all repetitions from (4.1), so each factor $G_{i+1}/G_i$ is nontrivial. If some factor $G_{i+1}/G_i$ is finite cyclic and not of prime order, let $p$ be a prime dividing $|G_{i+1}/G_i|$. Then $G_{i+1}/G_i$ has a subgroup of order $p$, say $H/G_i$. Since $G_i$ and $G_{i+1}$ are both normal in $G$, for all $g \in G$ conjugation by $g$ is well-defined on $G_{i+1}/G_i$ and sends $H/G_i$ to the subgroup $gHg^{-1}/G_i$ in $G_{i+1}/G_i$, also of size $p$. Since $G_{i+1}/G_i$ is cyclic it has only one subgroup of each possible size, so $H/G_i = gHg^{-1}/G_i$. Thus $H = gHg^{-1}$, so $H \triangleleft G$. Now we insert $H$ into the series (4.1) and we have an invariant series whose factors are still cyclic: $H/G_i$ is cyclic by construction while $G_{i+1}/H$ is a quotient of $G_{i+1}/G_i$ so it too is cyclic. The factor $H/G_i$ has prime size. Now repeat this construction until all finite cyclic factors have prime size. (The process will terminate since a finite factor $G_{i+1}/G_i$ can't be nontrivially refined indefinitely.) $\square$

In part I, we briefly discussed Lagrangian groups: those finite groups satisfying the converse of Lagrange's theorem. In particular, we saw every Lagrangian group is solvable. How is supersolvability related to the Lagrangian property?

**Corollary 4.19.** *A finite supersolvable group is Lagrangian.*

*Proof.* Our proof is adapted from [2]. Let $G$ be the group. We may of course take $G$ to be nontrivial and not have prime size.

By Theorem 4.18 there is a series

$$
\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G_r = G
$$

where each $G_i$ is normal in $G$ and the index $[G_{i+1} : G_i]$ is prime, and $r \geq 2$. Let $p = [G_1 : G_0]$ and $q = [G_2 : G_1]$. Given $d \mid |G|$ we want to construct a subgroup of $G$ with size $d$. We may assume by induction that the theorem is true for all supersolvable groups with size less than $|G|$.

If $p \mid d$ then $G/G_1$ has size $|G|/p$, so by induction it has a subgroup of size $d/p$. Pulling this back to $G$ gives a subgroup with size $(d/p)p = d$.

<!-- page 13 -->

If $(p, d) = 1$ then $pd \mid |G|$, so $d \mid |G|/p$. By induction there is a subgroup of $G/G_1$ with size $d$, whose pullback to $G$ is a subgroup $H$ of size $pd$. If $pd < |G|$ then $|H| < |G|$, so by induction $H$ (and thus $G$) has a subgroup of size $d$.

Suppose $(p, d) = 1$ and $pd = |G|$. Then $q \mid d$. (Remember $q = [G_2 : G_1]$.) Let $Q$ be a $q$-Sylow subgroup of $G_2$ (so $|Q|$ is $q$ or $q^2$, depending on whether or not $p = q$). Since $G_2 \triangleleft G$, by the Frattini argument, $G = G_2 \mathrm{N}_G(Q)$. Computing the size of both sides,

$$
pd = \frac{|G_2||\mathrm{N}_G(Q)|}{|G_2 \cap \mathrm{N}_G(Q)|} = \frac{pq|\mathrm{N}_G(Q)|}{|G_2 \cap \mathrm{N}_G(Q)|}.
$$

Therefore

$$
|\mathrm{N}_G(Q)| = \frac{d|G_2 \cap \mathrm{N}_G(Q)|}{q}. \tag{4.2}
$$

Since $Q \subset G_2 \cap \mathrm{N}_G(Q) \subset G_2$ and $[G_2 : Q]$ is 1 or $p$, $G_2 \cap \mathrm{N}_G(Q)$ is either $Q$ or $G_2$, so $|G_2 \cap \mathrm{N}_G(Q)|$ is either $q$ or $pq$. If the intersection has size $q$ then (4.2) says $\mathrm{N}_G(Q)$ has size $d$ and we're done. If the intersection has size $pq$ then $|\mathrm{N}_G(Q)| = pd = |G|$, so $\mathrm{N}_G(Q) = G$. Therefore $Q \triangleleft G$. The group $G/Q$ has size $pd/q = p(d/q)$. By induction, $G/Q$ has a subgroup of size $d/q$, whose pullback to $G$ has size $(d/q)q = d$. $\square$

So, among finite groups, we have the inclusions

$$
\text{cyclic} \subset \text{abelian} \subset \text{nilpotent} \subset \text{supersolvable} \subset \text{Lagrangian} \subset \text{solvable}.
$$

All inclusions are strict, *e.g.*, $S_4$ is Lagrangian but not supersolvable and $A_4$ is solvable but not Lagrangian.

If a finite group is supersolvable then all of its quotients are Lagrangian (since the quotients are all supersolvable, so Corollary 4.19 applies to them), but the converse is false: if all quotients are Lagrangian the group need not be supersolvable, $S_4$ being an example. However, for groups of odd order the converse is true: a group of odd order whose quotients are all Lagrangian is supersolvable [4]. It is conjectured [10] that a finite group $G$ whose quotients are all Lagrangian is supersolvable if and only if it has no subquotient (that is, no group $H/N$ where $N \triangleleft H \subset G$) isomorphic to $S_4$.

Theorem 4.18 is the technical result needed to prove the first two parts of the following theorem.

**Theorem 4.20.** *A nontrivial supersolvable group $G$ has the following properties:*

1. *every minimal normal subgroup of $G$ has prime order,*
2. *every maximal subgroup of $G$ has prime index,*
3. *$G'$ is nilpotent,*
4. *when $G$ is nonabelian there is an abelian $N \triangleleft G$ that properly contains the center of $G$.*

*Proof.* (1): Let $N$ be a minimal normal subgroup of $G$. By Theorem 4.18, $G$ has an invariant cyclic series whose factors are infinite cyclic or of prime order. Denote it as in (4.1). Since $G_i \triangleleft G$ we have $N \cap G_i \triangleleft G$, so by minimality $N \cap G_i$ is trivial or $N$. Since $N \cap G_0$ is trivial and $N \cap G_r$ is $N$, there is some maximal $i < r$ such that $N \cap G_i$ is trivial. Then $N \cap G_{i+1}$ is $N$, so $N \subset G_{i+1}$. The composite map $N \hookrightarrow G_{i+1} \to G_{i+1}/G_i$ has kernel $N \cap G_i$, which is trivial, so $N$ embeds into $G_{i+1}/G_i$. If $G_{i+1}/G_i \cong \mathbf{Z}/(p)$ then $N \cong \mathbf{Z}/(p)$. If $G_{i+1}/G_i \cong \mathbf{Z}$ then $N \cong \mathbf{Z}$. But we can't have $N \cong \mathbf{Z}$, because then $N$ has a unique subgroup of every index (or just index 2, to fix ideas) and uniqueness means such subgroups are preserved by

<!-- page 14 -->

conjugations from $G$, violating the minimal normality of $N$. So only $N \cong \mathbf{Z}/(p)$ for some prime $p$ is possible.

(2): Let $M$ be a maximal subgroup. First suppose $M \triangleleft G$. Then $G/M$ is supersolvable and contains no nontrivial proper subgroups. By Theorem 4.18, $G/M$ has an invariant series whose factors are isomorphic to $\mathbf{Z}$ or $\mathbf{Z}/(p)$ for primes $p$. In particular, the first nontrivial term in such a series is a nontrivial subgroup of $G/M$ and thus must be $G/M$. Therefore $G/M$ is isomorphic to $\mathbf{Z}$ or $\mathbf{Z}/(p)$. Since $G/M$ has no nontrivial proper subgroups, $G/M \cong \mathbf{Z}/(p)$, so $[G : M]$ is prime.

Now suppose $M$ is not a normal subgroup of $G$. Let $H = \cap_g gMg^{-1}$, which is the largest normal subgroup of $G$ lying in $M$. Then $\overline{M} := M/H$ is a maximal subgroup of $\overline{G} := G/H$ and $[G : M] = [\overline{G} : \overline{M}]$ (perhaps both indices are infinite *a priori*), so we can replace $G$ and $M$ with $\overline{G}$ and $\overline{M}$. Therefore we may assume the only normal subgroup of $G$ inside of $M$ is the identity.

Using Theorem 4.18, $G$ has a normal subgroup $N$ that is isomorphic to $\mathbf{Z}$ or some $\mathbf{Z}/(p)$. Since $N$ is cyclic, every subgroup of $N$ is normal in $G$. For instance, $M \cap N$ is normal in $G$. Since $M \cap N$ is also a subgroup of $M$, $M \cap N$ is trivial by the previous paragraph.

The group $MN$ is between $M$ and $G$ so either $MN = M$ or $MN = G$ by maximality of $M$. If $MN = M$ then $N \subset M$, so $N = M \cap N$ is trivial, which is false. Thus $MN = G$ and $M \cap N$ is trivial. If $N \cong \mathbf{Z}/(p)$ then it's easy to see that $[G : M] = [MN : M] = p$, so $M$ has prime index. If $N \cong \mathbf{Z}$ then we will get a contradiction. Let $H$ be a proper nontrivial subgroup of $N$, so $H \triangleleft G$. Then $M \subset MH \subset MN = G$. Either $MH = M$ or $MH = MN$. If $MH = M$ then $H \subset M$, so $H \subset M \cap N$, which means $H$ is trivial. That's not true, so $MH = MN$. But then each $x \in N$ can be written as $x = mh$ with $m \in M$ and $h \in H$, so $m = xh^{-1} \in N$. Thus $m \in M \cap N$, which is trivial, so $x = h \in H$. Hence $N = H$, a contradiction.

(3): Let

$$
\{e\} = G_0 \subset G_1 \subset \cdots \subset G_r = G.
$$

be an invariant cyclic series. Set $H_i = G' \cap G_i$, so we obtain an invariant cyclic series for $G'$:

$$
\{e\} = H_0 \subset H_1 \subset \cdots \subset H_r = G'. \tag{4.3}
$$

Since $G_i \triangleleft G$ and $G' \triangleleft G$, we have $H_i \triangleleft G$ (not just $H_i \triangleleft G'$). We will show $H_{i+1}/H_i \subset Z(G'/H_i)$ for all $i$, so (4.3) is a central series and that will prove $G'$ is nilpotent.

Let $G$ act on $H_{i+1}/H_i$ by conjugation. (It can act this way since $H_i$ and $H_{i+1}$ are normal in $G$.) This is a homomorphism $f: G \to \mathrm{Aut}(H_{i+1}/H_i)$. Since $H_{i+1}/H_i$ is cyclic, its automorphism group is abelian, so $G' \subset \ker f$. Thus $G'$ acts trivially by conjugation on $H_{i+1}/H_i$, so $H_{i+1}/H_i \subset Z(G'/H_i)$.

(4): Let $Z$ be the center of $G$, so $G/Z$ is a nontrivial supersolvable group. Write the first non-identity term in an invariant cyclic series for $G/Z$ as $H/Z$. Then $H/Z$ is cyclic, so $H$ is abelian and it properly contains $Z$. Since $H/Z \triangleleft G/Z$, also $H \triangleleft G$. $\square$

The last part of Theorem 4.20 has an important consequence in the representation theory of supersolvable (so in particular, nilpotent) groups. See [8, Thm. 16, Sect. 8.5].

We now get a conceptually simpler proof of Corollary 4.19: since subgroups of supersolvable groups are supersolvable, it suffices to show for each prime dividing the size of a finite supersolvable group that there is a subgroup with that prime index. Since a supersolvable group is solvable, for each prime $p$ dividing the size of the group there is a maximal subgroup with $p$-power index (this property of finite solvable groups depends on the Schur--Zassenhaus

<!-- page 15 -->

theorem). This $p$-power is $p$ itself because maximal subgroups in a supersolvable group have prime index. This proof of Corollary 4.19 lies a little deeper than the previous proof since it relies on the Schur--Zassenhaus theorem.

It's worth comparing Theorem 4.20 to what we know about minimal normal subgroups and maximal subgroups of nilpotent and solvable groups. This is collected in Table 1.

| Group | Minimal Normal | Maximal |
|-------|---------------|---------|
| Nilpotent | Prime Order | Normal, Prime Index |
| Supersolvable | Prime Order | Prime Index |
| Finite Solvable | $(\mathbf{Z}/(p))^k$ | Prime-Power Index |

Table 1.

For nontrivial finite groups, nilpotency is actually equivalent to maximal subgroups being normal. A characterization of supersolvability in terms of maximal subgroups will be given in Theorem 4.23(1).

Theorem 4.20 does not guarantee an *infinite* supersolvable group has either minimal normal subgroups or maximal subgroups. Some supersolvable groups have no minimal normal subgroups: consider $\mathbf{Z}$. What about maximal subgroups?

**Theorem 4.21.** *Every nontrivial supersolvable group has a maximal subgroup.*

*Proof.* We induct on the number of factors in an invariant cyclic series for the group. Groups having an invariant cyclic series with 1 factor are cyclic, and nontrivial cyclic groups have maximal subgroups (either because they are finite or because $\mathbf{Z}$ has maximal subgroups). Now assume

$$
\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G_r = G
$$

is an invariant cyclic series for a group $G$ and $r \geq 2$. Since $G_1 \triangleleft G$ we can drop the identity term and reduce modulo $G_1$:

$$
\{\bar{e}\} = G_1/G_1 \subset G_2/G_1 \subset \cdots \subset G_r/G_1 = G/G_1.
$$

This is an invariant cyclic series with $r - 1$ factors, so by induction $G/G_1$ has a maximal subgroup. Lift it up to $G$ to get a maximal subgroup of $G$. $\square$

For comparison, (infinite) nilpotent and solvable groups need not have maximal subgroups: try $\mathbf{Q}$.

**Example 4.22.** If a group $G$ has supersolvable normal subgroups $H$ and $K$, $HK$ need not be supersolvable. Here is a family of examples.

Let $\mathbf{F} = \mathbf{Z}/(p)$ for a prime $p \equiv 1 \bmod 4$ and $a^2 = -1$ in $\mathbf{F}$. In $\mathrm{GL}_2(\mathbf{F})$, set $x = \begin{pmatrix} a & 0 \\ 0 & 1/a \end{pmatrix}$ and $y = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Then $x^2 = y^2 = -I_2$ and $xy = -yx$, so $\langle x, y \rangle \cong Q_8$. Let $\mathrm{GL}_2(\mathbf{F})$ act on $\mathbf{F}^2$ in the usual way and set $G = \mathbf{F}^2 \rtimes \langle x, y \rangle$ using this action.

Set $H = \mathbf{F}^2 \rtimes \langle x \rangle$ and $K = \mathbf{F}^2 \rtimes \langle y \rangle$. Then $G = HK$, and $H$ and $K$ have index 2 in $G$, so they are normal in $G$. Since $\mathbf{F}^2$ is a subgroup of $H$ and $K$, and $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ is an eigenvector of $x$ and $\begin{pmatrix} a \\ 1 \end{pmatrix}$ is an eigenvector of $y$, $\mathbf{F}\begin{pmatrix} 1 \\ 0 \end{pmatrix} \triangleleft H$ and $\mathbf{F}\begin{pmatrix} a \\ 1 \end{pmatrix} \triangleleft K$. The invariant cyclic series

$$
\{e\} \subset \mathbf{F}\begin{pmatrix} 1 \\ 0 \end{pmatrix} \subset \mathbf{F}^2 \subset \mathbf{F}^2 \rtimes \langle x^2 \rangle \subset H
$$

<!-- page 16 -->

and

$$
\{e\} \subset \mathbf{F}\begin{pmatrix} a \\ 1 \end{pmatrix} \subset \mathbf{F}^2 \subset \mathbf{F}^2 \rtimes \langle y^2 \rangle \subset K
$$

show $H$ and $K$ are both supersolvable groups. (Neither $H$ nor $K$ is nilpotent, since they each have more than one 2-Sylow subgroup.)

Now we show $G = HK$ is not supersolvable. It has the normal subgroup $\mathbf{F}^2 = (\mathbf{Z}/(p))^2$, whose size is $p^2$. Minimal normal subgroups in a supersolvable group have prime size, so $G$ must have a normal subgroup of size $p$ inside of $\mathbf{F}^2$, which amounts to saying there is a common eigenvector of $x$ and $y$ in $\mathbf{F}^2$. However there is no common eigenvector, so $G$ is not supersolvable.

For the next theorem, recall that the Frattini subgroup $\Phi(G)$ is the intersection of the maximal subgroups of $G$.

**Theorem 4.23.** *The following properties of a nontrivial finite group $G$ are equivalent to supersolvability:*

1. *all maximal subgroups have prime index,*
2. *all subgroup series of maximal length in $G$ have the same length,*
3. *$G/\Phi(G)$ is supersolvable,*
4. *all subgroups of $G$ are Lagrangian.*

The meaning of (2) is illustrated by

$$
\{(1)\} \subset \langle (123) \rangle \subset A_4, \quad \{(1)\} \subset \langle (12)(34) \rangle \subset V \subset A_4, \tag{4.4}
$$

which are both subgroup series (just chains of subgroups, no normality assumptions) that have no refinements. They don't have the same number of terms, and $A_4$ is not supersolvable.

Note (4) is stronger than being Lagrangian: $S_4$ is Lagrangian but its subgroup $A_4$ is not.

*Proof.* (1): This is a theorem of Huppert. See [3, pp. 161--163] or [7, p. 268]. The first step is to show $G$ is solvable. Then this is sharpened to supersolvability.

(2): This is a theorem of Iwasawa. See [3, pp. 342--345].

(3): If $G$ is supersolvable then $G/\Phi(G)$ is supersolvable by Theorem 4.11. Conversely, if $G/\Phi(G)$ is supersolvable we will show the maximal subgroups of $G$ have prime index, so $G$ is supersolvable by (1). Well, if $M$ is a maximal subgroup of $G$ then $M \supset \Phi(G)$ by definition, so $M/\Phi(G)$ is maximal subgroup of $G/\Phi(G)$. Therefore $[G/\Phi(G) : M/\Phi(G)]$ is prime since $G/\Phi(G)$ is supersolvable, and $[G : M]$ is the same prime.

(4): This is a theorem of Zappa [9], building on earlier work of Ore [5]. $\square$

**Theorem 4.24.** *Let $G$ be a finite supersolvable group with size $p_1 p_2 \cdots p_m$ where $p_1 \geq p_2 \geq \cdots \geq p_m$. Then $G$ admits an invariant cyclic series*

$$
\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G_m = G,
$$

*where $[G_i : G_{i-1}] = p_i$. In particular, the elements of order prime to $p_m$ form a normal subgroup of $G$.*

*Proof.* We know $G$ has an invariant series with factors of prime order. To show such a series can be arranged so that the orders of the factors are as described in the theorem, it suffices to focus on three adjacent terms in the series, say $H \subset K \subset L$ with $p = [K : H]$ and $q = [L : K]$ primes. If $p \geq q$ then the primes are in the order we need for the theorem. Suppose $p < q$. The group $L/H$ has size $pq$, and such a group has a unique subgroup of

<!-- page 17 -->

size $q$. Call it $\widetilde{K}/H$. Then $H \subset \widetilde{K} \subset L$ with $[\widetilde{K} : H] = q$ and $[L : \widetilde{K}] = p$. Change the series by replacing $K$ with $\widetilde{K}$. It remains to show $\widetilde{K} \triangleleft G$. Conjugation by elements of $G$ gives automorphisms of $L/H$ (since $H$ and $L$ are normal in $G$), thus preserving the unique $q$-Sylow subgroup of $L/H$, so $\widetilde{K} \triangleleft G$.

With the subgroups of $G$ arranged as in the theorem, we show the elements of order prime to $p_m$ are a normal subgroup of $G$. Since all factors with size $p_m$ occur at the top of the series, there is some $G_i$ such that $[G : G_i]$ is the largest power of $p_m$ dividing $|G|$. That means $|G_i|$ is not divisible by $p_m$, so every element of $G_i$ has order prime to $p_m$. Conversely, since $G_i \triangleleft G$ and $G_i$ has $p_m$-power index in $G$, only the trivial element of $G/G_i$ has order prime to $p_m$, so an element of $G$ with order prime to $p_m$ must be in $G_i$. Thus $G_i$ is the set of elements in $G$ with order prime to $p_m$. $\square$

**Corollary 4.25.** *If $G$ is a finite supersolvable group then the elements of odd order form a normal subgroup.*

*Proof.* If $|G|$ is even then $p_m = 2$ in Theorem 4.24. $\square$

We can now give several reasons why $A_4$ is not supersolvable:

1. since $(123)(124) = (13)(24)$, the elements of $A_4$ with odd order are not a subgroup,
2. $A_4$ is not Lagrangian (no subgroup of size 6),
3. the minimal normal subgroup $V$ is not of prime order,
4. the maximal subgroup $\langle (123) \rangle$ is not of prime index,
5. $A_4$ has maximal subgroup series with different lengths in (4.4).

The next theorem is a crude supersolvable analogue of Burnside's $p^a q^b$-theorem.

**Theorem 4.26.** *If $|G| = pq^b$ where $p$ and $q$ are primes with $q \equiv 1 \bmod p$ then $G$ is supersolvable.*

*Proof.* See [6, Cor. 4.4, 4.5]. $\square$

## 5. Chief Series

As with nilpotency, supersolvability of a group can't be characterized by a composition series: $\mathbf{Z}/(12)$ is nilpotent and supersolvable while $A_4$ is neither, but both groups have composition series with two cyclic factors of order 2 and one of order 3.

When a group has an invariant series (a particular type of normal series), instead of refining it to a longer normal series until we can't proceed further we can refine it only to a longer *invariant* series as far as possible. By only refining to a new invariant series, we might have to stop before we would be done refining with normal series, and therefore we get a new notion.

**Definition 5.1.** A *chief series* of a group $G$ is an invariant series of $G$ with no trivial factors and no refinements to a longer invariant series.

**Example 5.2.** The composition series

$$
\{(1)\} \triangleleft U \triangleleft V \triangleleft A_4 \triangleleft S_4 \tag{5.1}
$$

for $S_4$ is not a chief series since $U$ is not normal in $S_4$. But the other subgroups in that series are normal in $S_4$ and they form a chief series for $S_4$: $\{(1)\} \subset V \subset A_4 \subset S_4$. Each subgroup is normal in $S_4$ and no refinement has this property.

<!-- page 18 -->

The proof that every nontrivial finite group has a composition series carries over to show it also has a chief series, while an infinite group may or may not have a chief series (*e.g.*, $\mathbf{Z}$ has no chief series).

What's the difference between a composition series and a chief series? The series

$$
\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G_r = G \tag{5.2}
$$

is a composition series when there are no repetitions, $G_i \triangleleft G_{i+1}$ for all $i$, and no refinement has these properties. The series (5.2) is a chief series when there are no repetitions, $G_i \triangleleft G$ for all $i$, and no refinement has these properties.

When (5.2) is a composition series, $G_i$ is a maximal normal subgroup of $G_{i+1}$ for all $i$. So composition series are closely related to maximal normal subgroups. The next result shows chief series are related to minimal normal subgroups of quotients of $G$.

**Theorem 5.3.** *The series (5.2) is a chief series if and only if $G_{i+1}/G_i$ is a minimal normal subgroup of $G/G_i$ for all $i$.*

*Proof.* Assuming (5.2) is a chief series for $G$, the series

$$
\{\bar{e}\} = G_i/G_i \subset G_{i+1}/G_i \subset \cdots \subset G_r/G_i = G/G_i
$$

is a chief series for $G/G_i$, since a normal subgroup of $G/G_i$ lying properly between two terms of this series pulls back to a normal subgroup of $G$ lying properly between the corresponding two terms of (5.2). Therefore no nontrivial normal subgroup of $G/G_i$ is properly contained in $G_{i+1}/G_i$, so $G_{i+1}/G_i$ is a minimal normal subgroup of $G/G_i$.

Conversely, if each $G_{i+1}/G_i$ is a minimal normal subgroup of $G/G_i$ then no normal subgroup of $G$ lies properly between $G_i$ and $G_{i+1}$, so (5.2) is a chief series for $G$. $\square$

Theorem 5.3 suggests a method of constructing a chief series of a nontrivial finite group using minimal normal subgroups from the bottom up, which runs in the opposite direction to the method of constructing a composition series from the top down using maximal normal subgroups. Let $G_0 = \{e\}$, $G_1$ be a minimal normal subgroup of $G$, $G_2/G_1$ be a minimal normal subgroup of $G/G_1$, $G_3/G_2$ be a minimal normal subgroup of $G/G_2$, and so on.

In Section 4 we saw that nilpotent, solvable, and supersolvable groups can be described in terms of the kinds of invariant series they admit (central, abelian, and cyclic). Let's now describe them in terms of the chief series they admit.

**Corollary 5.4.** *A nontrivial finite group is nilpotent if and only if it has a chief series that is a central series.*

*Proof.* A chief series that is central is a normal central series, so a group with such a series is nilpotent. Conversely, if $G$ is nilpotent and (5.2) is a chief series for $G$ then $G_{i+1}/G_i$ is a minimal normal subgroup of $G/G_i$. Since $G/G_i$ is nilpotent, $G_{i+1}/G_i$ is in the center of $G/G_i$ since minimal normal subgroups in a nilpotent group lie in the center. $\square$

**Example 5.5.** The group $A_4$ is not nilpotent and its only chief series is $\{(1)\} \subset V \subset A_4$. This is not central since $V$ is not in the center of $A_4$.

**Corollary 5.6.** *A nontrivial finite group is solvable if and only if it has a chief series whose factors are isomorphic to $(\mathbf{Z}/(p))^k$ for primes $p$ and integers $k \geq 1$.*

*Proof.* Let $G$ be a finite group. If $G$ has a chief series whose factors are as described in the theorem then the series is a normal abelian series, so the $G$ is solvable.

Conversely, if $G$ is solvable then in every chief series of $G$ all factors are isomorphic to some $(\mathbf{Z}/(p))^k$ since minimal normal subgroups of finite solvable groups look like that. $\square$

<!-- page 19 -->

**Example 5.7.** The chief series of $A_4$, $\{(1)\} \subset V \subset A_4$, has factors $(\mathbf{Z}/(2))^2$ and $\mathbf{Z}/(3)$.

**Corollary 5.8.** *A nontrivial finite group is supersolvable if and only if it has a chief series whose factors have prime order.*

*Proof.* Run through the same proof as Corollary 5.6, but use the fact that minimal normal subgroups in a supersolvable group have prime order. $\square$

Here is the Jordan--Holder theorem for chief series:

**Theorem 5.9.** *If $G$ is a nontrivial group and*

$$
\{e\} = G_0 \subset G_1 \subset G_2 \subset \cdots \subset G_r = G
$$

*and*

$$
\{e\} = \widetilde{G}_0 \subset \widetilde{G}_1 \subset \widetilde{G}_2 \subset \cdots \subset \widetilde{G}_s = G
$$

*are two chief series for $G$ then $r = s$ and for some permutation $\pi \in S_r$ we have $\widetilde{G}_i/\widetilde{G}_{i-1} \cong G_{\pi(i)}/G_{\pi(i)-1}$ for $1 \leq i \leq r$.*

*Proof.* The proof of the Jordan--Holder theorem adapts *verbatim* to this case, just taking care to notice that if you run through a proof with chief series then the groups that are constructed in the course of the proof are normal in the full group (and not just in the next term of the series). $\square$

The unrefinability of a composition series can be described in terms of its factors as abstract groups: each factor is a simple group. But Example 5.2 shows the factors in a chief series may not be simple: the bottom factor for the chief series of $S_4$ (or $A_4$) is $V \cong (\mathbf{Z}/(2))^2$. Does the unrefinability of a chief series tell us anything about the intrinsic group structure of its factors? A first answer comes from Theorem 5.3 and the following theorem.

**Theorem 5.10.** *A minimal normal subgroup of a nontrivial finite group is a direct product of isomorphic simple groups.*

*Proof.* Let $G$ be a nontrivial finite group and $N$ be a minimal normal subgroup of $G$. We want to show $N$ is a direct product of isomorphic simple groups.

Let $H$ be a minimal normal subgroup of $N$. There is no reason to expect $H$ is normal in $G$. Every $G$-conjugate of $H$ lies in $N$ since $N \triangleleft G$. Let $H_1, \ldots, H_r$ be all the different $G$-conjugates of $H$. So for all $g \in G$, $gH_ig^{-1}$ is some $H_j$. The $H_i$'s are minimal normal subgroups of $N$ (why?), so the set $H_1 H_2 \cdots H_r$ is a normal subgroup of $N$. We have $H_i H_j = H_j H_i$ by normality of the $H_i$'s in $N$, so $H_1 H_2 \cdots H_r \triangleleft G$. Because $N$ is a minimal normal subgroup of $G$, it follows that

$$
N = H_1 H_2 \cdots H_r. \tag{5.3}
$$

An example will help motivate the next step. Take $G = A_4$, which has one minimal normal subgroup, the subgroup $V$ generated by the $(2, 2)$-cycles. A minimal normal subgroup of $V$ is $H = \langle (12)(34) \rangle$, which has three $A_4$-conjugates (there are three linear subspaces in $(\mathbf{Z}/(2))^2$). Then $V = H_1 H_2 H_3$. Notice there is some redundancy, in the sense that we also have $V = H_1 H_2$.

Returning to the general case, from (5.3) we can write $N$ as the product of all $r$ subgroups conjugate to $H$. But, as the example with $A_4$ shows, we might be able to get by with fewer conjugate subgroups. Suppose $s$ is the smallest number of $H_i$'s whose product is $N$. Relabel such a choice as $H_1, \ldots, H_s$, so $N = H_1 \cdots H_s$. We will show $N \cong H_1 \times \cdots \times H_s$. This is obvious if $s = 1$, so suppose $s > 1$. To show the set product $H_1 \cdots H_s$ is isomorphic to their

<!-- page 20 -->

direct product, we just need to show $H_i \cap H_1 \cdots \widehat{H_i} \cdots H_s$ is trivial. This is an intersection of two normal subgroups of $N$ (since $H_j \triangleleft N$ for all $j$), so it is normal in $N$. Since it is a subgroup of $H_i$, which is a minimal normal subgroup of $N$, we obtain

$$
H_i \cap (H_1 \cdots \widehat{H_i} \cdots H_s) = \{1\} \text{ or } H_i.
$$

If the intersection is $H_i$ then $H_i \subset H_1 \cdots \widehat{H_i} \cdots H_s$, so $N = H_1 \cdots \widehat{H_i} \cdots H_s$. This contradicts the minimality of $s$, so $H_i \cap (H_1 \cdots \widehat{H_i} \cdots H_s)$ is trivial for all $i$.

Thus every minimal normal subgroup $N$ of $G$ is a direct product of groups $H_i$ that are each isomorphic to a minimal normal subgroup $H$ of $N$. We want to show $N$ is a direct product of isomorphic simple groups. If $N = G$ (that is, the minimal normal subgroup of $G$ is $G$) then $G$ is simple and the conclusion of the theorem is immediate. If $N \neq G$ then by induction on the size of the group the minimal normal subgroup $H$ of $N$ is a direct product of isomorphic simple groups, so $N$ itself is a direct product of isomorphic simple groups. $\square$

**Corollary 5.11.** *Every factor in a chief series of a finite group is a direct product of isomorphic simple groups.*

*Proof.* If $\{e\} = G_0 \subset G_1 \subset \cdots \subset G_r = G$ is a chief series for $G$ then $G_{i+1}/G_i$ is a minimal normal subgroup of $G/G_i$. Apply Theorem 5.10 to $G/G_i$. $\square$

The converse of this corollary is *false*: an invariant series having factors that are direct products of isomorphic simple groups need not be a chief series. For instance, $\{0\} \subset (\mathbf{Z}/(p))^k$ is such an invariant series, but it's not a chief series for $(\mathbf{Z}/(p))^k$.

Since Corollary 5.11 is not a characterization of the factors in a chief series, our search for such a characterization continues. We will have to keep the group $G$ close at hand in our description of the factors, since being a normal subgroup is not a property of a subgroup in isolation (there is no such thing as a "normal group.") The key thing to remember is that when $G_i$ and $G_{i+1}$ are terms in an invariant series, each is normal in $G$ so $G$ acts by conjugation on $G_i$ and $G_{i+1}$, and thus also on the factor $G_{i+1}/G_i$. Let's abstract this, using groups acting on groups.

Fix a group $G$. For a group $H$, we call $H$ a *$G$-group* when we have a chosen action of $G$ on $H$ by automorphisms. For instance, we could let $G$ act trivially on $H$ (always possible). Or, if $H = N_2/N_1$ where $N_1 \subset N_2$ are normal subgroups of $G$, $G$ acts on $H$ by conjugation. A $G$-group is not just a group on which $G$ acts in the sense of groups acting on sets: it must act by automorphisms of the underlying group, so that's the special feature to keep in mind.

A subgroup of a $G$-group $H$ need not be preserved by the action of $G$. Call $H$ a *$G$-simple* group if $H$ is nontrivial $G$-group and the only subgroups of $H$ preserved by the action of $G$ are the trivial subgroup and $H$ itself.

**Example 5.12.** If $G$ acts trivially on $H$ then it preserves all subgroups, so $H$ is $G$-simple if and only if $H$ has no subgroups besides itself and the identity: $H$ is a cyclic group of prime order.

**Example 5.13.** If $G$ acts on itself by conjugation, then the subgroups of $G$ preserved by $G$ are the normal subgroups of $G$, so $G$ is $G$-simple (using the conjugation action) precisely when $G$ is a simple group in the usual sense.

**Example 5.14.** Let $V \triangleleft A_4$ be the normal subgroup of size 4. The subgroups of size 2 in $V$ are conjugated into each other by $A_4$, so when $V$ is acted upon by $A_4$ using conjugation, $V$ is an $A_4$-simple group (but not a simple group in the plain sense).

<!-- page 21 -->

**Example 5.15.** If $N_1 \subset N_2$ are normal subgroups of $G$ and $H = N_2/N_1$ with $G$ acting on $H$ by conjugation, then the subgroups of $H$ preserved by $G$ are those of the form $N/N_1$ where $N$ is a normal subgroup of $G$ lying between $N_1$ and $N_2$. Therefore $H$ is $G$-simple precisely when there are no normal subgroups of $G$ strictly between $N_1$ and $N_2$.

By Example 5.15 we immediately get the next result, which resembles the description of factors in a composition series.

**Theorem 5.16.** *The series (5.2) is a chief series for $G$ precisely when each factor $G_{i+1}/G_i$ is a $G$-simple group, with $G$ acting on the factors by conjugation.*

## References

1. R. K. Agrawal, *Generalized center and hypercenter of a finite group*, Proc. Amer. Math. Soc. **58** (1976), 13--21.
2. C. D. H. Cooper, *Subgroups of a supersoluble group*, Amer. Math. Monthly **78** (1971), 1007.
3. M. Hall, "Theory of Groups," Macmillan, New York, 1959.
4. J. Humphreys, *On groups satisfying the converse of Lagrange's theorem*, Proc. Cambridge Philos. Soc. **75** (1974), 25--32.
5. O. Ore, *Contributions to the theory of groups of finite order*, Duke Math. J. **5** (1939), 431--460.
6. C. Pinnock, *Supersolubility and some characterizations of finite supersoluble groups*, https://cp1888.files.wordpress.com/2015/01/msci.pdf.
7. D. Robinson, "A Course in the Theory of Groups," 2nd ed., Springer-Verlag, New York, 1996.
8. J-P. Serre, "Linear Representations of Finite Groups," Springer--Verlag, New York, 1974.
9. G. Zappa, *Remark on a recent paper of O. Ore*, Duke Math. J. **6** (1940), 511--512.
10. L. W. Zhang, *The supersolvability of QCLT groups*, Acta Math. Sinica **1** (1985), 378--381.

[^1]: See Example 2.2 in https://kconrad.math.uconn.edu/blurbs/zorn1.pdf.
[^2]: See Theorem 5.20 in https://kconrad.math.uconn.edu/blurbs/grouptheory/subgpseries1.pdf.
[^3]: See Section 8 in https://kconrad.math.uconn.edu/blurbs/grouptheory/sylowapp.pdf.
