---
title: "Matrices = Linear Maps (part 3)"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Matrices-Linear-Maps-part-3"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

And now, the finale. In this post we will show that matrices and linear maps between finite dimensional vector spaces are one and the same. Up to know we’ve covered the basics of vector spaces and linear maps, so I will assume you know the material covered in parts [1](/posts/matrices-linear-maps-part-1/) and [2](/posts/matrices-linear-maps-part-2/). I will also assume knowledge of what matrices are and how to multiply them. Alright then, let’s get to it.

For the remainder of this post, let $V$ and $W$ be vector spaces of dimension $n$ and $m$ over the same field $F$. Further, let $\{v_1,\dots,v_n\}$ be a basis for $V$ and $\{w_1,\dots,w_m\}$ be a basis for $W$. Let $T:V \to W$ be a linear transformation.

The key observation to make when we use $T$ to construct a corresponding matrix $A$ is that by knowing how $T$ acts on the basis vectors of $V$, we know how the map acts on *any* vector $v \in V$. Let this sink in for a second. We have a finite object (a basis) that tells us everything about how $T$ acts on a potentially very infinite space of vectors! To see this, note that if

$$
v = a_1v_1 + a_2v_2 +\dots + a_nv_n,
$$

then

$$
Tv = T(a_1v_1 + a_2v_2 +\dots + a_nv_n)
$$

$$
= T(a_1v_1) + T(a_2v_2) + \dots + T(a_nv_n)
$$

$$
= a_1Tv_1 + a_2Tv_2 + \dots + a_nTv_n.
$$

Next, note that for each $i$, $Tv_i \in W$ can be written as a linear combination $W$’s basis vectors. That is, we can write

$$
Tv_1 = b_{11}w_1 + \dots + b_{m1} w_m
$$

$$
Tv_2 = b_{12}w_1 + \dots + b_{m2} w_m
$$

$$
\vdots
$$

$$
Tv_n = b_{1n}w_1 + \dots + b_{mn} w_m
$$

Ok, cool. Now we need to translate over to matrix land. I’m going to gloss over some details\*, but hopefully what I’ve chosen to dive into gets the point across. We can intuitively look at the above and say to ourselves, “Hmm, that kind of looks like a matrix, I can even see the $nm$ numbers that it would probably contain!” And you’d be right! For each $i$, represent $Tv_i$ as a column vector containing the $b_{jk}$s (the coefficients on $W$'s basis vectors) and glue those vectors together from left to right

$$
\begin{pmatrix}b_{11}&b_{12} & \dots & b_{1n} \\ b_{21}&b_{22} & \dots & b_{2n} \\ \vdots & \vdots & & \vdots \\ b_{m1} & b_{m2} & \dots & b_{mn} \end{pmatrix}
$$

We can also look at vectors $v \in V$ as these column vectors by using the coefficients of $v$’s (unique) linear combination of the $v_i$. For example, if $v = a_1v_1 + \dots + a_n v_n$, we would represent it as

$$
\begin{pmatrix}a_1 \\ \vdots \\ a_n\end{pmatrix}
$$

Here’s the cool part. To compute $Tv$, we can do the following:

1. Translate $v$ into its corresponding column vector.

2. Translate $T$ into its corresponding matrix $A$.

3. Compute $Av$.

4. Translate the resulting column vector into a linear combination of $W$’s basis vectors to see the answer.

Let’s see a quick example of this. Let’s say that $V$ and $W$ both had dimension 2 and that we chose bases $\{v_1,v_2\}$ for $V$ and $\{w_1,w_2\}$ for $W$. Suppose $v = 3v_1 + 2v_2$ and that a linear transformation $T$ acted on $v_1$ and $v_2$ with the rules:

$$
Tv_1 = 3w_1 + w_2
$$

$$
Tv_2 = w_1 + w_2
$$

Using our construction above, the matrix corresponding to $T$ and our choices of bases, would give us the matrix

$$
A = \begin{pmatrix}3 & 1 \\ 1 & 1\end{pmatrix}
$$

Let’s say that we wanted to compute $Tv$. Using the method above:

1. Translate v into the column vector $(3 ~~ 2).$

2. We’ve already done this step.

3. Using matrix multiplication, we get the column vector $(11 ~~ 5).$

4. Translating in the other direction, we claim that $Tv = 11w_1 + 5w_2$.

To check that this is correct, we will now do the same computation the matrix-free way. If $v = 3v_1 + 2v_2$, then

$$
Tv = 3Tv_1 + 2Tv_2 = 3(3w_1 + w_2) + 2(w_1 + w_2) = 11w_1 + 5w_2,
$$

as expected.

This is pretty amazing. At first glance, matrices look nothing at all like linear transformations. $A$ does not look at all like $T$. One looks like a random array of numbers and one looks like an abstract mathematical object with some weird properties. I think this equivalence of matrices and linear maps is one of the most beautiful examples I’ve seen of how looking at a problem in a different way may yield unimaginable benefits. One such benefit, for instance, is that many physical transformations of vectors through 3D space are linear transformations. The fact that we can represent those as matrices allows us to bring the power of computers to bear to produce the ridiculous feats of computer animation and graphics that are ubiquitous in video games.

Before I close, I want to mention a few things.

First, note that in addition to being able to change a linear transformation into a matrix, we can also go backwards. Given a matrix, we can determine the action of linear transformation on the basis vectors of the input space, which, as we said above, completely determines $T$ on the vectors of $V$. Without going into the technical details here, this gives us a mathematically strong one-to-one correspondence between linear transformations and matrices.

Second, this equivalence reveals a few things about matrices that we might not have been able to piece together before; I want to mention two in particular:

- **Matrix multiplication**: Have you ever wondered why matrix multiplication is defined the way it is? With that crazy row-column dot-product ridiculousness? It’s because we want multiplication of matrices to correspond with the composition of linear maps!\*\* With our equivalence in hand, the craziness we are fed in high school is actually the ***only*** sensible way to define it!

- **Associativity of matrix multiplication**: If I asked you to prove to me that matrix multiplication were associative and you didn’t know about the equivalence we were able to draw above, the proof would be downright nasty. You would have to do really annoying manipulations of general matrices and it’s dreadful. (If you don’t believe me, try it.) If you knew that matrices are just linear maps in disguise, you could could simply argue the much cleaner “function composition is associative” argument and just translate the result over to matrices when you’re done!

What I’ve tried to show in this series of posts is that in my mind, one of the most beautiful features of mathematics is that you can build theoretical bridges between things that look nothing alike. The hidden connections between different areas of math over the centuries have led to breakthrough after breakthrough, and I think this one well-represents an accessible, yet non-obvious connection between the worlds of theory and computation. I hope you’ve enjoyed!

\*The ability to represent a vector as an $n$-tuple of the coefficients is actually rigorous. It stems from the fact that every vector space of dimension $n$ is isomorphic to the “canonical” $n$-dimensional vector space $F^n$, where $F$ is the underlying field of $V$ and $W$. We thus can use the isomorphism to translate from $V$ to $F^n$, use the matrix A to then map from $F^n$ to $F^m$, and finally use the isomorphism again to map from $F^m$ to $W$. $A$ is an intermediary of sorts. Under the hood, using $A$ to map from $V$ to $W$ looks like

$$
V \iff F^n \xrightarrow{A} F^m \iff W
$$

\*\*What I mean here is that if $S:U \to V$ and $T:V\to W$ and $S$ and $T$ have matrices $A$ and $B$ respectively, for $u \in U$, we want $(T \circ S)u$ to produce the result that corresponds with $BAu$ (where the second $u$ is a column vector).
