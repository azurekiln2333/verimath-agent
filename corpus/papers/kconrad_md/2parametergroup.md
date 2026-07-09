# A 2-Parameter Nonabelian Group

> **Source**: https://kconrad.math.uconn.edu/blurbs/grouptheory/2parametergroup.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory

<!-- page 1 -->

## 1. Introduction

Set

$$G = \left\{\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix} : x > 0, y \in \mathbf{R}\right\},$$

which is a group under matrix multiplication:

$$\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}\begin{pmatrix} u & v \\ 0 & 1/u \end{pmatrix} = \begin{pmatrix} xu & xv + y/u \\ 0 & 1/xu \end{pmatrix}, \quad \begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}^{-1} = \begin{pmatrix} 1/x & -y \\ 0 & x \end{pmatrix}.$$

We *geometrically represent* $\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}$ as the point $(x,y)$ in the plane. So $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ corresponds to $(1,0)$ and we plot $g = \begin{pmatrix} 2 & 2 \\ 0 & 1/2 \end{pmatrix}$, $h = \begin{pmatrix} 3 & 1 \\ 0 & 1/3 \end{pmatrix}$, and several powers and products in Figure 1. Note $gh \neq hg$.

<!-- page 2 -->

In $G$, there are two "natural" subgroups

$$H = \left\{\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix} : x > 0\right\}, \quad K = \left\{\begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix} : y \in \mathbf{R}\right\}.$$

They are pictured below in Figure 2 as the points $(x,0)$ for $H$ and the points $(1,y)$ for $K$.

In Section 2 we will make pictures of conjugacy classes and conjugate subgroups, and in Section 3 we will see pictures of the left and right cosets of $H$ and $K$.

## 2. Conjugacy Classes and Conjugate Subgroups

The conjugate of $\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}$ by $\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}$ is

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \begin{pmatrix} x & ab(1/x - x) + a^2 y \\ 0 & 1/x \end{pmatrix}. \tag{2.1}$$

Equation (2.1) tells us **conjugate elements of $G$ have the same same upper left entry**. Therefore in our picture of $G$, conjugate elements of $G$ have the same first coordinate: they must lie on the same vertical line. We can use the formula (2.1) to compute a conjugacy class: fix $x$ and $y$, and let $a$ and $b$ vary on the right side of (2.1). Here are the results.

- The conjugacy class of the identity $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ is itself. See the green dot in Figure 3.
- Conjugates of $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ are found by setting $x = y = 1$ on the right side of (2.1). We get $\begin{pmatrix} 1 & a^2 \\ 0 & 1 \end{pmatrix}$ for all $a > 0$, which in Figure 3 is the red half-line through $(1,1)$ **above** the $x$-axis.
- Conjugates of $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ are $\begin{pmatrix} 1 & -a^2 \\ 0 & 1 \end{pmatrix}$ for all $a > 0$, which in Figure 3 is the blue half-line through $(1,-1)$ **below** the $x$-axis.
- We now determine the conjugacy class of $\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}$, where $x > 0$ and $x \neq 1$. A conjugate matrix has the form $\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}$ for some $y$. We will now show, for $x > 0$ and $x \neq 1$, that the matrix $\begin{pmatrix} x & y \\ 0 & 1/x \end{pmatrix}$ for **all** $y \in \mathbf{R}$ is conjugate to $\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}$. This would mean that in Figure 3, the conjugacy class of $\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}$ for $x > 0$ with $x \neq 1$ is represented by the **whole vertical line** through $(x,0)$.

To prove our description of the conjugacy class of $\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}$ is correct, this conjugacy class **includes** the matrices $\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} x & b(x-1/x) \\ 0 & 1/x \end{pmatrix}$, with $b$ running through all real numbers. Here $b$ *is variable* and $x$ *is fixed*. Since $x > 0$ and $x \neq 1$ we have $x - 1/x \neq 0$, so the upper right entry of the conjugate matrix runs through all real numbers as $b$ varies. See the orange and purple vertical lines in Figure 3 corresponding to $x = 3$ and $x = 5$.

<!-- page 4 -->

Turning from conjugacy classes of elements to conjugate subgroups, we will compute the subgroups of $G$ that are conjugate to $H = \{\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix} : x > 0\}$ and to $K = \{\begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix} : y \in \mathbf{R}\}$. The answers in these two cases will be **very** different.

For $a > 0$ and $b \in \mathbf{R}$, we have by equation (2.1) with $y = 0$ that $\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \begin{pmatrix} x & ab(1/x - x) \\ 0 & 1/x \end{pmatrix}$, so the subgroup conjugate to $H$ by $\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}$ is

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix} H \begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \left\{\begin{pmatrix} x & ab(1/x - x) \\ 0 & 1/x \end{pmatrix} : x > 0\right\}. \tag{2.2}$$

On the right side of (2.2), $a$ and $b$ are fixed and $x$ varies. Since $a$ and $b$ occur on the right side of (2.2) only through $ab$, conjugating $H$ by matrices in $G$ whose top two entries have the same product leads to the same conjugate subgroup to $H$. Thus for $b > 0$

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix} H \begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \begin{pmatrix} ab & 1 \\ 0 & 1/ab \end{pmatrix} H \begin{pmatrix} ab & 1 \\ 0 & 1/ab \end{pmatrix}^{-1}$$

since $a \cdot b = ab \cdot 1$, and for $b < 0$

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix} H \begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \begin{pmatrix} a|b| & -1 \\ 0 & 1/a|b| \end{pmatrix} H \begin{pmatrix} a|b| & -1 \\ 0 & 1/a|b| \end{pmatrix}^{-1}$$

since $a \cdot b = a|b| \cdot (-1)$. Thus conjugating $H$ by an element of $G$ that is not in $H$ (meaning $b \neq 0$) has the same effect as conjugating $H$ by a matrix of the form $\begin{pmatrix} t & 1 \\ 0 & 1/t \end{pmatrix}$ or $\begin{pmatrix} t & -1 \\ 0 & 1/t \end{pmatrix}$, where $t > 0$.

As an example,

$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} H \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^{-1} = \left\{\begin{pmatrix} x & 1/x - x \\ 0 & 1/x \end{pmatrix} : x > 0\right\}.$$

In Figure 4 this conjugate subgroup is represented by the set of all $(x, 1/x - x)$ with $x > 0$, which is *the graph of $y = 1/x - x$ for $x > 0$* (in red). The conjugate subgroup $\begin{pmatrix} 2 & 1 \\ 0 & 1/2 \end{pmatrix} H \begin{pmatrix} 2 & 1 \\ 0 & 1/2 \end{pmatrix}^{-1}$ is all $\begin{pmatrix} x & 2(1/x - x) \\ 0 & 1/x \end{pmatrix}$, which in Figure 4 is represented by the graph of $y = 2(1/x - x)$ for $x > 0$ (in green). More generally, from (2.2) the subgroup conjugate to $H$ by $\begin{pmatrix} a & 1 \\ 0 & 1/a \end{pmatrix}$ is represented as the graph of $y = a(1/x - x)$ for $x > 0$ and the subgroup conjugate to $H$ by $\begin{pmatrix} a & -1 \\ 0 & 1/a \end{pmatrix}$ is represented as the graph of $y = -a(1/x - x)$ for $x > 0$. These curves are pictured in Figure 4 for different $a$.

What subgroups in $G$ are conjugate to $K$? Since $\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}\begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \begin{pmatrix} 1 & a^2 y \\ 0 & 1 \end{pmatrix}$ we get

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix} K \begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}^{-1} = \left\{\begin{pmatrix} 1 & a^2 y \\ 0 & 1 \end{pmatrix} : y \in \mathbf{R}\right\} = \left\{\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} : t \in \mathbf{R}\right\} = K,$$

so the **only** subgroup of $G$ conjugate to $K$ is $K$. See Figure 5.

<!-- page 5 -->

## 3. Cosets

We will draw pictures for the left and right cosets of the subgroups $H$ and $K$. For $g = \begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}$, a typical element in $gH$ is

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix} = \begin{pmatrix} ax & b/x \\ 0 & 1/ax \end{pmatrix}$$

where $x > 0$. Letting $x$ run over all positive numbers, by a change of variables

$$gH = \left\{\begin{pmatrix} ax & b/x \\ 0 & 1/ax \end{pmatrix} : x > 0\right\} = \left\{\begin{pmatrix} t & ab/t \\ 0 & 1/t \end{pmatrix} : t > 0\right\},$$

which is pictured in Figure 6 as the graph of $y = ab/x$ for $x > 0$: the **branch of a hyperbola** passing through $(a,b)$. The left $H$-cosets are branches of hyperbolas that fill up $G$ without overlapping.

A typical element in the right coset $Hg$ is

$$\begin{pmatrix} x & 0 \\ 0 & 1/x \end{pmatrix}\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix} = \begin{pmatrix} ax & bx \\ 0 & 1/ax \end{pmatrix}$$

<!-- page 6 -->

for $x > 0$. Letting $x$ run over all positive numbers,

$$Hg = \left\{\begin{pmatrix} ax & bx \\ 0 & 1/ax \end{pmatrix} : x > 0\right\} = \left\{\begin{pmatrix} t & (b/a)t \\ 0 & 1/t \end{pmatrix} : t > 0\right\},$$

which is pictured in Figure 7 as the graph of the ray $y = (b/a)x$ coming out of the origin and passing through $(a,b)$. The right $H$-cosets are rays that fill up $G$ without overlapping.

Turning to the left and right cosets of $K$, a typical element in $gK$ is

$$\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix}\begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & ay + b \\ 0 & 1/a \end{pmatrix}.$$

As $y$ runs over all real numbers, $ay + b$ runs over all real numbers, so

$$gK = \left\{\begin{pmatrix} a & y \\ 0 & 1/a \end{pmatrix} : y \in \mathbf{R}\right\},$$

which is pictured as the vertical line $x = a$. Similarly, a typical element of the right coset $Kg$ is

$$\begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a & b \\ 0 & 1/a \end{pmatrix} = \begin{pmatrix} a & b + y/a \\ 0 & 1/a \end{pmatrix},$$

and as $y$ runs over $\mathbf{R}$ the numbers $b + y/a$ run over $\mathbf{R}$, so $Kg = gK$ for each $g \in G$. The left $K$-cosets and right $K$-cosets are each the collection of all vertical lines, which fill up $G$ without overlaps. See Figure 8.
