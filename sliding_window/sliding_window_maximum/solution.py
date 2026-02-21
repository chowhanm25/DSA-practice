 from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []

        dq = deque()      # stores indices of useful elements
        result = []

        for i in range(len(nums)):

            # Define the start of current window
            window_start = i - k + 1

            #⃣ Remove indices that are OUTSIDE the window
            if dq and dq[0] < window_start:
                dq.popleft()

            # ️ Remove smaller elements from the BACK
            # because they can never be maximum again
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # ️⃣ Add current index
            dq.append(i)

            # Once first window is formed, record max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
