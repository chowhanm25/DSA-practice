# 88. Merge Sorted Array

## Problem Description
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array.  
- `nums1` has a length of `m + n`, with the first `m` elements being valid and the last `n` elements set to 0.  
- The merged array should be stored in `nums1` **in-place**.

### Example

```python
nums1 = [1,3,5,0,0,0]
nums2 = [2,4,6]
merge(nums1, 3, nums2, 3)
print(nums1)  # Output: [1,2,3,4,5,6]

