# Modules over a PID

> **Source**: https://kconrad.math.uconn.edu/blurbs/modulesoverPID.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
MODULES OVER A PID
KEITH CONRAD
Every vector space over a ﬁeld K that has a ﬁnite spanning set has a ﬁnite basis: it is
isomorphic to Kn for some n ≥0. When we replace the scalar ﬁeld K with a commutative
ring A, it is no longer true that every A-module with a ﬁnite generating set has a basis: not
all modules have bases. But when A is a PID, we get something nearly as good as that:
(1) Every submodule of An has a basis of size at most n.
(2) Every ﬁnitely generated torsion-free A-module M has a ﬁnite basis: M ∼= An for a
unique n ≥0.
(3) Every ﬁnitely generated A-module M is isomorphic to Ad ⊕T, where d ≥0 and T
is a ﬁnitely generated torsion module.
We will prove this based on how a submodule of a ﬁnite free module over a PID sits inside
the free module. Then we’ll learn how to count with ideals in place of positive integers.
1. Preliminary results
We start with two lemmas that have nothing to do with PIDs.
Lemma 1.1. If A is a nonzero commutative ring and Am ∼= An as A-modules then m = n.
Proof. The simplest proof uses a maximal ideal m in A. Setting M = Am and N = An, if
M ∼= N as A-modules then it restricts to an isomorphism mM ∼= mN and we get an induced
isomorphism M/mM ∼= N/mN. This says (A/m)m ∼= (A/m)n as A-modules, hence also as
A/m-vector spaces, so m = n from the well-deﬁnedness of dimension for vector spaces.
□
Lemma 1.1 says all bases in a ﬁnite free module over a nonzero commutative ring have the
same size, and we call the size of that basis the rank of the free module. So the term rank
means dimension when the ring is a ﬁeld.1 The proof of Lemma 1.1 is valid for free modules
with an inﬁnite basis, so the rank of a free module with an inﬁnite basis is well-deﬁned as
a cardinal number. For our purposes, we only care about free modules of ﬁnite rank.
Commutativity in Lemma 1.1 matters: for some noncommutative A, A2 ∼= A as left
A-modules.
Lemma 1.2. A ﬁnitely generated torsion-free module M over an integral domain A embeds
into a ﬁnite free A-module. More precisely, if M ̸= 0, there is an embedding M ,→Ad for
some d ≥1 such that the image of M intersects each standard coordinate axis of Ad.
Proof. Let K be the fraction ﬁeld of A and x1, . . . , xn be a generating set for M as an
A-module. We will show n is an upper bound on the size of each A-linearly independent
subset of M. Let f : An →M be the linear map where f(ei) = xi for all i. (By e1, . . . , en
we mean the standard basis of An.) Let y1, . . . , yk be linearly independent in M, so their
A-span is isomorphic to Ak. Write yj = Pn
i=1 aijxi with aij ∈A. We pull the yj’s back to
1The word “rank” means something completely diﬀerent in linear algebra – the dimension of the image
of a linear map.
1

<!-- page 2 -->
2
KEITH CONRAD
An by setting vj = (a1j, . . . , anj), so f(vj) = yj. A linear dependence relation on the vj’s
is transformed by f into a linear dependence relation on the yj’s, which is a trivial relation
by their linear independence. Therefore v1, . . . , vk is A-linearly independent in An, hence
K-linearly independent in Kn. By linear algebra over ﬁelds, k ≤n.
From the bound k ≤n, there is a linearly independent subset of M with maximal size,
say t1, . . . , td. Then Pd
j=1 Atj ∼= Ad. We will ﬁnd a scalar multiple of M inside of this. For
each x ∈M, the set {x, t1, . . . , td} is linearly dependent by maximality of d, so there is a
nontrivial linear relation ax + Pd
i=1 aiti = 0, necessarily with a ̸= 0. Thus ax ∈Pd
j=1 Atj.
Letting x run through the spanning set x1, . . . , xn there is an a ∈A −{0} such that
axi ∈Pd
j=1 Atj for all i, so aM ⊂Pd
j=1 Atj. Multiplying by a is an isomorphism of M
with aM, so we have the sequence of A-linear maps
M →aM ,→
d
X
j=1
Atj →Ad,
where the last map is an isomorphism.
□
2. Submodules of a finite free module
First we will show submodules of a ﬁnite free module over a PID are ﬁnitely generated,
with a natural upper bound on the number of generators.
Theorem 2.1. When A is a PID, each submodule of a free A-module of rank n is ﬁnitely
generated with at most n generators.
Proof. A free A-module of rank n is isomorphic to An, so we may assume the free A-module
is An. We will induct on n. The case n = 0 is trivial and the case n = 1 holds since A is a
PID: an A-submodule of A is an ideal, hence Aa since all ideals in A are principal.
Suppose n ⩾1 and the theorem is proved for all submodules of An. Let M ⊂An+1 be
a submodule. We want to show M has at most n + 1 generators. Write An+1 = An ⊕A
and let π: An ⊕A ↠An be projection to the ﬁrst component of the direct sum. We look
at the image and kernel of π|M, the restriction of π to M. Its image π(M) is a submodule
of An, so π(M) has at most n generators by the inductive hypothesis: π(M) = Pk
i=1 Ayi
where y1, . . . , yk ∈An and k ≤n. We can write yi = π(xi) for some xi ∈M, so π(M) =
Pk
i=1 Aπ(xi). And ker(π|M) = M ∩(0 ⊕A), with 0 ⊕A ∼= A as A-modules. Since A is a
PID, A-submodules of A have a single generator, so ker(π|M) = Ax0 for some x0 ∈M.
We will show M = Pk
i=0 Axi, so M has at most k + 1 generators and k + 1 ⩽n + 1. The
containment Pk
i=0 Axi ⊂M is clear. For the reverse containment, pick an arbitrary x ∈M
and the previous paragraph tells us π(x) = a1π(x1) + · · · + akπ(xk) = π(a1x1 + · · · + akxk)
for some a1, . . . , ak in A. Therefore x −Pk
i=1 aixi ∈ker(π|M), so x −Pk
i=1 aixi = a0x0 for
some a0 ∈A. Thus x = a0x0 + a1x1 + · · · + akxk ∈Pk
i=0 Axi, so M ⊂Pk
i=0 Axi.
□
Let’s reﬁne the previous theorem by showing a submodule of a ﬁnite free A-module is
free (has a basis). The proof will be like the one above, but will not logically depend on it.
Theorem 2.2. When A is a PID, each submodule of a free A-module of rank n is free of
rank ⩽n.
Proof. As before, since a free A-module of rank n is isomorphic to An, we can assume the
free A-module we use is An. We’ll induct on n.

<!-- page 3 -->
MODULES OVER A PID
3
The case n = 0 is trivial and the case n = 1 follows from all submodules of A being (0)
or principal with a nonzero generator, and Aa ∼= A as A-modules when a is nonzero in A
since A is an integral domain.
Suppose n ⩾1 and the theorem is proved for all submodules of An. For a submodule M of
An+1, to show M is free of rank at most n+1 write An+1 = An⊕A and let π: An⊕A ↠An
be projection to the ﬁrst component. Since π(M) is a submodule of An, π(M) is free of
rank ⩽n by the inductive hypothesis.
Case 1: π(M) = 0. Here M ⊂0 ⊕A, so M is free of rank at most 1 since A is a PID.
Case 2: π(M) ̸= 0. Here π(M) is a nonzero submodule of An, so π(M) is free of positive
rank d ≤n. Write a basis of π(M) as π(e1), . . . , π(ed) where ei ∈M: π(M) = Ld
i=1 Aπ(ei).
The elements e1, . . . , ed in M are linearly independent since their images under π are: if
P aiei = 0 in M then apply π to get P aiπ(ei) = 0 in π(M), so all ai are 0.
For m ∈M, π(m) = Pd
i=1 aiπ(ei) for unique a1, . . . , ad ∈A. Then π(m−Pd
i=1 aiei) = 0,
so m −Pd
i=1 aiei ∈ker(π|M). We get inverse maps
M ←→Ad ⊕ker(π|M)
by
(
m 7−→(a1, . . . , ad, m −Pd
i=1 aiei)
Pd
i=1 aiei + k ←−[ (a1, . . . , ad, k)
and both maps are linear (check!). So M ∼= Ad ⊕ker(π|M) as A-modules. Thus M is free
of rank d or d + 1 (depending on ker(π|M) being {0} or not), and d + 1 ≤n + 1.
□
Theorem 2.2 is always false if A is not a PID, even for the A-module A itself.
Non-example 2.3. If A is not a PID then either it is not an integral domain or it has a
nonprincipal ideal. If A is not an integral domain then we have xy = 0 for some nonzero
x and y in A, and the principal ideal Ax is not a free A-module. If A has a nonprincipal
ideal then that ideal is not a free A-module.
Remark 2.4. Theorem 2.2 holds for inﬁnite-rank free modules too: submodules of all free
modules over a PID are free. The proof for inﬁnite bases uses Zorn’s lemma [5, pp. 650–651].
Remark 2.5. Unlike vector spaces, a spanning set of a ﬁnite free A-module might not
contain a basis: Z is spanned by {2, 3} as a Z-module, but {2} and {3} are not Z-bases.2
An analogue of that in Z2 is in Example 5.25.
Corollary 2.6. When A is a PID, every ﬁnitely generated torsion-free A-module is a ﬁnite
free A-module.
Proof. By Lemma 1.2, such a module embeds into a ﬁnite free A-module, so it is ﬁnite free
too by Theorem 2.2.
□
The term “free” in “torsion-free module” and “free module” means diﬀerent things: a
torsion-free module has no nonzero torsion elements (all elements have annihilator ideal (0)
aside from the element 0), while a free module has a basis. So Corollary 2.6 is saying a
ﬁnitely generated module over a PID that has no torsion elements admits a basis. Corollary
2.6 is false without the ﬁnite generatedness hypothesis. For example, Q is a torsion-free
abelian group but it has no basis over Z: every (nonzero) free Z-module has proper Z-
submodules (that is, proper subgroups) of ﬁnite index while Q does not.
2If you know about DVRs (a special type of PID): every minimal spanning set of a ﬁnite free module
over a DVR is a basis. The proof uses Nakayama’s lemma.

<!-- page 4 -->
4
KEITH CONRAD
Corollary 2.7. Let A be a PID. If we have a tower of A-modules M ⊃M′ ⊃M′′ with
M ∼= An and M′′ ∼= An then M′ ∼= An.
Proof. Since M is free of rank n and M′ is a submodule, Theorem 2.2 tells us M′ ∼= Am
with m ≤n. Using Theorem 2.2 on M′′ as a submodule of M′, M′′ ∼= Ak with k ≤m. By
hypothesis M′′ ∼= An, so k = n by Lemma 1.1. Thus m = n.
□
Corollaries 2.6 and 2.7 are both generally false when A is not a PID.
Non-example 2.8. Let A = Z[√−5] and consider the tower of ideals
3Z[
√
−5] ⊂(3, 1 +
√
−5) ⊂Z[
√
−5].
The bottom and top are principal ideals, so they are free A-modules of rank 1. The middle
ideal (3, 1 + √−5) is ﬁnitely generated and torsion-free, but is not principal and therefore
is not a free A-module. (A nonzero ideal is a free module only when it is principal, since
all pairs of elements in an ideal are linearly related.)
Corollary 2.9. When A is a PID, M is a ﬁnite free A-module, and N is a submodule of
M such that M/N is torsion-free, each A-basis of N can be extended to an A-basis of M.
Proof. The result is obvious if N = 0 or N = M, so we can assume N ̸= 0 and N ̸= M.
Step 1: M/N is a ﬁnite free A-module.
Since M is a ﬁnitely generated A-module, so is M/N.
Since M/N is a torsion-free
A-module by hypothesis, M/N is a ﬁnite free A-module by Corollary 2.6.
Step 2: each basis of N extends to a basis of M.
Let e1, . . . , er be a basis of N (the basis is nonempty since N ̸= 0). Since M/N is ﬁnite
free by Step 1, it has an A-basis, say er+1, . . . , ed (this basis is nonempty since M/N ̸= 0).
We will show e1, . . . , ed is a basis of M.
First we show e1, . . . , ed spans M as an A-module. For m ∈M, since m ∈M/N we have
m = ar+1er+1 + · · · + aded
for some ar+1, . . . , ad ∈A. Then m −ar+1er+1 −· · · −aded ∈N, so we can write
m −ar+1er+1 −· · · −aded = a1e1 + · · · + arer
for some a1, . . . , ar ∈A. Thus
m = a1e1 + · · · + arer + ar+1er+1 + · · · + aded.
Next we show e1, . . . , ed is A-linearly independent in M. If
(2.1)
a1e1 + · · · + aded = 0
then reduce both sides modulo N to get
ar+1er+1 + · · · + aded = 0,
so by the basis property in M/N we get ai = 0 for i = r + 1, . . . , d. Feeding this into (2.1),
a1e1 + · · · + arer = 0
in N, so ai = 0 for i = 1, . . . , d.
□
Example 2.10. Let M = Z[
4√
2] and N = Z[
√
2], with A = Z. Then
M = Z + Z
4√
2 + Z
√
2 + Z
4√
2
√
2 = N ⊕N
4√
2,
so M/N ∼= N
4√
2 ∼= Z2 is torsion-free. Thus each Z-basis of Z[
√
2] extends to a Z-basis of
Z[
4√
2].

<!-- page 5 -->
MODULES OVER A PID
5
Non-example 2.11. Let M = Z[
4√
2] and N = Z[3
√
2], with A = Z. Then
√
2 ̸= 0 in
M/N but 3
√
2 = 0 in M/N, so M/N is not torsion-free. It can be shown that the Z-basis
{1, 3
√
2} of N is not part of a Z-basis of M (see Exercise 3).
There is a convenient way of picturing a submodule of a ﬁnite free module over a PID:
bases can be chosen for the module and submodule that are aligned nicely, as follows.
Deﬁnition 2.12. If A is a PID, M is a ﬁnite free A-module, and M′ is a submodule of M,
then a basis {v1, . . . , vn} of M and a basis {a1v1, . . . , amvm} of M′ with ai ∈A −{0} and
m ≤n is called a pair of aligned bases.
Pictures will show how aligned bases look before seeing the main theorem about them.
Example 2.13. Let A = Z, M = Z[i] and take M′ = (1 + 2i)Z[i]. So M = Z + Zi and
M′ = (1 + 2i)Z[i] = (1 + 2i)Z + (1 + 2i)Zi = Z(1 + 2i) + Z(−2 + i).
The obvious Z-bases for M and M′ are {1, i} and {1 + 2i, −2 + i}. In Figure 1, we shade
a box having each basis as a pair of edges and translate each box across the plane. The
modules M and M′ are the intersection points of the networks of lines formed by the small
and large boxes, respectively. The lines are only a visual aid, showing how a choice of basis
gives a speciﬁc way to generate the module by the basis.
f
Z[i] = Z + Zi,
(1 + 2i) = Z(1 + 2i) + Z(−2 + i)
Figure 1. Nonaligned bases for a modules and submodule

<!-- page 6 -->
6
KEITH CONRAD
To see a completely diﬀerent picture of the same two modules M and M′, we use new
bases: {1 + 2i, i} for M and {1 + 2i, 5i} for M′. These are bases because of the relations

1 + 2i
i

=

1
2
0
1
 
1
i

,

1 + 2i
5i

=

1
0
2
1
 
1 + 2i
−2 + i

,
where the two matrices are integral with determinant 1, so the elements of Z[i] in the
vector components on both sides have the same Z-span. These new bases lead to Figure 2,
where the parallelograms with each basis as a pair of edges is shaded and looks quite unlike
the shaded boxes of Figure 1. Translating the parallelograms across the plane produces
two new networks of lines (both sharing all the vertical lines) The intersection points are
the same as before; make sure you can see the vertices of the large box from Figure 1 as
intersection points of lines in Figure 2. In Figure 2 ﬁve of the parallelograms for M ﬁll up
of the parallelograms for M′. These bases are aligned.
Z[i] = Z(1 + 2i) + Zi,
(1 + 2i) = Z(1 + 2i) + Z · 5i
Figure 2. Aligned bases for a module and submodule
Theorem 2.14. Each ﬁnite free A-module M of rank n ⩾1 and nonzero submodule M′
of rank m ⩽n admit a pair of aligned bases: there is a basis v1, . . . , vn of M and nonzero
a1, . . . , am ∈A such that
M =
n
M
i=1
Avi
and
M′ =
m
M
j=1
Aajvj.
We can also arrange that a1 | a2 | · · · | am.

<!-- page 7 -->
MODULES OVER A PID
7
The condition a1 | a2 | · · · | am at the end of the theorem plays an important role in
the proof of the theorem, but it is not used in any applications presented later except for
Theorem 3.6, so you can largely ignore it.
Proof. Our argument is based on [6, Sect. 1.5]. An A-basis of M gives us coordinate func-
tions for that basis, which are A-linear maps M →A: for an A-basis v1, . . . , vn of M, its dual
basis is the A-linear maps v∨
j : M →A where v∨
j (x1v1 + · · · + xdvd) = xj for x1, . . . , xd ∈A.
Bases for M and M′ as in the theorem are “aligned” coordinate systems on M and M′.
Motivation. To explain the main idea in the proof, we’ll ﬁrst suppose the conclusion of
the theorem is true and derive an important consequence about the images of all A-linear
maps ϕ: M →A (the dual module of M) when they are restricted to M′: there is a nonzero
A-linear map ψ: M →A such that
ϕ(M′) ⊂ψ(M′)
for all
ϕ.
To show this, by the formula for M′ in the conclusion of the theorem we get for all ϕ that
ϕ(M′) = ϕ
 m
X
j=1
Aajvj

=
m
X
j=1
Aajϕ(vj) ∈Aa1 + · · · + Aam.
Since A is a PID, Aa1 + · · · + Aam = (a) for some nonzero a ∈A, so ϕ(M′) ⊂(a) for all ϕ.3
Write a = c1a1 + · · · + cmam with cj ∈A (the choice of cj’s may not be unique, but
ﬁx such a representation for a) and deﬁne ψ = Pm
j=1 cje∨
j as a linear map M →A. Then
ψ(Pm
j=1 ajej) = Pm
j=1 cjaj = a and Pm
j=1 ajej ∈M′, so
(a) ⊂ψ(M′) ⊂(a).
Thus ψ(M′) = (a) and this ideal is the unique maximal member with respect to inclusion
among all ideals ϕ(M′) as ϕ varies over all linear maps M →A. (This is not saying (a) is
a maximal ideal!). This ends the motivation.
Step 1. The set of ideals S := {ϕ(M′) : ϕ: M →A is linear} is not {(0)} and has a
maximal member (a).
Let {v1, . . . , vn} be a basis of M. Since M′ ̸= {0}, at least one coordinate function v∨
j
for this basis of M is not identically 0 on M′, which makes v∨
j (M′) a nonzero ideal in S.
Each nonzero ideal of A is contained in only ﬁnitely many ideals of A since A is a PID: if
(x) is a nonzero ideal then we have (x) ⊂(y) if and only if y | x. Up to unit multiples, there
are only ﬁnitely many possible y since x has only ﬁnitely many factors up to unit multiples.
Applying this to (x) = ϕ(M′) for some ϕ where ϕ(M′) ̸= (0) and looking at the ﬁnitely
many ideals containing (x), S contains a maximal member with respect to inclusion, say
(a) = ψ(M′).
Then a ̸= 0, and maximality means that if (a) ⊂ϕ(M′) for some ϕ, then ϕ(M′) = (a).4
Since a ∈ψ(M′), there’s some v′ ∈M′ such that a = ψ(v′) .
Step 2: For the ideal (a) in Step 1 and each A-linear map ϕ: M →A, a | ϕ(v′) in A.
Write the ideal (a, ϕ(v′)) as (b), where b ∈A −{0}. For some x and y in A,
b = ax + ϕ(v′)y = xψ(v′) + yϕ(v′) = (xψ + yϕ)(v′).
3If a1 | a2 | · · · | am, which we don’t want to assume, then we can let a = a1 since (am) ⊂· · · ⊂(a2) ⊂(a1).
4We anticipate (a) will be the unique maximal member of S by the argument in the motivational section
at the start of this proof, but at the moment (a) is just some maximal member of S.

<!-- page 8 -->
8
KEITH CONRAD
Since xψ + yϕ is a linear map M →A,
(a) ⊂(a, ϕ(v′)) = (b) ⊂(xψ + yϕ)(M′),
so the maximality of (a) in Step 1 implies (a) = (b) = (a, ϕ(v′)). Therefore a | ϕ(v′).
Step 3: There is an e1 ∈M such that ψ(e1) = 1.
Write v′ in the basis {v1, . . . , vn} as v′ = Pn
i=1 civi. Then ci = v∨
i (v′) ∈(a) by Step 2, so
ci = abi where bi ∈A. Thus
v′ = a(b1v1 + · · · + bnvn).
Set e1 := b1v1 + · · · + bnvn in M, so a = ψ(v′) = aψ(e1) in A. Since a ̸= 0, ψ(e1) = 1.
Step 4: We have direct sum decompositions
M = Ae1 ⊕ker ψ,
M′ = Aae1 ⊕(M′ ∩ker ψ).
First we show M = Ae1 + ker ψ. For each v ∈M, ψ(v −ψ(v)e1) = ψ(v) −ψ(v)ψ(e1) =
ψ(v) −ψ(v) = 0, so v −ψ(v)e1 ∈ker ψ.
Therefore M ⊂Ae1 + ker ψ and the reverse
containment is obvious.
The sum in Ae1 + ker ψ is direct since if v ∈Ae1 ∩ker ψ then v = αe1 and ψ(v) =
αψ(e1) = α, so if ψ(v) = 0 then α = 0.
Next we show M′ = Aae1 + (M′ ∩ker ψ). For each v ∈M′, ψ(v −ψ(v)e1) = 0 as before,
and ψ(v) ∈ψ(M′) = (a), so M ⊂Aae1 + ker ψ and the reverse containment is obvious.
This sum is direct for the same reason as above. This completes Step 4.
Step 5: Extend the direct sum decompositions in Step 4 to bases of M and M′.
If M′ ∩ker ψ = {0} then M′ = Aae1, so m = 1 and the theorem is proved in this case by
using any basis of ker ψ as e2, . . . , en.
Now suppose M′ ∩ker ψ ̸= {0}. Then ker ψ is free of rank n −1 and M′ ∩ker ψ is free
of rank m −1 ≥1 by the direct sum decompositions of M and M′ in Step 4.
Rename a as a1. By induction on n (and m), there is a basis e2, . . . , en of ker ψ and
nonzero a2, . . . , am in A such that a2e2, . . . , amem is a basis of M′ ∩ker ψ. Then the direct
sums in Step 4 take the form
M = Ae1 ⊕(Ae2 ⊕· · · ⊕Aen),
M′ = Aa1e1 ⊕(Aa2e2 ⊕· · · ⊕Aamem).
If we are not interested in a relation like a1 | a2 | · · · | am then we are done with the
proof. If instead we want to prove a1 | a2 | · · · | am then we can bring in a2 | · · · | am by the
inductive hypothesis. Why does a1 | a2? Do we need to go back and prove stronger forms of
earlier steps? That isn’t necessary. Consider how ϕ = e∨
1 + e∨
2 behaves on v′ = ae1 = a1e1:
a1 = a = ϕ(v′) ∈ϕ(M′), so (a) ⊂ϕ(M′). By the maximality of (a) in Step 1, (a) = ϕ(M′).
Then a2 = ϕ(a2e2) ∈ϕ(M′) = (a) = (a1), so a1 | a2.
□
In this theorem, an aligned basis for M and M′ depends on both modules: there need
not be an aligned basis that uses an arbitrary basis for M or an arbitrary basis for M′.
Example 2.15. Let M = Z2 and M′ = {
 x
y

∈Z2 : x ≡y mod p} = Z
 1
1

+ Z
 p
0

for
prime p. An example of aligned Z-bases here is {
 1
1

,
 1
0

} for M and {
 1
1

, p
 1
0

} for M′,
so [M : M′] = p. (Another way to see [M : M′] = p is that the mapping M →Z/(p)
where
 x
y

7→x −y mod p is additive and surjective with kernel M′, so M/M′ ∼= Z/(p).) A
general pair of aligned bases for M and M′ has the form {v1, v2} for M and {a1v1, a2v2}
for M′, so M/M′ ∼= Z/(a1) × Z/(a2) as abelian groups. Then [M : M′] = p = |a1a2|, so
{a1, a2} = {±1, ±p}. That means v1 or v2 (depending on whether a1 or a2 is ±1) has to

<!-- page 9 -->
MODULES OVER A PID
9
be in M′, so the basis {
 1
0

,
 0
1

} of M isn’t part of an aligned basis with M′ since neither
element of that basis is in M′. Conversely, a vector in Z2 multiplied by p has both of its
coordinates divisible by p, so the basis {
 1
1

,
 p+1
1

} of M′ is not part of an aligned basis
with M.
Corollary 2.16. Let A be a PID, M be ﬁnite free A-module, and M′ be a submodule of
M. Then M and M′ have the same rank if and only if M/M′ is a torsion module.
Proof. Let M have rank n. The module M′ is free of some rank m ≤n. Using aligned
bases for M and M′, we can write
M =
n
M
i=1
Avi
and
M′ =
m
M
j=1
Aajvj
with nonzero aj’s. Then M/M′ ∼= Lm
j=1 A/(aj) ⊕An−m. This is a torsion module if and
only if m = n.
□
3. Applications to matrix groups
In this section we give applications of Corollary 2.7 and Theorem 2.14 to matrix groups.
A matrix in GLn(Q) that has ﬁnite order does not have to have entries in Z. For example,
( −1 x
0 1 ) has order 2 for all x ∈Q. But this matrix is conjugate to a matrix with entries in Z:
( 1 −x/2
0
1
)( −1 x
0 1 )( 1 −x/2
0
1
)−1 = ( −1 0
0 1 ). More generally, it turns out that every ﬁnite subgroup
of GLn(Q) is conjugate to a subgroup with entries in Z. This is a special case of a result
we prove below about subgroups of GLn(K) where K is the fraction ﬁeld of a PID.
Deﬁnition 3.1. Let A be a PID and K be its fraction ﬁeld. A subset S of K has a common
denominator in A when there is a nonzero a ∈A such that aS ⊂A.
Example 3.2. Every ﬁnite subset S of K has a common denominator in A: use the product
of the denominators of the elements of S when they are written as ratios of numbers in A.
Example 3.3. Let S = Pn
j=1 Axi be a ﬁnitely generated A-submodule of K. It has a
common denominator in A, such as a common denominator of the numbers x1, . . . , xn.
Non-example 3.4. In Q, the set of reciprocal powers {1/2, 1/4, 1/8, . . . , 1/2n, . . .} has no
common denominator in Z.
Theorem 3.5. Let A be a PID and K be its fraction ﬁeld. Every subgroup G of GLn(K)
whose matrix entries have a common denominator in A is conjugate to a subgroup with
matrix entries in A: there is a matrix L ∈GLn(K) such that all matrices in LGL−1 have
entries in A. In particular, every ﬁnite subgroup of GLn(K) is conjugate to a subgroup with
matrix entries in A.
The common denominator hypothesis of this theorem means for some nonzero a ∈A, ag
has matrix entries in A for all g ∈G.
Proof. For each g ∈G, g(An) is a ﬁnite free A-submodule of Kn. Let M be the A-module
P
g∈G g(An), which is the set of ﬁnite sums of vectors in Kn that belong to g(An) for some
g ∈G. This is an A-module in Kn that contains An (use g = In). Note M is G-stable
(carried back to itself when acting on it by elements of G).

<!-- page 10 -->
10
KEITH CONRAD
The common denominator hypothesis says there is a nonzero a ∈A such that each
matrix ag for g ∈G has all of its entries in A. Therefore aM = P
g∈G(ag)(An) ⊂An, so
M ⊂(1/a)An in Kn. Thus An ⊂M ⊂(1/a)An. By Corollary 2.7, M ∼= An as A-modules.
Let ϕ: An →M be an A-module isomorphism. Then M = ϕ(An) is the A-linear span
of ϕ(e1), . . . , ϕ(en). These vectors are A-linearly independent since they span a free A-
module of rank n, so they are also K-linearly independent: a nontrivial K-linear relation
would become a nontrivial A-linear relation. Therefore the matrix Φ = [ϕ(e1) · · · ϕ(en)] is
invertible, so Φ ∈GLn(K) and Φ = ϕ on An.
For each g ∈G, gM ⊂M since M is G-stable, so gϕ(An) ∈ϕ(An). Therefore g(Φ(An)) ⊂
Φ(An), so Φ−1gΦ(An) ⊂An. This means the matrix Φ−1gΦ has entries in A (its columns
are (Φ−1gΦ)(ei) for i = 1, . . . , n). Letting g run over G, the group Φ−1GΦ is conjugate to
G and its elements have matrix entries in A.
□
Our second application to matrix groups will be the computation of normalizers. For a
group G and subgroup H of G, the normalizer of H is NG(H) = {g ∈G : gHg−1 = H} =
{g ∈G : g−1Hg = H}: this is the largest subgroup of G in which H is a normal subgroup.
Theorem 3.6. Let A be a PID and K be its fraction ﬁeld. In the group GLn(K), both
GLn(A) and SLn(A) have normalizer K× GLn(A).
We view K× inside GLn(K) as the nonzero scalar diagonal matrices {cIn : c ∈K×}.
This is the center of GLn(K).
Proof. The result is trivial when n = 1, since GL1(K) = K× is commutative, so from now
on we can assume n ≥2. Set G = GLn(K). We will show NG(GLn(A)) = K× GLn(A) and
then indicate how that argument can be modiﬁed to show NG(SLn(A)) = K× GLn(A).
That K× GLn(A) ⊂NG(GLn(A)) is obvious. To prove NG(GLn(A)) ⊂K× GLn(A), pick
g ∈NG(GLn(A)). We will ﬁnd c ∈K× such that cg ∈GLn(A). The proof is based on an
answer to the Mathoverﬂow question https://mathoverflow.net/questions/80667. Set
M = g(An).
Step 1: M is a free A-module of rank n and is GLn(A)-stable: L(M) ⊂M for all
L ∈GLn(A).
The A-module M is spanned by g(e1), . . . , g(en) where e1, . . . , en is the standard basis
of An, and g(e1), . . . , g(en) is A-linearly independent since g is an invertible matrix over A.
Thus M ∼= An as A-modules.
To show M is GLn(A)-stable, we use the property g−1 GLn(A)g = GLn(A), which is the
condition of g normalizing GLn(A). For L ∈GLn(A), L′ := g−1Lg is in GLn(A) too, so
Lg = gL′. Therefore
L(M) = Lg(An) = gL′(An) = g(An) = M.
Step 2: There is d ∈A −{0} such that dM ⊂An.
Let d ∈A −{0} be a common denominator for the coordinates of g(e1), . . . , g(en) in Kn.
Then dg(ei) ∈An for i = 1, . . . , n, so dM ⊂An.
Step 3: There is c ∈K× such that cg ∈GLn(A).
By Steps 1 and 2, dM is a submodule of An with rank n, so by Theorem 2.14 we can ﬁnd
a basis {f1, . . . , fn} of An and nonzero a1, . . . , an in A such that {a1f1, . . . , anfn} is a basis
of dM and a1 | a2 | · · · | an. We won’t use the full strength of that divisibility condition,
but just a1 | ai for i = 1, . . . , n.

<!-- page 11 -->
MODULES OVER A PID
11
In the direct sum decomposition
dM =
n
M
i=1
Aaifi,
divide through by a1:
d
a1
M =
n
M
i=1
A ai
a1
fi = Af1 ⊕
n
M
i=2
A ai
a1
fi.
Set M′ = (d/a1)M, so M′ is a submodule of An (each ai/a1 is in A) and M′ contains the
vector f1 that’s part of a basis {f1, . . . , fn} of An. Since M is GLn(A)-stable by Step 1, so
is M′.
The matrix L with columns f1, . . . , fn (in that order) is in GLn(A) since the columns are
a basis of An, and L(e1) = f1. Then e1 = L−1(f1) ∈M′ because L−1 ∈GLn(A) and M′
is GLn(A)-stable. By a similar argument, if we permute the columns of L to place f1 in
the jth column for j = 2, . . . , n then we get ej ∈M′. Thus M′ is a submodule of An that
contains e1, . . . , en, so M′ = An . Rewriting that as (d/a1)g(An) = An tells us the matrix
(d/a1)g is in GLn(A), so cg ∈GLn(A) where c = d/a1 ∈K×. This completes the proof
that NG(GLn(A)) = K× GLn(A).
To show NG(SLn(A)) = K× GLn(A), we have K× GLn(A) ⊂NG(SLn(A)) since SLn(A)◁
GLn(A). For the reverse containment, if g ∈NG(SLn(A)) then we want c ∈K× such that
cg(An) = An, so cg ∈GLn(A). The procedure used above for NG(GLn(A)) can be applied to
NG(SLn(A)), with the following changes: M = g(An) is SLn(A)-stable rather than GLn(A)-
stable in Step 1, and in Step 3 modify the matrix L with columns f1, . . . , fn so that its last
column is u−1fn where u = det(f1 · · · fn) ∈A×, as that makes det(L) = uu−1 = 1, so
L ∈SLn(A).
□
4. Finitely generated modules
As an application of aligned bases for a submodule of a ﬁnite free module, we describe
the structure of every ﬁnitely generated module over a PID.
Theorem 4.1. Let A be a PID. Every ﬁnitely generated A-module has the form F ⊕T
where F is a ﬁnite free A-module and T is a ﬁnitely generated torsion A-module. Moreover,
T ∼= Lm
j=1 A/(aj) for some m with nonzero ai.
Proof. Let M be a ﬁnitely generated A-module, with generators x1, . . . , xn. Deﬁne f : An ↠
M by f(ei) = xi. Then there is a surjective linear map An ↠M, so M is isomorphic to
a quotient An/N. As in the proof of Corollary 2.16, An/N ∼=
Lm
j=1 A/(aj)

⊕An−m for
some m ≤n and nonzero aj’s. The direct sum of the A/(aj)’s is a torsion module and
An−m is a ﬁnite free A-module.
□
Example 4.2. Taking A = Z, every ﬁnitely generated abelian group is isomorphic to
Zn ⊕G where n ≥0 and G is a ﬁnite abelian group (a ﬁnitely generated torsion abelian
group must be ﬁnite).
Corollary 4.3. Every ﬁnitely generated torsion module over a PID A is a direct sum of
cyclic torsion modules: it is isomorphic to A/(a1)⊕· · ·⊕A/(ak), where the ai’s are nonzero.
Some ai’s might be units, making A/(ai) = 0.

<!-- page 12 -->
12
KEITH CONRAD
Proof. A ﬁnitely generated module in Theorem 4.1 is a torsion module if and only if F = 0.
The description of T in Theorem 4.1 gives the desired cyclic decomposition for ﬁnitely
generated torsion modules.
□
Corollary 2.6 could be regarded as a consequence of Theorem 4.1: a ﬁnitely generated
module is F ⊕T where F is ﬁnite free and T is torsion, and being torsion-free forces T = 0,
so the module is free.
When a ﬁnitely generated A-module is written as F ⊕T, where F is a ﬁnite free submodule
and T is a torsion submodule, the choice of F is not unique but T is unique: T is the set
of all elements in F ⊕T with nonzero annihilator ideal, which is a description that makes
no reference to the direct sum decomposition. The best way to see F is not unique is by
examples.
Example 4.4. Using A = Z, Z×Z/(2) has generating set {(1, 0), (0, 1)} and {(1, 1), (0, 1)}.
Therefore it can be written as F1 ⊕T1, where F1 = ⟨(1, 0)⟩∼= Z and T1 = 0 ⊕Z/(2), and
also as F2 ⊕T2 where F2 = ⟨(1, 1)⟩∼= Z and T2 = 0 ⊕Z/(2) = T1.
Example 4.5. It can be shown that every unit in Z[
√
2] has the form ±(1 +
√
2)k some
choice of sign ±1 and some integer k, so Z[
√
2]× is a ﬁnitely generated abelian group. The
torsion subgroup of Z[
√
2]× is {±1}, while 1 +
√
2 and −(1 +
√
2) each generate diﬀerent
free subgroups that complement {±1}:
Z[
√
2]× = {±1} × (1 +
√
2)Z = {±1} × (−(1 +
√
2))Z
This leads to two isomorphisms of Z[
√
2]× with Z×Z/2Z, which identify diﬀerent subgroups
with Z (the powers of 1 +
√
2 and the powers of −(1 +
√
2)) but both identify the same
subgroup {±1} with Z/(2).
Example 4.6. It can be shown that Z[
√
2,
√
3]× = ±(1 +
√
2)Z(2 +
√
3)Z(
√
2 +
√
3)Z,
where the units 1 +
√
2, 2 +
√
3, and
√
2 +
√
3 (with respective inverses
√
2 −1, 2 +
√
3, and
√
3 −
√
2) have no multiplicative relations over Z: if (1 +
√
2)a(2 +
√
3)b(
√
2 +
√
3)c = 1
for integer exponents a, b, and c, then a = b = c = 0. Therefore Z[
√
2,
√
3]× ∼= Z3 × Z/2Z.
Two examples of complements to ±1 in Z[
√
2,
√
3]× are ⟨1 +
√
2, 2 +
√
3,
√
2 +
√
3⟩and
⟨1 +
√
2, −(2 +
√
3), −(
√
2 +
√
3)⟩.
While the free part of a direct sum decomposition is not unique, the rank of the free
part is unique: writing M = F ⊕T with F ﬁnite free and T necessarily being the torsion
submodule Mtor of M, we have F ∼= M/T = M/Mtor so the rank of F is the rank of the
ﬁnite free module M/Mtor. The rank of a ﬁnitely generated module over a PID A is deﬁned
to be the rank of its free part, which is well-deﬁned even though the free part itself is not.
In down-to-earth terms, the rank is the largest number of linearly independent torsion-free
elements (over Z, it is the largest number of independent elements of inﬁnite order).
Our focus in this section was on describing the abstract structure of a ﬁnitely generated
module over a PID, not proving a module over a PID arising somewhere in mathematics is
ﬁnitely generated. The fact that certain abelian groups (Z-modules) are ﬁnitely generated
can be a major theorem (look up the Mordell–Weil theorem) and a formula for the rank
can be a major theorem or conjecture (look up Dirichlet’s unit theorem or the Birch and
Swinnerton-Dyer conjecture).
Theorem 4.1 says for a ﬁnitely generated module M over a PID A, M = Mtor ⊕F where
F is a free A-module. In particular, Mtor is a direct summand of M. That conclusion can

<!-- page 13 -->
MODULES OVER A PID
13
become false if (i) A is a PID and M is not ﬁnitely generated or (ii) M is ﬁnitely generated
and A is not a PID. We’ll give examples of this using A = Z for (i) and A = Z[x] for (ii).
Example 4.7. Set M = Q
p Z/(p), which is a Z-module in a natural way. We will show
the torsion submodule T of M is not a direct summand: M ̸= T ⊕N for a submodule N.
The argument is based on [4, Theorem 10.2].
Step 1: T = L
p Z/(p) and T ̸= M.
To prove the claim, one containment is immediate: since elements in the direct sum have
only ﬁnitely many nonzero coordinates and each Z/(p) is killed oﬀby a single prime p, each
element of the direct sum is killed oﬀby a product of ﬁnitely many primes and thus is in
T. Conversely, if m := (ap mod p)p is an element of T and km = 0 where k ∈Z−{0}, then
kap ≡0 mod p for each prime p. When p ∤k, ap ≡0 mod p, so m has only ﬁnitely many
possible nonzero coordinates (its p-coordinates where p is a prime factor of k). Therefore
m ∈L
p Z/(p), which ﬁnishes Step 1. Because there are inﬁnitely many primes, T ̸= M.
Step 2: We can’t write M = T ⊕N for a Z-submodule N of M.
Assume there is such a direct sum decomposition. Then N ∼= M/T, so M has a submodule
isomorphic to M/T. We will get a contradiction by showing M and its submodules all share
a property that is not true for M/T.
The property is this: T
p pM = {0}, where the intersection runs over all primes. Indeed,
for each prime p the p-coordinate of an element of pM has to be 0, so all coordinates of an
element of T
p pM equal 0. Therefore if N is a submodule of M, T
p pN = {0}.
In contrast to that, we will show T
p p(M/T) ̸= {0}. Speciﬁcally, let v := (1, 1, 1, . . .) be
the element of M with p-coordinate 1 mod p for each prime p. We’ll show
(i) v ̸∈T, so v ̸= 0 in M/T,
(ii) v ∈T
p p(M/T).
Proof of (i): If v ∈T, then kv = 0 for some nonzero integer k since v ̸= 0. Looking at
the coordinates of kv, we get k ≡0 mod p for each prime p, so k has inﬁnitely many prime
factors and that forces k = 0, a contradiction.
Proof of (ii): Fix a prime p. We will ﬁnd a w ∈M and t ∈T (depending on p). such
that v = pw + t, so v ≡pw mod T, so v ∈p(M/T).
All the coordinates of v are 1. For each prime q other than p, p is invertible mod q so
we can deﬁne wq ∈Z/(q) by the congruence pwq ≡1 mod q. Deﬁne wp = 0 mod p. Then
w = (wq)q is in M and pw has q-coordinate 1 for each q ̸= p and pw has p-coordinate
0. Therefore v = pw + t where t has p-coordinate 1 and every other coordinate 0, which
means t ∈T. That completes Step 2.
Remark 4.8. This construction of a Z-module whose torsion submodule is not a direct
summand of it carries over without change to modules over a PID A that has inﬁnitely
many non-associate irreducible elements. Let M be the A-module Q
(π) A/(π), where the
direct product is taken over all distinct maximal ideals (π). It is left to the reader to prove
the torsion submodule T of M is L
(π) A/(π) and M ̸= T ⊕N for an A-submodule N of M
by an argument similar to the case A = Z above.
The inﬁnite direct product Q
p Z/(p) in Example 4.7 may seem artiﬁcial. What about
using the abelian group S1, whose torsion submodule is the group µ∞of all roots of unity?
It seems plausible that we can’t write S1 = µ∞× H for a subgroup H of S1, but that is
possible by the Axiom of Choice since µ∞is a divisible abelian group. See Corollary 2.5 in

<!-- page 14 -->
14
KEITH CONRAD
https://kconrad.math.uconn.edu/blurbs/zorn1.pdf. Note that unlike µ∞, the torsion
submodule L
p Z/(p) in Example 4.7 is not divisible.
Example 4.9. Let A = Z[x] and r be an integer besides 0 and ±1, so the ideal a := (r, x)
in A is not principal. We will show M := A2/a
 r
x

, which is a ﬁnitely generated A-module,
does not have Mtor as a direct summand. This example and the argument behind it are
from https://math.stackexchange.com/questions/3593455/.
Since A is an integral domain and a is a proper ideal in A,
 r
x

̸∈a
 r
x

, so
 r
x

̸= 0 in M.
Claim: Mtor = A
 r
x

.
To prove the claim, we have
 r
x

∈Mtor since x
 r
x

= 0 and x ̸= 0. (Also r
 r
x

= 0.) Thus
A
 r
x

⊂Mtor. For the reverse containment, let
 a
b

∈Mtor for a and b in A, so c
 a
b

= 0 for
some nonzero c ∈A. That means
 ca
cb

is in a
 r
x

, so ca = dr and cb = dx for some d ∈a.
We want to show
 a
b

is in A
 r
x

.
If d = 0 then ca and cb are 0, so a and b are 0 since c is nonzero and Z[x] is an integral
domain. Thus
 a
b

= 0 ∈A
 r
x

.
Suppose instead that d ̸= 0.
From ca = dr and cb = dx we have b(dr) −a(dx) =
bca −acb = 0, so d(br −ax) = 0 and thus br = ax. Since x | br and x ∤r (note r is
nonzero in Z), x | b. Write b = xs where s ∈A, so ax = br = xsr. Thus a = sr, so
 a
b

=
 sr
sx

= s
 r
x

, which implies
 a
b

∈A
 r
x

in M. That proves the claim.
To show Mtor is not a direct summand of M, suppose M = Mtor ⊕N for some submodule
N. The projection M →Mtor associated to that hypothetical direct sum decomposition of
M is A-linear and ﬁxes each element of Mtor. We will show every A-linear map f : M →Mtor
must be zero on Mtor, which is incompatible with f ﬁxing Mtor since Mtor is nonzero. Since
Mtor is the A-multiples of
 r
x

, it suﬃces to show f
 r
x

= 0.
Write f
 1
0

= a
 r
x

and
f
 0
1

= b
 r
x

for some a and b in A. Then
f
r
x

= f
 
r
1
0

+ x
0
1
!
= rf
1
0

+ xf
0
1

= ra
r
x

+ xb
r
x

= 0
since
 r
x

is killed by both r and x.
Remark 4.10. Example 4.9 works in the same way if we replace Z[x] by R[x] where R is
an integral domain that is not a ﬁeld and r is a nonzero nonunit in R. What we used about
r and x in the example is that (r, x) is a proper ideal of Z[x], x is prime in Z[x], and x ∤r.
It wasn’t important that r is an integer. (For instance, we could have used r = x + 2).
Therefore we could replace Z[x] by an integral domain A containing a proper ideal of the
form (r, p) where p is prime in A and p ∤r. Such a domain A consisting of numbers rather
than polynomials is Z[√n] where the integer n is not a square and n ≡1 mod 4: the ideal
(1 + √n, 2) in Z[√n] is proper (it has index 2), 2 is prime in Z[√n], and 2 ∤(1 + √n).
There are some integral domains A that are not a PID but every ﬁnitely generated A-
module M has Mtor as a direct summand. This is true if A is a Dedekind domain, which is a
type of generalization of a PID. When we write M = Mtor ⊕N, the complementary module
N is torsion-free but need not be free (that is, it need not have an A-basis). For example,
let A = Z[√−6] and M = Z[
√
2, 1+√−3
2
], so A ⊂M since M contains
√
2 and √−3. Then
Mtor = {0} and M is ﬁnitely generated as an A-module (it is already ﬁnitely generated as

<!-- page 15 -->
MODULES OVER A PID
15
a Z-module, and Z ⊂A), but it can be shown that M is not a free A-module. See Example
2.3 in https://kconrad.math.uconn.edu/blurbs/gradnumthy/notfree.pdf.
5. Cardinality and Index over a PID
A ﬁnite abelian group is the same thing as a ﬁnitely generated torsion module over Z, so
ﬁnitely generated torsion modules over a PID are generalizations of ﬁnite abelian groups.
Corollary 4.3 provides a method of deﬁning a “size” for ﬁnitely generated torsion modules
over a PID as an ideal that generalizes the size of a ﬁnite abelian group.
Deﬁnition 5.1. Let T be a ﬁnitely generated torsion module over the PID A. Writing
T ∼= A/(a1) ⊕· · · ⊕A/(am), deﬁne the A-cardinality of T to be the ideal
cardA(T) = (a1a2 · · · am).
The term A-cardinality is adapted from [2, pp. 35], where they use “A-cardinal”.5 When
A = Z, so T is a ﬁnite abelian group, cardZ(T) is the size (cardinality) of T.
A ﬁnitely generated torsion module can be written as a direct sum of cyclic modules in
more than one way (including diﬀerent numbers of cyclic components), e.g.,
(5.1)
Z/(3) × Z/(4) × Z/(5) × Z/(5) ∼= Z/(5) × Z/(60)× ∼= Z/(15) × Z/(20)
and
(5.2)
R[X]/(X) × R[X]/(X) × R[X]/(X −1) ∼= R[X]/(X2 −X) × R[X]/(X),
so we need to check A-cardinality is well-deﬁned. First let’s look at a few examples of
A-cardinality, assuming that it is well-deﬁned.
Example 5.2. If G is a ﬁnite abelian group and G ∼= Z/(a1)×· · ·×Z/(am), then cardZ(G) =
(a1 · · · am)Z, whose positive generator is |a1 · · · am| = |G|.
Example 5.3. If T = {0} then each (ai) is (1), so cardA(T) = (1) = A. The converse holds
too: if cardA(T) = (1) then a1 · · · am is a unit, so each (ai) is (1) and thus T is trivial.
Example 5.4. When A is a ﬁeld, so A-modules are vector spaces, the only (ﬁnitely gener-
ated) torsion module over A is T = {0}, and each ideal (ai) has to be (1), so cardA(T) = (1).
Example 5.5. Let V = R2, viewed as an R[X]-module with X acting on R2 as the
identity matrix. Then V as an R[X]-module is the direct sum of submodules Re1 ⊕Re2 ∼=
R[X]/(X −1) ⊕R[X]/(X −1), so cardR[X](V ) = (X −1)2 as an ideal in R[X].
Example 5.6. Let V = R2, viewed as an R[X]-module with X acting on R2 as ( 1 1
0 1 ). Then
X(e1) = e1 and X(e2) =
 1
1

= e1 + e2, so {e2, X(e2)} is a basis of R2. Since X2(e2) =
2e1 + e2 = 2(e1 + e2) −e2 = 2X(e2) −e2, so (X2 −2X + 1)(e2) = 0, as an R[X]-module
V ∼= R[X]/(X2−2X +1) = R[X]/(X −1)2. Therefore cardR[X](V ) = (X −1)2, which is the
same ideal as in the previous example. The diﬀerence between R[X]/(X−1)⊕R[X]/(X−1)
and R[X]/(X −1)2 as R[X]-modules is similar to that between Z/(2) × Z/(2) and Z/(4)
as abelian groups, which are nonisomorphic but have the same size.
The ideal cardA(T) need not be the annihilator ideal AnnA(T) = {a ∈A : aT = 0},
which in terms of the cyclic decomposition of T is (lcm(a1, . . . , am)) (see Exercise 10). For
example, the Z-modules in (5.1) have Z-cardinality (300) and annihilator ideal (60), while
the R[X]-modules in (5.2) have R[X]-cardinality (X3−X2) and annihilator ideal (X2−X).
5Aluﬃ[1, Remark 5.8] uses the term “characteristic ideal,” which can be motivated by Exercise 7(a).

<!-- page 16 -->
16
KEITH CONRAD
When A = Z and G is a ﬁnite abelian group, AnnZ(G) is generated by the least positive
integer whose power (or multiple, in additive notation) kills everything in the group and is
traditionally called the exponent of G. The size and exponent of G are equal exactly when
G is cyclic, and likewise cardA(T) = AnnA(T) exactly when T is a cyclic A-module.
Now we show cardA(T) is well-deﬁned. You may want to skip the proof on a ﬁrst reading.
Theorem 5.7. If A/(a1) ⊕· · · ⊕A/(am) ∼= A/(b1) ⊕· · · ⊕A/(bn) as A-modules, where the
ai’s and bj’s are nonzero, then (a1a2 · · · am) = (b1b2 · · · bn) as ideals.
Proof. If A is a ﬁeld then the theorem is obvious (both ideals are (1)), so assume A is
not a ﬁeld: it has irreducible elements.
For each irreducible π in A, we will show the
highest powers of π in a1a2 . . . am and b1b2 · · · bn are equal. Then by unique factorization
(a PID is a UFD) a1a2 . . . am and b1b2 · · · bn are equal up to multiplication by a unit, so
(a1a2 . . . am) = (b1b2 · · · bn).
Set T = A/(a1) ⊕· · · ⊕A/(am). For each irreducible π in A we look at the descending
chain of modules
T ⊃πT ⊃π2T ⊃· · · ⊃πiT ⊃· · ·
The quotient of successive modules πi−1T/πiT is an A-module on which multiplication by
π is 0, so this is an A/(π)-vector space. Since T is ﬁnitely generated, so is πi−1T (multiply
the generators of T by πi−1) and thus so is its quotient πi−1T/πiT, so πi−1T/πiT is a ﬁnite-
dimensional A/(π)-vector space. The dimensions dimA/(π)(πi−1T/πiT) will be the key. We
will show the highest power of π in a1a2 . . . am is P
i≥1 dimA/(π)(πi−1T/πiT).
Step 1: T = A/(a) is a cyclic torsion module.
For i ≥1 we will show when T = A/(a) that
dimA/(π)(πi−1T/πiT) =
(
1,
if πi | a,
0,
otherwise.
Since T is generated as an A-module by 1, πi−1T/πiT is spanned as an A/(π)-vector space
by πi−1, so πi−1T/πiT has dimension ≤1 over A/(π). It is 0-dimensional if and only if
πi−1T = πiT, which is equivalent to πi−1 ∈πiA + (a) = (πi, a). If πi | a then (πi, a) ⊂(πi),
and obviously πi−1 ̸∈(πi), so πi−1T/πiT is 1-dimensional over A/(π). If πi does not divide
a then the greatest common divisor of πi and a is πj for some j ≤i −1, and therefore
πi−1 ∈(πj) = (πi, a). Thus
X
i≥1
dimA/(π)(πi−1T/πiT) = |{i ≥1 : πi | a}|,
which is the highest power of π dividing a. In particular, if π ∤a then the sum is 0.
Step 2: T is a ﬁnitely generated torsion module.
Writing T = A/(a1) ⊕· · · ⊕A/(am), we have an A/(π)-vector space isomorphism
πi−1T/πiT ∼=
m
M
k=1
πi−1(A/(ak))/πi(A/(ak)),
so
dimA/(π)(πi−1T/πiT) =
m
X
k=1
dimA/(π)(πi−1(A/(ak))/πi(A/(ak)))
so summing over all i ≥1 gives us on the right the sum of the highest powers of π in all
ak’s, which is the highest power of π in a1a2 · · · am. So if π ∤a1 · · · am then the sum is 0.

<!-- page 17 -->
MODULES OVER A PID
17
Step 3: Comparing isomorphic cyclic decompositions.
The number dimA/(π)(πi−1T/πiT), which does not depend on a cyclic decomposition, is
unchanged if T is replaced by an isomorphic A-module because an A-module isomorphism
T →T ′ induces an A/(π)-vector space isomorphism πi−1T/πiT →πi−1T ′/πiT ′ in a natural
way. So a1a2 . . . am and b1b2 · · · bn are divisible by the same highest power of π, for all π.
□
Example 5.8. We have cardA(T) = (1) if and only if each ai in a cyclic decomposition is
a unit, which means T = 0.
Example 5.9. For a ∈A−{0}, cardA(A/(a)) = (a). For nonzero a and b, cardA(A/(ab)) =
(ab) = (a)(b) = cardA(A/(a)) cardA(A/(b)).
Example 5.10. When A = Z and G is any of the isomorphic groups in (5.1), which have
A-cardinality (300) = (22 · 3 · 52), let’s recover the multiplicity of 5 in this by looking at
dimZ/5Z(5i−1G/5iG) for i ≥1. We have
G ∼= Z/(3) × Z/(4) × Z/(5) × Z/(5) ∼= Z/(5) × Z/(60)× ∼= Z/(15) × Z/(20)
and
5G ∼= Z/(3) × Z/(4) × (0) × (0) ∼= (0) × 5Z/(60)× ∼= 5Z/(15) × 5Z/(20)
and 5iG = 5G for i ≥2. Then dimZ/5Z(G/5G) = 2 and dimZ/5Z(5i−1G/5iG) = 0 for i ≥2,
so the sum of these dimensions is 2, which is the multiplicity of 5 in 300.
Example 5.11. When A = R[X] and T is an R[X]-module in (5.2), for which cardA(T) =
(X3−X2) = (X2(X−1)), the multiplicity of X in T is the sum of dimR[X]/(X)(Xi−1T/XiT)
for i ≥1. We have
T ∼= R[X]/(X) × R[X]/(X) × R[X]/(X −1) ∼= R[X]/(X2 −X) × R[X]/(X)
and
XT ∼= (0) × (0) × R[X]/(X −1) ∼= XR[X]/(X2 −X) × (0)
and XiT = XT for i ≥2. Then dimR[X]/(X)(T/XT) = 2 and dimR[X]/(X)(Xi−1T/XiT) = 0
for i ≥2, so the sum of the dimensions is 2, which is the multiplicity of X in X3 −X2.
Corollary 5.12. If T is a ﬁnitely generated torsion A-module then cardA(T) ⊂AnnA(T).
Proof. It is obvious from a cyclic decomposition T ∼= A/(a1)⊕· · ·⊕A/(am) that multiplica-
tion by a1a2 · · · am kills T, so a1 · · · am ∈AnnA(T), and therefore cardA(T) ⊂AnnA(T).
□
Theorem 5.13. For two ﬁnitely generated torsion A-modules T1 and T2, cardA(T1 ⊕T2) =
cardA(T1) cardA(T2).
Proof. Combine cyclic decompositions of T1 and T2 to get one for T1 ⊕T2.
□
Some properties of cardA(T) that generalize results about orders of ﬁnite abelian groups
(e.g., Cauchy’s theorem) are in the exercises.
The notion of index, not just cardinality, also generalizes from abelian groups to ﬁnitely
generated modules over a PID.
Deﬁnition 5.14. If M is a ﬁnitely generated module over the PID A with submodule M′
such that M/M′ is a torsion module, we set the A-index of M′ in M to be the A-cardinality
of their quotient:
[M : M′]A = cardA(M/M′).

<!-- page 18 -->
18
KEITH CONRAD
Example 5.15. If M′ ⊂M then M′ = M if and only if [M : M′]A = (1), since M/M′ = 0
if and only if cardA(M/M′) = (1).
Example 5.16. For nonzero a and b in A, [A2 : aA ⊕bA]A = (ab) since A2/(aA ⊕bA) ∼=
A/(a) ⊕A/(b).
Example 5.17. Let A = Z[i],
M = Z[i]2 = Z[i]
1
0

+ Z[i]
0
1

,
and
M′ = Z[i]
3
0

+ Z[i]

0
1 + 2i

= Z[i]3
1
0

+ Z[i](1 + 2i)
0
1

.
Since M/M′ ∼= Z[i]/(3) ⊕Z[i]/(1 + 2i), [M : M′]Z[i] = (3(1 + 2i)).
Using diﬀerent bases for these two modules,
M = Z[i]

3
1 + 2i

+ Z[i]
1 −2i
2

and
M′ = Z[i]

3
1 + 2i

+ Z[i]3(1 + 2i)
1 −2i
2

,
so M/M′ ∼= Z[i]/(3(1 + 2i)). Thus again we compute [M : M′]Z[i] = (3(1 + 2i)).
If M is a ﬁnite free A-module and M′ is a submodule, by Corollary 2.16 the A-index
[M : M′]A is deﬁned if and only if M and M′ have equal rank. This is also true in the
general case (Exercise 8). When A = Z, [M : M′]Z is the subgroup of Z generated by the
positive integer |M/M′|, which is the usual index [M : M′], so the A-index generalizes the
index in group theory.
Theorem 5.18. Let M be a ﬁnitely generated A-module with submodules M′ ⊃M′′ and
assume M/M′′ is a torsion module. Then
[M : M′′]A = [M : M′]A[M′ : M′′]A.
Proof. In terms of A-cardinalities, this says
cardA(M/M′′) = cardA(M/M′) cardA(M′/M ′′).
The ideal cardA(M/M′′) is deﬁned by hypothesis. Since M′/M ′′ is a submodule of M/M′′
and M/M′ is a quotient module of M/M′′, both are ﬁnitely generated torsion modules so
cardA(M/M′) and cardA(M′/M ′′) are both deﬁned.
Setting T = M/M′′ and T ′ = M′/M ′′, the identity we want to prove becomes
cardA(T) = cardA(T ′) cardA(T/T ′),
which is Exercise 9.
□
A ﬁnite free Z-module M looks like Zn, and a submodule M′ also of rank n has ﬁnite
index in M.
We will prove a determinant formula for the index of M′ in M and then
generalize to the case of an arbitrary PID in place of Z.
Theorem 5.19. Let M be a ﬁnite free Z-module with rank n and M′ be a submodule of
M with rank n. Let x1, . . . , xn be a basis of M and y1, . . . , yn be a basis of M′. Writing
yj = Pn
i=1 cijxi with cij ∈Z, the index [M : M′] equals | det(cij)|.

<!-- page 19 -->
MODULES OVER A PID
19
Proof. Our proof will be an application of aligned bases in a ﬁnite free abelian group and
ﬁnite-index subgroup: Theorem 2.14 with A = Z.
The n-tuples x1, . . . , xn and y1, . . . , yn do not have the same Z-span (unless M′ = M),
but morally they should have the same Q-span. To make this idea precise, we transfer
the data of M and M′ into the vector space Qn. Let e1, . . . , en be the standard basis of
Qn and set fj = Pn
i=1 cijei, using the same coeﬃcients that express y1, . . . , yn in terms of
x1, . . . , xn. Identify M with Zn by xi ↔ei (extended by Z-linearity). This isomorphism
identiﬁes yj with fj for all j, so M′ inside M is identiﬁed with the Z-span of f1, . . . , fn
inside Zn.
A Z-linear map Zn →Zn is determined by its eﬀect on the standard basis e1, . . . , en of
Zn. Let ϕ: Zn →Zn be the Z-linear map determined by ϕ(e1) = f1, . . . , ϕ(en) = fn. Then
ϕ(ej) = Pn
i=1 cijei for j = 1, . . . , n, so (cij) is the matrix representation of ϕ with respect
to the standard basis e1, . . . , en of Zn and
ϕ(Zn) = Zϕ(e1) ⊕· · · ⊕Zϕ(en) = Zf1 ⊕· · · ⊕Zfn,
so [M : M′] = [Zn : ϕ(Zn)]. We will show [Zn : ϕ(Zn)] = | det(ϕ)| = | det(cij)|.
The bases e1, . . . , en and f1, . . . , fn of Zn are usually not aligned with each other. By
Theorem 2.14, there is a set of aligned bases for Zn and its submodule ϕ(Zn):
Zn = Zv1 ⊕· · · ⊕Zvn,
ϕ(Zn) = Za1v1 ⊕· · · ⊕Zanvn,
where the ai’s are nonzero integers. Then
Zn/ϕ(Zn) ∼=
n
M
i=1
Z/aiZ,
which tells us
(5.3)
[Zn : ϕ(Zn)] = |a1a2 · · · an| .
We want to prove | det(ϕ)| = |a1a2 · · · an| too.
A Z-linearly independent set of size n in Qn is a Q-basis of Qn, so all four sets {ei},
{ϕ(ei)}, {vi} and {aivi} are Q-bases for Qn. For two Q-bases of Qn there is a unique
Q-linear map Qn →Qn taking one basis to the other. The Q-linear map Qn →Qn taking
ei to ϕ(ei) is the natural extension of ϕ: Zn →Zn from a Z-linear map to a Q-linear map,
so we will also call it ϕ (its matrix representation with respect to the standard basis of Qn
is (cij), just like ϕ as a Z-linear map on Zn). Consider the diagram of Q-linear maps
Qn
ϕ
/
α

Qn
Qn
β
/ Qn
γ
O
where
ei 
ϕ
/
_
α

fi
vi 
β
/ aivi
_
γ
O
This diagram commutes: ϕ = γ ◦β ◦α.
Taking determinants of these Q-linear maps
Qn →Qn,6
(5.4)
det(ϕ) = det(γ) det(β) det(α).
6We are using Q-linear maps throughout because it is nonsense to talk about the determinant of a Z-
linear map Zn →ϕ(Zn) when ϕ(Zn) ̸= Zn: the diﬀerent bases don’t all have the same Z-span but they do
all have the same Q-span.

<!-- page 20 -->
20
KEITH CONRAD
Using the Q-basis {vi} of Qn, the matrix representation [β] is diagonal with ai’s along its
main diagonal, so
det(β : Qn →Qn) = a1a2 · · · an.
What is det(α)? The map α identiﬁes two Z-bases of the same Z-module Zn:
α(c1e1 + · · · + cnen) = c1v1 + · · · + cnvn,
ci ∈Z.
Therefore α is invertible as a Z-linear map of Zn to itself. Using {ei} as the basis in which
a matrix for α is computed, the matrices of α: Qn →Qn over Q and α: Zn →Zn over Z
are the same. Since an invertible Z-linear map Zn →Zn has determinant ±1,
det(α: Qn →Qn) = det(α: Zn →Zn) = ±1.
A similar argument shows
det(γ : Qn →Qn) = det(γ : ϕ(Zn) →ϕ(Zn)) = ±1
since γ identiﬁes two Z-bases of ϕ(Zn). Feeding these determinant formulas into the right
side of (5.4),
(5.5)
det(ϕ) = ±a1a2 · · · an.
Comparing (5.3) and (5.5), |det(ϕ)| = |a1a2 · · · an| = [Zn : ϕ(Zn)] = [M : M′].
□
Example 5.20. Let M = Z[i] = Z + Zi and M′ = (1 + 2i)Z[i] = Z(1 + 2i) + Z(−2 + i). In
Example 2.13, we saw [M : M′] = 5 by ﬁnding aligned Z-bases for M and M′. We will now
compute this index in a new way by using a determinant for a matrix expressing a Z-basis
of M′ in terms of a Z-basis of M that are not aligned bases.
A Z-basis for Z[i] is {1, i} and a Z-basis for (1 + 2i) is {1 + 2i, −2 + i}. The isomorphism
of abelian groups (Z-modules) Z[i] →Z2 where x + yi 7→
 x
y

identiﬁes the ideal (1 + 2i)
with Z
 1
2

+ Z
 −2
1

= ( 1 −2
2
1 )(Z2), so by Theorem 5.19 [M : M′] =
det( 1 −2
2
1 )
 = |5| = 5.
Similarly, for a pure quadratic ring Z[√m] where m is an integer that is not a perfect
square, Z[√m] has Z-basis {1, √m} and a nonzero principal ideal (a + b√m) (for a, b ∈Z
not both 0) has Z-basis {a + b√m, mb + a√m}, so the index [Z[√m] : (a + b√m)] equals
det( a
b
mb a )
 = |a2 −mb2|.
Example 5.21. In the ring Z[
√
10] let a be the ideal (2+5
√
10, 4+7
√
10). We will compute
the index of a in Z[
√
10] as abelian groups using (unaligned) Z-bases for Z[
√
10] and a.
A Z-basis for Z[
√
10] is {1,
√
10}. A Z-basis for a is {2 + 5
√
10, 4 + 7
√
10}, but this
requires veriﬁcation because it is a stronger condition to generate a as a Z-module than to
generate it as an ideal7: the initial deﬁnition of a tells us that
a = Z[
√
10](2 + 5
√
10) + Z[
√
10](4 + 7
√
10)
= (Z + Z
√
10)(2 + 5
√
10) + (Z + Z
√
10)(4 + 7
√
10)
= Z(2 + 5
√
10) + Z(50 + 2
√
10) + Z(4 + 7
√
10) + Z(70 + 4
√
10).
7For example, in Z[i], (17, 3 + 5i) ̸= Z17 + Z(3 + 5i) since the ideal contains 4 + i = 17i −(3 + 5i)(2 + 2i)
but 4 + i ̸= 17a + (3 + 5i)b for integers a and b: look at the imaginary parts.

<!-- page 21 -->
MODULES OVER A PID
21
For a to be spanned over Z by 2 + 5
√
10 and 4 + 7
√
10, we need to write the other two
Z-module generators in terms of them. After some linear algebra, we can do this:
50 + 2
√
10 = −57(2 + 5
√
10) + 41(4 + 7
√
10),
70 + 4
√
10 = −79(2 + 5
√
10) + 57(4 + 7
√
10).
Therefore a = Z(2 + 5
√
10) + Z(4 + 7
√
10) and the numbers 2 + 5
√
10 and 4 + 7
√
10 are
obviously Z-linearly independent, so they are a Z-basis of a. The isomorphism Z[
√
10] →Z2
where x + y
√
10 7→
 x
y

identiﬁes the ideal a with Z
 2
5

+ Z
 4
7

= ( 2 4
5 7 )(Z2), so Theorem
5.19 tells us that the index of a in Z[
√
10] is |det( 2 4
5 7 )| = | −6| = 6. The absolute value is
important: the index is not −6.
Theorem 5.22. Let M be a ﬁnite free module over the PID A with rank n and M′ be a
submodule with rank n. Let x1, . . . , xn be a basis of M and y1, . . . , yn be a basis of M′.
Writing yj = Pn
i=1 cijxi with cij ∈A, (det(cij)) = [M : M′]A. In particular, det(cij) ̸= 0.
Proof. Let K be the fraction ﬁeld of A. If we run through the proof of Theorem 5.19 with
A in place of Z, K in place of Q, and use aligned bases v1, . . . , vn and a1v1, . . . , anvn for
M and M′, with all ai nonzero in A, so M/M′ ∼= Ln
i=1 A/(ai), then the proof of Theorem
5.19 shows det(cij) = det ϕ = ua1 · · · an, where u = det α det γ is a unit in A. The K-linear
operators α and γ on Kn have unit determinant since they are also A-linear operators on
An and ϕ(An) sending a basis to a basis.
By the deﬁnition of A-index, [M : M′]A = cardA(M/M′) = (a1a2 · · · an).
□
Corollary 5.23. Let M be a ﬁnite free A-module with rank n and basis x1, . . . , xn. For
y1, . . . , yn in M, write yj = Pn
i=1 cijxi with cij ∈A. Then y1, . . . , yn is linearly independent
if and only if det(cij) ̸= 0.
Proof. If y1, . . . , yn is a linearly independent set, then its A-span in M is a free A-submodule
of rank n, so det(cij) ̸= 0 by Theorem 5.22.
Conversely, if det(cij) ̸= 0, then we want to show an A-linear relation Pn
j=1 cjyj = 0 with
cj ∈A must have all cj equal to 0. Writing yj in terms of the xi’s,
0 =
n
X
j=1
cjyj =
n
X
j=1
cj
 n
X
i=1
cijxi
!
=
n
X
i=1


n
X
j=1
cijci

xi,
so looking at the coeﬃcients of x1, . . . , xn tells us Pn
j=1 cijci = 0 for all i. As a matrix
equation this says





c11
c21
. . .
cn1
c12
c22
. . .
cn2
...
...
...
...
c1n
c2n
. . .
cnn










c1
c2
...
cn




=





0
0
...
0




.
This is an equation in An ⊂Kn, where K is the fraction ﬁeld of A. The matrix is the
transpose of (cij). Since det((cji)⊤) = det(cij) ̸= 0 the vector vanishes, so all ci are 0.
□
Corollary 5.24. If M is a ﬁnite free module over the PID A with basis x1, . . . , xn, a set
of n elements y1, . . . , yn in M is a basis of M if and only if the matrix (cij) expressing the
y’s in terms of the x’s has unit determinant.

<!-- page 22 -->
22
KEITH CONRAD
Proof. If y1, . . . , yn is a basis of M then (det(cij)) = [M : M]A = (1) by Theorem 5.22,
so det(cij) ∈A×. Conversely, if det(cij) ∈A× then y1, . . . , yn is linearly independent by
Corollary 5.23 and the A-index of P Ayj in M is (det(cij)) = (1), so P Ayj = M.
□
Example 5.25. The Z-span of
 2
2

,
 3
6

, and
 0
5

is Z2 since
 1
0

= −4
 2
2

+ 3
 3
6

−2
 0
5

and
 0
1

= 12
 2
2

−8
 3
6

+ 5
 0
5

, but no 2-element subset is a Z-basis since det ( 2 3
2 6 ) = 6,
det ( 2 0
2 5 ) = 10, and det ( 3 0
6 5 ) = 15. This is a rank-2 analogue of Remark 2.5.
Example 5.26. A set of n vectors v1, . . . , vn in Zn is a basis of Zn if and only if the matrix
(v1 v2 · · · vn) with the v’s as the columns has determinant ±1, since this matrix expresses
v1, . . . , vn in terms of the standard basis of Zn.
The deﬁnition of the ideal cardA(T) for a torsion module T was based on a decomposition
of T as a direct sum of cyclic A-modules. To prove cardA(T) is well-deﬁned (i.e., it is
independent of the choice of cyclic decomposition of T), the proof in Theorem 5.7 gave a
formula for the multiplicity of each prime π in cardA(T) that makes no reference to a cyclic
decomposition of T: that multiplicity is
X
i≥1
dimA/(π)(πi−1T/πiT),
where each quotient module πi−1T/πiT is a vector space over the ﬁeld A/(π), and the sum
is ﬁnite since the ith term is 0 for large enough i (depending on T). This suggests the
following weaker notion of size for ﬁnitely generated torsion modules.
Deﬁnition 5.27. For a ﬁnitely generated torsion module T over the PID A, set the primary
cardinality of T to be
ωA(T) =
X
(π)
dimA/(π)(T/πT) ∈{0, 1, 2, 3, . . .}
where the sum runs over all nonzero prime ideals (π) of A.
Example 5.28. Let A = Z and T = Z/100Z ∼= Z/4Z ⊕Z/25Z.
If p is 2 or 5 then
T/pT = (Z/100Z)/(pZ/100Z) ∼= Z/pZ, so dimZ/(p)(T/pT) = 1. If p is a prime other than
2 or 5 then pT = T (p is invertible modulo 100), so T/pT = 0 and dimZ/(p)(T/pT) = 0.
Thus
ωZ(Z/100Z) =
X
prime p
dimZ/(p)(T/pT) = dimZ/(2)(T/2T) + dimZ/(5)(T/5T) = 1 + 1 = 2.
For general n ≥1, ωZ(Z/nZ) is the number of prime factors of n, which explains the name
“primary cardinality” for ωA(T). (In number theory, ω(n) is the standard notation for the
number of prime factors of n.) The multiplicity of the prime factors of n does not play
a role in ωZ(Z/nZ). For example, if we run through the same calculation for Z/10Z and
10Z/100Z (both cyclic of order 10) then ωZ(Z/10Z) = 2 and ωZ(10Z/100Z) = 2. So unlike
the ordinary notion of size, a ﬁnite abelian group and a proper subgroup (like Z/100Z and
its subgroup 10Z/100Z) could have the same primary cardinality.
In the sum deﬁning ωA(T), each term dimA/(π)(T/πT) is ﬁnite: since T as an A-module
is ﬁnitely generated, T/πT as an A/(π)-vector space is ﬁnite dimensional. The following
lemma explains why the sum deﬁning ωA(T) has only ﬁnitely many nonzero terms.

<!-- page 23 -->
MODULES OVER A PID
23
Theorem 5.29. Let T be a ﬁnitely generated torsion A-module. The ideal AnnA(T) =
{a ∈A : aT = 0} is not (0) and dimA/(π)(T/πT) > 0 if and only if π | AnnA(T), which
occurs for only ﬁnitely many prime ideals (π).
In the paragraph following Example 5.6, we saw AnnA(T) ̸= (0) by a formula for this
ideal in terms of a cyclic decomposition of T . The point of reproving AnnA(T) ̸= (0) again
is to see it can be done without relying on a cyclic decomposition.
Proof. To show AnnA(T) ̸= (0) we will use a ﬁnite spanning set of T as an A-module, say
{t1, . . . , tk}. Since each element of T is an A-linear combination of t1, . . . , tk, for a ∈A we
have aT = {0} if and only if at1 = 0, . . . , atk = 0. Since T is a torsion module, each of
t1, . . . , tk is killed by some nonzero element of A, and the product of such elements is a single
nonzero element of A killing all of t1, . . . , tk and thus killing all of T. Thus AnnA(T) ̸= (0).
The ideal AnnA(T) is principal, so it has a generator that is not 0, say AnnA(T) = (α).
We will show dimA/(π)(T/πT) > 0 if and only if π | α, or equivalently dimA/(π)(T/πT) = 0
if and only if π ∤α.
If π ∤α then (α, π) = (1) since π is prime, so αx + πy = 1 for some x and y in A. Thus
for each t ∈T, t = (αx + πy)t = x(αt) + π(yt) = π(yt) since αt = 0. This shows T ⊂πT,
and the reverse containment is obvious, so πT = T and thus T/πT = 0.
If π | α, write α = πα′. Then α′ ̸∈(α) (since α ∤α′), so α′T ̸= {0}: for some t ∈T we
have α′t ̸= 0. We can’t have t ∈πT since then α′t ∈α′πT = αT = {0}, which isn’t true.
So T/πT ̸= {0}.
We have dimA/(π)(T/πT) > 0 if and only if T/πT ̸= 0, and we showed that is the same
as π | α. A nonzero element of A has only ﬁnitely many prime factors up to unit multiple,
so π | α for only ﬁnitely many prime ideals (π).
□
Corollary 5.30. We have ωA(T) = 0 if and only if T = 0.
Proof. Obviously if T = 0 then ωA(T) = 0. Conversely, if ωA(T) = 0 then for all prime
elements π we have dimA/(π)(T/πT) = 0, so T = πT. By Theorem 5.29, the ideal AnnA(T)
has no prime factors, so AnnA(T) = (1). That 1 ∈AnnA(T) implies 1·T = 0, so T = 0.
□
Theorem 5.31. For ﬁnitely generated torsion A-modules T1 and T2, ωA(T1⊕T2) = ωA(T1)+
ωA(T2).
Proof. For each prime π, π(T1 ⊕T2) = πT1 ⊕πT2, so (T1 ⊕T2)/π(T1 ⊕T2) ∼= (T1/πT1) ⊕
(T2/πT2). Isomorphic vector spaces have the same dimension, so
dimA/(π)(T1 ⊕T2)/π(T1 ⊕T2) = dimA/(π)((T1/πT1) ⊕(T2/πT2))
= dimA/(π)(T1/πT1) + dimA/(π)(T2/πT2),
and summing over all (π) gives us ωA(T1 ⊕T2) = ωA(T1) + ωA(T2).
□
Example 5.32. For a ∈A −{0}, A/(a) is isomorphic to a direct sum of cyclic modules of
the form A/(πk) for prime π by the Chinese remainder theorem:
a = uπk1
1 · · · πkr
r =⇒A/(a) ∼= A/(πk1
1 ) ⊕· · · ⊕A/(πkr
r ),
where u ∈A× and π1, . . . , πr are nonassociate primes in A. So each nonzero ﬁnitely gener-
ated torsion A-module T is isomorphic to a direct sum of cyclic torsion A-modules:
T ∼= A/(πe1
1 ) ⊕· · · ⊕A/(πen
n ),

<!-- page 24 -->
24
KEITH CONRAD
where π1, . . . , πn are prime and e1, . . . , en are positive integers. (The primes could be the
same when T is not cyclic, e.g., (Z/15Z)× = ⟨2 mod 15⟩⊕⟨−1 mod 15⟩∼= Z/4Z ⊕Z/2Z.)
By Theorem 5.31, ωA(T) = Pn
j=1 ωA(A/(πej
j )). We have ωA(A/(πej
j )) = 1, so ωA(T) =
n.
Thus we have a concrete interpretation for ωA(T): it is the number of terms in a
decomposition of T as a direct sum of cyclic modules having a prime-power annihilator
ideal (AnnA(A/(πe)) = (πe) when π is prime). For instance, if a ﬁnite abelian group G is
expressed as a direct sum of cyclic abelian groups of prime-power order then ωZ(G) is the
number of direct summands, e.g., ωZ((Z/15Z)×)) = ωZ((Z/4Z) ⊕Z/2Z) = 2.
Exercises.
1. Let A be a nonzero commutative ring. Show that if every submodule of every ﬁnite
free A-module is a free A-module, then A is a PID.
2. Suppose A is a PID and π is irreducible in A. Inside A2, set
M = A
1
0

+ A
 0
π2

=
x
y

: y ≡0 mod π2

and
N = A
π
0

+ A
1
π

=
x
y

: y ≡0 mod π, πx ≡y mod π2

.
a) Find a basis {e1, e2} of A2 and a1 and a2 in A such that {a1e1, a2e2} is a basis
of N. (Such an aligned pair of bases obviously exists for A2 and M.)
b) Show there is no basis {e1, e2} of A2 and a1, a2, b1, b2 in A such that {a1e1, a2e2}
is a basis of M and {b1e1, b2e2} is a basis of N. That is, the submodules M and N
of A2 do not admit bases simultaneously aligned with a single basis of A2.
3. Let A be a PID, M be a ﬁnite free A-module, and N be a submodule. Consider the
following conditions on M and N:
(i) the quotient module M/N is torsion-free,
(ii) every A-basis of N extends to an A-basis of M,
(iii) some A-basis of N extends to an A-basis of M.
Corollary 2.9 shows (i) implies (ii), and trivially (ii) implies (iii). Prove (iii) implies
(i), so the three conditions are equivalent.
4. If M is a ﬁnitely generated module over a PID A and M′ is a submodule, is it
always possible to align their decompositions into free parts and torsion parts: can
we write M = F ⊕T and M′ = F ′ ⊕T ′ such that F and F ′ are free, T and T ′
are torsion, and F ′ ⊂F and T ′ ⊂T? If A is not a ﬁeld, show the answer is no by
picking an irreducible π in A and using M = A ⊕A/(π) and M′ = A(π, 1). (Hint:
ﬁrst show M′ is free.)
5. Let A be a PID.
a) Prove an analogue of Cauchy’s theorem from group theory: for a ﬁnitely
generated torsion A-module T and irreducible π in A such that π divides cardA(T),
meaning π divides a generator of the ideal cardA(T), show there is some t ∈T with
“order” π: the annihilator ideal AnnA(t) = {a ∈A : at = 0} is πA.
b) Let T and T ′ be ﬁnitely generated torsion A-modules such that cardA(T) =
cardA(T ′). If f : T →T ′ is an A-linear map, show f is one-to-one if and only if it is
onto. (When A = Z this is the familiar statement that a homomorphism between
ﬁnite abelian groups of equal size is one-to-one if and only if it is onto.)

<!-- page 25 -->
MODULES OVER A PID
25
c) Show a ﬁnitely generated A-module M is a torsion module if and only if there
is some a ̸= 0 in A such that aM = 0. (This is false without a hypothesis of ﬁnite
generatedness, e.g., Q/Z is a torsion abelian group and for all nonzero integers a
we have a(Q/Z) = Q/Z.)
d) For a ﬁnitely generated A-module M and submodule N, show M/N is a torsion
module if and only if there is some a ̸= 0 in A such that aM ⊂N.
6. Let A be a PID and R be a commutative ring containing A such that R is a ﬁnite free
A-module. Prove there is an A-basis of R that contains 1. (Hint: Let e1, . . . , en be
an A-basis of R and write 1 = Pn
i=1 ciei and d = gcd(c1, . . . , cn). Prove ϕ(R) ⊂dA
for all A-linear maps ϕ: R →A.
Deduce that d = 1 and then that there’s an
A-linear map ϕ: R →A such that ϕ(1) = 1. Conclude from the method of proof of
Theorem 2.14 that R = A ⊕N for an A-submodule N of R. )
7. Let V be a ﬁnite-dimensional vector space over a ﬁeld K and f : V →V be an
K-linear operator. Write Vf for V as a K[X]-module where X acts on V as f:
Xv = f(v) for v ∈V .
a) Show cardK[X](Vf) = (χf(X)), where χf is the characteristic polynomial of f.
b) If χf(X) decomposes into linear factors in K[X], so all the eigenvalues of f
are in K and we can ﬁnd a matrix for f in Jordan canonical form, show ωK[X](Vf)
is the number of Jordan blocks in that matrix.
8. For a pair of ﬁnitely generated A-modules M ⊃M′, show M/M′ is a torsion module
if and only if M and M′ have the same rank (that means the free parts of M and
M′ have equal rank). This generalizes Corollary 2.16 in the case of free modules.
9. Let T be a ﬁnitely generated torsion module over the PID A and T ′ be a submodule.
Show cardA(T) = cardA(T ′) cardA(T/T ′). In particular, if cardA(T ′) = cardA(T)
then cardA(T/T ′) = (1), so T/T ′ = {0} (Example 5.3) and thus T ′ = T, so if T ′ is
strictly contained in T then cardA(T) ⊊cardA(T ′).
10. Let T be a ﬁnitely generated torsion module over the PID A. Write a cyclic decom-
position of T as A/(a1) ⊕· · · A/(am) for nonzero ai in A.
a) Show AnnA(T) = (lcm(a1, . . . , am)).
b) For t and t′ in T, let AnnA(t) = (a) and AnnA(t′) = (a′). Show there is an
A-linear combination of t and t′ whose annihilator ideal is (lcm(a, a′)). (Hint: when
A = Z, this becomes the fact from group theory that in a ﬁnite abelian group, if g
has order m and h has order n, then some element of ⟨g, h⟩has order lcm(m, n).)
c) Using (a) and (b), show there is a t0 ∈T such that AnnA(t0) = AnnA(T).
(Hint: when A = Z, this is the statement that in a ﬁnite abelian group, the least
common multiple of the orders of its elements is the order of some element of the
group.)
11. Prove Corollaries 5.23 and 5.24 if A is an integral domain, not necessarily a PID.
References
[1] P. Aluﬃ, Algebra: Chapter 0, Amer. Math. Soc., Providence, 2009.
[2] H. Cohen and H. W. Lenstra, Jr., “Heuristics on class groups of number ﬁelds,” pp. 33–62 in Number
theory, Noordwijkerhout 1983, Springer Lecture Notes in Mathematics 1068, Springer-Verlag, Berlin,
1984.
[3] S. Roman, Advanced Linear Algebra, 2nd ed., Springer-Verlag, New York, 2005.
[4] J. Rotman, An Introduction to the Theory of Groups,4th ed., Springer-Verlag, NY, 1995.
[5] J. Rotman, Advanced Modern Algebra, Prentice-Hall, Upper Saddle River, NJ, 2002.
[6] P. Samuel, Algebraic Theory of Numbers, Dover, 2008.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*