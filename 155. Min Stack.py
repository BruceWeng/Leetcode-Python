class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minstack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.minstack) == 0 or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        # return the minimum number in stack
        return self.minstack[-1]
