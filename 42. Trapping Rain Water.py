"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
# Solution 1: Two Pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2 or height == None:
            return 0
        #find largest bar
        maxBarIdx = 0
        maxBar = height[0]
        for i in range(1, len(height)):
            if height[i] > maxBar:
                maxBarIdx = i
                maxBar = height[i]

        #find local highest left and local highest right
        left = 0
        right = len(height) - 1
        for i in range(maxBarIdx):
            if height[i] <= height[i + 1]:
                left += 1
            else:
                break

        for i in range(len(height) - 1, maxBarIdx, -1):
            if height[i] <= height[i - 1]:
                right -= 1
            else:
                break

        #calculate water from left to maxBar and from right to maxBar
        water = 0
        for i in range(left + 1, maxBarIdx):
            if height[i] < height[left]:
                water += height[left] - height[i]
            else:
                left = i

        for i in range(right - 1, maxBarIdx, -1):
            if height[i] < height[right]:
                water += height[right] - height[i]
            else:
                right = i

        return water

sol = Solution()
test1 = [0,1,0,2,1,0,1,3,2,1,2,1]
test2 = [2, 0, 2] #2
print sol.trap(test2) #6
