"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        length = len(nums)

        if length >= 3:
            nums[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])

        return max(nums[length - 1], nums[length - 2])
