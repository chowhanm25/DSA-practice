# 155. Min Stack

## Problem
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## Approach
We use two stacks:
- stack → stores all values
- minStack → stores the minimum value at each level

When pushing:
- Push value to stack
- Push min(current_value, previous_min) to minStack

This guarantees O(1) time complexity for:
- push
- pop
- top
- getMin

## Time Complexity
All operations: O(1)

## Space Complexity
O(n)
