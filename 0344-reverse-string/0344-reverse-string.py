class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l <= r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            # s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1 
        return s

        # ## using recursion:
        # def reverse(left, right):
        #     if left >= right:
        #         return
            
        #     s[left], s[right]= s[right], s[left]
        #     # s[right] = s[left]

        #     reverse(left + 1, right - 1)

        # reverse(0, len(s) - 1)
        