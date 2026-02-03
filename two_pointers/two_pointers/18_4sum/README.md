# 18. 4Sum

## Problem

Given an integer array `nums` and an integer `target`, return all unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target

The solution set must not contain duplicate quadruplets.

---

## Approach

1. Sort the array.
2. Fix the first number using a loop (index i).
3. Fix the second number using another loop (index j).
4. Use two pointers (left and right) to find the remaining two numbers.
5. Skip duplicates at every step to avoid repeated quadruplets.

This approach is an extension of the 3Sum problem.

---

## Algorithm Steps

- Sort the array.
- Loop i from 0 to n-4.
- Skip duplicate values of i.
- Loop j from i+1 to n-3.
- Skip duplicate values of j.
- Use two pointers:
  - left = j + 1
  - right = n - 1
- If sum == target → store result and move both pointers.
- If sum < target → move left forward.
- If sum > target → move right backward.

---

## Time Complexity

O(n^3)

Because:
- First loop → O(n)
- Second loop → O(n)
- Two pointer scan → O(n)

Total = O(n^3)

---

## Space Complexity

O(1) extra space (excluding output list).

---

## Example

Input:
nums = [1, 0, -1, 0, -2, 2]
target = 0

Output:
[
  [-2, -1, 1, 2],
  [-2,  0, 0, 2],
  [-1,  0, 0, 1]
]

