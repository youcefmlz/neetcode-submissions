class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buying_price = float('inf')
        max_profit = 0
    
        for price in prices: 
            max_profit = max(max_profit, price -lowest_buying_price )
            lowest_buying_price = min(lowest_buying_price, price)
            
        return max_profit



