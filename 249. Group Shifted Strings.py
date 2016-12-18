# T: O(nk), k = max string length
# S: O(nk)
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if len(strings) == 0 or not strings:
            return []

        cache = {}
        result = []
        def transform(strs):
            charList = list(strs)
            base = ord(charList[0])
            for i in range(len(charList)):
                newChar = ord(charList[i]) - base
                if newChar < 0:
                    newChar = newChar + 26
                charList[i] = chr(newChar)
            return  "".join(charList)

        for strs in strings:
            tStrs = transform(strs)
            if tStrs not in cache:
                cache[tStrs] = [strs]
            else:
                cache[tStrs].append(strs)

        for group in cache.values():
            result.append(group)

        return result

test1 = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
sol = Solution()
print sol.groupStrings(test1)
