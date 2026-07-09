# No Subgroup of $A_4$ Has Index 2

> **Source**: https://kconrad.math.uconn.edu/blurbs/grouptheory/A4noindex2.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory

<!-- page 1 -->

Lagrange's theorem says that if $H$ is a subgroup of a finite group $G$ then the order of $H$ divides the order of $G$. It is natural to ask about a converse: if $G$ is a finite group and the integer $d \geq 1$ divides the order of $G$, must $G$ contain a subgroup of order $d$? The answer is no, and the first such example is the group $A_4$: it has order 12 and it has subgroups of orders 1, 2, 3, 4, and 12, but $A_4$ has no subgroup of order 6, or equivalently no subgroup of index 2. Here is a proof of that using left cosets.

**Theorem 1.** *There is no subgroup of index 2 in $A_4$.*

*Proof.* Suppose a subgroup $H$ of $A_4$ has index 2, so $|H| = 6$. We will show for each $g \in A_4$ that $g^2 \in H$.

If $g \in H$ then clearly $g^2 \in H$. If $g \notin H$ then $gH$ is a left coset of $H$ different from $H$ (since $g \in gH$ and $g \notin H$), so from $[G:H] = 2$ the only left cosets of $H$ are $H$ and $gH$. Which one is $g^2H$? If $g^2H = gH$ then $g^2 \in gH$, so $g^2 = gh$ for some $h \in H$, and that implies $g = h$, so $g \in H$, but that's a contradiction. Therefore $g^2H = H$, so $g^2 \in H$.

Every 3-cycle $(abc)$ in $A_4$ is a square: $(abc)$ has order 3, so $(abc) = (abc)^4 = ((abc)^2)^2$. Thus $H$ contains all 3-cycles in $A_4$. The 3-cycles are

$$(123),\ (132),\ (124),\ (142),\ (134),\ (143),\ (234),\ (243)$$

and that is too much since there are 8 of them while $|H| = 6$. Hence $H$ does not exist. $\square$

We will now give four more proofs that there is no subgroup of index 2 in $A_4$ as corollaries of four different theorems from group theory.

**Theorem 2.** *If $G$ is a finite group and $N \triangleleft G$ then every element of $G$ with order relatively prime to $[G:N]$ lies in $N$. In particular, if $N$ has index 2 then all elements of $G$ with odd order lie in $N$.*

*Proof.* Let $g$ be an element of $G$ with order $m$, which is relatively prime to $[G:N]$. Reducing the equation $g^m = e$ modulo $N$ gives $\bar{g}^m = \bar{e}$ in $G/N$. Also $\bar{g}^{[G:N]} = \bar{e}$, so the order of $\bar{g}$ in $G/N$ divides $m$ and $[G:N]$. These numbers are relatively prime, so $\bar{g} = \bar{e}$, which means $g \in N$.

A subgroup with index 2 is normal, so this theorem says a subgroup of $G$ with index 2 must contain all elements of $G$ with odd order (that's an order relatively prime to 2). $\square$

**Corollary 3.** *There is no subgroup of index 2 in $A_4$.*

*Proof.* If $A_4$ has a subgroup with index 2 then by Theorem 2, all elements of $A_4$ with odd order are in the subgroup. But $A_4$ contains 8 elements of order 3 (there are 8 different 3-cycles), and an index-2 subgroup of $A_4$ has size 6, so not all elements of odd order can lie in the subgroup. $\square$

That proof is very closely related to the first proof we gave.

<!-- page 2 -->

**Theorem 4.** *If $G$ is a finite group with a subgroup of index 2 then its commutator subgroup has even index.*

*Proof.* If $[G:H] = 2$ then $H \triangleleft G$, so $G/H$ is a group of size 2 and thus is abelian. In an abelian group the only commutator is trivial, so the reduction homomorphism $G \to G/H$ sends every commutator in $G$ to the identity of $G/H$. That means $H$ contains every commutator of $G$, so $H$ contains the commutator subgroup of $G$. The index in $G$ of the commutator subgroup of $G$ is therefore divisible by $[G:H] = 2$. $\square$

**Corollary 5.** *There is no subgroup of index 2 in $A_4$.*

*Proof.* We will show the commutator subgroup of $A_4$ has odd index, so $A_4$ has no index-2 subgroup by Theorem 4. The subgroup

$$V = \{(1), (12)(34), (13)(24), (14)(23)\}$$

is normal in $A_4$ and $A_4/V$ has size 3, hence is abelian, so the commutator subgroup of $A_4$ is inside $V$. Each element of $V$ is a commutator (*e.g.*, $(12)(34) = [(123),(124)]$), so $V$ is the commutator subgroup of $A_4$. It has index 3, which is odd. $\square$

**Theorem 6.** *Every group of size 6 is cyclic or isomorphic to $S_3$.*

*Proof.* This is a special case of the classification of groups of order $pq$ for distinct primes $p$ and $q$, but we give a self-contained treatment in this special case using group actions.

Let $G$ have size 6 and assume $G$ is not cyclic. We want to show $G \cong S_3$. By Cauchy's theorem, $G$ contains elements $a$ with order 2 and $b$ with order 3. The subgroup $H = \{1, a\}$ has index 3, so the usual left multiplication action of $G$ on the left coset space $G/H$ is a homomorphism $G \to \text{Sym}(G/H) \cong S_3$. If $g$ is in the kernel then $gH = H$, so $g \in H$. Thus, if the kernel is nontrivial then it contains $a$. In particular, $abH = bH$. Since $bH = \{b, ba\}$ and $abH = \{ab, aba\}$, either $b = ab$ or $b = aba$. The first choice is impossible, so $b = aba$. Since $a$ has order 2, $ab = ba^{-1} = ba$, which means $a$ and $b$ commute. Thus $ab$ has order $2 \cdot 3 = 6$, so $G$ is cyclic. We were assuming $G$ is not cyclic, so the kernel of the map $G \to \text{Sym}(G/H)$ is trivial, hence this is an isomorphism. $\square$

**Corollary 7.** *There is no subgroup of index 2 in $A_4$.*

*Proof.* If $A_4$ has an index-2 subgroup $H$, that subgroup has size 6 and therefore is isomorphic to either $\mathbf{Z}/(6)$ or $S_3$. There are no elements in $A_4$ with order 6, so the first choice is impossible: $H$ must be isomorphic to $S_3$. In $S_3$ there are three elements of order 2 (the transpositions). The group $A_4$ also has only three elements of order 2 (the (2,2)-cycles $(12)(34), (13)(24), (14)(23)$), so all the elements of order 2 in $A_4$ must lie in $H$.

However, the elements of order 2 in $S_3$ don't commute with each other while the elements of order 2 in $A_4$ do commute with each other, so we have a contradiction from $H$ being isomorphic to $S_3$. Alternatively, in $A_4$ the identity and the three elements of order 2 are a group (namely the group $V$ mentioned earlier), so $H$ contains a subgroup of order 4, but by Lagrange's theorem a group of order 6 can't have a subgroup of order 4. Again we have a contradiction. $\square$

The next approach, which shares some features of the proof of Corollary 7, was suggested to me by Michiel Vermeulen and is based on the following theorem.

**Theorem 8.** *A group of even order contains an element of order 2.*

<!-- page 3 -->

*Proof.* Let $G$ be a group with even order. Pair together each $g \in G$ with its inverse $g^{-1}$. The set $\{g, g^{-1}\}$ has two elements unless $g = g^{-1}$, meaning $g^2 = e$. Therefore

$$|G| = 2|\{\text{pairs } \{g, g^{-1}\} : g \neq g^{-1}\}| + |\{g \in G : g = g^{-1}\}|.$$

The left side is even by hypothesis, and the first term on the right side is even from the factor of 2. Therefore $|\{g \in G : g^2 = e\}|$ is even. This count is positive, since $g = e$ is one possibility where $g^2 = e$. Since this count is even, there must be at least one more such $g$, so some $g \neq e$ in $G$ satisfies $g^2 = e$, which implies $g$ has order 2. $\square$

While Cauchy's theorem says more generally that for each prime $p$ dividing the order of a finite group $G$ there is an element of $G$ with order $p$, that is more difficult to show than the special case $p = 2$.

**Corollary 9.** *There is no subgroup of index 2 in $A_4$.*

*Proof.* Assume $A_4$ has a subgroup $H$ with index 2. Then $|H| = 6$, so by Theorem 8 there is an $h \in H$ with order 2. In $A_4$ the elements of order 2 are the (2,2)-cycles $(12)(34)$, $(13)(24)$, and $(14)(23)$, so $H$ contains some (2,2)-cycle. Since index 2 subgroups are normal and all (2,2)-cycles in $A_4$ are conjugate in $A_4$, $H$ contains all the (2,2)-cycles of $A_4$. Then $H$ contains $V = \{(1), (12)(34), (13)(24), (14)(23)\}$, a group of order 4. However, by Lagrange's theorem a group of order 6 can't contain a subgroup of order 4, so we have a contradiction. $\square$

For more proofs of this result, see [1].

## References

[1] M. Brennan, D. Machale, Variations on a Theme: $A_4$ Definitely Has No Subgroup of Order Six!, *Math. Mag.* **73** (2000), 36--40. Online at https://www.maa.org/sites/default/files/269148715312.pdf.bannered.pdf.
