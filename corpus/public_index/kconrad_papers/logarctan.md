# The Logarithm and Arctangent

> **Source**: https://kconrad.math.uconn.edu/blurbs/logarctan.pdf  
> **Author**: Keith Conrad  
> **Topic**: analysis  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
SERIES FOR THE LOGARITHM AND ARCTANGENT
KEITH CONRAD
1. Introduction
The purpose of this handout is twofold: review the derivation of the identities
(1.1)
log(1 + x) =
X
n≥1
(−1)n−1 xn
n = x −x2
2 + x3
3 −x4
4 + x5
5 −x6
6 + · · ·
and
(1.2)
arctan x =
X
n≥0
(−1)n x2n+1
2n + 1 = x −x3
3 + x5
5 −x7
7 + x9
9 −x11
11 + · · ·
for 0 ≤x ≤1 and extend them to a range which includes negative values of x. Speciﬁcally, we
want to show (1.1) is true for −1 < x ≤1 and (1.2) is true for −1 ≤x ≤1.
The main idea in both cases is an integration formula:
log(1 + x) =
Z x
0
dt
1 + t,
arctan x =
Z x
0
dt
1 + t2 .
These formulas connect both functions with the simpler function (integrand) 1/(1 −t) under a
change of variables.
2. Geometric series and integration
We start with the ﬁnite geometric series
1 + t + t2 + · · · + tN = tN+1 −1
t −1
= 1 −tN+1
1 −t
.
Here t ̸= 1. We isolate the term 1/(1 −t):
(2.1)
1
1 −t = 1 + t + t2 + · · · + tN + tN+1
1 −t.
Again, this is valid for t ̸= 1. Now we make two diﬀerent changes of variable to turn the left side
of (2.1) into an integrand adapted to the logarithm and arctangent functions. Replacing t with −t
in (2.1) gives
1
1 + t = 1 −t + t2 + · · · + (−1)NtN + (−1)N+1 tN+1
1 + t
=
N
X
n=0
(−1)ntn + (−1)N+1 tN+1
1 + t.
(2.2)
Here we must have t ̸= −1.
1

<!-- page 2 -->
2
KEITH CONRAD
Replacing t with −t2 in (2.1) gives
1
1 + t2 = 1 −t2 + t4 + · · · + (−1)Nt2N + (−1)N+1 t2(N+1)
1 + t2
=
N
X
n=0
(−1)nt2n + (−1)N+1 t2(N+1)
1 + t2 .
(2.3)
Here t can be any number: the denominator doesn’t become 0 since t2 is never −1.
These formulas for 1/(1 + t) and for 1/(1 + t2) will now be integrated from 0 to x (for variable
x). Well, we have to make sure −1 is not between 0 and x in the case of (2.2) since 1/(1 + t) blows
up at t = −1. We will apply
R x
0 (· · · ) dt to (2.2) with x > −1. We obtain
Z x
0
dt
1 + t =
N
X
n=0
(−1)n
Z x
0
tn dt + (−1)N+1
Z x
0
tN+1
1 + t dt,
which is the same as
log(1 + x) =
N
X
n=0
(−1)n xn+1
n + 1 + (−1)N+1
Z x
0
tN+1
1 + t dt
=
N+1
X
n=1
(−1)n−1 xn
n + (−1)N+1
Z x
0
tN+1
1 + t dt.
(2.4)
Now put the sum on one side and the other terms on the other side:
(2.5)
N+1
X
n=1
(−1)n−1 xn
n = log(1 + x) + (−1)N
Z x
0
tN+1
1 + t dt
Similarly, applying
R x
0 (· · · ) dt to (2.3) gives
Z x
0
dt
1 + t2 =
N
X
n=0
(−1)n
Z x
0
t2n dt + (−1)N+1
Z x
0
t2(N+1)
1 + t2 dt,
which is the same as
arctan x =
N
X
n=0
(−1)n x2n+1
2n + 1 + (−1)N+1
Z x
0
t2(N+1)
1 + t2 dt.
Isolating the sum on one side yields, after some algebra,
(2.6)
N
X
n=0
(−1)n x2n+1
2n + 1 = arctan x + (−1)N
Z x
0
t2(N+1)
1 + t2 dt.
Our remaining task is to show, for suitable ﬁxed x, that the deﬁnite integrals on the right sides
of (2.5) and (2.6) tend to 0 as N →∞. When that happens we obtain the series representations
(1.1) and (1.2) for those values of x.
From this point of view, the important issue concerning the deﬁnite integrals in (2.5) and (2.6)
is not to compute them exactly, but to estimate them and show in favorable cases through these
estimates that the integrals tend to 0 as N →∞.

<!-- page 3 -->
SERIES FOR THE LOGARITHM AND ARCTANGENT
3
3. The logarithm case
For the logarithm series (2.5), we will show
(3.1)
lim
N→∞
Z x
0
tN+1
1 + t dt = 0
for each x in the half-open interval (−1, 1].
First suppose 0 ≤x ≤1. When t ∈[0, x] we have
0 ≤tN+1
1 + t ≤tN+1.
Integrating these inequalities over the interval [0, x] gives
0 ≤
Z x
0
tN+1
1 + t dt ≤
Z x
0
tN+1 dt = xN+2
N + 2 ≤
1
N + 2.
Our integral of interest is squeezed between 0 and 1/(N + 2). As N →∞the upper bound tends
to 0, so (3.1) has been veriﬁed when 0 ≤x ≤1.
Now suppose −1 < x < 0. Write x = −y with 0 < y < 1. Then, using the change of variables
u = −t,
Z x
0
tN+1
1 + t dt = (−1)N
Z −x
0
uN+1
1 −u du
= (−1)N
Z y
0
uN+1
1 −u du.
The integrand uN+1/(1 −u) is nonnegative for 0 ≤u ≤y, so

Z x
0
tN+1
1 + t dt
 =
Z y
0
uN+1
1 −u du.
To get an upper bound on the integral we replace the denominator 1 −u by the lower bound 1 −y:
0 ≤u ≤y =⇒uN+1
1 −u ≤uN+1
1 −y .
Therefore
(3.2)

Z x
0
tN+1
1 + t dt
 =
Z y
0
uN+1
1 −u du ≤
Z y
0
uN+1
1 −y du.
Since 0 < y < 1,
Z y
0
uN+1
1 −y du =
1
1 −y
Z y
0
uN+1 du
=
yN+2
(N + 2)(1 −y)
≤
1
(N + 2)(1 −y)
=
1
(N + 2)(1 + x).

<!-- page 4 -->
4
KEITH CONRAD
Feeding this back into (3.2) gives

Z x
0
tN+1
1 + t dt
 ≤
1
(N + 2)(1 + x).
For each x in (−1, 0), this upper bound tends to 0 as N →∞.
We have completed the derivation of (1.1) for −1 < x ≤1.
4. The arctangent case
In (2.6) we want to show
lim
N→∞
Z x
0
t2(N+1)
1 + t2 dt = 0
for each x in the closed interval [−1, 1].
First we suppose 0 ≤x ≤1. If 0 ≤t ≤x then
0 ≤t2(N+1)
1 + t2 ≤t2(N+1),
so
0 ≤
Z x
0
t2(N+1)
1 + t2 dt ≤
Z x
0
t2(N+1) dt = x2N+3
2N + 3 ≤
1
2N + 3.
As N →∞, the upper bound tends to 0 so the integral tends to 0.
Now suppose −1 ≤x < 0. Write x = −y where 0 < y ≤1. Then, using the substitution u = −t,
Z x
0
t2(N+1)
1 + t2 dt = −
Z −x
0
u2(N+1)
1 + u2 du = −
Z y
0
u2(N+1)
1 + u2 du.
The integral on the right is exactly the kind we treated already: as N →∞it tends to 0.
This completes the derivation of (1.2) for −1 ≤x ≤1.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*