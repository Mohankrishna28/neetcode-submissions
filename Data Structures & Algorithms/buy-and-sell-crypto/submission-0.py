class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxprofit = 0
        for price in prices:
            if(price<buy):
                buy = price
            else:
                profit = price - buy
                maxprofit = max(maxprofit,profit)
        return maxprofit
        