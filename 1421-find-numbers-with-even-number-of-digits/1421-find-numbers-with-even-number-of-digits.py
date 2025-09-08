class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        for num in nums:
            num = str(num)
            if len(num)%2 == 0:
                even +=1
        return even