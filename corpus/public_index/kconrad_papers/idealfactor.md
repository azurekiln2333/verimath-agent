# Unique Factorization of Ideals

> **Source**: https://kconrad.math.uconn.edu/blurbs/idealfactor.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
IDEAL FACTORIZATION
KEITH CONRAD
1. Introduction
We will prove here the fundamental theorem of ideal theory in number ﬁelds: every
nonzero proper ideal in the integers of a number ﬁeld admits unique factorization into
a product of nonzero prime ideals. Then we will explore how far the techniques can be
generalized to other domains.
Deﬁnition 1.1. For ideals a and b in a commutative ring, write a | b if b = ac for an ideal
c.
Theorem 1.2. For elements α and β in a commutative ring, α | β as elements if and only
if (α) | (β) as ideals.
Proof. If α | β then β = αγ for some γ in the ring, so (β) = (αγ) = (α)(γ). Thus (α) | (β) as
ideals. Conversely, if (α) | (β), write (β) = (α)c for an ideal c. Since (α)c = αc = {αc : c ∈c}
and β ∈(β), β = αc for some c ∈c. Thus α | β in the ring.
□
Theorem 1.2 says that passing from elements to the principal ideals they generate does
not change divisibility relations. However, irreducibility can change.
Example 1.3. In Z[√−5], 2 is irreducible as an element but the principal ideal (2) factors
nontrivially: (2) = (2, 1 + √−5)(2, 1 −√−5).
To see that neither of the ideals (2, 1 + √−5) and (2, 1 −√−5) is the unit ideal, we give
two arguments. Suppose (2, 1 + √−5) = (1). Then we can write
1 = 2(a + b
√
−5) + (1 +
√
−5)(c + d
√
−5)
for some integers a, b, c, and d. Collecting real and imaginary parts,
1 = 2a + c −5d,
0 = 2b + c + d.
Solving for d in the second equation and substituting that into the ﬁrst,
1 = 2a + 10b + 6c,
which is impossible since the right side is even. The proof that (2, 1−√−5) ̸= (1) is similar.
For another proof, complex conjugation is an operation on ideals, a 7→a := {α : α ∈a}
that respects addition and multiplication of ideals, and (α, β) = (α, β). In particular, the
conjugate of (2, 1 + √−5) is (2, 1 −√−5), so if (2, 1 + √−5) = (1) then (2, 1 −√−5) = (1),
so the product (2, 1 + √−5)(2, 1 −√−5) = (2) is (1)(1) = (1). But (2) ̸= (1) since 2 is not
a unit in Z[√−5].
If a | b then for some ideal c we have b = ac ⊂a, so a ⊃b.
Divisibility implies
containment. The converse may fail in some rings (see Example 8.2), but in the ring of
integers of a number ﬁeld it will turn out that containment implies divisibility. So it is
useful to think about containment of ideals in a commutative ring as a preliminary form of
1

<!-- page 2 -->
2
KEITH CONRAD
divisibility: a ⊃b is something like a | b. Consider in this light the following result about
containment in prime ideals.
Theorem 1.4. In a commutative ring A, an ideal p is prime if and only if for all ideals a
and b in A,
p ⊃ab ⇒p ⊃a or p ⊃b.
Proof. First suppose p is a prime ideal. If p ⊃ab and p ̸⊃a, pick x ∈a with x ̸∈p. For
every y ∈b, xy ∈ab ⊂p, so by primality of p we get x ∈p or y ∈p. Since x ̸∈p, y ∈p.
This holds for all y ∈b, so b ⊂p, i.e., p ⊃b.
Now suppose p is an ideal such that, for every pair of ideals a and b, if p contains ab
then p contains a or b. If x, y ∈A and xy ∈p, then (x)(y) = (xy) ⊂p, so (x) or (y) is in p.
Thus x or y is in p, so p is prime.
□
Corollary 1.5. Let K be a number ﬁeld. In OK, if p ⊃p1 · · · pr where all the ideals are
nonzero and prime, then p = pi for some i.
Proof. By Theorem 1.4, p ⊃pi for some i. Since nonzero prime ideals in OK are maximal,
p = pi.
□
To prove the nonzero proper ideals of OK have unique prime factorization, we will ﬁrst
show how to invert a nonzero prime ideal. The inverse will be an OK-module that is in K
but not in OK (e.g., in Q the inverse of 2Z is (1/2)Z), so in Section 2 we will introduce
the kinds of OK-modules we need. That nonzero prime ideals have inverses will be proved
in Section 3, and after collecting a few corollaries of this invertibility we will obtain unique
factorization of ideals in OK.
Consequences of unique factorization (or, in some cases,
consequences of the results used to prove unique factorization) are discussed in Section 4.
In Section 5, the methods for OK are extended to the integral closure of F[T] in a ﬁnite
extension of F(T) (the “function ﬁeld” case). Another approach to unique factorization is
discussed in Section 6, which is independent of the other sections. In Section 7 we generalize
the norm operation from elements of OK to ideals. Finally, in Section 8 we discuss how to
extend unique factorization of ideals to non-maximal orders.
2. Fractional Ideals
To invert ideals, we introduce OK-modules that are “ideals with a denominator.”
Deﬁnition 2.1. A fractional ideal in K is a nonzero OK-module I ⊂K such that for some
d ∈OK −{0}, dI ⊂OK. Such a d is called a common denominator for I.
Since dI is an OK-module in OK, dI is an ideal of OK. Letting a denote dI, we have
I = 1
da. Conversely, if a ⊂OK is a nonzero ideal and d ∈OK −{0} then 1
da is an OK-module
in K with common denominator d, so 1
da is a fractional ideal.
Example 2.2. Since Z is a PID, the fractional ideals in Q are subgroups (Z-submodules)
of Q having the form rZ for r ∈Q×. Examples include 1
2Z and 6
5Z = 6 · 1
5Z.
Theorem 2.3. The following properties of an OK-module I ⊂K are equivalent:
(1) I is a fractional ideal: for some d ∈OK −{0}, dI ⊂OK,
(2) dI ⊂OK for some d ∈Z −{0},
(3) I = xa for some x ∈K× and some nonzero ideal a in OK,
(4) I is a nonzero ﬁnitely generated OK-module in K.

<!-- page 3 -->
IDEAL FACTORIZATION
3
Proof. (1) ⇒(2): Let I be a fractional ideal and dI ⊂OK. Every nonzero OK-multiple of
d is also a common denominator for I. In particular, since d | NK/Q(d) in OK we can use
NK/Q(d) ∈Z −{0} as a common denominator for I.
(2) ⇒(3): Since dI is an OK-module in OK, dI is an ideal. Take a = dI and x = 1/d to
see that I = xa.
(3) ⇒(4): An ideal a in OK is ﬁnitely generated as a Z-module, and thus ﬁnitely
generated as an OK-module. Its scalar multiple xa is also ﬁnitely generated over OK.
(4) ⇒(1): Write I = OKx1 + · · · + OKxd where the xi’s are in K and at least one is
nonzero. We want to ﬁnd a d ∈OK −{0} such that dI ⊂OK. Since OK has fraction ﬁeld
K, for each xi there is a di ∈OK −{0} such that dixi ∈OK. Let d be the product of the
di’s, so dxi ∈OK for all i. Thus dI ⊂OK.
□
Corollary 2.4. Every fractional ideal in K is a free Z-module of rank [K : Q].
Proof. This is true for nonzero ideals in OK and a fractional ideal is just a nonzero scalar
multiple of such an ideal.
□
Not all OK-submodules of K are fractional ideals. For instance, in Q the subgroup Z[1/2]
is not a fractional ideal: it admits no common denominator. The fractional ideals of K are
the (nonzero) ﬁnitely generated OK-submodules of K.
By comparison with fractional ideals, nonzero ideals in OK are called integral ideals.
(Think of the terms integer and fraction.) A fractional ideal of the form xOK for x ∈K×
is called principal. Writing x = α/m for α ∈OK and m ∈Z −{0}, xOK = 1
m · αOK, so a
principal fractional ideal is the same thing as a nonzero principal ideal in OK divided by an
integer. When OK is a PID, all fractional ideals in K are principal (and conversely).
The OK-modules in K can be added and multiplied, with multiplication being commu-
tative, associative, distributing over addition, and having multiplicative identity (1) = OK.
The sum and product of ideals in OK are ideals, so the sum and product of fractional ideals
are fractional ideals.
Deﬁnition 2.5. For a fractional ideal I in OK, set
eI = {x ∈K : xI ⊂OK}.
This is more than the common denominators of I, since we allow x ∈K and not just
x ∈OK −{0}. Each common denominator of I is in eI, so eI ̸= {0}. The set eI is an OK-
module. In fact, eI is a fractional ideal. To see this, pick a nonzero y ∈I. Then yeI ⊂OK,
so eI ⊂(1/y)OK. Therefore eI is a submodule of a ﬁnite free Z-module, so eI is a ﬁnitely
generated Z-module, hence ﬁnitely generated as an OK-module too. Thus eI is a fractional
ideal by Theorem 2.3(4).
Example 2.6. If a = αOK is a principal ideal in OK with α ̸= 0 then ea = {x ∈K :
xαOK ⊂OK} = (1/α)OK and aea = OK = (1). In particular, eOK = OK.
The importance of eI is that it is the only possible candidate for a multiplicative inverse
to I among the fractional ideals in K:
Theorem 2.7. Let I be a fractional ideal in the number ﬁeld K. If I admits a fractional
ideal inverse then the inverse must be eI.
Proof. Suppose there is a fractional ideal J such that IJ = OK. For all y ∈J, yI ⊂JI =
IJ = OK, so J ⊂eI. Multiplying this inclusion by I, OK ⊂I eI. At the same time, for all
x ∈eI we have xI ⊂OK, so eII ⊂OK.

<!-- page 4 -->
4
KEITH CONRAD
Hence I eI = OK and J = JOK = JI eI = OK eI = eI.
□
We can use Theorem 2.7 in two ways: to show I is not invertible we only have to check
II ̸= (1), and if we ﬁnd IJ = (1) for some J then we immediately know J = eI (even if J
was not originally deﬁned in that way).
Example 2.8. If I and J are fractional ideals with IJ = (x) a principal fractional ideal,
then 1
xJ is a multiplicative inverse for I, so eI =
1
xJ. For instance, in Z[√−5] let I =
(3, 1 + √−5) and J = (3, 1 −√−5). Check that IJ = (3). Therefore
eI = 1
3J = 1
3(3, 1 −
√
−5) = Z[
√
−5] + 1 −√−5
3
Z[
√
−5].
Check that if I1 ⊂I2 are fractional ideals then eI2 ⊂eI1. As a special case of this reversed
inclusion, if a is a nonzero ideal in OK then OK ⊂ea.
Remark 2.9. In Theorem 2.7, all we used about I is that it is an OK-module inside of K;
the fractional ideal hypothesis (i.e., I is a ﬁnitely generated OK-module) was not explicitly
invoked in the proof and the deﬁnition of eI makes sense for all OK-submodules I ⊂K.
However, the scope of validity of Theorem 2.7 is not made broader by this observation,
because an invertible OK-module in K must be ﬁnitely generated: if I eI = OK then 1 =
x1y1 + · · · + xryr for some r ≥1, xi ∈I, and yi ∈eI. Then for all x ∈I we have
x = x · 1 = (xy1)x1 + · · · + (xyr)xr ∈OKx1 + · · · + OKxr,
so I ⊂P OKxi. The reverse inclusion is immediate since I is an OK-module, so I = P OKxi
is a ﬁnitely generated OK-module in K and thus is a fractional ideal (Theorem 2.3).
3. Inverses of Prime Ideals
Prime factorization in Z can be proved by contradiction: if some integer greater than 1
has no prime factorization then let n > 1 be minimal without a prime factorization. Of
course n is not prime, so n = ab with a, b > 1. Then a, b < n, so a and b are products
of primes. Hence n = ab is a product of primes, which is a contradiction. Uniqueness
of the prime factorization requires more work. We will use the same idea (contradiction
from a minimal counterexample) to prove nonzero proper ideals in OK have prime ideal
factorization. The basic method is to induct on the index [OK : a] = |OK/a|.
Lemma 3.1. Every nonzero ideal in OK contains a product of nonzero prime ideals.
Returning to the intuitive idea that containment is a preliminary kind of divisibility, the
idea of this lemma is something like “every nonzero ideal divides a product of primes.”
Proof. Every nonzero ideal of OK has ﬁnite index. Assume the lemma is false and let a be a
nonzero ideal of least index that does not contain a product of nonzero prime ideals. Then
a ̸= OK since OK contains nonzero prime ideals, so [OK : a] ≥2. Since a can’t be a prime
ideal, there must be x and y in OK that are not in a but xy ∈a. Then the ideals (x) + a
and (y) + a both properly contain a, so they have smaller index in OK than a does. Thus
(x) + a and (y) + a contain products of nonzero prime ideals:
p1 · · · pr ⊂(x) + a,
q1 · · · qs ⊂(y) + a
for some nonzero primes pi and qj, so
(3.1)
p1 · · · prq1 · · · qs ⊂((x) + a)((y) + a) = (xy) + xa + ya + a2 ⊂a,

<!-- page 5 -->
IDEAL FACTORIZATION
5
where we used xy ∈a for the last step. By (3.1), a contains a product of nonzero prime
ideals. This is a contradiction.
□
Notice this proof is close to the proof that every integer > 1 is a product of primes. Why
didn’t we prove in Lemma 3.1 that every nonzero proper ideal equals (rather than merely
contains) a product of nonzero prime ideals? Because we do not know (yet) that every
non-prime ideal in OK is a product of ideals with smaller index.
The following theorem is the key technical property of nonzero prime ideals in OK.
Theorem 3.2. For each nonzero prime ideal p of OK, the fractional ideal ep deﬁned in
Deﬁnition 2.5 satisﬁes the following properties:
(1) OK ⊂ep and the containment is strict,
(2) pep = OK.
In particular, every nonzero prime ideal in OK is invertible as a fractional ideal.
Proof. Since p ⊂OK, OK ⊂ep. We need to ﬁnd an element of ep that is not in OK. The
element will arise as a ratio y/x with arbitrary nonzero x ∈p and a carefully chosen y ∈OK.
(For example, in the ring Z use p = 2Z, so ep = (1/2)Z. An element of ep not in Z is n/2
for odd n. We can write n/2 = (nm)/(2m) for all nonzero m in Z, and 2m is an arbitrary
nonzero element of p, but nm is not arbitrary.)
Pick x ∈p with x ̸= 0. Then p ⊃(x). From Lemma 3.1,
(x) ⊃p1p2 · · · pr
for some nonzero primes pi.
Use such a product where r is minimal.
If r = 1 then
p ⊃(x) ⊃p1, so p = p1 since both ideals are maximal. Thus p = (x), so ep = (1/x)OK ̸= OK,
which is what we wanted (with y = 1). Thus we may suppose r ≥2.
Since p ⊃(x) ⊃p1 · · · pr, p = pi for some i by Corollary 1.5. Without loss of generality,
p = p1. Then (x) ⊃p · p2 · · · pr. By the minimality of r, (x) does not contain the product
p2 · · · pr. So there is a y ∈p2 · · · pr with y ̸∈(x). Thus y/x ̸∈OK. Since yp ⊂pp2 · · · pr ⊂
(x) = xOK, (y/x)p ⊂OK. This shows y/x ∈ep, and we already saw that y/x ̸∈OK. Thus
we have settled the ﬁrst part.
Now we will show why the second part (which is more interesting) follows from the ﬁrst
part. Picking x ∈ep with x ̸∈OK, we have xp ⊂OK, so p ⊂p + xp ⊂OK. Since p is
maximal, p + xp = p or p + xp = OK. The second option says p(OK + xOK) = OK, so
OK + xOK is a fractional ideal inverse for p and must be ep by Theorem 2.7. We will show
this option holds by eliminating the ﬁrst option by contradiction.
Assume p + xp = p, or equivalently xp ⊂p. That means multiplication by x preserves
the ﬁnitely generated Z-module p. Recall the “linear” characterization for an element of K
to be an algebraic integer: it lies in a subring of K that’s a ﬁnitely generated Z-module.
The subring aspect is needed only to be sure that multiplication by the particular element
preserves the subring. But the condition xp ⊂p has exactly the same feature, even though
x need not lie in p (and p is not a subring of K but an ideal of OK). Therefore since p is a
ﬁnitely generated Z-module, the linear characterization of integrality can be applied to see
from xp ⊂p that x is integral over Z. Hence x ∈OK. But x ̸∈OK by its very deﬁnition,
so we are done.
□
Corollary 3.3. For nonzero ideals a and b in OK and nonzero prime p, pa = pb if and
only if a = b.

<!-- page 6 -->
6
KEITH CONRAD
Proof. If a = b then of course pa = pb. Conversely, if pa = pb, multiply both sides by ep.
Since OK-module multiplication is associative, the p-terms cancel because epp = OK.
□
Corollary 3.4. For every nonzero ideal a of OK and nonzero prime p, p ⊃a if and only if
p | a as ideals.
Proof. If p | a, obviously p ⊃a. Conversely, suppose p ⊃a. If we are going to be able to
write pb = a for some ideal b then it must be the case that b = epa. Thus, deﬁne b = epa.
This is a nonzero OK-module in K. Since p ⊃a, multiplying by ep shows OK ⊃epa = b, so
b is an OK-module in OK, i.e., b is an ideal in OK. Easily pb = a, so p | a as ideals.
□
Corollary 3.5. For every nonzero ideal b and nonzero prime p, pb ⊂b with strict inclusion.
This means multiplication by a prime ideal shrinks the ideal.
Proof. Easily pb ⊂b. If pb = b then b = p(pb) = p2b, and similarly b = pkb for all k ≥1.
Therefore b ⊂pk for all k ≥1, so
OK ⊃p ⊃p2 ⊃p3 ⊃· · · ⊃pk ⊃· · · ⊃b.
The index [OK : b] is ﬁnite, so the descending chain of powers of p must stabilize: pk+1 = pk
for some k. Then cancelling k factors of p using Corollary 3.3 implies p = OK, which is a
contradiction. Thus pb ̸= b.
□
Now we are (ﬁnally) ready to prove unique prime factorization of ideals in OK. All the
hard work is over!
Theorem 3.6. Every nonzero proper ideal of OK is uniquely a product of nonzero prime
ideals in OK.
Proof. Existence: We will prove by induction on r ≥1 that if a nonzero proper ideal a ⊂OK
contains a product of r nonzero prime ideals then it equals a product of nonzero prime ideals.
(Every nonzero proper ideal ﬁts this condition for some r since, by Lemma 3.1, every nonzero
ideal in OK contains a product of nonzero prime ideals.) When r = 1, a ⊃p for a nonzero
prime p, so p is maximal and a = p. Assuming the result for r, suppose a ⊃p1 · · · pr+1.
Since a is a proper ideal, a ⊂p for some maximal ideal p. Then p ⊃p1 · · · pr+1, so p = pi for
some i. All nonzero prime ideals in OK are invertible, so multiplying through the inclusion
pi ⊃a ⊃p1 · · · pr+1 by p−1
i
gives OK ⊃p−1
i a ⊃p1 · · ·bpi · · · pr+1. (The hat means “omit this
term.”) Therefore by induction, p−1
i a is a product of nonzero prime ideals, hence a is a
product of nonzero prime ideals by multiplying back by pi.
Uniqueness: Suppose p1 · · · pr = q1 · · · qs with nonzero primes pi and qj. To show r = s
and pi = qi after reindexing, we can cancel common prime ideals on both sides (Corollary
3.3) and thus may suppose pi ̸= qj for all i and j. Since p1 ⊃p1 · · · pr = q1 · · · qs, p1 is some
qj by Corollary 1.5. This is a contradiction.
□
Now we have a simpler proof of Corollary 3.5: if pb = b then p = (1) by writing b as a
product of primes and cancelling common prime factors on both sides.
4. Consequences
Using the existence of prime ideal factorizations and the invertibility of nonzero prime
ideals, we can extend some properties of nonzero prime ideals to other (integral or fractional)
ideals.

<!-- page 7 -->
IDEAL FACTORIZATION
7
Theorem 4.1. For every fractional ideal I in K, eI as in Deﬁnition 2.5 is an inverse for
I: I eI = OK.
Proof. If I = OK then eI = OK. Now suppose I = a is a nonzero proper ideal of OK. Then
we can write a = p1 · · · pr for some nonzero prime ideals pi and we already know piepi = OK.
For x ∈K,
x ∈ea ⇐⇒xa ⊂OK
⇐⇒(x)p1p2 · · · pr ⊂OK
⇐⇒(x)p2 · · · pr ⊂ep1
(multiply both sides by ep1)
...
⇐⇒(x) ⊂ep1ep2 · · ·epr
⇐⇒x ∈ep1ep2 · · ·epr.
Thus
ea = ep1ep2 · · ·epr.
Since pep = OK for every nonzero prime ideal p, we obtain aea = OK. If I is a fractional
ideal that is not an ideal of OK, let d be a common denominator of I: dI ⊂OK. Denote
dI as a, so I = (1/d)a. Then eI = {x ∈K : xI ⊂OK} = {x ∈K : (x/d)a ⊂OK} = dea, so
I eI = Idea = (1/d)adea = aea = OK.
□
From now on we write eI as I−1. That is,
I−1 = {x ∈K : xI ⊂OK}.
We deﬁne negative powers of I as positive powers of I−1 in the obvious way and the usual
rules of exponents (such as In1In2 = In1+n2) apply with arbitrary integral exponents.
Corollary 4.2. The fractional ideals in K form a commutative group under multiplication
that is freely generated by the nonzero prime ideals in OK.
Proof. Multiplication of OK-modules in K is commutative and associative, OK = (1) is the
identity, and the product of two fractional ideals is a fractional ideal (a product of ﬁnitely
generated OK-modules is ﬁnitely generated). We have just seen that fractional ideals have
fractional ideal inverses, so the fractional ideals are a multiplicative group. To show the
nonzero prime ideals generate the group, let I be a fractional ideal. For some d ∈OK −{0},
dI ⊂OK, so dI is a nonzero ideal in OK. Factor this into prime ideals: dI = p1 · · · pr. Since
dI = (d)I, we factor (d) into prime ideals, say as (d) = q1 · · · qs, and then obtain
I = (d)−1 · (d)I = q−1
1
· · · q−1
s p1 · · · pr.
Unique factorization says the nonzero prime ideals admit no nontrivial multiplicative rela-
tions, so they generate the group of fractional ideals freely.
□
Every fractional ideal can be written as a product
pa1
1 · · · par
r
with ai ∈Z, and by unique factorization this is an integral ideal (that is, an ideal in OK)
if and only if every exponent ai is nonnegative.
Now we can extend Corollaries 3.3, 3.4, and 3.5 to non-prime ideals in OK. The results
are collected into one theorem.

<!-- page 8 -->
8
KEITH CONRAD
Theorem 4.3. Let a be a nonzero ideal in OK.
(1) For nonzero ideals b and c in OK, ab = ac if and only if b = c.
(2) For each nonzero ideal b in OK, a ⊃b if and only if a | b as ideals.
(3) If a ̸= (1) then for each nonzero ideal b in OK, ab ⊂b with strict inclusion.
Proof. For (1), the direction (⇐) is trivial, and multiplication by a−1 settles (⇒).
For (2), (⇐) is trivial. For (⇒), let c = a−1b ⊂OK, so c is an ideal of OK and ac = b.
For (3), easily ab ⊂b. If ab = b then a = (1) by cancelling b.
□
Corollary 4.4. Every nonzero ideal in OK has a principal ideal multiple.
Proof. Let a be a nonzero ideal in OK. Pick α ̸= 0 in a. Then (α) ⊂a, so a | (α) by
Theorem 4.3. This says (α) is a multiple of a.
□
We can speak of the greatest common divisor and least common multiple of two nonzero
ideals in OK: gcd(a, b) is a common ideal divisor that all other common ideal divisors divide,
and lcm(a, b) is a common multiple that divides all other common multiples.
Corollary 4.5. For nonzero ideals a and b in OK, write a = Q
i pmi
i
and b = Q
i pni
i
with
the pi’s being distinct nonzero prime ideals. Then gcd(a, b) = a + b = Q
i pmin(mi,ni) and
lcm(a, b) = a ∩b = Q
i pmax(mi,ni)
i
. In particular, (a + b)(a ∩b) = ab.
Proof. Since Theorem 4.3 says divisibility among integral ideals is the same as containment,
the greatest common divisor of two integral ideals is the smallest ideal containing both of
them, which is their sum. The least common multiple of two integral ideals is the largest
ideal contained inside both ideals, which is their intersection. The prime factorization for-
mulas with exponents min(mi, ni) and max(mi, ni) also ﬁt the conditions to be the greatest
common divisor and least common multiple using unique prime ideal factorization.
Since max(mi, ni) + min(mi, ni) = mi + ni, (a + b)(a ∩b) = ab because the exponent of
each prime ideal on both sides is the same.
□
The formulas gcd(a, b) = a + b and lcm(a, b) = a ∩b permit the notion of gcd and lcm
to extend to the zero ideal: gcd(a, (0)) := a and lcm(a, (0)) := (0). We will have no use for
this.
Deﬁnition 4.6. When a and b are ideals in OK with a + b = (1), we say a and b are
relatively prime.
In OK, the conditions a + b = (1) and a ∩b = ab are equivalent, both expressing the fact
that a and b have no common ideal factors except the unit ideal. In a general commutative
ring, these conditions are not equivalent (e.g., in Z[T] we have (2) + (T) = (2, T) ̸= (1) but
(2) ∩(T) = (2T) = (2)(T)). However, the condition a + b = (1) does imply a ∩b = ab in all
commutative rings. Indeed, if a + b = (1) then
a ∩b = (a ∩b)(1) = (a ∩b)(a + b) = (a ∩b)a + (a ∩b)b ⊂ba + ab = ab,
and the reverse inclusion ab ⊂a ∩b is trivial, so a ∩b = ab.
Theorem 4.7. Let A be a commutative ring. If ideals a and b in A satisfy a+b = (1) then
A/ab ∼= A/a × A/b as rings.
Proof. Since a + b = (1), a ∩b = ab by the computation preceding the theorem.
Let f : A →A/a × A/b by f(x) = (x mod a, x mod b). This is a ring homomorphism.
The kernel is a ∩b = ab, so f induces an injective map f : A/ab →A/a × A/b. To show f

<!-- page 9 -->
IDEAL FACTORIZATION
9
is onto, write 1 = α + β for α ∈a and β ∈b. Then, for every pair (c1, c2) ∈A2, the element
x = c2α + c1β in A satisﬁes x ≡c1 mod a and x ≡c2 mod b.
□
Remark 4.8. Theorem 4.7 is called the Chinese remainder theorem. It extends by in-
duction from two ideals whose sum is (1) to every ﬁnite set of ideals that pairwise add to
the unit ideal. In terms of solving simultaneous congruences, if a1, . . . , ar are ideals with
ai + aj = (1) for i ̸= j, and c1, . . . , cr are in the ring, the congruences
x ≡c1 mod a1, . . . , x ≡cr mod ar
admit a common solution (uniquely modulo a1 · · · ar). The following corollary applies this
idea to strengthen Corollary 4.4.
Corollary 4.9. For all nonzero ideals a and b in OK, there is an ideal c such that ac is
principal and c is relatively prime to b.
This becomes Corollary 4.4 when b = (1): all ideals in OK are relatively prime to (1).
Proof. Write a = pe1
1 · · · per
r and b = pf1
1 · · · pfr
r , with ei, fi ≥0. (The exponents fi will play
no role in what follows. What really matters is that the pi’s denote the primes showing
up in either a or b; only their multiplicities in a will matter.) By Corollary 3.5, pei+1
i
is
a proper subset of pei
i . Pick yi ∈pei
i −pei+1, so yi ≡0 mod pei
i
and yi ̸≡0 mod pei+1
i
. (If
ei = 0 this just means yi ∈OK −pi.) Use Theorem 4.7 to choose x ≡yi mod pei+1
i
for all
i. Then for all i, x ≡0 mod pei
i and x ̸≡0 mod pei+1
i
, so pei
i divides (x) and pei+1
i
does not
divide (x). Thus (x) has the same prime-ideal divisibility as a at each pi, and since the pi
are all the prime ideal factors of a or b, (x) and ab have greatest common divisor a. Writing
(x) = ac, the ideal c is not divisible by some pi since (x) and a are divisible by the same
power of each pi. Thus c is relatively prime to b.
□
Remark 4.10. Let’s isolate a result we obtained in the proof of Corollary 4.9: given a
set of prime ideal powers pei
i
in OK (the pi’s are distinct) there is an x ∈OK such that
(x) is divisible by pei
i
but not pei+1
i
for all i. This says we can construct a principal ideal
(x) divisible by a preselected (ﬁnite) set of primes to preselected multiplicities, including
multiplicity 0. However, in this construction we have no control over which other prime
ideals may occur in (x). Usually (x) will be divisible by primes besides the pi’s.
Theorem 4.11. Each nonzero ideal a in OK has at most 2 generators and one of them can
be chosen arbitrarily in a −{0}: for each α ∈a −{0} there is β ∈a such that a = (α, β).
Proof. We can assume a ̸= (1) (otherwise use β = 1). Pick nonzero α in a. Then (α) ⊂a,
so a | (α) by Theorem 4.3(2). Write the prime ideal factorization of (α) as (α) = pe1
1 · · · per
r
with r ≥1 and all ei ≥1. Then a = pa1
1 · · · par
r
with 0 ≤ai ≤ei for all i. From Remark
4.10, there is β ∈OK such that, for all i, (β) is divisible by pai
i
and not by pai+1
i
. Then
(β) = pa1
1 · · · par
r b = ab where b is not divisible by each pi. Therefore (α, β) = (α) + (β) =
gcd((α), (β)). From the prime ideal factorizations of (α) and (β), their gcd is pa1
1 · · · par
r = a,
so a = (α, β).
□
Theorem 4.12. The ring OK is a unique factorization domain if and only if it is a principal
ideal domain.
Proof. It is a general theorem of algebra that every PID is a UFD. We now show that if OK
is a UFD then it is a PID. It suﬃces to show when OK is a UFD that every prime ideal is
principal, since every nonzero ideal is a product of prime ideals.

<!-- page 10 -->
10
KEITH CONRAD
For each irreducible π in a UFD, the ideal (π) is prime (check!). Now we will show if OK
is a UFD that every nonzero prime ideal p in OK is (π) for some irreducible π. Pick α ∈p
with α ̸= 0. Since (α) ⊂p, p divides (α).
By hypothesis, α has an irreducible factorization in OK. Write α = π1 · · · πr, where the
πi’s are irreducible in OK. Then (α) = (π1) · · · (πr). Each of the ideals (πi) is prime, and
p | (α), so by unique prime ideal factorization in OK we must have p = (πi) for some i.
Thus all prime ideals are principal, so OK is a PID.
□
For general domains, a UFD need not be a PID: Z[T] is an example.
5. Analogues in F[X]
Many properties of Z can be carried over to F[X], where F is a ﬁeld. Both Z and F[X]
have division with remainder, and thus are PIDs. The table below indicates some further
similarities. In particular, the units of F[X] are the nonzero constants F ×, so while Z has
only ﬁnitely many units, F[X] has ﬁnitely many units only when F is a ﬁnite ﬁeld. This is
a small indication that analogies between Z and F[X] are strongest when F is ﬁnite, but
here we allow arbitrary F (such as Q or R, not just ﬁnite ﬁelds).
Z
F[X]
Prime
Irreducible
±1
F ×
Positive
Monic
Q
F(X)
We want to adapt the methods from number ﬁelds to the “function ﬁeld” case: if K is a
ﬁnite extension of F(X), does the integral closure of F[X] in K have unique factorization
of ideals?
Example 5.1. In the ﬁeld C(X,
√
X3 −1), the integral closure of C[X] is C[X,
√
X3 −1].
A key idea running through the proofs in the previous two sections was induction on the
index of nonzero ideals in a ring of integers. We can’t directly use this idea for the integral
closure of F[X], since ideals in F[X] don’t have ﬁnite index if F is an inﬁnite ﬁeld. For
example, representatives in Q[X]/(X3 −2) are a + bX + cX2 with rational a, b, c, and there
are inﬁnitely many of these. However, there is something ﬁnite about this example: it is
ﬁnite-dimensional over Q with dimension 3. More generally, if f(X) has degree d ≥0 in
F[X] then F[X]/(f) has dimension d as an F-vector space (with basis 1, X, X2, . . . , Xd−1).
So if we count dimension over F rather than count index in F[X], then F[X]/(f) has a
ﬁniteness property we can take advantage of.1
Let K/F(X) be a ﬁnite separable extension of degree n and let A be the integral closure
of F[X] in K. This is an analogue of the ring of integers of a number ﬁeld. For α ∈A,
TrK/F(X)(α) and NK/F(X)(α) are in F[X]. More generally, the characteristic polynomial of
α is in F[X][T].
Theorem 5.2. With notation as above, A is a ﬁnite free F[X]-module of rank n, every
nonzero ideal a in A is a ﬁnite free F[X]-module of rank n, and A/a is ﬁnite-dimensional
over F.
1Don’t confuse F[X] with Z[X]. Quotient rings Z[X]/(f) with f ̸= 0 need not be ﬁnite free Z-modules:
Z[X]/(2X −1) ∼= Z[1/2] has no Z-basis.

<!-- page 11 -->
IDEAL FACTORIZATION
11
Proof. The proof that a ring of integers is a ﬁnite free Z-module uses the nonvanishing of
discriminants and the fact that Z is a PID. Because K/F(X) is separable, the discriminant
of every F(X)-basis of K is nonzero.
Since F[X], like Z, is a PID, the proof that a
ring of integers is a ﬁnite free Z-module carries over to show A is a ﬁnite free F[X]-
module. Speciﬁcally, there is an F(X)-basis of K that is inside A, say e1, . . . , en, and then
Ln
i=1 F[X]ei ⊂A ⊂Ln
i=1 F[X]ei/d where d = discK/F(X)(e1, . . . , en) ∈F[X]. Since A is
in between two free F[X]-modules of rank n, it too is free of rank n.
Now let a be a nonzero ideal in A. Pick α ∈a with α ̸= 0, so (α) ⊂a. The ideal
(α) is ﬁnite free as an F[X]-module with rank n: letting γ1, . . . , γn be an F[X]-basis of A,
αγ1, . . . , αγn is an F[X]-basis of αA. Therefore a lies between two ﬁnite free F[X]-modules
of rank n, so it also is ﬁnite free of rank n as an F[X]-module.
From the structure of ﬁnitely generated modules over a PID, there is an F[X]-basis
y1, . . . , yn of A and nonzero f1, . . . , fn in F[X] such that f1y1, . . . , fnyn is an F[X]-basis of
a, so
A/a = (
n
M
i=1
F[X]yi)/(
n
M
i=1
F[X]fiyi) ∼=
n
M
i=1
(F[X]/(fi))yi.
Each F[X]/(fi) has ﬁnite dimension over F and there are ﬁnitely many of these, so A/a is
ﬁnite-dimensional over F.
□
Corollary 5.3. Every nonzero prime ideal in A is a maximal ideal.
Proof. For every nonzero prime ideal p of A, A/p is a domain that is ﬁnite-dimensional over
F. A domain that is ﬁnite-dimensional over a ﬁeld is itself a ﬁeld, so p is maximal.
□
Deﬁne a fractional A-ideal I to be a nonzero A-module in K with a common denominator:
aI ⊂A for some a ∈A−{0}. All the theorems in Section 2 carry over to fractional A-ideals
in K.
For instance, fractional A-ideals are precisely the nonzero ﬁnitely generated A-
modules in K and each is a free F[X]-module of rank n = [K : F(X)]. The proof of Lemma
3.1 carries over to show every nonzero ideal in A contains a product of prime ideals: in the
inductive step, instead of saying one ideal containing another has smaller index as in the
number ﬁeld case we now say that if a ⊂a′ ⊂A with a ̸= a′ then dimF (A/a′) < dimF (A/a),
so the F-dimension (rather than the index) is smaller.
The proofs of Corollaries 3.3 and 3.4 go through for A with no change at all. In the proof
of Corollary 3.5, replace the ﬁniteness of the index of the ideal b in the ring of integers
with the ﬁniteness of dimF (A/b). Finally, Theorem 3.6 about unique factorization of ideals
carries over to A with no new ideas required. Every result in Section 4 applies to A by
the same proofs (e.g., in A containment of ideals is the same as divisibility). The only
change needed is in the analogue of Theorem 4.12, where the proof that every nonzero
nonunit α ∈A is a product of irreducible elements in A should proceed by induction on
deg(NK/F(X)(α)).
Example 5.4. The ring C[X,
√
X3 −1] has unique factorization of ideals.
There is one minor blemish in our treatment here: it was assumed from the outset that
the ﬁnite extension K/F(X) is separable. The reason for this assumption is that without it
discriminants vanish (since the trace map TrK/F(X) is identically 0), so our proof that the
integral closure of A in F[X] is a free F[X]-module breaks down. This doesn’t mean A can’t
have unique factorization of ideals, but our method of proof certainly doesn’t work anymore.

<!-- page 12 -->
12
KEITH CONRAD
Is there a counterexample to unique factorization of ideals if K/F(X) is inseparable? We
will ﬁnd out in the next section.
6. Unique factorization of ideals by commutative algebra
Our proof of unique factorization of ideals relied on the ﬁniteness of OK/a in the number
ﬁeld case and the ﬁniteness of dimF (A/a) in the function ﬁeld case. Using some concepts
from commutative algebra allows for another approach to unique factorization of ideals that
is applicable more broadly. Proofs in this section are only sketched.
Deﬁnition 6.1. Let A be a commutative ring. An A-module is called Noetherian if all of
its submodules are ﬁnitely generated. We call A a Noetherian ring if it is Noetherian as an
A-module, i.e., all the ideals of A are ﬁnitely generated.
The Noetherian property for modules is preserved under many constructions. For in-
stance, submodules and quotient modules of a Noetherian module are Noetherian, and a
ﬁnite direct sum of Noetherian modules is Noetherian. (These are derived from the follow-
ing general fact: if M is an A-module and N ⊂M is a submodule, then M is a Noetherian
A-module if and only if N and M/N are Noetherian A-modules.)
A PID is a Noetherian ring, since all ideals in a PID are singly generated, but Noetherian
rings are stable under many more ring-theoretic constructions than PIDs. For instance,
if A is Noetherian then so are A[T] and A/a for every ideal a. Thus Z[T1, . . . , Tn] and
F[T1, . . . , Tn] for a ﬁeld F are Noetherian rings for all n ≥1: all ideals in these rings are
ﬁnitely generated. By comparison, if A is a PID then A[T] is never a PID (unless A is a
ﬁeld), although A[T] is Noetherian.
In a number ﬁeld K, the ideals in OK are ﬁnitely generated Z-modules, and thus are
ﬁnitely generated OK-modules. Therefore OK is a Noetherian ring. Similarly, the integral
closure of F[X] in a ﬁnite separable extension of F(X) is a Noetherian ring.
Here is the analogue of Lemma 3.1 for Noetherian domains.
Lemma 6.2. In a Noetherian domain that is not a ﬁeld, every nonzero proper ideal contains
a product of nonzero prime ideals.
Proof. See [6, p. 626].
□
The proof of Lemma 6.2 is like that of Lemma 3.1, except studying a counterexample
with least index is replaced by “Noetherian induction,” which is a standard technique that
will be found in textbooks that discuss Noetherian modules. Noetherian induction can also
be used to prove that in a Noetherian domain every nonzero nonunit can be written as a
product of irreducible elements (usually not uniquely).
Deﬁnition 6.3. An integral domain is called a Dedekind domain if it has the following
properties:
(1) Noetherian,
(2) integrally closed,
(3) all of its nonzero prime ideals are maximal.
The ring of integers in a number ﬁeld is an example of a Dedekind domain.
So is
C[x, y]/(f) for an irreducible polynomial f such that the curve f(x, y) = 0 in C2 is smooth
[7, p. 56]. (Smooth means there is no solution in C2 to f(x, y) = 0 where both partial
derivatives of f vanish.) The ring Z[X] is not Dedekind, since (X) is a nonzero prime ideal

<!-- page 13 -->
IDEAL FACTORIZATION
13
in Z[X] that is not maximal. Historically, the ring of integers of a number ﬁeld and the
ring of polynomial functions on a smooth plane curve were the ﬁrst important examples of
Dedekind domains.
Every PID is both a UFD and a Dedekind domain, and the converse turns out to be true
too: a ring that is a UFD and a Dedekind domain is a PID.
Remark 6.4. A ﬁeld ﬁts the conditions to be a Dedekind domain: the third property holds
vacuously, since there aren’t nonzero prime ideals at all. To say UFDs ∩Dedekind domains
= PIDs, we need ﬁelds to be Dedekind domains since ﬁelds are PIDs and a UFDs (boring
ones, of course). On the other hand, for technical reasons related to algebraic geometry
it it better to regard ﬁelds as not being Dedekind domains. That is, a Dedekind domain
should have at least one nonzero prime ideal. At the level of our treatment here, whether
you want to say a ﬁeld is a Dedekind domain or not has only minor eﬀects on the validity
of theorems about Dedekind domains, so we won’t stress this point.
Deﬁnition 6.5. In a domain A, a fractional A-ideal is a nonzero A-module I in the fraction
ﬁeld of A that admits a common denominator: dI ⊂A for some d ∈A −{0}.
Theorem 6.6. If A is a Dedekind domain then every nonzero prime ideal p ⊂A is invertible
as an A-module. The inverse is the A-module ep consisting of x in the fraction ﬁeld of A
such that xp ⊂A, and ep is a fractional A-ideal.
Proof. The proof is essentially like that of Theorem 3.2 (using Lemma 6.2 in place of Lemma
3.1). This is left to the reader to check; each property in the deﬁnition of a Dedekind domain
is needed in the proof. (The Noetherian property was used in Lemma 6.2.)
□
Theorem 6.7. In a Dedekind domain A, each nonzero proper ideal has unique factorization
as a product of nonzero prime ideals. The fractional A-ideals are a commutative group under
A-module multiplication and is freely generated by the nonzero prime ideals of A.
Proof. The existence of a prime ideal factorization follows from Lemma 6.2 and Theorem
6.6 in the same way Theorem 3.6 follows from Lemma 3.1 and Theorem 3.2. The uniqueness
of prime ideal factorization follows from Theorem 6.6 by exactly the same argument we gave
earlier in the number ﬁeld setting. In a Dedekind domain, if p ⊃p1 · · · pr then p = pi for
some i by the same proof as Corollary 1.5.
□
Theorem 6.8. The integral closure of a Dedekind domain in a ﬁnite extension of its fraction
ﬁeld is also Dedekind.
Proof. See [6, pp. 633-634]. Notice we do not need to assume the ﬁeld extension is separable!
The proof treats ﬁrst the case of a separable extension (very much like the number ﬁeld
setting), then a purely inseparable extension (using special features of characteristic p),
and then the general case by writing a ﬁnite extension as a tower of a purely inseparable
extension on top of a separable extension.
□
Theorem 6.8 with base ring Z shows OK is Dedekind for a number ﬁeld K and therefore
OK has unique factorization of ideals by Theorem 6.7.
Theorem 6.8 is often proved in textbooks only in the case when the ﬁeld extension is
separable (or, even more simply, has characteristic 0). What is special about the separable
case is that the trace-pairing and discriminants are available. Moreover, in the case of a
separable extension one can prove a little more than Theorem 6.8: the integral closure of
the initial Dedekind domain A is a ﬁnitely generated A-module. This simpliﬁes the proof

<!-- page 14 -->
14
KEITH CONRAD
of Theorem 6.8. When the extension is not separable, the integral closure of A may not be
ﬁnitely generated as an A-module [2, exer. 3, p. 461].
We introduced Dedekind domains in Deﬁnition 6.3 by three technical properties. These
rings can be characterized in many other ways, such as the following.
Theorem 6.9. The following conditions on a domain A are equivalent:
(1) A is Dedekind,
(2) every nonzero proper ideal in A is a product of prime ideals,
(3) every nonzero proper ideal in A is a unique product of prime ideals,
(4) every nonzero ideal in A is invertible as a fractional A-ideal,
(5) every nonzero ideal in A is a projective A-module,
(6) A is Noetherian and the localization Ap is a PID for all nonzero prime ideals p.
Proof. See [5, pp. 765–767].
□
Remark 6.10. Another list of properties equivalent to being Dedekind is: Noetherian,
integrally closed, and (a + b)(a ∩b) = ab for all ideals a and b.
The integral closure of a UFD in a ﬁnite extension of its fraction ﬁeld might not be a
UFD, and if A is Dedekind then A[T] is not Dedekind (unless A is a ﬁeld and you consider
ﬁelds to be Dedekind domains). There is a class of domains that includes Dedekind domains
and UFDs as special cases and is preserved under both integral closure in a ﬁnite extension
of the fraction ﬁeld and under A ⇝A[T]: Krull rings. A discussion of Krull rings is in
[2, Chap. VII, Sect. 1] and [8, Sect. 12]. They are also the main object of study in [1,
Chap. 3], where they are called “rings with a theory of divisors.” Using terminology from
commutative algebra, Dedekind domains are the 1-dimensional Krull rings (this excludes
ﬁelds) and UFDs are the Krull rings with trivial class group.
7. Ideal Norms
We return to the setting of a number ﬁeld K and use the ﬁnite index of ideals to develop
analogues for OK of concepts from elementary number theory.
Deﬁnition 7.1. For a nonzero ideal a in OK, its (ideal) norm is Na = |OK/a| = [OK : a].
On principal ideals this notion of norm is compatible with the ring-theoretic norm on a
generator:
Theorem 7.2. For α ∈OK −{0}, N((α)) = | NK/Q(α)|.
Proof. From the structure of modules over a PID, there is a Z-basis e1, . . . , en of OK and
nonzero integers a1, . . . , an such that a1e1, . . . , anen is a Z-basis of the ideal (α). Then
OK/(α) ∼= Ln
i=1(Z/aiZ)ei, so N((α)) = Qn
i=1 |ai| = |a1 · · · an|.
Next we compute NK/Q(α) in a clever way and will get the same value as N((α)), up to
sign. The ﬁeld K has three Q-bases: {ei}, {aiei}, and {αei}. Consider the commutative
diagram of Q-linear maps
(7.1)
K
ei7→ei

mα
/ K
K
ei7→aiei
/ K
aiei7→αei
O

<!-- page 15 -->
IDEAL FACTORIZATION
15
where the map along the top is multiplication by α and the maps along the sides and bottom
interchange Q-bases of K as indicated. (The map on the left is the identity.) That the
diagram commutes follows by examining the eﬀect on each ei both ways: on the top it goes
to αei and the other way the eﬀect on it is ei 7→ei 7→aiei 7→αei, which is exactly what
mα does to ei. So by linearity the two ways around the diagram are the same.
Since all maps are from K to K we can speak about their determinants, and the determi-
nant along the top is the product of the other three determinants. The determinant along
the top is NK/Q(α), by deﬁnition. The determinant on the left is 1. The matrix representing
the linear map on the bottom is diagonal with ai’s on the main diagonal, so its determinant
is a1 · · · an. What about the determinant on the right? It is not clear what a matrix for
it is, so how can we compute the determinant? The key point is that {a1e1, . . . , anen} and
{αe1, . . . , αen} are not just Q-bases of K but Z-bases of a common free Z-module (the ideal
(α)). As bases of a ﬁnite free Z-module, changing from one basis to the other is a linear
map whose determinant is invertible over Z, hence the determinant is ±1.
Putting it all together, det(mα) = ±a1 · · · an, so | NK/Q(α)| = |a1 · · · an| = N((α)).
□
Example 7.3. The size of Z[
√
2]/(4 + 7
√
2) is |16 −2 · 49| = 82.
See [4, pp. 185–186] for a modiﬁed deﬁnition of the ideal norm that can take negative
values so a nonzero principal ideal (α) has ideal norm NK/Q(α), even with the correct sign.
Since the ring OK/a has size Na, Na ≡0 mod a. Containment implies divisibility, so
a | (Na) as ideals. This is analogous to the elementwise divisibility relation α | NK/Q(α) for
α ∈OK.
The following two theorems are the main properties of norms of ideals in OK.
Theorem 7.4. The norm of a nonzero prime ideal p is a prime power in Z+. If Np = pf
then p | (p).
Proof. Let p be a nonzero prime ideal in OK. The ring OK/p is a ﬁnite ﬁeld, so from the
theory of ﬁnite ﬁelds it has prime power size. Hence Np is a prime power in Z+.
Let p be the characteristic of OK/p, so p = 0 in OK/p. That means p ∈p, so (p) ⊂p, so
p | (p).
□
We call OK/p the residue ﬁeld at p. The number f in Theorem 7.4 can be interpreted as
dimZ/pZ(OK/p) and therefore is called the residue ﬁeld degree.
Theorem 7.5. For nonzero ideals a and b in OK, N(ab) = Na Nb.
Proof. We give two proofs.
First proof: Since every nonzero ideal is a product of prime ideals it suﬃces to show
N(ap) = Na Np for nonzero a and nonzero prime p.
Since OK ⊃a ⊃ap, [a : ap] = N(ap)/ Na and what we want is equivalent to |a/ap| =
|OK/p|.
The OK-module a/ap is killed by multiplication by elements of p, so a/ap is
naturally an (OK/p)-vector space. That’s the key point. We will show a/ap is 1-dimensional
over OK/p, so its size is |OK/p|.
Since ap is a proper subset of a, there is an x ∈a with x ̸∈ap, so x ̸= 0 in a/ap.
We expect, if a/ap is to be 1-dimensional over OK/p, that each nonzero element of a/ap
is a spanning set over OK/p. Let’s verify {x} is such a set. Since (x) ⊂a and (x) ̸⊂ap,
a divides (x) but ap does not divide (x) (containment is equivalent to divisibility). This
implies gcd((x), ap) = a, so a = (x) + ap by Corollary 4.5. So for each α ∈a we have
α = βx + γ where β ∈OK and γ ∈ap. Thus in a/ap, α = β · x, which shows a/ap is

<!-- page 16 -->
16
KEITH CONRAD
spanned as an (OK/p)-vector space by the single nonzero element x: the dimension of a/ap
over OK/p is 1. Hence N(ap) = Na Np.
Second proof: We will show a/ab ∼= OK/b as OK-modules, so [a : ab] = Nb, which
implies N(ab) = [OK : ab] = [OK : a][a : ab] = Na Nb. By Corollary 4.9, there is a c
prime to b such that ac is principal. Let ac = (x). Then (x) + ab = a(c + b) = a(1) = a.
Reducing the equation (x) + ab = a modulo ab shows a/ab is spanned by x as an OK-
module. Therefore the map f : OK →a/ab given by α 7→αx = αx is OK-linear, onto and
its kernel is {α ∈OK : αx ∈ab}. Since
αx ∈ab ⇐⇒(α)(x) ⊂ab
⇐⇒(α)ac ⊂ab
⇐⇒(α)c ⊂b,
for α in the kernel of f we have
(α) = (α)(1) = (α)(c + b) = (α)c + (α)b ⊂b + b = b,
so α ∈b. Hence ker f ⊂b. The reverse inclusion is easy since for y ∈b, yx ∈ab because
x ∈a.
□
Remark 7.6. In a domain where all nonzero ideals have ﬁnite index, the multiplicativity
of the ideal norm (if true) implies unique factorization of ideals. See [3].
Corollary 7.7. Let a be an ideal in OK and p be a prime number. The ideal a is divisible
by a prime factor of (p) if and only if Na is divisible by p.
Proof. Write a = pa1
1 · · · par
r
with distinct pi’s. Some pi is a factor of (p) if and only if Npi
is a power of p. Since Na is the product of Npai
i , p | Na if and only if some pi has norm a
power of p, which is equivalent to pi | (p).
□
When K/Q is Galois, with G = Gal(K/Q), the group G acts on the ideals in OK by the
natural rule σ(a) = {σ(α) : α ∈a}, which is an ideal of OK. This could be considered a
generalization of the Galois action on elements because of how it behaves on principal ideals:
σ((α)) = (σ(α)) (check!). The action of Galois groups on ideals has some aspects that are
diﬀerent from their eﬀect on elements: an element of OK ﬁxed by G is in Z, but an ideal of
OK ﬁxed by G need not come from Z, e.g., in Z[i], (1 + i) = (1 −i) = (1 + i) and (1 + i)
has no generator in Z, and in Z[√−5], (2, 1 + √−5) = (2, 1 −√−5) = (2, 1 + √−5), but
(2, 1+√−5) has no generating set in Z. Some aspects of the Galois action on elements and
ideals are similar. For example, each σ ∈G deﬁnes a ring isomorphism OK/a →OK/σ(a)
by the natural rule α mod a 7→σ(α) mod σ(a) (why is this well-deﬁned?), so these rings
have the same size: N(σ(a)) = Na, which resembles the formula NK/Q(σ(α)) = N(α) for
elements α ∈K. The following theorem presents a result similar to the element formula
(7.2)
NK/Q(α) =
Y
σ∈G
σ(α).
Theorem 7.8. For a Galois extension K/Q with Galois group G and nonzero ideal a in
OK, Q
σ∈G σ(a) = (Na)OK.
The ideal on the right side is not (Na)Z, since a product of ideals in OK can’t become
an ideal in Z. Therefore the formula in this theorem is the best2 ideal-theoretic analogue
of (7.2).
2Perhaps “most ideal”?

<!-- page 17 -->
IDEAL FACTORIZATION
17
Proof. By unique factorization, both sides of the desired equation
(7.3)
Y
σ∈G
σ(a) ?= (Na)OK
are equal if (and only if) a common power of both sides are equal. Let h be the class number
of K, so ah = (α) for some α ∈OK. We will check the h-th power of both sides are equal
since that reduces the whole task to the case of principal ideals.
It is straightforward to check G acts multiplicatively on ideals: σ(ab) = σ(a)σ(b) for all
ideals a and b. Since σ(xOK) = σ(x)OK, σ(a)h = σ(ah) = σ((α)) = (σ(α)). Therefore
(7.4)
 Y
σ∈G
σ(a)
!h
=
Y
σ∈G
σ(ah) =
Y
σ∈G
σ(αOK) =
Y
σ∈G
(σ(α)OK) = NK/Q(α)OK
since NK/Q(α) = Q
σ∈G σ(α).
On the right side of (7.3) the hth power is ((Na)OK)h = N(ah)OK = N((α))OK since the
ideal norm is multiplicative (Theorem 7.5). We have N((α)) = | NK/Q(α)| by Theorem 7.2,
so N((α))OK = | NK/Q(α)|OK = NK/Q(α)OK, which matches (7.4).
□
Example 7.9. In Z[√−5], let a = (1 + 2√−5, 4 + √−5). Here the Galois group is the
identity and complex conjugation, so
aa = (1 + 2
√
−5, 4 +
√
−5)(1 −2
√
−5, 4 −
√
−5)
= (21, 14 + 7
√
−5, 14 −7
√
−5, 21)
= 7(3, 2 +
√
−5, 2 −
√
−5)
= 7OK
since (3, 2 + √−5, 2 −√−5) contains 3 and 2 + √−5 + 2 −√−5 = 4. Thus (Na)OK = 7OK,
so Na = 7u where u ∈O×
K. Both Na and 7 are in Z+, so u = 1 and a has norm 7.
By manipulating generators, (1 + 2√−5, 4 + √−5) = (7, 3 −√−5) (check generators on
each side are in the ideal on the other side). Let’s compute the norm of a using these new
generators:
aa = (7, 3 −
√
−5)(7, 3 +
√
−5)
= (49, 21 + 7
√
−5, 21 −7
√
−5, 14)
= 7(7, 3 +
√
−5, 3 −
√
−5)
= 7OK
since the ideal contains 7 and 3 + √−5 + 3 −√−5 = 6.
Returning to the general case, where K/Q need not be Galois, the next theorem general-
izes Theorem 7.2 from principal ideals to all (nonzero) ideals in OK by describing the norm
of an ideal using the ring-theoretic norms of the elements in the ideal.
Theorem 7.10. Let a be a nonzero ideal in OK. The positive integer Na is the greatest
common divisor of the integers NK/Q(α) for all α ∈a.
The gcd here is being taken over norms of all elements of a, not just norms of a set
generators of the ideal: while N((α)) = | NK/Q(α)|, for an ideal described with more than
one generator, say a = (α, β), Na need not be the gcd of NK/Q(α) and NK/Q(β). In Example

<!-- page 18 -->
18
KEITH CONRAD
7.9, where a = (1 + 2√−5, 4 + √−5), 1 + 2√−5 and 4 + √−5 have norm 21 but Na is 7.
More simply, in Z[i] the ideal (1 + 2i, 1 −2i) is (1) so it has norm 1, but the Gaussian
integers 1 + 2i and 1 −2i have norm 5.
Proof. If a = (1) then the result is clear, so we take a ̸= (1).
Let d be the gcd of all NK/Q(α) as α runs over a.
For nonzero α ∈a, a | (α) so
Na | N((α)), so Na | NK/Q(α) by Theorem 7.2. Therefore Na | d, so each prime power
dividing Na also divides d. To show Na = d we will show for every prime number p that the
highest power of p dividing Na is also the highest power of p dividing NK/Q(α) for some
α ∈a (depending on p). Since d | NK/Q(α), it follows that the highest power of p dividing
Na and d agree (why?). Varying this over all primes implies Na = d.
In OK, let (p) = pe1
1 · · · per
r with distinct prime ideals pi and ei ≥1. Write a = pc1
1 · · · pcr
r b
where ci ≥0 and b is not divisible by the ideals pi. Since the pi’s are all the prime ideals
dividing (p), Nb is not divisible by p. Writing Npi = pfi, Na = pc1f1+···+crfr Nb, so the
multiplicity (i.e., exponent) of p in Na is c1f1 + · · · + crfr. We need to ﬁnd α ∈a such that
NK/Q(α) has the same p-power divisibility.
By Remark 4.10, there is an α ∈OK −{0} such that (α) is divisible by pci
i but not pci+1
i
for all i and is also divisible by b. It follows that (α) is divisible by a, so α ∈a, and also
N((α)) = | NK/Q(α)| is divisible by p with multiplicity P cifi.
□
Remark 7.11. Theorem 7.10 is not an algorithmic formula for computing the norm of an
ideal, since it doesn’t provide a ﬁnite list of elements in the ideal and calculations to make
on them that would compute that norm. If you are given an actual nonzero ideal a in an
actual ring of integers OK and you can compute bases for OK and a as Z-modules, then
the absolute value of the determinant of the matrix expressing a Z-basis of a in terms of a
Z-basis of OK is the index [OK : a], so this is Na.
Since the ideal norm is multiplicative, it extends to a multiplicative function on all
fractional ideals of K in a unique way: if I is a fractional ideal, then I = ab−1 for some
nonzero ideals a and b and we set N(I) := N(a)/ N(b) ∈Q×, which is independent of the
choice of ideals a and b. There is not a combinatorial meaning of the rational number N(I)
(but see Theorem 7.12). When I is a principal fractional ideal, N(I) coincides with the
absolute value of the norm of any generator of I: N(xOK) = | NK/Q(x)| for all x ∈K×.
This is proved by writing x = y/z for y and z in OK −{0}, so (x) = (y)(z)−1 and now apply
the ideal norm to both sides and use Theorem 7.2.
Theorem 7.12. For fractional ideals J ⊂I, [I : J] = N(J)/ N(I).
Proof. Pick d ∈OK −{0} such that dI and dJ are both in OK. Then dJ ⊂dI ⊂OK, and
I/J ∼= dI/dJ as OK-modules, so
[I : J] = [dI : dJ] = [OK : dJ]
[OK : dI] = N(dJ)
N(dI) = N((d)) N(J)
N((d)) N(I) = N(J)
N(I) .
□
Example 7.13. For each nonzero ideal a ⊂OK, we have OK ⊂a−1 so [a−1 : OK] =
N(OK)/ N(a−1) = 1/(1/ Na) = Na = [OK : a]. More generally, if J ⊂I are fractional ideals
then Theorem 7.12 shows [I : J] = [IM : JM] for every fractional ideal M.
Theorem 7.14. For fractional ideals J ⊂I, I/J ∼= OK/JI−1 as OK-modules.
Proof. Choose d ∈OK −{0} such that dI ⊂OK. Then dJ ⊂dI ⊂OK. Set a = dI and
b = JI−1, which are nonzero ideals in OK. Then multiplication by d gives us an OK-module

<!-- page 19 -->
IDEAL FACTORIZATION
19
isomorphism
I/J ∼= dI/dJ = dI/dIJI−1 = a/ab.
By the second proof of Theorem 7.5, a/ab ∼= OK/b as OK-modules, so I/J ∼= OK/b =
OK/JI−1 as OK-modules.
□
Example 7.15. When a is a nonzero ideal in OK, a−1/OK ∼= OK/a as OK-modules.
Using the notation of the proof of Theorem 7.14, [I : J] = |I/J| = |OK/JI−1| = |OK/b| =
N(b) and N(b) = N(JI−1) = N(J)/ N(I) by multiplicativity of the ideal norm on fractional
ideals. This gives us another proof of Theorem 7.12.
Using the ideal norm, especially its multiplicativity, many concepts from elementary
number theory for Z can be carried over to OK. For example, since OK/p is a ﬁeld of size
Np, we have an analogue of Fermat’s little theorem:
α ̸≡0 mod p =⇒αNp−1 ≡1 mod p.
Deﬁne ϕK(a) = |(OK/a)×|, which generalizes the Euler function ϕ(m) = |(Z/mZ)×|. The
standard formula
ϕ(m) = m
Y
p|m

1 −1
p

.
for the classical ϕ-function has an OK-analogue:
ϕK(a) = Na
Y
p|a

1 −1
Np

,
where the product runs over the prime ideals dividing a. The proof is left to the reader.
There is an important diﬀerence between the groups (Z/mZ)× and (OK/a)×. When
m = pk is an odd prime power the group (Z/pkZ)× is cyclic for all k ≥1.
However,
when a = pk is a prime power ideal and k > 1, the group (OK/pk)× is often not cyclic.
For example, 3 is prime in Z[i] and (Z[i]/3k)× is not cyclic when k > 1. (When k = 1,
(OK/pk)× = (OK/p)× is cyclic since this is the multiplicative group of a ﬁnite ﬁeld.)
In a diﬀerent direction, the Riemann zeta-function
ζ(s) =
X
n≥1
1
ns =
Y
p
1
1 −1/ps
generalizes to the zeta-function of K:
ζK(s) =
X
a
1
Nas =
Y
p
1
1 −1/ Nps ,
where the series runs over nonzero ideals of OK and the product runs over the nonzero prime
ideals. The series and product are absolutely convergent for Re(s) > 1. Unlike in Z+, some
positive integers may not be the norm of an ideal in OK and other positive integers may be
the norm of more than one ideal in OK. For example, the expansion of ζQ(i)(s) as a series
for Re(s) > 1 is
1 + 1
2s + 1
4s + 2
5s + 1
8s + 1
9s + 2
10s + · · · + 4
65s + · · · ,
where there is no term with 1/3s since no ideal in Z[i] has norm 3 and the term with 1/5s
has coeﬃcient 2 since there are two ideals in Z[i] with norm 5. The equality of the series
and product for ζK(s) comes from unique factorization of ideals and the multiplicativity of

<!-- page 20 -->
20
KEITH CONRAD
the ideal norm. The study of distribution of prime numbers involves analytic properties of
ζ(s), and similarly studying the distribution of prime ideals of OK uses analytic properties
of ζK(s). There is an analytic continuation of ζK(s) to the whole complex plane except for
a simple pole at s = 1, just like ζ(s).
8. Analogues for Orders
Let K be a number ﬁeld and O be an order in K. That is, O is a subring of K that is
ﬁnitely generated as a Z-module and contains a Q-basis of K. Concretely, orders in K are
the subrings of OK with ﬁnite index. A typical example is Z[α] where α is an algebraic
integer of K such that K = Q(α) and Z + a where a is a nonzero ideal in OK. Are the
arguments we developed to prove unique factorization of ideals in OK valid if we apply them
to an order O when O ̸= OK?
To start oﬀ, note that orders in K share several features with OK:
(1) each order in K has fraction ﬁeld K,
(2) each order has a Z-basis and that basis can be chosen to include 1,
(3) all nonzero ideals in an order are ﬁnitely generated as Z-modules (even free with
rank n = [K : Q]),
(4) all nonzero ideals in an order have ﬁnite index in the order,
(5) all nonzero prime ideals in an order are maximal,
(6) for x ̸= 0 in an order O, the index [O : xO] equals | NK/Q(x)|,
(7) for each x in an order O, x | NK/Q(x) in Z[x] ⊂O.
(8) the units of an order O are {u ∈O : NK/Q(u) = ±1},
Properties 1, 3, 4, and 5 are what we used about OK in the results up through and
including Theorem 3.2(1), so those results apply to all orders and not just to OK. For in-
stance, deﬁne a fractional O-ideal as a nonzero O-module in K with a common denominator
from O −{0}. Then fractional O-ideals are the same thing as nonzero ﬁnitely generated
O-modules in K (analogue of Theorem 2.3(4)) and the only possible inverse of a fractional
O-ideal I is eI = {x ∈K : xI ⊂O}, which is always a fractional O-ideal (analogue of Theo-
rem 2.7). Each nonzero ideal in O contains a product of nonzero prime ideals (analogue of
Lemma 3.1). When p is a nonzero prime ideal in O, O ⊂ep and this containment is strict
(analogue of Theorem 3.2(1)).
When we try to prove Theorem 3.2(2) with O in place of OK, we run into a problem!
For x ∈ep −O, xp + p is either p or O. If we try to show the ﬁrst option is not true by
contradiction, then we want to show from xp ⊂p that x ∈O. Since p is a ﬁnitely generated
Z-module, when xp ⊂p we know x is integral over Z, so x ∈OK, but there is no reason to
expect x ∈O (the integral closure of Z in K is OK, not O), so we can’t get a contradiction.
The three corollaries of Theorem 3.2 for OK are formal consequences of pep = (1): they
would apply to every nonzero prime ideal p ⊂O such that pep = O (using the same proofs).
The proof of unique prime ideal factorization in OK (Theorem 3.6) would also apply to an
order whose nonzero prime ideals all satisfy Theorem 3.2(2). Therefore Theorem 3.2(2), the
invertibility of all nonzero prime ideals, is really the key step in our proof of unique prime
ideal factorization in OK.
The following theorem implies that every order of K that is smaller than the maximal
order OK doesn’t satisfy Theorem 3.2(2) for at least one nonzero prime ideal.
Theorem 8.1. If a domain has cancellation of ideals, i.e., always ac = bc implies a = b
when c ̸= (0), then the domain is integrally closed.

<!-- page 21 -->
IDEAL FACTORIZATION
21
Proof. Let A be a domain with cancellation of ideals. Suppose an x in the fraction ﬁeld of
A is integral over A. We want to show x is in A. Write x = a/b where a and b are in A
with b ̸= 0. Since x is integral over A,
xn + cn−1xn−1 + · · · + c1x + c0 = 0
with n ≥1 and ci ∈A. Let R = A[x] = A + Ax + · · · + Axn−1. This is a ring and a nonzero
A-module in the fraction ﬁeld of A. Since x has denominator b, by the deﬁnition of R we
have bn−1R ⊂A, so R has common denominator bn−1. Therefore
a := bn−1R = Abn−1 + Abn−2a + · · · + Aan−1
is a nonzero A-module in A, i.e., a is a nonzero ideal in A. Since R is a ring, R2 = R, so
a2 = b2(n−1)R2 = bn−1bn−1R = (b)n−1a. Therefore by cancellation of nonzero ideals in A,
a = (b)n−1 = bn−1A, so bn−1R = bn−1A. This implies R = A, so x ∈R = A.
□
A domain with unique factorization of ideals will have cancellation of ideals and thus will
be integrally closed. Therefore, since no order in a number ﬁeld is integrally closed except
for the maximal order (the full ring of integers), non-maximal orders do not have unique
factorization of ideals: they must contain a non-invertible prime ideal p ̸= (0). We give
next a basic example of this.
Example 8.2. Let K be a number ﬁeld ﬁeld with degree n > 1 and p be a prime number.
Set
O = Z + pOK.
We will show O has a nonzero ideal with no prime ideal factorization in O and O has an
explicit nonzero prime ideal that is not invertible.
Set
b = pO = pZ + p2OK,
p = pOK = bOK,
so b ⊂p ⊂O. Note p is an ideal in both O and OK. We will show
(1) the chain of ideals has indices as indicated:
p2 p⊂b
pn−1
⊂p
p⊂O
pn−1
⊂OK,
(2) p is a prime ideal in O that is not invertible as a fractional O-ideal,
(3) bp = p2,
(4) b is not a product of prime ideals in O,
(5) p does not divide b.
(1): Let {1, e2, . . . , en} be a Z-basis of OK, so
OK = Z ⊕Ze2 ⊕· · · ⊕Zen,
O = Z ⊕Zpe2 ⊕· · · ⊕Zpen,
pOK = Zp ⊕Zpe2 ⊕· · · ⊕Zpen,
pO = Zp ⊕Zp2e2 ⊕· · · ⊕Zp2en,
p2OK = Zp2 ⊕Zp2e2 ⊕· · · ⊕Zp2en.
Since p2 = (pOK)2 = p2OK, these direct sums explain all the desired ideal indices. The
chain of strict inclusions p2 ⫋b ⫋p in O would be impossible in a Dedekind domain.
We can see explicitly in this example that the ideal norm in O is not multiplicative:
[O : p2] = pn+1 and [O : p]2 = p2.

<!-- page 22 -->
22
KEITH CONRAD
(2): Since O/p = (Z + pOK)/pOK ∼= Z/(pOK ∩Z) = Z/pZ, p is a prime ideal in O. If
p had an inverse as a fractional O-ideal then {x ∈K : xp ⊂p} would equal O. But p is
an ideal in OK and thus invertible as a fractional OK-ideal, so {x ∈K : xp ⊂p} actually
equals OK. In particular, although p is principal as an ideal in OK, it is not principal as an
ideal in O since nonzero principal ideals are always invertible. (The ideals p = pOK and pO
in O are not the same; the second one is principal in O.)
(3): This a computation: bp = pOpOK = p2OK = p2.
(4): Assume b is a product of prime ideals. Since p2 = bp ⊂b, if a nonzero prime ideal q
divides b then q ⊃b ⊃p2, so q = p by the analogue of Corollary 1.5 for orders. Therefore
b must be a power of p. From (1), b lies strictly between p and p2, and pk ⊂p2 for k ≥3,
so b is not a power of p.
(5): Assume b = pb′. Since b ̸= p, b′ ̸= (1). Therefore b′ ⊂q for some maximal ideal q
of O. Then q ⊃b′ ⊃pb′ = b ⊃p2, so q = p. Thus b′ ⊂p, so we get b = pb′ ⊂p2. However,
p2 is a proper subset of b, so we have a contradiction.
This shows containment of ideals does not imply divisibility (p contains b but p does not
divide b).
Example 8.3. A non-maximal order in a number ﬁeld can’t be a PID because a PID
is integrally closed. We can also directly exhibit an example of a non-principal ideal in
every non-maximal order. If K is a number ﬁeld and O ⊂OK is a non-maximal order, let
m = [OK : O] ≥2. Then mOK ⊂O and mOK is an ideal of O (it’s an O-module inside of
O) but it is not a principal ideal in O: if mOK = αO for some α ∈O then for all x ∈OK
we have xα ∈xmOK ⊂mOK = αO, so x ∈O. Thus OK ⊂O. But O is a proper subset of
OK, so we have a contradiction.
Example 8.4. In a number ﬁeld K with degree n, all nonzero ideals in an order of K have
at most n generators since they have n generators as a Z-module. We showed in Theorem
4.11 that each nonzero ideal in OK has at most 2 generators. When n ≥3 we’ll construct
orders O in K that have an ideal with a minimal generating set (as an ideal of O) of size n.
For c ≥2, set O = Z + cOK and a = cOK. Then a is an ideal in O since it’s an ideal
of OK inside the subring O. Since a ∼= Zn as an additive group, a Z-basis of a is also a
generating set of a as an ideal in O, so a has an n-element generating set as an ideal in O.
To show a has no generating set as an ideal in O of size less than n, we’ll look at a/a2
as an O/a-module. Every generating set of a as an ideal in O reduces to a generating set of
a/a2 as an O/a-module, so we’ll be done by showing a/a2 can’t be generated by less than
n elements as an O/a-module.
What is a2? The deﬁnition of a product of ideals in a ring doesn’t make direct reference
to the ambient ring, so since a = cOK is an ideal in both OK and O we will compute a2
more easily by viewing it as a principal ideal in OK: a2 = c2OK. Then as an abelian group,
a/a2 = cOK/c2OK ∼= OK/cOK ∼= (Z/cZ)n,
so |a/a2| = cn. If a/a2 has an r-element generating set as an O/a-module, then there’s
a surjective O/a-linear map (O/a)r ↠a/a2, so |(O/a)r| ≥|a/a2| = cn. Since a ∩Z =
cOK ∩Z = cZ, O/a = (Z + a)/a ∼= Z/cZ as rings, so |(Z/cZ)r| ≥cn. Thus r ≥n.
Similar reasoning works if we start with c ≥2 and an order R (not just R = OK) and
use O = Z + cR. The ideal a = cR in O has index c,3 and since R ∼= Zn as an abelian group
3There is a Z-basis of R that includes 1, so R = Z ⊕Ln
i=2 Zei. Then O = Z + cR = Z ⊕Ln
i=2 Zcei, so
[R : O] = cn−1. Thus [O : cR] = [R : cR]/[R : O] = cn/cn−1 = c.

<!-- page 23 -->
IDEAL FACTORIZATION
23
we have a/a2 = cR/c2R ∼= R/cR ∼= (Z/cZ)n as abelian groups, so every generating set of a
as an ideal in O has at least n elements.
Remark 8.5. For the order O = Z + pOK of Example 8.2, pOK is an ideal in both OK
and O, so an ideal for one order can also be an ideal for another order. This can lead to
diﬀerent meanings for eI. Consider I = pOK. Viewed in OK and O respectively, we have
eI = {α ∈K : αI ⊂OK},
eI = {α ∈K : αI ⊂O},
and these are not the same. The ﬁrst set is (1/p)OK (since I = pOK is a principal ideal in
OK), while the second set is OK (OK ⊂eI ⊂(1/p)O, [(1/p)O : OK] = p, and 1/p ̸∈eI, so eI
must be OK). This ambiguity in the meaning of eI won’t lead to confusion since we’re not
going to be dealing with more than one order at a time.
Theorem 8.6. For each order O in a number ﬁeld K, all but ﬁnitely many nonzero prime
ideals in O are invertible.
Proof. Both OK and O are ﬁnite free Z-modules with the same rank, so OK/O is ﬁnite.
Choose m ∈Z+ such that mOK ⊂O, such as the index [OK : O]. The ideal (m) = mO
contains a product of prime ideals in O, say (m) ⊃p1 · · · pr (analogue of Lemma 3.1 for O).
We will show each nonzero prime ideal other than p1, . . . , pr is invertible. (When O = OK
we can use m = 1 and this recovers the fact that all nonzero primes in OK are invertible.)
A prime ideal of O that contains (m) must be one of the pi’s (analogue of Corollary 1.5
for O). Let p ̸= p1, . . . , pr, so p ̸⊃(m). Therefore p + (m) = O by maximality of p. Write
π + mb = 1 for some π ∈p and b ∈O.
Choose x ∈ep −O (analogue of Theorem 3.2(1) for O). Then p ⊂p + xp ⊂O, so p + xp is
either p or O. If the second option occurs then p(O + xO) = O and p is invertible. That’s
what we want. To eliminate the ﬁrst option, we argue by contradiction. Suppose p+xp = p,
so xp ⊂p. Since p is a ﬁnitely generated Z-module, this inclusion implies x ∈OK. Write
x = x · 1 = xπ + xmb. Since mx ∈mOK ⊂O, xmb ∈O. The product xπ is in pep, which is
also in O by the deﬁnition of ep. Thus x = xπ + xmb is in O. This is a contradiction.
□
Example 8.7. Returning to Example 8.2, where O = Z + pOK for a prime p, we show
every prime ideal of O except for p is invertible. Obviously pOK ⊂O, so we can take m = p
in Theorem 8.6. The ideal mO = pO = b has b ⊃p2 where p = pOK is a prime ideal of
O, so the only prime that contains pO is p. This means every prime in O other than p is
invertible. In particular, taking K = Q(i) and p = 2, every prime ideal of Z[2i] = Z + 2Z[i]
is invertible except perhaps for p := 2Z[i] (which is not invertible as a Z[2i]-module since
{x ∈Q(i) : xp ⊂p} is Z[i] rather than Z[2i]).
Theorem 8.6 is analogous to the fact that a plane algebraic curve is smooth at all but
ﬁnitely many points.
Although unique prime ideal factorization is false in a non-maximal order, there is a
meaningful substitute. Rather than use products of prime ideals in O, we will use ﬁltrations
of ideals having simple successive quotients as O-modules.
When passing from ﬁnite abelian groups to general ﬁnite groups, the use of direct products
to decompose a group is replaced with the idea of a normal series (an increasing tower
of subgroups, each normal in the next, starting at the identity and ending at the whole
group).
The Jordan–H¨older theorem guarantees that when a normal series for a ﬁnite
group has simple quotients (the normal series is then called a composition series), those
simple quotients are unique up to isomorphism and multiplicity. In the setting of orders in

<!-- page 24 -->
24
KEITH CONRAD
a number ﬁeld, we will use the Jordan–H¨older theorem for modules to get a replacement
for unique factorization of ideals.
Theorem 8.8 (Jordan-H¨older). Let M be a module over a commutative ring R and assume
it admits a ﬁltration
M = M0 ⊃M1 ⊃· · · ⊃Mk = {0}
where each quotient module Mi/Mi+1 is simple. Then each ﬁltration
M = M′
0 ⊃M′
1 ⊃· · · ⊃M′
ℓ= {0}
where M′
i/M ′
i+1 is simple has k = ℓand there is some permutation π ∈Sk such that
Mi/Mi+1 ∼= M′
π(i)/M ′
π(i)+1 for all i.
This is proved in the same way as the Jordan-H¨older theorem for groups. A ﬁnite chain
of submodules Mi with Mi/Mi+1 simple is called a Jordan-H¨older ﬁltration (or composition
series) for M.
Theorem 8.9. Let O be an order in a number ﬁeld. For a nonzero proper ideal b ⊂O,
there is a descending series of ideals
(8.1)
O = b0 ⊃b1 ⊃· · · ⊃bℓ−1 ⊃bℓ= b
such that each bi/bi+1 is a simple O-module.
For 0 ≤i ≤ℓ−1, bi/bi+1 ∼= O/pi as O-modules for a unique nonzero prime ideal pi in
O. The pi’s are the nonzero prime ideals of O that contain b and for each prime p ⊃b the
number of pi’s equal to p is independent of the choice of series (8.1) having simple quotients.
Moreover, [O : b] = Qℓ−1
i=0[O : pi].
Proof. Since O/b is ﬁnite it has a composition series as a O-module:
O/b = M0 ⊃M1 ⊃· · · ⊃Mℓ= {0},
where each Mi/Mi+1 is a simple O-module. Since the Mi’s are submodules of O/b, Mi = bi/b
for an ideal bi, so bi ⊃bi+1 and bi/bi+1 ∼= Mi/Mi+1 is a simple O-module. The descending
chain of ideals bi is a series of the form (8.1).
A simple O-module is isomorphic as an O-module to O/p for a unique nonzero prime ideal
p. Indeed, if M is a simple O-module, pick x0 ̸= 0 in M. Then Ox0 is a nonzero submodule
of M, so by simplicity M = Ox0. We can map O onto M by b 7→bx0. This is O-linear and
surjective. Denote its kernel as p, so p is an ideal in O and O/p ∼= M as O-modules. Then O/p
is a simple O-module, so p must be maximal, since an intermediate ideal p ⊂a ⊂O yields a
nonzero proper O-submodule a/p ⊂O/p. Intrinsically, p = AnnO(M) since p = AnnO(O/p)
and isomorphic O-modules have equal annihilators. Thus, when we write bi/bi+1 ∼= O/pi as
O-modules, there is one choice for pi: the annihilator ideal AnnO(bi/bi+1).
Since pi = AnnO(bi/bi+1) and bi+1 kills bi/bi+1, bi+1 ⊂pi. Therefore for 0 ≤i ≤ℓ−1,
pi ⊃bi+1 ⊃bℓ= b, so every pi contains b. To prove that each prime ideal containing b
is some pi, we note that pibi ⊂bi+1 from the formula for pi as an annihilator, so taking
i = ℓ−1, ℓ−2, . . . , 0,
(8.2)
b = bℓ⊃pℓ−1bℓ−1 ⊃pℓ−1pℓ−2bℓ−2 ⊃· · · ⊃pℓ−1 · · · p0b0 = p0 · · · pℓ−1.
Therefore if p is a prime ideal that contains b then p ⊃p0 · · · pℓ−1, so p is some pi by the
analogue of Corollary 1.5 for orders.
The number of times a prime ideal occurs as an annihilator of quotient modules in the
series (8.1) is independent of the choice of series thanks to the Jordan–H¨older theorem, that

<!-- page 25 -->
IDEAL FACTORIZATION
25
says the quotient modules in a composition series for O/b are determined up to O-module
isomorphism and multiplicity.
Since indices are multiplicative in towers, [O : b] = Qℓ−1
i=0[bi : bi+1]. Since bi/bi+1 ∼= O/pi
as O-modules, [bi : bi+1] = [O : pi].
□
Remark 8.10. It might seem wrong that the condition O/p ∼= O/p′ for nonzero prime ideals
p and p′ implies p = p′. After all, taking O = Z[i], aren’t Z[i]/(1 + 2i) and Z[i]/(1 −2i)
isomorphic ﬁelds (all ﬁelds of order 5 are isomorphic) while the ideals (1+2i) and (1−2i) are
diﬀerent? That’s true, but the sense in which we refer to an isomorphism with O/p in the
proof above is not as ﬁelds (or rings), but as O-modules: if O/a ∼= O/b as O-modules then
a = b because the annihilator ideal of the O-module O/a is a and isomorphic O-modules
have equal annihilator ideals. Returning to the example of Z[i]/(1 + 2i) and Z[i]/(1 −2i),
they are isomorphic as ﬁelds, but they are not isomorphic as Z[i]-modules: in Z[i]/(1 + 2i)
we have i = 2 (since 1 + 2i = 0) and in Z[i]/(1 −2i) we have i = 3, so if there were a
Z[i]-linear map Z[i]/(1 + 2i) →Z[i]/(1 −2i) then the equation i = 2 in the domain would
become i = 2 in the target, so 3 = 2 in the target, but 3 ̸= 2 in Z[i]/(1 −2i).
Example 8.11. Returning to Example 8.2, where O = Z + pOK, we will ﬁnd a Jordan-
H¨older ﬁltration for O/b, where b = pO. Since p = pOK is the only prime containing b,
Theorem 8.9 says every simple quotient module in a Jordan-H¨older ﬁltration for O/b has
to be isomorphic (as an O-module) to O/p ∼= Z/pZ. Since |O/b| = pn, this means there is
a chain of ideals
O = b0 ⊃b1 ⊃· · · ⊃bn = b
such that bi/bi+1 ∼= O/p.
Let’s make such a chain of ideals explicit. Let {1, e2, . . . , en} be a Z-basis of OK, so
O = Z ⊕Zpe2 ⊕· · · ⊕Zpen,
pOK = Zp ⊕Zpe2 ⊕· · · ⊕Zpen,
pO = Zp ⊕Zp2e2 ⊕· · · ⊕Zp2en.
Set b0 = O, b1 = p = pOK, and for 2 ≤i ≤n set
bi = Zp ⊕Zp2e2 ⊕· · · ⊕Zp2ei ⊕Zpei+1 ⊕· · · ⊕Zpen.
This is an ideal in O since the product of each basis vector for O, besides 1, and each basis
vector for bi is in p2OK ⊂pO = b ⊂bi. We have bi/bi+1 ∼= Zpei+1/Zp2ei+1 ∼= Z/pZ.
Instead of factoring b into a product of prime ideals in O (which Example 8.2 says is
impossible) we have ﬁltered O/b by the O-modules
O/b ⊃b1/b ⊃b2/b ⊃· · · ⊃bn/b = {0}
with simple quotients bi/bi+1 ∼= Z/pZ ∼= O/p.
In Example 8.2 we saw [O : p2] = pn+1. The Jordan-H¨older ﬁltration for O/p2 comes
from O ⊃p ⊃b ⊃p2, where all successive quotients are isomorphic as O-modules to O/p.
Let’s see what Theorem 8.9 says for the case when O = OK is the full ring of integers
of a number ﬁeld K. When b is a nonzero proper ideal in OK, the prime factorization of
ideals in OK lets us make the Jordan–H¨older ﬁltration of OK/b explicit, as follows. Writing
b = p0 · · · pr−1, set b0 = OK and bi = p0 · · · pi−1 for 1 ≤i ≤r. Then
OK = b0 ⊃b1 ⊃· · · ⊃br = b

<!-- page 26 -->
26
KEITH CONRAD
and bi/bi+1 = bi/bipi ∼= OK/pi as OK-modules, by the ﬁrst proof of Theorem 7.5. Thus
each bi/bi+1 is a simple OK-module. Since the Jordan-H¨older theorem lets us compare each
Jordan-H¨older ﬁltration for OK/b with the particular one we just constructed, we can say
that in every Jordan-H¨older ﬁltration for OK/b,
• the prime ideal factors of b are the annihilators of the simple quotients in the
ﬁltration,
• the multiplicity of each prime ideal as a factor of b is its multiplicity as an annihilator
of a simple quotient in the ﬁltration.
References
[1] Z. I. Borevich and I. R. Shafarevich, “Number Theory,” Academic Press, New York, 1966.
[2] N. Bourbaki, “Commutative Algebra,” Addison-Welsey, Reading, MA 1972.
[3] H. S. Butts and L. Wade, Two Criteria for Dedekind Domains, Amer. Math. Monthly 73 (1966), 14–21.
[4] H. Cohen, “A Course in Computational Algebraic Number Theory,” Springer–Verlag, New York, 1993.
[5] D. Dummit and R. Foote, “Abstract Algebra,” 3rd ed., Wiley, New York, 2004.
[6] N. Jacobson, “Basic Algebra II,” 2nd ed., W. H. Freeman & Co., New York, 1989.
[7] D. Lorenzini, “An Introduction to Arithmetic Geometry,” American Math. Society, Providence, 1996.
[8] H. Matsumura, “Commutative Ring Theory,” Cambridge Univ. Press, Cambridge, 1986.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*