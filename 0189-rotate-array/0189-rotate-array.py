class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # rotated = [0] * n

        # for i in range(n):
        #     roated[(i+k)%n] = nums[i]


        # for i in range(n):
        #     nums[i] = rotated[i]


        # # Get the actual number of rotations
        # k = k % len(nums)      
        # # Get the number of elements to move from the end to the beginning
        # r = len(nums) - k
        # # Store the elements to move
        # new = nums[0:r]
        # # Remove the elements from the beginning
        # nums[0:r] = []
        # # Append the stored elements to the end
        # nums.extend(new)


        n = len(nums)
        k %= n  # In case k is larger than n
        
        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Reverse the entire array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the remaining n - k elements
        reverse(k, n - 1)