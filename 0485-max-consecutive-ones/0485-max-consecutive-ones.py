class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = 0
        count = 1
        if len(nums)==1 and nums != [0]:
            return 1
        if nums == [0,0] or nums == [0,0,0]:
            return 0
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1] and nums[index]!=0:
                count+=1
                
                # if high<count:
                #     high = count
            else:
                count = 1
            if high<count:
                high = count
        return high