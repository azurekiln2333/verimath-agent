# The Artin-Schreier Theorem

> **Source**: https://kconrad.math.uconn.edu/blurbs/artinschreier.pdf  
> **Author**: Keith Conrad  
> **Topic**: galois_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE ARTIN–SCHREIER THEOREM
KEITH CONRAD
1. Introduction
The algebraic closure of R is C, which is a ﬁnite extension. Are there other ﬁelds that
are not algebraically closed but have an algebraic closure that is a ﬁnite extension? Yes.
An example is the ﬁeld of real algebraic numbers. Since complex conjugation is a ﬁeld
automorphism ﬁxing Q, and the real and imaginary parts of a complex number can be
computed using ﬁeld operations and complex conjugation, a complex number a + bi is
algebraic over Q if and only if a and b are algebraic over Q (meaning a and b are real
algebraic numbers), so the algebraic closure of the real algebraic numbers is obtained by
adjoining i. This example is not too diﬀerent from R, in an algebraic sense. Is there an
example that does not look like the reals, such as a ﬁeld of positive characteristic or a ﬁeld
whose algebraic closure is a ﬁnite extension of degree greater than 2?
Amazingly, it turns out that if a ﬁeld F is not algebraically closed but its algebraic closure
C is a ﬁnite extension, then in a sense that is made precise below as Theorem 3.1, F looks
like the real numbers. For example, F must have characteristic 0 and C = F(i). This is
a theorem of Artin and Schreier. Proofs of the Artin–Schreier theorem can be found in [5,
Theorem 11.14] and [6, Corollary 9.3, Chapter VI], although in both cases the theorem is
proved only after the development of some general theory that is useful for more than just
the Artin–Schreier theorem. In [7] there is an elementary proof (based on the original one,
as all known proofs are) under the hypothesis that F has characteristic 0; we essentially
reproduce much of that proof below, but we add on some extra details to prove in an
elementary manner that F must have characteristic 0.
The prerequisites are a knowledge of basic ﬁeld theory and Galois theory of ﬁnite ex-
tensions, including Kummer extensions and Artin–Schreier extensions. Applications of the
Artin–Schreier theorem to the Galois theory of inﬁnite extensions will be mentioned after
the proof.
2. Some lemmas
Our proof of the Artin–Schreier theorem requires two lemmas.
Lemma 2.1. Let F be a ﬁeld of characteristic ℓ> 0 and a ∈F. If a ̸∈F ℓ, then Xℓm −a
is irreducible in F[X] for every m ≥1.
Proof. We will prove the contrapositive: if Xℓm −a is reducible in F[X] for some m ≥1,
then a ∈F ℓ.
Let Xℓm −a = f(X)g(X), where f, g are monic in F[X] with positive degree. Let E be
an extension ﬁeld of F containing a root b of Xℓm −a, so in E[X]
Xℓm −a = Xℓm −bℓm = (X −b)ℓm.
1

<!-- page 2 -->
2
KEITH CONRAD
Since E[X] has unique factorization and f and g are monic, f(X) = (X −b)r where
0 < r < ℓm. Let r = ℓts with s not divisible by ℓ(clearly t < m). Then
f(X) = (Xℓt −bℓt)s,
so the coeﬃcient of Xℓt(s−1) is −sbℓt. This lies in F, so (since s is nonzero in F) bℓt ∈F.
Thus
a = (bℓt)ℓm−t ∈F ℓm−t ⊂F ℓ.
□
Remark 2.2. For a prime number ℓand a ﬁeld of arbitrary characteristic, the irreducibility
of Xℓ−a over that ﬁeld implies irreducibility of Xℓm −a for all m ≥1 except when ℓ= 2:
X2+4 is irreducible in Q[X] but X4+4 = (X2+2X +2)(X2−2X +2). See [6, pp. 297–298]
for more information about this.
Over a ﬁeld of characteristic ℓ, the polynomial Xℓ−X −a is a common replacement for
Xℓ−a when doing Galois theory, so it’s natural to ask about an analogue of Lemma 2.1 for
this polynomial: does irreducibility of Xℓ−X −a in characteristic ℓimply irreducibility of
(Xℓ−X)◦m −a for all m ≥1, where ◦m means “m iterates”? (For comparison, Xℓm −a =
(Xℓ)◦m −a.) The answer is no. For example, (X2 −X)◦3 −1 is reducible over F2 and
(X3 −X)◦2 −1 is reducible over F3. An interesting question about degrees of irreducible
factors of (Xp −X)◦m −1 over Fp is in https://mathoverflow.net/questions/167613.
Lemma 2.3. Let F be a ﬁeld in which −1 is not a square (so F does not have characteristic
2), and every element of F(i) is a square in F(i), where i2 = −1. Then every ﬁnite sum of
squares in F is again a square in F and F has characteristic 0.
Proof. Without loss of generality we deal with two squares. Let a, b ∈F. There are c, d ∈F
such that a + bi = (c + di)2. Thus a = c2 −d2 and b = 2cd, so a2 + b2 = (c2 + d2)2.
If F has positive characteristic, then −1 is a ﬁnite sum of 1’s in F (why?). Obviously 1
is a square in F, so therefore the sum, −1, is a square in F, a contradiction. So F must
have characteristic 0!
□
3. Statement and proof
Theorem 3.1 (Artin–Schreier). Let C be algebraically closed with F a subﬁeld such that
1 < [C : F] < ∞. Then C = F(i) where i2 = −1, and F has characteristic 0. Moreover, for
a ∈F ×, exactly one of a or −a is a square in F, and every ﬁnite sum of nonzero squares
in F is again a nonzero square in F.1
Proof. First we show C/F is Galois. Since C is algebraically closed, C/F is clearly normal.
To show that C/F is separable (hence Galois), assume F has characteristic ℓ> 0. We will
show that F = F ℓ, which implies F is a perfect ﬁeld and therefore the ﬁnite extension C/F
is separable. Well, if there is some a in F that is not in F ℓthen Lemma 2.1 implies Xℓm −a
is irreducible in F[X] for all m ≥1. Thus F has algebraic extensions of arbitrarily large
degree, a contradiction.
Now we prove [C : F] = 2. Let G = Gal(C/F), so [C : F] = |G|. If |G| > 2, then |G|
is divisible by an odd prime or 4, hence G has a subgroup whose size is an odd prime or 4
(a ﬁnite group has a subgroup of size equal to each prime power factor of the size of the
group), so C has a subﬁeld K containing F such that [C : K] equals an odd prime or 4.
1We exclude the empty sum, which is 0.

<!-- page 3 -->
THE ARTIN–SCHREIER THEOREM
3
Using K in place of F, to show [C : F] = 2 it suﬃces to prove [C : F] can’t be an odd
prime or 4.
Assume [C : F] = p, a prime, so G = Gal(C/F) is cyclic. Let σ be a generator of G, so
for x ∈C, x ∈F if and only if σ(x) = x. We want to show p = 2.
First we show F (equivalently, C) does not have characteristic p. Assume the contrary,
i.e., F has characteristic p. Since C/F is cyclic of degree p in characteristic p, Artin–Schreier
theory tells us that C = F(α) where α is a root of some polynomial Xp −X −a ∈F[X].
Since {1, α, . . . , αp−1} is an F-basis of C, we can write each b in C as
b = b0 + b1α + · · · + bp−1αp−1,
with the bj in F. Then
bp −b =
p−1
X
j=0
(bjαj)p −
p−1
X
j=0
bjαj
=
p−1
X
j=0
(bp
jαpj −bjαj)
=
p−1
X
j=0
bp
j(α + a)j −bjαj
= ((bp−1)p −bp−1)αp−1 + lower degree terms in α.
Since C is algebraically closed, we can choose b ∈C such that bp −b = aαp−1, so comparing
the coeﬃcient of αp−1 on both sides tells us that bp−1 ∈F is a root of Xp −X −a.
However, Xp −X −a is irreducible in F[X] (it’s the minimal polynomial of α), so we have
a contradiction. Thus F does not have characteristic p = [C : F].
Therefore, since C is algebraically closed of characteristic diﬀerent from p, C contains a
root of unity of order p; call it ζ. Since [F(ζ) : F] ≤p −1 and [C : F] = p, we must have
[F(ζ) : F] = 1, so ζ ∈F. That means C/F is cyclic of degree p with F containing a root
of unity of order p, so by Kummer theory C = F(γ) where γp ∈F.
We use γ to show p = 2. Choose β ∈C such that βp = γ, so βp2 = γp ∈F. Thus
βp2 = σ(βp2) = (σ(β))p2, hence σ(β) = ωβ with ωp2 = 1. Thus ωp is a p-th root of unity
(possibly 1; we’ll see that it is not 1 next), so ωp lies in F. If ωp = 1 then (σ(β))p = βp, so
σ(βp) = βp. That forces βp ∈F, but βp = γ and γ is not in F, so we have a contradiction.
Thus ωp ̸= 1, so ω has order p2 and ωp has order p. Since ωp = σ(ωp) = (σ(ω))p, we have
for some k ∈Z
σ(ω) = ω(ωp)k = ω1+pk.
From the equation σ(β) = ωβ, we get
β = σp(β) = ωσ(ω) · · · σp−1(ω)β = ω1+(1+pk)+···+(1+pk)p−1β,

<!-- page 4 -->
4
KEITH CONRAD
so we get the sequence of congruences
1 + (1 + pk) + · · · + (1 + pk)p−1 ≡0 mod p2,
p−1
X
j=0
(1 + jpk) ≡0 mod p2,
p + p(p −1)
2
· pk ≡0 mod p2,
1 + p(p −1)
2
· k ≡0 mod p.
This last congruence shows p is not odd, so p = 2 and k is odd. Therefore ω has order
p2 = 4 and σ(ω) = ω1+pk = ω1+2k = ω3, so σ(ω) ̸= ω. Since ω has order 4, ω2 = −1, so we
write ω as i. Thus if [C : F] is a prime, then it equals 2, C doesn’t have characteristic 2,
and i /∈F.
If [C : F] = 4 then Gal(C/F) has size 4, hence a subgroup of size 2, so there is an
intermediate ﬁeld F ⊂K ⊂C with [C : K] = 2. The above reasoning implies i is not in K,
hence not in F. But then F(i) is a subﬁeld of C with [C : F(i)] = 2 and F(i) contains i, a
contradiction.
Hence if F is a nonalgebraically closed ﬁeld whose algebraic closure C is a ﬁnite extension,
then [C : F] is not divisible by an odd prime or 4, so [C : F] = 2, F does not have
characteristic 2, and i is not in F. Thus C = F(i).
From C = F(i) and C ̸= F, Lemma 2.3 shows that the squares in F are closed under
addition and F has characteristic 0. To establish the last part of the theorem, assume a and
−a are both not squares in F. Then √a and √−a each generate the quadratic extension
C/F. From C = F(√a) = F(√−a), the ratio −a/a = −1 must be a square in F, but i ̸∈F
so we have a contradiction. Thus one of a or −a is a square in F, but not both since i is
not in F. If n ≥2 and b1, . . . , bn are nonzero in F, then by Lemma 2.3 the sum b2
1 +· · ·+b2
n
is a square in F. If it is zero, then −1 = (b2/b1)2 + · · · + (bn/b1)2 is a sum of squares in F,
hence −1 is a square in F, a contradiction. So b2
1 + · · · + b2
n is a nonzero square in F.
□
Corollary 3.2. If K is a subﬁeld of R such that [R : K] < ∞, then K = R.
Proof. Let n = [R : K]. Then [C : K] = 2n. By Theorem 3.1, [C : K] = 2, so n = 1.
□
In the Artin–Schreier theorem, deﬁne a “positive” element of F to be a nonzero square.
For every nonzero a ∈F, exactly one of a or −a is positive, each ﬁnite sum of positive
elements is positive, and positive elements are clearly closed under multiplication. So F
admits a notion of ordering (deﬁne a < b in F if b −a is a nonzero square), much like the
real numbers, where the positive elements are the nonzero squares.
Comparing the proof of the Artin–Schreier theorem above with accounts of it in books,
the only new twist here (which surely is not really new, but it wasn’t in the books that I
checked) is the method of showing F has characteristic 0. The proofs in [5] and [6] follow the
original proof of Artin and Schreier on this issue by studying certain cyclotomic extensions
of the prime ﬁeld, Q or Fp, to rule out the case of prime ﬁeld Fp. Artin and Schreier ﬁrst
proved their theorem in 1926 under the hypothesis that F has characteristic 0 [1, Satz 4].
They indicated in a footnote that the characteristic 0 hypothesis could be removed, and
they did so in a paper the following year [2, Satz 4].

<!-- page 5 -->
THE ARTIN–SCHREIER THEOREM
5
4. Applications
The Artin–Schreier theorem tells us something about automorphisms of ﬁnite order in
the (inﬁnite) group of ﬁeld automorphisms of the algebraic numbers. One element of ﬁnite
order is complex conjugation (restricted to the algebraic numbers), which has order 2. Let’s
show that every nonidentity automorphism of ﬁnite order has order 2.
It is no harder to deal with a more general situation, which we now do. Let K be a ﬁeld,
G be a ﬁnite group of automorphisms of K, and KG the ﬁxed ﬁeld of K under G. The main
theorem in Artin’s development of Galois theory says K/KG is a ﬁnite Galois extension
with Galois group G. In particular, if C is algebraically closed and G is a nontrivial ﬁnite
group of automorphisms of C, then [C : CG] = |G| > 1, so by the Artin–Schreier theorem
|G| = 2 and the ﬁxed ﬁeld CG “looks like” the real numbers.
Taking G to be the ﬁnite group generated by an element of ﬁnite order in Aut(C), we see
that the only nontrivial torsion in the automorphism group of an algebraically closed ﬁeld
is 2-torsion, and if there is 2-torsion then the ﬁeld has characteristic 0. Two noncommuting
torsion elements in Aut(C) have a product whose order is neither 1 nor 2 (this is just basic
group theory), hence this product must have inﬁnite order by the Artin–Schreier theorem.
So for a ﬁeld K, with algebraic closure K, the torsion elements of Aut(K/K) ⊂Aut(K)
have order 1 or 2 and a pair of noncommuting torsion elements have a product with inﬁnite
order. In particular, each nontrivial torsion element of the automorphism group of Q has
order 2, and if C is an algebraically closed ﬁeld of positive characteristic then Aut(C) is
torsion-free.
With some more work (see [3] or [4, Exercise 32, Chapter VI §2]), it can be shown that
Q is characterized up to ﬁeld isomorphism among all algebraically closed ﬁelds by the fact
that its automorphism group has nontrivial torsion elements and they are all conjugate (this
property is more important for number theory than it might appear at ﬁrst glance).
As a ﬁnal remark, note that we really don’t need C to be algebraically closed in the
Artin–Schreier theorem to conclude that C = F(i).
We only need that certain special
polynomials in C[X] have a root in C. More precisely, the properties we used of C were:
(1) If there is a subﬁeld F ⊂C such that 1 < [C : F] < ∞, then C/F is Galois.
(2) If p is prime and C has characteristic p, then Xp −X −a has a root in C for all a
in C. Note Xp −X −a has no multiple roots in characteristic p.
(3) If p is a prime and C does not have characteristic p, then C contains a root of unity
of order p.
Assuming [C : F] is prime, the fourth paragraph in the proof of the Artin–Schreier
theorem used properties 1 and 2 to show that char(F) = char(C) ̸= [C : F]. The rest of
the proof used property 3 to show that [C : F] = 2 and C = F(i).
This observation is important because C does not have to be algebraically closed to satisfy
properties 1, 2, and 3. For example, it suﬃces to assume only that C is separably closed, i.e.,
that C has no proper separable algebraic extensions. So if a ﬁeld S is a separable closure of
a ﬁeld F with 1 < [S : F] < ∞, the proof of the Artin–Schreier theorem with S in the role of
C yields char(S) ̸= 2 (so each element of S is a square in S since S is separably closed) and
S = F(i). Then Lemma 2.3 implies that char(S) = 0, so S is algebraically closed after all!
This leads to the following analogue of the Artin–Schreier theorem for separable closures.
Theorem 4.1. Let F be a ﬁeld whose separable closure is a ﬁnite proper extension (so its
algebraic closure is a priori possibly an inﬁnite extension). Then F has characteristic 0 and
its algebraic (= separable) closure is the quadratic extension F(i). Moreover, for a ∈F ×,

<!-- page 6 -->
6
KEITH CONRAD
exactly one of a or −a is a square in F, and every ﬁnite sum of nonzero squares in F is
again a nonzero square in F.
The last part of this theorem, about nonzero squares, follows from F(i) being algebraically
closed by the last paragraph of the proof of Theorem 3.1.
Separable closures are contained in algebraic closures, so does Theorem 4.1 imply Theo-
rem 3.1? Yes, with a little bit of extra work. Suppose F is a ﬁeld with algebraic closure C
and 1 < [C : F] < ∞.
Case 1: F is separably closed. Since F ̸= C, F is not a perfect ﬁeld (for perfect ﬁelds,
separable and algebraic closures match), so F has a positive characteristic ℓwith F ̸= F ℓ,
and then Lemma 2.1 tells us that there are irreducibles in F[X] of arbitrarily large degree,
so the algebraic closure of F is not a ﬁnite extension. This is a contradiction, so this case
doesn’t arise.
Case 2: F is not separably closed. The separable closure of F is a ﬁnite proper extension
of F. Calling it S, Theorem 4.1 tells us that S = F(i) and F has characteristic 0, which
implies C = S = F(i) and everything else we want in Theorem 3.1.
References
[1] E. Artin and O. Schreier, Algebraische Konstruktion reeller K¨orper, pp. 258–272 in: Artin’s Collected
Papers (Ed. S. Lang and J. Tate), Springer-Verlag, New York, 1965.
[2] E. Artin and O. Schreier, Eine Kennzeichnung der reell abgeschlossenen K¨orper, pp. 289–295 in: Artin’s
Collected Papers (Ed. S. Lang and J. Tate), Springer-Verlag, New York, 1965.
[3] R. Baer, Die Automorphismengruppe eines algebraisch abgeschlossen K¨orpers der Charakteristik 0, Math.
Zeit. 117, 1970, 7-17.
[4] N. Bourbaki, “Algebra II,” Springer-Verlag, New York, 1990.
[5] N. Jacobson, “Basic Algebra II,” 2nd ed., W. H. Freeman and Co., New York, 1989.
[6] S. Lang, “Algebra,” 3rd revised ed., Springer-Verlag, New York, 2002.
[7] R. Guralnick and M. Miller, Subﬁelds of Algebraically Closed Fields, Math. Mag. 50, 1977, 260-261.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*