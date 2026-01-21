"""
Majority Element II

Given an integer array of size n, find all elements that appear more than n/3 times.
Uses the Boyer-Moore Voting Algorithm for optimal O(n) time and O(1) space.
"""

class MajorityElementII:
    def find_majority_elements(self, nums):
        """
        Finds all elements that appear more than n/3 times.

        Args:
            nums (List[int]): List of integers

        Returns:
            List[int]: List of majority elements
        """

        # -------- FIRST PASS: Find potential candidates --------
        # Initialize two potential candidates and their counts
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            # If the current number matches candidate1, increment count1
            if num == candidate1:
                count1 += 1

            # If it matches candidate2, increment count2
            elif num == candidate2:
                count2 += 1

            # If count1 is 0, assign candidate1 to current number
            elif count1 == 0:
                candidate1 = num
                count1 = 1

            # If count2 is 0, assign candidate2 to current number
            elif count2 == 0:
                candidate2 = num
                count2 = 1

            # If current number is different from both candidates
            # Decrement both counts (cancellation step)
            else:
                count1 -= 1
                count2 -= 1

        # -------- SECOND PASS: Verify actual counts --------
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # -------- COLLECT RESULTS --------
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result


# -------- Example usage --------
if __name__ == "__main__":
    nums_list = [
        [3, 2, 3],
        [1],
        [1, 2],
        [1, 2, 3, 2, 2, 1, 1]
    ]

    solver = MajorityElementII()

    for nums in nums_list:
        print(f"Input: {nums}")
        print(f"Majority elements (> n/3): {solver.find_majority_elements(nums)}\n")

