# Subgpseries2

> **Source**: https://kconrad.math.uconn.edu/blurbs/subgpseries2.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SUBGROUP SERIES II
KEITH CONRAD
1. Introduction
In part I, we met nilpotent and solvable groups, deﬁned in terms of normal series. Re-
calling the deﬁnitions, a group G is called nilpotent if it admits a normal series
(1.1)
{e} = G0 ◁G1 ◁G2 ◁· · · ◁Gr = G
in which Gi ◁G and Gi+1/Gi ⊂Z(G/Gi) for all i. We call G solvable if it admits a normal
series (1.1) in which Gi+1/Gi is abelian for all i. Every nilpotent group is solvable.
Nilpotent groups include ﬁnite p-groups. Some theorems about p-groups extend to nilpo-
tent groups (e.g., all nontrivial normal subgroups of a nilpotent group have a nontrivial
intersection with the center). Nilpotency for ﬁnite groups has many characterizations.
Theorem 1.1. For a nontrivial ﬁnite group G, the following are equivalent to nilpotency:
(1) for every proper subgroup H, H ̸= N(H),
(2) every subgroup of G is subnormal,
(3) every nontrivial quotient group of G has a nontrivial center,
(4) elements of relatively prime order in G commute,
(5) if d | |G| then there is a normal subgroup of size d,
(6) the group is isomorphic to the direct product of its Sylow subgroups.
We will meet other characterizations in Corollary 2.3 and Theorem 3.13.
In Section 2 we will look at the subgroup structure of nilpotent and solvable groups. Sec-
tion 3 discusses two important nilpotent subgroups of a ﬁnite group: the Fitting subgroup
and Frattini subgroup. In Section 4 we will meet supersolvable groups, which are a class
of groups intermediate between nilpotent and solvable groups. In Section 5 we will discuss
chief series, which are analogous to composition series and in terms of which nilpotent and
supersolvable groups can be characterized. (While solvability can be deﬁned in terms of
composition series, that isn’t true of nilpotency and supersolvability.)
2. Nilpotent and solvable groups: subgroup structure
Nilpotent and solvable groups have special features concerning their minimal normal
subgroups and maximal subgroups.
A minimal normal subgroup is a nontrivial normal
subgroup that contains no other nontrivial normal subgroup. A maximal subgroup is a
proper subgroup not contained in another proper subgroup. Nontrivial ﬁnite groups ob-
viously have minimal normal subgroups and maximal subgroups. But an inﬁnite abelian
(hence nilpotent and solvable) group need not contain minimal normal subgroups (try Z)
or maximal subgroups (try Q1.).
1See Example 2.2 in https://kconrad.math.uconn.edu/blurbs/zorn1.pdf
1

<!-- page 2 -->
2
KEITH CONRAD
Remark 2.1. Maximal normal subgroups naturally arise when constructing a composition
series for a nontrivial ﬁnite group: let G0 be G, G1 be a maximal normal subgroup of G0, G2
be a maximal normal subgroup of G1 (probably G2 is not normal in G), G3 be a maximal
normal subgroup of G2, and so on. When the process terminates at {e} we will have a
composition series where the subgroups descend rather than ascend as in (1.1).
Theorem 2.2. If G is a nontrivial nilpotent group then
(1) every minimal normal subgroup has prime order and lies in the center,
(2) every maximal subgroup M is normal with prime index and contains the commutator
subgroup,
(3) if G is ﬁnite and p is a prime dividing |G|, there is a minimal normal subgroup of
size p and a maximal subgroup of index p.
Proof. (1): Let N be a minimal normal subgroup. Since N is nontrivial and normal, N ∩Z1
is nontrivial by nilpotency of G. Since N ∩Z1 is a normal subgroup of G, by minimality of
N we have N = N ∩Z1, so N ⊂Z1. Since N is in the center of G, every subgroup of N is
a normal subgroup of G, so N contains no proper nontrivial subgroups. It follows that N
is abelian and simple, so it has prime order.
(2): If M is maximal then, since M ̸= N(M) by nilpotency of G, we must have N(M) = G,
hence M ◁G. The quotient group G/M contains no proper nontrivial subgroups (otherwise
we could lift one back to G and violate the maximality of M), so G/M has prime order.
Then G/M is abelian, so G′ ⊂M.
(3): Let |G| = pkm where p does not divide m. We can write G = P × H where P is the
p-Sylow subgroup of G and H is the direct product of the Sylow subgroups for primes other
than p. The center of P is nontrivial and a subgroup of size p in Z(P) is a normal subgroup
of G, necessarily minimal. The p-group P contains a subgroup of index p, and its direct
product with H is a subgroup of G with index p, which means it must be maximal.
□
Corollary 2.3. A nontrivial ﬁnite group is nilpotent if and only if every maximal subgroup
is normal.
Proof. The “only if” direction follows from Theorem 2.2.
Now assume every maximal
subgroup of a ﬁnite group G is normal, and let P be a Sylow subgroup of G. Then P ⊂
N(P) ⊂G. If N(P) ̸= G then N(P) ⊂M ̸= G with M a maximal subgroup. Then M ◁G.
Since P ⊂M ⊂G, by Sylow theory N(M) = M.
Also N(M) = G, since M ◁G, so
M = G. This is a contradiction, so N(P) = G, which tells us all the Sylow subgroups of G
are normal, so G is nilpotent.
□
Theorem 2.4. If G is a nontrivial ﬁnite solvable group then
(1) every minimal normal subgroup is isomorphic to (Z/(p))k for some prime p and
k ≥1,
(2) every maximal subgroup has prime-power index,
(3) for some prime p dividing |G| there is a minimal normal p-subgroup,
(4) for every prime p dividing |G| there is a maximal subgroup with p-power index.
Proof. (1): Let N be a minimal normal subgroup of G. Since N is solvable and nontrivial,
N′ is a proper subgroup of N. Since N ◁G, N′ = [N, N]◁G. Therefore by minimality of N
we must have N′ = {e}, so N is abelian. Let p be a prime dividing |N|, so {x ∈N : xp = e}
is a nontrivial normal subgroup of G. Again by minimality of N, this subgroup is N, so N

<!-- page 3 -->
SUBGROUP SERIES II
3
is a ﬁnite abelian group in which each element satisﬁes xp = e. It follows that N ∼= (Z/(p))k
for some k.
(2): We argue by induction on |G|. The result is clear if |G| is a prime (or even a prime
power), so we can assume |G| ≥6, |G| is not a prime and also that the result is true for
solvable groups of smaller size. Let M be a maximal subgroup of G. We want to show
[G : M] is a prime power. Let N be a minimal normal subgroup in G, so N ̸= G (e.g.,
the commutator subgroup of G is a proper normal subgroup). Then MN/N ⊂G/N, so
MN/N is solvable. Since M ⊂MN ⊂G, either MN = M or MN = G by maximality of
M. In the ﬁrst case N ⊂M, so M/N is a maximal subgroup of G/N. As |G/N| < |G|,
by induction [G/N : M/N] is a prime power. This index equals [G : M]. In the second
case, [G : M] = |G|/|M| = |MN|/|M| = |N|/|M ∩N|, which is a prime power since N is a
p-group by (1).
(3): The group has a minimal normal subgroup, and by (1) this subgroup is a p-group
for some prime p.
(4): We argue by induction on |G|.
The result is clear if |G| is a prime power (in
particular, if |G| is prime). Let p be a prime dividing |G| and N be a minimal normal
subgroup, so in particular N has prime-power size (the prime is not necessarily p). Since
G/N is solvable, if p | |G/N| then by induction G/N has a maximal subgroup of p-power
index, and the pullback of this subgroup to G will be a maximal subgroup of G with the
same p-power index (in G). What if p does not divide |G/N|? Then p | |N|, so N must
be a p-group, and therefore is a p-Sylow subgroup of G. Since N is a normal subgroup
with (|N|, |G/N|) = 1, by the Schur–Zassenhaus theorem there is a complement to N in G:
some K ⊂G has N ∩K = {e} and NK = G, so [G : K] = |N| is a power of p. A maximal
subgroup of G containing K will have p-power index in G.
□
Example 2.5. A minimal normal subgroup of S4 is V ∼= Z/(2) × Z/(2).
Part (3) of the theorem can’t be extended to all primes dividing |G|: there is no minimal
normal 3-subgroup of S4.
Remark 2.6. If G is an inﬁnite solvable group then part (1) of Theorem 2.4 can be extended
to say every minimal normal subgroup N is a vector space (over Q or some Z/(p) acting
on N as exponents). Here’s how. The proof that N is abelian goes through as before, so
x 7→xb is a homomorphism N →N for all b ∈Z. Consider Np = {xp : x ∈N} for all
primes p. These are normal subgroups of G, so they equal N or {e}. If one of them is
trivial then N is a vector space over Z/(p) for that p. If instead Np = N for all p then
x 7→xp on N is surjective with trivial kernel: Kp := {x ∈N : xp = e} is a normal subgroup
of G contained in N, and Kp ̸= N since Np = N ̸= {e} (minimal normal subgroups are
nontrivial by deﬁnition), so Kp = {e} for all p. Therefore N is a torsion-free abelian group.
The condition Np = N for all primes p implies Nb = N for all b ∈Z −{0}, so for each
x ∈N and integers a and b with b ̸= 0, xa = yb for a unique y ∈N. Deﬁne xa/b := y and
check this gives N the structure of a Q-vector space.
Here is an analogue of nontrivial quotients of nilpotent groups having nontrivial center.
Corollary 2.7. A nontrivial ﬁnite group is solvable if and only if every nontrivial quotient
of it contains a nontrivial abelian normal subgroup.
Proof. A nontrivial ﬁnite solvable group contains a nontrivial abelian normal subgroup,
such as a minimal normal subgroup. Since every quotient of a solvable group is solvable,

<!-- page 4 -->
4
KEITH CONRAD
the “only if” direction is settled. For the “if” direction, we induct on the size of the group.
For a group G whose nontrivial quotients all contain nontrivial abelian normal subgroups,
there is a nontrivial abelian normal subgroup N in G. If N = G then G is abelian, hence
solvable. Assuming N ̸= G, both N and G/N are nontrivial with size less than |G|. Every
quotient of G/N is a quotient of G, so G/N satisﬁes the hypotheses of the theorem. By
induction, G/N is solvable. As N is abelian, it too is solvable. Therefore N and G/N are
solvable, so G is solvable.
□
It is false that a ﬁnite group is solvable if and only if its nontrivial subgroups all con-
tain nontrivial abelian normal subgroups. For instance, SL2(Z/(5)) satisﬁes SL2(Z/(5))′ =
SL2(Z/(5)), so the group is not solvable. But it has a nontrivial abelian normal subgroup,
its center {±I2}, and every nontrivial subgroup of SL2(Z/(5)) is solvable and therefore also
contains a nontrivial abelian normal subgroup.
3. The Fitting and Frattini Subgroups
Recall that the upper and lower central series {Zi} and {Li} of a group G both reach
the end (the upper one reaching G and the lower one reaching {e}) precisely when G is
nilpotent, in which case the number of terms in both series is the same. The nilpotency
class of G is the least c ≥0 such that Zc = G (equivalently, Lc = {e}), and G is nontrivial
abelian precisely when it has nilpotency class 1.
Using a theorem of Fitting (Theorem 3.2 below) we will construct two new subgroup
series in each ﬁnite group, one ascending and the other descending, such that they both
terminate at the end precisely when the group is solvable, and the nilpotent groups will be
those where the process stops in one step.
Our starting point is a nilpotent analogue of the theorem that when H and K are solvable
normal subgroups of G, HK is solvable.
Lemma 3.1. If G is nilpotent of class c then each subgroup and quotient group of G has
class at most c. If G is nontrivial then G/Zi has class c −i.
Proof. The proof that nilpotency is preserved when passing to subgroups and quotient
groups shows that the nilpotence class does not grow when passing to subgroups or quotient
groups of nilpotent groups.
When G is nontrivial, the upper central series for G/Zi is
Zi/Zi ⊂Zi+1/Zi ⊂· · · ⊂Zc/Zi = G/Zi with Zc−1/Zi ̸= G/Zi.
This series has c −i
factors.
□
Theorem 3.2 (Fitting, 1938). If G is a group and H and K are nilpotent normal subgroups
of G then HK is nilpotent normal in G.
Proof. That HK is a normal subgroup when H and K are normal is standard. To prove
HK is nilpotent, since H and K are normal in HK we may as well take G = HK. That
is, we will show that if a group G is generated by two nilpotent normal subgroups H and
K then it is also nilpotent.
Let H have nilpotence class c and K have nilpotence class d. We will argue that HK
is nilpotent by induction on the sum c + d. The result is obvious if c or d is 0, so we
may take c and d positive. The center of H, Z(H), is a normal subgroup of G = HK.
The quotient group G := G/Z(H) is generated by the subgroups H = H/Z(H) and K =
KZ(H)/Z(H) ∼= K/(Z(H) ∩K). Both H and K are normal subgroups of G and they
are nilpotent.
The class of H is c −1 (Lemma 3.1) and the class of K is ≤d.
Since

<!-- page 5 -->
SUBGROUP SERIES II
5
c −1 + d < c + d, by induction G = G/Z(H) is nilpotent. By a similar argument G/Z(K)
is nilpotent. Then, since Z(H) and Z(K) are normal in G, G/(Z(H) ∩Z(K)) is nilpotent.
Since Z(H)∩Z(K) ⊂Z(G), G/Z(G) is a quotient group of G/(Z(H)∩Z(K)) and therefore
G/Z(G) is nilpotent. Hence G is nilpotent (if G/Zi(G) is nilpotent for some i then G is
nilpotent).
□
Theorem 3.2 is false if we replace nilpotency with commutativity: in D4 the subgroups
H = ⟨r⟩and K = ⟨r2, s⟩are abelian and normal, but HK = D4 is not abelian (but it is
nilpotent).
Theorem 3.2 need not hold without the normality condition on both H and K: the
subgroups H = ⟨r⟩and K = ⟨s⟩of Dn are both nilpotent and only one of them is normal
in Dn, but HK = Dn is not nilpotent when n ≥3 is odd.
The Fitting subgroup (or nilpotent radical) of a ﬁnite group G is
F(G) = unique maximal nilpotent normal subgroup of G.
That this subgroup makes sense follows from Fitting’s theorem.
If G is nilpotent then
F(G) = G.
When n is not a power of 2, F(Dn) = ⟨r⟩.
The Fitting subgroups of the
symmetric groups are F(S3) = A3, F(S4) = V , and F(Sn) = {(1)} for n ≥5. When G is
inﬁnite, the Fitting subgroup of G is deﬁned to be the subgroup generated by the nilpotent
normal subgroups, but it is not necessarily nilpotent itself. We will not discuss the Fitting
subgroup of inﬁnite groups.
The Fitting subgroup of a ﬁnite group G is a direct product of its own Sylow subgroups,
since F(G) is nilpotent. Since F(G) has a rather canonical status within G (the nilpotent
normal subgroup containing all others), the Sylow subgroups of F(G) are, not surprisingly,
closely related to the Sylow subgroups of G:
Theorem 3.3. For a ﬁnite group G and a prime p, the p-Sylow subgroup of F(G) is the
intersection of the p-Sylow subgroups of G.
Proof. Let Sylp(F(G)) = {Q}. Since F(G)◁G and Q is a normal Sylow subgroup of F(G), Q
is normal in G. Therefore Q lies in every p-Sylow subgroup of G. For the reverse inclusion,
the intersection of the p-Sylow subgroups of G is a normal p-subgroup of G, hence a normal
nilpotent subgroup, so it lies in F(G). The group Q is the unique p-Sylow in F(G), so the
intersection of the p-Sylows of G lies in Q.
□
Recall a subnormal subgroup is a subgroup linked to the whole group by a tower of
subgroups that are normal in each other.
Corollary 3.4. For each ﬁnite group G, its Fitting subgroup F(G) contains all nilpotent
subnormal subgroups of G.
Proof. Let H ⊂G be a subnormal subgroup, say
H = H0 ◁H1 ◁· · · ◁Hr = G.
We will prove quite generally that if K is a ﬁnite group and N ◁K then F(N) ⊂F(K).
Applying this to the above series from H to G, we obtain F(H) ⊂F(H1) ⊂· · · ⊂F(G), so
if H is nilpotent then H = F(H) and therefore H ⊂F(G).
To show N ◁K =⇒F(N) ⊂F(K) it suﬃces to show the p-Sylow subgroup of F(N) is
inside the p-Sylow subgroup of F(K) (Fitting subgroups are nilpotent). By Theorem 3.3,

<!-- page 6 -->
6
KEITH CONRAD
for each prime p the p-Sylow subgroup of F(N) is
\
P∈Sylp(N)
P.
Since every p-Sylow of N has the form N ∩Q for some p-Sylow Q of K (and vice versa),
\
P∈Sylp(N)
P =
\
Q∈Sylp(K)
(N ∩Q) = N ∩
\
Q∈Sylp(K)
Q,
and this last intersection is the intersection of N with the p-Sylow subgroup of F(K).
□
Armed with the Fitting subgroup, we can give a solvable analogue of the theorem that
nontrivial normal subgroups of nilpotent groups nontrivially intersect the center.
Theorem 3.5. If G is a nontrivial solvable group then every nontrivial normal subgroup
N contains a nontrivial abelian normal subgroup of G.
In particular, when G is ﬁnite
N ∩F(G) ̸= {e}.
Proof. We have N ∩G(0) = N ̸= {e} and N ∩G(i) = {e} for large i (since G(i) is trivial for
large i). Choose i ≥1 maximal such that N∩G(i) ̸= {e}. Since N′ ⊂N and (G(i))′ = G(i+1),
(N ∩G(i))′ ⊂N ∩G(i+1) = {e}, so N ∩G(i) is abelian. It is normal in G since N and G(i)
are both normal subgroups of G. Abelian groups are nilpotent, so N ∩G(i) ⊂N ∩F(G).
□
That a nontrivial ﬁnite solvable group has a nontrivial Fitting subgroup is analogous to
a nontrivial nilpotent group having a nontrivial center. Constructing “higher” centers of
a group leads to the upper central series, and we can similarly construct “higher” Fitting
subgroups. For a (ﬁnite) group G, let F0 = {e} and F1 = F(G). We have F(G) = G if and
only if G is nilpotent. If we have deﬁned a normal subgroup Fi◁G, write F(G/Fi) = Fi+1/Fi.
This is normal in G/Fi, so Fi+1 ◁G. Thus we get an ascending series
{e} = F0 ⊂F1 ⊂F2 ⊂· · · ⊂G
where Fi ◁G for all i. Each quotient group Fi+1/Fi is nilpotent by the deﬁnition of a
Fitting subgroup. Going down instead of up, the lower central series of a ﬁnite group G
will eventually stabilize: set L∞(G) = Li(G) for large i. Then L∞(G) is trivial if and only
if G is nilpotent. Deﬁne E0 = G, E1 = L∞(G), and Ei+1 = L∞(Ei). We get a descending
series
G = E0 ⊃E1 ⊃E2 ⊃· · · ⊃{e},
where Ei ◁G for all i. Each quotient group Ei/Ei+1 is nilpotent. (Hint: G/N is nilpotent
if and only if L∞(G) ⊂N). These series {Fi} and {Ei} bound series with nilpotent factors
from above and below in the same spirit of the upper and lower central series bounding
ascending and descending central series from above and below (Corollary 3.4 is useful here),
so {Fi} is called the upper nilpotent series for G and {Ei} is called the lower nilpotent series
for G. (Why doesn’t a construction Z∞, analogous to L∞but applied to the upper central
series, lead to a worthwhile subgroup series in place of the Fi’s?) Just as with central series,
Fi = G for large i if and only if Ei = {e} for large i, and then the least i’s in both cases
are equal (exercise). The least such i is called the Fitting length (or nilpotent length, not to
be confused with nilpotent class) of G. The trivial group has Fitting length 0, and a ﬁnite
group has Fitting length 1 if and only if it is nontrivial and nilpotent.

<!-- page 7 -->
SUBGROUP SERIES II
7
Example 3.6. Let G = Dn with n not a power of 2. Write n = 2km for odd m ≥3.
Then F1 = ⟨r⟩and Dn/F1 has size 2 (so it’s nilpotent), hence F2 = Dn. The subgroup
E1 = L∞(Dn) is ⟨r2k⟩, which is abelian, so E2 = {1}. Thus Dn has Fitting length 2.
Example 3.7. Let G = Sn for n ≥5. Then F(G) is trivial, so Fi is trivial for all i ≥0.
Since L∞(Sn) = An and L∞(An) = An, Ei = An for i ≥1. There is no Fitting length.
Theorem 3.8. A ﬁnite group has a Fitting length if and only if it is solvable.
Proof. Suppose G is a ﬁnite solvable group. If Fi ̸= G then G/Fi is a nontrivial ﬁnite
solvable group so its Fitting subgroup Fi+1/Fi is nontrivial. Therefore Fi+1 ̸= Fi, so for
large i we must have Fi = G. Similarly, if Ei ̸= {e} then Ei+1 ̸= Ei (because Ei+1 =
L∞(Ei) ⊂L1(Ei) = E′
i, which is a proper subgroup of Ei because Ei is a nontrivial solvable
group). Therefore Ei is trivial for large i.
Now suppose G has a Fitting length. The upper nilpotent series is a normal series for G
with nilpotent factors. Since nilpotent groups are solvable and solvability of N and H/N
implies solvability of H, we get solvability of G by arguing inductively that every Fi is
solvable.
□
Remark 3.9. A group G is called metacyclic, metabelian, or metanilpotent if it has a normal
subgroup N such that N and G/N are both cyclic, both abelian, or both nilpotent. This
means the normal series {e} ◁N ◁G has both factors cyclic or abelian or nilpotent, so
these properties are preserved by passage to subgroups and quotient groups (but not direct
products, since the direct product need not have such a series with 2 factors). All such
groups are solvable since N and G/N are solvable. Check that metabelian is the same as
having solvable length ≤2 while (when G is ﬁnite) metanilpotent is the same as having
Fitting length ≤2.
In addition to the Fitting subgroup, there is another important nilpotent subgroup of
each ﬁnite group: its Frattini subgroup.
Deﬁnition 3.10. The Frattini subgroup of a ﬁnite group is the intersection of its maximal
subgroups:
Φ(G) =
\
max.M
M.
We set the trivial group to have trivial Frattini subgroup.
The intersection deﬁning Φ(G) is preserved by conjugations, so Φ(G) ◁G. For instance,
Φ(D4) = {1, r2} and Φ(Sn) is trivial for n ≥3. (In particular, since D4 is the 2-Sylow
subgroup of S4, we see that if H ⊂G then Φ(H) can be larger than Φ(G).) When G is
nilpotent, G′ ⊂Φ(G) by Theorem 2.2(2), so the quotient G/ Φ(G) is abelian. In particular,
G/ Φ(G) is abelian when G is a ﬁnite p-group.
Theorem 3.11. Let G be a ﬁnite p-group.
The number of maximal subgroups of G is
(pn −1)/(p −1), where G/ Φ(G) has pn −1 elements of order p.
Proof. Maximal subgroups of G each contain Φ(G), so G and G/ Φ(G) have the same
number of maximal subgroups. Thus we focus on counting maximal subgroups of G/ Φ(G).
Each maximal subgroup M of G is normal with index p by Theorem 2.2. Since G/M has
order p, gp ∈M for all g ∈G, so gp ∈Φ(G) for all g ∈G. Thus in G/ Φ(G) all nontrivial
elements have order p, so this ﬁnite abelian group must be a direct sum of cyclic groups of
order p: G/ Φ(G) ∼= (Z/(p))n for some n. We will count maximal subgroups of (Z/(p))n.

<!-- page 8 -->
8
KEITH CONRAD
The maximal subgroups of (Z/(p))n are the subgroups with index p.
In every ﬁnite
abelian group, the number of subgroups of order d and index d are the same for each d.
Thus the number of subgroups of (Z/(p))n with index p equals the number of subgroups with
order p. Let s be the number of subgroups with order p. Each nonzero element generates
such a subgroup and two such subgroups have trivial intersection, so pn −1 = s(p −1).
Thus s = (pn −1)/(p −1), so G has (pn −1)/(p −1) maximal subgroups, where pn −1 is
the number of elements of G/ Φ(G) ∼= (Z/(p))n with order p.
□
Much more can be said (and used) about G/ Φ(G) when G is a ﬁnite p-group: look up
the “Burnside basis theorem” in a group theory book.
Theorem 3.12 (Frattini, 1885). For every ﬁnite group G, Φ(G) is nilpotent.
Proof. We will show all the Sylow subgroups of Φ(G) are normal subgroups of Φ(G), so
Φ(G) is nilpotent2. Let P be a Sylow subgroup of Φ(G). Then G = Φ(G) NG(P) by the
Frattini argument3.
If P is not normal in G then NG(P) ̸= G.
Let M be a maximal
subgroup of G containing NG(P), so Φ(G) ⊂M. Therefore G = Φ(G) NG(P) ⊂M, a
contradiction, so P ◁G, which implies P ◁Φ(G).
□
Since, for each ﬁnite group G, Φ(G) is a nilpotent normal subgroup of G,
Φ(G) ⊂F(G).
We can now give two more characterizations of nilpotency for ﬁnite groups (extending
the list from Theorem 1.1 and Corollary 2.3).
Theorem 3.13. For a nontrivial ﬁnite group G the following are equivalent to nilpotency:
(1) G′ ⊂Φ(G), i.e., G′ ⊂M for every maximal subgroup M,
(2) G/ Φ(G) is nilpotent.
Proof. By Theorem 2.2, every nilpotent group satisﬁes (2). Now assume (2). Then every
maximal subgroup of G is normal since all subgroups of G that contain G′ are normal.
Therefore G is nilpotent by (1).
Nilpotence of G implies (3) since every quotient of a nilpotent group is nilpotent. Now
assume (3). Pick a Sylow subgroup P of G. To show P ◁G, ﬁrst note that (P Φ(G))/ Φ(G) is
a Sylow subgroup of G/ Φ(G), so (P Φ(G))/ Φ(G)◁G/ Φ(G) by (3), which implies P Φ(G)◁
G. Set N = P Φ(G), so N is a normal subgroup of G. Then P is a Sylow subgroup of
N (why?), so by the Frattini argument, G = N NG(P) = NG(P)N = NG(P)P Φ(G) =
NG(P) Φ(G). If NG(P) ̸= G then NG(P) ⊂M for some maximal subgroup M of G. Since
Φ(G) ⊂M too, G = NG(P) Φ(G) ⊂M, a contradiction. Thus NG(P) = G, so P ◁G.
□
4. Supersolvable groups
Having examined nilpotent and solvable groups, we turn now to a third class of groups:
supersolvable groups. Among ﬁnite groups, these three classes of groups ﬁt into the following
chain of inclusions:
nilpotent ⊂supersolvable ⊂solvable,
and examples show all inclusions are strict. Following the pattern set before with nilpotent
and solvable groups, we’ll see how supersolvable groups behave under group constructions
2See Theorem 5.20 in https://kconrad.math.uconn.edu/blurbs/grouptheory/subgpseries1.pdf.
3See Section 8 in https://kconrad.math.uconn.edu/blurbs/grouptheory/sylowapp.pdf.

<!-- page 9 -->
SUBGROUP SERIES II
9
(subgroup, quotient group, direct product) and the nature of their minimal normal sub-
groups and maximal subgroups.
Nilpotent and solvable groups can both be described in terms of particular normal series
(the upper and lower central series or the derived series) whose constituent subgroups
happen to be normal in the whole group. This is a stronger property than normal series
require (each subgroup in the series only needs to be normal in the next subgroup of the
series), and it is convenient to give series with this stronger property a name.
Deﬁnition 4.1. A normal series
{e} = G0 ◁G1 ◁G2 ◁· · · ◁Gr = G
or
G = G0 ▷G1 ▷G2 ▷· · · ▷Gr = {e},
where Gi ◁G for all i is called an invariant series.
The word “invariant” comes from its obsolete meaning as “normal,” in the context of
subgroups.
That is, normal subgroups used to be called invariant subgroups (invariant
under conjugation, evidently).
Example 4.2. For every group G, {e} ◁G is an invariant series for G.
Example 4.3. The normal series
{(1)} ◁V ◁A4 ◁S4
for S4 is invariant, where
V = {(1), (12)(34), (13)(24), (14)(23)} = ⟨(12)(34), (13)(24)⟩∼= (Z/(2))2.
is the subgroup of permutations of type (2, 2)). However, the reﬁnement
{(1)} ◁U ◁V ◁A4 ◁S4,
where U is a subgroup of V with size 2, is not invariant: the subgroup U is not normal in
S4.
Remark 4.4. Recall that a subgroup H at the bottom of a tower of successive normal
subgroups H = H0 ◁H1 ◁H2 ◁· · · ◁G is called a subnormal subgroup of G. So a normal
series contains subnormal subgroups while an invariant series contains normal subgroups.
Doesn’t that sound like conﬂicting terminology?
Naturally enough, some people prefer
to label a normal series as a subnormal series and an invariant series as a normal series,
so that subnormal series contain subnormal subgroups while normal series contain normal
subgroups. It appears that most of the widely used algebra textbooks use the label “normal
series” in accordance with our usage, so we will stick to that.
Here’s the main object of interest for us.
Deﬁnition 4.5. A group G is called supersolvable if it has an invariant cyclic series: each
subgroup in the series is normal in G and every factor is a cyclic group.
This term in British English is supersoluble.
Where does the label “supersolvable” come from? Since an invariant cyclic series is a
normal cyclic series, every supersolvable group is solvable, and they’re such a special type
of solvable group that they are singled out by the extra decoration supersolvable.

<!-- page 10 -->
10
KEITH CONRAD
Example 4.6. The dihedral group Dn for n ≥3 is supersolvable since it has the invariant
cyclic series {1} ⊂⟨r⟩⊂Dn. (In particular, S3 ∼= D3 is supersolvable.) Easily D1 and D2
are also supersolvable.
Example 4.7. The inﬁnite dihedral group Aﬀ(Z) is supersolvable: it has the invariant
cyclic series {I2} ⊂{( 1 ∗
0 1 )} ⊂Aﬀ(Z), with factors Z and {±1}.
Example 4.8. The groups A4 and S4 are solvable, but not supersolvable. The only normal
subgroups of A4 are {(1)}, V ∼= (Z/(2))2, and A4, and V is not cyclic, so A4 has no invariant
cyclic series. (The normal cyclic series {(1)} ◁U ◁V ◁A4 is not an invariant series for A4
since U is not normal in A4.) The only normal subgroups of S4 are {(1)}, V , A4, and S4.
These can’t be ﬁt into an invariant cyclic series for the same reason A4 has none. Obviously
it is pretty tedious to show a group is not supersolvable in this way. Later we will see better
ways to check ﬁnite groups are not supersolvable. In any case, A4 and S4 are basic examples
of solvable groups that are not supersolvable. Remember them.
Remark 4.9. There is an ascending series of subgroups in each ﬁnite group whose behavior
reﬂects supersolvability in the same way that the upper and lower central series and derived
series are connected with nilpotency and solvability. See [1].
Remark 4.10. In Galois theory, it is believed (but not proved) that every ﬁnite group
arises as a Galois group over Q. This is not true when the base ﬁeld is the p-adic numbers
Qp since the Galois group of a ﬁnite Galois extension of Qp is solvable. It might not be
supersolvable. For instance, S4 and A4 are solvable but not supersolvable and they occur
as Galois groups over Q2: x4 + 2x + 2 has Galois group S4 over Q2 and x4 + 2x3 + 2x2 + 2
has Galois group A4 over Q2.
Theorem 4.11. Supersolvable groups are closed under passage to subgroups, quotients, and
direct products.
Proof. The basic behavior of normal series of a group under passage to subgroups, quotient
groups, and direct products carry over to invariant series with no changes whatsoever in
the proofs. In particular, if a group admits an invariant series with cyclic factors then so
does every subgroup and quotient group and direct product of such groups. The proofs
are absolutely the same. It’s just a matter of checking that all groups that are constructed
in the proofs are normal in the whole group when the subgroups in the original series are
normal in the whole group.
□
Example 4.12. The group SL2(Z/(3)) is solvable but not supersolvable. It is solvable
because the subgroup {±I2} and quotient SL2(Z/(3))/{±I2} ∼= A4 are solvable. This also
shows (by Theorem 4.11) that SL2(Z/(3)) is not supersolvable, since it has a quotient
isomorphic to the nonsupersolvable group A4.
Example 4.13. The groups Aﬀ(Z/(n)) are supersolvable for all n ≥2. To prove this, it
suﬃces (by Theorem 4.11) to check Aﬀ(Z/(pk)) is supersolvable for all prime powers pk,
since Aﬀ(Z/(n)) is a direct product of such groups by the Chinese remainder theorem. The
invariant series
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
for Aﬀ(Z/(pk)) has factors Z/(pk) and (Z/(pk))×. The ﬁrst factor is obviously cyclic for
all p, and (Z/(pk))× is cyclic for all odd primes p. Therefore Aﬀ(Z/(pk)) is supersolvable

<!-- page 11 -->
SUBGROUP SERIES II
11
when p ̸= 2. It remains to handle the case p = 2, and we will return to this point after
Lemma 4.16.
Corollary 4.14. Let G be a group with normal subgroups H and K. If G/H and G/K are
supersolvable then G/(H ∩K) is supersolvable.
Proof. This follows from Theorem 4.11 by the same proof as for nilpotency and solvability.
□
When G has normal subgroups H and K that are nilpotent or solvable, we saw in part
I that HK is nilpotent or solvable, respectively. The proof was easy in the solvable case,
harder in the nilpotent case and it is impossible in the supersolvable case. That is, the
supersolvable analogue is false: HK need not be supersolvable when H and K are. We will
see a counterexample after we have learned some more properties of supersolvable groups.
It is false in general that if N and G/N are supersolvable then G is supersolvable. For
instance, V and A4/V are supersolvable, but A4 is not supersolvable.
Here is a weak
substitute, however.
Theorem 4.15. Let G be a group and N ◁G. If N is cyclic and G/N is supersolvable
then G is supersolvable.
Proof. Lift an invariant cyclic series for G/N up to G, so it ends in N, and then tack the
identity subgroup on.
□
We already noted that every supersolvable group is solvable. How do the supersolvable
groups compare to the nilpotent groups?
Lemma 4.16. Every ﬁnite p-group is supersolvable.
Proof. Let |G| be a group of size pn. When n = 1, G is cyclic and therefore supersolvable.
We now suppose n > 1 and that the theorem is true for p-groups of size less than pn. Since
G is nilpotent, it has a normal subgroup N ◁G of size p. Then G/N has size pn−1, so G/N
is supersolvable by induction. Since N is cyclic, G is supersolvable by Theorem 4.15.
□
Now we can complete the remaining detail in Example 4.13. We had to show Aﬀ(Z/(2k))
is supersolvable. It’s a ﬁnite 2-group, so we’re done.
Theorem 4.17. Every ﬁnite nilpotent group is supersolvable.
Proof. Supersolvability is true for ﬁnite p-groups and thus also for direct products of ﬁnite
p-groups. These are precisely the ﬁnite nilpotent groups.
□
Inﬁnite nilpotent groups need not be supersolvable. The reason is that, since cyclic groups
have a single generator, a supersolvable group must be ﬁnitely generated, so in particular
countable. Therefore uncountable abelian groups are nilpotent but not supersolvable. It
turns out that a nilpotent group is supersolvable if and only if it is ﬁnitely generated (proof
omitted).
In an inﬁnite nilpotent group the elements with ﬁnite order form a subgroup, but this
need not hold in supersolvable groups. For example, Aﬀ(Z) is supersolvable (Example 4.7)
and the elements of ﬁnite order in Aﬀ(Z) are ( 1 0
0 1 ) and the matrices ( −1 b
0 1 ), that have order
2. Since ( −1 b
0 1 )( −1 c
0 1 ) = ( 1 b−c
0
1 ), the elements of ﬁnite order in Aﬀ(Z) are not a subgroup.
All three of our basic classes of groups – nilpotent, solvable, and supersolvable – can
be characterized in terms of invariant series. A group is nilpotent if and only if it has an

<!-- page 12 -->
12
KEITH CONRAD
invariant central series (the upper and lower central series will work), a group is solvable if
and only if it has an invariant abelian series (the derived series will work), and by deﬁnition
a group is supersolvable if and only if it has an invariant cyclic series. While there is no
diﬀerence between a ﬁnite group having a normal abelian series or a normal cyclic series (the
former can be reﬁned to the latter), there is a diﬀerence between a group having an invariant
abelian series or an invariant cyclic series (A4 has the former, namely {(1)} ◁V ◁A4, but
not the latter) and this motivates the introduction of supersolvability as a special kind of
solvability.
A nontrivial ﬁnite solvable group has a normal series whose factors are cyclic of prime
order. Here is the supersolvable analogue.
Theorem 4.18. A nontrivial supersolvable group has an invariant series whose factors are
inﬁnite cyclic or cyclic of prime order. In particular, a nontrivial ﬁnite supersolvable group
has an invariant series whose factors have prime order.
Proof. We show how to reﬁne each invariant cyclic series so that its ﬁnite cyclic factors
have prime order. The catch is that unlike in a normal series we have to make sure our
reﬁnements produce new subgroups that are normal in the whole group. Let
(4.1)
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂Gr = G
be an invariant cyclic series with Gi ◁G and Gi+1/Gi cyclic for all i. We may cut out all
repetitions from (4.1), so each factor Gi+1/Gi is nontrivial. If some factor Gi+1/Gi is ﬁnite
cyclic and not of prime order, let p be a prime dividing |Gi+1/Gi|. Then Gi+1/Gi has a
subgroup of order p, say H/Gi. Since Gi and Gi+1 are both normal in G, for all g ∈G
conjugation by g is well-deﬁned on Gi+1/Gi and sends H/Gi to the subgroup gHg−1/Gi in
Gi+1/Gi, also of size p. Since Gi+1/Gi is cyclic it has only one subgroup of each possible size,
so H/Gi = gHg−1/Gi. Thus H = gHg−1, so H ◁G. Now we insert H into the series (4.1)
and we have an invariant series whose factors are still cyclic: H/Gi is cyclic by construction
while Gi+1/H is a quotient of Gi+1/Gi so it too is cyclic. The factor H/Gi has prime size.
Now repeat this construction until all ﬁnite cyclic factors have prime size. (The process will
terminate since a ﬁnite factor Gi+1/Gi can’t be nontrivially reﬁned indeﬁnitely.)
□
In part I, we brieﬂy discussed Lagrangian groups: those ﬁnite groups satisfying the
converse of Lagrange’s theorem. In particular, we saw every Lagrangian group is solvable.
How is supersolvability related to the Lagrangian property?
Corollary 4.19. A ﬁnite supersolvable group is Lagrangian.
Proof. Our proof is adapted from [2]. Let G be the group. We may of course take G to be
nontrivial and not have prime size.
By Theorem 4.18 there is a series
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂Gr = G
where each Gi is normal in G and the index [Gi+1 : Gi] is prime, and r ≥2. Let p = [G1 : G0]
and q = [G2 : G1]. Given d | |G| we want to construct a subgroup of G with size d. We
may assume by induction that the theorem is true for all supersolvable groups with size less
than |G|.
If p | d then G/G1 has size |G|/p, so by induction it has a subgroup of size d/p. Pulling
this back to G gives a subgroup with size (d/p)p = d.

<!-- page 13 -->
SUBGROUP SERIES II
13
If (p, d) = 1 then pd | |G|, so d | |G|/p. By induction there is a subgroup of G/G1 with
size d, whose pullback to G is a subgroup H of size pd. If pd < |G| then |H| < |G|, so by
induction H (and thus G) has a subgroup of size d.
Suppose (p, d) = 1 and pd = |G|. Then q | d. (Remember q = [G2 : G1].) Let Q be
a q-Sylow subgroup of G2 (so |Q| is q or q2, depending on whether or not p = q). Since
G2 ◁G, by the Frattini argument, G = G2 NG(Q). Computing the size of both sides,
pd = |G2|| NG(Q)|
|G2 ∩NG(Q)| =
pq| NG(Q)|
|G2 ∩NG(Q)|.
Therefore
(4.2)
| NG(Q)| = d|G2 ∩NG(Q)|
q
.
Since Q ⊂G2 ∩NG(Q) ⊂G2 and [G2 : Q] is 1 or p, G2 ∩NG(Q) is either Q or G2, so
|G2 ∩NG(Q)| is either q or pq. If the intersection has size q then (4.2) says NG(Q) has size
d and we’re done. If the intersection has size pq then | NG(Q)| = pd = |G|, so NG(Q) = G.
Therefore Q ◁G.
The group G/Q has size pd/q = p(d/q).
By induction, G/Q has a
subgroup of size d/q, whose pullback to G has size (d/q)q = d.
□
So, among ﬁnite groups, we have the inclusions
cyclic ⊂abelian ⊂nilpotent ⊂supersolvable ⊂Lagrangian ⊂solvable.
All inclusions are strict, e.g., S4 is Lagrangian but not supersolvable and A4 is solvable but
not Lagrangian.
If a ﬁnite group is supersolvable then all of its quotients are Lagrangian (since the quo-
tients are all supersolvable, so Corollary 4.19 applies to them), but the converse is false:
if all quotients are Lagrangian the group need not be supersolvable, S4 being an example.
However, for groups of odd order the converse is true: a group of odd order whose quotients
are all Lagrangian is supersolvable [4]. It is conjectured [10] that a ﬁnite group G whose
quotients are all Lagrangian is supersolvable if and only if it has no subquotient (that is,
no group H/N where N ◁H ⊂G) isomorphic to S4.
Theorem 4.18 is the technical result needed to prove the ﬁrst two parts of the following
theorem.
Theorem 4.20. A nontrivial supersolvable group G has the following properties:
(1) every minimal normal subgroup of G has prime order,
(2) every maximal subgroup of G has prime index,
(3) G′ is nilpotent,
(4) when G is nonabelian there is an abelian N ◁G that properly contains the center of
G.
Proof. (1): Let N be a minimal normal subgroup of G. By Theorem 4.18, G has an invariant
cyclic series whose factors are inﬁnite cyclic or of prime order. Denote it as in (4.1). Since
Gi ◁G we have N ∩Gi ◁G, so by minimality N ∩Gi is trivial or N. Since N ∩G0 is trivial
and N ∩Gr is N, there is some maximal i < r such that N ∩Gi is trivial. Then N ∩Gi+1
is N, so N ⊂Gi+1. The composite map N ,→Gi+1 →Gi+1/Gi has kernel N ∩Gi, which is
trivial, so N embeds into Gi+1/Gi. If Gi+1/Gi ∼= Z/(p) then N ∼= Z/(p). If Gi+1/Gi ∼= Z
then N ∼= Z. But we can’t have N ∼= Z, because then N has a unique subgroup of every
index (or just index 2, to ﬁx ideas) and uniqueness means such subgroups are preserved by

<!-- page 14 -->
14
KEITH CONRAD
conjugations from G, violating the minimal normality of N. So only N ∼= Z/(p) for some
prime p is possible.
(2): Let M be a maximal subgroup. First suppose M ◁G. Then G/M is supersolvable
and contains no nontrivial proper subgroups. By Theorem 4.18, G/M has an invariant
series whose factors are isomorphic to Z or Z/(p) for primes p.
In particular, the ﬁrst
nontrivial term in such a series is a nontrivial subgroup of G/M and thus must be G/M.
Therefore G/M is isomorphic to Z or Z/(p). Since G/M has no nontrivial proper subgroups,
G/M ∼= Z/(p), so [G : M] is prime.
Now suppose M is not a normal subgroup of G. Let H = ∩ggMg−1, which is the largest
normal subgroup of G lying in M. Then M := M/H is a maximal subgroup of G := G/H
and [G : M] = [G : M] (perhaps both indices are inﬁnite a priori), so we can replace G and
M with G and M. Therefore we may assume the only normal subgroup of G inside of M
is the identity.
Using Theorem 4.18, G has a normal subgroup N that is isomorphic to Z or some Z/(p).
Since N is cyclic, every subgroup of N is normal in G. For instance, M ∩N is normal in
G. Since M ∩N is also a subgroup of M, M ∩N is trivial by the previous paragraph.
The group MN is between M and G so either MN = M or MN = G by maximality of
M. If MN = M then N ⊂M, so N = M ∩N is trivial, which is false. Thus MN = G and
M ∩N is trivial. If N ∼= Z/(p) then it’s easy to see that [G : M] = [MN : M] = p, so M
has prime index. If N ∼= Z then we will get a contradiction. Let H be a proper nontrivial
subgroup of N, so H ◁G. Then M ⊂MH ⊂MN = G. Either MH = M or MH = MN.
If MH = M then H ⊂M, so H ⊂M ∩N, which means H is trivial. That’s not true, so
MH = MN. But then each x ∈N can be written as x = mh with m ∈M and h ∈H,
so m = xh−1 ∈N. Thus m ∈M ∩N, which is trivial, so x = h ∈H. Hence N = H, a
contradiction.
(3): Let
{e} = G0 ⊂G1 ⊂· · · ⊂Gr = G.
be an invariant cyclic series. Set Hi = G′ ∩Gi, so we obtain an invariant cyclic series for
G′:
(4.3)
{e} = H0 ⊂H1 ⊂· · · ⊂Hr = G′.
Since Gi ◁G and G′ ◁G, we have Hi ◁G (not just Hi ◁G′). We will show Hi+1/Hi ⊂
Z(G′/Hi) for all i, so (4.3) is a central series and that will prove G′ is nilpotent.
Let G act on Hi+1/Hi by conjugation.
(It can act this way since Hi and Hi+1 are
normal in G.) This is a homomorphism f : G →Aut(Hi+1/Hi). Since Hi+1/Hi is cyclic,
its automorphism group is abelian, so G′ ⊂ker f. Thus G′ acts trivially by conjugaction
on Hi+1/Hi, so Hi+1/Hi ⊂Z(G′/Hi).
(4): Let Z be the center of G, so G/Z is a nontrivial supersolvable group. Write the ﬁrst
non-identity term in an invariant cyclic series for G/Z as H/Z. Then H/Z is cyclic, so H
is abelian and it properly contains Z. Since H/Z ◁G/Z, also H ◁G.
□
The last part of Theorem 4.20 has an important consequence in the representation theory
of supersolvable (so in particular, nilpotent) groups. See [8, Thm. 16, Sect. 8.5].
We now get a conceptually simpler proof of Corollary 4.19: since subgroups of supersolv-
able groups are supersolvable, it suﬃces to show for each prime dividing the size of a ﬁnite
supersolvable group that there is a subgroup with that prime index. Since a supersolvable
group is solvable, for each prime p dividing the size of the group there is a maximal subgroup
with p-power index (this property of ﬁnite solvable groups depends on the Schur-Zassenhaus

<!-- page 15 -->
SUBGROUP SERIES II
15
theorem). This p-power is p itself because maximal subgroups in a supersolvable group have
prime index. This proof of Corollary 4.19 lies a little deeper than the previous proof since
it relies on the Schur–Zassenhaus theorem.
It’s worth comparing Theorem 4.20 to what we know about minimal normal subgroups
and maximal subgroups of nilpotent and solvable groups. This is collected in Table 1.
Group
Minimal Normal
Maximal
Nilpotent
Prime Order
Normal, Prime Index
Supersolvable
Prime Order
Prime Index
Finite Solvable
(Z/(p))k
Prime-Power Index
Table 1.
For nontrivial ﬁnite groups, nilpotency is actually equivalent to maximal subgroups being
normal. A characterization of supersolvability in terms of maximal subgroups will be given
in Theorem 4.23(1).
Theorem 4.20 does not guarantee an inﬁnite supersolvable group has either minimal
normal subgroups or maximal subgroups.
Some supersolvable groups have no minimal
normal subgroups: consider Z. What about maximal subgroups?
Theorem 4.21. Every nontrivial supersolvable group has a maximal subgroup.
Proof. We induct on the number of factors in an invariant cyclic series for the group. Groups
having an invariant cyclic series with 1 factor are cyclic, and nontrivial cyclic groups have
maximal subgroups (either because they are ﬁnite or because Z has maximal subgroups).
Now assume
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂Gr = G
is an invariant cyclic series for a group G and r ≥2. Since G1 ◁G we can drop the identity
term and reduce modulo G1:
{e} = G1/G1 ⊂G2/G1 ⊂· · · ⊂Gr/G1 = G/G1.
This is an invariant cyclic series with r −1 factors, so by induction G/G1 has a maximal
subgroup. Lift it up to G to get a maximal subgroup of G.
□
For comparison, (inﬁnite) nilpotent and solvable groups need not have maximal sub-
groups: try Q.
Example 4.22. If a group G has supersolvable normal subgroups H and K, HK need not
be supersolvable. Here is a family of examples.
Let F = Z/(p) for a prime p ≡1 mod 4 and a2 = −1 in F. In GL2(F), set x = ( a
0
0 1/a )
and y = (
0 1
−1 0 ). Then x2 = y2 = −I2 and xy = −yx, so ⟨x, y⟩∼= Q8. Let GL2(F) act on
F2 in the usual way and set G = F2 ⋊⟨x, y⟩using this action.
Set H = F2 ⋊⟨x⟩and K = F2 ⋊⟨y⟩. Then G = HK, and H and K have index 2 in G,
so they are normal in G. Since F2 is a subgroup of H and K, and
 1
0

is an eigenvector of
x and
 a
1

is an eigenvector of y, F
 1
0

◁H and F
 a
1

◁K. The invariant cyclic series
{e} ⊂F
1
0

⊂F2 ⊂F2 ⋊⟨x2⟩⊂H

<!-- page 16 -->
16
KEITH CONRAD
and
{e} ⊂F
a
1

⊂F2 ⊂F2 ⋊⟨y2⟩⊂K
show H and K are both supersolvable groups. (Neither H nor K is nilpotent, since they
each have more than one 2-Sylow subgroup.)
Now we show G = HK is not supersolvable. It has the normal subgroup F2 = (Z/(p))2,
whose size is p2. Minimal normal subgroups in a supersolvable group have prime size, so
G must have a normal subgroup of size p inside of F2, which amounts to saying there is a
common eigenvector of x and y in F2. However there is no common eigenvector, so G is
not supersolvable.
For the next theorem, recall that the Frattini subgroup Φ(G) is the intersection of the
maximal subgroups of G.
Theorem 4.23. The following properties of a nontrivial ﬁnite group G are equivalent to
supersolvability:
(1) all maximal subgroups have prime index,
(2) all subgroup series of maximal length in G have the same length,
(3) G/ Φ(G) is supersolvable,
(4) all subgroups of G are Lagrangian.
The meaning of (2) is illustrated by
(4.4)
{(1)} ⊂⟨(123)⟩⊂A4,
{(1)} ⊂⟨(12)(34)⟩⊂V ⊂A4,
which are both subgroup series (just chains of subgroups, no normality assumptions) that
have no reﬁnements. They don’t have the same number of terms, and A4 is not supersolv-
able.
Note (4) is stronger than being Lagrangian: S4 is Lagrangian but its subgroup A4 is not.
Proof. (1): This is a theorem of Huppert. See [3, pp. 161–163] or [7, p. 268]. The ﬁrst step
is to show G is solvable. Then this is sharpened to supersolvability.
(2): This is a theorem of Iwasawa. See [3, pp. 342–345].
(3): If G is supersolvable then G/ Φ(G) is supersolvable by Theorem 4.11. Conversely,
if G/ Φ(G) is supersolvable we will show the maximal subgroups of G have prime index,
so G is supersolvable by (1). Well, if M is a maximal subgroup of G then M ⊃Φ(G) by
deﬁnition, so M/ Φ(G) is maximal subgroup of G/ Φ(G). Therefore [G/ Φ(G) : M/ Φ(G)]
is prime since G/ Φ(G) is supersolvable, and [G : M] is the same prime.
(4): This is a theorem of Zappa [9], building on earlier work of Ore [5].
□
Theorem 4.24. Let G be a ﬁnite supersolvable group with size p1p2 · · · pm where p1 ≥p2 ≥
· · · ≥pm. Then G admits an invariant cyclic series
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂Gm = G,
where [Gi : Gi−1] = pi. In particular, the elements of order prime to pm form a normal
subgroup of G.
Proof. We know G has an invariant series with factors of prime order. To show such a
series can be arranged so that the orders of the factors are as described in the theorem, it
suﬃces to focus on three adjacent terms in the series, say H ⊂K ⊂L with p = [K : H]
and q = [L : K] primes. If p ≥q then the primes are in the order we need for the theorem.
Suppose p < q. The group L/H has size pq, and such a group has a unique subgroup of

<!-- page 17 -->
SUBGROUP SERIES II
17
size q. Call it eK/H. Then H ⊂eK ⊂L with [ eK : H] = q and [L : eK] = p. Change the
series by replacing K with eK. It remains to show eK ◁G. Conjugation by elements of G
gives automorphisms of L/H (since H and L are normal in G), thus preserving the unique
q-Sylow subgroup of L/H, so eK ◁G.
With the subgroups of G arranged as in the theorem, we show the elements of order
prime to pm are a normal subgroup of G. Since all factors with size pm occur at the top of
the series, there is some Gi such that [G : Gi] is the largest power of pm dividing |G|. That
means |Gi| is not divisible by pm, so every element of Gi has order prime to pm. Conversely,
since Gi ◁G and Gi has pm-power index in G, only the trivial element of G/Gi has order
prime to pm, so an element of G with order prime to pm must be in Gi. Thus Gi is the set
of elements in G with order prime to pm.
□
Corollary 4.25. If G is a ﬁnite supersolvable group then the elements of odd order form a
normal subgroup.
Proof. If |G| is even then pm = 2 in Theorem 4.24.
□
We can now give several reasons why A4 is not supersolvable:
(1) since (123)(124) = (13)(24), the elements of A4 with odd order are not a subgroup,
(2) A4 is not Lagrangian (no subgroup of size 6),
(3) the minimal normal subgroup V is not of prime order,
(4) the maximal subgroup ⟨(123)⟩is not of prime index,
(5) A4 has maximal subgroup series with diﬀerent lengths in (4.4).
The next theorem is a crude supersolvable analogue of Burnside’s paqb-theorem.
Theorem 4.26. If |G| = pqb where p and q are primes with q ≡1 mod p then G is
supersolvable.
Proof. See [6, Cor. 4.4, 4.5].
□
5. Chief Series
As with nilpotency, supersolvability of a group can’t be characterized by a composition
series: Z/(12) is nilpotent and supersolvable while A4 is neither, but both groups have
composition series with two cyclic factors of order 2 and one of order 3.
When a group has an invariant series (a particular type of normal series), instead of
reﬁning it to a longer normal series until we can’t proceed further we can reﬁne it only to
a longer invariant series as far as possible. By only reﬁning to a new invariant series, we
might have to stop before we would be done reﬁning with normal series, and therefore we
get a new notion.
Deﬁnition 5.1. A chief series of a group G is an invariant series of G with no trivial factors
and no reﬁnements to a longer invariant series.
Example 5.2. The composition series
(5.1)
{(1)} ◁U ◁V ◁A4 ◁S4
for S4 is not a chief series since U is not normal in S4. But the other subgroups in that
series are normal in S4 and they form a chief series for S4: {(1)} ⊂V ⊂A4 ⊂S4. Each
subgroup is normal in S4 and no reﬁnement has this property.

<!-- page 18 -->
18
KEITH CONRAD
The proof that every nontrivial ﬁnite group has a composition series carries over to show
it also has a chief series, while an inﬁnite group may or may not have a chief series (e.g., Z
has no chief series).
What’s the diﬀerence between a composition series and a chief series? The series
(5.2)
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂Gr = G
is a composition series when there are no repetitions, Gi ◁Gi+1 for all i, and no reﬁnement
has these properties. The series (5.2) is a chief series when there are no repetitions, Gi ◁G
for all i, and no reﬁnement has these properties.
When (5.2) is a composition series, Gi is a maximal normal subgroup of Gi+1 for all i. So
composition series are closely related to maximal normal subgroups. The next result shows
chief series are related to minimal normal subgroups of quotients of G.
Theorem 5.3. The series (5.2) is a chief series if and only if Gi+1/Gi is a minimal normal
subgroup of G/Gi for all i.
Proof. Assuming (5.2) is a chief series for G, the series
{e} = Gi/Gi ⊂Gi+1/Gi ⊂· · · ⊂Gr/Gi = G/Gi
is a chief series for G/Gi, since a normal subgroup of G/Gi lying properly between two terms
of this series pulls back to a normal subgroup of G lying properly between the corresponding
two terms of (5.2). Therefore no nontrivial normal subgroup of G/Gi is properly contained
in Gi+1/Gi, so Gi+1/Gi is a minimal normal subgroup of G/Gi.
Conversely, if each Gi+1/Gi is a minimal normal subgroup of G/Gi then no normal
subgroup of G lies properly between Gi and Gi+1, so (5.2) is a chief series for G.
□
Theorem 5.3 suggests a method of constructing a chief series of a nontrivial ﬁnite group
using minimal normal subgroups from the bottom up, which runs in the opposite direction
to the method of constructing a composition series from the top down using maximal normal
subgroups. Let G0 = {e}, G1 be a minimal normal subgroup of G, G2/G1 be a minimal
normal subgroup of G/G1, G3/G2 be a minimal normal subgroup of G/G2, and so on.
In Section 4 we saw that nilpotent, solvable, and supersolvable groups can be described
in terms of the kinds of invariant series they admit (central, abelian, and cyclic). Let’s now
describe them in terms of the chief series they admit.
Corollary 5.4. A nontrivial ﬁnite group is nilpotent if and only if it has a chief series that
is a central series.
Proof. A chief series that is central is a normal central series, so a group with such a series
is nilpotent. Conversely, if G is nilpotent and (5.2) is a chief series for G then Gi+1/Gi is
a minimal normal subgroup of G/Gi. Since G/Gi is nilpotent, Gi+1/Gi is in the center of
G/Gi since minimal normal subgroups in a nilpotent group lie in the center.
□
Example 5.5. The group A4 is not nilpotent and its only chief series is {(1)} ⊂V ⊂A4.
This is not central since V is not in the center of A4.
Corollary 5.6. A nontrivial ﬁnite group is solvable if and only if it has a chief series whose
factors are isomorphic to (Z/(p))k for primes p and integers k ≥1.
Proof. Let G be a ﬁnite group. If G has a chief series whose factors are as described in the
theorem then the series is a normal abelian series, so the G is solvable.
Conversely, if G is fsolvable then in every chief series of G all factors are isomorphic to
some (Z/(p))k since minimal normal subgroups of ﬁnite solvable groups look like that.
□

<!-- page 19 -->
SUBGROUP SERIES II
19
Example 5.7. The chief series of A4, {(1)} ⊂V ⊂A4, has factors (Z/(2))2 and Z/(3).
Corollary 5.8. A nontrivial ﬁnite group is supersolvable if and only if it has a chief series
whose factors have prime order.
Proof. Run through the same proof as Corollary 5.6, but use the fact that minimal normal
subgroups in a supersolvable group have prime order.
□
Here is the Jordan–H¨older theorem for chief series:
Theorem 5.9. If G is a nontrivial group and
{e} = G0 ⊂G1 ⊂G2 ⊂· · · ⊂Gr = G
and
{e} = eG0 ⊂eG1 ⊂eG2 ⊂· · · ⊂eGs = G
are two chief series for G then r = s and for some permutation π ∈Sr we have eGi/ eGi−1 ∼=
Gπ(i)/Gπ(i)−1 for 1 ≤i ≤r.
Proof. The proof of the Jordan–H¨older theorem adapts verbatim to this case, just taking
care to notice that if you run through a proof with chief series then the groups that are
constructed in the course of the proof are normal in the full group (and not just in the next
term of the series).
□
The unreﬁnability of a composition series can be described in terms of its factors as
abstract groups: each factor is a simple group. But Example 5.2 shows the factors in a chief
series may not be simple: the bottom factor for the chief series of S4 (or A4) is V ∼= (Z/(2))2.
Does the unreﬁnability of a chief series tell us anything about the intrinsic group structure
of its factors? A ﬁrst answer comes from Theorem 5.3 and the following theorem.
Theorem 5.10. A minimal normal subgroup of a nontrivial ﬁnite group is a direct product
of isomorphic simple groups.
Proof. Let G be a nontrivial ﬁnite group and N be a minimal normal subgroup of G. We
want to show N is a direct product of isomorphic simple groups.
Let H be a minimal normal subgroup of N. There is no reason to expect H is normal
in G. Every G-conjugate of H lies in N since N ◁G. Let H1, . . . , Hr be all the diﬀerent
G-conjugates of H. So for all g ∈G, gHig−1 is some Hj. The Hi’s are minimal normal
subgroups of N (why?), so the set H1H2 · · · Hr is a normal subgroup of N.
We have
HiHj = HjHi by normality of the Hi’s in N, so H1H2 · · · Hr ◁G. Because N is a minimal
normal subgroup of G, it follows that
(5.3)
N = H1H2 · · · Hr.
An example will help motivate the next step. Take G = A4, which has one minimal normal
subgroup, the subgroup V generated by the (2, 2)-cycles. A minimal normal subgroup of
V is H = ⟨(12)(34)⟩, which has three A4-conjugates (there are three linear subspaces in
(Z/(2))2). Then V = H1H2H3. Notice there is some redundancy, in the sense that we also
have V = H1H2.
Returning to the general case, from (5.3) we can write N as the product of all r subgroups
conjugate to H. But, as the example with A4 shows, we might be able to get by with fewer
conjugate subgroups. Suppose s is the smallest number of Hi’s whose product is N. Relabel
such a choice as H1, . . . , Hs, so N = H1 · · · Hs. We will show N ∼= H1 × · · · × Hs. This is
obvious if s = 1, so suppose s > 1. To show the set product H1 · · · Hs is isomorphic to their

<!-- page 20 -->
20
KEITH CONRAD
direct product, we just need to show Hi ∩H1 · · · bHi · · · Hs is trivial. This is an intersection
of two normal subgroups of N (since Hj ◁N for all j), so it is normal in N. Since it is a
subgroup of Hi, which is a minimal normal subgroup of N, we obtain
Hi ∩(H1 · · · bHi · · · Hs) = {1} or Hi.
If the intersection is Hi then Hi ⊂H1 · · · bHi · · · Hs, so N = H1 · · · bHi · · · Hs. This contradicts
the minimality of s, so Hi ∩(H1 · · · bHi · · · Hs) is trivial for all i.
Thus every minimal normal subgroup N of G is a direct product of groups Hi that are
each isomorphic to a minimal normal subgroup H of N. We want to show N is a direct
product of isomorphic simple groups. If N = G (that is, the minimal normal subgroup of G
is G) then G is simple and the conclusion of the theorem is immediate. If N ̸= G then by
induction on the size of the group the minimal normal subgroup H of N is a direct product
of isomorphic simple groups, so N itself is a direct product of isomorphic simple groups.
□
Corollary 5.11. Every factor in a chief series of a ﬁnite group is a direct product of
isomorphic simple groups.
Proof. If {e} = G0 ⊂G1 ⊂· · · ⊂Gr = G is a chief series for G then Gi+1/Gi is a minimal
normal subgroup of G/Gi. Apply Theorem 5.10 to G/Gi.
□
The converse of this corollary is false: an invariant series having factors that are direct
products of isomorphic simple groups need not be a chief series. For instance, {0} ⊂(Z/(p))k
is such an invarant series, but it’s not a chief series for (Z/(p))k.
Since Corollary 5.11 is not a characterization of the factors in a chief series, our search
for such a characterization continues. We will have to keep the group G close at hand in our
description of the factors, since being a normal subgroup is not a property of a subgroup
in isolation (there is no such thing as a “normal group.”) The key thing to remember is
that when Gi and Gi+1 are terms in an invariant series, each is normal in G so G acts by
conjugation on Gi and Gi+1, and thus also on the factor Gi+1/Gi. Let’s abstract this, using
groups acting on groups.
Fix a group G. For a group H, we call H a G-group when we have a chosen action of G
on H by automorphisms. For instance, we could let G act trivially on H (always possible).
Or, if H = N2/N1 where N1 ⊂N2 are normal subgroups of G, G acts on H by conjugation.
A G-group is not just a group on which G acts in the sense of groups acting on sets: it
must act by automorphisms of the underlying group, so that’s the special feature to keep
in mind.
A subgroup of a G-group H need not be preserved by the action of G. Call H a G-simple
group if H is nontrivial G-group and the only subgroups of H preserved by the action of G
are the trivial subgroup and H itself.
Example 5.12. If G acts trivially on H then it preserves all subgroups, so H is G-simple
if and only if H has no subgroups besides itself and the identity: H is a cyclic group of
prime order.
Example 5.13. If G acts on itself by conjugation, then the subgroups of G preserved by
G are the normal subgroups of G, so G is G-simple (using the conjugation action) precisely
when G is a simple group in the usual sense.
Example 5.14. Let V ◁A4 be the normal subgroup of size 4. The subgroups of size 2 in
V are conjugated into each other by A4, so when V is acted upon by A4 using conjugation,
V is an A4-simple group (but not a simple group in the plain sense).

<!-- page 21 -->
SUBGROUP SERIES II
21
Example 5.15. If N1 ⊂N2 are normal subgroups of G and H = N2/N1 with G acting
on H by conjugation, then the subgroups of H preserved by G are those of the form N/N1
where N is a normal subgroup of G lying between N1 and N2. Therefore H is G-simple
precisely when there are no normal subgroups of G strictly between N1 and N2.
By Example 5.15 we immediately get the next result, which resembles the description of
factors in a composition series.
Theorem 5.16. The series (5.2) is a chief series for G precisely when each factor Gi+1/Gi
is a G-simple group, with G acting on the factors by conjugation.
References
[1] R. K. Agrawal, Generalized center and hypercenter of a ﬁnite group, Proc. Amer. Math. Soc. 58 (1976),
13–21.
[2] C. D. H. Cooper, Subgroups of a supersoluble group, Amer. Math. Monthly 78 (1971), 1007.
[3] M. Hall, “Theory of Groups,” Macmillan, New York, 1959.
[4] J. Humphreys, On groups satisfying the converse of Lagrange’s theorem, Proc. Cambridge Philos. Soc.
75 (1974), 25–32.
[5] O. Ore, Contributions to the theory of groups of ﬁnite order, Duke Math. J. 5 (1939), 431–460.
[6] C. Pinnock, Supersolubility and some characterizations of ﬁnite supersoluble groups, https://cp1888.
files.wordpress.com/2015/01/msci.pdf.
[7] D. Robinson, “A Course in the Theory of Groups,” 2nd ed., Springer-Verlag, New York, 1996.
[8] J-P. Serre, “Linear Representations of Finite Groups,” Springer–Verlag, New York, 1974.
[9] G. Zappa, Remark on a recent paper of O. Ore, Duke Math. J. 6 (1940), 511–512.
[10] L. W. Zhang, The supersolvability of QCLT groups, Acta Math. Sinica 1 (1985), 378–381.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*