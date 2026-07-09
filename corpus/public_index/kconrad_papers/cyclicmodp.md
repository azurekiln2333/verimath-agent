# Cyclicity of (Z/p)x

> **Source**: https://kconrad.math.uconn.edu/blurbs/cyclicmodp.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
CYCLICITY OF (Z/(p))×
KEITH CONRAD
1. Introduction
For a prime p, the group (Z/(p))× is cyclic. This is very important in number theory and
has had practical uses since a choice of generator of (Z/(p))× is part of the Diﬃe-Hellman
key exchange, which is how public-key cryptography started in 1976 (modern cryptography
uses a variant called the elliptic curve Diﬃe-Hellman key exchange)1.
We will give ten proofs that (Z/(p))× is cyclic. A feature of all known proofs is that they
do not lead to concrete formula for a generator in terms of p. While the proof in Section 7 is
an algorithm leading to a generator, is is not a provably eﬃcient algorithm since it depends
on the prime factorization of p −1.
Cyclicity of (Z/(p))× was ﬁrst conjectured by Lambert [4, Footnote 13], [7, pp. 127–128]
in 1769. Euler [5, §38] gave a proof like that in Section 9 in 1773, with some gaps. Gauss [6,
Art. 52–55] gave the proofs in Sections 2 and 7 in 1801, and cyclicity of (Z/(p))× is often
attributed to him.
Unlike prime moduli, for most (but not all) composite m the group (Z/(m))× is not
cyclic. For example, (Z/(12))× has size 4 but its elements have order 1 or 2.
The following result is used in all but the last three proofs that (Z/(p))× is cyclic, so we
state it now and will prove it in Appendix A.
Theorem 1.1. Let f(T) be a non-constant polynomial with coeﬃcients in Z/(p), of degree
d. Then f(T) has at most d roots in Z/(p).
What we need from Theorem 1.1 is the special case f(T) = T d −1: the congruence
td −1 ≡0 mod p has at most d solutions in Z/(p), or equivalently, there are at most d
solutions to the equation td −1 = 0 in Z/(p). The upper bound d can break down in Z/(m)
for non-prime m, e.g., the polynomial T 2 −1 has four solutions in Z/(8).
Appendix B discusses when a nonzero integer generates (Z/(p))× as p varies.
2. First Proof: Counting Elements of all Orders
For our ﬁrst proof that (Z/(p))× is cyclic, we are going to count the elements with various
orders. In (Z/(p))×, which has size p −1, the order of each element divides p −1. For each
positive divisor of p −1, say d, let Np(d) be the number of elements of order d in (Z/(p))×.
For instance, Np(1) = 1 and the cyclicity of (Z/(p))×, which we want to prove, is equivalent
to Np(p −1) > 0. Every element has some order, and the order of each element divides
p −1, so counting the elements of (Z/(p))× by their order yields
(2.1)
X
d|(p−1)
Np(d) = p −1.
1Generators for the nonzero elements of a ﬁnite ﬁeld not of the form Z/(p) have applications. For example,
QR codes use a generator of the nonzero elements of a ﬁeld with order 256.
1

<!-- page 2 -->
2
KEITH CONRAD
Theorem 2.1. Let d ∈Z+. If Np(d) > 0, then Np(d) = ϕ(d).
Proof. When Np(d) > 0, there is an element of order d in (Z/(p))×, say a.
Then the
diﬀerent solutions to xd = 1 are 1, a, a2, . . . , ad−1. There are at most d solutions of xd = 1
in Z/(p), by Theorem 1.1, and there are d diﬀerent powers of a, so the powers of a provide
all the solutions to xd = 1 in Z/(p). Each element of order d is a solution to xd = 1, and
therefore the elements of order d in (Z/(p))× are exactly the powers ak that have order d.
Since ak has order d/(k, d), which is d exactly when (k, d) = 1, Np(d) is the number of k
from 1 to d that are relatively prime to d. That number is ϕ(d).
□
Now we can say, for all d ∈Z+, that
(2.2)
Np(d) ≤ϕ(d).
Indeed, Theorem 2.1 tells us that Np(d) = 0 or Np(d) = ϕ(d). We now feed (2.2) into (2.1):
(2.3)
p −1 =
X
d|(p−1)
Np(d) ≤
X
d|(p−1)
ϕ(d).
We have obtained an inequality for each prime p:
(2.4)
p −1 ≤
X
d|(p−1)
ϕ(d).
If there is some d dividing p −1 for which the inequality in (2.2) is strict (that is, Np(d) <
ϕ(d)), then the inequality in (2.3) would be strict, and thus the inequality in (2.4) would
be strict. How sharp is (2.4)? Let’s look at some examples.
Example 2.2. If p = 5, then P
d|4 ϕ(d) = ϕ(1) + ϕ(2) + ϕ(4) = 1 + 1 + 2 = 4.
Example 2.3. If p = 11, then P
d|10 ϕ(d) = ϕ(1)+ϕ(2)+ϕ(5)+ϕ(10) = 1+1+4+4 = 10.
Example 2.4. If p = 29, then P
d|28 ϕ(d) = ϕ(1) + ϕ(2) + ϕ(4) + ϕ(7) + ϕ(14) + ϕ(28) =
1 + 1 + 2 + 6 + 6 + 12 = 28.
It appears that (2.4) might be an equality! This inspires us to prove it, and the appearance
of p −1 in (2.4) is not essential.
Theorem 2.5. For every positive integer n, P
d|n ϕ(d) = n. In particular, for each prime
number p we have P
d|(p−1) ϕ(d) = p −1.
Proof. We will count the n fractions
(2.5)
1
n, 2
n, . . . , n −1
n
, n
n
according to their denominators when the fractions are put in reduced form.
For such a fraction m/n with denominator n, its reduced form denominator is a divisor
of n.
How many of these reduced form fractions have a given denominator?
Writing
m/n = a/d, where (a, d) = 1, the condition 1 ≤m ≤n is equivalent to 1 ≤a ≤d.
Therefore the number of fractions in (2.5) with reduced form denominator d is the number
of a from 1 to d with (a, d) = 1. There are ϕ(d) such numbers. Thus, counting the fractions
in (2.5) according to their reduced form denominators, we get
n =
X
d|n
ϕ(d).
□

<!-- page 3 -->
CYCLICITY OF (Z/(p))×
3
Theorem 2.5 tells us (2.4) is an equality, so the inequalities in (2.2) must all be equalities.
(Reread the discussion right after (2.4) if you don’t see this.) Therefore Np(d) = ϕ(d) for
each d dividing p −1. In particular, Np(p −1) > 0, so there is an element of (Z/(p))× with
order p −1. We’ve (non-constructively) proved the existence of a generator of (Z/(p))×.
Let’s summarize the argument again.
Theorem 2.6. For each prime p, the group (Z/(p))× is cyclic.
Proof. For d ∈Z+, let Np(d) be the number of elements of order d in (Z/(p))×. By Theorem
2.1, Np(d) ≤ϕ(d). Therefore
p −1 =
X
d|(p−1)
Np(d) ≤
X
d|(p−1)
ϕ(d).
By Theorem 2.5, the sum on the right is p−1, so the ≤is an equality. Thus the inequalities
Np(d) ≤ϕ(d) for all d dividing p−1 have to be equalities. In particular, Np(p−1) = ϕ(p−1),
which is positive, so there is an element of (Z/(p))× with order p −1.
□
3. Second Proof: One Subgroup per Size
We begin our next proof by establishing a divisibility property among orders of elements
that is peculiar to ﬁnite abelian groups. In a ﬁnite group, all elements have order dividing
the size of the group.
In the abelian setting all orders also divide something else: the
maximal order.
Lemma 3.1. Let G be a ﬁnite abelian group. If n is the maximal order among the elements
in G, then the order of every element divides n.
For example, in (Z/(56))×, which has size 24, the orders of elements turn out to be 1,
2, 3, and 6. All orders divide the maximal order 6. In S4, also of size 24, the orders of
elements are 1, 2, 3, and 4. Note 3 does not divide the maximal order 4. Lemma 3.1 does
not apply to S4, as S4 is non-abelian.
The reader might want to jump ahead to Theorem 3.3 to see how Lemma 3.1 gets used,
before diving into the proof of Lemma 3.1.
Proof. Let g have the maximal order n. Pick h ∈G, and let h ∈G have order m. We want
to show m | n. We will assume m does not divide n (this forces m > 1) and use this non-
divisibility to construct an element with order exceeding n. That would be a contradiction,
so m | n.
For instance, if (m, n) = 1, then gh has order mn > n. But that is too easy: we can’t
expect m to have no factors in common with n. How can we use g and h to ﬁnd an element
with order larger than n just from knowing m (the order of h) does not divide n (the order
of g)? The following example will illustrate the idea before we carry it out in general.
Example 3.2. Suppose n = 96 and m = 18. (That is, g has order 96 and h has order 18.)
Look at the prime factorizations of these numbers:
96 = 25 · 3,
18 = 2 · 32.
Here m does not divide n because there are more 3’s in m than in n. The least common
multiple of m and n is 25 · 32, which is larger than n. We can get an element of that order
by reduction to the relatively prime order case: kill the 3 in 96 by working with g3 and kill
the 2 in 18 by working with h2. That is, g3 has order 96/3 = 25 and h2 has order 18/2 = 9.

<!-- page 4 -->
4
KEITH CONRAD
These orders are relatively prime, and the group is abelian, so the product g3h2 has order
25 · 9 > 96. Thus, 96 is not the maximal order in the group.
Now we return to the general case. If m does not divide n, then there is some prime
p whose multiplicity (exponent) as a factor of m exceeds that of n. Let pe be the highest
power of p in m and pf be the highest power of p in n, so e > f. (Quite possibly f = 0,
although in Example 3.2 both e and f were positive.)
Now consider gpf and hm/pe. The ﬁrst has order n/pf, which is not divisible by p, and
the second has order pe, which is a pure p-power. These orders are relatively prime. In an
abelian group, if g1 has order n1 and g2 has order n2 with (n1, n2) = 1, then g1g2 has order
n1n22 so gpf hm/pe has order
n
pf pe = npe−f > n.
This contradicts the maximality of n as an order in G, so we have a contradiction.
□
The following theorem will be our criterion for showing a group is cyclic. Recall that in
a cyclic group there is just one subgroup of each size that occurs. Assuming the group is
abelian, the converse holds.
Theorem 3.3. Let G be a ﬁnite abelian group with at most one subgroup per size. Then G
is cyclic.
Proof. Let n be the maximal order among the elements of G, and let g ∈G be an element
with order n. We will show every element of G is a power of g, so G = ⟨g⟩.
Pick h ∈G, and say h has order d. Since d | n by Lemma 3.1, we can write down
another element of order d: gn/d. Thus we have two subgroups of size d: ⟨h⟩and ⟨gn/d⟩.
By hypothesis, these subgroups are the same: ⟨h⟩= ⟨gn/d⟩. In particular, h ∈⟨gn/d⟩⊂⟨g⟩,
so h is a power of g. Since h was arbitrary in G, G = ⟨g⟩.
□
Remark 3.4. Is the abelian hypothesis in Theorem 3.3 necessary?
That is, is there a
non-abelian group with at most one subgroup of each size? No. A ﬁnite group with at most
one subgroup of each size must be cyclic, even if we don’t assume at ﬁrst that the group is
abelian. However, to prove this without an abelian hypothesis is quite a bit more involved
than the proof of Theorem 3.3. (Where did we use the abelian hypothesis in the proof of
Theorem 3.3?)
Now we are ready to show (Z/(p))× is cyclic.
Theorem 3.5. For each prime p, the group (Z/(p))× is cyclic.
Proof. We will show (Z/(p))× satisﬁes the hypothesis of Theorem 3.3: it has at most one
subgroup per size. Let H ⊂(Z/(p))× be a subgroup, with size (say) d. Then every a ∈H
satisﬁes ad = 1 in Z/(p), so H is a subset of the solutions to xd = 1. By Theorem 1.1, there
are at most d solutions to xd = 1 in Z/(p). Since d is the size of H (by deﬁnition), we ﬁlled
up the solutions of xd = 1 in Z/(p) using H:
H = {x ∈Z/(p) : xd = 1}.
The right side is determined by d (and p), so there is at most one subgroup of (Z/(p))×
with size d, for each d. Thus Theorem 3.3 applies, which shows (Z/(p))× is cyclic.
□
2If we drop the condition (n1, n2) = 1 then we can always say g1g2 has order dividing [n1, n2] since
(g1g2)[n1,n2] = g[n1,n2]
1
g[n1,n2]
2
= 1, but [n1, n2] is not a formula for the order of g1g2 in general. For example,
if g has order n > 1 then g−1 has order n and gg−1 = 1 has order 1 while [n, n] = n > 1.

<!-- page 5 -->
CYCLICITY OF (Z/(p))×
5
4. Third Proof: Bounding with the Maximal Order
Our next proof that (Z/(p))× is cyclic will apply Lemma 3.1 from Section 3, but in a
diﬀerent way. That lemma says that in a ﬁnite abelian group, the order of each element
divides the maximal order of the elements in the group. Review Lemma 3.1 after seeing
how it gets used here.
Theorem 4.1. For each prime p, the group (Z/(p))× is cyclic.
Proof. Let n be the maximal order among the elements in (Z/(p))×. We want to show
n = p −1, so there is an element of order p −1. Obviously n ≤p −1. (More precisely,
n | (p −1), but the crude inequality will suﬃce.)
Every element has order dividing n, by Lemma 3.1, so each a ∈(Z/(p))× satisﬁes an = 1.
Theorem 1.1 says the equation xn = 1 has at most n solutions in Z/(p).
We already
produced p −1 diﬀerent solutions (namely all of (Z/(p))×), so p −1 ≤n.
Comparing the two inequalities, n = p −1. Thus there is an element of (Z/(p))× with
order p −1, so (Z/(p))× is cyclic.
□
5. Fourth proof: Induction and Homomorphisms, I
For this proof we will show something superﬁcially stronger: every subgroup of (Z/(p))×
is cyclic. This is superﬁcially stronger because of the general theorem in group theory that
every subgroup of a cyclic group is cyclic: it means that once (Z/(p))× is proved cyclic by
some method, it follows that its subgroups are all cyclic. We are going to prove directly
that all subgroups of (Z/(p))× are cyclic, rather than only that (Z/(p))× is cyclic, so that
we can argue by induction on the order of the subgroup. I learned the argument below from
David Feldman and Paul Monsky on Mathoverﬂow3.
Theorem 5.1. For each prime p, every subgroup of (Z/(p))× is cyclic.
Proof. We argue by induction on the order of the subgroup of (Z/(p))×.
The only subgroup of order 1 is the trivial subgroup, which is obviously cyclic.
Let H be a subgroup of (Z/(p))× with order n > 1 and assume all subgroups of (Z/(p))×
with order less than n are cyclic. To prove H is cyclic, we consider two cases.
Case 1: The order of H is a prime power. Let |H| = qk, where q is prime. If H is not
cyclic, each element of H has order dividing qk and not equal to qk, so the order divides qk−1
(since q is prime). Then all x ∈H satisfy xqk−1 = 1. That means the equation xqk−1 = 1 has
at least qk solutions in Z/(p) (namely all the elements of H), but the polynomial T qk−1 −1
has degree qk−1, so the equation xqk−1 = 1 has at most qk−1 solutions in Z/(p) by Theorem
1.1. This is a contradiction, so H must have an element of order qk, so H is cyclic.
Case 2: The order of H is not a prime power. This means n = |H| has at least two
diﬀerent prime factors, so we can write n as ab where a > 1, b > 1, and (a, b) = 1. (For
example, let a be the highest power of one prime dividing n and b = n/a.) Let f : H →H
by f(x) = xa. This is a homomorphism since the group H is abelian. For x ∈H we have
xab = xn = 1, so f(x)b = 1. Thus we can say about the kernel and image of f that
ker f = {x ∈H : xa = 1},
im f ⊂{y ∈H : yb = 1},
3See https://mathoverflow.net/questions/54735/collecting-proofs-that-finite-multiplicative-
subgroups-of-fields-are-cyclic.

<!-- page 6 -->
6
KEITH CONRAD
so | ker f| ≤a < n and | im f| ≤b < n by Theorem 1.1. By induction, the subgroups ker f
and im f are cyclic. That means ker f = ⟨h⟩and im f = ⟨h′⟩for some h and h′ in H.
By the ﬁrst isomorphism theorem for groups we have H/ ker f ∼= im f, so
|H| = | ker f|| im f| ≤ab = n = |H|.
Therefore the inequalities | ker f| ≤a and | im f| ≤b have to be equalities, so h has order a
and h′ has order b. Since (a, b) = 1 and h and h′ commute, by group theory hh′ has order
ab, which is |H|. Thus hh′, which lies in H, is a generator of H, so H is cyclic.
By this inductive argument all subgroups of (Z/(p))× are cyclic, so (Z/(p))× is cyclic.
□
6. Fifth proof: Induction and Homomorphisms, II
Our next proof, due to David Leep [8, p. 171], uses ideas similar to those in Sections 3
and 5. Theorem 6.1 below is a special case of Theorem 3.3.
Theorem 6.1. Let G be a ﬁnite abelian group with at most one subgroup of order q for
each prime q dividing |G|. Then G is cyclic.
Proof. We prove this by induction on |G|.
It is clear when |G| = 1. For n ≥2, assume |G| = n and the theorem is proved for all
ﬁnite abelian groups of smaller order. The hypothesis on G is true for its subgroups, so all
proper subgroups of G are cyclic.
There are elements of G with prime order: pick a nontrivial element and let m be its
order, so m > 1. For a prime q dividing m, the (m/q)-th power of something with order m
has order q.
Let x ∈G have a prime order q. Since G is abelian, the function f : G →G where
f(g) = gq is a homomorphism and x is in its kernel. By the hypothesis on G, ⟨x⟩is the only
subgroup of G with order q. Since a nontrivial element of ker f has order q, ker f = ⟨x⟩.
We have G/ ker f ∼= im f, so | im f| = n/q < n. Since im f is a proper subgroup of G, im f
is cyclic, say im f = ⟨y⟩. Then G contains elements x of order q and y of order n/q. From
x and y we get an element of G with order n (and thus a generator of G) by taking cases:
Case 1: q ∤n/q. Since q is prime, (q, n/q) = 1, so xy has order n because x and y
commute.
Case 2: q | n/q. Write y = zq (here we use y ∈im f). Then zn = (zq)n/q = yn/q = 1
since y has order n/q. We’ll show z has order n.
Let m be the order of z. If q ∤m, then (q, m) = 1, so zq also has order m. But zq = y
has order n/q, which is divisible by q, so we have a contradiction. Thus q | m, so zq has
order m/q. Also zq = y has order n/q, so m/q = n/q, which implies m = n.
□
Remark 6.2. If we remove the abelian assumption in Theorem 6.1 then there are coun-
terexamples: Q8 (and more broadly a generalized quaternion group Q2n for n ≥3) has only
one subgroup of order 2 and it is not cyclic.4
Theorem 6.3. For each prime p, the group (Z/(p))× is cyclic.
Proof. Let q be a prime dividing p −1. If there is a subgroup of (Z/(p))× with order q,
say H, then the elements of H are roots of T q −1. This polynomial has at most q roots in
Z/(p), and |H| = q, so H is the full set of roots. Thus H is the only subgroup of order q,
so (Z/(p))× is cyclic by Theorem 6.1.
□
4In the ﬁrst edition (p. 94) of [8], the statement of our Theorem 6.1 omits the condition that G is abelian.

<!-- page 7 -->
CYCLICITY OF (Z/(p))×
7
7. Sixth Proof: Elements of Prime-Power Order
For the next proof that (Z/(p))× is cyclic we are going to use the prime factorization of
p −1. Say
p −1 = qe1
1 qe2
2 · · · qem
m ,
where the qi are distinct primes and ei ≥1. (The case p = 2 is trivial, so we can suppose
p > 2 and thus p−1 > 1.) We will show there are elements of order qei
i for each i, and their
product furnishes a generator of (Z/(p))×.
As a warm-up, using Theorem 1.1 we will show for each prime q dividing p−1 that there
is an element of order q in (Z/(p))× .
Lemma 7.1. If q is a prime dividing p −1 then there is an element of (Z/(p))× with order
q. Speciﬁcally, there is an a ∈(Z/(p))× such that a(p−1)/q ̸= 1, and necessarily a(p−1)/q has
order q in (Z/(p))×.
Proof. The equation a(p−1)/q = 1 in Z/(p) has at most (p −1)/q solutions in Z/(p) by
Theorem 1.1, and (p −1)/q is less than p −1 = |(Z/(p))×|, so (Z/(p))× has an element a
such that a(p−1)/q ̸= 1.
Set b = a(p−1)/q in Z/(p). Then b ̸= 1 and bq = (a(p−1)/q)q = ap−1 = 1 by Fermat’s little
theorem, so the order of b divides q and is not 1. Since q is prime, the only choice for the
order of b is q.
□
This proof is not saying that if a(p−1)/q ̸= 1 in (Z/(p))× then a has order q in (Z/(p))×,
but rather than a(p−1)/q has order q. Let’s look at an example.
Example 7.2. Take p = 19. By Fermat’s little theorem, all a in (Z/(19))× satisfy a18 = 1.
Since 18 is divisible by 3, the lemma is telling us that if a18/3 ̸= 1 in (Z/(19))× then a18/3 has
order 3. From the second row of the table below, which samples over the nonzero numbers
mod 19, we ﬁnd just two diﬀerent values of a6 mod 19 other than 1: 7 and 11. They both
have order 3. Many a in (Z/(19))× have order greater than 3, e.g., 2 mod 19 has order 18.
a mod 19
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
a6 mod 19
1
7
7
11
7
11
1
1
11
11
1
1
11
7
11
7
7
1
If the prime q divides p −1 more than once, the same reasoning as in Lemma 7.1 will
lead to elements of higher q-power order in (Z/(p))×.
Lemma 7.3. If q is a prime and qe | (p−1) for a positive integer e, then there is an element
of (Z/(p))× with order qe. Speciﬁcally, there is an a ∈(Z/(p))× such that a(p−1)/q ̸= 1 in
(Z/(p))×, and necessarily a(p−1)/qe has order qe in (Z/(p))×.
Proof. As in the proof of Lemma 7.1, there are fewer than p −1 solutions to a(p−1)/q = 1
in Z/(p) by Theorem 1.1, so there is an a in (Z/(p))× where a(p−1)/q ̸= 1 in Z/(p).
Set b = a(p−1)/qe, where (p −1)/qe is an integer (we do not use fractional exponents).
Then bqe = (a(p−1)/qe)qe = ap−1 = 1 in (Z/(p))× by Fermat’s little theorem, so the order of
b divides qe. Since q is prime, the (positive) factors of qe other than qe are factors of qe−1.
Since bqe−1 = (a(p−1)/qe)qe−1 = a(p−1)/q ̸= 1 in (Z/(p))×, by the choice of a, the order of b
does not divide qe−1. Thus the order of b in (Z/(p))× has to be qe.
□
Example 7.4. Returning to p = 19, the number p −1 = 18 is divisible by the prime power
9. In the table below we list the a for which a(p−1)/3 = a6 ̸= 1 and below that list the
corresponding values of a18/9 = a2: these are 4, 5, 6, 9, 16, and 17, and all have order 9.

<!-- page 8 -->
8
KEITH CONRAD
a mod 19
2
3
4
5
6
9
10
13
14
15
16
17
a6 mod 19
7
7
11
7
11
11
11
11
7
11
7
7
a2 mod 19
4
9
16
6
17
5
5
17
6
16
9
4
Remark 7.5. Lemma 7.3 can be proved in another way using unique factorization of
polynomials with coeﬃcients in Z/(p). Because all nonzero numbers mod p are roots of
T p−1 −1, this polynomial factors mod p as (T −1)(T −2) · · · (T −(p −1)). Being a product
of distinct linear factors, every factor of T p−1 −1 is also a product of distinct linear factors,
so in particular, every factor of T p−1 −1 has as many roots in Z/(p) as its degree. For a
prime power qe dividing p −1, T qe −1 divides T p−1 −1, so there are qe solutions of aqe = 1
in Z/(p). This exceeds the number of solutions of aqe−1 = 1 in Z/(p), which is at most qe−1
since a nonzero polynomial over a ﬁeld has no more roots than its degree. Therefore there
is an a in Z/(p) ﬁtting aqe = 1 and aqe−1 ̸= 1. All such a have order qe.
Theorem 7.6. For each prime p, the group (Z/(p))× is cyclic.
Proof. We may take p > 2, so p −1 > 1. Write p −1 as a product of primes:
p −1 = qe1
1 qe2
2 · · · qem
m .
By Lemma 7.3, for each i from 1 to m there is some bi in (Z/(p))× with order qei
i . These
orders are relatively prime, and (Z/(p))× is abelian, so the product of the bi’s has order
equal to the product of the qei
i ’s, which is p −1. Thus b1b2 · · · bm generates (Z/(p))×.
□
Remark 7.7. The way we used Theorem 1.1 is that it tells us when p > 2 and 1 ≤d < p−1,
there is a nonzero a mod p such that ad ̸≡1 mod p. Christophe Bertault [2] pointed out
that the existence of such a can be proved without properties of polynomials, by using a
combinatorial argument. When m and n are positive integers, the number of surjective
maps from an m-element set to an n-element set is Pn
k=1(−1)n−k n
k

km, so when m < n we
have Pn
k=1(−1)n−k n
k

km = 0. Therefore when p is an odd prime and d is a proper factor of
p −1, Pp−1
k=1(−1)p−1−k p−1
k

kd = 0. This implies kd ̸≡1 mod p for some k ∈{1, . . . , p −1},
since otherwise Pp−1
k=1(−1)p−1−k p−1
k

kd ≡Pp−1
k=1(−1)k p−1
k

≡(1 −1)p−1 −1 ≡−1 mod p,
which contradicts the sum being 0.
Based on the proof of Theorem 7.6, here is a procedure to ﬁnd a generator of (Z/(p))×:
(1) Get the prime factorization of p −1, say p −1 = qe1
1 qe2
2 · · · qem
m .
(2) For each qi, ﬁnd an ai such that a(p−1)/qi
i
̸≡1 mod p.
(3) By Lemma 7.3, bi := a
(p−1)/qei
i
i
mod p has order qei
i
in (Z/(p))×.
(4) The product b1b2 · · · bm is a generator of (Z/(p))×.
Here’s an example.
Example 7.8. Take p = 3943, so p −1 = 3942 = 2 · 33 · 73. We seek b1 of order 2, b2 of
order 27, and b3 of order 73. The product b1b2b3 mod p will have order p −1.
• The ﬁrst time a(p−1)/2 ̸≡1 mod p is at a = 3: 3(p−1)/2 ≡3942 ≡−1 mod p. This
has order 2.
• The ﬁrst time a(p−1)/3 ̸≡1 mod p is at a = 3: 3(p−1)/3 ≡1135 mod p.
Then
3(p−1)/27 ≡2387 mod p has order 27.
• The ﬁrst time a(p−1)/73 ̸≡1 mod p is at a = 2: 2(p−1)/73 ≡1406 mod p, which has
order 73.

<!-- page 9 -->
CYCLICITY OF (Z/(p))×
9
From these calculations, a generator of (Z/(p))× is (−1)(2387)(1406) ≡3314 mod p.
If we had instead tried a = 2, 3, . . . mod p by brute force to ﬁnd a generator mod p
directly, then we’d have found 3 mod p is a generator. (The order of 2 mod p is 219.)
The bottleneck in this procedure is Step 1 (factoring p −1) if p is large. The other steps
run quickly in practice. In order to ﬁnd a large prime p such that p −1 has a known prime
factorization, we usually ﬁnd p −1 ﬁrst: pick a large number n whose prime factorization is
known and then test if n + 1 is prime by a deterministic or probabilistic primality test. If
n+1 is prime, then set p = n+1. No matter what method is used to ﬁnd a generator, Shoup
[9, p. 340] pointed out that “there is no known way to eﬃciently recognize a [generator]
modulo p without knowing the prime factorization of p −1.”
8. Seventh proof: Subgroups of Prime-Power Order
This proof will, like the previous proof, focus on prime power factors of p −1.
Our new tool is the following theorem about ﬁnite abelian groups whose order is a prime
power.
Theorem 8.1. Let A be a ﬁnite abelian group of order qs, where q is a prime. If A is not
cyclic, then there are more than q solutions in A to the equation xq = 1.
Proof. All elements of A have q-power order. Since A is not cyclic, s ≥2. Let the maximal
order of an element of A be qt, so t < s. Pick g ∈A with this order:
|⟨g⟩| = qt.
The element gqt−1 has order q, and its powers provide q solutions to the equation xq = 1.
We now aim to ﬁnd an element of A with order q that is outside of the subgroup ⟨g⟩. This
will provide another solution to xq = 1, and thus prove the theorem.
For h ∈A with h ̸∈⟨g⟩, there is some q-power hqk that lies in ⟨g⟩. After all, h has q-power
order, so at the very least some q-power of h is the identity (which is in ⟨g⟩). Necessarily
k ≥1. It may happen that the ﬁrst q-power of h that lands in ⟨g⟩is not the identity. After
all, a q-power of h could land inside ⟨g⟩before we run through every possible power of h
(hitting the identity at the last exponent).
Let ℓbe the smallest integer ≥1 such that some element in A outside of ⟨g⟩has its qℓ-th
power inside ⟨g⟩. We claim ℓ= 1. That is, some element outside ⟨g⟩has its q-th power
inside ⟨g⟩. Indeed, suppose ℓ> 1 and let h0 be an element outside of ⟨g⟩with hqℓ
0 ∈⟨g⟩.
Then hqℓ−1
0
̸∈⟨g⟩by minimality of ℓ, yet this element itself satisﬁes (hqℓ−1
0
)q ∈⟨g⟩, so there
is an element whose ‘ℓ’ is 1. Thus ℓ= 1.
Take h1 to be such an element outside ⟨g⟩with hq
1 ∈⟨g⟩, say hq
1 = gn. Since h1 has (like
all elements of A) order dividing qt, the order of hq
1 is at most qt−1. Then gn has order at
most qt−1, so q must divide n. (Otherwise n is relatively prime to the order of g, which
would imply gn = hq
1 has order qt, and that is not correct.) Setting n = qr, we have
hq
1 = gqr.
Then (h1g−r)q = 1 and h1g−r ̸∈⟨g⟩(after all, h1 ̸∈⟨g⟩), so h1g−r is an element of order q
in A that lies outside of ⟨g⟩.
□
Remark 8.2. In Remark 3.4, it was noted that Theorem 3.3 is true (but harder to prove)
without an abelian hypothesis. What about Theorem 8.1? Is its conclusion correct if we
don’t make an initial abelian hypothesis? Yes if q is an odd prime, but no if q = 2. For

<!-- page 10 -->
10
KEITH CONRAD
instance, Q8 is not cyclic but it has only two solutions to x2 = 1. This is not a quirk about
Q8: there are inﬁnitely many non-abelian groups of 2-power order having only two solutions
to x2 = 1, such as the generalized quaternion groups Q2n for n ≥3.5
Theorem 8.3. For each prime p, the group (Z/(p))× is cyclic.
Proof. We may take p > 2, so p −1 > 1. Write p −1 = qe1
1 qe2
2 · · · qem
m , where the qi’s are
diﬀerent primes (and each ei is positive). Set
Ai = {a ∈(Z/(p))× : aqei
i = 1}.
This is a subgroup of (Z/(p))×, and all of its elements have qi-power order, so |Ai| is a
power of qi by Cauchy’s theorem.
If Ai is not cyclic, then Theorem 8.1 says Ai has more than qi solutions to the equation
xqi = 1. However, we know this equation has no more than qi solutions in Z/(p) by Theorem
1.1. Thus we have reached a contradiction, so Ai is cyclic. (We do not yet know the order
of Ai, except that it is a qi-power. We may expect, though, that |Ai| = qei
i .)
Write Ai = ⟨ai⟩. We are going to show a1, a2, . . . , am together generate (Z/(p))×. Then
we will show the single product a1a2 · · · am is a generator of the group.
Dividing p −1 by each of qe1
1 , . . . , qem
m , we get the integers
p −1
qe1
1
, p −1
qe2
2
, . . . , p −1
qem
m
.
These have no collective common prime factor, so some Z-combination of them is equal to
1 (iterated Bezout?):
m
X
i=1
ci
p −1
qei
i
= 1,
where ci ∈Z. Then each a ∈(Z/(p))× can be written as
a = a1 = a
P
i ci(p−1)/qei
i =
m
Y
i=1
aci(p−1)/qei
i .
Since the i-th factor has order dividing qei
i
(raise it to the qei
i -th power as a check), it lies
in Ai and thus the i-th factor is a power of ai. Therefore a is a product of powers of the
ai’s, which means
(Z/(p))× = ⟨a1, a2, . . . , am⟩.
To end the proof, we show that each product of powers an1
1 an2
2 · · · anm
m
is equal to a single
power (a1a2 · · · am)n. Considering that each ai has order dividing qei
i , we could ﬁnd such
an n by trying to solve the simultaneous congruences
n ≡n1 mod qe1
1 , n ≡n2 mod qe2
2 , . . . , n ≡nm mod qem
m .
(Then ani
i
= an
i .) Can we solve all of these congruences with a common n? Absolutely: the
moduli are pairwise relatively prime, so just use the Chinese Remainder Theorem.
□
Remark 8.4. The arguments in this proof really showed something quite general about
ﬁnite abelian groups. If A is a ﬁnite abelian group and p is a prime, let Ap be the subgroup
of elements with p-power order. Then A is cyclic if and only if Ap is cyclic for every p. (If
p does not divide |A|, then Ap is trivial.)
5See https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf, especially Corollary 4.3.

<!-- page 11 -->
CYCLICITY OF (Z/(p))×
11
9. Eighth Proof: Cyclotomic Polynomials
For this proof we will actually write down a polynomial factor of T p−1 −1 whose roots
in Z/(p) are the generators of (Z/(p))×! It sounds like a constructive proof, but there is a
catch: while we will construct a polynomial and show each of its roots in Z/(p) generates
(Z/(p))×, the proof of the existence of these roots in Z/(p) will give no recipe for ﬁnding
them (and thus no recipe for ﬁnding a generator of (Z/(p))×). So the roots are left to
be found by a brute force search. This one uses unique factorization for polynomials with
coeﬃcients in Z/(p), which we previous met in Remark 7.5.
The new polynomials we will meet are the cyclotomic polynomials. We will deﬁne them
ﬁrst as polynomials with complex coeﬃcients. Then we will prove that their coeﬃcients are
in fact integers, so it makes sense to reduce the coeﬃcients modulo p. Finally we will show
one of the cyclotomic polynomials, when reduced modulo p, decomposes into linear factors
and each of its roots in Z/(p) is a generator of (Z/(p))×.
In the complex numbers, let ρn be the basic n-th root of unity cos(2π/n) + i sin(2π/n) =
e2πi/n. It has order n and the other roots of unity with order n are ρj
n where 1 ≤j ≤n and
(j, n) = 1. Deﬁne the n-th cyclotomic polynomial Φn(T) to be the polynomial having for
its roots the roots of unity in C with order n:
(9.1)
Φn(T) :=
n
Y
j=1
(j,n)=1
(T −ρj
n).
For instance, Φ1(T) = T −1, Φ2(T) = T + 1, and Φ4(T) = (T −i)(T + i) = T 2 + 1.
Since (9.1) is a product of linear polynomials, indexed by integers from 1 to n that are
relatively prime to n, Φn(T) has degree ϕ(n) (hence the notation for the polynomial itself;
Φ is a capital Greek ϕ). While the deﬁnition of Φn(T) involves complex linear factors,
the polynomials themselves, after all the factors are multiplied out, actually have integer
coeﬃcients. Here is a table listing the ﬁrst 12 cyclotomic polynomials.
n
Φn(T)
1
T −1
2
T + 1
3
T 2 + T + 1
4
T 2 + 1
5
T 4 + T 3 + T 2 + T + 1
6
T 2 −T + 1
7
T 6 + T 5 + T 4 + T 3 + T 2 + T + 1
8
T 4 + 1
9
T 6 + T 3 + 1
10
T 4 −T 3 + T 2 −T + 1
11
T 10 + T 9 + T 8 + T 7 + T 6 + T 5 + T 4 + T 3 + T 2 + T + 1
12
T 4 −T 2 + 1
There are evidently a lot of patterns worth exploring here. For instance, Φ8 resembles
Φ4, which resembles Φ2, Φ10 is similar to Φ5, and Φ12 seems related to Φ6, which is close
to Φ3. The constant term of Φn(T), for n > 1, seems to be 1. Maybe the most striking
pattern, which persists for the ﬁrst 100 cyclotomic polynomials, is that the coeﬃcients are
all 0, 1, or −1. We will not determine whether or not this is always true (life needs some

<!-- page 12 -->
12
KEITH CONRAD
tantalizing mysteries), but let’s show at least that all the coeﬃcients are integers. First a
factorization lemma is needed.
Lemma 9.1. For n ≥1, T n −1 = Q
d|n Φd(T).
Proof. If ρ is an nth root of unity then ρ is a root of T n −1, so T −ρ is a factor of T n −1.
(see Lemma A.2). Thus, T n −1 is divisible by each T −ρ as ρ runs over the nth roots of
unity. The factors T −ρ for diﬀerent ρ are pairwise relatively prime to each other since
they’re linear with diﬀerent roots, so (using an analogue of Bezout’s identity6) their product
is a factor of T n −1:
(9.2)
T n −1 =
Y
ρn=1
(T −ρ)h(T)
for some polynomial h(T). Comparing degrees on both sides, we see h(T) has degree 0,
so h(T) is a constant. Now comparing leading coeﬃcients on both sides, we must have
h(T) = 1. Thus
(9.3)
T n −1 =
Y
ρn=1
(T −ρ),
Every n-th root of unity has some order dividing n. For each d dividing n, collect together
the linear factors T −ρ corresponding to roots of unity with order d. The product of these
factors is Φd(T), by the deﬁnition of Φd(T).
Thus, we have transformed (9.3) into the
desired formula.
□
Example 9.2. Taking n = 4,
Y
d|4
Φd(T) = Φ1(T)Φ2(T)Φ4(T) = (T −1)(T + 1)(T 2 + 1) = T 4 −1.
Example 9.3. Taking n = p a prime number, T p −1 = (T −1)Φp(T). Thus, we can
explicitly compute
Φp(T) = T p −1
T −1 = 1 + T + T 2 + · · · + T p−1.
Notice the coeﬃcients here all equal 1.
Theorem 9.4. For every n ≥1, the coeﬃcients of Φn(T) are in Z.
Proof. We will argue by induction on n. Since Φ1(T) = T −1, we can take n > 1 and
assume Φm(T) has integer coeﬃcients for m < n. In Lemma 9.1, we can pull out the term
at d = n:
(9.4)
T n −1 =
Y
d|n
d̸=n
Φd(T) · Φn(T).
Let Bn(T) = Q
d|n,d̸=n Φd(T), so
(9.5)
T n −1 = Bn(T)Φn(T).
By induction, Φd(T) has integer coeﬃcients when d is a proper divisor of n, so Bn(T) has
integer coeﬃcients. Each Φd(T) has leading coeﬃcient 1, so Bn(T) does as well. All we
6See Corollaries 4.2 and 4.3 and the generalizations of them at the end of https://kconrad.math.uconn.
edu/blurbs/ugradnumthy/divgcd.pdf as well as https://kconrad.math.uconn.edu/blurbs/ugradnumthy/
analogypoly.pdf.

<!-- page 13 -->
CYCLICITY OF (Z/(p))×
13
know about Φn(T) is that it has complex coeﬃcients. We want to deduce from (9.5) that
its coeﬃcients are integers.
Let’s cook up a second divisibility relation between T n−1 and Bn(T) in a completely dif-
ferent way: the usual division of (complex) polynomials, leaving a quotient and remainder.
We have
(9.6)
T n −1 = Bn(T)Q(T) + R(T),
where R(T) = 0 or 0 ≤deg R < deg Bn. When we divide one polynomial by another and
both have integer coeﬃcients, the quotient and remainder may not have integer coeﬃcients.
For instance,
T 2 + 1 = (2T + 1)
1
2T −1
4

+ 5
4.
However, if the divisor has leading coeﬃcient 1, then everything stays integral, e.g., T 2+1 =
(T + 1)(T −1) + 2. Brieﬂy, the source of all denominators in the quotient and remainder
comes from the leading coeﬃcient of the divisor, so when it is 1, no denominators are
introduced. Thus, since Bn(T) has integer coeﬃcients and leading coeﬃcient 1, Q(T) and
R(T) have integer coeﬃcients.
We now compare our two relations (9.5) and (9.6). Since division of polynomials (with,
say, complex coeﬃcients) has unique quotient and remainder, we must have Φn(T) = Q(T)
and 0 = R(T). In particular, since Q(T) has integer coeﬃcients, we have proved Φn(T) has
integer coeﬃcients!
□
Lemma 9.5. Working with coeﬃcients in Z/(p), the polynomial T p−1 −1 is a product of
linear factors:
T p−1 −1 = (T −1)(T −2)(T −3) · · · (T −(p −1)).
Proof. For every a ̸≡0 mod p, ap−1 ≡1 mod p, or ap−1 = 1 in Z/(p).
Therefore the
polynomial T p−1 −1, considered over Z/(p), has a as a root. Since a is a root, T −a is a
factor and the same reasoning used to get (9.2) implies
T p−1 −1 = (T −1)(T −2)(T −3) · · · (T −(p −1))h(T)
for a polynomial h(T).
Comparing degrees and then leading coeﬃcients on both sides,
h(T) = 1.
□
Theorem 9.6. For each prime p, the group (Z/(p))× is cyclic.
Proof. Consider the factorization
(9.7)
T p−1 −1 =
Y
d|(p−1)
Φd(T).
All polynomials appearing here have integer coeﬃcients. Collect the Φd(T) with d ̸= p −1
into a single term:
(9.8)
T p−1 −1 = Φp−1(T)H(T),
where H(T) has integer coeﬃcients.
Reducing the coeﬃcients in (9.8) modulo p lets us view (9.8) as a polynomial identity
over Z/(p). By Lemma 9.5, the left side of (9.8) breaks up into distinct linear factors over
Z/(p). Therefore, by unique factorization for polynomials with coeﬃcients in Z/(p), the
two factors on the right side of (9.8) are products of linear polynomials over Z/(p) (as many
linear polynomials as the degree of the factor). Therefore Φp−1(T) has a root in Z/(p); in

<!-- page 14 -->
14
KEITH CONRAD
fact, it has ϕ(p −1) roots in Z/(p). We will show each a ∈Z/(p) that is a root of Φp−1(T).
has order p −1, so it is a generator of (Z/(p))×.
Since 0 is not a root of T p−1 −1, a ∈(Z/(p))×. Let d be the order of a in (Z/(p))×, so
d | p −1. Could we have d < p −1? Assume so. (We will get a contradiction and then we
will be done.) Since d is the order of a, ad −1 = 0 in Z/(p). Now consider the factorization
of T d −1 given by Lemma 9.1:
T d −1 =
Y
k|d
Φk(T).
This identity between polynomials with integer coeﬃcients can be viewed as an identity
between polynomials with coeﬃcients in Z/(p) by reducing all the coeﬃcients modulo p.
Setting T = a in this formula, the left side vanishes (in Z/(p)), so Φk(a) is 0 for some k
dividing d. (In fact, it is Φd(a) that vanishes, but we don’t need to know that.) Once Φk(a)
vanishes, Lemma A.2 tells us T −a is a factor of Φk(T). Thus, in (9.7), T −a is a factor
twice: once in Φp−1(T) (that is how we deﬁned a) and also as a factor in Φk(T) for some k
dividing d. But the factorization of T p−1 −1 in Lemma 9.5 has distinct linear factors. We
have a contradiction to unique factorization, so our assumption that d < p −1 is in error:
d = p −1, so a is a generator of (Z/(p))×.
□
Example 9.7. Taking p = 7, Φp−1(T) = Φ6(T) = T 2 −T + 1. Its roots in Z/(7) are 3
and 5: Φ6(3) = 7 ≡0 mod 7 and Φ6(5) = 21 ≡0 mod 7. The numbers 3 and 5 are the
generators of (Z/(7))×, as you can check directly.
10. Ninth proof: p-adic Lifting
This proof, which is due to Matt Baker [1], uses p-adic numbers and the math of Galois
theory. If you know about p-adic numbers then you’ll ﬁnd it amusing. If you don’t know
p-adic numbers and Galois theory, then ignore this section.
The polynomial T p−1 −1 splits completely over Z/(p) with p −1 diﬀerent roots (every
nonzero integer mod p is a root of it), so by Hensel’s lemma this polynomial also splits
completely in Zp[T], where Zp is the p-adic integers. Let rp−1 be the set of roots of T p−1 −1
in Zp, so rp−1 is a subgroup of the unit group Z×
p since for all n ≥1 the set of nth roots of
unity in any commutative ring is a group under multiplication. Note rp−1 lies in the ﬁeld
Qp of p-adic numbers, which is a ﬁeld of characteristic 0.
The reduction mod p map on units redp : Z×
p →(Zp/pZp)× ∼= (Z/(p))× is a surjec-
tive group homomorphism, and it restricts to a surjective group homomorphism rp−1 →
(Z/(p))× by the root lifting in Hensel’s lemma. Since rp−1 and (Z/(p))× both have order
p −1, redp : rp−1 →(Z/(p))× is a group isomorphism, so we have lifted the group structure
of (Z/(p))× into characteristic 0 as the group rp−1.
Now it’s time to use the math behind Galois theory. The ﬁeld Q(rp−1) inside Qp is a
splitting ﬁeld of T p−1 −1 over Q. There is also a splitting ﬁeld of T p−1 −1 over Q inside C
since a full set of complex roots of T p−1 −1 is the powers e2πik/(p−1) for 0 ≤k ≤p −2. Set
µp−1 = ⟨e2πi/(p−1)⟩, so another splitting ﬁeld of T p−1 −1 over Q is Q(µp−1) = Q(e2πi/(p−1)).
By the isomorphism of splitting ﬁelds, the ﬁeld Q(rp−1) in Qp and the ﬁeld Q(µp−1) in C
are isomorphic. A ﬁeld isomorphism Q(rp−1) →Q(µp−1) restricts to a group isomorphism
Q(rp−1)× →Q(µp−1)×, and focusing on the groups of (p −1)-th roots of unity we get a
group isomorphism rp−1 →µp−1. Since µp−1 is cyclic (with generator e2πi/(p−1)), rp−1 is
cyclic, and thus (Z/(p))× = redp(rp−1) is cyclic!

<!-- page 15 -->
CYCLICITY OF (Z/(p))×
15
11. Tenth Proof: Determinants
This proof, unlike previous ones, will not need polynomials (not Theorem 1.1 and not
cyclotomic polynomials). It is based on determinants and I learned about it from Fedor
Petrov on Mathoverﬂow7. It uses the following property of ﬁnite abelian groups.
Lemma 11.1. Let G be a ﬁnite abelian group. If n is the maximal order among the elements
in G, then the order of every element divides n.
Proof. This is a restatement of Lemma 3.1, so you can review the proof of it in Section 3.
Sometimes this lemma is derived from the invariant factor decomposition for ﬁnite abelian
groups, but that makes the lemma appear harder than it really is by comparison with the
proof of Lemma 3.1.
□
Theorem 11.2. For each prime p, the group (Z/(p))× is cyclic.
Proof. Let n be the maximal order of the elements of (Z/(p))×, so n ≤p −1. The group
(Z/(p))× is cyclic if and only if n = p−1, so we will assume n < p−1 and get a contradiction.
By Lemma 11.1 for the group G = (Z/(p))×, an ≡1 mod p for all a ∈(Z/(p))×. We will
use the following (p −1) × (p −1) matrix:
(11.1)
A =







1
1
12
· · ·
1p−2
1
2
22
· · ·
2p−2
...
...
...
...
...
1
p −2
(p −2)2
· · ·
(p −2)p−2
1
p −1
(p −1)2
· · ·
(p −1)p−2







.
If n < p −1, so n ≤p −2, the column with exponent n has all entries equal to 1 mod p, so
that column matches the ﬁrst column of A mod p, which implies det A ≡0 mod p.
Since A is a Vandermonde matrix, the famous formula for determinants of Vandermonde
matrices tells us
det A =
Y
1≤i<j≤p−1
(j −i),
and the diﬀerences j −i are all nonzero mod p, so their product is nonzero mod p because
p is prime. Thus det A ̸≡0 mod p, but we saw above that det A ≡0 mod p if n < p −1,
and that is a contradiction. Therefore n = p −1.
□
A similar approach appears in [3, pp. 111-113] and is attributed to M. E. Alonso.
Appendix A. Proof of Theorem 1.1
We will prove Theorem 1.1, which we restate here.
Theorem A.1. Let f(T) be a non-constant polynomial with coeﬃcients in Z/(p), of degree
d. Then f(T) has at most d roots in Z/(p).
In all but the last proof that (Z/(p))× is cyclic, Theorem 1.1 is used for f(T) = T d −1.
To prove Theorem A.1, we will need a preliminary lemma connecting roots and linear
factors. We state the lemma with coeﬃcients in either C or Z/(p) because both versions
are needed in diﬀerent proofs that (Z/(p))× is cyclic.
7See https://mathoverflow.net/questions/54735/collecting-proofs-that-finite-multiplicative-
subgroups-of-fields-are-cyclic.

<!-- page 16 -->
16
KEITH CONRAD
Lemma A.2. Let f(T) be a non-constant polynomial with coeﬃcients in C or in Z/(p).
For a in C or Z/(p), f(a) = 0 if and only if T −a is a factor of f(T).
Proof. If T −a is a factor of f(T), then f(T) = (T −a)h(T) for some polynomial h(T), and
substituting a for T shows f(a) = 0.
Conversely, suppose f(a) = 0. Write the polynomial as
(A.1)
f(T) = cnT n + cn−1T n−1 + · · · + c1T + c0,
where cj ∈C or Z/(p). Then
(A.2)
0 = cnan + cn−1an−1 + · · · + c1a + c0.
Subtracting (A.2) from (A.1), the terms c0 cancel and we get
(A.3)
f(T) = cn(T n −an) + cn−1(T n−1 −an−1) + · · · + c1(T −a).
Since
T j −aj = (T −a)(T j−1 + aT j−2 + · · · + aiT j−1−i + · · · + aj−2T + aj−1),
each T i −ai on the right side of (A.3) has a factor T −a. Therefore f(T) = (T −a)g(T),
where g(T) is another polynomial with coeﬃcients in C or Z/(p).
□
Now we prove Theorem A.1.
Proof. We induct on the degree d of f(T). Note d ≥1.
A polynomial of degree 1 is aT + b for a and b in Z/(p) with a ̸= 0. This has one root in
Z/(p), namely −b/a, so it has at most one root in Z/(p).
For d ≥1, assume the theorem holds for all polynomials with coeﬃcients in Z/(p) of
degree d. To prove the theorem for all polynomials with coeﬃcients in Z/(p) of degree
d + 1, write such a polynomial as
(A.4)
f(T) = cd+1T d+1 + cdT d + · · · + c1T + c0,
where cj ∈Z/(p) and cd+1 ̸= 0.
Case 1: f(T) has no roots in Z/(p). We’re done, since 0 ≤d + 1.
Case 2: f(T) has a root in Z/(p), say r. By Lemma A.2, f(T) = (T −r)g(T), where g(T)
is a polynomial with coeﬃcients in Z/(p) of degree d (why degree d?). So by the inductive
hypothesis, g(T) has at most d roots in Z/(p). Since f(a) = (a −r)g(a), and a product of
numbers in Z/(p) is 0 only when one of the factors is 0 (this would be false if our modulus
were composite rather than prime!), we see that each root of f(T) in Z/(p) is r or is a root
of g(T). Thus, f(T) has at most d+1 roots in Z/(p). As f(T) was arbitrary of degree d+1
with coeﬃcients in Z/(p), we are done with the inductive step.
□
Remark A.3. There were two cases considered in the inductive step: when f(T) has a root
in Z/(p) and when it does not. One of those cases must occur, but in an example we don’t
know which case occurs without searching for roots. This is why this proof of Theorem A.1
is not eﬀective. It gives us an upper bound on the number of roots, but does not give us
the tools to decide if there is even one root in Z/(p) for a particular polynomial (of degree
greater than 1).

<!-- page 17 -->
CYCLICITY OF (Z/(p))×
17
Appendix B. The primes p where a generates (Z/(p))×
Fix a nonzero integer a. Does it generate (Z/(p))× for inﬁnitely many p? Not necessarily:
• taking a = −1, the only p where −1 mod p generates (Z/(p))× are p = 2 and 3,
• taking a to be a perfect square, say a = b2, a mod p can’t generate (Z/(p))× when
p > 2 since a mod p has order dividing (p −1)/2: a(p−1)/2 = bp−1 ≡1 mod p.
A conjecture of Artin, going back to 1927, says every each nonzero integer a other than
−1 and perfect squares generates (Z/(p))× for inﬁnitely many p.8 The table below lists, for
each a where |a| ≤12 and a is not −1 or a perfect square, the ﬁrst 14 primes p such that
a mod p generates (Z/(p))×. More data is at the OEIS link at the end of each row.
a
1
2
3
4
5
6
7
8
9
10
11
12
13
14
OEIS link
2
3
5
11
13
19
29
37
53
59
61
67
83
101
107
A001122
−2
5
7
13
23
29
37
47
53
61
71
79
101
103
149
A105874
3
2
5
7
17
19
29
31
43
53
79
89
101
113
127
A019334
−3
2
5
11
17
23
29
47
53
59
71
83
89
101
107
A105875
−4
3
7
11
19
23
47
59
67
71
79
83
103
107
131
A105876
5
2
3
7
17
23
37
43
47
53
73
83
97
103
107
A019335
−5
2
11
17
19
37
53
59
73
79
97
113
131
137
139
A105877
6
11
13
17
41
59
61
79
83
89
103
107
109
113
127
A019336
−6
13
17
19
23
41
47
61
67
71
89
109
113
137
157
A105878
7
2
5
11
13
17
23
41
61
67
71
79
89
97
101
A019337
−7
2
3
5
13
17
31
41
47
59
61
83
89
97
101
A105879
8
3
5
11
29
53
59
83
101
107
131
149
173
179
197
A019338
−8
5
23
29
47
53
71
101
149
167
173
191
197
239
263
A105880
−9
2
7
11
19
23
31
43
47
59
71
79
83
107
127
A105881
10
7
17
19
23
29
47
59
61
97
109
113
131
149
167
A001913
−10
3
17
29
31
43
61
67
71
83
97
107
109
113
149
A007348
11
2
3
13
17
23
29
31
41
47
59
67
71
73
101
A019339
−11
2
7
13
17
29
41
73
79
83
101
107
109
127
131
A105883
12
5
7
17
31
41
43
53
67
101
103
113
127
137
139
A019340
−12
5
17
23
41
47
53
59
71
83
101
107
113
131
137
A105884
Now consider, for prime p, the least a ∈Z+ such that a mod p generates (Z/(p))×. Call
that number gp, so 1 ≤gp ≤p −1, gp mod p has order p −1, and no positive integer less
than gp has that property. The table below lists gp for the ﬁrst 20 p.
p
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
gp
1
2
2
3
2
2
3
2
5
2
3
2
6
3
5
2
2
2
2
7
The number gp is never a perfect power except for g2: if b > 1 and br generates (Z/(p))×
where r ≥2, then b generates (Z/(p))× and b < br.
Probably each a ≥1 that is not a perfect power, besides 1, is gp for some prime p (and
for inﬁnitely many p if a > 1). The table below lists, for the ﬁrst 14 positive integers a that
are not perfect powers besides 1, the ﬁrst p such that gp = a. It is on OEIS at A023048.
a
1
2
3
5
6
7
10
11
12
13
14
15
17
18
1st p s.t. gp = a
2
3
7
23
41
71
313
643
4111
457
1031
439
311
53173
8Artin conjectured more precisely that the set of such p has positive density among the primes, and he
gave a proposed a formula for that density. Any subset of the primes with positive density is inﬁnite.

<!-- page 18 -->
18
KEITH CONRAD
References
[1] M. Baker, Primitive roots, discrete logarithms, and p-adic numbers, https://mattbaker.blog/2013/
11/07/primitive-roots-discrete-logarithms-and-the-interplay-between-p-adic-and-complex-
numbers/.
[2] C. Bertault, “Une identit´e remarquable au service de (Z/pZ)∗,” Revue de Math´ematiques Sp´eciales 131,
Jan. 2021. URL http://christophebertault.fr/articles/.
[3] E. Bujalance Garc´ıa, J. J. Etayo Gordejuela, and J. M. Gamboa Mutuberr´ıa, Teor´ıa Elemental de Grupos,
Univ. Nac. Educ. Distancia, Madrid, 2002.
[4] M. Bullynck, “Decimal periods and their tables: a German research topic (1765-1801),” URL https://
halshs.archives-ouvertes.fr/halshs-00663295/document.
[5] L. Euler, “Demonstrationes circa residua ex divisione potestatum per numeros primos resultantia,” Novi
commentarii academiae scientiarum Petropolitanae 18 (1773), 85–135, 1774, Opera Omnia I, vol. 3,
240–281. URL https://www.biodiversitylibrary.org/item/38569#page/157/mode/1up and https://
scholarlycommons.pacific.edu/euler-works/449/.
[6] C. F. Gauss, Disquisitiones Arithmeticae, translated by Arthur A. Clarke, Yale Univ. Press, New Haven,
1966.
[7] J. H. Lambert, “Adnotata quaedam de numeris, eorumque anatomia,” Nova Acta Eruditorum (1769),
URL http://www.kuttaka.org/∼JHL/L1769e.pdf.
[8] J. Rotman, Advanced Modern Algebra, 3rd ed., Part 1, Amer. Math. Soc., Providence, 2015.
[9] V. Shoup, A Computational Introduction to Number Theory and Algebra, 2nd edition, Cambridge Univ.
Press, 2008. URL https://shoup.net/ntb/.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*