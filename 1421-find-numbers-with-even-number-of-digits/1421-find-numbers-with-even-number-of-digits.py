class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        for num in nums:
            num = str(num)
            count = 0
            for digit in num:
                count+=1
            if count%2 == 0:
                even +=1
        return even