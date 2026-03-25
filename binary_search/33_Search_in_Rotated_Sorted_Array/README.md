# 33. Search in Rotated Sorted Array

## 🧩 Problem
Given a sorted array `nums` (with distinct values) that has been rotated at an unknown pivot, and an integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

You must write an algorithm with **O(log n)** time complexity.

---

## 💡 Intuition
Even after rotation, **at least one half of the array is always sorted**.

We use this property to decide:
- Which half is sorted
- Whether the target lies in that half
- Then discard the other half

---

## ⚙️ Approach (Binary Search)

1. Calculate `mid`
2. If `nums[mid] == target` → return `mid`
3. Check which half is sorted:
   - **Left sorted** (`nums[beg] <= nums[mid]`)
     - If target is in range → search left
     - Else → search right
   - **Right sorted**
     - If target is in range → search right
     - Else → search left

---

## ✅ Solution

```python
class Solution(object):
    def search(self, nums, target):
        beg, end = 0, len(nums)-1
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] == target:
                return mid
            if nums[beg] <= nums[mid]:
                if nums[beg] <= target <= nums[mid]:
                    end = mid-1
                else:
                    beg = mid+1
            else:
                if nums[mid] <= target <= nums[end]:
                    beg = mid +1
                else:
                    end = mid-1
        return -1 if nums[end] != target else end
