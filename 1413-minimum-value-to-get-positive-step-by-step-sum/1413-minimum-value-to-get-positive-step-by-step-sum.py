class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_start_value = 1
        
        for num in nums:
            prefix_sum += num
            min_start_value = max(min_start_value, 1 - prefix_sum)
        
        return min_start_value