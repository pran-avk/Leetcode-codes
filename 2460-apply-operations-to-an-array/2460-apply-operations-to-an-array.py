class Solution(object):
    def applyOperations(self, nums):
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums[i-1]=(nums[i-1])*2
                nums[i]=0
            i+=1
        i=j=0
        while i<len(nums):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                i+=1
        return nums
                    