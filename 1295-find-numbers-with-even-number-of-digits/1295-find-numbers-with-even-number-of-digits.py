class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in nums:
            a=0
            while i>0:
                i=i//10
                a+=1
            if a%2==0:
                count+=1
        return count
            
        