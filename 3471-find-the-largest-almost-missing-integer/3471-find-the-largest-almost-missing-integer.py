class Solution(object):
    def largestInteger(self, nums, k):
        a = {}

        for i in range(len(nums) - k + 1):
            b = nums[i:i+k]

            for j in set(b):
                a[j] = a.get(j, 0) + 1
        ans = -1
        for j in a:
            if a[j] == 1:
                ans = max(ans, j)
        return ans