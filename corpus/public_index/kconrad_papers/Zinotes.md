# Gaussian Integers

> **Source**: https://kconrad.math.uconn.edu/blurbs/Zinotes.pdf  
> **Author**: Keith Conrad  
> **Topic**: number_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE GAUSSIAN INTEGERS
KEITH CONRAD
Since the work of Gauss, number theorists have been interested in analogues of Z where
concepts from arithmetic can also be developed. The example we will look at here is the
Gaussian integers, introduced by Gauss in 1832 [1]:
Z[i] = {a + bi : a, b ∈Z}.
Excluding the last two sections, the topics we will study are extensions of common prop-
erties of the integers. Here is what we will cover in each section:
(1) The norm
(2) Divisibility in Z[i]
(3) The division algorithm in Z[i]
(4) The Euclidean algorithm in Z[i]
(5) Bezout’s theorem in Z[i]
(6) Unique factorization in Z[i]
(7) Modular arithmetic in Z[i]
(8) Applying Z[i] to Z
(9) Primes in Z[i]
1. The Norm
In Z, size is measured by the absolute value. In Z[i], we use the norm.
Deﬁnition 1.1. For α = a + bi ∈Z[i], its norm is the product
N(α) = αα = (a + bi)(a −bi) = a2 + b2.
For example, N(2 + 7i) = 22 + 72 = 53. For m ∈Z, N(m) = m2. In particular, N(1) = 1.
Thinking about a + bi as a complex number, its norm is the square of its usual absolute
value:
|a + bi| =
p
a2 + b2,
N(a + bi) = a2 + b2 = |a + bi|2.
The reason we prefer to deal with norms on Z[i] instead of absolute values on Z[i] is that
norms are integers (rather than square roots), and the divisibility properties of norms in Z
will provide important information about divisibility properties in Z[i]. This is based on
the following algebraic property of the norm.
Theorem 1.2. The norm is multiplicative: for α and β in Z[i], N(αβ) = N(α) N(β).
Proof. Write α = a+bi and β = c+di. Then αβ = (ac−bd)+(ad+bc)i. We now compute
N(α) N(β) and N(αβ):
N(α) N(β) = (a2 + b2)(c2 + d2) = (ac)2 + (ad)2 + (bc)2 + (bd)2
1

<!-- page 2 -->
2
KEITH CONRAD
and
N(αβ) = (ac −bd)2 + (ad + bc)2
= (ac)2 −2abcd + (bd)2 + (ad)2 + 2abcd + (bc)2
= (ac)2 + (bd)2 + (ad)2 + (bc)2.
The two results agree, so N(αβ) = N(α) N(β).
□
Remark 1.3. The calculations above work when the integer coeﬃcients are rational or
even real. If for a complex number z = x + yi with x, y ∈R we deﬁne N(z) = x2 + y2 then
N(zw) = N(z) N(w) for all z and w in C. This will be used in the proof of Theorem 3.1.
As a ﬁrst application of Theorem 1.2, we determine the Gaussian integers with a multi-
plicative inverse in Z[i]. The idea is to apply norms to reduce the question to invertibility
in Z.
Corollary 1.4. The only Gaussian integers that are invertible in Z[i] are ±1 and ±i.
Proof. It is easy to see ±1 and ±i have inverses in Z[i]: 1 and −1 are their own inverse and
i and −i are inverses of each other.
For the converse direction, suppose α ∈Z[i] is invertible, say αβ = 1 for some β ∈Z[i].
We want to show α ∈{±1, ±i}. Taking the norm of both sides of the equation αβ = 1,
we ﬁnd N(α) N(β) = 1. This is an equation in Z, so we know N(α) = ±1. Since the norm
doesn’t take negative values, N(α) = 1. Writing α = a + bi, we have a2 + b2 = 1, and the
integral solutions to this give us the four values α = ±1, ±i.
□
Invertible elements are called units. The units of Z are ±1. The units of Z[i] are ±1 and
±i. Knowing a Gaussian integer up to multiplication by a unit is analogous to knowing an
integer up to its sign.
While there is no such thing as inequalities on Gaussian integers, we can talk about
inequalities on their norms. In particular, induction on the norm (not on the Gaussian
integer itself) is a technique to bear in mind if you want to prove something by induction
in Z[i]. We will use induction on the norm to prove unique factorization (Theorems 6.4 and
6.6).
The norm of every Gaussian integer is a non-negative integer, but it is not true that every
non-negative integer is a norm. Indeed, the norms are the integers of the form a2 + b2, and
not every positive integer is a sum of two squares. Examples include 3, 7, 11, 15, 19, and
21. No Gaussian integer has norm equal to these values.
2. Divisibility in Z[i]
Divisibility in Z[i] is deﬁned in the natural way: we say β divides α (and write β | α) if
α = βγ for some γ ∈Z[i]. In this case, we call β a divisor or a factor of α.
Example 2.1. Since 14 + 3i = (4 −5i)(1 + 2i), 4 −5i divides 14 + 3i.
Example 2.2. Does (4 + 5i) | (14 + 3i)? We can do the division by taking a ratio and
rationalizing the denominator:
14 + 3i
4 + 5i = (14 + 3i)(4 −5i)
(4 + 5i)(4 −5i) = 71 −58i
41
= 71
41 −58
41i.
This is not in Z[i]: the real and imaginary parts are 71/41 and −58/41, which are not
integers. Therefore 4 + 5i does not divide 14 + 3i in Z[i].

<!-- page 3 -->
THE GAUSSIAN INTEGERS
3
Theorem 2.3. A Gaussian integer α = a + bi is divisible by an ordinary integer c if and
only if c | a and c | b in Z.
Proof. To say c | (a + bi) in Z[i] is the same as a + bi = c(m + ni) for some m, n ∈Z, and
that is equivalent to a = cm and b = cn, or c | a and c | b.
□
Taking b = 0 in Theorem 2.3 tells us divisibility between ordinary integers does not
change when working in Z[i]: for a, c ∈Z, c | a in Z[i] if and only if c | a in Z. However, this
does not mean other aspects in Z stay the same. For instance, we will see later (Section 6)
that some primes in Z factor in Z[i].
The multiplicativity of the norm turns divisibility relations in Z[i] into divisibility rela-
tions in the more familiar setting of Z, as follows.
Theorem 2.4. For α, β in Z[i], if β | α in Z[i] then N(β) | N(α) in Z.
Proof. Write α = βγ for γ ∈Z[i].
Taking the norm of both sides, we have N(α) =
N(β) N(γ). This equation is in Z, so it shows N(β) | N(α) in Z.
□
Corollary 2.5. A Gaussian integer has even norm if and only if it is a multiple of 1 + i.
Proof. Since N(1 + i) = 2, any multiple of 1 + i in Z[i] has even norm. Conversely, suppose
m + ni has even norm. Then m2 + n2 ≡0 mod 2. If m ̸≡n mod 2 then m2 + n2 ≡1 mod 2,
so m ≡n mod 2.
We want to write m + ni = (1 + i)(u + vi) for some u, v ∈Z. This is the same as
m + ni = (u −v) + (u + v)i.
This only happens when solution u = (n + m)/2 and v = (n −m)/2, which are integers
since m ≡n mod 2. Thus (1 + i) | (m + ni).
□
Example 2.6. The norm of 1 + 3i is 10, and 1 + 3i = (1 + i)(2 + i).
Example 2.7. Since 1 −i has norm 2, it must be a multiple of 1 + i. Indeed, 1 −i =
(−i)(1 + i).
Theorem 2.4 is useful as a quick way of showing one Gaussian integer does not divide
another: check the corresponding norm divisibility is not true in Z. For example, if (3+7i) |
(10 + 3i) in Z[i], then (taking norms), 58 | 109 in Z, but that isn’t true. Therefore 3 + 7i
does not divide 10 + 3i in Z[i]. Turning a divisibility problem in Z[i] into one in Z has an
obvious appeal, since we are more comfortable with divisibility in Z.
However, Theorem 2.4 only says norm-divisibility in Z follows from divisibility in Z[i].
The converse is usually false. Consider α = 14 + 3i and β = 4 + 5i. While N(β) = 41 and
N(α) = 205 = 41·5, so N(β) | N(α) in Z, we saw in Example 2.2 that 4+5i does not divide
14 + 3i.
The foolproof method of verifying divisibility in Z[i] is testing if the ratio is in Z[i] after
rationalizing the denominator, as we did in Example 2.2. The norm-divisibility check in Z
is a necessary condition for divisibility in Z[i] (when it fails, so does divisibility in Z[i]), but
it is not suﬃcient.
In Z, if |m| = |n| then m = ±n, so m and n are unit multiples of each other. The
corresponding statement in Z[i] is false: if N(α) = N(β) it is not generally true that α and
β are unit multiples of each other. Consider 4 + 5i and 4 −5i. Both have norm 41, but the
unit multiples of 4 + 5i are
4 + 5i,
−4 −5i,
−5 + 4i,
5 −4i.

<!-- page 4 -->
4
KEITH CONRAD
The number 4 −5i is not on this list, so 4 + 5i and 4 −5i are not unit multiples. We will
see later (Example 4.5) that 4 + 5i and 4 −5i are even relatively prime in Z[i]. In short,
taking the norm in Z[i] is a more drastic step than removing a sign on an integer.
3. The Division Algorithm in Z[i]
One reason we will be able to transfer a lot of results from Z to Z[i] is the following
analogue of division-with-remainder in Z.
Theorem 3.1 (Division Algorithm). For α, β ∈Z[i] with β ̸= 0, there are γ, ρ ∈Z[i] such
that α = βγ + ρ and N(ρ) < N(β). In fact, we can choose ρ so N(ρ) ≤(1/2) N(β).
The numbers γ and ρ are the quotient and remainder, and the remainder is bounded in
size (according to its norm) by the size of the divisor β.
There is a subtlety in trying to calculate γ and ρ in Theorem 3.1 that is best understood
by working through an example.
Example 3.2. Let α = 27 −23i and β = 8 + i. The norm of β is 65. We want to write
α = βγ + ρ where N(ρ) < 65. The idea is to consider the ratio α/β and rationalize the
denominator:
(3.1)
α
β = αβ
ββ = (27 −23i)(8 −i)
65
= 193 −211i
65
.
Since 193/65 = 2.969 . . . and −211/65 = −3.246 . . . , replace each fraction with its greatest
integer and try γ = 2 −4i. However,
α −β(2 −4i) = 7 + 7i,
so α = βγ + ρ where ρ = 7 + 7i and this is bad: N(ρ) = 98 > N(β) = 65. The usefulness
of a division algorithm is the smaller remainder: we want N(ρ) < N(β), so our choice of γ
and ρ is not desirable. This is the subtlety referred to before starting this example.
To correct our approach, we have to think more carefully about the way we replace
193/65 = 2.969 . . . and −211/65 = −3.246 . . . with nearby integers. Notice that 193/65
and −211/65 are each closer to the integer to their right rather than to their left. That
is, 193/65 is closer to 3 than to 2, and −211/65 is closer to −3 than to −4. Let’s use the
nearest integer rather than the greatest integer: try γ = 3 −3i. Then
α −β(3 −3i) = −2i,
so α = βγ + ρ where γ = 3 −3i and ρ = −2i, so N(ρ) = 4 < N(β) = 65.
Choosing the nearest integer rather than the greatest integer could also be done in Z.
For instance, 34/9 = 3.77 . . . is closer to 4 than to 3. In terms of a division-with-remainder
equation, this corresponds to preferring
34 = 9 · 4 −2
over
34 = 9 · 3 + 7.
The remainder in the ﬁrst equation is negative, but it is smaller in absolute value. In fact,
by letting bq be the multiple of b that is nearest to a in Z, we get |a −bq| ≤|b|/2, which is
a sharper bound than |b| at the cost of a −bq possibly being negative. And if a lies exactly
between two multiples of b, then there are two integers equally nearest to a/b, which makes

<!-- page 5 -->
THE GAUSSIAN INTEGERS
5
the quotient and remainder not unique when making |a −bq| ≤|b|/2, e.g., if a = 27 and
b = 6 then a is exactly between b(4) and b(5):
27 = 6 · 4 + 3,
27 = 6 · 5 −3.
Thus we get two choices of r, either 3 or −3. Potentially losing uniqueness of the quotient
and remainder in Z might seem like a calamity, but the analogue of this in Z[i] will let us
prove a division algorithm there now.
Proof. (of Theorem 3.1) We have α, β ∈Z[i] with β ̸= 0 and we want to construct γ, ρ ∈Z[i]
such that α = βγ + ρ where N(ρ) ≤(1/2) N(β).
Write
α
β = αβ
ββ =
αβ
N(β) = x + yi
where x and y are rational (divide the real and imaginary parts of αβ by N(β)). Let q1 and
q2 be the integers nearest to x and y, so |x −q1| ≤1/2 and |y −q2| ≤1/2. Set γ = q1 + q2i,
so γ ∈Z[i] and
α
β −γ = (x + yi) −(q1 + q2i)
= (x −q1) + (x −q2)i.
Take the norm of both sides:
N
α
β −γ

= (x −q1)2 + (x −q2)2 ≤1
4 + 1
4 = 2
4 = 1
2.
Multiply through by N(β): since the norm on Q[i] is multiplicative (Remark 1.3),
N(α −βγ) ≤1
2 N(β).
Thus by setting ρ = α −βγ, we have ρ ∈Z[i], α = βγ + ρ, and N(ρ) ≤(1/2) N(β).
□
Example 3.3. Let α = 11 + 10i and β = 4 + i. Then N(β) = 17. We compute
α
β =
αβ
N(β) = 54 + 29i
17
.
Since 54/17 = 3.17 . . . and 29/17 = 1.70 . . . , by using nearest integers set γ = 3 + 2i. Then
α −βγ = 1 −i, so set ρ = 1 −i and get α = βγ + ρ with N(ρ) = 2 ≤(1/2) N(β) = 8.5.
Example 3.4. Let α = 37 + 2i and β = 11 + 2i, so N(β) = 125 and
α
β = αβ
125 = 411 −52i
125
Since 411/125 = 3.288 and −52/125 = −.416, use γ = 3 + 0i = 3. Then α −βγ = 4 −4i,
so use ρ = 4 −4i:
α = β · 3 + (4 −4i).
and N(4 −4i) = 32 ≤(1/2) N(β) = 62.5.
If we change γ to 3 −i we get another valid choice:
α = β(3 −i) + (2 + 7i)
and N(2 + 7i) = 53 ≤(1/2) N(β) = 62.5, so we can use ρ = 2 + 7i.

<!-- page 6 -->
6
KEITH CONRAD
Example 3.5. Let α = 1 + 8i and β = 2 −4i. Then
α
β =
αβ
N(β) = −30 + 20i
20
= −3
2 + i.
Since −3/2 lies exactly between −2 and −1, we can use γ = −1 + i or γ = −2 + i. Using
the ﬁrst choice, we obtain
α = β(−1 + i) −1 + 2i.
Using the second choice,
α = β(−2 + i) + 1 −2i.
Both times, N(ρ) = 5 ≤(1/2) N(β) = 10.
That the division algorithm in Z[i] lacks uniqueness in the quotient and remainder does
not seriously limit the usefulness of the division algorithm. Indeed, back in Z, the unique-
ness of the quotient and remainder for the usual division algorithm is irrelevant for many
important applications (such as Euclid’s algorithm). All those applications will carry over
to Z[i], with essentially the same proofs.
4. The Euclidean Algorithm in Z[i]
We begin by deﬁning greatest common divisors in Z[i].
Deﬁnition 4.1. For non-zero α and β in Z[i], a greatest common divisor of α and β is a
common divisor with maximal norm.
This is analogous to the usual deﬁnition of greatest common divisor in Z, except the
concept is not pinned down as a speciﬁc number. If δ is a greatest common divisor of α
and β, so are (at least) its unit multiples −δ, iδ, and −iδ. Perhaps there are other greatest
common divisors; we just don’t know yet. (We will ﬁnd out in Corollary 4.7.) We can
speak about a greatest common divisor, but not the greatest common divisor. A similar
technicality would occur in Z if we deﬁned the greatest common divisor as a common divisor
with largest absolute value, rather than the largest positive common divisor. There is no
analogue of positivity in Z[i] (at least not in this course), so we are stuck with the concept
of greatest common divisor always ambiguous at least by a unit multiple.
Deﬁnition 4.2. When α and β only have unit factors in common, we call them relatively
prime.
Theorem 4.3 (Euclid’s algorithm). Let α, β ∈Z[i] be non-zero. Recursively apply the
division algorithm , starting with this pair, and make the divisor and remainder in one
equation the new dividend and divisor in the next, provided the remainder is not zero:
α = βγ1 + ρ1,
N(ρ1) < N(β)
β = ρ1γ2 + ρ2,
N(ρ2) < N(ρ1)
ρ1 = ρ2γ3 + ρ3,
N(ρ3) < N(ρ2)
...
The last non-zero remainder is divisible by all common divisors of α and β, and is itself a
common divisor, so it is a greatest common divisor of α and β.

<!-- page 7 -->
THE GAUSSIAN INTEGERS
7
Proof. The proof is identical to the usual proof that Euclid’s algorithm works in Z. We
brieﬂy summarize the argument.
Reasoning from the ﬁrst equation down shows every
common divisor of α and β divides the last non-zero remainder.
Conversely, reasoning
from the ﬁnal equation up shows the last non-zero remainder (which is in the second-to-last
equation) is a common divisor of α and β. Therefore this last non-zero remainder is a
common divisor that is divisible by all the others. Thus it must have maximal norm among
the common divisors, so it is a greatest common divisor.
□
Example 4.4. We compute a greatest common divisor of α = 32 + 9i and β = 4 + 11i.
Details involved in carrying out the division algorithm in each step of Euclid’s algorithm
are omitted. The reader could work them out as more practice with the division algorithm
. We ﬁnd
32 + 9i = (4 + 11i)(2 −2i) + 2 −5i,
4 + 11i = (2 −5i)(−2 + i) + 3 −i,
2 −5i = (3 −i)(1 −i) −i,
3 −i = (−i)(1 + 3i) + 0.
The last non-zero remainder is −i, so α and β only have unit factors in common. They are
relatively prime. Notice that, unlike in Z+, when two Gaussian integers are relatively prime
we do not necessarily obtain 1 as the last non-zero remainder. Rather, we just obtain some
unit as the last non-zero remainder.
Example 4.5. We show 4 + 5i and 4 −5i, which are conjugates, are relatively prime in
Z[i]:
4 + 5i = (4 −5i)i −(1 −i)
4 −5i = −(1 −i)(−4) −i
−(1 −i) = −i(1 + i) + 0.
The last non-zero remainder is a unit, so we are done.
Example 4.6. Here’s an example where the greatest common divisor is not a unit. Let
α = 11 + 3i and β = 1 + 8i. Then
11 + 3i = (1 + 8i)(1 −i) + 2 −4i
1 + 8i = (2 −4i)(−1 + i) −1 + 2i
2 −4i = (−1 + 2i)(−2) + 0,
so a greatest common divisor of α and β is −1 + 2i.
We could proceed in a diﬀerent way in the second equation (which we already met in
Example 3.5), and get a diﬀerent last non-zero remainder:
11 + 3i = (1 + 8i)(1 −i) + 2 −4i
1 + 8i = (2 −4i)(−2 + i) + 1 −2i
2 −4i = (1 −2i)(2) + 0.
Therefore 1 −2i is also a greatest common divisor.
Our two diﬀerent answers are not
inconsistent: a greatest common divisor is deﬁned at best only up to a unit multiple anyway,
and −1 + 2i and 1 −2i are unit multiples of each other: −1 + 2i = (−1)(1 −2i).

<!-- page 8 -->
8
KEITH CONRAD
If δ is a greatest common divisor of α and β, then N(δ) divides N(α) and N(β), so N(δ)
divides (N(α), N(β)). However, it can happen that N(δ) < (N(α), N(β)). In Example 4.5,
α and β are relatively prime and hence their greatest common divisor has norm 1, but
N(α) = N(β) = 41. In Example 4.6, N(α) = 130 and N(β) = 65, which have greatest
common divisor 65, while α and β have a greatest common divisor −1+2i, which has norm
5.
Suppose (N(α), N(β)) = 1. Then any common divisor of α and β has norm dividing
1, so its norm must be 1, and thus the common divisor is a unit. We see that Gaussian
integers with relatively prime norm have to be relatively prime themselves. (Again, the
converse is false, as 4 ± 5i shows.) For instance, returning to Example 4.4, we compute
N(32 + 9i) = 1105 = 5 · 13 · 17 and N(4 + 11i) = 137 (a prime), which are relatively prime.
Since the norms are relatively prime in Z, 32+9i and 4+11i are relatively prime in Z[i]. We
could have avoided Euclid’s algorithm in Z[i] in this case, by using it in Z (on the norms)
ﬁrst.
But in general one needs Euclid’s algorithm in Z[i] in order to compute greatest
common divisors in Z[i].
The following corollary of Euclid’s algorithm in Z[i] shows that a greatest common divisor
in Z[i] is ambiguous only by a unit multiple. That is, the built-in unit ambiguity is the only
one that actually occurs.
Corollary 4.7. For non-zero α and β in Z[i], let δ be a greatest common divisor produced
by Euclid’s algorithm. Any greatest common divisor of α and β is a unit multiple of δ.
Proof. Let δ′ be a greatest common divisor of α and β. From the proof of Euclid’s algorithm,
δ′ | δ (because δ′ is a common divisor). Write δ = δ′γ, so
N(δ) = N(δ′) N(γ) ≥N(δ′).
Since δ′ is a greatest common divisor, its norm is maximal among the norms of common
divisors, so the inequality N(δ) ≥N(δ′) has to be an equality. That implies N(γ) = 1, so
γ = ±1 or ±i. Thus δ and δ′ are unit multiples of each other.
□
5. Bezout’s Theorem in Z[i]
In Z, Bezout’s theorem says for any non-zero a and b in Z that (a, b) = ax + by for some
x and y in Z found by back-substitution in Euclid’s algorithm. The same idea works in Z[i]
and gives us Bezout’s theorem there.
Theorem 5.1 (Bezout’s theorem). Let δ be any greatest common divisor of two non-zero
Gaussian integers α and β. Then δ = αx + βy for some x, y ∈Z[i].
Proof. Being able to write δ as a Z[i]-combination of α and β is unaﬀected by replacing δ
with a unit multiple. (For instance, if we can do this for iδ, then we multiply through by
−i to do it for δ.) Thus, by Corollary 4.7, we only need to give a proof for δ a greatest
common divisor coming from Euclid’s algorithm. For such δ, back-substitution in Euclid’s
algorithm shows δ is a Z[i]-combination of α and β. Further details here are identical to
the integer case, and are left to the reader.
□
Corollary 5.2. The non-zero Gaussian integers α and β are relatively prime if and only
if we can write
1 = αx + βy
for some x, y ∈Z[i].

<!-- page 9 -->
THE GAUSSIAN INTEGERS
9
Proof. If α and β are relatively prime, then 1 is a greatest common divisor of α and β, so
1 = αx + βy for some x, y ∈Z[i] by Theorem 5.1. Conversely, if 1 = αx + βy for some
x, y ∈Z[i], then any common divisor of α and β is a divisor of 1, and thus is a unit. That
says α and β are relatively prime.
□
Example 5.3. We saw in Example 4.4 that α = 32 + 9i and β = 4 + 11i are relatively
prime, since the last non-zero remainder in Euclid’s algorithm is −i. We can reverse the
calculations in Example 4.4 to express −i as a Z[i]-combination of α and β:
−i = 2 −5i −(3 −i)(1 −i)
= 2 −5i −(β −(2 −5i)(−2 + i))(1 −i)
= (2 −5i)(1 + (−2 + i)(1 −i)) −β(1 −i)
= (2 −5i)(3i) −β(1 −i)
= (α −β(2 −2i))(3i) −β(1 −i)
= α(3i) −β(7 + 5i).
To write 1, rather than −i, as a combination of α and β, multiply by i:
(5.1)
1 = α(−3) + β(5 −7i).
Example 5.4. In Example 4.5, we checked that 4 + 5i and 4 −5i are relatively prime.
Using back-substitution in Example 4.5, we obtain
−i = 4 −5i −(−(1 −i))(−4)
= 4 −5i −(4 + 5i −(4 −5i)i)(−4)
= (4 + 5i)(4) + (4 −5i)(1 −4i),
and multiplying through by i gives
1 = (4 + 5i)(4i) + (4 −5i)(4 + i).
Example 5.5. In Example 4.6, we saw −1+2i is a greatest common divisor of α = 11+3i
and β = 1 + 8i. Reversing the steps of Euclid’s algorithm,
−1 + 2i = 1 + 8i −(2 −4i)(−1 + i)
= 1 + 8i −(11 + 3i −(1 + 8i)(1 −i))(−1 + i)
= (11 + 3i)(1 −i) + (1 + 8i)(1 + (1 −i)(−1 + i))
= (11 + 3i)(1 −i) + (1 + 8i)(1 + 2i)
= α(1 −i) + β(1 + 2i).
Example 5.6. Let α = 10 + 91i and β = 7 + 3i. By Euclid’s algorithm,
α = β(6 + 11i) + 1 −4i,
β = (1 −4i)(2i) + −1 + i,
1 −4i = (−1 + i)(−3 + i) −1,
−1 + i = −1(1 −i) + 0,

<!-- page 10 -->
10
KEITH CONRAD
so the last non-zero remainder is −1. That tells us α and β are relatively prime. Using
back-substitution,
−1 = 1 −4i −(−1 + i)(−3 + i)
= 1 −4i −(β −(1 −4i)(2i))(−3 + i)
= (1 −4i)(1 + (2i)(−3 + i)) −β(−3 + i)
= (1 −4i)(−1 −6i) + β(3 −i)
= (α −β(6 + 11i))(−1 −6i) + β(3 −i)
= α(−1 −6i) + β(−(6 + 11i)(−1 −6i) + 3 −i)
= α(−1 −6i) + β(−57 + 46i).
We can negate to write 1 as a Z[i]-combination of α and β:
(5.2)
1 = α(1 + 6i) + β(57 −46i).
While the previous example shows 10 + 91i and 7 + 3i do not have a common factor in
Z[i], notice that their norms are
N(10 + 91i) = 8381 = 172 · 29,
N(7 + 3i) = 58 = 2 · 29,
so the norms of 10+91i and 7+3i have a common factor in Z. We can understand how such
phenomena (relatively prime Gaussian integers have non-relatively prime norms) happen
by exhibiting the “prime factorizations” of 10+91i and 7+3i (without explaining how they
are found, however):
(5.3)
10 + 91i = (1 −4i)(4 + i)(5 + 2i),
7 + 3i = (1 + i)(5 −2i).
Now we see why such examples are possible: the factors 5 + 2i and 5 −2i have the same
norm (namely 29) but they are relatively prime to each other.
All the usual consequences of Bezout’s theorem over Z have analogues over Z[i]. Here
are some of them.
Corollary 5.7. Let α | βγ in Z[i] with α and β relatively prime. Then α | γ.
Proof. It’s just like the integer proof, but we write up the details anyway. Set βγ = ακ for
some κ in Z[i]. Since α and β are relatively prime, we can solve the equation
1 = αx + βy
for some x, y ∈Z[i]. Multiply both sides of the equation by γ:
γ = γαx + γβy
= αγx + ακy
= α(γx + κy).
Thus α | γ.
□
Corollary 5.8. If α | γ and β | γ in Z[i], with α and β relatively prime, then αβ | γ.
Proof. Left to the reader. It’s just like the integer case.
□
Corollary 5.9. For non-zero α, β, γ in Z[i], α and β are each relatively prime to γ if and
only if αβ is relatively prime to γ.
Proof. Left to the reader. It’s just like the integer case.
□

<!-- page 11 -->
THE GAUSSIAN INTEGERS
11
We close out this section with an extension to Z[i] of several diﬀerent characterizations
of the greatest common divisor in Z. The greatest common divisor of non-zero integers a
and b can be described in several ways:
• the largest common divisor of a and b (deﬁnition)
• the positive common divisor that all other common divisors divide
• the smallest positive value of ax + by (x, y ∈Z)
• the positive value of ax + by (x, y ∈Z) that divides all other values of ax + by
(x, y ∈Z)
The corresponding characterizations of greatest common divisors of two non-zero Gauss-
ian integers α and β are these:
• a common divisor of α and β with maximal norm (deﬁnition)
• a common divisor that all other common divisors divide
• a non-zero value of αx + βy (x, y ∈Z[i]) with smallest norm
• a non-zero value of αx + βy (x, y ∈Z[i]) that divides all other values of αx + βy
(x, y ∈Z[i])
Verifying the equivalence of all four conditions is left to the interested reader.
It is
completely analogous to the arguments used in the integer case. Notice the switch from
“the” to “a” when we pass from Z to Z[i]: there are always four greatest common divisors,
ambiguous up to multiplication by any of the four units.
6. Unique Factorization in Z[i]
We will deﬁne composite and prime Gaussian integers, and then prove unique factoriza-
tion.
By Theorem 2.4, if β | α, then N(β) | N(α), so 1 ≤N(β) ≤N(α) when α ̸= 0. Which
divisors of α have norm 1 or N(α)?
Lemma 6.1. For α ̸= 0, any divisor of α whose norm is 1 or N(α) is a unit or is a unit
multiple of α.
Proof. If β | α and N(β) = 1, then β is ±1 or ±i. If β | α and N(β) = N(α), consider
the complementary divisor γ, where α = βγ. Taking norms of both sides and cancelling
the common value N(α), we see N(γ) = 1, so γ is ±1 or ±i. Therefore β has to be ±α or
±iα.
□
Lemma 6.1 is not saying the only Gaussian integers whose norm is N(α) are ±α and ±iα.
For instance, 1+8i and 4+7i both have norm 65 and neither is a unit multiple of the other.
What Lemma 6.1 is saying is that the only Gaussian integers that divide α and have norm
equal to N(α) are ±α and ±iα.
When N(α) > 1, there are always eight obvious factors of α: ±1, ±i, ±α, and ±iα. We
call these the trivial factors of α. They are analogous to the four trivial factors ±1 and ±n
of any integer n with |n| > 1. Any other factor of α is called non-trivial. By Lemma 6.1,
the non-trivial factors of α are the factors with norm strictly between 1 and N(α).
Deﬁnition 6.2. Let α be a Gaussian integer with N(α) > 1. We call α composite if it has
a non-trivial factor. If α only has trivial factors, we call α prime.
Writing α = βγ, the condition 1 < N(β) < N(α) is equivalent to: N(β) > 1 and
N(γ) > 1. We refer to any such factorization of α, into a product of Gaussian integers with

<!-- page 12 -->
12
KEITH CONRAD
norm greater than 1, as a non-trivial factorization. Thus, a composite Gaussian integer is
one that admits a non-trivial factorization.
For instance, a trivial factorization of 7+i is i(1−7i). A non-trivial factorization of 7+i
is (1 −2i)(1 + 3i). A non-trivial factorization of 5 is (1 + 2i)(1 −2i). How interesting: 5
is prime in Z but it is composite in Z[i]. Even 2 is composite in Z[i]: 2 = (1 + i)(1 −i).
However, 3 is prime in Z[i], so some primes in Z stay prime in Z[i] while others do not.
To show 3 is prime in Z[i], we argue by contradiction. Assume it is composite and let a
non-trivial factorization be 3 = αβ. Taking the norm of both sides, 9 = N(α) N(β). Since
the factorization is non-trivial, N(α) > 1 and N(β) > 1. Therefore N(α) = 3. Writing
α = a + bi, we get a2 + b2 = 3. There are no integers a and b satisfying that equation, so
we have a contradiction. Thus, 3 has only trivial factorizations in Z[i], so 3 is prime in Z[i].
(In Corollary 9.4, we will see any prime p in Z+ satisfying p ≡3 mod 4 is prime in Z[i].)
While we don’t really need to construct primes explicitly in Z[i] in order to prove unique
factorization in Z[i], it is good to have some method of generating Gaussian primes, if only
to get a feel for what they look like by comparison with prime numbers. The following test
for primality in Z[i], using the norm, provides a way to generate many Gaussian primes if
we can recognize primes in Z.
Theorem 6.3. If the norm of a Gaussian integer is prime in Z, then the Gaussian integer
is prime in Z[i].
For example, since N(4 + 5i) = 41, 4 + 5i is prime in Z[i]. Similarly, 4 −5i is prime, as
are 1 ± i, 1 ± 2i, 2 ± 3i, 1 ± 4i, and 15 ± 22i. Compute each of their norms and check the
result is a prime number.
Proof. Let α ∈Z[i] have prime norm, say p = N(α). We will show α only has trivial factors
(that is, its factors have norm 1 or N(α) only), so α is prime in Z[i].
Consider any factorization of α in Z[i], say α = βγ. Taking norms, p = N(β) N(γ).
This is an equation in positive integers, and p is prime in Z+, so either N(β) or N(γ) is 1.
Therefore β or γ is a unit, so α does not admit nontrivial factors. Thus α is prime.
□
The converse of Theorem 6.3 is false: a Gaussian prime does not have to have prime
norm. For instance, 3 has norm 9, but we saw 3 is prime in Z[i].
We have said enough about concrete Gaussian primes for now, and turn our attention
to unique factorization. The existence of a prime factorization will be proved by a similar
argument to the proof of prime factorization in Z. First we will establish the existence of
a prime factorization, then we treat its uniqueness.
Theorem 6.4. Every α ∈Z[i] with N(α) > 1 is a product of primes in Z[i].
Proof. We argue by induction on N(α) (not by induction on α). Suppose that N(α) = 2.
(In other words, α = 1 ± i or −1 ± i.) Then α is prime by Theorem 6.3.
Now assume n ≥3 and every Gaussian integer with norm greater than 1 and less than
n is a product of primes.
We want to show every Gaussian integer with norm n is a
product of primes. If there are no Gaussian integers with norm n (recall the end of Section
1), then there is nothing to prove. So we may assume there are Gaussian integers with
norm n. Those that are prime are a product of primes (in Z[i]). If we have a Gaussian
integer α with norm n that is composite, write a non-trivial factorization of α as βγ, where
N(β), N(γ) < N(α) = n. By the inductive hypothesis, β and γ are products of primes
in Z[i]. Therefore their product, which is α, is also a product of primes in Z[i]. We are
done.
□

<!-- page 13 -->
THE GAUSSIAN INTEGERS
13
Having settled the existence of prime factorizations in Z[i], we aim for the uniqueness.
We start with a lemma that generalizes a familiar result about prime numbers in Z.
Lemma 6.5. Let π be prime in Z[i]. For Gaussian integers α1, . . . , αr, if π | α1α2 · · · αr
then π divides some αj.
Proof. We check the case r = 2. The proof for larger r is a straightforward induction.
Let π | α1α2. Suppose π does not divide α1. This implies π and α1 are relatively prime.
Indeed, otherwise π and α1 would have a non-unit greatest common divisor, which would
have to be a unit multiple of π (since π only has trivial factors, as it is prime). This would
imply π divides α1, which is not the case.
Now that we know π and α1 are relatively prime, π | α2 by Corollary 5.7.
□
We’re now ready to prove unique factorization in Z[i]. However, it is not quite what you
may expect. That is, the following is false: when
π1π2 · · · πr = π′
1π′
2 · · · π′
s
where the πi’s and πj’s are all prime in Z[i], r = s and πi = π′
i after a suitable relabelling.
Well, the r = s part is true. But there is no reason to expect we can match up the primes
term-by-term. Consider
5 = (1 + 2i)(1 −2i) = (2 −i)(2 + i).
The factors here are all prime in Z[i] (since their norms all equal the prime number 5), but
the two primes in one factorization do not appear in the other. Does this violate the idea
of unique factorization?
No. By allowing unit multiples, we can make a match between the two factorizations:
1 + 2i = (2 −i)i,
(1 −2i) = (2 + i)(−i).
In fact, the same phenomenon can happen in Z:
6 = 2 · 3 = (−2) · (−3).
This is not an example of non-unique factorization in Z, since we can match the factors up
to sign. Sign issues are avoided in Z by focusing attention on positive integers and positive
primes only. As there is no positivity in Z[i] (at least in this course), we are forced to allow
ambiguity up to unit multiples in our prime factorizations. This explains the role of units
in unique factorization for Z[i].
Theorem 6.6 (Unique Factorization). Each α ∈Z[i] with N(α) > 1 has a unique factor-
ization into primes in the following sense: If
α = π1π2 · · · πr = π′
1π′
2 · · · π′
s,
where the πi’s and π′
j’s are prime in Z[i], then r = s and after a suitable renumbering each
πi is a unit multiple of π′
i.
Proof. Theorem 6.4 shows each α ∈Z[i] with N(α) > 1 has a prime factorization.
When α is prime, its prime factorization is obviously unique. Now we show uniqueness
in general by induction on N(α). The base case, N(α) = 2, has already been settled since
such α’s are prime.
Assume now that n ≥3 and every Gaussian integer with norm greater than 1 and less
than n has a unique prime factorization.
We may assume there are Gaussian integers
with norm n (otherwise there is nothing to check), and we only have to focus attention on

<!-- page 14 -->
14
KEITH CONRAD
composite α with norm n. Consider two prime factorizations of α as in the statement of
the theorem. Since π1 | α, we can write
π1 | π′
1π′
2 · · · π′
s.
By Lemma 6.5, π1 | π′
j for some j. Relabelling, we may suppose j = 1, i.e., π1 | π′
1. The
only non-unit factors of π′
1 are unit multiples of π′
1, so π1 = uπ′
1 for some unit u ∈{±1, ±i}.
The two factorizations of α now look like this:
α = uπ′
1π2 · · · πr = π′
1π′
2 · · · π′
s,
We cancel π′
1 on both sides and get
(6.1)
uπ2 · · · πr = π′
2 · · · π′
s,
Call this common value β, so N(β) = N(α)/ N(π′
1) < N(α).
Although u is a unit, the product uπ2 on the left side of (6.1) is itself a prime, so (6.1)
gives two prime factorizations of β, with r −1 primes on the left side and s −1 primes on
the right side. Since N(β) < n, the inductive hypothesis tells us β has unique factorization,
so r −1 = s −1 (thus r = s) and, after suitable relabelling, we have uπ2 and π′
2 are unit
multiples and πi, π′
i are unit multiples for i > 2.
Since uπ2 and π′
2 are unit multiples,
π2 and π′
2 are unit multiples, so we see every πi is a unit multiple of π′
i and the proof is
complete.
□
Knowing there is a prime factorization in the abstract is diﬀerent from being able to
exhibit one in practice. For instance, what is the prime factorization of 3+4i or 511+2826i?
You have no experience factoring in Z[i], but you have factored in Z. Let’s use the norm
function to let your experience in Z be the ﬁrst step in helping you factor in Z[i]. Our goal
is not to prove a theorem about practical factoring in Z[i], but to illustrate the method
through some examples. Then you can try it out your own.
The key idea is this: any factorization in Z[i] implies a factorization in norms. Indeed,
α = βγ =⇒N(α) = N(β) N(γ).
We will try to use the conclusion to tell us something about the hypothesis: use integer
factorizations of the norm to suggest possible factors of the Gaussian integer and then test
them.
Example 6.7. Let’s factor 3 + 4i into primes. Its norm is 25 = 5 · 5, so a nontrivial factor
of 3 + 4i has to have norm 5. We know the Gaussian integers with norm 5: up to unit
multiple they are 1 + 2i and 1 −2i. So we try dividing 3 + 4i by 1 + 2i:
3 + 4i
1 + 2i = (3 + 4i)(1 −2i)
(1 + 2i)(1 −2i) = 11 −2i
5
̸∈Z[i],
so (1 + 2i) ∤(3 + 4i). Next try 1 −2i:
3 + 4i
1 −2i = (3 + 4i)(1 + 2i)
(1 −2i)(1 + 2i) = −5 + 10i
5
= −1 + 2i ∈Z[i],
so
3 + 4i = (1 −2i)(−1 + 2i),
This is a prime factorization of 3 + 4i since the factors on the right have prime norm. Since
−1 + 2i = −(−1 −2i), 3 + 4i = −(1 −2i)2.

<!-- page 15 -->
THE GAUSSIAN INTEGERS
15
Example 6.8. Let’s factor 511 + 2826i into primes. Its norm is 8247397, whose prime
factorization in Z is
8247397 = 17 · 29 · 16729.
Let’s look for Gaussian integers with norms 17, 29, and 16729. They can come from repre-
senting each number as a sum of two squares:
17 = 12 + 42,
29 = 22 + 52,
16729 = 402 + 1232.
(Admittedly, that last equation was not found by hand.) These give us factorizations
17 = (1 + 4i)(1 −4i),
29 = (2 + 5i)(2 −5i),
16729 = (40 + 123i)(40 −123i)
and the Gaussian integers here are prime since their norms are prime in Z. Let’s ﬁrst try
dividing 511 + 2826i by 1 + 4i:
511 + 2826i
1 + 4i
= (511 + 2826i)(1 −4i)
(1 + 4i)(1 −4i)
= 11815 + 782i
17
= 695 + 46i ∈Z[i].
so 511+2826i = (1+4i)(695+46i). The second factor has norm 29·16729. We try dividing
695 + 46i by 2 + 5i:
695 + 46i
2 + 5i
= (695 + 46i)(2 −5i)
(2 + 5i)(2 −5i)
= 1620 −3383i
29
̸∈Z[i].
so (2 + 5i) ∤(695 + 46i). Try the conjugate number 2 −5i:
695 + 46i
2 −5i
= (695 + 46i)(2 + 5i)
(2 −5i)(2 + 5i)
= 1160 −3567i
29
= 40 −123i ∈Z[i].
Thus
511 + 2826i = (1 + 4i)(695 + 46i) = (1 + 4i)(2 −5i)(40 −123i),
which is a prime factorization in Z[i] since the norms of the factors are prime numbers.
As an application of these ideas, try to discover the factorizations in (5.3) on your own.
7. Modular arithmetic in Z[i]
As in the integers, congruences are deﬁned using divisibility.
Deﬁnition 7.1. For Gaussian integers α, β, and γ, we write α ≡β mod γ when γ | (α−β).
Example 7.2. To check 1 + 12i ≡2 −i mod 3 + i, we subtract and divide:
(1 + 12i) −(2 −i)
3 + i
= −1 + 13i
3 + i
= 1 + 4i.
The ratio is in Z[i], so the congruence holds.
Congruences in Z[i] behave well under both addition and multiplication:
α ≡α′ mod γ,
β ≡β′ mod γ =⇒α + β ≡α′ + β′ mod γ,
αβ ≡α′β′ mod γ.
The details behind this are just like in Z and are left to the reader to check.
Since congruence modulo 0 means equality, we usually assume the modulus is non-zero.
A Gaussian integer can be reduced modulo α, if α ̸= 0, to get a congruent Gaussian
integer with small norm by dividing by α and using the remainder.
Example 7.3. Let’s compute (3 + 2i)2 mod 4 + i. Since (3 + 2i)2 = 5 + 12i and 5 + 12i =
(4 + i)(2 + 3i) −2i, we have (3 + 2i)2 ≡−2i mod 4 + i.

<!-- page 16 -->
16
KEITH CONRAD
Example 7.4. To reduce 1 + 8i mod 2 −4i, we divide. This was already done in Example
3.5, where we found more than one possibility:
1 + 8i = (2 −4i)(−1 + i) −1 + 2i,
1 + 8i = (2 −4i)(−1 + i) + 1 −2i.
Therefore 1 + 8i ≡−1 + 2i mod 2 −4i and 1 + 8i ≡1 −2i mod 2 −4i. There is no reason
to think −1 + 2i or 1 −2i is the more correct reduction. Both work.
There is a way to picture what modular arithmetic in Z[i] means, by plotting the mul-
tiples of a Gaussian integer in Z[i]. For example, let’s look at the Z[i]-multiples of 1 + 2i.
Algebraically, a general Z[i]-multiple of 1 + 2i is
(1 + 2i)(m + ni) = (1 + 2i)m + (1 + 2i)ni = m(1 + 2i) + n(−2 + i),
where m and n are in Z. This is an integral combination of 1 + 2i and −2 + i = (1 + 2i)i.
In Figure 1 we plot 1 + 2i and −2 + i as the vectors (1, 2) and (−2, 1) in R2.
Figure 1. 1 + 2i and −2 + i
The Z[i]-multiples of 1 + 2i are the integral combinations of the two vectors in Figure 1.
Forming all these combinations produces the picture in Figure 2, where the plane is tiled by
squares having the Gaussian multiples of 1 + 2i as the vertices. The signiﬁcance of Figure
2 for modular arithmetic is that Gaussian integers are congruent modulo 1 + 2i precisely
when they are located in the same relative positions within diﬀerent squares of Figure 2.
For example, 2 + 3i and 4 −3i are in the same relative position within their squares, and
their diﬀerence is a Gaussian multiple of 1 + 2i:
(2 + 3i) −(4 −3i)
1 + 2i
= −2 + 6i
1 + 2i = (−2 + 6i)(1 −2i)
(1 + 2i)(1 −2i) = 10 + 10i
5
= 2 + 2i ∈Z[i].
Why are congruent Gaussian integers mod 1+2i in the same position within their respective
squares? Because each square shares its sides with four other squares, and moving to these
squares corresponds to adding 1 + 2i, −(1 + 2i), −2 + i, or −(−2 + i). Moving from a
position in any square to the same relative position in any other square is translation by a
Gaussian multiple of 1 + 2i.
We can use Figure 2 to make a list of representatives for Z[i]/(1 + 2i): use the Gaussian
integers inside a square and one of its vertices. (All the vertices are Z[i]-multiples of 1 + 2i,
so we should use only one of them.) Choosing the square with edges 1 + 2i and −2 + i, we
get a list of 5 Gaussian integers:
0, i, 2i, −1 + i, −1 + 2i.

<!-- page 17 -->
THE GAUSSIAN INTEGERS
17
Figure 2. Z[i]-multiples of 1 + 2i
Every Gaussian integer is congruent modulo 1 + 2i to exactly one of these. For instance,
2 + 3i ≡−1 + 2i mod 1 + 2i since 2 + 3i and −1 + 2i are in the same relative position in
their respective squares. Using instead the square with edges 1 + 2i and 2 −i, we get the
list
0, 1, 2, 1 + i, 2 + i,
and with this list we have 2 + 3i ≡1 + i mod 1 + 2i. There is nothing special about using
the vertex 0 in our lists: we could use any of the other vertices of the square in place of 0
for our list of representatives modulo 1 + 2i. In fact, there is nothing special about using
points inside or on a single square. We just need to use a set of points that ﬁlls out each
relative position within all these squares. For instance, the numbers
0, 1, 2, 3, 4
could be used, and with this list we have 2 + 3i ≡3 mod 1 + 2i.
Let’s look at the picture for modulus 2 + 2i. In Figure 3 we plot the Z[i]-multiples of
2 + 2i as vertices of squares. Since
(2 + 2i)(m + ni) = (2 + 2i)m + (2 + 2i)ni = m(2 + 2i) + n(−2 + 2i),
the Z[i]-multiples of 2 + 2i are the integral combinations of 2 + 2i and −2 + 2i, which form
two edges of the shaded square in Figure 3.
What is a set of representatives for Z[i]/(2 + 2i)? Translating from one square to the
same relative position in another square is the same as adding a Gaussian multiple of 2+2i,
so every Gaussian integer is congruent modulo 2 + 2i to a Gaussian integer inside or on
one of the squares. Points in the same relative position on opposite edges of a square are
congruent since adding 2 + 2i or −2 + 2i takes us from one edge to another. We didn’t
have to worry about this issue for modulus 1 + 2i because there were no Gaussian integers
on the edges of squares in Figure 2 except for vertices. Taking the edge identiﬁcations into
account, a set of representatives for Z[i]/(2+2i) is all the Gaussian integers inside a square

<!-- page 18 -->
18
KEITH CONRAD
Figure 3. Z[i]-multiples of 2 + 2i
and on two adjacent edges of the square, with only one vertex counted. Using the square
with edges 2 + 2i and −2 + 2i, we get the 8 representatives
0, i, 2i, 3i, 1 + i, 1 + 2i, −1 + i, −1 + 2i.
For example, 6+i ≡3i mod 2+2i since 6+i and 3i are in the same relative position within
their squares in Figure 3.
Unlike in Figure 2, where ordinary integers can be used as representatives, we can’t
represent Z[i]/(2 + 2i) only using ordinary integers, because Z only represents 4 of the 8
congruence classes mod 2 + 2i.
Figure 4 is a picture of Z[i]/(3). The squares have vertices that are Z[i]-multiples of 3,
which all look like 3(m+ni) = m·3+n·3i where m and n are in Z. A set of representatives
for Z[i]/(3) can be formed from the Gaussian integers inside and on the shaded square
with edges 3 and 3i. Using two adjacent edges (and just one of the vertices), we have 9
representatives
0, 1, 2, i, 1 + i, 2 + i, 2i, 1 + 2i, 2 + 2i.
Finally, in Figure 5, we draw one square for modulus 3+i. Its two edges with a vertex at
0 are the vectors 3+i = (3, 1) and (3+i)i = −1+3i = (−1, 3). There are 10 representatives:
9 in the square and one vertex.
Algebraic properties of modular arithmetic in Z carry over to Z[i] practically word-for-
word.
Theorem 7.5. If π is prime in Z[i], then αβ ≡0 mod π if and only if α ≡0 mod π or
β ≡0 mod π.
Proof. This is Lemma 6.5 with r = 2.
□

<!-- page 19 -->
THE GAUSSIAN INTEGERS
19
Figure 4. Z[i]-multiples of 3
Figure 5. Representatives for Z[i]/(3 + i)
Theorem 7.6. For α and β in Z[i] with β ̸= 0, αx ≡1 mod β is solvable if and only
if α and β are relatively prime in Z[i]. If α and β are relatively prime then any linear
congruence αx ≡γ mod β has a unique solution.
Proof. To solve αx ≡1 mod β with x ∈Z[i] amounts to solving αx + βy = 1 with x and y
in Z[i], which is equivalent to relative primality of α and β by Corollary 5.2.
Once we can invert α mod β, we can solve αx ≡γ mod β by multiplying both sides by the
inverse of α mod β. If there is going to be a solution this must be it, and it does work.
□
Example 7.7. Can we solve (1 + 8i)x ≡1 mod 11 + 3i? No, since 1 + 8i and 11 + 3i have
a common factor of −1 + 2i by Example 4.6.
Example 7.8. Can we solve (7 + 3i)x ≡1 mod 10 + 91i? According to Example 5.6, 7 + 3i
and 10 + 91i are relatively prime (although their norms are not), so there is a solution.

<!-- page 20 -->
20
KEITH CONRAD
Moreover, by using Euclid’s algorithm and back-substitution we found in (5.2) that
(7 + 3i)(57 −46i) + (10 + 91i)(1 + 6i) = 1,
so a solution is x = 57 −46i. (The norm of 57 −46i is less than the norm of the modulus
10 + 91i, so there is no great incentive to reduce our solution further mod10 + 91i.)
Corollary 7.9. Let π be a Gaussian prime. Every α ̸≡0 mod π has a multiplicative inverse
modulo π and any polynomial congruence
cnxn + cn−1xn−1 + · · · + c1x + c0 ≡0 mod π,
where ci ∈Z[i] and cn ̸≡0 mod π, has at most n solutions modulo π.
Proof. Since π is prime, each α ̸≡0 mod π is relatively prime to π and therefore α mod π
has a multiplicative inverse by Theorem 7.6. Thus Z[i]/(π) is a ﬁeld, so this corollary is a
special case of the fact that polynomials have no more roots in a ﬁeld than their degree.
□
When we allow Gaussian integers into our congruences, does it change the meaning of
congruences among ordinary integers? That is, if a, b, and c are in Z, does the meaning of
a ≡b mod c change when we think in Z[i]? That is, could integers that are incongruent
modulo c in Z become congruent modulo c in Z[i]? No.
Theorem 7.10. For a, b, and c in Z, a ≡b mod c in Z if and only if a ≡b mod c in Z[i].
Proof. In terms of divisibility, this is saying
c | (a −b) in Z ⇐⇒c | (a −b) in Z[i],
which is something we already checked in the paragraph after the proof of Theorem 2.3:
divisibility between ordinary integers holds in Z if and only if it holds in Z[i].
□
So far modular arithmetic in Z[i] behaves just like in Z. But things now will get tricky,
so pay attention!
One of the useful properties of modular arithmetic in Z is Fermat’s little theorem. For a
prime p in Z+, if a ̸≡0 mod p then ap−1 ≡1 mod p. Naively translating this result into the
Gaussian integers, using a Gaussian prime π, we get something like this: if α ̸≡0 mod π
then απ−1 ≡1 mod π. ???? If π is not a positive integer, then raising to the power π −1
doesn’t mean anything in a congruence. (Well, if you have had complex analysis you may
know a way to do this, but then you would also know the result is almost certainly not
going to be in Z[i], so it’s the wrong idea for us.) Moreover, even when π is a positive
integer that is prime in Z[i] the congruence απ−1 ≡1 mod π is usually wrong.
Example 7.11. Let π = 3, which is prime in Z[i]. Take α = i. Then απ−1 = i2 = −1, but
−1 ̸≡1 mod 3, so απ−1 ̸≡1 mod π.
Despite this setback, there is a good Gaussian integer version of Fermat’s little theorem.
The way to ﬁnd it is to go back to the proof of Fermat’s little theorem and remind ourselves
how ap−1 actually showed up in the proof. It came from comparing two diﬀerent sets of
representatives for the non-zero integers modulo p: 1, 2, . . . , p −1 and a, 2a, . . . , (p −1)a.
The two products of all the numbers in both cases have to be congruent modulo p, and
cancelling common terms on both sides of the congruence (essentially a factor of (p −1)!)
leaves behind 1 ≡ap−1 mod p. So the source of ap−1 comes from the fact that there are
p −1 non-zero numbers modulo p. It is the size of the set of non-zero numbers modulo p
that gave us the exponent in Fermat’s little theorem. There are p numbers in total modulo

<!-- page 21 -->
THE GAUSSIAN INTEGERS
21
p, and we take away 1 because we don’t count 0. With this insight, we get almost for free
a Z[i]-analogue.
Theorem 7.12. Let π be a Gaussian prime and denote the number of Gaussian integers
modulo π by n(π). If α ̸≡0 mod π, then αn(π)−1 ≡1 mod π.
Proof. There is no natural complete set of representatives for Z[i]/(π), but we can use any
complete set of representatives at all. Denote it β1, β2, . . . , βn(π), where we take βn(π) = 0.
Since α is invertible modulo π, another complete set of representatives for Z[i]/(π) is
αβ1, αβ2, . . . , αβn(π). The last term here is 0. Multiplying congruent numbers retains the
congruence, so let’s multiply each set of non-zero representatives together and compare:
β1β2 · · · βn(π)−1 ≡(αβ1)(αβ2) · · · (αβn(π)−1) mod π
≡αn(π)−1β1β2 · · · βn(π)−1 mod π.
Since the βi’s here are non-zero modulo π (why?), we can cancel them on both sides and
we are left with 1 ≡αn(π)−1 mod π.
□
As soon as we try to test this result in an example, we run into a problem. We deﬁned
n(π) to be the size of Z[i]/(π) but we never gave a working formula for this size.
For
instance, what is n(3)? Or, to jazz things up, n(3 + 4i)?
Example 7.13. Let’s show there are 9 elements in Z[i]/3, so n(3) = 9. A Gaussian integer
is divisible by 3 exactly when its real and imaginary parts are divisible by 3 (Theorem 2.3).
Therefore
a + bi ≡c + di mod 3 ⇐⇒a ≡b mod 3 and c ≡d mod 3.
The real and imaginary parts have 3 possibilities modulo 3, so there is a total of 3·3 = 9 in-
congruent Gaussian integers modulo 3. We can even write down a nice set of representatives:
a + bi where 0 ≤a, b ≤2.
Since n(3) = 9, Theorem 7.12 says that if α ̸≡0 mod 3 then α8 ≡1 mod 3. This works
at α = i (unlike what we saw in Example 7.11). Using α = 1 + i shows the exponent 8 is
optimal: (1 + i)k ̸≡1 mod 3 for 1 ≤k < 8.
To make Theorem 7.12 really meaningful, we want a formula for n(π) in general. In fact,
there is a nice formula for n(α) = |(Z[i]/(α))| even when α is not prime.
Theorem 7.14. If α ̸= 0 in Z[i], then n(α) = N(α). That is, the size of Z[i]/(α) is N(α).
There is an analogy with the absolute value on Z: |(Z/m)| = |m| when m ̸= 0 and
now |(Z[i]/(α))| = N(α) when α ̸= 0. Our earlier lists of representatives for Z[i]/(1 + 2i),
Z[i]/(2 + 2i), Z[i]/(3), and Z[i]/(3 + i) are all consistent with this norm formula.
Perhaps we should point out why n(α) is ﬁnite (when α ̸= 0) before we prove the formula
for it. Using division by α, every Gaussian integer is congruent modulo α to some Gaussian
integer with norm less than N(α). There are only ﬁnitely many Gaussian integers with
norm below a given bound, so n(α) is ﬁnite.1
Before we prove Theorem 7.14 we establish a few lemmas about the n-function.
Lemma 7.15. If m ̸= 0 in Z then n(m) = m2.
1This shows Gaussian integers with norm less than N(α) ﬁll up all congruence classes modulo α, but there
could be diﬀerent remainders that are congruent, unlike in Z, so n(α) is actually smaller than the number
of these remainders.

<!-- page 22 -->
22
KEITH CONRAD
Proof. The argument is the same as the case m = 3 done in Example 7.13.
□
Lemma 7.16. If α ̸= 0 in Z[i] then n(α) = n(α).
Proof. Congruences modulo α and congruences modulo α can be converted into one another
by conjugating all terms:
x ≡y mod α ⇐⇒x ≡y mod α.
Therefore a complete set of representatives modulo α becomes a complete set of represen-
tatives modulo α by conjugating the representatives, so n(α) = n(α).
□
The next lemma needs a bit more work.
Lemma 7.17. The function n is multiplicative: if α and β are non-zero in Z[i], then
n(αβ) = n(α)n(β).
Proof. Let a complete set of representatives for Z[i]/(α) be x1, x2, . . . , xr and a complete
set of representatives for Z[i]/(β) be y1, y2, . . . , ys. (That is, r = n(α) and s = n(β).)
Given z ∈Z[i], we have z ≡xi mod α for some i. Then z −xi = αt for some Gaussian
integer t, and t ≡yj mod β for some j. Writing t = yj + βw, we have
z = xi + αyj + αβw ≡xi + αyj mod αβ.
Thus the rs numbers xi + αyj are a set of representatives for Z[i]/(αβ). To show they are
complete (that is, no repetitions), suppose
(7.1)
xi + αyj ≡xi′ + αyj′ mod αβ.
We want to show i = i′ and j = j′.
Reducing both sides of (7.1) modulo α, xi ≡xi′ mod α. Since the x’s are a complete set
of representatives modulo α, this congruence must be equality: xi = xi′ (that is, i = i′).
Then subtract the common xi on both sides of (7.1) and divide through the congruence
(including the modulus!)
by α.
We are left with yj ≡yj′ mod β.
Since the y’s are a
complete set of representatives modulo β, we have j = j′.
□
We are ready to prove Theorem 7.14. All the real work has been put into the lemmas,
so the proof now will be a short and slick argument.
Proof. By Lemma 7.17, n(αα) = n(α)n(α). By Lemma 7.16, the right side is n(α)2. At
the same time, since αα = N(α) is an integer, Lemma 7.15 says n(αα) = N(α)2. Thus
N(α)2 = n(α)2. Take positive square roots.
□
There are two points worth noting about this argument:
(1) While we proved n(α) is a totally multiplicative function of α as a lemma, we did
not use this to reduce the problem of calculating n(α) to the case of n(π) for prime
π. Usually when we know something is multiplicative, we take that as a clue to ﬁrst
compute on primes, then prime powers, and then in general by prime factorization.
But the way multiplicativity of n got used in the proof of Theorem 7.14 completely
sidestepped the special case of prime α.
(2) Our derivation of the formula for n(α) lets us count the size of Z[i]/(α) without
giving a method of listing a complete set of representatives. For instance, n(2 +
2i) = N(2 + 2i) = 8, but this counting does not tell us a set of representatives for
Z[i]/(2 + 2i) (it is not 0, 1, 2, . . . , 7, e.g., 4 ≡0 mod 2 + 2i). So the situation is
unlike the integers, where we know |(Z/m)| = |m| because we actually made a list
of representatives: 0, 1, 2, . . . , |m| −1.

<!-- page 23 -->
THE GAUSSIAN INTEGERS
23
With an exact formula for |(Z[i]/(π))| in hand let’s reformulate Theorem 7.12 as a more
honest analogue of Fermat’s little theorem:
(7.2)
α ̸≡0 mod π =⇒αN(π)−1 ≡1 mod π.
Comparing this to ap−1 ≡1 mod p, we see more clearly from the Gaussian case that p was
really playing two diﬀerent roles in the integer case: the modulus is p and the number of
incongruent integers for that modulus is p. The distinction between the modulus and the
number of incongruent numbers in that modulus is more vivid in (7.2), where we see π in
one place and N(π) in the other.
To formulate Euler’s congruence in Z[i], we need the analogue of the ϕ-function. If you
think about ϕ(m) as the number of positive integers between 1 and m that are relatively
prime to m, the correct generalization to Z[i] is not apparent. But if you think about ϕ(m)
as the number of invertible integers modulo m, then the generalization to Z[i] is (or should
be) immediate.
Deﬁnition 7.18. For non-zero α in Z[i], set ϕ(α) = |(Z[i]/(α))×|.
Example 7.19. When α = π is prime, every non-zero Gaussian integer modulo π is in-
vertible, so ϕ(π) = N(π) −1. Notice the analogy to ϕ(p) = p −1.
When we work with this ϕ-function on Z[i], we need to be careful when the argument
is in Z, because the Gaussian ϕ-function may not agree with the integral ϕ-function. For
instance in Z we have ϕ(3) = 2, but in Z[i] we have ϕ(3) = 8. That is, (Z/3)× has 2 elements
but (Z[i]/3)× has 8 elements. This might seem strange: didn’t Theorem 7.10 tell us that
congruences with a modulus in Z are the same in Z[i] as in Z? No. Theorem 7.10 was
about congruences in Z[i] among ordinary integers to an ordinary integer modulus, which
leaves out a lot of congruences among all the Gaussian integers to that ordinary integer
modulus. Perhaps we should write ϕZ[i] to distinguish the Gaussian ϕ-function from the
usual ϕ-function (which is now ϕZ?), but nobody does this.
Euler’s congruence for Z[i] looks like its counterpart over Z, using the Gaussian ϕ-
function:
Theorem 7.20. If (α, µ) = 1 in Z[i], then αϕ(µ) ≡1 mod µ.
Proof. This is left as an exercise in translating the proof over Z into this new setting.
□
How do we compute ϕ(µ)? Let’s recall the ϕ-formulas in Z:
ϕ(pk) = pk−1(p −1),
ϕ(ab) = ϕ(a)ϕ(b) if (a, b) = 1.
With these formulas, ϕ(m) can be computed from the prime factorization of m.
The
analogous formulas for the Gaussian ϕ-function use norms in certain places, but otherwise
are identical to the counterpart in Z:
ϕ(πk) = N(π)k−1(N(π) −1),
ϕ(αβ) = ϕ(α)ϕ(β) if (α, β) = 1.
Example 7.21. What is ϕ(3 + 4i)? The Gaussian prime factorization is 3 + 4i = (2 + i)2.
Therefore ϕ(3 + 4i) = N(2 + i)(N(2 + i) −1) = 5 · 4 = 20.
Example 7.22. What is ϕ(5)? The Gaussian prime factorization is 5 = (1 + 2i)(1 −2i),
where 1 + 2i and 1 −2i are relatively prime.
Therefore ϕ(5) = ϕ(1 + 2i)ϕ(1 −2i) =
(N(1 + 2i) −1)(N(1 −2i) −1) = 16.

<!-- page 24 -->
24
KEITH CONRAD
8. Applications of Z[i] to Z
We are ready to give applications of the arithmetic of Z[i] to properties of Z. All these
applications are connected with sums of two squares. It is precisely the formula
a2 + b2 = (a + bi)(a −bi),
where a sum of two squares is on the left and a (special type of) factorization in Z[i] is on
the right that explains why Z[i] is relevant to questions about sums of two squares in Z.
Our applications will address the following issues:
• a prime number that is a sum of two squares is so in essentially just one way,
• classiﬁcation of (primitive) Pythagorean triples,
• classiﬁcation of (primitive) solutions to a2 + b2 = c3.
• the only integer solution to y2 = x3 −1 is (x, y) = (1, 0),
• systematically ﬁnding integers that are sums of two squares in more than one way.
Theorem 8.1. If a prime number p is a sum of two squares then it is so in essentially just
one way: writing p = a2 + b2, the integers a and b are unique up to order and sign. (In
particular, the squares a2 and b2 are unique up to order.)
Notice the theorem says nothing explicitly about Z[i]. It is a theorem about Z alone. We
will ﬁnd it very useful to use Z[i] in the proof, however.
Proof. Let p = a2 + b2, with a, b ∈Z. Then, in Z[i], p factors as
p = (a + bi)(a −bi).
Since a + bi and a −bi both have norm p, which is prime in Z, they are prime in Z[i]
(Theorem 6.3). If there is a second representation p = c2 + d2, then
p = (c + di)(c −di),
and c ± di are prime in Z[i]. By unique factorization in Z[i], we must have
a + bi = u(c + di)
or
a + bi = u(c −di)
for some unit u. The only diﬀerence between c + di and c −di is the sign of the coeﬃcient
of i, and we are aiming to show that a and b are determined up to order and sign, so there
is no harm in treating only the case
a + bi = u(c + di).
If u = 1, then c = a and d = b. If u = −1, then c = −a and d = −b. If u = i, then c = b
and d = −a. If u = −i, then c = −b and d = a. Thus c and d equal a and b up to order
and sign.
□
Theorem 8.1 is not saying that any integer that is a sum of two squares has only one
representation in that form. It is only referring to primes that are sums of two squares. Two
non-primes that are a sum of two squares in more than one way are 50 = 52 + 52 = 12 + 72
and 65 = 12 + 82 = 42 + 72. (We will ﬁnd more examples at the end of this section.) Some
primes that can be written as sums of two squares (necessarily uniquely) are
2 = 12 + 12,
5 = 12 + 22,
13 = 22 + 32,
17 = 12 + 42,
29 = 22 + 52.

<!-- page 25 -->
THE GAUSSIAN INTEGERS
25
Example 8.2. The ﬁfth Fermat number 225 + 1 = 4294967297 is easily a sum of two
squares: 225 + 1 = (216)2 + 12. Euler found it can be written as a sum of two squares in a
diﬀerent way:
(216)2 + 12 = 622642 + 204492.
This actually has an interesting consequence. Fermat guessed that the ﬁfth Fermat number
was a prime, but the fact that it can be written as a sum of two squares in two diﬀerent
ways proves it is not prime without telling us what a nontrivial factor might be! (Euler did
ﬁnd a nontrivial factor, 641: 225 + 1 = 641 · 6700417.)
Our next application of Z[i] to ordinary arithmetic is the classiﬁcation of Pythagorean
triples, which are solutions (a, b, c) in Z+ to the equation
a2 + b2 = c2.
A common factor of any two of a, b, and c is also a factor of the third number (why?), so
its square appears in all terms. Conversely, multiplying both sides by a square rescales a, b,
and c by the same amount. Therefore, we focus our attention on the Pythagorean triples
(a, b, c) where they share no common factor (equivalently, a and b alone share no common
factor). Such Pythagorean triples are called primitive. Examples of primitive Pythagorean
triples include (3, 4, 5), (5, 12, 13), and (8, 15, 17), but not (6, 8, 10). We will use unique
factorization in Z[i] to obtain a parametric formula for all primitive Pythagorean triples.
Before presenting the parametric formula, let’s make a few observations about primitive
triples (a, b, c). Since there is no common factor among the three numbers, at most one of
them can be even (why?). Could c be even? If so, then a and b are odd, so a2 ≡1 mod 4
and b2 ≡1 mod 4. Then c2 = a2 + b2 ≡2 mod 4. But no integer squares to 2 mod 4.
Therefore c is odd. Since a2 + b2 is now known to be odd, a and b do not have the same
parity. That is, one of a or b is odd and the other is even. Relabelling if necessary, we may
assume that b is even, so
a is odd and b is even.
With these preliminary observations out of the way, we are ready for the main result.
Theorem 8.3. Every primitive Pythagorean triple (a, b, c) with b even has the form
a = m2 −n2,
b = 2mn,
c = m2 + n2,
where m > n > 0, (m, n) = 1, and m ̸≡n mod 2. Conversely, for any such choice of m
and n, the above formula is a primitive Pythagorean triple with b even. Diﬀerent choices of
m and n give diﬀerent triples.
The table below gives some primitive Pythagorean triples from choices of m and n.
m
2
3
4
5
4
n
1
2
1
2
3
a = m2 −n2
3
5
15
21
7
b = 2mn
4
12
8
20
24
c = m2 + n2
5
13
17
29
25
Proof. Write the equation a2 + b2 = c2 in the form
(8.1)
(a + bi)(a −bi) = c · c.
Our proof will have three steps:
• use primitivity of (a, b, c) to show a + bi and a −bi are relatively prime in Z[i],

<!-- page 26 -->
26
KEITH CONRAD
• use unique factorization in Z[i] to show a+bi is a square or i times a square in Z[i],
• use the evenness of b to show a + bi is a square in Z[i], and then read oﬀthe
consequences.
First we show a+bi and a−bi are relatively prime. This is going to follow from (a, b) = 1
and c being odd. Let δ be a common divisor of a + bi and a −bi in Z[i]. It divides their
sum and their diﬀerence:
(8.2)
δ | 2a,
δ | 2b.
(Strictly, δ dividing the diﬀerence means δ | 2bi, but i is a unit so we can remove it.) Now
we show δ is relatively prime to 2 in Z[i]. Since 2 = −i(1 + i)2 and 1 + i is prime, this is
equivalent to showing δ is not divisible by 1 + i. By Corollary 2.5, (1 + i) | δ if and only if
N(δ) is even. Because δ2 | c2, by (8.1), which implies N(δ)2 | c4, and c4 is odd, we see N(δ)
is odd. That tells us 1 + i does not divide δ.
Now that we know δ is relatively prime to 2 in Z[i], (8.2) simpliﬁes to
δ | a,
δ | b.
Because a and b are relatively prime in Z, they are also relatively prime in Z[i] (just solve
ax + by = 1 in Z and then view the equation in Z[i]). Thus, their only common divisors in
Z[i] are units, so at last we see δ is a unit.
In (8.1), we have a product of relatively prime Gaussian integers on the left and a perfect
square on the right. If you think about it, the only way two relatively prime Gaussian
integers can multiply to a square is if they are each squares. After all, think about how
their prime factors can combine to give a square, given that they are relatively prime and
that Z[i] has unique factorization. Thus, from (8.1) we must have
a + bi = (m + ni)2
for some Gaussian integer m + ni.
Alas, this reasoning is wrong! Two relatively prime Gaussian integers can multiply to a
square without either factor being a square. In fact, this possibility already happens in Z:
36 = (−4)(−9).
Neither −4 nor −9 is a square in Z, but their product is and they are relatively prime.
The sneaky aspect here are units. Recall that unique factorization has an ambiguity due to
units. (We tend to forget this in Z since we focus on factoring in Z+ into positive factors,
and the only unit in Z+ is 1.) We shouldn’t forget about units!
Very well, we keep in mind the units in Z[i] when looking at (8.1). Since the two factors
on the left are relatively prime and their product is a square, unique factorization in Z[i]
tells us each factor is itself a square up to unit multiple. The units in Z[i] are ±1 and ±i.
Since −1 is a perfect square, it can be absorbed into any square factor by writing it as i2.
Therefore, we can say
a + bi = (m + ni)2
or
a + bi = i(m + ni)2
for some m + ni ∈Z[i]. Expanding these out and collecting real and imaginary parts, we
have
a + bi = (m2 −n2) + (2mn)i
or
a + bi = (−2mn) + (m2 −n2)i.
Now we appeal to our convention that b is even (and a is odd). The second choice makes
a even, so it is not correct. We thus must have
(8.3)
a + bi = (m + ni)2,

<!-- page 27 -->
THE GAUSSIAN INTEGERS
27
so a + bi is a perfect square after all. (The point is that we have now argued this correctly,
rather than incorrectly as before.) The derivation of (8.3) from unique factorization in Z[i]
is really the key step in this proof. The remainder of the proof will be just a matter of
careful bookkeeping.
Identifying real and imaginary parts in (8.3) gives us
a = m2 −n2,
b = 2mn.
Therefore c2 = a2 +b2 = (m2 −n2)2 +4m2n2 = m4 +2m2n2 +n4 = (m2 +n2)2. Since c > 0
we see that
c = m2 + n2.
Since b > 0, the formula for b shows m and n have the same sign: they are both positive
or both negative. We can negate them both if necessary to assume m and n are positive
without changing the values of a, b, or c. Since a > 0 we have m2 > n2, so m > n. Because
a is odd, m and n have diﬀerent parities. If m and n have a common factor, then we get
a common factor in a, b, and c. Therefore primitivity of the triple (a, b, c) makes m and n
relatively prime.
Now we show any triple (m2 −n2, 2mn, m2 +n2) with m and n positive, relatively prime,
of opposite parity, and m > n, is a primitive Pythagorean triple. Easily it is a Pythagorean
triple: (m2 −n2)2 + (2mn)2 = (m2 + n2)2. Suppose this triple is not primitive. Then some
prime p divides each of m2 −n2, 2mn, and m2 + n2. Since the ﬁrst term is odd, p ̸= 2.
Then from p | 2mn we have either p | m or p | n. If p | m, then the relation m2 ≡n2 mod p
implies n2 ≡0 mod p, so p | n. Similarly, if p | n then p | m. We are supposing (m, n) = 1,
so we have a contradiction either way, and thus the triple is primitive.
As for the triple being uniquely determined by m and n, (8.3) tells us that the parameters
m and n that describe the triple (a, b, c) are the real and imaginary parts of a square root
of a + bi. As there are only two square roots, which just diﬀer by a sign, the uniqueness
falls out (since we take m > 0 and n > 0).
□
This proof tells us how to produce Pythagorean triples on demand: take any Gaussian
integer α (with non-zero real and imaginary parts) and square it, say α2 = a + bi. Then
(|a|, |b|, N(α)) is a Pythagorean triple. For example, (17+12i)2 = 145+408i and 172+122 =
433. Therefore (145, 408, 433) is a Pythagorean triple (check it!). Moreover, since 17 and
12 are relatively prime, this triple is primitive.
To better appreciate this approach to a2 + b2 = c2, let’s apply it to a2 + b2 = c3.
Theorem 8.4. The integral solutions to a2 + b2 = c3 with (a, b) = 1 are described by the
parametric formula
a = m3 −3mn2,
b = 3m2n −n3,
c = m2 + n2,
where (m, n) = 1 and m ̸≡n mod 2. Diﬀerent choices of m and n give diﬀerent solutions
(a, b, c).
Proof. Since (a, b) = 1, a and b are not both even. If they were both odd then c3 ≡1 + 1 ≡
2 mod 8, but 2 is not a cube mod 8. Therefore one of a or b is even and the other is odd:
a ̸≡b mod 2 and c is odd.
In Z[i], we can rewrite a2 + b2 = c3 as
(a + bi)(a −bi) = c3.

<!-- page 28 -->
28
KEITH CONRAD
Let’s show a+bi and a−bi are relatively prime. If δ is a common divisor then δ | 2a, δ | 2b,
and δ | c3. Taking norms, N(δ) is a factor of 4a2, 4b2, and c6. Since c is odd, N(δ) is odd,
so N(δ) divides a2 and b2. The numbers a and b are relatively prime, so N(δ) = 1, and thus
δ is ±1 or ±i. This proves a + bi and a −bi are relatively prime.
Because the product of a + bi and a −bi is a perfect cube in Z[i], and these numbers are
relatively prime, unique factorization in Z[i] implies a + bi and a −bi are each cubes up
to multiplication by a unit. Say a + bi = uα3 where u ∈{±1, ±i}. However, every unit is
itself a cube: 1 = 13, −1 = (−1)3, i = (−i)3, and −i = i3. Therefore we can absorb the
unit factor into α3, so a + bi is in fact a perfect cube. Write a + bi = (m + ni)3 for some
integers m and n. Expanding the cube and equating real and imaginary parts, we get
(8.4)
a = m3 −3mn2,
b = 3m2n −n3.
Any common factor of m and n would arise from these formulas as a common factor of a and
b, so (m, n) = 1. If m ≡n mod 2 then the parametric formulas would imply a ≡−2m3 ≡
0 mod 2 and b ≡2m3 ≡0 mod 2, but a and b are not both even. Thus m ̸≡n mod 2.
Moreover, c3 = (a + bi)(a −bi) = (m + ni)3(m −ni)3 = (m2 + n2)3, so c = m2 + n2.
Conversely, if (m, n) = 1 and m ̸≡n mod 2, then deﬁning a and b by (8.4), and c =
m2 + n2, makes them satisfy a2 + b2 = c3 and a + bi = (m + ni)3. It is left as an exercise
for the reader to check (a, b) = 1.
That the choice of m and n is unique for a and b follows from a + bi = (m + ni)3: the
only cube root of unity in Z[i] is 1, so if m′, n′ work in (8.4) for the same a and b then
(m + ni)3 = (m′ + n′i)3, which implies m + ni = m′ + n′i, so m = m′ and n = n′.
□
The table below gives some solutions to a2 + b2 = c3 with (a, b) = 1.
m
1
2
4
7
9
n
0
1
3
2
5
a = m3 −2mn2
1
2
−44
259
54
b = 3m2n −n3
0
11
117
286
1090
c = m2 + n2
1
5
25
53
106
Unlike a2 + b2 = c2, where every solution in integers is a multiple of a relatively prime
(primitive) solution of the same equation, integral solutions of a2 + b2 = c3 where (a, b) > 1
do not come from relatively prime solutions of the same equation because the exponents are
not all equal. For example, three solutions of a2 + b2 = c3 with (a, b) > 1 are (18, 26, 10),
(5, 10, 5), and (30, 10, 10). Divide through each triple by their greatest common divisor to
get (9, 13, 5), (1,2,1), and (3,1,1), and none of these satisfy a2 + b2 = c3. They satisfy new
equations: a2 + b2 = 2c3, a2 + b2 = 5c3, and a2 + b2 = 10c3, respectively.
The next application uses Z[i] to show a perfect square in Z never comes right before a
perfect cube, except for the pair 0 and 1.
Theorem 8.5. The only x, y ∈Z satisfying y2 = x3 −1 is (x, y) = (1, 0).
Although the cubes are spread out more thinly than the squares in Z, it is not obvious
why they couldn’t come within one of each other many times.
By the way, we know three examples where a cube precedes a square: −1 and 0, 0 and
1, and 8 and 9. However, this corresponds to the equation x3 = y2 −1, which is not the
one we are studying.
Proof. The integer pair (x, y) = (1, 0) obviously ﬁts the equation y2 = x3 −1. We now show
it is the only integral solution.

<!-- page 29 -->
THE GAUSSIAN INTEGERS
29
Write the equation in the form
x3 = y2 + 1,
which has the factored form
(8.5)
x3 = (y + i)(y −i).
The same idea as in the proof of Theorem 8.3 suggests itself: if the two factors on the right
side are relatively prime in Z[i], then since their product is a cube, each factor must be a
cube up to unit multiple, by unique factorization in Z[i]. Moreover, since every unit is a
cube (1 = 13, −1 = (−1)3, i = (−i)3, −i = i3), it can be absorbed into the cube. Thus,
provided we show y + i and y −i are relatively prime, (8.5) tells us y + i and y −i are
themselves cubes.
To see that y +i and y −i are relatively prime, let δ be a common divisor. Then δ divides
their diﬀerence, so δ | 2i. As 2i = (1 + i)2, unique factorization in Z[i] tells us that δ is 1,
1 + i, or (1 + i)2 up to units.
If δ is not a unit, it is divisible by 1 + i, so (1 + i) | x3. Taking norms, 2 | x6, so x is even.
Then y2 + 1 = x3 ≡0 mod 4, so y2 ≡−1 mod 4. But −1 mod 4 is not a square. We have a
contradiction, so δ is a unit.
Now that we know y + i and y −i are relatively prime, we must have (as argued already)
y + i = (m + ni)3
for some m, n ∈Z. Expanding the cube and equating real and imaginary parts,
y = m3 −3mn2 = m(m2 −3n2),
1 = 3m2n −n3 = n(3m2 −n2).
The equation on the right tells us n = ±1. If n = 1, then 1 = 3m2 −1, so 3m2 = 2, which
has no integer solution. If n = −1, then 1 = −(3m2 −1), so m = 0. Therefore y = 0, so
x3 = y2 + 1 = 1. Thus x = 1.
□
Remark 8.6. Using Z[i], in 1850 V. A. Lebesgue [2] showed for all m ≥2 that the equation
y2 = xm −1 has no solution in nonzero integers x and y.
We end this section by returning to the theme connected to our ﬁrst application: sums
of two squares. We saw that a prime is a sum of two squares in just one way. But other
numbers can be sums of two squares in more than one way, such as 50 and 65. We now use
arithmetic in Z[i] to systematically construct integers that are sums of two squares in more
than one way. Consider the factorizations of 5 and 13:
5 = (1 + 2i)(1 −2i),
13 = (2 + 3i)(2 −3i).
We can combine these factors in two ways:
5 · 13 = ((1 + 2i)(2 + 3i))((1 −2i)(2 −3i)) = ((1 + 2i)(2 −3i))((1 −2i)(2 + 3i)).
After some algebra, this becomes
65 = (−4 + 7i)(−4 −7i) = (8 + i)(8 −i).
Thus
65 = 42 + 72 = 82 + 12.
Diﬀerent representations of an integer as a sums of two squares in Z correspond to rear-
ranging prime factors in Z[i]!

<!-- page 30 -->
30
KEITH CONRAD
As another example, using 5 = (1 + 2i)(1 −2i) and 10 = (1 + 3i)(1 −3i), we can write
down two diﬀerent Gaussian integers with norm 50:
(1 + 2i)(1 + 3i) = −5 + 5i,
(1 + 2i)(1 −3i) = 7 −i.
Taking the norm, we ﬁnd 50 = 52 + 52 = 12 + 72.
Let’s ﬁnd an integer that is a sum of two squares in three diﬀerent ways. We use the
primes 5, 13, and 17. In Z[i],
5 = (1 + 2i)(1 −2i),
13 = (2 + 3i)(2 −3i),
17 = (1 + 4i)(1 −4i).
Consider the following products:
(1 + 2i)(2 + 3i)(1 + 4i) = −32 −9i,
(1 −2i)(2 + 3i)(1 + 4i) = 12 + 31i,
(1 + 2i)(2 −3i)(1 + 4i) = 4 + 33i.
Their common norm is 5 · 13 · 17 = 1105, so
1105 = 92 + 322 = 122 + 312 = 42 + 332.
Pursuing this theme further, you can try your hand at systematically (i.e., without having
to guess) constructing integers that are a sum of two squares in four, ﬁve, or more diﬀerent
ways.
9. Primes in Z[i]
Theorem 6.3 gave a suﬃcient condition for a Gaussian integer to be prime: it has prime
norm. We saw also that this condition was not necessary: 3 is prime but its norm is 9,
which is not prime.
Our goal in this section is to classify the primes in Z[i]. We don’t mean this in an absolute
sense, but rather in terms of the primes in Z.
Lemma 9.1. Let π be a prime in Z[i]. For some prime p in Z+, π | p.
The point of this lemma is that it tells us we can get a handle on all Gaussian primes by
factoring every prime in Z+ in the Gaussian integers: each Gaussian prime is a factor of an
ordinary prime.
Proof. It is always the case that π divides some positive integer, namely its norm: N(π) =
ππ, so π | N(π) in Z. Since N(π) > 1, we write N(π) as a product of primes in Z+:
N(π) = p1p2 · · · pr.
Since π | N(π) in Z[i], and π is prime in Z[i], we must have π | pj for some j by Lemma
6.5.
□
As noted already, this lemma tells us the prime factors in Z[i] of the primes in Z+ will
give us all Gaussian primes. Here are Gaussian prime factorizations of the ﬁrst three prime
numbers:
2 = (1 + i)(1 −i),
3 = 3,
5 = (1 + 2i)(1 −2i).
For instance, by unique factorization, any other Gaussian prime factor of 5 is a unit multiple
of 1 + 2i or 1 −2i, which gives one of the following numbers:
1 + 2i,
−1 −2i,
−2 + i,
2 −i,
1 −2i,
−1 + 2i,
−2 −i,
2 + i.
Up to unit multiple, these eight numbers are really just two numbers: 1 + 2i and 1 −2i.

<!-- page 31 -->
THE GAUSSIAN INTEGERS
31
Theorem 9.2. A prime p in Z+ is composite in Z[i] if and only if it is a sum of two
squares.
Thus, any prime p in Z+ that is not a sum of two squares is not composite in Z[i], so it
stays prime in Z[i]. Examples include 3, 7, 11, and 19.
Proof. If the prime p in Z+ is composite in Z[i], let a non-trivial factorization be p = αβ.
Then, taking norms, p2 = N(α) N(β). Since the factorization of p was nontrivial, and p > 0,
we must have N(α) = p. Then, writing α = a + bi, the norm equation tells us p = a2 + b2.
Conversely, suppose a prime p in Z+ is a sum of two squares, say p = a2 + b2. Then in
Z[i] we get the non-trivial factorization
p = (a + bi)(a −bi),
so p is composite in Z[i].
□
The ﬁrst primes in Z+ that are sums of two squares are 2, 5, 13, 17, and 29:
2 = 12 + 12,
5 = 12 + 22,
13 = 22 + 32,
17 = 12 + 42,
29 = 22 + 52.
Therefore each of these prime numbers is composite in Z[i], e.g. 29 = (2 + 5i)(2 −5i).
This is a Gaussian prime factorization, since the factors have prime norm (and thus are
themselves prime in Z[i]). The factorization of 2 is special, since its prime factors are unit
multiples of each other: 1 −i = −i(1 + i). In other words,
2 = −i(1 + i)2.
Corollary 9.3. If a prime p in Z+ is composite, and p ̸= 2, then up to unit multiple p has
exactly two Gaussian prime factors, which are conjugate and have norm p.
Proof. By Theorem 9.2, when p is composite we have
p = a2 + b2 = (a + bi)(a −bi)
for some a, b ∈Z. Since a + bi and a −bi have prime norm p, they are prime in Z[i]. Could
they be unit multiples? We consider all four ways this could happen and show each one
leads to a contradiction.
If a+bi = a−bi, then b = 0 and p = a2, which is a contradiction. If a+bi = −(a−bi), then
a = 0 and we get a contradiction again. If a+bi = i(a−bi), then b = a and p = a2+a2 = 2a2,
but p ̸= 2. We have a contradiction. The ﬁnal case, when a + bi = −i(a −bi), again implies
the contradiction p = 2a2.
□
Corollary 9.4. If a prime p in Z+ satisﬁes p ≡3 mod 4, then it is not a sum of two
squares in Z and it stays prime in Z[i].
Proof. Once we show p is not a sum of two squares in Z, it is prime in Z[i] by Theorem 9.2.
We consider the squares modulo 4: the only squares are 0 and 1. Adding them together
modulo 4 gives us 0 (= 0 + 0), 1(= 1 + 0 or 0 + 1), and 2(= 1 + 1). We can’t get 3, so any
number that is ≡3 mod 4 is not a sum of two squares in Z.
□
We now know how 2 factors into Gaussian primes and how any prime p in Z+ with
p ≡3 mod 4 factors in Z[i] (it doesn’t factor).
What about the primes p ≡1 mod 4?
The ﬁrst such primes are 5, 13, 17, and 29. These are primes we saw earlier among the
sums of two squares, so they are all composite in Z[i] by Theorem 9.2 and they factor into
conjugate Gaussian primes by Theorem 9.3. Is every prime p ≡1 mod 4 a sum of two
squares? Numerical evidence suggests it is true, so we make the

<!-- page 32 -->
32
KEITH CONRAD
Conjecture 9.5. For a prime p in Z+, the following conditions are equivalent:
(1) p = 2 or p ≡1 mod 4,
(2) p = a2 + b2 for some a, b ∈Z.
The easier condition to check in practice is (1). The more interesting condition, at least
from the viewpoint of ordinary arithmetic, is (2). It is easy to see that (2) implies (1): if
p = a2 + b2 for some a and b, then p mod 4 is a sum of two squares. The squares mod 4 are
0 and 1, so a sum of two squares mod 4 could be 0, 1, or 2. Therefore p ≡0, 1, 2 mod 4.
The ﬁrst choice is impossible (since p is prime) and the third only happens for p = 2. (This
argument may look familiar. You already met it in the proof of Corollary 9.4.)
What about the proof that (1) implies (2) (which is the more interesting direction any-
way)? It turns out to be convenient to insert an additional property in between them,
involving a polynomial modulo p.
Theorem 9.6. Let p be a prime in Z+. The following conditions are equivalent:
(1) p = 2 or p ≡1 mod 4,
(2) the congruence x2 ≡−1 mod p has a solution.
(3) p = a2 + b2 for some a, b ∈Z.
Proof. We have already shown (3) implies (1).
To show (1) implies (2), we may take p ̸= 2. Consider the polynomial factorization
(9.1)
T p−1 −1 = (T (p−1)/2 −1)(T (p−1)/2 + 1)
with mod p coeﬃcients. We are going to count roots of these polynomials modulo p. Recall
that a polynomial of degree d has no more than d roots modulo p.
By Fermat’s little theorem, the left side of (9.1) has p−1 diﬀerent roots modulo p, namely
the non-zero integers modulo p. The ﬁrst polynomial on the right side of (9.1) has degree
(p −1)/2, so it has at most (p −1)/2 roots modulo p. Therefore the second polynomial
T (p−1)/2 + 1 must have roots modulo p: some integer c satisﬁes c(p−1)/2 ≡−1 mod p. Since
p ≡1 mod 4, (p −1)/2 is an even integer: if p = 4k + 1 then (p −1)/2 = 2k. Therefore
(ck)2 ≡−1 mod p, which proves (2).
To show (2) implies (3), we are going to show (2) implies p is composite in Z[i]. Then
Theorem 9.2 says p is a sum of two squares.
View the congruence in (2) as a divisibility relation in Z. When x2 ≡−1 mod p for some
x ∈Z, p | (x2 + 1) in Z. Now consider this divisibility in Z[i], where we can factor x2 + 1:
(9.2)
p | (x + i)(x −i).
To show p is composite in Z[i], we argue by contradiction. If p is a Gaussian prime, then
by (9.2) p | (x + i) or p | (x −i) in Z[i]. Therefore some Gaussian integer m + ni satisﬁes
p(m + ni) = x ± i, but look at the imaginary part: pn = ±1. This is impossible! We have a
contradiction, which proves p is composite in Z[i], so p is a sum of two squares by Theorem
9.2.
□
Be sure you make note of the way we used the condition p ≡1 mod 4 in the proof that
(1) implies (2).
We can now summarize the factorization of primes in Z+ into Gaussian prime factors.
Theorem 9.7. Let p be a prime in Z+. The factorization of p in Z[i] is determined by
p mod 4 :
i) 2 = (1 + i)(1 −i) = −i(1 + i)2.

<!-- page 33 -->
THE GAUSSIAN INTEGERS
33
ii) If p ≡1 mod 4 then p = ππ is a product of two conjugate primes π, π that are not
unit multiples.
iii) If p ≡3 mod 4 then p stays prime in Z[i].
Proof. Part i is a numerical check. Part ii is a consequence of Corollary 9.3 and Theorem
9.6. Part iii is Corollary 9.4.
□
Example 9.8. The prime 61 satisﬁes 61 ≡1 mod 4, so 61 has two conjugate Gaussian
prime factors, coming from an expression of 61 as a sum of two squares. Since 61 = 52 +62,
61 = (5 + 6i)(5 −6i).
Combining the factorizations in Theorem 9.7 with Lemma 9.1, we now have a description
of all the Gaussian primes in terms of the primes in Z+.
Theorem 9.9. Every prime in Z[i] is a unit multiple of the following primes:
i) 1 + i
ii) π or π, where N(π) = p is a prime in Z+ that is ≡1 mod 4.
iii) p, where p is a prime in Z+ with p ≡3 mod 4.
Proof. Lemma 9.1 tells us any Gaussian prime is a factor of a prime in Z+. Theorem 9.7
and unique factorization in Z[i] tell us how the primes in Z+ factor in Z[i] up to unit
multiple.
□
The Gaussian primes in parts i and ii of Theorem 9.9 have prime norm in Z, while
the primes occurring in part iii have norm p2, where p ≡3 mod 4. Moreover, when p ≡
3 mod 4, its unit multiples in Z[i] are ±p and ±ip, which have real or imaginary part 0.
Thus, although the converse to Theorem 6.3 is not strictly true, we see it is true for the
“interesting” Gaussian integers, namely the ones with non-zero real and imaginary part:
write α = a + bi and suppose a and b are both non-zero in Z. Then α is prime in Z[i] if
and only if N(α) is prime in Z!
Our classiﬁcation of Gaussian primes tells us that a Gaussian prime has norm either p or
p2, where p is the prime in Z+ that the Gaussian prime divides. In particular, any Gaussian
prime other than 1 + i (and its unit multiples) has an odd norm. Thus, a Gaussian integer
that is not divisible by 1 + i must have a norm that is odd, so any Gaussian integer with an
even norm must be divisible by 1 + i. This is something we already checked, using simple
algebra, back in Corollary 2.5. But now we understand why it is true from a higher point
of view, in connection with unique factorization in Z[i]: Corollary 2.5 is true because every
Gaussian integer with norm greater than 1 is a product of Gaussian primes and 1 + i is the
only Gaussian prime up to unit multiple with even norm.
As an application of Theorem 9.7, we now classify all the positive integers that are sums
of two squares.
Theorem 9.10. An integer greater than 1 is a sum of two squares exactly when any prime
factor that is ≡3 mod 4 occurs with even multiplicity.
Proof. First we show any integer having even multiplicity at its prime factors that are
≡3 mod 4 can be written as a sum of two squares.
We know sums of two squares are closed under multiplication (view them as norms of
Gaussian integers and use multiplicativity of the norm). Any prime p ≡1 mod 4 is a sum
of two squares by Theorem 9.6, as is 2. While a prime p ≡3 mod 4 is not a sum of two
squares, any even power of it is (since an even power is itself a square). Therefore a product
of 2, primes ≡1 mod 4, and even powers of primes ≡3 mod 4 is a sum of two squares.

<!-- page 34 -->
34
KEITH CONRAD
Now we treat the converse direction: each n > 1 that is a sum of two squares has even
multiplicity at any prime factor that is ≡3 mod 4. We argue by induction on n. The result
is true when n = 2, as 2 is a sum of two squares and it has no prime factors that are
≡3 mod 4.
Assume n ≥3, n is a sum of two squares, and the theorem has been checked for sums of
two squares greater than 1 and less than n. If n has no prime factors that are ≡3 mod 4,
then there is nothing to prove. Thus, we may assume n has a prime factor p with p ≡
3 mod 4. Write n = a2 + b2, so p | (a2 + b2) in Z. In Z[i], we write this as
(9.3)
p | (a + bi)(a −bi).
Since p ≡3 mod 4, it is prime in Z[i]. Therefore from (9.3) we know p | (a+bi) or p | (a−bi)
in Z[i]. Both cases imply p | a and p | b in Z. (Why?) Write a = pa′ and b = pb′ for integers
a′ and b′. Then
n = p2(a′2 + b′2).
If n = p2 we are done, so we may suppose n > p2. The integer n′ = n/p2 = a′2 + b′2 is a
sum of two squares and it is greater than 1 and less than n. By our inductive hypothesis,
every prime factor of n′ that is ≡3 mod 4 has even multiplicity. Since the only diﬀerence
between n and n′ is the even power p2, we conclude that every prime factor of n that is
≡3 mod 4 has even multiplicity. That ends the inductive step.
□
Example 9.11. The number 35 = 5 · 7 has a prime factor that is ≡3 mod 4, namely 7.
This factor appears with multiplicity 1, so 35 is not a sum of two squares. Neither is 5k · 7ℓ
for any odd exponent ℓ> 0. But 5 · 72 = 245 is a sum of two squares: 245 = 72 + 142.
Theorem 9.10 describes the sums of two squares in terms of a condition on the prime
factors that are ≡3 mod 4. In particular, applying the condition in the theorem to decide
whether n is a sum of two squares requires that we factor n.
Appendix A. What did Gauss do in Z[i]?
The paper [1], where Gauss introduced Z[i], is written in Latin. If you are not put oﬀby
that, then you might be interested in following the hyperlink to [1] in the bibliography to
see how Gauss writes about topics we have discussed. Here are sections in [1] to look at.
• Section 31: units, associates, norm
• Section 32: ratios, square roots
• Section 33: composites and primes (classifying the latter)
• Section 37: prime factorization in Z[i], its uniqueness in the theorem on p. 108
• Section 39: if a + bi ̸= 0, then |Z[i](a + bi)| = a2 + b2
• Section 40: Z[i]/(a+bi) has representatives 0, 1, 2, . . . , n−1 when gcd(a, b) = 1 and
n = a2 + b2
• Section 41: Gives representatives for Z[i]/(a + bi) when gcd(a, b) > 1
• Sections 42, 43: Z[i] has a division algorithm (explained geometrically)
• Section 46: Euclid’s algorithm in Z[i] for the gcd up to unit multiple (p. 118)
• Section 47: Bezout’s theorem in Z[i], and an example with 31 + 6i and 11 −20i:
1 = (31 + 6i)(5 −6i) + (11 −20i)(−10 −4i)
• Section 51: Fermat’s little theorem
At the end of Section 38, after presenting the geometric way to think about complex
numbers as points in a plane, Gauss says that complaints about such numbers being unin-
tuitive are due in large part just to the terminology: “The diﬃculties in which the theory

<!-- page 35 -->
THE GAUSSIAN INTEGERS
35
of imaginary quantities is thought to be involved have, to a large extent, originated from
inadequate names (some have even used the name impossible quantities). If, starting from
the concepts oﬀered by the possibilities of two dimensions (as are seen in their greatest pu-
rity in the intuitions of space), we had called positive quantities direct, negative quantities
inverse, and imaginary quantities lateral, then we would have found simplicity instead of
frustration, and clarity instead of obscurity.”2
Appendix B. Pythagorean triples in Z[i]
Theorem 8.3 described the solutions to x2 + y2 = z2 in positive integers where x, y, and
z have no common factor. In this appendix we’ll work out an analogous result for solutions
to x2 + y2 = z2 in Gaussian integers, except the positivity condition will be dropped.
When α2 + β2 = γ2 in Z[i], any common factor of two of α, β, and γ is a factor of the
third (why?), so we can divide through by a gcd and assume the three numbers α, β, and
γ are pairwise relatively prime. Such triples are called primitive. Because −1 = i2, we can
put any term on the right side at the cost of multiplying inside by i, e.g., if α2 + β2 = γ2
then α2 + (iγ)2 = (iβ)2.
At least one of α, β, and γ is divisible by 1 + i; otherwise all three are ≡1 mod 1 + i,
which is impossible since 12 + 12 ̸≡12 mod 1 + i. We can’t have two of α, β, and γ divisible
by 1 + i since then all three are and that contradicts primitivity of the triple. So just one
term is divisible by 1 + i. By moving the three terms around (using multiplication by i,
which is something unavailable in Z), we may assume β is divisible by 1 + i and α and γ
are not.
Theorem B.1. Every primitive Pythagorean triple (α, β, γ) in Z[i] with β divisible by 1+i
and β ̸= 0 has the form
α = u(z2 −w2),
β = 2uzw,
γ = u(z2 + w2),
where u ∈{±1, ±i}, z and w are nonzero in Z[i], (z, w) = 1, and z ̸≡w mod 1 + i.
Conversely, for any such choice of z and w, the above formula is a primitive Pythagorean
triple in Z[i] where β is divisible by 1 + i and nonzero. Two choices of u, z, w and u′, z′,w′
describe the same triple (α, β, γ) if and only if there’s a unit ε such that u′ = ε2u, z′ = εz,
and w′ = εw.
Proof. The proof of 8.3 used the Gaussian integers to write a2 +b2 as (a+bi)(a−bi) when a
and b are integers. Although α2+β2 = (α+βi)(α−βi) when α and β are Gaussian integers,
this kind of factorization will not be useful because α+βi does not determine α and β when
they are in Z[i] (rather than in Z). So we’ll prove this theorem using factorizations in a
diﬀerent way than in the proof of Theorem 8.3.
Assume (α, β, γ) is a primitive Pythagorean triple in Z[i] such that β is divisible by 1 + i
and nonzero. Then α and γ are not divisible by 1 + i. Write
(B.1)
β2 = γ2 −α2 = (γ + α)(γ −α).
2The original text: “Diﬃcultates, quibus theoria quantitatum imaginariarum involuta putatur, ad magnam
partem a denominationibus parum idoneis originem traxerunt (quum adeo quidam usi sint nomine absono
quantitatum impossibilium). Si, a conceptibus, quos oﬀerunt varietates duarum dimensionum (quales in
maxima puritate conspiciuntur in intuitionibus spatii), profecti quantitates positivas directas, negativas
inversas, imaginarias laterales nuncupavissemus, pro tricis simplicitas, pro caligine claritas successisset.”

<!-- page 36 -->
36
KEITH CONRAD
Since α, γ ≡1 mod 1 + i we have γ + α and γ −α both divisible by 1 + i. Now divide
through (B.1) by (1 + i)2:
(B.2)

β
1 + i
2
= γ + α
1 + i
γ −α
1 + i
with all ratios in Z[i].
Claim: The Gaussian integers (γ + α)/(1 + i) and (γ −α)/(1 + i) have gcd 1 or 1 + i.
Let δ be a common factor of (γ +α)/(1+i) and (γ −α)/(1+i). Then δ divides their sum
and diﬀerence: δ | (1 + i)γ and δ | (1 + i)α. Since α and γ are relatively prime, δ | (1 + i),
so primality of 1 + i implies δ is 1 or 1 + i up to unit multiple. That proves the claim.
Case 1: (γ + α)/(1 + i) and (γ −α)/(1 + i) have gcd 1. We’re going to show this case
leads to a contradiction.
The two factors on the right in (B.2) are relatively prime, so their product being a square
makes each factor a square up to unit multiple. Then
γ + α
1 + i = uz2
and
γ −α
1 + i = u−1w2
for some unit u and relatively prime Gaussian integers z and w. Multiplying both equations
by 1 + i and then adding and subtracting the equations to isolate γ and α, we get
2γ = (uz2 + u−1w2)(1 + i),
2α = (uz2 −u−1w2)(1 + i).
Since 2 = −i(1 + i)2, divide through by 1 + i:
−i(1 + i)γ = uz2 + u−1w2,
−i(1 + i)α = uz2 −u−1w2.
Reducing the ﬁrst equation modulo 1 + i, we get 0 ≡z2 + w2 ≡z + w mod 1 + i, so
z ≡−w ≡w mod 1 + i, so relative primality of z and w implies z, w ≡1 mod 1 + i.
Squaring, we get z2, w2 ≡1 mod 2, so
−i(1 + i)γ ≡u + u−1 ≡u(1 + u2) mod 2.
Since u2 = ±1, we have 1 + u2 ≡0 mod 2. Then, since 2 = −i(1 + i)2,
−i(1 + i)γ ≡0 mod 2 =⇒−iγ ≡0 mod 1 + i,
which contradicts γ not being divisible by 1 + i. We have a contradiction.
Case 2: (γ + α)/(1 + i) and (γ −α)/(1 + i) have gcd 1 + i.
The two factors on the right in (B.2) have gcd 1+i, so γ +α and γ −α are both divisible
by 2. Writing that as γ ≡±α mod 2, we get γ2 ≡α2 mod 4, so β2 = γ2 −α2 ≡0 mod 4, so
2 | β. Now in (B.1) we can divide both sides by 4:
β
2
2
= γ + α
2
γ −α
2
,
with the two factors on the right being relatively prime. Since their product is a square, we
get
(B.3)
γ + α
2
= uz2
and
γ −α
2
= u−1w2
for some unit u and relatively prime Gaussian integers z and w. Then
β2 = (γ + α)(γ −α) = 4z2w2 =⇒β = ±2zw.

<!-- page 37 -->
THE GAUSSIAN INTEGERS
37
Since β ̸= 0, z and w are nonzero. Solving for γ and α in (B.3) by adding and subtracting
the two equations,
γ = uz2 + u−1w2 = u(z2 + (u−1w)2),
α = uz2 −u−1w2 = u(z2 −(u−1w)2).
Since β = ±2zw = ±2uz(u−1w), relabel u−1w as w to get
α = u(z2 −w2),
β = ±2uzw,
γ = u(z2 + w2).
If the expression for β has a plus sign we are done. If it has a minus sign, we can rename
−z as z since z2 = (−z)2, and again we’re done. If z ≡w mod 1+i then z2 ≡w2 mod 1+i,
so z2 + w2 and z2 −w2 are both divisible by 1 + i, which contradicts α and γ not being
divisible by 1 + i. Thus z ̸≡w mod 1 + i.
This completes the proof that all primitive Pythagorean triples in Z[i] with β divisible
by 1 + i and nonzero have the desired form.
Conversely, if α = u(z2 −w2), β = 2uzw, and γ = u(z2 + w2), where u is a unit, z and w
are nonzero and relatively prime in Z[i], and z ̸≡w mod 1 + i, then it’s easy to check that
α2 + β2 = γ2 and β ̸= 0. Since z ̸≡w mod 1 + i, we have z2 ̸≡w2 mod 1 + i, so α and β are
not divisible by 1 + i. Any common Gaussian prime factor of α and β is not 1 + i, so it has
to divide z or w by the formula for β. Then it divides γ, but z2 −w2 is relatively prime to
z and to w due to z and w being relatively prime, so we have a contradiction. Thus α and
β are relatively prime, so (α, β, γ) is a primitive Pythagorean triple in Z[i].
If u′, z′, and w′ parametrically describe (α, β, γ) under the same conditions as u, z, and
w, then
β
α + γ = 2uzw
2uz2 = w
z ,
so w/z = w′/z′. These are equal reduced form ratios, so there’s a unit ε such that w′ = εw.
Then z′ = εz, so α = u′(z′2 −w′2) = u′ε2(z2 −w2), showing u′ε2 = u. Since ε2 = ±1,
u′ = ε2u.
If u, z, and w ﬁt the conditions of the theorem to parametrically describe a primitive
Pythagorean triple (α, β, γ) where β is divisible by 1 + i and nonzero, then for any unit ε
the numbers ε2u, εz, and εw also parametrically describe (α, β, γ).
□
Some primitive Pythagorean triples in Z[i], using u = 1 in the parametric formula, are
in the table below.
z
1 + i
2 + i
2 −i
3 + i
4 + i
w
1
1 + i
1 + i
3
2
α = z2 −w2
−1 + 2i
3 + 2i
3 −6i
−1 + 6i
11 + 8i
β = 2zw
2 + 2i
2 + 6i
6 + 2i
18 + 6i
16 + 4i
γ = z2 + w2
1 + 2i
3 + 6i
3 −2i
17 + 6i
19 + 8i
References
[1] C. F. Gauss, Theoria Residuorum Biquadraticorum, Commentatio Secunda, pp. 93-148 in Werke,
Band II, K¨oniglichen Gesellschaft der Wissenschaften, G¨ottingen, 1876. URL https://archive.org/
details/117771763 002/page/n103/mode/2up
[2] V. A. Lebesgue, Sur l’impossibilit´e, en nombres entiers, de l’´equation xm = y2 + 1, Nouv. Ann. Math. 9
(1850), 178–181. URL https://eudml.org/doc/96100.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*