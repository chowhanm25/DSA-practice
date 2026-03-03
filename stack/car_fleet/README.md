# Car Fleet

## Problem
Given position and speed of cars, return number of fleets reaching target.

## Approach
- Sort cars by position descending
- Compute arrival time
- Use stack to count fleets

Time Complexity: O(n log n)
Space Complexity: O(n)
