"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""
"""
Algorithm:
The idea is to compare the predecessors and successors of the closest node to the target,
we can use two stacks to track the predecessors and successors, then like what we do in merge sort,
we compare and pick the closest one to the target and put it to the result list.

As we know, inorder traversal gives us sorted predecessors, whereas reverse-inorder traversal
gives us sorted successors.
T: O(log(n)) + O(k), balanced tree, height = log(n)
S: O(k)
"""
"""
@param {TreeNode} root
@param {Double} target
@param {Integer} k
@return {int[]}
"""
def closestKValues(root, target, k):
    if root == None or target == None or k == None or k < 0:
        return []

    result = []
    predecessors = [] # stack1
    successors = [] # stack2
    """
    @param {TreeNode} root
    @param {Double} target
    @param {Boolean} reverse
    @param {[]} stack
    @return {void}
    """
    def inorder(root, target, reverse, stack):
        if root == None: return

        inorder(root.right if reverse else root.left, target, reverse, stack)

        # Early terminate, no need to traverse the whole tree
        if reverse and root.val <= target or not reverse and root.val > target: return

        stack.append(root.val)

        inorder(root.left if reverse else root.right, target, reverse, stack)

    inorder(root, target, False, predecessors)
    inorder(root, target, True, successors)

    while k > 0:
        if not predecessors:
            result.append(successors.pop())
        elif not successors:
            result.append(predecessors.pop())
        elif abs(predecessors[-1] - target) < abs(successors[-1] - target):
            result.append(predecessors.pop())
        else:
            result.append(successors.pop())
        k -= 1
    return result
