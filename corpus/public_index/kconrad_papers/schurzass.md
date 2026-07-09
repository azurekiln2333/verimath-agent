# Schur-Zassenhaus Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/schurzass.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE SCHUR–ZASSENHAUS THEOREM
KEITH CONRAD
When N is a normal subgroup of G, can we reconstruct G from N and G/N? In general,
no. For instance, the groups Z/(p2) and Z/(p) × Z/(p) (for prime p) are nonisomorphic,
but each has a cyclic subgroup of order p and the quotient by it is cyclic with order p. As
another example, the nonisomorphic groups Z/(2p) and Dp (for odd prime p) have a normal
subgroup that is cyclic of order p, whose quotient is cyclic of order 2.
If we impose the condition that N and G/N have relatively prime order, then something
nice can be said: G is a semidirect product of N and G/N. This follows from the Schur-
Zassenhaus theorem, which is discussed below. It doesn’t uniquely determine G, as there
can be several non-isomorphic semi-direct products of the abstract groups N and G/N.
Also, G might not even be a semi-direct product of nontrivial groups: Q8 is an example of
that.
Theorem 1 (Schur-Zassenhaus). Let G be a ﬁnite group and write |G| = ab where (a, b) =
1. If G has a normal subgroup of order a then it has a subgroup of order b.
Letting N be the normal subgroup of order a and H be a subgroup of order b, the Schur-
Zassenhaus theorem implies G is a semidirect product of N and H: N ∩H is trivial since
(a, b) = 1, so G = NH ∼= N ⋊H where H acts on N by conjugation.
Here are two cases where the Schur-Zassenhaus theorem has proofs using no hard work.
Example 2. If G/N is cyclic (for instance, if N has prime index in G) then it is simple to
prove the Schur-Zassenhaus theorem, as follows. Let |N| = a, [G : N] = b, and G/N = ⟨g⟩.
Since a is relatively prime to b, which is the order of G/N, G/N = ⟨ga⟩too. Since G has
order ab, in G we have
1 = gab = (ga)b.
Set x = ga, so xb = 1 and G/N = ⟨x⟩. Then each element of G has the form xin for some
i ∈Z and n ∈N. The subgroup ⟨x⟩has order dividing b, which is relatively prime to
a = |N|, so ⟨x⟩∩N = {1}. Thus G = N⟨x⟩with the subgroups N and ⟨x⟩having trivial
intersection. Thus ab = |G| = |N||⟨x⟩| = a|⟨x⟩|, so |⟨x⟩| = b: x generates a subgroup of G
with order b.
Example 3. If G is abelian then it is also simple to prove the Schur-Zassenhaus theorem,
since power functions on abelian groups are homomorphisms. Let f : G →G by f(g) = gb.
Since (b, |N|) = 1, f restricts to an isomorphism N →N, so N ⊂f(G). Since (gb)a =
gab = 1 for all g ∈G, all elements of f(G) have order dividing a, so relative primality of
a and b implies (|f(G)|, b) = 1 (Cauchy’s theorem). Since |f(G)| | |G|, we get |f(G)| | a.
Also a | |f(G)| since N = f(N) is a subgroup of f(G). Thus |f(G)| = a, so f(G) = N. Let
H = ker f, so G/H ∼= f(G) = N. Thus |H| = |G|/|N| = b.
In the general case we will present two proofs of the Schur–Zassenhaus theorem that are
incomplete at the end. Each proof will reduce to the case when N is abelian, at which point
the machinery of group cohomology can be applied. While group cohomology provides a
1

<!-- page 2 -->
2
KEITH CONRAD
general tool to describe the groups having a particular normal subgroup with a particular
quotient group (up to isomorphism), it requires the normal subgroup to be abelian, and the
Schur-Zassenhaus theorem makes no such assumption about N. Thus the part of the proof
of the Schur-Zassenhaus theorem presented here amounts to a reduction to the case when
N is abelian.
The ﬁrst (partial) proof of the Schur–Zassenhaus theorem will use the following lemma.
Lemma 4. If N ◁G and P ∈Sylp(N) then G = N · NG(P). In particular, if P ◁N then
P ◁G.
Proof. Pick g ∈G. Since P ⊂N and N ◁G, gPg−1 ⊂N. Then by Sylow II for the
group N, there is an n ∈N such that gPg−1 = nPn−1, so n−1gPg−1n = P. That means
n−1g ∈NG(P), so g ∈n NG(P). Thus G = N · NG(P).
If P ◁N then N ⊂NG(P), so N · NG(P) = NG(P). Thus G = NG(P), so P ◁G.
□
Here is our ﬁrst proof of the Schur–Zassenhaus theorem (incomplete at the end).
Proof. Assume the theorem is false and let G be a counterexample of minimal order. So
any group with order less than |G| satisﬁes the theorem. Easily a > 1 and b > 1.
Let N ◁G with |N| = a > 1. We aim to get a contradiction.
Step 1: Show N is a minimal normal subgroup of G: there are no normal subgroups of
G lying strictly between {e} and N.
Suppose N′ ◁G with {e} ⊂N′ ⊂N and N′ ̸= {e} or N. The group G/N′ has order
< |G|. Since N/N′ ◁G/N′ and |G/N′| = |N/N′|b with the two factors being relatively
prime, by minimality of G there is a subgroup of G/N′ with order b. That subgroup has
the form K/N′, so |K| = |N′|b < ab. Since |N′| and b are relatively prime, by minimality
of G there is a subgroup of order b in K and hence in G. This is a contradiction, so N′
doesn’t exist.
Step 2: Show N is an abelian p-group.
Let P be a nontrivial Sylow subgroup of N, so by Lemma 4 we have G = N NG(P). Then
G/N ∼= NG(P)/(N ∩NG(P)) and the order of NG(P) is |N ∩NG(P)|b with |N ∩NG(P)|
being a factor of a (so it is relatively prime to b). Since N ∩NG(P) is normal in NG(P), if
NG(P) is a proper subgroup of G then by minimality of G there is a subgroup of order b
in NG(P), and hence in G. This is impossible, so NG(P) = G. Thus P ◁G. Since P is in
N, P is a normal subgroup of N, so P = N by Step 1. Then Z(P) is a nontrivial normal
subgroup of P, so Z(P) = P by Step 1 again, which means N is an abelian p-group.
Step 3: Show N ∼= (Z/(p))k for some k ≥1.
Since N is abelian by Step 2, Np = {xp : x ∈N} is a subgroup of N. By the structure of
ﬁnite abelian p-groups, (i) this step is equivalent to showing Np is trivial and (ii) |Np| < |N|.
Since Np is preserved as a set by all group automorphisms of N, gNpg−1 = Np for all g ∈G.
Thus Np ◁G, so also Np ◁N. By Step 1, Np is trivial. (I thank David Leep for showing
me how simplify this step compared to an earlier version.)
Step 4: Get a ﬁnal contradiction.
Let G act on N by conjugation. Since N ∼= (Z/(p))k, automorphisms of N can be in-
terpreted as elements of GLk(Z/(p)). Therefore the conjugation action of G on N is a
group homomorphism G →Aut(N) ∼= GLk(Z/(p)). Since N is abelian, it acts trivially on
itself, so our action descends to a homomorphism G/N →GLk(Z/(p)). At this point the
reader is referred to the literature for the rest of the proof. Two possible approaches use

<!-- page 3 -->
THE SCHUR–ZASSENHAUS THEOREM
3
transversals and Maschke’s theorem [2, p. 146] or group cohomology. The method using co-
homology amounts to showing the second cohomology group H2(G/N, N) is trivial because
(|G/N|, |N|) = 1; a cohomological neophyte can ﬁnd that done without any reference to
cohomology in [3, pp. 253–255], but it is not very illuminating.
□
Here is a second proof of the Schur–Zassenhaus theorem, also incomplete at the end.
Again we will reduce to the case of an abelian normal subgroup.
Proof. Let N ◁G with |N| and [G : N] relatively prime. We want to prove G has a subgroup
of order [G : N]. Of course we can assume N is a nontrivial proper subgroup of G.
We induct on |G|. Assume |G| > 1 and the theorem is veriﬁed for subgroups with smaller
order. Let p be a prime factor of |N| and P be a p-Sylow subgroup of N, so P is nontrivial.
Because [G : N] is prime to |N|, p does not divide [G : N] so P is also a p-Sylow subgroup
of G. Since P ⊂N and N ◁G, all G-conjugates of P are in N. Therefore all the p-Sylow
subgroups of G are in N, hence by counting p-Sylows in G and in N we get
[G : NG(P)] = [N : NG(P) ∩N].
Writing these indices as ratios and rearranging terms,
(1)
[G : N] = [NG(P) : NG(P) ∩N].
Case 1: P is not normal in G. Then NG(P) is a proper subgroup of G. The group
NG(P) ∩N is normal in NG(P) since N ◁G, the order of NG(P) ∩N divides |N|, and
the index of NG(P) ∩N in NG(P) is [G : N] by (1), so NG(P) and its normal subgroup
NG(P)∩N satisfy the hypotheses of the theorem. Since | NG(P)| < |G|, by induction NG(P)
has a subgroup of order [NG(P) : NG(P) ∩N] = [G : N]. This is a subgroup of G too, so
we’re done.
Case 2: P ◁G. Then P ◁N and N/P ◁G/P with |N/P| dividing |N| and [G/P :
N/P] = [G : N].
This order and index are relatively prime, and |G/P| < |G|, so by
induction the theorem holds for G/P and its subgroup N/P: there is a subgroup in G/P
of order [G/P : N/P] = [G : N]. Write the subgroup as H/P, so H is a subgroup of G and
(2)
[H : P] = |H/P| = [G : N]
is not divisible by p. (If P = N then H = G.)
Since P is a nontrivial p-group, its center Z := Z(P) is nontrivial. Also Z ◁H (the
center of a normal subgroup is also a normal subgroup), so P/Z ◁H/Z. The group P/Z is
a p-group (possibly trivial, if P is abelian) while [H/Z : P/Z] = [H : P] = [G : N] is prime
to p, so (since |H/Z| < |H| ≤|G|) by induction H/Z contains a subgroup K/Z of order
[H : P]. (If P is abelian then K = H.)
Now we have Z ◁K with Z a p-group and
[K : Z] = |K/Z| = [H : P] = [G : N]
being prime to p, so K and its normal subgroup Z satisfy the hypotheses of the theorem.
Now if |K| < |G| then we can apply induction to conclude K has a subgroup of order
[K : Z] = [G : N], and this is also a subgroup of G, so we’re done. What if K = G? Since
K ⊂H ⊂G, if K = G then H = G so [G : P] = [G : N] by (2). Therefore N = P since
P ⊂N, so N is a normal Sylow subgroup of G.
If N is a normal p-Sylow in G and it is not abelian, we can use induction yet again to
ﬁnish the proof. Run through the argument two paragraphs up (with P = N, H = G,
and Z = Z(P) = Z(N) the center of N). We get a subgroup K/Z of G/Z with order

<!-- page 4 -->
4
KEITH CONRAD
[G : N]. Now |K| = |Z|[G : N]. If Z ̸= N (i.e., N is non-abelian) then |Z| < |N| so
|K| < |N|[G : N] = |G| and we are done as before.
What if N is normal in G and N is abelian? In this case we can, as in the previous proof,
consider the subgroup Np = {x ∈N : xp = 1}. This is a normal subgroup of N and in fact
it is normal in G too. By running through the previous paragraph with Np in place of Z,
we will be done by induction unless Np = {1},1 which means all the elements of N have
order p. So we are left to contemplate the same case as at the end of the ﬁrst proof: N is
a normal p-Sylow subgroup of G and is isomorphic to (Z/(p))k for some k. Details for this
case are the same as in the ﬁrst proof.
□
Remark 5. The Schur–Zassenhaus theorem has an important second part, which we omit-
ted: any two subgroups of order b in G are conjugate to each other. See [3, p. 254–255] for
the proof of that.
Let’s put the Schur–Zassenhaus theorem to work. We ask, out of idle curiosity, whether
p | |G| implies p | | Aut(G)|. The answer, of course, is no: try G = Z/(p). As we now show,
this counterexample essentially explains all the others.
Corollary 6. Fix a prime p. For a ﬁnite group G with order divisible by p, the following
are equivalent:
(1) | Aut(G)| is not divisible by p,
(2) G ∼= Z/(p) × H where |H| and | Aut(H)| are not divisible by p.
In particular, if p2 | |G| then p | | Aut(G)|.
Proof. Assume (1) holds and let P be a p-Sylow subgroup of G. We expect to show G ∼=
P × H and P ∼= Z/(p).
For any x ∈P there is the automorphism γx ∈Aut(G) that is conjugation by x. Since
x has p-power order, so does γx (recall γn
x = γxn for all n). By hypothesis | Aut(G)| is
not divisible by p, so the only element of p-power order in Aut(G) is the identity. Thus
γx = idG for all x ∈P, which means P ⊂Z(G). In particular, P ◁G by Sylow II and P
is abelian. Therefore the Schur-Zassenhaus theorem tells us G ∼= PH for some subgroup H
with order not divisible by p. Since P ⊂Z(G), G ∼= P × H. Because the groups P and H
have relatively prime order and commute in G, Aut(G) ∼= Aut(P) × Aut(H) in the natural
way. Therefore p doesn’t divide | Aut(P)| or | Aut(H)|.
Which ﬁnite abelian p-groups P have | Aut(P)| not divisible by p? Write P as a direct
product of cyclic groups, say
P = Z/(pr1) × · · · × Z/(prk).
Since Aut(Z/(pr)) ∼= (Z/(pr))× has order pr−1(p −1), we see that if some ri > 1 then that
Z/(pri) has an automorphism of order p, so P does as well (act by the chosen automorphism
on the i-th factor and ﬁx elements in the other factors). Thus, if | Aut(P)| is not divisible
by p we must have ri = 1 for all i, so P ∼= (Z/(p))k is a direct sum of copies of Z/(p). That
1Assume N p ̸= {1}. We have N p ◁G since gN pg−1 = N p for all g ∈G, so N/N p ◁G/N p where N/N p
is a nontrivial abelian p-group and it is normal in G/N p since N ◁G. Since [G/N p : N/N p] = [G : N]
is relatively prime to p and |G/N p| < |G|, with all groups of smaller order than G satisfying the Schur–
Zassenhaus theorem, G/N p contains a subgroup M/N p of order [G : N]. Then M and its normal subgroup
N p satisfy the hypotheses of the Schur-Zassenhaus theorem and |M| < |G| since p ∤|M/N p| while p | |G/N p|
due to |N/N p| being a p-power bigger than 1. Thus M has a subgroup S such that |S| = [M : N p] = [G : N],
so S is a subgroup of G with order [G : N]. It remains to handle the case where N p = {1}.

<!-- page 5 -->
THE SCHUR–ZASSENHAUS THEOREM
5
means Aut(P) ∼= GLk(Z/(p)), whose order is divisible by pk(k−1)/2, and thus is divisible by
p unless k = 1. So we must have P ∼= Z/(p), which concludes the proof that (1) implies (2).
To show (2) implies (1), Aut(Z/(p) × H) ∼= Aut(Z/(p)) × Aut(H) ∼= (Z/(p))× × Aut(H),
and this has order not divisible by p since | Aut(H)| is not divisible by p.
□
Example 7. If |G| is even and | Aut(G)| is odd then G ∼= Z/(2) × H where H is a group
of odd order with Aut(H) of odd order too. The smallest example where |H| > 1 has
|H| = 729 = 36 and | Aut(G)| = 19683 = 39.
When p | | Aut(G)|, one way to search for elements of order p in Aut(G) is by looking for
an inner automorphism: if g ∈G has order p and g is not in the center of G then conjugation
by G is an (inner) automorphism of G with order p. Since inner automorphisms are a cheap
construction, we ask: when are there non-inner automorphisms of order p, assuming that
we know p | | Aut(G)| (and p | |G|)? For p-groups there is a complete answer. When G
is a ﬁnite abelian p-group, it has an automorphism of order p as long as G ̸∼= Z/(p), and
that automorphism is not inner since G is abelian. When G is a ﬁnite non-abelian p-group,
Gatsch¨utz [1] showed that there is an automorphism of order p that is not inner by using
cohomology.
References
[1] W. Gatsch¨utz, Nichtabelsche p-Gruppen besitzen ¨aussere p-Automorphismen, J. Algebra 4 (1966), 1–2.
[2] M. I. Kargapolov and Y. I. Merzlyakov, “Fundamentals of the Theory of Groups,” Springer–Verlag, New
York, 1979.
[3] D. J. S. Robinson, “A Course in the Theory of Groups,” 2nd ed., Springer-Verlag, New York, 1996.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*