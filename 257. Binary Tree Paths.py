# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return []

        result = []
        path = str(root.val)

        def traverse(curr, path, result):
            if curr.left == None and curr.right == None:
                result.append(path)
                return
            # Never declare new variables to pass to recursion function, they will share same reference
            if curr.left:
                # path += '->' + str(curr.left.val)
                traverse(curr.left, path + '->' + str(curr.left.val), result)

            if curr.right:
                # path += '->' + str(curr.right.val)
                traverse(curr.right, path + '->' + str(curr.right.val), result)

        traverse(root, path, result)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.binaryTreePaths(root)) # ["1->2->4", "1->2->5", "1->3"]
