"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
"""
Algorithm: Binary Search
1. if nums[mid] == target: return mid
2. if nums[mid] < target: start = mid
3. else end = mid
4. after Binary search:
    a. if nums[end] > target, return end
    b. if nums[end] < target, return end + 1
    c. if nums[start] > target, return start
"""
"""
@param {int[]} nums
@param {int} target
@return {int}
"""
def searchInsert(nums, target):
    if nums == None or len(nums) == 0 or target == None:
        return 0

    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid

    if nums[start] >= target:
        return start
    if nums[end] >= target:
        return end
    # All element less than target
    return end + 1


if __name__=="__main__":
    nums = [1, 3, 5, 6]
    target1 = 5
    target2 = 2
    target3 = 7
    target4 = 0
    print(searchInsert(nums, target1)) # 2
    print(searchInsert(nums, target2)) # 1
    print(searchInsert(nums, target3)) # 4
    print(searchInsert(nums, target4)) # 0
