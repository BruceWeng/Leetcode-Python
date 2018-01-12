"""
Given an array S of n integers, are there elements a, b, c in S such that a + b
 + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
"""

"""
@param {int[]} nums
@return {int[][]}
"""
def threeSum(nums):
    nums.sort()
    result = []
    # iterate the i index from 0 and moving left ptr from i + 1, right ptr from
    # len(nums) - 1
    # skip duplicate: nums[i] == nums[i-1]-> continue
    # compare sum of numbers in the three ptrs:
    # 1. sum > 0: right -= 1
    # 2. sum < 0: left += 1
    # 3. sum == 0: result.append(nums[i], nums[l], nums[r]), left += 1, right -= 1
    # 3.1. skip duplicate: nums[left] == nums[left-1] -> left += 1
    # 3.2. skip duplicate: nums[right] == nums[right+1] -> right -= 1
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums)-1
        while left < right:
            sumValue = nums[i] + nums[left] + nums[right]
            if sumValue > 0:
                right -= 1
            elif sumValue < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # 3.2
                while left < right < len(nums)-1 and nums[left] == nums[left-1]:
                    left += 1
                while left < right < len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
    return result
