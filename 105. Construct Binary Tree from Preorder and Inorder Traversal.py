"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
"""
@parms {int[]} preorder
@params {int[]} inorder
@return {TreeNode}
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    # The basic idea is here:
    # Say we have 2 arrays, PRE and IN.
    # Preorder traversing implies that PRE[0] is the root node.
    # Then we can find this PRE[0] in IN, say it's IN[5].
    # Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, IN[6] to the end is on the right side.
    # Recursively doing this on subarrays, we can build a tree out of it :)
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    if inorder != None:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root
