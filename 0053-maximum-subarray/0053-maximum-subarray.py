class Solution(object):
    def maxSubArray(self, nums):
        max_sum=nums[0]
        curr_sum=max_sum
        for i in range(1,len(nums)):
            curr_sum=max(curr_sum+nums[i],nums[i])
            max_sum=max(max_sum,curr_sum)
        return max_sum
        