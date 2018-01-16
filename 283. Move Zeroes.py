"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
"""
@param {int[]} nums
@return {void}
"""
def moveZeros(nums):
    if nums == None or len(nums) == 0:
        return
    # Find the insert position to insert non zero numbers and insert zero from
    # the last insert position to the end of list
    insertPos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insertPos] = nums[i]
            insertPos += 1
    for i in range(insertPos, len(nums)):
        nums[i] = 0
