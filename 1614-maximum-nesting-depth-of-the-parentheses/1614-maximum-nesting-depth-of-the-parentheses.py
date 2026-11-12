class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        level = 0
        max_dept = 0

        for bracket in s:
            if bracket == "(":
                level += 1
                if max_dept < level:
                    max_dept = level
            elif bracket == ")":
                level -= 1

        return max_dept