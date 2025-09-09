class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if nums1 == []:
            nums1 = nums2

        i = n+m-1
        n-=1
        m-=1
        while n>=0:
            if nums2[n] < nums1[m] and m>=0:
                nums1[i] = nums1[m]
                m-=1
                print(nums1)
            else:
                nums1[i] = nums2[n]
                n-=1

                
            i-=1
