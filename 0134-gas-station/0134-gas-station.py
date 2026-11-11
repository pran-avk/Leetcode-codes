class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        a=sum(gas)
        b=sum(cost)
        if a-b<0:
            return -1
        start=0
        su=0
        for i in range(len(cost)):
            diff=gas[i]-cost[i]
            su+=diff
            if su<0:
                start=i+1
                su=0
        return start
        