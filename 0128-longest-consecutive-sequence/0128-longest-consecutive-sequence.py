class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) meaning cant use sorting!

        hashset = set(nums)
        longest = 0

        for n in hashset:
            if (n-1) not in hashset:
                # so we know that n is the start of the sequence
                length = 1
                while (n+length) in hashset:
                    length += 1
                longest = max(longest, length)

        return longest