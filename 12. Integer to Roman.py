"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
import unittest
class Solution:
    """
    @param {integer} num
    @return {string} roman number
    """
    def intToRoman(self, num):
        if num < 1 or num > 3999: return ""
        result = [] # array of Character
        # List roman and numbers including 4, 9, 40, 90...
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        while num > 0:
            while num >= number[i]:
                result.append(roman[i])
                num -= number[i]
            i += 1
        return "".join(result)

class Test(unittest.TestCase):
    def test1(self):
        solution1 = Solution()
        self.assertEqual(solution1.intToRoman(0), "")
    def test2(self):
        solution2 = Solution()
        self.assertEqual(solution2.intToRoman(1234), "MCCXXXIV")

if __name__=="__main__":
    unittest.main()
