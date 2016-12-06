# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True

        stack = []
        curr = root
        result = []
        while curr:
            stack.append(curr)
            curr = curr.left

        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left

        return True if list(sorted(set(result))) == result else False

test1 = TreeNode(2)
test1.left = TreeNode(1)
test1.right = TreeNode(3)
sol = Solution()
print sol.isValidBST(test1)
