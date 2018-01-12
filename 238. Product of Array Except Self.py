"""
Given an array of n integers where n > 1, nums, return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does
not count as extra space for the purpose of space complexity analysis.)
"""
"""
@param {int[]} nums
@return {int[]}
"""
def productExceptSelf(nums):
    """
    nums  [   1,   2,     3,     4]
    result[   1,   1,     1,     1]
    left           1    1*2  1*2*3
    right 2*3*4  3*4      4
    T: O(n), S: O(1) except result[]
    """
    length = len(nums)
    result = [1] * length
    if nums == None or length == 0:
        return []
    right = 1
    for left in range(length):
        if left == 0:
            product = nums[left]
            continue
        result[left] *= product
        product *= nums[left]

    for right in range(length-1, -1, -1):
        if right == length-1:
            product = nums[right]
            continue
        result[right] *= product
        product *= nums[right]

    return result
