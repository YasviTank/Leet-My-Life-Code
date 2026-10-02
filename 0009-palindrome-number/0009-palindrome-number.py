class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        n = x
        reverse = 0
        while n:
            a = n%10
            reverse = reverse*10 + a
            n = n//10

        return (reverse == x)