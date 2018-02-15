"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
"""
Algorithm: Binary Search
1. Find left bound
    a. if nums[mid] >= target:
        end = mid
    b. else:
        start = mid
    c. after binary search:
        if nums[start] == target:
            result.append(start)
        else:
            result.append(end)
2. Find right bound
    a. if nums[mid] <= target:
        start = mid
    b. else:
        end = mid
    c. after binary search:
        if nums[end] == target:
            result.append(end)
        else:
            result.append(start)
3. Target not found: if nums[start] != target and nums[end] != target: return [-1, -1]
"""
"""
@param {int[]} nums
@param {int} target
@return {int[]}
"""
def searchRange(nums, target):
    if nums == None or len(nums) == 0 or target == None:
        return [-1, -1]

    result = []
    # Find left bound
    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] >= target:
            end = mid
        else:
            start = mid

    # target not match
    if nums[start] != target and nums[end] != target:
        return [-1, -1]

    if nums[start] == target:
        result.append(start)
    else:
        result.append(end)
    # Find right bound
    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] <= target:
            start = mid
        else:
            end = mid

    if nums[end] == target:
        result.append(end)
    else:
        result.append(start)

    return result

if __name__=="__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8)) # [3, 4]
    print(searchRange([1], 1)) # [0, 0]
