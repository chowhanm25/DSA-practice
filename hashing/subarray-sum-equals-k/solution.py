    """
    Problem: 560. Subarray Sum Equals K
    Link: https://leetcode.com/problems/subarray-sum-equals-k/
    """
    def subarraySum(self, nums, k):
        """
        Calculates the total number of continuous subarrays whose sum equals k.
        
        Args:
            nums (List[int]): Array of integers.
            k (int): Target sum.
            
        Returns:
            int: Total count of subarrays.
            
        Complexity:
            Time: O(n) - Single pass through the array.
            Space: O(n) - Storing prefix sums in a hash map.
        """
        # total_count: tracks the number of valid subarrays found
        total_count = 0
        
        # running_prefix_sum: sum of all elements from index 0 to the current index
        running_prefix_sum = 0
        
        # prefix_sum_counts: Hash map to store the frequency of each prefix sum
        # Initialized with {0: 1} to handle subarrays starting from index 0
        prefix_sum_counts = {0: 1}
        
        for num in nums:
            # Update the running total
            running_prefix_sum += num
            
            # Logic: If (running_prefix_sum - k) was a prefix sum seen previously,
            # the subarray between that point and the current index sums to k.
            target_sum = running_prefix_sum - k
            
            if target_sum in prefix_sum_counts:
                total_count += prefix_sum_counts[target_sum]
            
            # Update the frequency of the current prefix sum in the map
            prefix_sum_counts[running_prefix_sum] = prefix_sum_counts.get(running_prefix_sum, 0) + 1
            
        return total_count

