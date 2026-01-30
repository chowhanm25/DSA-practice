# 15. 3Sum

## Problem
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:
- i != j
- i != k
- j != k
- nums[i] + nums[j] + nums[k] == 0

## Approach
- Sort the array.
- Fix one element using a loop.
- Use two pointers (left and right) to find remaining two elements.
- Skip duplicates to avoid repeated triplets.

## Time Complexity
O(n^2)

## Space Complexity
O(1) auxiliary (excluding output)

