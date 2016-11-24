class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        localMax = ultiMax = nums[0]
        for i in range(1, len(nums)):
            localMax = max(localMax + nums[i], nums[i])
            ultiMax = max(localMax, ultiMax)

        return ultiMax
        
