# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root, maxDepth):
            if root == None:
                return 0
            return max(traverse(root.left, maxDepth), traverse(root.right, maxDepth)) + 1

        return traverse(root, 0)
