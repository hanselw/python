class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n3 = []
        n3 = nums1 + nums2
        n3.sort()
        lens  = len(n3)
        return  n3[lens/2] if lens % 2!=0 else (n3[lens/2]+n3[lens/2-1])/2.0
        