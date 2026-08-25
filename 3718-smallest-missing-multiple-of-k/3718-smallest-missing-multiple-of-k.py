class Solution(object):
    def missingMultiple(self, nums, k):
        a=set(nums)
        for i in range(1,len(nums)+2):
            b=k*i
            if b in a:
                continue
            else:
                return b
        