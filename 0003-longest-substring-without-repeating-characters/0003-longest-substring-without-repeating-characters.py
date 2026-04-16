class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        UniqueSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in UniqueSet:
                UniqueSet.remove(s[l])
                l += 1

            UniqueSet.add(s[r])

            res = max(res, r - l + 1)

        return res