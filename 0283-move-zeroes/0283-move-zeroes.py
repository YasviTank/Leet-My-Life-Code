class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        for index in range(n):
            if nums[index] != 0 and n!=1:
                nums[count] = nums[index]
                # nums[index] = 0
                count += 1
        for i in range(count,n ):
            if n!=1:
                nums[i] = 0
            