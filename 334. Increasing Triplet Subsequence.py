"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
"""
Algorithm:
1. first = maxint, second = MaxInt
2. replace first and second with smallest first two increasing numbers
3. if nums[i] > second, return true
"""
"""
@param {int[]} nums
@return {boolean}
"""
import sys
def increasingTriplet(nums):
    if nums == None or len(nums) == 0:
        return False

    first = sys.maxsize
    second = sys.maxsize
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False

if __name__=="__main__":
    print(increasingTriplet([1, 2, 3, 4, 5]))
