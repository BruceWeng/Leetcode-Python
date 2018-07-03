"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
"""
Algorithm:
1. Iterate nums, and find the last index and add ( curr_num + "->" + nums[i] ) to result
2. Handle duplicate cases
3. Return result
"""
"""
@param {int[]} nums
@return {str[]}
"""
def summaryRanges(nums):
    start_index = 0
    result = []

    for i in range(len(nums)):
        # Find last index for continuous series
        if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
            continue

        if start_index == i:
            result.append(str(nums[start_index]))
        else:
            result.append(str(nums[start_index]) + "->" + str(nums[i]))

        start_index = i + 1

    return result
