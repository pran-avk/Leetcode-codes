class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count=0
        i=j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count

        