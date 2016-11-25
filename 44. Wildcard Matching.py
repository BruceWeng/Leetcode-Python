# Solution1: DP, Time: O(m*n), Space: O(m*n), Memory Limit Exceeded
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]

        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == '*':
                    # '*' matches zero or more than one chars
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    continue
        return dp[m][n]

# Solution2: Four Pointers
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        # string pointer
        i = 0
        # pattern pointer
        j = 0
        # nearest star index
        track = m
        # string index while meet star
        star = 0

        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif  j < n and p[j] == '*':
                star = j
                track = i
                j += 1
            elif track < m:
                i = track + 1
                j = star + 1
                track += 1
            else:
                return False

        while j < n and p[j] == '*':
            j += 1
        return j == n


sol = Solution()
print sol.isMatch('abc', 'a*')
