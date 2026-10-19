class Solution(object):
    def targetIndices(self, nums, target):
        a=[]
        nums.sort()
        for i,j in enumerate(nums):
            if j==target:
                a.append(i)
        return a