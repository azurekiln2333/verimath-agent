# Small Groups Up to Isomorphism

> **Source**: https://kconrad.math.uconn.edu/blurbs/gpisomlist.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory

<!-- page 1 -->

The table below lists all the groups of order $\leq 15$, up to isomorphism. That is, any group of order $\leq 15$ is isomorphic to exactly one group on this list. We write $G^2$ for $G \times G$ and $G^3$ for $G \times G \times G$, just as in linear algebra (where $\mathbf{R}^3$ means $\mathbf{R} \times \mathbf{R} \times \mathbf{R}$).

| $n$ | Groups of order $n$ | Number |
|-----|---------------------|--------|
| 1 | $\{0\}$ | 1 |
| 2 | $\mathbf{Z}/(2)$ | 1 |
| 3 | $\mathbf{Z}/(3)$ | 1 |
| 4 | $\mathbf{Z}/(4)$, $(\mathbf{Z}/(2))^2$ | 2 |
| 5 | $\mathbf{Z}/(5)$ | 1 |
| 6 | $\mathbf{Z}/(6)$, $S_3$ | 2 |
| 7 | $\mathbf{Z}/(7)$ | 1 |
| 8 | $\mathbf{Z}/(8)$, $\mathbf{Z}/(4) \times \mathbf{Z}/(2)$, $(\mathbf{Z}/(2))^3$, $D_4$, $Q_8$ | 5 |
| 9 | $\mathbf{Z}/(9)$, $(\mathbf{Z}/(3))^2$ | 2 |
| 10 | $\mathbf{Z}/(10)$, $D_5$ | 2 |
| 11 | $\mathbf{Z}/(11)$ | 1 |
| 12 | $\mathbf{Z}/(12)$, $\mathbf{Z}/(2) \times \mathbf{Z}/(6)$, $D_6$, $A_4$, $Q_{12}$ | 5 |
| 13 | $\mathbf{Z}/(13)$ | 1 |
| 14 | $\mathbf{Z}/(14)$, $D_7$ | 2 |
| 15 | $\mathbf{Z}/(15)$ | 1 |

The notation for these groups should be familiar to a student learning group theory except perhaps for the group of order 12 denoted $Q_{12}$, which can be described as a nontrivial semidirect product $\mathbf{Z}/(3) \rtimes \mathbf{Z}/(4)$.[^1]

Books that explicitly list groups of small order up to isomorphism usually stop at 15 since the number of non-isomorphic groups of order 16 jumps by quite a bit: there are 14 groups of order 16 up to isomorphism. Here they are.

Five are abelian:

$$\mathbf{Z}/16\mathbf{Z}, \quad \mathbf{Z}/(8) \times \mathbf{Z}/(2), \quad (\mathbf{Z}/(4))^2, \quad \mathbf{Z}/(4) \times (\mathbf{Z}/(2))^2, \quad (\mathbf{Z}/(2))^4.$$

Of the remaining nine groups of order 16, two can be described with dihedral groups:

$$D_8, \quad \mathbf{Z}/(2) \times D_4.$$

Two more can be described with quaternionic groups[^2]:

$$\mathbf{Z}/(2) \times Q_8, \quad Q_{16} = \langle x, y \mid x^8 = 1, y^2 = x^4, yxy^{-1} = x^{-1} \rangle.$$

<!-- page 2 -->

Two more can be described as mod 8 matrix groups:

$$\left\{\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} : a, b \in \mathbf{Z}/(8), a \equiv 1, 3 \bmod 8\right\},$$

$$\left\{\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} : a, b \in \mathbf{Z}/(8), a \equiv 1, 5 \bmod 8\right\}.$$

(The analogous group of mod 8 matrices $\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$ where $a \equiv 1, 7 \bmod 8$ is isomorphic to $D_8$.)

The remaining three groups of order 16 can be built as semi-direct products:

$$Q_8 \rtimes \mathbf{Z}/(2), \quad \mathbf{Z}/(4) \rtimes \mathbf{Z}/(4), \quad (\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4),$$

where $\mathbf{Z}/(2)$ acts on $Q_8$ by having $1 \bmod 2$ act by conjugation by $i$ (since $i^2 = -1$, conjugation by $i$ on $Q_8$ has order 2), $\mathbf{Z}/(4)$ acts on $\mathbf{Z}/(4)$ by having $1 \bmod 4$ act by negation, and $\mathbf{Z}/(4)$ acts on $(\mathbf{Z}/(2))^2$ by having $1 \bmod 4$ act by the matrix $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

Below is a table of these 14 groups, with the first 5 being abelian. The row for each group of order 16 counts solutions in the group to $g^2 = e$, $g^4 = e$, and $g^8 = e$. A noncyclic group has no element of order 16, so all elements have order dividing 8 and thus $\{g : g^8 = e\}$ is the whole group except for the cyclic group of order 16.

| | $G$ | $|\{g : g^2 = e\}|$ | $|\{g : g^4 = e\}|$ | $|\{g : g^8 = e\}|$ |
|--|-----|---------------------|---------------------|---------------------|
| 1 | $\mathbf{Z}/(16)$ | 2 | 4 | 8 |
| 2 | $\mathbf{Z}/(8) \times \mathbf{Z}/(2)$ | 4 | 8 | 16 |
| 3 | $\mathbf{Z}/(4) \times \mathbf{Z}/(4)$ | 4 | 16 | 16 |
| 4 | $(\mathbf{Z}/(2))^2 \times \mathbf{Z}/(4)$ | 8 | 16 | 16 |
| 5 | $(\mathbf{Z}/(2))^4$ | 16 | 16 | 16 |
| 6 | $D_8$ | 10 | 12 | 16 |
| 7 | $D_4 \times \mathbf{Z}_2$ | 12 | 16 | 16 |
| 8 | $Q_8 \times \mathbf{Z}/(2)$ | 4 | 16 | 16 |
| 13 | $Q_8 \rtimes \mathbf{Z}/(2)$ | 8 | 16 | 16 |
| 9 | $Q_{16}$ | 2 | 12 | 16 |
| 10 | $\left\{\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} : a \equiv 1, 3 \bmod 8\right\}$ | 6 | 12 | 16 |
| 11 | $\left\{\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} : a \equiv 1, 5 \bmod 8\right\}$ | 4 | 8 | 16 |
| 12 | $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ | 4 | 16 | 16 |
| 14 | $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$ | 8 | 16 | 16 |

The counts in the table prove these 14 groups are nonisomorphic except when the counts all agree, which happens for the groups given the same color. Since abelian and nonabelian groups are not isomorphic, it remains to compare $Q_8 \times \mathbf{Z}/(2)$ and $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$, and $Q_8 \rtimes \mathbf{Z}/(2)$ and $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$. In the second pair, $Q_8 \rtimes \mathbf{Z}/(2)$ and $(\mathbf{Z}/(2))^2 \rtimes \mathbf{Z}/(4)$, their centers are not isomorphic: the first group has a cyclic center and the second group has noncyclic center. While the first pair, $Q_8 \times \mathbf{Z}/(2)$ and $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$, have isomorphic (noncyclic) centers, just one nontrivial element of the center of $Q_8 \times \mathbf{Z}/(2)$ is a square in the whole group, while two nontrivial elements in the center of $\mathbf{Z}/(4) \rtimes \mathbf{Z}/(4)$ are squares in the whole group, so these groups are nonisomorphic.[^3]

Let $G(n)$ be the number of non-isomorphic groups of order $n$. A list of $G(n)$ for $n \leq 200$ is on

$$\texttt{https://kconrad.math.uconn.edu/nonisomgp.html},$$

<!-- page 3 -->

for $n \leq 2000$ is in [2, Appendix], and for $n < 2047$ is in [1, Appendix].

There is no general formula for $G(n)$, but values can be given for some $n$ depending on its prime factorization:

- for prime $p$,

$$G(p) = 1, \quad G(p^2) = 2, \quad G(p^3) = 5, \quad \text{and } G(p^4) = \begin{cases} 14, & \text{if } p = 2, \\ 15, & \text{if } p \neq 2, \end{cases}$$

- for distinct primes $p < q$,

$$G(pq) = \begin{cases} 1, & \text{if } q \not\equiv 1 \bmod p, \\ 2, & \text{if } q \equiv 1 \bmod p, \end{cases}$$

- for distinct primes $p < q < r$, $G(pqr)$ is determined by the following table.

| $r \bmod p$ | $r \bmod q$ | $q \bmod p$ | $G(pqr)$ |
|-------------|-------------|-------------|----------|
| $\not\equiv 1$ | $\not\equiv 1$ | $\not\equiv 1$ | 1 |
| $\equiv 1$ | $\not\equiv 1$ | $\not\equiv 1$ | 2 |
| $\not\equiv 1$ | $\equiv 1$ | $\not\equiv 1$ | 2 |
| $\not\equiv 1$ | $\not\equiv 1$ | $\equiv 1$ | 2 |
| $\not\equiv 1$ | $\equiv 1$ | $\equiv 1$ | 3 |
| $\equiv 1$ | $\equiv 1$ | $\not\equiv 1$ | 4 |
| $\equiv 1$ | $\not\equiv 1$ | $\equiv 1$ | $p + 2$ |
| $\equiv 1$ | $\equiv 1$ | $\equiv 1$ | $p + 4$ |

Check this table says that, up to isomorphism, there are 4 groups of order 30, 6 groups of order 42, and 2 groups of order 105.

## References

[1] J. H. Conway, H. Dietrich, and E. A. O'Brien, "Counting groups: gnus, moas, and other exotica," *Math. Intell.*, **30** (2008), 6--15. URL https://www.math.auckland.ac.nz/~obrien/research/gnu.pdf.

[2] H. U. Besche, B. Eick, and E. A. O'Brien, "A millennium project: constructing small groups," *Internat. J. Algebra Comput.* **12** (2002), 623--644. URL https://www.worldscientific.com/doi/epdf/10.1142/S0218196702001115.

[^1]: See https://kconrad.math.uconn.edu/blurbs/grouptheory/group12.pdf.

[^2]: Groups $Q_{2^n}$ are described in https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf.

[^3]: See https://kconrad.math.uconn.edu/blurbs/grouptheory/group16.pdf for more information about the groups of order 16.
