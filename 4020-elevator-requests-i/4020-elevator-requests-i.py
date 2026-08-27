class Solution(object):
    def elevatorRequests(self, n, requests):
        a=0
        sumi=0
        for i in requests:
            sumi+=abs(i-a)
            a=i
        return sumi
        