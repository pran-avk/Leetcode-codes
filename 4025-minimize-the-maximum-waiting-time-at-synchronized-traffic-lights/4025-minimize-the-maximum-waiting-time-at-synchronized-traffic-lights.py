class Solution(object):
    def minPenalty(self, period, lights, arrivalTime):
        a=max(lights)
        total=0
        for i in arrivalTime:
            b=i%period
            if b>=a:
                total=max(total,period-b)
        return total