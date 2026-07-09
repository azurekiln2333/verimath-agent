# Small Groups Up to Isomorphism

> **Source**: https://kconrad.math.uconn.edu/blurbs/gpisomlist.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SMALL GROUPS UP TO ISOMORPHISM
KEITH CONRAD
The table below lists all the groups of order ≤15, up to isomorphism. That is, any group
of order ≤15 is isomorphic to exactly one group on this list. We write G2 for G × G and
G3 for G × G × G, just as in linear algebra (where R3 means R × R × R).
n
Groups of order n
Number
1
{0}
1
2
Z/(2)
1
3
Z/(3)
1
4
Z/(4), (Z/(2))2
2
5
Z/(5)
1
6
Z/(6), S3
2
7
Z/(7)
1
8
Z/(8), Z/(4) × Z/(2), (Z/(2))3, D4, Q8
5
9
Z/(9), (Z/(3))2
2
10
Z/(10), D5
2
11
Z/(11)
1
12
Z/(12), Z/(2) × Z/(6), D6, A4, Q12
5
13
Z/(13)
1
14
Z/(14), D7
2
15
Z/(15)
1
The notation for these groups should be familiar to a student learning group theory
except perhaps for the group of order 12 denoted Q12, which can be described as a nontrivial
semidirect product Z/(3) ⋊Z/(4).1
Books that explicitly list groups of small order up to isomorphism usually stop at 15
since the number of non-isomorphic groups of order 16 jumps by quite a bit: there are 14
groups of order 16 up to isomorphism. Here they are.
Five are abelian:
Z/16Z,
Z/(8) × Z/(2),
(Z/(4))2, Z/(4) × (Z/(2))2,
(Z/(2))4.
Of the remaining nine groups of order 16, two can be described with dihedral groups:
D8,
Z/(2) × D4.
Two more can be described with quaternionic groups2:
Z/(2) × Q8,
Q16 = ⟨x, y|x8 = 1, y2 = x4, yxy−1 = x−1⟩.
1See https://kconrad.math.uconn.edu/blurbs/grouptheory/group12.pdf.
2Groups Q2n are described in https://kconrad.math.uconn.edu/blurbs/grouptheory/genquat.pdf.
1

<!-- page 2 -->
2
KEITH CONRAD
Two more can be described as mod 8 matrix groups:

a
b
0
1

: a, b ∈Z/(8), a ≡1, 3 mod 8

,

a
b
0
1

: a, b ∈Z/(8), a ≡1, 5 mod 8

.
(The analogous group of mod 8 matrices ( a b
0 1 ) where a ≡1, 7 mod 8 is isomorphic to D8.)
The remaining three groups of order 16 can be built as semi-direct products:
Q8 ⋊Z/(2),
Z/(4) ⋊Z/(4),
(Z/(2))2 ⋊Z/(4),
where Z/(2) acts on Q8 by having 1 mod 2 act by conjugation by i (since i2 = −1, conjuga-
tion by i on Q8 has order 2), Z/(4) acts on Z/(4) by having 1 mod 4 act by negation, and
Z/(4) acts on (Z/(2))2 by having 1 mod 4 act by the matrix A = ( 1 1
0 1 ).
Below is a table of these 14 groups, with the ﬁrst 5 being abelian. The row for each group
of order 16 counts solutions in the group to g2 = e, g4 = e, and g8 = e. A noncyclic group
has no element of order 16, so all elements have order dividing 8 and thus {g : g8 = e} is
the whole group except for the cyclic group of order 16.
G
|{g : g2 = e}|
|{g : g4 = e}|
|{g : g8 = e}|
1
Z/(16)
2
4
8
2
Z/(8) × Z/(2)
4
8
16
3
Z/(4) × Z/(4)
4
16
16
4
(Z/(2))2 × Z/(4)
8
16
16
5
(Z/(2))4
16
16
16
6
D8
10
12
16
7
D4 × Z2
12
16
16
8
Q8 × Z/(2)
4
16
16
13
Q8 ⋊Z/(2)
8
16
16
9
Q16
2
12
16
10
{( a b
0 1 ) : a ≡1, 3 mod 8}
6
12
16
11
{( a b
0 1 ) : a ≡1, 5 mod 8}
4
8
16
12
Z/(4) ⋊Z/(4)
4
16
16
14
(Z/(2))2 ⋊Z/(4)
8
16
16
The counts in the table prove these 14 groups are nonisomorphic except when the counts
all agree, which happens for the groups given the same color. Since abelian and nonabelian
groups are not isomorphic, it remains to compare Q8 × Z/(2) and Z/(4) ⋊Z/(4), and
Q8 ⋊Z/(2) and (Z/(2))2 ⋊Z/(4). In the second pair, Q8 ⋊Z/(2) and (Z/(2))2 ⋊Z/(4),
their centers are not isomorphic: the ﬁrst group has a cyclic center and the second group
has noncyclic center. While the ﬁrst pair, Q8 × Z/(2) and Z/(4) ⋊Z/(4), have isomorphic
(noncyclic) centers, just one nontrivial element of the center of Q8 × Z/(2) is a square in
the whole group, while two nontrivial elements in the center of Z/(4) ⋊Z/(4) are squares
in the whole group, so these groups are nonisomorphic.3
Let G(n) be the number of non-isomorphic groups of order n. A list of G(n) for n ≤200
is on
https://kconrad.math.uconn.edu/nonisomgp.html,
3See https://kconrad.math.uconn.edu/blurbs/grouptheory/group16.pdf for more information about
the groups of order 16.

<!-- page 3 -->
SMALL GROUPS UP TO ISOMORPHISM
3
for n ≤2000 is in [2, Appendix], and for n < 2047 is in [1, Appendix].
There is no general formula for G(n), but values can be given for some n depending on
its prime factorization:
• for prime p,
G(p) = 1,
G(p2) = 2,
G(p3) = 5,
and G(p4) =
(
14,
if p = 2,
15,
if p ̸= 2,
• for distinct primes p < q,
G(pq) =
(
1,
if q ̸≡1 mod p,
2,
if q ≡1 mod p,
• for distinct primes p < q < r, G(pqr) is determined by the following table.
r mod p
r mod q
q mod p
G(pqr)
̸≡1
̸≡1
̸≡1
1
≡1
̸≡1
̸≡1
2
̸≡1
≡1
̸≡1
2
̸≡1
̸≡1
≡1
2
̸≡1
≡1
≡1
3
≡1
≡1
̸≡1
4
≡1
̸≡1
≡1
p + 2
≡1
≡1
≡1
p + 4
Check this table says that, up to isomorphism, there are 4 groups of order 30, 6 groups
of order 42, and 2 groups of order 105.
References
[1] J. H. Conway, H. Dietrich, and E. A. O’Brien, “Counting groups: gnus, moas, and other exotica,” Math.
Intell., 30 (2008), 6–15. URL https://www.math.auckland.ac.nz/∼obrien/research/gnu.pdf.
[2] H. U. Besche, B. Eick, and E. A. O’Brien, “A millennium project: constructing small groups,” In-
ternat. J. Algebra Comput. 12 (2002), 623–644. URL https://www.worldscientific.com/doi/epdf/
10.1142/S0218196702001115.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*