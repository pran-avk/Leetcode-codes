class Solution(object):
    def sortArrayByParityII(self, nums):
        odd=[]
        even=[]
        for i in nums:
            if i%2!=0:
                odd.append(i)
            elif i%2==0:
                even.append(i)
        a=[]
        for i in range(len(odd)):
            a.append(even[i])
            a.append(odd[i])
        return a      