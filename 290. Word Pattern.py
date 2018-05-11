"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase
letters separated by a single space.
"""
"""
Algorithm:
1. Use a cache maintain the pairs of (pattern[i], string[i])
2. iterate the cache, if pattern not in cache and string not in cache.values(),
create pair, if pattern in cache, check if cache[pattern[i]] == string[i]
3. else return false
"""
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
