from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count how many times each number appears
        frequency_map = Counter(nums)

        # Step 2: Group numbers by their frequency
        frequency_groups = {}
        for number, frequency in frequency_map.items():
            if frequency not in frequency_groups:
                frequency_groups[frequency] = []
            frequency_groups[frequency].append(number)

        # Step 3: Collect the k most frequent elements
        result = []
        max_frequency = max(frequency_groups.keys())

        for freq in range(max_frequency, 0, -1):
            if freq in frequency_groups:
                for number in frequency_groups[freq]:
                    result.append(number)
                    if len(result) == k:
                        return result

