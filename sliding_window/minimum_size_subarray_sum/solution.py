class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0                      # Left pointer of the sliding window
        current_sum = 0                # Current sum within the window
        min_length = float('inf')     # Initialize minimum length as infinity

        # Iterate with the right pointer over the array
        for right in range(len(nums)):
            current_sum += nums[right]   # Expand the window by adding nums[right]
            
            # While the sum is at least the target, try to shrink the window
            while current_sum >= target:
                # Update the minimum length if this window is smaller
                min_length = min(min_length, right - left + 1)
                # Shrink the window by moving left pointer
                current_sum -= nums[left]
                left += 1   # Move left pointer forward
        
        # After the loop, check if we found a valid window length; if not, return 0
        return 0 if min_length == float('inf') else min_length

