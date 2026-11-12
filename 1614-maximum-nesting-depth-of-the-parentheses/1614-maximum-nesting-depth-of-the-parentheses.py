class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        level = 0
        max_dept = 0

        for bracket in s:
            print(bracket)
            if bracket == "(":
                level += 1
                if max_dept < level:
                    max_dept = level
                    print("max_dept", max_dept)
            elif bracket == ")":
                level -= 1
                print("l",level)

        return max_dept