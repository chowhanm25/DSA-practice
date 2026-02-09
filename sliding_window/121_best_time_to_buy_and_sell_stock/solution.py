class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        max_current = 0
        max_global = 0
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            max_current = max(0, max_current + change)
            max_global = max(max_global, max_current)
        
        return max_global

