"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
import unittest
"""
@param {int[]} digits
@return {int[]} array representation of input number plus one
"""
def plusOne(digits):
    if digits == None or len(digits) == 0:
        return None
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    result = [0] * (len(digits) + 1)
    result[0] = 1
    return result

class Test(unittest.TestCase):
    def test1(self):
        self.assertListEqual(plusOne([1, 9, 9]), [2, 0, 0])
    def test2(self):
        self.assertListEqual(plusOne([0]), [1])
    def test3(self):
        self.assertListEqual(plusOne([9, 9]), [1, 0, 0])
    def test4(self):
        self.assertListEqual(plusOne([9, 8]), [9, 9])

if __name__=="__main__":
    unittest.main()
