class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        current_sum=0
        freq={0:1}
        for n in nums:
            current_sum+=n
            needed=current_sum-k
            count+=freq.get(needed,0)
            freq[current_sum]=freq.get(current_sum,0)+1
        return count
        