class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        largest = float('-inf')
        second_largest = float('-inf')
        index_of_largest = -1

        for i, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                index_of_largest = i
            elif num > second_largest:
                second_largest = num

        if largest >= 2 * second_largest:
            return index_of_largest
        return -1
