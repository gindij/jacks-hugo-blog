---
title: "Big and bigger (Epilogue): What about the rationals?"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Big-and-bigger-Epilogue-What-about-the-rationals"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

In this series so far, we've seen that infinity can be deceptive. Specifically, we've experienced the difficulty of telling whether two infinite sets have the same size. We established that the most reliable way to determine whether sets have the same cardinality is to find out if there is what we called a one-to-one correspondence between the sets. (Recall that a one-to-one correspondence is a matching that matches each element of one set to exactly one element of the other set.)

In this post, we are going to mathematically formalize the notion of a one-to-one correspondence and prove that contrary to what intuition suggests, the rational numbers are countably infinite.

As a note before we continue, this post may be a little bit more technical than the others in the series. It isn't *extremely* complicated, but it will be somewhat abstract and jargon-ish for those who haven't been exposed to this kind of argument before. This doesn't mean you won't get it... it just means that you may have to read some parts a few times and spend a little bit more time than you previously have mulling over the ideas before they click. To help you along, I'll note as we go the parts I think might be worth reading over before moving on. All that said, my recommendation is that you give it a shot, spend a little time grappling with it and see what happens.

(Note: just a few symbols we are going to be using: $\mathbb N$ is the set of positive whole numbers, $\mathbb Z$ is the set of positive and negative whole numbers, and $\mathbb R$ is the set of real numbers.)

One-to-one correspondences between sets -- say $A$ and $B$ -- are really mappings of elements of $A$ to elements of $B$ with some special properties. Mathematically, we represent them as ***functions*** whose ***domain*** (read: input set) is $A$ and whose ***codomain*** (read: output set) is $B$. The way we concisely write "$f$ is a function from elements of $A$ to elements of $B$" is $f:A \to B$. In addition to specifying a domain and a codomain, we also usually give a rule that specifies the mapping.

(If you aren't mathematically inclined, I suggest reading the previous paragraph again.)

For example, we can define $f : \mathbb Z \to \mathbb Z$ with the rule $f(x) = 3x$. These two pieces together say that (1) $f$ takes in and spits out integers, and (2) the specific rule by which $f$ does so is that it takes an integer $x$ as input and spits out $3x$ .

The last thing we need to do before we get to the good part is that we have to talk about the special properties of one-to-one correspondences mentioned above. We say that a function is ***onto*** if every element of the output set is mapped to by some element of the input set. In other words, a function is onto if it hits the entire output set. An example of a function that is *not* onto is $f:\mathbb N \to \mathbb N$ defined by $f(x) = 2x$. Take a second before continuing to see if you can tell which elements of $\mathbb N$ aren't hit by $f$. (Actually take a second ;) )

The elements that aren't hit are the odd numbers. There is no positive whole number from $f$'s input set that you can multiply by 2 to obtain 3, so we say that in this case, $f$ is *not* onto.

(Read the previous two paragraphs again. The properties we are discussing here might be the most important foundation we develop in this piece.)

(Before moving on, as a short exercise, convince yourself that $f$ would have been onto if we made the rule $f(x) = x$ instead of $f(x) = 2x$.)

We have one more property to consider. A function $f$ is ***one-to-one*** if no two inputs map to the same output. The mathematical statement of this property is a tad backhanded, but here it is anyway. We say that $f: A \to B$ is one-to-one if and only if $f(a_1) = f(a_2)$ (where $a_1,a_2$ are both members of the input set $A$) implies that $a_1 = a_2$.

An example of an injective function$g: \mathbb N \to \mathbb N$ is $f(x) = 4x$ because you can't multiply two different positive whole numbers by 4 and get the same answer. A *non* injective $f:\mathbb Z \to \mathbb Z$ can be defined by the rule $f(x) = x^2$. Why is this one not injective? Because the squares of a number and its negative are the same (eg: $(-3)^2=3^2=9$), so for $f$, there are an infinite number of pairs of different inputs for which $f$ produces the same output.

(Make sure you understand the previous 2 paragraphs.)

(\*\*deep sigh of relief\*\*)

If you sufficiently understand the definitions and the horrible jargon we had to resort to above, then it should make sense that a function that is one-to-one and onto -- that is, a function such that no two input elements map to the same output element and such that every element of the output set is hit by some element of the input set -- is a function that matches each element of the input with exactly one element of the output. In our previous discussion, we called such a function a one-to-one correspondence. We also explained that two sets are the same size only if you can find a one-to-one correspondence between them.

In our previous posts we saw that Cantor was able to show that $\mathbb R$ and $\mathbb N$ do not have the same size -- i.e. there is no possible one-to-one correspondence between them. This result was especially significant because it implies that there are a multitude of differently-sized infinities. For the rest of this post we are going to explore the relationship between $\mathbb N$ and another infinite set, the rational numbers -- the set of numbers that can be represented as the ratio of integers that share no factors -- which we will henceforth write as $\mathbb Q$.

One thing to note is that the rational numbers feel more like the real numbers than the natural numbers. One example of this seeming similarity is that $\mathbb Q$ is what we call dense, which effectively means that between any two rational numbers, you can find a third. Extending this line of thought, we can deduce that between any two rational numbers, there is actually an infinitude of additional rational numbers. $\mathbb N$ very clearly does not have this property. In fact, between any two natural numbers, there can only exist finitely many other natural numbers...

The density of the rational numbers makes them feel more continuous than discrete. What we will show is that in this case, as in many others involving infinity, our intuition leads us astray. Despite the density of the rational numbers, they are only as numerous as the natural numbers... this is mind-boggling when you consider it for a second. Because of their likeness to the natural numbers in all but minor ways, our minds can embrace the evens, odds, integers, primes etc as equals of the natural numbers. The fact that a set that seems so much bigger is actually of the natural number ilk is something we could only deduce using the power of mathematics. We've finally arrived at the crux of our discussion:

**Theorem:** $\mathbb Q$ and $\mathbb N$ have the same number of elements.

**Proof Sketch:** We first notice that the rational numbers can be looked at as pairs of integers. To prove our theorem then, we need to find a function $f : \mathbb N \times \mathbb N \to \mathbb N$ ($\mathbb N \times \mathbb N$ means pairs of natural numbers) that is a one-to-one correspondence. The function we use is defined by the rule $f(m,n) = 2^{m-1}(2n-1)$. We complete the proof by proving that this function is both one-to-one and onto. Having established the desired one-to-one correspondence, we will conclude that the two sets in question have the same size.

Now to the actual proof... If you've understood everything up to now, the proof is a slight bit more involved, but you should have what you need to follow. If you aren't clear on what has been said up to now, I encourage you to re-read the above -- specifically the bits about the notation we've developed and what it means for a function to be one-to-one and onto.

**Proof:** We first note that if each rational number can be represented as the ratio of two integers -- as $\frac{m}{n}$ where $m$ and $n$ are integers -- it can be equivalently represented rather simply as a pair of natural numbers $(m,n)$. Thus, if we can show that $f(m,n) = 2^{m-1}(2n-1)$ (notice that the input is a pair of natural numbers that the function combines into a single natural number) is a one-to-one correspondence, we will have completed the proof.

First, we will show that the function is onto. To do this, we need to show that for every natural number of $k$ (our function's output set), there is some pair of natural numbers $(m,n)$ for which $f$ produces $k$. That is, we have to show that for each $k$, there exists a pair $(m,n)$ such that $f(m,n) = 2^{m-1}(2n-1) = k$. To see that such a pair exists no matter what $k$ is, first let $m-1$ be the largest power of 2 that divides $k$ evenly. Note that such a power of 2 always exists (it could be that the largest power of 2 that divides $k$is the $2^0=1$, and 1 divides every number). Once we have $m -1$, we can divide $k$ by $2^{m-1}$. If we think about the number we are left with after doing that, we notice that it must be odd. Thinking a little bit more, we realize that every odd number can be written as an even number minus 1. In math speak this means that each odd number can be written as $2n-1$ for some $n$. As examples of this, observe that $27 = 2(14) - 1$ and $31 = 2(16)-1$. Given our resulting odd number, then, we can compute its corresponding $n$ by adding 1 to the number and dividing it by 2. To summarize, given our starting number $k$, we have found ways to produce an $m$ (1 more than the largest power of 2 that divides evenly into $k$) and an $n$ (that we derive using the left-over odd number) so that $f(m,n) = 2^{m-1}(2n-1) = k$, so every possible output has a corresponding input and we can conclude that our function is onto.

The next and final thing we have to do is to show that no two inputs map to the same output; that is, we need to show that $f$ is one-to-one. We will do this (in the standard way) by showing that if $f(m_1,n_1) = f(m_2,n_2)$ (if the output is the same for two different inputs) then $m_1 = m_2$ and $n_1 = n_2$ (then the inputs must have been the same). So we start out by supposing that for two pairs $(m_1, n_1)$ and $(m_2,n_2)$, that the function outputs the same result; that is, suppose that $2^{m_1 -1}(2n_1 - 1) = 2^{m_2 - 1}(2n_2 - 1)$. We need to leverage one more fact, the Fundamental Theorem of Arithmetic, which says that every natural number can be uniquely factored into a product of prime numbers. Because each such factorization is unique, if $2^{m_1 -1}(2n_1 - 1) = 2^{m_2 - 1}(2n_2 - 1)$, then the prime factorization of the numbers on each side of the equal sign must be the same. In particular, each side must have the same number of 2s -- which means that $m_1 - 1 = m_2 - 1$. Adding 1 to both sides, we see that $m_1 = m_2$. As a consequence, we get $2n_1  - 1 = 2n_2 - 1$. Adding 1 to both sides, then dividing each side by 2, we get that $n_1 = n_2$. So, as we wanted, we have $m_1 = m_2$ and $n_1 = n_2$. This shows that if two inputs produce the same output, they must have been the same inputs to begin with. This means our function is one-to-one.

We've thus established that $f$ is a one-to-one correspondence and, as a result, $\mathbb N$ and $\mathbb Q$ have the same size.

I would say more, but that was probably a lot. I hope to have illustrated that sometimes so get our minds wrapped around certain ideas, the oft-fearsome rigor of math can actually come to our aid.
