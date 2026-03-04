# 394. Decode String

## Problem
Given an encoded string, return its decoded string.

Encoding rule:
k[encoded_string] → encoded_string repeated k times.

Constraints:
- k is a positive integer
- Input is always valid
- No digits appear except repeat numbers

## Approach
- Use a stack
- Push characters until ']'
- When ']' appears:
  - Pop until '[' to build substring
  - Pop digits to get repeat count
  - Push repeated substring back to stack
- Join stack at end

## Time Complexity
O(n)

## Space Complexity
O(n)
