class Solution(object):
    def sortArray(self, nums):
        """
        Sorts an array of integers in ascending order using Merge Sort.
        
        :type nums: List[int]
        :rtype: List[int]
        """
        # Base case: an array of length 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums

        # Step 1: Divide the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        # Step 2: Merge the two sorted halves
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        """
        Merges two sorted lists into one sorted list.
        
        :type left: List[int]
        :type right: List[int]
        :rtype: List[int]
        """
        merged = []
        i = j = 0

        # Compare elements from both halves and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append any remaining elements from left or right
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])

        return merged

