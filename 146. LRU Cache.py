class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Check if key is in map
        if key not in self.map:
            return -1

        # Remove Current Node
        curr = self.map[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        # Move Current Node to the tail
        self.moveToTail(curr)
        return self.map[key].value

    def set(self, key, value):
        # Check if key-value pair is in map
        if self.get(key) != -1:
            self.map[key].value = value
            return

        # Check if map is full
        if len(self.map) == self.capacity:
            del self.map[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

        # Insert New Node to the tail
        newNode = ListNode(key, value)
        self.map[key] = newNode
        self.moveToTail(newNode)

    def moveToTail(self, curr):
        curr.prev = self.tail.prev
        self.tail.prev = curr
        curr.prev.next = curr
        curr.next = self.tail
