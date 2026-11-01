class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)
        m = len(goal)

        if n != m:
            return False

        goal += goal

        if s in goal:
            return True

        return False
