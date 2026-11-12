class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count1 = count2 = 0
        res = ""
        for bracket in s:
            if bracket == "(":
                count1 += 1
                if count1 > 1:
                    res += bracket
            else:
                count2 += 1
                if count1 != count2:
                    res += bracket
                else:
                    count1 = count2 = 0
                
        return res
