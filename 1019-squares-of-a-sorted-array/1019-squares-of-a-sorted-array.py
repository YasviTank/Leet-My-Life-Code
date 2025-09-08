class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for num in nums:
            arr.append(abs(num)*abs(num))
            print(num)
        return sorted(arr)