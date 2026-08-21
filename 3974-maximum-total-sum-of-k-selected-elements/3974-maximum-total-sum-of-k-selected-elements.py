class Solution(object):
    def maxSum(self, nums, k, mul):
        prod=0
        nums.sort(reverse=True)
        for i in range(k):
            if mul<1:
                prod+=nums[i]
            else:
                prod+=nums[i]*mul
                mul-=1
        return prod
        