class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        tot=0
        start=0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            tot+=diff
            if tot<0:
                tot=0
                start=i+1
        return start

        