"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). You might need
to change the root of the tree, so the result should return the new root of the
trimmed binary search tree.

Example1:       Example2:
Input:          Input:
    1               3
   / \             / \
  0   2           0   4
                   \
  L = 1             2
  R = 2            /
                  1
Output:
    1             L = 1
      \           R = 3
       2
                    Output:
                      3
                     /
                   2
                  /
                 1
"""
"""
@params {TreeNode} root
@params {int} L
@parmas {int} R
@return {TreeNode}
"""
def trimBST(root, L, R):
    if root == None:
        return None

    # new root in left subtree
    if root.val > R:
        return trimBST(root.left, L, R)
    # new root inright subtree
    if root.val < L:
        return trimBST(root.right, L, R)

    root.left = trimBST(root.left, L, R)
    root.right = trimBST(root.right, L, R)

    return root
