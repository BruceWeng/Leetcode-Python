"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
"""
Algorithm1: Sorting
1. Sort the array, traverse the sorted array, if the current element is the same
as previous element, return false
2. return true

T: O(nlogn)
S: O(1)

Algorithm2: HashSet
1. Declare a set(int), if element in set, return false, else add element in set
2. return true

T: O(n)
S: O(n)
"""
"""
@param {int[]} nums
@return {bool}
"""
""""Algo1"""
def containsDuplicate(nums):
    if nums == None or len(nums) == 0:
        return False

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True

    return False

"""Algo2"""
def containsDuplicate(nums):
    if nums == None or len(nums) == 0:
        return False

    hashSet = set()
    for i in range(len(nums)):
        if nums[i] in hashSet:
            return True

        else:
            hashSet.add(nums[i])

    return False
