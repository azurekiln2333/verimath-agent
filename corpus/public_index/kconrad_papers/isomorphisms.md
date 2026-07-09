# Isomorphisms

> **Source**: https://kconrad.math.uconn.edu/blurbs/isomorphisms.pdf  
> **Author**: Keith Conrad  
> **Topic**: mathematics  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
ISOMORPHISMS
KEITH CONRAD
1. Introduction
Groups that are not literally the same may be structurally the same. An example of this idea is
the relation between multiplication and addition via exponentiation:
(1.1)
exey = ex+y.
Every number in R>0 has the form ex for exactly one x ∈R, and (1.1) tells us that when we write
numbers in R>0 as ex then multiplying in R>0 corresponds to adding the exponents in R. Going
the other way, every real number has the form ln x for exactly one x > 0, and addition of logarithm
values corresponds to multiplication inside the logarithm:
ln(x) + ln(y) = ln(xy).
The functions exp: R →R>0 and ln: R>0 →R make the groups R>0 and R look the same: they
are each a bijective way of passing between the two groups that turn the operation in one group
into the operation in the other group (e.g. doubling in R is like squaring in R>0).
R
−2
−1
0
1
2
R>0
1/e2 1/e1
e
e2
Figure 1. The groups R and R>0, linked by x 7→ex and y 7→ln y.
Deﬁnition 1.1. An isomorphism f : G →eG between two groups G and eG is a bijective homomor-
phism. When there is an isomorphism between G and eG, the groups are called isomorphic and we
write G ∼= eG.
An isomorphism between two groups is a dictionary that lets us translate elements and operations
from one group to the other without losing essential information. For example, we’ll see that all
cyclic groups of the same size are isomorphic, so if we understand one cyclic group then we can
usually transfer that understanding to all the other cyclic groups of the same size. Isomorphisms
are the way to express how two groups that are diﬀerent are nevertheless basically the same.
2. Examples of isomorphisms
Example 2.1. The exponential function exp: R →R>0, sending each x ∈R to ex, is an isomor-
phism: it is a homomorphism since ex+y = exey and it is a bijection since it has an inverse function,
the natural logarithm.
1

<!-- page 2 -->
2
KEITH CONRAD
More generally, for each b > 0 with b ̸= 1 the function f : R →R>0 given by f(x) = bx is an
isomorphism: it is a homomorphism since f(x + y) = bx+y = bxby = f(x)f(y), and it is a bijection
since it has logb x as an inverse function. Figure 1 shows some corresponding elements of R and
R>0 under this isomorphism.
Going the other way, logb : R>0 →R is an isomorphism: it is a homomorphism since logb(xy) =
logb x + logb y, and it is a bijection since it has bx as an inverse function.
Example 2.2. The “exponential-type” function f : Z/(4) →(Z/(5))× where f(a mod 4) = 2a mod
5, is an isomorphism: it makes sense since 24 ≡1 mod 5 ⇒2a+4k = 2a24k ≡2a mod 5, and it is a
homomorphism since
f(a mod 4)f(b mod 4) = (2a mod 5)(2b mod 5) = 2a+b mod 5
and
f(a mod 4 + b mod 4) = f((a + b) mod 4) = 2a+b mod 5,
so f(a mod 4)f(b mod 4) = f(a mod 4+b mod 4). This function is a bijection from the data in the
table below.
a mod 4
0
1
2
3
2a mod 5
1
2
4
3
Example 2.3. The function f : Z/(4) →(Z/(5))× where f(a mod 4) = 4a mod 5, is not an iso-
morphism: it is a homomorphism by the same argument as in the previous example (just replace
2a with 4a), but f is not a bijection since it is not injective, as the table below shows (it is also not
surjective, as it misses two values).
a mod 4
0
1
2
3
4a mod 5
1
4
1
4
Example 2.4. The groups D3 and S3 are isomorphic. Evidence that they resemble each other is
that both groups have order 6, three elements of order 2, and two elements of order 3 (and of course
one element of order 1: the identity). To create an isomorphism from D3 to S3, label the vertices
of an equilateral triangle as 1, 2, and 3 (see picture below) so that each element of D3 permutes
the vertices and thus can be turned into an element of S3.
1
2
3
s
rs
r2s
Let r be a counterclockwise rotation by 120 degrees and s be the reﬂection across the horizontal
dashed line. Then rs and r2s are reﬂections across the other dashed lines. The vertex labels in the
picture lead to the table below turning elements of D3 into elements of S3.
D3 :
1
r
r2
s
rs
r2s
S3 :
(1)
(123)
(132)
(23)
(12)
(13)
The correspondence in the table is compatible with the group laws in D3 and S3, e.g., r has
order 3 and (123) has order 3, s has order 2 and (23) has order 2, and sr = r−1s while (23)(123) =
(123)−1(23). If we let f : D3 →S3 by the table above, it is a bijection and a tedious calculation
(omitted) can verify that it is a homomorphism. Since f is a bijective homomorphism from D3 to
S3, it is an isomorphism.

<!-- page 3 -->
ISOMORPHISMS
3
Example 2.5. The group Aﬀ(Z/(4)) is isomorphic to D4. The idea behind this is that each matrix
in Aﬀ(Z/(4)) can be written as ( a b
0 1 ) where a ∈{±1 mod 4} and b ∈Z/(4), and we can decompose
such a matrix as

a
b
0
1

=

1
b
0
1
 
a
0
0
1

where ( 1 1
0 1 ) mod 4 has order 4 in Aﬀ(Z/(4)), ( −1 1
0 1 ) mod 4 has order 2, and

−1
0
0
1
 
1
1
0
1

=

1
−1
0
1
 
−1
0
0
1

=

1
1
0
1
−1 
−1
0
0
1

,
which resembles the rule sr = r−1s in D4.
This suggests considering the function f : D4 →
Aﬀ(Z/(4)) where
f(rksℓ) =

(−1)ℓ
k
0
1

mod 4,
which makes sense since in rksℓthe exponent k only matters mod 4 and the exponent ℓonly matters
mod 2, which is also all that matters for k and ℓin the mod 4 matrix on the right. To check f is a
homomorphism we compute f(rksℓ)f(rk′sℓ′) and f((rksℓ)(rk′sℓ′)):
f(rksℓ)f(rk′sℓ′) =

(−1)ℓ
k
0
1
 
(−1)ℓ′
k′
0
1

=

(−1)ℓ+ℓ′
(−1)ℓk′ + k
0
1

,
and since sℓrk = r(−1)ℓksℓ(check this separately for even ℓand odd ℓ, trying ℓ= 0 and 1 ﬁrst),
f((rksℓ)(rk′sℓ′)) = f(rkr(−1)ℓk′sℓsℓ′)) = f(rk+(−1)ℓk′sℓ+ℓ′) =

(−1)ℓ+ℓ′
k + (−1)ℓk′
0
1

.
Thus f is a homomorphism. Its kernel is determined by solving f(rksℓ) = ( 1 0
0 1 ) mod 4, which
says ( (−1)ℓk
0
1 ) ≡( 1 1
0 1 ) mod 4, so ℓhas to be even and k ≡0 mod 4, which makes rksℓ= 1. Thus
f : D4 →Aﬀ(Z/(4)) is injective (kernel is trivial). Since D4 and Aﬀ(Z/(4)) both have order 8, an
injective function between them is surjective, so f is a bijection and thus is an isomorphism.
While there can be inﬁnitely many diﬀerent cyclic groups of the same size, they all turn out to
be isomorphic to each other. This is proved in the following two theorems.
Theorem 2.6. Every inﬁnite cyclic group is isomorphic to Z.
Proof. Let G = ⟨g⟩be an inﬁnite cyclic group, with generator g. Each element of G has the form
gn for some n ∈Z, and n is unique: if gn = gn′ where n ̸= n′, then without loss of generality n′ < n
so gn−n′ = 1 and n −n′ is a positive integer, so g has ﬁnite order and that contradicts ⟨g⟩being
inﬁnite.
Since gngn′ = gn+n′, the function f : Z →G where f(n) = gn is a homomorphism. This function
is injective since we showed gn ̸= gn′ when n ̸= n′, and it is surjective since g generates G, so every
element of G is some gn = f(n). Thus f is a bijection, so it is an isomorphism from Z to G.
□
Example 2.7. In Q×, the subgroup ⟨2⟩= {2n : n ∈Z} is inﬁnite cyclic with generator 2, so it is
isomorphic to Z by the function f : Z →⟨2⟩where f(n) = 2n.
Theorem 2.8. Every cyclic group of order m is isomorphic to Z/(m).
Proof. Let G = ⟨g⟩be a cyclic group of order m, with generator g. Since the order of g is the size
of ⟨g⟩, g has order m. Let f : Z/(m) →G by f(a mod m) = ga. We want to show this is a bijective
homomorphism.

<!-- page 4 -->
4
KEITH CONRAD
First we need to show f(a mod m) makes sense: it is deﬁned in terms of a representative a from a
congruence class, so we need to check that if a ≡a′ mod m then ga = ga′. We can write a = a′+mk
for some k ∈Z, so
ga = ga′+mk = ga′(gm)k = ga′1k = ga′.
To see f is a homomorphism,
f(a mod m)f(b mod m) = gagb = ga+b = f((a + b) mod m) = f(a mod m + b mod m).
To prove f is a bijection, since |⟨g⟩| = m = |Z/(m)| it suﬃces to prove just that f is injective or
just that f is surjective. Surjectivity is simpler: by the deﬁnition of a cyclic group with g being a
generator, every element of G is ga for some a ∈Z, so f(a mod n) = ga. Thus f is a bijection.1
□
Example 2.9. The groups Z/(6), U(7), and U(9) are all cyclic: Z/(6) has generator 1 mod 6, U(7)
has generator 3 mod 7 and U(9) has generator 2 mod 9. So there are isomorphisms f : Z./(6) →
U(7) and f′ : Z./(6) →U(9) where f(a mod 6) = 3a mod 7 and f′(a mod 6) = 2a mod 9.
The way we constructed an isomorphism from Z or Z/(m) to a cyclic group depended on a
choice of a generator, since f(1) = g is the generator we used. If we use a diﬀerent generator then f
becomes a diﬀerent isomorphism. Thus you should be careful not to confuse the statement that two
groups are isomorphic (there is some bijective homomorphism between them) and the statement
that a speciﬁc function between the groups is an isomorphism.
Example 2.10. In U(7) two generators are 3 and 5. They each lead to separate isomorphisms
Z/(6) →U(7), as shown in the table below.
a mod 6
0
1
2
3
4
5
3a mod 7
1
3
2
6
4
5
5a mod 7
1
5
4
6
2
3
Corollary 2.11. For a prime p, every group of order p is isomorphic to Z/(p).
Proof. Let G be a group of order p. Pick a nonidentity element g in G. Then the order of g divides
|G| = p and is not 1, so the order of g is p. Thus ⟨g⟩= G, so G is cyclic. By Theorem 2.8, there is
an isomorphism Z/(p) →G by a mod p 7→ga.
□
Example 2.12. Focusing on visualization, consider the quotient groups R/Z and R>0/2Z. In
R/Z, all integers are treated like 0 and the group is represented by [0, 1) or any half-open interval
[x, x + 1) for x ∈R.
In R>0/2Z, all integral powers of 2 are treated like 1 and the group is
represented by [1, 2) or any half-open interval [x, 2x) for x > 0.
R
−1
0
1
2
3
R>0
1/2 1
2
4
8
Figure 2. Diﬀerent sets of representatives for R/Z and R>0/2Z.
The pictures in Figure 2, with matching representatives in R and R>0 for R/Z and R>0/2Z
colored the same (using x 7→2x), suggest how R/Z and R>0/2Z are isomorphic to S1: both
1If instead we wanted to show f is injective we check its kernel is trivial: if f(a mod m) = 1 then ga = 1 so m | a
(because g has order m) and thus a ≡0 mod m.

<!-- page 5 -->
ISOMORPHISMS
5
quotient groups have a “wraparound” aspect that is similar to the unit circle S1.
A detailed
algebraic description of isomorphisms between S1, R/Z, and R>0/2Z is in Section 5.
3. Properties of isomorphisms
The relation of being isomorphic is an equivalence relation on groups: it is reﬂexive (G ∼= G),
symmetric (if G ∼= eG then eG ∼= G), and transitive (if G1 ∼= G2 and G2 ∼= G3 then G1 ∼= G3).
Reﬂexivity is easy to see: for every group G, the identity function G →G is an isomorphism from
G to itself. To show symmetry and transitivity, use the following two theorems.
Theorem 3.1. If f : G →eG is an isomorphism its inverse function f−1 : eG →G is also an
isomorphism.
Proof. First we show f−1 is a homomorphism. For y ∈eG, the deﬁnition of f−1(y) is the unique
x ∈G such that f(x) = y. For any y and y′ in eG, we can write y = f(x) and y′ = f(x′) for unique
x and x′ in G. Then yy′ = f(x)f(x′) = f(xx′), so
f−1(yy′) = xx′ = f−1(y)f−1(y′).
To show f−1 : eG →G is a bijection we appeal to the meaning of an inverse function.
Surjectivity: for each x ∈G, let y = f(x) ∈eG. Then f−1(y) = x, so each element of G is a value
of f−1 and thus f−1 is surjective.
Injectivity: since f−1 is a homomorphism, if suﬃces (and is equivalent) to show f−1 has trivial
kernel. If f−1(y) = eG then by the deﬁnition of an inverse function y = f(eG), which is e eG since
homomorphisms send the identity to the identity. Thus f−1 has trivial kernel, so it is injective.
□
Theorem 3.2. A composition of isomorphisms is an isomorphism.
Proof. Let f1 : G1 ∼= G2 and f2 : G2 ∼= G3 be group isomorphisms. We’ll show the composition
f1 ◦f2 : G1 →G3 is also an isomorphism:
(1) The composition of homomorphisms is a homomorphism, so f1 ◦f2 is a homomorphism.
(2) The composition of bijective functions is bijective (exercise), so f1 ◦f2 is a bijection.
□
Example 3.3. From the isomorphisms f : Z/(6) →U(7) and f′ : Z/(6) →U(9) by f(a mod 6) =
3a mod 7 and f′(b mod 9) = 2b mod 9, we get an isomorphism U(7) →U(9) by composing f−1
with f′: f′ ◦f−1 : U(7) →U(9) by 3a mod 7 7→2a mod 9.
More generally, if G = ⟨g⟩and eG = ⟨eg⟩are cyclic groups of the same size (possibly inﬁnite) then
there is an isomorphism ⟨g⟩→⟨eg⟩by gk 7→egk.
Properties of groups that are described purely in terms of the group operation (and not based
on what elements explicitly look like) transfer from a group to any isomorphic group. Here is an
example of two such properties.
Theorem 3.4. If G and eG are isomorphic groups then one is abelian if and only if the other is,
and one is cyclic if and only if the other is.
Proof. Suppose G is abelian and G ∼= eG. Let f : G →eG be an isomorphism from G to eG. For all
x, x′ ∈G we have
xx′ = x′x =⇒f(xx′) = f(x′x) =⇒f(x)f(x′) = f(x)f(x),
so every pair of values of f commute in eG. Since f is surjective, every element of eG is a value of f,
and thus all pairs of elements in eG commute, so eG is abelian.

<!-- page 6 -->
6
KEITH CONRAD
Conversely, if eG is abelian then for x and x′ in G we have f(x)f(x′) = f(x′)f(x), so f(xx′) =
f(x′x).
Since f is injective, xx′ = x′x, so all pairs of elements in G commute, and thus G is
abelian. (Alternatively, using the inverse isomorphism eG →G, from Theorem 3.1, lets us deduce
by reasoning similar to that in the previous paragraph that eG being abelian makes G abelian.)
Next suppose G is cyclic and f : G →eG is an isomorphism from G to another group eG. Write
G = ⟨g⟩= {ga : a ∈Z}. Every y ∈eG has the form y = f(x) for some x ∈G. Since g generates G,
x = ga for some integer a, so y = f(ga) = f(g)a. Thus every element of eG is a power of f(g), so eG
is cyclic and the isomorphism f sends any generator of G to a generator of eG.
Conversely, if eG is cyclic with generator eg, we will show G is cyclic. We can write eg = f(g) for
some g ∈G since f is surjective, and we’ll show g is a generator of G. For each x ∈G we can
write f(x) = egn for some integer n, so f(x) = f(g)n = f(gn). Since f is injective, x = gn, so
every element of G is a power of g and thus G = ⟨g⟩is cyclic. (Alternatively, using the inverse
isomorphism eG →G, from Theorem 3.1, we can use the reasoning from the previous paragraph
to show a generator of eG is mapped by that inverse isomorphism to a generator of G, so eG being
cyclic implies G is cyclic.)
□
Being isomorphic is a relation between groups, not a property (like being abelian or cyclic) of a
single group. Gerry Myerson2 once asked on a homework assignment if two speciﬁc groups G1 and
G2 are isomorphic and got a paper saying “G1 is, but G2 isn’t.” That is as absurd as asking if two
triangles T1 and T2 are congruent and hearing that T1 is congruent and T2 is not.
When classifying all groups that have a particular property, we don’t distinguish between isomor-
phic groups, since one group has the property if and only if the other does. For example, Corollary
2.11 says that every group of prime order p is isomorphic to Z/(p), and thus all groups of order p are
isomorphic to each other. We say they are “the same up to isomorphism.” Classiﬁcation questions
about groups are concerned not with ﬁnding all groups that have some particular property, but
rather with ﬁnding all the groups up to isomorphism that have the property.
Consider counting count how many essentially diﬀerent groups there are with a particular order.
Some groups of order 4 are
Z/(4),
(Z/(2))2,
U(5),
U(8),
U(10),
U(12),
⟨i⟩,
{(1), (12)(34), (13)(24), (14)(23)}
and some groups of order 6 are
Z/(6),
S3,
D3,
Z/(2) × Z/(3),
U(7),
U(9),
U(14),
U(18),
GL2(Z/(2)),
Aﬀ(Z/(3)).
The number of nonisomorphic groups of order 4 or order 6 is far less than these lists suggest. For
order 4 it turns out that
Z/(4) ∼= U(5) ∼= U(10) ∼= ⟨i⟩,
(Z/(2))2 ∼= U(8) ∼= U(12) ∼= {(1), (12)(34), (13)(24), (14)(23)}
and for order 6
Z/(6) ∼= Z/(2) × Z/(3) ∼= U(7) ∼= U(9) ∼= U(14) ∼= U(18),
S3 ∼= D3 ∼= GL2(Z/(2)) ∼= Aﬀ(Z/(3)).
It can be shown that every group of order 4 is isomorphic to Z/(4) or (Z/(2))2 (and these are
not isomorphic to each other since one is cyclic and the other isn’t), and every group of order 6 is
isomorphic to Z/(6) or S3 (and these are not isomorphic to each other since one is abelian and the
other isn’t).
The Online Encyclopedia of Integer Sequences (https://oeis.org/) is a massive database of
numerical sequences that have arisen in mathematics. If you ever meet a sequence and want to
2See https://mathoverflow.net/questions/53122/mathematical-urban-legends/62749.

<!-- page 7 -->
ISOMORPHISMS
7
know if it has been studied before, do a search on that website of the ﬁrst 5-10 terms. The very
ﬁrst entry, on https://oeis.org/A000001, is a count of the number of groups of each (small)
order up to isomorphism. The ﬁrst ten entries, starting with groups of order 0 (there are no such
groups), are 0, 1, 1, 1, 2, 1, 2, 1, 5, 2. The ﬁrst 2 means there are only 2 groups of order 4 up to
isomorphism, which was mentioned above: a group of order 4 is isomorphic to Z/(4) or to Z/(2))2.
The 5 means there are 5 groups of order 8 up to isomorphism.
Although isomorphic groups can be treated as “the same group,” that point of view does not
apply to subgroups of a group: if two subgroups are isomorphic to each other it does not generally
mean they behave in the same way as subgroups of the larger group.
For example, in D4 the
subgroups {1, s} and {1, r2} are isomorphic to each other (both are cyclic of order 2), but these
subgroups are quite diﬀerent as subgroups. For instance, r2 is in the center of D4 and s is not.
4. First isomorphism theorem
There is a fundamental theorem about group isomorphisms that lets us show when a quotient
group is isomorphic to another (possible more concrete) group. It is traditionally called the ﬁrst
isomorphism theorem.3
Theorem 4.1. Let f : G →eG be a group homomorphism with kernel K. The “induced function”
f : G/K →eG where f(gK) = f(g) is an injective homomorphism, it has the same image as f, and
f is an isomorphism of G/K with f(G). In particular, if f is surjective then G/ ker f ∼= eG.
Example 4.2. Let f : Z →C× by f(n) = in. Then f is a homomorphism (in+n′ = inin′), its
image is {1, i, −1, −i} = ⟨i⟩, and its kernel is 4Z since i has order 4 (in = 1 if and only if 4 | n).
Then the ﬁrst isomorphism theorem says Z/4Z ∼= ⟨i⟩by a mod 4 7→ia.
Example 4.3. Let f : Z →U(7) by f(n) = 2n mod 7. Then f is a homomorphism (2n+n′ ≡
2n2n′ mod 7), its image is {1, 2, 4 mod 7} since 2 mod 7 has order 3, and its kernel is 3Z since
2 mod 7 has order 3. The ﬁrst isomorphism theorem says Z/3Z ∼= {1, 2, 4 mod 7} = ⟨2 mod 7⟩by
a mod 3 7→2a mod 7.
Example 4.4. Let f : Z →U(7) by f(n) = 3n mod 7. Then f is a homomorphism (3n+n′ ≡
3n3n′ mod 7), its image is U(7) since 3 mod 7 is a generator, and its kernel is 6Z since 3 mod 7 has
order 6. The ﬁrst isomorphism theorem says Z/6Z ∼= U(7) by a mod 6 7→3a mod 7.
Example 4.5. The function f : R →S1 where f(x) = cos x + i sin x is a homomorphism that is
surjective (every point on S1 is cos x + i sin x for an x ∈R) and its kernel is 2πZ, so R/2πZ ∼= S1.
Example 4.6. The determinant det: GL2(R) →R× is a homomorphism (det(AB) = det A det B
for all A, B ∈GL2(R), and invertible matrices have nonzero determinant) that is surjective since
each δ ∈R× is the determinant of ( δ 0
0 1 ), and the kernel of det is, by deﬁnition, the group SL2(R) of
2×2 real matrices with determinant 1. The ﬁrst isomorphism theorem says GL2(R)/ SL2(R) ∼= R×
by A 7→det A, where A is the coset A SL2(R).
By similar reasoning, GL2(Z/(m))/ SL2(Z/(m)) ∼= U(m).
Here are two ways to think about what the ﬁrst isomorphism theorem is saying.
(1) Collapsing a group G modulo the kernel of a homomorphism out of G lets us identify the
quotient group of G by the kernel with the image of the homomorphism.
3There are also traditional results called the second and third isomorphism theorems, which we don’t discuss here.

<!-- page 8 -->
8
KEITH CONRAD
(2) If you want to show a quotient group G/N is isomorphic to some other group eG, write down
a homomorphism f : G →eG that’s surjective with kernel N. Then the induced function
f : G/N →eG where f(gN) = f(g) is a homomorphism that’s surjective (it has the same
image as f, which is f(G) = eG) and injective (part of the ﬁrst isomorphism theorem), so f
is an isomorphism from G/N to eG.
With examples and some viewpoints laid out, we now prove the ﬁrst isomorphism theorem. Pay
close attention to each step and try to understand what the ideas mean.
Proof. Deﬁne f : G/K →eG by f(gK) = f(g). This is well-deﬁned because
gK = g′K =⇒g = g′k for some k ∈K =⇒f(g) = f(g′k) = f(g′)f(k) = f(g′)
since k ∈K = ker f. The function f is a homomorphism since
f(g1K)f(g2K) = f(g1)f(g2) = f(g1g2)
and
f(g1K · g2K) = f(g1g2K) = f(g1g2).
The values of f are {f(gK) : g ∈G} = {f(g) : g ∈G}, which is the image of f, so f and f have
the same image in eG.
Finally, f : G/K →eG is injective since its kernel is trivial: if f(gK) = 1 then f(g) = 1 so
g ∈ker f = K, and thus gK = K, which is the identity in G/K.
The function f : G/K →eG has image f(G), so if we shrink the target group from eG to f(G)
then this makes f : G/K →f(G) surjective (same formula as before: f(gK) = f(g)), and it is also
injective (its kernel is trivial), so G/K ∼= f(G) by using the function f.
□
A visual way to describe the ﬁrst isomorphism theorem is through a commutative diagram.
Starting with the homomorphism f : G →eG having kernel K, the reduction map rK : G →G/K
(a generalization of mod m reduction Z →Z/(m)) is a homomorphism with kernel K, and what
the ﬁrst isomorphism theorem says is that the diagram of groups and homomorphisms f and rK
below can be ﬁlled in with a homomorphism f so that both ways of going around the diagram from
G to eG are the same function (the diagram “commutes”). That is, f ◦rK = f as functions G →eG,
since f(rK(g)) = f(gK) = f(g) for all g ∈G.
G
f
/
rK
!
eG
G/K
f (exists!)
=
5. Two isomorphisms with the circle group
Returning to the groups in Figure 2, let’s relate them to the unit circle S1, a subgroup of C×.
Theorem 5.1. The groups S1, R/Z, and R>0/2Z are all isomorphic.
In trigonometry, we treat the circle like R/360Z when using degrees (360 = 0 and −180 = 180)
and R/2πZ when using radians (2π = 0 and −π = π). Theorem 5.1 uses R/Z just to emphasize
that algebraically there is nothing special about degrees or radians.

<!-- page 9 -->
ISOMORPHISMS
9
Proof. We’re going to build isomorphisms R/Z →S1 and R/Z →R>0/2Z. This doesn’t directly
include an isomorphism between S1 and R>0/2Z, but we can get one by composing one of the
indicated isomorphisms with the inverse of the other (see Theorems 3.1 and 3.2).
Part 1: Create an isomorphism R/Z →S1.
Let f : R/Z →S1 by f(x) = cos(2πx) + i sin(2πx). (Where does this formula come from? We
use 2πx, not x, because the identity element 0 in R/Z has to go to the identity element 1 in S1
and the cosine and sine functions are 2π-periodic, not Z-periodic, so we want integers to turn into
integral multiples of 2π before taking their cosines and sines.)
Since the domain of f is a quotient group and it’s deﬁned by a formula in terms of representatives
of R/Z, we need to check ﬁrst that f is well-deﬁned. Then we’ll check it’s a homomorphism and
bijective.
f is well-deﬁned. If y = x in R/Z then y = x + k for some k ∈Z, so
cos(2πy) + i sin(2πy) = cos(2π(x + k)) + i sin(2π(x + k))
= cos(2πx + 2πk) + i sin(2πx + 2πk)
= cos(2πx) + i sin(2πx)
since the cosine and sine functions are 2π-periodic.
f is a homomorphism. For x and x′ in R/Z,
f(x)f(x′) = (cos(2πx) + i sin(2πx))(cos(2πx′) + i sin(2πx′))
= (cos(2πx) cos(2πx′) −sin(2πx) sin(2πx′)) + i(cos(2πx) sin(2πx′) + sin(2πx) cos(2πx′)).
(5.1)
The addition formulas for cosine and sine are
cos(α + β) = cos(α) cos(β) −sin(α) sin(β),
sin(α + β) = sin(α) cos(β) + cos(α) sin(β).
Comparing this to (5.1), we have
f(x)f(x′) = cos(2πx + 2πx′) + i sin(2πx + 2πx′) = f(2π(x + x′)),
so f is a homomorphism.
f is injective. Since f is a homomorphism, it suﬃces to check ker f is trivial: we want to show
if f(x) = 1 then x = 0, i.e., x ∈Z.
The condition f(x) = 1 says cos(2πx) + i sin(2πx) = 1, so cos(2πx) = 1 and sin(2πx) = 0 .
The solutions of sin t = 0 in R are the integral multiples of π, so 2πx = πn for n ∈Z. Thus
x = n/2, so x is an integer (if n is even) or a half-integer (if n is odd). We want x to be an integer,
so we want n to be even.
To n is even, we’ll show it’s not odd. If n were odd, so n = 2m + 1 for an integer m, then
cos(2πx) = cos(2π(n/2)) = cos(πn) = cos(π(2m + 1)) = cos(2πm + π) = cos(π) = −1,
but recall above that cos(2πx) = 1. We have a contradiction, so n is even. Thus x = n/2 ∈Z, so
x = 0.
f is surjective.
Let z ∈S1, so z ∈C× with |z| = 1.
Write z in polar coordinates: z =
r(cos θ + i sin θ) where r > 0 and θ ∈[0, 2π). Then |z| =
p
r2 cos2 θ +2 sin2 θ =
√
r2 = r, so r = 1,
and that leaves us with z = cos θ + i sin θ = f(θ/2π).
Part 2: Create an isomorphism R/Z →R>0/2Z.
Let f : R/Z →R>0/2Z by f(x) = 2x, meaning f(x+Z) = 2x2Z. (Where does this formula come
from? We want to convert addition into multiplication, so the function should involve exponenti-
ation. The real numbers that are trivial in R/Z are integers and the positive real numbers that

<!-- page 10 -->
10
KEITH CONRAD
are trivial in R>0/2Z are the integral powers of 2, we want to use an exponential function sending
integers to integral powers of 2. The nicest such function is x 7→2x.)
f is well-deﬁned. If y = x in R/Z then y = x + k for some k ∈Z, so
2y = 2x+k = 2x2k ∈2x2Z =⇒2y = 2x in R>0/2Z.
f is a homomorphism. For x and x′ in R/Z,
f(x)f(x′) = 2x 2x′ = 2x2x′ = 2x+x′ = f(x + x′),
so f is a homomorphism.
f is injective. Since f is a homomorphism, it suﬃces to check ker f is trivial. If f(x) = 1 then
2x = 1 in R>0/2Z, so 2x ∈2Z. Thus 2x = 2k for some k ∈Z, so x = k. In R/Z, x = k = 0 since k
is an integer.
f is surjective. Each element of R>0/2Z has the form t for some t > 0. Every positive real
number is a power of 2: t = 2x some x ∈R, so t = 2x = f(x).
□
Remark 5.2. By similar arguments, the group S1 is isomorphic to R/aZ for each nonzero real
number a and to R>0/bZ for each positive number b ̸= 1.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*