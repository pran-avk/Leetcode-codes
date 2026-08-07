class Solution(object):
    def findUnsortedSubarray(self, nums):
        a=0 
        mini=float('inf')
        maxi=nums[0]
        j=0
        for i in range(1,len(nums)):
            maxi=max(maxi,nums[i])
            if nums[i]<maxi:
                mini=min(mini,nums[i])
                a=1
                j=i
        if a==1:
            i=0
            while nums[i]<=mini:
                i+=1
            return j-i+1
        else:
            return 0

        