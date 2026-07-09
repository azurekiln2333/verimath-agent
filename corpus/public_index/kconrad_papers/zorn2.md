# Zorn's Lemma II

> **Source**: https://kconrad.math.uconn.edu/blurbs/zorn2.pdf  
> **Author**: Keith Conrad  
> **Topic**: algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
ZORN’S LEMMA AND SOME APPLICATIONS, II
KEITH CONRAD
We will describe some applications of Zorn’s lemma to ﬁeld extensions, mostly involving
algebraically closed and real closed ﬁelds.
1. Zorn’s lemma and algebraic closures
An algebraic closure of a ﬁeld K is an ﬁeld extension of K that is both an algebraic
extension of K and is algebraically closed. That every ﬁeld K has an algebraic closure is
proved in [2, p. 544] by an iterative procedure starting with a polynomial ring over K in
a very large number of variables and a suitably chosen maximal ideal of this ring. Such
a maximal ideal exists by Zorn’s lemma.1 A proof of the existence of an algebraic closure
of K that uses Zorn’s lemma in a more direct fashion is in [3, pp. 259–260], which uses
ﬁeld structures on subsets of an inﬁnite set with a well-chosen cardinality.2 In Zorn’s paper
[12] where Zorn’s lemma was introduced, the ﬁrst application of it was to a proof of the
existence of algebraic closures.
We will use Zorn’s lemma here to prove all algebraic closures of a ﬁeld are isomorphic to
each other. The ﬁrst step in the proof, which is where Zorn’s lemma is used, is to extend a
ﬁeld homomorphism to a larger ﬁeld.
Theorem 1.1. Let L/K be an algebraic extension. Every ﬁeld homomorphism ϕ: K →C,
where C is an algebraically closed ﬁeld, can be extended to a homomorphism L →C.
We are not requiring C to be an algebraic closure of K: it might be, but also it could be
much larger. For example, K could be Q(
4√
2) and C could be C. Also, the extension of
ϕ: K →C to a homomorphism L →C is very far from being unique.
Proof. Let S be the set of pairs (F, f) where F is an intermediate ﬁeld between K and L
and f : F →C is a ﬁeld homomorphism such that f|K = ϕ. Since (K, ϕ) ∈S, S ̸= ∅.
L
/ C
F
f
8
K
ϕ
@
Partially order S by declaring (F, f) ≤(F ′, f′) if F ⊂F ′ and f′|F = f. For a totally
ordered subset {(Fα, fα)}α∈A in S, an upper bound can be produced as follows. Let F =
1A modiﬁcation of this proof is in https://kconrad.math.uconn.edu/blurbs/galoistheory/algclosure
shorter.pdf.
2We can’t use Zorn’s lemma on “the set of all algebraic extensions of K” to build an algebraic closure of
K as a maximal algebraic extension of K, despite the intuitive appeal of this idea, because the collection of
all algebraic extensions of K is not a set. Zorn’s lemma is a property of partially ordered sets.
1

<!-- page 2 -->
2
KEITH CONRAD
S
α∈A Fα. Since the Fα’s are totally ordered, it’s easy to check that F is a ﬁeld. Deﬁne
f : F →C by f(x) = fα(x) when x ∈Fα. If x is also in Fβ, we should check fα(x) = fβ(x)
so we know the deﬁnition of f(x) is independent of the choice of Fα containing x. Since our
subset of S is totally ordered, either (Fα, fα) ≤(Fβ, fβ) or (Fβ, fβ) ≤(Fα, fα). In the ﬁrst
case, fβ restricts to fα on Fα, so fβ(x) = fα(x). The argument in the second case is the
same. For x ∈K, we can view x in some Fα and then f(x) = fα(x) = ϕ(x) since fα|K = ϕ,
so f|K = ϕ. To prove f is a ﬁeld homomorphism, view two elements of F in a common Fα
(total ordering) and use the fact that fα is a ﬁeld homomorphism. Since f|Fα = fα, (F, f)
is an upper bound on all the (Fα, fα)’s.
Now we can apply Zorn’s lemma: S has a maximal element (F, σ). That is, F is a ﬁeld
between K and L with a homomorphism σ: F →C such that σ|K = ϕ and there is no
extension of σ to a homomorphism from a larger intermediate ﬁeld to C. We will prove
F = L, which means ϕ extends up to L.
If F ̸= L then there is some a ∈L with a ̸∈F. Then F(a)/F is a ﬁnite extension of
degree greater than 1. We’re going to extend σ to a homomorphism F(a) →C. Let g(X) be
the minimal polynomial for a in F[X], so there is an F-isomorphism F(a) ∼= F[X]/(g(X)).
Applying σ to the coeﬃcients of g(X) gives a polynomial gσ(X) ∈C[X].
Since C is
algebraically closed, gσ(X) has a root in C, say r. Let F[X] →C by acting as σ on F and
sending X to r. This is a ring homomorphism that sends g(X) to gσ(r) = 0, so we get an
induced homomorphism F[X]/(g(X)) →C acting as σ on F and sending X to r. Composing
this with the isomorphism F(a) ∼= F[X]/(g(X)) from before gives us a homomorphism
τ : F(a) →C acting as σ on F.
Thus (F, σ) ≤(F(a), τ) and (F, σ) ̸= (F(a), τ) since
F ̸= F(a). This is impossible by maximality of (F, σ), so F = L.
□
Corollary 1.2. Let K be a ﬁeld and i: K →L be a homomorphism to a ﬁeld L such
that L/i(K) is an algebraic extension. For each ﬁeld homomorphism ϕ: K →C to an
algebraically closed ﬁeld C, there is a ﬁeld homomorphism σ: L →C such that σ ◦i = ϕ.
L
σ
/ C
K
i
O
ϕ
8
Proof. Since i is a ﬁeld homomorphism it is injective: K and i(K) are isomorphic ﬁelds
using i. Run through the above proof with the following change: S is the set of pairs (F, f)
where F is a ﬁeld between i(K) and L and f ◦i = ϕ (rather than f|K = ϕ as we used
before). Deﬁne the partial ordering as before: (F, f) ≤(F ′, f′) when F ⊂F ′ and f′|F = f.
It is left to the reader to check that S satisﬁes the assumptions of Zorn’s lemma and that
a maximal element of S provides a solution to our problem.
□
Now we can establish the desired result about comparing two algebraic closures of a ﬁeld.
Corollary 1.3. All algebraic closures of a ﬁeld are isomorphic. More precisely, if C1 and
C2 are algebraic closures of a ﬁeld K with embeddings i1 : K →C1 and i2 : K →C2, there
is a ﬁeld isomorphism σ that makes the following diagram commute.
C1
σ
/ C2
K
i1
`
i2
>

<!-- page 3 -->
ZORN’S LEMMA AND SOME APPLICATIONS, II
3
Proof. Since C2 is algebraically closed and C1 is an algebraic extension of i1(K), Corollary
1.2 implies there is a ﬁeld homomorphism σ: C1 →C2 such that σ◦i1 = i2. The image σ(C1)
is an algebraically closed ﬁeld that contains σ(i1(K)) = i2(K). Since C2 is an algebraic
extension of i2(K), C2/σ(C1) is an algebraic extension of algebraically closed ﬁelds, so the
extension has to be trivial: σ(C1) = C2. Thus σ: C1 →C2 is a ﬁeld isomorphism and
σ ◦i1 = i2.
□
There is a huge number of isomorphisms between two algebraically closed ﬁelds, so the
construction in Corollary 1.3 is not at all canonical. While some of the fundamental appli-
cations of Zorn’s lemma in part I3 are known to be equivalent to Zorn’s lemma, this is not
true for existence of algebraic closures of all ﬁelds or the isomorphism between the algebraic
closures of a ﬁeld (in general): each of these can be proved using the Boolean ultraﬁlter
theorem, which is known to be weaker than Zorn’s lemma [1].
Remark 1.4. That every ﬁeld has an algebraic closure and that two algebraic closures of
a ﬁeld are isomorphic were ﬁrst proved by Steinitz in 1910 in a long paper [11] that created
from scratch the general theory of ﬁelds as part of abstract algebra. The inﬂuence of this
paper on the development of algebra was enormous; for an indication of this, see [8]. Steinitz
was hindered in this work by the primitive state of set theory at that time and he used the
well-ordering principle rather than Zorn’s lemma (which only became widely known in the
1930s [12]). Steinitz’s proof of the existence of algebraic closures and their uniqueness up
to isomorphism, together with his account of set theory, took up 20 pages [11, Sect. 19–21].
Corollary 1.5. Let K1 and K2 be isomorphic ﬁelds with respective algebraic closures C1
and C2. Each isomorphism K1 →K2 extends to an isomorphism C1 →C2. In particular,
if K is a ﬁeld with algebraic closure C then every ﬁeld homomorphism f : K →C such that
C/f(K) is algebraic extends to a ﬁeld automorphism of C.
There is nothing canonical about the extension: an isomorphism K1 →K2 will generally
have many extensions to an isomorphism C1 →C2.
Proof. Let f : K1 →K2 be a ﬁeld isomorphism and i1 : K1 →C1 and i2 : K2 →C2 be
embeddings into algebraic closures. Composing f with the embedding i2 : K2 →C2 gives
us a ﬁeld homomorphism i2 ◦f : K1 →C2. In Corollary 1.2 use L = C1 and ϕ = i2 ◦f to
see there is a ﬁeld homomorphism σ: C1 →C2 such that σ ◦i1 = ϕ = i2 ◦f, so we have a
commutative diagram
C1
σ
/ C2
K1
i1
O
f
/
ϕ
=
K2
i2
O
that shows σ(C1) is a subﬁeld of C2 containing σ(i1(K1)) = i2(f(K1)) = i2(K2) = K2.
Since C2 is an algebraic closure of K2, K2 ⊂σ(C1) ⊂C2, and σ(C1) is algebraically closed,
we must have σ(C1) = C2, so σ is an isomorphism.
If the ﬁeld K has algebraic closure C and f : K →C is a ﬁeld homomorphism, then
f : K →σ(K) is a ﬁeld isomorphism (a homomorphism, surjective, and injective since all
ﬁeld homomorphisms are injective).
When C is algebraic over f(K), C is an algebraic
3See Section 6 of https://kconrad.math.uconn.edu/blurbs/zorn1.pdf

<!-- page 4 -->
4
KEITH CONRAD
closure of f(K), so f : K →f(K) extends to an isomorphism C →C by using K1 = K,
K2 = f(K), C1 = C2 = C, and i1 : K →C and i2 : f(K) →C are inclusions.
C
σ
/ C
K
i1
O
f / f(K)
i2
O
□
2. Zorn’s lemma and real closed fields
Every ﬁeld has an algebraic closure. Certain ﬁelds have another, smaller, kind of closure
called a real closure. Before we deﬁne a real closure, we have to deﬁne a real ﬁeld. A ﬁeld is
called real (some use the label formally real) if −1 is not a sum of squares in the ﬁeld. For
instance, R is a real ﬁeld. A subﬁeld of a real ﬁeld is also real. More generally, a ﬁeld that
can be embedded into a real ﬁeld is real. For example, the abstract ﬁeld Q(θ) where θ4 = 2
is a real ﬁeld since it is isomorphic to Q(
4√
2), which is real because it is a subﬁeld of R.
The ﬁelds C and Q(i) are not real since −1 is a square in these ﬁelds. The ﬁeld Q(√−2)
is not real since −1 is a sum of two squares in this ﬁeld: −1 = (√−2/2)2 + (√−2/2)2.
The concept of a real ﬁeld is closely connected with the concept of an ordered ﬁeld (a ﬁeld
in which there is a reasonable notion of positive and negative): a ﬁeld has some ordering
– not necessarily just one – precisely when it is a real ﬁeld. That is, the orderable ﬁelds
are the real ﬁelds. For example, Q(θ) where θ4 = 2 has two orderings, based on the two
embeddings into R (θ 7→
4√
2 and θ 7→−
4√
2). For more information about real ﬁelds, see
[5, Chap. XI].
A real closure of a ﬁeld K is an extension ﬁeld L that is algebraic over K, real, and
admits no proper real algebraic extension. A real closure is essentially a maximal algebraic
extension in which −1 is not a sum of squares. For example, the ﬁeld of real algebraic
numbers is a real closure of Q. Real closures are not algebraically closed since X2 + 1 has
no root in real ﬁelds.
Since a real closure is a real ﬁeld and subﬁelds of real ﬁelds are real, K can only have a
real closure if K is real. And indeed they all do, as we now prove.
Theorem 2.1. Every real ﬁeld admits a real closure.
Proof. Let K be a real ﬁeld. That is, −1 is not a sum of squares in K. A real closure of K,
if it exists, is a particular kind of algebraic extension of K, so we will work inside a ﬁxed
algebraic closure C ⊃K.
Since a real closure should be a maximal real algebraic extension of K, the way to use
Zorn’s lemma should be obvious: take for S the set of all real algebraic extensions of K
inside of C. We know S ̸= ∅since K ∈S. Deﬁne a partial ordering on S by inclusion:
F ≤F ′ if F ⊂F ′. If {Fα}α∈A is a totally ordered subset of S then the union F = S
α∈A Fα
is a ﬁeld (by the usual proof) that is inside of C and it contains each Fα. To see that F
is real, assume otherwise: −1 = Pn
i=1 c2
i where ci ∈F. These ﬁnitely many ci’s are in
some common Fα (since the Fα’s are totally ordered), but then the equation −1 = Pn
i=1 c2
i
violates the property of Fα being real. So −1 is not a sum of squares in F, which means F
is real and thus F is an upper bound on {Fα}α∈A in S.
By Zorn’s lemma, S contains a maximal element. Denote one as R. Then R is a real
algebraic extension ﬁeld of K. To show R is a real closure of K we need to show R has no

<!-- page 5 -->
ZORN’S LEMMA AND SOME APPLICATIONS, II
5
proper real algebraic extension. There is no such extension of R in C because R is maximal
with respect to inclusion among real algebraic extensions of K in C. If there is a ﬁeld
extension R ,→R′ outside of C where R′ is real and algebraic over R, then by Theorem
1.1 we can embed R′ into C by a map ﬁxing R. (The ﬁeld C is an algebraic closure of
R since it is an algebraic closure of K and R/K is algebraic.) In particular, the image of
an embedding R′ ,→C ﬁxing R pointwise will be a (necessarily) real ﬁeld in C of degree
greater than 1 over R, but that contradicts maximality of R in S. So R ﬁts the deﬁnition
of being a real closure of K.
□
As with algebraic closures, Zorn’s lemma can be used to prove all real closures of a real
ﬁeld are isomorphic to each other [5, p. 455]. The proof requires some preliminary work on
“real roots” of polynomials that would be a bit of a diversion for us to review here.
In a real ﬁeld, none of the polynomials Pn
i=1 X2
i + 1 have solutions. If we only avoid
ﬁelds with solutions to the single polynomial X2 + 1, such maximal extensions need not
be isomorphic. That is, Zorn’s lemma implies that a ﬁeld not containing a square root of
−1 has a maximal algebraic extension not containing a square root of −1, but two such
maximal extensions need not be isomorphic. For example, the ﬁelds Q(
√
2) and Q(√−2)
don’t contain a square root of −1 so each of these ﬁelds has a maximal algebraic extension
F/Q(
√
2) and F ′/Q(√−2) not containing √−1. Both F and F ′ are also maximal algebraic
extensions of Q not containing √−1, but F ̸∼= F ′ since X2 −2 has a root in F but not in
F ′: if F ′ has a square root of 2 then its ratio with √−2 ∈F ′ is a square root of −1 in F ′,
and that’s impossible.
3. Zorn’s lemma and transcendence bases
So far we have focused on applications of Zorn’s lemma to algebraic ﬁeld extensions
(speciﬁcally, algebraic closures and real closures). Zorn’s lemma is just as important in
dealing with non-algebraic ﬁeld extensions, such as K(X, Y ) where X and Y are indetermi-
nantes over K. The central notion here is a transcendence basis for a ﬁeld extension L/K,
which is a nonlinear generalization of a basis for L/K.
Deﬁnition 3.1. In a ﬁeld extension L/K, a ﬁnite subset {s1, . . . , sn} of L is called alge-
braically dependent over K if f(s1, . . . , sn) = 0 for some nonzero polynomial f(X1, . . . , Xn) ∈
K[X1, . . . , Xn]. A ﬁnite subset of L that is not algebraically dependent over K is called
algebraically independent over K. An arbitrary subset of L is called algebraically dependent
over K if some ﬁnite subset is algebraically dependent over K and it is called algebraically
independent over K when every ﬁnite subset is algebraically independent over K (that is,
no ﬁnite subset is algebraically dependent over K).
If we only use linear polynomials f(X1, . . . , Xn) = a1X1 + · · · + anXn in this deﬁnition
then we get the concepts of linear dependence and linear independence over K. That is why
algebraic dependence and independence over K is a higher-degree generalization of linear
dependence and independence over K. We consider ∅in L to be algebraically independent
over K, just as ∅in L is linearly independent over K.
Example 3.2. In R, {π, π +
√
2} is linearly independent over Q (since
√
2 is algebraic and
π is transcendental), but is algebraically dependent over Q since f(π, π +
√
2) = 0 where
f(X, Y ) = (X −Y )2 −2.

<!-- page 6 -->
6
KEITH CONRAD
Example 3.3. In R, {π2 −2, 3π +
√
2} is algebraically dependent over Q: f(π2 −2, 3π +
√
2) = 0 where f(X, Y ) = (X + 2 −(Y −
√
2)2/9)(X + 2 −(Y +
√
2)2/9) = X2 + (32/9)X +
Y 4/81 −(2/9)XY 2 −(40/81)Y 2 + 256/81.
Example 3.4. A one-element subset {s} of L is algebraically independent over K if and
only if it s is transcendental over K.
Example 3.5. The extension L/K is algebraic if and only if the only subset of L that is
algebraically independent over K is ∅.
Example 3.6. It is expected that π and e are algebraically independent over Q, but this
is still an open problem. It would follow from Schanuel’s conjecture [6, Theorem 21.3].
Example 3.7. In the rational function ﬁeld in n variables, K(u1, . . . , un), {u1, . . . , un} is
algebraically independent over K.
Deﬁnition 3.8. In a ﬁeld extension L/K, a subset S of L is called a transcendence basis
over K if S is algebraically independent over K and S is not strictly contained in any other
algebraically independent subset over K.
Example 3.9. For a ﬁeld K, each nonconstant rational function a(u)/b(u) ∈K(u) is a
transcendence basis: a(u)/b(u) is transcendental over K because K(u)/K(a/b) is algebraic
(u is a root of a(X) −(a(u)/b(u))b(X) ∈K(a/b)[X], which is not 0) and K(u)/K is not
algebraic. No subset of K(u) strictly containing {a(u)/b(u)} is algebraically independent
since K(u)/K(a/b) is algebraic.
Example 3.10. In the rational function ﬁeld K(u1, . . . , un), the subset {u1, . . . , un} is a
transcendence basis: it is algebraically independent over K, and for a rational function
r = a(u1, . . . , un)/b(u1, . . . , un), the polynomial
f(X1, . . . , Xn, Xn+1) = b(X1, . . . , Xn)Xn+1 −a(X1, . . . , Xn) ∈K[X1, . . . , Xn, Xn+1]
is nonzero (why?) and f(u1, . . . , un, r) = 0. Therefore tr. deg(K(u1, . . . , un)/K) = n.
Theorem 3.11. Every ﬁeld extension L/K has a transcendence basis and every subset of
L that is algebraically independent over K can be extended to a transcendence basis of L/K.
Proof. To show L/K has a transcendence basis, consider the collection of all subsets of L
that are algebraically independent over K, partially ordered by containment. This is not an
empty collection since ∅is algebraically independent over K by deﬁnition. For every totally
ordered subset {Sα}α∈A of algebraically independent subsets over K, the union S = S
α Sα
is an algebraically independent subset over K because every ﬁnite set of elements of S is in
some Sα and Sα is an algebraically independent subset over K. Therefore by Zorn’s lemma
there is a subset of L that is (i) algebraically independent over K and (ii) not strictly
contained in a subset of L that is algebraically independent over K. Properties (i) and (ii)
describe a transcendence basis of L/K.
To show every subset S0 of L that is algebraically independent over K can be extended
to a transcendence basis of L/K, run through the previous argument using algebraically
independent subsets of L that contain S0.
□
Theorem 3.12. All transcendence bases of L/K have the same cardinality.
Proof. See [3, Chap. VI, Theorems 1.8, 1.9].
□

<!-- page 7 -->
ZORN’S LEMMA AND SOME APPLICATIONS, II
7
The common cardinality of all transcendence bases for L/K is called the transcendence
degree of L/K and is denoted tr. deg(L/K). This cardinal number is well-deﬁned by Theo-
rem 3.12.
Example 3.13. We have tr. deg(L/K) = 0 if and only if L/K is algebraic.
Example 3.14. We have tr. deg(K(u1, . . . , un)/K) = n.
Example 3.15. The ﬁeld K(x, y) where x is transcendental over K and y2 = x3 −1 has
transcendence degree 1 over K, with transcendence basis {x}.
See [5, Chap. VIII] or [9, pp. 357–373] for a detailed discussion of transcendence bases
and [2, Sect. 14.9] for a survey on transcendence bases without proofs.
When L/K has a transcendence basis S, the intermediate ﬁeld K(S) is purely transcen-
dental over K, in the sense that it is generated over K by elements that are algebraically
independent over K. The extension L/K(S) is algebraic: if some α ∈L were transcendental
over K(S) then S ∪{α} would be algebraically independent over K (why?), which contra-
dicts the maximality of a transcendence basis. Therefore every ﬁeld extension L/K can be
broken up into a tower L/K(S)/K where K(S)/K is purely transcendental and L/K(S)
is algebraic. In particular, if L is algebraically closed then L is an algebraic closure of the
ﬁeld K(S) that is purely transcendental over K.
Example 3.16. If C is an algebraically closed ﬁeld of characteristic 0 and S is a transcen-
dence basis of C/Q then C = Q(S).
Example 3.17. If C is an algebraically closed ﬁeld of characteristic p and S is a transcen-
dence basis of C/Fp then C = Fp(S).
Remark 3.18. A transcendence basis S for L/K such that the algebraic extension L/K(S)
is separable is called a separating transcendence basis. When K is perfect, every ﬁnitely
generated extension ﬁeld of K has a separating transcendence basis over K. We will not
use this concept here.
Theorem 3.19. If C is an algebraically closed ﬁeld and K is a subﬁeld then every auto-
morphism of K can be extended to an automorphism of C.
This is not Corollary 1.5, but is more general, since here C is not necessarily the algebraic
closure of K. It could be bigger. We will use Corollary 1.5 in the proof of Theorem 3.19.
Proof. Let S be a transcendence basis of C/K, so C = K(S). Each ﬁeld automorphism σ
of K extends in a unique way to an automorphism of the polynomial ring K[S] by behaving
like σ on K and ﬁxing all the elements of S. (We can think of K[S] as a polynomial ring
in S because elements of S are algebraically independent over K.) This automorphism of
K[S] extends in a unique way to an automorphism of its fraction ﬁeld K(S). Since C is
an algebraic closure of K(S), by Corollary 1.5 every automorphism of K(S) extends to an
automorphism of C. Thus σ extends (usually in many ways) to an automorphism of C.
□
Example 3.20. On the ﬁeld Q(
4√
2) there is a unique automorphism sending
4√
2 to −
4√
2.
Theorem 3.19 tells us there is an automorphism of C sending
4√
2 to −
4√
2. In particular, this
automorphism of C is not the identity or complex conjugation since they both ﬁx all real
numbers. Similarly, every automorphism of a ﬁnite extension of Q extends (in many ways)
to an automorphism of C. It is basically hopeless to expect we can write down formulas on
all of C for automorphisms other than the identity or complex conjugation. The existence
of such automorphisms is entirely due to Zorn’s lemma.

<!-- page 8 -->
8
KEITH CONRAD
Our next application of transcendence bases is a surprising result about uncountable
algebraically closed ﬁelds.
Theorem 3.21. Two uncountable algebraically closed ﬁelds are isomorphic if and only if
they have the same characteristic and cardinality.
For instance, every algebraically closed ﬁeld of characteristic 0 whose cardinality is the
same as that of C is isomorphic to C as an abstract ﬁeld. (Examples of this situation really
do occur, e.g., the algebraic closure of the p-adic numbers.)
Theorem 3.21 is false for countable algebraically closed ﬁelds. For instance, the algebraic
closures of Q and Q(X) are both countable of characteristic 0, but they are not isomorphic
ﬁelds since we can’t embed Q(X) inside an algebraic closure of Q: the element X is not
algebraic over Q.
To prove Theorem 3.21 we will use the following two lemmas about transcendence bases.
Lemma 3.22. Let C and C′ be algebraically closed ﬁelds. Then C is isomorphic to C′ if
and only if the ﬁelds have the same characteristic and the same transcendence degree over
their prime subﬁeld (Q or Fp).
Proof. Suppose C and C′ are isomorphic ﬁelds and f : C →C′ is an isomorphism. Certainly
the characteristics of C and C′ are the same.
Let F be the common prime subﬁeld of
C and C′ (either Q or Fp).
Then f is the identity map on F.
For a transcendence
basis S of C/F, check that its image f(S) is a transcendence basis for C′/F. Therefore
tr. deg(C/F) = card S = tr. deg(C′/F).
Conversely, suppose C and C′ have the same characteristic and the same transcendence
degree over their common prime subﬁeld F. Let S be a transcendence basis for C/F and
S′ be a transcendence basis for C′/F, so by hypothesis S and S′ have the same cardinality:
there is a bijection S →S′. This bijection extends uniquely to a ring isomorphism F[S] →
F[S′] (ﬁxing the elements of F), which extends uniquely to a ﬁeld isomorphism of fraction
ﬁelds F(S) →F(S′). By Corollary 1.5, the ﬁeld isomorphism F(S) →F(S′) extends (by
Zorn’s lemma, so in many ways) to a ﬁeld isomorphism of the algebraic closures, which are
C and C′.
□
This lemma tells us that an algebraically closed ﬁeld is determined up to isomorphism
by its characteristic and its transcendence degree over its prime subﬁeld. Computing the
transcendence degree of a ﬁeld extension might seem formidable: what are tr. deg(R/Q) or
tr. deg(C/Q)?
Lemma 3.23. Let F be a ﬁeld that is ﬁnite or countably inﬁnite and {Xi}i∈I be an inﬁnite
set of algebraically independent indeterminates over F. The cardinality of F({Xi}i∈I) equals
card I.
Proof. We will prove the polynomial ring R := F[{Xi}i∈I] has cardinality card I. That
suﬃces, since every inﬁnite integral domain has the same cardinality as its fraction ﬁeld.
In R, the set of powers Xmi
i
with mi ≥1 is in bijection with Z+ ×I, which is in bijection
with I since I is inﬁnite. The set of pure monomials Xm1
i1 · · · Xmk
ik
(coeﬃcient is 1, exponents
are ≥1) is in bijection with the set F of ﬁnite subsets of Z+ × I by sending each ﬁnite
subset to the product of the corresponding powers (send ∅to 1). The set of ﬁnite subsets of
an inﬁnite set S has the same cardinality as S, so card F = card(Z+ × I) = card I. The set
M of all monomials in R (allowing arbitrary coeﬃcients from F) is in bijection with F × F,
so card M = card(F × F) = card(F × I).

<!-- page 9 -->
ZORN’S LEMMA AND SOME APPLICATIONS, II
9
Let En be the set of elements of R that are a sum of at most n monomials, so En ⊂En+1
and R = S
n≥1 En. Addition of polynomials gives us a surjection Mn →En, so card(En) ≤
card(Mn). Since M is inﬁnite, card(Mn) = card M = card(F×I). Therefore R is a countable
union of sets En that each have cardinality ≤card(F × I), so card R ≤card(F × I).
Up to now we have not used the fact that F is ﬁnite or countably inﬁnite. Now we use
that: it tells us card(F ×I) = card I. Therefore card R ≤card I. Since R contains {Xi}i∈I,
card R ≥card I, so the Schroeder–Bernstein theorem tells us card R = card I.
□
Now we can prove Theorem 3.21.
Proof. Let C be an algebraically closed ﬁeld.
By Lemma 3.22, C is determined up to
isomorphism by its characteristic and its transcendence degree over its prime subﬁeld F.
We will show when C is uncountable that tr. deg(C/F) = card C, so C is determined up to
isomorphism by its characteristic and cardinality.
Let S be a transcendence basis of C/F, so C = F(S). Since C is uncountable, S has
to be inﬁnite: if S were ﬁnite then, since F is ﬁnite or countable, an algebraic closure
of F(S) would be countable. By deﬁnition, tr. deg(C/F) = card S. Lemma 3.23 tells us
card S = card(F(S)). Since F(S) is inﬁnite and C/F(S) is algebraic, card C = card F(S).
Thus card C = card S = tr. deg(C/F).
□
The proof of Theorem 3.21 used the fact that C is algebraically closed in its appeal to
Lemma 3.22 and nowhere else. Therefore the reasoning in the proof shows that if L is an
arbitrary uncountable ﬁeld with prime subﬁeld F, tr. deg(L/F) = card L.
Example 3.24. The extensions C/Q and R/Q have transcendence degree equal the car-
dinality of the continuum.
4. More extension problems using Zorn’s lemma
Zorn’s lemma is the standard method used to extend functions to a ﬁeld when starting
with a function on a subset of the ﬁeld. This has been done so far with ﬁeld homomorphisms.
Here we describe two other kinds of functions that occur in ﬁeld theory: derivations and
absolute values. Motivation for interest in these concepts comes from commutative algebra,
algebraic geometry, and number theory.
Example 4.1. For a ﬁeld extension L/K, a derivation d: K →L is a mapping such that
(i) d(x + y) = d(x) + d(y) and (ii) d(xy) = xd(y) + yd(x). This can be regarded as an
abstract version of diﬀerentiation. For instance, diﬀerentiation with respect to u on the
rational function ﬁeld F(u) is a derivation F(u) →F(u). The zero function on a ﬁeld is
also a derivation (it’s the only derivation on Q).
If L/K is a separable algebraic ﬁeld extension, possibly of inﬁnite degree, then every
derivation K →L extends uniquely to a derivation L →L. The proof of this reduces,
by Zorn’s lemma, to the case when L = K(α) is a ﬁnite separable extension [4, Cor. 2.4,
Chap. 4], [5, ??].
Example 4.2. An absolute value on a ﬁeld F is a function |·|: F →R such that (i) |x| ≥0
for all x ∈F, with equality if and only if x = 0, (ii) |xy| = |x||y|, and (iii) |x+y| ≤|x|+|y|.
When (iii) is replaced by the more restrictive condition |x + y| ≤max(|x|, |y|), the absolute
value | · | is called non-Archimedean. (The terminology “non-Archimedean” come from the
condition |x| < |y| not implying there is an integer n such that |nx| > |y|, which is the
Archimedean property of the real numbers.)

<!-- page 10 -->
10
KEITH CONRAD
Krull’s theorem about the extension of absolute values says that for every ﬁeld exten-
sion L/K, a non-archimedean absolute value on a ﬁeld K can be extended (generally not
uniquely) to a non-archimedean absolute value on L. By Zorn’s lemma, the proof of this
reduces to the case of a simple extension L = K(t), and then the cases when t is algebraic
over K or transcendental over K are treated separately [10, pp. 36–39]. For an alternate
proof of Krull’s theorem using Zorn’s lemma, see [7, pp. 107–108].
References
[1] B. Banaschewski, Algebraic closure without choice, Z. Math. Logik Grundlag. Math. 38 (1992), 383–385.
[2] D. Dummit and R. Foote, “Abstract Algebra,” 3rd ed., Wiley, New York, 2004.
[3] T. W. Hungerford, “Algebra,” Springer-Verlag, New York, 1974.
[4] G. Karpilovsky, “Topics in Field Theory,” North-Holland, 1989.
[5] S. Lang, “Algebra,” 3rd revised ed., Springer-Verlag, New York, 2002.
[6] M. R. Murty and P. Rath, “Transcendental Numbers,” Springer-Verlag, New York, 2014.
[7] P. Ribenboim, “The Theory of Classical Valuations,” Springer-Verlag, New York, 1999.
[8] P. Roquette, In memoriam Ernst Steinitz (1871–1928), J. Reine Angew. Math. 648 (2010), 1–11. URL
https://www.mathi.uni-heidelberg.de/∼roquette/STEINITZ.pdf.
[9] J. Rotman, “Advanced Modern Algebra,” Prentice-Hall, Upper Saddle River, NJ, 2002.
[10] W. Schikhof, “Ultrametric Calculus: an Introduction to p-adic Analysis,” Cambridge Univ. Press,
Cambridge, 1984.
[11] E. Steinitz, Algebraische Theorie der K¨orper, J. Reine Angew. Math. 137 (1910), 167–309. URL
https://eudml.org/doc/149323.
[12] M. Zorn, A remark on method in transﬁnite algebra, Bull. Amer. Math. Soc. 41 (1935), 667–670. URL
https://www.ams.org/journals/bull/1935-41-10/S0002-9904-1935-06166-X/.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*