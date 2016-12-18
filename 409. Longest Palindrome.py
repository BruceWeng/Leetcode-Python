class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step1: init cache for counting number of chars
        # Step2: Iterate the cache, if plusOne == 0 and cache[i] % 2 == 1: plusOne += 1
        # Step3: result += cache[i] - 1 for every elements in cache
        if not s:
            return 0

        cache = {}
        plusOne = 0
        result = 0
        for key in s:
            if key not in cache:
                cache[key] = 1
            else:
                cache[key] += 1

        for value in cache.values():
            if plusOne == 0 and value % 2 == 1:
                plusOne += 1
            if value % 2 == 1:
                result += value - 1
            elif value % 2 == 0:
                result += value

        return result + plusOne

    def longestPalindrome2(self, s):
        if not s:
            return 0

        cache = set()
        count = 0
        for key in s:
            if key not in cache:
                cache.add(key)
            else:
                cache.remove(key)
                count += 1

        if len(cache) == 0:
            return count * 2
        else:
            return count * 2 + 1
test1 = "abccccdd"
sol = Solution()
print sol.longestPalindrome2(test1) #7
