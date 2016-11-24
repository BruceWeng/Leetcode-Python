'''
Solution: answer equals to sum of all local maximum - min elements
ex:
input: [1, 2, 3, 4, 5]
output:
(5 - 1) + (4 - 1) + (3 - 1) + (2 - 1)
= sum(nums) - min(nums) - min(nums) * (len(nums) - 1)
= sum(nums) - min(nums) * len(nums)
'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0 or nums == None):
            return 0

        return sum(nums) - min(nums) * len(nums)
