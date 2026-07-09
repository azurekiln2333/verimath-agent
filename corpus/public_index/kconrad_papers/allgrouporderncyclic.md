# Allgrouporderncyclic

> **Source**: https://kconrad.math.uconn.edu/blurbs/allgrouporderncyclic.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
WHEN ARE ALL GROUPS OF ORDER n CYCLIC?
KEITH CONRAD
1. Introduction
For a prime number p, every group of order p is cyclic: each element in the group besides
the identity has order p by Lagrange’s theorem, so the group has a generator. In fact each
nonidentity element of the group is a generator.
There are also composite n for which all groups of order n are cyclic, although the proof
is not as simple as choosing an arbitrary nonidentity element and expecting it to be a
generator. The ﬁrst such n is 15: every group of order 15 is cyclic. Here is a proof by Jyrki
Lahtonen [6]. If G is a group with order 15 then each element of G has order 1, 3, 5, or
15. By the Sylow theorems, G has a unique subgroup of order 3 and a unique subgroup of
order 5, so it has 2 elements of order 3, 4 elements of order 5, and of course 1 element of
order 1. That leaves 15 −2 −4 −1 = 8 elements unaccounted for, so they must all have
order 15 and any of them is a generator of G. The same argument shows every group of
order 35 is cyclic, and more generally every group of order pq where p and q are distinct
primes with p ̸≡1 mod q and q ̸≡1 mod p is cyclic: the congruences imply there is one
p-Sylow subgroup and one q-Sylow subgroup, making the number of elements of order 1,
p, or q equal to 1 + (p −1) + (q −1) = p + q −1, so the number of remaining elements is
pq −(p + q −1) = (p −1)(q −1), which is positive. Each of these remaining elements must
have order pq and thus generates the group.
The general question we want to address is: for which positive integers n is every group
of order n cyclic? For each n there is a cyclic group of order n, and a group isomorphic
to a cyclic group is cyclic, so a more abstract way of posing our question is: for which n
are all groups of order n isomorphic? Whatever way the question is formulated, here is the
answer.
Theorem 1.1. For a positive integer n, all groups of order n are cyclic if and only if n is
squarefree and, for each pair of distinct primes p and q dividing n, q ̸≡1 mod p.
A positive integer n ﬁtting the conclusion of Theorem 1.1 is called a cyclic number. It
vacuously includes 1 and all primes. In Table 1 are the ﬁrst ﬁve cyclic n with 2, 3, and 4
prime factors. The ﬁrst 61 cyclic n are online at the OEIS: see https://oeis.org/A003277.
2 primes
3 primes
4 primes
15 = 3 · 5
255 = 3 · 5 · 17
5865 = 3 · 5 · 17 · 23
33 = 3 · 11
345 = 3 · 5 · 23
7395 = 3 · 5 · 17 · 29
35 = 5 · 7
435 = 3 · 5 · 29
7735 = 5 · 7 · 13 · 17
51 = 3 · 17
455 = 5 · 7 · 13
8645 = 5 · 7 · 13 · 19
65 = 5 · 13
561 = 3 · 11 · 17
10005 = 3 · 5 · 23 · 29
Table 1. Cyclic numbers with 2, 3, and 4 prime factors.
1

<!-- page 2 -->
2
KEITH CONRAD
From the formula for ϕ(n) in terms of the prime factorization of n, the criterion on n in
Theorem 1.1 is equivalent to saying
(n, ϕ(n)) = 1,
which is a convenient way to generate a long list of cyclic numbers using a computer algebra
system that knows the ϕ-function. Necessarily n is odd when n ≥3, since ϕ(n) is even.
Dickson [2, §6] determined in 1905 those n for which all groups of order n are abelian1,
from which Theorem 1.1 is a consequence. The earliest proof focusing speciﬁcally on n for
which all groups of order n are cyclic (not just abelian) was given by Szele [8] in 1947.
Proving Theorem 1.1 has two directions:
(1) (necessity) if all groups of order n are cyclic then n is squarefree and q ̸≡1 mod p
for all distinct primes p and q dividing n,
(2) (suﬃciency) if n is squarefree and q ̸≡1 mod p for all distinct primes p and q dividing
n then all groups of order n are cyclic.
We will prove necessity in Section 2 and prove suﬃciency in three ways in Sections 3, 4,
and 5. Other proofs of Theorem 1.1 can be found in the references.
2. Necessity of n being a cyclic number
Assume all groups of order n are cyclic. To prove n is squarefree and q ̸≡1 mod p for
all distinct primes p and q dividing n, we want to show for every other n that there is a
noncyclic group of order n. Those other n are either (i) not squarefree or (ii) have a pair
of prime factors p and q where q ≡1 mod p (so q > p). In the ﬁrst case we have p2 | n
for some prime p, and in the second case we have pq | n where p and q are primes with
q ≡1 mod p. The following two examples give us noncyclic groups of order p2 and pq.
Example 2.1. For each prime p, the group Z/(p) × Z/(p) is not cyclic since it has order
p2 while each element has order 1 or p.
Example 2.2. Let p and q be distinct primes with p < q and q ≡1 mod p. The group
Aﬀ(Z/(q)) =

x
y
0
1

: x ∈(Z/(q))×, y ∈Z/(q)

has order (q −1)q. Since p | (q −1), by Cauchy’s theorem (Z/(q))× contains a g with order
p. The matrices in Aﬀ(Z/(q)) with upper-left entry a power of g form a group of order pq:
(2.1)

a
b
0
1

: a ∈⟨g⟩, b ∈Z/(q)

.
This group is not cyclic since it is not abelian: ( 1 1
0 1 ) and ( g 0
0 1 ) are in (2.1) and do not
commute, as you can check.
With these examples we can prove that if all groups of order n are cyclic then n is a
cyclic number.
Proof. If p2 | n for some prime p then the group Z/(p) × Z/(p) × Z/(n/p2) has order n
and is not cyclic since it has the noncyclic subgroup Z/(p) × Z/(p). If n has distinct prime
factors p and q such that q ≡1 mod p then the direct product of (2.1) and Z/(n/pq) has
order n and is not cyclic since it has the nonabelian (hence noncyclic) subgroup (2.1).
□
1Dickson’s theorem is that for n > 1, all groups of order n are abelian if and only if the prime factorization
of n is pe1
1 · · · per
r
where each ei is 1 or 2 and for i = 1, . . . , r we have pei
i ̸≡1 mod pj for all j ̸= i.

<!-- page 3 -->
WHEN ARE ALL GROUPS OF ORDER n CYCLIC?
3
3. First proof of sufficiency of n being a cyclic number
We will now prove every group having order equal to a cyclic number is a cyclic group
using induction on cyclic numbers. The result is obvious for groups of order 1, so assume n
is a cyclic number with n > 1 and all groups having order equal to a cyclic number less than
n are cyclic groups. To prove all groups of order n are cyclic, suppose there is a group G of
order n that is not cyclic. Another way of describing G is as a minimal counterexample: if
there is a non-cyclic group whose order is a cyclic number then there is a non-cyclic group
of least order equal to a cyclic number, and G is such a group by the inductive hypothesis.
We will prove G has various properties until we reach a contradiction.
Since all subgroups and quotient groups of G have order dividing n and every factor of
a cyclic number is a cyclic number, by the inductive hypothesis all subgroups and quotient
groups of G with order less than n are cyclic groups. We will use this multiple times.
Lemma 3.1. The group G is not abelian.
Proof. Since |G| is squarefree, |G| = p1p2 · · · pr for distinct primes pi. By Cauchy’s theorem
some gi ∈G has order pi for 1 ≤i ≤r. Suppose G is abelian. Then the gi’s pairwise
commute and have pairwise relatively prime orders, the order of the product g1 · · · gr is the
product of the orders of the gi’s, so g1 · · · gr has order p1 · · · pr = |G|. Thus G is cyclic,
contradicting the deﬁning condition that G is not cyclic.
□
Next we strengthen Lemma 3.1 by showing G is very far from being abelian.
Lemma 3.2. The group G has a trivial center.
Proof. Let Z be the center of G, so Z ◁G. If Z ̸= {e} then |G/Z| is a cyclic number less
than |G|, so G/Z is cyclic. It is a standard result in group theory that if G/Z is cyclic then
G is abelian, so our group G is abelian. That contradicts Lemma 3.1, so Z = {e}.
□
For x ∈G, its centralizer is Z(x) = {g ∈G : gx = xg}. If x ̸= e then Z(x) ̸= G since the
center of G is trivial by Lemma 3.2. The rest of our argument will use centralizers a lot.
Lemma 3.3. For nontrivial x in G, if y ∈Z(x) and y ̸= e then Z(y) = Z(x).
Proof. Since Z(x) ̸= G, Z(x) is cyclic and thus abelian. Therefore if y ∈Z(x), all elements
of Z(x) commute with y, which makes Z(x) ⊂Z(y). Now x ∈Z(y) and y ̸= e, so by similar
reasoning Z(y) ⊂Z(x), so Z(x) = Z(y).
□
Lemma 3.4. For nontrivial x and x′ in G, if Z(x) ̸= Z(x′) then Z(x) ∩Z(x′) = {e}.
Proof. We prove the contrapositive. If Z(x) ∩Z(x′) ̸= {e}, let y be a non-identity element
of Z(x) ∩Z(x′). By Lemma 3.3, Z(y) = Z(x) and Z(y) = Z(x′), so Z(x) = Z(x′).
□
For a subgroup H of a ﬁnite group G, the number of subgroups of G that are conjugate
to H is |G|/|N(H)|, where N(H) = {g ∈G : gHg−1 = H} is the normalizer of H.
Lemma 3.5. If x ∈G has prime order then Z(x) = N(⟨x⟩) and the number of subgroups
of G conjugate to Z(x) is |G|/|Z(x)|.
Proof. Let p be the order of x. Since Z(x) is abelian we have ⟨x⟩◁Z(x), so Z(x) ⊂N(⟨x⟩).
To prove N(⟨x⟩) ⊂Z(x), we adapt the argument from [4, Lemma 1].
Let g ∈N(⟨x⟩), so
(3.1)
gxg−1 = xi,

<!-- page 4 -->
4
KEITH CONRAD
where i ̸≡0 mod p. For k ∈Z+ conjugate both sides of (3.1) k times by g to get
gkxg−k = xik.
In this equation set k = n = |G|, so x = xin and therefore in ≡1 mod p. This implies the
order of i mod p divides n. Also the order of i mod p divides p −1, a factor of ϕ(n). Since
n is a cyclic number, (n, ϕ(n)) = 1. Thus the order of i mod p is 1, so i ≡1 mod p and
feeding this back into (3.1) gives us gxg−1 = x, so g ∈Z(x).
The number of subgroups of G conjugate to Z(x) is |G|/|N(Z(x))|. Since |G| is squarefree,
⟨x⟩is a p-Sylow subgroup of G. Therefore N(Z(x)) = Z(x) because the normalizer of every
Sylow subgroup is its own normalizer. Thus |G|/|N(Z(x))| = |G|/|Z(x)|.
□
Now we are ready to show the minimal counterexample G leads to a contradiction.
Let p be a prime factor of |G| and x be an element of G with order p (Cauchy’s theorem).
Then Lemma 3.5 tells us Z(x) has |G|/|Z(x)| conjugate subgroups in G, including itself.
Since |Z(x)| < |G|, there is a prime q dividing |G|/|Z(x)| and q does not divide |Z(x)|
since |G| is squarefree. Let y ∈G have order q (Cauchy again), so |Z(y)| is divisible by q
while |Z(x)| is not divisible by q.
We will now look at the union of the subgroups of G conjugate to Z(x) or to Z(y):
(3.2)
[
g∈G
gZ(x)g−1 ∪
[
h∈G
hZ(y)h−1.
It will turn out that this subset of G has more than |G| elements, a clear contradiction.
Since gZ(x)g−1 = Z(gxg−1), Lemma 3.4 tells us that diﬀerent subgroups conjugate to
Z(x) intersect trivially. Similarly, diﬀerent subgroups conjugate to Z(y) intersect trivially.
How does a subgroup conjugate to Z(x) compare to a subgroup conjugate to Z(y)? They
can’t be equal since subgroups of the second kind have order divisible by q and subgroups
of the ﬁrst kind do not, so Lemma 3.4 implies subgroups conjugate to Z(x) and subgroups
conjugate to Z(y) intersect trivially.
We can now count the size of (3.2). Using Lemma 3.5 and counting the identity element
separately,

[
g∈G
gZ(x)g−1 ∪
[
h∈G
hZ(y)h−1

= 1 +
|G|
|Z(x)|(|Z(x)| −1) +
|G|
|Z(y)|(|Z(y)| −1)
= 1 + |G| −
|G|
|Z(x)| + |G| −
|G|
|Z(y)|
≥1 + |G| −|G|
2 + |G| −|G|
2
= 1 + |G|,
which is a contradiction and that completes our proof.
4. Second proof of sufficiency of n being a cyclic number
Most proofs I have read that show each group with order equal to a cyclic number is a
cyclic group ([1, pp. 9–11], [3], [4], and [5]) involve maximal subgroups, where a maximal
subgroup of a group is a proper subgroup contained in no other proper subgroup. (The
proofs in [7], [8], and [9] are based on ideas other than maximal subgroups, e.g., [7] uses
Burnside’s normal complement theorem.) In this section we will describe the approach via

<!-- page 5 -->
WHEN ARE ALL GROUPS OF ORDER n CYCLIC?
5
maximal subgroups, which is similar in many respects to the argument in Section 3, since
the subgroups Z(x) for x ̸= e in a minimal counterexample G turn out to be the maximal
subgroups of G. We will use Lemmas 3.1 and 3.2 from Section 3, but otherwise develop
what we need from scratch.
Here is the strategy. If G is a minimal counterexample then its proper subgroups are all
cyclic, so all maximal subgroups of G are cyclic. For a maximal subgroup M of a minimal
counterexample G we will show that the size of
[
g∈G
gMg−1
is over half the size of G but is not all of G. Then we’ll show there is a maximal subgroup
M′ not conjugate to M, and the union of its conjugate subgroups also ﬁll up over half of G
but not all of G. We’ll show the conjugate subgroups of M and M′ taken together pairwise
intersect trivially, so they have over |G| distinct elements and that is a contradiction.
In a group of prime order its trivial subgroup is maximal, and in a group of non-prime
order its trivial subgroup is not maximal since, for each element of prime order (they exist
by Cauchy’s theorem), the subgroup it generates is a proper subgroup containing the trivial
subgroup.
Lemma 4.1. If x is nontrivial in G then Z(x) is a maximal subgroup of G.
Proof. Since x ̸= e and G has a trivial center (Lemma 3.2), Z(x) is a proper subgroup of G.
To prove Z(x) is a maximal subgroup of G, suppose Z(x) ⊂H ⊂G for a proper subgroup
H. Since |H| < |G|, the subgroup H is cyclic, and hence abelian, so all of its elements
commute with each other. Thus y ∈H ⇒y ∈Z(x), so H ⊂Z(x). Thus H = Z(x).
□
Lemma 4.2. If M is a maximal subgroup of G then M ̸= {e} and M = Z(x) for each
nontrivial x in M.
This is like Lemma 3.3.
Proof. The subgroup M is nontrivial since |G| is not 1 or prime, and since M is cyclic its
elements all commute with each other. So for x in M we have M ⊂Z(x). By the deﬁnition
of maximal subgroups, M ⊂Z(x) ⊂G ⇒Z(x) = M or Z(x) = G. If Z(x) = G then
x ∈Z(G), and Z(G) is trivial by Lemma 3.2, so x ̸= e ⇒Z(x) = M.
□
Lemma 4.3. If M and M′ are diﬀerent maximal subgroups of G then M ∩M′ is trivial.
This is like Lemma 3.4.
Proof. We prove the contrapositive. If M ∩M′ is not trivial, let x be a non-identity element
of M ∩M′. By Lemma 4.2, M = Z(x) and M′ = Z(x), so M = M′.
□
Lemma 4.4. There are no normal subgroups in G other than {e} and G.
This is not like any lemma in Section 3, but it will substitute for the property N(P) = P
of Sylow subgroups that was used in Section 3.
Proof. Let N be a proper normal subgroup of G, so N is cyclic, say of order m. For each
g ∈G we have gNg−1 = N, so we can associate to each g ∈G the conjugation function
γg : N →N by γg(x) = gxg−1. Each γg is an automorphism of N (its inverse is γg−1), so
g 7→γg is a homomorphism G →Aut(N) ∼= (Z/(m))×.

<!-- page 6 -->
6
KEITH CONRAD
Let K be the kernel of that homomorphism, so G/K embeds into Aut(N). Thus |G/K|
divides ϕ(m), which divides ϕ(n) since m | n (look at the formula for the ϕ-function,
especially on squarefree numbers). Also |G/K| divides |G|, which is n. Since n and ϕ(n)
are relatively prime and |G/K| divides both, G/K is trivial. Thus G = K, which means
every element of G conjugates like the identity on the elements of N. Thus N ⊂Z(G), so
N is trivial by Lemma 3.2.
□
Pick x ̸= e in G and set M = Z(x), which is a maximal subgroup. Each gMg−1 has
order |M|. Also gMg−1 is a maximal subgroup of G, either by checking for all ﬁnite groups
that the conjugate of a maximal subgroup is a maximal subgroup, or by checking in our
special case that gMg−1 = gZ(x)g−1 = Z(gxg−1) and using Lemma 4.1. The number
of diﬀerent subgroups gMg−1 as g varies is |G|/|N(M)|, and conjugate subgroups of M
intersect trivially when they are distinct by Lemma 4.3, so by counting the identity element
separately,

[
g∈G
gMg−1

= 1 +
|G|
|N(M)|(|M| −1).
Since M ⊂N(M) ⊂G, N(M) is M or G by maximality of M. From M ̸= {e} (Lemma 4.2)
and M ̸= G, M is not normal in G (Lemma 4.4), so N(M) ̸= G. Thus N(M) = M,2 so

[
g∈G
gMg−1

= 1 + |G|
|M|(|M| −1) = 1 +

1 −
1
|M|

|G| ≥1 + |G|
2 .
That’s a lower bound. We also have an upper bound:

[
g∈G
gMg−1

= 1 +

1 −
1
|M|

|G| < 1 +

1 −1
|G|

|G| = |G|.
By this strict inequality, there is some x′ ∈G that is not in any conjugate subgroup of M.3
Set M′ = Z(x′). Since x′ ̸= e, by reasoning as above with conjugate subgroups of M′ in
place of M, we get

[
h∈G
hM′h−1
 ≥1 + |G|
2 .
Subgroups of G having the form gMg−1 or hM′h−1 are maximal. Such subgroups can’t
be equal, since otherwise M′ is conjugate to M but x′ ∈M′ and x′ is (by deﬁnition) in no
conjugate subgroup of M. Thus every gMg−1 and hM′h−1 intersect trivially (Lemma 4.3),
so by counting the identity element separately,

[
g∈G
gMg−1 ∪
[
h∈G
hM′h−1

= 1 +

[
g∈G
gMg−1

−1 +

[
h∈G
hM′h−1
 −1
≥1 + |G|
2 + |G|
2
= 1 + |G|,
which is a contradiction.
2The step analogous to this in Section 3 is that N(P) = P when P is a Sylow subgroup of G.
3In fact, for every ﬁnite group G and proper subgroup H, the union of all gHg−1 is not G.

<!-- page 7 -->
WHEN ARE ALL GROUPS OF ORDER n CYCLIC?
7
5. Third proof of sufficiency of n being a cyclic number
For our next proof that a group whose order is a cyclic number must be a cyclic group,
we will use a description of all groups with squarefree order.
Theorem 5.1. A group has squarefree order if and only if it is a semidirect product of cyclic
groups with relatively prime squarefree orders: it is isomorphic to some Z/(a)⋊Z/(b) where
a and b are relatively prime squarefree integers.
Proof. (⇐=) When a and b are relatively prime and squarefree, every semidirect product
of Z/(a) and Z/(b) is a group with squarefree order ab.
(=⇒) See Theorem 10.2 and the appendix in https://kconrad.math.uconn.edu/blurbs/
grouptheory/semidirect-product.pdf.
□
Let |G| = n where n is a cyclic number.
Since n is squarefree, by Theorem 5.1 we
have G ∼= Z/(a) ⋊f Z/(b) where (a, b) = 1 and f : Z/(b) →Aut(Z/(a)) = (Z/(a))× is a
homomorphism. Thus n = ab and ϕ(n) = ϕ(a)ϕ(b) due to a and b being relatively prime.
Since ϕ(a) | ϕ(n), b | n, and (n, ϕ(n)) = 1, we have (b, ϕ(a)) = 1. That means Z/(b) and
(Z/(a))× have relatively prime orders, so f : Z/(b) →(Z/(a))× is the trivial homomorphism.
Thus the semidirect product Z/(a) ⋊f Z/(b) is a direct product: G ∼= Z/(a) × Z/(b). Since
(a, b) = 1, we have Z/(a) × Z/(b) ∼= Z/(ab), so G is cyclic.
This proof that groups whose order is a cyclic number are cyclic groups looks much
shorter than those in the previous two sections, but that impression is deceiving since we
did not include a proof of (=⇒) in Theorem 5.1. Including that proof here would make the
overall proof in this section just as long as the previous proofs.
References
[1] L. Crew, On the characterization of the numbers n such that any group of order n has a given property
P, https://arxiv.org/pdf/1501.03170.pdf.
[2] L. E. Dickson, Deﬁnitions of a group and a ﬁeld by independent postulates, Trans. Amer. Math.
Soc. 6 (1905), 198–204. URL http://www.ams.org/journals/tran/1905-006-02/S0002-9947-1905-
1500706-2/S0002-9947-1905-1500706-2.pdf.
[3] J. Gallian and D. Moulton, When is Zn the only group of order n?, Elem. Math. 48 (1993), 117–119.
URL http://gdz.sub.uni-goettingen.de/dms/load/img/?PID=GDZPPN002083140.
[4] Y. Ge, All Groups of Order n are cyclic iﬀ. . ., https://yiminge.wordpress.com/2009/01/22/all-groups
-of-order-n-are-cyclic-iff/.
[5] D. Jungnickel, On the Uniqueness of the Cyclic Group of Order n, Amer. Math. Monthly 99 (1992),
545–547. URL https://www.jstor.org/stable/2324062.
[6] J. Lahtonen, answer at https://math.stackexchange.com/questions/67407/group-of-order-15-is-
abelian.
[7] Y. Shariﬁ, Groups of order n with gcd(n,phi(n))=1 are cyclic, https://ysharifi.wordpress.com/2010/
12/13/groups-of-order-n-with-gcdn-phin1-are-cyclic/.
[8] T. Szele, ¨Uber die endlichen Ordnungszahlen, zu denen nur eine Gruppe geh¨ort, Comm. Math. Helv. 20
(1947), 265–267. URL https://eudml.org/doc/138922.
[9] S. K. Upadhyay and S. D. Kumar, Existence of a Unique Group of Finite Order, The Mathematics
Student 81 (2012), 215–218.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*