# Groups of Order 16

> **Source**: https://kconrad.math.uconn.edu/blurbs/group16.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory

<!-- page 1 -->

## 1. Introduction

There are 14 groups of order 16 up to isomorphism. This was first determined in 1893 by Holder [2] and Young [5]. A more recent proof of this result was given by Wild [4] in 2005.

These 14 groups are described in Table 1, with the 5 abelian ones listed first. The "GAP" number in the second column is the ordering among the groups of order 16 in the computer algebra package GAP, in case you want to find these groups in GAP or in tables online such as Dockchitser's site [1] where the GAP number is in the rightmost column. The "Wild" number in the third column is the ordering of these groups by Wild [4, Theorem 2].

| Group | GAP | Wild | Description |
|-------|-----|------|-------------|
| $\mathbf{Z}/(16)$ | 1 | 6 | Abelian |
| $\mathbf{Z}/(8) \times \mathbf{Z}/(2)$ | 5 | 1 | Abelian |
| $\mathbf{Z}/(4) \times \mathbf{Z}/(4)$ | 2 | 13 | Abelian |
| $(\mathbf{Z}/(2))^2 \times \mathbf{Z}/(4)$ | 10 | 7 | Abelian |
| $(\mathbf{Z}/(2))^4$ | 14 | 0 | Abelian |
| $D_8$ | 7 | 4 | |
| $D_4 \times \mathbf{Z}/(2)$ | 11 | 8 | |
| $Q_8 \times \mathbf{Z}/(2)$ | 12 | 11 | |
| $Q_8 \rtimes \mathbf{Z}/(2)$ | 13 | 10 | $(g, m)(h, n) = (gi^m hi^{-m}, m + n)$ |
| $Q_{16}$ | 9 | 5 | $\langle x, y \mid x^8 = 1, y^4 = 1, x^4 = y^2, yxy^{-1} = x^{-1} \rangle$ |
| $\mathbf{Z}/(8) \rtimes_3 \mathbf{Z}/(2)$ | 8 | 2 | $(a, b)(c, d) = (a + 3^b c, b + d)$ |
| $\mathbf{Z}/(8) \rtimes_5 \mathbf{Z}/(2)$ | 6 | 3 | $(a, b)(c, d) = (a + 5^b c, b + d)$ |
| $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ | 4 | 12 | $(a, b)(c, d) = (a + (-1)^b c, b + d)$ |
| $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ | 3 | 9 | $(v, m)(w, n) = (v + A^m w, m + n)$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ |

**Table 1.** Groups of order 16 up to isomorphism.

The group $Q_{16}$ is a generalized quaternion group.[^1] Five nonabelian groups in Table 1 are nontrivial semidirect products:

- $Q_8 \rtimes \mathbf{Z}/(2)$ has 1 mod 2 act on $Q_8$ as conjugation by $i$ (even though $i$ in $Q_8$ has order 4, $i^2 = -1 \in Z(Q_8)$, so conjugation by $i$ on $Q_8$ has order 2).
- $\mathbf{Z}/(8) \rtimes_3 \mathbf{Z}/(2)$ has 1 mod 2 act on $\mathbf{Z}/(8)$ by multiplication by 3.
- $\mathbf{Z}/(8) \rtimes_5 \mathbf{Z}/(2)$ has 1 mod 2 act on $\mathbf{Z}/(8)$ by multiplication by 5.
- $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ has 1 mod 4 act on $\mathbf{Z}/(4)$ by negation.
- $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ has 1 mod 4 act on $(\mathbf{Z}/(2))^2$ by the matrix $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

[^1]: See Section 3 of https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf.

<!-- page 2 -->

We will not explain here why every group of order 16 is isomorphic to some group in Table 1; for that, see [4]. What we will do, in the next section, is explain why the groups in Table 1 are nonisomorphic. In the course of this task we will see that some nonisomorphic groups of order 16 can have the same number of elements of each order.

## 2. Distinguishing the Groups of Order 16

In a group of order 16, every element has order 1, 2, 4, 8, or 16. Table 2 below indicates how many elements have each order in the groups from Table 1. Groups where these counts are all equal are given the same color.

| Group | GAP | Order 1 | Order 2 | Order 4 | Order 8 | Order 16 |
|-------|-----|---------|---------|---------|---------|----------|
| $\mathbf{Z}/(16)$ | 1 | 1 | 1 | 2 | 4 | 8 |
| $\mathbf{Z}/(8) \times \mathbf{Z}/(2)$ | 5 | 1 | 3 | 4 | 8 | 0 |
| $\mathbf{Z}/(4) \times \mathbf{Z}/(4)$ | 2 | 1 | 3 | 12 | 0 | 0 |
| $(\mathbf{Z}/(2))^2 \times \mathbf{Z}/(4)$ | 10 | 1 | 7 | 8 | 0 | 0 |
| $(\mathbf{Z}/(2))^4$ | 14 | 1 | 15 | 0 | 0 | 0 |
| $D_8$ | 7 | 1 | 9 | 2 | 4 | 0 |
| $D_4 \times \mathbf{Z}/(2)$ | 11 | 1 | 11 | 4 | 0 | 0 |
| $Q_8 \times \mathbf{Z}/(2)$ | 12 | 1 | 3 | 12 | 0 | 0 |
| $Q_8 \rtimes \mathbf{Z}/(2)$ | 13 | 1 | 7 | 8 | 0 | 0 |
| $Q_{16}$ | 9 | 1 | 1 | 10 | 4 | 0 |
| $\mathbf{Z}/(8) \rtimes_3 \mathbf{Z}/(2)$ | 8 | 1 | 5 | 6 | 4 | 0 |
| $\mathbf{Z}/(8) \rtimes_5 \mathbf{Z}/(2)$ | 6 | 1 | 3 | 4 | 8 | 0 |
| $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ | 4 | 1 | 3 | 12 | 0 | 0 |
| $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ | 3 | 1 | 7 | 8 | 0 | 0 |

**Table 2.** Groups of order 16 with orders of elements.

The counts in Table 2 can let us determine which group in Table 1 some other group of order 16 is isomorphic to.

**Example 2.1.** Let $G = (\mathbf{Z}/(4) \times \mathbf{Z}/(2)) \rtimes \mathbf{Z}/(2)$, where we make 1 mod 2 in $\mathbf{Z}/(2)$ act on $\mathbf{Z}/(4) \times \mathbf{Z}/(2)$ by negation, which is an automorphism of order 2. Check that $G$ has 11 elements of order 2 (these are the $(v, 0)$ where $v = (2, 0)$, $(2, 1)$, and $(0, 1)$ and all 8 elements $(v, 1)$), so $G \cong D_4 \times \mathbf{Z}/(2)$ by Table 2.

**Example 2.2.** Let $G = \mathbf{Z}/(8) \rtimes_7 \mathbf{Z}/(2)$, where
$$
(a, b)(c, d) = (a + 7^b c, b + d) = (a + (-1)^b c, b + d).
$$
Check $G$ is nonabelian with two elements of order 4 (these are $(2, 0)$ and $(6, 0)$), so $G \cong D_8$ by Table 2. In fact, for every $n \geq 3$ we have $\mathbf{Z}/(n) \rtimes \mathbf{Z}/(2) \cong D_n$ where $(a, b)(c, d) = (a + (-1)^b c, b + d)$ in the semidirect product.

Here are the nonisomorphic groups of order 16 having the same number of elements of each order:

- $\mathbf{Z}/(8) \times \mathbf{Z}/(2)$ and $\mathbf{Z}/(8) \rtimes_5 \mathbf{Z}/(2)$. These are not isomorphic since the first is abelian and the second isn't. (These groups also have the same subgroup lattice.)
- $\mathbf{Z}/(4) \times \mathbf{Z}/(4)$, $Q_8 \times \mathbf{Z}/(2)$, and $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$. The first one is abelian and the other two are nonabelian. We'll distinguish the nonabelian groups below.

<!-- page 3 -->

- $(\mathbf{Z}/(2))^2 \times \mathbf{Z}/(4)$, $Q_8 \rtimes \mathbf{Z}/(2)$, and $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$. The first one is abelian and the other two are nonabelian. We'll distinguish the nonabelian groups below.

That groups of order 16 can be nonisomorphic but have the same number of elements of each order was first pointed out by Miller [3, p. 270] in 1898. This does not happen for groups of order less than 16 or for abelian groups: a finite abelian group is determined up to isomorphism by the number of elements it has of each order. Here is an infinite collection of pairs of nonisomorphic groups with the same number of elements of each order. For odd primes $p$, the abelian group $(\mathbf{Z}/(p))^3$ and the nonabelian matrix group
$$
\left\{ \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} : a, b, c \in \mathbf{Z}/(p) \right\}
$$
have order $p^3$. All non-identity elements in $(\mathbf{Z}/(p))^3$ have order $p$, and this is true in the matrix group too on account of the power formula
$$
\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}^n = \begin{pmatrix} 1 & na & nb + \frac{n(n-1)}{2}ac \\ 0 & 1 & nc \\ 0 & 0 & 1 \end{pmatrix}
$$
for $n \in \mathbf{Z}$, which at $n = p$ becomes
$$
\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}^p = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
because $p$ and $p(p-1)/2$ are 0 in $\mathbf{Z}/(p)$ when $p > 2$. (For $p = 2$, the matrix group has elements of order 4 while all non-identity elements of $(\mathbf{Z}/(2))^3$ have order 2.)

Returning to nonabelian groups in Table 2 with the same number of elements of each order, we can show they are nonisomorphic by looking at their centers. To distinguish between $Q_8 \rtimes \mathbf{Z}/(2)$ and $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$, check the centers: $Q_8 \rtimes \mathbf{Z}/(2)$ has center $\langle (i, 1) \rangle \cong \mathbf{Z}/(4)$ and $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ has center $\langle \left(\binom{0}{0}, 2\right), \left(\binom{1}{0}, 0\right) \rangle \cong (\mathbf{Z}/(2))^2$. Both centers have order 4, with the first being cyclic and the second being noncyclic. Since the centers are not isomorphic, the original groups are not isomorphic.

To distinguish between $Q_8 \times \mathbf{Z}/(2)$ and $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ we can also use their centers, but the situation is more subtle: $Q_8 \times \mathbf{Z}/(2)$ has center $\{\pm 1\} \times \{0, 1\}$ and $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ has center $\{0, 2\} \times \{0, 2\}$, which are both isomorphic to $(\mathbf{Z}/(2))^2$ and thus don't distinguish the groups in the same way as the previous pair of groups. Here's a distinction: in the center of $Q_8 \times \mathbf{Z}/(2)$ just one nontrivial element is a square in the whole group ($(-1, 0) = (i, 0)^2$), while in the center of $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ two nontrivial elements are squares in the whole group ($(2, 0) = (1, 0)^2$ and $(0, 2) = (0, 1)^2$). Since the centers don't have the same number of nontrivial elements that are squares in the whole group, $Q_8 \times \mathbf{Z}/(2)$ and $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ are not isomorphic.

To summarize, we can determine with one exception whether two groups of order 16 are isomorphic by

- counting the number of elements of each order in both groups (or just of order 2 and 4),
- computing the centers of both groups up to isomorphism if the groups have the same number of elements of each order.

<!-- page 4 -->

Two groups of order 16 that are not distinguished by these two calculations must be isomorphic to $Q_8 \times \mathbf{Z}/(2)$ or $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$, and in that case we can determine if they are isomorphic by checking how many nontrivial elements in their centers are squares in the whole group.

**Example 2.3.** Let $G = D_4 \rtimes \mathbf{Z}/(2)$, where 1 mod 2 acts on $D_4$ as conjugation by $r$. Then $(g, 0)^2 = (g^2, 0)$ and $(g, 1)^2 = (grgr^{-1}, 0)$, so the number of elements of each order is 1, 7, 8, 0, and 0. That implies $G$ is isomorphic to $Q_8 \rtimes \mathbf{Z}/(2)$ or $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ and we can tell these apart by their centers: $Z(G)$ contains $(r, 1)$, which has order 4, so $Z(G)$ is cyclic and thus $G \cong Q_8 \rtimes \mathbf{Z}/(2)$.

A group $G$ of order 16 has a nontrivial center $Z$, and if $G$ is nonabelian then we can show $|Z| \leq 4$ by contradiction. If $|Z| > 4$ then $|Z| = 8$ since $G$ is nonabelian, so $|G/Z| = 2$. A standard result in group theory is that if $G/Z$ is cyclic then $G$ is abelian. If $|G/Z| = 2$ then $G/Z$ is cyclic, so $G$ is abelian and we have a contradiction since $G$ is nonabelian. Thus $|Z| \leq 4$ when $|G| = 16$ and $G$ is nonabelian. Table 3 collects the nine nonabelian groups of order 16 together according to their center (up to isomorphism), which has order 2 or 4. In the first two rows, where $|Z| = 4$, $G/Z$ isn't cyclic (otherwise $G$ would be abelian, which isn't true) and thus $G/Z \cong (\mathbf{Z}/(2))^2$ for all nonabelian $G$ with a center of order 4.

| Center | Groups of order 16 with that center, up to isomorphism |
|--------|-------------------------------------------------------|
| $\mathbf{Z}/(4)$ | $\mathbf{Z}/(8) \rtimes_5 \mathbf{Z}/(2)$, $Q_8 \rtimes \mathbf{Z}/(2)$ |
| $(\mathbf{Z}/(2))^2$ | $D_4 \times \mathbf{Z}/(2)$, $Q_8 \times \mathbf{Z}/(2)$, $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$, $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ |
| $\mathbf{Z}/(2)$ | $D_8$, $Q_{16}$, $\mathbf{Z}/(8) \rtimes_3 \mathbf{Z}/(2)$ |

**Table 3.** Nonabelian groups of order 16 having a specific center.

## References

[1] T. Dockchitser, Group Names, https://people.maths.bris.ac.uk/~matyd/GroupNames/.

[2] O. Holder, "Die Gruppen der Ordnungen $p^3$, $pq^2$, $pqr$, $p^4$," *Math. Ann.* **43** (1893), 301-412. URL https://eudml.org/doc/157685.

[3] G. A. Miller, "The Regular Substitution Groups Whose Orders are Less than 48," *Quart. J. Pure Appl. Math.* **28** (1896), 232-284. URL https://gdz.sub.uni-goettingen.de/id/PPN600494829_0028.

[4] M. Wild, "The Groups of Order Sixteen Made Easy" *Amer. Math. Monthly* **112** (2005), 20-31. URL https://www.jstor.org/stable/30037381.

[5] J. Young, "On the determination of the groups whose order is a power of a prime," *Amer. J. Math.* **15** (1893), 124-178. URL https://www.jstor.org/stable/2369564.
