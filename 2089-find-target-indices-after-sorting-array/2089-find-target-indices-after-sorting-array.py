class Solution(object):
    def targetIndices(self, nums, target):
        small=0
        equal=0
        for n in nums:
            if n<target:
                small+=1
            elif n==target:
                equal+=1
        a=[]
        for i in range(small,small+equal):
            a.append(i)
        return a
        