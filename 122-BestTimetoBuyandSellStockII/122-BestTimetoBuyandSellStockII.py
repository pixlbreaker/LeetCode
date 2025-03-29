# Last updated: 3/28/2025, 11:42:41 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        valley = prices[0]
        peak = prices[0]
        k = 0
        
        # List of Prices
        while (k < len(prices) -1):
            while ( k < len(prices) -1 and prices[k] >= prices[k+1]):
                k+=1
            valley = prices[k]
            while (k < len(prices) - 1 and prices[k] <= prices[k+1]):
                k+=1
            peak = prices[k]
            profit += peak - valley
        return profit