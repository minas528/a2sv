class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = total_profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] - buy < profit:
                buy = prices[i]
                total_profit += profit
                profit = 0
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        total_profit += profit
        return total_profit
		
