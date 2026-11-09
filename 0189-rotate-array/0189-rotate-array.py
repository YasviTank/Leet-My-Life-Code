class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        # Reverse the entire array
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])