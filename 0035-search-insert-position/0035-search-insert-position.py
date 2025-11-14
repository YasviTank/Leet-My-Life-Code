class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         print(i, nums[i])
        #         return i 
        #     if i == len(nums) - 1:
        #         print(i)
        #         return i + 1
        # This solution is O(n)


        start = 0
        end = len(nums) -1
        mid = 0

        while(start <= end): 
            mid = start + ( end - start)/2
            if(nums[mid] == target): 
                return mid
            elif(nums[mid] < target): 
                start = mid + 1
            else:
                end = mid - 1
    
        return start
        # This solution is O(log n)