class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        ans = float('inf')

        for right in range(n):
            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans
        
        
        
        
        
        
        
        
        
        # j = 0
        # i = -1
        # n = len(nums)
        # length = n
        # total = 0

        # while (j<n):
        #     total += nums[j]
        #     print("t",total)
        #     if total < target:
        #         j+=1
        #         print(j)
        #     elif total == target:
        #         length = min(length, j-i)
        #         print("length", length)
        #         i = j
        #         j += 1
        #     else:
        #         i = j
        #         j += 1
        #         print("j", j)
        #         total = 0
        # if total!=target:
        #     length = 0
        # return length
        