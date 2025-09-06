class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        arr = []
        for index in range(len(nums)):
            if nums[index] != val:
                arr.append(nums[index])
                count+=1
            else:
                pass
        for i in range(count):
            nums[i] = arr[i]
        return count
        