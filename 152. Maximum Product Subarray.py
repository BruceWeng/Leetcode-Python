class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        n = len(nums)
        localMin = localMax = ultiMax = nums[0]
        for i in range(1, len(nums)):
            temp = localMax
            localMax = max(max(localMin * nums[i], temp * nums[i]), nums[i])
            localMin = min(min(localMin * nums[i], temp * nums[i]), nums[i])
            ultiMax = max(localMax, ultiMax)

        return ultiMax

sol = Solution()
test1 = [2, -3, 4, -5]
print sol.maxProduct(test1) # 120
