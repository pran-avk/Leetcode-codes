class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            a=numbers[i]+numbers[j]
            if a==target:
                return [i+1,j+1]
            elif a>target:
                j-=1
            else:
                i+=1
        return None
        