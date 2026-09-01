class Solution(object):
    def sortArrayByParity(self, nums):
        odd=[]
        even=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.extend(odd)
        return even
            
        