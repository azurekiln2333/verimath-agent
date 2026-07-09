# Groups of Order p^3

> **Source**: https://kconrad.math.uconn.edu/blurbs/groupsp3.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
GROUPS OF ORDER p3
KEITH CONRAD
1. Introduction
For each prime p, we will describe all groups of order p3 up to isomorphism. This was done
for p = 2 by Cayley [3, 4] in 1859 and 1889 and Kempe [8, pp. 38–39, 45] in 1886, and for odd
p by Cole and Glover [5, pp. 196–201], H¨older [7, pp. 371–373] and Young [13, pp. 133–139]
independently in 1893. The groups were described by them using generators and relations,
which sometimes leads to unconvincing arguments that the groups constructed to be of
order p3 really have that order.1
From the cyclic decomposition of ﬁnite abelian groups, there are three abelian groups of
order p3 up to isomorphism: Z/(p3), Z/(p2) × Z/(p), and Z/(p) × Z/(p) × Z/(p).2 These
are nonisomorphic since they have diﬀerent maximal orders for their elements: p3, p2, and p
respectively. We will show there are two nonabelian groups of order p3 up to isomorphism.
That number is the same for all p, but the actual description of the two nonabelian groups
of order p3 will be diﬀerent for p = 2 and p ̸= 2, so we will treat these cases separately.
2. Groups of order 8
Theorem 2.1. A nonabelian group of order 8 is isomorphic to D4 or to Q8.
The groups D4 and Q8 are not isomorphic since there are 5 elements of order 2 in D4
and only one element of order 2 in Q8.
Proof. Let G be nonabelian of order 8. The nonidentity elements in G have order 2 or 4. If
g2 = 1 for all g ∈G then G is abelian, so some x ∈G must have order 4.
Let y ∈G −⟨x⟩. The subgroup ⟨x, y⟩properly contains ⟨x⟩, so ⟨x, y⟩= G. Since G is
nonabelian, x and y do not commute.
Since ⟨x⟩has index 2 in G, it is a normal subgroup. Therefore yxy−1 ∈⟨x⟩:
yxy−1 ∈{1, x, x2, x3}.
Since yxy−1 has order 4, yxy−1 = x or yxy−1 = x3 = x−1. The ﬁrst option is not possible,
since it says x and y commute, but they don’t. Therefore
yxy−1 = x−1.
The group G/⟨x⟩has order 2, so y2 ∈⟨x⟩:
y2 ∈{1, x, x2, x3}.
Since y has order 2 or 4, y2 has order 1 or 2. Thus y2 = 1 or y2 = x2.
1The page https://math.stackexchange.com/questions/1023341 gives a nonobvious description of the
trivial group by generators and relations.
2See https://kconrad.math.uconn.edu/blurbs/grouptheory/finite-abelian.pdf.
1

<!-- page 2 -->
2
KEITH CONRAD
Putting this together, G = ⟨x, y⟩where either
(2.1)
x4 = 1,
y2 = 1,
yxy−1 = x−1
or
(2.2)
x4 = 1,
y2 = x2,
yxy−1 = x−1.
The relations in (2.1) resemble D4, using x ↔r and y ↔s, while the relations in (2.2)
resemble Q8 using x ↔i and y ↔j. We will construct isomorphisms D4 →G in the ﬁrst
case and Q8 →G in the second case.3
First suppose (2.1) is true. Each element of D4 has the form rmsn for unique m ∈Z/(4)
and n ∈Z/(2). Set f : D4 →G by f(rmsn) = xmyn.
f is well-deﬁned.
The product rmsn determines m mod 4 and n mod 2, which makes
xmyn sensible since x4 = 1 and y2 = 1. Note f(r) = x and f(s) = y, which was suggested
by (2.1) originally. It remains to show f is a homomorphism and a bijection.
f is a homomorphism. For general elements g = rmsn and g′ = rm′sn′ in D4, we want
to show f(gg′) = f(g)f(g′). On the left side, gg′ = rmsnrm′sn′. To rewrite this as a power
of r times a power of s, from srs−1 = r−1 we have snrs−n = r(−1)n for n ∈Z/(2), so (raise
both sides to the m′-power) snrm′s−n = r(−1)nm′. Thus
(2.3)
gg′ = rmsnrm′sn′ = rmr(−1)nm′snsn′ = rm+(−1)nm′sn+n′,
so f(gg′) = xm+(−1)nm′yn+n′. Also
(2.4)
f(g)f(g′) = f(rmsn)f(rm′sn′) = xmynxm′xn′.
The rewriting of rmsnrm′sn′ in (2.3) was based only on the relations srs−1 = r−1 and
s2 = 1, so from the similar relations yxy−1 = x−1 and y2 = 1 in (2.1), the right side of (2.4)
is xm+(−1)nm′yn+n′, which is f(gg′). So f is a homomorphism.
f is a bijection. Since f is a homomorphism to G and its image includes x = f(r) and
y = f(s), the image of f contains ⟨x, y⟩, which is all of G. Thus f is onto. Since |D4| = |G|,
a surjection D4 →G is a bijection, so f is a bijection.
Now suppose (2.2) is true. We want to build an isomorphism Q8 →G mapping i to x
and j to y. Every element of Q8 looks like imjn where m, n ∈Z/(4). Set f : Q8 →G by
f(imjn) = xmyn.
f is well-deﬁned. A representation of an element of Q8 as imjn is not unique: if imjn =
im′jn′ then im−m′ = jn′−n, so m−m′ = 2a and n′−n = 2b where a ≡b mod 2 (why?). Then
xm−m′ = (x2)a = (y2)a = (y2)b = yn′−n by the ﬁrst two relations in (2.2), so xmyn = xm′yn′.
f is a homomorphism. Since jij−1 = i−1 and j2 commutes with i, check jnij−n = i(−1)n
for all n ∈Z/(4). This and the ﬁrst two relations in (2.2) imply f : Q8 →G is a homomor-
phism for reasons similar to the previous mapping D4 →G being a homomorphism.
f is a bijection. This follows for the same reasons as before, since the image of f includes
f(i) = x and f(j) = y and ⟨x, y⟩= G.
□
3We map from D4 or Q8 to G rather than in the other direction because D4 and Q8 are known groups,
so it is better to start there.

<!-- page 3 -->
GROUPS OF ORDER p3
3
3. The case of odd p
From now, p ̸= 2. We’ll show the two nonabelian groups of order p3, up to isomorphism,
are
Heis(Z/(p)) =





1
a
b
0
1
c
0
0
1

: a, b, c ∈Z/(p)



and
Gp =

a
b
0
1

: a, b ∈Z/(p2), a ≡1 mod p

=

1 + pm
b
0
1

: m, b ∈Z/(p2)

,
where m actually only matters modulo p.4 These two constructions both make sense at the
prime 2, but in that case the two groups are isomorphic to each other, as we’ll see below.
We can distinguish between Heis(Z/(p)) and Gp for p ̸= 2 by counting elements of order
p. In Heis(Z/(p)),
(3.1)


1
a
b
0
1
c
0
0
1


n
=


1
na
nb + n(n−1)
2
ac
0
1
nc
0
0
1


for n ∈Z, so


1
a
b
0
1
c
0
0
1


p
=


1
0
p(p−1)
2
ac
0
1
0
0
0
1

.
When p ̸= 2, p(p−1)
2
≡0 mod p, so all nonidentity elements of Heis(Z/(p)) have order p. On
the other hand, ( 1 1
0 1 ) in Gp has order p2 since ( 1 1
0 1 )n = ( 1 n
0 1 ). So Heis(Z/(p)) ̸∼= Gp.
At the prime 2, Heis(Z/(2)) and G2 each contain more than one element of order 2, so
Heis(Z/(2)) and G2 are both isomorphic to D4 (Theorem 2.1).
Let’s look at how matrices combine and decompose in Heis(Z/(p)) and Gp when p ̸= 2,
since this will inform some of our computations later when we classify the nonabelian grousp
of order p3. In Heis(Z/(p)),
(3.2)


1
a
b
0
1
c
0
0
1




1
a′
b′
0
1
c′
0
0
1

=


1
a + a′
b + b′ + ac′
0
1
c + c′
0
0
1


and in Gp
(3.3)

1 + pm
b
0
1
 
1 + pm′
b′
0
1

=

1 + p(m + m′)
b + b′ + pmb′
0
1

.
In Heis(Z/(p)),


1
a
b
0
1
c
0
0
1

=


1
0
0
0
1
c
0
0
1




1
a
0
0
1
0
0
0
1




1
0
b
0
1
0
0
0
1


=


1
0
0
0
1
1
0
0
1


c 

1
1
0
0
1
0
0
0
1


a 

1
0
1
0
1
0
0
0
1


b
by (3.1)
4The notation Gp for this group is not standard. I don’t know a standard “matrix group” notation for it.

<!-- page 4 -->
4
KEITH CONRAD
and a particular commutator is




1
1
0
0
1
0
0
0
1

,


1
0
0
0
1
1
0
0
1



=


1
0
1
0
1
0
0
0
1

.
So if we set
x =


1
1
0
0
1
0
0
0
1

and y =


1
0
0
0
1
1
0
0
1


then
(3.4)


1
a
b
0
1
c
0
0
1

= ycxa[x, y]b.
In Gp ⊂Aﬀ(Z/(p2)),

1 + pm
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
1 + pm
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
b 
1 + p
0
0
1
m
.
If we set
x =

1 + p
0
0
1

and y =

1
1
0
1

then

1 + pm
b
0
1

= ybxm
and
[x, y] =

1
p
0
1

= yp.
Lemma 3.1. In a group G, if g and h commute with [g, h] then [gm, hn] = [g, h]mn for all
m and n in Z, and gnhn = (gh)n[g, h](n
2).
Proof. Exercise.
□
Lemma 3.2. Let p be prime and G be a nonabelian group of order p3 with center Z. Then
|Z| = p, G/Z ∼= (Z/(p)) × (Z/(p)), and [G, G] = Z.
Proof. Since G is a nontrivial group of p-power order, its center is nontrivial. Therefore
|Z| = p, p2, or p3. Since G is nonabelian, |Z| ̸= p3. For a group G, if G/Z is cyclic then
G is abelian. So G being nonabelian forces G/Z to be noncyclic. Therefore |G/Z| ̸= p, so
|Z| ̸= p2. The only choice left is |Z| = p, so G/Z has order p2.
Up to isomorphism the only groups of order p2 are Z/(p2) and Z/(p)×Z/(p). Since G/Z
is noncyclic, G/Z ∼= Z/(p) × Z/(p).
Since G/Z is abelian, we have [G, G] ⊂Z. Because |Z| = p and [G, G] is nontrivial,
necessarily [G, G] = Z.
□
Remark 3.3. Although it won’t be necessary below, Lemma 3.2 implies for all primes p,
including p = 2, that a nonabelian group G of order p3 has p2 + p −1 conjugacy classes. To
start, G has p conjugacy classes of size 1 since those are the elements of the center Z and
|Z| = p. Next, if g ∈G−Z then its conjugacy class has order |G|/|Z(g)| = p3/|Z(g)|, where
Z(g) = {x ∈G : xg = gx} is the centralizer of g. Since Z(g) is a subgroup of G containing
Z and g and Z(g) ̸= G, |Z(g)| = p2. Thus |G|/|Z(g)| = p3/p2 = p, so all conjugacy classes

<!-- page 5 -->
GROUPS OF ORDER p3
5
of size greater than 1 have size p. Conjugate elements of G are equal in G/Z (since G/Z is
abelian) and each coset in G/Z has size p, so for each g ∈G −Z, its conjugacy class in G
must be the coset gZ.
Collecting the p3 −p noncentral elements of G into disjoint conjugacy classes each of
size p, the number of such conjugacy classes is (p3 −p)/p = p2 −1, so the total number of
conjugacy classes in G is p + (p2 −1) = p2 + p −1: p of size 1 and p2 −1 of size p.
Theorem 3.4. For p ̸= 2, a nonabelian group of order p3 is isomorphic to Heis(Z/(p)) or
Gp.
Proof. Let G be a nonabelian group of order p3. Each g ̸= 1 in G has order p or p2.
By Lemma 3.2, we can write G/Z = ⟨x, y⟩and Z = ⟨z⟩. For g ∈G, g ≡xiyj mod Z for
some integers i and j, so g = xiyjzk = zkxiyj for some k ∈Z. If x and y commute then
G is abelian (since zk commutes with x and y), which is a contradiction. Thus x and y do
not commute. Therefore [x, y] = xyx−1y−1 ∈Z is nontrivial, so Z = ⟨[x, y]⟩. Therefore we
can use [x, y] for z, showing G = ⟨x, y⟩.
Let’s see what the product of two elements of G looks like. Using Lemma 3.1,
(3.5)
xiyj = yjxi[x, y]ij,
yjxi = xiyj[x, y]−ij.
This shows we can move every power of y past every power of x on either side, at the cost
of introducing a (commuting) power of [x, y]. So every element of G = ⟨x, y⟩has the form
yjxi[x, y]k. (We write in this order because of (3.4).) A product of two such terms is
ycxa[x, y]b · yc′xa′[x, y]b′ = yc(xayc′)xa′[x, y]b+b′
= yc(yc′xa[x, y]ac′)xa′[x, y]b+b′
by (3.5)
= yc+c′xa+a′[x, y]b+b′+ac′.
Here the exponents are all integers.
Comparing this with (3.2), it appears we have a
homomorphism Heis(Z/(p)) →G by
(3.6)


1
a
b
0
1
c
0
0
1

7→ycxa[x, y]b.
After all, we just showed multiplication of such triples ycxa[x, y]b behaves like multiplication
in Heis(Z/(p)). But there is a catch: the matrix entries a, b, and c in Heis(Z/(p)) are integers
modulo p, so the “function” (3.6) from Heis(Z/(p)) to G is only well-deﬁned if x, y, and
[x, y] all have p-th power 1 (so exponents on them only matter mod p). Since [x, y] is in the
center of G, a subgroup of order p, its exponents only matter modulo p. But maybe x or y
could have order p2.
Well, if x and y both have order p, then there is no problem with (3.6). It is a well-deﬁned
function Heis(Z/(p)) →G that is a homomorphism. Since its image contains x and y, the
image contains ⟨x, y⟩= G, so the function is onto. Both Heis(Z/(p)) and G have order p3,
so our surjective homomorphism is an isomorphism: G ∼= Heis(Z/(p)).
What happens if x or y has order p2? In this case we anticipate that G ∼= Gp. In Gp,
two generators are g = ( 1+p 0
0
1 ) and h = ( 1 1
0 1 ), where g has order p, h has order p2, and
[g, h] = hp. We want to show our abstract G also has a pair of generators like this.
Starting with G = ⟨x, y⟩where x or y has order p2, without loss of generality let y have
order p2.
It may or may not be the case that x has order p.
To show we can change
generators to make x have order p, we will look at the p-th power function on G. For all

<!-- page 6 -->
6
KEITH CONRAD
g ∈G, gp ∈Z since G/Z ∼= Z/(p) × Z/(p). Moreover, the p-th power function on G is a
homomorphism: by Lemma 3.1, (gh)p = gphp[g, h]p(p−1)/2 and [g, h]p = 1 since [G, G] = Z
has order p, so
(gh)p = gphp.
Since yp has order p and yp ∈Z, Z = ⟨yp⟩. Therefore xp = (yp)r for some r ∈Z, and since
the p-th power function on G is a homomorphism we get (xy−r)p = 1, with xy−r ̸= 1 since
x ̸∈⟨y⟩. So xy−r has order p and G = ⟨x, y⟩= ⟨xy−r, y⟩. We now rename xy−r as x, so
G = ⟨x, y⟩where x has order p and y has order p2.
We are not guaranteed that [x, y] = yp, which is one of the relations for the two generators
of Gp. How can we force this relation to occur? Well, since [x, y] is a nontrivial element of
[G, G] = Z, Z = ⟨[x, y]⟩= ⟨yp⟩, so
(3.7)
[x, y] = (yp)k,
where k ̸≡0 mod p. Let ℓbe a multiplicative inverse for k mod p and raise both sides of
(3.7) to the ℓth power: using Lemma 3.1,
[x, y]ℓ= (ypk)ℓ=⇒[xℓ, y] = yp.
Since ℓ̸≡0 mod p, ⟨x⟩= ⟨xℓ⟩, so we can rename xℓas x: now G = ⟨x, y⟩where x has order
p, y has order p2, and [x, y] = yp.
Because [x, y] commutes with x and y and G = ⟨x, y⟩, every element of G has the form
yjxi[x, y]k = [x, y]kyjxi = ypk+jxi. Let’s see how such products multiply:
ybxm · yb′xm′ = yb(xmyb′)xm′
= yb(yb′xm[x, y]mb′)xm′
= yb+b′xm(yp)mb′xm′
= yb+b′+pmb′xm+m′.
Comparing this with (3.3), we have a homomorphism Gp →G by

1 + pm
b
0
1

7→ybxm.
(This function is well-deﬁned since on the left side m matters mod p and b matters mod p2
while xp = 1 and yp2 = 1.) This homomorphism is onto since x and y are in the image, so
it is an isomorphism since Gp and G have equal order: G ∼= Gp.
□
4. Nonisomorphic groups with the same subgroup lattice
When p = 2, the ﬁve groups of order 8 have diﬀerent subgroup lattices. This is almost
entirely explained by counting subgroups of order 2 (equivalently, counting elements of order
2): 1 for Z/(8), 3 for Z/(2)×Z/(4), 7 for (Z/(2))3, 5 for D4, and 1 for Q8. While the count
is the same for Z/(8) and Q8, these groups have diﬀerent numbers of subgroups of order 4:
1 for Z/(8) and 3 for Q8.
For p ̸= 2, we’ll show the subgroup lattices of Gp and Z/(p) × Z/(p2) are the same.
Theorem 4.1. For odd prime p, both Gp and Z/(p)×Z/(p2) have the same subgroup lattice:
• p + 1 subgroups of order p and p + 1 subgroups of order p2,

<!-- page 7 -->
GROUPS OF ORDER p3
7
• a unique subgroup H0 of order p2 that contains all subgroups of order p,
• a unique subgroup K0 of order p that is contained in all subgroups of order p2,
• each subgroup of order p2 besides H0 contains K0 as its only subgroup of order p,
• each subgroup of order p besides K0 has H0 as the only subgroup of order p2 con-
taining it.
Figure 1 is the subgroup lattice for G3. It reﬂects all 5 properties of Theorem 4.1.
Figure 1. Subgroup lattice for G3.
Theorem 4.1 is false for p = 2: G2 ∼= D4 has 5 subgroups of order 2 and 3 subgroups of
order 4 while Z/(2) × Z/(4) has 3 subgroups of order 2 and 3 subgroups of order 4. All
nonisomorphic groups of order 8 have diﬀerent subgroup lattices.
Proof. Case 1: subgroups of Z/(p) × Z/(p2).
Elements of order 1 or p are (a, b) where
b ∈pZ/(p2), so there are p2 −1 elements of order p. Diﬀerent subgroups of order p intersect
trivially, so the number of subgroups of order p is (p2 −1)/(p −1) = p + 1.
The elements of order 1 or p ﬁll up the subgroup H0 := {(a, b) : b ∈pZ/(p2)}, which has
order p2 and is not cyclic. Since H0 contains all the subgroups of order p, other subgroups
of order p2 must have an element of order p2 and are therefore cyclic. Elements of order p2
are (a, b) where b ∈(Z/(p2))×, and the subgroup ⟨(a, b)⟩has a generator of the form (c, 1).
As c varies in Z/(p), the p subgroups ⟨(c, 1)⟩have order p2 and are distinct, so the number
of subgroups of order p2 is p + 1.
In each cyclic subgroup ⟨(c, 1)⟩of order p2, the subgroup of order p is K0 = ⟨p(c, 1)⟩=
⟨(p, 0)⟩, which is independent of c. So K0 is the only subgroup of order p in subgroups of
order p2 besides H0.
Case 2: subgroups of Gp. Check by induction that for integers n ≥0,

1 + pm
b
0
1
n
=

1 + npm
(n + n(n−1)
2
pm)b
0
1

Since p is odd, p(p −1)/2 is divisible by p, so

1 + pm
b
0
1
p
=

1
pb
0
1

.
Therefore ( 1+pm b
0
1 )p is trivial if and only if b ∈pZ/(p2). Writing b ≡pℓmod p2,

1 + pm
b
0
1

=

1 + pm
pℓ
0
1

=

1
pℓ
0
1
 
1 + pm
0
0
1

=

1
p
0
1
ℓ
1 + p
0
0
1
m

<!-- page 8 -->
8
KEITH CONRAD
for ℓ, m ∈Z/(p). So there are p2 −1 elements of order p.
Check ( 1 p
0 1 ) and ( 1+p 0
0
1 ) commute, so the elements of Gp with order p are the nontriv-
ial elements of the subgroup H0 := ⟨( 1 p
0 1 ), ( 1+p 0
0
1 )⟩, which has order p2 and is not cyclic.
A subgroup of Gp with order p2 besides H0 must have an element of order p2, so sub-
groups of order p2 besides H0 are cyclic. Elements of Gp with order p2 are ( 1+pm b
0
1 ) where
b ∈(Z/(p2))× and ⟨( 1+pm b
0
1 )⟩has a generator of the form ( 1+pc 1
0
1 ) for c ∈Z/(p). These
subgroups for diﬀerent c are distinct, so the number of subgroups of order p2 is p + 1. In
⟨( 1+pc 1
0
1 )⟩, the subgroup of order p is K0 = ⟨( 1+pc 1
0
1 )p⟩= ⟨( 1 p
0 1 )⟩, which is independent of
c. Therefore K0 is the only subgroup of Gp with order p that is contained in subgroups of
order p2 other than H0.
□
5. Counting p-groups beyond order p3
Let’s summarize what is known about the count of groups of small p-power order.
• There is one group of order p up to isomorphism.
• There are two groups of order p2 up to isomorphism: Z/(p2) and Z/(p) × Z/(p).
• There are ﬁve groups of order p3 up to isomorphism, but our explicit description of
them is not uniform in p since the case p = 2 used a separate treatment.
For groups of order p4, the count is no longer uniform in p: there are 14 groups of order 24
and 15 groups of order p4 for p ̸= 2. This is due to H¨older [7] and Young [13]. A recent
account of this result by Adler, Garlow, and Wheland is on the arXiv [1]. For groups of
order p5, the count depends on p mod 12 as shown in the table below. This is due to Miller
[9] for p = 2 and Bagnera [2] for p > 2. Tables listing groups of order 32 and 243 are
available at Tim Dokchitser’s site [6]. The ﬁrst count of groups of order p6 is due to Potron
[12], with a modern count being made by Newman, O’Brien, and Vaughan-Lee [10]. A
count of groups of order p7 is due to O’Brien and Vaughan-Lee [11].
p
2
3
1 mod 12
5 mod 12
7 mod 12
11 mod 12
Groups of order p5
51
67
2p + 71
2p + 67
2p + 69
2p + 65
References
[1] J. D. Adler, M. Garlow, and E. R. Wheland, “Groups of order p4 made less diﬃcult.” URL https://
arxiv.org/abs/1611.00461.
[2] G. Bagnera, “La composizione dei gruppi ﬁniti il cui grado `e la quinta potenza di un numero primo,”
Ann. Mat. Pura Appl. 1 (1898), 137–228.
[3] A. Cayley, “On the theory of groups, as depending on the symbolic equation θn = 1, Part III” Philos.
Mag. 18 (1859), 34–37. URL https://www.tandfonline.com/doi/abs/10.1080/14786445908642716.
[4] A. Cayley, “On the theory of groups,” Amer. J. Math. 11 (1889), 139–157. URL https://archive.org/
details/jstor-2369415.
[5] F. N. Cole and J. W. Glover, “On groups whose orders are products of three prime factors,” Amer. J.
Math. 15 (1893), 191–220. URL https://www.jstor.org/stable/2369839.
[6] T. Dokchitser, Group Names, https://people.maths.bris.ac.uk/∼matyd/GroupNames/.
[7] O. H¨older, “Die Gruppen der Ordnungen p3, pq2, pqr, p4,” Math. Ann. 43 (1893), 301–412. URL https:
//eudml.org/doc/157685.
[8] A. B. Kempe, “A memoir on the theory of mathematical form,” Phil. Trans. 177 (1886), 1–70. URL
https://royalsocietypublishing.org/doi/10.1098/rstl.1886.0002.
[9] G. A. Miller, “The regular substitution groups whose order is less than 48,” Quart. J. Math. 28 (1896),
232–284.

<!-- page 9 -->
GROUPS OF ORDER p3
9
[10] M. F. Newman, E. A. O’Brien, and M. R. Vaughan-Lee, “Groups and nilpotent Lie rings whose order
is the sixth power of a prime,” J. Algebra 278 (2004), 383–401.
[11] E. A. O’Brien and M. R. Vaughan-Lee, “The groups of order p7 for odd prime p,” J. Algebra 292 (2005),
243–258.
[12] M. Potron, “Sur quelques groupes d’ordre p6,” Ph.D. thesis, Gauthier-Villars, Paris, 1904.
[13] J. Young, “On the determination of the groups whose order is a power of a prime,” Amer. J. Math. 15
(1893), 124–178. URL https://www.jstor.org/stable/2369564.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*