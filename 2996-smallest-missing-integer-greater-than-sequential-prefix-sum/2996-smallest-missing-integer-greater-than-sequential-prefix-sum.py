class Solution(object):
    def missingInteger(self, nums):
        a=set(nums)
        i=1
        sumi=nums[0]
        while i<len(nums):
            if nums[i]!=nums[i-1]+1:
                break
            sumi+=nums[i]
            i+=1
        while sumi in a:
            sumi+=1
        return sumi        