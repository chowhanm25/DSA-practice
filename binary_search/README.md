# 704. Binary Search

## Problem

Given a sorted array of integers `nums` and an integer `target`, return the index of the target if it exists in the array. Otherwise, return `-1`.

The algorithm must run in **O(log n)** time.

## Approach

Since the array is sorted, we use **Binary Search**.

1. Start with two pointers:

   * `left` at the beginning of the array
   * `right` at the end of the array
2. Find the middle index `mid`.
3. Compare `nums[mid]` with `target`:

   * If equal → return `mid`
   * If `nums[mid] < target` → search the right half
   * If `nums[mid] > target` → search the left half
4. Repeat until the target is found or the search space becomes empty.

## Complexity

* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

