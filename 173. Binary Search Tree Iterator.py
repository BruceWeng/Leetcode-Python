class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.curr = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr != None or self.stack

    def next(self):
        """
        :rtype: int
        """
        while self.curr != None:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        next = self.curr
        self.curr = self.curr.right
        return next.val
