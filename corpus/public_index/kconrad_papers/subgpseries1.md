# Subgpseries1

> **Source**: https://kconrad.math.uconn.edu/blurbs/subgpseries1.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SUBGROUP SERIES I
KEITH CONRAD
1. Introduction
If N is a nontrivial proper normal subgroup of a ﬁnite group G then N and G/N are
smaller than G. While it is false that G can be completely reconstructed from knowledge
of N and G/N (see Example 1.1 below), it is nevertheless a standard technique in ﬁnite
group theory to prove theorems about ﬁnite groups by induction on the size of the group
and thereby use information about the smaller groups N and G/N to say something about
G. Instead of using one normal subgroup, we will consider a (ﬁnite) series of subgroups
(1.1)
{e} = G0 ◁G1 ◁G2 ◁· · · ◁Gr = G
or
(1.2)
G = G0 ▷G1 ▷G2 ▷· · · ▷Gr = {e},
where each Gi is normal in the succeeding (or preceding) subgroup. The only diﬀerence
between (1.1) and (1.2) is the indexing, starting from the bottom or the top. Both (1.1) and
(1.2) are called normal series for G.1 Note {e} and G are among the Gi’s. We don’t assume
Gi ◁G, but only that each subgroup is normal in the next larger subgroup (succeeding or
preceding, depending on the indexing). The quotients Gi+1/Gi of (1.1) and Gi/Gi+1 of (1.2)
are called its factors. A normal series is a “ﬁltration” of G rather than a “decomposition”
of G: it is a way to ﬁll up G rather than a way to break it apart.
Example 1.1. For n ≥3, a normal series for Dn is {1}◁⟨r⟩◁Dn, with factors ⟨r⟩∼= Z/(n)
and Dn/⟨r⟩∼= Z/(2). A normal series for Z/(2n) is {0} ◁⟨2 mod 2n⟩◁Z/(2n), whose
factors are cyclic of orders n and 2. Thus non-isomorphic groups like Dn and Z/(2n) can
have normal series with isomorphic factors.
Example 1.2. If G = H1 ×H2 is a direct product of two groups then a normal series for G
is {(e, e)}◁H1×{e}◁H1×H2 with factors H1×{e} ∼= H1 and (H1×H2)/(H1×{e}) ∼= H2.
Similarly, a 3-fold direct product H1 × H2 × H3 has the normal series
{(e, e, e)} ◁H1 × {e} × {e} ◁H1 × H2 × {e} ◁H1 × H2 × H3
with successive factors isomorphic to H1, H2, and H3. More generally, a group that is a
direct product of ﬁnitely many groups admits a normal series whose factors are (isomorphic
to) the subgroups appearing in the direct product.
While Example 1.2 shows a ﬁnite direct product decomposition of G leads to a normal
series for G, most normal series do not come from a direct product decomposition. For
instance, the normal series for Dn in Example 1.1 doesn’t come from a direct product
decomposition of Dn into cyclic groups of orders 2 and n, since such a direct product would
be abelian and Dn is nonabelian.
1People who teach inﬁnite series in calculus may caution students not to use “series” as a synonym for
“sequence”, but in group theory it is traditional to do exactly that.
1

<!-- page 2 -->
2
KEITH CONRAD
In Section 2 we will look at some further examples of normal series and state the important
Jordan–H¨older theorem (it is proved in an appendix). Section 3 will discuss how a normal
series for a group becomes a normal series for related groups (subgroups, quotient groups,
and direct products). Two special kinds of subgroup series, central and derived series, are
the topics of Section 4. All of this general discussion is a prelude to Section 5, where we
will examine two classes of groups deﬁned in terms of normal series: nilpotent and solvable
groups. Nilpotent groups are always solvable but not conversely.
2. Some examples
Example 2.1. Each group G has the normal series {e} ◁G. This is the only normal series
if G is a simple group.
Example 2.2. Two normal series for Z/(6), with cyclic factors of order 2 and 3, are
{0} ◁⟨2⟩◁Z/(6)
and
{0} ◁⟨3⟩◁Z/(6).
Example 2.3. Three normal series for D4 are
{1} ◁⟨r2⟩◁D4,
{1} ◁⟨r2⟩◁⟨r⟩◁D4,
{1} ◁⟨s⟩◁⟨r2, s⟩◁D4.
The second series is a reﬁnement of the ﬁrst. The factors of the ﬁrst series are ⟨r2⟩∼= Z/(2)
and D4/⟨r2⟩∼= Z/(2) × Z/(2), while the second and third normal series both have 3 cyclic
groups of order 2 as their factors.
Example 2.4. A normal series for S4 is
{(1)} ◁A4 ◁S4.
The subgroup V = {(1), (12)(34), (13)(24), (14)(23)} is normal in A4 (and S4) and leads to
the reﬁned normal series
(2.1)
{(1)} ◁V ◁A4 ◁S4.
This can be reﬁned further to the normal series
(2.2)
{(1)} ◁U ◁V ◁A4 ◁S4,
where U is a 2-element subgroup of V . (Although U ◁V , U is not normal in A4 or S4.)
No further reﬁnements are possible since each subgroup in (2.2) has prime index (2 or 3) in
the next subgroup.
Our remaining examples involve matrix groups.
Example 2.5. For a ﬁeld F, the group Aﬀ(F) has the normal series
(2.3)

1
0
0
1

◁

1
∗
0
1

◁

∗
∗
0
1

,
with factors isomorphic to F and F ×.
In Example 2.4, a normal series for S4 was reﬁned twice. Reﬁning a normal series means
creating a longer normal series by inserting subgroups between the subgroups already in
the series. Repeating a subgroup already there is a trivial reﬁnement.
When can the series (1.1) be reﬁned nontrivially? If a factor Gi+1/Gi is not a simple
group then it has a proper nontrivial normal subgroup, which can be written as N/Gi

<!-- page 3 -->
SUBGROUP SERIES I
3
where Gi ⊂N ⊂Gi+1. Since N/Gi ◁Gi+1/Gi we have Gi ◁N ◁Gi+1. Therefore we can
insert N into (1.1) and obtain a new normal series for G with the same factors as before
except Gi+1/Gi has been replaced by the two nontrivial factors Gi+1/N and N/Gi. When
Gi+1/Gi is a simple group, there are no normal subgroups of Gi+1 lying strictly between Gi
and Gi+1, so (1.1) can’t be reﬁned by inserting a group nontrivially between Gi and Gi+1.
Therefore (1.1) is unreﬁnable (that is, (1.1) admits only trivial reﬁnements; unreﬁnable
means nontrivially unreﬁnable) precisely when all the factors Gi+1/Gi are simple or trivial.
Deﬁnition 2.6. An unreﬁnable normal series with no repetitions is a composition series.
Example 2.2 gives two composition series for Z/(6) and (2.2) is a composition series for
S4. The second and third normal series for D4 in Example 2.3 are composition series.
If a normal series is thought of as something like a “factorization” for the group, then a
reﬁnement of a normal series is like a further factorization and a composition series is like
a prime factorization. Having no repetitions is like avoiding factors of 1 in a factorization.
Theorem 2.7. Every nontrivial ﬁnite group has a composition series. In a ﬁnite abelian
group, every factor in a composition series has prime order.
Proof. Let G be a ﬁnite group with |G| > 1. It has a normal series, namely {e} ◁G. If
G is a simple group then this is a composition series. Otherwise G has a nontrivial proper
normal subgroup N and we have the normal series {e} ◁N ◁G. If N and G/N are simple
groups then this is a composition series. Otherwise we can reﬁne further. At each stage
when G has a normal series (1.1) with Gi ̸= Gi+1 for all i,
|G| = [Gr : Gr−1] · · · [G2 : G1][G1 : G0] ≥2r,
so the number of factors r is bounded above in terms of the size of G. Therefore we can’t
continue to reﬁne indeﬁnitely, so at some point we will reach a composition series.
When G is a ﬁnite abelian group, if Gi ◁Gi+1 are two successive terms in a composition
series then Gi+1/Gi is an abelian simple group, so necessarily of prime order.
□
Inﬁnite groups may or may not admit a composition series.
In particular, Z has no
composition series: if (1.1) is a normal series for Z then G1 is inﬁnite cyclic, so G1 has a
proper nontrivial subgroup that is obviously normal in Z. Therefore (1.1) can be reﬁned.
The following theorem for composition series is analogous to unique factorization in Z+.
Theorem 2.8 (Jordan–H¨older). If G is a nontrivial group and
{e} = G0 ◁G1 ◁G2 ◁· · · ◁Gr = G
and
{e} = eG0 ◁eG1 ◁eG2 ◁· · · ◁eGs = G
are two composition series for G then r = s and for some permutation π ∈Sr we have
eGi/ eGi−1 ∼= Gπ(i)/Gπ(i)−1 for 1 ≤i ≤r.
We don’t need this result, so its proof is left to an appendix. This theorem was proved
by Jordan in 1873, in the weaker form that [Gi : Gi−1] = [ eGπ(i) : eGπ(i)−1] for a suitable
π ∈Sr.
That the quotient groups themselves are isomorphic was proved by H¨older 16
years later. This theorem was an important milestone in the historical development of the
abstract quotient group concept [18].

<!-- page 4 -->
4
KEITH CONRAD
Example 2.9. Two composition series for D6 are
{1} ◁⟨r2⟩◁⟨r⟩◁D6
and
{1} ◁⟨r3⟩◁⟨r3, s⟩◁D6.
The factors in these composition series are one cyclic group of order 3 and two cyclic groups
of order 2. For instance, calling the subgroups in the ﬁrst series Gi and those in the second
series eGi, we have eG1/ eG0 ∼= G3/G2, eG2/ eG1 ∼= G2/G1, and eG3/ eG2 ∼= G1/G0. The Jordan–
H¨older theorem applies with π = (13) (or π = (123)).
Example 2.10. Not only is the Jordan–H¨older theorem an analogue of unique factorization
in Z, but unique factorization is the special case of the Jordan–H¨older theorem for ﬁnite
cyclic groups. Let’s see why.
Pick an integer n > 1. A composition series for Z/(n) will have factors of prime order,
since Z/(n) is abelian. If (1.1) is a composition series for G = Z/(n) and we set pi =
|Gi+1/Gi|, a prime number, then n = p1p2 · · · pr.
So composition series of Z/(n) yield
prime factorizations of n. Conversely, writing n = p1p2 · · · pr with primes pi, the series
{0} = ⟨p1p2 · · · pr⟩◁⟨p2p3 · · · pr⟩◁· · · ⟨pr⟩◁⟨1⟩= Z/(n),
is a composition series for Z/(n) with factors of prime orders p1, p2, . . . , pr. Thus the primes
and their multiplicities in a factorization of n can be recovered from a suitable composition
series for Z/(n). Comparing two composition series for Z/(n) shows, by the Jordan–H¨older
theorem, that n has a unique prime factorization.
Roughly speaking, the Jordan–H¨older theorem says that a group determines its compo-
sition series (assuming there is one at all). More precisely, a group determines the factors
(up to isomorphism) and their multiplicities in a composition series. But you can’t go the
other way: non-isomorphic groups can have the same composition factors with the same
multiplicities. For instance, for prime p both Dp and Z/(2p) have composition series with
one factor of size 2 and one of size p, by Example 1.1.
A more natural way of decomposing a group, at ﬁrst sight, is through direct products
instead of through normal series. Call a nontrivial group G decomposable if G ∼= H × K for
nontrivial groups H and K. If a nontrivial group is not decomposable, call it indecomposable.
Examples of indecomposable groups include nontrivial cyclic p-groups,2 Sn for n ≥2, and
Z. By an easy induction, each ﬁnite nontrivial group can be written as a direct product of
indecomposable groups. Some inﬁnite groups are (ﬁnite) direct products of indecomposable
groups and others are not.
Example 2.11. The group D6 = ⟨r, s⟩has two indecomposable decompositions: ⟨r2, s⟩×
⟨r3⟩and ⟨r2, rs⟩× ⟨r3⟩. The ﬁrst groups in both cases are not equal but are isomorphic.
Theorem 2.12 (Krull–Schmidt). If a group is isomorphic to H1×· · ·×Hr and K1×· · ·×Ks,
where the Hi’s and Kj’s are indecomposable, then r = s and there is some π ∈Sr such that
Hi ∼= Kπ(i) for all i.
Proof. See [14, Chap. II, §3].
□
The Krull–Schmidt theorem is nice to know, but it’s really not the right way to think
about “decomposing” nonabelian (ﬁnite) groups. Theorems of Krull–Schmidt type are more
important in other areas of algebra than group theory. For instance, see [7].
2See Example 2.3 in https://kconrad.math.uconn.edu/blurbs/grouptheory/finite-abelian.pdf.

<!-- page 5 -->
SUBGROUP SERIES I
5
3. Normal series under group constructions
We now look at how normal series behave under three constructions on groups: passage
to a subgroup, passage to a quotient group, and direct products. As you will see, there is
nothing really surprising in the results we ﬁnd or the way we ﬁnd them: the only way one
can imagine concocting a normal series for a subgroup, quotient group, and direct product
turns out to work. This material is primarily needed for technical work later. To ﬁx ideas,
we use an ascending normal series for G as in (1.1).
If H is a subgroup of G then intersecting H with each group in (1.1) yields
(3.1)
{e} = H0 ◁H1 ◁H2 ◁· · · ◁Hr = H,
where Hi := H ∩Gi. To see that Hi ◁Hi+1, and not just Hi ⊂Hi+1, the kernel of the
natural homomorphism Hi+1 →Gi+1/Gi is Hi+1 ∩Gi = (H ∩Gi+1) ∩Gi = H ∩Gi = Hi.
Therefore not only is Hi ◁Hi+1 for all i, but also Hi+1/Hi is isomorphic to a subgroup of
Gi+1/Gi. This proves the following theorem.
Theorem 3.1. If we intersect the normal series of G in (1.1) with a subgroup H, we obtain
the normal series (3.1) of H whose successive factors are isomorphic to subgroups of the
successive factors of (1.1).
Example 3.2. View D4 inside S4 by labelling the vertices of a square in order as 1, 2, 3, 4.
Let r = (1234), s = (24) (so D4 = ⟨r, s⟩), and U = ⟨(13)(24)⟩= ⟨r2⟩in (2.2). Intersecting
the normal series (2.2) of S4 with D4 gives a normal series for D4: {(1)} ◁⟨r2⟩◁⟨r2, rs⟩◁
⟨r2, rs⟩◁D4. Notice the repetition.
Corollary 3.3. When the factors in (1.1) belong to a class of groups closed under passage
to subgroups, every subgroup of G has a normal series whose factors are in that class.
Proof. The construction we gave for a normal series of a subgroup from a normal series
of the original group has factors that are (isomorphic to) subgroups of the factors in the
original normal series.
□
Example 3.4. If G admits a normal series whose factors are abelian then so do all subgroups
of G.
Having created normal series for a subgroup, we now look at normal series for a quotient
group. Let N ◁G and (1.1) be a normal series for G. To construct a normal series for G/N,
note that NGi is a subgroup of G and NGi ⊂NGi+1, so
(3.2)
N = NG0 ◁NG1 ◁NG2 ◁· · · ◁NGr = G.
The reason that NGi ◁NGi+1 is that N and Gi+1 each normalize NGi inside of G. Since
N is normal in G, it is normal in every group in (3.2), so we can reduce (3.2) modulo N to
get
(3.3)
{e} = G0 ◁G1 ◁G2 ◁· · · ◁Gr = G/N,
where Gi := (NGi)/N ∼= Gi/(N ∩Gi). The natural map Gi →Gi is onto for all i, so the
map Gi+1 →Gi+1/Gi is onto and kills Gi, so Gi+1/Gi is isomorphic to a quotient group of
Gi+1/Gi for all i. This proves the following theorem.
Theorem 3.5. If (1.1) is a normal series of G then (3.3) is a normal series of G/N and
its successive factors are quotient groups of the successive factors in (1.1).

<!-- page 6 -->
6
KEITH CONRAD
Corollary 3.6. When G has a normal series whose factors belong to a class of groups
closed under passage to quotient groups, then all quotient groups of G have a normal series
whose factors are in that class.
Example 3.7. Continuing Example 3.4, if G admits a normal series whose factors are
abelian then so do all quotient groups of G.
Next we look at normal series for a direct product. Suppose (1.1) is a normal series for
G, and another group eG has the normal series
(3.4)
{e} = eG0 ◁eG1 ◁eG2 ◁· · · ◁eGs = eG.
Then we can get a normal series for G × eG with r + s factors:
(3.5)
G0 × {e} ◁G1 × {e} ◁· · · ◁G × {e} ◁G × eG1 ◁· · · ◁G × eG.
The successive inclusions here are either Gi ×{e} ⊂Gi+1 ×{e} or G× eGj ⊂G× eGj+1. The
normality of Gi in Gi+1 and eGj in eGj+1 make successive subgroups in (3.5) normal in each
other, with quotient groups isomorphic to the factors in either (1.1) or (3.4).
Theorem 3.8. If G and eG have normal series (1.1) and (3.4) then the direct product G× eG
has normal series (3.5), whose successive factors are isomorphic to the successive factors of
(1.1) followed by the successive factors of (3.4).
Corollary 3.9. If two groups G and eG have normal series whose factors belong to a class
of groups then G × eG has a normal series whose factors are in that class.
Example 3.10. If G and eG have normal series with abelian factors then so does G × eG.
4. Abelian and Central series
In a group G, the center Z = Z(G) and commutator subgroup [G, G] play somewhat
dual3 roles:
• Commutativity of G is equivalent to both Z = G and [G, G] = {e}. (However,
ﬁniteness of G/Z and [G, G] are not equivalent, and the conditions Z = {e} and
[G, G] = G are not equivalent. See Remark 4.30.)
• Every subgroup of G that is contained in Z is normal in G since Z is abelian, while
every subgroup of G that contains [G, G] is normal in G since G/[G, G] is abelian.
• Corollary 4.28 will put the construction of two subgroup series, based on Z and
[G, G], in dual positions: one is ascending, the other is descending, and they have
the same number of terms.
If G is nonabelian, a measure of how close this group is to being abelian could be based
on how close Z is to G or how close [G, G] is to {e}. We will introduce three series of
subgroups, two generalizing the commutator subgroup (called the derived series G(i) and
lower central series Li, both tending down to {e}) and one generalizing the center (called
the upper central series Zi and tending up to G). These will be used to deﬁne solvable and
nilpotent groups in Section 5. Before we introduce these three particular subgroup series,
we deﬁne the general kinds of series they will all turn out to be examples of.
3Saying Z and [G, G] are dual to each other is informal usage. It is not meant in the sense of category
theory.

<!-- page 7 -->
SUBGROUP SERIES I
7
Deﬁnition 4.1. An ascending series
(4.1)
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂G
and descending series
(4.2)
G = G0 ⊃G1 ⊃G2 ⊃· · · ⊃{e}
are called abelian if successive subgroups are normal in each other and all factors in the
series (Gi+1/Gi or Gi/Gi+1) are abelian. We don’t assume G is some Gi in (4.1) or {e} is
some Gi in (4.2).
We call (4.1) a central series if, for all i, Gi◁G (stronger than Gi◁Gi+1!) and Gi+1/Gi ⊂
Z(G/Gi). Similarly, (4.2) is called central if, for all i, Gi ◁G and Gi/Gi+1 ⊂Z(G/Gi+1).
In the deﬁnition of a central series, we need Gi ◁G to make sense of G/Gi as a group.
A central series is an abelian series since, for instance, the condition Gi+1/Gi ⊂Z(G/Gi)
implies Gi+1/Gi is abelian. But the converse is false, since an abelian subgroup need not
lie in the center of the group.
Example 4.2. The normal series for Aﬀ(F) in Example 2.5 is abelian since its factors are
isomorphic to F and F ×. But it is not central when |F| > 2 since {( 1 ∗
0 1 )} ̸⊂Z(Aﬀ(F)).
Both abelian and central series can be described in terms of “commutator subgroups of
two subgroups.” For subgroups H and K in G, set
[H, K] = ⟨[h, k] : h ∈H, k ∈K⟩.
Two simple properties of this construction are: [H, K] = [K, H] (since [h, k]−1 = [k, h])
and if H and K are normal in G then [H, K] is normal in G (because g[h, k]g−1 =
[ghg−1, gkg−1]). We have [H, K] = {e} if and only if hk = kh for all h ∈H and k ∈K.
Theorem 4.3. The series (4.1) is abelian if and only if [Gi+1, Gi+1] ⊂Gi for all i and
(4.2) is abelian if and only if [Gi, Gi] ⊂Gi+1 for all i.
The series (4.1) is central if and only if [G, Gi+1] ⊂Gi for all i and (4.2) is central if
and only if [G, Gi] ⊂Gi+1 for all i.
Proof. If (4.1) is abelian then Gi+1/Gi is an abelian group for all i, so in Gi+1/Gi we have
[x, y] = 1 for all x and y in Gi+1. This is equivalent to [x, y] ∈Gi for all x and y in Gi+1,
which is equivalent to [Gi+1, Gi+1] ⊂Gi. The argument for when (4.2) is abelian is similar.
If (4.1) is central then elements of Gi+1/Gi commute with elements of G/Gi, which
is equivalent to ggi+1 ≡gi+1g mod Gi.
That is the same as [g, gi+1] ∈Gi for all i, so
[G, Gi+1] ⊂Gi. Conversely, suppose [G, Gi+1] ⊂Gi. Then [G, Gi] ⊂Gi since Gi ⊂Gi+1, so
ggig−1g−1
i
∈Gi for all g ∈G and gi ∈Gi. That is equivalent to ggig−1 ∈Gi, which means
gGig−1 ⊂Gi for all g ∈G, so Gi ◁G. Returning now to the inclusion [G, Gi+1] ⊂Gi, we
can reduce this modulo Gi to get [G/Gi, Gi+1/Gi] = {e} in G/Gi, so Gi+1/Gi ⊂Z(G/Gi).
The argument for when (4.2) is central is similar.
□
When (4.2) is an abelian series, so [Gi, Gi] ⊂Gi+1 for all i by Theorem 4.3, at i = 0 we
get [G, G] ⊂G1. At i = 1, [G1, G1] ⊂G2, so [[G, G], [G, G]] ⊂G2 since [G, G] ⊂G1. This
suggests introducing a collection of “iterated commutator subgroups” G(i) for i ≥0 deﬁned
recursively by G(0) = G, G(1) = G′ = [G, G], G(2) = G′′ = [G′, G′], and
G(i+1) = (G(i))′ = [G(i), G(i)]

<!-- page 8 -->
8
KEITH CONRAD
for i ≥0. Then G(i+1) is the commutator subgroup of G(i), so G(i+1)◁G(i) and G(i)/G(i+1) =
G(i)/(G(i))′ is abelian. Since [N, N] ◁G if N ◁G, we have G(i) ◁G for all i by induction,
so the descending series
(4.3)
G = G(0) ⊃G′ ⊃G′′ ⊃· · · ⊃{e}
consists of normal subgroups of G with successive abelian quotients.
Deﬁnition 4.4. The series (4.3) is called the derived series of G.
Example 4.5. If G is abelian then G′ = {e}.
Example 4.6. Let G = Dn. For n ≥3, D′
n = ⟨r2⟩, which is abelian, so D′′
n = {1}. For
n = 1 and 2, D′
n is trivial since D1 and D2 are abelian. Thus every dihedral group has a
derived series that reaches the identity in at most 2 steps.
Example 4.7. Let G = An for n ≥3. For n ≥5, A′
n = An since [(abd), (ace)] = (abc)
when a, b, c, d, e are distinct. Thus A(i)
n = An for i ≥0 when n ≥5, so the derived series for
An does not reach the identity.
Since A′
4 = V (the normal 2-Sylow subgroup of A4) and V is abelian, V ′ is trivial. Thus
A
′′
4 is trivial. Since A3 is abelian, A′
3 is trivial.
Example 4.8. Let G = Sn for n ≥3. We have G′ = [Sn, Sn] = An. Therefore, by the
previous example, G(i) = An for i ≥1 when n ≥5, so the derived series for Sn does not
reach the identity. On the other hand, S′
4 = A4 so S′′′
4 is trivial, and S′
3 = A3 so S′′
3 is
trivial.
Example 4.9. Let G = Heis(F), the group of 3 × 3 upper-triangular matrices


1
a
b
0
1
c
0
0
1

.
Then G′ = Z(G), which is abelian, so G′′ = {I3}.
Example 4.10. For n ≥1, the group Heisn(F) consists of (n + 2) × (n + 2) matrices


1
x
z
0
In
y
0
0
1

:=







1
x1
· · ·
xn
z
0
1
· · ·
0
y1
...
...
...
...
...
0
0
· · ·
1
yn
0
0
· · ·
0
1







under matrix multiplication:


1
x
z
0
1
y
0
0
1




1
x′
z′
0
1
y′
0
0
1

=


1
x + x′
z + z′ + x · y′
0
1
y + y′
0
0
1

.
Writing these matrices as (x, y, z), the group law and inversion are
(x, y, z)(x′, y′, z′) = (x + x′, y + y′, z + z′ + x · y′),
(x, y, z)−1 = (−x, −y, −z + x · y),
while the conjugation and commutator formulas are
(x, y, z)(x′, y′, z′)(x, y, z)−1 = (x′, y′, z′ + x · y′ −x′ · y)
[(x, y, z), (x′, y′, z′)] = (0, 0, x · y′ −x′ · y).

<!-- page 9 -->
SUBGROUP SERIES I
9
From this, Heisn(F)′ = Z(Heisn(F)) = {(0, 0, z) : z ∈F}, so Heisn(F)′′ is trivial.
Example 4.11. Let G = Aﬀ(F). For |F| > 2, G′ = {( 1 ∗
0 1 )}, which is abelian, so G′′ = {I2}.
For |F| = 2, G is abelian, so G′ = {I2}.
Example 4.12. Let G = GL2(F). When |F| > 3, it can be shown that GL2(F)′ = SL2(F)
and SL2(F)′ = SL2(F) (these are not obvious), so GL2(F)(i) = SL2(F) for i ≥1: the
derived series for GL2(F) stabilizes at SL2(F) and never reaches the identity.
When |F| = 3, GL2(F)′ = SL2(F), which has order 24, and SL2(F)′ is the 2-Sylow
subgroup of SL2(F) and isomorphic to Q8. Since Q′′
8 = {1}, GL2(F)
′′′ = {I3} when |F| = 3.
When |F| = 2, GL2(F) ∼= S3 so GL2(F)′′ = {I2}.
The following theorem tells us that the derived series controls the decay of all abelian
series from below.
Theorem 4.13. If (4.2) is an abelian series for G then G(i) ⊂Gi for all i. In particular,
if G has an abelian normal series then the derived series is a normal series.
Proof. We have G(0) = G0 = G. Since G/G1 is abelian by hypothesis, G′ ⊂G1. Assuming
G(i) ⊂Gi, since Gi/Gi+1 is abelian we get G′
i ⊂Gi+1, so G(i+1) = (G(i))′ ⊂G′
i ⊂Gi+1.
Now suppose G has a normal series with abelian factors. A normal series has both G
and {e} among the Gi’s, so we can index the series from the top down like (4.2). Then
G(i) ⊂Gi for all i and Gi = {e} for some i, so G(i) = {e} for some i. Therefore the derived
series of G reaches the identity and that makes it a normal series.
□
Theorem 4.13 shows that when G admits an abelian normal series its derived series is
its shortest descending abelian normal series: Gr = {e} implies G(r) = {e}, so no abelian
normal series can reach the identity before the derived series does.
Now we look at central series (rather than abelian series) for a group G. Suppose it is
written in descending form as in (4.2), so [G, Gi] ⊂Gi+1 for all i by Theorem 4.3. At i = 0 we
get [G, G] ⊂G1. At i = 1, [G, G1] ⊂G2, so [G, [G, G]] ⊂G2. This suggests introducing the
subgroups Li deﬁned by recursively by L0 = G, L1 = [G, G] = G′, L2 = [G, L1] = [L1, G],
and for i > 0
Li+1 = [G, Li] = [Li, G].
Since L1 ◁G, Li ◁G for all i by induction. Therefore Li+1 = [G, Li] ⊂Li, so
(4.4)
G = L0 ⊃L1 ⊃L2 ⊃· · · ⊃{e}.
Although L0 = G(0) and L1 = G′, usually Li ̸= G(i) for i > 1. By induction, G(i) ⊂Li
for all i. We’ll see how this looks for dihedral groups in an example below.
In G/Li+1 = G/[Li, G], the elements of Li commute with all elements of G, so Li/Li+1 ⊂
Z(G/Li+1). Therefore the Li’s are a descending central series of G.
Deﬁnition 4.14. The series (4.4) is called the lower central series of G.
As with the derived subgroups G(i), the Li’s might not form a normal series for G since
they may never reach {e}.
Example 4.15. If G is abelian, L1 = {e}.
Example 4.16. Let G = Dn. Then L1 = D′
n = ⟨r2⟩. For odd n, ⟨r2⟩= ⟨r⟩and [Dn, ⟨r⟩] =
⟨r2⟩= ⟨r⟩, so Li = ⟨r⟩for all i ≥1. For even n = 2km, Li = ⟨r2i⟩for 1 ≤i ≤k and Li stops

<!-- page 10 -->
10
KEITH CONRAD
shrinking at i = k since r2k has odd order: Li = ⟨r2k⟩for i ≥k. So the lower central series
reaches {1} only when n = 2k is a power of 2, in which case Lk−1 ̸= {1} and Lk = {1}.
The groups D1 and D2 are both abelian, so for them L1 = {1}.
For a comparison, the derived series of Dn reaches the identity in 2 steps and the lower
central series of Dn either stabilizes before the identity if n is not a power of 2 or reaches
the identity in k steps if n = 2k. So when the derived series and lower central series both
reach the identity (n = 2k), the derived series does so much more quickly.
In this example, we see the inclusion G(i) ⊂Li for a general group G is quite weak
compared to what actually happens when G = Dn: for n = 2k, for instance, G(i) becomes
trivial already at i = 2 while it takes the Li’s k steps to become trivial.
Thus we get
the idea that the derived series G(i) for a group G might decay exponentially faster than
the lower central series. In fact, the inclusion G(i) ⊂Li can always be strengthened to
G(i) ⊂L2i−1 for all i. (This follow by induction on i from the commutator containment
[Li, Lj] ⊂Li+j+1.)
Example 4.17. Let G = An for n ≥3. When n ≥5, A′
n = An so Li = G for i ≥0. When
n = 4, A′
4 = V and [A4, V ] = V , so Li = L1 for i ≥1. When n = 3, L1 = A′
3 is trivial since
A3 is abelian.
Example 4.18. Let G = Sn for n ≥3. We have L1 = S′
n = An. Since [(ab), (abc)] = (abc)
for distinct a, b, and c, L2 = [Sn, An] = An, so Li = L1 for i ≥1.
Example 4.19. Let G = Heis(F). Then L1 = [G, G] = Z (the Heisenberg group’s commu-
tator subgroup and center coincide), so L2 = [G, L1] = {I3}.
Example 4.20. Let G = Aﬀ(F). Then L1 = [G, G] = {( 1 ∗
0 1 )} and [G, L1] = L1 since
[( a b
0 1 ), ( 1 c
0 1 )] = ( 1 (a−1)c
0
1
), so Li = L1 for i ≥1. Unlike its derived series, which reaches the
identity in 2 steps, the lower central series of Aﬀ(F) does not reach the identity.
Example 4.21. Let G = GL2(F).
When |F| > 2, L1 = G′ = SL2(F) and L2 =
[GL2(F), SL2(F)] = SL2(F), so Li = SL2(F) for all i ≥1. When |F| = 2, GL2(F) =
SL2(F) ∼= S3 and [S3, A3] = A3, so Li = L1 for all i ≥1.
The following theorem explains the “lower” label on the lower central series: descending
central series are bounded below by the lower central series.
Theorem 4.22. If (4.2) is a central series for G then Li ⊂Gi for all i. In particular, if G
has a normal central series then the lower central series is a normal series.
Proof. To show Li ⊂Gi for all i we argue by induction. It is clear when i = 0. Assuming
Li ⊂Gi, Li+1 = [G, Li] ⊂[G, Gi]. Since (4.2) is a (descending) central series, [G, Gi] ⊂
Gi+1, so Li+1 ⊂Gi+1.
A normal central series can be indexed from the top down as in (4.2), so if Gi = {e} for
some i, then Li = {e} for some i, making the lower central series of G a normal series.
□
Now we consider ascending central series (4.1), so Gi+1/Gi ⊂Z(G/Gi). We will deﬁne
a sequence of “iterated centers” of G that control the growth of a central series (4.1) from
above, as the lower central series controls the decay of a central series (4.2) from below.
Set Z0 = {e} and Z1 = Z(G). Both are normal subgroups of G. Recursively, if we have
deﬁned a normal subgroup Zi ◁G, write the center of G/Zi as Zi+1/Zi:
Zi+1 = {g ∈G : gx ≡xg mod Zi for all x ∈G}.

<!-- page 11 -->
SUBGROUP SERIES I
11
(To compute this, determine the center of G/Zi and take its inverse image under the re-
duction map G →G/Zi to ﬁnd Zi+1.) Since the center of a group is a normal subgroup,
Zi+1/Zi ◁G/Zi, so Zi+1 ◁G. We obtain an ascending series of subgroups
(4.5)
{e} = Z0 ⊂Z1 ⊂Z2 ⊂· · · ⊂G
where Zi ◁G for all i (so Zi ◁Zi+1 for all i).
Deﬁnition 4.23. The series (4.5) is called the upper central series of G.
The recursive deﬁnitions of the three subgroup series G(i), Li, and Zi are in Table 1.
Name of Series
H0
Hi+1
Direction
Derived
G(0) = G
G(i+1) = [G(i), G(i)]
Descending
Lower Central
L0 = G
Li+1 = [G, Li] = [Li, G]
Descending
Upper Central
Z0 = {e}
Zi+1/Zi = Z(G/Zi)
Ascending
Table 1.
Example 4.24. If G is abelian then Z1 = G.
Example 4.25. We will determine the upper central series for the dihedral groups. Often
we will use the following characterization of a dihedral group: a group of order 2k with
generators x and y such that xk = e, y2 = e, and yxy−1 = x−1 is isomorphic to Dk.
When n is odd, Dn has trivial center, so Zi = {1} for all i.
When n = 2m with m ≥3 odd, Z1 = ⟨rn/2⟩and Dn/Z1 = ⟨r, s⟩. In this quotient group,
r has order n/2 and the group has generators with the relations of a dihedral group of order
n/2, so Dn/Z1 ∼= Dn/2 = Dm. Since m is odd, Dm has trivial center, so the center of Dn/Z1
is trivial. Therefore Z2 = Z1 and Zi = Z1 for all i ≥1.
Now suppose n = 2km where k ≥2 and m ≥3 is odd.
As before, Dn has center
Z1 = ⟨rn/2⟩and Dn/Z1 = ⟨r, s⟩∼= Dn/2. Now n/2 is even, so the center of Dn/Z1 is ⟨rn/4⟩.
Therefore Z2 = ⟨rn/4⟩and Dn/Z2 has order n/4 and generators satisfying the relations
of a dihedral group of order n/4, so Dn/Z2 ∼= Dn/4.
By induction, for i ≤k we have
Zi = ⟨rn/2i⟩and Dn/Zi ∼= Dn/2i. Since Dn/Zk ∼= Dm has trivial center (m is odd with
m ≥3), Zk+1 = Zk so Zi = Zk for i ≥k.
The remaining case is n = 2k. The groups D1 and D2 are both abelian, so for them
Zi = Dn for all i. Take now k ≥2. As in the previous case, Zi = ⟨rn/2i⟩= ⟨r2k−i⟩and
Dn/Zi ∼= Dn/2i = D2k−i for 0 ≤i ≤k −1. Then Dn/Zk−1 = ⟨r, s⟩∼= Z/(2) × Z/(2) = D2,
which is abelian (this never happened for n not a power of 2), so Zk = Dn.
That was a lot of computation, so let’s summarize what happens. If n is not a power of
2, then n = 2km where k ≥0 and m ≥3 is odd. The upper central series for Dn is
Z0 = {1} ⊂⟨rn/2⟩⊂⟨rn/4⟩⊂⟨rn/8⟩⊂· · · ⊂⟨rn/2k−1⟩⊂⟨rn/2k⟩= ⟨rm⟩= Zk
and Zi = ⟨rm⟩for i ≥k. If n is a power of 2, then n = 2k. For k ≥2, the upper central
series for D2k is
Z0 = {1} ⊂⟨rn/2⟩⊂⟨rn/4⟩⊂⟨rn/8⟩⊂· · · ⊂⟨rn/2k−1⟩= ⟨r2⟩⊂D2k = Zk
and Zi = D2k for i ≥k. If n = 1 or n = 2 then Zi = Dn for i ≥0.
Example 4.26. Let G = Heis(F). Then G/Z1 ∼= F 2 is abelian, so Z2 = G.

<!-- page 12 -->
12
KEITH CONRAD
G
Zi
Li
Dm, m ≥3 odd
{1}
⟨r⟩, i ≥1
D2km, k ≥1, m ≥3 odd
⟨rn/2k⟩, i ≥k
⟨r2k⟩, i ≥k
An, n ≥5
{(1)}
An
A4
{(1)}
V
Sn, n ≥3
{(1)}
An, i ≥1
Aﬀ(F), |F| > 2
{I2}
{( 1 ∗
0 1 )}
GL2(F), |F| > 2
F ×I2, i ≥1
SL2(F), i ≥1
Table 2.
In Table 2 are examples where the Zi’s do not reach G (and the Li’s do not reach {e}).
Theorem 4.27. If (4.1) is a central series for G then Gi ⊂Zi for all i. In particular, if G
has a normal central series then the upper central series is a normal series.
This is an upper analogue of Theorem 4.22.
Proof. To show Gi ⊂Zi we argue by induction. It is clear for i = 0. If Gi ⊂Zi for some i,
we want to show Gi+1 ⊂Zi+1. By deﬁnition, Zi+1/Zi is the center of G/Zi. For x ∈G and
y ∈Gi+1, xy ≡yx mod Gi since Gi+1/Gi ⊂Z(G/Gi), so xy ≡yx mod Zi by the inductive
hypothesis. Letting x run over G we see that y mod Zi ∈Z(G/Zi) = Zi+1/Zi, so y ∈Zi+1.
Now letting y vary shows Gi+1 ⊂Zi+1.
A normal central series can be indexed from the bottom up as in (4.1), so if Gi = G for
some i then Zi = G for some i, making the upper central series of G a normal series.
□
For all G, Z = G if and only if [G, G] = {e}. This is the case i = 1 of the following
connection between the upper and lower central series.
Corollary 4.28. For every group G, Zi = G for some i if and only if Li = {e} for some
i, in which case the least i’s for which these occur are the same.
Proof. Suppose Zn = G. Since G is reached, the upper central series can be viewed as a
descending normal central series by reversing the indices: set Gi = Zn−i for i = 0, 1, . . . , n.
Then for all i, Theorem 4.22 implies Li ⊂Gi = Zn−i, so Ln is trivial.
The converse
argument is similar, using Theorem 4.27.
□
Remark 4.29. A classical theorem about the center says that if G/Z is cyclic then G is
abelian. This can be generalized: if G/Zi is cyclic for some i ≥1 then G = Zi. Indeed,
G/Zi−1 has center Zi/Zi−1 and the quotient of G/Zi−1 by its center is isomorphic to G/Zi,
so if G/Zi is cyclic then by the classical theorem G/Zi−1 equals its center Zi/Zi−1. That
means G = Zi. (This proof doesn’t make sense for i = 0 and the result isn’t even true then:
take G to be nontrivial and cyclic.)
Remark 4.30. Since commutativity of G is equivalent to G/Z and [G, G] being trivial, we
ask: are the ﬁniteness of G/Z and [G, G] equivalent? Schur proved that if G/Z is ﬁnite then
[G, G] is ﬁnite [4, pp. 60–61] [16, pp. 43–44]. However, if [G, G] is ﬁnite then G/Z need not
be ﬁnite. (Examples are described on the ﬁrst page of [12] or in [16, p. 44].) Schur’s result
was generalized by Baer to higher terms in the upper and lower central series: if G/Zi is
ﬁnite then Li is ﬁnite (Schur’s theorem is the case i = 1). Hall [10] proved a converse of
Baer’s theorem: if Li is ﬁnite then G/Z2i (not G/Zi) is ﬁnite, and for each i he gave an

<!-- page 13 -->
SUBGROUP SERIES I
13
example where Li is ﬁnite and G/Zj is inﬁnite for each j < 2i. So some term of the lower
central series is ﬁnite if and only if some term of the upper central series has ﬁnite index,
but this need not ﬁrst occur at the same term in the two series.
The conditions Z = {e} and G = [G, G], as measures of extreme noncommutativity
of G, are not equivalent. For instance, the group Sn for n ≥3 has trivial center while
[Sn, Sn] = An. For prime p > 3, the group SL2(Z/(p)) has center {±I2} and the group is
equal to its commutator subgroup.
We did not deﬁne an “upper” counterpart to the derived series (bounding an abelian
series from above in the setting of Theorem 4.13). As an exercise, formulate what it should
mean for an ascending subgroup series (starting at G0 = {e}) to be abelian and explain
why there is no general construction of a subgroup series that will dominate every abelian
series from above.
5. Nilpotent and solvable groups: basic properties
Nilpotent and solvable groups are groups in which the upper/lower central series or
derived series are actually normal series, i.e., these subgroup series reach “the end”.
Deﬁnition 5.1. A group G is called nilpotent when it satisﬁes the following equivalent
conditions:
(1) G has a normal central series,
(2) Li = {e} for some i,
(3) Zi = G for some i.
The name “nilpotent” for this group property comes from an analogy with ring theory,
which can be explained for readers familiar with the connection between Lie groups and
Lie algebras. In a ring, an element with a power equal to 0 is called nilpotent. So in a Lie
algebra g, an element x could be called nilpotent if the linear operator y 7→[x, y] on g is
nilpotent in the sense of ring theory (some power of this operator is 0). A theorem of Engel
says all the elements of a Lie algebra are nilpotent if and only if the Lie group corresponding
to this Lie algebra has the properties in Deﬁnition 5.1, and thus this property on abstract
groups is called nilpotency.
By Theorem 4.27, the upper and lower central series of a nilpotent group are its shortest
central series. The least i such that Zi = G, or equivalently Li = {e}, is called the nilpotency
class of G. This is also the number of factors in the upper and lower central series. For
example, D2k has nilpotency class k for k ≥2. The only group of nilpotency class 0 is
the trivial group. Groups of nilpotency class 1 are nontrivial abelian groups. Groups of
nilpotency class 2 are nonabelian groups satisfying [G, G] ⊂Z (i.e., G/Z is nontrivial and
abelian).4 We could even deﬁne nilpotent groups recursively using the nilpotency class: the
trivial group has nilpotency class 0, and for n > 0 a group G has nilpotency class n when
G/Z(G) has nilpotency class n −1. Then the nilpotent groups are those having nilpotency
class n for some positive integer n.
Deﬁnition 5.2. A group G is called solvable when it satisﬁes the following equivalent
conditions:
(1) G has an abelian normal series,
4A theorem of Levi [17] says that G has nilpotency class at most 2 if and only if the commutator operation
x∗y := [x, y] is distributive over the group law (x∗(yz) = (x∗y)(x∗z)) and also if and only if the commutator
operation is associative.

<!-- page 14 -->
14
KEITH CONRAD
(2) G(i) is trivial for some i.
The term solvable comes from Galois theory, where it is shown that polynomials in Q[X]
whose roots can be described in terms of nested radicals are precisely those whose Galois
groups over Q are solvable groups in the above sense.
Speakers of British English use soluble instead of solvable.
Theorem 4.13 says the derived series of a solvable group is its shortest abelian normal
series. The least i such that G(i) is trivial, or equivalently the number of factors in the
derived series, is called the solvable length (or derived length) of the group. For n ≥3, Dn
has solvable length 2. The only group with solvable length 0 is the trivial group. Solvable
length 1 means the group is nontrivial and abelian. Solvable length 2 means the group
is nonabelian but its commutator subgroup is abelian. The collection of solvable groups
could be deﬁned recursively in terms of the solvable length: the trivial group has solvable
length 0, and for n > 0 a group G has solvable length ≤n when there is an abelian normal
subgroup A ◁G (not necessarily the center!) such that G/A has solvable length ≤n −1.
Theorem 5.3. All nilpotent groups are solvable.
Proof. A normal series that is central is abelian, so nilpotency implies solvability. Alterna-
tively, in terms of the special subgroup series we introduced, G(i) ⊂Li for all i (Theorem
4.13). If G is nilpotent then for large i the subgroup Li is trivial, so G(i) is trivial.
□
The converse of Theorem 5.3 is false: for odd n ≥3, Dn is solvable (D′′
n is trivial) but
not nilpotent (Li = ⟨r⟩for i ≥1).
Nilpotent
Solvable
abelian
S3, A4, S4
D2k
Dn
Heis(F)
Aﬀ(F)
Heis(Z/(n))
Aﬀ(Z/(n))
ﬁnite p-group
Table 3.
Table 3 lists some nilpotent and solvable groups. Our calculations of central and derived
series in Section 4 explain the ﬁrst three rows. In the third row, the group Heis(Z/(n))
is nilpotent since L1 = Heis(Z/(n))′ = Z(Heis(Z/(n))) so L2 = {I3}, or alternatively
Heis(Z/(n))/Z1 ∼= (Z/(n))2 is abelian so Z2 = Heis(Z/(n)).
The group Aﬀ(Z/(n)) is
solvable since {( 1 0
0 1 )} ◁{( 1 ∗
0 1 )} ◁{( ∗∗
0 1 )} is a normal series with abelian quotients Z/(n)
and (Z/(n))×. The reason ﬁnite p-groups (including D2k and Aﬀ(Z/(2k)), which are 2-
groups) are nilpotent is that nontrivial ﬁnite p-groups have nontrivial center, so the upper
central series has to keep growing until it reaches the whole group. (Here are the details.
Suppose |G| = pn > 1. Then Z1 is nontrivial. If some Zi is nontrivial and not equal to G
then G/Zi is a nontrivial ﬁnite p-group, so its center is nontrivial. Therefore Zi+1 is strictly
larger than Zi. This can’t continue indeﬁnitely, so some Zi equals G.)
The most important examples of nilpotent and solvable groups are groups of triangular
matrices (such as Heis(F) and Aﬀ(F)). They are treated in Appendix B.
The groups in the solvable column of Table 3 are not nilpotent except for Dn and
Aﬀ(Z/(n)) when n is a power of 2. This was shown for dihedral groups in Example 4.25 by

<!-- page 15 -->
SUBGROUP SERIES I
15
an explicit computation of upper and lower central series. Once we have some properties
of nilpotent groups under our belt, we will show in Example 5.8 that Aﬀ(Z/(n)) is not
nilpotent except when n is a power of 2.
Missing from Table 3 are some groups whose derived series we computed: Sn and An for
n ≥5 and GL2(F) and SL2(F) for |F| > 3 are not solvable, since S′
n = An and A′
n = An,
and GL2(F)′ = SL2(F) and SL2(F)′ = SL2(F). (The nonsolvability of Sn for n ≥5 is
responsible for the general polynomial of degree n over Q not being solvable in radicals.)
The smallest nonsolvable group is A5, of order 60, and every nonsolvable group of order 60
is isomorphic to A5.
We now proceed to churn through some tedious but basic properties of nilpotent and
solvable groups, e.g., relations to composition series and behavior under group constructions
like subgroups and quotient groups. The really interesting mathematical properties begin
with Theorem 5.15.
Theorem 5.4. For a group G, the following are equivalent:
(1) G is nilpotent,
(2) there is a series {e} = G0 ⊂G1 ⊂· · · ⊂Gr = G for some r such that [G, Gi+1] ⊂Gi
for all i,
(3) there is a series G = G0 ⊃G1 ⊃· · · ⊃Gr = {e} for some r such that [G, Gi] ⊂Gi+1
for all i.
For a group G, the following are equivalent:
(1) G is solvable,
(2) there is a series G = G0 ⊃G1 ⊃· · · ⊃Gr = {e} for some r such that [Gi, Gi] ⊂Gi+1
for all i.
Proof. Use Theorem 4.3.
□
Theorem 5.5. For a nontrivial group G, the following are equivalent:
(1) G is ﬁnite and solvable,
(2) G has a normal series with factors of prime order,
(3) G has a composition series with factors of prime order.
Proof. Easily (2) ⇒(1). To show (1) ⇒(2), assume G has an abelian normal series. Index
it as a descending series, say (1.2). If Gi/Gi+1 is a factor of (1.2) not of prime order, it has
a proper cyclic subgroup of prime order, say H/Gi+1. Then H lies strictly between Gi and
Gi+1 and Gi+1 ◁H ◁Gi (since Gi/Gi+1 is abelian). We therefore can add H to our normal
series and it remains an abelian series. Since we can nontrivially reﬁne the series as long as
it has a factor that is not of prime order, while at the same time a normal series for a ﬁnite
group can’t be nontrivially reﬁned indeﬁnitely, at some point we will reach an unreﬁnable
abelian normal series for G. Its factors must be of prime order.
Since a normal series with factors of prime order is a composition series, (2) and (3) are
obviously equivalent.
□
Example 5.6. The derived series for S4 is (2.1). The factors of this series are not all of
prime order, but (2.1) can be reﬁned to (2.2), whose factors are of order 2 or 3. Notice
– and this is crucial – the series (2.2) does not contain only normal subgroups of S4: the
subgroup U is normal in V but not in S4. Theorem 5.5 would not be true if we only allowed
normal series where each subgroup is normal in the whole group.

<!-- page 16 -->
16
KEITH CONRAD
In contrast to Theorem 5.5(3), there is no characterization of ﬁnite nilpotent groups in
terms of a composition series. For example, Z/(12) is nilpotent (all abelian groups are
nilpotent) while A4 is not nilpotent, but both groups have a composition series with two
cyclic factors of order 2 and one of order 3.
Nilpotency behaves well under standard constructions of new groups from old groups:
Theorem 5.7. Nilpotency is closed under subgroups, quotient groups, and direct products.
Proof. We will use the lower central series viewpoint.
If H ⊂G and N ◁G then by
induction Li(H) ⊂Li(G) and Li(G/N) = (NLi(G))/N for all i. For groups G and eG,
Li(G × eG) = Li(G) × Li( eG) for all i. Therefore if the lower central series of G and eG reach
the identity, so do the lower central series for every subgroup of G, quotient group of G,
and G × eG.
□
Example 5.8. We now show Aﬀ(Z/(n)) is not nilpotent if n is not a power of 2. For
odd n ≥3, Aﬀ(Z/(n)) is not nilpotent since its center is trivial.
When n is even and
not a power of 2, write n = 2km where m ≥3 is odd. Then reduction mod m gives a
natural map Z/(n) →Z/(m) that can be applied to matrix groups and gives us a natural
map Aﬀ(Z/(n)) →Aﬀ(Z/(m)). This reduction map on the aﬃne groups is onto (check!),
so Aﬀ(Z/(m)) is (isomorphic to) a quotient group of Aﬀ(Z/(n)). Since Aﬀ(Z/(m)) is not
nilpotent, neither can Aﬀ(Z/(n)) be nilpotent. (Similar reasoning shows Dn is not nilpotent
if n is not a power of 2: writing n = 2km with odd m ≥3, Dn/⟨r2k⟩∼= Dm is not nilpotent,
so Dn has a non-nilpotent quotient and therefore is not itself nilpotent.
Corollary 5.9. If H and K are normal subgroups of G such that G/H and G/K are
nilpotent then G/(H ∩K) is nilpotent.
Proof. The direct product G/H × G/K is nilpotent since G/H and G/K are nilpotent.
The diagonal map G →G/H × G/K has kernel H ∩K, so G/(H ∩K) is isomorphic to a
subgroup of a nilpotent group, and thus is nilpotent.
□
Remark 5.10. The same proof shows that if a property of groups is preserved by passage
to subgroups and direct products, then when H and K are normal subgroups of a group G
such that G/H and G/K have the property, then G/(H ∩K) has the property.
Solvability behaves well under group constructions, in fact slightly better than nilpotency:
Theorem 5.11. Solvability is closed under subgroups, quotient groups, and direct products.
Moreover, if N ◁G then G is solvable if and only if N and G/N are solvable.
Proof. We saw in examples in Section 3 that every subgroup, quotient group, and direct
product of groups that admit an abelian series also admit an abelian series. In particular,
if N ◁G then solvability of G implies solvability of N and G/N.
It remains to show that if N and G/N are solvable then so is G. We will do this in two
ways. First we argue in terms of abelian normal series. The groups N and G/N both admit
abelian normal series, say
{e} = H0 ◁H1 ◁· · · ◁Hr = N
and
{e} = G0/N ◁G1/N ◁· · · ◁Gs/N = G/N

<!-- page 17 -->
SUBGROUP SERIES I
17
where Hi+1/Hi is abelian and (Gj+1/N)/(Gj/N) is abelian for all i and j. The normal
series for G/N lifts to a normal series from N to G:
N = G0 ◁G1 ◁· · · ◁Gs = G,
and the factors here are isomorphic termwise to those in the series for G/N. Therefore
these factors are all abelian. Tacking the abelian normal series for N onto the start, we get
{e} = H0 ◁H1 ◁· · · ◁Hr = N = G0 ◁G1 ◁· · · ◁Gs = G,
which has abelian factors (either Hi+1/Hi or Gj+1/Gj).
Next we argue in terms of the derived series eventually reaching the trivial subgroup.
Since G/N is solvable, its derived subgroups (G/N)(i) eventually become trivial.
It’s
straightforward to check by induction that (G/N)(i) = (NG(i))/N, so solvability of G/N
implies that for large i, NG(i) = N. Thus G(i) ⊂N. Since N is solvable, N(j) is trivial
for large j, so (G(i))(j) is trivial for large i and j. Since (G(i))(j) = G(i+j), some derived
subgroup of G is eventually trivial, so we obtain solvability of G.
□
Remark 5.12. That solvability of N and G/N implies solvability of G gives a conceptual
role for the class of all solvable groups: it is the smallest class of groups C containing the
abelian groups and having the quotient-lifting property: if N ◁G and N and G/N are in
C then G is in C.
Corollary 5.13. Let H and K be normal subgroups of the group G.
(1) If G/H and G/K are solvable then G/(H ∩K) is solvable.
(2) If H and K are solvable then so is HK.
Proof. Part (1) follows by the same reasoning as in the proof of Corollary 5.9, or see Remark
5.10. For (2), since H is solvable and HK/H ∼= K/(H ∩K) is solvable, HK is solvable by
Theorem 5.11.
□
We only need one of H or K to be normal in G for (2) to work: the proof only used
normality of H, not K.
By Corollary 5.13 every ﬁnite group has a unique maximal solvable normal subgroup,
which contains all other solvable normal subgroups. The maximal solvable normal subgroup
of G is called the (solvable) radical of G and is denoted R(G). To say a group has trivial
radical means there are no nontrivial solvable normal subgroups, or equivalently (since the
second to last subgroup in the derived series has to be an abelian subgroup) there are no
nontrivial abelian normal subgroups. A group with trivial radical must have a trivial center
(since the center is an abelian normal subgroup), and an example of such a group is Sn for
n ≥5, as well as all nonabelian simple groups. As an exercise using the quotient-lifting
property of solvability, show G/R(G) has trivial radical. We won’t discuss the solvable
radical further, but a construction similar to it (Borel subgroups) is important in the study
of linear algebraic groups.
Comparing Corollaries 5.9 and 5.13, it is natural to ask if the nilpotent analogue of
Corollary 5.13(2) is true: when H and K are nilpotent normal subgroups in G, is HK also
nilpotent? Yes (theorem of H. Fitting), but it can’t be proved as we did for the solvable
case because nilpotency of N and G/N doesn’t generally imply nilpotency of G. (Consider
G = Dn and N = ⟨r⟩with n ≥3 odd.)
The next result gives a setting where nilpotency of N and G/N implies nilpotency of G.

<!-- page 18 -->
18
KEITH CONRAD
Theorem 5.14. Let G be a group and N be a normal subgroup of G with N ⊂Zi for some
i, where Zi is a member of the upper central series for G. If G/N is nilpotent then G is
nilpotent.
Proof. Since G/Zi is a quotient group of G/N, G/Zi is nilpotent. Since Zi ⊂Zi+1 ⊂Zi+2 ⊂
· · · ⊂G,
Zi/Zi ⊂Zi+1/Zi ⊂Zi+2/Zi ⊂· · · ⊂G/Zi.
This is the upper central series for G/Zi (check!).
If G/Zi is nilpotent we must have
Zj/Zi = G/Zi for some j ≥i, so Zj = G for some j. Thus G is nilpotent.
□
This proof did not explicitly assume or use the nilpotence of N, but its nilpotence is
automatic since every Zi is nilpotent and we assumed N ⊂Zi for some i. There is a result
of Philip Hall in the spirit of Theorem 5.14 that looks close to a quotient-lifting property:
if N and G/N′ are nilpotent then G is nilpotent. (Notice we use G/N′ and not G/N.)
We turn now to interesting structural properties of nilpotent and solvable groups.
Nilpotent groups include ﬁnite p-groups, and the next theorem shows some properties of
ﬁnite p-groups generalize to all nilpotent groups (including inﬁnite nilpotent groups).
Theorem 5.15. If G is a nontrivial nilpotent group then
(1) for every nontrivial normal subgroup N ◁G, N ∩Z(G) ̸= {e} and [G, N] ̸= N,
(2) for every proper subgroup H, H ̸= N(H).
In particular, a nontrivial nilpotent group has nontrivial center and its commutator sub-
group is a proper subgroup.
Proof. (1): We have Zi = G for some i ≥1. Therefore N ∩Zi is nontrivial for some i. Pick
i minimal, so i ≥1. Since [G, Zi] ⊂Zi−1, we have [G, N ∩Zi] ⊂N ∩Zi−1. By minimality of
i, N ∩Zi−1 is trivial, so [G, N ∩Zi] is trivial. Thus N ∩Zi ⊂Z(G) = Z1, so N ∩Zi ⊂N ∩Z1.
The reverse inclusion is clear, so N ∩Z1 = N ∩Zi ̸= {e}.
To prove [G, N] ̸= N, assume [G, N] = N. Then N ⊂[G, G] = L1, so N = [G, N] ⊂
[G, L1] = L2. By induction, N ⊂Li for all i, and taking i large enough implies N is trivial,
a contradiction.
Taking N = G in (1) recovers the special case mentioned at the end of the theorem.
(2): Since Z0 = {e} and Zi = G for some i, there is some i such that Zi ⊂H. Then
[H, Zi+1] ⊂[G, Zi+1] ⊂Zi ⊂H, so Zi+1 ⊂N(H). Picking i maximal such that Zi ⊂H, the
fact that Zi+1 ̸⊂H implies H ̸= N(H).
□
Corollary 5.16. If G is a nilpotent group and H is a subgroup of G with ﬁnite index n,
then gn ∈H for all g ∈G.
Proof. If H were a normal subgroup of G, this result would be immediate from the fact
that G/H is a group of order n. Although H need not be normal, we can use the nilpotent
condition on G to create a normal series
H = H0 ◁H1 ◁H2 ◁· · · ◁Hr = G
leading from H to G: set H1 = N(H), H2 = N(N(H)) = N(H1), and Hi+1 = N(Hi). Then
Hi ◁Hi+1 since every subgroup is normal in its normalizer, and Theorem 5.15(2) says Hi+1
properly contains Hi if Hi ̸= G. Since [G : H] is ﬁnite, the Hi’s can’t increase forever, so
Hr = G for r ≫0.
For g ∈G, write gn = g[G:H] in the form
g[G:H] = ((g[Hr:Hr−1])[Hr−1:Hr−2])···[H1:H0].

<!-- page 19 -->
SUBGROUP SERIES I
19
By normality of the subgroups, the successive powers on the right are in Hr−1, Hr−2, . . . ,
and ﬁnally in H0 = H.
□
This corollary is false for the non-nilpotent group S3 with H = {(1), (12)}. The index is
3 and (13)3 = (13) ̸∈H.
Remark 5.17. Call a positive integer n a nilpotent number if all groups of order n are
nilpotent. Call n a nontrivial center number if all groups of order n have nontrivial center.
Since a nontrivial nilpotent group has nontrivial center, every nilpotent number is a non-
trivial center number, but the converse is false. The ﬁrst counterexample is at 28: all groups
of order 28 have nontrivial center, but D14 is a group of order 28 that is not nilpotent.
We will see in Theorem 5.31 that Theorem 5.15(2) fails for all non-nilpotent solvable
groups: there is a proper subgroup H such that N(H) = H.
Nilpotent groups include abelian groups, and the next theorem is easy to check for abelian
groups but remains true for all nilpotent groups.
Theorem 5.18. If G is a nilpotent group then
(1) the elements of ﬁnite order in G are a subgroup,
(2) if H and K are subgroups of G and [G : H] is ﬁnite then [K : H ∩K] is ﬁnite and
[K : H ∩K] | [G : H].
Proof. For (1), see [15, pp. 111–112]. For (2), which is a consequence of Theorem 5.15(2),
see [11, p. 7].
□
For the second part of Theorem 5.18 in general groups, [K : H ∩K] ≤[G : H] but
divisibility may not occur.
Theorem 5.19. If G is a nontrivial solvable group then every nontrivial normal subgroup
of G contains a nontrivial abelian normal subgroup of G. In particular, if G is a nontrivial
solvable group of nonprime size then G contains a nontrivial proper normal subgroup.
This is a solvable analogue of Theorem 5.15(1); in the nilpotent case we can just intersect
the normal subgroup with the center of G. This method doesn’t work in the solvable case
since solvable groups can have trivial center (such as A4 and S4).
Proof. Let N ◁G with N nontrivial. Since N is solvable, N(i) = {e} for some i. Take
i minimal, so i ≥1. Then N(i−1) is nontrivial and (N(i−1))′ = N(i) = {e}, so N(i−1) is
abelian. It is normal in G since all members of the derived series of N are normal in G
(when H is normal in G, so is [H, H]).
To show G contains a nontrivial proper normal subgroup, run through the above argument
with N = G to obtain a nontrivial abelian normal subgroup of G, namely the last nontrivial
term in the derived series is an abelian normal subgroup of G, and it is a proper subgroup
if G is nonabelian. If G is abelian then we can use a nontrivial proper normal subgroup;
such a subgroup exists unless |G| is prime.
□
Theorem 5.20. For a nontrivial ﬁnite group G,
• G is solvable if and only if every nontrivial quotient of G has a nontrivial abelian
normal subgroup,
• G is nilpotent if and only if every nontrivial quotient of G has a nontrivial center.

<!-- page 20 -->
20
KEITH CONRAD
Proof. Since quotients of solvable groups are solvable and quotients of nilpotent groups are
nilpotent, the “only if” directions follow from nontrivial solvable groups having nontrivial
abelian normal subgroups and nontrivial nilpotent groups having nontrivial centers (and
the ﬁniteness of G is irrelevant).
We turn to the converse results. Suppose every nontrivial quotient of G has a nontrivial
abelian normal subgroup. Then G itself has a nontrivial abelian normal subgroup, say G1.
If G/G1 is abelian then G is solvable by the quotient-lifting property. If G/G1 is nonabelian
then G/G1 is at least nontrivial and then has a nontrivial abelian normal subgroup, which
has the form G2/G1, so G2 ̸= G1 and G2 ◁G. Now we have the normal series {e} ◁G1 ◁
G2 ◁G where the ﬁrst and second factors are abelian. If G/G2 is abelian then G is solvable.
If G/G2 is nonabelian then it has a nontrivial abelian normal subgroup G3/G2 and we
can reﬁne the normal series by inserting G3. Continuing this procedure eventually leads to
Gi = G for i ≫0 and the Gi’s are an abelian normal series of G, so G is solvable.
Now suppose every nontrivial quotient of G has a nontrivial center.
Then G has a
nontrivial center Z1. If Z1 = G then G is abelian and thus nilpotent. If Z1 ̸= G then G/Z1
is a nontrivial quotient of G so it has a nontrivial center, which is exactly Z2/Z1. As long
as Zi ̸= G the quotient G/Zi has a nontrivial center so Zi+1 ̸= Zi. Since G is ﬁnite we
eventually must have Zi = G for i ≫0, so G is nilpotent.
□
Our next theorem characterizes ﬁnite nilpotent groups very concretely.
Theorem 5.21. A ﬁnite group is nilpotent if and only if all of its Sylow subgroups are
normal, or equivalently the group is isomorphic to the direct product of its Sylow subgroups.
Proof. Suppose G is a ﬁnite nilpotent group. Let P be a Sylow subgroup. To show P ◁G
we will show the normalizer N(P) is G. From Sylow theory, N(N(P)) = N(P). No proper
subgroup of a nilpotent group equals its normalizer, so we must have N(P) = G. Conversely,
suppose all the Sylow subgroups of G are normal. Then G is isomorphic to a direct product
of its Sylow subgroups, by the Sylow theorems. The Sylow subgroups are ﬁnite p-groups,
hence they are nilpotent, so their direct product is nilpotent too.
□
The thrust of Theorem 5.21 is that a ﬁnite group is nilpotent if and only if it is a direct
product of p-groups (for varying primes p). So there is a special method of proving a ﬁnite
group is nilpotent: show all of its Sylow subgroups are normal.
Theorem 5.21 leads to a number of characterizations of nilpotency of ﬁnite groups. One of
the characterizations involves subnormal subgroups. A subnormal subgroup of a group is a
normal subgroup of a normal subgroup of . . . of a normal subgroup of the group. Essentially,
subnormality is the “transitive extension” of the relation of being a normal subgroup. In
particular, every subnormal proper subgroup is normal in some larger subgroup, so H ̸=
N(H) when H is subnormal.
Theorem 5.22. For a nontrivial ﬁnite group G, the following are equivalent to nilpotency:
(1) for every proper subgroup H, H ̸= N(H),
(2) every subgroup of G is subnormal,
(3) every nontrivial quotient group of G has a nontrivial center,
(4) elements of relatively prime order in G commute,
(5) if d | |G| then there is a normal subgroup of size d.
Proof. To show most of these properties imply nilpotency when G is ﬁnite, we will show
most of these properties, for a ﬁnite group, imply the Sylow subgroups are normal.

<!-- page 21 -->
SUBGROUP SERIES I
21
We saw nilpotency implies (1) in Theorem 5.15. Now assume (1) is true. Let P be a
Sylow subgroup of G. From the Sylow theorems, N(N(P)) = N(P), so N(P) is its own
normalizer. Therefore N(P) = G by (1), so P ◁G. Thus all the Sylow subgroups of G are
normal, so G is nilpotent.
If G is nilpotent and H is a proper subgroup with Zi ⊂H then Zi+1 ⊂N(H). (We
showed this in the proof of Theorem 5.15(2).)
Repeating this enough times shows an
iterated normalizer of H eventually equals G, so H is subnormal. Conversely, if (2) is true
then H ̸= N(H) for every proper subgroup H, so G is nilpotent by (1).
Since nilpotency of G implies nilpotency of every quotient, (3) is immediate. Conversely,
if (3) is true then G/Zi has a nontrivial center when Zi ̸= G. Therefore Zi+1 ̸= Zi when
Zi ̸= G. This can’t continue indeﬁnitely, so some Zi equals G.
If (4) is true let P1, . . . , Pm be a set of nontrivial Sylow subgroups of G for the diﬀerent
primes dividing |G|.
Elements in Pi and Pj commute when i ̸= j, by (4), so the map
P1 × · · · × Pm →G given by (x1, . . . , xm) 7→x1 · · · xm is a homomorphism between groups
of equal size. Since the xi’s commute and have relatively prime order, they multiply to the
identity only when each xi is trivial, so this map is injective and thus is an isomorphism.
This implies G is a direct product of ﬁnite p-groups, so it is nilpotent.
Conversely, to
see that in a ﬁnite nilpotent group (4) is true, write G as a direct product of its Sylow
subgroups. In this product decomposition, two elements in G with relatively prime order
don’t have a nontrivial component in a common p-Sylow coordinate, so they commute.
To show (5) is equivalent to nilpotency for ﬁnite groups, ﬁrst recall (5) is true for ﬁnite
p-groups (see Corollary 6.13 in https://kconrad.math.uconn.edu/blurbs/grouptheory/
conjclass.pdf). Next, in a direct product of p-groups for diﬀerent p, say P1 × · · · × Pm
where |Pi| = pei
i , to construct a normal subgroup with size d write d = pf1
1 · · · pfm
m and use
H1 × · · · × Hm where Hi is normal of size pfi
i in Pi. Conversely, if (5) is true then letting d
be the maximal power of a prime dividing |G| shows the Sylow subgroups are normal.
□
Remark 5.23. The analogue of Theorem 5.22(3) for subgroups (a ﬁnite group is nilpotent
if and only if all of its nontrivial subgroups have nontrivial center) is false: the nonabelian
semidirect product Z/(3)⋊Z/(4) is not nilpotent (it has more than one 2-Sylow subgroup),
but its proper subgroups are all cyclic and thus have nontrivial center. The properties in
Theorem 5.22 are not equivalent to nilpotency when G is inﬁnite. For example, there are
inﬁnite groups with trivial center (hence not nilpotent) in which every proper subgroup H
has H ̸= N(H). See [13].
The following interesting theorem of Philip Hall extends the Sylow theorems in solvable
groups.
Theorem 5.24 (P. Hall, 1928). Let G be a ﬁnite solvable group and d be a divisor of |G|
such that (d, |G|/d) = 1. Then
(1) there exists a subgroup of G with size d,
(2) all subgroups of G with size d are conjugate,
(3) if d′ | d then each subgroup of G with size d′ is inside a subgroup of G with size d.
Proof. See [15, pp. 140–141].
□
There is an extra part of Hall’s theorem that generalizes the congruence np ≡1 mod p
from Sylow theory. For that, see [9, Sect. 9.3].
For a prime p, writing the size of a group as pkm with p not dividing m, subgroups of
index pk are called p-Sylow complements (or just Sylow complements if p is understood). If

<!-- page 22 -->
22
KEITH CONRAD
P is a p-Sylow subgroup and H is a p-Sylow complement then P ∩H is trivial and the set
PH coincides with the whole group. This justiﬁes the label “complement.”
Several years after proving Theorem 5.24, Hall discovered that the only ﬁnite groups that
satisfy all the conclusions of his theorem are solvable. In fact, the existence of complements
to Sylow subgroups is suﬃcient:
Theorem 5.25 (Hall, 1937). A ﬁnite group is solvable if and only if every Sylow subgroup
has a complement.
Proof. See [6, pp. 890–892].
□
Corollary 5.26. If a ﬁnite group satisﬁes the converse of Lagrange’s theorem (that is, there
is a subgroup of every size dividing the size of the group), then it is solvable.
Proof. Such a group contains p-Sylow complements for every prime p dividing the size, so
the group is solvable by Theorem 5.25.
□
A group satisfying the converse of Lagrange’s theorem is called Lagrangian. Every nilpo-
tent group is Lagrangian by Theorem 5.22(5), and the Lagrangian groups lie strictly between
the nilpotent and solvable ﬁnite groups: S4 is Lagrangian but not nilpotent, and A4 is solv-
able but not Lagrangian. Since S4 and A4 ×Z/(2) are both Lagrangian while A4 is not, the
Lagrangian property is not closed under passage to subgroups or quotient groups. Let’s be
frank: the Lagrangian property has no real signiﬁcance in group theory.
In Theorem 5.25, we do not insist the complement to the Sylow subgroup is normal.
In fact, asking for Sylow complements to be normal (and not just to exist) provides a
characterization of (ﬁnite) nilpotent groups and thus provides a nice parallel description of
solvability and nilpotency for ﬁnite groups:
Theorem 5.27. A ﬁnite group is nilpotent if and only if every Sylow subgroup has a normal
complement.
Proof. Exercise.
□
Returning to Theorem 5.25, although we don’t discuss the proof it is worth recording
that its ﬁrst nontrivial step is Burnside’s famous paqb-theorem:
Theorem 5.28 (Burnside, 1904). If |G| = paqb for primes p and q, then G is solvable.
Proof. See [6, pp. 886–890] for Burnside’s original proof, by representation theory. A purely
group-theoretic proof of the theorem was found in the early 1970s [20, pp. 216–222].
□
The conclusion of the paqb-theorem is generally false when |G| has three prime factors,
e.g., A5 and S5 are not solvable and |A5| = 60 = 22 · 3 · 5 and |S5| = 120 = 23 · 3 · 5.
By the Sylow theorems, a group G of order paqb has subgroups P and Q of orders pa and
qb. Then P ∩Q is trivial, so G = PQ by counting. With this in mind, here is a generalization
of Burnside’s paqb theorem using nilpotent subgroups in place of prime-power subgroups.
Theorem 5.29. If G is a ﬁnite group and G = MN where M and N are nilpotent, then
G is solvable. More generally, a ﬁnite group G is solvable if and only if there are nilpotent
subgroups N1, N2, . . . , Nr such that G = N1N2 · · · Nr with NiNj = NjNi for all i and j.
A proof of this theorem is technical and is omitted. When G is solvable, a nilpotent
decomposition can be achieved using some of its Sylow subgroups, one for each prime
dividing |G|. (Not all choices of Sylow subgroups will work since the commuting condition

<!-- page 23 -->
SUBGROUP SERIES I
23
NiNj = NjNi may not hold for all the Sylow subgroups.) This was shown by Hall in 1937
and it generalizes the Sylow subgroup direct product decomposition for ﬁnite nilpotent
groups. To prove, conversely, that a ﬁnite group admitting a decomposition into setwise
commuting nilpotent subgroups is solvable uses Theorem 5.25 as a solvability criterion: the
group is shown to have a Sylow complement for every prime. This converse direction was
proved partially by Wielandt (1958) and in full by Kegel (1961), so Theorem 5.29 is called
the Kegel-Wielandt theorem.
The next theorem is the deepest result about solvability of ﬁnite groups and illustrates
the special role of the prime 2 in ﬁnite group theory.
Theorem 5.30 (Feit–Thompson, 1963). If |G| is odd, then G is solvable.
Proof. See [8]. The proof is 255 pages long and occupies an entire volume of the Paciﬁc
Journal of Mathematics.
□
Since a nontrivial solvable group not of prime order contains a nontrivial proper normal
subgroup (Theorem 5.19), all nonabelian ﬁnite simple groups have even order by the Feit–
Thompson theorem. In particular, all nonabelian ﬁnite simple groups contain an element
of order 2. This is the ﬁrst step in the classiﬁcation of the ﬁnite simple groups.
The classiﬁcation of ﬁnite simple groups can be used to provide further characterizations
of nilpotent and solvable ﬁnite groups:
• G is nilpotent if and only if N(P) is nilpotent for all Sylow subgroups P of G [3].
(After the fact, we must have P ◁G since G is nilpotent, so in fact N(P) = G for
all Sylow subgroups.)
• G is solvable if and only if its 2-Sylow and 3-Sylow subgroups have complements [1].
(Thus we only need to check the primes p = 2 and p = 3 in Theorem 5.25 to know
a group is solvable.)
In addition to Hall’s theorem about the existence and conjugacy of certain subgroups
in solvable groups, there is another theorem of Carter [5] about conjugate subgroups in
solvable groups:
Theorem 5.31 (Carter, 1961). Every ﬁnite solvable group contains a nilpotent subgroup
H such that N(H) = H, and all such subgroups are conjugate.
Proof. See [15, pp. 142–143].
□
The subgroups described in this theorem (self-normalizing and nilpotent) are called
Carter subgroups. The Carter subgroups of S3, S4, and Dn are the 2-Sylow subgroups.
While Carter subgroups always exist in ﬁnite solvable groups, they might not exist in a
nonsolvable group (there are no Carter subgroups in A5). However, whenever group theo-
rists found more than one Carter subgroup in a nonsolvable group these subgroups always
turned out to be conjugate. So the conjecture arose that the Carter subgroups of a ﬁ-
nite group are conjugate when they exist. This is true, and its proof [21] depends on the
classiﬁcation of ﬁnite simple groups.
Appendix A. Proof of the Jordan–H¨older theorem
We return to the Jordan–H¨older theorem from Section 2. Recall its statement: if G is a
nontrivial group and
(A.1)
{e} = G0 ◁G1 ◁G2 ◁· · · ◁Gr = G

<!-- page 24 -->
24
KEITH CONRAD
and
(A.2)
{e} = eG0 ◁eG1 ◁eG2 ◁· · · ◁eGs = G
are both composition series for G (that means the factors in both series are simple groups)
then r = s and there is π ∈Sr such that eGi/ eGi−1 ∼= Gπ(i)/Gπ(i)−1 for 1 ≤i ≤r. To prove
the Jordan–H¨older theorem, the bulk of the work is contained in the following basic result,
called the Schreier reﬁnement theorem. It was proved by Schreier in 1928, nearly 40 years
after Jordan proved the Jordan–H¨older theorem.
Theorem A.1 (Schreier). For two normal series of a group, intermediate subgroups can
be inserted to yield two new normal series for the group whose factor groups coincide up to
isomorphism, counting multiplicity.
Proof. This is a nice application of the ideas in Theorems 3.1 and 3.5.
We follow an
argument from [2].
Starting with (A.1), taking the intersection of each subgroup with eGj+1 produces (by
Theorem 3.1) the normal series
{e} ◁eGj+1 ∩G1 ◁eGj+1 ∩G2 ◁· · · ◁eGj+1 ∩Gr = eGj+1
for eGj+1. Since eGj ◁eGj+1, we can multiply each subgroup in this new normal series by eGj
to get an analogue of (3.2):
eGj ◁eGj( eGj+1 ∩G1) ◁eGj( eGj+1 ∩G2) ◁· · · ◁eGj( eGj+1 ∩Gr) = eGj+1.
This is a chain of subgroups between eGj and eGj+1 with each subgroup normal in the next
one. In this series, there are r factors. (Some factors might be trivial.) Linking these series
together over j = 0, 1, . . . , s −1 produces a normal series for G with rs factors of the form
(A.3)
eGj( eGj+1 ∩Gi+1)/ eGj( eGj+1 ∩Gi)
as i and j vary from 0 to r −1 and 0 to s −1, respectively.
In the same way, intersecting the series (A.2) with Gi+1 and then multiplying the result
by Gi (which is normal in Gi+1) gives a series of subgroups between Gi and Gi+1 that string
together over all i to a normal series of G with sr = rs factors of the form
(A.4)
Gi(Gi+1 ∩eGj+1)/Gi(Gi+1 ∩eGj)
as i and j vary.
The two reﬁnements we have made to (A.1) and (A.2) each have rs factors, and we will
show the quotient groups in (A.3) and (A.4) for the same i and j are isomorphic. These
quotient groups both have the form HJ/HK where the J in both quotients is the same
(J = eGj+1 ∩Gi+1), while the H’s and K’s in the two quotients are not (usually) the same.
We do have K ⊂J both times, since Gi ⊂Gi+1 and eGj ⊂eGj+1.
To prove (A.3) and (A.4) are isomorphic, we want to simplify a group of the form HJ/HK
by cancelling the H’s, assuming K ⊂J (as in our application of interest). This should leave
us with a certain quotient group of J (recall J in (A.3) and (A.4) are the same). To make
this explicit, look at the natural map f : J →HJ/HK. This is onto (since H ⊂HK). If
x ∈J is in the kernel then x = hk for some h ∈H and k ∈K, so h = xk−1 ∈J (because
K ⊂J), so h ∈H ∩J. Therefore the kernel of f is inside (H ∩J)K. Also (H ∩J)K dies
under f since it is inside of HK, so ker f = (H ∩J)K. That means J/(H ∩J)K ∼= HJ/HK,
so we have expressed HJ/HK as a quotient of J, at least up to isomorphism. In (A.3) and

<!-- page 25 -->
SUBGROUP SERIES I
25
(A.4), the H ∩J in one quotient equals the K in the other. That is, the quotient groups in
(A.3) and (A.4) are both isomorphic to
(Gi+1 ∩eGj+1)/(Gi ∩eGj+1)(Gi+1 ∩eGj),
and thus they are isomorphic to each other.
□
The proof of the Jordan–H¨older theorem is now easy.
Proof. If a group admits two composition series then Schreier’s reﬁnement theorem says
they can be reﬁned to two normal series whose factor groups coincide up to isomorphism,
counting multiplicity. The key feature of a composition series is that it can only be reﬁned
in a trivial way, i.e., by repeating some of the subgroups already in the series. Therefore the
factors in a composition series of a group are the nontrivial factors in all of the reﬁnements
of the composition series. That shows two composition series of a group have the same
(nontrivial) factors up to isomorphism, counting multiplicity.
□
One other use of the Schreier reﬁnement theorem is that it shows if a group admits
at least one composition series then every normal series for the group can be reﬁned to a
composition series. Indeed, start with a normal series and a composition series for the group
and reﬁne them by the Schreier reﬁnement theorem to normal series for the group whose
factor groups coincide up to isomorphism, counting multiplicity. Then the reﬁnement of
the original normal series will be a composition series after all repeated subgroups in its
reﬁnement are replaced with one copy of that subgroup.
Let’s put the Jordan–H¨older theorem to work.
Corollary A.2. Suppose f is a function deﬁned on ﬁnite simple groups, with values in Z,
which has the same value on isomorphic simple groups. There is exactly one way to extend
f to a function on all ﬁnite groups satisfying the following two properties:
(a) f takes the same value on isomorphic groups,
(b) f(G) = f(N) + f(G/N) whenever N ◁G.
Explicitly, f(e) = 0 and when G is nontrivial with composition series (A.1),
(A.5)
f(G) =
r−1
X
i=0
f(Gi+1/Gi).
Proof. First we assume f exists satisfying (a) and (b), and show it must be given by (A.5)
on nontrivial groups. Then we show (A.5) (along with f(e) = 0) satisﬁes (a) and (b).
When G is trivial, let N = G. Then f(G) = f(N) = f(G/N) by (a), so f(G) = 0 by (b).
When G is nontrivial, let (A.1) be a composition series for G. If r ≥1, then since Gr−1◁G
we have f(G) = f(Gr−1)+f(G/Gr−1) by (b). The series (A.1) with the top group removed
is a composition series for Gr−1, so by induction on the length of a composition series,
f(Gr−1) = Pr−1
i=0 f(Gi+1/Gi) (the sum is empty if r = 1). Adding f(G/Gr−1) to both sides
recovers the formula (A.5) for G.
Conversely, we now deﬁne f to be 0 on trivial groups and to have the value (A.5) on
nontrivial ﬁnite groups G. We want to show (a) and (b) are satisﬁed. First, however, we
need to check (A.5) is well-deﬁned. What if we change the composition series for G? By
the Jordan–H¨older theorem, the set of simple factors in the two series are the same up to
isomorphism and multiplicity. Therefore the sum in (A.5) is the same for all choices of
composition series of G, so (A.5) is well-deﬁned.

<!-- page 26 -->
26
KEITH CONRAD
Part (a) is now immediate: forming composition series for two isomorphic ﬁnite groups,
we can use the isomorphism to transfer the composition series for one group over to the
other group, leaving us with two composition series on the same group, and they yield the
same value for (A.5) by Jordan–H¨older.
To check (b), we build a composition series in a convenient way. Since (b) is clear if N
is trivial or if N = G, we may assume N is neither {e} nor G. Make a composition series
for G/N, lift it up to G to get a normal series from N to G with simple factors, and then
tack on a composition series for N. The result is a composition series for G containing N as
one term, with the (simple) factors from G down to N having the same (simple) factors up
to isomorphism and multiplicity as the chosen composition series of G/N. Applying (A.5),
the part of the sum using simple factors from subgroups of N equals f(N) and the rest of
the sum equals f(G/N).
□
In this proof, we really didn’t need the values of f to lie in Z. They could lie in an abelian
group and the proof goes through.
Appendix B. Matrix Groups
Normal series for matrix groups are important. For a ﬁeld F, the standard normal series
for GLn(F), when n ≥2 (the case n = 1 is not interesting) is
{In} ◁SLn(F) ◁GLn(F),
The center of SLn(F) is µn(F)In (scalar diagonal matrices with an n-th root of unity from
F on the diagonal), so we can reﬁne the above series to
{In} ◁µn(F)In ◁SLn(F) ◁GLn(F).
The ﬁrst and last quotients are abelian, while SLn(F)/µn(F)In = PSLn(F) is usually not
abelian. This is usually not a composition series, e.g., µn(F) is cyclic and thus can be
decomposed further if it is not of prime order.
It can be shown that [SLn(F), SLn(F)] = SLn(F) except when n = 2 and |F| ≤3, so for
n > 2 or |F| > 3 the derived series of SLn(F) never gets lower than the full group. Thus
SLn(F) is not solvable, so GLn(F) is also not solvable. If n = 2 and |F| ≤3 then GL2(F)
is solvable, so SL2(F) is solvable too. Neither of these groups is nilpotent.
Nilpotent and solvable matrix groups naturally occur among triangular matrices. For
n ≥2, let Tn(F) be the group of invertible upper triangular matrices in GLn(F):









∗
∗
∗
· · ·
∗
∗
0
∗
∗
· · ·
∗
∗
0
0
∗
· · ·
∗
∗
...
...
...
...
...
...
0
0
0
· · ·
∗
∗
0
0
0
· · ·
0
∗









(Although this makes sense when n = 1, with T1(F) = F ×, this case is boring for our
purposes so we don’t pay attention to it.) It is useful to view Tn(F) as the stabilizer of the
standard subspace ﬁltration of F n = Fe1 ⊕Fe2 ⊕· · · ⊕Fen. Speciﬁcally, let V0 = {0} and
Vk = Fe1 ⊕· · · ⊕Fek for k = 1, . . . , n. Then F n can be ﬁlled up by the Vk’s:
{0} = V0 ⊂V1 ⊂V2 ⊂· · · ⊂Vn = F n.

<!-- page 27 -->
SUBGROUP SERIES I
27
A matrix g ∈Mn(F) is in Tn(F) if and only if g(Vk) = Vk for all k. (Having g(Vk) ⊂Vk
for all k is equivalent to g being upper-triangular, while the more precise g(Vk) = Vk for all
k forces each diagonal entry to be nonzero, hence the matrix is invertible.) The condition
“g(Vk) = Vk for all k” is closed under multiplication and inversion on g, which is the
non-tedious way to show Tn(F) is a group.
We now introduce a normal series for Tn(F). Each g ∈Tn(F) deﬁnes a linear map on
the quotient spaces Vℓ/Vk for ℓ> k. For i = 1, . . . , n, set
UTi
n(F) = {g ∈Tn(F) : g|Vk+i/Vk = id . for 0 ≤k ≤n −i}
= {g ∈Tn(F) : g|Vi = idVi, g(ej) −ej ∈Vj−i for j > i}.
(The label UT stands for unipotent-triangular.) Thus UTn(F) := UT1
n(F) is the subgroup
consisting of matrices in Tn(F) with 1’s along the main diagonal:
(B.1)









1
∗
∗
· · ·
∗
∗
0
1
∗
· · ·
∗
∗
0
0
1
· · ·
∗
∗
...
...
...
...
...
...
0
0
0
· · ·
1
∗
0
0
0
· · ·
0
1









.
For instance, UT3(F) = Heis(F). We will see that Tn(F) is solvable and its subgroup
UTn(F) is nilpotent. These are the most important examples of solvable and nilpotent
groups in mathematics.
The matrices in UT2
n(F) have 1’s along the main diagonal and 0’s along the superdiagonal:









1
0
∗
· · ·
∗
∗
0
1
0
· · ·
∗
∗
0
0
1
· · ·
∗
∗
...
...
...
...
...
...
0
0
0
· · ·
1
0
0
0
0
· · ·
0
1









.
Notice the matrices in UT2
n(F) have 2 × 2 identity matrices down the main diagonal. More
generally, UTi
n(F) for 1 ≤i ≤n consists of matrices in Tn(F) with i × i identity matrices
down the main diagonal and arbitrary entries above them. (In terms of matrix entries,
these matrices have 1’s along the main diagonal and 0’s in the ﬁrst i −1 upper diagonals
that are parallel to and above the main diagonal.)
We have the subgroup series
(B.2)
Tn(F) ⊃UTn(F) ⊃UT2
n(F) ⊃· · · ⊃UTn
n(F) = {In}.
This is a normal series, since UTn(F) is the kernel of the homomorphism Tn(F) →(F ×)n
that projects upper-triangular matrices onto their sequence of diagonal entries and, for
i ≥1, UTi+1
n
(F) is the kernel of the map UTi
n(F) →F n−i that projects onto the ith upper
diagonal (the ﬁrst upper diagonal that is not automatically 0 in UTi
n(F)). The factors of
(B.2) are
(B.3)
Tn(F)/ UTn(F) ∼= (F ×)n,
UTi
n(F)/ UTi+1
n
(F) ∼= F n−i

<!-- page 28 -->
28
KEITH CONRAD
for i = 1, . . . , n−1. These are abelian, so Tn(F) is a solvable group. In terms of the derived
series for G = Tn(F), when F ̸= Z/(2), G(i) = UT2i−1
n
(F). (Notice the rapid decay of the
derived series, which is exponential in n.)
The group Tn(F) is not nilpotent, because
(B.4)
[Tn(F), UTn(F)] = UTn(F),
[Tn(F), Tn(F)] = UTn(F),
so the lower central series of Tn(F) is Li = UTn(F) for i ≥1.
The group UTn(F) has lower and upper central series
Li = UTi+1
n
(F),
Zi = UTn−i
n
(F),
so UTn(F) is nilpotent. Its lower and upper central series are exactly the same except for
the indexing running in the opposite orders in both series.
Here is a brief indication of the importance of the groups Tn(F) when F = C. It is a
theorem of linear algebra that every matrix in GLn(C) is conjugate to an upper-triangular
matrix. That means the subgroup Tn(C) and its conjugates ﬁll up GLn(C). So GLn(C) is
covered by a conjugacy class of solvable subgroups. Moreover, Tn(C) is connected and every
connected solvable subgroup of GLn(C) is conjugate to a subgroup of Tn(C) (Lie–Kolchin
theorem). It is false that arbitrary solvable subgroups of GLn(C) can be conjugated into
Tn(C). For instance, the dihedral group Dm can be embedded in GL2(C) but it can’t be
embedded in T2(C) since two noncommuting elements of order 2 in T2(C) never have a
product with ﬁnite order greater than 2 (like rs and s do in Dm).
We can express Tn(C) as a semidirect product using UTn(C): Tn(C) ∼= UTn(C)⋊(C×)n,
where (C×)n corresponds to the subgroup of diagonal matrices in Tn(C), on which UTn(C)
acts by conjugation. More generally, in every connected subgroup G ⊂GLn(C) there is a
maximal connected solvable normal subgroup B ⊂G, and this subgroup B can be expressed
as a semidirect product of a nilpotent normal subgroup and a group isomorphic to a product
of copies of C×, just as with Tn(C).
The groups Tn(F) and UTn(F) for ﬁnite F suggest an analogy between GLn(F) and
an arbitrary ﬁnite group G. The group U = UTn(F) is a Sylow subgroup of GLn(F) (p-
Sylow with p equal to the characteristic of F), so we will take as its analogue in G a Sylow
subgroup, say P. In GLn(F), T = Tn(F) equals the normalizer of U, so an analogue of T
in G is the normalizer of P. This is recorded in Table 4.
GLn(F)
G
U = UTn(F)
Sylow subgroup P
T = Tn(F)
N(P)
Table 4.
Both U and P are nilpotent (they are groups of prime-power size), but T is solvable while
N(P) need not be solvable and T/U ∼= (F×)n is abelian while N(P)/P need not be abelian.
Nevertheless, we will show that Table 4 can suggest fruitful ideas.
Let D be the group of n × n invertible diagonal matrices over F. This group is a “com-
plement” to U in T: D and U intersect trivially and T = DU = UD. We therefore ask if
there is a subgroup K ⊂N(P) such that P ∩K is trivial and N(P) = PK. There is! Our
analogy has led us to guess a special case of an important theorem about ﬁnite groups.

<!-- page 29 -->
SUBGROUP SERIES I
29
Theorem B.1 (Schur-Zassenhaus). If H is a ﬁnite group and N is a normal subgroup of
H such that (|N|, |H/N|) = 1, then there is a subgroup K ⊂H such that N ∩K is trivial
and H = NK. Moreover, all choices for K are conjugate to each other.
Proof. See [19, pp. 246–248]. The proof that all choices for K are conjugate uses solvability
of either N or H/N. Why is at least one of these solvable? Since N and H/N have relatively
prime orders, at least one of them has odd order (they can’t both have even order!), so at
least one of N and H/N is solvable by the Feit-Thompson theorem. That is all we will say
about the proof.
□
Take H = N(P) and N = P to get a complement to P in N(P).
Example B.2. If H = A4 and N = V , choices for K include ⟨(123)⟩and ⟨(124)⟩. These
are conjugate.
Invoking the Feit–Thompson theorem in the proof the Schur-Zassenhaus theorem is quite
out of proportion with the other details in the proof, so it’s probably a good idea to check,
when using the Schur–Zassenhaus theorem, if the solvability of N or H/N in the particular
application is known a priori for elementary reasons. For instance, in the analogy we were
building between GLn(F) and an arbitrary ﬁnite group G, the role of N is played by a Sylow
subgroup P (normal in N(P)), which is nilpotent and therefore solvable. Hence, to say every
Sylow subgroup of a ﬁnite group has a complementary subgroup inside its normalizer by
the Schur–Zassenhaus theorem does not require appealing to the Feit–Thompson theorem,
because the Sylow subgroup is trivially solvable.
References
[1] Z. Arad and M. B. Ward, New criteria for solvability of ﬁnite groups, J. Algebra 77 (1982), 234–246.
[2] B. Baumslag, A Simple Way of Proving the Jordan–H¨older-Schreier Theorem, Amer. Math. Monthly
113 (2006), 933–935.
[3] M. Bianchi, A. G. B. Mauri, and P. Hauck, On ﬁnite groups with nilpotent Sylow-normalizers, Arch.
Math. (Basel) 47 (1986), 193–197.
[4] A. Borel, “Linear Algebraic Groups,” 2nd ed., Springer-Verlag, New York, 1991.
[5] R. W. Carter, Nilpotent self-normalizing subgroups of soluble groups, Math. Z. 75 (1961), 136–139.
[6] D. Dummit and R. Foote, “Abstract Algebra,” 3rd ed., Wiley, New York, 2004.
[7] A. Facchini, The Krull–Schmidt theorem, pp. 357–397 in: Handbook of algebra, Vol. 3, North-Holland,
Amsterdam, 2003.
[8] W. Feit and J. Thompson, Solvability of groups of odd order, Paciﬁc J. Math. 13 (1963), 775–1029.
[9] M. Hall, “Theory of Groups,” Macmillan, New York, 1959.
[10] P. Hall, Finite-by-nilpotent groups, Proc. Cambridge Philos. Soc. 52 (1956), 611–616.
[11] P. Hall, “Edmonton Notes on Nilpotent Groups,” Queen Mary College Mathematics Notes, Queen Mary
College, London, 1969.
[12] P. Hilton, On Variants of a Theorem of Schur, Int. J. Math. Math. Sci 2005 (2005), 3269–3272.
[13] H. Heineken and I. J. Mohamed, A group with trivial centre satisfying the normalizer condition, J.
Algebra 10 (1968), 368–376.
[14] T. Hungerford, “Algebra,” Springer-Verlag, New York, 1974.
[15] M. I. Kargapolov and Y. I. Merzlyakov, “Fundamentals of the theory of groups,” Springer–Verlag, New
York, 1979.
[16] E. I. Khukhro, “Nilpotent Groups and Their Automorphisms,” de Gruyter, Berlin, 1993.
[17] F. Levi, Groups in which the commutator operation satisﬁes certain algebraic conditions, J. Indian
Math. Soc. 6 (1942), 87–97.
[18] J. Nicholson, The Development and Understanding of the Concept of Quotient Group, Historia Math.
20 (1993), 68–88.
[19] D. Robinson, “A Course in the Theory of Groups,” 2nd ed., Springer-Verlag, New York, 1996.

<!-- page 30 -->
30
KEITH CONRAD
[20] M. Suzuki, “Group Theory II,” Springer–Verlag, New York, 1986.
[21] E. P. Vdovin, Carter subgroups of ﬁnite almost simple groups, Algebra i Logika 46 (2007), 157–216.
[22] G. Zappa, Remark on a recent paper of O. Ore, Duke Math. J. 6 (1940), 511–512.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*