# Advice on Mathematical Writing

> **Source**: https://kconrad.math.uconn.edu/blurbs/writingtips.pdf
> **Author**: Keith Conrad
> **Topic**: mathematical_writing

<!-- page 1 -->

This handout lists some writing tips when you are preparing a mathematical text. The idea of using examples labeled "Bad" and then "Good" was inspired by this format in [1].

## 1. Notation

(1) Do not begin sentences with a symbol.

- Bad: $2^{\sqrt{2}}$ is irrational.
- Good: The number $2^{\sqrt{2}}$ is irrational.

- Bad: Let $n$ be an even number. $n = 2m$ for some $m \in \mathbf{Z}$.
- Good: Let $n$ be an even number. Thus $n = 2m$ for some $m \in \mathbf{Z}$.
- Good: Let $n$ be an even number, so $n = 2m$ for some $m \in \mathbf{Z}$.

- Bad: One solution is $f(x) = \sin x$. $f(x)$ is periodic.
- Good: One solution is $f(x) = \sin x$. In this case, $f(x)$ is periodic.

(2) If two mathematical symbols are not part of the same mathematical expression then they should not appear next to each other without words or grammatical marks in between them.

- Bad: If $n \neq 0$ $n^2 > 0$.
- Good: If $n \neq 0$ then $n^2 > 0$.

- Bad: Consider $x_k$ $1 \leq k \leq n$.
- Good: Consider $x_k$ for $1 \leq k \leq n$.
- Good: Consider $x_k$ where $1 \leq k \leq n$.
- Good: Consider $x_k$ for $k = 1, \ldots, n$.

(3) When introducing notation, make it fit the context. A lot of the time a choice of notation is just common sense.

- Bad: Let $m$ be a prime.
- Good: Let $p$ be a prime.

- Bad: Let $X$ be a set, and pick an element of $X$, say $t$.
- Good: Let $X$ be a set, and pick an element of $X$, say $x$.

- Bad: Pick two integers, say $a$ and $x$.
- Good: Pick two integers, say $a$ and $b$.
- Good: Pick two integers, say $a$ and $a'$.

(4) Always define new notation (is it a number? a function? of what type?) and be clear about its logical standing.

- Very bad: Since $n$ is composite, $n = ab$.
- Bad: Since $n$ is composite, $n = ab$ for some integers $a$ and $b$.

<!-- page 2 -->

- Good: Since $n$ is composite, $n = ab$ for some integers $a$ and $b$ greater than 1. [*Every* integer is a product, since $n = n \cdot 1$, so writing $n = ab$ alone introduces no constraint whatsoever.]

- Bad: If a polynomial $f(x)$ satisfies $f(n) \in \mathbf{Z}$, does $f(x)$ have integer coefficients?
- Good: If a polynomial $f(x)$ satisfies $f(n) \in \mathbf{Z}$ for every $n \in \mathbf{Z}$, does $f(x)$ have integer coefficients?

(5) Do not give multiple meanings to a variable in a single argument.

- Bad: To show the sum of two even numbers is even, suppose $a$ and $b$ are even. Then $a = 2m$ and $b = 2m$, for some integer $m$. We have $a + b = 4m = 2(2m)$, which is even. [Notice this reasoning shows the sum of any two even numbers is always a multiple of 4, which is nonsense.]
- Good: To show the sum of two even numbers is even, suppose $a$ and $b$ are even. Then $a = 2m$ and $b = 2n$, for some integers $m$ and $n$. We have $a + b = 2m + 2n = 2(m + n)$, which is even.

(6) Avoid overloading meaning into notation.

- Bad: Let $x > 0 \in \mathbf{Z}$.
- Good: Let $x$ be an integer, with $x > 0$.
- Good: Let $x$ be a positive integer.

(7) Remember that $\mathbf{Z}$, $\mathbf{Q}$, $\mathbf{R}$, and $\mathbf{C}$ denote the set of *all* integers, rational numbers, real numbers, and complex numbers. They do not stand for an individual number.

- Bad: Let $\mathbf{C}$ be a complex number.
- Good: Let $z$ be a complex number.

(8) **NEVER** use the logical symbols $\forall$ (for all), $\exists$ (there exists), $\wedge$ (and), and $\vee$ (or) when writing, *except* in a technical paper on logic. Write out what you mean in ordinary language.

- Bad: The conditions imply $a = 0 \wedge b = 1$.
- Good: The conditions imply $a = 0$ and $b = 1$.

- Bad: If $\exists$ a root of the polynomial then there is a linear factor.
- Good: If there is a root of the polynomial then there is a linear factor.

(9) The symbol $\forall$ means "For all" or "For every", not "All" or "Every".

- Bad: $\forall$ square matrices with nonzero determinant are invertible.
- Good: All square matrices with nonzero determinant are invertible.

- Bad: In the complex plane $\forall$ complex number has a square root.
- Good: In the complex plane every complex number has a square root.

- Bad: If the functions agree at three points then they agree at $\forall$ points.
- Good: If the functions agree at three points then they agree at all points.

(10) Avoid silly abbreviations, the misuse of standard notation, or the use of abbreviations that are used strictly on the blackboard (like WLOG, s.t., and iff).

- Bad: When $n$ is $\int$, $2n$ is an even number.
- Good: When $n$ is integral, $2n$ is an even number.
- Good: When $n$ is an integer, $2n$ is an even number.

<!-- page 3 -->

- Bad: Let $z$ be a $\mathbf{C}$.
- Good: Let $z$ be a complex number.
- Good: Choose $z \in \mathbf{C}$.

- Bad: WLOG, we can assume $x > 0$.
- Good: Without loss of generality, we can assume $x > 0$.

- Bad: There is a point $x$ s.t. $f(x) > 0$.
- Good: There is a point $x$ such that $f(x) > 0$.

(11) If a piece of notation is superfluous in your writing then don't use it.

- Bad: Every differentiable function $f$ is continuous.
- Good: Every differentiable function is continuous.
- Good: All differentiable functions are continuous.

- Bad: A square matrix $A$ is invertible when its determinant is not 0.
- Good: A square matrix $A$ is invertible when $\det A \neq 0$.
- Good: A square matrix is invertible when its determinant is not 0.

The difference between the use of $A$ in the Bad example and in the first Good example above is that in the first Good example something is actually done with $A$: we refer to it again in $\det A$. In the Bad example the use of $A$ is superfluous notation.

## 2. Equations and Expressions

(1) Don't confuse the terms *equation* and *expression*. An equation is anything of the form $A = B$. An expression is a mathematical notation of any kind that doesn't involve a relation like equality or inequality. For example, $x^2 - 3x + 4$ is an expression; it is not an equation.

(2) If an equation or expression is important (either for its own sake or because you will refer back to it later) then display the equation on its own line. If you need to refer to it later then make it labeled (as (2.1), (2.2), and so on) on the side. Of course, if you only need to make a reference to a displayed equation or expression immediately before or after it appears, you could avoid a label and say "by the above equation," *etc.*

- Bad: As a special case of the binomial theorem,

$$(x + y)^4 = x^4 + 4x^3 y + 6x^2 y^2 + 4xy^3 + y^4.$$

[suppose several lines of text are here]

By the equation 8 lines up, we see...

- Good: As a special case of the binomial theorem,

$$(2.1) \quad (x + y)^4 = x^4 + 4x^3 y + 6x^2 y^2 + 4xy^3 + y^4.$$

[suppose several lines of text are here]

By equation (2.1), we see...

(3) If a single computation involves several steps, especially more than two, then present the steps in stacked form.

- Bad:

$$(x + 1)^3 = (x + 1)^2(x + 1) = (x^2 + 2x + 1)(x + 1) = x^3 + 3x^2 + 3x + 1.$$

<!-- page 4 -->

- Bad:

$$\begin{aligned} (x + 1)^3 &= (x + 1)^2(x + 1) \\ (x + 1)^3 &= (x^2 + 2x + 1)(x + 1) \\ (x + 1)^3 &= x^3 + 3x^2 + 3x + 1. \end{aligned}$$

- Good:

$$\begin{aligned} (x + 1)^3 &= (x + 1)^2(x + 1) \\ &= (x^2 + 2x + 1)(x + 1) \\ &= x^3 + 3x^2 + 3x + 1. \end{aligned}$$

(4) Equations do not stand by themselves. They appear as part of a sentence and should be punctuated accordingly! If an equation ends a sentence then place a period at the end of the line. If an equation appears in the middle of a sentence then use a comma after the equation if one would naturally pause there. Sometimes no punctuation is needed after the equation.

- Bad: We call $x_0$ a *critical point* of $f$ when $f$ is differentiable and

$$f'(x_0) = 0$$

- Good: We call $x_0$ a *critical point* of $f$ when $f$ is differentiable and

$$f'(x_0) = 0.$$

- Good: When $f$ is differentiable, and $x_0$ satisfies

$$f'(x_0) = 0,$$

we call $x_0$ a *critical point*.

- Good: When $f$ is differentiable, any $x_0$ where

$$f'(x_0) = 0$$

is called a *critical point*.

(That the equation is displayed separately in each case simply serves to highlight its importance to the reader. It could have been included within the main text, and punctuation rules of course apply in the same way. The words "critical point" were set in italics to emphasize that this particular term is being defined. Some books put defined terms in **bold** in the definitions.)

## 3. Parentheses and Commas

(1) Avoid irrelevant parentheses in mathematical expressions.

- Bad: $(x + y)(x - y) = (x^2 - y^2)$. [The parentheses on the right have no purpose.]
- Good: $(x + y)(x - y) = x^2 - y^2$.

- Bad: If 7 is a factor of the product $(a_1 a_2 \cdots a_n)$, then ...
- Good: If 7 is a factor of the product $a_1 a_2 \cdots a_n$, then ...

- Bad: The length is a factor of $(p - 1)$.
- Good: The length is a factor of $p - 1$.

<!-- page 5 -->

- Bad: The Taylor series at 0 for $\log(1 + x)$ is

$$\sum_{n=1}^{\infty} \frac{(-1)^{(n-1)}}{n} x^n.$$

- Good: The Taylor series at 0 for $\log(1 + x)$ is

$$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} x^n.$$

- Good: $(a + b)^2 - (a + c)^2 = b^2 - c^2 + 2ab - 2ac$.
- Good: $(a + b)^2 - (a + c)^2 = (b^2 - c^2) + 2ab - 2ac$. [This example is good *only* if the writer wants the reader to view $b^2 - c^2$ as a single part of the right side.]

(2) Use parentheses to avoid confusing the meaning between a subtraction sign and a negative sign in a mathematical expression.

- Very bad: $(a + b) - c = -ac - bc$. [If you look at the right side then you can see the writer meant for the left side to be the product of $a + b$ and $-c$, but the left side instead looks like "$a$ plus $b$ minus $c$."]
- Bad: $(a + b) \cdot -c = -ac - bc$.
- Good: $(a + b)(-c) = -ac - bc$.

(3) Commas are natural places to pause briefly, but not as fully as a period. If you read something in your head, then you should be able to notice badly placed commas, either because no pause should occur or because a period should be there instead of a comma.

- Bad: The condition we want is, $a = 2b$.
- Good: The condition we want is $a = 2b$.

- Bad: The set is infinite, we pick a large finite subset of it.
- Good: The set is infinite. We pick a large finite subset of it.

(4) While "If ..., then..." is a common phrase, it is bad English to write "Let..., then..." with a comma as the separator.

- Very Bad: Let $n$ be an even number, then $n = 2m$ for some $m \in \mathbf{Z}$.
- Good: Let $n$ be an even number. Then $n = 2m$ for some $m \in \mathbf{Z}$.
- Good: Let $n$ be an even number, so $n = 2m$ for some $m \in \mathbf{Z}$.

## 4. Use Helpful Words

(1) Tell the reader where you are going.

- Good: We will prove this by induction on $n$.
- Good: We will prove this by induction on the dimension.
- Good: We argue by contradiction.
- Good: Now we consider the converse direction.
- Good: But $f(x)$ is actually continuous. To see why, consider...
- Good: The inequality $a \leq b$ is strict: $a < b$. Indeed, if there was equality then...

(2) Use key words to show the reader how you are reasoning. These include since, because, on the other hand, observe, note.

<!-- page 6 -->

At the same time, vary your choice of words to avoid monotonous writing. This may require you to completely rewrite a paragraph.

- Bad: We proved, for any $a$, that if $a^2$ is even, then $a$ is even. Now suppose $a^8$ is even. Since $a^8 = (a^4)^2$, we obtain that $a^4$ is even. Then $a^2$ is even. Then $a$ is even.
- Good: We proved, for any $a$, that if $a^2$ is even, then $a$ is even. Now suppose $a^8$ is even. Then, by successively applying the result we proved to $a^4$, $a^2$, and $a$, we see that $a$ is even.

## 5. Some Comments on English Grammar

(1) We commented in Section 2 about punctuating equations. Punctuate ordinary sentences too: use commas, periods, colons, semicolons, and apostrophes correctly.

Concerning apostrophes, use "it's" only to mean "it is". The word "its", like "his" and "her", refers to possession.

- Bad: It's clear that $f(x)$ has a real root since it's degree is odd.
- Bad: Its clear that $f(x)$ has a real root since its degree is odd.
- Good: It's clear that $f(x)$ has a real root since its degree is odd.
- Good: Since $f(x)$ has odd degree, clearly it has a real root. [Write like this if you can't remember the difference between its and it's.]

- Bad: Its surely true that starting your final draft on the last day will leave its mark in your work.
- Good: It's surely true that starting your final draft on the last day will leave its mark in your work.

(2) Avoid incomplete sentences (sentence fragments) or run-on sentences.

- Bad: How to describe rotations in $\mathbf{R}^3$.
- Good: We will explain how to describe rotations in $\mathbf{R}^3$.

- Bad: The new concept we will use is a Markov chain, it is a process where each new state is determined entirely by the previous state.
- Good: The new concept we will use is a Markov chain. It is a process where each new state is determined entirely by the previous state.
- Good: The new concept we will use is a Markov chain, which is a process where each new state is determined entirely by the previous state.

(3) Verb tenses should be consistent.

- Bad: A probability vector has components that add up to 1. An example was the outcome of coin flips.
- Good: A probability vector has components that add up to 1. An example is the outcome of coin flips.

- Bad: In 1873, Hermite proved that $e$ was transcendental.
- Good: In 1873, Hermite proved that $e$ is transcendental.

The error in that last example was referring to transcendence of $e$ in the past tense. A mathematical fact is not subject to time and should be regarded as being "always valid" and thus described in the present tense.

- Bad: Some day I expect $e + \pi$ will be irrational.
- Good: Some day I expect $e + \pi$ will be proved irrational.

<!-- page 7 -->

(4) Correctly use a noun in the singular or plural, and have associated verbs match.

- Bad: The set of real numbers are uncountable.
- Good: The set of real numbers is uncountable. [Not "are uncountable" because in this sentence it is the *set* that is being called uncountable.]
- Good: The real numbers are uncountable.

(5) Watch your spelling! If you aren't sure of the difference between "its" and "it's" (see the start of this section), "necessary" and "neccessary" (the second choice isn't a word), or "discriminate" and "discriminant," look it up. Note in particular the correct spelling of the following words in math, which are not two words:

- "counterexample" is correct and "counter example" is not,
- "straightforward" is correct and "straight forward" is not.

(Canadian students may use their own flavour of spelling, but non-native English speakers should be careful not to let the grammatical rules of their native language affect their writing in English where those rules are different.)

(6) Avoid repeating yourself with the same long word multiple times in the same sentence or with successive sentences that start with the same phrase.

- Bad: It is possible to show that all possible rational numbers can be enumerated.
- Good: It is possible to show that the rational numbers can be enumerated.

(7) Pay attention to where you start and end paragraphs. Don't end a paragraph with "For example, $\sqrt{2}$ is irrational" and then have the next paragraph explain that fact. Move "For example, $\sqrt{2}$ is irrational" to the start of that next paragraph.

(8) Use parallel structure.

- Bad: The real numbers can be decomposed into rational and irrational numbers, as well as into algebraic numbers and transcendental numbers.
- Good: The real numbers can be decomposed into rational and irrational numbers, as well as into algebraic and transcendental numbers.

(9) Don't repeat yourself unnecessarily. For example, if you tell the reader once that $\pi$ is the ratio of a circle's circumference to its diameter, when you mention $\pi$ later you shouldn't repeat that definition again.

(10) Avoid informal language.

- Bad: It is mind-boggling that most real numbers are transcendental.
- Good: It is surprising that most real numbers are transcendental.
- Good: It is striking that most real numbers are transcendental.

## 6. Types of Mathematical Results

In mathematics, results are labelled as either a theorem, lemma, or corollary. What's the difference?

- A theorem is a main result.
- A lemma is a result whose primary purpose is to be used in the proof of a theorem but which, on its own, is not considered significant or as interesting.
- A corollary is a result that follows from a theorem. It could be a special case of the theorem or a particularly important consequence of it.

<!-- page 8 -->

So theorems stand on their own, a lemma always comes before a theorem, and corollaries always come after a theorem. The order in which these appear, then, is always

$$\text{Lemma}, \quad \text{Theorem}, \quad \text{Corollary}.$$

There is no reason a theorem must have a lemma before it or a corollary after it. But if you have a string of lemmas that don't lead to a theorem, for instance, then it will look strange to anyone experienced with mathematical writing.

Here are two examples. First we give a lemma and a theorem whose proof depends on the lemma.

**Lemma 6.1.** *In the integers, if $d$ is a factor of $a$ and $b$ then $d$ is a factor of $ax + by$ for any integers $x$ and $y$.*

*Proof.* Since $d$ is a factor of both $a$ and $b$, we can write $a = dm$ and $b = dn$ for some integers $m$ and $n$. Then for any $x$ and $y$ we have

$$ax + by = dmx + dny = d(mx + ny),$$

which shows $d$ is a factor of $ax + by$.

**Theorem 6.2.** *If $a$ and $b$ are integers and $ax_0 + by_0 = 1$ for some integers $x_0$ and $y_0$, then $a$ and $b$ have no common factor greater than 1.*

*Proof.* This will be a proof by contradiction. Suppose there is a common factor $d > 1$ of $a$ and $b$. Applying Lemma 6.1 to the particular combination $ax_0 + by_0$, $d$ is a factor of $ax_0 + by_0$, so $d$ is a factor of 1. But there are no factors of 1 that are greater than 1, so we have a contradiction. Therefore $a$ and $b$ have no common factor greater than 1.

Next we give a theorem in linear algebra and a corollary that follows from the theorem.

**Theorem 6.3.** *For any two square matrices $A$ and $B$, $\det(AB) = (\det A)(\det B)$.*

[The proof of this is involved and is not included here.]

**Corollary 6.4.** *An invertible matrix has a nonzero determinant.*

*Proof.* If $A$ is invertible, say of size $n \times n$, then $AB = I_n$ for some matrix $B$. Taking the determinant of both sides, Theorem 6.3 tells us

$$(\det A)(\det B) = \det(I_n) = 1,$$

so $\det A \neq 0$.

Why do we need lemmas at all? Could we call everything a theorem? Yes, but the point of the three different names (lemma, theorem, corollary) is to indicate to the reader how the writer views the comparative standing of the different results.

When referring to a theorem, lemma, or corollary, numbered results get capitalized labels: write "by the previous theorem" and "by the next lemma" but "by Theorem 2.1" and "from Lemma 6.3". The same applies to sections of a paper: write "the next section" but "in Section 2".

Proofs start with *Proof* and end with a symbol such as $\square$. If you want to place a proof that $\sqrt{2}$ is irrational in a proof environment, it should come after an official statement that is being proved, like the following.

**Theorem.** *The number $\sqrt{2}$ is irrational.*

Notice we write "The number $\sqrt{2}$" and not "The $\sqrt{2}$." Even though in English we may say "the square root of 2", that is never written as "the $\sqrt{2}$".

<!-- page 9 -->

Don't put part of a proof within the statement of a theorem. The following is bad.

**Theorem.** *The number $\sqrt{2}$ is irrational, and it can be proved by contradiction.*

## 7. Definitions

In addition to the mathematical results in a paper, terminology that you use may need to be defined for the reader. Remember that a definition is not a theorem or anything like that. It's just a description of a new word, and the word being defined *belongs in italics* (or boldface). Here are two definitions.

**Definition 7.1.** A *geodesic* is a curve that locally minimizes lengths between points.

**Definition 7.2.** When all the elements in a partially ordered set are comparable to each other, we call it a *totally ordered* set.

Here is a bad definition.

**Definition 7.3.** If two sequences $\{a_n\}$ and $\{b_n\}$ converge to $A$ and $B$, respectively, then the *limit* of the sequence $\{a_n + b_n\}$ is $A + B$.

This is not a definition because saying that $\lim_{n \to \infty} (a_n + b_n) = A + B$ is a *result* that needs an explanation. In other words, this definition should be a theorem.

Here is another bad definition.

**Definition 7.4.** A number is *rational* if it is $m/n$ where $m, n \in \mathbf{Z}$ with $n \neq 0$. Rational numbers are closed under addition.

The way "rational" is defined there is correct, but what is incorrect is placing a property of rational numbers (closure under addition) within the environment of the definition. Properties belong after the definition.

Here is yet another bad definition.

**Definition 7.5.** A number $\alpha$ is called *algebraic* if there is a nonconstant polynomial $f(x)$ with rational coefficients such that $f(\alpha) = 0$. For instance, $\sqrt{2}$ is algebraic since it's the root of $f(x) = x^2 - 2$.

The mistake here is placing an example ($\sqrt{2}$ is algebraic) within the environment of the definition. Examples belong after the definition.

## 8. Fonts

Here are a few points about italic and non-italic fonts in mathematical writing:

- Single-letter variables are set in italics: $a$, $b$, $M$, $x$, and $y$. An example: "Let $p$ be a prime", not "Let p be a prime". Pay attention to what you're writing so that any time an individual mathematical letter appears in the middle of regular text you recognize it has to be in italics (math mode in LaTeX).

The quadratic formula is not

$$\frac{-\text{b} \pm \sqrt{\text{b}^2 - 4\text{ac}}}{2\text{a}}$$

but rather

$$\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$

<!-- page 10 -->

If you typeset a formula in LaTeX and put the entire formula in a single math mode, those individual letters will be set in italics automatically.

- Single function letters are also in italics, like $f(x)$ and $e^x$, not f(x) or e$^x$ (yuck!). The Fibonacci numbers are written as $F_n$, not as F$_n$ or (worse) F$_\text{n}$.

- Numbers are *never* in italics: $x^2 - 3x + 1$ should be $x^2 - 3x + 1$, $a \neq 0$ should be $a \neq 0$, and *If $p$ is the prime from Theorem 2.1, then ...* should be *If $p$ is the prime from Theorem 2.1, then ....* Italic numbers look awful and should be avoided in all circumstances. (Some disagree with this universal dictum, but at the very least never use italic numbers in mathematical formulas.)

- The statement of a lemma, theorem, or corollary is typeset in italics; in LaTeX there are special lemma, theorem, and corollary environments in which text is italicized automatically, so use those. Do *not* directly force italic text to make a theorem-like environment.

- Traditional functions whose label uses several letters are written in non-italic font: $\sin \theta$, $\cos \alpha$, and $\log t$, not $sin\,\theta$, $cos\,\alpha$, or $log\,t$. In LaTeX there are special function commands that keep such function labels in non-italic font automatically, even in theorem-like environments.

- Definitions and examples should not be in italics, except for a term that is being defined. See the previous section for illustrations of this.

You should open up a math book and notice this traditional way of typesetting if you were not explicitly aware of it before.

## 9. LaTeX Tips

Many questions about LaTeX have already been asked and answered online: search on [tex.stackexchange](https://tex.stackexchange.com) or let Google lead you there with suitable keywords.

Here are a few further tips.

- When typesetting a URL, if you need to use % or an underscore \_ or $\sim$ (the last one can disappear if you are not careful), find out how to make it appear properly from [tex.stackexchange](https://tex.stackexchange.com), where people have already asked about this.

- LaTeX does *not* typeset left double quotes properly if you're not careful: if you use the double quotes key around both sides of the word *here* then you'll get "here" instead of "here". To get left double quotes, type two left single quotes using the left quote key in the **upper left** part of the keyboard (to the left of the "1" key).

- Multiplication is indicated by $\cdot$ or juxtaposition (placing items next to each other): $x \cdot y$ or $xy$. In limited circumstances you could also use $\times$, but never use $x$ or * for multiplication.

## References

[1] D. E. Knuth, T. Larrabee, P. M. Roberts, "Mathematical Writing," Math. Assoc. America, 1989. Available online at http://tex.loria.fr/typographie/mathwriting.pdf.
