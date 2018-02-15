"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""
"""
Algorithm:
This question will not be ask to implement in real interview.
Only need to identify the worst case is all the elements are the same, ex [1, 1, 1, ...]
Worst case: T: O(n). Not necessary to use binary search.
Use a for loop is also O(n).
The point of this question is if we can think of worst case, not binary search.
"""
"""
@param {int[]} nums
@param {int} target
@return {bool}
"""
def search(nums, target):
    if len(nums) == 0:
        return False
    for num in nums:
        if num == target:
            return True
    return False
