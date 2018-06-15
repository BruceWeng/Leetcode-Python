"""
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
"""
Algorithm1:
1. Declare pointers left=0 and right=length-1, maxArea=0
2. To find the inteval with max sum, moving the smaller pointer left+=1 or right-=1
3. Update maxArea = max(maxArea, min(height[left], height[right]) * (right-left))
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
    left = 0
    right = len(height) - 1

    while left < right:
        maxArea = max(maxArea, min(height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return maxArea

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxArea([3, 2, 1, 2, 3, 4, 0, 3]), 4)
    def test2(self):
        self.assertEqual(maxArea([0, 1, 2, 3]), 6)

if __name__=="__main__":
    unittest.main()
