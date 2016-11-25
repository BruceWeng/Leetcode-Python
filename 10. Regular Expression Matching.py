class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        #empty string with empty pattern
        dp[0][0] = True
        #handle the first row with empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #check if char in string match the pattern or pattern is '.'
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    #check condition without '*' and one char before
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    #check condition with one or more char before '*'
                    elif s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j]
                else:
                    #not matching, keep dp[i][j] to False
                    continue

        return dp[len(s)][len(p)]
sol = Solution()
sol.isMatch('xaabyc', 'xa*b.c')
