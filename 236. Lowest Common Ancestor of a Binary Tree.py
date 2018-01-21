"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example
is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to
the LCA definition.
"""
"""
@params {TreeNode} root
@params {TreeNode} p
@params {TreeNode} q
@return {TreeNode}
"""
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    # Terminate condition
    if root == None:
        return None
    if root == p or root == q:
        return root
    # Recursion
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left == None and right == None:
        return None
    if left != None and right != None:
        return root

    return left if left != None else right

if __name__=="__main__":
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node4 = TreeNode(4)

    node3.left = node5
    node3.right = node1

    node5.left = node6
    node5.right = node2

    node2.left = node7
    node2.right = node4

    node1.left = node0
    node1.right = node8

    print(lowestCommonAncestor(node3, node5, node1).value) # 3 
    print(lowestCommonAncestor(node3, node5, node4).value) # 5
