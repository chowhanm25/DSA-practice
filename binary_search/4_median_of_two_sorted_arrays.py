# 4. Median of Two Sorted Arrays

**Difficulty:** Hard
**Topic:** Binary Search / Arrays

## Problem Description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` 
respectively, return the median of the two sorted arrays. The overall 
run time complexity should be O(log(m+n)).

## Approach
Binary search on the partition point of the smaller array. For a given 
partition of nums1, compute the corresponding partition of nums2 such 
that the combined left half has exactly (m+n+1)//2 elements. Check if 
the partition is valid (max of left side <= min of right side on both 
arrays); if not, move the binary search left or right accordingly. 
Once valid, the median is derived from the boundary elements — either 
the max of the left halves (odd total) or the average of the max-left 
and min-right (even total).

## Complexity
- Time: O(log(min(m, n))) — binary search runs on the smaller array
- Space: O(1)