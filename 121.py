class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] < buy_price:
                buy_price = prices[idx]
            profit = max(profit, prices[idx] - buy_price)
        return profit