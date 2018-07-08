"""
Given an unsorted array nums, reorder it in-place such that
nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""
"""
Algorithm: Toggle
1. Declare a toggle = 1, toggle *= -1 after each iteration
2. for i in range(1, len(nums)):
    if (nums[i] - nums[i-1]) * toggle < 0: swap(nums[i], nums[i-1])

    toggle *= -1

T: O(n)
S: O(1)
"""
def wiggleSort(nums):
    toggle = 1
    for i in range(1, len(nums)):
        if (nums[i] - nums[i-1]) * toggle < 0:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp

        toggle *= -1
