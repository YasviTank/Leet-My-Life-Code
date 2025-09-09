class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for index in range(len(arr)):
            sq = arr[index]*2
            div = arr[index]/2
            for i in range(len(arr)):
                if arr[i] == sq and i!=index:
                    return True
        return False