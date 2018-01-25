"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
"""
Algorithm:
left = right = n
left parentheses # must >= right parentheses #
if left == 0 and right == 0: result.append(current), return
if left > 0 :allow to add "(" and recursive call
if right > left: allow to add ")" and recursive call
"""
"""
@param {int} n
@return {string[]}
"""
def generateParenthesis(n):
    if n == 0: return []

    result = []

    def dfs(left, right, current):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            dfs(left - 1, right, current + "(")

        if right > left:
            dfs(left, right - 1, current + ")")

    dfs(n, n, "")
    return result

if __name__=="__main__":
    print(generateParenthesis(3))
