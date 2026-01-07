# Remove Element

**LeetCode Problem:** Remove Element  
**Difficulty:** Easy  
**Category:** Arrays, Two Pointers  

## Problem Statement
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.  
Return the number of elements remaining after removal.

## Approach
- Use a two-pointer technique.  
- Maintain `k` as the index for valid elements.  
- Traverse the array, copying elements not equal to `val`.  
- Return `k`.

## Time Complexity
O(n) — single pass through array

## Space Complexity
O(1) — in-place

