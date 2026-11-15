class Solution(object):
    def jump(self, nums):
        max_reach=0
        count=0
        current_end=0
        for i in range(len(nums)-1):
            max_reach=max(max_reach,i+nums[i])
            if i==current_end:
                count+=1
                current_end=max_reach
        return count