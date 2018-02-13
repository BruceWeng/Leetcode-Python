"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
S: O(1)
"""
"""
Algorithm:

start point         meet point
    <---A---> <---B--->
    ---------+---------+ <--slow, fast
    ^        |         |
    |        |         |
  slow2      |         |
             +---------+
                  X=A
A+B+X+B = 2A+2B
X=A

1. Let slow pointer = head, fast pointer = head
2. slow moves 1 step, fast moves steps each time
3. while slow == fast, let slow2 start from head
4. while slow2 != slow: slow moves 1 step, fast moves 1 step
5. if exit while loop, return slow2
6. return None if no cast that slow == fast
"""
"""
@param {ListNode} head
@return {ListNode}
"""
def detectCycle(head):
    if head == None: return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow2 = head

            while slow2 != slow:
                slow2 = slow2.next
                slow = slow.next

            return slow2

    return None
