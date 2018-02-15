"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
"""
Algorithm: Binary Search
1. if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: return nums[mid]
2. if nums[mid - 1] < nums[mid] < nums[mid + 1]: start = mid
3. if nums[mid - 1] > nums[mid] > nums[mid + 1]: end = mid
4. else (local minimum): end = mid (choose either way is fine)
5. After binary search: return start if nums[start] > nums[end] else end
"""
"""
@param {int[]} nums
@return {int}
"""
def findPeakElement(nums):
    if nums == None or len(nums) == 0:
        return 0

    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        # No need to check nums[mid] > nums[mid - 1]
        if nums[mid] < nums[mid + 1]:
            start = mid
        # No need to check nums[mid] > nums[mid + 1]
        elif nums[mid - 1] > nums[mid]:
            end = mid
        # The local minimum case that nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]
        else:
            # Either start = mid or end = mid is fine
            end = mid
    return start if nums[start] > nums[end] else end

if __name__=="__main__":
    print(findPeakElement([1, 2, 3, 1])) # 2
