class Solution(object):
    def rob(self, nums):
        if len(nums)<2:
            return nums[-1]
        a=[0]*len(nums)
        a[0]=nums[0]
        a[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            a[i]=max(a[i-1],a[i-2]+nums[i])
        return a[-1]