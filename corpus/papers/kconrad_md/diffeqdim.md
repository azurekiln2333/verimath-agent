# Differential Equations and Linear Algebra

> **Source**: https://kconrad.math.uconn.edu/blurbs/diffeqdim.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra

<!-- page 1 -->

## 1. Introduction

We develop some results about linear differential equations with constant coefficients using linear algebra. Our concern is not cookbook methods to find all the solutions to a differential equation, but the computation of the *dimension* of the solution space.

Consider a homogeneous linear differential equation with constant (real) coefficients:
$$y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1 y' + a_0 y = 0. \tag{1.1}$$
The "homogeneous" label means if $y$ fits the equation then so does $cy$ for all constants $c$. (If the right side were a nonzero function then $cy$ would no longer be a solution and (1.1) is then called "inhomogeneous.") The "linear" part refers to the linear operator
$$D^n + a_{n-1}D^{n-1} + \cdots + a_1 D + a_0 I, \tag{1.2}$$
where $D = \mathrm{d}/\mathrm{d}t$ is the basic differentiation operator on functions. (The $j$-th derivative operator, for $j \geq 1$, is $D^j$, and we consider the identity operator $I$ as $D^0$, since it is standard to regard the zero-th derivative of a function as the function itself: $D^0(y) = y$ for all functions $y$.) We call (1.2) an $n$-th order linear differential operator since the highest derivative appearing in it is the $n$-th derivative. We want to show the solution space to (1.1) is $n$-dimensional.

## 2. Passage to the Complex Case

A solution to (1.1) has to have at least $n$ derivatives for the equation to make sense. Then, by using (1.1) to write $y^{(n)}$ in terms of lower-order derivatives of $y$, induction shows every solution to (1.1) has to be infinitely differentiable. Let $C^\infty(\mathbf{R})$ be the space of all functions $\mathbf{R} \to \mathbf{R}$ that are infinitely differentiable. This is an infinite-dimensional vector space, and it is this space in which we search for solutions of (1.1) because every solution to (1.1) must be in here.

Let
$$p(t) = t^n + a_{n-1}t^{n-1} + \cdots + a_1 t + a_0 \tag{2.1}$$
be the polynomial having the coefficients from (1.1).

**Example 2.1.** If $y'' - 2y' - 3y = 0$ then $p(t) = t^2 - 2t - 3$.

The equation (1.1) can be written in the condensed form
$$p(D)(y) = 0.$$
That is, solutions $y$ to (1.1) form the *kernel* of the differential operator $p(D)$ on $C^\infty(\mathbf{R})$. This viewpoint, that solutions to a differential equation are the kernel of a linear operator on $C^\infty(\mathbf{R})$, is the link between differential equations and linear algebra. *Warning:* There are many nonlinear differential equations, like $y'' = yy' + y^3$, and the methods of linear

<!-- page 2 -->

algebra are not sufficient for their study. In particular, solutions to a nonlinear differential equation do not form a vector space (*e.g.*, the sum of two solutions is not a solution in general).

When the polynomial $p(t)$ factors, the operator $p(D)$ factors in a similar way: if
$$p(t) = (t - c_1)\cdots(t - c_n), \tag{2.2}$$
then
$$p(D) = (D - c_1 I)\cdots(D - c_n I). \tag{2.3}$$
Here $D - cI$ is the operator sending $y$ to $y' - cy$.

**Example 2.2.** The polynomial $p(t) = t^2 - 2t - 3$ factors as $(t + 1)(t - 3)$ and $p(D) = (D + I)(D - 3I)$:
$$\begin{aligned}
(D + I)(D - 3I)(y) &= (D + I)(y' - 3y) \\
&= (y' - 3y)' + (y' - 3y) \\
&= y'' - 2y' - 3y \\
&= p(D)(y).
\end{aligned}$$

Equation (2.3) expresses $p(D)$ as a composite of first-order differential operators $D - c_j I$. This decomposition of $p(D)$ will reduce the study of $n$-th order constant-coefficient differential equations to the study of first-order constant-coefficient differential equations by a clever use of linear algebra on an infinite-dimensional space.

Real polynomials do not always factor into linear factors with real coefficients, but the fundamental theorem of algebra tells us that complex polynomials always factor into linear factors with complex coefficients (so, in particular, real polynomials always factor into linear factors with complex coefficients). Therefore we generalize our point of view and consider equations like (1.1) with *complex* coefficients in order to have the factorization (2.3) available. For example, if $y'' + y = 0$ then $(D^2 + I)(y) = 0$ and the corresponding polynomial is $t^2 + 1$, which factors as $(t + i)(t - i)$. We want to regard $y'' + y$ as $(D + iI)(D - iI)(y)$, and a meaning has to be given to $D + iI$ and $D - iI$.

When we allow complex coefficients in (1.1), we should no longer restrict solutions $y$ to real-valued functions. For instance, the differential equation $y' - iy = 0$ has the interesting complex solution $y(t) = \cos t + i \sin t$, while the only real-valued solution of $y' - iy = 0$ is the zero function $y(t) = 0$. Even if we only started out caring about real-valued solutions with real coefficients in (1.1), factoring $p(t)$ into complex linear factors forces the complex case on us for mathematical reasons. From now on, we consider (1.1) with complex coefficients.

Let $C^\infty(\mathbf{R}, \mathbf{C})$ be the set of infinitely-differentiable functions $f: \mathbf{R} \to \mathbf{C}$. The domain is still $\mathbf{R}$; only the range has been enlarged. From now on $D = \mathrm{d}/\mathrm{d}t$ is the differentiation operator on $C^\infty(\mathbf{R}, \mathbf{C})$: if $f(t) = g(t) + ih(t)$, where $g(t)$ and $h(t)$ are real-valued, then $f'(t) = g'(t) + ih'(t)$. Differentiation on complex-valued functions $f: \mathbf{R} \to \mathbf{C}$ satisfies the sum rule and the product rule. Moreover, if $f$ has derivative $0$ then $f$ is constant (since $g$ and $h$ have derivative $0$, so they are constant from real calculus). Every complex-valued solution to (1.1) has at least $n$ derivatives, and by induction all solutions are in fact infinitely differentiable just as in the real case, so solutions to (1.1) lie in $C^\infty(\mathbf{R}, \mathbf{C})$. Equation (2.2) implies (2.3) when the roots $c_j$ are complex.

For $c \in \mathbf{R}$, the real solutions to the differential equation $y' = cy$ are the real scalar multiples of $e^{ct}$. A similar result holds if $c \in \mathbf{C}$:

<!-- page 3 -->

**Theorem 2.3.** *For $c \in \mathbf{C}$, the solutions to $y' = cy$ are the functions $y(t) = re^{ct}$ for $r \in \mathbf{C}$.*

*Proof.* Since $(e^{ct})' = ce^{ct}$, every function $y = re^{ct}$ satisfies $y' = cy$. Conversely, suppose $y' = cy$. Then the ratio $y/e^{ct}$ has derivative $(e^{ct}y' - y(e^{ct})')/(e^{ct})^2 = (e^{ct}cy - yce^{ct})/(e^{ct})^2 = 0$, so $y/e^{ct}$ is a constant. Call the constant $r$, so $y = re^{ct}$. $\square$

The equation $y' = cy$ is the same as $y' - cy = 0$, so $D - cI$ on $C^\infty(\mathbf{R}, \mathbf{C})$ has a one-dimensional kernel with $e^{ct}$ as a basis:
$$\ker(D - cI) = \mathbf{C}e^{ct}.$$
For example, the solution space of $y' = y$ is $\mathbf{C}e^t$ and not just $\mathbf{R}e^t$. For other differential equations like $y' = iy$, with honest complex coefficients, there may be no real-valued solutions besides the zero function while there are nonzero complex solutions.

Our study of (1.1) currently stands as follows. Solutions to (1.1), which lie in $C^\infty(\mathbf{R}, \mathbf{C})$, form the kernel of the differential operator $p(D)$. By the fundamental theorem of algebra and (2.3), $p(D)$ factors into a product of first-order operators. We know the kernel of the first-order differential operator $D - cI$: it is one-dimensional with basis $e^{ct}$.

Our *goal* is to prove, roughly, that the complex solution space to (1.1) has dimension $n$ over $\mathbf{C}$. In down-to-earth terms, this means there are $n$ "basic" solutions to (1.1) in $C^\infty(\mathbf{R}, \mathbf{C})$ such that the general solution is a linear combination of these $n$ basic solutions and none of these $n$ basic solutions is a linear combination of the other basic solutions. In linear algebra terms, this means an $n$-th order constant-coefficient linear differential operator $p(D)$ has an $n$-dimensional kernel in $C^\infty(\mathbf{R}, \mathbf{C})$. While this second description sounds more technical, it is the right way to think about the solutions of (1.1) in order to reach our goal. (Our goal does *not* include the explicit description of all solutions to (1.1). All we want to do is compute the dimension of the solution space.)

## 3. The Complex Case

To bootstrap our knowledge from the first-order differential operators $D - cI$ to the $n$-th order differential operators $p(D)$, we will use the following property of the operators $D - cI$.

**Lemma 3.1.** *For each $c \in \mathbf{C}$, $D - cI$ is onto. That is, for every $f \in C^\infty(\mathbf{R}, \mathbf{C})$, there is a $u \in C^\infty(\mathbf{R}, \mathbf{C})$ such that $u' - cu = f$.*

*Proof.* First, we check the special case $c = 0$, which says for every $f$ there is a $u$ such that $u' = f$. This is just a matter of antidifferentiating real and imaginary parts. Indeed, write $f(t) = a(t) + ib(t)$ and choose antiderivatives for $a(t)$ and $b(t)$, say $A(t) = \int_0^t a(x)\,\mathrm{d}x$ and $B(t) = \int_0^t b(x)\,\mathrm{d}x$. Then $u(t) = A(t) + iB(t)$ has derivative $a(t) + ib(t) = f(t)$. Since $f(t)$ is infinitely differentiable and $u' = f$, so is $u$. We're done with the case $c = 0$.

Now we show each $D - cI$ is onto, *i.e.*, the differential equation $u' - cu = f$, where $f$ is given, has a solution $u$ in $C^\infty(\mathbf{R}, \mathbf{C})$. The strategy is to reduce to the previously treated case $c = 0$ by a "change of coordinates." Multiply through the equation by $e^{-ct}$ (which is an invertible procedure, since $e^{ct}$ is a nonvanishing function):
$$e^{-ct}u' - ce^{-ct}u = e^{-ct}f.$$
By the product rule, this equation is the same as
$$(e^{-ct}u)' = e^{-ct}f.$$
This equation has the form $v' = g$, where $g = e^{-ct}f$ is given and $v$ is sought. That is the case treated in the previous paragraph: pick antiderivatives for the real and imaginary parts

<!-- page 4 -->

of $g(t)$ to get an antiderivative $v(t)$ for $g(t)$, and then multiply $v(t)$ by $e^{ct}$ to find a solution $u$. $\square$

Lemma 3.1 tells us the first-order inhomogeneous differential equation $u' - cu = f$ can always be solved when $f \in C^\infty(\mathbf{R}, \mathbf{C})$.

The next lemma has nothing to do with differential equations. It is only about linear algebra.

**Lemma 3.2.** *Let $V$ be a vector space over a field $F$. Let $T: V \to V$ and $U: V \to V$ be linear operators on $V$ such that $\ker(T)$ and $\ker(U)$ are finite-dimensional. Assume $U$ is onto. Then $\ker(TU)$ is finite-dimensional and*
$$\dim \ker(TU) = \dim \ker(T) + \dim \ker(U).$$

This lemma is tricky because your first guess about how to prove it does not work: it is *not* the case that a basis of $\ker(T)$ and a basis of $\ker(U)$ combine to give a basis of $\ker(TU)$. For instance, let $T$ and $U$ both be $D = \mathrm{d}/\mathrm{d}t$ on $C^\infty(\mathbf{R}, \mathbf{C})$ (or even on $C^\infty(\mathbf{R})$, if you want to work in a more familiar setting). Both $\ker(T)$ and $\ker(U)$ consist of constant functions, but the kernel of $TU = D^2 = \mathrm{d}^2/\mathrm{d}t^2$ has basis $\{1, t\}$, so it is not spanned by constant functions.

*Proof.* This proof might at first appear overly technical. If you need motivation to care about the proof, see below how this lemma is applied to differential equations. Then come back and read the proof.

Write $m = \dim \ker(T)$ and $n = \dim \ker(U)$. We want to prove $\dim \ker(TU) = m + n$. Notice we do not even know yet that $\ker(TU)$ is finite-dimensional. First we will prove $\ker(TU)$ is finite-dimensional, with a spanning set of $m + n$ vectors, so $\dim \ker(TU) \leq m + n$. Then we will prove the spanning set we find for $\ker(TU)$ is linearly independent, so $\dim \ker(TU) = m + n$.

Let $v_1, \ldots, v_m$ be a basis of $\ker(T)$ and $w_1, \ldots, w_n$ be a basis of $\ker(U)$.

For $v \in \ker(TU)$, the equation $(TU)(v) = 0$ says $T(Uv) = 0$, so $Uv$ is in the kernel of $T$:
$$Uv = c_1 v_1 + \cdots + c_m v_m$$
for some $c_1, \ldots, c_m \in F$.

To get anywhere with this equation, we use the hypothesis that $U$ is *onto* to write the $v_i$'s in another way. Since $U: V \to V$ is onto, we can write $v_i = U(\widetilde{v}_i)$ for some $\widetilde{v}_i$ in $V$. Then the above equation becomes
$$\begin{aligned}
Uv &= c_1 U(\widetilde{v}_1) + \cdots + c_m U(\widetilde{v}_m) \\
&= U(c_1 \widetilde{v}_1 + \cdots + c_m \widetilde{v}_m).
\end{aligned}$$
When $U$ takes the same value at two vectors, the difference of those vectors is in the kernel of $U$ (just subtract and compute). Therefore
$$v = c_1 \widetilde{v}_1 + \cdots + c_m \widetilde{v}_m + v', \tag{3.1}$$
where $v' \in \ker(U)$. Writing $v'$ in terms of the basis $w_1, \ldots, w_n$ of $\ker(U)$ and feeding this into (3.1), we have
$$v = c_1 \widetilde{v}_1 + \cdots + c_m \widetilde{v}_m + d_1 w_1 + \cdots + d_n w_n$$
for some $d_1, \ldots, d_n \in F$.

<!-- page 5 -->

We have written a general element $v$ of $\ker(TU)$ as a linear combination of $m + n$ vectors: the $\widetilde{v}_i$'s and the $w_j$'s. Moreover, the $\widetilde{v}_i$'s and $w_j$'s are in $\ker(TU)$:
$$(TU)(\widetilde{v}_i) = T(U\widetilde{v}_i) = T(v_i) = 0, \quad (TU)(w_j) = T(Uw_j) = T(0) = 0.$$
Since we have shown the $\widetilde{v}_i$'s and $w_j$'s are a spanning set for $\ker(TU)$, this kernel has dimension at most $m + n$.

To prove $\widetilde{v}_1, \ldots, \widetilde{v}_m, w_1, \ldots, w_n$ is a linearly independent set, suppose some $F$-linear combination is $0$:
$$c_1 \widetilde{v}_1 + \cdots + c_m \widetilde{v}_m + d_1 w_1 + \cdots + d_n w_n = 0. \tag{3.2}$$
Applying $U$ to this equation turns each $\widetilde{v}_i$ into $U(\widetilde{v}_i) = v_i$ and turns each $w_j$ into $U(w_j) = 0$, so we find
$$c_1 v_1 + \cdots + c_m v_m = 0.$$
The $v_i$'s are (by their definition) linearly independent, so each $c_i$ is $0$. This turns (3.2) into
$$d_1 w_1 + \cdots + d_n w_n = 0.$$
Now, since the $w_j$'s are (by their definition) linearly independent, each $d_j$ is $0$. Thus the set $\{\widetilde{v}_1, \ldots, \widetilde{v}_m, w_1, \ldots, w_n\}$ spans $\ker(TU)$ and is linearly independent, so $\ker(TU)$ has dimension $m + n$. $\square$

**Remark 3.3.** If $V$ is finite-dimensional, there is another proof of Lemma 3.2, using the rank-nullity theorem. However, we will not discuss this alternate proof for finite-dimensional $V$ because Lemma 3.2 for finite-dimensional $V$ is *useless* for our intended application to differential equations: the basic space of interest, $C^\infty(\mathbf{R}, \mathbf{C})$, is not finite-dimensional. This is a good reason that linear algebra must not be developed exclusively on finite-dimensional vector spaces: important applications of the *ideas* of linear algebra occur in contexts where the spaces are infinite-dimensional. This is especially true in applications of linear algebra to analysis (differential equations, integral equations, Fourier series) and physics (quantum mechanics).

There is a version of Lemma 3.2 even if $U$ is not onto. However, a new idea has to be introduced, the notion of the index of a linear operator. Lemma 3.2 generalizes to: the index of a product of operators is the sum of the indices. You can read about this in textbooks on functional analysis (specifically, look up Fredholm operators).

Now we are ready to prove our goal: the dimension of the solution space of (1.1) is $n$. The proof is deceptively short. All the hard work has gone into the preliminary results.

**Theorem 3.4.** *Let $p(t)$ be a polynomial of the form (2.1) with complex coefficients of degree $n \geq 1$ and let $p(D)$ be the corresponding $n$-th order linear differential operator with constant coefficients. The solution space to $p(D)(y) = 0$ in $C^\infty(\mathbf{R}, \mathbf{C})$ is $n$-dimensional, or equivalently $\ker(p(D))$ has dimension $n$.*

*Proof.* We induct on $n$, the degree of the polynomial $p(t)$. The case $n = 1$ says: for $c \in \mathbf{C}$, the operator $D - cI$ on $C^\infty(\mathbf{R}, \mathbf{C})$ has a one-dimensional kernel. That is, the equation $y' - cy = 0$ has a one-dimensional solution space. We saw this before by explicit methods: the solution space is $\mathbf{C}e^{ct}$ and has dimension $1$.

Now assume the theorem is proved whenever $p(t)$ has degree $n$. Let $p(t)$ have degree $n + 1$. We will prove $\ker(p(D))$ has dimension $n + 1$.

By the fundamental theorem of algebra,
$$p(t) = (t - c_1)(t - c_2)\cdots(t - c_n)(t - c_{n+1})$$

<!-- page 6 -->

for some complex numbers $c_1, \ldots, c_{n+1}$. (Some of the $c_j$'s may be equal, but that doesn't matter for our purposes.) Set $q(t) = (t - c_1)\cdots(t - c_n)$, so $p(t) = q(t)(t - c_{n+1})$. Therefore
$$p(D) = q(D)(D - c_{n+1}I).$$
By the inductive hypothesis, $\ker(q(D))$ has dimension $n$. By the base case, $\ker(D - c_{n+1}I)$ has dimension $1$.

We now apply Lemma 3.2, taking $V = C^\infty(\mathbf{R}, \mathbf{C})$, $T = q(D)$ and $U = D - c_{n+1}I$. The hypothesis in Lemma 3.2 that $U$ is onto is true by Lemma 3.1. Thus, Lemma 3.2 tells us $p(D)$ has a finite-dimensional kernel, with
$$\dim_{\mathbf{C}}(p(D)) = \dim_{\mathbf{C}}(q(D)) + \dim_{\mathbf{C}}(D - c_{n+1}I) = n + 1.$$
We're done! $\square$

This a rather curious state of affairs. We have computed the size (*i.e.*, the dimension) of the complex solution space to each constant-coefficient linear differential equation of the form (1.1), but we have not indicated what the solutions are when $n > 1$! A careful rereading will show the proofs of Lemmas 3.1 and 3.2 are constructive, so the proof of Theorem 3.4 really can be used to list a basis for the solution space of (1.1) when we factor $p(t)$. We will now see in some examples how to follow the method of proof of Lemma 3.2 to build a basis of $\ker(TU)$ from bases of $\ker(T)$ and $\ker(U)$.

**Example 3.5.** Consider $y'' - 2y' - 3y = 0$. The polynomial is $p(t) = t^2 - 2t - 3 = (t + 1)(t - 3)$. Take $T = D + I$ and $U = D - 3I$, so $p(D) = TU$. A basis of $\ker(T)$ is $e^{-t}$ and a basis of $\ker(U)$ is $e^{3t}$. As in the proof of Lemma 3.2, we write $e^{-t} = U(\widetilde{v}) = \widetilde{v}' - 3\widetilde{v}$ and want to solve for $\widetilde{v}$. First try $\widetilde{v} = e^{-t}$: $(e^{-t})' - 3(e^{-t}) = 2e^{-t}$. This didn't work, but if we scale and instead use $\widetilde{v} = (1/2)e^{-t}$ then it works. So a basis of $\ker(p(D))$ is $\{e^{3t}, (1/2)e^{-t}\}$, and by scaling another basis is $\{e^{3t}, e^{-t}\}$. The general solution to $y'' - 2y' - 3y = 0$ is a linear combination of $e^{3t}$ and $e^{-t}$.

**Example 3.6.** Consider $y'' - 2y' + y = 0$. The polynomial is $p(t) = t^2 - 2t + 1 = (t - 1)^2$, which has $1$ as a double root. Take $T = D - I$ and $U = D - I$, so $p(D) = TU$. A basis of $\ker(T) = \ker(U)$ is $e^t$. Writing $e^t = U(\widetilde{v}) = \widetilde{v}' - \widetilde{v}$, the function $\widetilde{v} = te^t$ works (check!) and therefore a basis of $\ker(p(D))$ is $\{e^t, te^t\}$.

**Example 3.7.** Consider $y'' + y = 0$. The polynomial is $p(t) = t^2 + 1 = (t + i)(t - i)$. Take $T = D + iI$ and $U = D - iI$, so $p(D) = TU$. A basis of $\ker(T)$ is $e^{-it}$ and a basis of $\ker(U)$ is $e^{it}$. Writing $e^{-it} = U(\widetilde{v}) = \widetilde{v}' - i\widetilde{v}$, we first try $\widetilde{v} = e^{-it}$. However, $(e^{-it})' - i(e^{-it}) = -2ie^{-it} \neq e^{-it}$. If we scale and use $\widetilde{v} = -(1/2i)e^{-it}$ then it works. Thus a basis of $\ker(TU)$ is $\{e^{it}, -(1/2i)e^{-it}\}$, and by scaling again another basis is $\{e^{it}, e^{-it}\}$. Another basis obtained from this one is $\{(e^{it} + e^{-it})/2, (e^{it} - e^{-it})/2i\} = \{\cos t, \sin t\}$, which looks more familiar as the basic real solution of $y'' + y = 0$. The general solution to $y'' + y = 0$ is a linear combination of $\cos t$ and $\sin t$.

**Remark 3.8.** A general constant-coefficient linear differential operator could have a coefficient $a_n \neq 1$ in front of $D^n$. Since scaling a linear differential operator by a nonzero constant (like $1/a_n$) does not change the kernel or the order of the differential operator, and makes the coefficient of $D^n$ equal to $1$, our treatment of the "special" case $a_n = 1$ was more or less a treatment of the general case.

<!-- page 7 -->

## 4. The Real Case

If the differential equation (1.1) has real coefficients, we are naturally interested in the real solutions, not all complex solutions. The above examples suggest that the complex solution space will have a basis of real-valued functions (although in the last example we had to work a little to find it), so one may hope that the real solution space has dimension $n$. This is true:

**Theorem 4.1.** *Let $p(t)$ be a polynomial with real coefficients of degree $n \geq 1$ and let $p(D)$ be the corresponding $n$-th order linear differential operator with constant coefficients. The solution space to $p(D)(y) = 0$ in $C^\infty(\mathbf{R})$ is $n$-dimensional.*

The basic idea behind Theorem 4.1 is that under fairly general circumstances a "real" linear operator acting on a complex vector space has a real kernel of the same dimension (over $\mathbf{R}$) as the dimension of its complex kernel (over $\mathbf{C}$). For example, a differential operator with real coefficients sends real functions to other real functions, so it should be considered a "real" operator. An example of a differential operator that is not "real" is $D - iI$, which sends $y(t)$ to $y'(t) - iy(t)$. Real functions don't get sent to real functions by this operator (in general), and the differential equation $y' - iy = 0$ has complex solution space $\mathbf{C}e^{it}$ of dimension $1$ over $\mathbf{C}$ and real solution space $\{0\}$ of dimension $0$ over $\mathbf{R}$. So the two dimensions don't match!

To determine the dimension of the real solution space from the dimension of the complex solution space requires another detour back through linear algebra. We temporarily forget about differential equations and will return to them after Lemma 4.8 below.

Let $V$ be a vector space over the complex numbers. We can consider $V$ as a *real* vector space by considering scaling by real numbers only. For instance, the complex scalar multiple $(2 + 3i)v$ is viewed as $2v + 3(iv)$, which is a real linear combination of $v$ and $iv$.

**Lemma 4.2.** *A complex vector space $V$ is finite dimensional over $\mathbf{C}$ if and only if it is finite dimensional over $\mathbf{R}$, in which case $\dim_{\mathbf{R}}(V) = 2\dim_{\mathbf{C}}(V)$. More precisely, if $V \neq \{0\}$ and $\{v_1, \ldots, v_n\}$ is a $\mathbf{C}$-basis of $V$, then*
$$\{v_1, iv_1, v_2, iv_2, \ldots, v_n, iv_n\} \tag{4.1}$$
*is an $\mathbf{R}$-basis of $V$.*

*Proof.* The result is clear if $V$ is $0$, so take $V$ nonzero.

If $V$ is finite dimensional over $\mathbf{R}$ then a finite basis of $V$ as a real vector space is a spanning set of $V$ as a complex vector space, so $V$ is finite dimensional over $\mathbf{C}$.

Conversely, suppose $V$ is finite dimensional over $\mathbf{C}$ with basis $\{v_1, \ldots, v_n\}$. We will show the set in (4.1) is a basis of $V$ as a vector space over $\mathbf{R}$, so $\dim_{\mathbf{R}}(V) = 2n$.

**Spanning set:** Each $v \in V$ is a $\mathbf{C}$-linear combination of $\{v_1, v_2, \ldots, v_n\}$, say
$$v = (a_1 + b_1 i)v_1 + (a_2 + b_2 i)v_2 + \cdots + (a_n + b_n i)v_n$$
for some complex numbers $a_j + ib_j$. Distributing the scalar multiplication,
$$v = a_1 v_1 + b_1(iv_1) + a_2 v_2 + b_2(iv_2) + \cdots + a_n v_n + b_n(iv_n).$$
This exhibits $v$ as a real linear combination of $\{v_1, iv_1, \ldots, v_n, iv_n\}$, so this set is a spanning set of $V$ over $\mathbf{R}$.

**Linear Independence:** Suppose in $V$ that
$$c_1 v_1 + c_1'(iv_1) + c_2 v_2 + c_2'(iv_2) + \cdots + c_n v_n + c_n'(iv_n) = 0$$

<!-- page 8 -->

for real $c_j$ and $c_j'$. We want to show each $c_j$ and $c_j'$ is $0$. Rewrite the equation as
$$(c_1 + ic_1')v_1 + (c_2 + ic_2')v_2 + \cdots + (c_n + ic_n')v_n = 0.$$
Since $\{v_1, \ldots, v_n\}$ are linearly independent over $\mathbf{C}$, each $c_j + ic_j'$ is $0$. Therefore each $c_j$ and $c_j'$ is $0$ because a complex number is $0$ only when its real and imaginary parts are $0$. $\square$

**Definition 4.3.** Let $V$ be a vector space over $\mathbf{C}$. A *conjugation* on $V$ is an operation $V \to V$, denoted $v \mapsto v^*$, with the following three properties:

- For all $v_1, v_2 \in V$, $(v_1 + v_2)^* = v_1^* + v_2^*$.
- For all $v \in V$ and $z \in \mathbf{C}$, $(zv)^* = \overline{z}v^*$ (*not* $zv^*$).
- For all $v \in V$, $(v^*)^* = v$.

In the following examples, you will see that a conjugation on a concrete complex vector space is typically just the operation of taking the complex conjugate of the coordinates (when the vector space is defined through a device like coordinates).

**Example 4.4.** Take $V = \mathbf{C}^n$. For $v = (z_1, \ldots, z_n)$ in $\mathbf{C}^n$, set $v^* = (\overline{z}_1, \ldots, \overline{z}_n)$. That is, $v^*$ is just the vector with coordinates that are complex conjugates of the coordinates of $v$.

**Example 4.5.** Take $V = \mathrm{M}_n(\mathbf{C})$. For $A = (a_{ij})$ in $\mathrm{M}_n(\mathbf{C})$, set $A^* = (\overline{a}_{ij})$. That is, $A^*$ is the matrix with components that are complex conjugates of those for $A$.

**Example 4.6.** A second conjugation on $\mathrm{M}_n(\mathbf{C})$ is $(a_{ij})^* = (\overline{a}_{ji})$. Here $A^*$ is the conjugate of the transposed matrix.

**Example 4.7.** Take $V = C^\infty(\mathbf{R}, \mathbf{C})$. For $y(t) = a(t) + ib(t) \in C^\infty(\mathbf{R}, \mathbf{C})$, let $y^*$ be the function $y^*(t) = \overline{y(t)} = a(t) - ib(t)$. For example, if $f(t) = \sin t + ie^t$, then $f^*(t) = \sin t - ie^t$.

When $V$ is a complex vector space with a conjugation operation, set
$$V^+ = \{v \in V : v^* = v\}.$$
Here is what this means in the above examples. When $V = \mathbf{C}^n$, $V^+$ is the set of $n$-tuples whose coordinates are real, so $V^+ = \mathbf{R}^n$. When $V = \mathrm{M}_n(\mathbf{C})$ in Example 4.5, $V^+$ is the set of $n \times n$ matrices with real entries: $V^+ = \mathrm{M}_n(\mathbf{R})$. When $V = \mathrm{M}_n(\mathbf{C})$ in Example 4.6, $V^+$ is the set of matrices $(a_{ij})$ such that $\overline{a}_{ji} = a_{ij}$. These are the complex matrices whose diagonal terms are real and whose components symmetric across the main diagonal are complex conjugates of each other. (Examples 4.5 and 4.6 remind us that the meaning of $V^+$ depends on the specific conjugation used on $V$.) Finally, when $V = C^\infty(\mathbf{R}, \mathbf{C})$, $V^+$ is the set of functions $y(t) = a(t) + ib(t)$ such that $b(t) = 0$. That is, $V^+ = C^\infty(\mathbf{R})$.

Notice $V^+$ is not a complex vector space since $V^+$ is not closed under complex scaling. For instance, in Example 4.4, $\mathbf{R}^n$ is not a complex subspace of $\mathbf{C}^n$. (In general, for all nonzero $v \in V^+$, $iv$ is not in $V^+$ since $(iv)^* = \overline{i}v^* = -iv$ is not $iv$ again.) However, $V^+$ is a subspace of $V$ as a real vector space. For instance, $\mathbf{R}^n$ is a subspace of $\mathbf{C}^n$ when we view $\mathbf{C}^n$ as a real vector space.

**Lemma 4.8.** *Suppose $V$ is a vector space over $\mathbf{C}$ and has a conjugation defined on it. Then $V$ is finite-dimensional over $\mathbf{C}$ if and only if $V^+$ is finite-dimensional over $\mathbf{R}$, and when the spaces are finite dimensional each $\mathbf{R}$-basis of $V^+$ is a $\mathbf{C}$-basis of $V$. In other words, $\dim_{\mathbf{R}}(V^+) = \dim_{\mathbf{C}}(V)$.*

Don't confuse the conclusions of Lemmas 4.2 and 4.8. Consider $V = \mathbf{C}$ with conjugation $z \mapsto \overline{z}$: it has real dimension $2$ and $V^+ = \mathbf{R}$ has real dimension $1$.

<!-- page 9 -->

*Proof.* First suppose $\dim_{\mathbf{C}}(V)$ is finite. Then if we view $V$ as a real vector space, it is finite-dimensional with $\dim_{\mathbf{R}}(V) = 2\dim_{\mathbf{C}}(V)$ by Lemma 4.2. Since $V^+$ is a *subspace* of $V$ as a real vector space, it follows that $V^+$ is a finite-dimensional real vector space.

Conversely, suppose $\dim_{\mathbf{R}}(V^+)$ is finite and $v_1, \ldots, v_n$ is a basis of $V^+$ over $\mathbf{R}$. We will prove $v_1, \ldots, v_n$ is a basis of $V$ over $\mathbf{C}$.

First we treat linear independence over $\mathbf{C}$. Suppose
$$c_1 v_1 + \cdots + c_n v_n = 0, \tag{4.2}$$
where $c_j = a_j + ib_j$. Applying the conjugation operation,
$$\overline{c}_1 v_1^* + \cdots + \overline{c}_n v_n^* = 0.$$
Since each $v_j$ is in $V^+$, $v_j^* = v_j$, so the above equation becomes
$$\overline{c}_1 v_1 + \cdots + \overline{c}_n v_n = 0. \tag{4.3}$$
Write $c_j = a_j + ib_j$ ($a_j, b_j \in \mathbf{R}$). Adding (4.2) and (4.3) kills off the imaginary parts of the $c_j$'s, and leaves us with
$$2a_1 v_1 + \cdots + 2a_n v_n = 0.$$
Since the $v_j$'s are linearly independent over $\mathbf{R}$, each $a_j$ is $0$. Similarly, subtracting (4.3) from (4.2) gives
$$i2b_1 v_1 + \cdots + i2b_n v_n = 0.$$
Dividing by $i$ converts this into a real linear combination of the $v_j$'s equal to $0$, and therefore each $b_j$ is $0$. That proves $c_j = a_j + ib_j$ is $0$ for $j = 1, 2, \ldots, n$, which settles the linear independence.

Now we want to show $\{v_1, \ldots, v_n\}$ spans $V$ over the complex numbers. Choose $v \in V$. We want to find complex $c_1, \ldots, c_n$ such that
$$v = c_1 v_1 + \cdots + c_n v_n.$$
To show this can be done, notice that the conjugation operation on $V$ is $\mathbf{R}$-linear (but not $\mathbf{C}$-linear) and satisfies $(v^*)^* = v$, so we can write
$$v = w_1 + iw_2,$$
where $w_1^* = w_1$ and $w_2^* = w_2$. Concretely, $w_1 = (1/2)(v + v^*)$ and $w_2 = (1/2i)(v - v^*)$. (This is like the formulas for the real and imaginary parts of a complex number $z = x + iy$: $x = (1/2)(z + \overline{z})$ and $y = (1/2i)(z - \overline{z})$.) Thus, $w_1$ and $w_2$ are in $V^+$. Using the basis $v_1, \ldots, v_n$ of $V^+$,
$$w_1 = a_1 v_1 + \cdots + a_n v_n, \quad w_2 = b_1 v_1 + \cdots + b_n v_n,$$
where $a_j, b_j \in \mathbf{R}$. Thus,
$$\begin{aligned}
v &= w_1 + iw_2 \\
&= (a_1 v_1 + \cdots + a_n v_n) + i(b_1 v_1 + \cdots + b_n v_n) \\
&= (a_1 + ib_1)v_1 + \cdots + (a_n + ib_n)v_n,
\end{aligned}$$
so each $v \in V$ is a $\mathbf{C}$-linear combination of the $v_j$'s. That shows the $v_j$'s span $V$ over $\mathbf{C}$. $\square$

Finally we are ready to prove Theorem 4.1.

<!-- page 10 -->

*Proof.* Let $p(D)$ be a constant-coefficient linear differential operator of order $n$ with real coefficients. We want to show the real solution space to $p(D)(y) = 0$, which is a real vector space, has dimension $n$ over $\mathbf{R}$.

Let $V$ be the complex solution space to $p(D)(y) = 0$ in $C^\infty(\mathbf{R}, \mathbf{C})$. Therefore $V$ has dimension $n$ as a complex vector space, by Theorem 3.4.

Write $p(D) = D^n + a_{n-1}D^{n-1} + \cdots + a_1 D + a_0 I$, with real $a_j$. Then the differential equation $p(D)(y) = 0$, when written out in full, is (1.1). When $y$ satisfies (1.1), so does the conjugate function $\overline{y}$. Indeed, $\overline{y^{(j)}} = \overline{y}^{(j)}$ and $\overline{a}_j = a_j$, so conjugating the differential equation shows $\overline{y}$ satisfies the differential equation. (This is *false* if the $a_j$ are not all real, *e.g.*, solutions to $y' - iy = 0$ are usually not again solutions to the same equation after conjugation.)

Since conjugates of complex solutions to $p(D)(y) = 0$ are again solutions, we can apply Lemma 4.8 to $V = C^\infty(\mathbf{R}, \mathbf{C})$ with its conjugation operation: it tells us the subset $V^+$ is an $n$-dimensional real vector space. Since $\overline{y} = y$ if and only if $y$ is in $C^\infty(\mathbf{R})$, $V^+$ is the real solution space to $p(D)(y) = 0$, so we have proved the real solution space to (1.1) is $n$-dimensional (over $\mathbf{R}$). $\square$

Theorem 4.1 is a good example of the benefits of first working over $\mathbf{C}$. Even if we are only interested in real solutions of real differential equations, the way that one computes the dimension of the real solution space is to first prove a corresponding result for complex solutions (as a complex vector space) and then use that to determine the dimension of the real solution space.

## 5. Equations With Initial Conditions

Now that we have existence of solutions, we can prove uniqueness of solutions given enough initial conditions. We will consider as initial conditions a specification of the values $y(0), y'(0), \ldots, y^{(n-1)}(0)$. These are $n$ pieces of information.

**Lemma 5.1.** *If $y$ satisfies (1.1) and $y^{(j)}(0) = 0$ for $0 \leq j \leq n - 1$ then $y(t) = 0$ for all $t$.*

*Proof.* We argue by induction on the order of the differential equation. When $n = 1$, the equation is $y' + ay = 0$, whose general solution is $y(t) = re^{-at}$ for some constant $r$. So if $y(0) = 0$ then $r = 0$ and $y(t) = 0$ for all $t$.

Now suppose $n \geq 2$ and the lemma is proved for constant-coefficient linear differential equations of order $n - 1$. Write (1.1) as $p(D)(y) = 0$ and split off one linear factor from the polynomial $p(t)$: $p(t) = q(t)(t - c)$, where $q(t)$ has degree $n - 1$. Then $p(D) = q(D)(D - cI)$, so $p(D)(y) = q(D)(D - cI)(y) = q(D)(y' - cy)$. The differential equation (1.1) now looks like
$$q(D)(y' - cy) = 0,$$
which may look more complicated, but it really helps because it tells us that $y' - cy$ is the solution of a differential equation of order $n - 1$ (since $q(D)$ is a differential operator of order $n - 1$). Moreover, for $0 \leq j \leq n - 2$ we have $(y' - cy)^{(j)}(0) = y^{(j+1)}(0) - cy^{(j)}(0) = 0 - c \cdot 0 = 0$. (We needed $j \leq n - 2$ so $j + 1 \leq n - 1$ and therefore $y^{(j+1)}(0) = 0$. So $y' - cy$ has its derivatives at $0$ through order $n - 2$ equal to $0$, hence by induction $y' - cy$ is the zero function. Now by the base case we get from this that $y(t)$ is the zero function. $\square$

**Theorem 5.2.** *For every $b_0, b_1, \ldots, b_{n-1} \in \mathbf{C}$, there is a unique solution to (1.1) satisfying $y^{(j)}(0) = c_j$ for $0 \leq j \leq n - 1$.*

<!-- page 11 -->

*Proof.* First we check uniqueness, and then existence.

**Uniqueness.** If $y$ and $z$ are two solutions to (1.1) satisfying the same initial conditions, then the difference $y - z$ is a solution whose initial conditions are all $0$, so by Lemma 5.1 we have $y(t) - z(t) = 0$ for all $t$, hence $y$ and $z$ are the same function.

**Existence.** Consider the linear map that turns a solution of (1.1) into its initial conditions: $y(t) \mapsto (y(0), y'(0), \ldots, y^{(n-1)}(0)) \in \mathbf{C}^n$. This is a $\mathbf{C}$-linear transformation from the $n$-dimensional solution space to $\mathbf{C}^n$. Lemma 5.1 tells us the transformation has kernel $0$, so it is injective. Both the solution space and $\mathbf{C}^n$ have the same dimension, so injectivity implies surjectivity. That's a fancy way of saying any given set of initial conditions is satisfied by some solution of (1.1). So we're done. $\square$

This treatment of linear differential equations has only covered equations with (real) constant coefficients. The coefficients of a linear differential equation could be functions:
$$y^{(n)} + a_{n-1}(t)y^{(n-1)} + \cdots + a_1(t)y' + a_0(t)y = 0. \tag{5.1}$$
A particular example is
$$y'' + (t^2 - t)y' - (\sin t)y = 0.$$
Even if the coefficients are varying with $t$, this differential equation is still linear in $y$: solutions to such a differential equation form a vector space under addition and scaling: the real solutions form a real vector space and the complex solutions form a complex vector space. When the coefficients $a_j(t)$ are continuous functions $I \to \mathbf{R}$ on an open interval $I$ in $\mathbf{R}$, the complex solution space is $n$-dimensional over $\mathbf{C}$ and the real solution space is $n$-dimensional over $\mathbf{R}$. (By Lemma 4.8, these dimension calculations for the real and complex solution spaces are equivalent.)

Our proof of the dimension calculation in the constant-coefficient case does not apply to the case of non-constant coefficients (why?), so analyzing (5.1) requires ideas from analysis such as fixed-point theorems. This result is found in many general treatments of differential equations. It is usually called a global existence and uniqueness theorem for (5.1) subject to initial conditions on $y$ and its first $n - 1$ derivatives: $y(t_0) = c_0, y'(t_0) = c_1, y''(t_0) = c_2, \ldots, y^{(n-1)}(t_0) = c_{n-1}$, where $t_0 \in I$. That is, there is exactly one solution $y(t)$ satisfying (5.1) together with those initial conditions at $t_0$, and this solution is defined for all $t \in I$. The reason this implies the solution space of (5.1) is $n$-dimensional (for real or complex solutions) is that the collection of $n$ initial conditions (read each row separately)
$$\begin{aligned}
y(t_0) = 1, \quad y'(t_0) = 0, \quad y''(t_0) = 0, \quad &\ldots, \quad y^{(n-1)}(t_0) = 0, \\
y(t_0) = 0, \quad y'(t_0) = 1, \quad y''(t_0) = 0, \quad &\ldots, \quad y^{(n-1)}(t_0) = 0, \\
&\vdots \\
y(t_0) = 0, \quad y'(t_0) = 0, \quad y''(t_0) = 0, \quad &\ldots, \quad y^{(n-1)}(t_0) = 1
\end{aligned}$$
leads to $n$ solutions $y_0(t), y_1(t), \ldots, y_{n-1}(t)$ of (5.1), and an arbitrary set of initial conditions
$$y(t_0) = c_0, \quad y'(t_0) = c_1, \quad y''(t_0) = c_2, \quad \ldots, \quad y^{(n-1)}(t_0) = c_{n-1} \tag{5.2}$$
is satisfied by $c_0 y_0(t) + c_1 y_1(t) + \cdots + c_{n-1} y_{n-1}(t)$, so the uniqueness for solutions of (5.1) implies the only solution satisfying (5.2) is $c_0 y_0(t) + c_1 y_1(t) + \cdots + c_{n-1} y_{n-1}(t)$. Therefore $y_0(t), \ldots, y_{n-1}(t)$ form a basis of the solution space of (5.1).
