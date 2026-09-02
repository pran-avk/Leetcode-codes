class Solution(object):
    def findMaxAverage(self, nums, k):
        b=sum(nums[:k])
        max_sum=b
        for i in range(1,len(nums)-k+1):
            b-=nums[i-1]
            b+=nums[i+k-1]
            max_sum=max(max_sum,b)
        return float(max_sum)/k
