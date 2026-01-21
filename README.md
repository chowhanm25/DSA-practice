# Subarray Sum Equals K

**LeetCode Problem 560 | Medium | Topics: Hashing, Prefix Sum**

---

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the **total number of subarrays** whose sum equals `k`.

A **subarray** is a contiguous, non-empty sequence of elements within an array.

---

## Solution Overview

This repository contains a **Python solution** using the **prefix sum + hash map approach**, which is the most efficient solution for this problem.

### Key Ideas

1. **Prefix Sum**: Maintain a running sum of elements as you iterate through the array.  
2. **Hash Map**: Track how many times each prefix sum has appeared.  
3. **Subarray Detection**:  
   For each new element, check if `(current_sum - k)` exists in the hash map. If it does, there are one or more subarrays ending at the current index whose sum equals `k`.

### Time & Space Complexity

- **Time Complexity**: O(n) — single pass through the array  
- **Space Complexity**: O(n) — hash map storing prefix sums

---

## Example

```python
nums = [1, 2, 3, -2, 5, -3, 2, 1, -1, 4]
k = 5
print(subarraySum(nums, k))  # Output: 6

