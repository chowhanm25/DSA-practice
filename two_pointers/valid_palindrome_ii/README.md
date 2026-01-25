# 680. Valid Palindrome II

## Problem Statement

Given a string `s`, return `true` if the string can become a palindrome
after deleting **at most one character**.  

Alphanumeric characters include letters and numbers.  

---

## Folder Structure

- **Category:** Two Pointers  
- **Folder:** `two_pointers/valid_palindrome_ii`  
- **File:** `valid_palindrome_ii.py`  

---

## Approach

- Use a **two-pointer technique** starting from both ends.  
- Move pointers inward as long as characters match.  
- On first mismatch:
  - Check if skipping the left character produces a palindrome  
  - Check if skipping the right character produces a palindrome  
- Return `True` if either works, otherwise `False`.

---

## Time Complexity

- O(n) — each character is visited at most once.

## Space Complexity

- O(1) — no extra data structures are used.

---

## Example

```python
Input: "abca"
Output: True
Explanation: Removing 'b' gives "aca", which is a palindrome.

Input: "abc"
Output: False

