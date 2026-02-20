# 76. Minimum Window Substring

## Problem
Given two strings `s` and `t`, return the smallest substring of `s` that contains all characters of `t` including duplicates.

If no such substring exists, return `""`.

---

## Example

Input:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"

---

## Approach — Sliding Window

We use two pointers:

left → start of window  
right → expand window

We keep expanding until the window becomes VALID  
(contains all characters of t)

Then we shrink from the left to make it MINIMUM.

---

## Key Idea

Expand → satisfy condition  
Shrink → minimize window

Repeat until string ends.

---

## Algorithm

1. Count frequency of characters in `t`
2. Expand right pointer
3. When window valid → shrink left pointer
4. Track minimum length substring

---

## Complexity

Time: O(n)  
Space: O(1) (only 52 characters max)

---

## Python Solution
See `solution.py`
