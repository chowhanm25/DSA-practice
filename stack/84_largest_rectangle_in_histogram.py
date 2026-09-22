"""
LeetCode 84: Largest Rectangle in Histogram
Approach: Monotonic increasing stack
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                bar_index = stack.pop()
                bar_height = heights[bar_index]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = bar_height * width
                max_area = max(max_area, area)

            stack.append(i)

        while stack:
            bar_index = stack.pop()
            bar_height = heights[bar_index]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            area = bar_height * width
            max_area = max(max_area, area)

        return max_area
