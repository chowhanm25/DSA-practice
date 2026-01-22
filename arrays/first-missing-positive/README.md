# First Missing Positive

## Problem Statement


Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


## Approach

- Convert the list into a set for O(1) lookup.
- Start checking from 1 upward.
- The first number not present in the set is the answer.

## Time Complexity
O(n)

## Space Complexity
O(n)

