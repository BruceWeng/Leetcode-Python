# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution1: Space: O(n)
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        stack = []
        inOrderNodes = []
        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left

        while stack:
            node = stack.pop()
            inOrderNodes.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        index1 = -1
        index2 = -1
        for i in range(len(inOrderNodes)):
            if inOrderNodes[i] > inOrderNodes[i+1]:
                index1 = i
                break
        for j in range(len(inOrderNodes) - 1, -1, -1):
            if inOrderNodes[j] < inOrderNodes[j-1]:
                index2 = j
                break

        temp = inOrderNodes[index1]
        inOrderNodes[index1] = inOrderNodes[index2]
        inOrderNodes[index2] = temp

        def sortedArrayToBST(nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            if nums == None or len(nums) == 0:
                return None

            def buildTree(nums, start, end):
                if start > end:
                    return None

                mid = start + (end - start) // 2
                curr = TreeNode(nums[mid])
                curr.left = buildTree(nums, start, mid - 1)
                curr.right = buildTree(nums, mid + 1, end)
                return curr

            return buildTree(nums, 0, len(nums) - 1)
        return sortedArrayToBST(inOrderNodes)

#Solution2: SPace: O(1)
import sys
class Solution(object):

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.last = TreeNode(-sys.maxint)

        def traverse(curr):
            if curr == None:
                return

            traverse(curr.left)
            if self.first == None and curr.val < self.last.val:
                self.first = self.last
            if self.first != None and curr.val < self.last.val:
                self.second = curr
            self.last = curr
            traverse(curr.right)

        traverse(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp





    #         10
    #        /  \
    #       5   15
    #      / \  / \
    #     3  8 11 17
    #    /       \
    #   13        2
sol = Solution()
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(8)
root1.left.left.left = TreeNode(13)
root1.right = TreeNode(15)
root1.right.left = TreeNode(11)
root1.right.right = TreeNode(17)
root1.right.left.right = TreeNode(2)

print sol.recoverTree(root1) # 0, 6
