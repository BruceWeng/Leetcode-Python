class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
            return False

        cache = {}
        for i in range(len(pattern)):
            P = pattern[i]
            S = str[i]
            if P not in cache:
                if S not in cache.values():
                    cache[P] = S
                else:
                    return False
            else:
                if cache[P] == S:
                    continue
                else:
                    return False

        return True

pattern1 = "abba"
str1 = "dog cat cat dog"
sol = Solution()
print sol.wordPattern(pattern1, str1)
