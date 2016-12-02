class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# BFS
from collections import deque
def bfsTree(root):
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        head = queue.popleft()
        result.append(head.val)
        """
        Do Something Here
        """
        if head.left:
            queue.append(head.left)
        if head.right:
            queue.append(head.right)
    return result

#DFS
def dfsTree(root):
    result = []
    stack = []
    stack.append(root)

    while stack:
        top = stack.pop()
        result.append(top.val)
        """
        Do Something Here
        """
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
    return result

"""
        1
       / \
      2   3
     / \ / \
    4  5 6  7
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# print bfsTree(root) #1 2 3 4 5 6 7
# print dfsTree(root) #1 2 4 5 3 6 7

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.children[val] = None

#BFS
from collections import deque
def bfsGraph(root):
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        head = queue.popleft()
        result.append(head.val)
        """
        Do Something Here
        """
        if head.children:
            for key in head.children:
                if head.children[key] != None:
                    queue.append(head.children[key])
    return result

#DFS
def dfsGraph(root):
    result = []
    stack = []
    stack.append(root)
    while stack:
        top = stack.pop()
        result.append(top.val)
        """
        Do Something Here
        """
        if top.children:
            for key in top.children:
                if top.children[key] != None:
                    stack.append(top.children[key])
    return result
"""
            1
          / | \
         2  3  4
       / | \
      5  6  7
             \
              8
             / \
            10  9
"""
root2 = GraphNode(1)
root2.children[2] = GraphNode(2)
root2.children[3] = GraphNode(3)
root2.children[4] = GraphNode(4)
root2.children[2].children[5] = GraphNode(5)
root2.children[2].children[6] = GraphNode(6)
root2.children[2].children[7] = GraphNode(7)
root2.children[2].children[7].children[8] = GraphNode(8)
root2.children[2].children[7].children[8].children[10] = GraphNode(10)
root2.children[2].children[7].children[8].children[9] = GraphNode(9)

# print root2.children[2].val
# print bfsGraph(root2) # 1 2 3 4 5 6 7
print dfsGraph(root2) #1 2 5 6 7 3 4

# Graph with circle(multiple parents)
#BFS
from collections import deque
def bfsGraph(root):
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        head = queue.popleft()
        result.append(head.val)
        """
        Do Something Here
        """
        if head.children:
            for child in head.children:
                queue.append(child)
    return result
