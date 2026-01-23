# 125. Valid Palindrome

**Problem Statement:**  
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.  
Alphanumeric characters include letters and numbers.

**Folder:** `two_pointers/valid_palindrome`  
**File:** `valid_palindrome.py`

**Solution Approach:**  
- Clean the string by keeping only alphanumeric characters and converting them to lowercase.  
- Use a simple **loop** to compare characters from both ends moving toward the center.  
- Return `False` immediately on mismatch for efficiency.  
- Return `True` if all character pairs match.  

**Example:**

```python
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False

