# Relativity

> **Source**: https://kconrad.math.uconn.edu/blurbs/relativity.pdf  
> **Author**: Keith Conrad  
> **Topic**: group_theory  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
RELATIVISTIC ADDITION AND GROUP THEORY
KEITH CONRAD
1. Introduction
For three particles P, Q, R traveling on a straight line, let vPQ be the (relative) velocity
of P as measured by Q, and deﬁne vQR, vPR similarly.
According to classical mechanics, the velocity v of a particle moving on a line can be an
arbitrary real number, and relative velocities add by the simple formula
vPR = vPQ + vQR.
On the other hand, the special theory of relativity says velocities are restricted to a
bounded range, −c < v < c, where c is the speed of light (whose value of course depends
on the choice of units, and it is convenient to choose them so c = 1, but we won’t do that.)
The relativistic addition formula for relative velocities along a line is
(1.1)
vPR =
vPQ + vQR
1 + (vPQvQR/c2).
Example 1.1. Suppose Q moves away from R at speed (1/2)c and P moves away from Q
in the same direction at speed (1/2)c. Then vQR = (1/2)c and vPQ = (1/2)c, so (1.1) says
vPR =
vPQ + vQR
1 + (vPQvQR/c2) =
c
1 + (1/4) = 4
5c < c.
Example 1.2. If P moves away from Q at speed (3/4)c and R moves away from Q in the
opposite direction at speed (1/2)c, so vPQ = (3/4)c and vRQ = −(1/2)c, then vQR = (1/2)c
and (1.1) says
vPR =
vPQ + vQR
1 + (vPQvQR/c2) =
(5/4)c
1 + (3/8) = 10
11c < c.
There is an interesting algebraic similarity between the classical and relativistic velocity
addition formulas.
The classical model for velocity addition is the set of real numbers,
combined under addition.
Special relativity involves velocities in an interval (−c, c) for
some c > 0, combining them by the formula
(1.2)
v ⊕w =
v + w
1 + vw/c2 .
The operation ⊕on (−c, c) has properties similar to addition on R (check these!):
• Closure, i.e., if v1, v2 ∈(−c, c) then v1 ⊕v2 ∈(−c, c).
• Identity for ⊕: 0 ⊕v = v ⊕0 = v for v ∈(−c, c).
• Inverse of each v under ⊕is −v: v ⊕−v = −v ⊕v = 0.
• Associativity: (v1 ⊕v2) ⊕v3 = v1 ⊕(v2 ⊕v3) for all v1, v2, v3 ∈(−c, c).
1

<!-- page 2 -->
2
KEITH CONRAD
These say (1.2) is a group law on (−c, c). Einstein, in his ﬁrst paper on special relativity,
wrote [1, §5] that “such parallel transformations – necessarily – form a group”.1
The formula for v ⊕w in (1.2) resembles the addition formula for the tangent function:
tan(x + y) =
tan x + tan y
1 −(tan x)(tan y).
However, there is a minus sign here where there is a plus sign in (1.2).
The hyperbolic tangent is better than the tangent in this regard. The hyperbolic tangent
function is given by the formula
tanh x = ex −e−x
ex + e−x : R →(−1, 1)
and a graph is in Figure 1. Its range is (−1, 1) and its inverse is
tanh−1(x) = 1
2 log
1 + x
1 −x

.
x
y
1
−1
Figure 1. Plot of y = tanh x.
It is a matter of algebra to check that
tanh(x + y) =
tanh x + tanh y
1 + (tanh x)(tanh y).
This is exactly like (1.2), up to some factors of c. Since tanh(R) = (−1, 1), the function
ϕ(x) = c tanh(x) is a bijection R →(−c, c) and satisﬁes
ϕ(x + y) = ϕ(x) ⊕ϕ(y).
Its inverse ψ: (−c, c) →R is given by
ψ(v) = 1
2 log
1 + v/c
1 −v/c

.
This “rescaled” velocity turns ⊕into addition:
(1.3)
ψ(v ⊕w) = ψ(v) + ψ(w).
Thus, by a suitably clever transformation, velocities v ∈(−c, c) turn into rescaled velocities
ψ(v) ∈R and the nonintuitive operation ⊕on (−c, c) turns into ordinary addition in R.
Example 1.3. If v = (1/2)c and w = (1/2)c then ψ(v) = (1/2) log 3 and ψ(w) = (1/2) log 3,
while ψ(v ⊕w) = ψ((4/5)c) = (1/2) log 9 = log 3 = ψ(v) + ψ(w).
1Einstein wrote the speed of light in [1] as V , a notation ﬁrst used in Maxwell’s work on electromagnetism.

<!-- page 3 -->
RELATIVISTIC ADDITION AND GROUP THEORY
3
Example 1.4. If v = (3/4)c and w = (1/2)c then ψ(v) = (1/2) log 7 and ψ(w) = (1/2) log 3,
while ψ(v ⊕w) = ψ((10/11)c) = (1/2) log 21 = ψ(v) + ψ(w).
Remark 1.5. Each velocity v in (−c, c) is c tanh(x) for a unique x in R. The parameter
x = ψ(v) is called “rapidity” in physics. Combining two relativistic velocities (along the
same direction) corresponds to adding their rapidities, and when v →c−, the rapidity ψ(v)
tends to ∞: light has ﬁnite velocity and inﬁnite rapidity.
Could we have found ψ if we did not know the hyperbolic tangent? Yes! Using the ideas
in [3, Chap. 6], we will prove that every (continuously diﬀerentiable) group law on an open
interval in R can be rescaled to look like ordinary addition on R.
Remark 1.6. Instead of converting relativistic addition on (−c, c) into ordinary addition on
R, we can convert it into ordinary multiplication on (0, ∞): the function f : (−c, c) →(0, ∞)
where f(v) = (1 + v/c)/(1 −v/c) = (c + v)/(c −v) is a bijection and f(v ⊕w) = f(v)f(w)
for all v and w in (−c, c).
2. Group laws on an interval
Let I ⊂R be an open interval with a group law ∗, so ∗has the following properties:
• Closure. x, y ∈I =⇒x ∗y ∈I.
• Identity. There is u ∈I such that for all x ∈I, x ∗u = u ∗x = x.
• Inverses. For all x ∈I there is some i(x) ∈I such that x ∗i(x) = i(x) ∗x = u.
• Associativity. For x, y, z ∈I, (x ∗y) ∗z = x ∗(y ∗z).
(We write the identity for ∗as u rather than, say, e, since we’re working with real numbers
and don’t want confusion with the real number 2.71828...)
It will be useful to write the operation x∗y in the notation of a function of two variables:
F(x, y) = x ∗y. For example, the classical and relativistic velocity addition formulas are
F(v, w) = v + w, I = R;
F(v, w) =
v + w
1 + vw/c2 , I = (−c, c).
The above properties of ∗take the following form in terms of F:
• x, y ∈I ⇒F(x, y) ∈I.
• There is u ∈I such that for all x ∈I, F(x, u) = F(u, x) = x.
• For all x ∈I there is some i(x) ∈I such that F(x, i(x)) = F(i(x), x) = u.
• For x, y, z ∈I, F(F(x, y), z) = F(x, F(y, z)).
Our goal is to prove the following theorem.
Theorem 2.1. If the group law F(x, y) = x ∗y on an interval I has continuous partial
derivatives, then there is a diﬀerentiable bijection ℓ: I →R that converts ∗on I to ordinary
addition on R. That is, ℓis a diﬀerentiable bijection with ℓ(x ∗y) = ℓ(x) + ℓ(y).
We write the rescaling function as ℓbecause we think about it as a ‘logarithm’ for ∗, just
as the usual logarithm turns multiplication on (0, ∞) into addition on R.
Theorem 2.1 will be proved by giving an explicit recipe for ℓ. To discover ℓ, let’s assume it
exists: ℓ(x∗y) = ℓ(x)+ℓ(y) for all x and y in I. Rewriting this in the functional F-notation
instead of the operator ∗-notation,
ℓ(F(x, y)) = ℓ(x) + ℓ(y).
Assuming ℓis diﬀerentiable, let’s diﬀerentiate both sides of this equation with respect to x:
ℓ′(F(x, y))F1(x, y) = ℓ′(x),

<!-- page 4 -->
4
KEITH CONRAD
where we write F1(x, y) for ∂F/∂x (and F2(x, y) = ∂F/∂y). Setting x = u,
ℓ′(y)F1(u, y) = ℓ′(u),
so we solve for ℓ′(y) and integrate:
(2.1)
ℓ(y) =
Z y
u
ℓ′(u)
F1(u, t) dt.
This is a possible formula for the rescaling function ℓ. The constant ℓ′(u), where u is the
∗-identity, is just an undetermined scaling factor that we will simply set equal to 1 once we
return to rigorous deﬁnitions. Incidentally, when we integrated in (2.1), we didn’t introduce
an additive constant since we want ℓ(u) = 0 (the ∗-identity should go the additive identity)
and the integral formula (2.1) already takes care of that. Of more pressing interest is the
validity of dividing by F1(u, t) in (2.1). Why is it never zero?
Lemma 2.2. For all t ∈I, F1(u, t) > 0.
Proof. Diﬀerentiate the associative law, F(F(x, y), z) = F(x, F(y, z)), with respect to x:
F1(F(x, y), z)F1(x, y) = F1(x, F(y, z)).
Setting x = u, the ∗-identity,
(2.2)
F1(y, z)F1(u, y) = F1(u, F(y, z)) = F1(u, y ∗z).
So if F1(u, y) = 0 for some y, then F1(u, y ∗z) = 0 for all z. Choose z = i(y) to get
F1(u, u) = 0. But this is not true:
F(x, u) = x for all x ⇒F1(x, u) = 1 ⇒F1(u, u) = 1.
So F1(u, y) is nonzero for every y. Since it equals 1 at y = u and is continuous, it must
always be positive by the Intermediate Value Theorem.
□
Lemma 2.2 allows us to divide by F1(u, t) for each t ∈I, and we will do this often without
explicitly appealing to the lemma each time.
Since 1/F1(u, t) is continuous in t, hence integrable, we are justiﬁed in making the fol-
lowing deﬁnition, for each x in the interval I:
(2.3)
ℓ(x) def
=
Z x
u
dt
F1(u, t).
By the Fundamental Theorem of Calculus, ℓis diﬀerentiable and
(2.4)
ℓ′(x) =
1
F1(u, x).
In particular, ℓ′(u) = 1.
Using (2.3) as our rescaling function, we now prove Theorem 2.1.
Proof. We need to check (i) ℓ(F(x, y)) = ℓ(x) + ℓ(y) and (ii) ℓ: I →R is a bijection.
For item (i), ﬁx y ∈I. We consider the x-derivatives of
ℓ(F(x, y)),
ℓ(x) + ℓ(y).
By (2.4), the derivative of the ﬁrst function is
ℓ′(F(x, y))F1(x, y) =
F1(x, y)
F1(u, F(x, y)).

<!-- page 5 -->
RELATIVISTIC ADDITION AND GROUP THEORY
5
Does this equal the x-derivative of the second function, namely ℓ′(x) = 1/F1(u, x)? Setting
them equal, we want to consider:
F1(x, y)F1(u, x) ?= F1(u, F(x, y)).
This is just (2.2) with x, y, z relabelled as u, x, y. Therefore ℓ(F(x, y)) and ℓ(x) + ℓ(y) have
equal x-derivatives for all x, which means they diﬀer by an additive constant. Since they
are equal at x = u, the additive constant is 0. This veriﬁes the ﬁrst item: ℓ(F(x, y)) =
ℓ(x) + ℓ(y).
For item (ii), bijectivity, since ℓ′(y) = 1/F1(u, y) > 0 we get ℓis increasing, hence
injective. To show surjectivity, note ℓ(I) is an interval by continuity. Choose x ∈I, x ̸= u.
Since ℓ(x) + ℓ(i(x)) = ℓ(x ∗i(x)) = ℓ(u) = 0, ℓ(x) and ℓ(i(x)) have opposite sign. For a
positive integer n,
ℓ(
n times
z
}|
{
x ∗· · · ∗x) = nℓ(x),
ℓ(
n times
z
}|
{
i(x) ∗· · · ∗i(x)) = nℓ(i(x)),
As n →∞, one tends to ∞, the other to −∞. Since ℓ(I) is an interval, we must have
ℓ(I) = R.
□
Corollary 2.3. When x ∗y = F(x, y) in Theorem 2.1 has continuous partial derivatives,
it is commutative.
Proof. Commutativity was never used in the proof of Theorem 2.1, so commutativity of
addition on R implies commutativity of ∗on I.
□
Remark 2.4. Without using diﬀerentiability, it can be shown that every continuous group
law ∗on an open interval I has the form x∗y = f(f−1(x)+f−1(y)) for some homeomorphism
f : R →I.2 In particular, every continuous group law on I is commutative.
3. Examples
Let’s look at some examples, to see which functions rescale various group laws on an
interval to the additive group of all real numbers.
Example 3.1. If F(x, y) = x + y on I = R, then u = 0, F1(0, x) = 1, and
ℓ(x) =
Z x
0
dt = x.
Example 3.2. If F(v, w) = v⊕w =
v + w
1 + vw/c2 on (−c, c), then u = 0, F1(0, v) = 1−v2/c2,
and
ℓ(v) =
Z v
0
dt
F1(0, t)
= c2
Z v
0
dt
c2 −t2
= c
2
Z v
0

1
c −t +
1
c + t

dt
= c
2 log
1 + v/c
1 −v/c

.
2This is a special case of Hilbert’s Fifth Problem.

<!-- page 6 -->
6
KEITH CONRAD
This is the same as the rescaling function ψ(v) we met at the beginning, up to a factor of c.
Of course if the rescaling function ℓ(x) in Theorem 2.1 is multiplied by a nonzero constant,
it has the same relevant properties (except ℓ′(u) ̸= 1.)
The following table, where vrel
PR is vPR computed according to the relativistic formula
(1.1), gives in the last column the diﬀerence between classical and relativistic formulas for
vPR. Note there is signiﬁcant relative error not only in the ﬁrst row, when both vPQ and vQR
are substantial fractions of the speed of light, but even in the second and third rows, when
only vPQ is near c. In the last row, the fourth column entry is about .5625vQR = (9/16)vQR.
vPQ
vQR
vrel
PR
(vPQ + vQR) −vrel
PR
(3/4)c
(1/2)c
(10/11)c
.341c
(3/4)c
(1/100)c
.75434c
.00566c
(3/4)c
(1/1000)c
.750437c
.000563c
For v, w ∈(−c, c), take v to be ﬁxed and think of v ⊕w as a function of w.
Set
h(w) = v ⊕w = (v + w)/(1 + vw/c2). For w/c small, a Taylor expansion of h(w) at w = 0
yields
v ⊕w ≈h(0) + h′(0)w = v +

1 −v2
c2

w.
If not just w/c is small, but also v/c is small, then the coeﬃcient of w is about 1, so
v ⊕w ≈v + w. If v/c is not small, e.g., v = (3/4)c, then we see a deviation from the
classical addition formula v + w by an error of around (v/c)2w. This explains the error
≈(9/16)vQR in the table above, where v = (3/4)c and 9/16 = (3/4)2.
Example 3.3. As a ﬁnal example, consider F(x, y) = xy on I = (0, ∞). This is the group
of positive real numbers under multiplication. (The multiplicative group of non-zero real
numbers, rather than just the positives, is not an interval. Where does the proof of Theorem
2.1 break down if we try to apply it to all non-zero reals?) Here u = 1 and F1(1, x) = x,
so Theorem 2.1 tells us that a rescaling function that converts multiplication on (0, ∞) to
addition on R is
ℓ(x) =
Z x
1
dt
F1(1, t) =
Z x
1
dt
t = log x.
Of course we already knew that log(xy) = log x + log y, but it is interesting to see how we
have rediscovered the logarithm by applying calculus to algebra.
Our discussion here has been entirely one-dimensional. In three dimensions, velocities and
reference frames are no longer collinear, and the relativistic formula for velocity addition is
rather complicated. See https://en.wikipedia.org/wiki/Velocity-addition formula.
Appendix A. Technical remarks
We want to give a more conceptual perspective on the way ℓ(x) in Theorem 2.1 is related
to the structure of the group law ∗on I. First of all, since ℓ: I →R is a bijection, and thus
invertible, we can apply ℓ−1 to both sides of ℓ(x ∗y) = ℓ(x) + ℓ(y) to see that
(A.1)
x ∗y = ℓ−1(ℓ(x) + ℓ(y)).
So the group law ∗can be reconstructed from ℓand ordinary real addition.
By Corollary 2.3, F(x, y) = F(y, x), and diﬀerentiating both sides of this formula with
respect to x shows F1(x, y) = F2(y, x) for all x, y ∈I. Since ℓis determined by the function

<!-- page 7 -->
RELATIVISTIC ADDITION AND GROUP THEORY
7
F1(u, t) (see 2.3), and the operation x ∗y is determined by ℓ(see A.1), we see the operation
∗is encoded in the function F1(u, t) = F2(t, u).
Now we take a look at Taylor expansions. The function F1(u, x) appears in the ﬁrst term
of the Taylor expansion at y = u of x ∗y = F(x, y) for small y:
(A.2)
x ∗y = F(x, y) ≈F(x, u) + F2(x, u)(y −u) = x + F1(u, x)(y −u).
Since F1(u, u) = 1, for x and y near u we get from (A.2) that x ∗y ≈x + y −u. Therefore
x ∗y −u ≈(x −u) + (y −u).
If we change variables to make 0 the ∗-identity, then this says ∗is approximately just
addition when both variables are small. However, for y near u and x not-so-near u there
is a deviation of x ∗y from the simple law x + y, measured by the function F1(u, x). This
deviation for all x and y near u has been used to reconstruct the operation x ∗y for all
x and all y. That is, the local structure of ∗near the identity completely determines the
global group law.
If you know about diﬀerential forms, then the following is of interest. Another way of
stating (2.2) is in terms of the diﬀerential form ω = dt/F1(u, t). For each z ∈I we have the
function τz : I →I given by right translation by z: τz(x) = F(x, z). This induces a map
τ ∗
z on diﬀerential forms on I, and (2.2) says τ ∗
z ω = ω. In other words, ω is a ∗-invariant
diﬀerential form, and ℓ(x) =
R x
u ω is the integral of this ∗-invariant diﬀerential form along
the path from the identity element to x. This description of the function ℓties it more
closely to the group structure than (2.3) alone suggests.
Appendix B. Deriving relativistic kinetic energy and momentum
When a particle of mass m and velocity v moves along a line, it has a kinetic energy
K = 1
2mv2 and a momentum p = mv. These are formulas from classical mechanics. The
relativistic formulas for kinetic energy and momentum of a particle with mass m moving
along a line at velocity v look quite diﬀerent from their classical versions:
(B.1)
K =
mc2
p
1 −v2/c2 −mc2,
p =
mv
p
1 −v2/c2 .
Taking power series expansions at v = 0, the ﬁrst nonzero term in each formula is 1
2mv2 and
mv respectively, so the kinetic energy and momentum formulas in classical mechanics are
limiting versions of the relativistic formulas when v ≪c. Using arguments from [4] we will
derive the relativistic formulas (B.1), in the sense that we will show these are reasonable
deﬁnitions for kinetic energy and momentum in relativity.
Assume a particle moving along a line with velocity v has a “kinetic energy” K(v) and
a “momentum” p(v). How should these be related to each other? In classical mechanics
Newton’s second law says F = dp/dt.
Also in classical mechanics, the work done on
a particle by a force F over a distance dx is equal to both F(x)dx and dK (change in
kinetic energy of the particle over the distance dx). We assume all of this remains true
relativistically, so
(B.2)
dK = F(x)dx = dp
dt dx = dx
dt dp = v dp.
We will come back to this equation after we carry out a thought experiment to ﬁnd another
relation between the unknown K(v) and p(v).

<!-- page 8 -->
8
KEITH CONRAD
Suppose two particles P and Q are moving along a line with ﬁxed velocities vP and vQ
relative to an observer, and after undergoing an elastic collision their velocities measured
by that observer change to evP and evQ. If the energy of the system of these two particles is
to be the same before and after the collision (conservation of energy) then we require
(B.3)
KP (vP ) + KQ(vQ) = KP (evP ) + KQ(evQ),
where KP and KQ are the kinetic energies of P and Q.
Velocity is a relative notion. If the observer we already discussed is moving at velocity
w ̸= 0 with respect to a second observer (w could be positive or negative) then the second
observer initially measures the velocities of the particles as vP ⊕w and vQ ⊕w and later
measures them as evP ⊕w and evQ⊕w. The principle of relativity says the laws of physics, like
conservation of energy, should be the same for two observers moving at constant velocity
relative to each other, so an analogue of (B.3) should be true for the second observer:
(B.4)
KP (vP ⊕w) + KQ(vQ ⊕w) = KP (evP ⊕w) + KQ(evQ ⊕w).
For our unknown kinetic energy function K, we’ll form the Taylor expansion of K(v ⊕w)
around w = 0 and pay attention to the ﬁrst two terms. Writing v⊕w = (v+w)/(1+vw/c2)
in functional form as G(v, w), so G(v, w) = (v + w)/(1 + vw/c2),
K(v ⊕w) = K(G(v, w)) = K(G(v, 0)) + ∂K(G(v, w))
∂w

w=0
w + O(w2)
and the chain rule implies ∂K(G(v, w))/∂w = K′(G(v, w))(∂G/∂w) = K′(G(v, w))G2(v, w).
Therefore
K(v ⊕w) = K(G(v, 0)) + K′(G(v, 0))G2(v, 0)w + O(w2)
= K(v) + K′(v)

1 −v2
c2

w + O(w2).
Applying this to each term in (B.4), equating the constant terms gives us (B.3), which is
not new. Equating the coeﬃcients of w gives us
(B.5) K′
P (vP )

1 −v2
P
c2

+K′
Q(vQ)
 
1 −
v2
Q
c2
!
= K′
P (evP )

1 −ev2
P
c2

+K′
Q(evQ)
 
1 −
ev2
Q
c2
!
.
Setting f(v) = K′(v)(1 −v2/c2), equation (B.5) says
fP (vP ) + fQ(vQ) = fP (evP ) + fQ(evQ),
which is a conversation law for the system of particles P and Q. Having already introduced
a conversation of energy in (B.3), we deﬁne f(v) to be relativistic momentum so that (B.5)
can be called conversation of momentum. Having called this momentum, we should write
it as p(v) instead of f(v), so set
(B.6)
p(v) = K′(v)

1 −v2
c2

= dK
dv

1 −v2
c2

.
This is the desired second relation between K(v) and p(v) (really it is a deﬁnition of p(v)).
Feeding (B.2) into this,
p(v) = v dp
dv

1 −v2
c2

,

<!-- page 9 -->
RELATIVISTIC ADDITION AND GROUP THEORY
9
which can be rearranged in physicist’s style to
dp
p =
dv
v(1 −v2/c2).
Decomposing the right side into partial fractions,
dp
p =
1
v + 1
2c
1
1 −v/c −1
2c
1
1 + v/c

dv.
Forming antiderivatives,
log |p| = log |v| −1
2 log
1 −v
c
 −1
2 log
1 + v
c
 + const. = log

v
p
1 −v2/c2
 + const.,
so
(B.7)
p(v) =
±econst.v
p
1 −v2/c2
The ﬁrst nonzero term in the Taylor expansion of the right side at v = 0 is ±econst.v, so for
consistency with classical mechanics the coeﬃcient of v in the numerator of (B.7) must be
the particle’s mass. (Thus mass arises from a constant of integration.) This is why we set
relativistic momentum to be p(v) = mv/
p
1 −v2/c2, which is the second formula in (B.1).
Feeding the formula for p(v) into (B.6), we proceed to solve for K(v):
mv
p
1 −v2/c2 = dK
dv

1 −v2
c2

=⇒dK
dv =
mv
(1 −v2/c2)3/2 = d
dv
 
mc2
p
1 −v2/c2
!
.
Therefore
(B.8)
K(v) =
mc2
p
1 −v2/c2 + const.
Since kinetic energy is the “energy of motion” we want K(0) = 0, so we need the constant
in (B.8) to be −mc2 and we are led to set
K(v) =
mc2
p
1 −v2/c2 −mc2,
which is the ﬁrst formula in (B.1). That we have to subtract mc2 to get the energy a particle
has when v ̸= 0 suggests treating mc2 as the intrinsic energy in the particle before it moves
at all. This is one way of interpreting Einstein’s famous equation E = mc2.
References
[1] A. Einstein, Zur Elektrodynamik bewegter K¨orper (On the Electrodynamics of moving bodies),
Annalen der Physik 17 (1905), 891–921. URL https://onlinelibrary.wiley.com/doi/10.1002/
andp.19053221004 (original), URL https://www.fourmilab.ch/etexts/einstein/specrel/www/ (Eng-
lish translation).
[2] A. Einstein, Ist die Tr¨agheit eines K¨orpers von seinem Energieinhalt abh¨angig?
(Does the in-
ertia of a body depend on its energy content?), Annalen der Physik 18 (1905), 639–641. URL
https://myweb.rz.uni-augsburg.de/∼eckern/adp/history/einstein-papers/1905 18 639-641.pdf
(original), URL https://www.fourmilab.ch/etexts/einstein/E mc2/e mc2.pdf (English translation).
[3] M. M. Schiﬀer and L. Bowden, “The Role of Mathematics in Science,” Math. Assoc. America, Washing-
ton, DC, 1984.
[4] S. Sonego and M. Pin, Deriving relativistic momentum and energy, Eur. J. Phys. 26 (2005), 33–45. URL
http://arxiv.org/pdf/physics/0402024.pdf.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*