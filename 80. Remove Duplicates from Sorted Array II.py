"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being
1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""
"""
Algorithm:
1. Use a pointer to identify the element to be replaced
2. If n == nums[i]: continue
3. Else: num[i] = n, i += 1
4. return i
variables:
i: pointer that element to be replaced
"""
"""
@param {[]} nums
@return {int}
"""
def removeDuplicates(nums):
    if nums == None or len(nums) == 0:
        return 0

    i = 0
    for n in nums:
        if i < 2 or n > nums[i - 2]:
            nums[i] = n
            i += 1

    return i
