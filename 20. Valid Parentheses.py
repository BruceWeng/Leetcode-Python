"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
"""
Algorithm: Stack
1. Declare a stack to store expect close parentheses ex: ")", "]", "}"
2. Iterate s:
    if meet open parentheses ex: "(", "[", "{",
        stack.push(corresponding close parentheses)
    ...
    else if meet close parentheses:
        if s[i] != stack.pop() or len(stack) == 0:
            return False

3. Check pop all close parentheses in stack or not:
    return True if len(stack) == 0 else False

T: O(n)
S: O(n)
"""
"""
@param {str} s
@return {bool}
"""
def isValid(s):
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(")")
        elif s[i] == "[":
            stack.append("]")
        elif s[i] == "{":
            stack.append("}")
        elif len(stack) == 0 or s[i] != stack.pop():
            return False

    return True if len(stack) == 0 else False
