11. Container With Most Water
Approach

Use a two-pointer greedy strategy.
Start with pointers at both ends.
Compute area using:

(right - left) * min(height[left], height[right])


Move the pointer at the smaller height to try increasing the limiting boundary.

Complexity

Time: O(n)

Space: O(1)
