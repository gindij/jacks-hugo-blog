---
title: "Matrices = Linear maps (part 1)"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Matrices-Linear-maps-part-1"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

In a previous post I wrote about how math is all one thing. I wrote about how some abstractions can be brought to bear to make solving other problems much easier. In this series of posts I'm going to take a foray into linear algebra where we will explore one of the most helpful and complete examples of these connections that I know of, namely the equivalence that exists between matrices and what are known as linear transformations from one vector space to another. I plan to do this in stages:

- First, I will develop some relevant ideas in the theory of vector spaces, namely spanning sets, linear independence, bases and dimension.

- Next, I will briefly go into some ideas about linear transformations. These are the vehicles that allow us to relate different vector spaces to one another.

- Finally, we will use what we've built to this point to draw a powerful equivalence between matrices and linear transformations and close with a few consequences.

A note before we get started. These posts will contain a significant amount of unavoidably scary-looking math. My target in this post is a curious, motivated reader with some mathematical maturity who hasn't yet formally studied linear algebra. If you've seen linear algebra, you may still enjoy this, but (hopefully) none of it will come as a surprise.

Before we talk about linear transformations, we need to talk about vector spaces. Let's say we have a field $F$ -- think of something like the real numbers. Elements of $F$ can be added and multiplied, every element has an inverse with respect to both operations, and addition and multiplication behave with respect to one another in the way you might expect (the standard distributive, associative and commutative laws all hold). A vector space $V$ over the field $F$ is a non-empty set of elements called **vectors** with two operations, addition and scalar multiplication. Informally, a vector space is a set of things with a way of combining and "scaling" those things.

One familiar vector space is $\mathbb{R}^3$ (the underlying field is $\mathbb{R}$). Vectors in this space are ordered triples of real numbers of the form $(r_1, r_2,r_3)$ (note how the vectors are made up of the underlying field $\mathbb{R}$). Addition is defined componentwise and scalar multiplication of $(r_1,r_2,r_3)$ by a real number $c$ (an element of the underlying field) is defined as $(cr_1, cr_2,cr_3)$. Addition and scalar multiplication in this space have geometric interpretations that students typically encounter sometime in high school. Let's see some examples of our operations in action:

- Let $v_1 = (1,2,3)$ and $v_2 = (1, -4,2)$. Then, as you might expect, $v_1 + v_2 = (2, -2, 5)$.

- If we wanted to stretch $v_1 = (1, 4,7)$ by a factor of 5, we would get $5v_1 = (5, 20,35)$.

- If $v_1 = (1,2,8)$ and $v_2 = (1, 1,3)$, we can combine addition and scalar multiplication to compute something like $3(v_1 + v_2) = 3v_1 + 3v_2 = (3, 6,24) + (3,3,9) = (6,9, 33)$.

Operations in $\mathbb{R}^3$ are easy to carry out and even visualize. You can draw any vector $(x,y,z)$ by drawing an arrow from $(0,0,0)$ to $(x,y,z)$ on a 3D coordinate system. What follows discusses what we can do with vector spaces over any field, but as an anchor to something you can play around with intuitively and visually, it will serve you well to keep $\mathbb{R}^3$ in mind.

Now that we have a (rather informal, but still useful) idea of what vector spaces are, we can analyze and think about what we can do with and say about combinations of the vectors in $V$. In particular, we are interested in two properties of subsets of $V$ (that include the zero vector -- vector spaces always have a zero vector): **span** and **linear independence**.

(Note: A subset of $V$ that is itself a vector space under $V$'s operation is called a **subspace** of $V$.)

The **span** of a subset $W$ of vectors of $V$ is the space made up of every possible vector obtained by adding and scaling the vectors in $W$ (these combinations are called **linear combinations**). We denote the span of $W$ as $span(W)$. It is always a subspace of $V$. To give you an intuitive anchor of the idea of what the span of vectors actually is, note that linear combinations of certain pairs of vectors in $\mathbb{R}^3$ define 2D planes that are literally subspaces of $\mathbb{R}^3$ in an observable sense. For example, the span of the set $\{ (1,2,3), (4,2,4)\}$ is the plane below:

We've seen to this point that there are subsets of $V$ that span parts of $V$. What about sets that span all of $V$? Sets of vectors that whose span makes up all of $V$ are called **spanning set**s; for any given vector space there are lots of these. Note that given a subset that doesn't span all of $V$, we can enlarge it to span all of $V$ with the following procedure: if $W$ does not span all of $V$, add a vector not in $span(W)$ to $W$. Repeat until $W$ spans. Provided that $V$ has a finite spanning set (see dimension below), this process will terminate after a finite number of iterations with $W$ as a spanning set. Before we use this idea, we need to shift our focus to linear independence for a minute.

The easiest way to define linear independence is to first discuss what linear dependence is and then just think of linear independence as "not" linear dependence. A set $\{v_1,\dots, v_n\}$ of vectors is linearly dependent if one of the $v_i$ can be written as a linear combination of the others. It follows that said set is **linearly independent** if none of the vectors can be written as linear combinations of the others. In math jargon, $\{v_1,\dots,v_n\}$ is linearly independent only if $a_1v_1 + \dots + a_nv_n = 0$ implies that all of the $a_i$ are $0$. To see that this definitions captures what we want it to, suppose that there is some linear combination of the $v_i$ with nonzero scalars that gives the zero vector; that is, suppose that for some nonzero combination of scalars,

$$
a_1v_1 + \dots + a_nv_n = 0
$$

with, let's say $a_1 \neq 0$ (you'll see that it the logic isn't affected by this specific choice). Then we can write

$a_1v_1 = -(a_2v_2 + \dots + a_nv_n)$,$

so

$$
v_1 = -(a_2/a_1)v_2 - \dots - (a_n/a_1)v_n,
$$

and we've succeeded in writing one of the $v_i$ as a linear combination of the others, so the vectors are indeed linearly dependent if there is some nonzero set of scalars such that $a_1v_1 + \dots + a_nv_n = 0$.

From what we just did above in discussing linear independence, note that we've given ourselves a way to take a large set of vectors and pare it down until we have a linearly independent set left over. As long as there are vectors that can be written as linear combinations of the others in the remaining set, eliminate them one by one, checking whether the resulting set is linearly independent at each step.

(Internalize this idea now before we continue.)

We now combine the ideas of span and linear independence. Suppose that I have some set of vectors $W$. If $W$ is not a linearly independent set, we can pare it down with the algorithm above until it is. We can then subsequently extend $W$ until it spans all of $V$. Note that during the extension phase, there is no point during which $W$ loses its independence. Why? Because the vectors we add at each step are explicitly not in the span of the others in $W$. When our extension algorithm terminates, it means there are no vectors left that cannot be written as a combination of those in $W$.

A linearly independent spanning set is called a **basis** of $V$. There are many, often infinitely many, smallest linearly independent spanning sets, and the one we choose at any particular point is based on convenience, not any kind of superiority of one over another. Bases are also minimal; there are no smaller linearly independent spanning sets of $V$. Given the discussion to this point, we've actually established an algorithm which, given any vector space $V$, computes a basis for it! It leads us to the following fact (bolded because it's very important):

**Every vector space has a basis.**

A basis is the smallest set of vectors with which we can uniquely constitute (via linear combinations) any vector in $V$. We are particularly interested in the vector spaces whose smallest spanning set is finite, i.e. one that has a finite basis. The size of a basis of $V$ is referred to as the **dimension** of $V$.

(deep breath out...)

Ok, that was a lot. But we've developed some important ideas in the theory of vector spaces that will be critical to our upcoming discussion. In the next post, we will take the ideas we just developed and zoom out, from thinking about single vector spaces to how we might relate vector spaces that at first look very different from one another.
