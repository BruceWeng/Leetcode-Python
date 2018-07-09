"""
Given a string containing just the characters '(' and ')', find the length of the
longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
"""
Algorithm1: Stack
1. Scan the string from beginning to end.

2. If current character is '(',
push its index to the stack. If current character is ')' and the
character at the index of the top of stack is '(', we just find a
matching pair so pop from the stack. Otherwise, we push the index of
')' to the stack.

3. After the scan is done, the stack will only
contain the indices of characters which cannot be matched. Then
let's use the opposite side - substring between adjacent indices
should be valid parentheses.

4. If the stack is empty, the whole input
string is valid. Otherwise, we can scan the stack to get longest
valid substring as described in step 3.

T: O(n)
S: O(n)

Algorithm2: DP
1. Construct a array longest[], for any longest[i], it stores the longest length
of valid parentheses which is end at i.

2.
If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot be a valid one.

Else if s[i] is ')'

     If s[i-1] is '(', longest[i] = longest[i-2] + 2

     Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], longest[5] = longest[4] + 2 + longest[1] = 6.

T: O(n)
S: O(n)
"""
"""
Algorithm1: Stack, More efficient
@param {str} s
@return {int}
"""
def longestValidParentheses(s):
    length = len(s)
    longest = 0
    stack = []

    for i in range(length):
        if s[i] == "(":
            stack.append(i)
        else:
            if len(stack) != 0:
                if s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

    if len(stack) == 0:
        longest = length
    else:
        end = length
        start = 0
        while len(stack) != 0:
            start = stack.pop()
            longest = max(longest, end-start-1)
            end = start

        longest = max(longest, end)

    return longest

"""
Algorithm2: DP
@param {str} s
@return {int}
"""
def longestValidParentheses(s):
    if len(s) <= 1:
        return 0

    currMax = 0
    longest = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i-1] == '(':
                longest[i] = longest[i-2] + 2 if i-2 >= 0 else 2
                currMax = max(longest[i], currMax)
            else: # if s[i-1] == ')', combine the previous length.
                if i - longest[i-1]-1 >= 0 and s[i-longest[i-1]-1] == '(':
                    longest[i] = longest[i-1] + 2
                    if i - longest[i-1] - 2 >= 0:
                        longest[i] += longest[i-longest[i-1]-2]
                    currMax = max(longest[i], currMax)

        # else if s[i] == '(', skip it, because longest[i] must be 0
    return currMax
