# Transcendence of e

> **Source**: https://kconrad.math.uconn.edu/blurbs/transcendence-e.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
TRANSCENDENCE OF e
KEITH CONRAD
1. Introduction
A complex number z is called algebraic if f(z) = 0 for a nonzero polynomial f with
rational coeﬃcients. Algebraic numbers include
√
2 and
√
2 +
√
3: they are roots of x2 −2
and x4 −10x2 + 1. Complex numbers that are not algebraic are called transcendental. A
transcendental number is a “strong” type of irrational number: the irrational numbers are
not roots of linear polynomials with rational coeﬃcients, while transcendental numbers are
not roots of polynomials of arbitrary positive degree with rational coeﬃcients.
The concept of a transcendental number is due to Euler.
He did not give a precise
deﬁnition, but he thought of such numbers as “transcending” the methods of algebra. In
1775 he suggested that π is transcendental when he wrote [3, §12]
“It appears quite certain that the perimeter of a circle constitutes such a
peculiar kind of transcendental quantity that it can in no way be compared
with any other quantities.”
At that time π was already known to be irrational by work of Lambert [7], but its transcen-
dence would take over 100 more years to be established.1 The ﬁrst proofs that transcendental
numbers really exist appeared in the 19th century.
• In 1844, Liouville [9, p. 885] introduced a technique that proves P
n≥0 1/bn! is tran-
scendental for each integer b ≥2, with full details appearing in 1851 [10]. Such sums
are not as mathematically interesting as π or e.
• In 1873, Hermite [4] proved e is transcendental.
• In 1874, Cantor [1] published his ﬁrst paper on set theory, where he showed that the
set of algebraic real numbers is countable while an interval [a, b] with a < b is not.
Therefore [a, b] contains transcendental real numbers (otherwise it is a subset of the
algebraic real numbers, and hence countable), so transcendental numbers exist.2
• In 1882, Lindemann [8] proved π is transcendental by modifying the proof for e.
We’ll prove below that e is transcendental. The main tools are (i) the identity (et)′ = et
(a characterizing property of e), (ii) integration by parts, and (iii) Taylor’s formula for
coeﬃcients in terms of higher derivatives.
2. A transcendence criterion
Ultimately all proofs of transcendence of speciﬁc numbers are based on the fact that
there are no integers between 0 and 1, or equivalently |n| ≥1 for all nonzero integers n.
To understand how this can help, let’s ﬁrst see how it implies that rational numbers don’t
have “good approximations” by other rational numbers. That might sound strange, since
1In 1744 Euler [2, §105] said that for positive rational a and b, with b ̸= 1, if logb a is irrational then it is
transcendental. This was proved by Gelfond and Schneider, independently, in 1934.
2For an account of [1], see https://en.wikipedia.org/wiki/Cantor’s first set theory article.
1

<!-- page 2 -->
2
KEITH CONRAD
rational numbers are dense in the real line: every real number α can be approximated
arbitrarily closed by a rational number, such as by a truncation of its decimal expansion.
So how can we say a number can’t be approximated well by rational numbers? It’s a matter
of deﬁning what the term “good approximation” means!
Rather than measuring the approximation of α by a fraction p/q using |α −p/q|, we will
use |qα −p|. Here and below, p and q are integers, with q > 0 (denominators are always
positive). That is, we consider p/q to be a good approximation to α if |qα −p| is small.3
That equals q|α−p/q|, so we are increasing the usual notion of closeness by a factor coming
from the denominator q: the size of the denominator is now just as important for us as the
distance between α and p/q in order to consider p/q to be a good approximation to α.
Example 2.1. For α =
√
3 = 1.732 . . ., if we use p/q = 173/100 (a reduced form fraction),
then |qα −p| = |100
√
3 −173| ≈.205, which might seem good, but for the fraction p/q =
26/15 we have |qα −p| = |15
√
3 −26| ≈.019, which is ten times less and uses a much
smaller denominator (15 vs. 100). So for our purposes, we consider 26/15 to be a much
better approximation to
√
3 than 173/100 is.
Let’s put this viewpoint to work for the approximation of fractions by other fractions.
If α = a/b is rational with b > 0 and p/q is another rational number, then |α −p/q| =
|a/b −p/q| = |qa −pb|/bq, so |qα −p| = q|α −p/q| = |qa −pb|/b. Since p/q ̸= α, qα −p
is not 0, so the integer qa −pb is not 0.
Thus |qa −pb| ≥1, so |qα −p| ≥1/b: we
can’t approximate a fraction a/b by other fractions, in the |qα −p| sense, to less than 1/b.
Therefore if α is a real number for which we can ﬁnd a sequence of diﬀerent fractions pr/qr
such that |qrα −pr| →0, then α must be irrational: a number that can be approximated
too well by rational numbers can’t be a rational number. And the converse is true too: for
every irrational number α there is a sequence of reduced form fractions pr/qr with qr →∞
as r →∞such that |qrα −pr| < 1/qr, so |qrα −pr| →0 as r →∞.
To improve this criterion for irrationality of α to a criterion for transcendence of α,
we’ll put a condition on approximations not just of α, but of its powers: if α, α2, . . . , αm,
for each m ∈Z+, can be simultaneously approximated well by fractions with a suitable
common denominator, then α is transcendental.
Theorem 2.2. For nonzero α in R, assume for each m ∈Z+ that there are m sequences
of rational numbers pr1/qr, . . . , prm/qr for r = 1, 2, . . . such that
(i) max1≤k≤m |qrαk −prk| →0 as r →∞,
(ii) pr1, . . . , prm have a common factor dr that is relatively prime to qr and dr →∞as
r →∞.
Then α is transcendental.
When we refer to the sequences pr1/qr, . . . , prm/qr for r ≥1, what we mean is the
sequences of (m+1)-tuples (pr1, . . . , prm, qr), since we use the numerators and denominators
in (i) and (ii). And for a given m, we allow pr1, . . . , prm, and qr to depend on m.
Proof. Assume α is algebraic, so a0+a1α+· · ·+amαm = 0 for some m ≥1 where the rational
coeﬃcients a0, . . . , am are not all 0. Take m as small as possible, which forces am ̸= 0 and
3If p/q is not in reduced form, say p/q = dp′/dq′ with d = (p, q), then |qα −p| = d|q′α −p′| ≥|q′α −p′|,
so when |qα −p| is small for a fraction p/q that may not be reduced, replacing p/q with its reduced form
will make this new method of measuring a rational approximation smaller, not larger.

<!-- page 3 -->
TRANSCENDENCE OF e
3
a0 ̸= 0 (since α ̸= 0). Multiply through the equation by a common denominator of the
coeﬃcients, so we can assume a0, . . . , am are all integers.
Since prk/qr should be a good approximation of αk, in the relation a0+a1α+· · ·+amαm =
0 let’s replace αk with prk/qr and see how close to 0 it is:
a0 + a1
pr1
qr
+ · · · + am
prm
qr
= a0 + a1
pr1
qr
+ · · · + am
prm
qr
−
m
X
k=0
akαk
(2.1)
= a0 −a0 + a1
pr1
qr
−α

+ · · · + am
prm
qr
−αm

=
m
X
k=1
ak
prk
qr
−αk

=⇒a0qr +
m
X
k=1
akprk =
m
X
k=1
ak(prk −αkqr)
(2.2)
by clearing the denominator qr to get the last equation.
The left side of (2.2) is an integer and the right side of (2.2) tends to 0 as r →∞:

m
X
k=1
ak(prk −αkqr)
 ≤
m
X
k=1
|ak||prk −αkqr| ≤
 m
X
k=1
|ak|
!
max
1≤k≤m |prk −αkqr|,
where Pm
k=1 |ak| is independent of r and max1≤k≤m |prk −αkqr| →0 as r →∞by condition
(i). Since the only integer with absolute value less than 1 is 0, for large enough r
a0qr +
m
X
k=1
akprk = 0.
By condition (ii), Pm
k=1 akprk is divisible by dr, so dr | a0qr. Since (dr, qr) = 1, dr | a0 for
large r. Since dr →∞as r →∞and a0 ̸= 0, we get a contradiction once |dr| > |a0|.
□
3. Transcendence of e
To prove e is transcendental, we follow the basic idea of Hermite’s proof with simpliﬁca-
tions introduced later by Hilbert [6]. We begin with a calculation based on integration by
parts. For a polynomial f(t) with real coeﬃcients and x ∈R,
Z x
0
e−tf(t) dt = f(0) −e−xf(x) +
Z x
0
e−tf′(t) dt.
The integral on the right is the same as that on the left side except f has been replaced by
f′. Repeating the integration by parts once more,
Z x
0
e−tf(t) dt = f(0) −e−xf(x) + (f′(0) −e−xf′(x)) +
Z x
0
e−tf′′(t) dt
= (f(0) + f′(0)) −e−x(f(x) + f′(x)) +
Z x
0
e−tf′′(t) dt.
Do this repeatedly, and since f(j) = 0 for large enough j, the integral term on the right
eventually disappears and we’re left with
(3.1)
Z x
0
e−tf(t) dt =
X
j≥0
f(j)(0) −e−x X
j≥0
f(j)(x),

<!-- page 4 -->
4
KEITH CONRAD
where the two sums on the right each have ﬁnitely many terms since f(j) = 0 for large j.
Remark 3.1. On the right side of (3.1), the ﬁrst sum is
R ∞
0 e−tf(t) dt and the second sum
is
R ∞
x e−tf(t) dt.
Set If(t) := P
j≥0 f(j)(t). It is a polynomial of degree deg f.4 Using If(t) on the right
side of (3.1) and multiplying both sides by ex, we obtain what is called Hermite’s identity:
(3.2)
ex
Z x
0
e−tf(t) dt = If(0)ex −If(x)
for a polynomial f(t).
Theorem 3.2. The number e is transcendental.
Proof. We will apply Hermite’s identity to a carefully chosen sequence of polynomials fr(t).
Fix m ∈Z+. For r ≥1, set
(3.3)
fr(t) = tr−1(t −1)r(t −2)r · · · (t −m)r.
(Although this polynomial depends on m, we keep m out of the notation to avoid clut-
ter.) What is important about fr(t) is that it has integral coeﬃcients, high-order zeros at
0, 1, 2, . . . , m when r is large, and the order of its zero at t = 0 is one less than the order
of its zeros at 1, . . . , m. For perspective, in many proofs of transcendence of speciﬁc types
of numbers, there is a key step involving the construction of polynomials or analytic or
meromorphic functions satisfying some type of behavior at speciﬁc points, such as high-
order zeros at certain points or growth conditions at ∞. While we can deﬁne the functions
fr(t) in an explicit way, in more diﬃcult transcendence proofs the existence of suitable
functions with growth conditions may only be known by an indirect method, such as from
the pigeonhole principle.
In Hermite’s identity (3.2), set x = k to be a nonnegative integer:
(3.4)
ek
Z k
0
e−tfr(t) dt = Ifr(0)ek −Ifr(k).
Since fr(t) has coeﬃcients in Z, so do its derivatives f(j)
r (t). Therefore Ifr(0) and Ifr(k)
are integers. The right side of (3.4) is going to play the role of qrαk −prk in Theorem 2.2
after we remove a common factor in Ifr(0) and Ifr(k) for 1 ≤k ≤m: we’re going to show
Ifr(0) is divisible by (r −1)! and Ifr(k) is divisible by r! for 1 ≤k ≤m.
From Taylor’s formula for coeﬃcients in terms of derivatives,
fr(t) =
X
j≥r−1
f(j)
r (0)
j!
tj =
X
j≥r
f(j)
r (k)
j!
(t −k)j,
where we can start the sums at j = r −1 and j = r because fr(t) is divisible by tr−1 and
(t −k)r. Because fr(t) has integral coeﬃcients, each f(j)
r (0)/j! for j ≥r −1 is an integer,
which makes f(j)
r (0) a multiple of j!. Thus f(r−1)
r
(0) is a multiple of (r −1)! and f(j)
r (0) is a
multiple of r! when j ≥r. The coeﬃcients of fr(t) as a polynomial in t −k are also integral
4The motivation to consider this sum of higher derivatives in If(t) comes from the successive use of
integration by parts. Integration by parts can be replaced by the Mean Value Theorem, as in the proof of
transcendence of e in [5, §5.2] but that leaves the role of If(t) completely mysterious.

<!-- page 5 -->
TRANSCENDENCE OF e
5
(since Z[t] = Z[t −k]), so when j ≥r, f(j)
r (k)/j! is an integer and thus f(j)
r (k) is a multiple
of r!.
In (3.4),
(3.5)
Ifr(0) =
X
j≥0
f(j)
r (0) = f(r−1)
r
(0) +
X
j≥r
f(j)
r (0)
and all terms in the sum over j ≥r are multiples of r!. Similarly, Ifr(k) = P
j≥r f(j)
r (k) is
a multiple of r!. Since Ifr(0) and Ifr(k) are multiples of (r −1)!, divide (3.4) by (r −1)!:
(3.6)
ek
(r −1)!
Z k
0
e−tfr(t) dt = Ifr(0)
(r −1)!ek −Ifr(k)
(r −1)! = qrek −prk,
where qr = Ifr(0)/(r −1)! and prk = Ifr(k)/(r −1)!. The numbers qr and pr1, . . . , prm
are integers with prk ≡0 mod r .
We can compute f(r−1)
r
(0) explicitly: the coeﬃcient
of tr−1 in fr(t) is f(r−1)
r
(0)/(r −1)!, and also by the deﬁnition of fr(t) that coeﬃcient is
(−1)r(−2)r · · · (−m)r = ±m!r, so f(r−1)
r
(0) = ±m!r(r−1)!. All terms in (3.5) after f(r−1)
r
(0)
are divisible by r!, so Ifr(0) ≡±m!r(r −1)! mod r!. Therefore qr ≡±m!r mod r .
We’re now going to check that qrek −prk in (3.6) ﬁts conditions (i) and (ii) in Theorem
2.2 when α = e.
Condition (i): for 1 ≤k ≤m,
|qrek −prk| =

ek
(r −1)!
Z k
0
e−tfr(t) dt

≤
ek
(r −1)!
Z k
0
e−t|fr(t)| dt
≤
em
(r −1)!
Z m
0
e−t|t|r−1|t −1|r · · · |t −m|r dt.
When 0 ≤t ≤m, |t| ≤m and |t −j| ≤m for j = 1, . . . , m, so
|qrek −prk| ≤
em
(r −1)!
Z m
0
e−tmr−1 mr · · · mr
|
{z
}
m copies
dt = emmr−1+mr
(r −1)!
Z m
0
e−t dt.
Since
R m
0 e−t dt = 1 −e−m < 1,
|qrek −prk| < emmr−1+mr
(r −1)!
= emm(m+1)(r−1)+m
(r −1)!
= emmm (mm+1)r−1
(r −1)!
.
This upper bound tends to 0 as r →∞since Ar−1/(r −1)! →0 for every number A; we
use A = mm+1 (note m is ﬁxed when verifying condition (i)).
Condition (ii): for 1 ≤k ≤m, we already noted that each prk is a multiple of r, so dr := r
is a common factor of pr1, . . . prm. We also saw that qr ≡±m!r mod r, so if (r, m!) = 1 then
(r, qr) = 1. To make (r, m!) = 1, focus on integers r such that r ≡1 mod m! or use prime r
that are greater than m. There are inﬁnitely many such r either way.5
5Most accounts of a proof of transcendence of e use prime r > m right from the start of the proof, so they
only use polynomials fp(t) where p is prime. This gives an impression that the proof of the transcendence
of e actually needs the inﬁnitude of the primes, which is incorrect: just use r = 1 + m!M for big M since all
we need about r is that (r, m!) = 1 and that we can let r →∞.

<!-- page 6 -->
6
KEITH CONRAD
In Theorem 2.2 we work with r →∞through the positive integers, but the proof works
with r running over any sequence of integers tending to ∞, so by letting r →∞through
the integers relatively prime to m!, we have shown the two conditions in Theorem 2.2 are
satisﬁed when α = e, so e is trancendental.
□
Remark 3.3. The choice of fr(t) in (3.3) is due to Hilbert [6] and appears in all modern
proofs of transcendence of e. Hermite used other polynomials. A survey of the polynomials
used by diﬀerent authors in proofs of transcendence of e is in [11, pp. 85–88].
The proof of Theorem 2.2 gives, for each m, good rational approximations to e, e2, . . . , em:
for 1 ≤k ≤m, ek is well approximated by prk/qr where prk = P
j≥0 f(j)
r (k)/(r −1)! and
qr = P
j≥0 f(j)
r (0)/(r −1)!. Both numerators are ﬁnite sums since fr(t) is a polynomial.
Example 3.4. Taking m = 2, here is a table of approximations to e = 2.718281828459 . . .
and e2 = 7.389056098930 . . . for 1 ≤r ≤4, using fr(t) = tr−1(t −1)r(t −2)r.
r
pr1
pr2
qr
pr1/qr
pr2/qr
1
1
3
1
1.000000000
3.0000000000
2
92
250
34
2.705882352
7.3529411764
3
17049
46344
6272
2.718271683
7.3890306122
4
5888864
16007592
2166392
2.718281825
7.3890560895
References
[1] G. Cantor, ¨Uber eine Eigenschaft des Inbegriﬀes aller reellen algebraischen Zahlen, Journal Reine Angew.
Mathematik 77 (1874), 258–262. URL https://eudml.org/doc/148238.
[2] L. Euler, “Introduction to Analysis of the Inﬁnite, Volume 1,” M.-M. Bousquet, Lausanne, 1748. URL
http://www.17centurymaths.com/contents/introductiontoanalysisvol1.htm.
[3] L.
Euler,
De
relatione
inter
ternas
pluresve
quantitates
instituenda,
Opuscula
Analytica
2
(1755), 91–101. URL https://scholarlycommons.pacific.edu/euler-works/591/. English translation:
http://eulerarchive.maa.org/docs/translations/E591trans.pdf.
[4] C. Hermite, Sur la fonction exponentielle, Comptes Rendus Acad. Sci. Paris 77 (1873), 18–24, 74–79,
226–233, 285–293. URL https://gallica.bnf.fr/ark:/12148/bpt6k3034n/f18.item.
[5] I. N. Herstein, “Topics in Algebra,” 2nd ed., Wiley, New York, 1975.
[6] D. Hilbert, Ueber die Transcendenz der Zahlen e und π, Math. Annalen 43 (1893), 216–219. URL
https://eudml.org/doc/157679.
[7] J. H. Lambert, M´emoire sur quelques propri´et´es remarquables des quantit´es transcendantes cir-
culaires et logarithmiques, Histoire de l’Acad´emie Royale des Sciences et Belles-Lettres de Berlin,
Ann´ee 1761 17 1768, 265–322. URL http://www.bibnum.education.fr/mathematiques/theorie-des-
nombres/lambert-et-l-irrationalite-de-p-1761. English translation at https://hal.archives-
ouvertes.fr/hal-02984214/document.
[8] F. Lindemann, ¨Uber die Zahl π, Math. Annalen 20 (1882), 213–225. URL https://eudml.org/doc/
157031.
[9] J.
Liouville,
Sur
les
classes
tr`es-´etendues
de
quantit´es
dont
la
valeur
n’est
ni
rationelle
ni
mˆeme
r´eductible
`a
des
irrationelles
alg´ebriques,
Comptes
Rendus
Acad.
Sci.
Paris
18
(1844),
883–885,
910–911.
URL
http://www.bibnum.education.fr/mathematiques/theorie-des-
nombres/propos-de-l-existence-des-nombres-transcendants.
[10] J. Liouville, Sur les classes tr`es-´etendues de quantit´es dont la valeur n’est ni alg´ebrique, Journal
Math. Pures et Appl. 16 (1851), 133–142. URL https://gallica.bnf.fr/ark:/12148/bpt6k16395z/
f141n10.capture.
[11] N. I. Feldman and Y. V. Nesterneko, “Number Theory IV: Transcendental Numbers,” Springer-Verlag,
Berlin, 1998.
[12] A. Shidlovskii, “Transcendental Numbers,” de Gruyter, Berlin 1989.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*