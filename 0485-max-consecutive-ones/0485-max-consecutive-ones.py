class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        a=0
        for i in nums:
            if i==0:
                a=0
            else:
                a+=1
                count=max(a,count)
        return count
        