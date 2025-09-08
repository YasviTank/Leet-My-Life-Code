class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Initialize a counter variable i to 0
        i = 0

        # Iterate through the elements of the array
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                
                # Remove the last element in the list
                arr.pop()
                
                # Move the counter by 2 to skip the next element (the one we just inserted)
                i += 2
            else:
                # If the current element is not 0, move the counter by 1
                i += 1
