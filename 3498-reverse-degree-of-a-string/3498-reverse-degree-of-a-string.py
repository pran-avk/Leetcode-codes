class Solution(object):
    def reverseDegree(self, s):
        s=list(s)
        count=0
        for i in range(len(s)):
            count+=(123-ord(s[i]))*(i+1)

        return count
        