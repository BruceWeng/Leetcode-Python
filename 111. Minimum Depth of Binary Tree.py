# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1:
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        def traverse(root):
            if root == None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)

            if root.left and root.right:
                return min(left, right) + 1
            return max(left, right) + 1

        return traverse(root)

# Solution 2: BFS
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        queue = deque()
        queue.append({'node': root, 'depth': 1})

        while queue:
            size = len(queue)
            for i in range(size):
                head = queue.popleft()
                node = head['node']
                depth = head['depth']
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    queue.append({'node': node.left, 'depth': depth + 1})
                if node.right:
                    queue.append({'node': node.right, 'depth': depth + 1})
