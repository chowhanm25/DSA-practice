# Sort an Array

## Problem Statement
Given an array of integers `nums`, sort the array in ascending order and return it.

---

## Approach: Merge Sort

Merge Sort is used because:
- It guarantees **O(n log n)** time complexity
- It is **stable** (maintains relative order)
- It divides the array recursively and merges sorted halves

---

## Algorithm
1. Divide the array into two halves recursively
2. Merge the two halves in sorted order
3. Continue until the entire array is sorted

---

## Complexity Analysis
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n) due to recursion and merged arrays

---

## Implementation
See `solution.py` for the full implementation.

