class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        if dp[amount] > amount:
            return -1
        return dp[amount]
