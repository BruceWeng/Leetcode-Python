class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        stack = []
        sign = 1
        n = len(s)
        ans = num = 0
        for i in range(n):
            if s[i] == ' ' and i != n - 1: continue
            if '0' <= s[i] <= '9':
                num = num * 10 + int(s[i])
            if s[i] in ['+', '-', '(', ')'] or i == n - 1:
                if s[i] == '(':
                    stack.append(ans)
                    stack.append(sign)
                    ans = 0
                    sign = 1
                elif s[i] == ')':
                    ans += num * sign
                    sign = stack.pop()
                    num = stack.pop()
                    ans = num + ans * sign
                    sign = 1
                else:
                    ans += num * sign
                    sign = 1 if s[i] == '+' else  -1
                num = 0
        return ans

sol = Solution()
test1 = "1 + - (2 - 3) + 1" #3
print sol.calculate(test1)
