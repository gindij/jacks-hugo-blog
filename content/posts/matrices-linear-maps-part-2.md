---
title: "Matrices = Linear Maps (part 2)"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Matrices-Linear-Maps-part-2"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

In the last post, we talked about properties of individual vector spaces. But what if we want to relate them? There are certain aspects of some vector spaces that make them easier to look at in certain ways but difficult in others. It is thus critical to be able to think about how to relate vector spaces to one another. These relationships allow us to look at inscrutable or difficult properties of one space from a different perspective that may offer valuable insight.

In this post we will develop some rudimentary theory that underlies the main tool with which we go about investigating these relationships: linear maps. Alright, let's get to it.

Suppose I have 2 vector spaces, $V$ (of dimension $n$) and $W$(of dimension $m$) both over the same field (so the scalars are the same). As stated above, we want to relate them. But the useful ways of relating them are ways that preserve the structure of the spaces we are mapping from when the map lands us in the second space. I think looking at this structure preservation mathematically sheds more light on this idea. Let's say I have a map $T: V \to W$ that turns vectors in $V$ into vectors in $W$. We say that $T$ is a **linear map** if:

1. $T(v_1 + v_2) = Tv_1 + Tv_2$.

2. $T(cv) = cTv$.

(Note: $Tv$ is read "$T$ of $v$", the same way you would read something like $f(x)$.)

The first property enforces the idea that my map should be such that I should be able to compute the sum of $v_1$ and $v_2$ with the addition defined for $V$ and then map the resulting vector over to the same vector in $W$ that I would get if I first mapped each of $v_1$ and $v_2$ over to $W$ and summed once there. Similarly, I should be able to scale in $V$ and then map the result and get the same thing as if I were to first map and then scale once in $W$. This is what I meant earlier when I said that we are preserving structure with these maps; via our map $T$, adding/scaling in one space corresponds to adding/scaling in the other space in a nice mathematical way. To drive this home, let's look at an example of some linear and non-linear maps.

For these examples, we will have $V = \mathbb{R}^2$ and $W = \mathbb{R}$ ($\mathbb{R}^2$ is the set of all ordered pairs of real numbers; you can think about them as points on a 2D coordinate plane).

As our first example, consider $T: \mathbb{R}^2 \to \mathbb{R}$ defined by $T(x,y) = 2x + 3y$ ($T$ takes a point in the coordinate plane and maps it to some real number). For this to be linear, we need to verify the two properties above:

1. We can verify the first property by looking at what happens when we try to map the sum of two pairs. That is, note that  
$T((x_1,y_1) + (x_2 ,y_2)) = T((x_1 + x_2, y_1 + y_2)) = 2(x_1 + x_2) + 3(y_1 + y_2) = T(x_1,y_1) + T(x_2,y_2)$.  
We've shown that mapping-then-summing is the same as summing-then-mapping.

2. The second property can be verified in a similar way, by noting that for some scalar $c$, we get $cT(x,y) = c(2x + 3y) = 2(cx) + 3(cy) = T(cx, cy)$.

Okay, but what about an example of a non-linear map? This time, let $T:\mathbb{R}^2 \to \mathbb{R}$ defined by $T(x,y) = x^2 + y^2$. To show that this is non-linear, we only need one of the properties to not hold. In this case, it happens that both don't hold, but it's easier to show that the second one doesn't hold, so that's what we'll show. Note that if I pick a scalar $c$, then on the one hand,

$$
cT(x,y) = c(x^2 + y^2) = cx^2 + cy^2
$$

but on the other,

$$
T(cx, cy) = (cx)^2 + (cy)^2 = c^2x^2 + c^2y^2.
$$

Because these aren't the same (for $c$ other than 0 and 1), we conclude that in this case, $T$ is non-linear.

Hopefully, at this point, I've convinced you that linear maps are important and somewhat special. In the next post, we will combine the ideas of linear maps and bases to establish our prized result: the equivalence between linear maps and matrices.
