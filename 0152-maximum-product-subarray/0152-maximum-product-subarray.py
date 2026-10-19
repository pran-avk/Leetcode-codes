class Solution(object):
    def maxProduct(self, nums):
        mini=1
        maxi=1
        max_prod=max(nums)
        for n in nums:
            if n==0:
                mini=maxi=1
                continue
            temp=maxi*n
            maxi=max(maxi*n,mini*n,n)
            mini=min(mini*n,temp,n)
            max_prod=max(max_prod,maxi)
        return max_prod
    
        