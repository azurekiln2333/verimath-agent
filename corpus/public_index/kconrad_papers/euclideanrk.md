# Euclidean Domains

> **Source**: https://kconrad.math.uconn.edu/blurbs/euclideanrk.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
KEITH CONRAD
1. Introduction
The following deﬁnition of a Euclidean (not Euclidian!)
domain is very common in
textbooks. We write N for {0, 1, 2, . . . }.
Deﬁnition 1.1. An integral domain R is called Euclidean if there is a function d: R−{0} →
N with the following two properties:
(1) d(a) ≤d(ab) for all nonzero a and b in R,
(2) for all a and b in R with b ̸= 0 we can ﬁnd q and r in R such that
a = bq + r,
r = 0 or d(r) < d(b).
We will call (1) the d-inequality. Sometimes it is expressed in a diﬀerent way: for nonzero
x and y in R, if x | y then d(x) ≤d(y). This is equivalent to the d-inequality.
Examples of Euclidean domains are Z (with d(n) = |n|), F[T] for a ﬁeld F (with d(f) =
deg f; this example is the reason that one doesn’t assume d(0) is deﬁned), and Z[i] (d(α) =
N(α)). A trivial kind of example is a ﬁeld F with d(a) = 1 for all a ̸= 0 (here all remainders
are 0). For any Euclidean domain (R, d) in the sense of Deﬁnition 1.1, other examples are
(R, 2d), (R, d2), and (R, 2d).
Deﬁnition 1.1 is used in [1, §2.1], [5, §37], [6, §7.2], [7, §6.5], [9, §3.7], [10, Chap. III §3],
and [18, §18], which shows that Deﬁnition 1.1 accounts for all the basic examples (since
otherwise we wouldn’t see Deﬁnition 1.1 so widely used).
However, we ﬁnd a diﬀerent
deﬁnition in [4, §8.1], where the d-inequality is missing:
Deﬁnition 1.2. An integral domain R is called Euclidean if there is a function d: R−{0} →
N such that R has division with remainder with respect to d: for all a and b in R with
b ̸= 0 we can ﬁnd q and r in R such that
(1.1)
a = bq + r,
r = 0 or d(r) < d(b).
We allow a = 0 in this deﬁnition since in that case we can use q = 0 and r = 0.
A function d: R −{0} →N that satisﬁes (1.1) will be called a Euclidean function on R.
Thus a Euclidean domain in Deﬁnition 1.2 is an integral domain that admits a Euclidean
function, while a Euclidean domain in Deﬁnition 1.1 is an integral domain that admits a
Euclidean function satisfying the d-inequality.
Does Deﬁnition 1.2 describe a larger class of rings than Deﬁnition 1.1? No. We will
show in Section 2 that every Euclidean domain (R, d) in the sense of Deﬁnition 1.2 can be
equipped with a diﬀerent Euclidean function ed such that ed(a) ≤ed(ab) for all a and b in R,
so (R, ed) is Euclidean in the sense of Deﬁnition 1.1.
The main reason that the d-inequality is not included in the deﬁnition of a Euclidean do-
main in [4] is that it is irrelevant to prove the two main theorems about Euclidean domains:
1

<!-- page 2 -->
2
KEITH CONRAD
that every ideal in a Euclidean domain is principal1 and that the Euclidean algorithm in
a Euclidean domain terminates after ﬁnitely many steps and produces a greatest common
divisor. There can be greatest common divisors in rings that are not Euclidean (such as
in Z[X, Y ]), but it may be hard in those rings to compute greatest common divisors by a
method that avoids factorization. When a ring is Euclidean, the Euclidean algorithm in the
ring lets us compute greatest common divisors without having to factor, which makes this
method practical.
Why is the d-inequality mentioned so often in the (textbook) literature if it’s actually not
needed? While it is not needed for the two speciﬁc results cited in the previous paragraph,
it is convenient to use the d-inequality if we want to prove there is factorization into irre-
ducibles in Euclidean domains without having to rely on a proof of this property by more
abstract methods for a larger collection of integral domains. This will be done in Section 4
(speciﬁcally, Theorem 4.2) after working out some preliminary results in Section 3.
In Section 5 we discuss Euclidean domains among quadratic rings.
2. Refining the Euclidean function
Suppose (R, d) is a Euclidean domain in the sense of Deﬁnition 1.2. We will introduce
a new Euclidean function ed: R −{0} →N, built out of d, which satisﬁes ed(a) ≤ed(ab).
Then (R, ed) is Euclidean in the sense of Deﬁnition 1.1, so the rings that admit Euclidean
functions in either sense are the same.
Here’s the deﬁnition (trick?): for nonzero a in R, set
ed(a) = min
b̸=0 d(ab).
That is, ed(a) is the smallest d-value on the nonzero multiples of a. (We have ab ̸= 0 when
b ̸= 0 since R is an integral domain.) Since a = a · 1 is a nonzero multiple of a,
(2.1)
ed(a) ≤d(a)
for all nonzero a in R.
For each a ̸= 0 in R, ed(a) = d(ab0) for some nonzero b0 and
d(ab0) = ed(a) ≤d(ab) for all nonzero b. For example,
ed(1) = min
b̸=0 d(b)
is the smallest d-value on R −{0}.
Theorem 2.1. Let (R, d) be a Euclidean domain in the sense of Deﬁnition 1.2. Then (R, ed)
is Euclidean in the sense of Deﬁnition 1.1.
If you want to use Deﬁnition 1.1 as the deﬁnition of a Euclidean domain then you can
skip the proof of Theorem 2.1.
Proof. For nonzero a and b in R we have
ed(a) ≤ed(ab).
Indeed, write ed(ab) = d(abc) for some nonzero c in R. Since abc is a nonzero multiple of a,
ed(a) ≤d(abc) = ed(ab).
1We’ll see in Section 5 that in some non-Euclidean domains all ideals may be principal too.

<!-- page 3 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
3
We now show R admits division with remainder with respect to ed. Pick a and b in R
with b ̸= 0. Set ed(b) = d(bc) for some nonzero c ∈R. Using division of a by bc (which is
nonzero) in (R, d) there are q0 and r0 in R such that
a = (bc)q0 + r0,
r0 = 0 or d(r0) < d(bc).
Set q = cq0 and r = r0, so a = bq + r. If r0 = 0 we are done, so we may assume r0 ̸= 0.
Since d(bc) = ed(b) and ed(r) ≤d(r) (by (2.1)), the condition d(r) = d(r0) < d(bc) implies
ed(r) < ed(b). Thus
a = bq + r,
r = 0 or ed(r) < ed(b).
Hence (R, ed) is a Euclidean domain in the sense of Deﬁnition 1.2.
□
We end this section with a brief discussion of two other possible reﬁnements one might
want in a Euclidean function (but which we will not need later): uniqueness of the quotient
and remainder it produces and multiplicativity.
In Z we write a = bq + r with 0 ≤r < |b| and q and r are uniquely determined by a
and b. There is also uniqueness of the quotient and remainder when we do division in F[T]
(relative to the degree function) and in a ﬁeld (the remainder is always 0). Are there other
Euclidean domains where the quotient and remainder are unique? Division in Z[i] does not
have a unique quotient and remainder relative to the norm on Z[i]. For instance, dividing
1 + 8i by 2 −4i gives
1 + 8i = (2 −4i)(−1 + i) −1 + 2i and 1 + 8i = (2 −4i)(−2 + i) + 1 −2i,
where both remainders have norm 5, which is less than N(2 −4i) = 20.
Theorem 2.2. If R is a Euclidean domain where the quotient and remainder are unique
then R is a ﬁeld or R = F[T] for a ﬁeld F.
Proof. See [11] or [15].
□
This might be a surprise: Z isn’t in the theorem! Aren’t the quotient and remainder in
Z unique? Yes if we use a remainder r where 0 ≤r < |b|, but not if we try to pick r in the
setting of Euclidean domains by using |r| < |b|. For instance,
51 = 6 · 8 + 3 and 51 = 6 · 9 −3.
The point is that using the Euclidan function on the remainder too, in the case of Z, permits
negative remainders so in fact Z does not have a unique quotient and remainder when we
measure the remainder by its absolute value.
The Euclidean function in many basic examples satisﬁes a stronger property than d(a) ≤
d(ab), namely d(ab) = d(a)d(b) with d(a) ≥1 when a ̸= 0. For instance, this holds in
Z (d(n) = |n|) and Z[i] (d(α) = N(α)). The degree on F[T] is not multiplicative, but
d(f) = 2deg f is multiplicative. There is also a multiplicative Euclidean function on a ﬁeld
F: d(a) = 1 for all a ̸= 0. For an example of a Euclidean domain that does not admit a
multiplicative Euclidean function, see [3].
3. Features of the d-inequality
Let R be a Euclidean domain. By Theorem 2.1 we may assume our Euclidean function
d satisﬁes the d-inequality: d(a) ≤d(ab) for all nonzero a and b in R. Using this inequality
we will prove a few properties of d.
Theorem 3.1. Let (R, d) be a Euclidean domain where d satisﬁes the d-inequality. Then

<!-- page 4 -->
4
KEITH CONRAD
(1) d(a) ≥d(1) for all nonzero a ∈R,
(2) if b ∈R× then d(ab) = d(a) for all nonzero a,
(3) if b ̸∈R× and b ̸= 0 then d(ab) > d(a) for all nonzero a.
In particular, for nonzero a and b, d(ab) = d(a) if and only if b ∈R×.
Proof. (1): By the d-inequality, d(1) ≤d(1 · a) = d(a).
(2): By the d-inequality, d(a) ≤d(ab). To get the reverse inequality, let c be the inverse
of b, so the d-inequality implies
d(ab) ≤d((ab)c) = d(a).
(3): We want to show the inequality d(a) ≤d(ab) is strict when b is not a unit and not
0. The proof is by contradiction. Assume d(a) = d(ab). Now use division of a by ab:
a = (ab)q + r,
r = 0 or d(r) < d(ab).
We rewrite this as
a(1 −bq) = r,
r = 0 or d(r) < d(a).
Since b is not a unit, 1 −bq is nonzero, so a(1 −bq) is nonzero (because R is an integral
domain). Thus r ̸= 0, so the inequality d(r) < d(a) becomes
d(a(1 −bq)) < d(a).
But this contradicts the d-inequality, which says d(a) ≤d(a(1 −bq)). Thus it is impossible
for d(a) to equal d(ab) when b is not a unit.
□
Note Theorem 3.1 is not saying two nonzero elements of R that have the same d-value
are unit multiples, but rather that a multiple of a nonzero a ∈R has the same d-value as a
if and only if it is a unit multiple of a. For example, in Z[i] we have N(1 + 2i) = N(1 −2i)
but 1 + 2i and 1 −2i are not unit multiples. Remember this!
Corollary 3.2. Let (R, d) be a Euclidean domain where d satisﬁes the d-inequality. We
have d(a) = d(1) if and only if a ∈R×. That is, the elements of least d-value in R are
precisely the units.
Proof. Take a = 1 in parts 2 and 3 of Theorem 3.1.
□
We can see Corollary 3.2 working in Z and F[T]: the integers satisfying |n| = |1| are ±1,
which are the units of Z. The polynomials f in F[T] satisfying deg f = deg 1 = 0 are the
nonzero constants, which are the units of F[T].
Corollary 3.3. Let (R, d) be a Euclidean domain where d satisﬁes the d-inequality. If a
and b are nonunits, then d(a) and d(b) are both less than d(ab).
Proof. This is immediate from part (3) of Theorem 3.1, where we switch the roles of a and
b to get the inequality on both d(a) and d(b).
□
4. Irreducible factorization
One of the key properties of Euclidean domains is that in them all ideals all principal:
every Euclidean domain is a PID2. Theorems about PIDs may be simpler to prove in
Euclidean domains. For an example of this, we’ll prove in diﬀerent ways that irreducible
factorization exists in Euclidean domains and in PIDs (Theorems 4.2 and 4.4).
2A PID (principal ideal domain) is an integral domain in which each ideal is a principal ideal.

<!-- page 5 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
5
Deﬁnition 4.1. Let R be an integral domain. A nonzero element a of R is called irreducible
if it is not a unit and in every factorization a = bc, one of the factors b or c is a unit. A
nonzero nonunit that is not irreducible is called reducible.
There are three types of nonzero elements in an integral domain: units (the invertible
elements, whose factors are always units too), irreducibles (nonunits whose factorizations
into two parts always involve one unit factor), and reducibles (nonunits that admit some
factorization into a product of two nonunits). Notice that in a ﬁeld there are no reducible or
irreducible elements: everything is zero or a unit. So if we want to prove a theorem about
irreducible factorization, we avoid ﬁelds.
Theorem 4.2. In a Euclidean domain that is not a ﬁeld, every nonzero nonunit is a product
of irreducibles.
Proof. Let (R, d) be a Euclidean domain that is not a ﬁeld. By Theorem 2.1 we may assume
d(a) ≤d(ab) for all nonzero a and b in R. Therefore Corollary 3.3 applies.
We will prove the existence of irreducible factorizations by induction on the d-value. From
Corollary 3.2, the units of R have the smallest d-value. An a ∈R with second smallest
d-value must be irreducible: if we write a = bc and b and c are both nonunits, then d(b)
and d(c) are both less than d(a) by Corollary 3.3. Therefore b and c are units, so a is a
unit. This is a contradiction.
Assume now that a ∈R is a nonunit and all nonunits with smaller d-value admit an
irreducible factorization. To prove a admits an irreducible factorization too, we may sup-
pose a is not irreducible itself. Therefore there is some factorization a = bc with b and c
both nonunits. Then d(b) < d(a) and d(c) < d(a) by Corollary 3.3, so b and c both have
irreducible factorizations by induction. Thus their product a has an irreducible factoriza-
tion.
□
We’ll see in the next theorem that the conclusion of Theorem 4.2 is true for PIDs, but
proving that will use more abstract methods than induction. It will rely on the following
lemma, which has a recursive ﬂavor.
Lemma 4.3. If R is an integral domain and a ∈R is a nonzero nonunit that does not admit
a factorization into irreducibles then there is a strict inclusion of principal ideals (a) ⊂(b)
where b is some other nonzero nonunit that does not admit a factorization into irreducibles.
Proof. By hypothesis a is not irreducible, so (since it is neither 0 nor a unit either) there
is some factorization a = bc where b and c are nonunits (and obviously are not 0 either).
If both b and c admitted irreducible factorizations then so does a, so at least one of b or c
has no irreducible factorization. Without loss of generality it is b that has no irreducible
factorization. Since c is not a unit, the inclusion (a) ⊂(b) is strict.
□
Theorem 4.4. In a PID that is not a ﬁeld, every nonzero nonunit is a product of irre-
ducibles.
Proof. Suppose there is an element a in the PID that is not 0 or a unit and has no irreducible
factorization. Then by Lemma 4.3 there is a strict inclusion
(a) ⊂(a1)
where a1 has no irreducible factorization. Then using a1 in the role of a (and Lemma 4.3
again) there is a strict inclusion
(a1) ⊂(a2)

<!-- page 6 -->
6
KEITH CONRAD
where a2 has no irreducible factorization. This argument (repeatedly applying Lemma 4.3
to the generator of the next larger principal ideal) leads to an inﬁnite increasing chain of
principal ideals
(4.1)
(a) ⊂(a1) ⊂(a2) ⊂(a3) ⊂· · ·
where all inclusions are strict. This turns out to be impossible in a PID.
Indeed, suppose a PID contains an inﬁnite strictly increasing chain of ideals:
I0 ⊂I1 ⊂I2 ⊂I3 ⊂· · ·
and set
I =
[
n≥0
In.
This union I is an ideal. The reason is that the In’s are strictly increasing, so every ﬁnite set
of elements from I lies in a common In. (This is the key idea.) So I is closed under addition
and arbitrary multiplications from the ring since each In has these properties. (Make sure
you understand that step.) Because we are in a PID, I is principal: I = (r) for some r in
the ring. But because I is the union of the In’s, r is in some IN. Then (r) ⊂IN since IN
is an ideal, so
I = (r) ⊂IN ⊂I,
which means
IN = I.
But this is impossible because the inclusion IN+1 ⊂I becomes IN+1 ⊂IN and we were
assuming IN was a proper subset of IN+1. Because of this contradiction, nonzero nonunits
in a PID without an irreducible factorization do not exist.
□
Remark 4.5. If we look at the proof of Theorem 4.4 in the contrapositive direction, in an
integral domain containing a nonzero nonunit a without an irreducible factorization, there
must be a nonprincipal ideal and in fact such an ideal is I := S
n≥0(an), where a0 = a, an
for n ≥1 is a factor of an−1 that is not a unit or a unit multiple of an−1, and an has no
irreducible factorization. The reason I can’t be principal is because the proof shows that if
I is principal then we get a contradiction to a not having an irreducible factorization.
The proof in Theorem 4.4 that a PID does not contain an inﬁnite strictly increasing chain
of ideals holds for a broader class of rings than PIDs.
Theorem 4.6. A commutative ring in which every ideal is ﬁnitely generated does not
contain an inﬁnite strictly increasing chain of ideals.
Proof. The second half of the proof of Theorem 4.4 works in this more general context. All
we have to do is show the logic works when I is ﬁnitely generated rather than principal.
The point is that if I = (x1, . . . , xm) then the ﬁnitely many xi’s all lie in some common IN
(because the In’s are an increasing chain). And now the contradiction is obtained just as
before: IN = I but then IN+1 ⊂IN, contradiction.
□
Corollary 4.7. In an integral domain where every ideal is ﬁnitely generated, every nonzero
nonunit has an irreducible factorization.
Proof. If there were an element a that is not 0 or a unit and that did not admit an irreducible
factorization then, as in the proof of Theorem 4.4, we could produce an inﬁnite strictly
increasing chain of (principal) ideals. But there are no inﬁnite strictly increasing chains of
ideals in the ring, by Theorem 4.6.
□

<!-- page 7 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
7
Deﬁnition 4.8. A commutative ring where every ideal is ﬁnitely generated is called a
Noetherian ring.
These rings are named after Emmy Noether, who was one of the pioneers of abstract
algebra in the early 20th century. Their importance, as a class of rings, stems from the
stability of the Noetherian property under many basic constructions. If R is a Noetherian
ring, then so is every quotient ring R/I (which may not be an integral domain even if R
is), every polynomial ring R[X] (and thus R[X1, . . . , Xn] by induction on n, viewing this as
R[X1, . . . , Xn−1][Xn]), and every formal power series ring R[[X]] (and thus R[[X1, . . . , Xn]]
by induction on n, since it is R[[X1, . . . , Xn−1]][[Xn]]). The PID property behaves badly for
ring constructions, e.g., if R is a PID that is not a ﬁeld then R[X] is not a PID. For instance,
R[X, Y ] = R[Y ][X] is never a PID for an integral domain R. But if R is Noetherian then
R[X, Y ] is Noetherian. Brieﬂy, the property “ideals are ﬁnitely generated” for Noetherian
rings is more robust than the property “ideals are singly generated” for PIDs.
Using this terminology, Corollary 4.7 says in every Noetherian integral domain each
element other than 0 or a unit has an irreducible factorization.
(Contrapositively, if a
nonzero nonunit a in an integral domain has no irreducible factorization, then the ideal
I := S
n≥0(an) from Remark 4.5 not only isn’t principal, but it isn’t ﬁnitely generated ei-
ther.) It is worth comparing the proof of existence of irreducible factorizations in Corollary
4.7 to the proof of the special case of Euclidean domains in Theorem 4.2, where the proof
of existence of irreducible factorizations is tied up with features of the Euclidean function
on the ring.
In the context of unique factorization domains, it is the uniqueness of the factorization
that lies deeper than the existence. We are not discussing uniqueness here, which most
deﬁnitely does not hold in most Noetherian integral domains. That is, the existence of
irreducible factorizations (for all nonzero nonunits) is not a very strong constraint, since
most integral domains that are met in day-to-day practice in mathematics are Noetherian,
so their elements must have a factorization into irreducible elements. But there usually is
not going to be a unique factorization into irreducible elements.
5. Euclidean and non-Euclidean quadratic rings
The main importance of Euclidean domains for an algebra course is that they give us
examples of PIDs. Three points are worth noting:
• Aside from computational issues (as in the Euclidean algorithm) it is more useful
to know whether or not a ring is a PID than whether or not it is Euclidean.
• There are methods that let one show certain kinds of integral domains are PIDs
without knowing whether or not they are Euclidean.
• There are PIDs that are not Euclidean.
The simplest rings that can be PIDs and not Euclidean are found among the quadratic
rings.
Deﬁnition 5.1. A quadratic ring is a ring of the form Z[γ] where γ is a complex number
that is a root of an irreducible quadratic polynomial T 2 + aT + b ∈Z[T] with leading
coeﬃcient 1. We call Z[γ] real if γ is real and imaginary otherwise.
For instance, the Gaussian integers Z[i] are an imaginary quadratic ring associated to the
polynomial T 2 + 1. When m ∈Z is not a perfect square, Z[√m] is real quadratic for m > 0
and imaginary quadratic for m < 0. The ring Z[(1+
√
5)/2] is real quadratic: (1+
√
5)/2 is

<!-- page 8 -->
8
KEITH CONRAD
a root of T 2 −T −1. Abstractly, Z[γ] ∼= Z[T]/(T 2 + aT + b). Irreducibility of T 2 + aT + b
in Z[T] implies the discriminant a2 −4b is not 0. Since γ = (−a ±
√
a2 −4b)/2, if a is even
then Z[γ] = Z[√m] where m = (a/2)2 −b ∈Z, and if a is odd then Z[γ] = Z[(1 + √m)/2]
where m = a2 −4b.
Since γ2 = −aγ −b ∈Z + Zγ, by induction every power of γ is in Z + Zγ, so
Z[γ] = Z + Zγ.
We can’t necessarily “complete” the square and write every quadratic ring as Z[√m] for
some integer m. For instance, Z[(1 +
√
5)/2] ̸= Z[√m] for m in Z, although in contrast to
that Q[(1 +
√
5)/2] = Q[
√
5].
When γ is one root of T 2 + aT + b, the second root is γ = −a −γ, which is called the
conjugate of γ. More generally, for α = x+yγ in Z[γ], where x and y are in Z, the conjugate
of α is
α := x + yγ = x −ay −yγ.
Check that α = α. In the special case that a = 0 and we write b = −m, so γ is a root of
T 2 −m (a square root of m), we have
γ = ±√m =⇒γ = −γ, x + yγ = x −yγ.
Example 5.2. If γ =
√
2 then x + y
√
2 = x −y
√
2.
Example 5.3. If γ = (1+
√
5)/2, a root of T 2−T −1, then x + yγ = x+y−yγ. Concretely,
this says x + y(1 +
√
5)/2 = x + y(1 −
√
5)/2.
The norm of α is deﬁned to be
N(α) = αα = x2 −axy + by2.
This is an integer, and it is zero only when α = 0. For c in Z, N(c) = c2. In particular,
N(±1) = 1. When γ = √m, we have
N(x + y√m) = (x + y√m)(x −y√m) = x2 −my2.
Notice the middle coeﬃcient −a of the formula x2 −axy + by2 for N(α) does not coincide
with the middle coeﬃcient a of T 2 + aT + b if a ̸= 0.
Example 5.4. If γ =
√
2 then N(x + y
√
2) = x2 −2y2, which takes both positive and
negative values, e.g., N(3 + 5
√
2) = −41.
Example 5.5. If γ = (1 +
√
5)/2, a root of T 2 −T −1, then N(x + yγ) = x2 + xy −y2 =
(x + y/2) −5y2/4, which has positive and negative values.
Example 5.6. If γ = √−5, a root of T 2 + 5, then N(x + yγ) = x2 + 5y2, which has no
negative values.
Example 5.7. If γ = √m for m ∈Z then N(x + yγ) = x2 −my2. This has both positive
and negative values if m > 0 and only nonnegative values if m < 0.
A direct calculation shows the norm is multiplicative:
N(αβ) = N(α) N(β).
Several “small” quadratic rings are Euclidean with the absolute value of the norm as a
Euclidean function. For instance, Z[i], Z[
√
2], and Z[√−2] are all Euclidean using d(α) =
| N(α)|. (For an imaginary quadratic ring like Z[i] we can drop the absolute value sign:

<!-- page 9 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
9
the norm is already nonnegative.)
This leads to two questions about a quadratic ring:
is it Euclidean (with respect to some Euclidean function) and is it norm-Euclidean (i.e.,
Euclidean with respect to the particular function d(α) = | N(α)|)?
For a quadratic ring to be norm-Euclidean is more precise than it being Euclidean: maybe
there is a Euclidean function on the ring even if the absolute value of the norm is not a
Euclidean function. The ﬁrst example of that was found by Clark [2] in 1994: he showed
Z[(1 +
√
69)/2] is Euclidean, and it was already known not to be norm-Euclidean. The
second such example was found by Harper [8]: he showed Z[
√
14] is Euclidean in 2004.
The ring Z[
√
14] was known to be a PID since the 19th century, and was known not to be
norm-Euclidean since the early 20th century. Here is a proof of that last statement.
Theorem 5.8. The ring Z[
√
14] is not norm-Euclidean.
Proof. We will show a speciﬁc equation can’t be solved in Z[
√
14]: 1 +
√
14 = 2γ + ρ where
| N(ρ)| < | N(2)| = 4. Assume this has a solution γ = m + n
√
14 and ρ = a + b
√
14 in
Z[
√
14], so
1 +
√
14 = (2m + a) + (2n + b)
√
14 =⇒a = 1 −2m, b = 1 −2n,
which means we’d want |(1 −2m)2 −14(1 −2n)2| < 4, so
(2m −1)2 −14(2n −1)2 = 0, ±1, ±2, ±3.
The left side is odd, so the right is ±1 or ±3.
Since odd numbers square to 1 mod 8,
(2m −1)2 −14(2n −1)2 ≡1 −14 ≡3 mod 8, and the numbers ±1 and ±3 are distinct mod
8, so
(2m −1)2 −14(2n −1)2 = 3.
Reducing this modulo 7, we get 3 ≡□mod 7, which is false. We have a contradiction.
□
Because Harper showed Z[
√
14] is Euclidean, the signiﬁcance of Theorem 5.8 is that
Z[
√
14] is not Euclidean for the speciﬁc function d(α) = | N(α)| even though Z[
√
14] is
Euclidean for another function, which is described in the accepted answer on the page
https://math.stackexchange.com/questions/1148364.
It is known that there are only ﬁnitely many norm-Euclidean quadratic rings.3 In con-
trast, it is believed that there are inﬁnitely many Euclidean quadratic rings, but that remains
an open problem. Harper gave a suﬃcient condition in terms of “two admissible primes”
(see [8, Theorem B]) for a real quadratic ring that is a PID to be Euclidean, and he checked
this condition is satisﬁed in many examples besides Z[
√
14] (such as Z[
√
22], Z[
√
23], and
Z[(1+
√
61)/2]). The method was extended to some inﬁnite families of real quadratic rings:
see [12] and [17]. Narkiewicz [14] used similar techniques to show every real quadratic ring
that is a PID must be Euclidean with at most two exceptions (it is believed there are no
exceptions). It is expected, but yet proved, that inﬁnitely many real quadratic rings are
PIDs, while it is known that only 9 imaginary quadratic rings are PIDs.4
The rest of this handout is concerned with setting up the background to present (i) many
quadratic rings that are not PIDs, and thus are not Euclidean (Theorem 5.11) and (ii) two
rings that each are a PID but are not Euclidean (Theorems 5.22 and 5.23), so the collection
of PIDs strictly contains the collection of Euclidean domains.
3See https://math.stackexchange.com/questions/2710457/norm-euclidean-fields.
4See https://en.wikipedia.org/wiki/Class number problem.

<!-- page 10 -->
10
KEITH CONRAD
In order to show some integral domain is not a PID, one method is to exhibit an explicit
example of an ideal in it that is not principal. It can be tricky to ﬁnd such an ideal. After
all, an ideal could be principal even if it is initially deﬁned using more than one generator,
e.g., in Z we have (6, 15) = (3). A more subtle way to show an integral domain R is not
a PID is to prove R fails to have a property that all PIDs have. We are going to describe
such a property now. It is a generalization of the rational roots theorem in Z[t], which says
that a rational root of a monic polynomial in Z[t] is an integer5. The generalization is based
on the following lemma, which says ratios from a PID have a reduced form, like rational
numbers do.
Lemma 5.9. Let R be a PID and F be its fraction ﬁeld. Every element of F has a ratio
in reduced form: it is a ratio of relatively prime elements of R.
Proof. In F, pick a ratio a/b where a and b are in R and b ̸= 0. The ideal (a, b) in R is
principal, say (a, b) = (d). Since d acts as a gcd for a and b, removing this common factor
from a and b should turn the ratio a/b into a reduced form ratio.
Since a, b ∈(d), we have d | a and d | b: a = da′ and b = db′ for some a′ and b′ in R.
Then a/b = (da′)/(db′) = a′/b′. We’ll show a′/b′ is a reduced form ratio: from (a, b) = (d),
d = ax + by for some x and y in R, so
d = ax + by = da′x + db′y = d(a′x + b′y) =⇒1 = a′x + b′y.
Thus the only common factors of a′ and b′ in R are units: a′ and b′ are relatively prime.
□
Theorem 5.10. Let R be a PID and F be its fraction ﬁeld. For a monic polynomial f(t)
in R[t], a root of f(t) in F must be in R.
Proof. By Lemma 5.9, a root of f(t) in F can be written in reduced form as a/b where a
and b are relatively prime in R.
Write f(t) = tn + cn−1tn−1 + · · · + c1t + c0 with n ≥1, so
0 = f(a/b) = an
bn + cn−1
an−1
bn−1 + · · · + c1
a
b + c0.
Multiply through by bn to clear the denominator:
0 = an + cn−1an−1b + · · · + c1abn−1 + c0bn.
Every term on the right side after an is divisible by b, so b | an. Since a and b are relatively
prime and R is a PID, from b | an we get b | 1, so b ∈R×.6 Thus a/b = ab−1 ∈R.
□
We now have a suﬃcient (but not necessary!) condition for Z[√m] not to be a PID.
Theorem 5.11. If m is an integer that is not a square and has a repeated prime factor,
then Z[√m] is not a PID.
Proof. Let p be a prime such that p2 | m, so m = p2m′. Since
√
m′ = √m/p,
√
m′ is in
the fraction ﬁeld of Z[√m] and is not in Z[√m]. Then f(t) = t2 −m′, which is monic in
Z[t] ⊂Z[√m][t], has the root
√
m′ in the fraction ﬁeld of Z[√m] that is not in Z[√m]. By
Theorem 5.10, Z[√m] is not a PID.
□
5The full form of the rational roots theorem says every rational root of a nonconstant polynomial cntn +
cn−1tn−1 + · · · + c1t + c0 ∈Z[t], where cn ̸= 0, has reduced form a/b where b | cn and a | c0. If cn = 1 then
b = ±1, so a/b = ±a is an integer.
6If R is not a PID, then we could have b | an where a and b are relatively prime and b ̸∈R×. An example
is R = Z[
√
5] with a = 2 and b = 1 +
√
5: b | a2 and the only common factors of a and b are in R are units.

<!-- page 11 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
11
Example 5.12. The rings Z[
√
12] = Z[2
√
3], Z[
√
8] = Z[2
√
2], and Z[
√
18] = Z[3
√
2] are
not PIDs.
An integral domain R with the property of Theorem 5.10 (namely for each monic poly-
nomial in R[t], a root of it in the fraction ﬁeld of R must be in R itself) is called integrally
closed, so Theorem 5.11 says every PID is an integrally closed domain, and thus integral
domains that are not integrally closed can’t be PIDs (which is how we found the rings in
Example 5.12). We have the following containments for three types of integral domains:
Euclidean domains ⊂PIDs ⊂integrally closed domains.
These containments are strict: Z[(1 + √−19)/2] is a PID and not Euclidean, as we’ll see in
Theorem 5.22, and Z[√−5] is integrally closed and not a PID.
Remark 5.13. For m as in Theorem 5.11, we showed Z[√m] is not a PID without giving
an explicit example of a nonprincipal ideal in Z[√m]. Such an ideal can be written down:
I = (p, √m), where p is a prime that divides m at least twice (such p exists since m is not
squarefree). Why isn’t I principal? It can be shown that I = Zp + Z√m as an additive
group, and comparing this to Z[√m] = Z + Z√m shows [Z[√m] : I] = p. It turns out
principal ideals in Z[√m] can’t have index p, as follows. For a nonzero principal ideal (α),
it can be shown that [Z[√m] : (α)] = | N(α)|,7 so if a principal ideal (α) has index p then
N(α) = ±p. Writing α as a + b√m for a and b in Z, we’d have a2 −mb2 = ±p. Since p | m
we have p | a2, so p | a. Then p2 | a2, and p2 | m by assumption, so a2 −mb2 is a multiple
o p2, which contradicts it being ±p. Thus the ideal (p, √m) in Z[√m] is not principal.
We turn next to examples of PIDs that are not Euclidean. The rings we’ll show have
this property are the quadratic ring Z[(1 + √−19)/2] and the quotient polynomial ring
R[x, y]/(x2 + y2 −1).
Theorem 5.14. In a quadratic ring Z[γ], the units are the elements with norm ±1.
Proof. If αβ = 1 in Z[γ] then taking norms shows N(α) N(β) = N(1) = 1 in Z, so N(α) = ±1.
Conversely, if N(α) = ±1 then αα = ±1, so α is invertible (with inverse ±α).
□
Example 5.15. The units of Z[
√
2] are built from integral solutions to x2 −2y2 = ±1. For
instance, one solution is x = 1 and y = 1, giving the unit 1 +
√
2. Its powers are also units
(units are closed under multiplication), so Z[
√
2] has inﬁnitely many units.
Example 5.16. Units in Z[
√
3] come from integral solutions to x2 −3y2 = ±1. However,
there are no solutions to x2 −3y2 = −1 since the equation has no solutions modulo 3:
x2 ≡−1 mod 3 has no solution. Thus the units of Z[
√
3] only correspond to solutions to
x2 −3y2 = 1. One nontrivial solution (that is, other than ±1) is x = 2 and y = 1, which
yields the unit 2 +
√
3. Its powers give inﬁnitely many more units.
Example 5.17. The units of Z[√−2] come from integral solutions to x2 + 2y2 = 1. The
right side is at least 2 once y ̸= 0, so the only integral solutions are x = ±1 and y = 0,
corresponding to the units ±1. In contrast to the previous two examples, where there are
inﬁnitely many units, Z[√−2] has only two units.
The following theorem about Euclidean domains is the key to proving later that certain
integral domains are not Euclidean. Notice the proof does not require the Euclidean function
on the ring to satisfy the d-inequality initially.
7See Example 5.20 in https://kconrad.math.uconn.edu/blurbs/linmultialg/modulesoverPID.pdf.

<!-- page 12 -->
12
KEITH CONRAD
Theorem 5.18. Let R be a Euclidean domain that is not a ﬁeld. There is a ∈R such that
R/(a) is represented by 0 and units of R.
Proof. Since R is not a ﬁeld, there are elements of R that are not 0 or a unit. Let d be the
Euclidean function on R. Pick a ∈R such that a is not 0 or a unit and d(a) is minimal
among such numbers. For each x ∈R, x = aq + r for some q and r in R where r = 0 or
d(r) < d(a). If r ̸= 0, then the inequality d(r) < d(a) forces r to be a unit of R. Since
x ≡r mod a, we conclude that R/(a) is represented by 0 and by units of R.
□
Remark 5.19. We can make the a in Theorem 2.1 irreducible: change the Euclidean
function d if necessary so that it satisﬁes the d-inequality (Theorem 2.1). For this d, an a
with minimal d-value among nonzero nonunits of R is irreducible, since if a were reducible,
then a = bc for some nonunits b and c and d(b) < d(bc) = d(a) by Corollary 3.3. That
contradicts the minimality of d(a) among nonzero nonunits of R.
Example 5.20. When R = Z we can use a = 2. Then Z/2Z is represented by 0 and 1, or
by 0 and −1. When R = Z[i] we can use a = 1 + i. Then Z[i]/(1 + i) is represented by 0
and 1 as well as by 0 and i. These examples show some units could be congruent to each
other modulo a, but at least every element of the ring is congruent modulo a to 0 or some
(perhaps more than one) unit.
We have shown that if R is a Euclidean domain that is not a ﬁeld, then there is an
element of R (namely a nonunit with least d-value) modulo which everything is congruent
to 0 or a unit from R. A domain that’s not a ﬁeld and which has no element modulo which
everything is congruent to 0 or a unit from R therefore can’t be a Euclidean domain.
Remark 5.21. In a domain R, an element a that is not 0 or a unit and for which the ring
R/(a) is represented by 0 and units in R is called a universal side divisor in the literature.
This terminology seems strange. What’s a side divisor? Remember the property, but forget
the label (and don’t use it, because nobody will know what you’re talking about).8
Theorem 5.22. The quadratic ring R = Z[(1 + √−19)/2] is a PID and not Euclidean.
Proof. We will only sketch the proof that R is a PID. Here are two methods.
• It can be shown that for all nonzero x and y in R, y | x or 0 < N(ax + by) < N(y),
where N is the norm map on R. This property of R implies it is a PID by a slight
modiﬁcation of the proof that a Euclidean domain is a PID. For further details, see
[4, p. 282] or [19, Sect. 2].
• Using algebraic number theory (the “Minkowski bound”), if R has a nonprincipal
ideal then it has a nonprincipal ideal whose index in R is less than 2
√
19/π ≈2.7,
so the index has to be 2 (the index can’t be 1, since an ideal with index 1 is R = (1),
which is principal). It can be shown that R has no ideal with index 2, principal or
nonprincipal, because (1 + √−19)/2 is a root of X2 −X + 5 and X2 −X + 5 mod 2
has no roots in Z/(2). The details justifying that can be found in algebraic number
theory texts where class numbers are computed (R has class number 1).
To prove R is not Euclidean (this is stronger than R not being norm-Euclidean!) we ﬁrst
note R is not a ﬁeld since Z ⊂R but 1/2 ̸∈R (in fact, R ∩Q = Z). Therefore to prove
8The terms “side divisor” and “universal side divisor” are due to Motzkin [13]. In an integral domain R,
he called a a side divisor of b if a is not 0 or a unit and a | (b −u) for some u ∈R×. This means b mod a is
represented by a unit of R. A universal side divisor in A is an a ∈A that is a side divisor of every b ∈A.

<!-- page 13 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
13
R is not Euclidean we will show R doesn’t satisfy the conclusion of Theorem 5.18: for no
nonunit a ∈R is R/(a) represented by 0 and units.
First we compute the norm of a typical element α = x + y(1 + √−19)/2:
(5.1)
N(α) = x2 + xy + 5y2 =

x + y
2
2
+ 19y2
4
.
This norm always takes values ≥0 (this is clearer from the second expression for it than
the ﬁrst) and once y ̸= 0 we have N(α) ≥19y2/4 ≥19/4 > 4. In particular, the units are
solutions to N(α) = 1, which are ±1:
R× = {±1}.
The ﬁrst few norm values are 0, 1, 4, 5, 7, and 9. In particular, there is no element of R
with norm 2 or 3. This and the fact that R× ∪{0} has size 3 are the key facts we will use.
If R were Euclidean then there would be a nonunit a in R such that R/(a) is represented
by 0 and units, so by 0, 1, or −1. Perhaps 1 ≡−1 mod a, but we deﬁnitely have ±1 ̸≡
0 mod a (since a is not a unit, (a) is a proper ideal so R/(a) is not the zero ring). Thus
R/(a) has size 2 (if 1 ≡−1 mod a) or 3 (if 1 ̸≡−1 mod a). We show this can’t happen.
If R/(a) has size 2 then 2 ≡0 mod a (think about R/(a) as an additive group of size 2),
so a | 2 in R. Therefore N(a) | 4 in Z. There are no elements of R with norm 2, so the only
nonunits with norm dividing 4 are elements with norm 4. A check using (5.1) shows the
only such numbers are ±2. However, R/(2) = R/(−2) does not have size 2: it has size 4,
since R ∼= Z2 as an abelian group implies R/2R ∼= (Z/2Z)2.
Similarly, if R/(a) has size 3 then a | 3 in R, so N(a) | 9 in Z. There is no element of R
with norm 3, so a must have norm 9 (it doesn’t have norm 1 since it is not a unit). The
only elements of R with norm 9 are ±3, so a = ±3. The ring R/(3) = R/(−3) does not
have size 3: its size is 9 since R/3R ∼= (Z/3Z)2.
Since R× ∪{0} has size 3 and R has no element a such that R/(a) has size 2 or 3, R
can’t be a Euclidean domain.
□
Theorem 5.23. The ring R = R[x, y]/(x2 + y2 + 1) is a PID and not Euclidean.
Proof. To prove R is a PID, there are four steps. Our argument is based on https://math.
stackexchange.com/questions/864212.
Step 1: The ring R is an integral domain.
The polynomial x2 + y2 + 1 is irreducible in the UFD R[x, y] since, as a polynomial in y,
it is Eisenstein at x2 + 1. Therefore the ideal (x2 + y2 + 1) in R[x, y] is prime.
Step 2: Every nonzero prime ideal in R is a maximal ideal.
Since R = R[x, y]/(x2 + y2 + 1), each ideal in R has the form I/(x2 + y2 + 1) where I is
an ideal of R[x, y] that contains (x2 + y2 + 1), and
R/(I/(x2 + y2 + 1)) = (R[x, y]/(x2 + y2 + 1))/(I/(x2 + y2 + 1)) ∼= R[x, y]/I.
Thus each nonzero prime ideal p of R has the form P/(x2 + y2 + 1) for a prime ideal P in
R[x, y] strictly containing (x2 + y2 + 1), so R/p ∼= R[x, y]/P. The prime ideal P in R[x, y]
is maximal, since it can be shown that if P1 ⊊P2 is a tower of two nonzero prime ideals in
R[x, y] then the larger ideal P2 is maximal.9 Therefore P/(x2 + y2 + 1) is maximal in R.
Step 3: Every maximal ideal in R is a principal ideal.
9This is true for prime ideals in F[x, y] when F is an arbitrary ﬁeld, not just R.

<!-- page 14 -->
14
KEITH CONRAD
Let m be a maximal ideal in R, so m = M/(x2 + y2 + 1) where M is a maximal ideal
in R[x, y]. The ﬁeld R/m ∼= R[x, y]/M is ﬁnitely generated as a ring over R (with two
generators – the images of x and y in the quotient ring). Zariski’s lemma10 says that when
a ﬁeld L is ﬁnitely generated as a ring over a subﬁeld K, L is ﬁnite-dimensional as a K-vector
space. Therefore R/m is ﬁnite-dimensional over R.
The only ﬁelds that are ﬁnite-dimensional over R are R and C, since C is algebraically
closed. The relation x2+y2+1 = 0 in R implies x2+y2+1 = 0 in R/m, where x = x mod m
and y = y mod m. Therefore R/m is larger than R, which means R/m is isomorphic as a
ﬁeld to C. Under this isomorphism, let x 7→z and y 7→w for complex numbers z and w
such that z2 +w2 +1 = 0. Obviously z and w can’t both be real. Without loss of generality,
suppose z is not real. Then w = a + bz for some a, b ∈R, so y = a + bx in R/m, which
means y −a −bx vanishes in in R/m ∼= R[x, y]/M. Thus (y −a −bx, x2 + y2 + 1) ⊂M in
R[x, y]. Check (y−a−bx, x2+y2+1) is maximal in R[x, y], so M = (y−a−bx, x2+y2+1).
Reducing to the ring R = R[x, y]/(x2 + y2 + 1), m = (y −a −bx), which is principal.
Step 4: Every ideal in R is a principal ideal, so R is a PID.
By Steps 2 and 3, all nonzero prime ideals of R are principal. Therefore all prime ideals
of R are principal (the zero ideal (0) is principal, whether or not (0) is a prime ideal). It
can be shown with Zorn’s lemma that if all prime ideals in a commutative ring are principal
then all ideals are principal.11 Therefore by Steps 2 and 3, all ideals in R are principal.
(Note this reasoning is very nonconstructive.) Since R is an integral domain in which all
ideals are principal, R is a PID.
To prove R is not Euclidean, there are three steps and they do not depend on knowing R
is a PID. We’ll compute the units of R and show the property of Euclidean domains related
to their units in Theorem 5.18 is not satisﬁed by R.
Step 1: Give a standard way to write elements of R.
In R[x, y] = R[x][y], x2 + y2 + 1 = y2 + (x2 + 1) is a monic polynomial in y of degree
2. Therefore we can do division by y2 + x2 + 1 with remainder in R[x, y]: each element of
R[x, y] has the unique form (y2 + x2 + 1)q(x, y) + (a(x) + b(x)y), so R[x, y]/(x2 + y2 + 1)
has representatives a(x) + b(x)y for a(x) and b(x) in R[x]. Since y2 = −1 −x2 in R, we can
think of R as R[x] + R[x]
√
−1 −x2.
Step 2: The units in R are nonzero constants: R× = R×.
Clearly R× ⊂R×. To prove R× ⊂R× use the norm function N: R →R[x] where
N(f(x) + g(x)
p
−1 −x2)
=
(f(x) + g(x)
p
−1 −x2)(f(x) −g(x)
p
−1 −x2)
=
f(x)2 + (x2 + 1)g(x)2.
This is a multiplicative function, so a unit in R must have a norm that’s a unit in R[x],
meaning the norm is in R×. In f(x)2 + (x2 + 1)g(x)2, the leading coeﬃcient of each term is
positive if the term is not 0, so the only way such an expression can be in R× is if g(x) = 0
and f(x) ∈R×, making f(x) + g(x)
√
−1 −x2 = f(x) ∈R×.
Step 3: Show R does not ﬁt the conclusion of Theorem 5.18.
If R were a Euclidean domain then there would be a nonunit a ∈R such that R/(a) is
represented by 0 and units from R, which are the elements of R. So the composite of natural
ring homomorphisms R →R[x] →R →R/(a) is surjective, and thus an isomorphism since
R is a ﬁeld (homomorphisms from a ﬁeld to a nonzero ring are always injective). Letting
10See Theorem 2.11 in https://kconrad.math.uconn.edu/blurbs/ringtheory/maxideal-polyring.pdf.
11See Theorem 3.6 and the exercise after it in https://kconrad.math.uconn.edu/blurbs/zorn1.pdf.

<!-- page 15 -->
REMARKS ABOUT EUCLIDEAN DOMAINS
15
x ≡α mod (a) and y ≡β mod (a) for α, β ∈R, the equation x2 + y2 + 1 = 0 in R implies
α2 + β2 + 1 = 0 in R, which is impossible.
□
References
[1] S. Alaca and K. S. Williams, “Introductory Algebraic Number Theory,” Cambridge Univ. Press, 2003.
[2] D. A. Clark, A quadratic ﬁeld which is Euclidean but not norm-Euclidean, Manuscripta Math. 83 (1994),
327–330.
[3] C. Conidis, P. P. Nielsen, and V. Tombs, Transﬁnitely valued Euclidean domains have arbitrary indecom-
posable order type, Comm. Algebra 47 (2019), 1105–1113. URL https://arxiv.org/abs/ 1703.02631.
[4] D. Dummit and R. Foote, “Abstract Algebra,” 3rd ed., Wiley, 2004.
[5] J. Durbin, “Modern Algebra: An Introduction,” 5th ed., J. Wiley, 2004.
[6] J. B. Fraleigh, “A First Course in Abstract Algebra,” 6th ed., Addison-Wesley, 1999.
[7] F. Goodman, “Algebra: Abstract and Concrete (Stressing Symmetry),” 2nd ed., Prentice-Hall, 2005.
[8] M. Harper, Z[
√
14] is Euclidean, Canad. J. Math. 56 (2004), 55–70.
[9] I. Herstein, “Topics in Algebra,” 2nd ed., Wiley, 1975.
[10] T. Hungerford, “Algebra,” Springer-Verlag, 1980.
[11] M. A. Jodeit, Uniqueness in the division algorithm, Amer. Math. Monthly 74 (1967), 835–836.
[12] R. M. Murty, K. Srinivas, and M. Subramani, Admissible primes and Euclidean quadratic ﬁelds, J.
Ramanujan Math. Soc. 33 (2018), 135–147.
[13] T. Motzkin, The Euclidean algorithm, Bull. Amer. Math. Soc. 38 (1949), 1142–1146.
[14] W. Narkiewicz, Euclidean algorithm in small abelian ﬁelds, Funct. Approx. Comment. Math. 37 (2007),
337–340.
[15] T. S. Rhai, A characterization of polynomial domains over a ﬁeld, Amer. Math. Monthly 69 (1962),
984–986.
[16] J. Rotman, “Advanced Modern Algebra,” Prentice-Hall, 2002.
[17] K. Srinivas and M. Subramani, On admissible sets of primes in real quadratic ﬁelds, pp. 227–233 in
“Modular forms and related topics,” Springer, Singapore, 2020.
[18] B. L. van der Waerden, “Modern Algebra,” Ungar, New York, 1953.
[19] J. C. Wilson, A principal ideal ring that is not a Euclidean ring, Math. Mag. 46 (1973), 34–38.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*