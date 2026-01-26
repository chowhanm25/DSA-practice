"""
1768. Merge Strings Alternately
Difficulty: Easy
Topic: Two Pointers / Strings

Problem:
Given two strings word1 and word2, merge them by adding letters in alternating order,
starting with word1. If one string is longer, append the remaining letters at the end.

Example:
Input: word1 = "abc", word2 = "pqrstu"
Output: "apbqcrstu"
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately in an efficient way.

        Time Complexity: O(n + m), where n = len(word1), m = len(word2)
        Space Complexity: O(n + m), due to list for result
        """
        result = []

        # Step 1: Merge characters from both strings alternately
        for c1, c2 in zip(word1, word2):
            result.append(c1)
            result.append(c2)

        # Step 2: Append remaining characters of the longer string
        result.append(word1[len(word2):])
        result.append(word2[len(word1):])

        # Step 3: Convert list to string and return
        return "".join(result)



