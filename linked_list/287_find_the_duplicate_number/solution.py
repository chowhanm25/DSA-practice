class Solution(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        # Find a meeting point inside the cycle.
        while True:
            slow = nums[slow]

            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break

        # Find the start of the cycle.
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
