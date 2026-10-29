---
title: "Proving Sylow’s Theorem (Part 1)"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Proving-Sylow-s-Theorem-Part-1"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

In my self-study of some abstract algebra, I recently came across Sylow’s Theorem. In order to better understand it myself, I thought it might be useful to write a series of blog posts in which I tried to walk through a proof I came across as understandably as I could. I’m a firm believer in the idea that one only understand things as well as one can express them, so while this post will be a mostly unoriginal presentation of a proof found in *Abstract Algebra* (Dummit and Foote), I’m hoping my presentation is enlightening and useful to those who read it.

The theorem has 3 parts and we will prove each in turn. This post will focus on the first piece.

(Note: The below proof assumes familiarity with some group theory learned at the beginning of an abstract algebra course. Also, I added some details that I think it would have been helpful for the authors to have included as well, so my proof might be a little bit longer.)

---

Before the theorem itself, it will be useful to establish a few definitions. For the below definitions, let $G$ be a group and $p$ a prime.

1. A $p$-subgroup $P$ of $G$ is a subgroup of $G$ of order $p^a$ for some nonnegative integer $a$.

2. If $|G| = p^am$ and $p$ does not divide $m$, then if $P$ is a $p$-subgroup of order $p^a$, we say that $P$ is a Sylow $p$-subgroup of $G$.

3. We denote the set of Sylow $p$-subgroups of $G$ as $Syl_p(G)$. Further, we denote the size of $Syl_p(G)$ by $n_p(G)$ (or just $n_p$ if we know what group we’re dealing with).

We’re now ready for the first part of Sylow’s theorem. The entirety of Sylow’s theorem is very important to many of the classification theorems surrouding groups; that is, it allows us to make statements like “if a group has an order that decomposes in such-and-such a way, then it must be isomorphic to this-that-or-the-other group” or “if a group has order X, it must have a normal subgroup of order something-related to X” among others. Let’s see how it works under the hood. For all 3 parts, $G$ is a group with order $p^\alpha m$ where $p$ is a prime not dividing $m$.

**Part 1**: $Syl_p(G) \neq \emptyset$. (In other words, $G$ has at least one Sylow $p$-subgroup.)

**Proof**: The proof of this piece of the theorem is by induction on the order of $G$. If $|G| = 1$, there is nothing to prove.

If $p$ divides the order of $Z(G)$ (the center of $G$), then by Cauchy’s theorem, $Z(G)$ has a subgroup $N$ of order $P$. Let $\bar G = G/N$ and note that $|\bar G| = p^{\alpha -1}m$. By the induction hypothesis, $\bar G$ has a subgroup $\bar P$ of order $p^{\alpha - 1}$. Let $P$ be a subgroup of $G$ containing $N$ such that $P/N = \bar P$. Then $P$ has order $p^\alpha$ and $P$ is thus a Sylow $p$-subgroup, so it only remains to show that we can also find one in the event $p$ does not divide the order of $Z(G)$.

Let $g_1,\dots, g_r$ be representatives of the non-central conjugacy classes of $G$. The class equation for $G$ looks like

$$
|G| = |Z(G)| + \sum_{i = 1}^r |G : C_G(g_i)|
$$

(where $C_G(g_i)$ is the set of elements that commute with $g_i$ in $G$).

If $p$ divides every $|G:C_G(g_i)|$ for each $i$, it would be forced to also divide $|Z(G)|$, which would contradict our assumption, so let $H = C_G(g_i)$ for some $g_i$ such that $p$ does not divide $|G:C_G(g_i)|$. Because $|G| = |C_G(g_i)||G:C_G(g_i)|$ and $p$ does not divide the second right hand term, we have $|H| < |G|$. Thus, by the induction hypothesis, $H$ has a Sylow $p$-subgroup, $P$. As $P$ is also a Sylow subgroup of $G$, we’ve completed the proof of part 1.
