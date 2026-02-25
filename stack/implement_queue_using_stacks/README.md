# 232. Implement Queue using Stacks

## Problem
Implement a FIFO queue using only two stacks.

## Approach
Use two stacks:
- s1 → input stack
- s2 → output stack

Push:
- Always push into s1.

Pop / Peek:
- If s2 is empty, move all elements from s1 to s2.
- Then pop/peek from s2.

## Time Complexity
- push → O(1)
- pop → Amortized O(1)
- peek → Amortized O(1)
- empty → O(1)

## Space Complexity
O(n)
