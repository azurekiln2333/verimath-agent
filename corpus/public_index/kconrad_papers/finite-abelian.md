# Decomposition of Finite Abelian Groups

> **Source**: https://kconrad.math.uconn.edu/blurbs/finite-abelian.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
DECOMPOSITION OF FINITE ABELIAN GROUPS
KEITH CONRAD
1. Introduction
Our goal is to prove the following decomposition theorem for ﬁnite abelian groups.
Theorem 1.1. Each nontrivial ﬁnite abelian group A is a direct sum of cyclic subgroups
of prime-power order: A = C1 ⊕· · · ⊕Cr, where Ci is cyclic and |Ci| is a prime power.1
Our strategy to prove Theorem 1.1 has the following steps:
• Deﬁne an analogue of primality and compositeness for ﬁnite abelian groups with
respect to direct sums, called indecomposability and decomposability.
• Prove each nontrivial ﬁnite abelian group is a direct sum of indecomposable sub-
groups by copying the proof that integers greater than 1 have prime factorizations.
• Show the indecomposable ﬁnite abelian groups are cyclic of prime-power order.
The decomposition in Theorem 1.1 is both unique and not unique. For example,
(1.1)
(Z/16Z)× = {±1 mod 16} × ⟨3 mod 16⟩= {1, 7 mod 16} × ⟨5 mod 16⟩.
This shows an abelian group can be a direct product of cyclic subgroups of order 2 and 4 in
more than one way, so in the most basic sense such a decomposition is not unique. On the
other hand, the cyclic subgroups in one decomposition are isomorphic to those in the other.
So if we consider the cyclic p-groups in a direct sum decomposition up to isomorphism (and
account for multiplicity) then the decomposition is unique. That is analogous to uniqueness
of prime factorization in Z+.
2. Decomposable and Indecomposable finite abelian groups
Here is an analogue for ﬁnite abelian groups of prime and composite numbers.
Deﬁnition 2.1. Let A be a nontrivial ﬁnite abelian group. Call A indecomposable if we
can’t write A = B ⊕C for some nontrivial subgroups B and C. Call A decomposable if we
can write A = B ⊕C for two nontrivial subgroups B and C.
Example 2.2. A group of prime order is abelian (it’s cyclic) and is indecomposable. For
a group to be decomposable it at least must have nontrivial proper subgroups, and a group
of prime order does not have such subgroups.
Example 2.3. A cyclic group of prime-power order is indecomposable. Let A be cyclic of
order pk where k ≥1. If A = B ⊕C where B and C are nontrivial subgroups of A then
B and C have p-power order greater than 1 and thus B and C each contain a subgroup of
order p (a subgroup of a cyclic group is cyclic and a cyclic group of order n has an element
of order d for each d dividing n). That implies A has more than one subgroup of order p,
but in a cyclic group there is at most one subgroup per size. Thus A is indecomposable.
Remark 2.4. The groups Z/(4) and Z/(2) ⊕Z/(2) are not isomorphic since Z/(4) is
indecomposable. Or since Z/(4) has an element of order 4 and Z/(2) ⊕Z/(2) does not.
1We write abstract abelian groups here additively, so outside of examples we speak about direct sums
rather than direct products.
1

<!-- page 2 -->
2
KEITH CONRAD
Theorem 2.5. A nontrivial ﬁnite abelian group is a direct sum of indecomposable subgroups.
Proof. This argument will be the same as the standard proof of the existence of prime
factorization in the positive integers. We argue by induction on the order n of the group.
For the base case n = 2, abelian groups of order 2 are indecomposable since 2 is prime
(Example 2.2). Suppose n > 2 and each nontrivial abelian group of order less than n is a
direct sum of indecomposable subgroups. Let A be abelian of order n.
Case 1: A is indecomposable. We are done, since A is a direct sum of itself (one term).
Case 2: A is decomposable. We have A = B ⊕C for nontrivial subgroups B and C. Then
n = |B||C| with |B| and |C| being greater than 1, so they are less than n. By induction,
B = P1 ⊕· · · ⊕Pr,
C = Q1 ⊕· · · ⊕Qs
for indecomposable Pi and Qj. Then A = P1 ⊕· · · ⊕Pr ⊕Q1 ⊕· · · ⊕Qs.
□
3. Classification of indecomposable finite abelian groups
To give Theorem 2.5 more substance, we will describe the indecomposable ﬁnite abelian
groups. In Example 2.3 we saw cyclic groups of prime-power order are indecomposable. It
turns out every indecomposable ﬁnite abelian group is cyclic of prime-power order. We’ll
show the group has prime-power order by the next lemma, which decomposes a ﬁnite abelian
group in terms of a decomposition of its order into relatively prime parts.
Lemma 3.1. If A is an abelian group and |A| = mn where (m, n) = 1 then A = Am ⊕An
for the subgroups Am = {a ∈A : ma = 0} and An = {a ∈A : na = 0}.
Proof. The subsets Am and An are subgroups because A is abelian, e.g., if ma = 0 and
ma′ = 0 then m(a + a′) = ma + ma′ = 0 + 0 = 0. Using multiplicative notation for a
moment, we have (gh)m = gmhm when gh = hg, but it might not be true if gh ̸= hg.2
To show A = Am + An, write 1 = mx + ny for x, y ∈Z since (m, n) = 1. For all a ∈A,
a = 1 · a = (mx + ny)a = (mx)a + (ny)a.
We have (ny)a ∈Am since m((ny)a) = (mn)(ya) = |A|ya = 0, and similarly (mx)a ∈An.
Thus A = Am + An.
To show Am ∩An = {0}, if a ∈Am ∩An then ma = 0 and na = 0, so a = (mx + ny)a =
x(ma) + y(na) = 0 + 0 = 0. Alternatively, the order of a divides m and n, so the order
divides (m, n) = 1 and thus a = 0.
We have shown A = Am + An and Am ∩An = {0}, so A = Am ⊕An.
□
Remark 3.2. Lemma 3.1 has a uniqueness aspect: |Am| = m, |An| = n, and these are the
unique subgroups of A with orders m and n. We will not need this.
Theorem 3.3. An indecomposable ﬁnite abelian group has prime-power order.
Proof. Let A be a nontrivial abelian group. We will prove the contrapositive of the theorem
for A: if |A| is not a prime power then A is decomposable.
Since |A| > 1 and |A| is not a prime power, |A| has more than one prime factor. Therefore
the prime factorization of |A| lets us write |A| = mn where (m, n) = 1 and m and n are
both greater than 1. For example, we can let m be the highest power of some prime dividing
|A| and let n be the complementary factor.
By Lemma 3.1, A = Am ⊕An. The subgroups Am and An are nontrivial by Cauchy’s
theorem: for a prime p dividing m, an element of A with order p lies in Am, and a similar
argument works for An. Note Cauchy’s theorem can be proved in a direct way for abelian
groups.3
□
2In S3, {g ∈S3 : g2 = (1)} is not a subgroup: it is {(1), (12), (13), (23)}.
3See https://kconrad.math.uconn.edu/blurbs/grouptheory/cauchypf.pdf.

<!-- page 3 -->
DECOMPOSITION OF FINITE ABELIAN GROUPS
3
To prove an indecomposable ﬁnite abelian p-group is cyclic, we’ll use the following lemma.
Lemma 3.4. A nontrivial ﬁnite abelian p-group with a unique subgroup of order p is cyclic.
Proof. Let A be a ﬁnite abelian p-group with a unique subgroup of order p and let pm be
the largest order of the elements of A. Then m ≥1 and each element of A has order pj
where j ≤m (A is a p-group and pm is the maximal order), so all elements of A have order
dividing pm: pmA = {0}.
Let a ∈A have order pm. Since pm−1a has order p, ⟨pm−1a⟩is a subgroup of order p,
so it is the only one by assumption. To prove A = ⟨a⟩, we’ll assume A ̸= ⟨a⟩and get a
contradiction.
The quotient group A/⟨a⟩(this makes sense since A is abelian) is nontrivial, abelian,
and of p-power order. By Cauchy’s theorem, A/⟨a⟩has an element of order p, say b. That
means b ̸∈⟨a⟩and pb ∈⟨a⟩. So we can write
pb = ja
for some j ∈Z. Since pmb = 0 (all elements of A have order dividing pm) and m ≥1,
0 = pmb = pm−1(pb) = pm−1(ja) = (pm−1j)a.
Since a has order pm, pm | pm−1j, so p | j. Thus j = pn for some n ∈Z, so pb = (pn)a.
Rewrite that as p(b−na) = 0. The only subgroup of order p is in ⟨a⟩, so b ∈na+⟨a⟩⊂⟨a⟩.
This contradicts b ̸∈⟨a⟩, so A = ⟨a⟩.
□
Remark 3.5. Lemma 3.4 is true without assuming A is abelian when p > 2,4 but the
quaternion group Q8 has a unique subgroup of order 2 and is not cyclic.
Theorem 3.6. For each ﬁnite abelian p-group A, let a be an element of A with maximal
order. Then A = ⟨a⟩⊕B for a subgroup B of A.
Proof. We use induction on |A|. The cases |A| = 1 and |A| = p are easy. Suppose |A| > p
and the theorem is true for all ﬁnite abelian p-groups of smaller order.
If A is cyclic then A = ⟨a⟩= ⟨a⟩⊕{0} since a has maximal order in A (each element of
maximal order in a ﬁnite cyclic group generates the group). Now we may assume A is not
cyclic. By Lemma 3.4, A has more than one subgroup of order p. In ⟨a⟩there is only one
subgroup of order p, so some b ∈A has order p and is not in ⟨a⟩. Thus ⟨a⟩∩⟨b⟩= {0}.
We will use the quotient group A/⟨b⟩. Let pm be the order of a, so m ≥1. We’ll show in
A/⟨b⟩that a also has order pm. From pma = 0 in A we get pma = 0 in A/⟨b⟩. If pm−1a = 0
then pm−1a ∈⟨a⟩∩⟨b⟩= {0}, but pm−1a ̸= 0. So pm−1a ̸= 0, which means a has order pm.
As in the proof of Lemma 3.4, all elements of A have order dividing pm, so pmA = {0}.
Therefore pm(A/⟨b⟩) = {0}. Since a has order pm, it has maximal order among the elements
of A/⟨b⟩. Since 1 < |A/⟨b⟩| < |A|, by induction ⟨a⟩is a direct summand of A/⟨b⟩:
(3.1)
A/⟨b⟩= ⟨a⟩⊕B/⟨b⟩
where B is a subgroup of A containing ⟨b⟩(all subgroups of A/⟨b⟩have the form B/⟨b⟩
where ⟨b⟩⊂B ⊂A). By (3.1), each element of A is congruent mod ⟨b⟩to a multiple of a
plus an element of B, so
A = ⟨a⟩+ B + ⟨b⟩= ⟨a⟩+ B,
where the last equation follows from ⟨b⟩⊂B. Since ⟨a⟩∩(B/⟨b⟩) = {0} we get ⟨a⟩∩B ⊂⟨b⟩,
so ⟨a⟩∩B ⊂⟨a⟩∩⟨b⟩= {0}. Thus A = ⟨a⟩+ B can be reﬁned to A = ⟨a⟩⊕B.
□
4See Corollary 4.10 in https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf.

<!-- page 4 -->
4
KEITH CONRAD
Example 3.7. In (Z/(16))×, the maximal order of the elements is 4. Two elements of
order 4 are 3 and 5: ⟨3⟩= {1, 3, 9, 11} and ⟨5⟩= {1, 5, 9, 13}. The elements of order 2 in
(Z/(16))× are 7, 9, and 15. Since ⟨7⟩and ⟨15⟩= ⟨−1⟩intersect ⟨3⟩and ⟨5⟩trivially,
(Z/(16))× = ⟨3⟩× ⟨7⟩= ⟨3⟩× ⟨−1⟩∼= Z/(4) × Z/(2)
and
(Z/(16))× = ⟨5⟩× ⟨7⟩= ⟨5⟩× ⟨−1⟩∼= Z/(4) × Z/(2).
This shows for a = 3 and a = 5 that B in Theorem 3.6 need not be unique. A simpler
example of that is Z/(p)⊕Z/(p) for prime p and a =
 0
1

: the group is ⟨
 0
1

⟩⊕⟨
 1
b

⟩for each
b ∈Z/(p), so p subgroups ⟨
 1
b

⟩(the lines y = bx) are complementary to ⟨
 0
1

⟩(the y-axis).
Corollary 3.8. An indecomposable ﬁnite abelian p-group is cyclic.
Proof. Let A be an indecomposable ﬁnite abelian p-group and a ∈A be an element of
maximal order, so a ̸= 0. By Theorem 3.6, A = ⟨a⟩⊕B for a subgroup B of A. Since A is
indecomposable and ⟨a⟩is nontrivial, B = {0}. Thus A = ⟨a⟩, which is cyclic.
□
Now we put everything together to prove Theorem 1.1. The hard work was already done.
Proof. A nontrivial ﬁnite abelian group A is a direct sum of indecomposable subgroups by
Theorem 2.5. The indecomposable ﬁnite abelian groups are the nontrivial cyclic p-groups
(for varying p) by Example 2.3, Theorem 3.3, and Corollary 3.8, so A is a direct sum of
cyclic p-groups.
□
The splitting in Theorem 3.6 using a cyclic subgroup of maximal order in a ﬁnite abelian
p-group works in all ﬁnite abelian groups A: for a maximal cyclic subgroup C, A = C⊕B for
a subgroup B. This is proved in Section 5 of https://kconrad.math.uconn.edu/blurbs/
grouptheory/charthy.pdf and that leads to a proof that each ﬁnite abelian group is a
direct sum of cyclic subgroups without relying on the case of ﬁnite abelian p-groups.
Example 3.9. In the group (Z/(100))×, of order 40, the maximal order of its elements is
20. One element of order 20 is 3, and (Z/(100))× = ⟨3⟩× ⟨−1⟩, which is a direct product
of cyclic groups of order 20 and 2.
4. Comparing two indecomposable decompositions
Let A be a direct sum of nontrivial cyclic subgroups of prime-power order in two ways:
(4.1)
A = C1 ⊕· · · ⊕Cr = C′
1 ⊕· · · ⊕C′
s.
We want to show r = s and, after relabeling, Ci ∼= C′
i for i = 1, . . . , r.5
This kind of
relation between two direct sum decompositions of A is what we mean when we say A has
a “unique” decomposition into indecomposable subgroups up to isomorphism. How is this
proved?
First there is a useful reduction step. For a prime p, the subset of elements of A with
p-power order form a subgroup of A (since A is abelian). In the direct sum of Ci’s in (4.1),
an element has p-power order if and only if it has component 0 in Ci whenever |Ci| is not a
power of p. That is, the elements of p-power order in A are the direct sum of subgroups Ci
of p-power order. Therefore the equality between two direct sum decompositions in (4.1)
implies, for each prime p, the equality (not merely isomorphism, but actual equality) of the
direct sums of cyclic p-subgroups in both decompositions. So proving the uniqueness in
(4.1) is reduced to the case that A has prime-power order.
5It is not true that we can literally have Ci = C′
i (equality), as shown with the subgroups of order 2 in
decompositions of (Z/(16))× in (1.1).

<!-- page 5 -->
DECOMPOSITION OF FINITE ABELIAN GROUPS
5
Theorem 4.1. For a prime p, when a nontrivial ﬁnite abelian p-group is written in two
ways as a direct sum of nontrivial cyclic subgroups, the number of direct summands of each
p-power order is the same for both direct sums.
Proof. Let A be a nontrivial ﬁnite abelian p-grpoup. If A ∼= Z/(pe1)⊕Z/(pe2)⊕· · ·⊕Z/(per)
for ei ∈Z+, we want to show e1, e2, . . . , er are determined by the group structure of A. The
key idea is to look at the successive quotient groups
A/pA,
pA/p2A,
p2A/p3A,
. . .
and get information using these. We’ll explain this by means of an example.
Suppose
(4.2)
A ∼= Z/pZ ⊕Z/pZ ⊕Z/p3Z ⊕Z/p4Z ⊕Z/p4Z.
Then
pA ∼= {0} ⊕{0} ⊕pZ/p3Z ⊕pZ/p4Z ⊕pZ/p4Z,
p2A ∼= {0} ⊕{0} ⊕p2Z/p3Z ⊕p2Z/p4Z ⊕p2Z/p4Z,
p3A ∼= {0} ⊕{0} ⊕{0} ⊕p3Z/p4Z ⊕p3Z/p4Z,
p4A = 0.
The direct sums on the right side are all compatible, e.g., the fourth direct summand each
time is a subgroup of the ﬁrst Z/p4Z in the direct sum decomposition of A. To compute the
successive quotients piA/pi+1A up to isomorphism, note (piZ/pjZ)/(pi+1Z/pjZ) is cyclic
of order p when j ≥i + 1, so
A/pA ∼= (Z/pZ)5,
pA/p2A ∼= (Z/pZ)3,
p2A/p3A ∼= (Z/pZ)3,
p3A/p4A ∼= (Z/pZ)2,
p4A/p5A = 0.
Each piA/pi+1A is isomorphic to a direct sum of some number of copies of Z/pZ, so all that
really matters is its size: set |piA/pi+1A| = pdi, so (d0, d1, d2, d3, d4) = (5, 3, 3, 2, 0) in (4.2).
A cyclic direct summand of order pe contributes to piA/pi+1A until i ≥e. It is the
diﬀerences di−1 −di for i ≥1, rather than the individual di’s, that provide the most directly
relevant information: the number of cyclic direct summands of order pi is di−1 −di. In
(4.2), for instance,
• d0 −d1 = 5 −3 = 2 and there are 2 summands in (4.2) that are cyclic of order p,
• d1 −d2 = 0 and there are 0 summands in (4.2) that are cyclic of order p2,
• d2 −d3 = 3 −2 = 1 and there is 1 summand in (4.2) that is cyclic of order p3,
• d3 −d4 = 2 −0 = 2 and there are 2 summands in (4.2) that are cyclic of order p4.
We can access this information using the individual di’s too: d0 is the number of nonzero
cyclic summands (note d0 = 5 in (4.2)) and in general di is the number of cyclic summands
of order at least pi+1. The largest i such that di ̸= 0 tells us the largest summand in A has
order pi+1. For (4.2), d3 ̸= 0 and di = 0 for i ≥4.
It is left to the reader to show this approach to recovering the number of cyclic summands
in (4.2) from the group structure of A works in the general case.
□
If A is a ﬁnite abelian p-group of order pn then A ∼= Z/(pn1) ⊕Z/(pn2) ⊕· · · ⊕Z/(pnk)
with n1 +· · ·+nk = n, and A is determined up to isomorphism by the exponents n1, . . . , nk

<!-- page 6 -->
6
KEITH CONRAD
(ignoring their order). Therefore the number of abelian groups of order pn, up to isomor-
phism, equals the number of ways of writing n as a sum of positive integers (ignoring their
order). For example, the diﬀerent ways of writing 2, 3, and 4 as a sum of positive integers
(in increasing order) is
2 = 1 + 1,
3 = 1 + 2 = 1 + 1 + 1,
4 = 1 + 3 = 2 + 2 = 1 + 1 + 2 = 1 + 1 + 1 + 1,
so the abelian groups of order p2, p3, and p4 are
• Z/(p2) and (Z/(p))2,
• Z/(p3), Z/(p) ⊕Z/(p2), and (Z/(p))3,
• Z/(p4), Z/(p) ⊕Z/(p3), (Z/(p2))2, (Z/(p))2 ⊕Z/(p2), and (Z/(p))4.
It’s natural to ask how much of this carries over to nonabelian ﬁnite groups. We can
deﬁne decomposable and indecomposable ﬁnite groups using direct product decompositions
(require the subgroups to be normal!). Theorem 2.5 extends easily to all nontrivial ﬁnite
groups. But in contrast to the abelian case, where indecomposable groups can be described
in a second way (they are the nontrivial cyclic p-groups), there isn’t a good description of
general indecomposable ﬁnite groups besides their deﬁnition. Simple groups are indecom-
posable (they have no nontrivial normal subgroups), but many non-simple groups are also
indecomposable.6 For example, Sn is indecomposable for n ≥2 but it is not simple when
n ≥3: the only nontrivial normal subgroup of Sn is An, so we can’t write Sn = An × H for
a subgroup H (necessarily normal of order 2).
There is a uniqueness for indecomposable decompositions of a ﬁnite group G: if
G = H1 × · · · × Hr = K1 × · · · × Ks
where Hi and Kj are indecomposable subgroups of G, then r = s and, after relabeling,
Hi ∼= Ki for i = 1, . . . , r. This is a special case of the Krull–Remak–Schmidt theorem.
While the decomposition of ﬁnite abelian groups into a direct product of cyclic subgroups
is very useful in applications of such groups, the decomposition of ﬁnite nonabelian groups
into a direct product of indecomposable (normal) subgroups is not that useful in practice.
Appendix A. Fitting’s Lemma
In this appendix we provide another approach to Theorem 3.3. It is based on the next
result, called Fitting’s lemma after Hans Fitting (not because the result is “ﬁtting” to be
used in mathematics).
Lemma A.1 (Fitting). Let A be a ﬁnite abelian group and f : A →A be a homomorphism.
For suﬃciently large k, A = im(fk) ⊕ker(fk).
This result, which is surprising when you ﬁrst meet it, shows that each homomorphism
of an abelian group A to itself leads to a direct sum decomposition of A if you iterate the
homomorphism enough times.
This is best appreciated by seeing how it looks in some
examples.
• Consider A = Z/(12) (the additive group mod 12, not units mod 12 under multi-
plication!) and f(a) = 2a. We have im(f) = {0, 2, 4, 6, 8, 10} = ⟨2⟩and ker(f) =
{0, 6} = ⟨6⟩. These subgroups intersect nontrivially (the kernel is inside the image).
Since f2(a) = 4a, we have im(f2) = {0, 4, 8} = ⟨4⟩and ker(f2) = {0, 3, 6, 9} = ⟨3⟩.
Compared to the image and kernel of f, the image of f2 is smaller and the kernel of
f2 is larger, and their intersection is trivial. We have a direct sum decomposition
A = ⟨4⟩⊕⟨3⟩= im(f2) ⊕ker(f2).
6We already saw this for abelian groups: Z/(pk) is indecomposable for k ≥1 but simple only for k = 1.

<!-- page 7 -->
DECOMPOSITION OF FINITE ABELIAN GROUPS
7
• Consider A = Z/(12) and f(a) = 6a. Then im(f) = {0, 6} = ⟨6⟩and ker(f) =
{0, 2, 4, 6, 8} = ⟨2⟩, while f2(a) = 36a = 0 so im(f2) = {0} and ker(f2) = A. Thus
A = im(f2) ⊕ker(f2).
• The decomposition in Lemma 3.1 ﬁts Fitting’s lemma: when |A| = mn with (m, n) =
1, A = Am ⊕An and Am = im(f) while An = ker(f) where f(a) = na.
Proof. Iterates of f are homomorphisms A →A. Since fk+1(a) = fk(f(a)), im(fk+1) ⊂
im(fk) and fk(a) = 0 ⇒fk+1(a) = f(fk(a)) = f(0) = 0, so ker(fk) ⊂ker(fk+1). That
means
im(f) ⊃im(f2) ⊃im(f3) ⊃· · · ,
ker(f) ⊂ker(f2) ⊂ker(f3) ⊂· · · ,
and since A is ﬁnite these containments have to stabilize: for some k ≥1, im(fk) = im(fℓ)
and ker(fk) = ker(fℓ) for all ℓ> k. We’ll show for such k that A = im(fk) ⊕ker(fk).
Step 1: A = im(fk) + ker(fk).
For a ∈A, fk(a) = f2k(a′) for some a′ since im(fk) = im(f2k). Thus fk(a) = fk(fk(a′)),
so fk(a−fk(a′)) = 0. Set b = a−fk(a′), so b ∈ker(fk). The equation a = fk(a′)+b shows
A = im(fk) + ker(fk).
Step 2: im(fk) ∩ker(fk) = {0}.
Suppose a = fk(c) for some c ∈A and fk(a) = 0. Then 0 = fk(a) = fk(fk(c)) = f2k(c),
so c ∈ker(f2k) = ker(fk), which implies a = fk(c) = 0.
□
Remark A.2. A seemingly weaker notion of stabilization for images and kernels is im(fk) =
im(fk+1) and ker(fk) = ker(fk+1) for some k ≥1, not equality from the kth point onwards.
This actually implies stabilization for all higher iterates of f: if im(fk) = im(fk+1) for
some k then im(fk) = im(fℓ) for all ℓ> k, and similarly for the kernels.
Therefore
A = im(fk) ⊕ker(fk) when fk and fk+1 have the same image and kernel. This is a more
practical condition to check in order to apply Fitting’s lemma.
Theorem A.3. An indecomposable ﬁnite abelian group has prime-power order.
Proof. Let A be an indecomposable ﬁnite abelian group. Since |A| > 1, |A| has a prime
factor, say p. Let f : A →A by f(a) = pa. then fk(a) = pka for each k ≥1. By Cauchy’s
theorem, A has an element of order p, so ker(f) ̸= {0}.
By Fitting’s lemma, A = im(fk) ⊕ker(fk) for some k ≥1. Since A is indecomposable,
im(fk) or ker(fk) is {0}. Since ker(f) ⊂ker(fk) and ker(f) ̸= {0}, ker(fk) is not {0}.
Therefore im(fk) = {0}, so pkA = {0}: all elements of A are killed by multiplication by pk,
so the order of each element of A is a power of p. Thus A has p-power order.
□

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*