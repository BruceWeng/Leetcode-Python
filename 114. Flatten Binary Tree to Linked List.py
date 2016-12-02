# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        stack = []
        head = root
        prev = TreeNode(None)
        stack.append(head)
        while stack:
            top = stack.pop()
            prev.left = None
            prev.right = top
            prev = top
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        prev.left = None
        prev.right = None
