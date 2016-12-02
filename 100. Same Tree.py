# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        stackP = []
        stackQ = []
        stackP.append(p)
        stackQ.append(q)

        while stackP and stackQ:
            topP = stackP.pop()
            topQ = stackQ.pop()
            if topP == None and topQ == None:
                continue

            if topP == None or topQ == None:
                return False

            if topP.val != topQ.val:
                return False

            stackP.append(topP.right)
            stackQ.append(topQ.right)

            stackP.append(topP.left)
            stackQ.append(topQ.left)

        if len(stackP) != 0 or len(stackQ) != 0:
            return False

        return True
