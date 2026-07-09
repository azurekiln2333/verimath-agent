# Cyclicity of $(\mathbf{Z}/(p))^\times$

> **Source**: https://kconrad.math.uconn.edu/blurbs/cyclicmodp.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory

<!-- page 1 -->

## 1. Introduction

For a prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic. This is very important in number theory and has had practical uses since a choice of generator of $(\mathbf{Z}/(p))^\times$ is part of the Diffie-Hellman key exchange, which is how public-key cryptography started in 1976 (modern cryptography uses a variant called the elliptic curve Diffie-Hellman key exchange)[^1].

We will give *ten* proofs that $(\mathbf{Z}/(p))^\times$ is cyclic. A feature of all known proofs is that they do not lead to concrete formula for a generator in terms of $p$. While the proof in Section 7 is an algorithm leading to a generator, is is not a provably efficient algorithm since it depends on the prime factorization of $p - 1$.

Cyclicity of $(\mathbf{Z}/(p))^\times$ was first conjectured by Lambert [4, Footnote 13], [7, pp. 127–128] in 1769. Euler [5, §38] gave a proof like that in Section 9 in 1773, with some gaps. Gauss [6, Art. 52–55] gave the proofs in Sections 2 and 7 in 1801, and cyclicity of $(\mathbf{Z}/(p))^\times$ is often attributed to him.

Unlike prime moduli, for most (but not all) composite $m$ the group $(\mathbf{Z}/(m))^\times$ is *not* cyclic. For example, $(\mathbf{Z}/(12))^\times$ has size 4 but its elements have order 1 or 2.

The following result is used in all but the last three proofs that $(\mathbf{Z}/(p))^\times$ is cyclic, so we state it now and will prove it in Appendix A.

**Theorem 1.1.** *Let $f(T)$ be a non-constant polynomial with coefficients in $\mathbf{Z}/(p)$, of degree $d$. Then $f(T)$ has at most $d$ roots in $\mathbf{Z}/(p)$.*

What we need from Theorem 1.1 is the special case $f(T) = T^d - 1$: the congruence $t^d - 1 \equiv 0 \bmod p$ has at most $d$ solutions in $\mathbf{Z}/(p)$, or equivalently, there are at most $d$ solutions to the equation $t^d - 1 = 0$ in $\mathbf{Z}/(p)$. The upper bound $d$ can break down in $\mathbf{Z}/(m)$ for non-prime $m$, e.g., the polynomial $T^2 - 1$ has *four* solutions in $\mathbf{Z}/(8)$.

Appendix B discusses when a nonzero integer generates $(\mathbf{Z}/(p))^\times$ as $p$ varies.

## 2. First Proof: Counting Elements of All Orders

For our first proof that $(\mathbf{Z}/(p))^\times$ is cyclic, we are going to count the elements with various orders. In $(\mathbf{Z}/(p))^\times$, which has size $p - 1$, the order of each element divides $p - 1$. For each positive divisor of $p - 1$, say $d$, let $N_p(d)$ be the number of elements of order $d$ in $(\mathbf{Z}/(p))^\times$. For instance, $N_p(1) = 1$ and the cyclicity of $(\mathbf{Z}/(p))^\times$, which we want to prove, is equivalent to $N_p(p - 1) > 0$. Every element has some order, and the order of each element divides $p - 1$, so counting the elements of $(\mathbf{Z}/(p))^\times$ by their order yields

$$\sum_{d \mid (p-1)} N_p(d) = p - 1. \tag{2.1}$$

[^1]: Generators for the nonzero elements of a finite field not of the form $\mathbf{Z}/(p)$ have applications. For example, QR codes use a generator of the nonzero elements of a field with order 256.

<!-- page 2 -->

**Theorem 2.1.** *Let $d \in \mathbf{Z}^+$. If $N_p(d) > 0$, then $N_p(d) = \varphi(d)$.*

*Proof.* When $N_p(d) > 0$, there is an element of order $d$ in $(\mathbf{Z}/(p))^\times$, say $a$. Then the different solutions to $x^d = 1$ are $1, a, a^2, \ldots, a^{d-1}$. There are at most $d$ solutions of $x^d = 1$ in $\mathbf{Z}/(p)$, by Theorem 1.1, and there are $d$ different powers of $a$, so the powers of $a$ provide *all* the solutions to $x^d = 1$ in $\mathbf{Z}/(p)$. Each element of order $d$ is a solution to $x^d = 1$, and therefore the elements of order $d$ in $(\mathbf{Z}/(p))^\times$ are exactly the powers $a^k$ that have order $d$. Since $a^k$ has order $d/(k, d)$, which is $d$ exactly when $(k, d) = 1$, $N_p(d)$ is the number of $k$ from 1 to $d$ that are relatively prime to $d$. That number is $\varphi(d)$. $\square$

Now we can say, for all $d \in \mathbf{Z}^+$, that

$$N_p(d) \leq \varphi(d). \tag{2.2}$$

Indeed, Theorem 2.1 tells us that $N_p(d) = 0$ or $N_p(d) = \varphi(d)$. We now feed (2.2) into (2.1):

$$p - 1 = \sum_{d \mid (p-1)} N_p(d) \leq \sum_{d \mid (p-1)} \varphi(d). \tag{2.3}$$

We have obtained an inequality for each prime $p$:

$$p - 1 \leq \sum_{d \mid (p-1)} \varphi(d). \tag{2.4}$$

If there is some $d$ dividing $p - 1$ for which the inequality in (2.2) is strict (that is, $N_p(d) < \varphi(d)$), then the inequality in (2.3) would be strict, and thus the inequality in (2.4) would be strict. How sharp is (2.4)? Let's look at some examples.

**Example 2.2.** If $p = 5$, then $\sum_{d \mid 4} \varphi(d) = \varphi(1) + \varphi(2) + \varphi(4) = 1 + 1 + 2 = 4$.

**Example 2.3.** If $p = 11$, then $\sum_{d \mid 10} \varphi(d) = \varphi(1) + \varphi(2) + \varphi(5) + \varphi(10) = 1 + 1 + 4 + 4 = 10$.

**Example 2.4.** If $p = 29$, then $\sum_{d \mid 28} \varphi(d) = \varphi(1) + \varphi(2) + \varphi(4) + \varphi(7) + \varphi(14) + \varphi(28) = 1 + 1 + 2 + 6 + 6 + 12 = 28$.

It appears that (2.4) might be an equality! This inspires us to prove it, and the appearance of $p - 1$ in (2.4) is not essential.

**Theorem 2.5.** *For every positive integer $n$, $\sum_{d \mid n} \varphi(d) = n$. In particular, for each prime number $p$ we have $\sum_{d \mid (p-1)} \varphi(d) = p - 1$.*

*Proof.* We will count the $n$ fractions

$$\frac{1}{n}, \frac{2}{n}, \ldots, \frac{n-1}{n}, \frac{n}{n} \tag{2.5}$$

according to their denominators when the fractions are put in reduced form.

For such a fraction $m/n$ with denominator $n$, its reduced form denominator is a divisor of $n$. How many of these reduced form fractions have a given denominator? Writing $m/n = a/d$, where $(a, d) = 1$, the condition $1 \leq m \leq n$ is equivalent to $1 \leq a \leq d$. Therefore the number of fractions in (2.5) with reduced form denominator $d$ is the number of $a$ from 1 to $d$ with $(a, d) = 1$. There are $\varphi(d)$ such numbers. Thus, counting the fractions in (2.5) according to their reduced form denominators, we get

$$n = \sum_{d \mid n} \varphi(d). \tag*{$\square$}$$

<!-- page 3 -->

Theorem 2.5 tells us (2.4) is an equality, so the inequalities in (2.2) must all be equalities. (Reread the discussion right after (2.4) if you don't see this.) Therefore $N_p(d) = \varphi(d)$ for each $d$ dividing $p - 1$. In particular, $N_p(p - 1) > 0$, so there is an element of $(\mathbf{Z}/(p))^\times$ with order $p - 1$. We've (non-constructively) proved the existence of a generator of $(\mathbf{Z}/(p))^\times$.

Let's summarize the argument again.

**Theorem 2.6.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* For $d \in \mathbf{Z}^+$, let $N_p(d)$ be the number of elements of order $d$ in $(\mathbf{Z}/(p))^\times$. By Theorem 2.1, $N_p(d) \leq \varphi(d)$. Therefore

$$p - 1 = \sum_{d \mid (p-1)} N_p(d) \leq \sum_{d \mid (p-1)} \varphi(d).$$

By Theorem 2.5, the sum on the right is $p - 1$, so the $\leq$ is an equality. Thus the inequalities $N_p(d) \leq \varphi(d)$ for all $d$ dividing $p - 1$ have to be equalities. In particular, $N_p(p-1) = \varphi(p-1)$, which is positive, so there is an element of $(\mathbf{Z}/(p))^\times$ with order $p - 1$. $\square$

## 3. Second Proof: One Subgroup Per Size

We begin our next proof by establishing a divisibility property among orders of elements that is peculiar to finite *abelian* groups. In a finite group, all elements have order dividing the size of the group. In the abelian setting all orders also divide something else: the maximal order.

**Lemma 3.1.** *Let $G$ be a finite abelian group. If $n$ is the maximal order among the elements in $G$, then the order of every element divides $n$.*

For example, in $(\mathbf{Z}/(56))^\times$, which has size 24, the orders of elements turn out to be 1, 2, 3, and 6. All orders divide the maximal order 6. In $S_4$, also of size 24, the orders of elements are 1, 2, 3, and 4. Note 3 does not divide the maximal order 4. Lemma 3.1 does not apply to $S_4$, as $S_4$ is non-abelian.

The reader might want to jump ahead to Theorem 3.3 to see how Lemma 3.1 gets used, before diving into the proof of Lemma 3.1.

*Proof.* Let $g$ have the maximal order $n$. Pick $h \in G$, and let $h \in G$ have order $m$. We want to show $m \mid n$. We will assume $m$ does not divide $n$ (this forces $m > 1$) and use this non-divisibility to construct an element with order exceeding $n$. That would be a contradiction, so $m \mid n$.

For instance, if $(m, n) = 1$, then $gh$ has order $mn > n$. But that is too easy: we can't expect $m$ to have no factors in common with $n$. How can we use $g$ and $h$ to find an element with order larger than $n$ just from knowing $m$ (the order of $h$) does not divide $n$ (the order of $g$)? The following example will illustrate the idea before we carry it out in general.

**Example 3.2.** Suppose $n = 96$ and $m = 18$. (That is, $g$ has order 96 and $h$ has order 18.) Look at the prime factorizations of these numbers:

$$96 = 2^5 \cdot 3, \quad 18 = 2 \cdot 3^2.$$

Here $m$ does not divide $n$ because there are more 3's in $m$ than in $n$. The least common multiple of $m$ and $n$ is $2^5 \cdot 3^2$, which is larger than $n$. We can get an element of that order by reduction to the relatively prime order case: kill the 3 in 96 by working with $g^3$ and kill the 2 in 18 by working with $h^2$. That is, $g^3$ has order $96/3 = 2^5$ and $h^2$ has order $18/2 = 9$.

<!-- page 4 -->

These orders are relatively prime, and the group is abelian, so the product $g^3 h^2$ has order $2^5 \cdot 9 > 96$. Thus, 96 is not the maximal order in the group.

Now we return to the general case. If $m$ does not divide $n$, then there is some prime $p$ whose multiplicity (exponent) as a factor of $m$ exceeds that of $n$. Let $p^e$ be the highest power of $p$ in $m$ and $p^f$ be the highest power of $p$ in $n$, so $e > f$. (Quite possibly $f = 0$, although in Example 3.2 both $e$ and $f$ were positive.)

Now consider $g^{p^f}$ and $h^{m/p^e}$. The first has order $n/p^f$, which is *not* divisible by $p$, and the second has order $p^e$, which is a pure $p$-power. These orders are *relatively prime*. In an abelian group, if $g_1$ has order $n_1$ and $g_2$ has order $n_2$ with $(n_1, n_2) = 1$, then $g_1 g_2$ has order $n_1 n_2$[^2] so $g^{p^f} h^{m/p^e}$ has order

$$\frac{n}{p^f} p^e = n p^{e-f} > n.$$

This contradicts the maximality of $n$ as an order in $G$, so we have a contradiction. $\square$

The following theorem will be our criterion for showing a group is cyclic. Recall that in a cyclic group there is just one subgroup of each size that occurs. Assuming the group is abelian, the converse holds.

**Theorem 3.3.** *Let $G$ be a finite abelian group with at most one subgroup per size. Then $G$ is cyclic.*

*Proof.* Let $n$ be the maximal order among the elements of $G$, and let $g \in G$ be an element with order $n$. We will show every element of $G$ is a power of $g$, so $G = \langle g \rangle$.

Pick $h \in G$, and say $h$ has order $d$. Since $d \mid n$ by Lemma 3.1, we can write down another element of order $d$: $g^{n/d}$. Thus we have two subgroups of size $d$: $\langle h \rangle$ and $\langle g^{n/d} \rangle$. By hypothesis, these subgroups are the same: $\langle h \rangle = \langle g^{n/d} \rangle$. In particular, $h \in \langle g^{n/d} \rangle \subset \langle g \rangle$, so $h$ is a power of $g$. Since $h$ was arbitrary in $G$, $G = \langle g \rangle$. $\square$

**Remark 3.4.** Is the abelian hypothesis in Theorem 3.3 necessary? That is, is there a non-abelian group with at most one subgroup of each size? No. A finite group with at most one subgroup of each size must be cyclic, even if we don't assume at first that the group is abelian. However, to prove this without an abelian hypothesis is quite a bit more involved than the proof of Theorem 3.3. (Where did we use the abelian hypothesis in the proof of Theorem 3.3?)

Now we are ready to show $(\mathbf{Z}/(p))^\times$ is cyclic.

**Theorem 3.5.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* We will show $(\mathbf{Z}/(p))^\times$ satisfies the hypothesis of Theorem 3.3: it has at most one subgroup per size. Let $H \subset (\mathbf{Z}/(p))^\times$ be a subgroup, with size (say) $d$. Then every $a \in H$ satisfies $a^d = 1$ in $\mathbf{Z}/(p)$, so $H$ is a subset of the solutions to $x^d = 1$. By Theorem 1.1, there are at most $d$ solutions to $x^d = 1$ in $\mathbf{Z}/(p)$. Since $d$ is the size of $H$ (by definition), we filled up the solutions of $x^d = 1$ in $\mathbf{Z}/(p)$ using $H$:

$$H = \{x \in \mathbf{Z}/(p) : x^d = 1\}.$$

The right side is determined by $d$ (and $p$), so there is at most one subgroup of $(\mathbf{Z}/(p))^\times$ with size $d$, for each $d$. Thus Theorem 3.3 applies, which shows $(\mathbf{Z}/(p))^\times$ is cyclic. $\square$

[^2]: If we drop the condition $(n_1, n_2) = 1$ then we can always say $g_1 g_2$ has order *dividing* $[n_1, n_2]$ since $(g_1 g_2)^{[n_1, n_2]} = g_1^{[n_1, n_2]} g_2^{[n_1, n_2]} = 1$, but $[n_1, n_2]$ is *not* a formula for the order of $g_1 g_2$ in general. For example, if $g$ has order $n > 1$ then $g^{-1}$ has order $n$ and $g g^{-1} = 1$ has order 1 while $[n, n] = n > 1$.

<!-- page 5 -->

## 4. Third Proof: Bounding with the Maximal Order

Our next proof that $(\mathbf{Z}/(p))^\times$ is cyclic will apply Lemma 3.1 from Section 3, but in a different way. That lemma says that in a finite abelian group, the order of each element divides the maximal order of the elements in the group. Review Lemma 3.1 after seeing how it gets used here.

**Theorem 4.1.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* Let $n$ be the maximal order among the elements in $(\mathbf{Z}/(p))^\times$. We want to show $n = p - 1$, so there is an element of order $p - 1$. Obviously $n \leq p - 1$. (More precisely, $n \mid (p-1)$, but the crude inequality will suffice.)

Every element has order dividing $n$, by Lemma 3.1, so each $a \in (\mathbf{Z}/(p))^\times$ satisfies $a^n = 1$. Theorem 1.1 says the equation $x^n = 1$ has at most $n$ solutions in $\mathbf{Z}/(p)$. We already produced $p - 1$ different solutions (namely all of $(\mathbf{Z}/(p))^\times$), so $p - 1 \leq n$.

Comparing the two inequalities, $n = p - 1$. Thus there is an element of $(\mathbf{Z}/(p))^\times$ with order $p - 1$, so $(\mathbf{Z}/(p))^\times$ is cyclic. $\square$

## 5. Fourth Proof: Induction and Homomorphisms, I

For this proof we will show something superficially stronger: every subgroup of $(\mathbf{Z}/(p))^\times$ is cyclic. This is superficially stronger because of the general theorem in group theory that every subgroup of a cyclic group is cyclic: it means that once $(\mathbf{Z}/(p))^\times$ is proved cyclic by some method, it follows that its subgroups are all cyclic. We are going to prove directly that all subgroups of $(\mathbf{Z}/(p))^\times$ are cyclic, rather than only that $(\mathbf{Z}/(p))^\times$ is cyclic, so that we can argue by induction on the order of the subgroup. I learned the argument below from David Feldman and Paul Monsky on Mathoverflow[^3].

**Theorem 5.1.** *For each prime $p$, every subgroup of $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* We argue by induction on the order of the subgroup of $(\mathbf{Z}/(p))^\times$.

The only subgroup of order 1 is the trivial subgroup, which is obviously cyclic.

Let $H$ be a subgroup of $(\mathbf{Z}/(p))^\times$ with order $n > 1$ and assume all subgroups of $(\mathbf{Z}/(p))^\times$ with order less than $n$ are cyclic. To prove $H$ is cyclic, we consider two cases.

**Case 1:** The order of $H$ is a prime power. Let $|H| = q^k$, where $q$ is prime. If $H$ is not cyclic, each element of $H$ has order dividing $q^k$ and not equal to $q^k$, so the order divides $q^{k-1}$ (since $q$ is prime). Then all $x \in H$ satisfy $x^{q^{k-1}} = 1$. That means the equation $x^{q^{k-1}} = 1$ has at least $q^k$ solutions in $\mathbf{Z}/(p)$ (namely all the elements of $H$), but the polynomial $T^{q^{k-1}} - 1$ has degree $q^{k-1}$, so the equation $x^{q^{k-1}} = 1$ has at most $q^{k-1}$ solutions in $\mathbf{Z}/(p)$ by Theorem 1.1. This is a contradiction, so $H$ must have an element of order $q^k$, so $H$ is cyclic.

**Case 2:** The order of $H$ is not a prime power. This means $n = |H|$ has at least two different prime factors, so we can write $n$ as $ab$ where $a > 1$, $b > 1$, and $(a, b) = 1$. (For example, let $a$ be the highest power of one prime dividing $n$ and $b = n/a$.) Let $f: H \to H$ by $f(x) = x^a$. This is a homomorphism since the group $H$ is abelian. For $x \in H$ we have $x^{ab} = x^n = 1$, so $f(x)^b = 1$. Thus we can say about the kernel and image of $f$ that

$$\ker f = \{x \in H : x^a = 1\}, \quad \mathrm{im}\, f \subset \{y \in H : y^b = 1\},$$

[^3]: See https://mathoverflow.net/questions/54735/collecting-proofs-that-finite-multiplicative-subgroups-of-fields-are-cyclic.

<!-- page 6 -->

so $|\ker f| \leq a < n$ and $|\mathrm{im}\, f| \leq b < n$ by Theorem 1.1. By induction, the subgroups $\ker f$ and $\mathrm{im}\, f$ are cyclic. That means $\ker f = \langle h \rangle$ and $\mathrm{im}\, f = \langle h' \rangle$ for some $h$ and $h'$ in $H$.

By the first isomorphism theorem for groups we have $H/\ker f \cong \mathrm{im}\, f$, so

$$|H| = |\ker f| |\mathrm{im}\, f| \leq ab = n = |H|.$$

Therefore the inequalities $|\ker f| \leq a$ and $|\mathrm{im}\, f| \leq b$ have to be equalities, so $h$ has order $a$ and $h'$ has order $b$. Since $(a, b) = 1$ and $h$ and $h'$ commute, by group theory $hh'$ has order $ab$, which is $|H|$. Thus $hh'$, which lies in $H$, is a generator of $H$, so $H$ is cyclic.

By this inductive argument all subgroups of $(\mathbf{Z}/(p))^\times$ are cyclic, so $(\mathbf{Z}/(p))^\times$ is cyclic. $\square$

## 6. Fifth Proof: Induction and Homomorphisms, II

Our next proof, due to David Leep [8, p. 171], uses ideas similar to those in Sections 3 and 5. Theorem 6.1 below is a special case of Theorem 3.3.

**Theorem 6.1.** *Let $G$ be a finite abelian group with at most one subgroup of order $q$ for each prime $q$ dividing $|G|$. Then $G$ is cyclic.*

*Proof.* We prove this by induction on $|G|$.

It is clear when $|G| = 1$. For $n \geq 2$, assume $|G| = n$ and the theorem is proved for all finite abelian groups of smaller order. The hypothesis on $G$ is true for its subgroups, so all proper subgroups of $G$ are cyclic.

There are elements of $G$ with prime order: pick a nontrivial element and let $m$ be its order, so $m > 1$. For a prime $q$ dividing $m$, the $(m/q)$-th power of something with order $m$ has order $q$.

Let $x \in G$ have a prime order $q$. Since $G$ is abelian, the function $f: G \to G$ where $f(g) = g^q$ is a homomorphism and $x$ is in its kernel. By the hypothesis on $G$, $\langle x \rangle$ is the only subgroup of $G$ with order $q$. Since a nontrivial element of $\ker f$ has order $q$, $\ker f = \langle x \rangle$. We have $G/\ker f \cong \mathrm{im}\, f$, so $|\mathrm{im}\, f| = n/q < n$. Since $\mathrm{im}\, f$ is a proper subgroup of $G$, $\mathrm{im}\, f$ is cyclic, say $\mathrm{im}\, f = \langle y \rangle$. Then $G$ contains elements $x$ of order $q$ and $y$ of order $n/q$. From $x$ and $y$ we get an element of $G$ with order $n$ (and thus a generator of $G$) by taking cases:

**Case 1:** $q \nmid n/q$. Since $q$ is prime, $(q, n/q) = 1$, so $xy$ has order $n$ because $x$ and $y$ commute.

**Case 2:** $q \mid n/q$. Write $y = z^q$ (here we use $y \in \mathrm{im}\, f$). Then $z^n = (z^q)^{n/q} = y^{n/q} = 1$ since $y$ has order $n/q$. We'll show $z$ has order $n$.

Let $m$ be the order of $z$. If $q \nmid m$, then $(q, m) = 1$, so $z^q$ also has order $m$. But $z^q = y$ has order $n/q$, which is divisible by $q$, so we have a contradiction. Thus $q \mid m$, so $z^q$ has order $m/q$. Also $z^q = y$ has order $n/q$, so $m/q = n/q$, which implies $m = n$. $\square$

**Remark 6.2.** If we remove the abelian assumption in Theorem 6.1 then there are counterexamples: $Q_8$ (and more broadly a generalized quaternion group $Q_{2^n}$ for $n \geq 3$) has only one subgroup of order 2 and it is not cyclic.[^4]

**Theorem 6.3.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* Let $q$ be a prime dividing $p - 1$. If there is a subgroup of $(\mathbf{Z}/(p))^\times$ with order $q$, say $H$, then the elements of $H$ are roots of $T^q - 1$. This polynomial has at most $q$ roots in $\mathbf{Z}/(p)$, and $|H| = q$, so $H$ is the full set of roots. Thus $H$ is the only subgroup of order $q$, so $(\mathbf{Z}/(p))^\times$ is cyclic by Theorem 6.1. $\square$

[^4]: In the first edition (p. 94) of [8], the statement of our Theorem 6.1 omits the condition that $G$ is abelian.

<!-- page 7 -->

## 7. Sixth Proof: Elements of Prime-Power Order

For the next proof that $(\mathbf{Z}/(p))^\times$ is cyclic we are going to use the prime factorization of $p - 1$. Say

$$p - 1 = q_1^{e_1} q_2^{e_2} \cdots q_m^{e_m},$$

where the $q_i$ are distinct primes and $e_i \geq 1$. (The case $p = 2$ is trivial, so we can suppose $p > 2$ and thus $p - 1 > 1$.) We will show there are elements of order $q_i^{e_i}$ for each $i$, and their product furnishes a generator of $(\mathbf{Z}/(p))^\times$.

As a warm-up, using Theorem 1.1 we will show for each prime $q$ dividing $p - 1$ that there is an element of order $q$ in $(\mathbf{Z}/(p))^\times$.

**Lemma 7.1.** *If $q$ is a prime dividing $p - 1$ then there is an element of $(\mathbf{Z}/(p))^\times$ with order $q$. Specifically, there is an $a \in (\mathbf{Z}/(p))^\times$ such that $a^{(p-1)/q} \not\equiv 1$, and necessarily $a^{(p-1)/q}$ has order $q$ in $(\mathbf{Z}/(p))^\times$.*

*Proof.* The equation $a^{(p-1)/q} = 1$ in $\mathbf{Z}/(p)$ has at most $(p-1)/q$ solutions in $\mathbf{Z}/(p)$ by Theorem 1.1, and $(p-1)/q$ is less than $p - 1 = |(\mathbf{Z}/(p))^\times|$, so $(\mathbf{Z}/(p))^\times$ has an element $a$ such that $a^{(p-1)/q} \neq 1$.

Set $b = a^{(p-1)/q}$ in $\mathbf{Z}/(p)$. Then $b \neq 1$ and $b^q = (a^{(p-1)/q})^q = a^{p-1} = 1$ by Fermat's little theorem, so the order of $b$ divides $q$ and is not 1. Since $q$ is prime, the only choice for the order of $b$ is $q$. $\square$

This proof is *not* saying that if $a^{(p-1)/q} \neq 1$ in $(\mathbf{Z}/(p))^\times$ then $a$ has order $q$ in $(\mathbf{Z}/(p))^\times$, but rather than $a^{(p-1)/q}$ has order $q$. Let's look at an example.

**Example 7.2.** Take $p = 19$. By Fermat's little theorem, all $a$ in $(\mathbf{Z}/(19))^\times$ satisfy $a^{18} = 1$. Since 18 is divisible by 3, the lemma is telling us that if $a^{18/3} \neq 1$ in $(\mathbf{Z}/(19))^\times$ then $a^{18/3}$ has order 3. From the second row of the table below, which samples over the nonzero numbers mod 19, we find just two different values of $a^6 \bmod 19$ other than 1: 7 and 11. They both have order 3. Many $a$ in $(\mathbf{Z}/(19))^\times$ have order greater than 3, e.g., 2 mod 19 has order 18.

| $a \bmod 19$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $a^6 \bmod 19$ | 1 | 7 | 7 | 11 | 7 | 11 | 1 | 1 | 11 | 11 | 1 | 1 | 11 | 7 | 11 | 7 | 7 | 1 |

If the prime $q$ divides $p - 1$ more than once, the same reasoning as in Lemma 7.1 will lead to elements of higher $q$-power order in $(\mathbf{Z}/(p))^\times$.

**Lemma 7.3.** *If $q$ is a prime and $q^e \mid (p-1)$ for a positive integer $e$, then there is an element of $(\mathbf{Z}/(p))^\times$ with order $q^e$. Specifically, there is an $a \in (\mathbf{Z}/(p))^\times$ such that $a^{(p-1)/q} \neq 1$ in $(\mathbf{Z}/(p))^\times$, and necessarily $a^{(p-1)/q^e}$ has order $q^e$ in $(\mathbf{Z}/(p))^\times$.*

*Proof.* As in the proof of Lemma 7.1, there are fewer than $p - 1$ solutions to $a^{(p-1)/q} = 1$ in $\mathbf{Z}/(p)$ by Theorem 1.1, so there is an $a$ in $(\mathbf{Z}/(p))^\times$ where $a^{(p-1)/q} \neq 1$ in $\mathbf{Z}/(p)$.

Set $b = a^{(p-1)/q^e}$, where $(p-1)/q^e$ is an integer (we do not use fractional exponents). Then $b^{q^e} = (a^{(p-1)/q^e})^{q^e} = a^{p-1} = 1$ in $(\mathbf{Z}/(p))^\times$ by Fermat's little theorem, so the order of $b$ divides $q^e$. Since $q$ is prime, the (positive) factors of $q^e$ other than $q^e$ are factors of $q^{e-1}$. Since $b^{q^{e-1}} = (a^{(p-1)/q^e})^{q^{e-1}} = a^{(p-1)/q} \neq 1$ in $(\mathbf{Z}/(p))^\times$, by the choice of $a$, the order of $b$ does not divide $q^{e-1}$. Thus the order of $b$ in $(\mathbf{Z}/(p))^\times$ has to be $q^e$. $\square$

**Example 7.4.** Returning to $p = 19$, the number $p - 1 = 18$ is divisible by the prime power 9. In the table below we list the $a$ for which $a^{(p-1)/3} = a^6 \neq 1$ and below that list the corresponding values of $a^{18/9} = a^2$: these are 4, 5, 6, 9, 16, and 17, and all have order 9.

<!-- page 8 -->

| $a \bmod 19$ | 2 | 3 | 4 | 5 | 6 | 9 | 10 | 13 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $a^6 \bmod 19$ | 7 | 7 | 11 | 7 | 11 | 11 | 11 | 11 | 7 | 11 | 7 | 7 |
| $a^2 \bmod 19$ | 4 | 9 | 16 | 6 | 17 | 5 | 5 | 17 | 6 | 16 | 9 | 4 |

**Remark 7.5.** Lemma 7.3 can be proved in another way using unique factorization of polynomials with coefficients in $\mathbf{Z}/(p)$. Because all nonzero numbers mod $p$ are roots of $T^{p-1} - 1$, this polynomial factors mod $p$ as $(T-1)(T-2)\cdots(T-(p-1))$. Being a product of distinct linear factors, every factor of $T^{p-1} - 1$ is also a product of distinct linear factors, so in particular, every factor of $T^{p-1} - 1$ has as many roots in $\mathbf{Z}/(p)$ as its degree. For a prime power $q^e$ dividing $p - 1$, $T^{q^e} - 1$ divides $T^{p-1} - 1$, so there are $q^e$ solutions of $a^{q^e} = 1$ in $\mathbf{Z}/(p)$. This exceeds the number of solutions of $a^{q^{e-1}} = 1$ in $\mathbf{Z}/(p)$, which is at most $q^{e-1}$ since a nonzero polynomial over a field has no more roots than its degree. Therefore there is an $a$ in $\mathbf{Z}/(p)$ fitting $a^{q^e} = 1$ and $a^{q^{e-1}} \neq 1$. All such $a$ have order $q^e$.

**Theorem 7.6.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* We may take $p > 2$, so $p - 1 > 1$. Write $p - 1$ as a product of primes:

$$p - 1 = q_1^{e_1} q_2^{e_2} \cdots q_m^{e_m}.$$

By Lemma 7.3, for each $i$ from 1 to $m$ there is some $b_i$ in $(\mathbf{Z}/(p))^\times$ with order $q_i^{e_i}$. These orders are relatively prime, and $(\mathbf{Z}/(p))^\times$ is abelian, so the product of the $b_i$'s has order equal to the product of the $q_i^{e_i}$'s, which is $p - 1$. Thus $b_1 b_2 \cdots b_m$ generates $(\mathbf{Z}/(p))^\times$. $\square$

**Remark 7.7.** The way we used Theorem 1.1 is that it tells us when $p > 2$ and $1 \leq d < p - 1$, there is a nonzero $a \bmod p$ such that $a^d \not\equiv 1 \bmod p$. Christophe Bertault [2] pointed out that the existence of such $a$ can be proved without properties of polynomials, by using a combinatorial argument. When $m$ and $n$ are positive integers, the number of surjective maps from an $m$-element set to an $n$-element set is $\sum_{k=1}^n (-1)^{n-k} \binom{n}{k} k^m$, so when $m < n$ we have $\sum_{k=1}^n (-1)^{n-k} \binom{n}{k} k^m = 0$. Therefore when $p$ is an odd prime and $d$ is a proper factor of $p - 1$, $\sum_{k=1}^{p-1} (-1)^{p-1-k} \binom{p-1}{k} k^d = 0$. This implies $k^d \not\equiv 1 \bmod p$ for some $k \in \{1, \ldots, p-1\}$, since otherwise $\sum_{k=1}^{p-1} (-1)^{p-1-k} \binom{p-1}{k} k^d \equiv \sum_{k=1}^{p-1} (-1)^k \binom{p-1}{k} \equiv (1-1)^{p-1} - 1 \equiv -1 \bmod p$, which contradicts the sum being 0.

Based on the proof of Theorem 7.6, here is a procedure to find a generator of $(\mathbf{Z}/(p))^\times$:

1. Get the prime factorization of $p - 1$, say $p - 1 = q_1^{e_1} q_2^{e_2} \cdots q_m^{e_m}$.
2. For each $q_i$, find an $a_i$ such that $a_i^{(p-1)/q_i} \not\equiv 1 \bmod p$.
3. By Lemma 7.3, $b_i := a_i^{(p-1)/q_i^{e_i}} \bmod p$ has order $q_i^{e_i}$ in $(\mathbf{Z}/(p))^\times$.
4. The product $b_1 b_2 \cdots b_m$ is a generator of $(\mathbf{Z}/(p))^\times$.

Here's an example.

**Example 7.8.** Take $p = 3943$, so $p - 1 = 3942 = 2 \cdot 3^3 \cdot 73$. We seek $b_1$ of order 2, $b_2$ of order 27, and $b_3$ of order 73. The product $b_1 b_2 b_3 \bmod p$ will have order $p - 1$.

- The first time $a^{(p-1)/2} \not\equiv 1 \bmod p$ is at $a = 3$: $3^{(p-1)/2} \equiv 3942 \equiv -1 \bmod p$. This has order 2.
- The first time $a^{(p-1)/3} \not\equiv 1 \bmod p$ is at $a = 3$: $3^{(p-1)/3} \equiv 1135 \bmod p$. Then $3^{(p-1)/27} \equiv 2387 \bmod p$ has order 27.
- The first time $a^{(p-1)/73} \not\equiv 1 \bmod p$ is at $a = 2$: $2^{(p-1)/73} \equiv 1406 \bmod p$, which has order 73.

<!-- page 9 -->

From these calculations, a generator of $(\mathbf{Z}/(p))^\times$ is $(-1)(2387)(1406) \equiv 3314 \bmod p$.

If we had instead tried $a = 2, 3, \ldots \bmod p$ by brute force to find a generator mod $p$ directly, then we'd have found 3 mod $p$ is a generator. (The order of 2 mod $p$ is 219.)

The bottleneck in this procedure is Step 1 (factoring $p - 1$) if $p$ is large. The other steps run quickly in practice. In order to find a large prime $p$ such that $p - 1$ has a known prime factorization, we usually find $p - 1$ first: pick a large number $n$ whose prime factorization is known and then test if $n + 1$ is prime by a deterministic or probabilistic primality test. If $n + 1$ is prime, then set $p = n + 1$. No matter what method is used to find a generator, Shoup [9, p. 340] pointed out that "there is no known way to efficiently recognize a [generator] modulo $p$ without knowing the prime factorization of $p - 1$."

## 8. Seventh Proof: Subgroups of Prime-Power Order

This proof will, like the previous proof, focus on prime power factors of $p - 1$.

Our new tool is the following theorem about finite abelian groups whose order is a prime power.

**Theorem 8.1.** *Let $A$ be a finite abelian group of order $q^s$, where $q$ is a prime. If $A$ is not cyclic, then there are more than $q$ solutions in $A$ to the equation $x^q = 1$.*

*Proof.* All elements of $A$ have $q$-power order. Since $A$ is not cyclic, $s \geq 2$. Let the maximal order of an element of $A$ be $q^t$, so $t < s$. Pick $g \in A$ with this order:

$$|\langle g \rangle| = q^t.$$

The element $g^{q^{t-1}}$ has order $q$, and its powers provide $q$ solutions to the equation $x^q = 1$. We now aim to find an element of $A$ with order $q$ that is outside of the subgroup $\langle g \rangle$. This will provide another solution to $x^q = 1$, and thus prove the theorem.

For $h \in A$ with $h \notin \langle g \rangle$, there is some $q$-power $h^{q^k}$ that lies in $\langle g \rangle$. After all, $h$ has $q$-power order, so at the very least some $q$-power of $h$ is the identity (which is in $\langle g \rangle$). Necessarily $k \geq 1$. It may happen that the first $q$-power of $h$ that lands in $\langle g \rangle$ is not the identity. After all, a $q$-power of $h$ could land inside $\langle g \rangle$ before we run through every possible power of $h$ (hitting the identity at the last exponent).

Let $\ell$ be the smallest integer $\geq 1$ such that some element in $A$ outside of $\langle g \rangle$ has its $q^\ell$-th power inside $\langle g \rangle$. We claim $\ell = 1$. That is, some element outside $\langle g \rangle$ has its $q$-th power inside $\langle g \rangle$. Indeed, suppose $\ell > 1$ and let $h_0$ be an element outside of $\langle g \rangle$ with $h_0^{q^\ell} \in \langle g \rangle$. Then $h_0^{q^{\ell-1}} \notin \langle g \rangle$ by minimality of $\ell$, yet this element itself satisfies $(h_0^{q^{\ell-1}})^q \in \langle g \rangle$, so there is an element whose '$\ell$' is 1. Thus $\ell = 1$.

Take $h_1$ to be such an element outside $\langle g \rangle$ with $h_1^q \in \langle g \rangle$, say $h_1^q = g^n$. Since $h_1$ has (like all elements of $A$) order dividing $q^t$, the order of $h_1^q$ is at most $q^{t-1}$. Then $g^n$ has order at most $q^{t-1}$, so $q$ must divide $n$. (Otherwise $n$ is relatively prime to the order of $g$, which would imply $g^n = h_1^q$ has order $q^t$, and that is not correct.) Setting $n = qr$, we have

$$h_1^q = g^{qr}.$$

Then $(h_1 g^{-r})^q = 1$ and $h_1 g^{-r} \notin \langle g \rangle$ (after all, $h_1 \notin \langle g \rangle$), so $h_1 g^{-r}$ is an element of order $q$ in $A$ that lies outside of $\langle g \rangle$. $\square$

**Remark 8.2.** In Remark 3.4, it was noted that Theorem 3.3 is true (but harder to prove) without an abelian hypothesis. What about Theorem 8.1? Is its conclusion correct if we don't make an initial abelian hypothesis? Yes if $q$ is an odd prime, but no if $q = 2$. For

<!-- page 10 -->

instance, $Q_8$ is not cyclic but it has only two solutions to $x^2 = 1$. This is not a quirk about $Q_8$: there are infinitely many non-abelian groups of 2-power order having only two solutions to $x^2 = 1$, such as the generalized quaternion groups $Q_{2^n}$ for $n \geq 3$.[^5]

**Theorem 8.3.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* We may take $p > 2$, so $p - 1 > 1$. Write $p - 1 = q_1^{e_1} q_2^{e_2} \cdots q_m^{e_m}$, where the $q_i$'s are different primes (and each $e_i$ is positive). Set

$$A_i = \{a \in (\mathbf{Z}/(p))^\times : a^{q_i^{e_i}} = 1\}.$$

This is a subgroup of $(\mathbf{Z}/(p))^\times$, and all of its elements have $q_i$-power order, so $|A_i|$ is a power of $q_i$ by Cauchy's theorem.

If $A_i$ is *not* cyclic, then Theorem 8.1 says $A_i$ has more than $q_i$ solutions to the equation $x^{q_i} = 1$. However, we know this equation has no more than $q_i$ solutions in $\mathbf{Z}/(p)$ by Theorem 1.1. Thus we have reached a contradiction, so $A_i$ is cyclic. (We do not yet know the order of $A_i$, except that it is a $q_i$-power. We may expect, though, that $|A_i| = q_i^{e_i}$.)

Write $A_i = \langle a_i \rangle$. We are going to show $a_1, a_2, \ldots, a_m$ together generate $(\mathbf{Z}/(p))^\times$. Then we will show the single product $a_1 a_2 \cdots a_m$ is a generator of the group.

Dividing $p - 1$ by each of $q_1^{e_1}, \ldots, q_m^{e_m}$, we get the integers

$$\frac{p-1}{q_1^{e_1}}, \frac{p-1}{q_2^{e_2}}, \ldots, \frac{p-1}{q_m^{e_m}}.$$

These have no collective common prime factor, so some $\mathbf{Z}$-combination of them is equal to 1 (iterated Bezout?):

$$\sum_{i=1}^m c_i \frac{p-1}{q_i^{e_i}} = 1,$$

where $c_i \in \mathbf{Z}$. Then each $a \in (\mathbf{Z}/(p))^\times$ can be written as

$$a = a^1 = a^{\sum_i c_i(p-1)/q_i^{e_i}} = \prod_{i=1}^m a^{c_i(p-1)/q_i^{e_i}}.$$

Since the $i$-th factor has order dividing $q_i^{e_i}$ (raise it to the $q_i^{e_i}$-th power as a check), it lies in $A_i$ and thus the $i$-th factor is a power of $a_i$. Therefore $a$ is a product of powers of the $a_i$'s, which means

$$(\mathbf{Z}/(p))^\times = \langle a_1, a_2, \ldots, a_m \rangle.$$

To end the proof, we show that each product of powers $a_1^{n_1} a_2^{n_2} \cdots a_m^{n_m}$ is equal to a single power $(a_1 a_2 \cdots a_m)^n$. Considering that each $a_i$ has order dividing $q_i^{e_i}$, we could find such an $n$ by trying to solve the simultaneous congruences

$$n \equiv n_1 \bmod q_1^{e_1}, \; n \equiv n_2 \bmod q_2^{e_2}, \; \ldots, \; n \equiv n_m \bmod q_m^{e_m}.$$

(Then $a_i^{n_i} = a_i^n$.) Can we solve all of these congruences with a common $n$? Absolutely: the moduli are pairwise relatively prime, so just use the Chinese Remainder Theorem. $\square$

**Remark 8.4.** The arguments in this proof really showed something quite general about finite abelian groups. If $A$ is a finite abelian group and $p$ is a prime, let $A_p$ be the subgroup of elements with $p$-power order. Then $A$ is cyclic if and only if $A_p$ is cyclic for every $p$. (If $p$ does not divide $|A|$, then $A_p$ is trivial.)

[^5]: See https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf, especially Corollary 4.3.

<!-- page 11 -->

## 9. Eighth Proof: Cyclotomic Polynomials

For this proof we will actually write down a polynomial factor of $T^{p-1} - 1$ whose roots in $\mathbf{Z}/(p)$ are the generators of $(\mathbf{Z}/(p))^\times$! It sounds like a constructive proof, but there is a catch: while we will construct a polynomial and show each of its roots in $\mathbf{Z}/(p)$ generates $(\mathbf{Z}/(p))^\times$, the proof of the existence of these roots in $\mathbf{Z}/(p)$ will give no recipe for finding them (and thus no recipe for finding a generator of $(\mathbf{Z}/(p))^\times$). So the roots are left to be found by a brute force search. This one uses unique factorization for polynomials with coefficients in $\mathbf{Z}/(p)$, which we previous met in Remark 7.5.

The new polynomials we will meet are the *cyclotomic polynomials*. We will define them first as polynomials with complex coefficients. Then we will prove that their coefficients are in fact integers, so it makes sense to reduce the coefficients modulo $p$. Finally we will show one of the cyclotomic polynomials, when reduced modulo $p$, decomposes into linear factors and each of its roots in $\mathbf{Z}/(p)$ is a generator of $(\mathbf{Z}/(p))^\times$.

In the complex numbers, let $\rho_n$ be the basic $n$-th root of unity $\cos(2\pi/n) + i\sin(2\pi/n) = e^{2\pi i/n}$. It has order $n$ and the other roots of unity with order $n$ are $\rho_n^j$ where $1 \leq j \leq n$ and $(j, n) = 1$. Define the $n$-th cyclotomic polynomial $\Phi_n(T)$ to be the polynomial having for its roots the roots of unity in $\mathbf{C}$ with order $n$:

$$\Phi_n(T) := \prod_{\substack{j=1 \\ (j,n)=1}}^n (T - \rho_n^j). \tag{9.1}$$

For instance, $\Phi_1(T) = T - 1$, $\Phi_2(T) = T + 1$, and $\Phi_4(T) = (T - i)(T + i) = T^2 + 1$.

Since (9.1) is a product of linear polynomials, indexed by integers from 1 to $n$ that are relatively prime to $n$, $\Phi_n(T)$ has degree $\varphi(n)$ (hence the notation for the polynomial itself; $\Phi$ is a capital Greek $\varphi$). While the definition of $\Phi_n(T)$ involves complex linear factors, the polynomials themselves, after all the factors are multiplied out, actually have integer coefficients. Here is a table listing the first 12 cyclotomic polynomials.

| $n$ | $\Phi_n(T)$ |
|---|---|
| 1 | $T - 1$ |
| 2 | $T + 1$ |
| 3 | $T^2 + T + 1$ |
| 4 | $T^2 + 1$ |
| 5 | $T^4 + T^3 + T^2 + T + 1$ |
| 6 | $T^2 - T + 1$ |
| 7 | $T^6 + T^5 + T^4 + T^3 + T^2 + T + 1$ |
| 8 | $T^4 + 1$ |
| 9 | $T^6 + T^3 + 1$ |
| 10 | $T^4 - T^3 + T^2 - T + 1$ |
| 11 | $T^{10} + T^9 + T^8 + T^7 + T^6 + T^5 + T^4 + T^3 + T^2 + T + 1$ |
| 12 | $T^4 - T^2 + 1$ |

There are evidently a lot of patterns worth exploring here. For instance, $\Phi_8$ resembles $\Phi_4$, which resembles $\Phi_2$, $\Phi_{10}$ is similar to $\Phi_5$, and $\Phi_{12}$ seems related to $\Phi_6$, which is close to $\Phi_3$. The constant term of $\Phi_n(T)$, for $n > 1$, seems to be 1. Maybe the most striking pattern, which persists for the first 100 cyclotomic polynomials, is that the coefficients are all 0, 1, or $-1$. We will not determine whether or not this is always true (life needs some

<!-- page 12 -->

tantalizing mysteries), but let's show at least that all the coefficients are integers. First a factorization lemma is needed.

**Lemma 9.1.** *For $n \geq 1$, $T^n - 1 = \prod_{d \mid n} \Phi_d(T)$.*

*Proof.* If $\rho$ is an $n$th root of unity then $\rho$ is a root of $T^n - 1$, so $T - \rho$ is a factor of $T^n - 1$. (see Lemma A.2). Thus, $T^n - 1$ is divisible by each $T - \rho$ as $\rho$ runs over the $n$th roots of unity. The factors $T - \rho$ for different $\rho$ are pairwise relatively prime to each other since they're linear with different roots, so (using an analogue of Bezout's identity[^6]) their product is a factor of $T^n - 1$:

$$T^n - 1 = \prod_{\rho^n = 1} (T - \rho) h(T) \tag{9.2}$$

for some polynomial $h(T)$. Comparing degrees on both sides, we see $h(T)$ has degree 0, so $h(T)$ is a constant. Now comparing leading coefficients on both sides, we must have $h(T) = 1$. Thus

$$T^n - 1 = \prod_{\rho^n = 1} (T - \rho). \tag{9.3}$$

Every $n$-th root of unity has some order dividing $n$. For each $d$ dividing $n$, collect together the linear factors $T - \rho$ corresponding to roots of unity with order $d$. The product of these factors is $\Phi_d(T)$, by the definition of $\Phi_d(T)$. Thus, we have transformed (9.3) into the desired formula. $\square$

**Example 9.2.** Taking $n = 4$,

$$\prod_{d \mid 4} \Phi_d(T) = \Phi_1(T)\Phi_2(T)\Phi_4(T) = (T-1)(T+1)(T^2+1) = T^4 - 1.$$

**Example 9.3.** Taking $n = p$ a prime number, $T^p - 1 = (T-1)\Phi_p(T)$. Thus, we can explicitly compute

$$\Phi_p(T) = \frac{T^p - 1}{T - 1} = 1 + T + T^2 + \cdots + T^{p-1}.$$

Notice the coefficients here all equal 1.

**Theorem 9.4.** *For every $n \geq 1$, the coefficients of $\Phi_n(T)$ are in $\mathbf{Z}$.*

*Proof.* We will argue by induction on $n$. Since $\Phi_1(T) = T - 1$, we can take $n > 1$ and assume $\Phi_m(T)$ has integer coefficients for $m < n$. In Lemma 9.1, we can pull out the term at $d = n$:

$$T^n - 1 = \prod_{\substack{d \mid n \\ d \neq n}} \Phi_d(T) \cdot \Phi_n(T). \tag{9.4}$$

Let $B_n(T) = \prod_{d \mid n, d \neq n} \Phi_d(T)$, so

$$T^n - 1 = B_n(T) \Phi_n(T). \tag{9.5}$$

By induction, $\Phi_d(T)$ has integer coefficients when $d$ is a proper divisor of $n$, so $B_n(T)$ has integer coefficients. Each $\Phi_d(T)$ has leading coefficient 1, so $B_n(T)$ does as well. All we

[^6]: See Corollaries 4.2 and 4.3 and the generalizations of them at the end of https://kconrad.math.uconn.edu/blurbs/ugradnumthy/divgcd.pdf as well as https://kconrad.math.uconn.edu/blurbs/ugradnumthy/analogypoly.pdf.

<!-- page 13 -->

know about $\Phi_n(T)$ is that it has complex coefficients. We want to deduce from (9.5) that its coefficients are integers.

Let's cook up a second divisibility relation between $T^n - 1$ and $B_n(T)$ in a completely different way: the usual division of (complex) polynomials, leaving a quotient and remainder. We have

$$T^n - 1 = B_n(T) Q(T) + R(T), \tag{9.6}$$

where $R(T) = 0$ or $0 \leq \deg R < \deg B_n$. When we divide one polynomial by another and both have integer coefficients, the quotient and remainder may not have integer coefficients. For instance,

$$T^2 + 1 = (2T + 1)\left(\frac{1}{2}T - \frac{1}{4}\right) + \frac{5}{4}.$$

However, if the divisor has leading coefficient 1, then everything stays integral, e.g., $T^2 + 1 = (T+1)(T-1) + 2$. Briefly, the source of all denominators in the quotient and remainder comes from the leading coefficient of the divisor, so when it is 1, no denominators are introduced. Thus, since $B_n(T)$ has integer coefficients and leading coefficient 1, $Q(T)$ and $R(T)$ have integer coefficients.

We now compare our two relations (9.5) and (9.6). Since division of polynomials (with, say, complex coefficients) has *unique* quotient and remainder, we must have $\Phi_n(T) = Q(T)$ and $0 = R(T)$. In particular, since $Q(T)$ has integer coefficients, we have proved $\Phi_n(T)$ has integer coefficients! $\square$

**Lemma 9.5.** *Working with coefficients in $\mathbf{Z}/(p)$, the polynomial $T^{p-1} - 1$ is a product of linear factors:*

$$T^{p-1} - 1 = (T-1)(T-2)(T-3)\cdots(T-(p-1)).$$

*Proof.* For every $a \not\equiv 0 \bmod p$, $a^{p-1} \equiv 1 \bmod p$, or $a^{p-1} = 1$ in $\mathbf{Z}/(p)$. Therefore the polynomial $T^{p-1} - 1$, considered over $\mathbf{Z}/(p)$, has $a$ as a root. Since $a$ is a root, $T - a$ is a factor and the same reasoning used to get (9.2) implies

$$T^{p-1} - 1 = (T-1)(T-2)(T-3)\cdots(T-(p-1))h(T)$$

for a polynomial $h(T)$. Comparing degrees and then leading coefficients on both sides, $h(T) = 1$. $\square$

**Theorem 9.6.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* Consider the factorization

$$T^{p-1} - 1 = \prod_{d \mid (p-1)} \Phi_d(T). \tag{9.7}$$

All polynomials appearing here have integer coefficients. Collect the $\Phi_d(T)$ with $d \neq p - 1$ into a single term:

$$T^{p-1} - 1 = \Phi_{p-1}(T) H(T), \tag{9.8}$$

where $H(T)$ has integer coefficients.

Reducing the coefficients in (9.8) modulo $p$ lets us view (9.8) as a polynomial identity over $\mathbf{Z}/(p)$. By Lemma 9.5, the left side of (9.8) breaks up into distinct linear factors over $\mathbf{Z}/(p)$. Therefore, by unique factorization for polynomials with coefficients in $\mathbf{Z}/(p)$, the two factors on the right side of (9.8) are products of linear polynomials over $\mathbf{Z}/(p)$ (as many linear polynomials as the degree of the factor). Therefore $\Phi_{p-1}(T)$ has a root in $\mathbf{Z}/(p)$; in

<!-- page 14 -->

fact, it has $\varphi(p-1)$ roots in $\mathbf{Z}/(p)$. We will show each $a \in \mathbf{Z}/(p)$ that is a root of $\Phi_{p-1}(T)$ has order $p - 1$, so it is a generator of $(\mathbf{Z}/(p))^\times$.

Since 0 is not a root of $T^{p-1} - 1$, $a \in (\mathbf{Z}/(p))^\times$. Let $d$ be the order of $a$ in $(\mathbf{Z}/(p))^\times$, so $d \mid p - 1$. Could we have $d < p - 1$? Assume so. (We will get a contradiction and then we will be done.) Since $d$ is the order of $a$, $a^d - 1 = 0$ in $\mathbf{Z}/(p)$. Now consider the factorization of $T^d - 1$ given by Lemma 9.1:

$$T^d - 1 = \prod_{k \mid d} \Phi_k(T).$$

This identity between polynomials with integer coefficients can be viewed as an identity between polynomials with coefficients in $\mathbf{Z}/(p)$ by reducing all the coefficients modulo $p$. Setting $T = a$ in this formula, the left side vanishes (in $\mathbf{Z}/(p)$), so $\Phi_k(a)$ is 0 for some $k$ dividing $d$. (In fact, it is $\Phi_d(a)$ that vanishes, but we don't need to know that.) Once $\Phi_k(a)$ vanishes, Lemma A.2 tells us $T - a$ is a factor of $\Phi_k(T)$. Thus, in (9.7), $T - a$ is a factor *twice*: once in $\Phi_{p-1}(T)$ (that is how we defined $a$) and also as a factor in $\Phi_k(T)$ for some $k$ dividing $d$. But the factorization of $T^{p-1} - 1$ in Lemma 9.5 has *distinct* linear factors. We have a contradiction to unique factorization, so our assumption that $d < p - 1$ is in error: $d = p - 1$, so $a$ is a generator of $(\mathbf{Z}/(p))^\times$. $\square$

**Example 9.7.** Taking $p = 7$, $\Phi_{p-1}(T) = \Phi_6(T) = T^2 - T + 1$. Its roots in $\mathbf{Z}/(7)$ are 3 and 5: $\Phi_6(3) = 7 \equiv 0 \bmod 7$ and $\Phi_6(5) = 21 \equiv 0 \bmod 7$. The numbers 3 and 5 are the generators of $(\mathbf{Z}/(7))^\times$, as you can check directly.

## 10. Ninth Proof: $p$-adic Lifting

This proof, which is due to Matt Baker [1], uses $p$-adic numbers and the math of Galois theory. If you know about $p$-adic numbers then you'll find it amusing. If you don't know $p$-adic numbers and Galois theory, then ignore this section.

The polynomial $T^{p-1} - 1$ splits completely over $\mathbf{Z}/(p)$ with $p - 1$ different roots (every nonzero integer mod $p$ is a root of it), so by Hensel's lemma this polynomial also splits completely in $\mathbf{Z}_p[T]$, where $\mathbf{Z}_p$ is the $p$-adic integers. Let $r_{p-1}$ be the set of roots of $T^{p-1} - 1$ in $\mathbf{Z}_p$, so $r_{p-1}$ is a subgroup of the unit group $\mathbf{Z}_p^\times$ since for all $n \geq 1$ the set of $n$th roots of unity in any commutative ring is a group under multiplication. Note $r_{p-1}$ lies in the field $\mathbf{Q}_p$ of $p$-adic numbers, which is a field of characteristic 0.

The reduction mod $p$ map on units $\mathrm{red}_p: \mathbf{Z}_p^\times \to (\mathbf{Z}_p/p\mathbf{Z}_p)^\times \cong (\mathbf{Z}/(p))^\times$ is a surjective group homomorphism, and it restricts to a surjective group homomorphism $r_{p-1} \to (\mathbf{Z}/(p))^\times$ by the root lifting in Hensel's lemma. Since $r_{p-1}$ and $(\mathbf{Z}/(p))^\times$ both have order $p - 1$, $\mathrm{red}_p: r_{p-1} \to (\mathbf{Z}/(p))^\times$ is a group isomorphism, so we have lifted the group structure of $(\mathbf{Z}/(p))^\times$ into characteristic 0 as the group $r_{p-1}$.

Now it's time to use the math behind Galois theory. The field $\mathbf{Q}(r_{p-1})$ inside $\mathbf{Q}_p$ is a splitting field of $T^{p-1} - 1$ over $\mathbf{Q}$. There is also a splitting field of $T^{p-1} - 1$ over $\mathbf{Q}$ inside $\mathbf{C}$ since a full set of complex roots of $T^{p-1} - 1$ is the powers $e^{2\pi i k/(p-1)}$ for $0 \leq k \leq p - 2$. Set $\mu_{p-1} = \langle e^{2\pi i/(p-1)} \rangle$, so another splitting field of $T^{p-1} - 1$ over $\mathbf{Q}$ is $\mathbf{Q}(\mu_{p-1}) = \mathbf{Q}(e^{2\pi i/(p-1)})$. By the isomorphism of splitting fields, the field $\mathbf{Q}(r_{p-1})$ in $\mathbf{Q}_p$ and the field $\mathbf{Q}(\mu_{p-1})$ in $\mathbf{C}$ are isomorphic. A field isomorphism $\mathbf{Q}(r_{p-1}) \to \mathbf{Q}(\mu_{p-1})$ restricts to a group isomorphism $\mathbf{Q}(r_{p-1})^\times \to \mathbf{Q}(\mu_{p-1})^\times$, and focusing on the groups of $(p-1)$-th roots of unity we get a group isomorphism $r_{p-1} \to \mu_{p-1}$. Since $\mu_{p-1}$ is cyclic (with generator $e^{2\pi i/(p-1)}$), $r_{p-1}$ is cyclic, and thus $(\mathbf{Z}/(p))^\times = \mathrm{red}_p(r_{p-1})$ is cyclic!

<!-- page 15 -->

## 11. Tenth Proof: Determinants

This proof, unlike previous ones, will not need polynomials (not Theorem 1.1 and not cyclotomic polynomials). It is based on determinants and I learned about it from Fedor Petrov on Mathoverflow[^7]. It uses the following property of finite abelian groups.

**Lemma 11.1.** *Let $G$ be a finite abelian group. If $n$ is the maximal order among the elements in $G$, then the order of every element divides $n$.*

*Proof.* This is a restatement of Lemma 3.1, so you can review the proof of it in Section 3. Sometimes this lemma is derived from the invariant factor decomposition for finite abelian groups, but that makes the lemma appear harder than it really is by comparison with the proof of Lemma 3.1. $\square$

**Theorem 11.2.** *For each prime $p$, the group $(\mathbf{Z}/(p))^\times$ is cyclic.*

*Proof.* Let $n$ be the maximal order of the elements of $(\mathbf{Z}/(p))^\times$, so $n \leq p - 1$. The group $(\mathbf{Z}/(p))^\times$ is cyclic if and only if $n = p - 1$, so we will assume $n < p - 1$ and get a contradiction.

By Lemma 11.1 for the group $G = (\mathbf{Z}/(p))^\times$, $a^n \equiv 1 \bmod p$ for all $a \in (\mathbf{Z}/(p))^\times$. We will use the following $(p-1) \times (p-1)$ matrix:

$$A = \begin{pmatrix} 1 & 1 & 1^2 & \cdots & 1^{p-2} \\ 1 & 2 & 2^2 & \cdots & 2^{p-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & p-2 & (p-2)^2 & \cdots & (p-2)^{p-2} \\ 1 & p-1 & (p-1)^2 & \cdots & (p-1)^{p-2} \end{pmatrix}. \tag{11.1}$$

If $n < p - 1$, so $n \leq p - 2$, the column with exponent $n$ has all entries equal to 1 mod $p$, so that column matches the first column of $A \bmod p$, which implies $\det A \equiv 0 \bmod p$.

Since $A$ is a Vandermonde matrix, the famous formula for determinants of Vandermonde matrices tells us

$$\det A = \prod_{1 \leq i < j \leq p-1} (j - i),$$

and the differences $j - i$ are all nonzero mod $p$, so their product is nonzero mod $p$ because $p$ is prime. Thus $\det A \not\equiv 0 \bmod p$, but we saw above that $\det A \equiv 0 \bmod p$ if $n < p - 1$, and that is a contradiction. Therefore $n = p - 1$. $\square$

A similar approach appears in [3, pp. 111-113] and is attributed to M. E. Alonso.

## Appendix A. Proof of Theorem 1.1

We will prove Theorem 1.1, which we restate here.

**Theorem A.1.** *Let $f(T)$ be a non-constant polynomial with coefficients in $\mathbf{Z}/(p)$, of degree $d$. Then $f(T)$ has at most $d$ roots in $\mathbf{Z}/(p)$.*

In all but the last proof that $(\mathbf{Z}/(p))^\times$ is cyclic, Theorem 1.1 is used for $f(T) = T^d - 1$.

To prove Theorem A.1, we will need a preliminary lemma connecting roots and linear factors. We state the lemma with coefficients in either $\mathbf{C}$ or $\mathbf{Z}/(p)$ because both versions are needed in different proofs that $(\mathbf{Z}/(p))^\times$ is cyclic.

[^7]: See https://mathoverflow.net/questions/54735/collecting-proofs-that-finite-multiplicative-subgroups-of-fields-are-cyclic.

<!-- page 16 -->

**Lemma A.2.** *Let $f(T)$ be a non-constant polynomial with coefficients in $\mathbf{C}$ or in $\mathbf{Z}/(p)$. For $a$ in $\mathbf{C}$ or $\mathbf{Z}/(p)$, $f(a) = 0$ if and only if $T - a$ is a factor of $f(T)$.*

*Proof.* If $T - a$ is a factor of $f(T)$, then $f(T) = (T - a)h(T)$ for some polynomial $h(T)$, and substituting $a$ for $T$ shows $f(a) = 0$.

Conversely, suppose $f(a) = 0$. Write the polynomial as

$$f(T) = c_n T^n + c_{n-1} T^{n-1} + \cdots + c_1 T + c_0, \tag{A.1}$$

where $c_j \in \mathbf{C}$ or $\mathbf{Z}/(p)$. Then

$$0 = c_n a^n + c_{n-1} a^{n-1} + \cdots + c_1 a + c_0. \tag{A.2}$$

Subtracting (A.2) from (A.1), the terms $c_0$ cancel and we get

$$f(T) = c_n(T^n - a^n) + c_{n-1}(T^{n-1} - a^{n-1}) + \cdots + c_1(T - a). \tag{A.3}$$

Since

$$T^j - a^j = (T - a)(T^{j-1} + aT^{j-2} + \cdots + a^i T^{j-1-i} + \cdots + a^{j-2}T + a^{j-1}),$$

each $T^i - a^i$ on the right side of (A.3) has a factor $T - a$. Therefore $f(T) = (T - a)g(T)$, where $g(T)$ is another polynomial with coefficients in $\mathbf{C}$ or $\mathbf{Z}/(p)$. $\square$

Now we prove Theorem A.1.

*Proof.* We induct on the degree $d$ of $f(T)$. Note $d \geq 1$.

A polynomial of degree 1 is $aT + b$ for $a$ and $b$ in $\mathbf{Z}/(p)$ with $a \neq 0$. This has one root in $\mathbf{Z}/(p)$, namely $-b/a$, so it has *at most* one root in $\mathbf{Z}/(p)$.

For $d \geq 1$, assume the theorem holds for all polynomials with coefficients in $\mathbf{Z}/(p)$ of degree $d$. To prove the theorem for all polynomials with coefficients in $\mathbf{Z}/(p)$ of degree $d + 1$, write such a polynomial as

$$f(T) = c_{d+1} T^{d+1} + c_d T^d + \cdots + c_1 T + c_0, \tag{A.4}$$

where $c_j \in \mathbf{Z}/(p)$ and $c_{d+1} \neq 0$.

**Case 1:** $f(T)$ has no roots in $\mathbf{Z}/(p)$. We're done, since $0 \leq d + 1$.

**Case 2:** $f(T)$ has a root in $\mathbf{Z}/(p)$, say $r$. By Lemma A.2, $f(T) = (T - r)g(T)$, where $g(T)$ is a polynomial with coefficients in $\mathbf{Z}/(p)$ of degree $d$ (why degree $d$?). So by the inductive hypothesis, $g(T)$ has at most $d$ roots in $\mathbf{Z}/(p)$. Since $f(a) = (a - r)g(a)$, and a product of numbers in $\mathbf{Z}/(p)$ is 0 only when one of the factors is 0 (this would be *false* if our modulus were composite rather than prime!), we see that each root of $f(T)$ in $\mathbf{Z}/(p)$ is $r$ or is a root of $g(T)$. Thus, $f(T)$ has at most $d + 1$ roots in $\mathbf{Z}/(p)$. As $f(T)$ was arbitrary of degree $d + 1$ with coefficients in $\mathbf{Z}/(p)$, we are done with the inductive step. $\square$

**Remark A.3.** There were two cases considered in the inductive step: when $f(T)$ has a root in $\mathbf{Z}/(p)$ and when it does not. One of those cases must occur, but in an example we don't know which case occurs without searching for roots. This is why this proof of Theorem A.1 is not effective. It gives us an upper bound on the number of roots, but does not give us the tools to decide if there is even one root in $\mathbf{Z}/(p)$ for a particular polynomial (of degree greater than 1).

<!-- page 17 -->

## Appendix B. The primes $p$ where $a$ generates $(\mathbf{Z}/(p))^\times$

Fix a nonzero integer $a$. Does it generate $(\mathbf{Z}/(p))^\times$ for infinitely many $p$? Not necessarily:

- taking $a = -1$, the only $p$ where $-1 \bmod p$ generates $(\mathbf{Z}/(p))^\times$ are $p = 2$ and 3,
- taking $a$ to be a perfect square, say $a = b^2$, $a \bmod p$ can't generate $(\mathbf{Z}/(p))^\times$ when $p > 2$ since $a \bmod p$ has order dividing $(p-1)/2$: $a^{(p-1)/2} = b^{p-1} \equiv 1 \bmod p$.

A conjecture of Artin, going back to 1927, says every each nonzero integer $a$ other than $-1$ and perfect squares generates $(\mathbf{Z}/(p))^\times$ for infinitely many $p$.[^8] The table below lists, for each $a$ where $|a| \leq 12$ and $a$ is not $-1$ or a perfect square, the first 14 primes $p$ such that $a \bmod p$ generates $(\mathbf{Z}/(p))^\times$. More data is at the OEIS link at the end of each row.

| $a$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | OEIS link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 5 | 11 | 13 | 19 | 29 | 37 | 53 | 59 | 61 | 67 | 83 | 101 | 107 | [A001122](https://oeis.org/A001122) |
| $-2$ | 5 | 7 | 13 | 23 | 29 | 37 | 47 | 53 | 61 | 71 | 79 | 101 | 103 | 149 | [A105874](https://oeis.org/A105874) |
| 3 | 2 | 5 | 7 | 17 | 19 | 29 | 31 | 43 | 53 | 79 | 89 | 101 | 113 | 127 | [A019334](https://oeis.org/A019334) |
| $-3$ | 2 | 5 | 11 | 17 | 23 | 29 | 47 | 53 | 59 | 71 | 83 | 89 | 101 | 107 | [A105875](https://oeis.org/A105875) |
| $-4$ | 3 | 7 | 11 | 19 | 23 | 47 | 59 | 67 | 71 | 79 | 83 | 103 | 107 | 131 | [A105876](https://oeis.org/A105876) |
| 5 | 2 | 3 | 7 | 17 | 23 | 37 | 43 | 47 | 53 | 73 | 83 | 97 | 103 | 107 | [A019335](https://oeis.org/A019335) |
| $-5$ | 2 | 11 | 17 | 19 | 37 | 53 | 59 | 73 | 79 | 97 | 113 | 131 | 137 | 139 | [A105877](https://oeis.org/A105877) |
| 6 | 11 | 13 | 17 | 41 | 59 | 61 | 79 | 83 | 89 | 103 | 107 | 109 | 113 | 127 | [A019336](https://oeis.org/A019336) |
| $-6$ | 13 | 17 | 19 | 23 | 41 | 47 | 61 | 67 | 71 | 89 | 109 | 113 | 137 | 157 | [A105878](https://oeis.org/A105878) |
| 7 | 2 | 5 | 11 | 13 | 17 | 23 | 41 | 61 | 67 | 71 | 79 | 89 | 97 | 101 | [A019337](https://oeis.org/A019337) |
| $-7$ | 2 | 3 | 5 | 13 | 17 | 31 | 41 | 47 | 59 | 61 | 83 | 89 | 97 | 101 | [A105879](https://oeis.org/A105879) |
| 8 | 3 | 5 | 11 | 29 | 53 | 59 | 83 | 101 | 107 | 131 | 149 | 173 | 179 | 197 | [A019338](https://oeis.org/A019338) |
| $-8$ | 5 | 23 | 29 | 47 | 53 | 71 | 101 | 149 | 167 | 173 | 191 | 197 | 239 | 263 | [A105880](https://oeis.org/A105880) |
| $-9$ | 2 | 7 | 11 | 19 | 23 | 31 | 43 | 47 | 59 | 71 | 79 | 83 | 107 | 127 | [A105881](https://oeis.org/A105881) |
| 10 | 7 | 17 | 19 | 23 | 29 | 47 | 59 | 61 | 97 | 109 | 113 | 131 | 149 | 167 | [A001913](https://oeis.org/A001913) |
| $-10$ | 3 | 17 | 29 | 31 | 43 | 61 | 67 | 71 | 83 | 97 | 107 | 109 | 113 | 149 | [A007348](https://oeis.org/A007348) |
| 11 | 2 | 3 | 13 | 17 | 23 | 29 | 31 | 41 | 47 | 59 | 67 | 71 | 73 | 101 | [A019339](https://oeis.org/A019339) |
| $-11$ | 2 | 7 | 13 | 17 | 29 | 41 | 73 | 79 | 83 | 101 | 107 | 109 | 127 | 131 | [A105883](https://oeis.org/A105883) |
| 12 | 5 | 7 | 17 | 31 | 41 | 43 | 53 | 67 | 101 | 103 | 113 | 127 | 137 | 139 | [A019340](https://oeis.org/A019340) |
| $-12$ | 5 | 17 | 23 | 41 | 47 | 53 | 59 | 71 | 83 | 101 | 107 | 113 | 131 | 137 | [A105884](https://oeis.org/A105884) |

Now consider, for prime $p$, the *least* $a \in \mathbf{Z}^+$ such that $a \bmod p$ generates $(\mathbf{Z}/(p))^\times$. Call that number $g_p$, so $1 \leq g_p \leq p - 1$, $g_p \bmod p$ has order $p - 1$, and no positive integer less than $g_p$ has that property. The table below lists $g_p$ for the first 20 $p$.

| $p$ | 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 | 43 | 47 | 53 | 59 | 61 | 67 | 71 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $g_p$ | 1 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 5 | 2 | 3 | 2 | 6 | 3 | 5 | 2 | 2 | 2 | 2 | 7 |

The number $g_p$ is never a perfect power except for $g_2$: if $b > 1$ and $b^r$ generates $(\mathbf{Z}/(p))^\times$ where $r \geq 2$, then $b$ generates $(\mathbf{Z}/(p))^\times$ and $b < b^r$.

Probably each $a \geq 1$ that is not a perfect power, besides 1, is $g_p$ for some prime $p$ (and for infinitely many $p$ if $a > 1$). The table below lists, for the first 14 positive integers $a$ that are not perfect powers besides 1, the first $p$ such that $g_p = a$. It is on OEIS at [A023048](https://oeis.org/A023048).

| $a$ | 1 | 2 | 3 | 5 | 6 | 7 | 10 | 11 | 12 | 13 | 14 | 15 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st $p$ s.t. $g_p = a$ | 2 | 3 | 7 | 23 | 41 | 71 | 313 | 643 | 4111 | 457 | 1031 | 439 | 311 | 53173 |

[^8]: Artin conjectured more precisely that the set of such $p$ has positive density among the primes, and he gave a proposed a formula for that density. Any subset of the primes with positive density is infinite.

<!-- page 18 -->

## References

[1] M. Baker, Primitive roots, discrete logarithms, and p-adic numbers, https://mattbaker.blog/2013/11/07/primitive-roots-discrete-logarithms-and-the-interplay-between-p-adic-and-complex-numbers/.

[2] C. Bertault, "Une identité remarquable au service de $(\mathbf{Z}/p\mathbf{Z})^*$," *Revue de Mathématiques Spéciales* **131**, Jan. 2021. URL http://christophebertault.fr/articles/.

[3] E. Bujalance García, J. J. Etayo Gordejuela, and J. M. Gamboa Mutuberría, *Teoría Elemental de Grupos*, Univ. Nac. Educ. Distancia, Madrid, 2002.

[4] M. Bullynck, "Decimal periods and their tables: a German research topic (1765-1801)," URL https://halshs.archives-ouvertes.fr/halshs-00663295/document.

[5] L. Euler, "Demonstrationes circa residua ex divisione potestatum per numeros primos resultantia," *Novi commentarii academiae scientiarum Petropolitanae* **18** (1773), 85–135, 1774, Opera Omnia I, vol. 3, 240–281. URL https://www.biodiversitylibrary.org/item/38569#page/157/mode/1up and https://scholarlycommons.pacific.edu/euler-works/449/.

[6] C. F. Gauss, *Disquisitiones Arithmeticae*, translated by Arthur A. Clarke, Yale Univ. Press, New Haven, 1966.

[7] J. H. Lambert, "Adnotata quaedam de numeris, eorumque anatomia," *Nova Acta Eruditorum* (1769), URL http://www.kuttaka.org/~JHL/L1769e.pdf.

[8] J. Rotman, *Advanced Modern Algebra*, 3rd ed., Part 1, Amer. Math. Soc., Providence, 2015.

[9] V. Shoup, *A Computational Introduction to Number Theory and Algebra*, 2nd edition, Cambridge Univ. Press, 2008. URL https://shoup.net/ntb/.
