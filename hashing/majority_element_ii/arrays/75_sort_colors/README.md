# Sort Colors (LeetCode 75)

## Problem
Given an array `nums` containing only `0`, `1`, and `2`, sort the array in-place so that elements of the same color are adjacent.

## Approach: Counting Sort
- Count the number of `0`s, `1`s, and `2`s
- Overwrite the original array using the counts
- No extra array is used

## Complexity
- Time: O(n)
- Space: O(1)

