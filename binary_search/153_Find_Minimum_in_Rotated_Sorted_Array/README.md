# 153. Find Minimum in Rotated Sorted Array

## Problem
Given a sorted array rotated at some pivot, find the minimum element in O(log n) time.

## Approach
Binary Search:
- If nums[mid] > nums[end] → search right
- Else → search left (including mid)

## Solution
See `solution.py` for Python implementation.

## Complexity
- Time: O(log n)
- Space: O(1)

## Example
Input: [4,5,6,7,8,0,1,2]  
Output: 0
