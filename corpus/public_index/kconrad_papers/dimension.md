# Dimension

> **Source**: https://kconrad.math.uconn.edu/blurbs/dimension.pdf  
> **Author**: Keith Conrad  
> **Topic**: linear_algebra  
> **License**: Public educational resource (link index only for original PDF)

---

<!-- page 1 -->
THE DIMENSION OF A VECTOR SPACE
KEITH CONRAD
1. Introduction
This handout is a supplementary discussion leading up to the deﬁnition of dimension of
a vector space and some of its properties. We start by deﬁning the span of a ﬁnite set of
vectors and linear independence of a ﬁnite set of vectors, which are combined to deﬁne the
all-important concept of a basis.
Deﬁnition 1.1. Let V be a vector space over a ﬁeld F. For any ﬁnite subset {v1, . . . , vn}
of V , its span is the set of all of its linear combinations:
Span(v1, . . . , vn) = {c1v1 + · · · + cnvn : ci ∈F}.
Example 1.2. In F 3, Span((1, 0, 0), (0, 1, 0)) is the xy-plane in F 3.
Example 1.3. If v is a single vector in V then
Span(v) = {cv : c ∈F} = Fv
is the set of scalar multiples of v, which for nonzero v should be thought of geometrically
as a line (through the origin, since it includes 0 · v = 0).
Since sums of linear combinations are linear combinations and the scalar multiple of a
linear combination is a linear combination, Span(v1, . . . , vn) is a subspace of V . It may not
be all of V , of course.
Deﬁnition 1.4. If {v1, . . . , vn} satisﬁes Span({v1, . . . , vn}) = V , that is, if every vector in
V is a linear combination from {v1, . . . , vn}, then we say this set spans V or it is a spanning
set for V .
Example 1.5. In F 2, the set {(1, 0), (0, 1), (1, 1)} is a spanning set of F 2. It has some
redundancy in it, since removing any one of the vectors leaves behind a spanning set, so
remember that spanning sets may be larger than necessary.
Deﬁnition 1.6. A ﬁnite subset {w1, . . . , wm} of V is called linearly independent when the
vanishing of a linear combination only happens in the obvious way:
c1w1 + · · · + cmwm = 0 =⇒all ci = 0.
The importance of this concept is that a linear combination of linearly independent
vectors has only one possible set of coeﬃcients:
(1.1)
c1w1 + · · · + cmwm = c′
1w1 + · · · + c′
mwm =⇒all ci = c′
i.
Indeed, subtracting gives P(ci −c′
i)wi = 0, so ci −c′
i = 0 for all i by linear independence.
Thus ci = c′
i for all i.
1

<!-- page 2 -->
2
KEITH CONRAD
If a subset {w1, . . . , wm} of V is not linearly independent, it is called linearly dependent.
What does this condition really mean? Well, to be not linearly independent means there is
some set of coeﬃcients c1, . . . , cm in F not all zero such that
(1.2)
c1w1 + · · · + cmwm = 0.
We don’t know which ci is not zero. If c1 ̸= 0 then we can collect all the other terms except
c1w1 on the other side and multiply by 1/c1 to obtain
w1 = −c2
c1
w2 −· · · −cm
c1
wm
Thus w1 is a linear combination of w2, . . . , wm. Conversely, if w1 = a2w2 + · · · + amwm is
linear combination of w2, . . . , wm then w1 −a2w2 −· · · −amwm is a linear combination of
all the w’s that vanishes and the coeﬃcient of w1 is 1, which is not zero. Similarly, if ci ̸= 0
in (1.2) then we can express wi as a linear combination of the other wj’s, and conversely
if wi is a linear combination of the other wj’s then we obtain a linear combination of all
the w’s that vanishes and the coeﬃcient of wi is 1, which is not zero. We have proved the
following important result.
Theorem 1.7. A ﬁnite subset {w1, . . . , wm} in a vector space is linearly dependent precisely
when some wi is a linear combination of the rest.
Spanning sets for V and linearly independent subsets of V are in some sense opposite
concepts:
• Any subset of a linearly independent subset is still linearly independent, but this
need not be true of spanning sets.
• Any superset of a spanning set for V is still a spanning set for V , but this need not
be true of linearly independent subsets.
Deﬁnition 1.8. A ﬁnite subset of V that is linearly independent and a spanning set is
called a basis of V .
Example 1.9. In F 2, the set {(1, 0), (0, 1), (1, 1)} is not a basis since it is linearly dependent:
the third vector is the sum of the ﬁrst two. But if we remove any single vector from this
set then we get a basis of F 2: {(1, 0), (0, 1)}, {(1, 0), (1, 1)}, and {(0, 1), (1, 1)} are each a
basis of F 2. To show each set is a basis we will show it is a spanning set and it is linearly
independent:
(1) For v = (x, y) in V we have v = x(1, 0) + y(0, 1), so {(1, 0), (0, 1)} spans F 2. To
show this set is linearly independent, if x(1, 0) + y(0, 1) = (0, 0) then (x, y) = (0, 0),
so x = 0 and y = 0.
(2) For v = (x, y) in V we have v = (x −y)(1, 0) + y(1, 1), so {(1, 0), (1, 1)} spans
F 2.
To show this set is linearly independent, if x(1, 0) + y(1, 1) = (0, 0) then
(x + y, y) = (0, 0), so x + y = 0 and y = 0. Therefore x = 0 and y = 0.
(3) For v = (x, y) in V we have v = (y −x)(0, 1) + x(1, 1), so {(0, 1), (1, 1)} spans F 2.
It is left to you to check this set is linearly independent.
Our main goal will be to show if V has a basis then all bases of V have the same size,
as we saw in Example 1.9 where we found three bases of F 2 all with size 2. That common
size of every basis will be called the dimension1 of V and we will look at how the dimension
behaves on subspaces.
1Spanning sets, linearly independent sets, and bases can all be extended to inﬁnite sets of vectors, leading
to inﬁnite-dimensional vector spaces, but we focus here on the ﬁnite-dimensional case.

<!-- page 3 -->
THE DIMENSION OF A VECTOR SPACE
3
2. Comparing bases
The following theorem is a ﬁrst result that links spanning sets in V with linearly inde-
pendent subsets.
Theorem 2.1. Suppose V ̸= {0} and it admits a ﬁnite spanning set {v1, . . . , vn}. Some
subset of this spanning set is a linearly independent spanning set.
The theorem says that once there is a ﬁnite spanning set, which could have lots of linear
dependence relations, there is a basis for the space. Moreover, the theorem tells us a basis
can be found within any spanning set at all.
Proof. While {v1, . . . , vn} may not be linearly independent, it contains linearly independent
subsets, such as any one single nonzero vi. Of course, such small linearly independent subsets
can hardly be expected to span V . But consider linearly independent subsets of {v1, . . . , vn}
that are as large as possible. Reindexing, without loss of generality, we can write such a
subset as {v1, . . . , vk}.
For i = k + 1, . . . , n, the set {v1, . . . , vk, vi} is not linearly independent (otherwise
{v1, . . . , vk} is not a maximal linearly independent subset).
Thus there is some linear
relation
c1v1 + · · · + ckvk + civi = 0,
where the c’s are in F are not all of them are 0. The coeﬃcient ci cannot be zero, since
otherwise we would be left with a linear dependence relation on v1, . . . , vk, which does not
happen due to their linear independence.
Since ci ̸= 0, we see that vi is in the span of v1, . . . , vk. This holds for i = k + 1, . . . , n, so
any linear combination of v1, . . . , vn is also a linear combination of just v1, . . . , vk. As every
element of V is a linear combination of v1, . . . , vn, we conclude that v1, . . . , vk spans V . By
its construction, this is a linearly independent subset of V as well.
□
Notice the non-constructive character of the proof.
If we somehow can check that a
(ﬁnite) subset of V spans the whole space, Theorem 2.1 says a subset of this is a linearly
independent spanning set, but the proof is not constructively telling us which subset of
{v1, . . . , vn} this might be.
Theorem 2.1 is a “top-down” theorem. It says any (ﬁnite) spanning set has a linearly
independent spanning set inside of it. It is natural to ask if we can go “bottom-up,” and
show any linearly independent subset can be enlarged to a linearly independent spanning
set. Something along these lines will be proved in Theorem 2.10.
Lemma 2.2. Suppose {v1, . . . , vn} spans V , where n ≥2. Pick any v ∈V . If some vi is a
linear combination of the other vj’s and v, then V is spanned by the other vj’s and v.
For example, if V is spanned by v1, v2, and v3, and v1 is a linear combination of v, v2,
and v3, where v is another vector in V , then V is spanned by v, v2, and v3.
Lemma 2.2 should be geometrically reasonable. See if you can prove it before reading
the proof below.
Proof. Reindexing if necessary, we can suppose it is v1 that is a linear combination of
v, v2, . . . , vn. We will show every vector in V is a linear combination of v, v2, . . . , vn, so
these vectors span V .
Pick any w ∈V . By hypothesis,
w = c1v1 + c2v2 + · · · + cnvn

<!-- page 4 -->
4
KEITH CONRAD
for some ci ∈F.
Since v1 is a linear combination of v, v2, . . . , vn, we feed this linear
combination into the above equation to see w is a linear combination of v, v2, . . . , vn. As w
was arbitrary in V , we have shown V is spanned by v, v2, . . . , vm.
□
The following central technical result relates spanning sets for V and linearly independent
subsets of V . It is called the “exchange theorem” from the process in its proof, which relies
on repeated applications of Lemma 2.2.
Theorem 2.3 (Exchange Theorem). Suppose V is spanned by n vectors, where n ≥1.
Every linearly independent subset of V has at most n vectors.
If you think about linear independence as “degrees of freedom,” the exchange theorem
makes sense. What makes the theorem somewhat subtle to prove is that the theorem bounds
the size of any linearly independent subset once we know the size of one spanning set. Most
linearly independent subsets of V are not directly related to the original choice of spanning
set, so linking the two sets of vectors is tricky. The proof will show how to link linearly
independent sets and spanning sets by an exchange process, one vector at a time.
Proof. First, let’s check the result when n = 1. In this case, V = Fv for some v (that is, V
is spanned by one vector). Two diﬀerent scalar multiples of v are linearly dependent, so a
linearly independent subset of V can have size at most 1.
Now we take n ≥2. We give a proof by contradiction. If the theorem is false, then V
contains a set of n + 1 linearly independent vectors, say w1, . . . , wn+1.
Step 1: We are told that V can be spanned by n vectors. Let’s call such a spanning set
v1, . . . , vn. We also have the n + 1 linearly independent vectors w1, . . . , wn+1 in V . Write
the ﬁrst vector from our linearly independent set in terms of our spanning set:
w1 = c1v1 + c2v2 + · · · + cnvn
for some ci ∈F. Since w1 ̸= 0 (a linearly independent set never contains the vector 0),
some coeﬃcient cj is nonzero. Without loss of generality, we can reindex the v’s so that
c1 is nonzero. Then the above equation can be solved for v1 as a linear combination of
w1, v2, . . . , vn. By Lemma 2.2,
(2.1)
V = Span(w1, v2, . . . , vn).
Notice that we have taken one element from the initial spanning set out and inserted an
element from the linearly independent set in its place, retaining the spanning property.
Step 2: Let’s repeat the procedure, this time using our new spanning set (2.1). Write w2
in terms of this new spanning set:
(2.2)
w2 = c′
1w1 + c′
2v2 + · · · + c′
nvn
for some c′
i in F. We want to use this equation to show w2 can be inserted into (2.1) and one
of the original vectors can be taken out, without destroying the spanning property. Some
care is needed, because we want to keep w1 in the spanning set rather than accidentally
swap it out. (This is an issue that we did not meet in the ﬁrst step, where no new vectors
had yet been placed in the spanning set.)
Certainly one of c′
1, c′
2, . . . , c′
n is nonzero, since w2 is nonzero. But in fact we can say
something a bit sharper: regardless of the value of c′
1, one of c′
2, . . . , c′
n is nonzero. Indeed,
if c′
2, . . . , c′
m are all zero, then w2 = c′
1w1 is a scalar multiple of w1, and that violates linear
independence (as {w1, . . . , wm} is linearly independent, so is the subset {w1, w2}).

<!-- page 5 -->
THE DIMENSION OF A VECTOR SPACE
5
Without loss of generality, we can reindex v2, . . . , vn so it is c′
2 that is nonzero. Then
we can use (2.2) to express v2 as a linear combination of w1, w2, v3, . . . , vn. By another
application of Lemma 2.2, using our new spanning set in (2.1) and the auxiliary vector w2,
it follows that
V = Span(w1, w2, v3, . . . , vn).
Step 3: Now that we see how things work, we argue inductively.
Suppose for some k between 1 and n −1 that we have shown
V = Span(w1, . . . , wk, vk+1, . . . , vn).
(This has already been checked for k = 1 in Step 1, and k = 2 in Step 2, although Step 2 is
not logically necessary for what we do; it was just included to see concretely the inductive
step we now carry out for any k.)
Using this spanning set for V , write
(2.3)
wk+1 = a1w1 + · · · + akwk + ak+1vk+1 + · · · + anvn
with ai ∈F. One of ak+1, . . . , an is nonzero, since otherwise this equation expresses wk+1
as a linear combination of w1, . . . , wk, and that violates linear independence of the w’s.
Reindexing vk+1, . . . , vn if necessary, we can suppose it is ak+1 that is nonzero. Then
(2.3) can be solved for vk+1 as a linear combination of w1, . . . , wk, wk+1, vk+2, . . . , vn. By
Lemma 2.2, using the spanning set {w1, . . . , wk, vk+1, . . . , vn} and the auxiliary vector wk+1,
we can swap wk+1 into the spanning set in exchange for vk+1 without losing the spanning
property:
V = Span(w1, . . . , wk, wk+1, vk+2, . . . , vn).
We have added an new vector to the spanning set and taken one of the original vectors out.
Now by induction (or, more loosely, “repeating this step n −k −1 more times”), we arrive
at the conclusion that
(2.4)
V = Span(w1, . . . , wn).
However, we were starting with n + 1 linearly independent vectors w1, . . . , wn+1, so wn+1
is not in the span of w1, . . . , wn. That contradicts the meaning of (2.4), which says every
vector in V is a linear combination of w1, . . . , wn. We have reached a contradiction, so no
linearly independent subset of V contains more than n vectors, where n is the size of a
spanning set for V .
□
Example 2.4. Consider M3(R), the 3 × 3 real matrices. It is a vector space over R under
matrix addition and the usual multiplication of a matrix by a real number. This vector
space has a 9-element spanning set, namely the 9 matrices with a 1 in one component and
0 elsewhere. Therefore any linearly independent subset of M3(R) has at most 9 elements
in it.
Corollary 2.5. Suppose V ̸= {0} and V admits a ﬁnite basis. Any two bases for V have
the same size.
Proof. Let {v1, . . . , vn} and {v′
1, . . . , v′
m} be bases for V . Treating the ﬁrst set as a spanning
set for V and the second set as a linearly independent subset of V , the exchange theorem
tells us that m ≤n. Reversing these roles (which we can do since bases are both linearly
independent and span the whole space), we get n ≤m. Thus m = n.
□
Deﬁnition 2.6. If V is a vector space over F and V has a ﬁnite basis then the (common)
size of any basis of V is called the dimension of V (over F).

<!-- page 6 -->
6
KEITH CONRAD
Example 2.7. There are obvious bases of the vector spaces Rn and Mn(R): in Rn one
basis is the vectors with 1 in one coordinate and 0 elsewhere, and in Mn(R) one basis is
the matrices with 1 in one entry and 0 elsewhere. Counting the number of terms in a basis,
Rn has dimension n and Mn(R) has dimension n2.
Example 2.8. Treating C as a real vector space, one basis is {1, i}, so C has dimension 2
as a vector space over R.
Example 2.9. The vector space {0} has no basis, or you might want to say its basis is the
empty set. In any event, it is natural to declare the zero vector space to have dimension 0.
Theorem 2.10. Let V be a vector space with dimension n ≥1. Any spanning set has at
least n elements, and contains a basis inside of it. Any linearly independent subset has at
most n elements, and can be extended to a basis of V . Finally, an n-element subset of V is
a spanning set if and only if it is a linearly independent set.
Proof. Since V has a basis of n vectors, let’s pick such a basis, say v1, . . . , vn. We will
compare this basis to the spanning sets and the linearly independent sets in V to draw our
conclusions, taking advantage of the dual nature of a basis as both a linearly independent
subset of V and as a spanning set for V .
If {u1, . . . , uk} is a spanning set for V , then a comparison with {v1, . . . , vn} (interpreted
as a linearly independent subset of V ) shows n ≤k by the exchange theorem. Equivalently,
k ≥n. Moreover, Theorem 2.1 says that {u1, . . . , uk} contains a basis for V . This settles
the ﬁrst part of the theorem.
For the next part, suppose {w1, . . . , wm} is a linearly independent subset of V . A compar-
ison with {v1, . . . , vn} (interpreted as a spanning set for V ) shows m ≤n by the exchange
theorem. To see that the w’s can be extended to a basis of V , apply the exchange process
from the proof of the exchange theorem, but only m times since we have only m linearly
independent w’s. We ﬁnd at the end that
V = Span(w1, . . . , wm, vm+1, . . . , vn),
which shows the w’s can be extended to a spanning set for V . This spanning set contains a
basis for V , by Theorem 2.1. Since all bases of V have n elements, this n-element spanning
set must be a basis itself.
Taking m = n in the previous paragraph shows any n-element linearly independent
subset is a basis (and thus spans V ). Conversely, any n-element spanning set is linearly
independent, since any linear dependence relation would let us cut down to a spanning set
of fewer than n elements, but that violates the ﬁrst result in this proof: a spanning set for
an n-dimensional vector space has at least n elements.
□
3. Dimension of subspaces
Theorem 3.1. If V is an n-dimensional vector space, any subspace is ﬁnite-dimensional,
with dimension at most n.
Proof. This theorem is trivial if V = {0}, so we may assume V ̸= {0}, i.e., n ≥1.
Let W be a subspace of V .
Any linearly independent subset of W is also a linearly
independent subset of V , and thus has size at most n by Theorem 2.10. Choose a linearly
independent subset {w1, . . . , wm} of W where m is maximal. Then m ≤n. We will show
Span(w1, . . . , wm) = W.

<!-- page 7 -->
THE DIMENSION OF A VECTOR SPACE
7
For any w ∈W, the set {w, w1, . . . , wm} has more than m elements, so it can’t be linearly
independent. Therefore there is some vanishing linear combination
aw + a1w1 + · · · + amwm = 0
where a, a1, . . . , am are in F and are not all 0.
If a = 0 then the ai’s all vanish since
w1, . . . , wm are linearly independent. Therefore a ̸= 0, so we can solve for w:
w = −a1
a w1 −· · · −am
a wm.
Thus w is a linear combination of w1, . . . , wm. Since w was arbitrary in W, this shows
the wi’s span W. So {w1, . . . , wm} is a spanning set for W that is linearly independent by
construction. This proves W is ﬁnite-dimensional with dimension m ≤n.
□
Theorem 3.2. If V has dimension n and W is a subspace with dimension n, then W = V .
Proof. When W has dimension n, any basis for W is a linearly independent subset of V
with n elements, so it spans V by Theorem 2.10. The span is also W (by deﬁnition of a
basis for W), so W = V .
□
It is important that throughout our calculations (expressing one vector as a linear com-
bination of others when we have a nontrivial linear combination of vectors equal to 0) we
can scale a nonzero coeﬃcient of a vector to make the coeﬃcient equal to 1. For example,
suppose we tried to do linear algebra over the integers Z instead of over a ﬁeld. Then we
can’t scale a coeﬃcient in Z to be 1 without possibly needing rational coeﬃcients for other
vectors in a linear combination. That suggests results like the ones we have established for
vector spaces over ﬁelds might not hold for “vector spaces over Z.” And it’s true: linear
algebra over Z is more subtle than over ﬁelds. For example, Theorem 3.2 is false if we
work with “vector spaces” over Z. Consider the integers Z and the even integers 2Z. By
any reasonable deﬁnitions, both Z and 2Z should be considered “one-dimensional” over
the integers, where Z has basis {1} and 2Z has basis {2} (since every integer is a unique
integral multiple of 2). But 2Z ⊂Z, so a “one-dimensional vector space over Z” can lie
inside another without them being equal. This is a pretty clear failure of Theorem 3.2 when
we use scalars from Z instead of from a ﬁeld.

---

*Extracted from public PDF using PyMuPDF. Mathematical formulas may be incomplete in text form; see page images for original rendering.*