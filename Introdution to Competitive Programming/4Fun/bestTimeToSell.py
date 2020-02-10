class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_max = 0
        max = 0
        if not prices:
            return 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > buy:
                max = prices[i]-buy
                
                if max > max_max:
                    max_max = max
                print(max,max_max)
            if prices[i] <=buy:
                buy = prices[i]
                
        return max_max
                