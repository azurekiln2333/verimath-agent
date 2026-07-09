# A4Noindex2

> **Source**: https://kconrad.math.uconn.edu/blurbs/A4noindex2.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
NO SUBGROUP OF A4 HAS INDEX 2
KEITH CONRAD
Lagrange’s theorem says that if H is a subgroup of a ﬁnite group G then the order of H
divides the order of G. It is natural to ask about a converse: if G is a ﬁnite group and the
integer d ≥1 divides the order of G, must G contain a subgroup of order d? The answer
is no, and the ﬁrst such example is the group A4: it has order 12 and it has subgroups of
orders 1, 2, 3, 4, and 12, but A4 has no subgroup of order 6, or equivalently no subgroup of
index 2.1 Here is a proof of that using left cosets.
Theorem 1. There is no subgroup of index 2 in A4.
Proof. Suppose a subgroup H of A4 has index 2, so |H| = 6. We will show for each g ∈A4
that g2 ∈H.
If g ∈H then clearly g2 ∈H. If g ̸∈H then gH is a left coset of H diﬀerent from H
(since g ∈gH and g ̸∈H), so from [G : H] = 2 the only left cosets of H are H and gH.
Which one is g2H? If g2H = gH then g2 ∈gH, so g2 = gh for some h ∈H, and that
implies g = h, so g ∈H, but that’s a contradiction. Therefore g2H = H, so g2 ∈H.
Every 3-cycle (abc) in A4 is a square: (abc) has order 3, so (abc) = (abc)4 = ((abc)2)2.
Thus H contains all 3-cycles in A4. The 3-cycles are
(123), (132), (124), (142), (134), (143), (234), (243)
and that is too much since there are 8 of them while |H| = 6. Hence H does not exist.
□
We will now give four more proofs that there is no subgroup of index 2 in A4 as corollaries
of four diﬀerent theorems from group theory.
Theorem 2. If G is a ﬁnite group and N ◁G then every element of G with order relatively
prime to [G : N] lies in N. In particular, if N has index 2 then all elements of G with odd
order lie in N.
Proof. Let g be an element of G with order m, which is relatively prime to [G : N]. Reducing
the equation gm = e modulo N gives gm = e in G/N. Also g[G:N] = e, so the order of g in
G/N divides m and [G : N]. These numbers are relatively prime, so g = e, which means
g ∈N.
A subgroup with index 2 is normal, so this theorem says a subgroup of G with index 2
must contain all elements of G with odd order (that’s an order relatively prime to 2).
□
Corollary 3. There is no subgroup of index 2 in A4.
Proof. If A4 has a subgroup with index 2 then by Theorem 2, all elements of A4 with odd
order are in the subgroup. But A4 contains 8 elements of order 3 (there are 8 diﬀerent
3-cycles), and an index-2 subgroup of A4 has size 6, so not all elements of odd order can lie
in the subgroup.
□
That proof is very closely related to the ﬁrst proof we gave.
1The groups of order 12 not isomorphic to A4 each have subgroups of orders 1, 2, 3, 4, 6, and 12.
1

<!-- page 2 -->
2
KEITH CONRAD
Theorem 4. If G is a ﬁnite group with a subgroup of index 2 then its commutator subgroup
has even index.
Proof. If [G : H] = 2 then H ◁G, so G/H is a group of size 2 and thus is abelian. In an
abelian group the only commutator is trivial, so the reduction homomorphism G →G/H
sends every commutator in G to the identity of G/H.
That means H contains every
commutator of G, so H contains the commutator subgroup of G. The index in G of the
commutator subgroup of G is therefore divisible by [G : H] = 2.
□
Corollary 5. There is no subgroup of index 2 in A4.
Proof. We will show the commutator subgroup of A4 has odd index, so A4 has no index-2
subgroup by Theorem 4. The subgroup
V = {(1), (12)(34), (13)(24), (14)(23)}
is normal in A4 and A4/V has size 3, hence is abelian, so the commutator subgroup of A4
is inside V . Each element of V is a commutator (e.g., (12)(34) = [(123), (124)]), so V is the
commutator subgroup of A4. It has index 3, which is odd.
□
Theorem 6. Every group of size 6 is cyclic or isomorphic to S3.
Proof. This is a special case of the classiﬁcation of groups of order pq for distinct primes p
and q, but we give a self-contained treatment in this special case using group actions.
Let G have size 6 and assume G is not cyclic. We want to show G ∼= S3. By Cauchy’s
theorem, G contains elements a with order 2 and b with order 3. The subgroup H = {1, a}
has index 3, so the usual left multiplication action of G on the left coset space G/H is a
homomorphism G →Sym(G/H) ∼= S3. If g is in the kernel then gH = H, so g ∈H. Thus,
if the kernel is nontrivial then it contains a. In particular, abH = bH. Since bH = {b, ba}
and abH = {ab, aba}, either b = ab or b = aba. The ﬁrst choice is impossible, so b = aba.
Since a has order 2, ab = ba−1 = ba, which means a and b commute. Thus ab has order
2 · 3 = 6, so G is cyclic.
We were assuming G is not cyclic, so the kernel of the map
G →Sym(G/H) is trivial, hence this is an isomorphism.
□
Corollary 7. There is no subgroup of index 2 in A4.
Proof. If A4 has an index-2 subgroup H, that subgroup has size 6 and therefore is isomorphic
to either Z/(6) or S3. There are no elements in A4 with order 6, so the ﬁrst choice is
impossible: H must be isomorphic to S3. In S3 there are three elements of order 2 (the
transpositions). The group A4 also has only three elements of order 2 (the (2, 2)-cycles
(12)(34), (13)(24), (14)(23)), so all the elements of order 2 in A4 must lie in H.
However, the elements of order 2 in S3 don’t commute with each other while the elements
of order 2 in A4 do commute with each other, so we have a contradiction from H being
isomorphic to S3. Alternatively, in A4 the identity and the three elements of order 2 are a
group (namely the group V mentioned earlier), so H contains a subgroup of order 4, but
by Lagrange’s theorem a group of order 6 can’t have a subgroup of order 4. Again we have
a contradiction.
□
The next approach, which shares some features of the proof of Corollary 7, was suggested
to me by Michiel Vermeulen and is based on the following theorem.
Theorem 8. A group of even order contains an element of order 2.

<!-- page 3 -->
NO SUBGROUP OF A4 HAS INDEX 2
3
Proof. Let G be a group with even order. Pair together each g ∈G with its inverse g−1.
The set {g, g−1} has two elements unless g = g−1, meaning g2 = e. Therefore
|G| = 2|{pairs {g, g−1} : g ̸= g−1}| + |{g ∈G : g = g−1}|.
The left side is even by hypothesis, and the ﬁrst term on the right side is even from the
factor of 2. Therefore |{g ∈G : g2 = e}| is even. This count is positive, since g = e is one
possibility where g2 = e. Since this count is even, there must be at least one more such g,
so some g ̸= e in G satisﬁes g2 = e, which implies g has order 2.
□
While Cauchy’s theorem says more generally that for each prime p dividing the order of
a ﬁnite group G there is an element of G with order p, that is more diﬃcult to show than
the special case p = 2.
Corollary 9. There is no subgroup of index 2 in A4.
Proof. Assume A4 has a subgroup H with index 2. Then |H| = 6, so by Theorem 8 there is
an h ∈H with order 2. In A4 the elements of order 2 are the (2,2)-cycles (12)(34), (13)(24),
and (14)(23), so H contains some (2, 2)-cycle. Since index 2 subgroups are normal and
all (2, 2)-cycles in A4 are conjugate in A4, H contains all the (2, 2)-cycles of A4. Then H
contains V = {(1), (12)(34), (13)(24), (14)(23)}, a group of order 4. However, by Lagrange’s
theorem a group of order 6 can’t contain a subgroup of order 4, so we have a contradiction.
□
For more proofs of this result, see [1].
References
[1] M. Brennan, D. Machale, Variations on a Theme: A4 Deﬁnitely Has No Subgroup of Order Six!, Math.
Mag. 73 (2000), 36–40. Online at https://www.maa.org/sites/default/files/269148715312.pdf.
bannered.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*