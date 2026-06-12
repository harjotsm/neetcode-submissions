class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        day = prices[0]

        for i in range(len(prices)):
            diff = prices[i] - day
            profit = max(diff, profit)

            if diff <= 0:
                day = prices[i]
        
        return profit