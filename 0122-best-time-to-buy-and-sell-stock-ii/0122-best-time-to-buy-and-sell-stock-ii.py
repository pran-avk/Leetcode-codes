class Solution(object):
    def maxProfit(self, prices):
        buy=0
        profit=0
        i=0
        while i<(len(prices)-1):
            if prices[i]<prices[i+1]:
                buy=prices[i]
                while i<len(prices)-1 and prices[i]<prices[i+1]:
                    i+=1
                profit+=prices[i]-buy
                buy=0
            i+=1
        return profit