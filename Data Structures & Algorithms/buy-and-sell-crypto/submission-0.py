class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        if max_profit < 0:
            max_profit = 0
        return max_profit