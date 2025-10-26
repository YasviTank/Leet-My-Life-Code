class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -1
        second_max = -1
        index = 0
        for i, num in enumerate(nums):
            if num > max:
                second_max = max
                index = i
                max = num

            elif num > second_max:
                second_max = num
                
        print(max, second_max)
        if (max >= (2*second_max)):
            return index

        return -1