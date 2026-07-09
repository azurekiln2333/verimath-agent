# Symmetric Polynomials

> **Source**: https://kconrad.math.uconn.edu/blurbs/symmfunction.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SYMMETRIC POLYNOMIALS
KEITH CONRAD
1. Introduction
Let F be a ﬁeld. A polynomial f(X1, . . . , Xn) ∈F[X1, . . . , Xn] is called symmetric if it
is unchanged by all permutations of its variables:
f(X1, . . . , Xn) = f(Xσ(1), . . . , Xσ(n))
for every permutation σ of {1, . . . , n}.
Example 1.1. The sum X1 + · · · + Xn and product X1 · · · Xn are both symmetric, as are
the power sums Xr
1 + · · · + Xr
n for all r ≥1.
Example 1.2. Let f(X1, X2, X3) = X5
1 + X2X3.
This polynomial is unchanged if we
interchange X2 and X3, but if we interchange X1 and X3 then f becomes X5
3 + X2X1,
which is not f. This polynomial is only “partially symmetric.”
An important collection of symmetric polynomials occurs as the coeﬃcients in the poly-
nomial
(1.1)
(T −X1)(T −X2) · · · (T −Xn) = T n −s1T n−1 + s2T n−2 −· · · + (−1)nsn.
Here s1 is the sum of the Xi’s, sn is their product, and more generally
sk =
X
1≤i1<···<ik≤n
Xi1 · · · Xik
is the sum of the products of the Xi’s taken k terms at a time.
The polynomial sk is
symmetric in X1, . . . , Xn and is called the kth elementary symmetric polynomial – or kth
elementary symmetric function – in X1, . . . , Xn.
Example 1.3. Let α = 3+
√
5
2
and β = 3−
√
5
2
. Although α and β are not rational, their
elementary symmetric polynomials are: s1 = α + β = 3 and s2 = αβ = 1.
Example 1.4. Let α, β, and γ be the three roots of T 3 −T −1, so
T 3 −T −1 = (T −α)(T −β)(T −γ).
Multiplying out the right side and equating coeﬃcients on both sides, the elementary sym-
metric functions of α, β, and γ are s1 = α + β + γ = 0, s2 = αβ + αγ + βγ = −1, and
s3 = αβγ = 1.
Our goal is to prove the following theorem.
Theorem 1.5. The set of symmetric polynomials in F[X1, . . . , Xn] is F[s1, . . . , sn]. That
is, every symmetric polynomial in n variables is a polynomial in the elementary symmetric
functions of those n variables.
1

<!-- page 2 -->
2
KEITH CONRAD
Example 1.6. In two variables, the polynomial X3 + Y 3 is symmetric in X and Y . As a
polynomial in s1 = X + Y and s2 = XY ,
X3 + Y 3 = (X + Y )3 −3XY (X + Y ) = s3
1 −3s1s2.
There are several ways to prove Theorem 1.5. For example, it is proved in [5, Chap. IV,
Sect. 6] by a double induction on n and on the degree of the polynomial. The theorem
can also be proved using Galois theory, transcendental ﬁeld extensions, and integral ring
extensions.1 The proof we will give, based on [2, Sect. 7.1], provides an explicit algorithm
that turns a symmetric polynomial in X1, . . . , Xn into a polynomial in s1, . . . , sn.
2. Lexicographic ordering on F[X1, . . . , Xn]
In F[X], many theorems are proved using induction on the degree of polynomials. The
degree is a nonnegative integer associated to each nonzero polynomial f(X): it is the largest
n ≥0 such that f(X) contains a monomial anXn where an ̸= 0 in F. The monomials
1, X, X2, X3, . . . (all with coeﬃcient 1) are ordered by degree as 1 < X < X2 < . . ., and
deg(f) is the largest monomial appearing in f with a nonzero coeﬃcient.
On F[X1, . . . , Xn] we will use a total ordering on the monomials Xi1
1 · · · Xin
n and associate
to that ordering an analogue on F[X1, . . . , Xn] of the degree on F[X].
Deﬁnition 2.1. For i = (i1, . . . , in) and j = (j1, . . . , jn) in Nn, set i < j if, for the ﬁrst
index r such that ir ̸= jr, we have ir < jr. Write i ≤j if i < j or i = j.
Example 2.2. In N4, (3, 0, 2, 4) < (5, 1, 1, 3) and (3, 0, 2, 4) < (3, 0, 3, 1).
Example 2.3. In Nn, 0 < i for all i ̸= 0.
This way of ordering n-tuples in Nn is called the lexicographic (i.e., dictionary) ordering
since it resembles the way words are ordered in the dictionary alphabetically if we think of
one word as “less” than another if it comes earlier in the dictionary. The “greater” word
comes later. Alphabetical order ﬁrst compares words by the ﬁrst letter, if the ﬁrst letters
are the same then the words are compared by the second letter, and so on. While words
in a dictionary have varying length, we are using lexicographic ordering only to compare
sequences in N with the same number of terms.
In Figure 1 some points in N2 are plotted. The lexicographic ordering compares points
by checking the x-coordinates and then the y-coordinates. For example, the points less than
(3, 2) are (3, 1), (3, 0), and each point (x, y) where x is 0, 1, or 2.
Theorem 2.4. Lexicographic ordering on Nn has the following properties.
(1) (Total ordering) For all i and j, exactly one of i = j or i < j or j < i holds.
(2) (Transitivity) If i < j and j < k then i < k. The same is true with ≤in place of <.
(3) (Compatibility with addition) If i ≤i′ and j ≤j′ then i + j ≤i′ + j′, and if either
inequality in the hypothesis is strict then the inequality in the conclusion is strict.
Proof. (1) If i ̸= j, then there is an r where ir ̸= jr in N. Let r be the least index where
this happens. If ir < jr then i < j, and if jr < ir then j < i.
(2) Let r be the least index where ir, jr, and kr are not all equal. We must have ir ̸= jr or
jr ̸= kr (if both were equalities then ir = jr = kr, which isn’t true). Since earlier coordinates
1Historically, Theorem 1.5 used to be part of the mathematical development leading to Galois theory,
which would make a proof of Theorem 1.5 by Galois theory circular, but Galois theory in its modern form
does not require Theorem 1.5.

<!-- page 3 -->
SYMMETRIC POLYNOMIALS
3
Figure 1. The point (3, 2) and smaller points in N2.
in i, j, and k are all equal, either ir < jr or jr < kr because i < j and j < k. Therefore
ir ≤jr ≤kr with at least one inequality being strict, so ir < kr and earlier coordinates in i
and k are equal. Thus i < k.
This result for ≤is the same argument as with < except we have the extra cases where
i and j may coincide or j and k may coincide, which makes things easier.
(3) Rather than take cases based on where i and i′ may ﬁrst diﬀer or where j and j′ may
ﬁrst diﬀer, observe that i ≤i′ ⇒i + k ≤i′ + k for all k: this is obvious when i = i′, and
when i < i′ the only way ir + kr diﬀers from i′
r + kr is if ir ̸= i′
r, and the ﬁrst time this
happens we have ir < i′
r, so ir + kr < i′
r + kr.
Now we use that twice together with the transitivity in (2). If i ≤i′ and j ≤j′, then
i + j ≤i′ + j = j + i′ ≤j′ + i′ = i′ + j′ =⇒i + j ≤i′ + j′.
The case of < in place of ≤is analogous.
□
A polynomial f ∈F[X1, . . . , Xd] is a sum of the form
f =
X
i1,...,in≥0
ci1,...,inXi1
1 · · · Xin
n
where ci1,...,in ∈F and only ﬁnitely many coeﬃcients can be nonzero.
Abbreviate this
sum to multi-index form as P
i ciXi, where Xi := Xi1
1 · · · Xin
n
for i = (i1, . . . , in). Note
XiXj = Xi+j. (In the notation P
i, only ﬁnitely many terms are nonzero.) When f ̸= 0,
lexicographic ordering lets us compare the diﬀerent nonzero monomials appearing in f,
which leads to the following concepts that generalize degree and leading terms on F[X].
Deﬁnition 2.5. Write f in F[X1, . . . , Xn] as P
i ciXi. If f ̸= 0, the multidegree of f is the
lexicographically largest index in Nn of a nonzero monomial in f:
mdeg f = max{i : ci ̸= 0} ∈Nn.
The multidegree of the zero polynomial is not deﬁned. If f ̸= 0 and mdeg f = d, we call
cdXd the leading term of f and cd the leading coeﬃcient of f, written cd = lead f.

<!-- page 4 -->
4
KEITH CONRAD
We can separate the leading term of a nonzero f of multidegree d from its other nonzero
terms to get
f = cdXd +
X
i<d
ciXi.
Because multidegrees are totally ordered, a nonzero polynomial in F[X1, . . . , Xn] has a
unique leading term and a unique leading coeﬃcient in F.
Example 2.6. In Q[X1, X2], let f = 7X1X5
2 + 3X8
2 + 9. Since max((1, 5), (0, 8), (0, 0)) =
(1, 5) in N2, mdeg(f) = (1, 5) and lead(7X1X5
2 + 3X8
2 + 9) = 7.
Example 2.7. In F[X1, . . . , Xn], mdeg(X1) = (1, 0, . . . , 0) and mdeg(Xn) = (0, 0, . . . , 1).
Example 2.8. The polynomials with multidegree 0 are the nonzero constants.
Example 2.9. The multidegrees of the elementary symmetric polynomials are
mdeg(s1) = (1, 0, 0, . . . , 0),
mdeg(s2) = (1, 1, 0, . . . , 0),
...
mdeg(sn) = (1, 1, 1, . . . , 1).
For k = 1, . . . , n, the leading term of sk is X1 · · · Xk, so the leading coeﬃcient of sk is 1.
Our deﬁnition of multidegree is speciﬁc to calling X1 the “ﬁrst” variable and Xn the
“last” variable. Despite its ad hoc nature (there is nothing intrinsic about making X1 the
“ﬁrst” variable), the multidegree is useful since it permits us to prove theorems about all
multivariable polynomials by ordering them according to their multidegree.
The following theorem shows that a number of standard properties of the degree of
polynomials in one variable carry over to multidegrees of multivariable polynomials.
Theorem 2.10. For nonzero f and g in F[X1, . . . , Xn], mdeg(fg) = mdeg(f) + mdeg(g)
in Nn and lead(fg) = (lead f)(lead g).
For f and g in F[X1, . . . , Xn], mdeg(f + g) ≤max(mdeg f, mdeg g) and if mdeg f <
mdeg g then mdeg(f + g) = mdeg g.
Proof. We will prove the ﬁrst result and leave the second to the reader.
Let mdeg f = n and mdeg g = m, say f = cnXn + P
i<n ciXi with cn ̸= 0 and g =
c′
mXb + P
j<m c′
jXj with c′
m ̸= 0. This amounts to pulling out the top multidegree terms
of f and g. Then fg has a nonzero term cnc′
mXn+m and every other term has multidegree
n + j, m + i, or i + j where i < n and j < m. By Theorem 2.4, all these other multidegrees
are less than n + m, so mdeg(fg) = n + m = mdeg f + mdeg g and lead(fg) = cnc′
m =
(lead f)(lead g).
□
Example 2.11. If f and g in F[X1, . . . , Xn] are diﬀerent polynomials with the same leading
term then let’s show mdeg(f −g) < mdeg f. Writing the common leading term as cnXn,
f = cnXn +
X
i<n
aiXi,
g = cnXn +
X
i<n
biXi
where the sums over i < n have ﬁnitely many nonzero terms. Subtracting,
f −g =
X
i<n
(ai −bi)Xi

<!-- page 5 -->
SYMMETRIC POLYNOMIALS
5
where the right side has ﬁnitely many nonzero terms. Each i on the right side is less than
n, so mdeg(f −g) < n.
In N with its usual ordering, there are only ﬁnitely many elements below a given element,
but this is not true in Nn for n ≥2 with lexicographic ordering: there can be inﬁnitely
many n-tuples below an n-tuple. For instance, (0, b) < (1, 0) for all b ∈N. In terms of
lexicographic ordering on monomials in F[X, Y ], where X > Y , this corresponds to saying
(2.1)
1 < Y < Y 2 < Y 3 < · · · < Y b < · · · < X.
However, if we have a lexicographically strictly decreasing sequence of monomials XiY j
that starts with X, the next term is a deﬁnite monomial Y j and below that there are only
ﬁnitely many possible monomials Y b (where b < j). This is an example of the following
important ﬁniteness property of the lexicographic ordering on every Nn.
Theorem 2.12. When Nn has lexicographic ordering, each nonempty subset of Nn has a
least element. In particular, every strictly decreasing sequence d1 > d2 > d3 > · · · of Nn
using the lexicographic ordering has ﬁnitely many terms.
Note (2.1) is not an example of a strictly decreasing sequence since no speciﬁc monomial
is the next term less than X: when d1 = X, there is no d2 in (2.1).
Before proving the theorem, we consider another example in N2 (see Figure 1). Let’s see
why a lexicographically strictly decreasing sequence in N2 that starts at (3, 2) has ﬁnitely
many terms. If there is a smaller term in the sequence of the form (3, b), then b < 2 and
there are ﬁnitely many of those. After these possibilities are exhausted, if the sequence is
not ﬁnished then the next smaller term in the sequence is a point of the form (2, b), (1, b),
or (0, b). Whichever form it has, there can be only ﬁnitely many smaller points vertically
below it, and once those choices are exhausted in the sequence, the next smaller point (if
there is one) is a deﬁnite point on a vertical line further to the left. Proceeding in this way,
we obtain only ﬁnitely many terms in the sequence until the options are exhausted, So a
lexicographically strictly decreasing sequence in N2 that starts at (3, 2) has ﬁnitely many
terms even though there are inﬁnitely many points in N2 that are less than (3, 2)!
Proof. First we will show each nonempty subset S of Nn has a lexicographically least
element. The ﬁrst coordinates of elements in S are a nonempty subset of N and thus have
a least element ℓ1. If n = 1 then ℓ1 is the least element of S. For n ≥2, among the
elements of S with ﬁrst coordinate ℓ1, their second coordinates are a nonempty subset of
N and thus have a least element ℓ2. If n = 2 then (ℓ1, ℓ2) is the least element of S. For
n ≥3, among the elements of S with ﬁrst coordinate ℓ1 and second coordinate ℓ2, their
third coordinates are a nonempty subset of N and thus have a least element ℓ3. Continue
this way up through the nth coordinate. The n-tuple (ℓ1, ℓ2, . . . , ℓn) in S is the least element
of S in the lexicographic ordering on Nn. It is left to the reader to rewrite this argument
as a proper proof by induction on n.
Next, to see that every lexicographically strictly decreasing sequence d1 > d2 > d3 > · · ·
in Nn is ﬁnite, assume such a sequence is inﬁnite.
Then this is a nonempty subset of
Nn without a lexicographically least element, which is impossible. So a lexicographically
strictly decreasing sequence in Nn has only ﬁnitely many terms.
□
The least element in a nonempty subset of Nn is unique since lexicographic ordering on
Nn is a total ordering.

<!-- page 6 -->
6
KEITH CONRAD
3. Proof of Theorem 1.5
Here is a proof of Theorem 1.5 that uses lexicographic ordering on F[X1, . . . , Xn] and
Theorem 2.12 to show a recursive process must terminate in ﬁnitely many steps.
Proof. We want to show every symmetric polynomial in F[X1, . . . , Xn] is a polynomial in
F[s1, . . . , sn]. This is obvious for constant polynomials, which are 0 and polynomials of
multidegree (0, 0, . . . , 0).
Let f be a nonconstant symmetric polynomial in F[X1, . . . , Xn] with multidegree d =
(d1, . . . , dn). Pull out the leading term of f:
(3.1)
f = cdXd +
X
i<d
ciXi = cdXd1
1 · · · Xdn
n +
X
i<d
ciXi,
where cd ̸= 0. We will ﬁnd a polynomial in s1, . . . , sn with the same leading term as f. Its
diﬀerence with f will be symmetric with smaller multidegree than d.
By Example 2.9 and Theorem 2.10, for nonnegative integers a1, . . . , an,
mdeg(sa1
1 sa2
2 · · · san
n ) = a1 mdeg(s1) + a2 mdeg(s2) + · · · + an mdeg(sn)
= (a1 + a2 + · · · + an, a2 + · · · + an, . . . , an).
The ith coordinate here is ai + ai+1 + · · · + an. To make this equal d = (d1, . . . , dn), we
must set
(3.2)
a1 = d1 −d2,
a2 = d2 −d3,
. . . ,
an−1 = dn−1 −dn,
an = dn.
Does this make sense? That is, are d1 −d2, d2 −d3, . . . , dn−1 −dn, dn all nonnegative? If
not then we have a problem. We need to show the coordinates of d = mdeg(f) satisfy
(3.3)
d1 ≥d2 ≥· · · ≥dn ≥0.
Why does an n-tuple that is the multidegree of a symmetric polynomial satisfy (3.3)?
To appreciate this issue, consider f = X1X5
2 + 3X2. The multidegree of f is (1, 5), so
the exponents don’t satisfy (3.3). This f is not symmetric, and that is the key point. If we
took f = X1X5
2 + X5
1X2 then f is symmetric and mdeg f = (5, 1) does satisfy (3.3). The
veriﬁcation of (3.3) will depend crucially on f being symmetric.
Since (d1, . . . , dn) is the multidegree of a nonzero monomial in f (the multidegree of the
leading term of f), and f is symmetric, every n-tuple with the di’s permuted is also a
multidegree of a nonzero monomial in f. (This is how the symmetry of f in the Xi’s is
used: under all permutations of the Xi’s, f stays unchanged.) For example, if f in F[x, y]
is symmetric and contains the monomial cx3y2 then f also contains the monomial cx2y3
since permuting x and y turns the ﬁrst monomial into the second while not changing f.
The multidegree of f is the largest multidegree of all monomials in f, so (d1, . . . , dn)
must be larger in Nn than all of its nontrivial permutations2, which means
d1 ≥d2 ≥· · · ≥dn ≥0.
That shows the deﬁnition of a1, . . . , an in (3.2) has nonnegative values, so sa1
1 · · · san
n
is a
polynomial. Its multidegree is the same as that of f by (3.2). Moreover, by Theorem 2.10,
lead(cdsa1
1 · · · san
n ) = (lead cd)(lead s1)a1 · · · (lead sn)an = cd.
2A trivial permutation is one that exchanges equal coordinates, like (2, 2, 1) and (2, 2, 1).

<!-- page 7 -->
SYMMETRIC POLYNOMIALS
7
So f and cdsa1
1 · · · san
n have the same leading term cdXd1
1 · · · Xdn
n . Set f1 := f −cdsa1
1 · · · san
n ,
so f1 is symmetric since it is a diﬀerence of symmetric polynomials and
f = cdsa1
1 · · · san
n + f1.
• If f1 = 0 then f = cdsa1
1 · · · san
n and we’re done.
• If f1 ̸= 0 then
mdeg(f1) = mdeg(f −cdsa1
1 · · · san
n ) < mdeg(f)
by Example 2.11 (the leading terms of f and cdsa1
1 · · · san
n match).
Run through the same process with f1 in place of f: let f1 have leading term cd1Xd1.
Since f1 is symmetric, some product sb1
1 · · · sbn
n has leading term Xd1, so f1 has the same
leading term as cd1sb1
1 · · · sbn
n . Set f2 := f1 −cd1sb1
1 · · · sbn
n , which is symmetric since it is a
diﬀerence of symmetric polynomials and
f = cdsa1
1 · · · san
n + f1 = cdsa1
1 · · · san
n + cd1sb1
1 · · · sbn
n + f2
where d1 < d.
• If f2 = 0 then
f = cdsa1
1 · · · san
n + cd1sb1
1 · · · sbn
n
and we’re done.
• If f2 ̸= 0 then mdeg(f2) < mdeg(f1) by Example 2.11.
In this way, we obtain a sequence of formulas
f = gk(s1, . . . , sn) + rk
where gk(s1, . . . , sn) is a polynomial in s1, . . . , sn and rk is a polynomial with mdeg(rk+1) <
mdeg(rk) if rk and rk+1 are not 0.
If rk is never 0 then we get an inﬁnite decreasing sequence
mdeg(r1) > mdeg(r2) > mdeg(r3) · · ·
in Nn. This is impossible by Theorem 2.12, so some rk is 0. Thus f = gk(s1, . . . , sn), which
shows f is a polynomial in s1, . . . , sn.
□
Let’s summarize the recursive step: if f is symmetric in X1, . . . , Xn that is not 0 and its
leading term is cdXd1
1 · · · Xdn−1
n−1 Xdn
n
then either f = cdsd1−d2
1
· · · sdn−1−dn
n−1
sdn
n or
mdeg(f −cdsd1−d2
1
· · · sdn−1−dn
n−1
sdn
n ) < mdeg(f).
By repeatedly subtracting oﬀappropriate scalar multiples of products of powers of s1, . . . , sn
we get a sequence of symmetric polynomials with decreasing multidegree if they are never
0, so they must at some point be 0 because there is no inﬁnite decreasing sequence in Nn.
Example 3.1. In three variables, let f(X, Y, Z) = X4+Y 4+Z4. To write f as a polynomial
in the elementary symmetric polynomials in X, Y , and Z, which are
s1 = X + Y + Z,
s2 = XY + XZ + Y Z,
s3 = XY Z,
use lexicographic ordering with X > Y > Z (that is, X = X1, Y = X2, and Z = X3). The
multidegree of sa
1sb
2sc
3 is (a + b + c, b + c, c).

<!-- page 8 -->
8
KEITH CONRAD
Step 1. The leading term of f is X4, with multidegree (4, 0, 0). This is the multidegree
of s4
1 = (X + Y + Z)4, which has leading term X4, so set f1 = f −s4
1. By a calculation,
f1 = −4X3Y −4XY 3 −4X3Z −4XZ3 −4Y 3Z −4Y Z3 −6X2Y 2 −6X2Z2 −6Y 2Z2
−12X2Y Z −12XY 2Z −12XY Z2.
Step 2. The symmetric polynomial f1 has leading term −4X3Y , with multidegree (3, 1, 0).
This is (a + b + c, b + c, c) when c = 0, b = 1, a = 2, so f1 has the same leading term as
−4sa
1sb
2sc
3 = −4s2
1s2. Set f2 = f1 + 4s2
1s2:
f2 = 2X2Y 2 + 2X2Z2 + 2Y 2Z2 + 8X2Y Z + 8XY 2Z + 8XY Z2.
Step 3.
The symmetric polynomial f2 has leading term is 2X2Y 2 with multidegree
(2, 2, 0).
This is (a + b + c, b + c, c) when c = 0, b = 2, a = 0, so f2 has the same
leading term as 2s2
2. Set f3 = f2 −2s2
2:
f3 = 4X2Y Z + 4XY 2Z + 4XY Z2.
Step 4. The symmetric polynomial f3 has leading term is 4X2Y Z, which has multidegree
(2, 1, 1). This is (a + b + c, b + c, c) for c = 1, b = 0, and a = 1, so f3 has the same leading
term as 4s1s3. Set f4 = f3 −4s1s3 and this vanishes:
f4 = 0.
Here is the decreasing sequence of multidegrees we obtained in successive steps before
the process terminated:
(3.4)
(4, 0, 0) > (3, 1, 0) > (2, 2, 0) > (2, 1, 1).
Putting everything back together, we get X4 + Y 4 + Z4 as a polynomial in s1, s2, s3:
X4 + Y 4 + Z4 = f
= (f −f1) + (f1 −f2) + (f2 −f3) + f3
= s4
1 −4s2
1s2 + 2s2
2 + 4s1s3.
(3.5)
Remark 3.2. The ﬁniteness that made the procedure in the proof of Theorem 1.5 terminate
is the ﬁniteness of strictly decreasing sequences in Nn (Theorem 2.12). We did not write the
proof of Theorem 1.5 using induction on the multidegree of symmetric polynomials, since
Nn in the lexicographic ordering does not have ﬁnitely many multidegrees below a given
multidegree when n ≥2 (see (2.1), where (0, b) < (1, 0) for all b ≥0). We can describe
the proof of Theorem 1.5 using induction if we think carefully about what makes the idea
of induction work. Suppose for every d in Nn we have a proposition P(d) (like “every
symmetric polynomial in F[X1, . . . , Xn] of multidegree d is in F[s1, . . . , sn]”) and
• P(0) is true (Base Case),
• if d ̸= 0 and P(n) is true for all n < d then P(d) is true (Inductive Step).
It follows that P(d) is true for all d in Nn. To prove that, let S = {d ∈Nn : P(d) is false}.
We want S to be empty: if there is no d in Nn such that P(d) is false, then P(d) is true
for all d. To show S = ∅when the two conditions above hold, assume S ̸= ∅. Then S has a
least element by Theorem 2.12, say d. By the ﬁrst condition above, d ̸= 0. When n < d,
we have n ̸∈S since d is the least element of S, so P(n) is true for all n < d. Therefore

<!-- page 9 -->
SYMMETRIC POLYNOMIALS
9
P(d) is true by the second condition above. That contradicts the meaning of d being in S,
so S = ∅.3
Let’s see how to think about the proof of Theorem 1.5 in terms of induction on Nn. We
started the proof by noting the theorem is true for nonzero constant polynomials, which
are those of multidegree 0. Next, when f is symmetric with multidegree d > 0, we found
a symmetric polynomial of the form cdsa1
1 · · · san
n such that that either
• f = cdsa1
1 · · · san
n or
• f ̸= cdsa1
1 · · · san
n and mdeg(f −cdsa1
1 · · · san
n ) < d.
In the ﬁrst case, f ∈F[s1, . . . , sn]. In the second case, f −cdsa1
1 · · · san
n
is nonzero and
symmetric with multidegree less than d, so if we assume all nonzero symmetric polynomials
in F[X1, . . . , Xn] of multidegree less than d are in F[s1, . . . , sn], then f −cdsa1
1 · · · san
n
is
in F[s1, . . . , sn], so f ∈F[s1, . . . , sn]. Do you see how this ﬁts the format of induction
on Nn? For each d ∈Nn let P(d) be the proposition “every symmetric polynomial in
F[X1, . . . , Xn] of multidegree d is in F[s1, . . . , sn]”. Then we showed P(0) is true and we
showed that if d ̸= 0 and P(n) is true for all n < d then P(d) is true. Thus P(d) is true for
all d by induction on Nn, so Theorem 1.5 is proved for all nonzero symmetric polynomials
in F[X1, . . . , Xn], and it is obvious for the polynomial 0, so the theorem is proved for all
symmetric polynomials.
Another way to prove Theorem 1.5 by induction that might feel less abstract is to modify
the method of ordering Nn: we could compare n-tuples ﬁrst by the sum of their coordinates,
and in case of a tie break the tie by lexicographic order. This is called graded lexicographic
order. For example, (2, 3) > (1, 7) > (0, 5) in lexicographic order but (1, 7) > (2, 3) > (0, 5)
in graded lexicographic order. The ordering in (3.4) is valid for graded lexicographic order
since all the triples there have the same sum of coordinates (all equal 4), so the comparison
is made by lexicographic order. On nonzero monomials, graded lexicographic order amounts
to comparing ﬁrst by total degree (sum of exponents) and using lexicographic order only
in case of equal total degree. When Nn is arranged in graded lexicographic order, there
are only ﬁnitely many n-tuples below a given n-tuple since that is already the case when
we order Nn just by the sum of the coordinates. This makes graded lexicographic order
closer to your intuition from the standard total ordering on N. Theorem 1.5 is proved by
induction using graded lexicographic order on monomials in [3, Theorem 2.2.2].
Corollary 3.3. Let L/K be a ﬁeld extension and f(T) ∈K[T] factor as
(T −α1)(T −α2) · · · (T −αn)
in L[T]. For each positive integer r,
(T −αr
1)(T −αr
2) · · · (T −αr
n) ∈K[T].
Proof. For indeterminates X1, . . . , Xn, write
(3.6)
(T −Xr
1)(T −Xr
2) · · · (T −Xr
n) =
n
X
k=0
ck(X1, . . . , Xn)T k.
We can view each ck(X1, . . . , Xn) in K[X1, . . . , Xn] (its coeﬃcients are all 0 and 1) and it is
symmetric in X1, . . . , Xn since the left side of (3.6) is symmetric in X1, . . . , Xn. Therefore
3In the case of N, the argument we just gave corresponds to the proof that the Well-Ordering Principle
on N implies the principle of mathematical induction on N. Theorem 2.12 says Nn with the lexicographic
ordering is a well-ordered set even though it has inﬁnitely many elements below some elements if n ≥2.

<!-- page 10 -->
10
KEITH CONRAD
ck(X1, . . . , Xn) is a polynomial over K in the elementary symmetric functions of X1, . . . , Xn,
say
ck(X1, . . . , Xn) = gk(s1, . . . , sn)
where gk is a polynomial in n indeterminates over K. Then
(T −Xr
1)(T −Xr
2) · · · (T −Xr
n) =
n
X
k=0
gk(s1, . . . , sn)T k.
On both sides of this equation, specialize Xi to αi.
(Each si is implicitly a polyno-
mial X1, . . . , Xn and thus also gets specialized.) The elementary symmetric functions of
α1, . . . , αn are the non-leading coeﬃcients of f(T) (up to a sign), so they lie in K since the
coeﬃcients of f(T) are in K. Therefore a polynomial in the elementary symmetric functions
of the αi’s with coeﬃcients in K lies in K, so each gk(s1, . . . , sn) is specialized to a value
in K.
□
Remark 3.4. The same reasoning shows for each h(X) ∈K[X], not just h(X) = Xr, that
(T −h(α1))(T −h(α2)) · · · (T −h(αn)) ∈K[T].
The coeﬃcient of T n−1 in (3.6) is −(Xr
1 + · · · + Xr
n). We call Xr
1 + · · · + Xr
n the rth
power sum of X1, . . . , Xn. It can be written as a polynomial in the elementary symmetric
functions s1, . . . , sn. The next example presents some of these polynomials for n = 2 and 3.
Example 3.5. For the second, third, and fourth powers sums in two variables,
X2 + Y 2 = (X + Y )2 −2XY = s2
1 −2s2,
X3 + Y 3 = (X + Y )3 −3(X + Y )XY = s3
1 −3s1s2
X4 + Y 4 = (X + Y )4 −4(X2 + Y 2)(XY ) −6X2Y 2 = s4
1 −4s2
1s2 + 2s2
2,
where we use the formula X2 + Y 2 = s2
1 −2s2 in the last calculation.
Example 3.6. For the second, third, and fourth powers sums in three variables,
X2 + Y 2 + Z2 = (X + Y + Z)2 −2(XY + XZ + Y Z) = s2
1 −2s2,
X3 + Y 3 + Z3 = (X + Y + Z)3 −3(XY + XZ + Y Z)(X + Y + Z) + 3XY Z
= s3
1 −3s1s2 + 3s3
X4 + Y 4 + Z4 = s4
1 −4s2
1s2 + 2s2
2 + 4s1s3 by (3.5).
Example 3.7. Let f(T) = T 2 + 5T + 2 = (T −α)(T −β) where α = (−5 +
√
17)/2 and
β = (−5 −
√
17)/2. Although α and β are irrational, their elementary symmetric functions
are integers: s1 = α + β = −5 and s2 = αβ = 2 . Using the formulas in Example 3.5,
α2 + β2 = p2 = s2
1 −2s2 = 21,
α3 + β3 = p3 = s3
1 −3s1s2 = −95,
α4 + β4 = p4 = s4
1 −4s2
1s2 + 2s2
2 = 433.
Numerically, α ≈−.438 and β ≈−4.561, so pr = αr + βr is extremely close to βr since
|αr| →0 rapidly as r grows. In fact, pr turns out to be the nearest integer to βr: compare
β2 ≈20.807, β3 ≈−94.915, and β4 ≈432.963. The way we computed the power sums
above needed no approximations or formulas for α and β. The power sums are determined
by the elementary symmetric functions s1 and s2 using exact calculations with integers.

<!-- page 11 -->
SYMMETRIC POLYNOMIALS
11
Example 3.8. Let α, β, and γ be the three roots of T 3 −T −1, so
T 3 −T −1 = (T −α)(T −β)(T −γ).
The elementary symmetric functions of α, β, and γ are all s1 = 0 , s2 = −1 , and s3 = 1 ,
so by the formulas in Example 3.6,
α2 + β2 + γ2 = p2 = s2
1 −2s2 = 2,
α3 + β3 + γ3 = p3 = s3
1 −3s1s2 + 3s3 = 3,
α4 + β4 + γ4 = p4 = s4
1 −4s2
1s2 + 2s2
2 + 4s1s3 = 2.
The next few power sums are p5 = 5, p6 = 5, p7 = 7, and p8 = 10. We do not need formulas
for α, β, and γ to make these power sum calculations. All of them are determined by the
elementary symmetric function values s1, s2, and s3, which come from the coeﬃcients of
T 3 −T −1.
Comparing the formulas in Examples 3.5 and 3.6 for the same exponent, they match
in degree 2 but look diﬀerent in degrees 3 and 4, However, they are the same formula in
degree 3 by taking s3 = 0 for two variables and they are the same formula in degree 4 by
also taking s4 = 0 for two variables. If we let sk(X1, . . . , Xn) = 0 when k > n then there are
“universal” formulas for power sums pr = Xr
1 + · · · + Xr
n in terms of elementary symmetric
polynomials in any number of variables, starting out as
p1 = s1,
p2 = s2
1 −2s2,
p3 = s3
1 −3s1s2 + 3s3,
p4 = s4
1 −4s2
1s2 + 2s2
2 + 4s1s3 −4s4.
There is some apparent regularity in these formulas: the ﬁrst two terms in the formula for
pr appear to be sr
1−rsr−2
1
s2. A nice regularity for all r can be seen in determinant formulas:
p2 = det

s1
1
2s2
s1

,
p3 = det


s1
1
0
2s2
s1
1
3s3
s2
s1

,
p4 = det




s1
1
0
0
2s2
s1
1
0
3s3
s2
s1
1
4s4
s3
s2
s1



.
4. Uniqueness for Theorem 1.5
The proof of Theorem 1.5 leads to a speciﬁc way of writing a symmetric polynomial f
in X1, . . . , Xn as a polynomial in s1, . . . , sn, but that does not automatically mean there
can only be one such representation of f as a polynomial in s1, . . . , sn: just because an
algorithm has a well-determined ﬁnal result does not mean the problem it is solving only
has one answer. For instance, if we apply Euclid’s algorithm to solve 18x + 5y = 1 in
integers, we get the speciﬁc solution (x, y) = (2, −7), but the equation 18x + 5y = 1 has
inﬁnitely many integral solutions: (x, y) = (2 + 5t, −7 −18t) for all t ∈Z. It turns out that
symmetric polynomials in X1, . . . , Xn do have a unique representation as a polynomial in
s1, . . . , sn.
Theorem 4.1. Every symmetric polynomial in F[X1, . . . , Xn] can be written in only one
way as a polynomial in the elementary symmetric functions of X1, . . . , Xn.

<!-- page 12 -->
12
KEITH CONRAD
Proof. Let s1, . . . , sn be the elementary symmetric functions of X1, . . . , Xn. Each polyno-
mial in F[X1, . . . , Xn] that is symmetric in the Xi’s is in F[s1, . . . , sn] by Theorem 1.5.
To prove uniqueness of this representation, suppose g(Y1, . . . , Yn) and h(Y1, . . . , Yn) in
F[Y1, . . . , Yn] satisfy g(s1, . . . , sn) = h(s1, . . . , sn) in F[X1, . . . , Xn]. We want to show g = h
in F[Y1, . . . , Yn] (that is, each monomial in Y1, . . . , Yn has the same coeﬃcients in g and h).
By passing to the diﬀerence g(Y1, . . . , Yn) −h(Y1, . . . , Yn), we are reduced to showing that
g(s1, . . . , sn) = 0 in F[X1, . . . , Xn] =⇒g(Y1, . . . , Yn) = 0 in F[Y1, . . . , Yn].
We will prove the contrapositive: if g(Y1, . . . , Yn) ̸= 0 in F[Y1, . . . , Yn] then g(s1, . . . , sn) ̸= 0
in F[X1, . . . , Xn].
Write the nonzero g(Y1, . . . , Yn) as a sum of ﬁnitely many monomials in the Yi’s:
g(Y1, . . . , Yn) =
X
i
ciYi
and some ci is nonzero. Therefore
(4.1)
g(s1, . . . , sn) =
X
i
cisi1
1 · · · sin
n .
Diﬀerent terms in this sum, as a polynomial in X1, . . . , Xn, could share some monomials and
thus lead to cancellation when like monomials are added together. To show g(s1, . . . , sn) ̸=
0, we want at least one monomial in the Xi’s not to cancel out in g(s1, . . . , sn).
The subtle issue here is that the leading term of g(Y1, . . . , Yn) need not contain the leading
term of g(s1, . . . , sn) as a polynomial in X1, . . . , Xn.
For example, suppose g(Y1, Y2) =
Y 5
1 + Y 5
2 , which has leading term Y 5
1 . Replacing Yi with si,
g(s1, s2) = s5
1 + s5
2 = (X1 + X2)5 + (X1X2)5,
and the leading term is (X1X2)5, which comes from the non-leading term Y 5
2 in g(Y1, Y2)
after substituting si for Yi.
In the general case, the leading term of g(s1, . . . , sn) as a
polynomial in X1, . . . , Xn comes from somewhere in g(Y1, . . . , Yn) but it’s not clear where.
We can compute the leading term of si1
1 · · · sin
n as a polynomial in X1, . . . , Xn by Example
2.9 and Theorem 2.10 because the multidegree tells us the exponents for the leading term:
mdeg(si1
1 · · · sin
n ) =
n
X
k=1
ik mdeg(sk)
= i1(1, 0, 0, . . . , 0) + i2(1, 1, 0, . . . , 0) + · · · + in(1, 1, 1, . . . , 1)
= (i1 + i2 + · · · + in, i2 + · · · + in, . . . , in−1 + in, in).
(4.2)
For i and j in Nn, comparing the formulas
mdeg(si1
1 · · · sin
n ) = (i1 + i2 + · · · + in, i2 + · · · + in, . . . , in−1 + in, in),
mdeg(sj1
1 · · · sjn
n ) = (j1 + j2 + · · · + jn, j2 + · · · + jn, . . . , jn−1 + jn, jn)
from rightmost to the leftmost coordinates shows that if mdeg(si1
1 · · · sin
n ) = mdeg(sj1
1 · · · sjn
n )
then i = j. Therefore when the n-tuples i and j are diﬀerent, the polynomials si1
1 · · · sin
n
and sj1
1 · · · sjn
n in F[X1, . . . , Xn] have diﬀerent multidegrees and leading coeﬃcients 1 (each
si has leading coeﬃcient 1). Therefore the terms in (4.1) with nonzero coeﬃcient ci have
diﬀerent multidegrees, so one of them (we don’t know which!) is greatest. The last part of
Theorem 2.10 extends to more than two polynomials:
mdeg(f1) > mdeg(f2), . . . , mdeg(fm) =⇒mdeg(f1 + f2 + · · · + fm) = mdeg(f1).

<!-- page 13 -->
SYMMETRIC POLYNOMIALS
13
Apply this when f1, . . . , fm are the nonzero terms in (4.1): mdeg(g(s1, . . . , sn)) is the largest
multidegree of a nonzero term in (4.1). In particular, g(s1, . . . , sn) ̸= 0.
□
Example 4.2. The only expression of X4 + Y 4 + Z4 as a polynomial in s1, s2, and s3 is
the one appearing in (3.5).
In the proofs of Theorems 1.5 and 4.1, the fact that the coeﬃcients come from a ﬁeld F
rather than a ring is not important since we never had to divide in F. The same proofs
show for a nonzero commutative ring R that each symmetric polynomial in R[X1, . . . , Xn]
lies in R[s1, . . . , sn] in exactly one way.4 For instance, Theorems 1.5 and 4.1 together using
integer coeﬃcients take the following form.
Theorem 4.3. The set of all symmetric polynomials in Z[X1, . . . , Xn] is Z[s1, . . . , sn], and
each element of Z[s1, . . . , sn] is a polynomial in s1, . . . , sn in exactly one way.
Example 4.4. Taking α and β as in Example 3.7, their elementary symmetric functions are
both integers: α + β = −5 and αβ = 2. If f(X, Y ) is a symmetric polynomial with integer
coeﬃcients then f(X, Y ) = g(X + Y, XY ) where g is a polynomial with integer coeﬃcients.
Therefore f(α, β) = g(−5, 2) ∈Z. This implies (T −αr)(T −βr), whose coeﬃcients are
αr + βr and αrβr, has integral coeﬃcients and not just rational coeﬃcients. That is why
the calculations with r = 2, 3, and 4 in Example 3.7 have coeﬃcients in Z.
Remark 4.5. Theorem 4.3 is used in the proof that π is transcendental [1, Section 5.2], [6,
Chapter 3].
5. History
Lexicographic ordering on multivariable polynomials and its application to the proof of
Theorem 1.5 go back to Gauss [4, pp. 36–37], who used Theorem 1.5 in his second proof of
the Fundamental Theorem of Algebra. His description of lexicographic ordering is shown in
Figure 2, where the Latin text says “from the two terms Maαbβcγ · · · and Maα′bβ′cγ′ · · · ,
call the ﬁrst one of higher order than the second if α > α′ or if α = α′ and β > β′, or if
α = α′, β = β′, and γ > γ′, etc.”.
Figure 2. Gauss’s deﬁnition of lexicographic ordering.
The lexicographic ordering is just one example of a total ordering on monomials in mul-
tivariable polynomial rings. These orderings are part of computer algebra systems that are
widely used in computational commutative algebra and algebraic geometry.
4There is a slight technicality to be aware of: if R is not a domain then the formula mdeg(fg) =
mdeg f + mdeg g is true only as long as the leading coeﬃcients of f and g are both not zero-divisors in R,
and that is true for the case of elementary symmetric polynomials s1, . . . , sn since their leading coeﬃcients
equal 1.

<!-- page 14 -->
14
KEITH CONRAD
References
[1] D. Angell, “Irrationality and Transcendence in Number Theory,” CRC Press, Boca Raton, 2022.
[2] D. Cox, J. Little, D. O’Shea, “Ideals, Varieties, and Algorithms: An Introduction to Computational
Algebraic Geometry and Commutative Algebra,” Springer-Verlag, New York, 1992.
[3] D. Cox, “Galois Theory,” 2nd ed., Wiley, Hoboken, 2012.
[4] C. F. Gauss, Demonstratio nova altera theorematis omnem functionem algebraicam rationalem in-
tegram unius variabilis in factores reales primi vel secundi gradus resolvi posse,
Comm. Soc.
Reg. Sci. G¨ottingen 3 (1816), 107–142;
pp. 33–56 in Werke, Band III (1866). URL https://
archive.org/details/werkecarlf03gausrich/page/n43/mode/2up. English translation at http://www.
paultaylor.eu/misc/gauss.pdf.
[5] S. Lang, “Algebra,” revised 3rd ed., Springer-Verlag, New York, 2002.
[6] M. R. Murty, P. Rath, Transcendental Numbers, Springer, New York, 2014.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*