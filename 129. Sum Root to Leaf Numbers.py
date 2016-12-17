# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        sumValue = 0
        stack = [{'node': root, 'number': root.val}]
        while stack:
            curr = stack.pop()
            value = curr['number']
            if curr['node'].left == None and curr['node'].right == None:
                sumValue += curr['number']
            if curr['node'].right:
                stack.append({'node': curr['node'].right, 'number': curr['node'].right.val + 10 * value})
            if curr['node'].left:
                stack.append({'node': curr['node'].left, 'number': curr['node'].left.val + 10 * value})

        return sumValue

# Modified with tuple
class Solution(object):
    def sumNumbers1(self, root):
    if not root:
        return 0
    stack = [(root, root.val)]
    sumValue = 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                sumValue += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return sumValue

test1 = TreeNode(0)
test1.right = TreeNode(1)
sol = Solution()
print sol.sumNumbers(test1)
