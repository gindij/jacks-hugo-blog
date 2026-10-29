---
title: "Proving Sylow’s Theorem (Part 2, 3)"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Proving-Sylow-s-Theorem-Part-2-3"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

(Note: This part assumes knowledge of [part 1](/posts/proving-sylow-s-theorem-part-1/))

Before we can prove Part 2 of Sylow’s Theorem — which we will state shortly — we need to do a little bit of legwork.

Recall that $G$ is a group of order $p^\alpha m$ where $p$ does not divide $m$. In the previous post, we showed that there is at least one $P \in Syl_p(G)$. Let $S = \{ gPg^{-1} ~|~ g \in G \} = \{P_1,\dots, P_r\}$ and let $Q$ be any $p$-subgroup of $G$. By definition, $G$, and thus $Q$, act on $S$ by conjugation, so we can write $S$ as a disjoint union of orbits of $Q$’s action on $S$, i.e.

$$
S = \cup_{i = 1}^s O_i.
$$

Let $r = \sum |O_i|$. Relabel the elements of $S$ so that the first $s$ elements are representatives of the $O_i$. By definition of orbits, we have $|O_i| = |Q:N_Q(P_i)|$. We also know that $N_Q(P_i) = N_G(P_i) \cap Q = P_i \cap Q$(see the bottom of this post for a proof of the second equality). Thus,

$$
|O_i| = |Q:P_i \cap Q|.
$$

Using the above, we can now show that $r \equiv 1 \pmod p$. Because $Q$ was *arbitrary,* take $Q = P_1$. Clearly, $|O_1| = |P_1:P_1\cap P_1| = 1$. For $i \neq 1, P_1 \neq P_1$, so $P_i \cap P_1 < P$ ($<$ means proper subgroup). We thus know that it’s index is greater than 1, i.e.

$$
|P_1: P_1 \cap P_i| > 1
$$

for $i$ at least 2. Each such index also must be a power of $p$, so the sum of the sizes of the orbits, or $r$, is thus $1 + \sum \text{ powers of } p$, so $r \equiv 1 \pmod p$. We’re now ready to prove the remainder of Sylow’s Theorem.

**Part 2**: If $P$ is a Sylow $p$-subgroup of $G$ and $Q$ is any $p$-subgroup of $G$, then $Q$ is contained in a conjugate of $P$. In particular, any two Sylow $p$-subgroups are conjugates of one another.

**Proof**: Let $Q$ be any $p$-subgroup of $G$. Suppose $Q$ is not contained in any of the $P_i$ (recall that the $P_i$ are, by definition, conjugates of $P$). Then, as above, $Q \cap P_i < Q$ for every $i$, whence, for each $i$, every $|O_i|$ is a power of $p$ greater than 1. Since $r = \sum |O_i|$, we would have $r \equiv 0 \pmod p$, a contradiction of what we just showed above, so $Q$ must be contained in one of the $P_i$.

A Sylow $p$-subgroup a the largest possible $p$-subgroup. By the above, any Sylow $p$-subgroup $H$ is a subgroup of one of the $P_i$ and has the same size as $P_i$. In other words $H = P_i$ for some i, so the second part of the theorem is proved. **QED**.

**Part 3**: $n_p \equiv 1 \pmod p$. Furthermore, $n_p$ must divide $m$.

**Proof**: From the above, we can also see that because Sylow p-subgroup are conjugates of each other, $S = Syl_p(G)$ and $n_p = r$. This immediately gives us $n_p \equiv 1 \pmod p$. Furthermore, the number of conjugacy classes of any subset, and, in particular, a Sylow $p$-subgroup $P$, is given by $|G:N_G(P)| = |S| = r = n_p$. We have the equality

$$
|P||G:P| = |N_G(P)||G:N_G(P)|.
$$

$P \leq N_G(P)$ so $|P|$ must divide $|N_G(P)|$. Let $k = |N_G(P)|/|P|$. Then the above equality becomes

$$
|G:P| = k|G:N_G(P)|.
$$

Substituting, $|G:P|= m$ and $|G:N_G(P)| = n_p$, we get $m = kn_p$. Put another way, $n_p$ divides $m$. **QED**.

Thanks for reading along! If you have any questions at all, do let me know!

---

**Lemma**: Let $P \in Syl_p(G)$. If $Q$ is any $p$-subgroup of $G$, then $Q \cap N_G(P) = Q \cap P$. ($N_G(P)$ is the normalizer of $P$ in $G$.)

**Proof**: Let $H = N_G(P) \cap Q$. Since $P \leq N_G(P)$, it is clear that $P \cap Q \leq H$. Thus, we only need to prove the other inclusion, namely $H \leq P \cap Q$. Because $H \leq Q$, this is equivalent to showing that $H \leq P$. To do this, we will show that $PH$ is a $p$-subgroup of $G$ containing both $P$ and $H$. Because $P$ is a $p$-subgroup of the largest possible order, this means that $PH = P$, which directly gives us $H \leq P$.

Since $H$ is a subgroup of the normalizer of $P$, we have that $PH = HP$. Now, if $x, y \in PH$, then $xy = p_1h_1p_2h_2 = p_1p_2h_1h_2 \in PH$ and $(xy)^{-1} =(h_1h_2)^{-1}(p_1p_2)^{-1} \in HP = PH$. We thus see that $PH \leq G$. Furthermore, we know that

$$
|PH| = \frac{|P| |H|}{|P \cap H|}.
$$

Recall that $|P| = p^\alpha$. Because $P \cap H \leq P$, $|P \cap H|$ must divide $|P|$, i.e. $|P \cap H|$ must also be a power of $p$. By the same reasoning, because $H \leq Q$, $|H|$ must be a power of $p$ as well. We can thus conclude that $|PH|$ must be a power of $p$, and in particular must divide $p^\alpha$. But $P \leq PH$, which means that $|PH| = |P|$, i.e. $PH = P$, so the proof of the lemma is complete. **QED.**
