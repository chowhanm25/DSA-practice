class Solution(object):
    def productExceptSelf(self, nums):
        """
        Given an array nums, returns an array answer such that:
        answer[i] = product of all elements in nums except nums[i].

        Constraints:
        - O(n) time complexity
        - No division operation
        """

        # Length of the input array
        n = len(nums)

        # Initialize the output array with 1s.
        # Each index will eventually store:
        # (product of elements to the left) * (product of elements to the right)
        answer = [1] * n

        # --------------------------------------------------
        # FIRST PASS: LEFT PRODUCT CALCULATION
        # --------------------------------------------------

        # This variable keeps track of the product of all elements
        # to the LEFT of the current index.
        left_product = 1

        # Traverse the array from left to right
        for i in range(n):
            # At index i, store the product of all elements
            # that appear BEFORE index i
            answer[i] = left_product

            # Update left_product by multiplying the current element
            # so it will be correct for the next index
            left_product *= nums[i]

        # After this loop:
        # answer[i] contains the product of all elements to the LEFT of i

        # --------------------------------------------------
        # SECOND PASS: RIGHT PRODUCT CALCULATION
        # --------------------------------------------------

        # This variable keeps track of the product of all elements
        # to the RIGHT of the current index.
        right_product = 1

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # Multiply the current value in answer[i]
            # (which already contains left product)
            # with the product of elements to the RIGHT
            answer[i] *= right_product

            # Update right_product by multiplying the current element
            # so it will be correct for the next index on the left
            right_product *= nums[i]

        # Now answer[i] contains:
        # (product of elements to the left of i) *
        # (product of elements to the right of i)

        return answer

