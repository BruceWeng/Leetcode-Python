"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
"""
Algorithm:
Worst case: every element are the same, T: O(n)
1. if nums[mid] == nums[end]: end -= 1 (save to remove end pointer)
2. if nums[mid] > nums[end]: start = mid
3. if nums[mid] < nums[end]: end = mid
4. After binary search: return min(nums[start], nums[end])
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
        if nums[mid] == nums[end]:
            end -= 1
        # Use nums[end] rather than nums[start] to compare to cover non-rotate case
        elif nums[mid] >= nums[end]:
            start = mid
        else:
            end = mid

    return min(nums[start], nums[end])

if __name__=="__main__":
    print(findMin([4, 5, 6, 7, 0, 0, 1, 1, 1, 2])) # 0
