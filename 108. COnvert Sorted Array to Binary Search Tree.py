# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None

        def buildTree(nums, start, end):
            if start > end:
                return None

            mid = start + (end - start) // 2
            curr = TreeNode(nums[mid])
            curr.left = buildTree(nums, start, mid - 1)
            curr.right = buildTree(nums, mid + 1, end)
            return curr

        return buildTree(nums, 0, len(nums) - 1)

            
