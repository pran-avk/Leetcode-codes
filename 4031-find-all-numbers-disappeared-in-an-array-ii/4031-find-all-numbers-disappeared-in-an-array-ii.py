class Solution(object):
    def findDisappearedNumbers(self, nums, lower, upper):
        a=set(nums)
        b=[]
        start=None
        for i in range(lower,upper+1):
            if start is None and i not in a:
                start=i
            elif start and i in a:
                b.append([start,i-1])
                start=None
            
        if start is not None:
            b.append([start,upper])
        return b
            
        