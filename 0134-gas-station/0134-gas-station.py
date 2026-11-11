class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total=0
        current=0
        start=0
        for i in range(len(cost)):
            diff=gas[i]-cost[i]
            total+=diff
            current+=diff
            if current<0:
                start=i+1
                current=0
        if total<0:
            return -1
        return start