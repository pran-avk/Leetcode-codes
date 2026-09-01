class Solution(object):
    def pivotIndex(self, nums):
        a=sum(nums)
        a-=nums[0]
        tot=0
        if a==tot:
            return 0
        for i in range(1,len(nums)):
            a-=nums[i]
            tot+=nums[i-1]
            if a==tot:
                return i
        return -1
        