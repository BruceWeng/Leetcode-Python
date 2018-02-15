"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
"""
Algorithm: Binary Search
1. if nums[mid] > nums[start]: start = mid
2. if nums[mid] < nums[start]: end = mid
3. after binary search:
    return min(start, end)
"""
"""
@param {int[]} nums
@return {int}
"""
def findMin(nums):
    if len(nums) == 0:
        return 0

    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        # Use nums[end] rather than nums[start] to compare to cover non-rotate case
        if nums[mid] >= nums[end]:
            start = mid
        else:
            end = mid

    return min(nums[start], nums[end])

if __name__=="__main__":
    print(findMin([4, 5, 6, 7, 0, 1, 2])) # 0
