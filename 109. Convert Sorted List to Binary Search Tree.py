# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None

        # tail not include
        def buildTree(head, tail):
            if head == tail:
                return
            slow = head
            fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next

            curr = TreeNode(slow.val)
            curr.left = buildTree(head, slow)
            curr.right = buildTree(slow.next, tail)
            return curr

        return buildTree(head, None)
