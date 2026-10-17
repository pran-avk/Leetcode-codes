class Solution(object):
    def maxSubArray(self, nums):
        max_s=float("-inf")
        current_sum=float("-inf")
        for i in nums:
            current_sum=max(i,current_sum+i)
            max_s=max(max_s,current_sum)
        return max_s
        