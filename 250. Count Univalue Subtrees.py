"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
"""
"""
Algorithm: Postorder
1. Declare result to update count of uni-value subtrees
2. Define postorder function bool checkUniValue(root) to do the following check
    2.1. If node == None: return True
    2.2. Find left node to check whether it is valid uni-value subtree
    2.3. Find right node to check wether it is valid uni-value subtree
    2.4. If left and right are True(Either both None or both valid),
            return False if node.val != node.left.val
            return False if node.val != node.right.val
            Otherwise, increment result, and return True if both children are valid.
3. Call checkUniValue(root)
4. Return result
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""
@param {TreeNode} root
@return {int}
"""
def countUnivalSubtrees(root):
    if root == None:
        return 0

    result = [0]

    """
    Use side effect to update result
    @param {TreeNode} node
    @return {boolean}
    """
    def checkUniValue(node):
        if node == None:
            return True

        left = checkUniValue(node.left)
        right = checkUniValue(node.right)

        if left and right:
            if node.left != None and node.left.val != node.val:
                return False

            if node.right != None and node.right.val != node.val:
                return False

            # Both children are identical to node or both children are None
            result[0] += 1
            return True

        return False # Only one child is None
    checkUniValue(root)
    return result[0]
