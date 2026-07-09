# Pythagorean Descent

> **Source**: https://kconrad.math.uconn.edu/blurbs/descentPythag.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory

<!-- page 1 -->

## 1. Introduction

A Pythagorean triple is a triple of positive integers $(a, b, c)$ such that $a^2 + b^2 = c^2$. Examples include $(3, 4, 5)$, $(5, 12, 13)$, and $(6, 8, 10)$. A Pythagorean triple is called primitive if $a$, $b$, and $c$ have no common factor greater than 1. For example, $(3, 4, 5)$ and $(5, 12, 13)$ are primitive while $(6, 8, 10)$ is not. In any primitive Pythagorean triple one of $a$ and $b$ is odd and the other is even: if $a$ and $b$ were both even then $c$ would be even, violating primitivity, and if $a$ and $b$ were both odd then $c^2 = a^2 + b^2 \equiv 1 + 1 \equiv 2 \bmod 4$, which has no solution. Since the roles of $a$ and $b$ are symmetric, we will assume throughout that $b$ *is even*.

In 1934, Berggren [3] showed every primitive Pythagorean triple $(a, b, c)$ with $b$ even can be generated from the triple $(3, 4, 5)$ by a 3-fold ascent using the three matrices

$$\begin{pmatrix} 1 & -2 & 2 \\ 2 & -1 & 2 \\ 2 & -2 & 3 \end{pmatrix}, \quad \begin{pmatrix} -1 & 2 & 2 \\ -2 & 1 & 2 \\ -2 & 2 & 3 \end{pmatrix}, \quad \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 3 \end{pmatrix}. \tag{1.1}$$

Labeling the matrices in (1.1) as $A$, $B$, and $C$, respectively, the start of the ascent to new primitive triples is illustrated in the diagram below, where the branches coming out of each node from left to right are obtained by applying $A$, then $B$, then $C$.

```
                                    A --- (7,24,25)
                                   /
                    (5,12,13) --- B --- (45,28,53)
                   /             \
                  /               C --- (55,48,73)
                 /
                A
               /
              /
             /                   A --- (33,56,65)
            /                   /
(3,4,5) --- B --- (15,8,17) --- B --- (35,12,37)
            \                   \
             \                   C --- (65,72,97)
              \
               C
                \
                 \                   A --- (39,80,89)
                  \                 /
                   (21,20,29) --- B --- (77,36,85)
                                 \
                                  C --- (119,120,169)
```

Berggren discovered the matrices in (1.1) algebraically, as follows. Suppose $(a, b, c)$ is a solution to $x^2 + y^2 = z^2$. He sought a nonzero $k$ that makes $(a+k, b+k, c+k)$ another solution

<!-- page 2 -->

to this equation. From the two conditions $a^2 + b^2 = c^2$ and $(a+k)^2 + (b+k)^2 = (c+k)^2$, we must have $k = 2(c - a - b)$ (so $k < 0$ if $a$, $b$, and $c$ are positive), and therefore

$$\begin{pmatrix} a+k \\ b+k \\ c+k \end{pmatrix} = \begin{pmatrix} -a - 2b + 2c \\ -2a - b + 2c \\ -2a - 2b + 3c \end{pmatrix} = \begin{pmatrix} -1 & -2 & 2 \\ -2 & -1 & 2 \\ -2 & -2 & 3 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix}. \tag{1.2}$$

The triples $(-a, b, c)$, $(a, -b, c)$, and $(-a, -b, c)$ also satisfy $x^2 + y^2 = z^2$, and if a nonzero $k$ is added to each coordinate of these in order to get another solution of $x^2 + y^2 = z^2$, the new triple in each case is a linear transformation of $(a, b, c)$ by the matrices in (1.1). These three matrices were rediscovered later by Barning [2, p. 3] and Hall [4, p. 377], based on the same motivation as Berggren. They are also in an exercise with solution in [6, pp. 84-85].

We will describe Berggren's tree of Pythagorean triples geometrically, using reflections for the orthogonal group of $x^2 + y^2 - z^2$. Each step of Berggren's tree will be broken up into 2 or 3 steps, each one involving a single reflection.

I thank Gabe Feinberg, Harold Erazo, and Pria Louka for comments and corrections.

## 2. Review of Reflections

In $\mathbf{R}^3$ we want to work out a formula for reflecting across a plane through the origin. To each plane through the origin there is a unique orthogonal line through the origin. We'll describe how to reflect across the plane by using a vector on its orthogonal line.

**Theorem 2.1.** *For any nonzero vector $w \in \mathbf{R}^3$ let $s_w \colon \mathbf{R}^3 \to \mathbf{R}^3$ be the reflection across the plane through the origin orthogonal to $w$. Then for all $v \in \mathbf{R}^3$,*

$$s_w(v) = v - 2\frac{v \cdot w}{\|w\|^2}w = v - 2\frac{v \cdot w}{w \cdot w}w. \tag{2.1}$$

*Proof.* The reflection $s_w$ should be linear, fix the plane through the origin orthogonal to $w$, and negate vectors on the line through $w$. Writing any $v \in \mathbf{R}^3$ as $aw + u$, with $a \in \mathbf{R}$ and $u \perp w$, we need

$$s_w(v) = s_w(aw) + s_w(u) = -aw + u = aw + u - 2aw = v - 2aw.$$

Since $v \cdot w = (aw + u) \cdot w = a(w \cdot w)$, we can solve for $a$ and obtain (2.1). $\square$

The formula for $s_w$ in (2.1) is written entirely in terms of the dot product, which is closely related to the quadratic form $x^2 + y^2 + z^2 = (x, y, z) \cdot (x, y, z)$ that provides $\mathbf{R}^3$ with its usual notion of length. For a more general quadratic form $Q(x, y, z) = ax^2 + by^2 + cz^2$ with all nonzero coefficients[^1] that might have negative values, we define its associated bilinear form to be $\langle v, w \rangle = \frac{1}{2}(Q(v + w) - Q(v) - Q(w))$ (when $Q$ is the sum of squares, this bilinear form is the dot product). Explicitly, if $v = (x_1, y_1, z_1)$ and $w = (x_2, y_2, z_2)$ then $\langle v, w \rangle = ax_1 x_2 + by_1 y_2 + cz_1 z_2$. Using this bilinear form in place of the dot product, we can promote (2.1) into a definition of reflections associated to $Q$: for each $w \in \mathbf{R}^3$ such that $Q(w) \neq 0$,[^2] define $s_w \colon \mathbf{R}^3 \to \mathbf{R}^3$ by the formula

$$s_w(v) = v - 2\frac{\langle v, w \rangle}{\langle w, w \rangle}w. \tag{2.2}$$

[^1]: More generally, any nondegenerate quadratic form on $\mathbf{R}^3$ can be brought into the diagonal shape $ax^2 + by^2 + cz^2$ with all nonzero coefficients by some linear change of variables.
[^2]: If $Q$ is indefinite, meaning it has coefficients of both signs, then some nonzero $w$ can have $Q(w) = 0$. For instance, if $Q(x, y, z) = x^2 + y^2 - z^2$ then $Q(1, 1, 0) = 0$.

<!-- page 3 -->

Here are some of properties of $s_w$:

- $s_w \colon \mathbf{R}^3 \to \mathbf{R}^3$ is linear,
- $s_w(w) = -w$ and $s_w(v) = v$ if $\langle v, w \rangle = 0$,
- $Q(s_w(v)) = Q(v)$ for all $v$,
- $s_w(s_w(v)) = v$ for all $v$.

The first and second properties generalize properties of ordinary reflections, while the third property is analogous to the length-preserving property of ordinary reflections. The third property also tells us that if $Q(v) = 0$ then $Q(s_w(v)) = 0$ as well, which is only interesting when $Q$ is indefinite, and this is going to be exactly the type of quadratic form we work with later. The fourth property makes inverting $s_w$ easy: it is its own inverse.

The *orthogonal group* of $Q$, denoted $\mathrm{O}_Q(\mathbf{R})$, is the set of all linear transformations $A \colon \mathbf{R}^3 \to \mathbf{R}^3$ preserved by $Q$: $Q(Av) = Q(v)$ for all $v \in \mathbf{R}^3$. For instance, when $Q(w) \neq 0$ the map $s_w$ in (2.2) belongs to the group $\mathrm{O}_Q(\mathbf{R})$. The Cartan-Dieudonne theorem says that every element of $\mathrm{O}_Q(\mathbf{R})$ is a product of at most 3 reflections.[^3]

## 3. The Orthogonal Group of $x^2 + y^2 - z^2$.

We return to the Pythagorean equation $a^2 + b^2 = c^2$. Writing it as $a^2 + b^2 - c^2 = 0$, we are inspired to think about the quadratic form $Q(x, y, z) = x^2 + y^2 - z^2$ and its orthogonal group $\mathrm{O}_Q(\mathbf{R})$. Barning [2] and Berggren [3] both observed that the matrices in (1.1) preserve $Q$, but they didn't say anything about them being reflections for $Q$.

We will use the reflections in $\mathrm{O}_Q(\mathbf{R})$ associated to the five vectors $e_1 = (1, 0, 0)$, $e_2 = (0, 1, 0)$, $e_3 = (0, 0, 1)$, $e_1 + e_2 = (1, 1, 0)$, and $e_1 + e_2 + e_3 = (1, 1, 1)$, and denote them by $s_1$, $s_2$, $s_3$, $s_{12}$, and $s_{123}$. The first three reflections are sign changes in coordinates:

$$s_1(x, y, z) = (-x, y, z), \quad s_2(x, y, z) = (x, -y, z), \quad s_3(x, y, z) = (x, y, -z). \tag{3.1}$$

For example, $(x, -y, -z) = s_3(s_2(x, y, z)) = s_2(s_3(x, y, z))$. The reflection associated to $(1, 1, 0)$ is

$$s_{12}(x, y, z) = (x, y, z) - (x + y)(1, 1, 0) = (-y, -x, z). \tag{3.2}$$

The reflection associated to $(1, 1, 1)$ is

$$\begin{aligned}
s_{123}(x, y, z) &= (x, y, z) - 2(x + y - z)(1, 1, 1) \\
&= (-x - 2y + 2z, -2x - y + 2z, -2x - 2y + 3z), \tag{3.3}
\end{aligned}$$

so the matrix for $s_{123}$ is[^4]

$$\begin{pmatrix} -1 & -2 & 2 \\ -2 & -1 & 2 \\ -2 & -2 & 3 \end{pmatrix}, \tag{3.4}$$

which is Berggren's matrix in (1.2). The matrices in (1.1) are

$$A = s_{123}s_1, \quad B = s_{123}s_2, \quad C = s_{123}s_1 s_2, \tag{3.5}$$

[^3]: Cartan showed each orthogonal transformation of $\mathbf{R}^n$ with respect to the standard quadratic form $x_1^2 + \cdots + x_n^2$ is a product of at most $n$ reflections in $\mathbf{R}^n$ if $n \geq 2$. See Theorem A.4 and the paragraph following it in https://kconrad.math.uconn.edu/blurbs/grouptheory/isometryRn.pdf. Dieudonne generalized this to other quadratic forms.
[^4]: Our matrix actions are all from the left, not right, so although we write vectors in coordinates as row vectors, like $(x, y, z)$, they need to be treated as *column* vectors when acted on by matrices.

<!-- page 4 -->

respectively.[^5] This can be checked by a direct calculation, and it also follows from how Berggren found the matrices in (1.1) by carrying out his algebraic idea with (3.4) on $(-a, b, c)$, $(a, -b, c)$, and $(-a, -b, c)$. Since reflections are their own inverse, $A^{-1} = s_1 s_{123}$, $B^{-1} = s_2 s_{123}$, and $C = s_2 s_1 s_{123}$.

The $(a, b, c) \in \mathbf{Z}^3$ such that $a^2 + b^2 = c^2$, allowing nonpositive coordinates, are the null vectors of $Q$ in $\mathbf{Z}^3$. A vector $(a, b, c) \in \mathbf{Z}^3$ is called primitive when its coordinates have gcd 1, so $(3, 4, 5)$ and $(3, -4, -5)$ are primitive null vectors of $Q$. Each element of $\mathrm{O}_Q(\mathbf{Z})$ preserves primitivity of an integral vector (more generally, it preserves the gcd of the coordinates of an integral vector) since the inverse of a matrix in $\mathrm{O}_Q(\mathbf{Z})$ is an integral matrix.

**Theorem 3.1.** *Let $Q(x, y, z) = x^2 + y^2 - z^2$. The group $\mathrm{O}_Q(\mathbf{Z})$ acts transitively on the primitive null vectors of $Q$ in $\mathbf{Z}^3$.*

*Proof.* We will prove this by descent, using reflections in $\mathrm{O}_Q(\mathbf{Z})$ to decrease the overall size of the coordinates of a vector.

Choose an integral vector $(a, b, c)$ such that $a^2 + b^2 = c^2$ and $(a, b, c) \neq (0, 0, 0)$. This vector may have some negative coordinates, and by applying $s_1$, $s_2$, or $s_3$ to $(a, b, c)$ we can make sign changes so that all the coordinates are nonnegative. Then from the condition $a^2 + b^2 = c^2$ we have $0 \leq a, b \leq c$.

Assume neither $a$ nor $b$ is 0, so both are positive. Then

$$0 < a < c, \quad 0 < b < c, \quad 0 < c < a + b, \tag{3.6}$$

where the last inequality comes from $c^2 = a^2 + b^2 < a^2 + 2ab + b^2 = (a + b)^2$.

Let's pass from $(a, b, c)$ to $s_{123}(a, b, c)$ using (3.4). The coordinates of this reflection satisfy

$$-a < -a - 2b + 2c < a, \quad -b < -2a - b + 2c < b, \quad -c < -2a - 2b + 3c < c, \tag{3.7}$$

since each of these inequalities is equivalent to one of the inequalities in (3.6) except for $-c < -2a - 2b + 3c$, which is equivalent to $a + b < 2c$ and that is immediate from $a < c$ and $b < c$ in (3.6).

By (3.7), the coordinates of $s_{123}(a, b, c)$ are, in absolute value, less than the corresponding coordinates of $(a, b, c)$. Apply the reflections $s_i$ to make the new coordinates all nonnegative and then, if neither of the first two coordinates is 0, use the reflection $s_{123}$ once again to shrink the absolute value of the coordinates further. Eventually we must reach an integral null vector for $Q$ with one of the first two coordinates being 0. That means it has the form $(a, 0, \pm a)$ or $(0, b, \pm b)$. If we had started off with a primitive null vector then every null vector we produce using reflections is primitive too, so the final primitive null vector with first or second coordinate 0 is one of the following:

$$(1, 0, 1), \; (1, 0, -1), \; (-1, 0, 1), \; (-1, 0, -1), \; (0, 1, 1), \; (0, 1, -1), \; (0, -1, 1), \; (0, -1, -1).$$

Using the reflections $s_1$, $s_2$, and $s_3$, which create sign changes, all of these vectors can be reached from $(1, 0, 1)$ or $(0, 1, 1)$, and we can pass from $(1, 0, 1)$ to $(0, 1, 1)$ using $s_2 s_{12}$ (the general effect of $s_{12}$ is in (3.2)), so the primitive integral null vectors for $Q$ are all in the same orbit of $\mathrm{O}_Q(\mathbf{Z})$. In particular, applying elements of $\mathrm{O}_Q(\mathbf{Z})$ to the primitive triple $(3, 4, 5)$ will lead to every primitive Pythagorean triple. $\square$

**Example 3.2.** *Let $v = (9, 40, 41)$, which is a primitive Pythagorean triple.*

**Step 1:** $s_{123}(v) = (-7, 24, 25)$, so we pass to $s_1 s_{123}(v) = (7, 24, 25)$.

[^5]: We can also write $C$ as $s_{123}s_2 s_1$ since $s_1$ and $s_2$ commute.

<!-- page 5 -->

**Step 2:** $s_{123}(7, 24, 25) = (-5, 12, 13)$, so we pass to $s_1 s_{123}(7, 24, 25) = (5, 12, 13)$.

**Step 3:** $s_{123}(5, 12, 13) = (-3, 4, 5)$, so we pass to $s_1 s_{123}(5, 12, 13) = (3, 4, 5)$.

Since $A = s_{123}s_1$ by (3.5) and reflections are their own inverse, $A^{-1} = s_1 s_{123}$. Thus

$$(3, 4, 5) = A^{-1}(5, 12, 13) = A^{-2}(7, 24, 25) = A^{-3}(9, 40, 41),$$

so

$$(9, 40, 41) = A^3(3, 4, 5),$$

where $A$ is the first matrix in (1.1). The appearance of $A^3$ here means that if we extend Berggren's tree on the first page one more step then we'd see $(9, 40, 41)$ at the top of the next column.

**Example 3.3.** *Let $v = (65, 72, 97)$, which is a primitive Pythagorean triple.*

**Step 1:** $s_{123}(v) = (-15, -8, 17)$, so $s_1 s_2 s_{123}(v) = (15, 8, 17)$.

**Step 2:** $s_{123}(15, 8, 17) = (3, -4, 5)$, so $s_2 s_{123}(15, 8, 17) = (3, 4, 5)$.

Thus $(3, 4, 5) = (s_2 s_{123})(s_1 s_2 s_{123})(65, 72, 97) = B^{-1}C^{-1}(65, 72, 97)$, so

$$(65, 72, 97) = CB(3, 4, 5),$$

and this is consistent with the location of $(65, 72, 97)$ in the tree on the first page.

Here is a proof that Berggren's tree has every primitive Pythagorean triple exactly once.

**Corollary 3.4 (Berggren).** *Each primitive Pythagorean triple $(a, b, c)$ with even $b$ is obtained from $(3, 4, 5)$ by applying to it a product of matrices $g_1 g_2 \cdots g_m$ where each $g_i$ is $A$, $B$, or $C$ in (1.1), and this product is unique[^6]: if*

$$g_1 g_2 \cdots g_m (3, 4, 5) = g_1' g_2' \cdots g_n'(3, 4, 5),$$

*where $g_i, g_j' \in \{A, B, C\}$ then $m = n$ and $g_i = g_i'$ for all $i$.*

*Proof.* From the *proof* of Theorem 3.1, a primitive Pythagorean triple $(a, b, c)$ can be brought down to $(1, 0, 1)$ or $(0, 1, 1)$ using only $s_1$, $s_2$, and $s_{123}$ provided that for positive $a, b, c$ the triple $s_{123}(a, b, c)$ has a positive third coordinate, since it makes applying $s_3$ unnecessary. Showing $s_{123}(a, b, c)$ has a positive third coordinate is equivalent to showing

$$3c \stackrel{?}{>} 2a + 2b.$$

If we square both sides and use $c^2 = a^2 + b^2$, this inequality is the same as

$$9c^2 > 4(a + b)^2 \iff 9(a^2 + b^2) > 4(a^2 + b^2 + 2ab) \iff a^2 + b^2 > \frac{8}{5}ab \iff \frac{a}{b} + \frac{b}{a} > \frac{8}{5}.$$

By calculus, $t + 1/t \geq 2$ for $t > 0$, and $2 > 8/5$, so $3c > 2a + 2b$ in any Pythagorean triple $(a, b, c)$.

In contrast to the third coordinate of $s_{123}(a, b, c)$ being positive when $a$, $b$, and $c$ are positive, we will show one of the first two coordinates of $s_{123}(a, b, c)$ is negative. (For example, look at the effect of $s_{123}$ in each step of Examples 3.2 and 3.3.) Assume, to the contrary, that the first two coordinates of $s_{123}(a, b, c)$ are both nonnegative. By the formula for $s_{123}$ in (3.3), $-a - 2b + 2c \geq 0$ and $-2a - b + 2c \geq 0$, which can be rewritten as

$$a + 2b \leq 2c, \quad 2a + b \leq 2c.$$

Since $a$, $b$, and $c$ are positive, squaring each of these inequalities implies

$$a^2 + 4ab + 4b^2 \leq 4c^2, \quad 4a^2 + 4ab + b^2 \leq 4c^2.$$

[^6]: To get $(3, 4, 5)$ itself we apply the empty product with $m = 0$.

<!-- page 6 -->

Since $c^2 = a^2 + b^2$, we get

$$4ab \leq 3a^2, \quad 4ab \leq 3b^2,$$

so $4b \leq 3a$ and $4a \leq 3b$. Adding these, $4(a + b) \leq 3(a + b)$, which is false since $a + b > 0$.

Since $s_1$, $s_2$, and $s_{123}$ don't change the parity of the middle coordinate, if $b$ is even then $(a, b, c)$ is eventually brought down to $(1, 0, 1)$, not $(0, 1, 1)$:

$$(1, 0, 1) = g_m \cdots g_2 g_1 (a, b, c), \tag{3.8}$$

where each $g_i$ is $s_1$, $s_2$, or $s_{123}$. More precisely, this product of $g_i$'s is built from products $s_1 s_{123}$, $s_2 s_{123}$, and $s_1 s_2 s_{123}$, where the reflections $s_1$ and $s_2$ serve to make all coordinates positive before the descent continues (see Examples 3.2 and 3.3). There is an $s_1$ or $s_2$ (or both) after each application of $s_{123}$ because at least one of the first two coordinates of $s_{123}(a, b, c)$ is negative if $a, b$, and $c$ are all positive.

We can bring the reflections $g_i$ in (3.8) from the right side to the left side by inverting them. A reflection is its own inverse, so

$$(a, b, c) = g_1 g_2 \cdots g_m (1, 0, 1). \tag{3.9}$$

Here the product of $g_i$'s is built from products of $(s_1 s_{123})^{-1} = s_{123}s_1 = A$, $(s_2 s_{123})^{-1} = s_{123}s_2 = B$, and $(s_1 s_2 s_{123})^{-1} = s_{123}s_2 s_1 = C$. Because $A(1, 0, 1) = (3, 4, 5)$, $B(1, 0, 1) = (1, 0, 1)$, and $C(1, 0, 1) = (3, 4, 5)$, if the left side of (3.9) has $a, b, c > 0$ then the right side can't be a product only of $B$'s. Therefore $g_1 g_2 \cdots g_m(1, 0, 1)$ can be rewritten to have $(3, 4, 5)$ at the start (right end) by combining $(1, 0, 1)$ with the first $A$ or $C$ that is applied to it. This proves every primitive Pythagorean triple with even $b$ appears in Berggren's tree.

Our last step is to show each primitive triple occurs just once in the tree. It suffices to show each triple $(a, b, c)$ with even $b$ other than $(3, 4, 5)$ has a unique parent in the tree: if $(a, b, c) \neq (3, 4, 5)$ then just one of the three triples

$$A^{-1}(a, b, c) = s_1 s_{123}(a, b, c), \quad B^{-1}(a, b, c) = s_2 s_{123}(a, b, c), \quad \text{and} \quad C^{-1}(a, b, c) = s_1 s_2 s_{123}(a, b, c)$$

has *all positive* coordinates. We already showed $s_{123}(a, b, c)$ has a positive third coordinate and its first two coordinates are not both $\geq 0$. Therefore just one of $s_1$, $s_2$, or $s_1 s_2$ applied to $s_{123}(a, b, c)$ produces a triple with all positive coordinates *unless* $s_{123}(a, b, c)$ has one of its first two coordinates equal to 0. Since $s_{123}(a, b, c)$ is primitive with even second coordinate, we must have $s_{123}(a, b, c) = (-1, 0, 1)$, so $(a, b, c) = s_{123}(-1, 0, 1) = (3, 4, 5)$. $\square$

**Remark 3.5.** *Since $A^{-1} = s_1 s_{123}$, $B^{-1} = s_2 s_{123}$, and $C^{-1} = s_1 s_2 s_{123}$ are all $s_{123}$ followed by (not preceded by!) sign changes on one or both of the first two coordinates, if you want to descend the tree from a specified primitive Pythagorean triple $(a, b, c)$ all the way down to $(3, 4, 5)$, it doesn't matter which of $A^{-1}$, $B^{-1}$, or $C^{-1}$ you apply to $(a, b, c)$. All three results will be the same up to sign changes, so after applying any of them simply pass to the absolute values of the coordinates (that is effectively applying $s_1$, $s_2$, or $s_1 s_2$) and then repeat the process.*

**Corollary 3.6.** *The group $\mathrm{O}_Q(\mathbf{Z})$ is generated by the five reflections*

$$s_1, \quad s_2, \quad s_3, \quad s_{123}, \quad s_{12}.$$

*Proof.* The proof of Theorem 3.1 used only these five reflections to carry any primitive null vector of $Q$ in $\mathbf{Z}^3$ to $(1, 0, 1)$, so $\mathrm{O}_Q(\mathbf{Z})$ is generated by these reflections and the matrices fixing $(1, 0, 1)$. Therefore it remains to show that the stabilizer subgroup of $(1, 0, 1)$ in $\mathrm{O}_Q(\mathbf{Z})$ lies in the group generated by the five reflections.

<!-- page 7 -->

A calculation (see the Appendix) shows the stabilizer of $(1, 0, 1)$ in $\mathrm{O}_Q(\mathbf{Z})$ consists of matrices of the form

$$\begin{pmatrix} 1 - 2m^2 & -2m & 2m^2 \\ 2m & 1 & -2m \\ -2m^2 & -2m & 1 + 2m^2 \end{pmatrix} \quad \text{or} \quad \begin{pmatrix} 1 - 2m^2 & 2m & 2m^2 \\ 2m & -1 & -2m \\ -2m^2 & 2m & 1 + 2m^2 \end{pmatrix}$$

for $m \in \mathbf{Z}$. The first matrix is $(s_2 s_{123})^m$ and the second matrix is $(s_2 s_{123})^m s_2$. $\square$

We used $s_{12}$ only to link $(1, 0, 1)$ and $(0, 1, 1)$ at the end of the proof of Theorem 3.1. The other four reflections in the generating set all reduce to the identity mod 2, so the subgroup of $\mathrm{O}_Q(\mathbf{Z})$ they generate can't send $(1, 0, 1)$ to $(0, 1, 1)$, or $(3, 4, 5)$ to $(4, 3, 5)$.

## 4. Other Matrices Generating Pythagorean Triples

In the literature there are other methods of generating primitive Pythagorean triples using matrices. We present two of them.

**Method 1:** Price [5] used the following three $3 \times 3$ matrices to generate the primitive Pythagorean triples starting from $(3, 4, 5)$:

$$\begin{pmatrix} 2 & 1 & -1 \\ -2 & 2 & 2 \\ -2 & 1 & 3 \end{pmatrix}, \quad \begin{pmatrix} 2 & 1 & 1 \\ 2 & -2 & 2 \\ 2 & -1 & 3 \end{pmatrix}, \quad \begin{pmatrix} 2 & -1 & 1 \\ 2 & 2 & 2 \\ 2 & 1 & 3 \end{pmatrix}. \tag{4.1}$$

Calling these $A'$, $B'$, and $C'$, we have the following start to an alternate tree of triples.

```
                                    A' --- (9,40,41)
                                   /
                    (5,12,13) --- B' --- (35,12,37)
                   /             \
                  /               C' --- (11,60,61)
                 /
                A'
               /
              /
             /                   A' --- (21,20,29)
            /                   /
(3,4,5) --- B' --- (15,8,17) --- B' --- (55,48,73)
            \                   \
             \                   C' --- (39,80,89)
              \
               C'
                \
                 \                   A' --- (13,84,85)
                  \                 /
                   (7,24,25) --- B' --- (63,16,65)
                                 \
                                  C' --- (15,112,113)
```

Price writes at the end of [5] that this method of generating Pythagorean triples is "less geometric" than Berggren's matrices, but $A'$, $B'$, and $C'$ can be interpreted geometrically. Each has determinant $\pm 8$, so they don't preserve $Q(x, y, z) = x^2 + y^2 - z^2$, but they almost preserve it: $Q(A'v) = 4Q(v)$, $Q(B'v) = 4Q(v)$, and $Q(C'v) = 4Q(v)$ for all $v \in \mathbf{R}^3$. Therefore $A'$, $B'$, and $C'$ preserve the cone $x^2 + y^2 - z^2 = 0$, where Pythagorean triples lie. A short search reveals how to write $B'$ and $C'$ in terms of $A'$ and reflections in $\mathrm{O}_Q(\mathbf{Z})$:

$$B' = s_1 A' s_1 s_2, \quad C' = s_{123}s_1 A'.$$

<!-- page 8 -->

**Method 2:** Instead of working in $\mathbf{R}^3$, Alperin [1] uses the 3-dimensional space $\mathcal{N}$ of $2 \times 2$ matrices $\left(\begin{smallmatrix} s & t \\ u & -s \end{smallmatrix}\right)$ with trace 0, equipped with the quadratic form $Q'\left(\begin{smallmatrix} s & t \\ u & -s \end{smallmatrix}\right) = s^2 + tu = -\det\left(\begin{smallmatrix} s & t \\ u & -s \end{smallmatrix}\right)$. The subset of matrices in $\mathcal{N}$ with determinant 0 is the replacement for the cone $\{(x, y, z) : x^2 + y^2 - z^2 = 0\}$ in $\mathbf{R}^3$. The quadratic spaces $(\mathbf{R}^3, Q)$ and $(\mathcal{N}, Q')$ are isomorphic by $f(x, y, z) = \left(\begin{smallmatrix} y & x - z \\ x + z & y \end{smallmatrix}\right)$, and primitive integral solutions to $a^2 + b^2 = c^2$ correspond to integral matrices $\left(\begin{smallmatrix} m & n \\ k & -m \end{smallmatrix}\right)$ where $m^2 + nk = 0$ and $\gcd(m, n, k) = 2$. Berggren's three matrices (1.1) appear on [1, p. 813]: $\mathcal{U}_-$ is $A$, $\mathcal{L}_+$ is $B$, and $\mathcal{U}_+$ is $C$.

## Appendix A. Calculating the Stabilizer of $(1, 0, 1)$.

We will calculate the stabilizer of $(1, 0, 1)$ in $\mathrm{O}_Q(\mathbf{Z})$, for the proof of Corollary 3.6. Since $Q(v) = v \cdot Jv$, where $J = \mathrm{diag}(1, 1, -1)$, we have $\mathrm{O}_Q(\mathbf{R}) = \{M \in \mathrm{M}_3(\mathbf{R}) : M^\top J M = J\}$.

From $M$ fixing $(1, 0, 1)$, it has the form

$$M = \begin{pmatrix} a & b & 1 - a \\ c & d & -c \\ e & f & 1 - e \end{pmatrix}.$$

The condition $M^\top J M = J$ implies

$$a^2 + c^2 - e^2 = 1, \tag{A.1}$$
$$ab + cd - ef = 0, \tag{A.2}$$
$$-a^2 + a - c^2 + e^2 - e = 0, \tag{A.3}$$
$$b^2 + d^2 - f^2 = 1, \tag{A.4}$$
$$-ab - cd + ef + b - f = 0. \tag{A.5}$$

Adding (A.1) and (A.3), $e = a - 1$. Adding (A.2) and (A.5), $f = b$, and feeding that into (A.4) gives us $d^2 = 1$, so $d = \pm 1$. Substituting these into (A.1) and (A.2) gives us

$$c^2 + 2a - 2 = 0,$$
$$cd + b = 0.$$

Thus $a = 1 - c^2/2$ and $b = -cd$, so

$$M = \begin{pmatrix} 1 - c^2/2 & -cd & c^2/2 \\ c & d & -c \\ -c^2/2 & -cd & 1 + c^2/2 \end{pmatrix}. \tag{A.6}$$

Conversely, any such matrix fixes $(1, 0, 1)$ and satisfies $M^\top J M = J$ (this requires $d^2 = 1$), so (A.6) describes the stabilizer of $(1, 0, 1)$ in $\mathrm{O}_Q(\mathbf{R})$. To be in $\mathrm{O}_Q(\mathbf{Z})$ requires $c$ to be an even number. Writing $c = 2m$ with $m \in \mathbf{Z}$, (A.6) becomes

$$\begin{pmatrix} 1 - 2m^2 & -2md & 2m^2 \\ 2m & d & -2m \\ -2m^2 & -2md & 1 + 2m^2 \end{pmatrix} \tag{A.7}$$

where $d = \pm 1$. When $d = m = 1$ this is

$$\begin{pmatrix} -1 & -2 & 2 \\ 2 & 1 & -2 \\ -2 & -2 & 3 \end{pmatrix} = s_2 s_{123}.$$

<!-- page 9 -->

When $d = 1$, the matrix in (A.7) is $(s_2 s_{123})^m$, and when $d = -1$ it is $(s_2 s_{123})^m s_2$.

## References

[1] R. C. Alperin, The Modular Tree of Pythagoras, *Amer. Math. Monthly* **112** (2005), 807-816.

[2] F. J. M. Barning, Over Pythagorese en bijna-Pythagorese driehoeken en een generatieproces met behulp van unimodulaire matrices, Math. Centrum, Amsterdam, Dept. Pure Math. ZW-011 (1963), 37 pages.

[3] B. Berggren, Pythagoreiska trianglar, *Tidskrift för Elementär Matematik, Fysik och Kemi* **17** (1934), 129-139.

[4] A. Hall, Genealogy of Pythagorean Triads, *The Math. Gazette* **54** (1970), 377-379.

[5] H. L. Price, The Pythagorean Tree: A New Species, http://arxiv.org/abs/0809.4324.

[6] J. Roberts, "Elementary Number Theory: A Problem Oriented Approach," MIT Press, Cambridge, MA 1977.
