"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
"""
@param {ListNode} head
@return {bool}
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head == None: return False

    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
