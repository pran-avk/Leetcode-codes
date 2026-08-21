class Solution(object):
    def maxSum(self, nums, k, mul):
        a=[-x for x in nums]
        heapq.heapify(a)
        prod=0
        for i in range(k):
            x=-heapq.heappop(a)
            if mul<=0:
                prod+=x
            else:
                prod+=x*mul
                mul-=1
        return prod
                

