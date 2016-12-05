# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#Solution1: Space: O(n)
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return

        queue = deque()
        queue.append(root)
        while queue:

            head = queue.popleft()

            if head.left == None or head.right == None:
                continue

            head.left.next = head.right

            if head.next:
                head.right.next = head.next.left

            queue.append(head.left)
            queue.append(head.right)


        return

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#Solution2: Space: O(1)
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return

        nextPtr = root
        curr = root
        atLeft = True
        while nextPtr:
            if curr.left == None or curr.right == None:
                break

            if atLeft:
                atLeft = False
                nextPtr = curr.left

            curr.left.next = curr.right

            if curr.next != None:
                curr.right.next = curr.next.left
                curr = curr.next

            else:
                curr = nextPtr
                atLeft = True

        return
