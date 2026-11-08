class Solution(object):
    def maxProfit(self, prices):
        min_price=prices[0]
        max_price=0
        for i in prices:
            min_price=min(min_price,i)
            max_price=max(max_price,i-min_price)
        return max_price
        