class Solution(object):
    def maxProduct(self, nums):
        mx=1
        mn=1
        curr_sum=max(nums)
        for n in nums:
            temp=mx*n
            mx=max(mx*n,mn*n,n)
            mn=min(temp,mn*n,n)
            curr_sum=max(curr_sum,mx)
        return curr_sum
        