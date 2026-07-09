# Groups of Order p^2

> **Source**: https://kconrad.math.uconn.edu/blurbs/groupsp2.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
GROUPS OF ORDER p2
KEITH CONRAD
For each prime p there is one group of order p up to isomorphism, namely the cyclic group
Z/(p). For groups of order p2 there are at least two possibilities: Z/(p2) and Z/(p)×Z/(p).
These are not isomorphic since the ﬁrst group is cyclic and the second is not (every non-
identity element in it has order p). We will show that every group of order p2 is isomorphic
to one of those two groups. This result is due to Netto [3, pp. 148–149].1 and we will largely
follow Netto’s proof, which doesn’t involve anything other than careful work with products,
conjugates, and orders of elements. The key point is to show ﬁrst that all groups of order
p2 are abelian. Then we’ll use this to classify the possible groups that have oder p2. At the
end, we’ll revisit Netto’s argument to see how it can be simpliﬁed using cosets.
Theorem 1. For prime p, every group of order p2 is abelian.
Proof. Let G be a group of order p2. If G is cyclic then it is abelian, so we can suppose G
is not cyclic. Pick x ∈G −{e}, and since G ̸= ⟨x⟩(otherwise G would be cyclic) we can
pick y ∈G −⟨x⟩. Since the order of each element of G divides p2 and no element of G
has order p2, each non-identity element of G must have order p. Thus x and y each have
order p. Since ⟨x⟩and ⟨y⟩are subgroups of G with prime order p and they are diﬀerent
subgroups (the ﬁrst does not contain y and the second does), their intersection is trivial:
⟨x⟩∩⟨y⟩= {e}.
In the list of products {xiyj : 0 ≤i, j ≤p −1} we will show there are no duplicates. If
xiyj = xi′yj′ then x−i′+i = yj′−j, which belongs to ⟨x⟩∩⟨y⟩, so x−i′+i = e and yj′−j =
e.
Since x and y have order p, i′ ≡i mod p and j′ ≡j mod p.
The exponents are in
{0, 1, . . . , p −1}, so being congruent mod p forces equality: i′ = i and j′ = j. Thus the
number of diﬀerent elements of G in {xiyj : 0 ≤i, j ≤p −1} is p2, which matches |G|, so
G = {xiyj : 0 ≤i, j ≤p −1}.
Now consider the product yx. It has to be some xi1yj1. Similarly, y2x, . . . , yp−1x all have
a similar form:
yx = xi1yi1,
y2x = xi2yi2,
. . . ,
yp−1x = xip−1yip−1,
where 0 ≤ik, jk ≤p −1. Each ik is not 0, since otherwise ykx = yik, so x = yik−k ∈⟨y⟩,
but ⟨x⟩and ⟨y⟩intersect trivially.
Claim: there are m, n ̸≡0 mod p such that xymx−1 = yn.
Case 1: Two of the products among yx, y2x, . . . , yp−1x have the same power of x when
written as xiyj.
This implies there are k ̸= k′ in {1, . . . , p −1} such that ykx = xiyjk and yk′x = xiyjk′
for a common i. Then jk ̸= jk′ in {0, . . . , p −1} (otherwise ykx = yk′x, so k ≡k′ mod p,
but k and k′ are distinct in {1, . . . , p −1}). Solving for xi in both equations, we get
ykxy−jk = xi = yk′xy−jk′,
1The special case p = 2 was treated earlier by Cayley [2, pp. 43-44].
1

<!-- page 2 -->
2
KEITH CONRAD
so yk−k′x = xyjk−jk′, or equivalently xyjk−jk′x−1 = yk−k′. The exponents on y on both
sides are nonzero mod p since each is a diﬀerence of unequal numbers in {0, . . . , p −1}.
Case 2: All of the products among yx, y2x, . . . , yp−1x have diﬀerent powers of x when
written as xiyj.
This means one of these p terms has i = 1: ykx = xyj for some k in {1, . . . , p −1} and
some j. Rewrite that equation as xyjx−1 = yk. We have j ̸≡0 mod p, since otherwise
yk = xex−1 = e, but that is not true since y has order p and k is not divisible by p.
From the claim, raise both sides of xymx−1 = yn to the ℓ-th power for ℓ∈Z, getting
(xymx−1)ℓ= ynℓ, so xymℓx−1 = ynℓ. Use for ℓa multiplicative inverse of m mod p (this can
be done since p is prime and m ̸≡0 mod p), so ymℓ= y1 = y and thus xyx−1 = yN where
N = nℓ. In words, this says the conjugate of y by x is yN. Let’s conjugate y by x2:
x2yx−2 = x(xyx−1)x−1 = xyNx−1 = (xyx−1)N = (yN)N = yN2.
By similar reasoning and induction, xryx−r = yNr for all r ≥1. Taking r = p, so xr = e,
we get y = yNp. Since y has order p, the exponents are congruent mod p: 1 ≡Np mod p.
By Fermat’s little theorem we have Np ≡N mod p, so 1 ≡N mod p, and that means
yN = y1 = y, so xyx−1 = yN = y, or equivalently xy = yx: x and y commute.
Since every element of G has the form xiyj and x and y commute, all powers of x commute
with all powers of y and thus all elements of G commute with each other:
(1)
(xiyj)(xi′yj′) = xi(yjxi′)yj′ = xi(xi′yj)yj′ = (xixi′)(yjyj′) = xi+i′yj+j′.
This last expression is unchanged if we swap i with i′ and j with j′, so xiyj and xi′yj′
commute.
□
Remark 2. This theorem can be proved in a shorter way by using a further result in group
theory called the class equation, and usually Theorem 1 is proved in textbooks by the class
equation: see [1, Prop. 7.3.3] and [4, Cor. 2.76] for two such approaches. A purpose in
presenting the longer proof here is to see how the result was originally proved.
Theorem 3. For prime p, there are two groups of order p2 up to isomorphism: Z/(p2) and
Z/(p) × Z/(p).
Proof. All cyclic groups of the same order are isomorphic, so it suﬃces to show every
noncyclic group G of order p2 is isomorphic to Z/(p) × Z/(p).
By Theorem 1, G is abelian and contains elements x and y of order p such that every
element of G has a unique representation as xiyj where i, j ∈{0, . . . , p−1}. The exponents
in xiyj only matter mod p since x and y have order p, so we can deﬁne f : Z/(p)×Z/(p) →G
by f(i mod p, j mod p) = xiyj. By the unique representation of elements of G in the form
xiyj, f is a bijection. Since x and y commute, f is a homomorphism by (1):
f(i mod p, j mod p)f(i′ mod p, j′ mod p) = (xiyj)(xi′yj′) = xi+i′yj+j′,
which is f(i + i′ mod p, j + j′ mod p). A bijective homomorphism is an isomorphism: G ∼=
Z/(p) × Z/(p).
□
In the proof of Theorem 1, an overarching logic to the succession of steps may be hard
to make out. We will “modernize” the claim in that proof saying xymx−1 = yn for some
integers m and n that are nonzero mod p by using cosets.
Set H = ⟨y⟩. Since ⟨x⟩and ⟨y⟩intersect trivially, no power of x is in H except for
the identity, so the left H-cosets H, xH, x2H, . . . , xp−1H are mutually disjoint (they have
diﬀerent powers of x as representatives).

<!-- page 3 -->
GROUPS OF ORDER p2
3
The right H-coset Hx is disjoint from H (x is not in H and diﬀerent right H-cosets are
disjoint), so Hx ⊂Sp−1
i=1 xiH. Since Hx has size p and the union contains p −1 cosets xiH,
at least two elements from Hx have to lie in a common xiH.2 Write this as yjx ∈xiH and
ykx ∈xiH where j and k are diﬀerent integers in {0, . . . , p −1}. Thus
yjx = xiyj′,
ykx = xiyk′,
so j′ ̸≡k′ mod p (why?) and that implies
yjxy−j′ = xi = ykxy−k′ =⇒yj−kx = xyj′−k′ =⇒xyj′−k′x−1 = yj−k.
Since j and k are incongruent mod p, as are j′ and k′, we get xymx−1 = yn where m =
j′ −k′ ̸≡0 mod p and n = j −k ̸≡0 mod p, and this completes the proof of the claim in
the proof of Theorem 1.
References
[1] M. Artin, Algebra, 2nd ed., Prentice Hall, New York, 2011.
[2] A. Cayley, “On the Theory of Groups, as Depending on the Symbolic Equation θn = 1,” Philos. Mag.
7 (1854), 40–47. Also pp. 123–130 of The Collected Papers of Arthur Cayley, Vol. II, Cambridge Univ.
Press, 1889.
[3] E. Netto, The Theory of Substitutions and its Applications to Algebra, Register Publ. Co., Ann Arbor,
1892. URL https://archive.org/details/theoryofsubstitu00nett/page/148.
[4] J. Rotman, A First Course in Abstract Algebra, 2nd ed., Prentice Hall, Upper Saddle River, NJ, 2000.
2This is closely related to the pigeonhole principle: a function from an a-element set to a b-element set
where a > b must send at least two elements to the same value.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*