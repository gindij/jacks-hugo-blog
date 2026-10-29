---
title: "Big and bigger (Part 2): countable and uncountable infinities"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/Big-and-bigger-Part-2-countable-and-uncountable-infinities"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

(If you aren’t intuitively comfortable with the idea of one-to-one correspondences, read [part 1](/posts/big-and-bigger-part-1-one-to-one-correspondences/).)

**Countable and uncountable infinities**

With one-to-one correspondences in mind, we now turn to a way of rigorously understanding how large infinity actually is. The first mathematically concretized size of infinity is known as a **countable infinity**. For a set to be countably infinite, we need to be able to put that set in a one-to-one correspondence with the **natural numbers** (otherwise known as the nonnegative whole numbers: 0, 1, 2,...). An example of one such set is the set of even numbers. We can match 2 with 1, 4 with 2, 6 with 3,... Noticing the pattern, we see that we can match every even number *n* with its half *n/2* (half of an even number will always be a whole number so we don't need to worry). How do we know that this is a one-to-one correspondence? First, we notice that each natural number has a unique double (e.g. there is no natural number other than 2 whose double is 4). To see it from the other side, we notice that every even number has a unique half (i.e. there is no number other than 4 such that when you half it, you get 2). Because we are able to put the even numbers in this one-to-one correspondence with the natural numbers, we conclude that the even numbers are countably infinite.

For a while, mathematicians thought that infinity had only one size. This makes sense according to our intuition; if infinity is to be the biggest "quantity" imaginable, there should be nothing larger than it right? Enter the father of transfinite mathematics, Georg Cantor. He was actually able to show that there is a larger infinity than the one just discussed, and he would call this flavor of infinity **uncountable**. The obvious question is: How could one possibly go about proving this? Even if someone could, the proof is probably full or inscrutable jargon, right? The next section details what has come to be known as one of the most elegant, accessible and "beautiful" proofs in all of mathematics.

**Cantor's diagonalization argument**

The argument that Cantor made was that there are actually more real numbers (think numbers with lots of decimal places) than there are natural numbers. His argument used a technique called proof by contradiction. To use this technique, you first assume the logical opposite of what you want to show. Then you prove that what you assumed is impossible. Once you have done this, it follows that the opposite of what you assumed is true. For example, if I wanted to prove that it isn't raining outside, I could do it by contradiction as follows. First I assume it *is* raining. Then I note that if it is raining, then when I go outside, I should get wet. I then go outside and not a drop of water hits me. So it cannot possibly be raining (because if it was, I would be wet). In the same spirit, his argument goes as follows (I will present it in steps):

1) Suppose that there are as many natural numbers as real numbers (that the sets have the same size).

2) Then by our definition of same-sizedness in Part 1 (the ability to put the sets into a one-to-one correspondence with one another), we can match each natural number with a real number, like so:

**Natural — Real**

0 — 1.76910872...

1 — 100.917263...

2— 478.35900...

⋮ — ⋮

3) Create a new number as follows: Let the number to the left of the decimal point be 0. Then, let the number in the first decimal place be different than the number occupying the first decimal place of the number matched with 0, the second decimal place be different from the number occupying the second decimal place of the number matched with 1, etc. Before continuing, read the last sentence again and make sure its meaning is clear. In our case, the number might look like

0.8 *(different from 7)* 0 *(different from 1)* 2 *(different from 9)*...

4) This is the key step. Because of the way we made up our new number, it is different from the real number matched with 0 (because its first decimal place is different), different from the real number matched with 1 (because its second decimal place is different), different from the real number matched with 2 (because its third decimal place is different)... When we allow our minds to run out to infinity with this pattern, we see that our new number is actually different from every other real number in our table; we missed a real number, which means that the correspondence we thought we had is not actually a one-to-one correspondence, contradicting our initial assumption that such a correspondence existed!!!

5) We realize that our initial assumption must be false, so the set of real numbers and the set of natural number are not actually the same size.

So which is bigger? Well, the "extra numbers" come from the real numbers side of our table, so there must be more real numbers than natural numbers. This larger, real-number variant of infinity is what came to be known as an uncountable infinity.

Personally, I think Cantor's stroke of insight in the above proof really illustrates the artistry that goes into what is often viewed as a formulaic, rigid field. Some proofs are indeed packed with abstract objects and terminology in the way that most might expect. But there are rare proofs, like Cantor's diagonalization argument, where creativity, simplicity and elegance win the day. It is in these moments of ingenuity that lines that separate unconstrained creativity and cold, hard, logical certitude blur together into something that could only be characterized as beautiful.
