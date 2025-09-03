class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = []
        arr.append(nums[0])
        count = -1
        for index in range(1, n):
            if nums[index] != arr[count]:
                # print(index, nums[index], arr[count])
                arr.append(nums[index])
                # print(arr)
                # print(count)
                # count-=1
            else:
                pass
        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(arr)



