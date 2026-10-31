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

        for i in range(n):
            if s[i] not in mapper:
                if t[i] not in mapper.values():
                    mapper[s[i]] = t[i]
                else:
                    return False
            else:
                if mapper[s[i]] != t[i]:
                    return False

        return True   
        # time complexity: worst case: O(n^2), mapper.values() takes o(n) to search

        # map1 = {}
        # map2 = {}

        # for i in range(n):
        #     if s[i] in map1 and map1[s[i]] != t[i]:
        #         return False

        #     if t[i] in map2 and map2[t[i]] != s[i]:
        #         return False

        #     map1[s[i]] = t[i]
        #     map2[t[i]] = s[i]

        # return True
        # time complexity: O(n)

    