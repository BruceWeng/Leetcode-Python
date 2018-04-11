"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
"""
@param {TreeNode} root
@param {Float} target
@return {TreeNode}
"""
"""
Algorithm: Recursive
Closest is either the root’s value (a) or the closest in the appropriate subtree (b).
T: O(n)
S: O(n)
"""
def closestValue(root, target):
    if root == None or target == None:
        return None

    a = root.val
    kid = root.left if a > target else root.right
    if not kid:
        return a
    b = closestValue(kid, target)
    return a if abs(a - target) < abs(b - target) else b
"""
Algorithm: Iterative
Closest is either the root’s value (a) or the closest in the appropriate subtree (b).
T: O(n)
S: O(1)
"""
def closestValue(root, target):
    if root == None or target == None:
        return None

    a = root.val
    while root:
        if abs(root.val - target) < abs(a - target):
            a = root.val
        root = root.left if root.val > target else root.right
    return a
