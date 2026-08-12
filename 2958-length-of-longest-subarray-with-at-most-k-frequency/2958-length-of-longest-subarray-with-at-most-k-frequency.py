class Solution(object):
    def maxSubarrayLength(self, nums, k):
        leng=0
        i=j=0
        a={}
        while i<len(nums):
            a[nums[i]]=a.get(nums[i],0)+1
            if a[nums[i]]>k:
                while a[nums[i]]>k:
                    a[nums[j]]-=1
                    j+=1
            leng=max(leng,i-j+1)
            i+=1
        return leng
        
                    
                


        