class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n != m:
            return False 

        mapper = {}

        for i in range(len(s)):
            if s[i] not in mapper:
                if t[i] not in mapper.values():
                    mapper[s[i]] = t[i]
                else:
                    return False
            else:
                if mapper[s[i]] != t[i]:
                    return False

        return True

    