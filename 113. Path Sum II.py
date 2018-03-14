"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
"""
@param {TreeNode} root
@param {int} sum
@return {int[][]}
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Algorithm: Recursive, DFS
"""
def pathSum(root, sum):
    if root == None or sum == None:
        return []

    result = []
    def dfs(root, sum, path):
        if not root.left and not root.right and root.val == sum:
            path.append(root.val)
            result.append(path)

        if root.left:
            dfs(root.left, sum - root.val, path + [root.val])

        if root.right:
            dfs(root.right, sum - root.val, path + [root.val])

    dfs(root, sum, [])
    return result

"""
Algorithm: BFS , Queue
"""
import collections
def pathSum(root, sum):
    if root == None or sum == None:
        return []

    result = []
    queue = collections.deque([])
    queue.append((root, root.val, [root.val]))
    while queue:
        current, value, path = queue.popleft()
        if not current.left and not current.right and value == sum:
            result.append(path)

        if current.left:
            queue.append((current.left, value + current.left.val, path + [current.left.val]))

        if current.right:
            queue.append((current.right, value + current.right.val, path + [current.right.val]))

    return result

"""
Algorithm: DFS, Stack
(Fastest Solution)
"""
def pathSum(root, sum):
    if root == None or sum == None:
        return []

    result = []
    stack = [(root, root.val, [root.val])]
    while stack:
        current, value, path = stack.pop()
        if not current.left and not current.right and value == sum:
            result.append(path)

        if current.right:
            stack.append((current.right, value + current.right.val, path + [current.right.val]))

        if current.left:
            stack.append((current.left, value + current.left.val, path + [current.left.val]))

    return result
