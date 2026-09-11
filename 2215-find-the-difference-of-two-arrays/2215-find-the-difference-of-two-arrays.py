class Solution(object):
    def findDifference(self, nums1, nums2):
        a=set(nums1)
        b=set(nums2)
        d=[]
        c=[]
        for i in list(a):
            if i not in b:
                c.append(i)
        d.append(c)
        c=[]
        for i in list(b):
            if i not in a:
                c.append(i)
        d.append(c)
        return d

        