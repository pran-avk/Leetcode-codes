class Solution(object):
    def maxProduct(self, nums):
        res=max(nums)
        currmin=currmax=1
        for n in nums:
            if n==0:
                currmax=currmin=1
                continue
            temp=currmax*n
            currmax=max(temp,currmin*n,n)
            currmin=min(temp,currmin*n,n)
            res=max(res,currmax)
        return res
        