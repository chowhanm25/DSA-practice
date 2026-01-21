# Majority Element II

## Problem
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

## Approach
Use Boyer-Moore Voting Algorithm:
1. First pass: Find up to two potential candidates.
2. Second pass: Count actual occurrences to verify.
3. Return elements appearing more than n/3 times.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

