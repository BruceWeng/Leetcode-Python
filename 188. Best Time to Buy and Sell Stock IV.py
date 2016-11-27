class Solution(object):
    # Solution 1: Time Limit Exceeded
    # Time: O(k * days^2)
    # Space: O(k * days)
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0 or prices == None:
            return 0

        dp = [[0 for j in range(len(prices))] for i in range(k + 1)]

        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                maxVal = 0
                for m in range(j):
                    maxVal = max(maxVal, prices[j] - prices[m] + dp[i - 1][m])

                dp[i][j] = max(dp[i][j - 1], maxVal)

        return dp[k][len(prices) - 1]

    # Solution 2: MemoryError
    # Time: O(k * days)
    # Space: O(k * days)
    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0 or prices == None:
            return 0

        dp = [[0 for j in range(len(prices))] for i in range(k + 1)]

        for i in range(1, k + 1):
            maxDiff = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])

        return dp[k][len(prices) - 1]

    # Solution 3: MemoryError
    # Time: O(k * days)
    # Space: O(2 * days)
    def maxProfit3(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0 or prices == None:
            return 0

        dp = [[0 for j in range(len(prices))] for i in range(2)]

        for i in range(1, k + 1):
            maxDiff = -prices[0]
            for j in range(1, len(prices)):
                dp[i % 2][j] = max(dp[i % 2][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[(i - 1) % 2][j] - prices[j])

        return dp[k % 2][len(prices) - 1]

    # Solution 4: Reduce to unlimited transaction when k > days
    # Time: O(days^2)
    # Space: O(2 * days)
    def maxProfit4(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0 or prices == None:
            return 0

        if k > len(prices):
            maxVal = 0

            for i in range(len(prices) - 1):
                if prices[i + 1] > prices[i]:
                    maxVal += prices[i + 1] - prices[i]

            return maxVal
            
        dp = [[0 for j in range(len(prices))] for i in range(2)]

        for i in range(1, k + 1):
            maxDiff = -prices[0]
            for j in range(1, len(prices)):
                dp[i % 2][j] = max(dp[i % 2][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[(i - 1) % 2][j] - prices[j])

        return dp[k % 2][len(prices) - 1]

sol = Solution()
test1 = [2, 5, 7, 1, 4, 3, 1, 3]
k = 3
print sol.maxProfit3(k, test1)
