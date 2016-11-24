'''
Solution: Answer equals to all the elements substract the median
1. sort array
2. use two pointers substract nums[end] and nums[start]
'''
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0 or nums == None):
            return 0

        count = 0
        start = 0
        end = len(nums) - 1
        nums = sorted(nums)

        while start < end:
            count += nums[end] - nums[start]
            end -= 1
            start += 1

        return count

test1 = [2, 1]
solution = Solution()
print solution.minMoves2(test1)
