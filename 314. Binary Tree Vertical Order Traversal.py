"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""
"""
Algorithm: Iterative BFS

Data structures:
1. HashTable<int col, [] root.val>:
Store column as key.
Store root.val in the list as value.
2. Queue: for Iterative BFS traversal.
Store tuple(root, col) to maintain relationship before node and column

Variables:
minCol = 0, update when find new root.left, minCol = min(minCol, col - 1)
maxCol = 0, update when find new root.right, maxCol = max(maxCol, col + 1)
result = []

Traverse HashTable from minCol to maxCol, result.append(map[i])
Return result
"""
"""
@param {TreeNode} root
@return {[[int]]}
"""
from collections import deque
def verticalOrder(root):
    if root == None:
        return []

    table = {}
    queue = deque([(root, 0)])
    minCol = 0
    maxCol = 0
    result = []

    while queue:
        root, col = queue.popleft()

        if col not in table:
            table[col] = []

        table[col].append(root.val)

        if root.left:
            queue.append((root.left, col - 1))
            minCol = min(minCol, col - 1)

        if root.right:
            queue.append((root.right, col + 1))
            maxCol = max(maxCol, col + 1)

    for i in range(minCol, maxCol + 1):
        result.append(table[i])

    return result
