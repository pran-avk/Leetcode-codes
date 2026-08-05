class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=set()
        i=j=0
        length=0
        while i<len(s):
            while s[i] in a:
                a.remove(s[j])
                j+=1
            length=max(length,i-j+1)
            a.add(s[i])
            i+=1
        return length

        