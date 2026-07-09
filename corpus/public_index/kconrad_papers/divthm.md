# Division Theorem in Z and R[T]

> **Source**: https://kconrad.math.uconn.edu/blurbs/divthm.pdf  
> **Author**: Keith Conrad  
> **Topic**: ring_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE DIVISION THEOREM IN Z AND R[T]
KEITH CONRAD
1. Introduction
In both Z and R[T], we can carry out a process of division with remainder.
Theorem 1.1. For any integers a and b, with b nonzero, there are unique integers q and r
such that
a = bq + r,
0 ≤r < |b|.
Theorem 1.2. For any f(T) and g(T) in R[T], with g(T) nonzero, there are unique q(T)
and r(T) in R[T] such that
f(T) = g(T)q(T) + r(T),
r(T) = 0 or deg r(T) < deg g(T).
In both theorems, there are two things to be proved: a quotient and remainder exist sat-
isfying the conclusions, and there is only one such pair. Often when proving such “existence
and uniqueness” theorems, it is simpler to split up the proof into an existence part and a
uniqueness part, which is what we will do.
2. Proof of Theorem 1.1
First we show uniqueness, then existence.
Proof. Uniqueness: Assume there are q1, r1 and q2, r2 in Z which both satisfy the conclusion.
That is,
(2.1)
a = bq1 + r1,
0 ≤r1 < |b|
and
(2.2)
a = bq2 + r2,
0 ≤r2 < |b|.
Comparing the equations in (2.1) and (2.2), we have bq1 + r1 = bq2 + r2. Subtracting,
(2.3)
b(q1 −q2) = r2 −r1.
This implies the diﬀerence r2 −r1 is a multiple of b.
Because r1 and r2 range from 0 to |b| −1, the diﬀerence r2 −r1 is smaller in absolute
value than |b|. (Why?) Feeding this into (2.3) implies
|b(q1 −q2)| = |r2 −r1| < |b|.
The only integer multiple of b which is smaller in absolute value than |b| is 0, so b(q1−q2) = 0.
Because b ̸= 0 (aha...), we must have q1 −q2 = 0, so q1 = q2. Then, returning to (2.3),
r2 −r1 = b · 0 = 0 and we get r1 = r2.
Existence: We give two proofs. The ﬁrst one is very short, while the second looks more
fussy and formal. It is the second proof whose ideas will generalize to the polynomial setting
of Theorem 1.2.
1

<!-- page 2 -->
2
KEITH CONRAD
The most interesting case is b > 0, so we treat this ﬁrst. Consider all the integer multiples
of b: {bq : q ∈Z}. Since b ̸= 0, these multiples are equally spaced all along the real line.
The integer a lies in the interval between two consecutive multiples of b:
bq ≤a < b(q + 1)
for some q ∈Z. (Why is b > 0 necessary here?) Now subtract bq from all terms to get
0 ≤a −bq < b. Let r = a −bq. Then 0 ≤r < b = |b|.
For the second proof of existence when b > 0, we treat the cases a ≥0 and a < 0
separately. That is, we ﬁx b > 0 and will show for each a ≥0 there are appropriate q and
r, and then we will show for each a < 0 there are appropriate q and r.
When a ≥0, we argue by (strong) induction on a. The case a = 0 is trivial: let q = 0
and r = 0. In fact, if 0 ≤a < b we can use q = 0 and r = a. Suppose now that a ≥b and
for all 0 ≤a0 < a we have the existence of a q0 and r0 for a0 and b. To get q and r for a
and b, consider the number a0 := a −b. Since a ≥b > 0, we have 0 ≤a0 < a. Therefore
there are q0 and r0 such that a0 = bq0 + r0 and 0 ≤r0 < b. Writing this as
a −b = bq0 + r0,
0 ≤r0 < b,
add b to both sides: a = b(q0 + 1) + r0. Use q = q0 + 1 and r = r0. This completes the
second proof of existence for b > 0 and a ≥0.
If a < 0 and b > 0, then consider −a and b. Both are positive, so by the previous case
we can write
−a = bQ + R,
0 ≤R < b.
Negating, we have a = b(−Q) −R with −b < −R ≤0. If R = 0 then a = b(−Q) so we can
use q = −Q and r = 0. If R > 0, so −b < −R < 0, we want to add b to −R to make it
positive (and still small), so write a = b(−Q −1) + (b −R) with 0 < b −R ≤b. We can use
q = −Q −1 and r = b −R
Finally, if b < 0 and a is arbitrary, then consider a and −b. From what we already
showed, we can write a = −bQ + R where 0 ≤R < b. Writing this as a = b(−Q) + R, we
can use q = −Q and r = R.
□
Reread this proof until you understand the basic strategy and really see what’s going on.
You might try running through the proof with several choices for a and b, say a = 17 and
b = 5, or a = −17 and b = 3.
3. Proof of Theorem 1.2
As with the proof of Theorem 1.1, we ﬁrst show uniqueness and then existence.
Proof. Uniqueness: Assume, for polynomials f(T) and g(T), that there are q1(T), r1(T)
and q2(T), r2(T) in R[T] which both satisfy the conclusion. That is,
(3.1)
f(T) = g(T)q1(T) + r1(T),
r1(T) = 0 or deg r1(T) < deg g(T)
and
(3.2)
f(T) = g(T)q2(T) + r2(T),
r2(T) = 0 or deg r2(T) < deg g(T).
Comparing the equations in (3.1) and (3.2), we have g(T)q1(T)+r1(T) = g(T)q2(T)+r2(T).
Subtracting,
(3.3)
g(T)(q1(T) −q2(T)) = r2(T) −r1(T).

<!-- page 3 -->
THE DIVISION THEOREM IN Z AND R[T]
3
This implies the diﬀerence r2(T) −r1(T) is a polynomial multiple of g(T).1
From the degree bounds2 in (3.1) and (3.2), if r1(T) ̸= r2(T) then
deg(r1(T) −r2(T)) ≤max(deg r1(T), deg r2(T)) < deg g(T).
But (3.3) tells us r1(T) −r2(T) is a multiple of g(T), so its degree (if r1(T) −r2(T) ̸= 0) is
at least deg g(T). This is a contradiction, so we must have r1(T) = r2(T). Then by (3.3),
g(T)(q1(T) −q2(T)) = 0, so (since g(T) ̸= 0) q1(T) −q2(T) = 0 and hence q1(T) = q2(T).
Existence: Looking back at the ﬁrst proof of the existence part of Theorem 1.1, we see
that argument does not extend so easily to polynomials, since inequalities with integers
don’t carry over as nicely to polynomials. (Also, what would “equally spaced” polynomials
mean?) However, there are inequalities on degrees of polynomials, since degrees are integers.
We will work with inequalities on the degrees of polynomials and mimic the idea in the
second proof of the existence part of Theorem 1.1.
The case when g(T) is constant (that is, deg g(T) = 0) is easy: if g(T) = c is a nonzero
constant then for any f(T) we can use q(T) = (1/c)f(T) and r(T) = 0.
Now ﬁx a nonconstant g(T). We will argue by (strong) induction on deg f(T). That is,
for all f(T) of a given degree we will explain in a uniform way how to ﬁnd polynomials q(T)
and r(T) such that f(T) = g(T)q(T) + r(T) with r(T) = 0 or 0 ≤deg r(T) < deg g(T).
First suppose deg f(T) < deg g(T). In this case use q(T) = 0 and r(T) = f(T).3
Now assume that for some integer n ≥deg g(T) we have constructed a polynomial q(T)
and r(T) for each f(T) of degree less than n. We want to construct q(T) and r(T) for all
polynomials f(T) of degree n. For a polynomial f(T) of degree n, write its leading term
as anT n. Let g(T) have leading term cdT d, so n ≥d. Then f(T) has the same leading
term as (an/cd)T n−dg(T) (check!), which means the diﬀerence f(T)−(an/cd)T n−dg(T) is a
polynomial with degree less than n,4 so by the inductive hypothesis there are polynomials
q0(T) and r0(T) such that
f(T) −(an/cd)T n−dg(T) = g(T)q0(T) + r0(T),
r0(T) = 0 or deg r0(T) < deg g(T).
Bring the g(T)-term on the left over to the other side by addition:
f(T) = g(T)(q0(T) + (an/cd)T n−d) + r0(T),
r0(T) = 0 or deg r0(T) < deg g(T).
Therefore f(T) = g(T)q(T)+r(T) where q(T) = q0(T)+(an/cd)T n−d and r(T) = r0(T).
□
In the last part of the proof (the ‘reduction’ part), we multiplied g(T) by a monomial
to make the top term match the top term of f(T) (in both degree and coeﬃcient), so the
diﬀerence has lower degree. This process can be repeated to drop the degree further, until
we get a polynomial having degree less than deg g(T) or being the polynomial 0. Putting
everything back together, we get q(T) and r(T). This is exactly the algorithm taught in
school to divide one polynomial by another, but perhaps said in a slightly diﬀerent way.
Example 3.1. Let f(T) = 7T 4 −1 and g(T) = T 2 + 5T. Since f(T) has the same leading
term as 7T 2g, we compute
f(T) −7T 2g(T) = −35T 3 −1.
1The argument so far is just like the proof of uniqueness in Z.
2Here we need a slightly diﬀerent argument than in Z, since polynomials don’t have absolute values. We
use the degree as a measure of size instead.
3This corresponds to the case 0 ≤a < b in the proof for Z when b > 0.
4This is the analogue, in the proof for Z, of considering a0 = a −b in place of a when a ≥b > 0.

<!-- page 4 -->
4
KEITH CONRAD
Since −35T 3 −1 has the same leading term as −35Tg(T), we compute
(−35T 3 −1) −(−35Tg(T)) = 175T 2 −1.
Since 175T 2 −1 has the same leading term as 175g(T), we compute
(175T 2 −1) −175g(T) = −875T −1,
whose degree is less than deg g, so we stop. Feeding each equation into the previous ones
gives
f(T)
=
7T 2g(T) −35T 3 −1
=
7T 2g(T) −35Tg(T) + (175T 2 −1)
=
7T 2g(T) −35Tg(T) + 175g(T) −875T −1
=
g(T)(7T 2 −35T + 175) −875T −1.
Thus q(T) = 7T 2 −35T + 175 and r(T) = −875T −1.
Example 3.2. Let f(T) = 2T 4 + T 2 + 6 and g(T) = 3T 2 + 1. Since f(T) has the same
leading term as 2
3T 2g(T), we compute
f(T) −2
3T 2g(T) = 1
3T 2 + 6.
The right side has the same leading term as 1
9g(T), so we compute
1
3T 2 + 6

−1
9g(T) = 53
9 ,
whose degree is less than deg g, so we stop. Feeding the equations into each other gives
f(T)
=
2
3T 2g(T) + 1
3T 2 + 6
=
2
3T 2g(T) + 1
9g(T) + 53
9
=
g(T)
2
3T 2 + 1
9

+ 53
9 ,
so q(T) = 2
3T 2 + 1
9 and r(T) = 53
9 .
4. Division theorem in Z[T]
Is Theorem 1.2 correct if we work in Z[T]? In other words, if f(T) and g(T) are in
Z[T], does the proof of Theorem 1.2 go through and give us unique q(T) and r(T) in Z[T]
such that f(T) = g(T)q(T) + r(T) where r(T) = 0 or 0 ≤deg r(T) < deg g(T)? The
uniqueness part goes through without a problem, but the existence part need not work!
Look at Example 3.2. The initial data f(T) and g(T) are in Z[T] while the q and r that
come out are not in Z[T]. Why is that? Where does the proof break down?
The proof has a problem in exactly one place: at the end of the existence part of the
proof, we want to multiply g(T) by a suitable monomial to get the top term to match
that of f(T), and for this we divide by cd, the leading coeﬃcient of g(T). This usually
requires rational numbers, unless cd = ±1. It is the division by the leading coeﬃcient of
g(T) which tells us the division theorem for Z[T] is not generally valid. More precisely, the
denominators that get introduced in q(T) and r(T) will come from the leading coeﬃcient of

<!-- page 5 -->
THE DIVISION THEOREM IN Z AND R[T]
5
g(T). For instance, in the second example after the proof of Theorem 1.2, g(T) has leading
coeﬃcient 3 and q(T) and r(T) have coeﬃcients with denominators 3 and 9.
There is a special (and important!) case where division in Z[T] is valid: if the leading
coeﬃcient of g(T) is 1. Division by 1 does not introduce denominators. Therefore, when
g(T) has leading coeﬃcient 1, the diﬃculty in the proof of Theorem 1.2 for Z[T] does not
arise. So there is a restricted division theorem in Z[T], as follows.
Theorem 4.1. For any f(T) and g(T) in Z[T], with g(T) having leading coeﬃcient 1, there
are unique q(T) and r(T) in Z[T] such that
f(T) = g(T)q(T) + r(T),
r(T) = 0 or deg r(T) < deg g(T).
It is left to the reader, as an exercise, to check that the proof of Theorem 1.2 carries over
to the setting of Theorem 4.1.
We already saw an example of Theorem 4.1 in Example 3.1. There g(T) has leading
coeﬃcient 1 and the resulting q(T) and r(T) are in Z[T].

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*