class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        i = -1

        while l <= r:
            
            if abs(nums[l]) > nums[r]:
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1
            i -= 1

        return res
