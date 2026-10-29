---
title: "The power of abstraction"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/The-power-of-abstraction"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

I think my most important takeaway from the math major is a well-honed ability to reason logically about things. One methodology that we often employ is abstraction; we often want to take what we know about a specific phenomenon or object that we care about and generalize what we know to apply it more broadly.

The simplest and most compelling example of a mathematical abstraction that I've come across in my studies is a mathematical object called a group. A group is very simple to define, yet somehow (in my first semester of abstract algebra) we spent a whole semester building up an intricate and elegant theory around them. The goal of the remainder of this post is to define groups and look at an example to see how useful abstractions can be.

A group is a set of things (this set will henceforth be referred to as $G$) and a way of combining them (formally called an operation) that satisfy the following four properties:  
(Note: each property will be written in English and then with more formal math language for those who prefer that.)

1. **Closure**: If we take two elements of $G$, say $a$ and $b$, their combination using the operation must also be in $G$ (the combination is denoted $ab$).  
Math language: For any $a,b \in G, ab\in G$.

2. **Existence of an Identity**: There is an element called the *identity element* -- we will call the identity element $e$ -- so that if we take any other element $a$ of $G$ and combine it with $e$, their combination yields $a$.  
Math language: There exists $e \in G$ such that for any $a \in G, ae = ea = a$.

3. **Existence of Inverses**: For every element $a$ of $G$, there is another element $a^{-1}$(read "$a$ inverse") in $G$ such that if you combine $a$ with its inverse, you get the identity. Math language: For any $a \in G$, there exists $a^{-1} \in G$ such that $aa^{-1} = e$.

4. **Associativity**: If you want to combine 3 elements $a,b$ and $c$ of $G$, you can insert parentheses whatever way you like. In other words, $(ab)c$ is the same is $a(bc)$.  
Math language: For $a,b,c \in G$, $(ab)c = a(bc)$.

The beauty of abstraction is that once you have come up with a sufficiently general object, you are able to reason about any specific instance of that object all at once. For example, a simple fact we can prove is that each group's identity element is unique. Once we've shown this about groups in general, we can apply this result to anything fitting a group's description. Let's look at an example.

Consider the set of integers $\mathbb{Z} = \{ \dots, -3, -2, -1, 0 , 1, 2, 3, \dots \}$ with the operation of addition. Is this a group? Take a second before reading on and see if you can verify the four properties above for the $\mathbb{Z}$ with $+$. [actually take a second]

To show that $\mathbb{Z}$ is a group under addition, we have to verify each of the four properties. The first and fourth clearly hold; that is, we know that if I pick two integers and add them I have to get an integer back and if I have three integers $a,b$ and $c$, that $(a + b) + c$ is the same as $a + (b + c)$. To verify the second property, we note that the identity element is 0 because no matter which integer $z$ I choose, $z + 0 = z$. Finally, to see that each element has an inverse, we observe that $z + (-z) = 0$, i.e. the inverse of any integer is its negative.

Thus $\mathbb{Z}$ with $+$ is a group, so I can now apply anything I know about groups to the integers without working out the specific-to-integer details. The integers happen to be easy to work with so this abstraction may not seem like it helps much, but if, for example, we consider the set of functions that have continuous first derivatives (don't worry about what this means) under addition, the tools we would need to reason about these functions specifically are far more complex in many senses than are tools we can use to think about more abstract groups. In this and many other cases, abstracting simplifies.

To sum up (because I know things teetered on the brink of boring math jargon for a second), abstraction is a really powerful tool that allows us to focus on big-picture properties of things so that we can think about richer, more general phenomena. I find myself using this methodology all the time -- I even used it on a literature final a few weeks ago! As I approach graduation and think about some of the things I've learned about and absorbed during my academic experience at Penn, I thought this particular bit was worth sharing.
