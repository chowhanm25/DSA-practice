class Solution(object):
    def rotate(self, nums, k):
        """
        Rotates the array nums to the right by k steps in-place.
        
        :type nums: List[int]
        :type k: int
        :rtype: None  # Do not return anything, modify nums in-place
        """
        n = len(nums)
        if n == 0:
            return

        # Handle cases where k > n
        k = k % n

        # Helper function to reverse part of the array
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements
        reverse(0, k - 1)

        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)


# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

