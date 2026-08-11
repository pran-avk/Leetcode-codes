class Solution(object):
    def missingInteger(self, nums):
        a=set(nums)
        i=1
        sumi=nums[0]
        while i<len(nums):
            if nums[i]==nums[i-1]+1:
                sumi+=nums[i]
                i+=1
            else:
                break
        while sumi in a:
            sumi+=1
        return sumi        