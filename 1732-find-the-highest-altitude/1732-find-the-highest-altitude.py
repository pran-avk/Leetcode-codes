class Solution(object):
    def largestAltitude(self, gain):
        pr=[0]*((len(gain))+1)
        for i in range(1,len(gain)+1):
            pr[i]=pr[i-1]+gain[i-1]
        return max(pr)
        