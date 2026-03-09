# 35. Search Insert Position

## Problem
Given a sorted array of distinct integers `nums` and a target value, return the index if the target is found. If not, return the index where it would be inserted in order.

The algorithm must run in **O(log n)** time.

## Approach
We use **Binary Search** because the array is sorted.

1. Set two pointers:
   - `l` at the start
   - `r` at the end
2. Find the middle index `mid`.
3. Compare `nums[mid]` with `target`:
   - If equal → return `mid`
   - If target is greater → search the right half
   - If target is smaller → search the left half
4. If the target is not found, return `l` because it represents the correct insert position.

## Complexity
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
