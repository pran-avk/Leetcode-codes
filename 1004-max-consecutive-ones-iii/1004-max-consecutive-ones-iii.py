class Solution(object):
    def longestOnes(self, nums, k):
        on=0
        i=j=0
        le=0
        while i<len(nums):
            if nums[i]==0:
                on+=1
            if on>k:
                while nums[j]!=0:
                    j+=1
                j+=1
                on-=1
            le=max(le,i-j+1)
            i+=1
        return le
            
            
        