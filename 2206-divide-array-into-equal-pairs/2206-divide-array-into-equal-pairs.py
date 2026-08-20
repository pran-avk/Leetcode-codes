class Solution(object):
    def divideArray(self, nums):
        if len(nums)%2!=0:
            return False
        else:
            a=Counter(nums)
            for key,value in a.items():
                if value%2!=0:
                    return False
            return True
        