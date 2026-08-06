class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        j=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                i+=1
            else:
                nums[j]=nums[i]
                i+=1
                j+=1
        return j
        