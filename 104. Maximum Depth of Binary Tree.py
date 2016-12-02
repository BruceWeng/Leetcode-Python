# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: Recursion
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

# Solution 2: BFS
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0

        height = 0
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            if size == 0:
                return height
            else:
                height += 1

            for i in range(size):
                head = queue.popleft()
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)

        return height
