# Longest Consecutive Sequence

**Problem:**  
Given an unsorted array of integers, return the length of the longest consecutive elements sequence. Must run in O(n) time.

**Approach:**  
- Use a hash set to store all numbers.
- Only start counting sequences from numbers that have no smaller neighbor.
- Expand sequence using consecutive number checks.
- Track maximum length.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

**Example:**  
Input: [100,4,200,1,3,2]  
Output: 4  
Explanation: Sequence is [1,2,3,4]

