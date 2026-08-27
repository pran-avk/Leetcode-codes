class Solution(object):
    def isMiddleElementUnique(self, nums):
        a=len(nums)//2
        count=0
        for i in range(len(nums)):
            if nums[i]==nums[a]:
                count+=1
        return count==1
        