# 189. Rotate Array

## Problem
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

## Approach
- Use the reverse method to rotate in-place
- Steps:
  1. Reverse the whole array
  2. Reverse first k elements
  3. Reverse the remaining n-k elements

## Complexity
- Time: O(n)
- Space: O(1)

## Example
Input: [1,2,3,4,5,6,7], k=3  
Output: [5,6,7,1,2,3,4]

