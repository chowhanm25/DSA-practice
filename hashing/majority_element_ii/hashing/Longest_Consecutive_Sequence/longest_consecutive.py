"""
Longest Consecutive Sequence
----------------------------

Problem:
Given an unsorted array of integers, return the length of the longest 
consecutive elements sequence. Your algorithm must run in O(n) time.

Approach:
- Use a hash set to store all numbers for O(1) lookups.
- Iterate through each number and only start counting sequences 
  from numbers that have no smaller neighbor (num - 1 not in set).
- Expand the consecutive sequence by checking num + 1 in the set.
- Keep track of the maximum sequence length.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: empty array
        if not nums:
            return 0

        # Step 1: Store all numbers in a hash set for O(1) lookups
        num_set = set(nums)
        max_length = 0  # To track the longest sequence found

        # Step 2: Iterate through all numbers
        for num in num_set:  
            # Only consider numbers that are sequence starts
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Step 3: Count consecutive numbers starting from current_num
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Step 4: Update maximum sequence length
                max_length = max(max_length, current_length)

        # Step 5: Return the longest consecutive sequence length
        return max_length

