# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def dfs(root):
            if root == None:
                return -1

            height = max(dfs(root.left), dfs(root.right)) + 1

            if height == len(result):
                result.append([])
            result[height].append(root.val)

            return height

        dfs(root)
        return result
