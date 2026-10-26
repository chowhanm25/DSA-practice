# 287. Find the Duplicate Number

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Floyd's Cycle Detection

[View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)

## Problem Description

Given an array nums containing n + 1 integers, where every value
is between 1 and n inclusive, return the only repeated number.

The repeated number can appear more than twice.

Solve the problem without modifying the array and using only
constant extra space.

## Examples

```text
Input: nums = [1, 3, 4, 2, 2]
Output: 2

Input: nums = [3, 1, 3, 4, 2]
Output: 3

Input: nums = [3, 3, 3, 3, 3]
Output: 3
```

## Approach

Use Floyd's Cycle Detection by treating the array like a linked list:
each index represents a node, and nums[index] gives the next index.

Following these links from index 0 eventually enters a cycle.
The entrance to this cycle is the duplicate number.

### Step 1: Find a meeting point

- Start slow and fast at index 0.
- Move slow one step and fast two steps.
- Stop when they meet inside the cycle.

### Step 2: Find the cycle entrance

- Reset slow to index 0.
- Move both pointers one step at a time.
- When they meet again, return that position.

## Dry Run

For nums = [1, 3, 4, 2, 2], following the links gives:

0 → 1 → 3 → 2 → 4 → 2 → ...

### First Phase

| Round | Slow | Fast |
|---|---:|---:|
| Start | 0 | 0 |
| 1 | 1 | 3 |
| 2 | 3 | 4 |
| 3 | 2 | 4 |
| 4 | 4 | 4 |

### Second Phase

Reset slow to 0 and keep fast at 4.

| Round | Slow | Fast |
|---|---:|---:|
| Reset | 0 | 4 |
| 1 | 1 | 2 |
| 2 | 3 | 4 |
| 3 | 2 | 2 |

Both meet at 2, so the duplicate number is 2.

## Complexity

- Time: O(n)
- Extra space: O(1)
- The original array is not modified.

## Solution

See [solution.py](solution.py).
