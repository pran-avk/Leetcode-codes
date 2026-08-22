class Solution(object):
    def checkDivisibility(self, n):
        prod=1
        su=0
        b=n
        while n>0:
            a=n%10
            prod*=a
            su+=a
            n=n//10
        m=prod+su
        return b%m==0
        