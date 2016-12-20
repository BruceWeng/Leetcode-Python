class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) == 0:
            return True

        result = []
        for char in s:
            if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                result.append(char.lower())

        start = 0
        end = len(result) - 1
        while start <= end:
            if result[start] != result[end]:
                return False
            start += 1
            end -= 1

        return True


test1 = "A man, a plan, a canal: Panama"
test2 = "0p"
sol = Solution()
print sol.isPalindrome(test2)
