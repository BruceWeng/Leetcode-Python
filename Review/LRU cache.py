class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Check if key is in Map
        if key not in self.map:
            return -1
        # Remove current node
        curr = self.map[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        # Move current node to tail.prev
        self.moveToTail(curr)
        # Return current node
        return self.map[key].value

    def set(self, key, value):
        # Check key value pair is existed, if existed, update
        if self.get(key) != -1:
            self.map[key].value = value
            return
        # Check capacity, if it's full, remove head.next node
        if len(self.map) == self.capacity:
            del self.map[self.head.next.key]
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
        # Move new node to tail.prev
        newNode = ListNode(key, value)
        self.map[key] = newNode
        self.moveToTail(newNode)

    def moveToTail(self, curr):
        curr.prev = self.tail.prev
        self.tail.prev.next = curr
        curr.next = self.tail
        self.tail.prev = curr
