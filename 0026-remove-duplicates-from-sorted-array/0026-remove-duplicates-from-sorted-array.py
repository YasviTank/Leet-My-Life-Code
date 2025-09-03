class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = []
        arr.append(nums[0])
        # count = -1
        for index in range(1, n):
            if nums[index] != arr[-1]:
                # print(index, nums[index], arr[count])
                arr.append(nums[index])
                # print(arr)
                # print(count)
                # count-=1
            else:
                pass
        m = len(arr)
        for i in range(m):
            nums[i] = arr[i]
        return len(arr)



