"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
"""
Algorithm: level order traversal
T: O(n)
S: O(1)
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
def connect(root):
    if root == None:
        return

    tail = dummy = TreeLinkNode(0)
    while root:
        tail.next = root.left
        if tail.next:
            tail = tail.next
        tail.next = root.right
        if tail.next:
            tail = tail.next
        root = root.next
        if not root:
            tail = dummy
            root = dummy.next
