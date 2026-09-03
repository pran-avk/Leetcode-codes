class Solution(object):
    def strStr(self, haystack, needle):
        a=len(needle)
        for i in range(len(haystack)-a+1):
            if haystack[i:i+a]==needle:
                return i
        return -1
        