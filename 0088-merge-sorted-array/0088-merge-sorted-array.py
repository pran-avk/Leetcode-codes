class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=0
        while i<n:
            nums1[m+i]=nums2[i]
            i+=1
        nums1.sort()
        return nums1