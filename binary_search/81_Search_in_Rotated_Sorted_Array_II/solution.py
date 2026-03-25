class Solution(object):
    def search(self, nums, target):
        beg, end = 0, len(nums)-1

        while beg <= end:
            mid = (beg + end)//2

            if nums[mid] == target:
                return True

            # Handle duplicates
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
