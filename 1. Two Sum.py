class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i in range(len(nums)):
            if target - nums[i] in cache:
                return [cache[target - nums[i]], i]
            cache[nums[i]] = i
        return [-1, -1]

test = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(test.twoSum(nums1, target1))
