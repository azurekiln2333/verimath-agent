# Pfister's Theorem on Sums of Squares

> **Source**: https://kconrad.math.uconn.edu/blurbs/pfister.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
PFISTER’S THEOREM ON SUMS OF SQUARES
KEITH CONRAD
1. Introduction
A classical identity in algebra is the 2-square identity:
(1.1)
(x2
1 + x2
2)(y2
1 + y2
2) = (x1y1 −x2y2)2 + (x1y2 + x2y1)2.
This expresses a sum of two squares times a sum of two squares as another sum of two
squares. It was known to Brahmagupta in the 7th century and rediscovered 1000 years
later by Fermat. For example, since 52 = 12 + 22 and 13 = 22 + 32, we get
65 = 5 · 13 = (12 + 22)(22 + 32) = (1 · 2 −2 · 3)2 + (1 · 3 + 2 · 2)2 = 42 + 72.
A similar 4-square identity was discovered by Euler in 1748:
(x2
1 + x2
2 + x2
3 + x2
4)(y2
1 + y2
2 + y2
3 + y2
4)
=
(x1y1 −x2y2 −x3y3 −x4y4)2 +
(x1y2 + x2y1 + x3y4 −x4y3)2 +
(x1y3 −x2y4 + x3y1 + x4y2)2 +
(x1y4 + x2y3 −x3y2 + x4y1)2.
This was rediscovered by Hamilton (1843) in his work on quaternions. Soon thereafter,
Graves (1843) and Cayley (1845) independently found an 8-square identity: the product
(x2
1 + · · · + x2
8)(y2
1 + · · · + y2
8) equals
(x1y1 −x2y2 −x3y3 −x4y4 −x5y5 −x6y6 −x7y7 −x8y8)2 +
(x1y2 + x2y1 + x3y4 −x4y3 + x5y6 −x6y5 −x7y8 + x8y7)2 +
(x1y3 −x2y4 + x3y1 + x4y2 + x5y7 + x6y8 −x7y5 −x8y6)2 +
(x1y4 + x2y3 −x3y2 + x4y1 + x5y8 −x6y7 + x7y6 −x8y5)2 +
(x1y5 −x2y6 −x3y7 −x4y8 + x5y1 + x6y2 + x7y3 + x8y4)2 +
(x1y6 + x2y5 −x3y8 + x4y7 −x5y2 + x6y1 −x7y4 + x8y3)2 +
(x1y7 + x2y8 + x3y5 −x4y6 −x5y3 + x6y4 + x7y1 −x8y2)2 +
(x1y8 −x2y7 + x3y6 + x4y5 −x5y4 −x6y3 + x7y2 + x8y1)2.
This formula had been discovered about 35 years earlier, by Degen, but that was unknown
to Hamilton, Cayley, and Graves. Mathematicians began searching next for a 16-square
identity but results were inconclusive for a long time.
The general question we ask is: for which n is there any identity
(1.2)
(x2
1 + · · · + x2
n)(y2
1 + · · · + y2
n) = z2
1 + · · · + z2
n
where the z’s are polynomials in the x’s and y’s? The 2-square and 4-square identities (as
well as the 8-square identity of Cayley and Graves) describe the z’s as simple polynomial
functions of the x’s and y’s. More precisely, each zi is a bilinear function of x1, . . . , xn and
y1, . . . , yn in these identities for n = 2, 4, and 8. In 1898, Hurwitz proved a theorem that
1

<!-- page 2 -->
2
KEITH CONRAD
killed this subject: if an identity of the form (1.2) holds in a ﬁeld of characteristic 0, where
each zi is a bilinear function of the x’s and the y’s, then n = 1, 2, 4, or 8. (The trivial
1-square identity is x2
1y2
1 = z2
1 where z1 = x1y1.) This is called Hurwitz’s 1, 2, 4, 8 theorem.
Moreover, it turns out for these four values of n that the identity must be the known one
up to a linear change of variables.
Hurwitz’s 1, 2, 4, 8 theorem should not have ended the search for a 16-square identity.
Hurwitz proved that there is no hope for an identity like (1.2) for n = 16 when the z’s are
bilinear functions of the x’s and y’s. But perhaps there is a 16-square identity without the
z’s being bilinear in the x’s and y’s.
In the 1960s, a 16-square identity was ﬁnally discovered [6]. This identity did not violate
Hurwitz’s theorem (with bilinear z’s) since it involved variables in denominators. Even
more generally, and without knowing about [6], Pﬁster [3, 4] proved that an identity like
(1.2) holds when n is any power of 2, with the z’s being rational functions of the x’s and y’s.
His method was so simple that everyone was taken by surprise. A few years later, Pﬁster
found an even easier approach to his result, and this is what we describe here (based on [5,
pp. 22–24]).
2. Pfister’s Theorem
The heart of Pﬁster’s argument is the following lemma. We write M⊤for the transpose
of a matrix M.
Lemma 2.1. Let F be a ﬁeld. Suppose c = c2
1 + · · · + c2
n, where n is a power of 2 and
ci ∈F. Then there is an n × n matrix C with entries in F and ﬁrst row
(c1, . . . , cn)
such that CC⊤= C⊤C = cIn.
The (1, 1) entry of CC⊤is c2
1 + · · · + c2
n = c. That is how the lemma will get used.
Proof. Writing n = 2k, we induct on k. The case k = 0 is easy. For the case k = 1, we want
to ﬁnd u, v ∈F such that the 2 × 2 matrix
C =

c1
c2
u
v

satisﬁes
CC⊤= C⊤C =

c2
1 + c2
2
0
0
c2
1 + c2
2

.
Well,
CC⊤
=

c1
c2
u
v
 
c1
u
c2
v

=

c2
1 + c2
2
c1u + c2v
c1u + c2v
u2 + v2

.
Setting u = c2 and v = −c1 (or u = −c2 and v = c1) we get CC⊤= cI2. The reader can
check C⊤C also equals cI2.
Now suppose k ≥2 and the result is true for k −1. Setting a = c2
1 + · · · + c2
n/2 and
b = c2
n/2+1 + · · · + c2
n, which are both sums of n/2 squares, c = a + b and by induction there

<!-- page 3 -->
PFISTER’S THEOREM ON SUMS OF SQUARES
3
are 2k−1 × 2k−1 matrices A and B with entries in F and respective ﬁrst rows (c1, . . . , cn/2)
and (cn/2+1, . . . , cn) such that
AA⊤= A⊤A = aIn/2 and BB⊤= B⊤B = bIn/2.
We seek a 2k × 2k matrix C such that CC⊤= C⊤C = cIn = (a + b)In. Generalizing the
case k = 1, let’s try to get C in the form
(2.1)
C =

A
B
U
V

for some 2k−1 × 2k−1 matrices U and V with entries in F. What could U and V be?
When matrices are decomposed into square blocks of the same size, as in (2.1), addition
and multiplication of such matrices can be carried out by working with the blocks as the
“entries,” taking care to remember the order of multiplication of those blocks. Therefore
CC⊤
=

A
B
U
V
 
A⊤
U⊤
B⊤
V ⊤

=

AA⊤+ BB⊤
AU⊤+ BV ⊤
UA⊤+ V B⊤
UU⊤+ V V ⊤

=
 (a + b)In/2
AU⊤+ BV ⊤
UA⊤+ V B⊤
UU⊤+ V V ⊤

.
The oﬀ-diagonal blocks are transposes of each other, so we have CC⊤= cIn provided
(2.2)
AU⊤+ BV ⊤= O and UU⊤+ V V ⊤= cIn/2.
As in the 2 × 2 case, take U = B. Then the ﬁrst equation implies V = −BA⊤(B−1)⊤if
B is invertible. Is B invertible? Since BB⊤= bIn/2 if b ̸= 0 then B is invertible. Could
b = 0? If c ̸= 0 then the equation c = a+b shows at least one of a or b is nonzero, so we can
suppose b ̸= 0 by swapping the roles of a and b (and thus also A and B) at the beginning
if necessary. If c = 0 then it could happen that b = 0 and we’ll address this case later.
When c ̸= 0, so we can choose b ̸= 0 and thus make B invertible, let’s check the above
choices for U and V work:
UU⊤+ V V ⊤
=
BB⊤+ (−BA⊤(B−1)⊤)(−B−1AB⊤)
=
BB⊤+ BA⊤(B⊤)−1B−1AB⊤
=
bIn/2 + BA⊤(BB⊤)−1AB⊤
=
bIn/2 + BA⊤(bIn/2)−1AB⊤
=
bIn/2 + (1/b)BA⊤AB⊤
=
bIn/2 + (1/b)B(aIn/2)B⊤
=
bIn/2 + (a/b)BB⊤
=
bIn/2 + aIn/2
=
cIn/2.
Therefore CC⊤= cIn. Since c ̸= 0, C is invertible, so the equation C⊤C = cIn follows
automatically (a matrix C and its inverse, in this case (1/c)C⊤, always commute).
Showing C exists if c = 0 is almost wholly a technicality.
It is possible in this case
that both a and b vanish. Consider F = C and 0 = (12 + i2) + (12 + i2). However, in

<!-- page 4 -->
4
KEITH CONRAD
this example there is a rearranged half-sum decomposition with nonzero b (and a), namely
0 = (12 + 12) + (i2 + i2). More generally, if
0 = c2
1 + c2
2 + · · · + c2
n
where n is a power of 2 (or n is any positive even integer), then either some half-sum of
terms is nonzero or the numbers c2
1, . . . , c2
n are all equal. Indeed, if every half-sum of terms
is zero then the sum of the ﬁrst n/2 squares is 0 and the sum of the ﬁrst n/2 −1 squares
added to c2
n/2+1 is 0, so after subtraction we get c2
n/2 = c2
n/2+1. By a similar argument all
c2
j are equal.
When c = 0 and one of the half-sums is nonzero, take such a half-sum to be b and
run through the above argument with U and V as deﬁned before. (Now, since C is not
invertible, you really have to check directly that C⊤C = cIn rather than deduce it from
CC⊤= cIn. This is left to the reader.)
When c = 0 and all c2
j are equal, we get 0 = c2
1 + · · · + c2
n = nc2
1. Recall n = 2k is a power
of 2. Therefore when F does not have characteristic 2, c1 = 0 (so each cj is 0) and we can
take for C the zero matrix. When F has characteristic 2, let C be the matrix whose rows all
equal (c1, . . . , cn). Then each entry of CC⊤is P c2
j = 0, so CC⊤= O = cIn. Multiplying
out C⊤C, its (i, j) entry is ncicj, which vanishes since n = 0 in F. Thus C⊤C = O = cIn
too.
□
Theorem 2.2 (Pﬁster). In any ﬁeld, the set of sums of n squares is closed under multipli-
cation when n is a power of 2.
Proof. Let the ﬁeld be F. Suppose x and y in F can be written as sums of n squares:
x = x2
1 + · · · + x2
n and y = y2
1 + · · · + y2
n
with xi, yi ∈F. In Lemma 2.1, choose n × n matrices X and Y with entries in F such that
XX⊤= X⊤X = xIn and Y Y ⊤= Y ⊤Y = yIn,
with the ﬁrst row of X being (x1, . . . , xn) and the ﬁrst row of Y being (y1, . . . , yn). Then
(XY )(XY )⊤= XY Y ⊤X⊤= yXX⊤= xyIn.
Let the ﬁrst row of XY be denoted (z1, . . . , zn). Then (XY )(XY )⊤has (1, 1) entry
z2
1 + · · · + z2
n = xy = (x2
1 + · · · + x2
n)(y2
1 + · · · + y2
n).
□
In the proof of Pﬁster’s theorem, the main point was to compute the (1, 1) entry, but we
needed the full matrix machinery to get it. Using XY ⊤in place of XY , we can take
z1 = x1y1 + · · · + xnyn
but we are not assured that the other zi’s will be bilinear functions of the x’s and y’s. Since
(z1, . . . , zn) can be taken as the ﬁrst row of XY or XY ⊤, we can always make each zi linear
in the x’s since the ﬁrst row of XY (or XY ⊤) only involves X through its ﬁrst row. Usually
zi is not linear in the y’s.
Corollary 2.3. If n is a power of 2 and X1, . . . , Xn, Y1, . . . , Yn are independent variables
over a ﬁeld K, there is an algebraic identity of the form
(X2
1 + · · · + X2
n)(Y 2
1 + · · · + Y 2
n ) = Z2
1 + · · · + Z2
n,
where Zi ∈K(X1, . . . , Xn, Y1, . . . , Yn).

<!-- page 5 -->
PFISTER’S THEOREM ON SUMS OF SQUARES
5
Proof. Apply Pﬁster’s theorem to the ﬁeld F = K(X1, . . . , Xn, Y1, . . . , Yn) with xi = Xi
and yi = Yi.
□
Corollary 2.4. When n is any power of 2, the set of nonzero sums of n squares in any
ﬁeld F is a subgroup of F ×.
Proof. Pﬁster’s theorem tells us this set is closed under multiplication.
Closure under
inversion follows by a simple trick: for nonzero s,
s = a2
1 + · · · + a2
n =⇒1
s = s
s2 =
a1
s
2
+ · · · +
an
s
2
.
□
If we make the proof of Pﬁster’s theorem explicit, then we see denominators are intro-
duced from the term −BA⊤(B−1)⊤in Lemma 2.1. Speciﬁcally, det B will be a denominator.
Let’s go through the proof of the theorem in early cases to see what sum of squares formulas
Pﬁster’s theorem gives us if n = 2 and n = 4.
Suppose n > 1 is a power of 2 and x = Pn
i=1 x2
i and y = Pn
i=1 y2
i . The proof of Pﬁster’s
theorem says xy is a sum of squares of the entries in the ﬁrst row of XY (or XY ⊤) where
X and Y are n × n matrices of the form
(2.3)
X =
A
B
B
−BA⊤(B−1)⊤

and Y =
C
D
D
−DC⊤(D−1)⊤

,
with A being the n/2 × n/2 matrix from Lemma 2.1 that corresponds to Pn/2
i=1 x2
i , B being
the n/2 × n/2 matrix from Lemma 2.1 that corresponds to Pn
i=n/2+1 x2
i , and likewise for
C and C with Pn
i=1 y2
i . (Here, for simplicity, we assume the half-sums in their initial order
are nonzero, which is certainly the case if the xi’s and yi’s are independent indeterminates.)
Take n = 2, with x = x2
1 + y2
1 and y = y2
1 + y2
2. Matrices of size n/2 × n/2 are just
numbers, so they commute and equal their transposes. Then (2.3) becomes
X =

x1
x2
x2
−x1

and Y =

y1
y2
y2
−y1

,
and the sum of squares formula for xy using XY is (x1y1 + x2y2)2 + (x1y2 −x2y1)2. This
is just a slight variation on the classical identity (1.1).
Now let n = 4, x = P4
i=1 x2
i , and y = P4
i=1 y2
i . Using the case n = 2 to build 2 × 2
matrices corresponding to the half-sums x2
1 + x2
2 and x2
3 + x2
4, Lemma 2.1 gives us a 4 × 4
matrix X that has ﬁrst row (x1, x2, x3, x4) and satisﬁes XX⊤= X⊤X = xI4:
X =




x1
x2
x3
x4
x2
−x1
x4
−x3
x3
x4
w1/d
w2/d
x4
−x3
w2/d
−w1/d



,
where w1 = x1(−x2
3 + x2
4) −2x2x3x4, w2 = x2(x2
3 −x2
4) −2x1x3x4, and d = x2
3 + x2
4. An
analogous 4 × 4 matrix Y is built from P4
i=1 y2
i . Then (P4
i=1 x2
i )(P4
i=1 y2
i ) = P4
i=1 z2
i ,
where (z1, z2, z3, z4) is the ﬁrst row of the matrix product XY . Explicitly,
z1 = x1y1 + x2y2 + x3y3 + x4y4,
z2 = x1y2 −x2y1 + x3y4 −x4y3,

<!-- page 6 -->
6
KEITH CONRAD
z3
=
x1y3 + x2y4 + x3
y1(−y2
3 + y2
4) −2y2y3y4
y2
3 + y2
4
+ x4
y2(y2
3 −y2
4) −2y1y3yy4
y2
3 + y2
4
z4
=
x1y4 −x2y3 + x3
y2(y2
3 −y2
4) −2y1y3y4
y2
3 + y2
4
+ x4
y1(y2
3 −y2
4) + 2y2y3y4
y2
3 + y2
4
.
(As a reality check, compute (x2
1 +x2
2 +x2
3 +x2
4)(y2
1 +y2
2 +y2
3 +y2
4)−(z2
1 +z2
2 +z2
3 +z2
4) with
the above deﬁnitions of z1, z2, z3, z4 on a computer algebra system and check the answer is
0; watch out for sign errors.) Unlike Euler’s 4-square identity, Pﬁster’s 4-square identity
has denominators in z3 and z4.
3. A Converse to Pfister’s Theorem
When n is a power of 2, Pﬁster’s theorem shows the nonzero sums of n squares in every
ﬁeld form a group under multiplication. What if n is not a power of 2? Of course in some
ﬁelds the nonzero sums of n squares will be a group under multiplication for any n ≥1,
such as in R, where the nonzero sums of n squares are the same thing as the positive real
numbers. It turns out, though, that for any n ≥1 that is not a power of 2 there is some
ﬁeld in which the nonzero sums of n squares are not a group. In fact, there is a ﬁeld that
settles this problem for all such n.
Theorem 3.1 (Pﬁster). In the ﬁeld R(X1, X2, X3, . . . ), for every positive integer n that is
not a power of 2 the nonzero sums of n squares are not closed under multiplication.
Proof. For any ﬁeld K, let SK(n) be the set of nonzero sums of n squares. Pﬁster [3] showed
that SK(ℓ)SK(m) = SK(ℓ◦m) where
ℓ◦m = min{k ≥1 : (x + y)k = 0 in F2[x, y]/(xℓ, ym)}
Since each monomial in the expansion of (x + y)ℓ+m−1 is divisible by xℓor ym, we have
ℓ◦m ≤ℓ+ m −1. As examples, 3 ◦3 = 4 and 3 ◦5 = 7. When n is a power of 2 we
have n ◦n = n, which implies as a special case that nonzero sums of n squares are closed
under multiplication when n is a power of 2. When n is not a power of 2, some intermediate
binomial coeﬃcient
 n
i

for 0 < i < n is odd, so (x + y)n ̸= 0 in F2[x, y]/(xn, yn). Therefore
n ◦n > n.
Generalizing a result of Cassels [1], Pﬁster [3] showed that if −1 is not a sum of squares
in a ﬁeld K then X2
1 + · · · + X2
n is not a sum of n −1 squares in K(X1, . . . , Xn). Since −1
is not a sum of squares in R(Xn+1, Xn+2, . . . ), it follows that X2
1 + · · · + X2
n is not a sum of
n −1 squares in R(Xn+1, Xn+2, . . . )(X1, . . . , Xn) = R(X1, X2, X3, . . . ). Call this ﬁeld F,
so SF (n −1) ⊊SF (n) for all n ≥2 by the example of X2
1 + · · · + X2
n. Therefore
SF (1) ⊊SF (2) ⊊· · · ⊊SF (n −1) ⊊SF (n) ⊊· · · ,
so if m < n then SF (m) ⊊SF (n). When n is not a power of 2, so n < n ◦n, we have
SF (n) ⊊SF (n ◦n). Therefore SF (n) ⊊SF (n)SF (n), which says there is a product of two
sums of n squares in F that is not a sum of n squares in F.
□
What can be said about sums of n squares being closed under multiplication in rings,
not just ﬁelds?
Theorem 3.2. If the sums of n squares in every commutative ring are closed under mul-
tiplication then n = 1, 2, 4, or 8.

<!-- page 7 -->
PFISTER’S THEOREM ON SUMS OF SQUARES
7
Proof. Our argument is taken from [2, pp. 278–279].
We will work in the particular ring A = R[X1, . . . , Xn, Y1, . . . , Yn]. Set u = X2
1 +· · ·+X2
n
and v = Y 2
1 + · · · + Y 2
n . Assuming sums of n squares in A are closed under multiplication,
uv is a sum of n squares in A, so there is an algebraic identity
(3.1)
(X2
1 + · · · + X2
n)(Y 2
1 + · · · + Y 2
n ) = f2
1 + · · · + f2
n
for some polynomials f1, . . . , fn ∈R[X1, . . . , Xn, Y1, . . . , Yn].
We will show f1, . . . , fn are each bilinear in the Xi’s and Yj’s, so n = 1, 2, 4, or 8 by the
Hurwitz 1, 2, 4, 8 theorem.
First note that by setting all variables equal to 0 in (3.1) we see that f1, . . . , fn all have
constant term 0. (This uses a special feature of R: a sum of squares is 0 only when each
term is 0.) Writing each of f1, . . . , fn as a sum of homogeneous polynomials in X1, . . . , Xn
(with coeﬃcients in R[Y1, . . . , Yn]), let d be the largest degree of such a term, so d ≥1.
Write fi,d for the homogeneous X-term in fi of degree d, so fi,d ̸= 0 for some i. If d > 1 then
equating the homogeneous X-terms of degree 2d on both sides of (3.1) implies 0 = Pn
i=1 f2
i,d,
so each fi,d is 0, which is a contradiction. Therefore d = 1, so each fi is linear in X1, . . . , Xn
with coeﬃcients in R[Y1, . . . , Yn]. By symmetry, each fi is also linear in Y1, . . . , Yn with
coeﬃcients in R[X1, . . . , Xn]. Thus each fi is bilinear in the Xi’s and Yj’s, so we are done
by the 1, 2, 4, 8 theorem.
□
It we look instead at the units in a ring that are sums of n squares (not necessarily of
other units), then such units being closed under multiplication also implies n is 1, 2, 4, or
8. This is a theorem of Dai, Lam, and Milgram and uses algebraic topology. See [2] or [7,
Prop. A.2].
References
[1] J. W. S. Cassels, “On the representation of rational functions as sums of squares,” Acta Arith. 9 (1964),
79–82.
[2] Z. D. Dai, T. Y. Lam, and R. J. Milgram, “Application of Topology to Problems on Sums of Squares,”
L’Enseign. Math. 27 (1981), 277–283.
[3] A. Pﬁster, “Zur Darstellung von −1 als Summe von Quadraten in einem K¨orper,” J. London Math. Soc.
40 (1965), 159–165.
[4] A. Pfsiter, “Multiplikative quadratische Formen,” Arch. Math. 16 (1965), 363–370.
[5] A. R. Rajwade, Squares, Cambridge Univ. Press, Cambridge, 1993.
[6] H. Zassenhaus and W. Eichhorn, “Herleitung von Acht- und Sechzehn-Quadrate-Identit¨aten mit Hilfe von
Eigenschaften der verallgemeinerten Quaternionen und der Cayley–Dicksonchen Zahlen,” Arch. Math.
17 (1966), 492–496.
[7] D. B. Shapiro, Compositions of Quadratic Forms, W. de Gruyter, Berlin, 2000.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*