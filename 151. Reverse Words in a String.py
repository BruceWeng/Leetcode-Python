"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Notes:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) == 0:
            return ""

        toArray = s.split(" ")
        length = len(toArray)
        start = 0
        end = length - 1
        while start < end:
            temp = toArray[start]
            toArray[start] = toArray[end]
            toArray[end] = temp

            start += 1
            end -= 1

        result = " ".join(toArray)
        return result

test1 = "ya the sky is blue"
solution = Solution()
print solution.reverseWords(test1) #"blue is sky the"
