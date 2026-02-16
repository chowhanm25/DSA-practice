class Solution(object):
    def checkInclusion(self, s1, s2):
        # If s1 longer than s2 → impossible
        if len(s1) > len(s2):
            return False

        # frequency count for a-z
        s1_count = [0] * 26
        window_count = [0] * 26

        # count letters of s1
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        # first window in s2
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1

        # check first window
        if s1_count == window_count:
            return True

        # slide window
        for i in range(len(s1), len(s2)):
            # add new char
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # remove old char
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # compare
            if s1_count == window_count:
                return True

        return False

