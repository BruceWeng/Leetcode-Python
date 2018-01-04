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
