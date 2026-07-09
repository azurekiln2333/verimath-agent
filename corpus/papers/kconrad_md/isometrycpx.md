# Isometries of the Plane and Complex Numbers

> **Source**: https://kconrad.math.uconn.edu/blurbs/isometrycpx.pdf
> **Author**: Keith Conrad
> **Topic**: geometry

<!-- page 1 -->

## 1. Introduction

The length of a vector $\mathbf{v} = \binom{x}{y}$ in $\mathbf{R}^2$ is $\left\|\binom{x}{y}\right\| = \sqrt{x^2 + y^2}$, and the distance between two vectors $\mathbf{v}$ and $\mathbf{w}$ is the length of their difference: $\|\mathbf{v} - \mathbf{w}\|$. A function $h: \mathbf{R}^2 \to \mathbf{R}^2$ is called an *isometry* when it preserves distances: $\|h(\mathbf{v}) - h(\mathbf{w})\| = \|\mathbf{v} - \mathbf{w}\|$ for all $\mathbf{v}$ and $\mathbf{w}$ in $\mathbf{R}^2$. Examples of isometries include translation by $\binom{1}{-1/2}$, a rotation by 40 degrees counterclockwise around the origin, and reflection across the line $y = 1 - 2x$. The effect of these isometries on some line segments is illustrated in the figures below.

<!-- figures: translation, rotation, reflection on line segments -->

Isometries of $\mathbf{R}^2$ can be described using linear algebra [1, Chap. 6],[^1] and this generalizes to isometries of $\mathbf{R}^n$ [2, Sect. 6.5, 6.11].[^2] However, we can describe isometries of $\mathbf{R}^2$ without linear algebra, using complex numbers by viewing vectors $\binom{x}{y}$ as complex numbers $x + yi$.

<!-- figure: complex plane showing x + yi = (x, y) -->

Algebraically, adding vectors and adding the corresponding complex numbers match, since we add vectors componentwise and add complex numbers by adding real parts and adding imaginary parts (which is also componentwise). Geometrically, the length of a vector is the absolute value of the corresponding complex number: $\left\|\binom{x}{y}\right\| = \sqrt{x^2 + y^2} = |x + yi|$, which is the length of the line segment connecting $x + yi$ to the origin in the figure above.

<!-- page 2 -->

The distance between two complex numbers $z$ and $w$ is $|z - w|$, so if the vectors $\mathbf{v}$ and $\mathbf{w}$ in $\mathbf{R}^2$ correspond to the complex numbers $z$ and $w$, then $\|\mathbf{v} - \mathbf{w}\| = |z - w|$. Therefore if we think of $\mathbf{R}^2$ as $\mathbf{C}$, an isometry of $\mathbf{R}^2$ can be viewed as a function $h: \mathbf{C} \to \mathbf{C}$ satisfying $|h(z) - h(w)| = |z - w|$ for all $z$ and $w$ in $\mathbf{C}$. Our goal is to describe all the isometries of the plane using algebraic operations with complex numbers. The reason that we will be able to do this is based on four features of complex numbers.

1. Addition by $x + yi$ is the *translation* of the plane by the vector $(x, y)$.
2. Multiplication by $\cos\theta + i\sin\theta$, a complex number of absolute value 1, is a counterclockwise *rotation* around the origin by an angle of $\theta$. In particular, for nonzero $\gamma \in \mathbf{C}$ the pair $\{\gamma, i\gamma\}$ is an orthogonal basis of $\mathbf{C}$ as a real vector space.
3. Complex conjugation has the effect of *reflection* across the $x$-axis, so in particular solutions to $\bar{z} = z$ lie on a line (in fact the real line).
4. The absolute value on $\mathbf{C}$, which is connected to the distance formula via $|z - w|$, behaves nicely with respect to multiplication in $\mathbf{C}$ and complex conjugation:

$$|zw| = |z||w| \text{ and } |\bar{z}| = |z|. \tag{1.1}$$

In Section 2, we will algebraically derive formulas for all isometries of the plane using complex numbers. These formulas will be interpreted geometrically in Section 3.

## 2. Algebraic Arguments

For all $z \in \mathbf{C}$, consider the two types of functions $\mathbf{C} \to \mathbf{C}$:

$$h_1(z) = \alpha z + \beta, \quad h_2(z) = \alpha\bar{z} + \beta, \tag{2.1}$$

where $|\alpha| = 1$ and $\beta$ is a complex number. These formulas are both isometries. Indeed,

$$h_1(z) - h_1(w) = \alpha(z - w), \quad h_2(z) - h_2(w) = \alpha\overline{(z - w)}.$$

By (1.1), $|h_1(z) - h_1(w)| = |z - w|$ and $|h_2(z) - h_2(w)| = |z - w|$ for all $z$ and $w$ in $\mathbf{C}$.

We will show every isometry of the plane is given by one of the formulas in (2.1).

**Lemma 2.1.** *An isometry of the plane that fixes $0$, $1$, and $i$ is the identity.*

*Proof.* Let $h$ be such an isometry. Since $h(0) = 0$, $h(1) = 1$, and $h(i) = i$, for each $z \in \mathbf{C}$ the formula $|h(z) - h(w)| = |z - w|$ at $w = 0, 1,$ and $i$ becomes

$$|h(z)| = |z|, \quad |h(z) - 1| = |z - 1|, \quad |h(z) - i| = |z - i|. \tag{2.2}$$

This says $h(z)$ and $z$ have the same distances from the three numbers $0$, $1$, and $i$. Geometrically, it is plausible that a complex number is completely determined by its distances from $0$, $1$, and $i$: three circles centered at each of these points can't intersect in more than one common point. Granting this, we conclude from (2.2) that $h(z) = z$.

To check this algebraically, we want to show for $w$ and $z$ in $\mathbf{C}$ that

$$|w| = |z|, \ |w - 1| = |z - 1|, \ |w - i| = |z - i| \implies w = z. \tag{2.3}$$

Square the three equations in (2.3) and use the formula $|u|^2 = u\bar{u}$ for $u \in \mathbf{C}$:

$$w\bar{w} = z\bar{z}, \quad (w - 1)(\bar{w} - 1) = (z - 1)(\bar{z} - 1), \quad (w - i)(\bar{w} + i) = (z - i)(\bar{z} + i).$$

Expanding the second and third equations, and feeding in the first, we obtain after simplifying

$$w + \bar{w} = z + \bar{z}, \quad w - \bar{w} = z - \bar{z}.$$

Therefore $w$ and $z$ have equal real parts and equal imaginary parts, so $w = z$. $\square$

<!-- page 3 -->

**Theorem 2.2.** *Each isometry of the plane is given by one of the formulas $h_1(z) = \alpha z + \beta$ or $h_2(z) = \alpha\bar{z} + \beta$ for unique $\alpha$ and $\beta$ in $\mathbf{C}$ where $|\alpha| = 1$.*

*Proof.* In both formulas, $\beta = h_i(0)$ and $\alpha = h_i(1) - h_i(0)$ for $i = 1, 2$. This suggests that, for an unknown isometry $h: \mathbf{C} \to \mathbf{C}$, we *define*

$$\beta = h(0), \quad \alpha = h(1) - h(0).$$

Then $|\alpha| = |h(1) - h(0)| = |1 - 0| = 1$. Now consider the function

$$k(z) := \frac{h(z) - \beta}{\alpha} = \frac{h(z) - h(0)}{h(1) - h(0)}. \tag{2.4}$$

We *expect* this function is either $z$ or $\bar{z}$.

Note first of all that $k(z)$ is an isometry:

$$|k(z) - k(w)| = \left|\frac{(h(z) - \beta) - (h(w) - \beta)}{\alpha}\right| = |h(z) - h(w)| = |z - w|.$$

With Lemma 2.1 in mind, we compute $k(z)$ at $z = 0, 1,$ and $i$. Easily $k(0) = 0$ and $k(1) = 1$. What about $k(i)$?

Since $k$ fixes $0$ and $1$,

$$|k(i)| = |k(i) - k(0)| = |i - 0| = 1, \quad |k(i) - 1| = |k(i) - k(1)| = |i - 1| = \sqrt{2},$$

so $k(i)$ lies on both the unit circle and the circle around $1$ of radius $\sqrt{2}$. There are only two such points: $i$ and $-i$.

<!-- figure: two intersecting circles showing i and -i -->

If $k(i) = i$, then $k$ is an isometry fixing $0$, $1$, and $i$, so $k(z) = z$ for all $z$ by Lemma 2.1. If $k(i) = -i$, then $\overline{k(z)}$ is an isometry fixing $0$, $1$, and $i$, so Lemma 2.1 tells us $\overline{k(z)} = z$ for all $z$. Conjugating, $k(z) = \bar{z}$ for all $z$.

Since $h(z) = \alpha k(z) + \beta$, the two possible formulas for $k(z)$ lead to the desired possible formulas for $h(z)$. The uniqueness of $\alpha$ and $\beta$ is clear from $\alpha = h(0)$ and $\beta = h(1) - h(0)$. $\square$

**Corollary 2.3.** *Every isometry of the plane is an invertible function and its inverse function is an isometry.*

*Proof.* If $h(z) = \alpha z + \beta$ with $|\alpha| = 1$, its inverse is $(1/\alpha)z - \beta/\alpha$ with $|1/\alpha| = 1$. If $h(z) = \alpha\bar{z} + \beta$ with $|\alpha| = 1$, its inverse is $(1/\bar{\alpha})\bar{z} - \beta/\alpha$ with $|1/\bar{\alpha}| = 1$. Both inverses have the shape of the formulas in Theorem 2.2 (e.g., the coefficient of $z$ or $\bar{z}$ has absolute value 1), so these inverse functions are isometries. $\square$

The composition of two isometries is an isometry, and composition of functions is associative, so Corollary 2.3 shows *the isometries of $\mathbf{R}^2$ are a group under composition*.

Now we can generalize Lemma 2.1.

<!-- page 4 -->

**Lemma 2.4.** *If an isometry of the plane fixes three points that are not collinear, then that isometry is the identity.*

We need to assume in the lemma that the isometry has at least three fixed points that are *not* collinear, since an isometry fixing three collinear points need not be the identity: it could be a reflection across the line through the two points. (Two different points are always fixed by some non-identity isometry: the reflection across the line through them.)

*Proof.* We can write an isometry $h(z)$ as $\alpha z + \beta$ or $\alpha\bar{z} + \beta$, where $|\alpha| = 1$. Unless $h(z)$ is the identity, we will show $h(z)$ can't have 3 fixed points that don't lie on a line.

**Case 1:** $h(z) = \alpha z + \beta$. If $\alpha \neq 1$ then there is only one solution to $h(z) = z$, namely $z = \beta/(1 - \alpha)$. If $\alpha = 1$, so $h(z) = z + \beta$, then there are no solutions to $h(z) = z$ if $\beta \neq 0$. So unless $\alpha = 1$ and $\beta = 0$, which means $h$ is the identity, $h(z)$ has at most 1 fixed point.

**Case 2:** $h(z) = \alpha\bar{z} + \beta$. The condition $h(z) = z$ is the same as $\alpha\bar{z} + \beta = z$. We will show the set of solutions to this equation, if it is not empty, lie along a line. Thus $h$ doesn't have three fixed points not lying on a line. Let $w$ and $z$ both be fixed points of $h$, so $\alpha\bar{z} + \beta = z$ and $\alpha\bar{w} + \beta = w$. Subtracting one equation from the other,

$$\alpha(\bar{w} - \bar{z}) = w - z. \tag{2.5}$$

If $\alpha$ were $1$, then $\bar{w} - \bar{z} = w - z$, so $t := w - z$ is real and $w = z + t$. This means all fixed points of $h$ are on the horizontal line through $z$, so three fixed points of $h$ can't be collinear. What if $\alpha \neq 1$? Here there is a clever trick with square roots. All complex numbers are squares, so we can write $\alpha = \gamma^2$. Then $|\gamma| = 1$, so $\bar{\gamma} = 1/\gamma$, which means $\alpha = \gamma/\bar{\gamma}$ and (2.5) becomes

$$\overline{\left(\frac{w - z}{\gamma}\right)} = \frac{w - z}{\gamma}.$$

Thus $t := (w - z)/\gamma$ is real, so $w = z + t\gamma$. Now $w$ lies on the line with direction $\gamma$ passing through $z$, so again all fixed points of $h$ lie on a line. $\square$

**Theorem 2.5.** *An isometry of the plane is determined by its values at three noncollinear points: if two isometries $h_1$ and $h_2$ are equal at three noncollinear points, then $h_1 = h_2$ everywhere on the plane.*

*Proof.* The isometry $h_2$ is invertible and its inverse is an isometry, by Corollary 2.3. To say $h_1(z) = h_2(z)$ is the same as saying $(h_2^{-1}h_1)(z) = z$. Therefore our hypothesis says the composite function $h_2^{-1}h_1$, which is an isometry (we mentioned earlier that the composition of isometries is an isometry) fixes three noncollinear points, so by Lemma 2.4 it is the identity: $(h_2^{-1}h_1)(z) = z$ for all $z \in \mathbf{C}$, so $h_1(z) = h_2(z)$ for all $z$. $\square$

## 3. Geometric Arguments

Now we want to understand the geometry behind the formulas in (2.1). We will see that the isometries of the plane fall into four types: translations, rotations, reflections, and glide reflections. A *glide reflection* is the composition of a reflection and a nonzero translation in a direction parallel to the line of reflection. A picture of a glide reflection is in the figure below, where the line of reflection is dashed and the translation is a movement to the right.

<!-- page 5 -->

<!-- figure: glide reflection illustration -->

The image above, which includes "before" and "after" states, suggests a physical interpretation of a glide reflection: it is the result of turning the plane in space like a half-turn of a screw. A more picturesque image, suggested to me by Michiel Vermeulen, is the effect of successive steps with a left foot and then a right foot in the sand or snow (if your feet are mirror reflections).

We will look at the functions in (2.1) and see how they are one of the four types of isometries in terms of conditions on the parameters $\alpha$ and $\beta$ in each case. Table 1 summarizes the relations we will prove between the geometric description of an isometry and the formula for the isometry. In the table, $|\alpha| = 1$ and $\gamma^2 = \alpha$. (The only isometry belonging to more than one of the four types is the identity, which is both a translation and a rotation, so we make the identity its own row in the table.)

| Isometry | Formula | Fixed points |
|---|---|---|
| Identity | $z$ | $\mathbf{C}$ |
| Nonzero Translation | $z + \beta$, with $\beta \neq 0$ | $\emptyset$ |
| Nonzero Rotation | $\alpha z + \beta$, with $\alpha \neq 1$ | $\beta/(1 - \alpha)$ |
| Reflection | $\alpha\bar{z} + \beta$, with $\beta^2/\alpha \in (-\infty, 0]$ | $\beta/2 + \mathbf{R}\gamma$ |
| Glide Reflection | $\alpha\bar{z} + \beta$, with $\beta^2/\alpha \notin (-\infty, 0]$ | $\emptyset$ |

**Table 1.** Isometries of $\mathbf{R}^2$

In this table, the only nonidentity isometries fixing more than one point are reflections, whose fixed points lie along a line. This is a better way of understanding Lemma 2.4.

Now we turn to the justification of the information in Table 1.

**Case 1:** $h(z) = z + \beta$. This is a translation of the plane by $\beta$. It has no fixed points unless $\beta = 0$, in which case $h$ is the identity and all points are fixed.

**Case 2:** $h(z) = \alpha z + \beta$, $\alpha \neq 1$.

The unique fixed point of $h$ is $z_0 = \beta/(1 - \alpha)$. We expect $h$ should be a rotation around $z_0$. To prove this, express $h(z)$ in terms of its fixed point $z_0$:

$$h(z) = \alpha z + \beta = \alpha z + (1 - \alpha)z_0 = \alpha(z - z_0) + z_0. \tag{3.1}$$

Since multiplication by $\alpha$ (of absolute value 1, and not equal to 1) is a nontrivial rotation around 0, (3.1) tells us $h$ is a rotation around $z_0$: the process of subtracting $z_0$, multiplying by $\alpha$, and then adding back $z_0$ amounts to rotating around $z_0$ by the nonzero angle determined by $\alpha$ as a rotation around 0.

**Case 3:** $h(z) = \alpha\bar{z} + \beta$. There may be some fixed points or there may be no fixed points. For instance, the equation $\bar{z} = z$ has the real line as its fixed points, while the equation $\bar{z} + 1 = z$ has no fixed points. It will turn out that $h$ has either a whole line of fixed points

<!-- page 6 -->

(in which case we will show $h$ is the reflection across that line) or it has no fixed points (in which case we will show $h$ is a glide reflection).

In the proof of Lemma 2.4 we studied the equation $\alpha\bar{z} + \beta = z$ using a square root of $\alpha$. Let's bring back that square root. Write $\alpha = \gamma^2$, so $|\gamma| = 1$ (since $|\alpha| = 1$). From the proof of Lemma 2.4, if $w$ and $z$ are both fixed points of $h$ then

$$\overline{\left(\frac{w - z}{\gamma}\right)} = \frac{w - z}{\gamma},$$

so $t := (w - z)/\gamma$ is real and $w = z + t\gamma$. Conversely, for real number $t$ and complex number $z$ such that $\alpha\bar{z} + \beta = z$, check that the number $w = z + t\gamma$ satisfies $\alpha\bar{w} + \beta = w$. Therefore the set of fixed points of $h(z) = \alpha\bar{z} + \beta$ is

$$\{z_0 + t\gamma : t \in \mathbf{R}\} = z_0 + \mathbf{R}\gamma, \tag{3.2}$$

where $z_0$ is a fixed point.

The function $\alpha\bar{z} + \beta$ may not have fixed points (e.g., $h(z) = \bar{z} + 1$). A necessary and sufficient condition on $\alpha$ and $\beta$ in order for the isometry $h(z) = \alpha\bar{z} + \beta$ to have a fixed point is that $\beta^2/\alpha \in (-\infty, 0]$. To see why this is necessary, suppose $\alpha\bar{z} + \beta = z$ for some $z$. Applying complex conjugation to this equation gives us $\bar{\alpha}z + \bar{\beta} = \bar{z}$, so we must have

$$\bar{z} = \frac{z - \beta}{\alpha} = \bar{\alpha}z + \bar{\beta}.$$

Since $\bar{\alpha} = 1/\alpha$, the terms $z/\alpha$ and $\bar{\alpha}z$ in the second equation above match, and subtracting them leaves us with $-\beta/\alpha = \bar{\beta}$, so $\beta^2/\alpha = -\beta\bar{\beta} = -|\beta|^2 \in (-\infty, 0]$. Conversely, if $\beta^2/\alpha \in (-\infty, 0]$, write $\beta^2/\alpha = -c^2$ where $c \geq 0$. Taking absolute values implies $|\beta|^2 = c^2$ and (miracle!) the number $\beta/2$ is a fixed point of $h$:

$$h\left(\frac{\beta}{2}\right) = \alpha \cdot \frac{\bar{\beta}}{2} + \beta = -\frac{\beta^2\bar{\beta}}{2c^2} + \beta = -\frac{\beta|\beta|^2}{2c^2} + \beta = -\frac{\beta}{2} + \beta = \frac{\beta}{2}.$$

To summarize, $h(z) = \alpha\bar{z} + \beta$ has a fixed point if and only if $\beta^2/\alpha \in (-\infty, 0]$, in which case $\beta/2$ is a fixed point, so (3.2) tells us that the set of all fixed points of $h$ is the line

$$\frac{\beta}{2} + \mathbf{R}\gamma,$$

where $\gamma^2 = \alpha$. See the figure below. We will prove $h$ is reflection across the line $\beta/2 + \mathbf{R}\gamma$ by checking two properties:

- for all $z$, the average $\frac{1}{2}(z + h(z))$ lies on the line $\beta/2 + \mathbf{R}\gamma$,
- for all $z$, the difference $z - h(z)$ is perpendicular to the line $\beta/2 + \mathbf{R}\gamma$.

<!-- figure: reflection geometry showing points z, h(z), and the line -->

<!-- page 7 -->

For the first property,

$$\frac{z + h(z)}{2} = \frac{z + \alpha\bar{z} + \beta}{2} = \frac{\beta}{2} + \frac{z + \gamma^2\bar{z}}{2} = \frac{\beta}{2} + \frac{\bar{\gamma}z + \gamma\bar{z}}{2}\gamma.$$

The number $\bar{\gamma}z + \gamma\bar{z} = \bar{\gamma}z + \overline{\bar{\gamma}z}$ is real, so this average is on the line $\beta/2 + \mathbf{R}\gamma$. For the second property,

$$z - h(z) = z - (\alpha\bar{z} + \beta) = \gamma\bar{\gamma}z - \gamma^2\bar{z} - \beta = (\bar{\gamma}z - \gamma\bar{z})\gamma - \beta.$$

We want this to be orthogonal to the direction of $\gamma$ (which is the direction of the line $\beta/2 + \mathbf{R}\gamma$). Multiplication of a complex number by $i$ rotates it 90 degrees counterclockwise, so the direction orthogonal to $\gamma$ is the direction of $i\gamma$. The difference $\bar{\gamma}z - \gamma\bar{z} = \bar{\gamma}z - \overline{\bar{\gamma}z}$ is purely imaginary, so the first term in the formula for $z - h(z)$ is in $\mathbf{R}i\gamma$. What about $-\beta$? Since $\beta^2/\alpha \in (-\infty, 0]$, write $\beta^2 = -\alpha c^2$ for real $c$. Then $\beta^2 = -\gamma^2 c^2$, so $\beta = \pm ic\gamma \in \mathbf{R}i\gamma$. Thus $z - h(z) \in \mathbf{R}i\gamma$. That completes the proof that $h$ is the reflection across the line $\beta/2 + \mathbf{R}\gamma$.

The remaining type of isometry is $h(z) = \alpha\bar{z} + \beta$ with no fixed points, so $\beta^2/\alpha \notin (-\infty, 0]$. Before we show $h$ is a glide reflection (that is, a composition of a reflection and a nonzero translation in a direction parallel to the line of reflection), let's look at two examples.

**Example 3.1.** Let $h(z) = \bar{z} + 1$. This is a reflection across the $x$-axis composed with a translation (by 1) in a direction parallel to the line of reflection.

**Example 3.2.** Let $h(z) = \bar{z} + (1 + i) = (\bar{z} + i) + 1$. Since $i = w - \bar{w}$ for $w = i/2$, the function $z \mapsto \bar{z} + i$ is a reflection across the horizontal line $i/2 + \mathbf{R}$. Thus $h$ is a composition of a reflection across a line and a translation (by 1) in a direction parallel to that line.

To see that $h(z) = \alpha\bar{z} + \beta$ describes a glide reflection when it has no fixed points, write $\alpha = \gamma^2$. Using $\{\gamma, i\gamma\}$ as an $\mathbf{R}$-basis of $\mathbf{C}$, we can write $\beta = a\gamma + bi\gamma$ with real $a$ and $b$. Then

$$h(z) = \alpha\bar{z} + \beta = \alpha\bar{z} + (a\gamma + bi\gamma) = (\alpha\bar{z} + bi\gamma) + a\gamma. \tag{3.3}$$

Since $(bi\gamma)^2/\alpha = -b^2 \leq 0$, our earlier discussion of reflections tells us that $\alpha\bar{z} + bi\gamma$ is a reflection across a line parallel to $\mathbf{R}\gamma$. Since $\beta^2/\alpha \notin (-\infty, 0]$, we must have $a \neq 0$. Therefore adding $a\gamma$ in (3.3) amounts to composition of a reflection across a line parallel to $\mathbf{R}\gamma$ with a nonzero translation in a direction parallel to the same line. Hence $h$ is a glide reflection.

This completes the justification of Table 1, although we should also emphasize why the different types of isometries in Table 1 are different from each other. Looking at the set of fixed points (empty, point, line, plane) easily distinguishes the first four types of isometries from each other and distinguishes a glide reflection from all but a translation. To show a glide reflection is not a translation, if $h(z) = \alpha\bar{z} + \beta$ were a translation then $h(z) - z$ would be constant, but $h(z) - z = \alpha\bar{z} - z + \beta$ is not constant: from $h(0) - 0 = h(1) - 1 = h(i) - i$ the first equation would imply $\alpha = 1$ and the second would imply $\alpha = -i$.

We now draw a few conclusions about plane isometries from the formulas in Table 1.

<!-- page 8 -->

**Theorem 3.3.** *The composition of two reflections is a translation or a rotation, and it is a translation precisely when the two reflections are across a pair of parallel lines.*

*Proof.* Let $s_1$ and $s_2$ be two reflections, so $s_1(z) = \alpha_1\bar{z} + \beta_1$ and $s_2(z) = \alpha_2\bar{z} + \beta_2$, where $\alpha_1$ and $\alpha_2$ have absolute value 1 and $\beta_1^2/\alpha_1$ and $\beta_2^2/\alpha_2$ are in $(-\infty, 0]$. Then

$$s_1(s_2(z)) = \alpha_1\overline{(\alpha_2\bar{z} + \beta_2)} + \beta_1 = (\alpha_1\bar{\alpha}_2)z + (\alpha_1\bar{\beta}_2 + \beta_1).$$

This has the form $\alpha z + \beta$ where $\alpha = \alpha_1\bar{\alpha}_2$, so $|\alpha| = 1$. Table 1 tells us that $s_1 \circ s_2$ is a translation or rotation (possibly the identity).

The composite $s_1 \circ s_2$ is a translation precisely when $\alpha_1\bar{\alpha}_2 = 1$, which (since $\bar{\alpha}_2 = 1/\alpha_2$) amounts to saying $\alpha_2 = \alpha_1$. Then $s_1(z) = \alpha_1 z + \beta_1$ and $s_2(z) = \alpha_1 z + \beta_2$. The fixed lines of these reflections are $\beta_1/2 + \mathbf{R}\gamma$ and $\beta_2/2 + \mathbf{R}\gamma$, where $\gamma^2 = \alpha_1$, so these lines are parallel. $\square$

**Example 3.4.** Let $s_1(z) = -\bar{z} + 3$, $s_2(z) = -\bar{z} + 5$, and $s_3(z) = \bar{z} + i$. Their respective lines of reflection are $3/2 + \mathbf{R}i$ (horizontal), $5/2 + \mathbf{R}i$ (horizontal), and $i/2 + \mathbf{R}$ (vertical). The composite $s_1(s_2(z))$ is $z - 2$, which is a translation. The composite $s_1(s_3(z))$ is $-z + (3 + i)$, which is a rotation around $(3 + i)/2$ by 180 degrees.

**Theorem 3.5.** *If $g$ and $h$ are two isometries of the plane, $ghg^{-1}$ is an isometry of the same type as $h$.*

*Proof.* Write $g(z) = \alpha z + \beta$. For a translation $t(z) = z + c$, an explicit calculation shows $(gtg^{-1})(z) = z + \alpha c$. If we have $\bar{z}$ in place of $z$ in $g(z)$, then $(gtg^{-1})(z) = z + \alpha\bar{c}$. Thus $gtg^{-1}$ is a translation for every isometry $g$.

For two plane isometries $g$ and $h$, $h$ fixes $z$ if and only if $ghg^{-1}$ fixes $g(z)$. An isometry takes a point or a line to a point or a line, respectively, so from our knowledge of fixed points of different kinds of isometries we see that if $h$ is a rotation then $ghg^{-1}$ is a rotation (1 fixed point), and if $h$ is a reflection then $ghg^{-1}$ is a reflection (a line of fixed points).

(We can say something more precise in the case $h(z) = \alpha z + \beta$ is a rotation. When $g$ is a translation or rotation $(ghg^{-1})(z) = \alpha z + *$, while when $g$ is a reflection or glide reflection $(ghg^{-1})(z) = \bar{\alpha}z + *$. Therefore $ghg^{-1}$ is a rotation by the same angle as $h$ or the opposite angle to $h$, at some point in the plane.)

Suppose $h$ is a glide reflection, so it has no fixed points. Then $ghg^{-1}$ also has no fixed points, which means $ghg^{-1}$ is either a glide reflection or a translation. If $ghg^{-1}$ were a translation, say $ghg^{-1} = t$, then $h = g^{-1}tg$, which is a translation by the first paragraph (replace $g$ with $g^{-1}$ there). That is a contradiction, so $ghg^{-1}$ must be a glide reflection. $\square$

**Theorem 3.6.** *Each isometry of $\mathbf{R}^2$ is a composition of at most 2 reflections, except for glide reflections, which are compositions of 3 (and no fewer) reflections.*

*Proof.* We check the result for the identity, nonzero translations, rotations, and glide reflections.

The identity is the composition of every reflection with itself. (For instance, $z = \bar{\bar{z}}$).

Write a nonzero translation as $t(z) = z + \beta$. Set $s(z) = -(\beta/\bar{\beta})\bar{z}$ and $s'(z) = -(\beta/\bar{\beta})\bar{z} + \beta$. Both are reflections by Table 1. (For instance, writing $s'(z) = \alpha\bar{z} + \beta$ we have $\beta^2/\alpha = -\beta\bar{\beta} = -|\beta|^2 \leq 0$). Check by a computation that $(s' \circ s)(z) = z + \beta = t(z)$. (Alternatively, from $s' = t \circ s$ we get $t = s' \circ s^{-1} = s' \circ s$.)

A rotation around 0 can be written as $h(z) = \alpha z$, where $|\alpha| = 1$. Take $k(z) = \bar{z}$ and $\ell(z) = \bar{\alpha} \cdot \bar{z}$. Then $k$ and $\ell$ are reflections by Table 1 and $h = k \circ \ell$. An arbitrary rotation of

<!-- page 9 -->

the plane has the form $h(z) = \alpha(z - z_0) + z_0$, where $z_0$ is the center of rotation and $|\alpha| = 1$. Then $h = t \circ r \circ t^{-1}$, where $t$ is translation by $z_0$ and $r(z) = \alpha z$ is a rotation around 0. From what we already said about rotations around 0, we can write $r = k \circ \ell$ for two reflections $k$ and $\ell$. Then $h = trt^{-1} = t(k\ell)t^{-1} = (tkt^{-1}) \circ (t\ell t^{-1})$, which is a composition of two reflections by Theorem 3.5.

Lastly, a glide reflection is a composition of a reflection and a nonzero translation. Since a (nonzero) translation is a composition of two reflections, a glide reflection is a composition of 3 reflections. The number of reflections can't be reduced. Indeed, a glide reflection is not a reflection since they don't have the same kind of fixed points (the empty set and a line), and a glide reflection is not a composition of two reflections since the only such isometries are translations and rotations, by Theorem 3.3. $\square$

## References

[1] M. Artin, "Algebra," 2nd ed., Prentice Hall, New York, 2011.

[2] S. H. Friedberg, A. J. Insel, and L. E. Spence, "Linear Algebra," 4th ed., Pearson, Upper Saddle River NJ, 2003.

[^1]: See also https://kconrad.math.uconn.edu/blurbs/grouptheory/isometryR2.pdf.
[^2]: See also https://kconrad.math.uconn.edu/blurbs/grouptheory/isometryRn.pdf.
