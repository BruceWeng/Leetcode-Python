"""
Given a binary search tree, write a function kthSmallest to find the kth smallest
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find
the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
"""
Algorithm: inorder
"""
"""
@param {TreeNode} root
@param {int} k
@return {int}
"""
"""
Inorder, Recursive
T: O(k), S: O(1) + O(k)(recursive call)
"""
def kthSmallest(root, k):
    if root == None:
        return -1

    counter = [k]
    result = [0]

    def inorder(node):
        if node == None:
            return

        inorder(node.left)

        counter[0] -= 1
        if counter[0] == 0:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]

"""
Inorder, Iterative
T: O(n), S: O(n)(stack)
"""
def kthSmallest(root, k):
    if root == None:
        return -1

    stack = []
    while root:
        stack.append(root)
        root = root.left

    while k != 0:
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val

        right = node.right
        while right:
            stack.append(right)
            right = right.left
