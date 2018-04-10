"""
Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure
that a binary tree can be serialized to a string and this string can be deserialized to
the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with
different approaches yourself.



Note: Do not use class member/global/static variables to store states. Your serialize
and deserialize algorithms should be stateless.
"""
"""
Algorithm:
1. serialize: Recursive, Preorder
serialize output example(stirng):
"1,2,3,X,X,4,5"
Spliter: ,
Null placeholder: X

2. deserialize: Recursive, Preorder, Queue
"""
import collections
class Codec:
    def __init__(self):
        self.null = "X"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        self.buildString(root, result)
        return ",".join(result)

    def buildString(self, node, data):
        if node == None:
            data.append(self.null)
        else:
            data.append(str(node.val))
            self.buildString(node.left, data)
            self.buildString(node.right, data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split(","))
        return self.buildTree(queue)

    def buildTree(self, deque):
        val = deque.popleft()
        if val == self.null:
            return None
        else:
            node = TreeNode(int(val))
            node.left = self.buildTree(deque)
            node.right = self.buildTree(deque)
            return node

"""
Algorithm:
1. serialize: Iterative BFS, Queue
2. deserialize: Iterative BFS, Queue
"""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
