"""
680. Valid Palindrome II

Problem:
Given a string `s`, return True if the string can become a palindrome
after deleting at most one character.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(left: int, right: int) -> bool:
            """
            Helper function to check if the substring s[left:right+1] is a palindrome.
            """
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left or the right character (only once)
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
            left += 1
            right -= 1

        return True

