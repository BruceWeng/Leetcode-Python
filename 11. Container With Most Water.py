"""
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
import unittest
"""
@param {ArrayOfInteger} height
@return {integer} max area containing water
"""
def maxArea(height):
    if height == None or len(height) < 2:
        return None
    maxArea = 0
    result = 0

    return result

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxArea([3, 2, 1, 2, 3, 4, 0, 3]), 4)
    def test2(self):
        self.assertEqual(maxArea([0, 1, 2, 3]), 6)

if __name__=="__main__":
    unittest.main()
