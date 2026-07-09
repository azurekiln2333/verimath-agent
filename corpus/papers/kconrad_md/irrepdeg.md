# The Degree May Not Divide the Size of the Group

> **Source**: https://kconrad.math.uconn.edu/blurbs/irrepdeg.pdf  
> **Author**: Keith Conrad  
> **Topic**: representation_theory

<!-- page 1 -->

Any irreducible finite-dimensional representation of a finite group over $\mathbf{C}$ (or more generally over an algebraically closed field whose characteristic doesn't divide the size of the group) has degree dividing the size of the group. This can fail for representations in positive characteristic. To see this explicitly, we'll find a 5-dimensional irreducible representation of $\mathrm{SL}_2(\mathbf{F}_{13})$ in characteristic 13. Note the size of the group is $2^3 \cdot 3 \cdot 7 \cdot 13 = 2184$, which is not divisible by 5.

To begin, we work with representations of $\mathrm{SL}_2(\mathbf{C})$, and then see how much the proof depends on the field of scalars being $\mathbf{C}$.

For a positive integer $d$, let $V_{d,2}$ be the space of homogeneous degree $d$ polynomials in two variables over the complex numbers:

$$
V_{d,2} = \left\{ \sum_{i+j=d} a_{ij} X^i Y^j : a_{ij} \in \mathbf{C} \right\}.
$$

We make $\mathrm{SL}_2(\mathbf{C})$ act on the polynomials $f(X,Y) \in V_{d,2}$ by

$$
\left( \begin{pmatrix} a & b \\ c & d \end{pmatrix} f \right)(X,Y) = f\!\left( \begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} \begin{pmatrix} X \\ Y \end{pmatrix} \right) = f(dX - bY, -cX + aY),
$$

where we need to use the matrix inverse to have a left action instead of a right action. Check that this is a linear representation of (the infinite group) $\mathrm{SL}_2(\mathbf{C})$ on $V_{d,2}$, which is a $(d+1)$-dimensional space with basis $e_i = X^i Y^{d-i}$, $0 \leq i \leq d$.

## 1. Theorem 1

**Theorem 1.** *Let $W$ be an $\mathrm{SL}_2(\mathbf{C})$-stable subspace of $V_{d,2}$ which contains a sum*

$$
\sum_{\ell \in S} c_\ell e_\ell, \quad c_\ell \in \mathbf{C}^\times,
$$

*where $S \subset \{0, \ldots, d\}$. Then $W$ contains each such $e_\ell$.*

*Proof.* The result is clear if the sum contains only one term, since the coefficients are nonzero.

For $t \in \mathbf{C}$, let

$$
g_t = \begin{pmatrix} t & 0 \\ 0 & t^{-1} \end{pmatrix},
$$

which is in $\mathrm{SL}_2(\mathbf{C})$. It is easy to check that $g_t(e_i) = t^{d-2i} e_i$. Let's suppose that the numbers

$$
t^{-d}, t^{-d+2}, \ldots, t^{d-2}, t^d
$$

are all distinct. Certainly almost any complex number can be chosen with that property. Make such a choice of $t$.

Let $v = \sum_{\ell \in S} c_\ell e_\ell$ be as in the statement of the theorem. Then $g_t(v) \in W$. By calculation,

$$
g_t(v) = \sum_{\ell \in S} c_\ell t^{d-2\ell} e_\ell \in W.
$$

<!-- page 2 -->

Let $k$ be an element of $S$. Then

$$
t^{d-2k} v - g_t v = \sum_{\ell \in S, \ell \neq k} (t^{d-2k} - t^{d-2\ell}) c_\ell e_\ell \in W.
$$

By hypothesis, $t^{d-2k} \neq t^{d-2\ell}$ for $\ell \neq k$. Thus the sum runs over $\ell \in S - \{k\}$ with nonzero coefficients. Hence there are fewer terms in the sum, so by induction on the number of (nonzero) addends, $e_\ell \in W$ for $\ell \in S - \{k\}$. And thus $e_k \in W$ as well. $\square$

## 2. Theorem 2

**Theorem 2.** *This representation of $\mathrm{SL}_2(\mathbf{C})$ on $V_{d,2}$ is irreducible.*

*Proof.* Let $W$ be a nonzero $\mathrm{SL}_2(\mathbf{C})$-stable subspace of $V_{d,2}$. By Theorem 1, $W$ contains some $e_i$. Let $j = d - i$. By $\mathrm{SL}_2(\mathbf{C})$-stability, $W$ contains

$$
\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} X^i Y^j = (X - Y)^i Y^j = \sum_{k=0}^{i} \binom{i}{k} X^k (-Y)^{i-k} Y^j = \sum_{k=0}^{i} (-1)^{i-k} \binom{i}{k} X^k Y^{d-k}.
$$

The coefficients $(-1)^{i-k} \binom{i}{k}$ are nonzero, so by Theorem 1 we have $X^k Y^{d-k} \in W$ for $k \leq i$. In particular, $Y^d \in W$. Then $W$ contains

$$
\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} Y^d = (X - Y)^d = \sum_{k=0}^{d} (-1)^{d-k} \binom{d}{k} X^k Y^{d-k}.
$$

The coefficients $(-1)^{d-k} \binom{d}{k}$ are nonzero for all $k \leq d$, so again by Theorem 1, $X^k Y^{d-k} \in W$ for all $k \leq d$. Thus $W = V_{d,2}$. $\square$

To what extent did this argument depend on the field of scalars being the complex numbers? Not much. Let $F$ be any field, with algebraic closure $\overline{F}$. Let $\mathrm{SL}_2(F)$ act on

$$
V_{d,2}(\overline{F}) = \left\{ \sum_{i+j=d} a_{ij} X^i Y^j : a_{ij} \in \overline{F} \right\}
$$

by the same way as in the complex case. In particular, for every finite field $\mathbf{F}_p$ we get a $(d+1)$-dimensional representation of the finite group $\mathrm{SL}_2(\mathbf{F}_p)$ on the vector space $V_{d,2}(\overline{\mathbf{F}}_p)$. Of course this also gives a representation of the infinite group $\mathrm{SL}_2(\overline{\mathbf{F}}_p)$, but our goal is to get an irreducible representation of a finite group.

Is this representation of $\mathrm{SL}_2(\mathbf{F}_p)$ irreducible? To make the proof over the complex numbers work in characteristic $p$, we need to be able to choose a $t \in \mathbf{F}_p^\times$ such that the numbers

$$
t^{-d}, t^{-d+2}, \ldots, t^{d-2}, t^d
$$

are all distinct. (It does not suffice to choose $t \in \overline{\mathbf{F}}_p$ with this property since the proof of irreducibility of the representation of $\mathrm{SL}_2(\mathbf{F}_p)$ needs the matrices $g_t$ to lie in the finite group $\mathrm{SL}_2(\mathbf{F}_p)$ we're representing!) We can choose such a $t$ by using a generator of $\mathbf{F}_p^\times$, provided $d < (p-1)/2$. Moreover, for such a choice the binomial coefficients that arise in the proof of Theorem 2 are nonzero in $\mathbf{F}_p$, so that proof works in characteristic $p$.

Thus for $d < (p-1)/2$ the space $V_{d,2}(\overline{\mathbf{F}}_p)$ gives a $(d+1)$-dimensional irreducible $\overline{\mathbf{F}}_p$-representation of $\mathrm{SL}_2(\mathbf{F}_p)$. These representations are naturally defined over $\mathbf{F}_p$: the action of $\mathrm{SL}_2(\mathbf{F}_p)$ on the standard basis of $V_{d,2}(\overline{\mathbf{F}}_p)$ gives a representation of $\mathrm{SL}_2(\mathbf{F}_p)$ in $V_{d,2}(\mathbf{F}_p)$. We want both $d < (p-1)/2$ and $d+1$ not to divide $|\mathrm{SL}_2(\mathbf{F}_p)| = (p^2-1)(p^2-p)/(p-1) = (p-1)p(p+1)$. These can't both be satisfied for $p = 2, 3, 5, 7, 11$. But they can be for $p = 13$, by taking $d = 4$. (The corresponding basis is $X^4, X^3Y, X^2Y^2, XY^3, Y^4$.)

<!-- page 3 -->

So $V_{4,2}(\overline{\mathbf{F}}_{13})$ provides a 5-dimensional irreducible representation of $\mathrm{SL}_2(\mathbf{F}_{13})$, a group of size $12 \cdot 13 \cdot 14 = 2184$, which is not divisible by 5.

Actually, the constraint $d < (p-1)/2$ can be weakened. For any $d \leq p-1$, $V_{d,2}(\overline{\mathbf{F}}_p)$ is an irreducible representation of $\mathrm{SL}_2(\mathbf{F}_p)$ by the indicated action. The proof given here just doesn't work that generally. For a more general proof, see [1, pp. 14--16]. (These are all the absolutely irreducible representations of $\mathrm{SL}_2(\mathbf{F}_p)$ in characteristic $p$.) Using $d \leq p-1$, we can take $p = 7$ and $d = 4$: $V_{4,2}(\overline{\mathbf{F}}_7)$ is a 5-dimensional irreducible representation of $\mathrm{SL}_2(\mathbf{F}_7)$, which has size $6 \cdot 7 \cdot 8 = 336$ that is not a multiple of 5.

Notice that the only scalar matrices in $\mathrm{SL}_2(\mathbf{F}_p)$ are $\pm I$. The effect of $-I$ on $e_i \in V_{d,2}$ is $(-X)^i(-Y)^{d-i} = (-1)^d e_i$, so for even $d$ the matrix $-I$ acts trivially, hence we get a representation of the group $\mathrm{SL}_2(\mathbf{F}_p)/\{\pm I\} = \mathrm{PSL}_2(\mathbf{F}_p)$, which (for $p \geq 5$) is a *simple* group. In particular, $V_{4,2}(\overline{\mathbf{F}}_7)$ is an irreducible 5-dimensional representation of the simple group $\mathrm{PSL}_2(\mathbf{F}_7)$ of order 168, which is not divisible by 5.

## References

[1] J. Alperin, *Local Representation Theory*, Cambridge Univ. Press, Cambridge, 1986.
