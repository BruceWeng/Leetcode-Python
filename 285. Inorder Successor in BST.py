"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
(Successor is a node whose value is greater than target val and the value is minimum)
(Predecessor is a node whose value is smaller than target and the value is maximum)
"""
"""
Algorithm:
1. Recursively call inorderSuccessor(root.right, p) until find the first node that node.val > p.val
2. Recursively call inorderSuccessor(root.left, p) until left == None, return root else return left
    (minimum)
The time complexity should be O(h) where h is the depth of the result node.
S: O(h)
"""
"""
@param {TreeNode} root
@param {TreeNode} p
@return {TreeNode}
"""
def inorderSuccessor(root, p):
    if root == None or p == None:
        return None

    if root.val <= p.val:
        return inorderSuccessor(root.right, p)
    else:
        left = inorderSuccessor(root.left, p)
    if left == None:
        return root
    else:
        return left

"""
Algorithm: Iterative solution
The time complexity should be O(h) where h is the depth of the result node.
S: O(1)
"""
def inorderSuccessor(root, p):
    if root == None or p == None:
        return None

    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ
"""
Inorder Predecessor in BST
"""
def inorderPredecessor(root, p):
    if root == None or p == None:
        return None

    if root.val >= p.val:
        return inorderPredecessor(root.left, p)
    else:
        right = inorderPredecessor(root.right, p)
    if right == None:
        return root
    else:
        return right
