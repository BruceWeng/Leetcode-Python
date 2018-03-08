"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
"""
"""
Algorithm: Stack
0. let sign = "+"
1. Initiate a stack the to store numbers, (+: num), (-: -num), (*: stack.pop() * num), (/: stack.pop() / num)
2. Traverse the string
    2.1 if s[i].isdigit(): num = num * 10 + Number(s[i])
    2.2 if !s[i].isdigt() and s[i] != " ":
        2.2.1 Push num into stack base on previous sign
        2.2.2 update sign = s[i], num = 0
3. result = 0, iterate stack and let result += element
4. return result
"""
"""
@param {string} s
@return {int}
"""
def calculate(s):
    if s == None or len(s) == 0:
        return 0

    stack = []
    sign = "+"
    num = 0

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        # When current char in "+, -, *, /", put previous num in stack base on previous sign
        # If current char is the last element, put previous num in stack base on previous sign
        if not char.isdigit() and char != " " or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            if sign == "-":
                stack.append(-num)
            if sign == "*":
                stack.append(stack.pop() * num)
            if sign == "/":
                if stack[-1] < 0:
                    stack.append(- (abs(stack.pop()) // num))
                else:
                    stack.append(stack.pop() // num)
            sign = char
            num = 0

    result = 0
    for element in stack:
        result += element

    return result

if __name__=="__main__":
    print(calculate(" 3+5 / 2 ")) # 5
    print(calculate("14-3/2")) # 13
