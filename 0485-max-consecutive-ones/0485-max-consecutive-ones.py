class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxx = 0
        k = 0
        for i in nums:
            if i == 1:
                count += 1
                maxx = max(count, maxx)
            else:
                maxx = max(count, maxx)
                count = 0
        return maxx