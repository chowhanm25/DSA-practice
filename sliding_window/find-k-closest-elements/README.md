# Find K Closest Elements

## Approach
Binary Search on Answer Space (Window Start)

The k closest elements in a sorted array must be contiguous.
So we binary search the starting index of a window of size k.

Compare:
x - arr[mid]  vs  arr[mid+k] - x

Move toward the closer side.

## Complexity
Time: O(log n + k)
Space: O(1)
