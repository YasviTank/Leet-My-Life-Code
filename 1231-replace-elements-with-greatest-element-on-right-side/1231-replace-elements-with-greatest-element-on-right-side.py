class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)

        if n == 1:
            return [-1]

        for index in range(n - 2, -1, -1):
            variable = arr[index]
            if index == n - 2:
                arr[index] = arr[index+1]
                new = variable
            else:
                arr[index] = max(new, arr[index+1])
                new = variable
                # print("new", new, arr[index+1])
            # print (arr)
        arr[n-1] = -1
        return arr
            


        