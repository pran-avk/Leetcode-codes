class Solution(object):
    def maxProduct(self, nums):
        maxi=1
        mini=1
        res=max(nums)
        for n in nums:
            if n==0:
                maxi=1
                mini=1
                continue
            temp=maxi*n
            maxi=max(maxi*n,mini*n,n)
            mini=min(temp,mini*n,n)
            res=max(maxi,res)
        return res
        