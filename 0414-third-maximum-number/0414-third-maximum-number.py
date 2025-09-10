class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        high = float('-inf')
        mid = float('-inf')
        low = float('-inf')
        for num in nums:
            if num > low and high!=num and mid!=num:
                if num > high:
                    low = mid
                    mid = high
                    high = num

                elif num > mid:
                    low = mid
                    mid = num
                else: 
                    low = num
                # high = num
                print(high, mid, low)
        if low == float('-inf'):
            return high


        return low
            

    