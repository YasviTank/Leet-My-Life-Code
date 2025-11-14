class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        for i in range(len(nums)):
            if nums[i] > target:
                print(i, nums[i])
                return i 
            if i == len(nums) - 1:
                print(i)
                return i + 1
            