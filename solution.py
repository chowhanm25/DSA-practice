class Solution(object):
    def majorityElement(self, nums):
        """
        Returns the majority element using the Boyer–Moore Voting Algorithm.

        Time Complexity: O(n)
        Space Complexity: O(1)

        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

