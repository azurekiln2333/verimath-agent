# Cosets and Lagrange's Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/coset.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
COSETS AND LAGRANGE’S THEOREM
KEITH CONRAD
1. Introduction
Pick an integer m ̸= 0. For a ∈Z, the congruence class a mod m is the set of integers
a + mk as k runs over Z. We can write this set as a + mZ. This can be thought of as
a translated subgroup: start with the subgroup mZ and add a to it. This idea can be
carried over from Z to an arbitrary group, provided we distinguish between translation of
a subgroup on the left and on the right.
Deﬁnition 1.1. Let G be a group and H be a subgroup. For g ∈G, the sets
gH = {gh : h ∈H},
Hg = {hg : h ∈H}
are called, respectively, a left H-coset and a right H-coset.
In other words, a coset is what we get when we take a subgroup and shift it: a left coset
gH is shifted on the left side and a right coset Hg is shifted on the right side.1 The best
way to think about cosets is that they are shifted subgroups or translated subgroups.
Note g lies in both gH and Hg, since g = ge = eg. Typically gH ̸= Hg. When G is
abelian, though, left and right cosets of a subgroup by a common element are the same.
When an abelian group operation is written additively, an H-coset should be written as
g + H, which is the same as H + g.
Example 1.2. In the additive group Z, with subgroup mZ, the mZ-coset of a is a + mZ.
This is just a congruence class modulo m.
Example 1.3. In the group R×, with subgroup H = {±1}, the H-coset of x is xH =
{x, −x}. This is “x up to sign.”
Example 1.4. When G = S3, and H = {(1), (12)}, the table below lists the left H-cosets
and right H-cosets of every element of the group. Compute a few of them for non-identity
elements to satisfy yourself that you understand how they are found.
g
gH
Hg
(1)
{(1), (12)}
{(1), (12)}
(12)
{(1), (12)}
{(1), (12)}
(13)
{(13), (123)}
{(13), (132)}
(23)
{(23), (132)}
{(23), (123)}
(123)
{(13), (123)}
{(23), (123)}
(132)
{(23), (132)}
{(13), (132)}
Notice ﬁrst of all that cosets are usually not subgroups (some do not even contain the
identity). Also, since (13)H ̸= H(13), a particular element can have diﬀerent left and right
H-cosets. Since (13)H = (123)H, diﬀerent elements can have the same left H-coset. (You
have already seen this happen with congruences: 14 + 3Z = 2 + 3Z, since 14 ≡2 mod 3.)
1Marshall Hall’s book The Theory of Groups calls gH a right coset and Hg a left coset. Don’t do that.
1

<!-- page 2 -->
2
KEITH CONRAD
In the next section we will see how cosets look in some geometric examples, where we
can visualize cosets. Then we will see that cosets arise in certain decimal patterns and as
“inhomogeneous solution spaces” to linear equations or diﬀerential equations. Then we will
look at some general properties of cosets. The index of a subgroup in a group, which tells
us how many cosets the subgroup has (either on the right or on the left), will lead to the
most basic important theorem about ﬁnite groups: Lagrange’s theorem. We will see a few
applications of Lagrange’s theorem and ﬁnish up with the more abstract topics of left and
right coset spaces and double coset spaces.
2. Geometric examples of cosets
When a group is deﬁned in terms of vectors and matrices, we can often get a picture of
the group and its cosets.
Example 2.1. Let G = R2 and H = Re1 be the x-axis. The (left) H-coset of a vector
v ∈R2 is
v + H = v + Re1 = {v + ce1 : c ∈R}.
This is the line parallel to H (the x-axis) that passes through the endpoint of v. The H-
cosets in general are the lines parallel to H. Two parallel lines are either equal or disjoint,
so each pair of H-cosets is either equal or disjoint. In Figure 1, the H-cosets of v and v′
are equal while those of v and w are disjoint.
x
y
H
v + H = v′ + H
w + H
v
v′
w
Figure 1. The cosets of Re1 in R2.
Example 2.2. Let G = Aﬀ+(R), the 2 × 2 matrices ( x y
0 1 ) with x > 0 under matrix
multiplication. Geometrically, we identify elements of G with points (x, y) in the plane
where x > 0. Such points form a right half-plane:

x
y
0
1

←→(x, y) ∈R>0 × R.

<!-- page 3 -->
COSETS AND LAGRANGE’S THEOREM
3
The identity element becomes the point (1, 0). See Figure 2. This is quite similar to the
idea of identifying complex numbers x + yi with points (x, y) in the plane.
x
y
(x, y)
(1, 0)
Figure 2. The group Aﬀ+(R).
Unlike the geometric interpretation of complex number addition, which is ordinary vector
addition with the intuitive “parallelogram rule”, the group law on Aﬀ+(R) when written
in terms of points in the plane is unfamiliar: starting from

x
y
0
1
 
u
v
0
1

=

xu
xv + y
0
1

,

x
y
0
1
−1
=

1/x
−y/x
0
1

,
we get the group law on points
(x, y)(u, v) = (xu, xv + y),
(x, y)−1 =
1
x, −y
x

.
Each matrix ( x y
0 1 ) in Aﬀ+(R) breaks up as the product ( 1 y
0 1 )( x 0
0 1 ) (not as ( x 0
0 1 )( 1 y
0 1 )!).
These special types of matrices each form subgroups, which we will call H and K:
(2.1)
H =

1
y
0
1

: y ∈R

,
K =

x
0
0
1

: x > 0

.
They are pictured in Figure 3.
For ( a b
0 1 ) in Aﬀ+(R), what are its left and right H-cosets ( a b
0 1 )H and H( a b
0 1 )?
To
compute these multiply a general element of H on the left and right by ( a b
0 1 ):

a
b
0
1
 
1
y
0
1

=

a
ay + b
0
1

,

1
y
0
1
 
a
b
0
1

=

a
b + y
0
1

.
Here a and b are ﬁxed, while y varies over R. The numbers ay + b run over all of R and
the numbers b + y run over R. This means the left and right H-cosets of ( a b
0 1 ) in Aﬀ+(R)
are the same:
(2.2)

a
b
0
1

H = H

a
b
0
1

=

a
t
0
1

: t ∈R

.
In the picture of Aﬀ+(R), this is simply the vertical line parallel to H passing through the
point (a, b). See the ﬁrst picture in Figure 4.

<!-- page 4 -->
4
KEITH CONRAD
x
y
(1, 0)
(x, 0)
(1, y)
K
H
Figure 3. The group Aﬀ+(R).
To compute the left K-coset of ( a b
0 1 ), for x > 0 we have
(2.3)

a
b
0
1
 
x
0
0
1

=

ax
b
0
1

.
As x > 0 varies, the right side of (2.3) runs through all matrices of the form ( t b
0 1 ) with
t > 0. Therefore
(2.4)

a
b
0
1

K =

t
b
0
1

: t > 0

.
In particular, the left K-coset of ( a b
0 1 ) is determined by b alone and is independent of the
choice of a > 0: ( a b
0 1 )K = ( 1 b
0 1 )K. This is the horizontal line through (a, b). See the second
picture in Figure 4.
To ﬁnd out what the right K-coset of ( a b
0 1 ) is, multiply a general element of K by ( a b
0 1 )
on the right:

x
0
0
1
 
a
b
0
1

=

ax
bx
0
1

.
Letting x > 0 vary, we obtain
(2.5)
K

a
b
0
1

=

u
v
0
1

: u > 0, v = b
au

.
This is a half-line out of the origin with slope b/a (third picture in Figure 4). In particular,
the left and right K-cosets of ( a b
0 1 ) in Aﬀ+(R) are not the same if b ̸= 0. A right K-coset
of ( a b
0 1 ) depends on both a and b, or more precisely on their ratio b/a, while its left K-coset
depends only on b.
For both H and K, its collection of all left cosets and its collection of all right cosets
ﬁll up the group Aﬀ+(R) in Figure 5 without overlap: a family of parallel half-lines, either
horizontal or vertical, and a family of half-lines out of the origin.
Later in this handout, we will see that left (or right) cosets of a subgroup in a group
exhibit properties that can be seen in our geometric examples: diﬀerent left cosets of a

<!-- page 5 -->
COSETS AND LAGRANGE’S THEOREM
5
Figure 4. Left and Right Cosets of H and K in Aﬀ+(R).
Figure 5. Left and Right Coset Decompositions of Aﬀ+(R) by H and K.
subgroup are disjoint, and the collection of all left cosets of a subgroup cover the group
(likewise for right cosets).
3. Cosets and decimal expansions
Each rational number a/b whose denominator b is relatively prime to 10 has a decimal
expansion that is purely periodic. For example,
1
3 = .3333333 . . . ,
1
7 = .142857142857142857 . . . ,
15
41 = .609756097560975 . . .
where the repeating part has 1 term, 6 terms, and 5 terms respectively. We abbreviate the
decimal expansion by writing only the periodic part and put a line over it, so
1
3 = .3,
1
7 = .142857,
15
41 = .60975.
In the tables below are all the reduced proper fractions with denominator 7, 13, and 27.
(We don’t include 3/27 in the second table, for instance, since it is not reduced.)

<!-- page 6 -->
6
KEITH CONRAD
Fraction
Decimal
Fraction
Decimal
Fraction
Decimal
1/7
.142857
1/13
.076923
2/13
.153846
2/7
.285714
3/13
.230769
4/13
.307692
3/7
.428571
5/13
.384615
6/13
.461538
4/7
.571428
7/13
.538461
8/13
.615384
5/7
.714285
9/13
.692307
10/13
.769230
6/7
.857142
11/13
.846153
12/13
.923076
Fraction
Decimal
Fraction
Decimal
Fraction
Decimal
1/27
.037
2/27
.074
4/27
.148
5/27
.185
7/27
.259
8/27
.296
10/27
.370
11/27
.407
13/27
.481
14/27
.518
16/27
.592
17/27
.629
19/27
.703
20/27
.740
22/27
.814
23/27
.851
25/27
.925
26/27
.962
There are two interesting features revealed in this table:
• the decimal expansions for all the reduced fractions with the same denominator
have the same period length (denominator 7 has period length 6, denominator 13
has period length 6, and denominator 27 has period length 3),
• if we cyclically shift the digits in the repeating part of the decimal expansions of
a reduced fraction, we get the repeating part of the decimal expansion of another
reduced fraction with the same denominator.
The ﬁrst feature is explained by Euler’s theorem from elementary number theory, and
we won’t discuss it here.2 We want to focus on the second feature. First, let’s make sure
we understand what it is saying. The string of digits 142857 is the repeating part of the
decimal for 1/7, and if we shift the numbers one position to the left, getting 428571, we
look in the ﬁrst table and see it is the repeating part of the decimal for 3/7. If we shift
one position to the left again, we get 285714, and when we look at the ﬁrst table we ﬁnd
that is the repeating part of the decimal for 2/7. Similarly, 407 is the repeating part of the
decimal for 11/27, and if we shift the terms one position to the left we get 074, which the
second table tells us is the repeating part of the decimal for 2/27. Are you surprised by
this? It turns out this phenomenon, which even a grade school student could discover, is
actually cosets in disguise. This is best explained by an example.
Example 3.1. Consider 5/13, which the ﬁrst table tells us is .384615. Multiplying by 10
has the eﬀect of cyclically shifting the digits in the decimal one position to the left:
10 · 5
13 = 10(.384615) = 10(.384615384615 . . . ) = 3.84615384615 . . . = 3.846153.
The numerator of 10(5/13) is 50, and 50 ≡11 mod 13, so 50/13 = 11/13 + integer. Since
we already saw that 50/13 = 3.846153, the integer part of 50/13 is 3 and therefore 11/13 =
.846153. In other words, shifting the digits in .384615 one position to the left turns 5/13 into
11/13, and the reason is that shifting digits in a decimal one position to the left corresponds
to multiplication by 10 and 5 · 10 ≡11 mod 13.
If we want to shift the digits to the left one more time, the fraction we get will again
be obtained from multiplying the new numerator by 10 and reducing the product mod 13:
11 · 10 = 110 ≡6 mod 13, or in terms of the original numerator, 5 · 102 ≡6 mod 13. In
2See Theorem 4.3 in https://kconrad.math.uconn.edu/blurbs/ugradnumthy/eulerthm.pdf.

<!-- page 7 -->
COSETS AND LAGRANGE’S THEOREM
7
general, if 5 · 10k ≡r mod 13, where 0 ≤r < 13, then r/13 will have a decimal expansion
whose repeating part is the digits for 5/13 shifted to the left k times. All these decimals have
the same length, which is 6, and that means after we do this shifting 6 times we come back
to the original fraction and have run through all the cycle shifts of the digits in the decimal
for 5/13. The fractions we have created in this way are all r/13 where r ≡5 · 10k mod 13
for some k. In other words, the numerators of the fractions with denominator 13 having
a decimal with the same digit cycle (up to the choice of starting point) as the decimal for
5/13 is precisely {5 · 10k mod 13 : k = 1, 2, . . . }, which is a coset in (Z/(13))× of the cyclic
subgroup ⟨10 mod 13⟩.
In general, if a/b is a reduced fraction where (10, b) = 1, then the other reduced fractions
whose decimal expansion has a repeating block that is a shift of the repeating block of the
decimal for a/b are precisely those fractions with denominator b and numerator in the coset
a⟨10 mod b⟩of (Z/(b))×.
Example 3.2. The fractions 2/27, 11/27, and 20/27 all have decimals with digit cycle
074 up to a shift, in (Z/(27))× we have ⟨10 mod 27⟩= {1, 10, 19}, and modulo 27 the
numerators of the fractions are {2, 11, 20} = {2, 2 · 102, 2 · 10} = 2⟨10 mod 27⟩, which is a
coset of ⟨10 mod 27⟩in (Z/(27))×.
4. Inhomogeneous solution spaces are cosets
When solving a linear equation Ax = b (A is a matrix), where the right side is non-
zero, we call the equation inhomogeneous. The general solution to this type of equation is
x0 + y, where x0 is a particular solution of Ax = b and y is the general solution to the
(homogeneous) equation Ax = 0. Let’s see how the solutions to an inhomogeneous linear
equation or inhomogeneous linear diﬀerential equation are an example of a coset. I do not
think the two examples that follow will give insight into cosets; they simply serve to show
that cosets appear in courses usually taken before abstract algebra.
Example 4.1. Consider a system of linear equations, written as a matrix equation Ax = b,
where A is an m × n real matrix, b ∈Rm, and x is an unknown vector in Rn. Let W be
the solution set of the corresponding homogeneous equation, where the right side is 0:
W = {x ∈Rn : Ax = 0}.
This is a group under vector addition. (It contains 0 ∈Rn, if Ax = 0 and Ax′ = 0 then
A(x + x′) = Ax + Ax′ = 0 + 0 = 0, and A(−x) = −A(x) = −0 = 0.) For b ̸= 0, if the
equation Ax = b has a solution, say x0, then the general solution to Ax = b is x0 + W.
Indeed, for each x ∈Rn we have the following equivalences:
Ax = b ⇐⇒Ax = Ax0
since Ax0 = b
⇐⇒A(x −x0) = 0
⇐⇒x −x0 ∈W
⇐⇒x ∈x0 + W.
The solution set x0 + W is a coset of W in Rn.
Remark 4.2. Consider the linear diﬀerential equation
(4.1)
y′ + xy = x3.

<!-- page 8 -->
8
KEITH CONRAD
The solutions to y′ +xy = 0, where the right side is 0 (homogeneous case), are the functions
of the form ce−x2/2. A particular solution to the equation (4.1) is x2 −2, and anyone who
had a good course in diﬀerential equations will know the general solution to (4.1) must take
the form x2 −2 + ce−x2/2. Letting c vary, the solution set to (4.1) is x2 −2 + Re−x2/2. This
is a coset of functions, so the same phenomenon we met with linear equations also occurs
for linear diﬀerential equations.
5. Properties of cosets
We will generally focus our attention on left cosets of a subgroup. Proofs of the corre-
sponding properties of right cosets will be completely analogous, and can be worked out by
the reader.
Since g = ge lies in gH, every element of G lies in some left H-coset, namely the left
coset deﬁned by the element itself. (Take a look at Example 1.4, where (13) lies in (13)H.)
Similarly, g ∈Hg since g = eg.
A subgroup is always a left and a right coset of itself: H = eH = He. (This is saying
nothing other than the obvious fact that if we multiply all elements of a subgroup by the
identity, on either the left or the right, we get nothing new.) What is more important to
recognize is that we can have gH = H (or Hg = H) even when g is not the identity. For
instance, in the additive group Z, 10 + 5Z = 5Z. All this is saying is that if we shift the
multiples of 5 by 10, we get back the multiples of 5. Isn’t that obvious? In fact, the only
way we can have a + 5Z = 5Z is if a is a multiple of 5, i.e., if a ∈5Z.
For a subgroup H of a group G, and g ∈G, when does gH equals H?
Theorem 5.1. For g ∈G, gH = H if and only if g ∈H.
Proof. Since g = ge ∈gH, having gH = H certainly requires g ∈H.
Now we need to show that if g ∈H, then gH = H. We prove gH = H by showing each
is a subset of the other. Since g ∈H, gh ∈H for all h ∈H, so gH ⊂H. To see H ⊂gH,
note h = g(g−1h) and that g−1h is in H (since g−1 ∈H).
□
Example 5.2. Consider the subgroup H = {1, s} of D4. We have
sH = {s, s2} = {s, e} = H.
Two of the elements of D4 that are not in H are r and r2. Their left H-cosets are not equal
to H:
rH = {r, rs},
r2H = {r2, r2s}.
Notice the left H-cosets H, rH, and r2H are not just unequal (which means each has
an element not in another), but are in fact disjoint (which means no element of one is in
another). This is similar to Example 2.1, where the cosets are a family of parallel lines:
diﬀerent parallel lines are disjoint. This is a completely general phenomenon, as follows.
Theorem 5.3. If two left H-cosets share a common element, then they are equal. Equiv-
alently, two left H-cosets that are not equal have no elements in common, i.e., they are
disjoint.
Proof. To show left H-cosets with a common element are the same, suppose x belongs to
g1H and to g2H, say
(5.1)
x = g1h1 = g2h2

<!-- page 9 -->
COSETS AND LAGRANGE’S THEOREM
9
where h1, h2 ∈H. Then g1 = g2h2h−1
1 . Each element of g1H has the form g1h for some
h ∈H, and
g1h = g2(h2h−1
1 h) ∈g2H.
Since h was arbitrary in H, we see g1H ⊂g2H. The reverse inclusion, g2H ⊂g1H, follows
by a similar argument (use the equation g2 = g1h1h−1
2
instead).
□
By Theorem 5.3, no element lies in more than one left H-coset. We call an element of a
left coset a representative of that coset. A set of representatives for all the left H-cosets is
called a complete set of left coset representatives.
Example 5.4. By the table in Example 1.4, each element of S3 is in exactly one of H,
(13)H, and (23)H, so
(5.2)
S3 = H ∪(13)H ∪(23)H.
This is a union of disjoint sets. An example of a complete set of left coset representatives
of H is (1), (13), and (23). Another complete set of left coset representatives of H is (12),
(13), and (132).
Example 5.5. Let G = Z and H = mZ, for m > 0. The coset decomposition of H in G
(left and right is the same) is just the decompsition of Z into congruence classes modulo m:
(5.3)
Z = mZ ∪(1 + mZ) ∪(2 + mZ) ∪· · · ∪(m −1 + mZ).
It is standard to use {0, 1, . . . , m −1} as the coset representatives.
Example 5.6. Let G = Aﬀ+(R) and K = {( x 0
0 1 ) : x > 0}. We saw in Example 2.2 that
a left K-coset of a matrix depends only on the upper-right entry of the matrix: ( a b
0 1 )K =
{( x b
0 1 ) : x > 0}.
Moreover, since all matrices in a given left K-coset have a common
upper-right entry, we can use the upper-right entry to parametrize diﬀerent left K-cosets:
(5.4)
Aﬀ+(R) =
[
b∈R

1
b
0
1

K,
where the union is disjoint. Coset representatives are the matrices ( 1 b
0 1 ).
Example 5.7. Consider the (additive) group R and the subgroup Z. Every real number,
up to addition by an integer, looks like a number between 0 and 1 (more precisely, in the
half-open interval [0, 1)). Diﬀerent numbers in this range are not Z-translates of each other,
so [0, 1) is a complete set of (left) coset representatives of Z in R:
(5.5)
R =
[
0≤x<1
(x + Z),
where the sets making up this union are disjoint.
Example 5.8. We saw in Example 2.1, where G = R2, that the cosets of the x-axis Re1 in
the plane are the lines parallel to the x-axis. A complete set of left coset representatives of
Re1 is a choice of one point on each line parallel to the x-axis. These choices could be made
at random, but a nicer method is to use the points lying on a line (any line) not parallel to
the x-axis. Such a line will pass once through each line parallel to the x-axis. An example
of such a line is the y-axis, i.e., the y-axis is a set of coset representatives for Re1 in R2:
(5.6)
R2 =
[
y∈R
((0, y) + Re1),
where the union is disjoint. Coset representatives are {(0, y) : y ∈R}.

<!-- page 10 -->
10
KEITH CONRAD
The decompositions in (5.2), (5.3), (5.4), (5.5), and (5.6) have analogues in every group
G. For a subgroup H of G, every element of G lies in some left H-coset, and diﬀerent left
H-cosets are disjoint, so we can write G as a union of disjoint left H-cosets. Write these
diﬀerent cosets as giH, so we have a disjoint union
(5.7)
G =
[
i∈I
giH.
Here I is just an indexing set counting the number of diﬀerent left H-cosets in G. Formula
(5.7) is called the left H-coset decomposition of G. The particular multipliers gi (which are
nothing other than a particular choice of one element from each left H-coset) are a complete
set of left coset representatives of H in G.
In a group, the passage from H to gH by left multiplication by g leads to no collapsing
of terms. For instance, in Example 5.4, the cosets of {(1), (12)} in S3 all have size 2. Even
in cases of an inﬁnite subgroup, as in Example 2.1, the cosets all look like the original
subgroup (just shifted). Let’s prove such a comparison between a subgroup and each of its
cosets in general.
Theorem 5.9. Let H be a subgroup of the group G. Each left H-coset in G has a bijection
with H. In particular, when H is ﬁnite, the cosets of H all have the same size as H.
Proof. Pick a left coset, say gH. We can pass from gH to H by left multiplication by g−1:
g−1(gh) = h ∈H. Conversely, we can pass from H to gH by left multiplication by g. These
functions from gH to H and vice versa are inverses to each other, showing gH and H are
in bijection with each other.
□
Of course there is an analogous result for right cosets, which the reader can formulate.
6. The index and Lagrange’s theorem
For an integer m ̸= 0, the number of cosets of mZ in Z is |m|. This gives us an interesting
way to think about the meaning of |m|, other than its deﬁnition as “m made positive.”
Passing from Z to other groups, counting the number of cosets of a subgroup gives a useful
numerical invariant.
Deﬁnition 6.1. Let H be a subgroup of a group G. The index of H in G is the number of
left cosets of H in G. This number, which is a positive integer or ∞, is denoted [G : H].
The terminology “index” is due to Cauchy in 1815 to count something that turns out to
be [G : H] in a special case. Concretely, the index of a subgroup tells us how many times
we have to translate the subgroup around (on the left) to cover the whole group.
Example 6.2. Since H = {(1), (12)} has 3 left cosets in S3, by Example 5.4, [S3 : H] = 3.
Example 6.3. The subgroup H = {1, s} of D4 has four left cosets:
H,
rH = {r, rs},
r2H = {r2, r2s}, r3H = {r3, r3s}.
The index of H in D4 is 4.
Example 6.4. For a positive integer m, [Z : mZ] = m, since 0, 1, . . . , m −1 are a complete
set of coset representatives of mZ in Z.

<!-- page 11 -->
COSETS AND LAGRANGE’S THEOREM
11
Example 6.5. What is the index of 15Z inside 3Z? (Not inside Z, but 3Z.) Modulo 15, a
multiple of 3 is congruent to 0, 3, 6, 9, or 12. That is, we have the disjoint union
3Z = 15Z ∪(3 + 15Z) ∪(6 + 15Z) ∪(9 + 15Z) ∪(12 + 15Z).
Thus [3Z : 15Z] = 5.
Example 6.6. The index [R : Z] is inﬁnite, by Example 5.7: there are inﬁnitely many
cosets of Z in R.
Remark 6.7. If we allow ourselves to use the language of cardinal numbers, which permits a
distinction between diﬀerent orders of inﬁnity, then we could deﬁne [G : H] as the cardinality
of the set of left H-cosets. This would have no eﬀect on the meaning of a ﬁnite index, but
would allow a more reﬁned meaning in the case of an inﬁnite index. Since we will not have
much use for the index concept when it is inﬁnite, we stick with the more concrete approach
in Deﬁnition 6.1.
In the case of ﬁnite groups, there is a simple formula for the index of a subgroup.
Theorem 6.8. When G is a ﬁnite group, and H is a subgroup, [G : H] = |G|/|H|.
For example, this formula says the index of {(1), (12)} in S3 is 6/2 = 3. Compare with the
computation of the same index in Example 6.2. Theorem 6.8 lets us read oﬀthe index of the
subgroup just from knowing the size of the subgroup, without actual coset constructions.
Proof. Since G is ﬁnite, H has ﬁnitely many left cosets in G. Let t = [G : H], and write
the diﬀerent left cosets of H as g1H, . . . , gtH. We know that two left cosets of H are either
the same or are disjoint. Therefore we have
(6.1)
G = g1H ∪· · · ∪gtH,
where the union is disjoint. By Theorem 5.9, each left H-coset has the same size as H, so
computing the size of both sides of (6.1) tells us
(6.2)
|G| = t|H|.
Thus [G : H] = t = |G|/|H|.
□
Using the formula for the index as a ratio, we get the next “transitivity” result quite
easily in the case of ﬁnite groups.
Theorem 6.9. In a group G, indices are multiplicative in towers: for subgroups K ⊂H ⊂
G,
[G : K] = [G : H][H : K]
if [G : K] is ﬁnite or if [G : H] and [H : K] are ﬁnite. In particular, if G is ﬁnite then
[G : K] = [G : H][H : K].
An example of this when G is an inﬁnite group is G = Z, H = 3Z, and K = 15Z:
[G : K] = 15, [G : H] = 3 and [H : K] = 5.
Proof. First suppose G is a ﬁnite group. Theorem 6.8 implies
[G : H][H : K] = |G|
|H| · |H|
|K| = |G|
|K| = [G : K].
Now suppose G is possibly not ﬁnite. We will treat separately the cases when the right
side of the desired formula is ﬁnite and the left side is ﬁnite.

<!-- page 12 -->
12
KEITH CONRAD
Case 1: [G : H] and [H : K] are ﬁnite. Let m = [G : H] and n = [H : K]. Then G is
the union of m diﬀerent left H-cosets g1H, . . . , gmH and H is the union of n diﬀerent left
K-cosets h1K, . . . , hnK. We want to show [G : K] = mn, i.e., G is a union of mn diﬀerent
left K-cosets.
Since G = Sm
i=1 giH and H = Sn
j=1 hjK, we have giH = Sn
j=1 gihjK, so
G =
m
[
i=1
giH =
m
[
i=1
n[
j=1
gihjK,
so [G : K] ≤mn. To prove this inequality is an equality, we show the cosets gihjK are
diﬀerent as i and j vary.
Suppose gihjK = gi′hj′K for some i, j, i′, j′. We will show i = i′ and j = j′. Since
K ⊂H, we get gihjK ⊂giH and gi′hj′K ⊂gi′H, so giH and gi′H overlap. That means
giH = gi′H (Theorem 5.3), so i = i′ (the terms g1, . . . , gm lie in diﬀerent left H-cosets).
Therefore gihjK = gihj′K, so hjK = hj′K. That implies j = j′ since h1, . . . , hn are in
diﬀerent K-cosets.
Case 2: [G : K] < ∞. Since K ⊂H ⊂G, left K-cosets in H are special cases of left
K-cosets in G, so [H : K] ≤[G : K] < ∞. Each left H-coset in G is a union of left K-cosets
in G, so from [G : K] being ﬁnite we get [G : H] ≤[G : K]. Thus [G : H] and [H : K] are
ﬁnite, so by Case 1, [G : K] = [G : H][H : K].
□
In Theorem 6.8, where G is ﬁnite, we found that |H| divides |G| since the ratio |G|/|H|
is a positive integer. This is called Lagrange’s theorem.
Theorem 6.10 (Lagrange, 1771). In a ﬁnite group, the order of each subgroup divides the
order of the group.
Proof. Let G be a ﬁnite group, and H a subgroup. By (6.2), |H| divides |G|. In fact, we
found the ratio |G|/|H| counts the number of left H-cosets in G.
□
We will see some applications of Lagrange’s theorem in the next section.
The converse of Lagrange’s theorem is true for some groups (e.g., all cyclic groups), but
it is false in general: given a divisor of the order of the group, there need not be a subgroup
with that size.
Example 6.11. The smallest counterexample is A4, which has order 12. While A4 has
subgroups of order 1,2,3,4, and 12, it has no subgroup of order 6.
To prove there is no subgroup of order 6, we argue by contradiction. Suppose there is
a subgroup of A4 with order 6, say H. Then [A4 : H] = 12/6 = 2. We will show for each
g ∈A4 that g2 ∈H.
If g ∈H then clearly g2 ∈H. If g ̸∈H then gH is a left coset of H diﬀerent from H
(since g ∈gH and g ̸∈H), so from [G : H] = 2 the only left cosets of H are H and gH.
Which one is g2H? If g2H = gH then g2 ∈gH, so g2 = gh for some h ∈H, and that
implies g = h, so g ∈H, but that’s a contradiction. Therefore g2H = H, so g2 ∈H.
Every 3-cycle (abc) in A4 is a square: (abc) has order 3, so (abc) = (abc)4 = ((abc)2)2.
Thus H contains all 3-cycles in A4. The 3-cycles are
(123), (132), (124), (142), (134), (143), (234), (243)
and that is too much since there are 8 of them while |H| = 6. Hence H does not exist.

<!-- page 13 -->
COSETS AND LAGRANGE’S THEOREM
13
Example 6.12. The next counterexample to the full converse of Lagrange’s theorem, in
terms of size, is SL2(Z/(3)). This group has order 24. It has subgroups of order 1, 2, 3, 4,
6, 8, and 24, but no subgroup of order 12.
To see why there is no subgroup of order 12, assume otherwise. Each subgroup H of order
12 in SL2(Z/(3)) has index 2, so just as in the previous example one can show a square
in SL2(Z/(3)) must lie in H. A tedious count shows there are 10 squares in SL2(Z/(3)).
Since |H| = 12, we don’t yet have a contradiction. To reach a contradiction, we use the
two squares ( 1 1
0 1 ) = ( 1 2
0 1 )2 and ( 1 0
1 1 ) = ( 1 0
2 1 )2. They must be in H, so their products
( 1 1
0 1 )( 1 0
1 1 ) = ( 2 1
1 1 ) and ( 1 0
1 1 )( 1 1
0 1 ) = ( 1 1
1 2 ) lie in H. These products turn out not to be
squares, so they ﬁll up the available space in H. The inverses of these products also have to
lie in H, but an explicit calculation shows the inverses of these two products are matrices
not yet taken into account. Thus H is too small, so H does not exist.
Example 6.13. For n ≥5, An has no proper subgroup with index less than n,3 so A5 has
no subgroup with index 2, 3, or 4 even though it has subgroups of order 2, 3 or 4.
Remark 6.14. There is no simple dividing line between those ﬁnite groups that satisfy
the converse to Lagrange’s theorem (for each divisor, there is a subgroup of that order)
and those ﬁnite groups that do not. Three classes of ﬁnite groups that satisfy the con-
verse include abelian groups, dihedral groups, and groups of prime-power order. (These
are all special cases of “supersolvable” groups, and all supersolvable groups satisfy the con-
verse of Lagrange’s theorem, but some non-supersolvable groups also satisfy the converse
of Lagrange’s theorem.)
Since we deﬁned the index of a subgroup as the number of its left cosets, presumably we
need to introduce a corresponding index for the count of right cosets. However, an extra
“right index” concept is not necessary, as we now explain.
Theorem 6.15. For every subgroup H of G, there are as many left H-cosets as right
H-cosets.
Proof. We will give two proofs, one in the case of ﬁnite G and the other in the case of
general G.
The “right” analogue of Theorem 5.9 says that each right H-coset is in bijection with
H. Therefore, supposing G is ﬁnite, running through the proof of Theorem 6.8 with right
cosets in place of left cosets shows |G|/|H| is a formula for the number of right H-cosets in
G. We already saw this is a formula for the number of left H-cosets, so the number of left
and right H-cosets is the same.
Now suppose G is an arbitrary group, possibly inﬁnite.
We want to give a bijection
between the collections of left and right H-cosets. One’s ﬁrst guess, to send gH to Hg, is
not well-deﬁned. For instance, taking G = S3 and H = {(1), (12)}, we have
(13)H = (123)H = {(13), (123)},
but
H(13) = {(13), (132)},
H(123) = {(23), (123)}.
So passing from gH to Hg depends on the coset representative g, which means it makes
no sense as a function from cosets to cosets. (If you want to remember an example of an
attempt to deﬁne a function that is in fact not well-deﬁned, this is it.)
3See Corollary 8.1 in https://kconrad.math.uconn.edu/blurbs/grouptheory/Ansimple.pdf.

<!-- page 14 -->
14
KEITH CONRAD
The correct way to turn left cosets into right cosets is to use inversion. For a subset
S ⊂G, let S−1 = {s−1 : s ∈S}. For instance, since subgroups are closed under inversion,
check that H−1 = H and (H−1)−1 = H. If we invert a left coset gH, we obtain
(gH)−1 = H−1g−1 = Hg−1.
Similarly, (Hg)−1 = g−1H. The function f(gH) = (gH)−1 gives a bijection between left
and right H-cosets.
□
Theorem 6.15 does not say every right coset is a left coset, but only that the number of
each kind of coset is the same. For instance, we saw in Example 5.4 that the diﬀerent left
cosets of H = {(1), (12)} in S3 are
{(1), (12)},
{(13), (123)},
{(23), (132)}.
The right coset H(13) = {(13), (132)} is not the same as a left coset. However, the collection
of right H-cosets has 3 members:
{(1), (12)},
{(13), (132)},
{(23), (123)}.
7. Applications of Lagrange’s theorem
Lagrange’s theorem leads to group-theoretic explanations of some divisibility properties
of integers. The idea is this: to prove a | b, ﬁnd a group of order b containing a subgroup
of order a. After illustrating this in a few cases, we will use Lagrange’s theorem to extract
information about subgroups of a group.
Theorem 7.1. Binomial coeﬃcients are integers: for n ≥1 and 0 ≤m ≤n, the ratio
n
m

=
n!
m!(n −m)!
is an integer.
Proof. The order of Sn is n!. We are going to write down a subgroup with order m!(n−m)!.
Consider the permutations in Sn that separately permute the subsets {1, . . . , m} and
{m + 1, . . . , n}:
H = {σ ∈Sn : σ permutes {1, 2, . . . , m} and {m + 1, . . . , n}}.
The reader can check H is a subgroup, and |H| = m!(n −m)!. If the reader is concerned
about the degenerate cases m = 0 and m = n, where one of the conditions deﬁning H is an
empty condition, note these cases of the theorem are easily checked directly.
□
Theorem 7.2. For positive integers a and b, the ratios
(ab)!
(a!)b ,
(ab)!
(a!)bb!
are integers.
Proof. Write out the integers from 1 to ab in sets of a consecutive integers:
1, 2, . . . , a; a + 1, . . . , 2a; 2a + 1, . . . , 3a; . . . ; (b −1)a + 1, . . . , ba.
There are b of these sets, separated by semi-colons. The permutations of 1, . . . , ba that
permute each set within itself form a subgroup of Sab and has order (a!)b.
Therefore
(a!)b | (ab)!.

<!-- page 15 -->
COSETS AND LAGRANGE’S THEOREM
15
The stronger divisibility relation (a!)bb! | (ab)! can be explained by ﬁnding a subgroup of
Sab with order (a!)bb!. This is left as an exercise for the reader. Hint: The new subgroup of
Sab should contain the one constructed in the previous paragraph.
□
Integrality of the ﬁrst ratio in the theorem generalizes to
n!
k1!k2!···kd! ∈Z when k1 + k2 +
· · · + kd = n with d ≥1 and all ki in N.
Theorem 7.3. For m ≥1, let ϕ(m) = |(Z/(m))×| be the number of invertible numbers
modulo m. If m ≥3, then ϕ(m) is even.
Here is a table illustrating the evenness of ϕ(m) once m ≥3. Can you ﬁnd your own
explanation?
m
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
ϕ(m)
1
1
2
2
4
2
6
4
6
4
10
4
12
6
8
Proof. For m ≥3, {±1} is a subgroup of (Z/(m))× with order 2, so 2 | ϕ(m) by Lagrange.
□
Remark 7.4. Curiously, the initial partial sums of the numbers in the above table, added
to 1, are often but not always prime. See the table below. Composite values are in red and
some primes that are skipped include 17, 31, 37, and 41.
m
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
1 + Pm
k=1 ϕ(k)
2
3
5
7
11
13
19
23
29
33
43
47
59
65
73
Now we turn to applications of Lagrange’s theorem in group theory itself. (The previous
application to ϕ(m) is more properly considered an application to number theory than to
group theory.) In each application below, pay attention to how Lagrange’s theorem is used.
Theorem 7.5. Let G be a ﬁnite group and let H and K be subgroups with relatively prime
orders. Then H ∩K = {e}.
Proof. Since H ∩K is a subgroup of both H and K, its order divides both |H| and |K| by
Lagrange. Therefore, by relative primality of these orders, |H ∩K| = 1, so H ∩K = {e}.
□
Theorem 7.6. Let G be a ﬁnite group. If g has order n, then n | |G|. In particular,
g|G| = e for every g ∈G.
Proof. Let H = ⟨g⟩be the subgroup generated by g. The order of H is exactly the order of
g, so |H| = n. By Lagrange, n | |G|. Since gn = e and n | |G|, we get g|G| = e.
□
This theorem can be proved for abelian groups by a simpler method: see Corollary 4.3
in https://kconrad.math.uconn.edu/blurbs/grouptheory/order.pdf. In the abelian
case, we can ﬁrst prove g|G| = e and then deduce that the order of each element is a factor
of |G|. In Theorem 7.6, which allows groups to be nonabelian, the proof ﬁrst shows each
element has order dividing |G| and then deduces that g|G| = e for each g in G.
Corollary 7.7. If G is a ﬁnite group and k is an integer relatively prime to |G|, then the
k-th power function on G is invertible.
This is not saying the k-th power function is multiplicative on G, but only that it is a
bijection.

<!-- page 16 -->
16
KEITH CONRAD
Proof. By Bezout, when (k, |G|) = 1 we can write kℓ+ |G|m = 1 for some integers ℓand
m. Therefore
g = g1 = gkℓ(g|G|)m = gkℓ
since g|G| = 1. So we see how to invert the k-th power function: raise to the power ℓ, where
kℓ≡1 mod |G|.
□
Example 7.8. When G = D5, which has order 10, let’s raise all the elements to the third
power. The result is a rearrangement of the elements of the group. See the table below.
(Reﬂections don’t change since an odd power of a reﬂection is itself.)
g
1
r
r2
r3
r4
s
rs
r2s
r3s
r4s
g3
1
r3
r
r4
r2
s
rs
r2s
r3s
r4s
Since 3·7 ≡1 mod 10, the seventh power is the inverse of the third power: (g3)7 = g21 =
g · (g10)2 = g. For example, (r4)3 = r12 = r2 and (r2)7 = r14 = r4.
What about the converse of Corollary 7.7? That is, is the k-th power function on G
invertible only when k is relatively prime to |G|? This can be answered using Cauchy’s
theorem, but we don’t do that here.
Corollary 7.9. Every group of prime order is cyclic, and in fact each non-identity element
is a generator.
Proof. Let G be the group, with p = |G|.
Pick a non-identity element g from G.
By
Theorem 7.6, the order of g divides p and is greater than 1, so g has order p. Therefore
|⟨g⟩| = p, so ⟨g⟩= G.
□
Remark 7.10. Be careful not to mis-apply Corollary 7.9. While it tells us that the additive
group Z/(p) is cyclic (each non-zero number modulo p is an additive generator), it does
not tell us anything about the nature of the multiplicative group (Z/(p))×, which has order
p −1. The group (Z/(p))× is cyclic for prime p, but the proof of that is not as simple as for
Z/(p). It certainly does not come from Corollary 7.9, since (Z/(p))× does not have prime
order (when p > 3).
Corollary 7.11. Let p and q be primes. Each non-trivial proper subgroup of a group of
order pq is cyclic.
Proof. A nontrivial proper subgroup will have order equal to a non-trivial factor of pq,
which is either p or q. In either case, the subgroup has prime order and therefore is cyclic
by Corollary 7.9.
□
For instance, if we want to ﬁnd all the subgroups of a group of order 6 (or 15 or 21. . . ),
we can compute the cyclic group generated by each element.
Every non-trivial proper
subgroup will arise in this way, and we then throw in the trivial group and the whole group
to complete the list.
Here is an application of Lagrange’s theorem to a characterization of cyclic groups from
combinatorial information about their subgroups.
Theorem 7.12. A ﬁnite group that has at most one subgroup of each size is cyclic.
Proof. I learned this proof from F. Ladisch.
Let G be a group with at most one subgroup of each size, and let n = |G|. We will count
the elements of G by collecting together all elements that generate the same subgroup. That
is, for each cyclic subgroup H we will collect together all of its generators and then add up

<!-- page 17 -->
COSETS AND LAGRANGE’S THEOREM
17
the number of these generators as H varies. This accounts for each element of G exactly
once (each element generates some cyclic subgroup), so
n =
X
cyc. subgp. H
|{generators of H}|.
Every subgroup of G has order dividing n, by Lagrange’s theorem, so we can sum over
cyclic subgroups of G by summing over cyclic subgroups of order d for each d dividing n:
n =
X
d|n
X
cyc.H,|H|=d
|{generators of H}|.
All cyclic groups of order d have the same number of generators: if ⟨h⟩has order d then
each element of ⟨h⟩is ha for a unique a between 1 and d, and ha generates ⟨h⟩if and only
if (a, d) = 1. Thus the number of generators in a cyclic group of order d is |{1 ≤a ≤d :
(a, d) = 1}| = ϕ(d), so
(7.1)
n =
X
d|n
X
cyc.H,|H|=d
ϕ(d) =
X
d|n
ϕ(d)|{H ⊂G : |H| = d, H cyclic}|.
This equation is valid for every ﬁnite group G of order n.
In the particular group Z/(n) of order n, which is cyclic, there is a unique cyclic subgroup
of every order dividing n, so (7.1) for G = Z/(n) becomes
(7.2)
n =
X
d|n
ϕ(d).
If G is a group of order n and it has at most one subgroup of order d for each d dividing
n, then |{H ⊂G : |H| = d, H cyclic}| = 0 or 1 for all d dividing n, so
(7.3)
n =
X
d|n
ϕ(d)|{H ⊂G : |H| = d, H cyclic}| ≤
X
d|n
ϕ(d)
(7.2)
= n.
Therefore |{H ⊂G : |H| = d, H cyclic}| = 1 for all d dividing n: if the count were ever 0
then the inequality in (7.3) would be strict and hence n < n, a contradiction. Since G has
a cyclic subgroup of order d for each d dividing n, taking d = n shows G is cyclic.
□
The only subgroups used in this proof are cyclic, so we proved something slightly stronger
than what was stated in the theorem: a ﬁnite group that has at most one cyclic subgroup
of each size is cyclic.
Corollary 7.13. Let G be a ﬁnite group such that, for each d dividing |G|, the equation
xd = 1 in G has at most d solutions. Then G is cyclic.
Proof. We will show G has at most one subgroup of each size. If H is a subgroup of G with
order d, then every element of H satisﬁes the equation xd = 1 and thus, by hypothesis, H
is the complete set of solutions in G to the equation xd = 1. This shows there is at most
one subgroup of order d: if H and H′ are both subgroups of order d then H and H′ both
equal {g ∈G : gd = 1}, so H = H′.
□
We conclude our list of applications of Lagrange’s theorem with a result that stands in
some sense “dual” to Theorem 7.5: instead of the subgroups having relatively prime orders,
and getting information about the size of the intersection, we look at what happens when
the subgroups have relatively prime index.
What can be said about the index of their
intersection?

<!-- page 18 -->
18
KEITH CONRAD
Theorem 7.14. Let G be a ﬁnite group, with subgroups H and K. Set m = [G : H] and
n = [G : K]. Then
[m, n] ≤[G : H ∩K] ≤mn.
In particular, if m and n are relatively prime, then [G : H ∩K] = mn = [G : H][G : K].
Proof. Since H ∩K ⊂H ⊂G and H ∩K ⊂K ⊂G, Theorem 6.9 tells us
[G : H ∩K] = [G : H][H : H ∩K] = [G : K][K : H ∩K].
Thus m and n each divide [G : H ∩K], so their least common multiple divides [G : H ∩K]
as well.
Now we want to show [G : H ∩K] ≤mn. Writing this as
[G : H][H : H ∩K] ≤[G : H][G : K],
our desired inequality is the same as
(7.4)
[H : H ∩K] ≤[G : K].
The number [G : K] counts how many left K-cosets are in G. Every left K-coset has the
form gK for some g ∈G. Among these, some cosets contain elements of H. How many?
We will show there are [H : H ∩K] such cosets, and thus we obtain the inequality (7.4).
The point is, for h1 and h2 in H, that
(7.5)
h1K = h2K ⇐⇒h1(H ∩K) = h2(H ∩K).
(If this is true, then it tells us the number of left K-cosets of G represented by an element
of H is the same as the number of left (H ∩K)-cosets in H, since H ∩K is a subgroup of
H.) Well, on the left side of (7.5), there is such equality exactly when h1 = h2k for some
k ∈K. Then k = h−1
2 h1 lies in H as well, so k ∈H ∩K. But then the equation h1 = h2k
tells us h1(H ∩K) = h2(H ∩K). The reverse implication in (7.5) is left as an exercise for
the interested reader.
□
8. Left and right coset spaces
The usefulness of modular arithemetic (in number theory, cryptography, etc.) suggests
the possibility of carrying it over from Z to other groups. After all, since congruence classes
modulo mZ are just a special instance of a coset decomposition, why not think about (left)
cosets for subgroups of groups other than Z as a generalization of Z/(m)?
Deﬁnition 8.1. Let G be a group and H be a subgroup. The left coset space G/H :=
{gH : g ∈G} is the set consisting of the left H-cosets in G.
A left coset space is a set whose elements are the left cosets of a subgroup. It is a “set of
sets,” as the following examples illustrate.
Example 8.2. In the group S3, let H = {(1), (12)}. By (5.2), there are 3 left H-cosets:
S3/H = {H, (13)H, (23)H}
= {{(1), (12)}, {(13), (123)}, {(23), (132)}}.
Example 8.3. In Aﬀ+(R), with K = {( x 0
0 1 ) : x > 0}, each left K-coset contains one
matrix of the form ( 1 b
0 1 ), so
Aﬀ+(R)/K =

1
b
0
1

K : b ∈R

.

<!-- page 19 -->
COSETS AND LAGRANGE’S THEOREM
19
Example 8.4. In R, every Z-coset is represented by a real number in [0, 1), so (5.5) tells
us
R/Z = {x + Z : 0 ≤x < 1}.
Can we make G/H into a group using the group operation from G, in the same way that
Z/(m) inherits an additive group structure from that of Z? The natural idea would be to
multiply two left cosets by multiplying two representatives:
g1H · g2H := g1g2H.
Unfortunately, such an operation does not always make sense. That is, the coset on the
right can change if we change the coset representatives on the left without changing the
cosets themselves.
Example 8.5. Take G = S3 and H = {(1), (12)}. We have
(13)H = (123)H = {(13), (123)},
(23)H = (132)H = {(23), (132)},
but
(13)(23)H = (132)H,
(123)(132)H = H,
and (132)H ̸= H, so changing the coset representatives changed the ‘product’ coset.
In Example 8.5, multiplication of left cosets is not well-deﬁned: it depends on the choice
of coset representative, and thus is not an honest operation at the level of cosets.
When G is abelian, this kind of diﬃculty does not arise: if g1H = g′
1H and g2H = g′
2H,
then g1g2H = g′
1g′
2H. One can proceed and turn G/H into a group, just as Z/(m) is a
group for addition. When G is non-abelian (the far more typical case), there are special
kinds of subgroups, called normal subgroups, for which multiplication of left cosets is a
well-deﬁned operation in terms of representatives, and one can make G/H into a group by
multiplying coset representatives.
Why should we care about trying to make G/H into a group? Here are three reasons:
• The usefulness of modular arithmetic in Z/(m) suggests having an analogous con-
struction for other groups has got to be worthwhile, even if it is not yet clear what
we might be able to do with the construction. (Note: While we can both add and
multiply in Z/(m), we only have in mind that G/H could be a group, inheriting the
one operation on G, analogous just to addition in Z/(m).)
• Having groups of the form G/H is a method of constructing new groups out of old
ones (by replacing G with G/H). This could allow us to ﬁnd alternate models for
certain kinds of groups, which might be more convenient to use than other models.
• When G is ﬁnite and H is a non-trivial proper subgroup of G, both H and G/H
have order less than the order of G. If G/H is a group, then we have two groups
related to G that have order less than |G|. This turns out to be very useful in
proving theorems about ﬁnite groups by induction on the order of the group.
Remark 8.6. In addition to the left coset space G/H, one can also consider the right
H-coset space H\G := {Hg : g ∈G}.
9. Double cosets
A coset can be viewed as the result of multiplying an element on one side by a subgroup.
Allowing multiplying on both sides (by possibly diﬀerent subgroups) leads to the idea of a
double coset.

<!-- page 20 -->
20
KEITH CONRAD
Deﬁnition 9.1. Let G be a group and H and K be subgroups. A set of the form
HgK = {hgk : h ∈H, k ∈K}
is called an (H, K) double coset, or simply a double coset if H and K are understood.
While special instances of double cosets appeared in the work of Cauchy, their systematic
consideration in group theory is due to Frobenius.
In this section we will look at some examples of double cosets and see how they are
similar to and diﬀerent from left and right cosets.
Example 9.2. Let’s look at double cosets in S3, with H = {(1), (12)} and K = {(1), (13)}.
The double coset of (1) is
H(1)K = HK = {hk : h ∈H, k ∈K} = {(1), (12), (13), (132)}
and the double coset of (23) is
H(23)K = {(1)(23)(1), (1)(23)(13), (12)(23)(1), (12)(23)(13)}
= {(23), (123)}.
Unlike a coset, we now see that a double coset does not have to have order dividing the
order of the group (4 does not divide 6). Moreover, diﬀerent double cosets for the same
pair of subgroups can have diﬀerent orders (such as 4 and 2).
The reader can compute the (H, K)-double cosets of the other four elements of S3 and
ﬁnd only the two examples above repeating. (Or appeal to Theorem 9.7 below.)
Example 9.3. Consider the group S3 again, but now use H = K = {(1), (12)}. There are
only two diﬀerent double cosets:
H(1)H = HH = {(1), (12)},
H(13)H = {(13), (23), (123), (132)}.
Example 9.4. Take G = D4 = ⟨r, s⟩and H = K = {1, s}. The diﬀerent (H, H) double
cosets are
HH = H = {1, s},
HrH = {r, rs, r3s, r3},
Hr2H = {r2, r2s}.
This example shows the number of double cosets for a pair of subgroups need not divide
the order of the group (3 does not divide 8). This is a contrast to what happens with left
and right cosets of a subgroup.
Example 9.5. An ordinary coset is a special kind of double coset, where one of the sub-
groups is trivial: Hg{e} = Hg and {e}gK = gK.
Example 9.6. If G is abelian, then the product set HK is a subgroup of G and an (H, K)
double coset is just an ordinary coset of the subgroup HK.
Theorem 9.7. Fix two subgroups H and K of the group G. Every element of G lies in
some (H, K) double coset, and two (H, K) double cosets that overlap are equal. Equivalently,
diﬀerent (H, K) double cosets are disjoint and they collectively cover the whole group.
Proof. Clearly g ∈HgK: use h = e and k = e. Thus, every element of G is in some (H, K)
double coset.
Now assume HgK and Hg′K overlap:
(9.1)
hgk = h′g′k′,

<!-- page 21 -->
COSETS AND LAGRANGE’S THEOREM
21
where h and h′ belong to H and k and k′ belong to K. We want to prove HgK = Hg′K.
By (9.1) g = h−1h′g′k′k−1, so g lies in Hg′K. For h′′ in H and k′′ in K,
h′′gk′′ = h′′h−1h′gk′k−1k′′ ∈Hg′K.
Letting h′′ and k′′ vary, we obtain HgK ⊂Hg′K. The reverse inclusion is proved in the
same way, so HgK = Hg′K.
□
A generalization of left and right coset spaces in Section 8 is a double coset space
H\G/K = {HgK : g ∈G}.
This is a left or right coset space when H or K is trivial. Invertin elements turns G/H into
H\G. Similarly, inverting turns H\G/K into K\G/H.
We noted in Example 9.4 that the number of (H, K) double cosets does not have to
divide the order of the group. However, Frobenius found a formula involving double coset
spaces that does generalize the “index formulas” |G| = |H||G/H| = |H||H\G|, as follows.
Theorem 9.8. Let G be a ﬁnite group and H and K be subgroups. Then
|{(h, g, k) ∈H × G × K : hgk = g}| = |H||K||H\G/K|.
When H or K is trivial, this reduces to the index formula for the other subgroup.
10. History
The ﬁrst use of cosets in a group-theoretic setting was by Euler in the mid-1700s, when he
proved [2, Theorems 10–14] for prime p and a ̸≡0 mod p that ap−1 ≡1 mod p by reasoning
as in the proof of Theorem 7.6. More speciﬁcally, he showed the subgroup H = ⟨a mod p⟩
of the group G = (Z/(p))× has order equal to the order of a mod p and then proved (6.2)
in this case by using the cosets of H in G. Later [3, Theorems 8–11], [4, Sect. 195–213] he
used cosets to show that if (a, m) = 1 then aϕ(m) ≡1 mod m.
While group theory as its own branch of math took form in the 19th century, the term
“coset” was introduced in a paper by G. A. Miller [6] in 1910, written as co-set. The preﬁx
“co-” has its standard meaning of “together with”, as in the word coauthor. Before this pa-
per, Burnside’s book Theory of Groups of Finite Order from 1897 used right cosets to prove
Lagrange’s theorem [1, pp. 21–22], but it had no special terminology for cosets. Weber’s
Lehrbuch der Algebra from 1896 did have a name (in German) for cosets: Nebengruppen
(“nearby groups”) [7, p. 8]. Strictly speaking, Weber used this label for cosets of a subgroup
other than the subgroup itself. In German today, the term for coset is Nebenklasse.
The label “Lagrange’s theorem” also became standard in the 20th century. It appears in
the 19th century literature [5, p. 273], but not in Burnside [1, p. 21] or Weber [7, p. 8].
References
[1] W. Burnside, “Theory of Groups of Finite Order,” Cambridge Univ. Press, Cambridge, 1897. URL
https://archive.org/details/in.ernet.dli.2015.168629/mode/2up.
[2] L. Euler, Theoremata circa residua ex divisione potestatum relicta, Novi Commentarii Academiae Sci-
entiarum Imperialis Petropolitanae 7 (1761), 49–82. URL https://scholarlycommons.pacific.edu/
euler-works/262/.
[3] L. Euler, Theoremata arithmetica nova methodo demonstrata, Novi Commentarii Academiae Scien-
tiarum Imperialis Petropolitanae 8 (1763), 74–104. URL https://scholarlycommons.pacific.edu/
euler-works/271/. German translation at https://arxiv.org/abs/1203.1993.
[4] L. Euler, Tractatus de numerorum doctrina capita sedecim, quae supersunt, Commentationes Arithmeti-
cae 2 (1849), 503–575. URL https://scholarlycommons.pacific.edu/euler-works/792/.

<!-- page 22 -->
22
KEITH CONRAD
[5] G. Frobenius,
Ueber die Congruenz nach einem aus zwei endlichen Gruppen gebildeten Dop-
pelmodul, Journal f¨ur die reine und angewandte Mathematik 101 (1887), 273–299. URL https://
eudml.org/doc/148695.
[6] G. A. Miller, On a method due to Galois, Quarterly Journal of Mathematics 41 (1910), 382–384. URL
https://babel.hathitrust.org/cgi/pt?id=inu.30000050138258&seq=390.
[7] H. Weber, “Lehrbuch der Algebra,” Band II, F. Vieweg und Sohn, Braunschweig, 1896. URL https://
archive.org/details/lehrbuchderalgeb02weberich/page/n7/mode/2up.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*