class Solution(object):
    def maxSubArray(self, nums):
        curr_max=max_sum=float("-inf")
        for n in nums:
            curr_max=max(curr_max+n,n)
            max_sum=max(max_sum,curr_max)
        return max_sum
        