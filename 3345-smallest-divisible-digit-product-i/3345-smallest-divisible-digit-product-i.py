class Solution(object):
    def smallestNumber(self, n, t):
        for j in range(n,n+t):
            i=j
            a=1
            while i>0:
                b=i%10
                a*=b
                i=i//10
            if a%t==0:
                return j
            
        