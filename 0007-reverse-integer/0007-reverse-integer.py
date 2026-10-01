class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        reverse = 0
        n = abs(x)

        while n:
            a = n%10
            reverse = (reverse*10) + a
            n = n//10

        if reverse < INT_MIN or reverse > INT_MAX:
            return 0 
            
        if x < 0:
            return -reverse
        else:
            return reverse
        