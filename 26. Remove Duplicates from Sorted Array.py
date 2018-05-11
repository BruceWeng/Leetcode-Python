"""
Given a sorted array, remove the duplicates in-place such that each element appear
only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.

Example: Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
"""
@param {int[]} nums
@return {int} new length
T: O(n), S: O(1)
"""
"""
1. Find the first element that different from previous one and mark as insertion index
2. Once find the next different element, replace the new element to insertion index,
and increment insertion index
[1, 2, 2, 3, 3, 3, 4, 5]
    ^
    insertion index
[1, 2, 2, 3, 3, 3, 4, 5]
       ^
       insertion index
[1, 2, 3, 3, 3, 3, 4, 5]
          ^
          insertion index
"""
def removeDuplicates(nums):
    if nums == None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    insertIndex = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        else:
            nums[insertIndex] = nums[i]
            insertIndex += 1
    return insertIndex
