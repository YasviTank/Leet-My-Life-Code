class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for index in range(1, len(nums)):
            nums[index] += nums[index - 1]
        return nums