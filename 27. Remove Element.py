"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""
"""
Algorithm:
1. Traverse array, when find val, swap current element with last element, array.pop()
2. Check current element again, and repeat 1. current += 1

variables:
current = 0: points to current element in array
T: O(n)
S: O(1)
"""
"""
@param {[]} nums
@param {int} val
@return {int} new length of nums
"""
def removeElement(nums, val):
    if nums == None or len(nums) == 0 or val == None:
        return 0

    current = 0

    while current < len(nums):
        if nums[current] == val:
            temp = nums[-1]
            nums[-1] = nums[current]
            nums[current] = temp
            nums.pop()
        else:
            current += 1

    return len(nums)
