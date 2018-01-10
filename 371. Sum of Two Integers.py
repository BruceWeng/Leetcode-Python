"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Bit manipulation summary: https://leetcode.com/problems/sum-of-two-integers/discuss/84278
Handling Python negative 32bit integer: https://www.hrwhisper.me/leetcode-sum-two-integers/
"""
import unittest
"""
@param {integer} a (xor value when entering recursing)
@param {integer} b ("and + shift" value when entering recursing)
@return {integer}
"""
# Recursively generate xor value and "and + shift" value
# and return and of two values until "and + shift" value becomes zero
def getSum(a, b):
    if a == None or b == None:
        return 0
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF
    # Instantiate scope variable
    result = 0
    # Helper function
    def helper(xor, andShift):
        nonlocal result, mask
        # Base case
        if andShift == 0:
            if xor <= MAX_INT:
                result = xor
            else:
                result = ~(xor & MAX_INT) ^ MAX_INT
            return
        # Recursive case
        helper((xor ^ andShift) & mask, ((xor & andShift) << 1) & mask)
    # Invoke helper function
    helper(a, b)
    # Return result
    return result

    # result = 0
    # xor_digits = a ^ b
    # and_digits = a & b
    # shift_digits = and_digits << 1
    # result = shift_digits & xor_digits


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(getSum(123, 456), 579)
    def test2(self):
        self.assertEqual(getSum(123, -123), 0)
    def test3(self):
        self.assertEqual(getSum(-123, -456), -579)

if __name__=="__main__":
    unittest.main()
