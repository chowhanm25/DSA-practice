# 81. Search in Rotated Sorted Array II

## 🧩 Problem
Given a rotated sorted array that **may contain duplicates**, return true if the target exists, otherwise false.

---

## 💡 Key Difference from Problem 33
- Duplicates are allowed
- This makes it harder to determine which half is sorted

---

## ⚙️ Approach (Modified Binary Search)

1. Calculate mid
2. If nums[mid] == target → return True
3. If duplicates block decision:
   - nums[beg] == nums[mid] == nums[end]
   - Shrink search space → beg++, end--
4. Otherwise:
   - Check which half is sorted
   - Decide where target lies

---

## ✅ Solution

```python
class Solution(object):
    def search(self, nums, target):
        beg, end = 0, len(nums)-1

        while beg <= end:
            mid = (beg + end)//2

            if nums[mid] == target:
                return True

            if nums[beg] == nums[mid] == nums[end]:
                beg += 1
                end -= 1

            elif nums[beg] <= nums[mid]:
                if nums[beg] <= target < nums[mid]:
                    end = mid - 1
                else:
                    beg = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    beg = mid + 1
                else:
                    end = mid - 1

        return False
