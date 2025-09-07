class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for index in range(len(nums)):
            sum = 0
            for i in range(index+1):
                sum += nums[i]
            arr.append(sum)

        return arr