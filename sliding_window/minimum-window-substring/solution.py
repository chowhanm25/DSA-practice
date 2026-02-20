class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # if impossible
        if len(t) > len(s):
            return ""

        from collections import Counter

        # frequency required
        need = Counter(t)

        # current window frequency
        window = {}

        # how many characters satisfied
        have = 0
        need_count = len(need)

        # result tracking
        res = [-1, -1]
        res_len = float("inf")

        left = 0

        # expand window
        for right in range(len(s)):
            char = s[right]

            # add char into window
            window[char] = window.get(char, 0) + 1

            # check if this char requirement satisfied
            if char in need and window[char] == need[char]:
                have += 1

            # shrink window when valid
            while have == need_count:

                # update best answer
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # remove left char
                left_char = s[left]
                window[left_char] -= 1

                # if requirement broken → window invalid
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1  # shrink

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
