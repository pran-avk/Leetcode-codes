class Solution(object):
    def runningSum(self, nums):
        pr=[0]*len(nums)
        pr[0]=nums[0]
        for i in range(1,len(nums)):
            pr[i]=nums[i]+pr[i-1]
        return pr

        