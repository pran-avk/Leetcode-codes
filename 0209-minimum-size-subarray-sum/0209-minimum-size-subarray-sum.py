class Solution(object):
    def minSubArrayLen(self, target, nums):
        j=0
        leng=float("inf")
        su=0
        for i in range(len(nums)):
            su+=nums[i]
            while su>=target:
                leng=min(leng,i-j+1)
                su-=nums[j]
                j+=1
        return leng if leng!=float("inf") else 0
                
        
        