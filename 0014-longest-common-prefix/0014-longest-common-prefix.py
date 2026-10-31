class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        base_string = strs[0]

        for i in range(len(base_string)):
            for s in strs[1:]:
                if i == len(s) or base_string[i] != s[i]:
                    return base_string[0:i]

        return base_string


        

        