"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
import unittest
"""
@param {integer} n: 32-bit integer
@param {integer} number of 1 bits
"""
def hammingWeight(n):
    # Bit manupulation technique: Remove last significant "1" bit: A = A & (A-1)
    result = 0
    while n != 0:
        n = n & (n-1)
        result += 1
    return result

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(hammingWeight(8), 1)
    def test2(self):
        self.assertEqual(hammingWeight(100), 3)

if __name__=="__main__":
    unittest.main()
