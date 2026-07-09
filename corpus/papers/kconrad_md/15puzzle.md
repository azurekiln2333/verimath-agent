# The 15-Puzzle (and Rubik's Cube)

> **Source**: https://kconrad.math.uconn.edu/blurbs/grouptheory/15puzzle.pdf
> **Author**: Keith Conrad
> **Topic**: group_theory

<!-- page 1 -->

## 1. Introduction

A permutation puzzle is a toy where the pieces can be moved around and the goal is to reassemble the pieces into their beginning state. We will discuss two such puzzles: the 15-puzzle and Rubik's Cube. The purpose here is to see how abstract ideas about permutations (transpositions, signs, and so on) tell us something about concrete toys.

## 2. The 15-Puzzle

The 15-puzzle contains 15 sliding pieces and one empty space. It looks like this:

$$
\begin{array}{|c|c|c|c|}
\hline
1 & 2 & 3 & 4 \\
\hline
5 & 6 & 7 & 8 \\
\hline
9 & 10 & 11 & 12 \\
\hline
13 & 14 & 15 & \\
\hline
\end{array}
\tag{2.1}
$$

After moving the pieces around until they are jumbled pretty thoroughly, the task is to bring the pieces back to the arrangement above.

The original 15-puzzle had removable pieces and the original challenge was to start with 14 and 15 swapped as in (2.2) and slide the pieces around to return to (2.1).

$$
\begin{array}{|c|c|c|c|}
\hline
1 & 2 & 3 & 4 \\
\hline
5 & 6 & 7 & 8 \\
\hline
9 & 10 & 11 & 12 \\
\hline
13 & 15 & 14 & \\
\hline
\end{array}
\tag{2.2}
$$

Today, 15-puzzles are usually sold with the pieces in a plastic or metal casing so they *can't* be removed, but some modern 15-puzzles have removable pieces: see Figure 1 (the last one there is sold by Qiyi).

**Figure 1.** Modern 15-puzzles with removable parts and pieces 14 and 15 are swapped.

<!-- page 2 -->

The 15-puzzle was created in upstate New York and initially manufactured in Hartford and then Boston in the 1870s. In early 1880 it swept across America and other countries. The last article of the December, 1879 issue of the *American Journal of Mathematics*, which was published in April, 1880[^1], was about the mathematics of the 15-puzzle and included the following remarks in a concluding footnote [6, p. 404]:

> The "15" puzzle for the last few weeks [...] may safely be said to have engaged the attention of nine out of ten persons [...]. The principle of the game has its root in what all mathematicians of the present day are aware constitutes the most subtle and characteristic concept of modern algebra.[^2]

Figure 2 is the start of a New York Times article on the 15-puzzle on page 4 of its March 22, 1880 edition. The Mr. Comstock it mentions is Anthony Comstock.

**Figure 2.** Excerpt from 1880 New York Times article about the 15-puzzle.

Many people came forward announcing they could go from (2.2) to (2.1), but either they were unable to demonstrate their winning sequence of moves in public or they misunderstood the challenge itself. Starting in the 1890s, Sam Loyd offered a $1000 prize (worth over $30000 today) for anyone who could show a solution, and it is commonly believed that Loyd invented the puzzle, but that is false.[^3]

Since today's 15-puzzles usually can't have their pieces removed, we consider the original challenge of the puzzle in reverse order: can one start with (2.1) and obtain (2.2)? Loyd's

[^1]: See [5, pp. 66, 67, and 117].
[^2]: The concept of modern algebra referred to here is the distinction between even and odd permutations.
[^3]: See [5] for more history on this puzzle.

<!-- page 3 -->

prize was safe for him to offer because it is impossible to move the pieces between the configurations (2.1) and (2.2) by legal moves. To show that, we will translate the task into a question about multiplying permutations in a symmetric group.

Our first task, which we adapt from [4, Sect. 5.1], is to *interpret* the puzzle's configurations (describe where each piece is located) and the puzzle's moves (describe how positions of pieces change) as permutations so that multiplying a move's permutation and a configuration's permutation gives us the new configuration after applying the move.

Each piece in the puzzle is numbered in a natural way from 1 to 15. To keep track of the empty space, call it piece 16. Each position in the puzzle is also numbered in a natural way from 1 to 16. The same set $\{1, \ldots, 16\}$ can keep track of puzzle pieces and puzzle positions.

**Definition 2.1.** If $C$ is a configuration of the puzzle pieces, including the empty space, view $C$ as a permutation in $S_{16}$ by the rule $C(i) = \text{position of piece } i$, for $1 \le i \le 16$.

If $M$ is a move of the puzzle pieces, view $M$ as a permutation in $S_{16}$ by the rule $M(i) = \text{position where } M \text{ moves the piece in position } i$, for $1 \le i \le 16$.

Different pieces of the puzzle are in different positions and every position is filled by some piece, so $C \colon \{1, \ldots, 16\} \to \{1, \ldots, 16\}$ is a permutation. Similarly, a move sends pieces in different positions to different positions, and each position after a move is filled by a piece from somewhere, so the function $M \colon \{1, \ldots, 16\} \to \{1, \ldots, 16\}$ is a permutation.

**Example 2.2.** If $C$ is the configuration

$$
\begin{array}{|c|c|c|c|}
\hline
8 & 12 & 2 & 5 \\
\hline
11 & 1 & 6 & \\
\hline
7 & 14 & 10 & 15 \\
\hline
9 & 4 & 3 & 13 \\
\hline
\end{array}
$$

then $C$ is described by the permutation

$$
\begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 \\
6 & 3 & 15 & 14 & 4 & 7 & 9 & 1 & 13 & 11 & 5 & 2 & 16 & 10 & 12 & 8
\end{pmatrix},
$$

which has disjoint cycle decomposition[^4] $(1\; 6\; 7\; 9\; 13\; 16\; 8)(2\; 3\; 15\; 12)(4\; 14\; 10\; 11\; 5)$.

**Example 2.3.** The standard configuration (2.1) is described by the identity permutation and the configuration (2.2) is described by the 2-cycle $(14\; 15)$. More generally, $(i\; j)$ in $S_{16}$ describes the configuration where piece $i$ is in position $j$, piece $j$ is in position $i$, and piece $k$ is in position $k$ for $k \ne i, j$.

**Example 2.4.** The puzzle moves

$$
\begin{array}{|c|c|c|c|}
\hline
8 & 12 & \mathbf{2} & \mathbf{5} \\
\hline
11 & 1 & \mathbf{6} & \\
\hline
7 & 14 & 10 & 15 \\
\hline
9 & 4 & 3 & 13 \\
\hline
\end{array}
\quad \leadsto \quad
\begin{array}{|c|c|c|c|}
\hline
8 & 12 & \mathbf{5} & \mathbf{6} \\
\hline
11 & 1 & \mathbf{2} & \\
\hline
7 & 14 & 10 & 15 \\
\hline
9 & 4 & 3 & 13 \\
\hline
\end{array}
\tag{2.3}
$$

and

$$
\begin{array}{|c|c|c|c|}
\hline
6 & 4 & \mathbf{1} & \mathbf{9} \\
\hline
10 & 12 & \mathbf{8} & \\
\hline
2 & 13 & 7 & 5 \\
\hline
14 & 3 & 15 & 11 \\
\hline
\end{array}
\quad \leadsto \quad
\begin{array}{|c|c|c|c|}
\hline
6 & 4 & \mathbf{9} & \mathbf{8} \\
\hline
10 & 12 & \mathbf{1} & \\
\hline
2 & 13 & 7 & 5 \\
\hline
14 & 3 & 15 & 11 \\
\hline
\end{array}
$$

[^4]: We multiply permutations from *right to left*, so $(12)(13) = (132)$. Some references on group theory and permutation puzzles, such as [3] and [4], instead multiply from left to right, saying $(12)(13) = (123)$.

<!-- page 4 -->

are the same move $M$ applied to different configurations of the pieces. It is not done in one step! Both forms of $M$ above come from the following successive one-step moves in the upper right of the puzzle.

$$
\begin{array}{|c|c|}
\hline
2 & 5 \\
\hline
6 & \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
2 & 5 \\
\hline
& 6 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
& 5 \\
\hline
2 & 6 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
5 & \\
\hline
2 & 6 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
5 & 6 \\
\hline
2 & \\
\hline
\end{array}
\tag{2.4}
$$

$$
\begin{array}{|c|c|}
\hline
1 & 9 \\
\hline
8 & \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
1 & 9 \\
\hline
& 8 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
& 9 \\
\hline
1 & 8 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
9 & \\
\hline
1 & 8 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
9 & 8 \\
\hline
1 & \\
\hline
\end{array}
$$

What $M$ does overall is move the piece in position 3 to position 7, the piece in position 7 to position 4, the piece in position 4 to position 3, and nothing else changes, so $M$ as a permutation has $M(3) = 7$, $M(7) = 4$, $M(4) = 3$, and $M(i) = i$ for $i \ne 3, 7, 4$. Thus $M = (374)$. Each step in carrying out $M$ uses piece 16, but $M$ in $S_{16}$ doesn't mention 16.

The following theorem shows that applying a move to a configuration is compatible with multiplication in $S_{16}$ when the move and configuration are both written as permutations.

**Theorem 2.5.** *In the 15-puzzle, applying a move $M$ to a configuration $C$ changes the configuration of the pieces into the product $MC$ when $M$ and $C$ are interpreted as permutations in $S_{16}$.*

*Proof.* Pick $i \in \{1, \ldots, 16\}$. Viewing $M$ and $C$ as elements of $S_{16}$, $(MC)(i) = M(C(i))$. Since $M$ is a move, the number $M(C(i))$ is the position in the puzzle to which $M$ moves the piece in position $C(i)$. Since $C$ is a configuration of the pieces, the number $C(i)$ is the position of piece $i$ in configuration $C$. Therefore $M(C(i))$ is the position to which $M$ moves piece $i$ starting in configuration $C$. That is, $(MC)(i)$ is the position of piece $i$ after applying move $M$ to configuration $C$, for all $i$, so $MC$ is the configuration of the puzzle after applying move $M$ to configuration $C$. $\square$

Since Theorem 2.5 shows the multiplication of a move and a configuration of the 15-puzzle is the new configuration after the move, if we apply moves $M_1, M_2, \ldots, M_r$ in that order to a configuration $C$ then the final configuration of the puzzle is the product $M_r \cdots M_2 M_1 C$.

**Example 2.6.** We saw in Example 2.4 that the move in (2.3) as a permutation is $M = (374)$. The initial configuration $C$ in (2.3), as a permutation, is described in Example 2.2. The product $MC = (3\; 7\; 4)(1\; 6\; 7\; 9\; 13\; 16\; 8)(2\; 3\; 15\; 12)(4\; 14\; 10\; 11\; 5)$ is the 16-cycle

$$
(1\; 6\; 4\; 14\; 10\; 11\; 5\; 3\; 15\; 12\; 2\; 7\; 9\; 13\; 16\; 8).
$$

As a configuration, this says piece 1 is in position 6, piece 6 is in position 4, and so on up to piece 8 being in position 1, which is the final configuration in (2.3).

In each row of (2.4), the four moves affect positions 3, 4, 7, and 8. They are, successively, $(78)$, $(37)$, $(34)$, and $(48)$. Since functions compose from right to left, we consider the product of those transpositions in the order $(48)(34)(37)(78) = (374)(8) = (374)$, which is the permutation $M$ we found for the move in (2.3) at the end of Example 2.4. Multiplying in the opposite order $(78)(37)(34)(48) = (347)$, we don't get $(374)$.

Now we can explain why Sam Loyd's $1000 challenge can have no winner.

**Theorem 2.7.** *It is impossible to pass between (2.1) and (2.2) by sliding the pieces.*

*Proof.* Going from (2.1) to (2.2) and *vice versa* are equivalent. We focus on (2.1) to (2.2).

Each basic move of the 15-puzzle involves an exchange of positions between piece 16 (the empty space) and an actual piece. If pieces in positions $i$ and $j$ are swapped and other

<!-- page 5 -->

pieces stay put, that move is described by the permutation $(i\; j)$ (no matter what pieces are in positions $i$ and $j$). The permutation for the configuration (2.1) is the identity $C = (1)$ and the permutation for the configuration (2.2) is the transposition $C' = (14\; 15)$, so going from (2.1) to (2.2) in the 15-puzzle means that in $S_{16}$ there are some transpositions $\tau_1, \tau_2, \ldots, \tau_r$ of position locations such that $C' = \tau_r \cdots \tau_2 \tau_1 C$. Since $C = (1)$ and $C' = (14\; 15)$ in $S_{16}$,

$$
(14\; 15) = \tau_r \cdots \tau_2 \tau_1.
\tag{2.5}
$$

Because the empty space is in the same location in (2.1) and (2.2), after the moves described by each $\tau_i$ are carried out, the empty space had to move up and down an equal number of times as well as right and left an equal number of times. Since the empty space changes position under each $\tau_i$,[^5] the number of transpositions on the right side of (2.5) is *even*. Therefore the right side of (2.5) is a product of an even number of transpositions, but the left side has an odd number of transpositions. This is a contradiction,[^6] so we are done. $\square$

**Remark 2.8.** A more intuitive approach to Theorem 2.7 is to say each basic move in the puzzle involves piece 16, and if a sequence of moves interchanges piece 16 with pieces $a_1, a_2, \ldots, a_r$ then a more explicit version of (2.5) is $(14\; 15) = (a_r\; 16) \cdots (a_2\; 16)(a_1\; 16)$, with $r$ being even since piece 16 moves an even number of times. That intuition is *not compatible* with Theorem 2.5, where a move is described as a permutation of the underlying *positions* it affects, not as a permutation of the specific numbered *pieces* involved. A succession of moves involving piece 16 is not expressed in Theorem 2.5 as a product of transpositions all involving (position) 16. If we model the effect of the moves in (2.4) as $(6\; 16)(5\; 16)(2\; 16)(6\; 16)$, which is $(256)$, this tells us each piece is *replaced by* the next piece: 2 by 5, 5 by 6, and 6 by 2.

**Corollary 2.9.** *Every movement of pieces in the 15-puzzle starting from the standard configuration (2.1) that brings the empty space back to its original position must be an even permutation of the other 15 pieces.*

*Proof.* Let $\pi$ be the permutation describing the configuration after the movement. Then $\pi$ is also the permutation describing the move from the standard configuration: initially piece $i$ is in position $i$, so $\pi(i)$ is where piece $i$ winds up. Running through the proof of Theorem 2.7, with $(14\; 15)$ replaced by $\pi$, from $\pi(16) = 16$ we get that $\pi$ is an even permutation in $S_{16}$. Since $\pi(16) = 16$, we can view $\pi$ in $S_{15}$. The parity of a permutation in $S_{15}$ is the same as its parity when viewed as a permutation in $S_{16}$ that fixes 16, so $\pi$ is an even permutation of $1, 2, \ldots, 15$. $\square$

The number of permutations of 15 objects is $15! = 1307674368000$. The number of even permutations of 15 objects is $15!/2 = 653837184000$. By Corollary 2.9, $15!/2$ is an upper bound on the number of (legal) positions of the pieces in the 15-puzzle with the empty space in the lower right. Is this bound achieved? Using 3-cycles we'll show the answer is yes.

**Theorem 2.10.** *For $n \ge 3$, $A_n$ is generated by the 3-cycles $(1\; 2\; i)$ for $3 \le i \le n$.*

This is a standard result in group theory and we omit the proof.[^7] It is a refinement of the more widely familiar fact in group theory that $A_n$ is generated by *all* 3-cycles when $n \ge 3$.

Each basic move in the 15-puzzle involves the empty space, and two puzzle moves can't be composed unless the first one leaves the empty space where the second one needs it.

[^5]: This does not mean each $\tau_i$ has the form $(*\; 16)$, since $\tau_i$ is a transposition of position locations, not of piece labels. Compare with $M = (48)(34)(37)(78) = (374)$ at the end of Example 2.6.
[^6]: See Theorem 2.1 in https://kconrad.math.uconn.edu/blurbs/grouptheory/sign.pdf.
[^7]: See Theorem 3.3 in https://kconrad.math.uconn.edu/blurbs/grouptheory/genset.pdf.

<!-- page 6 -->

Each configuration of the 15-puzzle can be modified to have the empty space in position 16, so we focus on moves that *leave the empty space in position 16 before and after the move*. Such moves, as permutations, are a subgroup of $S_{16}$ and in fact $S_{15}$. Call it the 15-puzzle group, denoted as $F$. Its elements are even (Corollary 2.9), so $F$ is a subgroup of $A_{15}$.

**Theorem 2.11.** *The 15-puzzle group $F$ is $A_{15}$.*

*Proof.* We will use Theorem 2.10 in a "coordinate-free" form: $A_{15}$ is generated by 3-cycles involving a common pair of terms. We will use the 3-cycles $(11\; 12\; i)$ instead of $(1\; 2\; i)$.

The move $M = (11\; 12\; 15)$ can be realized as follows, using $i$ in position $i$ for clarity.

$$
\begin{array}{|c|c|}
\hline
11 & 12 \\
\hline
15 & \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
11 & \\
\hline
15 & 12 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
& 11 \\
\hline
15 & 12 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
15 & 11 \\
\hline
& 12 \\
\hline
\end{array}
\leadsto
\begin{array}{|c|c|}
\hline
15 & 11 \\
\hline
12 & \\
\hline
\end{array}
\tag{2.6}
$$

Thus $M \in F$. For each $i \notin \{11, 12, 15, 16\}$, we will find $g_i$ in $F$ carrying the piece in position $i$ to position 15 (so $g_i(i) = 15$) while leaving pieces in positions 11, 12, and 16 fixed. Then $g_i^{-1} M g_i = (g_i^{-1}(11)\; g_i^{-1}(12)\; g_i^{-1}(15)) = (11\; 12\; i)$, so $(11\; 12\; i) \in F$ for all $i \ne 11, 12, 16$.

Starting in the standard configuration (2.1), let $m$ be the move taking the empty space to the inside of the puzzle by exchanging it with 12 and then 11, as shown below.

$$
\begin{array}{|c|c|c|c|}
\hline
1 & 2 & 3 & 4 \\
\hline
5 & 6 & 7 & 8 \\
\hline
9 & 10 & 11 & 12 \\
\hline
13 & 14 & 15 & \\
\hline
\end{array}
\;\xrightarrow{m}\;
\begin{array}{|c|c|c|c|}
\hline
1 & 2 & 3 & 4 \\
\hline
5 & 6 & 7 & 8 \\
\hline
9 & 10 & & 11 \\
\hline
13 & 14 & 15 & 12 \\
\hline
\end{array}
$$

As a permutation in $S_{16}$, $m = (11\; 12\; 16)$. This is not in $F$ since position 16 is not fixed.

Below are two 'tours' that together make the rest of the board pass through the empty space and the 15 in the configuration on the right side above. In the figures below, each tour is highlighted in bold and we use 16 as a label for the empty space. These tours are $16, 7, 3, 2, 1, 5, 9, 13, 14, 15$ on the left and $16, 7, 8, 4, 3, 2, 6, 10, 14, 15$ on the right.

$$
\begin{array}{|c|c|c|c|}
\hline
\mathbf{1} & \mathbf{2} & \mathbf{3} & 4 \\
\hline
\mathbf{5} & \mathbf{6} & \mathbf{7} & 8 \\
\hline
\mathbf{9} & 10 & \mathbf{16} & 11 \\
\hline
\mathbf{13} & \mathbf{14} & \mathbf{15} & 12 \\
\hline
\end{array}
\qquad
\begin{array}{|c|c|c|c|}
\hline
\mathbf{1} & \mathbf{2} & \mathbf{3} & 4 \\
\hline
\mathbf{5} & \mathbf{6} & \mathbf{7} & \mathbf{8} \\
\hline
9 & \mathbf{10} & \mathbf{16} & 11 \\
\hline
13 & 14 & \mathbf{15} & 12 \\
\hline
\end{array}
$$

(I found these in [3, pp. 123--124], which is all about permutation puzzles.) For each $i \ne 11, 12, 16$, one of the tours gives us a move $h_i$ that brings piece $i$ from position $i$ to position 15, by backtracking keeps the empty space 16 in position 11, and doesn't change the pieces 11 and 12 in positions 12 and 16. So as a permutation, $h_i$ fixes 11, 12, and 16, and $h_i(i) = 15$. The 3-cycle $m = (11\; 12\; 16)$ fixes $i$ and 15, so check that the move $g_i = m^{-1} h_i m$ fixes positions 11, 12, and 16 (it lies in $F$), and $g_i(i) = 15$. It follows, as explained earlier, that $(11\; 12\; i) \in F$. As $i$ varies such 3-cycles generate $A_{15}$, so $F = A_{15}$. $\square$

In summary, half the permutations of the pieces 1 to 15 in the 15-puzzle are solvable since $A_{15}$ is generated by 3-cycles with a common pair of terms, like 11 and 12.

**Example 2.12.** We will determine if the configuration

$$
\begin{array}{|c|c|c|c|}
\hline
8 & 7 & 6 & 5 \\
\hline
9 & 3 & 1 & 10 \\
\hline
2 & 11 & 14 & 4 \\
\hline
12 & 15 & 13 & \\
\hline
\end{array}
\tag{2.7}
$$

<!-- page 7 -->

can be reached from (2.1). The permutation for the move from (2.1) to (2.7) sends each $i$ (the piece in position $i$ in (2.1)) to the position of $i$ in (2.7). That is

$$
\begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 \\
7 & 9 & 6 & 12 & 4 & 3 & 2 & 1 & 5 & 8 & 10 & 13 & 15 & 11 & 14
\end{pmatrix},
$$

which when written as a product of disjoint cycles becomes

$$
(1\; 7\; 2\; 9\; 5\; 4\; 12\; 13\; 15\; 14\; 11\; 10\; 8)(3\; 6).
$$

This is a 13-cycle times a 2-cycle. A 13-cycle is an even permutation and a 2-cycle is an odd permutation, so overall this move is an odd permutation. Therefore it is impossible to reach (2.7) from (2.1), or conversely to go from (2.7) to (2.1).

## 3. Rubik's Cube

Nothing like the 19-th century frenzy over the 15-puzzle was seen again until essentially 100 years later, when Rubik's Cube came on the scene in the early 1980s. Its inventor, Erno Rubik, became the first self-made millionaire in the Communist bloc.

It's best if you have a copy of the cube to play with as you read the remaining discussion. We will *not* describe a solution to the cube, although many are on YouTube.[^8] What we will do here is introduce enough notation and terminology to explain how to count the number of solvable positions of Rubik's Cube, much like the number of solvable positions of the 15-puzzle (keeping space 16 in the lower right corner) is $15!/2 = |A_{15}|$.

If you pop out an edge piece by hand on a modern speedcube or with a screwdriver on an older cube (see Figure 3) then all the pieces come out and the center mechanism is revealed (Figure 4). It shows a basic fact about the cube: the 6 center pieces are all attached and no amount of turning will ever change their relative positions.[^9] Because the center pieces always maintain the same relative positions, each central color tells you what color that whole face must be in the solved cube. For instance, if a messed up cube has blue and green as opposite center colors then the solved state of that cube will have blue and green faces opposite each other.

**Figure 3.** Beginning to disassemble an old cube and getting one edge piece out.

There are three kinds of pieces in the cube: 8 corner pieces (each with 3 colors), 12 edge pieces (each having 2 colors) and 6 center pieces (each with one color). See Figure 5. The

[^8]: See https://www.youtube.com/watch?v=7Ron6MN45LY.
[^9]: Here are YouTube videos by Jared Owen showing the internal mechanisms of the original cube and speed cube: https://www.youtube.com/watch?v=bgcScY7CiMs and https://www.youtube.com/watch?v=SBcbiFqz3aU. He made a video about the inside of a $2 \times 2$ cube, which we don't discuss here: https://www.youtube.com/watch?v=AFNh4aARIz8.

<!-- page 8 -->

**Figure 4.** The center mechanism.

number of non-center colored squares is $8 \cdot 3 + 12 \cdot 2 = 48$. When you make a move of the cube, the 3 colors on a corner stay together and the 2 colors on an edge stay together.

**Figure 5.** A corner and edge piece.

Although you can physically rotate the whole cube in space to get a better view, this is not a move: relative positions of each piece stay the same. To discuss constraints on what can be done on a Rubik's Cube, center pieces can be kept in fixed positions (no cube rotations). When holding the cube with one face facing you, the labels of the 6 faces are

- F for Front,
- B for Back,
- L for Left,
- R for Right,
- U for Up,
- D for Down.

See Figure 6. The labels Up/Down are used instead of Top/Bottom to avoid confusion over the meaning of B (Bottom or Back?). I have seen a book on Rubik's Cube that uses the labels Top/Bottom, and calls the Back face the P(osterior) face, but this is uncommon.

**Figure 6.** Face Names.

Below is a diagram of the cube unfolded, taken from [3, p. 72]. (The numbers $1, 2, \ldots, 48$ correspond to non-center squares.) In this standard configuration, square $i$ is in position $i$.

<!-- page 9 -->

$$
\begin{array}{|c|c|c|}
\hline
1 & 2 & 3 \\
\hline
4 & \text{U} & 5 \\
\hline
6 & 7 & 8 \\
\hline
\end{array}
$$

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
9 & 10 & 11 & 17 & 18 & 19 & 25 & 26 & 27 & 33 & 34 & 35 \\
\hline
12 & \text{L} & 13 & 20 & \text{F} & 21 & 28 & \text{R} & 29 & 36 & \text{B} & 37 \\
\hline
14 & 15 & 16 & 22 & 23 & 24 & 30 & 31 & 32 & 38 & 39 & 40 \\
\hline
\end{array}
$$

$$
\begin{array}{|c|c|c|}
\hline
41 & 42 & 43 \\
\hline
44 & \text{D} & 45 \\
\hline
46 & 47 & 48 \\
\hline
\end{array}
$$

The choice of face labels F, B, L, R, U, D are due to D. Singmaster [2, p. 10].[^10] The face labels are used in two ways: to mark each face's center (which does not move), and to denote a quarter-turn clockwise of that face if you look at it head-on in a natural way. If you hold a cube with F in front of you (and U lying above it) then

- F is a quarter-turn of the Front face carrying its top row to R,
- B is a quarter-turn of the Back face carrying its top row to L,
- L is a quarter-turn of the Left face carrying its top row to F,
- R is a quarter-turn of the Right face carrying its top row to B,
- U is a quarter-turn of the Up face carrying its front row to L,
- D is a quarter-turn of the Down face carrying its front row to R.

We call these 6 quarter-turns the *basic* moves of the cube. Using the cube-face diagram above, a tedious verification shows the 6 basic moves are the following elements of $S_{48}$, where for each move $M$, $M(i)$ is the position where $M$ sends $i$ from the standard configuration. (More abstractly, for each configuration, $M(i)$ is the position where $M$ moves the piece in position $i$.)

$$
\begin{aligned}
\text{F} &= (17, 19, 24, 22)(18, 21, 23, 20)(6, 25, 43, 16)(7, 28, 42, 13)(8, 30, 41, 11), \\
\text{B} &= (33, 35, 40, 38)(34, 37, 39, 36)(3, 9, 46, 32)(2, 12, 47, 29)(1, 14, 48, 27), \\
\text{L} &= (9, 11, 16, 14)(10, 13, 15, 12)(1, 17, 41, 40)(4, 20, 44, 37)(6, 22, 46, 35), \\
\text{R} &= (25, 27, 32, 30)(26, 29, 31, 28)(3, 38, 43, 19)(5, 36, 45, 21)(8, 33, 48, 24), \\
\text{U} &= (1, 3, 8, 6)(2, 5, 7, 4)(9, 33, 25, 17)(10, 34, 26, 18)(11, 35, 27, 19), \\
\text{D} &= (41, 43, 48, 46)(42, 45, 47, 44)(14, 22, 30, 38)(15, 23, 31, 39)(16, 24, 32, 40).
\end{aligned}
$$

[^10]: The colors on the cube, for many years, were not the same for different manufacturers. Even the same 6 face colors could appear in different positions: white may be opposite blue on one solved cube but be opposite red on another solved cube. For modern cubes, the placement of all colors are the same.

<!-- page 10 -->

Another natural class of moves is quarter-turns of the three *middle* layers. They can be built from the 6 basic moves since a quarter-turn of a middle layer in one direction is the same as quarter-turns of the two parallel outer layers in the opposite direction, and that is a product of two of the six basic moves above.

From a group-theoretic perspective, understanding all possible configurations of a Rubik's Cube amounts to asking: what subgroup of $S_{48}$ is generated by F, B, L, R, U, D:

$$
\langle \text{F, B, L, R, U, D} \rangle = ???
$$

This set of all products of permutations generated by the 6 moves is called Rubik's group. Can it be written down in terms of simpler known groups? This is comparable to the connection between the arrangements of the pieces in the 15-puzzle and the group $A_{15}$.

Since corner and edge pieces can never occupy each other's positions, thinking about Rubik's group inside $S_{48}$ is not such a great idea. We should consider the corner and edge pieces separately. However, although each move of the cube permutes the 8 corner pieces among themselves and the 12 edge pieces among themselves, there is more information in a move than how it permutes the corner pieces and how it permutes the edge pieces: each corner and edge piece has an *orientation*, describing how it fits into its current position.

We call a position that a corner or edge piece can be placed in a *cubicle*. There are 20 of them: 8 corner cubicles and 12 edge cubicles. A corner cubicle can be filled by a corner piece in 3 ways, while an edge cubicle can be filled by an edge piece in 2 ways. These different possibilities are called the orientations of the (corner or edge) piece. We call the pieces in the solved state of the cube 'oriented.' How can we decide if a piece is oriented or not on a scrambled cube?

Each corner piece of a scrambled cube has one color matching the center color of the U or D face (why can't all its colors be F, B, L, or R?). *Mark* that face of the corner. On the edge pieces having a color matching the U or D center, *mark* that face of the edge. On the edge pieces not having a color matching the U or D center, there will be a color matching the F or B center. *Mark* that face. We have marked one face of each corner and each edge on a scrambled cube.

If you play with the cube, remembering not to change the location of the center pieces (*e.g.*, don't rotate the whole cube in space), we can assign a corner piece and edge piece of a scrambled cube an *orientation value* that is in $\mathbf{Z}/(3)$ for corners and in $\mathbf{Z}/(2)$ for edges according to the following rules:

- If a *corner* piece has its marked color on the U or D face, give that piece orientation value 0. (A corner piece is never in the middle layer.) If a corner piece has its marked color not on its U or D face, count how many *clockwise* rotations or that corner (in your mind!) bring the marked color to the U or D face: 1 or 2. Give the piece orientation value 1 or 2, respectively. (Since 2 clockwise rotations is 1 counterclockwise rotation, you could treat 2 as $-1$.) In all cases, an orientation value $n$ on a corner piece means a *clockwise* rotation by $n$ turns puts the marked color of the corner piece on the U or D face; $n$ only matters mod 3. For a physical demonstration, watch https://www.youtube.com/watch?v=o-RxLzRe2YE from 7:53 to 9:50.
- If an *edge* piece is in the upper or lower layer of the cube and has its marked color on the U or D face, give that piece orientation value 0. If the piece is in the middle layer and its marked color is on the F or B face, give the piece orientation value 0. In other cases give the piece orientation value 1. This value only matters mod 2.

<!-- page 11 -->

Instead of viewing a move of the cube in $S_{48}$ (as a permutation of the squares) we can view it as a permutation of the 8 corner pieces, keeping track of the 3 orientation values for each corner piece, and a permutation of the 12 edge pieces, keeping track of the 2 orientations of each edge piece. (That is still $8 \times 3 + 12 \times 2 = 48$ pieces of information.) Give the corner pieces a definite labeling $1, 2, \ldots, 8$ and the edge pieces a definite labeling $1, 2, \ldots, 12$. Then each move of the cube corresponds to a choice of 4-tuple

$$
(\pi, \rho, \mathbf{v}, \mathbf{w}) \in S_8 \times S_{12} \times (\mathbf{Z}/(3))^8 \times (\mathbf{Z}/(2))^{12}.
\tag{3.1}
$$

Which 4-tuples $(\pi, \rho, \mathbf{v}, \mathbf{w})$ from this set really correspond to moves on the cube? There are a few constraints. First of all, as a permutation on the pieces, each move among F, B, L, R, U, D is a 4-cycle on the 4 corner pieces it moves and a 4-cycle on the 4 edge pieces it moves. A 4-cycle is odd, so each basic move gives an odd permutation in $S_8$ and in $S_{12}$. This might sound strange: odd permutations do not form a group! However, let's think about the fact that *both* of the permutations of corner and edge pieces in F, B, L, R, U, or D are odd. When composed, permutations with this feature will have both odd or both even effects on the corner and edge pieces. In other words, two permutations $\pi \in S_8$ and $\rho \in S_{12}$ coming from the same move of the cube satisfy

$$
\text{sgn}(\pi) = \text{sgn}(\rho).
\tag{3.2}
$$

As for the orientations, a computation shows that each basic move does not change the sum of the coordinates in the orientation vectors $\mathbf{v}$ and $\mathbf{w}$ for a particular arrangement of the pieces. Thus, since a solved cube has both orientation vectors equal to $\mathbf{0}$, an actual move of the cube must have

$$
\sum_{i=1}^{8} v_i \equiv 0 \bmod 3, \quad \sum_{j=1}^{12} w_j \equiv 0 \bmod 2.
\tag{3.3}
$$

(The first formula in (3.3) tells us that in a move of the cube, we can't change the orientation of a single corner piece without changing something else. Similarly, the second formula in (3.3) tells us no move of the cube can change the orientation of a single edge piece without changing something else. A single corner rotation would change $\sum_{i=1}^8 v_i \bmod 3$ by $\pm 1 \bmod 3$, which doesn't preserve the condition $\sum_{i=1}^8 v_i \equiv 0 \bmod 3$.)

The conditions (3.2) and (3.3) carve out the following subset of (3.1):

$$
\left\{ (\pi, \rho, \mathbf{v}, \mathbf{w}) : \text{sgn}\,\pi = \text{sgn}\,\rho,\; \sum_{i=1}^{8} v_i \equiv 0 \bmod 3,\; \sum_{j=1}^{12} w_j \equiv 0 \bmod 2 \right\}.
\tag{3.4}
$$

Every arrangement of the pieces in Rubik's Cube that can be reached from the solved state lies in (3.4). It turns out that, conversely, every 4-tuple in (3.4) is a solvable arrangement of the pieces in Rubik's Cube. This is shown in [1, p. 42], which gives an (inefficient) algorithm to solve the cube starting from an arbitrary configuration satisfying (3.4).[^11] Therefore the number of arrangements of the pieces in Rubik's Cube is the size of (3.4). How large is (3.4)? Among all pairs of permutations $(\pi, \rho) \in S_8 \times S_{12}$, *half* have $\text{sgn}\,\pi = \text{sgn}\,\rho$. Among the 8-tuples $\mathbf{v} \in (\mathbf{Z}/(3))^8$, *one-third* have the sum of coordinates equal to 0. Among the 12-tuples $\mathbf{w} \in (\mathbf{Z}/(2))^{12}$, *half* have the sum of coordinates equal to 0. So the total number

[^11]: It was shown in 2010, by a brute force search with a computer, that any scrambled cube can be solved in at most 20 quarter-turns or half-turns. See http://www.cube20.org/.

<!-- page 12 -->

of arrangements of the pieces in Rubik's Cube that you get by mixing it up without taking it apart is

$$
\frac{8! \, 12! \, 3^8 \, 2^{12}}{2 \cdot 3 \cdot 2} = 2^{27} 3^{14} 5^3 7^2 11 = 43252003274489856000 \approx 4.3 \cdot 10^{19}.
\tag{3.5}
$$

This size is impressive, but its magnitude should not be construed as a reason that Rubik's Cube is hard to solve. After all, the letters of the alphabet can be arranged in $26! \approx 4.03 \cdot 10^{26}$ ways but it is very easy to rearrange a listing of the letters into alphabetical order. If a company came out with the Alphabet Game and said on the packaging "Over $4 \times 10^{26}$ possibilities!" you would not think it must be hard since that number is so big.

**Example 3.1.** The matching parity condition on edge and corner pieces in (3.2) means a solved Rubik's cube can't be rearranged so that the only change is permuting the center squares along a middle slice by a 4-cycle: in terms of edge and corner movements, this amounts to permuting the edges on that middle slice by a 4-cycle in the other direction without moving the corners, which is a 4-cycle on the edges and the identity on the corners. Those edge and corner permutations have opposite parity, contradicting (3.2).

If the edges are permuted only around a middle slice as a 4-cycle, this must be matched by an odd permutation of the corners, such as a corner transposition. Figure 7 shows this, with a pair of transposed corners in the top and bottom layers.

**Figure 7.** Rotated centers and transposed corners from two perspectives.

This insight can be applied to a puzzle called the Void cube, which has empty spaces in place of the center squares. The first photo of Figure 8 shows a solved Void cube.

When trying to solve a Void cube, you can sometimes have everything in place except for two corner pieces in the wrong positions, as shown in the second photo of Figure 8. That is a strange configuration from the viewpoint of Rubik's cube, because you can't solve Rubik's cube except for a corner transposition: it would contradict (3.2). But this *is* possible on Void cubes since you can solve them with the "wrong centers": the second photo in Figure 8 is how the first photo in Figure 7 would look if its center pieces become invisible.

**Example 3.2.** Another variant on Rubik's cube is the Penrose cube, which has only three colors and is shown from different perspectives in Figure 9. Its name alludes to the Penrose

<!-- page 13 -->

**Figure 8.** The Void cube: a Rubik's cube with no center pieces.

triangle, named after the psychiatrist Lionel Penrose and his son the physicist Roger Penrose, who wrote about that shape.[^12] Each color in a Penrose cube is on two adjacent faces, with their shared edge having curved pieces in that color.

**Figure 9.** The Penrose cube: a Rubik's cube with just three colors.

A Penrose cube has some identical edges: two blue-white edges, two white-red edges, two red-blue edges, and seen in Figure 10. There are also two corners in Figure 10 having all three colors but are oriented differently: one rotates clockwise as red-white-blue and the other rotates clockwise as red-blue-white.

**Figure 10.** Identical edges and two corners with same colors and different orientations.

Figure 11 shows a feature on a Penrose cube that is never on a regular Rubik's cube: all pieces are in their right position and just one edge piece (a red-blue edge) is incorrectly

[^12]: See https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/j.2044-8295.1958.tb00634.x.

<!-- page 14 -->

oriented. How can this happen? By the edge relation $\sum_{j=1}^{12} w_j \equiv 0 \bmod 2$ in (3.4), another edge piece is also flipped, or rather an odd number of other edges are flipped, but none *appears* flipped. What happened is 1 or 3 of the curved edges is also flipped and this is not directly seen because curved edge pieces are symmetric under flipping.

**Figure 11.** A Penrose cube with just one flipped edge: see left picture.

Unlike some edge pieces, every corner piece on a Penrose cube looks different in all 3 ways it can be twisted: this is obvious for a traditional corner piece, and for a curved corner piece see Figure 12. Thus a Penrose cube never has just one twisted corner using legal moves, but I once got exactly that! The corner had twisted in place by mistaken pressure, so I untwisted that corner by hand to solve the cube. There is a related JPerm video on YouTube: https://www.youtube.com/watch?v=FLBj7GKxNCc&pp=ygUJI3plbmNvcVvy..

**Figure 12.** A Penrose cube with a single curved corner twisted in two nontrivial ways.

**Remark 3.3.** Rubik's cubes come in sizes other than $3 \times 3$. Figure 13 shows cubes with size $2 \times 2$ and $1 \times 1$. When you know how to solve a $3 \times 3$ it doesn't take long to learn how to use the $3 \times 3$ methods to solve a $2 \times 2$ since a $2 \times 2$ is the corners on a $3 \times 3$.[^13]

Returning to the description of allowed movements of Rubik's cube, the denominator $2 \cdot 3 \cdot 2 = 12$ in (3.5) comes from the three constraints in (3.4). If you were to take apart the cube and put it back together at random, it is possible you wouldn't be able to solve it. In fact, the probability is only $\frac{1}{12}$ that you can solve it, because a random choice of $(\pi, \rho, \mathbf{v}, \mathbf{w})$ will have all three conditions in (3.4) satisfied with probability $\frac{1}{2} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{12}$. You won't be able to solve it if $\text{sgn}\,\pi \ne \text{sgn}\,\rho$, if $\sum v_i \equiv 1, 2 \bmod 3$, or if $\sum w_j \equiv 1 \bmod 2$.

[^13]: See https://www.youtube.com/watch?v=GAnNG5a19kg to solve a $2 \times 2$ and https://www.youtube.com/watch?v=73VNfiUKnbQ to solve a $1 \times 1$.

<!-- page 15 -->

**Figure 13.** A $2 \times 2$ and $1 \times 1$ cube.

Viewing (3.1) as a direct product of four groups, (3.4) is a subgroup, since the defining conditions are preserved under componentwise operations. Is (3.4), as a subgroup of a direct product group, the group of permutations of Rubik's Cube? No. Componentwise operations in (3.1) do not match the way moves of the cube in (3.4) compose with one another. Another group structure on (3.1) reflects how moves of the cube compose:

$$
(\pi, \rho, \mathbf{v}, \mathbf{w})(\pi', \rho', \mathbf{v}', \mathbf{w}') = (\pi\pi', \rho\rho', \mathbf{v} + \pi\mathbf{v}', \mathbf{w} + \rho\mathbf{w}').
\tag{3.6}
$$

(The notation $\pi\mathbf{v}'$ means the vector in $(\mathbf{Z}/(3))^8$ obtained by permuting the 8 coordinates of $\mathbf{v}'$ according to the permutation $\pi \in S_8$. The meaning of $\rho\mathbf{w}'$ as a vector in $(\mathbf{Z}/(2))^{12}$ is similar.) The operation (3.6) is componentwise in the first two coordinates, but not in the last two coordinates. This "twisted" direct product operation is called a *semi-direct product*. The set (3.4) with the composition law (3.6) is a group, because permuting coordinates of a vector does not change the sum of the coordinates. A proof that this is the group of movements of the pieces in Rubik's Cube is in [1, pp. 47--48].

Old Rubik's cube have stickers on each square, so you could solve such a cube by peeling off the stickers and putting them back on in a solved state. If you were to peel off all non-center stickers and put them back on at random, what is the probability you would be able to solve that cube?

The probability turns out to be *much smaller* than the $\frac{1}{12}$ probability of solving the cube after taking the cube apart and randomly reassembling the pieces. That is, there are far more ways to make a cube unsolvable by peeling off and reattaching the stickers. For instance, putting two stickers of the same color on both faces of an edge piece makes the cube impossible to solve no matter what else is done with the other stickers. (By comparison, if you use take the cube apart and reassemble it, placing an edge into the cube in a misoriented way can be counterbalanced by putting in another edge in a misoriented way.)

To compute the probability of solving an old cube after removing and randomly reattaching non-center stickers, we know the number of solvable states of the cube (with center colors fixed) is given by (3.5). The number of ways to place the 48 non-center stickers onto the faces after peeling is $48!$. We can't tell the difference between restickings that differ by permutations of stickers with the same color. Each of the 6 colors is on 8 non-center squares, so every particular resticking can occur in $8!^6$ ways. Thus the probability that peeling off the non-center stickers and randomly putting them back on the cube will be a solvable cube is

$$
\frac{(8! 12! 3^8 2^{12} / 12)(8!^6)}{48!} \approx 1.49 \cdot 10^{-14},
$$

<!-- page 16 -->

which is far smaller than $\frac{1}{12}$.

Suppose we now allow complete freedom: even the center stickers can be removed. There are $54!$ ways of putting all 54 stickers back onto the cube and each particular resticking can be done in $9!^6$ ways since permuting the stickers of a fixed color doesn't change the appearance of the faces. For a resticking to be a solvable cube, the center squares have to be assigned different colors. That can be done in $6!$ ways (no specification of which sticker of each color is actually used). If such an assignment of stickers to center squares is made, there are $8! 12! 3^8 2^{12} / 12$ ways to restick the remaining stickers into a solvable state of the cube. So the probability that resticking all stickers is a solvable state of the cube is

$$
\frac{(8! 12! 3^8 2^{12} / 12)(6!)(9!^6)}{54!} \approx 3.08 \cdot 10^{-16}.
$$

## Appendix A. A Move Sequence Only Affecting the Top Layer

Starting with a solved cube, as shown in Figure 14 with views from front (left) and back (right)[^14], apply the following moves in order *from left to right*, with R being the blue face:

$$
\text{U R U R}^{-1} \text{ U R U}^2 \text{ R}^{-1}.
\tag{A.1}
$$

**Figure 14.** A solved cube seen from the front and back.

The result is shown in Figure 15, again with views from the front (left) and back (right).

**Figure 15.** Effect of moves in (A.1).

Comparing Figures 14 and 15, the only affected parts of the cube are in the U (top) layer:

- two edges (in UF and UR positions) swap positions while staying oriented (their U faces both remain white),

[^14]: Images of cubes in this appendix are taken from https://rubikscu.be/

<!-- page 17 -->

- the 4 corners U face are all shifted by one position counterclockwise in a 4-cycle, with one corner remaining oriented (one corner color on the U face in Figure 15 is white) and the other 3 corners are each rotated by $120^\circ$ clockwise.

Figures 16 and 17 show what happens when we apply (A.1) a second and third time to a solved cube. The two swapped edges on top return to their original positions and then exchange positions once again (staying oriented both times). The corners all move one position counterclockwise each time, so at this point each corner has moved 3 positions around the top.

**Figure 16.** Effect of moves in (A.1) applied twice.

**Figure 17.** Effect of moves in (A.1) applied three times.

Applying (A.1) one more time returns all pieces to their original positions and the cube is solved. Figure 18 shows the repeated effect of (A.1) on a solved cube, from the front view. After four iterations the cube is back in the solved state.

**Figure 18.** Applying (A.1) four times.

It is intuitively clear why the edges are solved in 4 iterations of (A.1), because they already are solved in 2 iterations: in (A.1) the UF and UR edges swap positions while

<!-- page 18 -->

staying oriented. Since (A.1) advances each top corner by one position counterclockwise, the corners return to their original positions in 4 iterations (and not earlier), but you might be surprised that the corners are all oriented correctly in 4 iterations: a $120^\circ$ clockwise rotation on a corner can only complete a full rotation in a multiple of 3 number of turns, not 4 turns, so how is the top layer solved in 4 repetitions of (A.1) rather than needing at least 6 or 12 repetitions? The point is that each time you apply (A.1), three corners in the top layer rotate by $120^\circ$ clockwise while one corner does not rotate at all. So when we apply (A.1) 4 times, each corner in the top layer is rotated by $120^\circ$ clockwise three of those times and is not rotated one of those times, which after 4 iterations has the effect of bringing each corner in the top layer back to its original (solved) orientation.

## References

[1] C. Bandelow, *Inside Rubik's Cube and Beyond*, Birkhauser, 1982.

[2] A. H. Frey, Jr. and D. Singmaster, *Handbook of Cubic Math*, Enslow Publishers, 1982.

[3] D. Joyner, *Adventures in Group Theory: Rubik's Cube, Merlin's Machine, and Other Mathematical Toys*, Johns Hopkins Univ. Press, 2002.

[4] J. Mulholland, *Permutation Puzzles: A Mathematical Perspective*, URL http://www.sfu.ca/~jtmulhol/math302/notes/302notes.pdf.

[5] J. Slocum and D. Sonneveld, *The 15-Puzzle Book*, Slocum Puzzle Foundation, 2006.

[6] W. W. Johnson and W. E. Story, "Notes on the 15 puzzle," *Amer. J. Math.* **2** (1879), 397--404. URL https://archive.org/details/jstor-2369492/mode/2up.
