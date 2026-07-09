# Dihedral Groups I

> **Source**: https://kconrad.math.uconn.edu/blurbs/dihedral.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
DIHEDRAL GROUPS
KEITH CONRAD
1. Introduction
For n ≥3, the dihedral group Dn is deﬁned as the rigid motions1 taking a regular n-gon
back to itself, with the operation being composition. These polygons for n = 3, 4, 5, and 6
are in Figure 1. The dotted lines are lines of reﬂection: reﬂecting the polygon across each
line brings the polygon back to itself, so these reﬂections are in D3, D4, D5, and D6.2
Figure 1. Regular n-gons for n = 3, 4, 5, 6
In addition to reﬂections, a rotation by a multiple of 2π/n radians around the center carries
the polygon back to itself, so Dn contains some rotations.
We will look at elementary aspects of dihedral groups: listing its elements, relations
between rotations and reﬂections, the center, and conjugacy classes. Throughout, n ≥3.
2. Finding the elements of Dn
Points in the plane at a speciﬁed distance to a given point form a circle, so points with
speciﬁed distances to two given points are the intersection of two circles, which is two
points (non-tangent circles) or one point (tangent circles). For instance, the blue points
in the ﬁgure below have the same distance to each of the two black points (centers of the
circles). So given two distinct points (the black points), there are at most two points in the
plane (the blue points) that can have speciﬁed distances to them.
1A rigid motion is a distance-preserving transformation, such as a rotation, a reﬂection, and a translation,
and is also called an isometry.
2Group theorists write D2n where other mathematicians write Dn, so a group theorist writes the group of
rigid motions of the square as D8, not D4. Why do they do this? See https://math.stackexchange.com/
questions/2560348.
1

<!-- page 2 -->
2
KEITH CONRAD
Points that are equidistant to the two blue points are on the line through the two black
points, so if we pick a third point not collinear with the black points, then its distances to
the two blue points are diﬀerent. That means a point in the plane is uniquely speciﬁed by
its distances to three noncollinear points. But on a regular polygon there is a sharper result.
Lemma 2.1. Every point on a regular polygon is determined, among all points on the
polygon, by its distances to two adjacent vertices of the regular polygon.
Proof. Let A and B be adjacent vertices of a regular polygon, so the line segment AB is an
edge of the polygon.
We want to show diﬀerent points P and Q on the polygon can’t have the same distance
to A and the same distance to B. If they did, then P and Q would lie on two circles CA and
CB centered at A and B. Since CA ∩CB has size at most two, and P and Q lie in CA ∩CB,
P and Q are the only points in CA ∩CB. However, that places P and Q on opposite sides
of AB, and a regular polygon doesn’t have two of its points on opposite sides of an edge of
the polygon: a regular polygon is always on one side of the line through an edge.
Therefore two points in a regular polygon can’t share the same distance to both A and
B, which means each point of the polygon is determined by its distances to A and B.
□
Theorem 2.2. The size of Dn is 2n.
Proof. Our argument has two parts: ﬁrst show |Dn| ≤2n then construct 2n diﬀerent
elements of Dn.
Step 1: |Dn| ≤2n.
Pick two adjacent vertices of a regular n-gon, and call them A and B as in Figure 2
below. An element g of Dn is a rigid motion taking the n-gon back to itself, and it must
carry vertices to vertices (how are vertices unlike other points in terms of their distance
relationships with all points on the polygon?) and g must preserve adjacency of vertices,
so g(A) and g(B) are adjacent vertices of the polygon.
B
A
P
g(A)
g(B)
Figure 2. Eﬀect of g ∈Dn on vertices A and B.
For each point P on the polygon, the location of g(P) is determined by its distances to
the adjacent vertices g(A) and g(B) by Lemma 2.1, so g is determined by g(A) and g(B).
Thus to bound |Dn|, it suﬃces to bound the number of possibilities for g(A) and g(B).
Since g(A) and g(B) are a pair of adjacent vertices, g(A) has at most n possibilities (there
are n vertices), and for each choice of g(A), the vertex g(B) has at most 2 possibilities (it
is one of the two vertices adjacent to g(A)). That gives us at most n · 2 = 2n possibilities,
so |Dn| ≤2n.
Step 2: |Dn| = 2n.
We will describe n rotations and n reﬂections of a regular n-gon.

<!-- page 3 -->
DIHEDRAL GROUPS
3
A regular n-gon can be rotated around its center in n diﬀerent ways to come back to
itself (including rotation by 0 degrees). Speciﬁcally, we can rotate around the center by
2kπ/n radians where k = 0, 1, . . . , n −1. This is n rotations.
To describe reﬂections taking a regular n-gon back to itself, look at the pictures in Figure
1: if n is 3 or 5, there are lines of reﬂection connecting each vertex to the midpoint of the
opposite side, and if n is 4 or 6 there are lines of reﬂection connecting opposite vertices and
lines of reﬂection connecting midpoints of opposite sides. These descriptions of reﬂections
work in general, depending on whether n is even or odd:
• For odd n, there is a reﬂection across the line connecting each vertex to the midpoint
of the opposite side. This is a total of n reﬂections (one per vertex). They are
diﬀerent because each one ﬁxes a diﬀerent vertex.
• For even n, there is a reﬂection across the line connecting each pair of opposite
vertices (n/2 reﬂections) and across the line connecting midpoints of opposite sides
(another n/2 reﬂections). The number of these reﬂections is n/2+n/2 = n. They are
diﬀerent because they have diﬀerent types of ﬁxed points on the polygon: diﬀerent
pairs of opposite vertices or diﬀerent pairs of midpoints of opposite sides.
The rotations and reﬂections are diﬀerent in Dn since a non-identity rotation ﬁxes no point
on the polygon, the identity rotation ﬁxes all points, and a reﬂection ﬁxes two points.
□
In Dn it is standard to write r for the counterclockwise rotation by 2π/n radians. This
rotation depends on n, so the r in D3 means something diﬀerent from the r in D4. However,
as long as we are dealing with one value of n, there shouldn’t be confusion.
Theorem 2.3. The n rotations in Dn are 1, r, r2, . . . , rn−1.
Here and below, we designate the identity rigid motion as 1.
Proof. The rotations 1, r, r2, . . . , rn−1 are diﬀerent since r has order n.
□
Let s be a reﬂection across a line through a vertex. See examples in Figure 3 below.3 A
reﬂection has order 2, so s2 = 1 and s−1 = s.
s
s
s
s
Figure 3. Some lines of reﬂection for n = 3, 4, 5, 6.
Theorem 2.4. The n reﬂections in Dn are s, rs, r2s, . . . , rn−1s.
3The convention here that s denotes a reﬂection across a line through a vertex matters only for even n,
where there are some reﬂections across a line that does not pass through a vertex, namely a line connecting
midpoints of opposite sides. When n is odd, all reﬂections ﬁx a line through a vertex, and any of them could
be used as s.

<!-- page 4 -->
4
KEITH CONRAD
Proof. The rigid motions s, rs, r2s, . . . , rn−1s are diﬀerent since 1, r, r2, . . . , rn−1 are diﬀerent
and we just multiply them all on the right by s. No rks is a rotation because if rks = rℓ
then s = rℓ−k, but s is not a rotation.
Since Dn has n rotations and n reﬂections, and no rks is a rotation, each rks is a
reﬂection.
□
The elements of Dn are rotations or reﬂections; there is no “mixed rotation-reﬂection”:
the product of a rotation ri and a reﬂection rjs (in either order) is just a reﬂection.
The geometric interpretation of the reﬂections s, rs, r2s, and so on is this: drawing all
lines of reﬂection for a regular n-gon and moving clockwise around the polygon starting
from a vertex ﬁxed by s, we meet successively the lines ﬁxed by rs, r2s, . . . , rn−1s. See
Figure 4. Convince yourself, for instance, that if s is the reﬂection across the line through
the rightmost vertex then rs is the next line of reﬂection counterclockwise.
s
rs
r2s
s
rs
r2s
r3s
s
rs
r2s
r3s
r4s
s
rs
r2s
r3s
r4s
r5s
Figure 4. Lines of reﬂection in Dn labeled by element of Dn ﬁxing them.
Let’s summarize what we have now found.
Theorem 2.5. The group Dn has 2n elements. As a list,
(2.1)
Dn = {1, r, r2, . . . , rn−1, s, rs, . . . , rn−1s},
In particular, all elements of Dn with order greater than 2 are powers of r.
Warning. Although each element of Dn with order greater than 2 has to be a power of
r, because the non-rotations are reﬂections and thus have order 2, it is false in general that
the only elements of order 2 are reﬂections. When n is even, rn/2 is a 180-degree rotation,
which has order 2. Clearly a 180-degree rotation is the only rotation with order 2, and it
lies in Dn only when n is even.
3. Relations between rotations and reflections
The rigid motions r and s do not commute. Their commutation relation is a fundamental
formula for computations in Dn, and goes as follows.
Theorem 3.1. In Dn,
(3.1)
srs−1 = r−1.
Proof. A short proof comes from rs being a reﬂection: (rs)2 = 1 ⇒rsrs = 1 ⇒srs = r−1,
and s = s−1 since s has order 2.
We now want to prove (3.1) in a longer way using a geometric interpretation of srs−1.
Since every rigid motion of a regular n-gon is determined by its eﬀect on two adjacent

<!-- page 5 -->
DIHEDRAL GROUPS
5
vertices, to prove srs−1 = r−1 in Dn it suﬃces to check srs−1 and r−1 have the same values
at a pair of adjacent vertices.
Recall s is a reﬂection ﬁxing a vertex of the polygon. Let A be a vertex ﬁxed by s and
write its adjacent vertices as B and B′, with B appearing counterclockwise from A and B′
appearing clockwise from A. This is illustrated in Figure 5, where the dashed line through
A is ﬁxed by s. We have r(A) = B, r−1(A) = B′, s(A) = A, and s(B) = B′.
B
A
B′
Figure 5. A vertex A and two adjacent vertices B and B′.
The values of srs−1 and r−1 at A are
(srs−1)(A) = (srs)(A) = sr(s(A)) = sr(A) = s(B) = B′
and
r−1(A) = B′,
while their values at B are
(srs−1)(B) = (srs)(B) = sr(s(B)) = sr(B′) = s(A) = A
and
r−1(B) = A.
Since srs−1 and r−1 agree at A and at B, they agree on the polygon, so srs−1 = r−1.
□
Equivalent ways of writing srs−1 = r−1 are (since s−1 = s)
(3.2)
sr = r−1s,
rs = sr−1.
What these mean is that when calculating in Dn we can move r to the other side of s by
inverting it. By induction (or by raising both sides of (3.1) to an integral power) check
(3.3)
srk = r−ks,
rks = sr−k
for every integer k. In other words, every power of r can be moved to the other side of s
by inversion. This also follows from rks being a reﬂection:
1 = (rks)2 = rksrks ⇒srk = r−ks−1 = r−ks.
Example 3.2. In D7, using (3.3)
r2sr6sr3 = r2(sr6)sr3 = r2(r−6s)sr3 = r2r−6ssr3 = r−4r3 = r−1 = r6
and
sr4sr3sr2 = s(r4s)r3(sr2) = s(sr−4)r3(r−2s) = ssr−4r3r−2s = r−3s = r4s.
The relation (3.2) involves a particular rotation and a particular reﬂection in Dn. In
(3.3), we extended (3.2) to any rotation and a particular reﬂection in Dn. We can extend
(3.3) to any rotation and any reﬂection in Dn: a general reﬂection in Dn is ris, so by (3.3)
(ris)rj
=
rir−js
=
r−jris
=
r−j(ris).

<!-- page 6 -->
6
KEITH CONRAD
In the other order,
rj(ris)
=
rirjs
=
risr−j
=
(ris)r−j.
This has a nice geometric meaning: when multiplying in Dn, every rotation can be moved
to the other side of every reﬂection by inverting the rotation. This geometric description
makes such algebraic formulas easier to remember.
Remark 3.3. The group D5 = {1, r, r2, r3, r4, s, rs, r2s, r3s, r4s} has order 10 and is non-
abelian, so it is fundamentally diﬀerent from Z/(10) despite having the same size. To detect
incorrectly typed or scanned commercial product ID numbers (ISBN for books, UPC for
supermarket items, VIN for cars, etc.), they often include an additional number called a
check digit. The check digit, which is based on the rest of the ID number, is sometimes com-
puted by a calculation mod 10, and some methods of computing a check digit can detect all
single-digit errors (misreading one digit in an ID number), and many adjacent transposition
errors (e.g., misreading . . . 29 . . . as . . . 92 . . .), but using mod 10 can’t detect every adjacent
transposition error. By labeling the 10 elements of D5 with 0, 1, . . . , 9, Verhoeﬀ[5, Chap.
4] used the nonabelian group law in D5 to create a novel method of assigning check digits
to ID numbers that detects all single-digit errors and all adjacent transposition errors. It
has never been widely adopted in practice, even after the basic idea was rediscovered by
Gumm [1]. Other references about this potential application of dihedral groups are [2], [3],
[4, Chap. 5] and [6].
Knowing how rotations and reﬂections interact under multiplication lets us compute the
center of Dn. The answer depends on whether n is even or odd.
Theorem 3.4. When n ≥3 is odd, the center of Dn is trivial. When n ≥3 is even, the
center of Dn is {1, rn/2}.
Proof. No reﬂection is in the center of Dn since reﬂections do not commute with r:
(ris)r = ri(sr) = rir−1s = ri−1s,
r(ris) = ri+1s
so if ris commutes with r then ri−1 = ri+1, which implies r2 = 1, but r has order n ≥3.
Suppose a rotation rj is in the center of Dn. Without loss of generality, 0 ≤j < n.
Having rj in Z(Dn) implies rjs = srj, which is equivalent to rjs = r−js, so rj = r−j. Thus
r2j = 1. Since r has order n, from r2j = 1 we get n | 2j, and 0 ≤2j < 2n. The only
multiples of n in {0, 1, . . . , 2n −1} are 0 and n, so 2j = 0 or 2j = n. If 2j = 0 then j = 0,
so rj = r0 = 1. If 2j = n then (i) n is even and (ii) j = n/2, so rj = rn/2, which is a
180-degree rotation.
If n is odd then the only option is j = 0, so rj = 1. Obviously 1 ∈Z(Dn), so Z(Dn) = {1}.
If n is even then rj is 1 or rn/2. Again, obviously 1 ∈Z(Dn). Is rn/2 in Z(Dn)? Let’s
check rn/2 commutes with every rotation and reﬂection in Dn. Clearly rn/2 commutes with
every ri, since all powers of r commute with each other. Now we check rn/2 commutes with
each reﬂection ris:
rn/2(ris) = rn/2+is,
(ris)rn/2 = rir−n/2s = rirn/2s = ri+n/2s = rn/2+is,
where rn/2 = r−n/2 because this follows from rn = 1. (That rn/2 is its own inverse also
makes sense geometrically, since rotating by 180◦or −180◦has the same eﬀect.)
□

<!-- page 7 -->
DIHEDRAL GROUPS
7
Example 3.5. The group D3 has trivial center. The group D4 has center {1, r2}.
For even n, the rotation rn/2 on a regular n-gon is by 180 degrees. Theorem 3.4 says this
rotation for even n is the only nontrivial rigid motion of a regular n-gon that commutes with
all other rigid motions of the n-gon. A 180-degree rotation around the origin commutes
with all rigid motions of R2 ﬁxing the origin, but a 180-degree rotation is not in Dn for odd
n because a regular n-gon for odd n is not carried back to itself by a 180-degree rotation.
4. Conjugacy
In Dn the geometric description of reﬂections depends on the parity of n: for odd n, the
lines of reﬂection all look the same – each line connects a vertex and the midpoint on the
opposite side – but for even n the lines of reﬂection fall into two types – lines through pairs
of opposite vertices and lines through midpoints of opposite sides. See Figures 6 and 7.
Figure 6. Lines of Reﬂection for n = 3 and n = 5.
Figure 7. Lines of Reﬂection for n = 4 and n = 6.
The geometrically diﬀerent types of reﬂections in Dn for even n arise algebraically in the
conjugacy classes of Dn: the conjugacy class of g is all xgx−1 for x ∈Dn.
Theorem 4.1. The conjugacy classes in Dn are as follows.
(1) If n is odd,
• the identity element: {1},
• (n −1)/2 conjugacy classes of size 2: {r±1}, {r±2}, . . . , {r±(n−1)/2},
• all the reﬂections: {ris : 0 ≤i ≤n −1}.
(2) If n is even,
• two conjugacy classes of size 1: {1}, {r
n
2 },
• n/2 −1 conjugacy classes of size 2: {r±1}, {r±2}, . . . , {r±( n
2 −1)},
• the reﬂections fall into two conjugacy classes: {r2is : 0 ≤i ≤
n
2 −1} and
{r2i+1s : 0 ≤i ≤n
2 −1}.

<!-- page 8 -->
8
KEITH CONRAD
In words, the theorem says each rotation is conjugate only to its inverse (which is another
rotation) except for the identity and (if n is even) except for the 180-degree rotation rn/2.
Also the reﬂections are all conjugate for odd n but break up into two conjugacy classes
for even n. The two conjugacy classes of reﬂections for even n are the two types we see in
Figure 7: those whose ﬁxed line connects opposite vertices (revens) and those whose ﬁxed
line connects midpoints of opposite sides (rodds).
Proof. Every element of Dn is ri or ris for some integer i. Therefore to ﬁnd the conjugacy
class of an element g we will compute rigr−i and (ris)g(ris)−1. The formulas
rirjr−i = rj,
(ris)rj(ris)−1 = r−j
as i varies show the only conjugates of rj in Dn are rj and r−j. Explicitly, the basic formula
srjs−1 = r−j shows us rj and r−j are conjugate; we need the more general calculation to
be sure there is nothing further that rj is conjugate to.
To ﬁnd the conjugacy class of s, we compute
risr−i = r2is,
(ris)s(ris)−1 = r2is.
As i varies, r2is runs through the reﬂections in which r occurs with an exponent divisible
by 2. If n is odd then every integer modulo n is a multiple of 2 (since 2 is invertible mod n
we can solve k ≡2i mod n for i given k). Therefore when n is odd
{r2is : i ∈Z} = {rks : k ∈Z},
so every reﬂection in Dn is conjugate to s. When n is even, however, we only get half the
reﬂections as conjugates of s. The other half are conjugate to rs:
ri(rs)r−i = r2i+1s,
(ris)(rs)(ris)−1 = r2i−1s.
As i varies, this gives us {rs, r3s, . . . , rn−1s}.
□
Since elements in the center of a group are those whose conjugacy class has size 1, the
calculation of the conjugacy classes in Dn gives another proof that the center of Dn is trivial
for odd n and {1, rn/2} for even n: we see in Theorem 4.1 that for odd n the only conjugacy
class of size 1 is {1}, while for even n the only conjugacy classes of size 1 are {1} and {rn/2}.
Appendix A. Commutators in Dn
In a group, a commutator is a product of the form ghg−1h−1, which is denoted [g, h]. (We
have [g, h] = e if and only if gh = hg, so the commutator is related to commuting.) The set of
commutators in a group contains the identity and it is closed under inversion since [g, h]−1 =
hgh−1g−1 = [h, g], but it is not necessarily closed under multiplication. For example, the
matrix −I2 = ( −1
0
0 −1 ) in SL2(R) is a product of commutators since −I2 = (( 1 1
0 1 )(
1 0
−2 1 ))2
and each matrix on the right side is a commutator in SL2(R): ( 1 1
0 1 ) = [( 2
0
0 1/2 ), ( 1 1/3
0
1 )] and
(
1 0
−2 1 ) = [( 1
0
2/3 1 ), ( 1/2 0
0
2 )]. However, −I2 is not a commutator in SL2(R).4 So the set of
commutators in a group may not be a subgroup.
What is the set of commutators in dihedral groups?
Theorem A.1. The commutators in Dn form the subgroup ⟨r2⟩.
4See the answer by Tom Goodwillie in https://mathoverflow.net/questions/44269/.
Note −I2 is a
commutator in the larger group GL2(R): −I2 = [( −1 0
0 1 ), ( 0 1
1 0 )].

<!-- page 9 -->
DIHEDRAL GROUPS
9
Proof. The commutator [r, s] is rsr−1s−1 = rrss−1 = r2, so r2 is a commutator. More
generally, [ri, s] = risr−is−1 = ririss−1 = r2i, so every element of ⟨r2⟩is a commutator.
To show every commutator is in ⟨r2⟩, we will compute [g, h] = ghg−1h−1 when g and h
are rotations or reﬂections and check the answer is always a power of r2.
Case 1: g and h are rotations.
Writing g = ri and h = rj, these commute so ghg−1h−1 is trivial.
Case 2: g is a rotation and h is a reﬂection.
Write g = ri and h = rjs. Then h−1 = h, so
ghg−1h−1 = ghg−1h = ri(rjs)r−i(rjs) = ri+jsrj−is = ri+1r−(j−i)ss = r2i.
Case 3: g is a reﬂection and h is a rotation.
By Case 2 the commutator hgh−1g−1 is a power of r2. Since (ghg−1h−1)−1 = hgh−1g−1,
passing to inverses tells us that ghg−1h−1 is a power of r2.
Case 4: g and h are reﬂections.
Write g = ris and h = rjs. Then g−1 = g and h−1 = h, so
ghg−1h−1 = ghgh = (gh)2 = (risrjs)2 = (ri−jss)2 = r2(i−j).
□
Remark A.2. If n is odd, then ⟨r2⟩= ⟨r⟩. If n is even, then ⟨r2⟩is a proper subgroup of
⟨r⟩.
References
[1] H. Peter Gumm, “A new class of check-digit methods for arbitrary number systems,” IEEE Trans-
actions on Information Theory 3¯1 (1985), 102–105. URL https://www.mathematik.uni-marburg.de/
∼gumm/Papers/ANewClassOfCheckDigitMethods.pdf.
[2] J. A. Gallian, “The mathematics of identiﬁcation numbers,” The College Math. Journal 22 (1991),
194–202. URL https://www.d.umn.edu/∼jgallian/ident.pdf.
[3] J. A. Gallian, “Error detection methods,” ACM Computing Surveys 28 (1996), 504–517.
[4] J. Kirtland, Identiﬁcation Numbers and Check Digit Schemes, MAA, Washington, DC, 2001.
[5] J. Verhoeﬀ, Error Detecting Decimal Codes, The Mathematical Centre, Amsterdam, 1969. URL
https://ir.cwi.nl/pub/13046.
[6] S. J. Winters, “Error detecting schemes using dihedral groups,” The UMAP Journal 11 (1990), 299–308.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*