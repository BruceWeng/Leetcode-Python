class Solution(object):
    # Solution1
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        cache = {}
        result = [0] * len(s)
        counter = 0
        for i in range(len(s)):
            if s[i] not in cache:
                cache[s[i]] = counter
                counter += 1
            result[i] = cache[s[i]]

        cache = {}
        counter = 0
        for j in range(len(t)):
            if t[j] not in cache:
                cache[t[j]] = counter
                counter += 1
            if result[j] != cache[t[j]]:
                return False

        return True
        
    # Solution2
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == None or len(s) <= 1:
            return True
        if len(s) != len(t):
            return False

        cache = {}
        for i in range(len(s)):
            S = s[i]
            T = t[i]
            if S not in cache:
                if T not in cache.values():
                    cache[S] = T
                else:
                    return False
            else:
                if cache[S] == T:
                    continue
                else:
                    return False

        return True
