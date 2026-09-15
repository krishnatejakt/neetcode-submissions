class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buyPrice = prices[0]
        result = 0

        for i in range(1, len(prices)):
            buyPrice = min(buyPrice, prices[i])
            result = max(result, prices[i] - buyPrice)
        
        return result