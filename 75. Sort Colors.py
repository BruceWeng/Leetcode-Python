"""
Given an array with n objects colored red, white or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array
with total number of 0's, then 1's and followed by 2's.
T: O(n)
S: O(n)

Could you come up with a one-pass algorithm using only constant space?
"""
"""
Algorithm: Swap
1. Declare zero = 0 points to first index, second = len(nums) - 1 points last index
2. Iterate the nums when i <= second:
    2.a whenever find nums[i] == 2 and i < second, swap(nums[i], nums[second]), second -= 1
    2.b whenever find nums[i] == 0 and i > zero, swap(nums[i], nums[zero]), zero += 1

T: O(n)
S: O(1)
"""
def sortColors(nums):
    zero = 0
    second = len(nums) - 1
    for i in range(0, second + 1):
        while nums[i] == 2 and i < second:
            temp = nums[i]
            nums[i] = nums[second]
            nums[second] = temp
            second -= 1

        while nums[i] == 0 and i > zero:
            temp = nums[i]
            nums[i] = nums[zero]
            nums[zero] = temp
            zero += 1
