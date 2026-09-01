class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        cap=0
        while i<j:
            a=min(height[i],height[j])
            cap=max(cap,a*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return cap
        