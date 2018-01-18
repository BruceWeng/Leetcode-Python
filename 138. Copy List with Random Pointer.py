"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
"""
@params {RandomListNode} head
@return {RandomListNode}
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""
Deep copy must links to its own node. Declare a hash table map copy and origin linked list.

Lesson learned: Since node.next is possibly be None, use dict.get(key) to return None
if key is None.
"""
def copyRandomList(head):
    table = {}
    node = head
    while node:
        table[node] = RandomListNode(node.label)
        node = node.next
    node = head
    while node:
        table[node].next = table.get(node.next)
        table[node].random = table.get(node.random)
        node = node.next
    return table.get(head)
