class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## Sorting
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False


        ## Using Set
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        
        return False

        ## Using Length
        return True if len(set(nums)) < len(nums) else False