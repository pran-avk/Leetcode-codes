class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=[]
        b=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=b:
                a.append(True)
            else:
                a.append(False)
        return a
        