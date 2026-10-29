---
title: "The secretary problem"
date: 2026-10-29
tags: ["math"]
sourceURL: "https://whatabouttheory.quora.com/The-secretary-problem"
originalPublicationDate: null
migrationNote: "Imported from Quora; date is the import date. Exact original publication date was unavailable."
---

This post is about a cool application of probability I learned about earlier this week.

Suppose you are interviewing 1,000 candidates for a secretary position. Your goal is to choose the best secretary possible (assume for simplicity that there is a definite best, second best, third best, etc. and that there are no ties between candidates) with as few interviews as possible (you don't interview them in any particular order). After having interviewed, for example, 50 candidates, you are only able to rank the 50th candidate relative to the previous 49; you don't find out candidate 50's absolute rank upon interviewing him/her. Once you pass over a candidate, you can no longer hire him/her. Once you choose a candidate to hire, you cannot interview any of the remaining candidates. The question we are trying to answer is: How would you suggest interviewing candidates so that you have a good chance of choosing the best candidate without having to always interview every candidate? (Interviewing everyone will get you the best outcome every time, but if the pool is very large, this may be impractical and we may need a better strategy. The idea is that we sacrifice the guarantee of a perfect outcome via an inefficient for an efficient method that gets us the perfect outcome an acceptable portion of the time.)

We quickly notice that without smartly choosing which candidate to hire, our odds are pretty much the same as if we guessed which candidate was best, i.e. 1/1000. We also can see that if the candidate pool grows larger, our chances of choosing the right candidate grow slimmer and slimmer... This isn't looking good.

This is where a probabilistic analysis comes to the rescue! Consider the following method: Do not hire any of the first 500 candidates (let them all pass). From candidates 501-1000 choose the first candidate that is better than any of the first 500. Why should this strategy give me better odds? Because it works in one particular scenario, namely when the second best candidate (henceforth C2) is in the 1-500 pool and the best candidate (henceforth C1) is in the 501-1000 pool. This is because if C2 is in the first half, the only person we would stop for in the second half is a candidate better than C2, i.e. only for C1. This seems rather arbitrary doesn't it? Choosing a solution suited to one specific scenario feels a bit weird...

The key to understanding how this is actually a clever strategy is to notice that the probability of our ideal scenario is relatively high. The probabilities of the C2 being in the first 500 and of C1 being in the second 500 are each 1/2. This means that the probability of C2 being in the first half AND C1 being in the second half is 1/2 \* 1/2 = 1/4. Because our ideal scenario happens with a 25% probability, our strategy confers an automatic 25% chance at choosing the best candidate, regardless of the pool size!

It ain't perfect, but it sure beats 0.1%.
