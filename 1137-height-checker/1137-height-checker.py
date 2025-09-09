class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        arr = sorted(heights)
        count = 0

        for i in range(len(arr)):
            if arr[i] != heights[i]:
                count+=1

        return count