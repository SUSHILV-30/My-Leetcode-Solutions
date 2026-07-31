class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        total = 0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                total+=prices[i] - prices[i-1]
        return total
