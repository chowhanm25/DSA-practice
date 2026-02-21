# Sliding Window Maximum (LeetCode 239)

## Problem
Given an integer array `nums` and an integer `k`, return the maximum value in each sliding window of size `k`.

Example:
nums = [4,2,12,3,5,8,1]
k = 3

Output:
[12,12,12,12,8]

---

## Approach — Monotonic Deque (Optimal O(n))

We maintain a deque storing indices of useful elements.

Rules:
1. Remove indices outside the window
2. Remove smaller elements from the back (they can never be maximum)
3. Front of deque is always the maximum

---

## Algorithm
For each index i:

window_start = i - k + 1

• Remove expired indices
• Remove smaller elements
• Insert current index
• Record answer when window formed

---

## Complexity
Time Complexity: O(n)  
Space Complexity: O(k)

Each element is pushed and popped at most once.

---

## Key Concept
This problem uses a **Monotonic Decreasing Queue**.

The deque always stores candidates for maximum in decreasing order.

Front → Current Maximum
Back → Smallest candidate
