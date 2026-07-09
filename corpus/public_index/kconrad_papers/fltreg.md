# Fermat's Last Theorem for Regular Primes

> **Source**: https://kconrad.math.uconn.edu/blurbs/fltreg.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
FERMAT’S LAST THEOREM FOR REGULAR PRIMES
KEITH CONRAD
For a prime p, we call p regular when the class number hp = h(Q(ζp)) of the pth cyclotomic
ﬁeld is not divisible by p. For instance, all primes p ≤19 have hp = 1, so they are regular.
Since h23 = 3, 23 is regular. All primes less then 100 are regular except for 37, 59, and 67:
h37 = 37, h59 = 3 · 59 · 233, and h67 = 67 · 12739. It is known that there are inﬁnitely many
irregular primes, and heuristics and tables suggest around 61% of primes should be regular
[8, p. 63], but the inﬁnitude of regular primes is still an open problem.
The signiﬁcance of p being regular is that if an ideal a in Z[ζp] has ap being principal,
then a is principal. Indeed, if ap is principal, then it is trivial in the class group of Q(ζp).
Since p doesn’t divide hp, a is trivial in the class group, so a is principal.
The concept of regular prime was introduced by Kummer in his work on Fermat’s Last
Theorem (FLT). He proved the following result in 1847.
Theorem 1. For a regular prime p ≥3, the equation xp + yp = zp does not have a solution
in positive integers x, y, z.
Before Kummer’s work, FLT for prime exponents1 was only completely settled for expo-
nents 3 (Euler in 1770, with a gap), 5 (Germain in 1823, Dirichlet and Lagrange in 1825)
and 7 (Lam´e in 1839).2 After Kummer’s work, FLT was known for all odd primes below
100 except 37, 59, and 67. Our goal is to prove Theorem 1.
Since p is a ﬁxed prime, we will write ζp simply as ζ. The complex conjugate of each
α in Q(ζ) is written as α. Since complex conjugation is an automorphism of Q(ζ), whose
Galois group over Q is abelian, σ(α) = σ(α) for all α in Q(ζ) and σ in Gal(Q(ζ)/Q).
We start with some lemmas valid in the pth cyclotomic ﬁeld for odd prime p.
Lemma 1. In Z[ζ], the numbers 1 −ζ, 1 −ζ2, . . . , 1 −ζp−1 are all associates and 1 + ζ is
a unit. Also p = u(1 −ζ)p−1 for some unit u and (1 −ζ) is the only prime ideal in Z[ζ]
dividing p.
Proof. For 1 ≤j ≤p −1, (1 −ζj)/(1 −ζ) = 1 + ζ + · · · + ζj−1 lies in Z[ζ].
Writing
1 ≡jj′ mod p, we see the reciprocal (1−ζ)/(1−ζj) = (1−ζjj′)/(1−ζj) lies in Z[ζj] = Z[ζ].
So 1 −ζj is a unit multiple of 1 −ζ. In particular, taking j = 2, which we can do since
2 ≤p −1, shows 1 + ζ is a unit (which is not true for p = 2)
Setting X = 1 in the equation 1 + X + · · · + Xp−1 = Qp−1
j=1(X −ζj) gives
p =
p−1
Y
j=1
(1 −ζj) =
p−1
Y
j=1
1 −ζj
1 −ζ (1 −ζ) = u(1 −ζ)p−1,
where u is a unit. Taking norms, pp−1 = N(1 −ζ)p−1, so (1 −ζ) has prime norm and thus
is a prime ideal. Since (p) = (1 −ζ)p−1, (1 −ζ) is the only prime ideal factor of p.
□
1Fermat himself had proved FLT for exponent 4.
2Two accounts of Lam´e’s ﬂawed 1847 work on FLT for general odd prime exponents are [5, pp. 6–8] and
https://math.stackexchange.com/questions/953462.
1

<!-- page 2 -->
2
KEITH CONRAD
Lemma 2. For v ∈Z[ζ]×, v/v is a root of unity.
Proof. For σ ∈Gal(Q(ζ)/Q), σ(v) = σv, so v/v and all of its Q-conjugates have absolute
value 1. Therefore, by a theorem of Kronecker, v/v is a root of unity [8, Lemma 1.6].
□
The roots of unity in Z[ζ] are ±ζj,3 and in fact v/v in the preceding lemma is a power
of ζ (i.e., no minus sign), but we won’t need that. (For a proof, see [8, p. 4].)
Work on Fermat’s Last Theorem always assumes there is a solution in positive integers
and then gets a contradiction. The general proof of Fermat’s Last Theorem in the 1990s
treats all hypothetical solutions in positive integers to xp + yp = zp, for a prime p ≥5, in
the same way. (For technical reasons4 the general proof doesn’t work if p = 3, but that
case was settled by the 19th century.) Before the 1990s, work on Fermat’s Last Theorem
usually broke up the analysis of a hypothetical solution (x, y, z) into two traditional cases:
Case I: show no solution (x, y, z) in pairwise relatively prime integers where p ∤xyz,
Case II: show no solution (x, y, z) in pairwise relatively prime integers where p | xyz.
By the relative primality of x, y, and z, in Case II p divides exactly one of x, y, or z.
Experience shows Case II is much harder to treat than Case I using cyclotomic methods.
From now on, p is regular. Since (−1)p = −1, Fermat’s Last Theorem is equivalent to
xp + yp = zp having no solution in nonzero integers, which lets us permute x, y, and z up
to sign, e.g., xp + yp = zp is the same as xp + (−z)p = (−y)p.
Case I: Suppose xp + yp = zp where x, y, z are nonzero integers with p not dividing x, y,
or z. We may of course assume x, y, and z are pairwise relatively prime.
In Z[ζ], factor Fermat’s equation as
(1)
zp = xp + yp =
p−1
Y
j=0
(x + ζjy).
Let’s show the factors on the right side generate relatively prime ideals. For 0 ≤j < j′ ≤
p −1, a common ideal factor d of (x + ζjy) and (x + ζj′y) must be a factor of the diﬀerence
x + ζjy −x −ζj′y = ζjy(1 −ζj′−j) = vy(1 −ζ)
for some unit v. (Here we use Lemma 1.) Since y(1 −ζ) divides yp, we have d | (yp). We
also know, by (1), that d divides (z)p. Since yp and zp are relatively prime integers, we
conclude d is the unit ideal, so the ideals (x + ζjy) are relatively prime.
The product of these ideals is the pth power (z)p, so unique ideal factorization implies
each factor is a pth power. Taking j = 1,
(x + ζy) = ap
for an ideal a. Thus ap is trivial in the class group of Q(ζ). Since p is regular, a is trivial
in the class group, so a = (t) where t ∈Z[ζ]. Thus
x + ζy = utp
for some unit u in Z[ζ].
(If we assume Z[ζ] is a UFD, this deduction follows from the
numbers x + ζjy being pairwise relatively prime: their product is a pth power so each is a
pth power up to unit multiple. We got this conclusion by the weaker assumption that p ∤hp
rather than hp = 1.)
3For p ≥5, there are units in Z[ζ] of inﬁnite order, such as ζ + ζ−1 since (ζ + ζ−1) P(p−1)/2
k=0
ζ4k+1 =
(ζ2(p+1) −1)/(ζ2 −1) = 1 by summing a ﬁnite geometric series.
4See https://math.stackexchange.com/questions/4464666.

<!-- page 3 -->
FERMAT’S LAST THEOREM FOR REGULAR PRIMES
3
Writing t = b0 + b1ζ + · · · + bp−1ζp−2, with bj in Z, we get
(2)
tp ≡b0 + b1 + · · · + bp−2 mod pZ[ζ],
so tp ≡tp mod pZ[ζ].
By Lemma 2, u/u = ±ζj for some j between 0 and p −1. If u/u = ζj then
x + ζy = utp
= ζjutp
≡ζjutp mod pZ[ζ]
≡ζj(x + ζy) mod pZ[ζ].
Thus
(3)
u/u = ζj =⇒x + yζ −yζj−1 −xζj ≡0 mod pZ[ζ].
Similarly,
(4)
u/u = −ζj =⇒x + yζ + yζj−1 + xζj ≡0 mod pZ[ζ].
We want to show neither of these congruences can hold when 0 ≤j ≤p −1 and x and y
are integers prime to p.
Since x and y are nonzero mod p, these congruences appear to show linear depen-
dence over Z/(p) among some powers of ζ in Z[ζ]/(p). However, in Z[ζ]/(p) the powers
1, ζ, . . . , ζp−2 are linearly independent over Z/(p) since
Z[ζ]/(p) ∼= Z[X]/(p, Φp(X)) ∼= (Z/(p))[X]/Φp(X) ∼= (Z/(p))[X]/(X −1)p−1,
and {1, X, . . . , Xp−2} is a basis of the last ring, over Z/(p).
For those j ≤p −1 such
that 1, ζ, ζj−1, ζj are distinct powers in the set {1, ζ, . . . , ζp−2}, i.e., as long as 0, 1, j −1, j
are distinct integers with j ≤p −2, (3) and (4) both yield a contradiction.
So when
3 ≤j ≤p −2, there is a contradiction in Case I.
The rest of the proof is an accounting exercise in handling the remaining cases j = 0, 1, 2,
and p −1.
First of all, we may take p ≥5, since the equation x3 + y3 = z3 has no solutions in
integers prime to 3. (Even the congruence x3 + y3 ≡z3 mod 9 has no solutions in numbers
prime to 3, since the cubes of units mod 9 are ±1.)
Can j = p −1? If so, then the left side of the congruence in (3) becomes
x(1 −ζp−1) + y(ζ −ζp−2) = 2x + (x + y)ζ + x(ζ2 + · · · + ζp−3) + (x −y)ζp−2,
which contradicts linear independence of 1, ζ, . . . , ζp−2 mod p over Z/(p) by looking at the
coeﬃcient of, say, ζ2. There is a similar contradiction in (4) if j = p −1.
Can j = 0? If so, then (3) becomes y(ζ −ζ−1) ≡0 mod pZ[ζ]. Since y is not divisible by
p, we can divide by it and get ζ2 −1 ≡0 mod p, which contradicts linear independence of
1 and ζ2 mod p since p ≥5. Similarly, (4) with j = 0 implies 2xζ + yζ2 + y ≡0 mod p, so
again we get a contradiction.
Setting j = 2 in (3) or (4) leads to contradictions of linear independence as well. We
now are left with the case j = 1. In this case (4) implies (x + y)(1 + ζ) ≡0 mod p, so
x + y ≡0 mod pZ. (Here we use Lemma 1.) Thus zp = xp + yp ≡(x + y)p ≡0 mod p, so p
divides z. That violates the condition of Case I. The only remaining case is j = 1 in (3).

<!-- page 4 -->
4
KEITH CONRAD
To summarize, we have shown that if xp + yp = zp and x, y, z are not divisible by p, then
x + ζy = utp where u/u = ζ. Setting j = 1 in (3) yields
(5)
x(1 −ζ) + y(ζ −1) ≡0 mod p.
Writing p = u(1 −ζ)p−1, (5) implies
x ≡y mod (1 −ζ)p−2.
Since p −2 ≥1 and x and y are in Z, this forces x ≡y mod pZ. Running through the proof
with y and −z interchanged, we get x ≡−z mod pZ, so
0 = xp + yp −zp ≡3xp mod p.
Since p ̸= 3 and x is prime to p, we have a contradiction. This settles Case I for p a regular
prime.
□
Although we used congruences to prove the nonsolvability of xp + yp = zp in integers
prime to p (when p is regular), there often are solutions to xp + yp ≡zp mod pm for large
m and x, y, z all prime to p. For instance, 17 + 307 ≡317 mod 49 and from this one can
solve x7 + y7 ≡z7 mod 7m in numbers prime to 7, for every m. So it is rather hard to try
proving nonsolvability of Fermat’s equation with odd prime exponent using congruences
in Z. (This is why many crank proofs of FLT, based on elementary number theory, are
doomed to failure.) What we used in the above proof were congruences in Z[ζ], not in Z.
We now pass to Case II. Our treatement is taken largely from [7, pp. 31–33].
Case II. Assume Fermat’s equation has a solution in nonzero integers x, y, z with at least
one number divisible by p. Since p is odd, we may write the equation in the symmetric
form xp + yp + zp = 0. If p divides two of x, y, or z, then it divides the third as well. So
removing the highest common factor of p from the three numbers, we can assume p divides
only one of the numbers, say p | z. Writing z = prz0, with z0 prime to p and r ≥1, Fermat’s
equation reads
(6)
xp + yp + w(1 −ζ)pr(p−1)zp
0 = 0.
for some unit w in Z[ζ] and p not dividing xyz0. Since (1 −ζ) is the only prime over p
in Z[ζ] and x, y, z0 are in Z, saying xyz0 is not divisible by p in Z is equivalent to saying
xyz0 is not divisible by (1 −ζ) in Z[ζ]. We now suitably generalize the form of (6), thereby
making it easier to prove a stronger result.
Theorem 2. For a regular prime p ≥3, there do not exist α, β, γ in Z[ζ], all nonzero, such
that
(7)
αp + βp + ε(1 −ζ)pnγp = 0,
where ε ∈Z[ζ]×, n ≥1, and (1 −ζ) does not divide αβγ.
In particular, (6) and Theorem 2 show Fermat’s Last Theorem for exponent p has no
solution in Case II when p is regular. The need for allowing a unit coeﬃcient ε other than
1 is already evident in how Theorem 2 is applied to Case II of FLT.
Proof. By (7), we have the ideal equation
(8)
p−1
Y
j=0
(α + ζjβ) = (1 −ζ)pn(γ)p.
Since γ is nonzero, the left side is nonzero, so α + β, α + ζβ, . . . , α + ζp−1β are all nonzero.

<!-- page 5 -->
FERMAT’S LAST THEOREM FOR REGULAR PRIMES
5
Unlike Case I, the factors on the left side will not be relatively prime ideals. The plan
of the proof is to analyze the ideal factorization of each term on the left and then use the
regularity hypothesis to prove certain ideals are principal.
We will work often with congruences in Z[ζ]/(1−ζ) and Z[ζ]/(1−ζ)2. Note Z[ζ]/(1−ζ) ∼=
Z/(p) and (for p ≥3) Z[ζ]/(1−ζ)2 ∼= (Z/(p))[X]/(1−X)2. For a number δ(1−ζ) considered
modulo (1−ζ)2, δ only matters modulo 1−ζ, so there are p multiples of 1−ζ in Z[ζ]/(1−ζ)2.
Because α + ζjβ ≡α + β mod (1 −ζ) and the prime (1 −ζ) divides some factor on the
left side of (8), it divides all factors on the left side. We want to show some α + ζj0β is
divisible by 1 −ζ twice, i.e., α + ζj0β ≡0 mod (1 −ζ)2.
Assume, to the contrary, that 1 −ζ divides each factor on the left side of (8) exactly
once. (That is, assume n = 1.) Then each of the p factors on the left side of (8) reduces to
a nonzero multiple of 1 −ζ mod (1 −ζ)2. (Convince yourself of this.) However, there are
p −1 distinct nonzero multiples of 1 −ζ modulo (1 −ζ)2, so we must have
α + ζjβ ≡α + ζj′β mod (1 −ζ)2
for some 0 ≤j < j′ ≤p −1. Therefore (1 −ζj′−j)β ≡0 mod (1 −ζ)2. Since 1 −ζj′−j
is a unit multiple of 1 −ζ, this congruence forces 1 −ζ to divide β. But that violates the
hypothesis of the theorem.
Thus n ≥2 and some α + ζj0β is ≡0 mod (1 −ζ)2. By the previous paragraph, j0 is
unique. Replacing β with ζj0β in the statement of the theorem, we may assume that j0 = 0,
so α + β ≡0 mod (1 −ζ)2 and α + ζjβ ̸≡0 mod (1 −ζ)2 for 1 ≤j ≤p −1.
Since αβ ̸≡0 mod 1 −ζ, a common divisor of two factors on the left side of (8) must be
d(1 −ζ), where d = (α, β). Note (1 −ζ)d is independent of j, so it must appear as a pth
power on the left side of (8). The complementary divisor of (1 −ζ)d in (α + ζjβ) must be a
pth power by considering the right side of (8) and unique factorization of ideals. Therefore
(α + ζjβ) = d(1 −ζ)cp
j,
(α + β) = d(1 −ζ)np−(p−1)cp
0,
where 1 ≤j ≤p −1 and (1 −ζ) does not divide c0, c1, . . . , cp−1.
Taking ratios, we see that cp
jc−p
0
is a principal fractional ideal. Since p is regular, cjc−1
0
is a principal fractional ideal, so cjc−1
0
= tjZ[ζ], where tj ∈Q(ζ)× is prime to 1 −ζ. The
equation of ideals
(α + ζjβ)(α + β)−1 = (tj)p(1 −ζ)−p(n−1)
can be written as an elementwise equation
(9)
α + ζjβ
α + β
=
εjtp
j
(1 −ζ)p(n−1) ,
where 1 ≤j ≤p −1 and εj ∈Z[ζ]×.
Now consider, out of nowhere (!), the elementwise equation
ζ(α + ζβ) + (α + ζβ) −(1 + ζ)(α + β) = 0.
Note ζ = ζp−1. Dividing by α + β ̸= 0 and using (9),
ζεp−1tp
p−1
(1 −ζ)p(n−1) +
ε1tp
1
(1 −ζ)p(n−1) −(1 + ζ) = 0.
Clearing denominators,
(10)
ζεp−1tp
p−1 + ε1tp
1 −(1 + ζ)(1 −ζ)p(n−1) = 0.

<!-- page 6 -->
6
KEITH CONRAD
Write tj = xj/yj for some xj, yj ∈Z[ζ]. Since tj is prime to 1 −ζ and 1 −ζ generates
a prime ideal, xj and yj are each divisible by the same power of 1 −ζ. We can remove
this factor from both xj and yj and thus assume xj and yj are prime to 1 −ζ. Feeding the
formulas t1 = x1/y1 and tp−1 = xp−1/yp−1 into (10) and then clearing denominators,
ζεp−1cp
p−1 + ε1cp
1 −(1 + ζ)(1 −ζ)p(n−1)cp
0 = 0
where c0, c1, cp−1 ∈Z[ζ] are prime to (1 −ζ). Dividing by the (unit) coeﬃcient of cp
p−1,
(11)
cp
p−1 +
ε1
ζεp−1
cp
1 −1 + ζ
ζεp−1
(1 −ζ)p(n−1)cp
0 = 0.
This equation is very similar to (7), with n replaced by n −1. Note, for instance, the
coeﬃcient of (1 −ζ)p(n−1)cp
0 is a unit in Z[ζ] and c0, c1, cp−1 are prime to (1 −ζ).
Comparing (7) and (11), note the coeﬃcient of βp is 1 while the coeﬃcient of cp
1 is surely
not 1. If the coeﬃcient of cp
1 were a pth power (necessarily the pth power of another unit,
since the coeﬃcient is itself a unit), then we could absorb the coeﬃcient into cp
1 and obtain
an equation just like that in the statement of the theorem, with n replaced by n −1.
To show the coeﬃcient of cp
1 is a pth power, consider (11) modulo p:
cp
p−1 +
ε1
ζεp−1
cp
1 ≡0 mod pZ[ζ].
Since cp
1 and cp
p−1 are congruent to rational integers mod pZ[ζ] (see (2)), and also c1 is prime
to 1 −ζ, we can invert c1 modulo pZ[ζ] to get
ε1
ζεp−1
≡rational integer mod pZ[ζ].
Now we invoke a deep fact.
Kummer’s Lemma: Let p is regular and u be a unit in Z[ζ]. If there is some m ∈Z such
that u ≡m mod pZ[ζ], then u is the pth power of a unit in Z[ζ].
For proofs of Kummer’s Lemma, see [1, p. 377] or [8, Theorem 5.36].5 Somewhere in a
proof of Kummer’s Lemma a connection needs to be made between units in Z[ζ] and the
class number hp. Two connections, which each serve as the basis for a proof of Kummer’s
Lemma, are the facts that 1) adjoining the pth root of a unit to Q(ζ) is an abelian unramiﬁed
extension, whose degree over Q(ζ) must divide hp by class ﬁeld theory, and 2) the index
of the group of real cyclotomic units in Q(ζ) as a subgroup of all real units is equal to the
“plus part” of hp [8, Theorem 8.2].
Thanks to Kummer’s Lemma, we can replace the coeﬃcient of cp
1 in (11) with 1, obtaining
cp
p−1 + cp
1 + ε′(1 −ζ)p(n−1)cp
0 = 0.
This has the same form and conditions as the original equation, but n ≥1 is replaced with
n −1. Since we showed that in fact n ≥2, we have n −1 ≥1, so we have a contradiction
by descent.
□
The greatest diﬀerence between our proofs of Case I and Case II is the use of Kummer’s
Lemma in Case II, which amounts to using subtle relations between the class number and
the unit group of the pth cyclotomic ﬁeld. We could aﬀord to be largely ignorant about
Z[ζ]× in the proof of Case I for regular primes, and the proof of that case was much simpler.
5Or see https://kconrad.math.uconn.edu/blurbs/gradnumthy/kummer.pdf.

<!-- page 7 -->
FERMAT’S LAST THEOREM FOR REGULAR PRIMES
7
Even if p is not regular, Case I continues to be easier than Case II. That is, it is much
easier to show (when using cyclotomic methods) that there isn’t a solution to xp + yp = zp
where p ∤xyz than where p | xyz. For example, a theorem of Wieferich [4, p. 221] says
that if xp + yp = zp and p doesn’t divide x, y, or z, then 2p−1 ≡1 mod p2. The only primes
less than 3 × 109 satisfying this congruence are 1093 and 3511. Mirimanoﬀproved that also
3p−1 ≡1 mod p2 if Case I has a solution, and neither 1093 nor 3511 satisﬁes this congruence.
So that settles Case I for all odd primes below 3 × 109. In fact, it has been shown [8, p.
181] that a counterexample to Fermat in Case I for exponent p implies qp−1 ≡1 mod p2 for
all primes q ≤89, and that settles Case I for p < 7.57 × 1017.
When Kummer proved Fermat’s Last Theorem for a regular prime exponent p, he origi-
nally thought he proved a stronger result: for regular p, the equation αp + βp = γp has no
solution in nonzero α, β, γ in the ring Z[ζ], not just in the ring Z. However, in the course of
his proof he assumed α, β, and γ are pairwise relatively prime elements, and that doesn’t
make sense when Z[ζ] is not a UFD. Nevertheless, Kummer’s proof did basically cover the
more general setting of no solutions in Z[ζ] and Hilbert patched it up. For a proof of that,
see [3, Chap. 11] or [6, §V.3]. As in the treatment above, there are two cases: (i) none of
α, β, or γ are divisible by 1−ζ and (ii) at least one of α, β, or γ is divisible by 1−ζ. (Even
if Z[ζ] is not a UFD, 1 −ζ generates a prime ideal in Z[ζ], so divisibility by 1 −ζ in Z[ζ]
behaves nicely.) Case (ii) is essentially identical to the proof we gave of Case II above.
When p is irregular, what is known about Fermat’s Last Theorem for exponent p in the
ring Z[ζ]? The ﬁrst such prime is 37 and there are no solutions to x37 + y37 = z37 for
nonzero x, y, and z in the integers of the 37-th cyclotomic ﬁeld.6
Exercises
1. Find a regular prime p ≥3 and an integer m ≥1 for which the congruence xp + yp ≡
zp mod (1 −ζp)m has no solutions x, y, z ∈Z[ζp] that are all prime to 1 −ζp.
2. Prove Z[ζp]/(1 −ζp)2 ∼= (Z/(p))[X]/(1 −X)2 for p ≥3 and not for p = 2.
3. Let K be a number ﬁeld, with p1, . . . , pr distinct primes of OK. For α ∈K× with
ordpj(α) = 0 for all j, prove α = x/y for some x, y ∈OK that are both prime to all the pj.
Prove this ﬁrst in the easier case when all the pj are principal, and then when they need
not be principal. (Hint: Thinking of primes as points and the multiplicity of a prime as an
order of vanishing, the proof of [2, Prop. 2(2), Sect. 2.4] may provide some inspiration.)
References
[1] Z. I. Borevich and I. R. Shafarevich, “Number Theory,” Academic Press, New York, 1966.
[2] W. Fulton, “Algebraic Curves,” Addison-Wesley, Redwood City, CA, 1989. URL https://dept.math.
lsa.umich.edu/∼wfulton/CurveBook.pdf.
[3] E. Grosswald, “Topics from the Theory of Numbers,” Macmillan, New York, 1965.
[4] K. Ireland and M. Rosen, “A Classical Introduction to Modern Number Theory,” 2nd ed., Springer–
Verlag, New York, 1990.
[5] H. W. Lenstra, Jr., Euclidean Number Fields 1, Math. Intelligencer 2 (1979), 6–15.
[6] P. Ribenboim, “13 Lectures on Fermat’s Last Theorem,” Springer–Verlag, New York, 1979.
[7] A. van der Poorten, “Notes on Fermat’s Last Theorem,” J. Wiley & Sons, New York, 1996.
[8] L. Washington, “An Introduction to Cyclotomic Fields,” 2nd ed., Springer-Verlag, New York, 1997.
6See https://mathoverflow.net/questions/56107.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*