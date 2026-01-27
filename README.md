# 1768. Merge Strings Alternately

**Difficulty:** Easy  
**Topic:** Two Pointers / Strings  

---

## Problem Description

Given two strings `word1` and `word2`, merge them by adding letters in alternating order, starting with `word1`. If one string is longer, append the extra letters at the end.

**Example:**


---

## Approach / Solution

1. Use Python's `zip` to iterate through both strings simultaneously until the shorter string ends.  
2. Append characters alternately to a `list` (efficient for string building).  
3. Append the remaining characters from the longer string (if any).  
4. Join the list into a single string using `"".join(result)`.  

**Time Complexity:** O(n + m), where n = len(word1), m = len(word2)  
**Space Complexity:** O(n + m), for storing the result in a list.

---

## Example Code

```python
sol = Solution()
word1 = "abc"
word2 = "pqrstu"
print(sol.mergeAlternately(word1, word2))  # Output: apbqcrstu

