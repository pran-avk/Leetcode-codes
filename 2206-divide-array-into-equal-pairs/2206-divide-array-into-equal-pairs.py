class Solution(object):
    def divideArray(self, nums):
        if len(nums)%2!=0:
            return False
        else:
            a=Counter(nums)
            for key,value in a.items():
                while value:
                    if value==1:
                        return False
                    else:
                        value-=2
            return True
        