"""
Given a binary tree, find the length of the longest consecutive sequence path.
(increasing)

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""
"""
@param {TreeNode} root
@return {int}
"""
"""
Algorithm: Recursive, DFS
"""
def longestConsecutive(root):
    if root == None:
        return 0

    result = [0]

    def dfs(root, current_length):
        result[0] = max(result[0], current_length)

        if root.left:
            if root.left.val == root.val + 1:
                dfs(root.left, current_length + 1)
            else:
                dfs(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                dfs(root.right, current_length + 1)
            else:
                dfs(root.right, 1)

    dfs(root, 1)
    return result[0]

"""
Algorithm: BFS, Queue
"""
import collections
def longestConsecutive(root):
    if root == None:
        return 0

    result = [0]
    queue = collections.deque([])
    queue.append((root, 1))
    while queue:
        current_node, current_length = queue.popleft()
        result[0] = max(result[0], current_length)
        if current_node.left:
            if current_node.left.val == current_node.val + 1:
                queue.append((current_node.left, current_length + 1))
            else:
                queue.append((current_node.left, 1))

        if current_node.right:
            if current_node.right.val == current_node.val + 1:
                queue.append((current_node.right, current_length + 1))
            else:
                queue.append((current_node.right, 1))

    return result[0]

"""
Algorithm: DFS, Stack
"""
def longestConsecutive(root):
    if root == None:
        return 0

    result = [0]
    stack = [(root, 1)]
    while stack:
        current_node, current_length = stack.pop()
        result[0] = max(result[0], current_length)
        if current_node.right:
            if current_node.right.val == current_node.val + 1:
                stack.append((current_node.right, current_length + 1))
            else:
                stack.append((current_node.right, 1))

        if current_node.left:
            if current_node.left.val == current_node.val + 1:
                stack.append((current_node.left, current_length + 1))
            else:
                stack.append((current_node.left, 1))

    return result[0]
