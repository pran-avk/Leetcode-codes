class Solution(object):
    def subarraySum(self, nums, k):
        freq={0:1}
        count=0
        current_sum=0
        for i in range(len(nums)):
            current_sum+=nums[i]
            needed=current_sum-k
            count+=freq.get(needed,0)
            freq[current_sum]=freq.get(current_sum,0)+1
        return count