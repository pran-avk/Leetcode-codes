class Solution(object):
    def longestPalindrome(self, s):
        a=Counter(s)
        counter=0
        b=0
        for key,values in a.items():
            counter+=values//2
            a[key]=values%2
        for key,values in a.items():
            if values==1:
                b+=1
                break
        return counter*2+b
                
        