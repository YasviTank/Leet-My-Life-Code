class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       n = len(nums)
       j = 0
       i = -1
       count = 0


       while (j<n):

        if(nums[j] != 0):
            j+=1
            continue
        
        count = max(count, j-i-1)
        i = j
        j += 1
       
       count = max(count, j-i-1)
       return count
        
    


    

    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = 0
        # maxx = 0
        # k = 0
        # for i in nums:
        #     if i == 1:
        #         count += 1
        #         maxx = max(count, maxx)
        #     else:
        #         maxx = max(count, maxx)
        #         count = 0
        # return maxx