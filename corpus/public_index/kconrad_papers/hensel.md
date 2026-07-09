# Hensel's Lemma

> **Source**: https://kconrad.math.uconn.edu/blurbs/hensel.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
HENSEL’S LEMMA
KEITH CONRAD
1. Introduction
In the p-adic integers, congruences are approximations: for a and b in Zp, a ≡b mod pn
is the same as |a −b|p ≤1/pn. Turning information modulo one power of p into similar
information modulo a higher power of p can be interpreted as improving an approximation.
Example 1.1. The number 7 is a square mod 3: 7 ≡12 mod 3. Although 7 ̸≡12 mod 9,
we can write 7 as a square mod 9 by replacing 1 with 1 + 3: 7 ≡(1 + 3)2 mod 9. Here are
expressions of 7 as a square modulo further powers of 3:
7 ≡(1 + 3 + 32)2 mod 33,
7 ≡(1 + 3 + 32)2 mod 34,
7 ≡(1 + 3 + 32 + 2 · 34)2 mod 35,
...
7 ≡(1 + 3 + 32 + 2 · 34 + 2 · 37 + 38 + 39 + 2 · 310)2 mod 311.
If we can keep going indeﬁnitely then 7 is a perfect square in Z3 with square root
1 + 3 + 32 + 2 · 34 + 2 · 37 + 38 + 39 + 2 · 310 + · · · .
That we can continue this indeﬁnitely is due to Hensel’s lemma, proved by Hensel in 1904
[4, Sect. 4, pp. 77-84] (see also [5, Chap. 4, Sect. 3-5]). It gives conditions under which the
root of a polynomial mod p lifts to a root in Zp, such as the polynomial X2 −7 with p = 3:
its two roots mod 3 can both be lifted to square roots of 7 in Z3.
We will ﬁrst give a basic version of Hensel’s lemma, illustrate it with examples, and then
other versions that can be applied in cases where the basic version is inadequate.
2. A Basic Version of Hensel’s lemma
Theorem 2.1 (Hensel’s lemma). If f(X) ∈Zp[X] and a ∈Zp satisﬁes
f(a) ≡0 mod p,
f′(a) ̸≡0 mod p
then there is a unique α ∈Zp such that f(α) = 0 in Zp and α ≡a mod p.
Example 2.2. Let f(X) = X2−7. Then f(1) = −6 ≡0 mod 3 and f′(1) = 2 ̸≡0 mod 3, so
Hensel’s lemma tells us there is a unique 3-adic integer α such that α2 = 7 and α ≡1 mod 3.
We saw approximations to α in Example 1.1, e.g., α ≡1 + 3 + 32 + 2 · 34 mod 35.
Proof. We will prove by induction that for each n ≥1 there is an an ∈Zp such that
• f(an) ≡0 mod pn,
• an ≡a mod p.
(After proving this, we’ll show it leads to a solution of f(α) = 0 as a limit.) The case n = 1
is trivial, using a1 = a. If the inductive hypothesis holds for n, we seek an+1 ∈Zp such that
• f(an+1) ≡0 mod pn+1,
• an+1 ≡a mod p.
1

<!-- page 2 -->
2
KEITH CONRAD
Since f(an+1) ≡0 mod pn+1 ⇒f(an+1) ≡0 mod pn, each root of f(X) mod pn+1 reduces
to a root of f(X) mod pn. By the inductive hypothesis there is a root an mod pn such
that an ≡a mod p, so we seek a p-adic integer an+1 such that an+1 ≡an mod pn and
f(an+1) ≡0 mod pn+1. Writing
an+1 = an + pntn
for some tn ∈Zp to be determined, can we make f(an + pntn) ≡0 mod pn+1?
To compute f(an + pntn) mod pn+1, we use a polynomial identity:
(2.1)
f(X + Y ) = f(X) + f′(X)Y + g(X, Y )Y 2
for some polynomial g(X, Y ) ∈Zp[X, Y ]. This formula comes from isolating the ﬁrst two
terms in the binomial theorem: writing f(X) = Pd
i=0 ciXi we have
f(X + Y ) =
d
X
i=0
ci(X + Y )i = c0 +
d
X
i=1
(ci(Xi + iXi−1Y ) + gi(X, Y )Y 2),
where gi(X, Y ) ∈Z[X, Y ]. Thus
f(X + Y ) =
d
X
i=0
ciXi +
d
X
i=1
iciXi−1Y +
d
X
i=1
gi(X, Y )Y 2 = f(X) + f′(X)Y + g(X, Y )Y 2,
where g(X, Y ) = Pd
i=1 cigi(X, Y ) ∈Zp[X, Y ]. This gives us the desired identity.1
To make (2.1) numerical, for all x and y in Zp the number z := g(x, y) is in Zp, so
(2.2)
x, y ∈Zp =⇒f(x + y) = f(x) + f′(x)y + zy2, where z ∈Zp.
In this formula set x = an and y = pntn:
(2.3)
f(an + pntn) = f(an) + f′(an)pntn + zp2nt2
n ≡f(an) + f′(an)pntn mod pn+1
since 2n ≥n + 1.
In f′(an)pntn mod pn+1, the factors f′(an) and tn only matter mod
p since there is already a factor of pn present and the modulus is pn+1. Recalling that
an ≡a mod p, we get f′(an)pntn ≡f′(a)pntn mod pn+1. Therefore from (2.3),
f(an + pntn) ≡0 mod pn+1 ⇐⇒f(an) + f′(a)pntn ≡0 mod pn+1
⇐⇒f′(a)tn ≡−f(an)/pn mod p,
(2.4)
where the ratio f(an)/pn is in Zp since we assumed that f(an) ≡0 mod pn. There is a
solution for tn in (2.4), a congruence mod p, since we assume f′(a) ̸≡0 mod p.
Armed with this choice of tn and setting an+1 = an+pntn, we have f(an+1) ≡0 mod pn+1
and an+1 ≡an mod pn, so in particular an+1 ≡a mod p. This completes the induction.
Starting with a1 = a, our inductive argument has constructed a sequence a1, a2, a3, . . .
in Zp such that f(an) ≡0 mod pn and an+1 ≡an mod pn for all n. The second condition,
an+1 ≡an mod pn, implies that {an} is a Cauchy sequence in Zp. Let α be its limit in Zp.
We want to show f(α) = 0 and α ≡a mod p.
From an+1 ≡an mod pn for all n we get am ≡an mod pn for all m > n, so α ≡an mod pn
by letting m →∞. At n = 1 we get α ≡a mod p. For general n,
α ≡an mod pn =⇒f(α) ≡f(an) ≡0 mod pn =⇒|f(α)|p ≤1
pn .
1The identity (2.1) is similar to Taylor’s formula: f(x + h) = f(x) + f ′(x)h + (f ′′(x)/2!)h2 + · · · . The
catch is that terms in Taylor’s formula have factorials in the denominator, which can require some extra care
when reducing modulo powers of p: think about f ′′(x)/2! mod 2, for instance. What (2.1) essentially does
is extract the ﬁrst two terms of Taylor’s formula and say that what remains has p-adic integral coeﬃcients,
so (2.1) can be reduced mod p, or mod pn for all n ≥1.

<!-- page 3 -->
HENSEL’S LEMMA
3
Since this estimate holds for all n, f(α) = 0.
It remains to show α is the unique root of f(X) in Zp that is congruent to a mod p.
Suppose f(β) = 0 and β ≡a mod p. To show β = α we will show β ≡α mod pn for all n.
The case n = 1 is clear since α and β are both congruent to a mod p. Suppose n ≥1 and
we know that β ≡α mod pn. Then β = α + pnγn with γn ∈Zp, so a calculation similar to
(2.3) implies
f(β) = f(α + pnγn) ≡f(α) + f′(α)pnγn mod pn+1.
Both α and β are roots of f(X), so 0 ≡f′(α)pnγn mod pn+1. Thus f′(α)γn ≡0 mod p.
Since f′(α) ≡f′(a) ̸≡0 mod p, we have γn ≡0 mod p, which implies β ≡α mod pn+1.
□
Remark 2.3. Since an + pntn mod pn+1 only depends on tn mod p, and tn satisfying (2.4)
is unique mod p, the an ∈Zp where (i) f(an) ≡0 mod pn and (ii) an ≡a mod p is unique
modulo pn. Or an argument similar to the last paragraph in the proof shows for each n ≥1
that f(X) has a unique root mod pn that reduces to a mod p. Either way, in Theorem 2.1
we can think about the uniqueness of the lifting of the mod p root in two ways: it has a
unique lifting to a root in Zp or it has a unique lifting to a root in Zp/(pn) for all n ≥1.
Remark 2.4. If f(X) ∈Z[X] and a ∈Z, then g(X, Y ) in (2.1) is in Z[X, Y ] and z in (2.2)
is in Z. Use this to check that the inductive reasoning used in the proof before passing to
a p-adic limit near the end holds with Z in place of Zp, so for all n ≥1 there is an an ∈Z
such that f(an) ≡0 mod pn and an ≡a mod p, and such an is unique in Z/(pn).
The rest of this section has applications of Hensel’s lemma.
The hypotheses f(a) ≡
0 mod p and f′(a) ̸≡0 mod p in Hensel’s lemma are equivalent to saying a mod p is a
simple root of f(X) mod p: f(X) ≡(X −a)g(X) mod p where g(a) ̸≡0 mod p.
Example 2.5. Let f(X) = X3 −2. We have f(3) ≡0 mod 5 and f′(3) ̸≡0 mod 5, or
X3 −2 ≡(X −3)(X2 + 3X + 9) mod 5 where the second factor doesn’t vanish at 3 mod 5.
By Hensel’s lemma with a = 3 there is a unique cube root of 2 in Z5 that is congruent to
3 mod 5. It is 3 + 2 · 52 + 2 · 53 + · · · . Since X3 −2 ≡(X −4)(X −7)(X −20) mod 31, by
Hensel’s lemma there are three cube roots of 2 in Z31 and they are distinguished by their
values modulo 31. These numbers begin as 4+9·31+4·312 +· · · , 7+13·31+29·312 +· · · ,
and 20 + 8 · 31 + 28 · 312 + · · · ,
Example 2.6. Let f(X) = X3−X2−2 ≡X3−X2 ≡X2(X −1) mod 2, so f(0) ≡0 mod 2
and f′(0) ≡0 mod 2, while f(1) ≡0 mod 2 and f′(1) ̸≡0 mod 2: 0 is a multiple root mod
2 and 1 is a simple root mod 2. By Hensel’s lemma with a = 1, there is a unique α ∈Z2
such that f(α) = 0 and α ≡1 mod 2. Explicitly, α = 1 + 2 + 24 + 25 + 210 + · · · .
Although 0 is a root of f(X) mod 2, it does not lift to a root in Z2 since it doesn’t even
lift to a root mod 4: f(0) ≡2 mod 4 and f(2) ≡2 mod 4, so if β ∈Z2 and β ≡0 mod 2
then β ≡0 or 2 mod 4 and therefore f(β) ≡2 ̸≡0 mod 4.
Example 2.7. Let f(X) = X3 −X2 −2X −8 ≡X3 −X2 ≡X2(X −1) mod 2. As in
the previous example, 0 is a multiple root mod 2 and 1 is a simple root mod 2, so Hensel’s
lemma with a = 1 tells us f(X) has a unique root α ∈Z2 such that α ≡1 mod 2. Explicitly,
α = 1 + 2 + 22 + 24 + 26 + 29 + · · · .
Unlike the previous example, the multiple root 0 mod 2 lifts to roots in Z2, in fact to two
of them, but we can’t explain this with the basic version of Hensel’s lemma. We’ll return
to this example in Example 4.4 after meeting a stronger version of Hensel’s lemma.
Example 2.8. For each positive integer n not divisible by p and each u ≡1 mod pZp, u is
an nth power in Z×
p . Apply Hensel’s lemma to f(X) = Xn −u with a = 1: f(1) = 1 −u ≡
0 mod p and f′(1) = n ̸≡0 mod p. Therefore there is a unique solution to αn = u in Zp

<!-- page 4 -->
4
KEITH CONRAD
such that α ≡1 mod p. Example 1.1 is the case u = 7, p = 3, and n = 2: 7 has a unique
3-adic square root that is ≡1 mod 3.
Example 2.9. For an odd prime p, suppose u ∈Z×
p is a square mod p. We will show u is
a square in Z×
p . For example, 2 ≡32 mod 7 and that implies 2 is a square in Z×
7 .
Write u ≡a2 mod p, so a ̸≡0 mod p.
For the polynomial f(X) = X2 −u we have
f(a) ≡0 mod p and f′(a) = 2a ̸≡0 mod p, since p is not 2, so Hensel’s lemma tells us that
f(X) has a root in Zp that reduces to a mod p, which means u is a square in Z×
p . Conversely,
if u ∈Z×
p is a p-adic square, say u = v2, then 1 = |v|2
p, so v ∈Z×
p and u ≡v2 mod p. Thus
the elements of Z×
p that are squares in Qp are precisely those that reduce to squares mod
p. For example, the nonzero squares mod 7 are 1, 2, and 4, so u ∈Z×
7 is a 7-adic square if
and only if u ≡1, 2, or 4 mod 7.
This result can have problems when p = 2 because 2a ≡0 mod 2. In fact the lifting of a
square root mod 2 to a 2-adic square root really does have a problem: 3 ≡12 mod 2 but 3
is not a square in Z2 since 3 is not a square mod 4 (the squares mod 4 are 0 and 1). And 3
is not a square in Q2 either because a hypothetical square root in Q2 would have to be in
Z2: if α2 = 3 in Q2 then |α|2
2 = |3|2 = 1, so |α|2 = 1, and thus α ∈Z×
2 ⊂Z2.
Example 2.10. For each integer k between 0 and p −1, kp ≡k mod p. Letting f(X) =
Xp −X, we have f(k) ≡0 mod p and f′(k) = pkp−1 −1 ≡−1 ̸≡0 mod p. By Hensel’s
lemma there is a unique ωk ∈Zp such that ωp
k = ωk and ωk ≡k mod p. For instance, always
ω0 = 0 and ω1 = 1, and when p > 2, ωp−1 = −1. Other ωk for p > 2 are more interesting.
For p = 5, ωk is a root of X5 −X = X(X4 −1) = X(X −1)(X + 1)(X2 + 1). Thus ω2 and
ω3 in Z5 are square roots of −1:2
ω2 = 2 + 5 + 2 · 52 + 53 + 3 · 54 + 4 · 55 + 2 · 56 + 3 · 57 + · · · ,
ω3 = 3 + 3 · 5 + 2 · 52 + 3 · 53 + 54 + 2 · 56 + 57 + · · · .
For general p the numbers ωk for 0 ≤k ≤p −1 are distinct since they are already distinct
when reduced mod p, so Xp −X = X(Xp−1 −1) splits completely in Zp[X]. Its roots in Zp
are 0 and (p −1)th roots of unity. The number ωk in Zp is called the (p-adic) Teichmuller
representative for k: ωk is the unique lifting of k mod p to a root of Xp −X in Zp.
Example 2.11. As an application to solving equations in Qp, not just Zp, for p ̸= 2 and
a ∈Qp we’ll show the equation y2 = x4 + a has a p-adic solution (x, y) whenever |x|p is
suﬃciently large compared to |a|p.
Rewrite the equation as y2 = x4(1+a/x4). Since the ﬁrst term x4 is a square for all x, it
suﬃces to ﬁnd a condition on x that implies 1+a/x4 is a square in Qp. When p ̸= 2, such a
condition is |a/x4|p < 1, i.e., |x|p > |a|1/4
p
: for such x, a/x4 ∈pZp, so 1+a/x4 ≡1 mod pZp,
and therefore 1 + a/x4 is a square in Z×
p by Examples 2.8 or 2.9.
We’ll extend this to the case p = 2 in Example 4.6.
3. Roots of unity in Qp via Hensel’s Lemma
Hensel’s lemma is often considered to be a method of ﬁnding roots to polynomials, but
the existence of a root is just one aspect. There is also a uniqueness part to Hensel’s lemma:
it tells us there is a unique root within a certain distance of an approximate root. We’ll use
the uniqueness to ﬁnd all of the roots of unity in Qp.
Theorem 3.1. The roots of unity in Qp are the (p −1)th roots of unity for p odd and ±1
for p = 2.
2Hensel found ω2 and ω3 to 4 digits when he factored X2 + 1 over Q5, written by him as K(5) [4, p. 77].

<!-- page 5 -->
HENSEL’S LEMMA
5
Proof. If xn = 1 in Qp then |x|n
p = 1, so |x|p = 1. This means every root of unity in Qp lies
in Z×
p . Therefore we work in Z×
p right from the start.
First let’s consider roots of unity of order relatively prime to p. Assume ζ1 and ζ2 are
roots of unity in Z×
p with order prime to p. Letting m be the product of the orders of
these roots of unity, they are both roots of f(X) = Xm −1 and m is prime to p. Since
|f′(ζi)|p = |mζm−1
i
|p = 1, the uniqueness aspect of Hensel’s lemma implies that the only
root α of Xm −1 satisfying |α −ζ1|p < 1 is ζ1. So if ζ2 ≡ζ1 mod pZp then ζ2 = ζ1: distinct
roots of unity in Z×
p having order prime to p must be incongruent mod p. In Example
2.10 we found in each nonzero coset mod pZp a root of Xp−1 −1, and p −1 is prime to
p. Therefore each congruence class mod pZp contains a (p −1)th root of unity, so the only
roots of unity of order prime to p in Qp are the roots of Xp−1 −1.
Now we consider roots of unity of p-power order. We will show the only pth root of unity
in Z×
p is 1 for odd p and the only 4th roots of unity in Z×
2 are ±1. This implies the only
pth power roots of unity in Z×
p are 1 for odd p and ±1 for p = 2. (For instance, if there
were a nontrivial p-th power root of unity in Qp for p ̸= 2 then there would be a root of
unity in Qp of order p, but we’re going to show there aren’t any of those.) This part of the
proof will not use Hensel’s lemma.
We ﬁrst consider odd p and suppose ζp = 1 in Z×
p with ζ ̸= 1. Since ζp ≡ζ mod pZp,
we have ζ ≡1 mod pZp. Therefore ζ = 1 + py with y ∈Zp. Since ζ is not 1, ζ is a root
of (Xp −1)/(X −1) = 1 + X + X2 + · · · + Xp−1. For all integers k ≥0, ζk = (1 + py)k ≡
1 + kpy mod p2Zp by the binomial theorem, so
0 = 1 + ζ + ζ2 + · · · + ζp−1
=
p−1
X
k=0
ζk
≡
p−1
X
k=0
(1 + kpy) mod p2Zp
≡p + p(p −1)
2
py mod p2Zp.
(3.1)
Since p is odd, (p −1)/2 ∈Z, so (3.1) implies 0 ≡p mod p2, which is a contradiction.
Therefore there is no pth root of unity in Qp other than 1.
Now we turn to p = 2. We want to show the only 4th roots of unity in Z×
2 are ±1. If
ζ ∈Z×
2 is a 4th root of unity and ζ ̸= ±1 then ζ2 = −1, so ζ2 ≡−1 mod 4Z2. However,
ζ ∈Z×
2 =⇒ζ ≡1 or 3 mod 4Z2 =⇒ζ2 ≡1 mod 4Z2
and 1 ̸≡−1 mod 4Z2. Thus there is no 4th root of unity in Q2 besides ±1.
For prime p, a root of unity is a (unique) product of a root of unity of p-power order
and a root of unity of order prime to p, so the only roots of unity in Qp are the roots of
Xp−1 −1 for p ̸= 2 and ±1 for p = 2.
□
Here are the roots of X7 −X in Z7 besides ω0 = 0, ω1 = 1, and ω6 = −1.
ω2 = 2 + 4 · 7 + 6 · 72 + 3 · 73 + 0 · 74 + 2 · 75 + 6 · 76 + 2 · 77 + · · · ,
ω3 = 3 + 4 · 7 + 6 · 72 + 3 · 73 + 0 · 74 + 2 · 75 + 6 · 76 + 2 · 77 + · · · ,
ω4 = 4 + 2 · 7 + 0 · 72 + 3 · 73 + 6 · 74 + 4 · 75 + 0 · 76 + 4 · 77 + · · · ,
ω5 = 5 + 2 · 7 + 0 · 72 + 3 · 73 + 6 · 74 + 4 · 75 + 0 · 76 + 4 · 77 + · · · .

<!-- page 6 -->
6
KEITH CONRAD
The 7-adic digits of ω2 and ω3 appear to be matching after the ﬁrst digit, as do those in
ω4 and ω5. More speciﬁcally, it looks like ω3 −ω2 = 1 and ω5 −ω4 = 1. Let’s explain that
from the factorization
X7 −X = X(X6 −1) = X(X3 −1)(X3 + 1) = X(X −1)(X2 + X + 1)(X + 1)(X2 −X + 1).
Each ωk is a root of one polynomial on the right side. Since X2 + X + 1 has roots 2 mod 7
and 4 mod 7 in Z/(7), it has roots ω2 and ω4 in Z7. Its roots have sum −1 (why?), so
ω2 + ω4 = −1. Also ω2 and −ω5 are both roots of X7 −X that reduce to 2 mod 7, so the
uniqueness in Hensel’s lemma implies ω2 = −ω5. Thus ω5 −ω4 = −ω2 −(−1 −ω2) = 1. It’s
left to the reader to explain why ω3 −ω2 = 1.
Using the roots of unity in Qp, the following theorem gives multiplicative decompositions
of Z×
p and Q×
p that are analogues of R× = {±1} × R>0 and C× = S1 × R>0. Write µn for
the nth roots of unity.
Theorem 3.2. For all p, Z×
p = µp−1×(1+pZp) and Q×
p = pZ×Z×
p = pZ×µp−1×(1+pZp).
When p = 2, Z×
2 = {±1} × (1 + 4Z2) and Q×
2 = 2Z × Z×
2 = 2Z × {±1} × (1 + 4Z2).
Proof. Since pZ × Z×
p = Q×
p (by the map (pk, u) 7→pku), it suﬃces to explain the decom-
position Z×
p = µp−1 × (1 + pZp) for all p and Z×
2 = {±1} × (1 + 4Z2).
For each u ∈Z×
p , Example 2.10 says there is a (p −1)th root of unity ω such that
u ≡ω mod pZp. Let v = u/ω, so v ∈1 + pZp and u = ωv. Such a decomposition of u
is unique, since if u = ω′v′ where ω′p−1 = 1 and v′ ∈1 + pZp then reducing the equation
ωv = ω′v′ modulo p tells us ω ≡ω′ mod p, so ω = ω′ by the uniqueness of lifting roots of
Xp −X from Z/pZ to Zp in Hensel’s lemma. Thus ωv = ωv′, so v = v′.
The map µp−1 × (1 + pZp) →Z×
p given by (ω, v) 7→ωv is a group homomorphism
and the previous paragraph shows it is both surjective and injective, and thus bijective,
so we can write Z×
p = µp−1 × (1 + pZp). This decomposition is trivial when p = 2 since
µ2−1 = {1}, but in this case we can reﬁne the decomposition by using the roots of unity ±1,
which are distinguished modulo 4 rather than modulo 2. For u ∈Z×
2 either u ≡1 mod 4
or u ≡3 mod 4, so there is one ω ∈{±1} such that u ≡ω mod 4.
From this we get
Z×
2 = {±1} × (1 + 4Z2) in the same way we showed Z×
p = µp−1 × (1 + pZp).
□
4. A stronger version of Hensel’s Lemma
The hypotheses of Theorem 2.1 are f(a) ≡0 mod p and f′(a) ̸≡0 mod p. This means
a mod p is a simple root of f(X) mod p. We will now discuss a more general version of
Hensel’s lemma than Theorem 2.1. It can be applied to cases where a mod p is a multiple
root of f(X) mod p: f(a) ≡0 mod p and f′(a) ≡0 mod p. This will allow us to describe
squares in Z×
2 and, more generally, pth powers in Z×
p .
Theorem 4.1 (Hensel’s lemma). Let f(X) ∈Zp[X] and a ∈Zp satisfy
|f(a)|p < |f′(a)|2
p.
There is a unique α ∈Zp such that f(α) = 0 in Zp and |α −a|p < |f′(a)|p. Moreover,
(1) |α −a|p = |f(a)/f′(a)|p < |f′(a)|p,
(2) |f′(α)|p = |f′(a)|p.
Since f′(a) ∈Zp, |f′(a)|p ≤1. If |f′(a)|p = 1 then the hypotheses of Theorem 4.1 reduce
to those of Theorem 2.1: saying |f(a)|p < 1 and |f′(a)|p = 1 means f(a) ≡0 mod p and
f′(a) ̸≡0 mod p. Theorem 4.1 actually goes beyond the conclusions of Theorem 2.1 when
the hypotheses of Theorem 2.1 hold, since we learn in Theorem 4.1 exactly how far away
the root α is from the approximate root a. But the main point of Theorem 4.1 is that it
allows for the possibility that |f′(a)|p < 1, which isn’t covered by Theorem 2.1 at all.

<!-- page 7 -->
HENSEL’S LEMMA
7
We will prove Theorem 4.1 by two methods, in Sections 5 and 6. Here are some applica-
tions where the polynomial has a multiple root mod p.
Example 4.2. Let f(X) = X4−7X3+2X2+2X+1. Then f(X) ≡(X+1)2(X2+1) mod 3
and we notice 2 mod 3 is a double root. Since |f(2)|3 = 1/27 and |f′(2)|3 = |−42|3 = 1/3,
the condition |f(2)|3 < |f′(2)|2
3 holds, so there is a unique root α of f(X) in Z3 such that
|α −2|3 < 1/3, i.e., α ≡2 mod 9.
In fact there are two roots of f(X) in Z3:
2 + 3 + 2 · 32 + 2 · 33 + 2 · 34 + 2 · 36 + · · · and 2 + 32 + 34 + 2 · 35 + 2 · 36 + · · · .
The second root reduces to 2 mod 9, and is α. The ﬁrst root reduces to 5 mod 9, and its
existence can be veriﬁed by checking |f(5)|3 = 1/27 < |f′(5)|2
3 = 1/9.
Example 4.3. Let f(X) = X3 −10 and g(X) = X3 −5. We have f(X) ≡(X −1)3 mod 3
and g(X) ≡(X−2)3 mod 3: 1 is an approximate 3-adic root of f(X) and 2 is an approximate
3-adic root of g(X). Can these be reﬁned to 3-adic roots? The basic form of Hensel’s lemma
in Theorem 2.1 can’t be used since the polynomials do not have simple roots mod 3. Instead
we will use the stronger form of Hensel’s lemma in Theorem 4.1.
Since |f(1)|3 = 1/9 and |f′(1)|3 = 1/3, we don’t have |f(1)|3 < |f′(1)|2
3, so Theorem 4.1
can’t be used on f(X) with a = 1. However, |f(4)|3 = 1/27 and |f′(4)|3 = 1/3, so we can
use Theorem 4.1 on f(X) with a = 4: there is a unique root α of X3 −10 in Z3 satisfying
|α −4|3 < 1/3, so α ≡4 mod 9. The expansion of α begins as 1 + 3 + 32 + 2 · 36 + 37 + · · · .
Turning to g(X), we have |g(2)|3 = 1/3 and |g′(2)|3 = 1/9, so we can’t apply Theorem
4.1 with a = 2. In fact there is no root of g(X) in Q3. If there were a root α in Q3 then
α3 = 5, so |α|3 = 1, and thus α ∈Z3. Then α3 ≡5 mod 3n, so 5 would be a cube modulo
every power of 3. But 5 is not a cube mod 9 (the only cubes mod 9 are 0, 1, and 8).
Therefore the mod 3 root of X3 −5 does not lift to a 3-adic root of X3 −5.
Example 4.4. Let f(X) = X3−X2−2X −8 ≡X3−X2 ≡X2(X −1) mod 2. By Example
2.7, f(X) has a unique root α = 1 + 2 + 22 + 24 + 26 + 29 + · · · that is 1 mod 2. Now we’ll
show there are two roots in Z2 that are 0 mod 2. Since f(0) = −8 and f′(0) = −2, we have
|f(0)|2 = 1/8 < |f′(0)|2
2 = 1/4, so f(X) has a unique root β in Z2 such that |β|2 < 1/2,
meaning β ≡0 mod 4. Also f(2) = −8 and f′(2) = 6, so |f(2)|2 = 1/8 < |f′(2)|2
2 = 1/4,
so f(X) has a unique root γ in Z2 such that |γ −2|2 < 1/2, so γ ≡2 mod 4. Explicitly,
β = 22 + 24 + 26 + 27 + 28 + 210 + · · · and γ = 2 + 22 + 24 + 26 + 27 + 28 + 29 + · · ·
Theorem 4.5. If u ∈Z×
2 then u is a square in Q2 if and only if u ≡1 mod 8Z2.
Proof. If u = v2 in Q2 then 1 = |v|2
2, so v ∈Z×
2 . In Z2/8Z2 ∼= Z/8Z, the units are 1, 3,
5, and 7, whose squares are all congruent to 1 mod 8, so u = v2 ≡1 mod 8Z2. To show,
conversely, that all u ∈Z×
2 satisfying u ≡1 mod 8Z2 are squares in Z×
2 , let f(X) = X2 −u
and use a = 1 in Theorem 4.1. We have |f(1)|2 = |1 −u|2 ≤1/8 and |f′(1)|2 = |2|2 = 1/2,
so |f(1)|2 < |f′(1)|2
2. Therefore X2 −u has a root in Z2, so u is a square in Z2.
□
Example 4.6. We saw in Example 2.11 that for p ̸= 2 and a ∈Qp, y2 = x4 + a has a
solution in Qp when |x|4
p > |a|p. With Theorem 4.5 we’ll get an analogue of this for p = 2.
Rewriting the equation as y2 = x4(1 + a/x4), we want 1 + a/x4 to be a square in Q2,
and by Theorem 4.5 such a condition is |a/x4|2 ≤1/8, since then 1 + a/x4 ≡1 mod 8Z2.
The same method, using the stronger version of Hensel’s lemma, shows for prime p,
a ∈Qp, and n | m in Z+ that the equation yn = xm + a has a p-adic solution (x, y)
whenever |x|p is suﬃciently large in terms of |a|p, m, and n. Details are left to the reader.
Theorem 4.7. If p ̸= 2 and u ∈Z×
p , then u is a pth power in Qp if and only if u is a pth
power modulo p2.

<!-- page 8 -->
8
KEITH CONRAD
Proof. If u = vp in Qp then 1 = |v|p
p, so v ∈Z×
p : we only need to look for pth roots of u in
Z×
p . Let f(X) = Xp−u. In order to use Theorem 4.1 on f(X), we seek an a ∈Z×
p such that
|f(a)|p < |f′(a)|2
p. This means |ap −u|p < |pap−1|2
p = 1/p2, or equivalently ap ≡u mod p3.
Provided u is a pth power modulo p3, Theorem 4.1 tells us that Xp −u has a root in Zp,
so u is a pth power. The criterion in the theorem, however, has modulus p2 rather p3. We
need to do some work to bootstrap an approximate pth root from modulus p2 to modulus
p3 in order to apply Theorem 4.1.
Suppose u ≡ap mod p2 for some a ∈Zp. Then a ∈Z×
p and u/ap ≡1 mod p2. Write
u/ap ≡1 + p2c mod p3, where 0 ≤c ≤p −1. By the binomial theorem,
(1 + pc)p = 1 + p(pc) +
p
X
k=2
p
k

(pc)k.
The terms for k ≥3 are obviously divisible by p3 and the term at k = 2 is
 p
2

(pc)2 = p−1
2 p3c2,
which is also divisible by p3 since p > 2.
Therefore (1 + pc)p ≡1 + p2c mod p3, so u/ap ≡(1 + pc)p mod p3. Now we can write
u
ap(1 + pc)p ≡1 mod p3.
From Theorem 4.1, a p-adic integer that is congruent to 1 mod p3 is a pth power (see the
ﬁrst paragraph again). Thus u/(ap(1 + pc)p) is a pth power, so u is a pth power.
□
Theorem 4.7 is false for p = 2: the criterion for an element of Z×
2 to be a 2-adic square
needs modulus 23, not modulus 22, by Theorem 4.5. For instance, 5 mod 4 is a square but 5
is not a 2-adic square since 5 ̸≡1 mod 8. Theorem 4.7 explains what we found in Example
4.3: 10 is a 3-adic cube and 5 is not, since 10 mod 9 is a cube and 5 mod 9 is not a cube.
Remark 4.8. Hensel’s lemma in Theorem 4.1 says a root mod p lifts uniquely to a root
in Zp under weaker conditions than Hensel’s lemma in Theorem 2.1, but there may not be
a unique root mod pn, unlike in Theorem 2.1 (Remark 2.3). Consider Example 4.3: in Z3,
X3 = 10 has one solution 1 + 3 + 32 + 2 · 36 + · · · , but for n ≥2, X3 ≡10 mod 3n has
3 solutions, not 1. One of the solutions mod 3n lifts to three solutions mod 3n+1 and two
don’t. (For instance, solutions mod 27 are 4, 13, and 22 and only 13 lifts to solutions mod
81, in fact to 13, 40, and 67 mod 27.) This is consistent with a unique root in Z3 since the
3 solutions mod 3n are congruent modulo 3n−1 and thus are close: they have a common
limit in Z3 as n →∞.
Another example is X2 = 1. It has two solutions in Z2, but X2 ≡1 mod 2n for n ≥2
has 4 solutions: 1, −1, 1 + 2n−1, and −1 + 2n−1 mod 2n. As n →∞, the ﬁrst and third
solutions mod 2n tend to 1 and the second and fourth solutions mod 2n tend to −1.
5. First Proof of Theorem 4.1: Newton’s Method
Our ﬁrst proof of Theorem 4.1 will use Newton’s method and is a modiﬁcation of [6,
Chap. II, §2, Prop. 2].
Proof. As in Newton’s method from real analysis, deﬁne a sequence {an} in Qp by a1 = a
and
(5.1)
an+1 = an −f(an)
f′(an)
for n ≥1. Set t = |f(a)/f′(a)2|p < 1. We will show by induction on n that
(i) |an|p ≤1, i.e., an ∈Zp,
(ii) |f′(an)|p = |f′(a1)|p,

<!-- page 9 -->
HENSEL’S LEMMA
9
(iii) |f(an)|p ≤|f′(a1)|2
pt2n−1.
For n = 1 these conditions are all clear. Note in particular that we have equality in (iii)
and f′(a1) ̸= 0 since |f(a1)|p < |f′(a1)|2
p.
For the inductive step, we need two polynomial identities. The ﬁrst one, for F(X) ∈
Zp[X], is
(5.2)
F(X + Y ) = F(X) + F ′(X)Y + g(X, Y )Y 2
for some g(X, Y ) ∈Zp[X, Y ]. This is (2.1) from the proof of Theorem 2.1. So
(5.3)
x, y ∈Zp =⇒F(x + y) = F(x) + F ′(x)y + zy2, where z ∈Zp
with z = g(x, y). The second polynomial identity we need is that for F(X) ∈Zp[X],
F(X) −F(Y ) = (X −Y )G(X, Y )
for some G(X, Y ) ∈Zp[X, Y ]. This comes from X −Y being a factor of Xi −Y i for all
i ≥1. Writing F(X) = Pm
i=0 biXi,
F(X) −F(Y ) =
m
X
i=1
bi(Xi −Y i)
and we can factor X −Y out of each term on the right. For x and y in Zp, G(x, y) ∈Zp, so
(5.4)
x, y ∈Zp =⇒|F(x) −F(y)|p = |x −y|p|G(x, y)|p ≤|x −y|p.
Assume (i), (ii), and (iii) are true for n. To prove (i) for n + 1, ﬁrst note an+1 is deﬁned
since f′(an) ̸= 0 by (ii). To prove (i) it suﬃces to show |f(an)/f′(an)|p ≤1. Using (ii) and
(iii) for n, we have |f(an)/f′(an)|p = |f(an)/f′(a1)|p ≤|f′(a1)|pt2n−1 < 1 since t < 1.
To prove (ii) for n+1, (iii) for n implies |f(an)|p < |f′(a1)|2
p since t < 1 (and |f′(a1)|p ̸= 0),
so by (5.4) with F(X) = f′(X),
|f′(an+1) −f′(an)|p ≤|an+1 −an|p = |f(an)|p
|f′(an)|p
= |f(an)|p
|f′(a1)|p
< |f′(a1)|p = |f′(an)|p,
so |f′(an+1)|p = |f′(an)|p = |f′(a1)|p.
To prove (iii) for n + 1, we use (5.3) with F(X) = f(X), x = an and y = −f(an)/f′(an):
f(an+1) = f(x + y) = f(an) + f′(an)

−f(an)
f′(an)

+ z
 f(an)
f′(an)
2
= z
 f(an)
f′(an)
2
,
where z ∈Zp. (Note |y|p = |f(an)|p/|f′(an)|p < 1.) Thus, by (iii) for n,
|f(an+1)|p ≤

f(an)
f′(an)

2
p
= |f(an)|2
p
|f′(a1)|2p
≤|f′(a1)|4
pt2n
|f′(a1)|2p
= |f′(a1)|2
pt2n.
This completes the induction.
Now we show {an} is Cauchy in Qp. From the recursive deﬁnition of this sequence,
(5.5)
|an+1 −an|p =

f(an)
f′(an)

p
= |f(an)|p
|f′(a1)|p
≤|f′(a1)|pt2n−1,
where we used (ii) and (iii). Thus {an} is Cauchy. Let α be its limit, so |α|p ≤1 by (i), i.e.,
α ∈Zp. Letting n →∞in (ii) and (iii) we get |f′(α)|p = |f′(a1)|p = |f′(a)|p and f(α) = 0.

<!-- page 10 -->
10
KEITH CONRAD
To show |α −a|p = |f(a)/f′(a)|p, it’s true if f(a) = 0 since then an = a1 = a for all n,
so α = a.3 If f(a) ̸= 0 then we will show |an −a|p = |f(a)/f′(a)|p for all n ≥2 and let
n →∞. When n = 2 use the deﬁnition of a2 in terms of a1 = a. For all n ≥2, by (5.5)
(5.6)
|an+1 −an|p ≤|f′(a1)|pt2n−1 ≤|f′(a1)|pt2 < |f′(a1)|pt = |f′(a)|pt =

f(a)
f′(a)

p
,
where t ∈(0, 1) since f(a) ̸= 0. If |an −a|p = |f(a)/f′(a)|p then |an+1 −an|p < |an −a|p by
(5.6), so |an+1 −a|p = |(an+1 −an) + (an −a)|p = |an −a|p = |f(a)/f′(a)|p.
The last thing to do is show α is the only root of f(X) in the ball {x ∈Zp : |x −a|p <
|f′(a)|p}.
This will not use anything about Newton’s method.
Assume f(β) = 0 and
|β −a|p < |f′(a)|p. Since |α −a|p < |f′(a)|p we have |β −α|p < |f′(a)|p. Write β = α + h,
so h ∈Zp. Then by (5.3) with F(X) = f(X),
0 = f(β) = f(α + h) = f(α) + f′(α)h + zh2 = f′(α)h + zh2
for some z ∈Zp. If h ̸= 0 then f′(α) = −zh, so |f′(α)|p ≤|h|p = |β −α|p < |f′(a)|p. But
|f′(α)|p = |f′(a)|p, so we have a contradiction. Thus h = 0, so β = α.
□
Before we give a second proof of Theorem 4.1, it’s worth noting that the an’s converge
to α very rapidly. From the inequality |an+1 −an|p ≤|f′(a1)|pt2n−1 for all n ≥1 we obtain
by the strong triangle inequality |am −an|p ≤|f′(a1)|pt2n−1 for all m > n. Letting m →∞,
(5.7)
|α −an|p ≤|f′(a1)|pt2n−1 = |f′(a)|pt2n−1 = |f′(a)|p

f(a)
f′(a)2

2n−1
p
.
Since |f(a)/f′(a)2|p < 1, the exponent 2n−1 tells us that the number of initial p-adic digits
in an that agree with those in the limit α is at least doubling at each step.
Example 5.1. Let f(X) = X2 −7 in Q3[X]. It has two roots in Z3:
r = 1 + 3 + 32 + 2 · 34 + 2 · 37 + 38 + 39 + · · · ,
s = 2 + 3 + 32 + 2 · 33 + 2 · 35 + 2 · 36 + 38 + 39 + · · · .
Starting with a1 = 1, for which |f(a1)/f′(a1)2|3 = 1/3, Newton’s recursion (5.1) has limit
α where |α −a1|3 < |f′(a1)|3 = 1, so α ≡a1 ≡1 mod 3. Thus α = r. For example,
a4 = 977
368 = 1 + 3 + 32 + 2 · 34 + 2 · 37 + 39 + 310 + · · · ,
which has the same 3-adic digits as r up through terms including 37 (the ﬁrst 8 digits). The
estimate in (5.7) says |r−an|3 ≤|f′(a1)|3(1/3)2n−1 = (1/3)2n−1 for all n. Using a computer,
this inequality is an equality for 1 ≤n ≤10.
Example 5.2. Let f(X) = X2 −17 in Q2[X]. It has two roots in Z2:
r = 1 + 23 + 25 + 26 + 27 + 29 + · · · ,
s = 1 + 2 + 22 + 24 + 28 + · · · .
Using Newton’s recursion (5.1) for f(X) with initial seed a ∈Z×
2 , we need |a2−17|2 < |2a|2
2,
which is the same as a2 ≡17 mod 8, and this congruence works for all a ∈Z×
2 . Therefore
(5.1) with a1 ∈Z×
2 converges to r or s. Since |f′(a)|2 = 1/2 for a ∈Z×
2 , (5.1) with a1 = a
has a limit α satisfying |α −a|2 < |f′(a)|2 = 1/2, so α ≡a mod 4: if a ≡1 mod 4 then
3The case f(a) = 0 was not covered in an earlier draft and this omission was found when the proof here
was formalized using the Lean theorem prover [8, p. 8].

<!-- page 11 -->
HENSEL’S LEMMA
11
α = r, and if a ≡3 mod 4 then α = s. By (5.7), |α −an|2 ≤|f′(a)|2(|f(a)/f′(a)2|2)2n−1 =
(1/2)(4|a2 −17|2)2n−1. For a few choices of a, this inequality is an equality for 1 ≤n ≤10:
• When a = 1, |r −an|2 = (1/2)2n+1 for 1 ≤n ≤10.
• When a = 3, |s −an|2 = (1/2)2n−1+1 for 1 ≤n ≤10.
• When a = 5, |r −an|2 = (1/2)2n−1+1 for 1 ≤n ≤10.
Example 5.3. Let’s solve X2 −1 = 0 in Q3. This might seem silly, since we know the
solutions are ±1, but let’s check how an initial approximation aﬀects the 3-adic limit. We
use a1 = 2. (If we used a1 = 1 then an = 1 for all n, which is not interesting.) When
f(X) = X2 −1 the recursion for Newton’s method is
an+1 = an −f(an)
f′(an) = an −a2
n −1
2an
= a2
n + 1
2an
= 1
2

an + 1
an

.
Since |f(2)|3 = 1/3 < |f′(2)|2
3, Newton’s recursion with a1 = 2 converges in Q3. What is
the limit? Since a1 ≡−1 mod 3, we have an ≡−1 mod 3 for all n by induction: if an ≡
−1 mod 3 then an+1 = (1/2)(an + 1/an) ≡(1/2)(−1 + 1/(−1)) ≡(1/2)(−2) ≡−1 mod 3.
Thus limn→∞an = −1 in Q3. What makes this interesting is that in R all an are positive so
the sequence of rational numbers {an} converges to 1 in R and to −1 in Q3. The table below
illustrates the rapid convergence in R and Q3 (the 3-adic expansion of −1 is 2 = 2222 . . .).
n
an
Decimal approx.
3-adic approx.
1
2
2.00000000
20000000
2
5/4
1.25000000
22020202
3
41/40
1.02500000
22220222
4
3281/3280
1.00030487
22222222
Theorem 4.1 has Theorem 2.1 as the special case when |f′(a)|p = 1. Using a change
of variables, we will show Theorem 4.1 follows from Theorem 2.1, so the basic and strong
versions of Hensel’s lemma are in fact equivalent!
Theorem 5.4. Theorem 2.1 implies Theorem 4.1.
Proof. Suppose f(X) ∈Zp[X] and a ∈Zp satisﬁes |f(a)|p < |f′(a)|2
p. We will use Theorem
2.1 to show f(X) has a unique root α ∈Zp such that |α −a|p < |f′(a)|p, and in fact
|α −a|p = |f(a)/f′(a)|p and |f′(α)|p = |f′(a)|p.
Since |f(a)|p < |f′(a)|2
p, set b = f(a)/f′(a)2, so f(a) = f′(a)2b and |b|p < 1. A root
α ∈Zp of f(X) where |α −a|p < |f′(a)|p is a root of the form a + f′(a)s with |s|p < 1. We
thus want to show f(a + f′(a)s) = 0 for a unique s ∈Zp with |s|p < 1 and also show that
in fact |s|p = |f(a)/f′(a)2|. By the polynomial identity (5.2) with F(X) = f(X), there is a
polynomial g(X, Y ) ∈Zp[X, Y ] such that
f(X + Y ) = f(X) + f′(X)Y + g(X, Y )Y 2,
so for all s ∈Zp,
f(a + f′(a)s) = f(a) + f′(a)(f′(a)s) + g(a, f′(a)s)(f′(a)s)2
= f′(a)2b + f′(a)2s + g(a, f′(a)s)f′(a)2s2
= f′(a)2(b + s + g(a, f′(a)s)s2).
Set h(X) = b+X +g(a, f′(a)X)X2 ∈Zp[X]. Since h(X) has constant term b = f(a)/f′(a)2
and linear coeﬃcient 1, |h(0)|p = |b|p < 1 and |h′(0)|p = |1|p = 1. Theorem 2.1 implies
there is a unique β ∈Zp such that h(β) = 0 and |β|p < 1, so α := a + f′(a)β is the unique
root of f(X) in Zp such that |α −a|p < |f′(a)|p.

<!-- page 12 -->
12
KEITH CONRAD
To show |α −a|p = |f(a)/f′(a)|p, rewrite this as |β|p = |f(a)/f′(a)2|p. If β = 0 then
α = a, so f(a) = 0 and thus |f(a)/f′(a)2|p = 0 = |β|p. If β ̸= 0 then from
0 = h(β) = b + β + g(a, f′(a)β)β2
we get |b + β|p = |g(a, f′(a)β)β2|p ≤|β|2
p < |β|p, so |β|p = |b|p = |f(a)/f′(a)2|p.
That |f′(α)|p = |f(a)|p follows from |α −a|p < |f′(a)|p: by (5.4), |f′(α) −f′(a)|p ≤
|α −a|p < |f′(a)|p, so |f′(α)|p = |f′(a)|p.
□
Example 5.5. Let f(X) = X3 −10 with approximate root a = 4 in Z3. We can’t apply
Theorem 2.1 directly to f(X) to show there is a solution to f(α) = 0 in Z3 with α close to
4 since f′(4) = 48 ≡0 mod 3. From the proof of Theorem 5.4 we compute
f(X +Y ) = (X +Y )3−10 = X3+3X2Y +3XY 2+Y 3−10 = f(X)+f′(X)Y +(3X +Y )Y 2.
Then
f(4+48X) = f(4)+f′(4)48X+(12+48X)(48X)2 = 54+482X+(12+48X)(48X)2 = 482h(X)
where
h(X) = 54
482 + X + (12 + 48X)X2 =
3
128 + X + 12X2 + 48X3.
Since h(0) ≡0 mod 3 and h′(0) = 1 ̸≡0 mod 3, h(X) has a unique root β ∈3Z3 and that
gives us a root α = 4 + 48β of f(X).
By Theorem 2.1, each solution of h(x) ≡0 mod 3n with x ≡0 mod 3 lifts uniquely to
a solution of h(x) ≡0 mod 3n+1 but such uniqueness of lifting at each “ﬁnite level” is not
true for solving f(x) ≡0 mod 3n; see Remark 4.8. This diﬀerent behavior is compatible
because of the 48 (a multiple of 3) appearing on both sides of f(4 + 48X) = 482h(X).
For example, suppose we want to solve f(t) ≡0 mod 81 in Z3 with t ≡4 mod 3. Then
we can write t = 4 + 48x with x ∈Z3 since 48 is divisible by 3 just once, so
f(4 + 48x) ≡0 mod 81 ⇐⇒482h(x) ≡0 mod 81 ⇐⇒h(x) ≡0 mod 9.
Note the modulus decreased from 81 to 9. The unique solution of h(x) ≡0 mod 9 is 3 mod 9,
and that is the same as t = 4 + 48x ≡4 + 48 · 3 ≡13 mod 27. The modulus increased from
9 to 27 since congruences mod 9 are the same as congruences mod 27 when multiplying by
48. We have shown f(t) ≡0 mod 81 is the same as t ≡13 mod 27, and there are three
liftings of 13 from mod 27 to mod 81: 13, 40, and 67.
6. Second Proof of Theorem 4.1: Contraction Mappings
Newton’s method produces a sequence converging to a root of f(X) by iterating the
function x −f(x)/f′(x) with initial value a1 = a where |f(a)|p < |f′(a)|2
p. A root can also
be found with a diﬀerent iteration ϕ(x) = x −f(x)/f′(a), where again |f(a)|p < |f′(a)|2
p.
The denominator is f′(a), not f′(x), so it doesn’t change. We will show ϕ is a contraction
mapping on a suitable ball around a. Then the contraction mapping theorem will imply ϕ
has a (unique) ﬁxed point α in that ball.4 The condition ϕ(α) = α says α−f(α)/f′(a) = α,
so f(α) = 0 and we have a root of f(X). Filling in the details leads to the following second
proof of Theorem 4.1. If you’re not interested in a second proof, go to the next section.
Proof. For r ∈[0, 1] to be determined, set Ba(r) = {x ∈Qp : |x −a|p ≤r}, so Ba(r) ⊂Zp.
Set
ϕ(x) = x −f(x)
f′(a).
4There is an analogous method in real analysis to simplify Newton’s method to the contraction mapping
theorem by ﬁxing the denominator in the recursion. See [2, Thm. 1.2, p. 164].

<!-- page 13 -->
HENSEL’S LEMMA
13
We seek an r such that ϕ maps Ba(r) back to itself and is a contraction on that ball.
To show ϕ is a contraction on some ball around a, we want to estimate
|ϕ(x) −ϕ(y)|p =
x −y −f(x) −f(y)
f′(a)

for all x and y near a in order to make this ≤λ|x −y|p for some λ < 1.
Write f(X) as a polynomial in X −a, say f(X) = Pd
i=0 bi(X −a)i. Then b0 = f(a),
b1 = f′(a), and bi ∈Zp for i > 1. For all x and y in Qp,
f(x) −f(y) =
d
X
i=1
bi((x −a)i −(y −a)i) = f′(a)(x −y) +
d
X
i=2
bi((x −a)i −(y −a)i),
so
(6.1)
ϕ(x) −ϕ(y) = x −y −f(x) −f(y)
f′(a)
= −
1
f′(a)
d
X
i=2
bi((x −a)i −(y −a)i).
(If d ≤1 then the sum on the right is empty.) In the polynomial identity
Xi −Y i = (X −Y )
i−1
X
j=0
Xi−1−jY j
for i ≥2 set X = x −a and Y = y −a. Then
|(x −a)i −(y −a)i|p = |x −y|p

i−1
X
j=0
(x −a)i−1−j(y −a)j

p
≤|x −y|p
max
0≤j≤i−1 |x −a|i−1−j
p
|y −a|j
p
≤|x −y|p max(|x −a|p, |y −a|p)i−1
≤|x −y|p max(|x −a|p, |y −a|p)
when |x −a|p and |y −a|p are both at most 1. Therefore from (6.1),
|x −a|p, |y −a|p ≤1 =⇒|ϕ(x) −ϕ(y)|p ≤|x −y|p max(|x −a|p, |y −a|p)
|f′(a)|p
,
so for λ ∈[0, 1),
(6.2)
|x −a|p, |y −a|p ≤λ|f′(a)|p =⇒|ϕ(x) −ϕ(y)|p ≤λ|x −y|p.
If we can ﬁnd λ ∈[0, 1), perhaps depending on a and f(X), such that
(6.3)
|x −a|p ≤λ|f′(a)|p =⇒|ϕ(x) −a|p ≤λ|f′(a)|p
then (6.2) will tell us that ϕ is a contraction mapping on the closed ball around a of radius
λ|f′(a)|p. We will see that if |f(a)|p < |f′(a)|2
p then a choice for λ is |f(a)/f′(a)2|p. In
fact, we want to do more: show the condition |f(a)|p < |f′(a)|2
p arises naturally by trying
to make (6.3) work for some unknown λ.
For λ ∈(0, 1), when |x −a|p ≤λ|f′(a)|p we have
|ϕ(x) −a|p ≤λ|f′(a)|p ⇐⇒
x −a −f(x)
f′(a)

p
≤λ|f′(a)|p ⇐⇒

f(x)
f′(a)

p
≤λ|f′(a)|p.

<!-- page 14 -->
14
KEITH CONRAD
Returning to the formula f(X) = Pd
i=0 bi(X −a)i, where b0 = f(a) and b1 = f′(a),
(6.4)
f(x)
f′(a) = f(a)
f′(a) + (x −a) +
d
X
i=2
bi
f′(a)(x −a)i.
When |x −a|p ≤λ|f′(a)|p, which is less than |f′(a)|p ≤1, we have for i ≥2 that

bi
f′(a)(x −a)i

p
≤|x −a|2
p
|f′(a)|p
≤λ2|f′(a)|p ≤λ|f′(a)|p,
so by (6.4)

f(x)
f′(a)

p
≤λ|f′(a)|p ⇐⇒

f(a)
f′(a)

p
≤λ|f′(a)|p ⇐⇒

f(a)
f′(a)2

p
≤λ.
To make this occur for some λ < 1 is equivalent to requiring |f(a)/f′(a)2|p < 1. Therefore
if |f(a)|p < |f′(a)|2
p and we set λ = |f(a)/f′(a)2|p, the mapping ϕ(x) = x −f(x)/f′(a) is a
contraction on the closed ball around a with radius λ|f′(a)|p = |f(a)/f′(a)|p and contraction
constant λ. Any closed ball in Qp is complete, so the contraction mapping theorem implies
that the sequence {an} deﬁned recursively by a1 = a and
(6.5)
an+1 = ϕ(an) = an −f(an)
f′(a)
for n ≥1 converges to the unique ﬁxed point of ϕ in Ba(|f(a)/f′(a)|p). By the deﬁnition
of ϕ, a ﬁxed point of ϕ is the same thing as a zero of f(X), so there is a unique α in Qp
satisfying f(α) = 0 and |α −a|p ≤|f(a)/f′(a)|p.
To ﬁnish this proof of Theorem 4.1 we need to show |α −a|p = |f(a)/f′(a)|p, α is the
unique root of f(X) in Zp such that |α −a|p < |f′(a)|p, and |f′(α)|p = |f′(a)|p.
|α −a|p = |f(a)/f′(a)|p: We have |a2 −a|p = |a2 −a1|p = |f(a1)/f′(a)|p = |f(a)/f′(a)|p,
and for all n
|an+1 −an|p = |ϕn(a) −ϕn−1(a)|p = |ϕn−1(ϕ(a)) −ϕn−1(a)|p ≤λn−1|a2 −a1|p <

f(a)
f′(a)

p
.
Then |an −a|p = |f(a)/f′(a)|p for all n by induction, so |α −a|p = |f(a)/f′(a)|p by letting
n →∞.
α is the unique root of f(X) such that |α −a|p < |f′(a)|p: This was proved at the end
of the ﬁrst proof of Theorem 4.1 without needing Newton’s method. We won’t rewrite the
proof.
|f′(α)|p = |f′(a)|p: Since a1 = a, of course |f′(a1)|p = |f′(a)|p. If |f′(an)|p = |f′(a)|p for
some n ≥1 then
|f′(an+1) −f′(an)|p ≤|an+1 −an|p ≤

f(a)
f′(a)

p
where the ﬁrst inequality is from (5.4) and the second inequality is from an and an+1
both lying in the closed ball around a of radius |f(a)/f′(a)|p. Thus |f′(an+1) −f′(an)|p <
|f′(a)|p = |f′(an)|p, so |f′(an+1)|p = |f′(an)|p = |f′(a)|p. We’ve shown |f′(an)|p = |f′(a)|p
for all n, and letting n →∞gives us |f′(α)|p = |f′(a)|p.
□
It’s worthwhile to compare the recursions from Newton’s method and from the contraction
mapping theorem:
• Newton’s method: an+1 = an −f(an)
f′(an), with a1 = a and |f(a)|p < |f′(a)|2
p.
• Contraction mapping: an+1 = an −f(an)
f′(a) , with a1 = a and |f(a)|p < |f′(a)|2
p.

<!-- page 15 -->
HENSEL’S LEMMA
15
The diﬀerence is the denominators f′(an) and f′(a), and this has a profound eﬀect on the
rate of convergence. In Newton’s method, (5.7) tells us
(6.6)
|α −an|p ≤|f′(a)|p

f(a)
f′(a)2

2n−1
p
.
To ﬁnd an estimate on |α−an|p from the contraction mapping theorem, the recursion given
by (6.5) implies |an+1 −an|p = |ϕn−1(a2) −ϕn−1(a1)|p ≤|a2 −a1|pλn−1 for all n ≥1, where
a2 −a1 = f(a)/f′(a) and λ = |f(a)/f′(a)2|p. If m > n the strong triangle inequality implies
|am −an|p ≤
max
n≤j≤m−1 |aj+1 −aj|p ≤|a2 −a1|pλn−1 =

f(a)
f′(a)

p
λn−1.
Letting m →∞yields
(6.7)
|α −an|p ≤

f(a)
f′(a)

p

f(a)
f′(a)2

n−1
.
The upper bound in (6.6) goes to 0 much faster than the upper bound in (6.7), so we
anticipate that |α −an|p →0 faster when {an} is comes from Newton’s recursion compared
to the contraction mapping recursion. For instance, if |f(a)/f′(a)2|p = 1/p, then the bound
in (6.6) goes to 0 like (1/p)2n−1 while in (6.7) the bound goes to 0 like (1/p)n, so there is at
least a doubling of correct p-adic digits in each step of Newton’s recursion while we expect
at most one new correct p-adic digit at each step by the contraction mapping recursion.
Example 6.1. Let f(X) = X2 −7 with a = 1, so |f(a)/f′(a)|3 = 1/3. The sequence {an}
produced from the contraction mapping recursion (6.5) with a1 = 1 has a limit α and with a
computer we ﬁnd |α −an|3 = (1/3)n for 1 ≤n ≤10. The sequence {an} based on Newton’s
recursion in Example 5.1 with a1 = 1 has the same limit α, but a computer tells us that
|α −an|3 = (1/3)2n−1 for 1 ≤n ≤10, which is much smaller than (1/3)n.
7. The inevitability of |f(a)|p < |f′(a)|2
p
In Theorem 4.1 we have |f′(α)|p = |f′(a)|p ̸= 0, so Hensel’s lemma produces a simple
root α of f(X) in Zp that is close to a. The criterion |f(a)|p < |f′(a)|2
p in Theorem 4.1 is
not just a suﬃcient condition for there to be a simple root of f(X) near a but it is also
necessary, as the next theorem makes precise.
Theorem 7.1. If f(X) ∈Zp[X] has a simple root α in Zp, then for all a ∈Zp that are
close enough to α we have |f′(a)|p = |f′(α)|p and |f(a)|p < |f′(a)|2
p. In particular, these
conditions hold when |a −α|p < |f′(α)|p.
Proof. By (5.4) with F(X) = f′(X), |f′(α) −f′(a)|p ≤|α −a|p < |f′(α)|p. Thus |f′(a)|p =
|f′(α)|p. By (5.3) with F(X) = f(X),
f(a) = f(α + (a −α)) = f(α) + f′(α)(a −α) + z(a −α)2 = f′(α)(a −α) + z(a −α)2
for some z ∈Zp. Both terms on the right side have absolute value less than |f′(α)|2
p since
|a −α|p < |f′(α)|p, so |f(a)|p < |f′(α)|2
p = |f′(a)|2
p.
□
8. Hensel’s lemma for power series
Hensel’s lemma can be applied to p-adic power series, not just polynomials. By “p-adic
power series” we have in mind those with Zp-coeﬃcients, which we will call power series
“over Zp”. We will consider such series of two types: those that converge on Zp and those
that converge on pZp but not necessarily on Zp (e.g., eX for p > 2). To prove Hensel’s

<!-- page 16 -->
16
KEITH CONRAD
lemma for these two types of power series, we will use the following power series analogue
of (5.3) and (5.4).
Lemma 8.1. Let F(X) be a power series with coeﬃcients in Zp that converges on Zp.
(1) For x and y in Zp, F(x + y) = F(x) + F ′(x)y + zy2 for some z ∈Zp.
(2) For x and y in Zp, |F(x) −F(y)|p ≤|x −y|p.
If F(X) converges on pZp but not necessarily on Zp, then (1) and (2) are true for x, y ∈pZp.
Proof. Let F(X) = P
i≥0 ciXi, so ci ∈Zp. Convergence of F(X) on Zp implies ci →0 as
i →∞. To prove (1), the analogue of (5.3), for x and y in Zp we have
F(x + y) =
X
i≥0
ci(x + y)i
= c0 +
X
i≥1
ci(xi + ixi−1y + gi(x, y)y2) where gi(x, y) ∈Zp[x, y] ⊂Zp
=
X
i≥0
cixi +
X
i≥1
icixi−1y +
X
i≥2
cigi(x, y)y2,
where we can break apart the series since |ci|p →0 as i →∞and the numbers x, y, and
gi(x, y) are all in Zp (all the series converge) with g1(x, y) = 0. Thus
F(x + y) = F(x) + F ′(x)y + zy2
where z = P
i≥2 cigi(x, y) ∈Zp.
To prove (2), the analogue of (5.4), we use |xi −yi|p ≤|x−y|p for all x, y ∈Zp and i ≥0:
F(x) −F(y) =
X
i≥1
ci(xi −yi) =⇒|F(x) −F(y)|p ≤max
i≥1 |ci|p|xi −yi|p ≤max
i≥1 |ci|p|x −y|p,
which is at most |x −y|p since all |ci|p are at most 1.
If F(X) converges on pZp but not necessarily on Zp, so the coeﬃcients ci are in Zp but
need not tend to 0, the proofs of (1) and (2) remain valid for x, y ∈pZp after checking
some details: in the proof of (1), the series for F(x) and F ′(x) converge when x ∈Zp, while
the series P
i≥1 cigi(x, y) converges since |gi(x, y)|p ≤max(|x|p, |y|p)i−2 by the binomial
theorem that gave rise to gi(x, y). The proof of (2) carries over with no changes at all
provided x, y ∈pZp so that F(x) and F(y) converge.
□
Here is a power series version of Theorem 4.1 for series over Zp that converge on Zp.
Theorem 8.2. Let f(X) be a power series with coeﬃcients in Zp that converges on Zp. If
an a ∈Zp satisﬁes
|f(a)|p < |f′(a)|2
p
then there is a unique α ∈Zp such that f(α) = 0 in Zp and |α −a|p < |f′(a)|p. Moreover,
(1) |α −a|p = |f(a)/f′(a)|p < |f′(a)|p,
(2) |f′(α)|p = |f′(a)|p.
In this theorem, f′(a) makes sense for a ∈Zp since f′(X) converges on Zp: the coeﬃcients
of f(X) tend to 0 since f(1) converges so the coeﬃcients of f′(X) also tend to 0 and thus
f′(X) converges on Zp.
Proof. Using Lemma 8.1 in place of (5.3) and (5.4), the proof of Theorem 4.1 using Newton’s
method carries over word for word to the setting of power series with Zp-coeﬃcients that
converge on Zp.
□

<!-- page 17 -->
HENSEL’S LEMMA
17
Remark 8.3. Theorem 8.2 can also be proved by turning the power series f(X) into a
polynomial, thereby reducing to the polynomial case. The p-adic Weierstrass preparation
theorem says f(X) = W(X)U(X) where W(X) is a polynomial in Zp[X] and U(X) is a unit
power series with coeﬃcients in Zp that converges on Zp (this means U(X)V (X) = 1 for
some power series V (X) with Zp-coeﬃcients that converges on Zp). From f(a) = W(a)U(a)
and U(a)V (a) = 1 for all a ∈Zp, roots of f(X) in Zp are the same as roots of W(X) in Zp.
If |f(a)|p < |f′(a)|2
p then |f(a)|p = |W(a)|p since |U(a)|p = 1, and also |f′(a)|p = |W ′(a)|p
since from f′(a) = W ′(a)U(a)+W(a)U′(a) and |W(a)U′(a)|p ≤|W(a)|p = |f(a)|p < |f′(a)|p
we must have |f′(a)|p = |W ′(a)U(a)|p = |W ′(a)|p. Thus |W(a)|p < |W ′(a)|2
p, so there is a
unique α ∈Zp ﬁtting the conclusion of Theorem 4.1 for W(X). It’s left to the reader to
check α also ﬁts the uniqueness conditions in Theorem 8.2 for f(X).
The basic version of Hensel’s lemma is true for power series as a special case of the strong
version proved above: if f(X) is a power series over Zp that converges on Zp and an a ∈Zp
satisﬁes f(a) ≡0 mod p and f′(a) ̸≡0 mod p then there is a unique α ∈Zp such that
f(α) = 0 and α ≡a mod p.
Like Theorem 5.4, the basic and strong form of Hensel’s lemma for power series with
Zp-coeﬃcients that converge on Zp are equivalent, with a proof similar to the polynomial
case, but care is needed since part of the proof uses convergent power series in two variables.
Details are left to the reader. Check also that Theorem 7.1 and its proof carry over to power
series over Zp that converge on Zp, where a simple root of a power series is a root at which
the derivative is nonzero.
For power series over Zp that converge on pZp but not necessarily on Zp, here is a version
of Hensel’s Lemma.
Theorem 8.4. Let f(X) be a power series with coeﬃcients in Zp that converges on pZp.
If an a ∈pZp satisﬁes
|f(a)|p < |f′(a)|2
p
then there is a unique α ∈pZp such that f(α) = 0 in Zp and |α −a|p < |f′(a)|p. Moreover,
(1) |α −a|p = |f(a)/f′(a)|p < |f′(a)|p,
(2) |f′(α)|p = |f′(a)|p.
Proof. The proof of Theorem 8.2 (including its use of Lemma 8.1) carries over with the
complete space pZp replacing the complete space Zp as the set containing the approximate
roots an and the root α that is their limit.
□
Remark 8.5. The reduction of Theorem 8.2 to the case of polynomials in Remark 8.3
applies to Theorem 8.4 too by using a p-adic Weierstrass preparation theorem for power
series with Zp-coeﬃcients that converge on pZp (but perhaps not on Zp).
In the proof of Hensel’s lemma for polynomials by Newton’s method, the bounds on
|f(an)|p and |an+1 −an|p carry over to Hensel’s lemma for power series, whether in the
form of Theorem 8.2 or 8.4: |f(an)|p ≤|f′(a)|p(|f(a)|p/|f′(a)2|p)2n−1 and |an+1 −an|p ≤
|f′(a)|p|f(a)/f′(a)2|2n−1
p
. Using the strong triangle inequality in the second bound for am −
an = (am −am−1) + · · · + (an+1 −an) when m > n and then letting m →∞, we get the
bound from (5.7) all over again, but this time for power series:
(8.1)
|α −an|p ≤|f′(a)|p

f(a)
f′(a)2

2n−1
p
.
Example 8.6. For c ∈Zp, set (1 + X)c = P
n≥0
 c
n

xn, where
 c
n

= c(c−1)···(c−n−1)
n!
. Since
c is a p-adic limit of positive integers (use truncations of the p-adic expansion of c), the

<!-- page 18 -->
18
KEITH CONRAD
number
 c
n

is a p-adic limit of integers and thus
 c
n

∈Zp. For c ∈Zp −{0, 1, 2, 3, . . .},
 c
n

∈Z×
p inﬁnitely often (for those n whose base p expansion is an initial part of the p-adic
expansion of c), so (1 + X)c has coeﬃcients in Zp that do not tend to 0 and thus (1 + X)c
converges on pZp but not on Zp.
Consider f(X) = (1 + X)
√
7 −10, where
√
7 = 1 + 3 + 32 + 2 · 34 + · · · in Z3. For each
a ∈3Z3, f(a) ≡0 mod 3 and f′(a) =
√
7(1 + a)
√
7−1 ≡
√
7 ̸≡0 mod 3, so by Theorem
8.4 there is a unique solution to f(α) = 0 in 3Z3 by using Newton’s method with initial
value a1 = a. Taking a = 0, f(a1) = −9 and f′(a1) =
√
7 ̸≡0 mod 3. Using (8.1) for
f(X) = (1 + X)
√
7 −10, |α −an|3 ≤(1/9)2n−1 = (1/3)2n. Taking n = 3,
(8.2)
α ≡a3 ≡32 + 2 · 33 + 2 · 34 + 35 + 2 · 36 mod 38.
The number on the right is 1926. As a reality check5, let’s conﬁrm that f(a3) is 3-adically
small. Since |f(x) −f(y)|3 ≤|x −y|3 for x, y ∈Z3, f(a3) ≡f(1926) mod 38. Since 1926
is divisible by 9, so 1926n ≡0 mod 38 for n ≥4, and the power series coeﬃcients of f(X)
are all in Z3, f(1926) ≡−9 + P3
n=1
 √
7
n

1926n mod 38. With a computer, the right side is
0 mod 38.
Example 8.7. For p > 2 and c ∈1+pZp, set f(X) = eX −c. The p-adic disc of convergence
for eX (and thus for eX −c) on Qp is pZp. Since f(0) = 1 −c and f′(0) = 1, we have
|f(0)|p ≤1/p and |f′(0)||p = 1. Therefore Theorem 8.4 tells us there is a unique α ∈pZp
such that eα = c and |α|p < 1, and in fact |α|p = |f(0)|p = |c −1|p. This α in pZp for which
eα = c is the p-adic logarithm of c.
By (8.1) with a = 0, |α −an|p ≤|1 −c|2n−1
p
. For instance, if we want to solve eα = −2
for α ∈3Z3 and compute α mod 35, use Newton’s method with f(x) = ex + 2.
Then
|α −an|3 ≤|1 −(−2)|2n−1
3
= 1/32n−1. The upper bound is at most 1/35 for n ≥4, so take
n = 4. The Newton’s method recursion is an+1 = an −f(an)/f′(an) = an −(ean + 2)/ean =
an −1 −2/ean. By computer, the term for a4 in the table below satisﬁes ea4 ≡−2 mod 315.
n
an
1
0
2
−3
3
2 · 3 + 2 · 32 + 35 + 2 · 37 + 2 · 310 + · · ·
4
2 · 3 + 2 · 32 + 35 + 36 + 2 · 38 + 39 + · · ·
9. Hensel’s lemma beyond Qp
The proofs of Hensel’s lemma work for polynomials with coeﬃcients in a ﬁeld K com-
plete with respect to an absolute value satisfying the strong triangle inequality: |x + y| ≤
max(|x|, |y|) for all x and y in K. Set o = {x ∈K : |x| ≤1}.
Theorem 9.1. For o as above and a polynomial f(X) with coeﬃcients in o, assume some
a ∈o satisﬁes
|f(a)| < |f′(a)|2.
Then there is a unique α ∈o such that f(α) = 0 in o and |α −a| < |f′(a)|. Moreover,
(1) |α −a| = |f(a)/f′(a)| < |f′(a)|,
(2) |f′(α)| = |f′(a)| ̸= 0.
Conversely, if f(X) has a simple root α ∈o, then for a ∈K such that |a −α| < |f′(α)|
then we have |f′(a)| = |f′(α)| and |f(a)| < |f′(a)|2.
5Should this be called a 3-adicity check, since we’re not working over the reals?

<!-- page 19 -->
HENSEL’S LEMMA
19
Theorems 5.4 and 7.1 also carry over to o[X], with the same proofs (the proofs over Zp
were written speciﬁcally to make sure the proofs carry over to o with no changes):
Theorem 9.2. The following properties o[X] are equivalent.
(1) When f(X) ∈o[X] and there is an a ∈o such that |f(a)| < 1 and |f′(a)| = 1, there
is a unique α ∈o such that f(α) = 0 in o and |α −a| < 1,
(2) When f(X) ∈o[X] and there is an a ∈o such that |f(a)| < |f′(a)|2, there is a
unique α ∈o such that f(α) = 0 in o and |α −a| < |f′(a)|, and in fact |α −a|p =
|f(a)/f′(a)|p
Theorem 9.3. If f(X) ∈o[X] has a simple root α in o, then for all a ∈o that are close
enough to α we have |f′(a)| = |f′(α)| and |f(a)| < |f′(a)|2. In particular, these conditions
hold when |a −α| < |f′(α)|.
For power series, everything written about power series with coeﬃcients in Zp in Section
8 carries over to power series with coeﬃcients in o: all such power series converge on the
maximal ideal m = {x ∈o : |x| < 1}, and those with coeﬃcients tending to 0 converge on o.
We record below the statements of Hensel’s lemma for both types of power series, leaving
the proofs (similar to the polynomial case in most respects) to the reader.
Theorem 9.4. Let f(X) be a power series with coeﬃcients in o that converges on o. If an
a ∈o satisﬁes
|f(a)| < |f′(a)|2
then there is a unique α ∈o such that f(α) = 0 in o and |α −a| < |f′(a)|. Moreover,
(1) |α −a| = |f(a)/f′(a)| < |f′(a)|,
(2) |f′(α)| = |f′(a)|.
Theorem 9.5. Let f(X) be a power series with coeﬃcients in o, so it converges on m.
If an a ∈m satisﬁes
|f(a)| < |f′(a)|2
then there is a unique α ∈m such that f(α) = 0 in o and |α −a| < |f′(a)|. Moreover,
(1) |α −a| = |f(a)/f′(a)| < |f′(a)|,
(2) |f′(α)| = |f′(a)|.
10. Hensel’s lemma with submultiplicative absolute values
We will formulate a version of Hensel’s lemma where Zp is replaced by a ring A that is
complete with respect to an absolute value similar to | · |p where multiplicativity is replaced
by submultiplicativity.
Deﬁnition 10.1. A submultiplicative absolute value | · | on a nonzero commutative ring A
is a function | · |: A →R such that for all a and b in A,
(i) 0 ≤|a| ≤1 with |a| = 0 if and only if a = 0,
(ii) |a + b| ≤max(|a|, |b|) (strong triangle inequality),
(iii) |ab| ≤|a||b| (submultiplicative).
For an ordinary absolute value, |1| = 1 by multiplicativity since |1| = |12| = |1|2. When
we have submultiplicativity, we can still get |1| = 1 when |a| ≤1 for all a: |1| = |12| ≤|1|2
and |1| > 0, so 1 ≤|1|. Since the reverse inequality |1| ≤1 holds by deﬁnition, we get
|1| = 1. Therefore |−a| = |a|: |−a| ≤|−1||a| ≤|a| and |a| = |−(−a)| ≤|−1||−a| ≤|−a|.
On A we have a metric ρ(a, b) = |a−b|; (that ρ(a, b) = ρ(b, a) follows from |a−b| = |b−a|
because |x| = |−x|). Many basic properties of |·|p on Zp remain true for a submultiplicative
absolute value, with the same or very similar proofs. For example, addition and multiplica-
tion on A are continuous and a sequence {an} in A is Cauchy if and only if |an+1 −an| →0.

<!-- page 20 -->
20
KEITH CONRAD
Before describing a form of Hensel’s lemma for polynomials and power series with coef-
ﬁcients in a ring complete for a submultiplicative absolute value, let’s describe a source of
examples of submultiplicative absolute values using powers of an ideal.
Let A be a nonzero commutative ring containing an ideal I such that T
n≥0 In = {0},
where In is the nth power of I as an ideal6. For a ̸= 0 in A, set |a|I = (1/2)n if a ∈In for
n as large as possible (there is a maximal n such that a ∈In because T
n≥0 In = {0}), and
set |0|I = 0. Then 0 ≤|a|I ≤1 and |a|I = 0 only when a = 0.7 We have |a|Iρ = (1/2)n ⇒
a ∈In and a ∈In ⇒|a|I ≤(1/2)n (the exponent n in the second implication might not
be maximal for the choice of a). That |a + b|I ≤max(|a|I, |b|I) is left to the reader. The
function ρI(a, b) = |a −b|I is called the I-adic metric on A. To prove submultiplicativity of
| · |I on A, if a and b are nonzero in A with |a|I = (1/2)n and |b|I = (1/2)m then ab ∈In+m,
so |ab|I ≤(1/2)n+m = |a|I|b|I. Obviously |ab|I ≤|a|I|b|I if a or b is 0.
We have A = I0 ⊃I ⊃I2 ⊃I3 ⊃· · · and elements of In are considered I-adically small
if n is large. A sequence {aj} in A is I-adically Cauchy if for each n ≥1 there is j ≥1
such that aj′ −aj′′ ∈In for all j′, j′′ ≥j. This is equivalent to aj+1 −aj ∈In for all large j
(depending on n) and is the same as {aj} being a Cauchy sequence for the metric ρI. We
say A is I-adically complete if each I-adic Cauchy sequence in A converges in A.
An example of such a ring A and ideal I is R[T] and I = (T) = TR[T] where R is
a commutative ring. Then In = (T n), which is the set of polynomials with no terms in
degree less than n, so T
n≥1 In = {0}. The I-adic absolute value on R[T] is called the
T-adic absolute value and is denoted | · |T . We have |f(T)|T = (1/2)n if and only if the
lowest-degree nonzero term in f(T) has degree n. The ring R[T] is not T-adically complete
since, for instance, the partial sums sn = 1 + T + T 2 + · · · + T n form a T-adic Cauchy
sequence that has no limit in R[T]: (1 −T)sn = 1 −T n+1, which tends to 1, so if {sn} has
a limit s in R[T] then (1 −T)s = 1, but 1 −T has no multiplicative inverse in R[T].
Another example is the ring R[[T]] of formal power series P
n≥0 cnT n with cn ∈R and
the ideal I = (T) = TR[[T]] consisting of multiples of T in R[[T]] (the power series with
constant term 0). The T-adic absolute value | · |T on R[[T]] is deﬁned in the same way as
on R[T], and R[T] is dense in R[[T]]: the sum of all terms in a power series with degree
less than n is in R[T] and diﬀers from the power series by a series in In, and we can take n
arbitrarily large. The ring R[[T]] is T-adically complete: a T-adic Cauchy sequence has the
coeﬃcients in each degree eventually constant, leading to a candidate limit series in R[[T]]
that really is the limit of the sequence. So R[[T]] is the T-adic completion of R[T]. For
example, the sequence sn = 1 + T + T 2 + · · · + T n in R[[T]] converges to P
n≥0 T n, which
is a multiplicative inverse of 1 −T.
More generally, consider the ring R[T1, . . . , Td] and I = (T1, . . . , Td), so In is the polyno-
mials in R[T1, . . . , Td] having no nonzero terms in degree below n. Then |f(T1, . . . , Td)|I =
(1/2)n means the lowest-degree nonzero monomial in f(T1, . . . , Td) has degree n. This ring
is not I-adically complete, but the ring R[[T1, . . . , Td]] of formal power series in d indeter-
minates is complete with respect to its ideal I = (T1, . . . , Td) of formal power series with
constant term 0 and R[T1, . . . , Td] is dense in R[[T1, . . . , Td]].
Remark 10.2. On Z[T] we can consider the I-adic absolute value when I is (p), (T), and
(p, T). What’s the diﬀerence?
(1) Being p-adically small means all the coeﬃcients are highly divisible by p.
(2) Being T-adically small means the polynomial has no low-degree terms.
(3) Being (p, T)-adically small means low-degree coeﬃcients are highly divisible by p.
6In is the ideal generated by n-fold products a1 · · · an for ai ∈I. It’s more than all an for a ∈I.
7The role of 1/2 in the deﬁnition of |a|I when a ̸= 0 could be replaced by an arbitrary number strictly
between 0 and 1. The main point is that |a|I is very small when a ∈In for large n.

<!-- page 21 -->
HENSEL’S LEMMA
21
The p-adic completion of Z[T] is the set of power series P
n≥0 cnT n where cn ∈Zp and
cn →0, the T-adic completion of Z[T] is Z[[T]], and the (p, T)-adic completion of Z[T] is
Zp[[T]]. The ring Zp[[T]] is both T-adically and (p, T)-adically complete, but these notions
of convergence are diﬀerent. A sequence in Zp[[T]] that converges T-adically also converges
(p, T)-adically since (T)n ⊂(p, T)n as ideals in Zp[[T]], but the converse is false: a sequence
in Zp that converges p-adically does not converge T-adically when viewed as constants in
Zp[[T]]. And Z[T] is (p, T)-adically dense in Zp[[T]] but is not T-adically dense in Zp[[T]]:
for c ∈Zp −Z, no f(T) ∈Z[T] satisﬁes |c −f(T)|T < 1 since such an inequality forces
f(0) = c but f(0) ∈Z and c ̸∈Z.
Lemma 10.3. Let A be a nonzero commutative ring that is complete with respect to a
submultiplicative absolute value | · |.
(1) |ua| = |a| for all u ∈A× and a ∈A.
(2) If y ∈A satisﬁes |y| < 1 then 1 + y ∈A×.
(3) The units of A are closed in A×: if {un} is a sequence in A× with a limit in A, then
the limit is in A×.
Proof. (1) For u ∈A× and a ∈A, |ua| ≤|u||a| ≤|a|. For the reverse inequality, let uv = 1
in A, so |a| = |ua(v)| ≤|ua||v| ≤|ua|.
(2) We use a geometric series: the partial sums sn = 1 −y + y2 −y3 + · · · + (−y)n are a
Cauchy sequence in A by the strong triangle inequality since |(−y)n| ≤|y|n →0 as n →∞.
Let s = limn→∞sn in A, so (1 + y)s = limn→∞(1 + y)sn = limn→∞1 −(−y)n = 1. Thus
1 + y ∈A×.
(3) Let un →L in A.
Set vn = 1/un, so vn+1 −vn = vnvn+1(un −un+1).
Thus
|vn+1 −vn| ≤|un −un+1| →0 as n →∞. Therefore {vn} is Cauchy in A. Let M be its
limit, so unvn →LM by continuity of multiplication. Also unvn = 1 for all n, so LM = 1.
Thus L ∈A×.
□
Example 10.4. A power series f(T) ∈R[[T]] is a unit if and only if its constant term
f(0) is a unit in R. Indeed, if f(T)g(T) = 1 then the constant terms have product 1,
so f(0) ∈R×. Conversely, if f(0) ∈R× then we can prove f(T) ∈R[[T]]× by writing
f(T) = f(0) + TF(T) = f(0)(1 + (1/f(0))TF(T). The ﬁrst factor f(0) is a unit in R[[T]]
since it is a unit in R and the second factor 1+(1/f(0))TF(T) is a unit in R[[T]] by Lemma
10.3(2).
In contrast to Zp, where the condition a ∈Z×
p means the same thing as |a|p = 1, there is
a diﬀerence in R[[T]] between |f(T)|T = 1 and f(T) ∈R[[T]]× unless R is a ﬁeld: a power
series f(T) ∈R[[T]] has |f(T)|T = 1 when its constant term is in R −{0}, while f(T) is
a unit in R[[T]] only when its constant term is in R×, and that is more restrictive than
|f(T)|T = 1 unless R× = R −{0} (i.e., unless R is a ﬁeld). For instance, in Z[[T]] we have
|2 + T|T = 1 and 2 + T is not a unit in Z[[T]]. More generally, if A is a ring and I is an
ideal of A such that T
n≥0 In = {0}, if a ∈A× then |a|I = (1/2)0 = 1 because no unit is
contained in I (otherwise the powers of I could not have intersection {0}), but the converse
might not be true.
Now we can present a basic form of Hensel’s lemma in A[X].
Theorem 10.5. Let f(X) ∈A[X], where A is a nonzero commutative ring complete with
respect to a submultiplicative absolute value | · |.
If an a ∈A satisﬁes |f(a)| < 1 and f′(a) ∈A× then then there is a unique α ∈A such
that f(α) = 0 in A and |α −a| < 1. Moreover,
(1) |α −a| = |f(a)| < 1,
(2) f′(α) ∈A×.

<!-- page 22 -->
22
KEITH CONRAD
Note the condition on f′(a) is f′(a) ∈A×, not |f′(a)| = 1; being a unit in A is potentially
more precise than having absolute value 1.
Proof. The proof is like that of Theorem 4.1: set a1 = a and an+1 = an −f′(an)/f′(an) and
check by induction that f′(an) ∈A× and |f(an)| ≤|f(a)|2n−1 for all n ≥1. You need to be
careful not to use multiplicativity on | · | on all products, but it can be used if one factor in
a product is a unit in A, by Lemma 10.3(1).
The sequence {an} is Cauchy in A since |an+1 −an| →0, and letting α = limn→∞an, we
have f(α) = 0 since |f(an)| →0 and polynomials in A[X] are continuous on A. We have
f′(α) ∈A× by Lemma 10.3(3) since f′(an) ∈A× for all n and f′(X) is a polynomial.
The proof that |α −a| = |f(a)| is very similar to the case A = Zp. To prove α is the
unique root of f(X) such that |α −a| < 1, we need to be a little more careful than in the
case A = Zp since | · | is submultiplicative rather than multiplicative. If β ∈A satisﬁes
f(β) = 0 and |β −a| < 1 then |β −α| < 1, so β = α + h where |h| < 1. Then
0 = f(β) = f(α + h) = f(α) + f′(α)h + zh2 = f′(α)h + zh2
for some z ∈A. Then f′(α)h = −zh2. Taking absolute values of both sides and using
Lemma 10.3(1), |h| = |−zh2| ≤|h|2. Since |h| < 1, having |h| ≤|h|2 forces |h| = 0, so h = 0
and thus β = α.
□
Example 10.6. Let A = Q[[T]] and f(X) = Xn −(1 + T) ∈Q[[T]][X] = A[X] where
n ≥1. Since |f(1)|T = |−T|T < 1 and f′(1) = n ∈A×, there is a unique g(T) ∈Q[[T]] such
that g(T)n = 1 + T and |g(T) −1|T < 1, meaning g(T) ∈1 + TQ[[T]]. This g(T) begins as
1 + (1/n)T + · · · and is the power series (1 + T)1/n in Q[[T]] with constant term 1. Its full
formula is P
k≥0
 1/n
k

T k.
Note that if we use A = Z[[T]] and f(X) = Xn −(1 + T) ∈A[X] (same as before), then
|f(1)|T < 1 and f′(1) = n, so if n ≥2 then f′(1) ̸∈A× (a unit in Z[[T]] has constant term
±1 by Example 10.4) and there is no solution to g(T)n = 1+T in 1+TZ[[T]]: such a solution
would also be a solution in 1 + TQ[[T]] and we saw the unique solution in 1 + TQ[[T]] has
linear coeﬃcient 1/n, which is not an integer. This illustrates why in Theorem 10.5 we
can’t always replace “f′(a) ∈A×” with “|f′(a)| = 1”.
We don’t really need to replace Z[[T]] with Q[[T]] to ﬁnd a power series solution to
Xn = 1 + T: we just need n to be a unit in A, so we could use A = Z[1/n][[T]]. For
example,
√
1 + T ∈Z[1/2][[T]]. Indeed,
√
1 + T = 1 + 1
2T −1
23 T 2 + 1
24 T 3 −5
27 T 4 + 7
28 T 5 −21
210 T 6 + · · ·
and all coeﬃcients have 2-power denominator. Similarly,
6√
1 + T ∈Z[1/6][[T]]:
6√
1 + T = 1 + 1
6T −15
63 T 2 + 55
64 T 3 −8415
67 T 4 + 38709
68
T 5 −1122561
610
T 6 + · · · .
Here is an analogue of Theorem 10.5 for roots of power series in A[[X]]. Every such series
converges on {x ∈A : |x| < 1}, and this is where we’ll describe a criterion for the existence
of a root.
Theorem 10.7. Let f(X) ∈A[[X]], where A is a nonzero ring complete with respect to a
submultiplicative absolute value | · |.
If some a ∈A such that |a| < 1 satisﬁes |f(a)| < 1 and f′(a) ∈A× then then there is a
unique α ∈A such that f(α) = 0 in A and |α −a| < 1. Moreover,
(1) |α −a| = |f(a)| < 1,
(2) f′(α) ∈A×.

<!-- page 23 -->
HENSEL’S LEMMA
23
Proof. The proof proceeds in the same way as that of Theorem 10.5, relying on an extension
of Lemma 8.1 to power series with coeﬃcients in A rather than Zp.
□
Example 10.8. Let A = Q[[T]] and
f(X) = eX −(1 + T) = −T + X + 1
2X2 + · · · ∈A[[X]].
Since |f(0)|T = |−T|T < 1 and f′(0) = 1, there is a unique g(T) ∈TQ[[T]] such that
f(g(T)) = 0, meaning g(T) ∈TQ[[T]] and eg(T) = 1 + T. To ﬁnd the coeﬃcients of g(T),
diﬀerentiate both sides of the equation eg(T) = 1 + T: eg(T)g′(T) = 1, so
g′(T) =
1
eg(T) =
1
1 + T =
X
n≥0
(−1)nT n.
Therefore g(T) = P
n≥0((−1)n/(n + 1))T n+1 = P
n≥1((−1)n−1/n)T n, which is the formal
power series for log(1+T) in TQ[[T]]. The constant term of g(T) is 0 since g(T) ∈TQ[[T]].
Example 10.9. Let A = Q[[T]] and
f(X) = XeX −T = −T + X + X2 + 1
2X3 + · · · ∈A[[X]].
Since |f(0)|T = |−T|T < 1 and f′(0) = 1, there is a unique W(T) ∈TQ[[T]] such that
f(W(T)) = 0, meaning W(T)eW(T) = T. The series for W(T) is
T −T 2 + 3
2T 3 −8
3T 4 + 125
24 T 5 −54
5 T 6 + · · · =
X
n≥0
(−n)n−1
n!
T n.
Classically, W(T) as a function on C (initially near 0) is called Lambert’s W-function.
Example 10.10. (Formal compositional inverse) Let f(T) = c1T + · · · ∈TR[[T]] for a
commutative ring R. We’ll show there is a g(T) ∈TR[[T]] such that f(g(T)) = T if and
only if c1 ∈R×, in which case g(T) is unique and we also have g(f(T)) = T.
Suppose g(T) = b1T + · · · ∈TR[[T]] satisﬁes f(g(T)) = T. By a formal calculation,
f(g(T)) = c1b1T + higher order terms. That is, since g(T) ≡b1T mod T 2 we have g(T)n ≡
0 mod T 2 when n ≥2, so f(g(T)) ≡c1g(T) ≡c1b1T mod T 2. If f(g(T)) = T then T ≡
c1b1T mod T 2, so c1b1 = 1 in R. Thus c1 ∈R×.
Conversely, suppose c1 ∈R×. We will use Theorem 10.7 with A = R[[T]] and the power
series F(X) = f(X) −T ∈A[[X]]. Since |F(0)|T = |−T|T < 1 and F ′(0) = c1 ∈R× ⊂
R[[T]]×, by Theorem 10.7 there is a unique g(T) ∈TR[[T]] such that F(g(T)) = 0, which
means f(g(T)) = T.
Since g(T) is in TR[[T]], just like f(T), we can run through the same reasoning with
g(T) in place of f(T) by using G(X) = g(X) −T in place of F(X) = f(X) −T to see
there is a unique h(T) ∈TR[[T]] such that G(h(T)) = 0, meaning g(h(T)) = T. Then
f(T) = f(g(h(T))) = h(T) since f(g(T)) = T. That proves g(f(T)) = T. For instance, in
Example 10.8, rewriting elog(1+T) = 1 + T as F(log(1 + T)) = T where F(T) = eT −1, we
get log(1 + F(T)) = T, or equivalently log(eT ) = T.
The classical implicit function theorem says that if f(x, y) is a C1-function on an open
set U in R2 and at a point (x0, y0) in U we have f(x0, y0) = 0 and fy(x0, y0) ̸= 0, then for
all x close enough to x0 there is a unique g(x) near y0 such that f(x, g(x)) = 0, and g is C1
near x0. Here is an analogue of this result for formal power series “near (0, 0)”.
Example 10.11. (Formal implicit function theorem) Let f(X, Y ) = c10X + c01Y + · · ·
in R[[X, Y ]], so f(0, 0) = 0 and fY (0, 0) = c01. If fY (0, 0) ∈R×, then there is a unique
power series g(X) ∈XR[[X]] such that f(X, g(X)) = 0. To prove this, view R[[X, Y ]] as

<!-- page 24 -->
24
KEITH CONRAD
R[[X]][[Y ]] = A[[Y ]] where A = R[[X]], which is X-adically complete. Viewing f(X, Y ) in
R[[X]][[Y ]] means thinking of f(X, Y ) as a power series in Y whose coeﬃcients are power
series in X. We have |f(X, 0)|X = |c10X + · · · |X < 1 and fY (X, 0) is in R[[X]]× since its
constant term fY (0, 0) is a unit in R (Example 10.4), so there is a unique g(X) ∈XR[[X]]
such that f(X, g(X)) = 0 by Theorem 10.7 for power series in Y with A = R[[X]].
In particular, if K is a ﬁeld and f(X, Y ) ∈K[[X, Y ]] satisﬁes f(0, 0) = 0 and fY (0, 0) ̸= 0
then there is a unique g(X) ∈XK[[X]] such that f(X, g(X)) = 0. An example of this is
f(X, Y ) = cos X −1 + sin Y = X2/2 + Y + · · · in Q[[X]][[Y ]]. The constant term is 0
and the coeﬃcient of Y is nonzero in Q, so there is a unique g(X) ∈XQ[[X]] such that
sin(g(X)) = 1 −cos X. The series g(X) begins as −(1/2)X2 + (1/24)X4 −(1/45)X6 + · · · .
For a version of Hensel’s lemma where Zp is replaced by a complete local ring (possibly
not an integral domain), see [3, Theorem 7.3]. For a version of Hensel’s lemma dealing with
zeros of several polynomials in several variables, see [1].
Appendix A. Gauss’ work on p-adic roots
While Hensel introduced p-adic numbers in the early 1900s, unpublished work by Gauss
shows he was working with them over 50 years earlier. The scanned page below8 has the
heading (in Latin) “Inﬁnite Congruences” and begins with the equation
x5 −20x4 −86x3 −98x2 + 80x + 3 ≡0 mod 241∞,
where the modulus 241∞suggests the use of Z241. (The number 241 is prime.) There are
5 roots in Z241, which start oﬀas
2 + 191 · 241 + · · · , 3 + 238 · 241 + · · · , 4 + 192 · 241 + · · · , 5 + 65 · 241 + · · · 6 + 37 · 241 + · · ·
and below the equation are the ﬁrst digits of the roots (“habet radices” = “has roots”) and
the coeﬃcient of 241 in the ﬁrst root.
8This is from https://math.stackexchange.com/questions/844756/history-of-p-adic-numbers.

<!-- page 25 -->
HENSEL’S LEMMA
25
At the bottom left of the page, Gauss wrote
√
5 mod 11∞= 9 0 4 10 4 4. The congruence
x2 ≡5 mod 11 has two roots, 4 and 7, which lead to two square root of 5 in Z11, with the
ﬁrst one being
4 + 4 · 11 + 10 · 112 + 4 · 113 + 0 · 114 + 9 · 115 + · · ·
and these have the digits Gauss had found, but he wrote the expansion right to left rather
than left to right. The same 11-adic expansion appears in the middle of the page on the left
side. Lemmermeyer [7, p. 3] explains this as a calculation mod 116 of
√
5 = √1 + 4 · 11/3
using the binomial expansion of √1 + x at x = 44 split into terms with positive coeﬃcients
and negative coeﬃcients to get √1 + 4 · 11 = 1+2·11+9·112+3·113+1·114+5·115 mod 116.
References
[1] K. Conrad, A multivariable Hensel’s lemma, URL https://kconrad.math.uconn.edu/blurbs/gradnum
thy/multivarhensel.pdf.
[2] C. H. Edwards, Jr., “Advanced Calculus of Several Variables,” Academic Press, New York, 1973.
[3] D. Eisenbud, “Commutative Algebra with a View to Algebraic Geometry,” Springer-Verlag, New York,
1995.
[4] K. Hensel, Neue Grundlagen der Arithmetik, J. Reine Angew. Math. 127 (1904), 51–84 URL https://
eudml.org/doc/149178.
[5] K. Hensel, “Theorie der algebraischen Zahlen,” Teubner, Leipzig, 1908. URL https://archive.org/
details/in.ernet.dli.2015.493154.
[6] S. Lang, “Algebraic Number Theory,” 3rd ed., Springer-Verlag, New York, 1994.
[7] F. Lemmermeyer, Gauss and p-adic numbers, URL https://arxiv.org/pdf/2510.11559.
[8] R. Y. Lewis, A Formal Proof of Hensel’s Lemma over the p-adic Integers, URL http://robertylewis.
com/padics/padics.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*