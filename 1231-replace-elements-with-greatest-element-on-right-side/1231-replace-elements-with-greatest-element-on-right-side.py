class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)

        if n == 1:
            return [-1]

        maximum = -1
        for index in range(n - 1, -1, -1):
            variable = arr[index]
            arr[index] = maximum
            maximum = max(maximum, variable)
            
        return arr
            


        