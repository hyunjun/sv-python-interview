class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, profit = inf, 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
