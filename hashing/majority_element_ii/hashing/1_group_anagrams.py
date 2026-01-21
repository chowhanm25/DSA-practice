from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Problem:
        Group Anagrams

        Given an array of strings, group the anagrams together.

        Example:
        Input: ["eat","tea","tan","ate","nat","bat"]
        Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

        Approach:
        - Use a hash map where:
          key   = sorted version of the word
          value = list of words that share the same characters

        Time Complexity:
        O(n * k log k)

        Space Complexity:
        O(n * k)
        """

        anagram_dict = defaultdict(list)

        for word in strs:
            sorted_key = ''.join(sorted(word))
            anagram_dict[sorted_key].append(word)

        return list(anagram_dict.values())
