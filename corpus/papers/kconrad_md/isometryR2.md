# Isometries of the Plane and Linear Algebra

> **Source**: https://kconrad.math.uconn.edu/blurbs/isometryR2.pdf  
> **Author**: Keith Conrad  
> **Topic**: geometry

<!-- page 1 -->

## 1. Introduction

An *isometry* of $\mathbf{R}^2$ is a function $h: \mathbf{R}^2 \to \mathbf{R}^2$ that preserves the distance between vectors:

$$\|h(v) - h(w)\| = \|v - w\|$$

for all $v$ and $w$ in $\mathbf{R}^2$, where $\|(x, y)\| = \sqrt{x^2 + y^2}$.

**Example 1.1.** The identity transformation: $\operatorname{id}(v) = v$ for all $v \in \mathbf{R}^2$.

**Example 1.2.** Negation: $-\operatorname{id}(v) = -v$ for all $v \in \mathbf{R}^2$.

**Example 1.3.** Translation: fixing $u \in \mathbf{R}^2$, let $t_u(v) = v + u$. Easily $\|t_u(v) - t_u(w)\| = \|v - w\|$.

**Example 1.4.** Rotations around points and reflections across lines in the plane are isometries of $\mathbf{R}^2$. Formulas for these isometries will be given in Example 3.3 and Section 4.

The effects of a translation, rotation (around the origin) and reflection across a line in $\mathbf{R}^2$ are pictured below on sample line segments.

<!-- Figure: three diagrams showing translation, rotation, and reflection effects on line segments -->

The composition of two isometries of $\mathbf{R}^2$ is an isometry. Is every isometry invertible? It is clear that the three kinds of isometries pictured above (translations, rotations, reflections) are each invertible (translate by the negative vector, rotate by the opposite angle, reflect a second time across the same line).

In Section 2, we show the close link between isometries and the dot product on $\mathbf{R}^2$, which is more convenient to use than distances due to its algebraic properties. Section 3 is about the matrices that act as isometries on $\mathbf{R}^2$, called orthogonal matrices. Section 4 describes the isometries of $\mathbf{R}^2$ geometrically.

## 2. Isometries, Dot Products, and Linearity

Using translations, we can reduce the study of isometries of $\mathbf{R}^2$ to the case of isometries fixing $\mathbf{0}$.

<!-- page 2 -->

**Theorem 2.1.** *Every isometry of $\mathbf{R}^2$ can be uniquely written as the composition $t \circ k$ where $t$ is a translation and $k$ is an isometry fixing the origin.*

*Proof.* Let $h: \mathbf{R}^2 \to \mathbf{R}^2$ be an isometry. If $h = t_w \circ k$, where $t_w$ is translation by a vector $w$ and $k$ is an isometry fixing $\mathbf{0}$, then for all $v$ in $\mathbf{R}^2$ we have $h(v) = t_w(k(v)) = k(v) + w$. Setting $v = \mathbf{0}$ we get $w = h(\mathbf{0})$, so $w$ is determined by $h$. Then $k(v) = h(v) - w = h(v) - h(\mathbf{0})$, so $k$ is determined by $h$. Turning this around, if we define $t(v) = v + h(\mathbf{0})$ and $k(v) = h(v) - h(\mathbf{0})$, then $t$ is a translation, $k$ is an isometry fixing $\mathbf{0}$, and $h(v) = k(v) + h(\mathbf{0}) = t_w \circ k$, where $w = h(\mathbf{0})$. $\square$

**Theorem 2.2.** *For a function $h: \mathbf{R}^2 \to \mathbf{R}^2$, the following are equivalent:*

*(1) $h$ is an isometry and $h(\mathbf{0}) = \mathbf{0}$,*

*(2) $h$ preserves dot products: $h(v) \cdot h(w) = v \cdot w$ for all $v, w \in \mathbf{R}^2$.*

*Proof.* The link between length and dot product is the formula

$$\|v\|^2 = v \cdot v.$$

Suppose $h$ satisfies (1). Then for all vectors $v$ and $w$ in $\mathbf{R}^2$,

$$(2.1) \qquad \|h(v) - h(w)\| = \|v - w\|.$$

As a special case, when $w = \mathbf{0}$ in (2.1) we get $\|h(v)\| = \|v\|$ for all $v \in \mathbf{R}^2$. Squaring both sides of (2.1) and writing the result in terms of dot products makes it

$$(h(v) - h(w)) \cdot (h(v) - h(w)) = (v - w) \cdot (v - w).$$

Carrying out the multiplication,

$$(2.2) \qquad h(v) \cdot h(v) - 2h(v) \cdot h(w) + h(w) \cdot h(w) = v \cdot v - 2v \cdot w + w \cdot w.$$

The first term on the left side of (2.2) equals $\|h(v)\|^2 = \|v\|^2 = v \cdot v$ and the last term on the left side of (2.2) equals $\|h(w)\|^2 = \|w\|^2 = w \cdot w$. Canceling equal terms on both sides of (2.2), we obtain $-2h(v) \cdot h(w) = -2v \cdot w$, so $h(v) \cdot h(w) = v \cdot w$.

Now assume $h$ satisfies (2), so

$$(2.3) \qquad h(v) \cdot h(w) = v \cdot w$$

for all $v$ and $w$ in $\mathbf{R}^2$. Therefore

$$\|h(v) - h(w)\|^2 = (h(v) - h(w)) \cdot (h(v) - h(w))$$
$$= h(v) \cdot h(v) - 2h(v) \cdot h(w) + h(w) \cdot h(w)$$
$$= v \cdot v - 2v \cdot w + w \cdot w \quad \text{by (2.3)}$$
$$= (v - w) \cdot (v - w)$$
$$= \|v - w\|^2,$$

so $\|h(v) - h(w)\| = \|v - w\|$. Thus $h$ is an isometry. Setting $v = w = \mathbf{0}$ in (2.3), we get $\|h(\mathbf{0})\|^2 = 0$, so $h(\mathbf{0}) = \mathbf{0}$. $\square$

**Corollary 2.3.** *The only isometry of $\mathbf{R}^2$ fixing $\mathbf{0}$ and the standard basis is the identity.*

*Proof.* Let $h: \mathbf{R}^2 \to \mathbf{R}^2$ be an isometry that satisfies

$$h(\mathbf{0}) = \mathbf{0}, \quad h\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix}, \quad h\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}.$$

<!-- page 3 -->

Theorem 2.2 says

$$h(v) \cdot h(w) = v \cdot w$$

for all $v$ and $w$ in $\mathbf{R}^2$. Fix $v \in \mathbf{R}^2$ and let $w$ run over the standard basis vectors $e_1 = \binom{1}{0}$ and $e_2 = \binom{0}{1}$, so we see

$$h(v) \cdot h(e_i) = v \cdot e_i.$$

Since $h$ fixes each $e_i$,

$$h(v) \cdot e_i = v \cdot e_i.$$

Writing $v = c_1 e_1 + c_2 e_2$, we get

$$h(v) \cdot e_i = c_i$$

for $i = 1, 2$, so $h(v) = c_1 e_1 + c_2 e_2 = v$. As $v$ was arbitrary, $h$ is the identity on $\mathbf{R}^2$. $\square$

It is essential in Corollary 2.3 that the isometry fixes $\mathbf{0}$. An isometry of $\mathbf{R}^2$ fixing the standard basis *without* fixing $\mathbf{0}$ need not be the identity! For example, reflection across the line $x + y = 1$ in $\mathbf{R}^2$ is an isometry of $\mathbf{R}^2$ fixing $(1, 0)$ and $(0, 1)$ but not $\mathbf{0} = (0, 0)$. See below.

<!-- Figure: reflection across the line x + y = 1 -->

**Theorem 2.4.** *For a function $h: \mathbf{R}^2 \to \mathbf{R}^2$, the following are equivalent:*

*(1) $h$ is an isometry and $h(\mathbf{0}) = \mathbf{0}$,*

*(2) $h$ is linear, and the matrix $A$ such that $h(v) = Av$ for all $v \in \mathbf{R}^2$ satisfies $AA^\top = I_2$.*

*Proof.* Suppose $h$ is an isometry and $h(\mathbf{0}) = \mathbf{0}$. We want to prove linearity: $h(v + w) = h(v) + h(w)$ and $h(cv) = ch(v)$ for all $v$ and $w$ in $\mathbf{R}^2$ and all $c \in \mathbf{R}$. The mapping $h$ preserves dot products by Theorem 2.2:

$$h(v) \cdot h(w) = v \cdot w$$

for all $v$ and $w$ in $\mathbf{R}^2$. For the standard basis $e_1, e_2$ of $\mathbf{R}^2$ this says $h(e_i) \cdot h(e_j) = e_i \cdot e_j = \delta_{ij}$, so $h(e_1), h(e_2)$ is an orthonormal basis of $\mathbf{R}^2$. Thus two vectors in $\mathbf{R}^2$ are equal if they have the same dot product with each of $h(e_1)$ and $h(e_2)$.

For all $u$ in $\mathbf{R}^2$ we have

$$h(v + w) \cdot h(u) = (v + w) \cdot u$$

and

$$(h(v) + h(w)) \cdot h(u) = h(v) \cdot h(u) + h(w) \cdot h(u) = v \cdot u + w \cdot u = (v + w) \cdot u,$$

so $h(v + w) \cdot h(u) = (h(v) + h(w)) \cdot h(u)$ for all $u$. Letting $u = e_1, e_2$ shows $h(v + w) = h(v) + h(w)$. Similarly,

$$h(cv) \cdot h(u) = (cv) \cdot u = c(v \cdot u) = c(h(v) \cdot h(u)) = (ch(v)) \cdot h(u),$$

so again letting $u$ be $e_1$ and $e_2$ tells us $h(cv) = ch(v)$. Thus $h$ is linear.

<!-- page 4 -->

Let $A$ be the matrix for $h$: $h(v) = Av$ for all $v \in \mathbf{R}^2$, where $A$ has $j$th column $h(e_j)$. We want to show $AA^\top = I_2$. Since $h$ preserves dot products, the condition $h(v) \cdot h(w) = v \cdot w$ for all $v, w \in \mathbf{R}^2$ says $Av \cdot Aw = v \cdot w$. The fundamental link between the dot product and matrix transposes, which you should check, is that we can move a matrix to the other side of a dot product by using its transpose:

$$(2.4) \qquad v \cdot Mw = M^\top v \cdot w$$

for every $2 \times 2$ matrix $M$ and $v, w \in \mathbf{R}^2$. Using $M = A$ and $Av$ in place of $v$ in (2.4),

$$Av \cdot Aw = A^\top(Av) \cdot w = (A^\top A)v \cdot w.$$

This is equal to $v \cdot w$ for all $v$ and $w$, so $(A^\top A)v \cdot w = v \cdot w$ for all $v$ and $w$ in $\mathbf{R}^2$. Since the $(i, j)$ entry of a matrix $M$ is $Me_j \cdot e_i$, letting $v$ and $w$ run through the standard basis of $\mathbf{R}^2$ tells us $A^\top A = I_2$, so $A$ is invertible. An invertible matrix commutes with its inverse, so $A^\top A = I_2 \Rightarrow AA^\top = I_2$.

For the converse, assume $h(v) = Av$ for $v \in \mathbf{R}^2$ where $AA^\top = I_2$. Trivially $h$ fixes $\mathbf{0}$. To show $h$ is an isometry, by Theorem 2.2 it suffices to show

$$(2.5) \qquad Av \cdot Aw = v \cdot w$$

for all $v, w \in \mathbf{R}^2$. Since $A$ and its inverse $A^\top$ commute, we have $A^\top A = I_2$, so $Av \cdot Aw = A^\top(Av) \cdot w = (A^\top A)v \cdot w = v \cdot w$. $\square$

**Remark 2.5.** Linearity of isometries fixing $\mathbf{0}$ on finite-dimensional (not just 2-dimensional) vector spaces is due to A. Vogt [1, Lemma 1.5, Theorem 2.4]. The proof above is from [1]. Another proof is in my answer at https://math.stackexchange.com/questions/137139.

**Corollary 2.6.** *Isometries of $\mathbf{R}^2$ are invertible, the inverse of an isometry is an isometry, and two isometries on $\mathbf{R}^2$ that have the same values at $\mathbf{0}$ and any basis of $\mathbf{R}^2$ are equal.*

This gives a second proof of Corollary 2.3 as a special case.

*Proof.* Let $h: \mathbf{R}^2 \to \mathbf{R}^2$ be an isometry. By Theorem 2.1, $h = k + h(\mathbf{0})$ where $k$ is an isometry of $\mathbf{R}^2$ fixing $\mathbf{0}$. Theorem 2.4 tells us there is an invertible matrix $A$ such that $k(v) = Av$ for all $v \in \mathbf{R}^2$, so

$$h(v) = Av + h(\mathbf{0}).$$

This has inverse $h^{-1}(v) = A^{-1}(v - h(\mathbf{0}))$. In particular, $h$ is surjective.

The isometry condition $\|h(v) - h(w)\| = \|v - w\|$ for all $v$ and $w$ in $\mathbf{R}^2$ implies $\|v - w\| = \|h^{-1}(v) - h^{-1}(w)\|$ for all $v$ and $w$ in $\mathbf{R}^2$ by replacing $v$ and $w$ in the isometry condition with $h^{-1}(v)$ and $h^{-1}(w)$. Thus $h^{-1}$ is an isometry of $\mathbf{R}^2$.

If $h_1$ and $h_2$ are isometries of $\mathbf{R}^2$ that are equal on $\mathbf{0}$ and a basis then the functions $k_1(v) = h_1(v) - h_1(\mathbf{0})$ and $k_2(v) = h_2(v) - h_2(\mathbf{0})$ are linear and are equal on that basis, so by linearity $k_1 = k_2$ on $\mathbf{R}^2$. That is, $h_1(v) - h_1(\mathbf{0}) = h_2(v) - h_2(\mathbf{0})$ for all $v$ in $\mathbf{R}^2$. Since $h_1(\mathbf{0}) = h_2(\mathbf{0})$ we get $h_1 = h_2$ on $\mathbf{R}^2$. $\square$

**Corollary 2.7.** *Let $P_0, P_1, P_2$ be 3 points in $\mathbf{R}^2$ in "general position", i.e., they don't all lie on a line. Two isometries of $\mathbf{R}^2$ that are equal at $P_0, P_1, P_2$ are the same.*

In the definition of "general position", the lines in $\mathbf{R}^2$ need not contain the origin.

*Proof.* We know isometries of $\mathbf{R}^2$ are invertible. If $h_1$ and $h_2$ are isometries of $\mathbf{R}^2$ with the same values at each $P_i$ then $h_2^{-1} \circ h_1$ is an isometry that fixes each $P_i$. Therefore to prove $h_1 = h_2$ it suffices to show an isometry of $\mathbf{R}^2$ that fixes $P_0, P_1$, and $P_2$ is the identity.

<!-- page 5 -->

Let $h$ be an isometry of $\mathbf{R}^2$ such that $h(P_i) = P_i$ for $i = 0, 1, 2$. Set $t(v) = v - P_0$, which is a translation. Then $tht^{-1}$ is an isometry with formula

$$(tht^{-1})(v) = h(v + P_0) - P_0.$$

Thus $(tht^{-1})(\mathbf{0}) = h(P_0) - P_0 = \mathbf{0}$, so $tht^{-1}$ is linear by Theorem 2.4. Also $(tht^{-1})(P_i - P_0) = h(P_i) - P_0 = P_i - P_0$.

Upon subtracting $P_0$ from $P_0, P_1, P_2$, the points $\mathbf{0}, P_1 - P_0, P_2 - P_0$ are in general position. That means no hyperplane can contain them all, so there is no nontrivial linear relation among $P_1 - P_0$ and $P_2 - P_0$ (a nontrivial linear relation would place these 2 points, along with $\mathbf{0}$, on a common line), and thus $P_1 - P_0, P_2 - P_0$ is a basis of $\mathbf{R}^2$. By Corollary 2.6, $tht^{-1}$ is the identity, so $h$ is the identity. $\square$

## 3. Orthogonal Matrices

We have seen that the isometries of $\mathbf{R}^2$ that fix $\mathbf{0}$ come from matrices $A$ such that $AA^\top = I_2$. These matrices have a name.

**Definition 3.1.** A $2 \times 2$ matrix $A$ is called *orthogonal* if $AA^\top = I_2$, or equivalently if $A^\top A = I_2$.

A matrix is orthogonal when its transpose is its inverse. Since $\det(A^\top) = \det A$, an orthogonal matrix $A$ satisfies $(\det A)^2 = 1$, so $\det A = \pm 1$. (Not all matrices with determinant $\pm 1$ are orthogonal, such as $\begin{pmatrix}3 & 1\\5 & 2\end{pmatrix}$.)

**Example 3.2.** Negation on $\mathbf{R}^2$ (Example 1.2) is an isometry that is described by the matrix $-I_2$, which is orthogonal: $(-I_2)(-I_2)^\top = (-I_2)(-I_2) = I_2$.

**Example 3.3.** By algebra, $AA^\top = I_2$ if and only if $A = \begin{pmatrix}a & -\varepsilon b\\b & \varepsilon a\end{pmatrix}$, where $a^2 + b^2 = 1$ and $\varepsilon = \pm 1$. Writing $a = \cos\theta$ and $b = \sin\theta$, we get the matrices $\begin{pmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{pmatrix}$ and $\begin{pmatrix}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{pmatrix}$. Algebraically, these types of matrices are distinguished by their determinants: the first type has determinant $1$ and the second type has determinant $-1$.

The geometric effects of these two types of matrices differ. Below on the left, $\begin{pmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{pmatrix}$ is a counterclockwise rotation by angle $\theta$ around the origin. Below on the right, $\begin{pmatrix}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{pmatrix}$ is a reflection across the line through the origin at angle $\theta/2$ with respect to the positive $x$-axis. (Check $\begin{pmatrix}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{pmatrix}$ squares to the identity, as any reflection should.)

<!-- Figure: left shows rotation matrix A with vectors v, w and their images A(v), A(w); right shows reflection matrix A with vectors v, w and their images A(v), A(w) -->

Let's explain why $\begin{pmatrix}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{pmatrix}$ is a reflection at angle $\theta/2$. See the figure below. Pick a line $L$ through the origin, say at an angle $\varphi$ with respect to the positive $x$-axis. To find a formula for reflection across $L$, we'll use a basis of $\mathbf{R}^2$ with one vector **on** $L$ and the other

<!-- page 6 -->

vector **perpendicular** to $L$. The unit vector $u_1 = \binom{\cos\varphi}{\sin\varphi}$ lies on $L$ and the unit vector $u_2 = \binom{-\sin\varphi}{\cos\varphi}$ is perpendicular to $L$. For $v \in \mathbf{R}^2$, write $v = c_1 u_1 + c_2 u_2$ with $c_1, c_2 \in \mathbf{R}$.

<!-- Figure: coordinate system with line L at angle phi, showing vectors u1, u2, v, s(v) -->

The reflection of $v$ across $L$ is $s(v) = c_1 u_1 - c_2 u_2$. Writing $a = \cos\varphi$ and $b = \sin\varphi$ (so $a^2 + b^2 = 1$), in standard coordinates this becomes

$$(3.1) \qquad v = c_1 u_1 + c_2 u_2 = c_1\begin{pmatrix}a\\b\end{pmatrix} + c_2\begin{pmatrix}-b\\a\end{pmatrix} = \begin{pmatrix}c_1 a - c_2 b\\c_1 b + c_2 a\end{pmatrix} = \begin{pmatrix}a & -b\\b & a\end{pmatrix}\begin{pmatrix}c_1\\c_2\end{pmatrix}$$

and in a similar way

$$s(v) = c_1 u_1 - c_2 u_2$$
$$= \begin{pmatrix}a & b\\b & -a\end{pmatrix}\begin{pmatrix}c_1\\c_2\end{pmatrix}$$
$$= \begin{pmatrix}a & b\\b & -a\end{pmatrix}\begin{pmatrix}a & -b\\b & a\end{pmatrix}^{-1} v \quad \text{by (3.1)}$$
$$= \begin{pmatrix}a & b\\b & -a\end{pmatrix}\begin{pmatrix}a & b\\-b & a\end{pmatrix} v$$
$$= \begin{pmatrix}a^2 - b^2 & 2ab\\2ab & -(a^2 - b^2)\end{pmatrix} v.$$

By the sine and cosine duplication formulas, the last matrix is $\begin{pmatrix}\cos(2\varphi) & \sin(2\varphi)\\\sin(2\varphi) & -\cos(2\varphi)\end{pmatrix}$. Therefore $\begin{pmatrix}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{pmatrix}$ is a reflection across the line through the origin at angle $\theta/2$.

The geometric meaning of the condition $A^\top A = I_2$ is that the columns of $A$ are mutually perpendicular unit vectors (check!). From this we see how to create orthogonal matrices: starting with an orthonormal basis of $\mathbf{R}^2$, a $2 \times 2$ matrix having this basis as its columns (in any order) is an orthogonal matrix, and all $2 \times 2$ orthogonal matrices arise in this way.

Let $\operatorname{O}_2(\mathbf{R})$ denote the set of $2 \times 2$ orthogonal matrices:

$$(3.2) \qquad \operatorname{O}_2(\mathbf{R}) = \{A \in \operatorname{GL}_2(\mathbf{R}) : AA^\top = I_2\}.$$

**Theorem 3.4.** *The set $\operatorname{O}_2(\mathbf{R})$ is a group under matrix multiplication.*

*Proof.* Clearly $I_2 \in \operatorname{O}_2(\mathbf{R})$. If $A$ and $B$ are in $\operatorname{O}_2(\mathbf{R})$, then

$$(AB)(AB)^\top = ABB^\top A^\top = AA^\top = I_2,$$

so $AB \in \operatorname{O}_2(\mathbf{R})$. For $A \in \operatorname{O}_2(\mathbf{R})$, we have $A^{-1} = A^\top$ and

$$(A^{-1})(A^{-1})^\top = A^\top(A^\top)^\top = A^\top A = I_2.$$

Therefore $A^{-1} \in \operatorname{O}_2(\mathbf{R})$. $\square$

<!-- page 7 -->

The link between isometries and dot products (Theorem 2.2) gives us a more geometric description of $\operatorname{O}_2(\mathbf{R})$ than (3.2):

$$(3.3) \qquad \operatorname{O}_2(\mathbf{R}) = \{A \in \operatorname{GL}_2(\mathbf{R}) : Av \cdot Aw = v \cdot w \text{ for all } v, w \in \mathbf{R}^2\}.$$

The label "orthogonal matrix" is very unfortunate. It suggests that such matrices should be the ones that preserves orthogonality of vectors:

$$(3.4) \qquad v \cdot w = 0 \Longrightarrow Av \cdot Aw = 0$$

for all $v$ and $w$ in $\mathbf{R}^2$. While orthogonal matrices do satisfy (3.4), since (3.4) is a special case of the condition $Av \cdot Aw = v \cdot w$ in (3.3), many matrices satisfy (3.4) and are not orthogonal matrices! That is, orthogonal matrices (which, by definition, preserve *all* dot products) are not the only matrices that preserve orthogonality of vectors (dot products equal to $0$). A simple example of a nonorthogonal matrix satisfying (3.4) is a scalar matrix $cI_2$, where $c \ne \pm 1$ in $\mathbf{R}$. Since $(cv) \cdot (cw) = c^2(v \cdot w)$, $cI_2$ does not preserve dot products in general but it does preserve dot products equal to $0$. It's natural to ask which $2 \times 2$ matrices besides orthogonal matrices preserve orthogonality. Here is the complete answer, which shows they are not that far from being orthogonal.

**Theorem 3.5.** *A $2 \times 2$ real matrix $A$ satisfies (3.4) if and only if $A$ is a scalar multiple of an orthogonal matrix.*

*Proof.* If $A = cA'$ where $A'$ is orthogonal and $c \in \mathbf{R}$, then $Av \cdot Aw = c^2(A'v \cdot A'w) = c^2(v \cdot w)$, so if $v \cdot w = 0$ then $Av \cdot Aw = 0$.

Now assume $A$ satisfies (3.4). Then the vectors $Ae_1, Ae_2$ are mutually perpendicular, so the columns of $A$ are perpendicular to each other. We want to show that they have the same length.

Note that $e_1 + e_2 \perp e_1 - e_2$, so by (3.4) and linearity $Ae_1 + Ae_2 \perp Ae_1 - Ae_2$. Writing this in the form $(Ae_1 + Ae_2) \cdot (Ae_1 - Ae_2) = 0$ and expanding, we are left with $Ae_1 \cdot Ae_1 = Ae_2 \cdot Ae_2$, so $\|Ae_1\| = \|Ae_2\|$. Therefore the columns of $A$ are mutually perpendicular vectors with the same length. Call this common length $c$. If $c = 0$ then $A = O = 0 \cdot I_2$. If $c \ne 0$ then the matrix $(1/c)A$ has an orthonormal basis as its columns, so it is an orthogonal matrix. Therefore $A = c((1/c)A)$ is a scalar multiple of an orthogonal matrix. $\square$

Since a composition of isometries is an isometry and isometries are invertible with the inverse of an isometry being an isometry, isometries form a group under composition. We will describe the elements of this group and show how the group law looks in that description.

**Theorem 3.6.** *For $A \in \operatorname{O}_2(\mathbf{R})$ and $w \in \mathbf{R}^2$, the function $h_{A,w}: \mathbf{R}^2 \to \mathbf{R}^2$ given by*

$$h_{A,w}(v) = Av + w = (t_w A)(v)$$

*is an isometry. Moreover, every isometry of $\mathbf{R}^2$ has this form for unique $A$ and $w$.*

*Proof.* The indicated formula always gives an isometry, since it is the composition of a translation and orthogonal transformation, which are both isometries.

To show every isometry of $\mathbf{R}^2$ has the form $h_{A,w}$ for some $A$ and $w$, let $h: \mathbf{R}^2 \to \mathbf{R}^2$ be an isometry. By Theorem 2.1, $h = k(v) + h(\mathbf{0})$ where $k$ is an isometry of $\mathbf{R}^2$ fixing $\mathbf{0}$. Theorem 2.2 tells us there is an $A \in \operatorname{O}_2(\mathbf{R})$ such that $k(v) = Av$ for all $v \in \mathbf{R}^2$, so

$$h(v) = Av + h(\mathbf{0}) = h_{A,w}(v)$$

where $w = h(\mathbf{0})$.

<!-- page 8 -->

If $h_{A,w} = h_{A',w'}$ as functions on $\mathbf{R}^2$, then evaluating both sides at $\mathbf{0}$ gives $w = w'$. Therefore $Av + w = A'v + w$ for all $v$, so $Av = A'v$ for all $v$, which implies $A = A'$. $\square$

Let $\operatorname{Iso}(\mathbf{R}^2)$ denote the group of isometries of $\mathbf{R}^2$. Its elements have the form $h_{A,w}$ by Theorem 3.6. Here is what composition of such mappings looks like:

$$h_{A,w}(h_{A',w'}(v)) = A(A'v + w') + w$$
$$= AA'v + Aw' + w$$
$$= h_{AA', Aw'+w}(v).$$

This is similar to the multiplication law in the $ax + b$ group:

$$\begin{pmatrix}a & b\\0 & 1\end{pmatrix}\begin{pmatrix}a' & b'\\0 & 1\end{pmatrix} = \begin{pmatrix}aa' & ab'+b\\0 & 1\end{pmatrix}.$$

In fact, if we write an isometry $h_{A,w} \in \operatorname{Iso}(\mathbf{R}^2)$ as a $3 \times 3$ matrix $\begin{pmatrix}A & w\\0 & 1\end{pmatrix}$, where the $0$ in the bottom is a row vector of 2 zeros, then the composition law in $\operatorname{Iso}(\mathbf{R}^2)$ is multiplication of the corresponding $3 \times 3$ matrices, so $\operatorname{Iso}(\mathbf{R}^2)$ can be viewed as a subgroup of $\operatorname{GL}_3(\mathbf{R})$, acting on $\mathbf{R}^2$ as the column vectors $\binom{v}{1}$ in $\mathbf{R}^3$ (not a subspace!).

## 4. Geometric Description of Isometries of $\mathbf{R}^2$

We know from Theorem 3.6 what all the isometries of $\mathbf{R}^2$ look like by formulas. In this section we describe what they are like geometrically.

Write an isometry $h \in \operatorname{Iso}(\mathbf{R}^2)$ as $h(v) = Av + w$ with $A \in \operatorname{O}_2(\mathbf{R})$ and $w \in \mathbf{R}^2$. By Example 3.3, $A$ is a rotation or reflection, depending on $\det A$.

There turn out to be four possibilities for $h$: translations, rotations, reflections, and glide reflections. A *glide reflection* is the composition of a reflection and a nonzero translation in a direction parallel to the line of reflection. A picture of a glide reflection is in the figure below, where the (horizontal) line of reflection is dashed and the translation is a movement to the right.

<!-- Figure: glide reflection showing before and after states with dashed line of reflection -->

The image above, which includes "before" and "after" states, suggests a physical interpretation of a glide reflection: it is the result of turning the plane in space like a half-turn of a screw. A more picturesque image, suggested to me by Michiel Vermeulen, is the effect of successive steps with a left foot and then a right foot in the sand or snow (if your feet are mirror reflections).

The possibilities for isometries of $f$ are collected in Table 1 below. It describes how the type of an isometry $h$ is determined by $\det A$ and the geometry of the set of fixed points of $h$ (solutions to $h(v) = v$): empty, a point, a line, or the plane. (The only isometry belonging to more than one of the four possibilities is the identity, which is both a translation and a

<!-- page 9 -->

rotation, so we make the identity its own row in the table.) The table also shows that a description of the fixed points can be obtained algebraically from $A$ and $w$.

| Isometry | Condition | Fixed pts |
|---|---|---|
| Identity | $A = I_2, w = 0$ | $\mathbf{R}^2$ |
| Nonzero Translation | $A = I_2, w \ne 0$ | $\emptyset$ |
| Nonzero Rotation | $\det A = 1, A \ne I_2$ | $(I_2 - A)^{-1}w$ |
| Reflection | $\det A = -1, Aw = -w$ | $w/2 + \ker(A - I_2)$ |
| Glide Reflection | $\det A = -1, Aw \ne -w$ | $\emptyset$ |

**Table 1.** Isometries of $\mathbf{R}^2$: $h(v) = Av + w$, $A \in \operatorname{O}_2(\mathbf{R})$.

To justify the information in the table we move down the middle column. The first two rows are obvious, so we start with the third row.

**Row 3:** Suppose $\det A = 1$ and $A \ne I_2$, so $A = \begin{pmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{pmatrix}$ for some $\theta$ and $\cos\theta \ne 1$. We want to show $h$ is a rotation. First of all, $h$ has a unique fixed point: $v = Av + w$ precisely when $w = (I_2 - A)v$. We have $\det(I_2 - A) = 2(1 - \cos\theta) \ne 0$, so $I_2 - A$ is invertible and $p = (I_2 - A)^{-1}w$ is the fixed point of $h$. Then $w = (I_2 - A)p = p - Ap$, so

$$(4.1) \qquad h(v) = Av + (p - Ap) = A(v - p) + p.$$

Since $A$ is a rotation by $\theta$ around the origin, (4.1) shows $h$ is a rotation by $\theta$ around $P$.

**Rows 4, 5:** Suppose $\det A = -1$, so $A = \begin{pmatrix}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{pmatrix}$ for some $\theta$ and $A^2 = I_2$. We again look at fixed points of $h$. As before, $h(v) = v$ for some $v$ if and only if $w = (I_2 - A)v$. But unlike the previous case, now $\det(I_2 - A) = 0$ (check!), so $I_2 - A$ is not invertible and therefore $w$ may or may not be in the image of $I_2 - A$. When $w$ is in the image of $I_2 - A$, we will see that $h$ is a reflection. When $w$ is not in the image of $I_2 - A$, we will see that $h$ is a glide reflection.

Suppose the isometry $h(v) = Av + w$ with $\det A = -1$ has a fixed point. Then $w/2$ must be a fixed point. Indeed, let $p$ be a fixed point, so $p = Ap + w$. Since $A^2 = I_2$,

$$Aw = A(p - Ap) = Ap - p = -w,$$

so

$$h\left(\frac{w}{2}\right) = A\left(\frac{w}{2}\right) + w = \frac{1}{2}Aw + w = \frac{w}{2}.$$

Conversely, if $h(w/2) = w/2$ then $A(w/2) + w = w/2$, so $Aw = -w$.

Thus $h$ has a fixed point if and only if $Aw = -w$, in which case

$$(4.2) \qquad h(v) = Av + w = A\left(v - \frac{w}{2}\right) + \frac{w}{2}.$$

Since $A$ is a reflection across some line $L$ through $\mathbf{0}$, (4.2) says $h$ is a reflection across the parallel line $w/2 + L$ passing through $w/2$. See the figure below. (Algebraically, we can say $L = \{v : Av = v\} = \ker(A - I_2)$. Since $A - I_2$ is not invertible and not identically $0$, its kernel really is 1-dimensional.)

<!-- page 10 -->

<!-- Figure: reflection across line w/2 + L, showing vectors v, Av, w, h(v), w/2, and lines L and w/2 + L -->

Now assume $h$ has no fixed point, so $Aw \ne -w$. We will show $h$ is a glide reflection. (The formula $h = Av + w$ shows $h$ is the composition of a reflection and a nonzero translation, but $w$ need not be parallel to the line of reflection of $A$, which is $\ker(A - I_2)$, so this formula for $h$ does *not* show directly that $h$ is a glide reflection.) We will now take stronger advantage of the fact that $A^2 = I_2$.

Since $O = A^2 - I_2 = (A - I_2)(A + I_2)$ and $A \ne \pm I_2$ (after all, $\det A = -1$), $A + I_2$ and $A - I_2$ are not invertible. Therefore the subspaces

$$W_1 = \ker(A - I_2), \quad W_2 = \ker(A + I_2)$$

are both nonzero, and neither is the whole plane, so $W_1$ and $W_2$ are both one-dimensional. We already noted that $W_1$ is the line of reflection of $A$ (fixed points of $A$ form the kernel of $A - I_2$). It turns out that $W_2$ is the line perpendicular to $W_1$. To see why, pick $w_1 \in W_1$ and $w_2 \in W_2$, so

$$Aw_1 = w_1, \quad Aw_2 = -w_2.$$

Then, since $Aw_1 \cdot Aw_2 = w_1 \cdot w_2$ by orthogonality of $A$, we have

$$w_1 \cdot (-w_2) = w_1 \cdot w_2.$$

Thus $w_1 \cdot w_2 = 0$, so $w_1 \perp w_2$.

Now we are ready to show $h$ is a glide reflection. Pick nonzero vectors $w_i \in W_i$ for $i = 1, 2$, and use $\{w_1, w_2\}$ as a basis of $\mathbf{R}^2$. Write $w = h(\mathbf{0})$ in terms of this basis: $w = c_1 w_1 + c_2 w_2$. To say there are no fixed points for $h$ is the same as $Aw \ne -w$, so $w \notin W_2$. That is, $c_1 \ne 0$. Then

$$(4.3) \qquad h(v) = Av + w = (Av + c_2 w_2) + c_1 w_1.$$

Since $A(c_2 w_2) = -c_2 w_2$, our previous discussion shows $v \mapsto Av + c_2 w_2$ is a reflection across the line $c_2 w_2/2 + W_1$. Since $c_1 w_1$ is a nonzero vector in $W_1$, (4.3) exhibits $h$ as the composition of a reflection across the line $c_2 w_2/2 + W_1$ and a nonzero translation by $c_1 w_1$, whose direction is parallel to the line of reflection, so $h$ is a glide reflection.

We have now justified the information in Table 1. Each row describes a different kind of isometry. Using fixed points it is easy to distinguish the first four rows from each other and to distinguish glide reflections from isometries other than translations. A glide reflection can't be a translation since an isometry of $\mathbf{R}^2$ is uniquely of the form $h_{A,w}$, and translations have $A = I_2$ while glide reflections have $\det A = -1$.

**Lemma 4.1.** *A composition of two reflections of $\mathbf{R}^2$ is a translation or a rotation.*

*Proof.* The product of two matrices with determinant $-1$ has determinant $1$, so the composition of two reflections has the form $v \mapsto Av + w$ where $\det A = 1$. Such isometries

<!-- page 11 -->

are translations or rotations by Table 1 (consider the identity to be a trivial translation or rotation). $\square$

**Theorem 4.2.** *Each isometry of $\mathbf{R}^2$ is a composition of at most 2 reflections except for glide reflections, which are a composition of 3 (and no fewer) reflections.*

*Proof.* We check the theorem for each type of isometry in Table 1 besides reflections, for which the theorem is obvious.

The identity is the square of every reflection.

For a translation $t(v) = v + w$, let $A$ be the matrix representing the reflection across the line $w^\perp$. Then $Aw = -w$. Set $s_1(v) = Av + w$ and $s_2(v) = Av$. Both $s_1$ and $s_2$ are reflections, and $(s_1 \circ s_2)(v) = A(Av) + w = v + w$ since $A^2 = I_2$.

Now consider a rotation, say $h(v) = A(v - p) + p$ for some $A \in \operatorname{O}_2(\mathbf{R})$ with $\det A = 1$ and $p \in \mathbf{R}^2$. We have $h = t \circ r \circ t^{-1}$, where $t$ is translation by $p$ and $r(v) = Av$ is a rotation around the origin. Let $A'$ be a reflection matrix (e.g., $A' = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}$). Set $s_1(v) = AA'v$ and $s_2(v) = A'v$. Both $s_1$ and $s_2$ are reflections and $r = s_1 \circ s_2$ (check). Therefore

$$(4.4) \qquad h = t \circ r \circ t^{-1} = (t \circ s_1 \circ t^{-1}) \circ (t \circ s_2 \circ t^{-1}).$$

The conjugate of a reflection by a translation (or by any isometry, for that matter) is another reflection, as an explicit calculation using Table 1 shows. Thus, (4.4) expresses the rotation $h$ as a composition of 2 reflections.

Finally we consider glide reflections. Since this is the composition of a translation and a reflection, it is a composition of 3 reflections. We can't use fewer reflections to get a glide reflection, since a composition of two reflections is either a translation or a rotation by Lemma 4.1 and we know that a glide reflection is not a translation or rotation (or reflection). $\square$

In Table 2 we record the minimal number of reflections whose composition can equal a particular type of isometry of $\mathbf{R}^2$.

| Isometry | Min. Num. Reflections | dim(fixed set) |
|---|---|---|
| Identity | 0 | 2 |
| Nonzero Translation | 2 | 0 |
| Nonzero Rotation | 2 | 0 |
| Reflection | 1 | 1 |
| Glide Reflection | 3 | 0 |

**Table 2.** Counting Reflections in an Isometry

That each isometry of $\mathbf{R}^2$ is a composition of at most 3 reflections can be proved geometrically, without recourse to a prior classification of all isometries of the plane. We will give a rough sketch of the argument. We will take for granted (!) that an isometry that fixes at least two points is a reflection across the line through those points or is the identity. (This is related to Corollary 2.3 when $n = 2$.) Pick an isometry $h$ of $\mathbf{R}^2$. We may suppose $h$ is not a reflection or the identity (the identity is the square of every reflection), so $h$ has at most one fixed point. If $h$ has one fixed point, say $P$, choose $Q \ne P$. Then $h(Q) \ne Q$ and the points $Q$ and $h(Q)$ lie on a common circle centered at $P$ (because $h(P) = P$). Let $s$ be the reflection across the line through $P$ that is perpendicular to the line connecting $Q$ and $h(Q)$. Then $s \circ h$ fixes $P$ and $Q$, so $s \circ h$ is the identity or is a reflection. Thus $h = s \circ (s \circ h)$

<!-- page 12 -->

is a reflection or a composition of two reflections. If $h$ has no fixed points, pick a point $P$. Let $s$ be the reflection across the perpendicular bisector of the line connecting $P$ and $h(P)$, so $s \circ h$ fixes $P$. Thus $s \circ h$ has a fixed point, so our previous argument shows $s \circ h$ is either the identity, a reflection, or the composition of two reflections, so $h$ is the composition of at most 3 reflections.

A byproduct of this argument, which did not use the classification of isometries, is another proof that all isometries of $\mathbf{R}^2$ are invertible: every isometry is a composition of reflections and reflections are invertible.

## References

[1] A. Vogt, "On the linearity of form isometries," *SIAM Journal on Applied Mathematics* **22** (1972), 553--560.
