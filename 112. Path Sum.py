# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        stack = []
        stack.append({"node": root, "sum": root.val})
        while stack:
            top = stack.pop()
            right = top["node"].right
            left = top["node"].left
            if right == None and left == None and top["sum"] == sum:
                return True
            if right:
                stack.append({"node": right, "sum": top["sum"] + right.val})
            if left:
                stack.append({"node": left, "sum": top["sum"] + left.val})

        return False

            
