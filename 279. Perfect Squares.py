# Time: O(n * sqrt(n))
# Space: O(n)
# Time Limit Exceeded
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint for i in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1

        return dp[n]

sol = Solution()
print sol.numSquares(13) # 2
