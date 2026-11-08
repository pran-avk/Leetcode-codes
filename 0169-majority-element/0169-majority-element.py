class Solution(object):
    def majorityElement(self, nums):
        a=Counter(nums)
        keys=-1
        values=-1
        for key,value in a.items():
            if value>values:
                keys=key
                values=value
        return keys

            
        