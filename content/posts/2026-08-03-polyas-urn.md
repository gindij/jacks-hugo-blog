---
title: "Does order matter?"
date: 2026-08-03
tags: ["math"]
---

## Introduction
When doing math, many people look for ways to use their intuition -- they try to reason their way to the right answer by considering what *should* be true. After solving a problem or writing a proof, they might try to zoom out and come up with a human-legible way to understand why a given result should hold beyond the lines of algebra or symbolic manipulation. There are other times, though, where what's satisfying is to actually discover that intuition has led us astray. It is in these cases that rigor comes to our aid, rather than taking its usual place as rote, dry formalism.

In this post, I want to walk through a problem that represents the latter case. Our intuitions will be subverted, and we will try to wrap our heads around a concept from probability theory that goes back to the early 20th century.

## The problem

We start with a bag that contains one white ball and one black ball. On each turn, we (1) select a single ball uniformly at random, (2) check its color, and (3) place it and another ball of the same color back into the bag. We repeat this process until there are $n$ balls in the bag.

Our goal in this post is to answer the following question: After we play this process out, for a given value of $k$, what are the chances that we end up with $k$ white balls (and $n-k$ black balls) in the bag?

## Intuition
Let's consider the $n=5$ case to start. We start with $(W=1,B=1)$. Let's say that our three draws were BBW (black then black then white). What would the probability of drawing this sequence be? Well, there's a 1/2 probability of drawing the first black ball, then a 2/3 probability of drawing the second black ball, then a 1/4 probability of drawing the final white ball. In total then, we have
$$
    P(BBW) = \frac{1}{2} \frac{2}{3} \frac{1}{4} = \frac{1}{12}
$$

Note here that each probability in the sequence is influenced by prior choices. With respect to our original question, we notice two things that seem almost obvious:
1. A sequence like BBB...BW would be much less likely to occur than the sequence WBBB...B, since drawing the lone white ball early should be more likely than drawing it late after the bag has become overwhelmingly black. So knowing $k$ is not enough to know the likelihood of the sequence; you also need to know its order.
2. The numbers of sequences that are possible for each value of $k$ differ. For a bag ending with $k$ white balls in it, there are $\binom{n-2}{k-1}$ possible sequences of draws. (Since we start with one ball of each color, we only make $n-2$ selections and only need $k-1$ of them to be white balls.) So our expression for the likelihood of some number of white balls has the form $$P(\#W=k) = \sum_{i=1}^{\binom{n-2}{k-1}} P(s_i),$$ where the sum is over all sequences that leave $k$ white balls in the bag. The quantity $\binom{n-2}{k-1}$ is small for values of $k$ near 1 and $n-1$, and large for values near $k=n/2$. This would lead us to believe that the probabilities are larger for medium-sized values of $k$ than for small or large $k$.

We will now show that both of these intuitions are mistaken. Before reading on, can you see why?

## The solution
First, let's look at a simple case: $n=6$ and $k=3$. We start off with one black ball and one white ball in the bag and need to make four selections.
Here are three of the six possible ways to end up with $k=3$ white balls:

| Sequence | Probability |
| --- | --- |
| BBWW | $\frac{1}{2}\cdot \frac{2}{3} \cdot \frac{1}{4} \cdot \frac{2}{5}$ |
| BWBW | $\frac{1}{2}\cdot \frac{1}{3} \cdot \frac{2}{4} \cdot \frac{2}{5}$ |
| BWWB | $\frac{1}{2}\cdot \frac{1}{3} \cdot \frac{2}{4} \cdot \frac{2}{5}$ |

The first thing that stands out is that the denominator is the same for each sequence: $(n-1)!$. This makes sense, since on each selection we add one ball to the bag, increasing the size of the collection we choose from on the next draw. On the last draw, there are $n-1$ balls in the bag, hence $n-1$.

The second thing, which is slightly more challenging to notice, is that the numerators are just reorderings of the constituent terms of a product with two recognizable pieces: $(k-1)!$ and $(n-k-1)!$. Where do these quantities come from?

Well, in order to reach $k$ white balls, we need to draw white $k-1$ times during the game (since we start with one). Each time we draw a white ball, the probability of drawing it is
$$
    \frac{\text{\# white balls already in bag}}{\text{\# balls in bag}}.
$$

On the first white ball we draw, the numerator will be 1, since there is one white ball in the bag so far. Now we add a white ball to the bag, so on the next draw, it will be 2. On the next, it will be 3, and so on. When we multiply these probabilities together, the numerator becomes the product of these numbers, i.e., $(k-1)!$.

This same logic applies symmetrically to the black balls. If we reach a state in which there are $n-k$ black balls in the bag at the end of the game, we will observe a sequence where we drew $n-k-1$ of them (again, since we start with one), which means that the numerator of that sequence's probability will also include $(n-k-1)!$.

Therefore, the probability of seeing any particular sequence of draws that leaves $k$ white balls, **regardless of order**, is
$$
    p_{n,k} = \frac{(k-1)!(n-k-1)!}{(n-1)!}
$$

We have just invalidated the first of our two intuitive claims: it turns out that different sequences that have the same number of white balls actually have the same probability of occurring! The sequences we mentioned earlier, BB...BW and WBB...B are actually equally probable!

There is one piece that we have not yet added to the puzzle, though. So far, we have established that the probabilities of different sequences for the same value of $k$ are the same. But how do probabilities compare across different values of $k$? As we noted earlier, for each value of $k$, the number of sequences that leave $k$ white balls in the bag is given by $\binom{n-2}{k-1}$. Thus, the probability that we observe a bag ending up with $k$ white balls is
$$
\begin{align*}
    P(\#W = k) &= \binom{n-2}{k-1} p_{n,k} \\
    &= \frac{(n-2)!}{(k-1)!(n-2-k+1)!}\frac{(k-1)!(n-k-1)!}{(n-1)!} \\
    &= \frac{(n-2)!}{(k-1)!(n-k-1)!}\frac{(k-1)!(n-k-1)!}{(n-1)!} \\
    &= \frac{(n-2)!}{(n-1)!} \\
    &= \frac{1}{n-1}.
\end{align*}
$$
What we've shown is that the probability of observing $k$ white balls in the bag is *uniform*, which is to say, *completely independent* of $k$! (Note that since there are $n-1$ possible values of $k$ that we could observe, the probabilities here are all positive and sum to 1, making them a valid distribution.)

When I encountered this problem for the first time, these were both very surprising conclusions. Concretely, we can say two things:
1. If I fix the number of Ws in a sequence, no matter the order, the sequence will occur with the same probability as all other sequences with that many Ws.
2. If instead of thinking about the probabilities of a given specific sequence occurring, I care about the probability of running the process and seeing $k$ Ws, all values of $k$ are equally likely!

The second fact invalidates our second incorrect intuition. Once we do the math, we see a push-pull relationship between the quantity of sequences ending with $k$ white balls in the bag and the probability of picking each individual sequence. Values of $k$ that give smaller individual probabilities make up for it with more (equiprobable) sequences.

## Conclusion
That's pretty neat! This result is important enough that it has a name -- it is known as the [Pólya urn model](https://en.wikipedia.org/wiki/P%C3%B3lya_urn_model), and it is an example of what is known as an **exchangeable process**, or one where the joint probability of a sequence of random variables is invariant to permutation. Fanciness aside, I think it's another compact example of why theory is so important: it keeps our intuition in check. Thanks for reading!