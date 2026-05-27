class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        local_profit ="-inf"

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                local_profit = prices[j] - prices [i]
                if local_profit > profit:
                    profit = local_profit
        
        return profit