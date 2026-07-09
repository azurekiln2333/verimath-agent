# Applications of Galois Theory

> **Source**: https://kconrad.math.uconn.edu/blurbs/galoisappn.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory

<!-- page 1 -->

We'll examine here several types of applications of Galois theory: examples of the Galois correspondence in Section 1, theorems about field extensions in Section 2, a description of minimal polynomials in a Galois extension in Sections 3, and a brief indication of what lies beyond Galois theory of finite extensions in Section 4.

## 1. Examples

**Example 1.1.** The field extension $\mathbf{Q}(\sqrt{2}, \sqrt{3})/\mathbf{Q}$ is Galois of degree $4$, so its Galois group has order $4$. The elements of the Galois group are determined by their values on $\sqrt{2}$ and $\sqrt{3}$. The $\mathbf{Q}$-conjugates of $\sqrt{2}$ and $\sqrt{3}$ are $\pm\sqrt{2}$ and $\pm\sqrt{3}$, so we get at most four possible automorphisms in the Galois group. See Table 1. Since the Galois group has order $4$, these $4$ possible assignments of values to $\sigma(\sqrt{2})$ and $\sigma(\sqrt{3})$ all really exist.

| $\sigma$ | $\sigma(\sqrt{2})$ | $\sigma(\sqrt{3})$ |
|---|---|---|
| $\mathrm{id.}$ | $\sqrt{2}$ | $\sqrt{3}$ |
| $\sigma_1$ | $\sqrt{2}$ | $-\sqrt{3}$ |
| $\sigma_2$ | $-\sqrt{2}$ | $\sqrt{3}$ |
| $\sigma_3$ | $-\sqrt{2}$ | $-\sqrt{3}$ |

Table 1.

The automorphisms $\sigma_1$, $\sigma_2$, and $\sigma_3$ in Table 1 have order $2$. Since $\mathrm{Gal}(\mathbf{Q}(\sqrt{2}, \sqrt{3})/\mathbf{Q})$ contains $3$ elements of order $2$, $\mathbf{Q}(\sqrt{2}, \sqrt{3})$ has $3$ subfields $K_i$ such that $[\mathbf{Q}(\sqrt{2}, \sqrt{3}) : K_i] = 2$, or equivalently $[K_i : \mathbf{Q}] = 4/2 = 2$. Two such fields are $\mathbf{Q}(\sqrt{2})$ and $\mathbf{Q}(\sqrt{3})$. A third is $\mathbf{Q}(\sqrt{6})$ and that completes the list. Here is a diagram of all the subfields.

```
        Q(sqrt(2), sqrt(3))
       /        |         \
  Q(sqrt(2))  Q(sqrt(3))  Q(sqrt(6))
       \        |         /
              Q
```

In Table 1, the subgroup fixing $\mathbf{Q}(\sqrt{2})$ is $\langle \sigma_1 \rangle$, the subgroup fixing $\mathbf{Q}(\sqrt{3})$ is $\langle \sigma_2 \rangle$, and the subgroup fixing $\mathbf{Q}(\sqrt{6})$ is $\langle \sigma_3 \rangle$ (since $(-\sqrt{2})(-\sqrt{3}) = \sqrt{2}\sqrt{3}$).

The effect of $\mathrm{Gal}(\mathbf{Q}(\sqrt{2}, \sqrt{3})/\mathbf{Q})$ on $\sqrt{2} + \sqrt{3}$ is given in Table 2. The $4$ values are all different, since $\sqrt{2}$ and $\sqrt{3}$ are linearly independent over $\mathbf{Q}$. Therefore $\mathbf{Q}(\sqrt{2}, \sqrt{3}) = \mathbf{Q}(\sqrt{2} + \sqrt{3})$. The minimal polynomial of $\sqrt{2} + \sqrt{3}$ over $\mathbf{Q}$ must be
$$(X - (\sqrt{2} + \sqrt{3}))(X - (-\sqrt{2} + \sqrt{3}))(X - (\sqrt{2} - \sqrt{3}))(X - (-\sqrt{2} - \sqrt{3})) = X^4 - 10X^2 + 1.$$

<!-- page 2 -->

| $\sigma$ | $\sigma(\sqrt{2})$ | $\sigma(\sqrt{3})$ | $\sigma(\sqrt{2} + \sqrt{3})$ |
|---|---|---|---|
| $\mathrm{id.}$ | $\sqrt{2}$ | $\sqrt{3}$ | $\sqrt{2} + \sqrt{3}$ |
| $\sigma_1$ | $\sqrt{2}$ | $-\sqrt{3}$ | $\sqrt{2} - \sqrt{3}$ |
| $\sigma_2$ | $-\sqrt{2}$ | $\sqrt{3}$ | $-\sqrt{2} + \sqrt{3}$ |
| $\sigma_3$ | $-\sqrt{2}$ | $-\sqrt{3}$ | $-\sqrt{2} - \sqrt{3}$ |

Table 2.

In particular, $X^4 - 10X^2 + 1$ is irreducible in $\mathbf{Q}[X]$ since it's a minimal polynomial over $\mathbf{Q}$.

By similar reasoning, if a field $F$ does not have characteristic $2$ and $a$ and $b$ are nonsquares in $F$ such that $ab$ is not a square in $F$ either, then $[F(\sqrt{a}, \sqrt{b}) : F] = 4$ and all the fields between $F$ and $F(\sqrt{a}, \sqrt{b})$ are as in the following diagram.

```
        F(sqrt(a), sqrt(b))
       /        |         \
  F(sqrt(a))  F(sqrt(b))  F(sqrt(ab))
       \        |         /
              F
```

Furthermore, $F(\sqrt{a}, \sqrt{b}) = F(\sqrt{a} + \sqrt{b})$. The argument is as in the special case above.

**Example 1.2.** While $\mathbf{Q}(\sqrt[4]{2})/\mathbf{Q}$ is not Galois, $\mathbf{Q}(\sqrt[4]{2})$ lies in $\mathbf{Q}(\sqrt[4]{2}, i)$, which is Galois over $\mathbf{Q}$. We will use Galois theory for $\mathbf{Q}(\sqrt[4]{2}, i)/\mathbf{Q}$ to find the intermediate fields in $\mathbf{Q}(\sqrt[4]{2})/\mathbf{Q}$.

The Galois group of $\mathbf{Q}(\sqrt[4]{2}, i)/\mathbf{Q}$ equals $\langle r, s \rangle$, where
$$r(\sqrt[4]{2}) = i\sqrt[4]{2}, \quad r(i) = i \quad \text{and} \quad s(\sqrt[4]{2}) = \sqrt[4]{2}, \quad s(i) = -i.$$
(Viewing elements of $\mathbf{Q}(\sqrt[4]{2}, i)$ as complex numbers, $s$ acts on them like complex conjugation.) The group $\langle r, s \rangle$ is isomorphic to $D_4$, where $r$ corresponds to a $90$ degree rotation of the square and $s$ corresponds to a reflection across a diagonal. What is the subgroup $H$ of $\mathrm{Gal}(\mathbf{Q}(\sqrt[4]{2}, i)/\mathbf{Q})$ corresponding to $\mathbf{Q}(\sqrt[4]{2})$?

$$\begin{array}{cc}
\mathbf{Q}(\sqrt[4]{2}, i) & \{1\} \\
\mid_{2} & \mid_{2} \\
\mathbf{Q}(\sqrt[4]{2}) & H \\
\mid_{4} & \mid_{4} \\
\mathbf{Q} & D_4
\end{array} \tag{1.1}$$

Since $s$ is a nontrivial element of the Galois group that fixes $\mathbf{Q}(\sqrt[4]{2})$, $s \in H$. The size of $H$ is $[\mathbf{Q}(\sqrt[4]{2}, i) : \mathbf{Q}(\sqrt[4]{2})] = 2$, so $H = \{1, s\} = \langle s \rangle$. By the Galois correspondence for $\mathbf{Q}(\sqrt[4]{2}, i)/\mathbf{Q}$, fields strictly between $\mathbf{Q}(\sqrt[4]{2})$ and $\mathbf{Q}$ correspond to subgroups of the Galois group strictly between $\langle s \rangle$ and $\langle r, s \rangle$. From the known subgroup structure of $D_4$, the only subgroup lying strictly between $\langle s \rangle$ and $\langle r, s \rangle$ is $\langle r^2, s \rangle$. Therefore only one field lies strictly between $\mathbf{Q}(\sqrt[4]{2})$ and $\mathbf{Q}$. Since $\mathbf{Q}(\sqrt{2})$ is such a field it is the only one.

<!-- page 3 -->

**Remark 1.3.** While Galois theory provides the most systematic method to find intermediate fields, it may be possible to argue in other ways. For example, suppose $\mathbf{Q} \subset F \subset \mathbf{Q}(\sqrt[4]{2})$ with $[F : \mathbf{Q}] = 2$. Then $\sqrt[4]{2}$ has degree $2$ over $F$. Since $\sqrt[4]{2}$ is a root of $X^4 - 2$, its minimal polynomial over $F$ has to be a quadratic factor of $X^4 - 2$. There are three monic quadratic factors with $\sqrt[4]{2}$ as a root, but only one of them, $X^2 - \sqrt{2}$, has coefficients in $\mathbf{Q}(\sqrt[4]{2})$ (let alone in $\mathbf{R}$). Therefore $X^2 - \sqrt{2}$ must be the minimal polynomial of $\sqrt[4]{2}$ over $F$, so $\sqrt{2} \in F$. Since $[F : \mathbf{Q}] = 2$, $F = \mathbf{Q}(\sqrt{2})$ by counting degrees.

**Example 1.4.** Let's explore $\mathbf{Q}(\sqrt[4]{2}, \zeta_8)$, where $\zeta_8 = e^{2\pi i/8}$ is a root of unity of order $8$, whose minimal polynomial over $\mathbf{Q}$ is $X^4 + 1$. Both $\mathbf{Q}(\sqrt[4]{2})$ and $\mathbf{Q}(\zeta_8)$ have degree $4$ over $\mathbf{Q}$. Since $\zeta_8^2 = i$, $\mathbf{Q}(\sqrt[4]{2}, \zeta_8)$ is a splitting field over $\mathbf{Q}$ of $(X^4 - 2)(X^4 + 1)$ and therefore is Galois over $\mathbf{Q}$. What is its Galois group? We have the following field diagram.

```
          Q(sqrt[4]{2}, zeta_8)
          /                  \
        <=4                  <=4
        /                      \
  Q(sqrt[4]{2})              Q(zeta_8)
        \                      /
          4                  4
            \              /
                  Q
```

Thus $[\mathbf{Q}(\sqrt[4]{2}, \zeta_8) : \mathbf{Q}]$ is at most $16$. We will see the degree is *not* $16$: there are some hidden algebraic relations between $\sqrt[4]{2}$ and $\zeta_8$.

Any $\sigma \in \mathrm{Gal}(\mathbf{Q}(\sqrt[4]{2}, \zeta_8)/\mathbf{Q})$ is determined by its values
$$\sigma(\zeta_8) = \zeta_8^a \quad (a \in (\mathbf{Z}/8\mathbf{Z})^\times) \quad \text{and} \quad \sigma(\sqrt[4]{2}) = i^b \sqrt[4]{2} \quad (b \in \mathbf{Z}/4\mathbf{Z}). \tag{1.2}$$
There are $4$ choices each for $a$ and $b$. Taking independent choices of $a$ and $b$, there are at most $16$ automorphisms in the Galois group. But the choices of $a$ and $b$ *can not* be made independently because $\zeta_8$ and $\sqrt[4]{2}$ are linked to each other:
$$\zeta_8 + \zeta_8^{-1} = e^{2\pi i/8} + e^{-2\pi i/8} = 2\cos\left(\frac{\pi}{4}\right) = \sqrt{2} = \sqrt[4]{2}^2. \tag{1.3}$$
This says $\sqrt{2}$ belongs to both $\mathbf{Q}(\zeta_8)$ and $\mathbf{Q}(\sqrt[4]{2})$. Here is a field diagram that emphasizes the common subfield $\mathbf{Q}(\sqrt{2})$ in $\mathbf{Q}(\sqrt[4]{2})$ and $\mathbf{Q}(\zeta_8)$. This subfield is the source of (1.3).

```
          Q(sqrt[4]{2}, zeta_8)
          /                  \
        <=4                  <=4
        /                      \
  Q(sqrt[4]{2})              Q(zeta_8)
        \                      /
          2                  2
            \              /
          Q(sqrt(2))      Q(i)
            \              /
              2          2
                \      /
                  Q
```

Rewriting $\zeta_8 + \zeta_8^{-1} = \sqrt{2}$ as $\zeta_8^2 - \sqrt{2}\zeta_8 + 1 = 0$, $\zeta_8$ has degree at most $2$ over $\mathbf{Q}(\sqrt[4]{2})$. Since $\zeta_8$ is not real, it isn't inside $\mathbf{Q}(\sqrt[4]{2})$, so it has degree $2$ over $\mathbf{Q}(\sqrt[4]{2})$. Therefore

<!-- page 4 -->

$[\mathbf{Q}(\sqrt[4]{2}, \zeta_8) : \mathbf{Q}] = 2 \cdot 4 = 8$ and the degrees marked as "$\leq 4$" in the diagram both equal $2$. We rewrite the field diagram below.

```
          Q(sqrt[4]{2}, zeta_8)
          /                  \
          2                  2
        /                      \
  Q(sqrt[4]{2})              Q(zeta_8)
        \                      /
          2                  2
            \              /
          Q(sqrt(2))      Q(i)
            \              /
              2          2
                \      /
                  Q
```

Returning to the Galois group, (1.3) tells us the effect of $\sigma \in \mathrm{Gal}(\mathbf{Q}(\sqrt[4]{2}, \zeta_8)/\mathbf{Q})$ on $\sqrt[4]{2}$ partially determines it on $\zeta_8$, and conversely: $(\sigma(\sqrt[4]{2}))^2 = \sigma(\zeta_8) + \sigma(\zeta_8)^{-1}$, which in the notation of (1.2) is the same as
$$(-1)^b = \frac{\zeta_8^a + \zeta_8^{-a}}{\sqrt{2}}. \tag{1.4}$$
Since $\zeta_8 = e^{2\pi i/8} = (1 + i)/\sqrt{2}$, a calculation shows $\zeta_8^a + \zeta_8^{-a} = \sqrt{2}$ if $a \equiv 1, 7 \bmod 8$ and $\zeta_8^a + \zeta_8^{-a} = -\sqrt{2}$ if $a \equiv 3, 5 \bmod 8$ (note $\zeta_8^7 = \zeta_8^{-1}$ and $\zeta_8^5 = \zeta_8^{-3}$). Thus if $a \equiv 1, 7 \bmod 8$ we have $(-1)^b = 1$, so $b \equiv 0, 2 \bmod 4$, while if $a \equiv 3, 5 \bmod 8$ we have $(-1)^b = -1$, so $b \equiv 1, 3 \bmod 4$. For example, $\sigma$ can't both fix $\sqrt[4]{2}$ ($b = 0$) and send $\zeta_8$ to $\zeta_8^3$ ($a = 3$) because (1.4) would not hold.

The simplest way to understand $\mathbf{Q}(\sqrt[4]{2}, \zeta_8)$ is to use a different set of generators. Since $\zeta_8 = e^{2\pi i/8} = e^{\pi i/4} = (1 + i)/\sqrt{2}$,
$$\mathbf{Q}(\sqrt[4]{2}, \zeta_8) = \mathbf{Q}(\sqrt[4]{2}, i),$$
and from the second representation we know its Galois group over $\mathbf{Q}$ is isomorphic to $D_4$ with independent choices of where to send $\sqrt[4]{2}$ (to any fourth root of $2$) and $i$ (to any square root of $-1$) rather than $\sqrt[4]{2}$ and $\zeta_8$. A different choice of field generators can make it easier to see what the Galois group looks like. We also see immediately from the second representation that $[\mathbf{Q}(\sqrt[4]{2}, \zeta_8) : \mathbf{Q}] = 8$.

**Example 1.5.** Let's consider the splitting field of $X^8 - 2$ over $\mathbf{Q}$, which is $\mathbf{Q}(\sqrt[8]{2}, \zeta_8)$, where $\zeta_8 = e^{2\pi i/8} = (1 + i)/\sqrt{2}$. While $[\mathbf{Q}(\sqrt[8]{2}) : \mathbf{Q}] = 8$ and $[\mathbf{Q}(\zeta_8) : \mathbf{Q}] = 4$, we'll see that $[\mathbf{Q}(\sqrt[8]{2}, \zeta_8) : \mathbf{Q}]$ is $16$, not $32$, and determine $\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})$. It is a group of order $16$, but is not isomorphic to the dihedral group of order $16$.

What we do will build on the previous example, where $[\mathbf{Q}(\sqrt[4]{2}, \zeta_8) : \mathbf{Q}]$ is $8$, not $16$ (the product of $[\mathbf{Q}(\sqrt[4]{2}) : \mathbf{Q}]$ and $[\mathbf{Q}(\zeta_8) : \mathbf{Q}]$), since $\mathbf{Q}(\sqrt[4]{2})$ and $\mathbf{Q}(\zeta_8)$ are not "independent" over $\mathbf{Q}$: the fields both contain $\sqrt{2}$.

Since $\zeta_8 \notin \mathbf{Q}(\sqrt[8]{2})$ but $\zeta_8^2 - \sqrt{2}\zeta_8 + 1 = 0$ by the algebraic relation (1.3), the degree of $\zeta_8$ over $\mathbf{Q}(\sqrt[8]{2})$ is $2$. Thus $[\mathbf{Q}(\sqrt[8]{2}, \zeta_8) : \mathbf{Q}] = [\mathbf{Q}(\sqrt[8]{2}, \zeta_8) : \mathbf{Q}(\sqrt[8]{2})][\mathbf{Q}(\sqrt[8]{2}) : \mathbf{Q}] = 2 \cdot 8 = 16$, so $|\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})| = 16$.

Each $\sigma \in \mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})$ is determined by the values
$$\sigma(\zeta_8) = \zeta_8^a \quad (a \in (\mathbf{Z}/8\mathbf{Z})^\times) \quad \text{and} \quad \sigma(\sqrt[8]{2}) = \zeta_8^b \sqrt[8]{2} \quad (b \in \mathbf{Z}/8\mathbf{Z}). \tag{1.5}$$

<!-- page 5 -->

There is a condition linking $a$ and $b$, from (1.3):
$$\zeta_8^a + \zeta_8^{-a} = \sigma(\zeta_8 + \zeta_8^{-1}) = \sigma(\sqrt{2}) = \sigma(\sqrt[8]{2}^4) = \sigma(\sqrt[8]{2})^4 = (-1)^b\sqrt{2}. \tag{1.6}$$
(This is essentially the same as (1.4), excepts now $b$ comes from $\mathbf{Z}/8\mathbf{Z}$ instead of $\mathbf{Z}/4\mathbf{Z}$.) It follows from (1.6), by reasoning like that in the previous example, that if $a \equiv 1, 7 \bmod 8$ then $b$ is even and if $a \equiv 3, 5 \bmod 8$ then $b$ is odd. Therefore, since $b$ is in $\mathbf{Z}/8\mathbf{Z}$, there are at most $4$ values of $b$ allowed for each value of $a$. That means $\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})$ has order at most $16$. Since we earlier showed the Galois group has order $16$, the parity condition on $b$ for each $a$ is the only constraint: $\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})$ consists of the automorphisms described by (1.3) where (i) $b$ is even if $a \equiv 1, 7 \bmod 8$ and (ii) $b$ is odd if $a \equiv 3, 5 \bmod 8$.[^1]

Here is a field diagram, which is very far from showing all intermediate fields.

```
          Q(sqrt[8]{2}, zeta_8)
          /                  \
          2                  4
        /                      \
  Q(sqrt[8]{2})              Q(zeta_8)
        \                      /
          4                  2
            \              /
          Q(sqrt(2))      Q(i)
            \              /
              2          2
                \      /
                  Q
```

Each automorphism in $\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})$ can be written by (1.3) as $\sigma_{a,b}$ where $\sigma_{a,b}(\zeta_8) = \zeta_8^a$ and $\sigma_{a,b}(\sqrt[8]{2}) = \zeta_8^b \sqrt[8]{2}$. Two automorphisms $\sigma_{a,b}$ and $\sigma_{c,d}$ compose as follows:
$$\sigma_{a,b}(\sigma_{c,d}(\zeta_8)) = \sigma_{a,b}(\zeta_8^c) = \zeta_8^{ac},$$
$$\sigma_{a,b}(\sigma_{c,d}(\sqrt[8]{2})) = \sigma_{a,b}(\zeta_8^d \sqrt[8]{2}) = \sigma_{a,b}(\zeta_8)^d \sigma_{a,b}(\sqrt[8]{2}) = \zeta_8^{ad+b} \sqrt[8]{2}.$$
This is how matrices $\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$ multiply: $\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}\begin{pmatrix} c & d \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} ac & ad+b \\ 0 & 1 \end{pmatrix}$. Therefore $\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q})$ can be viewed as $2 \times 2$ mod $8$ matrices by
$$\sigma_{a,b} \mapsto \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$$
where $a \in (\mathbf{Z}/8\mathbf{Z})^\times$ and $b \in \mathbf{Z}/8\mathbf{Z}$ subject to the conditions

- $b$ is even if $a \equiv 1, 7 \bmod 8$,
- $b$ is odd if $a \equiv 3, 5 \bmod 8$.

This constraint on $b$ given $a$, or on $a$ given $b$, is important to remember, *e.g.*, the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is *not* in the Galois group: no $\sigma$ has the effect $\sigma(\zeta_8) = \zeta_8$ and $\sigma(\sqrt[8]{2}) = \zeta_8 \sqrt[8]{2}$!

What group of order $16$ is the Galois group? It is *not* isomorphic to the dihedral group of order $16$ since that dihedral group has $9$ elements of order $2$ (all $8$ reflections and the rotation $r^4$) while the Galois group has $5$ elements of order $2$: $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 7 & 0 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 7 & 2 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 7 & 4 \\ 0 & 1 \end{pmatrix}$, and $\begin{pmatrix} 7 & 6 \\ 0 & 1 \end{pmatrix}$. (The mod $8$ matrices $\begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 5 & 0 \\ 0 & 1 \end{pmatrix}$ have order $2$, but they are not in the Galois group since a matrix of the form $\begin{pmatrix} a & 0 \\ 0 & 1 \end{pmatrix}$ in the Galois group has $a \equiv 1, 7 \bmod 8$.)

The Galois group contains $\sigma := \begin{pmatrix} 5 & 1 \\ 0 & 1 \end{pmatrix}$, which has order $8$. Its successive powers are in the table below. An element of the Galois group with order $2$ that is not a power of $\sigma$ is

[^1]: A concise way of describing the two parity constraints on $b \bmod 8$ given $a \bmod 8$ is $b \equiv \frac{a^2 - 1}{8} \bmod 2$.

<!-- page 6 -->

$\tau := \begin{pmatrix} 7 & 0 \\ 0 & 1 \end{pmatrix}$. Since the Galois group has order $16$, it is $\langle \sigma, \tau \rangle$. By an explicit mod $8$ matrix calculation, $\tau\sigma\tau^{-1} = \tau\sigma\tau = \begin{pmatrix} 5 & 7 \\ 0 & 1 \end{pmatrix} = \sigma^3$.

| $k$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|
| $\sigma^k$ | $\begin{pmatrix} 5 & 1 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 5 & 7 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 5 & 5 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 5 & 3 \\ 0 & 1 \end{pmatrix}$ | $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ |

The group with two generators $x$ and $y$ where $x$ has order $8$, $y$ has order $2$, and $yxy^{-1} = x^3$ is called the *semidihedral group* of order $16$. You can look up information about it on the page [https://groupprops.subwiki.org/wiki/Semidihedral_group:SD16](https://groupprops.subwiki.org/wiki/Semidihedral_group:SD16). For example, that webpage says this group has $3$ subgroups of order $8$, so by Galois theory $\mathbf{Q}(\sqrt[8]{2}, \zeta_8)$ has $3$ quadratic fields. There are $3$ quadratic fields in $\mathbf{Q}(\zeta_8)$: $\mathbf{Q}(\sqrt{2})$, $\mathbf{Q}(i)$, and $\mathbf{Q}(i\sqrt{2})$. Thus these are all the quadratic fields of $\mathbf{Q}(\sqrt[8]{2}, \zeta_8)$.[^2] The webpage also says the $3$ subgroups of order $8$ are isomorphic to $\mathbf{Z}/8\mathbf{Z}$, $D_4$,[^3] and $Q_8$, so the Galois group has a subgroup isomorphic to each of these groups. For example, check $\sigma$ fixes $i = \zeta_8^4$, and since $\sigma$ has order $8$ we have
$$\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q}(i)) = \langle \sigma \rangle \cong \mathbf{Z}/8\mathbf{Z}.$$
By determining which elements of the Galois group fix $\sqrt{2} = \sqrt[8]{2}^4$ and $i\sqrt{2}$, it is left as an exercise to the reader to show
$$\mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q}(\sqrt{2})) \cong D_4, \quad \mathrm{Gal}(\mathbf{Q}(\sqrt[8]{2}, \zeta_8)/\mathbf{Q}(i\sqrt{2})) \cong Q_8.$$
This concludes our look at $\mathbf{Q}(\sqrt[8]{2}, \zeta_8)$ and its Galois group over $\mathbf{Q}$.

A Galois extension is said to have a given group-theoretic property (being abelian, non-abelian, cyclic, *etc.*) when its Galois group has that property.

**Example 1.6.** Any quadratic extension of $\mathbf{Q}$ is an abelian extension since its Galois group has order $2$. It is also a cyclic extension.

**Example 1.7.** The extension $\mathbf{Q}(\sqrt[3]{2}, \omega)/\mathbf{Q}$ is called non-abelian since its Galois group is isomorphic to $S_3$, which is a non-abelian group. The term "non-abelian" has nothing to do with the field operations, which of course are always commutative.

**Theorem 1.8.** *If $L/K$ is a finite abelian extension then every intermediate field is an abelian extension of $K$. If $L/K$ is cyclic then every intermediate field is cyclic over $K$.*

*Proof.* Every subgroup of an abelian group is a normal subgroup, so every field $F$ between $L$ and $K$ is Galois over $K$ and $\mathrm{Gal}(F/K) \cong \mathrm{Gal}(L/K)/\mathrm{Gal}(L/F)$. The quotient of an abelian group by any subgroup is abelian, so $\mathrm{Gal}(F/K)$ is abelian.

Since the quotient of a cyclic group by any subgroup is cyclic, if $L/K$ is cyclic then $F/K$ is cyclic too. $\square$

## 2. Applications to Field Theory

We will prove the complex numbers are algebraically closed (the "Fundamental Theorem of Algebra") using Galois theory and a small amount of analysis. We need one property of the real numbers, one property of the complex numbers, and two properties of finite groups:

(1) Every odd degree polynomial in $\mathbf{R}[X]$ has a real root. In particular, no polynomial of odd degree greater than $1$ in $\mathbf{R}[X]$ is irreducible.

[^2]: In fact those $3$ quadratic fields are the only quadratic fields in $\mathbf{Q}(\sqrt[2^k]{2}, \zeta_{2^k})$ for $k \geq 2$. This can be shown by methods of algebraic number theory without having to compute Galois groups.

[^3]: That webpage follows the group theorist's convention of writing the dihedral group of order $2n$ as $D_{2n}$ instead of $D_n$, so it writes $D_8$ instead of $D_4$.

<!-- page 7 -->

(2) Every number in $\mathbf{C}$ has square roots in $\mathbf{C}$.

(3) The first Sylow theorem (existence of Sylow subgroups).

(4) A nontrivial finite $p$-group has a subgroup of index $p$.

The first property is a consequence of the intermediate value theorem. The second property follows from writing a nonzero complex number as $re^{i\theta}$ and then its square roots are $\pm\sqrt{r}e^{i\theta/2}$. (For example, $i = e^{i\pi/2}$ and a square root of $i$ is $e^{i\pi/4} = \frac{1}{\sqrt{2}} + \frac{i}{\sqrt{2}}$.) It is a nice exercise to find a square root of $a + bi$ in terms of $a$ and $b$. The third property is proved as part of the Sylow theorems. The fourth property is often proved in the context of showing finite $p$-groups are solvable; this can be found in most group theory textbooks.

**Theorem 2.1.** *The complex numbers are algebraically closed.*

*Proof.* We need to show any irreducible in $\mathbf{C}[X]$ has degree $1$. If $\pi(X) \in \mathbf{C}[X]$ is irreducible and $\alpha$ is a root, then $[\mathbf{C}(\alpha) : \mathbf{C}] = \deg \pi$, so our task is the same as showing the only finite extension of $\mathbf{C}$ is $\mathbf{C}$ itself.

Let $E/\mathbf{C}$ be a finite extension. Since $E$ is a finite extension of $\mathbf{R}$, and we're in characteristic $0$, we can enlarge $E/\mathbf{R}$ to a finite Galois extension $K/\mathbf{R}$. Since $\mathbf{R} \subset \mathbf{C} \subset K$, $[K : \mathbf{R}]$ is even.

Let $2^m \geq 2$ be the highest power of $2$ dividing the size of $G = \mathrm{Gal}(K/\mathbf{R})$. There is a subgroup $H$ of $G$ with order $2^m$ (Property 3). Let $F$ be the corresponding fixed field, so $[F : \mathbf{R}]$ is odd.

```
K                {1}
|                |
2^m              2^m
|                |
F                H
|                |
odd              odd
|                |
C                Gal(K/C)
|                |
2                2
|                |
R                G
```

Every $\alpha \in F$ has degree over $\mathbf{R}$ dividing $[F : \mathbf{R}]$, so $[\mathbf{R}(\alpha) : \mathbf{R}]$ is odd. That means the minimal polynomial of $\alpha$ in $\mathbf{R}[X]$ has odd degree. Irreducible polynomials in $\mathbf{R}[X]$ of odd degree have degree $1$ (Property 1), so $[\mathbf{R}(\alpha) : \mathbf{R}] = 1$. Thus $\alpha \in \mathbf{R}$, so $F = \mathbf{R}$. Therefore $G = H$ is a $2$-group.

```
K                {1}
|                |
C                Gal(K/C)
|                |
2                2^{m-1}
|                |
R                G
```

The group $\mathrm{Gal}(K/\mathbf{C})$ has order $2^{m-1}$. If $m \geq 2$ then $\mathrm{Gal}(K/\mathbf{C})$ has a subgroup of index $2$ (Property 4), whose fixed field has degree $2$ over $\mathbf{C}$. Any quadratic extension of $\mathbf{C}$ has the form $\mathbf{C}(\sqrt{d})$ for some nonsquare $d \in \mathbf{C}^\times$. But every nonzero complex number has square

<!-- page 8 -->

roots in $\mathbf{C}$ (Property 2), so $[\mathbf{C}(\sqrt{d}) : \mathbf{C}]$ is $1$, not $2$. We have a contradiction. Thus $m = 1$, so $K = \mathbf{C}$. Since $\mathbf{C} \subset E \subset K$, we conclude that $E = \mathbf{C}$. $\square$

**Theorem 2.2.** *If $L/K$ be Galois with degree $p^m$, where $p$ is a prime, then there is a chain of intermediate fields*
$$K = F_0 \subset F_1 \subset F_2 \subset \cdots \subset F_m = K$$
*where $[F_i : F_{i-1}] = p$ for $i \geq 1$ and $F_i/K$ is Galois.*

*Proof.* The group $\mathrm{Gal}(L/K)$ is a finite group of order $p^m$. One of the consequences of finite $p$-groups being solvable is the existence of a rising chain of subgroups from the trivial subgroup to the whole group where each subgroup has index $p$ in the next one and each subgroup is *normal* in the whole group. Now apply the Galois correspondence. $\square$

The next application, which is an amusing technicality, is taken from [2, p. 67].

**Theorem 2.3.** *Let $p$ be a prime number. If $K$ is a field of characteristic $0$ such that every proper finite extension of $K$ has degree divisible by $p$ then every finite extension of $K$ has $p$-power degree.*

Aside from examples resembling $K = \mathbf{R}$ (where $p = 2$ works), fields that fit the conditions of Theorem 2.3 are not easy to describe at an elementary level. But the technique of proof is a pleasant use of elementary group theory.

*Proof.* Let $L/K$ be a finite extension. We want to show $[L : K]$ is a power of $p$. Since $K$ has characteristic $0$, $L/K$ is separable, so we can embed $L$ in a finite Galois extension $E/K$. Since $[L : K] \mid [E : K]$, it suffices to show $[E : K]$ is a power of $p$, *i.e.*, show finite Galois extensions of $K$ have $p$-power degree.

By the first Sylow theorem, $\mathrm{Gal}(E/K)$ contains a $p$-Sylow subgroup, say $H$. Let $F = E^H$, so $[F : K]$ is the index of $H$ in $\mathrm{Gal}(E/K)$. This index is prime to $p$ by the definition of a Sylow subgroup, so $[F : K]$ is prime to $p$.

```
E                {1}
|                |
|                power of p
|                |
F                H
|                |
|                prime to p
|                |
K                Gal(E/K)
```

Every proper finite extension of $K$ has degree divisible by $p$, so $[F : K] = 1$. Thus $F = K$ and $[E : K] = [E : F] = |H|$ is a power of $p$. $\square$

**Remark 2.4.** Theorem 2.3 is true when $K$ has positive characteristic, but then one has to consider the possibility that $K$ has inseparable extensions and additional reasoning is needed. See [2, p. 67].

## 3. Applications to Minimal Polynomials

When $L/K$ is a Galois extension and $\alpha \in L$, the Galois group $\mathrm{Gal}(L/K)$ provides us with a systematic way to describe all the roots of the minimal polynomial of $\alpha$ over $K$: they are the different elements of the Galois orbit $\{\sigma(\alpha) : \sigma \in \mathrm{Gal}(L/K)\}$. If we let $\mathrm{Gal}(L/K)$ act on $L[X]$, and not just $L$, by acting on polynomial coefficients, then we can relate minimal polynomials of the same number over different fields using a Galois group.

<!-- page 9 -->

**Theorem 3.1.** *Let $L/K$ be a finite Galois extension and $\alpha$ lie in some extension of $L$ with minimal polynomial $f(X)$ in $L[X]$. The minimal polynomial of $\alpha$ in $K[X]$ is the product of all the different values of $(\sigma f)(X)$ as $\sigma$ runs over $\mathrm{Gal}(L/K)$.*

When $\alpha \in L$, so $f(X) = X - \alpha$, we recover the construction of the minimal polynomial of $\alpha$ in $K[X]$ as $\prod_{j=1}^r (X - \sigma_j(\alpha))$, where $\sigma_1(\alpha), \ldots, \sigma_r(\alpha)$ are the distinct values of $\sigma(\alpha)$ as $\sigma$ runs over $\mathrm{Gal}(L/K)$.

*Proof.* Let $\pi(X)$ denote the minimal polynomial of $\alpha$ over $K$. Since $\pi(\alpha) = 0$ and $f(X)$ is the minimal polynomial of $\alpha$ over $L$, $f(X) \mid \pi(X)$ in $L[X]$. For any $\sigma \in \mathrm{Gal}(L/K)$, $f(X) \mid \pi(X) \Rightarrow (\sigma f)(X) \mid \pi(X)$ because $(\sigma\pi)(X) = \pi(X)$.

Note $(\sigma f)(X) = (\sigma_i f)(X)$ for some $i$. Each $\sigma_i f$ is monic irreducible in $L[X]$ and therefore $\sigma_i f$ and $\sigma_j f$ are relatively prime when $i \neq j$. Thus $\pi(X)$ is divisible by $F(X) := \prod_{i=1}^r (\sigma_i f)(X)$. For any $\sigma \in \mathrm{Gal}(L/K)$, the set of polynomials $(\sigma\sigma_i f)(X)$ are the same as all $(\sigma_i f)(X)$ except it may be in a different order, so
$$(\sigma F)(X) = \prod_{i=1}^r (\sigma\sigma_i f)(X) = \prod_{i=1}^r (\sigma_i f)(X) = F(X),$$
so the coefficients of $F(X)$ are in $K$. Since $F(X) \mid \pi(X)$ and $F(\alpha) = 0$, the meaning of minimal polynomial implies $F(X) = \pi(X)$. $\square$

**Example 3.2.** Consider $X^2 - \sqrt{2}$ in $\mathbf{Q}(\sqrt{2})[X]$. It is irreducible since $\sqrt{2}$ is not a square in $\mathbf{Q}(\sqrt{2})$: if $(a + b\sqrt{2})^2 = \sqrt{2}$ with $a, b \in \mathbf{Q}$ then $a^2 + 2b^2 = 0$, so $a = b = 0$, a contradiction. The different values of $\sigma(X^2 - \sqrt{2}) = X^2 - \sigma(\sqrt{2})$ as $\sigma$ runs over $\mathrm{Gal}(\mathbf{Q}(\sqrt{2})/\mathbf{Q})$ are $X^2 - \sqrt{2}$ and $X^2 + \sqrt{2}$, so the minimal polynomial over $\mathbf{Q}$ of the roots of $X^2 - \sqrt{2}$ is
$$(X^2 - \sqrt{2})(X^2 + \sqrt{2}) = X^4 - 2.$$

Since a minimal polynomial over a field is just an irreducible polynomial over that field (with a particular root), we can formulate Theorem 3.1 in terms of irreducible polynomials without mentioning roots: if $f(X)$ is monic irreducible in $L[X]$ then the product of the different $(\sigma f)(X)$, as $\sigma$ runs over $\mathrm{Gal}(L/K)$, is irreducible in $K[X]$. Consider a potential converse: if $f(X)$ is monic in $L[X]$ and the product of the different polynomials $(\sigma f)(X)$, as $\sigma$ runs over $\mathrm{Gal}(L/K)$, is irreducible in $K[X]$, then $f(X)$ is irreducible in $L[X]$. This is *false*: use $L/K = \mathbf{Q}(\sqrt{2})/\mathbf{Q}$ and $f(X) = X^2 - 2$. Here $(\sigma f)(X) = X^2 - 2$ for either $\sigma$, so the product of different $(\sigma f)(X)$ is $X^2 - 2$, which is irreducible in $K[X]$ but reducible in $L[X]$. Yet there is a kernel of truth in this false converse. We just have to make sure the coefficients of $f(X)$ don't all lie in an extension of $K$ that is smaller than $L$.

**Theorem 3.3.** *Let $L/K$ be a finite Galois extension. Suppose $f(X)$ is monic in $L[X]$ and its coefficients generate $L$ over $K$. If the product of the different polynomials $(\sigma f)(X)$, as $\sigma$ runs over $\mathrm{Gal}(L/K)$, is irreducible in $K[X]$, then $f(X)$ is irreducible in $L[X]$.*

This avoids the previous counterexample $f(X) = X^2 - 2$ with $L/K = \mathbf{Q}(\sqrt{2})/\mathbf{Q}$, since the coefficients of $f(X)$ do not generate $\mathbf{Q}(\sqrt{2})/\mathbf{Q}$.

*Proof.* Since the coefficients of $f(X)$ generate $L/K$ any $\sigma$ in $\mathrm{Gal}(L/K)$ that is not the identity changes at least one of the coefficients of $f(X)$. (Otherwise the coefficients lie in the field fixed by $\sigma$, which is a nontrivial subgroup of $\mathrm{Gal}(L/K)$ and a nontrivial subgroup has a fixed field smaller than $L$.) It follows that for any distinct $\sigma$ and $\tau$ in $\mathrm{Gal}(L/K)$, the

<!-- page 10 -->

polynomials $(\sigma f)(X)$ and $(\tau f)(X)$ are different: if $\sigma f = \tau f$ then $(\tau^{-1}\sigma)f = f$, so $\tau^{-1}\sigma$ fixes the coefficients of $f$ and therefore $\sigma = \tau$. Thus the hypothesis of the theorem is that
$$F(X) := \prod_{\sigma \in \mathrm{Gal}(L/K)} (\sigma f)(X)$$
is irreducible in $K[X]$, where the product runs over *all* of $\mathrm{Gal}(L/K)$, and we want to show $f(X)$ is irreducible in $L[X]$. We will prove the contrapositive. Suppose $f(X)$ is reducible in $L[X]$, so $f(X) = g(X)h(X)$ in $L[X]$ where $g(X)$ and $h(X)$ are nonconstant. Then
$$F(X) = \prod_{\sigma \in \mathrm{Gal}(L/K)} (\sigma f)(X) = \prod_{\sigma \in \mathrm{Gal}(L/K)} (\sigma g)(X) \prod_{\sigma \in \mathrm{Gal}(L/K)} (\sigma h)(X) = G(X)H(X),$$
where $G(X)$ and $H(X)$ are in $K[X]$ (why?). Since $g(X)$ and $h(X)$ have positive degree, so do $G(X)$ and $H(X)$, and therefore $F(X)$ is reducible in $K[X]$. $\square$

**Example 3.4.** Consider $X^n - \sqrt{2}$ in $\mathbf{Q}(\sqrt{2})[X]$. Its coefficients generate $\mathbf{Q}(\sqrt{2})/\mathbf{Q}$. Since
$$(X^n - \sqrt{2})(X^n + \sqrt{2}) = X^{2n} - 2$$
is irreducible over $\mathbf{Q}$, $X^n - \sqrt{2}$ is irreducible in $\mathbf{Q}(\sqrt{2})[X]$ for all $n$. The same kind of argument shows $X^n - (1 + 2\sqrt{2})$ is irreducible over $\mathbf{Q}(\sqrt{2})[X]$ for all $n$.

**Corollary 3.5.** *Let $L/K$ be a finite Galois extension. Suppose $f(X)$ is monic in $L[X]$, its coefficients generate $L/K$, and $F(X) := \prod_{\sigma \in \mathrm{Gal}(L/K)} (\sigma f)(X)$ is separable and irreducible in $K[X]$. Then each $(\sigma f)(X)$ is irreducible in $L[X]$ and if $\alpha$ is a root of $f(X)$ then the Galois closure of $L(\alpha)/K$ is the splitting field of $F(X)$ over $K$.*

*Proof.* The irreducibility of $f(X)$ in $L[X]$ follows from Theorem 3.3. The polynomials $(\sigma f)(X)$ satisfy the same hypotheses as $f(X)$, so they are all irreducible over $L$ as well. The minimal polynomial of $\alpha$ over $K$ is $F(X)$ and $K(\alpha)/K$ is separable since $F(X)$ is separable over $K$. Therefore $L(\alpha)/K$ is separable, so $L(\alpha)$ has a Galois closure over $K$.

A Galois extension of $K$ that contains $L(\alpha)$ must contain all the $K$-conjugates of $\alpha$ and hence must contain the splitting field of $F(X)$ over $K$. Conversely, the splitting field of $F(X)$ over $K$ is a Galois extension of $K$ that contains $\alpha$ as well as all the roots of $f(X)$, so the extension contains the coefficients of $f(X)$. Those coefficients generate $L/K$, so the splitting field of $F(X)$ over $K$ contains $L(\alpha)$. $\square$

There is nothing deep going on in this corollary. The point is that since the coefficients of $f$ generate $L$, $L$ is already inside the Galois closure of $K(\alpha)/K$, so just by forming the splitting field of $F(X)$ over $K$ we pick up $L$ inside it.

**Example 3.6.** Consider the extension $\mathbf{Q}(\gamma)/\mathbf{Q}$, where $\gamma$ is a root of $X^3 - 3X - 1$. This cubic extension is Galois and the $\mathbf{Q}$-conjugates of $\gamma$ are $2 - \gamma^2$ and $\gamma^2 - \gamma - 2$. Let $f(X) = X^3 - \gamma X - 1$. The polynomials $(\sigma f)(X)$ as $\sigma$ runs over the three elements of $\mathrm{Gal}(\mathbf{Q}(\gamma)/\mathbf{Q})$ are $f(X)$, $X^3 - (2 - \gamma^2)X - 1$, and $X^3 - (\gamma^2 - \gamma - 2)X - 1$. Their product is
$$F(X) = X^9 - 3X^6 - 3X^5 + 2X^3 + 3X^2 - 1,$$
which is irreducible mod $2$ and thus is irreducible in $\mathbf{Q}[X]$. Therefore the polynomials $f(X)$, $X^3 - (2 - \gamma^2)X - 1$, and $X^3 - (\gamma^2 - \gamma - 2)X - 1$ are all irreducible over $\mathbf{Q}(\gamma)[X]$ and the splitting field of $F(X)$ over $\mathbf{Q}$ is the smallest Galois extension of $\mathbf{Q}$ containing $\mathbf{Q}(\gamma, \alpha)$, where $\alpha$ is a root of $f(X)$. According to PARI, the splitting field of $F(X)$ over $\mathbf{Q}$ has degree $684 = 3 \cdot 6^3$.

<!-- page 11 -->

## 4. What Next?

There are two important aspects of field extensions that are missing in a study of Galois theory of finite extensions, and we briefly address them: Galois theory for infinite algebraic extensions and transcendental extensions.

An algebraic extension $L/K$ of infinite degree is called Galois when it is separable and normal. This means each element of $L$ is the root of a separable irreducible in $K[X]$ and each reducible in $K[X]$ with a root in $L$ splits completely over $L$. One infinite Galois extension of $\mathbf{Q}$ is $\mathbf{Q}(\mu_{p^\infty}) = \bigcup_{n \geq 1} \mathbf{Q}(\mu_{p^n})$, the union of all $p$-th power cyclotomic extensions of $\mathbf{Q}$, where $p$ is a prime. Even if an algebraic extension $L/K$ is infinite, any particular element (or finite set of elements) in $L$ is in a finite subextension of $K$, so knowledge of finite extensions helps us understand infinite algebraic extensions. In fact, another way of describing an infinite Galois extension is that it is a composite of finite Galois extensions.

For an infinite Galois extension $L/K$, its Galois group $\mathrm{Gal}(L/K)$ is still defined as the group of $K$-automorphisms of $L$, and we can associate a subgroup of the Galois group to each intermediate field and an intermediate field to each subgroup of the Galois group just as in the finite case. However, this correspondence is no longer a bijection! This was first discovered by Dedekind, who saw in examples that different subgroups of an infinite Galois group could have the same fixed field. So it looks like Galois theory for infinite extensions breaks down. But it isn't really so. Krull realized that if you put a suitable topology on the Galois group then a bijection can be given between all intermediate fields and the *closed* subgroups in that topology. (See [1] and [3].) Every subgroup of the Galois group is associated to the same field as the closure of the subgroup in the Krull topology, which explains Dedekind's examples of different subgroups with the same fixed field: one subgroup is the closure of the other. The Krull topology on Galois groups not only rescued Galois theory for infinite extensions, but it gave a new impetus to the study of topological groups. To understand infinite Galois theory, first learn about the $p$-adic numbers and their topological and algebraic structure, as they are used in the simplest examples of interesting infinite Galois groups, such as $\mathrm{Gal}(\mathbf{Q}(\mu_{p^\infty})/\mathbf{Q})$. Lectures on infinite Galois theory are [here](https://kconrad.math.uconn.edu/blurbs/galoistheory/infinitegalois.pdf).

Turning away from Galois extensions, the next most important class of field extensions are transcendental extensions. These are field extensions in which some element of the top field is transcendental (that is, not algebraic) over the bottom field. The simplest example of a transcendental extension of a field $F$ is the field $F(T)$ of rational functions over $F$ in an indeterminate $T$, or more generally the field $F(T_1, \ldots, T_n)$ of rational functions in $n$ independent variables over $F$. This is called a pure transcendental extension. A general transcendental extension is a mixture of algebraic and transcendental parts, such as $F(x, y)$ where $x$ is transcendental over $F$ and $y^2 = x^3 - 1$.

Since transcendental extensions of $F$ have infinite degree, the notion of field degree is no longer important. In its place is the concept of *transcendence degree*, which is a nonlinear analogue of a basis and measures how transcendental the extension is. The need to understand transcendental field extensions is not driven for its own sake, but for other areas of mathematics, such as algebraic geometry.

## References

[1] J. Bastida, "Field extensions and Galois theory," Addison-Wesley, Reading, MA 1984.

[2] I. Kaplansky, "Fields and Rings," 2nd ed., Univ. of Chicago Press, Chicago, 1972.

[3] P. Morandi, "Field and Galois theory," Springer-Verlag, New York, 1996.
