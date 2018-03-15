"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
"""
@param {TreeNode} root
@return {int}
"""
import sys
def maxPathSum(root):
    if root == None:
        return 0
    # max value
    result = [- sys.maxsize - 1]

    def postorder(root):
        if root == None:
            return 0
        # Exclude negative value
        left = max(0, postorder(root.left))
        right = max(0, postorder(root.right))
        # Update max value to result
        result[0] = max(result[0], left + right + root.val)
        # Each node maintain its max path sum
        return max(left, right) + root.val

    postorder(root)
    return result[0]
