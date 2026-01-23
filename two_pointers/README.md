# 344. Reverse String

**Problem Statement:**  
Write a function that reverses a string. The input string is given as an array of characters `s`.  
You must do this by modifying the input array in-place with O(1) extra memory.

**Folder:** `two_pointers`  
**File:** `reverse_string.py`  

**Solution Approach:**  
- Used the **two-pointer technique** to swap elements from both ends moving toward the center.
- Implemented using Python tuple unpacking for in-place swaps.

**Example:**

```python
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

