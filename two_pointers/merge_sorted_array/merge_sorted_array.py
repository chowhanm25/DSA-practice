"""
LeetCode 88. Merge Sorted Array

Merge two sorted arrays nums1 and nums2 into nums1 in-place.

Author: Munna Chowhan
Date: 2026-01-27
"""

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges nums2 into nums1 in-place to form a single sorted array.

    Args:
    nums1 (List[int]): First sorted array with size m+n; first m elements are valid, rest are 0.
    m (int): Number of valid elements in nums1.
    nums2 (List[int]): Second sorted array of size n.
    n (int): Number of elements in nums2.

    Returns:
    None: Modifies nums1 in-place.
    """
    i = m - 1       # Pointer for last valid element in nums1
    j = n - 1       # Pointer for last element in nums2
    k = m + n - 1   # Pointer for last index in nums1

    # Merge from the back
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Copy remaining elements from nums2, if any
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

