class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for index in range(len(nums) -1, -1, -1):
            if abs(nums[left]) > nums[right]:
                res[index] = nums[left]*nums[left]
                left += 1
            else:
                res[index] = nums[right]*nums[right]
                right -= 1

        return res