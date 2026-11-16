class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        total=0
        while i<j:
            if height[i]>height[j]:
                total=max(total,height[j]*((j-i)))
                j-=1
            else:
                total=max(total,height[i]*((j-i)))
                i+=1
        return total
