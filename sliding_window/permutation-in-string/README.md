# Permutation in String (Sliding Window)

## Problem
Given two strings s1 and s2, return true if s2 contains a permutation of s1.

In other words, return true if one of s1's permutations is a substring of s2.

Example:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Because "ba" is a permutation of "ab" inside s2.

---

## Approach (Sliding Window + Frequency Count)

Instead of generating permutations (which is slow),
we compare character frequencies.

Steps:
1. Count characters in s1
2. Create a window of same size in s2
3. Slide the window
4. Add new char, remove old char
5. If frequencies match → permutation found

---

## Time Complexity
O(n)

We scan s2 only once.

## Space Complexity
O(1)

We use fixed array of size 26.

---

## Key Idea
Permutation strings always have identical character counts.
So instead of rearranging strings, we compare counts.

