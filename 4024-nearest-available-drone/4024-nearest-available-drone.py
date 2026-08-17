class Solution(object):
    def nearestDrone(self, drones, target):
        min_drone=-1
        value=float("inf")
        for j,i in enumerate(drones):
            total=0
            a=abs(i[0] - target[0])
            b=abs(i[1]-target[1])
            if a+b<=i[2] and a+b<value:
                value=a+b
                min_drone=j
        return min_drone
                
            
        