"""
Given an array of 2n integers, your task is to group these integers into n
pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
min(ai, bi) for all i from 1 to n as large as possible.
"""
"""
@param {int[]} nums
@return {int}
T: O(nlogn), S: O(1)
"""
def arrayPairSum(nums):
    # In-place sort int[]
    nums.sort()
    result = 0
    for i in range(0, len(nums), 2):
        result += nums[i]
    return result
