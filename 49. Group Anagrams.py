"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution(object):
    # Solution:
    # T: if max words length == k, O(klogk * n)
    # S: O(n + k)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs or len(strs) == 0:
            return [[]]

        cache = {} # key: sorted(words), value: list of words
        result = []
        for words in strs:
            sortedWords = "".join(sorted(words))
            if sortedWords not in cache:
                cache[sortedWords] = [words]
            else:
                cache[sortedWords].append(words)

        for group in cache.values():
            result.append(group)

        return result

if __name__=="__main__":
    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print sol.groupAnagrams(test1)
