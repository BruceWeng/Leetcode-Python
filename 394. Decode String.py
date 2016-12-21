class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Correct Solution:
        if not s:
            return None
        stack = []
        stack.append([[], 1])
        num = []
        for ch in s:
            if ch.isdigit():
                num.append(ch)
            elif ch == '[':
                stack.append([[], int("".join(num))])
                num = []
            elif ch == ']':
                tempStr, tempNum = stack.pop()
                stack[-1][0].extend(tempStr * tempNum)
            else:
                stack[-1][0].append(ch)

        return "".join(stack[0][0])

        #1. Init stackNum[], Init stackStr[tempStr[]]
        #2. Traverse s, if type(s[i]) == 'int'): stackNum.append(s[i])
        #               elif type(s[i] == 'str'): tempStr.append(s[i])
        #               elif s[i] == '[': stackStr.pop()
        #               elif s[i] == ']': stackNum.pop(), result.append("".join(num * tempStr))

        # if not s:
        #     return None
        # result = []
        # stackNum = []
        # stackStr = []
        #
        # for i in range(len(s)):
        #     if type(s[i]) == 'int':
        #         stackNum.append(s[i])
        #     elif s[i] == '[':
        #         stackNum.append([])
        #     elif type(s[i] == 'str'):
        #         tempStr = stackStr.pop()
        #         tempStr.append(s[i])
        #         stackStr.append(tempStr)
        #     elif s[i] == ']':
        #         num = stackNum.pop()
        #         tempStr = stackNum.pop()
        #         result.append("".join(num * tempStr))
        #
        # return result

test1 = "3[a]2[bc]"
test2 = "3[a2[c]]"
sol = Solution()
print sol.decodeString(test1)
print sol.decodeString(test2)
