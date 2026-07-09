# Representations of $\text{Aff}(\mathbf{F}_q)$ and $\text{Heis}(\mathbf{F}_q)$

> **Source**: https://kconrad.math.uconn.edu/blurbs/grouptheory/affineheisrep.pdf  
> **Author**: Keith Conrad  
> **Topic**: representation_theory

<!-- page 1 -->

For each prime power $q$, we will construct all irreducible representations over $\mathbf{C}$ of the groups $\text{Aff}(\mathbf{F}_q)$ and $\text{Heis}(\mathbf{F}_q)$. To find all of them, there are three parts:

- build as many irreducible representations as the number of conjugacy classes,
- show a representation is irreducible by checking its character has inner product 1 with itself (1-dimensional representations are automatically irreducible),
- show irreducible representations are nonisomorphic by checking their characters are different.

## 1. Representations of $\text{Aff}(\mathbf{F}_q)$

Let $F$ be a field. In $\text{Aff}(F)$, the group law is

$$\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a' & b' \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} aa' & ab' + b \\ 0 & 1 \end{pmatrix}, \quad \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1/a & -b/a \\ 0 & 1 \end{pmatrix}.$$

The notation $\text{Aff}$ means "affine," which is the label in higher math for functions of the form $f(x) = ax + b$, and such functions with $a \neq 0$ compose in the same way matrices $\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$ multiply.

Two subgroups of $\text{Aff}(F)$ are

$$\left\{\begin{pmatrix} a & 0 \\ 0 & 1 \end{pmatrix} : a \neq 0\right\}, \quad \left\{\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} : b \in F\right\},$$

which are isomorphic to $F^\times$ and $F$ as groups. Matrices in $\text{Aff}(F)$ decompose into a product of elements in these subgroups as

$$\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a & 0 \\ 0 & 1 \end{pmatrix}.$$

The product in the other order doesn't work in the same way:

$$\begin{pmatrix} a & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & ab \\ 0 & 1 \end{pmatrix}.$$

Conjugation in $\text{Aff}(F)$ is

$$\begin{pmatrix} x & y \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x & y \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} a & bx - y(a-1) \\ 0 & 1 \end{pmatrix}. \tag{1.1}$$

By (1.1), $\text{Aff}(F)$ has trivial center unless $F = \mathbf{F}_2$, in which case $\text{Aff}(F)$ is abelian.

Here are the conjugacy classes in $\text{Aff}(F)$:

<!-- page 2 -->

- the identity matrix $\left\{\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\right\}$,
- the set $\left\{\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} : b \in F^\times\right\}$,
- for each $a \in F$ with $a \neq 0$ and $a \neq 1$, the set $\left\{\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} : b \in F\right\}$.

Taking $F = \mathbf{F}_q$, in $\text{Aff}(\mathbf{F}_q)$ there are a total of $1 + 1 + (q - 2) = q$ conjugacy classes and thus there are $q$ irreducible representations of $\text{Aff}(\mathbf{F}_q)$ over $\mathbf{C}$.

**One-dimensional representations:** Since the upper left entry in $\text{Aff}(\mathbf{F}_q)$ behaves multiplicatively in the group law, for each homomorphism $\chi: \mathbf{F}_q^\times \to \mathbf{C}^\times$ we get a one-dimensional representation $\text{Aff}(\mathbf{F}_q) \to \mathbf{C}^\times$ by

$$\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} \mapsto \chi(a).$$

Since $\mathbf{F}_q^\times$ is cyclic of order $q - 1$, there are $q - 1$ such $\chi$, so we get $q - 1$ one-dimensional representations of $\text{Aff}(\mathbf{F}_q)$.

**Remaining irreducible representation:** From the count of conjugacy classes there is one more irreducible representation of $\text{Aff}(\mathbf{F}_q)$. Letting $d$ denote its degree, from $q - 1 + d^2 = |\text{Aff}(\mathbf{F}_q)| = q(q-1)$ we get $d = q - 1$, so we seek a $(q-1)$-dimensional representation.

Consider the complex vector space $V$ of functions $f: \mathbf{F}_q \to \mathbf{C}$. This is $q$-dimensional. Let each $g \in \text{Aff}(\mathbf{F}_q)$ act on $V$ as a linear change of variables using $g^{-1}$: $(\rho_V(g)f)(x) = f(g^{-1}x)$. We need $g^{-1}$ rather than $g$ in the formula to get $\rho_V(gh) = \rho_V(g)\rho_V(h)$. Explicitly,

$$(\rho_V\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}f)(x) = f\left(\frac{1}{a}x - \frac{b}{a}\right).$$

The constant functions in $V$ form a one-dimensional subspace on which $\text{Aff}(\mathbf{F}_q)$ acts trivially. Another $\text{Aff}(\mathbf{F}_q)$-stable subspace of $V$ is

$$W = \left\{f \in V : \sum_{x \in \mathbf{F}_q} f(x) = 0\right\}$$

and $\rho_V = \rho_W \oplus 1$, where $\rho_W$ is the restriction of $\rho_V$ to $W$. The dimension of $W$ is $q - 1$.

To show $W$ is irreducible, we compute its character from that of $V$: $\chi_V = \chi_W + 1$. A basis of $V$ is the $q$ delta-functions $\delta_t: \mathbf{F}_q \to \mathbf{C}$ for $t \in \mathbf{F}_q$, where $\delta_t(x)$ is 0 for $x \neq t$ and $\delta_t(t) = 1$. Since $\rho_V\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}\delta_t = \delta_{at+b}$, the matrix for $\rho_V\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$ with respect to the delta-basis of $V$ is a permutation matrix that describes how $t \mapsto at + b$ permutes $\mathbf{F}_q$. Thus

$$\chi_V\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} = |\{t \in \mathbf{F}_q : at + b = t \text{ in } \mathbf{F}_q\}| = \begin{cases} 1, & \text{if } a \neq 1, \\ q, & \text{if } a = 1 \text{ and } b = 0, \\ 0, & \text{if } a = 1 \text{ and } b \neq 0. \end{cases}$$

Therefore

$$\chi_W\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} = \chi_V\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} - 1 = \begin{cases} 0, & \text{if } a \neq 1, \\ q - 1, & \text{if } a = 1 \text{ and } b = 0, \\ -1, & \text{if } a = 1 \text{ and } b \neq 0. \end{cases}$$

<!-- page 3 -->

The inner product of $\chi_W$ with itself is

$$\frac{1}{q(q-1)}\sum_g \chi_W(g)\overline{\chi_W(g)} = \frac{1}{q(q-1)}((q-1)^2 + (q-1)(-1)^2) = \frac{(q-1)^2 + (q-1)}{q(q-1)} = 1,$$

so $W$ is irreducible. It is a new irreducible representation since it's not 1-dimensional, except if $q = 2$, in which case $\rho_W$ is nontrivial while the single one-dimensional representation constructed earlier ($q - 1 = 1$ if $q = 2$) is trivial (note $\text{Aff}(\mathbf{F}_2) \cong \mathbf{F}_2$).

## 2. Representations of $\text{Heis}(\mathbf{F}_q)$

For a field $F$, the group law in the Heisenberg group $\text{Heis}(F)$ is

$$\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & a' & b' \\ 0 & 1 & c' \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & a+a' & b+b'+ac' \\ 0 & 1 & c+c' \\ 0 & 0 & 1 \end{pmatrix} \tag{2.1}$$

with inverse formula

$$\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & -a & -b+ac \\ 0 & 1 & -c \\ 0 & 0 & 1 \end{pmatrix}.$$

Three subgroups of $\text{Heis}(F)$ are

$$\left\{\begin{pmatrix} 1 & a & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} : a \in F\right\}, \quad \left\{\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} : b \in F\right\}, \quad \left\{\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} : c \in F\right\},$$

which are each isomorphic as groups to the additive group of $F$. Note the subset

$$\left\{\begin{pmatrix} 1 & a & 0 \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} : a, c \in F\right\}$$

is *not* a subgroup of $\text{Heis}(F)$ since it's not closed under multiplication.

Each matrix in $\text{Heis}(F)$ is a product of matrices in the three subgroups above:

$$\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & a & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}. \tag{2.2}$$

If we multiply these three matrices in the reverse order,

$$\begin{pmatrix} 1 & a & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & a & b+ac \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}.$$

Conjugation in $\text{Heis}(F)$ is described by the formula

$$\begin{pmatrix} 1 & x & y \\ 0 & 1 & z \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & x & y \\ 0 & 1 & z \\ 0 & 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & a & b - az + cx \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}. \tag{2.3}$$

In particular, the center of $\text{Heis}(F)$ is

$$\left\{\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} : b \in F\right\}. \tag{2.4}$$

<!-- page 4 -->

Using the conjugation formula (2.3), we get the conjugacy classes in $\text{Heis}(F)$:

- for each $b \in F$, the single matrix

$$\left\{\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\right\},$$

- for each pair $(a, c) \in F^2 - \{(0,0)\}$, the set

$$\left\{\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} : b \in F\right\}.$$

When $F = \mathbf{F}_q$, there are $q + (q^2 - 1) = q^2 + q - 1$ conjugacy classes in $\text{Heis}(\mathbf{F}_q)$, so this group has $q^2 + q - 1$ irreducible representations over $\mathbf{C}$.

**One-dimensional representations:** Fix a nontrivial homomorphism $\psi: \mathbf{F}_q \to \mathbf{C}^\times$. An example is $\psi(a) = e^{2\pi i \text{Tr}_{\mathbf{F}_q/\mathbf{F}_p}(a)}$, where $\mathbf{F}_q$ has characteristic $p$ and $\text{Tr}_{\mathbf{F}_q/\mathbf{F}_p}: \mathbf{F}_q \to \mathbf{F}_p$ is the trace map. (If $q = p$ then $\psi: \mathbf{F}_p \to \mathbf{C}^\times$ by $\psi(a) = e^{2\pi i a/p}$.) Since the $a$ and $c$ terms of a matrix in $\text{Heis}(\mathbf{F}_q)$ each combine additively under multiplication in $\text{Heis}(\mathbf{F}_q)$, for each $(x, y) \in \mathbf{F}_q^2$ there is a 1-dimensional representation $\psi_{x,y}: \text{Heis}(\mathbf{F}_q) \to \mathbf{C}^\times$ given by

$$\psi_{x,y}\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} = \psi(xa + yc). \tag{2.5}$$

Check as an exercise that from $\psi: \mathbf{F}_q \to \mathbf{C}^\times$ being nontrivial, if $\psi_{x,y} = \psi_{x',y'}$ then $(x,y) = (x',y')$ in $\mathbf{F}_q^2$, so $\{\psi_{x,y} : (x,y) \in \mathbf{F}_q^2\}$ is $q^2$ irreducible representations of degree 1. (Hint: first show that if $x \neq 0$ or $y \neq 0$ then $\psi_{x,y}$ is nontrivial, *i.e.*, is not identically 1.)

**Remaining irreducible representations:** The number of remaining irreducible representations is $(q^2 + q - 1) - q^2 = q - 1$. Their degrees $\{d_i\}$ satisfy $q^2 + \sum d_i^2 = |\text{Heis}(\mathbf{F}_q)| = q^3$, so $\sum d_i^2 = q^3 - q^2 = (q-1)q^2$. We will find $q - 1$ irreducible representations of degree $q$.

Let $V$, as before, be the $q$-dimensional vector space of functions $f: \mathbf{F}_q \to \mathbf{C}$. We will define three actions of $\mathbf{F}_q$ on $V$, and composing them in a suitable order will give an action of the group $\text{Heis}(\mathbf{F}_q)$ on $V$. Fix a nontrivial homomorphism $\psi: \mathbf{F}_q \to \mathbf{C}^\times$. For $a, b, c \in \mathbf{F}_q$, define the linear maps $\sigma_a: V \to V$, $\tau_b: V \to V$, and $\varphi_c: V \to V$ by

$$(\sigma_a f)(x) = f(x + a), \quad (\tau_b f)(x) = \psi(b)f(x), \quad (\varphi_c f)(x) = \psi(cx)f(x).$$

For $t \in \mathbf{F}_q$, note $\tau_t$ multiplies each function in $V$ by the *number* $\psi(t)$ while $\varphi_t$ multiplies each function in $V$ by the *function* $\psi(tx)$.

Check $\sigma_a \circ \sigma_{a'} = \sigma_{a+a'}$, $\tau_b \circ \tau_{b'} = \tau_{b+b'}$, and $\varphi_c \circ \varphi_{c'} = \varphi_{c+c'}$ as functions $V \to V$, so $a \mapsto \sigma_a$, $b \mapsto \tau_b$, $c \mapsto \varphi_c$ are actions of $\mathbf{F}_q$ on $V$ by linear maps. Check $\tau_b$ commutes with both $\sigma_a$ and $\varphi_c$, while $\sigma_a$ and $\varphi_c$ commute with each other up to scaling by a root of unity:

$$\sigma_a \circ \tau_b = \tau_b \circ \sigma_a, \quad \varphi_c \circ \tau_b = \tau_b \circ \varphi_c, \quad \sigma_a \circ \varphi_c = \psi(ac)\varphi_c \circ \sigma_a = \tau_{ac} \circ \varphi_c \circ \sigma_a. \tag{2.6}$$

<!-- page 5 -->

Using (2.6), the 3-fold composites $\sigma_a \circ \tau_b \circ \varphi_c$ compose as follows:

$$(\sigma_a \circ \tau_b \circ \varphi_c) \circ (\sigma_{a'} \circ \tau_{b'} \circ \varphi_{c'}) = \sigma_a \circ \tau_b \circ (\varphi_c \circ \sigma_{a'}) \circ \tau_{b'} \circ \varphi_{c'} = \sigma_a \circ \tau_b \circ (\tau_{-a'c} \circ \sigma_{a'} \circ \varphi_c) \circ \tau_{b'} \circ \varphi_{c'} = \sigma_a \circ \tau_{b-a'c} \circ \sigma_{a'} \circ \tau_{b'} \circ \varphi_c \circ \varphi_{c'} = \sigma_a \circ \sigma_{a'} \circ \tau_{b-a'c} \circ \tau_{b'} \circ \varphi_c \circ \varphi_{c'} = \sigma_{a+a'} \circ \tau_{b+b'-a'c} \circ \varphi_{c+c'}.$$

This is almost like the way matrices in $\text{Heis}(\mathbf{F}_q)$ multiply in (2.1), and it would match matrix multiplication if $\tau_{b+b'-a'c}$ were $\tau_{b+b'+ac'}$. Matrices in $\text{Heis}(\mathbf{F}_q)$ decompose in (2.2) using reverse alphabetical order, which suggests looking at $\varphi_c \circ \tau_b \circ \sigma_a$ instead. By calculations as above,

$$(\varphi_c \circ \tau_b \circ \sigma_a) \circ (\varphi_{c'} \circ \tau_{b'} \circ \sigma_{a'}) = \varphi_c \circ \tau_b \circ (\sigma_a \circ \varphi_{c'}) \circ \tau_{b'} \circ \sigma_{a'} = \varphi_c \circ \tau_b \circ (\tau_{ac'} \circ \varphi_{c'} \circ \sigma_a) \circ \tau_{b'} \circ \sigma_{a'} = \varphi_c \circ \tau_{b+ac'} \circ \varphi_{c'} \circ \tau_{b'} \circ \sigma_a \circ \sigma_{a'} = \varphi_c \circ \varphi_{c'} \circ \tau_{b+ac'} \circ \tau_{b'} \circ \sigma_a \circ \sigma_{a'} = \varphi_{c+c'} \circ \tau_{b+b'+ac'} \circ \sigma_{a+a'}.$$

This is exactly how matrices in $\text{Heis}(\mathbf{F}_q)$ multiply, so we can define a $q$-dimensional representation $\rho_\psi$ of $\text{Heis}(\mathbf{F}_q)$ on $V$ by

$$g = \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} \mapsto \rho_\psi(g) := \varphi_c \circ \tau_b \circ \sigma_a.$$

As a formula, for $f \in V$

$$(\rho_\psi(g)f)(x) = (\varphi_c \tau_b \sigma_a f)(x) = \psi(cx)(\tau_b \sigma_a f)(x) = \psi(cx)\psi(b)f(x+a) = \psi(cx+b)f(x+a).$$

Let's compute the character of $\rho_\psi$. Using the basis $\{\delta_t : t \in \mathbf{F}_q\}$ of $V$, we have

$$g = \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} \implies (\rho_\psi(g)\delta_t)(x) = \psi(cx+b)\delta_t(x+a) = \begin{cases} \psi(c(t-a)+b), & \text{if } x = t-a, \\ 0, & \text{if } x \neq t-a, \end{cases}$$

so

$$\rho_\psi(g)\delta_t = \psi(c(t-a)+b)\delta_{t-a}.$$

- If $a \neq 0$, then the matrix of $\rho_\psi(g)$ with respect to the delta-basis has 0's on the main diagonal, so $(\text{Tr}\ \rho_\psi)(g) = 0$.
- If $a = 0$, then the matrix of $\rho_\psi(g)$ with respect to the delta-basis has diagonal entries $\psi(ct+b)$, so $(\text{Tr}\ \rho_\psi)(g) = \sum_{t \in \mathbf{F}_q} \psi(ct+b)$. If $c \neq 0$ then this sum equals $\sum_{x \in \mathbf{F}_q} \psi(x)$, which is 0 *since $\psi$ is nontrivial*, and if $c = 0$ then this sum is $q\psi(b)$.

Thus the character $\chi_\psi$ of $\rho_\psi$ is

$$\chi_\psi\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} = \begin{cases} q\psi(b), & \text{if } a = c = 0, \\ 0, & \text{otherwise}. \end{cases} \tag{2.7}$$

<!-- page 6 -->

so for each nontrivial homomorphism $\psi: \mathbf{F}_q \to \mathbf{C}^\times$, the inner product of $\chi_\psi$ with itself is

$$\frac{1}{q^3}\sum_g \chi_\psi(g)\overline{\chi_\psi(g)} = \frac{1}{q^3}\sum_{b \in \mathbf{F}_q} q\psi(b)\overline{q\psi(b)} = \frac{1}{q}\sum_{b \in \mathbf{F}_q} 1 = 1.$$

There are $q - 1$ nontrivial homomorphisms $\psi: \mathbf{F}_q \to \mathbf{C}^\times$, and to each is a $q$-dimensional irreducible representation $\rho_\psi$ of $\text{Heis}(\mathbf{F}_q)$. To prove $\rho_\psi$'s for different nontrivial $\psi$ are nonisomorphic, we show their characters $\chi_\psi$ are distinct. This is a consequence of the formula

$$\chi_\psi\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = q\psi(b), \tag{2.8}$$

which is a special case of (2.7). It shows we can recover each nontrivial $\psi$ from the character $\chi_\psi$ of the $q$-dimensional representation $\rho_\psi$ of $\text{Heis}(\mathbf{F}_q)$. (Alternatively, check for different nontrivial homomorphisms $\psi_1, \psi_2: \mathbf{F}_q \to \mathbf{C}^\times$ that the inner product of the characters of $\rho_{\psi_1}$ and $\rho_{\psi_2}$ is 0, so for different nontrivial $\psi$'s the representations $\rho_\psi$ are nonisomorphic.)

The center of $\text{Heis}(\mathbf{F}_q)$, by (2.4), is

$$Z_q := \left\{\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} : b \in \mathbf{F}_q\right\} \cong \mathbf{F}_q,$$

so (2.8) tells us that each $q$-dimensional irreducible character $\chi_\psi$ of $\text{Heis}(\mathbf{F}_q)$ is determined by its restriction to $Z_q$, since $\chi_\psi$ on $Z_q$ is enough information to determine $\psi$ on $\mathbf{F}_q$, which is all we need to compute $\chi_\psi$ on $\text{Heis}(\mathbf{F}_q)$ in (2.7). In terms of representations rather than characters, the definition of $\rho_\psi$ shows that $\rho_\psi$ on $Z_q$ is described by

$$\rho_\psi\begin{pmatrix} 1 & 0 & b \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \tau_b: f \mapsto \psi(b)f$$

for all functions $f \in V$, so $\rho_\psi$ restricted to $Z_q$ is enough information to recover $\psi$ on $\mathbf{F}_q$.

Each $q$-dimensional irreducible representation $\rho_\psi$ of $\text{Heis}(\mathbf{F}_q)$ is nontrivial on $Z_q$. The other irreducible representations of $\text{Heis}(\mathbf{F}_q)$ are 1-dimensional, and they are trivial on $Z_q$ by (2.5). Thus the irreducible representations of $\text{Heis}(\mathbf{F}_q)$ that are nontrivial on $Z_q$ are in bijection with the nontrivial characters of $Z_q$ by $\rho_\psi \mapsto \psi$; this is an analogue of the Stone-von Neumann theorem in mathematical physics about representations of $\text{Heis}(\mathbf{R})$.

More on the irreducible representations of $\text{Aff}(\mathbf{F}_q)$ and $\text{Heis}(\mathbf{F}_q)$ is in [1, Chap. 16--18].

## References

[1] A. Terras, "Fourier Analysis on Finite Groups and Applications," Cambridge Univ. Press, 1999.
