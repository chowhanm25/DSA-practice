# 42. Trapping Rain Water

## Problem Statement

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---

## Approach: Two-Pointer Greedy

Water trapped at any index depends on:

    min(max_left, max_right) - height[i]

Instead of precomputing left and right max arrays, we use a two-pointer technique.

### Algorithm

1. Initialize two pointers:
   - left = 0
   - right = n - 1
2. Maintain:
   - left_max
   - right_max
3. While left < right:
   - If height[left] < height[right]:
       - Process left side
   - Else:
       - Process right side
4. Accumulate trapped water accordingly.

---

## Why It Works

The smaller boundary determines the water level.
So we always move the pointer at the smaller height.

---

## Complexity

Time Complexity: O(n)  
Space Complexity: O(1)

---

## Key Takeaway

This problem demonstrates optimal boundary tracking using a two-pointer greedy strategy without extra space.

