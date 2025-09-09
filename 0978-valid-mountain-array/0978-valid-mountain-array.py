class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n  = len(arr)
        
        if n<3:
            return False

        i = 0
        j = n - 1

        while i + 1 < n and arr[i] < arr[i + 1]: i += 1
        while j > 0 and arr[j] < arr[j - 1] : j -= 1

        return i == j and i > 0 and j < n - 1
        
