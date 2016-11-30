from collections import deque
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        self.queue.popleft()

    # @return an integer
    def top(self):
        top = None
        for x in range(len(self.queue)):
            top = self.queue.popleft()
            self.queue.append(top)
        return top

    # @return an boolean
    def empty(self):
        return len(self.queue) == 0
