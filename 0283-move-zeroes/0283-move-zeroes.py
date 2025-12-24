class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0

        if n == 1:
            return nums

        for j in range(n):
            if nums[j] != 0:
                nums[left] = nums[j]
                left+=1

        for j in range(left, n):
            nums[j] = 0


