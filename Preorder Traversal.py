class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Recursive
def preorder(root):
    result = []
    traverse(root, result)
    return result

def traverse(node, result):
    if node == None:
        return
    result.append(node.key)
    traverse(node.left, result)
    traverse(node.right, result)

test = Node(1)
test.left = Node(2)
test.right = Node(3)
test.left.left = Node(4)
test.left.right = Node(5)
test.right.left = Node(6)
test.right.right = Node(7)

print(preorder(test)) #1, 2, 4, 5, 3, 6, 7
