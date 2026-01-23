"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[-i-1]:
                return False
        return True



      
