class Solution(object):
    def isPalindromic(self, s):
        a=""
        for i in s:
            b=ord(i)
            a+=format(b,'08b')
        return a==a[::-1]
        