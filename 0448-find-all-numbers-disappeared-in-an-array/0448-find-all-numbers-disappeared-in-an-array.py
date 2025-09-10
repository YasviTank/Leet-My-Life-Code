class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -nums[index]
                
                
        result = []
        for i in range(n):
            if nums[i]  > 0:
                result.append(i + 1)

        return result
