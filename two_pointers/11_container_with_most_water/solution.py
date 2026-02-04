class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_volume = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_volume = max(max_volume, area)

            # Move the pointer at the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_volume

