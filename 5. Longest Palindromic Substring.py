"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    # Solution1: O(n^3), Brute Force
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        result = ""
        # Two pointers start=0 and end=1
        # for start in range(len(s))
        #   for end in range(1, len(s))
        #       if isPalindrome(s, start, end) and len(s[start:end+1]) > len(result): result = s[start:end+1]
        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        for start in range(len(s)):
            for end in range(len(s)):
                if isPalindrome(s, start, end) and len(s[start:end+1]) > len(result):
                    result = s[start:end+1]

        return result

    # Solution2: O(n^2)
    # Step1: Consider each chars as the middle of the palindrome(start form length 1 and 2)
    # Step2: Expand the start and end and check isPalindrome
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        result = ""

        def newPalindrome(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]

        for i in range(len(s)):
            newPalindrome1 = newPalindrome(s, i, i)
            newPalindrome2 = newPalindrome(s, i, i + 1)
            if len(newPalindrome1) > len(result):
                result = newPalindrome1
            if len(newPalindrome2) > len(result):
                result = newPalindrome2

        return result


test1 = "abagegeg"
test2 = "aaaabbb"
sol = Solution()
print sol.longestPalindrome2(test1)
print sol.longestPalindrome2(test2)
