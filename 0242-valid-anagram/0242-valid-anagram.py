class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in t:
            if letter in count and count[letter] > 0:
                count[letter] -= 1
            else:
                return False

        return True