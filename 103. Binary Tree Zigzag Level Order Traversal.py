# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        queue = collections.deque()
        queue.append(root)
        result = []
        temp = []
        flag = True
        while queue:
            if flag:
                for i in range(len(queue)):
                    temp.append(queue[i].val)
                flag = False
            else:
                for i in range(len(queue) - 1, -1, -1):
                    temp.append(queue[i].val)
                flag = True

            result.append(temp)
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return result
                    
