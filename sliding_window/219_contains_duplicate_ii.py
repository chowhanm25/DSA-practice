class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # This set will store at most k recent numbers
        window = set()
        
        for i in range(len(nums)):
            # If current number is already in the window → duplicate within k distance
            if nums[i] in window:
                return True
            
            # Add current number to the window
            window.add(nums[i])
            
            # Maintain the sliding window of size k
            if len(window) > k:
                # Remove the number that is now out of range
                window.remove(nums[i - k])
        
        # No duplicates found within k distance
        return False

