# Solution1
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
# Solution2
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        charList = list(s)
        while start < end:
            temp = charList[start]
            charList[start] = charList[end]
            charList[end] = temp
            start += 1
            end -= 1

        return "".join(charList)
