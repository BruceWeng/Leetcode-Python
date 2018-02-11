"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""
"""
Algorithm:
1. Sum: return sum of (1...n) - sum(nums)
2. XOR: XOR is used to find duplicate number:
    a. result = len(nums)
    b. for in range(len(nums)): result ^= i, result ^= nums[i]
    c. The one number shows only once will stay
"""
"""
@param {int[]} nums
@return {int}
"""
def missingNumber(nums):
    total = (len(nums) + 1) * len(nums) // 2
    return total - sum(nums)
