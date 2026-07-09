# Well-Defined Functions

> **Source**: https://kconrad.math.uconn.edu/blurbs/welldefined.pdf  
> **Author**: Keith Conrad  
> **Topic**: proof_writing  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
WELL-DEFINED FUNCTIONS
KEITH CONRAD
1. Introduction
When deﬁning an operation or function or formula, care has to be taken in the deﬁnition
if the operation or function or formula involves making choices along the way.
Example 1.1. In elementary school we learned how to add fractions by a rule amounting
to
(1.1)
a
b + c
d = ad + bc
bd
.
For instance,
1
2 + 1
3 = 5
6,
2
4 + 1
3 = 10
12 = 5
6.
What is not emphasized in elementary school is that changing the numerator and denomi-
nator without changing the fraction (e.g., writing 1/2 as 2/4) does not change the answer.
All students implicitly accept this, but for a rigorous development of fractions this feature
should be explained: if a/b = a′/b′ and c/d = c′/d′ why is (ad+bc)/bd = (a′d′ +b′c′)/(b′d′)?
Here is how this can be shown. If a/b = a′/b′ and c/d = c′/d′ then ab′ = a′b and cd′ = c′d
in Z. To show (ad+bc)/bd = (a′d′+b′c′)/(b′d′) we check that (ad+bc)(b′d′) = (a′d′+b′c′)(bd):
(ad + bc)(b′d′) = (ab′)dd′ + bb′(cd′) = (a′b)dd′ + bb′(c′d) = (a′d′ + b′c′)(bd). ✓
Someone may ask why we can’t add fractions using the diﬀerent rule
(1.2)
a
b ⊕c
d = a + c
b + d,
where we write ⊕rather than + to emphasize that this is a diﬀerent operation.
This
operation doesn’t make sense (ignore that it isn’t actual addition of fractions), since its
output can change if we change a numerator and denominator without changing the fraction,
e.g.,
1
2 ⊕1
3 = 2
5,
2
4 ⊕1
3 = 3
7,
and 2/5 ̸= 3/7.
We say that + in (1.1) is a well-deﬁned operation on fractions while (1.2) is not a well-
deﬁned operation on fractions. If you change the way you write fractions (diﬀerent numer-
ators and denominators, but keeping the same values of the fractions), the answer does not
change in (1.1) but it does change in (1.2).1
1We could make (1.2) well-deﬁned by insisting the fractions a/b and c/d are in reduced form with positive
denominators. A fraction can be written like that in just one way. The resulting operation on fractions, at
least those that are positive, is called the mediant and occurs in the study of Farey fractions and continued
fractions.
1

<!-- page 2 -->
2
KEITH CONRAD
Example 1.2. In elementary school we are told that the number π is the ratio C/D where
C is the circumference and D is the diameter of a circle. Did you ever ask yourself why this
is the same for all circles? Why does changing the size of a circle not change the ratio C/D?
Don’t try to show that by using the formula C = 2πr, as it is just another version of the
proposed deﬁnition π = C/D, since D = 2r, so it would be circular reasoning (literally).
The history behind this formula, going back to ancient Greece, is in [1].
That the ratio C/D is independent of the choice of circle in the plane tells us that π is
well-deﬁned.
Example 1.3. In calculus,
R b
a f(x)dx can be computed as
Z b
a
f(x)dx = F(b) −F(a),
where F(x) is an arbitrary anti-derivative of f(x) on [a, b], i.e., F ′(x) = f(x) for all x in [a, b].
This formula for
R b
a f(x)dx involves a choice of anti-derivative for f(x), but the formula does
not depend on the choice: every anti-derivative G(x) of f(x) on [a, b] diﬀers from F(x) by
a constant, say G(x) = F(x) + C for all x in [a, b], and changing the anti-derivative G(x)
does not change the diﬀerence of its values at the endpoints:
G(b) −G(a) = (F(b) + C) −(F(a) + C) = F(b) −F(a).
So the diﬀerence of the values of an anti-derivative of f(x) at x = a and x = b is independent
of the choice of anti-derivative of f(x) on the interval [a, b].2
In contrast, the “rule” F(b)+F(a) depends on the choice of anti-derivative of f(x), since
G(b) + G(a) = (F(b) + C) + (F(a) + C) = F(b) + F(a) + 2C,
which is a new value if C ̸= 0. Taking diﬀerences in an anti-derivative cancels the eﬀect of
the undetermined additive constant, so the expression F(b) −F(a) is a well-deﬁned value
based on the original input function f(x) and the interval [a, b].
2. Well-definedness in modular arithmetic
In algebra, there are many times when we want to deﬁne a function on Z/(m), the
integers modulo m. Usually the value of the function on a congruence class mod m involves
a choice of representative for that congruence class, and we must check this is well-deﬁned,
i.e., the function’s value does not depend on the choice of representative.
Example 2.1. If a ≡b mod 2, then (−1)a = (−1)b. Therefore, we have a well-deﬁned
function f : Z/(2) →{±1} given by the rule
f(a mod 2) = (−1)a.
You need to train yourself to check that functions you want to deﬁne on Z/(m) in terms
of congruence class representatives mod m are in fact well-deﬁned (that is, independent of
the choices made). The following table lists examples of well-deﬁned functions on various
Z/(m)’s. Some functions that are not well-deﬁned, i.e., are nonsense, will be given later.
2This is why in physics, potential energy has no intrinsic meaning (the zero level of potential energy can be
anywhere), but diﬀerences in potential energy are physically meaningful.

<!-- page 3 -->
WELL-DEFINED FUNCTIONS
3
Group
Rule
Z/(2)
(−1)a
Z/(4)
(−1)a
Z/(4)
ia
Z/(12)
ia
Z/(4)
2a mod 5
Z/(3)
2a mod 7
Z/(3)
a3 mod 9
Z/(4)
a(a−1)
2
mod 2
In all cases, to show a function f : Z/(m) →S that takes values in some set S is well-
deﬁned (that is, makes sense), we must show
a ≡b mod m =⇒f(a mod m) = f(b mod m).
Let’s run through this kind of check for the examples in the table above.
• if a ≡b mod 2, then a = b + 2k for k ∈Z, so (−1)a = (−1)b+2k = (−1)b(−1)2k =
(−1)b.
• if a ≡b mod 4, then a = b + 4k for k ∈Z, so (−1)a = (−1)b+4k = (−1)b(−1)4k =
(−1)b.
• if a ≡b mod 4, then a = b + 4k for k ∈Z, so ia = ib+4k = ibi4k = ib(i4)k = ib.
• if a ≡b mod 12, then a = b + 12k for k ∈Z, so ia = ib+12k = ibi12k = ib(i4)3k = ib.
• if a ≡b mod 4, then a = b + 4k for k ∈Z, so 2a = 2b+4k = 2b(24)k ≡2b mod 5 since
24 = 16 ≡1 mod 5.
• if a ≡b mod 3, then a = b + 3k for k ∈Z, so 2a = 2b+3k = 2b(23)k ≡2b mod 7 since
23 = 8 ≡1 mod 7.
• if a ≡b mod 3, then a = b + 3k for k ∈Z, so a3 = (b + 3k)3 = b3 + 3b2(3k) +
3b(3k)2 + (3k)3 = b3 + 9(b2k + 3bk2 + 3k3) ≡b3 mod 9.
• if a ≡b mod 4, then a(a −1) ≡b(b −1) mod 4. Both a(a −1) and b(b −1) are even,
since a or a −1 is even and b or b −1 is even. Therefore we can divide both sides
of the congruence and the modulus by 2 to obtain a(a−1)
2
≡b(b−1)
2
mod 2.
Before looking at more complicated examples that show how to check a function on
Z/(m) is well-deﬁned, let’s see why some “functions” on Z/(m) are not well-deﬁned.
Group
Bad Rule
Z/(3)
(−1)a
Z/(5)
2a mod 5
Z/(3)
a2 mod 9
Z/(2)
a(a−1)
2
mod 2
To show a rule introduced on Z/(m) is not well-deﬁned, we just need to ﬁnd an example
of a and b with a ≡b mod m and the rule leads to diﬀerent values in the two cases:
• (−1)a is not a well-deﬁned function on Z/(3), since 4 ≡1 mod 3, but (−1)4 = 1
while (−1)1 = −1.
• 2a mod 5 is not a well-deﬁned function on Z/(5) since 5 ≡0 mod 5 and 25 = 32 ≡
2 mod 5 while 20 ≡1 mod 5.
• 5 ≡2 mod 3, but 52 = 25 ≡7 mod 9 and 22 ≡4 mod 9. (Compare this with cubing,
as in the ﬁrst table: 53 ≡23 mod 9.)

<!-- page 4 -->
4
KEITH CONRAD
• 5 ≡3 mod 2 and 5(5−1)
2
≡0 mod 2 while 3(3−1)
2
≡1 mod 2. (Compare with the ﬁrst
table, where we saw a(a−1)
2
mod 2 is well-deﬁned when we treat a as belonging to
Z/(4) instead of Z/(2).)
While showing a function is not well-deﬁned requires just one counterexample, as above,
to show a function is well-deﬁned requires more work than checking one example! You must
verify that the rule for the function is truly independent of the representative you pick from
the congruence class, for all congruence classes. Look again at the proofs above that the
various well-deﬁned functions given earlier in the ﬁrst table are in fact well-deﬁned.
There is a point of terminology worth noting here. Speaking about “a well-deﬁned func-
tion” is in some sense an abuse of language, since a function has to make sense before it
is really called a function in the ﬁrst place. However, the conventional manner of writing
and speaking is to introduce a formula on some Z/(m) and call it a function before right
away doing the check that it is well-deﬁned (that is, it is independent of the choice of
representative) and thus worthy of being called a function.
Now that we have seen how to check a function is or is not well-deﬁned for some explicit
choices of the modulus, we consider some situations where the modulus is a parameter (it
is not ﬁxed to a speciﬁc value).
Theorem 2.2. The function Z/(m) →Z given by f(a mod m) = (a, m) is well-deﬁned. In
other words, the greatest common divisor of an integer with m does not change if we adjust
the integer modulo m.
Let’s see what the theorem is saying in an example before we prove the theorem. In
Z/(10) the congruence class of 4 is a list of integers {. . . , −6, 4, 14, 24, . . . } and every single
integer in this congruence class has the same gcd with 10: gcd(4, 10) = 2, gcd(14, 10) = 2,
gcd(−6, 10) = 2, and so on. If a ≡4 mod 10 then gcd(a, 10) = 2.
Proof. Let a ≡b mod m, say a = b + mk for k ∈Z. Set d = (a, m) and d′ = (b, m). We will
show d = d′.
Since d divides both a and m, it divides a −mk = b. Thus d is a common divisor of b
and m, so d ≤d′.
Since d′ divides both b and m, it divides b + mk = a. Thus d′ is a common divisor of a
and m, so d′ ≤d.
Comparing the two inequalities on d and d′, we have d = d′.
□
Theorem 2.3. If G is a ﬁnite group and g ∈G satisﬁes gn = e for some n ∈Z+ then the
function f : Z/(n) →G given by f(a mod n) = ga is well-deﬁned.
Proof. If a ≡b mod n, write a = b + nk for some k ∈Z. Then ga = gb+nk = gb(gn)k = gb
since gn = e.
□
The point of Theorem 2.3 is that, while we are used to viewing ga with a as an integer,
we can also view ga as having the exponent a belong to Z/(n) if gn = e.
Note we do not need n to be the order of g in Theorem 2.3. All that was used in the
proof was the condition gn = e, and that n might well be a multiple of the order. (Recall
the example of (−1)a with a ∈Z/(4).)
Theorem 2.4. If d | n, the reduction map r: Z/(n) →Z/(d) given by the rule r(a mod n) =
a mod d is well-deﬁned.
Proof. If a ≡b mod n, then n | (a −b). Since d | n, we have d | (a −b), so a ≡b mod d.
□

<!-- page 5 -->
WELL-DEFINED FUNCTIONS
5
For example the function r: Z/(10) →Z/(5) where r(a mod 10) = a mod 5 is well-
deﬁned: if two integers are congruent mod 10 then they are also congruent mod 5.
The “function” r: Z/(10) →Z/(4) given by r(a mod 10) = a mod 4 is not well-deﬁned
(it is not a function at all), since 10 ≡0 mod 10 but 10 ̸≡0 mod 4.
3. More examples of well-definedness
In this last section we describe more instances where a deﬁnition is well-deﬁned: rational
powers, a projection formula, and arc length integrals.
Rational powers. Our ﬁrst example is the deﬁnition of rational powers. Fix a > 0. For
each k ∈Z+, a has a unique positive kth root. This number is the unique positive solution
to the equation xk = a and it is often denoted as
k√a. We deﬁne a1/k =
k√a, and for a
fraction m/n where m ∈Z and n ∈Z+, we deﬁne am/n = (a1/n)m = ( n√a)m. There is
absolutely nothing ambiguous about the notation a1/n, but there is something potentially
ambiguous about writing ( n√a)m as am/n: a fraction can be written in many ways as a ratio
of integers m/n (with n > 0), so to show am/n is well-deﬁned we have to show any two ways
of writing a fraction as m/n leads to the same meaning for ( n√a)m.
Theorem 3.1. Fix a positive number a. If m/n = m′/n′ where n and n′ are in Z+ and m
and m′ are in Z, then ( n√a)m = ( n′√a)m′.
Proof. Set u = ( n√a)m and v = ( n′√a)m′. We want to show u = v. Since m/n = m′/n′ and
the denominators are positive, the numerators have the same sign (positive or negative) or
the numerators are both 0.
Case 1: m = m′ = 0. We have u = ( n√a)0 = 1 and v = ( n′√a)0 = 1.
Case 2: m > 0 and m′ > 0. We will show uk = vk for a certain positive integer k, and
then it would follow that u = v by the uniqueness of the kth root of positive numbers.
Since u involves an nth root and v involves an n′th root, we compute
un = (( n√a)m)n = (( n√a)n)m = am
and
vn′ = (( n′√a)m′)n′ = (( n′√a)n′)m′ = am′.
Since m/n = m′/n′, we have nm′ = n′m, so we further compute
(un)m′ = (am)m′ = amm′,
(vn′)m = (am′)m = am′m = amm′.
Both expressions are amm′, so unm′ = vn′m. The exponents here are equal in Z+, so by the
uniqueness of the kth root when k = nm′ = n′m, we have u = v.
Case 3: m < 0 and m′ < 0. From m/n = m′/n′ we have (−m)/n = (−m′)/n, so by Case
2, ( n√a)−m = ( n′√a)−m′. Inverting both sides, ( n√a)m = ( n′√a)m′.
□
Projection formula.
Our next example is from linear algebra.
For a one-dimensional
subspace L in Rn and each x ∈Rn, ProjL(x) denotes the vector in L for which the
diﬀerence x −ProjL(x) is perpendicular to L, as illustrated in the picture below (n = 2).

<!-- page 6 -->
6
KEITH CONRAD
L
x −ProjL(x)
x
ProjL(x)
Calculations with dot products lead to a formula for this projection:
ProjL(x) =
x · v
v · v

v
where v is a choice of nonzero vector in L. Let’s check this formula is independent of the
choice of v in its deﬁnition.
Theorem 3.2. If L is a one-dimensional subspace of Rn and v is a nonzero vector lying
in L then for each x in Rn, the vector
x · v
v · v

v
is independent of the choice of v.
Proof. Let v and w be two nonzero vectors in L. Since L is one-dimensional, v and w are
scalar multiples of each other, say w = cv with c ∈R. Then c ̸= 0, so
 x · w
w · w

w =
 x · (cv)
(cv) · (cv)

(cv) = c(x · v)
c2(v · v)(cv) = c2(x · v)
c2(v · v)v =
x · v
v · v

v.
□
Arc length integrals. Let C be a “nice” parametrized curve in Rn: there is a function
γ : [a, b] →Rn such that
• C = γ([a, b]),
• γ is continuously diﬀerentiable,
• γ′(t) ̸= 0 for all t.
Using γ we deﬁne the length of C to be
Z b
a
||γ′(t)|| dt.
We will show this notion of length is independent of the choice of parametrization used in
γ: it is unaﬀected by a “change of variables” in the path.
Theorem 3.3. If ϕ: [c, d] →[a, b] is a continuously diﬀerentiable bijection with ϕ′ ̸= 0 then
the composition eγ := γ ◦ϕ: [c, d] →Rn is also a “nice” parametrization of C and the length
of C using eγ is the same3 as the length of C using γ:
Z b
a
||γ′(t)|| dt =
Z d
c
||eγ′(u)|| du.
3Parametrizations of C that are not related in this way might not yield the same notion of length: consider
two parametrizations of a circle that go once and twice around.

<!-- page 7 -->
WELL-DEFINED FUNCTIONS
7
Proof. eγ is “nice” parametrization of C. By C = γ([a, b]) and [a, b] = ϕ([c, d]), we have
C = γ(ϕ([c, d])) = eγ([c, d]). A composition of continuously diﬀerentiable functions is con-
tinuously diﬀerentiable, so eγ is continuously diﬀerentiable. Using the chain rule on eγ = γ◦ϕ,
we have eγ′(u) = (γ ◦ϕ)′(u) = γ′(ϕ(u))ϕ′(u), so eγ′(u) ̸= 0 since γ′(ϕ(u)) ̸= 0 and the scalar
ϕ′(u) is nonzero.
Length is not changed. Since ϕ′ is continuous and nonvanishing, either ϕ′ > 0 on [c, d]
or ϕ′ < 0 on [c, d]. If ϕ′ > 0 then a = ϕ(c), b = ϕ(d), and ||eγ′(u)|| = ||γ′(ϕ(u))|||ϕ′(u)| =
||γ′(ϕ(u))||ϕ′(u), so
Z d
c
||eγ′(u)|| du =
Z d
c
||γ′(ϕ(u))||ϕ′(u) du.
By the substitution t = ϕ(u) we get dt = ϕ′(u) du and
Z d
c
||γ′(ϕ(u))||ϕ′(u) du =
Z ϕ(d)
ϕ(c)
||γ′(t)|| dt =
Z b
a
||γ′(t)|| dt.
If ϕ′ < 0 then a = ϕ(d), b = ϕ(c), and ||eγ′(u)|| = ||γ′(ϕ(u))|||ϕ′(u)| = ||γ′(ϕ(u))||(−ϕ′(u)), so
Z d
c
||eγ′(u)|| du = −
Z d
c
||γ′(ϕ(u))||ϕ′(u) du.
By the substitution t = ϕ(u) we get dt = ϕ′(u) du and
−
Z d
c
||γ′(ϕ(u))||ϕ′(u) du = −
Z ϕ(d)
ϕ(c)
||γ′(t)|| dt = −
Z a
b
||γ′(t)|| dt =
Z b
a
||γ′(t)|| dt.
□
References
[1] D. Richeson, Circular Reasoning: Who First Proved That C Divided by D Is a Constant? College Math.
J. 46 (2015), 162–171.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*