"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
"""
Algorithm1: Counter + Backtracking
Explanation:
1. We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
   The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative,
   we have more ‘)’ than ‘(‘ in the prefix.

2. To make the prefix valid, we need to remove a ‘)’. The problem is: which one?
   The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results,
   for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself
   to remove the first ) in a series of concecutive )s.

3. After the removal, the prefix is then valid. We then call the function recursively
   to solve the rest of the string. However, we need to keep another information: the last
   removal position. If we do not have this position, we will generate duplicate by removing two ‘)’
   in two steps only with a different order.

4. For this, we keep tracking the last removal position and only remove ‘)’ after that.

5. Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
   The answer is: do the same from right to left.
   However a cleverer idea is: reverse the string and reuse the code!

T: Remove ')':
       Iterate s: O(n)
       Find child node: O(2^n)
   reverse s and do the algorithm again to remove '(':
       Iterate s: O(n)
       Find child node: O(2^n)
   Total: O(n * 2^n * 2) = O(n * 2^n)

S: O(n * 2^n)

Note: Special backtracking, to reuse the code for right to left and keep count valid,
write the termination condition after recursive condition
"""
"""
@param {str} s
@return {str[]}
"""
def removeInvalidParentheses(s):
    result = []

    """
    @param {str} subStr
    @param {int} last_i
    @param {int} last_j
    @param {str[]} parentheses, ['(', ')'] for left to right, [')', '('] for right to left
    @return {void}
    """
    def removeHelper(subStr, last_i, last_j, parentheses):
        count = 0
        for i in range(last_i, len(subStr)):
            if subStr[i] == parentheses[0]:
                count += 1
            if subStr[i] == parentheses[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if subStr[j] == parentheses[1] and (j == last_j or subStr[j-1] != parentheses[1]):
                    removeHelper(subStr[:j]+subStr[j+1:], i, j, parentheses)
            return

        # Termination condition
        if parentheses[0] == '(' and count == 0:
            result.append(subStr)
            return

        reversedStr = subStr[::-1]
        if parentheses[0] == '(':
            removeHelper(reversedStr, 0, 0, [')', '(']);
        else:
            # Termination condition
            result.append(reversedStr)

    removeHelper(s, 0, 0, ['(', ')'])

    return result
