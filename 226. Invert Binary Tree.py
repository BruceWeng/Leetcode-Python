"""
Invert a binary tree

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
"""
@params {TreeNode} root
@return {TreeNode}
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Solution1: Recursion S: O(n)
"""
def invertTree(root):
    if root == None:
        return None

    """
    @params {TreeNode} root
    @params {TreeNode} node
    @return {void}
    """
    def invert(root, node):
        node.val = root.val
        if root.left:
            right = TreeNode(None)
            node.right = right
            invert(root.left, node.right)
        if root.right:
            left = TreeNode(None)
            node.left = left
            invert(root.right, node.left)

    result = TreeNode(None)
    invert(root, result)

    return result


"""
Solution2: Recursion S: O(1)
"""
def invertTree(root):
    if root == None:
        return None

    left = root.left
    right = root.right
    root.left = invertTree(right)
    root.right = invertTree(left)

    return root

"""
Solution3: BFS
"""
from collections import deque
def invertTree(root):
    if root == None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        left = node.left
        node.left = node.right
        node.right = left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root
