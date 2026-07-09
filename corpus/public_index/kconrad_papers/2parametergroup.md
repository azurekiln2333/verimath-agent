# 2Parametergroup

> **Source**: https://kconrad.math.uconn.edu/blurbs/2parametergroup.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
A 2-PARAMETER NONABELIAN GROUP
KEITH CONRAD
1. Introduction
Set
G =

x
y
0
1/x

: x > 0, y ∈R

,
which is a group under matrix multiplication:

x
y
0
1/x
 
u
v
0
1/u

=

xu
xv + y/u
0
1/xu

,

x
y
0
1/x
−1
=

1/x
−y
0
x

.
We geometrically represent (
x
y
0 1/x ) as the point (x, y) in the plane. So ( 1 0
0 1 ) corresponds to (1, 0)
and we plot g = ( 2
2
0 1/2 ), h = ( 3
1
0 1/3 ), and several powers and products in Figure 1. Note gh ̸= hg.
x
y
(1, 0)
g
g2
g−1
g−2
h
h2
h−1
h−2
gh
hg
Figure 1. Powers and products of g = ( 2
2
0 1/2 ) and h = ( 3
1
0 1/3 ) in G.
1

<!-- page 2 -->
2
KEITH CONRAD
In G, there are two “natural” subgroups
H =

x
0
0
1/x

: x > 0

,
K =

1
y
0
1

: y ∈R

.
They are pictured below in Figure 2 as the points (x, 0) for H and the points (1, y) for K.
x
y
(1, 0)
(x, 0)
(1, y)
H
K
Figure 2. The subgroups H and K.
In Section 2 we will make pictures of conjugacy classes and conjugate subgroups, and in Section
3 we will see pictures of the left and right cosets of H and K.
2. Conjugacy Classes and Conjugate Subgroups
The conjugate of (
x
y
0 1/x ) by ( a
b
0 1/a ) is
(2.1)

a
b
0
1/a
 
x
y
0
1/x
 
a
b
0
1/b
−1
=

x
ab(1/x −x) + a2y
0
1/x

.
Equation (2.1) tells us conjugate elements of G have the same same upper left entry.
Therefore in our picture of G, conjugate elements of G have the same ﬁrst coordinate: they must
lie on the same vertical line. We can use the formula (2.1) to compute a conjugacy class: ﬁx x and
y, and let a and b vary on the right side of (2.1). Here are the results.
• The conjugacy class of the identity ( 1 0
0 1 ) is itself. See the green dot in Figure 3.
• Conjugates of ( 1 1
0 1 ) are found by setting x = y = 1 on the right side of (2.1). We get ( 1 a2
0 1 )
for all a > 0, which in Figure 3 is the red half-line through (1, 1) above the x-axis.
• Conjugates of ( 1 −1
0
1 ) are ( 1 −a2
0
1 ) for all a > 0, which in Figure 3 is the blue half-line through
(1, −1) below the x-axis.
• We now determine the conjugacy class of ( x
0
0 1/x ), where x > 0 and x ̸= 1. A conjugate
matrix has the form (
x
y
0 1/x ) for some y. We will now show, for x > 0 and x ̸= 1, that the

<!-- page 3 -->
A 2-PARAMETER NONABELIAN GROUP
3
matrix (
x
y
0 1/x ) for all y ∈R is conjugate to ( x
0
0 1/x ). This would mean that in Figure 3, the
conjugacy class of ( x
0
0 1/x ) for x > 0 with x ̸= 1 is represented by the whole vertical line
through (x, 0).
To prove our description of the conjugacy class of ( x
0
0 1/x ) is correct, this conjugacy class
includes the matrices ( 1 b
0 1 )( x
0
0 1/x )( 1 b
0 1 )−1 = ( x b(x−1/x)
0
1/x
), with b running through all real
numbers. Here b is variable and x is ﬁxed. Since x > 0 and x ̸= 1 we have x −1/x ̸= 0,
so the upper right entry of the conjugate matrix runs through all real numbers as b varies.
See the orange and purple vertical lines in Figure 3 corresponding to x = 3 and x = 5.
x
y
(1, 0)
(3, 0)
(5, 0)
(1, 1)
(1, −1)
Figure 3. Conjugacy classes of ( 1 1
0 1 ), ( 1 −1
0
1 ), ( 1 0
0 1 ), ( 3
0
0 1/3 ), and ( 5
0
0 1/5 ).
Turning from conjugacy classes of elements to conjugate subgroups, we will compute the sub-
groups of G that are conjugate to H = {( x
0
0 1/x ) : x > 0} and to K = {( 1 y
0 1 ) : y ∈R}. The answers
in these two cases will be very diﬀerent.
For a > 0 and b ∈R, we have by equation (2.1) with y = 0 that ( a
b
0 1/a )( x
0
0 1/x )( a
b
0 1/a )−1 =
( x ab(1/x−x)
0
1/x
), so the subgroup conjugate to H by ( a
b
0 1/a ) is
(2.2)

a
b
0
1/a

H

a
b
0
1/a
−1
=

x
ab(1/x −x)
0
1/x

: x > 0

.
On the right side of (2.2), a and b are ﬁxed and x varies. Since a and b occur on the right side
of (2.2) only through ab, conjugating H by matrices in G whose top two entries have the same
product leads to the same conjugate subgroup to H. Thus for b > 0

a
b
0
1/a

H

a
b
0
1/a
−1
=

ab
1
0
1/ab

H

ab
1
0
1/ab
−1

<!-- page 4 -->
4
KEITH CONRAD
since a · b = ab · 1, and for b < 0

a
b
0
1/a

H

a
b
0
1/a
−1
=

a|b|
−1
0
1/a|b|

H

a|b|
−1
0
1/a|b|
−1
since a · b = a|b| · (−1). Thus conjugating H by an element of G that is not in H (meaning b ̸= 0)
has the same eﬀect as conjugating H by a matrix of the form ( t
1
0 1/t ) or ( t −1
0 1/t ), where t > 0.
As an example,

1
1
0
1

H

1
1
0
1
−1
=

x
1/x −x
0
1/x

: x > 0

.
x
y
(1, 0)
H
( 1/4 1
0
4 )
( 1/4 −1
0
4 )
( 1 1
0 1 )
( 1 −1
0
1 )
( 2
1
0 1/2 )
( 2 −1
0 1/2 )
Figure 4. Conjugating H by ( 1 1
0 1 ), ( 1 −1
0
1 ), ( 2
1
0 1/2 ), ( 2 −1
0 1/2 ), ( 1/4 1
0
4 ), and ( 1/4 −1
0
4 ).
In Figure 4 this conjugate subgroup is represented by the set of all (x, 1/x−x) with x > 0, which
is the graph of y = 1/x −x for x > 0 (in red). The conjugate subgroup ( 2
1
0 1/2 )H( 2
1
0 1/2 )−1 is all
( x 2(1/x−x)
0
1/x
), which in Figure 4 is represented by the graph of y = 2(1/x −x) for x > 0 (in green).
More generally, from (2.2) the subgroup conjugate to H by ( a
1
0 1/a ) is represented as the graph of
y = a(1/x −x) for x > 0 and the subgroup conjugate to H by ( a −1
0 1/a ) is represented as the graph
of y = −a(1/x −x) for x > 0. These curves are pictured in Figure 4 for diﬀerent a.
What subgroups in G are conjugate to K? Since ( a
b
0 1/a )( 1 y
0 1 )( a
b
0 1/a )−1 = ( 1 a2y
0
1 ) we get

a
b
0
1/a

K

a
b
0
1/a
−1
=

1
a2y
0
1

: y ∈R

=

1
t
0
1

: t ∈R

= K,

<!-- page 5 -->
A 2-PARAMETER NONABELIAN GROUP
5
so the only subgroup of G conjugate to K is K. See Figure 5.
x
y
(1, 0)
K = gKg−1
Figure 5. The only conjugate subgroup of K is K.
3. Cosets
We will draw pictures for the left and right cosets of the subgroups H and K.
For g = ( a
b
0 1/a ), a typical element in gH is

a
b
0
1/a
 
x
0
0
1/x

=

ax
b/x
0
1/ax

where x > 0. Letting x run over all positive numbers, by a change of variables
gH =

ax
b/x
0
1/ax

: x > 0

=

t
ab/t
0
1/t

: t > 0

,
which is pictured in Figure 6 as the graph of y = ab/x for x > 0: the branch of a hyper-
bola passing through (a, b). The left H-cosets are branches of hyperbolas that ﬁll up G without
overlapping.
A typical element in the right coset Hg is

x
0
0
1/x
 
a
b
0
1/a

=

ax
bx
0
1/ax


<!-- page 6 -->
6
KEITH CONRAD
x
y
(1, 0)
H
g
gH
Figure 6. The left cosets of H: hyperbolas xy = constant, x > 0.
for x > 0. Letting x run over all positive numbers,
Hg =

ax
bx
0
1/ax

: x > 0

=

t
(b/a)t
0
1/t

: t > 0

,
which is pictured in Figure 7 as the graph of the ray y = (b/a)x coming out of the origin and
passing through (a, b). The right H-cosets are rays that ﬁll up G without overlapping.
Turning to the left and right cosets of K, a typical element in gK is

a
b
0
1/a
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
1/a

.
As y runs over all real numbers, ay + b runs over all real numbers, so
gK =

a
y
0
1/a

: y ∈R

,
which is pictured as the vertical line x = a. Similarly, a typical element of the right coset Kg is

1
y
0
1
 
a
b
0
1/a

=

a
b + y/a
0
1/a

,
and as y runs over R the numbers b + y/a run over R, so Kg = gK for each g ∈G. The left
K-cosets and right K-cosets are each the collection of all vertical lines, which ﬁll up G without
overlaps. See Figure 8.

<!-- page 7 -->
A 2-PARAMETER NONABELIAN GROUP
7
x
y
(1, 0)
H
g
Hg
Figure 7. The right cosets of H: rays coming out of (0, 0).
x
y
(1, 0)
K
g
gK =Kg
Figure 8. The left and right cosets of K: vertical lines.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*