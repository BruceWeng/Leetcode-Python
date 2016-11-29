# Need to think case by case
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s == None or s[0] == '0':
            return 0

        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            if 10 < int(s[i - 2:i]) <= 26 and int(s[i - 1]) != 0:
                dp[i] += dp[i - 1] + dp[i - 2]
            elif int(s[i - 2: i]) == 10 or int(s[i - 2: i]) == 20:
                dp[i] = dp[i - 2]
            elif int(s[i - 1]) != 0:
                dp[i] = dp[i - 1]
            else:
                return 0

        return dp[len(s)]

sol = Solution()
test1 = '11'
print sol.numDecodings(test1) #3
