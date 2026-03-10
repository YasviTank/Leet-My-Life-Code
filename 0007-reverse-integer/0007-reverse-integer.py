class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if x == 0:
            return x
        s = ""
        neg = False

        if x<0:
            x = abs(x)
            neg = True
            
        while x:
            num = x%10
            s += str(num)
            x = x//10
        
        reversed_int = int(s)
        if neg:
            reversed_int = -reversed_int
        
        # Check for 32-bit overflow
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        return reversed_int