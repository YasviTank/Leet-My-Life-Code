class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        count = 0

        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                count += 1
        
        for i in range(n-j):
            nums[-i-1] = 0