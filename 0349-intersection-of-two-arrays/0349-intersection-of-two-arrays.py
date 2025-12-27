class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set()
        arr = []
        for num in nums1:
            if num not in hashset:
                hashset.add(num)

        for num in nums2:
            if num in hashset and num not in arr:
                arr.append(num)

        return arr