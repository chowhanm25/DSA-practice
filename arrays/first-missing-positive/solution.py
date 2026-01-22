class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Approach:
        - Convert the list into a set for O(1) lookups.
        - Start checking from 1 upward.
        - Return the first integer not present in the set.
        """

        nums_set = set(nums)
        smallest_missing = 1

        while smallest_missing in nums_set:
            smallest_missing += 1

        return smallest_missing

