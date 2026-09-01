class Solution(object):
    def sortedSquares(self, nums):
        if len(nums)==1:
            return [nums[0]**2]
        elif len(nums)==0:
            return 
        a=[]
        i=0 
        j=None
        while i<len(nums) and nums[i]<0 :
            i+=1
        if i!=0:
            j=i-1
        while j is not None and(j>=0 and i<len(nums)):
            if (nums[j])**2<nums[i]**2:
                a.append(nums[j]**2)
                j-=1
            else:
                a.append(nums[i]**2)
                i+=1
        while j is not None and  j>=0:
            a.append(nums[j]**2)
            j-=1
        while i<len(nums):
            a.append(nums[i]**2)
            i+=1
        return a
            
        