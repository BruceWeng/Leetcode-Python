"""
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only hold integers
within the 32-bit signed integer range. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""
import unittest
import math
class Solution:
    """
    @param {integer} x 32-bit signed integer
    @return {integer} reversed integer
    """
    def reverse(self, x):
        if x == None:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x *= -1 # Remember only use positive integer
        result = 0
        # let temp = the result of x recursively mod 10 until to the last digit
        # result = result * 10 + temp
        temp = 0
        while x != 0:
            temp = x % 10
            x = x // 10 # Floor division
            result = 10 * result + temp

        result *= sign
        if result > math.pow(2, 31) or result < -math.pow(2, 31) - 1:
            return 0
        return result

class Test(unittest.TestCase):
    def test1(self):
        solution1 = Solution()
        self.assertEqual(solution1.reverse(123), 321)

    def test2(self):
        solution2 = Solution()
        self.assertEqual(solution2.reverse(-456), -654)

    def test3(self):
        solution3 = Solution()
        self.assertEqual(solution3.reverse(math.pow(2, 31)), 0)
if __name__=="__main__":
    unittest.main()
