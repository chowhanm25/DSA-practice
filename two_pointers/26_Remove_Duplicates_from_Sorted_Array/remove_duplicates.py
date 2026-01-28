cat > remove_duplicates.py << EOL
"""
26_Remove_Duplicates_from_Sorted_Array
LeetCode_Problem_Easy
Topics_Two_Pointers_Arrays
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    i = 0  # last_unique_element_index

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == "__main__":
    nums = [1,1,2,2,3]
    k = removeDuplicates(nums)
    print(f"number_of_unique_elements: {k}")
    print(f"modified_array_first_k_elements_are_unique: {nums[:k]}")
EOL

