---
title: "An infinitude of primes"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/An-infinitude-of-primes"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

Early in our math careers, all of us learn about prime and composite numbers. In general, a prime number is one that can be divided evenly only by itself and 1. An example of a prime number is the number 5. A composite number is any number that isn't prime (even numbers are easy examples of these).

In Ancient Greece, as mathematicians first started studying the whole numbers as part of a discipline now known as number theory, there seemed to be strong evidence that there exist only a finite number of primes. If we didn't know better, we might agree.

- Between 1 and 100: 25 primes.

- Between 100 and 200: 21 primes.

- Between 200 and 300: 16 primes.  
$\vdots$

- Between 5000 and 5100: 12 primes.  
$\vdots$

- Between 1000000 and 1000100: 6 primes.

As we go higher and higher, their numbers continue to wane. Why does this happen? If we think about it for a minute, we realize that as numbers get larger, the pool of potential divisors grows also. So as the numbers grow, the "chances" of them being prime drop. Most mathematicians at the time agreed with this idea. The prevalence of this view combined with the lack of computational power to suggest an alternative made Euclid's claim that there are infinitely many primes all the more shocking.

His proof is insightful, and it is widely considered one of math's most elegant. His strategy is to show that no matter how many primes you claim to hold in your hand, there must be one that you aren't holding. It goes like this:

Suppose you have some collection of primes in a bag (could be of any size). We want to show that there is at least one that isn't in the bag. We do this as follows: define a number called $N = \text{(the product of all the primes in the bag)} + 1$. If $N$ is prime, the proof is complete because $N$ couldn't possibly have been in our collection already. But what if $N$ is not prime? It is a property of the whole numbers that every number can be decomposed into a product of primes. So if we suppose that $N$ isn't prime, it must have some prime divisor. To finish the argument, all we need to do is show this prime divisor was not in our initial collection. This is clear once we realize that if we divide $N$ by any number in our collection, we are left with a remainder of 1. We can conclude then, that whether $N$ is prime or not, it provides us with a missing prime, as desired.

I'll admit, his argument is pretty slick. Don't feel bad if you find yourself needing to read the above paragraph 2 or 3 times. To clarify what's happening, let's see a few examples.

1. Let's say that the collection of primes we start with is (2, 3, 11). Then $N = 2 \times 3 \times 11 + 1 = 67$. 67 is prime and is not in our original collection. Check.

2. Now suppose that the collection we start with is (3, 5, 17). Then $N = 3 \times 5 \times 17 + 1 = 256$. 256 can be decomposed into primes as the product $2^8$ (eight times), and 2 is not present in our collection. Check.
