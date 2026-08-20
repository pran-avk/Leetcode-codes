class Solution(object):
    def resultArray(self, nums):
        a=[]
        b=[]
        a.append(nums[0])
        b.append(nums[1])
        i=2
        while i<len(nums):
            if a[-1]>b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])
            i+=1
        a.extend(b)
        return a
        