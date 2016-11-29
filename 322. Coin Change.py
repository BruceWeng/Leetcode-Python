import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0 or coins == None:
            return -1

        dp = [sys.maxint for i in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == sys.maxint:
            return -1
        return dp[amount]

sol = Solution()
coin1 = [1, 2, 5]
amount1 = 13
print sol.coinChange(coin1, amount1) #4
