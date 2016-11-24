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
