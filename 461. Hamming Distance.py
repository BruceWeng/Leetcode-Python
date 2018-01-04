import unittest
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        for _ in range(32):
            count += xor & 1
            xor = xor >> 1

        return count

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().hammingDistance(1, 4), 2)

    def test2(self):
        self.assertEqual(Solution().hammingDistance(0, 0), 0)

if __name__=="__main__":
    unittest.main()
