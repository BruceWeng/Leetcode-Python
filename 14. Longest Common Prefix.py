"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
"""
1. Find the shortest string
2. Find substring result of the shortest string to see if there is match between
result and other strings in the array, if yes, continue add next character,
3. else return prefix[0:i]
4. else: return result

T: O(n^2)
S: O(1)
"""
import unittest
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :param  strs: List[String]
        :return result: String
        """
        if strs == None or len(strs) == 0:
            return ""

        result = ""
        prefix = min(strs, key=len)
        for i, pre in enumerate(prefix):
            result = prefix[0:i+1]
            for j, value in enumerate(strs):
                if result == value[0:i+1]:
                    continue
                else:
                    return prefix[0:i]

        return result

class Test(unittest.TestCase):
    def test1(self):
        solution = Solution()
        test1 = ["abc", "c", "bc", "abd"]
        self.assertEqual(solution.longestCommonPrefix(test1), "")

    def test2(self):
        solution = Solution()
        test2 = ["abc", "abd", "abe"]
        self.assertEqual(solution.longestCommonPrefix(test2), "ab")

if __name__=="__main__":
    unittest.main()
