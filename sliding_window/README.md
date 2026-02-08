# 219. Contains Duplicate II

## Problem
Given an integer array `nums` and an integer `k`, return true if there are two distinct indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Solution Approach
- Used a sliding window (set) to store the last `k` numbers.
- For each number, check if it exists in the set.
- Maintain the window size to at most `k` to ensure correctness.
- Time Complexity: O(n)
- Space Complexity: O(min(n, k))

