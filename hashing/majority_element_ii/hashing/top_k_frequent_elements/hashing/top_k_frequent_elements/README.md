# Top K Frequent Elements

## Problem
Return the `k` most frequent elements from an integer array.

## Approach
- Count frequencies using a hash map
- Group numbers by frequency
- Traverse from highest frequency to lowest
- Stop when `k` elements are collected

## Complexity
- Time: O(n)
- Space: O(n)

## Example
Input:
nums = [4,1,-1,2,-1,2,3], k = 2

Output:
[-1, 2]

