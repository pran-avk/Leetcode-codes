class Solution(object):
    def subarraySum(self, nums, k):
        freq={0:1}
        count=0
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            value=prefix-k
            count+=freq.get(value,0)
            freq[prefix]=freq.get(prefix,0)+1
        return count

        