class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                present_max_profit = prices[j]-prices[i]
                if present_max_profit > max_profit:
                    max_profit = present_max_profit
                    continue
                else:
                    continue
        return max_profit