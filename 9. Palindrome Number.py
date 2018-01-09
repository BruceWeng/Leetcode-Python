"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
import unittest
class Solution:
    """
    @param {integer} x
    @return {boolean}
    """
    def isPalindrome(self, x):
        if x < 0: return False
        result = 0
        # Compare half of x with result
        while result < x:
            result = 10 * result + x % 10
            x = x // 10
            if result == 0: return False # Handle the case that last digit is 0, which x must not a palindrome
        return result == x or result // 10 == x

class Test(unittest.TestCase):
    def test1(self):
        solution1 = Solution()
        self.assertEqual(solution1.isPalindrome(123), False)
    def test2(self):
        solution2 = Solution()
        self.assertEqual(solution2.isPalindrome(-123), False)
    def test3(self):
        solution3 = Solution()
        self.assertEqual(solution3.isPalindrome(12321), True)
    def test4(self):
        solution4 = Solution()
        self.assertEqual(solution4.isPalindrome(12210), False)
if __name__=="__main__":
    unittest.main()
