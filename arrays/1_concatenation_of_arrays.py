# Problem: Concatenation of Arrays
# Source: LeetCode
# Topic: Arrays
# Approach: Concatenate using + operator
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def getConcatenation(self, nums):
        """
        Concatenates the given array with itself.
        Args:
            nums (List[int]): Input array of integers.
        Returns:
            List[int]: Concatenated array.
        """
        return nums + nums
